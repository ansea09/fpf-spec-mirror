---
chunk_kind: "child"
pattern_id: "A.2.5"
pattern_title: "RoleStateRelation@BoundedContext - Role State Space and Enactable-State Admission"
section_id: "A.2.5:2"
section_title: "Problem"
source_path: "FPF-Spec.md"
output_path: "by_section/A.2.5/A.2.5__005_problem.md"
commit_sha: "17edd955485f60cafb16159c7d90e20f4ad21844"
heading_path:
  - "A.2.5 — RoleStateRelation@BoundedContext - Role State Space and Enactable-State Admission"
  - "A.2.5:2 — Problem"
line_start: 4038
line_end: 4049
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

### A.2.5:2 - Problem

Without this pattern:

1. **Assignment and state collapse.** A holder assigned to a role is treated as currently ready.
2. **Role and capability collapse.** A state label such as "ready" is treated as ability instead of a window-bounded state assertion.
3. **Role state and work collapse.** Being in a state is mistaken for having performed the work.
4. **State and source collapse.** A certificate, report, standard, model card, dashboard, or publication is treated as the state itself rather than as a source or evidence relation for a state assertion.
5. **Label-only incompatibility appears.** Incompatibility checks block or admit work by role names rather than by enactable states in a window.
6. **Context drift returns.** "Approved" or "Ready" travels across contexts without named state predicates or loss.
7. **Enactment reification survives.** `RoleEnactment` becomes a durable root value even though performed work is governed by `U.Work` and `U.RoleAssignment`.

