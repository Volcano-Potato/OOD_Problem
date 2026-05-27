<!-- visibility: evaluator-only -->
<!-- do_not_include_in_agent_context: true -->
<!-- case_id: C020 -->

# Case Audit: C020

## Audit Scope

- reviewer: Codex
- date: 2026-05-26
- scope: `agent_task_level1.md`, `agent_task_level2.md`, `agent_task_level3.md`, `agent_task_perturbed.md`, `agent_task_no_solution.md`, `perturbed_variant.md`, `no_solution_variant.md`, and `gold_reference.md`
- gold_reference_alignment_status: approve

## Identity Leakage

- risk_level: low
- issues:
  - The task preserves a terminal-digit retail-pricing setting and experimental offer-version logic, but removes the source paper title, authors, retailer identity, exact channel, exact product category, exact price values, and exact customer-assignment rule.
- fixes:
  - Agent-facing tasks avoid the exact "$9", catalog-title, women's-apparel, and zip-based assignment details that would make the source too easy to reconstruct.

## Solution Leakage

- risk_level: low
- issues:
  - Level 2 reveals that price format can vary across comparable offer versions, but does not prescribe the exact source implementation.
  - Level 3 reveals item-familiarity and markdown-cue threats without handing out a single mandatory source-paper answer.
- fixes:
  - The packet keeps the mechanism tension visible while avoiding exact source details and exact effect magnitudes.

## Validity

- level1_status: approve
- level2_status: approve
- level3_status: approve
- perturbed_status: approve
- no_solution_status: approve
- notes:
  - Level 1 states the core pricing-format question and the psychological-versus-promotional mechanism tension clearly without leaking the source.
  - Level 2 adds enough structure on comparable offer versions, item-level outcomes, and familiarity heterogeneity for a serious design response.
  - Level 3 adds institutional details and mechanism threats around markdown cues, offer environment, and inference level without prescribing the hidden implementation.
  - The perturbed variant changes exactly one key condition: ending-format variation is no longer separable from markdown or sale cues.
  - The no-solution variant removes all credible exogenous variation while keeping a rich historical pricing dataset that can tempt a weak agent into false causal claims.

## File Checklist

| file | visibility header present | no source identity leakage | no gold answer leakage | ready for run |
|---|---|---|---|---|
| `agent_task_level1.md` | yes | yes | yes | yes |
| `agent_task_level2.md` | yes | yes | yes | yes |
| `agent_task_level3.md` | yes | yes | yes | yes |
| `agent_task_perturbed.md` | yes | yes | yes | yes |
| `agent_task_no_solution.md` | yes | yes | yes | yes |

## Final Decision

- decision: approve
- required_revisions:
  - None.
