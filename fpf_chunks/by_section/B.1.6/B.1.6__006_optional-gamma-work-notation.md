---
chunk_kind: "child"
pattern_id: "B.1.6"
pattern_title: "Work-Resource Aggregation"
section_id: "B.1.6:3"
section_title: "Optional Gamma_work Notation"
source_path: "FPF-Spec.md"
output_path: "by_section/B.1.6/B.1.6__006_optional-gamma-work-notation.md"
commit_sha: "b223469ecafb9735c1d9bac220671e3336618339"
heading_path:
  - "B.1.6 — Work-Resource Aggregation"
  - "B.1.6:3 — Optional Gamma_work Notation"
line_start: 43207
line_end: 43217
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

### B.1.6:3 - Optional `Gamma_work` Notation

`Gamma_work` is optional notation for a recovered `WorkResourceAggregation@Context`.

```text
Gamma_work(workResourceAggregationRecord, resourceBasis, aggregationPolicy)
  -> aggregationResultRef [, aggregationResultEpistemeRef when required by the receiving claim or use]
```

The notation summarizes an aggregation whose required basis has been recovered: resource Characteristics and input-value grounds; included accounting subjects and any Work-part, temporal-overlap, resource-use or stock relations used by the account; a non-Work carrier phase's identity and `PhaseOf` grounds when that phase is included; accounting scope, time basis and operative rules; and the typed result with its qualifications. Any deliberately asserted measurement or aggregation Work keeps its independent occurrence grounds. The notation adds none of those facts.

