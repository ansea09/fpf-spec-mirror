---
chunk_kind: "child"
pattern_id: "A.2.1"
pattern_title: "U.RoleAssignment - System Role Assignment"
section_id: "A.2.1:6"
section_title: "Bias Annotation"
source_path: "FPF-Spec.md"
output_path: "by_section/A.2.1/A.2.1__008_bias-annotation.md"
commit_sha: "036c056e98c38522172c6b7b3ad08214281cc4e4"
heading_path:
  - "A.2.1 — U.RoleAssignment - System Role Assignment"
  - "A.2.1:6 — Bias Annotation"
line_start: 3216
line_end: 3226
dependencies:
  - "A.1.1"
  - "A.15"
  - "A.15.1"
  - "A.2"
  - "A.2.2"
  - "A.2.5"
  - "A.2.7"
  - "A.3.1"
  - "A.3.2"
  - "A.6.5"
  - "A.6.9"
  - "A.6.REL"
  - "C.2.1"
  - "F.6"
  - "F.9"
  - "U.Role"
keywords:
  - "AssignmentInterval"
  - "assignment occurrence"
  - "effective ReferenceScheme"
  - "holder System"
  - "performedUnderAssignment"
  - "role value"
  - "role-taxonomy episteme"
---

### A.2.1:6 - Bias Annotation

| Bias risk | Failure | Repair |
| --- | --- | --- |
| Record-first bias | A roster row or database identifier is treated as the assignment occurrence. | State the assignment predicate and apply the direct occurrence-identity rule; keep the row as an assertion or publication. |
| Universal-context bias | Every assignment receives a `U.BoundedContext` or optional model-use participant. | Use the four exact generic participants; place any selected model-use structure in the receiving assertion or use. |
| Assignment-as-work drift | Current assignment is treated as evidence that work happened. | Name exact dated `U.Work` `W`, exact assignment `RA`, and the admitted holder System `S = RA.HolderSystemSlot`; state that `S` performed `W` under `RA` through `F.6` `performedUnderAssignment(W, RA)`. |
| Assignment-as-capability drift | Holding a role is treated as proof of ability. | Use `A.2.2` and a capability-fit relation. |
| Episteme-as-holder drift | A standard, report, model, or dataset fills `HolderSystemSlot`. | Keep the episteme in its direct evidence, reliance, external-rule, or publication relation. |
| Structure-qualification drift | A selected model-use structure is appended to the generic signature without changing its obtaining law. | Keep the designation in the receiving assertion or use; admit a dependent species only through its own direct pattern and stronger identity law. |

