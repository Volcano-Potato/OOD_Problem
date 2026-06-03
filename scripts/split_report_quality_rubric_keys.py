from __future__ import annotations

import csv
import re
from dataclasses import dataclass
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
MASTER_PATH = REPO_ROOT / "results" / "report_quality_rubric_keys.md"
AXIS_A_INDEX_PATH = REPO_ROOT / "outputs" / "report_quality_judge_packets" / "axis_a_report_index.csv"
AXIS_B_INDEX_PATH = REPO_ROOT / "outputs" / "report_quality_judge_packets" / "axis_b_report_index.csv"
OUTPUT_ROOT = REPO_ROOT / "outputs" / "report_quality_judge_packets" / "rubric_keys"
AXIS_A_OUTPUT_DIR = OUTPUT_ROOT / "axis_a"
AXIS_B_OUTPUT_DIR = OUTPUT_ROOT / "axis_b"
MANIFEST_PATH = OUTPUT_ROOT / "rubric_key_manifest.csv"

CASE_HEADER_RE = re.compile(r"^## (C\d{3})\s+—", re.MULTILINE)
SECTION_HEADER_RE = re.compile(r"^### (Base key.*|Perturbed key.*|No-solution key.*)$", re.MULTILINE)
LEVEL_NOTE_RE = re.compile(r"^- `(?P<level>level[123])`:\s*(?P<text>.+)$", re.MULTILINE)
PER_LEVEL_SPLIT_MARKER = "\n**Per-level ceiling notes**\n"


@dataclass
class CaseSections:
    case_id: str
    base_full: str
    base_common: str
    level_notes: dict[str, str]
    perturbed: str
    no_solution: str


def _strip_block(text: str) -> str:
    return text.strip().rstrip("-").strip()


def parse_master_keys(master_text: str) -> dict[str, CaseSections]:
    case_matches = list(CASE_HEADER_RE.finditer(master_text))
    sections_by_case: dict[str, CaseSections] = {}

    for idx, match in enumerate(case_matches):
        case_id = match.group(1)
        start = match.start()
        end = case_matches[idx + 1].start() if idx + 1 < len(case_matches) else len(master_text)
        case_block = master_text[start:end].strip()

        section_matches = list(SECTION_HEADER_RE.finditer(case_block))
        section_map: dict[str, str] = {}
        for sidx, smatch in enumerate(section_matches):
            header = smatch.group(1)
            sstart = smatch.end()
            send = section_matches[sidx + 1].start() if sidx + 1 < len(section_matches) else len(case_block)
            body = _strip_block(case_block[sstart:send])
            section_map[header] = body

        base_key = next((v for k, v in section_map.items() if k.startswith("Base key")), None)
        perturbed_key = next((v for k, v in section_map.items() if k.startswith("Perturbed key")), None)
        no_solution_key = next((v for k, v in section_map.items() if k.startswith("No-solution key")), None)
        if not base_key or not perturbed_key or not no_solution_key:
            raise ValueError(f"Incomplete rubric key sections for {case_id}")

        if PER_LEVEL_SPLIT_MARKER not in base_key:
            raise ValueError(f"Missing per-level ceiling notes marker for {case_id}")
        base_common, _, notes_block = base_key.partition(PER_LEVEL_SPLIT_MARKER)
        level_notes = {m.group("level"): m.group("text").strip() for m in LEVEL_NOTE_RE.finditer(notes_block)}
        if set(level_notes) != {"level1", "level2", "level3"}:
            raise ValueError(f"Incomplete level notes for {case_id}: found {sorted(level_notes)}")

        sections_by_case[case_id] = CaseSections(
            case_id=case_id,
            base_full=base_key.strip(),
            base_common=base_common.strip(),
            level_notes=level_notes,
            perturbed=perturbed_key.strip(),
            no_solution=no_solution_key.strip(),
        )

    return sections_by_case


def build_axis_a_key(case_id: str, sections: CaseSections) -> str:
    return (
        f"<!-- generated_from: results/report_quality_rubric_keys.md -->\n"
        f"<!-- case_id: {case_id} -->\n"
        f"<!-- axis: axis_a -->\n"
        f"<!-- variant_id: perturbed -->\n\n"
        f"# Rubric Key\n\n"
        f"## Perturbed Key\n\n"
        f"{sections.perturbed}\n"
    )


def build_axis_b_key(case_id: str, variant_id: str, sections: CaseSections) -> str:
    header = (
        f"<!-- generated_from: results/report_quality_rubric_keys.md -->\n"
        f"<!-- case_id: {case_id} -->\n"
        f"<!-- axis: axis_b -->\n"
        f"<!-- variant_id: {variant_id} -->\n\n"
        f"# Rubric Key\n\n"
    )

    if variant_id in {"level1", "level2", "level3"}:
        note = sections.level_notes[variant_id]
        return (
            header
            + "## Base Key\n\n"
            + sections.base_common
            + "\n\n## Variant-Specific Scoring Note\n\n"
            + f"- `{variant_id}`: {note}\n"
        )
    if variant_id == "perturbed":
        return header + "## Perturbed Key\n\n" + sections.perturbed + "\n"
    if variant_id == "no_solution":
        return header + "## No-solution Key\n\n" + sections.no_solution + "\n"
    raise ValueError(f"Unsupported Axis B variant: {variant_id}")


def read_csv_rows(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def write_csv_rows(path: Path, fieldnames: list[str], rows: list[dict[str, str]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def generate_rubric_keys() -> dict[str, int]:
    master_text = MASTER_PATH.read_text(encoding="utf-8")
    sections_by_case = parse_master_keys(master_text)
    axis_a_rows = read_csv_rows(AXIS_A_INDEX_PATH)
    axis_b_rows = read_csv_rows(AXIS_B_INDEX_PATH)

    AXIS_A_OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    AXIS_B_OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    manifest_rows: list[dict[str, str]] = []

    for row in axis_a_rows:
        case_id = row["case_id"]
        variant_id = row["variant_id"]
        sections = sections_by_case[case_id]
        output_path = AXIS_A_OUTPUT_DIR / f"{case_id}_{variant_id}_key.md"
        output_path.write_text(build_axis_a_key(case_id, sections), encoding="utf-8")
        row["rubric_key_path"] = output_path.relative_to(REPO_ROOT).as_posix()
        manifest_rows.append(
            {
                "axis": "axis_a",
                "case_id": case_id,
                "variant_id": variant_id,
                "source_master_path": MASTER_PATH.relative_to(REPO_ROOT).as_posix(),
                "source_section": "perturbed",
                "generated_key_path": output_path.relative_to(REPO_ROOT).as_posix(),
                "generation_rule": "perturbed_direct_extract",
                "notes": row.get("notes", ""),
            }
        )

    for row in axis_b_rows:
        case_id = row["case_id"]
        variant_id = row["variant_id"]
        sections = sections_by_case[case_id]
        output_path = AXIS_B_OUTPUT_DIR / f"{case_id}_{variant_id}_key.md"
        output_path.write_text(build_axis_b_key(case_id, variant_id, sections), encoding="utf-8")
        row["rubric_key_path"] = output_path.relative_to(REPO_ROOT).as_posix()
        generation_rule = {
            "level1": "base_plus_level1_note",
            "level2": "base_plus_level2_note",
            "level3": "base_plus_level3_note",
            "perturbed": "perturbed_direct_extract",
            "no_solution": "no_solution_direct_extract",
        }[variant_id]
        source_section = {
            "level1": "base",
            "level2": "base",
            "level3": "base",
            "perturbed": "perturbed",
            "no_solution": "no_solution",
        }[variant_id]
        manifest_rows.append(
            {
                "axis": "axis_b",
                "case_id": case_id,
                "variant_id": variant_id,
                "source_master_path": MASTER_PATH.relative_to(REPO_ROOT).as_posix(),
                "source_section": source_section,
                "generated_key_path": output_path.relative_to(REPO_ROOT).as_posix(),
                "generation_rule": generation_rule,
                "notes": row.get("notes", ""),
            }
        )

    write_csv_rows(
        AXIS_A_INDEX_PATH,
        list(axis_a_rows[0].keys()),
        axis_a_rows,
    )
    write_csv_rows(
        AXIS_B_INDEX_PATH,
        list(axis_b_rows[0].keys()),
        axis_b_rows,
    )
    write_csv_rows(
        MANIFEST_PATH,
        [
            "axis",
            "case_id",
            "variant_id",
            "source_master_path",
            "source_section",
            "generated_key_path",
            "generation_rule",
            "notes",
        ],
        manifest_rows,
    )
    return {
        "axis_a_keys": len(axis_a_rows),
        "axis_b_keys": len(axis_b_rows),
        "manifest_rows": len(manifest_rows),
    }


def main() -> None:
    counts = generate_rubric_keys()
    print(
        "Generated rubric keys:",
        f"axis_a={counts['axis_a_keys']}",
        f"axis_b={counts['axis_b_keys']}",
        f"manifest_rows={counts['manifest_rows']}",
    )


if __name__ == "__main__":
    main()
