---
chunk_kind: "child"
pattern_id: "C.16.IR"
pattern_title: "Determine What an Indication Can Resolve"
section_id: "C.16.IR:2"
section_title: "Problem"
source_path: "FPF-Spec.md"
output_path: "by_section/C.16.IR/C.16.IR__003_problem.md"
commit_sha: "76efec98642d04026281c164a3a1ff840e787be5"
heading_path:
  - "C.16.IR — Determine What an Indication Can Resolve"
  - "C.16.IR:2 — Problem"
line_start: 54326
line_end: 54333
dependencies:
  - "A.3.3.PI"
  - "B.5.MPC.R"
  - "C.11.DUA"
  - "C.16"
  - "C.16.MR"
  - "C.29.1"
  - "C.29.2"
keywords:
---

### C.16.IR:2 - Problem

A measurement relation can predict the indication without allowing the sought value to be uniquely recovered. Several quantities may jointly affect the same reading; a conversion can erase distinctions through clipping, averaging, squaring or wrapping. An algorithm can return one solution while other compatible solutions remain.

The receiving question also matters. An interval may settle an operating threshold even when a point value is unavailable. Conversely, precise arithmetic on one arbitrarily selected solution can hide a decision-changing ambiguity.

The problem is to recover the alternatives allowed by the indication and its conditions, then determine which differences matter to the intended use. This requires keeping the observation, model assumptions, computed approximations and supported conclusion distinguishable throughout the calculation.

