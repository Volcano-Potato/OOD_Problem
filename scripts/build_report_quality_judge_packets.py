from __future__ import annotations

import csv
import hashlib
import json
import re
import shutil
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_AXIS_A_INDEX_PATH = REPO_ROOT / "outputs" / "report_quality_judge_packets" / "axis_a_report_index.csv"
DEFAULT_AXIS_B_INDEX_PATH = REPO_ROOT / "outputs" / "report_quality_judge_packets" / "axis_b_report_index.csv"
DEFAULT_OUTPUT_ROOT = REPO_ROOT / "outputs" / "report_quality_judge_packets"
DEFAULT_PACKET_MANIFEST_PATH = DEFAULT_OUTPUT_ROOT / "judge_packet_manifest.csv"
ABSOLUTE_PROMPT_PATH = REPO_ROOT / "benchmark" / "prompts" / "report_quality_judge" / "absolute_scoring_prompt.md"
AXIS_A_RANKING_PROMPT_PATH = (
    REPO_ROOT / "benchmark" / "prompts" / "report_quality_judge" / "axis_a_ranking_prompt.md"
)
AXIS_A_PAIRWISE_PROMPT_PATH = (
    REPO_ROOT / "benchmark" / "prompts" / "report_quality_judge" / "axis_a_pairwise_baseline_prompt.md"
)


def read_csv_rows(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def write_csv_rows(path: Path, fieldnames: list[str], rows: list[dict[str, str]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def read_text_from_repo_relative(relative_path: str) -> str:
    return (REPO_ROOT / relative_path).read_text(encoding="utf-8").strip() + "\n"


def extract_report_body_from_main_raw_log(path: Path) -> str:
    text = path.read_text(encoding="utf-8")
    marker = "## Raw Agent Output"
    if marker not in text:
        raise ValueError(f"Missing raw-output marker in {path}")
    body = text.split(marker, 1)[1].strip()
    return body + "\n"


def read_final_report(relative_path: str) -> str:
    path = REPO_ROOT / relative_path
    if "outputs/raw_agent_logs/main/" in relative_path:
        return extract_report_body_from_main_raw_log(path)
    return path.read_text(encoding="utf-8").strip() + "\n"


def word_count(text: str) -> int:
    return len(re.findall(r"\S+", text))


def char_count(text: str) -> int:
    return len(text)


def build_ranking_assignment(case_id: str) -> dict[str, str]:
    arms = ["baseline", "v1", "v2", "v3"]
    digest = hashlib.sha256(case_id.encode("utf-8")).digest()
    decorated = [(digest[i], arm) for i, arm in enumerate(arms)]
    ordered = [arm for _, arm in sorted(decorated)]
    return dict(zip(["A", "B", "C", "D"], ordered))


def build_pairwise_assignment(case_id: str, challenger: str) -> dict[str, str]:
    labels = ["A", "B"]
    arms = ["baseline", challenger]
    digest = hashlib.sha256(f"{case_id}:{challenger}".encode("utf-8")).digest()
    if digest[0] % 2 == 0:
        ordered = arms
    else:
        ordered = list(reversed(arms))
    return dict(zip(labels, ordered))


def ensure_clean_dir(path: Path) -> None:
    if path.exists():
        shutil.rmtree(path)
    path.mkdir(parents=True, exist_ok=True)


def write_packet_files(
    packet_dir: Path,
    task_packet_text: str,
    rubric_key_text: str,
    final_report_text: str,
    prompt_text: str,
    prompt_path: Path,
    manifest: dict,
) -> None:
    ensure_clean_dir(packet_dir)
    (packet_dir / "task_packet.md").write_text(task_packet_text, encoding="utf-8")
    (packet_dir / "rubric_key.md").write_text(rubric_key_text, encoding="utf-8")
    (packet_dir / "final_report.md").write_text(final_report_text, encoding="utf-8")
    judge_input_text = (
        "## Task Packet\n\n"
        + task_packet_text.strip()
        + "\n\n## Rubric Key\n\n"
        + rubric_key_text.strip()
        + "\n\n## Final Report\n\n"
        + final_report_text.strip()
        + "\n"
    )
    (packet_dir / "judge_input.md").write_text(judge_input_text, encoding="utf-8")
    judge_input_path = packet_dir / "judge_input.md"
    judge_request_text = prompt_text.strip() + "\n\n---\n\n" + judge_input_text
    judge_request_path = packet_dir / "judge_request.md"
    judge_request_path.write_text(judge_request_text, encoding="utf-8")
    manifest["judge_input_path"] = judge_input_path.as_posix()
    manifest["judge_request_path"] = judge_request_path.as_posix()
    manifest["prompt_path"] = prompt_path.relative_to(REPO_ROOT).as_posix()
    (packet_dir / "packet_manifest.json").write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )


def generate_judge_packets(
    axis_a_index_path: Path = DEFAULT_AXIS_A_INDEX_PATH,
    axis_b_index_path: Path = DEFAULT_AXIS_B_INDEX_PATH,
    output_root: Path = DEFAULT_OUTPUT_ROOT,
    packet_manifest_path: Path | None = None,
) -> dict[str, int]:
    axis_a_rows = read_csv_rows(axis_a_index_path)
    axis_b_rows = read_csv_rows(axis_b_index_path)
    packet_manifest_path = packet_manifest_path or (output_root / "judge_packet_manifest.csv")
    absolute_prompt_text = ABSOLUTE_PROMPT_PATH.read_text(encoding="utf-8")
    ranking_prompt_text = AXIS_A_RANKING_PROMPT_PATH.read_text(encoding="utf-8")
    pairwise_prompt_text = AXIS_A_PAIRWISE_PROMPT_PATH.read_text(encoding="utf-8")

    axis_a_root = output_root / "axis_a"
    axis_b_root = output_root / "axis_b"
    axis_a_root.mkdir(parents=True, exist_ok=True)
    axis_b_root.mkdir(parents=True, exist_ok=True)

    manifest_rows: list[dict[str, str]] = []

    for row in axis_a_rows:
        case_id = row["case_id"]
        variant_id = row["variant_id"]
        task_packet_text = read_text_from_repo_relative(row["task_packet_path"])
        rubric_key_text = read_text_from_repo_relative(row["rubric_key_path"])

        arm_sources = {
            "baseline": row["baseline_formal_report_path"],
            "v1": row["v1_preferred_report_path"],
            "v2": row["v2_preferred_report_path"],
            "v3": row["v3_preferred_report_path"],
        }

        final_reports: dict[str, str] = {}
        for arm, source_path in arm_sources.items():
            final_report_text = read_final_report(source_path)
            final_reports[arm] = final_report_text
            packet_dir = axis_a_root / case_id / arm
            manifest = {
                "axis": "axis_a",
                "packet_type": "absolute",
                "case_id": case_id,
                "variant_id": variant_id,
                "agent_variant": arm,
                "blind_label": "",
                "source_task_packet": row["task_packet_path"],
                "source_rubric_key": row["rubric_key_path"],
                "source_final_report": source_path,
                "word_count": word_count(final_report_text),
                "char_count": char_count(final_report_text),
                "notes": row.get("notes", ""),
            }
            write_packet_files(
                packet_dir,
                task_packet_text,
                rubric_key_text,
                final_report_text,
                absolute_prompt_text,
                ABSOLUTE_PROMPT_PATH,
                manifest,
            )
            manifest_rows.append(
                {
                    "axis": "axis_a",
                    "packet_type": "absolute",
                    "case_id": case_id,
                    "variant_id": variant_id,
                    "agent_variant": arm,
                    "packet_dir": packet_dir.relative_to(REPO_ROOT).as_posix()
                    if packet_dir.is_relative_to(REPO_ROOT)
                    else packet_dir.as_posix(),
                    "task_packet_path": row["task_packet_path"],
                    "rubric_key_path": row["rubric_key_path"],
                    "final_report_source_path": source_path,
                    "word_count": str(word_count(final_report_text)),
                    "char_count": str(char_count(final_report_text)),
                    "judge_input_path": (packet_dir / "judge_input.md").relative_to(REPO_ROOT).as_posix()
                    if packet_dir.is_relative_to(REPO_ROOT)
                    else (packet_dir / "judge_input.md").as_posix(),
                    "judge_request_path": (packet_dir / "judge_request.md").relative_to(REPO_ROOT).as_posix()
                    if packet_dir.is_relative_to(REPO_ROOT)
                    else (packet_dir / "judge_request.md").as_posix(),
                    "prompt_path": ABSOLUTE_PROMPT_PATH.relative_to(REPO_ROOT).as_posix(),
                    "blind_label": "",
                    "notes": row.get("notes", ""),
                }
            )

        ranking_dir = axis_a_root / case_id / "within_case_ranking"
        ensure_clean_dir(ranking_dir)
        (ranking_dir / "task_packet.md").write_text(task_packet_text, encoding="utf-8")
        (ranking_dir / "rubric_key.md").write_text(rubric_key_text, encoding="utf-8")
        assignment = build_ranking_assignment(case_id)
        reverse_assignment = {arm: label for label, arm in assignment.items()}
        for label, arm in assignment.items():
            (ranking_dir / f"report_{label}.md").write_text(final_reports[arm], encoding="utf-8")
        ranking_manifest = {
            "axis": "axis_a",
            "packet_type": "within_case_ranking",
            "case_id": case_id,
            "variant_id": variant_id,
            "arm_to_blind_label": reverse_assignment,
            "blind_label_to_arm": assignment,
            "source_task_packet": row["task_packet_path"],
            "source_rubric_key": row["rubric_key_path"],
            "report_word_counts": {arm: word_count(text) for arm, text in final_reports.items()},
            "report_char_counts": {arm: char_count(text) for arm, text in final_reports.items()},
            "notes": row.get("notes", ""),
        }
        judge_input_lines = [
            "## Task Packet",
            "",
            task_packet_text.strip(),
            "",
            "## Rubric Key",
            "",
            rubric_key_text.strip(),
            "",
        ]
        for label in ["A", "B", "C", "D"]:
            judge_input_lines.extend([f"## Report {label}", "", (ranking_dir / f"report_{label}.md").read_text(encoding='utf-8').strip(), ""])
        judge_input_text = "\n".join(judge_input_lines).rstrip() + "\n"
        (ranking_dir / "judge_input.md").write_text(judge_input_text, encoding="utf-8")
        (ranking_dir / "judge_request.md").write_text(
            ranking_prompt_text.strip() + "\n\n---\n\n" + judge_input_text,
            encoding="utf-8",
        )
        ranking_manifest["judge_input_path"] = (ranking_dir / "judge_input.md").as_posix()
        ranking_manifest["judge_request_path"] = (ranking_dir / "judge_request.md").as_posix()
        ranking_manifest["prompt_path"] = AXIS_A_RANKING_PROMPT_PATH.relative_to(REPO_ROOT).as_posix()
        (ranking_dir / "packet_manifest.json").write_text(
            json.dumps(ranking_manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
        )
        manifest_rows.append(
            {
                "axis": "axis_a",
                "packet_type": "within_case_ranking",
                "case_id": case_id,
                "variant_id": variant_id,
                "agent_variant": "A/B/C/D",
                "packet_dir": ranking_dir.relative_to(REPO_ROOT).as_posix()
                if ranking_dir.is_relative_to(REPO_ROOT)
                else ranking_dir.as_posix(),
                "task_packet_path": row["task_packet_path"],
                "rubric_key_path": row["rubric_key_path"],
                "final_report_source_path": json.dumps(arm_sources, ensure_ascii=False),
                "word_count": "",
                "char_count": "",
                "judge_input_path": (ranking_dir / "judge_input.md").relative_to(REPO_ROOT).as_posix()
                if ranking_dir.is_relative_to(REPO_ROOT)
                else (ranking_dir / "judge_input.md").as_posix(),
                "judge_request_path": (ranking_dir / "judge_request.md").relative_to(REPO_ROOT).as_posix()
                if ranking_dir.is_relative_to(REPO_ROOT)
                else (ranking_dir / "judge_request.md").as_posix(),
                "prompt_path": AXIS_A_RANKING_PROMPT_PATH.relative_to(REPO_ROOT).as_posix(),
                "blind_label": json.dumps(assignment, ensure_ascii=False),
                "notes": row.get("notes", ""),
            }
        )

        for challenger in ["v1", "v2", "v3"]:
            pairwise_dir = axis_a_root / case_id / f"pairwise_vs_baseline_{challenger}"
            ensure_clean_dir(pairwise_dir)
            (pairwise_dir / "task_packet.md").write_text(task_packet_text, encoding="utf-8")
            (pairwise_dir / "rubric_key.md").write_text(rubric_key_text, encoding="utf-8")
            assignment = build_pairwise_assignment(case_id, challenger)
            reverse_assignment = {arm: label for label, arm in assignment.items()}
            for label, arm in assignment.items():
                (pairwise_dir / f"report_{label}.md").write_text(final_reports[arm], encoding="utf-8")
            pairwise_manifest = {
                "axis": "axis_a",
                "packet_type": "pairwise_vs_baseline",
                "case_id": case_id,
                "variant_id": variant_id,
                "challenger": challenger,
                "arm_to_blind_label": reverse_assignment,
                "blind_label_to_arm": assignment,
                "source_task_packet": row["task_packet_path"],
                "source_rubric_key": row["rubric_key_path"],
                "report_word_counts": {
                    "baseline": word_count(final_reports["baseline"]),
                    challenger: word_count(final_reports[challenger]),
                },
                "report_char_counts": {
                    "baseline": char_count(final_reports["baseline"]),
                    challenger: char_count(final_reports[challenger]),
                },
                "notes": row.get("notes", ""),
            }
            pairwise_input_lines = [
                "## Task Packet",
                "",
                task_packet_text.strip(),
                "",
                "## Rubric Key",
                "",
                rubric_key_text.strip(),
                "",
                "## Report A",
                "",
                (pairwise_dir / "report_A.md").read_text(encoding="utf-8").strip(),
                "",
                "## Report B",
                "",
                (pairwise_dir / "report_B.md").read_text(encoding="utf-8").strip(),
                "",
            ]
            pairwise_input_text = "\n".join(pairwise_input_lines).rstrip() + "\n"
            (pairwise_dir / "judge_input.md").write_text(pairwise_input_text, encoding="utf-8")
            (pairwise_dir / "judge_request.md").write_text(
                pairwise_prompt_text.strip() + "\n\n---\n\n" + pairwise_input_text,
                encoding="utf-8",
            )
            pairwise_manifest["judge_input_path"] = (pairwise_dir / "judge_input.md").as_posix()
            pairwise_manifest["judge_request_path"] = (pairwise_dir / "judge_request.md").as_posix()
            pairwise_manifest["prompt_path"] = AXIS_A_PAIRWISE_PROMPT_PATH.relative_to(REPO_ROOT).as_posix()
            (pairwise_dir / "packet_manifest.json").write_text(
                json.dumps(pairwise_manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
            )
            manifest_rows.append(
                {
                    "axis": "axis_a",
                    "packet_type": "pairwise_vs_baseline",
                    "case_id": case_id,
                    "variant_id": variant_id,
                    "agent_variant": f"baseline_vs_{challenger}",
                    "packet_dir": pairwise_dir.relative_to(REPO_ROOT).as_posix()
                    if pairwise_dir.is_relative_to(REPO_ROOT)
                    else pairwise_dir.as_posix(),
                    "task_packet_path": row["task_packet_path"],
                    "rubric_key_path": row["rubric_key_path"],
                    "final_report_source_path": json.dumps(
                        {
                            "baseline": arm_sources["baseline"],
                            challenger: arm_sources[challenger],
                        },
                        ensure_ascii=False,
                    ),
                    "word_count": "",
                    "char_count": "",
                    "judge_input_path": (pairwise_dir / "judge_input.md").relative_to(REPO_ROOT).as_posix()
                    if pairwise_dir.is_relative_to(REPO_ROOT)
                    else (pairwise_dir / "judge_input.md").as_posix(),
                    "judge_request_path": (pairwise_dir / "judge_request.md").relative_to(REPO_ROOT).as_posix()
                    if pairwise_dir.is_relative_to(REPO_ROOT)
                    else (pairwise_dir / "judge_request.md").as_posix(),
                    "prompt_path": AXIS_A_PAIRWISE_PROMPT_PATH.relative_to(REPO_ROOT).as_posix(),
                    "blind_label": json.dumps(assignment, ensure_ascii=False),
                    "notes": row.get("notes", ""),
                }
            )

    for row in axis_b_rows:
        case_id = row["case_id"]
        variant_id = row["variant_id"]
        task_packet_text = read_text_from_repo_relative(row["task_packet_path"])
        rubric_key_text = read_text_from_repo_relative(row["rubric_key_path"])
        final_report_text = read_final_report(row["baseline_formal_report_path"])
        packet_dir = axis_b_root / f"{case_id}_{variant_id}"
        manifest = {
            "axis": "axis_b",
            "packet_type": "absolute",
            "case_id": case_id,
            "variant_id": variant_id,
            "agent_variant": "baseline",
            "blind_label": "",
            "source_task_packet": row["task_packet_path"],
            "source_rubric_key": row["rubric_key_path"],
            "source_final_report": row["baseline_formal_report_path"],
            "word_count": word_count(final_report_text),
            "char_count": char_count(final_report_text),
            "notes": row.get("notes", ""),
        }
        write_packet_files(
            packet_dir,
            task_packet_text,
            rubric_key_text,
            final_report_text,
            absolute_prompt_text,
            ABSOLUTE_PROMPT_PATH,
            manifest,
        )
        manifest_rows.append(
            {
                "axis": "axis_b",
                "packet_type": "absolute",
                "case_id": case_id,
                "variant_id": variant_id,
                "agent_variant": "baseline",
                "packet_dir": packet_dir.relative_to(REPO_ROOT).as_posix()
                if packet_dir.is_relative_to(REPO_ROOT)
                else packet_dir.as_posix(),
                "task_packet_path": row["task_packet_path"],
                "rubric_key_path": row["rubric_key_path"],
                "final_report_source_path": row["baseline_formal_report_path"],
                "word_count": str(word_count(final_report_text)),
                "char_count": str(char_count(final_report_text)),
                "judge_input_path": (packet_dir / "judge_input.md").relative_to(REPO_ROOT).as_posix()
                if packet_dir.is_relative_to(REPO_ROOT)
                else (packet_dir / "judge_input.md").as_posix(),
                "judge_request_path": (packet_dir / "judge_request.md").relative_to(REPO_ROOT).as_posix()
                if packet_dir.is_relative_to(REPO_ROOT)
                else (packet_dir / "judge_request.md").as_posix(),
                "prompt_path": ABSOLUTE_PROMPT_PATH.relative_to(REPO_ROOT).as_posix(),
                "blind_label": "",
                "notes": row.get("notes", ""),
            }
        )

    write_csv_rows(
        packet_manifest_path,
        [
            "axis",
            "packet_type",
            "case_id",
            "variant_id",
            "agent_variant",
            "packet_dir",
            "task_packet_path",
            "rubric_key_path",
            "final_report_source_path",
            "word_count",
            "char_count",
            "judge_input_path",
            "judge_request_path",
            "prompt_path",
            "blind_label",
            "notes",
        ],
        manifest_rows,
    )

    return {
        "axis_a_absolute_packets": len(axis_a_rows) * 4,
        "axis_a_ranking_packets": len(axis_a_rows),
        "axis_a_pairwise_packets": len(axis_a_rows) * 3,
        "axis_b_absolute_packets": len(axis_b_rows),
        "packet_manifest_rows": len(manifest_rows),
    }


def main() -> None:
    counts = generate_judge_packets()
    print(
        "Generated judge packets:",
        f"axis_a_absolute={counts['axis_a_absolute_packets']}",
        f"axis_a_ranking={counts['axis_a_ranking_packets']}",
        f"axis_a_pairwise={counts['axis_a_pairwise_packets']}",
        f"axis_b_absolute={counts['axis_b_absolute_packets']}",
        f"packet_manifest_rows={counts['packet_manifest_rows']}",
    )


if __name__ == "__main__":
    main()
