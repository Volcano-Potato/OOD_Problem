# research_agent_v1 vs baseline

## Scope

- Intervention arm: `research_agent_v1`
- Evaluation subset: `10` `perturbed` cases (`C001`, `C002`, `C004`, `C005`, `C008`, `C010`, `C014`, `C016`, `C019`, `C020`)
- Baseline comparator: frozen `benchmark_isolated` Level 2 vs perturbed paired audit in [perturbed_mechanical_reuse.csv](/Users/jiangcanxiang/Documents/OOD_Problem/results/perturbed_mechanical_reuse.csv)
- Smoke-only artifact handling: the provisional bridged `C001` smoke run was removed from `outputs/run_manifest.csv` before downstream analysis so that this comparison uses only the 10 official batch runs

## Headline

- Baseline `perturbed mechanical reuse`: `9/10`
- `research_agent_v1` `perturbed mechanical reuse`: `2/10`
- Absolute reduction: `-7/10 = -0.70`
- Relative reduction: `-77.8%`

Interpretation:
`task30` succeeded on its main H1-style intervention goal. The critic-and-reconcile loop substantially reduced broken-identification mechanical reuse on the perturbed subset.

## Case-by-case transition

| Case | Baseline | research_agent_v1 | Transition |
|---|---:|---:|---|
| `C001` | `yes` | `no` | downgraded to descriptive stratification + bounds |
| `C002` | `yes` | `no` | dropped clean channel separation; kept only narrower conditional panel design |
| `C004` | `yes` | `no` | abandoned causal design; descriptive benchmarking only |
| `C005` | `yes` | `yes` | residual reuse via supplementary IV/LATE on actual exposure |
| `C008` | `yes` | `yes` | residual reuse via secondary within-store DiD and salience-gradient logic |
| `C010` | `yes` | `no` | narrowed to bundle ITT; no procrastination identification |
| `C014` | `yes` | `no` | narrowed to reporting-side ITT; no corruption claim |
| `C016` | `yes` | `no` | switched to bounds/descriptive analysis |
| `C019` | `no` | `no` | remained a descriptive fallback |
| `C020` | `yes` | `no` | abandoned standalone format effect; reframed around bundle analysis |

## Auxiliary observations

- Stage 4 critic recognized the perturbed-condition dependency in `10/10` official batch runs.
- The intervention works mainly by forcing explicit downgrade to descriptive, bounded, or re-targeted estimands.
- Residual failure is concentrated in cases where the final memo still preserves a secondary causal candidate from the base design instead of dropping it completely.
- The two remaining reuse cases are:
  - `C005`: actual-exposure IV/LATE retained as a caveated supplementary estimand
  - `C008`: within-store treated-vs-untreated comparison retained as a caveated secondary design

## Plan-vs-implementation note

- This arm implements the `v1` logic described in [research_agent_redesign_plan.md](/Users/jiangcanxiang/Documents/OOD_Problem/report/research_agent_redesign_plan.md): `10` `perturbed` runs only, with a `Stage 3 -> Stage 4 -> Stage 5` critic-and-reconcile loop and H1 centered on paired `mechanical reuse`.
- It is not a literal one-to-one reproduction of every engineering detail in that plan.
- In particular:
  - the implementation reused the existing `benchmark_isolated` OpenClaw configuration instead of creating separate base agent configs for `benchmark_research_agent` and `benchmark_design_critic`
  - role separation was achieved through stage-specific prompts plus an external orchestrator
  - `v2` retrieval, `v3` planner, and multi-round debate were not implemented
  - actual tool use remained `none` across the official `10`-case batch
- Accordingly, this result should be read as a packet-grounded critic intervention result, not as evidence for a retrieval-heavy or planner-driven research agent.

## Metrics caveat

- [metrics_summary_research_agent_v1.csv](/Users/jiangcanxiang/Documents/OOD_Problem/results/metrics_summary_research_agent_v1.csv) is generated successfully and now carries the correct `Perturbed Mechanical Reuse Rate = 0.2`.
- The other claim-level headline values in that file are still provisional for this arm.
- Reason: the existing annotation pipeline was originally calibrated to the frozen baseline run IDs and has not yet been expanded with `research_agent_v1`-specific run-level override coverage. As a result, the `Mean Claim Score = 1.0` output should not be treated as a substantive intervention result.
- For `task30`, the manual perturbed-pair audit is the primary result source.

## Artifact map

- Manual audit CSV: [perturbed_mechanical_reuse_v1.csv](/Users/jiangcanxiang/Documents/OOD_Problem/results/perturbed_mechanical_reuse_v1.csv)
- Manual audit note: [perturbed_pair_audit_v1.md](/Users/jiangcanxiang/Documents/OOD_Problem/results/perturbed_pair_audit_v1.md)
- Arm-specific metrics: [metrics_summary_research_agent_v1.csv](/Users/jiangcanxiang/Documents/OOD_Problem/results/metrics_summary_research_agent_v1.csv)
- Multi-stage raw runs: [research_agent_v1](/Users/jiangcanxiang/Documents/OOD_Problem/outputs/raw_agent_logs/research_agent_v1)
- Formal main raw logs: [main](/Users/jiangcanxiang/Documents/OOD_Problem/outputs/raw_agent_logs/main)
