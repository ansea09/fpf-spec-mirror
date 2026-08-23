---
chunk_kind: "child"
pattern_id: "C.28"
pattern_title: "CausalUse-CAL: Causal-Use Questions, Identification, and Realizability"
section_id: "C.28:1"
section_title: "Problem Frame"
source_path: "FPF-Spec.md"
output_path: "by_section/C.28/C.28__003_problem-frame.md"
commit_sha: "5801dc610c657ac7b1efee349b18e80ce6d7df6f"
heading_path:
  - "C.28 — CausalUse-CAL: Causal-Use Questions, Identification, and Realizability"
  - "C.28:1 — Problem Frame"
line_start: 54419
line_end: 54424
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

### C.28:1 - Problem Frame

FPF already has patterns for measurement, temporal claims, evidence, assurance, choice, exploration, call planning, fairness, parity, and mathematical lenses. Each keeps its own result. Causal support cuts across them, so a small shared interface is needed without turning C.28 into a second version of those patterns.

The practical question is not “which causal vocabulary can we attach?” It is “what does this evidence support us to say about this causal question, and what would overturn that conclusion?”

