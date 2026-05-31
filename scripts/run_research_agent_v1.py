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
from datetime import datetime
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PROMPTS_DIR = ROOT / "benchmark" / "prompts" / "research_agent_v1"
DEFAULT_OUTPUT_ROOT = ROOT / "outputs" / "raw_agent_logs" / "research_agent_v1"
RUNNER = ROOT / "scripts" / "run_isolated_packet.sh"
CLAIM_EVIDENCE_COLUMNS = (
    "claim",
    "evidence used",
    "claim type",
    "confidence",
    "what would falsify this claim",
)
JSON_BLOCK_RE = re.compile(r"```json\s*(\{.*?\})\s*```", re.DOTALL)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Run a single-case research_agent_v1 smoke test.")
    parser.add_argument("--input-file", required=True)
    parser.add_argument("--output-root", default=str(DEFAULT_OUTPUT_ROOT))
    parser.add_argument("--timeout-seconds", type=int, default=1800)
    parser.add_argument("--thinking-level", default="high")
    parser.add_argument("--start-from", choices=["stage3", "stage4", "stage5"], default="stage3")
    parser.add_argument("--run-dir", help="Existing run directory required when resuming from stage4 or stage5.")
    return parser.parse_args()


def read_text(path: Path) -> str:
    return path.read_text()


def write_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text)


def sha256_text(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def render_template(template_text: str, replacements: dict[str, str]) -> str:
    rendered = template_text
    for key, value in replacements.items():
        rendered = rendered.replace(f"{{{{{key}}}}}", value)
    return rendered


def render_stage3_prompt(template_text: str, packet_text: str) -> str:
    return render_template(
        template_text,
        {
            "PACKET_TEXT": packet_text,
            "OUTPUT_SCHEMA_HINT": '"candidates", "recommended_primary", "notes"',
        },
    )


def render_stage4_prompt(template_text: str, packet_text: str, stage3_json: str) -> str:
    return render_template(
        template_text,
        {
            "PACKET_TEXT": packet_text,
            "STAGE3_JSON": stage3_json,
        },
    )


def render_stage5_prompt(
    template_text: str,
    packet_text: str,
    stage3_json: str,
    stage4_critique: str,
) -> str:
    return render_template(
        template_text,
        {
            "PACKET_TEXT": packet_text,
            "STAGE3_JSON": stage3_json,
            "STAGE4_CRITIQUE": stage4_critique,
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
        "agent_variant": "research_agent_v1",
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


def run_openclaw_prompt(prompt_text: str, stage_dir: Path, timeout_seconds: int, thinking_level: str) -> str:
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
        return extract_payload_text(data)
    finally:
        temp_prompt_path.unlink(missing_ok=True)


def append_retry_log(stage_dir: Path, attempt: int, message: str) -> None:
    retry_log = stage_dir / "retry_log.txt"
    existing = retry_log.read_text() if retry_log.exists() else ""
    new_line = f"attempt={attempt}: {message}\n"
    write_text(retry_log, existing + new_line)


def build_runner_env(thinking_level: str) -> dict[str, str]:
    env = dict(os.environ)
    env["THINKING_LEVEL"] = thinking_level
    return env


def run_stage_with_retry(
    stage_name: str,
    stage_dir: Path,
    render_prompt,
    validate_output,
    timeout_seconds: int,
    thinking_level: str,
) -> tuple[object, float, int]:
    last_error = None
    for attempt in range(2):
        start = time.time()
        prompt_text = render_prompt()
        try:
            raw_text = run_openclaw_prompt(prompt_text, stage_dir, timeout_seconds, thinking_level)
            artifact = validate_output(raw_text)
            duration = round(time.time() - start, 3)
            return artifact, duration, attempt
        except Exception as exc:  # noqa: BLE001
            last_error = exc
            append_retry_log(stage_dir, attempt + 1, str(exc))
    raise RuntimeError(f"{stage_name} failed after retry: {last_error}") from last_error


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
) -> dict[str, object]:
    payload = {
        "status": status,
        "retries": retries,
        "artifact_path": artifact_path,
        "duration_sec": duration,
        "validation": validation,
    }
    if stderr_path:
        payload["stderr_path"] = stderr_path
    return payload


def main() -> None:
    args = parse_args()
    input_file = Path(args.input_file).resolve()
    packet_text = read_text(input_file)
    case_id, variant_id = parse_case_and_variant(input_file)

    if args.start_from == "stage3":
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
            raise SystemExit("--run-dir is required when resuming from stage4 or stage5.")
        run_dir = Path(args.run_dir).resolve()
        if not run_dir.exists():
            raise SystemExit(f"Run directory not found: {run_dir}")

    manifest_path = run_dir / "pipeline_manifest.json"
    pipeline_failed = False

    try:
        stage3_template = read_text(PROMPTS_DIR / "stage3_candidates.md")
        stage4_template = read_text(PROMPTS_DIR / "stage4_critique.md")
        stage5_template = read_text(PROMPTS_DIR / "stage5_final.md")

        stage3_data = None
        if args.start_from in {"stage3"}:
            stage3_dir = run_dir / "stage3_candidates"
            stage3_data, stage3_duration, stage3_retries = run_stage_with_retry(
                "stage3_candidates",
                stage3_dir,
                lambda: render_stage3_prompt(stage3_template, packet_text),
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

        critique_md = None
        critique_meta = None
        if args.start_from in {"stage3", "stage4"}:
            stage4_dir = run_dir / "stage4_critique"
            stage3_json = json.dumps(stage3_data, indent=2, ensure_ascii=False)

            def validate_stage4(raw_text: str) -> tuple[str, dict[str, object]]:
                return parse_stage4_output(raw_text)

            (critique_md, critique_meta), stage4_duration, stage4_retries = run_stage_with_retry(
                "stage4_critique",
                stage4_dir,
                lambda: render_stage4_prompt(stage4_template, packet_text, stage3_json),
                validate_stage4,
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
        stage3_json = json.dumps(stage3_data, indent=2, ensure_ascii=False)
        final_md, stage5_duration, stage5_retries = run_stage_with_retry(
            "stage5_final",
            stage5_dir,
            lambda: render_stage5_prompt(stage5_template, packet_text, stage3_json, critique_md),
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
                f"recommend_descriptive_fallback={critique_meta.get('recommend_descriptive_fallback')}",
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
