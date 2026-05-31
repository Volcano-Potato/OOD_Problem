#!/usr/bin/env python3

import csv
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "outputs" / "run_manifest.csv"
OUTPUT_DIR = ROOT / "outputs" / "parsed_claims"
CLAIMS_CSV = OUTPUT_DIR / "claims_to_annotate.csv"
SKIPPED_CSV = OUTPUT_DIR / "claim_extraction_skipped.csv"
SUMMARY_MD = OUTPUT_DIR / "claim_extraction_summary.md"
DEFAULT_AGENT_VARIANT = "benchmark_isolated"


def normalize_header(text: str) -> str:
    cleaned = re.sub(r"[^a-z0-9]+", "_", text.lower()).strip("_")
    aliases = {
        "claim": "claim",
        "evidence_used": "evidence_used",
        "claim_type": "claim_type",
        "confidence": "confidence",
        "what_would_falsify_this_claim": "what_would_falsify_this_claim",
        "what_would_falsify": "what_would_falsify_this_claim",
        "#": "row_number",
    }
    return aliases.get(cleaned, cleaned)


def split_table_row(line: str) -> list[str]:
    return [cell.strip() for cell in line.strip().strip("|").split("|")]


def clean_claim_text(text: str) -> str:
    cleaned = text.replace("**", "").replace("`", "").replace("<br>", " ")
    cleaned = re.sub(r"^C\d+\s*:\s*", "", cleaned)
    cleaned = re.sub(r"^\d+[\.\)]\s*", "", cleaned)
    cleaned = re.sub(r"\s+", " ", cleaned).strip()
    return cleaned


def parse_claim_table(raw_text: str) -> list[dict[str, str]]:
    lines = raw_text.splitlines()
    header_idx = None
    for idx, line in enumerate(lines):
        if line.startswith("|") and "Claim" in line and "Evidence Used" in line and "Claim Type" in line:
            header_idx = idx
    if header_idx is None:
        return []

    header_cells = split_table_row(lines[header_idx])
    normalized = [normalize_header(cell) for cell in header_cells]
    rows = []
    for line in lines[header_idx + 1 :]:
        if not line.startswith("|"):
            break
        if set(line.replace("|", "").replace("-", "").replace(":", "").strip()) == set():
            continue
        cells = split_table_row(line)
        if len(cells) != len(normalized):
            continue
        row = dict(zip(normalized, cells))
        if row.get("claim", "").lower() == "claim":
            continue
        rows.append(row)
    return rows


def load_success_main_rows() -> list[dict[str, str]]:
    rows = []
    with MANIFEST.open(newline="") as handle:
        reader = csv.DictReader(handle)
        for row in reader:
            if row.get("status") != "success":
                continue
            if "/main/" not in row.get("raw_output_file", ""):
                continue
            row["agent_variant"] = row.get("agent_variant", "") or DEFAULT_AGENT_VARIANT
            rows.append(row)
    return rows


def main() -> None:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    manifest_rows = load_success_main_rows()
    claim_rows = []
    skipped_rows = []
    per_run_counts = {}

    for row in manifest_rows:
        raw_path = ROOT / row["raw_output_file"]
        raw_text = raw_path.read_text()
        parsed_claims = parse_claim_table(raw_text)
        if not parsed_claims:
            skipped_rows.append(
                {
                    "run_id": row["run_id"],
                    "case_id": row["case_id"],
                    "variant_id": row["variant_id"],
                    "reason": "claim_evidence_table_not_found",
                    "raw_output_file": row["raw_output_file"],
                }
            )
            continue

        per_run_counts[row["run_id"]] = len(parsed_claims)
        for idx, claim in enumerate(parsed_claims, start=1):
            raw_claim = claim.get("claim", "").strip()
            claim_rows.append(
                {
                    "case_id": row["case_id"],
                    "variant_id": row["variant_id"],
                    "level": row["level"],
                    "agent_variant": row["agent_variant"],
                    "run_id": row["run_id"],
                    "claim_id": f"{row['run_id']}_CL{idx:03d}",
                    "claim_type": claim.get("claim_type", "").strip(),
                    "agent_claim": clean_claim_text(raw_claim),
                    "cited_evidence": claim.get("evidence_used", "").strip(),
                    "confidence": claim.get("confidence", "").strip(),
                    "what_would_falsify_this_claim": claim.get("what_would_falsify_this_claim", "").strip(),
                    "verbatim_quote": raw_claim,
                    "source_section": "Claim-Evidence Table",
                    "raw_output_file": row["raw_output_file"],
                    "notes": "extracted_from_claim_evidence_table",
                }
            )

    claim_fieldnames = [
        "case_id",
        "variant_id",
        "level",
        "agent_variant",
        "run_id",
        "claim_id",
        "claim_type",
        "agent_claim",
        "cited_evidence",
        "confidence",
        "what_would_falsify_this_claim",
        "verbatim_quote",
        "source_section",
        "raw_output_file",
        "notes",
    ]
    with CLAIMS_CSV.open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=claim_fieldnames, lineterminator="\n")
        writer.writeheader()
        writer.writerows(claim_rows)

    skipped_fieldnames = ["run_id", "case_id", "variant_id", "reason", "raw_output_file"]
    with SKIPPED_CSV.open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=skipped_fieldnames, lineterminator="\n")
        writer.writeheader()
        writer.writerows(skipped_rows)

    min_claims = min(per_run_counts.values()) if per_run_counts else 0
    max_claims = max(per_run_counts.values()) if per_run_counts else 0
    with SUMMARY_MD.open("w") as handle:
        handle.write("# Claim Extraction Summary\n\n")
        handle.write(f"- Successful main runs processed: `{len(manifest_rows)}`\n")
        handle.write(f"- Runs with extracted claim tables: `{len(per_run_counts)}`\n")
        handle.write(f"- Runs skipped: `{len(skipped_rows)}`\n")
        handle.write(f"- Total extracted claims: `{len(claim_rows)}`\n")
        handle.write(f"- Minimum claims per run: `{min_claims}`\n")
        handle.write(f"- Maximum claims per run: `{max_claims}`\n")


if __name__ == "__main__":
    main()
