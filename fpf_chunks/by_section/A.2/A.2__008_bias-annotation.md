---
chunk_kind: "child"
pattern_id: "A.2"
pattern_title: "Role Taxonomy"
section_id: "A.2:6"
section_title: "Bias Annotation"
source_path: "FPF-Spec.md"
output_path: "by_section/A.2/A.2__008_bias-annotation.md"
commit_sha: "9a9a42e4d154021ca3f7415e0009a4214832f65f"
heading_path:
  - "A.2 — Role Taxonomy"
  - "A.2:6 — Bias Annotation"
line_start: 2903
line_end: 2912
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

### A.2:6 - Bias Annotation

| Bias risk | Failure | Mitigation |
| --- | --- | --- |
| Semio-bias | The pattern starts talking mainly about descriptions of roles, cards, records, and publications. | Keep `U.Role` as the EntityOfConcern. Descriptions and publications are neighboring epistemes. |
| Episteme-as-agent drift | A document, proof, standard, dataset, or model card is treated as if it acted. | Use evidence-use, source-use, status-use, publication-use, requirement-use, definition-use, explanation-use, or assurance-use relations. |
| Slot-role drift | Role is used as a generic slot position. | Use `A.6.5` for SlotKind and relation positions; keep `U.Role` for enactment-facing role values. |
| Capability-role drift | A role name is treated as ability. | Use `A.2.2` for capability; role assignment may cite capability-fit conditions but does not create ability. |
| Method-role drift | A role name is treated as the method itself. | Use `A.15`, `A.3.1`, and `A.3.2` for method and method-description claims. |

