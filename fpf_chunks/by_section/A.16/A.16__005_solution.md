---
chunk_kind: "child"
pattern_id: "A.16"
pattern_title: "Language-State Move Coordination"
section_id: "A.16:4"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/A.16/A.16__005_solution.md"
commit_sha: "7f7c592f4d633e54cdb202d622d6e0e05df41517"
heading_path:
  - "A.16 — Language-State Move Coordination"
  - "A.16:4 — Solution"
line_start: 26653
line_end: 26747
dependencies:
  - "A.15"
  - "A.15.1"
  - "A.15.2"
  - "A.15.5"
  - "A.15.PROD"
  - "A.16"
  - "A.16.0"
  - "A.16.0-A.16.2"
  - "A.16.1"
  - "A.16.2"
  - "A.18"
  - "A.19"
  - "A.2"
  - "A.2.1"
  - "A.6.A"
  - "A.6.P"
  - "B.4.1"
  - "B.5.2.0"
  - "C.16.Q"
  - "C.2.1"
  - "C.2.2a"
  - "C.2.4"
  - "C.2.5"
  - "C.2.6"
  - "C.2.7"
  - "C.2.LS"
  - "C.25"
  - "E.10.MOVE"
  - "E.11.PUR"
  - "E.18"
  - "E.24.PUB"
  - "F.6"
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

### A.16:4 - Solution

`A.16` defines admissible move names, guards, identity decisions, and next-use docking. It does not define formality `F`, make Work occur, pass an endpoint test, create publication availability, establish authority, or supply a rival path calculus.

Here *move* means a typed transition in the publication of selected episteme content. Observation is a precursor normally published through `B.4.1`; A.16 starts when a cue is deliberately noticed, stabilized, route-published, projected, formalized, operationalized, reopened, respecified, or retired.

#### A.16:4.1 - Canonical move table

This is the one canonical move table. Later examples apply it; they do not define another move family.

| Move | Use it when | Publication result | Keep explicit |
| --- | --- | --- | --- |
| `notice` | a low- or unstable-articulation cue is worth preserving | preservation-worthiness becomes explicit; a first typed preservation may begin | why the cue is worth preserving and which witnesses remain |
| `stabilize` | the noticed cue needs a steadier local shape before route or endpoint choice | `U.PreArticulationCuePack` or an equivalent early form may become admissible | cue nucleus, anchors, contrasts, witnesses, and preservation rationale |
| `route` | a stabilized cue has several plausible downstream directions or one route must be selected | `RoutedCueSet` or another route-bearing publication makes plurality and any selection explicit | live routes, selected route if any, selection reason, and reopen condition |
| `projection` | one aspect of an explicit route must be foregrounded without claiming endpoint admission | a typed route-bounded partial publication on an existing MVPK face | what is foregrounded, what is omitted or lost, and how reopen remains possible |
| `formalize` | articulation or closure can increase under a named later rule | a more explicit symbolic, slot, or normal-form publication | the rule used, changed facets, and any new evidence-generating Work boundary |
| `operationalize` | selected content is ready to face a method, Work, gate, or other operational question | the episteme or project record is docked to the pattern that defines or tests that use | the exact downstream contribution, its guard, and any world-facing Work boundary |
| `reopen` | the current route, frame, or closure no longer holds cleanly | the same broad family returns with reduced closure | reopened rivals, retained witnesses, and which prior endpoint-use or current-use claim no longer holds |
| `sketchBackoff` | an endpoint-bound or operational form over-commits the available grounds | an exploratory cue-bearing form becomes admissible again | retained anchors and witnesses, withdrawn closure, and the next safe question |
| `respecify` | the broad family remains plausible but its framing scaffold, facet reading, or route specification is wrong | a revised framing or route specification replaces the earlier one | replaced commitments, invariants that stay fixed, and any episteme-identity change |
| `retire` | a cue, route-bearing publication, episteme, or branch is no longer current for the named use because its grounds failed, a successor took over, or a current-use decision ended | retirement or withdrawal is explicit | reason, exact retired object, successor or no-successor note, and preserved history |

The table names moves, not the resulting objects. `U.PreArticulationCuePack`, `RoutedCueSet`, and `U.AbductivePrompt` are publication forms defined elsewhere. A claim-bearing episteme remains `U.Episteme`; `E.24.PUB` separately defines a bounded publication occurrence.

`projection` means route-bounded partialization. Its result must be a typed publication form; an MVPK face alone or an untyped placeholder is not enough. `respecify` changes framing, route specification, or a facet-profile reading. It does not replace the slot-explicit repairs governed by `A.6.P`, `C.16.Q`, or `A.6.A`.

Do not use A.16 to decide measurement admissibility, Bridge substitution, endpoint ontology, or another subject claim. Name the applicable pattern and test directly; A.16 coordinates only the publication move that makes that question current.

#### A.16:4.2 - Guard discipline

State the guard through named language-state facets and the route condition that matters. Use `AE` from `C.2.4`, `CD` from `C.2.5`, `LanguageStateAnchoringMode` from `C.2.6`, and `LanguageStateRepresentationFactorBundle` from `C.2.7`, separately or through one published facet profile. Add witnesses, scope, and `GammaTime` selectors when needed. “The idea matured” is not a guard.

A summarized chain may omit repeated unchanged fields, but it must leave every move identity, endpoint-rule change, loss, and status change that affects interpretation reconstructible. A later higher-closure publication does not retroactively strengthen an earlier cue; later retreat does not erase the earlier publication.

#### A.16:4.3 - Decide identity before describing movement

Do not use “move between publication forms” as a shortcut across these three cases:

1. **First typed preservation.** A precursor cue, trace, contrast, or witness may have no source episteme or source publication form. Name the precursor and the first typed preservation form. C.2.1 governs the identity of the first claim-bearing episteme when one is admitted.
2. **Same episteme edition, another form.** When EntityOfConcern, ClaimGraph content, and effective reference scheme remain the same, one episteme edition may be issued in another form or on another carrier. Name the episteme and source and target forms only when they matter. `E.24.PUB` governs each claimed availability occurrence; neither form nor occurrence creates a successor episteme.
3. **Content-changing successor.** When a C.2.1 discriminator changes, identify a separate target episteme. Name the source and target epistemes, the changed discriminator, what content is preserved, changed, and lost, and the exact lineage relation only when its predicate obtains. A repeated label, form, carrier, or move name proves no continuity. Use `A.16.0` only if the multi-step or branching history is load-bearing.

The same discipline applies to project records through their own identity patterns. `E.24.PUB` says that an already identified episteme was made available for a bounded use; it says neither that content changed nor that an endpoint test passed.

#### A.16:4.4 - One minimal move note

Write one note, keeping conditional fields out unless they change the use:

| Field | Minimum content |
| --- | --- |
| Current item | precursor cue or exact source episteme/project record; source form only when one exists and matters |
| Identity case | first typed preservation, same edition in another form, or content-changing successor |
| Move and guard | one move from §4.1 and the changed facet or route condition that justifies it |
| Target | exact target episteme/project record when identified, typed target publication form, and the downstream pattern's concrete definition, constraint, or test; name the exact `ClaimGraph` carrying that rule only when its identity or edition changes the use |
| Preservation | witnesses or anchors retained; for a successor episteme, content preserved, changed, and lost plus any exact lineage relation |
| Return | endpoint condition not yet met, omitted or lost content, and reopen or retirement condition |

Add an `EpistemePublicationRelation` occurrence only when bounded availability matters. Add the MVPK face only when rendering matters. Neither replaces the form, episteme, or next pattern.

#### A.16:4.5 - Work crossing and actual relation changes

Some `formalize` and `operationalize` moves only re-express available content. Others require measurements, experiments, instrumentation, execution, or other dated `U.Work`. In the latter case, expose the boundary and use the applicable Work, measurement, experiment, gate, or endpoint pattern. A.16 records the pending or separately established crossing; it does not claim that Work occurred or produced a result.

Next-use docking and a Work crossing normally change no authority, responsibility, permission, or commitment relation. If one of those relations actually changes, record it as a separate claim: exact giving and receiving admitted systems; any exact `U.SystemRoleAssignment` occurrences through which they participate; the exact relation; its object or action, scope, and effective interval; and the assigning, instituting, revoking, or superseding act when its pattern requires one. A.2, A.2.1, and the applicable deontic or authority pattern establish and test that claim.

Use `A.16.0` for such a handoff only when its legitimacy or interpretation depends on upstream move or lineage history. Otherwise the local Work-boundary note and separately established relation are enough.

#### A.16:4.6 - Keep coordination claims separate

Do not compress several claims into `AuthorityState`. A reusable language-state coordination readout is only a compact view of independently established facts, not a new U-kind or world-side state. Include only the fields needed by the reader:

| Claim | What to show |
| --- | --- |
| Route plurality or selection | live routes; selected route if any; selection reason; route-bearing publication |
| Endpoint admission or use disposition | named endpoint test, its result, and the exact stronger use admitted, narrowed, or blocked |
| Publication availability | exact episteme, form, bounded use, and `EpistemePublicationRelation` occurrence when current |
| Current use or retirement | exact cue, episteme, publication, or branch and the currentness, withdrawal, supersession, or retirement claim that applies |
| Actual relation change | only an independently established authority, responsibility, permission, or commitment relation with participants, object or action, scope, interval, and act; otherwise say that no such relation changes |

Open route plurality is not a lineage fork. A multi-route state keeps several directions live inside one route-bearing publication. A lineage fork has separately identified successor members, their preserved and lost content, and any exact lineage relations that obtain.

`EndpointAdmissionProfile` may still be reused as a declarative decision profile for next-use docking. It combines the relevant `C.2.2a` position, `C.2.LS` facet readings, route condition from `B.4.1`, prompt readiness from `B.5.2.0`, and visible witness or grounding conditions. It decides only whether docking to the later question is admissible: relation-like content toward `A.6.P`, an open question and rival set toward `B.5.2.0`, evaluative or action-inviting content toward `C.16.Q` or `A.6.A`, viability content toward `C.25`, and executable docking toward `A.15`. The endpoint pattern still decides its own content; tone, style, or apparent explicitness passes no endpoint test by itself. The admission result creates no authority, responsibility, permission, commitment, publication, gate, or Work state.

#### A.16:4.7 - One history threshold

A local note is sufficient when the move or short chain is reconstructible without extra lineage machinery. Use `A.16.0` only when at least one of these is load-bearing:

- derivation, supersession, fork, merge, or retirement structure;
- a multi-move history whose compression would hide a change in the applicable pattern or rule;
- loss notes or reopen conditions spanning more than one move; or
- an actual responsibility handoff, Bridge entry, or viewpoint entry whose legitimacy or interpretation depends on upstream history.

When that history must itself be published as a graph path, use `E.18`. A.16 defines move admissibility; A.16.0 packages the trajectory account; E.18 governs the graph publication.

