import unittest

from scripts.split_report_quality_rubric_keys import MASTER_PATH, parse_master_keys


class ReportQualityRubricSplitTest(unittest.TestCase):
    def test_parse_master_keys_has_expected_cases_and_sections(self) -> None:
        sections = parse_master_keys(MASTER_PATH.read_text(encoding="utf-8"))
        self.assertEqual(
            sorted(sections),
            ["C001", "C002", "C004", "C005", "C008", "C010", "C014", "C016", "C019", "C020"],
        )
        c001 = sections["C001"]
        self.assertIn("Key identification boundary", c001.base_common)
        self.assertIn("What changed", c001.perturbed)
        self.assertIn("What's missing", c001.no_solution)
        self.assertEqual(set(c001.level_notes), {"level1", "level2", "level3"})


if __name__ == "__main__":
    unittest.main()
