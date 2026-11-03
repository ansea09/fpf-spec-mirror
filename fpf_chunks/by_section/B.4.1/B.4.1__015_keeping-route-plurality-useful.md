---
chunk_kind: "child"
pattern_id: "B.4.1"
pattern_title: "Publish Candidate Routes for a Stabilized Cue (RoutedCueSet)"
section_id: "B.4.1:14"
section_title: "Keeping route plurality useful"
source_path: "FPF-Spec.md"
output_path: "by_section/B.4.1/B.4.1__015_keeping-route-plurality-useful.md"
commit_sha: "d73588bdcb52ed173d7b4c1552b2ce199a548c64"
heading_path:
  - "B.4.1 — Publish Candidate Routes for a Stabilized Cue (RoutedCueSet)"
  - "B.4.1:14 — Keeping route plurality useful"
line_start: 46150
line_end: 46167
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

### B.4.1:14 - Keeping route plurality useful

A routed cue set stays useful only when route plurality, route grounds, selection status, and any current-use or retirement claim remain explicit.

#### B.4.1:14.1 - Minimal route package
Use the minimal route package in §4 (Solution).

#### B.4.1:14.2 - Selected route is not endpoint governance
Even when one route is selected, the routed cue set states the route choice. If the receiving work calls for a further claim or result, apply its subject pattern under that pattern's entry conditions. Publishing the routes and selection can be the sufficient result.

#### B.4.1:14.3 - Review prompt and threshold reminder
Review the cue grounds and any further grounds used to justify the selection, including the reasons for excluding previously live alternatives. If the articulation threshold required for a proposed late prompt, requirement, or work claim is not yet met, keep the publication early.

#### B.4.1:14.4 - Deferred selection and route splitting
When selection is deferred, publish the live candidates, their grounds and any unresolved conditions. State an actual selection explicitly.

One cue cluster may also split into several routed cue sets if different sub-cues support different destinations. The split should be published explicitly so that later readers do not assume that one route exhausted the whole original cue complex.

