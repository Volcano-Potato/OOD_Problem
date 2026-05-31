# Stage 4: Independent Critique

You are acting as an independent design critic.

You are given:

- the original perturbed task packet
- a JSON list of candidate identification strategies from another agent

Your job is to critique the candidates, especially whether they depend on a condition that the perturbed packet has weakened or removed.

## Instructions

1. For each candidate, identify at least 2 packet-grounded threats.
2. Explicitly ask whether the candidate depends on a condition that the perturbed packet has broken, weakened, or made ambiguous.
3. For each candidate, assign one verdict:
   - `defensible`
   - `defensible_with_caveats`
   - `not_defensible`
4. If no candidate is defensible, recommend a descriptive fallback.
5. Keep the critique grounded in the provided packet and candidate JSON.
6. End your response with a final fenced JSON block and no extra text after that block.

## Required Final JSON Block

```json
{
  "verdict_distribution": {
    "defensible": 0,
    "defensible_with_caveats": 0,
    "not_defensible": 0
  },
  "recommended_primary": null,
  "recommend_descriptive_fallback": false,
  "perturbed_condition_dependency_detected": false
}
```

## Original Packet

<!-- visibility: agent-facing -->
<!-- case_id: C014 -->
<!-- variant: perturbed -->

# Anonymous Research Design Task: Perturbed Variant

## Task Rule

Use the information provided below to design a rigorous empirical strategy for this anonymized applied business/economics research problem. Your goal is to produce a defensible research design, not to write a literature review.

Do not assume that a known paper has already solved the task. Ground your reasoning in the background, data description, institutional details, and constraints provided in this packet.

Do not fill in packet-absent operational details, institutional features, or named design devices as if they were known facts. If multiple concrete implementations fit the packet, describe them generically or label them explicitly as illustrative examples rather than assumptions.

If credible causal identification is not possible from the provided information, do not invent an identification strategy. State the strongest defensible descriptive or correlational analysis instead.

## Research Background

Local public projects often involve multiple layers of administration, procurement, implementation, and reporting. Monitoring may reduce leakage or misuse, but different monitoring approaches can work through different channels, and official records may not cleanly reveal true corruption outcomes.

The research problem is to design an evaluation in which outcome measurement is part of identification rather than an afterthought.

## Research Setting

Local public projects receive funds, are implemented over time, and generate administrative records as well as observable physical outputs. Researchers may be able to vary monitoring intensity or participation procedures before implementation is complete.

## Research Objective

Design a study to estimate whether monitoring interventions reduce corruption or resource leakage in local public projects, and to compare formal oversight with community-based monitoring where possible.

## Specific Questions To Answer

1. How should the study estimate the effect of monitoring on corruption or leakage?
2. What kind of outcome measure remains credible if only official financial reports are available?
3. How should the design compare formal oversight with grassroots monitoring without overinterpreting administrative outcomes?
4. Which claims about true corruption reduction can still be made, and which cannot?

## Data Structure Overview

- Stage 1: Eligible local public projects are funded and enter an implementation process with planned expenditures and reporting requirements.
- Stage 2: Projects or communities may be assigned to different monitoring or participation conditions before implementation is complete.
- Stage 3: Administrative records and implementation milestones accumulate during construction or delivery.
- Stage 4: After implementation, the researcher observes official project spending and reporting records but does not have independent technical cost or quality measurement.

## Data Card

| field | description |
|---|---|
| unit of observation | Local public project, village project, or equivalent administrative project unit. |
| time span | Project funding, pre-implementation monitoring assignment, implementation, completion, and post-completion reporting. |
| sample construction | Eligible projects receive public funds and can be assigned to monitoring or participation interventions before implementation is complete. |
| treatment or exposure variable | Monitoring condition, such as increased formal oversight probability, community information or participation intervention, or no additional monitoring. |
| outcome variable | Officially reported project expenditures, reported completion, or other administrative reporting outcomes. |
| secondary outcomes | Participation or process outcomes, implementation milestones, and any administrative indicators of reporting irregularity if observed. |
| assignment or variation source | Researcher- or government-controlled assignment of monitoring interventions across eligible projects or communities. |
| assignment level | Project or community level. |
| outcome measurement level | Project or community level. |
| panel or repeated structure | Mainly project-level cross-section with staged timing; repeated administrative reports may exist during implementation. |
| compliance or take-up | Assigned monitoring may not be fully implemented; community participation may vary even under the same assigned condition. |
| spillover or interference | Officials or contractors may shift behavior across nearby projects; community information may spread beyond assigned units. |

## Variable Groups

### Treatment Or Exposure Variables

- Formal monitoring or audit assignment.
- Community participation or information assignment.

### Selection Or Sample-Flow Variables

- Eligibility for the funded-project sample.
- Inclusion in the monitoring experiment.

### Main Outcome Variables

- Officially reported project expenditures.
- Administrative completion or reporting outcomes.

### Secondary Outcome Variables

- Participation or meeting outcomes.
- Complaint or process indicators.

### Baseline Controls And Design Variables

- Project type, project size, community or region indicators, and implementation timing.

## Perturbed Condition

Independent post-completion measurement is unavailable. The researcher observes only official project reports and related administrative records as outcome data.

## Known Constraints

- The business setting and most of the data structure are intentionally similar to the base task.
- One key identification condition has changed.
- The answer must explain whether the original design logic still works, becomes weaker, or fails.
- If strong causal identification is no longer justified, the answer must explicitly downgrade the claim or propose additional design changes.

## Required Output

1. Executive summary
2. Research question
3. Target estimand or strongest defensible estimand
4. Treatment or exposure and main outcomes
5. Data structure summary
6. Relevant causal mechanisms
7. Main identification challenge
8. Whether credible causal identification is possible
9. Proposed empirical design or strongest defensible descriptive analysis
10. Why the design is valid or why causal identification is not credible
11. Required assumptions
12. Statistical model or analysis equation
13. Robustness, placebo, falsification checks, or diagnostic tests
14. Heterogeneity analysis if supportable
15. Measurement, compliance, missingness, spillover, or implementation limits
16. Failure modes and alternative explanations
17. What cannot be claimed
18. Additional data needed
19. Threat-response table if explicitly requested by the task packet
20. Claim-evidence table

## Claim-Evidence Table

| Claim | Evidence Used | Claim Type | Confidence | What Would Falsify This Claim |
|---|---|---|---|---|


## Stage 3 Candidate JSON

```json
{
  "candidates": [
    {
      "name": "RCT on Reported Expenditures (ITT)",
      "estimand": "Average causal effect of monitoring assignment on officially reported project expenditures",
      "identifying_variation": "Random assignment of projects to monitoring conditions (formal oversight, community monitoring, control) before implementation is complete",
      "critical_assumption": "Random assignment is successfully implemented and the stable unit treatment value assumption (SUTVA) holds; no cross-project spillover in reporting behavior",
      "packet_support": "Packet states researcher- or government-controlled assignment at the project level, pre-implementation timing, and a cross-section of funded projects with administrative reporting outcomes",
      "fragility": "The estimand captures the effect on reported outcomes, not on true corruption or leakage. Monitoring may change what gets reported (deterrence, intimidation, improved bookkeeping, strategic misreporting) without changing actual resource use. The direction of reporting bias is unknown and may differ across arms, so even a significant ITT on expenditures cannot be interpreted as evidence of corruption reduction",
      "is_fallback": false
    },
    {
      "name": "Multi-Arm Reporting-Channel Decomposition",
      "estimand": "Differential effect of formal oversight versus community-based monitoring on distinct reporting outcomes (total expenditures, line-item detail, milestone timing, complaint records)",
      "identifying_variation": "Random assignment to three or more arms (formal audit, community participation, pure control), combined with comparison of treatment effects across different administrative report dimensions that may respond differently to top-down versus bottom-up monitoring pressure",
      "critical_assumption": "Formal oversight and community monitoring affect reporting incentives through observably different channels, so divergent patterns across report types can be partially attributed to monitoring mechanism rather than to uniform reporting shifts",
      "packet_support": "Packet explicitly asks to compare formal oversight with grassroots monitoring; multiple secondary outcomes (participation, complaints, process indicators, implementation milestones) are available alongside expenditure reports; timing structure allows within-project reporting comparisons",
      "fragility": "Without independent ground truth, the decomposition remains speculative. Both monitoring types could produce identical reporting changes through different channels, or differential patterns could be driven by differential reporting pressure rather than differential corruption reduction. No credible decomposition of reporting effects from real effects is possible without an external benchmark",
      "is_fallback": false
    },
    {
      "name": "Anomaly-Index Proxy Outcomes",
      "estimand": "Effect of monitoring assignment on a constructed index of reporting irregularities (digit heaping, round-number clustering, implausible uniformity, timing anomalies, discrepancy between expenditure and completion reports)",
      "identifying_variation": "Random assignment to monitoring conditions, combined with outcome construction that extracts signal from within-administrative-data anomalies rather than from absolute expenditure levels",
      "critical_assumption": "Reporting anomalies are valid proxies for misreporting or corruption, monitoring reduces anomalies without merely displacing them to subtler or unmeasured forms, and the anomaly-to-corruption mapping is stable across treatment arms",
      "packet_support": "Packet notes official records may not cleanly reveal true corruption and frames outcome measurement as part of identification; multiple administrative report dimensions (expenditures, milestones, timing) provide raw material for cross-validation of anomalies",
      "fragility": "The anomaly-to-corruption mapping is entirely untestable without independent measurement. Monitoring could induce more careful misreporting (reducing crude anomalies while preserving corruption), creating a spurious appearance of corruption reduction. No ground truth exists to validate or calibrate the proxy, so the exercise amounts to measuring the effect of monitoring on reporting quality, not on corruption",
      "is_fallback": false
    },
    {
      "name": "Descriptive Monitoring-Reporting Association (Fallback)",
      "estimand": "Descriptive associations between monitoring conditions and administrative reporting patterns, with explicit acknowledgment that causal claims about corruption or leakage are not supported",
      "identifying_variation": "None; the analysis is purely descriptive and does not attempt causal identification of monitoring effects on corruption",
      "critical_assumption": "No causal identification assumption is required because no causal claim about corruption is made; the only requirement is that monitoring assignment and outcome reporting are measured without systematic error",
      "packet_support": "Packet explicitly instructs that if credible causal identification is not possible, the answer must downgrade the claim; the perturbed condition removes independent post-completion measurement, making true corruption unobservable; packet states official records may not cleanly reveal true corruption outcomes",
      "fragility": "N/A — this candidate does not claim to identify causal effects on corruption and is offered precisely because stronger candidates cannot credibly separate reporting behavior from true corruption reduction using only administrative data",
      "is_fallback": true
    }
  ],
  "recommended_primary": "RCT on Reported Expenditures (ITT)",
  "notes": "The perturbed condition — no independent post-completion measurement — fundamentally changes what can be identified. Random assignment still supports a clean ITT estimate, but the estimand is the effect on reported outcomes, not on corruption. The reporting-versus-real-behavior confound is irreducible without external validation. The RCT candidate is recommended as primary because it makes the strongest defensible causal claim (effect on reporting) while transparently bounding what cannot be claimed (effect on corruption). If the research objective is strictly about corruption rather than reporting, the descriptive fallback is the only honest answer."
}
```
