<!-- visibility: agent-facing -->
<!-- case_id: C001 -->
<!-- variant: level2 -->

# Anonymous Research Design Task: Level 2

## Task Rule

You must not search the web, infer the original paper, or use external literature. Use only the information provided below. Your goal is to design a rigorous empirical strategy, not to write a literature review.

Do not assume that a known paper has already solved the task. Treat this as an anonymous applied business/economics research problem.

If credible causal identification is not possible from the provided information, do not invent an identification strategy. State the strongest defensible descriptive or correlational analysis instead.

## Research Background

Organizations that rely on voluntary contributions often use direct personal requests to raise funds. Those requests may increase giving because people genuinely want to support the cause, because they feel pressure when confronted in person, or because communication changes who is available and willing to engage.

The research problem is to design a field study that separates these explanations rather than estimating only an undifferentiated average effect of solicitation.

## Research Setting

A fundraising organization approaches residential units in person and can vary how the solicitation is organized before the visit. Potential donors may or may not encounter the fundraiser, and conditional on contact they may or may not contribute. The operational process allows the researcher to observe both engagement with the fundraiser and giving outcomes.

## Research Objective

Design a study to estimate whether voluntary contributions in an in-person request setting reflect genuine willingness to support the cause, social pressure from the interaction, or both.

## Specific Questions To Answer

1. Which design can estimate the effect of solicitation conditions on contact and giving?
2. How can the study distinguish pressure-related giving from genuine willingness to contribute?
3. How should the researcher separate changes in engagement from changes in conditional giving?
4. What patterns would support a welfare-relevant pressure interpretation rather than a pure awareness or scheduling interpretation?

## Causal Mechanisms To Distinguish

- Some potential donors may actively want to engage and contribute.
- Some potential donors may prefer to avoid the interaction and give only when avoidance is difficult.
- Communication before the visit may change scheduling or awareness even if it does not change pressure.
- Small gifts or marginal giving may be especially sensitive to discomfort, but that interpretation is not automatic without the right design.

## Data Structure Overview

- Stage 1: The organization constructs a list or route of planned in-person solicitation opportunities.
- Stage 2: Before the solicitation encounter, contact opportunities may be assigned to different solicitation-process conditions that alter how the visit is communicated or how easy it is to avoid the interaction.
- Stage 3: During the visit window, the researcher observes whether contact occurs and whether a contribution is made, including the contribution amount.
- Stage 4: Supplementary information may be available on route, timing, solicitor, and possibly additional interpretation checks, but exact auxiliary instruments are not specified here.

## Data Card

| field | description |
|---|---|
| unit of observation | Household or individual solicitation opportunity. Each row corresponds to a planned contact attempt and its observed interaction outcome. |
| time span | Short field window around scheduled in-person solicitation attempts; exact dates are not provided. |
| geographic or market scope | Multiple local residential areas served by the same fundraising operation; exact location is withheld. |
| sample construction | Potential donors are selected from a feasible contact list or route plan before solicitation. Exclude units that cannot be reached according to pre-specified operational rules. |
| treatment or exposure variable | Solicitation-process condition before or during an in-person request. Conditions may vary whether potential donors receive advance information about the request and whether they face different interaction costs before contact. |
| outcome variable | Whether contact occurs, whether the person contributes, contribution amount, and contribution size bins. |
| secondary outcomes | Conditional giving among contacted units, engagement or avoidance behavior, and contribution-size patterns. |
| covariates | Route or neighborhood indicators, contact timing, household or building characteristics if available, and solicitor or team identifiers if assignment is not perfectly balanced. |
| baseline or pre-treatment variables | Pre-contact characteristics available from route planning, neighborhood records, or any pre-existing donor information if such records exist. |
| panel or repeated structure | Primarily one planned solicitation event per unit. Repeated attempts should be explicitly flagged rather than treated as independent units. |
| assignment or variation source | Researcher-controlled variation in solicitation-process conditions across contact opportunities. |
| assignment level | Household or individual contact opportunity. |
| outcome measurement level | Contact opportunity and resulting interaction. |
| recommended clustering or inference level | At minimum, account for route, building, or solicitor-level grouping if treatment is operationally grouped; otherwise justify household-level inference. |
| repeated exposure | Possible if the same household is contacted more than once or receives multiple messages; repeated exposure must be tracked. |
| compliance or take-up | Some assigned contacts may not result in an actual interaction because the potential donor is absent, avoids contact, or cannot be reached. |
| missingness or attrition | Missing outcomes can arise from failed contact, incomplete recording by solicitors, or unobserved reasons for non-response. |
| possible spillover or interference | Neighbors may communicate about the fundraiser; solicitor behavior may change across nearby routes or conditions. |

## Variable Groups

### Treatment Or Exposure Variables

- Solicitation-process condition.
- Indicators for pre-contact communication or pre-contact engagement options if such features vary.

### Selection Or Sample-Flow Variables

- Planned contact opportunity.
- Whether the fundraiser reaches the unit.
- Whether the unit engages with the fundraiser.

### Main Outcome Variables

- Whether contact occurs.
- Whether a contribution is made.
- Contribution amount.

### Secondary Outcome Variables

- Giving conditional on contact.
- Small versus large contribution categories.
- Any behavioral indicator of avoidance or engagement if observed.

### Baseline Controls And Design Variables

- Route, building, neighborhood, or area indicators.
- Contact timing or visit window.
- Solicitor or team identifiers.

## Known Constraints

- The design should match the data structure above.
- The answer must distinguish descriptive associations, causal claims, and mechanism claims.
- The answer should state what cannot be learned from the available information.
- Do not label the final identification strategy by name unless you justify why the data support it.
- Do not rely on external facts about the original paper, place, or organization.

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
