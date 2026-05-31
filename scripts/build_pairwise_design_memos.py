#!/usr/bin/env python3

import csv
import re
from pathlib import Path


REPO_ROOT = Path("/Users/jiangcanxiang/Documents/OOD_Problem")
OUT_DIR = REPO_ROOT / "outputs" / "pairwise_design_memos"
SPEC_PATH = REPO_ROOT / "benchmark" / "run_configs" / "main_run_batch_spec.csv"

CASE_DIRS = {
    "C001": "C001_charitable_giving",
    "C002": "C002_consumer_credit",
    "C004": "C004_paid_search_effectiveness",
    "C005": "C005_online_ad_measurement",
    "C008": "C008_retail_tax_salience",
    "C010": "C010_fertilizer_present_bias",
    "C014": "C014_corruption_monitoring",
    "C016": "C016_hiv_risk_information",
    "C019": "C019_in_store_travel_distance",
    "C020": "C020_price_ending_field_experiment",
}


def read_text(path: Path) -> str:
    return path.read_text()


def strip_md(text: str) -> str:
    text = re.sub(r"`([^`]*)`", r"\1", text)
    text = re.sub(r"\[(.*?)\]\(.*?\)", r"\1", text)
    text = re.sub(r"\*\*(.*?)\*\*", r"\1", text)
    text = re.sub(r"\*(.*?)\*", r"\1", text)
    return text.strip()


def section_block(text: str, header: str) -> str:
    pattern = rf"^## {re.escape(header)}\n(.*?)(?=^## |\Z)"
    match = re.search(pattern, text, flags=re.M | re.S)
    return match.group(1).strip() if match else ""


def bullet_lines(text: str) -> list[str]:
    lines = []
    for line in text.splitlines():
        line = line.strip()
        if line.startswith("- "):
            lines.append(strip_md(line[2:].strip()))
    return lines


def sentence_compact(text: str, max_chars: int = 700) -> str:
    text = strip_md(text)
    text = re.sub(r"\s+", " ", text).strip()
    return text[:max_chars].rstrip()


def table_rows(text: str) -> list[list[str]]:
    rows = []
    for line in text.splitlines():
        line = line.strip()
        if not (line.startswith("|") and line.endswith("|")):
            continue
        cells = [strip_md(cell.strip()) for cell in line.strip("|").split("|")]
        if not cells:
            continue
        if all(set(cell) <= {"-"} for cell in cells):
            continue
        if cells[0].lower() in {"design", "design or claim", "field", "fact_id", "failure_id", "expected claim"}:
            continue
        rows.append(cells)
    return rows


def build_published_memo(gold_text: str) -> str:
    problem = bullet_lines(section_block(gold_text, "Core Research Problem"))
    data_structure = bullet_lines(section_block(gold_text, "Data Structure"))
    identification = sentence_compact(section_block(gold_text, "Original Identification Logic"), 900)
    linchpin = bullet_lines(section_block(gold_text, "Linchpin Detail"))
    must_have = bullet_lines(section_block(gold_text, "Must-Have Conditions"))
    invalid_rows = table_rows(section_block(gold_text, "Common Invalid Designs"))

    proposed_design_lines = []
    if len(problem) > 3:
        proposed_design_lines.extend(problem[3:6])
    if len(data_structure) > 4:
        proposed_design_lines.extend(data_structure[4:6])
    proposed_design_lines.extend(must_have[:4])
    proposed_design_lines = proposed_design_lines[:7]

    defensibility_bits = []
    if linchpin:
        defensibility_bits.append(linchpin[0])
    if len(linchpin) > 1:
        defensibility_bits.append(linchpin[1])
    defensibility_bits.extend(must_have[:2])
    defensibility_assessment = " ".join(defensibility_bits)
    defensibility_assessment = re.sub(r"\s+", " ", defensibility_assessment).strip()

    invalid_lines = []
    for row in invalid_rows[:4]:
        if len(row) >= 2:
            invalid_lines.append(f"{row[0]} Why invalid: {row[1]}")

    parts = [
        "# Published Design Memo",
        "",
        "## Research Question",
        problem[0] if len(problem) > 0 else "",
        "",
        "## Target Estimand",
        problem[2] if len(problem) > 2 else "",
        "",
        "## Treatment And Outcomes",
        "\n".join(f"- {line}" for line in problem[3:6]),
        "",
        "## Identification Logic",
        identification,
        "",
        "## Key Data Structure",
        "\n".join(f"- {line}" for line in data_structure[:6]),
        "",
        "## Linchpin Conditions",
        "\n".join(f"- {line}" for line in linchpin[:4] + must_have[:4]),
        "",
        "## Defensibility Assessment",
        defensibility_assessment,
        "",
        "## Proposed Design",
        "\n".join(f"- {line}" for line in proposed_design_lines),
        "",
        "## What Cannot Be Claimed Or Omitted",
        "\n".join(f"- {line}" for line in invalid_lines),
    ]
    return "\n".join(part for part in parts if part is not None).strip() + "\n"


def extract_raw_agent_output(text: str) -> str:
    marker = "## Raw Agent Output"
    idx = text.find(marker)
    if idx == -1:
        return text
    return text[idx + len(marker):].strip()


def agent_section(text: str, title_regex: str) -> str:
    pattern = rf"^##\s+\d+\.\s+{title_regex}\n(.*?)(?=^##\s+\d+\. |\Z)"
    match = re.search(pattern, text, flags=re.M | re.S)
    return match.group(1).strip() if match else ""


def build_agent_memo(raw_log_text: str) -> str:
    agent_text = extract_raw_agent_output(raw_log_text)
    rq = sentence_compact(agent_section(agent_text, r"Research Question"), 700)
    estimand = sentence_compact(agent_section(agent_text, r"Target Estimand \(or Strongest Defensible Estimand\)"), 900)
    treatment = sentence_compact(agent_section(agent_text, r"Treatment or Exposure and Main Outcomes"), 1100)
    ident = sentence_compact(agent_section(agent_text, r"Main Identification Challenge"), 900)
    validity = sentence_compact(agent_section(agent_text, r"Whether Credible Causal Identification Is Possible"), 900)
    design = sentence_compact(agent_section(agent_text, r"Proposed Empirical Design(?: or Strongest Defensible Descriptive Analysis)?"), 1300)
    cannot = sentence_compact(agent_section(agent_text, r"What Cannot Be Claimed"), 900)

    parts = [
        "# Agent Design Memo",
        "",
        "## Research Question",
        rq,
        "",
        "## Target Estimand",
        estimand,
        "",
        "## Treatment And Outcomes",
        treatment,
        "",
        "## Identification Logic",
        ident,
        "",
        "## Defensibility Assessment",
        validity,
        "",
        "## Proposed Design",
        design,
        "",
        "## What Cannot Be Claimed",
        cannot,
    ]
    return "\n".join(part for part in parts if part is not None).strip() + "\n"


def level2_cases() -> list[str]:
    cases = []
    with SPEC_PATH.open(newline="") as fh:
        reader = csv.DictReader(fh)
        for row in reader:
            if row["variant_id"] == "level2" and row["enabled"].strip().lower() == "true":
                cases.append(row["case_id"])
    return cases


def main():
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    manifest_rows = []
    for case_id in level2_cases():
        case_dir = REPO_ROOT / "benchmark" / "cases" / CASE_DIRS[case_id]
        gold_path = case_dir / "gold_reference.md"
        log_candidates = sorted((REPO_ROOT / "outputs" / "raw_agent_logs" / "main").glob(f"{case_id}_level2_openclaw_*.md"))
        if not log_candidates:
            raise SystemExit(f"Missing level2 raw log for {case_id}")
        raw_log_path = log_candidates[-1]

        published_memo = build_published_memo(read_text(gold_path))
        agent_memo = build_agent_memo(read_text(raw_log_path))

        pub_out = OUT_DIR / f"{case_id}_published_design_memo.md"
        agent_out = OUT_DIR / f"{case_id}_agent_design_memo.md"
        pub_out.write_text(published_memo)
        agent_out.write_text(agent_memo)

        manifest_rows.append(
            {
                "case_id": case_id,
                "published_memo_file": str(pub_out.relative_to(REPO_ROOT)),
                "agent_memo_file": str(agent_out.relative_to(REPO_ROOT)),
                "source_gold_reference": str(gold_path.relative_to(REPO_ROOT)),
                "source_agent_log": str(raw_log_path.relative_to(REPO_ROOT)),
            }
        )

    index_path = OUT_DIR / "memo_index.csv"
    with index_path.open("w", newline="") as fh:
        writer = csv.DictWriter(
            fh,
            fieldnames=[
                "case_id",
                "published_memo_file",
                "agent_memo_file",
                "source_gold_reference",
                "source_agent_log",
            ],
        )
        writer.writeheader()
        writer.writerows(manifest_rows)

    print(f"Wrote {len(manifest_rows)} pairwise memo pairs to {OUT_DIR}")


if __name__ == "__main__":
    main()
