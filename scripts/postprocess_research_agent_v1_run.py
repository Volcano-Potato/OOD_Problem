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
    parser = argparse.ArgumentParser(description="Bridge one research_agent_v1 run directory into the formal manifest/raw-log chain.")
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
    stage5 = manifest["stages"]["stage5_final"]
    raw_json = run_dir / "stage5_final" / "raw_openclaw.json"
    stderr_path = run_dir / stage5.get("stderr_path", "stage5_final/stderr.log")

    return [
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
        manifest.get("agent_variant", "research_agent_v1"),
    ]


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
