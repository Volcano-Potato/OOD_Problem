<!-- visibility: evaluator-only -->
<!-- do_not_include_in_agent_context: true -->
<!-- case_id: C008 -->

# Gold Reference: C008

## Hidden Answer Summary

This evaluator-only gold reference defines what a valid answer must handle for the retail tax-salience case. A valid answer does not need to reproduce the exact product categories or paper specification, but it must use a comparison structure that separates the visibility intervention from product-category, store, and time shocks.

## Core Research Problem

- Research question: Do consumers underreact to taxes or add-on charges that are not salient because they are excluded from posted shelf prices? Evidence: F002.
- Benchmark objective: Design an empirical strategy estimating the demand effect of making an add-on charge visible at the point of decision. Evidence: F003.
- Target estimand: Causal effect of posting all-in prices on product demand. Evidence: F010-F016.
- Treatment or exposure: Shelf tags or equivalent display showing all-in prices for treated product categories. Evidence: F010-F011.
- Outcome: Demand measured by scanner data on quantity sold and revenue. Evidence: F014.
- Unit of analysis: Product/category by store by time using scanner demand data. Evidence: F005-F007.

## Data Structure

- Observation unit: Product-category/store/time demand observation. Evidence: F005.
- Assignment level: Product-category level within a treatment store. Evidence: F006.
- Outcome measurement level: Product/store/time scanner data. Evidence: F007.
- Time structure: Pre/post around a multi-week intervention. Evidence: F008.
- Required comparison structure: Treated products, same-aisle or similar control products, treatment store, and nearby control stores. Evidence: F009, F012-F013.
- Current uncertainty: Exact regression specification, weighting, standard-error method, and whether triple difference is full-credit requirement remain unresolved. Evidence: U001-U002.

## Original Identification Logic

The source uses a difference-in-differences design comparing treated product demand during the intervention against control products and nearby control stores. It also validates the comparison using control stores and constructs a triple-difference estimate combining within-store and across-store comparisons. Evidence: F017-F020.

## Linchpin Detail

- Linchpin: Use product-category and store/time controls together. Evidence: L001.
- Why it matters: It separates salience effects from category-specific demand shocks and store-wide time shocks. Evidence: F018-F020.
- What fails without it: A treated-store before-after design can mistake unrelated demand changes for salience effects. Evidence: L001, N001.
- Secondary linchpin: Validate trends using control stores without the intervention. Evidence: L002.
- Measurement condition: Track actual paid prices including discounts to avoid confounding salience with price changes. Evidence: L003.

## Must-Have Conditions

- The answer must not rely on a simple before-after comparison in the treated store.
- The answer must include both treated and control products or categories.
- The answer must address store/time shocks, preferably with control stores or equivalent untreated markets.
- The answer must measure demand with transaction/scanner data or similarly objective purchase data.
- The answer must discuss actual paid prices/promotions as possible confounders.

## Acceptable Alternative Designs

| design | conditions under which it is acceptable | supports what claim | cannot support what claim |
|---|---|---|---|
| Difference-in-differences across treated and control categories within stores over time | Control categories must have credible parallel trends and no spillover from treatment tags. | Can estimate demand effect of visible all-in pricing under DID assumptions. | Cannot rule out store-wide time shocks without additional controls. |
| Triple-difference using treated categories, control categories, treatment store, and control stores | Comparable control stores and pre/post data must be available. | Can better separate category shocks and store/time shocks. | Still cannot identify long-run effects if only short intervention window exists. |
| Randomized rollout of all-in price display across stores/categories | Randomization must be at category/store level and account for clustering and spillovers. | Can identify causal demand effect with weaker trend assumptions. | Cannot identify tax-salience mechanism if it does not isolate visibility from actual price changes. |

## Common Invalid Designs

| design or claim | why unacceptable | error label |
|---|---|---|
| Compare demand before and after tags in the treated store only. | Time shocks or store changes could explain demand changes. Evidence: N001. | Timing Endogeneity |
| Compare tagged products with arbitrary unrelated products and no control stores. | Category-specific trends may differ absent intervention. Evidence: N002. | Weak Identification |
| Ignore discounts or actual transaction prices. | Apparent salience effects could be price or promotion effects. Evidence: N003. | Critical Design Omission |
| Use cross-sectional product differences after tagging. | Treated and untreated products differ for reasons unrelated to salience. | Selection |
| Claim the intervention identifies consumer attention without measuring demand or price conditions. | Mechanism is not supported without relevant outcome and price controls. | Overclaim |

## Claim-Evidence Expectations

| expected claim | required supporting evidence | claim type | confidence |
|---|---|---|---|
| Before-after alone is insufficient. | N001, L001 | limitation | high |
| DID or DDD comparison structure is needed. | F017-F020, L001 | identification | high |
| Control stores support trend validation. | F019, L002 | assumption | high |
| Actual paid prices must be tracked. | F015, L003 | measurement/model | medium |

## Scoring Notes

- Full-credit answer: Proposes DID/DDD with treated products, control products, pre/post timing, and control stores or equivalent markets; measures demand objectively; handles prices/promotions.
- Partial-credit answer: Proposes DID with treated and control categories but lacks control-store validation or price/promotion discussion.
- Critical omission: No comparison group beyond before/after.
- Automatic failure: Strong causal claim from treated-store before-after or cross-sectional product comparison.
