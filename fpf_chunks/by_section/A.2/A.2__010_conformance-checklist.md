---
chunk_kind: "child"
pattern_id: "A.2"
pattern_title: "Role Taxonomy"
section_id: "A.2:8"
section_title: "Conformance Checklist"
source_path: "FPF-Spec.md"
output_path: "by_section/A.2/A.2__010_conformance-checklist.md"
commit_sha: "9b6d71cff42a9ac45e46a2be2d9450f766868bc4"
heading_path:
  - "A.2 — Role Taxonomy"
  - "A.2:8 — Conformance Checklist"
line_start: 2200
line_end: 2214
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

### A.2:8 - Conformance Checklist

| ID | Check |
| --- | --- |
| CC-A2.1 | A `U.Role` is a role value, not a system subtype, part, capability, method, work occurrence, commitment, obligation, permission, description, publication, or SlotKind. |
| CC-A2.2 | A `U.RoleAssignment` holder is a `U.System` or acting holon admitted as system-like performer by the governing work or method pattern. |
| CC-A2.3 | An episteme used as evidence, source, standard, definition, requirement, explanation, status bearer, publication, or assurance input is not a `U.RoleAssignment` holder. |
| CC-A2.4 | Role claims name or recover the bounded context that gives the role value its local meaning. |
| CC-A2.5 | Work claims cite the holder under `U.RoleAssignment`; the role value itself does not act. |
| CC-A2.6 | Capability requirements are governed by `A.2.2`, not hidden inside the role value. |
| CC-A2.7 | Method and method-description requirements are governed by `A.15`, `A.3.1`, and `A.3.2`, not hidden inside the role value. |
| CC-A2.8 | Role-requirement substitution, incompatibility, qualification, and bundles are context-local role relation structure under `A.2.7`, not mereology and not system-kind subsumption. |
| CC-A2.9 | Relation argument positions and SlotKinds are governed by `A.6.5`; they do not become `U.Role`. |
| CC-A2.10 | Role descriptions, role cards, registers, and publications describe, cite, or store role values or assignments; they are not the role value by default. |

