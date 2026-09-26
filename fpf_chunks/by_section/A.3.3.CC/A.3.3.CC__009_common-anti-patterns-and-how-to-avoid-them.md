---
chunk_kind: "child"
pattern_id: "A.3.3.CC"
pattern_title: "Construct a Configuration Description under Constraints"
section_id: "A.3.3.CC:8"
section_title: "Common Anti-Patterns and How to Avoid Them"
source_path: "FPF-Spec.md"
output_path: "by_section/A.3.3.CC/A.3.3.CC__009_common-anti-patterns-and-how-to-avoid-them.md"
commit_sha: "61a9542aa8479024cdd174c024079d2a6a15f16d"
heading_path:
  - "A.3.3.CC — Construct a Configuration Description under Constraints"
  - "A.3.3.CC:8 — Common Anti-Patterns and How to Avoid Them"
line_start: 9777
line_end: 9787
dependencies:
  - "A.17"
  - "A.18"
  - "A.19"
  - "A.3.3"
  - "A.6.3.RT"
  - "B.5.FM"
  - "B.5.MPC"
  - "C.29.1"
  - "C.29.2"
keywords:
---

### A.3.3.CC:8 - Common Anti-Patterns and How to Avoid Them

| Observed or example-demonstrated failure | Repair |
| --- | --- |
| Choosing valid values for each endpoint but violating the link between them | Test the joint tuple against the distance constraint, or reconstruct both endpoints from parameters satisfying it. |
| Carrying a fixed-total reduction into a model with arrivals | Make the changed total explicit or retain the counts needed to express it. |
| Answering a job-order question from queue lengths alone | Retain the ordered identities used by the service rule. |
| Treating a small coordinate count as a global representation | Supply coverage and equivalence information; use multiple charts or implicit constraints where needed. |
| Rejecting a parking position because immediate sideways motion is forbidden | Keep the position and test a sequence of allowed motions under the relevant steering and obstacle conditions. |
| Treating a failed search as impossibility | Return the search limit, or obtain a complete argument or computation for the impossibility claim. |

