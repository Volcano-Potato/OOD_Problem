<!-- visibility: evaluator-only -->
<!-- do_not_include_in_agent_context: true -->
<!-- case_id: C010 -->

# Source Facts: C010

## Scope

These facts are extracted only from `source_packet.md`. They are evaluator-only inputs for later `gold_reference.md` and anonymized task construction.

## Research Context

| fact_id | category | fact | evidence_id | confidence |
|---|---|---|---|---|
| F001 | research_context | The empirical setting is seasonal agricultural-input adoption among small producers facing a profitable but underused technology. | [P003], [P006] | high |
| F002 | research_question | The source asks why producers underinvest in a profitable input and whether small timing-based interventions can increase adoption more efficiently than large subsidies. | [P001], [P002], [P005] | high |
| F003 | benchmark_objective | The benchmark objective is to distinguish timing and acquisition-friction mechanisms from simple static price sensitivity, standard credit constraints, or reminder effects. | [P001], [P004], [P005], [P012] | high |
| F004 | central_threat | Low adoption can be misinterpreted if researchers do not separate procrastination or present-bias from alternative explanations such as large price effects or transaction costs. | [P004], [P005], [P012] | high |

## Data Structure

| fact_id | field | extracted fact | evidence_id | confidence |
|---|---|---|---|---|
| F005 | observation_unit | The relevant observation is a producer-season or household-season input-adoption outcome. | [P008], [P009], [P010] | medium |
| F006 | assignment_level | The intervention varies at the individual producer or household level through randomized offer arms. | [P008], [P009] | high |
| F007 | outcome_measurement_level | The main outcome is producer-level purchase or use of the input in the relevant season. | [P010], [P011] | high |
| F008 | clustering_or_inference_level | The design likely requires producer or local-cluster-level inference, but the exact standard-error choice is not fixed in the extracted packet. | [P008], [P009] | medium |
| F009 | time_span | The design spans the post-harvest decision moment, the later application period, and follow-up within one or more agricultural seasons. | [P001], [P005], [P008], [P010] | high |
| F010 | panel_or_repeated_observations | Repeated seasonal observations are available for at least some producers across multiple intervention rounds. | [P009], [P010] | medium |
| F011 | sample_construction | Producers are observed around the harvest period and then followed to determine whether they later purchase or use the input in the coming season. | [P007], [P008], [P010] | high |
| F012 | treatment_exposure_variable | The treatments vary the timing and form of a small acquisition-cost reduction, ordering convenience, or later subsidy/reminder offer. | [P001], [P005], [P008], [P009] | high |
| F013 | outcome_variable | The core outcome is actual input adoption or use rather than stated plans alone. | [P007], [P010], [P011] | high |
| F014 | covariates | Baseline producer characteristics, prior adoption history, timing within the season, and possibly liquidity-related conditions are relevant design variables. | [P006], [P007], [P009] | medium |
| F015 | missingness_or_noncompliance | Some producers offered a program do not purchase the input, and purchase through the program may not map perfectly into eventual use. | [P009], [P010] | medium |
| F016 | spillover_risk | Producers may learn from others or face local imitation, though the main extracted packet emphasizes own offer timing rather than network spillovers. | [P009], [P012] | low |

## Treatment / Variation / Exposure

| fact_id | category | fact | evidence_id | confidence |
|---|---|---|---|---|
| F017 | early_small_intervention | A key treatment offers a small, time-limited reduction in acquisition cost or hassle shortly after harvest. | [P001], [P005], [P008] | high |
| F018 | late_offer_comparison | Later offers of similar or even larger economic value have smaller effects than the early intervention. | [P001], [P005], [P010], [P011] | high |
| F019 | timing_choice_margin | Some variants allow producers to choose a future purchase or delivery schedule, creating evidence on demand for advance-purchase timing. | [P001], [P009] | medium |
| F020 | reminder_margin | Reminder-style interventions are included as a comparison and show much weaker effects. | [P009], [P012] | high |
| F021 | heavy_subsidy_margin | A larger price reduction later in the season is a benchmark comparison, not the core linchpin of the design. | [P002], [P009], [P011] | high |

## Outcomes And Measurement

| fact_id | outcome | measurement_method | evidence_id | confidence |
|---|---|---|---|---|
| F022 | adoption_or_use | The main measured outcome is whether the producer actually purchases or uses the input in the season. | [P007], [P010], [P011] | high |
| F023 | stated_intent | Stated plans to use the input are observed or discussed, but actual behavior differs from those plans. | [P007] | high |
| F024 | timing_behavior | Choice of early versus later purchase or delivery timing is informative about commitment demand. | [P001], [P009] | medium |

## Identification Logic

| fact_id | component | extracted fact | evidence_id | confidence |
|---|---|---|---|---|
| F025 | design_family | The source design is a randomized field experiment with multiple intervention arms focused on timing and acquisition frictions. | [P008], [P009] | high |
| F026 | source_of_variation | The identifying variation comes from random assignment to early small incentives, later offers, reminders, timing-choice options, and larger later discounts. | [P008], [P009], [P010], [P011] | high |
| F027 | comparison_group | The key comparison is between an early small intervention and later interventions or reminders, not simply between subsidized and unsubsidized producers. | [P001], [P005], [P010], [P012] | high |
| F028 | mechanism_test | If a small early intervention outperforms a later similar or larger offer, that pattern supports a procrastination or present-bias mechanism rather than a pure price-level story. | [P001], [P005], [P010], [P011] | high |
| F029 | why_reminder_is_not_enough | If reminders alone have little impact, pure forgetting or information salience is less convincing as the sole explanation. | [P009], [P012] | high |

## Linchpin Details

| linchpin_id | detail | why_it_matters | what_fails_without_it | evidence_id | confidence |
|---|---|---|---|---|---|
| L001 | The design must compare an early small acquisition-cost reduction offered just after income arrival with a later offer. | It isolates timing and procrastination from simple price-level effects. | A generic subsidy experiment cannot show whether timing rather than subsidy size drives adoption. | [P001], [P005], [P008], [P010] | high |
| L002 | The design must include an explicit later comparison arm of similar or greater value. | It shows that the early effect is not explained solely by economic magnitude. | Without a later comparison, any positive effect could be attributed to a generic discount or transaction-cost reduction. | [P001], [P009], [P011] | high |
| L003 | The design should compare actual adoption with stated intentions or reminder-only arms. | It helps separate procrastination from simple lack of awareness or lack of intent. | Without this, low adoption could be misread as simple information failure or low baseline demand. | [P007], [P009], [P012] | medium |

## Robustness / Placebo / Mechanism Checks

| fact_id | check_type | extracted fact | evidence_id | confidence |
|---|---|---|---|---|
| F030 | later_offer_comparison | Later small or even larger incentives produce weaker responses than the early offer. | [P001], [P010], [P011] | high |
| F031 | reminder_check | Reminder interventions have little effect relative to the timing-based offer. | [P012] | high |
| F032 | commitment_choice_check | Some producers choose schedules that induce advance purchase or earlier commitment. | [P001], [P009] | medium |

## Naive Design Failure Modes

| failure_id | naive_design | why_it_fails | evidence_id | confidence |
|---|---|---|---|---|
| N001 | Compare only a large later subsidy against no offer and conclude the mechanism is present-bias. | This does not isolate timing from price magnitude. | [P002], [P005], [P011] | high |
| N002 | Attribute low adoption entirely to credit constraints because producers say they lack money later. | The design is about timing and follow-through, not just static liquidity. | [P004], [P007], [P010] | high |
| N003 | Use stated intention to adopt as the main outcome. | The key behavioral gap is between stated plans and realized adoption. | [P007], [P010] | medium |
| N004 | Treat a reminder effect as equivalent to an early commitment-style intervention. | Reminder-only evidence is weaker and does not replicate the early-timing effect. | [P009], [P012] | high |

## Evaluator Inference

| inference_id | inference | basis_evidence_id | use_in_later_tasks |
|---|---|---|---|
| I001 | Agent-facing packets should preserve a seasonal production cycle with an early cash-on-hand moment and a later input-application moment, but should avoid exact country, crop, and program-name details. | [P001], [P008], [P012] | leakage control |
| I002 | Full-credit gold answers should require timing-based mechanism separation rather than generic subsidy effects. | [P001], [P005], [P010], [P011] | gold reference |
| I003 | Reminder-null logic is helpful for evaluator reasoning but may be partial-credit rather than absolute full-credit requirement. | [P012] | scoring design |

## Uncertainties

| uncertainty_id | uncertainty | evidence_id | consequence |
|---|---|---|---|
| U001 | The exact recommended clustering level and the exact panel structure across seasons are not fully pinned down in the source packet. | [P008], [P009] | Gold reference should avoid requiring a very specific inference formula. |
| U002 | It is not fully fixed whether full credit should require an explicit reminder-comparison discussion or whether this should count as stronger but not mandatory reasoning. | [P012] | Gold reference should distinguish full credit from strong bonus reasoning carefully. |
| U003 | The exact mix of purchase-through-program versus eventual use outcomes across arms is not fully extracted. | [P009], [P010] | Agent-facing tasks should describe actual adoption or use generically, without hard-coding source-specific measurement counts. |

## Facts Safe For Agent-Facing Packets

- The setting involves a profitable but underused seasonal input.
- Producers face an early post-income decision moment and a later input-use moment.
- Small timing-based reductions in acquisition cost or hassle can be experimentally varied.
- Actual adoption differs from stated intentions.
- Later offers, reminders, or larger price cuts can serve as comparison arms.

## Facts Unsafe For Agent-Facing Packets

- Source-paper title, authors, venue, exact year.
- Exact country, crop, and program acronym.
- Distinctive program labels and exact delivery wording.
- Exact subsidy sizes, precise adoption percentages, and source-specific welfare calibration language.
