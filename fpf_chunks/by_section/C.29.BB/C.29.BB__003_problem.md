---
chunk_kind: "child"
pattern_id: "C.29.BB"
pattern_title: "Construct a Balance across a Boundary"
section_id: "C.29.BB:2"
section_title: "Problem"
source_path: "FPF-Spec.md"
output_path: "by_section/C.29.BB/C.29.BB__003_problem.md"
commit_sha: "1e57ccda08ebbb9d49b7b2190bc2740b72075a13"
heading_path:
  - "C.29.BB — Construct a Balance across a Boundary"
  - "C.29.BB:2 — Problem"
line_start: 74211
line_end: 74216
dependencies:
  - "A.3.3.TR"
  - "C.11.DUA"
  - "C.29.1"
  - "C.29.2"
  - "E.18.2"
keywords:
---

### C.29.BB:2 - Problem

An equation such as “change equals input minus output” can leave its subject undecided. The parts may overlap, an intermediate store may be omitted, or two records may count the same transfer at different times. The quantity may also be created or removed within the boundary: the number of unfinished jobs changes when a job is completed, while the amount of a conserved material follows a different law.

Adding local equations works only after their quantities, intervals and shared transfers have been made compatible. Otherwise cancellation can hide a missing store or combine values that cannot be added.

