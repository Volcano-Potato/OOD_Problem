<!-- visibility: agent-facing -->
<!-- case_id: C008 -->
<!-- variant: no_solution -->

# Anonymous Research Design Task: No-Solution Variant

## Task Rule

Use the information provided below to design a rigorous empirical strategy for this anonymized applied business/economics research problem. Your goal is to produce a defensible research design, not to write a literature review.

Do not assume that a known paper has already solved the task. Ground your reasoning in the background, data description, institutional details, and constraints provided in this packet.

Do not fill in packet-absent operational details, institutional features, or named design devices as if they were known facts. If multiple concrete implementations fit the packet, describe them generically or label them explicitly as illustrative examples rather than assumptions.

If credible causal identification is not possible from the provided information, do not invent an identification strategy. State the strongest defensible descriptive or correlational analysis instead.

## Research Background

Consumers sometimes face add-on charges that are paid at checkout but are not fully visible when they choose products. A retailer wants to know whether displaying the all-in price more prominently changes demand.

The question matters for pricing strategy and consumer response, but observational store practices do not automatically reveal a causal salience effect.

## Research Setting

A retail chain collects product-level weekly sales data from many stores. Some store managers choose to display all-in prices more prominently for certain product groups, while others do not. Store managers make these display decisions based on local sales conditions, operational constraints, and their own judgment.

## Research Objective

Assess whether stores or product groups with more visible all-in pricing have different demand outcomes and whether those differences can be interpreted causally.

## Specific Questions To Answer

1. Are products with more visible all-in pricing associated with lower demand?
2. Can store, product, and time controls make that association causal?
3. What can be learned descriptively from the cross-store, cross-product sales data?
4. What additional design or data would be needed to identify a causal salience effect?

## Data Structure Overview

- Stage 1: Stores and product groups generate routine weekly transaction data.
- Stage 2: Some managers choose to implement more visible all-in pricing displays for selected product groups.
- Stage 3: The retailer records weekly sales, revenue, and price conditions for treated and untreated product groups across stores.
- Stage 4: Historical store and product information are available, but display decisions are managerial choices rather than experimentally assigned.

## Available Data

| field | description |
|---|---|
| unit of observation | Product or product-category by store by week sales record. |
| time span | Multi-week or multi-month retail panel. |
| sample construction | Product groups sold in stores with varying display practices. |
| treatment or exposure variable | Whether the store or category uses more visible all-in price display. |
| outcome variable | Quantity sold, revenue, and transactions. |
| secondary outcomes | Actual paid price, discounting, and category substitution if observed. |
| covariates | Store characteristics, product characteristics, category indicators, local demand conditions, promotions, and time indicators. |
| panel or repeated structure | Repeated store-category-week observations over time. |
| assignment or variation source | Store managers or regional operators choose display practices based on local conditions. |
| assignment level | Store-category-time decision. |
| outcome measurement level | Store-category-week transaction record. |
| missingness or attrition | Missing data can arise from stockouts, product turnover, or incomplete promotion records. |
| possible spillover or interference | Shoppers can substitute across products and stores, and visibility changes can affect nearby categories. |

## Variable Groups

### Treatment Or Exposure Variables

- Visible all-in price display indicator.
- Timing of display adoption.

### Selection Or Sample-Flow Variables

- Inclusion of store-category-week cells.
- Managerial choice to adopt visible display.

### Main Outcome Variables

- Quantity sold.
- Revenue and transactions.

### Secondary Outcome Variables

- Actual paid price.
- Promotion status.
- Category substitution.

### Baseline Controls And Design Variables

- Store and category characteristics.
- Local demand conditions.
- Time indicators and historical sales.

## Identification Limitations

- No randomized assignment or quasi-random variation is provided.
- No credible instrument, threshold, boundary, or externally imposed timing shock is provided.
- Stores choosing visible displays may already differ in underlying demand trends, manager quality, or local competition.
- Even with panel data, adoption timing is a managerial choice tied to the outcome process rather than an exogenous intervention.

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
