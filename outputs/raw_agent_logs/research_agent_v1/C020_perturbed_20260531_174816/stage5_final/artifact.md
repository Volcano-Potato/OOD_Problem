# Stage 5: Final Design Memo

## 1. Executive Summary

This memo evaluates whether a retailer can credibly estimate the causal effect of a salient terminal-digit pricing format (e.g., .99 endings) on product demand given a critical perturbation: the format is never varied independently of promotional framing. Whenever the focal item displays the salient terminal-digit ending, the surrounding offer simultaneously presents the product as explicitly discounted or on sale; alternative endings appear only without that promotional framing. This perfect collinearity is lethal to causal identification of the format effect itself.

The strongest defensible analysis is a **descriptive demand decomposition** that documents how the bundled format–promotion package correlates with demand, stratified by item familiarity, product category, and offer context, with no causal attribution to the terminal-digit ending per se. A supplementary **causal estimate of the bundle effect** is defensible if customer-group assignment is conditionally ignorable, but this answers a different question — the joint effect of format + promotion, not the format alone. Heterogeneity analysis by item familiarity remains purely descriptive; the perturbed condition precludes any mechanism-probing interpretation. Recovery of a clean format-effect interpretation requires an independent design change, most naturally a 2×2 factorial crossing the terminal-digit format with promotional framing.

## 2. Research Question

Does a salient terminal-digit pricing format (e.g., .99 endings) raise demand for a focal item, and does any measured demand effect reflect the format itself rather than the broader bargain-signaling context — specifically, the explicit markdown or sale presentation that is now perfectly bundled with the format?

## 3. Target Estimand or Strongest Defensible Estimand

**Target estimand (unidentified):** The average causal effect of the terminal-digit format itself on focal-item demand, holding promotional framing and other offer-context features constant.

**Strongest defensible estimand:** The descriptive association between the bundled format–promotion package and focal-item demand, decomposed across item-familiarity strata, product categories, and offer contexts, explicitly characterized as correlational with regard to the format component. As a supplementary causal quantity, the average treatment effect of the bundled treatment package (salient ending + promotional framing) on demand is estimable under the conditional ignorability of customer-group assignment, but this estimand answers the question "what is the effect of the bundle?", not "what is the effect of the format?"

## 4. Treatment or Exposure and Main Outcomes

**Treatment/exposure:** A binary indicator taking value 1 when the focal item is displayed with the salient terminal-digit ending (and simultaneously with explicit markdown/sale presentation), and 0 when shown with an alternative ending format (and without promotional framing). By the perturbed condition, this is a single bundled exposure; no independent variation of its two components exists.

**Main outcome:** Demand for the focal product, measured as item purchases or units sold at the product–offer-version level.

**Secondary outcomes:** Differential demand response by item familiarity or prior appearance, measured through interaction terms between the bundled treatment and item-history indicators.

## 5. Data Structure Summary

| Dimension | Description |
|---|---|
| Unit of observation | Item–offer exposure or offer-version demand outcome for a focal product |
| Time span | Repeated merchandising or campaign waves |
| Sample construction | Comparable customer groups receive different versions of the same focal offer |
| Assignment level | Product–offer version or customer-group-by-offer-version |
| Assignment mechanism | The visible ending format varies across versions, but is always bundled with promotional framing (perturbed condition) |
| Outcome level | Product demand or transaction outcome linked to the assigned version |
| Panel structure | Yes; items may recur across versions or waves |
| Compliance | Assignment determines the displayed version; realized purchases remain customer choices |
| Spillover | Other cues in the same version may alter interpretation of the focal price |

## 6. Relevant Causal Mechanisms

Three mechanisms could, in principle, link the terminal-digit format to demand:

1. **Format-specific perceptual processing (the left-digit or level-effect channel).** Consumers process prices from left to right and may truncate or round down, perceiving $9.99 as meaningfully cheaper than $10.00 despite the $0.01 difference. This mechanism operates through cognitive heuristics independent of promotional context.

2. **Learned bargain association (the format-as-signal channel).** Consumers have learned, through repeated market exposure, that .99 endings signal discounted or value-priced goods. The format acts as a cue that triggers bargain-seeking behavior even absent explicit sale labeling. Under the unperturbed design, this channel is partially separable from mechanism 1 because it depends on consumer learning histories.

3. **Promotional-framing salience (the bundle amplification channel).** Explicit markdown or sale labels amplify attention and purchase intention through urgency, perceived savings, and deal evaluation. When bundled with the format, this channel operates jointly with mechanisms 1 and 2, and the three are observationally indistinguishable.

Under the perturbed condition, mechanisms 1, 2, and 3 are perfectly collinear, making any decomposition among them impossible.

## 7. Main Identification Challenge

The central identification challenge is **perfect collinearity between the terminal-digit format and promotional framing**, imposed by the perturbed condition. The packet states: "The visible ending format is no longer varied independently of bargain presentation. Whenever the focal item uses the salient terminal-digit ending, the surrounding offer also makes the product look explicitly discounted or on promotion. Alternative ending formats appear only in versions without that promotional framing."

This creates a single bundled treatment variable with no within-packet source of independent variation in either component. Any observed demand difference across treatment conditions is jointly attributable to the format, the promotional framing, the interaction between them, and any other version-level cues that co-vary with the treatment assignment. The format effect — the quantity the packet asks about — is unidentified because it is never observed varying alone.

Additional challenges include version-level confound contamination (other cues like layout, color, or positioning may differ between versions), the unknown strength of the assignment mechanism (groups are "comparable" but not necessarily randomized), and endogenous item familiarity (items become familiar through retailer choices correlated with demand expectations).

## 8. Whether Credible Causal Identification Is Possible

**Credible causal identification of the terminal-digit format effect itself is not possible** under the perturbed condition. The format and promotional framing are perfectly collinear by packet construction; no available variation can separate them. The Stage 4 critic confirms this: the perturbation "is lethal to causal identification of the format effect itself."

Credible causal identification of the **bundled treatment effect** (format + promotion) is possible, conditional on the ignorability of customer-group assignment to offer versions and the absence of material version-level confounds beyond the treatment package. However, this bundled estimand does not answer the packet's primary research question ("Can the researcher still estimate a credible causal effect of the terminal-digit format itself?"), to which the honest answer is no.

Per the packet's explicit instruction — "If credible causal identification is not possible, do not invent an identification strategy. State the strongest defensible descriptive or correlational analysis instead" — the primary analysis is descriptive. The bundle estimate is presented as a supplementary causal quantity with its limitations clearly stated.

## 9. Proposed Empirical Design or Strongest Defensible Descriptive Analysis

### Primary Analysis: Descriptive Demand Decomposition with Design Agenda

This analysis documents how the bundled format–promotion package covaries with demand across the available data, making no causal claims about the terminal-digit format per se.

**Step 1: Raw demand comparison.** Compute mean demand (units sold) for items shown with the salient ending + promotional framing versus items shown with alternative endings without promotional framing, pooling across all waves.

**Step 2: Stratified decomposition.** Repeat the comparison within strata defined by:
- Item-familiarity terciles (high/medium/low prior appearances across waves)
- Product category
- Offer-context indicators (campaign wave, season, channel if available)

**Step 3: Adjusted associational estimates.** Estimate OLS regressions of demand on the bundled treatment indicator, progressively adding controls for item history, category fixed effects, and wave fixed effects, documenting how the coefficient on the bundled treatment changes as controls are added. This is an associational exercise, not a causal identification strategy; the coefficient movements reveal confounding patterns, not causal effects.

**Step 4: Variance decomposition.** Partition the cross-version demand variance into components attributable to the bundled treatment, item fixed effects, wave fixed effects, and residual, quantifying how much of the observed demand variation is coincident with the format–promotion bundle versus other observable factors.

**Step 5: Design agenda.** Explicitly enumerate the design changes needed to recover a clean format-effect estimate, as required by the packet's Question 4.

### Supplementary Analysis: Causal Estimate of the Bundle Effect

Under the assumption that customer-group assignment to offer versions is conditionally ignorable given observable group and product characteristics, estimate:

\[
\text{Demand}_{ivw} = \alpha + \beta \cdot \text{Bundle}_{iv} + \gamma X_i + \delta_w + \varepsilon_{ivw}
\]

where $\text{Bundle}_{iv}$ is the bundled treatment indicator for item $i$ in version $v$, $X_i$ is a vector of item-level controls (history, category), $\delta_w$ are wave fixed effects, and $\beta$ is interpreted — with explicit caveats — as the average causal effect of the bundled format–promotion package on demand. This estimate is presented separately from and subordinated to the descriptive decomposition; the report must clearly state that $\beta$ is not an estimate of the format effect.

## 10. Why the Design Is Valid or Why Causal Identification Is Not Credible

**Why causal identification of the format effect is not credible.** The format and promotional framing are perfectly collinear. No statistical adjustment, instrumental variable, or heterogeneity strategy can decompose a treatment effect into the contributions of two components that never vary independently. This is not an estimation problem — it is an identification problem: the causal effect of the format itself is not a function of the observed data distribution. The Stage 4 critic's assessment is adopted in full: the perturbation is lethal, and Candidate 1 survives only by changing the estimand.

**Why the descriptive decomposition is valid.** Descriptive comparisons require only measurement validity and representativeness. The analysis transparently labels all reported associations as correlational, makes no causal claims about the format, and explicitly states what cannot be concluded. This follows the packet's fallback instruction and the critic's recommendation.

**Why the supplementary bundle estimate is defensible (with caveats).** If customer-group assignment is conditionally ignorable, the bundle effect is identified as a causal quantity. The critic rated Candidate 1 `defensible_with_caveats`, and this memo adopts all three caveats: (a) the estimand is the bundle, not the format; (b) version-level confounds remain a threat; (c) the assignment mechanism requires validation, not mere assertion. The supplementary analysis is presented only with these caveats prominently displayed.

## 11. Required Assumptions

### For the descriptive decomposition (primary):

1. **Measurement validity.** Demand outcomes, treatment indicators, and item-history variables are measured without systematic error across versions and waves.
2. **Representativeness.** The observed waves and items are representative of the retailer's merchandising universe; no selection into the analytical sample biases the descriptive patterns.
3. **No hidden version-level variation in format within treatment arms.** If the "salient terminal-digit ending" varies (e.g., .99 vs .95 vs .97 endings) within the treatment condition, these sub-formats must be documented but no differential effects are claimed without further variation.

### For the supplementary bundle causal estimate:

4. **Conditional ignorability of version assignment.** Customer-group assignment to offer versions is as-good-as-random conditional on observable item and group characteristics, or is determined by a known and correctly modeled selection process.
5. **Stable unit treatment value assumption (SUTVA).** Each customer group's demand outcomes depend only on its assigned version, not on versions assigned to other groups. This is challenged by the data card's spillover note.
6. **No unmeasured version-level confounds.** Beyond the format–promotion bundle, no other version features (layout, color palette, product positioning, co-displayed items) differ systematically between treatment and control versions in ways that affect demand.
7. **No differential compliance or attention.** All customers in a group are exposed to their assigned version, and exposure translates to attention with no systematic differences across groups or versions.

## 12. Statistical Model or Analysis Equation

### Primary descriptive model:

\[
D_{ivw} = \alpha + \beta^{\text{desc}}_{B} \cdot B_{iv} + \sum_{k=2}^{K} \gamma_k \cdot \text{Cat}_{ik} + \sum_{t=1}^{T} \theta_t \cdot \text{Wave}_{it} + \sum_{f=1}^{F} \phi_f \cdot \text{Fam}_{if} + \varepsilon_{ivw}
\]

where $D_{ivw}$ is demand for item $i$ in version $v$ during wave $w$, $B_{iv}$ is the bundled treatment indicator, $\text{Cat}_{ik}$ are product-category dummies, $\text{Wave}_{it}$ are wave fixed effects, $\text{Fam}_{if}$ are item-familiarity category dummies, and $\beta^{\text{desc}}_{B}$ is the **descriptive association** between the bundle and demand. All coefficients are interpreted as partial correlations; no causal language is attached to $\beta^{\text{desc}}_{B}$.

### Familiarity-stratified decomposition:

\[
D_{ivw} = \alpha + \sum_{f=1}^{F} \beta^{\text{desc}}_{f} \cdot (B_{iv} \times \text{Fam}_{if}) + \sum_{f=1}^{F} \lambda_f \cdot \text{Fam}_{if} + \gamma X_i + \delta_w + \varepsilon_{ivw}
\]

The $\beta^{\text{desc}}_{f}$ coefficients describe how the bundle–demand association varies by familiarity stratum, with no mechanistic attribution.

### Supplementary bundle causal model:

\[
D_{ivw} = \alpha + \beta^{\text{causal}}_{B} \cdot B_{iv} + \gamma X_i + \delta_w + \varepsilon_{ivw}
\]

where $\beta^{\text{causal}}_{B}$ is the **causal effect of the bundle** under conditional ignorability, with standard errors clustered at the item level to account for repeated observations across waves. This estimate is reported separately, labeled as "causal effect of the format–promotion bundle (not the format effect)," and subordinated to the descriptive analysis.

## 13. Robustness, Placebo, Falsification Checks, or Diagnostic Tests

### For the descriptive decomposition:

1. **Leave-one-wave-out stability.** Recompute all descriptive associations dropping one wave at a time; check whether any single wave drives the pattern, which could indicate idiosyncratic confounds in that campaign period.
2. **Within-category rank correlations.** Instead of mean differences, compute rank correlations between the bundled treatment and demand within product categories; check consistency of sign and approximate magnitude across categories.
3. **Balance tables for descriptive patterns.** Tabulate item characteristics (baseline demand in pre-treatment waves if available, category, average price level) by treatment status to document the extent of pre-existing differences that the descriptive comparison does not adjust for.
4. **Sensitivity to familiarity threshold.** Vary the cutoffs for high/medium/low familiarity strata and document whether the descriptive pattern is robust to alternative binning choices.

### For the supplementary bundle causal estimate:

5. **Covariate balance tests.** Test whether observable item and group characteristics are balanced across bundled-treatment and control versions. Systematic imbalance suggests the ignorability assumption is violated and the bundle estimate is confounded.
6. **Pre-trend comparison.** If pre-period demand data exist for the same items (in waves before the format–promotion manipulation), test whether demand trends are parallel between items eventually assigned to treatment and control versions.
7. **Placebo outcome test.** Apply the same estimator to an outcome that should not respond to the bundle (e.g., demand for a product category not featured in the manipulated offers). A non-zero "effect" would indicate confounding.
8. **Sensitivity analysis for unobserved confounding.** Apply bounding methods (e.g., Oster's delta or Cinelli-Hazlett sensitivity) to assess how large an unobserved confound would need to be to eliminate the bundle estimate.

## 14. Heterogeneity Analysis If Supportable

Heterogeneity analysis by item familiarity is supportable only in a **descriptive** form. The Stage 4 critic correctly identifies that Candidate 2's mechanism-probe interpretation is `not_defensible` because the perfect collinearity between format and promotion makes it "impossible to attribute any familiarity gradient to the format channel specifically." This memo adopts the critic's downgrade.

**What can be reported (descriptive only):**
- Stratum-specific descriptive associations between the bundled treatment and demand for high-familiarity, medium-familiarity, and low-familiarity items.
- Documentation of whether the association's magnitude differs across strata (e.g., is it larger for familiar items that consumers "recognize" as repeat offers vs. novel items?).
- Qualitative discussion of alternative interpretations: a larger association for familiar items could reflect format-specific learning (consistent with mechanism 2), greater responsiveness to promotional labels among repeat customers, or selection (familiar items are those the retailer features more because they sell well).

**What cannot be claimed:**
- That any familiarity gradient "isolates," "probes," or "provides evidence for" the format-specific mechanism.
- That a null familiarity gradient rules out a format effect.
- That familiarity is exogenous (items become familiar through endogenous retailer choices).

Additional heterogeneity dimensions that can be explored descriptively include product category (durable vs. non-durable, high vs. low price point), offer context (holiday vs. non-holiday waves, email vs. in-app display if channels vary), and item price tier.

## 15. Measurement, Compliance, Missingness, Spillover, or Implementation Limits

**Measurement.** The packet defines the outcome as "item purchases or units sold" and the treatment as an indicator for the salient terminal-digit ending. Two measurement concerns arise: (a) if the "salient ending" encompasses multiple specific digits (.99, .95, .97), pooling them assumes homogeneous effects within the treatment arm; (b) demand is observed as realized transactions, which conflates purchase incidence and quantity choice.

**Compliance.** Assignment determines the displayed version, but customers choose whether to purchase. This is a standard intention-to-treat setting; the estimand is the effect of *displaying* the bundled treatment, not of customers *noticing* or *processing* the format. No compliance adjustment is possible without individual-level exposure measures.

**Missingness.** The packet does not describe missing-data patterns. If demand is zero for some item–version–wave cells, the analysis must distinguish structural zeros (the item was not offered) from true zero demand. Item–wave combinations where the focal product was not featured should be excluded; true zeros should be retained.

**Spillover.** The data card explicitly notes that "other cues in the same version may alter interpretation of the focal price." This means that even the bundled treatment effect may be contaminated by co-varying version features. Within-customer-group spillover (one customer's purchase affecting another's through social influence or inventory depletion) is an additional concern not addressed by the packet.

**Implementation limits.** The analysis is constrained to the retailer's existing merchandising waves, offer versions, and product selection. Generalizability to other retailers, product categories, or pricing contexts requires external validation that the packet does not support.

## 16. Failure Modes and Alternative Explanations

1. **Promotion-only explanation.** Any observed demand difference is entirely attributable to the promotional framing (sale label, markdown presentation), with the terminal-digit format contributing nothing. The data cannot rule this out because format and promotion never vary independently.

2. **Format-only explanation (equally unverifiable).** The terminal-digit format drives the entire effect, and the promotional framing is redundant. Also unverifiable.

3. **Version-level confounding.** Unmeasured features of the offer versions (aesthetic design, placement prominence, co-displayed comparison prices) differ between treatment and control versions and account for some or all of the demand difference. The packet offers no guarantee that versions are identical except for the format–promotion bundle.

4. **Selection into assignment.** Customer groups are described as "comparable," not randomly assigned. If groups differ in price sensitivity, brand loyalty, or purchase frequency, and these differences correlate with version assignment, the bundle estimate is confounded.

5. **Endogenous item selection.** The researcher "selects focal products that can appear in multiple otherwise comparable offer versions." If this selection favors items with particular demand characteristics (high volume, promotional responsiveness), the estimates may not generalize to the retailer's full product assortment.

6. **Dynamic demand effects.** If the bundled treatment generates a demand spike that cannibalizes future purchases (intertemporal substitution), the per-wave estimate overstates the net demand effect. The panel structure enables testing for this pattern but the packet provides no guidance on appropriate spacing of waves.

7. **Attention decay.** If customers are exposed to repeated waves with the same format–promotion bundle, the effect may attenuate over time. Any pooled estimate conflates early-wave and late-wave responses unless explicitly modeled.

## 17. What Cannot Be Claimed

In light of the Stage 4 critique, the following claims are explicitly disclaimed:

1. **The terminal-digit format itself causes any change in demand.** Cannot be claimed. Format and promotion are perfectly collinear; no estimate isolates the format effect. The Stage 4 critic correctly identifies that even Candidate 1's bundle estimate "cannot answer the packet's primary research question about the terminal-digit format itself."

2. **The format and promotion channels are separable through heterogeneity analysis.** Cannot be claimed. The Stage 4 critic marks Candidate 2 `not_defensible` because "the perturbed condition makes it impossible to attribute any familiarity gradient to the format channel specifically." The heterogeneity analysis is descriptive only.

3. **Item familiarity provides a mechanism probe for format-specific signaling.** Cannot be claimed. Same reason as above. Familiarity may moderate response to the format, the promotion, both, or neither; the data cannot distinguish.

4. **The bundle estimate equals the format estimate minus some promotion component.** Cannot be claimed. The bundle is not a sum of separable components; format and promotion may interact synergistically (the format amplifies the promotion's credibility, or the promotion draws attention that makes the format salient). Without independent variation, no decomposition is possible.

5. **Customer groups are randomly assigned.** Cannot be claimed. The packet states groups are "comparable," which is weaker than random assignment. The bundle estimate's causal interpretation hangs on an assumption that requires validation.

6. **Results generalize beyond the retailer's specific setting, products, and customer base.** Cannot be claimed. The packet provides no basis for external validity claims.

7. **The absence of a demand difference implies the format has no effect.** Cannot be claimed. A null bundle effect could reflect offsetting format and promotion effects, ceiling effects, or insufficient statistical power.

## 18. Additional Data Needed

To recover a credible causal estimate of the terminal-digit format effect itself, the following data or design changes are required:

1. **Independent variation of format and promotion.** The single most critical addition. A 2×2 factorial design crossing the terminal-digit format (salient ending vs. standard ending) with promotional framing (explicit markdown/sale label vs. no promotional framing) would identify the format main effect, the promotion main effect, and their interaction. This is the minimal design change needed to answer the packet's core question.

2. **A natural experiment in format exposure.** If the retailer cannot experimentally vary the format independently (e.g., because format is tied to pricing policy), an alternative is to exploit a setting where the same price ending appears both with and without promotional framing in different contexts — for example, across product categories where .99 endings are standard (not promotional) versus categories where they are used only for markdowns.

3. **Individual-level exposure and attention measures.** Customer-level tracking of which version was displayed, whether the customer viewed the price, and how long they attended to it, would enable compliance-adjusted estimates and attention-weighted heterogeneity analysis.

4. **Exogenous variation in item familiarity.** Random assignment of items to waves or a natural experiment in which exposure timing is quasi-random (e.g., item introduction dates determined by supply-chain constraints unrelated to demand) would enable causal interpretation of familiarity interactions.

5. **Detailed version-level metadata.** Systematic coding of all version features (layout template, color scheme, position on page/screen, co-displayed items, font size, presence of comparison/reference prices) to test and adjust for version-level confounds.

6. **Pre-period outcome data.** Demand for the same items in periods or waves before the format–promotion manipulation was introduced, enabling difference-in-differences or pre-trend validation.

## 19. Threat-Response Table

The packet does not explicitly request a threat-response table. However, for completeness, the key threats identified in this memo and the Stage 4 critique are summarized below with the design's response.

| Threat | Source | Severity | Response |
|---|---|---|---|
| Perfect collinearity of format and promotion | Perturbed condition | Fatal to format-effect identification | Adopt descriptive fallback; clearly disclaim format-effect claims; enumerate design changes needed |
| Estimand-target mismatch (bundle ≠ format) | Stage 4 Critic (Candidate 1) | Fatal to answering packet Question 1 | Present bundle estimate as supplementary only, with explicit caveat that it answers a different question |
| Mechanism probe logic broken by collinearity | Stage 4 Critic (Candidate 2) | Fatal to Candidate 2's core claim | Downgrade heterogeneity to descriptive; remove all mechanism-probing language |
| Version-level confound contamination | Data card spillover note; Stage 4 Critic | High for bundle estimate | Test covariate balance; apply sensitivity analysis; report version-level metadata if available |
| Assignment mechanism unverified ("comparable" ≠ random) | Packet language; Stage 4 Critic | High for bundle estimate | Conduct balance tests; report with explicit caveat about ignorability assumption |
| Endogenous item familiarity | Packet structure | High for heterogeneity interpretation | Label all familiarity-stratified results as descriptive associations; discuss selection into familiarity |
| Customer self-selection into purchase | Data card compliance note | Moderate | Frame as intention-to-treat; no individual compliance adjustment possible |
| Implicit causal framing of descriptive results | Stage 4 Critic (Candidate 3) | Moderate for primary analysis | Use explicit correlational language throughout; no causal path diagrams or structural interpretations |
| Other cues alter price interpretation | Data card spillover note | Moderate-high | Acknowledge as limitation; recommend detailed version coding in design agenda |
| Dynamic/cannibalization effects | Memo analysis | Moderate | Test for wave-attenuation patterns; include wave interactions in descriptive models |

## 20. Claim-Evidence Table

| Claim | Evidence Used | Claim Type | Confidence | What Would Falsify This Claim |
|---|---|---|---|---|
| The terminal-digit format effect itself cannot be credibly identified under the perturbed condition | Packet perturbed condition: format and promotion are perfectly collinear ("the visible ending format is no longer varied independently of bargain presentation"); Stage 4 critic confirms this is "lethal to causal identification" | Identification impossibility | High (logical necessity) | A source of independent variation in the format would need to be discovered within the packet — but the packet explicitly rules this out |
| The bundled format–promotion package effect is causally estimable under conditional ignorability of group assignment | Packet states groups are "comparable"; assignment determines displayed version; demand observed at product–version level | Causal (of the bundle, not the format) | Moderate | Balance tests showing systematic pre-existing differences between treatment and control groups on observables; sensitivity analysis showing small confounding could eliminate the estimate |
| The bundled treatment effect cannot be decomposed into format and promotion components | Packet perturbed condition; perfect collinearity precludes any statistical decomposition | Identification impossibility | High (logical necessity) | Within-packet variation in one component holding the other fixed. The packet rules this out |
| Item-familiarity heterogeneity is purely descriptive and provides no mechanism-probing traction on the format effect | Perfect collinearity makes any familiarity gradient equally consistent with format-only, promotion-only, or interactive mechanisms; Stage 4 critic marks Candidate 2 `not_defensible` | Descriptive | High | Exogenous familiarity variation plus independent format–promotion variation would enable mechanism probing — neither exists in the packet |
| Demand differences across offer versions reflect the joint influence of format, promotion, and unmeasured version-level cues | Data card spillover note: "Other cues in the same version may alter interpretation of the focal price"; Stage 4 critic highlights version-level confound threat | Descriptive/caveat | High | Systematic coding of all version features showing no differences beyond the format–promotion bundle |
| Customer-group assignment is not confirmed as random; "comparable" is weaker than random assignment | Packet language: "Comparable customer groups receive different versions"; data card: variation source is format/promotion bundling, not experimental protocol; Stage 4 critic flags this | Methodological caveat | Moderate-high | Documentation of an explicit randomization protocol or quasi-experimental assignment mechanism |
| The format effect can be recovered by independently varying format and promotional framing | Logical necessity: identification requires independent variation; the packet's Question 4 explicitly requests design-change enumeration | Design recommendation | High (logical) | Proof that under perfect collinearity a format effect can be identified without additional data, which is mathematically impossible |
| A null bundle effect does not imply the format has no effect | Format and promotion effects could offset; insufficient power; ceiling effects | Methodological caveat | High (logical) | Evidence that the format and promotion effects must have the same sign and that power is adequate to detect even small effects |
| Descriptive comparisons may mislead if implicitly framed as causal despite explicit correlational labeling | Stage 4 Critic (Candidate 3 Threat 2): "implicit causal framing" risk from unmeasured version-level confounds | Methodological caution | Moderate | Reader comprehension testing; qualitative analysis of downstream citations or interpretations |
| The analysis does not generalize beyond the retailer's setting | Packet provides only within-retailer data; no multi-retailer or multi-market variation | External validity caveat | High | Multi-retailer replication data or a formal sampling frame covering a defined population of retailers |