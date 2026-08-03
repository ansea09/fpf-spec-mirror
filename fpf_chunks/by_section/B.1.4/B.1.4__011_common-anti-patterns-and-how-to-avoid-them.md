---
chunk_kind: "child"
pattern_id: "B.1.4"
pattern_title: "Contextual and Temporal Aggregation"
section_id: "B.1.4:7"
section_title: "Common Anti-Patterns and How to Avoid Them"
source_path: "FPF-Spec.md"
output_path: "by_section/B.1.4/B.1.4__011_common-anti-patterns-and-how-to-avoid-them.md"
commit_sha: "9dd9215969126625d449a40e8ca4d1df9ac903f8"
heading_path:
  - "B.1.4 — Contextual and Temporal Aggregation"
  - "B.1.4:7 — Common Anti-Patterns and How to Avoid Them"
line_start: 36399
line_end: 36408
dependencies:
  - "A.1.1"
  - "A.14"
  - "A.15.1"
  - "A.15.2"
  - "A.3.1"
  - "A.3.2"
  - "A.3.4"
  - "B.1"
  - "B.1.6"
  - "B.2-family"
  - "B.2.P"
  - "C.13"
  - "C.2.1"
  - "C.27"
  - "C.27.TA"
  - "C.29"
  - "E.18"
  - "E.18.2"
keywords:
---

### B.1.4:7 - Common Anti-Patterns and How to Avoid Them

| Overread | Repair |
| --- | --- |
| A sequence is treated as physical parthood. | Recover ordered relation refs and use contextual aggregation; use part-whole owners only for part-whole claims. |
| A phase label is treated as a new system level. | Recover the carrier identity and phase relation; use whole reidentification only if B.2.P keeps that claim current. |
| A planning order is treated as performed work. | Use `A.15.2` for work plan and `A.15.1` for dated work occurrence. |
| A resource total is placed inside temporal aggregation. | Use `B.1.6` for the work-resource ledger. |
| A diagram or table is treated as the aggregate. | Recover the Description episteme or publication relation and the EntityOfConcern separately. |

