<!-- visibility: agent-facing -->
<!-- case_id: C001 -->
<!-- variant: level2 -->

# Anonymous Research Design Task: Level 2

## Task Rule

You must not search the web, infer the original paper, or use external literature. Use only the information provided below. Your goal is to design a rigorous empirical strategy, not to write a literature review.

If credible causal identification is not possible from the provided information, do not invent an identification strategy. State the strongest defensible descriptive or correlational analysis instead.

## Research Background

Organizations that request voluntary contributions often rely on direct personal contact with potential donors. These interactions may raise donations for different reasons. Some people may value the social cause and feel better when they contribute. Others may give mainly because refusing a request in person is uncomfortable, socially costly, or difficult to avoid.

This distinction matters for both research and practice. A campaign that increases giving by helping motivated donors act on their preferences has a different welfare interpretation from a campaign that raises money mainly by creating unwanted pressure.

## Research Objective

Design a study to estimate whether voluntary contributions in an in-person request setting reflect genuine willingness to support the cause, social pressure from the interaction, or both. The design should clarify what outcome patterns would support each interpretation.

## Data Card

| field | description |
|---|---|
| unit of observation | Household or individual solicitation opportunity. Each row corresponds to a planned contact attempt and its observed interaction outcome. |
| time span | Short field window around scheduled in-person solicitation attempts; exact dates are not provided. |
| geographic or market scope | Multiple local residential areas served by the same fundraising operation; exact location is withheld. |
| sample construction | Potential donors are selected from a feasible contact list or route plan before solicitation. Exclude units that cannot be reached according to pre-specified operational rules. |
| treatment or exposure variable | Solicitation-process condition before or during an in-person request. Conditions may vary whether potential donors receive advance information about the request and whether they face different interaction costs before contact. |
| outcome variable | Whether contact occurs, whether the person contributes, contribution amount, and contribution size bins. |
| covariates | Pre-treatment route or neighborhood indicators, contact timing, household or building characteristics if available, solicitor/team indicators if assignment is not perfectly balanced. |
| panel or repeated structure | Primarily one planned solicitation event per unit. Repeated attempts should be explicitly flagged rather than treated as independent units. |
| assignment or variation source | Researcher-controlled variation in solicitation-process conditions across contact opportunities. |
| assignment level | Household or individual contact opportunity. |
| outcome measurement level | Contact opportunity and resulting interaction. |
| recommended clustering or inference level | At minimum, account for the assignment/contact route or solicitor level if treatment is grouped operationally; otherwise justify household-level inference. |
| repeated exposure | Possible if the same household is contacted more than once or receives multiple messages; repeated exposure must be tracked. |
| compliance or take-up | Some assigned contacts may not result in an actual interaction because the potential donor is absent, avoids contact, or cannot be reached. |
| missingness or attrition | Missing outcomes can arise from failed contact, incomplete recording by solicitors, or unobserved reasons for non-response. |
| possible spillover or interference | Neighbors may communicate about the fundraiser; solicitor behavior may change across routes or conditions. |

## Known Constraints

- The design should match the data structure above.
- The answer must distinguish causal claims from descriptive claims.
- The answer should state what cannot be learned from the available information.
- Do not assume that a simple comparison of contacted and non-contacted people is automatically causal.
- Do not rely on external facts about charities, cities, campaigns, or previous studies.

## Required Output

1. Research question
2. Estimand
3. Treatment or exposure
4. Outcome
5. Main identification challenge
6. Proposed empirical design
7. Why the design is valid
8. Required assumptions
9. Statistical model
10. Robustness or placebo checks
11. Heterogeneity analysis
12. Failure modes
13. What cannot be claimed
14. Additional data needed
15. Claim-evidence table

## Claim-Evidence Table

| Claim | Evidence Used | Claim Type | Confidence | What Would Falsify This Claim |
|---|---|---|---|---|
