# Raw Agent Run Log

- `run_id`: RUN_20260527_224724_11_openclaw_deepseekv4pro_isolated
- `case_id`: C005
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
- `timestamp`: 2026-05-27T22:47:24+0800
- `input_file`: benchmark/cases/C005_online_ad_measurement/agent_task_level2.md
- `system_prompt_summary`: workspace=/Users/jiangcanxiang/OpenClawBenchmarkIsolated; thinking=high; actual_tool_use=none; agent=benchmark_isolated
- `contamination_status`: unknown
- `contamination_reason`: pending manual content review; actual tool use=none
- `status`: success

## Raw Agent Output

# Research Design: Measuring the Causal Effect of Digital Ad Exposure Under Platform-Mediated Delivery

---

## 1. Executive Summary

This design addresses the fundamental tension in digital advertising measurement: platform delivery systems optimize ad serving, so users who actually receive impressions differ systematically from those who do not. The packet provides a two-layer structure—campaign-level randomization or holdout assignment (*Stage 2*) plus platform-mediated actual delivery (*Stage 3*)—that creates a path to credible causal identification. The core insight is that assignment can serve as a source of exogenous variation in exposure, even though exposure itself is selected. I propose an encouragement-design framework: the estimand of interest is the effect of actual ad exposure for the subpopulation whose exposure status is shifted by assignment (compliers). The design yields two defensible causal quantities: (a) the intention-to-treat (ITT) effect of campaign assignment on downstream outcomes, and (b) the complier-average causal effect (CACE) of actual exposure, identified under an exclusion restriction and monotonicity. I also specify the descriptive analyses that remain credible when IV assumptions are strained, the robustness checks needed, and the claims that the data cannot sustain.

---

## 2. Research Question

What is the causal effect of actual digital ad exposure on downstream user conversions (visits, registrations, purchases, or revenue), in a setting where the platform's delivery algorithm selects which eligible users receive impressions?

Refined sub-questions:
- What is the effect of *being assigned or made eligible* for the campaign (the ITT)?
- What is the effect of *actually receiving* the focal ad impression, for users whose exposure status responds to assignment?
- How much of any observed association between exposure and conversions is attributable to platform selection rather than to the ad itself?

---

## 3. Target Estimand (or Strongest Defensible Estimand)

### Primary Causal Estimand

**Intention-to-Treat (ITT):** The average effect of campaign assignment (or eligibility) on the downstream conversion outcome, over all users assigned or made eligible.

\[
\tau_{\text{ITT}} = E[Y_i(1) - Y_i(0) \mid \text{assigned/eligible}]
\]

where \(Y_i(1)\) is the potential outcome under assignment and \(Y_i(0)\) is the potential outcome under non-assignment.

This estimand is directly identified from the randomization or holdout structure described in Stage 2. It does not require assumptions about exposure mechanisms and is the most robust causal quantity available.

### Secondary Causal Estimand

**Complier-Average Causal Effect (CACE) / Local Average Treatment Effect (LATE):** The effect of actual ad exposure for the subpopulation of users whose exposure status is determined by assignment—i.e., users who would receive the ad if assigned/eligible but would not receive it if unassigned/ineligible.

\[
\tau_{\text{CACE}} = E[Y_i(1) - Y_i(0) \mid \text{complier}]
\]

where compliers are users for whom \(D_i(1) = 1\) and \(D_i(0) = 0\), with \(D_i(z)\) denoting actual exposure under assignment status \(z\).

This estimand is identified under the standard IV assumptions (detailed in Section 11). It is more policy-relevant than the ITT for questions about the ad's effect among users who can actually be reached, but rests on stronger assumptions.

### Estimand That Is NOT Credibly Identified

The **Average Treatment Effect on the Treated (ATT)** or the **population Average Treatment Effect (ATE)** of actual exposure are not identified without additional assumptions that are unsupported by the data in this packet. Always-takers (users who would receive the ad regardless of assignment) and never-takers (users who would never receive it) have exposure status that is determined entirely by platform selection, and no experimental variation identifies the counterfactual for these groups.

---

## 4. Treatment/Exposure and Main Outcomes

| Role | Variable | Measurement Level |
|---|---|---|
| **Instrument (Z)** | Campaign assignment or eligibility indicator (binary) | User-level, from randomization or holdout logs |
| **Endogenous treatment (D)** | Actual focal-ad exposure (binary: ≥1 impression) | User-level, aggregated from opportunity-level delivery logs |
| **Alternative treatment** | Exposure frequency (count of impressions) | User-level |
| **Primary outcome (Y)** | Downstream conversion (binary: visit/registration/purchase within attribution window) | User-level |
| **Secondary outcome** | Revenue or purchase value (continuous, if observed) | User-level |
| **Secondary outcome** | Intermediate engagement events | User or opportunity level |

The user-level aggregation of exposure to a binary indicator (ever-exposed vs. never-exposed) is the recommended primary treatment definition because it maps cleanly onto the binary instrument. Continuous exposure intensity (impression count) can be analyzed as a secondary specification but requires stronger assumptions.

---

## 5. Data Structure Summary

The data follow a four-stage structure:

```
Stage 1: Eligibility ──→ Stage 2: Assignment/Randomization ──→
Stage 3: Platform Delivery ──→ Stage 4: Outcome Observation
```

| Dimension | Description |
|---|---|
| **Unit** | User-ad-opportunity at the finest grain; aggregated to user for analysis |
| **Time** | Campaign delivery window + post-exposure attribution window |
| **Assignment source** | Higher-level randomization or holdout (Stage 2) |
| **Selection source** | Platform auctions, targeting, pacing, optimization (Stage 3) |
| **Treatment variables** | Z: assignment/eligibility; D: actual exposure; opportunity indicators |
| **Outcome variable** | Y: downstream conversion within attribution window |
| **Covariates** | Pre-campaign activity, device/channel, geography, time, relevance scores |
| **Panel structure** | Users may appear in multiple opportunities; repeated exposure possible |
| **Clustering** | User-level (primary); campaign-cell or time-cell (secondary) |
| **Missingness** | Tracking loss, cross-device behavior, identifier churn |
| **Spillover** | Possible via other channels, social sharing, market saturation |

---

## 6. Relevant Causal Mechanisms

The packet identifies four mechanisms that must be distinguished. I map each to its implications for identification:

### Mechanism 1: Selection on Baseline Demand
*Users who receive impressions have higher baseline purchase intent.*

**Implication:** Naive comparison of exposed vs. unexposed users confounds the ad effect with pre-existing differences. This is the standard selection problem. The randomization-based design addresses this by using assignment, not realized exposure, as the source of variation.

### Mechanism 2: Platform Sorting Under Experiment
*Even under randomization, platform delivery rules sort different user types into exposure.*

**Implication:** This is precisely why D (actual exposure) is endogenous even when Z (assignment) is randomized. The sorting creates the compliance structure: always-takers, never-takers, compliers, and defiers. Monotonicity (no defiers) is needed for CACE identification. If the platform's algorithm systematically denies the ad to certain user types even when they are assigned, these users are never-takers and their treatment effect is not identified.

### Mechanism 3: Assignment Affects Opportunity Without Guaranteeing Exposure
*Campaign assignment can affect eligibility or opportunity without guaranteeing actual exposure.*

**Implication:** This is the first-stage relationship. A weak first stage (assignment barely shifts exposure probability) makes the IV design fragile. The design must document the first-stage F-statistic and assess whether the instrument is sufficiently strong.

### Mechanism 4: Measurement Depends on Tracking Systems
*Measured conversions depend on tracking systems as well as on real behavior.*

**Implication:** The outcome is \(Y^* = Y \cdot R + (1-R) \cdot 0\), where R is a tracking indicator. If tracking probability differs by assignment or exposure status, the estimand is contaminated by measurement error that is differential. This cannot be fully resolved without auxiliary data on tracking coverage.

---

## 7. Main Identification Challenge

The central challenge is that the platform delivery algorithm creates a **non-ignorable selection process** between assignment and actual exposure. Formally:

\[
E[Y_i \mid D_i = 1] - E[Y_i \mid D_i = 0] = \underbrace{E[Y_i(1) - Y_i(0) \mid D_i = 1]}_{\text{ATT (causal)}} + \underbrace{\{E[Y_i(0) \mid D_i = 1] - E[Y_i(0) \mid D_i = 0]\}}_{\text{selection bias}}
\]

The selection bias term is positive if the platform's optimization successfully identifies users with higher baseline conversion propensity. The naive difference overstates the causal effect.

The randomization in Stage 2 addresses this by providing an instrument Z that is:
- **As-good-as-randomly assigned** (by design of the holdout or randomization)
- **Relevant** (affects the probability of actual exposure)
- **Plausibly excludable** (affects outcomes only through its effect on exposure opportunity)

The identification challenge reduces to: *Is the exclusion restriction credible, and is the first stage strong enough?*

---

## 8. Whether Credible Causal Identification Is Possible

**Yes, credible causal identification is possible for two estimands:**

1. **The ITT effect of assignment on outcomes** is credibly identified directly from the randomization or holdout, requiring only that the assignment mechanism is as-good-as-random and that assignment does not affect outcomes through channels other than campaign exposure opportunity (partial exclusion). This is the most defensible causal claim.

2. **The CACE/LATE of actual exposure among compliers** is identified under the additional assumptions of (a) the full exclusion restriction, (b) monotonicity, and (c) a non-zero first stage. Whether these assumptions are credible depends on institutional details about the platform's delivery rules—details that are partially available (we know randomization exists) but not fully specified in this packet.

**Causal identification is NOT credible for:**
- The ATE or ATT of actual exposure in the full population
- The effect for always-takers or never-takers
- The effect of exposure intensity (multiple impressions vs. one) without additional structure

---

## 9. Proposed Empirical Design

### Design Framework

I propose a design that leverages the two-layer structure (randomized assignment + platform-mediated delivery) as an **encouragement design** where assignment serves as an instrument for actual exposure.

### Step 1: Document the Assignment Mechanism

Before any causal analysis, characterize:
- How assignment is determined (randomization seed, hash-based, time-based holdout)
- The unit of assignment (user, cookie, device, or ad opportunity)
- The assignment ratio (e.g., treatment:control split)
- Whether assignment is cross-cutting with other campaigns or isolated

**Rationale:** The validity of the ITT depends entirely on the integrity of the assignment mechanism. Documenting it is the first line of defense against confounded assignment.

### Step 2: Balance and Covariate Checks

Test whether pre-campaign covariates are balanced across assignment arms:

\[
X_i = \alpha + \beta Z_i + \varepsilon_i
\]

For each pre-campaign covariate, test \(H_0: \beta = 0\). Report standardized differences. If imbalance is detected, the randomization may be compromised, and the design reduces to a selection-on-observables analysis (which is weaker).

### Step 3: Intention-to-Treat (ITT) Analysis

Estimate the reduced-form effect of assignment on outcomes:

\[
Y_i = \alpha + \tau_{\text{ITT}} Z_i + \gamma' X_i + \varepsilon_i
\]

- Cluster standard errors at the user level (or at the assignment-unit level if assignment is at a coarser grain).
- \(\tau_{\text{ITT}}\) is the average effect of being assigned/eligible for the campaign, regardless of whether the ad was actually served.
- This is the most defensible causal estimate. It answers: "What did the campaign achieve, accounting for the fact that the platform may not deliver to everyone assigned?"

### Step 4: First-Stage Analysis

Estimate the effect of assignment on actual exposure:

\[
D_i = \alpha + \pi Z_i + \gamma' X_i + \varepsilon_i
\]

- Report the first-stage coefficient \(\pi\) and the Kleibergen-Paap F-statistic.
- If \(F < 10\), the instrument is weak; the CACE is not reliably identified, and only the ITT is credible.
- Document the compliance classes implied by the data: proportion always-takers (\(D_i = 1\) when \(Z_i = 0\)), never-takers (\(D_i = 0\) when \(Z_i = 1\)), and compliers.

### Step 5: Complier-Average Causal Effect (CACE)

If the first stage is strong and monotonicity is plausible, estimate:

\[
\tau_{\text{CACE}} = \frac{\tau_{\text{ITT}}}{\pi} = \frac{E[Y_i \mid Z_i = 1] - E[Y_i \mid Z_i = 0]}{E[D_i \mid Z_i = 1] - E[D_i \mid Z_i = 0]}
\]

This is the Wald estimator. In a regression framework, this is equivalent to two-stage least squares (2SLS):

First stage: \(D_i = \alpha_1 + \pi Z_i + \gamma_1' X_i + \varepsilon_{1i}\)
Second stage: \(Y_i = \alpha_2 + \tau_{\text{CACE}} \hat{D}_i + \gamma_2' X_i + \varepsilon_{2i}\)

The CACE interpretation is: the average effect of actual ad exposure for compliers—users who would receive the ad if assigned but not if unassigned.

### Step 6: Characterize Compliers

Profile the complier subpopulation by estimating the relative likelihood that users with covariate value \(X = x\) are compliers vs. the full population. This uses the approach of estimating:

\[
P(\text{complier} \mid X = x) \propto P(D = 1 \mid Z = 1, X = x) - P(D = 1 \mid Z = 0, X = x)
\]

This tells us *to whom the CACE applies*, which is essential for external validity and business interpretation.

---

## 10. Why the Design Is Valid (or Why Causal Identification Is Not Credible)

### Why the ITT Is Valid

The ITT is valid because assignment Z is randomized (or determined by a holdout mechanism that is as-good-as-random). The only threat to the ITT is that Z affects Y through channels other than campaign exposure opportunity. Since Z is an administrative assignment to a campaign cell, this threat is limited—though it could arise if assignment affects platform behavior in other ways (e.g., the platform suppresses other ads for the holdout group). This must be checked empirically.

### Why the CACE Is Valid (Conditional on Assumptions)

The CACE is valid under the IV assumptions (Section 11). The key threats are:
1. **Weak instrument:** If the first-stage F-statistic is low, the CACE estimate is biased toward the OLS estimate, and standard errors are misleading.
2. **Violation of exclusion:** If assignment affects outcomes through channels other than the focal ad (e.g., through other platform treatments correlated with assignment), the CACE is biased.
3. **Violation of monotonicity:** If some users are *less* likely to receive the ad when assigned (defiers), the CACE is not identified. This is unlikely in standard holdout designs but possible if assignment triggers platform pacing adjustments that reduce delivery probability for some users.

### Why the ATE/ATT Are Not Credible

Always-takers and never-takers have exposure status that is determined by platform selection alone. No experimental variation identifies the counterfactual for these groups. Extrapolating from compliers to the full population requires an assumption of treatment effect homogeneity that is unsupported and implausible given the selection mechanisms described in the packet.

---

## 11. Required Assumptions

### For the ITT

| # | Assumption | Justification |
|---|---|---|
| A1 | **Random assignment:** Z is independent of potential outcomes \((Y_i(0), Y_i(1))\) | Supported by the randomization/holdout structure in Stage 2 |
| A2 | **Stable unit treatment value (SUTVA):** One user's assignment does not affect another user's outcomes | Questionable given possible spillover (see Section 15); partially testable |
| A3 | **No differential attrition:** Outcome measurement is not differentially missing by assignment status | Testable; if violated, bounds analysis is needed |

### For the CACE (in addition to A1–A3)

| # | Assumption | Justification |
|---|---|---|
| A4 | **Relevance:** \(P(D_i=1 \mid Z_i=1) \neq P(D_i=1 \mid Z_i=0)\) | Empirically testable via first-stage F-statistic |
| A5 | **Exclusion restriction:** Z affects Y only through its effect on D | The strongest and least testable assumption; requires that assignment does not change outcomes through other channels (e.g., other platform treatments, user awareness of assignment) |
| A6 | **Monotonicity:** \(D_i(1) \geq D_i(0)\) for all i (no defiers) | Plausible in a holdout design where assignment expands eligibility; must be argued from platform delivery rules |

---

## 12. Statistical Model or Analysis Equation

### Primary ITT Specification

\[
Y_i = \beta_0 + \tau_{\text{ITT}} Z_i + \mathbf{X}_i' \boldsymbol{\beta} + \varepsilon_i
\]

where:
- \(Y_i\): binary conversion outcome for user \(i\)
- \(Z_i\): binary assignment/eligibility indicator
- \(\mathbf{X}_i\): vector of pre-campaign covariates (improves precision; not required for consistency)
- \(\varepsilon_i\): error term, clustered at user level
- \(\tau_{\text{ITT}}\): the ITT effect (causal under assumptions A1–A3)

Estimation: OLS (linear probability model) for binary outcomes, with cluster-robust standard errors at the user level. Logistic regression with marginal effects as a robustness check.

### First Stage

\[
D_i = \alpha_0 + \pi Z_i + \mathbf{X}_i' \boldsymbol{\alpha} + \nu_i
\]

- \(\pi\): effect of assignment on exposure probability (compliance rate)
- Report Kleibergen-Paap F-statistic for weak instrument diagnostics

### IV/2SLS Specification (CACE)

\[
\begin{aligned}
D_i &= \alpha_0 + \pi Z_i + \mathbf{X}_i' \boldsymbol{\alpha} + \nu_i \quad &\text{(First stage)} \\
Y_i &= \beta_0 + \tau_{\text{CACE}} \hat{D}_i + \mathbf{X}_i' \boldsymbol{\beta} + \varepsilon_i \quad &\text{(Second stage)}
\end{aligned}
\]

where \(\hat{D}_i\) is the predicted exposure from the first stage. Standard errors must account for the generated regressor; use 2SLS with cluster-robust standard errors.

### Wald Estimator (Equivalent, Without Covariates)

\[
\hat{\tau}_{\text{CACE}} = \frac{\bar{Y}_{Z=1} - \bar{Y}_{Z=0}}{\bar{D}_{Z=1} - \bar{D}_{Z=0}}
\]

### For Binary Outcome-Binary Endogenous Treatment

If both Y and D are binary, consider bivariate probit with an instrumental variable or the Abadie (2003) kappa-weighting approach for LATE with covariates.

---

## 13. Robustness, Placebo, Falsification Checks, and Diagnostic Tests

### Pre-Treatment Balance Checks

| Check | Method | What Would Raise Concern |
|---|---|---|
| Covariate balance | Regress each pre-campaign covariate on Z; report standardized differences | Any standardized difference > 0.1 SD or significant at p < 0.05 after multiple-testing correction |
| Pre-campaign outcome trends | Compare pre-period conversion rates by Z | Significant difference suggests non-random assignment or differential selection |
| Joint orthogonality | F-test of all covariates jointly predicting Z | Rejection of null of no relationship |

### Placebo / Falsification Tests

1. **Pre-period outcome test:** Regress pre-campaign conversion outcomes on Z. If Z predicts pre-period outcomes, assignment is not as-good-as-random or exclusion is violated.

2. **Placebo outcome test:** Identify an outcome that should NOT be affected by the ad (e.g., activity on a different product category, or during hours when the campaign is not running). If Z predicts this outcome, the exclusion restriction may be violated.

3. **False treatment timing:** Shift the campaign window earlier and test whether "assignment" in the pre-period predicts outcomes. A null result supports the validity of the design.

4. **Donut-hole analysis:** Exclude observations near the assignment boundary or near the campaign start/end to test sensitivity to edge cases.

### IV-Specific Diagnostics

| Diagnostic | Method | Threshold for Concern |
|---|---|---|
| First-stage strength | Kleibergen-Paap F-statistic | F < 10 (Stock-Yogo) |
| Overidentification (if multiple instruments from assignment strata) | Sargan/Hansen J-test | p < 0.05 |
| Weak-instrument robust inference | Anderson-Rubin confidence set, or LIML | Compare to 2SLS; large divergence indicates weak-instrument bias |
| Sensitivity to exclusion violation | Conley, Hansen, Rossi (2012) "plausibly exogenous" bounds | Assess how large a direct effect of Z on Y would need to be to nullify the result |

### Attrition and Missingness Checks

| Check | Method |
|---|---|
| Differential outcome missingness by Z | Regress missingness indicator on Z |
| Bounds under non-random attrition | Lee (2009) bounds; Horowitz-Manski bounds |
| Sensitivity to tracking loss | Compare results using different attribution windows |

---

## 14. Heterogeneity Analysis (If Supportable)

Heterogeneity analysis is supportable for the ITT (since Z is randomized) and, with appropriate methods, for the CACE (since complier status interacts with covariates).

### ITT Heterogeneity

\[
Y_i = \beta_0 + \tau Z_i + \delta Z_i \times W_i + \eta W_i + \mathbf{X}_i' \boldsymbol{\beta} + \varepsilon_i
\]

where \(W_i\) is a pre-specified moderator:
- **Pre-campaign activity terciles:** Does the campaign affect high-activity users differently?
- **Device/channel:** Mobile vs. desktop; different ad formats
- **Broad geography or market segment:** Regional variation in baseline conversion rates
- **Time of eligibility:** Early vs. late in the campaign window

**Important caveat:** Heterogeneity in the ITT conflates heterogeneity in the first stage (compliance) with heterogeneity in the CACE. A larger ITT in a subgroup could mean either a larger treatment effect or higher compliance. The CACE can be estimated within subgroups using separate first stages, but this requires sufficient within-subgroup compliance.

### CACE Heterogeneity

If compliance varies across subgroups, estimate subgroup-specific Wald estimators or interacted IV:

\[
\begin{aligned}
D_i &= \alpha_0 + \pi_1 Z_i + \pi_2 Z_i \times W_i + \eta W_i + \mathbf{X}_i' \boldsymbol{\alpha} + \nu_i \\
Y_i &= \beta_0 + \tau_1 \hat{D}_i + \tau_2 \hat{D}_i \times W_i + \eta W_i + \mathbf{X}_i' \boldsymbol{\beta} + \varepsilon_i
\end{aligned}
\]

This requires that the instrument is strong within each subgroup. If not, heterogeneity analysis should be restricted to the ITT.

### Multiple Testing

Apply the Benjamini-Hochberg false discovery rate correction across all heterogeneity tests. Pre-register the heterogeneity dimensions to avoid p-hacking.

---

## 15. Measurement, Compliance, Missingness, Spillover, and Implementation Limits

### Measurement Error in Exposure

Actual exposure may be measured with error:
- **Impression tracking:** Ad servers may count an impression even if the ad was not viewable (below the fold, rendered off-screen).
- **Cross-device exposure:** A user may see the ad on one device but convert on another, making the exposure-conversion link incomplete.
- **Ad blocking:** Some impressions are blocked and unobserved.

**Implication for ITT:** Measurement error in D does not affect the ITT (which uses only Z and Y). **Implication for CACE:** Classical measurement error in D attenuates the first-stage coefficient and biases the CACE away from zero. Non-classical error (e.g., differential by user type) introduces unknown bias.

### Compliance Structure

The packet notes that assignment does not guarantee exposure. The compliance rate (first-stage coefficient \(\pi\)) is a critical parameter. If \(\pi\) is small (e.g., < 0.05), the CACE is imprecisely estimated and the complier subpopulation may be a small, unrepresentative slice of users.

### Missing Outcomes

| Type | Mechanism | Mitigation |
|---|---|---|
| Tracking loss | Cookie deletion, cross-device, identifier churn | Sensitivity analysis using different attribution windows; bounds analysis |
| Differential tracking | Assignment may affect user behavior in ways that change tracking probability | Compare tracking rates by Z; Lee bounds if differential |
| Censoring | Outcome window may be too short to capture delayed conversions | Vary the attribution window; survival analysis for time-to-conversion |

### Spillover and Interference

The packet flags possible spillover via other channels, social sharing, or market saturation. Under SUTVA violations:
- The ITT estimates a *total* effect that includes spillover effects on the control group, which may attenuate or inflate the estimate depending on the direction of spillover.
- If spillover is substantial, the ITT may be biased toward zero (if treatment lifts control-group outcomes) or away from zero (if treatment displaces control-group activity).

**Partial mitigation:** If there is geographic or temporal clustering in assignment, test for SUTVA violations by comparing outcomes in control units with low vs. high treatment density in their cluster. This requires variation in treatment saturation, which may or may not be available.

### Repeated Exposure

Users can receive multiple impressions. The binary exposure definition (any vs. none) avoids the dimensionality problem but discards information. If the design uses assignment as an instrument for binary exposure, the CACE is the effect of any exposure (vs. none). The effect of incremental impressions requires a separate design (e.g., multiple instruments from variation in assignment intensity, or a dose-response model with stronger assumptions).

---

## 16. Failure Modes and Alternative Explanations

| Failure Mode | How It Would Manifest | Mitigation |
|---|---|---|
| **Weak instrument** | Large standard errors on CACE; 2SLS biased toward OLS; first-stage F < 10 | Report weak-instrument-robust confidence sets (Anderson-Rubin); default to ITT as primary result |
| **Exclusion violation** | Z affects Y through channels other than D | Placebo tests on outcomes that should not respond; sensitivity analysis using plausibly exogenous methods |
| **Defiers (monotonicity violation)** | The Wald estimator no longer identifies a weighted average of treatment effects | Argue from platform mechanics why defiers are implausible; if indefensible, CACE is not identified |
| **Differential attrition** | Missing outcome rates differ by Z | Lee bounds; report ITT with complete-case and imputed analyses |
| **SUTVA violation** | Outcomes in the control group are contaminated by treatment-group behavior | Test for dose-response in control-group outcomes by treatment density; if present, ITT is biased |
| **Anticipatory behavior** | Users learn about assignment before the campaign and change behavior | Test for pre-campaign outcome divergence by Z |
| **Platform adaptation** | The platform changes delivery rules in response to the experiment | Compare delivery patterns across assignment arms; if the platform treats assigned and unassigned users differently beyond the focal ad, exclusion may be violated |
| **Hawthorne effects** | Users aware of being in an experiment change behavior | Unlikely in passive digital ad settings, but possible if assignment involves visible changes (e.g., different ad frequency) |

---

## 17. What Cannot Be Claimed

1. **"The ad causes a X% lift in conversions for all users."** The CACE applies only to compliers. The ATE and ATT are not identified.

2. **"The treatment effect is the same for heavy users and light users."** Heterogeneity is estimable only for the ITT, and ITT heterogeneity confounds compliance heterogeneity with effect heterogeneity.

3. **"Each additional impression increases conversions by Y%."** The binary exposure design does not identify the marginal effect of incremental impressions. A dose-response claim requires additional modeling assumptions.

4. **"The ad is cost-effective with ROI of Z%."** This requires cost data (not in the packet) and an ATE or ATT estimate (not identified). The CACE for compliers can inform but not fully answer ROI questions.

5. **"There is no spillover or interference."** The packet explicitly flags possible spillover. The design can test for it but cannot rule it out without variation in treatment saturation.

6. **"Measurement error in outcomes is ignorable."** If tracking is differential by assignment or exposure, outcome measurement error is non-classical.

7. **"The effect persists beyond the attribution window."** The outcome window is finite. Long-term effects require longer observation, which may be complicated by repeated campaigns.

8. **"The results generalize to other campaigns, platforms, or time periods."** External validity is not addressed by this design. The complier population is specific to this campaign, this platform, and this time period.

---

## 18. Additional Data Needed

| Data Element | Why Needed | What It Would Enable |
|---|---|---|
| **Detailed assignment mechanism** (randomization seed, hash function, stratification variables) | To verify as-good-as-random assignment and conduct stratified analysis | Stronger balance tests; more precise ITT |
| **Platform delivery algorithm details** (auction mechanics, pacing rules, relevance thresholds) | To assess monotonicity and exclusion plausibility | More credible CACE; understanding of compliance classes |
| **Longer outcome window** | To assess whether effects decay or persist | Duration analysis; cumulative vs. instantaneous effects |
| **Cross-device identity graph or deterministic matching** | To reduce measurement error from cross-device behavior | More complete exposure-outcome linkage |
| **Cost data (CPM, CPC, total spend)** | To conduct cost-effectiveness analysis | ROI estimates (still bounded by CACE limitations) |
| **Competitor ad exposure or multi-advertiser data** | To assess SUTVA violations and substitution effects | Spillover analysis; category-level effects |
| **Multiple campaigns or variation in assignment intensity** | To estimate dose-response or multi-treatment effects | Marginal effect of incremental impressions; interaction effects across campaigns |
| **Pre-period data over a longer horizon** | To test parallel trends and rule out pre-existing divergence | Stronger falsification tests |
| **User-level tracking completeness indicators** | To model and correct for differential outcome measurement | Selection models or bounds for missing outcomes |
| **Granular geographic or network data** | To construct treatment-density instruments for spillover analysis | SUTVA violation tests; spillover-robust estimates |

---

## 19. Threat-Response Table

*(This section was not explicitly requested by the task packet. Omitted.)*

---

## 20. Claim-Evidence Table

| Claim | Evidence Used | Claim Type | Confidence | What Would Falsify This Claim |
|---|---|---|---|---|
| **C1:** Campaign assignment caused a change in downstream conversions of magnitude \(\tau_{\text{ITT}}\) | ITT estimate from randomization + outcome data; balance checks; pre-period falsification test | Causal (ITT) | High (conditional on valid randomization) | Pre-period outcome differences by Z; covariate imbalance; differential attrition by Z |
| **C2:** Actual ad exposure caused a change in conversions of magnitude \(\tau_{\text{CACE}}\) among compliers | Wald estimate (ITT / first stage); first-stage F-statistic; monotonicity argument | Causal (CACE) | Moderate to High (if first stage strong and exclusion plausible); Low (if first stage weak) | Weak first stage (F < 10); placebo test failure (Z predicts outcomes that should not respond); evidence of defiers |
| **C3:** The platform's delivery algorithm selects users with higher baseline conversion propensity | Comparison of exposed vs. unexposed in the assigned group; correlation of pre-campaign covariates with D conditional on Z | Descriptive / Mechanism | High | No correlation between pre-campaign activity and D conditional on Z |
| **C4:** The treatment effect is larger for high-activity users than low-activity users | ITT × pre-campaign activity interaction | Descriptive heterogeneity (ITT); suggestive for CACE | Moderate (ITT); Low (CACE without subgroup-specific first stages) | Null interaction; or subgroup-specific first stages showing the interaction is driven by compliance differences, not effect differences |
| **C5:** Exposure measurement error is non-differential by assignment | Comparison of tracking rates by Z | Diagnostic | Moderate | Significant difference in tracking rates by Z |
| **C6:** Spillover effects are negligible | Comparison of control-group outcomes by local treatment density | Diagnostic | Low to Moderate (depends on available variation in treatment density) | Control-group outcomes correlated with treatment density |
| **C7:** The campaign had no effect on outcomes that should be unrelated to the advertised product | Placebo outcome test | Falsification | High (for ruling out confounding); Low (for proving validity) | Significant ITT effect on placebo outcomes |
| **C8:** Results are robust to the choice of attribution window | Sensitivity analysis varying the outcome window | Robustness | Moderate | ITT effect changes sign or significance with different windows |
| **C9:** The complier subpopulation is demographically and behaviorally similar to the full eligible population | Complier profiling (covariate means weighted by compliance probability) | Descriptive | Moderate | Large standardized differences between complier-weighted and full-sample covariate means |
| **C10:** The exclusion restriction is approximately satisfied | Placebo tests; sensitivity analysis (Conley-Hansen-Rossi bounds) | Partial validation | Moderate | Placebo failures; bounds that include zero under small plausible violations |

---

### Summary of the Design Logic

The fundamental contribution of this design is to **separate what the randomization identifies (the ITT) from what requires additional, partially testable assumptions (the CACE)**. The ITT is the anchor—a credible causal quantity that answers "what did making users eligible for the campaign achieve?"—while the CACE answers the more policy-relevant question "what did actually seeing the ad do?" for the subset of users whose exposure is determined by assignment.

The design is strongest when:
1. The first stage is strong (high compliance rate)
2. Balance checks and placebo tests pass cleanly
3. The complier subpopulation is a substantively meaningful fraction of the eligible population
4. The exclusion restriction can be defended on institutional grounds

The design is weakest when the first stage is weak, in which case only the ITT is credible, and the business interpretation must be in terms of campaign assignment effects rather than ad exposure effects.

## Tool Log Summary

- actual tool use: none
- trajectory `toolMetas`: []
- toolCall count: 0
- toolResult count: 0
- session_id: isolated_20260527_224724_98725_11
- session_log: /Users/jiangcanxiang/.openclaw/agents/benchmark_isolated/sessions/isolated_20260527_224724_98725_11.jsonl
- trajectory_log: /Users/jiangcanxiang/.openclaw/agents/benchmark_isolated/sessions/isolated_20260527_224724_98725_11.trajectory.jsonl

## Operator Notes

- duration_ms: 207600
- stderr_excerpt: [plugins] plugins.allow is empty; discovered non-bundled plugins may auto-load: qqbot (/Users/jiangcanxiang/.openclaw/npm/node_modules/@openclaw/qqbot/dist/index.js), openclaw-weixin (/Users/jiangcanxiang/.openclaw/npm/node_modules/@tencent-weixin/openclaw-weixin/dist/index.js). Set plugins.allow to explicit trusted ids. [skills] Skipping escaped skill path outside its configured root: source=openclaw-managed root=~/.openclaw/skills reason=symlink-escape requested=~/.openclaw/skills/0-autoresearch-skill resolved=~/.orchestra/skills/0-autoresearch-skill [skills] Skipping escaped skill path outside its configured root: source=openclaw-managed root=~/.openclaw/skills reason=symlink-escape requested=~/.openclaw/skills/brainstorming-research-ideas resolved=~/.orchestra/skills/21-research-ideation/brainstorming-research-ideas [skills] Skipping escaped skill path outside its configured root: source=openclaw-managed root=~/.openclaw/skills reason=symlink-escape requested=~/.openclaw/skills/creative-thinking-for-research resolved=~/.orchestra/skills/21-research-ideation/creative-thinking-for-research [skills] Skipping escaped skill path outside its configured root: source=openclaw-managed r
