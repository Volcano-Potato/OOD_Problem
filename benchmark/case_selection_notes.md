# Case Selection Notes

## Selection Goal

Task 04 freezes a practical case pool for the first version of OOD-CausalDesignBench:

- 20 available candidate cases are kept in `benchmark/case_registry.csv`.
- 5 pilot cases are selected for early construction and protocol debugging.
- 10 main-set cases are selected for the main benchmark.

The selection prioritizes cases that expose scientific-agent weaknesses in causal research design, especially:

- missing non-obvious identification linchpins
- confusing causal effects with mechanisms
- treating endogenous exposure as randomized
- trusting contaminated or manipulable outcomes
- ignoring assignment/outcome/inference levels
- overclaiming when identification is weak

## Frozen Pilot Set

The pilot set is intentionally small but covers four primary failure modes. It should be used to test the full construction pipeline before building all main cases.

| case_id | anonymous setting | domain | design_family | key_failure_mode | diagnostic_value | memorization_risk | selected_for |
|---|---|---|---|---|---|---|---|
| `C001` | charitable giving and social pressure | `behavioral` | `mechanism_experiment` | `mechanism_confounding` | Tests whether the agent can design a low-cost avoidance channel to distinguish altruism or warm glow from social pressure rather than only randomizing solicitation. | medium | pilot + main |
| `C002` | consumer credit information asymmetry | `consumer_finance` | `factorial_RCT` | `mechanism_confounding` | Tests whether the agent can separate adverse selection from moral hazard using multi-stage price and contract variation rather than saying "randomize interest rates." | medium | pilot + main |
| `C005` | online advertising exposure measurement | `platform_economics` | `field_experiment` | `endogenous_exposure` | Tests whether the agent understands that observed ad exposure is endogenous and that the relevant counterfactual is exposure opportunity not naive exposed-vs-unexposed comparison. | medium | pilot + main |
| `C008` | retail tax salience | `public_econ` | `DID` | `timing_endogeneity` | Tests whether the agent moves beyond before-after comparison to a treated-category by control-category by store by time design with correct inference. | medium | pilot + main |
| `C014` | public-project corruption monitoring | `political_econ` | `field_experiment` | `measurement_error` | Tests whether the agent notices that official records may be manipulable and that independent outcome measurement is part of the design. | medium | pilot + main |

### Why `C010` Is Main But Not Pilot

`C010` is highly valuable and remains in the main set, but the pilot already contains several mechanism-separation cases. Replacing it with `C014` makes the pilot cover measurement error, which is required for diagnosing a common agent failure: treating institutionally produced outcomes as clean evidence.

## Frozen Main Set

The main set contains 10 cases. It keeps all pilot cases and adds harder or broader cases in development, health, marketing, and IV/endogenous-exposure settings.

| case_id | anonymous setting | domain | design_family | key_failure_mode | diagnostic_value | memorization_risk | selected_for |
|---|---|---|---|---|---|---|---|
| `C001` | charitable giving and social pressure | `behavioral` | `mechanism_experiment` | `mechanism_confounding` | Exposes whether the agent can identify a mechanism-separating behavioral design rather than generic treatment randomization. | medium | pilot + main |
| `C002` | consumer credit information asymmetry | `consumer_finance` | `factorial_RCT` | `mechanism_confounding` | Exposes whether the agent understands that adverse selection and moral hazard require different randomized margins. | medium | pilot + main |
| `C004` | paid search advertising effectiveness | `platform_economics` | `field_experiment` | `endogenous_exposure` | Exposes whether the agent handles search intent and consumer heterogeneity instead of treating ad clicks or exposure as exogenous. | medium | main |
| `C005` | retargeting ad measurement | `platform_economics` | `field_experiment` | `endogenous_exposure` | Exposes whether the agent recognizes exposure-opportunity endogeneity and the need for a ghost-ad-like counterfactual. | medium | pilot + main |
| `C008` | retail tax salience | `public_econ` | `DID` | `timing_endogeneity` | Exposes whether the agent uses the correct comparison structure and avoids unsupported before-after causal claims. | medium | pilot + main |
| `C010` | fertilizer adoption timing | `development` | `mechanism_experiment` | `mechanism_confounding` | Exposes whether the agent shifts from price-level logic to timing friction and present-bias mechanism design. | medium | main |
| `C014` | public-project monitoring and corruption | `political_econ` | `field_experiment` | `measurement_error` | Exposes whether the agent designs independent outcome measurement rather than trusting potentially manipulated official accounts. | medium | pilot + main |
| `C016` | health-risk information intervention | `health` | `field_experiment` | `measurement_error` | Exposes whether the agent chooses hard outcomes and handles social-desirability bias instead of relying on self-reported behavior. | medium | main |
| `C019` | in-store travel path and unplanned spending | `marketing` | `IV` | `endogenous_exposure` | Exposes whether the agent treats shopping paths as choice-driven and articulates a credible source of exogenous variation rather than running OLS. | medium | main |
| `C020` | retail price endings | `marketing` | `field_experiment` | `mechanism_confounding` | Exposes whether the agent separates psychological price-ending effects from low-price or sale-signal mechanisms and handles product-level assignment. | medium | main |

## Candidate Pool With Inclusion Decisions

| case_id | domain | design_family | key_failure_mode | diagnostic_value | memorization_risk | selected_for |
|---|---|---|---|---|---|---|
| `C001` | `behavioral` | `mechanism_experiment` | `mechanism_confounding` | Social-pressure mechanism requires an avoidance or opt-out contrast. | medium | pilot + main |
| `C002` | `consumer_finance` | `factorial_RCT` | `mechanism_confounding` | Multi-stage credit terms are needed to separate adverse selection from moral hazard. | medium | pilot + main |
| `C003` | `labor` | `mechanism_experiment` | `mechanism_confounding` | Competition-choice design must separate preferences from ability, risk, and confidence. | high | reserve |
| `C004` | `platform_economics` | `field_experiment` | `endogenous_exposure` | Paid-search effectiveness is confounded by consumer search intent and prior brand demand. | medium | main |
| `C005` | `platform_economics` | `field_experiment` | `endogenous_exposure` | Ad effectiveness requires comparing users with similar exposure opportunity rather than observed exposure. | medium | pilot + main |
| `C006` | `health` | `mechanism_experiment` | `selection` | Price effects on health-product use require separating selection from sunk-cost behavior. | medium | reserve |
| `C007` | `health` | `mechanism_experiment` | `selection` | Purchase is not usage; real-use outcomes are needed to separate screening from sunk-cost mechanisms. | medium | reserve |
| `C008` | `public_econ` | `DID` | `timing_endogeneity` | Tax-salience design requires cross-product, cross-store, and over-time contrasts. | medium | pilot + main |
| `C009` | `consumer_finance` | `factorial_RCT` | `mechanism_confounding` | Advertising content, loan price, and deadline effects must be separated. | medium | reserve |
| `C010` | `development` | `mechanism_experiment` | `mechanism_confounding` | Fertilizer adoption requires identifying timing friction and present bias rather than price level alone. | medium | main |
| `C011` | `labor` | `audit_experiment` | `measurement_error` | Resume audit is useful as a sanity check but too famous for main claims. | high | reserve |
| `C012` | `behavioral` | `natural_experiment` | `timing_endogeneity` | Fine introduction and withdrawal tests social-norm crowd-out and persistence. | high | reserve |
| `C013` | `education` | `field_experiment` | `mechanism_confounding` | Gain versus loss framing requires economically equivalent incentive arms. | medium | reserve |
| `C014` | `political_econ` | `field_experiment` | `measurement_error` | Corruption measurement requires independent engineering or audit-style outcomes. | medium | pilot + main |
| `C015` | `development` | `mechanism_experiment` | `mechanism_confounding` | Learning design must separate having information from noticing the relevant relationship. | medium | reserve |
| `C016` | `health` | `field_experiment` | `measurement_error` | Health-risk information needs hard outcomes to reduce self-report and social-desirability bias. | medium | main |
| `C017` | `energy` | `field_experiment` | `spillover` | Social-norm reports require heterogeneity and boomerang-effect reasoning. | medium | reserve |
| `C018` | `marketing` | `field_experiment` | `mechanism_confounding` | Norm intervention requires reference-group specificity rather than generic social-norm messaging. | high | reserve |
| `C019` | `marketing` | `IV` | `endogenous_exposure` | In-store path length is behaviorally chosen and needs credible exogenous variation. | medium | main |
| `C020` | `marketing` | `field_experiment` | `mechanism_confounding` | Price-ending effects must be separated from sale cue and low-price signaling. | medium | main |

## Exclusion And Reserve Logic

Cases marked reserve are not rejected. They are held for later expansion, ablations, or appendix examples.

| case_id | reason not in main v1 |
|---|---|
| `C003` | High memorization risk and overlaps with mechanism-confounding capability already covered by C001, C002, C010, and C020. |
| `C006` | Strong case, but health-product selection is partly covered by C016 and mechanism separation is already dense in the main set. |
| `C007` | Similar diagnostic role to C006; useful if the project later emphasizes public replication data. |
| `C009` | Strong consumer-finance marketing case, but C002 already covers credit mechanism design and C004/C005 cover advertising/platform measurement. |
| `C011` | Very high leakage risk because the resume-audit design is widely known; keep as sanity check rather than main evidence. |
| `C012` | Famous and distinctive setup creates memory risk; useful later for natural-experiment/timing variants. |
| `C013` | Good education/incentive case, but main v1 prioritizes business/platform/marketing OOD relevance. |
| `C015` | Useful development mechanism case, but overlaps with C010 on mechanism reasoning and is less central to business OOD framing. |
| `C017` | Good spillover/heterogeneity case, but main v1 already reaches 10 cases and prioritizes advertising/marketing/measurement. |
| `C018` | High leakage risk and overlaps with C001 on social-pressure/norm mechanism reasoning. |

## Coverage Check

### Pilot Coverage

| criterion | result |
|---|---|
| number of pilot cases | 5 |
| primary failure modes | `mechanism_confounding`, `endogenous_exposure`, `timing_endogeneity`, `measurement_error` |
| domains | `behavioral`, `consumer_finance`, `platform_economics`, `public_econ`, `political_econ` |
| design families | `mechanism_experiment`, `factorial_RCT`, `field_experiment`, `DID` |
| high memorization-risk cases | 0 |
| all have local PDFs | yes |

### Main Coverage

| criterion | result |
|---|---|
| number of main cases | 10 |
| domains | `behavioral`, `consumer_finance`, `platform_economics`, `public_econ`, `development`, `political_econ`, `health`, `marketing` |
| subdomains | charitable_giving, consumer_credit, search_advertising, retargeting_advertising, tax_salience, agricultural_adoption, public_project_monitoring, health_information, retail_navigation, retail_pricing |
| design families | `mechanism_experiment`, `factorial_RCT`, `field_experiment`, `DID`, `IV` |
| primary failure modes | `mechanism_confounding`, `endogenous_exposure`, `timing_endogeneity`, `measurement_error` |
| marketing or platform advertising cases | `C004`, `C005`, plus marketing cases `C019`, `C020` |
| mechanism decomposition cases | `C001`, `C002`, `C010`, `C020` |
| measurement-error or manipulable-outcome cases | `C014`, `C016` |
| high memorization-risk cases | 0 |
| all have local PDFs | yes |

## Memorization Risk Policy

High-risk classic papers are useful for debugging because humans know what a correct answer should look like. They are not used in the main set because they can inflate performance if the agent has memorized the source paper.

For main cases:

- remove paper titles, author names, original places, named organizations, and distinctive treatment labels
- avoid exact sample sizes and exact dates unless needed for design logic
- rewrite the setting as a generic anonymous business/economics problem
- keep the identification challenge intact even when surface details are generalized

## Task 04 Completion Checklist

- [x] Pilot set contains exactly 5 cases.
- [x] Main set contains exactly 10 cases.
- [x] Pilot set covers at least 4 primary failure modes.
- [x] Main set covers at least 5 domains or subdomains.
- [x] Main set includes at least 2 marketing or platform-advertising cases.
- [x] Main set includes at least 2 mechanism-decomposition cases.
- [x] Main set includes at least 1 measurement-error or manipulable-outcome case.
- [x] Every selected case has a local PDF path in `benchmark/case_registry.csv`.
