#!/usr/bin/env python3

from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import subprocess
import sys
import tempfile
import time
import urllib.parse
import urllib.request
from datetime import datetime
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PROMPTS_DIR = ROOT / "benchmark" / "prompts" / "research_agent_v2"
DEFAULT_OUTPUT_ROOT = ROOT / "outputs" / "raw_agent_logs" / "research_agent_v2"
RUNNER = ROOT / "scripts" / "run_isolated_packet.sh"
LOCAL_ENV_PATH = ROOT / ".benchmark.local.env"
CLAIM_EVIDENCE_COLUMNS = (
    "claim",
    "evidence used",
    "claim type",
    "confidence",
    "what would falsify this claim",
)
JSON_BLOCK_RE = re.compile(r"```json\s*(\{.*?\})\s*```", re.DOTALL)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Run a single-case research_agent_v2 smoke test.")
    parser.add_argument("--input-file", required=True)
    parser.add_argument("--output-root", default=str(DEFAULT_OUTPUT_ROOT))
    parser.add_argument("--timeout-seconds", type=int, default=1800)
    parser.add_argument("--thinking-level", default="high")
    parser.add_argument("--start-from", choices=["stage2", "stage3", "stage4", "stage5"], default="stage2")
    parser.add_argument("--run-dir", help="Existing run directory required when resuming from a later stage.")
    return parser.parse_args()


def read_text(path: Path) -> str:
    return path.read_text()


def write_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text)


def load_local_env_file(env_path: Path = LOCAL_ENV_PATH) -> dict[str, str]:
    if not env_path.exists():
        return {}
    loaded: dict[str, str] = {}
    for raw_line in env_path.read_text().splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, value = line.split("=", 1)
        key = key.strip()
        value = value.strip()
        if not key:
            continue
        if len(value) >= 2 and value[0] == value[-1] and value[0] in {"'", '"'}:
            value = value[1:-1]
        loaded[key] = value
    return loaded


def ensure_local_env_loaded() -> None:
    local_values = load_local_env_file()
    for key, value in local_values.items():
        os.environ.setdefault(key, value)


def sha256_text(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def render_template(template_text: str, replacements: dict[str, str]) -> str:
    rendered = template_text
    for key, value in replacements.items():
        rendered = rendered.replace(f"{{{{{key}}}}}", value)
    return rendered


def render_stage2_prompt(
    template_text: str,
    packet_text: str,
    openalex_seed_json: str,
    mandatory_first_query: str,
) -> str:
    schema = """{
  "queries": ["query 1", "query 2"],
  "sources_consulted": ["openalex", "deepxiv"],
  "tools_attempted": ["deepxiv__search_papers"],
  "tool_attempt_count": 1,
  "tool_success_count": 1,
  "retrieval_attempted": true,
  "retrieval_successful": true,
  "failure_reason": null,
  "method_fragility_findings": ["finding 1"],
  "design_fallback_findings": ["finding 2"],
  "packet_relevant_takeaways": ["takeaway 1"],
  "evidence_items": [
    {
      "source": "openalex",
      "query": "query 1",
      "title": "paper title",
      "identifier": "https://openalex.org/W123",
      "relevance_note": "why it matters for the packet"
    }
  ]
}"""
    return render_template(
        template_text,
        {
            "PACKET_TEXT": packet_text,
            "OPENALEX_SEED_JSON": openalex_seed_json,
            "MANDATORY_FIRST_QUERY": mandatory_first_query,
            "RETRIEVAL_OUTPUT_SCHEMA_HINT": schema,
        },
    )


def render_stage3_prompt(template_text: str, packet_text: str, stage2_json: str, openalex_seed_json: str) -> str:
    return render_template(
        template_text,
        {
            "PACKET_TEXT": packet_text,
            "STAGE2_JSON": stage2_json,
            "OPENALEX_SEED_JSON": openalex_seed_json,
        },
    )


def render_stage4_prompt(
    template_text: str,
    packet_text: str,
    stage2_json: str,
    stage3_json: str,
    openalex_seed_json: str,
) -> str:
    return render_template(
        template_text,
        {
            "PACKET_TEXT": packet_text,
            "STAGE2_JSON": stage2_json,
            "STAGE3_JSON": stage3_json,
            "OPENALEX_SEED_JSON": openalex_seed_json,
        },
    )


def render_stage5_prompt(
    template_text: str,
    packet_text: str,
    stage2_json: str,
    stage3_json: str,
    stage4_critique: str,
    openalex_seed_json: str,
) -> str:
    return render_template(
        template_text,
        {
            "PACKET_TEXT": packet_text,
            "STAGE2_JSON": stage2_json,
            "STAGE3_JSON": stage3_json,
            "STAGE4_CRITIQUE": stage4_critique,
            "OPENALEX_SEED_JSON": openalex_seed_json,
        },
    )


def extract_payload_text(data: dict) -> str:
    payloads = data.get("payloads") or []
    text_parts = []
    for payload in payloads:
        if isinstance(payload, dict):
            text = payload.get("text")
            if text:
                text_parts.append(text)
    if text_parts:
        return "\n\n".join(text_parts).strip()
    meta = data.get("meta", {})
    return (meta.get("finalAssistantVisibleText") or "").strip()


def strip_optional_json_fence(text: str) -> str:
    stripped = text.strip()
    if stripped.startswith("```json") and stripped.endswith("```"):
        return stripped[len("```json") : -3].strip()
    if stripped.startswith("```") and stripped.endswith("```"):
        return stripped[3:-3].strip()
    return stripped


def validate_stage2_output(raw_text: str) -> dict[str, object]:
    cleaned = strip_optional_json_fence(raw_text)
    try:
        parsed = json.loads(cleaned)
    except json.JSONDecodeError as exc:
        raise ValueError(f"Stage 2 output is not valid JSON: {exc}") from exc

    required_keys = {
        "queries",
        "sources_consulted",
        "tools_attempted",
        "tool_attempt_count",
        "tool_success_count",
        "retrieval_attempted",
        "retrieval_successful",
        "failure_reason",
        "method_fragility_findings",
        "design_fallback_findings",
        "packet_relevant_takeaways",
        "evidence_items",
    }
    missing = sorted(required_keys - set(parsed))
    if missing:
        raise ValueError(f"Stage 2 output is missing required keys: {', '.join(missing)}")
    if parsed.get("retrieval_attempted") is not True:
        raise ValueError("Stage 2 output must record retrieval_attempted=true.")
    if not isinstance(parsed.get("packet_relevant_takeaways"), list):
        raise ValueError("Stage 2 output must contain packet_relevant_takeaways as a list.")
    if not isinstance(parsed.get("sources_consulted"), list):
        raise ValueError("Stage 2 output must contain sources_consulted as a list.")
    if not isinstance(parsed.get("evidence_items"), list):
        raise ValueError("Stage 2 output must contain evidence_items as a list.")
    return parsed


def build_openalex_url(query: str, api_key: str, email: str, per_page: int = 5) -> str:
    params = {
        "search": query,
        "per-page": str(per_page),
        "select": "id,display_name,publication_year,cited_by_count,primary_location,best_oa_location,authorships",
        "api_key": api_key,
        "mailto": email,
    }
    return "https://api.openalex.org/works?" + urllib.parse.urlencode(params)


def build_openalex_seed_query(packet_text: str) -> str:
    heading_patterns = (
        "## Research Background",
        "## Research Objective",
        "## Perturbed Condition",
        "## Specific Questions To Answer",
    )
    focused_sections = []
    for pattern in heading_patterns:
        start = packet_text.find(pattern)
        if start == -1:
            continue
        next_heading = packet_text.find("\n## ", start + len(pattern))
        if next_heading == -1:
            next_heading = len(packet_text)
        focused_sections.append(packet_text[start:next_heading])

    seed_text = "\n".join(focused_sections) if focused_sections else packet_text
    seed_text = re.sub(r"<!--.*?-->", " ", seed_text, flags=re.DOTALL)
    stopwords = {
        "agent",
        "answer",
        "about",
        "advance",
        "after",
        "among",
        "anonymous",
        "approach",
        "causal",
        "because",
        "before",
        "between",
        "business",
        "condition",
        "could",
        "design",
        "effect",
        "economics",
        "field",
        "facing",
        "household",
        "households",
        "identification",
        "information",
        "interaction",
        "notice",
        "design",
        "effect",
        "identification",
        "inperson",
        "observe",
        "outcome",
        "packet",
        "people",
        "person",
        "precontact",
        "problem",
        "provided",
        "question",
        "questions",
        "receive",
        "request",
        "research",
        "setting",
        "solicitation",
        "should",
        "stage",
        "study",
        "support",
        "their",
        "there",
        "these",
        "those",
        "through",
        "units",
        "under",
        "using",
        "variant",
        "visibility",
        "whether",
        "which",
        "window",
        "which",
        "would",
    }
    words = re.findall(r"[A-Za-z][A-Za-z\\-]{4,}", seed_text.lower())
    picked = []
    for word in words:
        if word in stopwords or word in picked:
            continue
        picked.append(word)
        if len(picked) >= 6:
            break
    query_terms = picked or ["donation", "fundraising", "social", "pressure"]
    return " ".join(query_terms[:6]) + " empirical identification"


def fetch_openalex_seed(packet_text: str) -> dict[str, object]:
    ensure_local_env_loaded()
    api_key = os.environ.get("OPENALEX_API_KEY", "").strip()
    email = os.environ.get("OPENALEX_EMAIL", "").strip()
    query = build_openalex_seed_query(packet_text)
    if not api_key or not email:
        return {
            "available": False,
            "query": query,
            "failure_reason": "missing_openalex_credentials",
            "results": [],
        }

    url = build_openalex_url(query=query, api_key=api_key, email=email, per_page=5)
    try:
        with urllib.request.urlopen(url, timeout=30) as response:
            payload = json.loads(response.read().decode("utf-8"))
    except Exception as exc:  # noqa: BLE001
        return {
            "available": False,
            "query": query,
            "failure_reason": str(exc),
            "results": [],
        }

    results = []
    for item in payload.get("results", [])[:5]:
        results.append(
            {
                "id": item.get("id"),
                "title": item.get("display_name"),
                "publication_year": item.get("publication_year"),
                "cited_by_count": item.get("cited_by_count"),
            }
        )

    return {
        "available": True,
        "query": query,
        "failure_reason": None,
        "results": results,
    }


def validate_stage3_output(raw_text: str) -> dict[str, object]:
    cleaned = strip_optional_json_fence(raw_text)
    try:
        parsed = json.loads(cleaned)
    except json.JSONDecodeError as exc:
        raise ValueError(f"Stage 3 output is not valid JSON: {exc}") from exc
    candidates = parsed.get("candidates")
    if not isinstance(candidates, list):
        raise ValueError("Stage 3 output must contain a candidates list.")
    if len(candidates) < 3:
        raise ValueError("Stage 3 output must contain at least 3 candidates.")
    return parsed


def parse_stage4_output(raw_text: str) -> tuple[str, dict[str, object]]:
    matches = list(JSON_BLOCK_RE.finditer(raw_text))
    if not matches:
        raise ValueError("Stage 4 output must end with a fenced JSON block.")
    last_match = matches[-1]
    critique_md = raw_text[: last_match.start()].rstrip() + "\n"
    try:
        meta = json.loads(last_match.group(1))
    except json.JSONDecodeError as exc:
        raise ValueError(f"Stage 4 meta JSON is invalid: {exc}") from exc
    return critique_md, meta


def validate_stage5_output(raw_text: str) -> bool:
    for line in raw_text.splitlines():
        if not line.strip().startswith("|"):
            continue
        cells = [cell.strip().lower() for cell in line.strip().strip("|").split("|")]
        if tuple(cells) == CLAIM_EVIDENCE_COLUMNS:
            return True
    raise ValueError("Stage 5 output must contain the canonical claim-evidence table header.")


def initialize_pipeline_manifest(
    manifest_path: Path,
    case_id: str,
    variant_id: str,
    input_packet_sha256: str,
) -> None:
    data = {
        "case_id": case_id,
        "variant_id": variant_id,
        "agent_variant": "research_agent_v2_search",
        "input_packet_sha256": input_packet_sha256,
        "stages": {},
        "pipeline_failed": False,
        "created_at": datetime.now().isoformat(),
    }
    write_text(manifest_path, json.dumps(data, indent=2, ensure_ascii=False) + "\n")


def update_pipeline_manifest(
    manifest_path: Path,
    stage_name: str,
    stage_status: dict[str, object],
) -> None:
    manifest = json.loads(manifest_path.read_text())
    manifest.setdefault("stages", {})[stage_name] = stage_status
    write_text(manifest_path, json.dumps(manifest, indent=2, ensure_ascii=False) + "\n")


def finalize_pipeline_manifest(manifest_path: Path, pipeline_failed: bool) -> None:
    manifest = json.loads(manifest_path.read_text())
    manifest["pipeline_failed"] = pipeline_failed
    manifest["completed_at"] = datetime.now().isoformat()
    write_text(manifest_path, json.dumps(manifest, indent=2, ensure_ascii=False) + "\n")


def parse_case_and_variant(input_file: Path) -> tuple[str, str]:
    case_match = re.search(r"(C\d{3})_", input_file.as_posix())
    if not case_match:
        raise ValueError(f"Could not infer case id from input path: {input_file}")
    case_id = case_match.group(1)
    name = input_file.name
    if name.startswith("agent_task_") and name.endswith(".md"):
        variant_id = name[len("agent_task_") : -len(".md")]
    else:
        raise ValueError(f"Could not infer variant id from input file name: {input_file.name}")
    return case_id, variant_id


def create_run_dir(output_root: Path, case_id: str, variant_id: str) -> Path:
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    run_dir = output_root / f"{case_id}_{variant_id}_{timestamp}"
    run_dir.mkdir(parents=True, exist_ok=False)
    return run_dir


def build_runner_env(thinking_level: str) -> dict[str, str]:
    env = dict(os.environ)
    env["THINKING_LEVEL"] = thinking_level
    return env


def count_tool_calls_from_session(session_file: Path) -> dict[str, int]:
    """Count actual tool activity from an OpenClaw session transcript.

    OpenClaw records tool use as assistant messages whose ``content`` contains
    ``toolCall`` blocks, plus separate top-level messages with ``role`` of
    ``toolResult``. This is the authoritative source of truth.
    """
    tool_calls = 0
    tool_results = 0
    for line in session_file.read_text().splitlines():
        line = line.strip()
        if not line:
            continue
        try:
            entry = json.loads(line)
        except json.JSONDecodeError:
            continue
        if entry.get("type") != "message":
            continue
        message = entry.get("message") or entry
        if message.get("role") == "toolResult":
            tool_results += 1
            continue
        content = message.get("content")
        if isinstance(content, list):
            for block in content:
                if isinstance(block, dict) and block.get("type") == "toolCall":
                    tool_calls += 1
    return {"tool_calls": tool_calls, "tool_results": tool_results}


def extract_tool_call_counts(data: dict) -> dict[str, int]:
    meta = data.get("meta") or {}

    # Preferred source: the session transcript referenced by the run. Current
    # OpenClaw `--json` output does NOT include a top-level "messages" array or
    # a populated meta.toolMetas, so tool activity can only be counted from the
    # session jsonl file.
    session_file = ((meta.get("agentMeta") or {}).get("sessionFile"))
    if session_file:
        session_path = Path(session_file)
        if session_path.exists():
            return count_tool_calls_from_session(session_path)

    # Fallback for older/alternative `--json` schemas.
    tool_calls = 0
    tool_results = 0
    for entry in data.get("messages") or []:
        if not isinstance(entry, dict):
            continue
        entry_type = entry.get("type", "")
        if entry_type == "toolCall":
            tool_calls += 1
        elif entry_type == "toolResult":
            tool_results += 1

    tool_metas = meta.get("toolMetas") or []
    if tool_calls == 0 and tool_metas:
        tool_calls = len(tool_metas)
    return {"tool_calls": tool_calls, "tool_results": tool_results}


def run_openclaw_prompt(prompt_text: str, stage_dir: Path, timeout_seconds: int, thinking_level: str) -> tuple[str, dict, dict[str, int]]:
    stage_dir.mkdir(parents=True, exist_ok=True)
    prompt_path = stage_dir / "prompt.md"
    raw_json_path = stage_dir / "raw_openclaw.json"
    stderr_path = stage_dir / "stderr.log"
    write_text(prompt_path, prompt_text)

    with tempfile.NamedTemporaryFile("w", suffix=".md", delete=False) as handle:
        handle.write(prompt_text)
        temp_prompt_path = Path(handle.name)

    try:
        command = [
            str(RUNNER),
            str(temp_prompt_path),
            str(timeout_seconds),
        ]
        env = build_runner_env(thinking_level)
        result = subprocess.run(
            command,
            cwd=ROOT,
            capture_output=True,
            text=True,
            env=env,
            check=False,
        )
        write_text(raw_json_path, result.stdout)
        write_text(stderr_path, result.stderr)
        if result.returncode != 0:
            raise RuntimeError(
                f"OpenClaw stage failed with exit code {result.returncode}: {result.stderr.strip()}"
            )
        data = json.loads(result.stdout)
        return extract_payload_text(data), data, extract_tool_call_counts(data)
    finally:
        temp_prompt_path.unlink(missing_ok=True)


def append_retry_log(stage_dir: Path, attempt: int, message: str) -> None:
    retry_log = stage_dir / "retry_log.txt"
    existing = retry_log.read_text() if retry_log.exists() else ""
    write_text(retry_log, existing + f"attempt={attempt}: {message}\n")


def run_stage_with_retry(
    stage_name: str,
    stage_dir: Path,
    render_prompt,
    validate_output,
    timeout_seconds: int,
    thinking_level: str,
) -> tuple[object, float, int, dict[str, int]]:
    last_error = None
    for attempt in range(2):
        start = time.time()
        prompt_text = render_prompt()
        try:
            raw_text, data, tool_counts = run_openclaw_prompt(prompt_text, stage_dir, timeout_seconds, thinking_level)
            artifact = validate_output(raw_text)
            duration = round(time.time() - start, 3)
            return artifact, duration, attempt, tool_counts
        except Exception as exc:  # noqa: BLE001
            last_error = exc
            append_retry_log(stage_dir, attempt + 1, str(exc))
    raise RuntimeError(f"{stage_name} failed after retry: {last_error}") from last_error


def save_stage2_artifacts(stage_dir: Path, artifact: dict[str, object]) -> tuple[Path, Path]:
    artifact_path = stage_dir / "artifact.json"
    summary_path = stage_dir / "evidence_summary.md"
    write_text(artifact_path, json.dumps(artifact, indent=2, ensure_ascii=False) + "\n")
    summary_lines = [
        "# Stage 2 Retrieval Summary",
        "",
        f"- retrieval_attempted: `{artifact['retrieval_attempted']}`",
        f"- retrieval_successful: `{artifact['retrieval_successful']}`",
        f"- tool_attempt_count: `{artifact['tool_attempt_count']}`",
        f"- tool_success_count: `{artifact['tool_success_count']}`",
        f"- failure_reason: `{artifact['failure_reason']}`",
        "",
        "## Packet-Relevant Takeaways",
    ]
    for item in artifact.get("packet_relevant_takeaways", []):
        summary_lines.append(f"- {item}")
    write_text(summary_path, "\n".join(summary_lines) + "\n")
    return artifact_path, summary_path


def save_openalex_seed(stage_dir: Path, seed: dict[str, object]) -> Path:
    seed_path = stage_dir / "openalex_seed.json"
    write_text(seed_path, json.dumps(seed, indent=2, ensure_ascii=False) + "\n")
    return seed_path


def save_stage3_artifact(stage_dir: Path, artifact: dict[str, object]) -> Path:
    artifact_path = stage_dir / "artifact.json"
    write_text(artifact_path, json.dumps(artifact, indent=2, ensure_ascii=False) + "\n")
    return artifact_path


def save_stage4_artifact(stage_dir: Path, critique_md: str, critique_meta: dict[str, object]) -> tuple[Path, Path]:
    critique_path = stage_dir / "artifact.md"
    meta_path = stage_dir / "artifact.meta.json"
    write_text(critique_path, critique_md)
    write_text(meta_path, json.dumps(critique_meta, indent=2, ensure_ascii=False) + "\n")
    return critique_path, meta_path


def save_stage5_artifact(stage_dir: Path, final_md: str) -> Path:
    artifact_path = stage_dir / "artifact.md"
    write_text(artifact_path, final_md)
    return artifact_path


def stage_status(
    status: str,
    retries: int,
    artifact_path: str,
    duration: float,
    validation: str,
    stderr_path: str | None = None,
    retrieval_attempted: bool | None = None,
    retrieval_successful: bool | None = None,
    retrieval_tool_calls: int | None = None,
    retrieval_failure_reason: str | None = None,
) -> dict[str, object]:
    payload: dict[str, object] = {
        "status": status,
        "retries": retries,
        "artifact_path": artifact_path,
        "duration_sec": duration,
        "validation": validation,
    }
    if stderr_path:
        payload["stderr_path"] = stderr_path
    if retrieval_attempted is not None:
        payload["retrieval_attempted"] = retrieval_attempted
    if retrieval_successful is not None:
        payload["retrieval_successful"] = retrieval_successful
    if retrieval_tool_calls is not None:
        payload["retrieval_tool_calls"] = retrieval_tool_calls
    if retrieval_failure_reason is not None:
        payload["retrieval_failure_reason"] = retrieval_failure_reason
    return payload


def normalize_stage2_artifact(artifact: dict[str, object], tool_counts: dict[str, int]) -> dict[str, object]:
    normalized = dict(artifact)
    normalized["tool_attempt_count"] = max(int(normalized.get("tool_attempt_count", 0)), tool_counts["tool_calls"])
    normalized["tool_success_count"] = max(int(normalized.get("tool_success_count", 0)), tool_counts["tool_results"])
    if tool_counts["tool_calls"] == 0:
        normalized["retrieval_successful"] = False
        if not normalized.get("failure_reason"):
            normalized["failure_reason"] = "no_actual_tool_use_recorded"
    return normalized


def main() -> None:
    args = parse_args()
    input_file = Path(args.input_file).resolve()
    packet_text = read_text(input_file)
    case_id, variant_id = parse_case_and_variant(input_file)

    if args.start_from == "stage2":
        run_dir = create_run_dir(Path(args.output_root), case_id, variant_id)
        write_text(run_dir / "input_packet.md", packet_text)
        initialize_pipeline_manifest(
            manifest_path=run_dir / "pipeline_manifest.json",
            case_id=case_id,
            variant_id=variant_id,
            input_packet_sha256=sha256_text(packet_text),
        )
        manifest = json.loads((run_dir / "pipeline_manifest.json").read_text())
        manifest["source_input_file"] = input_file.relative_to(ROOT).as_posix()
        write_text(run_dir / "pipeline_manifest.json", json.dumps(manifest, indent=2, ensure_ascii=False) + "\n")
    else:
        if not args.run_dir:
            raise SystemExit("--run-dir is required when resuming from a later stage.")
        run_dir = Path(args.run_dir).resolve()
        if not run_dir.exists():
            raise SystemExit(f"Run directory not found: {run_dir}")

    manifest_path = run_dir / "pipeline_manifest.json"
    pipeline_failed = False

    try:
        stage2_template = read_text(PROMPTS_DIR / "stage2_retrieval.md")
        stage3_template = read_text(PROMPTS_DIR / "stage3_candidates.md")
        stage4_template = read_text(PROMPTS_DIR / "stage4_critique.md")
        stage5_template = read_text(PROMPTS_DIR / "stage5_final.md")
        openalex_seed = fetch_openalex_seed(packet_text)
        openalex_seed_json = json.dumps(openalex_seed, indent=2, ensure_ascii=False)
        mandatory_first_query = str(openalex_seed.get("query") or build_openalex_seed_query(packet_text))

        if args.start_from == "stage2":
            stage2_dir = run_dir / "stage2_retrieval"
            openalex_seed_path = save_openalex_seed(stage2_dir, openalex_seed)
            stage2_data, stage2_duration, stage2_retries, stage2_tool_counts = run_stage_with_retry(
                "stage2_retrieval",
                stage2_dir,
                lambda: render_stage2_prompt(
                    stage2_template,
                    packet_text,
                    openalex_seed_json,
                    mandatory_first_query,
                ),
                validate_stage2_output,
                args.timeout_seconds,
                args.thinking_level,
            )
            stage2_data = normalize_stage2_artifact(stage2_data, stage2_tool_counts)
            stage2_artifact_path, stage2_summary_path = save_stage2_artifacts(stage2_dir, stage2_data)
            if stage2_tool_counts["tool_calls"] == 0:
                update_pipeline_manifest(
                    manifest_path,
                    "stage2_retrieval",
                    stage_status(
                        "invalid",
                        stage2_retries,
                        stage2_artifact_path.relative_to(run_dir).as_posix(),
                        stage2_duration,
                        (
                            f"summary_path={stage2_summary_path.relative_to(run_dir).as_posix()}; "
                            f"openalex_seed_path={openalex_seed_path.relative_to(run_dir).as_posix()}"
                        ),
                        stderr_path=(stage2_dir / "stderr.log").relative_to(run_dir).as_posix(),
                        retrieval_attempted=bool(stage2_data.get("retrieval_attempted")),
                        retrieval_successful=bool(stage2_data.get("retrieval_successful")),
                        retrieval_tool_calls=int(stage2_tool_counts["tool_calls"]),
                        retrieval_failure_reason=stage2_data.get("failure_reason"),
                    ),
                )
                raise RuntimeError("Stage 2 is invalid: no actual retrieval tool call was recorded.")
            update_pipeline_manifest(
                manifest_path,
                "stage2_retrieval",
                stage_status(
                    "ok",
                    stage2_retries,
                    stage2_artifact_path.relative_to(run_dir).as_posix(),
                    stage2_duration,
                    (
                        f"summary_path={stage2_summary_path.relative_to(run_dir).as_posix()}; "
                        f"openalex_seed_path={openalex_seed_path.relative_to(run_dir).as_posix()}"
                    ),
                    stderr_path=(stage2_dir / "stderr.log").relative_to(run_dir).as_posix(),
                    retrieval_attempted=bool(stage2_data.get("retrieval_attempted")),
                    retrieval_successful=bool(stage2_data.get("retrieval_successful")),
                    retrieval_tool_calls=int(stage2_tool_counts["tool_calls"]),
                    retrieval_failure_reason=stage2_data.get("failure_reason"),
                ),
            )
        else:
            stage2_data = json.loads((run_dir / "stage2_retrieval" / "artifact.json").read_text())

        stage2_json = json.dumps(stage2_data, indent=2, ensure_ascii=False)

        if args.start_from in {"stage2", "stage3"}:
            stage3_dir = run_dir / "stage3_candidates"
            stage3_data, stage3_duration, stage3_retries, _stage3_tool_counts = run_stage_with_retry(
                "stage3_candidates",
                stage3_dir,
                lambda: render_stage3_prompt(stage3_template, packet_text, stage2_json, openalex_seed_json),
                validate_stage3_output,
                args.timeout_seconds,
                args.thinking_level,
            )
            stage3_artifact_path = save_stage3_artifact(stage3_dir, stage3_data)
            update_pipeline_manifest(
                manifest_path,
                "stage3_candidates",
                stage_status(
                    "ok",
                    stage3_retries,
                    stage3_artifact_path.relative_to(run_dir).as_posix(),
                    stage3_duration,
                    f"n_candidates={len(stage3_data['candidates'])}",
                    stderr_path=(stage3_dir / "stderr.log").relative_to(run_dir).as_posix(),
                ),
            )
        else:
            stage3_data = json.loads((run_dir / "stage3_candidates" / "artifact.json").read_text())

        stage3_json = json.dumps(stage3_data, indent=2, ensure_ascii=False)

        if args.start_from in {"stage2", "stage3", "stage4"}:
            stage4_dir = run_dir / "stage4_critique"
            (critique_md, critique_meta), stage4_duration, stage4_retries, _stage4_tool_counts = run_stage_with_retry(
                "stage4_critique",
                stage4_dir,
                lambda: render_stage4_prompt(stage4_template, packet_text, stage2_json, stage3_json, openalex_seed_json),
                parse_stage4_output,
                args.timeout_seconds,
                args.thinking_level,
            )
            critique_path, meta_path = save_stage4_artifact(stage4_dir, critique_md, critique_meta)
            update_pipeline_manifest(
                manifest_path,
                "stage4_critique",
                stage_status(
                    "ok",
                    stage4_retries,
                    critique_path.relative_to(run_dir).as_posix(),
                    stage4_duration,
                    f"meta_path={meta_path.relative_to(run_dir).as_posix()}",
                    stderr_path=(stage4_dir / "stderr.log").relative_to(run_dir).as_posix(),
                ),
            )
        else:
            critique_md = (run_dir / "stage4_critique" / "artifact.md").read_text()
            critique_meta = json.loads((run_dir / "stage4_critique" / "artifact.meta.json").read_text())

        stage5_dir = run_dir / "stage5_final"
        final_md, stage5_duration, stage5_retries, _stage5_tool_counts = run_stage_with_retry(
            "stage5_final",
            stage5_dir,
            lambda: render_stage5_prompt(stage5_template, packet_text, stage2_json, stage3_json, critique_md, openalex_seed_json),
            lambda raw_text: raw_text if validate_stage5_output(raw_text) else raw_text,
            args.timeout_seconds,
            args.thinking_level,
        )
        stage5_artifact_path = save_stage5_artifact(stage5_dir, final_md)
        update_pipeline_manifest(
            manifest_path,
            "stage5_final",
            stage_status(
                "ok",
                stage5_retries,
                stage5_artifact_path.relative_to(run_dir).as_posix(),
                stage5_duration,
                (
                    "recommend_descriptive_fallback="
                    f"{critique_meta.get('recommend_descriptive_fallback')}; "
                    f"retrieval_successful={stage2_data.get('retrieval_successful')}"
                ),
                stderr_path=(stage5_dir / "stderr.log").relative_to(run_dir).as_posix(),
            ),
        )
    except Exception as exc:  # noqa: BLE001
        pipeline_failed = True
        update_pipeline_manifest(
            manifest_path,
            "pipeline_error",
            {"status": "failed", "message": str(exc)},
        )
        raise
    finally:
        finalize_pipeline_manifest(manifest_path, pipeline_failed=pipeline_failed)


if __name__ == "__main__":
    try:
        main()
    except Exception as exc:  # noqa: BLE001
        print(str(exc), file=sys.stderr)
        raise SystemExit(1) from exc
