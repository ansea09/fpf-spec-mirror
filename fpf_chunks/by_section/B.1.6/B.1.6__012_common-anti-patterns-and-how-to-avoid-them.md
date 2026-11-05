---
chunk_kind: "child"
pattern_id: "B.1.6"
pattern_title: "Work-Resource Aggregation"
section_id: "B.1.6:8"
section_title: "Common Anti-Patterns and How to Avoid Them"
source_path: "FPF-Spec.md"
output_path: "by_section/B.1.6/B.1.6__012_common-anti-patterns-and-how-to-avoid-them.md"
commit_sha: "4260875dd8bc4595bbca3b6dbfa61e6f35afa013"
heading_path:
  - "B.1.6 — Work-Resource Aggregation"
  - "B.1.6:8 — Common Anti-Patterns and How to Avoid Them"
line_start: 43309
line_end: 43318
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
  - "B.2"
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
---

### B.1.6:8 - Common Anti-Patterns and How to Avoid Them

| Overread | Repair |
| --- | --- |
| A method or algorithm is treated as the work-resource roll-up. | Recover the actual resource claim and its grounds through `B.1.6`. Use `A.3.1` for a separate Method question, or `A.3.2` for a MethodDescription membership or description-use question. |
| A work plan is treated as measured work. | Use `A.15.2` for the plan and `A.15.1` for performed work evidence. |
| A phase label or timeline is treated as a resource ledger or as proof of a Work relation. | Recover the exact subject first: A.15.1 for Work temporal parts or occurrences, the carrier's identity pattern plus A.14 for proper non-Work `PhaseOf`, and B.1.4 only for bounded aggregation of already recovered temporal relations. Add B.1.6 only when typed resource values are being aggregated. |
| A resource gain is treated as emergence. | Use measurement and evidence-use patterns first; use `B.2` when whole identity remains the question; use `B.2.P` for unresolved emergence-family wording. |
| A ledger, dashboard or report total is relied on without the grounds its use requires. | Recover the existing result statement, input records, included subjects and relations, operative rule and qualifications. Preserve an adequate account; obtain only missing grounds under §§4–5. An asserted dated aggregation Work or a needed replayable provenance account retains its own requirements. |

