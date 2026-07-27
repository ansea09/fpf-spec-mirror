---
chunk_kind: "child"
pattern_id: "B.3.5"
pattern_title: "Working-Model Relations & Grounding (CT2R-LOG)"
section_id: "B.3.5:3"
section_title: "Problem"
source_path: "FPF-Spec.md"
output_path: "by_section/B.3.5/B.3.5__004_problem.md"
commit_sha: "60caecb4751fb2a3623a1faaca757d29a19acff9"
heading_path:
  - "B.3.5 — Working-Model Relations & Grounding (CT2R-LOG)"
  - "B.3.5:3 — Problem"
line_start: 38788
line_end: 38793
dependencies:
  - "B.3"
  - "C.13"
  - "E.14"
keywords:
  - "CT2R"
  - "Compose-CAL"
  - "assurance layer"
  - "constructive trace"
  - "grounding"
  - "working model"
---

### B.3.5:3 - Problem

Declared sub-relations of `ut:PartOf` (e.g., **ComponentOf**, **MemberOf**) are easy to use but **not self-justifying**: their declaration alone does not show which exact participants and direct relation occurrences obtain, which construction rule applies, or which identity or reidentification rule governs the whole. Conversely, exposing construction traces everywhere makes the graph unreadable to non-specialists.

**We need**: a stable **public relation layer** for relations *and* a mandatory, **reconstructible** **grounding channel**—plus a visible **validation intent** that downstream assurance can reason about.

