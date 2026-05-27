<!-- visibility: agent-facing -->
<!-- case_id: C016 -->
<!-- variant: level3 -->

# Anonymous Research Design Task: Level 3

## Task Rule

Use the information provided below to design a rigorous empirical strategy for this anonymized applied business/economics research problem. Your goal is to produce a defensible research design, not to write a literature review.

Do not assume that a known paper has already solved the task. Ground your reasoning in the background, data description, institutional details, and constraints provided in this packet.

Do not fill in packet-absent operational details, institutional features, or named design devices as if they were known facts. If multiple concrete implementations fit the packet, describe them generically or label them explicitly as illustrative examples rather than assumptions.

If credible causal identification is not possible from the provided information, do not invent an identification strategy. State the strongest defensible descriptive or correlational analysis instead.

## Research Background

School-based adolescent health programs often aim to reduce harmful behavior through information. But "more information" is not a single treatment: some messages are generic and tell students to avoid risk altogether, while others emphasize that some choices or relationship types are materially riskier than others.

The policy question is whether the content of information changes behavior in a way that can be seen in real downstream outcomes, not just in survey responses. That makes outcome measurement and mechanism interpretation central to the design.

## Research Setting

Researchers observe a cohort of students exposed to different information environments at school. A standard curriculum-style message may be delivered broadly, while a targeted campaign provides more differentiated risk information. Follow-up then combines broad objective outcome measurement for the cohort with narrower survey-based evidence on behavior and partner choices for a selected subgroup.

## Research Objective

Design a study to estimate whether targeted risk information changes adolescent behavior more effectively than the standard generic curriculum and to identify whether any effect operates through safer partner choice, greater protection, or lower activity.

## Specific Questions To Answer

1. How should the study estimate the effect of targeted information content rather than merely the effect of receiving any message?
2. What is the most credible primary outcome when behavior is sensitive and survey responses may be biased?
3. How should the design separate intensive-margin change from extensive-margin abstinence or activity effects?
4. What can and cannot be claimed causally about mechanism, given the available data and threats below?

## Causal Mechanisms To Distinguish

- Students may substitute away from riskier relationships toward safer ones.
- Students may adopt more protective behavior within ongoing relationships.
- Generic curriculum exposure may not move behavior if it does not change the perceived relative risk of available choices.
- Survey responses may reflect reporting comfort or selected follow-up rather than true behavioral change.

## Data Structure Overview

- Stage 1: A focal student cohort is enrolled in schools before targeted information is delivered.
- Stage 2: Schools differ in whether students receive only the standard generic curriculum or also receive a targeted information campaign that highlights differences in risk across choices or partner types.
- Stage 3: The cohort is followed into the next period using broad status checks that reveal an objective downstream consequence related to unsafe behavior.
- Stage 4: A later follow-up survey among a selected subgroup records self-reported activity, partner characteristics, and protection behavior.

## Data Card

| field | description |
|---|---|
| unit of observation | Individual student outcome linked to school-level assignment. |
| time span | Intervention period plus follow-up over the next academic year; exact dates are withheld. |
| geographic or market scope | Multiple schools under a common education and adolescent health environment; exact location is withheld. |
| sample construction | A focal school cohort is exposed during a key grade or school stage, then followed through objective status checks and a selected survey-based follow-up. |
| treatment or exposure variable | School-level information-content condition, including standard generic information and targeted risk information. |
| outcome variable | Objective downstream consequence related to unsafe behavior. |
| secondary outcomes | Partner-profile outcomes, self-reported activity, and self-reported protection behavior. |
| covariates | Baseline school characteristics, cohort composition, follow-up schooling status, and other pre-treatment design variables. |
| baseline or pre-treatment variables | Pre-treatment school characteristics and cohort environment measures. |
| panel or repeated structure | No full balanced individual panel; broad objective follow-up plus narrower selected survey follow-up. |
| assignment or variation source | Planned school-level variation in information content. |
| assignment level | School or classroom-wide implementation level. |
| outcome measurement level | Individual student level. |
| recommended clustering or inference level | School level or higher implementation cluster if treatments were grouped. |
| repeated exposure | Yes; students remain in the school information environment over the intervention period. |
| compliance or take-up | Actual exposure may vary with attendance or participation. |
| missingness or attrition | Survey-based follow-up is selective; objective status follow-up is broader but still imperfect. |
| possible spillover or interference | Information can spread across cohorts or nearby schools, and partner markets can transmit interference between treated and untreated groups. |

## Variable Groups

### Treatment Or Exposure Variables

- Generic-information assignment.
- Targeted-information assignment.
- Exposure-intensity or attendance indicators if available.

### Selection Or Sample-Flow Variables

- Focal-cohort membership.
- Availability in broad follow-up status checks.
- Inclusion in the selected survey follow-up sample.

### Main Outcome Variables

- Objective downstream unsafe-behavior consequence.
- Objective partner-risk-related suboutcome if observed.

### Secondary Outcome Variables

- Self-reported activity.
- Self-reported partner-profile measures.
- Self-reported protection measures.

### Baseline Controls And Design Variables

- School characteristics, cohort composition, baseline environment measures, and follow-up schooling-status indicators.

## Institutional Details Relevant For Identification

- Assignment is controlled at the school or program level rather than by individual students choosing their information condition.
- Students learn about the relevant information during the school period, before the follow-up outcomes are measured.
- Not every student is equally exposed, because attendance, participation, and attention can differ within assigned schools.
- The most credible outcome comes from later status tracking and verification rather than from self-administered behavior questions alone.
- The later behavioral survey is available only for a selected subgroup observed after the school transition.
- Students within the same school or nearby schools may interact, share information, or affect one another through overlapping relationship markets.

## Potential Threats

- Potential selection or sample-flow issue: the subgroup observed in the later behavioral survey may not represent the full treated cohort.
- Potential measurement issue: self-reported behavior is sensitive and may differ in reporting quality across treatment conditions.
- Potential mechanism-confounding issue: if the targeted campaign differs in format or messenger as well as in content, content effects may be mixed with delivery-channel effects.
- Potential spillover or interference issue: information may spread across adjacent cohorts or nearby schools, and risky partners may reallocate across treated and untreated groups.
- Potential compliance issue: school assignment does not guarantee equal student-level exposure to the information.
- Potential interpretation issue: a change in the objective outcome does not automatically reveal whether the effect came through abstinence, safer partner choice, or more protection.
- Potential inference issue: assignment occurs at the school level, so individual-level analysis must respect clustered variation.

## Required Threat-Response Table

In addition to the standard output, include this table. If a threat cannot be addressed with the available data, say so.

| Threat | Why It Matters | Proposed Diagnostic Or Design Response | Remaining Limitation |
|---|---|---|---|

## Known Constraints

- The design should match the data, institutional details, and threats above.
- The answer must distinguish descriptive associations, randomized or quasi-random causal claims, and mechanism claims.
- The answer should state what cannot be learned from the available information.
- Do not turn the threat list into a generic robustness checklist. Connect each threat to the proposed design.
- Do not rely on unsupported source-specific facts about the original paper, country, or disease topic.

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
