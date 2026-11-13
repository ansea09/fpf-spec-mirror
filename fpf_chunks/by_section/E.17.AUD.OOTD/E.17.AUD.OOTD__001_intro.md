---
chunk_kind: "child"
pattern_id: "E.17.AUD.OOTD"
pattern_title: "Clarify the Primary Subject of a Publication Unit (PublicationUnit Primary-Subject Discipline)"
section_id: "E.17.AUD.OOTD:intro"
section_title: "Intro"
source_path: "FPF-Spec.md"
output_path: "by_section/E.17.AUD.OOTD/E.17.AUD.OOTD__001_intro.md"
commit_sha: "1e57ccda08ebbb9d49b7b2190bc2740b72075a13"
heading_path:
  - "E.17.AUD.OOTD — Clarify the Primary Subject of a Publication Unit (PublicationUnit Primary-Subject Discipline)"
  - "E.17.AUD.OOTD:intro — Intro"
line_start: 116577
line_end: 116615
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

## E.17.AUD.OOTD - Clarify the Primary Subject of a Publication Unit (PublicationUnit Primary-Subject Discipline)

> **Status:** Stable

**Placement.** A pattern in the `PublicationUnit Stability Discipline` for stabilizing one publication unit.

**Builds on.** `A.6.P`, `A.7`, `E.10`, `F.18`, `E.14`, `E.19`, `C.2.2a`, `A.16.0`.

**Coordinates with.** `E.17.AUD.LHR`, `E.17.ID.CR`, `E.17.EFP`, `A.6.3`, `A.6.3.CR`, `A.6.3.RT`, `A.10`, `A.2.8.PER`, `A.2.9`, `A.15`, `A.15.4`, `B.3`, `C.11`, `A.20`, `A.21`.

**Plain-name.** Keep one publication unit explicit about its primary subject.

**One-line summary.** For one bounded publication unit at a time, `PublicationUnit Primary-Subject Discipline` makes clear what the unit is mainly about, what claim or communicative move it carries, and which wider work, downstream use, decision, or reliance claim remains outside.

**Primary subject.** In this pattern, `publicationUnitPrimarySubject` means what this bounded publication unit is mainly about for the current reading. It may be a named entity, boundary, episode, question, proposal, pattern section, or another plainly named subject. This is a publication aid, not a new `U.` kind or a `C.2.1` participant by default.

**Exact C.2.1 projection.** Only when the unit carries one identified claim-bearing episteme `E`, and its primary subject is the entity that the claims of `E` concern, may the author state `publicationUnitPrimarySubject = EntityOfConcern(E)`. Otherwise do not infer an `EntityOfConcernRef` from a topic label or interpretation alone, or use a primary-subject transition as evidence that the `C.2.1` participant changed.

**Publication unit.** Here this means one bounded note, memo, sheet, review aid, screen, table, or short section that people are expected to read as one unit.

**Use this when.** A note, memo, sheet, screen, table, comparison aid, or other publication unit can sound continuous even as it shifts what it is mainly about, which question it foregrounds, what it claims or asks the reader to do, or which wider process it appears to license. Use this pattern when local word repair is no longer enough and the unit needs stable answers about its subject, the move it makes, its permitted use, and the work that remains outside.

**What goes wrong.** A publication unit changes its subject, concern, claim, communicative move, or downstream use without marking the change. Reviewers argue over sentences while the reading of the unit as a whole shifts. Readers then give it decision weight or scope it never claimed.

**Practical gain.** A team can prevent an unmarked change of reading before a memo, note, or review unit comes to stand for rollout, approval, wider architecture strategy, or another concern beyond the unit without saying so. Reviewers can identify what needs to be stabilized sooner, keep downstream work outside the unit, and decide more quickly whether its interpretation is stable enough for continued use.

**When to use another approach.** Use another approach when:
- the problem is still local lexical-head kind or qualifier repair and `E.17.AUD.LHR` (`Local Head Restoration`) is enough;
- the same publication unit is already stable enough, and the question under repair is one bounded comparative review move over already available source epistemes or publications under `E.17.ID.CR`;
- the question under repair is still same-entity rewrite, representation shift, explanation-face work, bridge-explication, or another neighboring pattern whose move is already primary;
- the question under repair is view, face, carrier, or publication architecture rather than publication-unit interpretation instability;
- the unit is already being used to approve, assign, adjudicate, or direct work and should use the downstream decision, work, or reliance publication appropriate to that use.

**Quick recovery.** If this situation fits, write the ordinary natural-language declaration in `E.17.AUD.OOTD:4.3` and compare it with the nearest worked slice in `E.17.AUD.OOTD:5.1` through `E.17.AUD.OOTD:5.6`. Use the six diagnostic prompts only if it is hard to state the declaration accurately. If one clear sentence or two short sentences settle the case, stop there. A card or further assurance is unnecessary for that ordinary result.

**What this pattern does.** `PublicationUnit Stability Discipline` names the broader family. `PublicationUnit Primary-Subject Discipline` is the local writing-and-review pattern for making one unit's primary subject, carried move, downstream-use boundary, and outside-work boundary clear together.

**Reader.** The primary reader is an engineer-manager, architect, reviewer, or programme lead who needs to stop one publication unit from changing its subject without saying so.

