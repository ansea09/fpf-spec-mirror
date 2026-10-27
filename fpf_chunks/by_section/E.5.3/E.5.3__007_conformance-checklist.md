---
chunk_kind: "child"
pattern_id: "E.5.3"
pattern_title: "Unidirectional Dependency between FPF Families"
section_id: "E.5.3:6"
section_title: "Conformance Checklist"
source_path: "FPF-Spec.md"
output_path: "by_section/E.5.3/E.5.3__007_conformance-checklist.md"
commit_sha: "00a27c2889bb2f7b8e0a7669075826e74d4dd270"
heading_path:
  - "E.5.3 — Unidirectional Dependency between FPF Families"
  - "E.5.3:6 — Conformance Checklist"
line_start: 94848
line_end: 94855
dependencies:
  - "E.4"
  - "E.5"
keywords:
---

### E.5.3:6 - Conformance Checklist

| ID | Requirement |
|----|-------------|
| **CC-UD.1** | Dependency graph among all FPF ecosystem family members **MUST** be acyclic. |
| **CC-UD.2** | A family member **SHALL** import only from its own family or any family above it in the order. |
| **CC‑UD.3** | A DRR that introduces a downward edge **SHALL** be automatically rejected. |

