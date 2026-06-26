---
chunk_kind: "child"
pattern_id: "F.6"
pattern_title: "RoleAssignment and Performed-Work Attribution Check"
section_id: "F.6:12"
section_title: "Rationale"
source_path: "FPF-Spec.md"
output_path: "by_section/F.6/F.6__014_rationale.md"
commit_sha: "40b232f11ed950ed34082273c57ff4f6c45b7f06"
heading_path:
  - "F.6 — RoleAssignment and Performed-Work Attribution Check"
  - "F.6:12 — Rationale"
line_start: 81724
line_end: 81729
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

### F.6:12 - Rationale

`U.RoleAssignment` is first-class because work attribution needs a stable holder-role-context relation. `RoleEnactmentFact` is not first-class because the fact is derived from a work occurrence and its `performedBy` assignment. Status-use and evidence-use relations are not branches of role assignment because their EntityOfConcern and slot discipline differ: they qualify claims, epistemes, standards, requirements, publications, gates, or decisions rather than assigning acting holders to work-facing roles.

The pattern is deliberately thinner than `A.15`. It does not rebuild the full role-method-work alignment. It gives Part F a local check that keeps role-description, naming, bridge, status, and work-attribution uses from crossing wires.

