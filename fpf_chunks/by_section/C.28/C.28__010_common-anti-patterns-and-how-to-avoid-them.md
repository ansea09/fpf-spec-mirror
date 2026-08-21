---
chunk_kind: "child"
pattern_id: "C.28"
pattern_title: "CausalUse-CAL: Causal-Use Questions, Identification, and Realizability"
section_id: "C.28:8"
section_title: "Common Anti-Patterns and How to Avoid Them"
source_path: "FPF-Spec.md"
output_path: "by_section/C.28/C.28__010_common-anti-patterns-and-how-to-avoid-them.md"
commit_sha: "f0b498ddfdf562242984ff7ab7a2557b55af6690"
heading_path:
  - "C.28 — CausalUse-CAL: Causal-Use Questions, Identification, and Realizability"
  - "C.28:8 — Common Anti-Patterns and How to Avoid Them"
line_start: 54917
line_end: 54933
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

### C.28:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Repair |
| --- | --- |
| Fill-all-cards default | Start with triage and add only the live profile. |
| Rung label as validity proof | Run the common threat screen and cite the actual results. |
| One support-basis enum | Keep data, identification, estimate, sampling, simulation, and transport separate. |
| Estimate creates identification | Require an identification or design-based result first. |
| Graph-only causality | Cite the model or diagram, assumptions, and replayable derivation or bound. |
| Feasibility as performed evidence | Keep the sampling-realizability result separate from a WorkPlan, dated Work, and resulting data. |
| Work or plan as data | Require the A.10 path to the resulting sample or data before claiming the empirical regime. |
| Simulation as realized evidence | Use `simulationResultRef` and state unsupported realized/interventional use. |
| Shared context label proves transport | Name exact causal endpoints, assumptions, and formula. |
| Support verdict authorizes action | Return the support result to the downstream decision pattern. |
| Specialist branch named but not consumable | Put its exact result ref in the common component contract and keep its assumptions, limits, uncertainty, and reopen condition with that result. |
| Ontology dossier as precision | Keep specialist refs behind the ordinary question, threat, and support statement. |

