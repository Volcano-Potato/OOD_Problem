<!-- visibility: evaluator-only -->
<!-- do_not_include_in_agent_context: true -->
<!-- case_id: C004 -->

# Gold Reference: C004

## Hidden Answer Summary

This evaluator-only gold reference defines what a valid answer must handle for the paid-search effectiveness case. A valid answer does not need to reproduce the original paper's exact query labels or firm-specific implementation, but it must break the link between user intent and observed paid-search activity by using exogenous ad-availability variation and downstream sales outcomes.

## Core Research Problem

- Research question: What is the causal effect of paid search advertising on downstream sales, and how does that effect vary by prior user familiarity or activity? Evidence: F002, F022.
- Benchmark objective: Design a measurement strategy that handles search-intent endogeneity and heterogeneous treatment effects, rather than treating clicks or attributed sales as causal ROI. Evidence: F003-F004.
- Target estimand: Incremental sales effect of paid search exposure or paid search availability for the relevant exposed or affected user population. Evidence: F013, F023-F028.
- Treatment or exposure: Paid search advertising active versus suspended for a focal query set or comparable ad-availability margin. Evidence: F012, F016-F017.
- Outcome: Downstream sales or purchases, with heterogeneity by prior recency/frequency or familiarity segment. Evidence: F013, F020, F022.
- Unit of analysis: Geographic-market by time sales observation, optionally segmented by prior user type. Evidence: F005-F010.

## Data Structure

- Observation unit: Geographic-market by time sales outcome, potentially split by user-history segment. Evidence: F005, F010, F014.
- Assignment level: Geographic market or comparable grouped exposure cell controlled by the platform. Evidence: F006, F011.
- Outcome measurement level: Sales or purchase outcomes measured downstream from the advertising intervention. Evidence: F007, F020.
- Time structure: Pre/post campaign window with repeated observations across treated and control markets. Evidence: F009-F010.
- Required comparison structure: Treated markets versus matched or comparable control markets over time; not clicked versus unclicked users. Evidence: F024-F027, F031.
- Current uncertainty: Exact region counts, campaign duration, and whether full credit requires an explicit placebo benchmark are unresolved, so gold scoring should not require exact operational counts. Evidence: U001, U003.

## Original Identification Logic

The source design is a large-scale field experiment that exogenously suspends paid search advertising in a set of matched geographic markets while comparable markets remain on. The core comparison is downstream sales in treated and control markets over time. This avoids using observed clicks or attributed conversions as the identifying variation. The source also studies heterogeneous effects by prior user activity and uses a navigational-query placebo benchmark to show that some apparently valuable paid search traffic is largely substitutive. Evidence: F023-F031.

## Linchpin Detail

- Linchpin 1: Use exogenous ad-availability variation rather than observed clicks or attributed paid-search purchases. Evidence: L001.
- Why it matters: It breaks the link between search intent and observed paid-search activity. Evidence: F004, F026-F027.
- What fails without it: Click-based or attribution-based ROI comparisons confound user intent, prior familiarity, and treatment effects. Evidence: L001, N001-N002.
- Linchpin 2: Compare treated and control markets with pre/post structure or equivalent matched time controls. Evidence: L002, F031.
- Why it matters: Advertising effects are small relative to background seasonality and market-level demand variation. Evidence: L002, F031.
- Linchpin 3: Preserve heterogeneity by prior activity or familiarity if the answer claims paid search is ineffective on average. Evidence: L003, F019, F022.
- Why it matters: Near-zero average effects can mask positive effects for less active or less familiar users. Evidence: L003, F028.

## Must-Have Conditions

- The answer must state that observed clicks, click-through traffic, or attributed conversions are endogenous to search intent.
- The answer must introduce exogenous variation in ad availability or eligibility; observational matching alone is insufficient for full credit.
- The answer must use downstream sales or purchases as the main causal outcome, not clicks alone.
- The answer must include a market/time comparison structure or equivalent control for background trends.
- The answer must not infer "paid search has no effect" from an average effect alone without discussing heterogeneity if segmented user-history information is available.

## Acceptable Alternative Designs

| design | conditions under which it is acceptable | supports what claim | cannot support what claim |
|---|---|---|---|
| Randomized market-level ad suspension with matched untreated markets | Ad availability must be randomized or administratively assigned exogenously; downstream sales must be observed consistently across markets and time. | Can identify campaign-level incremental sales effects of paid search. | Cannot isolate user-segment heterogeneity if user-history segmentation is unavailable. |
| Randomized switchback design that alternates paid-search availability across markets or time cells | Switchback timing must be exogenous, demand seasonality must be controlled, and spillovers across adjacent cells must be limited. | Can identify short-run causal effects of ad availability on sales. | Cannot support long-run equilibrium claims without longer horizons. |
| Randomized eligibility or bidding suspension for a subset of comparable query-market cells with downstream conversion tracking | Eligibility variation must be exogenous and outcome measurement must be downstream purchases rather than clicks. | Can identify incremental paid-search value for the affected query or user segment. | Cannot support population-wide ROI claims if the affected cells are highly selected. |

## Common Invalid Designs

| design or claim | why unacceptable | error label |
|---|---|---|
| Compare users who clicked paid search ads with users who did not click and call the difference causal. | Clicking is endogenous to intent and familiarity, so the groups differ even absent treatment. Evidence: N001, F026. | Endogenous Exposure Error |
| Use attributed conversions or attributed sales as causal ROI. | Many attributed purchases would have occurred through other channels, so attribution overstates incremental effects. Evidence: N002, F027. | Unsupported Claim |
| Compare sales before and after ad suspension in treated markets only. | Market-level seasonality and time shocks can drive the difference. Evidence: N003, L002. | Timing Endogeneity |
| Use observational controls for user intent and claim that resolves paid-search selection. | Intent and channel substitution are not fully observed, so residual confounding remains. Evidence: F004, F015, L001. | Weak Identification |
| Report only the pooled average effect and conclude ads are uniformly ineffective. | The main substantive lesson may depend on heterogeneity by prior activity or familiarity. Evidence: N004, L003. | Overclaim |

## Claim-Evidence Expectations

| expected claim | required supporting evidence | claim type | confidence |
|---|---|---|---|
| Clicks and attributed conversions are not valid causal estimands by themselves. | F004, F021, F026-F027 | limitation | high |
| Exogenous ad-availability variation is the core identification requirement. | F023-F025, L001 | identification | high |
| Downstream sales, not click activity, should anchor the main outcome. | F013, F020 | measurement | high |
| Heterogeneity by prior familiarity or activity matters for interpretation of average effects. | F019, F022, F028, L003 | mechanism / limitation | medium |

## Scoring Notes

- Full-credit answer: Proposes exogenous ad-availability variation, a credible market/time comparison structure, downstream sales outcomes, and explicit recognition that average effects can mask heterogeneity by prior familiarity or activity.
- Partial-credit answer: Proposes a credible field experiment or geo/time shutdown design and recognizes click-based ROI is invalid, but omits heterogeneity or gives only limited discussion of substitution/placebo logic.
- Critical omission: No exogenous ad-availability variation, or no downstream sales outcome beyond clicks/attribution.
- Automatic failure: Claims causal paid-search ROI from clicked-versus-unclicked comparisons, attributed sales, or treated-market before/after comparisons alone.
