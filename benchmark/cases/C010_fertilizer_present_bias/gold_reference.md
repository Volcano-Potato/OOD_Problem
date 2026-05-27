<!-- visibility: evaluator-only -->
<!-- do_not_include_in_agent_context: true -->
<!-- case_id: C010 -->

# Gold Reference: C010

## Hidden Answer Summary

This evaluator-only gold reference defines what a valid answer must handle for the seasonal-input timing case. A valid answer does not need to reproduce the original paper's exact intervention branding or theoretical language, but it must recognize that the key design question is not simply whether subsidies increase adoption. The design must separate early timing and acquisition-friction effects from larger later price subsidies, reminders, or static liquidity stories.

## Core Research Problem

- Research question: Why do producers underinvest in a profitable seasonal input, and do small early interventions raise adoption by reducing procrastination or present-bias rather than by acting as large subsidies? Evidence: F002, F028.
- Benchmark objective: Design an experiment that distinguishes timing and follow-through mechanisms from simple price sensitivity, transaction-cost reduction, or reminder effects. Evidence: F003-F004, F027-F031.
- Target mechanism or estimand: Effect of early small acquisition-cost reduction on actual seasonal adoption, relative to later offers and other comparison arms, with interpretation centered on procrastination or present-bias. Evidence: F017-F021, F022-F024.
- Treatment or exposure: Early small acquisition-cost reduction, later comparable offer, later larger subsidy, timing-choice option, or reminder-style intervention. Evidence: F017-F021.
- Outcome: Actual seasonal purchase or use of the input, not stated intention alone. Evidence: F022-F024.
- Unit of analysis: Producer-season or household-season adoption decision. Evidence: F005-F013.

## Data Structure

- Observation unit: Producer-season or household-season adoption outcome. Evidence: F005, F011-F013.
- Assignment level: Producer or household intervention arm. Evidence: F006, F025-F026.
- Outcome measurement level: Producer-level actual purchase or use within the relevant season. Evidence: F007, F013, F022.
- Time structure: Early post-income moment, later application window, and seasonal follow-up. Evidence: F009, F017-F020.
- Required comparison structure: Early small intervention versus later offer, with additional comparison arms such as reminders or larger later subsidy when available. Evidence: F018-F021, F027-F031.
- Current uncertainty: Exact inference details and whether reminder-arm discussion is mandatory for full credit are unresolved. Evidence: U001-U002.

## Original Identification Logic

The source design is a randomized field experiment with multiple arms that vary the timing and form of a small acquisition-cost reduction. The critical test compares an early small intervention shortly after income arrival with later offers that are similar or even more generous in monetary value. Stronger uptake in the early arm supports a procrastination or present-bias interpretation. Reminder and timing-choice arms further separate commitment-related mechanisms from pure information or static price sensitivity. Evidence: F025-F032.

## Linchpin Detail

- Linchpin 1: The design must compare an early small intervention with a later offer. Evidence: L001.
- Why it matters: This is what separates timing-based follow-through problems from generic willingness to respond to subsidies. Evidence: F027-F028.
- What fails without it: A single subsidy arm cannot distinguish present-bias or procrastination from static price sensitivity. Evidence: L001, N001.
- Linchpin 2: The later comparison arm must be economically comparable or stronger. Evidence: L002, F018, F021.
- Why it matters: If the later arm is weaker, the early effect could simply reflect larger incentives rather than timing. Evidence: L002, F030.
- Linchpin 3: Actual adoption must be observed rather than only stated intention. Evidence: L003, F022-F023.
- Why it matters: The mechanism is about failure to follow through on stated plans. Evidence: F023, N003.

## Must-Have Conditions

- The answer must recognize that the core mechanism test is about timing of a small intervention, not only price level.
- The answer must compare an early post-income intervention with a later intervention or later decision point.
- The answer must use actual adoption or use as the primary outcome rather than intentions alone.
- The answer must explain why a simple large subsidy design is insufficient for full mechanism separation.
- The answer must distinguish procrastination or present-bias from at least one alternative explanation such as transaction costs, reminders, or static liquidity.

## Acceptable Alternative Designs

| design | conditions under which it is acceptable | supports what claim | cannot support what claim |
|---|---|---|---|
| Randomized early-order coupon versus later-order coupon with equal face value | The economic value and hassle reduction must be comparable across timing arms; actual adoption must be observed. | Can identify whether earlier commitment timing raises adoption beyond a later identical offer. | Cannot isolate pure price elasticity if timing and value are still confounded. |
| Randomized early low-hassle ordering option versus later low-hassle ordering option plus no-offer control | Ordering hassle must be the manipulated margin and assignment must be randomized. | Can test whether early reduction in acquisition friction changes follow-through. | Cannot separately identify reminder-only effects without an additional reminder arm. |
| Factorial design with early small intervention, later larger subsidy, and reminder comparison | All arms must be randomized and actual use must be tracked. | Can distinguish timing-based mechanism from simple subsidy size and salience effects. | Cannot by itself prove structural present-bias without stronger modeling assumptions. |

## Common Invalid Designs

| design or claim | why unacceptable | error label |
|---|---|---|
| Randomize only a large later subsidy and infer procrastination or present-bias from higher adoption. | This does not separate timing from price magnitude. Evidence: N001, L001-L002. | Mechanism Confounding |
| Regress adoption on self-reported liquidity or stated intent and call the pattern causal evidence of present-bias. | Stated intention and liquidity reports do not provide exogenous variation in timing. Evidence: N002-N003. | Unsupported Claim |
| Treat reminder effects as equivalent to an early commitment-style intervention. | Reminder-only evidence addresses salience or forgetting, not the same mechanism as early acquisition timing. Evidence: N004, F029. | Overclaim |
| Use intention to adopt as the main outcome. | The design is about the gap between plans and realized behavior. Evidence: F023, L003. | Critical Design Omission |
| Conclude that heavy subsidies are the core answer without comparing early small interventions. | The benchmark asks whether timing and small acquisition-friction changes can outperform or match larger later incentives. Evidence: F021, F028. | Mis-specified Estimand |

## Claim-Evidence Expectations

| expected claim | required supporting evidence | claim type | confidence |
|---|---|---|---|
| Timing of the intervention is central to identification. | F017-F020, F027-F028, L001 | identification | high |
| A generic subsidy effect is not enough for mechanism separation. | F021, L002, N001 | limitation | high |
| Actual adoption or use must be measured. | F022-F023, L003 | measurement | high |
| Reminder-only explanations are weaker than timing-based explanations. | F020, F029, F031 | mechanism / limitation | medium |

## Scoring Notes

- Full-credit answer: Proposes a randomized timing-based design comparing an early small intervention with a later comparable offer, uses actual adoption or use as the outcome, and explicitly explains why this design tests procrastination or present-bias rather than simple subsidy demand.
- Partial-credit answer: Proposes a reasonable randomized adoption experiment and recognizes that timing matters, but does not clearly separate timing from subsidy size or does not use the correct behavioral outcome.
- Critical omission: No early-versus-late comparison or no actual adoption/use outcome.
- Automatic failure: Claims that a generic subsidy RCT, reminder intervention, or observational correlation between cash on hand and adoption identifies the mechanism.
