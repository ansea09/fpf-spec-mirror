---
chunk_kind: "child"
pattern_id: "E.5.3"
pattern_title: "Unidirectional Dependency between FPF Families"
section_id: "E.5.3:3"
section_title: "Forces"
source_path: "FPF-Spec.md"
output_path: "by_section/E.5.3/E.5.3__004_forces.md"
commit_sha: "169e3e09c04a4174ce4c26682cf181a0d255b6f7"
heading_path:
  - "E.5.3 — Unidirectional Dependency between FPF Families"
  - "E.5.3:3 — Forces"
line_start: 102331
line_end: 102338
dependencies:
  - "E.4"
  - "E.5"
keywords:
---

### E.5.3:3 - Forces

| Force | Tension |
|-------|---------|
| **Agility vs Stability** | Tooling must iterate quickly, while changes to Core must remain slow and deliberate. |
| **Reuse vs Isolation** | Authors want to reuse helper concepts, but Core cannot depend on volatile code. |
| **Simplicity** | The rule must be testable and unambiguous and must allow legitimate upward imports. |

