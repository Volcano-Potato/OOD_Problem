<!-- visibility: evaluator-only -->
<!-- do_not_include_in_agent_context: true -->
<!-- case_id: C019 -->

# Gold Reference: C019

## Hidden Answer Summary

This evaluator-only gold reference defines what a valid answer must handle for the in-store travel-distance case. A strong answer does not need to recreate the exact route-construction algorithm from the source paper, but it must recognize that observed shopper path length is endogenous and that causal identification requires pre-trip route-based variation or a randomized path-inducing intervention.

## Core Research Problem

- Research question: What is the causal effect of in-store travel distance on unplanned spending, and can path-inducing interventions increase unplanned purchases? Evidence: F002, F028.
- Benchmark objective: Design a study that handles endogenous shopper paths rather than treating observed route length as exogenous. Evidence: F003-F004, F023-F026.
- Target estimand: Incremental effect of longer in-store travel distance on trip-level unplanned spending. Evidence: F012-F013, F020-F028.
- Treatment or exposure: Actual path length or exogenously induced additional travel distance. Evidence: F017-F019.
- Outcome: Trip-level unplanned spending, with optional robustness on unplanned item counts. Evidence: F013, F020-F022.
- Unit of analysis: Individual shopping trip. Evidence: F005-F010.

## Data Structure

- Observation unit: Individual shopping trip. Evidence: F005, F009-F011.
- Assignment level: No natural assignment in the observational design; shopper-trip level randomization only in the validating promotion experiment. Evidence: F006, F019.
- Outcome measurement level: Trip-level spending and path measures. Evidence: F007, F020-F021.
- Time structure: Pre-trip basket declaration, in-trip path measurement, and post-checkout spending. Evidence: F009, F011.
- Required comparison structure: Either pre-trip route-based variation that precedes spending or a randomized farther-versus-nearer promotion design. Evidence: F024-F025.
- Current uncertainty: The gold should allow either a valid route-based IV or a clearly randomized path-inducing experiment as full-credit designs. Evidence: U001.

## Original Identification Logic

The source combines an IV-style observational design with a randomized validation experiment. In the observational design, the key exposure of interest is actual route length, but this variable is endogenous because shoppers choose paths and may deviate when they encounter stimuli. The source addresses this by constructing a pre-trip reference path from the store layout and the shopper's planned basket. This route benchmark precedes actual spending and is used as an instrument for actual path length, while controlling for shopping mission and budget slack. The paper then complements this with a randomized far-versus-near coupon experiment that directly induces additional travel. Evidence: F023-F032.

## Linchpin Detail

- Linchpin 1: Observed path length cannot be treated as exogenous. Evidence: L001.
- Why it matters: Travel and unplanned purchasing are jointly generated during the trip. Evidence: F004, F017, F026.
- What fails without it: Naive path-length regressions confuse causation with endogenous wandering. Evidence: N001.
- Linchpin 2: The design needs path-inducing variation determined before or independently of in-trip spending. Evidence: L002.
- Why it matters: This is what breaks simultaneity and reversed-causality concerns. Evidence: F024-F025.
- What fails without it: A correlational route-spending analysis cannot isolate whether longer routes cause spending or spending causes longer routes. Evidence: N001.
- Linchpin 3: Planned-basket and budget controls are required because route benchmarks depend on shopping mission. Evidence: L003.
- Why it matters: Shoppers with different missions both travel differently and have different slack for unplanned purchases. Evidence: F014, F025.

## Must-Have Conditions

- The answer must explicitly state that actual shopper route length is endogenous.
- The answer must create pre-trip or randomized variation in route length rather than relying on observed route length alone.
- The answer must use trip-level unplanned spending as the core outcome rather than generic store revenue.
- The answer must control for shopping mission, planned basket structure, or equivalent pre-trip demand conditions.
- The answer must state what the design cannot say about net welfare or truly incremental long-run revenue without additional evidence.

## Acceptable Alternative Designs

| design | conditions under which it is acceptable | supports what claim | cannot support what claim |
|---|---|---|---|
| Route-based IV using a pre-trip reference path from planned baskets and store layout | The reference path must be determined before the trip and must affect spending only through actual route length after controlling for shopping mission and budget slack. | Can identify the causal effect of longer route exposure on unplanned spending. | Cannot directly identify longer-run revenue or customer-satisfaction effects. |
| Randomized farther-versus-nearer targeted promotion that induces additional travel | Assignment must be randomized across comparable shoppers, and outcome measurement must be checkout unplanned spending. | Can identify the causal effect of induced additional travel on unplanned spending for the affected shopping context. | Cannot necessarily generalize to all route-length variation in observational data. |
| Randomized store-layout or product-placement manipulation that exogenously changes path length | Layout changes must be exogenous to the focal shoppers and measured at checkout. | Can identify whether exogenously longer routes increase unplanned spending. | Cannot isolate specific mechanisms if layout changes also alter salience, congestion, or assortment. |

## Common Invalid Designs

| design or claim | why unacceptable | error label |
|---|---|---|
| Regress unplanned spending on observed route length and interpret the coefficient causally. | Route length is endogenous to omitted stimuli, simultaneity, and measurement error. Evidence: N001, L001. | Endogenous Exposure Error |
| Use shopping time as the identifying exposure without defending why it isolates product exposure. | Time in store is not the same as exposure to additional product areas. Evidence: N002, F027. | Weak Identification |
| Ignore planned basket size, mission, or budget slack. | These variables affect both route construction and capacity for unplanned spending. Evidence: N003, L003. | Selection |
| Claim that path-inducing promotions necessarily raise net store value or long-run welfare. | Additional unplanned spending may borrow from planned or future purchases and may reduce shopping convenience. Evidence: N004, P013. | Overclaim |
| Treat noisy route tracking as harmless. | Measurement error is one of the stated endogeneity channels. Evidence: F004, F021. | Measurement Error |

## Claim-Evidence Expectations

| expected claim | required supporting evidence | claim type | confidence |
|---|---|---|---|
| Actual route length is endogenous. | F004, F017, F026, L001 | limitation / identification | high |
| A pre-trip route benchmark or randomized path manipulation is needed for causal inference. | F024-F025, F032, L002 | identification | high |
| Planned basket and budget slack must be controlled. | F014, L003 | assumption / design | high |
| Longer route exposure may raise unplanned spending, but broader welfare or long-run incremental-revenue claims are weaker. | F028, P013 | limitation | medium |

## Scoring Notes

- Full-credit answer: Proposes either a valid pre-trip route-based IV or a clearly randomized path-inducing intervention, treats actual route length as endogenous, uses unplanned spending as the core outcome, and controls for shopping mission or budget slack.
- Partial-credit answer: Recognizes endogeneity and proposes a plausible experimental or quasi-experimental solution, but omits key pre-trip controls or mixes path exposure with broader store-stimulus changes.
- Critical omission: Fails to recognize path endogeneity or offers only a naive route-spending regression.
- Automatic failure: Claims causal effects from observed route length, shopping time alone, or path correlations without exogenous variation.
