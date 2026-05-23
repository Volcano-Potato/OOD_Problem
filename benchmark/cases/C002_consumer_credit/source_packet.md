<!-- visibility: evaluator-only -->
<!-- do_not_include_in_agent_context: true -->
<!-- case_id: C002 -->

# Source Packet: C002

## Paper Metadata

- paper_key: `karlan_zinman_2009_credit_asymmetry`
- title: Observing Unobservables: Identifying Information Asymmetries with a Consumer Credit Field Experiment
- authors: Dean Karlan, Jonathan Zinman
- year: 2009
- venue: Econometrica
- registry_domain: `consumer_finance`
- registry_design_family: `factorial_RCT`
- registry_key_failure_mode: `mechanism_confounding`
- source_pdf: `downloads/deepscientist_econ_business_experiment_papers/Karlan_Zinman_2009_Observing_Unobservables_Identifying_Information_Asymmetries_with_a_Consumer_Credit_Field_Experiment.pdf`
- source_url: `https://sites.dartmouth.edu/jzinman/files/2021/02/KarlanZinman_OU_long.pdf`
- pdf_pages: 49

## Research Question And Objective

- source_research_question: Are repayment outcomes in a consumer credit market driven by adverse selection, moral hazard, or both?
- benchmark_research_objective: Given an anonymized consumer-credit lending setting, ask the agent to design a field experiment that can distinguish borrower selection at take-up from incentive effects after borrowing.
- target_mechanism_or_estimand: Mechanism-specific effects of loan offer terms, final contract terms, and future-loan incentives on borrowing and repayment behavior.
- why_this_case_tests_agent_weakness: A single randomized interest rate is not enough because default responses can mix adverse selection and moral hazard. The agent must propose a staged or factorial design that separates the timing and information channels.

## Source Locations

| section | pdf_text_pages_used | role in benchmark construction |
|---|---|---|
| abstract | 2 | research question, three randomizations, headline findings |
| introduction | 3-5 | why adverse selection and moral hazard are confounded |
| design overview | 4-5 | offer rate, contract rate, and future-price incentive logic |
| implementation | 8-11 | offer mailing, surprise contract rate, blind application checks |

## Extracted Passages

[P001]
source_page: 2
section: abstract
why_included: Defines the core research question and target mechanisms.
text: The paper estimates adverse selection and moral hazard in a consumer credit market using a field experiment designed to identify specific private-information problems.

[P002]
source_page: 2
section: abstract
why_included: Captures the three treatment dimensions.
text: The experiment randomizes direct-mail loan offers along three dimensions: the initial offer interest rate, a contract interest rate revealed only after the borrower accepts the offer, and a dynamic repayment incentive tied to future loan pricing.

[P003]
source_page: 2
section: abstract
why_included: Explains why the design can separate mechanisms.
text: The three randomizations, combined with knowledge of the lender's information set, permit identification of particular private-information mechanisms rather than a single reduced-form interest-rate effect.

[P004]
source_page: 3
section: introduction
why_included: States the central identification problem.
text: A correlation between default and a randomized interest rate can reflect adverse selection before borrowing or moral hazard after borrowing. A single randomized loan price does not by itself distinguish those channels.

[P005]
source_page: 4
section: introduction
why_included: Records the institutional setting.
text: The study was implemented with a financial institution making high-interest, unsecured, fixed-repayment loans to lower-income workers in South Africa.

[P006]
source_page: 4
section: introduction
why_included: Captures the contract-rate surprise logic.
text: Some borrowers responding to high offer rates randomly receive lower contract rates after applying. Borrowers do not know before application that the final contract rate may differ from the offer rate.

[P007]
source_page: 5
section: introduction
why_included: Identifies the adverse-selection comparison.
text: Selection effects are identified by comparing repayment among borrowers who accepted different offer rates but ultimately received the same low contract rate.

[P008]
source_page: 5
section: introduction
why_included: Identifies the moral-hazard comparison.
text: The dynamic repayment incentive changes future borrowing terms without changing the initial repayment burden, so repayment responses to that incentive are interpreted as a moral-hazard channel.

[P009]
source_page: 11
section: implementation checks
why_included: Flags a required validity check for the gold reference.
text: The paper reports checks that application decisions were blind to the contract rate, supporting the claim that applicants did not condition take-up on the later randomized contract rate.

## Human Notes

- suspected_linchpin: The anonymized task must preserve the distinction between offer rate, surprise contract rate, and future-loan incentive. If the agent only proposes "randomize interest rates," it has not solved the mechanism problem.
- known_risks: Exact country, lender description, and three-rate terminology are distinctive. Agent-facing tasks should generalize the setting while keeping the timing and information structure intact.
- extraction_uncertainties: Task 06 should verify exact sample counts, wave-level versus individual-level randomization for the dynamic incentive, and the preferred inference level.
