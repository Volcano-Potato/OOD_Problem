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
