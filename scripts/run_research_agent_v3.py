#!/usr/bin/env python3

from __future__ import annotations

import argparse
import importlib.util
import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PROMPTS_DIR = ROOT / "benchmark" / "prompts" / "research_agent_v3"
DEFAULT_OUTPUT_ROOT = ROOT / "outputs" / "raw_agent_logs" / "research_agent_v3"
PLANNER_SCHEMA_HINT = """{
  "primary_estimand_hypotheses": ["itt on assignment"],
  "threat_checks": ["broken untreated comparator"],
  "search_priorities": ["interference bias"],
  "fallback_triggers": ["if no candidate survives the perturbation"],
  "final_decision_rule": "Prefer the weakest defensible estimand if causal identification fails."
}"""
ALLOWED_DISPOSITIONS = {"accept", "partial", "reject"}


def _load_v2_module():
    module_path = ROOT / "scripts" / "run_research_agent_v2.py"
    spec = importlib.util.spec_from_file_location("run_research_agent_v2", module_path)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


V2 = _load_v2_module()
read_text = V2.read_text
write_text = V2.write_text
sha256_text = V2.sha256_text
render_template = V2.render_template
extract_payload_text = V2.extract_payload_text
strip_optional_json_fence = V2.strip_optional_json_fence
validate_stage2_output = V2.validate_stage2_output
validate_stage3_output = V2.validate_stage3_output
validate_stage5_output = V2.validate_stage5_output
stage_status = V2.stage_status
build_openalex_seed_query = V2.build_openalex_seed_query
fetch_openalex_seed = V2.fetch_openalex_seed
save_openalex_seed = V2.save_openalex_seed
normalize_stage2_artifact = V2.normalize_stage2_artifact
run_stage_with_retry = V2.run_stage_with_retry
save_stage2_artifacts = V2.save_stage2_artifacts
save_stage3_artifact = V2.save_stage3_artifact
save_stage4_artifact = V2.save_stage4_artifact
save_stage5_artifact = V2.save_stage5_artifact
update_pipeline_manifest = V2.update_pipeline_manifest
finalize_pipeline_manifest = V2.finalize_pipeline_manifest
parse_case_and_variant = V2.parse_case_and_variant
create_run_dir = V2.create_run_dir


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Run a single-case research_agent_v3 smoke test.")
    parser.add_argument("--input-file", required=True)
    parser.add_argument("--output-root", default=str(DEFAULT_OUTPUT_ROOT))
    parser.add_argument("--timeout-seconds", type=int, default=1800)
    parser.add_argument("--thinking-level", default="high")
    parser.add_argument(
        "--start-from",
        choices=["stage0", "stage2", "stage3", "stage4", "stage3b", "stage4b", "stage5"],
        default="stage0",
    )
    parser.add_argument("--run-dir", help="Existing run directory required when resuming from a later stage.")
    return parser.parse_args()


def render_stage0_prompt(template_text: str, packet_text: str) -> str:
    return render_template(
        template_text,
        {
            "PACKET_TEXT": packet_text,
            "PLANNER_OUTPUT_SCHEMA_HINT": PLANNER_SCHEMA_HINT,
        },
    )


def render_stage2_prompt(
    template_text: str,
    packet_text: str,
    stage0_json: str,
    openalex_seed_json: str,
    mandatory_first_query: str,
) -> str:
    schema = """{
  "queries": ["query 1", "query 2"],
  "sources_consulted": ["openalex", "deepxiv"],
  "tools_attempted": ["deepxiv__search_papers"],
  "tool_attempt_count": 1,
  "tool_success_count": 1,
  "retrieval_attempted": true,
  "retrieval_successful": true,
  "failure_reason": null,
  "method_fragility_findings": ["finding 1"],
  "design_fallback_findings": ["finding 2"],
  "packet_relevant_takeaways": ["takeaway 1"],
  "evidence_items": [
    {
      "source": "openalex",
      "query": "query 1",
      "title": "paper title",
      "identifier": "https://openalex.org/W123",
      "relevance_note": "why it matters for the packet"
    }
  ]
}"""
    return render_template(
        template_text,
        {
            "PACKET_TEXT": packet_text,
            "STAGE0_JSON": stage0_json,
            "OPENALEX_SEED_JSON": openalex_seed_json,
            "MANDATORY_FIRST_QUERY": mandatory_first_query,
            "RETRIEVAL_OUTPUT_SCHEMA_HINT": schema,
        },
    )


def render_stage3_prompt(
    template_text: str,
    packet_text: str,
    stage0_json: str,
    stage2_json: str,
    openalex_seed_json: str,
) -> str:
    return render_template(
        template_text,
        {
            "PACKET_TEXT": packet_text,
            "STAGE0_JSON": stage0_json,
            "STAGE2_JSON": stage2_json,
            "OPENALEX_SEED_JSON": openalex_seed_json,
        },
    )


def render_stage4_prompt(
    template_text: str,
    packet_text: str,
    stage0_json: str,
    stage2_json: str,
    stage3_json: str,
    openalex_seed_json: str,
) -> str:
    return render_template(
        template_text,
        {
            "PACKET_TEXT": packet_text,
            "STAGE0_JSON": stage0_json,
            "STAGE2_JSON": stage2_json,
            "STAGE3_JSON": stage3_json,
            "OPENALEX_SEED_JSON": openalex_seed_json,
        },
    )


def render_stage3b_prompt(
    template_text: str,
    packet_text: str,
    stage0_json: str,
    stage2_json: str,
    stage3_json: str,
    stage4_critique: str,
    stage4_meta_json: str,
) -> str:
    return render_template(
        template_text,
        {
            "PACKET_TEXT": packet_text,
            "STAGE0_JSON": stage0_json,
            "STAGE2_JSON": stage2_json,
            "STAGE3_JSON": stage3_json,
            "STAGE4_CRITIQUE": stage4_critique,
            "STAGE4_META_JSON": stage4_meta_json,
        },
    )


def render_stage4b_prompt(
    template_text: str,
    packet_text: str,
    stage0_json: str,
    stage2_json: str,
    stage3_json: str,
    stage4_critique: str,
    stage3b_json: str,
) -> str:
    return render_template(
        template_text,
        {
            "PACKET_TEXT": packet_text,
            "STAGE0_JSON": stage0_json,
            "STAGE2_JSON": stage2_json,
            "STAGE3_JSON": stage3_json,
            "STAGE4_CRITIQUE": stage4_critique,
            "STAGE3B_JSON": stage3b_json,
        },
    )


def render_stage5_prompt(
    template_text: str,
    packet_text: str,
    stage0_json: str,
    stage2_json: str,
    stage3_json: str,
    stage4_critique: str,
    stage3b_json: str,
    stage4b_critique: str,
    openalex_seed_json: str,
) -> str:
    return render_template(
        template_text,
        {
            "PACKET_TEXT": packet_text,
            "STAGE0_JSON": stage0_json,
            "STAGE2_JSON": stage2_json,
            "STAGE3_JSON": stage3_json,
            "STAGE4_CRITIQUE": stage4_critique,
            "STAGE3B_JSON": stage3b_json,
            "STAGE4B_CRITIQUE": stage4b_critique,
            "OPENALEX_SEED_JSON": openalex_seed_json,
        },
    )


def validate_stage0_output(raw_text: str) -> dict[str, object]:
    cleaned = strip_optional_json_fence(raw_text)
    try:
        parsed = json.loads(cleaned)
    except json.JSONDecodeError as exc:
        raise ValueError(f"Stage 0 output is not valid JSON: {exc}") from exc
    required_keys = {
        "primary_estimand_hypotheses",
        "threat_checks",
        "search_priorities",
        "fallback_triggers",
        "final_decision_rule",
    }
    missing = sorted(required_keys - set(parsed))
    if missing:
        raise ValueError(f"Stage 0 output is missing required keys: {', '.join(missing)}")
    for key in (
        "primary_estimand_hypotheses",
        "threat_checks",
        "search_priorities",
        "fallback_triggers",
    ):
        value = parsed.get(key)
        if not isinstance(value, list) or not value:
            raise ValueError(f"Stage 0 field {key} must be a non-empty list of strings.")
        if any(not isinstance(item, str) or not item.strip() for item in value):
            raise ValueError(f"Stage 0 field {key} must contain only non-empty strings.")
    if not str(parsed.get("final_decision_rule", "")).strip():
        raise ValueError("Stage 0 output must contain a non-empty final_decision_rule.")
    return parsed


def validate_stage3b_output(raw_text: str) -> dict[str, object]:
    cleaned = strip_optional_json_fence(raw_text)
    try:
        parsed = json.loads(cleaned)
    except json.JSONDecodeError as exc:
        raise ValueError(f"Stage 3b output is not valid JSON: {exc}") from exc
    responses = parsed.get("responses")
    if not isinstance(responses, list) or not responses:
        raise ValueError("Stage 3b output must contain a non-empty responses list.")
    for response in responses:
        if not isinstance(response, dict):
            raise ValueError("Stage 3b responses must be JSON objects.")
        disposition = response.get("disposition")
        if disposition not in ALLOWED_DISPOSITIONS:
            raise ValueError(f"Stage 3b disposition must be one of {sorted(ALLOWED_DISPOSITIONS)}.")
        for key in ("focus_point", "packet_evidence", "revision"):
            if not str(response.get(key, "")).strip():
                raise ValueError(f"Stage 3b response must contain non-empty {key}.")
    if "updated_fallback_position" not in parsed:
        raise ValueError("Stage 3b output must include updated_fallback_position.")
    return parsed


def parse_stage4b_output(raw_text: str) -> tuple[str, dict[str, object]]:
    critique_md, meta = V2.parse_stage4_output(raw_text)
    required_keys = {
        "resolved_focus_points",
        "unresolved_focus_points",
        "final_recommendation",
        "continue_debate",
    }
    missing = sorted(required_keys - set(meta))
    if missing:
        raise ValueError(f"Stage 4b meta JSON is missing required keys: {', '.join(missing)}")
    if meta.get("continue_debate") is not False:
        raise ValueError("Stage 4b must set continue_debate=false for the smoke-only implementation.")
    return critique_md, meta


def initialize_pipeline_manifest(
    manifest_path: Path,
    case_id: str,
    variant_id: str,
    input_packet_sha256: str,
) -> None:
    data = {
        "case_id": case_id,
        "variant_id": variant_id,
        "agent_variant": "research_agent_v3_planner_debate",
        "input_packet_sha256": input_packet_sha256,
        "stages": {},
        "pipeline_failed": False,
        "planner_present": False,
        "debate_rounds_run": 0,
        "stop_rule_triggered_by": None,
        "created_at": V2.datetime.now().isoformat(),
    }
    write_text(manifest_path, json.dumps(data, indent=2, ensure_ascii=False) + "\n")


def update_manifest_fields(manifest_path: Path, **fields: object) -> None:
    manifest = json.loads(manifest_path.read_text())
    manifest.update(fields)
    write_text(manifest_path, json.dumps(manifest, indent=2, ensure_ascii=False) + "\n")


def main() -> None:
    args = parse_args()
    input_file = Path(args.input_file).resolve()
    packet_text = read_text(input_file)
    case_id, variant_id = parse_case_and_variant(input_file)

    if args.start_from == "stage0":
        run_dir = create_run_dir(Path(args.output_root), case_id, variant_id)
        write_text(run_dir / "input_packet.md", packet_text)
        initialize_pipeline_manifest(
            manifest_path=run_dir / "pipeline_manifest.json",
            case_id=case_id,
            variant_id=variant_id,
            input_packet_sha256=sha256_text(packet_text),
        )
        update_manifest_fields(
            run_dir / "pipeline_manifest.json",
            source_input_file=input_file.relative_to(ROOT).as_posix(),
        )
    else:
        if not args.run_dir:
            raise SystemExit("--run-dir is required when resuming from a later stage.")
        run_dir = Path(args.run_dir).resolve()
        if not run_dir.exists():
            raise SystemExit(f"Run directory not found: {run_dir}")

    manifest_path = run_dir / "pipeline_manifest.json"
    pipeline_failed = False

    try:
        stage0_template = read_text(PROMPTS_DIR / "stage0_planner.md")
        stage2_template = read_text(PROMPTS_DIR / "stage2_retrieval.md")
        stage3_template = read_text(PROMPTS_DIR / "stage3_candidates.md")
        stage4_template = read_text(PROMPTS_DIR / "stage4_critique.md")
        stage3b_template = read_text(PROMPTS_DIR / "stage3b_response.md")
        stage4b_template = read_text(PROMPTS_DIR / "stage4b_critique.md")
        stage5_template = read_text(PROMPTS_DIR / "stage5_final.md")
        openalex_seed = fetch_openalex_seed(packet_text)
        openalex_seed_json = json.dumps(openalex_seed, indent=2, ensure_ascii=False)
        mandatory_first_query = str(openalex_seed.get("query") or build_openalex_seed_query(packet_text))

        if args.start_from == "stage0":
            stage0_dir = run_dir / "stage0_planner"
            stage0_data, stage0_duration, stage0_retries, _ = run_stage_with_retry(
                "stage0_planner",
                stage0_dir,
                lambda: render_stage0_prompt(stage0_template, packet_text),
                validate_stage0_output,
                args.timeout_seconds,
                args.thinking_level,
            )
            stage0_artifact_path = save_stage3_artifact(stage0_dir, stage0_data)
            update_pipeline_manifest(
                manifest_path,
                "stage0_planner",
                stage_status(
                    "ok",
                    stage0_retries,
                    stage0_artifact_path.relative_to(run_dir).as_posix(),
                    stage0_duration,
                    "planner_json",
                    stderr_path=(stage0_dir / "stderr.log").relative_to(run_dir).as_posix(),
                ),
            )
            update_manifest_fields(manifest_path, planner_present=True)
        else:
            stage0_data = json.loads((run_dir / "stage0_planner" / "artifact.json").read_text())

        stage0_json = json.dumps(stage0_data, indent=2, ensure_ascii=False)

        if args.start_from in {"stage0", "stage2"}:
            stage2_dir = run_dir / "stage2_retrieval"
            openalex_seed_path = save_openalex_seed(stage2_dir, openalex_seed)
            stage2_data, stage2_duration, stage2_retries, stage2_tool_counts = run_stage_with_retry(
                "stage2_retrieval",
                stage2_dir,
                lambda: render_stage2_prompt(
                    stage2_template,
                    packet_text,
                    stage0_json,
                    openalex_seed_json,
                    mandatory_first_query,
                ),
                validate_stage2_output,
                args.timeout_seconds,
                args.thinking_level,
            )
            stage2_data = normalize_stage2_artifact(stage2_data, stage2_tool_counts)
            stage2_artifact_path, stage2_summary_path = save_stage2_artifacts(stage2_dir, stage2_data)
            stage2_status = stage_status(
                "ok" if stage2_tool_counts["tool_calls"] > 0 else "invalid",
                stage2_retries,
                stage2_artifact_path.relative_to(run_dir).as_posix(),
                stage2_duration,
                (
                    f"summary_path={stage2_summary_path.relative_to(run_dir).as_posix()}; "
                    f"openalex_seed_path={openalex_seed_path.relative_to(run_dir).as_posix()}"
                ),
                stderr_path=(stage2_dir / "stderr.log").relative_to(run_dir).as_posix(),
                retrieval_attempted=bool(stage2_data.get("retrieval_attempted")),
                retrieval_successful=bool(stage2_data.get("retrieval_successful")),
                retrieval_tool_calls=int(stage2_tool_counts["tool_calls"]),
                retrieval_failure_reason=stage2_data.get("failure_reason"),
            )
            update_pipeline_manifest(manifest_path, "stage2_retrieval", stage2_status)
            if stage2_tool_counts["tool_calls"] == 0:
                raise RuntimeError("Stage 2 is invalid: no actual retrieval tool call was recorded.")
        else:
            stage2_data = json.loads((run_dir / "stage2_retrieval" / "artifact.json").read_text())

        stage2_json = json.dumps(stage2_data, indent=2, ensure_ascii=False)

        if args.start_from in {"stage0", "stage2", "stage3"}:
            stage3_dir = run_dir / "stage3_candidates"
            stage3_data, stage3_duration, stage3_retries, _ = run_stage_with_retry(
                "stage3_candidates",
                stage3_dir,
                lambda: render_stage3_prompt(stage3_template, packet_text, stage0_json, stage2_json, openalex_seed_json),
                validate_stage3_output,
                args.timeout_seconds,
                args.thinking_level,
            )
            stage3_artifact_path = save_stage3_artifact(stage3_dir, stage3_data)
            update_pipeline_manifest(
                manifest_path,
                "stage3_candidates",
                stage_status(
                    "ok",
                    stage3_retries,
                    stage3_artifact_path.relative_to(run_dir).as_posix(),
                    stage3_duration,
                    f"n_candidates={len(stage3_data['candidates'])}",
                    stderr_path=(stage3_dir / "stderr.log").relative_to(run_dir).as_posix(),
                ),
            )
        else:
            stage3_data = json.loads((run_dir / "stage3_candidates" / "artifact.json").read_text())

        stage3_json = json.dumps(stage3_data, indent=2, ensure_ascii=False)

        if args.start_from in {"stage0", "stage2", "stage3", "stage4"}:
            stage4_dir = run_dir / "stage4_critique"
            (stage4_critique_md, stage4_meta), stage4_duration, stage4_retries, _ = run_stage_with_retry(
                "stage4_critique",
                stage4_dir,
                lambda: render_stage4_prompt(
                    stage4_template,
                    packet_text,
                    stage0_json,
                    stage2_json,
                    stage3_json,
                    openalex_seed_json,
                ),
                V2.parse_stage4_output,
                args.timeout_seconds,
                args.thinking_level,
            )
            stage4_path, stage4_meta_path = save_stage4_artifact(stage4_dir, stage4_critique_md, stage4_meta)
            update_pipeline_manifest(
                manifest_path,
                "stage4_critique",
                stage_status(
                    "ok",
                    stage4_retries,
                    stage4_path.relative_to(run_dir).as_posix(),
                    stage4_duration,
                    f"meta_path={stage4_meta_path.relative_to(run_dir).as_posix()}",
                    stderr_path=(stage4_dir / "stderr.log").relative_to(run_dir).as_posix(),
                ),
            )
        else:
            stage4_critique_md = (run_dir / "stage4_critique" / "artifact.md").read_text()
            stage4_meta = json.loads((run_dir / "stage4_critique" / "artifact.meta.json").read_text())

        stage4_meta_json = json.dumps(stage4_meta, indent=2, ensure_ascii=False)

        if args.start_from in {"stage0", "stage2", "stage3", "stage4", "stage3b"}:
            stage3b_dir = run_dir / "stage3b_response"
            stage3b_data, stage3b_duration, stage3b_retries, _ = run_stage_with_retry(
                "stage3b_response",
                stage3b_dir,
                lambda: render_stage3b_prompt(
                    stage3b_template,
                    packet_text,
                    stage0_json,
                    stage2_json,
                    stage3_json,
                    stage4_critique_md,
                    stage4_meta_json,
                ),
                validate_stage3b_output,
                args.timeout_seconds,
                args.thinking_level,
            )
            stage3b_artifact_path = save_stage3_artifact(stage3b_dir, stage3b_data)
            update_pipeline_manifest(
                manifest_path,
                "stage3b_response",
                stage_status(
                    "ok",
                    stage3b_retries,
                    stage3b_artifact_path.relative_to(run_dir).as_posix(),
                    stage3b_duration,
                    f"n_responses={len(stage3b_data['responses'])}",
                    stderr_path=(stage3b_dir / "stderr.log").relative_to(run_dir).as_posix(),
                ),
            )
            update_manifest_fields(manifest_path, debate_rounds_run=1)
        else:
            stage3b_data = json.loads((run_dir / "stage3b_response" / "artifact.json").read_text())

        stage3b_json = json.dumps(stage3b_data, indent=2, ensure_ascii=False)

        if args.start_from in {"stage0", "stage2", "stage3", "stage4", "stage3b", "stage4b"}:
            stage4b_dir = run_dir / "stage4b_critique"
            (stage4b_critique_md, stage4b_meta), stage4b_duration, stage4b_retries, _ = run_stage_with_retry(
                "stage4b_critique",
                stage4b_dir,
                lambda: render_stage4b_prompt(
                    stage4b_template,
                    packet_text,
                    stage0_json,
                    stage2_json,
                    stage3_json,
                    stage4_critique_md,
                    stage3b_json,
                ),
                parse_stage4b_output,
                args.timeout_seconds,
                args.thinking_level,
            )
            stage4b_path, stage4b_meta_path = save_stage4_artifact(stage4b_dir, stage4b_critique_md, stage4b_meta)
            update_pipeline_manifest(
                manifest_path,
                "stage4b_critique",
                stage_status(
                    "ok",
                    stage4b_retries,
                    stage4b_path.relative_to(run_dir).as_posix(),
                    stage4b_duration,
                    f"meta_path={stage4b_meta_path.relative_to(run_dir).as_posix()}",
                    stderr_path=(stage4b_dir / "stderr.log").relative_to(run_dir).as_posix(),
                ),
            )
            update_manifest_fields(
                manifest_path,
                debate_rounds_run=1,
                stop_rule_triggered_by="fixed_single_round_smoke_rule",
            )
        else:
            stage4b_critique_md = (run_dir / "stage4b_critique" / "artifact.md").read_text()
            stage4b_meta = json.loads((run_dir / "stage4b_critique" / "artifact.meta.json").read_text())

        stage5_dir = run_dir / "stage5_final"
        final_md, stage5_duration, stage5_retries, _ = run_stage_with_retry(
            "stage5_final",
            stage5_dir,
            lambda: render_stage5_prompt(
                stage5_template,
                packet_text,
                stage0_json,
                stage2_json,
                stage3_json,
                stage4_critique_md,
                stage3b_json,
                stage4b_critique_md,
                openalex_seed_json,
            ),
            lambda raw_text: raw_text if validate_stage5_output(raw_text) else raw_text,
            args.timeout_seconds,
            args.thinking_level,
        )
        stage5_artifact_path = save_stage5_artifact(stage5_dir, final_md)
        update_pipeline_manifest(
            manifest_path,
            "stage5_final",
            stage_status(
                "ok",
                stage5_retries,
                stage5_artifact_path.relative_to(run_dir).as_posix(),
                stage5_duration,
                (
                    "final_recommendation="
                    f"{stage4b_meta.get('final_recommendation')}; "
                    f"retrieval_successful={stage2_data.get('retrieval_successful')}"
                ),
                stderr_path=(stage5_dir / "stderr.log").relative_to(run_dir).as_posix(),
            ),
        )
    except Exception as exc:  # noqa: BLE001
        pipeline_failed = True
        update_pipeline_manifest(manifest_path, "pipeline_error", {"status": "failed", "message": str(exc)})
        raise
    finally:
        finalize_pipeline_manifest(manifest_path, pipeline_failed=pipeline_failed)


if __name__ == "__main__":
    try:
        main()
    except Exception as exc:  # noqa: BLE001
        print(str(exc), file=sys.stderr)
        raise SystemExit(1) from exc
