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
CASE_LEVEL_CSV = RESULTS_DIR / "case_level_scores.csv"
RUN_LEVEL_CSV = RESULTS_DIR / "run_level_scores.csv"
GROUPED_CSV = RESULTS_DIR / "grouped_metrics.csv"
PERTURBED_AUDIT_CSV = RESULTS_DIR / "perturbed_mechanical_reuse.csv"
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
    make_case_error_heatmap(baseline_labels)
    make_perturbed_downgrade_figure(baseline_run_level)
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
