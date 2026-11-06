---
chunk_kind: "child"
pattern_id: "A.5"
pattern_title: "Open-Ended FPF Kernel and Extension Layering"
section_id: "A.5:2"
section_title: "Problem"
source_path: "FPF-Spec.md"
output_path: "by_section/A.5/A.5__003_problem.md"
commit_sha: "d8dd955fddb923b5b946d2c5865d0665cff5a67e"
heading_path:
  - "A.5 — Open-Ended FPF Kernel and Extension Layering"
  - "A.5:2 — Problem"
line_start: 13700
line_end: 13708
dependencies:
keywords:
  - "FPF architecture"
  - "declarative modularity"
  - "dependency versus specialization"
  - "domain extensions"
  - "extensibility"
  - "kernel boundaries"
---

### A.5:2 - Problem

Admitting domain-specific primitives without their applicability boundaries can create two problems:

| Problem | Practical effect |
| --- | --- |
| **Kernel bloat** | Unnecessary root U-kinds or local type vocabularies can increase users' learning effort and maintainers' support work. |
| **Conflicting assumptions** | Incompatible axioms presented as unconditional commitments leave the reader unable to select an applicable explanation. |

