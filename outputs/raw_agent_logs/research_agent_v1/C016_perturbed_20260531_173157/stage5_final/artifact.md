# Stage 5: Final Design Memo

---

## 1. Executive Summary

This memo addresses whether targeted risk information delivered in schools changes adolescent behavior more effectively than a standard generic curriculum when only self-reported survey outcomes are available. The perturbed condition — removal of the objective downstream outcome — is fatal to credible causal identification. No within-packet design can separate the effect of targeted information on true behavior from its effect on reporting propensity, because the treatment itself differentially changes what students know about risk and, plausibly, how they report sensitive behavior.

The strongest defensible response is a **descriptive partial-identification bounds analysis** that replaces point identification with transparently qualified interval estimates. The ITT, difference-in-differences, and partner-characteristic triangulation designs all implicitly assume away the core underidentification problem and are therefore not defensible under the packet constraints. The bounds approach follows the packet's explicit instruction to downgrade the claim when strong causal identification is no longer justified. Its practical value depends on auxiliary data the packet does not supply; absent such data, the bounds will be too wide to support policy conclusions. Concrete recommendations for additional data collection are provided in Section 18.

---

## 2. Research Question

Does exposure to targeted risk information (information about differential risk across behavioral choices or partner types) change adolescent behavior more effectively than exposure to a standard generic curriculum, when behavioral outcomes are measured only through self-reported survey responses?

---

## 3. Target Estimand or Strongest Defensible Estimand

**Strongest defensible estimand:** A bounded interval for the average treatment effect of school-level assignment to targeted risk information (vs. generic curriculum) on true behavioral outcomes. The interval is derived from self-reported outcomes under explicit, transparent assumptions about the direction and maximum magnitude of differential reporting bias between treatment arms.

**Why a point estimand is not defensible:** The treatment itself differentially alters what students know about risk. This plausibly changes both their behavior and their propensity to report behavior accurately. Without an objective outcome to benchmark reporting accuracy, the behavioral effect and the reporting effect are jointly underidentified from self-reports alone. No within-packet design resolves this underidentification; it is structural, not a matter of estimator choice.

The bounds estimand explicitly acknowledges this underidentification and produces an interval that is honest about what can and cannot be learned from the available data.

---

## 4. Treatment or Exposure and Main Outcomes

**Treatment/Exposure:** School-level or classroom-wide assignment to one of two information-content conditions:
- **Generic-information condition:** Students receive only the standard generic curriculum.
- **Targeted-information condition:** Students additionally receive information about differential risk across behavioral choices or partner types.

**Main outcomes (all self-reported, measured at a single survey follow-up):**
- Self-reported activity (e.g., participation in behaviors of interest).
- Self-reported partner-profile measures (e.g., age gaps, partner-type composition).
- Self-reported protection behavior (e.g., use of protective measures).

**Secondary outcomes (if observed):**
- Follow-up schooling-status indicators.

---

## 5. Data Structure Summary

| Dimension | Description |
|---|---|
| **Unit of observation** | Individual student in the survey follow-up sample |
| **Time span** | Intervention period plus later survey follow-up; exact dates withheld |
| **Sample construction** | Survey respondents from the focal cohort after the school transition |
| **Treatment assignment level** | School or classroom-wide |
| **Outcome measurement level** | Individual student |
| **Panel structure** | Single selected survey follow-up; no broad verified tracking |
| **Treatment variation source** | Planned school-level variation in information content |
| **Baseline data** | School characteristics, cohort composition, available pre-treatment environment measures |
| **Key missing element** | No objective downstream outcome (the perturbed condition) |
| **Compliance concern** | Exposure varies with attendance or participation |
| **Spillover concern** | Students may exchange information across cohorts or schools; partner markets create interference |

---

## 6. Relevant Causal Mechanisms

**Behavioral mechanism (the intended pathway):** Targeted information about differential risk across choices or partner types increases students' perceived risk of certain behaviors relative to others, leading them to substitute away from higher-risk behaviors or partner types. This is the mechanism the research question seeks to estimate.

**Reporting mechanism (the confounding pathway):** The same targeted information changes what students know about risk, which in turn changes how they interpret survey questions and how willing they are to report sensitive behaviors accurately. A student who learns that certain behaviors carry elevated risk may:
- **Underreport** those behaviors due to heightened stigma or shame (the information makes the behavior newly salient as "bad").
- **Overreport** protective behaviors due to increased social-desirability pressure (the information makes protection newly salient as "good").
- **Reclassify** partner characteristics differently (e.g., an age gap previously seen as normal may now be seen as a risk factor worth mentioning).

**The fundamental problem:** These two mechanisms operate through the same channel — the information content itself — and produce observationally equivalent patterns in self-reported data. Both predict that targeted-information students will report less risky behavior at follow-up. One interpretation is that behavior changed; the other is that reporting changed. The available data cannot distinguish them.

---

## 7. Main Identification Challenge

The core identification challenge is the **underidentification of the behavioral treatment effect from the reporting treatment effect**. The treatment (targeted risk information) is hypothesized to change behavior, but it also differentially changes the measurement process — what students know about risk, how they interpret survey items, and how honestly they report sensitive behaviors.

In the base case (the unperturbed task), an objective downstream outcome related to unsafe behavior was available. This objective outcome provided a benchmark: it was plausibly unaffected by differential reporting bias because its measurement did not depend on student self-report. The treatment effect on the objective outcome could be interpreted as the behavioral effect, and the gap between the treatment effect on self-reports and on the objective outcome could be interpreted as the reporting effect.

In the perturbed case, the objective outcome is removed. Self-reported outcomes are the only measures available. The treatment effect on self-reports is a single reduced-form quantity that conflates:

> *Effect on self-reports = Effect on true behavior + Effect on reporting propensity*

With only one observable quantity and two unknown parameters, the behavioral effect is not point-identified.

---

## 8. Whether Credible Causal Identification Is Possible

**No.** Credible causal identification is not possible under the packet constraints.

The Stage 4 critique confirms this conclusion for each candidate design:

- **School-level ITT (Candidate 1, `not_defensible`):** The critical assumption — no differential reporting bias between arms — is precisely the condition the perturbed packet has broken. The ITT conflates behavioral effects with measurement effects, and the missing objective outcome makes this confound untestable.

- **Difference-in-differences (Candidate 2, `not_defensible`):** DiD removes time-invariant confounds but does not address treatment-induced changes in the measurement process. The parallel-trends violation is built into the treatment mechanism, not an external shock. Furthermore, the packet does not confirm that baseline behavioral survey measures exist; the pre-treatment measures mentioned could be demographic or administrative rather than the same self-reported behavioral outcomes.

- **Partner-characteristic triangulation (Candidate 3, `not_defensible`):** The design rests on an untestable hierarchy of reporting bias across item types that the packet provides no evidence for. Moreover, because the treatment specifically targets partner-type risk information, partner-characteristic items may carry *larger* differential reporting bias than activity items — the opposite of what the design requires.

No candidate design achieves credible causal identification. The problem is structural, not a matter of estimator choice or additional within-packet modeling.

---

## 9. Proposed Empirical Design: Descriptive Partial-Identification Bounds Analysis

Following the packet instruction — "If strong causal identification is no longer justified, the answer must explicitly downgrade the claim or propose additional design changes" — the proposed design is a **descriptive partial-identification bounds analysis**.

### Design Logic

Rather than attempting to point-identify the causal effect, the design:

1. **Estimates the reduced-form ITT** of school-level information-content assignment on each self-reported outcome using the available cross-school variation. This is the only quantity the data can credibly estimate without additional assumptions.

2. **Imposes explicit, transparent bounds** on the differential reporting bias parameter, drawing on the best available auxiliary evidence (institutional knowledge, survey-methodology literature, sensitivity of the population and items).

3. **Produces a bounded interval** for the true behavioral treatment effect by subtracting the reporting-bias bound from the reduced-form estimate.

4. **Presents a sensitivity analysis** showing how the bounds widen or narrow under different assumptions about reporting bias magnitude and direction, so that stakeholders can assess what conclusions are robust to plausible bias ranges.

### Concrete Implementation Options

**Option A: Worst-case (Manski) bounds.** With no assumptions about reporting bias, bound the true behavioral effect using the logical limits of the outcome variable. If the outcome is binary (e.g., any risky activity: 0/1), the worst-case bounds are [−1, 1] — substantively uninformative but logically correct. This option quantifies the severity of the underidentification and demonstrates that the data alone cannot support any substantive conclusion.

**Option B: Monotone reporting bias bounds.** If institutional knowledge or survey-mode evidence supports the assumption that targeted information makes students *more* likely to underreport risky behavior (i.e., reporting bias is monotone in a known direction), the bounds can be tightened. For example, if reporting bias is assumed non-negative (students in the treatment arm underreport risky behavior relative to the control arm by at most δ), the behavioral effect interval is:

> [ITT_self-report, ITT_self-report + δ]

where δ is the maximum plausible underreporting differential.

**Option C: Auxiliary-data-calibrated bounds.** If external validation data can be obtained (see Section 18), bounds can be calibrated against an objective benchmark in a subsample, producing empirically grounded rather than assumed bounds.

### Why This Is the Strongest Defensible Response

This design is the only candidate that:
- Does not implicitly assume away the core underidentification.
- Follows the packet's explicit instruction to downgrade the claim.
- Makes its assumptions transparent and testable (conditional on obtaining auxiliary data).
- Provides a framework for stakeholders to assess what conclusions survive under different plausible bias scenarios.

---

## 10. Why the Design Is Valid or Why Causal Identification Is Not Credible

**Causal identification is not credible** because the treatment differentially affects both the outcome of interest (true behavior) and the measurement process (reporting propensity), and the perturbed condition removes the objective benchmark that could separate them. This is a structural underidentification, not a weakness of any particular estimator.

**The bounds design is valid as a descriptive analysis** because it:
1. Estimates the only quantity the data can credibly identify: the reduced-form association between information-content assignment and self-reported outcomes.
2. Does not claim to have solved the underidentification.
3. Makes the severity of the underidentification transparent through the width of the bounds.
4. Allows stakeholders to assess what policy conclusions require what assumptions about reporting bias.

The validity of the bounds design is not in its ability to produce a narrow causal estimate — it cannot — but in its intellectual honesty about what the data can and cannot support.

---

## 11. Required Assumptions

### For the reduced-form ITT estimate (common to all approaches):

1. **School-level assignment is as-good-as-random** conditional on observables, or school-level unobservables are uncorrelated with assignment. The packet describes "planned school-level variation," which suggests some level of control, but the nature of selection into assignment conditions is not fully specified.

2. **No differential attrition** from the focal cohort to the survey follow-up sample across information-content conditions. If targeted information changes students' likelihood of being present for the follow-up survey (e.g., through differential school dropout or survey non-response), the follow-up sample is selected on treatment.

3. **Stable unit treatment value assumption (SUTVA)** at the school level: a student's outcomes depend only on their own school's information-content condition, not on the conditions in other schools. The packet flags spillover concerns (student information exchange across cohorts/schools, partner-market interference).

### Additional assumptions required by the bounds analysis:

4. **Direction and magnitude of differential reporting bias can be credibly bounded** using institutional knowledge, survey-methodology evidence, or auxiliary data. This is the critical assumption — and the packet provides no direct support for it. Without auxiliary data, bounds are either uninformative (worst-case) or assumption-driven (monotonicity).

5. **Reporting bias operates monotonically** (if monotonicity bounds are used): the treatment shifts reporting in a known direction for all students, with no crossing of reporting functions.

### What the bounds design does NOT assume:

The bounds design explicitly does **not** assume away differential reporting bias, does **not** assume that partner-characteristic items are less biased than activity items, and does **not** assume that differencing removes treatment-induced measurement change. These are the assumptions that make Candidates 1–3 indefensible.

---

## 12. Statistical Model or Analysis Equation

### Reduced-form ITT estimation

For student *i* in school *s*, with school-level information-content assignment *T_s* ∈ {0, 1} (1 = targeted information, 0 = generic):

> *Y_{is}^{self} = α + β · T_s + X_{is}γ + ε_{is}*

where:
- *Y_{is}^{self}* is the self-reported outcome (activity, partner characteristics, or protection behavior).
- *β* is the reduced-form ITT of information-content assignment on self-reported outcomes.
- *X_{is}* is a vector of baseline controls (school characteristics, cohort composition, pre-treatment environment measures).
- *ε_{is}* is clustered at the school level.

### Decomposition of the reduced-form estimate

The self-reported outcome is the sum of true behavior and reporting error:

> *Y_{is}^{self} = Y_{is}^{true} + e_{is}(T_s)*

where the reporting error *e_{is}(T_s)* may depend on treatment assignment. The reduced-form ITT then decomposes as:

> *β = β^{true} + [E(e | T=1) − E(e | T=0)]*
> *β = β^{true} + Δe*

where *β^{true}* is the true behavioral treatment effect (the quantity of interest) and *Δe* is the differential reporting bias between arms.

### Partial-identification bounds

With *Δe* bounded in [*Δe_L*, *Δe_U*]:

> *β^{true} ∈ [β̂ − Δe_U, β̂ − Δe_L]*

Under worst-case (Manski) bounds for a binary outcome: *β̂ − 1 ≤ β^{true} ≤ β̂ + 1*.

Under monotone underreporting (Δe ≥ 0, bounded above by δ):

> *β̂ ≤ β^{true} ≤ β̂ + δ*

### Sensitivity analysis

Report *β̂* and the interval for *β^{true}* as a function of δ ∈ {0, 0.05, 0.10, 0.20, ...}, showing at what δ the sign or policy relevance of the effect changes.

---

## 13. Robustness, Placebo, Falsification Checks, or Diagnostic Tests

### Feasible checks within packet constraints:

1. **Balance tests on pre-treatment covariates.** Test whether school characteristics, cohort composition, and available pre-treatment environment measures are balanced across information-content conditions. Imbalance would suggest non-random assignment and require covariate adjustment or caution in interpretation.

2. **Attrition analysis.** Compare the characteristics of students who appear in the follow-up survey sample vs. those who do not, by information-content condition. Differential attrition on observables would raise concerns about differential attrition on unobservables.

3. **Within-item consistency checks.** If the survey contains items that should be logically consistent (e.g., reports of any activity should be consistent with reports of specific activity types), test whether consistency rates differ across arms. Differential inconsistency would be evidence of differential reporting quality.

4. **Sensitivity of bounds to alternative bias assumptions.** Report how the bounded interval changes under a range of plausible assumptions about Δe's direction and magnitude. This is the core diagnostic: it shows stakeholders which conclusions are robust to which bias scenarios.

5. **Don't-know/refusal analysis.** If the survey records item non-response or "don't know" responses, test whether these rates differ across arms. Differential item non-response is a weak proxy for differential reporting propensity.

### Checks that are NOT feasible without additional data:

- No falsification test can validate the parallel-trends assumption for DiD without baseline behavioral measures.
- No placebo outcome test can validate the absence of differential reporting bias without an objective outcome known to be unaffected by the treatment.
- No within-survey validation can rank item types by reporting-bias sensitivity without an external benchmark.

---

## 14. Heterogeneity Analysis If Supportable

Heterogeneity analysis is supportable for the **reduced-form ITT** on self-reported outcomes — the only quantity the data identifies without additional assumptions. The bounds analysis can also be conducted within subgroups, though subgroup bounds will be wider (less precise β̂ estimates combined with the same or larger Δe bounds).

### Supportable heterogeneity dimensions (if covariates available):

1. **By baseline school characteristics:** Do schools with different pre-treatment environments (e.g., baseline health-curriculum intensity, demographic composition) show different reduced-form associations?

2. **By student characteristics:** If the survey records gender, age, or other demographics, test whether the reduced-form ITT differs across these dimensions. This is descriptive, not causal: any observed heterogeneity could reflect differential behavioral response, differential reporting bias, or both.

3. **By outcome type:** Compare the reduced-form ITT across activity items, partner-profile items, and protection-behavior items. Differences in estimated β̂ across item types are informative about the pattern of self-reported outcomes but cannot be attributed to behavioral vs. reporting mechanisms.

### Important caveat:

Heterogeneity in β̂ across subgroups or item types **cannot** be interpreted as heterogeneity in true behavioral effects. Any observed pattern is equally consistent with differential reporting bias. The bounds design makes this transparent: subgroup-specific or item-specific β̂ estimates are reduced-form associations, not causal effects.

---

## 15. Measurement, Compliance, Missingness, Spillover, or Implementation Limits

### Measurement limits (the core problem):

All outcomes are self-reported. The treatment differentially affects what students know about risk, which plausibly changes how they report sensitive behavior. The packet explicitly states that no objective outcome is available. This is the defining constraint of the perturbed case and the reason causal identification is not credible.

### Compliance and exposure:

The data card notes that "exposure can vary with attendance or participation." The proposed design estimates an intention-to-treat (ITT) effect of school-level *assignment*, not the effect of *receiving* the targeted information. If attendance or participation differs across schools, the ITT captures a mix of compliance and treatment effects. Without individual-level exposure measures, treatment-on-the-treated estimation (e.g., instrumental variables) is not feasible.

### Missingness and attrition:

Students who are absent from the follow-up survey are not observed. If targeted information changes school dropout, absenteeism, or survey participation, the follow-up sample is selected on treatment. The packet provides no information about follow-up response rates, and the bounds design does not address this selection problem (which is additive to the reporting-bias problem).

### Spillover and interference:

The data card flags two spillover channels:
1. **Information exchange across cohorts or schools:** Students may share targeted information with peers in generic-information schools, attenuating the treatment contrast.
2. **Partner-market interference:** If targeted information changes behavior, it may also change the partner pool available to untreated students (e.g., if treated students reduce risky partnerships, untreated students face a different partner market).

Both channels violate SUTVA. The proposed design estimates the reduced-form effect in the presence of spillover, which is a policy-relevant parameter (total effect including equilibrium adjustments) but is not a pure direct treatment effect.

### Implementation limits:

- **Single follow-up wave:** Precludes analysis of treatment-effect dynamics, persistence, or fade-out.
- **No implementation fidelity data:** The packet does not describe monitoring of whether schools actually delivered the assigned information content as intended.
- **No information about survey mode or timing:** Survey-mode effects (in-person, self-administered, online) interact with reporting bias; the packet provides no detail.

---

## 16. Failure Modes and Alternative Explanations

### Primary failure mode: Differential reporting bias explains all observed effects.

If targeted information changes only what students know and report — not what they do — then the true behavioral effect is zero, and any observed difference in self-reports is entirely a measurement artifact. This cannot be ruled out with the available data.

### Alternative explanations for observed ITT differences:

1. **Differential social-desirability bias.** Treatment-arm students may report lower risky activity not because they engaged in less of it, but because the information made certain behaviors newly stigmatized in their self-concept.

2. **Differential recall or salience.** Targeted information may make certain behaviors or partner characteristics more (or less) salient, changing the accuracy of recall-based reports without changing true behavior.

3. **Differential survey interpretation.** The treatment may change how students understand survey questions (e.g., what "counts" as a certain type of behavior or partner), producing different responses to the same questions without different underlying behavior.

4. **Differential attrition.** If targeted information changes which students appear in the follow-up survey, the composition of the treatment and control samples differs, and observed differences may reflect selection rather than treatment.

5. **Spillover contamination.** If students in generic-information schools receive targeted information through peer networks, the treatment contrast is attenuated, and the ITT understates any true effect.

6. **Implementation heterogeneity.** If schools vary in how they deliver the information content, treatment-effect heterogeneity may be misattributed to student characteristics rather than implementation quality.

---

## 17. What Cannot Be Claimed

In light of the Stage 4 critique, the following claims **cannot** be made:

1. **That targeted risk information causally changes adolescent behavior.** The data cannot separate a behavioral effect from a reporting effect. Any statement that the treatment "reduces risky behavior" rather than "reduces self-reported risky behavior" is unsupported.

2. **That the ITT on self-reports identifies a causal behavioral parameter.** The ITT estimate β̂ conflates the true behavioral effect and the differential reporting bias. Neither the sign nor the magnitude of β^{true} can be identified from β̂ alone.

3. **That DiD resolves the identification problem**, even if baseline behavioral measures exist. DiD addresses time-invariant unobserved heterogeneity, not treatment-induced changes in the measurement process. The parallel-trends assumption for measurement error is violated by construction.

4. **That partner-characteristic items are less biased than activity items.** The packet provides no evidence for this hierarchy, and the treatment content specifically targets partner-type risk information, which could increase — not decrease — reporting bias on those items.

5. **That any within-packet design achieves credible causal identification.** The Stage 4 critique confirms this across all four candidates. The underidentification is structural.

6. **That the bounds analysis produces policy-actionable estimates without auxiliary data.** Without external validation data, the bounds are either the trivial [−1, 1] interval (worst-case) or assumption-driven intervals whose credibility depends entirely on the credibility of the assumed bounds — which the packet does not supply.

7. **That the absence of an observed ITT effect on self-reports implies the absence of a behavioral effect.** A zero reduced-form ITT is consistent with a positive behavioral effect offset by differential underreporting, a negative behavioral effect amplified by differential overreporting, or any other combination.

---

## 18. Additional Data Needed

To restore stronger causal interpretation, the following additional data would be needed, in approximate order of feasibility and value:

### Tier 1: Within-study validation (highest value, most feasible)

1. **Objective outcome for a validation subsample.** A random subset of the follow-up sample could be assessed using an objective measure (e.g., biological testing, administrative records, or direct observation), even if infeasible for the full sample. This subsample would calibrate the reporting-bias bounds and transform them from assumption-driven to empirically grounded.

2. **List experiment or randomized response module.** Embedding a list experiment or randomized-response technique within the follow-up survey would provide an alternative, less-biased estimate of sensitive behavior prevalence that could be compared to direct self-reports, quantifying the reporting-bias differential between arms.

3. **Survey-mode experiment.** Randomizing students within schools to different survey modes (e.g., self-administered vs. interviewer-administered) would provide within-study evidence on how reporting sensitivity varies with mode, which could inform bound calibration.

### Tier 2: Strengthened measurement (moderate value, moderate feasibility)

4. **Baseline behavioral survey measures.** Administering the same self-reported behavioral outcomes at baseline (before information delivery) would make DiD feasible and allow assessment of pre-treatment reporting differences across schools. It would not solve the core underidentification (treatment-induced reporting change would remain), but it would eliminate time-invariant reporting confounds.

5. **Repeated follow-up waves.** Multiple follow-up surveys would allow testing whether treatment-control differences in self-reports persist, fade, or grow — patterns that may be differentially consistent with behavioral vs. reporting mechanisms.

6. **Peer or partner reports.** Obtaining reports from peers or partners about the focal student's behavior would provide a partially independent (though not fully objective) benchmark.

### Tier 3: Design changes (lower feasibility, structural solutions)

7. **Information treatment that is less likely to induce differential reporting.** If the targeted information focuses on factual knowledge (e.g., "what is the transmission rate of X?") rather than normative framing ("behavior Y is risky"), it may generate weaker differential reporting bias while preserving the behavioral-relevant information content.

8. **Within-school or within-classroom randomization.** Randomizing at the individual or classroom level within schools would improve statistical power and allow school fixed effects to absorb school-level reporting norms — but would increase spillover risk and still not solve the differential-reporting-bias problem because the treatment content itself creates the bias.

---

## 19. Threat-Response Table

The original task packet does not explicitly request a threat-response table. This section is omitted per the output contract instruction.

---

## 20. Claim-Evidence Table

| Claim | Evidence Used | Claim Type | Confidence | What Would Falsify This Claim |
|---|---|---|---|---|
| Targeted-information assignment is associated with differences in self-reported behavioral outcomes relative to generic-information assignment | Cross-school variation in information-content condition; individual-level self-reported survey outcomes at single follow-up | Descriptive association (ITT on self-reports) | Moderate (the reduced-form association is directly estimable, but its interpretation is contested) | Null finding: no statistically or substantively significant difference in β̂ across arms after accounting for clustering and covariates |
| The ITT on self-reports conflates true behavioral effects with differential reporting bias | Treatment mechanism logic: the information itself changes knowledge about risk, which plausibly changes reporting propensity; the perturbed condition removes the objective benchmark that could separate them | Structural identification claim | High (logically necessary given the packet setup — the treatment differentially affects measurement by construction) | An objective validation subsample showing zero differential reporting bias between arms across all outcome items would falsify this claim |
| No within-packet design can credibly separate behavioral from reporting effects | Stage 4 critique of all four candidate designs; each assumes away the core underidentification in a different guise; the Stage 3 notes concur that "no design achieves credible causal identification" | Structural identification claim | High (derived from the packet's own perturbed condition and the logic of the treatment mechanism) | A design that introduces an objective benchmark or external validation data within the packet constraints (none exists) would falsify this claim |
| Partial-identification bounds can characterize the range of behavioral effects consistent with the data under explicit reporting-bias assumptions | Bounds-analysis logic; the reduced-form ITT is estimable; the decomposition Y_self = Y_true + e(T) is definitional | Methodological claim | High (mathematically correct) | This is a logical framework, not an empirical claim; it cannot be falsified by data, but its practical value can be undermined if bounds are too wide to guide policy |
| Without auxiliary data, the bounds will be too wide to support policy conclusions | Worst-case Manski bounds for binary outcome: [−1, 1]; the packet provides no auxiliary data to tighten them | Methodological claim | High (worst-case bounds are definitionally uninformative for binary outcomes) | Auxiliary data that tightens bounds to a policy-relevant width without introducing untestable assumptions |
| Partner-characteristic items may carry larger differential reporting bias than activity items | Treatment content targets "differential risk across choices or partner types"; this makes partner characteristics directly salient to treatment-arm students and plausibly increases, rather than decreases, reporting bias on those items | Causal mechanism claim (directional) | Low to moderate (logically plausible but untestable without an objective benchmark for partner characteristics) | Validation data showing that partner-characteristic reports have lower differential reporting bias than activity reports across arms |
| DiD cannot address treatment-induced changes in measurement error | The measurement-error component of parallel trends is directly violated by the treatment mechanism; DiD differences out time-invariant confounds, not time-varying, treatment-induced ones | Methodological identification claim | High (definitional: DiD requires parallel trends in the error term; the treatment changes the error term's distribution by construction) | Empirical evidence that the targeted information does not change how students interpret or report survey items (requires objective benchmark) |
| Bounds analysis is the strongest defensible response to the packet constraints | Stage 4 critique verdicts: all three causal designs are `not_defensible`; the bounds design is `defensible_with_caveats`; the bounds design follows the packet instruction to downgrade the claim and makes assumptions transparent | Comparative design assessment | Moderate to high (the ranking follows from the logic of the underidentification; the bounds design is the only one that does not assume it away) | A design not considered here that credibly identifies the behavioral effect from self-reports alone without auxiliary data — but this would require resolving a structural underidentification, which is definitionally impossible |

---

**Summary:** The perturbed condition creates a structural underidentification that no within-packet design can resolve. The bounds analysis is the strongest defensible response because it honestly represents this underidentification, makes assumptions transparent, and provides a framework for what can be learned — and what cannot — from the available data. Its practical value depends on obtaining auxiliary validation data, which the memo recommends as the highest-priority next step.