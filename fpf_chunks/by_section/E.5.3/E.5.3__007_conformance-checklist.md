---
chunk_kind: "child"
pattern_id: "E.5.3"
pattern_title: "Unidirectional Dependency"
section_id: "E.5.3:6"
section_title: "Conformance Checklist"
source_path: "FPF-Spec.md"
output_path: "by_section/E.5.3/E.5.3__007_conformance-checklist.md"
commit_sha: "1d5c1edd154b636a446b3887a6094be60c60faff"
heading_path:
  - "E.5.3 — Unidirectional Dependency"
  - "E.5.3:6 — Conformance Checklist"
line_start: 67349
line_end: 67356
dependencies:
  - "E.4"
  - "E.5"
keywords:
  - "Core"
  - "Pedagogy"
  - "Tooling"
  - "acyclic"
  - "architecture"
  - "dependency"
  - "layers"
  - "modularity"
---

### E.5.3:6 - Conformance Checklist

| ID | Requirement |
|----|-------------|
| **CC-UD.1** | Dependency graph among all FPF ecosystem family members **MUST** be acyclic. |
| **CC-UD.2** | A family member **SHALL** import only from its own family or any family above it in the order. |
| **CC‑UD.3** | A DRR that introduces a downward edge **SHALL** be automatically rejected. |

