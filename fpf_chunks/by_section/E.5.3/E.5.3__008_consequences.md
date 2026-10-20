---
chunk_kind: "child"
pattern_id: "E.5.3"
pattern_title: "Unidirectional Dependency between FPF Families"
section_id: "E.5.3:7"
section_title: "Consequences"
source_path: "FPF-Spec.md"
output_path: "by_section/E.5.3/E.5.3__008_consequences.md"
commit_sha: "1868c30c5d056ce8bafddb819b6ca0b7c24a7c94"
heading_path:
  - "E.5.3 — Unidirectional Dependency between FPF Families"
  - "E.5.3:7 — Consequences"
line_start: 95547
line_end: 95553
dependencies:
  - "E.4"
  - "E.5"
keywords:
---

### E.5.3:7 - Consequences

| Benefits | Trade‑offs / Mitigations |
|----------|-------------------------|
| Core stays free of tool churn and tutorial bias. | Authors must create abstraction layers in Tooling instead of inserting hooks into Core. |
| Release cadence decoupled: Core (slow), Tooling (medium), Pedagogy (fast). | Slight duplication when multiple tools target same concept; mitigated by shared Core definitions. |

