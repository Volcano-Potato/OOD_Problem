# Stage 5: Final Design Memo

You are writing the final memo after reviewing:

- the original perturbed task packet
- the Stage 3 candidate list
- the Stage 4 independent critique

Your output must follow the existing evidence-aware benchmark report structure.

## Required Reconciliation Rule

You must reconcile the Stage 4 critic verdict.

- If the critic marks a candidate `not_defensible`, do not present it as a credibly identified causal design unless you explicitly point to packet-local evidence that the critic missed.
- If the critic recommends a descriptive fallback, you must either adopt that downgrade or explain, with packet-local evidence, why a stronger design is still defensible.
- In section 17, explicitly state what cannot be claimed in light of the critique.

## Required Output Contract

Follow this structure exactly:

1. Executive summary
2. Research question
3. Target estimand or strongest defensible estimand
4. Treatment or exposure and main outcomes
5. Data structure summary
6. Relevant causal mechanisms
7. Main identification challenge
8. Whether credible causal identification is possible
9. Proposed empirical design or strongest defensible descriptive analysis
10. Why the design is valid or why causal identification is not credible
11. Required assumptions
12. Statistical model or analysis equation
13. Robustness, placebo, falsification checks, or diagnostic tests
14. Heterogeneity analysis if supportable
15. Measurement, compliance, missingness, spillover, or implementation limits
16. Failure modes and alternative explanations
17. What cannot be claimed
18. Additional data needed
19. Threat-response table if explicitly requested by the task packet
20. Claim-evidence table

Use the canonical claim-evidence table header:

| Claim | Evidence Used | Claim Type | Confidence | What Would Falsify This Claim |
|---|---|---|---|---|

## Original Packet

<!-- visibility: agent-facing -->
<!-- case_id: C002 -->
<!-- variant: perturbed -->

# Anonymous Research Design Task: Perturbed Variant

## Task Rule

Use the information provided below to design a rigorous empirical strategy for this anonymized applied business/economics research problem. Your goal is to produce a defensible research design, not to write a literature review.

Do not assume that a known paper has already solved the task. Ground your reasoning in the background, data description, institutional details, and constraints provided in this packet.

Do not fill in packet-absent operational details, institutional features, or named design devices as if they were known facts. If multiple concrete implementations fit the packet, describe them generically or label them explicitly as illustrative examples rather than assumptions.

If credible causal identification is not possible from the provided information, do not invent an identification strategy. State the strongest defensible descriptive or correlational analysis instead.

## Research Background

A consumer lender wants to understand why borrowers with different loan terms show different repayment outcomes. Repayment differences may reflect who chooses to borrow under different offer terms, or they may reflect how realized loan terms and later incentives change behavior after borrowing.

The research problem is to design a credit-market study that separates these explanations rather than estimating a single reduced-form price effect on default.

## Research Setting

The lender makes offers to prospective borrowers, observes who responds or accepts, finalizes a contract, and later tracks repayment. Some terms are visible before application or take-up, while other terms or incentives may arise only after the borrower has already entered the borrowing relationship.

## Research Objective

Design a study to estimate whether repayment outcomes in a consumer-credit setting are driven by borrower selection at take-up, incentive effects after borrowing, or both.

## Specific Questions To Answer

1. Which design can estimate how pre-borrowing terms affect take-up and borrower composition?
2. How can the study separate borrower selection from post-borrowing incentives?
3. What happens to that separation if borrowers already know how later contract terms can change before they apply?
4. Which repayment comparisons remain credible, and which become confounded?

## Data Structure Overview

- Stage 1: Eligible prospective borrowers receive loan offers with observable pre-borrowing terms.
- Stage 2: Before deciding whether to apply, borrowers are informed that final contract terms may differ from the initial offer and are shown how later terms can be determined.
- Stage 3: Accepted borrowers receive finalized contract terms and enter repayment.
- Stage 4: The lender observes repayment outcomes and may also vary or observe future-credit consequences tied to repayment behavior.

## Data Card

| field | description |
|---|---|
| unit of observation | Prospective borrower offer, application, accepted loan, and repayment record. |
| time span | Sequential credit process: offer stage, application or acceptance stage, contract finalization stage, repayment period, and possible future-borrowing period. |
| sample construction | Prospective borrowers receive loan offers. Accepted loans are followed through repayment. Non-applicants remain observable for take-up but not repayment outcomes. |
| treatment or exposure variable | Loan terms and incentives that can vary at different stages, including terms shown before application, terms finalized after acceptance, and future-access or pricing incentives tied to repayment behavior. |
| outcome variable | Application or take-up, repayment status, delinquency or default, and future borrowing eligibility or terms. |
| secondary outcomes | Intermediate repayment behavior and accepted loan amount if observed. |
| assignment or variation source | The lender still varies initial offer terms and later contract terms, but borrowers are informed before application that later terms may differ from the initial offer. |
| assignment level | Borrower-offer level for initial terms; later terms may still vary at borrower-loan level after acceptance. |
| outcome measurement level | Borrower-loan repayment record. |
| panel or repeated structure | Borrowers can have linked observations across offer, acceptance, repayment, and future-borrowing stages. |
| compliance or take-up | Not all offered borrowers apply or accept; later incentive variation may matter only within originated loans. |
| spillover or interference | Borrowers may share offer information; staff may treat borrowers differently if they observe assigned terms. |

## Variable Groups

### Treatment Or Exposure Variables

- Pre-borrowing offer terms.
- Realized contract terms.
- Future access or repayment-linked incentive terms.

### Selection Or Sample-Flow Variables

- Offer receipt.
- Application or take-up.
- Acceptance and loan origination.

### Main Outcome Variables

- Take-up.
- Repayment, delinquency, or default.

### Secondary Outcome Variables

- Loan amount if relevant.
- Intermediate repayment behavior.

### Baseline Controls And Design Variables

- Pre-offer borrower risk measures.
- Prior credit history or lender-side information.
- Offer wave, branch, or operational batch indicators.

## Perturbed Condition

Before deciding whether to apply, borrowers are informed that the eventual contract terms may differ from the initial offer and are shown how those later terms can be determined.

## Known Constraints

- The business setting and most of the data structure are intentionally similar to the base task.
- One key identification condition has changed.
- The answer must explain whether the original design logic still works, becomes weaker, or fails.
- If strong causal identification is no longer justified, the answer must explicitly downgrade the claim or propose additional design changes.

## Required Output

1. Executive summary
2. Research question
3. Target estimand or strongest defensible estimand
4. Treatment or exposure and main outcomes
5. Data structure summary
6. Relevant causal mechanisms
7. Main identification challenge
8. Whether credible causal identification is possible
9. Proposed empirical design or strongest defensible descriptive analysis
10. Why the design is valid or why causal identification is not credible
11. Required assumptions
12. Statistical model or analysis equation
13. Robustness, placebo, falsification checks, or diagnostic tests
14. Heterogeneity analysis if supportable
15. Measurement, compliance, missingness, spillover, or implementation limits
16. Failure modes and alternative explanations
17. What cannot be claimed
18. Additional data needed
19. Threat-response table if explicitly requested by the task packet
20. Claim-evidence table

## Claim-Evidence Table

| Claim | Evidence Used | Claim Type | Confidence | What Would Falsify This Claim |
|---|---|---|---|---|


## Stage 3 Candidate JSON

```json
{
  "candidates": [
    {
      "name": "within_borrower_panel",
      "estimand": "Average effect of realized contract terms on repayment, identified off within-borrower variation in realized terms across repeated borrowing episodes, net of time-invariant borrower unobserved heterogeneity.",
      "identifying_variation": "Within-borrower variation in realized contract terms across two or more accepted loans for the same borrower observed over the panel (offer → acceptance → repayment → future borrowing).",
      "critical_assumption": "Within-borrower changes in realized contract terms are as-good-as-random conditional on borrower fixed effects and time-varying observables (no time-varying unobserved confounders that drive both term assignment and repayment).",
      "packet_support": "Data card notes 'Borrowers can have linked observations across offer, acceptance, repayment, and future-borrowing stages' and lists 'panel or repeated structure'. The lender also 'may vary or observe future-credit consequences tied to repayment behavior,' which can generate within-borrower term variation.",
      "fragility": "Repeated borrowing may be sparse or highly selected (borrowers with multiple loans differ systematically from one-time borrowers). Within-borrower term variation may be too limited for precise estimation if terms are sticky. Time-varying confounders (e.g., changing creditworthiness, life events) may correlate with both term changes and repayment. The perturbation—borrowers knowing terms can change—may itself alter within-borrower behavior across episodes in ways not captured by fixed effects.",
      "is_fallback": false
    },
    {
      "name": "rd_term_determination_rule",
      "estimand": "Local average treatment effect of a discrete change in realized contract terms on repayment at the threshold of the term-determination rule that borrowers are shown before application.",
      "identifying_variation": "Discontinuous jump in realized contract terms at a cutoff in the observable rule (e.g., credit-score threshold, debt-to-income cutoff) that the lender shows borrowers before they apply.",
      "critical_assumption": "The term-determination rule contains at least one sharp discontinuity in a continuous running variable; borrowers cannot precisely manipulate the running variable at the threshold; and any anticipation-driven selection is smooth through the cutoff (or can be handled by donut-RD).",
      "packet_support": "The perturbed condition states that 'borrowers are informed that the eventual contract terms may differ from the initial offer and are shown how those later terms can be determined.' This implies an observable, rule-based mapping from borrower characteristics to final terms. If that rule is discontinuous, RD becomes available.",
      "fragility": "The perturbation is the fragility: because borrowers are shown the rule before applying, they can anticipate the discontinuity and select around it (e.g., borrowers just below a favorable cutoff may not apply at all, or may manipulate the running variable). Standard RD validity requires no manipulation of the running variable, which anticipation directly threatens. A donut-RD discarding observations near the cutoff may help but reduces power and changes the estimand. The rule may not contain a discontinuous element—it may be smooth, in which case RD is unavailable.",
      "is_fallback": false
    },
    {
      "name": "iv_initial_offer_weakened",
      "estimand": "Local average treatment effect of realized contract terms on repayment for compliers whose realized terms shift with the initial offer, under an exclusion restriction that is explicitly threatened by the perturbation.",
      "identifying_variation": "Exogenous or quasi-random variation in initial offer terms (e.g., from offer-wave or operational-batch indicators) used as an instrument for realized contract terms.",
      "critical_assumption": "Initial offer terms affect repayment only through their effect on realized contract terms (exclusion restriction). Under the perturbation, this requires that borrowers' anticipation of term changes does not create a separate selection channel connecting initial offers to repayment through the composition of who takes up the loan.",
      "packet_support": "Data card lists 'Offer wave, branch, or operational batch indicators' as baseline controls, and the lender 'varies initial offer terms.' The two-stage structure (offer → acceptance → repayment) is the natural setting for an IV design.",
      "fragility": "The perturbation directly threatens the exclusion restriction: borrowers are told before applying that final terms may differ and are shown how they are determined. This means initial offer terms influence not just realized terms but also take-up composition (who selects into borrowing), because borrowers make take-up decisions based on their expected final terms, which are a function of both the initial offer and the known determination rule. This selection channel means initial offers affect repayment through borrower composition, violating the exclusion restriction. Even with randomly assigned initial offers, the IV estimand confounds incentive effects with selection composition.",
      "is_fallback": false
    },
    {
      "name": "descriptive_selection_incentive_decomposition",
      "estimand": "Conditional associations: (i) between initial offer terms and take-up/composition, and (ii) between realized contract terms and repayment, controlling for observed borrower characteristics. No causal claim attempted.",
      "identifying_variation": "Observed cross-sectional covariation in initial offer terms, realized contract terms, take-up decisions, and repayment outcomes across the full borrower-offer sample.",
      "critical_assumption": "No causal identifying assumption is asserted. The analysis is descriptive and conditions only on observables; residual unobserved heterogeneity is acknowledged as a confound.",
      "packet_support": "All stages of the credit process are observable in the data: offer terms, take-up decisions, realized contract terms, and repayment outcomes. Baseline controls include pre-offer risk measures, prior credit history, and operational indicators. The perturbation makes causal separation difficult but does not prevent rich description of the empirical patterns.",
      "fragility": "Cannot answer the core research question (separating selection from incentives). Any observed difference in repayment across borrowers with different realized terms may be driven by unobserved borrower type rather than incentive effects. Similarly, differences in take-up across initial offers may reflect unobserved borrower characteristics correlated with both take-up propensity and repayment risk. The analysis can describe patterns and generate hypotheses but cannot attribute repayment differences to selection versus incentives.",
      "is_fallback": true
    }
  ],
  "recommended_primary": "within_borrower_panel",
  "notes": "The perturbation—borrowers are informed before application that final contract terms may differ from the initial offer and are shown the determination rule—fundamentally compromises any design that relies on initial-offer variation to separately identify selection and incentive effects. Because borrowers anticipate final terms and incorporate that anticipation into their take-up decision, initial offers no longer isolate pure selection. The within-borrower panel design is recommended as the strongest remaining causal strategy because it differences out time-invariant borrower selection directly, though it identifies only the incentive margin and requires sufficient within-borrower term variation. The RD design on the term-determination rule is a close second but is fragile to anticipation-driven manipulation. The IV design is included to illustrate exactly what the perturbation breaks. If within-borrower variation is insufficient, the descriptive decomposition is the only defensible fallback."
}
```

## Stage 4 Critique

# Independent Critique: Stage 4

## Candidate 1: `within_borrower_panel`

### Threat 1 — Strategic cross-episode behavior induced by the perturbation
The perturbation states that borrowers are "informed that the eventual contract terms may differ from the initial offer and are shown how those later terms can be determined." This means a borrower who receives unfavorable realized terms in episode 1 and repays strategically to improve their measured characteristics (inputs to the known determination rule) will experience a term change in episode 2 that is endogenous to their own episode-1 repayment behavior. The within-borrower change in terms is then driven partly by strategic repayment, which is the same outcome the design aims to study. This creates a direct reverse-causality channel that borrower fixed effects cannot eliminate because it operates *within* borrower and *across* time.

### Threat 2 — Repeated borrowing is permissive, not guaranteed, and selected on observables that shift with the rule
The data card says "Borrowers *can* have linked observations across offer, acceptance, repayment, and future-borrowing stages" (emphasis added). This is a possibility, not a structural guarantee. The packet never states that borrowers routinely take multiple loans. Borrowers who return for a second loan under a known term-determination rule are a selected subsample: those whose characteristics, shaped in part by episode-1 repayment under the known rule, still qualify them for episode-2 borrowing. The within-borrower estimand is identified off a selected population whose selection itself is altered by the perturbation. The sample of repeat borrowers under the perturbed regime differs systematically from repeat borrowers under opacity, and the design offers no way to recover the unperturbed parameter.

### Perturbation-dependency question
Does this candidate depend on the condition—removed or weakened by the perturbation—that borrowers do not incorporate knowledge of the term-determination rule into their repayment and re-borrowing decisions across episodes? **Yes, it does.** The perturbation gives borrowers a roadmap linking their behavior to future terms, which transforms within-borrower term variation from something potentially quasi-random into something endogenously produced by the borrower's own strategic choices. The critical assumption of no time-varying unobserved confounders is substantially weakened because the perturbation itself creates a mechanism through which repayment behavior (the outcome) feeds into future term assignment (the treatment).

### Verdict
`defensible_with_caveats`

The design retains the ability to net out time-invariant borrower heterogeneity, which remains valuable. However, the perturbation introduces a credible channel for time-varying unobserved confounding (strategic cross-episode behavior) that the fixed-effects structure cannot address. The design works only if the lender can fully observe and condition on every input to the term-determination rule that a borrower could manipulate, and only if repeat borrowing is sufficiently common and not differentially selected under the perturbation. Both conditions are unverified in the packet.

---

## Candidate 2: `rd_term_determination_rule`

### Threat 1 — Anticipation-driven manipulation of the running variable at the cutoff
The perturbation states that borrowers are "shown how those later terms can be determined" *before* they apply. If the determination rule contains a discontinuity, borrowers can see it. A borrower whose running variable falls just below a favorable cutoff has a strong incentive to either (a) manipulate the running variable to cross the threshold (e.g., pay down a small debt to nudge a credit score over the cutoff) or (b) self-select out of the applicant pool entirely if they cannot cross it. Both behaviors violate the continuity assumption that underlies RD identification. This is not a hypothetical fragility—it is a direct and inevitable consequence of the perturbation, because the perturbation *is* the act of showing borrowers the rule ex ante.

### Threat 2 — No packet evidence that a discontinuous rule exists
The perturbation says borrowers are "shown how those later terms can be determined." The word "how" does not imply a discontinuous function. The rule could be a continuous formula (e.g., term = α + β·credit_score), a set of graduated risk tiers with smooth transitions, or a multivariate underwriting model without sharp cutoffs. The candidate *assumes* a discontinuity exists, but the packet provides no support for this assumption. If the rule is continuous everywhere, RD is unavailable regardless of the perturbation. The candidate therefore rests on an extra-packet premise.

### Perturbation-dependency question
Does this candidate depend on the condition—removed by the perturbation—that borrowers cannot anticipate or manipulate the assignment rule before applying? **Yes, fatally.** Standard RD validity requires that agents cannot precisely control the running variable at the threshold. The perturbation explicitly grants borrowers both knowledge of the rule and the opportunity to act on that knowledge before applying. This is a textbook violation of the no-manipulation condition. The donut-RD remedy does not restore the original identifying variation; it estimates a different LATE further from the cutoff where selection pressures from the known rule may operate in unknown ways, and where the first-stage discontinuity no longer drives assignment.

### Verdict
`not_defensible`

The perturbation directly and irreparably breaks the core identifying assumption of RD. The candidate's own fragility section acknowledges this. Without evidence that a discontinuity exists in the first place (absent from the packet) and without any way to prevent anticipation-driven sorting (which the perturbation guarantees), the design cannot credibly identify a causal effect.

---

## Candidate 3: `iv_initial_offer_weakened`

### Threat 1 — Exclusion restriction violated through selection composition
Under the perturbation, borrowers know before applying that final terms may differ from initial offers and know how final terms are determined. A borrower's take-up decision therefore depends on their *expected* final terms, which are a function of both the initial offer and the known determination rule applied to their own characteristics. Variation in initial offers now affects *who* takes up the loan, not just what terms they receive. This creates a direct path from initial offers to repayment outcomes through borrower composition (initial offer → selection into borrowing → repayment) that does not operate through realized contract terms. This is a violation of the exclusion restriction: the instrument affects the outcome through a channel other than the endogenous variable.

### Threat 2 — Complier population is unstable and uninterpretable under the perturbation
Even if initial offers are randomly assigned across offer waves or batches, the IV estimand recovers a LATE for compliers—borrowers whose realized terms shift with the initial offer. Under the perturbation, the complier group is defined by a two-stage selection process: first, whether a borrower applies given their expected final terms (which incorporate the known rule), and second, whether realized terms then shift with the initial offer. This complier population is not the same as the complier population under opacity. Because the perturbation fundamentally changes the take-up decision, the IV identifies an effect for a group whose composition and behavior cannot be mapped to any policy-relevant population under either the base or perturbed regime.

### Perturbation-dependency question
Does this candidate depend on the condition—broken by the perturbation—that initial offers affect repayment *only* through realized contract terms? **Yes, and the candidate itself concedes this.** Under the base packet (without the perturbation), an IV design using randomly assigned initial offers would face standard exclusion concerns but could be defended. The perturbation adds an explicit, packet-grounded channel through which initial offers shape borrower composition, because borrowers now use initial offers *plus* the known rule to form expectations about final terms and decide whether to apply. The exclusion restriction is not merely "threatened" or "weakened"—it is broken by a mechanism described in the perturbation itself.

### Verdict
`not_defensible`

The perturbation introduces a packet-documented selection channel that violates the exclusion restriction. The candidate's own name ("iv_initial_offer_weakened") and analysis acknowledge this. No amount of quasi-random assignment of initial offers can restore the exclusion restriction when the perturbation guarantees that initial offers affect take-up composition through borrowers' expectations of final terms. This design is included in the candidate list as an illustration of what the perturbation breaks, and the verdict confirms that assessment.

---

## Candidate 4: `descriptive_selection_incentive_decomposition`

### Threat 1 — Cannot address the core research objective
The research objective is to "separate" selection from incentives. The descriptive approach explicitly does not attempt causal separation. It estimates conditional associations and acknowledges that "any observed difference in repayment across borrowers with different realized terms may be driven by unobserved borrower type rather than incentive effects." The packet states: "If credible causal identification is not possible from the provided information, do not invent an identification strategy. State the strongest defensible descriptive or correlational analysis instead." The descriptive candidate follows this instruction faithfully, but it does not—and cannot—answer the research question. It is a valid response to *failure*, not a strategy that succeeds.

### Threat 2 — Perturbation degrades even the descriptive interpretability of associations
Under the perturbation, borrowers anticipate final terms and incorporate them into take-up decisions. The observed association between realized terms and repayment now reflects three channels: (i) incentive effects of terms on repayment, (ii) selection of borrower types into different terms (which exists under the base packet), and (iii) a new perturbation-specific channel where borrowers' knowledge of the rule alters both *who* takes up which loan and *how* they repay, in ways correlated with the observed term variation. The descriptive decomposition can document patterns but cannot even informally attribute them to any single channel, because the perturbation multiplies the number of unobserved pathways linking terms to outcomes.

### Perturbation-dependency question
Does this candidate depend on a condition that the perturbation has broken, weakened, or made ambiguous? **No.** The descriptive candidate makes no causal identifying assumptions that the perturbation could break. It conditions only on observables and acknowledges unobserved confounding. The perturbation does not prevent the measurement of associations between offer terms, take-up, realized terms, and repayment. It does, however, make those associations *less informative* about underlying mechanisms, because the perturbation adds an additional layer of strategic behavior that is not separately observable.

### Verdict
`defensible`

The candidate is defensible as a descriptive fallback. It does not claim causal identification, it acknowledges unobserved confounding, and it follows the packet's explicit instruction to state "the strongest defensible descriptive or correlational analysis" when causal identification is not credible. The perturbation does not break descriptive measurement. However, the packet should be clear that this approach does not "separate selection from incentives"—it maps the empirical landscape of associations that could be consistent with many different mixtures of selection and incentive effects.

---

## Summary Assessment

The perturbation—showing borrowers the term-determination rule before they apply—is not a minor variation. It fundamentally reconfigures the strategic environment. Borrowers are no longer passive recipients of terms; they are active agents who incorporate their knowledge of the rule into take-up, repayment, and re-borrowing decisions. This single change:

- **Breaks** the IV exclusion restriction (candidate 3) by creating a selection-composition channel from initial offers to repayment.
- **Breaks** RD continuity (candidate 2) by enabling anticipation-driven sorting around any discontinuity.
- **Weakens** the within-borrower panel (candidate 1) by introducing strategic cross-episode behavior that creates time-varying unobserved confounding.
- **Leaves** the descriptive fallback (candidate 4) untouched in measurement terms, though even descriptive patterns become harder to interpret.

The within-borrower panel remains the strongest causal candidate because it directly differences out time-invariant selection—the core confound the research question targets—and the perturbation's threat to it, while real, can be mitigated if the lender observes all inputs to the determination rule and repeat borrowing is sufficient. However, the perturbation eliminates any design that could *separately* identify selection and incentive effects in a single step, because it fuses the two channels at the take-up stage.

