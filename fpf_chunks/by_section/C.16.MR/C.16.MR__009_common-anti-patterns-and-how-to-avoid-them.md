---
chunk_kind: "child"
pattern_id: "C.16.MR"
pattern_title: "Construct a Measurement Relation"
section_id: "C.16.MR:8"
section_title: "Common Anti-Patterns and How to Avoid Them"
source_path: "FPF-Spec.md"
output_path: "by_section/C.16.MR/C.16.MR__009_common-anti-patterns-and-how-to-avoid-them.md"
commit_sha: "0caf9a10acfc0ee17c32fc71f6173b542393f0a4"
heading_path:
  - "C.16.MR — Construct a Measurement Relation"
  - "C.16.MR:8 — Common Anti-Patterns and How to Avoid Them"
line_start: 52821
line_end: 52831
dependencies:
  - "A.3.3"
  - "B.5.FM"
  - "B.5.MPC.R"
  - "B.5.RC"
  - "C.11.DUA"
  - "C.16"
  - "C.29.2"
keywords:
---

### C.16.MR:8 - Common Anti-Patterns and How to Avoid Them

| Failure | Effect on use | Repair |
| --- | --- | --- |
| Read the display as the sought value after the procedure changes the subject | The answer can concern the measured arrangement instead of the target conditions. | Model the interaction and state which quantity is sought. |
| Copy a correction without its measurement relation | Its direction, magnitude or range can be wrong for the current arrangement. | Recover where the effect enters and derive its contribution. |
| Fill an unknown influence with zero | A numerical answer hides unresolved alternatives. | Keep the influence unknown and use available bounds or a justified distribution. |
| Treat expected response as an error-free observed proportion | The inferred population property loses sampling uncertainty. | Keep the response model and sampling inference distinct. |
| Repeat measurements to remove structural ambiguity | The same indication can still fit different sought values. | Change the relation or observation that distinguishes those values. |
| Model every conceivable influence before answering | The work expands without changing the result. | Test the consequence of the influence for the intended use and stop with an adequate result. |

