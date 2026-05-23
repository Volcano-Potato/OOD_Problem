<!-- visibility: evaluator-only -->
<!-- do_not_include_in_agent_context: true -->
<!-- case_id: C014 -->

# Gold Reference: C014

## Hidden Answer Summary

This evaluator-only gold reference defines what a valid answer must handle for the corruption-monitoring case. A valid answer does not need to reproduce the exact public-project setting, but it must recognize that outcome measurement is part of identification because official records can be manipulated.

## Core Research Problem

- Research question: Do top-down audits or grassroots monitoring reduce corruption in local public projects? Evidence: F002.
- Benchmark objective: Design an evaluation that estimates monitoring effects while using an outcome not controlled by potentially corrupt actors. Evidence: F003.
- Target estimand: Causal effect of audit probability and participation interventions on missing expenditures or equivalent corruption outcomes. Evidence: F010-F017.
- Treatment or exposure: External audit probability and grassroots monitoring interventions. Evidence: F010-F013.
- Outcome: Missing expenditures or equivalent discrepancy between reported spending and independently estimated actual costs. Evidence: F014-F016.
- Unit of analysis: Local public project or village project. Evidence: F005-F007.

## Data Structure

- Observation unit: Local public project/village project. Evidence: F005.
- Assignment level: Village/project intervention assignment. Evidence: F006.
- Outcome measurement level: Project/village level discrepancy between official and independent cost estimates. Evidence: F007.
- Time structure: Audit notification after funds are awarded but before construction; independent measurement after completion. Evidence: F008.
- Required measurement structure: Official reports must be compared with independent technical cost/quality estimates. Evidence: F014-F016.
- Current uncertainty: Exact assignment, stratification, clustering, and model details are not fully extracted. Evidence: U001.

## Original Identification Logic

The source uses a randomized field experiment. Audit effects are identified by comparing projects assigned to higher audit probability with projects not assigned to that condition. Causal interpretation depends not only on random assignment, but also on measuring corruption using independent cost estimates rather than relying only on official spending reports. Evidence: F018-F021.

## Linchpin Detail

- Linchpin: Construct an independent estimate of actual project costs. Evidence: L001.
- Why it matters: It prevents the outcome from being defined solely by official records produced by actors who may manipulate or obscure corruption. Evidence: F020.
- What fails without it: A design using only official reports could miss or understate corruption. Evidence: L001, N001.
- Secondary linchpin: Audit timing occurs after funding but before implementation. Evidence: L002.
- Additional mechanism detail: Comparing top-down auditing with grassroots monitoring can distinguish intervention channels. Evidence: L003.

## Must-Have Conditions

- The answer must address outcome manipulability or measurement error in official records.
- The answer must propose independent measurement, audit verification, engineering/technical inspection, third-party cost estimates, or equivalent hard outcome construction.
- The answer must identify randomized or otherwise credible variation in monitoring intensity.
- The answer must align assignment and inference at the project/village level rather than treating line items as independent units.
- The answer must distinguish monitoring participation/process outcomes from actual corruption outcomes.

## Acceptable Alternative Designs

| design | conditions under which it is acceptable | supports what claim | cannot support what claim |
|---|---|---|---|
| Randomized audit-probability experiment with independent cost estimates | Audit assignment must be exogenous; independent measurement must occur after implementation. | Can estimate audit effect on missing expenditures. | Cannot fully measure corruption forms not captured by the independent cost measure. |
| Randomized third-party monitoring with objective quality/input inspections | Inspection must be independent of implementing officials and comparable across projects. | Can estimate monitoring effect on objectively measured leakage or quality. | Cannot claim effects on all corruption channels without broader measures. |
| Staggered audit rollout with pre-specified independent measurements | Rollout timing must be plausibly exogenous; pre/post and comparison projects must be credible. | Can estimate monitoring effects if timing assumptions hold. | Cannot support causal claims if audits target suspicious projects. |

## Common Invalid Designs

| design or claim | why unacceptable | error label |
|---|---|---|
| Use only official project accounts as the corruption outcome. | Official records may be manipulated or fail to reveal missing expenditures. Evidence: N001. | Measurement Credulity |
| Compare audited and unaudited projects without randomization or assignment logic. | Audit selection may reflect project risk or suspicion. Evidence: N002. | Selection |
| Measure only meeting attendance or complaint volume and call it corruption reduction. | Participation can increase without reducing missing expenditures. Evidence: N003. | Overclaim |
| Treat line-item observations as independent when assignment is at project/village level. | Inference would overstate precision. Evidence: F006-F007. | Inference Mismatch |
| Ignore substitution to other corruption forms. | Measured missing expenditures may not capture all behavioral responses. Evidence: F017, F024. | Critical Design Omission |

## Claim-Evidence Expectations

| expected claim | required supporting evidence | claim type | confidence |
|---|---|---|---|
| Official records alone are not clean corruption outcomes. | F004, F014-F016, L001 | measurement | high |
| Independent measurement is central to identification. | F020, L001 | identification | high |
| Audit treatment requires credible assignment timing. | F008, L002 | assumption | medium |
| Participation outcomes are not the same as corruption outcomes. | F021, F023, N003 | limitation | high |

## Scoring Notes

- Full-credit answer: Proposes randomized or otherwise credible monitoring variation plus independent outcome measurement of actual inputs/costs/quality; handles project-level assignment and official-record manipulation risk.
- Partial-credit answer: Proposes randomized audits but gives weak or generic outcome measurement, or proposes independent measurement but weak assignment logic.
- Critical omission: No independent or hard outcome measure beyond official reports.
- Automatic failure: Claims corruption reduction from official accounts, meeting attendance, or selected audits without causal assignment and measurement safeguards.
