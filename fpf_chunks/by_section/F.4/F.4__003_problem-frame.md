---
chunk_kind: "child"
pattern_id: "F.4"
pattern_title: "Role Description (RCS + RoleStateGraph + Checklists)"
section_id: "F.4:2"
section_title: "Problem frame"
source_path: "FPF-Spec.md"
output_path: "by_section/F.4/F.4__003_problem-frame.md"
commit_sha: "7c617d5d0fa1abf94a21bac2dd909f68ed514249"
heading_path:
  - "F.4 — Role Description (RCS + RoleStateGraph + Checklists)"
  - "F.4:2 — Problem frame"
line_start: 72481
line_end: 72489
dependencies:
  - "A.11"
  - "A.2.1"
  - "A.7"
  - "B.3"
  - "D.CTX"
  - "E.10.D1"
  - "E.10.D2"
  - "F.1"
  - "F.2"
  - "F.3"
  - "F.5"
  - "F.6"
  - "F.7"
  - "F.8"
  - "F.9"
  - "U.RoleAssignment"
  - "U.Types"
keywords:
  - "Role Characterisation Space (RCS)"
  - "RoleStateGraph (RSG)"
  - "invariants"
  - "role template"
  - "status template"
---

### F.4:2 - Problem frame

Without explicit Role Descriptions:

1. **Role/status conflation.** Access **role** (RBAC) treated as behavioural **mask** (BPMN participant); deontic **duty** treated as runtime **effect**.
2. **Context drift.** A “role” quietly starts meaning different things across canons; later assignments contradict each other.
3. **Hidden commitments.** We name a role assignment or status assertion but never state what **must hold** when it is assigned; downstream reasoning becomes arbitrary.
4. **Premature unification.** A single template tries to straddle several Contexts; losses remain implicit.

