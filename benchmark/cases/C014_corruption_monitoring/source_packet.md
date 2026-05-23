<!-- visibility: evaluator-only -->
<!-- do_not_include_in_agent_context: true -->
<!-- case_id: C014 -->

# Source Packet: C014

## Paper Metadata

- paper_key: `olken_2007_corruption_monitoring`
- title: Monitoring Corruption: Evidence from a Field Experiment in Indonesia
- authors: Benjamin A. Olken
- year: 2007
- venue: Journal of Political Economy
- registry_domain: `political_econ`
- registry_design_family: `field_experiment`
- registry_key_failure_mode: `measurement_error`
- source_pdf: `downloads/deepscientist_econ_business_experiment_papers/Olken_2007_Monitoring_Corruption_Evidence_from_a_Field_Experiment_in_Indonesia.pdf`
- source_url: `https://www.povertyactionlab.org/sites/default/files/research-paper/27_Olken_Monitoring_Corruption.pdf`
- pdf_pages: 50

## Research Question And Objective

- source_research_question: Do top-down audits or grassroots monitoring reduce corruption in local public projects?
- benchmark_research_objective: Given an anonymized public-project monitoring setting, ask the agent to design an evaluation that estimates anti-corruption effects while using an outcome measure that is not itself controlled by potentially corrupt actors.
- target_mechanism_or_estimand: Causal effect of audit probability and participation interventions on missing expenditures, measured using independent estimates of actual project costs.
- why_this_case_tests_agent_weakness: Agents may treat official spending records as clean outcomes. This case tests whether the agent recognizes outcome manipulability and designs independent measurement as part of identification.

## Source Locations

| section | pdf_text_pages_used | role in benchmark construction |
|---|---|---|
| abstract | 1 | research question, audit treatment, independent outcome |
| introduction | 2-5 | monitoring mechanisms and measurement challenge |
| setting | 5-7 | village infrastructure program context |
| experimental interventions | 3-5, 8 | audit and grassroots monitoring arms |
| outcome measurement | 4-5 | independent engineering estimate and missing expenditures |

## Extracted Passages

[P001]
source_page: 1
section: abstract
why_included: Defines the research question and main intervention.
text: The paper evaluates randomized anti-corruption interventions in village road projects, including increasing the probability of government audits from a low baseline to certainty.

[P002]
source_page: 1
section: abstract
why_included: Captures the measurement linchpin.
text: The main corruption outcome is missing expenditures, measured as the discrepancy between official project costs and an independent engineering estimate of actual costs.

[P003]
source_page: 1
section: abstract
why_included: Records headline contrast between monitoring approaches.
text: Increased government audits reduce missing expenditures, while grassroots monitoring has limited average impact except under conditions that reduce free-riding or elite capture.

[P004]
source_page: 2
section: introduction
why_included: Explains why outcome measurement is difficult.
text: Corruption is inherently hard to measure directly, which has limited empirical evidence on how best to reduce it.

[P005]
source_page: 3
section: introduction
why_included: Records the randomized audit treatment and timing.
text: Some villages are randomly told, after funds are awarded but before road construction begins, that their project will later be audited by the central government audit agency.

[P006]
source_page: 3
section: introduction
why_included: Captures alternative treatment arms.
text: The study also tests grassroots participation interventions, including broad meeting invitations and anonymous comment forms for accountability meetings.

[P007]
source_page: 4
section: outcome measurement
why_included: Details the independent measurement process.
text: After construction, engineers and surveyors estimate actual road costs using core samples, local supplier price surveys, and interviews about wages, then compare these estimates with village spending reports.

[P008]
source_page: 4
section: outcome measurement
why_included: Defines the key outcome.
text: Missing expenditures are defined as the difference between what the village reported spending and what independent engineers estimated the road actually cost.

[P009]
source_page: 5
section: results and interpretation
why_included: Flags a measurement and mechanism nuance.
text: Even with certain external audit, a substantial share of expenditures remains unaccounted for, and some evidence suggests possible substitution toward other forms of corruption.

[P010]
source_page: 5
section: setting
why_included: Provides anonymizable institutional context.
text: The projects are local infrastructure projects funded through a national village-level program; villages propose projects and funded projects must report expenditures through accountability processes.

## Human Notes

- suspected_linchpin: The task must preserve that official spending records are not a clean outcome. A strong design needs independent measurement of actual inputs or quality.
- known_risks: Exact country, program name, road-project details, and audit-probability numbers can identify the paper. Agent-facing tasks should generalize them while preserving official-versus-independent measurement.
- extraction_uncertainties: Task 06 should verify treatment assignment level, stratification or subdistrict randomization details, and standard-error clustering before writing the gold reference.
