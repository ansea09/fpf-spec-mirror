---
chunk_kind: "child"
pattern_id: "G.5"
pattern_title: "Multi‑Method Dispatcher and MethodFamily Registry"
section_id: "G.5:0.4"
section_title: "First output"
source_path: "FPF-Spec.md"
output_path: "by_section/G.5/G.5__006_first-output.md"
commit_sha: "9a9c1b14df894386c664cf49a9ccbbd4a4063100"
heading_path:
  - "G.5 — Multi‑Method Dispatcher and MethodFamily Registry"
  - "G.5:0.4 — First output"
line_start: 103414
line_end: 103436
dependencies:
  - "C.11"
  - "C.18"
  - "C.19"
  - "C.23"
  - "C.24"
  - "C.32.P2S"
  - "C.35"
  - "E.17"
  - "E.24.PUB"
  - "E.4.PFR"
  - "G.0"
  - "G.11"
  - "G.2"
  - "G.2-G.4"
  - "G.5"
  - "G.6"
  - "G.9-G.11"
  - "G.Core"
keywords:
  - "RankedShortlist"
  - "SelectorOutcomeKind"
  - "Shortlist"
  - "ShortlistId"
  - "SpecialistHandoff"
  - "abstain/escalation result"
  - "are forbidden in registry"
  - "assurance"
  - "basis pins"
  - "dispatcher"
  - "eligibility"
  - "generator-family registry"
  - "in core registry and eligibility fields"
  - "method-family registry"
  - "no hidden scalar winner"
  - "or selector‑kernel obligations (E.5.*)"
  - "selected-set publication"
  - "set-result outcome"
  - "tool choices are outside the core"
---

### G.5:0.4 - First output

The first useful output from this dispatcher and registry question is one declared `SelectorOutcome` admitted by the closed `SelectorOutcomeKind` set in §4.4b. For `SetResultOutcome`, use the closed `SetResultFamily` rule to distinguish `Shortlist`, `RankedShortlist`, and `JointUseSet`; for another outcome kind, state its admitted handoff, abstain, or escalation content. In every case, state the applicable members or keyed member entries, ordering, named use and inclusion conditions when applicable, and basis pins in one place.

For an ordinary run over already grounded rows, that selector-facing result content is enough. The basis pins may be direct references to the declared grouping, eligibility, and comparison basis, and the same compact record may carry the DRR/SCR-addressable audit refs required by S3. Do not require a fresh registry build, `CrossingAllowance`, evidence graph, assurance claim, stable public id, separate audit package, or E.24.PUB occurrence unless the current use actually needs that stronger object or claim.



Here a selector outcome means complete selector-facing result content. A stable public designator is an additional field only when a named use needs it. Neither the result content nor its designator is evidence that selection Work or an actual `Select` application occurred, and neither is an E.24.PUB availability occurrence. Claim actual publication only through the exact selected C.2.1 episteme edition, audience declaration, bounded-use declaration, publication form, presentation carrier, and obtaining `EpistemePublicationRelation`; rendering or uploading Work remains another occurrence.


If that first output cannot yet be stated honestly, the `G.5` result is incomplete.

G.5 keeps the dispatcher and registry object set here and leaves universal Part-G invariants to `G.Core`; method-specific and generator-specific semantics stay in their named source patterns and arrive here only through explicit pins.

When `C.11` has already emitted one local choice result, `C.19` one pool-policy result, or `C.24` one enactment-facing next action, `G.5` applies when the question becomes declaring selector-facing result content for retained alternatives, all-member joint use, or a narrowed handoff rather than one more explanation of why the upstream result looked reasonable. The `G.5` result states its outcome kind, applicable public label, membership form, and basis pins directly.

The `G.5` result is incomplete if its outcome kind, applicable public label, retained members or keyed joint-use member entries, ordering, named use where required, handoff content, abstain or escalation condition, or basis pins are still only implicit in upstream notes.

When a framework needs a selector-facing result for a selected pattern set, use `G.5` only to declare that result: scope, selection or inclusion conditions, included pattern refs, excluded candidate refs when relevant, and basis pins. Use `JointUseSet` only when every exact ref is included for the named use; otherwise retain shortlist semantics. Add a stable public identity and its UTS obligation only when a named use needs them. If audience availability is current, use E.17 for a source-backed face and return to source and E.24.PUB for the publication occurrence and availability. This selected-set result does not define pattern-use relations, architecture decisions, or framework edition dependencies.

When exact framework editions are the members, preserve their existing edition identities and use E.4.PFR for any direct dependency or compatibility claim. G.5 creates no `MethodRef`, method-family row, publication occurrence, access claim, or actual selection Work for those editions.

