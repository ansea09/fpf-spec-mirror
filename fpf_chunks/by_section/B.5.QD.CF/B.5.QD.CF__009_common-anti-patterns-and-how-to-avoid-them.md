---
chunk_kind: "child"
pattern_id: "B.5.QD.CF"
pattern_title: "Reformulate a Problem by Examining Its Conflicting Assumptions"
section_id: "B.5.QD.CF:8"
section_title: "Common Anti-Patterns and How to Avoid Them"
source_path: "FPF-Spec.md"
output_path: "by_section/B.5.QD.CF/B.5.QD.CF__009_common-anti-patterns-and-how-to-avoid-them.md"
commit_sha: "61a9542aa8479024cdd174c024079d2a6a15f16d"
heading_path:
  - "B.5.QD.CF — Reformulate a Problem by Examining Its Conflicting Assumptions"
  - "B.5.QD.CF:8 — Common Anti-Patterns and How to Avoid Them"
line_start: 45962
line_end: 45972
dependencies:
  - "B.1.5.EW"
  - "B.5.FM"
  - "B.5.QD"
  - "B.5.RA"
  - "B.5.TC"
  - "C.11.DUA"
  - "C.40.CD"
keywords:
---

### B.5.QD.CF:8 - Common Anti-Patterns and How to Avoid Them

| Failure invited by conflict repair | Better move |
| --- | --- |
| “This way has always worked, so the result requires it.” | Recover what the way supplies and ask whether another operation supplies that contribution. |
| A solver returns a solution after a hard requirement is removed. | State the changed requirement and return to the original need; the witness answers the relaxed problem. |
| Two names are introduced for one quantity in one condition. | Establish the actual distinction or retain the incompatibility, as in :5.1. |
| The small conflicting set is repaired while another affected requirement is ignored. | Reapply the retained requirements; inspect the transition time or lost information that the change can affect. |
| A consistent description is presented as an implemented repair. | State the operation and support still needed to obtain the result. |
| Every conflict is promised a solution that preserves every demand. | Return the supported limit or requirement-change question when no warranted repair exists. |

