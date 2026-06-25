---
chunk_kind: "child"
pattern_id: "A.2"
pattern_title: "Role Taxonomy"
section_id: "A.2:7"
section_title: "Working Guidance"
source_path: "FPF-Spec.md"
output_path: "by_section/A.2/A.2__009_working-guidance.md"
commit_sha: "b0368ed8d883c04d0b261b03f46c28e23d790dc5"
heading_path:
  - "A.2 — Role Taxonomy"
  - "A.2:7 — Working Guidance"
line_start: 2161
line_end: 2170
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

### A.2:7 - Working Guidance

1. Start with the source phrase and recover the current project concern.
2. If the phrase names what an acting system or acting holon is being in a bounded context, recover a `U.Role` value.
3. If the phrase names the holder-role-context-window relation, recover `U.RoleAssignment` under `A.2.1`.
4. If the phrase names ability, recover capability under `A.2.2`.
5. If the phrase names performed work, intended work, or governing method, use `A.15` and its neighboring method and work patterns.
6. If the phrase names evidence, source, standard, requirement, definition, explanation, publication, status, assurance, or gate use of an episteme, use the direct episteme-use relation pattern.
7. If the phrase only names a relation position, field, parameter, or argument, use `A.6.5`.

