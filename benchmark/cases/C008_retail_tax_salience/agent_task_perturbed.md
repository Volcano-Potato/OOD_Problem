<!-- visibility: agent-facing -->
<!-- case_id: C008 -->
<!-- variant: perturbed -->

# Anonymous Research Design Task: Perturbed Variant

## Task Rule

Use the information provided below to design a rigorous empirical strategy for this anonymized applied business/economics research problem. Your goal is to produce a defensible research design, not to write a literature review.

Do not assume that a known paper has already solved the task. Ground your reasoning in the background, data description, institutional details, and constraints provided in this packet.

Do not fill in packet-absent operational details, institutional features, or named design devices as if they were known facts. If multiple concrete implementations fit the packet, describe them generically or label them explicitly as illustrative examples rather than assumptions.

If credible causal identification is not possible from the provided information, do not invent an identification strategy. State the strongest defensible descriptive or correlational analysis instead.

## Research Background

Consumers sometimes face add-on charges that are paid at checkout but are not fully visible when they choose products. If shoppers focus mainly on the posted shelf price, making the full cost more visible at the point of decision may change demand even when the underlying economic price is unchanged.

The research problem is to estimate a salience effect rather than a generic correlation between an in-store intervention and changing sales.

## Research Setting

A retailer can change how price information is displayed for some products or categories while observing sales over time. Transaction or scanner data are available, and untreated products may provide comparison groups inside the same store.

## Research Objective

Design a study to estimate the causal effect of making an add-on charge visible at the point of product choice on consumer demand.

## Specific Questions To Answer

1. How should the researcher estimate the effect of visible all-in pricing on product demand?
2. What comparison groups remain available if no untreated comparison stores are observed?
3. How should the design distinguish salience effects from actual price or promotion changes?
4. Which claims can still be made credibly, and which become weaker without untreated markets?

## Data Structure Overview

- Stage 1: The retailer records pre-intervention transaction outcomes for treated and untreated products or categories in the focal store.
- Stage 2: Selected products or categories in that store receive a display change that makes the add-on charge visible at the point of decision.
- Stage 3: The researcher observes transaction outcomes during the intervention window for treated and untreated products in the same store.
- Stage 4: The data no longer include untreated comparison stores from the same operating environment.

## Data Card

| field | description |
|---|---|
| unit of observation | Product or product-category by store by time-period sales record. |
| time span | Pre-intervention and intervention periods over multiple weeks. |
| sample construction | Include treated products or categories and comparable untreated products or categories within the focal store, using consistent transaction data over time. |
| treatment or exposure variable | Whether the product's displayed price information makes the add-on charge visible at the point of choice during a given store-time period. |
| outcome variable | Quantity sold, revenue, transactions, or category demand from scanner or transaction records. |
| secondary outcomes | Category substitution, product-level demand shifts, and any auxiliary execution indicators if observed. |
| assignment or variation source | Retailer-controlled display intervention applied to selected products or categories in the focal store. |
| assignment level | Product category or product group within store-time period. |
| outcome measurement level | Product or category by store by time-period transaction record. |
| panel or repeated structure | Repeated product or category observations over time in the focal store. |
| compliance or take-up | Store execution may be imperfect if tags are misplaced, missing, or implemented late. |
| spillover or interference | Shoppers may substitute between treated and untreated products; display changes may draw attention to nearby products or categories. |

## Variable Groups

### Treatment Or Exposure Variables

- Indicator for visible all-in price display.
- Treatment timing and treated-category indicators.

### Selection Or Sample-Flow Variables

- Whether a product-category-time cell is included in the analysis window.
- Whether the display intervention is actually implemented in that cell.

### Main Outcome Variables

- Quantity sold.
- Revenue or transaction counts.

### Secondary Outcome Variables

- Nearby-category substitution.
- Product-level demand composition.

### Baseline Controls And Design Variables

- Product, category, and time indicators.
- Actual paid price, discounts, and promotions.
- Pre-period sales levels or trends if available.

## Perturbed Condition

The data no longer include untreated comparison stores. The researcher observes treated and untreated product groups over time only within the focal store.

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
