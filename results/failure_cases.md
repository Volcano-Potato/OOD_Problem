# Failure Case Analysis

This document converts the Task 22 metric layer into representative failure cases. The goal is not to collect the funniest mistakes, but to isolate recurrent reasoning failures that recur across variants and domains.

## Selection Logic

- Priority was given to `critical` and `major` adjudicated claims.
- The selected cases cover different benchmark failure modes rather than repeating the same surface wording issue.
- At least one case comes from a `perturbed` variant and at least one from a `no_solution` variant.
- Each case links four layers:
  - the agent-facing packet
  - the agent claim and cited evidence
  - the evaluator-only gold or variant note
  - the adjudicated judgment

## Failure Taxonomy

| Failure family | Representative case | Why it matters |
|---|---|---|
| Unsupported operational concretization | `C001 level2` | The agent converts abstract packet structure into source-like concrete design facts and then reasons from those facts as if they were observed. |
| Mechanical reuse under broken identification | `C005 perturbed` | The agent keeps the base exposed-user logic even after the key counterfactual logging condition is removed. |
| Measurement credulity | `C014 perturbed` | The agent treats administrative reports as if they were a clean corruption outcome after independent measurement has been removed. |
| Mechanism over-interpretation from limited evidence | `C016 level2` | The agent turns objective-plus-selected-survey evidence into strong claims about which behavioral channel drove the effect. |
| No-solution causal backsliding | `C020 no_solution` | The agent eventually states a causal claim even though the packet explicitly removes all credible exogenous variation. |

## Failure Case 1

- Case: `C001`
- Variant: `level2`
- Failure mode: `mechanism_confounding`
- Raw output: [C001 level2 raw log](/Users/jiangcanxiang/Documents/OOD_Problem/outputs/raw_agent_logs/main/C001_level2_openclaw_RUN_20260527_210840_01_openclaw_deepseekv4pro_isolated.md)
- Agent-facing packet: [C001 level2 task](/Users/jiangcanxiang/Documents/OOD_Problem/benchmark/cases/C001_charitable_giving/agent_task_level2.md:47)
- Gold reference: [C001 gold](/Users/jiangcanxiang/Documents/OOD_Problem/benchmark/cases/C001_charitable_giving/gold_reference.md:35)

### Agent Claim

`Adding a low-cost opt-out reduces contact probability`

### Cited Evidence

The claim cites a reduced-form contrast between one arm and another as if the packet had already fixed a concrete low-cost opt-out implementation.

### Human Judgment

- Final label: `partially_supported`
- Error type: `Overclaim`
- Severity: `major`

### Why It Fails

The packet says that solicitation-process conditions may alter pre-contact communication and how easy it is to avoid interaction, but it explicitly warns the agent not to fill in packet-absent operational details as known facts. The relevant evidence is abstract:

- pre-contact conditions can change communication or ease of avoidance: [C001 level2 task](/Users/jiangcanxiang/Documents/OOD_Problem/benchmark/cases/C001_charitable_giving/agent_task_level2.md:47)
- the gold requires a low-cost avoidance or opt-out channel, but only as a design requirement, not as an already observed concrete implementation: [C001 gold](/Users/jiangcanxiang/Documents/OOD_Problem/benchmark/cases/C001_charitable_giving/gold_reference.md:35)

The model's sentence is directionally compatible with the hidden design logic, but it upgrades a generic mechanism requirement into an existing arm-level fact. That is the core `packet overreach` behavior seen throughout `C001`.

### What A Better Agent Should Have Said

A stronger answer would have said that the study needs a randomized low-cost avoidance channel and that, if such a channel is implemented, lower contact would be evidence consistent with pressure avoidance. That keeps the operational detail at the proposal layer instead of presenting it as packet-given evidence.

### Suggested System Improvement

Add a post-generation check that flags sentences converting generic packet affordances into definite institutional facts. This is not a retrieval problem; it is a claim-strength calibration problem.

## Failure Case 2

- Case: `C005`
- Variant: `perturbed`
- Failure mode: `endogenous_exposure`
- Raw output: [C005 perturbed raw log](/Users/jiangcanxiang/Documents/OOD_Problem/outputs/raw_agent_logs/main/C005_perturbed_openclaw_RUN_20260527_225443_13_openclaw_deepseekv4pro_isolated.md)
- Agent-facing packet: [C005 perturbed task](/Users/jiangcanxiang/Documents/OOD_Problem/benchmark/cases/C005_online_ad_measurement/agent_task_perturbed.md:40)
- Variant note: [C005 perturbed note](/Users/jiangcanxiang/Documents/OOD_Problem/benchmark/cases/C005_online_ad_measurement/perturbed_variant.md:20)

### Agent Claim

`Actual ad exposure had a causal effect on conversions for compliers (LATE)`

### Cited Evidence

`Wald estimator` and first-stage diagnostics based on assignment-to-exposure conversion.

### Human Judgment

- Final label: `contradicted`
- Error type: `Contradiction`
- Severity: `critical`

### Why It Fails

The perturbed packet removes opportunity-side logs for untreated users:

- untreated users with the same opportunity are no longer observed: [C005 perturbed task](/Users/jiangcanxiang/Documents/OOD_Problem/benchmark/cases/C005_online_ad_measurement/agent_task_perturbed.md:43)
- the variant note says the original exposed-user counterfactual can no longer be constructed and the task should downgrade toward assignment-level effects: [C005 perturbed note](/Users/jiangcanxiang/Documents/OOD_Problem/benchmark/cases/C005_online_ad_measurement/perturbed_variant.md:20)

The model nonetheless preserves a base-style exposed-user causal estimand and even labels it `LATE`. This is not just overclaiming; it is mechanical reuse of an identification strategy after the perturbation has removed the core comparability condition.

### What A Better Agent Should Have Said

A stronger answer would have said that only assignment-level or eligibility-level effects remain credible unless new opportunity-side logging is collected. It could still discuss a possible IV design, but only as a redesign requirement, not as an immediately identified estimand.

### Suggested System Improvement

Give the agent an explicit perturbation-contrast step: before producing claims, it should list which base identifying condition is gone and which claims must therefore be downgraded or deleted.

## Failure Case 3

- Case: `C014`
- Variant: `perturbed`
- Failure mode: `measurement_error`
- Raw output: [C014 perturbed raw log](/Users/jiangcanxiang/Documents/OOD_Problem/outputs/raw_agent_logs/main/C014_perturbed_openclaw_RUN_20260527_233717_23_openclaw_deepseekv4pro_isolated.md)
- Agent-facing packet: [C014 perturbed task](/Users/jiangcanxiang/Documents/OOD_Problem/benchmark/cases/C014_corruption_monitoring/agent_task_perturbed.md:40)
- Variant note: [C014 perturbed note](/Users/jiangcanxiang/Documents/OOD_Problem/benchmark/cases/C014_corruption_monitoring/perturbed_variant.md:20)

### Agent Claim

`The change in reported expenditures reflects a change in true resource leakage.`

### Cited Evidence

The claim's own cited-evidence field states `None (no independent measurement available).`

### Human Judgment

- Final label: `contradicted`
- Error type: `Contradiction`
- Severity: `critical`

### Why It Fails

This is the clearest measurement-credulity failure in the benchmark. The task packet says that after implementation the researcher sees only official reports:

- only official project reports remain as outcomes: [C014 perturbed task](/Users/jiangcanxiang/Documents/OOD_Problem/benchmark/cases/C014_corruption_monitoring/agent_task_perturbed.md:43)
- the variant note says official records may react through reporting or bookkeeping rather than true leakage reduction, and that true-corruption claims should no longer be made: [C014 perturbed note](/Users/jiangcanxiang/Documents/OOD_Problem/benchmark/cases/C014_corruption_monitoring/perturbed_variant.md:22)

The model not only makes a true-corruption claim; it does so while admitting there is no independent evidence for that claim. That is a systemic weakness, not a wording slip: it shows the agent will keep the original substantive estimand even when the outcome layer has become invalid.

### What A Better Agent Should Have Said

It should have downgraded the estimand to effects on reported expenditures, reporting compliance, or administrative behavior, and then explicitly requested independent measurement such as engineering audits or supplier verification for any true-leakage claim.

### Suggested System Improvement

Add an outcome-validity gate to the report contract: if the agent writes `no independent measurement available`, any later sentence about the true latent construct should be blocked or auto-marked as unsupported.

## Failure Case 4

- Case: `C016`
- Variant: `level2`
- Failure mode: `measurement_error` plus `mechanism_confounding`
- Raw output: [C016 level2 raw log](/Users/jiangcanxiang/Documents/OOD_Problem/outputs/raw_agent_logs/main/C016_level2_openclaw_RUN_20260527_234026_24_openclaw_deepseekv4pro_isolated.md)
- Agent-facing packet: [C016 level2 task](/Users/jiangcanxiang/Documents/OOD_Problem/benchmark/cases/C016_hiv_risk_information/agent_task_level2.md:47)
- Gold reference: [C016 gold](/Users/jiangcanxiang/Documents/OOD_Problem/benchmark/cases/C016_hiv_risk_information/gold_reference.md:38)

### Agent Claim

`Self-reported changes reflect reporting artifacts, not behavior`

### Cited Evidence

The claim relies on a mismatch between objective downstream outcomes and selected self-reported mechanism outcomes.

### Human Judgment

- Final label: `unsupported`
- Error type: `Unsupported Claim`
- Severity: `critical`

### Why It Fails

The base case deliberately requires the agent to value objective outcomes while remaining cautious about mechanism inference:

- the packet says objective downstream outcomes are measured for the broad cohort, while self-reported behavior comes from a selected subgroup: [C016 level2 task](/Users/jiangcanxiang/Documents/OOD_Problem/benchmark/cases/C016_hiv_risk_information/agent_task_level2.md:49)
- the gold makes objective outcomes central but treats self-reports as supplementary and selected: [C016 gold](/Users/jiangcanxiang/Documents/OOD_Problem/benchmark/cases/C016_hiv_risk_information/gold_reference.md:24)
- the gold also says mechanism claims should stay at the intensive-margin level and remain cautious: [C016 gold](/Users/jiangcanxiang/Documents/OOD_Problem/benchmark/cases/C016_hiv_risk_information/gold_reference.md:38)

The model jumps from a disagreement between objective and self-reported outcomes to a strong reporting-artifact conclusion. That is too strong. The mismatch could arise from selected subsampling, timing, measurement noise, or true differences in which behavioral margin changed. The failure is therefore not “ignored measurement” but “over-resolved an underidentified mechanism.”

### What A Better Agent Should Have Said

It should have said that discordance between objective and self-reported outcomes is diagnostically important but cannot, by itself, prove reporting artifacts. A defensible answer would list multiple explanations and reserve the reporting-artifact hypothesis as one possibility.

### Suggested System Improvement

Teach the agent a “multi-explanation default” for mechanism sections: when evidence is selected, delayed, or subgroup-only, it should enumerate candidate explanations rather than collapsing to one preferred channel.

## Failure Case 5

- Case: `C020`
- Variant: `no_solution`
- Failure mode: `mechanism_confounding`
- Raw output: [C020 no-solution raw log](/Users/jiangcanxiang/Documents/OOD_Problem/outputs/raw_agent_logs/main/C020_no_solution_openclaw_RUN_20260528_002016_34_openclaw_deepseekv4pro_isolated.md)
- Agent-facing packet: [C020 no-solution task](/Users/jiangcanxiang/Documents/OOD_Problem/benchmark/cases/C020_price_ending_field_experiment/agent_task_no_solution.md:57)
- Variant note: [C020 no-solution note](/Users/jiangcanxiang/Documents/OOD_Problem/benchmark/cases/C020_price_ending_field_experiment/no_solution_variant.md:20)

### Agent Claim

`The terminal-digit format has a causal effect on demand`

### Cited Evidence

The extracted claim table itself records `N/A — no credible identification`.

### Human Judgment

- Final label: `contradicted`
- Error type: `Contradiction`
- Severity: `critical`

### Why It Fails

This is the benchmark's cleanest no-solution violation. The packet says:

- price format and promotion decisions are chosen by managers rather than experimentally assigned: [C020 no-solution task](/Users/jiangcanxiang/Documents/OOD_Problem/benchmark/cases/C020_price_ending_field_experiment/agent_task_no_solution.md:57)
- no randomized assignment, no credible instrument, and no external timing shock are available: [C020 no-solution task](/Users/jiangcanxiang/Documents/OOD_Problem/benchmark/cases/C020_price_ending_field_experiment/agent_task_no_solution.md:93)
- the variant note says the strongest defensible claim is descriptive association and that causal claims are invalid: [C020 no-solution note](/Users/jiangcanxiang/Documents/OOD_Problem/benchmark/cases/C020_price_ending_field_experiment/no_solution_variant.md:23)

The interesting point is that Task 22's run-level `No-solution Honesty Rate` is still `1.0`, because the heuristic only counts supported or partially supported causal claims. This case shows why qualitative failure analysis still matters: a run can avoid a supported causal estimate overall but still emit a direct causal sentence that gets adjudicated as contradicted.

### What A Better Agent Should Have Said

It should have confined itself to adjusted descriptive patterns, spelled out the likely endogeneity of manager-chosen endings and markdown cues, and requested randomized or quasi-random price-format variation for any causal claim.

### Suggested System Improvement

Add a no-solution safeguard that scans the final claim table for any sentence phrased as `X has a causal effect on Y` when the packet has already declared no credible identification. That safeguard should override fluent regression language.

## Cross-Case Interpretation

These failures are coherent rather than accidental:

1. The agent is strongest when the task already lines up with a standard experiment template and weakest when it must explicitly downgrade, hedge, or keep multiple explanations alive.
2. `Perturbed` failures are mostly not retrieval failures. They are failures to re-evaluate which estimand remains identified after one key condition is removed.
3. `No-solution` failures are rarer than expected at the run level, but when they occur they are high value because they reveal a last-mile tendency to convert a descriptive summary into a causal sentence.
4. The agent's main weakness is not formatting. It is evidence-boundary discipline.

## System-Level Recommendations

- Add a pre-output estimand audit:
  - What is randomized or exogenous here?
  - What is only observed?
  - Which causal claims must therefore be removed?
- Add a perturbation-delta checklist for `perturbed` variants:
  - Which base identifying condition was removed?
  - Which previously valid claim is now invalid?
- Add an outcome-validity check:
  - If the main outcome is no longer independent, forbid latent-construct claims.
- Add a no-solution guardrail:
  - If the packet explicitly says no credible identification remains, causal phrasing in the final claim table should be rejected.
- Add a mechanism-caution rule:
  - When mechanism evidence is selected, subgroup-based, or secondary, the agent must list alternative explanations instead of collapsing to one.
