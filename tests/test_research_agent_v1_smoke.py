import importlib.util
import json
import os
import tempfile
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
SCRIPT_PATH = REPO_ROOT / "scripts" / "run_research_agent_v1.py"


def load_module():
    spec = importlib.util.spec_from_file_location("run_research_agent_v1", SCRIPT_PATH)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


class ResearchAgentV1SmokeTests(unittest.TestCase):
    def test_render_stage3_prompt_includes_packet_and_schema_cues(self) -> None:
        module = load_module()

        prompt = module.render_stage3_prompt(
            template_text="PACKET:\n{{PACKET_TEXT}}\nJSON ONLY\n{{OUTPUT_SCHEMA_HINT}}",
            packet_text="example perturbed packet",
        )

        self.assertIn("example perturbed packet", prompt)
        self.assertIn("candidates", prompt)

    def test_validate_stage3_output_requires_at_least_three_candidates(self) -> None:
        module = load_module()

        valid_text = json.dumps(
            {
                "candidates": [
                    {"name": "A"},
                    {"name": "B"},
                    {"name": "fallback", "is_fallback": True},
                ]
            }
        )
        parsed = module.validate_stage3_output(valid_text)
        self.assertEqual(len(parsed["candidates"]), 3)

        invalid_text = json.dumps({"candidates": [{"name": "A"}, {"name": "B"}]})
        with self.assertRaises(ValueError):
            module.validate_stage3_output(invalid_text)

    def test_parse_stage4_output_extracts_final_json_block(self) -> None:
        module = load_module()

        raw_text = """# Critique

- threat 1
- threat 2

```json
{"recommended_primary": null, "recommend_descriptive_fallback": true}
```
"""
        critique_md, critique_meta = module.parse_stage4_output(raw_text)
        self.assertIn("# Critique", critique_md)
        self.assertTrue(critique_meta["recommend_descriptive_fallback"])

    def test_validate_stage5_output_detects_claim_evidence_table(self) -> None:
        module = load_module()

        valid_text = """## Claim-Evidence Table

| Claim | Evidence Used | Claim Type | Confidence | What would falsify this claim |
|---|---|---|---|---|
| A | B | C | D | E |
"""
        self.assertTrue(module.validate_stage5_output(valid_text))

        invalid_text = "No table here"
        with self.assertRaises(ValueError):
            module.validate_stage5_output(invalid_text)

    def test_pipeline_manifest_writer_updates_stage_without_main_manifest_side_effect(self) -> None:
        module = load_module()

        with tempfile.TemporaryDirectory() as tmpdir:
            run_dir = Path(tmpdir)
            manifest_path = run_dir / "pipeline_manifest.json"
            module.initialize_pipeline_manifest(
                manifest_path=manifest_path,
                case_id="C001",
                variant_id="perturbed",
                input_packet_sha256="abc123",
            )
            module.update_pipeline_manifest(
                manifest_path=manifest_path,
                stage_name="stage3_candidates",
                stage_status={
                    "status": "ok",
                    "retries": 0,
                    "artifact_path": "stage3_candidates/artifact.json",
                },
            )

            manifest = json.loads(manifest_path.read_text())
            self.assertEqual(manifest["case_id"], "C001")
            self.assertEqual(manifest["stages"]["stage3_candidates"]["status"], "ok")
            self.assertFalse((run_dir / "run_manifest.csv").exists())

    def test_build_runner_env_preserves_existing_path(self) -> None:
        module = load_module()

        env = module.build_runner_env("high")

        self.assertEqual(env["THINKING_LEVEL"], "high")
        self.assertEqual(env["PATH"], os.environ["PATH"])

    def test_stage_status_can_record_stderr_path(self) -> None:
        module = load_module()

        status = module.stage_status(
            status="ok",
            retries=0,
            artifact_path="stage5_final/artifact.md",
            duration=12.3,
            validation="claim_table_present",
            stderr_path="stage5_final/stderr.log",
        )

        self.assertEqual(status["stderr_path"], "stage5_final/stderr.log")


if __name__ == "__main__":
    unittest.main()
