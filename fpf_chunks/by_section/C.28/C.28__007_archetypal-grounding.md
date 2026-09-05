---
chunk_kind: "child"
pattern_id: "C.28"
pattern_title: "CausalUse-CAL: Causal-Use Questions, Identification, and Realizability"
section_id: "C.28:5"
section_title: "Archetypal Grounding"
source_path: "FPF-Spec.md"
output_path: "by_section/C.28/C.28__007_archetypal-grounding.md"
commit_sha: "9fba9529833b4e288fa149878b22a9ee44e1886f"
heading_path:
  - "C.28 — CausalUse-CAL: Causal-Use Questions, Identification, and Realizability"
  - "C.28:5 — Archetypal Grounding"
line_start: 57118
line_end: 57135
dependencies:
  - "A.10"
  - "A.15"
  - "A.2.4"
  - "A.3.2"
  - "A.6"
  - "B.3"
  - "C.11"
  - "C.16"
  - "C.19"
  - "C.24"
  - "C.26"
  - "C.27"
  - "D.5"
  - "G.11"
  - "G.5"
  - "G.9"
keywords:
  - "CausalUseSupportResult"
  - "Pearl Causal Hierarchy"
  - "Structural Causal Model"
  - "association"
  - "causal diagram"
  - "causal estimand"
  - "causal fairness"
  - "causal support components"
  - "causal-RL evaluation"
  - "causal-use question"
  - "causality ladder"
  - "counterfactual"
  - "counterfactual sampling realizability"
  - "identification"
  - "intervention"
  - "off-policy causal evaluation"
  - "target trial"
---

### C.28:5 - Archetypal Grounding

**System.** A product team observes better outcomes among recipients of X. Triage returns association support. If the team needs an effect claim, it opens identification or evidence-design work; C.28 does not let the observation decide deployment.

**Fairness.** A report claims counterfactual fairness after a policy change. C.28 identifies the rung and estimand, exposes the additional counterfactual-identifiability assumptions, and cites an estimate with its consistency result when the audit relies on that estimate. Missing identification or consistency lowers the support result even with more of the same data. D.5 carries the `BiasAuditReport@Context` and makes the audit conclusion.

**Policy.** Logged behaviour data are used to evaluate a new policy. The result names both policies, horizon, confounding and overlap checks, transport endpoints when changed, estimate and uncertainty, supported regime, and unsupported unqualified optimality. C.11 or another policy pattern makes the choice.

**Causal RL.** An online learner combines logged behaviour, interventions, and a counterfactual-data source. The sampling-realizability result explains whether that source can be produced; dated Work and the resulting data path show whether it was produced; a separate identification or estimate result says what follows from it. Replay reward does not become an optimal-action claim.

**Evidence Work.** A lab's `CounterfactualSamplingRealizabilityResult` cites its decision Method and positive construction. That result supports planning but claims no sample. The later WorkPlan remains prospective. After sampling, the lab cites dated Work, attribution, and the resulting data in an A.10 evidence path before using `realizedCounterfactualSamplingData`. Identification from those data remains a separate result.

**Simulation.** A simulator supports rehearsal and sensitivity analysis under named assumptions and validation. The support result blocks realized-sample and intervention-effect wording. A pure simulator-output report exits C.28 earlier.

**Transport.** The population is unchanged but the care environment and measurement mechanism differ. The transport result names source and target environments and data-generating regimes, then states the assumptions and formula. A population ref alone would miss the shift.

**Benchmark.** G.9 compares an observational predictor, intervention optimizer, and counterfactual policy only after it checks rung, estimand, support components, window, and endpoints. The admissible result may be a selected set or abstention rather than a scalar winner.

