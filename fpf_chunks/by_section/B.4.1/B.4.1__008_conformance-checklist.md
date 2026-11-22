---
chunk_kind: "child"
pattern_id: "B.4.1"
pattern_title: "Publish Candidate Routes for a Stabilized Cue (RoutedCueSet)"
section_id: "B.4.1:7"
section_title: "Conformance Checklist"
source_path: "FPF-Spec.md"
output_path: "by_section/B.4.1/B.4.1__008_conformance-checklist.md"
commit_sha: "4ee69807f8e5d4fa438e8c9b5de001d91275cc31"
heading_path:
  - "B.4.1 — Publish Candidate Routes for a Stabilized Cue (RoutedCueSet)"
  - "B.4.1:7 — Conformance Checklist"
line_start: 48190
line_end: 48197
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
- `CC-B.4.1-1` Observe output **SHALL NOT** be forced into `AnomalyStatement` when articulation threshold is not met.
- `CC-B.4.1-2` A routed cue set **SHALL** name its `candidateRouteSet` and explain how the stated continuations serve the receiving question in the applicable conditions. Support any claim of completeness. One justified route may suffice for a request for one continuation.
- `CC-B.4.1-3` A published selection **SHALL** identify the selected route and whose decision it was. For a past selection, state the grounds for attributing it to that person or system. Report their rationale when the evidence establishes it, and identify any rationale still unknown. A recommendation supplied by the author gives the author’s grounds. When publication is part of the assignment, establish availability to its intended recipients.
- `CC-B.4.1-4` `publicationFaceRefs` **MAY** be named. The expression **SHALL** satisfy the route-form requirements as well as the presentation rules of any selected MVPK face.
- `CC-B.4.1-5` `RoutedCueSet` **SHALL NOT** be treated as establishing a late endpoint result.
- `CC-B.4.1-6` When a specialization-sensitive route is kept live, the route package **SHALL** name the declared task family or utility target, any budget condition that qualifies the proposed continuation, any unresolved fact needed for its use or selection, and the downstream subject pattern with its entry conditions.

