# Published Design Memo

## Research Question
Research question: What is the causal effect of in-store travel distance on unplanned spending, and can path-inducing interventions increase unplanned purchases? Evidence: F002, F028.

## Target Estimand
Target estimand: Incremental effect of longer in-store travel distance on trip-level unplanned spending. Evidence: F012-F013, F020-F028.

## Treatment And Outcomes
- Treatment or exposure: Actual path length or exogenously induced additional travel distance. Evidence: F017-F019.
- Outcome: Trip-level unplanned spending, with optional robustness on unplanned item counts. Evidence: F013, F020-F022.
- Unit of analysis: Individual shopping trip. Evidence: F005-F010.

## Identification Logic
The source combines an IV-style observational design with a randomized validation experiment. In the observational design, the key exposure of interest is actual route length, but this variable is endogenous because shoppers choose paths and may deviate when they encounter stimuli. The source addresses this by constructing a pre-trip reference path from the store layout and the shopper's planned basket. This route benchmark precedes actual spending and is used as an instrument for actual path length, while controlling for shopping mission and budget slack. The paper then complements this with a randomized far-versus-near coupon experiment that directly induces additional travel. Evidence: F023-F032.

## Key Data Structure
- Observation unit: Individual shopping trip. Evidence: F005, F009-F011.
- Assignment level: No natural assignment in the observational design; shopper-trip level randomization only in the validating promotion experiment. Evidence: F006, F019.
- Outcome measurement level: Trip-level spending and path measures. Evidence: F007, F020-F021.
- Time structure: Pre-trip basket declaration, in-trip path measurement, and post-checkout spending. Evidence: F009, F011.
- Required comparison structure: Either pre-trip route-based variation that precedes spending or a randomized farther-versus-nearer promotion design. Evidence: F024-F025.
- Current uncertainty: The gold should allow either a valid route-based IV or a clearly randomized path-inducing experiment as full-credit designs. Evidence: U001.

## Linchpin Conditions
- Linchpin 1: Observed path length cannot be treated as exogenous. Evidence: L001.
- Why it matters: Travel and unplanned purchasing are jointly generated during the trip. Evidence: F004, F017, F026.
- What fails without it: Naive path-length regressions confuse causation with endogenous wandering. Evidence: N001.
- Linchpin 2: The design needs path-inducing variation determined before or independently of in-trip spending. Evidence: L002.
- The answer must explicitly state that actual shopper route length is endogenous.
- The answer must create pre-trip or randomized variation in route length rather than relying on observed route length alone.
- The answer must use trip-level unplanned spending as the core outcome rather than generic store revenue.
- The answer must control for shopping mission, planned basket structure, or equivalent pre-trip demand conditions.

## Defensibility Assessment
Linchpin 1: Observed path length cannot be treated as exogenous. Evidence: L001. Why it matters: Travel and unplanned purchasing are jointly generated during the trip. Evidence: F004, F017, F026. The answer must explicitly state that actual shopper route length is endogenous. The answer must create pre-trip or randomized variation in route length rather than relying on observed route length alone.

## Proposed Design
- Treatment or exposure: Actual path length or exogenously induced additional travel distance. Evidence: F017-F019.
- Outcome: Trip-level unplanned spending, with optional robustness on unplanned item counts. Evidence: F013, F020-F022.
- Unit of analysis: Individual shopping trip. Evidence: F005-F010.
- Required comparison structure: Either pre-trip route-based variation that precedes spending or a randomized farther-versus-nearer promotion design. Evidence: F024-F025.
- Current uncertainty: The gold should allow either a valid route-based IV or a clearly randomized path-inducing experiment as full-credit designs. Evidence: U001.
- The answer must explicitly state that actual shopper route length is endogenous.
- The answer must create pre-trip or randomized variation in route length rather than relying on observed route length alone.

## What Cannot Be Claimed Or Omitted
- Regress unplanned spending on observed route length and interpret the coefficient causally. Why invalid: Route length is endogenous to omitted stimuli, simultaneity, and measurement error. Evidence: N001, L001.
- Use shopping time as the identifying exposure without defending why it isolates product exposure. Why invalid: Time in store is not the same as exposure to additional product areas. Evidence: N002, F027.
- Ignore planned basket size, mission, or budget slack. Why invalid: These variables affect both route construction and capacity for unplanned spending. Evidence: N003, L003.
- Claim that path-inducing promotions necessarily raise net store value or long-run welfare. Why invalid: Additional unplanned spending may borrow from planned or future purchases and may reduce shopping convenience. Evidence: N004, P013.
