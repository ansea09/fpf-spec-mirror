---
chunk_kind: "child"
pattern_id: "C.32.LCA"
pattern_title: "Construct and Compare a Control Architecture"
section_id: "C.32.LCA:2"
section_title: "Problem"
source_path: "FPF-Spec.md"
output_path: "by_section/C.32.LCA/C.32.LCA__003_problem.md"
commit_sha: "3f6e02840fe3a22427aed590f9688a9c8f6bf5c8"
heading_path:
  - "C.32.LCA — Construct and Compare a Control Architecture"
  - "C.32.LCA:2 — Problem"
line_start: 75819
line_end: 75826
dependencies:
  - "A.3.3.PI"
  - "B.2.5"
  - "C.30.LCA"
  - "C.32"
  - "C.32.MWA.PP"
keywords:
---

### C.32.LCA:2 - Problem

Separately reasonable choices can be incompatible when connected. A planner assumes immediate execution; an executor receives a stale state; two units allocate the same scarce resource; a requested exception requires authority outside the decision window. Each local description can be correct while the intended result remains unobtainable.

A familiar layered drawing does not resolve these dependencies. Nor does naming “strategy, planning and execution”: the designer still needs to determine which choices belong together, what information crosses a boundary, how long each contribution may take, and what remains possible when a premise fails.

The practical problem is to construct and compare those relations without losing the purpose, physical or organizational constraints, or the costs introduced by separation. The result must explain both how the arrangement can continue and which feedback calls for a different action, goal or architecture.

