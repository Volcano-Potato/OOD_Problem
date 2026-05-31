## Independent Critique: Stage 4

### Candidate 1: `prompt-zone-iv`

**Packet-Grounded Threat 1 — Exclusion Restriction Violation Is Unaddressable Without Pre-Trip Intentions.** The packet explicitly states that "there is no reliable pre-trip record of the shopper's planned basket or intended mission." The IV exclusion restriction requires that prompt placement affects checkout spending *only* through route length. But a snack-aisle prompt may trigger a direct reminder or salience effect — the shopper buys snacks *without* deviating from their path. Testing this exclusion restriction requires knowing what the shopper would have bought absent the prompt, which in turn requires pre-trip intentions. The perturbation removes exactly the data needed to even attempt a falsification of this pathway. The packet itself flags this: "The main issue is endogenous within-trip exposure."

**Packet-Grounded Threat 2 — No Evidence of Exogenous Prompt Assignment and Zone Selection Is Endogenous to Unobserved Mission.** The packet says the retailer "observes which category-level prompts were available near different store areas" but contains no description of temporal or spatial randomization of prompts. Meanwhile, the perturbation removes pre-trip mission data, meaning shoppers with different trip intentions (e.g., "restock fresh produce" vs. "buy birthday cake supplies") self-select into different store zones for reasons correlated with their spending plans. A shopper who walks past the bakery zone (and sees bakery prompts) is not randomly assigned to that exposure — they walked there *because* they planned to buy bakery items. The instrument's exogeneity is untestable under the packet's data constraints.

**Perturbed-Condition Dependency Assessment:** This candidate depends on two conditions that the perturbation has broken: (a) the ability to separate prompt-salience effects from route-length effects (requires pre-trip intentions to test the exclusion restriction), and (b) the independence of prompt-zone exposure from trip mission (requires either randomization or mission controls, neither of which the packet provides). **Dependency confirmed.**

**Verdict: `not_defensible`**

---

### Candidate 2: `within-trip-sequential`

**Packet-Grounded Threat 1 — Visit-Order Is Endogenous to Unobserved Purchase Intentions.** The critical assumption states that category visit order is independent of planned spending intensity. But the perturbation removes pre-trip basket data, and shoppers almost certainly route themselves based on what they intend to buy. A shopper planning to buy fresh produce visits produce first; a shopper planning to buy frozen foods heads to the freezer aisle first. Without pre-trip plans, there is no way to control for or even diagnose this planned-ordering confound. The packet's own data card confirms the data are "primarily cross-sectional at the trip level," so within-shopper differencing (which might absorb stable preferences) is unavailable.

**Packet-Grounded Threat 2 — Trip-Stage Effects Are Inseparable from Route-Position Effects.** Even if visit order were plausibly exogenous, later-category spending could differ from early-category spending for reasons unrelated to route-induced impulse: shopper fatigue, budget depletion as the basket fills, or time pressure as the trip progresses. The perturbation removes the ability to benchmark these against a pre-trip plan (e.g., "I planned to spend X on category Y and actually spent X+Z"). The packet provides no trip-duration or basket-accumulation metrics to disentangle these mechanisms.

**Perturbed-Condition Dependency Assessment:** The design's logic — that early-category spending ≈ planned and late-category spending ≈ unplanned — is exactly the inference the perturbation renders impossible by removing pre-trip baskets. Without knowing what was planned, the analyst cannot assign plan/impulse labels to any visit-order position. **Dependency confirmed.**

**Verdict: `not_defensible`**

---

### Candidate 3: `selection-on-observables-matching`

**Packet-Grounded Threat 1 — The Dominant Confound (Trip Mission) Is Unobserved by Construction.** The unconfoundedness assumption requires that all joint determinants of route length and spending are captured in covariates. The perturbation explicitly removes "the shopper's original intended basket before wandering begins." Trip mission type — whether this is a major weekly stock-up trip, a quick fill-in trip, or a browse-heavy leisure trip — determines *both* how far the shopper walks *and* how much they spend. The packet's available covariates (demographics, store familiarity, time-of-day, prompt exposure) cannot proxy for mission type: two demographically identical shoppers entering at the same time on the same day can have fundamentally different trip missions with radically different route-length/spending relationships. The perturbation degrades the covariate set precisely at its most critical variable.

**Packet-Grounded Threat 2 — The Outcome "Unplanned Spending" Is Unmeasurable, Forcing Reliance on Total Spending.** The research objective asks to estimate "whether longer in-store travel causes higher unplanned spending." The perturbation removes pre-trip baskets, so "unplanned" cannot be defined at the individual-trip level. The candidate substitutes total spending, which conflates planned and unplanned components. Even if matching balanced covariates perfectly, the estimand would be the effect of route length on *total* spending — a different, weaker question than the one posed, and one where the business interpretation ("does making people walk more make them spend more overall?") fails to address the mechanism the retailer cares about.

**Perturbed-Condition Dependency Assessment:** The candidate depends on the ability to condition on trip mission and to measure unplanned spending. The perturbation breaks both. Demographics and time-of-day do not substitute for trip-level purchase intentions. **Dependency confirmed.**

**Verdict: `not_defensible`**

---

### Candidate 4: `descriptive-correlation-decomposition`

**Packet-Grounded Threat 1 — "Unplanned" Spending Proxies Are Inherently Misclassification-Prone.** This candidate acknowledges that any definition of "unplanned" constructed from checkout data alone (e.g., rarely-purchased categories, prompt-matched items) is a proxy. Without pre-trip baskets, there is no ground truth to calibrate or validate this proxy. A shopper who always buys cereal on every trip and passes a cereal prompt will have their cereal purchase classified as "prompt-responsive/unplanned" under a naive proxy, when it is in fact entirely planned. The packet provides no household purchase-history panel that could be used to construct a better baseline.

**Packet-Grounded Threat 2 — Descriptive Associations Cannot Answer the Causal Business Question.** The retailer wants to know "whether path-inducing promotions are useful." A positive partial correlation between route length and spending does not imply that interventions lengthening routes will increase spending. Reverse causality (shoppers with larger spending needs walk further to fulfill them) and omitted variable bias (trip mission drives both) are equally consistent with the same descriptive pattern. The candidate correctly disclaims causal interpretation, but the business decision-maker receives no actionable evidence on the policy question.

**Perturbed-Condition Dependency Assessment:** This candidate makes no causal identification assumptions and does not depend on pre-trip basket information. It operates entirely within the data the packet actually provides. Its threats are inherent to descriptive analysis and are explicitly acknowledged in the candidate's own framing. **No dependency on perturbed conditions.**

**Verdict: `defensible_with_caveats`** — defensible as a descriptive analysis, with the caveat that it cannot answer the causal research question and that "unplanned spending" proxies are unvalidated.

---

### Summary Assessment

All three causal candidates (`prompt-zone-iv`, `within-trip-sequential`, `selection-on-observables-matching`) depend on conditions that the perturbation — removal of reliable pre-trip planned basket and mission data — has broken or rendered unverifiable. The perturbation is not a marginal data limitation; it removes the single most important variable for causal identification of route-length effects on *unplanned* spending. The descriptive fallback is the only candidate consistent with the packet's actual data constraints. The Stage 3 recommendation of `descriptive-correlation-decomposition` as primary is correct and necessary.
