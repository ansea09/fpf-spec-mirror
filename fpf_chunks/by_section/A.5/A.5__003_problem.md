---
chunk_kind: "child"
pattern_id: "A.5"
pattern_title: "Open-Ended FPF Kernel and Extension Layering"
section_id: "A.5:2"
section_title: "Problem"
source_path: "FPF-Spec.md"
output_path: "by_section/A.5/A.5__003_problem.md"
commit_sha: "3f6e02840fe3a22427aed590f9688a9c8f6bf5c8"
heading_path:
  - "A.5 — Open-Ended FPF Kernel and Extension Layering"
  - "A.5:2 — Problem"
line_start: 13588
line_end: 13596
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

