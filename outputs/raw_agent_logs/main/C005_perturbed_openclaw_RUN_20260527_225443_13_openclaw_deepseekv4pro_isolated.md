# Raw Agent Run Log

- `run_id`: RUN_20260527_225443_13_openclaw_deepseekv4pro_isolated
- `case_id`: C005
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
- `timestamp`: 2026-05-27T22:54:43+0800
- `input_file`: benchmark/cases/C005_online_ad_measurement/agent_task_perturbed.md
- `system_prompt_summary`: workspace=/Users/jiangcanxiang/OpenClawBenchmarkIsolated; thinking=high; actual_tool_use=none; agent=benchmark_isolated
- `contamination_status`: unknown
- `contamination_reason`: pending manual content review; actual tool use=none
- `status`: success

## Raw Agent Output

# Research Design: Causal Effect of Digital Ad Exposure Without Opportunity-Side Logs for Untreated Users

---

## 1. Executive Summary

This task asks whether we can credibly estimate the causal effect of actual digital ad exposure on downstream user conversions when the platform retains campaign assignment and impression logs but does **not** retain logs identifying which untreated users had the same opportunity to receive the focal ad. The loss of opportunity-side tracking for untreated users eliminates the ability to construct the most rigorous counterfactual designs (e.g., matching exposed users to unexposed users who were in the same auctions, or regression discontinuity around auction score thresholds). However, **the core instrumental-variables (IV) strategy using randomized campaign assignment to identify the local average treatment effect (LATE) of exposure on compliers remains computable and defensible**, because the Wald estimator requires only group-level statistics — not individual-level compliance status for the control group. The design is **weaker** than the full-information benchmark: we lose the ability to characterize the complier subpopulation, to test monotonicity, to construct alternative estimators for triangulation, and to inspect opportunity-level mechanisms. The strongest defensible claim is the **intent-to-treat (ITT) effect of campaign assignment**. The LATE of actual exposure is a secondary claim that requires stronger, untestable assumptions. If the evaluator requires opportunity-level counterfactual precision, the appropriate conclusion is that only ITT is credible and that exposure-effect claims must be downgraded to correlational.

---

## 2. Research Question

What is the causal effect of actual digital ad exposure (being served the focal creative at an available impression opportunity) on downstream user conversion outcomes, in a setting where:

- Campaign assignment or eligibility is subject to some form of higher-level randomization or holdout,
- The platform optimizes which eligible users actually receive impressions through auctions, pacing, and targeting,
- The researcher observes assignment status, realized impressions, and downstream outcomes for all users,
- **But the researcher cannot observe which untreated users had an ad opportunity (i.e., were in the auction) and failed to receive the focal ad.**

---

## 3. Target Estimand or Strongest Defensible Estimand

Three estimands are ordered from most defensible to least:

### 3.1 Intent-to-Treat (ITT) — Fully Credible

$$
\tau_{ITT} = \mathbb{E}[Y_i \mid Z_i = 1] - \mathbb{E}[Y_i \mid Z_i = 0]
$$

where \( Z_i = 1 \) if user \( i \) is assigned/eligible for the campaign and \( Z_i = 0 \) otherwise. Under random assignment, \( \tau_{ITT} \) identifies the average causal effect of being assigned to campaign eligibility on the downstream outcome. This does **not** require opportunity-side logs for untreated users and relies only on the randomization of \( Z \).

### 3.2 Local Average Treatment Effect (LATE) via IV — Credible with Stronger Assumptions

$$
\tau_{LATE} = \frac{\mathbb{E}[Y_i \mid Z_i = 1] - \mathbb{E}[Y_i \mid Z_i = 0]}{\mathbb{E}[D_i \mid Z_i = 1] - \mathbb{E}[D_i \mid Z_i = 0]}
$$

where \( D_i \) is actual focal-ad exposure. This identifies the average causal effect of exposure for **compliers** — users who would be exposed if and only if assigned. The Wald estimator requires only group-level means, not individual opportunity logs. However, without opportunity-side logs, we cannot characterize compliers, test monotonicity, or rule out certain exclusion-restriction violations.

### 3.3 Average Treatment Effect on the Treated (ATT) — Not Credibly Identified

Without opportunity-side logs, we cannot construct a valid counterfactual for exposed users by matching on auction-level covariates, opportunity timing, or bid landscapes. ATT estimation via selection-on-observables is not defensible.

**Recommendation:** Report \( \tau_{ITT} \) as the primary result. Report \( \tau_{LATE} \) as a secondary, assumption-dependent estimate with explicit caveats.

---

## 4. Treatment or Exposure and Main Outcomes

| Concept | Variable | Measurement Level |
|---|---|---|
| **Instrument** | \( Z_i \): Campaign assignment / eligibility indicator | User level (randomized) |
| **Endogenous treatment** | \( D_i \): Actual focal-ad impression (binary) or exposure count | User-impression level, aggregated to user |
| **Primary outcome** | \( Y_i \): Downstream conversion (binary: visit, registration, purchase) | User level, post-exposure window |
| **Secondary outcome** | Revenue, purchase amount, intermediate engagement | User level |
| **Auxiliary** | Exposure frequency (number of impressions served) | User level |

---

## 5. Data Structure Summary

| Stage | Description | Observed for Treated | Observed for Untreated |
|---|---|---|---|
| 1. Eligibility | Users enter the campaign delivery window | ✅ Assignment flag | ✅ Assignment flag |
| 2. Opportunity | Platform auction/ad-slot becomes available | ❓ Partially (only if impression served) | ❌ **Not retained** |
| 3. Impression | Focal ad is served or not | ✅ Impression log | N/A (by design or by leakage log) |
| 4. Outcome | Downstream conversion | ✅ | ✅ |

The critical data gap is at Stage 2: opportunity-side logs are missing for untreated users. This means we cannot answer: "Which untreated users were in an auction where the focal ad could have been served?" This prevents us from constructing the ideal counterfactual group of "users who had the same opportunity but did not receive the ad."

---

## 6. Relevant Causal Mechanisms

### 6.1 The Assignment-to-Exposure Pipeline

1. **Randomization → Eligibility:** Users are assigned to campaign eligibility through a holdout or randomized mechanism. This creates a valid instrument \( Z \).

2. **Eligibility → Opportunity:** Eligible users generate ad opportunities when they visit the platform. The frequency and timing of opportunities are endogenous to user behavior (active users generate more opportunities).

3. **Opportunity → Exposure:** The platform runs an auction or allocation algorithm. The focal ad may win (impression served) or lose (no impression). This step is optimized by the platform based on predicted click-through rates, conversion rates, bid prices, budget pacing, and user features.

4. **Exposure → Outcome:** The ad may causally affect downstream behavior.

### 6.2 Selection Mechanisms

- **User selection into opportunity generation:** More active users generate more opportunities and are more likely to be exposed. They also have higher baseline conversion rates.
- **Platform selection into exposure:** The platform allocates impressions to users it predicts are most likely to convert, creating positive selection into \( D \).
- **Assignment may shift platform behavior:** If the platform's algorithm treats assigned and unassigned users differently (beyond the ad-serving decision), the exclusion restriction may be violated.

---

## 7. Main Identification Challenge

The core challenge is the **unobserved opportunity counterfactual**. Without opportunity-side logs for untreated users, we face:

1. **Impossibility of opportunity-level matching:** Cannot match each exposed user to an untreated user who was in the same auction or had a similar opportunity profile.

2. **Unobservable compliance types at the individual level:** Cannot classify individual untreated users as compliers, never-takers, or always-takers, because we cannot observe whether they had the opportunity to be exposed.

3. **Inability to characterize the complier subpopulation:** Even if the LATE is point-identified, we cannot describe who the compliers are (their demographics, activity levels, opportunity frequency), which limits external validity and business interpretation.

4. **Potential exclusion-restriction violations are untestable:** If assignment affects platform behavior in ways other than exposure (e.g., different bidding, different pacing, different frequency caps), we cannot detect this without opportunity-level data.

---

## 8. Whether Credible Causal Identification Is Possible

**Yes, partially.** 

- **ITT of campaign assignment is credibly identified** under the assumption that assignment is randomized. This requires no opportunity-side logs.
- **LATE of actual exposure is computable and identifies a causal parameter under IV assumptions**, but the assumptions are stronger and less testable than in the full-information case.
- **ATT of actual exposure is not credibly identified** using the available data alone.

The design logic from the full-information case **still works in its core mechanics** (random assignment → ITT → Wald rescaling → LATE), but it becomes **weaker** because:
- Assumptions cannot be tested as rigorously,
- The complier subpopulation cannot be characterized,
- Alternative estimators cannot be constructed for triangulation.

---

## 9. Proposed Empirical Design

### 9.1 Primary Design: ITT with IV-Based LATE

**Step 1: Verify randomization of assignment.**
Test balance on pre-campaign covariates (pre-campaign activity, device type, channel, segment, geographic indicators) between \( Z = 1 \) and \( Z = 0 \) groups. Report standardized mean differences.

**Step 2: Estimate the ITT.**
$$
\hat{\tau}_{ITT} = \bar{Y}_{Z=1} - \bar{Y}_{Z=0}
$$
with robust standard errors. Optionally include pre-campaign covariates to improve precision:
$$
Y_i = \alpha + \tau_{ITT} Z_i + \mathbf{X}_i'\beta + \varepsilon_i
$$

**Step 3: Estimate the first stage.**
$$
\hat{\pi} = \bar{D}_{Z=1} - \bar{D}_{Z=0}
$$
This is the difference in actual exposure rates between assigned and unassigned users. If the untreated group is a strict holdout, \( \bar{D}_{Z=0} = 0 \) and \( \hat{\pi} = \bar{D}_{Z=1} \). If there is leakage (untreated users see the ad through other channels), \( \bar{D}_{Z=0} > 0 \).

**Step 4: Compute the Wald estimator for LATE.**
$$
\hat{\tau}_{LATE} = \frac{\hat{\tau}_{ITT}}{\hat{\pi}}
$$
With standard errors via the delta method or two-stage least squares (2SLS):
- First stage: \( D_i = \gamma + \pi Z_i + \mathbf{X}_i'\delta + \nu_i \)
- Second stage: \( Y_i = \alpha + \tau_{LATE} \hat{D}_i + \mathbf{X}_i'\beta + \varepsilon_i \)

**Step 5: Report and caveat.** Present ITT as the primary causal estimate. Present LATE as a secondary estimate with explicit warnings about untestable assumptions.

### 9.2 Augmentation Designs (If Feasible Within the Platform)

If the platform can implement design changes, the following would strengthen identification:

**Option A: Ghost/PSA Ads.** Randomize, among users who win an auction, whether they see the focal ad or a placebo ad (e.g., a public service announcement). This identifies the causal effect of ad *content* among exposed users, removing the need for opportunity-side controls. This is the Johnson, Lewis, and Nubbemeyer (2017) design.

**Option B: Ad Creative Randomization.** Randomize which creative variant is served among impressions. This identifies marginal creative effects within the exposed population, though not the effect of exposure per se.

**Option C: Two-Sided Holdout with Opportunity Logging.** Retain opportunity-side logs for all users in a future campaign, enabling the full-information design.

### 9.3 If IV Assumptions Are Deemed Untenable: Descriptive Analysis

If the evaluator rules that the exclusion restriction or monotonicity cannot be justified without opportunity-side logs, downgrade to:

1. **ITT estimation** (causal for assignment, not for exposure).
2. **Naive comparison of exposed vs. unexposed** among assigned users, clearly labeled as correlational/descriptive, with a warning that selection bias is expected to inflate estimates.
3. **Bounds analysis:** Under weak monotonicity assumptions (e.g., exposure does not harm outcomes), compute Manski-style bounds for the ATT.

---

## 10. Why the Design Is Valid or Why Causal Identification Is Not Credible

### 10.1 Why the ITT Is Valid

The ITT relies only on the randomization of \( Z \). Randomization ensures that \( Z \) is independent of potential outcomes and potential treatment states. The ITT estimator is unbiased for the average effect of assignment. No opportunity-side logs are needed.

### 10.2 Why the LATE Is Computable but Weaker

The LATE is identified under the standard IV assumptions:

1. **Independence:** \( Z \perp\!\!\!\perp (Y_i(0), Y_i(1), D_i(0), D_i(1)) \). Satisfied if assignment is randomized.
2. **Exclusion restriction:** \( Z \) affects \( Y \) only through \( D \). **Cannot be fully tested without opportunity-side logs.**
3. **First stage (relevance):** \( \mathbb{E}[D \mid Z=1] \neq \mathbb{E}[D \mid Z=0] \). Directly testable; requires that assignment meaningfully changes exposure probability.
4. **Monotonicity:** \( D_i(1) \geq D_i(0) \) for all \( i \). **Cannot be tested without opportunity-side logs**, but is plausible in a holdout design where control users cannot be served the focal ad through the campaign channel.

The **critical weakening** from the missing logs is that assumptions (2) and (4) become untestable rather than partially testable, and the complier subpopulation cannot be characterized. The point estimate is unchanged, but our confidence in its interpretation is reduced.

### 10.3 Why Selection-on-Observables Designs Are Not Credible

Without opportunity-side logs, any matching estimator that compares exposed users (\( D = 1 \)) to unexposed users (\( D = 0 \)) suffers from unmeasured confounding: we cannot condition on opportunity availability, auction competitiveness, or platform bidding decisions. The platform's optimization creates systematic differences between exposed and unexposed users that observed covariates cannot fully capture.

---

## 11. Required Assumptions

### For ITT

| Assumption | Testable? | Comment |
|---|---|---|
| A1. Random assignment of \( Z \) | Partially (balance checks) | Verify on pre-treatment covariates |
| A2. SUTVA / no interference | Partially (design-based) | Check for evidence of spillover across assigned/unassigned users |
| A3. No differential attrition | Yes | Compare outcome missingness rates by \( Z \) |

### For LATE (additional)

| Assumption | Testable? | Comment |
|---|---|---|
| A4. Exclusion restriction | **No**, without opportunity logs | \( Z \) affects \( Y \) only through \( D \). Cannot rule out assignment affecting platform behavior beyond exposure. |
| A5. Monotonicity | **No**, without opportunity logs | Cannot identify defiers. Plausible if holdout prevents exposure entirely. |
| A6. First-stage relevance | Yes | Test \( H_0: \pi = 0 \) |
| A7. No always-takers in control (if holdout) | Partially | Check if any \( Z=0 \) users have \( D=1 \); if yes, investigate leakage |

---

## 12. Statistical Model or Analysis Equation

### 12.1 Primary Specification: Covariate-Adjusted ITT

$$
Y_i = \alpha + \tau_{ITT} Z_i + \mathbf{X}_i'\beta + \varepsilon_i, \quad \varepsilon_i \sim (0, \sigma^2)
$$

where \( \mathbf{X}_i \) includes pre-campaign activity, device, channel, segment, and time-of-opportunity indicators. Robust (HC2/HC3) standard errors. \( \tau_{ITT} \) is the estimand of interest.

### 12.2 IV Specification: Two-Stage Least Squares

**First stage:**
$$
D_i = \gamma + \pi Z_i + \mathbf{X}_i'\delta + \nu_i
$$

**Second stage:**
$$
Y_i = \alpha + \tau_{LATE} \hat{D}_i + \mathbf{X}_i'\beta + \varepsilon_i
$$

With robust standard errors. The F-statistic on the excluded instrument in the first stage should exceed conventional thresholds (F > 10, or use the Stock-Yogo critical values for weak instruments).

### 12.3 For Repeated Exposure (If Exposure Counts Available)

If the data include exposure frequency \( D_i \in \{0, 1, 2, \ldots\} \), the IV framework extends to multiple endogenous variables using assignment-by-opportunity interactions as instruments, but this requires careful handling of dynamic selection and is substantially weaker without opportunity logs.

### 12.4 Bounds (If LATE Assumptions Are Not Credible)

If only ITT is defended:
- **Upper bound on ATT:** Assume no defiers and that exposure does not harm. Under this, the per-protocol effect among the treated is bounded above by the IV estimand.
- **Manski bounds:** Use the full support of the outcome variable to bound the treatment effect without instrumental variable assumptions.

---

## 13. Robustness, Placebo, Falsification Checks, or Diagnostic Tests

### 13.1 Randomization Checks
- Balance table of pre-campaign covariates across \( Z = 1 \) and \( Z = 0 \).
- Joint F-test for all covariates predicting \( Z \).
- If imbalance is detected, re-weight or include controls; if severe, question randomization integrity.

### 13.2 Pre-Trends / Placebo Outcome Test
- If pre-campaign outcome data are available (e.g., conversions in a window before the campaign), test \( H_0: \tau_{ITT}^{pre} = 0 \). A non-zero pre-campaign "effect" suggests selection bias or failure of randomization.

### 13.3 Placebo Assignment Test
- Shift the campaign window to a pre-campaign period and re-estimate ITT. Should yield null.

### 13.4 Negative Control Outcomes
- Identify outcomes that should not be affected by the ad (e.g., unrelated platform actions). Test \( H_0: \tau_{ITT}^{neg} = 0 \).

### 13.5 First-Stage Strength
- Report the Kleibergen-Paap F-statistic. If F < 10, use weak-instrument robust inference (Anderson-Rubin, LIML, or conditional likelihood ratio).

### 13.6 Sensitivity Analysis for Exclusion Restriction
- Use the method of Conley, Hansen, and Rossi (2012) to assess how large a direct effect of \( Z \) on \( Y \) (bypassing \( D \)) would be needed to nullify the LATE estimate.

### 13.7 Within-Assigned-Group Analysis (Descriptive)
- Compare outcomes of exposed (\( D=1, Z=1 \)) and unexposed (\( D=0, Z=1 \)) users within the assigned group. This is **not** a causal comparison but provides a benchmark for the magnitude of selection bias. A large difference between this naive estimate and the LATE suggests substantial selection on unobservables.

---

## 14. Heterogeneity Analysis If Supportable

Heterogeneity analysis is feasible for the **ITT**, since assignment is randomized and observed for all users:

- **By pre-campaign activity terciles:** Are more active users more responsive to assignment?
- **By device or channel:** Does the campaign effect vary by mobile vs. desktop, or by platform entry point?
- **By geographic region:** Are there region-specific effects?
- **By exposure frequency (among the assigned):** Descriptive comparison of outcomes by number of impressions received, with explicit warning that this is not causally identified.

For the **LATE**, heterogeneity analysis by complier characteristics is **not possible** because we cannot identify which untreated users are compliers. Heterogeneity of the LATE across observable dimensions of the assigned group requires stronger assumptions (e.g., that the proportion of compliers is constant across subgroups, or interactions of \( Z \) with subgroup indicators in a fully saturated IV model).

---

## 15. Measurement, Compliance, Missingness, Spillover, or Implementation Limits

### 15.1 Measurement
- **Exposure measurement:** Actual impressions are logged, but viewability (was the ad actually seen?) may not be. If the platform logs viewable impressions, use those; otherwise, the exposure variable measures *served* impressions, not *viewed* impressions, introducing measurement error that biases LATE toward zero if classical, or in unknown directions if systematic.
- **Outcome measurement:** Conversions should be attributed to a fixed post-exposure window. Ensure that the conversion window is identical for treated and untreated users.

### 15.2 Compliance
- One-sided non-compliance: assignment increases but does not guarantee exposure. This is the standard IV setup. Imperfect compliance is the reason IV is needed.
- Two-sided non-compliance: if untreated users can be exposed through other channels (leakage), the first stage is reduced and the LATE applies to a different complier subpopulation.

### 15.3 Missingness
- If outcome data are differentially missing by assignment or exposure status, estimates are biased. Test for differential attrition. If present, use bounds or imputation with sensitivity analysis.

### 15.4 Spillover / Interference
- SUTVA may be violated if: (a) users in the same household or social network see different ad assignments, (b) market-level saturation affects control users, (c) the platform's budget pacing changes auction dynamics for all users when the campaign is active.
- **Without opportunity logs, spillover is harder to detect.** If geographic or temporal variation in assignment intensity is available, test for dose-response relationships that would indicate interference.

### 15.5 Implementation Limits
- The researcher cannot modify platform logging. If opportunity-side logs are genuinely unavailable and cannot be retroactively recovered, the limitations described throughout this document are binding.

---

## 16. Failure Modes and Alternative Explanations

### 16.1 Threats to ITT Validity
| Failure Mode | Explanation | Mitigation |
|---|---|---|
| Non-random assignment | Assignment was not truly randomized | Balance checks, institutional knowledge |
| Differential attrition | Outcomes missing more often for one group | Compare missingness rates; bounds |
| Spillover | Control users affected by treated users or market effects | Design-based (geographic clustering); sensitivity analysis |

### 16.2 Threats to LATE Validity
| Failure Mode | Explanation | Mitigation |
|---|---|---|
| Exclusion restriction violation | Assignment changes platform behavior beyond exposure (e.g., different auction bidding, user experience changes) | Sensitivity analysis; negative control outcomes; cannot be fully tested without opportunity logs |
| Defiers | Some users avoid exposure when assigned, or seek exposure when not assigned | Cannot test without opportunity logs; assume away with holdout design |
| Weak instrument | Assignment has small effect on exposure probability | Report F-statistic; use weak-instrument robust inference |
| Heterogeneous treatment effects | LATE applies only to compliers, may not generalize | Explicitly caveat; report ITT as primary |
| Measurement error in \( D \)| Served ≠ viewed; misattribution of impressions | Sensitivity analysis for measurement error bounds |

### 16.3 Alternative Explanations for Observed Effects
- **Seasonality or concurrent events:** If the campaign window coincides with other marketing activity, promotions, or external events, the ITT may confound the campaign effect with these factors. Use pre-campaign periods and placebo timing tests.
- **User self-selection into opportunity frequency:** More active users generate more opportunities and have different baseline conversion trajectories. The LATE on compliers may differ from the ATE.
- **Platform algorithmic changes:** If the platform changed its delivery algorithm during the campaign window, effects may reflect algorithm changes rather than ad exposure.

---

## 17. What Cannot Be Claimed

1. **The average treatment effect (ATE) of ad exposure on all users.** The LATE recovers the effect only for compliers. Without opportunity logs, we cannot even characterize who the compliers are, let alone generalize to the full population.

2. **The average treatment effect on the treated (ATT).** Without a valid counterfactual for exposed users (which requires opportunity-side logs for untreated users), we cannot identify the ATT.

3. **That the ad "caused" conversions in any individual exposed user.** The design identifies average effects for subpopulations, not individual-level causal effects.

4. **That the LATE equals the ATE or ATT.** Compliers may differ systematically from the full population and from the treated population. We do not know this without opportunity logs.

5. **The dose-response function of exposure frequency.** While we can describe associations between exposure count and outcomes, these are not causally identified without additional instruments or assumptions.

6. **The mechanism through which exposure affects outcomes** (e.g., awareness vs. persuasion vs. retargeting). The design measures reduced-form effects, not mechanisms.

7. **That the results generalize to other campaigns, platforms, or time periods.** External validity is limited to the specific campaign context.

---

## 18. Additional Data Needed

To strengthen causal identification from the current state to the full-information benchmark, the following data would be needed:

| Data Element | What It Enables | Priority |
|---|---|---|
| **Opportunity-side logs for untreated users** | Matching, RDD, complier characterization, monotonicity testing, exclusion restriction diagnostics | **Critical** |
| **Auction-level data** (bid landscape, win probability, auction score) | Quasi-experimental designs (RDD around win threshold), selection modeling | High |
| **Viewability data** | Distinguishing served from actually-viewed impressions | High |
| **Pre-campaign outcome history** (extended panel) | Difference-in-differences, pre-trend validation | High |
| **Geographic or temporal variation in assignment intensity** | Alternative instruments, spillover testing | Medium |
| **User-level activity logs** (session frequency, duration) | Opportunity generation modeling, complier characterization | Medium |
| **Cross-device or cross-channel exposure data** | Leakage detection, spillover measurement | Medium |
| **Ghost/PSA ad implementation capability** | Within-exposed randomization, removing need for unexposed controls | Medium (design change) |

---

## 19. Threat-Response Table

| Threat | Severity Without Opportunity Logs | Response |
|---|---|---|
| **Confounding of exposure-outcome relationship** | High. Platform optimizes who sees ads. Cannot condition on opportunity without logs. | Use IV via random assignment. Downgrade ATT claims. |
| **Exclusion restriction violation** | Elevated. Cannot test whether assignment affects platform behavior beyond exposure. | Sensitivity analysis. Acknowledge as untestable. |
| **Monotonicity violation** | Elevated. Cannot identify defiers without opportunity logs. | Assume under holdout design. Acknowledge limitation. |
| **Complier characterization impossible** | High. Cannot describe who LATE applies to. | Report ITT as primary. Caveat LATE interpretation. |
| **Spillover / interference** | Moderate. Harder to detect without opportunity logs. | Geographic/temporal clustering checks if available. |
| **Weak instrument** | Unchanged. First stage testable without opportunity logs. | Standard weak-instrument diagnostics and inference. |
| **Measurement error in exposure** | Unchanged. Served ≠ viewed. | Report both served-impression and viewable-impression estimates if available. |
| **Differential outcome missingness** | Unchanged. Testable. | Compare missingness rates; bounds analysis. |
| **Seasonality / concurrent events** | Unchanged. | Placebo timing tests; pre-period comparisons. |

---

## 20. Claim-Evidence Table

| # | Claim | Evidence Used | Claim Type | Confidence | What Would Falsify This Claim |
|---|---|---|---|---|---|
| 1 | Campaign assignment had a causal effect on downstream conversions (ITT) | Randomized comparison of \( Z=1 \) vs. \( Z=0 \) outcomes; balance on pre-campaign covariates | **Causal** | **High** | Evidence of non-random assignment (covariate imbalance not explained by chance); differential attrition; pre-campaign "effect" in placebo test |
| 2 | Actual ad exposure had a causal effect on conversions for compliers (LATE) | Wald estimator \( \tau_{ITT} / \pi \); first-stage F-statistic | **Causal with strong assumptions** | **Moderate** | Weak first stage (F < 10); sensitivity analysis shows exclusion restriction violation would overturn result; evidence of defiers (if opportunity data later available) |
| 3 | The LATE estimate applies to a specific, identifiable subpopulation | — | **Descriptive** | **Low** | Cannot be verified without opportunity-side logs; this claim should not be made |
| 4 | Exposed users converted more than observationally similar unexposed users | Naive comparison \( \mathbb{E}[Y \mid D=1] - \mathbb{E}[Y \mid D=0] \) | **Correlational** | **High (as correlation), Low (as causation)** | This is a descriptive fact, falsified only by measurement error. The causal interpretation is not claimed. |
| 5 | The ad exposure effect is larger/smaller for high-activity users | ITT heterogeneity by pre-campaign activity | **Causal for assignment effect; descriptive for exposure effect** | **Moderate** | Null interaction between \( Z \) and activity in ITT specification |
| 6 | Repeated exposures have incrementally different effects | Comparison by exposure frequency among assigned users | **Descriptive / correlational** | **Low (as causation)** | Cannot be causally tested without additional instruments for exposure frequency |
| 7 | Results generalize to other campaigns or platforms | — | **Speculative** | **Very low** | This claim should not be made without replication across contexts |

---

## Summary Assessment

The loss of opportunity-side logs for untreated users **does not break** the ITT or IV/LATE identification strategies, because both rely on randomized assignment — not on matching or conditioning on opportunity-level observables. The Wald estimator \( \tau_{ITT} / \pi \) is computable from group-level statistics alone.

However, the design is **materially weaker** than the full-information benchmark in four ways:

1. **Untestable assumptions:** Monotonicity and the exclusion restriction cannot be subjected to opportunity-level diagnostic checks.
2. **Uncharacterizable compliers:** We know the LATE exists for some subpopulation but cannot describe it, limiting business utility.
3. **No triangulation:** Alternative estimators (matching, RDD, selection models) that could corroborate the IV estimate are unavailable.
4. **Reduced falsifiability:** Fewer diagnostic tests can be performed, increasing the risk that unidentified violations are present.

The appropriate recommendation is to **report ITT as the primary causal result** and to **present the IV-based LATE with explicit caveats** about the strength of its underlying assumptions. If the business requires opportunity-level precision, the platform must implement opportunity-side logging for untreated users or adopt a ghost-ad/PSA design for future campaigns.

## Tool Log Summary

- actual tool use: none
- trajectory `toolMetas`: []
- toolCall count: 0
- toolResult count: 0
- session_id: isolated_20260527_225443_98725_13
- session_log: /Users/jiangcanxiang/.openclaw/agents/benchmark_isolated/sessions/isolated_20260527_225443_98725_13.jsonl
- trajectory_log: /Users/jiangcanxiang/.openclaw/agents/benchmark_isolated/sessions/isolated_20260527_225443_98725_13.trajectory.jsonl

## Operator Notes

- duration_ms: 231050
- stderr_excerpt: [plugins] plugins.allow is empty; discovered non-bundled plugins may auto-load: qqbot (/Users/jiangcanxiang/.openclaw/npm/node_modules/@openclaw/qqbot/dist/index.js), openclaw-weixin (/Users/jiangcanxiang/.openclaw/npm/node_modules/@tencent-weixin/openclaw-weixin/dist/index.js). Set plugins.allow to explicit trusted ids. [skills] Skipping escaped skill path outside its configured root: source=openclaw-managed root=~/.openclaw/skills reason=symlink-escape requested=~/.openclaw/skills/0-autoresearch-skill resolved=~/.orchestra/skills/0-autoresearch-skill [skills] Skipping escaped skill path outside its configured root: source=openclaw-managed root=~/.openclaw/skills reason=symlink-escape requested=~/.openclaw/skills/brainstorming-research-ideas resolved=~/.orchestra/skills/21-research-ideation/brainstorming-research-ideas [skills] Skipping escaped skill path outside its configured root: source=openclaw-managed root=~/.openclaw/skills reason=symlink-escape requested=~/.openclaw/skills/creative-thinking-for-research resolved=~/.orchestra/skills/21-research-ideation/creative-thinking-for-research [skills] Skipping escaped skill path outside its configured root: source=openclaw-managed r
