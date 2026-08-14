---
chunk_kind: "child"
pattern_id: "B.1.6"
pattern_title: "Work-Resource Aggregation"
section_id: "B.1.6:3"
section_title: "Optional Gamma_work Notation"
source_path: "FPF-Spec.md"
output_path: "by_section/B.1.6/B.1.6__006_optional-gamma-work-notation.md"
commit_sha: "7205ce8cea50eb778520a026373b2b7bcbc43fbb"
heading_path:
  - "B.1.6 — Work-Resource Aggregation"
  - "B.1.6:3 — Optional Gamma_work Notation"
line_start: 36855
line_end: 36865
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

### B.1.6:3 - Optional `Gamma_work` Notation

`Gamma_work` is optional notation for a recovered `WorkResourceAggregation@Context`.

```text
Gamma_work(workResourceAggregationRecord, resourceBasis, aggregationPolicy)
  -> aggregationResultRef, aggregationResultEpistemeRef
```

The notation applies only after the resource Characteristics, C.16 measurement Work and result epistemes, dated Work set, exact A.15.1 Work-part, episode, and overlap relations or non-Work carrier identity and `PhaseOf` relations, accounting boundary and time window, aggregation policy, and dated aggregation Work have been named. It does not create those objects or relations, order method steps, certify a method, or declare emergence.

