# Raw Agent Run Log

- `run_id`: RUN_20260527_223351_08_openclaw_deepseekv4pro_isolated
- `case_id`: C004
- `variant_id`: level2
- `level`: level2
- `agent_name`: openclaw
- `agent_id`: benchmark_isolated
- `model`: deepseek-v4-pro
- `model_provider`: deepseek
- `openclaw_build_or_version`: 2026.5.5
- `channel`: cli
- `temperature`: not_supported
- `top_p`: not_supported
- `max_tokens`: not_supported
- `seed`: not_supported
- `tools_enabled`: locally_isolated_remote_tool_enabled
- `closed_book`: false
- `timestamp`: 2026-05-27T22:33:51+0800
- `input_file`: benchmark/cases/C004_paid_search_effectiveness/agent_task_level2.md
- `system_prompt_summary`: workspace=/Users/jiangcanxiang/OpenClawBenchmarkIsolated; thinking=high; actual_tool_use=none; agent=benchmark_isolated
- `contamination_status`: unknown
- `contamination_reason`: pending manual content review; actual tool use=none
- `status`: success

## Raw Agent Output

# Research Design: Causal Effect of Paid Search Availability on Downstream Purchases

---

## 1. Executive Summary

This design proposes estimating the causal effect of market-level paid-search availability on downstream purchases using a panel of comparable markets observed before and during a campaign window in which paid search availability varies across markets. The core empirical challenge is that paid-search clicks and attributed conversions are mechanically correlated with underlying user intent: users who click paid links are already searching for the firm, so naive comparisons between clickers and non-clickers are uninformative about causation. By exploiting market-level variation in whether paid search is available—rather than variation in who clicks—the design sidesteps individual-level selection into ad exposure. The analysis leverages pre-period sales histories to control for market-specific demand trends and uses user-history segments to assess whether effects concentrate among less familiar users (demand creation) or already-active users (channel substitution). The main threat to validity is whether the markets with and without paid-search availability would have followed parallel sales trajectories absent the intervention; the design includes explicit diagnostics for this assumption. Results are interpreted as intent-to-treat effects of making paid search available in a market, not as the effect of an individual clicking a paid link.

---

## 2. Research Question

What is the causal effect of making paid search available in a market on downstream purchase outcomes, and does this effect differ between users with low versus high prior activity with the firm?

---

## 3. Target Estimand

**Primary estimand:** The average treatment effect on the treated markets (ATT) of paid-search availability on total downstream purchases, defined as:

> The difference between the average downstream purchase outcome in markets where paid search is available during the campaign window and the average outcome those same markets would have experienced had paid search been unavailable, conditional on pre-period sales histories and observable market characteristics.

Because treatment is assigned at the market level but users within treated markets may or may not see, click, or act on paid placements, this is an intent-to-treat (ITT) estimand: the effect of *offering* paid search in a market, not the effect of *receiving* a paid click.

**Secondary estimands:**

- The ATT of paid-search availability on purchases from users in the low-prior-activity segment.
- The ATT of paid-search availability on purchases from users in the high-prior-activity segment.
- The difference between these two segment-specific ATTs.

If market-level assignment was plausibly as-if random (conditional on observables), the ATT generalizes to the average treatment effect (ATE) across all markets in the study. Without evidence of random assignment, the design targets the ATT and limits extrapolation to untreated markets.

---

## 4. Treatment/Exposure and Main Outcomes

### Treatment Variable

- **Primary:** A binary indicator \( D_{m} = 1 \) if paid search is available in market \( m \) during the campaign window, and \( D_{m} = 0 \) otherwise.
- **Secondary (if observed):** Continuous or categorical measures of paid-search intensity or campaign duration in each treated market, useful for dose-response analyses.

### Main Outcome Variables

- **Primary:** Total downstream purchases (or sales revenue, or order counts) in market \( m \) during time period \( t \), denoted \( Y_{mt} \). This must be *total* sales recorded through the firm's sales-recording system, not sales attributed by the ad platform to paid clicks. Using attributed conversions as the outcome would mechanically inflate the treatment effect estimate.

- **Secondary:** Segment-specific purchases, \( Y_{mt}^{g} \), for user-history segment \( g \) (e.g., low-activity vs. high-activity users), measured over the same market-by-time structure.

### Critical Measurement Distinction

The outcome must capture all purchases, regardless of acquisition channel. If the outcome were limited to purchases *attributed* to paid search clicks, the analysis would be circular: treated markets would mechanically show more attributed conversions because paid search is available to attribute. The estimand of interest is whether total sales rise, not whether the attribution channel shifts.

---

## 5. Data Structure Summary

| Dimension | Description |
|---|---|
| **Unit** | Market \( m \) × time period \( t \), with optional split by user-history segment \( g \) |
| **Time** | Pre-period (multiple periods before campaign) + campaign period (multiple periods during campaign) |
| **Markets** | Multiple comparable market areas, all served by a common sales-recording system |
| **Treatment** | Binary: paid search available (\( D_m = 1 \)) or unavailable (\( D_m = 0 \)) in market \( m \) during campaign |
| **Assignment** | Market-level; exact mechanism unspecified but described as "planned market-level variation" |
| **Outcomes** | Total purchases/sales per market-period; segment-specific purchases |
| **Covariates** | Pre-period sales histories, market size, seasonality indicators, segment composition |
| **Panel structure** | Balanced or nearly balanced panel with market and time dimensions |
| **Segments** | Defined by pre-period user familiarity, recency, or frequency; fixed before the campaign |

The panel structure is central to identification: it allows within-market comparisons over time (absorbing time-invariant market heterogeneity) and between-market comparisons at each time point (absorbing common time shocks).

---

## 6. Relevant Causal Mechanisms

The data structure and research design allow distinguishing four distinct mechanisms:

**Mechanism A — Demand creation (informative/advertising effect):** Paid search makes less familiar users aware of the firm's offering, leading to purchases that would not have occurred otherwise. Empirically, this predicts a positive treatment effect concentrated in the low-prior-activity segment *and* an increase in *total* (not just search-attributed) sales.

**Mechanism B — Channel substitution (interception of existing intent):** Already-active users who would have reached the firm through unpaid search, direct navigation, or other channels instead click the paid link. Empirically, this predicts a positive effect on *search-attributed* purchases but a null or near-null effect on *total* purchases, and any observed effect would concentrate in the high-prior-activity segment.

**Mechanism C — Attribution inflation:** Even if total sales are unchanged, the firm's attribution system may credit paid search for purchases that the user would have made through another channel. This is a measurement artifact, not a causal effect. It is diagnosed by comparing results using total-sales outcomes versus search-attributed-sales outcomes.

**Mechanism D — Heterogeneous effects by prior activity:** The average treatment effect may obscure offsetting patterns: demand creation among less active users and pure substitution among active users. Segment-level analysis is designed to detect this.

---

## 7. Main Identification Challenge

The central challenge is **confounding between paid-search availability and underlying market-level demand trends.** Markets where the firm chose to maintain paid search may differ systematically from markets where it was turned off. If treated markets were growing faster before the campaign (or were selected because they showed stronger prior performance), then a naive post-period comparison of treated vs. untreated markets would attribute pre-existing trend differences to the treatment.

Three specific threats:

1. **Non-parallel pre-trends:** Treated and untreated markets may have had different sales trajectories before the campaign, violating the core assumption needed for panel-based causal inference.

2. **Time-varying confounders:** Concurrent changes (local economic conditions, competitor actions, other marketing) that coincide with the campaign and differ across treatment-status groups.

3. **Outcome measurement contamination:** If the outcome inadvertently captures only search-attributed sales, the design conflates channel shifting with incremental demand.

---

## 8. Whether Credible Causal Identification Is Possible

**Yes, credible causal identification is possible under the data structure provided, but its credibility is conditional on (a) the nature of the assignment mechanism and (b) whether pre-period outcomes evolve in parallel across treatment conditions.** The panel structure with pre-period observations allows direct testing of parallel trends, which is the critical diagnostic. If parallel pre-trends hold, the design supports causal interpretation as an intent-to-treat effect of market-level paid-search availability. If parallel trends are rejected, the strongest defensible analysis becomes a descriptive decomposition of sales changes, not a causal claim.

The credibility is not at the level of a randomized experiment (the assignment is "planned" but not described as random) and is weaker than a regression-discontinuity design. It sits in the space of a well-diagnosed panel-based design with explicit pre-trend checking.

---

## 9. Proposed Empirical Design

### Overview

Compare the change in total downstream purchases from the pre-period to the campaign period between markets where paid search is available and markets where it is unavailable, controlling for market-specific time-invariant characteristics and common time effects. Estimate both aggregate and segment-specific effects.

### Step 1: Validate Comparability

- Tabulate pre-period characteristics (average sales levels, trends, market size, segment composition) by treatment status.
- Compute standardized differences; flag any covariate with a standardized difference exceeding 0.25 as potentially problematic.
- Plot raw average sales trajectories for treated and untreated markets over the full observation window. Inspect visually for parallel movement in the pre-period.

### Step 2: Estimate Aggregate Treatment Effect

Using the panel of market-by-time observations, estimate the effect of paid-search availability on total purchases, controlling for market fixed effects, time fixed effects, and optionally market-specific linear time trends. The coefficient on the interaction of treatment status and campaign-period indicator captures the average change in outcomes in treated markets beyond what would be predicted by their pre-period trajectory and common time shocks.

### Step 3: Estimate Segment-Specific Effects

Repeat the estimation separately for each user-history segment (e.g., low-activity and high-activity users). Compare the segment-specific treatment effects. If the effect is positive and statistically significant in the low-activity segment but close to zero in the high-activity segment, this supports demand creation (Mechanism A). If the pattern is reversed or both segments show positive effects on search-attributed outcomes but null effects on total outcomes, this supports channel substitution (Mechanism B).

### Step 4: Channel-Level Decomposition (If Data Permit)

If outcomes are available disaggregated by acquisition channel (paid search, unpaid search, direct, other), estimate treatment effects on each channel separately. A finding of positive effects on paid-search-channel sales but offsetting negative effects on unpaid/direct channels would directly evidence substitution.

### Step 5: Diagnostic and Robustness Checks

Conduct the battery of checks described in Section 13.

---

## 10. Why the Design Is Valid (Conditional on Assumptions)

The design addresses the main identification challenge through four features:

1. **Market-level treatment assignment avoids individual selection bias.** Users do not choose whether paid search is available in their market; the firm does. This breaks the direct link between individual search intent and treatment status that would invalidate a user-level comparison of clickers vs. non-clickers.

2. **Pre-period data allow testing of the central assumption.** The panel structure with multiple pre-period observations makes it possible to check whether treated and untreated markets were on parallel trajectories before the campaign. This is not an untestable assumption—it is directly testable.

3. **Total-sales outcomes avoid mechanical attribution bias.** By measuring all downstream purchases rather than search-attributed conversions, the design does not confound channel shifting with incremental demand. Even if users substitute paid links for unpaid links, total sales would not rise unless there is genuine demand creation.

4. **Market fixed effects absorb all time-invariant differences** between markets (size, average demand, segment composition, permanent geographic factors). Time fixed effects absorb common shocks affecting all markets in a given period (seasonality, macro conditions). The treatment effect is identified from differential *within-market changes* over time across treatment conditions.

The segment-level analysis further distinguishes mechanisms: if paid search primarily intercepts existing demand from active users, the segment-specific effects will reveal this pattern even when the aggregate estimate is ambiguous.

---

## 11. Required Assumptions

### Assumption 1: Parallel Trends in the Absence of Treatment

In the absence of paid-search availability, treated markets would have experienced the same change in total purchases from the pre-period to the campaign period as untreated markets, conditional on market fixed effects and time fixed effects. This is the core identifying assumption. It is testable in the pre-period (see Section 13).

### Assumption 2: No Anticipation Effects

Markets did not adjust behavior in the pre-period in anticipation of paid search becoming available or unavailable. If assignment was planned and announced, users or local managers might have shifted behavior before the campaign started. The pre-period should be defined to end before any such anticipation could occur.

### Assumption 3: Stable Unit Treatment Value (No Cross-Market Spillovers)

Purchases recorded in untreated markets are not materially affected by paid-search availability in treated markets. This could be violated if, for example, users in untreated markets travel to treated markets, or if the firm's overall brand awareness rises because of advertising in treated markets and spills over to untreated markets. The geographic scope of markets should be large enough to make cross-market shopping unlikely.

### Assumption 4: No Concurrent Confounding Interventions

No other marketing or operational changes were introduced simultaneously with the paid-search variation in a way that correlates with treatment status across markets.

### Assumption 5: Segment Assignment Is Pre-Determined

User-history segments are defined using pre-period data only. If segments are defined using campaign-period behavior, they are themselves affected by treatment (bad control problem), and the segment-level analysis would be biased.

### Assumption 6: Outcome Measurement Is Complete

Total purchases are recorded consistently across markets and time periods. Differential measurement error or reporting lags across treatment conditions would bias estimates.

### Assumption 7: Treatment Is Well-Defined and Stable

Paid-search availability in a treated market means paid placements were consistently present throughout the campaign window. Partial or intermittent availability would attenuate the ITT estimate toward zero.

---

## 12. Statistical Model or Analysis Equation

### Primary Specification: Aggregate Effect

\[
Y_{mt} = \alpha_m + \lambda_t + \delta \cdot (D_m \times \text{Post}_t) + \varepsilon_{mt}
\]

Where:
- \( Y_{mt} \): total purchases in market \( m \) during period \( t \)
- \( \alpha_m \): market fixed effects
- \( \lambda_t \): time fixed effects
- \( D_m \): indicator for paid-search availability in market \( m \)
- \( \text{Post}_t \): indicator for campaign-period observations
- \( \delta \): coefficient of interest — the average ITT effect of paid-search availability
- \( \varepsilon_{mt} \): error term, clustered at the market level

### Specification with Market-Specific Trends

\[
Y_{mt} = \alpha_m + \lambda_t + \delta \cdot (D_m \times \text{Post}_t) + \gamma_m \cdot t + \varepsilon_{mt}
\]

Where \( \gamma_m \cdot t \) allows each market to have its own linear time trend. This relaxes Assumption 1 by requiring only that *deviations from market-specific linear trends* are parallel, rather than levels. However, with a small number of pre-periods, this specification can absorb substantial variation and reduce precision; it is reported as a robustness check rather than the primary model.

### Segment-Specific Specification

\[
Y_{mt}^{g} = \alpha_m^{g} + \lambda_t^{g} + \delta_g \cdot (D_m \times \text{Post}_t) + \varepsilon_{mt}^{g}
\]

Estimated separately for each segment \( g \in \{\text{low-activity}, \text{high-activity}\} \). The parameters \( \delta_{\text{low}} \) and \( \delta_{\text{high}} \) capture segment-specific treatment effects. The difference \( \delta_{\text{low}} - \delta_{\text{high}} \) is tested for statistical significance.

### Event-Study Specification (for Pre-Trend Visualization)

\[
Y_{mt} = \alpha_m + \lambda_t + \sum_{k \neq -1} \beta_k \cdot (D_m \times \mathbf{1}[t = k]) + \varepsilon_{mt}
\]

Where \( k \) indexes time periods relative to the campaign start, with \( k = -1 \) as the reference period. The coefficients \( \beta_k \) for \( k < 0 \) test for differential pre-trends; coefficients for \( k \geq 0 \) trace out the dynamic treatment effect over the campaign window.

### Inference

Standard errors are clustered at the market level to account for serial correlation within markets over time. With a small number of markets, wild cluster bootstrap or randomization inference p-values supplement asymptotic inference.

---

## 13. Robustness, Placebo, Falsification, and Diagnostic Checks

### 13.1 Pre-Trend Test (Critical)

Estimate the event-study specification. The null hypothesis is \( \beta_k = 0 \) for all pre-period leads \( k < 0 \). Joint F-test of all pre-period coefficients. Visual inspection of the event-study plot: pre-period coefficients should be close to zero with no visible trend. Any systematic pre-trend (rising or falling coefficients before the campaign) undermines the design's credibility.

### 13.2 Placebo Treatment Timing

Shift the hypothetical campaign start to an earlier date within the pre-period and re-estimate the primary specification using only pre-period data with a false post-period. A significant "effect" of this placebo treatment indicates that treated and untreated markets were already diverging before the actual campaign, violating Assumption 1.

### 13.3 Placebo Outcome

Replace the outcome with a variable that should not be affected by paid-search availability—ideally a sales category unrelated to the firm's search-advertised products, or a lead indicator measured before search activity could influence purchases. A null effect on the placebo outcome supports the design.

### 13.4 Leave-One-Out Market Analysis

Re-estimate the primary specification dropping one market at a time. This assesses whether results are driven by a single influential market rather than a systematic pattern.

### 13.5 Balance Checks on Pre-Period Characteristics

Regress treatment status on pre-period market characteristics (average sales, trend, size, segment composition). If pre-period characteristics strongly predict treatment status, the design relies more heavily on the parallel-trends assumption holding conditional on those characteristics. Report the R-squared from this regression to quantify selection on observables.

### 13.6 Sensitivity to Alternative Outcome Definitions

Re-estimate using:
- Log-transformed sales (to capture proportional effects)
- Sales per capita (if market population data are available)
- Order counts rather than revenue (to distinguish price vs. quantity effects)

### 13.7 Segment Stability Check

Verify that segment composition is stable across treatment conditions in the pre-period. If treated markets have systematically different segment mixes at baseline, segment-level effects may reflect composition rather than heterogeneous treatment effects. If segment composition differs, re-weight or control for baseline composition.

### 13.8 Total vs. Attributed Outcome Comparison

If search-attributed purchase data are available, estimate the treatment effect on both total purchases and search-attributed purchases. The difference between these estimates quantifies the attribution inflation (Mechanism C). If the effect on total purchases is zero but the effect on attributed purchases is positive and large, the apparent campaign performance is entirely attribution artifact.

---

## 14. Heterogeneity Analysis

### 14.1 Primary: By Pre-Period User Activity

Define segments using pre-period data only (before the campaign window):

- **Low-activity segment:** Users with no purchases, one purchase, or purchases only in the distant past (e.g., bottom tercile of recency-frequency) during the pre-period.
- **High-activity segment:** Users with frequent or recent purchases during the pre-period.

Estimate the segment-specific specifications from Section 12. Interpret the pattern:

| Low-activity effect | High-activity effect | Interpretation |
|---|---|---|
| \( \delta_{\text{low}} > 0 \) | \( \delta_{\text{high}} \approx 0 \) | Demand creation dominates |
| \( \delta_{\text{low}} \approx 0 \) | \( \delta_{\text{high}} > 0 \) | Channel substitution; active users shift routes |
| \( \delta_{\text{low}} > 0 \) | \( \delta_{\text{high}} > 0 \) | Both mechanisms operate |
| \( \delta_{\text{low}} \approx 0 \) | \( \delta_{\text{high}} \approx 0 \) | No detectable effect on total sales |

### 14.2 Secondary: By Market Characteristics

If market-level characteristics are available, explore whether treatment effects vary by:
- Market size (paid search may matter more in larger, more competitive markets or in smaller markets with less organic visibility)
- Baseline share of low-activity users (effects may be larger where the addressable segment is larger)
- Competitive intensity (if measurable)

These are exploratory and should be clearly labeled as such.

### 14.3 Caution on Segment-Level Inference

Segment-specific outcomes are not independently varying across segments within a market—they sum to the market total. Standard errors should account for this dependence, and joint testing (e.g., seemingly unrelated regression) may be appropriate. With a small number of markets, formal heterogeneity testing has limited power; qualitative patterns in point estimates may be as informative as formal significance tests.

---

## 15. Measurement, Compliance, Missingness, Spillover, and Implementation Limits

### 15.1 Compliance and Take-Up

Market-level ad availability is an *offer* of treatment, not individual exposure. Within treated markets, some users will not see paid placements (e.g., they use ad blockers, skip ads, or never search for relevant queries). The ITT estimand incorporates this non-exposure and is therefore a lower bound on the effect of *actual exposure* among compliers. Without individual-level exposure data, the treatment-on-the-treated effect cannot be identified without additional assumptions (e.g., monotonicity and an instrument, which are not supported by the data structure as described).

### 15.2 Spillover and Interference

Several spillover channels are possible:

- **Cross-channel substitution within market:** Users in treated markets substitute paid clicks for unpaid clicks. The design addresses this by using total sales as the outcome, but it cannot separately quantify how much paid-search-attributed sales cannibalize unpaid-search sales without channel-disaggregated outcomes.
- **Cross-market spillover:** Users near market borders may search from an untreated market but purchase in a treated market (or vice versa). If market boundaries are porous, the treatment/control distinction is blurred. Geographic buffering or excluding border areas can mitigate this if the data permit.
- **General equilibrium effects:** If paid search in treated markets bids up keyword prices or affects organic ranking across all markets, untreated markets are partially treated. This is difficult to detect without cost or ranking data.

### 15.3 Missingness

- **Segment classification:** Some users may not be classifiable into activity segments (e.g., new users with no pre-period history). These users should be analyzed as a separate category or excluded from segment-specific analyses with transparent reporting.
- **Cross-channel tracking:** If the firm cannot link a purchase back to the acquisition channel, some outcomes are unclassified. Differential missingness by treatment status would bias estimates.

### 15.4 Repeated Exposure

Users in treated markets face repeated search opportunities during the campaign. The design estimates the cumulative effect of sustained availability, not the effect of a single impression. This is appropriate for the policy question ("should we run paid search in this market?") but does not identify the effect of marginal increases or decreases in ad intensity unless intensity variation is observed and modeled.

### 15.5 Small Number of Markets

With a small number of markets, cluster-robust standard errors can be unreliable. Wild cluster bootstrap or randomization inference should supplement conventional inference. The design's power is fundamentally constrained by the number of treatment units (markets), not the number of time periods or individual observations.

---

## 16. Failure Modes and Alternative Explanations

### Scenario A: Pre-Trends Are Not Parallel

If the event-study reveals systematic divergence between treated and untreated markets before the campaign, the primary causal interpretation is not credible. Fallback: report a descriptive decomposition of sales changes, noting that differences cannot be attributed to paid search vs. pre-existing trends. Segment-level analyses become purely descriptive.

### Scenario B: Positive Effect on Attributed Sales, Null on Total Sales

This pattern suggests pure channel substitution plus attribution inflation. The paid-search campaign appears to "work" in platform dashboards but creates no incremental business value. This is a substantively important finding even if it is not a causal effect on total demand.

### Scenario C: Confounding Marketing Changes

If the firm simultaneously changed other marketing activities (e.g., email campaigns, social media, pricing) in a way correlated with paid-search availability, the estimated effect conflates paid search with these other changes. Without data on concurrent marketing activities, this cannot be ruled out. The design should explicitly document all known concurrent changes.

### Scenario D: Differential Attrition or Entry

If the campaign period coincides with market entry or exit of competitors, or changes in the user base composition that differ by treatment status, the estimated effect confounds treatment with market structure changes. The segment stability check (Section 13.7) partially addresses this.

### Scenario E: Hawthorne or Reactivity Effects

If market managers knew they were part of a test, they might have changed behavior (e.g., increased local promotional effort) in ways correlated with treatment status. The "planned" nature of the variation makes this possible. The design cannot rule this out without data on local managerial actions.

---

## 17. What Cannot Be Claimed

1. **The effect of an individual clicking a paid link on that individual's purchase probability.** The design identifies a market-level ITT, not an individual-level treatment effect. Users who click paid links in treated markets differ from users who do not in unobservable ways (search intent), so individual-level comparisons are not causal.

2. **The return on ad spend (ROAS) in the platform-attribution sense.** ROAS calculations typically divide attributed revenue by ad cost, but attributed revenue conflates incremental and cannibalized sales. The design can estimate incremental total sales, which should inform a *true* ROAS calculation, but requires cost data not described in the packet.

3. **That the effect generalizes to markets outside the study.** If the markets in the study are not a random sample of all markets the firm operates in, external validity is limited. The ATT applies to the study markets only.

4. **That paid search "causes" purchases at the user level.** The design identifies whether making paid search available increases *aggregate* purchases in a market. It does not identify the psychological or behavioral mechanism at the individual level (awareness vs. reminder vs. convenience).

5. **The separate contributions of ad position, ad copy, or landing page.** The treatment bundles all aspects of paid-search availability (impressions, clicks, ad creative, landing page experience). The design cannot decompose which element drives any observed effect.

6. **Long-run effects beyond the campaign window.** With only pre-period and campaign-period data, the persistence of effects after the campaign ends is not identified.

---

## 18. Additional Data Needed

The following data, if available, would substantially strengthen the design:

| Data Need | Purpose |
|---|---|
| **Channel-disaggregated outcomes** (paid search, unpaid search, direct, referral, other) | Distinguish demand creation from channel substitution within-market; quantify cannibalization |
| **Cost data** (cost per click, total campaign spend by market) | Enable cost-benefit analysis and true incremental ROAS calculation |
| **Individual-level exposure indicators** (whether a specific user saw or clicked a paid link) | Estimate treatment-on-the-treated effects via instrumental variables (market availability as instrument for individual exposure) |
| **Query-level data** (search terms, branded vs. generic queries) | Understand whether paid search primarily captures branded/navigational searches (substitution) or generic/category searches (demand creation) |
| **Concurrent marketing activity** by market | Rule out confounding interventions |
| **Market demographic/economic covariates** | Improve precision and assess external validity |
| **Longer post-campaign follow-up** | Assess persistence of effects |
| **Assignment rationale** (why these markets got treatment) | Assess selection mechanism and strengthen or weaken causal claims |
| **Competitor presence and actions** by market | Rule out competitive confounding |

---

## 19. Threat-Response Table

*(Included per explicit inclusion in the output requirements.)*

| Threat | Severity | Response Strategy | Diagnostic |
|---|---|---|---|
| Non-parallel pre-trends | Critical | Market fixed effects + time fixed effects; include market-specific trends as robustness check | Event-study plot; joint F-test of pre-period coefficients |
| Selection into treatment based on expected growth | Critical | Conditional parallel trends; control for pre-period trend in primary specification | Placebo timing test; balance regression of treatment on pre-period characteristics |
| Outcome measures only search-attributed sales | Critical | Define outcome as total purchases, not attributed conversions | Compare total vs. attributed outcome specifications |
| Concurrent marketing interventions | High | Document all known concurrent activities; if unavailable, acknowledge as limitation | Cannot test without data; qualitative reporting |
| Cross-market spillover | Medium | Geographic buffering if data permit; acknowledge residual contamination | Impossible to test without individual location data |
| Small number of markets → unreliable inference | Medium | Wild cluster bootstrap; randomization inference | Report both conventional and bootstrap p-values |
| Segment composition differs by treatment | Medium | Pre-period balance check on segment shares; control for baseline composition | Regress segment shares on treatment status |
| Anticipation effects | Medium | Define pre-period to end before assignment announcement | Test for differential pre-trends in the period immediately before campaign |
| Repeated exposure dynamics | Low | Acknowledge that the estimand is cumulative, not per-impression | Not directly testable without impression-level data |
| Differential attrition or market exit | Low | Examine market-level observation counts over time | Test for differential missingness by treatment status |

---

## 20. Claim-Evidence Table

| # | Claim | Evidence Used | Claim Type | Confidence | What Would Falsify This Claim |
|---|---|---|---|---|---|
| 1 | Paid-search availability causes an increase in total market-level purchases | \( \hat{\delta} > 0 \) with \( p < 0.05 \) in primary specification, robust to alternative specifications | Causal (intent-to-treat) | Conditional on parallel pre-trends | \( \hat{\delta} \approx 0 \) in primary specification; pre-trend divergence |
| 2 | Paid search creates demand among less active users | \( \hat{\delta}_{\text{low}} > 0 \) with \( p < 0.05 \) in segment specification, \( \hat{\delta}_{\text{high}} \approx 0 \) | Causal (segment-specific ITT) | Moderate (lower power at segment level) | \( \hat{\delta}_{\text{low}} \approx 0 \); effect concentrated in high-activity segment instead |
| 3 | Paid search primarily substitutes for other channels among active users | \( \hat{\delta}_{\text{high}} > 0 \) on total purchases but effect on search-attributed purchases exceeds effect on total purchases | Mechanism | Moderate (requires channel-level data for direct test) | \( \hat{\delta}_{\text{high}} \approx 0 \); no gap between total and attributed effects |
| 4 | Attribution systems overstate campaign value | Treatment effect on search-attributed purchases > treatment effect on total purchases | Measurement | High (if attributed outcome data are available) | Equal effects on total and attributed outcomes |
| 5 | Average effect masks meaningful heterogeneity | \( \hat{\delta}_{\text{low}} \) and \( \hat{\delta}_{\text{high}} \) differ significantly; joint F-test rejects equality | Descriptive/Heterogeneity | Moderate (limited power for interaction tests) | \( \hat{\delta}_{\text{low}} \approx \hat{\delta}_{\text{high}} \); failure to reject equality |
| 6 | Treated and untreated markets were on parallel pre-trends | Event-study coefficients for \( k < 0 \) not significantly different from zero; joint F-test fails to reject | Diagnostic | High (directly testable) | Significant pre-period coefficients; rejection of joint null |
| 7 | The effect is not driven by a single market | Leave-one-out estimates stable; no single exclusion meaningfully changes \( \hat{\delta} \) | Robustness | High (directly testable) | Large change in \( \hat{\delta} \) when a specific market is excluded |
| 8 | Treatment effects persist (or decay) over the campaign window | Event-study coefficients for \( k \geq 0 \) show a stable (or declining, or rising) pattern | Descriptive dynamics | Low (limited number of campaign periods) | Not applicable to a single summary; pattern itself is the finding |

---

## Summary of Design Logic

```
Market-level variation in    →  ITT effect on total    →  Segment-level      →  Mechanism inference
paid-search availability         market purchases          decomposition          (creation vs. substitution)
        │                              │                        │                        │
        ▼                              ▼                        ▼                        ▼
  [Exogenous if               [Total sales avoids       [Pre-period segment      [δ_low > 0 & δ_high ≈ 0
   parallel trends              attribution bias]         assignment avoids         → demand creation]
   hold]                                                 bad control]
```

The design's strength is that it addresses the most pernicious threat—confounding by user search intent—by moving the analysis to the market level, where treatment is assigned by the firm rather than selected by users. Its primary vulnerability is the credibility of the parallel-trends assumption, which is directly testable. If that test is passed, the design provides causally interpretable evidence on whether paid search creates incremental demand and for whom.

## Tool Log Summary

- actual tool use: none
- trajectory `toolMetas`: []
- toolCall count: 0
- toolResult count: 0
- session_id: isolated_20260527_223351_98725_8
- session_log: /Users/jiangcanxiang/.openclaw/agents/benchmark_isolated/sessions/isolated_20260527_223351_98725_8.jsonl
- trajectory_log: /Users/jiangcanxiang/.openclaw/agents/benchmark_isolated/sessions/isolated_20260527_223351_98725_8.trajectory.jsonl

## Operator Notes

- duration_ms: 266367
- stderr_excerpt: [plugins] plugins.allow is empty; discovered non-bundled plugins may auto-load: qqbot (/Users/jiangcanxiang/.openclaw/npm/node_modules/@openclaw/qqbot/dist/index.js), openclaw-weixin (/Users/jiangcanxiang/.openclaw/npm/node_modules/@tencent-weixin/openclaw-weixin/dist/index.js). Set plugins.allow to explicit trusted ids. [skills] Skipping escaped skill path outside its configured root: source=openclaw-managed root=~/.openclaw/skills reason=symlink-escape requested=~/.openclaw/skills/0-autoresearch-skill resolved=~/.orchestra/skills/0-autoresearch-skill [skills] Skipping escaped skill path outside its configured root: source=openclaw-managed root=~/.openclaw/skills reason=symlink-escape requested=~/.openclaw/skills/brainstorming-research-ideas resolved=~/.orchestra/skills/21-research-ideation/brainstorming-research-ideas [skills] Skipping escaped skill path outside its configured root: source=openclaw-managed root=~/.openclaw/skills reason=symlink-escape requested=~/.openclaw/skills/creative-thinking-for-research resolved=~/.orchestra/skills/21-research-ideation/creative-thinking-for-research [skills] Skipping escaped skill path outside its configured root: source=openclaw-managed r
