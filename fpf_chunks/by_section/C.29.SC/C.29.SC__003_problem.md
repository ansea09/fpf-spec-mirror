---
chunk_kind: "child"
pattern_id: "C.29.SC"
pattern_title: "Derive a Consequence from a Symmetry"
section_id: "C.29.SC:2"
section_title: "Problem"
source_path: "FPF-Spec.md"
output_path: "by_section/C.29.SC/C.29.SC__003_problem.md"
commit_sha: "f965ffb27d69ec5e4ae94f1bb0092c15fa13c991"
heading_path:
  - "C.29.SC — Derive a Consequence from a Symmetry"
  - "C.29.SC:2 — Problem"
line_start: 64851
line_end: 64856
dependencies:
  - "A.3.3.TR"
  - "C.29.1"
  - "C.29.2"
  - "C.29.AV"
keywords:
---

### C.29.SC:2 - Problem

A suggestive symmetry can omit the feature that decides the problem. Equal-looking components can have different costs. A law can be unchanged while its boundary or initial data change. A function can require its output to rotate with its input rather than stay numerically identical.

A second error begins after a real symmetry is established: the solver assumes more than it implies. A symmetric problem can have several asymmetric solutions. A rotation-respecting numerical scheme can fail to conserve the physical angular momentum. To obtain a usable conclusion, follow the transformation through the actual solution condition.

