# Presentation Outline

## Slide 1: Title

- OOD-CausalDesignBench
- Evaluating Research-Design Agents on OOD Business and Economics Causal Tasks

## Slide 2: Motivation

- Most research agents are evaluated in AI or science-heavy settings.
- Business and economics tasks stress endogenous exposure, mechanism separation, measurement credibility, and no-solution honesty.
- These are strong OOD pressures for general-purpose scientific agents.

## Slide 3: Core Question

- What exactly is a research agent weak at in anonymized business/economics causal-design tasks?
- Not paper retrieval
- Not formatting
- Specifically: evidence-bounded design reasoning

## Slide 4: Benchmark Structure

- 10 main-set cases
- 8 domains
- agent-facing vs evaluator-only separation
- `level2`, `level3`, `perturbed`, `no_solution`

Visual:
- simple pipeline figure from case construction to adjudicated labels

## Slide 5: Run Condition

- OpenClaw `benchmark_isolated`
- locally isolated
- remote-tool enabled
- one packet per run
- fresh session
- no local benchmark file access

Key message:
- the benchmark is trying to isolate reasoning quality rather than repo leakage

## Slide 6: Evaluation Pipeline

- main run: 34 successful annotated runs
- claim extraction: 285 claims
- first-pass annotation
- 21.1% second-label sample
- adjudication
- frozen label table

## Slide 7: Headline Metrics

- Mean Claim Score: `0.8193`
- Design-Evidence Inconsistency Rate: `0.2526`
- Overclaim Rate: `0.1439`
- Unsupported Design Claim Rate: `0.0842`
- No-solution Honesty Rate: `1.0000`

Visual:
- summary metric table

## Slide 8: Information Gradient

Visual:
- [information_gradient_scores.svg](/Users/jiangcanxiang/Documents/OOD_Problem/results/figures/information_gradient_scores.svg)

Takeaway:
- `level3` is only slightly better than `level2`
- more context helps a little, but not enough to eliminate boundary violations

## Slide 9: Perturbation Sensitivity

Visual:
- [perturbed_downgrade.svg](/Users/jiangcanxiang/Documents/OOD_Problem/results/figures/perturbed_downgrade.svg)

Takeaway:
- performance drops most when one key identification condition is removed
- strongest evidence that the agent struggles to recompute what remains identified

## Slide 10: Error-Type Distribution

Visual:
- [error_type_distribution.svg](/Users/jiangcanxiang/Documents/OOD_Problem/results/figures/error_type_distribution.svg)

Takeaway:
- biggest problem is not contradiction
- biggest problem is overclaim and evidence-boundary violation

## Slide 11: Hard Domains

- weakest domains:
  - political economy
  - health
  - development
- hardest key failure mode:
  - measurement error / outcome validity

Visual:
- grouped metric excerpt or case heatmap

## Slide 12: Failure Taxonomy

- unsupported operational concretization
- mechanical reuse under broken identification
- measurement credulity
- mechanism over-interpretation
- no-solution causal backsliding

## Slide 13: Failure Case A

- `C005 perturbed`
- key condition removed: untreated opportunity-side logs
- agent still claimed exposed-user `LATE`

Message:
- brittle reuse of base estimand

## Slide 14: Failure Case B

- `C014 perturbed`
- only official reports remain
- agent still claimed true corruption reduction

Message:
- outcome-validity failure

## Slide 15: Failure Case C

- `C020 no_solution`
- no credible exogenous variation remains
- agent still wrote a direct causal sentence

Message:
- local causal backsliding despite broader caution

## Slide 16: Main Conclusion

- The agent is often capable of producing a plausible-looking design report.
- Its main weakness is not missing methods; it is failure to keep claims aligned with what the packet justifies.
- Business/economics causal-design tasks are therefore an effective OOD stress test.

## Slide 17: System Recommendations

- estimand audit before final output
- perturbation-delta checklist
- outcome-validity gate
- no-solution causal guard
- mechanism-caution rule

## Slide 18: Limitations and Next Steps

- only 10 cases
- `no_solution` coverage still sparse
- some metrics are proxies because label space is coarse
- run condition is locally isolated but remote-tool enabled
- future work:
  - more cases
  - richer mechanism-specific labels
  - direct comparison across models and tool policies
