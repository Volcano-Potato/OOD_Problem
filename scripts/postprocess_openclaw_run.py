#!/usr/bin/env python3

import argparse
import csv
import json
import os
import re
import sys
from pathlib import Path


DEFAULT_AGENT_VARIANT = "benchmark_isolated"
MANIFEST_FIELDNAMES = [
    "run_id",
    "case_id",
    "variant_id",
    "level",
    "agent_name",
    "agent_variant",
    "model",
    "model_provider",
    "openclaw_build_or_version",
    "temperature",
    "top_p",
    "max_tokens",
    "seed",
    "tools_enabled",
    "closed_book",
    "channel",
    "timestamp",
    "input_file",
    "raw_output_file",
    "status",
    "contamination_status",
    "contamination_reason",
    "notes",
]


def parse_args():
    parser = argparse.ArgumentParser(
        description="Postprocess one OpenClaw benchmark_isolated run into raw log + manifest entry."
    )
    parser.add_argument("--repo-root", required=True)
    parser.add_argument("--json-path", required=True)
    parser.add_argument("--stderr-path", required=True)
    parser.add_argument("--run-id", required=True)
    parser.add_argument("--case-id", required=True)
    parser.add_argument("--variant-id", required=True)
    parser.add_argument("--level", required=True)
    parser.add_argument("--split", required=True)
    parser.add_argument("--input-file", required=True)
    parser.add_argument("--session-id", required=True)
    parser.add_argument("--timestamp", required=True)
    parser.add_argument("--timeout-seconds", required=True)
    parser.add_argument("--thinking-level", required=True)
    parser.add_argument("--agent-id", default="benchmark_isolated")
    parser.add_argument("--agent-name", default="openclaw")
    parser.add_argument("--agent-variant", default=DEFAULT_AGENT_VARIANT)
    parser.add_argument("--channel", default="cli")
    parser.add_argument(
        "--tools-enabled",
        default="locally_isolated_remote_tool_enabled",
    )
    parser.add_argument("--manifest-path", default="outputs/run_manifest.csv")
    parser.add_argument("--default-status", default="unknown")
    return parser.parse_args()


def load_json_if_present(path: Path):
    if not path.exists() or path.stat().st_size == 0:
        return None
    try:
        return json.loads(path.read_text())
    except json.JSONDecodeError:
        return None


def find_session_paths(session_id: str, session_file_hint: str | None):
    if session_file_hint:
        session_file = Path(session_file_hint)
    else:
        session_file = (
            Path.home()
            / ".openclaw"
            / "agents"
            / "benchmark_isolated"
            / "sessions"
            / f"{session_id}.jsonl"
        )
    trajectory_file = session_file.with_name(f"{session_id}.trajectory.jsonl")
    return session_file, trajectory_file


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


def extract_tool_meta(trajectory_path: Path):
    tool_metas = None
    workspace_dir = None
    trace_status = None
    if trajectory_path.exists():
        for line in trajectory_path.read_text(errors="ignore").splitlines():
            try:
                obj = json.loads(line)
            except json.JSONDecodeError:
                continue
            workspace_dir = workspace_dir or obj.get("workspaceDir")
            if obj.get("type") == "trace.artifacts":
                data = obj.get("data", {})
                if isinstance(data, dict):
                    tool_metas = data.get("toolMetas")
                    trace_status = data.get("finalStatus")
    if tool_metas is None:
        tool_metas = []
    return tool_metas, workspace_dir, trace_status


def extract_tool_counts(session_path: Path):
    if not session_path.exists():
        return {
            "tool_call_count": 0,
            "tool_result_count": 0,
            "session_log_exists": False,
        }
    text = session_path.read_text(errors="ignore")
    return {
        "tool_call_count": text.count("toolCall"),
        "tool_result_count": text.count("toolResult"),
        "session_log_exists": True,
    }


def normalize_tool_names(tool_metas):
    names = []
    for item in tool_metas or []:
        if isinstance(item, dict):
            for key in ("name", "toolName", "id"):
                value = item.get(key)
                if value:
                    names.append(str(value))
                    break
        elif item:
            names.append(str(item))
    return names


def derive_status(exit_code: int, json_data: dict | None, output_text: str):
    if exit_code != 0 and not output_text:
        return "runtime_fail"
    if json_data is None and exit_code == 0:
        return "partial"
    meta = (json_data or {}).get("meta", {})
    if meta.get("aborted"):
        return "aborted"
    if not output_text:
        return "partial"
    return "success"


def derive_contamination(status: str, actual_tool_use: str, trajectory_exists: bool):
    if status != "success":
        reason = "run did not complete successfully; contamination review pending"
        return "unknown", reason
    if not trajectory_exists:
        reason = "trajectory missing; actual tool use could not be reconstructed"
        return "suspected", reason
    if actual_tool_use == "none":
        reason = "pending manual content review; actual tool use=none"
    else:
        reason = f"pending manual content review; actual tool use={actual_tool_use}"
    return "unknown", reason


def sanitize_note(text: str):
    return re.sub(r"\s+", " ", text).strip()


def write_raw_log(
    out_path: Path,
    run_id: str,
    case_id: str,
    variant_id: str,
    level: str,
    agent_name: str,
    agent_id: str,
    agent_variant: str,
    model: str,
    provider: str,
    build: str,
    channel: str,
    tools_enabled: str,
    timestamp: str,
    input_file: str,
    system_prompt_summary: str,
    contamination_status: str,
    contamination_reason: str,
    status: str,
    output_text: str,
    actual_tool_use: str,
    tool_metas,
    session_id: str,
    session_path: Path,
    trajectory_path: Path,
    duration_ms,
    stderr_excerpt: str,
    tool_counts: dict,
):
    tool_meta_json = json.dumps(tool_metas, ensure_ascii=False)
    text = f"""# Raw Agent Run Log

- `run_id`: {run_id}
- `case_id`: {case_id}
- `variant_id`: {variant_id}
- `level`: {level}
- `agent_name`: {agent_name}
- `agent_id`: {agent_id}
- `agent_variant`: {agent_variant}
- `model`: {model}
- `model_provider`: {provider}
- `openclaw_build_or_version`: {build}
- `channel`: {channel}
- `temperature`: not_supported
- `top_p`: not_supported
- `max_tokens`: not_supported
- `seed`: not_supported
- `tools_enabled`: {tools_enabled}
- `closed_book`: false
- `timestamp`: {timestamp}
- `input_file`: {input_file}
- `system_prompt_summary`: {system_prompt_summary}
- `contamination_status`: {contamination_status}
- `contamination_reason`: {contamination_reason}
- `status`: {status}

## Raw Agent Output

{output_text if output_text else "[no output captured]"}

## Tool Log Summary

- actual tool use: {actual_tool_use}
- trajectory `toolMetas`: {tool_meta_json}
- toolCall count: {tool_counts['tool_call_count']}
- toolResult count: {tool_counts['tool_result_count']}
- session_id: {session_id}
- session_log: {session_path}
- trajectory_log: {trajectory_path}

## Operator Notes

- duration_ms: {duration_ms}
- stderr_excerpt: {stderr_excerpt if stderr_excerpt else 'none'}
"""
    out_path.write_text(text)


def append_manifest_row(manifest_path: Path, row: dict[str, str]):
    manifest_path.parent.mkdir(parents=True, exist_ok=True)
    existing = set()
    header = MANIFEST_FIELDNAMES
    if manifest_path.exists():
        with manifest_path.open(newline="") as fh:
            reader = csv.DictReader(fh)
            if reader.fieldnames:
                header = reader.fieldnames
            for current in reader:
                run_id = current.get("run_id")
                if run_id:
                    existing.add(run_id)
    if row["run_id"] in existing:
        raise SystemExit(f"run_id already exists in manifest: {row['run_id']}")
    with manifest_path.open("a", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=header, lineterminator="\n")
        if fh.tell() == 0:
            writer.writeheader()
        writer.writerow({key: row.get(key, "") for key in header})


def main():
    args = parse_args()
    repo_root = Path(args.repo_root)
    json_path = repo_root / args.json_path
    stderr_path = repo_root / args.stderr_path
    manifest_path = repo_root / args.manifest_path

    stderr_excerpt = ""
    if stderr_path.exists():
        stderr_excerpt = sanitize_note(stderr_path.read_text(errors="ignore")[:1200])

    json_data = load_json_if_present(json_path)
    output_text = extract_payload_text(json_data) if json_data else ""
    meta = (json_data or {}).get("meta", {})
    agent_meta = meta.get("agentMeta", {})
    session_id = agent_meta.get("sessionId") or args.session_id
    session_file_hint = agent_meta.get("sessionFile")
    session_path, trajectory_path = find_session_paths(session_id, session_file_hint)
    tool_metas, workspace_dir, trace_status = extract_tool_meta(trajectory_path)
    tool_counts = extract_tool_counts(session_path)
    tool_names = normalize_tool_names(tool_metas)
    actual_tool_use = ",".join(tool_names) if tool_names else "none"

    exit_code = int(os.environ.get("OPENCLAW_RUN_EXIT_CODE", "0"))
    status = derive_status(exit_code, json_data, output_text)
    contamination_status, contamination_reason = derive_contamination(
        status=status,
        actual_tool_use=actual_tool_use,
        trajectory_exists=trajectory_path.exists(),
    )

    model = agent_meta.get("model", "unknown")
    provider = agent_meta.get("provider", "unknown")
    build = (
        ((meta.get("systemPromptReport") or {}).get("systemPromptReport") or {}).get("version")
        or ((meta.get("systemPromptReport") or {}).get("harness") or {}).get("version")
        or "2026.5.5"
    )
    if build == "2026.5.5":
        harness = (meta.get("systemPromptReport") or {}).get("harness") or {}
        if harness.get("version"):
            build = harness["version"]
    duration_ms = meta.get("durationMs", "unknown")

    if args.agent_variant == DEFAULT_AGENT_VARIANT:
        raw_output_name = f"{args.case_id}_{args.variant_id}_{args.agent_name}_{args.run_id}.md"
    else:
        raw_output_name = f"{args.case_id}_{args.variant_id}__{args.agent_variant}__{args.run_id}.md"
    raw_output_rel = Path("outputs") / "raw_agent_logs" / args.split / raw_output_name
    raw_output_path = repo_root / raw_output_rel
    raw_output_path.parent.mkdir(parents=True, exist_ok=True)

    system_prompt_summary = (
        f"workspace={workspace_dir or 'unknown'}; "
        f"thinking={args.thinking_level}; "
        f"actual_tool_use={actual_tool_use}; "
        f"agent={args.agent_id}; "
        f"agent_variant={args.agent_variant}"
    )

    write_raw_log(
        out_path=raw_output_path,
        run_id=args.run_id,
        case_id=args.case_id,
        variant_id=args.variant_id,
        level=args.level,
        agent_name=args.agent_name,
        agent_id=args.agent_id,
        agent_variant=args.agent_variant,
        model=model,
        provider=provider,
        build=build,
        channel=args.channel,
        tools_enabled=args.tools_enabled,
        timestamp=args.timestamp,
        input_file=args.input_file,
        system_prompt_summary=system_prompt_summary,
        contamination_status=contamination_status,
        contamination_reason=contamination_reason,
        status=status,
        output_text=output_text,
        actual_tool_use=actual_tool_use,
        tool_metas=tool_metas,
        session_id=session_id,
        session_path=session_path,
        trajectory_path=trajectory_path,
        duration_ms=duration_ms,
        stderr_excerpt=stderr_excerpt,
        tool_counts=tool_counts,
    )

    notes_parts = [
        f"batch runner",
        f"timeout={args.timeout_seconds}",
        f"thinking={args.thinking_level}",
        "local-file-isolated",
        f"actual tool use={actual_tool_use}",
    ]
    if stderr_excerpt:
        notes_parts.append("stderr captured")

    row = {
        "run_id": args.run_id,
        "case_id": args.case_id,
        "variant_id": args.variant_id,
        "level": args.level,
        "agent_name": args.agent_name,
        "agent_variant": args.agent_variant,
        "model": model,
        "model_provider": provider,
        "openclaw_build_or_version": build,
        "temperature": "not_supported",
        "top_p": "not_supported",
        "max_tokens": "not_supported",
        "seed": "not_supported",
        "tools_enabled": args.tools_enabled,
        "closed_book": "false",
        "channel": args.channel,
        "timestamp": args.timestamp,
        "input_file": args.input_file,
        "raw_output_file": raw_output_rel.as_posix(),
        "status": status,
        "contamination_status": contamination_status,
        "contamination_reason": contamination_reason,
        "notes": "; ".join(notes_parts),
    }
    append_manifest_row(manifest_path, row)

    summary = {
        "run_id": args.run_id,
        "status": status,
        "contamination_status": contamination_status,
        "session_id": session_id,
        "raw_output_file": raw_output_rel.as_posix(),
        "actual_tool_use": actual_tool_use,
        "duration_ms": duration_ms,
    }
    print(json.dumps(summary, ensure_ascii=False))


if __name__ == "__main__":
    main()
