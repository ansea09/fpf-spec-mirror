---
chunk_kind: "child"
pattern_id: "A.2.1"
pattern_title: "U.RoleAssignment - Contextual Work-Role Assignment"
section_id: "A.2.1:6"
section_title: "Bias Annotation"
source_path: "FPF-Spec.md"
output_path: "by_section/A.2.1/A.2.1__008_bias-annotation.md"
commit_sha: "cf12b97913ff82ca8a45ba77d3658ad11e0fdeb6"
heading_path:
  - "A.2.1 — U.RoleAssignment - Contextual Work-Role Assignment"
  - "A.2.1:6 — Bias Annotation"
line_start: 2461
line_end: 2470
dependencies:
  - "A.15"
  - "A.2"
  - "A.2.1"
keywords:
  - "RCS/RSG"
  - "RoleEnactmentFact"
  - "Standard"
  - "context"
  - "holder"
  - "performedBy"
  - "role"
---

### A.2.1:6 - Bias Annotation

| Bias risk | Failure | Mitigation |
| --- | --- | --- |
| Semio-bias | The pattern starts talking mainly about reports, standards, records, cards, and publication forms. | Keep `U.RoleAssignment` as the primary EntityOfConcern. Treat descriptions and publications as neighboring epistemes. |
| Episteme-as-agent drift | A standard, report, dataset, proof, or model card is treated as if it performed work. | Use direct evidence-use, source-use, status-use, publication-use, requirement-use, definition-use, explanation-use, assurance-use, gate-use, or decision-use relations. |
| Slot-role drift | Holder, role value, context, window, justification, or provenance words become untyped fields. | Use `A.6.5` SlotSpec discipline and keep the filled values under their governing patterns. |
| Work-admission shortcut | A role assignment is treated as permission, gate passage, capability, or completed work. | Recover the direct work-admission, gate, capability, method, plan, or work claim before acting. |
| Notation bias | `Holder#Role:Context@Window` is treated as the ontology. | Use the notation only after the assignment relation and core slots are recoverable. |

