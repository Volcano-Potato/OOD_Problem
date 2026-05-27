<!-- visibility: evaluator-only -->
<!-- do_not_include_in_agent_context: true -->
<!-- case_id: C004 -->

# Source Packet: C004

## Paper Metadata

- paper_key: `blake_nosko_tadelis_2015_paid_search`
- title: Consumer Heterogeneity and Paid Search Effectiveness: A Large Scale Field Experiment
- authors: Thomas Blake, Chris Nosko, Steven Tadelis
- year: 2015
- venue: Econometrica
- registry_domain: `platform_economics`
- registry_design_family: `field_experiment`
- registry_key_failure_mode: `endogenous_exposure`
- source_pdf: `downloads/deepscientist_econ_business_experiment_papers/Blake_Nosko_Tadelis_2015_Consumer_Heterogeneity_and_Paid_Search_Effectiveness_A_Large_Scale_Field_Experiment.pdf`
- source_url: `https://www.nber.org/papers/w20171`
- pdf_pages: 43

## Research Question And Objective

- source_research_question: What is the causal effect of paid search advertising on downstream sales, and how does that effect vary across consumers with different prior familiarity or activity?
- benchmark_research_objective: Given an anonymized search-advertising setting, ask the agent to design a causal measurement strategy that handles search intent endogeneity and heterogeneous treatment effects rather than treating clicks or attributed sales as causal ROI.
- target_mechanism_or_estimand: Incremental effect of paid search on sales, user acquisition, and purchases for users with different prior frequency or recency of activity.
- why_this_case_tests_agent_weakness: Agents often treat paid-search clicks or attributed conversions as causal, ignore that spending is behavior-driven, and miss that average effects can be near zero even when marginal effects are positive for less-informed users.

## Source Locations

| section | pdf_text_pages_used | role in benchmark construction |
|---|---|---|
| abstract | 1 | headline result, endogeneity warning, heterogeneous ad response |
| introduction | 2-4 | search-intent endogeneity and why observational ROI is misleading |
| brand search experiment | 6-7 | placebo-style benchmark showing navigational search has almost zero incremental effect |
| non-brand experimental design | 7-9 | geographic randomization, matched DMA design, core identification structure |
| consumer heterogeneity | 11-13 | prior frequency/recency segmentation as the key heterogeneity result |
| appendix ROI regressions | 21-22 | difference-in-differences implementation and near-zero average causal effect |

## Extracted Passages

[P001]
source_page: 1
section: abstract
why_included: States the central empirical problem and the main heterogeneity result.
text: Because search clicks and purchase intent are correlated, we show that returns from paid search are a fraction of non-experimental estimates. For non-brand keywords we find that new and infrequent users are positively influenced by ads but that more frequent users whose purchasing behavior is not influenced by ads account for most of the advertising expenses, resulting in average returns that are negative.

[P002]
source_page: 2
section: introduction
why_included: Captures the benchmark's main failure mode: behavior-driven ad spend and search-intent endogeneity.
text: The amount spent on internet marketing is a function not only of the advertiser’s campaign, but is also determined by the behavior and intent of consumers because expenditures increase with clicks.

[P003]
source_page: 2
section: introduction
why_included: Explains why observed ad responders may be infra-marginal and why observational attribution is not causal.
text: In many cases, the consumers who choose to click on ads are loyal customers or are otherwise already informed about the company’s product. Advertising may appear to attract these consumers, when in reality they would have found other channels to visit the company’s website.

[P004]
source_page: 5
section: introduction
why_included: Gives the magnitude of observational overstatement relative to experimental estimates.
text: Typical OLS methods result in a ROI of over 4,100 percent without time and geographic controls, and a ROI of over 1,400 percent with such controls. We then used our experimental methods to control for endogeneity and found a ROI of −63 percent, with a 95 percent confidence interval of [−124 percent, −3 percent].

[P005]
source_page: 6
section: brand search experiments
why_included: Provides the near-placebo logic for navigational or brand search.
text: For brand keywords, natural search is close to a perfect substitute for paid search, making brand keyword search engine marketing ineffective for short-term sales.

[P006]
source_page: 7
section: non-brand terms controlled experiment
why_included: Identifies the causal challenge that remains even when ads are more informative than for brand search.
text: Non-brand ads can attract users that are not directly searching for the firm, but the endogeneity problem persists because the ads may attract informed users who may have visited the site even if the ad were not present.

[P007]
source_page: 8
section: experimental design and basic results
why_included: Records the actual randomization structure used to identify the average causal effect.
text: To measure the effect of advertising on non-brand queries, the study implemented a large scale field experiment that exposed a random group of users to ads while a control group did not see ads, using Google’s geographic bid feature and suspending ads in roughly 30 percent of designated market areas.

[P008]
source_page: 8
section: experimental design and basic results
why_included: Records the matched-region comparison structure rather than naive before-after or click-based comparison.
text: Candidate geographic markets were divided into test and control regions using an algorithm that matched historical serial correlation in sales between the two regions, creating a control group that mirrored the test group in seasonality and lending itself to a difference-in-differences estimation of the effect of paid search on sales.

[P009]
source_page: 11
section: consumer response heterogeneity
why_included: Preserves the central substantive result that average zero effects mask strong heterogeneity by prior user activity.
text: The largest effect on sales was for users who had not purchased before. The treatment effect diminishes quickly with purchase frequency as estimates are near zero for users who buy more regularly.

[P010]
source_page: 12
section: consumer response heterogeneity
why_included: Adds the recency version of heterogeneity and the interpretation that ads mainly inform less-active users.
text: Advertising has little effect on active and moderately active customers, but the effect rises with absence and is large again for customers who have not purchased in over a year. Search advertising works only on a firm’s least active customers.

[P011]
source_page: 13
section: where did the non-brand traffic go
why_included: Reminds the builder that even non-brand search requires reasoning about substitution and alternative channels, not just treated clicks.
text: Only experimental variation can quantify the number of users who are actually directed by the presence of search advertising.

## Human Notes

- suspected_linchpin: The anonymous task must preserve that paid-search spending and clicks are endogenous to user intent, and that the causal design requires randomized ad suspension or equivalent exposure variation rather than click-based attribution.
- known_risks: The exact firm name and “brand keyword versus non-brand keyword” framing are source-identifying. Agent-facing tasks should generalize to a well-known online marketplace or platform advertiser without using eBay, Google, SEM, or exact keyword labels.
- extraction_uncertainties: Task 06 should verify whether the benchmark should emphasize DMA-level assignment, user-level heterogeneity by prior frequency/recency, and whether brand-search placebo logic should appear directly in Level 3 or remain evaluator-only.
