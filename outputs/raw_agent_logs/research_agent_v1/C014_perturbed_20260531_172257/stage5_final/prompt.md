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
<!-- case_id: C014 -->
<!-- variant: perturbed -->

# Anonymous Research Design Task: Perturbed Variant

## Task Rule

Use the information provided below to design a rigorous empirical strategy for this anonymized applied business/economics research problem. Your goal is to produce a defensible research design, not to write a literature review.

Do not assume that a known paper has already solved the task. Ground your reasoning in the background, data description, institutional details, and constraints provided in this packet.

Do not fill in packet-absent operational details, institutional features, or named design devices as if they were known facts. If multiple concrete implementations fit the packet, describe them generically or label them explicitly as illustrative examples rather than assumptions.

If credible causal identification is not possible from the provided information, do not invent an identification strategy. State the strongest defensible descriptive or correlational analysis instead.

## Research Background

Local public projects often involve multiple layers of administration, procurement, implementation, and reporting. Monitoring may reduce leakage or misuse, but different monitoring approaches can work through different channels, and official records may not cleanly reveal true corruption outcomes.

The research problem is to design an evaluation in which outcome measurement is part of identification rather than an afterthought.

## Research Setting

Local public projects receive funds, are implemented over time, and generate administrative records as well as observable physical outputs. Researchers may be able to vary monitoring intensity or participation procedures before implementation is complete.

## Research Objective

Design a study to estimate whether monitoring interventions reduce corruption or resource leakage in local public projects, and to compare formal oversight with community-based monitoring where possible.

## Specific Questions To Answer

1. How should the study estimate the effect of monitoring on corruption or leakage?
2. What kind of outcome measure remains credible if only official financial reports are available?
3. How should the design compare formal oversight with grassroots monitoring without overinterpreting administrative outcomes?
4. Which claims about true corruption reduction can still be made, and which cannot?

## Data Structure Overview

- Stage 1: Eligible local public projects are funded and enter an implementation process with planned expenditures and reporting requirements.
- Stage 2: Projects or communities may be assigned to different monitoring or participation conditions before implementation is complete.
- Stage 3: Administrative records and implementation milestones accumulate during construction or delivery.
- Stage 4: After implementation, the researcher observes official project spending and reporting records but does not have independent technical cost or quality measurement.

## Data Card

| field | description |
|---|---|
| unit of observation | Local public project, village project, or equivalent administrative project unit. |
| time span | Project funding, pre-implementation monitoring assignment, implementation, completion, and post-completion reporting. |
| sample construction | Eligible projects receive public funds and can be assigned to monitoring or participation interventions before implementation is complete. |
| treatment or exposure variable | Monitoring condition, such as increased formal oversight probability, community information or participation intervention, or no additional monitoring. |
| outcome variable | Officially reported project expenditures, reported completion, or other administrative reporting outcomes. |
| secondary outcomes | Participation or process outcomes, implementation milestones, and any administrative indicators of reporting irregularity if observed. |
| assignment or variation source | Researcher- or government-controlled assignment of monitoring interventions across eligible projects or communities. |
| assignment level | Project or community level. |
| outcome measurement level | Project or community level. |
| panel or repeated structure | Mainly project-level cross-section with staged timing; repeated administrative reports may exist during implementation. |
| compliance or take-up | Assigned monitoring may not be fully implemented; community participation may vary even under the same assigned condition. |
| spillover or interference | Officials or contractors may shift behavior across nearby projects; community information may spread beyond assigned units. |

## Variable Groups

### Treatment Or Exposure Variables

- Formal monitoring or audit assignment.
- Community participation or information assignment.

### Selection Or Sample-Flow Variables

- Eligibility for the funded-project sample.
- Inclusion in the monitoring experiment.

### Main Outcome Variables

- Officially reported project expenditures.
- Administrative completion or reporting outcomes.

### Secondary Outcome Variables

- Participation or meeting outcomes.
- Complaint or process indicators.

### Baseline Controls And Design Variables

- Project type, project size, community or region indicators, and implementation timing.

## Perturbed Condition

Independent post-completion measurement is unavailable. The researcher observes only official project reports and related administrative records as outcome data.

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
      "name": "RCT on Reported Expenditures (ITT)",
      "estimand": "Average causal effect of monitoring assignment on officially reported project expenditures",
      "identifying_variation": "Random assignment of projects to monitoring conditions (formal oversight, community monitoring, control) before implementation is complete",
      "critical_assumption": "Random assignment is successfully implemented and the stable unit treatment value assumption (SUTVA) holds; no cross-project spillover in reporting behavior",
      "packet_support": "Packet states researcher- or government-controlled assignment at the project level, pre-implementation timing, and a cross-section of funded projects with administrative reporting outcomes",
      "fragility": "The estimand captures the effect on reported outcomes, not on true corruption or leakage. Monitoring may change what gets reported (deterrence, intimidation, improved bookkeeping, strategic misreporting) without changing actual resource use. The direction of reporting bias is unknown and may differ across arms, so even a significant ITT on expenditures cannot be interpreted as evidence of corruption reduction",
      "is_fallback": false
    },
    {
      "name": "Multi-Arm Reporting-Channel Decomposition",
      "estimand": "Differential effect of formal oversight versus community-based monitoring on distinct reporting outcomes (total expenditures, line-item detail, milestone timing, complaint records)",
      "identifying_variation": "Random assignment to three or more arms (formal audit, community participation, pure control), combined with comparison of treatment effects across different administrative report dimensions that may respond differently to top-down versus bottom-up monitoring pressure",
      "critical_assumption": "Formal oversight and community monitoring affect reporting incentives through observably different channels, so divergent patterns across report types can be partially attributed to monitoring mechanism rather than to uniform reporting shifts",
      "packet_support": "Packet explicitly asks to compare formal oversight with grassroots monitoring; multiple secondary outcomes (participation, complaints, process indicators, implementation milestones) are available alongside expenditure reports; timing structure allows within-project reporting comparisons",
      "fragility": "Without independent ground truth, the decomposition remains speculative. Both monitoring types could produce identical reporting changes through different channels, or differential patterns could be driven by differential reporting pressure rather than differential corruption reduction. No credible decomposition of reporting effects from real effects is possible without an external benchmark",
      "is_fallback": false
    },
    {
      "name": "Anomaly-Index Proxy Outcomes",
      "estimand": "Effect of monitoring assignment on a constructed index of reporting irregularities (digit heaping, round-number clustering, implausible uniformity, timing anomalies, discrepancy between expenditure and completion reports)",
      "identifying_variation": "Random assignment to monitoring conditions, combined with outcome construction that extracts signal from within-administrative-data anomalies rather than from absolute expenditure levels",
      "critical_assumption": "Reporting anomalies are valid proxies for misreporting or corruption, monitoring reduces anomalies without merely displacing them to subtler or unmeasured forms, and the anomaly-to-corruption mapping is stable across treatment arms",
      "packet_support": "Packet notes official records may not cleanly reveal true corruption and frames outcome measurement as part of identification; multiple administrative report dimensions (expenditures, milestones, timing) provide raw material for cross-validation of anomalies",
      "fragility": "The anomaly-to-corruption mapping is entirely untestable without independent measurement. Monitoring could induce more careful misreporting (reducing crude anomalies while preserving corruption), creating a spurious appearance of corruption reduction. No ground truth exists to validate or calibrate the proxy, so the exercise amounts to measuring the effect of monitoring on reporting quality, not on corruption",
      "is_fallback": false
    },
    {
      "name": "Descriptive Monitoring-Reporting Association (Fallback)",
      "estimand": "Descriptive associations between monitoring conditions and administrative reporting patterns, with explicit acknowledgment that causal claims about corruption or leakage are not supported",
      "identifying_variation": "None; the analysis is purely descriptive and does not attempt causal identification of monitoring effects on corruption",
      "critical_assumption": "No causal identification assumption is required because no causal claim about corruption is made; the only requirement is that monitoring assignment and outcome reporting are measured without systematic error",
      "packet_support": "Packet explicitly instructs that if credible causal identification is not possible, the answer must downgrade the claim; the perturbed condition removes independent post-completion measurement, making true corruption unobservable; packet states official records may not cleanly reveal true corruption outcomes",
      "fragility": "N/A — this candidate does not claim to identify causal effects on corruption and is offered precisely because stronger candidates cannot credibly separate reporting behavior from true corruption reduction using only administrative data",
      "is_fallback": true
    }
  ],
  "recommended_primary": "RCT on Reported Expenditures (ITT)",
  "notes": "The perturbed condition — no independent post-completion measurement — fundamentally changes what can be identified. Random assignment still supports a clean ITT estimate, but the estimand is the effect on reported outcomes, not on corruption. The reporting-versus-real-behavior confound is irreducible without external validation. The RCT candidate is recommended as primary because it makes the strongest defensible causal claim (effect on reporting) while transparently bounding what cannot be claimed (effect on corruption). If the research objective is strictly about corruption rather than reporting, the descriptive fallback is the only honest answer."
}
```

## Stage 4 Critique

## Independent Critique

### Candidate 1: RCT on Reported Expenditures (ITT)

**Threat 1 — Reporting-vs-reality confound is irreducible.** The perturbed condition ("Independent post-completion measurement is unavailable. The researcher observes only official project reports") severs any empirical link between the ITT estimand (effect on *reported* expenditures) and the research objective (effect on *corruption or leakage*). Monitoring can change what enters official records — through deterrence, improved bookkeeping, strategic misreporting, or intimidation — without changing actual resource use. The direction and magnitude of reporting bias are unknown and may differ across arms, making the ITT uninterpretable as evidence about corruption.

**Threat 2 — SUTVA violations are undetectable and uncorrectable without independent observation.** The packet explicitly flags that "officials or contractors may shift behavior across nearby projects" and "community information may spread beyond assigned units." With only administrative data from assigned projects, cross-project displacement of either real resources or reporting behavior cannot be detected. Spillover-contaminated ITT estimates could be attenuated, inflated, or sign-reversed relative to the true treatment effect on either reported or actual outcomes.

**Perturbed-condition dependency:** Yes. The candidate's internal validity for the ITT on *reported* expenditures survives. But the mapping from that estimand to the research question about corruption is entirely dependent on an assumption — that reporting faithfully reflects reality — that the perturbation explicitly removes. The ITT identifies a well-defined but wrong-target estimand.

**Verdict:** `defensible_with_caveats` — Internally valid causal design for the effect on reporting, but the caveat is existential: it does not answer the research question about corruption, and no amount of within-study analysis can bridge the gap without the independent measurement the perturbation removed.

---

### Candidate 2: Multi-Arm Reporting-Channel Decomposition

**Threat 1 — Observational equivalence of mechanism and measurement effects.** Both formal oversight and community monitoring could produce identical changes in administrative reports through entirely different mechanisms — or different reporting patterns through the same mechanism operating at different intensities. Without independent ground truth, any divergence across report types (expenditures vs. complaints vs. milestones) is equally consistent with differential corruption reduction, differential reporting pressure, or differential reporting completeness across arms. The perturbation makes these alternatives indistinguishable.

**Threat 2 — The decomposition's core premise is untestable under the perturbation.** The candidate assumes "formal oversight and community monitoring affect reporting incentives through observably different channels." But whether the channels are actually different in their corruption-reducing effects (as opposed to their reporting effects) can only be tested with independent outcome measurement. The packet's own warning — "different monitoring approaches can work through different channels, and official records may not cleanly reveal true corruption outcomes" — directly undercuts this premise when "different channels" operate partly or wholly outside the administrative record.

**Perturbed-condition dependency:** Yes — critically. The decomposition requires attributing divergent reporting patterns to divergent mechanisms of corruption reduction. The perturbation eliminates the only evidence that could distinguish "monitoring changed corruption" from "monitoring changed reporting."

**Verdict:** `not_defensible` — The decomposition is speculative. Every observed pattern has at least two observationally equivalent interpretations (real effect vs. reporting artifact), and the perturbation precludes resolving this ambiguity.

---

### Candidate 3: Anomaly-Index Proxy Outcomes

**Threat 1 — The proxy cannot be validated or calibrated without external measurement.** The anomaly-to-corruption mapping (digit heaping, round-number clustering, timing anomalies → corruption) is entirely untestable under the perturbation. Monitoring could reduce crude anomalies while displacing corruption into subtler forms that the index misses — officials learn to misreport more carefully rather than steal less. The perturbation directly removes the independent measurement needed to establish that the mapping is stable, monotonic, or even correctly signed.

**Threat 2 — Treatment-induced changes in the anomaly-corruption mapping.** The packet notes that monitoring interventions work "through different channels." One channel may be teaching or incentivizing more sophisticated reporting. If formal audits reduce digit heaping not by reducing theft but by making bookkeeping more meticulous, the anomaly index would spuriously indicate corruption reduction. Community monitoring could have the opposite effect — generating more informal records that appear "anomalous" in administrative data. The treatment assignment systematically changes the relationship between latent corruption and observable anomalies, and the perturbation makes this relationship change untestable.

**Perturbed-condition dependency:** Yes — absolute. The entire validity of anomaly indices as corruption proxies depends on validation against ground truth. The perturbation removes the only source of ground truth. Without it, the exercise measures the effect of monitoring on reporting quality, not on corruption.

**Verdict:** `not_defensible` — The proxy cannot be validated. Both the level and the treatment-induced change in the anomaly-corruption mapping are unknown and unknowable under the perturbed conditions. The candidate collapses into measuring reporting quality under a different name.

---

### Candidate 4: Descriptive Monitoring-Reporting Association (Fallback)

**Threat 1 — Compliance and spillover threaten even descriptive measurement.** The packet notes "assigned monitoring may not be fully implemented" and "community participation may vary even under the same assigned condition." Without independent field verification, the descriptive association is between *assigned* (not *received*) conditions and administrative reports. If compliance differs systematically across arms or project types, the descriptive pattern confounds assignment fidelity with reporting behavior.

**Threat 2 — Differential reporting completeness across conditions.** Monitoring conditions may change what gets recorded in administrative systems, not just what values get recorded. Some projects under monitoring may generate more complete administrative records, making them appear systematically different on expenditure or milestone metrics even if underlying reality is identical. This reporting-coverage confound creates spurious descriptive patterns that cannot be diagnosed without independent observation.

**Perturbed-condition dependency:** Partially. The fallback does not depend on independent measurement for causal claims, since it makes none. However, the perturbation weakens even the descriptive analysis by precluding diagnosis of differential reporting completeness. These threats are limitations to be transparently disclosed, not fatal flaws for a descriptive exercise that explicitly disclaims causal interpretation.

**Verdict:** `defensible` — Honest, appropriately scoped, and explicitly aligned with the packet's instruction that "if credible causal identification is not possible, the answer must downgrade the claim." The descriptive analysis remains informative about how monitoring conditions correlate with administrative reporting patterns, provided all threats are transparently documented. It is the only candidate that does not attempt to identify corruption effects from data that cannot support such identification.

---

### Summary

The perturbation — removal of independent post-completion measurement — severs the link between administrative reporting and true corruption for all three causal/construct-validity candidates. Candidate 1 retains internal validity for the wrong estimand (reporting, not corruption). Candidates 2 and 3 are not defensible because their decompositions and proxies are untestable without ground truth. Candidate 4 is the only honest answer to the research question as stated, precisely because it refuses to claim what the data cannot support.

