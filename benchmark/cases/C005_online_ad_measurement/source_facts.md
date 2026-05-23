<!-- visibility: evaluator-only -->
<!-- do_not_include_in_agent_context: true -->
<!-- case_id: C005 -->

# Source Facts: C005

## Scope

These facts are extracted only from `source_packet.md`. They are evaluator-only inputs for later `gold_reference.md` and anonymized task construction.

## Research Context

| fact_id | category | fact | evidence_id | confidence |
|---|---|---|---|---|
| F001 | research_context | The empirical setting is online advertising effectiveness measurement. | [P001], [P003], [P009] | high |
| F002 | research_question | The source question is how to estimate causal ad lift when actual ad exposure is selected by platform auctions and optimization. | [P001], [P003], [P004], [P006] | high |
| F003 | benchmark_objective | The benchmark objective is to ask for a design comparing treated exposed users with control users who had comparable exposure opportunity. | [P001], [P005] | high |
| F004 | central_threat | Observed ad exposure is endogenous because exposed users can have higher baseline purchase intent. | [P003], [P006] | high |

## Data Structure

| fact_id | field | extracted fact | evidence_id | confidence |
|---|---|---|---|---|
| F005 | observation_unit | The relevant observation can be an ad opportunity or impression linked to downstream user outcomes. | [P005], [P007], [P009] | medium |
| F006 | assignment_level | The empirical application has randomized treatment assignment in an online ad campaign. | [P009] | medium |
| F007 | outcome_measurement_level | Outcomes are downstream user conversions such as website visits, sign-ups, or purchases. | [P007] | high |
| F008 | time_structure | The application studies ad impressions during a short campaign window. | [P009] | medium |
| F009 | platform_structure | The platform uses auctions and performance optimization to determine which users see ads. | [P004], [P005] | high |

## Treatment / Exposure / Variation

| fact_id | category | fact | evidence_id | confidence |
|---|---|---|---|---|
| F010 | treatment | Treatment users can be shown the focal advertiser's ad. | [P001], [P005] | high |
| F011 | control_condition | Control users do not see the focal ad, but the platform can identify when they would have had the focal ad opportunity. | [P005] | high |
| F012 | exposure_measure | Simulated or logged ghost impressions identify would-be focal ad impressions in the control group. | [P005] | high |
| F013 | alternative_design | Public-service-announcement and intent-to-treat tests are comparison approaches discussed by the source. | [P002], [P004] | high |

## Outcomes And Measurement

| fact_id | outcome | measurement_method | evidence_id | confidence |
|---|---|---|---|---|
| F014 | conversions | Conversions include downstream interactions such as website visits, sign-ups, or purchases. | [P007] | high |
| F015 | ad lift | Incremental ad effect is measured by comparing exposed treatment users with comparable control users identified through exposure opportunity. | [P001], [P005] | high |
| F016 | prediction_validity | If predicted exposure is imperfect, the control comparison can become selected and invalid. | [P008] | high |

## Identification Logic

| fact_id | component | extracted fact | evidence_id | confidence |
|---|---|---|---|---|
| F017 | design_family | The source design is an online advertising field experiment using randomized assignment and platform-level exposure-opportunity logging. | [P001], [P005], [P009] | high |
| F018 | comparison_group | The key comparison is between treatment users who see the focal ad and control users who would have seen the focal ad under treatment assignment. | [P001], [P005] | high |
| F019 | why_naive_exposure_fails | Users who see retargeted ads may have high sales even without ads because they are selected on purchase intent. | [P006] | high |
| F020 | why_psa_can_fail | Performance optimization can expose different user types to treatment ads and PSA ads, breaking holdout symmetry. | [P004] | high |

## Linchpin Details

| linchpin_id | detail | why_it_matters | what_fails_without_it | evidence_id | confidence |
|---|---|---|---|---|---|
| L001 | Identify control users with the same focal-ad exposure opportunity as treated exposed users. | It constructs the relevant counterfactual for the users who actually saw the ad. | Comparing exposed users to all unexposed users confounds ad effects with baseline purchase intent. | [P001], [P005], [P006] | high |
| L002 | Account for platform optimization when defining controls. | Optimized delivery can make PSA-exposed controls systematically different from treatment-ad-exposed users. | PSA tests can be biased if ad platforms choose different user types for different ads. | [P004] | high |
| L003 | Validate predicted exposure-opportunity assignment. | Prediction mistakes can create selected control groups. | A predicted-exposure design can introduce selection bias if the control set is mismatched. | [P008] | high |

## Robustness / Placebo / Mechanism Checks

| fact_id | check_type | extracted fact | evidence_id | confidence |
|---|---|---|---|---|
| F021 | comparison_design_check | The source compares ghost-ad logic against PSA and ITT approaches. | [P002] | high |
| F022 | implementation_check | The source flags prediction quality as a threat to valid predicted ghost-ad comparisons. | [P008] | high |

## Naive Design Failure Modes

| failure_id | naive_design | why_it_fails | evidence_id | confidence |
|---|---|---|---|---|
| N001 | Compare users who saw ads with users who did not see ads. | Exposed users may be selected on high purchase intent. | [P003], [P006] | high |
| N002 | Use a PSA control without accounting for platform optimization. | Optimizing algorithms can expose different user types to PSA and treatment ads. | [P004] | high |
| N003 | Use only ITT over all randomized users. | ITT can include many unexposed users and be noisy relative to the exposed-user counterfactual. | [P002] | medium |

## Evaluator Inference

| inference_id | inference | basis_evidence_id | use_in_later_tasks |
|---|---|---|---|
| I001 | Agent-facing tasks should avoid the source-identifying phrase "ghost ads" but preserve exposure-opportunity logging. | [P005] | leakage control |
| I002 | Full-credit gold answers should require a counterfactual exposure-opportunity group, not just random assignment. | [P001], [P005], [P006] | gold reference |

## Uncertainties

| uncertainty_id | uncertainty | evidence_id | consequence |
|---|---|---|---|
| U001 | Exact assignment share, outcome window, and campaign implementation details are not fully extracted. | [P009] | Do not hard-code exact campaign parameters before Task 07 verification. |
| U002 | It is not yet settled whether ITT should receive partial credit or be treated as insufficient for the main estimand. | [P002] | Gold reference should explicitly define partial-credit policy. |

## Facts Safe For Agent-Facing Packets

- An online ad platform randomly assigns users or opportunities to treatment/control.
- Actual ad exposure is not equivalent to random assignment because platform delivery is optimized.
- Control users can be identified by whether they would have had the same ad opportunity.
- Outcomes can include visits, sign-ups, or purchases.

## Facts Unsafe For Agent-Facing Packets

- Source-paper title, authors, venue, exact year.
- The phrase "ghost ads" or "Predicted Ghost Ads".
- Named retailer, exact campaign date, exact impression counts.
- Any statement that the original solution is the ghost-ad method.
