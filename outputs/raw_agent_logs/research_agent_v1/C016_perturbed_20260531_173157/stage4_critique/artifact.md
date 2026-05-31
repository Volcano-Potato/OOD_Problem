# Stage 4: Independent Critique

## Candidate 1: School-level ITT on self-reported outcomes

**Packet-grounded threats:**

1. **Treatment-induced differential reporting bias.** The treatment itself changes students' knowledge about risk. A student in the targeted-information arm who learns that certain behaviors or partner types carry elevated risk may become *more* aware that their own behavior is "risky" and adjust their self-reporting accordingly (e.g., underreporting due to heightened stigma, or overreporting due to increased salience). The generic-information arm receives no such differential awareness. This creates exactly the kind of differential measurement error the critical assumption rules out — and the packet's perturbed condition (removal of the objective outcome) makes this confound untestable.

2. **Single-wave outcome structure precludes validation.** The data card explicitly states "Single selected survey follow-up rather than broad verified tracking." Without repeated measures, an objective benchmark, or any external validation data, there is no way to assess whether between-arm differences in self-reports reflect true behavioral differences or merely differences in reporting norms induced by the treatment itself. The packet's entire perturbed condition is designed around this exact underidentification.

**Perturbed condition dependency:** YES. The candidate's critical assumption — that self-reporting propensity and social-desirability bias do not differ systematically between arms — is precisely the condition the perturbed packet has broken. The removal of the objective downstream outcome eliminates the only tool that could validate or falsify this assumption. The ITT design was defensible in the base case *because* an objective outcome existed; without it, the ITT conflates behavioral effects with measurement effects.

**Verdict:** `not_defensible`

---

## Candidate 2: Difference-in-differences with baseline survey measures

**Packet-grounded threats:**

1. **DiD cannot remove treatment-induced changes in the measurement process.** The DiD strategy differences out time-invariant confounds (e.g., a school where students always underreport). But the core threat here is *time-varying and treatment-induced*: the targeted information itself changes how students interpret and report their behavior at follow-up relative to baseline. The parallel-trends assumption must hold for *true behavior and measurement error jointly*, and the treatment directly attacks the measurement-error component. This is not a violation of parallel trends that DiD can detect or correct — it is a violation built into the treatment mechanism.

2. **The packet does not confirm that baseline behavioral survey measures exist.** The packet states that the cohort is "enrolled in schools before targeted information is delivered" and mentions "baseline controls and design variables" including "available pre-treatment environment measures." It does *not* state that the same self-reported behavioral outcomes (activity, partner characteristics, protection behavior) were measured at baseline. The pre-treatment measures could be demographic, administrative, or school-level characteristics — not individual-level behavioral survey items. Running DiD on outcomes that were not measured at baseline is impossible; assuming they were measured is filling in packet-absent operational details, which the packet explicitly forbids.

**Perturbed condition dependency:** YES. Even granting the existence of baseline behavioral measures, DiD addresses a different identification problem (time-invariant unobserved heterogeneity) than the one the perturbed condition creates (inability to separate behavioral change from reporting change). The missing objective outcome remains the fatal confound regardless of differencing.

**Verdict:** `not_defensible`

---

## Candidate 3: Partner-characteristic triangulation design

**Packet-grounded threats:**

1. **Untestable hierarchy of reporting bias across item types.** The design assumes partner characteristics are reported with "materially lower social-desirability bias" than direct activity reports. The packet provides zero evidence for this hierarchy — it merely lists "self-reported partner-profile measures" and "self-reported activity" as distinct fields in the data card. There is no embedded validation study, no mode experiment, no external benchmark that would allow an analyst to rank item types by bias magnitude. Asserting such a hierarchy without packet support is exactly the kind of operational-detail invention the task rule prohibits.

2. **Partner characteristics may be *more* sensitive to treatment-induced reporting change, not less.** If targeted information specifically educates students about differential risk across partner types or age gaps, then students in the treatment arm become differentially aware that certain partner profiles are "risky." This could increase — not decrease — the social-desirability pressure around those items. The triangulation logic could easily invert: partner-characteristic reports might carry *larger* differential reporting bias than activity reports precisely because the treatment content targets those characteristics. The packet describes "targeted information about differential risk across choices or partner types," which directly implicates partner-profile items.

**Perturbed condition dependency:** YES. The triangulation logic is an attempt to route around the missing objective outcome by exploiting within-survey variation in presumed sensitivity. But validating that presumption requires exactly what the perturbed condition removed: an objective benchmark against which to compare reporting accuracy across item types. Without it, the triangulation is pure assumption.

**Verdict:** `not_defensible`

---

## Candidate 4: Descriptive partial-identification bounds analysis

**Packet-grounded threats:**

1. **Bound selection is unconstrained without external validation.** The critical assumption requires analysts to "credibly sign and bound the differential reporting bias." But the packet's perturbed condition explicitly removes the only tool that could calibrate such bounds — the objective outcome. The packet provides no auxiliary data source, no survey-mode experiment, no institutional parameters about the magnitude or direction of social-desirability bias in this population. Without these, the analyst faces a choice between (a) imposing bounds from external literature (which may not transport to this setting) or (b) using worst-case Manski bounds that will return the trivial interval covering the full outcome range. Neither yields a policy-relevant result.

2. **Bounding does not solve the underidentification — it only quantifies it.** The candidate acknowledges this fragility directly ("bounding reporting bias does not solve the underidentification of the behavioral effect vs. the reporting effect — it only quantifies the severity of the problem"). A bound analysis that returns [−1, 1] is mathematically correct but substantively empty. The packet asks whether "credible causal identification is possible"; partial identification with uninformative bounds answers "no, but here is how bad the problem is." This is intellectually honest but may not satisfy stakeholders expecting actionable estimates.

**Perturbed condition dependency:** PARTIALLY. Unlike the other candidates, this design does not depend on the objective outcome being present — it directly responds to its absence. However, it *does* depend on the availability of credible auxiliary information to tighten the bounds, and the packet provides none. The dependency is on a substitute for the missing outcome (external validation data), and the packet does not clearly supply that substitute.

**Verdict:** `defensible_with_caveats`

**Rationale for the caveat:** This is the only candidate that does not implicitly assume away the core identification problem. It follows the packet's explicit instruction: "If strong causal identification is no longer justified, the answer must explicitly downgrade the claim or propose additional design changes." It replaces point identification with transparently qualified interval estimates and makes its assumptions explicit. The caveat is that the resulting bounds may be too wide to be policy-relevant, and credible bound-tightening requires auxiliary data the packet does not provide — a limitation that must be stated clearly and that may require recommending additional data collection (e.g., a validation subsample with objective measures, a list experiment, or a randomized response module).

---

## Synthesis

All four candidates face the same fundamental problem: the perturbed condition removes the objective outcome that would distinguish behavioral effects from reporting effects. Candidates 1–3 effectively assume this problem away, each in a different guise (no differential reporting bias, differencing removes it, or it varies predictably across item types). Candidate 4 is the only one that explicitly confronts the underidentification, downgrades the causal claim, and provides a framework for transparent analysis — albeit one whose practical value depends on auxiliary information the packet does not supply.

The Stage 3 notes correctly observe that "no design achieves credible causal identification given the packet's removal of the objective outcome." Candidate 4 is the strongest defensible response not because it solves the problem, but because it honestly represents it.
