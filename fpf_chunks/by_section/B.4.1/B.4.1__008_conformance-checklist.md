---
chunk_kind: "child"
pattern_id: "B.4.1"
pattern_title: "Publish Candidate Routes for a Stabilized Cue (RoutedCueSet)"
section_id: "B.4.1:7"
section_title: "Conformance Checklist"
source_path: "FPF-Spec.md"
output_path: "by_section/B.4.1/B.4.1__008_conformance-checklist.md"
commit_sha: "4260875dd8bc4595bbca3b6dbfa61e6f35afa013"
heading_path:
  - "B.4.1 — Publish Candidate Routes for a Stabilized Cue (RoutedCueSet)"
  - "B.4.1:7 — Conformance Checklist"
line_start: 46096
line_end: 46103
dependencies:
  - "A.15"
  - "A.16"
  - "A.16.0"
  - "A.16.1"
  - "A.6.A"
  - "A.6.P"
  - "B.4"
  - "B.5.2"
  - "B.5.2.0"
  - "C.16.Q"
  - "C.2.2a"
  - "C.2.4"
  - "C.2.5"
  - "C.2.6"
  - "C.2.7"
  - "C.2.LS"
  - "C.22.1"
keywords:
---

### B.4.1:7 - Conformance Checklist
- `CC-B.4.1-1` Observe output **SHALL NOT** be forced directly into `AnomalyStatement` when articulation threshold is not yet met.
- `CC-B.4.1-2` A routed cue set **SHALL** name its `candidateRouteSet`.
- `CC-B.4.1-3` When route selection occurs, `routeDecision`, `selectedRoute`, and `routeRationale` **SHALL** be explicit.
- `CC-B.4.1-4` `publicationFaceRefs` **MAY** be named, but route-bearing form and publication face **SHALL NOT** be collapsed.
- `CC-B.4.1-5` `RoutedCueSet` **SHALL NOT** be treated as establishing a late endpoint result.
- `CC-B.4.1-6` When a specialization-sensitive route is kept live, the route package **SHALL** name the declared task family or utility target, any budget condition that qualifies the proposed continuation, any unresolved fact needed for its use or selection, and the downstream subject pattern with its entry conditions.

