---
chunk_kind: "child"
pattern_id: "C.29.BB"
pattern_title: "Construct a Balance across a Boundary"
section_id: "C.29.BB:8"
section_title: "Common Anti-Patterns and How to Avoid Them"
source_path: "FPF-Spec.md"
output_path: "by_section/C.29.BB/C.29.BB__009_common-anti-patterns-and-how-to-avoid-them.md"
commit_sha: "4ddaf71557d4159e988cc61d2bd3088bfc1d2803"
heading_path:
  - "C.29.BB — Construct a Balance across a Boundary"
  - "C.29.BB:8 — Common Anti-Patterns and How to Avoid Them"
line_start: 66241
line_end: 66249
dependencies:
  - "A.3.3.TR"
  - "C.11.DUA"
  - "C.29.1"
  - "C.29.2"
  - "E.18.2"
keywords:
---

### C.29.BB:8 - Common Anti-Patterns and How to Avoid Them

| Failure | Repair |
| --- | --- |
| **The connector disappears.** The tanks are combined while the line's changing content is omitted. | Include the line or retain its two crossings and storage difference. |
| **Similar numbers are added.** Temperatures or overlapping job populations are summed as a stored amount. | Construct an additive quantity or retain the local values required by the question. |
| **A discrepancy is named a leak.** Incompatible endpoints or transfer observations are never examined. | Compare the accounts and choose a discriminating check when its result matters. |
| **Local updates disagree.** The two sides of a computational interface use different transferred amounts. | Share the amount or provide a compatible conversion, then derive the aggregate update again. |

