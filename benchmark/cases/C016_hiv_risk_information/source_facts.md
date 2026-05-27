<!-- visibility: evaluator-only -->
<!-- do_not_include_in_agent_context: true -->
<!-- case_id: C016 -->

# Source Facts: C016

## Scope

These facts are extracted only from `source_packet.md`. They are evaluator-only inputs for later `gold_reference.md` and anonymized task construction.

## Research Context

| fact_id | category | fact | evidence_id | confidence |
|---|---|---|---|---|
| F001 | research_context | The setting is a school-based adolescent health-information environment in which policymakers want to reduce unsafe behavior through scalable information interventions. | [P002], [P007] | high |
| F002 | research_question | The source asks whether targeted partner-risk information changes adolescent behavior more effectively than the standard generic risk-avoidance curriculum. | [P001], [P004], [P005] | high |
| F003 | benchmark_objective | The benchmark objective is to distinguish information-content effects from generic education effects while taking outcome measurement seriously. | [P001], [P005], [P006] | high |
| F004 | central_threat | A study can go wrong either by treating all information interventions as equivalent or by relying too heavily on self-reported behavior. | [P002], [P006], [P009], [P010] | high |

## Data Structure

| fact_id | field | extracted fact | evidence_id | confidence |
|---|---|---|---|---|
| F005 | observation_unit | The relevant observation is an individual adolescent, with some outcomes aggregated from school-based treatment assignment. | [P007], [P008], [P011] | high |
| F006 | assignment_level | Information treatments are assigned at the school or classroom-wide implementation level rather than at the individual level. | [P004], [P011] | high |
| F007 | outcome_measurement_level | The primary outcome is measured at the individual level through downstream childbearing status, with some partner-characteristic information collected for a subset. | [P008], [P009] | high |
| F008 | clustering_or_inference_level | Inference is clustered at the school level. | [P011] | high |
| F009 | time_span | The design includes baseline exposure conditions, intervention rollout, and follow-up within roughly the next academic year. | [P007], [P008] | high |
| F010 | panel_or_repeated_observations | The design is not a long panel for all individuals, but it has staged follow-up and some cohort-based or subgroup-based repeated comparisons. | [P007], [P010] | medium |
| F011 | sample_construction | A focal adolescent cohort is exposed during the final primary-school grade, then followed through school visits, home verification for objective outcomes, and a later selected behavioral survey. | [P007], [P008], [P010] | high |
| F012 | treatment_exposure_variable | Treatments differ in the content and delivery of health-risk information, including a standard generic curriculum arm and a targeted partner-risk information arm. | [P004], [P005], [P013] | high |
| F013 | outcome_variable | The core outcome is an objective downstream consequence related to unprotected behavior, with self-reported behavior used only as supplementary mechanism evidence. | [P001], [P006], [P008], [P010] | high |
| F014 | covariates | Baseline school characteristics, pre-treatment cohort characteristics, student sex, schooling status, and partner-characteristic measures are relevant design covariates. | [P007], [P008], [P011] | medium |
| F015 | missingness_or_attrition | Attrition for location/status follow-up is relatively low, but behavioral-survey coverage is selective because it includes only students observed in secondary school. | [P007], [P010] | high |
| F016 | spillover_risk | Information and partner-market spillovers may arise within schools, across cohorts, or across nearby schools. | [P012] | high |

## Treatment / Variation / Exposure

| fact_id | category | fact | evidence_id | confidence |
|---|---|---|---|---|
| F017 | standard_information_arm | One arm delivers the standard curriculum that emphasizes generic risk avoidance and abstinence-oriented content. | [P004], [P005] | high |
| F018 | targeted_information_arm | Another arm delivers information that differentiates risk across partner types or partner profiles rather than giving only average-risk messages. | [P001], [P003], [P004] | high |
| F019 | layered_assignment | The targeted-information arm is assigned after stratifying on the generic-curriculum assignment, so the design can compare content types while preserving randomized variation. | [P004] | medium |
| F020 | implementation_channel | The targeted information is delivered through a campaign format that may differ from the standard teacher-led curriculum, introducing a possible implementation-channel confound. | [P013] | medium |

## Outcomes And Measurement

| fact_id | outcome | measurement_method | evidence_id | confidence |
|---|---|---|---|---|
| F021 | objective_main_outcome | The main outcome is whether girls began childbearing within the follow-up window, measured through school status checks and home verification. | [P005], [P008] | high |
| F022 | partner_profile_suboutcome | For girls who begin childbearing, home follow-up can recover whether the partner belonged to a riskier profile. | [P005], [P008] | medium |
| F023 | self_reported_behavior | Secondary outcomes include self-reported sexual activity, partner characteristics, and protection behavior among a selected subgroup. | [P010] | high |
| F024 | measurement_limit | The objective outcome is useful but imperfect because it does not capture all risky behavior and may understate same-age risky behavior. | [P009] | high |

## Identification Logic

| fact_id | component | extracted fact | evidence_id | confidence |
|---|---|---|---|---|
| F025 | design_family | The source design is a randomized field experiment with school-level assignment of information-content interventions. | [P004], [P011] | high |
| F026 | source_of_variation | Identifying variation comes from randomized differences in which schools receive generic curriculum support and which receive targeted partner-risk information. | [P004], [P011] | high |
| F027 | comparison_group | The key comparison is not simply treated versus untreated schools, but targeted risk information versus generic risk-avoidance information, with control comparisons over time or across schools. | [P001], [P004], [P005] | high |
| F028 | mechanism_test | Mechanism interpretation depends on whether the targeted information changes partner choice or protection behavior rather than only abstinence or broad sexual activity. | [P002], [P003], [P005], [P013] | high |
| F029 | why_objective_outcome_is_central | Objective downstream outcomes are central because self-reports alone are vulnerable to social-desirability bias and selected follow-up coverage. | [P006], [P009], [P010] | high |

## Linchpin Details

| linchpin_id | detail | why_it_matters | what_fails_without_it | evidence_id | confidence |
|---|---|---|---|---|---|
| L001 | The design must distinguish targeted partner-risk information from the standard generic curriculum. | The benchmark is about information content, not about any information intervention versus no information. | A generic "health education works" design cannot isolate whether content about differentiated partner risk matters. | [P001], [P004], [P005] | high |
| L002 | The design must treat the objective downstream consequence as the primary outcome and self-report as supplementary. | This blocks a common failure mode where mechanism stories rely only on socially sensitive self-reports. | Without the objective outcome, the agent could overclaim from noisy or biased survey responses. | [P006], [P008], [P009], [P010] | high |
| L003 | Mechanism claims should focus on intensive-margin adjustment, such as partner choice or protection, rather than assuming reduced activity on the extensive margin. | The source conclusion is not generic abstinence success; it is a shift in risk composition and behavior margin. | Without this distinction, the design can confuse safer substitution with total abstinence or total risk avoidance. | [P002], [P005], [P013] | high |

## Robustness / Placebo / Mechanism Checks

| fact_id | check_type | extracted fact | evidence_id | confidence |
|---|---|---|---|---|
| F030 | balance_and_randomization_check | School-level randomization and balance checks support the identifying assumption. | [P011] | high |
| F031 | selected_self_report_check | Self-reported behavior is used only as suggestive mechanism evidence because the sample is selected and may be reporting-biased. | [P010] | high |
| F032 | spillover_check | Difference-in-difference or cohort comparisons are informative but can be complicated by spillovers across adjacent cohorts or nearby schools. | [P012] | medium |
| F033 | implementation_confound_check | The targeted-information effect may partly reflect facilitator or campaign-format differences rather than content alone, so interpretation should be careful. | [P013] | medium |

## Naive Design Failure Modes

| failure_id | naive_design | why_it_fails | evidence_id | confidence |
|---|---|---|---|---|
| N001 | Compare a generic curriculum arm to no curriculum and conclude that targeted partner-risk information is unnecessary. | This does not test information-content differences. | [P004], [P005], [L001] | high |
| N002 | Use only self-reported sexual behavior as the main outcome. | Self-reports are selected and vulnerable to reporting bias. | [P006], [P010], [L002] | high |
| N003 | Interpret lower pregnancy alone as proof that all sexual activity fell. | The source emphasizes intensive-margin adjustment and partner substitution. | [P002], [P005], [L003] | high |
| N004 | Ignore spillovers or implementation-channel differences when interpreting content effects. | School-based information may spill across cohorts or nearby schools, and facilitator differences can contaminate interpretation. | [P012], [P013] | medium |

## Evaluator Inference

| inference_id | inference | basis_evidence_id | use_in_later_tasks |
|---|---|---|---|
| I001 | Agent-facing packets should preserve a school-based youth-information setting, a standard generic-information arm, and a targeted-information arm without naming HIV, Kenya, or source-specific partner labels. | [P001]-[P005] | leakage control |
| I002 | Full-credit answers should require an objective downstream outcome and should not treat self-report as sufficient on its own. | [P006], [P008]-[P010] | gold reference |
| I003 | Discussion of facilitator/video confounding should count as stronger reasoning but does not need to be an automatic failure if omitted. | [P013] | scoring design |

## Uncertainties

| uncertainty_id | uncertainty | evidence_id | consequence |
|---|---|---|---|
| U001 | The exact relative importance of the home-follow-up partner-age suboutcome versus the main objective outcome is not fully pinned down from the source packet alone. | [P008] | Gold reference should avoid requiring a single exact secondary outcome specification. |
| U002 | The source includes cohort-based difference-in-difference logic, but agent-facing tasks may not need to reveal that extra structure. | [P012] | Lower-level packets should keep the randomized cross-school variation primary. |
| U003 | The implementer/video confound is real but may be too source-specific for lower-level packets. | [P013] | Keep this mainly evaluator-only or Level 3 threat material. |

## Facts Safe For Agent-Facing Packets

- The setting is school-based adolescent health-risk information provision.
- The study can compare generic risk-avoidance information with more targeted information about differential risk across partner types.
- Assignment occurs at the school or classroom-wide level.
- An objective downstream outcome related to unprotected behavior is available.
- Self-reported behavior exists but is noisier and more selective.
- Spillovers and mechanism confounding are genuine concerns.

## Facts Unsafe For Agent-Facing Packets

- Source-paper title, author, venue, and year.
- Exact country, disease name, exact school counts, and exact age cutoffs.
- Distinctive source phrases such as "sugar daddies."
- Exact effect sizes and source-specific cost-effectiveness numbers.
- Exact program names and exact official-curriculum labels.
