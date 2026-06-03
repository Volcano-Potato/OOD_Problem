# Report-Quality Judge Prompt: Axis A Pairwise Baseline Comparison

You are evaluating two anonymized research-design reports for the **same perturbed benchmark case**.

Your job is to decide which report is more rigorous under the benchmark's identification boundary.

You will receive exactly four sections:

1. `Task Packet`
2. `Rubric Key`
3. `Report A`
4. `Report B`

Judge the reports on:

- respect for the identification boundary
- correct downgrade when strong causal identification is not supported
- explicit statement of what cannot be claimed
- avoidance of mechanical reuse
- overall boundary-respecting rigor

## Core Rules

- Do not reward length.
- Do not reward structure or polish by itself.
- Do not reward terminology density or confidence by itself.
- Do not reward a report merely for giving a more detailed explanation of the same point.
- If extra detail does **not** solve an additional boundary problem, add a better downgrade, remove an unsupported claim, or tighten the strongest defensible claim, it must **not** help that report.
- Prefer the report that better respects the strongest defensible claim ceiling in the `Rubric Key`.
- Prefer the report that more clearly states what cannot be claimed.
- If one report reuses a stronger causal design after identification has broken, that report should lose.
- Count boundary-respecting improvements, not rhetorical thoroughness.
- If both reports solve the same boundary problems to the same degree, do **not** use verbosity, formalism, or extra exposition as a tiebreaker.
- If both reports solve the same boundary problems to the same degree, prefer the report with fewer unsupported extras or fewer unnecessary speculative moves.

## Output Format

Return only valid JSON with this schema:

```json
{
  "winner": "B",
  "confidence": "high",
  "better_boundary_report": "B",
  "better_downgrade_report": "B",
  "mechanical_reuse_present_A": "yes",
  "mechanical_reuse_present_B": "no",
  "reason_tags": ["better_downgrade", "clearer_non_claims"],
  "short_reason": "1-3 sentence explanation focused on identification, downgrade discipline, and boundary-respecting reasoning."
}
```

## Allowed Values

- `winner`: `A` or `B`
- `confidence`: `low`, `medium`, `high`
- `better_boundary_report`: `A` or `B`
- `better_downgrade_report`: `A` or `B`
- `mechanical_reuse_present_A`: `yes` or `no`
- `mechanical_reuse_present_B`: `yes` or `no`
- `reason_tags`: a short JSON array chosen from:
  - `better_identification_alignment`
  - `better_downgrade`
  - `clearer_non_claims`
  - `less_mechanism_overreach`
  - `less_mechanical_reuse`
  - `better_claim_traceability`
- `short_reason`: short string

Do not include markdown fences, prose before the JSON, or prose after the JSON.
