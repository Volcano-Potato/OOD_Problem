<!-- visibility: agent-facing -->
<!-- case_id: C008 -->
<!-- variant: level2 -->

# Anonymous Research Design Task: Level 2

## Task Rule

You must not search the web, infer the original paper, or use external literature. Use only the information provided below. Your goal is to design a rigorous empirical strategy, not to write a literature review.

Do not assume that a known paper has already solved the task. Treat this as an anonymous applied business/economics research problem.

If credible causal identification is not possible from the provided information, do not invent an identification strategy. State the strongest defensible descriptive or correlational analysis instead.

## Research Background

Consumers sometimes face add-on charges that are paid at checkout but are not fully visible when they choose products. If shoppers focus mainly on the posted shelf price, making the full cost more visible at the point of decision may change demand even when the underlying economic price is unchanged.

The research problem is to estimate a salience effect rather than a generic correlation between an in-store intervention and changing sales.

## Research Setting

A retailer can change how price information is displayed for some products or categories while observing sales over time. Transaction or scanner data are available, and untreated products or stores may provide comparison groups.

## Research Objective

Design a study to estimate the causal effect of making an add-on charge visible at the point of product choice on consumer demand.

## Specific Questions To Answer

1. How should the researcher estimate the effect of visible all-in pricing on product demand?
2. What comparison groups are needed to separate the intervention from unrelated store, category, and time shocks?
3. How should the design distinguish salience effects from actual price or promotion changes?
4. What claims can be made about short-run demand responses, and what remains uncertain?

## Causal Mechanisms To Distinguish

- Consumers may react to the visibility of the total price rather than to a change in the economic price itself.
- Sales may move because of store-wide or time-specific shocks unrelated to salience.
- Treated product groups may differ from untreated groups in baseline demand trends.
- Measured demand effects may be confounded by promotions, discounts, or substitution across products.

## Data Structure Overview

- Stage 1: The retailer records pre-intervention transaction outcomes for treated and untreated products or categories.
- Stage 2: Selected products or categories in one or more stores receive a display change that makes the add-on charge visible at the point of decision.
- Stage 3: The researcher observes transaction outcomes during the intervention window for treated and untreated products.
- Stage 4: Comparison stores, untreated categories, or post-intervention checks may be available to assess whether the observed sales change is specific to the intervention.

## Data Card

| field | description |
|---|---|
| unit of observation | Product or product-category by store by time-period sales record. |
| time span | Pre-intervention and intervention periods over multiple weeks; exact calendar dates are withheld. |
| geographic or market scope | One or more retail stores from a common operating environment, with potential comparison stores; exact chain and locations are withheld. |
| sample construction | Include products eligible for the display change, comparable non-treated products or categories, and stores or time periods with consistent transaction data. |
| treatment or exposure variable | Whether the product's displayed price information makes the add-on charge visible at the point of choice during a given store-time period. |
| outcome variable | Quantity sold, revenue, transactions, or category demand from scanner or transaction records. |
| secondary outcomes | Category substitution, product-level demand shifts, and any auxiliary price-display or execution indicators if observed. |
| covariates | Product price, discounts, promotions, product fixed characteristics, category indicators, store indicators, time indicators, and local demand shifters if available. |
| baseline or pre-treatment variables | Pre-intervention product demand, pre-period price conditions, and baseline category or store characteristics if available. |
| panel or repeated structure | Repeated product or category observations across stores and time. |
| assignment or variation source | Retailer-controlled display intervention applied to selected products or categories in selected store-time cells. |
| assignment level | Product category or product group within store-time period. |
| outcome measurement level | Product or category by store by time-period transaction record. |
| recommended clustering or inference level | Store-category or product-category level if treatment varies by category; store or store-time level if implementation is grouped. |
| repeated exposure | Products remain exposed to the display condition across multiple selling periods during the intervention. |
| compliance or take-up | Store execution may be imperfect if tags are misplaced, missing, or implemented late. |
| missingness or attrition | Missing data may arise from stockouts, product entry or exit, scanner recording problems, or incomplete promotion records. |
| possible spillover or interference | Shoppers may substitute between treated and untreated products; display changes may draw attention to nearby products or categories. |

## Variable Groups

### Treatment Or Exposure Variables

- Indicator for visible all-in price display.
- Treatment timing and treated-category indicators.

### Selection Or Sample-Flow Variables

- Whether a product-category-store cell is included in the analysis window.
- Whether the display intervention is actually implemented in that cell.

### Main Outcome Variables

- Quantity sold.
- Revenue or transaction counts.

### Secondary Outcome Variables

- Nearby-category substitution.
- Product-level demand composition.
- Any execution or visibility proxies if observed.

### Baseline Controls And Design Variables

- Product, category, store, and time indicators.
- Actual paid price, discounts, and promotions.
- Pre-period sales levels or trends if available.

## Known Constraints

- The design should match the data structure above.
- The answer must distinguish descriptive associations, causal claims, and mechanism claims.
- The answer should state what cannot be learned from the available information.
- Do not label the final identification strategy by name unless you justify why the data support it.
- Do not rely on external facts about the original paper, store chain, or jurisdiction.

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
