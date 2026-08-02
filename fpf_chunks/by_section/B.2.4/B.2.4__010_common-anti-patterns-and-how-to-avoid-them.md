---
chunk_kind: "child"
pattern_id: "B.2.4"
pattern_title: "Capability and Functioning Whole Reidentification"
section_id: "B.2.4:7"
section_title: "Common Anti-Patterns and How to Avoid Them"
source_path: "FPF-Spec.md"
output_path: "by_section/B.2.4/B.2.4__010_common-anti-patterns-and-how-to-avoid-them.md"
commit_sha: "9a9a42e4d154021ca3f7415e0009a4214832f65f"
heading_path:
  - "B.2.4 — Capability and Functioning Whole Reidentification"
  - "B.2.4:7 — Common Anti-Patterns and How to Avoid Them"
line_start: 38121
line_end: 38130
dependencies:
  - "A.10"
  - "A.15"
  - "A.15.1"
  - "A.15.2"
  - "A.2.2"
  - "A.22"
  - "A.3.1"
  - "A.3.2"
  - "A.3.4"
  - "A.6.F"
  - "A.6.M"
  - "B.2"
  - "B.2.P"
  - "C.16"
  - "C.29"
  - "C.30"
  - "C.30.ASV"
  - "C.30.TFS-REL"
  - "E.18"
keywords:
---

### B.2.4:7 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Symptom | Repair |
| --- | --- | --- |
| Capability by declaration | A leader names a new capability, but the exact capability facts remain component-level or unknown. | Use A.2.2 and C.16 for the facts and A.10 for support; return to B.2 only if the existing-whole explanation fails. |
| Function as part | A function block is treated as a physical or organizational part. | Use A.6.F, C.30.TFS-REL, A.6.M, and architecture allocation owners. |
| Method chain as whole | A sequence of methods is called a new holon. | Recover method relation and work occurrence; return to B.2 only when a result holon is current. |
| Diagram as flow structure | A diagram or graph is treated as the transformation-flow structure itself. | Use C.29, E.17, C.30.AD, or publication owners unless the selected structure is recovered. |
| Metric jump as whole | A KPI improves and MHT is declared. | Use C.16, A.10, and existing-whole explanation first. |

