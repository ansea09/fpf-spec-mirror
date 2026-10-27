---
chunk_kind: "child"
pattern_id: "B.3.5"
pattern_title: "Assurance Grounding for Working-Model Relation Claims (CT2R-LOG)"
section_id: "B.3.5:3"
section_title: "Problem"
source_path: "FPF-Spec.md"
output_path: "by_section/B.3.5/B.3.5__004_problem.md"
commit_sha: "c475118bc1c11d2921b14f74c876e69c24ced3ea"
heading_path:
  - "B.3.5 — Assurance Grounding for Working-Model Relation Claims (CT2R-LOG)"
  - "B.3.5:3 — Problem"
line_start: 45221
line_end: 45226
dependencies:
  - "B.3"
  - "C.13"
  - "E.14"
keywords:
---

### B.3.5:3 - Problem

Working-Model relations such as **ComponentOf** and an ordinary belongs-to sentence are easy to use but not self-justifying. Their declarations alone do not show which participants and occurrences obtain, which rule defines the relation, or what identifies the whole or collection. Conversely, exposing construction traces everywhere makes the graph unreadable to non-specialists.

**We need**: a stable **public relation layer** for relations and, where this profile is elected, a required, **reconstructible** **grounding channel** plus a visible **validation intent** that downstream assurance can reason about. The direct relation layer does not depend on electing the profile.

