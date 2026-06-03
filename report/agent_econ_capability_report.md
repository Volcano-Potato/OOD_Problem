# Agent Capability in Economics: An Execution-Side Diagnostic of Causal-Design Reasoning

*A sub-project report for the final project on AI agents in economics research.*

---

## 0. Executive Summary

This sub-project asks a narrow but consequential question:

> When a research agent is handed an **anonymized applied business/economics research-design task**, where does it actually fail?

The motivation comes directly from *The Ideation Bottleneck* (Li Ning, Tsinghua University, April 2026), which decomposes the AI–human quality gap in economics research into **idea quality** and **execution quality**, and finds that execution still carries a real, measurable residual gap even after idea quality is held aside. This sub-project does **not** try to re-measure idea quality. Instead it turns one especially credibility-critical slice of *execution* — causal-design reasoning — into a controlled out-of-distribution (OOD) stress test, and instruments exactly where the agent's claims drift away from what the evidence supports.

I built a full benchmark pipeline (not a prompt demo): Our 10-paper main set spans 8 application domains, including behavioral economics, consumer finance, platform economics, public economics, development, political economy, health, and marketing, each rendered as five task variants under an information gradient and two stress conditions (`perturbed`, `no_solution`); ran an isolated OpenClaw research agent (DeepSeek-V4-Pro backbone) one packet at a time; extracted **414** atomic claims from the agent outputs; double-labeled and adjudicated them; and computed claim- and run-level metrics. I then ran a four-rung **intervention ladder** (baseline → critic-reconcile → +retrieval → +planner/debate) on the hardest stress condition.

**Headline finding.** The agent is fluent at *producing* a plausible design memo, but unreliable at *keeping its claim strength aligned with what the packet actually justifies*. On the frozen baseline:

- Mean Claim Score: **0.82** (414 adjudicated claims, 50 runs)
- Design-Evidence Inconsistency Rate: **0.2415**; Overclaim is the largest non-clean error class (**51 claims, 12.3%**)
- Information gradient: `level1 → level2` jumps **0.690 → 0.831**, but `level2 → level3` is flat (**0.831 → 0.842**)
- Under broken identification (`perturbed`), **9/10** cases show *mechanical reuse* of the original design
- The intervention ladder drives `perturbed` mechanical reuse from **9/10 → 2/10 → 0/10 → 0/10**

In Bottleneck's vocabulary, this is an **execution-residual** result, not an ideation result: once a plausible design direction is on the table, the agent often fails to keep identification logic, measurement assumptions, and final claims mutually consistent.

---

## 1. Background and Positioning

### 1.1 The Ideation Bottleneck decomposition

*The Ideation Bottleneck* evaluates 953 economics papers — 912 AI-generated papers from the APE (Autonomous Policy Evaluation) project at the University of Zurich, and 41 human papers from the *American Economic Review* and *AEJ: Economic Policy*. Its central results:

- In head-to-head comparisons, human papers win **~83%** of matchups.
- The gap decomposes into two independent components. The **idea-quality gap is large** (Cohen's *d* = **2.23**, *p* < 0.001): human papers reach **47.1%** mean ensemble "exceptional" probability versus **16.5%** for AI.
- The **execution-quality gap is significant but smaller** (*d* = **0.90**): human papers score **4.38/5.0** versus **3.84** for AI.
- A variance decomposition attributes **≈71%** of the total quality gap to **idea quality** and **≈29%** to **execution quality**.
- Within execution, the single largest weakness is **mechanism analysis depth** (*d* = **1.43**), "reflecting AI papers' tendency to rely on established causal architectures without probing boundary conditions or constructing rich theoretical accounts of why effects arise." There is **no significant gap on robustness** (*d* = 0.08, *p* = 0.827).
- **74%** of AI papers use difference-in-differences as their primary identification strategy; only **7 of 912** AI papers (**0.8%**) surpass the median human paper on *both* idea and execution simultaneously.

The paper's six execution dimensions are: *causal identification strength, econometric sophistication, robustness and sensitivity analysis, data quality and appropriateness, mechanism analysis depth, and writing clarity and precision.*

### 1.2 What this sub-project adds

Bottleneck supplies the top-level decomposition; it scores *finished papers* holistically. This sub-project operationalizes a **micro-decomposition of the execution side**: instead of grading a finished paper, it stresses the agent at *design time* and watches, claim by claim, where causal credibility breaks. Concretely, it isolates four execution failures most consequential for causal credibility:

1. **Identification mismatch** — proposing variation that does not actually identify the estimand.
2. **Failure to re-evaluate after a condition breaks** — keeping a base design after a key identifying condition is removed.
3. **Mechanism claims that outrun the design** — committing to one channel when the evidence supports several.
4. **Confidence that survives the loss of identification** — emitting causal language when no credible exogenous variation remains.

This deliberately concentrates on Bottleneck's **Identification Strategy** and **Mechanism & External Validity** dimensions — the latter being exactly where Bottleneck found the largest execution gap (*d* = 1.43). Robustness and writing are intentionally secondary, mirroring Bottleneck's own finding that they are not where the action is.

---

## 2. What I Built and Did

### 2.1 Benchmark construction

The frozen main set is **10 cases** spanning **8 domains**: behavioral economics, consumer finance, development economics, health, marketing, platform economics, political economy, and public economics. Each case is built in two strictly separated layers:

- **Evaluator-only** (never enters agent context): `source_packet.md`, `source_facts.md`, `gold_reference.md`, `audit.md`, variant construction notes, `metadata.yaml`.
- **Agent-facing**: `agent_task_level1/2/3.md`, `agent_task_perturbed.md`, `agent_task_no_solution.md`.

Each case is rendered into **five variants** along three benchmark pressures:

| Pressure | Variant | What it tests |
|---|---|---|
| Information gradient | `level1` → `level2` → `level3` | Can the agent *use* better-structured evidence when it is available? (`level1` = core setting + objective; `level2` adds data structure; `level3` adds institutional detail + explicit threats.) |
| Perturbation | `perturbed` | Does the agent re-check identification after **one critical identifying condition is removed**? |
| No-solution honesty | `no_solution` | Does the agent **downgrade from causal to descriptive** language when no credible identification remains? |

A core design principle is anti-reconstruction: agent-facing packets carry no paper titles, authors, or precise locations, and an explicit `Task Rule` forbids inventing packet-absent operational facts. If an output reconstructs source-paper-like detail, it is flagged `suspected`/`contaminated` rather than auto-`clean`.

### 2.2 Run setup

All formal runs used a locally **isolated** OpenClaw agent (`benchmark_isolated`, DeepSeek-V4-Pro backbone) under script-driven orchestration:

- fixed workspace **outside** the repo, with **no local benchmark file access**;
- one task packet per run, fed as a plain-text message;
- a fresh session per run (no cross-case contamination);
- **remote tools allowed** (web search/fetch, scholarly MCPs) — a realistic agent condition, not strict closed-book.

The frozen main matrix is **50 successful annotated runs** = 10 cases × 5 variants (`level1/2/3/perturbed/no_solution`).

### 2.3 Scoring pipeline

1. Extract atomic claims from each output's `Claim-Evidence Table`.
2. First-pass annotation (`human_judgment` ∈ {supported, partially_supported, unsupported, contradicted}; `error_type`; severity).
3. Sample **21.1%** of claims for blind second labeling.
4. Adjudicate disagreements; freeze `adjudicated_labels.csv` as the single source of truth.
5. Compute claim- and run-level metrics, grouped tables, and figures.

Inter-annotator agreement on the second-label sample was high (**~97.4%** simple agreement on both judgment and error type), with only a handful of explicit adjudicated disagreements — adequate reliability for a structured diagnostic of this size.

### 2.4 Intervention ladder (post-baseline extension)

After freezing the baseline, I built three increasingly structured **research-agent arms** and re-ran them on the shared 10-case `perturbed` subset:

- `research_agent_v1` — external **critic-and-reconcile** loop (candidate design → independent critique → reconciled final memo).
- `research_agent_v2_search` — v1 **plus a real retrieval stage** (live scholarly retrieval seeded via OpenAlex).
- `research_agent_v3_planner_debate` — v2 **plus a planner stage and a one-round critique–response debate**.

---

## 3. Results

> **Scope note.** All baseline headline numbers below are from `agent_variant == benchmark_isolated` (50 runs, 414 claims), the frozen main benchmark. The intervention arms ran only on the 10 `perturbed` cases; for them the defensible headline is the **paired manual mechanical-reuse audit**, not their claim-level summary scores (which are inflated on the small subset and should not be quoted as headline quality).

### 3.1 Overall error profile

The agent is not failing on format. It is failing on **claim calibration**.

| Error type | Count | Rate |
|---|---:|---:|
| none (clean) | 314 | 0.7585 |
| **Overclaim** | **51** | **0.1232** |
| Unsupported Claim | 42 | 0.1014 |
| Contradiction | 7 | 0.0169 |

| Headline metric | Value |
|---|---:|
| Mean Claim Score | **0.8200** |
| Design-Evidence Inconsistency Rate | 0.2415 |
| Overclaim Rate | 0.1232 |
| Unsupported Design Claim Rate | 0.1014 |
| Contradiction Rate | 0.0169 |
| Mechanism Confounding Rate (proxy) | 0.2711 |
| Critical Design Omission Rate (proxy) | 0.0386 |

Overclaim is the single largest non-clean class. Contradictions are rare but severe — they cluster exactly in the `perturbed` and `no_solution` stress conditions, where a single causal sentence violates the design.

### 3.2 Information gradient: more context helps once, then plateaus

Run-level mean claim scores along the information gradient:

| Variant | Mean run score | Inconsistency rate |
|---|---:|---:|
| `level1` | **0.6902** | 0.3784 |
| `level2` | **0.8313** | 0.2528 |
| `level3` | **0.8421** | 0.2557 |

The pattern is sharp and informative: a **large** `level1 → level2` jump (+0.14), then a **flat** `level2 → level3` (+0.01). Structured data and design information clearly help; **adding explicit threat hints on top did not**. The dominant weakness is therefore *not* "lack of context" — it is how the agent constrains claims **once context is present**.

This dovetails with a separate threat-recognition audit on baseline `level2` outputs: the agent named the seeded threats **19/20** times (95%; mean 1.9/2 per case). So the agent largely *sees* the threats; the failure is in **threat-to-claim alignment**, not threat blindness.

### 3.3 Perturbation: identification vigilance is weak

Baseline `perturbed` mean run score is **0.7562**, clearly below `level2`/`level3`. The paired Level-2-vs-Perturbed audit sharpens it: **9/10** perturbed cases exhibit **mechanical reuse** — the agent keeps the original identifying logic even after the one critical condition is removed.

The sharpest collapses:

- **C014 perturbed = 0.375** (corruption monitoring): after independent measurement is removed, the agent still claims a change in *true* leakage while its own evidence field reads "None (no independent measurement available)" — a **critical contradiction**.
- **C005 perturbed = 0.5714** (ad measurement): after opportunity-side logs for untreated users are removed, the agent preserves an exposed-user LATE estimand and even labels it `LATE` — **mechanical reuse of an identification strategy** whose comparability condition no longer exists.

These are not retrieval failures. They are failures to ask "**which estimand survives now that this condition is gone?**"

### 3.4 No-solution: strong global downgrading, fragile local backsliding

Under the current heuristic, **8/10** tested `no_solution` runs avoided supported/partially-supported causal claims. That is encouraging but incomplete: a run can pass the run-level honesty heuristic and still emit one direct causal sentence that adjudicates as `contradicted`. The cleanest example is **C020 no_solution** (price-ending field experiment): the packet explicitly states there is no randomization, no instrument, no timing shock — yet the output still asserts "the terminal-digit format has a causal effect on demand," with its own claim table reading "N/A — no credible identification."

Reading: the agent is **strong at global downgrading, still vulnerable to last-mile causal backsliding**.

### 3.5 Heterogeneity by domain and failure mode

The weakest slices are coherent with the causal-credibility theme. By **key failure mode** (claim-level mean score):

| Failure mode | Mean claim score | Inconsistency rate |
|---|---:|---:|
| `measurement_error` | **0.8297** | 0.2174 |
| `mechanism_confounding` | 0.8769 | 0.1731 |
| `endogenous_exposure` | 0.9212 | 0.1033 |
| `timing_endogeneity` | 0.9308 | 0.0923 |

`measurement_error` is the hardest category — the agent struggles most when **measurement quality is itself part of identification**, not a minor caveat. By domain, the weakest runs are **health (0.818)** and **political economy (0.841)**, both measurement-heavy.

### 3.6 Representative failure taxonomy

Five recurring, non-accidental failure families (full write-ups in `results/failure_cases.md`):

| Failure family | Case | Core mechanism |
|---|---|---|
| Unsupported operational concretization | `C001 level2` | Converts a generic packet affordance into a definite, observed institutional fact, then reasons from it. |
| Mechanical reuse under broken identification | `C005 perturbed` | Keeps the base exposed-user estimand after the comparability condition is removed. |
| Measurement credulity | `C014 perturbed` | Treats administrative reports as a clean corruption outcome with no independent measurement. |
| Mechanism over-interpretation | `C016 level2` | Jumps from objective-vs-self-report discordance to a single "reporting artifact" conclusion. |
| No-solution causal backsliding | `C020 no_solution` | Emits a causal sentence after the packet declared no credible identification. |

### 3.7 Intervention ladder: what actually fixes it

Paired **mechanical-reuse** audit on the 10 `perturbed` cases:

| Arm | Mechanical reuse | Retrieval success | Planner | Mean debate rounds | Mean retrieval calls | Mean runtime (s) |
|---|---:|---:|---:|---:|---:|---:|
| `baseline` | **9/10** | 0/10 | 0/10 | 0.0 | 0.0 | 0.0 |
| `research_agent_v1` (critic-reconcile) | **2/10** | 0/10 | 0/10 | 0.0 | 0.0 | 0.0 |
| `research_agent_v2_search` (+retrieval) | **0/10** | 10/10 | 0/10 | 0.0 | 16.7 | 789.9 |
| `research_agent_v3_planner_debate` (+planner+debate) | **0/10** | 10/10 | 10/10 | 1.0 | 19.7 | 899.7 |

Reading:

- **`v1` is the dominant first-order fix** (9→2). Most baseline failure is *not* lack of candidate designs — it is the absence of a forced reconciliation between the final answer and an explicit threat audit.
- **`v2` closes the gap** (2→0) with *real* retrieval (attempted 10/10, successful 10/10, zero-tool runs 0/10), especially on residual cases where the downgrade needs methodological backing to justify rejecting a tempting salvage design.
- **`v3` does not beat `v2` on the headline** (0→0) while costing more tool calls (19.7 vs 16.7) and ~14% more runtime. Its value is **auditability** (explicit planner + critique-response traces), not better default results.

**Default recommendation: `research_agent_v2_search`.** Keep `v3` as a diagnostic/ablation arm.

---

## 4. What These Phenomena Indicate

**1. The measured weakness is an execution residual, exactly as Bottleneck predicts.** Bottleneck found execution contributes ~29% of the gap, with mechanism depth (*d* = 1.43) the worst dimension and robustness essentially fine. This sub-project's results are the *fine-grained, claim-level* version of that picture: the agent's worst behaviors are mechanism over-interpretation and identification reuse, while format/robustness boilerplate is competent. The benchmark is, in effect, a downstream diagnostic layer for Bottleneck's execution residual.

**2. The bottleneck inside execution is calibration, not capability.** The agent recognizes threats (95% on the threat audit), can articulate standard designs, and writes fluently. What it cannot reliably do is hold a **stable mapping** between *what the packet supports → what the design requires → what the claim table is allowed to say*. Fluency masks the gap: a confidently written memo can contain a critical contradiction while reading as polished.

**3. "More information" is not the lever; "forced reconciliation" is.** The flat `level2 → level3` step shows that piling on threat hints does not help once basic structure is present. The intervention ladder shows the opposite lever works: a single critic-and-reconcile pass removes most failures. This is a concrete, actionable design implication — the cheapest large win is a structured self-critique step, not more context or a bigger model.

**4. Measurement-entangled identification is the frontier.** The hardest failure mode (`measurement_error`) and the worst single case (C014, 0.375) both involve settings where the *outcome's validity* is the identification problem. This is precisely the kind of "is my outcome even measuring the construct?" reasoning that distinguishes credible applied work — and where the agent is weakest.

**5. Retrieval helps, but as a *justification* aid, not a *recognition* aid.** `perturbed` failures are not caused by missing literature. Retrieval (v2) helped mainly by giving the agent the methodological backing to *justify rejecting* a tempting-but-invalid salvage design, closing the last 2/10 residual cases — not by helping it notice the broken condition in the first place.

---

## 5. Future Directions

1. **Scale the case set and decouple the dimensions.** Ten cases is enough for structured diagnosis, not for population claims. Expanding to 30–50 cases would allow stable per-dimension and per-domain estimates, and would let me run separate scores for "propose an idea / choose an identification strategy / refine the design / reflect on robustness," turning Bottleneck's holistic dimensions into independently observable agent abilities.

2. **Promote the safeguards into a tested agent contract.** The failure analysis already implies five concrete guards: (i) a pre-output **estimand audit** ("what is randomized vs merely observed?"), (ii) a **perturbation-delta check** ("which base condition changed; which claims must die?"), (iii) an **outcome-validity gate** (if "no independent measurement," block latent-construct claims), (iv) a **no-solution causal guard** (reject "X causes Y" when identification was declared absent), and (v) a **multi-explanation default** for mechanism sections. These should be implemented as testable hooks and ablated individually.

3. **Cross-model and cross-harness generalization.** All current runs use one backbone (DeepSeek-V4-Pro) under OpenClaw. Re-running the frozen matrix on other frontier models would separate *model-level* from *scaffold-level* contributions to the calibration failure.

4. **A strict closed-book arm.** The formal condition is isolated-but-tool-enabled. A matched closed-book arm would cleanly separate reasoning from retrieval and let me quantify retrieval's true marginal value rather than treating it as ambient.

5. **Better no-solution and mechanism metrics.** Replace the run-level no-solution *heuristic* with a per-sentence causal-language detector (the C020 case shows why), and add explicit omission-only and mechanism-only labels so the current *proxy* metrics become direct measurements.

6. **Push toward the idea side.** This sub-project stays on execution by design. The natural complement — and the place Bottleneck says the real gap lives (~71%) — is whether the agent can propose a *novel and appropriate* question and avoid mechanical reuse of familiar identification templates. The observed `perturbed` reuse behavior is a natural bridge into that idea-quality work.

---

## 6. Limitations

1. **Case count.** 10 cases support structured diagnosis, not exhaustive coverage of business/economics causal design.
2. **Single model / single harness.** Findings are about one OpenClaw + DeepSeek-V4-Pro configuration; generality is untested.
3. **Heuristic no-solution metric.** The 8/10 honesty figure counts supported/partial causal claims at the run level and can miss a single contradicted sentence — interpret it as "8/10 tested runs," not a population rate.
4. **Proxy metrics.** Critical-omission and mechanism-confounding rates are proxies because the label schema lacks omission-only and mechanism-only tags.
5. **Annotation subjectivity.** Despite ~97% second-label agreement, overclaim-strength judgments still rest on human interpretation.
6. **Run condition is not closed-book.** Remote tools were enabled; this is realistic but not a clean reasoning-only setting.
7. **Intervention metric stability.** For v1/v2/v3 the *only* defensible headline is the paired mechanical-reuse audit; their claim-level summary scores (≈1.0 on the 10-case subset) are inflated artifacts and must **not** be quoted as quality headlines.
8. **Exploratory pairwise extension.** An APE-style pairwise design-memo comparison was tried but its protocol strongly favors the agent memo under compression/same-family judging; it is evidence of protocol sensitivity, not a reversal of the main conclusion.

---

## 7. Bottom Line

Business and economics causal-design tasks are a useful OOD probe for research agents because they stress exactly the behaviors generic scientific-assistant evaluation under-measures: **evidence-boundary discipline, identification downgrading, measurement-aware reasoning, mechanism restraint, and honesty under no-solution conditions.**

Under this benchmark, the agent is consistently competent at *producing* a formal design report but markedly less reliable at *keeping its claims aligned with what the packet justifies*. That is the central weakness — and it is an **execution-residual** weakness, precisely the part of the gap *The Ideation Bottleneck* isolates after idea quality is set aside. The intervention ladder then shows the residual is **largely fixable with structure, not scale**: a forced critic-and-reconcile pass plus a real retrieval layer (`research_agent_v2_search`) drives broken-identification reuse from 9/10 to 0/10, while heavier planner/debate machinery (`v3`) buys auditability rather than additional accuracy.

---

### Appendix: Key Artifacts

- Frozen metrics — `results/metrics_summary.md`, `results/metrics_summary.csv`, `results/grouped_metrics.csv`
- Failure analysis — `results/failure_cases.md`
- Intervention ladder — `results/research_agent_ablation_summary.md`, `results/perturbed_pair_audit_v{1,2,3}.md`
- Bottleneck mapping — `results/bottleneck_crosswalk.md`
- Figures — `results/figures/information_gradient_scores.svg`, `error_type_distribution.svg`, `perturbed_downgrade.svg`, `research_agent_ablation_ladder.svg`
- Full technical report — `report/research_report.md`
