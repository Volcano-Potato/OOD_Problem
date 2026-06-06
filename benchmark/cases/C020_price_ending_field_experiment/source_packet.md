<!-- visibility: evaluator-only -->
<!-- do_not_include_in_agent_context: true -->
<!-- case_id: C020 -->

# Source Packet: C020

## Paper Metadata

- paper_key: `anderson_simester_2003_price_endings`
- title: Effects of $9 Price Endings on Retail Sales: Evidence from Field Experiments
- authors: Eric T. Anderson, Duncan I. Simester
- year: 2003
- venue: Quantitative Marketing and Economics
- registry_domain: `marketing`
- registry_design_family: `field_experiment`
- registry_key_failure_mode: `mechanism_confounding`
- source_pdf: `downloads/deepscientist_econ_business_experiment_papers/C020_Anderson_Simester_2003_Effects_of_9_Price_Endings_on_Retail_Sales_Evidence_from_Field_Experiments.pdf`
- source_url: `https://doi.org/10.1023/A:1023581927405`
- pdf_pages: 18

## Research Question And Objective

- source_research_question: Do prices ending in 9 increase demand, and if so, is the effect stronger when customers have less information and weaker when other low-price or sale cues are already present?
- benchmark_research_objective: Given an anonymized retail-pricing setting, ask the agent to design a causal study that isolates the effect of a salient terminal-digit pricing format from generic low-price, markdown, or sale-signal interpretations.
- target_mechanism_or_estimand: Incremental demand effect of using a salient terminal-digit price ending on otherwise comparable offers, plus moderation by item familiarity and promotional context.
- why_this_case_tests_agent_weakness: Agents often treat any difference between odd-ending prices and nearby alternatives as proof of a psychological threshold effect, while ignoring confounding from sale cues, item novelty, and differences between product-level assignment and transaction-level inference.

## Source Locations

| section | pdf_text_pages_used | role in benchmark construction |
|---|---|---|
| abstract | 1 | headline research question, three-field-study result, new-item moderation, sale-cue moderation |
| introduction | 1-2 | motivation, pilot evidence, why price-ending effects remain empirically unsettled |
| overview of studies | 3 | how customer samples and identical items were varied across versions, why the design overcomes historical-price endogeneity |

## Extracted Passages

[P001]
source_page: 1
section: abstract
why_included: States the main question, the field-experiment design, and the two headline findings.
text: The paper presents three field studies in which price endings were experimentally manipulated. Demand increased in all three experiments, the effect was stronger for new items than for items sold in previous years, and there is some evidence that the effect is weaker when sale cues are present.

[P002]
source_page: 1
section: abstract
why_included: Preserves the hidden mechanism interpretation.
text: The authors suggest that salient terminal-digit endings may be more effective when customers have limited information, which helps explain why retailers do not use those endings on every item.

[P003]
source_page: 1
section: introduction
why_included: Establishes that the source is motivated by a lack of conclusive evidence despite widespread use.
text: Although many retail prices end in 9, prior empirical evidence on whether such endings affect demand was limited and inconclusive.

[P004]
source_page: 1-2
section: introduction
why_included: Preserves the motivating pilot logic and the importance of large price manipulations that remove the 9 ending.
text: In a pilot catalog test, otherwise similar dresses were offered across different catalog versions, and removing the 9 ending reduced sales even when the alternative prices were both higher and lower in absolute level.

[P005]
source_page: 2
section: introduction
why_included: Preserves the central heterogeneity question for later task construction.
text: The studies investigate whether the 9-ending effect varies depending on how often an item has appeared before and whether the effect is moderated by sale cues that claim an item is discounted.

[P006]
source_page: 2
section: introduction
why_included: Preserves that the studies manipulate prices by nontrivial dollar amounts rather than tiny cent differences.
text: The evidence comes from large-scale studies with dollar-level price changes rather than very small cent changes, and the results are described as consistent across the three experiments.

[P007]
source_page: 3
section: overview of studies
why_included: Gives the assignment logic that supports causal interpretation.
text: Identical items were shown in different offer versions mailed to randomly selected customer samples, with one control version using the retailer's standard pricing policy and one or more treatment versions manipulating the price ending.

[P008]
source_page: 3
section: overview of studies
why_included: Explains why the source is not just a historical observational pricing comparison.
text: Because the same items could be offered at different prices across randomized versions, the design avoids the endogeneity problems that arise when analyzing historical price data chosen by managers.

[P009]
source_page: 3
section: overview of studies
why_included: Preserves the strong source-identifying operational detail while keeping it evaluator-only.
text: Customers were randomly assigned to receive different offer versions, and the randomization was implemented at a customer-sample level rather than by letting managers choose which customers saw which prices.

[P010]
source_page: 3
section: overview of studies
why_included: Preserves that the experimental environment still had practical constraints.
text: Managers restricted which prices and pages could be changed, so the field experiments retained real-world operational constraints rather than full laboratory control.

## Human Notes

- suspected_linchpin: The anonymized task must preserve that the causal design comes from experimentally varying a salient terminal-digit pricing format across otherwise comparable offers, while forcing the agent to separate pure price-ending effects from low-price or markdown signals.
- known_risks: Exact references to "$9", mail-order catalogs, women's clothing, zip+4 assignment, and named catalog titles are all source-identifying if copied into agent-facing tasks.
- extraction_uncertainties: Task 06 should verify whether full-credit answers must explicitly model item newness or whether recognizing promotional-context confounding is sufficient. It should also decide how strongly to require a factorial separation between ending format and sale labeling.
