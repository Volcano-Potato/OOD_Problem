<!-- visibility: agent-facing -->
<!-- case_id: C001 -->
<!-- variant: no_solution -->

# Anonymous Research Design Task: No-Solution Variant

## Task Rule

Use the information provided below to design a rigorous empirical strategy for this anonymized applied business/economics research problem. Your goal is to produce a defensible research design, not to write a literature review.

Do not assume that a known paper has already solved the task. Ground your reasoning in the background, data description, institutional details, and constraints provided in this packet.

Do not fill in packet-absent operational details, institutional features, or named design devices as if they were known facts. If multiple concrete implementations fit the packet, describe them generically or label them explicitly as illustrative examples rather than assumptions.

If credible causal identification is not possible from the provided information, do not invent an identification strategy. State the strongest defensible descriptive or correlational analysis instead.

## Research Background

Organizations that rely on voluntary contributions often use direct personal requests to raise funds. Those requests may increase giving because people genuinely want to support the cause, because they feel pressure when confronted in person, or because people who are easier to reach are also more likely to give.

The business problem is important: fundraisers want to know whether more intensive personal outreach actually changes giving behavior or merely targets people who were already easier to persuade.

## Research Setting

A fundraising organization keeps operational records on residential outreach campaigns across many local areas. Households may receive different amounts of contact effort depending on route decisions, prior donor history, expected availability, and solicitor judgment. The organization records whether a household was contacted and whether a contribution was made.

## Research Objective

Assess whether more intensive in-person fundraising contact increases contributions and whether contribution patterns reflect genuine willingness to give or pressure from the interaction.

## Specific Questions To Answer

1. Are households that receive more intensive outreach more likely to contribute?
2. Do observed contribution patterns suggest genuine demand or pressure-related behavior?
3. What can be learned descriptively from outreach intensity, contact, and giving records?
4. What additional design change would be needed to make causal claims credible?

## Data Structure Overview

- Stage 1: The organization assembles historical donor and neighborhood information before each campaign.
- Stage 2: Solicitors and managers choose where to spend more effort, whom to revisit, and which households to approach first.
- Stage 3: The organization records contact outcomes and donations during the campaign.
- Stage 4: A cross-sectional campaign summary links outreach intensity, contact success, and donation outcomes with household and area covariates.

## Available Data

| field | description |
|---|---|
| unit of observation | Household-by-campaign outreach record. |
| time span | Single campaign cross-section with some historical household or neighborhood covariates. |
| sample construction | Households appearing on fundraising routes during a campaign. |
| treatment or exposure variable | Outreach intensity, whether the household was contacted, number of attempts, and whether the household received advance communication chosen operationally by the organization. |
| outcome variable | Whether the household contributed and contribution amount. |
| secondary outcomes | Whether contact occurred, number of attempts, and contribution size category. |
| covariates | Neighborhood characteristics, prior donor history if available, route timing, household observables, and solicitor identifiers. |
| panel or repeated structure | Mostly cross-sectional for one campaign; limited historical covariates may exist but no clean repeated experimental structure. |
| assignment or variation source | Outreach intensity and communication choices are determined by managers and solicitors using operational judgment. |
| assignment level | Household-by-campaign record. |
| outcome measurement level | Household-by-campaign record. |
| missingness or attrition | Some households are not reached, and some operational fields may be incomplete. |
| possible spillover or interference | Neighbors may communicate and solicitors may shift effort across nearby households. |

## Variable Groups

### Treatment Or Exposure Variables

- Outreach intensity.
- Contact indicator.
- Operationally chosen pre-contact communication.

### Selection Or Sample-Flow Variables

- Inclusion on a route.
- Number of attempts.
- Whether contact occurs.

### Main Outcome Variables

- Contribution indicator.
- Contribution amount.

### Secondary Outcome Variables

- Contribution size bins.
- Contact success.

### Baseline Controls And Design Variables

- Prior donor history if available.
- Neighborhood and route indicators.
- Solicitor and timing indicators.

## Identification Limitations

- No randomized assignment or quasi-random variation is provided.
- No credible instrument, threshold, boundary, or externally imposed timing shock is provided.
- Households receiving more intensive outreach may differ in unobserved willingness to give, availability, or prior relationship with the organization.
- Observed giving and contact outcomes cannot cleanly separate genuine willingness from pressure-related behavior.

## Known Constraints

- The task should still look empirically tempting: many covariates, clear outcomes, and real business relevance.
- The answer must explicitly distinguish what is causally identifiable from what is only descriptive or correlational.
- If causal identification is not credible, the answer must say so plainly rather than inventing a design.

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
