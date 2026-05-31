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
