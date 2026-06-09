---
chunk_kind: "child"
pattern_id: "C.28"
pattern_title: "CausalUse-CAL: Causal-Use Questions, Causality-Ladder Rungs, Identification and Realizability"
section_id: "C.28:5"
section_title: "Archetypal Grounding"
source_path: "FPF-Spec.md"
output_path: "by_section/C.28/C.28__007_archetypal-grounding.md"
commit_sha: "093d30e806a1466e24032733eb020bb5a5f585cc"
heading_path:
  - "C.28 — CausalUse-CAL: Causal-Use Questions, Causality-Ladder Rungs, Identification and Realizability"
  - "C.28:5 — Archetypal Grounding"
line_start: 50260
line_end: 50277
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
  - "Pearl Causal Hierarchy"
  - "Structural Causal Model"
  - "association"
  - "causal diagram"
  - "causal estimand"
  - "causal evidence support basis"
  - "causal fairness"
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

**Tell.** A causal-use claim is a promise about what a reader may do with a result. The claim is safe only when the rung, contrast, support basis, and allowed use are named.

**Show (System).** A product team observes that users who received an intervention had better outcomes. `C.28` first records an observational association unless the team can name an interventional-action design, target trial protocol, identification profile, or evidence design that supports intervention-effect use. If the team only has observational association, the next move is to publish association or build evidence, not to claim causal improvement.

**Show (Episteme).** A fairness report says one model is fair because a metric improved after a policy change. `C.28` asks whether the fairness claim is associative, interventional, or counterfactual. If it is interventional-action-rung only, it cannot be published as counterfactual fairness without identification or realizability support.

**Show (Policy).** A team wants to deploy a causal policy learned from logged behavior data. `C.28` records `causalPolicyClaim`, `interventionalActionRung` or `counterfactualComparisonRung` as appropriate, `CausalActionPolicyClass`, `OffPolicyCausalEvaluationProfile`, support/overlap checks, uncertainty, supported policy use, and unsupported policy use. If the behavior policy cannot support the target policy, the admissible output is bounded use or abstain rather than "the policy is optimal".

**Show (Causal RL).** An online learner uses behavior-policy logs and counterfactual data-fusion to choose a treatment, ranking, or action policy. `C.28` records the natural behavior policy, evaluation policy, `CausalActionPolicyClass`, target rung, confounding/support assumptions, `OffPolicyCausalEvaluationProfile`, uncertainty, supported policy use, and unsupported policy use. The learner may publish bounded causal policy support only for the declared regime; it must not turn replay reward, exploration success, or counterfactual strategy output into an unqualified optimal-action claim.

**Show (Evidence Work).** A lab can physically run a counterfactual-rung sampling procedure by assigning compatible action regimes to matched units under ethical and operational constraints. `C.28` separates `CounterfactualSamplingRealizabilityProfile` from `CausalIdentificationProfile`: the realized sampling work becomes `U.Work` with evidence carriers and guards, while identification remains the inferential route from assumptions, graph, calculus, and available data.

**Show (Simulation-Only).** A simulator produces "what would have happened" traces for a rollout decision. `C.28` can allow useful model-supported use without calling the traces realized counterfactual-rung evidence: the record uses `simulationOnlyCounterfactualOutputBasis`, names `counterfactualModelAssumptionSetRef`, `simulationValidationRef`, supported simulation use, and unsupported use. The output may support rehearsal, sensitivity exploration, or model-based explanation inside declared limits; it does not support direct counterfactual sample wording or intervention-effect publication by vocabulary alone.

**Show (Benchmark).** A benchmark compares one observational predictor, one intervention optimizer, and one counterfactual strategy. `C.28` does not ban the comparison, but it requires `CausalMethodRungParityRecord` through `G.9`: if rung, `estimandRef`, interventional-action basis, support basis, consumed `C.28` support record and verdict, transportability, follow-up window, and estimation-validity basis are not comparable, the benchmark publishes bridge and loss relation, degraded use, or abstain instead of one superiority claim.

