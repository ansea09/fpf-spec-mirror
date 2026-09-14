---
chunk_kind: "child"
pattern_id: "B.5.MPC.R"
pattern_title: "Repair a Physical-Mathematical-Computational Connection"
section_id: "B.5.MPC.R:8"
section_title: "Common Anti-Patterns and How to Avoid Them"
source_path: "FPF-Spec.md"
output_path: "by_section/B.5.MPC.R/B.5.MPC.R__009_common-anti-patterns-and-how-to-avoid-them.md"
commit_sha: "b6bc6961903d9196811f71f561c1877fd3feec07"
heading_path:
  - "B.5.MPC.R — Repair a Physical-Mathematical-Computational Connection"
  - "B.5.MPC.R:8 — Common Anti-Patterns and How to Avoid Them"
line_start: 43197
line_end: 43206
dependencies:
  - "A.15.9"
  - "A.3.3"
  - "A.6.3.RT"
  - "B.5"
  - "B.5.MPC"
  - "B.5.RR"
  - "C.16"
  - "C.29.1"
  - "C.29.2"
  - "C.29.3"
keywords:
---

### B.5.MPC.R:8 - Common Anti-Patterns and How to Avoid Them

| Failure | Consequence | Repair |
| --- | --- | --- |
| Solve for the former unknown | A correct formula answers the old question. | Retain the relation and select the givens and unknowns again. |
| Refine the computation of ambiguous data | The physical alternatives remain indistinguishable. | Change acquisition or return the supported ambiguity. |
| Treat debugger time as physical time | A retained actuator command can continue to act during the pause. | Recover the actual timer and actuator behavior. |
| Treat a probe as passive despite its coupling | The observed system differs from the modelled unobserved arrangement. | Include the probe interaction or change the measurement. |
| Switch algorithms while retaining the disputed physical premise | The alternative preserves the same failure. | Compare its complete application conditions. |

