---
chunk_kind: "child"
pattern_id: "B.3.5"
pattern_title: "Working-Model Relations & Grounding (CT2R-LOG)"
section_id: "B.3.5:3"
section_title: "Problem"
source_path: "FPF-Spec.md"
output_path: "by_section/B.3.5/B.3.5__004_problem.md"
commit_sha: "02a8b4bac1f141b1751421bf522e9dc489ae522e"
heading_path:
  - "B.3.5 — Working-Model Relations & Grounding (CT2R-LOG)"
  - "B.3.5:3 — Problem"
line_start: 34622
line_end: 34627
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

Declared sub‑relations of `ut:PartOf` (e.g., **ComponentOf**, **MemberOf**) are easy to use but **not self‑justifying**: nothing in their declaration shows *why* a given edge should be trusted, or how to **re‑derive** it if challenged. Conversely, exposing constructor traces everywhere makes the graph unreadable to non‑specialists.

**We need**: a stable **public relation layer** for relations *and* a mandatory, **reconstructible** **grounding channel**—plus a visible **validation intent** that downstream assurance can reason about.

