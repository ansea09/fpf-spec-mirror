---
chunk_kind: "child"
pattern_id: "B.2.4"
pattern_title: "Do Capability or Functioning Changes Require Whole Reidentification?"
section_id: "B.2.4:7"
section_title: "Common Anti-Patterns and How to Avoid Them"
source_path: "FPF-Spec.md"
output_path: "by_section/B.2.4/B.2.4__010_common-anti-patterns-and-how-to-avoid-them.md"
commit_sha: "870fb0c2a5dcfe1e0165a111fdf2cf8659c85a54"
heading_path:
  - "B.2.4 — Do Capability or Functioning Changes Require Whole Reidentification?"
  - "B.2.4:7 — Common Anti-Patterns and How to Avoid Them"
line_start: 44567
line_end: 44576
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
| Capability by declaration | A leader names a new capability, but the exact capability facts remain component-level or unknown. | Test the capability claim under A.2.2; use C.16 for a measured-characteristic claim and A.10 when a replayable source-to-use account is needed. Use B.2 if a consequential whole-reidentification question remains. |
| Function as part | A function block is treated as a physical or organizational part. | Recover the actual functioning, allocation or parthood claim under its direct pattern. Use A.6.F or A.6.M for unresolved function-like or module/interface wording; use E.18, C.30.TFS-REL, C.30, A.22 or C.30.ASV only for the corresponding live flow, architecture, selected-structure or view claim. |
| Method chain as whole | A sequence of methods is called a new holon. | Recover the exact method relation and any current work occurrence; use B.2 when those facts leave a consequential whole-reidentification question. |
| Diagram as flow structure | A diagram or graph is treated as the transformation-flow structure itself. | Use the applicable description, publication, mathematical-lens, or selected-structure pattern; use B.2.4 only after the selected structure is recovered and a whole-reidentification question remains. |
| Metric jump as whole | A KPI improves and MHT is declared. | Test the characteristic claim under its subject pattern and perform the existing-whole comparison. Use A.10 when a replayable source-to-use account is needed. |

