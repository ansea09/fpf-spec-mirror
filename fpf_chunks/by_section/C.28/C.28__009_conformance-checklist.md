---
chunk_kind: "child"
pattern_id: "C.28"
pattern_title: "CausalUse-CAL: Causal-Use Questions, Causality-Ladder Rungs, Identification and Realizability"
section_id: "C.28:7"
section_title: "Conformance Checklist"
source_path: "FPF-Spec.md"
output_path: "by_section/C.28/C.28__009_conformance-checklist.md"
commit_sha: "ae1ff1c7a231a2ec78d244b40d7805a5538c6608"
heading_path:
  - "C.28 — CausalUse-CAL: Causal-Use Questions, Causality-Ladder Rungs, Identification and Realizability"
  - "C.28:7 — Conformance Checklist"
line_start: 48756
line_end: 48772
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

### C.28:7 - Conformance Checklist

| Check | Requirement |
| --- | --- |
| `CC-C28-0` Triage-only use | For triage-only use, causality-ladder rung is named or causal use is declined, supported use and unsupported use is named, and a causal-use claim beyond triage is not implied. |
| `CC-C28-1` Causality-ladder rung declaration | Every causal-use claim declares its target causality-ladder rung: observational association question, interventional action/effect question, or counterfactual comparison question. |
| `CC-C28-2` Durable causal estimand discipline | Every durable interventional/counterfactual-rung causal-use claim names causal-use question, comparator or counterfactual, estimand, assignment or intervention window, follow-up window, outcome measure, assumptions, rival causes, and supported use and unsupported use. |
| `CC-C28-3` No unsupported causality-ladder climb | A claim at interventional-action or counterfactual-comparison rung is not supported only by lower-rung causality-ladder data unless `CausalIdentificationProfile`, `CounterfactualSamplingRealizabilityProfile`, or bounded-use treatment is cited. |
| `CC-C28-4` Realizability is not identification | `CausalIdentificationProfile` and `CounterfactualSamplingRealizabilityProfile` remain distinct. One supports inference from other data; the other supports direct sampling through feasible physical actions. |
| `CC-C28-5` Counterfactual data collection is work | Any realized counterfactual-rung-data procedure is represented as `U.Work` enacted by `U.System` under `RoleAssignment`, with `MethodDescription`, `WorkPlan`, evidence carriers, and physical, ethical, and operational guards. |
| `CC-C28-6` Verdicts are action grammar | `supported`, `bounded`, `unsupported`, and `abstain` each change what the reader may do next. |
| `CC-C28-7` No durable-card default | Escalate from triage to local card to durable card and profiles only when the claimed use triggers the durable causal-use object. |
| `CC-C28-8` Heavy causal-use object payoff | Every selected heavy field or check changes a reader action, blocks a specific overclaim, or supports a concrete evidence/assurance/fairness/parity decision. |
| `CC-C28-9` Semantic-authority split | `C.28` governs causal-use value sets, identification profiles and realizability profiles, graph naming and calculus naming, and support verdicts; neighbors may consume or quote them but must not define competing causal-use value sets. |
| `CC-C28-10` Simulation-only bounded use | Simulation-only output may support bounded model-supported use, but it never becomes interventional evidence or realized counterfactual sample evidence by vocabulary, validation, or role relabeling alone. |
| `CC-C28-11` Decision-economics of evidence | A causal-evidence plan for deployment, assurance, audit, benchmark, policy, fairness, or support-treatment use names the decision threshold, evidence value or probe-worthiness, and cost/risk posture when escalation is not already mandatory by safety, release, or assurance constraints. |

