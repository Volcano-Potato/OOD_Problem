# Case Taxonomy and Metadata Schema

## Purpose

This schema defines the case-level metadata used by OOD-CausalDesignBench. Its job is not to describe papers for a literature review. Its job is to make benchmark construction, agent runs, annotation, and grouped error analysis reproducible.

Every case should be classifiable by:

- application domain
- plausible design family
- main weakness the case is meant to expose
- task difficulty under anonymized information
- leakage risk
- planned variants

The schema should remain stable once Task 04 freezes the final case pool. If a new field is needed later, add it as a new column rather than changing the meaning of an existing column.

## Case Registry Columns

| field | required | definition | allowed format |
|---|---:|---|---|
| `case_id` | yes | Stable benchmark case identifier. It should not encode author names or titles. | `C001`, `C002`, ... |
| `paper_key` | yes | Internal source-paper key used by the benchmark builder. This is evaluator-facing metadata and should never be shown to the agent. | `author_year_shorttopic` |
| `short_name` | yes | Short human-readable internal label for coordination. This should remain evaluator-only if it reveals the source paper. | lowercase snake case |
| `domain` | yes | Application area of the research problem, not the identification method. | one value from `domain` enum |
| `subdomain` | no | More specific business/economics setting for later qualitative analysis. | lowercase snake case |
| `design_family` | yes | Broad family of empirically defensible designs that a strong answer might propose. This is not the same as the failure mode. | one value from `design_family` enum |
| `variation_source` | yes | Where identifying variation comes from in the source case. This helps distinguish "randomized message" from "self-selected exposure" and similar traps. | one value from `variation_source` enum |
| `assignment_level` | yes | Level at which treatment or exposure is assigned or varies. This is needed for inference and spillover checks. | one value from `unit_level` enum |
| `outcome_level` | yes | Level at which the main outcome is measured. It may differ from `assignment_level`. | one value from `unit_level` enum |
| `unit_of_observation` | yes | Main row-level unit in the likely analysis dataset. This may be finer than assignment level. | one value from `unit_level` enum |
| `key_failure_mode` | yes | Primary agent weakness this case is designed to test. Pick one main mode even if several are relevant. | one value from `key_failure_mode` enum |
| `secondary_failure_modes` | no | Additional likely errors. Use pipe-separated values so the CSV remains easy to parse. | `mode1|mode2` |
| `difficulty` | yes | Expected difficulty of the anonymized research-design task, based on hiddenness of the identification condition, not the paper's publication rank. | `easy`, `medium`, `hard` |
| `leakage_risk` | yes | Risk that an agent can identify the original paper from the anonymized task packet. | `low`, `medium`, `high` |
| `variant_plan` | yes | Variants planned for this case. Use pipe-separated values. | values from `variant_type` enum |
| `selected_for_pilot` | yes | Whether this case should be included in the first pilot run. | `yes` or `no` |
| `selected_for_main` | yes | Whether this case is currently recommended for the main benchmark. This can change in Task 04. | `yes` or `no` |
| `source_pdf` | yes | Relative path to the source PDF used for gold-reference extraction. | relative file path |
| `has_replication_data` | yes | Whether the current source list identifies public replication material. This is useful but not required because the benchmark evaluates design reasoning, not code replication. | `yes`, `no`, or `unknown` |
| `notes` | no | Short evaluator-facing note explaining the key linchpin or construction risk. Avoid commas to keep the CSV simple. | short text without commas |

## Enumerations

### `domain`

Use one primary application domain.

| value | definition | examples |
|---|---|---|
| `marketing` | Consumer response, pricing, advertising, retail, platform measurement, or promotion design. | paid search, mobile coupons, price endings |
| `consumer_finance` | Credit, loan offers, financial marketing, repayment, or information asymmetry in lending. | consumer credit field experiments |
| `labor` | Worker, applicant, teacher, or labor-market behavior. | audit resumes, competition choice, teacher incentives |
| `public_econ` | Taxation, public finance, regulation, or public policy salience. | tax salience |
| `behavioral` | Behavioral mechanism where the main object is preferences, pressure, norms, attention, loss aversion, or present bias. | social pressure, fines, competition preference |
| `development` | Low- and middle-income country development questions not primarily health-only. | fertilizer adoption, agricultural learning |
| `health` | Health product adoption, health information, or health behavior. | bed nets, water disinfectant, HIV risk information |
| `education` | School, student, teacher, or classroom interventions. | teacher incentives |
| `platform_economics` | Online platform measurement, auction/exposure systems, recommendation systems, or digital marketplace behavior. | retargeting ads, search ads |
| `political_econ` | Corruption, governance, public monitoring, or political institutions. | audit probability for public projects |
| `energy` | Energy use, conservation, or utility behavior. | household energy reports |

If a case plausibly fits multiple domains, choose the domain that best describes the business/economic setting being tested. For example, online advertising should usually be `platform_economics` rather than generic `marketing` if exposure endogeneity is central.

### `design_family`

Use the broad design a strong response should consider. This is not a grading answer by itself; the gold reference will define the exact acceptable and unacceptable designs.

| value | definition |
|---|---|
| `RCT` | Simple randomized controlled trial where one primary treatment is randomized and the key causal claim follows directly if compliance and measurement are handled. |
| `factorial_RCT` | Multiple treatments or treatment dimensions are randomized to separate mechanisms or interactions. |
| `field_experiment` | Real-world intervention with randomization or controlled treatment variation, but operational details are central. |
| `audit_experiment` | Randomized profiles, resumes, messages, or applications are sent to real-world decision makers to measure discriminatory or differential response. |
| `mechanism_experiment` | Design must separate two or more mechanisms, not just estimate an average treatment effect. |
| `DID` | Difference-in-differences using treated and control units over time. |
| `event_study` | Dynamic treatment timing design with pre-trend and post-treatment effect checks. |
| `IV` | Instrumental variables design where a source of exogenous variation affects treatment or exposure but not outcomes except through that treatment. |
| `RDD` | Regression discontinuity design around a cutoff or eligibility threshold. |
| `natural_experiment` | Quasi-experimental design based on institutional shocks, rules, or timing not directly randomized by researchers. |
| `no_solution` | The anonymized task intentionally lacks credible identifying variation for causal inference. |

### `variation_source`

This field makes the source of identifying variation explicit.

| value | definition |
|---|---|
| `researcher_randomization` | Treatment is randomized by researchers. |
| `factorial_randomization` | Multiple treatment dimensions are independently randomized. |
| `encouragement_randomization` | Randomization changes incentives or encouragement but treatment take-up remains partly behavioral. |
| `platform_randomization` | A platform or firm randomizes exposure or eligibility. |
| `institutional_rule` | Variation comes from a policy rule, eligibility threshold, boundary, or timing rule. |
| `policy_timing` | Variation comes from staggered or time-specific policy implementation. |
| `market_exposure` | Observed treatment/exposure is generated by market behavior or user choice and is potentially endogenous. |
| `measurement_design` | The key design issue is how the outcome or exposure is measured, not just assignment. |
| `none` | No credible exogenous variation is available in the task packet. |

### `unit_level`

Use these values for `assignment_level`, `outcome_level`, and `unit_of_observation`.

| value | definition |
|---|---|
| `individual` | Person, applicant, consumer, donor, student, worker, teacher, or farmer. |
| `household` | Household-level treatment or outcome. |
| `firm` | Firm-level treatment or outcome. |
| `store` | Store, branch, shop, hotel, catalog cell, or retail location. |
| `product` | Product, category, SKU, item, or listing. |
| `ad_impression` | Impression, ad opportunity, click opportunity, or exposure event. |
| `transaction` | Purchase, loan, donation, repayment, or other transaction event. |
| `classroom` | Classroom, school-grade cell, or teacher-class unit. |
| `village` | Village, community, neighborhood, or local public-project unit. |
| `region` | Region, district, market, or geographic unit above village/store. |
| `time_period` | Day, week, month, season, or campaign period. |
| `panel_unit_time` | Repeated unit-by-time observation such as household-week or product-store-week. |

### `key_failure_mode`

Pick the single weakness the case is primarily intended to expose.

| value | definition | typical agent error |
|---|---|---|
| `endogenous_exposure` | Exposure is related to latent demand, targeting, search intent, risk, or selection. | Treating exposed and unexposed units as comparable. |
| `selection` | Take-up or observed treatment status selects particular units. | Interpreting purchaser/non-purchaser differences as treatment effects. |
| `mechanism_confounding` | The design estimates an effect but cannot distinguish competing mechanisms without additional arms or timing. | Claiming to identify altruism, pressure, selection, or sunk cost without the needed contrast. |
| `measurement_error` | Outcome or treatment measurement is self-reported, manipulable, or institutionally contaminated. | Treating official records or self-reports as clean causal outcomes. |
| `spillover` | Treatment can affect untreated units or change equilibrium behavior. | Ignoring interference between households, stores, classrooms, or markets. |
| `attrition` | Missing outcomes, nonresponse, or dropout may be treatment-related. | Ignoring differential follow-up or missing usage checks. |
| `non_compliance` | Assignment differs from actual treatment received or treatment intensity. | Reporting treatment-on-treated effects without addressing compliance. |
| `timing_endogeneity` | Timing of exposure or adoption is tied to expected outcomes or anticipation. | Running before-after or event studies without checking timing assumptions. |
| `weak_identification` | Proposed design lacks sufficient identifying variation or diagnostic support. | Proposing DID, IV, or RDD with missing assumptions or no valid source of variation. |
| `overclaim` | The task supports a weaker descriptive claim but the agent states a strong causal or mechanism claim. | Inventing causal identification in no-solution cases. |
| `inference_mismatch` | Assignment and outcome levels differ and standard errors or effective sample size are mishandled. | Clustering at the wrong level or treating individual rows as independent. |

### `difficulty`

Difficulty is about what the anonymized packet requires the agent to infer.

| value | rule | example |
|---|---|---|
| `easy` | The assignment mechanism is explicit and the main risk is applying standard design discipline. A competent answer should identify the design family from Level 2. | audit experiment with randomized names and resume quality |
| `medium` | The design family is visible, but the answer must notice one non-obvious detail such as assignment level, comparison group, compliance, or measurement. | store-product-week DID for tax salience |
| `hard` | The core research value comes from a hidden linchpin, mechanism separation, endogenous exposure correction, or no-solution honesty. A generic RCT/DID/OLS answer should fail. | ghost ads, adverse selection vs moral hazard, social pressure opt-out |

### `leakage_risk`

Leakage risk is about benchmark contamination, not causal difficulty.

| value | definition | handling |
|---|---|---|
| `low` | The anonymized task can remove most identifying details without destroying the design problem. | Suitable for main benchmark. |
| `medium` | The case is known or has a distinctive design, but careful paraphrasing can reduce direct lookup risk. | Use with stronger anonymization and no unique phrases. |
| `high` | The case is very famous or has a highly distinctive setup that may be recognized from memory. | Prefer for pilot, sanity check, or appendix rather than main claims. |

### `variant_type`

| value | definition |
|---|---|
| `level1` | Background and research objective only. Used to test whether the agent can structure the problem without full data details. |
| `level2` | Background plus Data Card. Used to test whether data structure changes design reasoning. |
| `level3` | Background, Data Card, institutional details, and threat hints. Used to test whether errors persist even with enough information. |
| `perturbed` | A counterfactual variant where one key identification condition is changed or removed. |
| `no_solution` | A variant intentionally lacking credible causal identification. Correct behavior is to refuse strong causal claims and propose descriptive analysis or needed new data. |

## Recommended Grouping Variables

The main quantitative analysis should group agent performance by:

- `domain`
- `design_family`
- `key_failure_mode`
- `difficulty`
- `variant_type`
- `leakage_risk`

Secondary analysis can group by:

- `variation_source`
- `assignment_level`
- `outcome_level`
- whether `assignment_level` equals `outcome_level`
- whether the case has `has_replication_data = yes`

## Construction Rules

1. `domain` must describe the empirical setting, not the method. Use `platform_economics` for ad-exposure cases where targeting and exposure measurement are central.
2. `design_family` should describe what a strong answer could defensibly use, not what a weak agent is likely to say.
3. `key_failure_mode` should be the main weakness the case is meant to reveal. Put extra risks in `secondary_failure_modes`.
4. `difficulty` should be assigned after imagining the anonymized Level 2 packet. Do not rank difficulty by journal prestige or mathematical complexity.
5. `leakage_risk` should be reassessed after anonymization. Famous cases can become usable if the task removes title-specific wording, location names, and unique institutional phrases.
6. `variant_plan` should include `level1|level2|level3` for every main case unless there is a clear reason not to. Add `perturbed` and `no_solution` when the case has a clean condition to remove or invert.
7. Do not expose `paper_key`, `short_name`, `source_pdf`, or source-paper details to the agent-facing task packet.

## Five-Case Schema Trial

These five trial rows test whether the schema covers the planned main benchmark:

| case_id | source pattern | domain | design_family | key_failure_mode | why schema covers it |
|---|---|---|---|---|---|
| `C001` | social-pressure charitable giving field experiment | `behavioral` | `mechanism_experiment` | `mechanism_confounding` | The schema captures that the hard part is distinguishing altruism or warm glow from social pressure, not merely randomizing solicitation. |
| `C002` | consumer-credit information asymmetry experiment | `consumer_finance` | `factorial_RCT` | `mechanism_confounding` | The schema captures multi-stage randomization and mechanism separation between adverse selection and moral hazard. |
| `C005` | retargeting or online advertising effectiveness | `platform_economics` | `field_experiment` | `endogenous_exposure` | The schema captures exposure endogeneity and the distinction between ad opportunity, actual exposure, and conversion outcome. |
| `C008` | tax salience in retail purchases | `public_econ` | `DID` | `timing_endogeneity` | The schema captures store-product-week structure and the need for treated categories, control categories, stores, and time comparisons. |
| `C010` | fertilizer timing and present-bias intervention | `development` | `mechanism_experiment` | `mechanism_confounding` | The schema captures that the key design is timing/friction rather than simply lowering price. |

This trial suggests the schema can cover the current candidate pool while preserving the variables needed for later grouped error statistics.

## Task 02 Completion Checklist

- [x] Every registry field has an operational definition.
- [x] Domain, design, failure-mode, difficulty, leakage, unit, and variant enums are defined.
- [x] At least five candidate papers can be filled without adding ad hoc fields.
- [x] The schema separates application domain from identification method.
- [x] The schema separates design family from intended failure mode.
- [x] The schema supports grouped statistics by domain, design family, and key failure mode.
