<!-- visibility: evaluator-only -->
<!-- do_not_include_in_agent_context: true -->
<!-- case_id: C019 -->

# Source Packet: C019

## Paper Metadata

- paper_key: `hui_inman_huang_suher_2013_store_travel_distance`
- title: The Effect of In-Store Travel Distance on Unplanned Spending: Applications to Mobile Promotion Strategies
- authors: Sam K. Hui, J. Jeffrey Inman, Yanliu Huang, Jacob Suher
- year: 2013
- venue: Journal of Marketing
- registry_domain: `marketing`
- registry_design_family: `IV`
- registry_key_failure_mode: `endogenous_exposure`
- source_pdf: `downloads/deepscientist_econ_business_experiment_papers/Hui_Inman_Huang_Suher_2013_The_Effect_of_In_Store_Travel_Distance_on_Unplanned_Spending_Applications_to_Mobile_Promotion_Strategies.pdf`
- source_url: `https://doi.org/10.1509/jm.11.0496`
- pdf_pages: 16

## Research Question And Objective

- source_research_question: What is the causal effect of in-store travel distance on unplanned spending, and can targeted mobile promotions increase unplanned purchases by lengthening shoppers' paths?
- benchmark_research_objective: Given an anonymized retail-navigation setting, ask the agent to design a causal study that handles endogenous shopper paths rather than treating observed route length as exogenous exposure.
- target_mechanism_or_estimand: Incremental effect of longer in-store path length on unplanned spending, plus applied implications for interventions that induce shoppers to visit additional store areas.
- why_this_case_tests_agent_weakness: Agents often regress unplanned spending on observed path length or time in store, ignore simultaneity and omitted in-store stimuli, and miss that the key identification source is a pre-trip reference path built from planned baskets and store layout.

## Source Locations

| section | pdf_text_pages_used | role in benchmark construction |
|---|---|---|
| abstract | 1 | headline research question, endogeneity warning, IV plus field-experiment summary |
| motivation and literature gap | 1-3 | unplanned spending, external memory cues, why travel distance may matter |
| endogeneity discussion | 3-4 | omitted variables, reversed causality, measurement error |
| instrumental-variable setup | 4-5 | reference path logic, relevance and exclusion conditions |
| field study procedure | 5-7 | planned basket survey, path tracking, receipts, slack controls |
| main observational results | 7-10 | elasticity estimate, IV versus OLS gap, control structure |
| simulation and mobile-promotion application | 10-12 | marketing implication of farther promotions |
| field experiment | 12-13 | near-path versus far-path coupon treatment |
| discussion and limitations | 13-14 | generalizability, incremental versus borrowed spending, irritation risk |
| appendix | 14-16 | exact reference-path construction, TSP and one-step-look-ahead heuristics |

## Extracted Passages

[P001]
source_page: 1
section: abstract
why_included: States the main causal question and why endogeneity matters.
text: Encouraging shoppers to travel more of the store may increase unplanned spending, but estimating the direct effect of in-store travel distance on unplanned spending is complicated by the endogeneity of in-store travel distance.

[P002]
source_page: 1
section: abstract
why_included: Preserves the observational IV result and the practical application.
text: The authors collect path data and develop an instrumental variable approach. The estimated elasticity of unplanned spending with respect to travel distance is substantially higher than the uncorrected ordinary least squares estimate.

[P003]
source_page: 2-3
section: background and literature review
why_included: Gives the substantive mechanism.
text: Shoppers often use physical products in the store as external memory cues that create or revive needs, so traveling through more store areas may expose them to more product stimuli and increase unplanned purchases.

[P004]
source_page: 3
section: endogeneity of in-store travel distance
why_included: States the three key endogeneity channels.
text: In-store path length is endogenous because omitted in-store and out-of-store variables can affect both unplanned purchases and path length, causality may run from unplanned purchases to additional travel, and path measures are noisy.

[P005]
source_page: 4
section: instrumental-variable logic
why_included: Preserves the hidden design linchpin.
text: The instrument is based on the length of a reference path determined before the trip begins using store layout, planned purchases, and a behavioral rule for how a shopper would collect planned items.

[P006]
source_page: 4-5
section: instrument validity
why_included: Explains why the reference path can satisfy relevance and exclusion.
text: Reference-path length is strongly correlated with actual path length, and because it is determined before the shopping trip starts, it can precede unplanned spending and avoid reversed-causality concerns if suitable controls are included.

[P007]
source_page: 5-6
section: field study procedure
why_included: Gives the data structure used for the observational study.
text: Shoppers report planned purchases at store entry, path length is tracked during the trip, receipts reveal total spending, and unplanned spending is computed by subtracting planned-category spending from total spending.

[P008]
source_page: 5
section: field study procedure
why_included: Adds the control logic around in-store slack.
text: Given the same trip budget, a shopper with more planned purchases has less slack left for unplanned spending, so budget slack based on planned expenditure is an important control variable.

[P009]
source_page: 7-8
section: main results
why_included: States the IV versus OLS gap and the main causal claim.
text: The coefficient on travel distance is positive in both OLS and IV, but the IV estimate is materially larger, confirming that naive observational estimates are biased.

[P010]
source_page: 8-10
section: robustness
why_included: Preserves the comparison against shopping time and other controls.
text: Travel distance performs better than shopping time as a predictor of unplanned spending, and the results remain when controlling for basket size or studying counts of unplanned categories.

[P011]
source_page: 10-12
section: simulation and promotion strategy
why_included: Connects the causal estimate to a practical intervention.
text: Because some categories are located far from the shopper's planned path, targeted promotions can be used to induce additional travel and thereby increase unplanned spending more than a benchmark relocation strategy.

[P012]
source_page: 12-13
section: field experiment
why_included: Gives the randomized validation or application result.
text: A controlled field experiment compares a coupon for an unplanned category far from the shopper's planned path with a coupon for a similar category near that path, and the farther coupon increases unplanned spending more.

[P013]
source_page: 13-14
section: discussion and limitations
why_included: Preserves key caveats.
text: Additional unplanned spending may partly reflect borrowing from planned or future purchases, and interventions that lengthen paths can also reduce shopping convenience or irritate shoppers.

## Human Notes

- suspected_linchpin: The anonymous task must preserve that observed path length is choice-driven and endogenous, and that the key identifying variation comes from a pre-trip reference path or other exogenous path-inducing design rather than from raw path logs.
- known_risks: The exact RFID technology, store map, TSP and one-step-look-ahead labels, and the mobile-promotion framing are all source-identifying if copied too literally into agent-facing tasks.
- extraction_uncertainties: Task 06 should verify how strongly the gold reference should require the reference-path IV rather than a randomized farther-versus-nearer promotion design, and whether shopping-time comparisons should remain evaluator-only or appear in Level 3 as a threat.
