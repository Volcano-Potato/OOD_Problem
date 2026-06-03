import unittest
from pathlib import Path


class ReportQualityJudgePromptsTest(unittest.TestCase):
    def test_absolute_scoring_prompt_contains_required_constraints(self) -> None:
        path = Path("benchmark/prompts/report_quality_judge/absolute_scoring_prompt.md")
        text = path.read_text(encoding="utf-8")
        self.assertIn("Return only valid JSON", text)
        self.assertIn("Do not reward length", text)
        self.assertIn("no_solution", text)
        self.assertIn("identification_alignment", text)
        self.assertIn("fallback_design_present", text)
        self.assertIn("ceiling_respected", text)
        self.assertIn("core_failure_present", text)
        self.assertIn("decimal scores", text)
        self.assertIn("mechanical_reuse_present = yes", text)

    def test_axis_a_ranking_prompt_contains_required_constraints(self) -> None:
        path = Path("benchmark/prompts/report_quality_judge/axis_a_ranking_prompt.md")
        text = path.read_text(encoding="utf-8")
        self.assertIn("Report A", text)
        self.assertIn("Return only valid JSON", text)
        self.assertIn("Do not reward length", text)
        self.assertIn("closest_pair", text)
        self.assertIn("main_separator", text)

    def test_axis_a_pairwise_prompt_contains_required_constraints(self) -> None:
        path = Path("benchmark/prompts/report_quality_judge/axis_a_pairwise_baseline_prompt.md")
        text = path.read_text(encoding="utf-8")
        self.assertIn("Report A", text)
        self.assertIn("Report B", text)
        self.assertIn("winner", text)
        self.assertIn("Do not reward length", text)
        self.assertIn("mechanical_reuse_present_A", text)
        self.assertIn("Do not reward a report merely for giving a more detailed explanation", text)
        self.assertIn("Count boundary-respecting improvements, not rhetorical thoroughness", text)


if __name__ == "__main__":
    unittest.main()
