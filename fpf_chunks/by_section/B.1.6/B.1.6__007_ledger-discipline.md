---
chunk_kind: "child"
pattern_id: "B.1.6"
pattern_title: "Work-Resource Aggregation"
section_id: "B.1.6:4"
section_title: "Ledger Discipline"
source_path: "FPF-Spec.md"
output_path: "by_section/B.1.6/B.1.6__007_ledger-discipline.md"
commit_sha: "6bbbb622859fbbcddc02b23ea76bee4dd71c6291"
heading_path:
  - "B.1.6 — Work-Resource Aggregation"
  - "B.1.6:4 — Ledger Discipline"
line_start: 32168
line_end: 32184
dependencies:
  - "A.1"
  - "A.10"
  - "A.14"
  - "A.15"
  - "A.15.1"
  - "A.15.2"
  - "A.15.5"
  - "A.3.1"
  - "A.3.2"
  - "A.3.4"
  - "B.1"
  - "B.1.4"
  - "B.1.6"
  - "B.2"
  - "B.2-family"
  - "B.2.P"
  - "C.13"
  - "C.16"
  - "C.27"
  - "C.29"
  - "E.17"
keywords:
---

### B.1.6:4 - Ledger Discipline

A conforming `WorkResourceAggregation@Context` includes a work-resource ledger with:

- work occurrence refs or parent and child work occurrence refs;
- resource-accounting basis and unit refs;
- time window and phase refs when time slicing is used;
- holon delimitation refs and any boundary-crossing relation refs used for accounting;
- method, method-description, and work-plan refs only when those objects are actually used;
- evidence, measurement, or source refs for the resource values;
- overlap or deduplication policy when work occurrences share resources, time windows, ports, stocks, people, tools, or data;
- admissible use and non-admissible overread.

For any resource type in the selected resource-accounting basis, the ledger should say whether the value is measured, estimated, normalized, or converted. If the value is measured, it names the measurement or evidence relation. If the value is planned, it stays marked as expected work-resource use and does not become performed-work evidence.

When the aggregation divides a stock or resource amount, use `PortionOf` or the direct quantitative relation owner. When the aggregation slices one work occurrence or one carrier over time, use `PhaseOf` or the direct phase owner. Do not use `MemberOf` for resource stock, resource portion, or time-slice composition.

