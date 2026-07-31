---
chunk_kind: "child"
pattern_id: "C.28"
pattern_title: "CausalUse-CAL: Causal-Use Questions, Causality-Ladder Rungs, Identification and Realizability"
section_id: "C.28:1"
section_title: "Problem Frame"
source_path: "FPF-Spec.md"
output_path: "by_section/C.28/C.28__003_problem-frame.md"
commit_sha: "d1f696e7c7767705206a8cacd9f6ed48e4dc5b02"
heading_path:
  - "C.28 — CausalUse-CAL: Causal-Use Questions, Causality-Ladder Rungs, Identification and Realizability"
  - "C.28:1 — Problem Frame"
line_start: 57038
line_end: 57057
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

### C.28:1 - Problem Frame

FPF already has dedicated neighboring patterns for measurement, evidence, assurance, temporal claims, decisions, exploration, call planning, fairness, method dispatch, parity, and quantum-like modeling. None of those neighbors should become the general authority for causal use.

`C.28` exists because causal use cuts across those neighbors. The same sentence can be:

- a measurement description handled by `C.16`;
- a temporal trend handled by `C.27`;
- an assurance claim handled by `B.3`;
- an evidence graph reference handled by `A.10`;
- a decision record handled by `C.11`;
- a pool-policy record handled by `C.19`;
- a call-planning record handled by `C.24`;
- a fairness audit handled by `D.5`;
- a parity report handled by `G.9`;
- a quantum-like residual handled by `C.26`;
- or a causal-use claim governed here.

The first pattern task is therefore not to classify wording for its own sake. It is to recover the live causal question, the target causality-ladder rung, the support basis currently available, and the cheapest truthful next use. Sometimes that move is to downgrade the claim to association, temporal change, metric-only fairness, or simulation-only use. Sometimes it is to open identification, realizability, evidence-design, fairness, policy-evaluation, or benchmark-parity work. `C.28` exists to keep those moves distinct and to stop teams from acting as if an identification, realizability, or intervention-support basis had already been earned.

