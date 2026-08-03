---
chunk_kind: "child"
pattern_id: "C.28"
pattern_title: "CausalUse-CAL: Causal-Use Questions, Causality-Ladder Rungs, Identification and Realizability"
section_id: "C.28:3"
section_title: "Forces"
source_path: "FPF-Spec.md"
output_path: "by_section/C.28/C.28__005_forces.md"
commit_sha: "9dd9215969126625d449a40e8ca4d1df9ac903f8"
heading_path:
  - "C.28 — CausalUse-CAL: Causal-Use Questions, Causality-Ladder Rungs, Identification and Realizability"
  - "C.28:3 — Forces"
line_start: 57426
line_end: 57436
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

### C.28:3 - Forces

| Force | Tension |
| --- | --- |
| Causal safety vs cognitive affordability | FPF must block causal laundering without forcing every causal word into a full causal dossier. |
| Rung clarity vs ordinary language | Ordinary language says "improves", "causes", "fair", or "would have"; FPF must recover whether that means association, intervention, or counterfactual comparison. |
| Identification vs realizability | A counterfactual estimand may be identifiable from other data but not directly sampleable, or directly sampleable under action constraints but not generally available. |
| Graph and formalism precision vs reader usability | SCM, DAG, ADMG, SWIG, SCM twin network, AMWN, and counterfactual graphical model names matter, but they must not bury the first practical move. |
| Domain plurality vs one FPF pattern | SCM and PCH, potential outcomes, target-trial emulation, causal ML, transportability, causal representation learning, causal RL, and causal fairness must all remain recognizable without making `C.28` a one-school vocabulary. |
| Neighbor fit vs authority creep | Neighbor patterns need causal-use hooks, but they must not redefine causal-use question, rung, estimand, identification, or realizability. |

