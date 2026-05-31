# Stage 3: Candidate Identification Strategies

You are working on an anonymized business or economics research-design task packet.

Your job in this stage is not to write the final report. Your job is to enumerate candidate designs before any final commitment.

## Instructions

1. Read the packet carefully.
2. List at least 3 distinct candidate strategies.
3. Do not collapse multiple ideas into one bundled candidate.
4. If no credible causal design is defensible from the packet, at least one candidate must be a descriptive fallback and set `is_fallback` to `true`.
5. Stay inside the packet. Do not reconstruct hidden paper details.
6. Output JSON only. No prose before or after the JSON.

## Required JSON Schema

```json
{
  "candidates": [
    {
      "name": "short candidate name",
      "estimand": "target estimand or strongest defensible target",
      "identifying_variation": "what variation would identify it",
      "critical_assumption": "most important identifying assumption",
      "packet_support": "which packet-local evidence motivates this candidate",
      "fragility": "why this candidate may fail in this packet",
      "is_fallback": false
    }
  ],
  "recommended_primary": "candidate name or null",
  "notes": "optional short note"
}
```

## Packet

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

