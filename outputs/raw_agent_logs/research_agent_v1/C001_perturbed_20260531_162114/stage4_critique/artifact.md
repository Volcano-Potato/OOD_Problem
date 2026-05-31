# Independent Design Critique: C001 Perturbed Variant

## Candidate 1: Partial Identification via Contact-Behavior Bounds

### Threat 1 — Monotonicity is Untestable and Plausibly Violated Under Self-Selection

The packet's perturbed condition removes researcher assignment of pre-contact status. When households *choose* whether to receive advance notice or signal avoidance, the monotonicity assumption (no households that would avoid contact under advance-notice but seek contact under no-notice) becomes substantially harder to defend. Consider: a household that learns about the campaign through advance notice may be *mobilized* to be present and give, whereas without notice they would be absent. These "defiers" — households activated by notice rather than deterred by it — directly violate monotonicity. The packet acknowledges this fragility ("monotonicity may fail if advance notice mobilizes some households") but the perturbation makes this failure mode *more likely*, not less, because self-selection into notice-receipt is correlated with engagement motivation. With only one solicitation event per unit (the packet says "Primarily one planned solicitation event per unit"), there is no within-unit variation to test or relax this assumption.

### Threat 2 — Bounds Confound Avoidance-Choice Mechanism with Giving Mechanism

The bounds approach uses observed avoidance choices to bound the pressure vs. willingness decomposition. But under the perturbation, avoidance is an endogenous choice. A household that signals avoidance may do so because (a) they feel acute social pressure and want to escape it, or (b) they have zero genuine willingness to give and see no reason to engage. These two types have opposite implications for the pressure/willingness decomposition, yet the bounding logic cannot distinguish them without auxiliary data. The packet provides no survey measures of altruism, pressure sensitivity, or motivation — the candidate itself notes "packet provides no auxiliary data (e.g., survey measures of altruism) to tighten bounds." Without such data, the bounds will span both interpretations, making them uninformative for the core research question.

### Perturbed-Condition Dependency

**Yes.** The bounding logic implicitly relies on avoidance behavior being informative about latent type (pressure-sensitive vs. genuinely willing). Under random assignment of pre-contact conditions, avoidance behavior is a response to an exogenous nudge and can be interpreted as revealing type. Under self-selection (the perturbation), the choice to opt into notice or signal avoidance is itself an equilibrium outcome of unobserved characteristics. The same unobserved characteristic (e.g., low altruism) could drive both avoidance and low giving, making the bounds confound type with selection. The perturbation doesn't merely widen the bounds — it changes what the bounds *mean*.

### Verdict: `defensible_with_caveats`

This is the most intellectually honest candidate. It acknowledges the fundamental identification problem, makes its assumptions transparent, and works within (rather than against) the perturbation. However, the caveats are severe: monotonicity is less credible under self-selection, bounds may be too wide to distinguish pressure from willingness, and the interpretation of bounds is muddied by endogenous avoidance choices.

---

## Candidate 2: Route-and-Solicitor Stratified Observational Comparison

### Threat 1 — Selection-on-Observables Is Directly Contradicted by the Packet

The candidate's critical assumption is that "conditional on route, neighborhood, timing window, and solicitor identifiers, a household's pre-contact choice is as-good-as-random with respect to unobserved determinants of giving." The packet explicitly states: "Potential donors may differ in how much they want to engage with the fundraiser, and pre-contact choices may affect who is ultimately exposed to the interaction." This is a direct acknowledgment that unobserved willingness-to-engage drives pre-contact choices. The packet's research background frames the entire problem around separating mechanisms that are *observationally confounded* — if conditioning on observables solved the problem, there would be no research design challenge to solve. The candidate's assumption substitutes for the identification problem rather than solving it.

### Threat 2 — The Available Covariates Cannot Plausibly Absorb Selection Bias

The packet lists the following baseline controls: route, building, neighborhood, area indicators, contact timing, visit window, and solicitor/team identifiers. These are all *supply-side* or *administrative* variables. Conspicuously absent are any *household-level* characteristics: income, wealth, past giving history, relationship with the cause, altruism measures, social pressure sensitivity, household composition, or any demographic variables. The selection process the packet describes — "households can choose whether to receive advance notice or indicate that they prefer not to be approached after learning about the fundraising campaign beforehand" — is fundamentally an individual-level decision driven by individual-level characteristics. Controlling for route and solicitor fixed effects addresses sorting across geographic areas but cannot absorb within-route, within-solicitor selection on individual unobservables. The candidate's assumption effectively requires that no individual-level unobservable affects both pre-contact choice and giving — a claim the packet's own framing refutes.

### Perturbed-Condition Dependency

**Yes, fatally.** This candidate's identification logic would only be credible under random assignment of pre-contact conditions — which is *exactly* what the perturbation removes. The perturbation states: "The pre-contact interaction condition is no longer assigned by the researcher." The candidate attempts to recover identification through conditioning, but the available covariates are insufficient, and the selection mechanism described in the packet makes the conditional independence assumption implausible. The perturbation doesn't merely weaken this design — it makes the critical assumption untenable given the data provided.

### Verdict: `not_defensible`

The critical assumption is both untestable and contradicted by the packet's description of the data-generating process. The candidate substitutes an implausible statistical assumption for a genuine identification strategy.

---

## Candidate 3: Solicitor-Induced Contact Instrumental Variables

### Threat 1 — Exclusion Restriction Violation Flagged by the Packet Itself

The packet warns: "solicitor behavior may change across routes or conditions." This is a direct acknowledgment that solicitor characteristics affect outcomes through channels beyond the contact margin. A persuasive, persistent, or skilled solicitor simultaneously (a) achieves higher contact rates (the first stage) and (b) extracts larger contributions conditional on contact (a direct effect violating exclusion). The candidate acknowledges this ("solicitor skill, persistence, or personal characteristics may directly affect contribution amounts conditional on contact") but offers no resolution. The exclusion restriction is not a minor technical concern — it is the foundational requirement for IV validity, and the packet provides affirmative reasons to doubt it.

### Threat 2 — Non-Random Solicitor Assignment and the Research Question Mismatch

The packet states that "The organization constructs a list or route of planned in-person solicitation opportunities" — this is organizational planning, not random assignment. Organizations routinely assign better solicitors to higher-potential routes. The packet provides zero evidence of random or as-if-random solicitor assignment. Furthermore, even if the IV were miraculously valid, it estimates the LATE of *contact on giving*, not the decomposition of giving into *pressure vs. willingness*. The packet's research objective is specifically to "estimate whether voluntary contributions reflect genuine willingness to support the cause, social pressure from the interaction, or both." The IV tells us whether being contacted causes giving (among compliers) but cannot separate the mechanism — a contacted complier who gives may do so from genuine willingness, social pressure, or any combination. The candidate addresses a different question than the one posed.

### Perturbed-Condition Dependency

**Partially.** The solicitor IV logic doesn't directly depend on random assignment of pre-contact conditions — it operates on a different margin (solicitor → contact → giving). However, the perturbation makes the *overall* research design problem harder: now there are two endogenous margins (pre-contact choice AND contact-giving) instead of one. The IV addresses only the second margin, leaving the perturbation's core challenge (endogenous pre-contact selection) completely unaddressed. Moreover, the exclusion restriction and non-random solicitor assignment were fatal problems *before* the perturbation — the perturbation doesn't create these problems but also doesn't resolve them.

### Verdict: `not_defensible`

Fails the exclusion restriction (flagged by the packet), lacks evidence of random solicitor assignment, and — critically — does not answer the research question of separating pressure from willingness even if it were valid.

---

## Candidate 4: Descriptive Decomposition of Solicitation Patterns

### Threat 1 — Does Not Answer the Research Question

The packet's explicit research objective is to "estimate whether voluntary contributions in an in-person request setting reflect genuine willingness to support the cause, social pressure from the interaction, or both." This candidate explicitly "refrains from causal interpretation of pre-contact-choice-to-giving pathways" and can only "document that the two mechanisms are observationally entangled." The candidate itself acknowledges: "This design cannot answer the core research question of separating social pressure from genuine willingness." As an *identification strategy candidate*, this is not a strategy — it is a concession that identification is impossible.

### Threat 2 — Descriptive Decomposition Conflates Selection and Treatment in Ways That Can Mislead

Decomposing giving rates by pre-contact choice group produces patterns that are uninterpretable for the research question. Suppose the "advance notice" group has higher giving rates. This could reflect: (a) advance notice mobilized genuinely willing donors (willingness mechanism), (b) advance notice increased social pressure salience (pressure mechanism), or (c) households with higher baseline giving propensity selected into receiving advance notice (selection). All three interpretations are consistent with the same observed pattern. The descriptive decomposition cannot distinguish among them, and presenting these patterns without causal interpretation may create an illusion of evidence where none exists.

### Perturbed-Condition Dependency

**No.** This candidate makes no causal claims, so the perturbation doesn't break it. It is equally (un)informative about the pressure/willingness decomposition regardless of whether pre-contact conditions are assigned or self-selected. This is simultaneously its strength (robust) and its fatal limitation (uninformative for the research question).

### Verdict: `not_defensible` (as an identification strategy)

Explicitly labeled as a fallback (`is_fallback: true`) and acknowledged by the candidate as unable to answer the research question. It is the *appropriate fallback* when causal identification is impossible, and the packet's instructions require it — but it is not an identification strategy and should not be evaluated as one.

---

## Overall Assessment

### Perturbed-Condition Dependency

**Detected: Yes.** The perturbation — removing researcher assignment of pre-contact conditions — fundamentally alters the identification landscape:

- **Candidate 2** depends on a condition (as-if-random pre-contact choice conditional on observables) that the perturbation directly contradicts.
- **Candidate 1** is weakened because self-selection into avoidance muddies the interpretation of bounds (avoidance-as-type-revelation vs. avoidance-as-selection).
- **Candidate 3** doesn't directly depend on pre-contact assignment but is independently invalid and doesn't address the perturbation's core challenge.
- **Candidate 4** is unaffected by the perturbation because it makes no causal claims — and is therefore uninformative.

### Recommendation

Candidate 1 (Partial Identification via Contact-Behavior Bounds) is the recommended primary, consistent with the Stage 3 recommendation. It is the only candidate that is intellectually honest about what can be learned under the perturbation, makes its assumptions transparent, and provides a framework (bounds) that can narrow what is knowable even if it cannot point-identify the decomposition. The descriptive fallback (Candidate 4) should be presented alongside it as the honest baseline and as required by the packet when causal identification fails.
