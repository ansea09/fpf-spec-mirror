---
chunk_kind: "child"
pattern_id: "C.3.1"
pattern_title: "U.Kind and U.SubkindOf Core"
section_id: "C.3.1:2"
section_title: "Problem"
source_path: "FPF-Spec.md"
output_path: "by_section/C.3.1/C.3.1__004_problem.md"
commit_sha: "6bbbb622859fbbcddc02b23ea76bee4dd71c6291"
heading_path:
  - "C.3.1 — U.Kind and U.SubkindOf Core"
  - "C.3.1:2 — Problem"
line_start: 40202
line_end: 40205
dependencies:
  - "A.1"
  - "A.11"
  - "A.2.6"
  - "A.8"
  - "C.2.3"
  - "C.3"
  - "C.3.2"
  - "C.3.3"
  - "E.24.UK"
  - "F.5"
  - "F.8"
keywords:
  - "kind"
  - "partial order"
  - "subkind"
  - "type hierarchy"
---

### C.3.1:2 - Problem

A user can need the sentence "cooling pump is a pump" to be typed and checkable without claiming that FPF must add `U.CoolingPump`. If `U.SubkindOf` is allowed to stand for every stronger-looking relation, then dependency, part-whole, slot filling, construction, and public naming all collapse into one hierarchy. C.3.1 keeps the partial order narrow so other governing relations stay available.

