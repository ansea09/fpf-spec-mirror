---
chunk_kind: "child"
pattern_id: "A.5"
pattern_title: "Open‑Ended Kernel & Extension Layering"
section_id: "A.5:4"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/A.5/A.5__005_solution.md"
commit_sha: "093d30e806a1466e24032733eb020bb5a5f585cc"
heading_path:
  - "A.5 — Open‑Ended Kernel & Extension Layering"
  - "A.5:4 — Solution"
line_start: 6869
line_end: 6881
dependencies:
keywords:
  - "FPF architecture"
  - "extensibility"
  - "modularity"
  - "specialization vs dependancy hierarhies"
---

### A.5:4 - Solution

FPF’s modularity is **declarative**, not “callable”: pattern texts publish **law‑governed declarations** (vocabulary + laws + applicability) that can be reused and specialised. They are not subroutines, services, or protocol endpoints in the software‑architecture sense; treat “module” as a metaphor at most.

To keep the Kernel open‑ended without a bespoke plug‑in patterns standard, FPF relies on the boundary stack that already exists elsewhere in Part A/E/F:

1. **Kernel minimality (C‑5).** Domain knowledge (physics, biology, economics, …) stays outside the Kernel by default; it enters as extension vocabularies and laws.
2. **Boundary packaging via `U.Signature` (A.6.0).** Reusable bundles are published as signatures with an explicit `SignatureManifest` (`imports`, `provides`).
3. **Dependency vs specialisation are separate relations.** `imports` forms a dependency DAG constrained by **E.5.3**; refinement/extension (`⊑`, `⊑⁺`) is expressed separately (e.g., **A.6.1 `U.MechMorph`**) and should not be conflated with `imports`.
4. **Registry references stay references.** Bridges, policy‑ids, and edition‑ids (Part F) are registry identifiers: they are cited/pinned where needed, not treated as exported symbols in `provides`.

This section is intentionally lightweight: it provides architectural intent and neighboring-pattern pointers only. Any new enforceable modularity constraints belong in the A.6.* boundary patterns (or in E.* guard‑rails), not here.

