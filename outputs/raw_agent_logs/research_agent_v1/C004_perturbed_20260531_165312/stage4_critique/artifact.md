## Independent Critique: Stage 3 Candidates vs. Perturbed Packet C004

### Perturbation Recap

The packet's perturbed condition explicitly replaces exogenous or pre-committed assignment with manager discretion: *"campaign managers choose which markets to reduce or suspend based on operational judgments, expected demand, or budget considerations."* This is not a minor weakening — it introduces forward-looking, private-information selection directly into the treatment assignment mechanism. Every causal candidate must survive scrutiny under this condition.

---

### Candidate 1: Staggered Difference-in-Differences

**Threat 1 — Forward-looking selection on anticipated demand shocks.** The packet states managers choose suspension markets based on "expected demand." If a manager anticipates a market-specific downturn and suspends paid-search there, the post-suspension sales decline reflects both the treatment effect AND the anticipated demand shock. Parallel trends is violated because treatment timing is correlated with future potential outcomes. Pre-trend tests only detect pre-existing divergence; they are silent on shocks contemporaneous with treatment that the manager foresaw but the econometrician did not.

**Threat 2 — Endogenous treatment timing with heterogeneous effects.** The packet provides no commitment device, no phased roll-out rule, and no quasi-random variation in timing. Under recent staggered-DiD decompositions (Goodman-Bacon 2021; Sun & Abraham 2021; Callaway & Sant'Anna 2021), when treatment adoption timing correlates with unit-specific trend differentials and effects are heterogeneous across cohorts or over time, the two-way fixed-effects estimator recovers a contaminated weighted average that can have the wrong sign. The packet's institutional details — manager discretion tied to demand and budget — are precisely the conditions that produce such contamination.

**Does this candidate depend on a condition the perturbed packet has broken?** Yes, directly. The original unperturbed design would have relied on exogenous or pre-committed assignment, under which parallel trends might be defensible. The perturbation removes this and introduces forward-looking selection by managers using private demand information. Parallel trends is no longer credible.

**Verdict:** `not_defensible`

---

### Candidate 2: Synthetic Control Method

**Threat 1 — Idiosyncratic selection pressures cannot be synthesized from untreated donors.** If managers suspend paid-search in markets experiencing (or anticipating) unique demand weakness, no convex combination of untreated markets — which by construction did not face those same pressures — can reproduce the treated market's counterfactual sales path. The synthetic control will systematically attribute a demand-driven decline to the treatment, inflating the estimated effect. This is not a minor bias; it is a structural failure of the donor pool.

**Threat 2 — Sparse donor pool and limited pre-period under packet ambiguity.** The packet says "multiple market areas" without specifying numbers. SCM requires a sufficiently large donor pool with a sufficiently long pre-period to achieve a good pre-intervention fit. If only a handful of markets are suspended, and the remaining untreated markets are few or systematically different, the pre-period fit will be poor or the post-period counterfactual will be unreliable. The perturbation makes systematic difference likely because manager selection targets specific markets for reasons correlated with outcomes.

**Does this candidate depend on a condition the perturbed packet has broken?** Yes. SCM relies on selection being driven by factors that can be captured through pre-period outcomes and observed covariates. The perturbation introduces forward-looking demand expectations — time-varying, unobserved, and market-specific — that cannot be reconstructed from donor markets that lacked those same expectations.

**Verdict:** `not_defensible`

---

### Candidate 3: Selection-on-Observables with Pre-Trend Adjustment

**Threat 1 — Explicitly named unobserved confounders in the packet.** The perturbation states that managers use "expected demand" and "operational judgments" when deciding where to suspend. Neither appears in the observed covariate set (historical sales, market fixed characteristics, seasonality controls, time indicators, segment summaries). Expected demand is forward-looking and inherently unobserved by the researcher. Operational judgments are private managerial information. The unconfoundedness assumption is violated by construction — the packet names the unobserved confounders.

**Threat 2 — Pre-trend adjustment cannot substitute for forward-looking information.** Including pre-period sales trends as controls can absorb divergent historical trajectories but cannot capture information the manager possesses about future market conditions that has not yet materialized in any observed variable. If a manager suspends paid-search in a market because they anticipate a local competitor entering next quarter, that rationale is not in pre-trends, not in historical sales, and not in market fixed characteristics. It is private, forward-looking, and jointly determines both treatment and future outcomes.

**Does this candidate depend on a condition the perturbed packet has broken?** Yes. Selection-on-observables requires that all confounders are observed and conditioned on. The perturbation explicitly introduces private, forward-looking confounders (expected demand, operational judgments) that are absent from the data card. No conditioning strategy can recover identification when treatment decisions incorporate information about future outcomes that the researcher cannot access.

**Verdict:** `not_defensible`

---

### Candidate 4: Descriptive Correlational Benchmarking

**Threat 1 — Patterns confound treatment effects with selection, demand heterogeneity, and substitution.** The packet documents that users substitute across unpaid search, direct navigation, neighboring markets, and other channels. A simple pre-post comparison in suspended markets will reflect not only any causal effect of paid-search removal but also demand seasonality, substitution to other channels, and the manager's reason for suspension. Even as description, the raw associations have no clear structural interpretation without a model of the manager's selection rule and user substitution behavior.

**Threat 2 — Segment-level heterogeneity is uninterpretable under non-random assignment.** The packet asks about differences across "less active and already active users." Under non-random assignment, any observed difference in paid-search associations across segments conflates (a) genuine differential treatment effects, (b) differential manager selection of which markets to treat — correlated with market segment composition, and (c) differential substitution elasticities across segments. A descriptive analysis cannot disentangle these, and presenting segment-level contrasts may actively mislead if readers impose causal interpretations.

**Does this candidate depend on a condition the perturbed packet has broken?** No. This candidate explicitly disclaims causal identification and does not rely on exogenous assignment, parallel trends, unconfoundedness, or any quasi-experimental identifying assumption. The perturbation weakens what can be learned (the descriptive patterns become harder to interpret meaningfully), but it does not break the descriptive method itself.

**Verdict:** `defensible_with_caveats` — The descriptive approach is valid as a fallback precisely because it makes no causal claims requiring exogenous assignment. However, it requires stringent caveats: (a) all associations confound treatment effects with selection, demand heterogeneity, and substitution; (b) segment-level descriptive contrasts have no clear interpretation; (c) no finding can distinguish incremental purchases from demand interception; (d) the direction of any observed association cannot be attributed to paid-search without a model of why managers suspended it.

---

### Overall Assessment

All three quasi-experimental candidates (`Staggered Difference-in-Differences`, `Synthetic Control Method`, `Selection-on-Observables with Pre-Trend Adjustment`) depend on identifying conditions that the perturbation explicitly breaks: exogenous or unconfounded assignment. The perturbation replaces experimental or quasi-experimental variation with manager discretion driven by forward-looking demand expectations — private information that is unobserved, time-varying, and jointly determines both treatment and outcomes. No amount of pre-trend testing, covariate adjustment, or synthetic matching can recover identification when the selection mechanism itself incorporates information about future potential outcomes that the researcher cannot access.

Only the descriptive fallback survives, and only with strong caveats. A descriptive fallback is recommended.

---
