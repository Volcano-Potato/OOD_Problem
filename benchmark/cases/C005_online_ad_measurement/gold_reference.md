<!-- visibility: evaluator-only -->
<!-- do_not_include_in_agent_context: true -->
<!-- case_id: C005 -->

# Gold Reference: C005

## Hidden Answer Summary

This evaluator-only gold reference defines what a valid answer must handle for the online-advertising measurement case. A valid answer does not need to use the source paper's named method, but it must correct for endogenous exposure and construct a credible counterfactual for users who actually had the opportunity to see the focal ad.

## Core Research Problem

- Research question: How can advertisers estimate causal ad lift when actual ad exposure is selected by platform auctions and optimization? Evidence: F002.
- Benchmark objective: Design a measurement strategy comparing treated exposed users with control users who had comparable focal-ad exposure opportunity. Evidence: F003.
- Target estimand: Incremental ad effect on downstream conversions among users who would have been eligible or likely to receive the focal ad. Evidence: F014-F015.
- Treatment or exposure: Focal ad exposure generated within a randomized online advertising campaign. Evidence: F010-F012.
- Outcome: Conversions such as website visits, sign-ups, or purchases. Evidence: F014.
- Unit of analysis: Ad opportunity or impression linked to downstream user outcome. Evidence: F005-F007.

## Data Structure

- Observation unit: Ad opportunity/impression linked to user-level downstream outcomes. Evidence: F005.
- Assignment level: Randomized treatment assignment in an online ad campaign, with exact share/details unresolved. Evidence: F006, U001.
- Outcome measurement level: User conversion outcomes. Evidence: F007.
- Platform structure: Auctions and performance optimization determine realized exposure. Evidence: F009.
- Required exposure measure: Control users' would-be focal-ad opportunities must be logged or predicted. Evidence: F011-F012.
- Current uncertainty: Exact assignment share, outcome window, campaign details, and ITT partial-credit policy remain open. Evidence: U001-U002.

## Original Identification Logic

The source design uses randomized assignment plus platform-level exposure-opportunity logging. The key comparison is not all treated users versus all control users, and not observed exposed users versus observed unexposed users. It compares treatment users who see the focal ad with control users who would have had the focal ad opportunity under treatment assignment. Evidence: F017-F020.

## Linchpin Detail

- Linchpin: Identify control users with the same focal-ad exposure opportunity as treated exposed users. Evidence: L001.
- Why it matters: It constructs the relevant counterfactual for the users who actually saw the ad. Evidence: F018.
- What fails without it: Comparing exposed to all unexposed users confounds ad effects with purchase intent and platform selection. Evidence: F019, N001.
- Secondary linchpin: Account for platform optimization when defining controls. Evidence: L002.
- Implementation condition: Validate predicted exposure-opportunity assignment if it is not directly logged. Evidence: L003.

## Must-Have Conditions

- The design must address endogenous actual ad exposure.
- The design must distinguish randomized eligibility/assignment from realized exposure.
- The design must define a control group based on comparable exposure opportunity, not merely non-exposure.
- The design must measure downstream conversions consistently across treatment and control.
- The design must discuss platform optimization or targeting as a threat to PSA or naive holdout comparisons.

## Acceptable Alternative Designs

| design | conditions under which it is acceptable | supports what claim | cannot support what claim |
|---|---|---|---|
| Logged exposure-opportunity holdout design | Platform logs whether the focal ad would have been served to control users; treatment assignment is randomized. | Can estimate ad lift for users with focal-ad opportunity. | Cannot generalize to all platform users without additional assumptions. |
| Randomized ad eligibility with auction replay or simulated auction for controls | Simulation must include the focal ad and preserve platform decision rules; prediction quality must be validated. | Can estimate incremental conversions among likely exposed users. | Cannot support causal claims if prediction creates selected or imbalanced control users. |
| Clean randomized geo/time campaign shutdown | Markets or time cells must be comparable; spillovers and seasonality must be addressed. | Can estimate campaign-level ad lift. | Cannot identify exposed-user lift if exposure opportunity within cells remains unknown. |

## Common Invalid Designs

| design or claim | why unacceptable | error label |
|---|---|---|
| Compare users who saw ads with users who did not. | Exposed users may have higher purchase intent. Evidence: N001. | Endogenous Exposure Error |
| Use PSA controls without addressing platform optimization. | Optimizing algorithms can expose different user types to PSA and treatment ads. Evidence: N002. | Mis-citation |
| Use ITT over all randomized users and claim exposed-user lift. | ITT may be noisy and targets eligibility/assignment, not the exposed-user estimand. Evidence: N003, U002. | Overclaim |
| Treat clicks as proof of causal ad effectiveness. | Clicks or observed exposure can be selected by user intent and platform targeting. Evidence: F003-F004. | Unsupported Claim |
| Ignore prediction error in would-be exposure. | Mismatched predicted controls can introduce selection bias. Evidence: F016, L003. | Critical Design Omission |

## Claim-Evidence Expectations

| expected claim | required supporting evidence | claim type | confidence |
|---|---|---|---|
| Actual exposure is endogenous. | F004, F019, N001 | causal threat | high |
| Comparable exposure opportunity is the key control condition. | F011-F012, F018, L001 | identification | high |
| PSA controls can fail under platform optimization. | F020, L002, N002 | limitation | high |
| Prediction quality is a validity condition. | F016, L003 | assumption | high |

## Scoring Notes

- Full-credit answer: Proposes randomized ad assignment plus a control group defined by would-be focal-ad exposure opportunity; addresses optimization/targeting; states conversion outcomes and validation checks.
- Partial-credit answer: Proposes a clean randomized campaign-level ITT and acknowledges it estimates assignment/eligibility effects rather than exposed-user lift.
- Critical omission: No correction for endogenous realized exposure.
- Automatic failure: Exposed-versus-unexposed comparison with causal language, click regression as causal proof, or PSA control assumed valid without optimization discussion.
