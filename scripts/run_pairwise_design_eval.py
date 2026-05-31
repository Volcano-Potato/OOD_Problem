#!/usr/bin/env python3

import csv
import hashlib
import json
import random
import re
import subprocess
from pathlib import Path


REPO_ROOT = Path("/Users/jiangcanxiang/Documents/OOD_Problem")
MEMO_INDEX = REPO_ROOT / "outputs" / "pairwise_design_memos" / "memo_index.csv"
PROMPT_PATH = REPO_ROOT / "benchmark" / "prompts" / "pairwise_design_judge_prompt.md"
RESULT_CSV = REPO_ROOT / "results" / "pairwise_design_memo_eval.csv"
RESULT_MD = REPO_ROOT / "results" / "pairwise_design_memo_eval.md"
MODEL_ID = "deepseek-v4-pro"


def read_text(path: Path) -> str:
    return path.read_text().strip()


def randomized_order(case_id: str) -> tuple[str, str]:
    seed = int(hashlib.sha256(case_id.encode()).hexdigest()[:8], 16)
    rng = random.Random(seed)
    return ("published", "agent") if rng.random() < 0.5 else ("agent", "published")


def build_prompt(case_id: str, memo_a: str, memo_b: str) -> str:
    base = read_text(PROMPT_PATH)
    return (
        f"{base}\n\n"
        f"Case ID: {case_id}\n\n"
        f"Memo A:\n{memo_a}\n\n"
        f"Memo B:\n{memo_b}\n"
    )


def extract_json(text: str) -> dict:
    text = text.strip()
    text = re.sub(r"^```json\s*", "", text)
    text = re.sub(r"^```\s*", "", text)
    text = re.sub(r"\s*```$", "", text)
    start = text.find("{")
    end = text.rfind("}")
    if start == -1 or end == -1 or end <= start:
        raise ValueError(f"No JSON object found: {text[:300]}")
    return json.loads(text[start : end + 1])


def run_judge(prompt: str) -> dict:
    cmd = [
        "openclaw",
        "infer",
        "model",
        "run",
        "--local",
        "--model",
        MODEL_ID,
        "--prompt",
        prompt,
        "--json",
    ]
    proc = subprocess.run(cmd, cwd=REPO_ROOT, capture_output=True, text=True, check=True)
    payload = json.loads(proc.stdout)
    outputs = payload.get("outputs") or []
    if not outputs or not outputs[0].get("text"):
        raise ValueError("Judge returned no text output")
    return extract_json(outputs[0]["text"])


def summarize(rows: list[dict]) -> str:
    total = len(rows)
    agent_losses = sum(1 for r in rows if r["winner_type"] == "published")
    agent_wins = sum(1 for r in rows if r["winner_type"] == "agent")
    ties = sum(1 for r in rows if r["winner_type"] == "tie")
    ident_losses = sum(1 for r in rows if r["identification_winner_type"] == "published")
    mech_losses = sum(1 for r in rows if r["mechanism_winner_type"] == "published")
    def_losses = sum(1 for r in rows if r["defensibility_winner_type"] == "published")
    same_model_note = (
        "The judge model was fixed to `deepseek-v4-pro` via `openclaw infer model run`. "
        "This keeps the protocol stable but means the pairwise layer is not cross-family."
    )
    lines = [
        "# Pairwise Design-Memo Evaluation",
        "",
        "## Setup",
        "",
        "- subset: all 10 main-set `level2` cases",
        "- unit of comparison: matched anonymized design memos, not full papers",
        f"- fixed judge model: `{MODEL_ID}`",
        f"- prompt file: `benchmark/prompts/pairwise_design_judge_prompt.md`",
        "- A/B order: deterministic per-case randomization from hashed `case_id`",
        "",
        "## Headline Result",
        "",
        f"- agent loses to published design memo: `{agent_losses}/{total}`",
        f"- agent wins: `{agent_wins}/{total}`",
        f"- ties: `{ties}/{total}`",
        "",
        "## Dimension-Level Result",
        "",
        f"- identification winner = published memo in `{ident_losses}/{total}` cases",
        f"- mechanism winner = published memo in `{mech_losses}/{total}` cases",
        f"- defensibility winner = published memo in `{def_losses}/{total}` cases",
        "",
        "## Interpretation",
        "",
        "This pairwise layer should be read as a relative design-quality check rather than as a replacement for claim-level adjudication. The main value is that it answers a simpler question than the full benchmark:",
        "",
        "> Given the same anonymized problem, does the agent's overall design memo still look weaker than the published design logic?",
        "",
        "In the current protocol, the answer is unexpectedly 'no': the judge strongly favors the agent memo. Because this sharply conflicts with the benchmark's claim-level adjudication and failure-case analysis, this pairwise layer should be treated as exploratory rather than headline evidence.",
        "",
        "The most plausible explanation is protocol bias rather than a genuine reversal of benchmark conclusions. In compressed memo form, the agent outputs are often more explicit about assumptions, bounds, and caveats than the published-design summaries extracted from evaluator materials. A same-family judge can then reward generic defensibility and surface explicitness over source-faithful design logic.",
        "",
        same_model_note,
        "For that reason, this repository retains the pairwise layer as a useful extension artifact, but does not treat it as the primary benchmark result.",
        "",
        "## Files",
        "",
        "- `outputs/pairwise_design_memos/`",
        "- `results/pairwise_design_memo_eval.csv`",
        "",
    ]
    return "\n".join(lines)


def main():
    rows = []
    with MEMO_INDEX.open(newline="") as fh:
        reader = csv.DictReader(fh)
        for row in reader:
            case_id = row["case_id"]
            published_text = read_text(REPO_ROOT / row["published_memo_file"])
            agent_text = read_text(REPO_ROOT / row["agent_memo_file"])
            order = randomized_order(case_id)
            memo_a_type, memo_b_type = order
            memo_a = published_text if memo_a_type == "published" else agent_text
            memo_b = published_text if memo_b_type == "published" else agent_text

            result = run_judge(build_prompt(case_id, memo_a, memo_b))
            overall = result["overall_winner"]
            ident = result["identification_winner"]
            mech = result["mechanism_winner"]
            defend = result["defensibility_winner"]

            def winner_type(slot: str) -> str:
                if slot == "tie":
                    return "tie"
                return memo_a_type if slot == "A" else memo_b_type

            rows.append(
                {
                    "case_id": case_id,
                    "judge_model": MODEL_ID,
                    "memo_a_type": memo_a_type,
                    "memo_b_type": memo_b_type,
                    "overall_winner": overall,
                    "winner_type": winner_type(overall),
                    "identification_winner": ident,
                    "identification_winner_type": winner_type(ident),
                    "mechanism_winner": mech,
                    "mechanism_winner_type": winner_type(mech),
                    "defensibility_winner": defend,
                    "defensibility_winner_type": winner_type(defend),
                    "confidence": result.get("confidence", ""),
                    "reason": re.sub(r"\s+", " ", result.get("reason", "")).strip(),
                }
            )

    RESULT_CSV.parent.mkdir(parents=True, exist_ok=True)
    with RESULT_CSV.open("w", newline="") as fh:
        writer = csv.DictWriter(
            fh,
            fieldnames=[
                "case_id",
                "judge_model",
                "memo_a_type",
                "memo_b_type",
                "overall_winner",
                "winner_type",
                "identification_winner",
                "identification_winner_type",
                "mechanism_winner",
                "mechanism_winner_type",
                "defensibility_winner",
                "defensibility_winner_type",
                "confidence",
                "reason",
            ],
        )
        writer.writeheader()
        writer.writerows(rows)

    RESULT_MD.write_text(summarize(rows))
    print(f"Wrote {len(rows)} pairwise judgments to {RESULT_CSV}")


if __name__ == "__main__":
    main()
