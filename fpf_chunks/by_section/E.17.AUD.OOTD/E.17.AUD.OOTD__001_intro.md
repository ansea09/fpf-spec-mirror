---
chunk_kind: "child"
pattern_id: "E.17.AUD.OOTD"
pattern_title: "PublicationUnit Stability Discipline and PublicationUnit Primary-Subject Discipline - publication-unit stability over one primary subject"
section_id: "E.17.AUD.OOTD:intro"
section_title: "Intro"
source_path: "FPF-Spec.md"
output_path: "by_section/E.17.AUD.OOTD/E.17.AUD.OOTD__001_intro.md"
commit_sha: "434e17ec848bb7f49e6da99dfc268effb2b5b9af"
heading_path:
  - "E.17.AUD.OOTD — PublicationUnit Stability Discipline and PublicationUnit Primary-Subject Discipline - publication-unit stability over one primary subject"
  - "E.17.AUD.OOTD:intro — Intro"
line_start: 84797
line_end: 84835
dependencies:
  - "A.10"
  - "A.15"
  - "A.15.4"
  - "A.16.0"
  - "A.2.8.PER"
  - "A.2.9"
  - "A.20"
  - "A.21"
  - "A.6.3"
  - "A.6.3.CR"
  - "A.6.3.RT"
  - "A.6.P"
  - "A.7"
  - "B.3"
  - "C.11"
  - "C.2.2a"
  - "E.10"
  - "E.14"
  - "E.17.AUD.LHR"
  - "E.17.EFP"
  - "E.17.ID.CR"
  - "E.19"
  - "F.18"
keywords:
---

## E.17.AUD.OOTD - PublicationUnit Stability Discipline and PublicationUnit Primary-Subject Discipline - publication-unit stability over one primary subject

**Placement.** Narrow publication-unit stability pattern inside the broader `PublicationUnit Stability Discipline`.

**Builds on.** `A.6.P`, `A.7`, `E.10`, `F.18`, `E.14`, `E.19`, `C.2.2a`, `A.16.0`.

**Coordinates with.** `E.17.AUD.LHR`, `E.17.ID.CR`, `E.17.EFP`, `A.6.3`, `A.6.3.CR`, `A.6.3.RT`, `A.10`, `A.2.8.PER`, `A.2.9`, `A.15`, `A.15.4`, `B.3`, `C.11`, `A.20`, `A.21`.

**Plain-name.** Keep one publication unit explicit about its primary subject.

**One-line summary.** `PublicationUnit Primary-Subject Discipline` applies to one bounded publication unit at a time and keeps that unit explicit about what it is mainly about, what claim or communicative move it carries, and what wider work, downstream use, decision, or reliance claim remains outside.

**Primary subject.** In this pattern, `publicationUnitPrimarySubject` means what this bounded publication unit is mainly about for the current reading. It may be a named entity, boundary, episode, question, proposal, pattern section, or another plainly named subject. This is a publication aid, not a new `U.` kind or a `C.2.1` participant by default.

**Exact C.2.1 projection.** Only when the unit carries one identified claim-bearing episteme `E`, and its primary subject is the exact entity that the claims of `E` concern, may the author state `publicationUnitPrimarySubject = EntityOfConcern(E)`. Otherwise do not infer an `EntityOfConcernRef`, do not treat a topic or interpretation as an entity, and do not use a primary-subject transition as evidence that the exact `C.2.1` participant changed.

**Publication unit.** Here this means one bounded note, memo, sheet, review aid, screen, table, or short section that people are expected to read as one unit.

**Use this when.** Use this pattern when one note, memo, sheet, screen, table, comparison aid, or other publication unit sounds continuous while it quietly shifts what it is mainly about, which question it foregrounds, what it claims or asks the reader to do, or which wider process it appears to license. Use it when local word repair is no longer enough and the unit needs one stable answer to: what is this unit about, what move is it making, how may it be used, and what still remains outside?

**What goes wrong if you miss this.** One publication unit starts with one subject and quietly ends with another concern, claim, communicative move, or downstream use. Review then gets trapped in sentence-level wording arguments while the real defect is publication-unit interpretation instability, and readers over-attribute decision weight or scope to a unit that never declared it.

**What this buys you in practice.** It lets a team stop publication-unit interpretation instability before one memo, note, or review unit quietly starts carrying rollout, approval, wider architecture strategy, or another wider concern by habit. In practice that means reviewers can name the real stabilization job earlier, keep downstream work outside, and decide faster whether the current unit is stable enough to keep using at all.

**Not this pattern when.** This is not the right pattern when:
- the problem is still local lexical-head kind or qualifier repair and `E.17.AUD.LHR` (`Local Head Restoration`) is enough;
- the same publication unit is already stable enough, and the question under repair is one bounded comparative review move over already available source epistemes or publications under `E.17.ID.CR`;
- the question under repair is still same-entity rewrite, representation shift, explanation-face work, bridge-explication, or another neighboring pattern whose move is already primary;
- the question under repair is view, face, carrier, or publication architecture rather than publication-unit interpretation instability;
- the unit is already being used to approve, assign, adjudicate, or direct work and should use the more honest downstream decision, work, or reliance publication.

**Quick recovery.** If this situation fits, write the ordinary natural-language declaration in `E.17.AUD.OOTD:4.3` and compare it with the nearest worked slice in `E.17.AUD.OOTD:5.1` through `E.17.AUD.OOTD:5.6`. Use the six diagnostic prompts only if the declaration is hard to make honest. If one clear sentence or two short sentences settle the case, stop there rather than creating a card or climbing into heavier assurance by habit.

**Quick boundary bank.** If this situation no longer fits, stop at the right boundary instead of opening the heavier stack by habit. One overloaded local lexical head or qualifier only -> `E.17.AUD.LHR` (`Local Head Restoration`). Same stable publication unit, but the question under repair is one bounded comparison over already pinned source epistemes or publications -> `E.17.ID.CR`. View, face, carrier, same-entity rewrite, or downstream approval, work, or reliance question -> the neighboring pattern or the more honest downstream decision publication.

**What this pattern does.** `PublicationUnit Stability Discipline` names the broader family. `PublicationUnit Primary-Subject Discipline` is the local writing-and-review pattern for making one unit's primary subject, carried move, downstream-use boundary, and outside-work boundary clear together. The moving lineage remains successive `U.Episteme` publications over `U.CharacteristicSpace`; this pattern only keeps one publication unit clear about that lineage or one move over it.

**Reader.** This pattern is written first for an engineer-manager, architect, reviewer, or programme lead who needs to stop one publication unit from quietly changing what it is about. Others may polish or review the text itself, but the opening should still read as ordinary review and writing guidance.

