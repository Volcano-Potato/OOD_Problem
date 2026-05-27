<!-- visibility: evaluator-only -->
<!-- do_not_include_in_agent_context: true -->
<!-- case_id: C004 -->

# Case Audit: C004

## Audit Scope

- reviewer: Codex
- date: 2026-05-26
- scope: `agent_task_level1.md`, `agent_task_level2.md`, `agent_task_level3.md`, `agent_task_perturbed.md`, `agent_task_no_solution.md`, `perturbed_variant.md`, `no_solution_variant.md`, and `gold_reference.md`
- gold_reference_alignment_status: approve

## Identity Leakage

- risk_level: low
- issues:
  - The task preserves a paid-search measurement setting that is recognizable at a high level, but it removes the source paper title, authors, named firm, named search platform, exact market count, exact percentages, exact dates, and the most searchable query-label phrasing.
- fixes:
  - None.

## Solution Leakage

- risk_level: low
- issues:
  - Level 2 and Level 3 reveal that market-level ad availability differs across comparable markets and that clicks are not the causal estimand, but they do not leak the exact source implementation, named method, exact query taxonomy, or precise experiment settings.
  - The Level 3 threat list points to substitution, trend, and inference concerns without naming a required estimator or source-specific design label.
- fixes:
  - None.

## Validity

- level1_status: approve
- level2_status: approve
- level3_status: approve
- perturbed_status: approve
- no_solution_status: approve
- notes:
  - Level 1 states the business problem clearly and preserves the key tension between incremental demand and intent-based interception without revealing the hidden design.
  - Level 2 adds enough market-time structure, downstream outcomes, and user-history heterogeneity for a serious design response while avoiding source-identifying query or firm details.
  - Level 3 adds real identification threats around individual intent, channel substitution, trend differences, and market-level inference without handing out a named solution.
  - The perturbed variant changes exactly one key condition: market-level assignment is no longer exogenous and is instead chosen by managers.
  - The no-solution variant removes credible exogenous variation entirely while keeping the task realistic and tempting through rich marketing logs and repeated sales data.

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
