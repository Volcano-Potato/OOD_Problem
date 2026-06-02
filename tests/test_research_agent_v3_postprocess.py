import importlib.util
import json
import tempfile
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
POSTPROCESS_PATH = REPO_ROOT / "scripts" / "postprocess_research_agent_v3_run.py"


def load_module(path: Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


class ResearchAgentV3PostprocessTests(unittest.TestCase):
    def test_summarize_pipeline_tool_activity_aggregates_all_v3_stages(self) -> None:
        module = load_module(POSTPROCESS_PATH, "postprocess_research_agent_v3_run")

        with tempfile.TemporaryDirectory() as tmpdir:
            repo_root = Path(tmpdir)
            run_dir = repo_root / "outputs" / "raw_agent_logs" / "research_agent_v3" / "C005_perturbed_20260601_000000"
            run_dir.mkdir(parents=True, exist_ok=True)

            session_path = repo_root / "sess.jsonl"
            session_path.write_text(
                "\n".join(
                    [
                        json.dumps(
                            {
                                "type": "message",
                                "message": {
                                    "role": "assistant",
                                    "content": [
                                        {"type": "toolCall", "name": "deepxiv__search_papers"},
                                        {"type": "toolCall", "name": "web_search"},
                                    ],
                                },
                            }
                        ),
                        json.dumps(
                            {
                                "type": "message",
                                "message": {
                                    "role": "toolResult",
                                    "toolName": "deepxiv__search_papers",
                                },
                            }
                        ),
                        json.dumps(
                            {
                                "type": "message",
                                "message": {
                                    "role": "toolResult",
                                    "toolName": "web_search",
                                },
                            }
                        ),
                    ]
                )
            )

            for stage in ("stage2_retrieval", "stage3b_response"):
                stage_dir = run_dir / stage
                stage_dir.mkdir(parents=True, exist_ok=True)
                (stage_dir / "raw_openclaw.json").write_text(
                    json.dumps({"meta": {"agentMeta": {"sessionFile": str(session_path)}}})
                )

            (run_dir / "pipeline_manifest.json").write_text(
                json.dumps(
                    {
                        "case_id": "C005",
                        "variant_id": "perturbed",
                        "agent_variant": "research_agent_v3_planner_debate",
                        "stages": {
                            "stage2_retrieval": {"status": "ok"},
                            "stage3b_response": {"status": "ok"},
                        },
                    }
                )
            )

            summary = module.summarize_pipeline_tool_activity(run_dir)
            self.assertEqual(summary["tool_call_count"], 4)
            self.assertEqual(summary["tool_result_count"], 4)
            self.assertEqual(summary["tool_names"], ["deepxiv__search_papers", "web_search"])

    def test_build_postprocess_args_targets_v3_variant_and_stage5(self) -> None:
        module = load_module(POSTPROCESS_PATH, "postprocess_research_agent_v3_run")

        with tempfile.TemporaryDirectory() as tmpdir:
            repo_root = Path(tmpdir)
            run_dir = repo_root / "outputs" / "raw_agent_logs" / "research_agent_v3" / "C005_perturbed_20260601_000000"
            stage5_dir = run_dir / "stage5_final"
            stage5_dir.mkdir(parents=True, exist_ok=True)
            session_path = repo_root / "sess.jsonl"
            session_path.write_text(
                json.dumps(
                    {
                        "type": "message",
                        "message": {
                            "role": "assistant",
                            "content": [{"type": "toolCall", "name": "web_search"}],
                        },
                    }
                )
                + "\n"
                + json.dumps(
                    {
                        "type": "message",
                        "message": {"role": "toolResult", "toolName": "web_search"},
                    }
                )
            )
            (stage5_dir / "raw_openclaw.json").write_text(
                json.dumps(
                    {
                        "payloads": [{"text": "final output"}],
                        "meta": {
                            "agentMeta": {
                                "sessionId": "sess123",
                                "sessionFile": str(session_path),
                                "model": "deepseek-v4-pro",
                                "provider": "deepseek",
                            }
                        },
                    }
                )
            )
            (stage5_dir / "stderr.log").write_text("")
            stage2_dir = run_dir / "stage2_retrieval"
            stage2_dir.mkdir(parents=True, exist_ok=True)
            (stage2_dir / "raw_openclaw.json").write_text(
                json.dumps({"meta": {"agentMeta": {"sessionFile": str(session_path)}}})
            )
            (run_dir / "pipeline_manifest.json").write_text(
                json.dumps(
                    {
                        "case_id": "C005",
                        "variant_id": "perturbed",
                        "agent_variant": "research_agent_v3_planner_debate",
                        "source_input_file": "benchmark/cases/C005_online_ad_measurement/agent_task_perturbed.md",
                        "stages": {
                            "stage2_retrieval": {
                                "status": "ok",
                                "retrieval_attempted": True,
                                "retrieval_successful": True,
                                "retrieval_tool_calls": 1,
                                "retrieval_failure_reason": None,
                            },
                            "stage5_final": {
                                "status": "ok",
                                "artifact_path": "stage5_final/artifact.md",
                                "stderr_path": "stage5_final/stderr.log",
                            },
                        },
                    }
                )
            )

            args = module.build_postprocess_args(
                repo_root=repo_root,
                run_dir=run_dir,
                run_id="RUN_TEST_V3",
                timestamp="2026-06-01T18:00:00+08:00",
                timeout_seconds=1800,
                thinking_level="high",
            )

            joined = " ".join(args)
            self.assertIn("--agent-variant research_agent_v3_planner_debate", joined)
            self.assertIn("stage5_final/raw_openclaw.json", joined)
            self.assertIn("--actual-tool-use-override web_search", joined)
            self.assertIn("--retrieval-attempted-override True", joined)


if __name__ == "__main__":
    unittest.main()
