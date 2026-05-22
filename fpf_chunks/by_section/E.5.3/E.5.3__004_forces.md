---
chunk_kind: "child"
pattern_id: "E.5.3"
pattern_title: "Unidirectional Dependency"
section_id: "E.5.3:3"
section_title: "Forces"
source_path: "FPF-Spec.md"
output_path: "by_section/E.5.3/E.5.3__004_forces.md"
commit_sha: "725f0b7b372754cda3f6f4e15184215da568fc4d"
heading_path:
  - "E.5.3 — Unidirectional Dependency"
  - "E.5.3:3 — Forces"
line_start: 50100
line_end: 50107
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

### E.5.3:3 - Forces

| Force | Tension |
|-------|---------|
| **Agility vs Stability** | Tooling must iterate quickly ↔ Core must remain slow and deliberate. |
| **Reuse vs Isolation** | Authors want to reuse helper concepts ↔ Core cannot depend on volatile code. |
| **Simplicity** | Rule must be testable and unambiguous ↔ must allow legitimate upward imports. |

