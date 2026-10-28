---
chunk_kind: "child"
pattern_id: "E.19"
pattern_title: "Pattern Quality Gates: Review and Refresh Profiles"
section_id: "E.19:5"
section_title: "Archetypal Grounding — perform the selected review"
source_path: "FPF-Spec.md"
output_path: "by_section/E.19/E.19__007_archetypal-grounding-perform-the-selected-review.md"
commit_sha: "3f6e02840fe3a22427aed590f9688a9c8f6bf5c8"
heading_path:
  - "E.19 — Pattern Quality Gates: Review and Refresh Profiles"
  - "E.19:5 — Archetypal Grounding — perform the selected review"
line_start: 112335
line_end: 112362
dependencies:
  - "A.15.1"
  - "A.6.P"
  - "E.10"
  - "E.2.DA"
  - "E.21"
  - "E.22"
  - "E.23"
  - "E.8"
  - "E.9"
  - "E.9.DA"
  - "F.18"
  - "F.19"
keywords:
  - "(see H-8)"
  - "inside the predicate)"
  - "under E.8 H-8 and CC-SG.4"
  - "where a non-deontic Invariant: predicate is required)"
---

### E.19:5 - Archetypal Grounding — perform the selected review

The situations in section 0.2 help a reviewer recognize which questions to select. The following constructed reviews show the comparison, conclusion and return for two different kinds of defect.

#### E.19:5.1 - Review and repair a source-change instruction

E.21:5.0 supplies the complete compact pattern `EX.1@source-pin-1`. It asks the user to record a source edition, the rule used and its effect on a decision, then concludes: "Reopen the decision whenever the source publishes any new edition." The present E.19 question is a bounded refresh review of that last instruction, read with the whole quoted pattern. The relying use is to keep a decision connected to its source grounds.

The reviewer selects PCP-BASE and PCP-REFRESH. The edition-change instruction can repeatedly create work and can also determine which decisions receive attention; its semantic condition therefore needs examination. The small scope permits inspect-repair-verify within the reviewer's authority.

The reviewer compares the trigger with the reliance described earlier in the pattern. In one constructed new edition the title changes while the used rule, applicability and limitations remain the same. The instruction reopens a decision whose stated ground is unchanged. In another edition the relied-on maximum inspection interval becomes shorter, affecting the chosen interval. Here reconsideration is needed. The difference identifies the defect: publication of an edition is being used in place of a material change to the decision's basis.

The reviewer replaces the last instruction with:

> When a source changes, compare the used rule, its applicability and its stated limitations. Reopen the relying decision where that comparison changes its grounds. Retain decisions whose grounds remain applicable. If the used rule or edition cannot be recovered, apply the existing stop-and-retrieve instruction before relying on it.

Focused verification applies the two changes to the revised instruction. The title change now calls for preserving the recovery route while retaining the decision. The shortened interval sends the affected decision back for reconsideration. The source-identity and stop-and-retrieve contributions remain intact. The review can close this bounded refresh question with the repaired instruction and that comparison. E.21's evaluation of the deliberately defective quoted edition remains an evaluation of its original text.

#### E.19:5.2 - Keep a pattern-quality conclusion within its authority

A different candidate adds this claim to its otherwise developed review guidance: "An admitted deployment pattern authorizes the team to deploy the system." The requested review concerns this new authority claim; the preceding account already explains the Method and its conditions.

PCP-BASE identifies a change from the quality of guidance to permission for a particular operation. PCP-NORM is selected because the new sentence asserts authority. The reviewer locates no project decision or authorization relation in the candidate's grounds: the supplied conclusion concerns the pattern edition. The claim therefore lacks the contribution that would permit the asserted deployment.

Under independent findings, the reviewer leaves the candidate unchanged and returns the exact repair: state that the admitted pattern supplies guidance for the deployment work, and identify the project's governing authorization before claiming permission to perform that work. The author replaces the sentence with: "Use the admitted pattern as guidance for preparing deployment. The project's responsible authority decides whether this deployment may proceed under its governing conditions." Focused rereading preserves the useful Method guidance and separates the permission decision and its needed basis.

This defect requires a different comparison from section 5.1. There the relation from source change to decision grounds selected the refresh; here the subject and authority of the returned conclusion select its permissible use. Both reviews choose their depth from an actual claim, carry out the selected comparison and complete a repair or findings return. Their reasoning is available for analogous questions under the applicable profiles; observation of transfer by other reviewers requires those actual uses.

