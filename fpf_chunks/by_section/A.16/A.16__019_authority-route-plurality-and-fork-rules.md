---
chunk_kind: "child"
pattern_id: "A.16"
pattern_title: "Language-State Move Coordination"
section_id: "A.16:18"
section_title: "Authority, Route Plurality, and Fork Rules"
source_path: "FPF-Spec.md"
output_path: "by_section/A.16/A.16__019_authority-route-plurality-and-fork-rules.md"
commit_sha: "7205ce8cea50eb778520a026373b2b7bcbc43fbb"
heading_path:
  - "A.16 — Language-State Move Coordination"
  - "A.16:18 — Authority, Route Plurality, and Fork Rules"
line_start: 27153
line_end: 27204
dependencies:
  - "A.16"
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
  - "E.10.MOVE"
  - "E.18"
keywords:
  - "admissible language-state move"
  - "language-state"
  - "move"
  - "reopen"
  - "respecify"
  - "responsibility transfer"
  - "retire"
  - "sketch-backoff"
---

### A.16:18 - Authority, Route Plurality, and Fork Rules

The pattern is not just about movement; it is about admissible movement under explicit authority boundaries.

#### A.16:18.1 - Multi-route state versus lineage fork
A **multi-route state** means one route-bearing publication such as `RoutedCueSet` still keeps several downstream directions live.

A **lineage fork** means separate successor members have already been published, each with distinct authority and losses, plus any separately established future next-use or responsibility-handoff conditions.

The first is plurality inside one member. The second is explicit branching of lineage. Reviewers shall not treat them as the same lineage relation.

#### A.16:18.2 - Four route / authority states
A route-bearing publication after route work is usually in one of four states:

- **open plurality** - several downstream directions remain live;
- **selected-route-before-endpoint-publication** - one route is preferred, but the issued form is still early or at a seam; no target episteme or project record has yet passed an endpoint admission test for the stronger use;
- **endpoint-pattern-publication-issued** - the target claim-bearing episteme or project record meets the named endpoint criterion, while current availability separately names the form, bounded use, carrier, and `EpistemePublicationRelation` occurrence;
- **retired / withdrawn** - the publication or branch is no longer current and survives only as historical continuity.

Confusing these states is one of the main causes of premature endpoint language.

#### A.16:18.3 - `AuthorityState` extraction note
The four states above may be reused as `AuthorityState`, an extracted shared profile for corridor coordination and review.

That extraction does **not** create a new pattern. It reuses the state vocabulary defined here for later cross-references in `B.4.1`, `B.5.2.0`, `A.6.P`, `C.16.Q`, `A.6.A`, and `A.15`.

`AuthorityState` names route authority state after route work. It does not replace `routeDecision`, `selectedRoute`, `routeAuthorityState`, route-bearing publication rules, gate state, or work-execution state. Any `endpoint-pattern-publication-issued` state still names the next pattern and its concrete rule or test, the selected `U.Episteme` or project record, the publication form and bounded use, and the `EpistemePublicationRelation` occurrence when availability matters.

#### A.16:18.4 - Authority may rise, stay bounded, fall, or retire
A move may:

- **raise authority**, as when a claim-bearing episteme or project record meets a named endpoint criterion for a stronger use; a separate publication occurrence may make it available but does not grant that authority;
- **keep authority bounded**, as when a route-bearing publication clarifies one route without claiming endpoint admission;
- **lower authority**, as when reopening or sketch-backoff withdraws prior closure or route force;
- **retire authority**, as when a branch or publication is explicitly withdrawn from current use.

The authority effect should be named as carefully as the move kind itself.

#### A.16:18.5 - Boundary to endpoint-rule change
`A.16` never authorizes a silent change in the rule claimed to apply. If a language-state move makes an `A.6.P`, `B.5.2`, `A.15`, `C.25`, or another endpoint question current, name that question, the pattern and contribution used to answer it, and the target publication form. Add an exact subject assertion, predicate, or `ClaimGraph` only when its identity or edition changes the use. `A.16` coordinates the move; it does not replace the endpoint rule.

#### A.16:18.6 - `EndpointAdmissionProfile` extraction note
The corridor can reuse an `EndpointAdmissionProfile` as a declarative profile for admissible next-use docking from a language-state publication to a later pattern-based question or use.

That profile uses conditions already defined in `C.2.2a`, the facet readings in `C.2.LS` and `C.2.4`-`C.2.7`, explicit route state in `B.4.1`, prompt-readiness in `B.5.2.0`, and witness or grounding conditions visible in the publication chain.

`EndpointAdmissionProfile` decides whether that docking is admissible; it does not replace the rule for the downstream content or publication form. A relation-like skeleton may therefore be admitted toward `A.6.P`; an explicit open question with rival-set toward `B.5.2.0`; evaluative or action-inviting content toward `C.16.Q` or `A.6.A`; and executable docking toward `A.15`.

Next-use docking establishes no responsibility, commitment, permission, or authority relation. If an actual responsibility handoff also occurs, record and test that separate relation under `A.16:4.4` and its applicable pattern.

No admission result makes the endpoint conditions optional. Tone, style, or apparent explicitness is never sufficient by itself; apply the relevant pattern's actual conditions.

