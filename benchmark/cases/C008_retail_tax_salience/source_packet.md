<!-- visibility: evaluator-only -->
<!-- do_not_include_in_agent_context: true -->
<!-- case_id: C008 -->

# Source Packet: C008

## Paper Metadata

- paper_key: `chetty_looney_kroft_2009_tax_salience`
- title: Salience and Taxation: Theory and Evidence
- authors: Raj Chetty, Adam Looney, Kory Kroft
- year: 2009
- venue: American Economic Review
- registry_domain: `public_econ`
- registry_design_family: `DID`
- registry_key_failure_mode: `timing_endogeneity`
- source_pdf: `downloads/deepscientist_econ_business_experiment_papers/Chetty_Looney_Kroft_2009_Salience_and_Taxation_Theory_and_Evidence.pdf`
- source_url: `https://rajchetty.com/wp-content/uploads/2021/04/taxsalience_aer.pdf`
- pdf_pages: 33

## Research Question And Objective

- source_research_question: Do consumers underreact to taxes that are not salient because they are excluded from posted shelf prices?
- benchmark_research_objective: Given an anonymized retail pricing setting, ask the agent to design an empirical strategy for estimating the demand effect of making an add-on charge visible at the point of decision.
- target_mechanism_or_estimand: Causal effect of posting all-in prices on product demand, with comparison against untreated products, untreated stores, and pre/post periods.
- why_this_case_tests_agent_weakness: A simple before-after design confounds the intervention with time shocks. The agent must recover the multi-dimensional comparison structure across treated categories, control categories, stores, and weeks.

## Source Locations

| section | pdf_text_pages_used | role in benchmark construction |
|---|---|---|
| abstract | 1 | research question and headline field-experiment result |
| introduction | 2 | salience mechanism, intervention, data and DID design |
| experiment details | 7-9 | tagged product categories, timing, control stores/products |
| identification and robustness | 10-11 | control-store validation and triple-difference logic |

## Extracted Passages

[P001]
source_page: 1
section: abstract
why_included: Defines the behavioral public-finance question.
text: The paper studies whether consumers underreact to taxes that are not salient and reports that posting tax-inclusive shelf prices in a grocery store reduces demand.

[P002]
source_page: 2
section: introduction
why_included: Captures the mechanism and intervention.
text: The intervention makes the sales tax visible at the shelf by adding tags that show tax-inclusive prices below original pretax prices.

[P003]
source_page: 2
section: introduction
why_included: Records the treated product groups and scope.
text: Tax-inclusive tags are posted for products in three taxable groups: cosmetics, hair care accessories, and deodorants. The intervention covers roughly 750 products.

[P004]
source_page: 2
section: introduction
why_included: Identifies the broad empirical design.
text: The paper analyzes scanner data with a difference-in-differences design comparing treated product demand during the intervention with control products and nearby control stores.

[P005]
source_page: 7
section: experiment details
why_included: Provides timing required for Level 2/3 task construction.
text: The price-tag intervention runs for approximately three weeks in early 2006, with tags posted for all products in the treated categories.

[P006]
source_page: 8
section: identification strategy
why_included: Captures the two control groups.
text: The design uses other products in the same aisle and products in two nearby stores from the same chain as control groups for the treated product categories.

[P007]
source_page: 9
section: data notes
why_included: Clarifies product definitions and price measurement.
text: Treatment products are the tagged taxable categories, while control products are other toiletries in the same aisles. Product prices reflect actual prices paid including discounts.

[P008]
source_page: 10
section: validity check
why_included: Records an identifying-assumption diagnostic.
text: The paper checks whether treatment and control products evolve similarly in control stores where no intervention occurred, supporting the comparison structure.

[P009]
source_page: 11
section: triple difference
why_included: Captures the more robust design target.
text: The paper combines the within-treatment-store comparison with the control-store comparison to construct a triple-difference estimate of the intervention's effect.

## Human Notes

- suspected_linchpin: The benchmark task should force the agent to use product-category, store, and time comparisons rather than a simple before-after analysis in the treated store.
- known_risks: Exact product categories, the original exhibit, and the named authors are recognizable. Agent-facing tasks should generalize categories while preserving treated products, control products, stores, and weeks.
- extraction_uncertainties: Task 06 should verify exact regression specification, weighting, standard errors, and whether triple difference is required for full credit or only strong partial credit.
