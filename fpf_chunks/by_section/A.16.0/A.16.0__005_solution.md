---
chunk_kind: "child"
pattern_id: "A.16.0"
pattern_title: "U.LanguageStateMoveTrajectory - Optional trajectory-account normal form over the language-state U.CharacteristicSpace"
section_id: "A.16.0:4"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/A.16.0/A.16.0__005_solution.md"
commit_sha: "322625be006f38158e4e7d600f662558f03df77a"
heading_path:
  - "A.16.0 — U.LanguageStateMoveTrajectory - Optional trajectory-account normal form over the language-state U.CharacteristicSpace"
  - "A.16.0:4 — Solution"
line_start: 27596
line_end: 27721
dependencies:
  - "A.16"
  - "A.16.1"
  - "A.16.2"
  - "A.19"
  - "A.6.A"
  - "A.6.P"
  - "B.4.1"
  - "B.5.2"
  - "B.5.2.0"
  - "C.16.Q"
  - "C.2.2a"
  - "C.2.LS"
  - "E.10.MOVE"
  - "E.17"
  - "E.17.1"
  - "E.18"
  - "F.9"
  - "F.9.1"
keywords:
  - "fork"
  - "heavy history"
  - "lineage"
  - "merge"
  - "responsibility transfer"
  - "supersedes"
  - "trajectory account"
---

### A.16.0:4 - Solution
`U.LanguageStateMoveTrajectory` is the **optional** trajectory-account normal form for a load-bearing history across positions in the language-state `U.CharacteristicSpace` named in `C.2.2a`. It records selected episteme editions, links among changed editions, typed moves, publication forms, and any availability occurrence that matters.

It does **not** define position semantics, move admissibility, publication forms, or path-publication semantics. Use `C.2.2a` and `A.19` for positions, `A.16` for moves, `E.24.PUB` for publication availability, and `E.17` or `E.18` for face and path publication.

It answers the question: `when the history matters, which episteme edition is current, what precedes or branches from it, which moves and links connect the entries, how is each edition published when availability matters, what was lost, and which rule or use applies next?`

#### A.16.0:4.0a - E.24.UK settlement

`U.LanguageStateMoveTrajectory` is retained as a dependent durable trajectory-account U-kind under the language-state settlement, not as a root U-kind. Its identity depends on the selected episteme editions, the declared `U.CharacteristicSpace` from `C.2.2a`, the typed move and lineage links, and any publication occurrence that is load-bearing for the account. An ordinary local history, route note, or publication form does not become `U.LanguageStateMoveTrajectory` by resemblance.

#### A.16.0:4.1 - Keep the account positions distinct
Keep seven positions distinct:

- **selected episteme edition** - the current `U.Episteme` whose claims are being positioned or re-expressed;
- **lineage links** - explicit `derivedFrom`, `supersedes`, `forkedFrom`, `mergedFrom`, and retirement or no-successor links among episteme editions when the claims change;
- **grounds or witnesses** - disturbances, discrepancies, traces, model outputs, bodily tensions, contrasts, or exemplars that justify the history;
- **publication form** - a cue pack, routed cue set, prompt form, typed route-bounded projection form, partial normal form, or endpoint-bound record used to express an edition;
- **publication occurrence** - an `EpistemePublicationRelation` occurrence only when availability to an audience for a bounded use matters;
- **publication face** - the MVPK face on which a form is rendered when face typing matters;
- **carrier** - the document, console note, card, trace file, model output, or other entity that bears the form.

A form, face, carrier, or publication-occurrence change can leave the selected episteme edition unchanged. A changed claim discriminator identifies another episteme edition. Publication alone creates neither the edition nor a lineage link.

Several live routes for one selected edition are **not** yet a lineage fork. A fork requires separately identified successor editions with explicit links, authority, and losses; publishing the same edition through two forms is not enough.

A trajectory step may reuse one edition in another form, add a successor edition, or relate several editions through fork, merge, supersession, or retirement. It does **not** mean that the source phenomenon moved through the language-state chart.

Here `route` names an `A.16` move-family label or a typed upstream publication-form cue. It is not an action route, work sequence, workflow, or transformation-flow path.

#### A.16.0:4.2 - Position-account discipline
The position read by this pattern is the slot-explicit claim defined in `C.2.2a`: a partial coordinate publication in the declared language-state `U.CharacteristicSpace`, where each basis slot publishes a `ValueSet(slot)`, interval, or other admissible set-valued claim.

Early seam publications may leave some slots unknown or wide. That uncertainty is admissible only if it is explicit. A trajectory account therefore records the position claim for the current episteme edition and, when needed, for predecessor or sibling editions that justify the move reading.

#### A.16.0:4.3 - Use threshold and core trajectory record
A single local `A.16` move note is sufficient when no load-bearing branch, loss, or supersession structure needs publication and no actual responsibility handoff depends on upstream history.

Use `U.LanguageStateMoveTrajectory` when at least one of the following is load-bearing:

- derivation, supersession, fork, merge, or retirement structure;
- multi-step loss notes or reopen conditions that would be hidden by a compressed move note;
- an actual responsibility handoff whose legitimacy or interpretation depends on upstream history;
- bridge or viewpoint entry that depends on upstream route, loss, or lineage structure.

A conforming trajectory account then keeps at least the following explicit:

- the current selected episteme edition;
- predecessor, sibling, or ancestor editions when the current reading depends on lineage;
- the lineage link kind (`derivedFrom`, `supersedes`, `forkedFrom`, `mergedFrom`, `retiredWithSuccessor`, `retiredWithoutSuccessor`, or another explicitly typed link);
- the current position claim and any load-bearing predecessor position claims;
- the typed move or move sequence;
- the publication form and, when availability matters, the publication occurrence;
- the MVPK face only when rendering matters;
- the next question or use, the applicable pattern, and its concrete contribution;
- when an actual responsibility handoff is load-bearing, the separate participants, relation, object or action, scope, interval, and instituting-act references required by `A.16.0:4.6`;
- any loss note, reopen condition, branch-specific authority note, or bridge-sensitive note that matters.

#### A.16.0:4.4 - Recorded move-family discipline
`U.LanguageStateMoveTrajectory` records the `A.16` move family: `notice`, `stabilize`, `route`, `projection`, `formalize`, `operationalize`, `reopen`, `sketchBackoff`, `respecify`, and `retire`.

Not every account uses every move. Forward movement, retreat, reframing, and explicit retirement belong to one family defined in `A.16` when that history is worth publishing.

`A.16` defines the detailed move guards. `A.16.0` records the moves and their satisfied guards; it does not replace them.

#### A.16.0:4.5 - Seam publication and face discipline
A trajectory account may refer to seam publication forms that remain upstream of endpoint admission. In the current cluster these include:

- `U.PreArticulationCuePack`;
- `RoutedCueSet`;
- `U.AbductivePrompt`;
- partial normal forms already typed elsewhere;
- other explicitly typed upstream publications that preserve a non-endpoint position.

These are not a rival publication-face sequence. They are typed publication forms rendered, when necessary, on existing MVPK faces under `E.17`.

Untyped placeholders such as "route-bounded publication face" are non-conformant in a trajectory account unless the text also names the actual publication form and, separately, the MVPK face if face typing matters.

#### A.16.0:4.6 - Endpoint docking and next use
A trajectory does not need to terminate to be useful. What matters is a visible docking milestone to the next pattern-based question or later use.

Typical next-use patterns include:

- `A.6.P` for relation precision or repair;
- `A.6.A` for an action invitation;
- `C.16.Q` for evaluative precision or repair;
- `B.5.2` for abductive inquiry;
- `A.15` for method-facing or work-facing planning;
- `C.25` for endpoint bundle structure.

Name the next pattern and what its content defines, constrains, or tests. The account already identifies the selected episteme edition; add a project record, particular publication form, or publication occurrence only when that distinction changes the next use. This is next-use docking, not a transfer of responsibility, and a pattern reference alone does not prove endpoint admission.

**Separate responsibility-handoff branch.** Open this branch only when responsibility, commitment, permission, or authority actually changes. Name the giving and receiving admitted systems and, when their system-role classification matters, the exact system-role kinds and assignments through which they participate; name the exact relation before and after the change under its applicable pattern, its governed object or action, scope, and effective interval, and any assigning, instituting, revoking, or superseding act that the relation requires. The trajectory account cites that relation and its history; episteme lineage, publication form, publication occurrence, endpoint admission, and next-use docking neither create nor prove it.

After docking to a next use, monitoring, maintenance, revisit, or later re-entry may continue through new lineage entries or later trajectories. Keep lineage continuity separate from the current endpoint use and from any separately established responsibility or authority relation.

#### A.16.0:4.7 - Effect-free moves versus work-requiring crossings
Some `formalize` and `operationalize` steps are effect-free epistemic changes: rewriting, slot-explicit articulation, route-bounded partialization, view retargeting, or normal-form repair over already available grounds.

Other steps require new measurements, experiments, instrumentation, execution, or other `U.Work`. When that happens, the trajectory account shall expose the work-boundary crossing instead of pretending that world-facing work occurred inside the language layer. The account records why the crossing was required; use the relevant work, gate, or endpoint pattern to describe or test the world step. Add a particular Work, assertion, or `ClaimGraph` identity only when the claim or later reliance depends on it.

A work-boundary crossing does not by itself transfer responsibility or authority. If a separate actual responsibility handoff occurs, use the triggered branch in `A.16.0:4.6` and keep its relation distinct from the Work, episteme lineage, publication, and endpoint use.

#### A.16.0:4.8 - Relation to `A.16` and `E.18`
`U.LanguageStateMoveTrajectory` is not an `E.18` path publication, and `A.16.0` does **not** define language-state move semantics.

- `A.19` and `C.2.2a` define the declared characteristic-space reading of positions;
- `A.16` defines move kinds and guards;
- `E.17` and `E.18` define publication-face discipline and graph publication of paths;
- endpoint patterns define, constrain, or test endpoint-local claims and uses;
- `E.24.PUB` distinguishes the selected episteme edition, publication form, carrier, bounded use, and any publication occurrence that matters.

`A.16.0` standardizes only the heavier history package for cases where that history is itself worth publication.

The word `move` remains inherited from `A.16` and means a typed language-state publication transition. `A.16.0` does not generalize it into project action, work-entry readiness, pattern-use recommendation, performed work, work plan, workflow, or transformation-flow path. If source wording uses move-like language outside this scope, restore the concern through `E.10.MOVE` before selecting `E.11.PUR`, `A.15.5`, the A.15 work family, or another applicable pattern.

#### A.16.0:4.9 - Bridge and viewpoint entry
A trajectory may later cross a viewpoint or context boundary. When that happens:

- the trajectory establishes neither an F.9 Bridge nor the suitability of any bounded cross-context use; exact relation and use claims remain with `F.9`;
- stance notes remain with `F.9.1`;
- viewpoint reuse remains with `E.17.1`;
- endpoint-local semantics remain in the rules defined or tested by the named endpoint patterns; publication availability remains a separate `E.24.PUB` relation.

`A.16.0` only makes those entry points explicit. It establishes no current reliance, authorization, or receiving use. When those questions are live, apply triggered `A.10` or `B.3` for reliance, the pattern that directly constrains the receiving action for authorization, and evidence of the receiving Work or publication for occurrence. No bundled record is required when those questions are not live.

