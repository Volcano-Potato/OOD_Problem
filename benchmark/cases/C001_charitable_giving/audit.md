<!-- visibility: evaluator-only -->
<!-- do_not_include_in_agent_context: true -->
<!-- case_id: C001 -->

# Case Audit: C001

## Audit Scope

- reviewer: Codex
- date: 2026-05-24
- scope: `agent_task_level1.md`, `agent_task_level2.md`, `agent_task_level3.md`, `agent_task_perturbed.md`, `agent_task_no_solution.md`, `perturbed_variant.md`, `no_solution_variant.md`, and `gold_reference.md`
- gold_reference_alignment_status: approve

## Identity Leakage

- risk_level: low
- issues:
  - The in-person fundraising plus avoidance-channel setting remains somewhat recognizable at the abstract domain level, but the paper title, authors, named charities, exact city, exact dates, and exact sample-size combination are removed.
- fixes:
  - None.

## Solution Leakage

- risk_level: low
- issues:
  - Level 2 and Level 3 make clear that contact and giving must be analyzed jointly, which narrows the design space, but they do not reveal the original source labels, exact arm structure, or the hidden gold phrasing around the key mechanism.
- fixes:
  - None.

## Validity

- level1_status: approve
- level2_status: approve
- level3_status: approve
- perturbed_status: approve
- no_solution_status: approve
- notes:
  - Level 1 cleanly states the business problem and mechanism question without giving away the design answer.
  - Level 2 adds enough assignment, timing, and outcome structure for a serious causal-design response while keeping the linchpin anonymous.
  - Level 3 adds useful threats and institutional detail without naming the source design or turning the hints into an answer key.
  - The perturbed variant changes exactly one key condition: the pre-contact avoidance channel becomes self-selected rather than assigned.
  - The no-solution variant removes credible exogenous variation and leaves only descriptive or correlational analysis as defensible.

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
