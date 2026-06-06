<!-- visibility: evaluator-only -->
<!-- do_not_include_in_agent_context: true -->
<!-- case_id: C016 -->

# Source Packet: C016

## Paper Metadata

- paper_key: `dupas_2011_hiv_information`
- title: Do Teenagers Respond to HIV Risk Information? Evidence from a Field Experiment in Kenya
- authors: Pascaline Dupas
- year: 2011
- venue: American Economic Journal: Applied Economics
- registry_domain: `health`
- registry_design_family: `field_experiment`
- registry_key_failure_mode: `measurement_error`
- source_pdf: `downloads/deepscientist_econ_business_experiment_papers/C016_Dupas_2011_Do_Teenagers_Respond_to_HIV_Risk_Information_Evidence_from_a_Field_Experiment_in_Kenya.pdf`
- source_url: `http://www.aeaweb.org/articles.php?doi=10.1257/app.3.1.1`
- pdf_pages: 34

## Research Question And Objective

- source_research_question: Does providing adolescents with partner-risk-specific sexual health information change behavior more effectively than the standard generic risk-avoidance curriculum?
- benchmark_research_objective: Given an anonymized adolescent health-information setting, ask the agent to design a study that separates generic curriculum effects from more targeted risk-information effects while dealing seriously with outcome measurement and self-report bias.
- target_mechanism_or_estimand: Effect of targeted partner-risk information, relative to standard generic health-risk education, on objectively measured unsafe-sex-related outcomes and on partner-choice or protection mechanisms.
- why_this_case_tests_agent_weakness: Agents often default to self-reported behavior surveys, generic information-treatment logic, or simple education-treatment comparisons. The source linchpin is that outcome measurement and the content of the information intervention are both part of identification.

## Source Locations

| section | pdf_text_pages_used | role in benchmark construction |
|---|---|---|
| abstract | 1 | core research question, objective outcome, intensive-versus-extensive margin conclusion |
| introduction and motivation | 2-4 | why generic risk-avoidance information may fail, why partner-risk information may matter |
| experimental design overview | 3-5 | randomized school-level design, generic curriculum arm, targeted-information arm |
| theory and mechanism intuition | 10-11 | partner selection, protection, and intensive-versus-extensive margin logic |
| timeline and sample | 12-13 | treatment timing, grade-specific exposure, attrition and follow-up structure |
| childbearing outcome measurement | 13-15 | objective outcome construction, proxy limitations, home follow-up validation |
| self-reported behavioral follow-up | 14-15, 24-25 | survey selection limits, reporting-bias concerns, mechanism evidence |
| estimation strategy and balance | 15-16, 30 | randomization, balance, clustered inference |
| partner-age and spillover discussion | 20-23 | mechanism interpretation, spillovers across cohorts and schools |
| conclusion and limitations | 28-29 | video confounding concern, implementer concern, external-validity caveat |

## Extracted Passages

[P001]
source_page: 1
section: abstract
why_included: States the headline contrast between targeted risk information and the standard curriculum, plus the objective-outcome logic.
text: Providing information on the relative risk of infection by partner type led to a large decrease in teen pregnancy, an objective proxy for unprotected sex, while the official abstinence-only curriculum had no impact on teen pregnancy.

[P002]
source_page: 2
section: introduction
why_included: Establishes that generic abstinence-oriented messages may miss an important behavioral margin.
text: If behavior is more elastic on the intensive margin, such as partner choice or protection, than on the extensive margin of whether to have sex at all, programs focused only on abstinence may ignore an important margin of risk reduction.

[P003]
source_page: 2-3
section: introduction
why_included: Preserves the mechanism intuition behind partner-risk information.
text: Risk differs across partner types because older partners can be substantially riskier than same-age partners, while also providing more economic resources, so relative-risk information may alter partner choice or protection decisions.

[P004]
source_page: 3
section: experimental design overview
why_included: Captures the randomized contrast between the standard curriculum arm and the targeted-information arm.
text: Half of the schools were randomly assigned to receive teacher training on the standard curriculum. A subset of schools, randomly selected after stratifying by teacher-training status, received a separate information campaign that presented risk prevalence disaggregated by partner characteristics.

[P005]
source_page: 3-4
section: results summary
why_included: States the key objective outcome and mechanism pattern.
text: The standard curriculum had no effect on whether girls started childbearing within a year, while the targeted information reduced that outcome and appears to have shifted behavior away from riskier partners rather than simply reducing all sexual activity.

[P006]
source_page: 4
section: motivation
why_included: Explains why objective outcomes matter.
text: Earlier studies often relied solely on self-reported sexual behavior, which is likely to suffer from social desirability bias, whereas the present study combines randomization with an objective outcome related to unprotected sex.

[P007]
source_page: 12-13
section: timeline and sample
why_included: Gives the staged data structure and treatment timing.
text: The generic curriculum arm was rolled out earlier and school-wide, while the targeted information campaign was later delivered to the final primary-school grade only. Follow-up combined school visits, home visits for girls who had begun childbearing, and a later behavioral survey among students observed in secondary school.

[P008]
source_page: 13-14
section: childbearing data
why_included: Defines the core objective outcome and how it was measured.
text: The main outcome is incidence of childbearing within a short follow-up window. School-based status checks and home follow-up visits were used to verify whether girls had begun childbearing and, when possible, the age profile of the partner involved.

[P009]
source_page: 14-15
section: measurement caveats
why_included: Preserves the fact that the objective outcome is useful but imperfect.
text: Childbearing is an imperfect proxy for unsafe sex because pregnancy risk varies by partner type, abortion and nonvaginal sex are not observed, and same-age risky sex may not map one-for-one into pregnancy, but the measure remains more objective than self-reported behavior alone.

[P010]
source_page: 15
section: behavioral follow-up
why_included: Captures the self-report selection and reporting-bias concern.
text: The follow-up behavioral survey covers only those who joined secondary school and may therefore represent a selected subgroup. Self-reported sexual behavior may also suffer from reporting bias and familiarity with the implementing organization.

[P011]
source_page: 16
section: estimation strategy
why_included: States the randomization and inference structure.
text: Random assignment of schools to treatment and comparison groups provides identification in expectation, and inference is clustered at the school level.

[P012]
source_page: 22-23
section: spillovers and interpretation
why_included: Preserves the interference risk.
text: Spillovers may run through information sharing within schools or through market-like reallocation of risky partners across nearby schools or adjacent cohorts, complicating interpretation of treatment-control comparisons.

[P013]
source_page: 28-29
section: conclusion and limitations
why_included: Records the key mechanism and external-validity caveats.
text: The evidence suggests greater elasticity on the intensive margin than on the extensive margin. However, one cannot fully rule out that ancillary discussion content, nonteacher facilitators, or role-model effects contributed to the impact of the targeted information campaign.

## Human Notes

- suspected_linchpin: The anonymous task must preserve two linked ideas: the contrast is about information content, not just "information versus no information," and the most credible primary outcome is an objective downstream consequence rather than self-report.
- known_risks: The source is highly leak-prone if agent-facing files mention HIV, Kenya, exact school counts, "sugar daddies," exact age cutoffs, or the title-level framing around older partners.
- extraction_uncertainties: Task 06 should verify how strongly the gold reference should require discussion of the implementer/video confound, whether the control-cohort difference-in-difference logic should remain evaluator-only, and how much partner-age structure can safely appear in Level 2 versus Level 3 packets.
