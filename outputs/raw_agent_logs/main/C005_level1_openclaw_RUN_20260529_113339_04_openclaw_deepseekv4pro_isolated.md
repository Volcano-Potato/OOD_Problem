# Raw Agent Run Log

- `run_id`: RUN_20260529_113339_04_openclaw_deepseekv4pro_isolated
- `case_id`: C005
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
- `timestamp`: 2026-05-29T11:33:39+0800
- `input_file`: benchmark/cases/C005_online_ad_measurement/agent_task_level1.md
- `system_prompt_summary`: workspace=/Users/jiangcanxiang/OpenClawBenchmarkIsolated; thinking=high; actual_tool_use=none; agent=benchmark_isolated
- `contamination_status`: unknown
- `contamination_reason`: pending manual content review; actual tool use=none
- `status`: success

## Raw Agent Output

# Research Design: Measuring the Causal Effect of Digital Advertising Exposure

---

## 1. Executive Summary

This design addresses the fundamental challenge of measuring the causal effect of digital ad exposure when platform delivery algorithms systematically select which users see impressions. The core insight is that **campaign eligibility (assignment)** and **actual ad exposure** are distinct treatments, and the design must treat them separately. The proposed strategy uses campaign-level randomization—where the researcher controls which users are *eligible* for the campaign—as an instrument for actual exposure in an instrumental variables (IV) framework. This yields two defensible estimands: (a) the Intent-to-Treat (ITT) effect of campaign eligibility, which is the most robust causal parameter, and (b) the Local Average Treatment Effect (LATE) of actual exposure among compliers whose exposure status is shifted by assignment. When no randomization exists, the strongest defensible analysis is a carefully specified observational comparison with explicit acknowledgment of unmeasured confounding from baseline purchase intent.

---

## 2. Research Question

What is the causal effect of actual digital ad exposure on downstream user conversion outcomes (visits, registrations, purchases), given that the platform's delivery algorithm, not the researcher, determines which users among those eligible for the campaign actually receive impressions?

---

## 3. Target Estimand and Strongest Defensible Estimand

Two distinct estimands are relevant, and the design should report both:

### (a) Intent-to-Treat (ITT) — Policy-Relevant Effect
**E[Y(1) − Y(0) | Z = 1]** — the average effect of being *assigned to campaign eligibility* on outcomes, regardless of whether the user actually saw an ad.

### (b) Complier Average Causal Effect (CACE / LATE) — Exposure Effect
**E[Y(1) − Y(0) | complier]** — the average effect of actual ad exposure on outcomes, among the subpopulation of users whose exposure status is determined by assignment (compliers).

> **Strongest defensible estimand**: The ITT is always the strongest defensible parameter. It requires only that assignment is randomized (or conditionally ignorable) and does not require the stronger assumptions needed for LATE. The ITT directly answers the business question: "What is the return from running (vs. not running) this campaign?"

---

## 4. Treatment/Exposure and Main Outcomes

| Concept | Definition |
|---|---|
| **Assignment (Instrument Z)** | Indicator for whether a user is designated as eligible for the campaign by the researcher (Z = 1) or held out (Z = 0). |
| **Actual Exposure (Treatment D)** | Indicator for whether the platform's delivery system served at least one campaign impression to the user (D = 1) or not (D = 0). |
| **Exposure Opportunity (Alternative D*)** | Indicator for whether the user was in a position to receive an impression (e.g., visited a page where the ad *could have* been served), even if not ultimately shown. |
| **Main Outcome (Y)** | Downstream conversion: binary or count of visits, registrations, or purchases within a pre-specified attribution window after the campaign eligibility date. |

---

## 5. Data Structure Summary

The dataset should be organized at the **user–campaign** level with the following structure:

```
User ID | Z (assignment) | D (actual exposure) | D* (exposure opportunity, if available) | Y (outcome) | Pre-period Y₀ | Covariates X
```

- **If assignment is randomized**: One observation per randomized user, with assignment status Z, actual exposure D, baseline covariates X, and outcome Y.
- **If repeated observations are available**: A panel structure with user-level observations across multiple time periods or campaign waves, enabling within-user comparisons.
- **If only observational**: Cross-section of users with exposure status D, outcome Y, and whatever covariates the platform provides.

The minimum viable data requires: (user identifier, assignment/eligibility indicator, actual exposure indicator, outcome indicator, and a set of pre-campaign covariates for balance checking).

---

## 6. Relevant Causal Mechanisms

The packet identifies four mechanisms, each with distinct implications for the empirical design:

1. **Endogenous exposure channel**: Users with higher baseline purchase intent are more likely to be in auctions where the advertiser's bid wins. This creates positive selection bias in naive exposed-vs-unexposed comparisons. The direction of bias is expected to be upward (overstating ad effectiveness).

2. **Platform-delivery channel**: The platform's auction, pacing, and optimization rules act as a complex selection function mapping assignment Z to actual exposure D. This function is generally unknown to the researcher but determines compliance. Understanding it qualitatively helps assess monotonicity plausibility.

3. **Measurement channel**: Attribution windows (e.g., 7-day, 30-day post-exposure) and conversion tracking fidelity determine what the researcher observes as Y. Window choice affects both signal and noise. Shorter windows reduce contamination from unrelated events but may miss delayed effects; longer windows capture more conversions but introduce more confounding.

4. **Interpretation risk**: A clean ITT estimate answers "what happens if we run this campaign?" but not "what happens if we could force every eligible user to see the ad?" The gap between these questions is the compliance rate. Both are meaningful; neither is universally "correct."

---

## 7. Main Identification Challenge

The **central identification challenge** is that actual ad exposure D is endogenously determined by the platform's delivery algorithm, which selects users based on unobserved characteristics correlated with outcomes. Formally:

**E[Y | D = 1] − E[Y | D = 0] ≠ E[Y(1) − Y(0)]**

because:

**Cov(D, ε_Y) ≠ 0**

where ε_Y captures all unobserved determinants of Y, including baseline purchase intent, browsing behavior, and demographic factors that both increase the likelihood of winning an ad auction and the probability of conversion. The sign of this covariance is expected to be positive.

A secondary challenge is that the compliance function — the mapping from Z to D — is controlled by the platform and may be non-monotonic in complex ways if, for example, the platform optimizes for different objectives across user segments.

---

## 8. Whether Credible Causal Identification Is Possible

**Conditional answer**: Credible causal identification of the ITT is possible **if and only if** the researcher has control over campaign assignment Z and can implement it in a way that is independent of potential outcomes. This requires:

- Randomization of users (or clusters of users) to campaign eligibility vs. holdout.
- The platform respecting the assignment such that holdout users (Z = 0) cannot receive campaign impressions.
- Observation of actual exposure D and outcomes Y in both arms.

Under these conditions, the ITT is credibly identified. The LATE requires additional assumptions (exclusion restriction, monotonicity, non-zero first stage) and is less robust but still defensible.

**Without randomization**, credible causal identification is not possible from cross-sectional data alone. The strongest defensible analysis in that case is a descriptive comparison with careful covariate adjustment and explicit caveats about unmeasured confounding. Panel or repeated-observation designs can strengthen the case but do not fully resolve the endogeneity problem.

---

## 9. Proposed Empirical Design

### Primary Design: Randomized Encouragement with Instrumental Variables

**Step 1 — Randomization**: The researcher randomly assigns users to:
- **Treatment arm (Z = 1)**: Eligible for the campaign. The platform may serve impressions to these users according to its normal optimization.
- **Control arm (Z = 0)**: Held out. The platform must not serve campaign impressions to these users.

**Step 2 — Measurement**: For all users (both arms), record:
- Z: assignment status
- D: whether any campaign impression was actually served (from ad delivery logs)
- Y: downstream conversions within a pre-specified attribution window
- X: pre-randomization covariates for precision and balance checks

**Step 3 — Compliance characterization**: Classify users into compliance types:
- **Compliers**: D = 1 when Z = 1; D = 0 when Z = 0
- **Never-takers**: D = 0 regardless of Z (users the platform never serves, even when eligible)
- **Always-takers**: D = 1 regardless of Z (problematic — these would be users in the control arm who somehow receive impressions; a well-implemented holdout should make this group empty)

**Step 4 — Estimation**:

*ITT estimate* (reduced form):
```
Y_i = θ₀ + θ₁Z_i + X_i'λ + u_i
```
θ₁̂ is the causal effect of campaign eligibility.

*IV/2SLS estimate*:
```
First stage:  D_i = α₀ + α₁Z_i + X_i'γ + ε_i
Second stage: Y_i = β₀ + β₁D̂_i + X_i'δ + ν_i
```
β₁̂ is the LATE: the causal effect of actual exposure among compliers.

*Compliance-adjusted Wald estimator* (equivalent in the binary case):
```
LATE = ITT / (E[D|Z=1] − E[D|Z=0])
```

**Step 5 — Reporting**: Report ITT, first-stage F-statistic, compliance rate, LATE, and explicit discussion of the complier population's characteristics vs. the full eligible population.

### Fallback Design (No Randomization Available): Stratified Observational Comparison

If assignment is not randomized, the strongest defensible approach is:

1. Define exposure opportunity D* as the comparison basis (users who were "in a position" to see the ad vs. those who were not).
2. Match or stratify on all available pre-campaign covariates (browsing history, past purchases, demographics, platform engagement metrics).
3. Estimate covariate-adjusted difference in outcomes.
4. Use bounding approaches (e.g., Oster bounds, Rosenbaum sensitivity) to characterize how strong unobserved confounding would need to be to eliminate the estimated effect.
5. Label all findings as **descriptive associations**, not causal effects.

---

## 10. Why the Design Is Valid

**For the ITT**: Randomization of Z ensures that Z is independent of potential outcomes (Y(0), Y(1)) in expectation. Therefore:

**E[Y | Z = 1] − E[Y | Z = 0] → E[Y(1) − Y(0) | Z = 1]**

This is unbiased and requires no modeling assumptions beyond successful randomization and no interference between users.

**For the LATE**: Under the standard IV assumptions (see Section 11), the 2SLS estimator identifies the average treatment effect for compliers. The key practical defense is:
- The instrument (random assignment) is clearly exogenous.
- The first stage is directly testable and should be strong (F > 10).
- Monotonicity is plausible because the platform has no incentive to *reduce* exposure for assigned-eligible users relative to a world where they are not eligible.

**Why causal identification is not credible without randomization**: Without randomization, assignment Z is not independent of potential outcomes. Users who end up in the "eligible" group differ from those who do not in ways correlated with outcomes. Covariate adjustment can reduce but not eliminate this bias because baseline purchase intent—the key confounder—is typically unmeasured or measured only through noisy proxies.

---

## 11. Required Assumptions

### For the ITT

| Assumption | Description | Testable? |
|---|---|---|
| **Random assignment** | Z is independent of (Y(0), Y(1)) | Partially — covariate balance tests |
| **No interference (SUTVA)** | One user's assignment does not affect another user's outcomes | Requires design-level argument |
| **Exclusion of never-eligible** | Z = 0 users cannot receive campaign impressions (one-sided non-compliance) | Yes — verify D = 0 in control arm from delivery logs |

### Additional Assumptions for the LATE

| Assumption | Description | Testable? |
|---|---|---|
| **Relevance** | Z has a non-zero effect on D (Cov(Z, D) ≠ 0) | Yes — first-stage F-test |
| **Exclusion restriction** | Z affects Y only through D; no direct effect of eligibility on outcomes | No — must be argued; platform-level artifacts (e.g., the act of being in the eligible pool changing platform behavior in other ways) are the main threat |
| **Monotonicity** | No defiers: for all users, D(Z = 1) ≥ D(Z = 0) | No — must be argued; plausible if holdout is enforced |
| **Homogeneous treatment effects (for 2SLS interpretation)** | Treatment effect constant across compliers, or at minimum, 2SLS consistently estimates LATE | No — 2SLS estimates a variance-weighted average of covariate-specific LATEs under heterogeneity |

---

## 12. Statistical Model and Analysis Equations

### Notation

- i = 1, ..., N users
- Z_i ∈ {0, 1}: assignment to campaign eligibility (instrument)
- D_i ∈ {0, 1}: actual ad exposure (endogenous treatment)
- Y_i: outcome (conversion indicator or count)
- X_i: vector of pre-randomization covariates
- ε_i, u_i, ν_i: mean-zero error terms

### Model 1: Intent-to-Treat (Reduced Form)

```
Y_i = θ₀ + θ₁Z_i + X_i'λ + u_i
```
- θ₁: ITT effect (causal if Z is randomized)
- Standard errors: heteroskedasticity-robust (HC2/HC3)

### Model 2: Two-Stage Least Squares (2SLS)

**First stage:**
```
D_i = α₀ + α₁Z_i + X_i'γ + ε_i
```
- α₁: compliance rate (difference in exposure probability between arms)
- Diagnosis: F-statistic on α₁; F > 10 indicates strong instrument

**Second stage:**
```
Y_i = β₀ + β₁D̂_i + X_i'δ + ν_i
```
- β₁: LATE (complier average causal effect)
- Standard errors: must account for generated regressor D̂_i (standard 2SLS SEs do this)

**Relationship:**
```
LATE = θ₁ / α₁   (when Z and D are binary)
```

### Model 3: Linear Probability Model with Covariates (Observational Fallback)

```
Y_i = κ₀ + κ₁D_i + X_i'π + η_i
```
- κ₁: covariate-adjusted association between exposure and outcome
- Labeled explicitly as **descriptive**, not causal
- Reported with sensitivity analysis (Oster δ, Rosenbaum Γ)

### Model Extension: Panel / Repeated Observations

If repeated observations across campaigns or time periods are available:

```
Y_{it} = μ₀ + μ₁D_{it} + α_i + τ_t + ω_{it}
```
- α_i: user fixed effects (absorb time-invariant unobserved confounders)
- τ_t: time fixed effects
- μ₁: within-user estimate of exposure-outcome association
- Still not fully causal unless within-user variation in D is exogenous

---

## 13. Robustness, Placebo, Falsification Checks, and Diagnostic Tests

### Pre-Analysis Diagnostics

1. **Covariate balance tables**: Compare standardized mean differences for all pre-randomization X across Z = 1 and Z = 0 arms. Threshold: |SMD| < 0.1 for adequate balance.
2. **First-stage strength**: Report Kleibergen-Paap F-statistic; F < 10 indicates weak instrument problems.
3. **Compliance characterization**: Report E[D | Z = 1] and E[D | Z = 0]; verify that E[D | Z = 0] ≈ 0 (one-sided non-compliance holds).
4. **Attrition check**: Test whether outcome missingness differs by Z arm.

### Falsification Tests

5. **Pre-period outcome test**: If pre-campaign outcome data Y₀ exists, regress Y₀ on Z. A null finding supports randomization; a significant finding indicates imbalance.
6. **Placebo outcome test**: Identify an outcome that should not be affected by the campaign (e.g., behavior on an unrelated product category) and test whether Z predicts it.
7. **Placebo treatment test**: Define a "fake" treatment window before the actual campaign and test whether Z predicts "exposure" in this period (should be null).

### Robustness Checks

8. **Alternative IV estimators**: Compare 2SLS with Limited Information Maximum Likelihood (LIML) if instruments are weak; LIML is more robust to weak instruments.
9. **Alternative attribution windows**: Estimate ITT and LATE under 1-day, 7-day, 14-day, and 30-day attribution windows to assess sensitivity.
10. **Donut RD / threshold analysis**: If the platform uses a bid or quality score threshold for delivery, examine outcomes in a narrow bandwidth around the threshold.
11. **Sensitivity to covariate sets**: Report estimates with and without covariate adjustment; similar point estimates support randomization.
12. **Non-parametric bounds**: Compute Manski bounds on the ATE using only randomization and the bounded outcome assumption, without monotonicity or exclusion.

---

## 14. Heterogeneity Analysis (If Supportable)

Heterogeneity analysis is supportable for the ITT (since Z is randomized) but requires caution for the LATE (since complier status is unobserved).

### ITT Heterogeneity (Defensible)

Stratify the ITT analysis by pre-specified covariates measured before randomization:
- **Prior engagement level** (high vs. low platform activity): Does the campaign work better on already-engaged users?
- **Prior purchase history** (new vs. returning customer): Differential effects by customer lifecycle stage.
- **Device type** (mobile vs. desktop): Channel-specific effects.
- **Geographic region**: Regional variation.
- **Time of eligibility** (early vs. late in campaign): Wear-out or cumulative effects.

**Implementation**: Include interaction terms in the reduced-form equation:
```
Y_i = θ₀ + θ₁Z_i + θ₂Z_i × H_i + θ₃H_i + X_i'λ + u_i
```
Report θ₁ + θ₂ for each level of H, with multiple comparison adjustments.

### LATE Heterogeneity (Requires Caution)

Complier characteristics can be described but not observed at the individual level. Report:
- Marginal treatment effect (MTE) analysis if a continuous instrument (e.g., bid level) is available.
- Stratifying LATE by observed covariates using the Abadie (2003) kappa-weighting approach.

---

## 15. Measurement, Compliance, Missingness, Spillover, and Implementation Limits

| Issue | Severity | Mitigation |
|---|---|---|
| **Attribution window choice** | Moderate | Pre-register the primary window; report sensitivity across alternatives |
| **Conversion tracking fidelity** | Moderate | Cross-validate against external data (e.g., CRM records) if available |
| **One-sided non-compliance failure** (control users seeing ads) | High | Monitor delivery logs; exclude or reclassify if detected; this undermines the instrument |
| **Two-sided non-compliance** (eligible users never reachable by platform) | Low-Moderate | Reduces first-stage power; increase sample size or accept wider confidence intervals |
| **Outcome missingness** | Moderate | Test differential missingness by arm; use multiple imputation if missingness is conditional on observables |
| **Interference / spillover** (SUTVA violation) | Potentially high | Cluster randomization (by household, geography, or device graph); measure within-cluster correlation |
| **Platform changes mid-campaign** | Moderate | Split campaign into temporal blocks; test for structural breaks |
| **Ad blocking** | Low | Cannot observe blocked impressions; reduces compliance in treatment arm; differential ad-block usage by arm is testable |
| **Cross-device tracking** | Moderate-High | A user may see an ad on mobile but convert on desktop; linkage depends on platform identity graph quality |

---

## 16. Failure Modes and Alternative Explanations

### Failure Mode 1: Exclusion Restriction Violation

**Scenario**: Being in the eligible pool changes user behavior even without seeing an ad (e.g., the platform's recommendation algorithm treats eligible users differently, or eligibility triggers other marketing touches).

**Implication**: LATE is biased; user-level effects cannot be separated from platform-level effects.

**Diagnosis**: If possible, compare Z = 1, D = 0 users to Z = 0 users. If they differ, the exclusion restriction may be violated (though selection into never-taker status could also explain the difference).

### Failure Mode 2: Monotonicity Violation

**Scenario**: Some users would be *less* likely to see ads when eligible than when not eligible (defiers). This could happen if the platform reallocates inventory away from users flagged as "already in the campaign."

**Implication**: The 2SLS estimand is no longer the LATE; it is a weighted average where some weights may be negative.

**Diagnosis**: Untestable directly. Argue plausibility based on platform incentives. A platform that optimizes for advertiser outcomes has no incentive to create defiers.

### Failure Mode 3: Weak Instrument

**Scenario**: Compliance rate α₁ is very low (few eligible users actually see ads).

**Implication**: LATE is estimated with very wide confidence intervals; 2SLS is biased toward OLS in finite samples.

**Diagnosis**: Directly testable (F < 10). Mitigation: increase sample size, report only ITT, or use weak-instrument-robust methods (Anderson-Rubin confidence sets).

### Failure Mode 4: Differential Attribution Window Contamination

**Scenario**: If the attribution window is long, outcomes for Z = 1 users may include conversions driven by non-campaign factors that simply occur later in time.

**Implication**: ITT estimate contaminated by time-varying confounders.

**Diagnosis**: Report ITT by time-to-conversion; if the effect is concentrated in the first few days and flattens, this supports a causal interpretation. If the effect grows linearly with time, contamination is likely.

### Failure Mode 5: Selection on Unobservables (Observational Design)

**Scenario**: Without randomization, users selected by the platform for ad delivery have higher baseline intent in ways not captured by observed covariates.

**Implication**: Observational estimates overstate the true effect.

**Diagnosis**: Oster bounds on selection proportionality (δ); Rosenbaum sensitivity parameter (Γ).

---

## 17. What Cannot Be Claimed

1. **"The ad caused an X% lift in conversions for all users."** — The LATE only applies to compliers (users whose exposure is determined by assignment). It does not generalize to always-takers or never-takers without additional assumptions.

2. **"The ad caused conversions for the specific users who saw it."** — The LATE is a local effect for a latent subpopulation. We cannot identify which individual users are compliers.

3. **"The estimated effect would replicate on a different platform or campaign."** — External validity is not addressed by this design. Platform algorithms, user populations, and campaign creatives differ.

4. **"The ITT equals the effect of ad exposure."** — The ITT is the effect of campaign *eligibility*, diluted by non-compliance. It is a different parameter from the exposure effect.

5. **"Observational estimates are causal."** — Without randomization, all estimates are descriptive associations. Sensitivity analyses indicate how robust they are to confounding but do not prove causality.

6. **"The campaign has no long-term effects beyond the attribution window."** — The design only captures outcomes within the pre-specified window.

7. **"The ad creative itself (vs. ad delivery mechanics) drives the effect."** — The design bundles creative, targeting, delivery algorithm, and platform environment into a single treatment.

---

## 18. Additional Data Needed

| Data Element | Why Needed | Priority |
|---|---|---|
| **Pre-campaign outcome history** (Y₀) | Enables falsification tests, improves precision via ANCOVA, supports DiD if randomization fails | High |
| **User-level pre-randomization covariates** | Balance checking, precision improvement, heterogeneity analysis | High |
| **Detailed delivery logs** (impression timestamps, frequency, viewability) | Enables dose-response analysis, distinguishes one-impression from multi-impression effects | Medium |
| **Exposure opportunity indicators** (D*) | Enables comparison of "in-auction but not shown" vs. "not in auction" users to assess platform selection | Medium |
| **Bid/auction data** (if available) | Enables regression discontinuity around bid thresholds or continuous instrument analysis | Low-Medium |
| **Cross-device identity graph** | Reduces measurement error from cross-device conversions | Medium |
| **Platform experiment metadata** (if platform ran its own A/B test) | Ground truth comparison for researcher-designed IV | Low |
| **User-level identifiers for cluster assignment** (household, geography) | Enables cluster-randomized or cluster-robust inference | Medium |
| **Post-campaign long-run outcome data** | Assesses persistence of effects beyond the primary attribution window | Low |

---

## 19. Threat-Response Table

*(This section was not explicitly requested by the task packet but is included for completeness.)*

| Threat | Type | Response |
|---|---|---|
| Non-random exposure — users with high intent more likely to see ads | Endogeneity | Use randomized assignment Z as instrument for D; estimate LATE |
| Exclusion restriction violation — eligibility affects outcomes through channels other than exposure | Identification | Argue design; test never-taker outcomes vs. control if possible; report ITT as primary result |
| Weak instrument — low compliance rate | Estimation | Monitor first-stage F; increase N; use LIML or Anderson-Rubin CS; fall back to ITT |
| SUTVA violation — user-to-user interference | Identification | Cluster randomization; spatial/temporal buffer zones; estimate within-cluster correlation |
| Attribution window contamination | Measurement | Pre-register window; sensitivity across windows; analyze time-to-event |
| Differential attrition | Internal validity | Test missingness by arm; bounds with worst-case imputation (Lee bounds if outcome is binary) |
| Platform algorithm change mid-experiment | Internal validity | Temporal block indicators; structural break tests; split-sample analysis |
| External validity — results specific to this campaign/platform | Generalizability | Explicit caveats; replicate across campaigns if possible |

---

## 20. Claim-Evidence Table

| Claim | Evidence Used | Claim Type | Confidence | What Would Falsify This Claim |
|---|---|---|---|---|
| Campaign eligibility (Z) is independent of potential outcomes | Randomization protocol; covariate balance tables; pre-period outcome falsification test | Causal / Design | High (if randomization implemented correctly) | Significant imbalance in observed covariates or pre-period outcomes between Z = 1 and Z = 0 |
| Campaign eligibility increases ad exposure probability | First-stage regression: D on Z; F-statistic > 10 | Statistical / Mechanism | High (directly testable) | F-statistic ≤ 10; α₁̂ ≈ 0 |
| Assignment affects outcomes only through exposure (exclusion restriction) | Design argument; qualitative understanding of platform mechanics | Causal / Assumption | Moderate (untestable) | Z = 1, D = 0 users systematically differ in outcomes from Z = 0 users in ways not explained by selection into never-taker status |
| Platform delivery is monotonic in assignment (no defiers) | Platform incentives analysis; holdout enforcement | Causal / Assumption | Moderate-High (plausible but untestable) | Evidence that the platform suppresses ad delivery to users flagged as eligible relative to ineligible users |
| The ITT estimate is an unbiased estimate of the causal effect of campaign eligibility | Randomization; no interference; no differential attrition | Causal | High | Significant differential attrition by arm; evidence of between-user interference; failed balance checks |
| The LATE estimate is the causal effect of exposure for compliers | ITT validity + exclusion + monotonicity + relevance | Causal | Moderate | Any of the IV assumptions fail (see above rows) |
| Naive exposed-vs-unexposed comparison overstates ad effectiveness | Comparison of OLS (D on Y) to IV estimate; direction of selection bias | Descriptive / Diagnostic | High (if IV estimate is valid) | IV estimate > OLS estimate (would suggest negative selection, contrary to mechanism intuition) |
| Campaign effect is concentrated within the primary attribution window | Time-to-event analysis; sensitivity to window length | Statistical | Moderate | Effect magnitude proportional to window length; significant effects at window boundaries |
| Results generalize to other campaigns or platforms | None from this design alone | External validity | Low | N/A — this claim is not supported by a single-campaign design |
| Observed covariates capture all confounding (observational designs) | Balance after matching; sensitivity analysis (Oster δ, Rosenbaum Γ) | Descriptive / Assumption | Low | Large Oster δ or small Rosenbaum Γ needed to eliminate effect |

## Tool Log Summary

- actual tool use: none
- trajectory `toolMetas`: []
- toolCall count: 0
- toolResult count: 0
- session_id: isolated_20260529_113339_52386_4
- session_log: /Users/jiangcanxiang/.openclaw/agents/benchmark_isolated/sessions/isolated_20260529_113339_52386_4.jsonl
- trajectory_log: /Users/jiangcanxiang/.openclaw/agents/benchmark_isolated/sessions/isolated_20260529_113339_52386_4.trajectory.jsonl

## Operator Notes

- duration_ms: 134064
- stderr_excerpt: [plugins] plugins.allow is empty; discovered non-bundled plugins may auto-load: qqbot (/Users/jiangcanxiang/.openclaw/npm/node_modules/@openclaw/qqbot/dist/index.js), openclaw-weixin (/Users/jiangcanxiang/.openclaw/npm/node_modules/@tencent-weixin/openclaw-weixin/dist/index.js). Set plugins.allow to explicit trusted ids. [skills] Skipping escaped skill path outside its configured root: source=openclaw-managed root=~/.openclaw/skills reason=symlink-escape requested=~/.openclaw/skills/0-autoresearch-skill resolved=~/.orchestra/skills/0-autoresearch-skill [skills] Skipping escaped skill path outside its configured root: source=openclaw-managed root=~/.openclaw/skills reason=symlink-escape requested=~/.openclaw/skills/brainstorming-research-ideas resolved=~/.orchestra/skills/21-research-ideation/brainstorming-research-ideas [skills] Skipping escaped skill path outside its configured root: source=openclaw-managed root=~/.openclaw/skills reason=symlink-escape requested=~/.openclaw/skills/creative-thinking-for-research resolved=~/.orchestra/skills/21-research-ideation/creative-thinking-for-research [skills] Skipping escaped skill path outside its configured root: source=openclaw-managed r
