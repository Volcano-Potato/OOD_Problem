<!-- visibility: evaluator-only -->
<!-- do_not_include_in_agent_context: true -->
<!-- case_id: C001 -->

# Source Facts: C001

## Scope

These facts are extracted only from `source_packet.md`. They are evaluator-only inputs for later `gold_reference.md` and anonymized task construction.

## Research Context

| fact_id | category | fact | evidence_id | confidence |
|---|---|---|---|---|
| F001 | research_context | The empirical setting is in-person door-to-door charitable fundraising. | [P004] | high |
| F002 | research_question | The source question is whether giving reflects altruism or warm glow versus social pressure from refusing an in-person request. | [P001], [P003] | high |
| F003 | benchmark_objective | The benchmark objective is to ask for a design that separates genuine giving motives from pressure-induced giving. | [P001], [P003], [P005] | high |
| F004 | mechanism | The relevant mechanisms have different welfare interpretations: supply-driven giving can be utility-enhancing, while demand-driven pressure can be utility-reducing. | [P003] | high |

## Data Structure

| fact_id | field | extracted fact | evidence_id | confidence |
|---|---|---|---|---|
| F005 | observation_unit | The relevant observed unit is a household solicitation/contact opportunity. | [P004], [P005] | medium |
| F006 | assignment_level | Treatment varies at the household solicitation level through whether the household receives no flyer, an advance flyer, or a flyer with opt-out. | [P005], [P006] | high |
| F007 | outcome_measurement_level | Outcomes are measured at the household interaction level: whether the household opens the door and whether/how much it gives. | [P002], [P007] | high |
| F008 | time_structure | The flyer announces a one-hour visit window one day in advance. | [P005] | high |
| F009 | sample_or_setting | The field experiment approaches households in towns around a large US city during 2008. | [P004] | high |

## Treatment / Exposure / Variation

| fact_id | category | fact | evidence_id | confidence |
|---|---|---|---|---|
| F010 | treatment | The baseline condition is ordinary door-to-door solicitation without advance flyer. | [P006] | high |
| F011 | treatment | One treatment gives advance notice of the visit window through a flyer. | [P005] | high |
| F012 | treatment | A second treatment adds an opt-out box to the flyer so households can indicate they do not want to be disturbed. | [P005] | high |
| F013 | variation_source | The design compares the baseline, flyer, and flyer-with-opt-out conditions. | [P006] | high |

## Outcomes And Measurement

| fact_id | outcome | measurement_method | evidence_id | confidence |
|---|---|---|---|---|
| F014 | door opening/contact | Whether households open the door after advance notice or no advance notice. | [P002], [P007] | high |
| F015 | donation/giving | Whether and how much households donate under the solicitation conditions. | [P002] | high |
| F016 | small donations | The reduction in giving under opt-out is concentrated among smaller donations. | [P002] | high |

## Identification Logic

| fact_id | component | extracted fact | evidence_id | confidence |
|---|---|---|---|---|
| F017 | design_family | The source design is a mechanism experiment embedded in a field experiment. | [P001], [P005], [P006] | high |
| F018 | comparison_group | The key comparisons are no-flyer baseline versus advance flyer and advance flyer versus advance flyer with opt-out. | [P005], [P006] | high |
| F019 | identifying_logic | Advance notice lets households seek or avoid contact, while opt-out lowers the cost of avoiding the solicitor. | [P001], [P005], [P007] | high |
| F020 | mechanism_logic | Door-opening and giving responses to avoidance options help separate altruistic demand from pressure-induced giving. | [P001], [P002], [P007] | high |

## Linchpin Details

| linchpin_id | detail | why_it_matters | what_fails_without_it | evidence_id | confidence |
|---|---|---|---|---|---|
| L001 | The design includes a low-cost avoidance or opt-out channel before the solicitation interaction. | It creates behavioral evidence on whether households want to avoid the solicitor. | A generic randomized solicitation can estimate whether solicitation changes donations, but cannot distinguish altruism/warm glow from social pressure. | [P001], [P005], [P007] | high |
| L002 | The design compares advance notice alone with advance notice plus opt-out. | It helps distinguish simple scheduling/awareness from lower-cost refusal or avoidance. | A flyer-only design could mix people seeking the fundraiser with people avoiding the fundraiser. | [P005], [P007] | high |

## Robustness / Placebo / Mechanism Checks

| fact_id | check_type | extracted fact | evidence_id | confidence |
|---|---|---|---|---|
| F021 | mechanism_support | A complementary survey experiment varies payment, duration, and announcement status to support interpretation of avoidance behavior. | [P008] | medium |
| F022 | outcome_pattern | The opt-out effect is concentrated among smaller donations, which supports a social-pressure interpretation. | [P002] | high |

## Naive Design Failure Modes

| failure_id | naive_design | why_it_fails | evidence_id | confidence |
|---|---|---|---|---|
| N001 | Randomize only whether a solicitor visits. | It can estimate solicitation effects but does not reveal whether giving is voluntary altruism or costly pressure. | [P001], [P003], [P005] | high |
| N002 | Measure only total donations after a flyer. | Flyer effects can combine avoidance by pressure-averse households and seeking by altruistic households. | [P007] | high |
| N003 | Treat lower giving under opt-out as lower altruism. | The opt-out option is specifically designed to reduce unwanted interaction, so lower giving may reveal avoidance of pressure. | [P002], [P005] | high |

## Evaluator Inference

| inference_id | inference | basis_evidence_id | use_in_later_tasks |
|---|---|---|---|
| I001 | Agent-facing tasks should describe an anonymized in-person request setting rather than the exact charity, city, or "Do Not Disturb" phrase. | [P004], [P005] | leakage control |
| I002 | Full-credit gold answers should require some avoidance, opt-out, or sorting channel for mechanism identification. | [P001], [P003], [P005] | gold reference |

## Uncertainties

| uncertainty_id | uncertainty | evidence_id | consequence |
|---|---|---|---|
| U001 | Exact randomization unit, treatment counts, and inference details are not yet extracted in this source packet. | [P004], [P005] | Task 07 should not make hard claims about standard errors or exact sample sizes until verified. |
| U002 | The complementary survey experiment is noted but not fully extracted. | [P008] | It can support mechanism discussion but should not be central to the anonymized task unless later extracted. |

## Facts Safe For Agent-Facing Packets

- An in-person solicitation setting where potential donors can be contacted.
- A research objective about separating genuine willingness to give from pressure-induced giving.
- Generic treatments involving advance notice and a low-cost way to avoid interaction.
- Outcomes such as contact/opening and donation behavior.

## Facts Unsafe For Agent-Facing Packets

- Source-paper title, authors, venue, exact year.
- Exact charity identities, exact city/suburb details, and exact sample size.
- The phrase "Do Not Disturb" if it makes the source too recognizable.
- Any statement that the original paper's answer is an opt-out flyer design.
