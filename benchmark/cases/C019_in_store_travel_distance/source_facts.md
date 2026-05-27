<!-- visibility: evaluator-only -->
<!-- do_not_include_in_agent_context: true -->
<!-- case_id: C019 -->

# Source Facts: C019

## Scope

These facts are extracted only from `source_packet.md`. They are evaluator-only inputs for later `gold_reference.md` and anonymized task construction.

## Research Context

| fact_id | category | fact | evidence_id | confidence |
|---|---|---|---|---|
| F001 | research_context | The empirical setting is brick-and-mortar retail navigation, where managers want to know whether sending shoppers through more of the store increases unplanned spending. | [P001], [P003], [P011] | high |
| F002 | research_question | The source asks for the causal effect of in-store travel distance on unplanned spending and for implications for path-inducing promotions. | [P001], [P002], [P012] | high |
| F003 | benchmark_objective | The benchmark objective is to force the agent to handle endogenous path choice rather than treat observed route length as exogenous. | [P004], [P005], [P006] | high |
| F004 | central_threat | Shopper path length is confounded by omitted in-store stimuli, simultaneity, and measurement error. | [P004] | high |

## Data Structure

| fact_id | field | extracted fact | evidence_id | confidence |
|---|---|---|---|---|
| F005 | observation_unit | The observational study centers on an individual shopping trip. | [P007], [P008] | high |
| F006 | assignment_level | In the observational design, path length is not assigned; it emerges at the shopper-trip level. In the validating experiment, promotion assignment is randomized at the shopper-trip level. | [P005], [P012] | high |
| F007 | outcome_measurement_level | The main outcome is trip-level unplanned spending measured from receipts and planned-basket information. | [P007], [P008] | high |
| F008 | clustering_or_inference_level | The natural inference level is the shopper-trip level; there is no higher-level randomized cluster in the main observational analysis. | [P007], [P009] | medium |
| F009 | time_span | The core design covers a single shopping trip, with pre-trip, in-trip, and post-checkout measurement. | [P005], [P007] | high |
| F010 | panel_or_repeated_observations | The core study is largely cross-sectional at the trip level rather than a long panel. | [P007], [P009] | medium |
| F011 | sample_construction | Shoppers are intercepted at store entry, report planned purchases, are tracked during the trip, and then have purchases observed at checkout. | [P007] | high |
| F012 | treatment_exposure_variable | The key endogenous exposure is actual in-store travel distance. A secondary intervention variable is whether a targeted promotion induces a farther or nearer deviation from the planned route. | [P001], [P011], [P012] | high |
| F013 | outcome_variable | The core outcome is the dollar amount of unplanned spending, with robustness checks on the number of unplanned categories. | [P007], [P009], [P010] | high |
| F014 | covariates | Planned basket composition, mental budget or budget slack, impulsivity, demographics, and store familiarity are relevant controls. | [P007], [P008], [P010] | high |
| F015 | missingness_or_noncompliance | Some shoppers may not redeem targeted promotions, and path measures can contain noise. | [P004], [P012] | medium |
| F016 | spillover_risk | Spillover across shoppers is not the main concern; the key issue is within-trip endogeneity of exposure. | [P004], [P012] | medium |

## Treatment / Variation / Exposure

| fact_id | category | fact | evidence_id | confidence |
|---|---|---|---|---|
| F017 | endogenous_exposure | Actual path length is partly chosen by the shopper and affected by in-store events, so it is not directly exogenous. | [P004], [P005] | high |
| F018 | reference_path_variation | A pre-trip reference path can be constructed from store layout and the shopper's planned basket. | [P005], [P006] | high |
| F019 | promotion_variation | A targeted promotion can be assigned to an unplanned category nearer to or farther from the shopper's planned route to induce additional travel. | [P011], [P012] | high |

## Outcomes And Measurement

| fact_id | outcome | measurement_method | evidence_id | confidence |
|---|---|---|---|---|
| F020 | unplanned_spending | Unplanned spending is measured by comparing planned purchases declared at entry with actual purchases at checkout. | [P007] | high |
| F021 | path_length | Path length is measured during the trip using detailed location tracking, but still contains measurement noise. | [P004], [P007] | high |
| F022 | unplanned_item_count | Number of unplanned categories is a robustness outcome. | [P010] | medium |

## Identification Logic

| fact_id | component | extracted fact | evidence_id | confidence |
|---|---|---|---|---|
| F023 | design_family | The source design is an IV-style observational study, complemented by a randomized field experiment that shifts travel distance. | [P002], [P005], [P012] | high |
| F024 | source_of_variation | The key identifying variation in the observational design comes from reference-path length, which is determined before the trip begins. | [P005], [P006] | high |
| F025 | comparison_group | The observational comparison is effectively across shoppers with different pre-trip reference paths after controlling for planned-basket and budget conditions; the experimental comparison is far-path coupon versus near-path coupon. | [P006], [P008], [P012] | high |
| F026 | why_naive_ols_fails | Regressing unplanned spending on observed path length alone confounds route choice, in-store stimuli, and reversed causality. | [P004], [P009] | high |
| F027 | shopping_time_is_not_enough | Shopping time is a weaker proxy than path length for exposure to in-store product stimuli. | [P010] | medium |
| F028 | applied_marketing_claim | If longer path length truly causes more unplanned spending, then targeted path-inducing promotions can be effective. | [P011], [P012] | high |

## Linchpin Details

| linchpin_id | detail | why_it_matters | what_fails_without_it | evidence_id | confidence |
|---|---|---|---|---|---|
| L001 | The design must not treat observed path length as exogenous. | Path length is itself chosen and shaped during the trip. | A simple regression of spending on observed distance mistakes endogenous wandering for causal exposure. | [P004], [P005], [P009] | high |
| L002 | The observational design needs a pre-trip reference path or another path-inducing source of variation determined before spending occurs. | This is what breaks simultaneity and reversed-causality concerns. | Without pre-trip variation, the agent cannot separate travel-induced spending from purchase-induced travel. | [P005], [P006] | high |
| L003 | Planned-basket and budget-slack controls are part of identification, not cosmetic extras. | Reference-path length depends on planned purchases, which also affect slack available for unplanned spending. | Without these controls, the instrument or comparison can directly proxy for shopping mission and spending capacity. | [P007], [P008] | high |

## Robustness / Placebo / Mechanism Checks

| fact_id | check_type | extracted fact | evidence_id | confidence |
|---|---|---|---|---|
| F029 | iv_vs_ols_check | IV estimates are materially larger than naive OLS estimates, consistent with endogeneity in observed path length. | [P002], [P009] | high |
| F030 | shopping_time_check | Path length performs better than shopping time in explaining unplanned spending. | [P010] | medium |
| F031 | basket_size_check | The results are checked against alternative controls for planned basket size and number of planned categories. | [P008], [P010] | medium |
| F032 | experimental_validation | A randomized far-versus-near promotion experiment provides direct evidence that induced travel distance can increase unplanned spending. | [P012] | high |

## Naive Design Failure Modes

| failure_id | naive_design | why_it_fails | evidence_id | confidence |
|---|---|---|---|---|
| N001 | Regress unplanned spending on observed path length and call the slope causal. | Observed path length is endogenous to omitted stimuli, simultaneity, and measurement error. | [P004], [P009] | high |
| N002 | Use shopping time as the main causal exposure without arguing why it maps to product exposure. | Shopping time is a weaker proxy than path length for product exposure. | [P010] | medium |
| N003 | Ignore planned basket structure and budget slack. | Shopping mission affects both route construction and remaining capacity for unplanned purchases. | [P007], [P008] | high |
| N004 | Treat the mobile-promotion result as proving all path-inducing interventions raise net store revenue without caveats. | Additional unplanned spending may borrow from planned or future purchases and may reduce shopping convenience. | [P013] | medium |

## Evaluator Inference

| inference_id | inference | basis_evidence_id | use_in_later_tasks |
|---|---|---|---|
| I001 | Agent-facing packets should preserve a pre-trip basket, route-tracking data, and route-induced exposure logic but should avoid explicit TSP, 1SLA, and RFID labels. | [P005]-[P007] | leakage control |
| I002 | Full-credit answers should require either a valid pre-trip route-based IV or a clearly randomized path-inducing intervention. | [P005], [P006], [P012] | gold reference |
| I003 | Shopping-time versus path-length comparison is useful as a threat or robustness discussion, not as the hidden answer itself. | [P010] | level design |

## Uncertainties

| uncertainty_id | uncertainty | evidence_id | consequence |
|---|---|---|---|
| U001 | It is not fully fixed whether full credit should require the observational IV logic specifically, or whether a strong randomized promotion design is equally sufficient. | [P005], [P012] | Gold reference should allow both if they truly create exogenous path variation. |
| U002 | The exact strength of the route-tracking measurement issue relative to other endogeneity channels is not fully quantified in the source packet. | [P004], [P007] | Level 3 should mention measurement noise as a threat without overweighting it. |
| U003 | The store-layout and category details are highly source-specific and should not enter agent-facing tasks. | [P005], [P007], [P011] | Keep operational geometry generic in all agent-facing files. |

## Facts Safe For Agent-Facing Packets

- Shoppers enter with a planned basket or shopping mission.
- Researchers can observe pre-trip plans, in-trip route measures, and checkout spending.
- Unplanned spending is linked to route exposure.
- Actual route length is endogenous.
- A pre-trip route benchmark or randomized path-inducing intervention can help identify causal effects.

## Facts Unsafe For Agent-Facing Packets

- Source-paper title, authors, venue, exact year.
- Exact RFID label and exact route-construction algorithm names.
- Exact store map, zone counts, and category names.
- Exact elasticity magnitudes and exact coupon outcomes.
