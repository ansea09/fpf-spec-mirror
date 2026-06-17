---
chunk_kind: "child"
pattern_id: "A.16.0"
pattern_title: "U.LanguageStateMoveTrajectory - Optional trajectory-account normal form over the language-state U.CharacteristicSpace"
section_id: "A.16.0:4"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/A.16.0/A.16.0__005_solution.md"
commit_sha: "205de763b710fe9f2baecbcdae132ec8fdbbe38c"
heading_path:
  - "A.16.0 — U.LanguageStateMoveTrajectory - Optional trajectory-account normal form over the language-state U.CharacteristicSpace"
  - "A.16.0:4 — Solution"
line_start: 22422
line_end: 22529
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
  - "E.17"
  - "E.17.1"
  - "E.18"
  - "F.9"
  - "F.9.1"
keywords:
  - "fork"
  - "handoff"
  - "heavy history"
  - "lineage"
  - "merge"
  - "supersedes"
  - "trajectory account"
---

### A.16.0:4 - Solution
`U.LanguageStateMoveTrajectory` is the **optional** trajectory-account normal form that records how successive governed `U.Episteme` publications are linked across position claims in the declared language-state `U.CharacteristicSpace` chart named in `C.2.2a`.

It does **not** define position semantics, move admissibility, or publication-face ontology by itself. Those remain with `C.2.2a` / `A.19`, `A.16`, and `E.17` / `E.18` respectively.

It answers the question: `when history itself matters, which governed publication is current, which members precede or branch from it, which admissible moves relate them, which publication forms carry them, what was lost, and who now governs the next responsibility?`

#### A.16.0:4.1 - Ontological subject and role lanes
In this cluster, keep six roles distinct:

- **current governed member** - the current `U.Episteme` publication under language-state governance;
- **lineage links** - explicit `derivedFrom`, `supersedes`, `forkedFrom`, `mergedFrom`, and retirement / no-successor links among governed members;
- **grounds / witnesses** - service disturbances, model-vs-observation discrepancies, traces, model outputs, bodily tensions, contrasts, or exemplars that justify the history;
- **publication forms** - cue packs, routed cue sets, prompt forms, typed route-bounded projection publications, partial normal forms, and records governed by endpoint patterns through which lineage members are published;
- **publication faces** - the existing MVPK faces on which those publication forms are rendered when face typing matters;
- **carriers** - documents, console notes, cards, trace files, or model outputs or carriers that hold or render those publications.

A multi-route state inside one current governed member is **not** yet a lineage fork. It becomes a fork only when distinct successor members are published and given distinct authority, losses, or handoff semantics.

A trajectory step may add a new lineage member, revise the current member, or relate several members through fork, merge, supersession, or retirement. It does **not** mean that the source phenomenon itself has moved through the language-state chart.

#### A.16.0:4.2 - Position-account discipline
The position read by this pattern is the slot-explicit claim defined in `C.2.2a`: a partial coordinate publication in the declared language-state `U.CharacteristicSpace`, where each basis slot publishes a `ValueSet(slot)`, interval, or other admissible set-valued claim.

Early seam publications may leave some slots unknown or wide. That uncertainty is admissible only if it is explicit. A trajectory account therefore records the position claims of the current lineage member and, when needed, of the predecessor or sibling members that justify the move reading.

#### A.16.0:4.3 - Use threshold and core trajectory record
A single local `A.16` move note is sufficient when no load-bearing branch, loss, handoff, or supersession structure needs publication.

Use `U.LanguageStateMoveTrajectory` when at least one of the following is load-bearing:

- derivation, supersession, fork, merge, or retirement structure;
- multi-step loss notes or reopen conditions that would be hidden by a compressed move note;
- responsibility handoff whose legitimacy depends on upstream history;
- bridge or viewpoint entry that depends on upstream route, loss, or lineage structure.

A conforming trajectory account then keeps at least the following explicit:

- the current governed member;
- predecessor, sibling, or ancestor references when the current reading depends on lineage structure;
- the lineage link kind (`derivedFrom`, `supersedes`, `forkedFrom`, `mergedFrom`, `retiredWithSuccessor`, `retiredWithoutSuccessor`, or another explicitly typed link);
- the current position claim and any load-bearing predecessor position claims;
- the typed move or move sequence that relates them;
- the publication form currently carrying the governed member and, if it matters, the MVPK face carrying that form;
- the next intended governing pattern or handoff state;
- any loss note, reopen condition, branch-specific authority note, or bridge-sensitive note that matters.

#### A.16.0:4.4 - Recorded move-family discipline
`U.LanguageStateMoveTrajectory` records the governed `A.16` move family: `notice`, `stabilize`, `route`, `projection`, `formalize`, `operationalize`, `reopen`, `sketchBackoff`, `respecify`, and `retire`.

The point is not that every account uses every move. The point is that forward movement, retreat, reframing, and explicit retirement belong to one governed family when that history is worth publishing.

Detailed move guards remain with `A.16`. `A.16.0` records their use; it does not govern them.

#### A.16.0:4.5 - Seam publication and face discipline
A trajectory account may refer to seam publications that remain upstream of endpoint governance. In the current cluster these include:

- `U.PreArticulationCuePack`;
- `RoutedCueSet`;
- `U.AbductivePrompt`;
- partial normal forms already typed elsewhere;
- other explicitly typed upstream publications that preserve non-endpoint status.

These are not a rival publication-face sequence. They are typed publication forms rendered, when necessary, on existing MVPK faces under `E.17`.

Untyped placeholders such as "route-bounded publication face" are non-conformant in a trajectory account unless the text also names the actual publication form and, separately, the MVPK face if face typing matters.

#### A.16.0:4.6 - Endpoint docking and responsibility handoff
A trajectory does not need to terminate in order to be useful. What matters is a visible docking milestone or responsibility handoff into a governing pattern that is allowed to take the next pattern-governed declaration.

Typical docking governing patterns include:

- `A.6.P` for relation repair forms;
- `A.6.A` for invitation forms;
- `C.16.Q` for evaluative repair forms;
- `B.5.2` for later abductive work;
- `A.15` for method-facing or work-facing forms;
- `C.25` for endpoint bundle structures.

A trajectory account should therefore name not only the docking governing pattern but also the pattern-governed publication or record that now carries the next pattern-governed declaration. Naming only the governing pattern under-publishes the handoff.

After such a handoff, monitoring, maintenance, revisit, or later re-entry may continue through new lineage members or later trajectories. The pattern therefore distinguishes `lineage continuity` from `current governing pattern responsibility`.

#### A.16.0:4.7 - Effect-free moves versus work-requiring crossings
Some `formalize` and `operationalize` steps are effect-free epistemic changes: rewriting, slot-explicit articulation, route-bounded partialization, view retargeting, or normal-form repair over already available grounds.

Other steps require new measurements, experiments, instrumentation, execution, or other `U.Work`. When that happens, the trajectory account shall publish the crossing or handoff explicitly rather than pretending that world-facing work occurred inside the language layer. `A.16.0` records that the crossing was required; the relevant work, gate, or endpoint governing pattern records the world step itself.

#### A.16.0:4.8 - Relation to `A.16` and `E.18`
`U.LanguageStateMoveTrajectory` is not an `E.18` path publication, and `A.16.0` does **not** govern the semantics of language-state movement.

- `A.19` plus `C.2.2a` govern the declared characteristic-space reading of positions;
- `A.16` governs move kinds and move guards;
- `E.17` / `E.18` govern publication-face discipline and graph publication of paths;
- endpoint patterns govern endpoint-local `U.EpistemePublication` forms and declarations.

`A.16.0` standardizes only the heavier history package for cases where that package is itself worth publication.

#### A.16.0:4.9 - Bridge and viewpoint entry
A trajectory may later cross a viewpoint or context boundary. When that happens:

- bridge substitution licence remains with `F.9`;
- stance overlays remain with `F.9.1`;
- viewpoint reuse remains with `E.17.1`;
- endpoint-local semantics remain with their named endpoint patterns and governed publication forms.

`A.16.0` only makes those entry points explicit so that later attachments do not float without an upstream history account.

