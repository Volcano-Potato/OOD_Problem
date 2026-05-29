#!/usr/bin/env python3

from __future__ import annotations

import csv
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
OUTPUT_CSV = ROOT / "results" / "perturbed_mechanical_reuse.csv"
OUTPUT_MD = ROOT / "results" / "perturbed_pair_audit.md"


ROWS = [
    {
        "case_id": "C001",
        "level2_run_id": "RUN_20260527_210840_01_openclaw_deepseekv4pro_isolated",
        "perturbed_run_id": "RUN_20260528_173940_01_openclaw_deepseekv4pro_isolated",
        "broken_condition": "pre-contact state is no longer researcher-assigned; households self-select into pre-contact availability",
        "level2_logic": "use variation in contact and avoidance frictions to separate social pressure from underlying willingness",
        "perturbed_behavior": "agent keeps mechanism-separation language and reuses contribution-pattern logic instead of fully downgrading the estimand",
        "mechanical_reuse": "yes",
        "audit_rationale": "The perturbed packet breaks clean assignment of pre-contact state, but the output continues to reason as if the base decomposition remains available.",
    },
    {
        "case_id": "C002",
        "level2_run_id": "RUN_20260527_215707_05_openclaw_deepseekv4pro_isolated",
        "perturbed_run_id": "RUN_20260527_222901_07_openclaw_deepseekv4pro_isolated",
        "broken_condition": "borrowers are no longer cleanly blind to later terms at take-up",
        "level2_logic": "separate adverse selection from repayment incentives using staged timing variation",
        "perturbed_behavior": "agent keeps the staged decomposition and still treats selection and incentive channels as separately identified",
        "mechanical_reuse": "yes",
        "audit_rationale": "The output does not fully re-scope the estimand after the key timing condition is weakened.",
    },
    {
        "case_id": "C004",
        "level2_run_id": "RUN_20260527_223907_09_openclaw_deepseekv4pro_isolated",
        "perturbed_run_id": "RUN_20260527_224310_10_openclaw_deepseekv4pro_isolated",
        "broken_condition": "ad-availability variation is manager-chosen rather than exogenous",
        "level2_logic": "use exogenous ad-availability variation to identify incremental downstream sales effects",
        "perturbed_behavior": "agent still proposes sensitivity analysis and weaker diagnostics, but retains causal language around ad-availability effects",
        "mechanical_reuse": "yes",
        "audit_rationale": "The output downgrades somewhat, but not enough to stop using the broken assignment as if it still carried causal identification.",
    },
    {
        "case_id": "C005",
        "level2_run_id": "RUN_20260527_224724_11_openclaw_deepseekv4pro_isolated",
        "perturbed_run_id": "RUN_20260527_225443_13_openclaw_deepseekv4pro_isolated",
        "broken_condition": "untreated opportunity-side logs are removed",
        "level2_logic": "compare exposed and unexposed units within the same opportunity set to identify exposed-user lift",
        "perturbed_behavior": "agent continues to claim exposed-user causal lift and LATE-style interpretation",
        "mechanical_reuse": "yes",
        "audit_rationale": "This is the clearest mechanical reuse case in the benchmark.",
    },
    {
        "case_id": "C008",
        "level2_run_id": "RUN_20260527_230420_15_openclaw_deepseekv4pro_isolated",
        "perturbed_run_id": "RUN_20260527_231251_17_openclaw_deepseekv4pro_isolated",
        "broken_condition": "untreated comparison stores/products are no longer available in the original clean form",
        "level2_logic": "use relative tax-visibility contrasts with untreated comparisons to isolate salience effects",
        "perturbed_behavior": "agent still frames the problem in the original salience-comparison design language",
        "mechanical_reuse": "yes",
        "audit_rationale": "The output preserves more of the base comparison logic than the perturbed packet supports.",
    },
    {
        "case_id": "C010",
        "level2_run_id": "RUN_20260527_231632_18_openclaw_deepseekv4pro_isolated",
        "perturbed_run_id": "RUN_20260527_232448_20_openclaw_deepseekv4pro_isolated",
        "broken_condition": "later offer is known in advance, weakening timing-based procrastination separation",
        "level2_logic": "use timing contrast between early small intervention and later known alternatives to diagnose present-bias/procrastination",
        "perturbed_behavior": "agent still leans on procrastination interpretation, although with some caveats",
        "mechanical_reuse": "yes",
        "audit_rationale": "The output softens the claim but still reuses the base mechanism story too directly.",
    },
    {
        "case_id": "C014",
        "level2_run_id": "RUN_20260527_232816_21_openclaw_deepseekv4pro_isolated",
        "perturbed_run_id": "RUN_20260527_233717_23_openclaw_deepseekv4pro_isolated",
        "broken_condition": "independent outcome measurement is removed; only official reports remain",
        "level2_logic": "compare treatment effects on independently measured corruption-related outcomes",
        "perturbed_behavior": "agent still interprets official-report changes as if they were clean corruption outcomes",
        "mechanical_reuse": "yes",
        "audit_rationale": "The output does not fully absorb the measurement breakdown.",
    },
    {
        "case_id": "C016",
        "level2_run_id": "RUN_20260527_234026_24_openclaw_deepseekv4pro_isolated",
        "perturbed_run_id": "RUN_20260527_235045_26_openclaw_deepseekv4pro_isolated",
        "broken_condition": "objective downstream outcome is removed, leaving selected self-reports",
        "level2_logic": "contrast targeted information with generic curriculum and interpret downstream effects using objective outcomes",
        "perturbed_behavior": "agent continues to interpret self-report differences as if they could directly support actual behavior change",
        "mechanical_reuse": "yes",
        "audit_rationale": "The output weakens some claims but still reuses the base behavioral interpretation too aggressively.",
    },
    {
        "case_id": "C019",
        "level2_run_id": "RUN_20260527_235916_28_openclaw_deepseekv4pro_isolated",
        "perturbed_run_id": "RUN_20260528_000656_30_openclaw_deepseekv4pro_isolated",
        "broken_condition": "clean pre-trip basket capture is removed",
        "level2_logic": "combine pre-trip intent measurement with route variation to isolate route-induced incremental spending",
        "perturbed_behavior": "agent pivots toward proxy-based and assumption-heavy design rather than simply reusing the full base estimand",
        "mechanical_reuse": "no",
        "audit_rationale": "The output still stretches some assumptions, but it does recognize the main design downgrade and proposes a weaker approach.",
    },
    {
        "case_id": "C020",
        "level2_run_id": "RUN_20260528_001055_31_openclaw_deepseekv4pro_isolated",
        "perturbed_run_id": "RUN_20260528_001721_33_openclaw_deepseekv4pro_isolated",
        "broken_condition": "price ending is bundled with markdown/sale framing",
        "level2_logic": "hold underlying price constant while varying terminal-digit format to separate formatting from bargaining cues",
        "perturbed_behavior": "agent still talks as if ending-format effects can be separated from sale-signal effects",
        "mechanical_reuse": "yes",
        "audit_rationale": "The output does not fully abandon the base mechanism separation after bundling is introduced.",
    },
]


def write_csv() -> None:
    OUTPUT_CSV.parent.mkdir(parents=True, exist_ok=True)
    fieldnames = list(ROWS[0].keys())
    with OUTPUT_CSV.open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames, lineterminator="\n")
        writer.writeheader()
        writer.writerows(ROWS)


def write_markdown() -> None:
    yes_count = sum(row["mechanical_reuse"] == "yes" for row in ROWS)
    total = len(ROWS)
    lines = [
        "# Perturbed Pair Audit",
        "",
        f"- Mechanical reuse headline: `{yes_count}/{total}` perturbed cases show mechanical reuse under broken identification.",
        "- Counting rule: `yes` means the key identifying condition is explicitly broken in the perturbed packet, but the agent still retains the base estimand, base identification logic, or only surface-level threat wording.",
        "",
        "| Case | Broken Condition | Mechanical Reuse | Rationale |",
        "|---|---|---|---|",
    ]
    for row in ROWS:
        lines.append(
            f"| `{row['case_id']}` | {row['broken_condition']} | `{row['mechanical_reuse']}` | {row['audit_rationale']} |"
        )
    OUTPUT_MD.write_text("\n".join(lines) + "\n")


def main() -> None:
    write_csv()
    write_markdown()


if __name__ == "__main__":
    main()
