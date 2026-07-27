---
chunk_kind: "child"
pattern_id: "A.2.5"
pattern_title: "RoleStateRelation@BoundedContext - Role State Space and Enactable-State Admission"
section_id: "A.2.5:11"
section_title: "Rationale"
source_path: "FPF-Spec.md"
output_path: "by_section/A.2.5/A.2.5__014_rationale.md"
commit_sha: "66e732dfef7a4a93ff23eec43b3f759a6664652d"
heading_path:
  - "A.2.5 — RoleStateRelation@BoundedContext - Role State Space and Enactable-State Admission"
  - "A.2.5:11 — Rationale"
line_start: 4276
line_end: 4281
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

### A.2.5:11 - Rationale

FPF keeps role state separate because the surrounding values have different kinds and different failure modes. A role assignment can be valid while the role state is not work-admitting. A holder can be capable while the assignment window is stale. A method can require a role while no current holder has an enactable state. A publication can describe or evidence any of these without becoming the holder, the role, or the state.

The state-machine lens is useful because finite named states, guarded change, and state assertions are easy to inspect. But the pattern does not make every role claim executable behavior. It uses the state lens only where the project needs role-state recognition, admission, currentness, and state-aware role relation structure.

