---
chunk_kind: "child"
pattern_id: "E.5.3"
pattern_title: "Unidirectional Dependency"
section_id: "E.5.3:7"
section_title: "Consequences"
source_path: "FPF-Spec.md"
output_path: "by_section/E.5.3/E.5.3__008_consequences.md"
commit_sha: "4b75b56c13f5d61be5238fdbc7c20af5c6f89df7"
heading_path:
  - "E.5.3 — Unidirectional Dependency"
  - "E.5.3:7 — Consequences"
line_start: 70273
line_end: 70279
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

