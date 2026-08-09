---
chunk_kind: "child"
pattern_id: "A.16"
pattern_title: "Language-State Move Coordination"
section_id: "A.16:4"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/A.16/A.16__005_solution.md"
commit_sha: "036c056e98c38522172c6b7b3ad08214281cc4e4"
heading_path:
  - "A.16 — Language-State Move Coordination"
  - "A.16:4 — Solution"
line_start: 27045
line_end: 27106
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

### A.16:4 - Solution
`A.16` defines only the admissible move kinds, their guards, and docking rules for movement among declared language-state positions. It does **not** define `F`, the trajectory-account semantics, or a rival graph calculus beside `E.18`.

In this pattern, `move` is a local term for a typed transition between publication forms of selected `U.Episteme` content. It is not a general project move, pattern-use recommendation, work-entry readiness relation, performed work, or work plan. When source prose uses move-like wording outside this local language-state scope, restore the project concern through `E.10.MOVE` and then use `E.11.PUR`, `A.15.5`, `A.15.1`, `A.15.2`, or the pattern for the actual question.

A conforming move may be published as a local move note without any `U.LanguageStateMoveTrajectory` wrapper. Use `A.16.0` only when lineage, branch structure, loss notes, supersession, retirement, bridge-sensitive history, or a change in the rule applied after the move must be published as an account.

Observation itself is a precursor condition typically published through `B.4.1`. `A.16` move kinds begin once a cue is deliberately noticed, stabilized, route-published, reopened, formalized, operationalized, respecified, or retired under explicit move discipline.

#### A.16:4.1 - Admissible language-state move family
| Move | What it does | Typical source condition | Typical publication effect |
|---|---|---|---|
| `notice` | marks that a low-articulation cue is being deliberately preserved | low or unstable articulation | cue preservation becomes explicit enough for early publication work |
| `stabilize` | makes the local shape steadier without forcing route or endpoint choice | cue already noticed | cue nucleus, anchors, or witness structure become steadier |
| `route` | publishes downstream route plurality or a selected route through an explicit route-bearing form | stabilized cue exists | `RoutedCueSet` or equivalent route-bearing publication makes route state explicit |
| `projection` | publishes route-bounded partialization without pretending that endpoint admission conditions are met | route is explicit and one aspect is being foregrounded | a typed route-bounded publication form is emitted on an existing MVPK face, with loss notes and reopen conditions |
| `formalize` | increases explicit symbolic or normal-form structure | articulation threshold is met | a publication form with higher articulation or closure is published; new evidence-generation crossings stay visible if required |
| `operationalize` | turns a selected line toward method, work, or gate use | method, work, or gate-facing line exists | operational hooks become explicit; work crossings stay visible if new world-facing work is required |
| `reopen` | relaxes closure while preserving the current family if possible | route or frame no longer holds cleanly | closure drops and rivals re-open |
| `sketchBackoff` | moves to an exploratory cue-bearing publication form | endpoint-bound, method-facing, work-facing, or gate-facing publication form over-commits the current publication | exploratory cue-bearing form becomes admissible again |
| `respecify` | keeps the broad family but revises framing scaffold, facet-profile reading, or route specification | current framing remains plausible but is stated wrongly | a new framing scaffold or route specification replaces the old one while continuity stays explicit |
| `retire` | declares that a cue, route-bearing publication, or branch is no longer current or no longer worth preserving | better-supported successor exists, supporting grounds have collapsed, or authority has been withdrawn entirely | retirement or withdrawal becomes explicit together with successor or no-successor note |

`A.16` defines these **move names**, not the publication forms or occurrences that may result from them. `U.PreArticulationCuePack`, `RoutedCueSet`, and `U.AbductivePrompt` are publication forms defined elsewhere; they are not move kinds. Any selected claim-bearing episteme remains `U.Episteme`, and `E.24.PUB` separately defines its bounded publication occurrence.

Here `projection` remains the move name, but its reading is tightened: it is route-bounded partialization. The resulting publication must be a **typed publication form** rendered on an existing MVPK face. Naming only the face is insufficient; naming only an untyped placeholder is insufficient.

`respecify` is intentionally narrower than epistemic precision repair. In `A.16`, it may change framing scaffold, route specification, or facet-profile reading while preserving the broad family. Use `A.6.P`, `C.16.Q`, or `A.6.A` for their slot-explicit precision and endpoint-local lexical repairs.

#### A.16:4.2 - Guard discipline
Move guards are stated over named facets from `C.2.LS`, together with witnesses, scope, and `GammaTime` selectors where needed. In practice this means explicit reference to `AE` (`C.2.4`), `CD` (`C.2.5`), `LanguageStateAnchoringMode` (`C.2.6`), and `LanguageStateRepresentationFactorBundle` (`C.2.7`), either facetwise or through one published facet profile. No move may be justified by vague prose such as "the idea matured" without naming what changed in articulation, closure, anchoring, representation, or route state.

#### A.16:4.3 - Docking discipline
After `route`, `projection`, `formalize`, or `operationalize`, keep the following positions distinct whenever they are current:

- the selected claim-bearing `U.Episteme` or project record;
- the **target publication form** being issued, such as `U.PreArticulationCuePack`, `RoutedCueSet`, or `U.AbductivePrompt`;
- the `EpistemePublicationRelation` occurrence only when availability for a bounded use matters;
- the pattern whose content defines, constrains, or tests the target use;
- the **MVPK face** only when rendering matters.

An ordinary move note names the target form and the next pattern's concrete contribution. Add the selected episteme, publication occurrence, or face only when that distinction changes the use; none of them substitutes for another. This is next-use docking, not a transfer of responsibility.

#### A.16:4.4 - Effect-free versus work-requiring moves
Some `formalize` and `operationalize` moves are effect-free epistemic rewrites or moves to publication forms with higher articulation or closure over already available grounds. Others require new measurements, experiments, instrumentation, execution, or other `U.Work`. When the latter happens, the move note shall expose the work-boundary crossing and name the applicable work, measurement, experiment, gate, or endpoint question; `A.16` does not pretend that world-facing work occurred inside the language layer.

A work-boundary crossing or next-use docking does not by itself transfer responsibility. Claim a responsibility handoff only as a separate triggered branch: name the giving and receiving admitted systems or the exact role assignments through which they participate; the exact responsibility, commitment, permission, or authority relation being ended, instituted, or retargeted; its object or action, scope, and effective interval; and the assigning, instituting, revoking, or superseding act when the applicable pattern requires one. `A.16` records the boundary; the applicable role, deontic, permission, or authority pattern establishes and tests the relation.

Use `A.16.0` for this branch only when the handoff's legitimacy or interpretation depends on upstream move or lineage history. Otherwise the work-boundary note and the separately established responsibility relation are enough.

#### A.16:4.5 - Move-note threshold and path publication discipline
A typed local move note is sufficient when a small move or short move chain can be kept reconstructible without publishing extra lineage machinery.

Use `A.16.0` only when at least one of the following is load-bearing:

- derivation, supersession, fork, merge, or retirement structure;
- a multi-move history whose compression would hide a change in the applicable pattern, rule, or authority;
- visible loss notes or reopen conditions spanning more than one move;
- an actual responsibility handoff, bridge entry, or viewpoint entry whose legitimacy or interpretation depends on upstream history.

If the history itself must be published as a graph publication, reuse `E.18`. `A.16` defines move admissibility; `A.16.0` packages trajectory accounts; `E.18` defines graph publication of paths.

