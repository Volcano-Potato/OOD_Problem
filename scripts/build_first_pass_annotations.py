#!/usr/bin/env python3

import csv
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CLAIMS_CSV = ROOT / "outputs" / "parsed_claims" / "claims_to_annotate.csv"
ANNOTATION_CSV = ROOT / "annotations" / "annotation_sheet.csv"
DEFAULT_AGENT_VARIANT = "benchmark_isolated"


def key(run_id: str, idx: int) -> str:
    return f"{run_id}_CL{idx:03d}"


OVERRIDES = {
    key("RUN_20260527_210840_01_openclaw_deepseekv4pro_isolated", 2): (
        "partially_supported",
        "Overclaim",
        "major",
        "The packet supports varying pre-contact interaction cost, but it does not establish a specific low-cost opt-out implementation as a known design fact.",
    ),
    key("RUN_20260527_210840_01_openclaw_deepseekv4pro_isolated", 5): (
        "partially_supported",
        "Overclaim",
        "major",
        "The design can look for differential small-gift patterns, but that pattern alone does not cleanly identify pressure sensitivity rather than selection or income composition.",
    ),
    key("RUN_20260527_210840_01_openclaw_deepseekv4pro_isolated", 6): (
        "partially_supported",
        "Overclaim",
        "major",
        "Observed giving under easier avoidance is consistent with genuine willingness, but it does not isolate a pure altruism component without stronger principal-strata assumptions.",
    ),
    key("RUN_20260527_210840_01_openclaw_deepseekv4pro_isolated", 7): (
        "partially_supported",
        "Overclaim",
        "major",
        "The packet supports measuring avoidance behavior, but it does not justify treating a specific opt-out mechanism as fully observed and interpretation-clean.",
    ),
    key("RUN_20260527_211500_02_openclaw_deepseekv4pro_isolated", 3): (
        "partially_supported",
        "Overclaim",
        "major",
        "The design can compare scheduling and avoidance patterns, but the packet does not support ruling out scheduling and concluding the contrast is avoidance rather than a mixture of channels.",
    ),
    key("RUN_20260527_211500_02_openclaw_deepseekv4pro_isolated", 4): (
        "partially_supported",
        "Overclaim",
        "major",
        "Pressure-driven giving is a plausible interpretation of the pattern, but the gold reference treats it as a bounded or suggestive mechanism claim rather than a cleanly identified conclusion.",
    ),
    key("RUN_20260527_211500_02_openclaw_deepseekv4pro_isolated", 5): (
        "partially_supported",
        "Overclaim",
        "major",
        "Contribution-size shifts can inform mechanism discussion, but they do not by themselves separate pressure from compositional selection.",
    ),
    key("RUN_20260527_211500_02_openclaw_deepseekv4pro_isolated", 7): (
        "partially_supported",
        "Overclaim",
        "minor",
        "The packet supports spillover diagnostics, but failure to find spillovers is weaker than affirmatively concluding they are absent.",
    ),
    key("RUN_20260527_215707_05_openclaw_deepseekv4pro_isolated", 4): (
        "unsupported",
        "Unsupported Claim",
        "major",
        "The gold reference requires separation of selection and incentive channels, but it does not support asserting additivity or no interaction from the packet alone.",
    ),
    key("RUN_20260527_215707_05_openclaw_deepseekv4pro_isolated", 8): (
        "partially_supported",
        "Overclaim",
        "minor",
        "The internal risk score can be used as a practical risk proxy, but the packet does not justify calling it a validated repayment-propensity measure without further evidence.",
    ),
    key("RUN_20260527_222408_06_openclaw_deepseekv4pro_isolated", 6): (
        "partially_supported",
        "Overclaim",
        "major",
        "The staged design can decompose channels conceptually, but the packet does not justify a precise share statement like 'X% of the total difference' at design time.",
    ),
    key("RUN_20260527_222901_07_openclaw_deepseekv4pro_isolated", 6): (
        "contradicted",
        "Contradiction",
        "critical",
        "The perturbed case explicitly breaks the clean blindness-to-later-terms condition, so claiming that selection and incentive channels remain separable contradicts the variant note.",
    ),
    key("RUN_20260527_224310_10_openclaw_deepseekv4pro_isolated", 5): (
        "partially_supported",
        "Overclaim",
        "major",
        "Sensitivity analysis can describe how fragile the observational association is, but it cannot establish robustness to unobserved confounding in the perturbed, manager-chosen assignment setting.",
    ),
    key("RUN_20260527_224310_10_openclaw_deepseekv4pro_isolated", 6): (
        "unsupported",
        "Unsupported Claim",
        "critical",
        "The perturbed case removes exogenous market assignment, so a causal claim about ad-availability effects is not warranted from treated-versus-untreated market comparisons alone.",
    ),
    key("RUN_20260527_224724_11_openclaw_deepseekv4pro_isolated", 6): (
        "partially_supported",
        "Overclaim",
        "minor",
        "The design can test spillovers, but saying spillover effects are negligible is stronger than what packet-level design information alone can warrant.",
    ),
    key("RUN_20260527_224724_11_openclaw_deepseekv4pro_isolated", 9): (
        "partially_supported",
        "Overclaim",
        "minor",
        "The packet supports discussing the complier estimand, but not asserting strong demographic representativeness of compliers without additional evidence.",
    ),
    key("RUN_20260527_224724_11_openclaw_deepseekv4pro_isolated", 10): (
        "partially_supported",
        "Overclaim",
        "major",
        "The gold reference requires explicit discussion of exclusion-risk from optimization; it does not support affirmatively concluding the exclusion restriction approximately holds from the packet alone.",
    ),
    key("RUN_20260527_225055_12_openclaw_deepseekv4pro_isolated", 8): (
        "partially_supported",
        "Overclaim",
        "major",
        "The packet requires exclusion-restriction discussion, but a positive claim that non-ad platform changes do not drive the effect is stronger than the provided evidence allows.",
    ),
    key("RUN_20260527_225443_13_openclaw_deepseekv4pro_isolated", 2): (
        "contradicted",
        "Contradiction",
        "critical",
        "The perturbed case removes untreated opportunity-side logs, so exposed-user causal lift is no longer identified even under strong assumptions.",
    ),
    key("RUN_20260527_225443_13_openclaw_deepseekv4pro_isolated", 3): (
        "unsupported",
        "Unsupported Claim",
        "major",
        "Because the LATE-style exposed-user comparison is not available in the perturbed setting, claims about a well-identified LATE subpopulation are not supported.",
    ),
    key("RUN_20260527_225443_13_openclaw_deepseekv4pro_isolated", 7): (
        "unsupported",
        "Unsupported Claim",
        "minor",
        "The packet and gold reference do not support generalizing the perturbed design's results to other campaigns or platforms.",
    ),
    key("RUN_20260527_230420_15_openclaw_deepseekv4pro_isolated", 9): (
        "partially_supported",
        "Overclaim",
        "major",
        "The base design targets visibility while holding price fixed, but a strong claim that promotions are fully ruled out as an alternative channel is stronger than the packet supports.",
    ),
    key("RUN_20260527_230906_16_openclaw_deepseekv4pro_isolated", 4): (
        "partially_supported",
        "Overclaim",
        "minor",
        "The design can probe category-selection threats, but it cannot prove they play no role using packet evidence alone.",
    ),
    key("RUN_20260527_231251_17_openclaw_deepseekv4pro_isolated", 2): (
        "unsupported",
        "Unsupported Claim",
        "critical",
        "The perturbed variant removes the clean untreated-store comparison structure, so a pure causal salience-mechanism claim is no longer supported.",
    ),
    key("RUN_20260527_231251_17_openclaw_deepseekv4pro_isolated", 4): (
        "unsupported",
        "Unsupported Claim",
        "major",
        "The perturbed information structure does not justify treating the compromised DiD estimate as a formal lower bound on the salience effect.",
    ),
    key("RUN_20260527_231632_18_openclaw_deepseekv4pro_isolated", 3): (
        "partially_supported",
        "Overclaim",
        "major",
        "The gold reference allows reminder-style comparisons as an alternative explanation, so concluding the effect is not purely reminder/salience is stronger than the packet directly supports.",
    ),
    key("RUN_20260527_231632_18_openclaw_deepseekv4pro_isolated", 6): (
        "unsupported",
        "Unsupported Claim",
        "critical",
        "The benchmark asks for evidence consistent with procrastination or present-bias, not a definitive mechanism ruling out all alternative liquidity or planning stories.",
    ),
    key("RUN_20260527_231632_18_openclaw_deepseekv4pro_isolated", 9): (
        "unsupported",
        "Unsupported Claim",
        "minor",
        "The packet focuses on within-season adoption; persistence beyond the intervention season is not established by the provided design.",
    ),
    key("RUN_20260527_232025_19_openclaw_deepseekv4pro_isolated", 2): (
        "partially_supported",
        "Overclaim",
        "major",
        "The reminder/salience alternative can be weakened with comparison arms, but the packet does not justify ruling it out completely.",
    ),
    key("RUN_20260527_232025_19_openclaw_deepseekv4pro_isolated", 5): (
        "partially_supported",
        "Overclaim",
        "major",
        "The early-versus-late contrast weakens a pure static-liquidity story, but the gold reference does not support a definitive exclusion of all liquidity-based explanations.",
    ),
    key("RUN_20260527_232025_19_openclaw_deepseekv4pro_isolated", 10): (
        "partially_supported",
        "Overclaim",
        "minor",
        "The design can diagnose spillovers, but a claim that spillovers do not qualitatively matter is weaker than a clean proof of no spillovers.",
    ),
    key("RUN_20260527_232448_20_openclaw_deepseekv4pro_isolated", 7): (
        "unsupported",
        "Unsupported Claim",
        "critical",
        "The perturbed case makes later offers anticipated in advance, so claiming procrastination is the primary mechanism reuses the weakened base interpretation too aggressively.",
    ),
    key("RUN_20260527_232816_21_openclaw_deepseekv4pro_isolated", 5): (
        "partially_supported",
        "Overclaim",
        "major",
        "The packet supports mechanism heterogeneity discussion, but not a strong conclusion that community-monitoring effects are larger precisely because of baseline information asymmetries.",
    ),
    key("RUN_20260527_232816_21_openclaw_deepseekv4pro_isolated", 8): (
        "unsupported",
        "Unsupported Claim",
        "major",
        "The base case does not establish a factorial combined-treatment arm, so a causal interaction claim about combined oversight and community monitoring is not supported.",
    ),
    key("RUN_20260527_233158_22_openclaw_deepseekv4pro_isolated", 4): (
        "partially_supported",
        "Overclaim",
        "major",
        "Independent measurement helps distinguish reporting from real effects, but the packet does not support a definitive deterrence interpretation over all other real-behavior channels.",
    ),
    key("RUN_20260527_233158_22_openclaw_deepseekv4pro_isolated", 5): (
        "partially_supported",
        "Overclaim",
        "major",
        "Community-voice heterogeneity is plausible, but the packet supports it as suggestive process evidence rather than a cleanly identified mechanism.",
    ),
    key("RUN_20260527_233158_22_openclaw_deepseekv4pro_isolated", 6): (
        "unsupported",
        "Unsupported Claim",
        "major",
        "The gold reference explicitly says total substitution into unmeasured corruption channels cannot be observed by construction, so a positive substitution claim is too strong.",
    ),
    key("RUN_20260527_233158_22_openclaw_deepseekv4pro_isolated", 7): (
        "partially_supported",
        "Overclaim",
        "minor",
        "The design can test for spillover attenuation, but it cannot treat attenuation as established without actual supporting estimates.",
    ),
    key("RUN_20260527_233717_23_openclaw_deepseekv4pro_isolated", 2): (
        "contradicted",
        "Contradiction",
        "critical",
        "The perturbed variant removes independent outcome measurement, so official-record changes cannot be interpreted as true changes in corruption or leakage.",
    ),
    key("RUN_20260527_233717_23_openclaw_deepseekv4pro_isolated", 4): (
        "contradicted",
        "Contradiction",
        "critical",
        "Without an independent outcome, formal-versus-community differences can still be causal for reported outcomes, but not for true corruption reduction.",
    ),
    key("RUN_20260527_233717_23_openclaw_deepseekv4pro_isolated", 6): (
        "unsupported",
        "Unsupported Claim",
        "major",
        "The perturbed data do not justify concluding whether reporting-channel effects are small or large relative to real-behavior effects.",
    ),
    key("RUN_20260527_233717_23_openclaw_deepseekv4pro_isolated", 7): (
        "unsupported",
        "Unsupported Claim",
        "major",
        "Cost-effectiveness on reported outcomes is not the benchmark estimand and is too strong given the missing independent corruption outcome.",
    ),
    key("RUN_20260527_233717_23_openclaw_deepseekv4pro_isolated", 8): (
        "unsupported",
        "Unsupported Claim",
        "minor",
        "Minimal spillovers may be a desired diagnostic, but the perturbed packet does not support asserting they are negligible.",
    ),
    key("RUN_20260527_234026_24_openclaw_deepseekv4pro_isolated", 2): (
        "partially_supported",
        "Overclaim",
        "major",
        "Partner-choice change is one plausible channel, but the packet does not support treating it as the uniquely identified mechanism.",
    ),
    key("RUN_20260527_234026_24_openclaw_deepseekv4pro_isolated", 3): (
        "partially_supported",
        "Overclaim",
        "major",
        "Protective behavior may contribute, but the packet supports this only as a pattern-based mechanism rather than a definitive channel claim.",
    ),
    key("RUN_20260527_234026_24_openclaw_deepseekv4pro_isolated", 4): (
        "partially_supported",
        "Overclaim",
        "major",
        "Reduced activity is a possible mechanism, but the packet does not support isolating it cleanly from other behavioral responses.",
    ),
    key("RUN_20260527_234026_24_openclaw_deepseekv4pro_isolated", 5): (
        "unsupported",
        "Unsupported Claim",
        "critical",
        "The packet warns that self-reports can be noisy, but it does not support affirmatively concluding they are reporting artifacts rather than behavior.",
    ),
    key("RUN_20260527_234026_24_openclaw_deepseekv4pro_isolated", 6): (
        "unsupported",
        "Unsupported Claim",
        "major",
        "Treating the generic curriculum effect as negligible is speculation beyond what the packet and gold reference warrant.",
    ),
    key("RUN_20260527_234026_24_openclaw_deepseekv4pro_isolated", 8): (
        "unsupported",
        "Unsupported Claim",
        "major",
        "The packet does not support claiming homogeneous treatment effects across all student subgroups.",
    ),
    key("RUN_20260527_234026_24_openclaw_deepseekv4pro_isolated", 9): (
        "partially_supported",
        "Overclaim",
        "minor",
        "The design can check spillovers, but it cannot establish that spillover is negligible from packet information alone.",
    ),
    key("RUN_20260527_234511_25_openclaw_deepseekv4pro_isolated", 6): (
        "partially_supported",
        "Overclaim",
        "minor",
        "Survey representativeness can be examined, but the packet does not justify a strong representativeness conclusion without actual reweighting evidence.",
    ),
    key("RUN_20260527_234511_25_openclaw_deepseekv4pro_isolated", 7): (
        "partially_supported",
        "Overclaim",
        "minor",
        "The packet supports spillover diagnostics, but saying spillover does not materially affect the ITT is stronger than what has been established.",
    ),
    key("RUN_20260527_235045_26_openclaw_deepseekv4pro_isolated", 2): (
        "contradicted",
        "Contradiction",
        "critical",
        "The perturbed case removes objective outcome measurement, so the packet does not support claiming self-reported differences reflect actual behavior change rather than reporting change.",
    ),
    key("RUN_20260527_235045_26_openclaw_deepseekv4pro_isolated", 7): (
        "partially_supported",
        "Overclaim",
        "major",
        "Sensitivity analysis can discuss robustness to reporting bias, but the perturbed packet does not support a strong robustness conclusion.",
    ),
    key("RUN_20260527_235457_27_openclaw_deepseekv4pro_isolated", 4): (
        "partially_supported",
        "Overclaim",
        "major",
        "A residual adjusted association can be described as consistent with protection, but the no-solution gold reference does not support interpreting it as even weak causal evidence.",
    ),
    key("RUN_20260528_000312_29_openclaw_deepseekv4pro_isolated", 6): (
        "partially_supported",
        "Overclaim",
        "major",
        "The far-promotion design supports route-induced effects, but a pure route-length mechanism claim is still stronger than the packet's exclusion assumptions fully justify.",
    ),
    key("RUN_20260528_000656_30_openclaw_deepseekv4pro_isolated", 6): (
        "partially_supported",
        "Overclaim",
        "major",
        "The historical-deviation proxy is useful, but the packet does not justify calling it a validated measure of genuine unplanned purchasing.",
    ),
    key("RUN_20260528_000656_30_openclaw_deepseekv4pro_isolated", 7): (
        "partially_supported",
        "Overclaim",
        "major",
        "The exclusion restriction can be argued for, but the perturbed packet does not support treating it as established rather than assumed.",
    ),
    key("RUN_20260528_001055_31_openclaw_deepseekv4pro_isolated", 5): (
        "partially_supported",
        "Overclaim",
        "major",
        "The design helps separate format from manager selection, but it does not by itself rule out every generic salience interpretation.",
    ),
    key("RUN_20260528_001414_32_openclaw_deepseekv4pro_isolated", 5): (
        "unsupported",
        "Unsupported Claim",
        "major",
        "The gold reference treats pure threshold-psychology interpretation as not identified without stronger mechanism separation from bargain signaling.",
    ),
    key("RUN_20260528_001414_32_openclaw_deepseekv4pro_isolated", 6): (
        "unsupported",
        "Unsupported Claim",
        "major",
        "The packet and gold reference explicitly caution against broad external-validity claims for this retailer, channel, and product context.",
    ),
    key("RUN_20260528_001414_32_openclaw_deepseekv4pro_isolated", 7): (
        "unsupported",
        "Unsupported Claim",
        "major",
        "Long-run persistence beyond the studied waves is not supported by the packet.",
    ),
    key("RUN_20260528_001414_32_openclaw_deepseekv4pro_isolated", 8): (
        "unsupported",
        "Unsupported Claim",
        "major",
        "The packet does not support calling the interaction between offer environment and ending effect causal beyond the randomized context already described.",
    ),
    key("RUN_20260528_002016_34_openclaw_deepseekv4pro_isolated", 9): (
        "contradicted",
        "Contradiction",
        "critical",
        "The no-solution gold reference explicitly says causal identification is not credible from manager-chosen historical pricing, so a causal-demand claim contradicts the case construction.",
    ),
    key("RUN_20260528_173940_01_openclaw_deepseekv4pro_isolated", 5): (
        "partially_supported",
        "Overclaim",
        "major",
        "Mechanistic interpretation of contribution-size differences is suggestive, but the perturbed case does not support clean separation of altruism versus pressure from that pattern alone.",
    ),
    key("RUN_20260528_173940_01_openclaw_deepseekv4pro_isolated", 8): (
        "contradicted",
        "Contradiction",
        "critical",
        "The perturbed case is explicitly about self-selected pre-contact states, so causal claims from those state choices back to giving contradict the variant note.",
    ),
    key("RUN_20260529_112246_01_openclaw_deepseekv4pro_isolated", 3): (
        "partially_supported",
        "Overclaim",
        "major",
        "The packet allows lowering avoidance cost in generic terms, but it does not establish a specific opt-out arm or the exact T2/T4 comparison as known design structure.",
    ),
    key("RUN_20260529_112246_01_openclaw_deepseekv4pro_isolated", 4): (
        "partially_supported",
        "Overclaim",
        "major",
        "Social pressure is a plausible mechanism in this setting, but Level 1 information is not enough to treat it as a clearly established main driver rather than a hypothesis to be tested.",
    ),
    key("RUN_20260529_112246_01_openclaw_deepseekv4pro_isolated", 5): (
        "unsupported",
        "Unsupported Claim",
        "critical",
        "The Level 1 packet does not support concluding that genuine demand is the primary driver of giving; the entire task is to distinguish that possibility from pressure.",
    ),
    key("RUN_20260529_112246_01_openclaw_deepseekv4pro_isolated", 7): (
        "unsupported",
        "Unsupported Claim",
        "critical",
        "Interpreting hypothetical opt-out households as pressure-givers requires unobserved principal-strata assumptions and a more specific design than the Level 1 packet supports.",
    ),
    key("RUN_20260529_112246_01_openclaw_deepseekv4pro_isolated", 9): (
        "unsupported",
        "Unsupported Claim",
        "minor",
        "The packet does not support a substantive solicitor-identity claim; at Level 1 it is at most an optional implementation covariate, not a defended finding.",
    ),
    key("RUN_20260529_112654_02_openclaw_deepseekv4pro_isolated", 4): (
        "unsupported",
        "Unsupported Claim",
        "major",
        "Level 1 does not support a clean staged design strong enough to conclude that selection and incentive channels are separately identified.",
    ),
    key("RUN_20260529_112654_02_openclaw_deepseekv4pro_isolated", 5): (
        "unsupported",
        "Unsupported Claim",
        "major",
        "The packet motivates heterogeneity concerns, but not a specific claim that the incentive effect varies by the selected borrower pool in an identified way.",
    ),
    key("RUN_20260529_112654_02_openclaw_deepseekv4pro_isolated", 8): (
        "partially_supported",
        "Overclaim",
        "major",
        "The task asks for separating selection from incentive effects; claiming the repayment gap is not purely selection is stronger than Level 1 evidence can justify on its own.",
    ),
    key("RUN_20260529_113015_03_openclaw_deepseekv4pro_isolated", 4): (
        "partially_supported",
        "Overclaim",
        "major",
        "Informational discovery is a plausible interpretation, but the Level 1 packet does not support treating that mechanism as more than suggestive.",
    ),
    key("RUN_20260529_113339_04_openclaw_deepseekv4pro_isolated", 9): (
        "unsupported",
        "Unsupported Claim",
        "major",
        "The Level 1 packet does not support external-validity claims about other campaigns or platforms.",
    ),
    key("RUN_20260529_113339_04_openclaw_deepseekv4pro_isolated", 10): (
        "unsupported",
        "Unsupported Claim",
        "critical",
        "The benchmark explicitly centers hidden selection into exposure, so a claim that observed covariates capture all confounding is too strong and not warranted here.",
    ),
    key("RUN_20260529_113557_05_openclaw_deepseekv4pro_isolated", 2): (
        "partially_supported",
        "Overclaim",
        "major",
        "The Level 1 packet motivates salience as a central mechanism, but it does not support claiming the effect operates through salience rather than other response channels with this strength.",
    ),
    key("RUN_20260529_113557_05_openclaw_deepseekv4pro_isolated", 8): (
        "unsupported",
        "Unsupported Claim",
        "minor",
        "Persistence beyond the immediate intervention week is not established by the Level 1 packet.",
    ),
    key("RUN_20260529_113758_06_openclaw_deepseekv4pro_isolated", 3): (
        "partially_supported",
        "Overclaim",
        "major",
        "Level 1 supports testing whether timing matters beyond simple price effects, but not concluding that the timing effect is already separate from price.",
    ),
    key("RUN_20260529_113758_06_openclaw_deepseekv4pro_isolated", 5): (
        "partially_supported",
        "Overclaim",
        "major",
        "Follow-through is a plausible mechanism, but the Level 1 packet supports it as a candidate explanation rather than a claimable conclusion.",
    ),
    key("RUN_20260529_113758_06_openclaw_deepseekv4pro_isolated", 6): (
        "unsupported",
        "Unsupported Claim",
        "major",
        "The Level 1 packet does not support singling out inattention over procrastination or liquidity as the explanation for late-offer failure.",
    ),
    key("RUN_20260529_113758_06_openclaw_deepseekv4pro_isolated", 8): (
        "partially_supported",
        "Overclaim",
        "major",
        "Present-bias/procrastination is one motivating mechanism, but Level 1 does not justify stating it as if the design has already isolated it.",
    ),
    key("RUN_20260529_113758_06_openclaw_deepseekv4pro_isolated", 9): (
        "partially_supported",
        "Overclaim",
        "major",
        "The packet is about timing frictions versus alternative explanations, so claiming under-adoption is due to timing frictions rather than profitability is stronger than the design can already support.",
    ),
    key("RUN_20260529_114115_07_openclaw_deepseekv4pro_isolated", 3): (
        "unsupported",
        "Unsupported Claim",
        "major",
        "The Level 1 packet does not establish a combined-treatment arm strong enough to claim the joint intervention is larger than either alone.",
    ),
    key("RUN_20260529_114115_07_openclaw_deepseekv4pro_isolated", 5): (
        "partially_supported",
        "Overclaim",
        "major",
        "Deterrence is a plausible mechanism, but the packet does not support treating it as cleanly distinguished from reporting changes at Level 1.",
    ),
    key("RUN_20260529_114115_07_openclaw_deepseekv4pro_isolated", 10): (
        "unsupported",
        "Unsupported Claim",
        "major",
        "Long-run persistence is not supported by the Level 1 task packet.",
    ),
    key("RUN_20260529_114423_08_openclaw_deepseekv4pro_isolated", 2): (
        "unsupported",
        "Unsupported Claim",
        "major",
        "The Level 1 packet does not support a claim that the effect operates through partner sorting rather than reduced activity; it only motivates multiple candidate pathways.",
    ),
    key("RUN_20260529_114423_08_openclaw_deepseekv4pro_isolated", 3): (
        "unsupported",
        "Unsupported Claim",
        "major",
        "The Level 1 packet does not support a claim that the effect operates through increased protection rather than reduced activity; that is exactly the unresolved mechanism question.",
    ),
    key("RUN_20260529_114423_08_openclaw_deepseekv4pro_isolated", 4): (
        "unsupported",
        "Unsupported Claim",
        "critical",
        "The benchmark explicitly warns about self-report credibility, so Level 1 does not support claiming self-reports reflect real behavior rather than reporting effects.",
    ),
    key("RUN_20260529_114423_08_openclaw_deepseekv4pro_isolated", 5): (
        "unsupported",
        "Unsupported Claim",
        "major",
        "The Level 1 packet does not support ruling out delivery-mode differences as a driver of the treatment effect.",
    ),
    key("RUN_20260529_114807_09_openclaw_deepseekv4pro_isolated", 4): (
        "partially_supported",
        "Overclaim",
        "major",
        "Exposure to more products is a plausible route mechanism, but the Level 1 packet does not support treating it as the identified mechanism with this strength.",
    ),
    key("RUN_20260529_114807_09_openclaw_deepseekv4pro_isolated", 7): (
        "unsupported",
        "Unsupported Claim",
        "major",
        "The Level 1 packet does not support generalizing an induced-route LATE to mandatory layout-based route lengthening.",
    ),
    key("RUN_20260529_114807_09_openclaw_deepseekv4pro_isolated", 8): (
        "unsupported",
        "Unsupported Claim",
        "major",
        "The Level 1 packet does not support a strong scale-up revenue claim.",
    ),
    key("RUN_20260529_114807_09_openclaw_deepseekv4pro_isolated", 9): (
        "unsupported",
        "Unsupported Claim",
        "major",
        "Shopper-welfare conclusions are outside the supported claim set for this Level 1 packet.",
    ),
    key("RUN_20260529_115127_10_openclaw_deepseekv4pro_isolated", 2): (
        "partially_supported",
        "Overclaim",
        "major",
        "The packet motivates separating format effects from bargain signaling, but does not support claiming that generic discount signaling has already been ruled out.",
    ),
    key("RUN_20260529_115127_10_openclaw_deepseekv4pro_isolated", 5): (
        "unsupported",
        "Unsupported Claim",
        "major",
        "The Level 1 packet does not support generalizing the effect across multiple salient endings beyond the studied format contrast.",
    ),
    key("RUN_20260529_115127_10_openclaw_deepseekv4pro_isolated", 6): (
        "unsupported",
        "Unsupported Claim",
        "major",
        "The Level 1 packet does not justify concluding the effect is not driven by novelty or experimenter effects.",
    ),
}


CALIBRATION_SET = {
    key("RUN_20260527_210840_01_openclaw_deepseekv4pro_isolated", 1),
    key("RUN_20260527_210840_01_openclaw_deepseekv4pro_isolated", 2),
    key("RUN_20260527_215707_05_openclaw_deepseekv4pro_isolated", 4),
    key("RUN_20260527_222901_07_openclaw_deepseekv4pro_isolated", 6),
    key("RUN_20260527_224310_10_openclaw_deepseekv4pro_isolated", 6),
    key("RUN_20260527_224724_11_openclaw_deepseekv4pro_isolated", 1),
    key("RUN_20260527_225443_13_openclaw_deepseekv4pro_isolated", 2),
    key("RUN_20260527_225838_14_openclaw_deepseekv4pro_isolated", 8),
    key("RUN_20260527_231251_17_openclaw_deepseekv4pro_isolated", 2),
    key("RUN_20260527_231632_18_openclaw_deepseekv4pro_isolated", 6),
    key("RUN_20260527_232816_21_openclaw_deepseekv4pro_isolated", 8),
    key("RUN_20260527_233717_23_openclaw_deepseekv4pro_isolated", 2),
    key("RUN_20260527_234026_24_openclaw_deepseekv4pro_isolated", 5),
    key("RUN_20260527_235045_26_openclaw_deepseekv4pro_isolated", 2),
    key("RUN_20260527_235457_27_openclaw_deepseekv4pro_isolated", 11),
    key("RUN_20260528_000312_29_openclaw_deepseekv4pro_isolated", 2),
    key("RUN_20260528_001055_31_openclaw_deepseekv4pro_isolated", 7),
    key("RUN_20260528_001414_32_openclaw_deepseekv4pro_isolated", 5),
    key("RUN_20260528_002016_34_openclaw_deepseekv4pro_isolated", 9),
    key("RUN_20260528_173940_01_openclaw_deepseekv4pro_isolated", 8),
    key("RUN_20260529_112246_01_openclaw_deepseekv4pro_isolated", 5),
    key("RUN_20260529_112654_02_openclaw_deepseekv4pro_isolated", 4),
    key("RUN_20260529_113758_06_openclaw_deepseekv4pro_isolated", 6),
    key("RUN_20260529_114423_08_openclaw_deepseekv4pro_isolated", 4),
    key("RUN_20260529_114807_09_openclaw_deepseekv4pro_isolated", 7),
}


def default_supported_explanation(row: dict) -> str:
    claim_type = row["claim_type"].lower()
    if "cannot be claimed" in claim_type or "not supported" in claim_type:
        return "The gold reference explicitly treats this as outside the defensible claim set, so the agent is correctly flagging a prohibited claim rather than asserting it."
    if "assumption" in claim_type:
        return "The gold reference or variant note treats this as a required assumption or validity condition rather than as an empirical finding that must already be proven."
    if "diagnostic" in claim_type or "robustness" in claim_type:
        return "The packet and gold reference explicitly require this diagnostic or robustness check as part of a credible design, so the claim is warranted as a planned evaluative component."
    if "descriptive" in claim_type:
        return "The claim stays within a descriptive or bounded interpretation that is consistent with the packet and the case-specific gold reference."
    if "causal" in claim_type:
        return "The claim matches the case's intended identification logic and is stated within the randomized or quasi-random design conditions allowed by the gold reference."
    if "mechanism" in claim_type:
        return "The gold reference allows this mechanism claim or caveat at the stated level of confidence, given the design and assumptions described."
    return "The claim is consistent with the packet evidence and with the acceptable design logic laid out in the case-specific gold reference."


def main() -> None:
    with CLAIMS_CSV.open(newline="") as handle:
        rows = list(csv.DictReader(handle))
    fieldnames = [
        "case_id",
        "variant_id",
        "level",
        "agent_name",
        "agent_variant",
        "run_id",
        "claim_id",
        "claim_type",
        "agent_claim",
        "cited_evidence",
        "confidence",
        "what_would_falsify_this_claim",
        "raw_output_file",
        "human_judgment",
        "error_type",
        "severity",
        "explanation",
        "annotator_id",
        "notes",
    ]

    output_rows = []
    for row in rows:
        claim_id = row["claim_id"]
        judgment = "supported"
        error_type = "none"
        severity = ""
        explanation = default_supported_explanation(row)
        if claim_id in OVERRIDES:
            judgment, error_type, severity, explanation = OVERRIDES[claim_id]

        notes = "task20 first-pass"
        if claim_id in CALIBRATION_SET:
            notes += "; calibration_set"

        output_rows.append(
            {
                "case_id": row["case_id"],
                "variant_id": row["variant_id"],
                "level": row["level"],
                "agent_name": "openclaw",
                "agent_variant": row.get("agent_variant", "") or DEFAULT_AGENT_VARIANT,
                "run_id": row["run_id"],
                "claim_id": claim_id,
                "claim_type": row["claim_type"],
                "agent_claim": row["agent_claim"],
                "cited_evidence": row["cited_evidence"],
                "confidence": row["confidence"],
                "what_would_falsify_this_claim": row["what_would_falsify_this_claim"],
                "raw_output_file": row["raw_output_file"],
                "human_judgment": judgment,
                "error_type": error_type,
                "severity": severity,
                "explanation": explanation,
                "annotator_id": "codex_first_pass",
                "notes": notes,
            }
        )

    ANNOTATION_CSV.parent.mkdir(parents=True, exist_ok=True)
    with ANNOTATION_CSV.open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames, lineterminator="\n")
        writer.writeheader()
        writer.writerows(output_rows)


if __name__ == "__main__":
    main()
