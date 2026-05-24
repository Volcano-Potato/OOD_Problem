<!-- visibility: evaluator-only -->
<!-- do_not_include_in_agent_context: true -->
<!-- case_id: C005 -->

# Case Audit: C005

## Audit Scope

- reviewer: Codex
- date: 2026-05-24
- scope: `agent_task_level1.md`, `agent_task_level2.md`, `agent_task_level3.md`, `agent_task_perturbed.md`, `agent_task_no_solution.md`, `perturbed_variant.md`, `no_solution_variant.md`, and `gold_reference.md`
- gold_reference_alignment_status: approve

## Identity Leakage

- risk_level: low
- issues:
  - The digital-ad-measurement setting is recognizable at a high level, but the source method name, advertiser identity, platform identity, exact campaign details, and exact source phrasing are removed.
- fixes:
  - None.

## Solution Leakage

- risk_level: low
- issues:
  - Level 2 and Level 3 tell the agent that assignment and realized exposure differ and that comparable opportunity matters, but they do not leak the named source method or a fully specified estimator.
- fixes:
  - None.

## Validity

- level1_status: approve
- level2_status: approve
- level3_status: approve
- perturbed_status: approve
- no_solution_status: approve
- notes:
  - Level 1 states the core business question cleanly and does not reveal the hidden solution.
  - Level 2 gives enough log structure, exposure language, and estimand tension for a serious design response.
  - Level 3 adds endogenous-exposure threats without naming the canonical solution or turning the task into a method-matching exercise.
  - The perturbed variant changes exactly one key condition: untreated opportunity-side logs are missing.
  - The no-solution variant remains realistic and tempting, but it removes holdout-style or opportunity-matched identification entirely.

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
