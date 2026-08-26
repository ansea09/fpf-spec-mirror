---
chunk_kind: "child"
pattern_id: "C.3.2"
pattern_title: "Kind Intent, Membership Judgment, and Extension"
section_id: "C.3.2:2"
section_title: "Problem"
source_path: "FPF-Spec.md"
output_path: "by_section/C.3.2/C.3.2__004_problem.md"
commit_sha: "563f4c8e06a319cbd375b66cdbb2df27a5f8b9ef"
heading_path:
  - "C.3.2 — Kind Intent, Membership Judgment, and Extension"
  - "C.3.2:2 — Problem"
line_start: 43722
line_end: 43725
dependencies:
  - "A.14"
  - "A.2.6"
  - "A.6.0"
  - "C.2.1"
  - "C.2.3"
  - "C.29"
  - "C.3"
  - "C.3.1"
  - "C.3.3"
  - "C.3.4"
  - "E.24.UK"
keywords:
---

### C.3.2:2 - Problem

The shorthand `MemberOf(e,k,slice)` is unsafe because readers can take it as an A.14 collection relation, an ontic occurrence, a classification result, a database lookup, or a guard. It also hides whether the request was applicable. C.3.2 restores a declaration, an admissibility result, a three-valued judgment only for admissible candidates, and an optional representation while leaving candidate identity and the criterion's governed conditions with their direct patterns.

