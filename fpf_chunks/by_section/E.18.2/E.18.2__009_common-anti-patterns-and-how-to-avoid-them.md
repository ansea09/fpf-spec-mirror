---
chunk_kind: "child"
pattern_id: "E.18.2"
pattern_title: "Transformation Flow Mathematical Description"
section_id: "E.18.2:6"
section_title: "Common Anti-Patterns and How to Avoid Them"
source_path: "FPF-Spec.md"
output_path: "by_section/E.18.2/E.18.2__009_common-anti-patterns-and-how-to-avoid-them.md"
commit_sha: "fe0df9dcb06cfc87c8a6cb2f7cce3ac0d3b64d5e"
heading_path:
  - "E.18.2 — Transformation Flow Mathematical Description"
  - "E.18.2:6 — Common Anti-Patterns and How to Avoid Them"
line_start: 70649
line_end: 70658
dependencies:
  - "A.10"
  - "A.15"
  - "A.20"
  - "A.21"
  - "A.3.4"
  - "A.6.0"
  - "A.6.5"
  - "B.3"
  - "C.2.1"
  - "C.29"
  - "C.30"
  - "C.30.TFS-REL"
  - "E.17"
  - "E.18"
  - "E.18.1"
  - "U.Episteme"
  - "U.Signature"
  - "U.Transformation"
keywords:
  - "C.29 boundary"
  - "algebraic description"
  - "graph expression"
  - "mathematical description"
  - "path expression"
  - "transformation-flow math"
---

### E.18.2:6 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Repair |
|---|---|
| **Graph-as-world.** A graph-shaped expression is treated as the project-world structure because it is visually convincing. | Name whether the current EoC is E.18 selected structure, E.18.2 mathematical description, E.17 publication, or C.29 lens-use adequacy. |
| **Path-as-procedure.** A mathematical path or path slice is read as a required project procedure. | Keep it as a mathematical relation over a selected structure; use method or work-plan patterns for procedures. |
| **Algebra-as-mechanism.** An operation law or equation system is treated as a realized mechanism. | Use A.6.0 for formal substrate and A.6.1 for mechanism claims; keep E.18.2 to the expression relation. |
| **Fold-as-identity.** A quotient, fold, or coarsening erases detail and is then used as if nothing was lost. | State preserved structure, lost structure, and return condition; use C.29 when the adequacy of the fold matters. |
| **Diagram-as-architecture adequacy.** A clean diagram is treated as proof that the architecture is good. | Use `C.30` for the architecture claim, `C.30.ASV` for architecture structural-view adequacy, and `C.31` for reusable-structure characteristics; `E.18.2` only describes selected structure mathematically. |

