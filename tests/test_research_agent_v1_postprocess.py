import csv
import importlib.util
import json
import tempfile
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
SCRIPT_PATH = REPO_ROOT / "scripts" / "postprocess_research_agent_v1_run.py"


def load_module():
    spec = importlib.util.spec_from_file_location("postprocess_research_agent_v1_run", SCRIPT_PATH)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


def write_csv(path: Path, fieldnames: list[str], rows: list[dict[str, str]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


class ResearchAgentV1PostprocessTests(unittest.TestCase):
    def test_build_postprocess_args_targets_stage5_and_research_agent_variant(self) -> None:
        module = load_module()

        with tempfile.TemporaryDirectory() as tmpdir:
            repo_root = Path(tmpdir)
            run_dir = repo_root / "outputs" / "raw_agent_logs" / "research_agent_v1" / "C001_perturbed_20260531_162114"
            stage5_dir = run_dir / "stage5_final"
            stage5_dir.mkdir(parents=True, exist_ok=True)

            write_csv(
                repo_root / "outputs" / "run_manifest.csv",
                [
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
                ],
                [],
            )

            (run_dir / "input_packet.md").write_text("packet")
            (stage5_dir / "raw_openclaw.json").write_text(
                json.dumps(
                    {
                        "payloads": [{"text": "final output"}],
                        "meta": {
                            "agentMeta": {
                                "sessionId": "sess123",
                                "sessionFile": "/tmp/sess123.jsonl",
                                "model": "deepseek-v4-pro",
                                "provider": "deepseek",
                            },
                            "durationMs": 1000,
                        },
                    }
                )
            )
            (stage5_dir / "stderr.log").write_text("")
            (run_dir / "pipeline_manifest.json").write_text(
                json.dumps(
                    {
                        "case_id": "C001",
                        "variant_id": "perturbed",
                        "agent_variant": "research_agent_v1",
                        "source_input_file": "benchmark/cases/C001_charitable_giving/agent_task_perturbed.md",
                        "stages": {
                            "stage5_final": {
                                "status": "ok",
                                "artifact_path": "stage5_final/artifact.md",
                                "stderr_path": "stage5_final/stderr.log",
                            }
                        },
                    }
                )
            )

            args = module.build_postprocess_args(
                repo_root=repo_root,
                run_dir=run_dir,
                run_id="RUN_TEST_RA",
                timestamp="2026-05-31T16:30:00+08:00",
                timeout_seconds=1800,
                thinking_level="high",
            )

            self.assertIn("--agent-variant", args)
            self.assertIn("research_agent_v1", args)
            self.assertIn("outputs/raw_agent_logs/research_agent_v1/C001_perturbed_20260531_162114/stage5_final/raw_openclaw.json", args)
            self.assertIn("benchmark/cases/C001_charitable_giving/agent_task_perturbed.md", args)


if __name__ == "__main__":
    unittest.main()
