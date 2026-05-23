<!-- visibility: evaluator-only -->
<!-- do_not_include_in_agent_context: true -->
<!-- case_id: C014 -->

# Source Facts: C014

## Scope

These facts are extracted only from `source_packet.md`. They are evaluator-only inputs for later `gold_reference.md` and anonymized task construction.

## Research Context

| fact_id | category | fact | evidence_id | confidence |
|---|---|---|---|---|
| F001 | research_context | The empirical setting is anti-corruption monitoring in local public infrastructure projects. | [P001], [P010] | high |
| F002 | research_question | The source question is whether top-down audits or grassroots monitoring reduce corruption in local public projects. | [P001], [P003], [P006] | high |
| F003 | benchmark_objective | The benchmark objective is to ask for an evaluation design that estimates monitoring effects while using an outcome not controlled by potentially corrupt actors. | [P002], [P004], [P007], [P008] | high |
| F004 | measurement_problem | Corruption is hard to measure directly, so outcome construction is part of the research design. | [P004] | high |

## Data Structure

| fact_id | field | extracted fact | evidence_id | confidence |
|---|---|---|---|---|
| F005 | observation_unit | The relevant unit is a local public project or village project. | [P001], [P010] | high |
| F006 | assignment_level | Villages/projects are assigned to audit or participation interventions. | [P001], [P005], [P006] | high |
| F007 | outcome_measurement_level | Missing expenditures are measured at the project/village level by comparing reported spending with independent cost estimates. | [P002], [P007], [P008] | high |
| F008 | time_structure | Audit notification occurs after funds are awarded but before construction begins; independent measurement occurs after construction. | [P005], [P007] | high |
| F009 | institutional_setting | Projects are funded through a national village-level infrastructure program with local expenditure reporting. | [P010] | high |

## Treatment / Exposure / Variation

| fact_id | category | fact | evidence_id | confidence |
|---|---|---|---|---|
| F010 | treatment | The top-down monitoring treatment increases the probability of external government audit from a low baseline to certainty. | [P001], [P005] | high |
| F011 | timing | Treated villages are told about the audit after funding but before construction. | [P005] | high |
| F012 | treatment | Grassroots monitoring interventions include meeting invitations and anonymous comment forms. | [P006] | high |
| F013 | variation_source | The source describes randomized anti-corruption interventions. | [P001], [P005], [P006] | high |

## Outcomes And Measurement

| fact_id | outcome | measurement_method | evidence_id | confidence |
|---|---|---|---|---|
| F014 | missing_expenditures | Missing expenditures are the difference between reported project spending and independently estimated actual costs. | [P002], [P008] | high |
| F015 | independent_cost_estimate | Engineers and surveyors estimate costs using road core samples, supplier price surveys, and wage interviews. | [P007] | high |
| F016 | official_reports | Official or village spending reports are compared with independent cost estimates. | [P007], [P008] | high |
| F017 | alternative_outcome_risk | Even with audit, some expenditures remain unaccounted for and corruption may substitute across forms. | [P009] | medium |

## Identification Logic

| fact_id | component | extracted fact | evidence_id | confidence |
|---|---|---|---|---|
| F018 | design_family | The source uses a randomized field experiment. | [P001], [P005], [P006] | high |
| F019 | comparison_group | The audit effect is identified by comparing villages/projects assigned to higher audit probability with those not assigned to that condition. | [P001], [P005] | high |
| F020 | measurement_logic | Causal inference requires an independently measured outcome because official reports may not reveal actual corruption. | [P002], [P004], [P007], [P008] | high |
| F021 | mechanism_contrast | The design compares top-down auditing with grassroots monitoring interventions. | [P003], [P006] | high |

## Linchpin Details

| linchpin_id | detail | why_it_matters | what_fails_without_it | evidence_id | confidence |
|---|---|---|---|---|---|
| L001 | Construct an independent estimate of actual project costs. | It prevents the outcome from being controlled solely by actors who may manipulate official spending records. | A design using only official reports could miss or understate corruption. | [P002], [P004], [P007], [P008] | high |
| L002 | Audit treatment is announced after funds are awarded but before construction. | It targets behavior during implementation while reducing selection into funding. | If audit assignment occurred before project selection or after completion, interpretation would change. | [P005] | medium |
| L003 | Compare top-down and grassroots monitoring approaches. | It distinguishes different anti-corruption mechanisms and implementation constraints. | A single monitoring treatment would not test whether community participation works differently from audits. | [P003], [P006] | medium |

## Robustness / Placebo / Mechanism Checks

| fact_id | check_type | extracted fact | evidence_id | confidence |
|---|---|---|---|---|
| F022 | measurement_check | Independent engineering estimates are compared with official reported costs to construct the corruption outcome. | [P007], [P008] | high |
| F023 | mechanism_heterogeneity | Grassroots monitoring has limited average effects but may work where free-riding or elite capture is limited. | [P003] | medium |
| F024 | substitution_risk | The source notes possible substitution toward other forms of corruption. | [P009] | medium |

## Naive Design Failure Modes

| failure_id | naive_design | why_it_fails | evidence_id | confidence |
|---|---|---|---|---|
| N001 | Use only official project accounts as the corruption outcome. | Official records may be manipulated or fail to reveal missing expenditures. | [P002], [P004], [P007], [P008] | high |
| N002 | Compare audited and unaudited projects without randomized assignment or timing control. | Differences could reflect which projects were selected for audit rather than audit effects. | [P001], [P005] | high |
| N003 | Measure only whether accountability meetings occurred. | Participation may increase without materially reducing missing expenditures. | [P003], [P006] | high |

## Evaluator Inference

| inference_id | inference | basis_evidence_id | use_in_later_tasks |
|---|---|---|---|
| I001 | Agent-facing tasks should generalize the public-project setting but preserve official-versus-independent outcome measurement. | [P002], [P007], [P008], [P010] | task construction |
| I002 | Full-credit gold answers should require independent measurement or auditing of actual inputs/quality, not just official spending reports. | [P002], [P004], [P007], [P008] | gold reference |

## Uncertainties

| uncertainty_id | uncertainty | evidence_id | consequence |
|---|---|---|---|
| U001 | Exact treatment assignment level, stratification, and clustering are not fully extracted. | [P001], [P005], [P006] | Gold reference should verify inference details before requiring a specific model. |
| U002 | Details of cost-benefit analysis and later results sections are not extracted. | [P009] | Task 07 should focus on design and measurement rather than exact reported effect sizes. |

## Facts Safe For Agent-Facing Packets

- Local public projects report official spending.
- Monitoring interventions can be randomly assigned before implementation.
- Independent technical measurement of actual inputs or quality is possible after completion.
- Outcomes can compare reported costs with independent cost estimates.

## Facts Unsafe For Agent-Facing Packets

- Source-paper title, author, venue, exact year.
- Exact country, program name, village count, and audit-probability numbers if leakage risk is high.
- Specific road-core engineering details if too recognizable, unless generalized.
- Any statement that the original answer uses independent engineers to estimate missing expenditures.
