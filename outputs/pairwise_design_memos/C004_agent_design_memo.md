# Agent Design Memo

## Research Question
What is the causal effect of making paid search available in a market on downstream purchase outcomes, and does this effect differ between users with low versus high prior activity with the firm? ---

## Target Estimand


## Treatment And Outcomes


## Identification Logic
The central challenge is confounding between paid-search availability and underlying market-level demand trends. Markets where the firm chose to maintain paid search may differ systematically from markets where it was turned off. If treated markets were growing faster before the campaign (or were selected because they showed stronger prior performance), then a naive post-period comparison of treated vs. untreated markets would attribute pre-existing trend differences to the treatment. Three specific threats: 1. Non-parallel pre-trends: Treated and untreated markets may have had different sales trajectories before the campaign, violating the core assumption needed for panel-based causal inference. 2. Time-varying confounders: Concurrent changes (local economic conditions, competitor actions, other marketing) that coincide with the campaign and differ across treatment-status groups. 3. Out

## Defensibility Assessment
Yes, credible causal identification is possible under the data structure provided, but its credibility is conditional on (a) the nature of the assignment mechanism and (b) whether pre-period outcomes evolve in parallel across treatment conditions. The panel structure with pre-period observations allows direct testing of parallel trends, which is the critical diagnostic. If parallel pre-trends hold, the design supports causal interpretation as an intent-to-treat effect of market-level paid-search availability. If parallel trends are rejected, the strongest defensible analysis becomes a descriptive decomposition of sales changes, not a causal claim. The credibility is not at the level of a randomized experiment (the assignment is "planned" but not described as random) and is weaker than a regression-discontinuity design. It sits in the space of a well-diagnosed panel-based design with expl

## Proposed Design
### Overview Compare the change in total downstream purchases from the pre-period to the campaign period between markets where paid search is available and markets where it is unavailable, controlling for market-specific time-invariant characteristics and common time effects. Estimate both aggregate and segment-specific effects. ### Step 1: Validate Comparability - Tabulate pre-period characteristics (average sales levels, trends, market size, segment composition) by treatment status. - Compute standardized differences; flag any covariate with a standardized difference exceeding 0.25 as potentially problematic. - Plot raw average sales trajectories for treated and untreated markets over the full observation window. Inspect visually for parallel movement in the pre-period. ### Step 2: Estimate Aggregate Treatment Effect Using the panel of market-by-time observations, estimate the effect of paid-search availability on total purchases, controlling for market fixed effects, time fixed effects, and optionally market-specific linear time trends. The coefficient on the interaction of treatment status and campaign-period indicator captures the average change in outcomes in treated markets beyond what would be predicted by their pre-period trajectory and common time shocks. ### Step 3: Es

## What Cannot Be Claimed
1. The effect of an individual clicking a paid link on that individual's purchase probability. The design identifies a market-level ITT, not an individual-level treatment effect. Users who click paid links in treated markets differ from users who do not in unobservable ways (search intent), so individual-level comparisons are not causal. 2. The return on ad spend (ROAS) in the platform-attribution sense. ROAS calculations typically divide attributed revenue by ad cost, but attributed revenue conflates incremental and cannibalized sales. The design can estimate incremental total sales, which should inform a true ROAS calculation, but requires cost data not described in the packet. 3. That the effect generalizes to markets outside the study. If the markets in the study are not a random sample of all markets the firm operates in, external validity is limited. The ATT applies to the study ma
