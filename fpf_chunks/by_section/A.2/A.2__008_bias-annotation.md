---
chunk_kind: "child"
pattern_id: "A.2"
pattern_title: "Role Taxonomy"
section_id: "A.2:6"
section_title: "Bias Annotation"
source_path: "FPF-Spec.md"
output_path: "by_section/A.2/A.2__008_bias-annotation.md"
commit_sha: "036c056e98c38522172c6b7b3ad08214281cc4e4"
heading_path:
  - "A.2 — Role Taxonomy"
  - "A.2:6 — Bias Annotation"
line_start: 2895
line_end: 2905
dependencies:
  - "A.1"
  - "A.1.1"
  - "A.13"
  - "A.15"
  - "A.2.1-A.2.6"
  - "A.6.0"
  - "A.6.5"
  - "A.6.REL"
  - "C.2.1"
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

| Bias risk | Failure | Repair |
| --- | --- | --- |
| Semio-bias | A role description or taxonomy publication is treated as the role value. | Keep the episteme and its publication relations separate from `U.Role`. |
| Global-label bias | Matching role labels are taken as matching meanings or sufficient permission for cross-scheme use. | Compare the role-taxonomy claims and exact sense cells. For a proposed cross-scheme use, require an obtaining F.9 Bridge, a separate C.2.1 bounded-use assertion, and current A.10 or B.3 reliance; infer neither role identity nor authorization. |
| Episteme-as-agent drift | A standard, report, dataset, or model is said to perform work. | Name the holder system and work occurrence; keep the episteme in its direct evidence, reliance, external-rule, or publication relation. |
| Slot-role drift | A value filling a relation participant slot is treated as a system-held role because the external notation labels that participant `role`. | Declare the exact SlotKind and ValueKind under `A.6.5`; use `U.Role` only for an actual enactment-facing role value. |
| Capability-role drift | Assignment is treated as proof of ability. | Use `A.2.2` and a separately stated capability-fit condition. |
| Method-role drift | A role value is treated as the method of work. | Keep method, method description, admission condition, and work occurrence under `A.3` and `A.15`. |

