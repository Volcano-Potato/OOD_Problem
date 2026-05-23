<!-- visibility: agent-facing -->
<!-- case_id: C008 -->
<!-- variant: level3 -->

# Anonymous Research Design Task: Level 3

## Task Rule

You must not search the web, infer the original paper, or use external literature. Use only the information provided below. Your goal is to design a rigorous empirical strategy, not to write a literature review.

If credible causal identification is not possible from the provided information, do not invent an identification strategy. State the strongest defensible descriptive or correlational analysis instead.

## Research Background

Consumers sometimes face add-on charges that are paid at checkout but are not fully visible when they choose products. If shoppers focus mainly on displayed prices, making the full cost more visible at the point of decision may reduce demand even when the underlying economic price is unchanged.

This question matters for retail pricing, consumer attention, and policy design. A retailer or researcher wants to know whether increasing the visibility of an add-on charge changes purchasing behavior, not merely whether demand changes over time for unrelated reasons.

## Research Objective

Design a study to estimate the causal effect of making an add-on charge visible at the point of product choice on consumer demand.

## Data Card

| field | description |
|---|---|
| unit of observation | Product or product-category by store by time-period sales record. |
| time span | Pre-intervention and intervention periods over multiple weeks; exact calendar dates are withheld. |
| geographic or market scope | One or more retail stores from a common operating environment, with potential comparison stores; exact chain and locations are withheld. |
| sample construction | Include products eligible for the display change, comparable non-treated products or categories, and stores/time periods with consistent transaction data. |
| treatment or exposure variable | Whether the product's displayed price information makes the add-on charge visible at the point of choice during a given store-time period. |
| outcome variable | Quantity sold, revenue, transactions, or category demand from scanner or transaction records. |
| covariates | Product price, discounts, promotions, product fixed characteristics, category indicators, store indicators, time indicators, and local demand shifters if available. |
| panel or repeated structure | Repeated product/category observations across stores and time. |
| assignment or variation source | Retailer-controlled display intervention applied to selected products or categories in selected store-time cells. |
| assignment level | Product category or product group within store-time period. |
| outcome measurement level | Product/category by store by time-period transaction record. |
| recommended clustering or inference level | Store-category or product-category level if treatment varies by category; store or store-time level if implementation is grouped. |
| repeated exposure | Products remain exposed to the display condition across multiple selling periods during the intervention. |
| compliance or take-up | Store execution may be imperfect if tags are misplaced, missing, or implemented late. |
| missingness or attrition | Missing data may arise from stockouts, product entry/exit, scanner recording problems, or incomplete promotion records. |
| possible spillover or interference | Shoppers may substitute between treated and untreated products; display changes may draw attention to nearby products or categories. |

## Potential Threats

- Potential timing issue: Demand for treated products may have been changing before the display intervention for reasons unrelated to price visibility.
- Potential selection issue: Products or categories chosen for the display change may differ systematically from comparison products in baseline demand, promotion intensity, or seasonality.
- Potential measurement issue: Observed demand changes may reflect stockouts, scanner-recording errors, changes in discounts, or actual paid prices rather than salience.
- Potential spillover or interference: Shoppers may substitute from treated products to nearby untreated products, or the display change may alter attention to the broader aisle or category.
- Potential compliance issue: Store staff may implement display changes inconsistently across products or time periods.
- Potential scope issue: A short intervention window may estimate only short-run demand responses and may not reveal long-run consumer learning or adaptation.

## Known Constraints

- The design should match the data structure and threats above.
- The answer must distinguish causal claims from descriptive claims.
- The answer should state what cannot be learned from the available information.
- Do not assume that a simple before-after comparison is causal.
- Do not rely on external facts about any named retailer, jurisdiction, product category, tax rule, or prior paper.

## Required Output

In addition to the standard output below, explicitly explain how your design addresses each listed threat. If a threat cannot be addressed with the available data, say so.

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
