---
chunk_kind: "child"
pattern_id: "E.17.AUD"
pattern_title: "Keep a Publication Unit Stable (PublicationUnit Stability Discipline)"
section_id: "E.17.AUD:5"
section_title: "Worked slices"
source_path: "FPF-Spec.md"
output_path: "by_section/E.17.AUD/E.17.AUD__006_worked-slices.md"
commit_sha: "1e57ccda08ebbb9d49b7b2190bc2740b72075a13"
heading_path:
  - "E.17.AUD — Keep a Publication Unit Stable (PublicationUnit Stability Discipline)"
  - "E.17.AUD:5 — Worked slices"
line_start: 116109
line_end: 116142
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

### E.17.AUD:5 - Worked slices

#### E.17.AUD:5.1 - Local-head case

A semio note keeps saying `this review` and `this interpretation`, but nobody can tell which FPF kind or locally declared head those lexical heads name here. Once those terms are clarified, the rest of the unit is stable. Use `Local Head Restoration`; a whole-unit repair is unnecessary.

#### E.17.AUD:5.2 - Whole-unit interpretation-shift case

A memo starts about one bounded architecture question over an inherited lineage or move, then shifts into wider rollout or approval language without declaring the transition. Repairing one sentence does not stabilize the publication unit under review because its concern and carried publication move have widened; that widening does not by itself establish a changed EntityOfConcern. Use `PublicationUnit Primary-Subject Discipline`.

#### E.17.AUD:5.3 - Stable-unit comparison case

A comparison sheet already keeps one stable primary subject and one clear outside boundary to work, work planning, decision, gate, or reliance claim, but the team is using publication-unit instability language because the comparison is contentious. Use `E.17.ID.CR ComparativeReviewUnit`. The team can address the contested comparison without further stabilization.

#### E.17.AUD:5.4 - Explanation-laundering case

An onboarding explainer starts from one stable source-pinned note, but then the simplified prose begins to sound like canonical assurance or policy. The publication unit may still be readable, yet its main problem has shifted from unit stability to explanation use. Use `E.17.EFP`'s simpler source-linked boundary sentence first; instantiate `ExplanationFaithfulnessProfile` only when explanation-class ambiguity still changes the next action.

#### E.17.AUD:5.5 - Downstream decision and reliance case

A status card starts as one bounded summary of progress, then leads readers to infer approval, assignment, or go or no-go claim or effect. The problem is no longer only publication-unit stability. Treating the card as a neutral note would miss those consequences. Use the downstream decision, gate, work, or reliance publication.

#### E.17.AUD:5.6 - Quick contrasting cases

Use this quick contrast set when the initial interpretation is unclear:

| Near-miss case | What to look for | Next pattern or project reference |
| --- | --- | --- |
| `LHR-only` | one overloaded local lexical head is doing most of the semantic work while the publication unit under review otherwise stays stable | apply `Local Head Restoration` |
| `whole-unit interpretation shift` | the publication unit under review changes its primary subject or carried publication move without marking the change | apply `PublicationUnit Primary-Subject Discipline` |
| `stable comparison -> CR` | the unit is already stable and the live problem situation is bounded comparison over pinned source publications | apply `E.17.ID.CR ComparativeReviewUnit` |
| `downstream claim or effect overread` | readers are inferring approval, assignment, or go or no-go claim or effect from the publication unit | leave the publication-unit stability family for the applicable downstream decision, gate, work, or reliance publication |
| `modeling-lens hidden` | the unit only makes sense because of one unpublished model, formal substrate, or rationale | publish that substrate or rationale briefly or use a heavier publication form or neighboring pattern |

