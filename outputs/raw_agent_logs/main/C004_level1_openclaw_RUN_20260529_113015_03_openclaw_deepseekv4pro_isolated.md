# Raw Agent Run Log

- `run_id`: RUN_20260529_113015_03_openclaw_deepseekv4pro_isolated
- `case_id`: C004
- `variant_id`: level1
- `level`: level1
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
- `timestamp`: 2026-05-29T11:30:15+0800
- `input_file`: benchmark/cases/C004_paid_search_effectiveness/agent_task_level1.md
- `system_prompt_summary`: workspace=/Users/jiangcanxiang/OpenClawBenchmarkIsolated; thinking=high; actual_tool_use=none; agent=benchmark_isolated
- `contamination_status`: unknown
- `contamination_reason`: pending manual content review; actual tool use=none
- `status`: success

## Raw Agent Output

# Research Design: Paid Search Incrementality

---

## 1. Executive Summary

This design proposes a **market-level experiment** (or quasi-experimental variant) to estimate whether paid search ads generate incremental purchases. By comparing sales outcomes in market areas where paid search is active versus inactive, the design leverages geographic and temporal variation to approximate a counterfactual. The core identification logic is **difference-in-differences** (DiD) across market areas with staggered or simultaneous on/off conditions, supplemented by **within-user heterogeneity analysis** based on pre-existing familiarity and activity segments.

The design addresses three nested questions: (i) does paid search change aggregate purchases? (ii) does it create genuinely new demand or merely intercept existing demand? and (iii) do effects vary by user type in a way that reveals the mechanism? The strongest defensible causal claims attach to *aggregate market-level intent-to-treat effects* under the assumption that market-area treatment assignment is exogenous to demand shocks. User-level effect decomposition and mechanism claims require stronger, more tenuous assumptions and are best treated as descriptive or correlational.

---

## 2. Research Question

**Primary question:** Does making paid search placements available cause an increase in downstream purchases, and does any such effect vary by users' prior familiarity or activity with the firm?

**Decomposition questions:**
- What share of any observed purchase increase reflects genuinely incremental demand versus interception of users who would have converted through unpaid channels?
- Are effects larger among users with low prior familiarity or activity (consistent with an informational discovery mechanism) or among already active users (consistent with interception or substitution)?

---

## 3. Target Estimand

Given the available information, the strongest defensible target estimand is the **average treatment effect on the treated market areas (ATT) of paid search availability on aggregate downstream purchases**, defined over the time window in which treatment is manipulated and measured.

Formally, let \( Y_{m,t}(1) \) denote purchases in market \( m \) at time \( t \) under paid-search-on, and \( Y_{m,t}(0) \) under paid-search-off. Let \( D_{m,t} \in \{0,1\} \) indicate treatment status. The primary estimand is:

\[
\tau = \mathbb{E}[Y_{m,t}(1) - Y_{m,t}(0) \mid D_{m,t} = 1]
\]

where the expectation is taken over treated market-time units in the analysis window.

**Weaker estimand** (if assignment is non-random): the DiD estimand comparing treated and untreated markets after adjusting for pre-treatment differences in trends:

\[
\tau_{DiD} = \left( \mathbb{E}[Y_{m,post} \mid D_m = 1] - \mathbb{E}[Y_{m,pre} \mid D_m = 1] \right) - \left( \mathbb{E}[Y_{m,post} \mid D_m = 0] - \mathbb{E}[Y_{m,pre} \mid D_m = 0] \right)
\]

**User-level decomposition estimand** (descriptive only): the difference in purchase rates between campaign-on and campaign-off periods, stratified by user prior-familiarity segment. This is:

\[
\delta_s = \mathbb{E}[Y_{i} \mid D=1, S_i=s] - \mathbb{E}[Y_{i} \mid D=0, S_i=s]
\]

where \( S_i \) indexes user segment \( s \) (e.g., low vs. high prior familiarity). This estimand does *not* have a causal interpretation without additional assumptions (see Section 20).

---

## 4. Treatment / Exposure and Main Outcomes

### Treatment (exposure)
- **Variable:** \( D_{m,t} \in \{0,1\} \) — whether paid search placements are active for the focal query class in market area \( m \) during time period \( t \).
- **Nature:** Market-level binary toggle under the firm's control. The packet states the firm "can influence whether sponsored placements are active [...] in different market areas." This implies the researcher can assign or observe variation in treatment status across markets, though it does **not** guarantee random assignment.
- **Treatment assignment mechanism:** Not specified in the packet. If the firm cooperates to randomize markets to on/off conditions, assignment is experimental. If the firm determines which markets receive ads based on business considerations, assignment is observational and requires quasi-experimental methods. Both scenarios are addressed below.

### Main outcomes
1. **Primary outcome — aggregate purchases:** Total purchase count or value in market \( m \) during time \( t \), aggregated across all users in that market. This captures the net effect including both incremental and cannibalized purchases.
2. **Secondary outcome — unpaid-origin purchases:** Purchases attributed to unpaid routes (organic search, direct navigation, bookmarks, email) in market \( m \) during time \( t \). If paid search intercepts organic traffic, this outcome should *decrease* when paid search is turned on.
3. **Tertiary outcome — paid-origin purchases:** Purchases attributed to paid search click-throughs in market \( m \) during time \( t \). This is the standard "return on ad spend" numerator and is expected to be mechanically higher when ads are on.
4. **User-level outcome — individual purchase indicator:** Binary indicator for whether user \( i \) makes a purchase in period \( t \), used for heterogeneity analysis.

### Critical measurement note
The packet does not specify whether the firm can reliably decompose purchases by *attribution channel* (paid vs. unpaid origin). If this decomposition is available, the design can distinguish incremental from intercepted demand. If only aggregate sales are observed, only net effects can be estimated, and mechanism decomposition is not feasible.

---

## 5. Data Structure Summary

The data structure is a **panel of market areas over time**, with user-level segment information available as cross-sectional or repeated measures.

| Level | Unit | Dimensions | Key Variables |
|---|---|---|---|
| Market-time | Market area × time period | \( M \times T \) | Treatment indicator \( D_{m,t} \), aggregate purchases \( Y_{m,t} \), unpaid-origin purchases (if available), paid-origin purchases (if available) |
| User (cross-sectional) | Individual user | \( N \) total users | Prior familiarity segment, prior activity intensity segment, market area assignment |
| User-time (if repeated) | Individual user × time | \( N \times T \) | Purchase indicator, segment-at-baseline |

**Time structure:** The ideal design uses three phases:
1. **Pre-period:** \( T_0 \) time intervals with no paid search in any market (or stable status quo), used to establish baseline trends and segment definitions.
2. **Treatment period:** \( T_1 \) intervals where selected markets have paid search active while control markets do not.
3. **Post-period (optional):** After treatment ends, to test for persistence or reversal.

**Segment definitions** (measured at baseline, before treatment onset):
- **Prior familiarity:** Categorical or continuous measure derived from historical account activity, previous purchase history, or recency of interaction with the firm. For example: "new/never-purchased," "lapsed (>X days since last activity)," "active (purchased within Y days)."
- **Prior activity intensity:** Measure of how frequently or recently the user has engaged with the firm, such as number of past purchases, site visits, or account logins.

---

## 6. Relevant Causal Mechanisms

The packet identifies four mechanisms. I restate them here with their empirical implications — each predicts a distinct pattern in the data that the design can test:

### Mechanism 1: Informational discovery
**Logic:** Paid search exposes less familiar or less active users to the firm, generating purchases that would not have occurred otherwise.

**Empirical prediction:** Turning paid search on increases *aggregate* purchases. The increase is concentrated among users with *low* prior familiarity or activity. Unpaid-origin purchases are largely unaffected. This is the **incremental demand creation** channel.

### Mechanism 2: Interception / substitution
**Logic:** Already-informed users click paid links instead of unpaid routes. Purchases occur, but they merely replace purchases that would have happened through organic or direct channels.

**Empirical prediction:** Turning paid search on produces little or no increase in *aggregate* purchases. Paid-origin purchases rise, but unpaid-origin purchases fall by a similar magnitude. The effect is concentrated among users with *high* prior familiarity or activity. This is the **cannibalization** channel.

### Mechanism 3: Selection
**Logic:** Users who click paid search ads differ from those who do not in unobserved ways (e.g., higher latent purchase intent). Observed correlations between ad exposure and purchases reflect these differences, not ad effectiveness.

**Empirical prediction:** Naive comparisons of purchasers who saw ads vs. those who did not yield positive associations, but market-level treatment variation (which breaks the user-level selection link) shows no or much smaller effects.

### Mechanism 4: Heterogeneity masking
**Logic:** Average treatment effects may be near zero even if discovery effects (positive) and interception effects (zero net) coexist, because they offset each other.

**Empirical prediction:** Aggregate market-level effects may be null or small, but effects differ systematically across user segments in opposite directions, or differ in magnitude but not direction.

---

## 7. Main Identification Challenge

The central identification challenge is the **fundamental unobservability of the counterfactual**: for any market-time unit with paid search active, we cannot observe what purchases would have been had paid search been off. The specific threats are:

1. **Non-random treatment assignment.** If the firm activates paid search in markets where demand is already growing for reasons unrelated to ads (e.g., regional promotions, seasonality, local economic conditions), the DiD estimator will be biased upward.

2. **User-level selection into ad exposure.** Within treated markets, users who click ads differ from those who do not. Comparing purchasers who clicked ads to purchasers who did not conflates treatment effects with selection. This is why the design operates at the *market* level.

3. **Interception confounds the interpretation of paid-origin purchases.** Even if market-level DiD shows a positive aggregate effect, the *composition* of that effect (incremental vs. cannibalized) requires observing unpaid-origin purchases and modeling the shift between channels, which demands additional assumptions.

4. **Spillover / SUTVA violations.** Users in control markets may be exposed to paid search if they travel, use VPNs, or if the platform's geo-targeting is imperfect. Users in treated markets may search from locations classified as control markets. This attenuates treatment contrast and biases estimates toward zero.

5. **Dynamic demand responses.** Turning ads on may have lagged effects (users search, see the ad, and purchase later) or anticipatory effects. The time window for outcome measurement must be specified to capture these dynamics.

---

## 8. Whether Credible Causal Identification Is Possible

**Yes, partial credible causal identification is possible — but only for aggregate market-level effects under specific conditions.** The quality of identification depends critically on the treatment assignment mechanism, which the packet does not fully specify.

### Scenario A: Randomized market assignment (strongest case)
If the firm agrees to randomize a subset of comparable market areas to paid-search-on versus paid-search-off, the design is a **cluster-randomized experiment**. Under randomization, the difference in mean aggregate purchases between treated and control markets during the treatment period identifies the intent-to-treat (ITT) effect. The primary threat is SUTVA violations (spillover). Causal claims for the *aggregate market-level ITT* are credible. User-level mechanism decomposition remains correlational.

### Scenario B: Quasi-experimental (if assignment is non-random but staggered or as-if random conditional on covariates)
If assignment is not randomized, the design relies on DiD with the assumption of **parallel trends** in the absence of treatment. Credibility depends on:
- The number of market areas (more markets → better inference, more plausible asymptotics).
- Whether pre-treatment trends are visually and statistically parallel.
- Whether the researcher can control for time-varying market-level confounders.
Causal claims are **weaker than under randomization** and require the parallel-trends assumption.

### Scenario C: Purely observational (no market-level variation in treatment)
If all markets receive treatment simultaneously or treatment follows a deterministic rule (e.g., only the largest markets get ads), the design collapses to a **pre-post comparison** with no contemporaneous control group. In this case, **credible causal identification is not possible**. The strongest defensible analysis is descriptive: compare purchase patterns before versus during the campaign, and across user segments, while explicitly noting that time trends, seasonality, and co-occurring events cannot be separated from treatment effects.

**The remainder of this design assumes Scenario A or B. I will flag where conclusions differ under Scenario C.**

---

## 9. Proposed Empirical Design

### Design: Market-level experiment with DiD analysis and user-segment heterogeneity

**Step 1 — Define market areas and treatment allocation.**
- Identify \( M \) market areas (geographic regions used for ad targeting on the platform). The packet does not specify the number; the design requires enough markets for meaningful inference (practically: >10 per arm for nonparametric inference, >30 per arm for asymptotically valid parametric inference).
- **Scenario A (randomized):** Randomly assign half the markets to treatment (paid search on) and half to control (paid search off). Stratify randomization on pre-treatment average purchase levels to improve balance.
- **Scenario B (observational):** Document the rule by which treatment status varies. Use markets that never receive treatment (or receive it later) as controls, provided pre-treatment trends are parallel.

**Step 2 — Define time periods.**
- **Pre-period:** \( t = -T_0, \ldots, -1 \), during which treatment status is as-observed or (preferably) off for all markets. Use this period to validate parallel trends and define user segments.
- **Treatment period:** \( t = 1, \ldots, T_1 \), during which assigned markets have paid search on and control markets have it off.
- **Segment definition window:** Baseline period before \( t = -T_0 \) for classifying users by prior familiarity and activity. Users are classified based on *pre-period* behavior only, ensuring segments are not post-treatment (i.e., not affected by the treatment itself).

**Step 3 — Primary analysis: Market-level DiD.**
- Aggregate purchases to market \( \times \) time level.
- Estimate DiD with market and time fixed effects (equation in Section 12).

**Step 4 — Mechanism analysis: Decompose aggregate effects.**
- Repeat the DiD on unpaid-origin purchases. A decrease in unpaid-origin purchases when paid search is active is evidence of interception/substitution.
- Repeat on paid-origin purchases. The difference (paid effect minus unpaid displacement) approximates net incremental demand.

**Step 5 — Heterogeneity analysis: User-segment effects.**
- Estimate treatment effects separately by user segment (low vs. high familiarity; low vs. high activity), using market-segment-time aggregates. Because segments are defined at baseline, they are not affected by treatment.

---

## 10. Why the Design Is Valid (or Why Causal Identification Is Not Credible)

### Validity under Scenario A (randomized assignment)
Randomization of market areas to treatment ensures that, in expectation, treated and control markets are comparable on all observed and unobserved characteristics. The difference in mean outcomes identifies the ATE (or ATT, depending on the estimand of interest). The cluster-randomized structure correctly accounts for within-market correlation of outcomes.

### Validity under Scenario B (DiD with parallel trends)
The DiD estimator removes:
- Time-invariant market-level differences (via market fixed effects).
- Common time shocks affecting all markets equally (via time fixed effects).
What remains is the differential change in treated markets relative to control markets after treatment onset. This identifies the ATT if:
- In the absence of treatment, treated markets would have evolved *in parallel* to control markets.
- No other market-specific shocks coincide with treatment onset.

### Validity of mechanism decomposition
The channel decomposition (paid vs. unpaid) is valid for the *intent-to-treat* effect: it tells us whether aggregate purchases increased and whether unpaid purchases were displaced, *at the market level*. However, it cannot identify what any *individual* user would have done in the counterfactual, because the decomposition aggregates over users with different latent behaviors.

### Why user-level comparisons are not causally identified
Within a treated market, users who click ads differ from users who do not. Comparing their purchase rates cannot separate the causal effect of ad exposure from selection. The segment analysis is valid for *market-level treatment effects conditional on baseline segment* (i.e., does making ads available in a market increase purchases among low-familiarity users in that market?) — but this remains an ITT at the segment level, not a treatment-on-the-treated effect.

---

## 11. Required Assumptions

| # | Assumption | Role | Plausibility / Threat |
|---|---|---|---|
| **A1** | **No spillover (SUTVA).** Treatment status in market \( m \) does not affect outcomes in market \( m' \). | Required for DiD to identify ATT. | Plausible if market areas are geographically separated and users rarely cross boundaries for search/purchase. Threat: VPNs, travel, platform targeting imprecision. |
| **A2** | **Parallel trends.** In the absence of treatment, the difference between treated and control markets would have remained constant over time. | Required for DiD validity (Scenario B). Under Scenario A, this is not required — randomization suffices. | Testable in the pre-period. Not testable post-treatment. |
| **A3** | **No anticipation.** Outcomes in treated markets are not affected by treatment before it is turned on. | Required for DiD to correctly attribute effects to the treatment period. | Plausible if treatment onset is unannounced. Threatened if the firm pre-announces campaign changes. |
| **A4** | **Treatment is as-assigned.** The firm does not deviate from the assigned treatment schedule based on interim outcomes. | Required for the ITT interpretation. | Under researcher control in an experimental design. Threatened if business needs override the research protocol. |
| **A5** | **Segment classification is pre-treatment.** User segments (familiarity, activity) are defined using data from before treatment onset. | Required for heterogeneity analysis to avoid conditioning on post-treatment variables (which would be endogenous). | Under researcher control. |
| **A6** | **No compositional changes.** The user base in each market does not change systematically in response to treatment (e.g., ads do not attract users from outside the market who then appear in the data as if they were always there). | Required for market-level DiD to capture the effect on a stable population. | Potentially violated if ads attract genuinely new users to the firm. This is a *feature* (incremental demand) but complicates the fixed-effects interpretation. |
| **A7** | **Correct attribution of purchase channels.** Unpaid-origin and paid-origin purchases are measured without systematic error. | Required for mechanism decomposition. | Threatened if the firm's attribution system is cookies-based and users clear cookies, switch devices, or use multiple browsers. |

---

## 12. Statistical Model / Analysis Equation

### Primary specification: Market-level difference-in-differences

\[
Y_{m,t} = \alpha_m + \lambda_t + \beta \cdot (D_{m,t}) + \varepsilon_{m,t}
\]

Where:
- \( Y_{m,t} \): aggregate purchases in market \( m \) during time period \( t \).
- \( \alpha_m \): market fixed effects (absorb time-invariant market characteristics).
- \( \lambda_t \): time fixed effects (absorb common time shocks).
- \( D_{m,t} \in \{0,1\} \): treatment indicator (=1 if market \( m \) has paid search on in period \( t \)).
- \( \beta \): **parameter of interest** — the ATT of paid search availability on aggregate purchases.
- \( \varepsilon_{m,t} \): error term. Standard errors should be **clustered at the market level** to account for serial correlation within markets (Bertrand, Duflo, and Mullainathan, 2004).

### Event-study specification (for parallel trends validation and dynamic effects)

\[
Y_{m,t} = \alpha_m + \lambda_t + \sum_{k = -K, k \neq -1}^{L} \beta_k \cdot \mathbf{1}[t - t^*_m = k] + \varepsilon_{m,t}
\]

Where:
- \( t^*_m \) is the period when treatment starts for market \( m \).
- \( k \) indexes periods relative to treatment onset (\( k < 0 \) = pre-treatment leads; \( k \geq 0 \) = post-treatment lags).
- \( \beta_k \) for \( k < 0 \) tests for pre-trends (should be near zero under parallel trends).
- \( \beta_k \) for \( k \geq 0 \) captures the dynamic treatment effect over time.

### Channel decomposition specification

\[
Y^{\text{unpaid}}_{m,t} = \alpha^{\text{unpaid}}_m + \lambda^{\text{unpaid}}_t + \beta^{\text{unpaid}} \cdot D_{m,t} + \varepsilon^{\text{unpaid}}_{m,t}
\]

\[
Y^{\text{paid}}_{m,t} = \alpha^{\text{paid}}_m + \lambda^{\text{paid}}_t + \beta^{\text{paid}} \cdot D_{m,t} + \varepsilon^{\text{paid}}_{m,t}
\]

- If \( \beta > 0 \) (aggregate purchases increase) and \( \beta^{\text{unpaid}} \approx 0 \): evidence for **incremental demand**.
- If \( \beta \approx 0 \) but \( \beta^{\text{paid}} > 0 \) and \( \beta^{\text{unpaid}} < 0 \) with \( \beta^{\text{paid}} \approx -\beta^{\text{unpaid}} \): evidence for **pure interception** with no net incrementality.
- If \( \beta > 0 \) but \( \beta^{\text{paid}} > \beta \) (i.e., paid purchases increase by more than aggregate): partial interception coexisting with some incremental demand.

### Heterogeneity specification (segment-level)

\[
Y_{m,s,t} = \alpha_{m,s} + \lambda_{s,t} + \sum_{s \in \mathcal{S}} \beta_s \cdot (D_{m,t} \times \mathbf{1}[S = s]) + \varepsilon_{m,s,t}
\]

Where:
- \( Y_{m,s,t} \): aggregate purchases among users in segment \( s \) in market \( m \) at time \( t \).
- \( \beta_s \): ATT of paid search availability for segment \( s \).
- Segments \( \mathcal{S} \) are defined at baseline.

---

## 13. Robustness, Placebo, Falsification, and Diagnostic Tests

### 13.1 Parallel trends diagnostics
- **Visual inspection:** Plot event-study coefficients \( \beta_k \) for \( k < 0 \). Pre-trend coefficients should be close to zero and show no systematic upward or downward pattern.
- **Joint F-test:** Test the null that all pre-treatment \( \beta_k = 0 \) for \( k < 0 \). Failure to reject is consistent with (but does not prove) parallel trends.
- **Placebo treatment date test:** Shift the treatment date backward to a pre-period and re-estimate the DiD. The "effect" at the false treatment date should be near zero.

### 13.2 Falsification using outcomes that should not respond
- If the data contain a *purchase category or product line that is not advertised* in the paid search campaign, test whether treatment affects purchases of that category. A non-zero effect suggests confounding demand shocks rather than ad effects.
- If the data contain user actions that occur *before* the search-and-purchase funnel (e.g., unrelated browsing), test for treatment effects on these actions. No effect is expected.

### 13.3 Robustness to alternative specifications
- **Alternative functional forms:** Log-transformed outcomes (to estimate proportional effects), Poisson pseudo-maximum likelihood (if outcomes are count data with zeros).
- **Leave-one-out:** Drop each market one at a time and re-estimate to check sensitivity to any single market.
- **Alternative time aggregations:** Aggregate to weekly, biweekly, and monthly levels to ensure results are not driven by the choice of time window.
- **Varying the pre-period window:** Use different lengths of pre-period data to ensure baseline trend estimation is not sensitive to the pre-period length.

### 13.4 Randomization inference (Scenario A)
- Under randomized assignment, conduct **Fisher randomization tests**: simulate the distribution of the treatment effect under all possible (or a large number of random) assignments of markets to treatment and control, and compare the observed effect to this null distribution.

### 13.5 Sensitivity to spillover
- **Buffer-zone analysis:** If geographic distance between markets is available, exclude market pairs that are geographically adjacent and re-estimate. If spillover is present, estimates should increase when contiguous markets are excluded (because contamination is removed).
- **Dose-response check:** If the platform provides *impression counts* or ad-spend levels (not guaranteed by the packet), test whether purchases increase with treatment intensity within treated markets.

---

## 14. Heterogeneity Analysis

### 14.1 By prior familiarity

Define segments at baseline:
- **Low familiarity:** Users with no prior purchases or no account activity before the pre-period.
- **Medium familiarity:** Users with some prior interaction but not recent.
- **High familiarity:** Users with recent purchases or frequent past engagement.

**Estimation:** Estimate the segment-level DiD specification (Section 12). If the informational discovery mechanism operates, we expect \( \beta_{\text{low}} > \beta_{\text{high}} \) and \( \beta_{\text{low}} > 0 \).

### 14.2 By prior activity intensity

Define segments at baseline:
- **Inactive:** No measurable activity in the pre-period window.
- **Low activity:** Infrequent engagement.
- **High activity:** Frequent or recent engagement.

The same logic applies: discovery effects should be concentrated among low-activity users.

### 14.3 Cross-segment analysis

Examine the intersection of familiarity and activity (e.g., low-familiarity + low-activity vs. high-familiarity + high-activity). The discovery channel predicts the largest positive effect in the low-low cell.

### 14.4 Important caveat on heterogeneity

These segment-level estimates remain **ITT effects at the segment level**. They answer: "When paid search is made available in a market, do purchases among low-familiarity users in that market increase relative to a counterfactual market?" They do **not** answer: "Does exposing a specific low-familiarity user to a paid search ad cause that user to purchase?" The latter requires an instrument or exogenous variation in ad *exposure* conditional on availability, which the packet does not provide.

---

## 15. Measurement, Compliance, Missingness, Spillover, and Implementation Limits

### 15.1 Measurement limits

- **Attribution window:** The firm's attribution system may attribute a purchase to paid search only if the click occurred within a fixed window (e.g., 30 days). Purchases influenced by ads but occurring after the window are misattributed to unpaid channels, inflating the apparent interception rate.
- **Cross-device tracking:** Users who click on mobile but purchase on desktop (or vice versa) may have their purchase misattributed. This attenuates the measured paid-search effect.
- **Cookie deletion and browser fragmentation:** Users who clear cookies or use multiple browsers appear as "new" users, inflating the low-familiarity segment with false positives.

### 15.2 Compliance limits

- **Imperfect ad delivery:** The platform may not deliver ads uniformly across all treated markets due to auction dynamics, budget constraints, or ad-quality thresholds. Actual treatment intensity may vary even when treatment is nominally "on."
- **Two-sided noncompliance:** Some control-market users may see ads (e.g., if they travel to treated areas or if geo-targeting fails). Some treated-market users may not see ads (e.g., if they use ad blockers or search queries that do not trigger the placement).

### 15.3 Missingness

- **Outcome missingness:** If the firm's sales tracking system has incomplete coverage in certain markets, the data are missing not at random (correlated with market characteristics). This biases market-level comparisons.
- **Segment missingness:** User segment classification requires pre-period activity data. Users with no pre-period data at all cannot be classified; they are either genuinely new or represent tracking failures.

### 15.4 Spillover

- **Geographic spillover:** The most serious threat. Users near market boundaries may be classified in one market but see ads targeted to another.
- **Digital spillover:** The platform's targeting algorithms may not respect the researcher's market boundaries (e.g., IP-based geo-targeting is imperfect).
- **Mitigation:** Define market areas as conservatively as possible (larger, more separated units). If available, use platform-provided impression data to verify treatment compliance at the user level.

### 15.5 Implementation limits

- **Minimum detectable effect:** With a limited number of market areas, statistical power may be low. The design may only be able to detect large effects. The packet does not provide sample sizes; if \( M \) is small (e.g., <20), the study is underpowered for all but the largest effects.
- **Duration:** If the treatment period is short, effects may not have time to materialize (users need time to search, discover, and purchase). If it is long, market conditions may change, threatening the parallel-trends assumption.

---

## 16. Failure Modes and Alternative Explanations

1. **Confounded treatment assignment.** If treatment status correlates with unobserved demand shocks, the DiD estimate captures both the ad effect and the shock. Example: the firm activates ads in markets where a local event or promotion is also running.

2. **Ashenfelter's dip.** If treated markets were selected because they had unusually low sales in the pre-period, mean reversion will cause sales to rise in the treatment period regardless of ads, producing a spurious positive DiD estimate.

3. **Seasonality interacting with treatment.** If treated and control markets have different seasonal patterns (e.g., different holiday timing, tourism seasons), the DiD estimator confounds treatment effects with differential seasonality.

4. **Compositional changes.** If ads attract genuinely new users who were not previously in the market's user base, aggregate sales increase, but the effect is partly due to a change in the population, not just behavior within a fixed population. This is not a "bias" per se (it is a real effect), but it changes the interpretation.

5. **Equilibrium responses.** If control-market outcomes are affected by treatment (spillover): users in control markets travel to treated markets to purchase, or word-of-mouth from treated-market users influences control-market users. This biases DiD toward zero.

6. **Learning and habituation.** If users in treated markets learn to use paid search as their primary discovery method and shift away from organic routes over time, the effect composition changes dynamically. Short-run estimates may differ from long-run estimates.

7. **Platform algorithmic response.** If the search platform's algorithm adjusts organic rankings or ad auction dynamics in response to demand signals, the "treatment" is not simply "ad on vs. off" but a bundle of platform responses that differ across markets.

---

## 17. What Cannot Be Claimed

The following claims are **not supported** by the available information and design:

1. **"Paid search ads cause individual users to purchase."** The design identifies the effect of *making ads available in a market*, not the effect of *exposing a specific user to an ad*. The latter requires individual-level exogenous variation in ad exposure, which the packet does not provide.

2. **"X% of paid-search-attributed purchases are incremental."** Attributing incremental purchases at the individual level requires assumptions about which specific purchases would or would not have occurred without ads. The design can estimate *net* incrementality at the market level but cannot tag individual purchases as incremental or cannibalized.

3. **"The return on ad spend (ROAS) is Y."** ROAS requires knowing ad spend, which the packet does not mention as available. Even if it were, ROAS conflates incremental and non-incremental purchases unless net incrementality is used as the numerator.

4. **"Low-familiarity users respond to ads because ads provide information."** The heterogeneity analysis can show *whether* low-familiarity users respond more, but it cannot identify *why*. The informational mechanism is one interpretation; alternative interpretations (e.g., low-familiarity users are more price-sensitive and ads signal discounts) are equally consistent with the data pattern.

5. **"Effects persist indefinitely" or "effects generalize to other query classes, platforms, or time periods."** The design estimates effects for the specific query class, platform, and time period studied. External validity is not established.

6. **"The optimal ad-spend level is Z."** The design estimates the effect of presence/absence, not a dose-response function. Even with spend data, extrapolating to optimal spend requires assumptions about the shape of the response function outside the observed range.

---

## 18. Additional Data Needed

The following data, if available, would substantially strengthen the design. Each item is listed with its purpose:

| Data Need | Purpose |
|---|---|
| **Ad impression and click data at the user level** | Enables instrumental-variables estimation (using market-level ad availability as an instrument for individual ad exposure) to estimate treatment-on-the-treated effects. |
| **Ad spend or impression counts by market and time** | Enables dose-response analysis and cost-effectiveness calculations. |
| **Exact number of market areas and their identities** | Enables power analysis, randomization design, and assessment of parallel trends plausibility. |
| **Platform-side data on organic search rankings** | Distinguishes whether interception occurs because users *choose* paid links over organic links or because organic rankings *change* when ads are present. |
| **User-level search query text** | Enables analysis of whether ad effects differ by query type (navigational vs. generic/category queries), which is central to the discovery-vs-interception distinction but was classified as "not provided" in the packet. |
| **Cross-device and cross-browser identity resolution** | Reduces measurement error in user-segment classification and purchase attribution. |
| **Information on other concurrent marketing activities** | Rules out confounded treatment assignment (e.g., markets with paid search also receive email campaigns or in-store promotions). |

---

## 19. Threat-Response Table

The task packet does not explicitly request a threat-response table, but for completeness:

| Threat | Severity | Detection Strategy | Response |
|---|---|---|---|
| Non-parallel pre-trends | High | Event-study plot; F-test on pre-treatment coefficients | If pre-trends are present, DiD is not credible. Consider synthetic control methods (Abadie et al., 2010) to construct better counterfactuals, or restrict to markets with parallel pre-trends. If neither solves the problem, downgrade to descriptive pre-post analysis. |
| Spillover across markets | High | Buffer-zone analysis; check outcomes in adjacent untreated markets | Exclude adjacent market pairs; use "doughnut" designs that drop boundary regions; if spillover is pervasive, the market-level design is compromised. |
| Confounded treatment assignment | High (Scenario B) | Placebo tests on unaffected outcomes; check covariate balance on observables | If observables are imbalanced in the pre-period, include market-specific linear trends or reweight using propensity scores. If unobservables are imbalanced, causal claims are not credible. |
| Ashenfelter's dip | Medium | Check whether treated markets had unusually low pre-period outcomes | If present, control for lagged outcomes or use changes-on-changes specifications. Interpret results cautiously. |
| Differential seasonality | Medium | Include market-specific seasonal controls; test effects on outcomes with different seasonality | If seasonality differs systematically across treatment arms, restrict to seasonally homogeneous markets or use year-over-year DiD. |
| Compositional change | Low-Medium | Compare user-base size and characteristics pre vs. post in treated markets | If user base grows in treated markets, report both per-capita and aggregate effects. |
| Attribution measurement error | Medium | Sensitivity analysis varying the attribution window; compare device-level vs. account-level attribution | Report results under multiple attribution assumptions. If measurement error is severe, the channel decomposition is unreliable. |
| Low statistical power | Medium | Ex-ante power analysis; ex-post confidence interval width | If power is low, report effect sizes with confidence intervals rather than binary significance. Caution against overinterpreting null results. |

---

## 20. Claim-Evidence Table

| # | Claim | Evidence Used | Claim Type | Confidence | What Would Falsify This Claim |
|---|---|---|---|---|---|
| 1 | Paid search availability increases aggregate purchases in treated markets relative to control markets. | Market-level DiD estimate \( \hat{\beta} > 0 \) with confidence interval excluding zero; balanced pre-trends; robustness to alternative specifications. | **Causal** (under randomization, Scenario A) or **Causal-with-assumptions** (under DiD, Scenario B) | High under Scenario A; moderate under Scenario B depending on pre-trend evidence | (a) Pre-treatment event-study coefficients show systematic non-zero trends. (b) Placebo test at false treatment date produces significant effect. (c) Effect is not robust to exclusion of any single market or alternative time aggregation. |
| 2 | The aggregate purchase increase reflects incremental demand rather than interception. | \( \hat{\beta} > 0 \) and \( \hat{\beta}^{\text{unpaid}} \) is not significantly negative; paid-origin purchases increase without corresponding decrease in unpaid-origin purchases. | **Causal interpretation of a mechanism test** (channel decomposition is identified under same assumptions as primary DiD) | Moderate | (a) \( \hat{\beta}^{\text{unpaid}} \) is negative and similar in magnitude to \( \hat{\beta}^{\text{paid}} \), implying full cannibalization. (b) Attribution measurement error is large enough to obscure the channel decomposition. |
| 3 | Effects are larger for low-familiarity users than high-familiarity users. | Segment-level DiD estimates with \( \hat{\beta}_{\text{low}} > \hat{\beta}_{\text{high}} \); formal test of coefficient equality rejects. | **Causal for market-level ITT at the segment level; descriptive for user-level mechanism** | Moderate-Low | (a) Segment estimates are not statistically distinguishable. (b) Segment classification is contaminated by measurement error (cookie deletion, cross-device). (c) High-familiarity users show equal or larger effects. |
| 4 | Ads create informational discovery — new users learn about the firm through paid search and subsequently purchase. | Combination of claims 2 and 3: aggregate purchases increase, unpaid purchases do not fall, and effects concentrate among low-familiarity users. | **Interpretive / mechanism inference** (consistent with but not proven by the data pattern) | Low | Any of the falsification conditions for claims 2 or 3. Also: the same pattern could arise from low-familiarity users being more price-sensitive and responding to ad-communicated promotions rather than informational discovery per se. |
| 5 | Paid search is a cost-effective customer acquisition channel. | Not testable with available information (requires ad spend data, which the packet does not mention). | **Not claimable** | N/A | N/A |
| 6 | The estimated effect generalizes to other query classes, platforms, or time periods. | No evidence provided in the design. External validity would require replication across settings. | **Not claimable** | N/A | N/A |
| 7 | Individual user purchases attributed to paid search are causally caused by ad exposure. | The design operates at the market level; individual ad exposure is endogenous. | **Not claimable** | N/A | N/A |

---

### Summary of the Design's Logical Structure

```
                     Market-level treatment
                     (paid search on/off)
                            │
                            ▼
              ┌─────────────────────────────┐
              │  DiD / Randomized comparison │  ← Credibly identified
              │  Aggregate purchases         │     (under assumptions)
              └─────────────────────────────┘
                            │
                ┌───────────┴───────────┐
                ▼                       ▼
     ┌──────────────────┐    ┌──────────────────┐
     │ Paid-origin       │    │ Unpaid-origin     │  ← Mechanism decomposition
     │ purchases         │    │ purchases         │     (same assumptions)
     └──────────────────┘    └──────────────────┘
                │                       │
                └───────────┬───────────┘
                            ▼
              ┌─────────────────────────────┐
              │ Net incrementality estimate  │  ← Interpretable as causal
              │ (paid increase - unpaid      │     under same assumptions
              │  displacement)               │
              └─────────────────────────────┘
                            │
                            ▼
              ┌─────────────────────────────┐
              │ Segment-level DiD            │  ← Causal for segment ITT;
              │ (low vs. high familiarity,   │     mechanism interpretation
              │  low vs. high activity)      │     is correlational
              └─────────────────────────────┘
                            │
                            ▼
              ┌─────────────────────────────┐
              │ Mechanism interpretation     │  ← Descriptive / suggestive
              │ (discovery vs. interception) │     only
              └─────────────────────────────┘
```

The descending gradient from top to bottom reflects the declining strength of causal identification as the analysis moves from aggregate market-level effects to user-level mechanism interpretations.

## Tool Log Summary

- actual tool use: none
- trajectory `toolMetas`: []
- toolCall count: 0
- toolResult count: 0
- session_id: isolated_20260529_113015_52386_3
- session_log: /Users/jiangcanxiang/.openclaw/agents/benchmark_isolated/sessions/isolated_20260529_113015_52386_3.jsonl
- trajectory_log: /Users/jiangcanxiang/.openclaw/agents/benchmark_isolated/sessions/isolated_20260529_113015_52386_3.trajectory.jsonl

## Operator Notes

- duration_ms: 200276
- stderr_excerpt: [plugins] plugins.allow is empty; discovered non-bundled plugins may auto-load: qqbot (/Users/jiangcanxiang/.openclaw/npm/node_modules/@openclaw/qqbot/dist/index.js), openclaw-weixin (/Users/jiangcanxiang/.openclaw/npm/node_modules/@tencent-weixin/openclaw-weixin/dist/index.js). Set plugins.allow to explicit trusted ids. [skills] Skipping escaped skill path outside its configured root: source=openclaw-managed root=~/.openclaw/skills reason=symlink-escape requested=~/.openclaw/skills/0-autoresearch-skill resolved=~/.orchestra/skills/0-autoresearch-skill [skills] Skipping escaped skill path outside its configured root: source=openclaw-managed root=~/.openclaw/skills reason=symlink-escape requested=~/.openclaw/skills/brainstorming-research-ideas resolved=~/.orchestra/skills/21-research-ideation/brainstorming-research-ideas [skills] Skipping escaped skill path outside its configured root: source=openclaw-managed root=~/.openclaw/skills reason=symlink-escape requested=~/.openclaw/skills/creative-thinking-for-research resolved=~/.orchestra/skills/21-research-ideation/creative-thinking-for-research [skills] Skipping escaped skill path outside its configured root: source=openclaw-managed r
