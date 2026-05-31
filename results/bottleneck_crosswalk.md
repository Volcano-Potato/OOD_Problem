# Bottleneck Execution-Dimension Crosswalk

## Purpose

This note explains how the benchmark's current evidence maps onto the execution-quality dimensions used in *The Ideation Bottleneck*.

The goal is not to claim that this repository fully reproduces Bottleneck's six-dimension scoring scheme. Instead, the goal is to show which parts of the execution side are directly stressed by this benchmark, which parts are only partially proxied, and which parts are intentionally secondary.

The central design choice is:

> This benchmark prioritizes the execution dimensions most consequential for causal credibility in OOD business and economics research-design tasks, especially identification, mechanism reasoning, and claim calibration under broken designs.

## Crosswalk Table

| Bottleneck execution dimension | Benchmark evidence | Representative metric / artifact | Scope note |
|---|---|---|---|
| Identification Strategy | Information gradient, `perturbed`, `no_solution`, paired reuse audit | `Level 1/2/3 Mean Run Score`, `Perturbed Mean Run Score`, `Perturbed Mechanical Reuse Rate`, `No-solution Honesty Rate` | Core. This is the benchmark's strongest direct measurement area. |
| Econometric Methodology | Claim-level design errors and invalid causal language | `Unsupported Design Claim Rate`, `Contradiction Rate`, adjudicated claim table | Partial. The benchmark focuses on design-level econometric reasoning rather than estimator implementation details. |
| Robustness and Sensitivity | Limited direct coverage | selected claims and failure notes only | Secondary. The benchmark does not treat robustness as a headline dimension. |
| Data Quality | Dirty outcomes, weak measurement, missing untreated opportunity logs, contaminated proxies | `measurement_error` grouped results, `C014 perturbed`, `C016 level2`, selected failure cases | Partial but meaningful. Data quality is measured insofar as it interacts with causal credibility. |
| Mechanism and External Validity | Mechanism over-interpretation, mechanism confounding, unsupported mechanism claims | `Mechanism Confounding Rate (proxy)`, failure cases, overclaim patterns | Core. This is one of the benchmark's most important stress points. |
| Writing and Presentation | Output-contract compliance and report structure | contract adherence, raw-log review | Out of scope as a primary research contribution. Writing quality is observed, but not treated as a major benchmark target. |

## Direct Measurement vs Proxy Measurement

### Directly stressed dimensions

The benchmark most directly measures:

- `Identification Strategy`
- `Mechanism and External Validity`

This is because the benchmark was explicitly constructed around:

- information availability changes (`level1 -> level2 -> level3`)
- broken-identification stress tests (`perturbed`)
- strong-claim-without-identification stress tests (`no_solution`)

These structures make it possible to observe whether the agent:

- identifies what variation supports the causal claim
- notices when a key identifying condition disappears
- weakens the estimand or the final claim when it should

### Proxy-measured dimensions

The benchmark only partially or indirectly measures:

- `Econometric Methodology`
- `Data Quality`

The current label schema is strongest at claim-level design reasoning. It is weaker at capturing:

- estimator-level sophistication
- standard-error choices
- specification-level corrections

Similarly, data quality is mostly observed when it becomes part of identification or outcome validity, not as a standalone auditing dimension.

### Intentionally secondary dimensions

The benchmark treats:

- `Robustness and Sensitivity`
- `Writing and Presentation`

as secondary.

This is a deliberate design choice rather than a missing feature. The benchmark follows Bottleneck's own implication that the most informative execution failures for current AI economics systems are not necessarily the same across all dimensions. Here, the emphasis is on the parts of execution most tightly linked to causal credibility under OOD applied-economics conditions.

## Why Identification and Mechanism Are Prioritized

According to *The Ideation Bottleneck*, the largest execution-side weakness is `Mechanism and External Validity`, with large additional gaps in `Data Quality`, `Identification Strategy`, and `Econometric Methodology`, while `Robustness and Sensitivity` shows no meaningful gap. That pattern supports a selective benchmarking strategy rather than an equal-weight strategy.

This repository follows that implication:

- it gives high weight to whether the agent can preserve identification logic when conditions change
- it gives high weight to whether mechanism claims remain commensurate with the design
- it does not spend its main evaluation budget on generic robustness boilerplate

In short, the benchmark is not trying to be a full paper-quality evaluator. It is trying to be a focused execution-quality probe for causal-design reasoning.

## Practical Interpretation

The main empirical results can therefore be read through the Bottleneck lens as follows:

- `level1 -> level2` improvement:
  - better structured evidence helps identification reasoning
- `level2 -> level3` near-flatness:
  - explicit threat hints alone do not materially close the execution gap
- `9/10` perturbed mechanical reuse:
  - strong evidence of weak identification vigilance under broken conditions
- `4/4` tested no-solution honesty:
  - evidence that global claim downgrading is possible, though not guaranteed to prevent local causal backsliding
- high `Overclaim` and non-trivial `Mechanism Confounding Rate`:
  - evidence that mechanism reasoning often outruns what the packet supports

## Summary

The benchmark's cleanest contribution relative to Bottleneck is:

- not a new decomposition of idea versus execution
- but a micro-decomposition of the execution side into observable OOD causal-design failures

That is the sense in which this repository should be read as a downstream diagnostic layer for the execution residual identified by *The Ideation Bottleneck*.
