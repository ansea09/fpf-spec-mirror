---
chunk_kind: "child"
pattern_id: "B.1.6"
pattern_title: "Work-Resource Aggregation"
section_id: "B.1.6:8"
section_title: "Common Anti-Patterns and How to Avoid Them"
source_path: "FPF-Spec.md"
output_path: "by_section/B.1.6/B.1.6__012_common-anti-patterns-and-how-to-avoid-them.md"
commit_sha: "11f2345e65e4b2ec5b84c0cecde4c9485834d28d"
heading_path:
  - "B.1.6 — Work-Resource Aggregation"
  - "B.1.6:8 — Common Anti-Patterns and How to Avoid Them"
line_start: 37229
line_end: 37238
dependencies:
  - "A.1"
  - "A.10"
  - "A.14"
  - "A.15.1"
  - "A.15.2"
  - "A.15.5"
  - "A.3.1"
  - "A.3.2"
  - "A.3.4"
  - "A.6.1"
  - "B.1"
  - "B.1.4"
  - "B.1.6"
  - "B.2-family"
  - "B.2.P"
  - "C.13"
  - "C.16"
  - "C.2.1"
  - "C.27"
  - "C.29"
  - "E.17"
  - "G.11"
  - "G.6"
keywords:
  - "C.16 measurement work/result episteme"
  - "Scale/Unit"
  - "aggregation work"
  - "allocation/deduplication"
  - "dated work set"
  - "edition-pinned aggregation policy"
  - "provenance"
  - "resource Characteristic"
  - "typed aggregation result"
  - "typed input"
  - "uncertainty"
  - "work parthood/phase/overlap"
  - "work-resource aggregation"
---

### B.1.6:8 - Common Anti-Patterns and How to Avoid Them

| Overread | Repair |
| --- | --- |
| A method or algorithm is treated as the work-resource roll-up. | Use `A.3.1` or `A.3.2`; use `B.1.6` only for the resource aggregation claim. |
| A work plan is treated as measured work. | Use `A.15.2` for the plan and `A.15.1` for performed work evidence. |
| A phase label or timeline is treated as a resource ledger or as proof of a Work relation. | Recover the exact subject first: A.15.1 for Work temporal parts or occurrences, the carrier's identity pattern plus A.14 for proper non-Work `PhaseOf`, and B.1.4 only for bounded aggregation of already recovered temporal relations. Add B.1.6 only when typed resource values are being aggregated. |
| A resource gain is treated as emergence. | Use measurement and evidence-use patterns first; use `B.2.P` only if whole reidentification remains current. |
| A ledger, dashboard, or report total is treated as the aggregation result. | Recover the source publications, C.16 measurements, work set and relations, policy, dated aggregation work, B.1.6 result, C.2.1 episteme, and A.10/G.6 provenance. |

