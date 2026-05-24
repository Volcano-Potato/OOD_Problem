<!-- visibility: evaluator-only -->
<!-- do_not_include_in_agent_context: true -->
<!-- case_id: C000 -->

# Case Audit

## Audit Scope

- reviewer: replace_with_reviewer
- date: YYYY-MM-DD
- scope: `agent_task_level1.md`, `agent_task_level2.md`, `agent_task_level3.md`, `agent_task_perturbed.md`, `agent_task_no_solution.md`, `perturbed_variant.md`, `no_solution_variant.md`, and `gold_reference.md`
- gold_reference_alignment_status: approve / revise / reject

## Identity Leakage

- risk_level: low / medium / high
- issues:
  - [Describe whether title, authors, exact place, exact sample size, named organization, or distinctive phrase leakage remains.]
- fixes:
  - [If no fixes are needed, write `None.`]

## Solution Leakage

- risk_level: low / medium / high
- issues:
  - [Describe whether Level 2 or Level 3 gives away the hidden design, linchpin, or exact source method.]
- fixes:
  - [If no fixes are needed, write `None.`]

## Validity

- level1_status: approve / revise / reject
- level2_status: approve / revise / reject
- level3_status: approve / revise / reject
- perturbed_status: approve / revise / reject
- no_solution_status: approve / revise / reject
- notes:
  - [Explain whether Level 1 remains understandable.]
  - [Explain whether Level 2 adds enough structure without method leakage.]
  - [Explain whether Level 3 adds threats without handing out the answer.]
  - [Explain whether the perturbed variant changes exactly one key condition.]
  - [Explain whether the no-solution variant truly removes strong identification.]

## File Checklist

| file | visibility header present | no source identity leakage | no gold answer leakage | ready for run |
|---|---|---|---|---|
| `agent_task_level1.md` | yes / no | yes / no | yes / no | yes / no |
| `agent_task_level2.md` | yes / no | yes / no | yes / no | yes / no |
| `agent_task_level3.md` | yes / no | yes / no | yes / no | yes / no |
| `agent_task_perturbed.md` | yes / no | yes / no | yes / no | yes / no |
| `agent_task_no_solution.md` | yes / no | yes / no | yes / no | yes / no |

## Final Decision

- decision: approve / revise / reject
- required_revisions:
  - [If no revisions are needed, write `None.`]
