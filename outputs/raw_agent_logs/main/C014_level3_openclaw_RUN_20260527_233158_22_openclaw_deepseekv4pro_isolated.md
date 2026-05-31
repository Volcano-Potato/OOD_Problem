# Raw Agent Run Log

- `run_id`: RUN_20260527_233158_22_openclaw_deepseekv4pro_isolated
- `case_id`: C014
- `variant_id`: level3
- `level`: level3
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
- `timestamp`: 2026-05-27T23:31:58+0800
- `input_file`: benchmark/cases/C014_corruption_monitoring/agent_task_level3.md
- `system_prompt_summary`: workspace=/Users/jiangcanxiang/OpenClawBenchmarkIsolated; thinking=high; actual_tool_use=none; agent=benchmark_isolated
- `contamination_status`: unknown
- `contamination_reason`: pending manual content review; actual tool use=none
- `status`: success

## Raw Agent Output

# Research Design: Monitoring Interventions and Corruption in Local Public Projects

---

## 1. Executive Summary

This design proposes a multi-arm field experiment in which local public projects are assigned to (i) a pure control condition with standard administrative processes, (ii) increased formal oversight (e.g., audit probability or inspection intensity), and (iii) a community-based monitoring intervention (e.g., information disclosure plus structured participation). The central measurement innovation is that outcomes are derived from *independently collected post-completion evidence* — technical audits, physical input verification, or quality assessments conducted by teams outside the implementing agency — rather than from the implementing institution's own administrative records, which may be strategically misreported. This design allows estimation of (a) whether monitoring reduces resource leakage relative to control, (b) whether formal and community-based monitoring differ in effectiveness, and (c) the extent to which official reports diverge from independently verified inputs and outputs. The design also incorporates diagnostic tests for spillover, substitution across leakage dimensions, and differential attrition. The key identification requirement — that assignment to monitoring conditions is orthogonal to potential outcomes — is secured if the researcher or a cooperating government partner implements random assignment before projects complete their major procurement and construction decisions. Without random assignment, the design defaults to the strongest defensible difference-in-differences or instrumental-variables analysis using whatever source of exogenous variation in monitoring is actually available, but the packet indicates researcher/government-controlled assignment, making randomization the natural benchmark.

---

## 2. Research Question

Do monitoring interventions — formal oversight and community-based monitoring — reduce corruption or resource leakage in local public projects, and through what channels do they operate? Specifically:

- **RQ1:** What is the causal effect of assigning a project to increased formal oversight (relative to no additional monitoring) on independently measured resource leakage?
- **RQ2:** What is the causal effect of assigning a project to a community-based monitoring intervention (relative to no additional monitoring) on independently measured resource leakage?
- **RQ3:** Do formal oversight and community-based monitoring differ in their effects on leakage, and if so, do the differences align with distinct causal mechanisms (deterrence via detection probability vs. accountability via local information and voice)?
- **RQ4:** To what extent do official administrative expenditure reports diverge from independently verified expenditures, and does this divergence itself respond to monitoring assignment?

---

## 3. Target Estimand (or Strongest Defensible Estimand)

**Primary estimand:** The intention-to-treat (ITT) effect of random assignment to a monitoring condition on the project-level leakage rate, defined as:

\[
\tau_k = \mathbb{E}[Y_i(1_k) - Y_i(0)]
\]

where \(Y_i(1_k)\) is the potential outcome under assignment to monitoring arm \(k \in \{\text{formal, community}\}\) and \(Y_i(0)\) is the potential outcome under the pure control condition. The leakage outcome \(Y_i\) is measured as the percentage discrepancy between independently verified project expenditures (or physical input quantities valued at market prices) and officially reported expenditures, normalized by the project's planned budget.

**Secondary estimands:**
- The local average treatment effect (LATE) among compliers, if non-compliance with assigned monitoring is substantial and an instrument for actual monitoring receipt is available.
- The difference \(\tau_{\text{formal}} - \tau_{\text{community}}\), which identifies the comparative effectiveness of the two monitoring approaches.

**If randomization is not feasible:** The strongest defensible estimand shifts to a conditional-on-observables comparison (e.g., propensity-score-weighted or regression-adjusted difference in leakage between monitored and unmonitored projects), with the explicit caveat that unobserved determinants of both monitoring assignment and leakage cannot be ruled out. In that case, the design yields a *descriptive association* rather than a causal estimate, and the threat-response table below identifies which confounders remain uncontrolled.

---

## 4. Treatment or Exposure and Main Outcomes

### Treatment Arms

| Arm | Label | Description |
|-----|-------|-------------|
| T0 | Pure control | Projects proceed under standard administrative procedures with no additional monitoring beyond routine reporting requirements. |
| T1 | Formal oversight | Projects are assigned to an increased probability of formal audit or inspection. This could mean: (a) announcing that the project *will* be audited after completion, (b) scheduling intermediate inspections, or (c) increasing the frequency or depth of official reviews. The key feature is that the monitoring is conducted by a *hierarchically superior or independent government body*, not by the project's own administrators. |
| T2 | Community-based monitoring | Projects (or the communities they serve) receive: (a) information about the project's planned budget, timeline, and specifications, and (b) a structured mechanism for community participation in oversight — e.g., community scorecards, public expenditure tracking meetings, or a grievance/feedback mechanism. The key feature is that monitoring relies on *local beneficiaries' information and voice* rather than on top-down bureaucratic enforcement. |

A factorial or combined arm (T1 + T2) could be included if sample size permits, to test whether formal and community monitoring are complements or substitutes.

### Main Outcomes

1. **Primary leakage measure:**  
   \[
   \text{Leakage}_i = \frac{\text{Independently verified cost}_i - \text{Officially reported cost}_i}{\text{Planned budget}_i}
   \]
   where independently verified cost is constructed from technical audits, physical input counts, materials testing, or labor verification conducted by an external enumerator team after project completion. This measure does not rely on the implementing agency's self-reports. A positive value indicates that independently verified inputs exceeded reported spending (suggesting unreported diversion elsewhere or inflated reporting of non-verifiable items); a negative value suggests that reported spending exceeded verifiable inputs (suggesting over-reporting or ghost expenditures). Both directions can indicate corruption, and the design should analyze the absolute discrepancy or, preferably, disaggregate the two directions.

2. **Objective quality measure:** If the post-completion measurement includes technical quality assessments (e.g., engineering ratings, materials specifications compliance, functional tests), a standardized quality index provides a complementary outcome that may be harder for officials to manipulate on short notice than financial accounts.

3. **Official-report divergence:** The signed ratio of officially reported to independently verified expenditures, analyzed as an outcome in its own right. This captures whether monitoring causes officials to bring their reports closer to (or further from) independently verifiable reality.

### Secondary Outcomes

- Process indicators: number of community meetings held, complaints filed, audit flags raised.
- Implementation milestones: on-time completion, budget adherence (as officially reported).
- Alternative leakage proxies: unit-cost comparisons across projects; discrepancies between quantities in procurement documents and quantities physically observed.

---

## 5. Data Structure Summary

| Stage | Timing | Data Collected |
|-------|--------|----------------|
| Stage 1: Baseline | Before treatment assignment | Project characteristics (budget, type, location, planned timeline), community baseline covariates (population, poverty measures, prior project experience, baseline infrastructure quality), implementing agency and contractor identifiers. |
| Stage 2: Assignment & announcement | After baseline, before major implementation decisions | Random assignment to treatment arms; verification that announcement reached the relevant actors (project managers, contractors, community representatives). |
| Stage 3: Implementation | During project execution | Administrative milestones (expenditure reports, progress reports, procurement records), process indicators (meetings, complaints, inspection visits), intermediate outputs. |
| Stage 4: Post-completion measurement | After project completion | Independent technical audit (physical input verification, quality assessment, market-price valuation of observed inputs), official final expenditure report, community survey on perceived quality and satisfaction. |

The unit of observation is the project (or project-community pair). The design is primarily cross-sectional with staged data collection, but implementation milestones provide a limited panel structure for intermediate checks. Repeated measures within a project (e.g., multiple inspection visits, multiple community meetings) can be aggregated to the project level for primary analysis.

---

## 6. Relevant Causal Mechanisms

The packet identifies four distinct mechanisms that the design should attempt to distinguish:

### Mechanism 1: Deterrence via expected detection (formal oversight channel)
Formal oversight increases the perceived probability that diversion will be detected and punished by an external authority (auditor, inspector, higher-level government). This operates through *top-down incentives*: officials and contractors reduce leakage because they fear sanctions. The mechanism predicts that formal oversight should be most effective when (a) the audit/inspection probability is credibly high, (b) sanctions are meaningful, and (c) officials believe they cannot manipulate the audit process itself.

### Mechanism 2: Accountability via information and voice (community monitoring channel)
Community-based monitoring improves the flow of information from beneficiaries to authorities and/or empowers beneficiaries to demand accountability. This operates through *bottom-up pressure*: officials reduce leakage because they face social sanctions, reputational costs, or complaints that trigger formal investigations. The mechanism predicts that community monitoring should be most effective when (a) beneficiaries have sufficient information to detect problems, (b) voice mechanisms are credible (complaints lead to action), and (c) collective action problems among beneficiaries are surmountable.

### Mechanism 3: Strategic reporting manipulation
Because the same actors who may divert resources also produce official records, monitoring may change *what is reported* without changing *what actually happens*. For example, an audit threat could cause officials to improve the appearance of their books without reducing actual leakage — or even increase leakage in dimensions not covered by the audit. This mechanism implies that official-records-based outcome measures will confound real behavioral change with reporting change.

### Mechanism 4: Substitution across leakage dimensions
If monitoring covers only some dimensions of project implementation (e.g., materials quantities but not labor quality, or procurement prices but not specification compliance), officials may substitute corruption into unmonitored dimensions. Total corruption may remain unchanged even as measured leakage falls. This mechanism implies that single-dimension outcome measures may overstate treatment effects.

The design addresses these mechanisms by (a) using independently collected outcomes to separate real effects from reporting effects (Mechanism 3), (b) measuring multiple outcome dimensions to detect substitution (Mechanism 4), and (c) testing for heterogeneity across treatment arms and project characteristics to shed light on Channels 1 and 2 — though fully *proving* a specific mechanism requires additional assumptions or experimental variation in mechanism components that this design alone may not provide.

---

## 7. Main Identification Challenge

The core identification challenge is that **unobserved determinants of corruption may be correlated with monitoring assignment**. Even with researcher/government-controlled assignment, the following concerns arise:

1. **Non-random assignment (selection):** If monitoring is targeted toward high-risk projects or politically salient ones, the simple difference between monitored and unmonitored projects conflates treatment effects with baseline differences in corruption propensity. Random assignment solves this. Without it, the design must rely on an explicit source of quasi-experimental variation (e.g., administrative rules, budget thresholds, phase-in rollouts).

2. **Measurement of the outcome itself is contaminated by the treatment (measurement):** If outcomes are drawn from official records that the treatment may affect through reporting behavior rather than real behavior, then even a well-identified design estimates the effect on *what is reported*, not on *what happened*. The design addresses this by constructing outcomes from independently collected post-completion evidence, but this solution introduces its own challenges: independent measurement may be costly, may cover only a subset of project dimensions, and may itself be subject to error or manipulation.

3. **Spillover contaminates the control group:** If officials or contractors who learn about monitoring in treated projects adjust their behavior in control-group projects, the estimated treatment effect is attenuated (closer to zero), potentially masking real effects. This requires measuring spatial or administrative proximity and testing for spillover.

4. **Timing and announcement effects:** If monitoring is assigned or announced after key implementation decisions are locked in, the treatment cannot affect behavior during those decisions, and the estimated effect reflects only post-announcement adjustments. This dilutes the estimand and potentially mischaracterizes which decisions monitoring can affect.

---

## 8. Whether Credible Causal Identification Is Possible

**Yes, credible causal identification is possible**, conditional on the following being true in the actual implementation:

1. **Random assignment is feasible and implemented.** The packet states that assignment is "researcher- or government-controlled" at the project or community level, which is consistent with randomization. If the cooperating government or program administrator can commit to random assignment before projects begin major implementation, the design yields internally valid ITT estimates.

2. **Independent post-completion measurement can be conducted.** The packet states that researchers "may be able to collect additional post-completion evidence on project quality or actual input use." If this capacity is real and the measurement protocol is applied uniformly across treatment arms (i.e., the independent measurement team is blind to treatment status or follows a fixed protocol), then the outcome measure is not contaminated by treatment-induced reporting changes.

3. **Timing allows the treatment to reach relevant decisions.** The packet states that projects "may be assigned to different monitoring or participation conditions before implementation is complete." The crucial refinement is that assignment must occur before the *specific implementation decisions that determine leakage* — typically procurement and major construction phases — not merely before the project is administratively closed. If assignment arrives after procurement but before construction, the treatment can affect construction-phase leakage but not procurement-phase leakage, and this should be noted as a limitation.

If any of these conditions fails — e.g., assignment is not random, independent measurement is infeasible for most projects, or timing is too late — then the design does **not** support credible causal identification and the analysis should be presented as the strongest defensible descriptive or correlational study, with explicit acknowledgment of what confounders remain.

---

## 9. Proposed Empirical Design

### 9.1 Core Design: Multi-Arm Randomized Controlled Trial

**Randomization procedure:** Eligible projects are randomly assigned to T0 (control), T1 (formal oversight), or T2 (community monitoring) using stratified randomization. Stratification variables include project budget category (quartiles or size bins), project type (infrastructure category), and administrative region. Within each stratum, projects are assigned with equal probability (1/3 each), yielding roughly balanced arms.

**Sample size and power:** The minimum detectable effect depends on the number of projects (\(N\)), the variance of the leakage outcome, and the intra-cluster correlation if assignment is clustered. For a two-sided test at \(\alpha = 0.05\) with 80% power, the minimum detectable standardized effect size is approximately \(2.8 / \sqrt{N/3}\) per pairwise comparison (assuming equal allocation). If \(N = 300\) projects (100 per arm), the design can detect effects of roughly 0.28 standard deviations in pairwise comparisons. Power calculations should use pilot data on the variance of independently measured leakage; if pilot data are unavailable, the design should include an interim power analysis after baseline data collection.

**Announcement protocol:** After randomization, treatment status is communicated to the relevant implementing actors (project manager, local government, contractor, community representatives in T2). The control group receives no special announcement beyond standard program communications. The announcement itself must be standardized to avoid confounding treatment content with announcement salience.

### 9.2 Outcome Construction

**Independent post-completion measurement protocol:**
1. After project completion, a team of external engineers or technical enumerators visits each project site.
2. The team measures physical inputs (e.g., quantities of materials, dimensions of constructed facilities, observable quality indicators) using a standardized checklist developed before treatment assignment.
3. Quantities are valued at market prices from an independent price survey (not from project procurement records) to construct an "independently verified cost."
4. The team is blind to treatment status where possible. If blinding is infeasible (e.g., community monitors are visibly present), the protocol relies on standardization and objective measurement (e.g., measuring a road's width with a tape measure rather than rating it subjectively) to minimize measurement bias.

**Leakage calculation:**
For each project:
\[
\text{Leakage}_i = \frac{\text{IV Cost}_i - \text{Official Reported Cost}_i}{\text{Planned Budget}_i}
\]
where IV Cost is the independently verified cost. The analysis should examine both the signed leakage (to detect direction of manipulation) and absolute leakage \(|\text{Leakage}_i|\) (to measure total discrepancy).

### 9.3 Primary Analysis

**ITT estimation:**
\[
Y_i = \alpha + \beta_1 \cdot \text{Formal}_i + \beta_2 \cdot \text{Community}_i + \mathbf{X}_i'\gamma + \delta_{s(i)} + \varepsilon_i
\]
where \(\text{Formal}_i\) and \(\text{Community}_i\) are indicators for assignment to the respective arms, \(\mathbf{X}_i\) is a vector of baseline covariates (included to improve precision; not required for unbiasedness under randomization), and \(\delta_{s(i)}\) are stratification fixed effects. Standard errors are clustered at the level of treatment assignment (project or community level; higher-level clustering if assignment is grouped by administrative unit).

The coefficients \(\beta_1\) and \(\beta_2\) are the ITT estimates for formal oversight and community monitoring, respectively. The test of \(\beta_1 = \beta_2\) compares the two monitoring approaches.

**Complier analysis (if non-compliance is substantial):**
If assigned monitoring is not fully implemented (e.g., some assigned audits do not occur, some community meetings are not held), the design estimates LATE via instrumental variables:
\[
Y_i = \alpha + \lambda_1 \cdot \widehat{\text{ActualFormal}}_i + \lambda_2 \cdot \widehat{\text{ActualCommunity}}_i + \mathbf{X}_i'\gamma + \delta_{s(i)} + \varepsilon_i
\]
where actual monitoring receipt is instrumented by random assignment. The exclusion restriction requires that assignment affects outcomes only through actual monitoring receipt. This is plausible for formal oversight (the announcement of an audit should affect behavior only if the audit actually occurs or is credibly threatened) but more questionable for community monitoring, where the mere announcement of a participation mechanism could change official behavior even if community participation is low.

---

## 10. Why the Design Is Valid (or Why Causal Identification Is Not Credible)

Under random assignment:

1. **Balance:** Randomization ensures that, in expectation, treatment and control groups are balanced on all baseline characteristics — both observed and unobserved. The stratified design further improves balance on key dimensions. The ITT comparison of \(\bar{Y}_{T1}\) vs. \(\bar{Y}_{T0}\) and \(\bar{Y}_{T2}\) vs. \(\bar{Y}_{T0}\) yields unbiased estimates of the causal effect of *assignment to monitoring*.

2. **Independently measured outcomes break the reporting-manipulation link:** Because outcomes are constructed from external technical measurements rather than from implementing agencies' own records, the estimated effect reflects changes in *actual resource use and quality*, not merely changes in how these are reported. This is the key design feature that distinguishes this study from evaluations that rely solely on administrative data.

3. **Multi-arm design enables comparison of mechanisms:** The head-to-head comparison of formal oversight vs. community monitoring provides direct evidence on which approach is more effective, though the *reason* for any difference (deterrence vs. accountability) requires additional assumptions or process evidence.

If random assignment is not feasible, the validity of the design depends on the specific source of variation:

- **If assignment is based on an administrative rule** (e.g., projects above a budget threshold receive formal audits, or monitoring is phased in by region over time): a regression discontinuity or difference-in-differences design may yield credible causal estimates, but only for projects near the threshold or in the phase-in window.
- **If assignment is based on administrative discretion** with no clear exogenous source of variation: the design does **not** support credible causal identification. The analysis should be presented as a descriptive comparison with rich covariate adjustment, and all causal language should be removed.

---

## 11. Required Assumptions

### For ITT causal interpretation:

1. **Random assignment (SUTVA, part 1 — consistency):** Each project's potential outcomes depend only on its own treatment assignment, and the assigned treatment is delivered as intended (or at least, assignment is the causal variable of interest). This is secured by the randomization procedure.

2. **No interference between units (SUTVA, part 2):** A project's outcome does not depend on the treatment status of other projects. This assumption is *explicitly threatened* by the packet's spillover concern. The design addresses it through diagnostic tests (see Section 13) but cannot eliminate the concern by design alone without physical or administrative separation of treatment and control units — which may not be feasible in a connected administrative system.

3. **Excludability of the instrument (for LATE):** Random assignment affects outcomes only through actual monitoring receipt. This is plausible for formal oversight but requires careful defense for community monitoring.

4. **No differential attrition:** The availability of post-completion measurement is not affected by treatment assignment. If treated projects are more (or less) likely to be accessible for independent measurement, the ITT on the measured sample is biased.

5. **Independent measurement is not itself manipulable:** The external measurement team is not captured, bribed, or misled by the same officials whose behavior is being measured. This requires institutional separation between the measurement team and the implementing agency.

6. **Measurement captures the relevant dimensions of leakage:** The independent protocol covers the main channels through which resources can be diverted. If major corruption occurs in dimensions not measured (e.g., kickbacks in procurement that leave physical inputs unaffected), the leakage measure will understate true corruption — and the estimated treatment effect may reflect substitution into unmeasured dimensions rather than genuine reduction.

### For mechanism interpretation (comparing formal vs. community monitoring):

7. **The two treatments are comparable in intensity and timing:** If the formal oversight arm receives a more intensive or earlier intervention than the community arm, the comparison \(\beta_1\) vs. \(\beta_2\) conflates differences in mechanism with differences in dose.

8. **Mechanism-specific predictions are testable:** To claim that formal oversight works through deterrence while community monitoring works through accountability, the design needs auxiliary predictions that differ across arms — e.g., formal oversight should reduce leakage more in dimensions that are auditable, while community monitoring should reduce leakage more in dimensions that are visible to beneficiaries. Without such tests, the comparison of \(\beta_1\) and \(\beta_2\) identifies which arm is more effective but not *why*.

---

## 12. Statistical Model or Analysis Equation

### Primary specification: ITT with covariate adjustment

\[
Y_i = \alpha + \beta_1 \cdot T_{1i} + \beta_2 \cdot T_{2i} + \mathbf{X}_i'\gamma + \sum_{s} \delta_s \cdot \mathbb{1}\{\text{stratum}_i = s\} + \varepsilon_i
\]

where:
- \(Y_i\) is the independently measured leakage rate for project \(i\).
- \(T_{1i}\) is an indicator for assignment to formal oversight.
- \(T_{2i}\) is an indicator for assignment to community monitoring.
- \(\mathbf{X}_i\) includes baseline covariates: project budget (log or category indicators), project type fixed effects, baseline community characteristics, implementation start date (to control for any residual time trends), and contractor/committee characteristics if available.
- \(\delta_s\) are stratum fixed effects (the strata used in randomization).
- \(\varepsilon_i\) is the error term, clustered at the assignment level.

**Estimation:** OLS with heteroskedasticity-robust standard errors clustered at the level of treatment assignment (project or community). If assignment is clustered at a higher administrative level (e.g., district), cluster at that level.

**Hypothesis tests:**
- \(H_0: \beta_1 = 0\) — effect of formal oversight vs. control.
- \(H_0: \beta_2 = 0\) — effect of community monitoring vs. control.
- \(H_0: \beta_1 = \beta_2\) — equality of treatment effects across arms.
- Joint test: \(H_0: \beta_1 = \beta_2 = 0\) — any monitoring effect.

**Multiple testing adjustment:** If multiple outcome measures are tested (leakage rate, quality index, official-report divergence), adjust p-values using the Romano-Wolf stepdown procedure or report sharpened q-values to control the family-wise error rate or false discovery rate.

### IV specification (if non-compliance is substantial):

First stage:
\[
D_{1i} = \pi_{10} + \pi_{11} T_{1i} + \pi_{12} T_{2i} + \mathbf{X}_i'\gamma_1 + \delta_{1s(i)} + \nu_{1i}
\]
\[
D_{2i} = \pi_{20} + \pi_{21} T_{1i} + \pi_{22} T_{2i} + \mathbf{X}_i'\gamma_2 + \delta_{2s(i)} + \nu_{2i}
\]

Second stage:
\[
Y_i = \alpha + \lambda_1 \cdot \widehat{D}_{1i} + \lambda_2 \cdot \widehat{D}_{2i} + \mathbf{X}_i'\gamma + \delta_{s(i)} + \varepsilon_i
\]

where \(D_{1i}\) and \(D_{2i}\) are indicators for *actual* receipt of formal oversight and community monitoring, respectively. The coefficients \(\lambda_1\) and \(\lambda_2\) are LATE estimates among compliers. The first-stage F-statistic for each endogenous variable should exceed conventional thresholds (e.g., Stock-Yogo critical values) to avoid weak-instrument bias. Because there are two treatments, the first stage should report the Kleibergen-Paap Wald F-statistic and the Sanderson-Windmeijer F-statistic for each endogenous regressor.

---

## 13. Robustness, Placebo, Falsification Checks, or Diagnostic Tests

### 13.1 Balance checks
- Regress each baseline covariate on treatment indicators to verify that randomization produced balanced groups. Report omnibus F-test from a multinomial logit predicting treatment arm from all baseline covariates. If imbalance is detected on variables predictive of the outcome, include them as controls (the primary specification already does this).

### 13.2 Timing placebo
- If the independent measurement protocol allows, measure leakage on a dimension of the project that was *completed before treatment announcement*. This pre-treatment outcome should not differ across arms. A significant difference suggests either baseline imbalance or a failure of the measurement protocol.

### 13.3 Spillover tests
- For each control project, construct a "spillover exposure" measure: the number or proportion of treated projects in the same administrative unit, or within a specified geographic radius, or managed by the same contractor. Regress the control-group outcome on this exposure measure. A significant coefficient suggests spillover. If spillover is detected, the primary analysis can restrict the control group to "pure controls" (those with zero or minimal exposure) or model spillover explicitly.
- Alternatively, if the design includes variation in the *density* of treatment assignment across clusters (e.g., some districts have 80% treated projects, others have 20%), test whether control-group outcomes vary systematically with treatment density.

### 13.4 Substitution tests
- If multiple leakage dimensions are measured (e.g., materials leakage, labor-payment leakage, quality shortcuts), test whether treatment reduces leakage in some dimensions while increasing it in others. A negative correlation between treatment effects across dimensions, or a positive overall effect accompanied by positive point estimates on some dimensions, suggests substitution. Report a "total leakage index" that aggregates across all measured dimensions.
- If substitution into *unmeasured* dimensions is suspected, the design can include a "pure waste" or "impossible output" item in the independent protocol — something that could not possibly be affected by legitimate project decisions — as a sentinel indicator.

### 13.5 Attrition analysis
- Test whether the probability of successful post-completion measurement differs by treatment arm. If differential attrition is detected, construct bounds on the treatment effect using Lee (2009) bounds or similar approaches. Report both the complete-case analysis and the bounded estimates.

### 13.6 Reporting-manipulation test
- Regress the *official* leakage measure (based on administrative reports alone) on treatment indicators, and compare the coefficients to those from the independently measured outcome. If formal oversight reduces officially reported leakage more than independently measured leakage, this suggests that formal oversight primarily improves *reporting* rather than reducing actual diversion. If community monitoring shows the opposite pattern, that suggests distinct mechanisms.

### 13.7 Randomization inference
- As a complement to cluster-robust standard errors, conduct randomization inference (Fisher exact p-values) for the primary hypothesis tests by repeatedly reassigning treatment status according to the original randomization procedure and computing the test statistic in each permutation.

---

## 14. Heterogeneity Analysis (If Supportable)

Heterogeneity analysis is exploratory and should be pre-specified and clearly labeled as such. The design has limited power for subgroup analysis unless \(N\) is large. Suggested dimensions:

### 14.1 By project characteristics
- **Project size (budget):** Larger projects may offer greater opportunities for leakage and may attract more attention from formal auditors. Testing \(\beta_1\) and \(\beta_2\) by budget terciles can reveal whether monitoring is more effective for large or small projects.
- **Project type:** Infrastructure categories (e.g., roads vs. schools vs. water systems) differ in the observability of inputs and the complexity of procurement. Heterogeneity by project type can inform where each monitoring approach is most cost-effective.
- **Baseline corruption risk:** If a pre-treatment proxy for corruption risk is available (e.g., past audit findings in the same district, perception-based corruption indices), test whether monitoring is more effective in high-risk environments.

### 14.2 By community characteristics
- **Community collective action capacity:** If a baseline measure of community organization, literacy, or prior participation experience is available, test whether community monitoring effects are larger in communities with higher capacity for collective action. This speaks to Mechanism 2 (accountability via voice).
- **Information access:** If baseline information about project plans varies across communities, test whether community monitoring is more effective where beneficiaries start with less information.

### 14.3 By implementation fidelity
- Stratify the community monitoring arm by whether the planned community meetings actually occurred at high frequency. This is a non-experimental comparison (participation is endogenous), so results should be labeled as descriptive and potentially confounded. However, it can generate hypotheses about the minimum effective dose of community engagement.

### 14.4 Caution on multiple testing
All heterogeneity tests should be reported with and without multiple-testing adjustment. The design should pre-specify which heterogeneity dimension is the *primary* one (if any) and treat all others as exploratory.

---

## 15. Measurement, Compliance, Missingness, Spillover, or Implementation Limits

### Measurement
- **Incomplete coverage of leakage dimensions:** The independent measurement protocol can verify physical inputs (materials, dimensions) and observable quality but may not capture kickbacks in procurement (where the price is inflated but the delivered materials are genuine), ghost workers, or bribes for permits and approvals. The estimated leakage rate is a *lower bound* on total corruption, and the treatment effect on measured leakage may overstate or understate the effect on total corruption depending on substitution patterns.
- **Measurement error in independent verification:** Engineering measurements have their own error (sampling of locations to measure, accuracy of instruments, enumerator effects). Random measurement error in the dependent variable reduces precision but does not bias treatment effect estimates. Systematic error correlated with treatment (e.g., if enumerators are more diligent at treated sites) would bias estimates. Inter-rater reliability checks and standardized protocols mitigate this.

### Compliance
- **Imperfect implementation of formal oversight:** Some assigned audits may not occur due to administrative constraints. The ITT estimates the effect of *assignment*, which is policy-relevant but may understate the effect of *actual* monitoring. The IV analysis addresses this but requires the exclusion restriction.
- **Variable community participation:** Even under the same assigned treatment, some communities may hold many meetings and file many complaints while others do little. The ITT bundles the effect of the participation opportunity with the effect of actual participation. A complier analysis is possible but the exclusion restriction is harder to defend.

### Missingness
- **Inaccessible sites:** Some projects may be in areas that are inaccessible to the independent measurement team (security concerns, remote locations, seasonal road closures). If inaccessibility is correlated with treatment (e.g., community monitoring empowers communities to resist external measurement), attrition is differential and biases the ITT.
- **Delayed completion:** Projects not completed by the measurement window cannot be measured. If monitoring affects completion speed (e.g., audits slow down procurement), the measured sample is selected on completion status in a way that differs by treatment arm.

### Spillover
- **Contractor-level spillover:** If the same contractor works on multiple projects in the sample, and some of their projects are monitored, the contractor may adjust behavior on all projects. This violates SUTVA and biases the ITT toward zero. The design should track contractor identifiers and test for contractor-level clustering of treatment effects.
- **Information diffusion:** Community monitoring information may spread to neighboring communities not assigned to the treatment. If those communities then demand accountability, the control group is partially treated.

### Implementation limits
- **Blinding:** The independent measurement team cannot realistically be blinded to community monitoring (community members may discuss the intervention during the site visit). The protocol relies on objective measurements rather than subjective ratings.
- **Simultaneity of treatments:** If a project receives both formal oversight and community monitoring (by design or by accident), the design cannot separately identify their effects without a full factorial design. The packet mentions this possibility ("Possible if a project receives both formal oversight and community participation interventions") and the design should either explicitly include a combined arm or document and analyze cross-arm contamination.

---

## 16. Failure Modes and Alternative Explanations

| Failure mode | Description | How the design addresses it |
|---|---|---|
| **Selection into treatment** | Projects with different corruption propensity end up in different arms. | Randomization eliminates this in expectation. Balance checks verify it ex post. If randomization fails, causal claims are not defensible. |
| **Reporting manipulation** | Treatment changes what officials *report* without changing what they *do*. | Independently measured outcomes break this link. The reporting-manipulation test (Section 13.6) directly tests for this alternative explanation. |
| **Spillover attenuates effects** | Officials shift behavior in control projects after learning about treatment elsewhere. | Spillover tests (Section 13.3) detect this. If spillover is present, the ITT is a lower bound, and the pure-control subgroup provides a less contaminated estimate. |
| **Substitution masks total effect** | Reductions in measured leakage are offset by increases in unmeasured corruption. | Multi-dimensional outcome measures and sentinel indicators detect within-measurement substitution. Substitution into unmeasured dimensions cannot be detected by construction. |
| **Hawthorne effects** | The act of measurement itself (independent verification) changes behavior. | All arms receive the same measurement protocol, so Hawthorne effects difference out in the treatment-control comparison. However, the *level* of leakage in all arms may be lower than in the unmeasured population. |
| **Differential attrition** | Treated projects are more or less likely to complete on time or be accessible for measurement. | Attrition analysis and Lee bounds. If attrition is severe and differential, even bounded estimates may be uninformative. |
| **Anticipatory behavior** | If the randomization is predictable or announced early, officials may front-load or delay corruption. | The timing placebo test (Section 13.2) partially addresses this. If officials anticipate treatment and adjust pre-treatment behavior, baseline measures of pre-treatment leakage dimensions provide evidence. |
| **Treatment contamination** | Control-group projects accidentally receive monitoring, or treatment-arm projects do not receive it. | ITT analysis is robust to this (it estimates the effect of *assignment*, not receipt). The IV analysis addresses it but requires stronger assumptions. |
| **Enforcement of formal oversight is weak** | Audits occur but findings are ignored or sanctions are not applied. | The ITT estimate for formal oversight would be near zero, but this reflects a genuine null effect of *this* formal oversight regime rather than a failure of the design. Process data on audit findings and follow-up actions can distinguish "oversight without teeth" from "oversight that works." |
| **Community monitoring is captured by elites** | The participation mechanism is co-opted by local elites who use it to divert resources rather than to increase accountability. | Heterogeneity analysis by community inequality or elite capture proxies can detect this. If community monitoring *increases* leakage, this is a plausible (and policy-important) explanation. |

---

## 17. What Cannot Be Claimed

1. **The design cannot claim to measure total corruption.** Only leakage in dimensions covered by the independent measurement protocol is captured. Corruption in procurement pricing, ghost workers, permit bribery, or other channels outside physical-input verification is unmeasured. The estimated treatment effect should be described as the effect on *physically verifiable resource leakage*, not on "corruption" in general.

2. **The design cannot definitively attribute differences between formal and community monitoring to specific mechanisms.** While the design provides evidence on *which treatment works better*, attributing that difference to deterrence vs. accountability requires either additional experimental variation (e.g., varying audit probability or community information content independently) or strong auxiliary assumptions. The mechanism interpretation should be presented as suggestive and grounded in process evidence (meeting attendance, complaint patterns, audit findings) rather than as conclusively proven.

3. **The design cannot estimate general equilibrium effects.** If monitoring at scale changes the broader equilibrium of corruption (e.g., by shifting norms among contractors or officials, or by changing the supply of corruptible projects), the partial-equilibrium estimates from this study do not capture those effects. This is a standard limitation of randomized evaluations and should be acknowledged.

4. **The design cannot claim external validity beyond the specific program and context.** The packet withholds country, program, and project type. The estimated effects are conditional on the specific monitoring protocols, institutional environment, and project types in the study. Extrapolation to other settings requires additional assumptions about institutional similarity.

5. **The design cannot estimate the effect of community monitoring independent of the researcher's presence.** If the community monitoring intervention is implemented by researchers or requires researcher facilitation, the estimated effect may not generalize to a government-run community monitoring program without researcher support.

6. **If random assignment is not feasible, the design cannot make causal claims at all.** In that case, all findings should be presented as descriptive associations conditional on observables, with explicit acknowledgment of unobserved confounders.

---

## 18. Additional Data Needed

The following data, while not strictly required for the core analysis, would substantially strengthen the design:

1. **Pre-treatment audit or leakage measures:** If past projects in the same communities or by the same contractors have audit findings or known leakage rates, these provide a baseline measure of corruption propensity that improves precision and enables heterogeneity analysis by baseline risk.

2. **Contractor and official identifiers:** Tracking which contractors and which government officials are involved in each project enables spillover tests at the contractor/official level and allows estimation of whether monitoring effects operate through specific actors.

3. **Detailed procurement data:** Unit prices, bidder information, and procurement process data would allow the independent measurement protocol to detect procurement-phase corruption (e.g., inflated prices) that physical input verification alone cannot capture.

4. **Community baseline survey:** Measures of social capital, collective action history, inequality, literacy, and prior experience with public projects would enable heterogeneity analysis for community monitoring mechanisms and help diagnose elite capture.

5. **Audit enforcement data:** Information on whether formal audit findings lead to sanctions, recoveries, or prosecutions would distinguish "oversight without consequences" from "oversight with teeth," clarifying the mechanism for formal oversight.

6. **Implementation timeline detail:** Precise dates of procurement award, construction start, major milestones, and completion for each project would enable the timing placebo test and ensure that treatment is assigned before the decisions it is meant to affect.

7. **Geographic coordinates:** Project GPS locations enable precise spillover analysis based on spatial proximity rather than administrative boundaries.

8. **Cost data for the interventions themselves:** To conduct a cost-effectiveness comparison between formal oversight and community monitoring, the design needs data on the cost per project of implementing each intervention.

---

## 19. Threat-Response Table

| Threat | Why It Matters | Proposed Diagnostic or Design Response | Remaining Limitation |
|---|---|---|---|
| **Selection: projects receiving monitoring may differ from unmonitored projects** | If assignment is related to project risk, political attention, or administrative capacity, the treatment-control difference conflates monitoring effects with baseline differences in corruption propensity. | Random assignment with stratification on project type, budget, and region. Balance checks on all baseline covariates. Randomization inference for primary tests. | If randomization is not feasible (packet says "researcher- or government-controlled assignment" — consistent with randomization but not guaranteed), the design cannot support causal claims. Even with randomization, finite-sample imbalance on unobserved predictors of leakage is possible, though unlikely with adequate N and stratification. |
| **Measurement: official records may be manipulable, incomplete, or strategically reported** | If outcomes rely on administrative data that the treatment itself affects through reporting behavior rather than real behavior, the estimated effect is on *what is reported*, not on *what happened*. | Primary outcomes are constructed from independently collected post-completion evidence (physical input verification, quality assessment) by an external team using a standardized protocol. The reporting-manipulation diagnostic test compares treatment effects on independently measured vs. officially reported leakage. | Independent measurement covers only physically verifiable dimensions. Corruption in procurement pricing, ghost workers, or bribery is not captured. The independent measurement team may itself be subject to error or manipulation, though standardization and blinding mitigate this. |
| **Compliance/take-up: assigned monitoring may not be implemented as planned** | If audits do not occur or community meetings are not held, the ITT estimates the effect of *assignment* rather than *actual monitoring receipt*, potentially understating the effect of monitoring when it actually happens. | ITT is the primary estimand (policy-relevant: it estimates the effect of *offering* monitoring). IV analysis estimates LATE among compliers if non-compliance is substantial. Process data on audit occurrence, meeting frequency, and complaint volume describe the compliance profile. | IV requires the exclusion restriction (assignment affects outcomes only through actual monitoring receipt), which is harder to defend for community monitoring (announcement itself could change behavior). The LATE applies only to compliers and may not generalize to the full sample. |
| **Timing: monitoring may be assigned after implementation choices are already made** | If treatment is assigned after procurement or early construction decisions, it cannot affect leakage during those phases, and the estimated effect reflects only post-announcement adjustments — underestimating the potential effect of timely monitoring. | The design requires assignment before major implementation decisions. The timing placebo test checks whether pre-treatment leakage dimensions differ across arms. Implementation timeline data enable stratification by project phase at assignment. | If assignment timing varies across projects and some receive treatment late, the estimated ITT is a weighted average of effects for early- and late-treated projects, and the weights may not reflect policy interest. The design can report treatment effects by project phase at assignment, but this is an observational stratification. |
| **Spillover/interference: officials, contractors, or community members may change behavior in unmonitored projects after learning about monitoring elsewhere** | Spillover violates SUTVA and biases the ITT toward zero (if spillover reduces leakage in control projects) or away from zero (if spillover increases leakage in control projects as officials compensate for losses in treated projects). | Spillover exposure measures (proportion of treated projects in same administrative unit or radius, common contractor indicators). Test whether control-group outcomes vary with spillover exposure. If spillover is detected, restrict analysis to pure controls or model spillover explicitly. Contractor-level clustering analysis. | Spillover tests have limited power (they rely on variation within the control group). If spillover is pervasive, no unit is truly untreated, and the ITT estimates the effect of *relative* treatment intensity rather than treatment vs. no treatment. Geographic or administrative isolation of treatment and control units would be needed to eliminate spillover by design, but this may conflict with representativeness. |
| **Substitution: reductions in measured leakage may be offset by unmeasured forms of corruption** | If officials substitute into corruption channels not covered by the measurement protocol, the estimated treatment effect overstates the reduction in total corruption. | Multi-dimensional outcome measures (materials, labor, quality). Tests for negative correlations between treatment effects across dimensions. Sentinel indicators for implausible patterns. Report a total leakage index aggregating across all measured dimensions. | Substitution into unmeasured dimensions is fundamentally undetectable with the available data. The estimated treatment effect should be interpreted as the effect on *measured leakage*, and the possibility of substitution into unmeasured corruption should be explicitly acknowledged as a limitation. Additional data on procurement prices, ghost workers, or other corruption channels would narrow this gap. |
| **Differential attrition: treated projects may have different rates of successful measurement** | If monitoring affects project completion speed, site accessibility, or willingness to cooperate with measurement, the measured sample is endogenously selected and the ITT on completers is biased. | Test whether measurement success differs by treatment arm. Lee (2009) bounds for the treatment effect under different assumptions about the distribution of missing outcomes. Report both complete-case and bounded estimates. | Lee bounds can be wide and uninformative if attrition is substantial. If attrition is non-monotonic with respect to treatment (which Lee bounds require), alternative approaches (e.g., parametric selection models) require stronger assumptions. |

---

## 20. Claim-Evidence Table

| Claim | Evidence Used | Claim Type | Confidence | What Would Falsify This Claim |
|---|---|---|---|---|
| **C1:** Assignment to formal oversight reduces independently measured resource leakage relative to control. | ITT estimate \(\hat{\beta}_1\) from the primary specification, comparing T1 to T0 on independently measured leakage. | Causal (under random assignment and no spillover). | High if randomization is successfully implemented and no major violations detected. Moderate if spillover is present. | (a) \(\hat{\beta}_1 \approx 0\) with tight confidence intervals, or (b) a significant pre-treatment difference in leakage between T1 and T0 on the timing placebo test, or (c) evidence of differential attrition that cannot be bounded away from zero. |
| **C2:** Assignment to community monitoring reduces independently measured resource leakage relative to control. | ITT estimate \(\hat{\beta}_2\) from the primary specification, comparing T2 to T0. | Causal (under random assignment and no spillover). | High under same conditions as C1. | Same falsification conditions as C1, applied to \(\hat{\beta}_2\). |
| **C3:** Formal oversight and community monitoring differ in effectiveness. | Test of \(H_0: \beta_1 = \beta_2\) from the primary specification. | Causal (under random assignment and comparable treatment intensity/timing). | Moderate: even if the difference is precisely estimated, attributing it to mechanisms rather than differences in implementation intensity requires auxiliary evidence. | Failure to reject \(H_0: \beta_1 = \beta_2\) with adequate power. Power analysis should determine whether the design can detect policy-meaningful differences. |
| **C4:** Formal oversight reduces leakage primarily by deterring diversion (not merely by improving reporting). | Comparison of treatment effects on independently measured leakage vs. officially reported leakage. If \(\hat{\beta}_1\) is similar or larger for the independent measure than for the official measure, this supports the deterrence interpretation. If \(\hat{\beta}_1\) is significant for the official measure but not the independent measure, this supports the reporting-manipulation interpretation. | Mechanism (suggestive, not definitive). | Low to moderate: this test distinguishes reporting effects from real effects but does not directly test deterrence vs. other real-effect channels (e.g., fear of community complaints triggered by audit announcements). | A significant \(\hat{\beta}_1\) on officially reported leakage accompanied by a near-zero \(\hat{\beta}_1\) on independently measured leakage would suggest that formal oversight primarily changes reporting, not behavior. |
| **C5:** Community monitoring reduces leakage through increased beneficiary information and voice. | Heterogeneity analysis: larger effects in communities with higher baseline collective action capacity, higher meeting attendance, or more complaints filed. Process evidence linking complaints to official responses. | Mechanism (suggestive, not definitive). | Low: heterogeneity by collective action capacity is an observational comparison (capacity is not randomly assigned). Process evidence is descriptive. | Null heterogeneity by collective action capacity, or community monitoring effects that are driven entirely by communities where no meetings actually occurred (suggesting the announcement, not participation, is the active ingredient). |
| **C6:** Officials substitute corruption from measured to unmeasured dimensions when monitoring is introduced. | Negative within-project correlation between treatment effects on different leakage dimensions (e.g., materials leakage falls but quality shortcuts increase). Sentinel indicators flag implausible patterns. | Descriptive/diagnostic. | Low: substitution into measured dimensions can be detected, but substitution into unmeasured dimensions cannot. Absence of evidence of substitution within measured dimensions does not imply absence of substitution overall. | Positive treatment effects on one leakage dimension combined with negative effects on another would be *consistent* with substitution but does not prove it. Direct evidence of substitution would require measuring all relevant corruption channels — which the design cannot do by construction. |
| **C7:** Spillover from treated to control projects attenuates the estimated treatment effects. | Significant coefficient on spillover exposure in the control-group regression, or systematic variation in control-group outcomes across clusters with different treatment densities. | Diagnostic (descriptive). | Low to moderate: spillover tests have limited power and require sufficient variation in exposure within the control group. | Failure to detect spillover does not prove its absence (the test may lack power). Detection of spillover confirms its presence but the magnitude is estimated with uncertainty. |
| **C8:** The estimated treatment effects are not driven by differential attrition. | Non-significant difference in measurement success rates across treatment arms. Lee bounds that exclude zero for the estimated treatment effects. | Diagnostic. | Moderate: if attrition is low and balanced, this claim is well-supported. If attrition is high or differential, Lee bounds may be wide and the claim is less certain. | Significant difference in measurement success rates across arms, or Lee bounds that include zero. |
| **C9:** Pre-existing differences between treatment arms do not explain the results. | Balance checks on baseline covariates show no significant differences. Omnibus F-test from multinomial logit of treatment arm on baseline covariates is non-significant. | Diagnostic. | High under successful randomization with adequate N. | Significant imbalance on covariates predictive of the outcome. This can be partially addressed by covariate adjustment but raises concerns about unobserved imbalance. |
| **C10:** The estimated effects apply to the study population and program but may not generalize to other contexts. | The design is internally valid (if randomized) but externally valid only to the extent that the study context is representative. The packet withholds country and program details, so external validity cannot be assessed from the available information. | Descriptive/interpretive. | Not applicable: this is a limitation, not a testable claim. | Not testable within this study design. Replication in other contexts would be needed to assess external validity. |

---

## Summary Assessment

This design can produce credible causal estimates of the effect of monitoring interventions on physically verifiable resource leakage in local public projects, provided that (a) random assignment is feasible and implemented before major implementation decisions, and (b) independent post-completion measurement of sufficient scope and quality can be conducted. The design's key strength is its separation of outcome measurement from the administrative reporting system that is itself potentially corrupted — a feature that directly addresses the most fundamental challenge in corruption research. Its key limitation is that it cannot measure total corruption (only physically verifiable dimensions) and therefore cannot rule out substitution into unmeasured corruption channels. The comparison between formal oversight and community monitoring can identify which approach is more effective but requires additional evidence to attribute differences to specific causal mechanisms.

## Tool Log Summary

- actual tool use: none
- trajectory `toolMetas`: []
- toolCall count: 0
- toolResult count: 0
- session_id: isolated_20260527_233158_98725_22
- session_log: /Users/jiangcanxiang/.openclaw/agents/benchmark_isolated/sessions/isolated_20260527_233158_98725_22.jsonl
- trajectory_log: /Users/jiangcanxiang/.openclaw/agents/benchmark_isolated/sessions/isolated_20260527_233158_98725_22.trajectory.jsonl

## Operator Notes

- duration_ms: 314838
- stderr_excerpt: [plugins] plugins.allow is empty; discovered non-bundled plugins may auto-load: qqbot (/Users/jiangcanxiang/.openclaw/npm/node_modules/@openclaw/qqbot/dist/index.js), openclaw-weixin (/Users/jiangcanxiang/.openclaw/npm/node_modules/@tencent-weixin/openclaw-weixin/dist/index.js). Set plugins.allow to explicit trusted ids. [skills] Skipping escaped skill path outside its configured root: source=openclaw-managed root=~/.openclaw/skills reason=symlink-escape requested=~/.openclaw/skills/0-autoresearch-skill resolved=~/.orchestra/skills/0-autoresearch-skill [skills] Skipping escaped skill path outside its configured root: source=openclaw-managed root=~/.openclaw/skills reason=symlink-escape requested=~/.openclaw/skills/brainstorming-research-ideas resolved=~/.orchestra/skills/21-research-ideation/brainstorming-research-ideas [skills] Skipping escaped skill path outside its configured root: source=openclaw-managed root=~/.openclaw/skills reason=symlink-escape requested=~/.openclaw/skills/creative-thinking-for-research resolved=~/.orchestra/skills/21-research-ideation/creative-thinking-for-research [skills] Skipping escaped skill path outside its configured root: source=openclaw-managed r
