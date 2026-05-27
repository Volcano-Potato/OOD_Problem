<!-- visibility: evaluator-only -->
<!-- do_not_include_in_agent_context: true -->
<!-- case_id: C020 -->

# Gold Reference: C020

## Hidden Answer Summary

This evaluator-only gold reference defines what a valid answer must handle for the price-ending field-experiment case. A strong answer does not need to reproduce the exact source implementation, but it must recognize that the clean design uses experimentally assigned ending-format variation on otherwise comparable offers and that a causal interpretation requires separating terminal-digit format from sale or markdown signaling.

## Core Research Problem

- Research question: Does a salient terminal-digit price ending increase demand, and how does the effect vary with item familiarity and sale-cue context? Evidence: F001-F004, F019-F020.
- Benchmark objective: Design a study that identifies the causal demand effect of terminal-digit pricing format while handling mechanism confounding from low-price or markdown signals. Evidence: F003-F004, F024-F029.
- Target estimand: Incremental effect of assigning a salient terminal-digit ending to an otherwise comparable offer on item-level demand. Evidence: F012-F013, F021-F023.
- Treatment or exposure: Experimentally assigned ending format for the same item across different offer versions. Evidence: F017-F018, F024-F026.
- Outcome: Item-level demand, purchases, or units sold after exposure. Evidence: F013, F021-F022.
- Unit of analysis: Item-offer exposure or offer-version demand outcome, with realized purchases observed after assignment. Evidence: F005-F007, F011.

## Data Structure

- Observation unit: Item-offer exposure or product demand outcome under a specific offer version. Evidence: F005, F011.
- Assignment level: Product-offer-version level delivered through randomized customer samples. Evidence: F006, F017, F025.
- Outcome measurement level: Item-level demand or transaction-level purchases aggregated back to the treated offer. Evidence: F007, F013, F021.
- Time structure: Repeated field experiments across merchandising waves, with a distinction between new and previously offered items. Evidence: F009-F010, F019.
- Required comparison structure: Same or otherwise highly comparable items shown under different ending formats, preferably with orthogonal variation in sale cues or at least explicit handling of sale-cue confounding. Evidence: F022, F028, F032.
- Current uncertainty: The gold should allow either a direct randomized ending-format experiment or a stronger factorial version that cleanly separates ending format from sale labeling. Evidence: U001.

## Original Identification Logic

The source uses a field-experimental design in which otherwise identical items are shown under different price-ending versions to randomly assigned customer samples. This eliminates the main endogeneity problem of historical pricing, where managers choose which items receive particular endings. The central interpretation challenge is not assignment validity but mechanism validity: even with randomized pricing versions, a measured demand effect could reflect a low-price or sale signal rather than a pure terminal-digit effect. The paper therefore treats item familiarity and sale-cue context as key moderators. Evidence: F017-F020, F024-F029.

## Linchpin Detail

- Linchpin 1: The design must use experimentally assigned ending-format variation rather than observational historical pricing. Evidence: L001.
- Why it matters: Manager-chosen odd-ending prices are endogenous to markdown policy, demand expectations, and item characteristics. Evidence: F024-F027.
- What fails without it: A historical regression cannot isolate a causal price-ending effect. Evidence: N001.
- Linchpin 2: The design must separate terminal-digit format from low-price or sale-cue interpretation. Evidence: L002.
- Why it matters: Otherwise the study may identify a general promotional signal rather than a specific price-ending effect. Evidence: F020, F028, F032.
- What fails without it: A strong claim about psychological threshold pricing becomes overstated or wrong. Evidence: N003.
- Linchpin 3: Item familiarity or prior appearance should enter the analysis as a moderator or mechanism check. Evidence: L003.
- Why it matters: The source's interpretation depends in part on stronger effects for newer items. Evidence: F019, F029.
- What fails without it: The agent may miss the information-based mechanism and produce a misleading pooled interpretation. Evidence: N004.

## Must-Have Conditions

- The answer must explicitly state that historical manager-chosen ending formats are not by themselves causally interpretable.
- The answer must propose randomized or otherwise exogenous variation in ending format across otherwise comparable offers.
- The answer must use demand or purchases for the focal item as the core outcome rather than generic store-level revenue alone.
- The answer must discuss mechanism confounding from sale cues, markdown labeling, or low-price signaling.
- The answer must either incorporate item familiarity or explain why the available design cannot separately identify that heterogeneity.

## Acceptable Alternative Designs

| design | conditions under which it is acceptable | supports what claim | cannot support what claim |
|---|---|---|---|
| Randomized offer-version experiment that varies the terminal-digit format for the same item across customer samples | Assignment must be randomized and the focal item must remain otherwise comparable across versions. | Can identify the causal effect of ending format on demand for the studied offer context. | Cannot by itself prove a pure psychological mechanism if markdown or sale cues also change. |
| Factorial randomized design varying ending format and sale cue independently | Both dimensions must be orthogonally assigned or otherwise cleanly separated. | Can identify the average ending-format effect and test whether sale cues moderate or absorb it. | Cannot automatically generalize beyond the studied retailer or product categories. |
| Randomized design stratified by new versus previously offered items | Assignment must remain randomized within item-history strata. | Can test whether effects are stronger for less familiar items. | Cannot prove that familiarity is the only mechanism without ruling out correlated differences. |

## Common Invalid Designs

| design or claim | why unacceptable | error label |
|---|---|---|
| Regress observed sales on historical odd-ending prices and interpret the coefficient causally. | Ending-format assignment is manager-chosen and endogenous. Evidence: N001, L001. | Endogenous Pricing Error |
| Compare different items with different endings without matching identical or comparable products. | Cross-item demand differences confound format with product characteristics. Evidence: N002. | Product Confounding |
| Claim that any observed treatment effect proves a pure threshold-psychology mechanism. | The effect may instead reflect sale or low-price signaling. Evidence: N003, L002. | Mechanism Confounding |
| Ignore item newness or prior appearance. | The source explicitly treats familiarity as a major moderator. Evidence: N004, L003. | Heterogeneity Omission |
| Treat each transaction as independently randomized without accounting for version-level assignment. | Randomization occurs at the offer-version and sample-assignment level. Evidence: N005. | Inference Mismatch |

## Claim-Evidence Expectations

| expected claim | required supporting evidence | claim type | confidence |
|---|---|---|---|
| Historical pricing alone cannot identify the price-ending effect. | F024-F027, L001 | limitation / identification | high |
| A valid causal design needs exogenous variation in ending format for comparable offers. | F017-F018, F024-F026, L001 | identification | high |
| Any interpretation must address whether the ending works by signaling a bargain or sale. | F020, F028, F032, L002 | mechanism / limitation | high |
| Item familiarity can legitimately moderate the treatment effect. | F019, F029, L003 | heterogeneity / mechanism | high |

## Scoring Notes

- Full-credit answer: Uses randomized or equally strong exogenous ending-format variation, compares otherwise comparable offers, treats sale-cue confounding as central, and includes item familiarity as a moderator or explicit limitation.
- Partial-credit answer: Proposes a valid experiment but underdevelops the mechanism-confounding discussion or does not clearly address new-versus-familiar item heterogeneity.
- Critical omission: Fails to distinguish ending-format effects from sale signaling, or relies on historical pricing data without exogenous variation.
- Automatic failure: Claims causal threshold-pricing effects from observational pricing patterns alone or ignores product comparability entirely.
