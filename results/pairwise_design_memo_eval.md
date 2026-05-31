# Pairwise Design-Memo Evaluation

## Setup

- subset: all 10 main-set `level2` cases
- unit of comparison: matched anonymized design memos, not full papers
- fixed judge model: `deepseek-v4-pro`
- prompt file: `benchmark/prompts/pairwise_design_judge_prompt.md`
- A/B order: deterministic per-case randomization from hashed `case_id`

## Headline Result

- agent loses to published design memo: `0/10`
- agent wins: `10/10`
- ties: `0/10`

## Dimension-Level Result

- identification winner = published memo in `0/10` cases
- mechanism winner = published memo in `1/10` cases
- defensibility winner = published memo in `0/10` cases

## Interpretation

This pairwise layer should be read as a relative design-quality check rather than as a replacement for claim-level adjudication. The main value is that it answers a simpler question than the full benchmark:

> Given the same anonymized problem, does the agent's overall design memo still look weaker than the published design logic?

In the current protocol, the answer is unexpectedly 'no': the judge strongly favors the agent memo. Because this sharply conflicts with the benchmark's claim-level adjudication and failure-case analysis, this pairwise layer should be treated as exploratory rather than headline evidence.

The most plausible explanation is protocol bias rather than a genuine reversal of benchmark conclusions. In compressed memo form, the agent outputs are often more explicit about assumptions, bounds, and caveats than the published-design summaries extracted from evaluator materials. A same-family judge can then reward generic defensibility and surface explicitness over source-faithful design logic.

The judge model was fixed to `deepseek-v4-pro` via `openclaw infer model run`. This keeps the protocol stable but means the pairwise layer is not cross-family.
For that reason, this repository retains the pairwise layer as a useful extension artifact, but does not treat it as the primary benchmark result.

## Files

- `outputs/pairwise_design_memos/`
- `results/pairwise_design_memo_eval.csv`
