<!-- visibility: evaluator-only -->
<!-- do_not_include_in_agent_context: true -->
<!-- case_id: C010 -->

# Source Packet: C010

## Paper Metadata

- paper_key: `duflo_kremer_robinson_2011_fertilizer_timing`
- title: Nudging Farmers to Use Fertilizer: Theory and Experimental Evidence from Kenya
- authors: Esther Duflo, Michael Kremer, Jonathan Robinson
- year: 2011
- venue: American Economic Review
- registry_domain: `development`
- registry_design_family: `mechanism_experiment`
- registry_key_failure_mode: `mechanism_confounding`
- source_pdf: `downloads/deepscientist_econ_business_experiment_papers/Duflo_Kremer_Robinson_2011_Nudging_Farmers_to_Use_Fertilizer_Theory_and_Experimental_Evidence_from_Kenya.pdf`
- source_url: `https://www.nber.org/papers/w15131`
- pdf_pages: 46

## Research Question And Objective

- source_research_question: Why do many farmers underinvest in a seemingly profitable agricultural input, and can small timing-based interventions increase adoption more efficiently than heavy subsidies?
- benchmark_research_objective: Given an anonymized agricultural-input adoption setting, ask the agent to design a study that distinguishes timing and delivery frictions, present-bias or procrastination, and standard price-subsidy explanations.
- target_mechanism_or_estimand: Effects of early small acquisition-cost reductions, later discounts, and timing-choice or reminder interventions on profitable input adoption; mechanism separation between present-bias or procrastination and standard static demand for subsidies.
- why_this_case_tests_agent_weakness: Agents often jump to “large price subsidy raises adoption” or “credit constraints explain low take-up” and miss that the source linchpin is the timing of a small, early intervention rather than the size of the subsidy.

## Source Locations

| section | pdf_text_pages_used | role in benchmark construction |
|---|---|---|
| abstract | 1 | headline research question, timing mechanism, early versus late discount contrast |
| introduction and motivation | 2-5 | profitable but underused technology, present-bias mechanism, policy debate |
| background and returns to input use | 6-8 | profitability, low baseline adoption, apparent contradiction with stated intent |
| model intuition | 9-16 | procrastination and small fixed acquisition costs |
| intervention description | 17-20 | SAFI design, early free delivery, late free delivery, heavier subsidy, reminder |
| main results | 21-27 | adoption impacts of early versus late offers and subsidy comparison |
| alternative explanations and discussion | 34-40 | tests against reminder-only, strong commitment, and pure transaction-cost stories |

## Extracted Passages

[P001]
source_page: 1
section: abstract
why_included: States the core mechanism and the early-versus-late timing contrast.
text: Many farmers fail to take advantage of apparently profitable fertilizer investments, but they do invest in response to small, time-limited discounts on the cost of acquiring fertilizer just after harvest. Later discounts have a smaller impact, and many farmers choose schedules that induce advance purchase.

[P002]
source_page: 1
section: abstract
why_included: States the high-level policy comparison against heavy subsidies.
text: Calibration suggests such small, time-limited discounts yield higher welfare than either laissez faire or heavy subsidies by helping present-biased farmers commit to fertilizer use without inducing those with standard preferences to substantially overuse fertilizer.

[P003]
source_page: 3
section: introduction
why_included: Establishes that the input appears privately profitable on real farms, so low adoption is puzzling.
text: Previous trials on farmers' own plots showed that when fertilizer is used in limited quantities, it generates substantial returns over a season, yet investment remains low even though the technology is well known and divisible.

[P004]
source_page: 4
section: introduction
why_included: Gives the behavioral mechanism that future source facts should preserve.
text: Even if the utility cost of buying fertilizer is small, farmers who plan to use fertilizer may defer the purchase until later, expecting to remain willing to buy, and then fail to follow through if they become impatient at the moment of purchase.

[P005]
source_page: 5
section: introduction
why_included: States the key comparative-static prediction for early small discounts.
text: Small, time-limited discounts offered just after harvest, when farmers have money, can induce sizeable changes in fertilizer use and may work better than much larger discounts later in the season.

[P006]
source_page: 7
section: background on fertilizer use
why_included: Records the empirical tension between high observed returns and low adoption.
text: A limited-quantity top-dressing strategy yields a high return on farmers' own plots, yet only a minority of farmers report using fertilizer in recent seasons.

[P007]
source_page: 8
section: background on fertilizer use
why_included: Preserves the fact that stated intentions exceed realized follow-through.
text: Most farmers say they intend to use fertilizer in the following season, but far fewer actually follow through when the time to purchase or apply arrives.

[P008]
source_page: 17
section: The SAFI program
why_included: Captures the experimental design linchpin.
text: The program offered farmers at harvest the opportunity to buy fertilizer vouchers at the regular price but with free delivery. The key feature was that the offer came early, close to harvest, rather than later when fertilizer would actually be needed.

[P009]
source_page: 18
section: The SAFI program
why_included: Adds the timing-choice and comparison-arm logic.
text: Additional variants allowed farmers to choose a future visit date, offered free delivery later in the season, offered a larger price subsidy later in the season, and included reminder-style interventions.

[P010]
source_page: 21
section: main results
why_included: States the main adoption effect of the early intervention.
text: Offering free delivery at harvest substantially increased fertilizer adoption, while free delivery later in the season had a noticeably smaller effect.

[P011]
source_page: 24
section: main results
why_included: Preserves the comparison against a much larger later subsidy.
text: A much larger reduction in fertilizer cost later in the season generated effects comparable to, but not clearly larger than, the early small intervention tied to the harvest period.

[P012]
source_page: 37
section: alternative explanations
why_included: Rules out simple reminder or transaction-cost-only interpretations.
text: Reminder visits had little effect, and the pattern of results is difficult to reconcile with a pure transaction-cost story in which timing should not matter once the intervention is announced in advance.

## Human Notes

- suspected_linchpin: The anonymous task must preserve that the causal contrast is about timing and acquisition friction, not simply “discount versus no discount.” Early small interventions near harvest are the identification linchpin.
- known_risks: The exact program acronym, country name, crop details, and distinctive free-delivery implementation are source-identifying if copied directly into agent-facing tasks.
- extraction_uncertainties: Task 06 should verify which intervention arms belong in the final benchmark, whether heavy-subsidy comparison should remain evaluator-only in lower levels, and how strongly the gold reference should require evidence against simple reminder or transaction-cost explanations.
