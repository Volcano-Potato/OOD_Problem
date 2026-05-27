<!-- visibility: evaluator-only -->
<!-- do_not_include_in_agent_context: true -->
<!-- case_id: C004 -->

# Source Facts: C004

## Scope

These facts are extracted only from `source_packet.md`. They are evaluator-only inputs for later `gold_reference.md` and anonymized task construction.

## Research Context

| fact_id | category | fact | evidence_id | confidence |
|---|---|---|---|---|
| F001 | research_context | The empirical setting is paid search advertising effectiveness measurement for a well-known online marketplace or platform advertiser. | [P001], [P006], [P007] | high |
| F002 | research_question | The source question is the causal effect of paid search on downstream sales and how that effect varies by prior user familiarity or activity. | [P001], [P009], [P010] | high |
| F003 | benchmark_objective | The benchmark objective is to ask for a design that handles search-intent endogeneity and consumer heterogeneity rather than treating clicks or attributed sales as causal ROI. | [P001], [P002], [P003], [P008] | high |
| F004 | central_threat | Paid search clicks and spending are endogenous because they depend on user behavior and purchase intent. | [P002], [P003], [P006] | high |

## Data Structure

| fact_id | field | extracted fact | evidence_id | confidence |
|---|---|---|---|---|
| F005 | observation_unit | The observed outcomes are user-level or market-by-time sales outcomes linked to advertising exposure conditions. | [P007], [P008] | medium |
| F006 | assignment_level | The experiment varies advertising exposure across geographic markets using platform-level controls. | [P007], [P008] | high |
| F007 | outcome_measurement_level | The primary outcome is downstream sales, with additional attention to user acquisition or purchases by different user segments. | [P001], [P009], [P010] | high |
| F008 | clustering_or_inference_level | The design is analyzed at the geographic-market by time level, using matched test and control regions. | [P008] | medium |
| F009 | time_span | The experimental variation runs over a finite campaign period and is compared across pre and post windows. | [P008] | medium |
| F010 | panel_or_repeated_observations | The design relies on repeated sales observations over time across test and control markets. | [P008] | medium |
| F011 | sample_construction | A subset of geographic markets is assigned to ad suspension while other matched markets remain on, creating test and control regions. | [P007], [P008] | high |
| F012 | treatment_exposure_variable | The key treatment is whether paid search advertising is on or suspended for a set of non-brand queries. | [P006], [P007], [P008] | high |
| F013 | outcome_variable | The core outcome is incremental sales rather than clicks or attributed conversions alone. | [P001], [P004], [P008] | high |
| F014 | covariates | User recency and frequency of prior purchases are important heterogeneity dimensions. | [P009], [P010] | high |
| F015 | spillover_risk | Users may substitute across channels or routes to reach the platform, so observed paid-click traffic is not itself the causal target. | [P003], [P005], [P011] | medium |

## Treatment / Variation / Exposure

| fact_id | category | fact | evidence_id | confidence |
|---|---|---|---|---|
| F016 | treatment_condition | In treated markets, paid search ads remain active for the focal non-brand keyword set. | [P007], [P008] | medium |
| F017 | control_condition | In test markets, the platform suspends those paid search ads, creating exogenous exposure reduction. | [P007], [P008] | high |
| F018 | placebo_logic | Brand-keyword search behaves like a navigational placebo because natural search is a near-perfect substitute. | [P005] | high |
| F019 | heterogeneity_margin | Less active, infrequent, or long-absent users are the group most likely to respond positively to ads. | [P001], [P009], [P010] | high |

## Outcomes And Measurement

| fact_id | outcome | measurement_method | evidence_id | confidence |
|---|---|---|---|---|
| F020 | sales | Sales are measured downstream from the advertising intervention rather than inferred from clicks alone. | [P001], [P004], [P008] | high |
| F021 | attributed_click_outcomes | Clicks and attributed conversions are observed but are not valid causal outcomes by themselves. | [P002], [P003], [P004] | high |
| F022 | heterogeneous_response | The treatment effect is positive for new or infrequent users and near zero for frequent or active users. | [P001], [P009], [P010] | high |

## Identification Logic

| fact_id | component | extracted fact | evidence_id | confidence |
|---|---|---|---|---|
| F023 | design_family | The source design is a large-scale field experiment using exogenous geographic variation in paid search exposure. | [P007], [P008] | high |
| F024 | source_of_variation | The identifying variation comes from suspending or continuing ads across matched geographic markets. | [P007], [P008] | high |
| F025 | comparison_group | The relevant comparison is between treated and matched control markets over time, not clicked versus unclicked users. | [P003], [P008] | high |
| F026 | why_click_based_comparison_fails | Clicking is itself selected on search intent and existing familiarity, so clicked users are not a valid control contrast. | [P002], [P003], [P006] | high |
| F027 | why_observational_roi_fails | Observational ROI based on attributed sales can be orders of magnitude larger than the experimental estimate because intent and clicks are endogenous. | [P004] | high |
| F028 | heterogeneity_identification | Segmenting users by prior frequency or recency reveals that average near-zero effects can mask meaningful subgroup effects. | [P009], [P010] | high |

## Linchpin Details

| linchpin_id | detail | why_it_matters | what_fails_without_it | evidence_id | confidence |
|---|---|---|---|---|---|
| L001 | The design must use exogenous variation in ad availability rather than observed clicks or ad-attributed purchases. | It breaks the link between user intent and ad exposure. | Click-based ROI or exposed-versus-unexposed comparisons confound selection with treatment effects. | [P002], [P003], [P007], [P008] | high |
| L002 | Test and control regions must be matched on pre-period sales dynamics or otherwise controlled over time. | Search advertising effects are small relative to background seasonality and trend variation. | A simple before-after comparison can mistake time variation for treatment effects. | [P008] | high |
| L003 | The design should preserve heterogeneity by prior user familiarity or activity. | Average treatment effects can be near zero even when marginal effects are positive for less-informed users. | A pooled design can miss the main substantive lesson and falsely conclude that ads are uniformly ineffective. | [P001], [P009], [P010] | high |

## Robustness / Placebo / Mechanism Checks

| fact_id | check_type | extracted fact | evidence_id | confidence |
|---|---|---|---|---|
| F029 | placebo_check | Brand-keyword advertising provides a benchmark case where natural search is a near-perfect substitute and incremental ad effect is near zero. | [P005] | high |
| F030 | heterogeneity_check | The source checks treatment effects by prior purchase frequency and recency. | [P009], [P010] | high |
| F031 | trend_control | The source uses matched control regions and difference-in-differences logic to account for seasonality and pre-existing trend structure. | [P008] | high |

## Naive Design Failure Modes

| failure_id | naive_design | why_it_fails | evidence_id | confidence |
|---|---|---|---|---|
| N001 | Compare users who clicked on paid search ads with users who did not click. | Clicking is endogenous to intent and prior familiarity, so the groups differ even without treatment. | [P002], [P003] | high |
| N002 | Use attributed conversions or attributed sales as causal ROI. | Attribution overstates causal effects because many users would have reached the platform through other channels anyway. | [P003], [P004], [P011] | high |
| N003 | Use a simple before-after comparison in treated markets. | Background seasonality and market-level variation can be mistaken for ad effects. | [P008] | high |
| N004 | Report only an average treatment effect with no user segmentation. | The main effect can look near zero even when less-informed users respond strongly. | [P001], [P009], [P010] | high |

## Evaluator Inference

| inference_id | inference | basis_evidence_id | use_in_later_tasks |
|---|---|---|---|
| I001 | Agent-facing packets should preserve search-intent endogeneity but avoid source-identifying references to the exact marketplace, search platform, and keyword labels. | [P005], [P006], [P007] | leakage control |
| I002 | Full-credit gold answers should require exogenous ad-availability variation plus explicit recognition of user heterogeneity. | [P007], [P008], [P009], [P010] | gold reference |
| I003 | Brand-search placebo logic is useful for evaluator reasoning but may be too source-specific for lower-level packets. | [P005] | level design |

## Uncertainties

| uncertainty_id | uncertainty | evidence_id | consequence |
|---|---|---|---|
| U001 | The exact operational details of keyword selection, region assignment, and duration are not fully extracted into the source packet. | [P007], [P008] | Do not hard-code exact counts or campaign duration before Task 07 verification. |
| U002 | It is not yet fixed how much partial credit to give designs that identify only average treatment effects without the heterogeneity component. | [P001], [P009], [P010] | Gold reference should state whether heterogeneity is required for full credit or only for stronger credit. |
| U003 | It remains open whether brand-search placebo logic should appear as a direct hint in Level 3 or stay evaluator-only. | [P005] | Decide during task-packet design to avoid unnecessary leakage. |

## Facts Safe For Agent-Facing Packets

- The platform can vary paid search exposure exogenously across geographic markets or comparable groups.
- Observed clicks and attributed conversions are not sufficient for causal ROI because user intent is endogenous.
- Outcomes should focus on downstream sales or purchases rather than clicks alone.
- User recency and frequency of prior activity are relevant heterogeneity dimensions.

## Facts Unsafe For Agent-Facing Packets

- Source-paper title, authors, venue, exact year.
- Named firm, named search platform, and exact keyword labels.
- Exact “brand keyword” versus “non-brand keyword” wording if it makes the source too identifiable.
- The exact experimental share of markets or exact ROI magnitudes from the source.
