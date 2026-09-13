---
chunk_kind: "child"
pattern_id: "C.29.AV"
pattern_title: "Derive a Condition from an Admissible Variation"
section_id: "C.29.AV:1"
section_title: "Problem frame"
source_path: "FPF-Spec.md"
output_path: "by_section/C.29.AV/C.29.AV__002_problem-frame.md"
commit_sha: "bbfb5347013400e9a895fa4b0f66992e931c0ece"
heading_path:
  - "C.29.AV — Derive a Condition from an Admissible Variation"
  - "C.29.AV:1 — Problem frame"
line_start: 64613
line_end: 64626
dependencies:
  - "B.5.MPC"
  - "B.5.RR"
  - "C.29"
  - "C.29.2"
keywords:
---

### C.29.AV:1 - Problem frame

Use this pattern when you have a candidate allocation, shape, history or other mathematical construction under constraints, and need to find an improving change or a condition that an optimum or stationary construction must satisfy.

For example, two allocations obey the same resource limit, but it is unclear how moving some resource between them changes the criterion. Or a proposed physical history has fixed endpoints, and you need to find what its action principle requires of the motion between them. In both cases, construct changes that preserve the relevant constraints, calculate their effect and determine the strength of the resulting conclusion.

The subject of the Method is a family of admissible mathematical candidates and the change of a stated scalar quantity over that family. A *variation* is a specified change within the family; *admissible* means that the changed candidate satisfies the conditions retained for this question.

The first useful result is an improving candidate, a necessary condition, a justified minimum or maximum, or a located obstacle to obtaining one. A necessary condition can narrow a search even when it does not settle the optimum.

The reader needs the candidate, its constraints, the quantity being compared and the mathematical operations used to calculate its change. Elementary algebra is enough for the allocation example. The history example additionally uses differentiation and integration. A specialist can supply a construction or theorem at the step where that preparation is needed.

If an available evaluation of a few fixed alternatives already answers the question, use that comparison. This Method is useful when constructing the allowed changes or reasoning from them is the difficulty.

