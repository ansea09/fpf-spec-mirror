---
chunk_kind: "child"
pattern_id: "B.1.4"
pattern_title: "Contextual and Temporal Aggregation"
section_id: "B.1.4:3"
section_title: "Optional Operator Notation"
source_path: "FPF-Spec.md"
output_path: "by_section/B.1.4/B.1.4__006_optional-operator-notation.md"
commit_sha: "9a9a42e4d154021ca3f7415e0009a4214832f65f"
heading_path:
  - "B.1.4 — Contextual and Temporal Aggregation"
  - "B.1.4:3 — Optional Operator Notation"
line_start: 36226
line_end: 36241
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

### B.1.4:3 - Optional Operator Notation

`Gamma_ctx` and `Gamma_time` are optional notation for already recovered aggregation claims.

```text
Gamma_ctx(contextualAggregationRecord, orderSpec, independenceAndJoinConditions)
  -> contextual aggregate record

Gamma_time(temporalAggregationRecord, timeWindow, coverageAndNonOverlapConditions)
  -> temporal aggregate record
```

The notation does not create a holon, transformation, method, work occurrence, or whole reidentification by itself. It records how the selected relation set is combined for the current use.

If the source says a system actually sequences, combines, transforms, measures, or audits something, name that acting-side relation separately through `A.12`, `A.3.4`, `A.15.1`, `B.1.6`, `A.10`, or the direct owner. The person, team, controller, or tool that writes an aggregation record is not automatically the in-world transformer for the EntityOfConcern being aggregated.

