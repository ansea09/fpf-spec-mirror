---
chunk_kind: "child"
pattern_id: "B.1.4"
pattern_title: "Specify Order-Sensitive or Temporal Aggregation (Γ_ctx, Γ_time)"
section_id: "B.1.4:3"
section_title: "Optional Operator Notation"
source_path: "FPF-Spec.md"
output_path: "by_section/B.1.4/B.1.4__006_optional-operator-notation.md"
commit_sha: "b223469ecafb9735c1d9bac220671e3336618339"
heading_path:
  - "B.1.4 — Specify Order-Sensitive or Temporal Aggregation (Γ_ctx, Γ_time)"
  - "B.1.4:3 — Optional Operator Notation"
line_start: 42031
line_end: 42046
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
  - "B.2"
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

`Gamma_ctx` and `Gamma_time` are optional notation for a selected aggregation operation and its result. A specification may state such an application without claiming that its result has already been computed.

```text
Gamma_ctx(selectedInputs, combiningRule, orderSpec, joinOrIndependenceConditions?)
  -> contextual aggregation result

Gamma_time(selectedTemporalInputs, combiningRule, temporalReference, timeWindow, coverageAndOverlapPolicy)
  -> temporal aggregation result
```

The notation expresses the selected operation; it supplies no default combining rule. Temporal inputs retain the values and temporal facts consumed by that rule. An optional account can provide the argument values and describe the result. Establish the represented objects and relations under their direct patterns, and check the operation's conditions before relying on that result.

Keep an ordinary statement about who prepared the aggregation ordinary. If the use asserts one exact dated sequencing, combining, measuring or auditing Work, recover the actual performer's A.13 core and admit the Work independently under A.15.1. Use A.3.4 for a separate transformation claim, B.1.6 for resource aggregation, and A.10 to recover provenance and bounded reliance on independently established results. Writing the record does not identify its writer as the transformer of the EntityOfConcern.

