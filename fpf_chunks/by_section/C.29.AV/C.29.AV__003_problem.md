---
chunk_kind: "child"
pattern_id: "C.29.AV"
pattern_title: "Derive a Condition from an Admissible Variation"
section_id: "C.29.AV:2"
section_title: "Problem"
source_path: "FPF-Spec.md"
output_path: "by_section/C.29.AV/C.29.AV__003_problem.md"
commit_sha: "f965ffb27d69ec5e4ae94f1bb0092c15fa13c991"
heading_path:
  - "C.29.AV — Derive a Condition from an Admissible Variation"
  - "C.29.AV:2 — Problem"
line_start: 64627
line_end: 64634
dependencies:
  - "B.5.MPC"
  - "B.5.RR"
  - "C.29"
  - "C.29.2"
keywords:
---

### C.29.AV:2 - Problem

Changing one value independently can leave the allowed set. A derivative calculated in that direction can then recommend an impossible change. Even with admissible directions, a zero first derivative can describe a maximum, a saddle point or a flat comparison; further reasoning is needed for a minimum.

The reverse difficulty occurs at a constraint boundary: an optimum can have a nonzero derivative because the improving direction is unavailable. A calculation that discards the allowed parameter range loses that conclusion.

These errors share a missing connection between what can vary, what the variation does to the quantity and what the examined family establishes about the original question.

