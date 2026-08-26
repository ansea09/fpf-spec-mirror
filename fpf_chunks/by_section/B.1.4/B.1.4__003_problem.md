---
chunk_kind: "child"
pattern_id: "B.1.4"
pattern_title: "Contextual and Temporal Aggregation"
section_id: "B.1.4:1.1"
section_title: "Problem"
source_path: "FPF-Spec.md"
output_path: "by_section/B.1.4/B.1.4__003_problem.md"
commit_sha: "c7ac61bbaa8d3c10165b1a5a4a350956c87d77c9"
heading_path:
  - "B.1.4 — Contextual and Temporal Aggregation"
  - "B.1.4:1.1 — Problem"
line_start: 35780
line_end: 35785
dependencies:
  - "A.1.1"
  - "A.14"
  - "A.15.1"
  - "A.15.2"
  - "A.3.1"
  - "A.3.2"
  - "A.3.4"
  - "B.1"
  - "B.1.6"
  - "B.2-family"
  - "B.2.P"
  - "C.13"
  - "C.2.1"
  - "C.27"
  - "C.27.TA"
  - "C.29"
  - "E.18"
  - "E.18.2"
keywords:
---

### B.1.4:1.1 - Problem

Without this pattern, four errors recur. First, `SerialStepOf` or another ordered relation is read as ordinary parthood, so changing the order looks harmless even when the aggregate meaning changes. Second, a phase label is read as a new holon level or a new whole, so identity change is hidden instead of handled by whole reidentification. Third, design-time plans, possible method order, run-time histories, and evidence windows are folded together as one sequence. Fourth, mathematical order, graph, or operator notation starts to stand for the in-life object instead of expressing a recovered relation for one bounded use.

The practical failure is not a missing diagram. It is an inadmissible aggregate: the user cannot tell which carrier is being followed, which positions or phases are included, which relation is ordered, which time window is covered, whether gaps or overlaps matter, or which pattern must carry a stronger work, resource, transformation, evidence, or whole-reidentification claim.

