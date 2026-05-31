# Stage 5: Final Design Memo

**Case ID:** C002 (Perturbed Variant)
**Perturbation:** Borrowers are informed before application that final contract terms may differ from the initial offer and are shown how those terms are determined.

---

## 1. Executive Summary

The perturbation—showing borrowers the term-determination rule before they apply—fundamentally restructures the strategic environment. Borrowers become active agents who incorporate their knowledge of the rule into take-up, repayment, and re-borrowing decisions, fusing selection and incentive channels at the point of application. This single change breaks the IV exclusion restriction (the perturbation creates a packet-documented selection-composition channel from initial offers to repayment through expected final terms), breaks RD continuity (borrowers can anticipate and sort around any discontinuity they are shown), and weakens the within-borrower panel design (strategic cross-episode behavior creates time-varying unobserved confounding that fixed effects cannot eliminate).

No design can credibly *separate* selection from incentive effects under the perturbation using only the data and variation described in the packet. The within-borrower panel design is the strongest remaining causal strategy: it differences out time-invariant borrower selection and identifies incentive effects of realized term changes on repayment, but only under strong and unverified conditions (the lender observes every input to the term-determination rule, and repeat borrowing is both common and not differentially selected under the perturbation). If those conditions fail, the only defensible product is a descriptive analysis of conditional associations between offer terms, take-up decisions, realized contract terms, and repayment outcomes, with no causal attribution of repayment differences to selection versus incentives.

---

## 2. Research Question

What drives differences in repayment outcomes across borrowers who receive different loan terms—borrower selection at take-up, post-borrowing incentive effects of realized contract terms, or both—and can these channels be separately identified when borrowers know before applying how final contract terms will be determined?

---

## 3. Target Estimand or Strongest Defensible Estimand

The research objective calls for separation of selection and incentive effects. Under the perturbation, no single estimand credibly achieves this separation. The structured set of strongest defensible estimands is:

**Primary causal estimand (within-borrower panel):** The average effect of a change in realized contract terms on repayment outcomes, identified from within-borrower variation in realized terms across repeated borrowing episodes, net of time-invariant borrower unobserved heterogeneity. This identifies the incentive margin only—it does not recover the selection margin.

**Fallback descriptive estimand:** The conditional association between (i) initial offer terms and take-up/borrower composition, and (ii) realized contract terms and repayment outcomes, controlling for observed borrower characteristics. No causal separation is claimed.

**Estimands explicitly not defensible:** The local average treatment effect of realized terms on repayment using initial offer variation as an instrument (IV) and the local average treatment effect at a discontinuity in the term-determination rule (RD) are both classified as `not_defensible` under the perturbation, as explained in Sections 8–9 and 17.

---

## 4. Treatment or Exposure and Main Outcomes

**Treatment/exposure variables:**
- *Pre-borrowing offer terms* (visible before application): interest rate, fee structure, loan amount, duration, or other price/non-price terms shown in the initial offer.
- *Realized contract terms* (finalized after acceptance): the actual terms in the executed loan contract, which may differ from the initial offer according to the determination rule that borrowers are shown ex ante.

**Main outcomes:**
- *Take-up / application:* binary indicator for whether the prospective borrower applies for and accepts the loan.
- *Repayment performance:* delinquency (30/60/90+ days past due), default (charge-off or severe delinquency), or a continuous repayment metric (e.g., fraction of scheduled payments made on time).

**Secondary outcomes:**
- Accepted loan amount.
- Intermediate repayment behavior (e.g., early payments, partial payments, first-payment default).

---

## 5. Data Structure Summary

The data follow a sequential credit process across four observable stages:

| Stage | What is observed | Units affected |
|---|---|---|
| Stage 1: Offer | Initial loan terms offered to eligible prospective borrowers | All prospective borrowers |
| Stage 2: Application/Take-up | Whether borrower applies; borrower characteristics at application | All offered borrowers |
| Stage 3: Contract finalization | Realized contract terms after acceptance | Accepted borrowers only |
| Stage 4: Repayment & future borrowing | Repayment outcomes; future borrowing eligibility and terms | Originated loans |

Key structural features:
- Borrowers *may* have linked observations across all stages and across multiple borrowing episodes (panel/repeated structure is possible but not guaranteed).
- Non-applicants remain observable for take-up analysis but have no repayment outcomes.
- The perturbation operates between Stage 1 and Stage 2: borrowers see the term-determination rule before deciding whether to apply.

---

## 6. Relevant Causal Mechanisms

Four mechanisms link loan terms to repayment outcomes, and the perturbation alters how they interact:

1. **Pure selection (M1):** Borrowers with different unobserved repayment propensities self-select into different offer terms. Under the base packet, this operates through borrowers' responses to the *initial offer*. Under the perturbation, selection additionally operates through borrowers' *expectations of final terms* formed from the initial offer plus the known determination rule applied to their own characteristics.

2. **Pure incentive (M2):** Realized contract terms causally affect repayment behavior after origination (e.g., higher interest rates increase payment burden and default risk; more favorable terms reduce it).

3. **Strategic anticipation of the rule (M3):** *Perturbation-specific.* Borrowers who know the determination rule may alter their application behavior (applying/not applying based on predicted final terms), their pre-application characteristics (manipulating inputs to the rule before applying), and their repayment behavior (repaying strategically in episode 1 to secure better terms in episode 2).

4. **Cross-episode feedback (M4):** *Amplified by the perturbation.* Repayment behavior in an earlier loan episode feeds into the inputs of the known determination rule, altering realized terms in later episodes. This creates a direct path from the outcome (repayment) to future treatment (realized terms).

Under the perturbation, M1, M3, and M4 are no longer separable using only initial-offer variation, because the perturbation makes initial offers just one input into borrowers' expected final terms, and expected final terms—not initial offers—drive take-up decisions.

---

## 7. Main Identification Challenge

The core identification challenge is that the perturbation *fuses* selection and incentive channels at the take-up stage. In the base packet, randomly assigned initial offers could in principle isolate selection (who takes up at which terms) from incentives (how realized terms affect repayment). Under the perturbation:

- **Borrowers' take-up decisions depend on expected final terms, not initial offers.** Expected final terms are a function of both the initial offer and the known determination rule applied to the borrower's own (potentially manipulable) characteristics. Initial offer variation therefore affects *who* applies—not just through a pure preference-for-terms channel but through a borrower-specific expected-final-term calculation.
- **The determination rule is public knowledge.** Any discontinuity, threshold, or functional form in the rule can be anticipated and acted upon before application. This eliminates the quasi-experimental variation that RD and IV designs require.
- **Repayment behavior can feed back into future terms.** A borrower who repays strategically to improve the characteristics that enter the rule in episode 2 creates an endogenous relationship between the outcome and future treatment that operates within-borrower and across time.

---

## 8. Whether Credible Causal Identification Is Possible

**Credible causal identification of the separate selection and incentive channels is not possible** using only the data and variation described in the packet.

The perturbation eliminates both design families that could, in principle, separately identify the two channels:
- **IV strategies** (using initial offer variation as an instrument for realized terms) are broken because the exclusion restriction is violated by a packet-documented mechanism: initial offers affect repayment through borrower composition (initial offer → expected final terms → take-up composition → repayment), not solely through realized terms.
- **RD strategies** (exploiting discontinuities in the term-determination rule) are broken because the perturbation *is* the act of showing borrowers the rule ex ante, which guarantees anticipation-driven sorting and manipulation of the running variable. This is a textbook violation of the no-manipulation condition.

**Credible causal identification of the incentive effect alone is possible under strong and unverified conditions** using a within-borrower panel design that differences out time-invariant borrower selection. This design does not recover the selection margin but can estimate whether within-borrower changes in realized terms affect within-borrower changes in repayment.

If the conditions for the within-borrower panel are not met (insufficient repeat borrowing, unobserved inputs to the rule), then **no causal identification is credible**, and the analysis must be downgraded to descriptive.

---

## 9. Proposed Empirical Design or Strongest Defensible Descriptive Analysis

### 9.1 Primary Design: Within-Borrower Panel (Incentive Effect Only)

**Design:** Estimate the effect of realized contract terms on repayment using within-borrower variation across repeated borrowing episodes, absorbing time-invariant borrower heterogeneity through borrower fixed effects.

**Identifying variation:** Changes in realized contract terms across two or more accepted loans for the same borrower, observed over the linked offer→acceptance→repayment→future-borrowing panel.

**What it identifies:** The average effect of realized term changes on repayment, net of all time-invariant borrower characteristics (including the selection type that the research question targets). This is the incentive margin only. The selection margin—who becomes a borrower at which terms—is differenced out and not recovered.

**Required implementation conditions:**
1. The lender observes and can condition on *every* borrower characteristic that enters the term-determination rule. This is necessary to control for the strategic cross-episode feedback channel (M4) that the perturbation introduces. If any input to the rule is unobserved, within-borrower term changes are contaminated by repayment-driven manipulation of that input.
2. Repeat borrowing is sufficiently common in the data to support precise estimation. The packet states borrowers *can* have linked observations; it does not guarantee they do.
3. The sample of repeat borrowers under the perturbation is not so differentially selected—relative to repeat borrowers under opacity—that the estimated incentive effect has no external validity for any policy-relevant population.

### 9.2 Fallback Design: Descriptive Conditional Association Analysis

**Design:** Estimate conditional associations between (i) initial offer terms and take-up/borrower composition, (ii) realized contract terms and repayment outcomes, and (iii) the joint distribution of offer terms, realized terms, and repayment, all conditional on observed borrower characteristics (pre-offer risk measures, prior credit history, operational indicators).

**What it produces:** A mapping of the empirical landscape—how take-up rates, borrower characteristics, and repayment outcomes covary with initial and realized terms—with no causal attribution of observed differences to selection versus incentives.

**What it does not produce:** Any claim that a particular observed repayment difference is "due to incentives" or "due to selection."

---

## 10. Why the Design Is Valid or Why Causal Identification Is Not Credible

### 10.1 Validity of the Within-Borrower Panel (Conditional)

The within-borrower panel is valid as a strategy for identifying the incentive effect **if and only if** the following conditions hold:

- **Time-invariant selection is the primary confound.** The design differences out any borrower characteristic that does not change across episodes. If selection into borrowing is driven by stable borrower traits (risk preferences, financial literacy, income volatility), fixed effects eliminate it.
- **The lender observes all rule inputs.** The perturbation creates a channel through which episode-1 repayment can alter episode-2 realized terms via the determination rule. If the lender observes every characteristic that enters the rule (e.g., credit score, debt-to-income ratio, internal risk grade) and includes them as time-varying controls, this channel is blocked econometrically. The critical assumption is then that, conditional on borrower fixed effects *and* observed time-varying rule inputs, remaining variation in realized terms is as-good-as-random.
- **Repeat borrowing is non-trivial.** The design requires within-borrower term variation, which requires borrowers with at least two accepted loans.

### 10.2 Why RD Is Not Credible (Not Defensible)

The Stage 4 critic correctly marks `rd_term_determination_rule` as `not_defensible`. The perturbation directly and irreparably violates the core RD identifying assumption:

- **No-manipulation condition violated.** Borrowers are shown the rule and its cutoffs *before applying*. A borrower just below a favorable threshold can manipulate the running variable (e.g., pay down debt to nudge a credit score) or self-select out of the applicant pool. Both behaviors break continuity of the conditional expectation function at the cutoff.
- **No packet evidence of a discontinuity.** The perturbation says borrowers are shown *how* terms are determined. A continuous formula, smooth risk tiers, or a multivariate model without sharp cutoffs generates no discontinuity to exploit. The RD candidate assumes an extra-packet premise.
- **Donut-RD does not restore the original identification.** Discarding observations near the cutoff estimates a different LATE at a point where the first-stage discontinuity no longer drives assignment in the same way, and where selection pressures from the known rule still operate.

No packet-local evidence contradicts the critic's assessment. The perturbation *is* the act that breaks RD.

### 10.3 Why IV Is Not Credible (Not Defensible)

The Stage 4 critic correctly marks `iv_initial_offer_weakened` as `not_defensible`. The perturbation introduces a packet-documented selection channel that violates the exclusion restriction:

- **Direct selection channel from instrument to outcome.** Under the perturbation, initial offer Z affects take-up composition C (borrowers with different unobserved repayment propensities select into borrowing based on expected final terms, which are a function of Z and the known rule). Composition C then affects repayment Y. This path Z → C → Y does not go through realized terms D. The exclusion restriction requires Z → D → Y only.
- **The complier population is uninterpretable.** Even with randomly assigned initial offers, compliers under the perturbation are defined by a two-stage process (apply given expected terms; then have realized terms shift with initial offer) that differs fundamentally from compliers under opacity.

The candidate's own name and Stage 3 analysis acknowledge it is "weakened." The Stage 4 critic correctly upgrades that assessment to "broken." No packet-local evidence contradicts this.

---

## 11. Required Assumptions

### For the Within-Borrower Panel (Incentive Effect)

1. **A1 — Time-invariant unobserved heterogeneity is the dominant confound.** Borrower characteristics that drive both term assignment and repayment are stable across episodes. (Plausible for traits like risk aversion, financial sophistication; less plausible for employment shocks, health events, or life transitions.)

2. **A2 — Conditional exogeneity of within-borrower term changes.** Conditional on borrower fixed effects *and* all time-varying observables that enter the term-determination rule, changes in realized contract terms are as-good-as-random with respect to time-varying repayment shocks. (The perturbation makes this assumption harder to satisfy because it introduces strategic cross-episode behavior; A2 holds only if the lender observes every rule input.)

3. **A3 — No cross-episode carryover effects of terms on repayment through channels other than incentives.** Realized terms in episode 1 do not directly affect repayment capacity in episode 2 except through the treatment in episode 2. (Rules out, e.g., episode-1 terms causing financial distress that persists into episode 2 independently of episode-2 terms.)

4. **A4 — Sufficient within-borrower term variation.** A non-trivial share of borrowers have at least two accepted loans, and realized terms vary across episodes for a meaningful fraction of them. (Unverified in the packet; the packet says borrowers *can* have linked observations, not that they *do*.)

5. **A5 — Repeat borrowers are exchangeable with the broader borrower population for the incentive parameter.** The incentive effect estimated on repeat borrowers generalizes to one-time borrowers. (Strong assumption; repeat borrowers under the perturbed rule may differ systematically.)

6. **A6 — The lender observes all inputs to the term-determination rule.** Any unobserved rule input creates an open backdoor path from episode-1 repayment to episode-2 terms that borrower fixed effects cannot close.

### For the Descriptive Fallback

No causal identifying assumptions are asserted. The analysis conditions only on observables and acknowledges that residual associations may reflect any mixture of selection, incentives, and perturbation-induced strategic behavior.

---

## 12. Statistical Model or Analysis Equation

### 12.1 Within-Borrower Panel Specification

For borrower *i* in borrowing episode *e*:

$$Y_{ie} = \alpha_i + \beta D_{ie} + \gamma' X_{ie} + \delta_t + \varepsilon_{ie}$$

Where:
- $Y_{ie}$: repayment outcome (e.g., delinquency indicator, fraction of payments on time)
- $\alpha_i$: borrower fixed effect (absorbs time-invariant selection)
- $D_{ie}$: realized contract term(s) of interest (e.g., interest rate, fee)
- $X_{ie}$: vector of time-varying controls that enter the known term-determination rule (credit score, DTI, internal risk grade, prior repayment history with this lender)
- $\delta_t$: calendar-time or offer-wave fixed effects
- $\varepsilon_{ie}$: idiosyncratic error

$\beta$ is the parameter of interest: the within-borrower effect of realized term changes on repayment.

**Estimation:** Fixed-effects OLS (or conditional logit for binary repayment outcomes). Standard errors clustered at the borrower level.

**Key diagnostics:**
- Report the number and share of borrowers with multiple episodes.
- Report within-borrower standard deviation of $D_{ie}$ relative to between-borrower standard deviation.
- Test for differential attrition from the repeat-borrower sample by comparing episode-1 characteristics of borrowers who do versus do not return.

### 12.2 Descriptive Association Specification

Cross-sectional specification for the full sample of offered borrowers:

$$\Pr(\text{Take-up}_i = 1) = \Lambda(\theta_1 \cdot \text{InitialOfferTerms}_i + \pi_1' W_i)$$

And for originated loans only:

$$Y_i = \beta_1 \cdot \text{RealizedTerms}_i + \beta_2 \cdot \text{InitialOfferTerms}_i + \pi_2' W_i + u_i$$

Where $W_i$ includes pre-offer risk measures, prior credit history, and operational indicators. All coefficients are interpreted as conditional associations, not causal effects.

---

## 13. Robustness, Placebo, Falsification Checks, or Diagnostic Tests

### For the Within-Borrower Panel

1. **Pre-trend test (pseudo-placebo):** Among repeat borrowers, test whether episode-1 repayment predicts the *direction* of term change between episode 1 and episode 2, conditional on observed rule inputs. If it does, unobserved rule inputs or strategic behavior are contaminating within-borrower term variation.

2. **Balancing test on lagged outcomes:** Test whether borrowers whose terms improve between episodes had systematically different episode-1 repayment (conditional on rule inputs) relative to those whose terms worsen. Rejection suggests violation of A2.

3. **Stability of $\hat{\beta}$ to adding time-varying controls:** Estimate the model with (a) only borrower FE, (b) borrower FE + observed rule inputs, (c) borrower FE + rule inputs + lagged repayment. If $\hat{\beta}$ changes substantially as rule inputs are added, the perturbation's cross-episode feedback channel is operative.

4. **Sample composition check:** Compare the distribution of pre-offer risk measures and episode-1 outcomes for borrowers with one episode versus multiple episodes. If multi-episode borrowers are substantially lower-risk or different on observables, flag external validity concerns.

5. **Placebo outcome test:** Test whether episode-2 realized terms predict episode-1 repayment (which they cannot causally affect). A significant association indicates unobserved time-invariant confounders that fixed effects should absorb; failure to reject supports the FE structure.

6. **Variance decomposition:** Report $R^2$ from borrower indicators alone to assess how much of the variation in terms and outcomes is cross-sectional (differenced out) versus within-borrower (used for identification).

### For the Descriptive Fallback

1. **Sensitivity to observed confounders:** Report coefficient movements as blocks of controls are added to assess how much of the raw association is attributable to observables (Oster-style bounds or coefficient stability tests).

2. **Subsample consistency:** Estimate associations separately by offer wave, branch, or risk tier to check whether patterns are stable or driven by specific subgroups.

---

## 14. Heterogeneity Analysis If Supportable

Heterogeneity analysis faces two constraints: (i) limited within-borrower sample sizes for subgroup estimation, and (ii) the perturbation makes heterogeneous selection responses an integral part of the mechanism, not an auxiliary analysis.

**If the within-borrower panel is feasible and subsamples permit:**

- **By observable risk tier:** Estimate $\beta$ separately for low-, medium-, and high-risk borrowers (based on pre-offer measures). The perturbation predicts that strategic cross-episode behavior may be concentrated among borrowers near the thresholds of the determination rule, generating heterogeneous incentive effects by risk tier.
- **By magnitude or direction of term change:** Test whether the effect of term *increases* differs from term *decreases*, which would indicate asymmetry in how borrowers respond to favorable versus unfavorable term changes.
- **By episode gap:** Test whether the incentive effect differs by the time elapsed between episodes, as strategic planning may be more feasible over shorter horizons.

**If only the descriptive fallback is available:**

- Report associations stratified by pre-offer risk tiers, prior credit history, and offer-wave indicators to map which borrower groups drive the overall patterns.

---

## 15. Measurement, Compliance, Missingness, Spillover, or Implementation Limits

**Measurement:**
- The packet does not specify the granularity of realized contract terms (e.g., whether they are continuous, discrete, or a vector of correlated terms). If realized terms are a bundle (rate + fee + duration), isolating the effect of a single term dimension requires sufficient independent variation.
- The term-determination rule is described as something borrowers are *shown*. Whether it is a simple univariate threshold or a complex multivariate function matters for the feasibility of conditioning on all rule inputs (A6).

**Compliance and missingness:**
- Non-applicants have no repayment outcomes. This is an irreducible sample-selection problem for any repayment analysis. The within-borrower panel further restricts to borrowers with multiple episodes, compounding selection concerns.
- If the determination rule causes some borrowers to not apply (those who predict unfavorable final terms), the sample of originated loans is truncated on expected final terms in a way that depends on the rule.

**Spillover:**
- The data card notes that borrowers may share offer information. Under the perturbation, information sharing is more consequential because borrowers can share not just their offers but also their understanding of the determination rule, potentially homogenizing strategic behavior across social networks.
- Staff treatment effects: if loan officers observe assigned terms and adjust their behavior, this creates an additional channel from terms to repayment that is neither selection nor borrower-level incentives.

**Implementation limits:**
- The packet does not guarantee that the term-determination rule is observed in the data. The perturbation says borrowers *are shown* the rule; it does not say the researcher has access to the rule's functional form or inputs.
- If the researcher cannot observe the rule, A6 cannot be satisfied, and the within-borrower panel is not defensible even for the incentive margin.

---

## 16. Failure Modes and Alternative Explanations

### Failure Mode 1: Unobserved Rule Inputs (Fatal for Within-Borrower Panel)
If the lender does not observe every characteristic that enters the term-determination rule, the within-borrower design fails. Episode-1 repayment that strategically improves an unobserved rule input will generate a spurious correlation between term changes and repayment changes. Alternative explanation: any estimated within-borrower effect reflects strategic repayment behavior rather than incentive effects.

### Failure Mode 2: Insufficient Repeat Borrowing (Fatal for Within-Borrower Panel)
If few borrowers have multiple accepted loans, the within-borrower panel has no identifying variation. Under the perturbation, repeat borrowing may be particularly rare because borrowers who receive unfavorable predicted final terms in episode 1 may not return. Alternative explanation: the few repeat borrowers are a highly selected group whose behavior does not generalize.

### Failure Mode 3: Differential Attrition Under the Perturbation
The perturbation may cause borrowers who predict unfavorable terms to not apply at all (Stage 2 attrition) or to not return for episode 2 (panel attrition). If attrition is correlated with unobserved repayment propensity and the determinants of attrition are not fully observed, the within-borrower sample is selected on unobservables in a way that fixed effects cannot address.

### Failure Mode 4: The Rule Is Continuous (RD Unavailable Regardless)
If the term-determination rule contains no discontinuities, RD is unavailable. This is not a consequence of the perturbation—it is a feature of the institutional setting that the packet leaves unspecified. The perturbation merely adds the anticipation channel that would break RD even if a discontinuity existed.

### Failure Mode 5: Strategic Behavior Changes the Meaning of All Estimates
The perturbation itself may alter borrower behavior in ways that make even the within-borrower incentive parameter uninterpretable for policy. If borrowers under the perturbed regime repay differently than they would under opacity (because they know repayment affects future terms), the estimated incentive effect is a parameter of the *perturbed* regime only and cannot be extrapolated to settings where borrowers lack this knowledge.

---

## 17. What Cannot Be Claimed

In light of the Stage 4 critique, the following claims are explicitly ruled out:

1. **Cannot claim that selection and incentive effects are separately identified.** No design available under the perturbation can credibly partition repayment differences into a selection component and an incentive component. The within-borrower panel nets out selection but cannot recover its magnitude, and the IV and RD designs that could, in principle, achieve separation are broken by the perturbation.

2. **Cannot claim that initial offer variation identifies the causal effect of realized terms on repayment.** The IV exclusion restriction is violated by a packet-documented mechanism: initial offers affect take-up composition through borrowers' expected final terms, creating a direct selection channel to repayment.

3. **Cannot claim that any discontinuity in the term-determination rule identifies a local causal effect.** The perturbation shows borrowers the rule before they apply, enabling anticipation-driven manipulation that violates RD continuity. This verdict is final; no packet-local evidence contradicts it.

4. **Cannot claim that the within-borrower incentive parameter generalizes to one-time borrowers or to a regime without the perturbation.** Repeat borrowers under the perturbed rule are a selected population whose behavior may differ from the broader borrower pool and from borrowers under opacity.

5. **Cannot claim that the perturbation leaves the base-packet identification unchanged or only "slightly weakened."** The perturbation is a structural change to the strategic environment that breaks two of the three candidate causal designs and substantially weakens the third. The Stage 4 critic's assessment—that the perturbation "fundamentally reconfigures" the environment—is correct and must be reflected in all claims.

6. **Cannot claim that observational associations between terms and repayment are "mostly" due to incentives or "mostly" due to selection.** The descriptive fallback estimates associations only. Under the perturbation, these associations reflect at least three unobserved channels (pure selection, pure incentives, strategic anticipation), and no decomposition among them is possible with the available data.

---

## 18. Additional Data Needed

To strengthen the within-borrower panel toward credible identification, or to restore the possibility of separate identification:

1. **Full documentation of the term-determination rule:** The exact functional form, all input variables, and any thresholds or discontinuities. Without this, the researcher cannot verify A6 (all rule inputs observed), and the within-borrower design cannot control for strategic cross-episode feedback.

2. **Data on the rule inputs at the time of each offer:** Even if rule inputs are observed at origination, they must also be observed at the time of the *initial offer* (before any strategic manipulation between the offer display and application) to distinguish genuine borrower characteristics from strategically altered ones.

3. **Pre-perturbation data (if the lender previously operated without showing the rule):** A historical sample where borrowers did not know the rule would allow comparison of the same design under opacity versus under the perturbation, revealing how much the perturbation alters selection, repayment, and repeat-borrowing patterns.

4. **Information-sharing or network data:** If borrowers share offer information or knowledge of the rule, individual-level data on social or geographic clusters would help assess the magnitude of spillover-driven strategic behavior.

5. **A randomized experiment:** The perturbation is fundamentally an information-treatment problem. If the lender could randomly assign some borrowers to a "no rule disclosure" condition while others see the rule, the difference between regimes would directly identify how knowledge of the rule alters take-up composition and repayment behavior.

---

## 19. Threat-Response Table

The task packet does not explicitly request a threat-response table. This section is omitted per the output contract instruction.

---

## 20. Claim-Evidence Table

| Claim | Evidence Used | Claim Type | Confidence | What Would Falsify This Claim |
|---|---|---|---|---|
| The perturbation breaks the IV exclusion restriction by creating a selection-composition channel from initial offers to repayment through expected final terms | Perturbation text: "borrowers are informed that the eventual contract terms may differ from the initial offer and are shown how those later terms can be determined"; data card confirming take-up is observable and precedes contract finalization | Design-assessment | High (packet-local) | Evidence that borrowers ignore the disclosed rule and make take-up decisions based solely on initial offer terms |
| The perturbation breaks RD continuity by enabling anticipation-driven sorting around any discontinuity in the known rule | Perturbation text establishing that borrowers see the rule before applying; standard RD no-manipulation condition | Design-assessment | High (analytic) | Evidence that the rule contains no discontinuity (making RD unavailable for separate reasons) or that borrowers cannot act on rule knowledge before applying |
| Within-borrower fixed effects eliminate time-invariant selection confounding | Panel structure in data card; within-borrower differencing is mathematically sufficient to remove any confound that does not vary across episodes for the same borrower | Causal (conditional) | Moderate (conditional on A2, A4, A6) | Pre-trend test shows that episode-1 repayment predicts direction of term change between episodes conditional on observed rule inputs |
| Within-borrower variation in realized terms is as-good-as-random conditional on FE and observed rule inputs | Assumption A2; not directly testable without full rule documentation | Causal (conditional) | Low (perturbation introduces strategic cross-episode behavior) | Balancing test on lagged outcomes shows systematic differences between borrowers whose terms improve versus worsen; significant coefficient movement when adding rule-input controls |
| Repeat borrowing is sufficiently common to support within-borrower estimation | Packet states borrowers "can have linked observations" but does not guarantee multiple episodes; data card lists "panel or repeated structure" | Descriptive | Unknown (packet-absent) | Empirical examination of data shows fewer than [threshold]% of borrowers have 2+ episodes, or within-borrower term variation is negligible |
| The incentive effect estimated on repeat borrowers generalizes to the broader borrower population | Assumption A5; no direct evidence in packet | Causal (conditional) | Low | Repeat borrowers differ systematically from one-time borrowers on pre-offer risk measures and episode-1 repayment, and these differences predict different treatment responses |
| The descriptive fallback measures valid conditional associations between terms and outcomes | All stages of the credit process are observable; baseline controls include pre-offer risk measures and operational indicators | Descriptive | High | Systematic measurement error in offer terms, realized terms, or repayment outcomes |
| Under the perturbation, no single design can credibly separate selection from incentive effects | IV and RD broken by packet-documented perturbation mechanisms; within-borrower panel estimates only incentive margin; review of all candidate designs | Design-assessment | High | Discovery of a packet-local source of identifying variation not considered in the candidate list that isolates the selection margin independently of the perturbation |

---

**Final assessment:** The perturbation is not a minor parameter change. It restructures the information environment in which borrowers make take-up, repayment, and re-borrowing decisions. The practical consequence is that any empirical analysis of this setting must either (a) settle for estimating the incentive margin alone under strong assumptions about observability of the determination rule and the availability of within-borrower variation, or (b) produce a descriptive mapping of associations with no causal attribution. The research objective of "separating selection from incentives" cannot be achieved with the data and variation described in the packet under the perturbed condition.