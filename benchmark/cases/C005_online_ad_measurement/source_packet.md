<!-- visibility: evaluator-only -->
<!-- do_not_include_in_agent_context: true -->
<!-- case_id: C005 -->

# Source Packet: C005

## Paper Metadata

- paper_key: `johnson_lewis_nubbemeyer_2017_ghost_ads`
- title: Ghost Ads: Improving the Economics of Measuring Online Ad Effectiveness
- authors: Garrett A. Johnson, Randall A. Lewis, Elmar I. Nubbemeyer
- year: 2017
- venue: Journal of Marketing Research
- registry_domain: `platform_economics`
- registry_design_family: `field_experiment`
- registry_key_failure_mode: `endogenous_exposure`
- source_pdf: `downloads/deepscientist_econ_business_experiment_papers/C005_Johnson_Lewis_Nubbemeyer_2017_Ghost_Ads_Improving_the_Economics_of_Measuring_Online_Ad_Effectiveness.pdf`
- source_url: `https://conference.nber.org/confer/2016/EoDs16/Johnson_Lewis_Nubbemeyer.pdf`
- pdf_pages: 41

## Research Question And Objective

- source_research_question: How can advertisers estimate the causal lift from online ads when actual ad exposure is selected by platform auctions and optimization algorithms?
- benchmark_research_objective: Given an anonymized online advertising campaign, ask the agent to design a measurement strategy that compares treated exposed users with appropriate control users who had comparable exposure opportunity.
- target_mechanism_or_estimand: Incremental ad effect on downstream conversions among users who would have been eligible or likely to receive the focal ad.
- why_this_case_tests_agent_weakness: Agents often compare exposed and unexposed users or use all randomized users in a noisy ITT. This case tests whether the agent recognizes endogenous exposure and constructs the correct counterfactual exposure-opportunity group.

## Source Locations

| section | pdf_text_pages_used | role in benchmark construction |
|---|---|---|
| abstract | 1 | research objective, method name, headline comparison |
| introduction | 2-4 | why PSA and naive exposure comparisons fail |
| experimental design | 7-8 | nomenclature for treatment, control, exposure, conversions |
| application | 22 | retargeting campaign setting |
| implementation risk | 20 | predicted ghost ad selection-bias risk |

## Extracted Passages

[P001]
source_page: 1
section: abstract
why_included: Defines the causal measurement target.
text: The advertising measurement problem is to estimate how consumers would have behaved if they had not seen the ads. The proposed method identifies control-group counterparts of exposed treatment users in a randomized experiment.

[P002]
source_page: 1
section: abstract
why_included: Records comparison against standard ad-test approaches.
text: The paper compares the ghost-ad approach with public-service-announcement tests and intent-to-treat A/B tests, emphasizing cost, precision, and compatibility with real-time optimized ad platforms.

[P003]
source_page: 2
section: introduction
why_included: Captures why naive digital advertising data are insufficient.
text: Granular click, visit, and purchase logs do not by themselves solve causal measurement because observed exposed users may differ from unexposed users in baseline purchase propensity.

[P004]
source_page: 2
section: introduction
why_included: Identifies failure of PSA controls under optimization.
text: Performance-optimizing ad platforms may expose different types of users to PSA ads and focal treatment ads, breaking the symmetry required for a valid holdout comparison.

[P005]
source_page: 3
section: introduction
why_included: Captures the linchpin design logic.
text: In the control group, the platform can simulate whether the focal ad would have won the auction. These logged ghost impressions identify control users who had the same exposure opportunity but did not see the focal ad.

[P006]
source_page: 4
section: introduction
why_included: Records the central endogenous-exposure threat.
text: Retargeted-ad viewers may have high sales even without ads because they are a selected group with high purchase intent. A causal design must separate incremental ad effects from this selection.

[P007]
source_page: 7
section: experimental design
why_included: Defines conversion outcomes for agent task construction.
text: The paper treats conversions as downstream interactions with the advertiser, such as website visits, sign-ups, or purchases.

[P008]
source_page: 20
section: predicted ghost ad implementation
why_included: Flags a validity risk for predicted exposure.
text: If predicted ghost-ad exposure is imperfect, comparing treatment users with a mismatched set of predicted control users can introduce selection bias and undermine the experiment.

[P009]
source_page: 22
section: empirical application
why_included: Gives the application setting without requiring the exact brand in agent-facing tasks.
text: The empirical application studies a display retargeting campaign run by an online retailer, with randomized treatment assignment and ad impressions during a short campaign window.

## Human Notes

- suspected_linchpin: The anonymous task must preserve the difference between actual exposure and exposure opportunity. A strong agent should not compare exposed users with all unexposed users.
- known_risks: The phrase "ghost ads" is source-identifying. Agent-facing tasks should describe the counterfactual exposure-opportunity idea without using that label.
- extraction_uncertainties: Task 06 should verify campaign assignment shares, exact outcome windows, and whether the gold answer should allow ITT as partial credit.
