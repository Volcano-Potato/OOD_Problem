<!-- visibility: evaluator-only -->
<!-- do_not_include_in_agent_context: true -->
<!-- case_id: C020 -->

# Source Facts: C020

## Scope

These facts are extracted only from `source_packet.md`. They are evaluator-only inputs for later `gold_reference.md` and anonymized task construction.

## Research Context

| fact_id | category | fact | evidence_id | confidence |
|---|---|---|---|---|
| F001 | research_context | The empirical setting is consumer retail pricing, where managers want to know whether a salient terminal-digit price format increases demand. | [P001], [P003] | high |
| F002 | research_question | The source asks whether 9-ending prices increase demand and whether the effect depends on customer information, item familiarity, and promotional context. | [P001], [P002], [P005] | high |
| F003 | benchmark_objective | The benchmark objective is to force the agent to distinguish a genuine price-ending effect from low-price or sale-signal mechanisms. | [P001], [P002], [P005] | high |
| F004 | central_threat | A naive comparison of odd-ending and non-odd-ending prices can confound terminal-digit format with markdown cues, low-price signaling, item familiarity, and manager-chosen pricing. | [P002], [P005], [P008] | high |

## Data Structure

| fact_id | field | extracted fact | evidence_id | confidence |
|---|---|---|---|---|
| F005 | observation_unit | The design centers on item offers shown to randomly assigned customer samples, with realized demand measured after exposure. | [P004], [P007], [P009] | high |
| F006 | assignment_level | Treatment is assigned at the product-offer-version level and delivered through customer-sample randomization. | [P007], [P009] | high |
| F007 | outcome_measurement_level | Outcomes are measured through item-level demand or units sold after customers receive the offer version. | [P001], [P004], [P006] | high |
| F008 | clustering_or_inference_level | Inference should respect product-offer or customer-sample assignment rather than treating each realized transaction as independently randomized. | [P007], [P009] | medium |
| F009 | time_span | The source uses multiple field experiments across repeated merchandising waves rather than a single laboratory session. | [P001], [P006], [P010] | medium |
| F010 | panel_or_repeated_observations | Some items are new while others have appeared in previous periods, creating a repeated-history dimension that matters for heterogeneity. | [P001], [P005] | high |
| F011 | sample_construction | Separate customer samples receive different offer versions containing identical items priced with different endings or nearby price alternatives. | [P004], [P007], [P009] | high |
| F012 | treatment_exposure_variable | The focal treatment is whether an offer uses a salient terminal-digit ending rather than a nearby alternative ending. | [P001], [P004], [P007] | high |
| F013 | outcome_variable | The core outcome is product-level demand or units purchased for the focal item offer. | [P001], [P004], [P006] | high |
| F014 | covariates | Relevant controls include item familiarity or prior appearance, customer-segment information if available, and whether sale or discount cues accompany the price. | [P001], [P002], [P005] | high |
| F015 | missingness_or_noncompliance | Some operational constraints limit which prices or pages can be changed, so treatment coverage may be partial rather than universal across all items. | [P010] | medium |
| F016 | spillover_risk | Spillovers can arise if customers compare items within the same offer or if pricing changes on some items alter perceptions of the whole offer. | [P007], [P010] | medium |

## Treatment / Variation / Exposure

| fact_id | category | fact | evidence_id | confidence |
|---|---|---|---|---|
| F017 | randomized_variation | The source uses experimentally assigned offer versions rather than historical manager-chosen prices. | [P001], [P007], [P008], [P009] | high |
| F018 | price_ending_manipulation | In the main design, treatment versions often remove the salient 9 ending from the retailer's standard pricing format. | [P004], [P007] | high |
| F019 | moderator_item_history | The effectiveness of the ending format is studied separately for new items versus items sold in previous years. | [P001], [P005] | high |
| F020 | moderator_sale_cue | The effect may be weaker when explicit sale cues already tell customers that the item is discounted. | [P001], [P005] | high |

## Outcomes And Measurement

| fact_id | outcome | measurement_method | evidence_id | confidence |
|---|---|---|---|---|
| F021 | demand | Demand is measured through realized purchases or units sold for the focal offer. | [P001], [P004], [P006] | high |
| F022 | comparative_demand | The design compares demand for identical items across different pricing versions rather than across different products. | [P004], [P007] | high |
| F023 | absolute_price_change | Some manipulated prices differ by several dollars, so the design is not limited to tiny cent-level changes. | [P004], [P006] | high |

## Identification Logic

| fact_id | component | extracted fact | evidence_id | confidence |
|---|---|---|---|---|
| F024 | design_family | The source design is a field experiment that randomizes price endings across otherwise comparable offer versions. | [P001], [P007], [P008] | high |
| F025 | source_of_variation | The key identifying variation comes from experimentally assigning customer samples to different offer versions for identical items. | [P007], [P009] | high |
| F026 | comparison_group | The main comparison is between customer samples that see the same item under different terminal-digit pricing formats. | [P004], [P007] | high |
| F027 | why_historical_pricing_fails | Historical manager-chosen prices are endogenous because managers choose which items, contexts, and markdowns receive particular endings. | [P008], [P010] | high |
| F028 | mechanism_question | A strong design must separate terminal-digit effects from low-price or sale-signal interpretations. | [P002], [P005] | high |
| F029 | heterogeneity_question | The effect should be allowed to differ for new items and previously familiar items. | [P001], [P005] | high |

## Linchpin Details

| linchpin_id | detail | why_it_matters | what_fails_without_it | evidence_id | confidence |
|---|---|---|---|---|---|
| L001 | The design must rely on experimentally assigned price-ending variation, not observational differences in existing prices. | Manager-chosen pricing is endogenous to item quality, markdown strategy, and expected demand. | A historical price-ending regression cannot isolate a causal ending effect. | [P007], [P008], [P009] | high |
| L002 | The design must distinguish terminal-digit format from generic low-price or sale cues. | A measured effect could otherwise reflect discount signaling rather than the ending itself. | The agent may overclaim a pure psychological threshold effect when the true mechanism is confounded. | [P001], [P002], [P005] | high |
| L003 | Item familiarity or prior appearance matters for interpretation and should enter either the design or the heterogeneity analysis. | The source itself finds stronger effects for newer items, which supports an information-based interpretation. | Ignoring familiarity can hide the mechanism and produce misleading pooled claims. | [P001], [P002], [P005] | high |

## Robustness / Placebo / Mechanism Checks

| fact_id | check_type | extracted fact | evidence_id | confidence |
|---|---|---|---|---|
| F030 | same_item_comparison | The source compares identical items across different offer versions, reducing cross-item confounding. | [P004], [P007] | high |
| F031 | new_vs_familiar_items | Heterogeneity by prior item appearance is a core mechanism check rather than an optional flourish. | [P001], [P005] | high |
| F032 | sale_cue_moderation | The design or interpretation should consider whether explicit sale cues reduce or absorb the ending effect. | [P001], [P005] | high |
| F033 | operational_constraint_check | Real-world restrictions on which prices can be manipulated mean design feasibility and sample restrictions should be discussed explicitly. | [P010] | medium |

## Naive Design Failure Modes

| failure_id | naive_design | why_it_fails | evidence_id | confidence |
|---|---|---|---|---|
| N001 | Regress demand on existing odd-ending prices in historical data and call the coefficient causal. | Historical use of the ending format is chosen by managers and may be correlated with unobserved demand conditions and markdown strategy. | [P008], [P010] | high |
| N002 | Compare items with different endings without matching identical products or comparable versions. | Cross-item differences can reflect assortment, style, quality, or placement rather than the terminal digit. | [P004], [P007] | high |
| N003 | Interpret an observed ending effect as pure threshold psychology without addressing sale cues or discount signaling. | The source explicitly notes weaker effects when sale cues are present. | [P001], [P005] | high |
| N004 | Ignore item familiarity and pool new and familiar items into one unconditional effect. | The source highlights stronger effects for new items. | [P001], [P005] | high |
| N005 | Treat each purchase as independently randomized without respecting assignment at the offer-version level. | Randomization operates at the version and sample-assignment level, not at each realized transaction. | [P007], [P009] | medium |

## Evaluator Inference

| inference_id | inference | basis_evidence_id | use_in_later_tasks |
|---|---|---|---|
| I001 | Agent-facing packets should preserve randomized offer-version logic and mechanism confounding, but should avoid the exact "$9", catalog, and zip-based implementation details. | [P001], [P007], [P009] | leakage control |
| I002 | Full-credit answers should require either a direct randomized ending-format experiment or an equally strong exogenous product-offer design. | [P007], [P008], [P009] | gold reference |
| I003 | New-item heterogeneity and sale-cue moderation should appear in Level 3 or gold as mechanism-relevant structure, not as source-identifying trivia. | [P001], [P005] | level design |

## Uncertainties

| uncertainty_id | uncertainty | evidence_id | consequence |
|---|---|---|---|
| U001 | It is not fully fixed whether a clean factorial design separating ending format and sale cue should be required for full credit, or whether a strong discussion of mechanism confounding is enough. | [P001], [P005] | Gold reference should allow both, but it should penalize answers that ignore the confounding entirely. |
| U002 | The source packet does not fully quantify how much of the treatment effect survives after conditioning on familiarity and sale cues. | [P001], [P002], [P005] | Agent-facing packets should ask for mechanism separation without leaking exact effect sizes. |
| U003 | Operational constraints on price manipulation are present but not fully detailed in the source packet. | [P010] | Level 3 should mention implementation limits and partial coverage without overfitting to the source. |

## Facts Safe For Agent-Facing Packets

- A retailer can experimentally vary terminal-digit price format across otherwise comparable offer versions.
- Demand is observed at the item-offer or transaction level after exposure.
- Item familiarity or prior appearance may moderate the effect.
- Explicit markdown or sale cues may confound the interpretation of any measured ending effect.
- Historical manager-chosen prices are not by themselves a credible causal design.

## Facts Unsafe For Agent-Facing Packets

- Source-paper title, authors, venue, exact year.
- Exact "$9" phrasing as the canonical source form if it becomes too identifying.
- Exact catalog titles, product categories, customer-address randomization details, and exact sample counts.
- Exact pilot-study quantities, exact page restrictions, and exact effect magnitudes.
