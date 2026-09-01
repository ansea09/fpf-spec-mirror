---
chunk_kind: "child"
pattern_id: "C.28"
pattern_title: "CausalUse-CAL: Causal-Use Questions, Identification, and Realizability"
section_id: "C.28:2"
section_title: "Problem"
source_path: "FPF-Spec.md"
output_path: "by_section/C.28/C.28__004_problem.md"
commit_sha: "3c3f968398a938bc10e83da22d509b7b8f642d83"
heading_path:
  - "C.28 — CausalUse-CAL: Causal-Use Questions, Identification, and Realizability"
  - "C.28:2 — Problem"
line_start: 56310
line_end: 56319
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

### C.28:2 - Problem

Three collapses produce most causal overclaim:

1. **Rung collapse:** observation, intervention, and counterfactual comparison are treated as the same question.
2. **Support collapse:** data regime, identification, estimation, direct sampling, and simulation are treated as one alternative-valued “basis”.
3. **Authority collapse:** an evidential conclusion is treated as publication, choice, deployment, fairness, or assurance authority.

C.28 keeps those distinctions visible while allowing a cheap stop.

