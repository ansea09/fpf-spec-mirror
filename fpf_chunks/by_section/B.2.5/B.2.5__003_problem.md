---
chunk_kind: "child"
pattern_id: "B.2.5"
pattern_title: "Supervisor-Subholon Feedback Loop"
section_id: "B.2.5:2"
section_title: "Problem"
source_path: "FPF-Spec.md"
output_path: "by_section/B.2.5/B.2.5__003_problem.md"
commit_sha: "646b0b9b164f7c13258633a33b92d2d0a569da28"
heading_path:
  - "B.2.5 — Supervisor-Subholon Feedback Loop"
  - "B.2.5:2 — Problem"
line_start: 32022
line_end: 32031
dependencies:
  - "A.1"
  - "A.15"
  - "A.2"
  - "A.2.1"
  - "A.3"
  - "A.3.4"
  - "A.7"
  - "B.2"
  - "C.30.LCA"
  - "U.RoleAssignment"
  - "U.Work"
keywords:
  - "control architecture"
  - "feedback loop"
  - "layered control"
  - "stability"
  - "supervisor"
---

### B.2.5:2 - Problem

Layered supervision is useful across engineered, biological, organizational, and epistemic cases, but it is easy to model incorrectly. The common error is to collapse three different structures into one drawing:

1. Structural composition: part-whole or structural composition of a holon.
2. Supervisory relation: an acting system or acting holon holding the supervisor role through current `U.RoleAssignment` in a bounded context, the supervised holon set, and the transformation, work, or constraint relation being governed.
3. Interaction or publication network: observation, signal, command, constraint, report, review, or publication channels through which the loop is enacted, observed, constrained, or revised.

When these are confused, a functional or supervisory layer is treated as a physical part, a publication is treated as an acting agent, a diagram is treated as proof, or a controller label is treated as a gate or assurance result.

