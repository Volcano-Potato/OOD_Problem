<!-- visibility: evaluator-only -->
<!-- do_not_include_in_agent_context: true -->
<!-- case_id: C001 -->

# Gold Reference: C001

## Hidden Answer Summary

This evaluator-only gold reference defines what a valid answer must handle for the charitable-giving mechanism case. A valid agent answer does not need to reproduce the original paper, but it must propose a design that can distinguish genuine willingness to give from pressure-induced giving.

## Core Research Problem

- Research question: Does in-person charitable giving reflect altruism/warm glow or social pressure from refusing a direct request? Evidence: F002.
- Benchmark objective: Design an empirical field experiment that separates genuine giving motives from pressure-induced giving. Evidence: F003.
- Target mechanism or estimand: Mechanism separation between altruism/warm glow and social pressure; treatment effects of advance notice and low-cost avoidance on contact and donation behavior. Evidence: F003, F014-F016.
- Treatment or exposure: Baseline solicitation, advance notice, and advance notice plus low-cost opt-out/avoidance. Evidence: F010-F013.
- Outcome: Door opening/contact, donation probability, donation amount, and small-donation pattern. Evidence: F014-F016.
- Unit of analysis: Household solicitation/contact opportunity. Evidence: F005-F007.

## Data Structure

- Observation unit: Household contact opportunity. Evidence: F005.
- Assignment level: Household solicitation level. Evidence: F006.
- Outcome measurement level: Household interaction level. Evidence: F007.
- Time structure: Advance notice before a scheduled solicitation window. Evidence: F008.
- Required comparison structure: No-notice baseline versus advance notice, and advance notice versus advance notice with low-cost opt-out. Evidence: F018.
- Current uncertainty: Exact sample size, treatment counts, and inference details are not yet extracted, so gold scoring should not require exact standard-error formulas. Evidence: U001.

## Original Identification Logic

The source design is a mechanism experiment embedded in a field experiment. Advance notice lets households seek or avoid contact, and adding a low-cost opt-out channel lowers the cost of avoiding an unwanted solicitation. Door-opening and giving responses to these avoidance options provide evidence about whether observed giving is driven by altruistic demand or by social pressure. Evidence: F017-F020.

## Linchpin Detail

- Linchpin: The design includes a low-cost avoidance or opt-out channel before the solicitation interaction. Evidence: L001.
- Why it matters: Avoidance behavior is direct evidence that some households prefer not to face the solicitation, which is essential for identifying pressure-induced giving. Evidence: L001, F019-F020.
- What fails without it: A generic randomized solicitation can estimate whether solicitation changes donations, but cannot distinguish altruism/warm glow from social pressure. Evidence: L001, N001.
- Secondary linchpin: Comparing advance notice alone with advance notice plus opt-out prevents interpreting all flyer effects as simple awareness or scheduling. Evidence: L002.

## Must-Have Conditions

- The answer must separate donation effects from contact/avoidance behavior, not only report total giving.
- The answer must include some way for subjects to avoid the solicitation at low cost before the interaction.
- The answer must explain how the design distinguishes altruistic donors who seek contact from pressure-averse households that avoid contact.
- The answer must identify door-opening/contact and donation as separate outcomes.
- The answer must avoid claiming that a simple solicitation RCT identifies social pressure.

## Acceptable Alternative Designs

| design | conditions under which it is acceptable | supports what claim | cannot support what claim |
|---|---|---|---|
| Randomized advance notice plus randomized easy opt-out channel | Must observe contact/avoidance and giving; opt-out must be available before solicitor contact. | Can support mechanism evidence that avoidance behavior reveals social-pressure costs. | Cannot alone quantify welfare without stronger preference or structural assumptions. |
| Randomized solicitation with privately chosen appointment/decline option | Appointment/decline choice must be private and low-cost; outcomes must include both choice to engage and giving. | Can distinguish willingness to engage from giving under pressure. | Cannot identify social pressure if decline is costly or publicly observable in a way that creates new pressure. |
| Two-stage design randomizing solicitation intensity and private avoidance cost | Avoidance cost must vary exogenously and be measured before solicitation. | Can test whether lower avoidance cost reduces contact and small pressured gifts. | Cannot claim pure altruism if contact and giving are not separately measured. |

## Common Invalid Designs

| design or claim | why unacceptable | error label |
|---|---|---|
| Randomize only whether a solicitor visits and compare total donations. | It estimates solicitation effects but does not identify the mechanism behind giving. Evidence: N001. | Critical Design Omission |
| Use a flyer-only treatment and interpret lower total giving as lower altruism. | Flyer effects can mix seeking by altruistic households and avoidance by pressure-averse households. Evidence: N002. | Mechanism Confounding |
| Treat opt-out-related lower giving as proof that donors are less altruistic. | The opt-out channel is designed to lower unwanted interaction costs, so lower giving may reveal pressure avoidance. Evidence: N003. | Overclaim |
| Measure only donation amount and ignore door-opening/contact. | The mechanism requires separating avoidance/contact from conditional giving. Evidence: F014-F016. | Critical Design Omission |
| Use observational donor characteristics to infer altruism versus pressure. | Selection into contact and giving would be unaddressed. | Unsupported Claim |

## Claim-Evidence Expectations

| expected claim | required supporting evidence | claim type | confidence |
|---|---|---|---|
| Social pressure requires an avoidance or opt-out test. | L001, F019-F020 | mechanism | high |
| Donation amount alone cannot identify the mechanism. | N001-N002 | limitation | high |
| Door opening/contact is a key outcome. | F014, F020 | outcome | high |
| Exact inference details remain unresolved at this stage. | U001 | limitation | high |

## Scoring Notes

- Full-credit answer: Proposes a randomized mechanism design with advance notice or equivalent information, low-cost avoidance/opt-out, separate contact and donation outcomes, and explicit assumptions about interpreting avoidance as pressure-related.
- Partial-credit answer: Proposes a fundraising field experiment and mentions social pressure, but has only weak or incomplete mechanism separation.
- Critical omission: No avoidance, opt-out, or sorting channel.
- Automatic failure: Claims a simple solicitation RCT, OLS donor comparison, or donation-only outcome identifies altruism versus social pressure.
