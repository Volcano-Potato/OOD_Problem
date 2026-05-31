# Agent Design Memo

## Research Question
Does offering small, early purchase-facilitating opportunities to producers—compared to later, economically comparable or more generous offers—increase seasonal input adoption, and is the pattern more consistent with procrastination or present-bias than with simple static demand for subsidies? ---

## Target Estimand


## Treatment And Outcomes


## Identification Logic
The central challenge is disentangling timing effects from bundled convenience and liquidity effects. The early offer (T1) bundles three features: early timing, economic benefit (price reduction), and reduced acquisition friction (convenience). An observed T1 advantage over C could reflect any combination of these. The arm structure disassembles this bundle: - T1 vs. T2 isolates timing while holding economic value and convenience constant. - T1 vs. T3 isolates the economic/convenience bundle from pure early salience. - T2 vs. T4 isolates subsidy magnitude while holding timing and convenience constant. A secondary challenge is liquidity as a confound for timing. Even if T1 > T2, this could mean that producers spend their liquidity quickly and lack funds later, not that they procrastinate. The design partially addresses this through baseline liquidity measurement and heterogeneity analysis

## Defensibility Assessment
Yes, credible causal identification of the ITT effects of each arm on adoption is possible. The researcher controls random assignment, the input is familiar (ruling out learning/uncertainty confounds that plague new-technology adoption studies), and the multi-arm structure enables informative contrasts. Causal identification of specific mechanisms (procrastination, present-bias, liquidity) is more tentative. The arm contrasts can rule out some mechanisms and provide patterns consistent with others, but no single contrast cleanly isolates, say, present-bias from a liquidity-smoothing story without additional assumptions. The design's strength is in narrowing the set of plausible explanations, not in uniquely identifying one mechanism. ---

## Proposed Design
### 9.1 Randomization Producers are block-randomized into the five arms. Stratification variables should include: - Prior input adoption (binary: ever adopted before or not). - Baseline liquidity proxy (e.g., harvest timing relative to offer, asset index). - Geographic community (to ensure within-community balance across arms, which also aids spillover measurement). ### 9.2 Primary Specification: ITT Effects on Adoption The core analysis estimates the effect of arm assignment on actual seasonal input adoption using a linear probability model (or logistic regression with marginal effects; the linear specification is preferred for transparency and ease of interpretation with interaction terms): Adopt_i = α + Σ_{k=1}^{4} β_k · Arm_{ki} + γ'X_i + δ_s + ε_i Where: - Adopt_i is a binary indicator for producer i purchasing or using the input in the target season. - Arm_{ki} are indicators for T1 through T4, with C as the omitted reference category. - X_i is a vector of baseline covariates (prior adoption, farm size, asset index, harvest timing, etc.). - δ_s are stratum fixed effects. - Standard errors clustered at the producer level (or at the operational randomization cluster level if assignment was grouped). The coefficients β_1 through β_4 are the ITT estimates. ### 9.3 Mechanism-Iso

## What Cannot Be Claimed
1. "Procrastination causes low adoption." The design can produce patterns consistent with procrastination (T1 > T2, T3 = 0, T1 > T4 despite T4 being more generous) but cannot uniquely identify procrastination as the causal mechanism because liquidity dissipation, framing, and other channels produce overlapping predictions. 2. "Present-bias (β < 1) rather than naïveté drives the result." Distinguishing sophisticated from naïve procrastinators requires data on demand for commitment devices or predictions about one's own future behavior, which are not in the packet's data structure. 3. "The early offer is welfare-improving." Without a structural model and data on producer utility, the design can only speak to behavioral responses, not welfare. An increase in adoption does not imply a welfare gain if producers would have been better off not adopting. 4. "The results generalize to other input
