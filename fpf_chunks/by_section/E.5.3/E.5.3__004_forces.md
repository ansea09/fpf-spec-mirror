---
chunk_kind: "child"
pattern_id: "E.5.3"
pattern_title: "Unidirectional Dependency between FPF Families"
section_id: "E.5.3:3"
section_title: "Forces"
source_path: "FPF-Spec.md"
output_path: "by_section/E.5.3/E.5.3__004_forces.md"
commit_sha: "996ae39ce00b4a9c9b59b48a4f1446b2175dcffb"
heading_path:
  - "E.5.3 — Unidirectional Dependency between FPF Families"
  - "E.5.3:3 — Forces"
line_start: 95989
line_end: 95996
dependencies:
  - "E.4"
  - "E.5"
keywords:
---

### E.5.3:3 - Forces

| Force | Tension |
|-------|---------|
| **Agility vs Stability** | Tooling must iterate quickly ↔ Core must remain slow and deliberate. |
| **Reuse vs Isolation** | Authors want to reuse helper concepts ↔ Core cannot depend on volatile code. |
| **Simplicity** | Rule must be testable and unambiguous ↔ must allow legitimate upward imports. |

