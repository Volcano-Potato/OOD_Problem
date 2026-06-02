#!/usr/bin/env python3

from __future__ import annotations

import csv
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
OUTPUT_CSV = ROOT / "results" / "perturbed_mechanical_reuse.csv"
OUTPUT_MD = ROOT / "results" / "perturbed_pair_audit.md"
OUTPUT_V1_CSV = ROOT / "results" / "perturbed_mechanical_reuse_v1.csv"
OUTPUT_V1_MD = ROOT / "results" / "perturbed_pair_audit_v1.md"
OUTPUT_V2_CSV = ROOT / "results" / "perturbed_mechanical_reuse_v2.csv"
OUTPUT_V2_MD = ROOT / "results" / "perturbed_pair_audit_v2.md"


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

ROWS_V1 = [
    {
        "case_id": "C001",
        "level2_run_id": "RUN_20260527_210840_01_openclaw_deepseekv4pro_isolated",
        "perturbed_run_id": "RUN_20260531_163414_01_openclaw_deepseekv4pro_researchagentv1",
        "broken_condition": "pre-contact state is no longer researcher-assigned; households self-select into pre-contact availability",
        "level2_logic": "use variation in contact and avoidance frictions to separate social pressure from underlying willingness",
        "perturbed_behavior": "agent abandons point identification and replaces the base decomposition with descriptive four-way stratification plus a bounded revealed-preference exercise",
        "mechanical_reuse": "no",
        "audit_rationale": "The final memo explicitly says the perturbation is fatal to the base causal design and downgrades claims to descriptive or bound-based statements rather than preserving the original decomposition.",
    },
    {
        "case_id": "C002",
        "level2_run_id": "RUN_20260527_215707_05_openclaw_deepseekv4pro_isolated",
        "perturbed_run_id": "RUN_20260531_164250_02_openclaw_deepseekv4pro_researchagentv1",
        "broken_condition": "borrowers are no longer cleanly blind to later terms at take-up",
        "level2_logic": "separate adverse selection from repayment incentives using staged timing variation",
        "perturbed_behavior": "agent rejects clean channel separation and keeps only a narrower within-borrower realized-terms design under strong added assumptions",
        "mechanical_reuse": "no",
        "audit_rationale": "The output no longer claims that selection and incentive effects remain separately identified; the surviving fixed-effects design targets a different, weaker incentive-margin estimand.",
    },
    {
        "case_id": "C004",
        "level2_run_id": "RUN_20260527_223907_09_openclaw_deepseekv4pro_isolated",
        "perturbed_run_id": "RUN_20260531_165312_03_openclaw_deepseekv4pro_researchagentv1",
        "broken_condition": "ad-availability variation is manager-chosen rather than exogenous",
        "level2_logic": "use exogenous ad-availability variation to identify incremental downstream sales effects",
        "perturbed_behavior": "agent discards all causal candidates and recommends descriptive correlational benchmarking only",
        "mechanical_reuse": "no",
        "audit_rationale": "The memo fully abandons the broken exogeneity logic instead of trying to salvage causal ad-availability effects with surface-level threat language.",
    },
    {
        "case_id": "C005",
        "level2_run_id": "RUN_20260527_224724_11_openclaw_deepseekv4pro_isolated",
        "perturbed_run_id": "RUN_20260531_170002_04_openclaw_deepseekv4pro_researchagentv1",
        "broken_condition": "untreated opportunity-side logs are removed",
        "level2_logic": "compare exposed and unexposed units within the same opportunity set to identify exposed-user lift",
        "perturbed_behavior": "agent centers the ITT but still retains an IV/LATE estimate of actual exposure as a supplementary causal quantity",
        "mechanical_reuse": "yes",
        "audit_rationale": "The final memo does downgrade the headline estimand, but it still preserves a causal actual-exposure LATE despite the packet removing the clean opportunity-side support that made the base exposed-user logic credible.",
    },
    {
        "case_id": "C008",
        "level2_run_id": "RUN_20260527_230420_15_openclaw_deepseekv4pro_isolated",
        "perturbed_run_id": "RUN_20260531_170747_05_openclaw_deepseekv4pro_researchagentv1",
        "broken_condition": "untreated comparison stores/products are no longer available in the original clean form",
        "level2_logic": "use relative tax-visibility contrasts with untreated comparisons to isolate salience effects",
        "perturbed_behavior": "agent recommends descriptive pre-post analysis, but still keeps a within-store DiD and salience-gradient story as a secondary causal attempt",
        "mechanical_reuse": "yes",
        "audit_rationale": "The clean untreated comparison is gone, yet the memo still leans on treated-versus-untreated within-store comparisons and salience-pattern interpretation rather than fully dropping the base comparison design.",
    },
    {
        "case_id": "C010",
        "level2_run_id": "RUN_20260527_231632_18_openclaw_deepseekv4pro_isolated",
        "perturbed_run_id": "RUN_20260531_171514_06_openclaw_deepseekv4pro_researchagentv1",
        "broken_condition": "later offer is known in advance, weakening timing-based procrastination separation",
        "level2_logic": "use timing contrast between early small intervention and later known alternatives to diagnose present-bias/procrastination",
        "perturbed_behavior": "agent narrows the estimand to the ITT of the announced schedule bundle and explicitly rejects procrastination identification",
        "mechanical_reuse": "no",
        "audit_rationale": "The output stops short of reusing the base procrastination story and clearly states that timing and anticipation are now fused.",
    },
    {
        "case_id": "C014",
        "level2_run_id": "RUN_20260527_232816_21_openclaw_deepseekv4pro_isolated",
        "perturbed_run_id": "RUN_20260531_172257_07_openclaw_deepseekv4pro_researchagentv1",
        "broken_condition": "independent outcome measurement is removed; only official reports remain",
        "level2_logic": "compare treatment effects on independently measured corruption-related outcomes",
        "perturbed_behavior": "agent narrows the remaining causal claim to reporting-side ITT and explicitly refuses corruption claims",
        "mechanical_reuse": "no",
        "audit_rationale": "The memo treats administrative reports as the only credible outcome target left and does not keep the base corruption-reduction interpretation.",
    },
    {
        "case_id": "C016",
        "level2_run_id": "RUN_20260527_234026_24_openclaw_deepseekv4pro_isolated",
        "perturbed_run_id": "RUN_20260531_173157_08_openclaw_deepseekv4pro_researchagentv1",
        "broken_condition": "objective downstream outcome is removed, leaving selected self-reports",
        "level2_logic": "contrast targeted information with generic curriculum and interpret downstream effects using objective outcomes",
        "perturbed_behavior": "agent abandons point identification and replaces the base interpretation with bounds and descriptive self-report analysis",
        "mechanical_reuse": "no",
        "audit_rationale": "The final memo absorbs the measurement breakdown and no longer treats self-reports as if they identified actual behavioral change.",
    },
    {
        "case_id": "C019",
        "level2_run_id": "RUN_20260527_235916_28_openclaw_deepseekv4pro_isolated",
        "perturbed_run_id": "RUN_20260531_174004_09_openclaw_deepseekv4pro_researchagentv1",
        "broken_condition": "clean pre-trip basket capture is removed",
        "level2_logic": "combine pre-trip intent measurement with route variation to isolate route-induced incremental spending",
        "perturbed_behavior": "agent abandons causal route-length designs and keeps only descriptive correlation decomposition",
        "mechanical_reuse": "no",
        "audit_rationale": "The memo fully downgrades to non-causal route-spending associations and does not preserve the base incremental-spending identification logic.",
    },
    {
        "case_id": "C020",
        "level2_run_id": "RUN_20260528_001055_31_openclaw_deepseekv4pro_isolated",
        "perturbed_run_id": "RUN_20260531_174815_10_openclaw_deepseekv4pro_researchagentv1",
        "broken_condition": "price ending is bundled with markdown/sale framing",
        "level2_logic": "hold underlying price constant while varying terminal-digit format to separate formatting from bargaining cues",
        "perturbed_behavior": "agent abandons the standalone format-effect target and reframes the task around descriptive bundle analysis plus an alternative bundle estimand",
        "mechanical_reuse": "no",
        "audit_rationale": "The output no longer claims that ending-format effects can be separated from promotion effects; the remaining bundle discussion changes the estimand rather than reusing the base mechanism separation.",
    },
]

ROWS_V2 = [
    {
        "case_id": "C001",
        "level2_run_id": "RUN_20260527_210840_01_openclaw_deepseekv4pro_isolated",
        "perturbed_run_id": "RUN_20260601_141101_01_openclaw_deepseekv4pro_researchagentv2search",
        "broken_condition": "pre-contact state is no longer researcher-assigned; households self-select into pre-contact availability",
        "level2_logic": "use variation in contact and avoidance frictions to separate social pressure from underlying willingness",
        "perturbed_behavior": "agent rejects the base decomposition and replaces it with descriptive self-selection contrasts plus partial-identification bounds and sensitivity analysis",
        "mechanical_reuse": "no",
        "audit_rationale": "The final memo no longer preserves a point-identified pressure-versus-altruism estimand and explicitly treats the perturbation as fatal to the base causal design.",
    },
    {
        "case_id": "C002",
        "level2_run_id": "RUN_20260527_215707_05_openclaw_deepseekv4pro_isolated",
        "perturbed_run_id": "RUN_20260601_142014_02_openclaw_deepseekv4pro_researchagentv2search",
        "broken_condition": "borrowers are no longer cleanly blind to later terms at take-up",
        "level2_logic": "separate adverse selection from repayment incentives using staged timing variation",
        "perturbed_behavior": "agent abandons the channel-separation target and reframes the design around the reduced-form ITT of the initial offer rate on repayment",
        "mechanical_reuse": "no",
        "audit_rationale": "The final memo explicitly states that the Karlan-Zinman style decomposition is not identified once later terms are anticipated, so the base selection-versus-incentive logic is not retained.",
    },
    {
        "case_id": "C004",
        "level2_run_id": "RUN_20260527_223907_09_openclaw_deepseekv4pro_isolated",
        "perturbed_run_id": "RUN_20260601_143245_03_openclaw_deepseekv4pro_researchagentv2search",
        "broken_condition": "ad-availability variation is manager-chosen rather than exogenous",
        "level2_logic": "use exogenous ad-availability variation to identify incremental downstream sales effects",
        "perturbed_behavior": "agent rejects all causal candidates and keeps only descriptive partial-correlation analysis under explicit non-causal caveats",
        "mechanical_reuse": "no",
        "audit_rationale": "The memo fully abandons the exogenous-assignment logic rather than trying to salvage causal ad-availability effects with a weakened observational design.",
    },
    {
        "case_id": "C005",
        "level2_run_id": "RUN_20260527_224724_11_openclaw_deepseekv4pro_isolated",
        "perturbed_run_id": "RUN_20260601_145350_04_openclaw_deepseekv4pro_researchagentv2search",
        "broken_condition": "untreated opportunity-side logs are removed",
        "level2_logic": "compare exposed and unexposed units within the same opportunity set to identify exposed-user lift",
        "perturbed_behavior": "agent rejects exposure-level lift, rejects Wald-IV/LATE, keeps only campaign-assignment ITT plus predictive PIE as a non-causal budget-allocation supplement",
        "mechanical_reuse": "no",
        "audit_rationale": "Unlike v1, the final memo no longer preserves a secondary causal actual-exposure estimand; the base exposed-user logic is explicitly treated as not identified under the perturbation.",
    },
    {
        "case_id": "C008",
        "level2_run_id": "RUN_20260527_230420_15_openclaw_deepseekv4pro_isolated",
        "perturbed_run_id": "RUN_20260601_150718_05_openclaw_deepseekv4pro_researchagentv2search",
        "broken_condition": "untreated comparison stores/products are no longer available in the original clean form",
        "level2_logic": "use relative tax-visibility contrasts with untreated comparisons to isolate salience effects",
        "perturbed_behavior": "agent abandons within-store treated-vs-untreated causal comparisons and keeps only descriptive demand-reallocation analysis",
        "mechanical_reuse": "no",
        "audit_rationale": "Unlike v1, the memo does not retain a secondary within-store DiD or salience-gradient causal story after the untreated comparison structure is removed.",
    },
    {
        "case_id": "C010",
        "level2_run_id": "RUN_20260527_231632_18_openclaw_deepseekv4pro_isolated",
        "perturbed_run_id": "RUN_20260601_152208_06_openclaw_deepseekv4pro_researchagentv2search",
        "broken_condition": "later offer is known in advance, weakening timing-based procrastination separation",
        "level2_logic": "use timing contrast between early small intervention and later known alternatives to diagnose present-bias/procrastination",
        "perturbed_behavior": "agent narrows the target to the menu-announcement bundle ITT and explicitly rejects procrastination identification",
        "mechanical_reuse": "no",
        "audit_rationale": "The memo no longer treats the timing contrast as identifying procrastination once the later offer is anticipated.",
    },
    {
        "case_id": "C014",
        "level2_run_id": "RUN_20260527_232816_21_openclaw_deepseekv4pro_isolated",
        "perturbed_run_id": "RUN_20260601_153503_07_openclaw_deepseekv4pro_researchagentv2search",
        "broken_condition": "independent outcome measurement is removed; only official reports remain",
        "level2_logic": "compare treatment effects on independently measured corruption-related outcomes",
        "perturbed_behavior": "agent narrows the estimand to reporting-side ITT on officially reported outcomes and explicitly refuses corruption-reduction claims",
        "mechanical_reuse": "no",
        "audit_rationale": "The memo fully absorbs the measurement breakdown and no longer interprets official records as clean corruption outcomes.",
    },
    {
        "case_id": "C016",
        "level2_run_id": "RUN_20260527_234026_24_openclaw_deepseekv4pro_isolated",
        "perturbed_run_id": "RUN_20260601_154952_08_openclaw_deepseekv4pro_researchagentv2search",
        "broken_condition": "objective downstream outcome is removed, leaving selected self-reports",
        "level2_logic": "contrast targeted information with generic curriculum and interpret downstream effects using objective outcomes",
        "perturbed_behavior": "agent narrows to self-reported ITT plus sensitivity bounds and explicitly states that actual behavior change is not identified",
        "mechanical_reuse": "no",
        "audit_rationale": "The final memo treats self-reports as a distinct reporting outcome rather than reusing the base interpretation of actual behavioral change.",
    },
    {
        "case_id": "C019",
        "level2_run_id": "RUN_20260527_235916_28_openclaw_deepseekv4pro_isolated",
        "perturbed_run_id": "RUN_20260601_160120_09_openclaw_deepseekv4pro_researchagentv2search",
        "broken_condition": "clean pre-trip basket capture is removed",
        "level2_logic": "combine pre-trip intent measurement with route variation to isolate route-induced incremental spending",
        "perturbed_behavior": "agent downgrades to descriptive route-spending association and partial-identification diagnostics without claiming a causal route effect",
        "mechanical_reuse": "no",
        "audit_rationale": "The memo preserves the same broad downgrade discipline as v1 and does not attempt to keep the base incremental-spending identification logic.",
    },
    {
        "case_id": "C020",
        "level2_run_id": "RUN_20260528_001055_31_openclaw_deepseekv4pro_isolated",
        "perturbed_run_id": "RUN_20260601_161412_10_openclaw_deepseekv4pro_researchagentv2search",
        "broken_condition": "price ending is bundled with markdown/sale framing",
        "level2_logic": "hold underlying price constant while varying terminal-digit format to separate formatting from bargaining cues",
        "perturbed_behavior": "agent rejects the standalone terminal-digit estimand and reframes the design around the compound bundle effect only",
        "mechanical_reuse": "no",
        "audit_rationale": "The final memo does not preserve the base mechanism-separation claim after price endings and promotion framing become perfectly bundled.",
    },
]


def write_csv(path: Path, rows: list[dict[str, str]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    fieldnames = list(rows[0].keys())
    with path.open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def write_markdown(path: Path, rows: list[dict[str, str]], title: str) -> None:
    yes_count = sum(row["mechanical_reuse"] == "yes" for row in rows)
    total = len(rows)
    lines = [
        title,
        "",
        f"- Mechanical reuse headline: `{yes_count}/{total}` perturbed cases show mechanical reuse under broken identification.",
        "- Counting rule: `yes` means the key identifying condition is explicitly broken in the perturbed packet, but the agent still retains the base estimand, base identification logic, or only surface-level threat wording.",
        "",
        "| Case | Broken Condition | Mechanical Reuse | Rationale |",
        "|---|---|---|---|",
    ]
    for row in rows:
        lines.append(
            f"| `{row['case_id']}` | {row['broken_condition']} | `{row['mechanical_reuse']}` | {row['audit_rationale']} |"
        )
    path.write_text("\n".join(lines) + "\n")


def main() -> None:
    write_csv(OUTPUT_CSV, ROWS)
    write_markdown(OUTPUT_MD, ROWS, "# Perturbed Pair Audit")
    if ROWS_V1:
        write_csv(OUTPUT_V1_CSV, ROWS_V1)
        write_markdown(OUTPUT_V1_MD, ROWS_V1, "# Perturbed Pair Audit (research_agent_v1)")
    if ROWS_V2:
        write_csv(OUTPUT_V2_CSV, ROWS_V2)
        write_markdown(OUTPUT_V2_MD, ROWS_V2, "# Perturbed Pair Audit (research_agent_v2_search)")


if __name__ == "__main__":
    main()
