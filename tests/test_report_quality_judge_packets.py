import tempfile
import unittest
from pathlib import Path

from scripts.split_report_quality_rubric_keys import (
    AXIS_A_INDEX_PATH,
    AXIS_B_INDEX_PATH,
)
from scripts.build_report_quality_judge_packets import (
    AXIS_A_PAIRWISE_PROMPT_PATH,
    build_ranking_assignment,
    build_pairwise_assignment,
    extract_report_body_from_main_raw_log,
    generate_judge_packets,
)


class ReportQualityJudgePacketsTest(unittest.TestCase):
    def test_extract_report_body_from_main_raw_log_drops_header(self) -> None:
        path = Path(
            "outputs/raw_agent_logs/main/"
            "C001_perturbed_openclaw_RUN_20260528_173940_01_openclaw_deepseekv4pro_isolated.md"
        )
        body = extract_report_body_from_main_raw_log(path)
        self.assertTrue(body.startswith("# Research Design:"))
        self.assertNotIn("## Raw Agent Output", body)
        self.assertNotIn("system_prompt_summary", body)

    def test_build_ranking_assignment_is_deterministic_and_complete(self) -> None:
        first = build_ranking_assignment("C001")
        second = build_ranking_assignment("C001")
        self.assertEqual(first, second)
        self.assertEqual(set(first.keys()), {"A", "B", "C", "D"})
        self.assertEqual(set(first.values()), {"baseline", "v1", "v2", "v3"})

    def test_build_pairwise_assignment_is_deterministic_and_complete(self) -> None:
        first = build_pairwise_assignment("C001", "v2")
        second = build_pairwise_assignment("C001", "v2")
        self.assertEqual(first, second)
        self.assertEqual(set(first.keys()), {"A", "B"})
        self.assertEqual(set(first.values()), {"baseline", "v2"})

    def test_generate_judge_packets_writes_expected_counts(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            output_root = Path(tmpdir)
            counts = generate_judge_packets(
                axis_a_index_path=AXIS_A_INDEX_PATH,
                axis_b_index_path=AXIS_B_INDEX_PATH,
                output_root=output_root,
            )
            self.assertEqual(counts["axis_a_absolute_packets"], 40)
            self.assertEqual(counts["axis_a_ranking_packets"], 10)
            self.assertEqual(counts["axis_a_pairwise_packets"], 30)
            self.assertEqual(counts["axis_b_absolute_packets"], 50)
            self.assertEqual(counts["packet_manifest_rows"], 130)
            self.assertTrue((output_root / "axis_a" / "C001" / "baseline" / "packet_manifest.json").exists())
            self.assertTrue((output_root / "axis_a" / "C001" / "baseline" / "judge_input.md").exists())
            self.assertTrue((output_root / "axis_a" / "C001" / "baseline" / "judge_request.md").exists())
            self.assertTrue(
                (output_root / "axis_a" / "C001" / "within_case_ranking" / "report_A.md").exists()
            )
            self.assertTrue(
                (output_root / "axis_a" / "C001" / "within_case_ranking" / "judge_input.md").exists()
            )
            self.assertTrue(
                (output_root / "axis_a" / "C001" / "within_case_ranking" / "judge_request.md").exists()
            )
            self.assertTrue(
                (output_root / "axis_a" / "C001" / "pairwise_vs_baseline_v2" / "judge_request.md").exists()
            )
            self.assertTrue((output_root / "axis_b" / "C001_level1" / "packet_manifest.json").exists())
            self.assertTrue((output_root / "axis_b" / "C001_level1" / "judge_input.md").exists())
            self.assertTrue((output_root / "axis_b" / "C001_level1" / "judge_request.md").exists())

    def test_generated_judge_input_has_expected_section_order(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            output_root = Path(tmpdir)
            generate_judge_packets(
                axis_a_index_path=AXIS_A_INDEX_PATH,
                axis_b_index_path=AXIS_B_INDEX_PATH,
                output_root=output_root,
            )
            absolute_text = (output_root / "axis_a" / "C001" / "baseline" / "judge_input.md").read_text()
            self.assertIn("## Task Packet", absolute_text)
            self.assertIn("## Rubric Key", absolute_text)
            self.assertIn("## Final Report", absolute_text)
            self.assertLess(absolute_text.find("## Task Packet"), absolute_text.find("## Rubric Key"))
            self.assertLess(absolute_text.find("## Rubric Key"), absolute_text.find("## Final Report"))

            ranking_text = (
                output_root / "axis_a" / "C001" / "within_case_ranking" / "judge_input.md"
            ).read_text()
            for header in ["## Task Packet", "## Rubric Key", "## Report A", "## Report B", "## Report C", "## Report D"]:
                self.assertIn(header, ranking_text)

            pairwise_text = (
                output_root / "axis_a" / "C001" / "pairwise_vs_baseline_v2" / "judge_input.md"
            ).read_text()
            for header in ["## Task Packet", "## Rubric Key", "## Report A", "## Report B"]:
                self.assertIn(header, pairwise_text)

    def test_generated_judge_request_uses_correct_prompt_for_packet_type(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            output_root = Path(tmpdir)
            generate_judge_packets(
                axis_a_index_path=AXIS_A_INDEX_PATH,
                axis_b_index_path=AXIS_B_INDEX_PATH,
                output_root=output_root,
            )
            axis_a_abs = (output_root / "axis_a" / "C001" / "baseline" / "judge_request.md").read_text()
            self.assertIn("# Report-Quality Judge Prompt: Absolute Scoring", axis_a_abs)
            self.assertIn("## Final Report", axis_a_abs)

            axis_a_rank = (
                output_root / "axis_a" / "C001" / "within_case_ranking" / "judge_request.md"
            ).read_text()
            self.assertIn("# Report-Quality Judge Prompt: Axis A Within-Case Ranking", axis_a_rank)
            self.assertIn("## Report A", axis_a_rank)

            axis_a_pairwise = (
                output_root / "axis_a" / "C001" / "pairwise_vs_baseline_v2" / "judge_request.md"
            ).read_text()
            self.assertIn("# Report-Quality Judge Prompt: Axis A Pairwise Baseline Comparison", axis_a_pairwise)
            self.assertIn("## Report B", axis_a_pairwise)

            axis_b_abs = (output_root / "axis_b" / "C001_level1" / "judge_request.md").read_text()
            self.assertIn("# Report-Quality Judge Prompt: Absolute Scoring", axis_b_abs)
            self.assertNotIn("# Report-Quality Judge Prompt: Axis A Within-Case Ranking", axis_b_abs)
            self.assertEqual(
                AXIS_A_PAIRWISE_PROMPT_PATH.name,
                "axis_a_pairwise_baseline_prompt.md",
            )


if __name__ == "__main__":
    unittest.main()
