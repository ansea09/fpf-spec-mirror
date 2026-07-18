---
chunk_kind: "child"
pattern_id: "A.2"
pattern_title: "Role Taxonomy"
section_id: "A.2:11"
section_title: "Rationale"
source_path: "FPF-Spec.md"
output_path: "by_section/A.2/A.2__013_rationale.md"
commit_sha: "1d5c1edd154b636a446b3887a6094be60c60faff"
heading_path:
  - "A.2 — Role Taxonomy"
  - "A.2:11 — Rationale"
line_start: 2318
line_end: 2329
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

### A.2:11 - Rationale

Roles are needed because holons participate in different contexts without changing their substantial identity. A role value gives this context-local participation a name. The pump remains the same pump while being a cooling circulator in one context and test article in another. The engineer remains the same person while holding verifier or author roles in different work packages.

The selected ontology keeps three levels separate:

1. `U.Role`: the context-bound role value.
2. `U.RoleAssignment`: the typed relation value linking holder, role, context, and window.
3. Neighboring values: capability, method, method description, work plan, work occurrence, evidence-use relation, status-use relation, source-use relation, publication-use relation, and role description.

This is a compact architecture. It avoids type explosion, but it also avoids the opposite error of making role a generic slot word for anything that participates in anything else. A role is a real role value when an admitted `U.System` holder is being something in a bounded context for work, transformation, functioning, method, or attribution. Other participation claims use their own relation patterns.

