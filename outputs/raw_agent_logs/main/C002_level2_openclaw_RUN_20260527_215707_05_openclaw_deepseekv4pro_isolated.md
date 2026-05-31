# Raw Agent Run Log

- `run_id`: RUN_20260527_215707_05_openclaw_deepseekv4pro_isolated
- `case_id`: C002
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
- `timestamp`: 2026-05-27T21:57:07+0800
- `input_file`: benchmark/cases/C002_consumer_credit/agent_task_level2.md
- `system_prompt_summary`: workspace=/Users/jiangcanxiang/OpenClawBenchmarkIsolated; thinking=high; actual_tool_use=none; agent=benchmark_isolated
- `contamination_status`: unknown
- `contamination_reason`: pending manual content review; actual tool use=none
- `status`: success

## Raw Agent Output

# Research Design: Separating Borrower Selection from Post-Borrowing Incentives in Consumer Credit Repayment

---

## 1. Executive Summary

This research design addresses the question of whether repayment outcomes in consumer credit are driven by **borrower selection at take-up**, **post-borrowing incentive effects**, or **both**. The core challenge is that offer terms simultaneously influence who enters the loan sample (selection) and, if those terms carry through to the contract, how borrowers behave during repayment (incentive). When borrowers anticipate later terms at the time of take-up, selection and incentives become observationally entangled.

The proposed design uses **two-stage randomized variation**: (i) independently randomized pre-borrowing offer terms visible before take-up, and (ii) independently randomized post-acceptance contract terms or repayment-linked incentives revealed only after acceptance. Information timing is the linchpin — post-acceptance terms must be genuinely unknown to borrowers at the take-up stage. Under this structure, the effect of pre-borrowing terms on take-up identifies selection into the loan pool; the effect of post-acceptance terms on repayment, conditional on the pre-borrowing randomization stratum, identifies the post-borrowing incentive channel. Interaction tests reveal whether selection and incentives operate independently or amplify one another.

If two-stage randomization is infeasible (e.g., the lender cannot hide later terms, or ethical constraints prevent withholding information), the strongest defensible analysis is a **descriptive decomposition** of repayment differences into selection-consistent and incentive-consistent components, with explicit acknowledgment of what remains confounded.

---

## 2. Research Question

In a consumer-credit setting where borrowers receive offers, decide whether to take up a loan, and later enter repayment, **to what extent are repayment outcomes driven by (a) the types of borrowers who select into borrowing under different pre-borrowing terms, versus (b) the causal effect of realized post-borrowing contract terms and repayment-linked incentives on borrower behavior?**

---

## 3. Target Estimand (or Strongest Defensible Estimand)

The design targets three linked estimands:

| Estimand | Definition |
|---|---|
| **τ_selection** | The effect of pre-borrowing offer terms on the composition of borrowers who accept a loan, measured through observables (risk scores, prior history) and through the implied repayment propensity of the accepted pool. |
| **τ_incentive** | The causal effect of post-acceptance contract terms or repayment-linked incentives on repayment outcomes, estimated within the pool of borrowers who accepted a loan, holding the pre-borrowing selection margin constant. |
| **τ_total** | The total difference in repayment outcomes across borrowers who faced different pre-borrowing offer terms (the reduced-form difference in observed repayment). This decomposes into τ_selection + τ_incentive + their interaction, where identification of the decomposition depends on the two-stage randomization structure. |

If two-stage randomization is unavailable, the strongest estimand is a **descriptive decomposition** of observed repayment differences across offer-term groups into components attributable to observable borrower characteristics at take-up (selection-correlated) versus within-loan repayment variation that is consistent with incentive effects but not cleanly attributable.

---

## 4. Treatment or Exposure and Main Outcomes

### Treatment/Exposure Variables

| Variable | Stage | Description |
|---|---|---|
| **Z_pre** | Pre-borrowing (offer stage) | Offer terms visible to borrowers before take-up: interest rate, loan amount ceiling, repayment duration, or fees. Can be experimentally varied across eligible borrowers. |
| **Z_post** | Post-acceptance (contract/recovery stage) | Terms or incentives revealed only after loan acceptance: final contract rate, grace-period structure, late-fee policy, or future-credit access tied to repayment. Must be varied independently of Z_pre for clean separation. |

### Main Outcomes

| Outcome | Stage | Type |
|---|---|---|
| **Y_takeup** | Application/acceptance | Binary: borrower applies for or accepts the loan offer. |
| **Y_repay** | Repayment period | Binary or continuous: on-time repayment, delinquency (30+/60+/90+ days past due), default, or a continuous repayment rate (fraction of scheduled payments made). |
| **Y_future** | Future-borrowing period | Binary or continuous: whether borrower receives or takes up future credit, at what terms. |

---

## 5. Data Structure Summary

The data follow a **sequential linked-records structure** across four stages for each prospective borrower:

```
Stage 1: Offer → Stage 2: Take-up → Stage 3: Contract & Repayment → Stage 4: Future Borrowing
─────────────────────────────────────────────────────────────────────────────────────────────
Z_pre           Y_takeup         Z_post → Y_repay                    Y_future
(experimental)  (binary)         (experimental,   (delinquency/      (future access,
                                 revealed post-    default)           pricing)
                                 acceptance)
```

| Feature | Implication for Design |
|---|---|
| Non-applicants observable at Stage 1–2 but not Stage 3–4 | Selection analysis uses full offer sample; repayment analysis conditions on acceptance. |
| Linked records across stages for the same borrower | Borrower-level clustering; repeated observations possible if borrowers receive multiple offers. |
| Post-acceptance terms assigned at borrower-loan level | Z_post is unavailable for non-accepters. This is a sample-selection constraint, not a design flaw, and must be addressed explicitly. |
| Future-borrowing outcomes potentially observed | Enables tests of whether repayment-linked future-credit incentives affect current repayment. |

---

## 6. Relevant Causal Mechanisms

### Mechanism M1: Borrower Selection at Take-Up

Different pre-borrowing offer terms (Z_pre) attract borrowers with different underlying repayment propensity. A lower offered interest rate may draw in borrowers with lower default risk (adverse selection in reverse) or, alternatively, borrowers who are more credit-constrained and therefore riskier. The *direction* of selection is an empirical question; the *existence* of selection creates sample-composition differences across Z_pre arms.

**Operational signature:** The distribution of pre-offer risk scores, income proxies, and prior borrowing history differs significantly across Z_pre arms among accepted borrowers, even after accounting for the mechanical correlation between terms and take-up rates.

### Mechanism M2: Post-Borrowing Incentive Effects

After a borrower has accepted a loan, the realized contract terms (Z_post) or repayment-linked future consequences alter the cost of repayment, the cost of delinquency, or the continuation value of the borrower-lender relationship.

**Operational signature:** Among borrowers who accepted under the same Z_pre, repayment outcomes differ across Z_post arms in the direction consistent with economic incentives (e.g., higher interest rates increase default probability; stronger future-access incentives reduce default).

### Mechanism M3: Anticipatory Effects (Cross-Stage Contamination)

If borrowers know or can forecast Z_post at the time of take-up, their take-up decision already incorporates the post-borrowing incentives. This collapses the distinction between M1 and M2 because Z_post affects both who enters the sample and how they behave within it.

**Operational signature:** Take-up rates differ across Z_post arms — which should not happen if Z_post is genuinely unknown at take-up. This serves as a falsification check for information separation.

### Mechanism M4: Dynamic Selection Through Future Access

If future borrowing terms (Y_future stage) depend on current repayment behavior, borrowers' current repayment decisions incorporate the option value of maintaining access to future credit. This is a form of incentive effect that operates through forward-looking borrower optimization rather than contemporaneous budget constraints.

**Operational signature:** Repayment differs between borrowers who face different future-credit consequences even when current-period repayment burden is identical.

---

## 7. Main Identification Challenge

The fundamental challenge is **sample selection on unobservables interacting with treatment**. Specifically:

1. **Selection into the repayment sample is endogenous.** Only borrowers who accept a loan enter Stage 3 where Y_repay is observed. The decision to accept depends on Z_pre and on borrower characteristics (observed and unobserved). If we compare Y_repay across Z_pre arms without adjustment, we cannot separate "Z_pre caused different types of people to borrow" (M1) from "Z_pre caused different repayment behavior conditional on borrowing" (M2, if Z_pre flows through to contract terms).

2. **Z_post is only defined for accepters.** The post-borrowing incentive treatment cannot be randomized across the full offer sample because it only applies to loans that exist. This creates a built-in conditioning-on-post-treatment problem if we naively compare Z_post arms.

3. **Information contamination.** If borrowers learn Z_post before deciding on take-up — even probabilistically — the take-up decision already reflects anticipated post-acceptance terms, making it impossible to assign repayment differences exclusively to selection or to incentives.

---

## 8. Whether Credible Causal Identification Is Possible

**Yes, credible causal identification is possible** — *if and only if* the following conditions are jointly satisfied:

1. The lender has the operational ability to independently randomize both Z_pre (across all eligible borrowers) and Z_post (across accepted borrowers).
2. Z_post is not revealed, signaled, or predictable by prospective borrowers at the take-up stage.
3. The randomization mechanisms are not compromised by staff discretion, borrower communication, or operational leakage.
4. Attrition between acceptance and repayment observation is minimal and uncorrelated with treatment assignment.

If any of these conditions fail, a credible causal decomposition is not possible, and the analysis should revert to the strongest defensible descriptive or correlational strategy (see Section 9, Alternative).

---

## 9. Proposed Empirical Design

### Primary Design: Two-Stage Randomized Experiment with Information Separation

**Stage 1: Pre-Borrowing Randomization (Z_pre).** From the pool of eligible prospective borrowers, randomly assign offer terms Z_pre ∈ {z₁, z₂, ..., z_K} at the borrower-offer level. Z_pre must include terms that are salient to the take-up decision (e.g., offered interest rate, loan amount ceiling). Randomization should be stratified on pre-offer risk measures to improve precision.

**Stage 2: Post-Acceptance Randomization (Z_post).** Among borrowers who accept a loan, randomly assign post-acceptance contract terms or repayment-linked incentives Z_post ∈ {w₁, w₂, ..., w_L}. Crucially, Z_post must be independent of Z_pre (orthogonal assignment). The randomization of Z_post must occur after acceptance, and borrowers must not have learned Z_post beforehand.

**Information Protocol.** Borrowers must receive Stage 1 offer terms without any information about Stage 2 terms. The offer communication must not reference, hint at, or allow inference about post-acceptance terms. A post-acceptance disclosure provides Z_post after the contract is executed.

### Assignment Structure

```
Eligible Borrowers (N)
       │
       ▼
Randomize Z_pre ──────────────────────────────┐
       │                                       │
       ├──► Accept (N_A) ──► Randomize Z_post ─┤
       │         │                             │
       │         └──► Observe Y_repay          │
       │                                       │
       └──► Reject (N_R) ──► Observe only      │
                              take-up outcome   │
                                               │
                      ┌────────────────────────┘
                      ▼
              Identify:
              • τ̂_selection: effect of Z_pre on take-up and borrower composition
              • τ̂_incentive: effect of Z_post on Y_repay | Z_pre
              • Decomposition of total repayment differences
```

### Estimation

**Selection channel (τ_selection):** Estimate the effect of Z_pre on the take-up decision and on the composition of accepted borrowers:

```
P(Y_takeup = 1 | Z_pre, X) = g(α₀ + α₁·Z_pre + X'β)
```

where X includes pre-offer risk measures. The compositional effect is assessed by testing whether the distribution of X differs across Z_pre arms among acceptors, and by estimating the implied repayment propensity using pre-offer risk models.

**Incentive channel (τ_incentive):** Among accepted borrowers, estimate:

```
Y_repay = γ₀ + γ₁·Z_pre + γ₂·Z_post + γ₃·(Z_pre × Z_post) + X'δ + ε
```

- γ₁ captures the **residual selection channel** — any effect of Z_pre on repayment that operates through unobserved borrower characteristics correlated with Z_pre-induced selection, net of X.
- γ₂ captures the **post-borrowing incentive effect** of Z_post on repayment.
- γ₃ captures the **interaction** — whether the incentive effect differs by the selection margin (e.g., borrowers who accepted under worse terms respond differently to post-acceptance incentives).

**Selection-composition test.** Among acceptors, regress pre-offer risk scores on Z_pre:

```
RiskScore_i = θ₀ + θ₁·Z_pre + ν_i
```

A significant θ₁ indicates that Z_pre sorts borrowers by observable risk, providing direct evidence of Mechanism M1.

### Alternative: Strongest Defensible Descriptive Analysis (When Two-Stage Randomization Is Not Feasible)

If the lender cannot randomize at both stages (e.g., post-acceptance terms are fixed by policy or cannot be concealed), the strongest defensible analysis is:

**A. Selection-curve analysis.** Estimate take-up as a function of Z_pre and pre-offer characteristics. Characterize how the risk profile of the accepted pool shifts with Z_pre. This provides descriptive evidence on selection.

**B. Within-loan incentive correlation.** Among accepted borrowers, exploit any quasi-experimental variation in Z_post that is plausibly exogenous to borrower characteristics (e.g., policy discontinuities, timing-based variation, or administrative rule changes). Test whether repayment differs by Z_post, controlling for Z_pre and observables. This provides correlational evidence on incentives, but cannot be interpreted as causal without additional identifying assumptions.

**C. Decomposition (descriptive).** The observed repayment difference between two offer groups (Z_pre = z_a vs. Z_pre = z_b) can be decomposed into:

```
ΔY_repay = [E(Y_repay | Z_pre = z_a, Accept) · P(Accept | z_a)] 
         - [E(Y_repay | Z_pre = z_b, Accept) · P(Accept | z_b)]
```

This total can be further decomposed via Oaxaca-Blinder or similar methods into a "composition effect" (different borrower types) and a "structural effect" (different repayment behavior conditional on type). The structural component is **not** a causal estimate without exogenous Z_post variation.

---

## 10. Why the Design Is Valid (or Why Causal Identification Is Not Credible)

### Validity of the Primary Design

The two-stage randomization with information separation identifies the selection and incentive channels because:

1. **Z_pre is randomly assigned** across all eligible borrowers. Any difference in take-up rates or accepted-borrower characteristics across Z_pre arms is causally attributable to the offer terms (M1).

2. **Z_post is randomly assigned and orthogonal to Z_pre.** Within any Z_pre stratum, Z_post varies independently of borrower characteristics. This breaks the correlation between post-acceptance terms and borrower unobservables that would otherwise confound Y_repay comparisons.

3. **Information separation ensures Z_post does not affect selection.** If borrowers do not know Z_post at take-up, Z_post cannot influence who enters the repayment sample. This is empirically testable (see falsification checks).

4. **The interaction test (γ₃) distinguishes independent from interactive mechanisms.** If γ₃ = 0, selection and incentives operate additively — borrowers sorted by Z_pre respond similarly to Z_post incentives regardless of which Z_pre they faced. If γ₃ ≠ 0, the two channels interact (e.g., borrowers who accepted under unfavorable terms are more responsive to post-acceptance incentives).

### Why Identification Fails Without These Conditions

Without two-stage randomization:
- Z_post may correlate with borrower characteristics that affect repayment (confounding).
- If Z_post is known at take-up, the effect of Z_pre on take-up already incorporates anticipated Z_post, making the selection channel unidentifiable.
- Without orthogonal variation, the contribution of each channel to observed repayment differences is not separately estimable.

---

## 11. Required Assumptions

| # | Assumption | Justification / Testability |
|---|---|---|
| A1 | **Random assignment of Z_pre.** No correlation between Z_pre assignment and borrower characteristics. | Testable: balance tests on pre-offer covariates across Z_pre arms. |
| A2 | **Random assignment of Z_post.** Z_post independent of borrower characteristics conditional on acceptance. | Testable: balance tests on pre-offer and acceptance-stage covariates across Z_post arms, within Z_pre strata. |
| A3 | **Information separation (exclusion).** Z_post is not known, predicted, or signaled to borrowers at the take-up stage. | Testable: Z_post should not predict Y_takeup. A significant coefficient of Z_post in a take-up regression is a falsification flag (see Section 13). |
| A4 | **No interference (SUTVA).** One borrower's assigned Z_pre or Z_post does not affect another borrower's take-up or repayment. | Testable: examine spatial or temporal clustering of outcomes; test whether neighbors' assignments predict own outcomes. |
| A5 | **Orthogonality of Z_pre and Z_post.** The two assignments are independent. | Enforced by design. Testable: cross-tabulation of assignments. |
| A6 | **Monotonicity of take-up response.** Higher Z_pre "generosity" does not decrease take-up (if Z_pre ordered by attractiveness). | Testable: check that take-up rates are monotonic in Z_pre. |
| A7 | **No differential attrition.** Missing Y_repay is unrelated to treatment assignment. | Testable: compare attrition rates across treatment arms. |
| A8 | **Stable unit treatment over time.** The effect of Z_pre and Z_post does not change systematically over the study period. | Testable: treatment-time interaction tests. |
| A9 | **No anticipation of future offers.** Borrowers' current take-up decision is not influenced by expectations of future offers from the same lender. | Partially testable if repeat-offer data are available. |

---

## 12. Statistical Model or Analysis Equation

### 12.1 Take-Up Equation (Selection Margin)

```
Y_takeup_i = 1[α₀ + α₁·Z_pre_i + X_i'β + ν_b(i) + ε_i > 0]
```

Where:
- Y_takeup_i = 1 if borrower i accepts the loan offer
- Z_pre_i = vector of pre-borrowing offer term indicators (or continuous term)
- X_i = pre-offer risk score, prior borrowing history, demographics/proxies
- ν_b(i) = random effect for offer-wave, branch, or batch b(i)
- ε_i ∼ Logistic(0,1) (logit specification) or N(0,1) (probit)

**Estimand of interest:** ∂P(Y_takeup = 1 | Z_pre, X) / ∂Z_pre — the marginal effect of offer terms on take-up probability.

### 12.2 Risk-Composition Equation (Selection Mechanism Test)

```
RiskScore_i = θ₀ + θ₁·Z_pre_i + u_i   (estimated on acceptors only)
```

A significant θ₁ provides direct evidence of risk-based selection — the offer terms shift the risk composition of the accepted pool.

### 12.3 Repayment Equation (Incentive and Residual Selection)

```
Y_repay_i = γ₀ + γ₁·Z_pre_i + γ₂·Z_post_i + γ₃·(Z_pre_i × Z_post_i) + X_i'δ + η_b(i) + ε_i
```

Where:
- Y_repay_i = repayment outcome (binary default indicator, delinquency days, or continuous repayment rate)
- Z_post_i = vector of post-acceptance term indicators
- γ₁ = residual selection channel (effect of Z_pre on repayment, net of X, through unobserved borrower type)
- γ₂ = post-borrowing incentive effect (causal under A2 + A3)
- γ₃ = interaction between selection arm and incentive arm

**Inference:** Standard errors clustered at the borrower level (if multiple loans per borrower), or at the offer-wave/branch level if assignment is grouped. Use randomization inference (Fisher exact p-values) as a complement to model-based standard errors, since the design is experimental.

### 12.4 Decomposition (Total Repayment Difference)

For any two pre-borrowing arms (z_a, z_b), the observed repayment difference can be decomposed:

```
Δ_total = E[Y_repay | Z_pre = z_a, Accept] - E[Y_repay | Z_pre = z_b, Accept]

        = γ₁·(z_a - z_b)                              ← residual selection
        + γ₂·E[Z_post | z_a, Accept] - E[Z_post | z_b, Accept]  ← incentive (if Z_post varies with Z_pre)
        + [compositional difference in X]              ← observed selection
```

Under orthogonal assignment (A5), E[Z_post | Z_pre, Accept] is independent of Z_pre, so the incentive channel is cleanly identified by γ₂.

### 12.5 Future-Access Incentive Extension

If future borrowing terms are experimentally varied as a function of current repayment:

```
Y_repay_i = γ₀ + γ₁·Z_pre_i + γ₂·Z_post_i + γ₄·Z_future_incentive_i + X_i'δ + ε_i
```

where Z_future_incentive captures whether the borrower is informed (post-acceptance) that future credit access or pricing depends on current repayment performance. A significant γ₄ identifies the forward-looking incentive channel (M4), independent of contemporaneous repayment burden.

---

## 13. Robustness, Placebo, Falsification Checks, and Diagnostic Tests

### Falsification Checks

| Test | Procedure | What It Verifies |
|---|---|---|
| **Pre-treatment balance** | Regress pre-offer covariates on Z_pre assignment. | Assumption A1 (random assignment of Z_pre). |
| **Post-acceptance balance** | Within each Z_pre arm, regress pre-offer and acceptance-stage covariates on Z_post assignment. | Assumption A2 (random assignment of Z_post). |
| **Information separation test** | Among all offered borrowers, regress Y_takeup on Z_post assignment (which should be observable administratively even if not disclosed to borrowers). | Assumption A3. A significant coefficient is a **falsification red flag**: it indicates Z_post information leaked to the take-up stage. |
| **Orthogonality check** | Cross-tabulate Z_pre × Z_post assignment frequencies; test for independence with χ². | Assumption A5 (orthogonality). |

### Placebo Tests

| Test | Procedure | What It Verifies |
|---|---|---|
| **Placebo Z_pre on future outcomes** | Regress future-borrowing outcomes (pre-dating the current offer cycle) on Z_pre. Should be null. | No pre-existing trends or confounding. |
| **Placebo Z_post on pre-acceptance behavior** | Regress pre-acceptance behaviors (e.g., inquiry rate, application timing) on Z_post. Should be null if A3 holds. | Information separation. |
| **Donut-hole placebo** | Omit borrowers near the acceptance boundary and re-estimate. | Results not driven by marginal accepters. |

### Robustness Checks

| Check | Procedure |
|---|---|
| **Alternative outcome definitions** | Use 30/60/90-day delinquency, continuous repayment rate, and binary default. |
| **Stratification sensitivity** | Re-estimate with and without randomization strata fixed effects. |
| **Inference method** | Report both model-based clustered standard errors and randomization-inference p-values. |
| **Attrition bounds** | Lee (2009) bounds for repayment outcomes under differential attrition by treatment arm. |
| **Multiple-offer adjustments** | If borrowers receive multiple offers, estimate with borrower random effects and compare to single-offer-first specifications. |
| **Definition of Z_pre** | Collapse multi-valued Z_pre into binary (high vs. low generosity) and check consistency. |

### Diagnostic Tests

| Test | Procedure |
|---|---|
| **Take-up monotonicity** | Plot take-up rate against Z_pre levels; test for non-monotonicity. |
| **Risk-gradient plot** | Plot mean pre-offer risk score among acceptors against Z_pre levels. |
| **Repayment-by-stratum plot** | Plot mean Y_repay by Z_post arm, separately for each Z_pre arm, to visualize γ₁, γ₂, and γ₃. |
| **Density discontinuity** | If Z_pre is continuous, test for a discontinuity in the density of accepted borrowers at policy-relevant thresholds (McCrary test). |
| **Attrition pattern** | Compare observable characteristics of borrowers with missing vs. observed Y_repay across treatment arms. |

---

## 14. Heterogeneity Analysis (If Supportable)

If sample sizes permit, heterogeneity analysis can probe mechanism plausibility and external validity:

### 14.1 By Pre-Offer Risk Stratum

Split borrowers by pre-offer risk tercile (or quartile) and re-estimate the repayment equation. Mechanism M1 predicts that the compositional shift in accepted borrowers should be larger (in absolute terms) for intermediate-risk borrowers, who are most marginal to the take-up decision. Mechanism M2 predicts that incentive effects may be stronger for higher-risk borrowers (more credit-constrained, more responsive to repayment burden) or for lower-risk borrowers (more sensitive to future-credit access incentives).

### 14.2 By Prior Borrowing History

First-time borrowers may have different selection elasticities and incentive responsiveness than repeat borrowers with an established relationship. Repeat borrowers may have more information about the lender's practices, potentially threatening A3 if they anticipate Z_post from prior experience.

### 14.3 By Loan Size

If the offer includes variation in loan amount, the incentive effect may differ by loan size — larger loans imply higher absolute repayment burden for a given rate change.

### 14.4 By Channel or Branch

If offers are delivered through different channels (digital, branch, agent), information separation may be more credible in automated digital channels (where Z_post can be algorithmically assigned post-acceptance) than in high-touch channels where staff may (inadvertently or deliberately) signal later terms.

### Important Caveat

Heterogeneity analyses are **exploratory** unless pre-registered with explicit multiplicity corrections. They should be reported as suggestive mechanism evidence, not as confirmatory hypothesis tests.

---

## 15. Measurement, Compliance, Missingness, Spillover, and Implementation Limits

### 15.1 Measurement Issues

| Issue | Concern | Mitigation |
|---|---|---|
| **Z_post definition precision** | If Z_post includes multiple dimensions (rate, grace period, future access), the treatment is a bundle, and individual component effects are not separately identified. | Design Z_post as factorial or single-dimension variation where possible. |
| **Repayment outcome definition** | "Default" may be defined differently across loan types or time horizons. Censoring by the observation window may miss late defaults. | Pre-specify fixed-horizon outcomes (e.g., 12-month default); use survival models for time-to-delinquency as a complement. |
| **Risk score as selection proxy** | The pre-offer risk score is the lender's own model output — it may be a noisy or biased measure of true repayment propensity. | Use multiple pre-offer proxies (credit bureau score if available, income proxy, debt-to-income proxy). |

### 15.2 Compliance

| Issue | Concern | Mitigation |
|---|---|---|
| **One-sided noncompliance** | Borrowers assigned to Z_pre cannot be forced to take up. | This is inherent and expected; the design estimates intent-to-treat (ITT) effects on take-up and selection, which are the policy-relevant parameters for offer design. |
| **Z_post noncompliance** | Staff or systems may fail to implement assigned Z_post; borrowers may renegotiate. | Report ITT on Z_post assignment. If take-up of Z_post treatment is measurable (actual contract terms observed), estimate complier-average causal effects (CACE) using assignment as instrument. |

### 15.3 Missingness and Attrition

| Issue | Concern | Mitigation |
|---|---|---|
| **Repayment outcome missing** | Loans transferred, sold, or exited from the lender's tracking system. | Compare attrition rates by treatment arm; implement Lee bounds; document censoring reasons. |
| **Future-borrowing outcomes unobserved** | Borrowers may obtain future credit from other lenders. | This is a fundamental limitation — the lender only observes its own portfolio. Claims about total future-credit effects are not supportable. |

### 15.4 Spillover and Interference

| Issue | Concern | Mitigation |
|---|---|---|
| **Borrower-to-borrower information sharing** | Borrowers may share information about their assigned Z_pre or Z_post with other prospective borrowers. | If assignment is at the individual level over a short window, the probability of contamination is low. Test for spatial clustering of outcomes. If clustering by geography or time is suspected, consider cluster-level randomization. |
| **Staff behavior** | Loan officers or agents may treat borrowers differently based on assigned Z_pre or Z_post (e.g., more effort for higher-rate offers). | This is a design implementation concern. Protocol standardization, blinding of staff to treatment status where feasible, and monitoring of staff-borrower interactions are required. |

### 15.5 Implementation Limits

| Limit | Description |
|---|---|
| **Ethical constraint on information withholding** | In many jurisdictions, lenders are required to disclose all material terms before contract signing. Withholding Z_post may conflict with consumer protection regulations (e.g., Truth in Lending Act in the US). This is the single most important feasibility constraint. |
| **Operational constraint on Z_post randomization** | The lender's loan origination system may not support post-acceptance randomization of contract terms. System changes may be costly or infeasible. |
| **Time horizon** | If the repayment observation window is short, default measurement is censored. If it is long, the design must contend with macroeconomic changes over the study period. |
| **Repeated borrowing** | If the lender routinely makes repeat offers, borrowers' current behavior is shaped by expectations of future offers, complicating the interpretation of both selection and incentive channels. |

---

## 16. Failure Modes and Alternative Explanations

| Failure Mode | Alternative Explanation | Diagnostic |
|---|---|---|
| **Z_post affects Y_takeup** | Information leaked. Borrowers learned or inferred Z_post before acceptance. | Information separation test (Section 13). |
| **γ₁ ≠ 0 with full covariate controls** | (i) Genuine residual selection on unobservables; (ii) Z_pre persisted into contract terms and directly affected repayment burden (violating the design intent that Z_pre only affects selection). | Check whether realized contract terms differ by Z_pre. If they do, the design conflates selection and incentive channels for Z_pre. |
| **Treatment effect heterogeneity** | The average treatment effect of Z_post masks variation across borrower types. The interaction term γ₃ may be significant due to a few outlier types rather than a systematic pattern. | Examine distribution of individual-level treatment effects; use quantile treatment effect methods. |
| **Equilibrium response** | The lender's own behavior (collection effort, renegotiation offers) responds endogenously to Z_pre or Z_post assignment. | Document lender-side actions by treatment arm; restrict analysis to outcomes before lender intervention if possible. |
| **Macroeconomic confounding** | If the study period coincides with economic shocks, treatment effects may be period-specific. | Include time fixed effects; test treatment-time interactions. |
| **Hawthorne effects** | Borrowers aware of being in a study may alter behavior. | Compare outcomes to pre-study historical benchmarks if available. |
| **Selection on gains** | Borrowers who accept under less favorable Z_pre may have higher unobserved gains from borrowing, biasing γ₁ upward (more resilient repayment). | Cannot be directly tested without an instrument for the unobserved gain. |

---

## 17. What Cannot Be Claimed

1. **General equilibrium effects.** The design estimates partial-equilibrium effects within one lender's portfolio. Market-level effects (e.g., borrower reallocation across lenders, aggregate credit supply changes) are not identified.

2. **Long-run welfare effects.** The design identifies repayment behavior over the observation window. Whether observed repayment changes reflect improved borrower welfare or merely delayed default is not assessable without a welfare model and longer follow-up.

3. **External validity to other lenders, markets, or borrower populations.** The estimates are local to the lender's borrower population, product features, and institutional context.

4. **Causal claims about individual borrower characteristics as drivers of selection.** The design identifies that Z_pre causes compositional shifts. It does not identify *why* specific borrower types are more responsive to specific terms without additional structural assumptions.

5. **The separate contributions of specific Z_pre or Z_post components if varied as bundles.** If offer terms vary along multiple dimensions simultaneously (rate and amount together), the effect of each component is not separately identified without a factorial design.

6. **Causal claims if two-stage randomization is not implemented.** Without randomization at both stages, the analysis is descriptive or correlational. The decomposition attributes repayment differences to selection-consistent and incentive-consistent components but does not establish causality.

7. **Future-credit effects outside the lender's portfolio.** The lender observes only its own future lending to a given borrower. Borrowers may obtain credit from competitors, making total future-credit effects unobservable.

8. **That selection and incentives are the only channels.** Other mechanisms — borrower learning, relationship-specific capital, changes in borrower circumstances during repayment — are not separately identified unless explicitly modeled and measured.

---

## 18. Additional Data Needed

For the **primary (causal) design** to be implementable:

| Data Need | Purpose |
|---|---|
| **Operational ability to randomize Z_post post-acceptance** | Essential for identification of incentive channel. Requires system capability and regulatory clearance. |
| **Protocol for information separation** | Verbatim offer scripts, disclosure timing, and channel protocols to ensure Z_post is not revealed or signaled at take-up. |
| **Pre-offer credit bureau data** (if accessible) | External validation of lender's internal risk scores; richer characterization of borrower types for selection analysis. |
| **Income or employment proxies** | Improve characterization of borrower types and selection patterns. |
| **Loan officer/staff identifiers** | To test and control for staff-level heterogeneity in implementation. |
| **Full contract terms at origination** | To verify that realized terms match assigned Z_post and do not inadvertently differ by Z_pre. |
| **Collection and recovery actions** | To distinguish borrower-driven repayment from lender-driven collection intensity. |
| **Historical benchmarks** | Pre-study repayment data by risk score, to calibrate expected repayment rates and detect Hawthorne effects. |

For the **descriptive alternative**, less operational data is needed, but the analysis should still have:

| Data Need | Purpose |
|---|---|
| **Plausibly exogenous variation in Z_post** (e.g., policy discontinuities, timing variation) | To move beyond pure correlation in the incentive channel analysis. |
| **Detailed offer-acceptance-repayment linkage** | To track borrowers through all stages. |

---

## 19. Threat-Response Table

| Threat | Severity | Response |
|---|---|---|
| **Information leakage: Z_post known at take-up** | **Critical.** Collapses selection-incentive distinction. | (a) Information separation test as primary falsification check. (b) If detected, the design reverts to descriptive decomposition — the experimental variation identifies a bundled "offer effect" that cannot be decomposed into selection and incentives. (c) In protocol design, use automated digital channels where Z_post can be revealed algorithmically post-acceptance. |
| **Noncompliance with Z_post assignment** | **High.** Attenuates incentive channel estimate. | (a) Report ITT (by assignment). (b) Estimate CACE using assignment as instrument for realized Z_post if realized terms are observed. (c) Document reasons for noncompliance. |
| **Differential attrition from repayment observation** | **High.** Biases repayment comparisons if attrition correlates with treatment. | (a) Compare attrition rates across arms. (b) Lee bounds on treatment effects. (c) Multiple imputation with explicit sensitivity analysis. |
| **Z_pre and Z_post are not orthogonal** | **High.** Confounds the decomposition. | (a) Enforced by independent randomization protocol. (b) Testable via cross-tabulation. |
| **Regulatory prohibition on withholding Z_post** | **Critical.** Prevents primary design implementation. | Fall back to descriptive analysis (Section 9, Alternative). If Z_post is always disclosed pre-acceptance, the design cannot separate channels and should estimate the combined effect of the full information set on take-up and repayment. |
| **Borrower-to-borrower information sharing** | **Moderate.** Depends on borrower density and offer timing. | (a) Test spatial/temporal clustering of outcomes. (b) If clustered assignment is necessary (e.g., by branch or time window), increase cluster-level sample size. (c) Report intra-cluster correlation. |
| **Staff discretion in implementation** | **Moderate.** Staff may compensate for assigned terms through other margins. | (a) Audit staff behavior across treatment arms (e.g., approval rates, discretionary adjustments). (b) Include staff fixed effects. (c) Blind staff to treatment where possible. |
| **Repeated borrowing contaminates single-offer interpretation** | **Moderate.** Borrowers' expectations of future offers affect current behavior. | (a) Document repeat-offer patterns. (b) Estimate separately for first-time vs. repeat borrowers. (c) If repeat offers are endogenous, acknowledge that the single-offer interpretation is approximate. |
| **Macroeconomic shocks during study** | **Moderate.** Treatment effects may be period-contingent. | (a) Include time fixed effects. (b) Test treatment-time interactions. (c) Compare to historical benchmarks. |
| **Low take-up rate → small accepted sample** | **Low-Moderate.** Reduces power for Z_post estimation. | (a) Power calculations before study launch. (b) Stratify Z_pre to ensure adequate sample in each arm. (c) Pre-specify minimum detectable effect sizes. |

---

## 20. Claim-Evidence Table

| # | Claim | Evidence Used | Claim Type | Confidence | What Would Falsify This Claim |
|---|---|---|---|---|---|
| C1 | Pre-borrowing offer terms causally affect the take-up decision. | ITT estimate of Z_pre on Y_takeup from randomized offer variation; balance on pre-offer covariates across Z_pre arms. | Causal | High (if A1 holds) | No significant difference in take-up rates across Z_pre arms; or pre-treatment imbalance across arms. |
| C2 | Pre-borrowing offer terms causally shift the risk composition of accepted borrowers. | Significant θ₁ in risk-composition regression; shift in mean risk score across Z_pre arms among acceptors. | Causal (M1) | High (if A1 holds) | No difference in risk-score distribution among acceptors across Z_pre arms, despite different take-up rates. |
| C3 | Post-borrowing terms causally affect repayment behavior. | Significant γ₂ in repayment equation; Z_post randomly assigned and orthogonal to Z_pre; information separation test passes. | Causal (M2) | High (if A1–A5 hold) | γ₂ not significant; or information separation test fails; or post-acceptance imbalance across Z_post arms. |
| C4 | Selection and incentive effects are additive (do not interact). | γ₃ not significantly different from zero in the Z_pre × Z_post interaction term. | Causal (mechanism) | Moderate (depends on power) | Significant γ₃; or visual inspection of repayment-by-stratum plots shows non-parallel patterns. |
| C5 | Future-credit access incentives causally affect current repayment. | Significant γ₄ in future-access extension; orthogonal assignment of future-access terms. | Causal (M4) | High (if assignment is random and information-separated) | No difference in current repayment by future-access assignment; or information leakage to current stage. |
| C6 | The total repayment difference across Z_pre arms is decomposable into selection and incentive components. | Sum of γ₁ (residual selection) + observed compositional shift + γ₂-based incentive channel matches observed total difference. | Causal decomposition | High (under A1–A5) | Decomposition terms do not sum to observed total; or alternative decomposition methods produce qualitatively different allocations. |
| C7 | Observably riskier borrowers are differentially selected into the accepted pool under less generous Z_pre. | Interaction of Z_pre with pre-offer risk score in take-up equation; risk-gradient plot across Z_pre arms. | Descriptive pattern | Moderate | Risk gradient is flat or goes in the opposite direction. |
| C8 | The lender's internal risk score is a valid proxy for repayment propensity. | Correlation between pre-offer risk score and realized repayment among a holdout or pre-study sample. | Descriptive / diagnostic | Moderate | Risk score does not predict repayment in pre-study data; or correlation reverses in study period. |
| C9 | Attrition from the repayment sample is unrelated to treatment assignment. | Attrition rates do not differ significantly across Z_pre or Z_post arms. | Diagnostic | Moderate | Significant differential attrition by treatment arm; Lee bounds include zero but are wide. |
| C10 | Borrowers do not share assignment information with each other. | Absence of spatial or temporal clustering of outcomes; neighbors' assignments do not predict own outcomes. | Assumption (A4) | Moderate | Significant spatial autocorrelation of outcomes; neighbors' Z_pre or Z_post predict own Y_takeup or Y_repay. |

---

## Summary of Design Logic

```
┌──────────────────────────────────────────────────────────────────┐
│                    DESIGN LOGIC                                  │
├──────────────────────────────────────────────────────────────────┤
│                                                                  │
│  Z_pre (randomized) ──► Y_takeup ──► Accepted Sample            │
│       │                      │              │                    │
│       │                      │              ▼                    │
│       │                      │    Z_post (randomized, orthogonal)│
│       │                      │              │                    │
│       │                      │              ▼                    │
│       │                      └──────► Y_repay ◄─────────────────┤
│       │                                                          │
│       ▼                                                          │
│  Selection Channel (M1):                   Incentive Channel (M2):│
│  α₁ in take-up equation                    γ₂ in repayment eq    │
│  θ₁ in risk-composition eq                 (conditional on Z_pre)│
│                                                                  │
│  Information Separation (A3):                                    │
│  Z_post must NOT predict Y_takeup                                │
│  ⚠ If it does → channels are not separable                      │
│                                                                  │
│  Orthogonality (A5):                                             │
│  Z_pre ⟂ Z_post → decomposition identified                      │
│  ⚠ If not → channels confounded within Z_pre                    │
│                                                                  │
└──────────────────────────────────────────────────────────────────┘
```

**Bottom line:** With two-stage randomization and genuine information separation, the design cleanly identifies both selection and incentive channels and their interaction. Without these conditions — particularly if Z_post cannot be concealed from prospective borrowers or randomized independently — the strongest defensible analysis is a descriptive decomposition that acknowledges which components are causal and which are correlational.

## Tool Log Summary

- actual tool use: none
- trajectory `toolMetas`: []
- toolCall count: 0
- toolResult count: 0
- session_id: isolated_20260527_215707_98725_5
- session_log: /Users/jiangcanxiang/.openclaw/agents/benchmark_isolated/sessions/isolated_20260527_215707_98725_5.jsonl
- trajectory_log: /Users/jiangcanxiang/.openclaw/agents/benchmark_isolated/sessions/isolated_20260527_215707_98725_5.trajectory.jsonl

## Operator Notes

- duration_ms: 1615716
- stderr_excerpt: [plugins] plugins.allow is empty; discovered non-bundled plugins may auto-load: qqbot (/Users/jiangcanxiang/.openclaw/npm/node_modules/@openclaw/qqbot/dist/index.js), openclaw-weixin (/Users/jiangcanxiang/.openclaw/npm/node_modules/@tencent-weixin/openclaw-weixin/dist/index.js). Set plugins.allow to explicit trusted ids. [skills] Skipping escaped skill path outside its configured root: source=openclaw-managed root=~/.openclaw/skills reason=symlink-escape requested=~/.openclaw/skills/0-autoresearch-skill resolved=~/.orchestra/skills/0-autoresearch-skill [skills] Skipping escaped skill path outside its configured root: source=openclaw-managed root=~/.openclaw/skills reason=symlink-escape requested=~/.openclaw/skills/brainstorming-research-ideas resolved=~/.orchestra/skills/21-research-ideation/brainstorming-research-ideas [skills] Skipping escaped skill path outside its configured root: source=openclaw-managed root=~/.openclaw/skills reason=symlink-escape requested=~/.openclaw/skills/creative-thinking-for-research resolved=~/.orchestra/skills/21-research-ideation/creative-thinking-for-research [skills] Skipping escaped skill path outside its configured root: source=openclaw-managed r
