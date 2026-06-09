---
chunk_kind: "child"
pattern_id: "C.28"
pattern_title: "CausalUse-CAL: Causal-Use Questions, Causality-Ladder Rungs, Identification and Realizability"
section_id: "C.28:10"
section_title: "Rationale"
source_path: "FPF-Spec.md"
output_path: "by_section/C.28/C.28__012_rationale.md"
commit_sha: "093d30e806a1466e24032733eb020bb5a5f585cc"
heading_path:
  - "C.28 — CausalUse-CAL: Causal-Use Questions, Causality-Ladder Rungs, Identification and Realizability"
  - "C.28:10 — Rationale"
line_start: 50342
line_end: 50355
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

### C.28:10 - Rationale

FPF needs this pattern because causal language changes what a reader may do.

Temporal language can say that something changed. Measurement language can say that a score is higher. Assurance language can say that evidence has more or less support. None of those alone says that an action caused a result, that a counterfactual comparison is supported, or that a causal policy should be deployed.

`C.28` therefore uses a semantic-authority split:

- `C.28` governs causal-use question, rung, estimand, identification, realizability, causal evidence support basis, and causal-use verdict.
- Neighbor patterns keep their own authority and cite `C.28` only when causal use is live.
- `C.26` receives a causal exit: intervention, causal effect, causal fairness, causal policy, and counterfactual-rung-data realizability are ordinary causal-use questions before they are quantum-like modeling questions.

The pattern is not Pearl-only. SCM/PCH provides the rung discipline, but potential outcomes, target-trial emulation, causal ML estimation, transportability, causal representation learning, causal RL, and causal fairness all change the fields that FPF must preserve.

