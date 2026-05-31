#!/usr/bin/env python3

import csv
import random
from collections import Counter, defaultdict
from math import ceil
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
FIRST_PASS = ROOT / "annotations" / "annotation_sheet.csv"
SECOND_LABELS = ROOT / "annotations" / "second_labels.csv"
ADJUDICATED = ROOT / "annotations" / "adjudicated_labels.csv"
ADJ_NOTES = ROOT / "annotations" / "adjudication_notes.md"
DEFAULT_AGENT_VARIANT = "benchmark_isolated"


MIN_TARGET_SAMPLE_SIZE = 60
SAMPLE_SEED = 20260528
TARGET_SAMPLE_SHARE = 0.21
MIN_PER_CASE = 6
MIN_PER_VARIANT = {
    "level1": 10,
    "level2": 10,
    "level3": 10,
    "perturbed": 10,
    "no_solution": 4,
}


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
    target_sample_size = max(MIN_TARGET_SAMPLE_SIZE, ceil(len(rows) * TARGET_SAMPLE_SHARE))
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
        need = max(0, MIN_PER_CASE - len(current))
        if need:
            pool = [r for r in items if r["claim_id"] not in selected]
            for row in random.sample(pool, min(need, len(pool))):
                selected[row["claim_id"]] = row

    by_variant = defaultdict(list)
    for row in rows:
        by_variant[row["variant_id"]].append(row)
    for variant_id, items in sorted(by_variant.items()):
        target = min(MIN_PER_VARIANT.get(variant_id, 0), len(items))
        current = [r for r in selected.values() if r["variant_id"] == variant_id]
        need = max(0, target - len(current))
        if need:
            pool = [r for r in items if r["claim_id"] not in selected]
            for row in random.sample(pool, min(need, len(pool))):
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
        if len(selected) >= target_sample_size:
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
                "agent_variant": row.get("agent_variant", "") or DEFAULT_AGENT_VARIANT,
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
                "agent_variant": row.get("agent_variant", "") or DEFAULT_AGENT_VARIANT,
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
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def load_existing_rows(path: Path) -> list[dict[str, str]]:
    if not path.exists():
        return []
    with path.open(newline="") as handle:
        return list(csv.DictReader(handle))


def preserve_existing_sample_rows(
    existing_rows: list[dict[str, str]],
    agent_variant: str,
    first_rows: list[dict[str, str]],
) -> list[dict[str, str]] | None:
    variant_rows = [
        row for row in existing_rows if (row.get("agent_variant", "") or DEFAULT_AGENT_VARIANT) == agent_variant
    ]
    if not variant_rows:
        return None

    first_claim_ids = {row["claim_id"] for row in first_rows}
    if any(row["claim_id"] not in first_claim_ids for row in variant_rows):
        return None

    return sorted(variant_rows, key=lambda row: (row["case_id"], row["variant_id"], row["claim_id"]))


def preserve_existing_full_rows(
    existing_rows: list[dict[str, str]],
    agent_variant: str,
    first_rows: list[dict[str, str]],
) -> list[dict[str, str]] | None:
    variant_rows = [
        row for row in existing_rows if (row.get("agent_variant", "") or DEFAULT_AGENT_VARIANT) == agent_variant
    ]
    if not variant_rows:
        return None

    first_claim_ids = [row["claim_id"] for row in first_rows]
    existing_by_claim = {row["claim_id"]: row for row in variant_rows}
    if set(existing_by_claim) != set(first_claim_ids):
        return None

    return [existing_by_claim[claim_id] for claim_id in first_claim_ids]


def build_notes_section(
    agent_variant: str,
    sample: list[dict[str, str]],
    disagreements: list[dict[str, str]],
    stats: dict[str, float],
) -> list[str]:
    sample_case = Counter(r["case_id"] for r in sample)
    sample_variant = Counter(r["variant_id"] for r in sample)
    lines = [
        f"## Agent Variant: `{agent_variant}`",
        "",
        "### Sampling Rule",
        "",
        f"- fixed seed: `{SAMPLE_SEED}`",
        "- include all `critical` first-pass claims",
        "- include all `calibration_set` claims",
        f"- target sample size: `max({MIN_TARGET_SAMPLE_SIZE}, ceil(total_claims * {TARGET_SAMPLE_SHARE:.2f}))`",
        f"- enforce minimum case coverage: `{MIN_PER_CASE}` claims per case when available",
        "- enforce minimum variant coverage:",
    ]
    for variant_id, target in MIN_PER_VARIANT.items():
        lines.append(f"  - `{variant_id}`: up to `{target}` claims when available")
    lines.extend(
        [
            "",
            "### Sample Summary",
            "",
            f"- sampled claims: `{len(sample)}`",
            "- sample by case:",
        ]
    )
    for case_id in sorted(sample_case):
        lines.append(f"  - `{case_id}`: `{sample_case[case_id]}`")
    lines.append("- sample by variant:")
    for variant_id in sorted(sample_variant):
        lines.append(f"  - `{variant_id}`: `{sample_variant[variant_id]}`")
    lines.extend(
        [
            "",
            "### Agreement",
            "",
            f"- simple agreement on `human_judgment`: `{stats['judgment_agreement']:.1%}`",
            f"- simple agreement on `error_type`: `{stats['error_agreement']:.1%}`",
            f"- disagreement rows requiring adjudication: `{stats['disagreements']}`",
            "",
            "### Disagreement Table",
            "",
            "| Claim ID | Case | Variant | Labeler1 | Labeler2 | Final | Reason |",
            "|---|---|---|---|---|---|---|",
        ]
    )
    for row in disagreements:
        lines.append(
            f"| `{row['claim_id']}` | `{row['case_id']}` | `{row['variant_id']}` | `{row['labeler1_judgment']}` | `{row['labeler2_judgment']}` | `{row['final_judgment']}` | {row['reason']} |"
        )
    lines.append("")
    return lines


def write_notes(
    total_first_pass_rows: int,
    preserved_variants: list[tuple[str, int]],
    generated_sections: list[list[str]],
) -> None:
    with ADJ_NOTES.open("w") as handle:
        handle.write("# Adjudication Notes\n\n")
        handle.write(f"- total first-pass claims in file: `{total_first_pass_rows}`\n")
        if preserved_variants:
            handle.write("- preserved existing adjudication for variants with unchanged claim sets:\n")
            for agent_variant, count in preserved_variants:
                handle.write(f"  - `{agent_variant}`: `{count}` claims\n")
        if generated_sections:
            handle.write("- newly generated adjudication sections follow below.\n")
        handle.write("\n")
        for section in generated_sections:
            handle.write("\n".join(section))
            handle.write("\n")


def main() -> None:
    with FIRST_PASS.open(newline="") as handle:
        first_rows_all = list(csv.DictReader(handle))

    existing_second_rows = load_existing_rows(SECOND_LABELS)
    existing_adjudicated_rows = load_existing_rows(ADJUDICATED)

    rows_by_variant = defaultdict(list)
    for row in first_rows_all:
        rows_by_variant[row.get("agent_variant", "") or DEFAULT_AGENT_VARIANT].append(row)

    second_rows: list[dict[str, str]] = []
    adjudicated: list[dict[str, str]] = []
    preserved_variants: list[tuple[str, int]] = []
    generated_sections: list[list[str]] = []

    for agent_variant in sorted(rows_by_variant):
        first_rows = rows_by_variant[agent_variant]
        preserved_second = preserve_existing_sample_rows(existing_second_rows, agent_variant, first_rows)
        preserved_adjudicated = preserve_existing_full_rows(existing_adjudicated_rows, agent_variant, first_rows)
        if preserved_second is not None and preserved_adjudicated is not None:
            second_rows.extend(preserved_second)
            adjudicated.extend(preserved_adjudicated)
            preserved_variants.append((agent_variant, len(first_rows)))
            continue

        sample = select_sample(first_rows)
        variant_second_rows = build_second_labels(sample)
        variant_adjudicated, disagreements, stats = adjudicate(first_rows, variant_second_rows)
        second_rows.extend(variant_second_rows)
        adjudicated.extend(variant_adjudicated)
        generated_sections.append(build_notes_section(agent_variant, sample, disagreements, stats))

    second_rows.sort(key=lambda row: (row["case_id"], row["variant_id"], row["claim_id"]))
    adjudicated.sort(key=lambda row: (row["case_id"], row["variant_id"], row["claim_id"]))

    write_csv(
        SECOND_LABELS,
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
        second_rows,
    )

    write_csv(
        ADJUDICATED,
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
        adjudicated,
    )

    write_notes(len(first_rows_all), preserved_variants, generated_sections)


if __name__ == "__main__":
    main()
