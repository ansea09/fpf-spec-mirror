---
chunk_kind: "child"
pattern_id: "B.1.4"
pattern_title: "Contextual and Temporal Aggregation"
section_id: "B.1.4:6"
section_title: "Conformance Checklist"
source_path: "FPF-Spec.md"
output_path: "by_section/B.1.4/B.1.4__010_conformance-checklist.md"
commit_sha: "421266f0a37ab295b1ffd9e214ace6541e21f5be"
heading_path:
  - "B.1.4 — Contextual and Temporal Aggregation"
  - "B.1.4:6 — Conformance Checklist"
line_start: 37406
line_end: 37416
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

### B.1.4:6 - Conformance Checklist

| ID | Requirement | Purpose |
| --- | --- | --- |
| CC-B1.4-1 | The aggregate names the EntityOfConcern, included positions or phases, aggregation mode, ClaimScope when needed, time window when temporal qualification matters, and admissible use. | Prevents a generic context or time label from standing in for the aggregation boundary. |
| CC-B1.4-2 | Contextual aggregation names ordered relation refs and an `OrderSpec`; temporal aggregation names carrier identity, phase refs, and `TimeWindow`. | Keeps order and time as different relations. |
| CC-B1.4-3 | Independence, join, coverage, and non-overlap conditions are present when the claim uses them. | Keeps local composition reviewable. |
| CC-B1.4-4 | Method, method-description, work-plan, work-occurrence, work-resource, transformation, and whole-reidentification claims use the patterns that define or test them. | Prevents B.1.4 from absorbing neighboring objects. |
| CC-B1.4-5 | Mathematical notation is treated as a selected lens or expression, not as the in-life object or relation. | Keeps `Gamma_ctx`, `Gamma_time`, graph, and algebra language bounded. |
| CC-B1.4-6 | If identity changes, coverage breaks, or a new whole is claimed, the record narrows use or names the pattern for the stronger claim. | Prevents temporal aggregation from becoming hidden MHT or transformation. |

