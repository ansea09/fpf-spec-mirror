---
chunk_kind: "child"
pattern_id: "A.19.USCM"
pattern_title: "Unified Scoring Mechanism, USCM"
section_id: "A.19.USCM:5"
section_title: "Archetypal Grounding — informative"
source_path: "FPF-Spec.md"
output_path: "by_section/A.19.USCM/A.19.USCM__007_archetypal-grounding-informative.md"
commit_sha: "4ce2f7202e12c5c519a3466f5e07fe0b92e78a44"
heading_path:
  - "A.19.USCM — Unified Scoring Mechanism, USCM"
  - "A.19.USCM:5 — Archetypal Grounding — informative"
line_start: 38039
line_end: 38068
dependencies:
keywords:
  - "CG-Spec.MinimalEvidence"
  - "CSLC-lawful transforms"
  - "ScaleComplianceProfile (SCP)"
  - "ScoringMethodDescription"
  - "score profile"
  - "scoring"
  - "tri-state admissibility (pass"
---

### A.19.USCM:5 - Archetypal Grounding — informative

#### A.19.USCM:5.1 - Tell

Think of USCM as **admissibility‑gated scoring**:

* Input: “an admitted profile of measures for this exact bearer, criteria, scope and window, comparison basis, evidence policy, and result use, plus the CN-Spec and CG-Spec editions that declare those bounds”
* Output: “a set of score measures that downstream steps may compare/select on”

The key didactic boundary is: **USCM is allowed to transform measures only within the admissibility surface (SCP+CSLC), and it must not hide normalization, aggregation, or ordering.**

#### A.19.USCM:5.2 - Show — U.System

A program manager evaluates competing rollout plans for a product launch.

* The admitted profile includes measures like `{Cost, LeadTime, Reliability, RiskExposure, CarbonPerUnit}`.
* The CG-Spec's SCP states the allowed transforms and their output meanings. A rescaling that preserves a ratio chart uses a positive factor; an interval-chart conversion uses its admissible affine rule. A different scoring function declares its score Scale and valuation instead of claiming that any monotone function preserves the original quantity.
* USCM runs `Score(...)` and outputs a score profile such as `{UtilityScore, RiskScore}` rather than forcing a single number.
* A plan lacks sufficient evidence for RiskExposure. In this constructed case the declared method can return a bounded risk-score interval from the available inputs, and the effective failure policy permits that qualified output. ScoreEligibility returns degrade only if the non-evidence conditions still hold. Audit retains the interval meaning, limitation and CN/CG editions. If the method has no defined result on the available inputs, the result is abstain instead.

A downstream comparison can use that interval only under a rule that accepts its meaning and uncertainty. The audit identifies the grounds; it does not supply a missing comparison rule.

#### A.19.USCM:5.3 - Show — U.Episteme

A research lead compares several model families for deployment across heterogeneous environments.

* Indicators include calibration and robustness metrics; scoring is done using a calibrated probabilistic score plus uncertainty‑aware score dimensions.
* A chosen scoring method may require monotonicity or interpretability, as in the additive and lattice examples below. A separate prediction-uncertainty account may supply an interval under its own method and conditions; its interval is not another name for a vector of score dimensions.
* The declared score profile retains each score dimension and any justified uncertainty representation. Unknown input is not replaced by a point score. Downstream comparison explicitly handles the actual scalar, vector or interval meanings it consumes.

