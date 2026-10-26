---
chunk_kind: "child"
pattern_id: "A.5"
pattern_title: "Open-Ended FPF Kernel and Extension Layering"
section_id: "A.5:2"
section_title: "Problem"
source_path: "FPF-Spec.md"
output_path: "by_section/A.5/A.5__003_problem.md"
commit_sha: "4ce2f7202e12c5c519a3466f5e07fe0b92e78a44"
heading_path:
  - "A.5 — Open-Ended FPF Kernel and Extension Layering"
  - "A.5:2 — Problem"
line_start: 13543
line_end: 13551
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
| **Kernel bloat** | Adding unnecessary root U-kinds or local type vocabularies increases what every Kernel user must understand and maintain. |
| **Conflicting assumptions** | Incompatible axioms presented as unconditional commitments leave the reader unable to select an applicable explanation. |

