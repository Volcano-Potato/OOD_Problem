# Raw Agent Run Log

- `run_id`: RUN_20260527_224310_10_openclaw_deepseekv4pro_isolated
- `case_id`: C004
- `variant_id`: perturbed
- `level`: perturbed
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
- `timestamp`: 2026-05-27T22:43:10+0800
- `input_file`: benchmark/cases/C004_paid_search_effectiveness/agent_task_perturbed.md
- `system_prompt_summary`: workspace=/Users/jiangcanxiang/OpenClawBenchmarkIsolated; thinking=high; actual_tool_use=none; agent=benchmark_isolated
- `contamination_status`: unknown
- `contamination_reason`: pending manual content review; actual tool use=none
- `status`: success

## Raw Agent Output

# Research Design: Paid-Search Availability and Downstream Purchases

## 1. Executive Summary

This packet asks whether paid-search availability generates incremental purchases or merely intercepts users who would reach the firm through other channels. Unlike the base variant, the **perturbed condition** replaces exogenous or pre-committed experimental assignment with campaign managers' discretionary decisions — which markets to reduce or suspend paid search in, based on operational judgments, expected demand, or budget considerations. This change fundamentally transforms the identification problem: treatment status is now **endogenously selected**, and the original Difference-in-Differences logic no longer supports credible causal identification without further design elements not present in the packet. The strongest defensible analysis is a carefully matched comparison with explicit sensitivity diagnostics, yielding **conditional correlational evidence** rather than causal estimates. The design below lays out what can and cannot be claimed under these constraints, proposes a structured empirical workflow, and specifies the additional data or design features that would be required to restore causal credibility.

---

## 2. Research Question

Does paid-search availability in a given market cause incremental downstream purchases, or does it largely intercept demand that would have converted through unpaid or direct channels anyway? Does any measured effect differ between less-active and already-active users?

---

## 3. Target Estimand (and Strongest Defensible Estimand)

**Target estimand:** The average treatment effect on the treated (ATT) of paid-search availability on downstream purchases during the intervention window, separately for the full market and for user-history segments.

Formally, let \( M \) index markets and \( t \) index time. Let \( D_{m} \in \{0, 1\} \) indicate whether market \( m \) has paid-search availability reduced or suspended during the intervention period. Let \( Y_{mt}(1) \) and \( Y_{mt}(0) \) be potential purchase outcomes with and without paid-search availability, respectively. The intended ATT is:

\[
\tau_{\text{ATT}} = \mathbb{E}\left[Y_{mt}(1) - Y_{mt}(0) \mid D_m = 1\right]
\]

for \( t \) in the intervention window.

**Strongest defensible estimand under the perturbed condition:** The above ATT is **not credibly identifiable** from the available data and variation, because treatment assignment is endogenous to expected outcomes. The strongest defensible quantity is a **conditional difference-in-differences estimate** — the change in outcomes for treated markets relative to a matched comparison group, adjusted for observable baseline characteristics — interpreted as **descriptive associational evidence** rather than a causal effect. The estimand becomes:

\[
\delta = \mathbb{E}\left[\Delta Y_m \mid D_m = 1, \mathbf{X}_m\right] - \mathbb{E}\left[\Delta Y_m \mid D_m = 0, \mathbf{X}_m\right]
\]

where \(\Delta Y_m\) is the pre-to-intervention change in market-level purchases and \(\mathbf{X}_m\) is a vector of observable baseline characteristics. This is an association measure. It does not recover a causal parameter unless selection into treatment is fully determined by \(\mathbf{X}_m\) (unconfoundedness), an assumption the packet explicitly rules out.

---

## 4. Treatment or Exposure and Main Outcomes

| Concept | Operational Definition | Level |
|---|---|---|
| **Treatment variable** | Binary indicator: paid-search availability reduced or suspended in market \( m \) during the intervention window (= 1 if reduced/suspended; = 0 if maintained) | Market |
| **Intensity alternative** | If observed: fraction of intervention-period days in which paid search was unavailable, or a continuous measure of ad spend reduction | Market-time |
| **Primary outcome** | Downstream purchases, sales, orders, or revenue aggregated to the market-time level | Market-time |
| **Secondary outcome** | Segment-specific purchases: new-to-firm users, less-active users (low prior frequency/recency), already-active users (high prior frequency/recency) | Market-time-segment |

---

## 5. Data Structure Summary

- **Panel structure:** Market-by-time repeated observations, spanning a pre-period (before intervention) and an intervention period.
- **Number of units:** Multiple market areas, continuously observed.
- **Treatment assignment:** Non-random; campaign managers choose which markets to reduce/suspend based on operational judgment, expected demand, or budget considerations.
- **Treatment variation:** Cross-sectional (between-market) variation in paid-search availability status during the intervention window, possibly with within-market time variation if availability changes partway through.
- **Outcome measurement:** Downstream purchases or revenue per market per time period; additionally split by user-history segment (prior familiarity, recency, frequency).
- **Key complication:** Market-level ad availability does not map one-to-one into individual exposure. Users may substitute across unpaid search, direct navigation, neighboring markets, or other channels (spillover/interference).

---

## 6. Relevant Causal Mechanisms

The following mechanisms must be accounted for in any empirical design:

1. **Direct ad effect**: Paid-search availability generates incremental purchases by surfacing the firm to users who would not otherwise find or choose it (the causal channel of interest).

2. **Interception / cannibalization**: Paid-search placements capture users who would have reached the firm through unpaid (organic) search, direct navigation, bookmarks, email, or other channels. In this case, observed purchases under paid-search availability overstate the incremental effect.

3. **Endogenous treatment selection**: Campaign managers reduce or suspend paid search in markets where they expect lower returns — for instance, markets with weaker underlying demand, lower conversion rates, or budget-constrained marginal returns. This induces a **negative correlation between treatment status and potential outcomes**, biasing naive comparisons downward. Conversely, managers might suspend paid search in markets that are already performing well organically (perceived as not needing paid support), inducing the opposite bias. The direction of bias is unknowable from the packet alone.

4. **Market-level demand heterogeneity**: Markets differ in baseline demand levels, trends, seasonality, competitive intensity, and customer composition. These differences both influence treatment assignment and drive outcome trajectories.

5. **Substitution and spillover**: Users in treated markets (reduced paid search) may substitute to organic search, direct navigation, or neighboring-market search results. Users in control markets may be unaffected or may absorb demand displaced from treated markets.

6. **Segment-level heterogeneity**: Less-active users may rely more on paid search for discovery (potentially larger treatment effects), while already-active users may navigate directly (potentially smaller effects, or pure interception).

---

## 7. Main Identification Challenge

The core identification challenge is **selection on unobservables**. Campaign managers choose treatment status based on factors that are correlated with the outcome — expected demand, market potential, operational constraints, budget considerations, and past performance. These factors are not fully observed by the researcher.

In the base (unperturbed) variant, treatment assignment is exogenous or governed by a pre-committed experimental rule, making it orthogonal to potential outcomes. Under the perturbed condition, the parallel-trends assumption required by Difference-in-Differences is no longer defensible, because:

\[
\mathbb{E}\left[\Delta Y_m(0) \mid D_m = 1\right] \neq \mathbb{E}\left[\Delta Y_m(0) \mid D_m = 0\right]
\]

Managers' decisions embed private information about expected demand trajectories. Treated and untreated markets would have diverged even without the intervention, and the magnitude and direction of this divergence cannot be inferred from pre-period data alone.

The problem is compounded by spillover and substitution, which violate the Stable Unit Treatment Value Assumption (SUTVA).

---

## 8. Whether Credible Causal Identification Is Possible

**No.** From the information provided in this packet, credible causal identification of the effect of paid-search availability on downstream purchases is not possible.

The perturbation — replacing exogenous assignment with discretionary manager decisions — severs the key link between data structure and identification. No amount of covariate adjustment, matching, or panel-data technique can recover a causal parameter when treatment assignment is systematically correlated with unobserved outcome determinants.

The analysis that follows is therefore **the strongest defensible associational/descriptive analysis**, not a causal design. The output should be interpreted as evidence about patterns of association between paid-search availability and downstream purchases, subject to unmeasured confounding. The confidence consumers should place in these results is substantially lower than they could place in results from a design with exogenous variation.

---

## 9. Proposed Empirical Design: Strongest Defensible Descriptive Analysis

### Phase 1: Characterize the Selection Process

Before any outcome analysis, **document how treatment was assigned**:

- Interview campaign managers or review internal decision records to elicit the criteria used for selecting markets to reduce/suspend.
- Tabulate observable differences between treated and untreated markets in the pre-period: mean sales, sales trends, seasonal patterns, market size, competitive intensity proxies, user composition (share of active vs. less-active users).
- Estimate a selection equation (probit or logit) predicting treatment status from pre-period observables:
  \[
  \Pr(D_m = 1) = \Phi(\gamma_0 + \gamma_1 \bar{Y}_{m,\text{pre}} + \gamma_2 \Delta Y_{m,\text{pre}} + \gamma_3 \mathbf{W}_m)
  \]
  where \(\bar{Y}_{m,\text{pre}}\) is average pre-period sales, \(\Delta Y_{m,\text{pre}}\) is the pre-period sales trend, and \(\mathbf{W}_m\) contains baseline market characteristics.

- Report the pseudo-\(R^2\) and the estimated selection-on-observables relationship. This transparency is essential for readers to assess the plausibility of confounding.

### Phase 2: Construct a Matched Comparison Group

Use **propensity score matching** or **entropy balancing** to construct a comparison group of untreated markets that resemble treated markets on all available pre-period observables:

1. Estimate propensity scores from the selection equation in Phase 1.
2. Match each treated market to one or more untreated markets (e.g., nearest-neighbor matching with caliper, or inverse probability weighting).
3. Assess balance: standardized mean differences and variance ratios for all pre-period covariates after matching/weighting. Report Love plots.
4. If balance cannot be achieved on key covariates, acknowledge this as a further threat to interpretability.

### Phase 3: Descriptive Difference-in-Differences

Estimate the conditional DiD specification:

\[
Y_{mt} = \alpha + \beta_1 \text{Post}_t + \beta_2 D_m + \tau (\text{Post}_t \times D_m) + \mathbf{X}_{m,\text{pre}}'\delta + \varepsilon_{mt}
\]

where:
- \(\text{Post}_t = 1\) in the intervention period, \(0\) in the pre-period.
- \(D_m = 1\) for treated (reduced/suspended paid search) markets.
- \(\mathbf{X}_{m,\text{pre}}\) is a vector of pre-period market characteristics (baseline sales level, pre-trend, market size proxies, user composition).
- \(\tau\) is the descriptive DiD coefficient.

Weight observations by the matching weights from Phase 2. Use cluster-robust standard errors at the market level.

**Interpret \(\tau\) strictly as a conditional associational estimate**, not a causal effect. The estimate describes how outcomes changed in treated markets relative to observably similar untreated markets, under the assumption that post-treatment divergence is attributable to the treatment — an assumption known to be questionable given endogenous assignment.

### Phase 4: Sensitivity Analysis for Unobserved Confounding

Since the identifying assumption is not credible, conduct structured sensitivity analyses:

- **Oster (2019) bounds**: Estimate how large the selection on unobservables would need to be, relative to selection on observables, to drive \(\tau\) to zero. Report \(\delta\) (the coefficient of proportionality) and the identified set.
- **Rosenbaum bounds for hidden bias** (if using matched pairs): Report the \(\Gamma\) value at which inference would be overturned for different significance levels.
- **Imbens (2003) sensitivity**: Parameterize the correlation between treatment assignment and potential outcomes and trace out how the estimated effect changes.
- **Altonji-Elder-Taber (2005) ratio**: Compare the coefficient movement upon adding controls to assess the likely importance of unobservables.

### Phase 5: Heterogeneity by User Segment

For segment-level analysis, estimate:

\[
Y_{mt}^s = \alpha^s + \beta_1^s \text{Post}_t + \beta_2^s D_m + \tau^s (\text{Post}_t \times D_m) + \mathbf{X}_{m,\text{pre}}^{s'}\delta^s + \varepsilon_{mt}^s
\]

for each segment \(s \in \{\text{less-active}, \text{already-active}, \text{new-to-firm}\}\).

The key descriptive pattern of interest is whether \(\tau^s\) differs materially across segments — i.e., whether the association between paid-search suspension and purchases is larger in magnitude for less-active users. However, segment membership itself may be correlated with unobserved market-level confounders, and the same sensitivity caveats apply.

---

## 10. Why the Design Is Not Credibly Causal

The design described above produces **descriptive associational estimates**, not causal effects. The reasons are:

1. **Selection on unobservables**: Managers' decisions incorporate private information (expected demand trajectories, operational constraints, budget pressures) not captured by \(\mathbf{X}_m\). No econometric technique can adjust for unobserved confounders without additional structure not present in this packet.

2. **Untestable parallel trends**: The standard DiD justification — that treated and untreated markets would have followed parallel outcome paths absent treatment — is an untestable assumption about counterfactual post-treatment outcomes. With endogenous assignment, there is no reason to believe this assumption holds.

3. **Spillover / SUTVA violation**: Users in treated markets may substitute to other channels (organic search, direct navigation) or to neighboring markets. This means the treatment effect for "reduced paid-search availability" does not isolate the incremental contribution of paid search but rather captures a bundle of substitution behaviors.

4. **No instrument**: The packet provides no source of exogenous variation in treatment assignment (no policy threshold, no budget exhaustion cutoff, no platform-level rule change, no natural experiment).

Sensitivity analyses (Oster bounds, Rosenbaum bounds) quantify how severe the unobserved confounding problem would need to be to overturn the estimates, but they do not resolve it. They are diagnostic tools, not identification strategies.

---

## 11. Required Assumptions

Even for the descriptive analysis, the following assumptions are required. Those marked with an asterisk are **not justified** by the packet.

| Assumption | Required for... | Status |
|---|---|---|
| **Conditional parallel trends*** | Interpreting \(\tau\) as a causal ATT | Not credible; violated by design |
| **No spillover / SUTVA*** | Isolating the effect to treated markets only | Likely violated; users can substitute across channels |
| **No anticipation effects** | Using pre-period outcomes as valid baseline | Plausible but should be tested |
| **Common support** | Valid propensity score comparisons | Testable; report overlap |
| **No time-varying confounders** | Attributing post-treatment divergence to treatment | Not credible; managers respond to evolving conditions |
| **Correct functional form** | Consistency of \(\tau\) | Standard; robustness to alternatives should be tested |
| **Stable unit composition** | Panel interpretation | Plausible if market boundaries are stable |

---

## 12. Statistical Model or Analysis Equation

**Primary specification (descriptive conditional DiD):**

\[
Y_{mt} = \alpha_m + \lambda_t + \tau (D_m \times \text{Post}_t) + \varepsilon_{mt}
\]

where \(\alpha_m\) are market fixed effects and \(\lambda_t\) are time fixed effects. The market fixed effects absorb time-invariant confounders (e.g., permanent market size differences). The time fixed effects absorb common macro shocks.

**Weighted variant:**

\[
Y_{mt} = \alpha_m + \lambda_t + \tau (D_m \times \text{Post}_t) + \varepsilon_{mt}, \quad \text{weighted by } w_m
\]

where \(w_m\) are inverse propensity score weights or entropy balancing weights.

**Event-study / dynamic specification:**

\[
Y_{mt} = \alpha_m + \lambda_t + \sum_{k \neq -1} \beta_k \mathbf{1}[t - t^*_m = k] + \varepsilon_{mt}
\]

where \(t^*_m\) is the period when paid-search availability changes for market \(m\). The coefficients \(\beta_k\) for \(k < 0\) serve as a **pre-trend falsification check**: if \(\beta_k \neq 0\) for \(k < 0\), pre-existing divergence between treated and control markets is present. Even if pre-trends are flat, this does not validate the parallel counterfactual-trends assumption, because managers could have selected markets that were *about to diverge* from controls for unobserved reasons.

**Segment heterogeneity specification:**

\[
Y_{mt}^s = \alpha_m^s + \lambda_t^s + \tau^s (D_m \times \text{Post}_t) + \varepsilon_{mt}^s
\]

estimated separately by segment \(s\), or pooled with segment-treatment interactions.

---

## 13. Robustness, Placebo, Falsification Checks, and Diagnostic Tests

### Falsification / Pre-trend Tests

1. **Event-study plot**: Estimate \(\beta_k\) for \(k\) periods before the intervention. Visual inspection for pre-existing divergence. If pre-trends differ, the conditional DiD estimate is even less defensible.
2. **Placebo treatment date**: Shift the pseudo-intervention date to an earlier period (before actual treatment). Re-estimate the DiD; a non-zero "effect" at the placebo date signals systematic pre-existing divergence.
3. **Placebo outcome**: Apply the same design to an outcome that should be unaffected by paid-search availability (e.g., sales in a product category not advertised via paid search). A non-zero "effect" on the placebo outcome signals unobserved confounding.

### Robustness Checks

4. **Alternative matching methods**: Replicate with coarsened exact matching (CEM), entropy balancing, and synthetic control methods (SCM) for each treated market. Report the range of estimates.
5. **Leave-one-out**: Iteratively drop one treated market and re-estimate to check for influential units.
6. **Alternative functional forms**: Log outcome, Poisson pseudo-maximum likelihood (PPML) for count outcomes, inverse hyperbolic sine.
7. **Varying the pre-period window**: Truncate the pre-period to different lengths to check sensitivity to the baseline window choice.
8. **Donut RD / threshold**: If any quasi-threshold exists in the selection rule (e.g., markets above/below a budget cutoff), test sensitivity around that threshold. However, the packet does not provide such a threshold.

### Diagnostic Tests

9. **Balance diagnostics**: Standardized mean differences, variance ratios, and Love plots for all pre-period covariates before and after matching/weighting.
10. **Overlap / common support**: Histograms or density plots of estimated propensity scores for treated and untreated markets. Trim or restrict to common support region.
11. **McCrary-type density test**: If any assignment threshold exists, test for manipulation of the running variable.

---

## 14. Heterogeneity Analysis (If Supportable)

Heterogeneity analysis is supportable **as a descriptive exercise**, subject to all the same caveats about confounding. The analysis examines whether the associational pattern between paid-search suspension and purchases differs across segments.

### User-History Segments

| Segment | Definition | Hypothesis |
|---|---|---|
| **New-to-firm** | No prior purchases in the pre-period | Paid search may be disproportionately important for discovery → larger negative association with suspension |
| **Less-active** | Low prior frequency or long recency (e.g., bottom tercile of purchase frequency, top tercile of days since last purchase) | Paid search may serve as a re-engagement channel → moderate association |
| **Already-active** | High prior frequency or short recency (e.g., top tercile of purchase frequency, bottom tercile of days since last purchase) | These users navigate directly or use bookmarks → weak or zero association (pure interception) |

### Estimation Approach

- Estimate the segment-specific DiD specification (Section 12).
- Test for equality of \(\tau^s\) across segments using a pooled model with segment-treatment-post triple interactions.
- **Critical caveat**: Segment composition itself may change differentially across treated and untreated markets post-intervention (compositional selection). If paid-search suspension causes some users to drop out of the observable purchase data entirely, segment-level comparisons are biased.

### Placebo Segment

If a user segment exists that should be entirely unaffected by paid search (e.g., users who exclusively purchase through a channel not connected to search — such as in-store-only customers, if separately identifiable), use this as a placebo outcome.

---

## 15. Measurement, Compliance, Missingness, Spillover, and Implementation Limits

| Issue | Severity | Mitigation |
|---|---|---|
| **Treatment is a market-level indicator, not individual exposure** | High | Interpret \(\tau\) as an intent-to-treat (ITT)-type associational parameter at the market level. Cannot recover individual-level treatment effects. |
| **Non-compliance / imperfect take-up** | Moderate–High | Users in "active" markets may still not see or click paid-search ads. Users in "suspended" markets may see ads through other devices, locations, or retargeting. The market-level indicator is a noisy proxy. |
| **Channel substitution (spillover)** | High | The outcome captures net purchases after any substitution across organic, direct, or other channels. The estimate cannot be interpreted as the pure incremental effect of paid search; it captures the *net* effect of reduced paid-search availability given substitution possibilities. |
| **Cross-market spillover** | Moderate | Users near market borders may search in neighboring markets. Without user-level geo-location data, this cannot be detected or corrected. |
| **Missingness** | Unknown | The packet does not describe missing data patterns. If treated markets are more likely to have incomplete outcome tracking (e.g., due to operational disruptions coinciding with the decision to suspend paid search), systematic missingness biases estimates. |
| **Segment classification** | Moderate | Pre-period activity segments are defined using historical data. If the pre-period length is short, segment classification may be noisy. Users may transition between segments over time. |
| **Time-varying confounders** | High | Markets may experience differential demand shocks, competitive entry, or platform algorithm changes during the intervention period that both affect outcomes and are correlated with managers' treatment decisions. |

---

## 16. Failure Modes and Alternative Explanations

Even if \(\tau\) (the conditional DiD estimate) is negative and statistically significant — suggesting that reducing paid-search availability is associated with lower purchases — the following alternative explanations are not ruled out:

1. **Reverse causality / simultaneous determination**: Managers reduced paid search in markets where demand was already softening for unrelated reasons. The negative \(\tau\) reflects the demand softening, not the causal effect of reduced paid search.

2. **Omitted variable bias from market-specific shocks**: A market-specific shock (e.g., competitor entry, local economic downturn, platform algorithm change) simultaneously depresses demand and triggers managers to reduce paid-search spending in that market.

3. **Regression to the mean**: If managers reduce paid search in markets with unusually high pre-period sales (expecting mean reversion), and those markets naturally revert downward, \(\tau\) captures regression to the mean rather than a treatment effect.

4. **Ashenfelter's dip**: If pre-period outcomes in treated markets exhibit a temporary dip that triggers the treatment decision, and those markets naturally recover (even partially), \(\tau\) is biased.

5. **Compositional changes**: If paid-search suspension causes certain user types to stop purchasing from the firm entirely (rather than switching channels), the observed segment-level outcomes reflect a selected sample of surviving purchasers, not the population-level effect for that segment.

6. **Spillover as an offset**: Users in treated markets may increase organic-search or direct-navigation purchases, partially or fully offsetting the reduction in paid-search-mediated purchases. A near-zero \(\tau\) does not demonstrate that paid search has no incremental effect — it may reflect complete substitution.

7. **Simultaneous operational changes**: The decision to suspend paid search may coincide with other operational or marketing changes (e.g., staff reassignment, budget reallocation to other channels) that independently affect outcomes.

---

## 17. What Cannot Be Claimed

The following claims **cannot be made** from the available data and variation:

1. ✗ **"Paid-search availability causes an X% increase in purchases."** The design does not support causal attribution.

2. ✗ **"The incremental effect of paid search is Y% and the remaining Z% is cannibalization."** Separating incremental from interceptive effects requires individual-level randomization of ad exposure (or a valid instrument), not available here.

3. ✗ **"The effect is larger for less-active users."** While segment-level associational patterns can be described, segment membership is not randomly assigned and may be correlated with unobserved determinants of both treatment and outcomes.

4. ✗ **"Reducing paid-search spend by $X reduces revenue by $Y."** The estimates are associational and confounded; they should not be used for ROI or budget-allocation decisions.

5. ✗ **"The estimated effect generalizes to other markets or time periods."** External validity is compromised by the non-random selection of treated markets.

---

## 18. Additional Data Needed

To upgrade from descriptive associational evidence to credible causal identification, at least one of the following would be required:

| Data or Design Element | What It Would Enable |
|---|---|
| **Pre-committed experimental rule or randomization** | Restores orthogonal treatment assignment → validates parallel trends → supports causal DiD or simple treatment-control comparison |
| **A valid instrument for paid-search availability** (e.g., auction-price variation from platform-side keyword bidding shocks, budget-exhaustion timing driven by unrelated campaign mechanics, platform policy changes affecting some markets but not others) | Instrumental variables (IV) estimation → recovers local average treatment effect (LATE) for complier markets |
| **A sharp geographic or administrative boundary with differential paid-search policy** | Regression discontinuity design |
| **Detailed manager decision protocols and real-time demand forecasts** | Allows explicit modeling of the selection process (e.g., Heckman selection model, though this requires a valid exclusion restriction) |
| **Individual-level ad-exposure data with random or as-good-as-random assignment** | Enables individual-level causal inference about ad exposure, bypassing the market-level aggregation problem |
| **Long pre-period with multiple treatment timing** | Enables staggered DiD / event-study designs with the Callaway-Sant'Anna or Sun-Abraham estimators (but does not itself solve the endogeneity of treatment timing) |
| **A/B test or holdout design, even if at smaller scale** | Provides a causally identified benchmark against which observational estimates can be validated or calibrated |

---

## 19. Threat-Response Table

| Threat | Severity | Detection Strategy | Response / Mitigation |
|---|---|---|---|
| **Endogenous treatment selection (selection on unobservables)** | Critical | Phase 1 selection analysis; compare treated vs. untreated pre-period characteristics | Sensitivity analysis (Oster bounds, Rosenbaum bounds); transparent downgrading of claims to associational |
| **Divergent pre-trends** | High | Event-study plots; placebo treatment date | If present, the descriptive DiD is further compromised; report and acknowledge |
| **Channel substitution / spillover** | High | Supplemental analysis of organic-search and direct-navigation traffic if available; placebo outcome tests | Interpret \(\tau\) as net effect inclusive of substitution; do not claim to isolate paid-search incrementality |
| **Compositional selection in segment analysis** | Moderate–High | Track user counts by segment over time; check for differential attrition | If attrition is differential, segment-level estimates are biased; caveat prominently |
| **Time-varying market-specific shocks** | High | Placebo outcomes; analysis of market-level economic indicators | Cannot be eliminated; acknowledge as a limitation |
| **Regression to the mean / Ashenfelter's dip** | Moderate | Examine pre-period outcome paths in detail; test for asymmetry in pre-trend | If present, control for pre-period outcome level and trend; report sensitivity |
| **Simultaneous operational changes** | Moderate | Interview managers; collect data on other contemporaneous marketing or operational actions | Cannot be eliminated without additional data; acknowledge as a limitation |
| **Weak overlap / poor common support** | Moderate | Propensity score distributions; trimming | Restrict analysis to common support region; acknowledge reduced external validity |
| **Noisy treatment measure (market-level indicator ≠ individual exposure)** | Moderate | If click or impression data available, report first-stage relationship | Interpret as ITT-type associational parameter at market level; do not claim individual-level effects |

---

## 20. Claim-Evidence Table

| # | Claim | Evidence Used | Claim Type | Confidence | What Would Falsify This Claim |
|---|---|---|---|---|---|
| 1 | Paid-search availability is associated with downstream purchases in the expected direction | Conditional DiD estimate \(\tau\) from matched/weighted specification, with cluster-robust inference | Descriptive / Associational | Low (due to unobserved confounding) | \(\tau\) is statistically indistinguishable from zero across specifications; sensitivity bounds include zero under modest unobserved confounding |
| 2 | The association between paid-search availability and purchases differs across user-history segments | Segment-specific \(\tau^s\) estimates; formal test of equality | Descriptive / Associational | Low–Moderate | Segment-specific estimates are statistically indistinguishable; the pattern reverses under alternative segment definitions |
| 3 | Pre-existing trends do not differ between treated and untreated markets on observables | Event-study pre-period coefficients \(\beta_k \approx 0\) for \(k < 0\) | Diagnostic / Descriptive | Moderate (for observable trends only; says nothing about unobservable counterfactual trends) | Pre-period event-study coefficients are jointly significant and economically meaningful |
| 4 | Treated and untreated markets are balanced on observable pre-period characteristics after matching/weighting | Standardized mean differences < 0.1–0.25; variance ratios near 1; Love plots | Diagnostic / Descriptive | Moderate | Large post-matching imbalances remain on key covariates; no adequate common support |
| 5 | The observed association is robust to reasonable unobserved confounding | Oster \(\delta\) bounds; Rosenbaum \(\Gamma\) sensitivity | Sensitivity Analysis | Inherently uncertain (these bounds are calibration tools, not causal tests) | The identified set includes zero under plausible values of \(\delta\) or \(\Gamma\) |
| 6 | Reducing paid-search availability causes a change in downstream purchases | Any of the above | Causal | **Not supported** — this claim cannot be made from the available data | N/A — the claim itself is not falsifiable with the available evidence because the design cannot support it |

---

## Summary Assessment

The perturbed condition — replacing exogenous treatment assignment with discretionary manager decisions — fundamentally breaks the identification logic that would support a credible causal claim. The packet does not provide any instrument, discontinuity, or other source of exogenous variation that could restore causal identification. The strongest defensible empirical contribution is a **transparently reported descriptive associational analysis** with structured sensitivity diagnostics, event-study pre-trend visualizations, and careful covariate balance reporting. The key output is not a single estimate but a body of evidence that documents (a) how treatment was assigned, (b) what observable differences exist between treated and untreated markets, (c) what associational patterns emerge after matching/weighting, and (d) how sensitive those patterns are to plausible unobserved confounding. The analysis should conclude not with a causal claim but with a clear statement of what additional data or design variation would be required to make causal claims defensible.

## Tool Log Summary

- actual tool use: none
- trajectory `toolMetas`: []
- toolCall count: 0
- toolResult count: 0
- session_id: isolated_20260527_224310_98725_10
- session_log: /Users/jiangcanxiang/.openclaw/agents/benchmark_isolated/sessions/isolated_20260527_224310_98725_10.jsonl
- trajectory_log: /Users/jiangcanxiang/.openclaw/agents/benchmark_isolated/sessions/isolated_20260527_224310_98725_10.trajectory.jsonl

## Operator Notes

- duration_ms: 249872
- stderr_excerpt: [plugins] plugins.allow is empty; discovered non-bundled plugins may auto-load: qqbot (/Users/jiangcanxiang/.openclaw/npm/node_modules/@openclaw/qqbot/dist/index.js), openclaw-weixin (/Users/jiangcanxiang/.openclaw/npm/node_modules/@tencent-weixin/openclaw-weixin/dist/index.js). Set plugins.allow to explicit trusted ids. [skills] Skipping escaped skill path outside its configured root: source=openclaw-managed root=~/.openclaw/skills reason=symlink-escape requested=~/.openclaw/skills/0-autoresearch-skill resolved=~/.orchestra/skills/0-autoresearch-skill [skills] Skipping escaped skill path outside its configured root: source=openclaw-managed root=~/.openclaw/skills reason=symlink-escape requested=~/.openclaw/skills/brainstorming-research-ideas resolved=~/.orchestra/skills/21-research-ideation/brainstorming-research-ideas [skills] Skipping escaped skill path outside its configured root: source=openclaw-managed root=~/.openclaw/skills reason=symlink-escape requested=~/.openclaw/skills/creative-thinking-for-research resolved=~/.orchestra/skills/21-research-ideation/creative-thinking-for-research [skills] Skipping escaped skill path outside its configured root: source=openclaw-managed r
