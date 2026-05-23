# Benchmark Scope

## One-Sentence Definition

OOD-CausalDesignBench evaluates whether OpenClaw / DeepScientist-based scientific agents can transform anonymized business and economics research settings into defensible causal research designs without producing unsupported causal, identification, mechanism, or statistical design claims.

中文定义：OOD-CausalDesignBench 评估基于 OpenClaw / DeepScientist 的科研 Agent 在商科、经济学、营销学等 OOD 场景中，能否基于匿名研究任务包提出可辩护的因果研究设计，并避免生成没有证据支撑的因果识别、机制解释或模型设计结论。

## Research Questions

- RQ1: Given an anonymized business/economics research case, can the agent correctly identify the treatment or exposure, outcome, unit of analysis, estimand, and target mechanism?
- RQ2: Can the agent identify the main causal threats implied by the data structure and institutional setting, such as selection, endogenous exposure, timing endogeneity, spillover, attrition, measurement error, or non-compliance?
- RQ3: Can the agent propose an empirical or experimental design whose assumptions match the available data, assignment mechanism, institutional details, and outcome measurement process?
- RQ4: Does the agent overclaim by turning descriptive, correlational, or weakly identified evidence into strong causal, mechanism, or policy claims?
- RQ5: Does the agent improve when given richer information from Level 1 to Level 2 to Level 3, or does it still produce generic/template designs?
- RQ6: When a key identification condition is perturbed or removed, does the agent weaken or revise its design, or does it mechanically reuse the original design family?
- RQ7: In no-solution cases, does the agent honestly state that credible causal identification is not possible with the available data?

## Evaluated Capabilities

| capability | operational definition | later evidence |
|---|---|---|
| Problem structuring | The agent identifies treatment/exposure, outcome, unit, estimand, and mechanism in a way consistent with the task packet. | Rubric dimensions for research question understanding; claim labels for treatment/outcome/unit/estimand errors. |
| Causal threat recognition | The agent identifies concrete threats implied by the task, rather than only saying generic phrases such as "there may be endogeneity." | Threat-related claims; missed threat counts; error analysis by failure mode. |
| Identification strategy design | The agent proposes a design whose identification logic, assumptions, comparison groups, and model match the data and assignment structure. | Identification claim annotations; design score; critical design omission rate. |
| Assumption and diagnostic reasoning | The agent states required assumptions and proposes relevant balance checks, placebo tests, falsification tests, robustness checks, heterogeneity analysis, or event-study diagnostics. | Robustness/check claims; rubric dimensions for assumptions and diagnostics. |
| Evidence boundary awareness | The agent distinguishes supported causal claims from descriptive claims and states what cannot be claimed from the available materials. | Unsupported/Overclaim rates; no-solution honesty rate; Claim-Evidence Table annotations. |
| Perturbation sensitivity | The agent adjusts its design when randomization, timing, exposure, measurement, spillover, or compliance conditions are changed. | Perturbed variant comparisons; design downgrade/revision indicators. |

## Out-of-Scope Capabilities

| excluded item | reason |
|---|---|
| Recalling the original paper | The benchmark is not a memory test. Original titles, authors, locations, and unique phrases are hidden to prevent pretraining or search-based shortcuts. |
| Reproducing the exact original method | A valid answer may differ from the paper if it satisfies the necessary identification conditions. Evaluation focuses on causal validity, not exact replication. |
| Literature review quality | The agent is asked to design an empirical strategy, not summarize related work or cite external papers. |
| Open-ended web search ability | Main runs are closed-book. Retrieval can be tested separately, but it would confound research-design reasoning with search success. |
| Paper-writing fluency | Polished prose is not the target. Long, fluent reports can still be failures if their design claims are unsupported. |
| Code implementation or data analysis execution | The benchmark evaluates research-design planning and claim grounding, not whether the agent can execute Stata/R/Python code on real datasets. |
| General business knowledge | The task is not to give business advice. It is to formulate credible empirical identification under explicit data and institutional constraints. |

## Main Failure Modes

| failure mode | definition | example |
|---|---|---|
| Unsupported Claim | The agent makes a causal, identification, mechanism, or model claim that is not supported by any provided task evidence. | Claiming "random assignment identifies the treatment effect" when the task only says users chose whether to enroll. |
| Overclaim | The task evidence supports a weaker descriptive or correlational conclusion, but the agent states a stronger causal, mechanism, or policy conclusion. | A cross-sectional association is described as proving that a promotion caused higher purchases. |
| Mis-citation | The agent cites relevant-looking task evidence, but that evidence does not support the specific claim being made. | Citing the existence of transaction logs as evidence that advertising exposure is exogenous. |
| Contradiction | The agent's claim conflicts with the task materials or constraints. | Proposing an RCT even though the task says treatment was allocated by a platform algorithm based on purchase intent. |
| Critical Design Omission | The agent omits a design component needed to block the main alternative explanation. | Randomizing price but claiming to separate screening from sunk-cost effects without measuring post-purchase use or adding a second randomization. |
| Mechanism Confounding | The agent claims to distinguish mechanisms but proposes a design that cannot separate them. | Claiming to distinguish adverse selection from moral hazard using only a single randomized loan offer rate. |
| Endogenous Exposure Error | The agent treats exposure, take-up, ad viewing, or program enrollment as if it were randomly assigned when it is behaviorally or algorithmically selected. | Comparing ad-exposed users with unexposed users without addressing targeting or purchase intent. |
| Measurement Credulity | The agent treats self-reported, manipulable, or institutionally produced outcomes as clean evidence without discussing measurement risk. | Using official accounting data as the only outcome in a corruption-monitoring task where the accounts may be manipulated. |
| No-Solution Overclaim | The agent invents an identification strategy when the provided data cannot support credible causal inference. | Proposing DID with no pre-period, no control group, and self-selected treatment. |

## Unit of Evaluation

The primary unit of evaluation is the **claim** in the agent's output. A claim is an atomic statement about the research question, treatment, outcome, identification strategy, assumption, mechanism, statistical model, robustness check, limitation, or additional data need.

The secondary units of evaluation are:

- **Run-level**: one agent response to one task packet, identified by `case_id`, `variant_id`, `level`, and `run_id`.
- **Case-level**: all runs associated with one anonymized source paper and its variants.
- **Variant-level**: Level 1, Level 2, Level 3, perturbed, and no-solution versions of a case.

## Core Experimental Setting

The main benchmark uses a closed-book setting:

- The agent receives only the anonymized task packet.
- The agent must not search the web, infer the original paper, or use external literature.
- The task packet may include research background, data card, institutional details, constraints, and threat hints depending on level.
- The original paper, gold reference, linchpin detail, acceptable designs, invalid designs, and audit notes are evaluator-only.

This setting is necessary because the benchmark is intended to evaluate research-design reasoning, not retrieval or memorization.

## Why This Is Not "Guess The Paper"

The benchmark uses real papers as hidden anchors, but the scoring target is not exact replication of the paper. A response can receive high credit if it proposes an alternative design that satisfies the same necessary identification conditions. Conversely, a response can fail even if it names a plausible method, if the method does not address the assignment mechanism, measurement risk, or key alternative explanation in the provided task.

The evaluation asks:

> Given the information available in the anonymized research case, does the agent make design claims that are warranted by the evidence and assumptions?

It does not ask:

> Can the agent reconstruct the exact published design from memory?

## Planned Evidence For Conclusions

| conclusion type | required evidence |
|---|---|
| Overall weakness | Design-Evidence Inconsistency Rate over claim-level annotations. |
| Information sensitivity | Error and design-score comparison across Level 1, Level 2, and Level 3. |
| Identification-condition sensitivity | Performance difference between original-like and perturbed variants. |
| Scientific honesty | No-solution honesty rate and examples where the agent refuses or fails to refuse causal claims. |
| Systematic failure modes | Grouped errors by domain, design family, and key failure mode. |
| Concrete failure analysis | Case studies with task evidence, agent claim, gold reference, human judgment, and error type. |

## Task 01 Completion Checklist

- [ ] The benchmark can be explained in 1-2 sentences.
- [ ] At least 4 evaluated capabilities are defined.
- [ ] At least 4 out-of-scope capabilities are defined with reasons.
- [ ] The core error types match the later annotation system: Unsupported Claim, Overclaim, Mis-citation, Contradiction.
