---
chunk_kind: "child"
pattern_id: "E.17.AUD"
pattern_title: "PublicationUnit Stability Discipline - keep one publication unit stable enough to read honestly"
section_id: "E.17.AUD:intro"
section_title: "Intro"
source_path: "FPF-Spec.md"
output_path: "by_section/E.17.AUD/E.17.AUD__001_intro.md"
commit_sha: "308edacfa2bdb2c60d07e4e10c0deb1f260a6a31"
heading_path:
  - "E.17.AUD — PublicationUnit Stability Discipline - keep one publication unit stable enough to read honestly"
  - "E.17.AUD:intro — Intro"
line_start: 81063
line_end: 81126
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
  - "A.7"
  - "B.3"
  - "C.11"
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

## E.17.AUD - PublicationUnit Stability Discipline - keep one publication unit stable enough to read honestly

**Placement.** First publication-unit stability pattern for publication units whose active problem must be handled by one existing governing FPF pattern or by one project-side record or publication whose governing FPF pattern is named: local lexical-head repair, whole-unit primary-EntityOfConcern stabilization, bounded comparison, or a neighboring non-publication-unit pattern.

**Builds on.** `C.2.2a`, `A.16.0`, `A.7`, `E.10`, `F.18`, `E.14`, `E.19`.

**Coordinates with.** `E.17.AUD.LHR`, `E.17.AUD.OOTD`, `E.17.ID.CR`, `E.17.EFP`, `A.6.3`, `A.6.3.CR`, `A.6.3.RT`, `A.10`, `A.15`, `A.15.4`, `B.3`, `A.20`, `A.21`.

**Plain-name.** Keep one publication unit stable enough to read honestly.

**One-line summary.** `PublicationUnit Stability Discipline` is the first stability discipline for notes, memos, sheets, tables, screens, and short sections whose primary-EntityOfConcern interpretation, carried publication move, or outside boundary to work, work planning, decision, gate, or reliance claim has become unstable while the unit still looks unchanged. It helps the reader decide whether the honest next repair is local lexical-head repair, whole-unit primary-EntityOfConcern stabilization, bounded comparison over already stable source publications, or leaving the publication-unit stability family for a neighboring non-publication-unit pattern.
**Primary EntityOfConcern discipline.** Publication-unit stability uses `primary EntityOfConcern` as the plain head and assigns claim-bearing cases to `publicationUnitPrimaryEntityOfConcern` when the bounded unit exposes a `U.Episteme` or an episteme-side `U.View`. When no claim-bearing episteme or episteme-side view is live, the pattern names the non-claim-bearing kind named by value, topic, or subject without creating a false `EntityOfConcernRef`.

**Publication unit under review in plain terms.** The publication unit under review is the publication unit itself: one note, memo, sheet, table, screen, or short section that people are expected to read as one readable unit. When the unit carries or exposes a claim-bearing episteme or episteme-side `U.View`, the primary EntityOfConcern is the EntityOfConcern value of that carried item. When no claim-bearing episteme or episteme-side view is live, do not invent a `EntityOfConcernRef`; name the non-claim-bearing kind named by value, or use plain topic or subject only in non-normative explanatory prose. Keep those relations separate: this pattern keeps the unit stable as a readable unit, while the whole-unit repair pattern checks whether that unit still keeps one stable primary EntityOfConcern or subject named by value.

**Minimal lens in plain terms.** Use a four-part interpretation: one publication unit under review, one primary EntityOfConcern, one carried publication move over that primary EntityOfConcern, and one outside boundary to work, work planning, decision, gate, or reliance claim. That outside boundary usually needs one light boundary type too: neighboring pattern application, downstream claim or effect, or ongoing engineering-process continuation. If any of those interpretation relations changes quietly, the unit is no longer honest enough to read as one unchanged publication unit.

**Local working vocabulary.**
- `publication unit under review` = the note, memo, sheet, table, screen, or short section being kept honest as one unit;
- `primary EntityOfConcern` = the primary EntityOfConcern named by value of the claim-bearing episteme or episteme-side view that the unit carries or exposes when such an item is live; otherwise use non-claim-bearing kind named by value, topic, or subject without creating a `EntityOfConcernRef`;
- `carried publication move` = the publication-side claim, interpretation, comparison, or explanation move that the unit performs over that primary EntityOfConcern;
- `outside work boundary` = downstream `U.Work`, `U.WorkPlanning`, decision, gate, or reliance claim that still remains outside the unit;
- `downstream claim or effect` = an approval, assignment, go or no-go, gate, work, or reliance claim or effect that readers infer from the unit but that belongs outside this pattern unless explicitly handled by its governing pattern or by the project-side FPF kind and reference named by value that governs that claim or effect.

**A.6.P unpacking of overloaded local words.** This pattern does not use `route`, `branch`, `head`, or `unit` as hidden ontology. Use these local entries instead:
- `local lexical head` = the head word or phrase inside one claim-bearing sentence or heading, such as `review`, `interpretation`, `note`, or `text`; it is not an FPF pattern head, not a package-family head, and not a language-state alternative;
- `publication-unit repair disposition` = the current repair disposition: local lexical-head repair, whole-unit primary-EntityOfConcern stabilization, bounded comparison, explanation classification, representation change, controlled coarsening, changed primary EntityOfConcern, or downstream decision, gate, work, or reliance claim;
- `governing FPF pattern or project-side FPF kind and reference named by value` = the named FPF pattern, or a project-side evidence record, gate record, decision record, work plan, work occurrence, method, action invitation, relation record, or `U.EpistemePublication` whose governing FPF pattern is named;
- `publication-unit stability family` = the relation among `E.17.AUD`, `E.17.AUD.LHR`, `E.17.AUD.OOTD`, and neighboring comparison and explanation patterns; it is not a runtime path and not a transformation-flow structure;
- `presentation-form label` = `note`, `memo`, `sheet`, `screen`, and similar form words; these are only form clues until the publication unit under review and primary EntityOfConcern are restored.

When any of those entries carries a claim, record the active entry in the working card rather than polishing the sentence with another generic word.

**Use this when.** Use this pattern when one note, memo, sheet, screen, table, or short section is no longer trustworthy as one stable interpretation unit. Use it when people keep arguing about a paragraph, but the real question is simpler: repair one local lexical head, stabilize the whole unit, treat the unit as bounded comparison, or stop using this pattern because another FPF pattern or project publication governs the claim being made.

**First-minute working moment.** A memo starts by naming one primary EntityOfConcern, then quietly makes a different publication move over it, or quietly becomes about a different primary EntityOfConcern. One reviewer wants to repair one vague local lexical head. Another wants to rewrite the whole memo. A third person thinks the unit is already a bounded comparison or a downstream decision or reliance publication. You need one honest stabilization decision before the unit gets patched in three incompatible ways.

**What goes wrong if you miss this.** Teams keep fixing sentences without agreeing on the publication unit under review. Local lexical-head repair gets asked to carry whole-unit stabilization. Whole-unit stabilization gets asked to carry bounded comparison. Comparison gets mistaken for approval or rollout. A more polished or official-looking format gets mistaken for downstream claim or effect. The text stays readable enough to circulate, but no longer honest enough to trust.

**What this buys you in practice.** It gives one quick publication-unit stabilization decision before the draft widens or needs a neighboring governing pattern or downstream publication. Teams can decide earlier whether to stay local, stabilize the whole publication unit, apply bounded comparison, or leave the publication-unit stability family entirely for a more honest neighboring pattern or downstream publication.

**Cheap stop.** If the four-part interpretation names one publication unit under review, one primary EntityOfConcern, one carried publication move, and one outside boundary clearly enough for the current reader, stop with that stabilization decision. Do not build a dossier or open the wider assurance sections unless the unit still attracts comparison, explanation, evidence, gate, decision, work, or reliance overread.

**Not this pattern when.** This is not the right pattern when:
- one overloaded local lexical head is still the only real defect and `Local Head Restoration` is enough;
- the publication unit is already stable and the active problem situation is one bounded comparison over already pinned source publications;
- the main problem situation is explanation classification over an existing face, view, carrier, or publication discipline, or another neighboring semio pattern rather than publication-unit stability;
- the text is already being used to approve, direct, assign, or adjudicate work and should use the more honest downstream decision, gate, work, or reliance publication.

**Primary working reader.** The first working reader is an author or reviewer who needs to stop one memo, note, sheet, table, screen, or short section from quietly changing its primary EntityOfConcern, carried publication move, or downstream claim or effect. Architects, managers, and program leads are important secondary readers when they need the same governing-pattern and project-side-reference boundary signal, but they are not the first-minute reader for this opening recognition block.

**Quick kind positions.** `PublicationUnit Stability Discipline` keeps the current publication-unit problem from being repaired at the wrong level. `E.17.AUD.LHR` governs the local lexical-head repair case: one word or phrase inside the unit is carrying too much semantic work while the unit otherwise stays stable. `E.17.AUD.OOTD` governs the whole-unit stabilization case: the same publication unit no longer keeps one primary EntityOfConcern, one carried publication move, and one outside boundary to work, work planning, decision, gate, or reliance claim visible. `E.17.ID.CR` governs the bounded-comparison case once the publication unit is stable and the primary move is comparison over available source publications. Other explanation, representation, bridge, gate, approval, work, or reliance problem situations belong to their own governing FPF patterns, or to project-side records and publications whose governing FPF pattern is named. This pattern names that working distinction; it does not create a path, call chain, fixed process, or runtime control path.

**Quick recognition matrix.**

| Situation | What is really happening | Honest next interpretation |
| --- | --- | --- |
| An episteme-publication-heavy note keeps using vague lexical heads such as `review`, `interpretation`, or `interpretation` | the whole unit is mostly stable, but one overloaded local lexical head is doing too much semantic work | stay local with `Local Head Restoration` |
| An architecture or status memo starts about one bounded question, then quietly starts sounding like rollout, approval, go or no-go, or assignment publication | the publication unit now carries a quiet shift in primary EntityOfConcern or carried publication move | apply `PublicationUnit Primary EntityOfConcern Discipline` |
| A comparison sheet already keeps one stable primary EntityOfConcern and one clear boundary, but reviewers keep treating it as if it needed whole-unit rescue | the unit is stable enough; the active problem situation is bounded contrast over already available source publications | apply `E.17.ID.CR ComparativeReviewUnit` |
| An onboarding explainer, dashboard card, or review note starts to act as if cleaner prose alone licensed a policy claim, assurance claim, work claim, or reliance claim that its governing FPF pattern has not made admissible | the problem situation has left publication-unit stability and entered a neighboring explanation problem or downstream claim or effect | apply the neighboring governing pattern instead of keeping the case inside publication-unit stability |

**Recognition-block note.** The opening card above is the quick recognition block. The sections below carry the heavier assurance section: publication-unit boundary decisions, A.6.P unpacking, governing-pattern and project-side-reference boundary decisions, worked slices, and SoTA and domain grounding.

