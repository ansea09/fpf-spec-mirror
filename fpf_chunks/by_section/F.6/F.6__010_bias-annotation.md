---
chunk_kind: "child"
pattern_id: "F.6"
pattern_title: "RoleAssignment and Performed-Work Attribution Check"
section_id: "F.6:8"
section_title: "Bias Annotation"
source_path: "FPF-Spec.md"
output_path: "by_section/F.6/F.6__010_bias-annotation.md"
commit_sha: "646b0b9b164f7c13258633a33b92d2d0a569da28"
heading_path:
  - "F.6 — RoleAssignment and Performed-Work Attribution Check"
  - "F.6:8 — Bias Annotation"
line_start: 73765
line_end: 73774
dependencies:
  - "A.15"
  - "A.15.1"
  - "A.2"
  - "A.2.1"
  - "A.2.2"
  - "A.2.5"
  - "A.3.1"
  - "A.3.2"
  - "A.6.5"
  - "E.10"
  - "E.10.ARCH"
  - "F.18"
  - "F.4"
  - "F.5"
  - "F.9"
  - "U.Role"
  - "U.RoleAssignment"
keywords:
  - "asserting status"
  - "conceptual moves"
  - "enactment"
  - "role assignment"
---

### F.6:8 - Bias Annotation

| Bias risk | Failure | Mitigation |
| --- | --- | --- |
| Semio-bias | The pattern starts explaining reports, standards, dashboards, model cards, logs, or publications instead of checking role assignment and work attribution. | Keep the primary check on holder, role, context, window, and performed-by relation. Send episteme uses to direct patterns. |
| Status-role drift | Status values are treated as a branch of role assignment because both can have holders, subjects, windows, or evidence. | Status-use statements go to `F.10` or the direct status pattern. F.6 handles work-facing role assignment only. |
| Enactment reification | `RoleEnactment` becomes a separate root kind or object that competes with `U.Work`. | Use direct `Work.performedBy = RoleAssignment`; use `RoleEnactmentFact` only as a named derived fact. |
| Notation authority | A compact string is treated as if it were the relation. | Recover the typed SlotSpecs through `A.2.1`; the string is only shorthand or source wording. |
| Bridge overreach | Cross-context similarity licenses local assignment. | Keep assignment local; use `F.9` only for the cross-context bridge claim. |

