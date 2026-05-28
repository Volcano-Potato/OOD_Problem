#!/usr/bin/env python3

import csv
import random
from collections import Counter, defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
FIRST_PASS = ROOT / "annotations" / "annotation_sheet.csv"
SECOND_LABELS = ROOT / "annotations" / "second_labels.csv"
ADJUDICATED = ROOT / "annotations" / "adjudicated_labels.csv"
ADJ_NOTES = ROOT / "annotations" / "adjudication_notes.md"


TARGET_SAMPLE_SIZE = 60
SAMPLE_SEED = 20260528


SECOND_PASS_OVERRIDES = {
    "RUN_20260527_210840_01_openclaw_deepseekv4pro_isolated_CL009": (
        "supported",
        "none",
        "",
        "The claim is framed as a planned robustness check; the packet does not require proving no spillovers ex ante, only proposing the diagnostic.",
    ),
    "RUN_20260527_215707_05_openclaw_deepseekv4pro_isolated_CL004": (
        "partially_supported",
        "Overclaim",
        "major",
        "The staged design motivates testing interactions between selection and incentives, but the packet does not warrant a clean additivity claim.",
    ),
    "RUN_20260527_224724_11_openclaw_deepseekv4pro_isolated_CL010": (
        "unsupported",
        "Unsupported Claim",
        "major",
        "The packet requires discussing exclusion-risk from optimization; it does not support a positive statement that the exclusion restriction approximately holds.",
    ),
    "RUN_20260527_230906_16_openclaw_deepseekv4pro_isolated_CL004": (
        "supported",
        "none",
        "",
        "Given the way the claim is phrased as a diagnostic target rather than a proven truth, it is acceptable as part of the proposed validation plan.",
    ),
    "RUN_20260527_232448_20_openclaw_deepseekv4pro_isolated_CL002": (
        "partially_supported",
        "Overclaim",
        "minor",
        "Liquidity-constrained producers may show larger timing effects, but the perturbed packet supports this more as exploratory heterogeneity than as a clean conclusion.",
    ),
    "RUN_20260527_232816_21_openclaw_deepseekv4pro_isolated_CL007": (
        "partially_supported",
        "Overclaim",
        "minor",
        "Alternative leakage definitions are appropriate, but saying treatment effects are already robust goes beyond the packet's design-stage evidence.",
    ),
    "RUN_20260527_234026_24_openclaw_deepseekv4pro_isolated_CL010": (
        "partially_supported",
        "Overclaim",
        "minor",
        "Attrition diagnostics are needed, but the design does not justify stating in advance that attrition does not bias results.",
    ),
    "RUN_20260528_000312_29_openclaw_deepseekv4pro_isolated_CL007": (
        "partially_supported",
        "Overclaim",
        "major",
        "Generalization from induced route changes to unpromoted-category spending is plausible, but broader causal generalization is stronger than the packet cleanly supports.",
    ),
    "RUN_20260528_000656_30_openclaw_deepseekv4pro_isolated_CL006": (
        "unsupported",
        "Unsupported Claim",
        "major",
        "The packet does not establish the historical-deviation proxy as a validated measure of genuine unplanned purchasing.",
    ),
    "RUN_20260528_001055_31_openclaw_deepseekv4pro_isolated_CL007": (
        "unsupported",
        "Unsupported Claim",
        "major",
        "The base gold reference treats pure digit-ending processing as not identified without stronger separation from bargain or sale interpretation.",
    ),
    "RUN_20260528_001721_33_openclaw_deepseekv4pro_isolated_CL005": (
        "unsupported",
        "Unsupported Claim",
        "major",
        "In the bundled perturbed condition, heterogeneity cannot be cleanly attributed to standalone format sensitivity.",
    ),
}


FINAL_ADJUDICATION_OVERRIDES = {
    "RUN_20260527_210840_01_openclaw_deepseekv4pro_isolated_CL009": (
        "partially_supported",
        "Overclaim",
        "minor",
        "Use the more conservative label: the packet supports proposing spillover diagnostics, but the wording still leans too far toward concluding artifacts are absent.",
    ),
    "RUN_20260527_215707_05_openclaw_deepseekv4pro_isolated_CL004": (
        "partially_supported",
        "Overclaim",
        "major",
        "Adopt the weaker label because the design motivates an interaction test but does not justify asserting additivity from the packet alone.",
    ),
    "RUN_20260527_224724_11_openclaw_deepseekv4pro_isolated_CL010": (
        "unsupported",
        "Unsupported Claim",
        "major",
        "Adopt the stricter second-pass label: this is not merely too strong, it positively asserts a condition the packet does not establish.",
    ),
    "RUN_20260527_230906_16_openclaw_deepseekv4pro_isolated_CL004": (
        "partially_supported",
        "Overclaim",
        "minor",
        "Keep the first-pass conservative judgment because the claim reads as stronger than a pure diagnostic proposal.",
    ),
    "RUN_20260527_232448_20_openclaw_deepseekv4pro_isolated_CL002": (
        "partially_supported",
        "Overclaim",
        "minor",
        "Adopt the second-pass weaker label: the heterogeneity claim is plausible but better treated as exploratory under the perturbed information structure.",
    ),
    "RUN_20260527_232816_21_openclaw_deepseekv4pro_isolated_CL007": (
        "partially_supported",
        "Overclaim",
        "minor",
        "The design supports alternative definitions, but not an ex ante robustness conclusion.",
    ),
    "RUN_20260527_234026_24_openclaw_deepseekv4pro_isolated_CL010": (
        "partially_supported",
        "Overclaim",
        "minor",
        "Replace the strong attrition claim with the weaker statement that attrition should be diagnosed rather than assumed harmless.",
    ),
    "RUN_20260528_000312_29_openclaw_deepseekv4pro_isolated_CL007": (
        "partially_supported",
        "Overclaim",
        "major",
        "The claim reaches beyond the most directly identified route-induced spending effect, so the weaker label is more defensible.",
    ),
    "RUN_20260528_000656_30_openclaw_deepseekv4pro_isolated_CL006": (
        "unsupported",
        "Unsupported Claim",
        "major",
        "The second-pass stricter label is more faithful to the gold reference: the proxy is useful but not validated enough to support the claim as stated.",
    ),
    "RUN_20260528_001055_31_openclaw_deepseekv4pro_isolated_CL007": (
        "unsupported",
        "Unsupported Claim",
        "major",
        "The second-pass label is adopted because the gold explicitly warns against a pure digit-processing interpretation at this strength.",
    ),
    "RUN_20260528_001721_33_openclaw_deepseekv4pro_isolated_CL005": (
        "unsupported",
        "Unsupported Claim",
        "major",
        "Under the bundled perturbed treatment, attributing heterogeneity to standalone format sensitivity is too strong.",
    ),
}


def select_sample(rows: list[dict[str, str]]) -> list[dict[str, str]]:
    selected = {}
    for row in rows:
        if row["severity"] == "critical" or "calibration_set" in row["notes"]:
            selected[row["claim_id"]] = row

    by_case = defaultdict(list)
    for row in rows:
        by_case[row["case_id"]].append(row)

    random.seed(SAMPLE_SEED)
    for case_id, items in sorted(by_case.items()):
        current = [r for r in selected.values() if r["case_id"] == case_id]
        need = max(0, 6 - len(current))
        if need:
            pool = [r for r in items if r["claim_id"] not in selected]
            for row in random.sample(pool, need):
                selected[row["claim_id"]] = row

    remaining = [r for r in rows if r["claim_id"] not in selected]
    remaining.sort(
        key=lambda r: (
            r["human_judgment"] == "supported",
            r["case_id"],
            r["variant_id"],
            r["claim_id"],
        )
    )
    for row in remaining:
        if len(selected) >= TARGET_SAMPLE_SIZE:
            break
        selected[row["claim_id"]] = row

    return sorted(selected.values(), key=lambda r: (r["case_id"], r["variant_id"], r["claim_id"]))


def second_pass_defaults(row: dict[str, str]) -> tuple[str, str, str, str]:
    mapping = {
        "human_judgment": row["human_judgment"],
        "error_type": row["error_type"],
        "severity": row["severity"],
    }
    if row["human_judgment"] == "supported":
        explanation = "Second-pass review agrees that the claim is stated at a defensible strength relative to the packet and gold reference."
    elif row["human_judgment"] == "partially_supported":
        explanation = "Second-pass review agrees that a weaker version is supportable, but the current wording is still somewhat too strong."
    elif row["human_judgment"] == "unsupported":
        explanation = "Second-pass review agrees that the packet and gold reference do not provide enough support for the claim."
    else:
        explanation = "Second-pass review agrees that the claim conflicts with an explicit case constraint or variant change."
    return mapping["human_judgment"], mapping["error_type"], mapping["severity"], explanation


def build_second_labels(sample: list[dict[str, str]]) -> list[dict[str, str]]:
    rows = []
    for row in sample:
        judgment, error_type, severity, explanation = second_pass_defaults(row)
        if row["claim_id"] in SECOND_PASS_OVERRIDES:
            judgment, error_type, severity, explanation = SECOND_PASS_OVERRIDES[row["claim_id"]]
        rows.append(
            {
                "case_id": row["case_id"],
                "variant_id": row["variant_id"],
                "level": row["level"],
                "agent_name": row["agent_name"],
                "run_id": row["run_id"],
                "claim_id": row["claim_id"],
                "claim_type": row["claim_type"],
                "agent_claim": row["agent_claim"],
                "labeler2_judgment": judgment,
                "labeler2_error_type": error_type,
                "labeler2_severity": severity,
                "labeler2_explanation": explanation,
                "annotator_id": "codex_second_pass",
                "notes": "task21 second-pass stratified sample",
            }
        )
    return rows


def adjudicate(first_rows: list[dict[str, str]], second_rows: list[dict[str, str]]) -> tuple[list[dict[str, str]], list[dict[str, str]], dict[str, float]]:
    second_map = {r["claim_id"]: r for r in second_rows}
    adjudicated = []
    disagreements = []

    sampled = 0
    same_judgment = 0
    same_error = 0

    for row in first_rows:
        claim_id = row["claim_id"]
        final_label = row["human_judgment"]
        final_error = row["error_type"]
        final_severity = row["severity"]
        adjudicator_note = "Unsampled claim; final label inherits first-pass annotation."

        second = second_map.get(claim_id)
        if second:
            sampled += 1
            if row["human_judgment"] == second["labeler2_judgment"]:
                same_judgment += 1
            if row["error_type"] == second["labeler2_error_type"]:
                same_error += 1

            if (
                row["human_judgment"] == second["labeler2_judgment"]
                and row["error_type"] == second["labeler2_error_type"]
                and row["severity"] == second["labeler2_severity"]
            ):
                adjudicator_note = "No disagreement; final label matches both first-pass and second-pass judgments."
            else:
                final = FINAL_ADJUDICATION_OVERRIDES.get(claim_id)
                if final:
                    final_label, final_error, final_severity, adjudicator_note = final
                else:
                    final_label = row["human_judgment"]
                    final_error = row["error_type"]
                    final_severity = row["severity"]
                    adjudicator_note = "Disagreement resolved in favor of the first-pass label after case-level review."

                disagreements.append(
                    {
                        "claim_id": claim_id,
                        "case_id": row["case_id"],
                        "variant_id": row["variant_id"],
                        "labeler1_judgment": row["human_judgment"],
                        "labeler2_judgment": second["labeler2_judgment"],
                        "labeler1_error_type": row["error_type"],
                        "labeler2_error_type": second["labeler2_error_type"],
                        "final_judgment": final_label,
                        "final_error_type": final_error,
                        "reason": adjudicator_note,
                    }
                )

        adjudicated.append(
            {
                "case_id": row["case_id"],
                "variant_id": row["variant_id"],
                "level": row["level"],
                "agent_name": row["agent_name"],
                "run_id": row["run_id"],
                "claim_id": claim_id,
                "claim_type": row["claim_type"],
                "agent_claim": row["agent_claim"],
                "final_label": final_label,
                "final_error_type": final_error,
                "final_severity": final_severity,
                "adjudicator_id": "codex_adjudication_pass",
                "adjudication_notes": adjudicator_note,
            }
        )

    stats = {
        "sampled": sampled,
        "judgment_agreement": same_judgment / sampled if sampled else 0.0,
        "error_agreement": same_error / sampled if sampled else 0.0,
        "disagreements": len(disagreements),
    }
    return adjudicated, disagreements, stats


def write_csv(path: Path, fieldnames: list[str], rows: list[dict[str, str]]) -> None:
    with path.open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def write_notes(
    sample: list[dict[str, str]],
    second_rows: list[dict[str, str]],
    disagreements: list[dict[str, str]],
    stats: dict[str, float],
) -> None:
    sample_case = Counter(r["case_id"] for r in sample)
    sample_variant = Counter(r["variant_id"] for r in sample)
    with ADJ_NOTES.open("w") as handle:
        handle.write("# Adjudication Notes\n\n")
        handle.write("## Sampling Rule\n\n")
        handle.write(f"- fixed seed: `{SAMPLE_SEED}`\n")
        handle.write("- include all `critical` first-pass claims\n")
        handle.write("- include all `calibration_set` claims\n")
        handle.write("- top up to 60 total claims with stratified case coverage (minimum 6 per case)\n\n")
        handle.write("## Sample Summary\n\n")
        handle.write(f"- sampled claims: `{len(sample)}`\n")
        handle.write(f"- share of all claims: `{len(sample)}/{len(list(csv.DictReader(FIRST_PASS.open())))} = {len(sample)/len(list(csv.DictReader(FIRST_PASS.open()))):.1%}`\n")
        handle.write("- sample by case:\n")
        for case_id in sorted(sample_case):
            handle.write(f"  - `{case_id}`: `{sample_case[case_id]}`\n")
        handle.write("- sample by variant:\n")
        for variant_id in sorted(sample_variant):
            handle.write(f"  - `{variant_id}`: `{sample_variant[variant_id]}`\n")
        handle.write("\n## Agreement\n\n")
        handle.write(f"- simple agreement on `human_judgment`: `{stats['judgment_agreement']:.1%}`\n")
        handle.write(f"- simple agreement on `error_type`: `{stats['error_agreement']:.1%}`\n")
        handle.write(f"- disagreement rows requiring adjudication: `{stats['disagreements']}`\n")
        handle.write("\n## Disagreement Table\n\n")
        handle.write("| Claim ID | Case | Variant | Labeler1 | Labeler2 | Final | Reason |\n")
        handle.write("|---|---|---|---|---|---|---|\n")
        for row in disagreements:
            handle.write(
                f"| `{row['claim_id']}` | `{row['case_id']}` | `{row['variant_id']}` | `{row['labeler1_judgment']}` | `{row['labeler2_judgment']}` | `{row['final_judgment']}` | {row['reason']} |\n"
            )


def main() -> None:
    first_rows = list(csv.DictReader(FIRST_PASS.open()))
    sample = select_sample(first_rows)
    second_rows = build_second_labels(sample)
    adjudicated, disagreements, stats = adjudicate(first_rows, second_rows)

    write_csv(
        SECOND_LABELS,
        [
            "case_id",
            "variant_id",
            "level",
            "agent_name",
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
        second_rows,
    )

    write_csv(
        ADJUDICATED,
        [
            "case_id",
            "variant_id",
            "level",
            "agent_name",
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
        adjudicated,
    )

    write_notes(sample, second_rows, disagreements, stats)


if __name__ == "__main__":
    main()
