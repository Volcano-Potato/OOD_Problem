# Raw Agent Run Log

- `run_id`: RUN_20260529_114115_07_openclaw_deepseekv4pro_isolated
- `case_id`: C014
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
- `timestamp`: 2026-05-29T11:41:15+0800
- `input_file`: benchmark/cases/C014_corruption_monitoring/agent_task_level1.md
- `system_prompt_summary`: workspace=/Users/jiangcanxiang/OpenClawBenchmarkIsolated; thinking=high; actual_tool_use=none; agent=benchmark_isolated
- `contamination_status`: unknown
- `contamination_reason`: pending manual content review; actual tool use=none
- `status`: success

## Raw Agent Output

# Research Design: Monitoring Interventions and Corruption in Local Public Projects

---

## 1. Executive Summary

This design proposes a field experiment to estimate the effect of monitoring interventions on resource leakage in local public projects and to compare formal oversight mechanisms with community-based monitoring. The central challenge is that corruption is inherently concealed and official records may themselves be compromised. The design addresses this through (a) random assignment of projects to monitoring arms, creating credible causal variation, and (b) an independently implemented outcome measurement protocol that triangulates physical audits, community price benchmarks, and user surveys, rather than relying on administrative reports. The design identifies average treatment effects on directly measured leakage (the gap between allocated funds and the independently assessed value of delivered outputs), while acknowledging that certain forms of corruption—collusion, favoritism without measurable cost inflation, and substitution into unmeasured margins—will remain partially or fully unobserved.

---

## 2. Research Question

Do monitoring interventions reduce corruption or resource leakage in local public projects, and do formal oversight and community-based monitoring differ in their effectiveness, mechanisms, or patterns of substitution?

---

## 3. Target Estimand (or Strongest Defensible Estimand)

**Primary estimand:** The average treatment effect (ATE) of each monitoring intervention on *independently measured resource leakage*, defined as:

> Leakage = (Funds Allocated) − (Independently Assessed Value of Delivered Outputs)

where "independently assessed value" is constructed from physical measurements of inputs and outputs, benchmarked against local market prices at the time of implementation, collected by enumerators not involved in project administration.

**Secondary estimands:**
- The differential effect of formal oversight vs. community-based monitoring: ATE_formal − ATE_community.
- The effect of each monitoring type on the *discrepancy* between official expenditure records and independently assessed value (i.e., whether monitoring changes reporting behavior independently of actual leakage).

**Why this is the strongest defensible estimand:** Random assignment of monitoring generates an unbiased estimate of the ITT (intention-to-treat) effect on leakage measured through an independent protocol. The independent measurement avoids the contamination that arises when the outcome data source (official records) is itself a strategic choice of the agents being monitored.

---

## 4. Treatment or Exposure and Main Outcomes

### Treatment Arms (randomly assigned at the project level)

| Arm | Label | Description |
|-----|-------|-------------|
| T0 | Control | Business-as-usual monitoring (whatever the existing system provides) |
| T1 | Formal Oversight | Projects receive announced, probabilistically scheduled formal audits by independent (non-local) auditors, with results shared upward to funding authorities |
| T2 | Community-Based Monitoring | Projects receive a facilitated community monitoring protocol (e.g., public dissemination of project budgets and timelines, community scorecard meetings at project milestones, a structured grievance mechanism) |
| T3 | Combined | Both formal oversight and community-based monitoring are deployed simultaneously |

### Main Outcomes (independently measured)

1. **Primary outcome — Resource Leakage Index:** The percentage gap between allocated project funds and the independently assessed market value of observed inputs and outputs. Constructed from:
   - Physical measurements of quantities (materials, labor days, dimensions of constructed assets)
   - Unit price benchmarks collected from local markets contemporaneously
   - Independent engineering assessment of whether specifications were met

2. **Secondary outcome — Official-Independent Discrepancy:** The difference between officially reported expenditures and the independently assessed value, signed so that positive values indicate official over-reporting.

3. **Secondary outcome — Project Quality Score:** A composite of independently rated quality dimensions (structural integrity, materials grade, adherence to specifications, user-reported functionality).

4. **Process indicators (interpreted cautiously, not as corruption measures):**
   - Number and attendance at community monitoring meetings
   - Grievances filed and resolved
   - Audit findings count
   - Procurement process deviations flagged

---

## 5. Data Structure Summary

The dataset would have the following structure:

- **Unit of observation:** Project × Time (panel) or Project (cross-section at completion)
- **Level of randomization:** Project
- **Key variables:**
  - Treatment assignment indicators for each arm
  - Project-level covariates (sector, budget size, location, implementing agency type, baseline characteristics of the beneficiary community)
  - Independent outcome measurements (physical audit data, price benchmarks, quality scores, user surveys)
  - Administrative records (official expenditures, reported progress, audit reports if any)
  - Process and compliance data (meeting attendance, audit completion, grievance logs)
- **Timing:** Baseline covariates collected at project approval/start; treatment assigned before implementation; outcomes measured at project completion and potentially at an intermediate milestone

---

## 6. Relevant Causal Mechanisms

The design is structured around four mechanisms, each of which generates testable implications:

| Mechanism | Channel | Observable Implication |
|-----------|---------|------------------------|
| **Deterrence** | Formal oversight raises the expected cost of diversion (probability of detection × penalty) | Leakage should fall most in T1 and T3; the effect should be concentrated in easily auditable line items |
| **Participation/Scrutiny** | Community monitoring improves local information, social accountability, and ability to challenge misuse | Leakage should fall in T2 and T3, especially for locally visible aspects of projects; user satisfaction and grievance resolution should improve |
| **Measurement/Reporting** | Monitoring changes what gets *reported* in official records, not necessarily what happens on the ground | The official-independent discrepancy should respond to treatment; T1 may reduce the discrepancy (auditors catch misreporting); T2 may increase reporting accuracy through transparency |
| **Substitution** | Reducing leakage in one observable margin shifts it to another, less observable margin | The composition of measured leakage may change across line items; T3 (combined) may show less substitution than T1 or T2 alone |

These mechanisms are not mutually exclusive, and the design can provide suggestive evidence on their relative importance without being able to isolate each one cleanly.

---

## 7. Main Identification Challenge

The fundamental identification challenge is **simultaneous unobservability of the counterfactual, the outcome, and the strategic response.** Specifically:

1. **Outcome measurement:** Corruption is concealed. If the researcher relies on official records, the measurement instrument is contaminated by the very behavior being studied. Officials can under-report leakage in monitored projects without reducing actual leakage.

2. **Strategic substitution:** Even with independent measurement, agents may shift leakage into margins the measurement protocol does not capture (e.g., from materials quantity to materials quality, from inputs to procurement kickbacks, from construction to maintenance contracts).

3. **Non-compliance and endogenous implementation:** Monitoring interventions may not be implemented as designed. Auditors may be captured; community meetings may be captured by local elites. Treatment take-up is endogenous.

4. **Spillover:** If monitoring resources are fixed at a higher administrative level, monitoring some projects may reduce monitoring of others. If deterrence signals generalize, control projects may also change behavior.

5. **Selection into projects:** Projects that receive monitoring may differ from those that do not in unobserved ways, which is why random assignment is essential.

---

## 8. Whether Credible Causal Identification Is Possible

**Yes, credible causal identification of the intention-to-treat (ITT) effect of monitoring assignment on independently measured leakage is possible**, provided:

- Random assignment of projects to monitoring arms is successfully implemented and maintained.
- An independent outcome measurement protocol is designed and deployed before treatment assignment is known to enumerators.
- The measurement protocol captures a sufficiently broad set of leakage margins that substitution cannot fully escape detection.
- Attrition and non-compliance are measured and addressed analytically.

**Causal identification is not credible** for:
- Forms of corruption entirely outside the measurement protocol (e.g., collusion in procurement before project approval; nepotism in hiring that does not affect measured costs; political favoritism in project selection).
- The precise *mechanism* through which monitoring reduces leakage (deterrence vs. participation vs. reporting effects) — these can be suggested by patterns but not cleanly separated without additional experimental variation.
- General equilibrium or market-level effects of scaling up monitoring.

---

## 9. Proposed Empirical Design

### Design Type: Multi-Arm Cluster-Randomized Controlled Trial

**Step 1: Sampling and Randomization**
- Define the sampling frame of eligible projects (e.g., all projects approved in a given period, above a minimum budget threshold, in regions accessible for independent measurement).
- Conduct a baseline data collection: project characteristics, community characteristics, implementing agency details.
- Stratify by project sector, budget size tercile, and geographic region.
- Randomly assign projects within strata to T0, T1, T2, T3 with equal probability. The randomization is at the project level. If implementing agencies manage multiple projects, cluster randomization at the agency level should be considered to avoid within-agency spillover.

**Step 2: Treatment Implementation**
- T0: No additional intervention beyond existing procedures.
- T1: Announce to project implementers that the project will be subject to formal audit with probability p at a pre-announced milestone. Deploy trained, independent auditors. Share audit findings with funding authorities.
- T2: Facilitate community monitoring at key project milestones. This includes: (a) public posting of project budget and timeline in accessible locations and formats; (b) facilitated community meetings to review progress against plans; (c) a structured mechanism for filing and tracking complaints.
- T3: Both T1 and T2 protocols simultaneously.

**Step 3: Independent Outcome Measurement**
- Deploy independent enumerator teams at project completion (and ideally at one intermediate milestone).
- Enumerators are blinded to treatment assignment where feasible. (Blinding is imperfect since community monitoring activities are visible, but physical measurements can be taken without knowledge of treatment status.)
- Measurement protocol:
  - Physical audit: Measure quantities of all major inputs (materials, labor days, equipment hours) and dimensions/quality of outputs using standardized instruments and protocols.
  - Price benchmarking: Collect contemporaneous market prices for major inputs from independent market surveys in the project area.
  - Quality assessment: Independent engineering assessment using standardized checklists.
  - User survey: Structured interviews with a random sample of intended beneficiaries about perceived quality, functionality, and whether they observed or heard about misuse.
- Construct the leakage index as described in Section 4.

**Step 4: Analysis**
- Estimate ITT effects using the specification in Section 12.
- Conduct heterogeneity analysis as described in Section 14.
- Triangulate across measurement methods to assess sensitivity.

---

## 10. Why the Design Is Valid (or Why Causal Identification Is Not Credible)

**Validity of the ITT estimate:**

- **Internal validity:** Random assignment ensures that, in expectation, treatment and control projects differ only in monitoring assignment. Any post-randomization difference in independently measured leakage can be attributed to the causal effect of assignment to monitoring.
- **Measurement validity:** The independent measurement protocol breaks the link between the strategic actor (project implementer) and the outcome data (official records). Physical quantities and market prices are harder to manipulate than administrative ledgers.
- **Construct validity:** The leakage index directly operationalizes the gap between resources provided and value delivered, which is the conceptual definition of resource leakage.

**Limits to validity:**

- The independent measurement can be imperfect (measurement error in physical quantities, unrepresentative price benchmarks). Random measurement error attenuates estimates toward zero; systematic measurement error correlated with treatment (e.g., if monitoring makes implementers more careful about the specific margins being measured) could bias estimates.
- Substitution into unmeasured margins remains a threat to the interpretation of the estimate as the *total* effect on corruption, rather than the effect on *measured* corruption.
- The design estimates the effect of *assignment to* monitoring, not the effect of monitoring itself (the TOT) without additional assumptions about compliance.

---

## 11. Required Assumptions

| Assumption | Justification / Assessment |
|------------|---------------------------|
| **A1. Random assignment is successfully implemented** | Requires verification through balance tests on baseline covariates. Pre-registration of randomization protocol. |
| **A2. Stable Unit Treatment Value Assumption (SUTVA)** | Projects' outcomes depend only on their own treatment assignment. Threats: spillover through shared implementing agencies, contractors, or information diffusion. Testable through spatial/proximity analysis. |
| **A3. Independent measurement is not systematically biased by treatment status** | Enumerator blinding and standardized protocols reduce this risk. Testable through comparison of measurement characteristics (variance, item non-response) across arms. |
| **A4. No differential attrition** | Projects must not drop out of the study at rates that differ by treatment arm. Testable and addressable through bounding exercises (Lee bounds). |
| **A5. Price benchmarks are representative** | Market price surveys must capture the prices actually faced by projects. Stratified price collection by geography and time reduces bias. |
| **A6. The measured leakage index captures a meaningful share of total leakage** | Cannot be fully verified; triangulation across measurement methods provides partial assessment. |
| **A7. Compliance with treatment is non-zero** | If no projects comply with monitoring protocols, the ITT is zero by construction. Process monitoring verifies compliance. |

---

## 12. Statistical Model or Analysis Equation

### Primary specification (ITT)

```
Leakage_i = α + β₁·T1_i + β₂·T2_i + β₃·T3_i + δ_s + ε_i
```

Where:
- `Leakage_i` = independently measured resource leakage index for project i
- `T1_i, T2_i, T3_i` = indicators for assignment to formal oversight, community monitoring, and combined arms (T0 is the omitted reference category)
- `δ_s` = stratification fixed effects (strata dummies)
- `ε_i` = error term, clustered at the level of randomization (project or implementing agency)

**Coefficients of interest:**
- β̂₁: ITT effect of formal oversight relative to control
- β̂₂: ITT effect of community monitoring relative to control
- β̂₃: ITT effect of combined monitoring relative to control
- H₀: β₁ = β₂ (test of differential effectiveness of formal vs. community monitoring)
- H₀: β₃ = β₁ + β₂ (test of additive vs. super-additive/sub-additive effects of combining interventions)

### Covariate-adjusted specification (for precision)

```
Leakage_i = α + β₁·T1_i + β₂·T2_i + β₃·T3_i + γ·X_i + δ_s + ε_i
```

Where `X_i` includes pre-specified baseline covariates (project budget, sector, implementing agency characteristics, community characteristics). The adjusted specification should be pre-registered; the unadjusted specification remains the primary analysis.

### Analysis of official-independent discrepancy

```
Discrepancy_i = α + β₁·T1_i + β₂·T2_i + β₃·T3_i + δ_s + ε_i
```

Where `Discrepancy_i = OfficialReportedExpenditure_i − IndependentAssessedValue_i`. A negative β̂₁ would suggest formal oversight reduces over-reporting. A negative β̂₂ would suggest community monitoring improves reporting accuracy. The sign and magnitude of these coefficients, compared to those in the primary leakage equation, can suggest whether monitoring operates through deterrence (leakage falls, discrepancy falls) or primarily through reporting changes (discrepancy falls but leakage unchanged).

### Instrumental variables / TOT estimation (secondary)

If compliance data are available, use treatment assignment as an instrument for actual monitoring exposure:

```
Leakage_i = α + β·ActualMonitoring_i + γ·X_i + ε_i
ActualMonitoring_i = π₀ + π₁·T1_i + π₂·T2_i + π₃·T3_i + ν_i
```

where `ActualMonitoring_i` could be a binary indicator (project actually audited or community meeting actually held) or a continuous measure of monitoring intensity. This recovers the local average treatment effect (LATE) on compliers.

### Multiple testing adjustment

With multiple outcomes and treatment arms, control the family-wise error rate or false discovery rate. Pre-specify the primary outcome and primary comparison. Index outcomes into standardized summary indices following Anderson (2008).

---

## 13. Robustness, Placebo, Falsification Checks, and Diagnostic Tests

### Balance tests
- Regress each baseline covariate on treatment indicators. Joint F-test for orthogonality. Report any imbalances and assess sensitivity by including imbalanced covariates.

### Placebo outcome tests
- Test whether treatment predicts *baseline* or *pre-treatment* characteristics that should not be affected by treatment (e.g., project characteristics determined before randomization). A significant "effect" on pre-determined variables would suggest a failure of randomization rather than a genuine treatment effect.

### Alternative leakage constructions
- Vary the price benchmarks used (median vs. mean market prices; nearest-market vs. regional-average prices).
- Vary the weighting of physical input categories in the leakage index.
- Use only the subset of inputs that are most objectively measurable (e.g., exclude quality ratings and use only physical quantities).
- Report whether results are sensitive to these alternatives.

### Attrition analysis
- Test whether project completion rates (or measurement response rates) differ by treatment arm.
- If attrition is differential, compute Lee (2009) bounds on treatment effects.

### Spillover tests
- For each control project, compute the distance to the nearest treated project or the number of treated projects in the same administrative unit. Test whether control-project leakage correlates with proximity to treated projects.

### Donut-hole / buffer zone analysis
- If geographic spillover is suspected, re-estimate primary effects excluding control projects within a specified radius of treated projects.

### Stratification sensitivity
- Re-estimate primary effects without stratification fixed effects. Results should be similar but less precise.

### Randomization inference
- Compute exact p-values using Fisher randomization inference (permuting treatment assignment within strata) to avoid reliance on asymptotic approximations.

### Measurement validation
- Compare independent measurements against a subset of projects with unusually reliable administrative data (if available) or against a "gold standard" intensive engineering audit on a subsample.
- Assess inter-enumerator reliability for physical measurements.

---

## 14. Heterogeneity Analysis (If Supportable)

The following heterogeneity analyses should be pre-specified and interpreted as exploratory (they are not powered for formal testing unless the sample is large):

### By project characteristics
- **Budget size:** Does monitoring matter more for larger projects (more resources to divert) or smaller projects (less existing scrutiny)?
- **Sector:** Infrastructure vs. service-delivery projects may have different leakage profiles and measurability.
- **Complexity:** Projects with more line items or more complex procurement may offer more opportunities for leakage and more margins for substitution.

### By implementing agency characteristics
- **Agency capacity:** Does monitoring substitute for or complement existing administrative capacity?
- **Prior audit history:** Do agencies with a history of adverse audit findings respond differently?

### By community characteristics
- **Baseline social capital / collective action capacity:** Community monitoring may be more effective where communities have stronger pre-existing organization.
- **Information environment:** Distance to administrative centers, media access, literacy rates.

### By treatment intensity
- Within T1: Does the effect vary with the number of audit visits actually conducted? (Endogenous; interpret cautiously.)
- Within T2: Does the effect vary with meeting attendance rates? (Endogenous.)

### Interaction between mechanisms
- The T3 arm allows testing whether formal and community monitoring are substitutes or complements. A negative interaction (β₃ < β₁ + β₂) would suggest diminishing returns or redundancy; a positive interaction (β₃ > β₁ + β₂) would suggest complementarity.

---

## 15. Measurement, Compliance, Missingness, Spillover, and Implementation Limits

### Measurement limits
- **Physical measurement error:** Quantities may be mismeasured, especially for underground or internal components of construction projects. Random error attenuates treatment effects. Systematic error (e.g., if implementers strategically conceal diversion in ways that physical audits miss) could bias estimates in unknown directions.
- **Price benchmark representativeness:** Market prices may differ from actual procurement prices due to bulk discounts, transportation costs, quality differences, or kickbacks embedded in unit prices. The leakage index may misattribute procurement inefficiency to corruption, or miss corruption that occurs through inflated unit prices rather than quantity shortfalls.
- **Quality assessment subjectivity:** Quality ratings require judgment, which introduces enumerator-level variation. Standardized rubrics, enumerator training, and inter-rater reliability checks mitigate but do not eliminate this.
- **User survey reliability:** Beneficiaries may not know about hidden corruption, may fear reporting, or may be subject to elite capture of the survey process.

### Compliance limits
- **Audit non-compliance:** Auditors may not show up, may be captured, or may conduct superficial audits. Record audit completion, duration, and findings as process measures.
- **Community monitoring participation:** Meetings may be dominated by local elites; attendance may be low; complaints mechanisms may not be used. These are both compliance problems and informative process outcomes. The ITT estimate remains valid; the TOT interpretation requires the IV approach.
- **Treatment crossover:** Control projects may receive audits through other channels; treated projects may face obstacles that prevent monitoring from occurring. Document all such instances.

### Missingness and attrition
- **Project non-completion:** Projects may be abandoned for reasons correlated with both treatment and potential leakage (e.g., a corrupt implementer facing a community audit may abandon the project). This is differential attrition and requires bounding approaches.
- **Item non-response:** Some physical measurements may be infeasible for certain project types. Pre-specify how missing components are handled (imputation with bounds, or analysis restricted to complete cases with sensitivity checks).

### Spillover
- **Information spillover:** Knowledge that monitoring is happening (in either form) may spread to control projects or to other projects managed by the same implementers, changing their behavior. This biases ITT estimates toward zero (if spillover reduces leakage in controls) or away from zero in unpredictable directions.
- **Resource spillover:** If audit staff or community facilitators are a fixed resource, treating some projects reduces the resources available for others. This can create a negative spillover (control projects get less monitoring than they would in the absence of the experiment).
- **Market spillover:** If the experiment is large enough to affect local markets for construction materials or labor, price benchmarks may be contaminated.

### Implementation limits
- **Enumerator blinding:** Community monitoring activities (public meetings, posted budgets) are inherently visible. Enumerators may infer treatment status, which could affect measurement behavior. Physical measurements from standardized instruments reduce this risk; user surveys are more vulnerable.
- **Simultaneity:** If the experiment changes implementer behavior during construction, the set of projects that reach completion may differ across arms, complicating inference about project-level effects.
- **Ethical constraints:** Withholding monitoring from control projects when monitoring is believed to reduce corruption raises ethical concerns. The design should include a plan to extend beneficial monitoring to control projects after outcome measurement.

---

## 16. Failure Modes and Alternative Explanations

| Failure Mode | Description | Mitigation |
|-------------|-------------|------------|
| **Strategic substitution** | Monitoring reduces leakage in measured margins but increases it in unmeasured margins (e.g., from quantity to quality, from construction to maintenance) | Measure as many margins as feasible; report exactly what is and is not measured; the combined arm (T3) may reduce substitution opportunities |
| **Hawthorne effects** | Behavior changes temporarily because of observation, not because of deterrence or accountability; effects fade when monitoring ends | Include a follow-up measurement wave after monitoring ends; test whether effects persist |
| **Enumerator demand effects** | Enumerators (who know or infer treatment status) systematically rate treated projects differently | Blinding protocols; standardized instruments; inter-rater reliability tests; comparison of subjective vs. objective measures |
| **Differential attrition** | Corrupt implementers abandon monitored projects, so measured leakage falls only because the worst projects drop out | Bounding exercises; analysis of project completion rates by arm |
| **Anticipatory behavior** | Implementers change behavior between randomization and treatment implementation | Measure baseline leakage if possible; use pre-determined covariates as placebo outcomes |
| **John Henry effects** | Control-group implementers, knowing they are in a study, increase effort to demonstrate they are not corrupt | Understates treatment effects; mitigates ethical concerns but reduces statistical power |
| **Elite capture of community monitoring** | Community meetings are dominated by local elites who redirect monitoring toward their interests, potentially increasing rather than reducing leakage | Measure who participates; heterogeneity analysis by community inequality measures |
| **Auditor capture** | Formal auditors are bribed or socially pressured | Audit quality checks; comparison of auditor findings with independent measurements; rotation of auditors |
| **Gaming of measurement protocol** | Implementers learn what is being measured and optimize only those margins | Vary the specific items measured across projects or waves; include unannounced measurement components |

---

## 17. What Cannot Be Claimed

1. **The total effect of monitoring on corruption.** Only the effect on *measured* leakage can be estimated. Corruption through channels not captured by the measurement protocol (collusion in contractor selection, nepotism in staffing, political favoritism in project allocation, bribery that does not affect project costs or quality) remains unobserved.

2. **That monitoring *eliminates* corruption.** Even large estimated effects do not imply that corruption is absent in treated projects, only that measured leakage is lower than in control projects.

3. **The precise mechanism through which monitoring operates.** The design can provide suggestive evidence on deterrence vs. participation vs. reporting channels, but cannot cleanly separate them without additional experimental variation (e.g., cross-cutting audit probability with penalty severity, or cross-cutting information provision with participation facilitation).

4. **General equilibrium or scale-up effects.** The experiment estimates partial equilibrium effects holding the monitoring system fixed. If monitoring were scaled to all projects, implementer and market responses could differ.

5. **Cost-effectiveness without comprehensive cost data.** The design estimates effectiveness, but cannot compare cost-effectiveness across arms without systematic cost data on both the monitoring interventions and the independent measurement protocol.

6. **Long-run effects beyond the study period.** Without extended follow-up, whether effects persist, fade, or reverse after the study ends is unknown.

7. **External validity to other settings.** The treatment effects are identified for the specific institutional, cultural, and economic context of the study. Transportability to other settings requires additional assumptions.

---

## 18. Additional Data Needed

For the design to be implemented, the following data would be required beyond what is described in the task packet:

| Data Need | Purpose | Feasibility Note |
|-----------|---------|-----------------|
| **Complete project roster** with characteristics (budget, sector, location, implementing agency, timeline) | Sampling frame construction and stratified randomization | Typically available from program administrative data |
| **Project engineering specifications and bills of quantities** | Baseline for physical measurement protocol; defines what should be present | May need to be collected as part of baseline |
| **Local market price data** for major inputs at the time and location of project implementation | Price benchmarking for leakage index construction | Requires independent market surveys contemporaneous with project implementation |
| **Administrative expenditure records** (official reports of spending by line item) | Construction of official-independent discrepancy | Typically available from program records; must be collected independently of the measurement protocol |
| **Implementing agency characteristics** (staffing, prior audit history, institutional type) | Covariates for adjustment and heterogeneity analysis | May require separate institutional survey |
| **Community characteristics** (population, poverty, literacy, existing organizations, distance to administrative centers) | Heterogeneity analysis; assessment of community monitoring feasibility | Baseline household/community survey |
| **Process monitoring data** (audit completion, meeting attendance, grievances filed) | Compliance analysis; TOT estimation | Requires embedded process monitoring system |
| **Cost data for interventions** (auditor time, facilitator costs, materials for community meetings) | Cost-effectiveness analysis | Requires tracking of intervention implementation costs |

---

## 19. Threat-Response Table

*(The task packet did not explicitly request a separate threat-response table beyond the failure modes in Section 16, but this is included for completeness.)*

| Threat to Validity | Type | Response |
|--------------------|------|----------|
| Non-random selection into monitoring arms | Internal validity | Random assignment with verification through balance tests |
| Official records as manipulated outcome measure | Measurement | Independent physical measurement protocol |
| Substitution into unmeasured corruption margins | Construct validity | Measure multiple margins; report measurement scope transparently |
| Differential attrition | Internal validity | Bounding exercises; analyze completion rates |
| Spillover between treatment arms | SUTVA | Cluster randomization at agency level; spatial spillover tests |
| Hawthorne / observer effects | Internal validity | Follow-up measurement; comparison of short-run vs. sustained effects |
| Low statistical power | Precision | Power calculations during design; covariate adjustment; outcome indices |
| Multiple testing | Inference | Pre-specified primary outcome; FWER/FDR control; summary indices |
| Treatment non-compliance | Construct validity | ITT as primary analysis; IV for TOT as secondary |
| Enumerator bias | Measurement | Blinding; standardized instruments; inter-rater reliability |
| Elite capture | Treatment integrity | Participation tracking; heterogeneity by community inequality |
| External validity | Generalizability | Transparent reporting of context; replication in other settings recommended |

---

## 20. Claim-Evidence Table

| Claim | Evidence Used | Claim Type | Confidence | What Would Falsify This Claim |
|-------|---------------|------------|------------|-------------------------------|
| Assignment to formal oversight reduces independently measured leakage (β₁ < 0) | ITT estimate from randomized comparison of T1 vs. T0 on independently measured leakage index | Causal (ITT) | High (if randomization successful) | β̂₁ ≈ 0 with tight confidence intervals, verified by randomization inference |
| Assignment to community monitoring reduces independently measured leakage (β₂ < 0) | ITT estimate from randomized comparison of T2 vs. T0 | Causal (ITT) | High (if randomization successful) | β̂₂ ≈ 0 with tight confidence intervals |
| The combined intervention has a larger effect than either alone (β₃ > max(β₁, β₂)) | ITT estimate from T3 vs. T0 compared to T1 and T2 estimates | Causal (ITT) | Moderate (requires sufficient power for interaction tests) | β̂₃ ≤ max(β̂₁, β̂₂); failure to reject β₃ = β₁ + β₂ |
| Formal oversight and community monitoring differ in effectiveness (β₁ ≠ β₂) | Test of equality of coefficients from primary specification | Causal (ITT) | Moderate (depends on power and effect size difference) | Failure to reject β₁ = β₂ |
| Monitoring reduces leakage through deterrence (not just reporting changes) | Comparison of β coefficients in leakage equation vs. discrepancy equation; if leakage falls *and* discrepancy narrows proportionally, consistent with deterrence | Mechanistic (suggestive) | Low (alternative mechanisms consistent with same pattern) | Leakage unchanged but discrepancy narrows (pure reporting effect); or leakage falls but discrepancy unchanged (measurement pattern inconsistent with deterrence) |
| Monitoring effects are not driven by differential attrition | Bounding analysis; test of differential completion rates | Diagnostic | High for ruling out; moderate for precise bounding | Significant difference in attrition rates; Lee bounds include zero |
| Treatment effects are not contaminated by spillover | Spatial spillover tests; donut-hole analysis | Diagnostic | Moderate (spillover tests have limited power) | Significant correlation between control outcomes and proximity to treated projects |
| Independent measurement protocol is not biased by treatment status | Comparison of measurement characteristics across arms; inter-rater reliability | Diagnostic | Moderate | Systematic differences in measurement variance or item non-response by arm; poor inter-rater reliability |
| Community monitoring is not captured by elites | Heterogeneity of T2 effects by community inequality measures | Mechanistic (suggestive) | Low | T2 effects concentrated in high-inequality communities (but this could also reflect greater scope for improvement) |
| Effects persist beyond the monitoring period | Follow-up measurement | Causal (ITT, long-run) | Moderate (attrition risk increases with time) | Follow-up effects converge to zero |

## Tool Log Summary

- actual tool use: none
- trajectory `toolMetas`: []
- toolCall count: 0
- toolResult count: 0
- session_id: isolated_20260529_114115_52386_7
- session_log: /Users/jiangcanxiang/.openclaw/agents/benchmark_isolated/sessions/isolated_20260529_114115_52386_7.jsonl
- trajectory_log: /Users/jiangcanxiang/.openclaw/agents/benchmark_isolated/sessions/isolated_20260529_114115_52386_7.trajectory.jsonl

## Operator Notes

- duration_ms: 183381
- stderr_excerpt: [plugins] plugins.allow is empty; discovered non-bundled plugins may auto-load: qqbot (/Users/jiangcanxiang/.openclaw/npm/node_modules/@openclaw/qqbot/dist/index.js), openclaw-weixin (/Users/jiangcanxiang/.openclaw/npm/node_modules/@tencent-weixin/openclaw-weixin/dist/index.js). Set plugins.allow to explicit trusted ids. [skills] Skipping escaped skill path outside its configured root: source=openclaw-managed root=~/.openclaw/skills reason=symlink-escape requested=~/.openclaw/skills/0-autoresearch-skill resolved=~/.orchestra/skills/0-autoresearch-skill [skills] Skipping escaped skill path outside its configured root: source=openclaw-managed root=~/.openclaw/skills reason=symlink-escape requested=~/.openclaw/skills/brainstorming-research-ideas resolved=~/.orchestra/skills/21-research-ideation/brainstorming-research-ideas [skills] Skipping escaped skill path outside its configured root: source=openclaw-managed root=~/.openclaw/skills reason=symlink-escape requested=~/.openclaw/skills/creative-thinking-for-research resolved=~/.orchestra/skills/21-research-ideation/creative-thinking-for-research [skills] Skipping escaped skill path outside its configured root: source=openclaw-managed r
