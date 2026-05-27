<!-- visibility: agent-facing -->
<!-- case_id: C016 -->
<!-- variant: perturbed -->

# Anonymous Research Design Task: Perturbed Variant

## Task Rule

Use the information provided below to design a rigorous empirical strategy for this anonymized applied business/economics research problem. Your goal is to produce a defensible research design, not to write a literature review.

Do not assume that a known paper has already solved the task. Ground your reasoning in the background, data description, institutional details, and constraints provided in this packet.

Do not fill in packet-absent operational details, institutional features, or named design devices as if they were known facts. If multiple concrete implementations fit the packet, describe them generically or label them explicitly as illustrative examples rather than assumptions.

If credible causal identification is not possible from the provided information, do not invent an identification strategy. State the strongest defensible descriptive or correlational analysis instead.

## Research Background

A school-based adolescent health program wants to know whether targeted risk information changes behavior more effectively than standard generic messages. The practical challenge is that sensitive behavior is hard to measure directly, and not every plausible dataset provides an equally credible outcome.

## Research Setting

Schools differ in the information environment students face: some students receive only a standard generic message, while others are additionally exposed to targeted information about differential risk across choices or partner types. Follow-up still includes a later survey about activity, partner characteristics, and protection behavior, but the objective downstream outcome available in the base case is not available here.

## Research Objective

Design a study to estimate whether targeted risk information changes adolescent behavior more effectively than the standard generic curriculum when only survey-based behavioral outcomes are observed.

## Specific Questions To Answer

1. Can the information-content effect still be identified credibly with the available outcomes?
2. How much can be learned from self-reported activity, partner characteristics, and protection behavior alone?
3. Which mechanism claims remain plausible, and which become too strong without the objective outcome?
4. What additional data or design changes would be needed to restore stronger causal interpretation?

## Data Structure Overview

- Stage 1: A focal student cohort is enrolled in schools before targeted information is delivered.
- Stage 2: Schools differ in whether students receive only the standard generic curriculum or also receive targeted information about differential risk.
- Stage 3: The cohort is followed into a later period through a behavior survey that records self-reported activity, partner characteristics, and protection behavior.
- Stage 4: No objective downstream outcome related to unsafe behavior is available in the current data.

## Data Card

| field | description |
|---|---|
| unit of observation | Individual student in the survey follow-up sample. |
| time span | Intervention period plus later survey follow-up; exact dates are withheld. |
| sample construction | Survey respondents come from the focal cohort after the school transition. |
| treatment or exposure variable | School-level information-content condition. |
| outcome variable | Self-reported behavior, partner-profile measures, and self-reported protection behavior. |
| secondary outcomes | Follow-up schooling status or related survey outcomes if observed. |
| assignment or variation source | Planned school-level variation in information content. |
| assignment level | School or classroom-wide implementation level. |
| outcome measurement level | Individual student level. |
| panel or repeated structure | Single selected survey follow-up rather than broad verified tracking. |
| compliance or take-up | Exposure can vary with attendance or participation. |
| spillover or interference | Students may exchange information across cohorts or schools, and partner markets may create interference. |

## Variable Groups

### Treatment Or Exposure Variables

- Generic-information assignment.
- Targeted-information assignment.

### Selection Or Sample-Flow Variables

- Focal-cohort membership.
- Inclusion in the later survey follow-up sample.

### Main Outcome Variables

- Self-reported activity.
- Self-reported partner-profile measures.
- Self-reported protection behavior.

### Secondary Outcome Variables

- Follow-up schooling-status indicators if observed.

### Baseline Controls And Design Variables

- School characteristics, cohort composition, and available pre-treatment environment measures.

## Perturbed Condition

The broad objective downstream outcome used in the base setting is not observed here. The available outcomes are only self-reported survey responses collected in later follow-up.

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
