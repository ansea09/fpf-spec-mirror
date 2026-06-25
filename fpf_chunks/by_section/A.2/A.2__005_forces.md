---
chunk_kind: "child"
pattern_id: "A.2"
pattern_title: "Role Taxonomy"
section_id: "A.2:3"
section_title: "Forces"
source_path: "FPF-Spec.md"
output_path: "by_section/A.2/A.2__005_forces.md"
commit_sha: "b0368ed8d883c04d0b261b03f46c28e23d790dc5"
heading_path:
  - "A.2 — Role Taxonomy"
  - "A.2:3 — Forces"
line_start: 1975
line_end: 1984
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
| Ordinary speech vs FPF kind discipline | "Role of X" is common language, but FPF must recover whether X is a holder, source, evidence, status bearer, method, work, relation argument, or publication. |
| Work-facing roles vs episteme use | Systems and acting holons perform work; epistemes are used, cited, asserted, published, evaluated, refreshed, or relied on through direct relations. |
| Minimal kernel vs practical traceability | A small role kernel is useful only if it can still connect to role descriptions, role states, role relation structure, capability requirements, method requirements, work, and evidence about performed work. |

