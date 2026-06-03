import csv
import importlib.util
import json
import os
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]


def load_script_module(relative_path: str, module_name: str):
    path = REPO_ROOT / relative_path
    spec = importlib.util.spec_from_file_location(module_name, path)
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


class AgentVariantPipelineTests(unittest.TestCase):
    def test_compute_metrics_special_cases_v2_perturbed_audit_path(self) -> None:
        module = load_script_module("scripts/compute_benchmark_metrics.py", "compute_benchmark_metrics_paths")
        self.assertEqual(
            module.perturbed_audit_path_for_variant("research_agent_v1").name,
            "perturbed_mechanical_reuse_v1.csv",
        )
        self.assertEqual(
            module.perturbed_audit_path_for_variant("research_agent_v2_search").name,
            "perturbed_mechanical_reuse_v2.csv",
        )
        self.assertEqual(
            module.perturbed_audit_path_for_variant("research_agent_v3_planner_debate").name,
            "perturbed_mechanical_reuse_v3.csv",
        )

    def test_compute_metrics_builds_error_counts_by_agent_variant(self) -> None:
        module = load_script_module("scripts/compute_benchmark_metrics.py", "compute_metrics_error_counts")
        rows = [
            {"agent_variant": "benchmark_isolated", "final_error_type": "Overclaim"},
            {"agent_variant": "benchmark_isolated", "final_error_type": "none"},
            {"agent_variant": "research_agent_v1", "final_error_type": "none"},
            {"agent_variant": "research_agent_v2_search", "final_error_type": "Unsupported Claim"},
            {"agent_variant": "research_agent_v3_planner_debate", "final_error_type": "Contradiction"},
        ]
        counts = module.build_error_counts_by_agent_variant(rows)
        by_key = {(row["agent_variant"], row["error_type"]): row for row in counts}
        self.assertEqual(by_key[("benchmark_isolated", "Overclaim")]["count"], 1)
        self.assertEqual(by_key[("benchmark_isolated", "none")]["n_claims"], 2)
        self.assertEqual(by_key[("research_agent_v1", "none")]["count"], 1)
        self.assertEqual(by_key[("research_agent_v2_search", "Unsupported Claim")]["count"], 1)
        self.assertEqual(by_key[("research_agent_v3_planner_debate", "Contradiction")]["count"], 1)

    def test_postprocess_uses_session_file_as_tool_truth_source(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            repo_root = Path(tmpdir)
            manifest_path = repo_root / "outputs" / "run_manifest.csv"
            write_csv(
                manifest_path,
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

            session_path = repo_root / "tmp" / "sess123.jsonl"
            session_path.parent.mkdir(parents=True, exist_ok=True)
            session_path.write_text(
                "\n".join(
                    [
                        '{"type":"message","message":{"role":"assistant","content":[{"type":"toolCall","id":"call_1","name":"web_search","arguments":{"query":"q"}}]}}',
                        '{"type":"message","message":{"role":"toolResult","toolCallId":"call_1","toolName":"web_search","content":[{"type":"text","text":"ok"}]}}',
                    ]
                )
                + "\n"
            )

            json_path = repo_root / "run.json"
            json_path.write_text(
                json.dumps(
                    {
                        "payloads": [{"text": "final output"}],
                        "meta": {
                            "durationMs": 1234,
                            "agentMeta": {
                                "sessionId": "sess123",
                                "sessionFile": str(session_path),
                                "model": "deepseek-v4-pro",
                                "provider": "deepseek",
                            },
                        },
                    }
                )
            )
            stderr_path = repo_root / "run.stderr"
            stderr_path.write_text("")

            env = os.environ.copy()
            env["OPENCLAW_RUN_EXIT_CODE"] = "0"
            subprocess.run(
                [
                    sys.executable,
                    str(REPO_ROOT / "scripts" / "postprocess_openclaw_run.py"),
                    "--repo-root",
                    str(repo_root),
                    "--json-path",
                    "run.json",
                    "--stderr-path",
                    "run.stderr",
                    "--run-id",
                    "RUN_SESSION_TRUTH",
                    "--case-id",
                    "C001",
                    "--variant-id",
                    "perturbed",
                    "--level",
                    "perturbed",
                    "--split",
                    "main",
                    "--input-file",
                    "benchmark/cases/C001/agent_task_perturbed.md",
                    "--session-id",
                    "sess123",
                    "--timestamp",
                    "2026-06-01T12:00:00+08:00",
                    "--timeout-seconds",
                    "1800",
                    "--thinking-level",
                    "medium",
                ],
                check=True,
                cwd=REPO_ROOT,
                env=env,
            )

            with manifest_path.open(newline="") as handle:
                rows = list(csv.DictReader(handle))
            self.assertEqual(len(rows), 1)
            self.assertIn("actual tool use=web_search", rows[0]["contamination_reason"])

            raw_output_rel = rows[0]["raw_output_file"]
            raw_output_text = (repo_root / raw_output_rel).read_text()
            self.assertIn("actual tool use: web_search", raw_output_text)
            self.assertIn("toolCall count: 1", raw_output_text)
            self.assertIn("toolResult count: 1", raw_output_text)

    def test_postprocess_upgrades_manifest_header_for_retrieval_fields(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            repo_root = Path(tmpdir)
            manifest_path = repo_root / "outputs" / "run_manifest.csv"
            write_csv(
                manifest_path,
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

            session_path = repo_root / "tmp" / "sess456.jsonl"
            session_path.parent.mkdir(parents=True, exist_ok=True)
            session_path.write_text(
                "\n".join(
                    [
                        '{"type":"message","message":{"role":"assistant","content":[{"type":"toolCall","id":"call_1","name":"web_search","arguments":{"query":"q"}}]}}',
                        '{"type":"message","message":{"role":"toolResult","toolCallId":"call_1","toolName":"web_search","content":[{"type":"text","text":"ok"}]}}',
                    ]
                )
                + "\n"
            )

            json_path = repo_root / "run.json"
            json_path.write_text(
                json.dumps(
                    {
                        "payloads": [{"text": "final output"}],
                        "meta": {
                            "durationMs": 1234,
                            "agentMeta": {
                                "sessionId": "sess456",
                                "sessionFile": str(session_path),
                                "model": "deepseek-v4-pro",
                                "provider": "deepseek",
                            },
                        },
                    }
                )
            )
            stderr_path = repo_root / "run.stderr"
            stderr_path.write_text("")

            env = os.environ.copy()
            env["OPENCLAW_RUN_EXIT_CODE"] = "0"
            subprocess.run(
                [
                    sys.executable,
                    str(REPO_ROOT / "scripts" / "postprocess_openclaw_run.py"),
                    "--repo-root",
                    str(repo_root),
                    "--json-path",
                    "run.json",
                    "--stderr-path",
                    "run.stderr",
                    "--run-id",
                    "RUN_MANIFEST_UPGRADE",
                    "--case-id",
                    "C005",
                    "--variant-id",
                    "perturbed",
                    "--level",
                    "perturbed",
                    "--split",
                    "main",
                    "--input-file",
                    "benchmark/cases/C005/agent_task_perturbed.md",
                    "--session-id",
                    "sess456",
                    "--timestamp",
                    "2026-06-01T12:00:00+08:00",
                    "--timeout-seconds",
                    "1800",
                    "--thinking-level",
                    "medium",
                    "--retrieval-attempted-override",
                    "true",
                    "--retrieval-successful-override",
                    "true",
                    "--retrieval-tool-calls-override",
                    "5",
                    "--retrieval-failure-reason-override",
                    "",
                ],
                check=True,
                cwd=REPO_ROOT,
                env=env,
            )

            with manifest_path.open(newline="") as handle:
                reader = csv.DictReader(handle)
                rows = list(reader)
                fieldnames = reader.fieldnames or []
            self.assertIn("retrieval_attempted", fieldnames)
            self.assertIn("retrieval_successful", fieldnames)
            self.assertIn("retrieval_tool_calls", fieldnames)
            self.assertEqual(rows[0]["retrieval_attempted"], "true")
            self.assertEqual(rows[0]["retrieval_successful"], "true")
            self.assertEqual(rows[0]["retrieval_tool_calls"], "5")

    def test_postprocess_records_agent_variant_and_variant_filename(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            repo_root = Path(tmpdir)
            manifest_path = repo_root / "outputs" / "run_manifest.csv"
            write_csv(
                manifest_path,
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

            json_path = repo_root / "run.json"
            json_path.write_text(
                """{
  "payloads": [{"text": "final output"}],
  "meta": {
    "durationMs": 1234,
    "agentMeta": {"model": "deepseek-v4-pro", "provider": "deepseek"}
  }
}
"""
            )
            stderr_path = repo_root / "run.stderr"
            stderr_path.write_text("")

            env = os.environ.copy()
            env["OPENCLAW_RUN_EXIT_CODE"] = "0"
            subprocess.run(
                [
                    sys.executable,
                    str(REPO_ROOT / "scripts" / "postprocess_openclaw_run.py"),
                    "--repo-root",
                    str(repo_root),
                    "--json-path",
                    "run.json",
                    "--stderr-path",
                    "run.stderr",
                    "--run-id",
                    "RUN_TEST",
                    "--case-id",
                    "C001",
                    "--variant-id",
                    "perturbed",
                    "--level",
                    "perturbed",
                    "--split",
                    "main",
                    "--input-file",
                    "benchmark/cases/C001/agent_task_perturbed.md",
                    "--session-id",
                    "SESSION_TEST",
                    "--timestamp",
                    "2026-05-31T12:00:00+08:00",
                    "--timeout-seconds",
                    "1800",
                    "--thinking-level",
                    "medium",
                    "--agent-variant",
                    "research_agent_v1",
                ],
                check=True,
                cwd=REPO_ROOT,
                env=env,
            )

            with manifest_path.open(newline="") as handle:
                rows = list(csv.DictReader(handle))
            self.assertEqual(len(rows), 1)
            self.assertEqual(rows[0]["agent_variant"], "research_agent_v1")
            self.assertIn("__research_agent_v1__", rows[0]["raw_output_file"])

    def test_extract_agent_claims_preserves_agent_variant(self) -> None:
        module = load_script_module(
            "scripts/extract_agent_claims.py",
            "extract_agent_claims_test",
        )

        with tempfile.TemporaryDirectory() as tmpdir:
            root = Path(tmpdir)
            raw_rel = "outputs/raw_agent_logs/main/C001_level2__research_agent_v1__RUN_TEST.md"
            raw_path = root / raw_rel
            raw_path.parent.mkdir(parents=True, exist_ok=True)
            raw_path.write_text(
                """# Raw Agent Run Log

## Raw Agent Output

| Claim | Evidence Used | Claim Type | Confidence | What would falsify this claim |
|---|---|---|---|---|
| A valid claim | Packet evidence | Causal (ITT) | High | Null estimate |
"""
            )

            manifest_path = root / "outputs" / "run_manifest.csv"
            write_csv(
                manifest_path,
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
                [
                    {
                        "run_id": "RUN_TEST",
                        "case_id": "C001",
                        "variant_id": "level2",
                        "level": "level2",
                        "agent_name": "openclaw",
                        "agent_variant": "research_agent_v1",
                        "model": "deepseek-v4-pro",
                        "model_provider": "deepseek",
                        "openclaw_build_or_version": "2026.5.5",
                        "temperature": "not_supported",
                        "top_p": "not_supported",
                        "max_tokens": "not_supported",
                        "seed": "not_supported",
                        "tools_enabled": "enabled",
                        "closed_book": "false",
                        "channel": "cli",
                        "timestamp": "2026-05-31T12:00:00+08:00",
                        "input_file": "benchmark/cases/C001/agent_task_level2.md",
                        "raw_output_file": raw_rel,
                        "status": "success",
                        "contamination_status": "unknown",
                        "contamination_reason": "pending",
                        "notes": "",
                    }
                ],
            )

            output_dir = root / "outputs" / "parsed_claims"
            module.ROOT = root
            module.MANIFEST = manifest_path
            module.OUTPUT_DIR = output_dir
            module.CLAIMS_CSV = output_dir / "claims_to_annotate.csv"
            module.SKIPPED_CSV = output_dir / "claim_extraction_skipped.csv"
            module.SUMMARY_MD = output_dir / "claim_extraction_summary.md"

            module.main()

            with module.CLAIMS_CSV.open(newline="") as handle:
                rows = list(csv.DictReader(handle))
            self.assertEqual(rows[0]["agent_variant"], "research_agent_v1")

    def test_annotation_chain_preserves_agent_variant(self) -> None:
        first_pass = load_script_module(
            "scripts/build_first_pass_annotations.py",
            "build_first_pass_annotations_test",
        )
        adjudication = load_script_module(
            "scripts/build_second_labels_and_adjudication.py",
            "build_second_labels_and_adjudication_test",
        )

        with tempfile.TemporaryDirectory() as tmpdir:
            root = Path(tmpdir)
            claims_csv = root / "outputs" / "parsed_claims" / "claims_to_annotate.csv"
            write_csv(
                claims_csv,
                [
                    "case_id",
                    "variant_id",
                    "level",
                    "agent_variant",
                    "run_id",
                    "claim_id",
                    "claim_type",
                    "agent_claim",
                    "cited_evidence",
                    "confidence",
                    "what_would_falsify_this_claim",
                    "verbatim_quote",
                    "source_section",
                    "raw_output_file",
                    "notes",
                ],
                [
                    {
                        "case_id": "C001",
                        "variant_id": "level2",
                        "level": "level2",
                        "agent_variant": "research_agent_v1",
                        "run_id": "RUN_TEST",
                        "claim_id": "RUN_TEST_CL001",
                        "claim_type": "Causal (ITT)",
                        "agent_claim": "A valid claim",
                        "cited_evidence": "Packet evidence",
                        "confidence": "High",
                        "what_would_falsify_this_claim": "Null estimate",
                        "verbatim_quote": "A valid claim",
                        "source_section": "Claim-Evidence Table",
                        "raw_output_file": "outputs/raw_agent_logs/main/C001_level2__research_agent_v1__RUN_TEST.md",
                        "notes": "extracted_from_claim_evidence_table",
                    }
                ],
            )

            annotation_csv = root / "annotations" / "annotation_sheet.csv"
            annotation_csv.parent.mkdir(parents=True, exist_ok=True)
            first_pass.CLAIMS_CSV = claims_csv
            first_pass.ANNOTATION_CSV = annotation_csv
            first_pass.main()

            with annotation_csv.open(newline="") as handle:
                annotation_rows = list(csv.DictReader(handle))
            self.assertEqual(annotation_rows[0]["agent_variant"], "research_agent_v1")

            second_labels = root / "annotations" / "second_labels.csv"
            adjudicated = root / "annotations" / "adjudicated_labels.csv"
            notes = root / "annotations" / "adjudication_notes.md"
            adjudication.FIRST_PASS = annotation_csv
            adjudication.SECOND_LABELS = second_labels
            adjudication.ADJUDICATED = adjudicated
            adjudication.ADJ_NOTES = notes
            adjudication.main()

            with second_labels.open(newline="") as handle:
                second_rows = list(csv.DictReader(handle))
            with adjudicated.open(newline="") as handle:
                adjudicated_rows = list(csv.DictReader(handle))

            self.assertEqual(second_rows[0]["agent_variant"], "research_agent_v1")
            self.assertEqual(adjudicated_rows[0]["agent_variant"], "research_agent_v1")

    def test_adjudication_preserves_frozen_baseline_rows_when_new_variant_is_added(self) -> None:
        adjudication = load_script_module(
            "scripts/build_second_labels_and_adjudication.py",
            "build_second_labels_and_adjudication_preserve_baseline_test",
        )

        with tempfile.TemporaryDirectory() as tmpdir:
            root = Path(tmpdir)
            first_pass_csv = root / "annotations" / "annotation_sheet.csv"
            write_csv(
                first_pass_csv,
                [
                    "case_id",
                    "variant_id",
                    "level",
                    "agent_name",
                    "agent_variant",
                    "run_id",
                    "claim_id",
                    "claim_type",
                    "agent_claim",
                    "cited_evidence",
                    "confidence",
                    "what_would_falsify_this_claim",
                    "raw_output_file",
                    "human_judgment",
                    "error_type",
                    "severity",
                    "explanation",
                    "annotator_id",
                    "notes",
                ],
                [
                    {
                        "case_id": "C001",
                        "variant_id": "level2",
                        "level": "level2",
                        "agent_name": "openclaw",
                        "agent_variant": "benchmark_isolated",
                        "run_id": "RUN_BASE",
                        "claim_id": "RUN_BASE_CL001",
                        "claim_type": "Causal (ITT)",
                        "agent_claim": "Baseline claim",
                        "cited_evidence": "packet",
                        "confidence": "High",
                        "what_would_falsify_this_claim": "null",
                        "raw_output_file": "outputs/raw_agent_logs/main/base.md",
                        "human_judgment": "supported",
                        "error_type": "none",
                        "severity": "",
                        "explanation": "baseline",
                        "annotator_id": "codex_first_pass",
                        "notes": "task20 first-pass",
                    },
                    {
                        "case_id": "C001",
                        "variant_id": "perturbed",
                        "level": "perturbed",
                        "agent_name": "openclaw",
                        "agent_variant": "research_agent_v1",
                        "run_id": "RUN_RA",
                        "claim_id": "RUN_RA_CL001",
                        "claim_type": "Descriptive",
                        "agent_claim": "RA claim",
                        "cited_evidence": "packet",
                        "confidence": "High",
                        "what_would_falsify_this_claim": "null",
                        "raw_output_file": "outputs/raw_agent_logs/main/ra.md",
                        "human_judgment": "supported",
                        "error_type": "none",
                        "severity": "",
                        "explanation": "ra",
                        "annotator_id": "codex_first_pass",
                        "notes": "task20 first-pass",
                    },
                ],
            )

            second_labels_csv = root / "annotations" / "second_labels.csv"
            adjudicated_csv = root / "annotations" / "adjudicated_labels.csv"
            notes_md = root / "annotations" / "adjudication_notes.md"

            write_csv(
                second_labels_csv,
                [
                    "case_id",
                    "variant_id",
                    "level",
                    "agent_name",
                    "agent_variant",
                    "run_id",
                    "claim_id",
                    "claim_type",
                    "agent_claim",
                    "labeler2_judgment",
                    "labeler2_error_type",
                    "labeler2_severity",
                    "labeler2_explanation",
                    "annotator_id",
                    "notes",
                ],
                [
                    {
                        "case_id": "C001",
                        "variant_id": "level2",
                        "level": "level2",
                        "agent_name": "openclaw",
                        "agent_variant": "benchmark_isolated",
                        "run_id": "RUN_BASE",
                        "claim_id": "RUN_BASE_CL001",
                        "claim_type": "Causal (ITT)",
                        "agent_claim": "Baseline claim",
                        "labeler2_judgment": "supported",
                        "labeler2_error_type": "none",
                        "labeler2_severity": "",
                        "labeler2_explanation": "baseline frozen second-pass",
                        "annotator_id": "codex_second_pass",
                        "notes": "frozen baseline",
                    }
                ],
            )

            write_csv(
                adjudicated_csv,
                [
                    "case_id",
                    "variant_id",
                    "level",
                    "agent_name",
                    "agent_variant",
                    "run_id",
                    "claim_id",
                    "claim_type",
                    "agent_claim",
                    "final_label",
                    "final_error_type",
                    "final_severity",
                    "adjudicator_id",
                    "adjudication_notes",
                ],
                [
                    {
                        "case_id": "C001",
                        "variant_id": "level2",
                        "level": "level2",
                        "agent_name": "openclaw",
                        "agent_variant": "benchmark_isolated",
                        "run_id": "RUN_BASE",
                        "claim_id": "RUN_BASE_CL001",
                        "claim_type": "Causal (ITT)",
                        "agent_claim": "Baseline claim",
                        "final_label": "supported",
                        "final_error_type": "none",
                        "final_severity": "",
                        "adjudicator_id": "codex_adjudication_pass",
                        "adjudication_notes": "baseline frozen adjudication",
                    }
                ],
            )

            adjudication.FIRST_PASS = first_pass_csv
            adjudication.SECOND_LABELS = second_labels_csv
            adjudication.ADJUDICATED = adjudicated_csv
            adjudication.ADJ_NOTES = notes_md
            adjudication.main()

            with second_labels_csv.open(newline="") as handle:
                second_rows = list(csv.DictReader(handle))
            with adjudicated_csv.open(newline="") as handle:
                adjudicated_rows = list(csv.DictReader(handle))

            baseline_second = [row for row in second_rows if row["agent_variant"] == "benchmark_isolated"]
            baseline_adjudicated = [row for row in adjudicated_rows if row["agent_variant"] == "benchmark_isolated"]

            self.assertEqual(len(baseline_second), 1)
            self.assertEqual(len(baseline_adjudicated), 1)
            self.assertEqual(baseline_second[0]["labeler2_explanation"], "baseline frozen second-pass")
            self.assertEqual(baseline_adjudicated[0]["adjudication_notes"], "baseline frozen adjudication")

    def test_metrics_freeze_baseline_and_emit_research_outputs(self) -> None:
        module = load_script_module(
            "scripts/compute_benchmark_metrics.py",
            "compute_benchmark_metrics_test",
        )

        with tempfile.TemporaryDirectory() as tmpdir:
            root = Path(tmpdir)
            metadata_path = root / "benchmark" / "cases" / "C001_demo" / "metadata.yaml"
            metadata_path.parent.mkdir(parents=True, exist_ok=True)
            metadata_path.write_text(
                """case_id: C001
anonymous_short_name: demo
selection:
  selected_for_main: true
taxonomy:
  domain: marketing
  subdomain: retail
  design_family: field_experiment
  variation_source: random_assignment
  assignment_level: shopper
  outcome_level: shopper
  unit_of_observation: shopper_visit
  key_failure_mode: mechanism_confounding
  secondary_failure_modes: []
  difficulty: medium
"""
            )

            labels_csv = root / "annotations" / "adjudicated_labels.csv"
            write_csv(
                labels_csv,
                [
                    "case_id",
                    "variant_id",
                    "level",
                    "agent_name",
                    "agent_variant",
                    "run_id",
                    "claim_id",
                    "claim_type",
                    "agent_claim",
                    "final_label",
                    "final_error_type",
                    "final_severity",
                    "adjudicator_id",
                    "adjudication_notes",
                ],
                [
                    {
                        "case_id": "C001",
                        "variant_id": "level2",
                        "level": "level2",
                        "agent_name": "openclaw",
                        "agent_variant": "benchmark_isolated",
                        "run_id": "RUN_BASE",
                        "claim_id": "RUN_BASE_CL001",
                        "claim_type": "Causal (ITT)",
                        "agent_claim": "Baseline claim",
                        "final_label": "supported",
                        "final_error_type": "none",
                        "final_severity": "",
                        "adjudicator_id": "codex",
                        "adjudication_notes": "baseline",
                    },
                    {
                        "case_id": "C001",
                        "variant_id": "perturbed",
                        "level": "perturbed",
                        "agent_name": "openclaw",
                        "agent_variant": "research_agent_v1",
                        "run_id": "RUN_RA",
                        "claim_id": "RUN_RA_CL001",
                        "claim_type": "Causal (ITT)",
                        "agent_claim": "Research claim",
                        "final_label": "unsupported",
                        "final_error_type": "Unsupported Claim",
                        "final_severity": "major",
                        "adjudicator_id": "codex",
                        "adjudication_notes": "research",
                    },
                ],
            )

            manifest_csv = root / "outputs" / "run_manifest.csv"
            write_csv(
                manifest_csv,
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
                [
                    {
                        "run_id": "RUN_BASE",
                        "case_id": "C001",
                        "variant_id": "level2",
                        "level": "level2",
                        "agent_name": "openclaw",
                        "agent_variant": "benchmark_isolated",
                        "model": "deepseek-v4-pro",
                        "model_provider": "deepseek",
                        "openclaw_build_or_version": "2026.5.5",
                        "temperature": "not_supported",
                        "top_p": "not_supported",
                        "max_tokens": "not_supported",
                        "seed": "not_supported",
                        "tools_enabled": "enabled",
                        "closed_book": "false",
                        "channel": "cli",
                        "timestamp": "2026-05-31T12:00:00+08:00",
                        "input_file": "benchmark/cases/C001/agent_task_level2.md",
                        "raw_output_file": "outputs/raw_agent_logs/main/C001_level2_openclaw_RUN_BASE.md",
                        "status": "success",
                        "contamination_status": "unknown",
                        "contamination_reason": "pending",
                        "notes": "",
                    },
                    {
                        "run_id": "RUN_RA",
                        "case_id": "C001",
                        "variant_id": "perturbed",
                        "level": "perturbed",
                        "agent_name": "openclaw",
                        "agent_variant": "research_agent_v1",
                        "model": "deepseek-v4-pro",
                        "model_provider": "deepseek",
                        "openclaw_build_or_version": "2026.5.5",
                        "temperature": "not_supported",
                        "top_p": "not_supported",
                        "max_tokens": "not_supported",
                        "seed": "not_supported",
                        "tools_enabled": "enabled",
                        "closed_book": "false",
                        "channel": "cli",
                        "timestamp": "2026-05-31T12:05:00+08:00",
                        "input_file": "benchmark/cases/C001/agent_task_perturbed.md",
                        "raw_output_file": "outputs/raw_agent_logs/main/C001_perturbed__research_agent_v1__RUN_RA.md",
                        "status": "success",
                        "contamination_status": "unknown",
                        "contamination_reason": "pending",
                        "notes": "",
                    },
                ],
            )

            perturbed_audit_csv = root / "results" / "perturbed_mechanical_reuse.csv"
            write_csv(
                perturbed_audit_csv,
                [
                    "case_id",
                    "level2_run_id",
                    "perturbed_run_id",
                    "broken_condition",
                    "level2_logic",
                    "perturbed_behavior",
                    "mechanical_reuse",
                    "audit_rationale",
                ],
                [],
            )

            results_dir = root / "results"
            figures_dir = results_dir / "figures"
            module.ROOT = root
            module.LABELS_CSV = labels_csv
            module.MANIFEST_CSV = manifest_csv
            module.RESULTS_DIR = results_dir
            module.FIGURES_DIR = figures_dir
            module.METRICS_SUMMARY_CSV = results_dir / "metrics_summary.csv"
            module.METRICS_SUMMARY_MD = results_dir / "metrics_summary.md"
            module.ERROR_COUNTS_CSV = results_dir / "error_type_counts.csv"
            module.CASE_LEVEL_CSV = results_dir / "case_level_scores.csv"
            module.RUN_LEVEL_CSV = results_dir / "run_level_scores.csv"
            module.GROUPED_CSV = results_dir / "grouped_metrics.csv"
            module.PERTURBED_AUDIT_CSV = perturbed_audit_csv

            module.main()

            with module.METRICS_SUMMARY_CSV.open(newline="") as handle:
                metrics_rows = list(csv.DictReader(handle))
            total_claims_row = next(row for row in metrics_rows if row["metric"] == "Total Claims")
            self.assertEqual(total_claims_row["value"], "1")

            research_metrics_csv = results_dir / "metrics_summary_research_agent_v1.csv"
            self.assertTrue(research_metrics_csv.exists())
            with research_metrics_csv.open(newline="") as handle:
                research_rows = list(csv.DictReader(handle))
            research_total_claims_row = next(row for row in research_rows if row["metric"] == "Total Claims")
            self.assertEqual(research_total_claims_row["value"], "1")

            with module.GROUPED_CSV.open(newline="") as handle:
                grouped_rows = list(csv.DictReader(handle))
            group_types = {row["group_type"] for row in grouped_rows}
            self.assertIn("agent_variant", group_types)
            self.assertIn("agent_variant_x_variant_id", group_types)


if __name__ == "__main__":
    unittest.main()
