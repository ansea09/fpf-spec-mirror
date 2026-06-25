---
chunk_kind: "child"
pattern_id: "B.1.4"
pattern_title: "Contextual and Temporal Aggregation"
section_id: "B.1.4:8.1"
section_title: "Rationale"
source_path: "FPF-Spec.md"
output_path: "by_section/B.1.4/B.1.4__013_rationale.md"
commit_sha: "6bbbb622859fbbcddc02b23ea76bee4dd71c6291"
heading_path:
  - "B.1.4 — Contextual and Temporal Aggregation"
  - "B.1.4:8.1 — Rationale"
line_start: 31717
line_end: 31722
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
  - "C.27"
  - "C.27.TA"
  - "C.29"
  - "E.18"
  - "E.18.2"
keywords:
---

### B.1.4:8.1 - Rationale

`B.1.4` exists because contextual order and temporal phase aggregation are neither ordinary part-whole construction nor generic process talk. The same carrier can be considered through phases; a selected relation set can be order-sensitive; and both cases need admissible aggregation without inventing a new holon kind. The pattern therefore keeps relation discipline explicit: `PhaseOf` and carrier identity for phase aggregation; ordered relation refs and `OrderSpec` for contextual aggregation; direct-owner return for method, work, resource, transformation, evidence, and whole reidentification.

The old `DesignRunTag` warning is preserved as a rule rather than a label: do not fold design-time possible order and run-time history into one aggregate. If both are needed, make two records and relate them by value.

