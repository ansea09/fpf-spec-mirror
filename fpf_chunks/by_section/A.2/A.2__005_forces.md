---
chunk_kind: "child"
pattern_id: "A.2"
pattern_title: "Role Taxonomy"
section_id: "A.2:3"
section_title: "Forces"
source_path: "FPF-Spec.md"
output_path: "by_section/A.2/A.2__005_forces.md"
commit_sha: "3bc659a6f866071f629bf41fc2dd41f2518e579a"
heading_path:
  - "A.2 — Role Taxonomy"
  - "A.2:3 — Forces"
line_start: 2071
line_end: 2081
dependencies:
  - "A.1"
  - "A.1.1"
  - "A.13"
  - "A.15"
  - "A.2.1-A.2.6"
  - "A.6.5"
  - "A.6.RSIR"
  - "E.24"
keywords:
  - "U.RoleAssignment"
  - "assignment"
  - "context"
  - "function vs identity"
  - "holder"
  - "responsibility"
  - "role"
---

### A.2:3 - Forces

| Force | Tension |
| --- | --- |
| Context reuse vs type explosion | One role value can be reused inside a bounded context; making every contextual use a system subtype loses reuse. |
| Role identity vs assignment relation | `U.Role` must stay a role value, while `U.RoleAssignment` links holder, role, context, and window. |
| Role boundary vs false role holon | A role decomposition may be useful, but A.2 must route factors, responsibilities, permissions, obligations, role states, capability-fit conditions, and method role-admission conditions to their direct owners instead of treating them as role parts. |
| Ordinary speech vs FPF kind discipline | "Role of X" is common language, but FPF must recover whether X is a holder, source, evidence, status bearer, method, work, relation argument, or publication. |
| Work-facing roles vs episteme use | Systems perform work, including physical and operational work by motors, pumps, devices, organisms, services, teams, and people; epistemes are used, cited, asserted, published, evaluated, refreshed, or relied on through direct relations. |
| Minimal kernel vs practical traceability | A small role kernel is useful only if it can still connect to role descriptions, role states, role relation structure, capability-fit conditions, method role-admission conditions, work, and evidence about performed work. |

