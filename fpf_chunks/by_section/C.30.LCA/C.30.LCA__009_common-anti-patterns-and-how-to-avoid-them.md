---
chunk_kind: "child"
pattern_id: "C.30.LCA"
pattern_title: "Control Structure View Adequacy (LCA)"
section_id: "C.30.LCA:8"
section_title: "Common Anti-Patterns and How to Avoid Them"
source_path: "FPF-Spec.md"
output_path: "by_section/C.30.LCA/C.30.LCA__009_common-anti-patterns-and-how-to-avoid-them.md"
commit_sha: "66e732dfef7a4a93ff23eec43b3f759a6664652d"
heading_path:
  - "C.30.LCA — Control Structure View Adequacy (LCA)"
  - "C.30.LCA:8 — Common Anti-Patterns and How to Avoid Them"
line_start: 61479
line_end: 61488
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
  - "C.30.ASV"
  - "C.30.LCA"
  - "C.30.STRAT"
  - "C.30.TFS-REL"
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
| LCA-as-proof | The text says the control stack proves safety, stability, or gate readiness. | Keep the control view and assign proof or claim named by values to dynamics, evidence, assurance, gate, or safety patterns. |
| Control-layer-as-generic-level | `Layer`, `level`, `tier`, or `stack` is used without a recovered control role, relation, rate band, bounded context, or `B.2.5` supervisor-subholon relation. | Apply `C.30.STRAT`; return to C.30.LCA only for a recovered control-layer or control-relation case. |
| Agentive episteme | A policy, model, dashboard, or architecture note is said to watch, decide, plan, or adapt. | Name the acting system in role, the method it enacts when current, the work or review practice when current, and any publication relation, source relation, or reliance relation. |
| Transformation-flow and LCA substitution | A transformation-flow graph expression is treated as the control architecture, or an LCA diagram is treated as the transformation-flow graph expression. | Use `DescriptionContext` and structure kind fields to keep views distinct. |
| Hidden rate claim | Multi-rate control is named, but rate adequacy is not checked. | Add `rateSeparationClaimRefs?`; assign temporal-aspect or rate-band claims to `C.27.TA` and authored temporal-claim adequacy to `C.27`. |

