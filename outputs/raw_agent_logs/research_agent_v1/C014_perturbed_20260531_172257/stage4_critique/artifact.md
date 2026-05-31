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
