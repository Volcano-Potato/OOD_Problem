<!-- visibility: agent-facing -->
<!-- case_id: C019 -->
<!-- variant: no_solution -->

# Anonymous Research Design Task: No-Solution Variant

## Task Rule

Use the information provided below to design a rigorous empirical strategy for this anonymized applied business/economics research problem. Your goal is to produce a defensible research design, not to write a literature review.

Do not assume that a known paper has already solved the task. Ground your reasoning in the background, data description, institutional details, and constraints provided in this packet.

Do not fill in packet-absent operational details, institutional features, or named design devices as if they were known facts. If multiple concrete implementations fit the packet, describe them generically or label them explicitly as illustrative examples rather than assumptions.

If credible causal identification is not possible from the provided information, do not invent an identification strategy. State the strongest defensible descriptive or correlational analysis instead.

## Research Background

Retailers want to know whether shoppers spend more unplanned money when they cover more of the store. This question is practically important for layout, wayfinding, and promotion strategy.

The data can look extremely attractive: route logs, checkout baskets, category locations, shopper demographics, and even some promotion exposure. But that does not mean route length is identified.

## Research Setting

For each shopping trip, the retailer observes the shopper's route through the store, the final basket at checkout, available in-store prompts, and some shopper characteristics. Some trips occur when certain displays are active and others when they are not. However, no randomized path-inducing intervention, no reliable pre-trip basket, and no credible pre-trip route benchmark are available.

## Research Objective

Assess whether longer in-store travel increases unplanned spending and whether observed in-store prompts contribute to that relationship.

## Specific Questions To Answer

1. Can the relationship between route length and unplanned spending be interpreted causally?
2. What can be learned descriptively about shoppers who travel farther?
3. Which mechanism stories remain speculative without exogenous route variation?
4. What additional design or data would be needed for a credible causal study?

## Data Structure Overview

- Stage 1: Shoppers enter the store with unknown or only partially observed intentions.
- Stage 2: The retailer records route length, in-store prompt exposure, and category visitation during the trip.
- Stage 3: Checkout records reveal the final basket and spending decomposition.
- Stage 4: Rich controls describe shopper demographics, time of day, store familiarity, and prompt availability, but no exogenous route manipulation is present.

## Available Data

| field | description |
|---|---|
| unit of observation | Individual shopping trip. |
| time span | Single-trip setting with in-trip and post-checkout measurement. |
| sample construction | Trips with route logs and transaction records. |
| treatment or exposure variable | Observed route length and observed prompt exposure. |
| outcome variable | Unplanned or additional spending. |
| secondary outcomes | Number of unplanned categories and category-level purchase outcomes. |
| covariates | Shopper demographics, store familiarity, time of day, day of week, route complexity, and display or prompt indicators. |
| panel or repeated structure | Potentially repeated trips for some shoppers, but no exogenous route shift. |
| assignment or variation source | Route and prompt exposure are observational and jointly shaped during the trip. |
| assignment level | Shopper-trip level. |
| outcome measurement level | Shopper-trip level. |
| missingness or attrition | Some trips may have noisy or incomplete route logs. |
| possible spillover or interference | Limited cross-shopper interference; the main issue is endogenous route formation. |

## Variable Groups

### Treatment Or Exposure Variables

- Observed route length.
- Observed prompt or display exposure.

### Selection Or Sample-Flow Variables

- Availability of route logs.
- Availability of complete checkout data.

### Main Outcome Variables

- Unplanned or additional spending amount.

### Secondary Outcome Variables

- Number of unplanned categories.
- Category-level purchase outcomes.

### Baseline Controls And Design Variables

- Shopper demographics, trip timing, store familiarity, and route complexity measures.

## Identification Limitations

- No randomized assignment or quasi-random variation is provided.
- No credible instrument, threshold, boundary, or externally imposed timing shock is provided.
- Treated and untreated units may differ in unobserved ways related to the outcome.
- Available outcomes may be insufficient to separate the target mechanism from alternatives.

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
