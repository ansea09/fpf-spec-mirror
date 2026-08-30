---
chunk_kind: "child"
pattern_id: "C.28"
pattern_title: "CausalUse-CAL: Causal-Use Questions, Identification, and Realizability"
section_id: "C.28:10"
section_title: "Rationale"
source_path: "FPF-Spec.md"
output_path: "by_section/C.28/C.28__012_rationale.md"
commit_sha: "8bb4989c9be7fa4b33f0bb7537e4611676ee3087"
heading_path:
  - "C.28 — CausalUse-CAL: Causal-Use Questions, Identification, and Realizability"
  - "C.28:10 — Rationale"
line_start: 56908
line_end: 56913
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

### C.28:10 - Rationale

Temporal change, a higher metric, a convincing graph, or a plausible simulator can all be useful without supporting a causal effect. Conversely, observational data can support a causal estimate when an explicit identification result closes the inferential gap. C.28 therefore separates the question from the components that support it and separates that evidential conclusion from downstream authority.

The integrated contract is deliberately plural: SCM and graphical methods, potential outcomes, target-trial practice, design-based identification, causal ML, transport, causal representation learning, causal RL, and causal fairness may supply different specialist results. None is installed as the universal method.

