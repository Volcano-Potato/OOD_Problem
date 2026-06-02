#!/usr/bin/env python3

from __future__ import annotations

import argparse
import json
import subprocess
from datetime import datetime
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
POSTPROCESS = ROOT / "scripts" / "postprocess_openclaw_run.py"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Bridge one research_agent_v3 run directory into the formal manifest/raw-log chain."
    )
    parser.add_argument("--run-dir", required=True)
    parser.add_argument("--run-id", required=True)
    parser.add_argument("--input-file")
    parser.add_argument("--timestamp", default=datetime.now().astimezone().isoformat(timespec="seconds"))
    parser.add_argument("--timeout-seconds", type=int, default=1800)
    parser.add_argument("--thinking-level", default="high")
    parser.add_argument("--split", default="main")
    return parser.parse_args()


def load_manifest(run_dir: Path) -> dict:
    return json.loads((run_dir / "pipeline_manifest.json").read_text())


def count_tool_activity_from_session(session_file: Path) -> dict[str, object]:
    if not session_file.exists():
        return {"tool_call_count": 0, "tool_result_count": 0, "tool_names": []}
    tool_call_count = 0
    tool_result_count = 0
    tool_names: list[str] = []
    seen = set()
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
        message = entry.get("message") or {}
        if message.get("role") == "toolResult":
            tool_result_count += 1
            tool_name = message.get("toolName")
            if tool_name and tool_name not in seen:
                seen.add(tool_name)
                tool_names.append(str(tool_name))
            continue
        content = message.get("content")
        if isinstance(content, list):
            for block in content:
                if not isinstance(block, dict) or block.get("type") != "toolCall":
                    continue
                tool_call_count += 1
                tool_name = block.get("name")
                if tool_name and tool_name not in seen:
                    seen.add(tool_name)
                    tool_names.append(str(tool_name))
    return {
        "tool_call_count": tool_call_count,
        "tool_result_count": tool_result_count,
        "tool_names": tool_names,
    }


def summarize_pipeline_tool_activity(run_dir: Path) -> dict[str, object]:
    manifest = load_manifest(run_dir)
    tool_call_count = 0
    tool_result_count = 0
    tool_names: list[str] = []
    seen = set()
    for stage_name in (
        "stage0_planner",
        "stage2_retrieval",
        "stage3_candidates",
        "stage4_critique",
        "stage3b_response",
        "stage4b_critique",
        "stage5_final",
    ):
        if stage_name not in manifest.get("stages", {}):
            continue
        raw_json = run_dir / stage_name / "raw_openclaw.json"
        if not raw_json.exists():
            continue
        data = json.loads(raw_json.read_text())
        session_file = (((data.get("meta") or {}).get("agentMeta") or {}).get("sessionFile"))
        if not session_file:
            continue
        counts = count_tool_activity_from_session(Path(session_file))
        tool_call_count += int(counts["tool_call_count"])
        tool_result_count += int(counts["tool_result_count"])
        for name in counts["tool_names"]:
            if name not in seen:
                seen.add(name)
                tool_names.append(str(name))
    return {
        "tool_call_count": tool_call_count,
        "tool_result_count": tool_result_count,
        "tool_names": tool_names,
    }


def build_postprocess_args(
    repo_root: Path,
    run_dir: Path,
    run_id: str,
    timestamp: str,
    timeout_seconds: int,
    thinking_level: str,
    split: str = "main",
    input_file_override: str | None = None,
) -> list[str]:
    manifest = load_manifest(run_dir)
    pipeline_tools = summarize_pipeline_tool_activity(run_dir)
    stage2 = manifest["stages"].get("stage2_retrieval", {})
    stage5 = manifest["stages"]["stage5_final"]
    raw_json = run_dir / "stage5_final" / "raw_openclaw.json"
    stderr_path = run_dir / stage5.get("stderr_path", "stage5_final/stderr.log")

    command = [
        "python3",
        str(POSTPROCESS),
        "--repo-root",
        str(repo_root),
        "--json-path",
        raw_json.relative_to(repo_root).as_posix(),
        "--stderr-path",
        stderr_path.relative_to(repo_root).as_posix(),
        "--run-id",
        run_id,
        "--case-id",
        manifest["case_id"],
        "--variant-id",
        manifest["variant_id"],
        "--level",
        manifest["variant_id"],
        "--split",
        split,
        "--input-file",
        input_file_override or manifest["source_input_file"],
        "--session-id",
        "placeholder_from_stage5_json",
        "--timestamp",
        timestamp,
        "--timeout-seconds",
        str(timeout_seconds),
        "--thinking-level",
        thinking_level,
        "--agent-variant",
        manifest.get("agent_variant", "research_agent_v3_planner_debate"),
    ]
    if pipeline_tools["tool_names"]:
        command.extend(
            [
                "--actual-tool-use-override",
                ",".join(pipeline_tools["tool_names"]),
                "--tool-call-count-override",
                str(pipeline_tools["tool_call_count"]),
                "--tool-result-count-override",
                str(pipeline_tools["tool_result_count"]),
            ]
        )
    if stage2:
        if "retrieval_attempted" in stage2:
            command.extend(
                [
                    "--retrieval-attempted-override",
                    str(stage2.get("retrieval_attempted")),
                ]
            )
        if "retrieval_successful" in stage2:
            command.extend(
                [
                    "--retrieval-successful-override",
                    str(stage2.get("retrieval_successful")),
                ]
            )
        if stage2.get("retrieval_tool_calls") is not None:
            command.extend(
                [
                    "--retrieval-tool-calls-override",
                    str(stage2.get("retrieval_tool_calls")),
                ]
            )
        if stage2.get("retrieval_failure_reason") is not None:
            command.extend(
                [
                    "--retrieval-failure-reason-override",
                    str(stage2.get("retrieval_failure_reason")),
                ]
            )
    return command


def main() -> None:
    args = parse_args()
    run_dir = Path(args.run_dir).resolve()
    command = build_postprocess_args(
        repo_root=ROOT,
        run_dir=run_dir,
        run_id=args.run_id,
        timestamp=args.timestamp,
        timeout_seconds=args.timeout_seconds,
        thinking_level=args.thinking_level,
        split=args.split,
        input_file_override=args.input_file,
    )
    subprocess.run(command, cwd=ROOT, check=True)


if __name__ == "__main__":
    main()
