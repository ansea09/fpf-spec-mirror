---
chunk_kind: "child"
pattern_id: "A.2.7"
pattern_title: "RoleRelationStructure@BoundedContext - Context-Local Role Relations and Representation-Lens Boundary"
section_id: "A.2.7:8"
section_title: "Anti-Patterns and Repairs"
source_path: "FPF-Spec.md"
output_path: "by_section/A.2.7/A.2.7__010_anti-patterns-and-repairs.md"
commit_sha: "cf12b97913ff82ca8a45ba77d3658ad11e0fdeb6"
heading_path:
  - "A.2.7 — RoleRelationStructure@BoundedContext - Context-Local Role Relations and Representation-Lens Boundary"
  - "A.2.7:8 — Anti-Patterns and Repairs"
line_start: 5058
line_end: 5069
dependencies:
  - "A.15"
  - "A.2"
  - "A.2.5"
keywords:
  - "bundles (⊗)"
  - "incompatibility (⊥)"
  - "requiredRoles substitution"
  - "role algebra"
  - "separation of duties (SoD)"
  - "specialization (≤)"
---

### A.2.7:8 - Anti-Patterns and Repairs

| Anti-pattern | Symptom | Repair |
|---|---|---|
| Role relation structure as type hierarchy | `EngineerRole <= HumanSystem`. | Keep role relation over `U.Role` values; use kind taxonomy only for kinds. |
| Role relation structure as org chart | "Manager is above Engineer, therefore satisfies Engineer." | Declare same-context role-requirement substitution only when that role-requirement relation is intended. |
| Role-requirement substitution as capability model | "Senior role implies precision capability." | Keep the substitution relation separate; add `U.Capability` claim for measured ability if current. |
| Bundle as new holder | `IncidentLeadOnCall` is treated as a person or team. | Treat it as role-bundle expression unless a role value or holder is separately declared. |
| Incompatibility as slogan | "Approver is independent" without relation. | State the incompatible role values, holder relation, bounded context, and overlapping window condition. |
| Cross-context label equivalence | Same role label in two contexts is treated as the same role relation structure. | Use F-family bridge or naming patterns; do not import role relations by label. |
| Episteme as role relation structure | A standard, report, or dashboard is put into role relation structure. | Use `C.2.1`, `A.10`, `B.3`, `E.17.*`, `E.24.PUB`, or `A.7` for the source, evidence, status, assurance, publication, description, or strict-distinction claim being made. |

