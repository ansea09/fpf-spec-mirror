---
chunk_kind: "child"
pattern_id: "C.28.MR"
pattern_title: "Derive an Intervention Consequence by Mechanism Replacement"
section_id: "C.28.MR:8"
section_title: "Common Anti-Patterns and How to Avoid Them"
source_path: "FPF-Spec.md"
output_path: "by_section/C.28.MR/C.28.MR__009_common-anti-patterns-and-how-to-avoid-them.md"
commit_sha: "76efec98642d04026281c164a3a1ff840e787be5"
heading_path:
  - "C.28.MR — Derive an Intervention Consequence by Mechanism Replacement"
  - "C.28.MR:8 — Common Anti-Patterns and How to Avoid Them"
line_start: 63835
line_end: 63845
dependencies:
  - "A.3.3.TR"
  - "B.5.MPC"
  - "B.5.RR"
  - "C.28"
  - "C.29.1"
keywords:
---

### C.28.MR:8 - Common Anti-Patterns and How to Avoid Them

| Recurring difficulty | What fails | Useful repair |
| --- | --- | --- |
| Substitute a conditional probability for an intervention | Selection on an observation changes the input information while leaving the natural mechanisms in place. | Replace the targeted mechanism and derive under the intended input law, as in :5.1. |
| Force a displayed number and infer a changed load | The changed expression belongs to a measurement or interface that does not determine the physical quantity. | Locate the actuator or subject mechanism and compare the replacements, as in :5.2. |
| Freeze all other variable values | Downstream effects of the replacement disappear from the calculation. | Preserve the other functions and recompute their outputs. |
| Resample shared disturbances independently | The computation describes another dependence structure. | Generate the retained joint inputs and reuse their common causes. |
| Keep the first numerical branch | A chosen solution hides other admitted answers to the query. | Test whether alternatives change that answer; retain a bound or a stated selection condition when they do. |
| Use a static answer for a later controlled state | The intervention's duration, event order or feedback has been omitted. | Add the relevant continuation rule and horizon before deriving the later result. |

