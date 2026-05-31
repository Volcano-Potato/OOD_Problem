# OOD-CausalDesignBench Research Report

## 1. Problem Definition

This project should be read as a fine-grained follow-up to the execution side of *The Ideation Bottleneck*. That paper argues that the quality gap between AI-generated and human economics research is not a single object: it can be decomposed into idea quality and execution quality, with a meaningful residual gap remaining on the execution side even after ideas are conceptually separated. The present benchmark does not try to reproduce the idea-quality side of that decomposition. Instead, it takes one especially consequential subset of execution in applied economics and business research, namely causal-design reasoning, and turns it into a structured OOD stress test.

The core claim is that business-oriented causal design tasks stress a different part of agent behavior than AI-for-science or standard ML research planning: they force the agent to reason about endogenous exposure, mechanism separation, measurement quality, and when causal identification is simply not available.

The benchmark is not trying to test whether a model can recognize the source paper. It is trying to test whether the model can stay inside the information boundary of an anonymized task packet while still proposing a valid empirical design. That makes business and economics tasks a useful OOD stress test for scientific agents that were mostly developed around AI, biomedicine, and more directly experimental workflows.

In that sense, the benchmark's contribution is not "another research-agent benchmark." It is a micro-decomposition of execution failures that are particularly important for causal credibility:

- identification mismatch
- failure to re-evaluate a design after a critical condition is broken
- mechanism claims that outrun the design
- confidence that survives the loss of credible exogenous variation

## 2. Benchmark Design

The final main set contains 10 cases spanning:

- behavioral economics
- consumer finance
- development economics
- health
- marketing
- platform economics
- political economy
- public economics

Each case is built from an evaluator-only layer and an agent-facing layer.

- Evaluator-only files include `source_packet.md`, `source_facts.md`, `gold_reference.md`, `audit.md`, and variant construction notes.
- Agent-facing files include `agent_task_level1.md`, `agent_task_level2.md`, `agent_task_level3.md`, `agent_task_perturbed.md`, and selected `agent_task_no_solution.md`.

The benchmark uses three core pressures:

1. Information gradient
   - `level1` gives only the core research setting and objective.
   - `level2` adds background plus data structure.
   - `level3` adds institutional details and threats.
2. Perturbation
   - `perturbed` variants remove one critical identification condition while keeping the rest of the setting similar.
3. No-solution honesty
   - `no_solution` variants keep the task empirically tempting but remove any credible exogenous variation.

These three pressures correspond to different slices of execution quality. The information gradient measures whether the agent can use better-structured evidence when it is available. Perturbation measures whether the agent re-checks causal logic after one identifying condition fails. No-solution variants measure whether the agent can honestly downgrade claims when a strong design is no longer defensible. The benchmark therefore focuses most heavily on the parts of execution quality most tightly tied to causal credibility, rather than trying to cover every possible dimension of paper quality equally.

The project therefore maps onto Bottleneck's execution dimensions asymmetrically rather than uniformly. In the current benchmark, `Identification Strategy` and `Mechanism and External Validity` are the strongest directly stressed dimensions; `Econometric Methodology` and `Data Quality` are partially proxied through claim-level design errors and selected failure cases; `Robustness and Sensitivity` and `Writing and Presentation` are intentionally secondary. A detailed mapping is documented in [results/bottleneck_crosswalk.md](/Users/jiangcanxiang/Documents/OOD_Problem/results/bottleneck_crosswalk.md).

## 3. Case Construction

Case construction followed a fixed pipeline:

1. prepare `source_packet`
2. extract `source_facts`
3. draft and audit `gold_reference`
4. build `level1/2/3`
5. build `perturbed`
6. build `no_solution`
7. run leakage and validity audit

This pipeline matters because the benchmark depends on a clean separation between:

- what the agent is allowed to see
- what the evaluator uses for scoring

The guiding rule for final runs was:

`one run = one case = one variant = one agent-facing packet`

## 4. Agent Run Setup

All formal runs used the local OpenClaw `benchmark_isolated` agent. The run condition was:

- locally isolated
- remote-tool enabled
- one packet at a time
- fresh session per run
- no local benchmark file access

The isolation logic was implemented through external orchestration scripts rather than asking the agent to browse the repo:

- [run_isolated_packet.sh](/Users/jiangcanxiang/Documents/OOD_Problem/scripts/run_isolated_packet.sh)
- [run_batch_isolated.sh](/Users/jiangcanxiang/Documents/OOD_Problem/scripts/run_batch_isolated.sh)
- [postprocess_openclaw_run.py](/Users/jiangcanxiang/Documents/OOD_Problem/scripts/postprocess_openclaw_run.py)

After the Task 26 extension, the main matrix contained 44 successful annotated runs:

- 10 `level1`
- 10 `level2`
- 10 `level3`
- 10 `perturbed`
- 4 `no_solution`

There were also 2 historical aborted main-run manifest rows retained for audit purposes.

## 5. Annotation Protocol

The evaluation pipeline after running the agent was:

1. extract claims from the `Claim-Evidence Table`
2. perform first-pass annotation
3. sample 21.1% of claims for second labeling
4. adjudicate disagreements
5. freeze `annotations/adjudicated_labels.csv`

Final annotation totals:

- total claims: `370`
- second-label sample: `78`
- simple agreement on `human_judgment`: `97.4%`
- simple agreement on `error_type`: `97.4%`
- explicit adjudicated disagreements: `2`

Final label counts:

- `supported`: `271`
- `partially_supported`: `51`
- `unsupported`: `41`
- `contradicted`: `7`

## 6. Metrics

All main metrics are derived from [results/metrics_summary.csv](/Users/jiangcanxiang/Documents/OOD_Problem/results/metrics_summary.csv) and documented in [results/metrics_summary.md](/Users/jiangcanxiang/Documents/OOD_Problem/results/metrics_summary.md).

The most important headline numbers are:

- Mean Claim Score: `0.8014`
- Design-Evidence Inconsistency Rate: `0.2676`
- Unsupported Design Claim Rate: `0.1108`
- Contradiction Rate: `0.0189`
- Overclaim Rate: `0.1378`
- Critical Design Omission Rate (proxy): `0.0432`
- Mechanism Confounding Rate (proxy): `0.2914`
- All `4/4` tested `no_solution` runs avoided supported causal claims under the current heuristic.
- `perturbed` mechanical reuse: `9/10`

After Task 26, the information-gradient comparison is no longer limited to `level2` vs `level3`; it now spans `level1`, `level2`, and `level3`.

## 7. Results

### 7.1 Overall Pattern

The agent is not failing mainly on format compliance. It is failing on execution discipline under constrained causal-design information. The strongest repeated failure is not “cannot think of a design,” but “turns a plausible design idea into a claim stronger than the packet supports.”

This shows up directly in the error profile:

- `Overclaim` is the single largest non-`none` error class at `41` claims.
- `Unsupported Claim` and `Contradiction` are smaller but more severe when they appear.

### 7.2 Information Gradient

Core figure:
- [information_gradient_scores.svg](/Users/jiangcanxiang/Documents/OOD_Problem/results/figures/information_gradient_scores.svg)

Run-level means:

- `level1`: `0.6902`
- `level2`: `0.8363`
- `level3`: `0.8421`

The key pattern is not “more information always helps.” It is more specific:

- the jump from `level1` to `level2` is large
- the jump from `level2` to `level3` is minimal

This means that structured data and design information matter, but additional explicit threat hints did not produce a meaningful further improvement in this round. The dominant weakness is therefore not simply “lack of context.” It is how the agent interprets and constrains claims once context is present.

### 7.3 Perturbation Sensitivity

Core figure:
- [perturbed_downgrade.svg](/Users/jiangcanxiang/Documents/OOD_Problem/results/figures/perturbed_downgrade.svg)

Average `perturbed` run score is `0.7634`, clearly below both `level2` and `level3`. The paired perturbation audit sharpens this result: `9/10` perturbed cases show mechanical reuse under broken identification. In other words, the agent often does not fully re-evaluate which estimand remains defensible after one critical identifying condition is removed.

The strongest perturbed collapses occur in:

- `C014 perturbed`: `0.375`
- `C005 perturbed`: `0.5714`

These are exactly the settings where outcome validity or exposure-counterfactual construction was explicitly broken.

### 7.4 Domain and Failure-Mode Heterogeneity

Grouped outputs are in [grouped_metrics.csv](/Users/jiangcanxiang/Documents/OOD_Problem/results/grouped_metrics.csv).

The weakest domains in this round are:

- `political_econ`
  - mean claim score: `0.6974`
  - inconsistency rate: `0.3684`
- `health`
  - mean claim score: `0.7209`
  - inconsistency rate: `0.3721`
- `development`
  - mean claim score: `0.7778`
  - inconsistency rate: `0.3333`

By key failure mode, the hardest category is:

- `measurement_error`
  - mean claim score: `0.7099`
  - inconsistency rate: `0.3704`

This is consistent with the qualitative finding that the agent struggles when measurement quality is part of identification rather than a minor caveat.

### 7.5 No-solution Behavior

The run-level no-solution honesty result should be stated cautiously: all `4/4` tested `no_solution` runs avoided supported or partially supported causal claims under the current heuristic.

That is encouraging, but it is not the whole story. One of the strongest qualitative lessons from Task 23 is that a run can still emit a direct causal sentence that gets adjudicated as `contradicted`, even if the run-level heuristic marks it broadly cautious. The no-solution result is therefore better interpreted as:

- strong at global downgrading
- still vulnerable to local causal backsliding

### 7.6 Core Figures

Three core figures for the report are:

1. [information_gradient_scores.svg](/Users/jiangcanxiang/Documents/OOD_Problem/results/figures/information_gradient_scores.svg)
2. [error_type_distribution.svg](/Users/jiangcanxiang/Documents/OOD_Problem/results/figures/error_type_distribution.svg)
3. [perturbed_downgrade.svg](/Users/jiangcanxiang/Documents/OOD_Problem/results/figures/perturbed_downgrade.svg)

An additional diagnostic figure is:

4. [case_error_heatmap.svg](/Users/jiangcanxiang/Documents/OOD_Problem/results/figures/case_error_heatmap.svg)

## 8. Failure Cases

The qualitative failure analysis is in [results/failure_cases.md](/Users/jiangcanxiang/Documents/OOD_Problem/results/failure_cases.md). The five representative failures show a coherent pattern:

- `C001 level2`: unsupported operational concretization
- `C005 perturbed`: mechanical reuse under broken identification
- `C014 perturbed`: measurement credulity
- `C016 level2`: mechanism over-interpretation from limited evidence
- `C020 no_solution`: causal backsliding under no-solution conditions

The most important conclusion from these examples is that the agent's weakness is not primarily lack of methods. It is failure to maintain a stable mapping between:

- what the packet supports
- what the design requires
- what the final claim table is allowed to say

## 9. Limitations

This benchmark is useful, but it is still limited.

1. Case count
   - The main set has 10 cases, which is enough for structured diagnosis but not enough to claim exhaustive coverage of all business/economics causal-design settings.

2. Variant coverage
   - `no_solution` is intentionally sparse at 4 runs, so its estimates are lower-variance descriptively than inferentially robust.

3. Annotation subjectivity
   - Task 21 adjudication improves reliability, but the label space still depends on human interpretation of overclaim strength and evidentiary scope.

4. Metric granularity
   - Some Task 22 metrics are explicitly marked as proxies because the annotation schema does not contain omission-only or mechanism-only labels.

5. Run condition
   - The formal condition is locally isolated but remote-tool enabled.
   - This is a realistic agent condition, but it is not the same thing as strict closed-book evaluation.

6. Tool-use ambiguity
   - The benchmark records the formal tool-enabled environment, but the main evaluation story here is primarily about agent reasoning and claim calibration, not about a detailed decomposition of external retrieval benefits.

7. Exploratory pairwise extension
   - An APE-style pairwise design-memo comparison was added as an exploratory extension, but its current protocol strongly favors agent memos.
   - Because that result conflicts with the benchmark's claim-level adjudication, it is better interpreted as evidence of protocol sensitivity under memo compression and same-family judging than as a reversal of the main benchmark conclusion.

## 10. Recommendations

The benchmark suggests five concrete system improvements for research-design agents:

1. Estimand audit before final answer
   - force the agent to state what is randomized, what is merely observed, and which causal claims are still admissible.

2. Perturbation delta check
   - require the agent to name the one condition that changed and to list which base claims must be weakened or deleted.

3. Outcome-validity gate
   - when the main outcome becomes indirect or administratively contaminated, block claims about the latent construct.

4. No-solution causal guard
   - when the packet explicitly removes credible identification, the final claim table should reject direct causal wording.

5. Mechanism caution rule
   - when mechanism evidence is secondary, selected, or noisy, the agent should enumerate multiple explanations rather than commit to one.

## 11. Bottom Line

Business and economics causal-design tasks are a useful OOD benchmark for research agents because they stress exactly the behaviors that generic scientific-assistant evaluation often under-measures:

- evidence-boundary discipline
- identification downgrading
- measurement-aware reasoning
- mechanism restraint
- honesty under no-solution conditions

Under this benchmark, the agent is often competent at producing a formal design report, but noticeably less reliable at keeping its claims aligned with what the packet actually justifies. That is the central weakness this benchmark surfaces.
