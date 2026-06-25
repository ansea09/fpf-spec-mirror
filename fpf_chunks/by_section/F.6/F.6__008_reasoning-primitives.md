---
chunk_kind: "child"
pattern_id: "F.6"
pattern_title: "RoleAssignment and Performed-Work Attribution Check"
section_id: "F.6:6"
section_title: "Reasoning Primitives"
source_path: "FPF-Spec.md"
output_path: "by_section/F.6/F.6__008_reasoning-primitives.md"
commit_sha: "6bbbb622859fbbcddc02b23ea76bee4dd71c6291"
heading_path:
  - "F.6 — RoleAssignment and Performed-Work Attribution Check"
  - "F.6:6 — Reasoning Primitives"
line_start: 80855
line_end: 80879
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

### F.6:6 - Reasoning Primitives

```text
RoleDescription RD describes Role R in Context C
  and Holder H is admitted for R in C
  -> candidate RoleAssignment(H, R, C).
```

```text
RoleAssignment RA is admitted
  and Work W is a current U.Work occurrence
  and W performedBy RA is admitted
  -> RoleEnactmentFact(W, RA) may be named.
```

```text
Source episteme E is used as evidence, standard, requirement, source, publication, or status bearer
  -> no RoleAssignment holder is recovered from that use alone.
```

```text
Role-like label L comes from another bounded context
  -> no assignment substitution without F.9 bridge and local A.2.1 check.
```

