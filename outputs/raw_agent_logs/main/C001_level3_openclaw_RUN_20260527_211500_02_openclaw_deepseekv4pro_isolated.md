# Raw Agent Run Log

- `run_id`: RUN_20260527_211500_02_openclaw_deepseekv4pro_isolated
- `case_id`: C001
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
- `timestamp`: 2026-05-27T21:15:00+0800
- `input_file`: benchmark/cases/C001_charitable_giving/agent_task_level3.md
- `system_prompt_summary`: workspace=/Users/jiangcanxiang/OpenClawBenchmarkIsolated; thinking=high; actual_tool_use=none; agent=benchmark_isolated
- `contamination_status`: unknown
- `contamination_reason`: pending manual content review; actual tool use=none
- `status`: success

## Raw Agent Output

# Research Design: Separating Genuine Willingness from Social Pressure in In-Person Fundraising

---

## 1. Executive Summary

This document proposes a multi-arm field experiment that exogenously varies both pre-contact information and the ease of avoiding in-person solicitation. The design exploits random assignment of solicitation-process conditions across planned contact opportunities to decompose the total effect of in-person requests into (a) an awareness/scheduling channel, (b) a sorting/avoidance channel, and (c) a residual pressure or genuine-willingness channel operating conditional on contact. The analysis uses a potential-outcomes framework with principal stratification to bound treatment effects on giving for latent compliance types, combined with pattern-of-evidence tests across contact rates, unconditional giving, and contribution-size distributions. Causal identification of pressure effects is partial: the design can identify bounds and diagnostic patterns consistent with pressure, but cannot point-identify the pressure component without additional structure. The strongest defensible claims are ITT effects on contact and unconditional giving, plus bounded decomposition of the contact versus conditional-giving margins.

---

## 2. Research Question

In an in-person charitable solicitation setting where the researcher controls the solicitation process, to what extent do voluntary contributions reflect (i) genuine willingness to support the cause, (ii) social pressure arising from the difficulty of refusing a face-to-face request, and (iii) changes in awareness or scheduling that alter who is available for contact?

---

## 3. Target Estimand (or Strongest Defensible Estimand)

The design targets three nested estimands, in order of increasing strength of required assumptions:

**Estimand 1 (nonparametric, point-identified).** Intent-to-treat (ITT) effects of solicitation-process condition assignment on:
- Contact probability:  E[C_i(z) − C_i(z′)]
- Unconditional giving:  E[G_i(z) − G_i(z′)]
where z, z′ index two solicitation-process conditions and C_i, G_i are potential contact and giving outcomes.

**Estimand 2 (partially identified, bounds).** The decomposition of the ITT on unconditional giving into:
- A composition margin: the change in giving attributable to the change in *who* is contacted
- A conditional-giving margin: the change in giving attributable to changes in behavior *among those contacted*

This decomposition is partially identified because giving is observed only for contacted units (a sample-selection problem). Bounds are constructed under monotonicity or stochastic-dominance assumptions on contact selection.

**Estimand 3 (pattern-of-evidence, not point-identified).** The "pressure gap" — the portion of unconditional giving that vanishes when avoidance becomes easier, net of changes attributable to awareness or scheduling shifts. This is identified only as a pattern across treatment arms; point identification requires assumptions about the counterfactual giving behavior of avoiders that the data cannot directly verify.

---

## 4. Treatment or Exposure and Main Outcomes

### Treatment arms (illustrative)

The packet describes variation in "solicitation-process conditions" — whether potential donors receive advance information and whether they face different interaction costs before contact. Without specifying exact operational features not in the packet, the design requires at least two dimensions of variation:

| Dimension | Description | Operational examples (illustrative) |
|---|---|---|
| **Information** | Whether potential donors receive advance notice of the upcoming visit | No notice vs. door hanger / leaflet announcing a future visit window |
| **Avoidance ease** | How easy it is to avoid the face-to-face interaction | Standard approach vs. mechanism to decline in advance (e.g., a check-box on a door hanger to opt out of the visit) |

Crossing these dimensions yields a factorial design (e.g., 2×2 or multi-arm). Let Z_i ∈ {0, 1, 2, 3} index the assigned cell.

### Main outcomes

| Outcome | Definition | Measurement level |
|---|---|---|
| Contact (C_i) | Binary: fundraiser reaches and engages the household member | Interaction level |
| Contribution indicator (D_i) | Binary: any positive contribution made | Interaction level |
| Contribution amount (G_i) | Continuous: monetary amount (0 if no contribution) | Interaction level |

### Secondary outcomes

- G_i \| C_i = 1: Giving conditional on contact
- Contribution-size bins (e.g., small vs. large relative to the distribution)
- Any behavioral indicator of avoidance (e.g., not answering the door despite presence indicators, use of opt-out mechanism if available)

---

## 5. Data Structure Summary

| Feature | Detail |
|---|---|
| Unit | Household or individual solicitation opportunity |
| Assignment level | Household / contact opportunity |
| Assignment mechanism | Researcher-controlled randomization of solicitation-process conditions |
| Time span | Short field window around scheduled visits |
| Scope | Multiple local residential areas, single fundraising operation |
| Outcomes | Contact (binary), contribution (binary), amount (continuous) |
| Covariates | Route/neighborhood indicators, timing, solicitor/team IDs, building characteristics if available |
| Repeated exposure | Flagged and tracked; primary analysis uses first planned contact per unit |
| Clustering | Minimum: route, building, or solicitor level |

---

## 6. Relevant Causal Mechanisms

The packet identifies four mechanisms to distinguish:

**M1: Genuine willingness.** Donors actively want to engage and contribute. These individuals would seek out or welcome the interaction and contribute regardless of whether avoidance is easy.

**M2: Pressure / avoidance-cost giving.** Donors prefer to avoid the interaction and contribute only when avoidance is difficult. They give not out of genuine desire but because refusing a direct in-person request is uncomfortable. Making avoidance easier should reduce their giving.

**M3: Awareness / scheduling.** Advance communication changes whether potential donors are present, available, or expecting the visit, without altering their underlying willingness to give conditional on contact. This operates through the contact margin, not the conditional-giving margin.

**M4: Contribution-size sorting.** The size of contributions may be informative about mechanisms: small, token contributions that appear only under high-avoidance-cost conditions are candidate pressure responses, while larger contributions that persist across conditions are candidate genuine-willingness responses.

These mechanisms are not mutually exclusive; the design aims to quantify their relative contributions.

---

## 7. Main Identification Challenge

The central identification problem is a **sample-selection problem with multiple latent types**. Giving outcomes are observed only for households that are contacted (C_i = 1), and contact itself is an endogenous choice that responds to the treatment. The observed difference in mean giving across treatment arms confounds:

1. **Composition effects**: treatment changes *who* is contacted (the sample of observed givers changes)
2. **Behavioral effects**: treatment changes *how much* contacted people give

Without further structure, we cannot separate these. Moreover, among those who give under high-pressure conditions but would avoid under low-pressure conditions, we never observe their counterfactual giving under low pressure. Their giving under high pressure could reflect genuine willingness, pressure, or both.

---

## 8. Whether Credible Causal Identification Is Possible

**Partial causal identification is credible.** The ITT effects on contact and unconditional giving are point-identified under random assignment (the organization controls assignment, satisfying the core identification requirement). The decomposition into contact versus conditional-giving margins is partially identified (bounds). The separation of pressure from genuine willingness is identified only as a *pattern of evidence*, not as a point estimate, because it requires assumptions about the counterfactual giving of avoiders that the data alone cannot verify.

The strongest defensible claims are:
- ITT effects on contact and unconditional giving (point-identified)
- Bounds on treatment effects on giving for latent compliance strata (partially identified)
- Diagnostic patterns consistent or inconsistent with a pressure interpretation (not identified as a parameter, but testable as joint hypotheses)

---

## 9. Proposed Empirical Design

### 9.1 Experimental structure

The design randomizes solicitation-process conditions across planned contact opportunities. The minimal structure requires at least three arms to separate the mechanisms:

| Arm | Pre-contact information | Avoidance ease | What it identifies |
|---|---|---|---|
| **A (Baseline)** | None | Standard (low ease of avoidance) | Baseline contact and giving rates under status-quo pressure |
| **B (Information only)** | Advance notice of visit | Standard (low ease of avoidance) | Effect of awareness/scheduling on contact and giving, holding avoidance cost constant |
| **C (Information + easy avoidance)** | Advance notice of visit | Easy (e.g., opt-out mechanism available) | Effect of reducing avoidance costs, holding information constant |

Additional arms (e.g., easy avoidance without advance notice, if operationally feasible) strengthen identification but are not strictly required.

### 9.2 Randomization and inference

Randomization is at the household level, stratified by route or neighborhood to improve balance. If operational constraints require clustering (e.g., entire routes assigned to one condition), standard errors are clustered at the route level and the design accounts for the reduced effective sample size.

### 9.3 Analysis pipeline

**Step 1: ITT on contact.** Estimate the effect of each treatment arm on contact probability:
- A vs. B: Does advance notice change who is present/available? If contact falls in B relative to A, households are sorting away from the solicitor when informed. If contact is unchanged, advance notice does not alter availability.
- B vs. C: Does easier avoidance further reduce contact? If contact falls in C relative to B, some households use the avoidance mechanism (revealed preference for avoidance).

**Step 2: ITT on unconditional giving.** Estimate the effect on total giving (including zeros for non-contacts):
- A vs. B: If unconditional giving changes when contact changes, the effect operates partly through the contact margin.
- B vs. C: The difference in unconditional giving between B and C is the "pressure gap" — giving that disappears when avoidance becomes easier. This is the key quantity for the pressure interpretation.

**Step 3: Decomposition using bounds.** Under a monotonicity assumption (the treatment only induces households to avoid contact, never to initiate contact who would otherwise avoid), we can bound the average treatment effect on giving for "always-contacted" households using Lee (2009) bounds or principal stratification:

Let the population be partitioned into latent strata based on contact behavior across arms:
- **Always-contacted**: contacted regardless of treatment
- **Avoiders**: contacted only when avoidance is harder (e.g., Arm B but not Arm C)
- **Never-contacted**: not contacted regardless of treatment

For always-contacted households, we observe giving under both B and C. The difference in their mean giving identifies the behavioral effect of easier avoidance, net of composition changes.

For avoiders, we observe giving only under B (the harder-to-avoid condition). Their counterfactual giving under C is unobserved. Bounds on their giving under C can be constructed using trimming or imputation under weak assumptions.

**Step 4: Contribution-size analysis.** Examine the distribution of contribution amounts across arms:
- If small contributions disproportionately disappear in Arm C relative to Arm B (among contacted households), this is consistent with pressure-driven token giving.
- If the entire distribution shifts down, it is consistent with a general reduction in pressure.
- If only the contact rate changes but the conditional giving distribution is unchanged, the effect operates purely through sorting, not pressure.

### 9.4 Pattern-of-evidence tests for pressure

The following joint pattern would support a welfare-relevant pressure interpretation rather than a pure awareness or scheduling interpretation:

| Pattern | Interpretation if observed | Interpretation if absent |
|---|---|---|
| Contact rate falls from B to C | Households actively avoid when given the chance (revealed preference) | No evidence of avoidance demand |
| Unconditional giving falls from B to C by more than can be explained by the contact-rate change alone | Giving conditional on contact is lower when avoidance is easier → some giving under B was pressure-driven | Effect operates entirely through the contact margin → awareness/scheduling story |
| Small contributions disproportionately affected | Token pressure contributions | Pressure operates uniformly or not at all |
| Households that use the opt-out mechanism had positive giving propensity under B | Direct evidence that avoiders would have given under pressure | Avoiders were non-givers anyway → no welfare loss from avoidance |

---

## 10. Why the Design Is Valid (and Its Limits)

**What is valid:**
- Random assignment by the organization (not self-selection by donors) identifies ITT effects on contact and unconditional giving without confounding.
- The multi-arm structure allows separation of the contact margin from the conditional-giving margin under monotonicity.
- The pattern-of-evidence approach does not require strong parametric assumptions and generates testable joint hypotheses.

**What is not point-identified:**
- The fraction of giving attributable to pressure versus genuine willingness is not point-identified because the counterfactual giving of avoiders is fundamentally unobserved. Only bounds are available.
- If avoidance behavior and giving propensity are correlated in ways not captured by observable covariates, the bounds may be wide and uninformative.

---

## 11. Required Assumptions

**A1. Random assignment (point identification of ITT).** Solicitation-process conditions are assigned independently of potential outcomes. Supported by: organization-controlled assignment. Threat: operational deviations from protocol.

**A2. Stable Unit Treatment Value Assumption (SUTVA).** A household's potential outcomes depend only on its own treatment assignment. Threat: neighbor communication or solicitor adaptation across conditions (see spillover analysis).

**A3. Monotonicity of contact response (for bounds).** The treatment does not induce any household to be contacted who would not be contacted under the comparison condition. Formally, C_i(z) ≥ C_i(z′) or C_i(z) ≤ C_i(z′) for all i, for the relevant comparison. This rules out "defiers" who avoid when uninformed but answer when informed. Plausibility: advance notice is unlikely to increase contact among those who would otherwise be absent.

**A4. Exclusion restriction for information-only arm (for mechanism interpretation).** Conditional on contact, advance notice (Arm B) does not directly change giving propensity except through changing who is contacted. Threat: advance notice might change the psychological frame of the interaction (e.g., households feel more obligated because they "knew about it"). This assumption can be probed but not proven.

**A5. No differential measurement error across arms.** Solicitor recording behavior does not vary systematically with treatment assignment. Threat: solicitors aware of treatment conditions may record differently.

**A6. Ignorable non-contact missingness within strata (for bounds).** Within latent contact strata, missing giving outcomes are ignorable conditional on observed covariates.

---

## 12. Statistical Model or Analysis Equations

### 12.1 ITT estimation

For binary treatment arms indexed by a ∈ {A, B, C}:

**Contact:**
$$
\hat{\tau}_C^{a,a'} = \frac{1}{N_a} \sum_{i: Z_i=a} C_i - \frac{1}{N_{a'}} \sum_{i: Z_i=a'} C_i
$$

**Unconditional giving:**
$$
\hat{\tau}_G^{a,a'} = \frac{1}{N_a} \sum_{i: Z_i=a} G_i - \frac{1}{N_{a'}} \sum_{i: Z_i=a'} G_i
$$

With cluster-robust standard errors at the route or solicitor level. Covariate adjustment (route fixed effects, timing indicators, solicitor FE) is included via:

$$
Y_i = \alpha + \sum_{a} \beta_a \cdot \mathbf{1}[Z_i = a] + \mathbf{X}_i'\gamma + \varepsilon_i
$$

### 12.2 Bounds on conditional-giving effects

For the comparison B vs. C, define latent strata:
- Always-contacted (AC): C_i(B) = C_i(C) = 1
- Avoiders (AV): C_i(B) = 1, C_i(C) = 0

Under monotonicity (no households with C_i(B) = 0, C_i(C) = 1):

The observed mean giving in Arm B among contacted is:
$$
E[G_i | C_i=1, Z_i=B] = (1-p) \cdot E[G_i(B) | AC] + p \cdot E[G_i(B) | AV]
$$

where p is the share of avoiders among contacted in Arm B.

In Arm C, only always-contacted are observed:
$$
E[G_i | C_i=1, Z_i=C] = E[G_i(C) | AC]
$$

Lee (2009) bounds: trim the upper or lower p share of the Arm B giving distribution to bound E[G_i(B) | AC]. The difference between this bound and E[G_i(C) | AC] bounds the behavioral effect on always-contacted households.

### 12.3 Decomposition of the ITT on unconditional giving

$$
\underbrace{E[G|B] - E[G|C]}_{\text{Total ITT}} = \underbrace{E[G|B, C{=}1] \cdot P(C{=}1|B) - E[G|C, C{=}1] \cdot P(C{=}1|C)}_{\text{Observed-means decomposition}}
$$

Rewrite as:
$$
\tau_G = \underbrace{E[G|C{=}1, B] \cdot [P(C{=}1|B) - P(C{=}1|C)]}_{\text{Composition margin}} + \underbrace{P(C{=}1|C) \cdot [E[G|C{=}1, B] - E[G|C{=}1, C]]}_{\text{Conditional-giving margin (naive)}}
$$

The naive conditional-giving margin is biased because the set of contacted households differs across arms. The bounds analysis replaces the second term with bounded estimates.

### 12.4 Contribution-size analysis

Estimate quantile treatment effects or test for distributional shifts using:
- Kolmogorov-Smirnov tests of equality of giving distributions (conditional on contact) across arms
- Regression of contribution amount on treatment indicators and their interaction with contribution-size bins

---

## 13. Robustness, Placebo, Falsification Checks, and Diagnostic Tests

### 13.1 Balance checks
- Test that pre-treatment covariates (route characteristics, neighborhood indicators, timing, any baseline donor records) are balanced across arms. Imbalance on observables would suggest a randomization failure or operational deviation.

### 13.2 Placebo / falsification tests
- **Pre-treatment outcomes**: If any pre-existing donor records exist, test that prior giving behavior does not differ across arms. (If no such records exist, this test is unavailable — state this limitation.)
- **Non-contact households**: Among households not contacted, test whether any observable characteristics differ by arm. If treatment affects only contact and not the composition of non-contacts on observables, selection on unobservables is less likely (though not ruled out).
- **Solicitor fixed effects**: If the same solicitor operates across arms, test for solicitor-specific heterogeneity. Systematic differences would suggest protocol deviation or solicitor adaptation.

### 13.3 Bounds sensitivity
- Vary the trimming proportion used in Lee bounds and report how the bounds change.
- If the contact-rate difference between arms is small, the bounds will be tight; if large, acknowledge that the bounds are wide and the decomposition is imprecise.

### 13.4 Alternative mechanisms
- **Scheduling vs. avoidance**: If contact falls from A to B (information effect) but not further from B to C, the effect is scheduling, not pressure-driven avoidance. If contact falls from B to C, it is avoidance.
- **Awareness vs. pressure in giving**: If conditional giving is unchanged across arms but contact changes, the mechanism is awareness/sorting. If conditional giving changes, pressure (or a change in the psychological frame of the interaction) is at work.

---

## 14. Heterogeneity Analysis (If Supportable)

If the data include baseline covariates, explore heterogeneity along:

1. **Neighborhood or route characteristics**: Do contact and giving responses differ across areas with different socioeconomic profiles? Pressure effects may be stronger in closer-knit communities where social norms are more salient.

2. **Timing**: Do effects differ by time of day or day of week? Evening/weekend visits may have different contact rates and pressure dynamics than weekday visits.

3. **Pre-existing donor status** (if available): Do prior donors respond differently from non-donors? Prior donors may have stronger genuine willingness; non-donors may be more susceptible to pressure.

4. **Solicitor characteristics**: If multiple solicitors are used and solicitor identity is recorded, test for solicitor-specific treatment effects. Large heterogeneity would suggest that pressure effects are mediated by solicitor behavior, not just the solicitation protocol.

**Caveat**: The design is powered for main effects, not interactions. Heterogeneity analyses are exploratory and should be pre-registered as secondary rather than presented as primary results.

---

## 15. Measurement, Compliance, Missingness, Spillover, and Implementation Limits

### 15.1 Measurement
- Solicitor-recorded outcomes may be incomplete. If possible, implement independent verification for a random subsample (e.g., follow-up contact or administrative records of contributions). If verification is unavailable, acknowledge measurement error and discuss its likely direction (solicitors may under-record refusals or small contributions).
- Contribution amounts may be top-coded or rounded. Use bins rather than continuous amounts if precision is poor.

### 15.2 Compliance
- Some households assigned to an information treatment may not receive the advance notice (e.g., flyer removed by weather, not seen by resident). This is one-sided noncompliance. The ITT analysis handles this; complier-average causal effects require the additional assumption that advance notice receipt monotonically affects contact.
- Solicitors may deviate from protocol (e.g., using a more or less persistent approach than prescribed). If solicitor-level indicators are available, test for systematic deviation.

### 15.3 Missingness
- Non-contact yields missing giving outcomes. The bounds approach addresses this.
- Incomplete recording by solicitors: if missingness is differential by arm, the ITT estimates are biased. Test for differential missingness rates across arms as a diagnostic. If present, use worst-case bounds (imputing extreme values for missing outcomes).

### 15.4 Spillover
- Neighbors may communicate. If randomization is at the household level within routes, this generates potential interference. Diagnostic: test whether a household's outcomes correlate with the treatment status of nearby households on the same route. If spillover is detected, the design should either (a) move to route-level randomization and accept reduced power, or (b) model and bound spillover effects using partial-interference frameworks.
- Solicitor adaptation: if the same solicitor handles multiple arms, their behavior may drift. Randomize solicitors to arms where feasible, or include solicitor fixed effects and test for arm-specific solicitor heterogeneity.

### 15.5 Implementation limits
- Repeated contact attempts: flag and analyze separately. Primary analysis uses first planned contact.
- The short field window limits temporal dynamics. If the fundraising campaign spans multiple weeks and households learn from neighbors over time, later-treated households may be partially "treated" by information spillovers.

---

## 16. Failure Modes and Alternative Explanations

| Failure mode | Why it matters | How to detect |
|---|---|---|
| **Anticipation changes the psychological frame, not just sorting** | If advance notice makes households feel more obligated ("I knew they were coming"), the B vs. C comparison conflates pressure from the interaction with pressure from the notice itself. Arm B giving could be *higher* than Arm A giving conditional on contact. | Test: Is E[G\|C=1, B] > E[G\|C=1, A]? If yes, advance notice increases obligation, not just awareness. |
| **Differential solicitor effort across arms** | Solicitors who know a household received advance notice may approach differently (more or less persistent). | Test for solicitor×arm interactions; if present, the treatment effect is partly a solicitor-behavior effect. |
| **Selective opt-out signals low giving propensity** | If only households that would not give anyway use the opt-out, the B vs. C comparison overstates the pressure effect. | Compare observable characteristics of opt-out households to contacted households in Arm B. If they are observably similar, selective opt-out is less of a concern. |
| **Scheduling, not avoidance** | Reduced contact under advance notice could reflect genuine scheduling conflicts (households ensure they are out doing errands), not active avoidance of the solicitor. | This is fundamentally difficult to distinguish without direct elicitation of motives. The design can only flag it as an alternative interpretation. |
| **Spillover contaminates control** | If neighbors in Arm A learn about the fundraiser from Arm B/C neighbors, the "no information" condition is compromised. | Test whether Arm A households with more Arm B/C neighbors have different outcomes. |

---

## 17. What Cannot Be Claimed

1. **The exact dollar value of pressure-driven giving.** Only bounds are available. Point identification would require observing the counterfactual giving of avoiders, which is logically impossible without a design that forces contact on all households (which would eliminate the avoidance margin by construction).

2. **That pressure is "bad" in a welfare sense.** The design can show that giving disappears when avoidance is easier, but cannot show that the giving was welfare-reducing. Avoiders might have experienced mild discomfort that they would willingly trade off against the warm glow of giving. Welfare interpretation requires additional assumptions about donor utility.

3. **That the results generalize to other fundraising contexts.** The estimates are local to the specific organization, population, and solicitation protocol studied. Different causes, solicitor types, or community norms could produce different pressure dynamics.

4. **Causal separation of genuine willingness from internalized social norms.** Some "genuine" giving may itself be driven by internalized social norms. The design distinguishes externally imposed interaction pressure from giving that persists when pressure is removed, but cannot distinguish autonomous preference from deeply internalized norms.

5. **That the absence of a pressure pattern implies no pressure.** If the bounds are wide (because the contact-rate difference across arms is small), the design may lack power to detect pressure even if it exists.

---

## 18. Additional Data Needed

| Data element | Why needed | Priority |
|---|---|---|
| **Pre-existing donor records** (if any exist) | Baseline giving history would enable within-household comparisons and strengthen balance checks | High |
| **Independent verification of contact/contribution** (subsample) | To assess measurement error in solicitor-recorded outcomes | High |
| **Household characteristics** (from route planning or administrative data) | Covariate balance checks and heterogeneity analysis | Medium |
| **Solicitor-level protocol adherence indicators** | To distinguish treatment effects from solicitor behavior effects | Medium |
| **Post-solicitation survey** (subsample of contacted and non-contacted households) | To directly elicit motives, awareness of advance notice, and reasons for avoidance | Medium (adds interpretation but risks Hawthorne effects) |
| **Neighbor treatment status matrix** | To model and test for spillover effects | Medium |
| **Exact timing of each contact attempt** | To control for time-of-day effects and test for temporal spillovers | Low |

---

## 19. Threat-Response Table

| Threat | Why It Matters | Proposed Diagnostic or Design Response | Remaining Limitation |
|---|---|---|---|
| **Endogenous contact** (households who are contacted differ systematically from those not contacted) | Giving conditional on contact conflates treatment effects on who is contacted with treatment effects on giving behavior; naive conditional comparisons are biased | Multi-arm design with contact as an observed intermediate outcome; Lee bounds or principal stratification to bound treatment effects on giving for always-contacted households | Bounds may be wide if contact-rate differences across arms are large; the counterfactual giving of avoiders is fundamentally unobserved |
| **Timing / anticipation** (advance notice changes presence, availability, or willingness to engage) | The information treatment may change the psychological framing of the interaction, not just sorting; conflates awareness with anticipation effects | Three-arm structure (A: no notice, B: notice only, C: notice + easy avoidance) allows separate identification of the information effect on contact from the avoidance effect on contact and giving | Cannot fully separate scheduling-based avoidance from solicitor-specific avoidance without direct elicitation of motives |
| **Mechanism confounding** (total contributions mix genuine willingness with discomfort from refusing) | The core research question cannot be answered by observing total giving alone; need to exploit variation in avoidance costs | Comparison of unconditional giving across B and C, combined with bounds on conditional giving for always-contacted, isolates the giving that disappears when avoidance is easier | Disappearing giving could reflect reduced obligation from advance notice itself rather than reduced in-person pressure; cannot point-identify the pressure share |
| **Measurement error** (solicitor-recorded outcomes incomplete or inconsistent) | ITT estimates are biased if recording errors are differential by arm; attenuation bias if classical measurement error | Test for differential missingness rates and solicitor×arm interactions in recording completeness; if independent verification is available, estimate measurement-error-corrected effects for the verified subsample | Without independent verification, measurement error cannot be quantified; worst-case bounds are conservative but may be uninformative |
| **Spillover / interference** (neighbor communication, solicitor adaptation) | SUTVA violation biases ITT estimates and can create false patterns consistent with pressure or sorting | Test for correlation between a household's outcomes and neighbors' treatment status; if detected, use route-level randomization or partial-interference bounds; block solicitors to arms where feasible | Route-level randomization reduces power; partial-interference bounds require modeling assumptions about the spillover structure |
| **Compliance / missingness** (assigned conditions may not translate into actual conditions) | ITT estimates the effect of assignment, not the effect of the solicitation condition as actually experienced; non-contact generates missing outcomes | ITT is the policy-relevant parameter; for mechanism interpretation, estimate complier-average effects under monotonicity; use bounds for missing outcomes under extreme-value imputation as a robustness check | Complier-average effects require additional assumptions; extreme-value bounds may be too wide to be informative |

---

## 20. Claim-Evidence Table

| Claim | Evidence Used | Claim Type | Confidence | What Would Falsify This Claim |
|---|---|---|---|---|
| Solicitation-process conditions causally affect contact probability | ITT estimate of treatment assignment on contact, with cluster-robust inference; balance on pre-treatment covariates | Causal (point-identified under random assignment) | High | Failure of balance on observables; evidence of selective noncompliance or differential attrition by arm |
| Solicitation-process conditions causally affect unconditional giving | ITT estimate of treatment assignment on giving, with cluster-robust inference | Causal (point-identified under random assignment) | High | Same as above; or evidence of spillover that contaminates the control condition |
| Advance notice enables sorting/avoidance, not just scheduling | Contact rate is lower under advance-notice arms (B, C) than under no-notice arm (A), and lower in C than in B (revealed preference for avoidance via opt-out) | Causal (ITT) for contact-rate differences; mechanism inference for sorting vs. scheduling | Medium-High for existence of avoidance; Medium for scheduling vs. avoidance distinction | Contact rate does not differ across arms → no evidence of sorting; contact rate differs between A and B but not B and C → consistent with scheduling-only, not active avoidance |
| Some giving under standard solicitation is pressure-driven | Unconditional giving falls from B to C by more than can be explained by the contact-rate change alone; small contributions disproportionately affected; opt-out households had positive giving under B | Pattern-of-evidence (not point-identified) | Medium | Conditional giving distribution is unchanged across B and C; all giving reduction is explained by contact-rate change; opt-out households were zero-givers under B |
| Contribution size is informative about pressure vs. genuine willingness | Small contributions differentially disappear in low-pressure arm (C); large contributions are stable across arms | Correlational pattern | Low-Medium | Contribution-size distribution shifts uniformly across arms; or small contributions are stable while large contributions change (opposite pattern) |
| Contact selection is non-ignorable | Observable characteristics of contacted households differ across arms; bounds on conditional-giving effects differ from naive conditional estimates | Descriptive / diagnostic | High | No observable differences in contacted-household composition across arms; Lee bounds are trivially tight (but this does not prove ignorability) |
| Spillover effects are absent or small | No correlation between household outcomes and neighbors' treatment assignment; results robust to route-level clustering | Diagnostic (failure to reject null of no spillover) | Medium (limited power for spillover detection) | Significant correlation between own outcomes and neighbor treatment; route-level vs. household-level standard errors differ substantially |

---

## Summary of Design Logic

The design exploits the organization's control over solicitation-process assignment to create exogenous variation in two dimensions: whether potential donors have advance information about the visit, and how easy it is to avoid the face-to-face interaction. The three-arm structure allows the researcher to trace the effect of each dimension on contact and giving, decomposing the total effect into awareness/scheduling, sorting/avoidance, and residual pressure or genuine-willingness channels operating conditional on contact. The strongest defensible claims are the ITT effects on contact and unconditional giving (point-identified under random assignment). The decomposition into pressure versus genuine willingness is identified only through a pattern of evidence — comparing contact-rate changes, unconditional giving changes, conditional giving distributions, and contribution-size patterns across arms — rather than as a point-identified parameter. The design transparently acknowledges that the counterfactual giving behavior of households that avoid solicitation is fundamentally unobserved, and that only bounds on the pressure component are available.

## Tool Log Summary

- actual tool use: none
- trajectory `toolMetas`: []
- toolCall count: 0
- toolResult count: 0
- session_id: isolated_20260527_211500_98725_2
- session_log: /Users/jiangcanxiang/.openclaw/agents/benchmark_isolated/sessions/isolated_20260527_211500_98725_2.jsonl
- trajectory_log: /Users/jiangcanxiang/.openclaw/agents/benchmark_isolated/sessions/isolated_20260527_211500_98725_2.trajectory.jsonl

## Operator Notes

- duration_ms: 806605
- stderr_excerpt: [plugins] plugins.allow is empty; discovered non-bundled plugins may auto-load: qqbot (/Users/jiangcanxiang/.openclaw/npm/node_modules/@openclaw/qqbot/dist/index.js), openclaw-weixin (/Users/jiangcanxiang/.openclaw/npm/node_modules/@tencent-weixin/openclaw-weixin/dist/index.js). Set plugins.allow to explicit trusted ids. [skills] Skipping escaped skill path outside its configured root: source=openclaw-managed root=~/.openclaw/skills reason=symlink-escape requested=~/.openclaw/skills/0-autoresearch-skill resolved=~/.orchestra/skills/0-autoresearch-skill [skills] Skipping escaped skill path outside its configured root: source=openclaw-managed root=~/.openclaw/skills reason=symlink-escape requested=~/.openclaw/skills/brainstorming-research-ideas resolved=~/.orchestra/skills/21-research-ideation/brainstorming-research-ideas [skills] Skipping escaped skill path outside its configured root: source=openclaw-managed root=~/.openclaw/skills reason=symlink-escape requested=~/.openclaw/skills/creative-thinking-for-research resolved=~/.orchestra/skills/21-research-ideation/creative-thinking-for-research [skills] Skipping escaped skill path outside its configured root: source=openclaw-managed r
