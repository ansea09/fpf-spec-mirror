---
chunk_kind: "child"
pattern_id: "A.2"
pattern_title: "Role Taxonomy"
section_id: "A.2:8"
section_title: "Conformance Checklist"
source_path: "FPF-Spec.md"
output_path: "by_section/A.2/A.2__010_conformance-checklist.md"
commit_sha: "b7ec5a0b1dfa4bdae4cf055188219e89cef61a63"
heading_path:
  - "A.2 — Role Taxonomy"
  - "A.2:8 — Conformance Checklist"
line_start: 2915
line_end: 2930
dependencies:
  - "A.1"
  - "A.1.1"
  - "A.13"
  - "A.15"
  - "A.2.1-A.2.6"
  - "A.6.0"
  - "A.6.5"
  - "A.6.REL"
  - "C.2.1"
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

### A.2:8 - Conformance Checklist

| ID | Check |
| --- | --- |
| CC-A2.1 | The current role claim names an enactment-facing `U.Role` value held by an admitted `U.System`. |
| CC-A2.2 | Role interpretation names the role-taxonomy episteme and effective `U.ReferenceScheme`. |
| CC-A2.3 | A relied-on assignment claim uses `U.RoleAssignment` with holder system, role value, role-taxonomy episteme, and effective reference scheme as its four participants; the assignment extent is described separately. |
| CC-A2.4 | Role-state, capability-fit, method-admission, work, transformation, responsibility, evidence, and reliance claims remain direct neighboring relations. |
| CC-A2.5 | An episteme is not made a role holder because a system uses it in a description, constraint, evidence, reliance, or publication relation. |
| CC-A2.6 | A relation participant uses an exact SlotSpec; an external participant label does not create `U.Role` or a role assignment. |
| CC-A2.7 | A proposed role decomposition is resolved through `A.2.7` and direct neighboring patterns; `U.Role` is not placed in a `partOf` chain. |
| CC-A2.8 | Matching labels under different taxonomies or schemes are not treated as identity evidence. |
| CC-A2.9 | Any selected model-use structure is designated by the receiving assertion or use; no optional `ModelUseStructureSlot` is added to a generic role relation. |
| CC-A2.10 | A selected model-use structure, when current for a receiving interpretation, neither holds nor assigns the role and does not replace the role taxonomy or effective scheme. |
| CC-A2.11 | Any cross-scheme role use cites the exact obtaining F.9 Bridge, states a separate C.2.1 assertion with its bounded use, direction, rule, tolerance, polarity, and effective scheme, and recovers current A.10 or B.3 reliance; a Bridge Card is not a use licence and any use that occurred remains under its direct owner. |

