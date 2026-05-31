#!/usr/bin/env python3

from __future__ import annotations

import csv
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
OUTPUT_CSV = ROOT / "results" / "threat_recognition_audit.csv"
OUTPUT_MD = ROOT / "results" / "threat_recognition_summary.md"


ROWS = [
    {
        "case_id": "C001",
        "level2_run_id": "RUN_20260527_210840_01_openclaw_deepseekv4pro_isolated",
        "threat_1": "social-pressure identification requires a low-cost avoidance or opt-out channel, not just solicitation assignment",
        "threat_1_gold_basis": "C001 gold: Linchpin L001-L002; Must-Have Conditions 2 and 5",
        "threat_1_hit": "yes",
        "threat_1_evidence": "Sections 8 and 10 explicitly treat the Arm C vs Arm B contrast as the causal effect of adding a low-cost opt-out and reject a simple solicitation-only interpretation.",
        "threat_2": "contact and avoidance must be analyzed separately from donation outcomes",
        "threat_2_gold_basis": "C001 gold: Must-Have Conditions 1 and 4; Claim-Evidence Expectations on door opening/contact",
        "threat_2_hit": "yes",
        "threat_2_evidence": "Sections 7, 10, and 15 distinguish contact from conditional giving, and the output defines separate contact and contribution measurement issues.",
        "hits": "2",
        "max_hits": "2",
        "audit_note": "Strong recognition, despite later packet-overreach in some concrete implementation details.",
    },
    {
        "case_id": "C002",
        "level2_run_id": "RUN_20260527_215707_05_openclaw_deepseekv4pro_isolated",
        "threat_1": "selection into borrowing must be separated from post-borrowing incentive effects",
        "threat_1_gold_basis": "C002 gold: Linchpin 1-2; Must-Have Conditions 1-2",
        "threat_1_hit": "yes",
        "threat_1_evidence": "Sections 7, 8, and 10 explicitly describe a two-stage randomization that separates take-up selection from repayment incentives.",
        "threat_2": "borrowers must not know the later contract term at application",
        "threat_2_gold_basis": "C002 gold: Linchpin 3; Must-Have Condition 4; Claim-Evidence Expectations on blindness",
        "threat_2_hit": "yes",
        "threat_2_evidence": "Sections 7, 8, 10, and 11 explicitly flag information contamination and require information separation as a validity condition.",
        "hits": "2",
        "max_hits": "2",
        "audit_note": "Threat recognition is direct and design-linked.",
    },
    {
        "case_id": "C004",
        "level2_run_id": "RUN_20260527_223351_08_openclaw_deepseekv4pro_isolated",
        "threat_1": "clicks and attributed conversions are endogenous and cannot anchor the causal estimand",
        "threat_1_gold_basis": "C004 gold: Linchpin 1; Must-Have Conditions 1-3; Common Invalid Designs 1-2",
        "threat_1_hit": "yes",
        "threat_1_evidence": "Sections 10 and 17 reject user-level click comparisons and instead anchor the design on market-level ad availability and total downstream sales.",
        "threat_2": "market-level background trends require explicit pre/post counterfactual validation",
        "threat_2_gold_basis": "C004 gold: Linchpin 2; Must-Have Condition 4; Claim-Evidence Expectations on exogenous ad availability",
        "threat_2_hit": "yes",
        "threat_2_evidence": "Sections 7, 8, 11, 13, and 16 explicitly center non-parallel pre-trends and panel-based diagnostics as the main identification threat.",
        "hits": "2",
        "max_hits": "2",
        "audit_note": "The output clearly recognizes both endogenous click data and market-trend threats.",
    },
    {
        "case_id": "C005",
        "level2_run_id": "RUN_20260527_224724_11_openclaw_deepseekv4pro_isolated",
        "threat_1": "actual focal-ad exposure is endogenous because auctions, targeting, and optimization select who sees the ad",
        "threat_1_gold_basis": "C005 gold: Linchpin L001-L002; Must-Have Conditions 1-2; Claim-Evidence Expectations 1 and 3",
        "threat_1_hit": "yes",
        "threat_1_evidence": "Sections 7, 9, 15, and 16 explicitly describe non-ignorable selection between assignment and realized exposure and discuss optimization-driven bias.",
        "threat_2": "the valid counterfactual is a comparable exposure-opportunity control group, not a generic ITT or exposed-versus-unexposed comparison",
        "threat_2_gold_basis": "C005 gold: Linchpin L001-L003; Must-Have Condition 3; Claim-Evidence Expectations 2 and 4",
        "threat_2_hit": "no",
        "threat_2_evidence": "The output pivots to an encouragement-design ITT/CACE framework and never explicitly defines or defends a same-opportunity control group for treated exposed users.",
        "hits": "1",
        "max_hits": "2",
        "audit_note": "Strong on exposure endogeneity, but it misses the benchmark's narrower opportunity-matched control requirement.",
    },
    {
        "case_id": "C008",
        "level2_run_id": "RUN_20260527_230420_15_openclaw_deepseekv4pro_isolated",
        "threat_1": "treated-store before-after comparisons are invalid without untreated counterfactual structure and trend validation",
        "threat_1_gold_basis": "C008 gold: Linchpin L001-L002; Must-Have Conditions 1-3; Common Invalid Designs 1-2",
        "threat_1_hit": "yes",
        "threat_1_evidence": "Sections 7, 9, 11, 13, and 16 all foreground non-random treatment selection, parallel trends, untreated cells, and event-study validation.",
        "threat_2": "actual paid prices and promotions must be controlled so that salience is not confounded with price changes",
        "threat_2_gold_basis": "C008 gold: Measurement condition L003; Must-Have Condition 5; Common Invalid Design 3",
        "threat_2_hit": "yes",
        "threat_2_evidence": "The executive summary, Sections 7, 9, 15, 16, and the claim table all explicitly discuss actual prices and promotions as competing explanations that must be controlled.",
        "hits": "2",
        "max_hits": "2",
        "audit_note": "Threat recognition is explicit and tied to concrete design responses.",
    },
    {
        "case_id": "C010",
        "level2_run_id": "RUN_20260527_231632_18_openclaw_deepseekv4pro_isolated",
        "threat_1": "timing must be separated from subsidy magnitude and convenience; a generic subsidy contrast is insufficient",
        "threat_1_gold_basis": "C010 gold: Linchpin L001-L002; Must-Have Conditions 1-4; Common Invalid Design 1",
        "threat_1_hit": "yes",
        "threat_1_evidence": "Sections 7, 9, 10, and 16 explicitly use the T1/T2/T4 contrasts to separate timing from price magnitude and convenience.",
        "threat_2": "actual adoption and reminder-only comparisons are needed; intentions alone cannot identify the mechanism",
        "threat_2_gold_basis": "C010 gold: Linchpin L003; Must-Have Conditions 3 and 5; Claim-Evidence Expectations 3-4",
        "threat_2_hit": "yes",
        "threat_2_evidence": "Sections 9, 15, 16, and 17 treat actual adoption as the primary outcome and use a reminder-only arm to address salience/forgetting alternatives.",
        "hits": "2",
        "max_hits": "2",
        "audit_note": "The output recognizes both the timing bundle problem and the reminder/intention threat.",
    },
    {
        "case_id": "C014",
        "level2_run_id": "RUN_20260527_232816_21_openclaw_deepseekv4pro_isolated",
        "threat_1": "official records are manipulable and cannot serve as the sole corruption outcome",
        "threat_1_gold_basis": "C014 gold: Linchpin L001; Must-Have Conditions 1-2; Claim-Evidence Expectations 1-2",
        "threat_1_hit": "yes",
        "threat_1_evidence": "Sections 7, 9, 15, 16, and 17 explicitly state that administrative outcomes may react through reporting and that independent leakage measurement is essential.",
        "threat_2": "administrative or participation outcomes are not the same as true corruption outcomes",
        "threat_2_gold_basis": "C014 gold: Must-Have Condition 5; Claim-Evidence Expectations 4; Common Invalid Design 3",
        "threat_2_hit": "yes",
        "threat_2_evidence": "Sections 16 and 17 explicitly separate administrative effects from true leakage reduction and warn that monitoring-related participation or reporting changes do not equal corruption reduction.",
        "hits": "2",
        "max_hits": "2",
        "audit_note": "This case shows strong recognition that outcome validity is part of identification.",
    },
    {
        "case_id": "C016",
        "level2_run_id": "RUN_20260527_234026_24_openclaw_deepseekv4pro_isolated",
        "threat_1": "planned school-level variation may be non-random and confounded by school selection",
        "threat_1_gold_basis": "C016 gold: Must-Have Conditions 2 and 5; Common Invalid Design 1",
        "threat_1_hit": "yes",
        "threat_1_evidence": "Sections 7, 8, 10, 11, 16, and 17 explicitly state that the packet does not guarantee random assignment and that causal claims depend on confirming a real identification device.",
        "threat_2": "objective downstream outcomes are central; self-reports are selected and reporting-biased",
        "threat_2_gold_basis": "C016 gold: Linchpin L002; Must-Have Condition 3; Claim-Evidence Expectations 2 and 4",
        "threat_2_hit": "yes",
        "threat_2_evidence": "Sections 10, 15, and 17 explicitly center the objective outcome and describe self-reports as supplementary and vulnerable to selection and reporting bias.",
        "hits": "2",
        "max_hits": "2",
        "audit_note": "Threat recognition is strong even though later mechanism interpretation elsewhere can still overreach.",
    },
    {
        "case_id": "C019",
        "level2_run_id": "RUN_20260527_235916_28_openclaw_deepseekv4pro_isolated",
        "threat_1": "observed route length is endogenous, so naive route-length regressions are not causal",
        "threat_1_gold_basis": "C019 gold: Linchpin L001-L002; Must-Have Conditions 1-2; Common Invalid Design 1",
        "threat_1_hit": "yes",
        "threat_1_evidence": "Sections 7, 8, 10, and 17 explicitly describe simultaneity and reverse causality in observed route length and downgrade naive route coefficients.",
        "threat_2": "planned basket and shopping mission controls are required because they shape both route construction and unplanned spending",
        "threat_2_gold_basis": "C019 gold: Linchpin L003; Must-Have Condition 4; Claim-Evidence Expectations 3",
        "threat_2_hit": "yes",
        "threat_2_evidence": "Sections 7, 11, and 15 explicitly discuss pre-trip planned basket measurement, mission controls, and budget-related confounding.",
        "hits": "2",
        "max_hits": "2",
        "audit_note": "The output clearly recognizes both endogenous wandering and mission-selection threats.",
    },
    {
        "case_id": "C020",
        "level2_run_id": "RUN_20260528_001055_31_openclaw_deepseekv4pro_isolated",
        "threat_1": "historical manager-chosen price endings are endogenous; valid causal inference requires randomized format variation",
        "threat_1_gold_basis": "C020 gold: Linchpin L001; Must-Have Conditions 1-2; Claim-Evidence Expectations 1-2",
        "threat_1_hit": "yes",
        "threat_1_evidence": "Sections 8, 9, 10, and 11 explicitly assume researcher-randomized format assignment and reject historical observational pricing as a causal basis.",
        "threat_2": "format effects are confounded with bargain or sale cues, and familiarity heterogeneity is descriptive unless separately justified",
        "threat_2_gold_basis": "C020 gold: Linchpin L002-L003; Must-Have Conditions 4-5; Claim-Evidence Expectations 3-4",
        "threat_2_hit": "yes",
        "threat_2_evidence": "Sections 7, 9, 16, and 17 explicitly discuss bargain-signal confounding, explicit promo-cue crossing, and the non-causal status of familiarity moderation.",
        "hits": "2",
        "max_hits": "2",
        "audit_note": "The output is explicit about both promotional-cue confounding and the limits of familiarity heterogeneity.",
    },
]


FIELDNAMES = [
    "case_id",
    "level2_run_id",
    "threat_1",
    "threat_1_gold_basis",
    "threat_1_hit",
    "threat_1_evidence",
    "threat_2",
    "threat_2_gold_basis",
    "threat_2_hit",
    "threat_2_evidence",
    "hits",
    "max_hits",
    "audit_note",
]


def summarize_rows(rows: list[dict[str, str]]) -> dict[str, float | int]:
    case_count = len(rows)
    total_hits = sum(int(row["hits"]) for row in rows)
    max_possible_hits = sum(int(row["max_hits"]) for row in rows)
    two_of_two_cases = sum(int(row["hits"]) == 2 for row in rows)
    one_of_two_cases = sum(int(row["hits"]) == 1 for row in rows)
    zero_of_two_cases = sum(int(row["hits"]) == 0 for row in rows)
    average_hits_per_case = total_hits / case_count if case_count else 0.0
    overall_hit_rate = total_hits / max_possible_hits if max_possible_hits else 0.0
    return {
        "case_count": case_count,
        "total_hits": total_hits,
        "max_possible_hits": max_possible_hits,
        "average_hits_per_case": average_hits_per_case,
        "overall_hit_rate": overall_hit_rate,
        "two_of_two_cases": two_of_two_cases,
        "one_of_two_cases": one_of_two_cases,
        "zero_of_two_cases": zero_of_two_cases,
    }


def write_csv(rows: list[dict[str, str]], path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=FIELDNAMES, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def write_markdown(rows: list[dict[str, str]], path: Path) -> None:
    summary = summarize_rows(rows)
    lines = [
        "# Threat Recognition Summary",
        "",
        "- Scope: baseline `level2` main-set outputs only (`10` cases).",
        "- Unit of audit: `2` pre-defined threats per case.",
        "- Counting rule: a threat is a hit only if the output both identifies the threat and gives a concrete design response, assumption, limitation, or non-claim that addresses it.",
        "- This is a light RQ1 audit layer, not a new full annotation system.",
        "",
        "## Headline",
        "",
        f"- Average threat hits per case: `{summary['average_hits_per_case']:.1f}/2`",
        f"- Overall threat hit rate: `{summary['total_hits']}/{summary['max_possible_hits']} = {summary['overall_hit_rate']:.1%}`",
        f"- `{summary['two_of_two_cases']}/{summary['case_count']}` cases scored `2/2`",
        f"- `{summary['one_of_two_cases']}/{summary['case_count']}` cases scored `1/2`",
        f"- `{summary['zero_of_two_cases']}/{summary['case_count']}` cases scored `0/2`",
        "",
        "## Interpretation",
        "",
        "- Baseline `level2` outputs usually recognize the core threats in these cases.",
        "- The main remaining weakness is not total threat blindness at `level2`; it is more often overclaiming, packet overreach, or failure to keep later claims aligned with the recognized threat structure.",
        "- The clearest miss in this audit is `C005`, where the output recognizes endogenous exposure but does not recover the benchmark's narrower requirement of a comparable exposure-opportunity control group.",
        "",
        "## Case Table",
        "",
        "| Case | Hits | Note |",
        "|---|---:|---|",
    ]
    for row in rows:
        lines.append(f"| `{row['case_id']}` | `{row['hits']}/{row['max_hits']}` | {row['audit_note']} |")
    path.write_text("\n".join(lines) + "\n")


def main() -> None:
    write_csv(ROWS, OUTPUT_CSV)
    write_markdown(ROWS, OUTPUT_MD)


if __name__ == "__main__":
    main()
