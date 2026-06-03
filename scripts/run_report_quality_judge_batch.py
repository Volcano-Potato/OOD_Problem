from __future__ import annotations

import argparse
import csv
import json
import os
import time
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
LOCAL_ENV_PATH = REPO_ROOT / ".benchmark.local.env"
DEFAULT_PACKET_MANIFEST_PATH = REPO_ROOT / "outputs" / "report_quality_judge_packets" / "judge_packet_manifest.csv"
DEFAULT_RAW_ROOT = REPO_ROOT / "outputs" / "report_quality_judge_raw"
DEFAULT_RESPONSE_MANIFEST_PATH = DEFAULT_RAW_ROOT / "response_manifest.csv"
DEFAULT_AXIS_A_SCORES_PATH = REPO_ROOT / "results" / "report_quality_axis_a_scores.csv"
DEFAULT_AXIS_A_RANKINGS_PATH = REPO_ROOT / "results" / "report_quality_axis_a_rankings.csv"
DEFAULT_AXIS_A_PAIRWISE_PATH = REPO_ROOT / "results" / "report_quality_axis_a_pairwise_vs_baseline.csv"
DEFAULT_AXIS_B_SCORES_PATH = REPO_ROOT / "results" / "report_quality_axis_b_scores.csv"
DEFAULT_GEMINI_BASE_URL = "https://api.aigocode.com/v1beta"
DEFAULT_ANTHROPIC_BASE_URL = "https://api.aigocode.com/v1"
DEFAULT_ANTHROPIC_VERSION = "2023-06-01"

ABSOLUTE_FIELDS = [
    "ceiling_respected",
    "core_failure_present",
    "estimand_clarity",
    "identification_alignment",
    "assumption_explicitness",
    "threat_coverage",
    "downgrade_discipline",
    "measurement_caution",
    "mechanism_restraint",
    "claim_evidence_traceability",
    "fatal_flaw_present",
    "mechanical_reuse_present",
    "explicit_non_claims_present",
    "fallback_design_present",
    "overall_recommendation",
    "short_reason",
]

RANKING_FIELDS = [
    "ranking",
    "top_choice",
    "bottom_choice",
    "closest_pair",
    "main_separator",
    "top_choice_reason",
]

PAIRWISE_FIELDS = [
    "winner",
    "confidence",
    "better_boundary_report",
    "better_downgrade_report",
    "mechanical_reuse_present_A",
    "mechanical_reuse_present_B",
    "reason_tags",
    "short_reason",
]


def load_local_env_file(env_path: Path = LOCAL_ENV_PATH) -> dict[str, str]:
    if not env_path.exists():
        return {}
    loaded: dict[str, str] = {}
    for raw_line in env_path.read_text(encoding="utf-8").splitlines():
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


def ensure_local_env_loaded(env_path: Path = LOCAL_ENV_PATH) -> None:
    for key, value in load_local_env_file(env_path).items():
        os.environ.setdefault(key, value)


def normalize_provider(provider: str) -> str:
    normalized = provider.strip().lower()
    if normalized not in {"gemini", "anthropic"}:
        raise ValueError(f"Unsupported provider: {provider}")
    return normalized


def default_base_url_for_provider(provider: str) -> str:
    normalized = normalize_provider(provider)
    if normalized == "anthropic":
        return DEFAULT_ANTHROPIC_BASE_URL
    return DEFAULT_GEMINI_BASE_URL


def build_generate_content_url(base_url: str, model: str, api_key: str) -> str:
    normalized = base_url.rstrip("/")
    if not normalized.endswith("/v1beta"):
        normalized = normalized + "/v1beta"
    model_path = urllib.parse.quote(model, safe=".-_")
    return f"{normalized}/models/{model_path}:generateContent?key={urllib.parse.quote(api_key, safe='')}"


def build_anthropic_messages_url(base_url: str) -> str:
    normalized = base_url.rstrip("/")
    if not normalized.endswith("/v1"):
        normalized = normalized + "/v1"
    return f"{normalized}/messages"


def build_request_url(provider: str, base_url: str, model: str, api_key: str) -> str:
    normalized = normalize_provider(provider)
    if normalized == "anthropic":
        return build_anthropic_messages_url(base_url)
    return build_generate_content_url(base_url=base_url, model=model, api_key=api_key)


def build_request_payload(judge_request_text: str, provider: str, model: str) -> dict:
    normalized = normalize_provider(provider)
    if normalized == "anthropic":
        return {
            "model": model,
            "max_tokens": 4096,
            "temperature": 0,
            "messages": [
                {
                    "role": "user",
                    "content": judge_request_text,
                }
            ],
        }
    return {
        "contents": [
            {
                "parts": [
                    {
                        "text": judge_request_text,
                    }
                ]
            }
        ],
        "generationConfig": {
            "responseMimeType": "application/json",
            "temperature": 0,
        },
    }


def post_generate_content(url: str, payload: dict, provider: str, api_key: str) -> dict:
    data = json.dumps(payload).encode("utf-8")
    normalized = normalize_provider(provider)
    headers = {"Content-Type": "application/json"}
    if normalized == "anthropic":
        headers["x-api-key"] = api_key
        headers["anthropic-version"] = DEFAULT_ANTHROPIC_VERSION
    request = urllib.request.Request(
        url,
        data=data,
        headers=headers,
        method="POST",
    )
    with urllib.request.urlopen(request, timeout=300) as response:
        return json.loads(response.read().decode("utf-8"))


def extract_response_text(response_payload: dict, provider: str) -> str:
    normalized = normalize_provider(provider)
    if normalized == "anthropic":
        blocks = response_payload.get("content") or []
        texts = [block.get("text", "") for block in blocks if isinstance(block, dict) and block.get("type") == "text"]
        text = "\n".join(t for t in texts if t).strip()
        if not text:
            raise ValueError("No text blocks in Anthropic response")
        return text
    candidates = response_payload.get("candidates") or []
    if not candidates:
        raise ValueError("No candidates in Gemini response")
    content = candidates[0].get("content") or {}
    parts = content.get("parts") or []
    texts = [part.get("text", "") for part in parts if isinstance(part, dict) and "text" in part]
    text = "\n".join(t for t in texts if t).strip()
    if not text:
        raise ValueError("No text parts in Gemini response")
    return text


def normalize_json_text(text: str) -> str:
    stripped = text.strip()
    if stripped.startswith("```"):
        lines = stripped.splitlines()
        if lines and lines[0].startswith("```"):
            lines = lines[1:]
        if lines and lines[-1].strip() == "```":
            lines = lines[:-1]
        stripped = "\n".join(lines).strip()
    return stripped


def read_csv_rows(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def write_csv_rows(path: Path, fieldnames: list[str], rows: list[dict[str, str]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def load_packet_rows(path: Path, axis_filters: set[str] | None, packet_type_filters: set[str] | None) -> list[dict[str, str]]:
    rows = read_csv_rows(path)
    filtered = []
    for row in rows:
        if axis_filters and row["axis"] not in axis_filters:
            continue
        if packet_type_filters and row["packet_type"] not in packet_type_filters:
            continue
        filtered.append(row)
    return filtered


def build_raw_output_dir(raw_root: Path, row: dict[str, str]) -> Path:
    if row["axis"] == "axis_a":
        return raw_root / "axis_a" / row["case_id"] / row["agent_variant"]
    return raw_root / "axis_b" / f"{row['case_id']}_{row['variant_id']}"


def append_absolute_result(row: dict[str, str], parsed: dict, output_rows: list[dict[str, str]], model: str) -> None:
    result = {
        "axis": row["axis"],
        "packet_type": row["packet_type"],
        "case_id": row["case_id"],
        "variant_id": row["variant_id"],
        "agent_variant": row["agent_variant"],
        "model": model,
        "judge_request_path": row["judge_request_path"],
        "prompt_path": row["prompt_path"],
        "word_count": row["word_count"],
        "char_count": row["char_count"],
        "notes": row["notes"],
    }
    for key in ABSOLUTE_FIELDS:
        value = parsed.get(key, "")
        if isinstance(value, (list, dict)):
            value = json.dumps(value, ensure_ascii=False)
        result[key] = value
    output_rows.append(result)


def append_ranking_result(row: dict[str, str], parsed: dict, output_rows: list[dict[str, str]], model: str) -> None:
    result = {
        "axis": row["axis"],
        "packet_type": row["packet_type"],
        "case_id": row["case_id"],
        "variant_id": row["variant_id"],
        "agent_variant": row["agent_variant"],
        "model": model,
        "judge_request_path": row["judge_request_path"],
        "prompt_path": row["prompt_path"],
        "blind_label": row["blind_label"],
        "notes": row["notes"],
    }
    for key in RANKING_FIELDS:
        value = parsed.get(key, "")
        if isinstance(value, (list, dict)):
            value = json.dumps(value, ensure_ascii=False)
        result[key] = value
    output_rows.append(result)


def append_pairwise_result(row: dict[str, str], parsed: dict, output_rows: list[dict[str, str]], model: str) -> None:
    blind_map = json.loads(row["blind_label"])
    winner = parsed.get("winner", "")
    winner_arm = blind_map.get(winner, "") if winner else ""
    challenger = row["agent_variant"].replace("baseline_vs_", "", 1)
    challenger_label = next((label for label, arm in blind_map.items() if arm == challenger), "")
    baseline_label = next((label for label, arm in blind_map.items() if arm == "baseline"), "")
    result = {
        "axis": row["axis"],
        "packet_type": row["packet_type"],
        "case_id": row["case_id"],
        "variant_id": row["variant_id"],
        "agent_variant": row["agent_variant"],
        "challenger": challenger,
        "baseline_label": baseline_label,
        "challenger_label": challenger_label,
        "winner_arm": winner_arm,
        "challenger_beats_baseline": "yes" if winner_arm == challenger else "no",
        "model": model,
        "judge_request_path": row["judge_request_path"],
        "prompt_path": row["prompt_path"],
        "blind_label": row["blind_label"],
        "notes": row["notes"],
    }
    for key in PAIRWISE_FIELDS:
        value = parsed.get(key, "")
        if isinstance(value, (list, dict)):
            value = json.dumps(value, ensure_ascii=False)
        result[key] = value
    output_rows.append(result)


def run_batch(
    packet_manifest_path: Path,
    raw_root: Path,
    response_manifest_path: Path,
    axis_a_scores_path: Path,
    axis_a_rankings_path: Path,
    axis_a_pairwise_path: Path,
    axis_b_scores_path: Path,
    provider: str,
    base_url: str,
    api_key: str,
    model: str,
    axis_filters: set[str] | None = None,
    packet_type_filters: set[str] | None = None,
    limit: int | None = None,
    overwrite: bool = False,
    sleep_seconds: float = 0.0,
) -> dict[str, int]:
    rows = load_packet_rows(packet_manifest_path, axis_filters, packet_type_filters)
    if limit is not None:
        rows = rows[:limit]

    url = build_request_url(provider=provider, base_url=base_url, model=model, api_key=api_key)
    response_manifest_rows: list[dict[str, str]] = []
    axis_a_score_rows: list[dict[str, str]] = []
    axis_a_ranking_rows: list[dict[str, str]] = []
    axis_a_pairwise_rows: list[dict[str, str]] = []
    axis_b_score_rows: list[dict[str, str]] = []

    raw_root.mkdir(parents=True, exist_ok=True)

    for row in rows:
        raw_dir = build_raw_output_dir(raw_root, row)
        raw_dir.mkdir(parents=True, exist_ok=True)
        response_json_path = raw_dir / "response.json"
        response_text_path = raw_dir / "response_text.json"
        parsed_json_path = raw_dir / "parsed_result.json"

        status = "success"
        error_message = ""
        response_payload = None
        response_text = ""
        parsed = {}

        try:
            if response_json_path.exists() and parsed_json_path.exists() and not overwrite:
                response_payload = json.loads(response_json_path.read_text(encoding="utf-8"))
                response_text = json.loads(response_text_path.read_text(encoding="utf-8"))["response_text"]
                parsed = json.loads(parsed_json_path.read_text(encoding="utf-8"))
            else:
                judge_request = (REPO_ROOT / row["judge_request_path"]).read_text(encoding="utf-8")
                payload = build_request_payload(judge_request_text=judge_request, provider=provider, model=model)
                response_payload = post_generate_content(url=url, payload=payload, provider=provider, api_key=api_key)
                response_json_path.write_text(
                    json.dumps(response_payload, ensure_ascii=False, indent=2) + "\n",
                    encoding="utf-8",
                )
                response_text = extract_response_text(response_payload, provider=provider)
                response_text_path.write_text(
                    json.dumps({"response_text": response_text}, ensure_ascii=False, indent=2) + "\n",
                    encoding="utf-8",
                )
                parsed = json.loads(normalize_json_text(response_text))
                parsed_json_path.write_text(
                    json.dumps(parsed, ensure_ascii=False, indent=2) + "\n",
                    encoding="utf-8",
                )
                if sleep_seconds > 0:
                    time.sleep(sleep_seconds)
        except (urllib.error.HTTPError, urllib.error.URLError, TimeoutError, ValueError, json.JSONDecodeError) as exc:
            status = "error"
            error_message = str(exc)

        response_manifest_rows.append(
            {
                "axis": row["axis"],
                "packet_type": row["packet_type"],
                "case_id": row["case_id"],
                "variant_id": row["variant_id"],
                "agent_variant": row["agent_variant"],
                "provider": provider,
                "model": model,
                "judge_request_path": row["judge_request_path"],
                "prompt_path": row["prompt_path"],
                "raw_output_dir": raw_dir.relative_to(REPO_ROOT).as_posix(),
                "response_json_path": response_json_path.relative_to(REPO_ROOT).as_posix(),
                "response_text_path": response_text_path.relative_to(REPO_ROOT).as_posix(),
                "parsed_json_path": parsed_json_path.relative_to(REPO_ROOT).as_posix(),
                "status": status,
                "error_message": error_message,
            }
        )

        if status != "success":
            continue

        if row["packet_type"] == "within_case_ranking":
            append_ranking_result(row, parsed, axis_a_ranking_rows, model)
        elif row["packet_type"] == "pairwise_vs_baseline":
            append_pairwise_result(row, parsed, axis_a_pairwise_rows, model)
        elif row["axis"] == "axis_a":
            append_absolute_result(row, parsed, axis_a_score_rows, model)
        else:
            append_absolute_result(row, parsed, axis_b_score_rows, model)

    write_csv_rows(
        response_manifest_path,
        [
            "axis",
            "packet_type",
            "case_id",
            "variant_id",
            "agent_variant",
            "provider",
            "model",
            "judge_request_path",
            "prompt_path",
            "raw_output_dir",
            "response_json_path",
            "response_text_path",
            "parsed_json_path",
            "status",
            "error_message",
        ],
        response_manifest_rows,
    )

    write_csv_rows(
        axis_a_scores_path,
        [
            "axis",
            "packet_type",
            "case_id",
            "variant_id",
            "agent_variant",
            "model",
            "judge_request_path",
            "prompt_path",
            "word_count",
            "char_count",
            *ABSOLUTE_FIELDS,
            "notes",
        ],
        axis_a_score_rows,
    )
    write_csv_rows(
        axis_a_rankings_path,
        [
            "axis",
            "packet_type",
            "case_id",
            "variant_id",
            "agent_variant",
            "model",
            "judge_request_path",
            "prompt_path",
            *RANKING_FIELDS,
            "blind_label",
            "notes",
        ],
        axis_a_ranking_rows,
    )
    write_csv_rows(
        axis_a_pairwise_path,
        [
            "axis",
            "packet_type",
            "case_id",
            "variant_id",
            "agent_variant",
            "challenger",
            "baseline_label",
            "challenger_label",
            "winner_arm",
            "challenger_beats_baseline",
            "model",
            "judge_request_path",
            "prompt_path",
            *PAIRWISE_FIELDS,
            "blind_label",
            "notes",
        ],
        axis_a_pairwise_rows,
    )
    write_csv_rows(
        axis_b_scores_path,
        [
            "axis",
            "packet_type",
            "case_id",
            "variant_id",
            "agent_variant",
            "model",
            "judge_request_path",
            "prompt_path",
            "word_count",
            "char_count",
            *ABSOLUTE_FIELDS,
            "notes",
        ],
        axis_b_score_rows,
    )

    return {
        "requested_packets": len(rows),
        "successful_packets": sum(1 for row in response_manifest_rows if row["status"] == "success"),
        "failed_packets": sum(1 for row in response_manifest_rows if row["status"] != "success"),
        "axis_a_scores": len(axis_a_score_rows),
        "axis_a_rankings": len(axis_a_ranking_rows),
        "axis_a_pairwise": len(axis_a_pairwise_rows),
        "axis_b_scores": len(axis_b_score_rows),
    }


def parse_args() -> argparse.Namespace:
    ensure_local_env_loaded()
    parser = argparse.ArgumentParser(description="Run report-quality judge batch via Gemini-compatible API.")
    parser.add_argument("--packet-manifest", default=str(DEFAULT_PACKET_MANIFEST_PATH))
    parser.add_argument("--raw-root", default=str(DEFAULT_RAW_ROOT))
    parser.add_argument("--response-manifest", default=str(DEFAULT_RESPONSE_MANIFEST_PATH))
    parser.add_argument("--axis-a-scores", default=str(DEFAULT_AXIS_A_SCORES_PATH))
    parser.add_argument("--axis-a-rankings", default=str(DEFAULT_AXIS_A_RANKINGS_PATH))
    parser.add_argument("--axis-a-pairwise", default=str(DEFAULT_AXIS_A_PAIRWISE_PATH))
    parser.add_argument("--axis-b-scores", default=str(DEFAULT_AXIS_B_SCORES_PATH))
    parser.add_argument("--provider", default=os.environ.get("LLM_JUDGE_PROVIDER", "gemini"), choices=["gemini", "anthropic"])
    parser.add_argument("--base-url")
    parser.add_argument("--model", default=os.environ.get("LLM_JUDGE_MODEL", os.environ.get("GEMINI_MODEL", os.environ.get("ANTHROPIC_MODEL", ""))))
    parser.add_argument("--api-key", default=os.environ.get("LLM_JUDGE_API_KEY", os.environ.get("AIGOCODE_API_KEY", os.environ.get("GEMINI_API_KEY", ""))))
    parser.add_argument("--axis", action="append", choices=["axis_a", "axis_b"])
    parser.add_argument("--packet-type", action="append", choices=["absolute", "within_case_ranking", "pairwise_vs_baseline"])
    parser.add_argument("--limit", type=int)
    parser.add_argument("--overwrite", action="store_true")
    parser.add_argument("--sleep-seconds", type=float, default=0.0)
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    provider = normalize_provider(args.provider)
    base_url = args.base_url or os.environ.get("LLM_JUDGE_BASE_URL") or default_base_url_for_provider(provider)
    if not args.api_key:
        raise SystemExit("Missing API key. Set LLM_JUDGE_API_KEY, AIGOCODE_API_KEY, or GEMINI_API_KEY.")
    if not args.model:
        raise SystemExit("Missing model. Set LLM_JUDGE_MODEL, GEMINI_MODEL, or ANTHROPIC_MODEL.")

    counts = run_batch(
        packet_manifest_path=Path(args.packet_manifest),
        raw_root=Path(args.raw_root),
        response_manifest_path=Path(args.response_manifest),
        axis_a_scores_path=Path(args.axis_a_scores),
        axis_a_rankings_path=Path(args.axis_a_rankings),
        axis_a_pairwise_path=Path(args.axis_a_pairwise),
        axis_b_scores_path=Path(args.axis_b_scores),
        provider=provider,
        base_url=base_url,
        api_key=args.api_key,
        model=args.model,
        axis_filters=set(args.axis) if args.axis else None,
        packet_type_filters=set(args.packet_type) if args.packet_type else None,
        limit=args.limit,
        overwrite=args.overwrite,
        sleep_seconds=args.sleep_seconds,
    )
    print(
        "Completed report-quality judge batch:",
        f"requested={counts['requested_packets']}",
        f"success={counts['successful_packets']}",
        f"failed={counts['failed_packets']}",
        f"axis_a_scores={counts['axis_a_scores']}",
        f"axis_a_rankings={counts['axis_a_rankings']}",
        f"axis_a_pairwise={counts['axis_a_pairwise']}",
        f"axis_b_scores={counts['axis_b_scores']}",
    )


if __name__ == "__main__":
    main()
