## Independent Critique

### Candidate 1: Descriptive Stratification by Pre-Contact Choice × Contact Status

**Threat 1 — Double selection confound.** The four-way stratification (opted-for-notice × contacted status) embeds two layers of endogenous selection. The packet states that "Potential donors may differ in how much they want to engage with the fundraiser, and pre-contact choices may affect who is ultimately exposed to the interaction." Households that seek advance notice are likely more engaged with the cause; among those who did not seek notice, who is contacted depends on availability and absence patterns. Neither dimension is random, so group mean differences conflate engagement propensity, availability, and any causal effects.

**Threat 2 — No basis for decomposition.** The packet's core objective is to "separate these explanations" (genuine willingness vs. social pressure). Descriptive stratification across self-selected groups cannot separate these mechanisms. A contacted household that opted for notice and gives could be acting from willingness, pressure, or both; the design provides no leverage to decompose these components, and the stratification offers no test that would falsify one mechanism over another.

**Condition dependency?** No. This candidate explicitly disclaims causal identification and operates entirely within the perturbation's constraints. It does not depend on researcher assignment of the pre-contact condition because it makes no causal claims requiring such assignment.

**Verdict:** `defensible` — as a descriptive fallback. The packet instructs that if "strong causal identification is no longer justified, the answer must explicitly downgrade the claim," and this candidate does exactly that.

---

### Candidate 2: Instrumental Variables Using Solicitor Identity and Visit Timing

**Threat 1 — Exclusion restriction is implausible and untestable.** The IV requires that solicitor identity and visit timing affect contribution outcomes *only* through contact probability. But the packet warns that "solicitor behavior may change across routes or conditions." Solicitors differ in persuasiveness, persistence, ask amounts, and interpersonal skills — all of which plausibly affect giving *conditional on contact*, violating the exclusion restriction. The packet provides no evidence, protocol, or institutional detail suggesting solicitors follow standardized scripts that would support the restriction.

**Threat 2 — No assignment mechanism for the instrument.** The packet describes Stage 1 as: "The organization constructs a list or route of planned in-person solicitation opportunities." It says nothing about random or quasi-random assignment of solicitors to routes. Organizations facing fundraising goals have strong incentives to assign experienced solicitors to higher-potential areas. The packet provides route/neighborhood/timing controls but no evidence that solicitor assignment is orthogonal to area characteristics — and the burden of establishing quasi-random assignment falls on the researcher, not on the absence of contradictory evidence.

**Additional fragility:** Even if the instrument were valid for contact, it does not address the perturbation's core challenge. The IV estimates the effect of *contact* on giving (among compliers), not the effect of *pre-contact conditions* (advance notice vs. avoidance signal) on giving. The packet asks the design to distinguish pressure from willingness in the context of pre-contact choices; an IV for contact does not decompose these mechanisms under self-selected pre-contact conditions.

**Condition dependency?** Yes, indirectly. The IV strategy depends on the existence of quasi-random variation in solicitor assignment or timing — a condition the packet never establishes but that becomes more fragile precisely because the perturbation removes researcher control over the primary treatment. When the researcher cannot assign the key treatment, relying on an unverified secondary source of variation that the packet does not describe as randomized is not defensible.

**Verdict:** `not_defensible`

---

### Candidate 3: Revealed-Preference Bounding with Avoidance Signals

**Threat 1 — Avoidance signal truthfulness is a strong, untestable behavioral assumption.** The packet states that households "can choose whether to receive advance notice or indicate that they prefer not to be approached after hearing about the fundraising campaign beforehand." The perturbation makes this choice unconstrained and unobserved in its motivation. A household might signal avoidance because it is busy at the scheduled time, because it prefers to donate online through a different channel, or because it has a policy of never answering the door — not because it is susceptible to social pressure. Attributing contributions from contacted avoiders to "pressure" requires that the avoidance signal cleanly reflects pressure sensitivity, which the packet provides no basis to assert.

**Threat 2 — The contacted-avoider subpopulation may be trivially small or non-representative.** The packet notes that "pre-contact choices may affect who is ultimately exposed to the interaction" and that "Some households may be absent, unreachable, or inconsistent between stated preferences and realized contact." If avoidance signals translate into effective avoidance (e.g., households that signal avoidance are not home or refuse to answer), the "contacted avoiders" group shrinks toward zero. Even if some avoiders are contacted, they may be a selected subset (e.g., those who were less determined to avoid, or those the solicitor pursued more aggressively), introducing additional selection bias into the lower bound.

**Threat 3 — Bounds may be uninformatively wide.** The packet provides no information about expected subgroup sizes, variance in contribution behavior, or the strength of the avoidance signal's correlation with giving. Without such information, the bounds could span nearly the entire range of possible contribution probabilities, making them substantively vacuous even if formally valid.

**Condition dependency?** Partially. The bounding strategy does not depend on random assignment, which is a strength given the perturbation. However, it does depend on avoidance signals carrying reliable information about social-pressure sensitivity — a condition the perturbation weakens because the researcher no longer controls how, when, or with what framing the avoidance option is presented. In a researcher-assigned design, the signal could be embedded in a structured instrument; under the perturbation, it is an organic household choice of unknown meaning.

**Verdict:** `defensible_with_caveats` — The logic is coherent and does not require random assignment, but the truthfulness assumption is heroic, the sample-size concern is acute, and the bounds may be uninformative.

---

### Candidate 4: Selection-on-Observables with Route-Neighborhood Fixed Effects

**Threat 1 — Unconfoundedness is explicitly violated by the perturbation.** The perturbation states: "Households can choose whether to receive advance notice or indicate that they prefer not to be approached after learning about the fundraising campaign beforehand." This choice is endogenous to precisely the unobserved characteristics that drive giving outcomes. The packet explicitly flags that "Potential donors may differ in how much they want to engage with the fundraiser." Household-level altruism, income, civic engagement, and social-pressure sensitivity are all unobserved in the data card and all plausibly determine both pre-contact choice and contribution behavior. The selection-on-observables assumption requires these to be irrelevant conditional on geographic and timing controls, which is not credible.

**Threat 2 — Within-neighborhood variation is endogenously determined, not as-good-as-random.** Two adjacent households on the same route segment that make different pre-contact choices are not exchangeable. The household that opts for advance notice has revealed higher baseline engagement with the cause. Even conditional on neighborhood × timing × solicitor fixed effects, the remaining variation in pre-contact choice is driven by individual-level factors that also predict giving. The fixed effects absorb area-level confounds but not the individual-level selection that the perturbation introduces.

**Threat 3 — No household-level balancing covariates exist.** The packet's baseline controls consist entirely of geographic, timing, and solicitor identifiers. It contains no household-level demographics, no prior giving history, no income or wealth proxies, and no measures of cause affinity. Selection-on-observables designs in applied microeconomics typically require rich pre-treatment covariates (e.g., lagged outcomes, detailed demographics) to make unconfoundedness plausible. The packet provides none of these.

**Condition dependency?** Yes, critically. This design depends on the condition that selection into pre-contact status is determined by observables (or that unobservables are orthogonal to pre-contact choice conditional on observables). The perturbation explicitly breaks this condition by making pre-contact choice a household-level behavioral decision driven by unobserved engagement with the cause. The candidate treats the perturbation as a nuisance to be controlled with fixed effects when it is, in fact, the central identification failure.

**Verdict:** `not_defensible`

---

### Summary

The perturbation — removal of researcher assignment of the pre-contact condition — is fatal to causal identification strategies that require exogeneity of treatment assignment (Candidates 2, 4). Candidate 3 partially survives by using the choice itself as information, but depends on untestable behavioral assumptions. Candidate 1 is the only fully defensible design because it honestly aligns with the packet's requirement to "downgrade the claim" when "strong causal identification is no longer justified."
