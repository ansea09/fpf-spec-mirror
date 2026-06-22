---
chunk_kind: "child"
pattern_id: "A.2.5"
pattern_title: "RoleStateRelation@BoundedContext - Role State Space and Enactable-State Admission"
section_id: "A.2.5:3"
section_title: "Forces"
source_path: "FPF-Spec.md"
output_path: "by_section/A.2.5/A.2.5__006_forces.md"
commit_sha: "9b6d71cff42a9ac45e46a2be2d9450f766868bc4"
heading_path:
  - "A.2.5 — RoleStateRelation@BoundedContext - Role State Space and Enactable-State Admission"
  - "A.2.5:3 — Forces"
line_start: 3768
line_end: 3778
dependencies:
  - "A.15"
  - "A.2.1"
keywords:
  - "RSG"
  - "enactability"
  - "role state"
  - "role-state evolution"
  - "state machine"
---

### A.2.5:3 - Forces

| Force | Tension |
| --- | --- |
| Minimal use vs safety | Ordinary use needs a small state list; high-consequence work needs windowed state assertions and evidence. |
| Role assignment vs role state | `U.RoleAssignment` says who holds the role; `RoleStateRelation@BoundedContext` says what states that role can be in and which states admit work. |
| State-machine clarity vs method-order drift | State diagrams are useful, but this pattern does not encode method order or work-order structure. |
| Authorization words vs capability | "Authorized", "permitted", and "ready" can be role states, but they do not create capability. |
| Status words vs episteme use | "Approved standard" or "validated dataset" may be an episteme status-use relation, not a work-facing role state. |
| Context reuse vs local meaning | State names are memorable, but their predicates and admission effect stay local to one bounded context unless a bridge or comparison relation is declared. |

