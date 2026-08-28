---
chunk_kind: "child"
pattern_id: "C.30.LCA"
pattern_title: "Control Structure View Adequacy (LCA)"
section_id: "C.30.LCA:8"
section_title: "Common Anti-Patterns and How to Avoid Them"
source_path: "FPF-Spec.md"
output_path: "by_section/C.30.LCA/C.30.LCA__009_common-anti-patterns-and-how-to-avoid-them.md"
commit_sha: "72222c13cc1bba009f1ee1f1aca47654db8e5716"
heading_path:
  - "C.30.LCA — Control Structure View Adequacy (LCA)"
  - "C.30.LCA:8 — Common Anti-Patterns and How to Avoid Them"
line_start: 60798
line_end: 60807
dependencies:
  - "A.10"
  - "A.20"
  - "A.21"
  - "A.22"
  - "A.3.3"
  - "B.2.5"
  - "B.3"
  - "C.27"
  - "C.28"
  - "C.29"
  - "C.30"
  - "C.30.AD"
  - "C.30.ASV"
  - "C.30.STRAT"
  - "C.30.TFS-REL"
  - "E.17.0"
  - "E.18"
  - "G.6"
keywords:
  - "control layer"
  - "control-structure view"
  - "controller and plant"
  - "layered control architecture"
  - "proof overread"
  - "rate band"
  - "supervisor loop"
---

### C.30.LCA:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Symptom | Repair |
|---|---|---|
| LCA-as-proof | The text says the control stack proves safety, stability, or gate readiness. | Keep the control view and use the relevant dynamics, evidence, assurance, gate, or safety pattern for each proof or claim named by value. |
| Control-layer-as-generic-level | `Layer`, `level`, `tier`, or `stack` is used without a direct control relation, inter-layer relation, rate band, or `B.2.5` supervisor-subholon relation. | Apply `C.30.STRAT`; use C.30.LCA only after a control-specific relation is recovered. |
| Agentive episteme, kind, or assignment | A policy, model, dashboard, local system-role kind, assignment, or architecture note is said to watch, decide, plan, or adapt. | Recover the direct control relation and participant meanings. For actual action, recover the exact performer through A.13 and admit the `U.Work` occurrence independently through A.15.1. Add assignment and F.6 only when precise assignment-bound attribution is expressly consumed; keep publication, source-to-use, work-reliance, authority, responsibility, gate, safety, and evidence relations separate. |
| Transformation-flow and LCA substitution | A transformation-flow graph expression is treated as control architecture, or an LCA diagram is treated as the transformation-flow graph expression. | Recover both exact selected structures and description epistemes separately; use E.17.0 only for actual viewpoint conformance. |
| Hidden rate claim | Multi-rate control is named, but rate adequacy is not checked. | Add `rateSeparationClaimRefs?`; use `C.27.TA` for temporal-aspect or rate-band claims and `C.27` for authored temporal-claim adequacy. |

