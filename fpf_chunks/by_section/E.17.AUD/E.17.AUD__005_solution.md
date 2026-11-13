---
chunk_kind: "child"
pattern_id: "E.17.AUD"
pattern_title: "Keep a Publication Unit Stable (PublicationUnit Stability Discipline)"
section_id: "E.17.AUD:4"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/E.17.AUD/E.17.AUD__005_solution.md"
commit_sha: "1e57ccda08ebbb9d49b7b2190bc2740b72075a13"
heading_path:
  - "E.17.AUD — Keep a Publication Unit Stable (PublicationUnit Stability Discipline)"
  - "E.17.AUD:4 — Solution"
line_start: 115997
line_end: 116108
dependencies:
  - "A.16.0"
  - "A.7"
  - "C.2.1"
  - "C.2.2a"
  - "E.10"
  - "E.14"
  - "E.17"
  - "E.17.AUD"
  - "E.17.AUD.LHR"
  - "E.17.AUD.OOTD"
  - "E.17.EFP"
  - "E.17.ID.CR"
  - "E.19"
  - "E.21"
  - "F.18"
keywords:
---

### E.17.AUD:4 - Solution

> Name what the unit is mainly about, the publication move it carries, the claim that remains outside, and one repair choice. Apply another pattern only when that choice requires it.

#### E.17.AUD:4.0 - Plain working terms

- `publication unit under review` = one note, memo, sheet, table, screen, or short section that readers inspect as one unit;
- `primary subject` = what the unit is mainly about. `publicationUnitPrimaryEntityOfConcern` names the primary `EntityOfConcern` of the claim-bearing episteme or episteme-side view carried by the unit. When no such EntityOfConcern applies, use the non-claim-bearing kind named by value or an ordinary topic or subject without inventing an `EntityOfConcernRef`. An ordinary topic or subject value is not a claim about a C.2.1 entity participant;
- `carried publication move` = the claim, interpretation, comparison, or explanation move the unit makes about that primary subject;
- `outside boundary` = a decision, gate, `U.Work`, work planning, reliance claim, or continuing engineering work that remains outside the unit;
- `local lexical head` = one word or phrase such as `review`, `interpretation`, `note`, or `text` whose meaning is unstable inside an otherwise stable unit;
- `repair choice` = stable for current use, local-head repair, whole-unit stabilization, bounded comparison, or leave publication-unit stability for explanation classification, bridge or hypothesis work, representation change, controlled coarsening, a changed primary EntityOfConcern, or a downstream action, authority, adjudication, decision, gate, work, or reliance claim;
- `applicable pattern and project reference` = the FPF pattern to apply plus, when the live claim needs it, the exact evidence, gate, decision, work-plan, work-occurrence, method, action-invitation, or relation record, selected `U.Episteme`, or exact `EpistemePublicationRelation` occurrence when availability matters;
- `publication-unit stability family` = `E.17.AUD`, `E.17.AUD.LHR`, and `E.17.AUD.OOTD` together with their comparison and explanation neighbors, grouped here for selecting the applicable repair;
- `presentation-form label` = `note`, `memo`, `sheet`, `table`, `screen`, or a similar description of form. The label alone does not establish the unit’s kind.

Use the terms above only when their distinctions change the repair choice.

#### E.17.AUD:4.1 - Minimum admissible interpretation

A locally admissible interpretation keeps four entries available for inspection by value:
- one publication unit under review;
- one primary subject;
- one carried publication move over that primary subject;
- one outside boundary to work, work planning, decision, gate, or reliance claim, with one light boundary type when that distinction matters: neighboring pattern application, downstream claim or effect, or ongoing engineering-process continuation.

If the publication unit changes any of those four without saying so, its interpretation has shifted, however polished the sentences look.

#### E.17.AUD:4.2 - Publication-unit stability vs whole-unit requirement
**Ordinary result.** Choose one of the following responses.
- `stable for current use`: the four-part interpretation is explicit enough and none of the neighboring questions named above is live;
- `local lexical-head repair`: apply `E.17.AUD.LHR` to the overloaded head;
- `whole-unit stabilization`: apply `E.17.AUD.OOTD` to the unit;
- `bounded comparison`: if the unit is stable, apply `E.17.ID.CR`;
- `leave publication-unit stability`: the live question concerns work, work planning, decision, gate, evidence, explanation, reliance, carrier or front-end work, or another claim that this pattern does not test; apply the relevant pattern and name the exact project object or record.

Leave the narrower whole-unit check to `PublicationUnit Primary-Subject Discipline`. Its question is whether this unit can still keep one stable primary subject, one carried publication move, and one outside boundary to work, work planning, decision, gate, or reliance claim.

#### E.17.AUD:4.3 - Inherited dynamic frame

When the unit describes a lineage or move, use `C.2.2a` or `A.16.0` for that subject and inspect how the unit expresses it.

#### E.17.AUD:4.4 - Kind and boundary

Treat one publication unit as a readable unit. Do **not** identify it automatically with:
- the `U.Episteme` or episteme species whose claims the unit carries, quotes, or describes;
- an `EpistemePublicationRelation` occurrence, publication form, or carrier involved in making that selected episteme available;
- the primary subject, including the exact EntityOfConcern when applicable;
- a generic publication face or MVPK face under E.17 constraints;
- a carrier or evidence carrier;
- proof, evidence record, assurance claim, or release admissibility;
- a view or viewpoint;
- an engineering-process stage;
- a downstream decision, gate, work, or reliance publication.

Those objects may matter, but mentioning them in the same note, sheet, or screen does not make them the current publication-unit problem.

**Publication-unit boundary choice.** A `PublicationUnit` boundary is valid when a careful reader would naturally inspect that bounded item as carrying one primary publication move over one primary subject, with one visible outside boundary to work, work planning, decision, gate, reliance claim, or neighboring pattern application.

Choose the bounded item that carries the claim being made or effect being repaired. Do not choose a smaller boundary merely to hide a downstream overclaim, or a larger one merely to absorb several primary subjects into one unit.

A table row may be the unit when that row carries the claim; the whole table may be the unit when the table-level caption or comparison frame carries the claim. A dashboard tile, note, card, sheet, or screen block may be the unit only when that bounded item, not the whole carrier or interface, carries the live publication move.

**Publication-unit snapshot identity.** A `PublicationUnit` may remain the same bounded unit while its carrier rendering, export format, screenshot, or layout changes. It does not remain the same stabilized interpretation by visual or file continuity alone.

If a revision, refresh, translation, regeneration, or dashboard update changes the primary subject, carried publication move, outside boundary, source pins, or admissible use, rerun the four-part interpretation for the new snapshot before the unit is used for comparison, explanation, evidence, gate, decision, work, or reliance claims.

#### E.17.AUD:4.5 - Ordinary working card

When a wider repair needs these distinctions, use the seven questions to recover them:

| Row | Ordinary prompt |
| --- | --- |
| 1 | Which publication unit is under review? |
| 2 | What is that unit mainly about in this interpretation? |
| 3 | What publication move does the unit make about that subject in this interpretation? |
| 4 | What downstream `U.Work`, work planning, decision, gate, or reliance claim remains outside this unit, and is that boundary mainly a neighboring pattern application, downstream claim or effect, or ongoing engineering-process continuation? |
| 5 | Does the present problem call for repair of an overloaded local head, stabilization of the whole unit’s primary subject, bounded comparison, or another neighboring pattern? |
| 6 | Is the current form label (`note`, `sheet`, `table`, `screen`, and similar ordinary labels) naming only the presentation form, or are readers taking it to change the publication unit under review or the kind of downstream claim or effect they infer? |
| 7 | Does the current interpretation depend on a modeling substrate or rationale to identify the primary subject or carried publication move, and if so is the necessary substrate or rationale published where the reader can recover that subject or move for this unit? |

#### E.17.AUD:4.6 - Choose the next pattern

- If row 5 points to one overloaded local lexical head, apply `Local Head Restoration`.
- If row 5 shows that the whole publication unit still cannot keep one stable primary subject, one carried publication move, and one outside boundary to work, work planning, decision, gate, or reliance claim visible, apply `PublicationUnit Primary-Subject Discipline`.
- If the publication unit is stable enough and its move is bounded comparison over available source publications, apply `E.17.ID.CR ComparativeReviewUnit`.
- If the main problem is explanation classification over an existing face, apply the neighboring explanation pattern.
- If claim content, representation, coarsening, or the primary EntityOfConcern changes, apply the relevant `A.6.3` or `A.6.4` pattern before checking a later publication form here.
- If the active problem situation is publication form, bridge or hypothesis work, or a downstream claim or effect, leave the publication-unit stability family, apply the relevant pattern, and name the exact project object or record when one is needed.

#### E.17.AUD:4.7 - Local naming rule

Treat ordinary labels such as `note`, `memo`, `sheet`, `table`, `screen`, `review`, and `status` as clues to presentation form. A label alone does not establish the kind of publication unit.

Working rule:
- if one overloaded local lexical head is doing most of the semantic work, repair that local lexical head first through `Local Head Restoration`;
- if the local lexical head does not explain the instability, keep the publication unit stable in the whole-unit stabilization pattern. Adding another qualifier could hide the shift in interpretation;
- cleaner or more formal wording cannot make an inadmissible downstream claim, effect, or comparison source relation admissible.

#### E.17.AUD:4.8 - Keep a needed model or rationale visible

If the primary subject or the carried publication move depends on a modeling substrate or rationale, publish that substrate or rationale briefly in the unit or move the case to a fuller publication form or neighboring pattern that can carry it. When the interpretation depends on a formal model or rationale, wording repair alone is insufficient.

#### E.17.AUD:4.9 - Keep stronger claims separate

When explanation, comparison, or a downstream claim is load-bearing, keep five facts recoverable to preserve the repair choice:
- evidence status and source-pin status when the unit leans on already available source publications;
- which reliance or interpretation of work is currently admissible on the basis of this unit, and which decision, work or gate claims cannot be made on that basis;
- whether this unit is the primary publication unit or a derivative helper publication;
- any claim-bearing modeling substrate or rationale;
- how any assurance finding corrects or bounds the opening claim according to its result. If the revision also proposes a downstream claim or effect, distinguish that proposal from what the finding establishes.

