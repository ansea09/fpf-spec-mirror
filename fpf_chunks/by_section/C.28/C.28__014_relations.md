---
chunk_kind: "child"
pattern_id: "C.28"
pattern_title: "CausalUse-CAL: Causal-Use Questions, Identification, and Realizability"
section_id: "C.28:12"
section_title: "Relations"
source_path: "FPF-Spec.md"
output_path: "by_section/C.28/C.28__014_relations.md"
commit_sha: "3f6714ae3235e0d771dce32835be7696f626d2ee"
heading_path:
  - "C.28 — CausalUse-CAL: Causal-Use Questions, Identification, and Realizability"
  - "C.28:12 — Relations"
line_start: 56326
line_end: 56341
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

### C.28:12 - Relations

- `C.16` keeps measurements and scales; `C.27` keeps temporal-claim adequacy.
- `A.10` keeps evidence paths and provenance and may cite C.28 support components and result.
- `A.2.4` classifies how an episteme is used; it cannot promote simulation output or association into stronger causal evidence.
- `A.15` keeps Method, plan, Work, and attribution for interventions, target trials, and sampling.
- `B.3` may cite a C.28 result as one basis for a separate bounded assurance result.
- `C.11`, `C.19`, and `C.24` keep choice, pool treatment, and call planning and consume only the needed causal refs.
- `D.5` keeps bias/fairness audit and uses `BiasAuditReport@Context` when a causal fairness question is consequential or reusable.
- `G.5` keeps method dispatch; `G.9` keeps parity and benchmark conclusions; `G.11` keeps refresh planning.
- `C.26` is used only for a residual quantum-like modelling issue after ordinary causal explanations are tried.

#### C.28:12.1 - C.29 mathematical-lens relation

`C.29` may describe a mapping as abstraction-like, quotient-like, coarse-graining-like, simulation-like, or macro-model-like. It does not decide causal support. When intervention, policy, counterfactual, causal explanation, or causal decision use is current, apply C.28; otherwise record no causal-use claim or the exact blocker.

