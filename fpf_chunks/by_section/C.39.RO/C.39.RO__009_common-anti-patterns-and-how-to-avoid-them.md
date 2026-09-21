---
chunk_kind: "child"
pattern_id: "C.39.RO"
pattern_title: "Turn a Construction into a Reusable Operation"
section_id: "C.39.RO:8"
section_title: "Common Anti-Patterns and How to Avoid Them"
source_path: "FPF-Spec.md"
output_path: "by_section/C.39.RO/C.39.RO__009_common-anti-patterns-and-how-to-avoid-them.md"
commit_sha: "31f4cb0b7f8000e0115098b50b44f80c8c36a671"
heading_path:
  - "C.39.RO — Turn a Construction into a Reusable Operation"
  - "C.39.RO:8 — Common Anti-Patterns and How to Avoid Them"
line_start: 75382
line_end: 75392
dependencies:
  - "A.3.1"
  - "A.3.2"
  - "B.5.QD"
  - "B.5.RC"
  - "B.5.RR"
  - "B.5.TU"
  - "C.39"
  - "C.40"
keywords:
---

### C.39.RO:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Consequence | Repair |
| --- | --- | --- |
| Copy the successful constants | A later input receives the earlier case's answer. | Recover the relation that selected those constants and apply it to the changed input. |
| Turn every fixed fact into a parameter | A premise needed by the operation disappears. | State the proposed variation and retain or replace the conditions that support it. |
| Hide a missing operation behind a name | The next practitioner can request a result but cannot obtain it. | Recover or construct the step that supplies that result. |
| Compose matching labels | An output reaches a step that needs a different quantity or condition. | Compare the intermediate meanings and application conditions. |
| Extend a physical action from one successful run | A change of apparatus or operating condition defeats the claimed repeatability. | Carry the physical basis and develop the missing relation for the changed use. |
| Discard a failure witness | The practitioner repeats a search that the result already rules out. | Use the obstruction to change the attainable result, permitted operation or next question. |

