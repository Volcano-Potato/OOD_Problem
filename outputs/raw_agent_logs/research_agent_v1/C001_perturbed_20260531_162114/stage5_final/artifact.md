# Stage 5: Final Design Memo — C001 Perturbed Variant

## 1. Executive Summary

This memo presents a final research design for estimating whether voluntary contributions in an in-person fundraising setting reflect genuine willingness to support the cause, social pressure from the interaction, or both. The perturbed condition — households self-select into pre-contact notice status rather than being randomly assigned — fundamentally breaks the identification logic available in the base (unperturbed) variant. After reviewing four candidate strategies and an independent critique, the following conclusions emerge:

- **No candidate can credibly point-identify** the separation of social-pressure giving from genuine-willingness giving. The perturbation makes the core research question unanswerable through any single empirical design given the data provided.
- **Candidate 1 (Partial Identification via Contact-Behavior Bounds)** is the recommended primary approach. It is intellectually honest about what can and cannot be learned, makes its assumptions transparent, and provides a framework for bounding the fraction of giving attributable to each mechanism. The Stage 4 critic rated it `defensible_with_caveats`, flagging severe but not fatal concerns.
- **Candidate 2 (Stratified Observational Comparison)** and **Candidate 3 (Solicitor-Induced Contact IV)** are rated `not_defensible` by the critic, and this memo concurs. Candidate 2's conditional-independence assumption is contradicted by the packet; Candidate 3 fails the exclusion restriction and does not answer the research question.
- **Candidate 4 (Descriptive Decomposition)** is adopted as the required fallback. It makes no causal claims but provides the honest descriptive baseline that the packet mandates when credible causal identification fails.
- The strongest defensible claim is that **bounds can be placed on the pressure-versus-willingness decomposition under an explicit monotonicity assumption**, not that the decomposition is point-identified.

## 2. Research Question

Do voluntary contributions in an in-person fundraising request setting reflect genuine willingness to support the cause, social pressure from the face-to-face interaction, or a combination of both?

## 3. Target Estimand or Strongest Defensible Estimand

**Target estimand (aspirational, not point-identified):** The fraction of total giving attributable to social pressure versus genuine willingness, and the average contribution that would be made under each mechanism separately.

**Strongest defensible estimand:** Bounds on the fraction of giving attributable to social pressure versus genuine willingness, derived from observed variation in household pre-contact avoidance choices, contact occurrence, and contribution outcomes, under an explicit monotonicity assumption. These bounds narrow the set of possible decompositions consistent with the data but cannot — and should not be interpreted as — point estimates of each mechanism's contribution.

## 4. Treatment or Exposure and Main Outcomes

**Exposures (all endogenous under the perturbation):**
- Whether the household receives pre-contact advance notice
- Whether the household signals a preference to avoid the visit
- Whether in-person contact actually occurs

**Main outcomes:**
- Whether a contribution is made (binary)
- Contribution amount (continuous, with size bins)

**Secondary outcomes:**
- Whether contact occurs (also serves as an intermediate step in the causal chain)
- Engagement or avoidance behavior
- Contribution-size patterns (small vs. large categories)

## 5. Data Structure Summary

The data follow a three-stage structure observed for each solicitation opportunity:

| Stage | Description | What is observed |
|-------|-------------|-----------------|
| Stage 1 | Route/contact-list construction | Planned solicitation opportunities, route identifiers, solicitor/team assignment |
| Stage 2 | Pre-contact household choice | Whether the household receives advance notice, signals avoidance preference, or takes no action |
| Stage 3 | Solicitation visit window | Whether contact occurs, whether a contribution is made, contribution amount |

The unit of observation is the household or individual solicitation opportunity. Each unit experiences primarily one planned solicitation event. Baseline control variables include route, building, neighborhood, area indicators, contact timing, visit window, and solicitor/team identifiers. Critically, **no household-level characteristics** (income, wealth, past giving, altruism measures, demographics) are available in the packet.

## 6. Relevant Causal Mechanisms

Three mechanisms are relevant to interpreting observed giving:

1. **Genuine willingness (altruism channel):** The household donates because it values the cause. Giving would occur even absent in-person social interaction — e.g., via mail, online portal, or other low-pressure channels.

2. **Social pressure (compliance channel):** The household donates because of the discomfort, obligation, or reputational concern induced by a face-to-face solicitation. Giving would not occur — or would be smaller — absent the in-person interaction.

3. **Selection/engagement (sorting channel):** Households that are more willing to give are also more likely to make themselves available for contact. Pre-contact choices (opting into advance notice, avoiding the visit) are driven by the same unobserved characteristics (altruism, social-desirability bias, income) that determine giving.

The research objective is to separate mechanisms (1) and (2). The perturbation makes mechanism (3) the central confounding force: pre-contact choices are endogenous, and the characteristics driving those choices also drive giving behavior.

## 7. Main Identification Challenge

The core identification challenge is that **the same unobserved household characteristics simultaneously determine pre-contact choices (advance notice uptake, avoidance signaling), contact occurrence, and contribution behavior**. Under the perturbed condition, pre-contact status is chosen by households rather than assigned by the researcher. A household's choice to receive advance notice, signal avoidance, or do nothing is an equilibrium outcome of its latent willingness to engage — the very construct the study aims to measure. This creates a fundamental confounding triangle:

```
Latent willingness → Pre-contact choice
Latent willingness → Contact occurrence
Latent willingness → Contribution (yes/no, amount)
```

No within-household variation exists (one solicitation event per unit), and no experimental instrument is available. The identification challenge is therefore structural: **observational data alone cannot point-identify the pressure-versus-willingness decomposition when pre-contact selection is endogenous and driven by the same unobservables as the outcomes.**

## 8. Whether Credible Causal Identification Is Possible

**Point identification: No.** No candidate design, including all four reviewed in Stage 3, can credibly point-identify the separation of social-pressure giving from genuine-willingness giving under the perturbation. The data structure lacks three essential ingredients: (a) random or as-if-random assignment of pre-contact conditions (removed by the perturbation), (b) a valid instrument for contact or pre-contact choice, and (c) household-level characteristics to model the selection process.

**Partial identification: Yes, with severe caveats.** Bounds on the decomposition are attainable under explicit, transparent assumptions (notably monotonicity of selection into contact). The bounds will likely be wide and the interpretation of avoidance choices is muddied by endogenous selection, but partial identification is the strongest honest claim possible given the data.

**Descriptive analysis: Always possible.** Rich descriptive decomposition of giving patterns by pre-contact choice group, contact status, route, and solicitor is feasible and provides the transparent baseline against which any causal claim must be evaluated.

## 9. Proposed Empirical Design or Strongest Defensible Descriptive Analysis

### Primary Design: Partial Identification via Contact-Behavior Bounds

The proposed primary design is **Candidate 1 from Stage 3**, adopted with the caveats identified by the Stage 4 critic. The design proceeds as follows:

**Step 1 — Classify households by pre-contact choice and contact outcome.**
Define three observable groups based on Stage 2 choices and Stage 3 contact:
- *Notice-takers (N):* Households that receive advance notice
- *Avoiders (A):* Households that signal a preference to avoid the visit
- *Neither-group (X):* Households that take no action (neither opt into notice nor signal avoidance)

Within each group, observe whether contact occurs and whether a contribution is made.

**Step 2 — Impose the monotonicity (no-defiers) assumption.**
Assume that households that would avoid contact under advance-notice conditions would also avoid contact under no-notice conditions. Formally: there are no households who, counterfactually, would seek contact only when given the opportunity to opt out. This assumption bounds the possible type composition of the population.

**Step 3 — Construct worst-case bounds on pressure vs. willingness giving.**
Under monotonicity, the observed contribution rates across the three groups place bounds on:
- The maximum fraction of giving that could be attributable to genuine willingness (under the assumption that all giving by avoiders-who-are-contacted is pressure-driven, and all giving among contacted notice-takers reflects willingness)
- The minimum fraction of giving that could be attributable to social pressure (under the reverse extreme assignment of unobserved types)

**Step 4 — Sensitivity analysis.**
Vary the composition of unobserved types within each observable group to map the set of possible pressure/willingness decompositions consistent with the data. Report the full identified set rather than a point estimate.

### Fallback Design: Descriptive Decomposition of Solicitation Patterns

**Candidate 4 from Stage 3** is adopted as the required descriptive fallback. This involves:

- Tabulating contribution rates, contact rates, and contribution amounts by pre-contact choice group, route, neighborhood, solicitor, and timing window
- Decomposing overall giving rates into components attributable to each observable group
- Visualizing patterns through cross-tabulations and conditional distributions
- Explicitly labeling all results as descriptive associations, not causal effects

This fallback is adopted because the packet's instructions require an explicit descriptive fallback when credible causal identification is not defensible, which is the case here.

## 10. Why the Design Is Valid or Why Causal Identification Is Not Credible

**Why point identification is not credible:** The perturbation removes the one condition — random assignment of pre-contact notice status — that would make the pressure/willingness decomposition point-identifiable through a standard experimental design. Without random assignment, pre-contact choice is endogenous, and the three mechanisms (genuine willingness, social pressure, selection) are observationally confounded. No covariate set provided in the packet can absorb this endogeneity, because the packet provides only supply-side and administrative controls — no household-level characteristics that would model the individual selection process.

**Why partial identification is the strongest defensible approach:** The bounds approach does not claim point identification. It works with (rather than against) the fundamental non-identifiability of the problem. By making the monotonicity assumption explicit and transparent, it provides a framework for narrowing what can be learned from the data. The approach is valid in the sense that it correctly characterizes the set of parameter values consistent with the observed data under stated assumptions, and it makes no claims beyond what those assumptions support.

**Why the descriptive fallback is necessary:** When the bounds are wide (which is likely given the single-observation-per-unit structure and absence of auxiliary data) or when the monotonicity assumption is deemed implausible, the descriptive decomposition provides the honest residual: a transparent presentation of what the data show, without causal interpretation.

This assessment directly reconciles with the Stage 4 critic:

- **Candidate 1 (`defensible_with_caveats`):** Adopted as primary, with caveats fully acknowledged.
- **Candidate 2 (`not_defensible`):** Rejected. The critic correctly identifies that the conditional-independence assumption is contradicted by the packet's own framing ("Potential donors may differ in how much they want to engage with the fundraiser, and pre-contact choices may affect who is ultimately exposed to the interaction"). The available covariates (route, building, area indicators, timing, solicitor IDs) are supply-side variables that cannot plausibly absorb individual-level selection.
- **Candidate 3 (`not_defensible`):** Rejected. The exclusion restriction is affirmatively doubted by the packet ("solicitor behavior may change across routes or conditions"), solicitor assignment is not randomized, and the IV addresses contact→giving rather than the pressure-versus-willingness decomposition.
- **Candidate 4 (`not_defensible` as identification):** Adopted as fallback per packet requirements.

## 11. Required Assumptions

### For the Bounds Approach (Primary Design)

1. **Monotonicity of selection into contact (no defiers):** Households that would avoid contact under advance-notice conditions would also avoid contact under no-notice conditions. There are no households activated to seek contact specifically by the opportunity to opt out. This is the critical untestable assumption.

2. **Contact as necessary intermediate step:** A household can contribute only if contact occurs. No unobserved alternative giving channels are available during the study window.

3. **No within-household spillover from pre-contact information to latent type:** Receiving advance notice does not change a household's underlying willingness to give (only whether contact occurs). This is a stable-unit-treatment-value assumption on the pre-contact margin.

4. **Correctly measured pre-contact choices and outcomes:** Households' advance-notice receipt and avoidance signals are accurately recorded, and contributions are fully observed conditional on contact.

### For the Descriptive Fallback

No causal identifying assumptions are required. The analysis is purely descriptive and makes no claims beyond observed associations.

## 12. Statistical Model or Analysis Equation

### Bounds Approach

Let \( Y_i \in \{0,1\} \) indicate whether household \( i \) contributes. Let \( C_i \in \{0,1\} \) indicate whether contact occurs. Let \( G_i \in \{N, A, X\} \) denote the observable pre-contact choice group (notice-taker, avoider, neither).

Under monotonicity, the population can be partitioned into latent compliance types with respect to advance notice → contact. Define:
- **Always-contacted (AC):** Contact occurs regardless of advance notice
- **Never-contacted (NC):** Contact never occurs
- **Compliers (CO):** Contact occurs only with advance notice
- **Defiers (DE):** Contact occurs only without advance notice — assumed empty under monotonicity

Let \( \pi_{ac}, \pi_{nc}, \pi_{co} \) be the population proportions of each type. Let \( p_{ac}, p_{nc}, p_{co} \) be the probability of giving conditional on being contacted within each type.

The observed contribution rate among contacted notice-takers is a mixture:

\[
P(Y=1 \mid G=N, C=1) = \frac{\pi_{ac} \cdot p_{ac} + \pi_{co} \cdot p_{co}}{\pi_{ac} + \pi_{co}}
\]

The observed contribution rate among contacted avoiders (if any are contacted):

\[
P(Y=1 \mid G=A, C=1) = p_{ac}
\]

The observed contribution rate among contacted neither-group households (if any):

\[
P(Y=1 \mid G=X, C=1) = \text{mixture of types depending on realized contact patterns}
\]

The bounding exercise varies \( (p_{ac}, p_{nc}, p_{co}) \) within [0,1] subject to the observable moment constraints, producing the identified set for the pressure-versus-willingness decomposition.

The pressure fraction (PF) — the share of total giving that would not occur absent in-person social pressure — is bounded by:

\[
PF_{min} = f_{min}(\text{observed rates}) \quad \leq \quad PF \quad \leq \quad PF_{max} = f_{max}(\text{observed rates})
\]

Where \( f_{min} \) and \( f_{max} \) are derived from the extreme assignments of type composition consistent with the data under monotonicity.

### Descriptive Fallback

For the descriptive decomposition, compute:

\[
\bar{Y}_g = \frac{1}{N_g} \sum_{i \in G_i = g} Y_i, \quad g \in \{N, A, X\}
\]

\[
\text{Share}_g = \frac{N_g \cdot \bar{Y}_g}{\sum_{g'} N_{g'} \cdot \bar{Y}_{g'}}
\]

These quantities are reported with the explicit caveat that they represent observed associations, not causal effects of pre-contact choice on giving.

## 13. Robustness, Placebo, Falsification Checks, or Diagnostic Tests

### For the Bounds Approach

1. **Monotonicity sensitivity analysis:** Report bounds under progressively weaker monotonicity assumptions — e.g., allowing a small fraction of defiers (1%, 5%, 10%) and showing how the identified set expands. If bounds collapse to [0,1] under even modest defier fractions, this demonstrates that the bounds are fragile and should not be over-interpreted.

2. **Balance checks on observables:** Compare notice-takers, avoiders, and the neither-group on all available observables (route, neighborhood, timing, solicitor). Large observable differences do not prove selection on unobservables, but the absence of large differences would be surprising given the self-selection mechanism and would warrant investigation.

3. **Solicitor-stratified replication:** Repeat the bounding analysis within each solicitor or solicitor team to check whether the bounds are stable across solicitors. Substantial variation in bounds across solicitors would suggest solicitor-specific effects that the bounding logic does not capture.

4. **Timing-based falsification:** If visit timing is plausibly exogenous within route (e.g., time-of-day variation), test whether contact and contribution rates vary with timing independently of household type. Systematic timing effects would challenge the assumption that contact is solely determined by household type and advance notice.

### For the Descriptive Fallback

No causal falsification tests are applicable. Diagnostic checks are limited to data quality assessments: missingness patterns, contribution amount distributions, and cross-tabulation consistency.

## 14. Heterogeneity Analysis if Supportable

Heterogeneity analysis is limited by the absence of household-level covariates in the packet. The following stratifications are possible:

1. **By route and neighborhood:** Examine whether the bounds on the pressure fraction differ across geographic areas. Differences may reflect variation in community norms around fundraising, social pressure salience, or solicitor assignment patterns — but cannot be causally attributed to any specific mechanism.

2. **By solicitor or team:** Examine whether contact rates and contribution patterns vary by solicitor. If solicitors with higher contact rates also have systematically different contribution patterns conditional on contact, this would provide suggestive (not causal) evidence that solicitor characteristics affect both margins, consistent with the packet's warning.

3. **By contribution size bin:** Examine whether the pressure-versus-willingness bounds differ for small vs. large contributions. If social pressure primarily induces small "token" contributions while genuine willingness drives large gifts, the bounds may differ across contribution size categories. This is speculative absent auxiliary data and should be presented as exploratory.

All heterogeneity analyses are descriptive and subject to the same endogeneity concerns as the main analysis. They cannot identify *why* patterns differ across groups.

## 15. Measurement, Compliance, Missingness, Spillover, or Implementation Limits

**Measurement:**
- Pre-contact choices (advance notice uptake, avoidance signaling) must be accurately recorded. If some households receive notice but do not recall or acknowledge it, misclassification will attenuate differences across groups and widen bounds.
- Contribution amounts may be censored (e.g., cash donations go unrecorded, very large donations are top-coded). Contribution size bins (small vs. large) are coarser but may be more reliably measured.

**Compliance and missingness:**
- "Some households may be absent, unreachable, or inconsistent between stated preferences and realized contact" (packet data card). Absence creates missing outcomes, not zero contributions. The bounds approach must account for non-contact as a distinct state — not as zero giving.
- Inconsistency between stated preferences and realized contact (e.g., a household that signaled avoidance is nonetheless contacted) is informative for the bounding exercise but complicates group classification.

**Spillover or interference:**
- "Neighbors may communicate about the fundraiser" (packet). If a household's pre-contact choice or contribution is influenced by neighbors' behavior, the stable-unit-treatment-value assumption (SUTVA) is violated. The bounds approach does not accommodate spillover.
- "Solicitor behavior may change across routes or conditions" (packet). If solicitors adjust their effort or style based on route characteristics or perceived household type, contact probabilities are not independent across units within a route.

**Implementation limits:**
- The bounds may be too wide to distinguish pressure from willingness in practice. With only one observation per unit and no auxiliary data, the identified set may span [0,1] — meaning the data are consistent with both "all giving is pressure-driven" and "all giving is willingness-driven."
- The analysis cannot be implemented without specifying the exact bounding logic (Manski bounds, Horowitz-Manski bounds with monotonicity, etc.), which requires additional parametric or semi-parametric choices not specified in the packet.

## 16. Failure Modes and Alternative Explanations

### Failure Mode 1: Monotonicity Violation

If advance notice *mobilizes* some households — i.e., learning about the campaign in advance prompts them to be present and give when they would otherwise be absent — then monotonicity is violated. These "defiers" are households for whom advance notice increases (rather than decreases) the probability of contact and giving. Under the perturbation, this failure mode is *more likely* because households that opt into advance notice are precisely those most engaged with the cause. The bounds become invalid if defiers exist.

**Alternative explanation consistent with observed patterns:** Higher contribution rates among notice-takers reflect mobilization of genuinely willing donors, not social pressure on those who would have been contacted anyway.

### Failure Mode 2: Unobserved Alternative Giving Channels

If households that avoid in-person contact can give through alternative channels (mail, online, phone), then contact is not a necessary intermediate step. The bounds approach overstates pressure-driven giving because it attributes all giving among contacted households to the in-person interaction, when some of those households would have given through other channels.

**Alternative explanation:** Giving by contacted households reflects willingness, not pressure — those same households would have donated through alternative channels.

### Failure Mode 3: Endogenous Avoidance as Confounded Signal

Under self-selection, the choice to signal avoidance may reflect: (a) genuine unwillingness to give (supporting the willingness interpretation), (b) acute sensitivity to social pressure (supporting the pressure interpretation), or (c) practical unavailability during the visit window (neither mechanism). The bounds approach uses avoidance behavior as informative about latent type, but endogenous avoidance confounds type with selection.

**Alternative explanation:** Low giving among avoiders reflects selection (low-willingness households avoid contact) rather than revealing that contact-induced pressure would have been effective.

### Failure Mode 4: Solicitor Behavior as Simultaneous Confounder

If solicitors adjust their effort, persistence, or persuasive style based on route characteristics or perceived household receptivity, then contact probability and contribution are simultaneously determined by solicitor behavior. The bounds approach treats contact as determined by household type and advance notice, not by endogenous solicitor adjustment.

**Alternative explanation:** Variation in contribution rates across groups reflects differential solicitor effort allocation, not differences in household pressure sensitivity or willingness.

## 17. What Cannot Be Claimed

In light of the Stage 4 critique and the perturbation, the following claims **cannot** be made:

1. **Cannot claim point identification of the pressure-versus-willingness decomposition.** The critic confirms that no candidate can credibly point-identify this decomposition. The bounds approach yields an identified set, not a point estimate.

2. **Cannot claim that pre-contact choice has a causal effect on giving.** Pre-contact choice is endogenous under the perturbation. Any observed association between pre-contact choice and giving confounds the causal effect of notice/avoidance with selection on unobserved willingness. Candidate 2's attempt to recover this through conditioning is rated `not_defensible`.

3. **Cannot claim that solicitor assignment provides a valid instrument.** The exclusion restriction is affirmatively doubted by the packet and the critic. Candidate 3 is rated `not_defensible`.

4. **Cannot claim that the bounds are narrow or informative.** The bounds may span the full [0,1] interval — i.e., the data may be consistent with "all giving is pressure-driven," "all giving is willingness-driven," and everything in between. The memo can only claim that the bounds *narrow the set of logically possible decompositions under stated assumptions*, not that they *identify a practically meaningful range*.

5. **Cannot claim that the descriptive decomposition (Candidate 4) answers the research question.** The descriptive fallback documents patterns but cannot — and does not — estimate whether giving reflects pressure, willingness, or both. The critic confirms this and the candidate itself acknowledges it.

6. **Cannot claim external validity.** The bounds are identified within the specific fundraising organization, population, and solicitation window described in the packet. No claims about other settings, populations, or fundraising methods are warranted.

## 18. Additional Data Needed

To strengthen the bounds approach or potentially achieve point identification in future work, the following additional data would be required:

| Priority | Data Need | Reason |
|----------|-----------|--------|
| **Critical** | Household-level characteristics (income, wealth, past giving history, relationship with the cause, household composition, demographics) | To model the selection process into pre-contact choice; currently the absence of these variables makes the conditional-independence assumption (Candidate 2) untenable and prevents narrowing bounds |
| **Critical** | Survey measures of altruism, social-desirability bias, and pressure sensitivity | To tighten bounds by excluding implausible type compositions; without these, the bounds are bounded only by logical [0,1] extremes |
| **High** | Random or quasi-random variation in pre-contact conditions | To restore the identification logic available in the unperturbed variant; e.g., randomize the framing of advance notice, the timing of pre-contact outreach, or the default opt-in/opt-out status |
| **High** | Auxiliary data on alternative giving channels | To test whether contact is a necessary intermediate step; if alternative giving channels exist, the bounds overstate pressure-driven giving |
| **Medium** | Repeated solicitation events per household | To observe within-household variation in pre-contact choice and giving, enabling relaxation of the monotonicity assumption and estimation of household fixed effects |
| **Medium** | Detailed solicitor characteristics and assignment protocol | To evaluate whether solicitor assignment is plausibly random or as-if-random; if not, to model solicitor selection |
| **Low** | Post-solicitation survey on motivation for giving/not giving | To provide a direct (if noisy) measure of the pressure-versus-willingness decomposition against which bounds can be validated |

## 19. Threat-Response Table

The task packet does not explicitly request a threat-response table, but one is included for completeness given the severity of the identification challenges:

| Threat | Severity | Response |
|--------|----------|----------|
| Endogenous pre-contact choice (the perturbation itself) | **Fatal for point identification** | Downgrade from point identification to partial identification (bounds). Explicitly acknowledge that the decomposition is not point-identified. |
| Monotonicity violation (defiers mobilized by advance notice) | **Fatal for bounds validity if present** | Conduct sensitivity analysis allowing increasing defier fractions. Report bounds under multiple monotonicity assumptions. If bounds collapse quickly, acknowledge fragility. |
| Bounds too wide to be informative ([0,1] identified set) | **High** | Report full identified set honestly. Present descriptive fallback. Acknowledge that the data cannot distinguish pressure from willingness. |
| Endogenous avoidance confounds type with selection | **High (interpretational)** | Do not interpret avoidance as solely revealing pressure sensitivity or solely revealing unwillingness. Present both interpretations and the resulting range of decompositions. |
| Exclusion restriction violation (solicitor IV) | **Fatal for Candidate 3** | Reject Candidate 3 entirely. Do not present IV results as identifying the pressure/willingness decomposition. |
| No household-level covariates | **High** | Reject Candidate 2's conditional-independence strategy. Acknowledge that the available supply-side covariates cannot absorb individual-level selection. |
| Spillover (neighbor communication, solicitor behavior adaptation) | **Moderate to high** | Flag as a limitation. The bounds approach assumes SUTVA. If spillover is present, all estimates are biased in unknown directions. |
| Alternative giving channels | **Moderate** | If alternative channels exist, the bounds overstate pressure-driven giving. This is a one-sided bias: the bounds approach becomes conservative for the pressure mechanism. |

## 20. Claim-Evidence Table

| Claim | Evidence Used | Claim Type | Confidence | What Would Falsify This Claim |
|---|---|---|---|---|
| Point identification of the pressure-versus-willingness decomposition is not possible under the perturbation | Packet's perturbed condition (pre-contact choice is endogenous); Stage 4 critic assessment that Candidate 2 is `not_defensible` and Candidate 3 is `not_defensible`; absence of random assignment, valid instrument, or household-level covariates | Negative claim (impossibility) | High | Discovery of a valid, packet-supported instrument or natural experiment that generates exogenous variation in pre-contact choice |
| Bounds on the pressure/willingness decomposition can be placed under a monotonicity (no-defiers) assumption | Three-stage data structure (pre-contact choice → contact → contribution); observed contact and contribution outcomes across pre-contact choice groups | Partial identification | Low to moderate (depends on bounds width and monotonicity credibility) | Monotonicity sensitivity analysis showing bounds collapse to [0,1] with small defier fractions; evidence that advance notice mobilizes (rather than deters) contact among engaged households |
| The stratified observational comparison (Candidate 2) does not credibly identify the causal effect of pre-contact choice on giving | Packet statement: "Potential donors may differ in how much they want to engage with the fundraiser, and pre-contact choices may affect who is ultimately exposed"; absence of household-level covariates; Stage 4 critic rating of `not_defensible` | Negative claim (design invalidity) | High | Provision of household-level covariates that absorb selection into pre-contact choice, or evidence of as-if-random pre-contact choice conditional on available covariates |
| The solicitor IV (Candidate 3) does not credibly separate pressure from willingness | Packet warning: "solicitor behavior may change across routes or conditions"; absence of random solicitor assignment; IV addresses contact→giving, not pressure vs. willingness; Stage 4 critic rating of `not_defensible` | Negative claim (design invalidity) | High | Evidence of random or as-if-random solicitor assignment AND evidence that solicitor characteristics affect only contact probability (not contribution amounts conditional on contact) AND an extension that maps the LATE into the pressure/willingness decomposition |
| Observed giving patterns can be described by pre-contact choice group, route, and solicitor without causal interpretation | Full data structure: contact occurrence, contribution yes/no, contribution amount, size bins, pre-contact choices, route/neighborhood/solicitor identifiers | Descriptive | High (trivially, since no causal claim is made) | N/A — descriptive claims are not falsifiable by causal evidence; they would only be falsified by data errors or mismeasurement |
| Self-selection into pre-contact choice is driven by unobserved household characteristics that also affect giving | Packet: "households can choose whether to receive advance notice or indicate that they prefer not to be approached after learning about the fundraising campaign beforehand"; research background framing the entire problem as one of separating observationally confounded mechanisms | Structural claim about data-generating process | High | Evidence that pre-contact choice is independent of latent willingness to give (which would contradict the packet's framing and make the research question trivial) |
| Under the perturbation, no candidate design can point-identify the pressure/willingness decomposition | All four Stage 3 candidates reviewed; Stage 4 critic assessment; the perturbation removes the one condition (random assignment) that made identification possible in the base variant | Synthesis claim | High | A novel design not considered in the candidate set that exploits packet-provided variation not identified in the Stage 3 analysis |

---

**Assessment Summary:** The perturbation — removing researcher assignment of pre-contact conditions — is fatal for point identification of the core research question. The strongest defensible approach (Candidate 1) yields only bounds under a fragile monotonicity assumption, and those bounds may be too wide to be practically informative. The descriptive fallback (Candidate 4) provides the honest baseline. Two candidates (2 and 3) are demonstrably not defensible. The memo's primary contribution is to clarify *what cannot be known* from the available data, which is itself a valuable output when the research question exceeds what the data can support.