---
chunk_kind: "child"
pattern_id: "F.6"
pattern_title: "RoleAssignment and Performed-Work Attribution Check"
section_id: "F.6:9"
section_title: "Conformance Checklist"
source_path: "FPF-Spec.md"
output_path: "by_section/F.6/F.6__011_conformance-checklist.md"
commit_sha: "b74ecf2b633a2315086198e4aab07c2b61257c27"
heading_path:
  - "F.6 — RoleAssignment and Performed-Work Attribution Check"
  - "F.6:9 — Conformance Checklist"
line_start: 77609
line_end: 77625
dependencies:
  - "A.15"
  - "A.15.1"
  - "A.2"
  - "A.2.1"
  - "A.2.2"
  - "A.2.5"
  - "A.3.1"
  - "A.3.2"
  - "A.6.5"
  - "E.10"
  - "E.10.ARCH"
  - "F.18"
  - "F.4"
  - "F.5"
  - "F.9"
  - "U.Role"
  - "U.RoleAssignment"
keywords:
  - "asserting status"
  - "conceptual moves"
  - "enactment"
  - "role assignment"
---

### F.6:9 - Conformance Checklist

Use this checklist when applying F.6.

1. The candidate role is a `U.Role` in one bounded context, not only a source label.
2. The candidate holder is a system or acting holon admitted by `A.2.1`.
3. The assignment window is filled, inherited, unknown, not asserted, or not current for this claim.
4. If role state matters, an `A.2.5` role-state admission or blocker is named.
5. If capability matters, an `A.2.2` capability relation or blocker is named.
6. If method or method description matters, `A.3.1`, `A.3.2`, or `A.15` is named.
7. If actual work is claimed, the `U.Work` occurrence is named under `A.15.1`.
8. Performed work uses `Work.performedBy = RoleAssignment` or `RoleEnactmentFact`, not `U.RoleEnactment`.
9. Status, evidence, source, standard, requirement, publication, assurance, gate, and decision uses are not encoded as role assignment.
10. Cross-context role-like reuse is represented by `F.9` and does not mutate the local assignment.
11. Compact notation is unfolded to typed assignment slots before reliance-bearing use.
12. `NotCarried` names the strongest tempting overclaim that this F.6 check does not make.

