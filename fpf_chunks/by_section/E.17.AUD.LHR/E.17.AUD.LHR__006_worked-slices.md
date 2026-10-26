---
chunk_kind: "child"
pattern_id: "E.17.AUD.LHR"
pattern_title: "PublicationUnit Stability Discipline and Local Head Restoration - repair the overloaded local lexical head before the publication unit inherits it"
section_id: "E.17.AUD.LHR:5"
section_title: "Worked slices"
source_path: "FPF-Spec.md"
output_path: "by_section/E.17.AUD.LHR/E.17.AUD.LHR__006_worked-slices.md"
commit_sha: "4ce2f7202e12c5c519a3466f5e07fe0b92e78a44"
heading_path:
  - "E.17.AUD.LHR — PublicationUnit Stability Discipline and Local Head Restoration - repair the overloaded local lexical head before the publication unit inherits it"
  - "E.17.AUD.LHR:5 — Worked slices"
line_start: 107776
line_end: 107898
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

**Worked-slice mini-schema.** When a case turns episteme-publication-heavy or boundary-heavy, recover the same compact output in this order: `overloaded local lexical head | lexical-head kind | active local reading | primary entity/relation | carried action or question under repair | outside work | repair disposition`.

#### E.17.AUD.LHR:5.1 - `review` is really carrying two jobs

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

The repaired unit can now either stay with the boundary review or explicitly become a responsibility-assignment publication. Without that repair, the note quietly overclaims.

#### E.17.AUD.LHR:5.2 - `text` quietly shifts into carrier or document status

A paragraph says:
`This text is the policy.`

But what it really means is one publication form that describes the policy rather than being the policy object itself.

Local repair:
- overloaded local lexical head = `text`;
- restored lexical-head kind = publication form;
- active local reading = publication unit, not policy authority object;
- primary entity/relation = the policy description visible in this unit;
- carried move = describe the policy rather than claim authority for it;
- outside work = approval, rollout, release, gate, policy, assurance, or adjudication status.

**Repaired sentence.** `This publication form describes the policy.`

This is the ordinary stay-local case. One repaired local lexical head keeps later sentences from borrowing authority from the wrong local reading without forcing publication-unit stabilization.

**Recovery reading.** Stay in `E.17.AUD.LHR`: the local lexical head is now honest, the same local unit no longer shifts, and no neighboring reading has become primary.

#### E.17.AUD.LHR:5.3 - Semio-heavy family name does too much work

A semio note says:
`This interpretation clarifies the package.`

But the same paragraph is really about one bounded comparison over one review unit, not about `InterpretationDiscipline` as a whole and not about the whole package.

Local repair:
- overloaded local lexical head = `interpretation`;
- restored lexical-head kind = bounded comparative review unit inside one episteme-publication-heavy paragraph;
- active local comparison = bounded comparison, not wider-family package explanation;
- primary entity/relation = comparative review unit;
- restored relation set = family `InterpretationDiscipline`, governing pattern `ComparativeReviewUnit`;
- move = bounded comparison;
- outside work = wider architecture strategy.

Now the local paragraph stops pulling package-level load it never declared.

#### E.17.AUD.LHR:5.4 - Local repair selects bounded comparison

A comparison note says:
`This review shows option A is safer than option B.`

But the unit is really one comparative review note over already pinned source epistemes or publications, not a publication-unit reading-instability case and not yet a publication-unit stability case.

Local repair:
- overloaded local lexical head = `review`;
- restored lexical-head kind = comparative review unit;
- active local comparison = compare the pinned options within this review unit; the whole release process remains outside;
- primary entity/relation = the already pinned option contrast;
- carried move = make one bounded contrast visible over already available source epistemes or publications;
- outside work = rollout choice or approval.

Recover the declared safety criterion and source-backed contrast through `E.17.ID.CR`. If either is missing, leave the contrast unresolved and return to its sources; the repaired head alone establishes no comparison result. Once both are recoverable, the repaired sentence can say:

`This comparison note shows how the pinned descriptions differ on the declared safety criterion; it does not by itself establish overall safety or approve rollout.`

**Recovery reading.** This is the honest bounded-comparison disposition: finish the local repair here, then let `E.17.ID.CR` carry the remaining bounded contrast over the now-stable unit.

#### E.17.AUD.LHR:5.5 - Local repair exposes publication-unit reading instability and must apply whole-unit discipline

A release note says:
`This document records the release decision for the candidate.`

After one sentence, the same unit starts talking as if it were:
- the review publication unit that compares evidence;
- the decision object itself;
- and the rollout work that follows if approval is recorded.

Local repair can still restore the overloaded local lexical head:
- overloaded local lexical head = `document`;
- restored lexical-head kind = review publication unit;
- active local reading = publication unit, not decision object or rollout work;
- carried move = record the current release reasoning visible in this unit;
- outside work = actual approval, rollout execution, release, gate, policy, assurance, or adjudication question.

But the repaired local lexical head does not keep the same publication unit stable. The next sentences still slide between the object being decided, the move of comparing evidence, and the wider work that happens after the decision. That means local lexical-head repair has done its job and shown the remaining defect honestly: the publication unit still cannot keep one stable object, one move, and one outside-work boundary visible.

**Recovery reading.** This is the admissible publication-unit stabilization move case: stop thickening the local repair, keep the restored local lexical head as the last honest local result, and apply `E.17.AUD.OOTD` because the same unit still has unstable reading after one honest repair.

#### E.17.AUD.LHR:5.6 - Outside observation changes what the same head can honestly carry

A status note says:
`This note captures the current rollback state for the candidate.`

Mid-review, a new vendor bulletin changes the reported failure boundary and pushes the surrounding conversation toward approval pressure.

Local repair can still make the current sentence honest:
- overloaded local lexical head = `note`;
- restored lexical-head kind = review publication unit;
- active local reading = current review publication unit, not downstream approval record;
- carried move = capture the rollback state visible on the current evidence slice;
- outside work = any new approval, adjudication, or widened authority step.

But this is the stop-and-reopen case. Once outside observation changes what the same local unit can honestly stay about, do not keep appending new pressure as if the same local repair simply continued. Stop, reopen with a newly declared question, or apply the governing pattern if approval, rollout, release, gate, policy, assurance, or adjudication use, or publication-unit stabilization has become primary.

**Recovery reading.** Do not keep thickening the local card here: outside observation has changed what the same local unit can honestly carry, so the admissible repair disposition is stop-and-reopen or application of the neighboring governing pattern, not one more local qualifier.

