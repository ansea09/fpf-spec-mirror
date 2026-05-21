---
chunk_kind: "child"
pattern_id: "E.17.AUD.OOTD"
pattern_title: "PublicationUnit Stability Discipline and PublicationUnit Primary Described-Entity Discipline - publication-unit stability over one primary described entity"
section_id: "E.17.AUD.OOTD:4"
section_title: "Solution - stabilize one publication unit, one described entity, one move, and one outside-work boundary"
source_path: "FPF-Spec.md"
output_path: "by_section/E.17.AUD.OOTD/E.17.AUD.OOTD__005_solution-stabilize-one-publication-unit-one-described-entity-one-move-and-one-outside-work-boundary.md"
commit_sha: "eb2832093c1e482d5fdd4985c3d2011ab240b429"
heading_path:
  - "E.17.AUD.OOTD — PublicationUnit Stability Discipline and PublicationUnit Primary Described-Entity Discipline - publication-unit stability over one primary described entity"
  - "E.17.AUD.OOTD:4 — Solution - stabilize one publication unit, one described entity, one move, and one outside-work boundary"
line_start: 58415
line_end: 58521
dependencies:
  - "A.10"
  - "A.15"
  - "A.15.4"
  - "A.16.0"
  - "A.20"
  - "A.21"
  - "A.6.3"
  - "A.6.3.CR"
  - "A.6.3.RT"
  - "A.6.P"
  - "A.7"
  - "B.3"
  - "C.2.2a"
  - "E.10"
  - "E.10.SEMIO"
  - "E.14"
  - "E.17.AUD.LHR"
  - "E.17.EFP"
  - "E.17.ID.CR"
  - "E.19"
  - "F.18"
keywords:
---

### E.17.AUD.OOTD:4 - Solution - stabilize one publication unit, one described entity, one move, and one outside-work boundary

#### E.17.AUD.OOTD:4.1 - Manager-first entry

> `PublicationUnit Primary Described-Entity Discipline` keeps one publication unit explicit about what it is mainly about, what move it is carrying over that entity, and what wider work remains outside.
>
> It becomes necessary when local repair is no longer enough and the publication unit still has unstable reading across described entity, description, carrier, publication unit, process, or downstream decision use while sounding unchanged.

In plain working terms, this section is for moments like:
- `this memo is about the architecture boundary, not yet about the rollout plan`;
- `this review note is about the incident episode, not yet about the action decision`;
- `this comparison sheet is about the governed described entity under review, not yet about approval or the downstream decision`;
- `this semio note is about one pattern section or publication form, not the wider architecture policy around it`.

If that is the clarification you need, start here.
If the real problem is still only one vague local lexical head word, start with `E.17.AUD.LHR` (`Local Head Restoration`).

#### E.17.AUD.OOTD:4.1.a - Pairwise plain glosses

- **Publication unit** = one written or displayed bounded unit others are meant to read as one unit, such as a note, memo, sheet, table, or guided screen.
- **Primary described entity** = the local stabilization reading for what that unit is mainly about when it carries or exposes a claim-bearing episteme or episteme-lane `U.View`; it is not a new `C.2.1` slot. If no claim-bearing episteme or episteme-lane view is live, name the exact non-claim-bearing kind, topic, or subject instead of inventing a `DescribedEntityRef`.
- **Carried move** = what the unit is doing over that entity, or that it is only stabilizing it without adding a new move.
- **Outside-work boundary** = what wider review, execution work, unsupported downstream decision, or reliance claim stays outside the current unit.
- **Explicit transition** = the unit openly says it has moved from one reading or described entity to another instead of pretending nothing changed.

#### E.17.AUD.OOTD:4.1.b - Minimal modeling lens

Treat the governed publication unit here as one publication unit carrying one primary described-entity reading over one current working concern or lineage slice. That reading does not make the unit itself a `U.EpistemePublication`; it stabilizes the unit's reading over the already-governed item it carries or exposes.
The smallest honest lens asks five entries:
1. what publication unit is being governed;
2. what described entity is primary;
3. what move over that entity is being carried;
4. which reading is active;
5. what wider work still stays outside.

If that lens cannot stay stable after local repair, do not patch over the reading shift with a heavier declaration; reopen the unit or apply the governing pattern instead.

#### E.17.AUD.OOTD:4.2 - Scope and exclusions

**In scope**
- one publication unit with unstable reading across multiple described entities;
- one unit mixing move and outside work;
- one unit quietly shifting between described entity, description, carrier, publication unit, process, or downstream decision use;
- semio-heavy texts where repair disposition, governing pattern, governed object, carried move, and outside work must stay explicit across one publication unit.

**Out of scope**
- local lexical-head repair only;
- pure view, face, or carrier architecture work;
- same-entity transform, explanation, bridge, ontology, or comparative-reading questions whose neighboring patterns already govern the main move;
- downstream gate, approval, execution, or decision pressure.

**Ordinary stop rule.** If the ordinary six-row card plus one nearest worked slice already settle the case, stop there. Do not climb into heavier support just to prove that one unit now keeps one primary described entity, one carried move, and one outside-work boundary honestly in place.

#### E.17.AUD.OOTD:4.3 - Ordinary working card

For ordinary use, keep at least these six rows visible:

| Row | Ordinary prompt |
| --- | --- |
| 1 | What single publication unit am I asking people to read as one bounded unit? |
| 2 | What is it mainly about? |
| 3 | What move is it making over that primary described entity, or is it only stabilizing it? |
| 4 | What wider work or engineering process is outside this unit? |
| 5 | Is any transition between readings or described entities explicit? |
| 6 | If this remains unstable after local repair, which governing pattern applies? |

If those six rows can stay stable across the same publication unit, ordinary use is usually enough.
Treat that six-row card as the recognition surface.

If local repair is still enough, go back to `E.17.AUD.LHR` (`Local Head Restoration`) instead of adding more structure here.
If the unit remains one publication unit but neighboring-boundary load, misuse risk, or cross-reading ambiguity becomes load-bearing, use the heavier extension as the assurance surface.
If the same unit is already stable as one primary described entity, one carried move, and one outside-work boundary, and the remaining question is one bounded comparative review move over already available source epistemes or publications, apply `E.17.ID.CR` before thickening this publication-unit card.
If the unit cannot keep one stable primary described entity, one carried move, and one outside-work boundary even after local repair, do not solve that by stacking more fields onto the heavier extension; apply or reopen the neighboring-pattern check first.

#### E.17.AUD.OOTD:4.4 - Load-bearing extension and quick boundary summary

Use the heavier extension only when the ordinary six-row card already stays stable and the case is close to important seams.
It is for heavier declaration, not for rescuing a unit that still cannot keep one primary described entity, one carried move, and one outside-work boundary in place.

Then add:
- `publicationUnitFormCue`;
- `primaryReading`;
- `transitionPolicy`;
- `modelingLensPolicy`;
- `downstreamDecisionPolicy`.

These fields do not create a rival rule track. `publicationUnitFormCue` names words such as note, sheet, screen, and table as form clues only; it does not make those clues governed-object kinds. The fields only make the heavier neighboring-boundary load visible once the ordinary card already holds.

**Quick governing-pattern and project-side-reference boundary summary**
- use `E.17.AUD.LHR` (`Local Head Restoration`) when the instability is still local to one local lexical head, qualifier, or reading word;
- use `E.17.ID.CR` when the same publication unit already holds one stable primary described entity, one carried move, and one outside-work boundary, and the live question is one bounded comparative review move over already available source epistemes or publications;
- use this pattern when one publication unit still has unstable described-entity, carried-move, or outside-work reading after honest local repair;
- use the neighboring pattern or the exact project-side FPF kind and reference when view, face, carrier, same-entity transform, explanation, bridge, ontology, gate, approval, or execution claim becomes primary.

#### E.17.AUD.OOTD:4.5 - Boundary-rule summary

This section is the canonical governing-pattern boundary summary for `PublicationUnit Primary Described-Entity Discipline` inside the Core.
Companion notes may elaborate support checks and review scaffolding, but they may not override this section.

The practical summary is:
1. keep one primary described entity unless a transition is explicit;
2. do not collapse described entity, description, carrier, publication unit, process, and downstream decision use into one unchanged reading;
3. keep the carried move distinct from the wider work around it;
4. use local `E.17.AUD.LHR` (`Local Head Restoration`) first, and open this pattern when publication-unit reading instability remains after that;
5. apply `E.17.ID.CR` when publication-unit stability already holds and the remaining question is one bounded comparative review move over already available source epistemes or publications;
6. move out when the unit starts carrying downstream decision pressure or another neighboring pattern question.

