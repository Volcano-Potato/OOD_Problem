import json
import os
import tempfile
import unittest
from pathlib import Path

from scripts.run_report_quality_judge_batch import (
    append_pairwise_result,
    build_anthropic_messages_url,
    build_generate_content_url,
    build_request_payload,
    default_base_url_for_provider,
    ensure_local_env_loaded,
    extract_response_text,
    load_local_env_file,
    normalize_provider,
    normalize_json_text,
)


class ReportQualityJudgeRunnerTest(unittest.TestCase):
    def test_build_generate_content_url_normalizes_v1beta(self) -> None:
        url = build_generate_content_url(
            base_url="https://api.aigocode.com",
            model="gemini-3.5-flash",
            api_key="KEY123",
        )
        self.assertEqual(
            url,
            "https://api.aigocode.com/v1beta/models/gemini-3.5-flash:generateContent?key=KEY123",
        )

    def test_build_anthropic_messages_url_normalizes_v1(self) -> None:
        self.assertEqual(
            build_anthropic_messages_url("https://api.aigocode.com"),
            "https://api.aigocode.com/v1/messages",
        )

    def test_build_request_payload_uses_gemini_text_shape(self) -> None:
        payload = build_request_payload("hello world", provider="gemini", model="gemini-3.5-flash")
        self.assertEqual(payload["contents"][0]["parts"][0]["text"], "hello world")
        self.assertEqual(payload["generationConfig"]["responseMimeType"], "application/json")
        self.assertEqual(payload["generationConfig"]["temperature"], 0)

    def test_build_request_payload_uses_anthropic_messages_shape(self) -> None:
        payload = build_request_payload("hello world", provider="anthropic", model="claude-sonnet-4-6")
        self.assertEqual(payload["model"], "claude-sonnet-4-6")
        self.assertEqual(payload["messages"][0]["role"], "user")
        self.assertEqual(payload["messages"][0]["content"], "hello world")
        self.assertEqual(payload["temperature"], 0)

    def test_extract_response_text_reads_first_candidate_parts(self) -> None:
        payload = {
            "candidates": [
                {
                    "content": {
                        "parts": [
                            {"text": '{"a": 1}'},
                        ]
                    }
                }
            ]
        }
        self.assertEqual(extract_response_text(payload, provider="gemini"), '{"a": 1}')

    def test_extract_response_text_reads_anthropic_text_blocks(self) -> None:
        payload = {
            "content": [
                {"type": "text", "text": '{"a": 1}'},
            ]
        }
        self.assertEqual(extract_response_text(payload, provider="anthropic"), '{"a": 1}')

    def test_normalize_json_text_strips_markdown_fences(self) -> None:
        fenced = "```json\n{\"a\": 1}\n```"
        normalized = normalize_json_text(fenced)
        self.assertEqual(json.loads(normalized), {"a": 1})

    def test_provider_helpers(self) -> None:
        self.assertEqual(normalize_provider("Anthropic"), "anthropic")
        self.assertEqual(default_base_url_for_provider("gemini"), "https://api.aigocode.com/v1beta")
        self.assertEqual(default_base_url_for_provider("anthropic"), "https://api.aigocode.com/v1")

    def test_append_pairwise_result_derives_challenger_outcome(self) -> None:
        rows = []
        row = {
            "axis": "axis_a",
            "packet_type": "pairwise_vs_baseline",
            "case_id": "C001",
            "variant_id": "perturbed",
            "agent_variant": "baseline_vs_v2",
            "judge_request_path": "foo",
            "prompt_path": "bar",
            "blind_label": "{\"A\": \"baseline\", \"B\": \"v2\"}",
            "notes": "",
        }
        parsed = {
            "winner": "B",
            "confidence": "high",
            "better_boundary_report": "B",
            "better_downgrade_report": "B",
            "mechanical_reuse_present_A": "yes",
            "mechanical_reuse_present_B": "no",
            "reason_tags": ["better_downgrade"],
            "short_reason": "ok",
        }
        append_pairwise_result(row, parsed, rows, "deepseek-v4-flash")
        self.assertEqual(rows[0]["challenger"], "v2")
        self.assertEqual(rows[0]["winner_arm"], "v2")
        self.assertEqual(rows[0]["challenger_beats_baseline"], "yes")

    def test_load_local_env_file_parses_quoted_values(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            env_path = Path(tmpdir) / ".benchmark.local.env"
            env_path.write_text(
                "LLM_JUDGE_API_KEY='abc123'\n"
                'LLM_JUDGE_MODEL="gemini-3.5-flash"\n'
                "# comment\n",
                encoding="utf-8",
            )
            loaded = load_local_env_file(env_path)
        self.assertEqual(
            loaded,
            {
                "LLM_JUDGE_API_KEY": "abc123",
                "LLM_JUDGE_MODEL": "gemini-3.5-flash",
            },
        )

    def test_ensure_local_env_loaded_preserves_existing_env(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            env_path = Path(tmpdir) / ".benchmark.local.env"
            env_path.write_text("LLM_JUDGE_API_KEY=file_value\nLLM_JUDGE_MODEL=file_model\n", encoding="utf-8")
            original_key = os.environ.get("LLM_JUDGE_API_KEY")
            original_model = os.environ.get("LLM_JUDGE_MODEL")
            try:
                os.environ["LLM_JUDGE_API_KEY"] = "existing"
                os.environ.pop("LLM_JUDGE_MODEL", None)
                ensure_local_env_loaded(env_path)
                self.assertEqual(os.environ["LLM_JUDGE_API_KEY"], "existing")
                self.assertEqual(os.environ["LLM_JUDGE_MODEL"], "file_model")
            finally:
                if original_key is None:
                    os.environ.pop("LLM_JUDGE_API_KEY", None)
                else:
                    os.environ["LLM_JUDGE_API_KEY"] = original_key
                if original_model is None:
                    os.environ.pop("LLM_JUDGE_MODEL", None)
                else:
                    os.environ["LLM_JUDGE_MODEL"] = original_model


if __name__ == "__main__":
    unittest.main()
