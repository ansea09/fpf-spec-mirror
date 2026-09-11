---
chunk_kind: "child"
pattern_id: "A.5"
pattern_title: "Open‑Ended Kernel & Extension Layering"
section_id: "A.5:4"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/A.5/A.5__005_solution.md"
commit_sha: "ef9ded2cb965193aa2484c84f06d65770439cef8"
heading_path:
  - "A.5 — Open‑Ended Kernel & Extension Layering"
  - "A.5:4 — Solution"
line_start: 10118
line_end: 10129
dependencies:
keywords:
  - "FPF architecture"
  - "extensibility"
  - "modularity"
  - "specialization vs dependancy hierarhies"
---

### A.5:4 - Solution

FPF’s modularity is **declarative**, not “callable”: pattern texts publish **law‑governed declarations** (vocabulary + laws + applicability) that can be reused and specialised.

To keep the Kernel open‑ended, use the following boundary rules:

1. **Kernel minimality (C‑5).** Domain knowledge stays outside the Kernel by default; it enters as extension vocabularies and laws.
2. **Boundary packaging via `U.Signature` (A.6.0).** For reusable declaration bundles admitted as signatures under **A.6.0**, expose actual declaration dependencies in an explicit `SignatureManifest` (`imports`, `provides`).
3. **Dependency vs specialisation are separate relations.** `imports` forms a dependency DAG constrained by **E.5.3**; refinement/extension (`⊑`, `⊑⁺`) is expressed separately (for mechanism declarations, see **A.6.1:4.8**; use **C.29** when a mathematical morphism is claimed) and should not be conflated with `imports`.
4. **Registry references stay references.** Bridge ids, policy‑ids, and edition‑ids (Part F) are registry identifiers: they are cited/pinned where needed, not treated as exported symbols in `provides`.


