<!-- visibility: evaluator-only -->
<!-- do_not_include_in_agent_context: true -->
<!-- case_id: C008 -->

# Source Facts: C008

## Scope

These facts are extracted only from `source_packet.md`. They are evaluator-only inputs for later `gold_reference.md` and anonymized task construction.

## Research Context

| fact_id | category | fact | evidence_id | confidence |
|---|---|---|---|---|
| F001 | research_context | The empirical setting is retail consumer demand under add-on taxes or charges. | [P001], [P002] | high |
| F002 | research_question | The source question is whether consumers underreact to taxes that are not salient because they are excluded from posted shelf prices. | [P001] | high |
| F003 | benchmark_objective | The benchmark objective is to ask for a design estimating the demand effect of making an add-on charge visible at the point of decision. | [P001], [P002], [P004] | high |
| F004 | mechanism | The mechanism is tax salience: including the tax in the posted shelf price may change consumer demand. | [P001], [P002] | high |

## Data Structure

| fact_id | field | extracted fact | evidence_id | confidence |
|---|---|---|---|---|
| F005 | observation_unit | The likely analysis unit is product-category by store by time, using scanner demand data. | [P004], [P006], [P007] | medium |
| F006 | assignment_level | The intervention varies at the product-category level within a treatment store. | [P003], [P005] | high |
| F007 | outcome_measurement_level | Demand outcomes are measured from scanner data at product/store/time level. | [P004], [P007] | high |
| F008 | time_structure | The intervention occurs over approximately three weeks in early 2006. | [P005] | high |
| F009 | comparison_structure | The design uses treated products, other products in the same aisle, and products in nearby control stores. | [P004], [P006], [P007] | high |

## Treatment / Exposure / Variation

| fact_id | category | fact | evidence_id | confidence |
|---|---|---|---|---|
| F010 | treatment | Treated products receive shelf tags showing tax-inclusive prices below original pretax prices. | [P002], [P003] | high |
| F011 | treated_units | The tagged product groups are taxable categories covering roughly 750 products. | [P003] | high |
| F012 | control_units | Control units include other toiletries in the same aisles and products in nearby stores from the same chain. | [P006], [P007] | high |
| F013 | variation_source | The intervention generates over-time variation in price salience for treated categories relative to control categories and stores. | [P004], [P005], [P006] | high |

## Outcomes And Measurement

| fact_id | outcome | measurement_method | evidence_id | confidence |
|---|---|---|---|---|
| F014 | demand | Demand is measured using scanner data on quantity sold and revenue. | [P004] | high |
| F015 | product_price | Product prices reflect actual paid prices including discounts. | [P007] | high |
| F016 | demand_effect | The source reports that posting tax-inclusive prices reduces demand. | [P001] | high |

## Identification Logic

| fact_id | component | extracted fact | evidence_id | confidence |
|---|---|---|---|---|
| F017 | design_family | The source uses a difference-in-differences design. | [P004] | high |
| F018 | comparison_group | The design compares treated product demand during the intervention against control products and nearby control stores. | [P004], [P006] | high |
| F019 | validation_check | The paper checks whether treatment and control products evolve similarly in control stores without the intervention. | [P008] | high |
| F020 | stronger_design | The source combines treatment-store and control-store comparisons into a triple-difference estimate. | [P009] | high |

## Linchpin Details

| linchpin_id | detail | why_it_matters | what_fails_without_it | evidence_id | confidence |
|---|---|---|---|---|---|
| L001 | Use both product-category and store/time controls. | It separates the salience intervention from category-specific demand shocks and store-wide time shocks. | A treated-store before-after design could mistake unrelated demand changes for salience effects. | [P004], [P006], [P008], [P009] | high |
| L002 | Validate trends using control stores where no intervention occurred. | It supports the identifying assumption that treated and control categories would have evolved similarly absent the intervention. | DID credibility is weak if control categories have different natural trends. | [P008] | high |
| L003 | Track actual paid prices including discounts. | Demand changes should not be mechanically attributed to salience if actual transaction prices change differently. | The design could confound salience with price/promotional changes. | [P007] | medium |

## Robustness / Placebo / Mechanism Checks

| fact_id | check_type | extracted fact | evidence_id | confidence |
|---|---|---|---|---|
| F021 | parallel_comparison_check | The paper compares treatment and control product changes in control stores. | [P008] | high |
| F022 | triple_difference | The paper constructs a triple-difference estimate from the treatment-store and control-store comparisons. | [P009] | high |

## Naive Design Failure Modes

| failure_id | naive_design | why_it_fails | evidence_id | confidence |
|---|---|---|---|---|
| N001 | Compare demand before and after tags in the treated store only. | Time shocks or store-level changes could explain demand changes. | [P004], [P006], [P009] | high |
| N002 | Compare tagged products with unrelated products without control stores. | Category-specific demand trends could differ even without intervention. | [P006], [P008] | high |
| N003 | Ignore discounts or actual paid prices. | Apparent salience effects could be confounded by changes in transaction prices. | [P007] | medium |

## Evaluator Inference

| inference_id | inference | basis_evidence_id | use_in_later_tasks |
|---|---|---|---|
| I001 | Agent-facing tasks should generalize product categories but preserve treated products, control products, stores, and pre/post timing. | [P003], [P004], [P006] | task construction |
| I002 | Full-credit gold answers should require at least DID logic and likely give extra credit for triple-difference structure. | [P004], [P008], [P009] | gold reference |

## Uncertainties

| uncertainty_id | uncertainty | evidence_id | consequence |
|---|---|---|---|
| U001 | Exact regression specification, weighting, and standard-error method are not extracted. | [P004], [P009] | Gold reference should not specify exact model formula until Task 07 verification. |
| U002 | It is not yet decided whether triple difference is required for full credit or accepted as a stronger version of DID. | [P009] | Task 07 should define scoring thresholds. |

## Facts Safe For Agent-Facing Packets

- A retailer can make an add-on charge visible for some product categories.
- Transaction/scanner data are available over time.
- Treated products, control products, treatment store, and control stores can be described generically.
- The task can ask for demand-effect estimation under salience concerns.

## Facts Unsafe For Agent-Facing Packets

- Source-paper title, authors, venue, exact year.
- Exact product categories if leakage risk is high.
- The original exhibit and exact tax rate.
- Any statement that the original design is a Chetty-Looney-Kroft tax-salience triple difference.
