<!-- visibility: evaluator-only -->
<!-- do_not_include_in_agent_context: true -->
<!-- case_id: C016 -->

# Gold Reference: C016

## Hidden Answer Summary

This evaluator-only gold reference defines what a valid answer must handle for the adolescent health-information case. A strong answer does not need to reproduce the original source paper's exact country, disease framing, or precise partner-age language, but it must recognize that this is not a generic "information campaign" benchmark. The case tests whether the agent can separate the content of information, the credibility of outcome measurement, and the behavioral margin on which the intervention operates.

## Core Research Problem

- Research question: Does targeted partner-risk information change adolescent behavior more effectively than the standard generic risk-avoidance curriculum? Evidence: F002, F017-F018, F025-F028.
- Benchmark objective: Design an experiment that distinguishes generic curriculum effects from targeted-information effects and that does not rely only on self-report. Evidence: F003-F004, F021-F029.
- Target mechanism or estimand: Effect of targeted risk information on objectively measured downstream unsafe-behavior consequences, plus mechanism evidence on partner choice or protection. Evidence: F018, F021-F024, F028-F029.
- Treatment or exposure: School-level assignment to a standard generic-information condition, a targeted risk-information condition, or both depending on the design extension. Evidence: F017-F020.
- Outcome: Objective downstream consequence related to unprotected behavior, with self-reported partner and protection behavior treated as secondary evidence. Evidence: F021-F024.
- Unit of analysis: Individual adolescent outcome under school-level or classroom-level assignment. Evidence: F005-F008.

## Data Structure

- Observation unit: Individual adolescent, nested within assigned schools or classrooms. Evidence: F005-F007.
- Assignment level: School or classroom-wide implementation unit. Evidence: F006, F025-F026.
- Outcome measurement level: Individual-level objective downstream outcome, with supplementary survey-based mechanism outcomes for a selected subgroup. Evidence: F007, F021-F024.
- Time structure: Intervention during the focal school year, followed by short-run status checks, home verification for objective outcomes, and a later selected behavioral survey. Evidence: F009-F011.
- Required comparison structure: Targeted-information content must be compared against generic information content, not merely against no intervention. Evidence: F017-F019, F027.
- Required inference level: At least school- or classroom-level clustered inference. Evidence: F008, F011.

## Original Identification Logic

The source design is a randomized field experiment at the school level. The critical comparison is between a standard generic curriculum and a targeted-information campaign that provides more differentiated partner-risk information. Randomization identifies treatment-content effects, while the use of an objective downstream consequence as the primary outcome protects against overreliance on selected, socially sensitive self-reports. Self-reported partner and protection behavior then provide suggestive mechanism evidence about intensive-margin adjustments. Evidence: F025-F033.

## Linchpin Detail

- Linchpin 1: The design must compare targeted risk information with the standard generic curriculum. Evidence: L001.
- Why it matters: Without this contrast, the study reduces to a generic information-treatment question and misses the content mechanism. Evidence: F017-F020, F027.
- What fails without it: An answer that says "provide information and compare treated versus untreated" does not test the distinctive research problem. Evidence: N001.
- Linchpin 2: The primary outcome must be an objective downstream consequence rather than self-report alone. Evidence: L002.
- Why it matters: This benchmark is partly about whether the agent recognizes measurement as part of identification. Evidence: F021-F024, F029.
- What fails without it: A survey-only design can overclaim on noisy or socially desirable responses. Evidence: N002.
- Linchpin 3: Mechanism claims should be framed around intensive-margin adjustment, partner substitution, or protection rather than only abstinence. Evidence: L003.
- Why it matters: The intervention may change how adolescents engage in risky behavior rather than whether they engage at all. Evidence: F028, F033.

## Must-Have Conditions

- The answer must distinguish targeted partner-risk information from generic risk-avoidance information.
- The answer must use random or otherwise credibly exogenous variation in information content.
- The answer must center an objective downstream outcome and treat self-reports as supplementary or limited.
- The answer must explain what mechanism can and cannot be inferred from the observed outcomes.
- The answer must address spillovers, implementation-channel differences, or both when interpreting mechanism claims.

## Acceptable Alternative Designs

| design | conditions under which it is acceptable | supports what claim | cannot support what claim |
|---|---|---|---|
| Randomized school-level comparison between a standard generic curriculum module and a targeted partner-risk module, with administrative pregnancy or verified childbearing outcomes | Assignment must be exogenous at the school or classroom level; outcome measurement must be objective and comparably collected across arms. | Can identify whether targeted content changes downstream risky-behavior consequences more than generic content. | Cannot by itself fully isolate whether content or facilitator style drives the effect if delivery channels differ. |
| Factorial design crossing generic curriculum content and targeted risk-content add-on, all delivered by the same facilitators | Delivery must be harmonized so that content rather than implementer differences drives variation. | Can isolate whether the targeted content adds value beyond the generic curriculum. | Cannot identify broader equilibrium effects or long-run disease transmission without additional data. |
| Randomized content variation plus objective administrative outcome and a separately validated mechanism subsample | Mechanism subsample must be clearly secondary and its selection limits acknowledged. | Can support causal claims on the main outcome and suggestive mechanism claims on partner choice or protection. | Cannot support strong population-level mechanism claims if the subsample is highly selected. |

## Common Invalid Designs

| design or claim | why unacceptable | error label |
|---|---|---|
| Randomize only whether any health information is provided and conclude that targeted partner-risk content is better. | This does not compare content types. Evidence: N001, L001. | Mis-specified Estimand |
| Use a self-reported sexual-behavior survey as the sole primary outcome. | The benchmark requires recognizing measurement bias and the need for an objective outcome. Evidence: N002, L002. | Measurement Error |
| Interpret lower pregnancy or lower objective-risk outcome as proof that total sexual activity fell. | The mechanism may run through safer partner selection or protection rather than total abstinence. Evidence: N003, L003. | Mechanism Confounding |
| Ignore spillovers and treat school-level assignment as if no within-school or nearby-school interference exists. | Information and partner markets may spill across cohorts or locations. Evidence: N004, F016, F032. | Spillover Blindness |
| Attribute all observed effects to the content alone without discussing possible delivery-channel or facilitator confounds. | The targeted campaign format may differ from the generic curriculum. Evidence: F020, F033. | Overclaim |

## Claim-Evidence Expectations

| expected claim | required supporting evidence | claim type | confidence |
|---|---|---|---|
| Targeted partner-risk information is the relevant treatment contrast, not generic information versus no information. | F017-F020, F027, L001 | causal / design | high |
| Objective downstream outcomes are central to credible inference in this case. | F021-F024, F029, L002 | measurement | high |
| Mechanism claims should focus on intensive-margin change rather than assume abstinence effects. | F028, F033, L003 | mechanism | high |
| Self-reported outcomes can be used only with explicit caveats about selection and reporting bias. | F023-F024, F031 | limitation | high |
| Spillovers or implementation-channel differences limit overconfident interpretation. | F016, F032-F033 | limitation | medium |

## Scoring Notes

- Full-credit answer: Proposes randomized or otherwise credibly exogenous school- or classroom-level variation in information content, compares targeted information with generic curriculum content, uses an objective downstream outcome as the primary endpoint, and interprets mechanisms in intensive-margin terms with explicit caveats.
- Partial-credit answer: Proposes a reasonable randomized information-content study and recognizes that objective outcomes are preferable, but does not clearly articulate why generic curriculum and targeted information differ or overstates what self-reports can show.
- Critical omission: No objective main outcome, no content contrast, or no exogenous variation in information content.
- Automatic failure: Claims that a self-report-only survey, a generic health-education comparison, or observational exposure to information messages can by itself identify the targeted mechanism.
