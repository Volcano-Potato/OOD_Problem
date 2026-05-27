<!-- visibility: agent-facing -->
<!-- case_id: C020 -->
<!-- variant: no_solution -->

# Anonymous Research Design Task: No-Solution Variant

## Task Rule

Use the information provided below to design a rigorous empirical strategy for this anonymized applied business/economics research problem. Your goal is to produce a defensible research design, not to write a literature review.

Do not assume that a known paper has already solved the task. Ground your reasoning in the background, data description, institutional details, and constraints provided in this packet.

Do not fill in packet-absent operational details, institutional features, or named design devices as if they were known facts. If multiple concrete implementations fit the packet, describe them generically or label them explicitly as illustrative examples rather than assumptions.

If credible causal identification is not possible from the provided information, do not invent an identification strategy. State the strongest defensible descriptive or correlational analysis instead.

## Research Background

A retailer wants to know whether using a salient terminal-digit pricing format increases demand. The available data look rich: there are historical records on product prices, item characteristics, item history, promotional labeling, and realized sales across many waves.

The business question is important, but rich retail pricing data do not solve the causal problem if managers choose which items receive the pricing format and when that format appears together with promotional cues.

## Research Setting

The retailer sets product prices repeatedly over time. Managers choose whether a focal item uses a salient terminal-digit ending, whether it is shown as a markdown or promotion, and how aggressively it is priced relative to neighboring alternatives. The researcher observes item-level sales, item history, and many controls, but there is no experimental assignment and no externally imposed pricing rule in the available data.

## Research Objective

Assess whether products shown with the salient terminal-digit format sell more and whether those differences can be interpreted causally.

## Specific Questions To Answer

1. Are items with the salient terminal-digit format associated with higher demand?
2. Can rich historical controls and item-history information make that relationship causal?
3. What can the data still support descriptively or predictively?
4. What additional design or intervention would be needed to estimate a credible causal effect of the pricing format?

## Data Structure Overview

- Stage 1: The researcher observes historical item characteristics, prior appearance, and pricing histories.
- Stage 2: During repeated merchandising waves, managers choose price levels, ending formats, and promotional framing for focal items.
- Stage 3: The researcher records item-level sales or demand outcomes for each wave.
- Stage 4: The researcher can classify items by novelty, familiarity, and promotional context.

## Available Data

| field | description |
|---|---|
| unit of observation | Item-by-wave or offer-by-wave sales observation. |
| time span | Historical pricing and sales records across repeated merchandising waves. |
| sample construction | Items are observed under live pricing decisions with no experimental holdout in the available data. |
| treatment or exposure variable | Terminal-digit ending format, price level, markdown status, or promotional framing chosen by managers. |
| outcome variable | Item-level demand, purchases, or units sold. |
| secondary outcomes | Item response by novelty, familiarity, category, or promotional context. |
| covariates | Item characteristics, item history, historical demand, category controls, and promotional indicators. |
| panel or repeated structure | Yes; repeated item-by-wave observations. |
| assignment or variation source | Price format and promotion decisions are made by managers based on merchandising strategy and expected demand rather than experimental assignment. |
| assignment level | Item, item-by-wave, or offer-by-wave. |
| outcome measurement level | Item-by-wave demand outcome. |
| missingness or attrition | Some items may enter or exit the assortment, and promotion metadata may be incomplete. |
| possible spillover or interference | Pricing and promotion of one item can affect demand for nearby or substitute items. |

## Variable Groups

### Treatment Or Exposure Variables

- Terminal-digit ending format.
- Price level and markdown status.
- Promotional framing and display indicators.

### Selection Or Sample-Flow Variables

- Item inclusion in the observed assortment.
- Item-history and novelty classification.
- Inclusion in promotion metadata systems.

### Main Outcome Variables

- Item-level purchases or units sold.
- Demand rate or sales volume.

### Secondary Outcome Variables

- Demand by item familiarity or promotional context.
- Category-level substitution summaries if observed.

### Baseline Controls And Design Variables

- Item history and prior appearance.
- Historical demand and seasonality.
- Category controls and product characteristics.

## Identification Limitations

- No randomized assignment or quasi-random variation is provided.
- No credible instrument, threshold, or externally imposed timing shock is provided.
- Managers choose ending formats and markdown cues in response to expected demand and merchandising goals.
- Observed demand differences cannot separately identify terminal-digit effects from low-price or promotional signaling.

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
