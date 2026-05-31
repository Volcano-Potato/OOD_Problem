# Published Design Memo

## Research Question
Research question: How can advertisers estimate causal ad lift when actual ad exposure is selected by platform auctions and optimization? Evidence: F002.

## Target Estimand
Target estimand: Incremental ad effect on downstream conversions among users who would have been eligible or likely to receive the focal ad. Evidence: F014-F015.

## Treatment And Outcomes
- Treatment or exposure: Focal ad exposure generated within a randomized online advertising campaign. Evidence: F010-F012.
- Outcome: Conversions such as website visits, sign-ups, or purchases. Evidence: F014.
- Unit of analysis: Ad opportunity or impression linked to downstream user outcome. Evidence: F005-F007.

## Identification Logic
The source design uses randomized assignment plus platform-level exposure-opportunity logging. The key comparison is not all treated users versus all control users, and not observed exposed users versus observed unexposed users. It compares treatment users who see the focal ad with control users who would have had the focal ad opportunity under treatment assignment. Evidence: F017-F020.

## Key Data Structure
- Observation unit: Ad opportunity/impression linked to user-level downstream outcomes. Evidence: F005.
- Assignment level: Randomized treatment assignment in an online ad campaign, with exact share/details unresolved. Evidence: F006, U001.
- Outcome measurement level: User conversion outcomes. Evidence: F007.
- Platform structure: Auctions and performance optimization determine realized exposure. Evidence: F009.
- Required exposure measure: Control users' would-be focal-ad opportunities must be logged or predicted. Evidence: F011-F012.
- Current uncertainty: Exact assignment share, outcome window, campaign details, and ITT partial-credit policy remain open. Evidence: U001-U002.

## Linchpin Conditions
- Linchpin: Identify control users with the same focal-ad exposure opportunity as treated exposed users. Evidence: L001.
- Why it matters: It constructs the relevant counterfactual for the users who actually saw the ad. Evidence: F018.
- What fails without it: Comparing exposed to all unexposed users confounds ad effects with purchase intent and platform selection. Evidence: F019, N001.
- Secondary linchpin: Account for platform optimization when defining controls. Evidence: L002.
- The design must address endogenous actual ad exposure.
- The design must distinguish randomized eligibility/assignment from realized exposure.
- The design must define a control group based on comparable exposure opportunity, not merely non-exposure.
- The design must measure downstream conversions consistently across treatment and control.

## Defensibility Assessment
Linchpin: Identify control users with the same focal-ad exposure opportunity as treated exposed users. Evidence: L001. Why it matters: It constructs the relevant counterfactual for the users who actually saw the ad. Evidence: F018. The design must address endogenous actual ad exposure. The design must distinguish randomized eligibility/assignment from realized exposure.

## Proposed Design
- Treatment or exposure: Focal ad exposure generated within a randomized online advertising campaign. Evidence: F010-F012.
- Outcome: Conversions such as website visits, sign-ups, or purchases. Evidence: F014.
- Unit of analysis: Ad opportunity or impression linked to downstream user outcome. Evidence: F005-F007.
- Required exposure measure: Control users' would-be focal-ad opportunities must be logged or predicted. Evidence: F011-F012.
- Current uncertainty: Exact assignment share, outcome window, campaign details, and ITT partial-credit policy remain open. Evidence: U001-U002.
- The design must address endogenous actual ad exposure.
- The design must distinguish randomized eligibility/assignment from realized exposure.

## What Cannot Be Claimed Or Omitted
- Compare users who saw ads with users who did not. Why invalid: Exposed users may have higher purchase intent. Evidence: N001.
- Use PSA controls without addressing platform optimization. Why invalid: Optimizing algorithms can expose different user types to PSA and treatment ads. Evidence: N002.
- Use ITT over all randomized users and claim exposed-user lift. Why invalid: ITT may be noisy and targets eligibility/assignment, not the exposed-user estimand. Evidence: N003, U002.
- Treat clicks as proof of causal ad effectiveness. Why invalid: Clicks or observed exposure can be selected by user intent and platform targeting. Evidence: F003-F004.
