---
chunk_kind: "child"
pattern_id: "C.29.BB"
pattern_title: "Construct a Balance across a Boundary"
section_id: "C.29.BB:2"
section_title: "Problem"
source_path: "FPF-Spec.md"
output_path: "by_section/C.29.BB/C.29.BB__003_problem.md"
commit_sha: "7bba05916e6e8ad42f868ed3aad0a7644fe0c354"
heading_path:
  - "C.29.BB — Construct a Balance across a Boundary"
  - "C.29.BB:2 — Problem"
line_start: 66297
line_end: 66302
dependencies:
  - "A.3.3.TR"
  - "C.11.DUA"
  - "C.29.1"
  - "C.29.2"
  - "E.18.2"
keywords:
---

### C.29.BB:2 - Problem

A plausible equation such as “change equals input minus output” can leave its subject undecided. The chosen parts may overlap, an intermediate store may be omitted, or two records may count the same transfer at different times. A selected quantity may also be created or removed within the boundary: the number of unfinished jobs changes when a job is completed, while the amount of a conserved material follows a different law.

Adding local equations works only after their quantities, intervals and shared transfers have been made compatible. Otherwise cancellation can hide a missing store or combine values that cannot be added.

