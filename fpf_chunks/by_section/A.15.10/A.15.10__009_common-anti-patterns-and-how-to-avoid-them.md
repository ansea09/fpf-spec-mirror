---
chunk_kind: "child"
pattern_id: "A.15.10"
pattern_title: "Resume Interrupted Work"
section_id: "A.15.10:8"
section_title: "Common Anti-Patterns and How to Avoid Them"
source_path: "FPF-Spec.md"
output_path: "by_section/A.15.10/A.15.10__009_common-anti-patterns-and-how-to-avoid-them.md"
commit_sha: "a4048aafca7f550ddc5dc880c9b488e9c8401434"
heading_path:
  - "A.15.10 — Resume Interrupted Work"
  - "A.15.10:8 — Common Anti-Patterns and How to Avoid Them"
line_start: 29558
line_end: 29568
dependencies:
  - "A.15"
  - "A.15.5"
  - "A.15.7"
  - "A.15.8"
  - "A.15.9"
  - "B.1.5"
  - "B.5.RA"
  - "B.5.RC"
  - "B.5.RR"
  - "C.11.DUA"
  - "E.23.CAE"
keywords:
---

### A.15.10:8 - Common Anti-Patterns and How to Avoid Them

| Failure | Consequence | Repair |
| --- | --- | --- |
| Resume from a cursor alone | The performer applies a different rule to the right item. | Recover the governing method and the last established result. |
| Turn a planned step into a completed step | Later reasoning relies on a result that was never obtained. | Inspect the result or reconstruct the smallest safe missing contribution. |
| Retain everything in a separate report | Preparation, reading and synchronization displace the work. | Keep only the threatened contributions in existing working material. |
| Trust the old account as present state | A changed input, tool or physical condition invalidates continuation. | Inspect the dependencies that can change the next use. |
| Restart all work after any doubt | Valid results and effort are discarded. | Return to the last reliable point and revise the affected part. |
| Equate delivery with a usable handoff | The receiver lacks a rule, access or capability needed to act. | Restore that contribution and test understanding through useful continuation when needed. |

