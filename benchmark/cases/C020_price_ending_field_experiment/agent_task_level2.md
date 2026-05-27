<!-- visibility: agent-facing -->
<!-- case_id: C020 -->
<!-- variant: level2 -->

# Anonymous Research Design Task: Level 2

## Task Rule

Use the information provided below to design a rigorous empirical strategy for this anonymized applied business/economics research problem. Your goal is to produce a defensible research design, not to write a literature review.

Do not assume that a known paper has already solved the task. Ground your reasoning in the background, data description, institutional details, and constraints provided in this packet.

Do not fill in packet-absent operational details, institutional features, or named design devices as if they were known facts. If multiple concrete implementations fit the packet, describe them generically or label them explicitly as illustrative examples rather than assumptions.

If credible causal identification is not possible from the provided information, do not invent an identification strategy. State the strongest defensible descriptive or correlational analysis instead.

## Research Background

A retailer wants to know whether using a salient terminal-digit pricing format increases demand for a product offer. Managers care about this both as a direct pricing tactic and as a clue about how customers interpret prices when information is limited.

The difficulty is that a terminal-digit format can be confounded with broader promotional meaning. Customers may react because the ending looks familiar as a bargain cue, because the item appears to be on sale, or because the product is unfamiliar enough that price presentation carries more informational weight.

## Research Setting

The retailer can present otherwise comparable versions of product offers to separate customer groups. The focal products are identical across versions, but the visible price format can differ. The researcher can observe resulting demand for the focal items and can also classify items by whether they are relatively new or already familiar to the customer base.

## Research Objective

Design a study to estimate the causal effect of a salient terminal-digit price format on demand and to assess whether the effect varies with product familiarity and promotional context.

## Specific Questions To Answer

1. What causal effect can be learned about terminal-digit pricing format itself?
2. How should the design distinguish a price-ending effect from a generic low-price or sale signal?
3. How should the researcher study whether the effect is stronger for newer or less familiar items?
4. Which claims are credible about the mechanism behind any measured demand change?

## Causal Mechanisms To Distinguish

- A true price-ending or threshold-processing effect tied to the format of the displayed price.
- A low-price or promotional-signal effect in which the ending format is interpreted as a bargain cue.
- An information-limitation effect in which the format matters more when customers know less about the item.
- An endogenous-pricing alternative in which managers choose the format for items or contexts with different underlying demand.

## Data Structure Overview

- Stage 1: The researcher identifies a set of focal product offers that can be presented in multiple otherwise comparable versions.
- Stage 2: Different customer groups receive different offer versions that vary the visible price format for the same focal item.
- Stage 3: The researcher records downstream purchases or item-level demand for the focal products after exposure.
- Stage 4: The researcher can classify items or offers by whether they are relatively new versus previously familiar, and can note whether explicit promotional cues are also present.

## Data Card

| field | description |
|---|---|
| unit of observation | Item-offer exposure or offer-version demand outcome for a focal product. |
| time span | Repeated merchandising or campaign waves; exact dates are withheld. |
| geographic or market scope | Customer samples exposed to a common retail format; exact retailer and channel are withheld. |
| sample construction | Otherwise comparable customer groups receive different versions of the same focal offers. |
| treatment or exposure variable | Indicator for whether the focal offer uses a salient terminal-digit price format or an alternative format. |
| outcome variable | Demand for the focal product, measured through purchases, units sold, or closely related order outcomes. |
| secondary outcomes | Relative effects for new versus familiar items, or for offers with versus without explicit promotional cues. |
| covariates | Item characteristics, familiarity or prior-appearance indicators, customer-group controls if available, and promotional-context indicators. |
| baseline or pre-treatment variables | Item history, prior appearance, prior customer familiarity, and any pre-existing promotional classification. |
| panel or repeated structure | Yes; products or offers may appear across multiple waves or customer-group versions. |
| assignment or variation source | Researcher-controlled variation in price format across otherwise comparable offer versions. |
| assignment level | Product-offer version or customer-group-by-offer version. |
| outcome measurement level | Product demand or transaction outcome linked back to the assigned offer version. |
| recommended clustering or inference level | Offer-version, product, or customer-group level, depending on the realized assignment and aggregation structure. |
| repeated exposure | Possible if products or customers recur across waves. |
| compliance or take-up | Not every exposed customer purchases, but version assignment determines the displayed price format they face. |
| missingness or attrition | Operational limits may prevent every item from being manipulated in every wave. |
| possible spillover or interference | Other items in the same offer may affect perception of the focal item; cross-item promotional framing may also spill over. |

## Variable Groups

### Treatment Or Exposure Variables

- Indicator for salient terminal-digit ending versus alternative ending.
- Indicator for whether the focal offer also carries a markdown or sale cue.
- Interaction terms for ending format with item familiarity or prior appearance.

### Selection Or Sample-Flow Variables

- Customer-group assignment to offer version.
- Inclusion of the focal item in the manipulated offer set.
- Availability of usable purchase outcomes for the focal item.

### Main Outcome Variables

- Item-level purchases or units sold.
- Demand rate for the focal offer.

### Secondary Outcome Variables

- Differential response for newer versus familiar items.
- Differential response when explicit promotional cues are present.

### Baseline Controls And Design Variables

- Item history or prior appearance.
- Product category or comparable-item controls.
- Customer-group fixed characteristics if observed.
- Promotional-context indicators.

## Known Constraints

- The design should match the data structure above.
- The answer must distinguish descriptive associations, randomized or quasi-random causal claims, and mechanism claims.
- The answer should state what cannot be learned from the available information.
- Do not label the final identification strategy by name unless you have justified why the data support it.
- Do not rely on unsupported source-specific facts about the original paper, retailer, channel, customer-sampling rule, or exact price values.

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
