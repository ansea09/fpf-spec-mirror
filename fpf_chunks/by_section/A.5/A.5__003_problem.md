---
chunk_kind: "child"
pattern_id: "A.5"
pattern_title: "Open‑Ended Kernel & Extension Layering"
section_id: "A.5:2"
section_title: "Problem"
source_path: "FPF-Spec.md"
output_path: "by_section/A.5/A.5__003_problem.md"
commit_sha: "f1d0f9319cf1f93129b7691a328a281022252c4e"
heading_path:
  - "A.5 — Open‑Ended Kernel & Extension Layering"
  - "A.5:2 — Problem"
line_start: 7963
line_end: 7973
dependencies:
keywords:
  - "FPF architecture"
  - "extensibility"
  - "modularity"
  - "specialization vs dependancy hierarhies"
---

### A.5:2 - Problem

If FPF were to let **domain‑specific primitives creep into its Kernel**, two pathologies would follow:

| Pathology               | Manifestation                                                                                                                  | Breach of Constitution                                                     |
| ----------------------- | ------------------------------------------------------------------------------------------------------------------------------ | -------------------------------------------------------------------------- |
| **Kernel Bloat**        | Every new field (e.g. synthetic biology) adds convenience root U-kinds or local type vocabularies -> Core size explodes, review workload becomes unscalable.       | Violates **C-5 Ontological Parsimony**; erodes **P-1 Cognitive Elegance**. |
| **Conceptual Gridlock** | Conflicting axioms (deterministic thermodynamics vs. indeterministic econ‑metrics) must fight for space in the same namespace. | Breaks **C‑3 Cross‑Scale Consistency**; triggers chronic DRR deadlock.     |

A *minimal, extensible* design is therefore mandatory.

