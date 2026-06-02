import importlib.util
import json
import tempfile
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
RUNNER_PATH = REPO_ROOT / "scripts" / "run_research_agent_v2.py"
POSTPROCESS_PATH = REPO_ROOT / "scripts" / "postprocess_research_agent_v2_run.py"


def load_module(path: Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


class ResearchAgentV2SmokeTests(unittest.TestCase):
    def test_load_local_env_file_parses_simple_key_values(self) -> None:
        module = load_module(RUNNER_PATH, "run_research_agent_v2")

        with tempfile.TemporaryDirectory() as tmpdir:
            env_path = Path(tmpdir) / ".benchmark.local.env"
            env_path.write_text(
                "# comment\n"
                "OPENALEX_API_KEY='KEY123'\n"
                "OPENALEX_EMAIL=user@example.com\n"
            )

            parsed = module.load_local_env_file(env_path)
            self.assertEqual(parsed["OPENALEX_API_KEY"], "KEY123")
            self.assertEqual(parsed["OPENALEX_EMAIL"], "user@example.com")

    def test_build_openalex_url_includes_api_key_and_mailto(self) -> None:
        module = load_module(RUNNER_PATH, "run_research_agent_v2")

        url = module.build_openalex_url(
            query="staggered difference in differences",
            api_key="KEY123",
            email="user@example.com",
            per_page=5,
        )

        self.assertIn("api.openalex.org/works", url)
        self.assertIn("api_key=KEY123", url)
        self.assertIn("mailto=user%40example.com", url)
        self.assertIn("per-page=5", url)

    def test_render_stage2_prompt_includes_packet_and_constraints(self) -> None:
        module = load_module(RUNNER_PATH, "run_research_agent_v2")

        prompt = module.render_stage2_prompt(
            template_text="PACKET:\n{{PACKET_TEXT}}\nSEED:\n{{OPENALEX_SEED_JSON}}\nFIRST:\n{{MANDATORY_FIRST_QUERY}}\nRULES:\n{{RETRIEVAL_OUTPUT_SCHEMA_HINT}}",
            packet_text="example perturbed packet",
            openalex_seed_json='{"query":"q","results":[]}',
            mandatory_first_query="selection bias causal identification",
        )

        self.assertIn("example perturbed packet", prompt)
        self.assertIn("queries", prompt)
        self.assertIn("tools_attempted", prompt)
        self.assertIn("OPENALEX", prompt.upper())
        self.assertIn("selection bias causal identification", prompt)

    def test_validate_stage2_output_requires_attempt_and_summary_fields(self) -> None:
        module = load_module(RUNNER_PATH, "run_research_agent_v2")

        valid_text = json.dumps(
            {
                "queries": ["causal identification threat checklist"],
                "sources_consulted": ["openalex", "deepxiv"],
                "tools_attempted": ["web_search"],
                "tool_attempt_count": 1,
                "tool_success_count": 1,
                "retrieval_attempted": True,
                "retrieval_successful": True,
                "failure_reason": None,
                "method_fragility_findings": ["parallel trends may fail"],
                "design_fallback_findings": ["descriptive fallback may be safest"],
                "packet_relevant_takeaways": ["packet does not guarantee untreated comparators"],
                "evidence_items": [
                    {
                        "source": "openalex",
                        "query": "parallel trends",
                        "title": "Example paper",
                        "identifier": "https://openalex.org/W123",
                        "relevance_note": "motivates fallback",
                    }
                ],
            }
        )
        parsed = module.validate_stage2_output(valid_text)
        self.assertTrue(parsed["retrieval_attempted"])
        self.assertEqual(parsed["tool_attempt_count"], 1)

        invalid_attempt = json.dumps(
            {
                "queries": [],
                "sources_consulted": [],
                "tools_attempted": [],
                "tool_attempt_count": 0,
                "tool_success_count": 0,
                "retrieval_attempted": False,
                "retrieval_successful": False,
                "failure_reason": "did not try",
                "method_fragility_findings": [],
                "design_fallback_findings": [],
                "packet_relevant_takeaways": [],
                "evidence_items": [],
            }
        )
        with self.assertRaises(ValueError):
            module.validate_stage2_output(invalid_attempt)

        missing_summary = json.dumps(
            {
                "queries": ["x"],
                "sources_consulted": ["openalex"],
                "tools_attempted": ["web_search"],
                "tool_attempt_count": 1,
                "tool_success_count": 0,
                "retrieval_attempted": True,
                "retrieval_successful": False,
                "failure_reason": "429",
                "method_fragility_findings": [],
                "design_fallback_findings": [],
            }
        )
        with self.assertRaises(ValueError):
            module.validate_stage2_output(missing_summary)

    def test_normalize_stage2_artifact_marks_zero_tool_use_invalid(self) -> None:
        module = load_module(RUNNER_PATH, "run_research_agent_v2")

        artifact = {
            "queries": ["query"],
            "sources_consulted": ["openalex"],
            "tools_attempted": ["deepxiv__search_papers"],
            "tool_attempt_count": 3,
            "tool_success_count": 2,
            "retrieval_attempted": True,
            "retrieval_successful": True,
            "failure_reason": None,
            "method_fragility_findings": ["x"],
            "design_fallback_findings": ["y"],
            "packet_relevant_takeaways": ["z"],
            "evidence_items": [
                {
                    "source": "openalex",
                    "query": "query",
                    "title": "Example paper",
                    "identifier": "https://openalex.org/W123",
                    "relevance_note": "note",
                }
            ],
        }
        normalized = module.normalize_stage2_artifact(artifact, {"tool_calls": 0, "tool_results": 0})
        self.assertFalse(normalized["retrieval_successful"])
        self.assertEqual(normalized["failure_reason"], "no_actual_tool_use_recorded")

    def test_extract_tool_call_counts_handles_empty_and_nonempty_meta(self) -> None:
        module = load_module(RUNNER_PATH, "run_research_agent_v2")

        empty = {"meta": {"toolMetas": []}}
        self.assertEqual(module.extract_tool_call_counts(empty), {"tool_calls": 0, "tool_results": 0})

        populated = {
            "meta": {
                "toolMetas": [{"toolName": "web_search"}],
                "agentMeta": {"sessionId": "sess"},
            },
            "messages": [
                {"type": "toolCall", "name": "web_search"},
                {"type": "toolResult", "name": "web_search"},
                {"type": "toolCall", "name": "web_fetch"},
            ],
        }
        counts = module.extract_tool_call_counts(populated)
        self.assertEqual(counts["tool_calls"], 2)
        self.assertEqual(counts["tool_results"], 1)

    def test_stage_status_can_record_retrieval_metadata(self) -> None:
        module = load_module(RUNNER_PATH, "run_research_agent_v2")

        status = module.stage_status(
            status="ok",
            retries=0,
            artifact_path="stage2_retrieval/artifact.json",
            duration=10.5,
            validation="stage2",
            stderr_path="stage2_retrieval/stderr.log",
            retrieval_attempted=True,
            retrieval_successful=False,
            retrieval_tool_calls=1,
            retrieval_failure_reason="429 rate limit",
        )

        self.assertTrue(status["retrieval_attempted"])
        self.assertFalse(status["retrieval_successful"])
        self.assertEqual(status["retrieval_tool_calls"], 1)
        self.assertEqual(status["retrieval_failure_reason"], "429 rate limit")

    def test_build_postprocess_args_targets_stage5_and_v2_variant(self) -> None:
        module = load_module(POSTPROCESS_PATH, "postprocess_research_agent_v2_run")

        with tempfile.TemporaryDirectory() as tmpdir:
            repo_root = Path(tmpdir)
            run_dir = repo_root / "outputs" / "raw_agent_logs" / "research_agent_v2" / "C001_perturbed_20260601_120000"
            stage5_dir = run_dir / "stage5_final"
            stage5_dir.mkdir(parents=True, exist_ok=True)

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
                        "agent_variant": "research_agent_v2_search",
                        "source_input_file": "benchmark/cases/C001_charitable_giving/agent_task_perturbed.md",
                        "stages": {
                            "stage2_retrieval": {
                                "status": "ok",
                                "retrieval_attempted": True,
                                "retrieval_successful": True,
                                "retrieval_tool_calls": 2,
                                "retrieval_failure_reason": None,
                            },
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
                run_id="RUN_TEST_RA_V2",
                timestamp="2026-06-01T12:30:00+08:00",
                timeout_seconds=1800,
                thinking_level="high",
            )

            self.assertIn("--agent-variant", args)
            self.assertIn("research_agent_v2_search", args)
            self.assertIn("--retrieval-attempted-override", args)
            self.assertIn("--retrieval-successful-override", args)
            self.assertIn("--retrieval-tool-calls-override", args)
            self.assertIn(
                "outputs/raw_agent_logs/research_agent_v2/C001_perturbed_20260601_120000/stage5_final/raw_openclaw.json",
                args,
            )
            self.assertIn("benchmark/cases/C001_charitable_giving/agent_task_perturbed.md", args)

    def test_summarize_pipeline_tool_activity_aggregates_stage_sessions(self) -> None:
        module = load_module(POSTPROCESS_PATH, "postprocess_research_agent_v2_run")

        with tempfile.TemporaryDirectory() as tmpdir:
            repo_root = Path(tmpdir)
            run_dir = repo_root / "outputs" / "raw_agent_logs" / "research_agent_v2" / "C001_perturbed_20260601_120000"
            stage2_dir = run_dir / "stage2_retrieval"
            stage5_dir = run_dir / "stage5_final"
            stage2_dir.mkdir(parents=True, exist_ok=True)
            stage5_dir.mkdir(parents=True, exist_ok=True)

            session_stage2 = repo_root / "tmp" / "stage2.jsonl"
            session_stage2.parent.mkdir(parents=True, exist_ok=True)
            session_stage2.write_text(
                "\n".join(
                    [
                        '{"type":"message","message":{"role":"assistant","content":[{"type":"toolCall","id":"call_1","name":"web_search","arguments":{"query":"q"}}]}}',
                        '{"type":"message","message":{"role":"toolResult","toolCallId":"call_1","toolName":"web_search","content":[{"type":"text","text":"ok"}]}}',
                        '{"type":"message","message":{"role":"assistant","content":[{"type":"toolCall","id":"call_2","name":"deepxiv__search_papers","arguments":{"query":"q2"}}]}}',
                        '{"type":"message","message":{"role":"toolResult","toolCallId":"call_2","toolName":"deepxiv__search_papers","content":[{"type":"text","text":"ok"}]}}',
                    ]
                )
                + "\n"
            )

            session_stage5 = repo_root / "tmp" / "stage5.jsonl"
            session_stage5.write_text(
                '{"type":"message","message":{"role":"assistant","content":[{"type":"text","text":"final"}]}}\n'
            )

            (stage2_dir / "raw_openclaw.json").write_text(
                json.dumps(
                    {
                        "payloads": [{"text": "stage2"}],
                        "meta": {"agentMeta": {"sessionFile": str(session_stage2)}},
                    }
                )
            )
            (stage5_dir / "raw_openclaw.json").write_text(
                json.dumps(
                    {
                        "payloads": [{"text": "stage5"}],
                        "meta": {"agentMeta": {"sessionFile": str(session_stage5)}},
                    }
                )
            )
            (run_dir / "pipeline_manifest.json").write_text(
                json.dumps(
                    {
                        "case_id": "C001",
                        "variant_id": "perturbed",
                        "agent_variant": "research_agent_v2_search",
                        "source_input_file": "benchmark/cases/C001_charitable_giving/agent_task_perturbed.md",
                        "stages": {
                            "stage2_retrieval": {"status": "ok"},
                            "stage5_final": {"status": "ok", "stderr_path": "stage5_final/stderr.log"},
                        },
                    }
                )
            )

            summary = module.summarize_pipeline_tool_activity(run_dir)
            self.assertEqual(summary["tool_call_count"], 2)
            self.assertEqual(summary["tool_result_count"], 2)
            self.assertEqual(summary["tool_names"], ["web_search", "deepxiv__search_papers"])


if __name__ == "__main__":
    unittest.main()
