---
chunk_kind: "child"
pattern_id: "B.1.4"
pattern_title: "Contextual and Temporal Aggregation"
section_id: "B.1.4:8.1"
section_title: "Rationale"
source_path: "FPF-Spec.md"
output_path: "by_section/B.1.4/B.1.4__013_rationale.md"
commit_sha: "d9170ae93b035896511bce82dfb5d9082a50b8a2"
heading_path:
  - "B.1.4 — Contextual and Temporal Aggregation"
  - "B.1.4:8.1 — Rationale"
line_start: 36344
line_end: 36349
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

### B.1.4:8.1 - Rationale

`B.1.4` exists because contextual order and temporal phase aggregation are neither ordinary part-whole construction nor generic process talk. One enduring carrier with a stated identity rule can be considered through proper temporal restrictions; a selected relation set can be order-sensitive; and both cases need admissible aggregation without inventing a new holon kind. The pattern therefore keeps relation discipline explicit: `PhaseOf` and the carrier's identity rule for legitimate phase aggregation; C.2.1 identity and independently obtaining edition relations for distinct episteme history; A.15.1 relations for Work; ordered relation refs and `OrderSpec` for contextual aggregation; and separate patterns for resource, transformation, evidence, and whole reidentification.

The old `DesignRunTag` warning is preserved as a rule rather than a label: do not fold design-time possible order and run-time history into one aggregate. If both are needed, make two records and relate them by value.

