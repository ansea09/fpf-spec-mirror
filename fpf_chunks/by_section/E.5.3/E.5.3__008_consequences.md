---
chunk_kind: "child"
pattern_id: "E.5.3"
pattern_title: "Unidirectional Dependency between FPF Families"
section_id: "E.5.3:7"
section_title: "Consequences"
source_path: "FPF-Spec.md"
output_path: "by_section/E.5.3/E.5.3__008_consequences.md"
commit_sha: "c475118bc1c11d2921b14f74c876e69c24ced3ea"
heading_path:
  - "E.5.3 — Unidirectional Dependency between FPF Families"
  - "E.5.3:7 — Consequences"
line_start: 95281
line_end: 95287
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

