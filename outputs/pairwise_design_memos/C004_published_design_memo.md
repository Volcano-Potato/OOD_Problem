# Published Design Memo

## Research Question
Research question: What is the causal effect of paid search advertising on downstream sales, and how does that effect vary by prior user familiarity or activity? Evidence: F002, F022.

## Target Estimand
Target estimand: Incremental sales effect of paid search exposure or paid search availability for the relevant exposed or affected user population. Evidence: F013, F023-F028.

## Treatment And Outcomes
- Treatment or exposure: Paid search advertising active versus suspended for a focal query set or comparable ad-availability margin. Evidence: F012, F016-F017.
- Outcome: Downstream sales or purchases, with heterogeneity by prior recency/frequency or familiarity segment. Evidence: F013, F020, F022.
- Unit of analysis: Geographic-market by time sales observation, optionally segmented by prior user type. Evidence: F005-F010.

## Identification Logic
The source design is a large-scale field experiment that exogenously suspends paid search advertising in a set of matched geographic markets while comparable markets remain on. The core comparison is downstream sales in treated and control markets over time. This avoids using observed clicks or attributed conversions as the identifying variation. The source also studies heterogeneous effects by prior user activity and uses a navigational-query placebo benchmark to show that some apparently valuable paid search traffic is largely substitutive. Evidence: F023-F031.

## Key Data Structure
- Observation unit: Geographic-market by time sales outcome, potentially split by user-history segment. Evidence: F005, F010, F014.
- Assignment level: Geographic market or comparable grouped exposure cell controlled by the platform. Evidence: F006, F011.
- Outcome measurement level: Sales or purchase outcomes measured downstream from the advertising intervention. Evidence: F007, F020.
- Time structure: Pre/post campaign window with repeated observations across treated and control markets. Evidence: F009-F010.
- Required comparison structure: Treated markets versus matched or comparable control markets over time; not clicked versus unclicked users. Evidence: F024-F027, F031.
- Current uncertainty: Exact region counts, campaign duration, and whether full credit requires an explicit placebo benchmark are unresolved, so gold scoring should not require exact operational counts. Evidence: U001, U003.

## Linchpin Conditions
- Linchpin 1: Use exogenous ad-availability variation rather than observed clicks or attributed paid-search purchases. Evidence: L001.
- Why it matters: It breaks the link between search intent and observed paid-search activity. Evidence: F004, F026-F027.
- What fails without it: Click-based or attribution-based ROI comparisons confound user intent, prior familiarity, and treatment effects. Evidence: L001, N001-N002.
- Linchpin 2: Compare treated and control markets with pre/post structure or equivalent matched time controls. Evidence: L002, F031.
- The answer must state that observed clicks, click-through traffic, or attributed conversions are endogenous to search intent.
- The answer must introduce exogenous variation in ad availability or eligibility; observational matching alone is insufficient for full credit.
- The answer must use downstream sales or purchases as the main causal outcome, not clicks alone.
- The answer must include a market/time comparison structure or equivalent control for background trends.

## Defensibility Assessment
Linchpin 1: Use exogenous ad-availability variation rather than observed clicks or attributed paid-search purchases. Evidence: L001. Why it matters: It breaks the link between search intent and observed paid-search activity. Evidence: F004, F026-F027. The answer must state that observed clicks, click-through traffic, or attributed conversions are endogenous to search intent. The answer must introduce exogenous variation in ad availability or eligibility; observational matching alone is insufficient for full credit.

## Proposed Design
- Treatment or exposure: Paid search advertising active versus suspended for a focal query set or comparable ad-availability margin. Evidence: F012, F016-F017.
- Outcome: Downstream sales or purchases, with heterogeneity by prior recency/frequency or familiarity segment. Evidence: F013, F020, F022.
- Unit of analysis: Geographic-market by time sales observation, optionally segmented by prior user type. Evidence: F005-F010.
- Required comparison structure: Treated markets versus matched or comparable control markets over time; not clicked versus unclicked users. Evidence: F024-F027, F031.
- Current uncertainty: Exact region counts, campaign duration, and whether full credit requires an explicit placebo benchmark are unresolved, so gold scoring should not require exact operational counts. Evidence: U001, U003.
- The answer must state that observed clicks, click-through traffic, or attributed conversions are endogenous to search intent.
- The answer must introduce exogenous variation in ad availability or eligibility; observational matching alone is insufficient for full credit.

## What Cannot Be Claimed Or Omitted
- Compare users who clicked paid search ads with users who did not click and call the difference causal. Why invalid: Clicking is endogenous to intent and familiarity, so the groups differ even absent treatment. Evidence: N001, F026.
- Use attributed conversions or attributed sales as causal ROI. Why invalid: Many attributed purchases would have occurred through other channels, so attribution overstates incremental effects. Evidence: N002, F027.
- Compare sales before and after ad suspension in treated markets only. Why invalid: Market-level seasonality and time shocks can drive the difference. Evidence: N003, L002.
- Use observational controls for user intent and claim that resolves paid-search selection. Why invalid: Intent and channel substitution are not fully observed, so residual confounding remains. Evidence: F004, F015, L001.
