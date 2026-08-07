---
chunk_kind: "child"
pattern_id: "B.4.1"
pattern_title: "Observe -> Notice -> Stabilize -> Route"
section_id: "B.4.1:7"
section_title: "Conformance Checklist"
source_path: "FPF-Spec.md"
output_path: "by_section/B.4.1/B.4.1__008_conformance-checklist.md"
commit_sha: "2729cfe5a3e4a86da8632aabcb859488c06a2d51"
heading_path:
  - "B.4.1 — Observe -> Notice -> Stabilize -> Route"
  - "B.4.1:7 — Conformance Checklist"
line_start: 39905
line_end: 39912
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
  - "F.9.1"
keywords:
  - "pre-abductive seam"
  - "route plurality"
  - "route selection"
  - "routed cue set"
  - "task-family specialization route"
---

### B.4.1:7 - Conformance Checklist
- `CC-B.4.1-1` Observe output **SHALL NOT** be forced directly into `AnomalyStatement` when articulation threshold is not yet met.
- `CC-B.4.1-2` A routed cue set **SHALL** name its `candidateRouteSet`.
- `CC-B.4.1-3` When route selection occurs, `routeDecision`, `selectedRoute`, and `routeRationale` **SHALL** be explicit.
- `CC-B.4.1-4` `publicationFaceRefs` **MAY** be named, but route-bearing form and publication face **SHALL NOT** be collapsed.
- `CC-B.4.1-5` `RoutedCueSet` **SHALL NOT** silently masquerade as a late endpoint governing pattern.
- `CC-B.4.1-6` When a specialization-sensitive route is kept live, the route package **SHALL** name the declared task family or utility target, the current budget window if known, the missing discriminator still needed, and the downstream governing pattern that would become admissible if the discriminator is satisfied.

