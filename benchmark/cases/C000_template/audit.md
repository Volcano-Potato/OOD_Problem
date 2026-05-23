<!-- visibility: evaluator-only -->
<!-- do_not_include_in_agent_context: true -->
<!-- case_id: C000 -->

# Case Audit

## Leakage Audit

- [ ] Agent-facing files do not contain original paper title.
- [ ] Agent-facing files do not contain author names.
- [ ] Agent-facing files do not contain exact named organizations or distinctive locations.
- [ ] Agent-facing files do not contain exact sample sizes when searchable.
- [ ] Agent-facing files do not contain unique treatment-arm labels or source phrases.
- [ ] Agent-facing files do not contain source PDF paths.
- [ ] File and directory names are anonymous.

## Agent-Facing File Audit

| file | visibility header present | no source identity leakage | no gold answer leakage | ready for run |
|---|---|---|---|---|
| `agent_task_level1.md` | no | no | no | no |
| `agent_task_level2.md` | no | no | no | no |
| `agent_task_level3.md` | no | no | no | no |
| `agent_task_perturbed.md` | no | no | no | no |
| `agent_task_no_solution.md` | no | no | no | no |

## Gold Reference Audit

- [ ] Gold reference states the true research question.
- [ ] Gold reference states treatment, outcome, unit, and estimand.
- [ ] Gold reference states the identification logic.
- [ ] Gold reference states must-recognize threats.
- [ ] Gold reference lists acceptable alternative designs.
- [ ] Gold reference lists unacceptable designs and error labels.

## Variant Consistency Audit

- [ ] Level 1, Level 2, and Level 3 describe the same base research setting.
- [ ] Level 2 adds data structure without leaking the gold design.
- [ ] Level 3 adds institutional details and threat hints without giving away the answer.
- [ ] Perturbed variant changes exactly one key identification condition.
- [ ] No-solution variant removes credible causal identification without becoming nonsensical.

## Audit Decision

- Decision: approve / revise / reject
- Reviewer:
- Date:
- Required revisions:
