<!-- visibility: evaluator-only -->
<!-- do_not_include_in_agent_context: true -->
<!-- case_id: C001 -->

# Source Packet: C001

## Paper Metadata

- paper_key: `dellavigna_2012_charity_social_pressure`
- title: Testing for Altruism and Social Pressure in Charitable Giving
- authors: Stefano DellaVigna, John A. List, Ulrike Malmendier
- year: 2012
- venue: Quarterly Journal of Economics
- registry_domain: `behavioral`
- registry_design_family: `mechanism_experiment`
- registry_key_failure_mode: `mechanism_confounding`
- source_pdf: `downloads/deepscientist_econ_business_experiment_papers/C001_DellaVigna_List_Malmendier_2012_Testing_for_Altruism_and_Social_Pressure_in_Charitable_Giving.pdf`
- source_url: `https://sdellavi.com/pdf/CharityQJEFeb12.pdf`
- pdf_pages: 56

## Research Question And Objective

- source_research_question: Does door-to-door charitable giving reflect donor utility from altruism or warm glow, or does it partly reflect social pressure from in-person solicitation?
- benchmark_research_objective: Given an anonymized fundraising setting, ask the agent to design an empirical field experiment that can separate genuine giving motives from pressure-induced giving.
- target_mechanism_or_estimand: Mechanism separation between altruism/warm glow and social pressure; the key empirical target is how advance notice and a low-cost avoidance option change contact and donation behavior.
- why_this_case_tests_agent_weakness: A generic randomized solicitation experiment can estimate an average effect but cannot identify the mechanism. The agent must notice that an avoidance or opt-out channel is the identification linchpin.

## Source Locations

| section | pdf_text_pages_used | role in benchmark construction |
|---|---|---|
| abstract | 1 | research question, headline intervention, headline outcome |
| introduction | 2-5 | mechanism contrast, field setting, opt-out design logic |
| experiment description | 3-5 | assignment arms and sorting channel |
| results summary | 1, 4-5 | behavioral interpretation and outcome pattern |

## Extracted Passages

[P001]
source_page: 1
section: abstract
why_included: Defines the central mechanism contrast and the core empirical intervention.
text: The paper studies whether charitable giving reflects altruism or warm glow versus a dislike of refusing in-person requests. The field design informs some households about the exact solicitation time using a flyer so that they can seek or avoid contact with the solicitor.

[P002]
source_page: 1
section: abstract
why_included: Records the primary behavioral outcomes used to infer social pressure.
text: Advance flyers reduce the probability that households open the door, and flyers with a Do Not Disturb option reduce giving. The decrease is concentrated among smaller donations, which is consistent with avoidance of social pressure rather than only lower altruistic demand.

[P003]
source_page: 2
section: introduction
why_included: Identifies why mechanism separation matters for welfare interpretation.
text: The introduction distinguishes supply-driven giving, where donors enjoy giving, from demand-driven giving, where donors would rather avoid a personal request. These mechanisms imply different welfare conclusions for fundraising.

[P004]
source_page: 3
section: introduction
why_included: Gives the field setting and sample frame needed for anonymized task construction.
text: The experiment is a door-to-door fundraising drive for two charities. Households in towns around a large US city were approached during 2008.

[P005]
source_page: 3
section: introduction
why_included: Captures the linchpin design detail.
text: The crucial design feature is that households can sort into or out of interaction with the solicitor. One treatment uses a flyer announcing a one-hour visit window, while another adds an opt-out box indicating that the household does not want to be disturbed.

[P006]
source_page: 3
section: introduction
why_included: Establishes comparison arms for later gold-reference extraction.
text: The flyer and opt-out conditions are compared against a baseline door-to-door solicitation condition with no advance flyer.

[P007]
source_page: 4
section: introduction
why_included: Records how the paper interprets door-opening behavior.
text: Lower door-opening after receiving a flyer is interpreted as evidence that some households avoid the solicitor. The baseline flyer has offsetting implications because altruistic households may seek the solicitor while pressure-averse households avoid the visit.

[P008]
source_page: 5
section: introduction
why_included: Notes complementary design logic that may appear as acceptable alternative detail.
text: A complementary survey experiment varies payment, duration, and whether the survey is announced with a flyer. This supports the broader interpretation that avoidance behavior responds to the private cost or benefit of interaction.

## Human Notes

- suspected_linchpin: The task must preserve the low-cost avoidance or opt-out channel. Without it, an agent can estimate solicitation effects but cannot credibly separate altruism/warm glow from social pressure.
- known_risks: Exact phrases such as Do Not Disturb, named charities, city/suburb details, and the distinctive door-hanger setup may leak the source if copied into agent-facing tasks.
- extraction_uncertainties: Later pages should be checked in Task 06 for exact randomization unit, treatment counts, and inference details before writing the gold reference.
