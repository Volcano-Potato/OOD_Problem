# Published Design Memo

## Research Question
Research question: Does in-person charitable giving reflect altruism/warm glow or social pressure from refusing a direct request? Evidence: F002.

## Target Estimand
Target mechanism or estimand: Mechanism separation between altruism/warm glow and social pressure; treatment effects of advance notice and low-cost avoidance on contact and donation behavior. Evidence: F003, F014-F016.

## Treatment And Outcomes
- Treatment or exposure: Baseline solicitation, advance notice, and advance notice plus low-cost opt-out/avoidance. Evidence: F010-F013.
- Outcome: Door opening/contact, donation probability, donation amount, and small-donation pattern. Evidence: F014-F016.
- Unit of analysis: Household solicitation/contact opportunity. Evidence: F005-F007.

## Identification Logic
The source design is a mechanism experiment embedded in a field experiment. Advance notice lets households seek or avoid contact, and adding a low-cost opt-out channel lowers the cost of avoiding an unwanted solicitation. Door-opening and giving responses to these avoidance options provide evidence about whether observed giving is driven by altruistic demand or by social pressure. Evidence: F017-F020.

## Key Data Structure
- Observation unit: Household contact opportunity. Evidence: F005.
- Assignment level: Household solicitation level. Evidence: F006.
- Outcome measurement level: Household interaction level. Evidence: F007.
- Time structure: Advance notice before a scheduled solicitation window. Evidence: F008.
- Required comparison structure: No-notice baseline versus advance notice, and advance notice versus advance notice with low-cost opt-out. Evidence: F018.
- Current uncertainty: Exact sample size, treatment counts, and inference details are not yet extracted, so gold scoring should not require exact standard-error formulas. Evidence: U001.

## Linchpin Conditions
- Linchpin: The design includes a low-cost avoidance or opt-out channel before the solicitation interaction. Evidence: L001.
- Why it matters: Avoidance behavior is direct evidence that some households prefer not to face the solicitation, which is essential for identifying pressure-induced giving. Evidence: L001, F019-F020.
- What fails without it: A generic randomized solicitation can estimate whether solicitation changes donations, but cannot distinguish altruism/warm glow from social pressure. Evidence: L001, N001.
- Secondary linchpin: Comparing advance notice alone with advance notice plus opt-out prevents interpreting all flyer effects as simple awareness or scheduling. Evidence: L002.
- The answer must separate donation effects from contact/avoidance behavior, not only report total giving.
- The answer must include some way for subjects to avoid the solicitation at low cost before the interaction.
- The answer must explain how the design distinguishes altruistic donors who seek contact from pressure-averse households that avoid contact.
- The answer must identify door-opening/contact and donation as separate outcomes.

## Defensibility Assessment
Linchpin: The design includes a low-cost avoidance or opt-out channel before the solicitation interaction. Evidence: L001. Why it matters: Avoidance behavior is direct evidence that some households prefer not to face the solicitation, which is essential for identifying pressure-induced giving. Evidence: L001, F019-F020. The answer must separate donation effects from contact/avoidance behavior, not only report total giving. The answer must include some way for subjects to avoid the solicitation at low cost before the interaction.

## Proposed Design
- Treatment or exposure: Baseline solicitation, advance notice, and advance notice plus low-cost opt-out/avoidance. Evidence: F010-F013.
- Outcome: Door opening/contact, donation probability, donation amount, and small-donation pattern. Evidence: F014-F016.
- Unit of analysis: Household solicitation/contact opportunity. Evidence: F005-F007.
- Required comparison structure: No-notice baseline versus advance notice, and advance notice versus advance notice with low-cost opt-out. Evidence: F018.
- Current uncertainty: Exact sample size, treatment counts, and inference details are not yet extracted, so gold scoring should not require exact standard-error formulas. Evidence: U001.
- The answer must separate donation effects from contact/avoidance behavior, not only report total giving.
- The answer must include some way for subjects to avoid the solicitation at low cost before the interaction.

## What Cannot Be Claimed Or Omitted
- Randomize only whether a solicitor visits and compare total donations. Why invalid: It estimates solicitation effects but does not identify the mechanism behind giving. Evidence: N001.
- Use a flyer-only treatment and interpret lower total giving as lower altruism. Why invalid: Flyer effects can mix seeking by altruistic households and avoidance by pressure-averse households. Evidence: N002.
- Treat opt-out-related lower giving as proof that donors are less altruistic. Why invalid: The opt-out channel is designed to lower unwanted interaction costs, so lower giving may reveal pressure avoidance. Evidence: N003.
- Measure only donation amount and ignore door-opening/contact. Why invalid: The mechanism requires separating avoidance/contact from conditional giving. Evidence: F014-F016.
