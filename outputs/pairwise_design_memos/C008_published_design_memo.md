# Published Design Memo

## Research Question
Research question: Do consumers underreact to taxes or add-on charges that are not salient because they are excluded from posted shelf prices? Evidence: F002.

## Target Estimand
Target estimand: Causal effect of posting all-in prices on product demand. Evidence: F010-F016.

## Treatment And Outcomes
- Treatment or exposure: Shelf tags or equivalent display showing all-in prices for treated product categories. Evidence: F010-F011.
- Outcome: Demand measured by scanner data on quantity sold and revenue. Evidence: F014.
- Unit of analysis: Product/category by store by time using scanner demand data. Evidence: F005-F007.

## Identification Logic
The source uses a difference-in-differences design comparing treated product demand during the intervention against control products and nearby control stores. It also validates the comparison using control stores and constructs a triple-difference estimate combining within-store and across-store comparisons. Evidence: F017-F020.

## Key Data Structure
- Observation unit: Product-category/store/time demand observation. Evidence: F005.
- Assignment level: Product-category level within a treatment store. Evidence: F006.
- Outcome measurement level: Product/store/time scanner data. Evidence: F007.
- Time structure: Pre/post around a multi-week intervention. Evidence: F008.
- Required comparison structure: Treated products, same-aisle or similar control products, treatment store, and nearby control stores. Evidence: F009, F012-F013.
- Current uncertainty: Exact regression specification, weighting, standard-error method, and whether triple difference is full-credit requirement remain unresolved. Evidence: U001-U002.

## Linchpin Conditions
- Linchpin: Use product-category and store/time controls together. Evidence: L001.
- Why it matters: It separates salience effects from category-specific demand shocks and store-wide time shocks. Evidence: F018-F020.
- What fails without it: A treated-store before-after design can mistake unrelated demand changes for salience effects. Evidence: L001, N001.
- Secondary linchpin: Validate trends using control stores without the intervention. Evidence: L002.
- The answer must not rely on a simple before-after comparison in the treated store.
- The answer must include both treated and control products or categories.
- The answer must address store/time shocks, preferably with control stores or equivalent untreated markets.
- The answer must measure demand with transaction/scanner data or similarly objective purchase data.

## Defensibility Assessment
Linchpin: Use product-category and store/time controls together. Evidence: L001. Why it matters: It separates salience effects from category-specific demand shocks and store-wide time shocks. Evidence: F018-F020. The answer must not rely on a simple before-after comparison in the treated store. The answer must include both treated and control products or categories.

## Proposed Design
- Treatment or exposure: Shelf tags or equivalent display showing all-in prices for treated product categories. Evidence: F010-F011.
- Outcome: Demand measured by scanner data on quantity sold and revenue. Evidence: F014.
- Unit of analysis: Product/category by store by time using scanner demand data. Evidence: F005-F007.
- Required comparison structure: Treated products, same-aisle or similar control products, treatment store, and nearby control stores. Evidence: F009, F012-F013.
- Current uncertainty: Exact regression specification, weighting, standard-error method, and whether triple difference is full-credit requirement remain unresolved. Evidence: U001-U002.
- The answer must not rely on a simple before-after comparison in the treated store.
- The answer must include both treated and control products or categories.

## What Cannot Be Claimed Or Omitted
- Compare demand before and after tags in the treated store only. Why invalid: Time shocks or store changes could explain demand changes. Evidence: N001.
- Compare tagged products with arbitrary unrelated products and no control stores. Why invalid: Category-specific trends may differ absent intervention. Evidence: N002.
- Ignore discounts or actual transaction prices. Why invalid: Apparent salience effects could be price or promotion effects. Evidence: N003.
- Use cross-sectional product differences after tagging. Why invalid: Treated and untreated products differ for reasons unrelated to salience.
