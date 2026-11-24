---
chunk_kind: "child"
pattern_id: "E.17.AUD.LHR"
pattern_title: "Restore the Local Meaning of an Overloaded Word or Phrase (Local Head Restoration)"
section_id: "E.17.AUD.LHR:5"
section_title: "Worked slices"
source_path: "FPF-Spec.md"
output_path: "by_section/E.17.AUD.LHR/E.17.AUD.LHR__006_worked-slices.md"
commit_sha: "cadc8eb15721be464193af85206e345f34a64b04"
heading_path:
  - "E.17.AUD.LHR — Restore the Local Meaning of an Overloaded Word or Phrase (Local Head Restoration)"
  - "E.17.AUD.LHR:5 — Worked slices"
line_start: 117529
line_end: 117648
dependencies:
  - "A.10"
  - "A.15"
  - "A.15.4"
  - "A.20"
  - "A.21"
  - "A.6.3"
  - "A.6.3.CR"
  - "A.6.3.RT"
  - "A.6.P"
  - "A.7"
  - "B.3"
  - "C.2.P"
  - "E.10"
  - "E.14"
  - "E.17.AUD"
  - "E.17.AUD.OOTD"
  - "E.17.EFP"
  - "E.17.ID.CR"
  - "F.18"
keywords:
---

### E.17.AUD.LHR:5 - Worked slices

The following cases illustrate local repair, transfer to comparison or whole-unit repair, and reopening after changed observations. They are alternative outcomes, not a recommended sequence.

**Worked-slice aid.** The cases below display the overloaded local lexical head, its kind and active reading, the primary entity or relation, the carried action, outside work and repair disposition. Use this arrangement when it helps recover the repair; an adequate repaired sentence needs no separate output schema.

#### E.17.AUD.LHR:5.1 - `review` carries two jobs

A note says:
`This review establishes the release boundary for the service.`

Two sentences later it says:
`The review should therefore assign rollout responsibility to platform.`

Local repair first:
- overloaded local lexical head = `review`;
- restored lexical-head kind = review publication unit;
- active local reading = boundary review, not responsibility assignment;
- primary entity/relation = the release boundary as made visible in this review unit;
- carried move = make one boundary visible;
- outside work = responsibility assignment.

If the request was to report the service boundary, the note can end with that boundary. If the same commission also calls for assigning responsibility, identify who can make the assignment and how the boundary bears on that choice. The authorized assignment has its own grounds. For a proposal to change the agreed scope, follow the applicable agreement. It may entrust the change to a service or require several parties to agree.

#### E.17.AUD.LHR:5.2 - A published text is mistaken for the policy it describes

A paragraph says:
`This text is the policy.`

The intended claim is that this published text describes the policy.

Local repair:
- overloaded local lexical head = `text`;
- restored lexical-head kind = publication expression;
- active local reading = this expression of a policy description;
- primary entity/relation = the described policy;
- carried move = describe the policy rather than claim authority for it;
- outside work = approval, rollout, release, gate, policy, assurance, or adjudication status.

**Repaired sentence.** `This published text describes the policy.`

This is the ordinary stay-local case. One repaired local lexical head keeps later sentences from borrowing authority from the wrong local reading without forcing publication-unit stabilization.

**Recovery reading.** Stay in `E.17.AUD.LHR`: the local lexical head now identifies the intended expression, the same local unit no longer shifts, and no neighboring reading has become primary.

#### E.17.AUD.LHR:5.3 - Semio-heavy family name does too much work

A semio note says:
`This interpretation clarifies the package.`

But the same paragraph is about one bounded comparison over one review unit, not about `InterpretationDiscipline` as a whole and not about the whole package.

Local repair:
- overloaded local lexical head = `interpretation`;
- restored lexical-head kind = bounded comparative review unit inside one episteme-publication-heavy paragraph;
- active local comparison = bounded comparison, not wider-family package explanation;
- primary entity/relation = comparative review unit;
- restored relation set = family `InterpretationDiscipline`, governing pattern `ComparativeReviewUnit`;
- move = bounded comparison;
- outside work = wider architecture strategy.

The repaired paragraph can answer a request for that comparison. If the reader asked how the whole package works, retain the comparison as a contribution and supply the connection between the compared parts and the organization of the package (C.39.GA:4).

#### E.17.AUD.LHR:5.4 - Local repair selects bounded comparison

A comparison note says:
`This review shows option A is safer than option B.`

But the unit is one comparative review note over already pinned source epistemes or publications, not a publication-unit reading-instability case and not yet a publication-unit stability case.

Local repair:
- overloaded local lexical head = `review`;
- restored lexical-head kind = comparative review unit;
- active local comparison = compare the pinned options within this review unit; the whole release process remains outside;
- primary entity/relation = the proposed safety contrast between the options described by the pinned sources;
- carried move = make one bounded contrast visible over already available source epistemes or publications;
- outside work = rollout choice or approval.

Recover the declared safety criterion and source-backed contrast through `E.17.ID.CR`. If either is missing, leave the contrast unresolved and return to its sources; the repaired head alone establishes no comparison result. Once both are recoverable, the repaired sentence can say:

`This comparison note shows how the pinned descriptions differ on the declared safety criterion; it does not by itself establish overall safety or approve rollout.`

**Recovery reading.** Finish the local repair here. Use `E.17.ID.CR` for the remaining bounded contrast over the now-stable unit.

#### E.17.AUD.LHR:5.5 - Local repair exposes publication-unit reading instability and must apply whole-unit discipline

A release note says:
`This document records the release decision for the candidate.`

After one sentence, the same unit starts talking as if it were:
- the review publication unit that compares evidence;
- the decision object;
- and the rollout work that follows if approval is recorded.

First identify what the entry actually contains. The word `document` can be replaced by `release note` on the quoted sentence alone. Its heading leaves open whether the entry gives a reviewer’s recommendation, an authorized outcome, or both. If all the reader needs is the note about the release question, the local repair can finish there.

If the entry attributes “defer until the seal test passes” to the authorized release owner and the provenance confirms that decision for this candidate, the editor can report the deferral. If the reviewer only recommended deferral, report the recommendation. An entry that contains both can identify the reasoning and the decision. If the distinction matters and the source leaves it open, state which outcome remains unknown and what would settle it.

In this example the following paragraphs still move from weighing evidence to reporting a decision and then to carrying out rollout. Mark the change of move and the boundary of the work that follows. A heading alone cannot grant rollout authority.

**Recovery reading.** Keep the restored head as the local result and stop expanding the local repair. Apply `E.17.AUD.OOTD` because the unit’s reading still shifts after that repair.

#### E.17.AUD.LHR:5.6 - Outside observation changes what the same head can support

A status note says:
`This note captures the current rollback state for the candidate.`

Mid-review, a new vendor bulletin changes the reported failure boundary and pushes the surrounding conversation toward approval pressure.

Local repair can still clarify the current sentence:
- overloaded local lexical head = `note`;
- restored lexical-head kind = review publication unit;
- active local reading = current review publication unit, not downstream approval record;
- carried move = capture the rollback state visible on the current evidence slice;
- outside work = any new approval, adjudication, or widened authority step.

The new bulletin can change the answer to the same question about the current rollback state. Keep the restored meaning of `note` and update the finding if the evidence warrants it. When the question concerns the earlier snapshot, the earlier finding may still answer it.

**Recovery reading.** Establish which state and date the reader needs. Open a new approval or a wider review question when the commission or an applicable rule calls for that work. The change in evidence by itself grants no authority to approve.

