---
chunk_kind: "child"
pattern_id: "E.17.AUD.OOTD"
pattern_title: "PublicationUnit Stability Discipline and PublicationUnit Primary EntityOfConcern Discipline - publication-unit stability over one primary EntityOfConcern"
section_id: "E.17.AUD.OOTD:intro"
section_title: "Intro"
source_path: "FPF-Spec.md"
output_path: "by_section/E.17.AUD.OOTD/E.17.AUD.OOTD__001_intro.md"
commit_sha: "b74ecf2b633a2315086198e4aab07c2b61257c27"
heading_path:
  - "E.17.AUD.OOTD — PublicationUnit Stability Discipline and PublicationUnit Primary EntityOfConcern Discipline - publication-unit stability over one primary EntityOfConcern"
  - "E.17.AUD.OOTD:intro — Intro"
line_start: 70636
line_end: 70671
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
  - "E.14"
  - "E.17.AUD.LHR"
  - "E.17.EFP"
  - "E.17.ID.CR"
  - "E.19"
  - "F.18"
keywords:
---

## E.17.AUD.OOTD - PublicationUnit Stability Discipline and PublicationUnit Primary EntityOfConcern Discipline - publication-unit stability over one primary EntityOfConcern

**Placement.** Narrow publication-unit stability pattern inside the broader `PublicationUnit Stability Discipline`.

**Builds on.** `A.6.P`, `A.7`, `E.10`, `F.18`, `E.14`, `E.19`, `C.2.2a`, `A.16.0`.

**Coordinates with.** `E.17.AUD.LHR`, `E.17.ID.CR`, `E.17.EFP`, `A.6.3`, `A.6.3.CR`, `A.6.3.RT`, `A.10`, `A.15`, `A.15.4`, `B.3`, `A.20`, `A.21`.

**Plain-name.** Keep one publication unit about one primary EntityOfConcern at a time.

**One-line summary.** `PublicationUnit Primary EntityOfConcern Discipline` governs one bounded publication unit at a time and keeps that unit explicit about what it is mainly about, what move it is carrying over that entity, and what wider work, non-admissible downstream decision, or reliance claim remains outside.
**Primary EntityOfConcern discipline.** The live technical field is `publicationUnitPrimaryEntityOfConcern`: the primary EntityOfConcern, non-claim-bearing kind named by value, topic, or subject that this bounded publication unit is mainly about for the current use. When no claim-bearing episteme or episteme-lane view is live, the pattern names the non-claim-bearing kind named by value, topic, or subject without creating a false `EntityOfConcernRef`.

**Publication unit under review in plain terms.** The publication unit under review is one bounded publication unit that other people are meant to read as one unit: a note, memo, sheet, review aid, screen, table, or short section. The carried publication move is to keep that unit explicit about one `publicationUnitPrimaryEntityOfConcern`, one carried move over that entity, and one outside-work boundary.

**Use this when.** Use this pattern when one note, memo, sheet, screen, table, comparison aid, or other publication unit starts being interpreted as if it is still about one primary EntityOfConcern while it is quietly shifting into a different primary EntityOfConcern, a different concern, or a wider process. Use it when local word repair is not enough anymore and the publication unit needs one stable answer to: what is this unit about, what move is it making, and what still remains outside?

**What goes wrong if you miss this.** One publication unit starts by talking about one primary EntityOfConcern and quietly ends by licensing a different interpretation, a different concern, or wider work. Review then gets trapped in sentence-level wording arguments while the real defect is publication-unit interpretation instability, and readers over-attribute decision weight or scope to a unit that never declared it.

**What this buys you in practice.** It lets a team stop publication-unit interpretation instability before one memo, note, or review unit quietly starts carrying rollout, approval, wider architecture strategy, or another wider concern by habit. In practice that means reviewers can name the real stabilization job earlier, keep downstream work outside, and decide faster whether the current unit is stable enough to keep using at all.

**Not this pattern when.** This is not the right pattern when:
- the problem is still local lexical-head kind or qualifier repair and `E.17.AUD.LHR` (`Local Head Restoration`) is enough;
- the same publication unit is already stable enough, and the question under repair is one bounded comparative review move over already available source epistemes or publications under `E.17.ID.CR`;
- the question under repair is still same-entity rewrite, representation shift, explanation-face work, bridge-explication, or another neighboring pattern whose move is already primary;
- the question under repair is view, face, carrier, or publication architecture rather than publication-unit interpretation instability;
- the unit is already being used to approve, assign, adjudicate, or direct work and should use the more honest downstream decision, work, or reliance publication.

**Quick recovery entry.** If the recognition block fits, recover the working question through the ordinary six-row card in `E.17.AUD.OOTD:4.3` and the nearest worked slices in `E.17.AUD.OOTD:5.1` through `E.17.AUD.OOTD:5.5`. If that ordinary card plus one nearest worked slice already settles the case, stop there rather than climbing into the heavier assurance sections by habit.

**Quick boundary bank.** If the recognition block no longer fits, stop at the right boundary instead of opening the heavier stack by habit. One overloaded local lexical head or qualifier only -> `E.17.AUD.LHR` (`Local Head Restoration`). Same stable publication unit, but the question under repair is one bounded comparison over already pinned source epistemes or publications -> `E.17.ID.CR`. View, face, carrier, same-entity rewrite, or downstream approval, work, or reliance question -> the neighboring pattern or the more honest downstream decision publication.

**Quick kind-plus-lens interpretation.** `PublicationUnit Stability Discipline` names the broader publication-unit discipline family. `PublicationUnit Primary EntityOfConcern Discipline` names the publication-unit stability pattern used when one publication unit needs its primary EntityOfConcern, carried move, and outside-work boundary made explicit together. The inherited moving lineage still remains successive `U.Episteme` publications over `U.CharacteristicSpace`; this pattern keeps explicit how one publication unit speaks about that lineage or a move over it, not a rival moving lineage.

**Primary working reader.** The first-minute reader is an engineer-manager, architect, reviewer, or programme lead who needs to stop one publication unit from quietly changing what it is about. Secondary readers may include people polishing or reviewing the text itself, but the top recognition block should still read as ordinary review and writing discipline first.

