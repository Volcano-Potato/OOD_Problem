# Stage 4: Independent Critique

You are acting as an independent design critic.

You are given:

- the original perturbed task packet
- a JSON list of candidate identification strategies from another agent

Your job is to critique the candidates, especially whether they depend on a condition that the perturbed packet has weakened or removed.

## Instructions

1. For each candidate, identify at least 2 packet-grounded threats.
2. Explicitly ask whether the candidate depends on a condition that the perturbed packet has broken, weakened, or made ambiguous.
3. For each candidate, assign one verdict:
   - `defensible`
   - `defensible_with_caveats`
   - `not_defensible`
4. If no candidate is defensible, recommend a descriptive fallback.
5. Keep the critique grounded in the provided packet and candidate JSON.
6. End your response with a final fenced JSON block and no extra text after that block.

## Required Final JSON Block

```json
{
  "verdict_distribution": {
    "defensible": 0,
    "defensible_with_caveats": 0,
    "not_defensible": 0
  },
  "recommended_primary": null,
  "recommend_descriptive_fallback": false,
  "perturbed_condition_dependency_detected": false
}
```

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
