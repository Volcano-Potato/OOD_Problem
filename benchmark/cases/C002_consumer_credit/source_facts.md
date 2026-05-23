<!-- visibility: evaluator-only -->
<!-- do_not_include_in_agent_context: true -->
<!-- case_id: C002 -->

# Source Facts: C002

## Scope

These facts are extracted only from `source_packet.md`. They are evaluator-only inputs for later `gold_reference.md` and anonymized task construction.

## Research Context

| fact_id | category | fact | evidence_id | confidence |
|---|---|---|---|---|
| F001 | research_context | The empirical setting is consumer credit lending with direct-mail loan offers. | [P002], [P005] | high |
| F002 | research_question | The source question is whether repayment outcomes are driven by adverse selection, moral hazard, or both. | [P001] | high |
| F003 | benchmark_objective | The benchmark objective is to ask for a credit-market experiment that separates borrower selection at take-up from incentive effects after borrowing. | [P001], [P004], [P007], [P008] | high |
| F004 | mechanism | A single interest-rate response can confound adverse selection before borrowing with moral hazard after borrowing. | [P004] | high |

## Data Structure

| fact_id | field | extracted fact | evidence_id | confidence |
|---|---|---|---|---|
| F005 | observation_unit | The relevant observed unit is a loan offer, application, or loan repayment observation for a potential borrower. | [P002], [P006], [P007] | medium |
| F006 | assignment_level | Offer terms are randomized at the borrower-offer level for the initial offer and contract-rate dimensions. | [P002], [P006] | medium |
| F007 | outcome_measurement_level | Repayment/default behavior is measured at the borrower-loan level. | [P004], [P007], [P008] | high |
| F008 | time_structure | The design has a pre-borrowing offer stage, a post-application contract-rate stage, and a later repayment/future-loan-incentive stage. | [P002], [P006], [P008] | high |
| F009 | institutional_setting | The experiment was implemented with a financial institution offering high-interest, unsecured, fixed-repayment loans to lower-income workers. | [P005] | high |

## Treatment / Exposure / Variation

| fact_id | category | fact | evidence_id | confidence |
|---|---|---|---|---|
| F010 | treatment | The initial offer interest rate is randomized in direct-mail loan solicitations. | [P002] | high |
| F011 | treatment | The final contract interest rate is revealed only after the borrower accepts the initial offer. | [P002], [P006] | high |
| F012 | treatment | A dynamic repayment incentive changes future loan pricing for borrowers who remain in good standing. | [P002], [P008] | high |
| F013 | information_structure | Borrowers do not know before application that the contract rate may differ from the offer rate. | [P006], [P009] | high |

## Outcomes And Measurement

| fact_id | outcome | measurement_method | evidence_id | confidence |
|---|---|---|---|---|
| F014 | borrowing/take-up | Whether a prospective borrower responds to or accepts the direct-mail offer. | [P006], [P009] | high |
| F015 | repayment/default | Repayment behavior after borrowing is used to study adverse selection and moral hazard. | [P001], [P004], [P007], [P008] | high |
| F016 | application blindness | The paper checks whether application decisions were blind to the later contract rate. | [P009] | high |

## Identification Logic

| fact_id | component | extracted fact | evidence_id | confidence |
|---|---|---|---|---|
| F017 | design_family | The source design is a staged or factorial randomized field experiment. | [P002], [P003] | high |
| F018 | adverse_selection_logic | Selection effects are identified by comparing repayment among borrowers who accepted different offer rates but ultimately received the same low contract rate. | [P007] | high |
| F019 | moral_hazard_logic | Moral hazard is identified using the dynamic repayment incentive because it affects future terms without changing the initial repayment burden. | [P008] | high |
| F020 | validity_check | The blind-application check supports the claim that applicants could not condition take-up on the later contract rate. | [P009] | high |

## Linchpin Details

| linchpin_id | detail | why_it_matters | what_fails_without_it | evidence_id | confidence |
|---|---|---|---|---|---|
| L001 | The design separates initial offer rate from later contract rate. | It creates variation in borrower selection independent of final repayment incentives. | A single randomized rate cannot distinguish high-risk borrowers selecting into loans from borrowers defaulting because of repayment burden. | [P004], [P006], [P007] | high |
| L002 | The dynamic repayment incentive affects future borrowing terms without changing the initial loan burden. | It isolates a choice/incentive channel after borrowing. | Moral hazard cannot be separated from adverse selection if all price variation also changes who borrows. | [P008] | high |
| L003 | Borrowers must be blind to the contract-rate randomization at application time. | The contract-rate surprise preserves the intended separation between take-up and repayment incentives. | If borrowers anticipate the contract rate, take-up could again be selected on final terms. | [P006], [P009] | high |

## Robustness / Placebo / Mechanism Checks

| fact_id | check_type | extracted fact | evidence_id | confidence |
|---|---|---|---|---|
| F021 | information_check | The paper checks that contract rate is uncorrelated with application decisions. | [P009] | high |
| F022 | mechanism_check | The design uses separate comparisons for adverse selection and moral hazard rather than one pooled repayment comparison. | [P007], [P008] | high |

## Naive Design Failure Modes

| failure_id | naive_design | why_it_fails | evidence_id | confidence |
|---|---|---|---|---|
| N001 | Randomize only the interest rate and compare default rates. | A default response to a randomized rate can reflect adverse selection or moral hazard. | [P004] | high |
| N002 | Compare high-rate borrowers with low-rate borrowers without equalizing final contract terms. | Repayment differences would mix who accepts the loan with incentives created by final loan terms. | [P006], [P007] | high |
| N003 | Use future repayment incentives without ensuring the initial debt burden is unchanged. | The design would no longer isolate pure moral hazard. | [P008] | high |

## Evaluator Inference

| inference_id | inference | basis_evidence_id | use_in_later_tasks |
|---|---|---|---|
| I001 | Agent-facing tasks should preserve the timing sequence: offer, acceptance/application, contract revelation, repayment/future incentive. | [P002], [P006], [P008] | task construction |
| I002 | Full-credit gold answers should require at least two randomized margins, and likely three, to separate selection and incentive channels. | [P002], [P004], [P007], [P008] | gold reference |

## Uncertainties

| uncertainty_id | uncertainty | evidence_id | consequence |
|---|---|---|---|
| U001 | Exact sample counts and wave-level versus individual-level randomization are not fully extracted in this source packet. | [P002] | Do not hard-code exact sample size or clustering in gold reference until verified. |
| U002 | Preferred regression specification and standard-error level are not extracted. | [P007], [P008] | Statistical model details should be verified before Task 07. |

## Facts Safe For Agent-Facing Packets

- A consumer-credit lender can randomize loan offer terms.
- Borrower take-up and repayment are both observed.
- A later contract term can be revealed only after application.
- Future borrowing incentives can be varied separately from current repayment burden.

## Facts Unsafe For Agent-Facing Packets

- Source-paper title, authors, venue, exact year.
- Exact country, lender identity, and source-specific direct-mail details if recognizable.
- The exact three-randomization framing if it gives away the original paper too directly.
- Statements that the original answer separates adverse selection and moral hazard through named offer/contract/dynamic-rate arms.
