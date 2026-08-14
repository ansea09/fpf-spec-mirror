---
chunk_kind: "child"
pattern_id: "C.28"
pattern_title: "CausalUse-CAL: Causal-Use Questions, Causality-Ladder Rungs, Identification and Realizability"
section_id: "C.28:8"
section_title: "Common Anti-Patterns and How to Avoid Them"
source_path: "FPF-Spec.md"
output_path: "by_section/C.28/C.28__010_common-anti-patterns-and-how-to-avoid-them.md"
commit_sha: "646b41f84ffef4918ad9bdb34e7b450f0c4903ee"
heading_path:
  - "C.28 — CausalUse-CAL: Causal-Use Questions, Causality-Ladder Rungs, Identification and Realizability"
  - "C.28:8 — Common Anti-Patterns and How to Avoid Them"
line_start: 58339
line_end: 58351
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

### C.28:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Symptom | Repair |
| --- | --- | --- |
| Fill-all-cards default | Every mention of "cause", "effect", or "counterfactual" triggers a durable dossier. | Start with `CausalUseTriageRecord`; escalate only when the claimed use requires it. |
| Causal certification theater | Every field is filled, but no reader action, evidence design, downgrade, or unsupported use changes. | Remove fields or downgrade their claim-use until each remaining field changes a decision or blocks an overclaim. |
| Association as intervention | "Users who received intervention X did better" is published as effect of X without action support or assignment support. | Publish association, build identification work, or design evidence. |
| Interventional proxy as counterfactual fairness | A policy-change metric is called counterfactual fairness. | Declare interventional-action rung unless counterfactual estimand plus identification or realizability is present. |
| Simulation as realized counterfactual sample | Model output is described as realized counterfactual-rung support without direct sampling or validation. | Use `simulationOnlyCounterfactualOutputBasis` and name supported model use and unsupported model use. |
| Graph-only causality | A DAG or SCM diagram is treated as sufficient support. | Add assumptions, data regime, graph representation kind, calculus, and admissible use. |
| Cross-rung benchmark | Methods are compared as peers while one answers association, another intervention, and another counterfactual comparison. | Use `CausalMethodRungParityRecord` and degrade or abstain when parity is absent. |
| QL escape | Causal confusion is rebranded as quantum-like because ordinary probability feels hard. | Use `C.26` only after causal-use explanation and ordinary FPF neighbors have done their work. |

