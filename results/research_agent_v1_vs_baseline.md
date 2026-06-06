# research_agent_v1 vs baseline

## Scope

- Intervention arm: `research_agent_v1`
- Evaluation subset: `10` `perturbed` cases (`C001`, `C002`, `C004`, `C005`, `C008`, `C010`, `C014`, `C016`, `C019`, `C020`)
- Baseline comparator: frozen `benchmark_isolated` Level 2 vs perturbed paired audit in [perturbed_mechanical_reuse.csv](/Users/jiangcanxiang/Documents/OOD_Problem/results/perturbed_mechanical_reuse.csv)
- Smoke-only artifact handling: the provisional bridged `C001` smoke run was removed from `outputs/run_manifest.csv` before downstream analysis so that this comparison uses only the 10 official batch runs

## Headline

- Baseline `perturbed mechanical reuse`: `1/10`
- `research_agent_v1` `perturbed mechanical reuse`: `1/10`
- Absolute change: `0/10 = 0.00`

Interpretation:
After re-auditing both the frozen baseline and the `v1` raw reports, `task30` no longer supports a "v1 beats baseline" headline on paired mechanical reuse, but it also no longer underperforms the re-audited baseline. On this metric, `v1` matches baseline at `1/10`, with `C005` remaining the only clear reuse case.

## Case-by-case transition

| Case | Baseline | research_agent_v1 | Transition |
|---|---:|---:|---|
| `C001` | `no` | `no` | both downgrade away from the broken base decomposition |
| `C002` | `no` | `no` | both abandon clean selection-versus-incentive separation |
| `C004` | `no` | `no` | both drop the causal design and stay descriptive |
| `C005` | `yes` | `yes` | residual reuse via supplementary IV/LATE on actual exposure |
| `C008` | `no` | `no` | both downgrade away from the clean salience estimand; v1 keeps only a heavily caveated fallback contrast |
| `C010` | `no` | `no` | both narrow to bundle ITT; no procrastination identification |
| `C014` | `no` | `no` | both narrow to reporting-side effects; no true corruption claim |
| `C016` | `no` | `no` | both switch to bounds or descriptive analysis |
| `C019` | `no` | `no` | remained a descriptive fallback |
| `C020` | `no` | `no` | both abandon standalone format effect and reframe around bundle analysis |

## Auxiliary observations

- Stage 4 critic recognized the perturbed-condition dependency in `10/10` official batch runs.
- The pipeline still often helps force explicit downgrade to descriptive, bounded, or re-targeted estimands.
- But paired-audit headline improvement is not present once the baseline is re-audited.
- Residual failure is concentrated in cases where the final memo still preserves a secondary causal candidate from the base design instead of dropping it completely.
- The remaining reuse case is:
  - `C005`: actual-exposure IV/LATE retained as a caveated supplementary estimand

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

- [metrics_summary_research_agent_v1.csv](/Users/jiangcanxiang/Documents/OOD_Problem/results/metrics_summary_research_agent_v1.csv) is generated successfully and carries `Perturbed Mechanical Reuse Rate = 0.1`.
- The other claim-level headline values in that file are still provisional for this arm.
- Reason: the existing annotation pipeline was originally calibrated to the frozen baseline run IDs and has not yet been expanded with `research_agent_v1`-specific run-level override coverage. As a result, the `Mean Claim Score = 1.0` output should not be treated as a substantive intervention result.
- For `task30`, the manual perturbed-pair audit remains the primary result source, but it should now be read against the re-audited baseline rather than the older `9/10` headline.

## Artifact map

- Manual audit CSV: [perturbed_mechanical_reuse_v1.csv](/Users/jiangcanxiang/Documents/OOD_Problem/results/perturbed_mechanical_reuse_v1.csv)
- Manual audit note: [perturbed_pair_audit_v1.md](/Users/jiangcanxiang/Documents/OOD_Problem/results/perturbed_pair_audit_v1.md)
- Arm-specific metrics: [metrics_summary_research_agent_v1.csv](/Users/jiangcanxiang/Documents/OOD_Problem/results/metrics_summary_research_agent_v1.csv)
- Multi-stage raw runs: [research_agent_v1](/Users/jiangcanxiang/Documents/OOD_Problem/outputs/raw_agent_logs/research_agent_v1)
- Formal main raw logs: [main](/Users/jiangcanxiang/Documents/OOD_Problem/outputs/raw_agent_logs/main)
