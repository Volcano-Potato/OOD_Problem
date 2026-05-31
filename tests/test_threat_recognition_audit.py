import csv
import importlib.util
import tempfile
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
SCRIPT_PATH = REPO_ROOT / "scripts" / "build_threat_recognition_audit.py"


def load_module():
    spec = importlib.util.spec_from_file_location("build_threat_recognition_audit", SCRIPT_PATH)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


class ThreatRecognitionAuditTests(unittest.TestCase):
    def test_summary_metrics_and_markdown(self) -> None:
        module = load_module()

        rows = [
            {
                "case_id": "C001",
                "level2_run_id": "RUN_A",
                "threat_1": "Threat A1",
                "threat_1_gold_basis": "gold A1",
                "threat_1_hit": "yes",
                "threat_1_evidence": "evidence A1",
                "threat_2": "Threat A2",
                "threat_2_gold_basis": "gold A2",
                "threat_2_hit": "yes",
                "threat_2_evidence": "evidence A2",
                "hits": "2",
                "max_hits": "2",
                "audit_note": "complete recognition",
            },
            {
                "case_id": "C002",
                "level2_run_id": "RUN_B",
                "threat_1": "Threat B1",
                "threat_1_gold_basis": "gold B1",
                "threat_1_hit": "yes",
                "threat_1_evidence": "evidence B1",
                "threat_2": "Threat B2",
                "threat_2_gold_basis": "gold B2",
                "threat_2_hit": "no",
                "threat_2_evidence": "evidence B2",
                "hits": "1",
                "max_hits": "2",
                "audit_note": "partial recognition",
            },
            {
                "case_id": "C003",
                "level2_run_id": "RUN_C",
                "threat_1": "Threat C1",
                "threat_1_gold_basis": "gold C1",
                "threat_1_hit": "no",
                "threat_1_evidence": "evidence C1",
                "threat_2": "Threat C2",
                "threat_2_gold_basis": "gold C2",
                "threat_2_hit": "no",
                "threat_2_evidence": "evidence C2",
                "hits": "0",
                "max_hits": "2",
                "audit_note": "missed both",
            },
        ]

        summary = module.summarize_rows(rows)
        self.assertEqual(summary["case_count"], 3)
        self.assertEqual(summary["total_hits"], 3)
        self.assertEqual(summary["max_possible_hits"], 6)
        self.assertAlmostEqual(summary["average_hits_per_case"], 1.0)
        self.assertAlmostEqual(summary["overall_hit_rate"], 0.5)
        self.assertEqual(summary["two_of_two_cases"], 1)
        self.assertEqual(summary["one_of_two_cases"], 1)
        self.assertEqual(summary["zero_of_two_cases"], 1)

        with tempfile.TemporaryDirectory() as tmpdir:
            out = Path(tmpdir) / "summary.md"
            module.write_markdown(rows, out)
            text = out.read_text()
            self.assertIn("Average threat hits per case", text)
            self.assertIn("`1/3` cases scored `2/2`", text)
            self.assertIn("`1/3` cases scored `0/2`", text)
            self.assertIn("| `C002` | `1/2` |", text)


if __name__ == "__main__":
    unittest.main()
