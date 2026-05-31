# Published Design Memo

## Research Question
Research question: Does a salient terminal-digit price ending increase demand, and how does the effect vary with item familiarity and sale-cue context? Evidence: F001-F004, F019-F020.

## Target Estimand
Target estimand: Incremental effect of assigning a salient terminal-digit ending to an otherwise comparable offer on item-level demand. Evidence: F012-F013, F021-F023.

## Treatment And Outcomes
- Treatment or exposure: Experimentally assigned ending format for the same item across different offer versions. Evidence: F017-F018, F024-F026.
- Outcome: Item-level demand, purchases, or units sold after exposure. Evidence: F013, F021-F022.
- Unit of analysis: Item-offer exposure or offer-version demand outcome, with realized purchases observed after assignment. Evidence: F005-F007, F011.

## Identification Logic
The source uses a field-experimental design in which otherwise identical items are shown under different price-ending versions to randomly assigned customer samples. This eliminates the main endogeneity problem of historical pricing, where managers choose which items receive particular endings. The central interpretation challenge is not assignment validity but mechanism validity: even with randomized pricing versions, a measured demand effect could reflect a low-price or sale signal rather than a pure terminal-digit effect. The paper therefore treats item familiarity and sale-cue context as key moderators. Evidence: F017-F020, F024-F029.

## Key Data Structure
- Observation unit: Item-offer exposure or product demand outcome under a specific offer version. Evidence: F005, F011.
- Assignment level: Product-offer-version level delivered through randomized customer samples. Evidence: F006, F017, F025.
- Outcome measurement level: Item-level demand or transaction-level purchases aggregated back to the treated offer. Evidence: F007, F013, F021.
- Time structure: Repeated field experiments across merchandising waves, with a distinction between new and previously offered items. Evidence: F009-F010, F019.
- Required comparison structure: Same or otherwise highly comparable items shown under different ending formats, preferably with orthogonal variation in sale cues or at least explicit handling of sale-cue confounding. Evidence: F022, F028, F032.
- Current uncertainty: The gold should allow either a direct randomized ending-format experiment or a stronger factorial version that cleanly separates ending format from sale labeling. Evidence: U001.

## Linchpin Conditions
- Linchpin 1: The design must use experimentally assigned ending-format variation rather than observational historical pricing. Evidence: L001.
- Why it matters: Manager-chosen odd-ending prices are endogenous to markdown policy, demand expectations, and item characteristics. Evidence: F024-F027.
- What fails without it: A historical regression cannot isolate a causal price-ending effect. Evidence: N001.
- Linchpin 2: The design must separate terminal-digit format from low-price or sale-cue interpretation. Evidence: L002.
- The answer must explicitly state that historical manager-chosen ending formats are not by themselves causally interpretable.
- The answer must propose randomized or otherwise exogenous variation in ending format across otherwise comparable offers.
- The answer must use demand or purchases for the focal item as the core outcome rather than generic store-level revenue alone.
- The answer must discuss mechanism confounding from sale cues, markdown labeling, or low-price signaling.

## Defensibility Assessment
Linchpin 1: The design must use experimentally assigned ending-format variation rather than observational historical pricing. Evidence: L001. Why it matters: Manager-chosen odd-ending prices are endogenous to markdown policy, demand expectations, and item characteristics. Evidence: F024-F027. The answer must explicitly state that historical manager-chosen ending formats are not by themselves causally interpretable. The answer must propose randomized or otherwise exogenous variation in ending format across otherwise comparable offers.

## Proposed Design
- Treatment or exposure: Experimentally assigned ending format for the same item across different offer versions. Evidence: F017-F018, F024-F026.
- Outcome: Item-level demand, purchases, or units sold after exposure. Evidence: F013, F021-F022.
- Unit of analysis: Item-offer exposure or offer-version demand outcome, with realized purchases observed after assignment. Evidence: F005-F007, F011.
- Required comparison structure: Same or otherwise highly comparable items shown under different ending formats, preferably with orthogonal variation in sale cues or at least explicit handling of sale-cue confounding. Evidence: F022, F028, F032.
- Current uncertainty: The gold should allow either a direct randomized ending-format experiment or a stronger factorial version that cleanly separates ending format from sale labeling. Evidence: U001.
- The answer must explicitly state that historical manager-chosen ending formats are not by themselves causally interpretable.
- The answer must propose randomized or otherwise exogenous variation in ending format across otherwise comparable offers.

## What Cannot Be Claimed Or Omitted
- Regress observed sales on historical odd-ending prices and interpret the coefficient causally. Why invalid: Ending-format assignment is manager-chosen and endogenous. Evidence: N001, L001.
- Compare different items with different endings without matching identical or comparable products. Why invalid: Cross-item demand differences confound format with product characteristics. Evidence: N002.
- Claim that any observed treatment effect proves a pure threshold-psychology mechanism. Why invalid: The effect may instead reflect sale or low-price signaling. Evidence: N003, L002.
- Ignore item newness or prior appearance. Why invalid: The source explicitly treats familiarity as a major moderator. Evidence: N004, L003.
