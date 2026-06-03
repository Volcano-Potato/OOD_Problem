#!/usr/bin/env python3

from __future__ import annotations

import csv
from collections import Counter, defaultdict
from pathlib import Path
import yaml


ROOT = Path(__file__).resolve().parent.parent
LABELS_CSV = ROOT / "annotations" / "adjudicated_labels.csv"
MANIFEST_CSV = ROOT / "outputs" / "run_manifest.csv"
RESULTS_DIR = ROOT / "results"
FIGURES_DIR = RESULTS_DIR / "figures"
METRICS_SUMMARY_CSV = RESULTS_DIR / "metrics_summary.csv"
METRICS_SUMMARY_MD = RESULTS_DIR / "metrics_summary.md"
ERROR_COUNTS_CSV = RESULTS_DIR / "error_type_counts.csv"
ERROR_COUNTS_BY_VARIANT_CSV = RESULTS_DIR / "error_type_counts_by_agent_variant.csv"
CASE_LEVEL_CSV = RESULTS_DIR / "case_level_scores.csv"
RUN_LEVEL_CSV = RESULTS_DIR / "run_level_scores.csv"
GROUPED_CSV = RESULTS_DIR / "grouped_metrics.csv"
PERTURBED_AUDIT_CSV = RESULTS_DIR / "perturbed_mechanical_reuse.csv"
ABLATION_SUMMARY_CSV = RESULTS_DIR / "research_agent_ablation_summary.csv"
DEFAULT_AGENT_VARIANT = "benchmark_isolated"

CLAIM_SCORE = {
    "supported": 1.0,
    "partially_supported": 0.5,
    "unsupported": 0.0,
    "contradicted": 0.0,
}

CAUSAL_KEYWORDS = (
    "causal",
    "itt",
    "late",
    "cace",
    "experimental",
    "randomized",
    "parallel trends",
    "iv assumptions",
)

SVG_NS = "http://www.w3.org/2000/svg"


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="") as f:
        return list(csv.DictReader(f))


def write_csv(path: Path, rows: list[dict[str, object]], fieldnames: list[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames, lineterminator="\n")
        writer.writeheader()
        for row in rows:
            writer.writerow(row)


def normalize_agent_variant(value: str | None) -> str:
    return value or DEFAULT_AGENT_VARIANT


def metric_suffix(agent_variant: str) -> str:
    return agent_variant.lower().replace("-", "_")


def filter_by_agent_variant(rows: list[dict[str, object]], agent_variant: str) -> list[dict[str, object]]:
    return [row for row in rows if str(row.get("agent_variant")) == agent_variant]


def research_metrics_summary_paths(agent_variant: str) -> tuple[Path, Path]:
    suffix = metric_suffix(agent_variant)
    return (
        RESULTS_DIR / f"metrics_summary_{suffix}.csv",
        RESULTS_DIR / f"metrics_summary_{suffix}.md",
    )


def perturbed_audit_path_for_variant(agent_variant: str) -> Path:
    if agent_variant == DEFAULT_AGENT_VARIANT:
        return PERTURBED_AUDIT_CSV
    if agent_variant == "research_agent_v1":
        return RESULTS_DIR / "perturbed_mechanical_reuse_v1.csv"
    if agent_variant == "research_agent_v2_search":
        return RESULTS_DIR / "perturbed_mechanical_reuse_v2.csv"
    if agent_variant == "research_agent_v3_planner_debate":
        return RESULTS_DIR / "perturbed_mechanical_reuse_v3.csv"
    return RESULTS_DIR / f"perturbed_mechanical_reuse_{metric_suffix(agent_variant)}.csv"


def load_metadata() -> dict[str, dict[str, str]]:
    out: dict[str, dict[str, str]] = {}
    for path in sorted((ROOT / "benchmark" / "cases").glob("C*/metadata.yaml")):
        data = yaml.safe_load(path.read_text())
        if not data.get("selection", {}).get("selected_for_main"):
            continue
        taxonomy = data["taxonomy"]
        out[data["case_id"]] = {
            "case_name": data["anonymous_short_name"],
            "domain": taxonomy["domain"],
            "subdomain": taxonomy["subdomain"],
            "design_family": taxonomy["design_family"],
            "variation_source": taxonomy["variation_source"],
            "assignment_level": taxonomy["assignment_level"],
            "outcome_level": taxonomy["outcome_level"],
            "unit_of_observation": taxonomy["unit_of_observation"],
            "key_failure_mode": taxonomy["key_failure_mode"],
            "secondary_failure_modes": "|".join(taxonomy["secondary_failure_modes"]),
            "difficulty": taxonomy["difficulty"],
        }
    return out


def load_main_manifest() -> list[dict[str, str]]:
    rows = read_csv(MANIFEST_CSV)
    main_rows = []
    for row in rows:
        if "/raw_agent_logs/main/" not in row["raw_output_file"]:
            continue
        row["agent_variant"] = normalize_agent_variant(row.get("agent_variant"))
        main_rows.append(row)
    return main_rows


def load_perturbed_audit(agent_variant: str = DEFAULT_AGENT_VARIANT) -> list[dict[str, str]]:
    path = perturbed_audit_path_for_variant(agent_variant)
    if not path.exists():
        return []
    return read_csv(path)


def annotate_labels(
    rows: list[dict[str, str]], metadata: dict[str, dict[str, str]]
) -> list[dict[str, object]]:
    enriched: list[dict[str, object]] = []
    for row in rows:
        meta = metadata[row["case_id"]]
        claim_type_lc = row["claim_type"].lower()
        is_causal_claim = any(key in claim_type_lc for key in CAUSAL_KEYWORDS)
        score = CLAIM_SCORE[row["final_label"]]
        enriched.append(
            {
                **row,
                **meta,
                "agent_variant": normalize_agent_variant(row.get("agent_variant")),
                "claim_score": score,
                "is_error": row["final_error_type"] != "none",
                "is_unsupported": row["final_error_type"] == "Unsupported Claim",
                "is_contradiction": row["final_error_type"] == "Contradiction",
                "is_overclaim": row["final_error_type"] == "Overclaim",
                "is_critical": row["final_severity"] == "critical",
                "is_mechanism_family": meta["key_failure_mode"] == "mechanism_confounding",
                "is_causal_claim": is_causal_claim,
            }
        )
    return enriched


def rate(num: int, den: int) -> float:
    return 0.0 if den == 0 else num / den


def mean(values: list[float]) -> float:
    return 0.0 if not values else sum(values) / len(values)


def svg_escape(text: object) -> str:
    s = str(text)
    return (
        s.replace("&", "&amp;")
        .replace("<", "&lt;")
        .replace(">", "&gt;")
        .replace('"', "&quot;")
    )


def write_svg(path: Path, width: int, height: int, body: list[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    content = [
        f'<svg xmlns="{SVG_NS}" width="{width}" height="{height}" viewBox="0 0 {width} {height}">',
        '<rect width="100%" height="100%" fill="white"/>',
        *body,
        "</svg>",
    ]
    path.write_text("\n".join(content) + "\n")


def build_run_level(rows: list[dict[str, object]]) -> list[dict[str, object]]:
    by_run: dict[str, list[dict[str, object]]] = defaultdict(list)
    for row in rows:
        by_run[str(row["run_id"])].append(row)

    run_level: list[dict[str, object]] = []
    for run_id, claims in sorted(by_run.items()):
        first = claims[0]
        scores = [float(c["claim_score"]) for c in claims]
        n_claims = len(claims)
        supported = sum(c["final_label"] == "supported" for c in claims)
        partial = sum(c["final_label"] == "partially_supported" for c in claims)
        unsupported = sum(c["final_label"] == "unsupported" for c in claims)
        contradicted = sum(c["final_label"] == "contradicted" for c in claims)
        errors = sum(bool(c["is_error"]) for c in claims)
        critical = sum(bool(c["is_critical"]) for c in claims)
        causal_supported = sum(
            bool(c["is_causal_claim"])
            and c["final_label"] in {"supported", "partially_supported"}
            for c in claims
        )
        no_solution_honest = ""
        if first["variant_id"] == "no_solution":
            no_solution_honest = "yes" if causal_supported == 0 else "no"
        run_level.append(
            {
                "run_id": run_id,
                "case_id": first["case_id"],
                "variant_id": first["variant_id"],
                "agent_variant": first["agent_variant"],
                "domain": first["domain"],
                "design_family": first["design_family"],
                "key_failure_mode": first["key_failure_mode"],
                "n_claims": n_claims,
                "mean_claim_score": round(mean(scores), 4),
                "supported_rate": round(rate(supported, n_claims), 4),
                "partial_rate": round(rate(partial, n_claims), 4),
                "unsupported_rate": round(rate(unsupported, n_claims), 4),
                "contradicted_rate": round(rate(contradicted, n_claims), 4),
                "inconsistency_rate": round(rate(errors, n_claims), 4),
                "critical_issue_rate": round(rate(critical, n_claims), 4),
                "supported_causal_claims": causal_supported,
                "no_solution_honest": no_solution_honest,
            }
        )
    return run_level


def aggregate_group(
    rows: list[dict[str, object]], key_fields: list[str]
) -> list[dict[str, object]]:
    grouped: dict[tuple[str, ...], list[dict[str, object]]] = defaultdict(list)
    for row in rows:
        key = tuple(str(row[field]) for field in key_fields)
        grouped[key].append(row)

    output: list[dict[str, object]] = []
    for key, items in sorted(grouped.items()):
        scores = [float(i["claim_score"]) for i in items]
        n = len(items)
        record = {field: value for field, value in zip(key_fields, key)}
        record.update(
            {
                "n_claims": n,
                "mean_claim_score": round(mean(scores), 4),
                "supported_rate": round(rate(sum(i["final_label"] == "supported" for i in items), n), 4),
                "partial_rate": round(rate(sum(i["final_label"] == "partially_supported" for i in items), n), 4),
                "unsupported_rate": round(rate(sum(i["final_label"] == "unsupported" for i in items), n), 4),
                "contradicted_rate": round(rate(sum(i["final_label"] == "contradicted" for i in items), n), 4),
                "inconsistency_rate": round(rate(sum(bool(i["is_error"]) for i in items), n), 4),
                "critical_issue_rate": round(rate(sum(bool(i["is_critical"]) for i in items), n), 4),
            }
        )
        output.append(record)
    return output


def build_case_level(rows: list[dict[str, object]]) -> list[dict[str, object]]:
    grouped = aggregate_group(rows, ["case_id", "domain", "design_family", "key_failure_mode", "variant_id"])
    for record in grouped:
        record["level"] = record["variant_id"]
    return grouped


def compute_metrics(
    rows: list[dict[str, object]],
    run_level: list[dict[str, object]],
    manifest_rows: list[dict[str, str]],
    perturbed_audit_rows: list[dict[str, str]],
) -> list[dict[str, object]]:
    total_claims = len(rows)
    total_runs = len(run_level)
    inconsistency_num = sum(bool(r["is_error"]) for r in rows)
    unsupported_num = sum(bool(r["is_unsupported"]) for r in rows)
    contradiction_num = sum(bool(r["is_contradiction"]) for r in rows)
    overclaim_num = sum(bool(r["is_overclaim"]) for r in rows)
    critical_num = sum(bool(r["is_critical"]) for r in rows)
    mechanism_rows = [r for r in rows if bool(r["is_mechanism_family"])]
    no_solution_runs = [r for r in run_level if r["variant_id"] == "no_solution"]
    honest_no_solution = sum(r["no_solution_honest"] == "yes" for r in no_solution_runs)
    perturbed_audit_yes = sum(r["mechanical_reuse"] == "yes" for r in perturbed_audit_rows)
    manifest_success = sum(r["status"] == "success" for r in manifest_rows)
    manifest_aborted = sum(r["status"] == "aborted" for r in manifest_rows)
    contaminated = sum(r["contamination_status"] == "contaminated" for r in manifest_rows)
    unknown_contam = sum(r["contamination_status"] == "unknown" for r in manifest_rows)

    level1_scores = [r["mean_claim_score"] for r in run_level if r["variant_id"] == "level1"]
    level2_scores = [r["mean_claim_score"] for r in run_level if r["variant_id"] == "level2"]
    level3_scores = [r["mean_claim_score"] for r in run_level if r["variant_id"] == "level3"]
    perturbed_scores = [r["mean_claim_score"] for r in run_level if r["variant_id"] == "perturbed"]

    return [
        {
            "metric": "Total Claims",
            "scope": "claim",
            "numerator": total_claims,
            "denominator": total_claims,
            "value": total_claims,
            "formula": "count(all adjudicated claims)",
            "notes": "Source: annotations/adjudicated_labels.csv",
        },
        {
            "metric": "Mean Claim Score",
            "scope": "claim",
            "numerator": round(sum(float(r["claim_score"]) for r in rows), 4),
            "denominator": total_claims,
            "value": round(mean([float(r["claim_score"]) for r in rows]), 4),
            "formula": "mean(score), with supported=1, partially_supported=0.5, unsupported/contradicted=0",
            "notes": "Primary claim-level quality score.",
        },
        {
            "metric": "Design-Evidence Inconsistency Rate",
            "scope": "claim",
            "numerator": inconsistency_num,
            "denominator": total_claims,
            "value": round(rate(inconsistency_num, total_claims), 4),
            "formula": "count(error_type in {Overclaim, Unsupported Claim, Contradiction}) / total_claims",
            "notes": "Current annotation schema did not emit Mis-citation labels in this round.",
        },
        {
            "metric": "Unsupported Design Claim Rate",
            "scope": "claim",
            "numerator": unsupported_num,
            "denominator": total_claims,
            "value": round(rate(unsupported_num, total_claims), 4),
            "formula": "count(error_type == Unsupported Claim) / total_claims",
            "notes": "Contradictions are reported separately.",
        },
        {
            "metric": "Contradiction Rate",
            "scope": "claim",
            "numerator": contradiction_num,
            "denominator": total_claims,
            "value": round(rate(contradiction_num, total_claims), 4),
            "formula": "count(error_type == Contradiction) / total_claims",
            "notes": "Useful for perturbed and no-solution stress tests.",
        },
        {
            "metric": "Overclaim Rate",
            "scope": "claim",
            "numerator": overclaim_num,
            "denominator": total_claims,
            "value": round(rate(overclaim_num, total_claims), 4),
            "formula": "count(error_type == Overclaim) / total_claims",
            "notes": "Captures source-like concretization and claim-strength inflation.",
        },
        {
            "metric": "Critical Design Omission Rate (proxy)",
            "scope": "claim",
            "numerator": critical_num,
            "denominator": total_claims,
            "value": round(rate(critical_num, total_claims), 4),
            "formula": "count(final_severity == critical) / total_claims",
            "notes": "Proxy because the current annotation schema does not have an explicit omission-only label.",
        },
        {
            "metric": "Mechanism Confounding Rate (proxy)",
            "scope": "claim",
            "numerator": sum(bool(r["is_error"]) for r in mechanism_rows),
            "denominator": len(mechanism_rows),
            "value": round(rate(sum(bool(r["is_error"]) for r in mechanism_rows), len(mechanism_rows)), 4),
            "formula": "count(non-supported claims in cases with key_failure_mode == mechanism_confounding) / total_claims_in_those_cases",
            "notes": "Proxy for mechanism-sensitive failures under the current label schema.",
        },
        {
            "metric": "No-solution Honesty Rate",
            "scope": "run",
            "numerator": honest_no_solution,
            "denominator": len(no_solution_runs),
            "value": round(rate(honest_no_solution, len(no_solution_runs)), 4),
            "formula": "count(no_solution runs with zero supported/partially-supported causal claims) / total_no_solution_runs",
            "notes": f"Causal claims are detected from claim_type keywords. Interpret as 'all {len(no_solution_runs)} tested no-solution runs' rather than as a broad population rate.",
        },
        {
            "metric": "Perturbed Mechanical Reuse Rate",
            "scope": "run",
            "numerator": perturbed_audit_yes,
            "denominator": len(perturbed_audit_rows),
            "value": round(rate(perturbed_audit_yes, len(perturbed_audit_rows)), 4),
            "formula": "count(perturbed cases with mechanical_reuse == yes) / total_perturbed_cases_audited",
            "notes": "Derived from results/perturbed_mechanical_reuse.csv and interpreted as a paired Level 2 vs Perturbed audit.",
        },
        {
            "metric": "Level 1 Mean Run Score",
            "scope": "run",
            "numerator": round(sum(level1_scores), 4),
            "denominator": len(level1_scores),
            "value": round(mean(level1_scores), 4),
            "formula": "mean(run mean_claim_score for variant == level1)",
            "notes": "Task 26 extends the information gradient to Level 1, Level 2, and Level 3.",
        },
        {
            "metric": "Level 2 Mean Run Score",
            "scope": "run",
            "numerator": round(sum(level2_scores), 4),
            "denominator": len(level2_scores),
            "value": round(mean(level2_scores), 4),
            "formula": "mean(run mean_claim_score for variant == level2)",
            "notes": "Interpret jointly with Level 1 and Level 3 after Task 26.",
        },
        {
            "metric": "Level 3 Mean Run Score",
            "scope": "run",
            "numerator": round(sum(level3_scores), 4),
            "denominator": len(level3_scores),
            "value": round(mean(level3_scores), 4),
            "formula": "mean(run mean_claim_score for variant == level3)",
            "notes": "Do not describe small Level 2 to Level 3 deltas as meaningful without stronger support.",
        },
        {
            "metric": "Perturbed Mean Run Score",
            "scope": "run",
            "numerator": round(sum(perturbed_scores), 4),
            "denominator": len(perturbed_scores),
            "value": round(mean(perturbed_scores), 4),
            "formula": "mean(run mean_claim_score for variant == perturbed)",
            "notes": "Used to measure downgrade under broken identification conditions.",
        },
        {
            "metric": "Main Success Runs",
            "scope": "run",
            "numerator": manifest_success,
            "denominator": len(manifest_rows),
            "value": manifest_success,
            "formula": "count(status == success) among manifest rows under outputs/raw_agent_logs/main/",
            "notes": "Only success runs entered claim extraction and adjudication.",
        },
        {
            "metric": "Main Aborted Runs",
            "scope": "run",
            "numerator": manifest_aborted,
            "denominator": len(manifest_rows),
            "value": manifest_aborted,
            "formula": "count(status == aborted) among manifest rows under outputs/raw_agent_logs/main/",
            "notes": "Historical aborted rows were retained in the manifest after reruns.",
        },
        {
            "metric": "Main Unknown Contamination Rows",
            "scope": "run",
            "numerator": unknown_contam,
            "denominator": len(manifest_rows),
            "value": unknown_contam,
            "formula": "count(contamination_status == unknown) among main manifest rows",
            "notes": "Content-level adjudication is complete, but manifest contamination_status was not backfilled in Task 22.",
        },
        {
            "metric": "Main Contaminated Rows",
            "scope": "run",
            "numerator": contaminated,
            "denominator": len(manifest_rows),
            "value": contaminated,
            "formula": "count(contamination_status == contaminated) among main manifest rows",
            "notes": "No main-row was explicitly marked contaminated in the manifest.",
        },
    ]


def build_error_counts(rows: list[dict[str, object]]) -> list[dict[str, object]]:
    counts = Counter(str(r["final_error_type"]) for r in rows)
    total = len(rows)
    ordered = ["none", "Overclaim", "Unsupported Claim", "Contradiction"]
    return [
        {
            "error_type": name,
            "count": counts.get(name, 0),
            "rate": round(rate(counts.get(name, 0), total), 4),
        }
        for name in ordered
    ]


def build_error_counts_by_agent_variant(rows: list[dict[str, object]]) -> list[dict[str, object]]:
    ordered_variants = [
        DEFAULT_AGENT_VARIANT,
        "research_agent_v1",
        "research_agent_v2_search",
        "research_agent_v3_planner_debate",
    ]
    ordered_errors = ["none", "Overclaim", "Unsupported Claim", "Contradiction"]
    output: list[dict[str, object]] = []
    for agent_variant in ordered_variants:
        subset = [row for row in rows if str(row["agent_variant"]) == agent_variant]
        if not subset:
            continue
        counts = Counter(str(r["final_error_type"]) for r in subset)
        total = len(subset)
        for error_type in ordered_errors:
            output.append(
                {
                    "agent_variant": agent_variant,
                    "error_type": error_type,
                    "count": counts.get(error_type, 0),
                    "rate": round(rate(counts.get(error_type, 0), total), 4),
                    "n_claims": total,
                }
            )
    return output


def build_grouped_metrics(rows: list[dict[str, object]], run_level: list[dict[str, object]]) -> list[dict[str, object]]:
    out: list[dict[str, object]] = []
    claim_groups = [
        ("domain", aggregate_group(rows, ["domain"])),
        ("design_family", aggregate_group(rows, ["design_family"])),
        ("key_failure_mode", aggregate_group(rows, ["key_failure_mode"])),
        ("variant_id", aggregate_group(rows, ["variant_id"])),
        ("agent_variant", aggregate_group(rows, ["agent_variant"])),
        ("agent_variant_x_variant_id", aggregate_group(rows, ["agent_variant", "variant_id"])),
    ]
    for group_field, records in claim_groups:
        for record in records:
            if group_field == "agent_variant_x_variant_id":
                key_value = f"{record['agent_variant']}::{record['variant_id']}"
            else:
                key_value = record[group_field]
            out.append(
                {
                    "group_type": group_field,
                    "group_value": key_value,
                    "scope": "claim",
                    "n_units": record["n_claims"],
                    "mean_claim_score": record["mean_claim_score"],
                    "inconsistency_rate": record["inconsistency_rate"],
                    "critical_issue_rate": record["critical_issue_rate"],
                }
            )

    run_groups: dict[str, list[dict[str, object]]] = defaultdict(list)
    for row in run_level:
        for field in ("domain", "design_family", "key_failure_mode", "variant_id", "agent_variant"):
            run_groups[f"{field}:{row[field]}"].append(row)
        run_groups[f"agent_variant_x_variant_id:{row['agent_variant']}::{row['variant_id']}"].append(row)
    for composite_key, records in sorted(run_groups.items()):
        field, value = composite_key.split(":", 1)
        out.append(
            {
                "group_type": field,
                "group_value": value,
                "scope": "run",
                "n_units": len(records),
                "mean_claim_score": round(mean([float(r["mean_claim_score"]) for r in records]), 4),
                "inconsistency_rate": round(mean([float(r["inconsistency_rate"]) for r in records]), 4),
                "critical_issue_rate": round(mean([float(r["critical_issue_rate"]) for r in records]), 4),
            }
        )
    return out


def load_ablation_summary() -> list[dict[str, object]]:
    if not ABLATION_SUMMARY_CSV.exists():
        return []
    rows: list[dict[str, object]] = []
    for row in read_csv(ABLATION_SUMMARY_CSV):
        rows.append(
            {
                "arm": row["arm"],
                "mechanical_reuse_yes_count": int(row["mechanical_reuse_yes_count"]),
                "mechanical_reuse_rate": float(row["mechanical_reuse_rate"]),
                "tool_use_rate": float(row["tool_use_rate"]),
                "retrieval_success_rate": float(row["retrieval_success_rate"]),
                "planner_usage_rate": float(row["planner_usage_rate"]),
                "mean_debate_rounds": float(row["mean_debate_rounds"]),
                "mean_retrieval_tool_calls": float(row["mean_retrieval_tool_calls"]),
                "mean_pipeline_duration_sec": float(row["mean_pipeline_duration_sec"]),
                "pipeline_complexity_note": row["pipeline_complexity_note"],
                "headline_reading": row["headline_reading"],
            }
        )
    return rows


def format_arm_label(arm: str) -> str:
    mapping = {
        "baseline": "Baseline",
        "research_agent_v1": "v1",
        "research_agent_v2_search": "v2",
        "research_agent_v3_planner_debate": "v3",
    }
    return mapping.get(arm, arm)


def make_ablation_ladder_figure(ablation_rows: list[dict[str, object]]) -> None:
    if not ablation_rows:
        return
    ordered = ["baseline", "research_agent_v1", "research_agent_v2_search", "research_agent_v3_planner_debate"]
    rows = [row for arm in ordered for row in ablation_rows if str(row["arm"]) == arm]
    output_rows = [
        {
            "arm": format_arm_label(str(row["arm"])),
            "mechanical_reuse_yes_count": int(row["mechanical_reuse_yes_count"]),
            "mechanical_reuse_rate": round(float(row["mechanical_reuse_rate"]), 4),
        }
        for row in rows
    ]
    write_csv(
        FIGURES_DIR / "research_agent_ablation_ladder.csv",
        output_rows,
        ["arm", "mechanical_reuse_yes_count", "mechanical_reuse_rate"],
    )

    width, height = 920, 560
    margin_left, margin_bottom, margin_top = 96, 96, 144
    plot_w, plot_h = width - margin_left - 48, height - margin_bottom - margin_top
    colors = {
        "baseline": "#7B4651",
        "research_agent_v1": "#C78B47",
        "research_agent_v2_search": "#2F6B5F",
        "research_agent_v3_planner_debate": "#7E97C2",
    }
    grid = "#E2E8F0"
    text_dark = "#1F2937"
    text_mid = "#5B6472"
    accent_fill = "#F5F8FC"
    accent_line = "#D6E1EE"
    body = [
        f'<rect x="28" y="18" width="{width-56}" height="84" rx="16" fill="{accent_fill}" stroke="{accent_line}"/>',
        f'<text x="40" y="44" font-size="13" font-weight="700" fill="{colors["research_agent_v2_search"]}">Main Result</text>',
        f'<text x="40" y="68" font-size="24" font-weight="700" fill="{text_dark}">Mechanical reuse falls from 9/10 at baseline to 0/10 by v2.</text>',
        f'<text x="40" y="90" font-size="12" fill="{text_mid}">Paired perturbed audit; lower is better. v3 matches v2 on accuracy but adds no further headline reduction.</text>',
        f'<line x1="{margin_left}" y1="{height-margin_bottom}" x2="{width-24}" y2="{height-margin_bottom}" stroke="{text_dark}" stroke-width="1.4"/>',
        f'<line x1="{margin_left}" y1="{margin_top}" x2="{margin_left}" y2="{height-margin_bottom}" stroke="{text_dark}" stroke-width="1.4"/>',
        f'<text x="28" y="{margin_top + plot_h/2}" transform="rotate(-90 28 {margin_top + plot_h/2})" text-anchor="middle" font-size="13" fill="{text_dark}">Mechanical Reuse Rate</text>',
    ]
    for tick in range(6):
        y_val = tick / 5
        y = height - margin_bottom - plot_h * y_val
        body.append(f'<line x1="{margin_left}" y1="{y}" x2="{width-24}" y2="{y}" stroke="{grid}" stroke-width="1"/>')
        body.append(f'<text x="{margin_left-10}" y="{y+4}" text-anchor="end" font-size="11" fill="{text_mid}">{y_val:.1f}</text>')
    bar_w = plot_w / (len(rows) * 1.45)
    for i, row in enumerate(rows):
        rate_value = float(row["mechanical_reuse_rate"])
        count_value = int(row["mechanical_reuse_yes_count"])
        arm = str(row["arm"])
        x = margin_left + (i + 0.28) * bar_w
        h = plot_h * rate_value
        y = height - margin_bottom - h
        label = format_arm_label(arm)
        fill = colors[arm]
        highlight = arm == "research_agent_v2_search"
        bar_height = h if h > 0 else 3
        body.append(
            f'<rect x="{x}" y="{height-margin_bottom-bar_height}" width="{bar_w*0.82}" height="{bar_height}" '
            f'rx="10" fill="{fill}" fill-opacity="0.96" '
            f'stroke="{"#154E43" if highlight else fill}" stroke-width="{"2.2" if highlight else "0"}"/>'
        )
        if highlight:
            body.append(
                f'<rect x="{x-10}" y="{margin_top+14}" width="{bar_w*0.82+20}" height="34" rx="10" fill="#E4F3EE" stroke="#2F6B5F" stroke-width="1.2"/>'
            )
            body.append(
                f'<text x="{x + bar_w*0.41}" y="{margin_top+36}" text-anchor="middle" font-size="12" font-weight="700" fill="#20584D">Recommended default: v2</text>'
            )
        if arm == "research_agent_v3_planner_debate":
            body.append(
                f'<text x="{x + bar_w*0.41}" y="{margin_top+34}" text-anchor="middle" font-size="11" fill="{text_mid}">same 0/10, higher cost</text>'
            )
        body.append(f'<text x="{x + bar_w*0.41}" y="{height-margin_bottom+28}" text-anchor="middle" font-size="12" font-weight="700" fill="{text_dark}">{label}</text>')
        body.append(f'<text x="{x + bar_w*0.41}" y="{max(y-20, margin_top-10)}" text-anchor="middle" font-size="17" font-weight="700" fill="{fill}">{count_value}/10</text>')
        body.append(f'<text x="{x + bar_w*0.41}" y="{max(y-4, margin_top+10)}" text-anchor="middle" font-size="11" fill="{text_mid}">{rate_value:.0%} reuse</text>')
    write_svg(FIGURES_DIR / "research_agent_ablation_ladder.svg", width, height, body)


def make_cost_benefit_figure(ablation_rows: list[dict[str, object]]) -> None:
    if not ablation_rows:
        return
    ordered = ["baseline", "research_agent_v1", "research_agent_v2_search", "research_agent_v3_planner_debate"]
    rows = [row for arm in ordered for row in ablation_rows if str(row["arm"]) == arm]
    output_rows = [
        {
            "arm": format_arm_label(str(row["arm"])),
            "mean_pipeline_duration_sec": round(float(row["mean_pipeline_duration_sec"]), 3),
            "mechanical_reuse_rate": round(float(row["mechanical_reuse_rate"]), 4),
            "mean_retrieval_tool_calls": round(float(row["mean_retrieval_tool_calls"]), 3),
        }
        for row in rows
    ]
    write_csv(
        FIGURES_DIR / "research_agent_cost_benefit.csv",
        output_rows,
        ["arm", "mean_pipeline_duration_sec", "mechanical_reuse_rate", "mean_retrieval_tool_calls"],
    )

    width, height = 980, 560
    margin_left, margin_bottom, margin_top = 98, 92, 146
    plot_w, plot_h = width - margin_left - 70, height - margin_bottom - margin_top
    x_max = max(float(row["mean_pipeline_duration_sec"]) for row in rows) if rows else 1.0
    x_max = max(x_max, 1.0)
    colors = {
        "baseline": "#7B4651",
        "research_agent_v1": "#C78B47",
        "research_agent_v2_search": "#2F6B5F",
        "research_agent_v3_planner_debate": "#7E97C2",
    }
    text_dark = "#1F2937"
    text_mid = "#5B6472"
    grid = "#D9DEE7"
    display_offsets = {
        "baseline": 0.08,
        "research_agent_v1": 0.15,
    }
    body = [
        f'<rect x="28" y="18" width="{width-56}" height="86" rx="16" fill="#F5F8FC" stroke="#D6E1EE"/>',
        f'<text x="40" y="44" font-size="13" font-weight="700" fill="{colors["research_agent_v2_search"]}">Efficiency Frontier</text>',
        f'<text x="40" y="68" font-size="24" font-weight="700" fill="{text_dark}">v2 sits on the best cost–benefit frontier.</text>',
        f'<text x="40" y="90" font-size="12" fill="{text_mid}">x-axis: mean pipeline duration. y-axis: perturbed mechanical reuse. Bubble size encodes mean retrieval tool calls.</text>',
        f'<line x1="{margin_left}" y1="{height-margin_bottom}" x2="{width-24}" y2="{height-margin_bottom}" stroke="{text_dark}" stroke-width="1.4"/>',
        f'<line x1="{margin_left}" y1="{margin_top}" x2="{margin_left}" y2="{height-margin_bottom}" stroke="{text_dark}" stroke-width="1.4"/>',
        f'<text x="{width/2}" y="{height-26}" text-anchor="middle" font-size="13" fill="{text_dark}">Mean Pipeline Duration (seconds)</text>',
        f'<text x="28" y="{margin_top + plot_h/2}" transform="rotate(-90 28 {margin_top + plot_h/2})" text-anchor="middle" font-size="13" fill="{text_dark}">Mechanical Reuse Rate</text>',
    ]
    for tick in range(6):
        frac = tick / 5
        x_val = round(x_max * frac)
        x = margin_left + plot_w * frac
        body.append(f'<line x1="{x}" y1="{margin_top}" x2="{x}" y2="{height-margin_bottom}" stroke="{grid}" stroke-width="1"/>')
        body.append(f'<text x="{x}" y="{height-margin_bottom+24}" text-anchor="middle" font-size="11" fill="{text_mid}">{x_val}</text>')
        y_val = frac
        y = height - margin_bottom - plot_h * y_val
        body.append(f'<line x1="{margin_left}" y1="{y}" x2="{width-24}" y2="{y}" stroke="{grid}" stroke-width="1"/>')
        body.append(f'<text x="{margin_left-10}" y="{y+4}" text-anchor="end" font-size="11" fill="{text_mid}">{y_val:.1f}</text>')
    for row in rows:
        arm = str(row["arm"])
        x_value = float(row["mean_pipeline_duration_sec"])
        y_value = float(row["mechanical_reuse_rate"])
        tool_calls = float(row["mean_retrieval_tool_calls"])
        effective_frac = x_value / x_max if x_max else 0.0
        if x_value == 0.0:
            effective_frac = display_offsets.get(arm, 0.0)
        x = margin_left + plot_w * effective_frac
        y = height - margin_bottom - plot_h * y_value
        radius = 7 + min(tool_calls, 40.0) * 0.18
        fill = colors[arm]
        label = format_arm_label(arm)
        body.append(f'<circle cx="{x}" cy="{y}" r="{radius+4:.1f}" fill="none" stroke="{"#2F6B5F" if arm=="research_agent_v2_search" else "transparent"}" stroke-width="2.2"/>')
        body.append(f'<circle cx="{x}" cy="{y}" r="{radius:.1f}" fill="{fill}" fill-opacity="0.86" stroke="white" stroke-width="2"/>')
        body.append(f'<text x="{x}" y="{y - radius - 12}" text-anchor="middle" font-size="12" font-weight="700" fill="{text_dark}">{label}</text>')
        duration_label = "0s" if x_value == 0.0 else f"{x_value:.0f}s"
        body.append(f'<text x="{x}" y="{y + radius + 18}" text-anchor="middle" font-size="11" fill="{text_mid}">{duration_label} • {y_value:.0%}</text>')
        if arm == "research_agent_v2_search":
            body.append(f'<path d="M {x-18} {y-18} L {x-126} {y-78}" stroke="#2F6B5F" stroke-width="1.6" fill="none"/>')
            body.append(f'<rect x="{x-286}" y="{y-96}" width="154" height="42" rx="10" fill="#E8F4EF" stroke="#B8DCCF"/>')
            body.append(f'<text x="{x-209}" y="{y-78}" text-anchor="middle" font-size="11" font-weight="700" fill="#20584D">Same 0/10 as v3</text>')
            body.append(f'<text x="{x-209}" y="{y-63}" text-anchor="middle" font-size="11" fill="#20584D">with lower runtime and fewer tool calls</text>')
        if arm == "research_agent_v3_planner_debate":
            body.append(f'<path d="M {x-16} {y-20} L {x-88} {y-64}" stroke="#7E97C2" stroke-width="1.4" fill="none"/>')
            body.append(f'<text x="{x-94}" y="{y-68}" text-anchor="end" font-size="11" fill="#5F7398">extra process without</text>')
            body.append(f'<text x="{x-94}" y="{y-53}" text-anchor="end" font-size="11" fill="#5F7398">extra headline gain</text>')
    body.append(f'<text x="{width-300}" y="118" font-size="11" fill="{text_mid}">bubble size = mean retrieval tool calls</text>')
    write_svg(FIGURES_DIR / "research_agent_cost_benefit.svg", width, height, body)


def make_stage_metadata_figure(ablation_rows: list[dict[str, object]]) -> None:
    if not ablation_rows:
        return
    ordered = ["baseline", "research_agent_v1", "research_agent_v2_search", "research_agent_v3_planner_debate"]
    rows = [row for arm in ordered for row in ablation_rows if str(row["arm"]) == arm]
    output_rows = []
    for row in rows:
        output_rows.append(
            {
                "arm": format_arm_label(str(row["arm"])),
                "tool_use_rate": round(float(row["tool_use_rate"]), 4),
                "retrieval_success_rate": round(float(row["retrieval_success_rate"]), 4),
                "planner_usage_rate": round(float(row["planner_usage_rate"]), 4),
                "mean_debate_rounds": round(float(row["mean_debate_rounds"]), 4),
                "mean_retrieval_tool_calls": round(float(row["mean_retrieval_tool_calls"]), 4),
            }
        )
    write_csv(
        FIGURES_DIR / "research_agent_stage_metadata.csv",
        output_rows,
        [
            "arm",
            "tool_use_rate",
            "retrieval_success_rate",
            "planner_usage_rate",
            "mean_debate_rounds",
            "mean_retrieval_tool_calls",
        ],
    )

    width, height = 1040, 430
    left, top = 38, 132
    row_h = 52
    body = [
        f'<rect x="28" y="18" width="{width-56}" height="88" rx="16" fill="#F5F8FC" stroke="#D6E1EE"/>',
        f'<text x="40" y="44" font-size="13" font-weight="700" fill="#2F6B5F">Process Evidence</text>',
        f'<text x="40" y="68" font-size="20" font-weight="700" fill="#1F2937">Retrieval drives the main gain; planner and debate mostly add process overhead.</text>',
        f'<text x="40" y="90" font-size="12" fill="#5B6472">Filled cells mark stage usage rates. Bars summarize mean rounds or retrieval calls.</text>',
    ]
    headers = ["Arm", "Tool Use", "Retrieval Success", "Planner Usage", "Debate Rounds", "Retrieval Calls"]
    col_x = [left, 176, 314, 484, 666, 844]
    col_w = [116, 112, 148, 138, 138, 138]
    for header, x, w in zip(headers, col_x, col_w):
        body.append(f'<text x="{x + w/2}" y="{top-14}" text-anchor="middle" font-size="12" font-weight="700" fill="#374151">{svg_escape(header)}</text>')
    max_calls = max(float(r["mean_retrieval_tool_calls"]) for r in output_rows) or 1.0
    max_rounds = max(float(r["mean_debate_rounds"]) for r in output_rows) or 1.0
    row_fills = {"v2": "#F4FBF8", "v3": "#F4F8FD", "Baseline": "#FFFFFF", "v1": "#FFFFFF"}
    for idx, row in enumerate(output_rows):
        y = top + idx * row_h
        arm = str(row["arm"])
        fill = row_fills.get(arm, "#FFFFFF")
        body.append(f'<line x1="{left-10}" y1="{y+34}" x2="{width-46}" y2="{y+34}" stroke="#EEF2F7"/>')
        if arm in {"v2", "v3"}:
            body.append(f'<rect x="{left-10}" y="{y-10}" width="956" height="{row_h-6}" rx="12" fill="{fill}" stroke="{"#2F6B5F" if arm=="v2" else "#7E97C2"}" stroke-width="1"/>')
        body.append(f'<text x="{col_x[0] + 8}" y="{y+23}" font-size="13" font-weight="700" fill="#1F2937">{svg_escape(arm)}</text>')
        for x, w, value in [
            (col_x[1], col_w[1], float(row["tool_use_rate"])),
            (col_x[2], col_w[2], float(row["retrieval_success_rate"])),
            (col_x[3], col_w[3], float(row["planner_usage_rate"])),
        ]:
            alpha = 0.12 + 0.72 * value
            body.append(f'<rect x="{x}" y="{y-6}" width="{w}" height="30" rx="9" fill="#2F6B5F" fill-opacity="{alpha:.2f}" stroke="#D6E4DF"/>')
            body.append(f'<text x="{x + w/2}" y="{y+15}" text-anchor="middle" font-size="12" font-weight="700" fill="#1F2937">{value:.0%}</text>')
        rounds = float(row["mean_debate_rounds"])
        rounds_w = col_w[4] * (rounds / max_rounds if max_rounds else 0.0)
        body.append(f'<rect x="{col_x[4]}" y="{y-6}" width="{col_w[4]}" height="30" rx="9" fill="#F1F5F9" stroke="#D6DEE8"/>')
        body.append(f'<rect x="{col_x[4]}" y="{y-6}" width="{rounds_w}" height="30" rx="9" fill="#7E97C2"/>')
        body.append(f'<text x="{col_x[4] + col_w[4]/2}" y="{y+15}" text-anchor="middle" font-size="12" font-weight="700" fill="#1F2937">{rounds:.1f}</text>')
        calls = float(row["mean_retrieval_tool_calls"])
        calls_w = col_w[5] * (calls / max_calls if max_calls else 0.0)
        body.append(f'<rect x="{col_x[5]}" y="{y-6}" width="{col_w[5]}" height="30" rx="9" fill="#F1F5F9" stroke="#D6DEE8"/>')
        body.append(f'<rect x="{col_x[5]}" y="{y-6}" width="{calls_w}" height="30" rx="9" fill="#2F6B5F" fill-opacity="0.88"/>')
        body.append(f'<text x="{col_x[5] + col_w[5]/2}" y="{y+15}" text-anchor="middle" font-size="12" font-weight="700" fill="#1F2937">{calls:.1f}</text>')
    write_svg(FIGURES_DIR / "research_agent_stage_metadata.svg", width, height, body)


def make_information_gradient_figure(run_level: list[dict[str, object]]) -> None:
    ordered = ["level1", "level2", "level3"]
    rows = []
    for variant in ordered:
        values = [float(r["mean_claim_score"]) for r in run_level if r["variant_id"] == variant]
        rows.append(
            {
                "variant_id": variant,
                "n_runs": len(values),
                "mean_run_score": round(mean(values), 4),
            }
        )
    csv_path = FIGURES_DIR / "information_gradient_scores.csv"
    write_csv(csv_path, rows, ["variant_id", "n_runs", "mean_run_score"])

    width, height = 640, 420
    margin_left, margin_bottom, margin_top = 70, 60, 50
    plot_w, plot_h = width - margin_left - 40, height - margin_bottom - margin_top
    colors = ["#2F6B5F", "#D8893A"]
    body = [
        f'<text x="{width/2}" y="28" text-anchor="middle" font-size="20">Information Gradient: Level 1 vs Level 2 vs Level 3</text>',
        f'<line x1="{margin_left}" y1="{height-margin_bottom}" x2="{width-20}" y2="{height-margin_bottom}" stroke="#222"/>',
        f'<line x1="{margin_left}" y1="{margin_top}" x2="{margin_left}" y2="{height-margin_bottom}" stroke="#222"/>',
        f'<text x="20" y="{margin_top + plot_h/2}" transform="rotate(-90 20 {margin_top + plot_h/2})" text-anchor="middle" font-size="13">Mean Run Score</text>',
    ]
    for tick in range(6):
        y_val = tick / 5
        y = height - margin_bottom - plot_h * y_val
        body.append(f'<line x1="{margin_left-5}" y1="{y}" x2="{margin_left}" y2="{y}" stroke="#222"/>')
        body.append(f'<text x="{margin_left-10}" y="{y+4}" text-anchor="end" font-size="11">{y_val:.1f}</text>')
    bar_w = plot_w / (len(rows) * 2)
    for i, row in enumerate(rows):
        score = float(row["mean_run_score"])
        x = margin_left + (2 * i + 0.75) * bar_w
        h = plot_h * score
        y = height - margin_bottom - h
        body.append(f'<rect x="{x}" y="{y}" width="{bar_w}" height="{h}" fill="{colors[i % len(colors)]}"/>')
        body.append(f'<text x="{x + bar_w/2}" y="{height-margin_bottom+20}" text-anchor="middle" font-size="12">{svg_escape(row["variant_id"])}</text>')
        body.append(f'<text x="{x + bar_w/2}" y="{y-8}" text-anchor="middle" font-size="12">{score:.2f}</text>')
    write_svg(FIGURES_DIR / "information_gradient_scores.svg", width, height, body)


def make_error_type_figure(error_rows: list[dict[str, object]]) -> None:
    csv_path = FIGURES_DIR / "error_type_distribution.csv"
    write_csv(csv_path, error_rows, ["error_type", "count", "rate"])

    rows = [r for r in error_rows if r["error_type"] != "none"]
    width, height = 720, 420
    margin_left, margin_bottom, margin_top = 70, 80, 50
    plot_w, plot_h = width - margin_left - 40, height - margin_bottom - margin_top
    max_count = max(int(r["count"]) for r in rows) if rows else 1
    colors = ["#B65E5E", "#4F8BC9", "#8A5FBF"]
    body = [
        f'<text x="{width/2}" y="28" text-anchor="middle" font-size="20">Error Type Distribution</text>',
        f'<line x1="{margin_left}" y1="{height-margin_bottom}" x2="{width-20}" y2="{height-margin_bottom}" stroke="#222"/>',
        f'<line x1="{margin_left}" y1="{margin_top}" x2="{margin_left}" y2="{height-margin_bottom}" stroke="#222"/>',
    ]
    for tick in range(6):
        val = round(max_count * tick / 5)
        y = height - margin_bottom - plot_h * (val / max_count if max_count else 0)
        body.append(f'<line x1="{margin_left-5}" y1="{y}" x2="{margin_left}" y2="{y}" stroke="#222"/>')
        body.append(f'<text x="{margin_left-10}" y="{y+4}" text-anchor="end" font-size="11">{val}</text>')
    bar_w = plot_w / (len(rows) * 2)
    for i, row in enumerate(rows):
        count = int(row["count"])
        x = margin_left + (2 * i + 0.75) * bar_w
        h = plot_h * (count / max_count if max_count else 0)
        y = height - margin_bottom - h
        body.append(f'<rect x="{x}" y="{y}" width="{bar_w}" height="{h}" fill="{colors[i % len(colors)]}"/>')
        body.append(f'<text x="{x + bar_w/2}" y="{height-margin_bottom+32}" text-anchor="middle" font-size="12">{svg_escape(row["error_type"])}</text>')
        body.append(f'<text x="{x + bar_w/2}" y="{y-8}" text-anchor="middle" font-size="12">{count}</text>')
    write_svg(FIGURES_DIR / "error_type_distribution.svg", width, height, body)


def make_error_type_by_agent_variant_figure(error_rows: list[dict[str, object]]) -> None:
    write_csv(
        FIGURES_DIR / "error_type_by_agent_variant.csv",
        error_rows,
        ["agent_variant", "error_type", "count", "rate", "n_claims"],
    )

    rows = [r for r in error_rows if r["error_type"] != "none"]
    variants = [
        DEFAULT_AGENT_VARIANT,
        "research_agent_v1",
        "research_agent_v2_search",
        "research_agent_v3_planner_debate",
    ]
    labels = {
        DEFAULT_AGENT_VARIANT: "Baseline",
        "research_agent_v1": "v1",
        "research_agent_v2_search": "v2",
        "research_agent_v3_planner_debate": "v3",
    }
    error_types = ["Overclaim", "Unsupported Claim", "Contradiction"]
    counts_by_key = {
        (str(row["agent_variant"]), str(row["error_type"])): int(row["count"]) for row in rows
    }
    max_rate = max((float(row["rate"]) for row in rows), default=0.15)
    max_rate = max(max_rate, 0.15)
    width, height = 1040, 540
    margin_left, margin_bottom, margin_top = 92, 94, 144
    plot_w, plot_h = width - margin_left - 90, height - margin_bottom - margin_top
    group_w = plot_w / len(error_types)
    bar_w = group_w / (len(variants) + 1)
    colors = {
        DEFAULT_AGENT_VARIANT: "#7B4651",
        "research_agent_v1": "#C78B47",
        "research_agent_v2_search": "#2F6B5F",
        "research_agent_v3_planner_debate": "#7E97C2",
    }
    body = [
        f'<rect x="28" y="18" width="{width-56}" height="86" rx="16" fill="#F8F4F4" stroke="#E7DADB"/>',
        f'<text x="40" y="44" font-size="13" font-weight="700" fill="{colors["research_agent_v2_search"]}">Claim-Level Pattern</text>',
        f'<text x="40" y="68" font-size="24" font-weight="700" fill="#1F2937">The baseline arm carries nearly all claim-level errors.</text>',
        f'<text x="40" y="90" font-size="12" fill="#5B6472">Rates are shown on the y-axis; raw counts are printed above each bar. Intervention arms remain at zero across these error classes.</text>',
        f'<line x1="{margin_left}" y1="{height-margin_bottom}" x2="{width-26}" y2="{height-margin_bottom}" stroke="#1F2937" stroke-width="1.4"/>',
        f'<line x1="{margin_left}" y1="{margin_top}" x2="{margin_left}" y2="{height-margin_bottom}" stroke="#1F2937" stroke-width="1.4"/>',
        f'<text x="28" y="{margin_top + plot_h/2}" transform="rotate(-90 28 {margin_top + plot_h/2})" text-anchor="middle" font-size="13" fill="#1F2937">Error Rate Among Claims</text>',
    ]
    for tick in range(6):
        val = max_rate * tick / 5
        y = height - margin_bottom - plot_h * (val / max_rate if max_rate else 0)
        body.append(f'<line x1="{margin_left}" y1="{y}" x2="{width-26}" y2="{y}" stroke="#D9DEE7" stroke-width="1"/>')
        body.append(f'<text x="{margin_left-10}" y="{y+4}" text-anchor="end" font-size="11" fill="#5B6472">{val:.0%}</text>')

    for error_index, error_type in enumerate(error_types):
        group_left = margin_left + error_index * group_w
        body.append(
            f'<text x="{group_left + group_w/2}" y="{height-margin_bottom+30}" text-anchor="middle" font-size="12" font-weight="700" fill="#374151">{svg_escape(error_type)}</text>'
        )
        for variant_index, agent_variant in enumerate(variants):
            count = counts_by_key.get((agent_variant, error_type), 0)
            matching = next((r for r in rows if str(r["agent_variant"]) == agent_variant and str(r["error_type"]) == error_type), None)
            rate_value = float(matching["rate"]) if matching else 0.0
            x = group_left + (variant_index + 0.5) * bar_w
            h = plot_h * (rate_value / max_rate if max_rate else 0)
            y = height - margin_bottom - h
            if agent_variant == DEFAULT_AGENT_VARIANT:
                body.append(f'<rect x="{x-6}" y="{margin_top-10}" width="{bar_w*0.8+12}" height="{plot_h+18}" rx="10" fill="#FCF7F7"/>')
            body.append(
                f'<rect x="{x}" y="{height-margin_bottom-max(h, 3)}" width="{bar_w*0.8}" height="{max(h, 3)}" rx="8" fill="{colors[agent_variant]}" fill-opacity="0.95"/>'
            )
            body.append(
                f'<text x="{x + bar_w*0.4}" y="{max(y-20, margin_top-10)}" text-anchor="middle" font-size="12" font-weight="700" fill="{colors[agent_variant]}">{rate_value:.0%}</text>'
            )
            body.append(
                f'<text x="{x + bar_w*0.4}" y="{max(y-5, margin_top+9)}" text-anchor="middle" font-size="10" fill="#5B6472">n={count}</text>'
            )

    legend_x = width - 208
    legend_y = 116
    for idx, agent_variant in enumerate(variants):
        y = legend_y + idx * 20
        body.append(f'<rect x="{legend_x}" y="{y}" width="12" height="12" fill="{colors[agent_variant]}"/>')
        body.append(f'<text x="{legend_x + 20}" y="{y + 11}" font-size="12" fill="#374151">{labels[agent_variant]}</text>')
    write_svg(FIGURES_DIR / "error_type_by_agent_variant.svg", width, height, body)


def make_case_error_heatmap(rows: list[dict[str, object]]) -> None:
    cases = sorted({str(r["case_id"]) for r in rows})
    error_types = ["Overclaim", "Unsupported Claim", "Contradiction"]
    matrix_rows = []
    matrix = []
    for case in cases:
        subset = [r for r in rows if r["case_id"] == case]
        n = len(subset)
        rates = [rate(sum(r["final_error_type"] == et for r in subset), n) for et in error_types]
        matrix_rows.append({"case_id": case, **{et: round(val, 4) for et, val in zip(error_types, rates)}})
        matrix.append(rates)
    write_csv(FIGURES_DIR / "case_error_heatmap.csv", matrix_rows, ["case_id"] + error_types)

    width, height = 720, 460
    left, top = 130, 70
    cell_w, cell_h = 150, 28
    vmax = max(max(row) for row in matrix) if matrix else 1
    body = [f'<text x="{width/2}" y="28" text-anchor="middle" font-size="20">Case-by-Error-Type Rate</text>']
    for j, et in enumerate(error_types):
        x = left + j * cell_w + cell_w / 2
        body.append(f'<text x="{x}" y="{top-14}" text-anchor="middle" font-size="12">{svg_escape(et)}</text>')
    for i, case in enumerate(cases):
        y = top + i * cell_h
        body.append(f'<text x="{left-10}" y="{y + cell_h*0.65}" text-anchor="end" font-size="12">{case}</text>')
        for j, value in enumerate(matrix[i]):
            x = left + j * cell_w
            intensity = 255 - int(180 * (value / vmax if vmax else 0))
            fill = f"rgb(255,{intensity},{max(0, intensity-40)})"
            body.append(f'<rect x="{x}" y="{y}" width="{cell_w-2}" height="{cell_h-2}" fill="{fill}" stroke="#ffffff"/>')
            body.append(f'<text x="{x + (cell_w-2)/2}" y="{y + cell_h*0.65}" text-anchor="middle" font-size="11">{value:.2f}</text>')
    write_svg(FIGURES_DIR / "case_error_heatmap.svg", width, height, body)


def make_perturbed_downgrade_figure(run_level: list[dict[str, object]]) -> None:
    level3 = {r["case_id"]: float(r["mean_claim_score"]) for r in run_level if r["variant_id"] == "level3"}
    perturbed = {r["case_id"]: float(r["mean_claim_score"]) for r in run_level if r["variant_id"] == "perturbed"}
    rows = []
    for case_id in sorted(set(level3) & set(perturbed)):
        rows.append(
            {
                "case_id": case_id,
                "level3_mean_run_score": round(level3[case_id], 4),
                "perturbed_mean_run_score": round(perturbed[case_id], 4),
                "delta_perturbed_minus_level3": round(perturbed[case_id] - level3[case_id], 4),
            }
        )
    write_csv(
        FIGURES_DIR / "perturbed_downgrade.csv",
        rows,
        ["case_id", "level3_mean_run_score", "perturbed_mean_run_score", "delta_perturbed_minus_level3"],
    )

    width, height = 860, 460
    margin_left, margin_bottom, margin_top = 70, 80, 50
    plot_w, plot_h = width - margin_left - 30, height - margin_bottom - margin_top
    body = [
        f'<text x="{width/2}" y="28" text-anchor="middle" font-size="20">Design Downgrade Under Perturbation</text>',
        f'<line x1="{margin_left}" y1="{height-margin_bottom}" x2="{width-20}" y2="{height-margin_bottom}" stroke="#222"/>',
        f'<line x1="{margin_left}" y1="{margin_top}" x2="{margin_left}" y2="{height-margin_bottom}" stroke="#222"/>',
    ]
    for tick in range(6):
        y_val = tick / 5
        y = height - margin_bottom - plot_h * y_val
        body.append(f'<line x1="{margin_left-5}" y1="{y}" x2="{margin_left}" y2="{y}" stroke="#222"/>')
        body.append(f'<text x="{margin_left-10}" y="{y+4}" text-anchor="end" font-size="11">{y_val:.1f}</text>')

    def point(i: int, score: float) -> tuple[float, float]:
        if len(rows) == 1:
            x = margin_left + plot_w / 2
        else:
            x = margin_left + plot_w * i / (len(rows) - 1)
        y = height - margin_bottom - plot_h * score
        return x, y

    level3_points = [point(i, float(r["level3_mean_run_score"])) for i, r in enumerate(rows)]
    pert_points = [point(i, float(r["perturbed_mean_run_score"])) for i, r in enumerate(rows)]
    body.append(
        '<polyline fill="none" stroke="#2F6B5F" stroke-width="2" points="{}"/>'.format(
            " ".join(f"{x},{y}" for x, y in level3_points)
        )
    )
    body.append(
        '<polyline fill="none" stroke="#B65E5E" stroke-width="2" points="{}"/>'.format(
            " ".join(f"{x},{y}" for x, y in pert_points)
        )
    )
    for i, row in enumerate(rows):
        x, y1 = level3_points[i]
        _, y2 = pert_points[i]
        body.append(f'<circle cx="{x}" cy="{y1}" r="4" fill="#2F6B5F"/>')
        body.append(f'<circle cx="{x}" cy="{y2}" r="4" fill="#B65E5E"/>')
        body.append(f'<text x="{x}" y="{height-margin_bottom+24}" text-anchor="middle" font-size="11">{row["case_id"]}</text>')
    body.append(f'<rect x="{width-180}" y="52" width="12" height="12" fill="#2F6B5F"/>')
    body.append(f'<text x="{width-160}" y="63" font-size="12">level3</text>')
    body.append(f'<rect x="{width-110}" y="52" width="12" height="12" fill="#B65E5E"/>')
    body.append(f'<text x="{width-90}" y="63" font-size="12">perturbed</text>')
    write_svg(FIGURES_DIR / "perturbed_downgrade.svg", width, height, body)


def write_metrics_markdown(
    metrics_rows: list[dict[str, object]],
    output_path: Path,
    agent_variant: str,
) -> None:
    if agent_variant == DEFAULT_AGENT_VARIANT:
        intro = (
            "Canonical metrics are derived from `annotations/adjudicated_labels.csv` filtered to "
            f"`agent_variant == \"{DEFAULT_AGENT_VARIANT}\"`, with main-run execution counts cross-checked against `outputs/run_manifest.csv`."
        )
    else:
        intro = (
            "Research-agent metrics are derived from `annotations/adjudicated_labels.csv` filtered to "
            f"`agent_variant == \"{agent_variant}\"`, with main-run execution counts cross-checked against `outputs/run_manifest.csv`."
        )
    lines = [
        "# Metrics Summary",
        "",
        intro,
        "",
        "## Counting Rules",
        "",
        "- Claim-level metrics use claims as the denominator.",
        "- Run-level metrics use successful annotated runs as the denominator unless the metric explicitly references all main-manifest rows.",
        "- Main-run rows are identified by `raw_output_file` paths under `outputs/raw_agent_logs/main/`.",
        f"- This file summarizes only rows with `agent_variant == \"{agent_variant}\"`.",
        "- After Task 26, information-gradient reporting should be interpreted across `level1`, `level2`, and `level3` together rather than from a single adjacent pair.",
        "- `Critical Design Omission Rate` and `Mechanism Confounding Rate` are reported as proxies because the current annotation schema does not contain explicit omission-only or mechanism-only tags.",
        "",
    ]
    if agent_variant == DEFAULT_AGENT_VARIANT:
        lines.extend(
            [
                "## Bottleneck Crosswalk",
                "",
                "This benchmark is best interpreted as a focused execution-quality probe rather than a full reproduction of *The Ideation Bottleneck* six-dimension rubric. The detailed mapping from Bottleneck dimensions to benchmark evidence is documented in [results/bottleneck_crosswalk.md](/Users/jiangcanxiang/Documents/OOD_Problem/results/bottleneck_crosswalk.md).",
                "",
                "The short version is:",
                "",
                "- `Identification Strategy` and `Mechanism and External Validity` are the benchmark's strongest direct measurement areas.",
                "- `Econometric Methodology` and `Data Quality` are only partially proxied through claim-level errors and selected failure cases.",
                "- `Robustness and Sensitivity` and `Writing and Presentation` are intentionally secondary in this benchmark.",
                "",
            ]
        )
    lines.extend(
        [
            "## Metrics",
            "",
            "| Metric | Scope | Value | Formula | Notes |",
            "|---|---|---:|---|---|",
        ]
    )
    for row in metrics_rows:
        lines.append(
            f"| {row['metric']} | {row['scope']} | {row['value']} | {row['formula']} | {row['notes']} |"
        )
    output_path.write_text("\n".join(lines) + "\n")


def main() -> None:
    RESULTS_DIR.mkdir(parents=True, exist_ok=True)
    FIGURES_DIR.mkdir(parents=True, exist_ok=True)

    metadata = load_metadata()
    labels_all = annotate_labels(read_csv(LABELS_CSV), metadata)
    manifest_rows_all = load_main_manifest()
    run_level_all = build_run_level(labels_all)

    baseline_labels = filter_by_agent_variant(labels_all, DEFAULT_AGENT_VARIANT)
    baseline_manifest_rows = filter_by_agent_variant(manifest_rows_all, DEFAULT_AGENT_VARIANT)
    baseline_perturbed_audit_rows = load_perturbed_audit(DEFAULT_AGENT_VARIANT)
    baseline_run_level = build_run_level(baseline_labels)
    case_level = build_case_level(baseline_labels)
    error_counts = build_error_counts(baseline_labels)
    error_counts_by_variant = build_error_counts_by_agent_variant(labels_all)
    grouped_metrics = build_grouped_metrics(labels_all, run_level_all)
    metrics_rows = compute_metrics(
        baseline_labels,
        baseline_run_level,
        baseline_manifest_rows,
        baseline_perturbed_audit_rows,
    )

    write_csv(
        METRICS_SUMMARY_CSV,
        metrics_rows,
        ["metric", "scope", "numerator", "denominator", "value", "formula", "notes"],
    )
    write_csv(ERROR_COUNTS_CSV, error_counts, ["error_type", "count", "rate"])
    write_csv(
        ERROR_COUNTS_BY_VARIANT_CSV,
        error_counts_by_variant,
        ["agent_variant", "error_type", "count", "rate", "n_claims"],
    )
    write_csv(
        CASE_LEVEL_CSV,
        case_level,
        [
            "case_id",
            "domain",
            "design_family",
            "key_failure_mode",
            "variant_id",
            "n_claims",
            "mean_claim_score",
            "supported_rate",
            "partial_rate",
            "unsupported_rate",
            "contradicted_rate",
            "inconsistency_rate",
            "critical_issue_rate",
            "level",
        ],
    )
    write_csv(
        RUN_LEVEL_CSV,
        baseline_run_level,
        [
            "run_id",
            "case_id",
            "variant_id",
            "agent_variant",
            "domain",
            "design_family",
            "key_failure_mode",
            "n_claims",
            "mean_claim_score",
            "supported_rate",
            "partial_rate",
            "unsupported_rate",
            "contradicted_rate",
            "inconsistency_rate",
            "critical_issue_rate",
            "supported_causal_claims",
            "no_solution_honest",
        ],
    )
    write_csv(
        GROUPED_CSV,
        grouped_metrics,
        ["group_type", "group_value", "scope", "n_units", "mean_claim_score", "inconsistency_rate", "critical_issue_rate"],
    )

    make_information_gradient_figure(baseline_run_level)
    make_error_type_figure(error_counts)
    make_error_type_by_agent_variant_figure(error_counts_by_variant)
    make_case_error_heatmap(baseline_labels)
    make_perturbed_downgrade_figure(baseline_run_level)
    ablation_rows = load_ablation_summary()
    make_ablation_ladder_figure(ablation_rows)
    make_cost_benefit_figure(ablation_rows)
    make_stage_metadata_figure(ablation_rows)
    write_metrics_markdown(metrics_rows, METRICS_SUMMARY_MD, DEFAULT_AGENT_VARIANT)

    other_variants = sorted(
        {
            str(row["agent_variant"])
            for row in labels_all
            if str(row["agent_variant"]) != DEFAULT_AGENT_VARIANT
        }
    )
    for agent_variant in other_variants:
        variant_labels = filter_by_agent_variant(labels_all, agent_variant)
        variant_manifest_rows = filter_by_agent_variant(manifest_rows_all, agent_variant)
        variant_run_level = build_run_level(variant_labels)
        variant_perturbed_audit_rows = load_perturbed_audit(agent_variant)
        variant_metrics_rows = compute_metrics(
            variant_labels,
            variant_run_level,
            variant_manifest_rows,
            variant_perturbed_audit_rows,
        )
        summary_csv, summary_md = research_metrics_summary_paths(agent_variant)
        write_csv(
            summary_csv,
            variant_metrics_rows,
            ["metric", "scope", "numerator", "denominator", "value", "formula", "notes"],
        )
        write_metrics_markdown(variant_metrics_rows, summary_md, agent_variant)


if __name__ == "__main__":
    main()
