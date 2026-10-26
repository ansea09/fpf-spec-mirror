---
chunk_kind: "child"
pattern_id: "E.5.3"
pattern_title: "Unidirectional Dependency between FPF Families"
section_id: "E.5.3:7"
section_title: "Consequences"
source_path: "FPF-Spec.md"
output_path: "by_section/E.5.3/E.5.3__008_consequences.md"
commit_sha: "4ce2f7202e12c5c519a3466f5e07fe0b92e78a44"
heading_path:
  - "E.5.3 — Unidirectional Dependency between FPF Families"
  - "E.5.3:7 — Consequences"
line_start: 94753
line_end: 94759
dependencies:
  - "E.4"
  - "E.5"
keywords:
---

### E.5.3:7 - Consequences

| Benefits | Trade‑offs / Mitigations |
|----------|-------------------------|
| Core stays free of tool churn and tutorial bias. | Authors must create abstraction layers in Tooling instead of inserting hooks into Core. |
| Tooling and Pedagogy changes need not require a Core release. | Slight duplication when multiple tools target same concept; mitigated by shared Core definitions. |

