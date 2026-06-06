# Plan: Leveraging *The Ideation Bottleneck* and Project APE

## Goal

Use **The Ideation Bottleneck** and **Project APE** not as background citations only, but as two external frameworks that can make this benchmark look more like a publishable research artifact:

1. **Bottleneck** provides the conceptual decomposition.
2. **APE** provides the evaluation style and external comparison logic.

The right positioning is:

> Bottleneck shows that, after controlling for research idea quality, a non-trivial share of the AI-human gap remains in execution. This project turns that residual execution gap into a fine-grained causal-design benchmark for OOD business/economics settings, and uses trap-augmented evaluation to expose specific econometric failure modes.

This is stronger than saying "we built a benchmark for OpenClaw." It says:

- Bottleneck gives the **why**.
- APE gives the **how to compare**.
- This project contributes the **fine-grained diagnosis layer**.

The key principle is:

> The project should **borrow their research posture, evaluation logic, and framing discipline**, not try to clone their full systems.

So the question is not "how do we expand into another APE or another Bottleneck."
The question is:

- what is already strong in this project,
- what can be reinterpreted through Bottleneck,
- and what small additions from APE would sharply improve credibility.

---

## What This Project Already Has

The current project is already in a good position to leverage both works:

- `10` main cases across multiple business/economics subdomains
- `44` successful main runs
- `370` adjudicated claims
- a complete `level1 -> level2 -> level3` information gradient
- `perturbed` and `no_solution` challenge variants
- a re-audited paired result: `1/10` perturbed baseline cases show mechanical reuse

So the project does **not** need more scale first.
It needs better **positioning**, **crosswalks**, and **one extra evaluation layer**.

---

## What To Borrow From Each Work

### From *The Ideation Bottleneck*

The most useful ideas to borrow are:

1. **The decomposition logic**
   - idea quality versus execution quality
   - your benchmark should be presented as a deeper probe into the execution side

2. **The prioritization logic**
   - not all execution dimensions matter equally
   - identification and mechanism are where the most informative failures live

3. **The residual-gap framing**
   - after controlling for idea quality, execution still matters
   - your project explains what that execution residual looks like in causal-design terms

4. **The anti-diffuse discipline**
   - do not try to measure every research ability
   - focus on a narrow set of economically meaningful design failures

### From Project APE

The most useful ideas to borrow are:

1. **Head-to-head comparison logic**
   - relative comparison is often more interpretable than absolute scores alone

2. **Fixed-judge protocol discipline**
   - one judge model
   - one prompt
   - one comparison protocol
   - fixed randomization procedure

3. **Tournament mindset**
   - the interesting question is not just "what score did the agent get"
   - it is also "does the agent's design lose to a stronger comparator"

4. **Autonomous-system diagnosis mindset**
   - evaluation should support a concrete story about failure modes and system repair

### What Not To Borrow

Do **not** borrow these now:

- APE's full paper-generation stack
- APE's full tournament machinery
- Bottleneck's full idea-quality pipeline
- larger-scale corpus ambitions

Those would expand the project too much and blur its current strength.

---

## Core Strategy

### Track A. Use Bottleneck as the top-level research framing

This is the most important framing change.

Instead of presenting the benchmark as:

- "an OpenClaw weakness benchmark,"

present it as:

- "a fine-grained follow-up to the execution side of Bottleneck."

### Concrete move

Add a short framing paragraph in the report and presentation:

1. Bottleneck decomposes the AI-human economics research gap into:
   - idea quality
   - execution quality
2. Bottleneck finds that execution still explains a meaningful residual gap.
3. This project takes one especially important part of execution in economics:
   - causal identification
   - mechanism reasoning
   - modern econometric awareness
4. It then measures these failures under controlled, anonymized, OOD research-design tasks.

### Why this helps

This immediately upgrades the novelty claim from:

- "we built a benchmark"

to:

- "we operationalize and micro-decompose the execution residual identified by Bottleneck."

That is a much more defensible research story.

---

## Track B. Build a Bottleneck-to-benchmark dimension crosswalk

Right now your benchmark has strong internal metrics, but the bridge to Bottleneck can be made much tighter.

### Proposed crosswalk

Create one table mapping your current outputs to Bottleneck's execution dimensions:

| Bottleneck execution dimension | Closest benchmark evidence |
|---|---|
| Identification | `level1/2/3`, `perturbed`, `no_solution`, mechanical reuse |
| Econometrics | claim-level unsupported/contradicted design claims |
| Mechanism | mechanism confounding cases; overclaim under limited evidence |
| Robustness | currently secondary; not headline |
| Data quality | misuse of self-reports / dirty outcome proxies / missing untreated opportunity logs |
| Writing | contract adherence only; not core contribution |

### Recommended use

Do **not** try to fully reproduce Bottleneck's six-dimension scoring.
Instead:

- explicitly say this benchmark focuses on the subset of execution dimensions most relevant to causal design failure;
- use Bottleneck as the reason for prioritizing identification and mechanism over robustness.

### Deliverable

Add a figure or table in the report:

- `Bottleneck execution gap -> this benchmark's measurable failure channels`

This makes your benchmark look like a principled probe rather than an ad hoc task suite.

---

## Track C. Import APE's evaluation logic as an extra validation layer

This is the single most valuable methodological upgrade.

APE's strongest reusable idea is not the corpus size.
It is the **head-to-head comparison logic**.

### Current state

Your current benchmark is mostly:

- packet-grounded tasking
- claim extraction
- human-style adjudication
- scalar metrics

This is already good, but it still evaluates OpenClaw largely in isolation.

### Proposed APE-style extension

Add one **blind pairwise design comparison** layer:

For a selected subset of cases, compare:

- **A:** the published paper's design logic, rewritten as a short anonymized design memo
- **B:** OpenClaw's proposed design, rewritten or lightly normalized into the same memo format

Then ask a fixed judge model to choose which design is more credible on:

- identification credibility
- mechanism interpretability
- defensibility under available data

### Important constraint

This should not compare full papers.
It should compare **design memos** only.

Otherwise you would be reproducing APE too literally and introducing too much noise from writing quality.

### Minimal version

Do this for:

- the `10` level2 runs only, or
- a `6-10` case subset with the cleanest packets

### Output

Report:

- `Agent design loses X/Y pairwise matchups against published design memos`
- optionally by subtype:
  - normal cases
  - perturbed cases
  - no-solution cases

### Why this helps

This gives you one external-style headline that is much easier to explain in a defense:

- claim-level metrics show *where* the errors are;
- APE-style pairwise evaluation shows *whether the overall design is still judged inferior to the real paper's logic*.

That is a strong complement.

---

## Track D. Use Bottleneck and APE together to justify a focused agent-improvement experiment

If you want one extra experiment that makes the project look more complete, this is the best candidate.

### Current diagnosis

Your benchmark already suggests:

- major gain from `level1 -> level2`
- almost no gain from `level2 -> level3`
- `1/10` mechanical reuse in the re-audited perturbed baseline

This implies the bottleneck is not "lack of more hints."
It is something like:

- methodological anchoring
- failure to re-check identification after conditions change
- weak causal-design self-critique

### Proposed intervention

Add one **reviewer-style design-critic condition**:

- baseline: current `benchmark_isolated`
- improved condition: same agent plus a fixed internal checklist or external critique pass before final answer

The checklist should force the agent to answer:

1. What is the causal estimand?
2. What exact variation identifies it?
3. Which condition would break this design?
4. Has any such condition been removed in this packet?
5. If identification fails, what weaker descriptive claim remains?

### Why this is the right add-on

This intervention is tightly motivated by both works:

- Bottleneck says execution remains a real gap after ideas are controlled.
- APE shows autonomous pipelines can be compared systematically.
- Your benchmark isolates one specific execution weakness and then tests whether a structured self-critique reduces it.

### Recommended scope

Do not run this on everything.
Run it on:

- the `10` perturbed cases
- optionally the `4` no-solution cases

### Desired headline

- `mechanical reuse changes from the current re-audited baseline rate of 1/10 to X/10`

If you can get even a modest reduction, the project becomes:

- diagnosis + targeted intervention

instead of diagnosis only.

---

## Track E. Upgrade the trap story from "dataset trick" to "theory-backed stress testing"

Your trap/variant design is already one of the best parts of the benchmark.
It should be explicitly tied to both papers.

### Better interpretation

The traps are not just "harder examples."
They are:

- **Bottleneck-style execution probes**, because they isolate design reasoning under controlled ideas
- **APE-compatible challenge splits**, because they create structured comparisons across task regimes

### Concrete reporting move

For each trap family, state:

- what hidden design condition is broken
- what weak agent behavior is expected
- which Bottleneck dimension this most directly stresses

Example:

- `perturbed`: stresses identification vigilance and anti-anchoring
- `no_solution`: stresses claim calibration and execution honesty
- `level3`: stresses whether more explicit threat information actually improves reasoning

This makes the benchmark look theoretically designed rather than heuristically assembled.

---

## Decision View

This section is the practical answer to "what should actually be added to the project?"

### Adopt Now

1. **Bottleneck framing rewrite**
   - highest value
   - almost zero engineering cost
   - improves the research identity of the project immediately

2. **Bottleneck crosswalk table**
   - clarifies why the benchmark focuses on identification and mechanism
   - makes the current metrics more interpretable

3. **APE-style pairwise design-memo evaluation**
   - the best methodological addition
   - gives an external-style relative comparison result without needing full-paper tournaments

### Adopt If Time Remains

4. **Reviewer-style design-critic intervention on perturbed cases**
   - strongest diagnosis-to-repair extension
   - but is still an extra experiment, not a framing necessity

### Do Not Add Now

- new cases
- new annotation rounds
- new error taxonomies
- cross-agent expansion
- full APE replication
- full Bottleneck idea-scoring replication

These would increase scope much more than scientific value.

---

## Why These Additions Fit This Project Specifically

The project already has a strong internal evaluation spine:

- task packets
- gold references
- claim extraction
- adjudication
- grouped metrics
- failure cases

So the right additions are not "more infrastructure."
They are additions that improve:

1. **external intelligibility**
   - Bottleneck framing

2. **theoretical justification**
   - Bottleneck crosswalk

3. **evaluation credibility**
   - APE-style head-to-head layer

4. **repair relevance**
   - design-critic intervention

This is why these two works are useful here:

- Bottleneck helps explain **what your benchmark is for**
- APE helps explain **how one extra comparison layer should be done**

---

## Recommended Deliverables

If the goal is to make the project more outstanding without exploding scope, the best additions are:

### Must-do

1. **Bottleneck framing rewrite**
   - make the project explicitly a fine-grained execution-gap diagnostic

2. **Bottleneck crosswalk table**
   - connect your current metrics to Bottleneck's execution dimensions

3. **APE-style pairwise design-memo evaluation**
   - even on a subset

### High-value optional

4. **Design-critic intervention on perturbed cases**
   - the smallest improvement experiment with the highest interpretive value

### Not recommended now

- adding many more cases
- adding more error taxonomies
- adding more annotation rounds
- reproducing APE's full tournament machinery

The practical interpretation is:

- Bottleneck contributes mainly to **positioning and dimension choice**
- APE contributes mainly to **evaluation protocol and relative comparison**

---

## Concrete Execution Order

### Phase 1. Positioning cleanup

Update:

- `report/research_report.md`
- `README.md`
- presentation story

with the new statement:

> This benchmark is a fine-grained diagnostic of the execution residual identified by *The Ideation Bottleneck*, with OOD business/economics cases and trap-augmented causal-design evaluation.

### Phase 2. Bottleneck crosswalk artifact

Create:

- `results/bottleneck_crosswalk.md`

Contents:

- one table mapping benchmark evidence to Bottleneck execution dimensions
- one paragraph on why identification + mechanism are the focal dimensions

### Phase 3. APE-style pairwise layer

Create:

- `results/pairwise_design_memo_eval.csv`
- `results/pairwise_design_memo_eval.md`

Procedure:

1. convert paper design logic and agent design logic into matched memos
2. randomize A/B order
3. use one fixed judge model
4. report win/loss rate

### Phase 4. Optional improvement experiment

Create:

- `benchmark/prompts/design_critic_checklist.md`
- `results/perturbed_intervention_eval.md`

Run only on perturbed cases.

---

## Minimal Implementation Route

If the goal is to make the project more outstanding with the least extra work, the minimal route is:

1. rewrite framing in `README` and `research_report`
2. add `results/bottleneck_crosswalk.md`
3. add one `pairwise_design_memo_eval` layer on a clean subset

That alone is enough to make the project feel substantially more research-like.

The design-critic intervention should be treated as a second-phase bonus, not as a requirement for the main story.

---

## Best Final Story

If these additions are executed, the strongest final story becomes:

1. Bottleneck shows that AI economics research still suffers a meaningful execution gap after controlling for ideas.
2. This project operationalizes that execution gap as a benchmark for OOD causal-design reasoning in business/economics.
3. The benchmark shows:
   - strong gain from structured data information (`level1 -> level2`)
   - little gain from extra explicit threat hints (`level2 -> level3`)
   - a narrow but real mechanical-reuse residual when identification conditions are broken (`1/10`)
4. An APE-style pairwise comparison can then show whether agent designs are still judged inferior to published design logic overall.
5. A final reviewer-style design-critic intervention can test whether the main weakness is actually reducible.

That is a much more memorable and defensible project than "we evaluated OpenClaw on some business tasks."

---

## Recommendation

If time is limited, do the following in order:

1. **Framing rewrite using Bottleneck**
2. **Bottleneck crosswalk table**
3. **APE-style pairwise design-memo evaluation**
4. **Only if time remains: perturbed design-critic intervention**

This order maximizes research value per unit effort.

---

## Reference Notes

- *The Ideation Bottleneck* is used here for:
  - the `idea vs execution` decomposition
  - the finding that execution remains a meaningful residual gap
  - the emphasis on mechanism and identification failures
  - the observation that AI economics papers over-concentrate on DiD-like designs

- Project APE is used here for:
  - head-to-head comparison logic
  - fixed-judge evaluation consistency
  - tournament-style thinking about relative design quality
  - a stronger external comparison story than absolute scoring alone
