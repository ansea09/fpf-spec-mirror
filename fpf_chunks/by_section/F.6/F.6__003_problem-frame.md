---
chunk_kind: "child"
pattern_id: "F.6"
pattern_title: "RoleAssignment and Performed-Work Attribution Check"
section_id: "F.6:1"
section_title: "Problem Frame"
source_path: "FPF-Spec.md"
output_path: "by_section/F.6/F.6__003_problem-frame.md"
commit_sha: "2ada413629b846ef308222d16489a82cb5b40a71"
heading_path:
  - "F.6 — RoleAssignment and Performed-Work Attribution Check"
  - "F.6:1 — Problem Frame"
line_start: 89927
line_end: 89934
dependencies:
  - "A.1.1"
  - "A.10"
  - "A.15"
  - "A.15.1"
  - "A.15.4"
  - "A.2"
  - "A.2.1"
  - "A.2.2"
  - "A.2.5"
  - "A.3.1"
  - "A.3.2"
  - "A.6.REL"
  - "E.10"
  - "E.17"
  - "F.18"
  - "F.4"
  - "F.5"
  - "F.9"
  - "U.Role"
  - "U.RoleAssignment"
  - "U.Work"
keywords:
  - "actual performing U.System"
  - "assignment coverage"
  - "exact U.RoleAssignment"
  - "performedUnderAssignment"
  - "separate assertion and evidence"
  - "world-side attribution"
---

### F.6:1 - Problem Frame

`U.RoleAssignment` admits assignment-relation occurrences; `U.Work` admits Work individuals. One exact `RA : U.RoleAssignment` is a world-side assignment-relation occurrence that relates an admitted holder System to one role value, one role-taxonomy episteme, and one effective reference scheme and obtains throughout one assignment episode. One exact `W : U.Work` is a dated world-side Work occurrence. The existence of `RA` and `W` does not by itself establish the additional world-side attribution between them: `performedUnderAssignment(W, RA)` must separately obtain. A distinct assertion or record may designate `RA` and `W`, state that `RA` obtains, state that `W` occurred, or state that the attribution relation obtains.

F.6 governs the missing direct relation. The assignment is one participant and the work occurrence is the other. A roster row may assert the assignment; a work log may assert the work and attribution; evidence may support either assertion. Those epistemes help a system know or use the relation, but they do not become relation participants and do not make the world-side relation obtain merely by being recorded.

This separation matters because assignment, state, ability, performance, evidence, and acceptance can vary independently. A system can hold a role and do no work. It can perform poor work under a valid assignment. A report can accurately describe the work without performing it. One compact "enactment" label hides these distinctions.

