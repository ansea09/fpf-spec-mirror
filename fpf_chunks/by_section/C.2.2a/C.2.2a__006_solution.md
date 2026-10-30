---
chunk_kind: "child"
pattern_id: "C.2.2a"
pattern_title: "Language-State Chart over U.CharacteristicSpace"
section_id: "C.2.2a:4"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/C.2.2a/C.2.2a__006_solution.md"
commit_sha: "9fa2a3596dab58d282d736bcf413cdda4286db0a"
heading_path:
  - "C.2.2a — Language-State Chart over U.CharacteristicSpace"
  - "C.2.2a:4 — Solution"
line_start: 52480
line_end: 52560
dependencies:
  - "A.16"
  - "A.16.0"
  - "A.19"
  - "A.6.A"
  - "B.4.1"
  - "C.16.Q"
  - "C.2.3"
  - "C.2.4"
  - "C.2.5"
  - "C.2.6"
  - "C.2.7"
  - "C.2.LS"
  - "E.10"
  - "E.17.1"
  - "F.18"
  - "F.9"
  - "F.9.1"
keywords:
  - "articulation"
  - "characteristic space"
  - "closure"
  - "episteme publication"
  - "formality"
  - "language-state chart"
  - "local thresholds"
  - "partial coordinates"
  - "position claim"
  - "representation"
  - "source and use conditions"
---

### C.2.2a:4 - Solution
A language-state chart is a declared `U.CharacteristicSpace` whose basis slots use selected language-state Characteristics and Scales under `A.19`. A profile containing several Characteristics expands into their separate slots; it is not one atomic Coordinate.

#### C.2.2a:4.0a - Chart, position claims and publication

The space declaration identifies the chart and makes its basis, optional overlays and typing hooks recoverable under A.19. A position claim states facet readings about the selected published `U.Episteme` edition; the E.24.PUB publication occurrence remains separate. A score table or local route map can express the declaration and position claims. Its reusable form and carrier remain distinct from those contents.

Changing a slot's Characteristic, Scale or position requires a changed space declaration under A.19. Revising a reading changes the position claim and can use the same space. Changing a threshold changes the predicate under A.19:5.1.8. Changing only the form or carrier of these unchanged contents changes neither the space, reading nor predicate.

#### C.2.2a:4.1 - Core use
Use the declared chart to answer five questions:

- which basis slots define where the governed episteme stands;
- what a position claim in that chart means;
- which thresholds are locally declared over those slots;
- what comparisons are admissible without cross-facet collapse;
- and how the same position claim stays distinct from the publication form currently expressing it.

#### C.2.2a:4.2 - Position reading under `A.19`
A language-state position is a partial, slot-explicit coordinate claim in the declared language-state `U.CharacteristicSpace`.

`ValueSet(Scale)` in A.19 is the full Scale domain. Publish each selected slot's reading as one value or as a supported set of remaining possible values within that domain. This set describes incomplete information about the slot's value. Use an interval only where the Scale admits it; state a decision-relevant `unknown` separately when the available information does not determine the needed reading. For closure, `{CD1, CD2}` can report two remaining possible values while the assessment is incomplete. Separate source and use claims follow C.2.6:4.3: two unresolved possible sources differ from an established contribution by both.

`position` here abbreviates these slot-explicit `A.19` coordinate claims.

#### C.2.2a:4.3 - Facet basis
The language-state chart is coordinated by explicit facet subject patterns rather than by an informal master progression. Select the actual Characteristics and Scales needed for the next action from:

- `C.2.3` for the selected expression properties in a formality assessment, or an explicitly justified local summary;
- `C.2.4` for articulation explicitness;
- `C.2.5` for language-state closure degree;
- `C.2.7` for the language-state representation-factor bundle.

The selected basis slots together define the chart under A.19. Each actual Characteristic has its own Scale and slot. In particular, neither a formality profile nor a representation-factor bundle is silently treated as one Coordinate. `C.2.2a` does **not** govern the internal meanings or Scale semantics of those Characteristics. C.2.6 supplies the source, evidence, access and action-condition account needed beside the coordinates. That account contributes no slot by itself. A local summary contributes a slot only when its one aspect and Scale are defined under C.2.6:15.1 and A.18/A.19; changing that basis requires an explicit chart change.

#### C.2.2a:4.4 - Position, grounds and publication
Keep the positioned episteme publication separate from the grounds for its assessment and from its publication form and carrier:

- **positioned episteme publication** - the governed `U.Episteme` publication whose current position is being claimed;
- **grounds / witnesses** - disturbances, discrepancies, traces, model outputs, bodily tensions, exemplars, or contrasts that justify the current reading;
- **publication forms** - arrangements or notations used for publications such as cue packs, prompts, typed projections, partial normal forms and endpoint records; an MVPK face is a selected publication form, identified when that distinction matters;
- **carriers** - physical or digital media, such as a paper sheet, file or console display, that bear the selected form.

C.2.2a governs the coordinate reading of the position claim. Keep that claim distinct from its grounds, publication form and carrier. C.2.6 also distinguishes a reading's derivation from evidence for its target claim and from the conditions under which someone uses it.

#### C.2.2a:4.5 - Position publication rule

A published position states the exact episteme publication, the facet readings that matter to the present use, and the grounds for those readings. A decision-relevant unknown is stated as `unknown`; unrelated facets need not be filled merely to complete a form.

Add the local threshold and named next action only when the row is used for movement, routing, comparison, or endpoint entry. If that action also requires a source, evidence or interaction condition, state or cite its predicate beside the coordinate test; the condition does not become a Coordinate by being included in the same row. Add publication form, MVPK face, carrier, or SCR/RSCR lane only when that distinction affects interpretation, preservation, distribution, or the next action.

The position is reviewable when the named or inherited episteme publication, relevant readings, grounds, and any relied-on threshold are recoverable, and when any form, face, or carrier actually mentioned remains distinct from the positioned episteme publication. A polished note or better carrier does not by itself prove a new chart position.

#### C.2.2a:4.6 - Non-substitution of `F`
The formality assessment supplies the selected expression Characteristics, each with its own basis slot. A justified local summary may occupy one slot; a multi-property profile does not. These readings describe only the expression properties selected under C.2.3.

A conforming account shall not infer:

- closure from formality alone;
- source or use relations from publication-face format alone;
- representation factors from articulation alone;
- or routing admissibility from a lone `F` statement.

Where operationally meaningful thresholds exist, they must be published on the relevant slots rather than being disguised as informal `F` sublevels.

#### C.2.2a:4.7 - Position versus publication form
A position claim states facet readings about the identified episteme. Witnesses provide grounds for those readings; a selected publication form, including an MVPK face, expresses the claim; a carrier bears that form. Changing the form or carrier does not by itself change a facet reading. Any later publication qualified under an endpoint subject pattern still needs that pattern's conditions.

#### C.2.2a:4.8 - Threshold publication discipline
If a threshold is used to justify a move or endpoint entry, that threshold shall be stated on explicit basis slots in the chart. Statements such as `this is now ready`, `this has matured`, or `this is still too early` are non-conformant when they substitute for undeclared slot conditions.

#### C.2.2a:4.9 - Comparison and bridge note

Positions may be compared directly only under one shared chart meaning and the applicable local comparison rule. When comparison or reuse depends on distinct local meanings, recover the two exact F.17 local senses and test the direct F.9 predicate. Cite a Bridge only when that predicate obtains. State the proposed bounded use and any reliance separately; a loss note is optional and belongs to that use, not to the fact that the contexts differ.

If no Bridge obtains, preserve both local positions. Name the actual comparison or translation relation needed by the receiving use, or return the applicable missing-governor result instead of inventing correspondence.

#### C.2.2a:4.10 - What changes after the row exists

Compare the relevant readings with the local threshold named by the next action. Use the result to decide whether to keep the publication where it is, route it through a seam or prompt pattern, open a facet or endpoint question, or stop because a required reading is unknown. The receiving pattern governs the actual route, comparison, or publication decision; the chart row supplies only the position facts that decision uses.

