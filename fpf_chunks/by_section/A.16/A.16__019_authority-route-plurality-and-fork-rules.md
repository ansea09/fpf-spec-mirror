---
chunk_kind: "child"
pattern_id: "A.16"
pattern_title: "Language-State Transduction Coordination"
section_id: "A.16:18"
section_title: "Authority, Route Plurality, and Fork Rules"
source_path: "FPF-Spec.md"
output_path: "by_section/A.16/A.16__019_authority-route-plurality-and-fork-rules.md"
commit_sha: "18497f0808242ab7c1a31cb5c94898e9f6b6879d"
heading_path:
  - "A.16 — Language-State Transduction Coordination"
  - "A.16:18 — Authority, Route Plurality, and Fork Rules"
line_start: 21459
line_end: 21508
dependencies:
  - "A.16.0"
  - "A.16.0-A.16.2"
  - "A.16.1"
  - "A.16.2"
  - "A.18"
  - "A.19"
  - "A.6.A"
  - "A.6.P"
  - "B.4.1"
  - "B.5.2.0"
  - "C.16.Q"
  - "C.2.2a"
  - "C.2.4"
  - "C.2.5"
  - "C.2.6"
  - "C.2.7"
  - "C.2.LS"
  - "E.18"
keywords:
  - "admissible moves"
  - "handoff"
  - "language-state"
  - "reopen"
  - "respecify"
  - "retire"
  - "sketch-backoff"
  - "transduction"
---

### A.16:18 - Authority, Route Plurality, and Fork Rules

The pattern is not just about movement; it is about admissible movement under explicit authority boundaries.

#### A.16:18.1 - Multi-route state versus lineage fork
A **multi-route state** means one governed member still keeps several downstream directions live inside one publication such as `RoutedCueSet`.

A **lineage fork** means separate successor members have already been published, each with distinct authority, losses, and future handoff semantics.

The first is plurality inside one member. The second is explicit branching of lineage. Reviewers shall not treat them as the same lineage relation.

#### A.16:18.2 - Four route / authority states
A governed publication after route work is usually in one of four states:

- **open plurality** - several downstream directions remain live;
- **selected-route-before-endpoint-publication** - one route is preferred, but the `U.EpistemePublication` is still an early or seam publication form;
- **endpoint-pattern-publication-issued** - a named endpoint pattern now governs the relevant `U.EpistemePublication` form and responsibility handoff;
- **retired / withdrawn** - the publication or branch is no longer current and survives only as historical continuity.

Confusing these states is one of the main causes of premature endpoint language.

#### A.16:18.3 - `AuthorityState` extraction note
The four states above may be reused as `AuthorityState`, an extracted shared profile for corridor coordination and review.

That extraction does **not** create a new governing pattern. It reuses the state vocabulary already pattern-governed here for later cross-references in `B.4.1`, `B.5.2.0`, `A.6.P`, `C.16.Q`, `A.6.A`, and `A.15`.

`AuthorityState` names authority posture after route work. It does not replace `routeDecision`, `selectedRoute`, `routeAuthorityState`, route-bearing publication governance, gate state, or work-execution state. Any `endpoint-pattern-publication-issued` state still names the downstream governing pattern and governed `U.EpistemePublication` form explicitly.

#### A.16:18.4 - Authority may rise, stay bounded, fall, or retire
A move may:

- **raise authority**, as when a routed cue becomes an admissible `U.EpistemePublication` form governed by a named endpoint pattern;
- **keep authority bounded**, as when a route-bearing publication clarifies one route without claiming endpoint governance;
- **lower authority**, as when reopening or sketch-backoff withdraws prior closure or route force;
- **retire authority**, as when a branch or publication is explicitly withdrawn from current use.

The authority effect should be named as carefully as the move kind itself.

#### A.16:18.5 - Boundary to governing pattern replacement
`A.16` never authorizes a silent governing pattern replacement. If a route crosses into `A.6.P`, `B.5.2`, `A.15`, `C.25`, or another endpoint governing pattern, that governing pattern and the pattern-governed publication form must be named explicitly. `A.16` coordinates the crossing; it does not absorb the destination governing pattern's semantics.

#### A.16:18.6 - `EndpointAdmissionProfile` extraction note
The corridor can reuse an `EndpointAdmissionProfile` as a declarative pattern-derived profile for admissible handoff from language-state publications to receiving governing patterns.

That profile is stated over already pattern-governed conditions: declared language-state positions in `C.2.2a`, facet readings in `C.2.LS` and `C.2.4`-`C.2.7`, explicit route state in `B.4.1`, prompt-readiness in `B.5.2.0`, and witness or grounding conditions that are already visible in the publication chain.

`EndpointAdmissionProfile` decides whether handoff is admissible; it does not govern the downstream publication form itself. A relation-like skeleton may therefore be admitted toward `A.6.P`; an explicit open question with rival-set may be admitted toward `B.5.2.0`; evaluative or `A.6.A`-inviting publication content may be admitted toward `C.16.Q` or `A.6.A`; executable docking may be admitted toward `A.15`.

No admission result makes a receiving governing pattern optional. Tone, style, or mere apparent explicitness is never sufficient by itself; the relevant governing pattern conditions still have to be named and met.

