---
chunk_kind: "child"
pattern_id: "B.1.6"
pattern_title: "Work-Resource Aggregation"
section_id: "B.1.6:3"
section_title: "Optional Gamma_work Notation"
source_path: "FPF-Spec.md"
output_path: "by_section/B.1.6/B.1.6__006_optional-gamma-work-notation.md"
commit_sha: "c927fef1dac0f4d5f8ca93deef8a52de75e3f77b"
heading_path:
  - "B.1.6 — Work-Resource Aggregation"
  - "B.1.6:3 — Optional Gamma_work Notation"
line_start: 32725
line_end: 32735
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

### B.1.6:3 - Optional `Gamma_work` Notation

`Gamma_work` is optional notation for a recovered `WorkResourceAggregation@Context`.

```text
Gamma_work(workResourceAggregationRecord, resourceBasis, aggregationRule)
  -> aggregated resource value plus ledger
```

The notation applies only after the work occurrence refs, resource-accounting basis, time window, holon delimitation, and evidence or measurement refs have been named. It does not order method steps, certify the method, create work evidence, or declare emergence.

