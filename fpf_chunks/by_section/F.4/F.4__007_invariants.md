---
chunk_kind: "child"
pattern_id: "F.4"
pattern_title: "Role Description - Description Episteme for U.Role"
section_id: "F.4:5"
section_title: "Invariants"
source_path: "FPF-Spec.md"
output_path: "by_section/F.4/F.4__007_invariants.md"
commit_sha: "646b0b9b164f7c13258633a33b92d2d0a569da28"
heading_path:
  - "F.4 — Role Description - Description Episteme for U.Role"
  - "F.4:5 — Invariants"
line_start: 72986
line_end: 72998
dependencies:
  - "A.15"
  - "A.15.1"
  - "A.15.2"
  - "A.2"
  - "A.2.1"
  - "A.2.2"
  - "A.2.5"
  - "A.2.7"
  - "A.6.5"
  - "A.7"
  - "C.2.1"
  - "E.10.D2"
  - "E.24"
  - "F.10"
  - "F.14"
  - "F.15"
  - "F.18"
  - "F.3"
  - "F.6"
  - "F.8"
  - "F.9"
keywords:
  - "Role Characterisation Space (RCS)"
  - "RoleStateGraph (RSG)"
  - "invariants"
  - "role template"
  - "status template"
---

### F.4:5 - Invariants

1. **One described role.** A role description describes exactly one `U.Role` value in the current application.
2. **One bounded context.** The role description is local to one `U.BoundedContext`; cross-context reuse needs `F.9`.
3. **Description boundary.** The role description is a `U.Episteme`; it is not the role value, assignment relation, holder, capability, method, work, or status-use relation.
4. **Work-facing holder boundary.** The holder admitted by a role assignment is a system or acting holon admitted by the governing work or method pattern. An episteme is not a role holder because it is used as evidence, source, standard, requirement, definition, explanation, status bearer, publication, or assurance input.
5. **No hidden capability.** Capability requirements may be referenced, but the role description does not prove capability.
6. **No hidden method.** Method requirements may be referenced, but the role description is not a method description.
7. **No hidden work.** A role description may enable work attribution checks, but it is not evidence that work occurred.
8. **No status-template fusion.** Status-use and evidence-use relations are direct relations, not a second branch of role description.
9. **Slot discipline.** If a source says "role" for a relation position, recover `SlotKind`, `ValueKind`, and `RefKind` through `A.6.5`.
10. **Name after meaning.** Durable naming follows `F.18` only after role value, context, and local sense are recovered.

