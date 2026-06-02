import importlib.util
import json
import tempfile
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
RUNNER_PATH = REPO_ROOT / "scripts" / "run_research_agent_v3.py"


def load_module(path: Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


class ResearchAgentV3SmokeTests(unittest.TestCase):
    def test_validate_stage0_output_requires_schema(self) -> None:
        module = load_module(RUNNER_PATH, "run_research_agent_v3")

        valid = json.dumps(
            {
                "primary_estimand_hypotheses": ["itt on assignment"],
                "threat_checks": ["broken untreated counterfactual"],
                "search_priorities": ["interference bias"],
                "fallback_triggers": ["if untreated comparison is contaminated"],
                "final_decision_rule": "Prefer descriptive fallback if no candidate survives the perturbation.",
            }
        )
        parsed = module.validate_stage0_output(valid)
        self.assertEqual(parsed["primary_estimand_hypotheses"][0], "itt on assignment")

        invalid = json.dumps(
            {
                "primary_estimand_hypotheses": [],
                "threat_checks": [],
                "search_priorities": [],
                "fallback_triggers": [],
                "final_decision_rule": "",
            }
        )
        with self.assertRaises(ValueError):
            module.validate_stage0_output(invalid)

        invalid_type = json.dumps(
            {
                "primary_estimand_hypotheses": ["itt"],
                "threat_checks": {"x": "y"},
                "search_priorities": ["search x"],
                "fallback_triggers": ["fallback x"],
                "final_decision_rule": "pick weakest defensible estimand",
            }
        )
        with self.assertRaises(ValueError):
            module.validate_stage0_output(invalid_type)

    def test_render_stage0_prompt_includes_packet_and_schema(self) -> None:
        module = load_module(RUNNER_PATH, "run_research_agent_v3")
        prompt = module.render_stage0_prompt(
            template_text="PACKET:\n{{PACKET_TEXT}}\nSCHEMA:\n{{PLANNER_OUTPUT_SCHEMA_HINT}}",
            packet_text="example packet text",
        )
        self.assertIn("example packet text", prompt)
        self.assertIn("primary_estimand_hypotheses", prompt)
        self.assertIn("final_decision_rule", prompt)

    def test_render_stage3b_prompt_threads_prior_artifacts(self) -> None:
        module = load_module(RUNNER_PATH, "run_research_agent_v3")
        prompt = module.render_stage3b_prompt(
            template_text="P0={{STAGE0_JSON}}\nP2={{STAGE2_JSON}}\nP3={{STAGE3_JSON}}\nP4={{STAGE4_CRITIQUE}}\nM={{STAGE4_META_JSON}}\nPKT={{PACKET_TEXT}}",
            packet_text="packet body",
            stage0_json='{"final_decision_rule":"x"}',
            stage2_json='{"retrieval_successful":true}',
            stage3_json='{"candidates":[]}',
            stage4_critique="critic body",
            stage4_meta_json='{"debate_required":true}',
        )
        self.assertIn("packet body", prompt)
        self.assertIn('{"debate_required":true}', prompt)
        self.assertIn("critic body", prompt)

    def test_validate_stage3b_output_requires_allowed_dispositions(self) -> None:
        module = load_module(RUNNER_PATH, "run_research_agent_v3")

        valid = json.dumps(
            {
                "responses": [
                    {
                        "focus_point": "broken untreated comparator",
                        "disposition": "accept",
                        "packet_evidence": "packet says untreated stores removed",
                        "retrieval_evidence": None,
                        "revision": "drop within-store DiD candidate",
                    }
                ],
                "updated_primary_candidate": None,
                "updated_fallback_position": "descriptive demand reallocation",
            }
        )
        parsed = module.validate_stage3b_output(valid)
        self.assertEqual(parsed["responses"][0]["disposition"], "accept")

        invalid = json.dumps(
            {
                "responses": [
                    {
                        "focus_point": "x",
                        "disposition": "ignore",
                        "packet_evidence": "y",
                        "retrieval_evidence": None,
                        "revision": "z",
                    }
                ],
                "updated_primary_candidate": None,
                "updated_fallback_position": "fallback",
            }
        )
        with self.assertRaises(ValueError):
            module.validate_stage3b_output(invalid)

    def test_parse_stage4b_output_requires_fenced_json(self) -> None:
        module = load_module(RUNNER_PATH, "run_research_agent_v3")
        text = """Critique body.

```json
{"resolved_focus_points":["a"],"unresolved_focus_points":[],"final_recommendation":"descriptive_fallback","continue_debate":false}
```"""
        critique_md, meta = module.parse_stage4b_output(text)
        self.assertIn("Critique body.", critique_md)
        self.assertEqual(meta["final_recommendation"], "descriptive_fallback")

    def test_stage_status_can_record_planner_and_debate_fields(self) -> None:
        module = load_module(RUNNER_PATH, "run_research_agent_v3")
        status = module.stage_status(
            status="ok",
            retries=0,
            artifact_path="stage4b_critique/artifact.md",
            duration=12.3,
            validation="stage4b",
        )
        self.assertEqual(status["status"], "ok")
        self.assertEqual(status["validation"], "stage4b")

    def test_initialize_manifest_sets_v3_agent_variant(self) -> None:
        module = load_module(RUNNER_PATH, "run_research_agent_v3")
        with tempfile.TemporaryDirectory() as tmpdir:
            manifest_path = Path(tmpdir) / "pipeline_manifest.json"
            module.initialize_pipeline_manifest(
                manifest_path=manifest_path,
                case_id="C005",
                variant_id="perturbed",
                input_packet_sha256="abc123",
            )
            data = json.loads(manifest_path.read_text())
            self.assertEqual(data["agent_variant"], "research_agent_v3_planner_debate")
            self.assertEqual(data["planner_present"], False)
            self.assertEqual(data["debate_rounds_run"], 0)

    def test_output_root_defaults_to_research_agent_v3(self) -> None:
        module = load_module(RUNNER_PATH, "run_research_agent_v3")
        self.assertEqual(module.DEFAULT_OUTPUT_ROOT.name, "research_agent_v3")


if __name__ == "__main__":
    unittest.main()
