---
chunk_kind: "child"
pattern_id: "C.28"
pattern_title: "CausalUse-CAL: Causal-Use Questions, Causality-Ladder Rungs, Identification and Realizability"
section_id: "C.28:2"
section_title: "Problem"
source_path: "FPF-Spec.md"
output_path: "by_section/C.28/C.28__004_problem.md"
commit_sha: "11f2345e65e4b2ec5b84c0cecde4c9485834d28d"
heading_path:
  - "C.28 — CausalUse-CAL: Causal-Use Questions, Causality-Ladder Rungs, Identification and Realizability"
  - "C.28:2 — Problem"
line_start: 57700
line_end: 57711
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

### C.28:2 - Problem

Causal language is easy to overclaim because ordinary prose hides the difference between association, action, counterfactual comparison, realized counterfactual sample, identified estimate, and simulation.

Three collapses are especially dangerous:

1. **Rung collapse.** Observational association, interventional action or effect, and counterfactual comparison are treated as one causality-ladder rung.
2. **Support collapse.** Observed data, experimental data, direct counterfactual-rung samples, identified estimates, and simulations are treated as one evidence basis.
3. **Use collapse.** A result that supports one use, such as association reporting, is reused for another use, such as causal fairness, policy optimality, or method superiority.

`C.28` prevents those collapses by making rung, support, and use explicit before claims requiring higher causal support are admitted.

