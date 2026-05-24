<!-- visibility: evaluator-only -->
<!-- do_not_include_in_agent_context: true -->
<!-- case_id: C014 -->

# Case Audit: C014

## Audit Scope

- reviewer: Codex
- date: 2026-05-24
- scope: `agent_task_level1.md`, `agent_task_level2.md`, `agent_task_level3.md`, `agent_task_perturbed.md`, `agent_task_no_solution.md`, `perturbed_variant.md`, `no_solution_variant.md`, and `gold_reference.md`
- gold_reference_alignment_status: approve

## Identity Leakage

- risk_level: low
- issues:
  - The public-project monitoring setting is somewhat distinctive, but the country, program name, exact project type, exact engineering protocol, and exact implementation details are withheld.
- fixes:
  - None.

## Solution Leakage

- risk_level: low
- issues:
  - The task packet makes clear that official records may not be enough, but it does not reveal the source paper, exact measurement protocol, or a fully specified gold design.
- fixes:
  - None.

## Validity

- level1_status: approve
- level2_status: approve
- level3_status: approve
- perturbed_status: approve
- no_solution_status: approve
- notes:
  - Level 1 cleanly frames the corruption-monitoring research problem without leaking paper identity.
  - Level 2 adds the project-level assignment and outcome structure needed for design reasoning while keeping the key measurement linchpin implicit.
  - Level 3 adds the official-versus-independent-measurement threat in a way that guides evaluation but still requires genuine causal reasoning.
  - The perturbed variant changes exactly one key condition: independent outcome measurement is removed.
  - The no-solution variant removes both exogenous assignment and independent outcomes, so only descriptive administrative analysis remains defensible.

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
