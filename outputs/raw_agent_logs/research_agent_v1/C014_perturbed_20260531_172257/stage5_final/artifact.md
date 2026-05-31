# Final Design Memo

**Case ID:** C014 (Perturbed Variant)
**Stage:** 5 — Final Memo with Critique Reconciliation

---

## 1. Executive Summary

This memo addresses whether monitoring interventions — formal oversight and community-based participation — reduce corruption or resource leakage in local public projects. The perturbed condition is decisive: **independent post-completion measurement is unavailable**. The researcher observes only official project reports and administrative records as outcome data.

Random assignment of projects to monitoring conditions supports a well-identified **intention-to-treat (ITT) estimate of monitoring's effect on reported expenditures**. However, the perturbation severs any empirical link between reported outcomes and true corruption. The ITT identifies a valid but wrong-target estimand: it captures what happens in administrative records, not what happens to actual resource use. The direction and magnitude of reporting bias are unknown and may differ across monitoring arms, making the ITT uninterpretable as evidence about corruption.

Two stronger candidates — a multi-arm reporting-channel decomposition and an anomaly-index proxy — are judged **not defensible** because their core interpretive steps are untestable without the independent measurement the perturbation removed. Every pattern they would produce has at least two observationally equivalent interpretations (real corruption change vs. reporting artifact).

**The only honest answer to the corruption research question is a descriptive analysis** that transparently documents associations between monitoring conditions and administrative reporting patterns, without claiming to identify causal effects on corruption. If the research objective is narrowed to the effect on reporting behavior itself, the RCT-ITT on reported expenditures provides a defensible causal estimate, with the caveat that it does not answer the original research question.

---

## 2. Research Question

Do monitoring interventions — formal oversight and community-based participation — reduce corruption or resource leakage in local public projects, and how do formal oversight and grassroots monitoring compare in their effects?

---

## 3. Target Estimand or Strongest Defensible Estimand

**Primary (descriptive fallback):** Descriptive association between assigned monitoring condition and administrative reporting patterns (expenditure levels, reporting completeness, milestone timing, complaint records, and constructed reporting-anomaly indices). No causal interpretation is attached.

**Secondary (narrowed causal estimand):** The average causal effect of monitoring assignment on officially reported project expenditures (ITT), estimated via random assignment. This estimand is internally valid but explicitly addresses *reporting behavior*, not *corruption*. The mapping from the ITT to any corruption-related claim is untestable under the perturbed condition.

**What is not a defensible estimand:** The average causal effect of monitoring on actual corruption or resource leakage. This estimand is not identifiable from administrative data alone when independent post-completion measurement is unavailable.

---

## 4. Treatment or Exposure and Main Outcomes

**Treatments (assigned at the project or community level, before implementation is complete):**

| Arm | Description |
|-----|-------------|
| T₁ | Formal oversight / audit assignment (increased probability of inspection, formal reporting requirements, or government audit visits) |
| T₂ | Community participation / information assignment (public disclosure of project details, community meetings, grassroots monitoring structures) |
| C | Control (no additional monitoring beyond standard administrative procedures) |

**Main outcomes (all from administrative records):**

| Outcome | Measurement |
|---------|-------------|
| Y₁ | Officially reported total project expenditures |
| Y₂ | Reported project completion status (binary or categorical milestone indicator) |
| Y₃ | Line-item expenditure detail (number of distinct expenditure categories reported) |
| Y₄ | Timing of administrative reporting (lag between milestone and report filing) |
| Y₅ | Complaint or process indicators (number of complaints filed, if recorded) |
| Y₆ | Constructed anomaly index (digit heaping, round-number clustering, timing anomalies, expenditure-completion discrepancies) |

**Critical limitation:** All outcomes are products of the same administrative reporting system that monitoring may itself affect. No independent measurement of project quality, actual costs, material quantities, or physical completion exists.

---

## 5. Data Structure Summary

| Dimension | Description |
|-----------|-------------|
| Unit of observation | Local public project (or village project) |
| Time structure | Staged cross-section: funding → assignment → implementation → completion → reporting |
| Assignment mechanism | Researcher- or government-controlled random assignment at the project or community level |
| Assignment timing | After funding, before implementation is complete |
| Treatment arms | Formal oversight (T₁), community monitoring (T₂), control (C) |
| Outcomes observed | Administrative expenditure reports, completion reports, process indicators |
| Independent validation | **None** — the perturbed condition removes all independent post-completion measurement |
| Compliance | Imperfect; assigned monitoring may not be fully implemented; community participation may vary |
| Spillover | Possible; officials/contractors may shift behavior across nearby projects; community information may spread |

---

## 6. Relevant Causal Mechanisms

The packet identifies multiple channels through which monitoring could affect both actual corruption and administrative reporting:

1. **Deterrence channel:** Monitoring increases the perceived probability of detection, reducing actual misappropriation. This would produce both lower reported expenditures (closer to true cost) and less actual leakage.

2. **Improved bookkeeping channel:** Monitoring induces more careful record-keeping. Reported expenditures become more complete and detailed, potentially increasing reported totals even if actual resource use is unchanged.

3. **Strategic misreporting channel:** Monitoring causes officials to conceal misappropriation through more sophisticated means rather than reducing it. Crude anomalies (digit heaping, round numbers) decrease, but corruption persists in subtler forms.

4. **Intimidation / reporting suppression channel:** Community monitoring may generate social pressure that suppresses complaint reporting or alters what gets officially recorded, creating discrepancies between administrative records and ground truth.

5. **Displacement / spillover channel:** Monitoring on some projects causes officials to shift corrupt activity to unmonitored projects, generating apparent treatment effects that reflect reallocation rather than reduction.

6. **Differential reporting completeness channel:** Monitoring conditions differ in whether they generate more complete administrative records, creating systematic differences in what gets observed that are unrelated to differences in underlying reality.

**The perturbed condition makes channels 1–5 indistinguishable from each other using administrative data alone.** A reduction in reported expenditures is equally consistent with deterrence (less theft), improved bookkeeping (more honest reporting replacing inflated claims), strategic misreporting (theft shifted off-books), or intimidation (under-reporting of legitimate expenses). No within-administrative-data test can separate these.

---

## 7. Main Identification Challenge

**The irreducible reporting-versus-reality confound.** The research objective is to estimate the effect of monitoring on *corruption or leakage* — a latent construct defined by the gap between actual resource use and officially recorded resource use. The perturbed condition removes the only measurement of actual resource use. The researcher observes:

- Official reports (R) under treatment (T) and control (C)
- True corruption (K) is unobserved

The observed difference E[R|T] − E[R|C] is:

> E[R|T] − E[R|C] = [E[K|T] − E[K|C]] + [E[B|T] − E[B|C]]

where B is reporting bias (R = K + B, or more generally some unknown function relating truth to report). The first bracketed term is the effect on corruption (the estimand of interest). The second is the differential reporting bias induced by treatment. **Without observing K, neither term is separately identified.** Random assignment identifies the sum, not the components.

Additional challenges (compounding but secondary to the main confound):

- **SUTVA violations are undetectable:** Spillover cannot be diagnosed or corrected without independent observation in untreated units.
- **Compliance is unverifiable:** Whether assigned monitoring was actually implemented cannot be confirmed from administrative records alone.
- **Differential reporting completeness:** Monitoring arms may generate systematically different rates of missing or incomplete reports.

---

## 8. Whether Credible Causal Identification Is Possible

**For the effect on corruption or leakage: No.** The perturbation removes the measurement link between administrative reports and true corruption. No within-study design — no decomposition, no proxy construction, no anomaly index — can reconstruct this link without external validation data that the perturbation explicitly makes unavailable. Credible causal identification of the corruption effect is not possible under the given constraints.

**For the effect on reporting behavior: Yes, limited.** Random assignment supports an internally valid ITT estimate of monitoring's effect on reported expenditures and other administrative outcomes. This estimand is well-defined but does not answer the research question about corruption. It answers a different question: "Does monitoring change what gets recorded in official project reports?"

This conclusion is consistent with the Stage 4 critic's verdicts: Candidate 1 (`defensible_with_caveats`) is valid for the reporting estimand but not for corruption; Candidates 2 and 3 (`not_defensible`) attempt to bridge this gap with untestable assumptions; Candidate 4 (`defensible`) is the honest answer to the corruption question.

---

## 9. Proposed Empirical Design: Descriptive Association with Optional ITT on Reporting

Given the critique's verdicts, I propose a **two-tier analysis**:

### Tier 1: Descriptive Monitoring-Reporting Association (Primary)

This is the strongest defensible answer to the research question about *corruption*. The analysis documents how administrative reporting patterns differ across monitoring conditions without interpreting these differences as evidence about corruption.

**Analysis steps:**

1. Report balance checks on baseline project characteristics (type, size, location, timing) across assigned monitoring arms, using the random assignment to assess whether arms are comparable on observables.

2. Compute and report unconditional means and distributions of each outcome variable (Y₁–Y₆) by assigned monitoring arm.

3. Estimate differences in outcomes across arms, conditional on baseline covariates, using the regression specification in Section 12. Present these as *descriptive associations*, not causal effects on corruption.

4. Disaggregate outcomes by report type (expenditure reports vs. milestone reports vs. complaint records) to document whether associations differ across reporting dimensions — without attributing divergence to differential corruption reduction.

5. Construct and report the anomaly index (Y₆) as a descriptive measure of reporting quality, explicitly noting that it cannot be validated as a corruption proxy.

**Interpretive discipline:** All results are framed as "Projects assigned to monitoring condition X showed, on average, [higher/lower/different] administrative reporting patterns on dimension Y compared to projects assigned to condition Z." No claim is made about whether these differences reflect changes in corruption, changes in reporting behavior, or both.

### Tier 2: ITT on Reported Expenditures (Secondary, with Explicit Caveats)

If the research question is narrowed to "Does monitoring change what gets reported?", the RCT supports a clean ITT estimate:

- **Estimand:** ATE of monitoring assignment on reported expenditures and related administrative outcomes.
- **Identification:** Random assignment of projects to monitoring arms.
- **Caveat:** This estimand does not answer the question about corruption.

**Why this two-tier approach reconciles the critique:**

- Candidate 1 (`defensible_with_caveats`) is preserved as Tier 2 with its caveat explicitly elevated to primary importance.
- Candidate 4 (`defensible`) is elevated to Tier 1 as the honest answer to the corruption research question.
- Candidates 2 and 3 (`not_defensible`) are not pursued, consistent with the critic's verdict that their decompositions and proxies are untestable without independent measurement.

---

## 10. Why the Design Is Valid — and Why Causal Identification of Corruption Is Not Credible

**Tier 1 (descriptive) validity:** The analysis makes no causal claims about corruption, so no causal identification is required. Random assignment ensures that the descriptive comparisons are made across groups that are comparable on baseline observables and unobservables, but this does not license causal interpretation because the outcome measurement itself is affected by treatment in unknown ways.

**Tier 2 (reporting ITT) validity:** Random assignment supports internal validity for the effect on reported outcomes. The standard IV/RCT logic applies: assignment is (by construction) independent of potential outcomes, so the difference in mean reported outcomes across arms identifies the ITT. The validity concern is not internal but *construct*: the ITT identifies an effect on reporting, not on corruption.

**Why causal identification of corruption is not credible:**

Four irreducible problems, each of which is independently fatal:

1. **Reporting bias is unidentified.** E[R|T] − E[R|C] = treatment effect on corruption + differential reporting bias. Neither component is separately identified without observing true corruption. Random assignment does not solve this; it only ensures a clean estimate of the sum.

2. **The sign of reporting bias is unknown.** Monitoring could increase or decrease reported expenditures relative to truth depending on whether deterrence, improved bookkeeping, strategic misreporting, or intimidation dominates. The ITT could be positive, zero, or negative under any true corruption effect.

3. **No external benchmark exists for validation.** The perturbation explicitly removes independent post-completion measurement. Without it, no anomaly index, decomposition, or proxy can be calibrated. These exercises measure reporting quality under different names — not corruption.

4. **Spillover is undetectable.** Displacement of corruption to unmonitored projects would produce apparent treatment effects that vanish when the broader system is considered, but this cannot be detected or corrected without observing unmonitored projects' true outcomes.

---

## 11. Required Assumptions

### Tier 1 (Descriptive Association)

| # | Assumption | Justification / Testability |
|---|-----------|---------------------------|
| A1 | Monitoring assignment and outcome reporting are measured without systematic error in the assignment variable itself | Assignment is researcher/government-controlled and should be well-documented |
| A2 | No differential attrition from the administrative record across arms | Testable: compare rates of missing reports across arms |
| A3 | Administrative data are consistently generated across arms (same systems, same reporting requirements) | Partially testable: compare report filing dates, completeness rates |

**No causal identification assumptions are required because no causal claims about corruption are made.**

### Tier 2 (ITT on Reporting)

| # | Assumption | Justification / Testability |
|---|-----------|---------------------------|
| B1 | Random assignment is successfully implemented | Testable via balance checks on baseline covariates |
| B2 | SUTVA: no interference across projects in *reporting* outcomes | Untestable (no independent data from potential spillover recipients) |
| B3 | No differential attrition from outcome measurement | Testable as in A2 |
| B4 | Exclusion restriction (for IV interpretation): assignment affects corruption only through monitoring receipt | Plausible if assignment is blinded or has no independent effect |

**Critically, the following assumption is NOT MADE and cannot be justified:**
- *B5: Reported expenditures are an unbiased measure of true expenditures.* This is precisely what the perturbation removes. Without B5, the ITT does not identify the corruption effect.

---

## 12. Statistical Model or Analysis Equation

### Tier 1: Descriptive Specification

For outcome k in project i assigned to arm a:

> Y_{ik} = α_k + Σ_{a∈{T₁,T₂}} β_{ak} · 1[Arm_i = a] + γ_k' X_i + ε_{ik}

where:
- Y_{ik} is administrative outcome k for project i
- Arm_i ∈ {C, T₁, T₂} is assigned monitoring condition (C = control omitted)
- X_i is a vector of baseline covariates (project type, size, location, timing)
- β_{ak} is the *descriptive association* between assignment to arm a and outcome k, conditional on X_i

**Interpretation:** β̂_{ak} describes how outcomes differ on average across assigned arms. No causal interpretation is attached. Confidence intervals are computed using cluster-robust standard errors at the community level (if assignment is at the community level) or heteroskedasticity-robust standard errors (if assignment is at the project level).

### Tier 2: ITT Specification (Narrowed to Reporting)

> Y_i = α + τ₁ · 1[Arm_i = T₁] + τ₂ · 1[Arm_i = T₂] + δ' X_i + ν_i

where:
- Y_i is reported project expenditure (primary) or other administrative outcome
- τ₁ is the ITT of formal oversight assignment on reported expenditures
- τ₂ is the ITT of community monitoring assignment on reported expenditures
- X_i is baseline covariates (included for precision; τ identified without them under random assignment)

**Estimand under random assignment:**

> τ₁ = E[Y_i(1,0) − Y_i(0,0)]  (ITT of formal oversight)
> τ₂ = E[Y_i(0,1) − Y_i(0,0)]  (ITT of community monitoring)

where Y_i(t₁,t₂) is the potential reported outcome under treatment assignment (t₁,t₂).

**Comparison of arms:**

> τ₁ − τ₂ = E[Y_i(1,0) − Y_i(0,1)]

This difference identifies the differential effect of formal oversight vs. community monitoring on *reported* outcomes — not on corruption.

---

## 13. Robustness, Placebo, Falsification Checks, and Diagnostic Tests

### Tests feasible under the perturbed condition:

1. **Balance checks (ITT internal validity):** Regress baseline covariates (project type, size, location dummies, funding amount, pre-assignment reporting patterns if available) on treatment assignment. Under successful randomization, these should be jointly insignificant (F-test).

2. **Attrition analysis:** Test whether the probability of observing a completed administrative report differs across arms. Differential missingness would indicate systematic reporting-coverage effects of monitoring.

3. **Pre-treatment outcome placebo:** If any administrative data exist from before assignment (e.g., initial funding disbursement recording), test whether pre-treatment reporting patterns differ across arms. Under randomization, pre-treatment outcomes should be balanced.

4. **Distributional analysis of reported expenditures:** Beyond mean differences, examine whether monitoring shifts the entire distribution (variance, quantiles) of reported expenditures. A mean-preserving compression of the distribution would be informative about reporting standardization effects, even if not interpretable as corruption reduction.

5. **Sensitivity analysis for reporting-bias magnitude:** For the ITT on reported expenditures, compute the minimum differential reporting bias (as a proportion of the control-group mean) that would be required to explain the observed ITT under a null corruption effect. This bounds the vulnerability of the estimate without quantifying it precisely.

### Tests infeasible under the perturbed condition (explicitly noted):

- **Validation of anomaly index against ground truth:** Cannot calibrate Y₆ without independent measurement of actual corruption.
- **SUTVA diagnostics:** Cannot test for spillover without observing outcomes in untreated units that are near treated units on some independent metric.
- **Audit-based outcome validation:** Cannot compare administrative reports to independent technical or financial audits.
- **Physical output verification:** Cannot verify that reported completion corresponds to physical completion.

---

## 14. Heterogeneity Analysis

Heterogeneity analysis is supportable for the descriptive associations (Tier 1) and for the ITT on reporting (Tier 2), provided sub-group comparisons are pre-specified and interpreted as descriptive patterns rather than causal moderation.

**Pre-specified dimensions:**

| Dimension | Rationale | Interpretation Caution |
|-----------|-----------|----------------------|
| Project size (above/below median funding) | Monitoring may have different reporting effects in large vs. small projects | Cannot attribute differential patterns to differential corruption effects |
| Project type (infrastructure vs. service delivery) | Reporting practices and monitoring intensity may differ by type | Type-specific reporting norms may drive heterogeneity independently of monitoring |
| Community characteristics (urban/rural, literacy rates if available) | Community monitoring effectiveness may depend on community capacity | Observed heterogeneity could reflect differential reporting completeness, not differential monitoring effects |
| Implementation timing (early vs. late cohorts) | Learning effects in monitoring implementation or reporting | Cohort effects may confound monitoring with secular trends in administrative quality |

**Analysis approach:** For each dimension D, estimate:

> Y_i = α + Σ_a τ_{a} · 1[Arm_i = a] + Σ_a θ_{a} · 1[Arm_i = a] · D_i + λ · D_i + δ' X_i + ν_i

and report θ̂_{a} as the differential association by subgroup. All heterogeneity results are accompanied by the explicit statement that they describe differential *reporting* patterns, not differential *corruption reduction*.

---

## 15. Measurement, Compliance, Missingness, Spillover, and Implementation Limits

### Measurement

| Issue | Severity | Mitigation |
|-------|----------|------------|
| All outcomes from administrative records | **Fundamental** | Acknowledge. No mitigation possible without independent data. |
| No independent cost or quality measurement | **Fundamental** | The perturbation makes this the central constraint. |
| Anomaly index (Y₆) unvalidated | **High** | Present as descriptive reporting-quality metric only; do not label as corruption proxy. |
| Reporting definitions may differ across projects/regions | **Moderate** | Document any known differences in administrative definitions; include region fixed effects. |

### Compliance

| Issue | Severity | Mitigation |
|-------|----------|------------|
| Assigned monitoring may not be implemented | **High** | ITT preserves internal validity for assignment effect but cannot estimate treatment-on-treated without compliance data. Record any available implementation indicators. |
| Community participation varies within arm | **High** | Without independent field data, compliance is unobservable. The ITT is the only defensible estimand. |
| No compliance data from independent source | **Fundamental** | Explicitly note that the analysis estimates the effect of *assignment*, not *receipt*. |

### Missingness

| Issue | Severity | Mitigation |
|-------|----------|------------|
| Differential report completion across arms | **High** | Test for differential missingness (Section 13, check 2). If present, it is itself an outcome of monitoring and should be reported. |
| Missing baseline data for some projects | **Moderate** | Document missingness patterns; use complete-case analysis with sensitivity checks. |

### Spillover

| Issue | Severity | Mitigation |
|-------|----------|------------|
| Officials/contractors shifting behavior across projects | **Potentially high** | Cannot be detected or corrected without independent data. Note as a limitation; the ITT estimates are contaminated by spillover in unknown direction and magnitude. |
| Community information spreading beyond assigned units | **Potentially high** | Same as above. If assignment is geographically clustered, consider spatial buffer zones between clusters (requires geographic data). |

### Implementation Limits

| Issue | Severity | Mitigation |
|-------|----------|------------|
| Assignment timing relative to implementation | **Moderate** | Projects already underway at assignment may have pre-existing reporting patterns. Control for implementation stage at assignment. |
| Administrative data quality varies across jurisdictions | **Moderate** | Include jurisdiction fixed effects; document any known quality differences. |

---

## 16. Failure Modes and Alternative Explanations

### For the ITT on reported expenditures (Tier 2):

1. **Differential reporting bias produces a spurious treatment effect.** Formal oversight (T₁) induces more complete and honest bookkeeping, increasing reported expenditures, while community monitoring (T₂) intimidates officials into under-reporting. The observed ITT difference τ̂₁ − τ̂₂ could be entirely driven by opposite-sign reporting biases even if neither arm reduced actual corruption.

2. **Monitoring changes the composition of what gets reported, not corruption.** If community monitoring leads to more line items being reported (greater detail) but the same total, and formal oversight leads to fewer but larger line items (aggregation), expenditure totals could appear identical while reporting processes differ substantially. The ITT on total expenditure would be zero despite both arms having real effects on reporting.

3. **Differential attrition from the administrative record.** If projects under formal oversight are more likely to file final reports (because auditors demand them), the set of observed projects differs across arms. An ITT estimated on observed reporters would confound the reporting effect with a selection effect.

4. **Spillover generates sign reversals.** If formal oversight in treated projects causes officials to shift corrupt activity to nearby control projects, control-group reported expenditures would be inflated relative to a no-spillover counterfactual, making the treatment effect appear larger (or even sign-reversed) relative to the true total-system effect.

5. **Implementation timing confounds monitoring with project maturity.** If monitoring assignment occurs at different stages of project implementation across arms and implementation stage is not perfectly controlled, the ITT would partially reflect differential project maturity rather than monitoring.

### For the descriptive association (Tier 1):

6. **Reporting completeness confounds create spurious patterns.** If formal oversight generates more complete records while community monitoring generates more complaints (by design), these are true effects of monitoring on reporting but are not interpretable as evidence about corruption.

7. **Baseline imbalance despite randomization.** If randomization fails (e.g., due to political interference in assignment), the descriptive comparisons are confounded by pre-existing differences across arms. This is testable via balance checks.

### Alternative explanations applicable to all candidates:

8. **All observed patterns are reporting artifacts.** Under the perturbation, the null hypothesis "monitoring has zero effect on corruption" is observationally equivalent to "monitoring has a non-zero effect on corruption that is exactly offset by a reporting-bias effect of equal magnitude and opposite sign." This equivalence cannot be broken without independent measurement.

---

## 17. What Cannot Be Claimed

In light of the Stage 4 critique and the perturbed condition, the following claims **cannot be made** from this study:

1. **Cannot claim that monitoring reduces corruption or resource leakage.** The perturbation removes the only measurement link between administrative reports and true corruption. Any statement about corruption reduction would be an untestable extrapolation from reporting data.

2. **Cannot claim that formal oversight is more or less effective than community monitoring at reducing corruption.** The multi-arm decomposition (Candidate 2) is `not_defensible`: every differential pattern across arms has at least two observationally equivalent interpretations, and the perturbation precludes resolving this ambiguity.

3. **Cannot claim that constructed anomaly indices measure corruption reduction.** The anomaly-index proxy (Candidate 3) is `not_defensible`: the anomaly-to-corruption mapping is entirely untestable without independent measurement, and treatment may change this mapping in unknown ways.

4. **Cannot claim that SUTVA holds or that spillover is absent.** Spillover is undetectable and uncorrectable without independent observation of outcomes in unmonitored projects that may be affected by displacement.

5. **Cannot claim that compliance is perfect or that the treatment-on-treated (TOT) effect is identified.** Without independent field verification of monitoring implementation, only the ITT (effect of assignment) is identified.

6. **Cannot claim that the study design "compares formal oversight with grassroots monitoring" with respect to corruption.** The comparison is valid for *reported* outcomes only. The packet's explicit question about comparing these approaches for corruption reduction cannot be answered from these data.

7. **Cannot claim that null ITT results imply no monitoring effect.** A zero ITT on reported expenditures is consistent with (a) no effect on corruption, (b) offsetting corruption reduction and reporting-bias effects, (c) offsetting deterrence and displacement effects, or (d) monitoring having effects only on dimensions not captured by expenditure totals.

The critic's verdict on Candidates 2 and 3 as `not_defensible` is adopted in full. I find no packet-local evidence that the critic missed: the perturbation explicitly removes independent measurement, and the packet itself warns that "official records may not cleanly reveal true corruption outcomes." These two facts jointly preclude any claim of corruption identification from administrative data alone.

---

## 18. Additional Data Needed

To move from the descriptive fallback to credible causal identification of corruption effects, the following data would be required (in descending order of importance):

| Priority | Data Need | What It Would Enable |
|----------|-----------|---------------------|
| **Critical** | Independent post-completion measurement: technical audits, physical inspections, independent cost estimates, or beneficiary surveys measuring project quality and value | Calibration of the reporting-to-corruption mapping; validation of anomaly indices; separation of reporting effects from corruption effects |
| **High** | Independent compliance/monitoring-implementation data: field verification that assigned monitoring actually occurred, with what intensity, and with what participation levels | Estimation of treatment-on-treated (TOT) effects via instrumental variables; diagnosis of compliance heterogeneity |
| **High** | Spatial/network data on project locations and administrative jurisdictions | Diagnosis and modeling of spillover; construction of buffer zones; partial identification of spillover bounds |
| **Moderate** | Pre-assignment outcome data from independent sources (e.g., prior audits, prior project evaluations) | Placebo tests on pre-treatment corruption proxies; validation of the corruption measurement model |
| **Moderate** | Qualitative process data: interviews with officials, contractors, and community members about how monitoring changed behavior | Triangulation of mechanisms; contextualization of quantitative patterns |

**Without the critical item (independent measurement), no amount of additional administrative or process data can bridge the reporting-corruption gap.** The perturbation is binding.

---

## 19. Threat-Response Table

The task packet does not explicitly request a threat-response table. However, for completeness:

| Threat | Response | Residual Risk |
|--------|----------|---------------|
| Reporting-vs.-reality confound | Acknowledge as irreducible; adopt descriptive fallback; clearly separate reporting ITT from corruption claims | High. No mitigation possible without independent data. |
| SUTVA / spillover | Acknowledge; document as limitation; note direction of potential bias is unknown | High. Undetectable without spatial data and independent outcomes. |
| Differential reporting completeness | Test for differential missingness across arms; report any imbalance as an outcome of monitoring itself | Moderate. Can be detected but not corrected. |
| Compliance / implementation fidelity | ITT preserves internal validity; explicitly note that TOT is unidentified | Moderate. ITT is the appropriate policy-relevant estimand for assignment-based interventions. |
| Anomaly-index invalidity | Present anomaly index only as a descriptive measure of reporting quality; do not label as corruption proxy | Low after downgrade. Risk is removed by not making the invalid claim. |
| Baseline imbalance | Test via balance checks; include covariates if imbalance detected | Low. Randomization is testable on observables. |
| Differential attrition | Test; report as outcome if present | Moderate. Can be detected but selection-correction requires assumptions. |

---

## 20. Claim-Evidence Table

| Claim | Evidence Used | Claim Type | Confidence | What Would Falsify This Claim |
|---|---|---|---|---|
| C1: Random assignment to monitoring arms was successfully implemented | Balance tests on baseline covariates (project type, size, location, timing); documentation of assignment protocol | **Descriptive / design integrity** | High (testable) | Significant joint F-test on baseline covariates predicting treatment assignment; evidence of political interference or non-random assignment in protocol documentation |
| C2: Monitoring assignment affects officially reported project expenditures (ITT) | Random assignment; comparison of mean reported expenditures across arms; regression estimates τ̂₁, τ̂₂ with robust standard errors | **Causal (narrowed to reporting)** | Moderate–High (internal validity from randomization; construct validity limited) | Failure of randomization (C1 falsified); differential attrition from outcome measurement; evidence that assignment directly affects reporting independently of monitoring (violation of exclusion restriction for IV interpretation) |
| C3: Formal oversight and community monitoring produce different patterns of administrative reporting | Differential ITT estimates across arms for multiple outcome dimensions (expenditures, milestones, complaints, anomaly index); test of τ̂₁ = τ̂₂ for each outcome | **Descriptive association** | Moderate (internal validity from randomization; multiple outcomes provide convergent evidence) | No significant differences across any outcome dimension; differences attributable entirely to differential missingness rather than differential reporting content |
| C4: Monitoring does not cause differential attrition from the administrative record | Test of missing-report probability across arms; comparison of report-filing rates | **Descriptive** | Moderate (testable for observed reports) | Significant difference in report-filing rates across arms |
| C5: The anomaly index captures reporting quality | Construct validity argument from digit-preference literature; cross-validation across anomaly dimensions within administrative data | **Descriptive** | Low (no external validation possible under perturbation) | No correlation between anomaly dimensions that should be correlated if driven by common reporting-quality variation; pattern of anomalies differs qualitatively from established findings in digit-preference literature |
| C6: Formal oversight reduces corruption more than community monitoring (or vice versa) | — | **Cannot be claimed** | — | — |
| C7: Monitoring reduces corruption or resource leakage | — | **Cannot be claimed** | — | — |
| C8: Observed reporting differences reflect real differences in project outcomes | — | **Cannot be claimed** | — | — |

---

## Reconciliation Summary

| Candidate | Critic Verdict | Memo Treatment | Rationale |
|-----------|---------------|----------------|-----------|
| RCT on Reported Expenditures (ITT) | `defensible_with_caveats` | **Adopted as Tier 2**, with the caveat elevated to primary framing: identifies effects on reporting, not corruption | The critic correctly identifies that internal validity for the reporting estimand survives but the research question about corruption is not answered. The memo treats this as a valid but wrong-target estimand. |
| Multi-Arm Reporting-Channel Decomposition | `not_defensible` | **Not pursued** | The critic's assessment is adopted: every differential pattern has observationally equivalent interpretations under the perturbation. No packet-local evidence contradicts this verdict. |
| Anomaly-Index Proxy Outcomes | `not_defensible` | **Not pursued as corruption proxy**; anomaly index retained only as a descriptive reporting-quality metric | The critic's assessment is adopted: the mapping is untestable and treatment may change it. The memo uses anomaly indices only for descriptive purposes, explicitly disclaiming any corruption interpretation. |
| Descriptive Fallback | `defensible` | **Adopted as Tier 1 (primary)** | The critic's assessment is adopted: this is the only honest answer to the corruption research question. The memo elevates it to the primary analysis, consistent with the packet's instruction to downgrade claims when causal identification is not credible. |