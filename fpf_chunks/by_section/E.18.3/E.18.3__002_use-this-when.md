---
chunk_kind: "child"
pattern_id: "E.18.3"
pattern_title: "Constraint-Governed Transformation-Flow Unfolding Structure"
section_id: "E.18.3:0"
section_title: "Use This When"
source_path: "FPF-Spec.md"
output_path: "by_section/E.18.3/E.18.3__002_use-this-when.md"
commit_sha: "504747d26299e3963dc0457bf48d4e2a791d926a"
heading_path:
  - "E.18.3 — Constraint-Governed Transformation-Flow Unfolding Structure"
  - "E.18.3:0 — Use This When"
line_start: 82351
line_end: 82360
dependencies:
  - "A.10"
  - "A.15"
  - "A.20"
  - "A.21"
  - "A.22"
  - "A.22.CGUS"
  - "A.3.4"
  - "A.6.3.NAR"
  - "B.3"
  - "C.18"
  - "C.19"
  - "C.30.TFS-REL"
  - "C.32.P2S"
  - "E.17"
  - "E.18"
  - "E.18.1"
  - "E.23"
  - "G.11"
  - "G.5"
keywords:
---

### E.18.3:0 - Use This When

Use this pattern when a team is planning, reviewing, or explaining a transformation and a route-like flow card is useful, but branches, joins, guards, or connections to separately governed positions determine what can follow. The practical need is to recover those transformation-flow relations without treating displayed order as performed-work order, evidence, decision, or authorization.

The admitted object is a `U.Structure` whose substrate is transformation-flow structure over bounded `U.Transformation` values, typed flow positions, exact flow relations, and explicit connections to positions governed by neighboring patterns.

Do not use this pattern merely because a visible record or description is a route, path, graph, process map, chain, loop, or swimlane. First ask whether typed transformation positions, exact crossings and guards, a flow valuation when current, preserved transformation structures, C.33 adequacy notes, and direct governing-pattern connections are recoverable.

The first useful move is small: name the transformed entity and kind, then name two candidate transformation positions and the exact relation or guard that may change which continuation is admissible. If that relation is not recoverable, keep the visible artifact as a `ProvisionalUnfoldingDemonstrationDescription@Context` and use the broader `A.22.CGUS` admission question.

