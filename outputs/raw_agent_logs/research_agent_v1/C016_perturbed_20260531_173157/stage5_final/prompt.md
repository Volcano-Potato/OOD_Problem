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
<!-- case_id: C016 -->
<!-- variant: perturbed -->

# Anonymous Research Design Task: Perturbed Variant

## Task Rule

Use the information provided below to design a rigorous empirical strategy for this anonymized applied business/economics research problem. Your goal is to produce a defensible research design, not to write a literature review.

Do not assume that a known paper has already solved the task. Ground your reasoning in the background, data description, institutional details, and constraints provided in this packet.

Do not fill in packet-absent operational details, institutional features, or named design devices as if they were known facts. If multiple concrete implementations fit the packet, describe them generically or label them explicitly as illustrative examples rather than assumptions.

If credible causal identification is not possible from the provided information, do not invent an identification strategy. State the strongest defensible descriptive or correlational analysis instead.

## Research Background

A school-based adolescent health program wants to know whether targeted risk information changes behavior more effectively than standard generic messages. The practical challenge is that sensitive behavior is hard to measure directly, and not every plausible dataset provides an equally credible outcome.

## Research Setting

Schools differ in the information environment students face: some students receive only a standard generic message, while others are additionally exposed to targeted information about differential risk across choices or partner types. Follow-up still includes a later survey about activity, partner characteristics, and protection behavior, but the objective downstream outcome available in the base case is not available here.

## Research Objective

Design a study to estimate whether targeted risk information changes adolescent behavior more effectively than the standard generic curriculum when only survey-based behavioral outcomes are observed.

## Specific Questions To Answer

1. Can the information-content effect still be identified credibly with the available outcomes?
2. How much can be learned from self-reported activity, partner characteristics, and protection behavior alone?
3. Which mechanism claims remain plausible, and which become too strong without the objective outcome?
4. What additional data or design changes would be needed to restore stronger causal interpretation?

## Data Structure Overview

- Stage 1: A focal student cohort is enrolled in schools before targeted information is delivered.
- Stage 2: Schools differ in whether students receive only the standard generic curriculum or also receive targeted information about differential risk.
- Stage 3: The cohort is followed into a later period through a behavior survey that records self-reported activity, partner characteristics, and protection behavior.
- Stage 4: No objective downstream outcome related to unsafe behavior is available in the current data.

## Data Card

| field | description |
|---|---|
| unit of observation | Individual student in the survey follow-up sample. |
| time span | Intervention period plus later survey follow-up; exact dates are withheld. |
| sample construction | Survey respondents come from the focal cohort after the school transition. |
| treatment or exposure variable | School-level information-content condition. |
| outcome variable | Self-reported behavior, partner-profile measures, and self-reported protection behavior. |
| secondary outcomes | Follow-up schooling status or related survey outcomes if observed. |
| assignment or variation source | Planned school-level variation in information content. |
| assignment level | School or classroom-wide implementation level. |
| outcome measurement level | Individual student level. |
| panel or repeated structure | Single selected survey follow-up rather than broad verified tracking. |
| compliance or take-up | Exposure can vary with attendance or participation. |
| spillover or interference | Students may exchange information across cohorts or schools, and partner markets may create interference. |

## Variable Groups

### Treatment Or Exposure Variables

- Generic-information assignment.
- Targeted-information assignment.

### Selection Or Sample-Flow Variables

- Focal-cohort membership.
- Inclusion in the later survey follow-up sample.

### Main Outcome Variables

- Self-reported activity.
- Self-reported partner-profile measures.
- Self-reported protection behavior.

### Secondary Outcome Variables

- Follow-up schooling-status indicators if observed.

### Baseline Controls And Design Variables

- School characteristics, cohort composition, and available pre-treatment environment measures.

## Perturbed Condition

The broad objective downstream outcome used in the base setting is not observed here. The available outcomes are only self-reported survey responses collected in later follow-up.

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
      "name": "School-level ITT on self-reported outcomes",
      "estimand": "Intention-to-treat effect of school-level assignment to targeted risk information (vs. generic curriculum) on self-reported activity, partner characteristics, and protection behavior.",
      "identifying_variation": "Cross-school variation in planned information-content condition, with individual-level survey outcomes measured at a single follow-up wave.",
      "critical_assumption": "Self-reporting propensity and social-desirability bias do not differ systematically between the targeted-information and generic-information arms.",
      "packet_support": "Packet provides school-level assignment ('Planned school-level variation in information content'), individual-level survey follow-up recording activity, partner characteristics, and protection behavior, and baseline school characteristics.",
      "fragility": "The treatment itself differentially changes the information students possess about risk, which likely alters their awareness of what constitutes risky behavior and their willingness to report it. Differential reporting bias is therefore highly plausible and cannot be tested without an objective outcome. This confound is the core identification problem the perturbed condition creates.",
      "is_fallback": false
    },
    {
      "name": "Difference-in-differences with baseline survey measures",
      "estimand": "Effect of targeted-information assignment on change in self-reported outcomes from pre-intervention baseline to follow-up, relative to the change in generic-information schools.",
      "identifying_variation": "Within-school pre-post change interacted with between-school variation in information-content condition.",
      "critical_assumption": "Neither time-varying shocks to reporting behavior nor treatment-induced shifts in reporting norms differ across arms; parallel trends hold for true behavior and for measurement error jointly.",
      "packet_support": "Packet states that the focal cohort is 'enrolled in schools before targeted information is delivered' and mentions 'baseline controls and design variables' including available pre-treatment environment measures. This implies at least some pre-intervention measurement exists.",
      "fragility": "The DiD structure can difference out time-invariant school-level or individual-level reporting tendencies, but it cannot separate a treatment-induced change in true behavior from a treatment-induced change in reporting propensity. If targeted information makes students more aware of risk and therefore more (or less) honest in follow-up surveys, the DiD estimate conflates behavioral change with measurement change. The single follow-up wave also precludes testing for differential trends.",
      "is_fallback": false
    },
    {
      "name": "Partner-characteristic triangulation design",
      "estimand": "Effect of targeted-information assignment on self-reported partner-profile measures (age gaps, partner-type composition), using these as less-direct but potentially less-reporting-biased behavioral proxies.",
      "identifying_variation": "Cross-school variation in information content interacted with the differential sensitivity of partner-profile items versus direct activity items within the same survey instrument.",
      "critical_assumption": "Partner characteristics are reported with materially lower social-desirability bias than direct activity reports, and the differential between the two item classes captures true behavioral response rather than differential reporting error.",
      "packet_support": "The survey records 'partner characteristics' and 'self-reported activity' as distinct outcomes. Partner characteristics (e.g., age differences, partner type) may be perceived as less sensitive to disclose than direct sexual-activity reports and may be less directly targeted by the information treatment.",
      "fragility": "All outcome measures remain self-reported; there is no objective benchmark to validate differential reporting bias across item types. If targeted information changes how students perceive and report partner characteristics (e.g., increased awareness of age gaps as a risk factor), then partner-profile measures inherit the same reporting-bias problem. The triangulation logic relies on an untestable assumption about relative bias magnitude.",
      "is_fallback": false
    },
    {
      "name": "Descriptive partial-identification bounds analysis",
      "estimand": "Bounded interval for the average treatment effect of targeted information on true behavior, derived from self-reported outcomes under explicit, transparent assumptions about the direction and maximum magnitude of differential reporting bias.",
      "identifying_variation": "Cross-school variation in information content combined with researcher-imposed bounds on the misreporting differential (e.g., using worst-case Manski-style bounds or assumptions about monotonic reporting bias).",
      "critical_assumption": "Analysts can credibly sign and bound the differential reporting bias between treatment arms from institutional knowledge, survey-mode evidence, or auxiliary data; without such bounds, the interval is [-1, 1] and uninformative.",
      "packet_support": "The perturbed condition explicitly removes the objective outcome, making causal point identification indefensible. The packet instructs: 'If strong causal identification is no longer justified, the answer must explicitly downgrade the claim or propose additional design changes.' The partial-identification framework directly addresses this instruction by replacing point identification with transparently qualified interval estimates.",
      "fragility": "Without external validation data or an objective benchmark, bound selection is subjective; ranges may be too wide to be policy-relevant; and bounding reporting bias does not solve the underidentification of the behavioral effect vs. the reporting effect—it only quantifies the severity of the problem.",
      "is_fallback": true
    }
  ],
  "recommended_primary": null,
  "notes": "No candidate can credibly separate the effect of targeted information on true behavior from its effect on reporting propensity because the perturbed condition removes the objective outcome that would serve as a benchmark. The school-level ITT design is the natural starting point but fails under the most plausible form of differential measurement error. The DiD variant improves on the ITT by removing time-invariant confounds but does not solve the core underidentification. The partner-characteristic triangulation is creative but rests on an untestable hierarchy of reporting bias. The partial-identification fallback is the most intellectually honest response to the packet constraints: it explicitly downgrades the causal claim and provides a framework for what can be learned under transparent assumptions. Recommended primary is null because no design achieves credible causal identification given the packet's removal of the objective outcome."
}
```

## Stage 4 Critique

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

