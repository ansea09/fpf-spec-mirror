---
chunk_kind: "child"
pattern_id: "C.30.LCA"
pattern_title: "Control Structure View Adequacy (LCA)"
section_id: "C.30.LCA:8"
section_title: "Common Anti-Patterns and How to Avoid Them"
source_path: "FPF-Spec.md"
output_path: "by_section/C.30.LCA/C.30.LCA__009_common-anti-patterns-and-how-to-avoid-them.md"
commit_sha: "16cd31387cff04ab6b0feef22717f82ac54efa8f"
heading_path:
  - "C.30.LCA — Control Structure View Adequacy (LCA)"
  - "C.30.LCA:8 — Common Anti-Patterns and How to Avoid Them"
line_start: 53026
line_end: 53035
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
  - "C.30.TGA-FLOW-REL"
  - "E.18"
  - "G.6"
keywords:
  - "control layer"
  - "control-structure view"
  - "controller/plant"
  - "layered control architecture"
  - "proof overread"
  - "rate band"
  - "supervisor loop"
---

### C.30.LCA:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Symptom | Repair |
|---|---|---|
| LCA-as-proof | The text says the control stack proves safety, stability, or gate readiness. | Keep the control view and assign proof or exact claims to dynamics, evidence, assurance, gate, or safety patterns. |
| Control-layer-as-system-level | `Layer`, `level`, `tier`, or `stack` is used without a declared role, relation, rate band, or scope. | Recover the exact field: control layer, declared system level, aggregation scope, rate band, organization level, work/evidence scope, or scale window. |
| Agentive episteme | A policy, model, dashboard, or architecture note is said to watch, decide, plan, or adapt. | Name the acting transformer, method, work practice, or publication or source/reliance relation. |
| TGA/LCA substitution | A TGA graph is treated as the control architecture, or an LCA diagram is treated as the flow graph. | Use `DescriptionContext` and structure kind fields to keep views distinct. |
| Hidden rate claim | Multi-rate control is named, but rate adequacy is not checked. | Add `rateSeparationClaimRefs?` and assign timing claims to `C.27`. |

