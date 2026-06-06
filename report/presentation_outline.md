# Presentation Outline

## Slide 1: Title

- OOD-CausalDesignBench
- Micro-decomposing the execution side of research-agent failure on OOD business and economics causal tasks

## Slide 2: Motivation

- *The Ideation Bottleneck* separates economics-research quality into idea quality and execution quality.
- This project follows the execution side only.
- Business and economics tasks stress endogenous exposure, mechanism separation, measurement credibility, and no-solution honesty.
- These are strong OOD pressures for general-purpose scientific agents.

## Slide 3: Core Question

- After holding the research idea side fixed, what exactly does a research agent fail at on anonymized business/economics causal-design tasks?
- Not paper retrieval
- Not formatting
- Specifically: evidence-bounded execution of causal-design reasoning

## Slide 4: Benchmark Structure

- 10 main-set cases
- 8 domains
- agent-facing vs evaluator-only separation
- `level1`, `level2`, `level3`, `perturbed`, `no_solution`

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

- main run: 44 successful annotated runs
- claim extraction: 370 claims
- first-pass annotation
- 21.1% second-label sample
- adjudication
- frozen label table

## Slide 7: Headline Metrics

- Mean Claim Score: `0.8014`
- Design-Evidence Inconsistency Rate: `0.2676`
- Overclaim Rate: `0.1378`
- Unsupported Design Claim Rate: `0.1108`
- `8/10` tested no-solution runs avoided supported causal claims

Visual:
- summary metric table

## Slide 8: Information Gradient

Visual:
- [information_gradient_scores.svg](/Users/jiangcanxiang/Documents/OOD_Problem/results/figures/information_gradient_scores.svg)

Takeaway:
- large jump from `level1` to `level2`
- almost no further gain from `level2` to `level3`
- structured data information helps; extra explicit threat hints do not meaningfully close the execution gap

## Slide 9: Perturbation Sensitivity

Visual:
- [perturbed_downgrade.svg](/Users/jiangcanxiang/Documents/OOD_Problem/results/figures/perturbed_downgrade.svg)

Takeaway:
- performance drops most when one key identification condition is removed
- paired audit result after baseline re-audit: `1/10` show clear mechanical reuse
- strongest remaining baseline example is `C005`, not a broad 9-case pattern

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

## Slide 16: Intervention Ladder

- baseline `perturbed` mechanical reuse: `1/10`
- `research_agent_v1`: `1/10`
- `research_agent_v2_search`: `0/10`
- `research_agent_v3_planner_debate`: `0/10`

Visual:
- one compact ablation table or step-down chart

Takeaway:
- `v1` is not a headline gain over the re-audited baseline
- `v2` is the strongest practical intervention arm
- `v3` adds process structure but no extra headline gain over `v2`

## Slide 17: Why Stop At v2

- `v2` already reaches `0/10` mechanical reuse
- `v3` also reaches `0/10`, but is more expensive
- average retrieval tool calls:
  - `v2 = 16.7`
  - `v3 = 19.7`
- average pipeline duration:
  - `v2 = 789.9s`
  - `v3 = 899.7s`

Message:
- default recommendation = `research_agent_v2_search`
- `v3` is better treated as a diagnostic / ablation arm

## Slide 18: Main Conclusion

- The agent is often capable of producing a plausible-looking design report.
- Its main weakness is not missing methods; it is failure to keep identification logic, measurement assumptions, and final claims aligned with what the packet justifies.
- Business/economics causal-design tasks are therefore an effective OOD execution stress test.

## Slide 19: System Recommendations

- estimand audit before final output
- perturbation-delta checklist
- outcome-validity gate
- no-solution causal guard
- mechanism-caution rule

## Slide 20: Limitations and Next Steps

- only 10 cases
- `no_solution` now covers the full 10-case main set, but the honesty metric remains heuristic
- some metrics are proxies because label space is coarse
- run condition is locally isolated but remote-tool enabled
- intervention-arm claim-level metrics are still secondary to paired manual audit
- future work:
  - `task32` complete: no-solution coverage expanded to the full main set
  - writing/presentation polish and archive freeze
  - only revisit new agent arms if a new benchmark slice shows residual failures beyond `v2`
