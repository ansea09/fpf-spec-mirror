---
chunk_kind: "child"
pattern_id: "A.6.3.RT.OE"
pattern_title: "Construct an Operative Expression"
section_id: "A.6.3.RT.OE:8"
section_title: "Common Anti-Patterns and How to Avoid Them"
source_path: "FPF-Spec.md"
output_path: "by_section/A.6.3.RT.OE/A.6.3.RT.OE__009_common-anti-patterns-and-how-to-avoid-them.md"
commit_sha: "b6bc6961903d9196811f71f561c1877fd3feec07"
heading_path:
  - "A.6.3.RT.OE — Construct an Operative Expression"
  - "A.6.3.RT.OE:8 — Common Anti-Patterns and How to Avoid Them"
line_start: 16661
line_end: 16671
dependencies:
  - "A.6.3.RT"
  - "B.5.RA"
  - "B.5.RC"
  - "B.5.RR"
  - "C.2.8"
  - "C.37"
  - "E.5.2"
keywords:
---

### A.6.3.RT.OE:8 - Common Anti-Patterns and How to Avoid Them

| Failure in these situations | Consequence | Repair |
| --- | --- | --- |
| Preserve all labels but hide a shared part | The user cannot combine the relevant relations. | Keep the common part recognizable across the needed groupings. |
| Remove grouping to make the expression shorter | A different operation or continuation becomes permitted. | Restore the scheme's scope or grouping rule. |
| Align signs without a common reference | The arrangement suggests a comparison or timing relation that does not hold. | Supply the relevant origin, scale, units or temporal reference. |
| Treat a conclusion suggested by a drawing as source-given | The claim loses the argument needed for its use. | Perform the subject inference and retain its premises. |
| Change notation when the subject operation is missing | A new form leaves the same construction unavailable. | Obtain the missing Method contribution and then prepare its expression. |
| Infer fluent performance from a calculated arrangement | A prepared sequence is mistaken for acquired capability. | Assess execution or learning when that result is required. |

