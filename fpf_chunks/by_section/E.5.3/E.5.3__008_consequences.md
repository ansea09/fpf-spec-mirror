---
chunk_kind: "child"
pattern_id: "E.5.3"
pattern_title: "Unidirectional Dependency"
section_id: "E.5.3:7"
section_title: "Consequences"
source_path: "FPF-Spec.md"
output_path: "by_section/E.5.3/E.5.3__008_consequences.md"
commit_sha: "0caf9a10acfc0ee17c32fc71f6173b542393f0a4"
heading_path:
  - "E.5.3 — Unidirectional Dependency"
  - "E.5.3:7 — Consequences"
line_start: 80159
line_end: 80165
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

### E.5.3:7 - Consequences

| Benefits | Trade‑offs / Mitigations |
|----------|-------------------------|
| Core stays free of tool churn and tutorial bias. | Authors must create abstraction layers in Tooling instead of inserting hooks into Core. |
| Release cadence decoupled: Core (slow), Tooling (medium), Pedagogy (fast). | Slight duplication when multiple tools target same concept; mitigated by shared Core definitions. |

