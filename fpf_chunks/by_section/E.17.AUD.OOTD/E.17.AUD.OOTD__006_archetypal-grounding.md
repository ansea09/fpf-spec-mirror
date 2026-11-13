---
chunk_kind: "child"
pattern_id: "E.17.AUD.OOTD"
pattern_title: "Clarify the Primary Subject of a Publication Unit (PublicationUnit Primary-Subject Discipline)"
section_id: "E.17.AUD.OOTD:5"
section_title: "Archetypal grounding"
source_path: "FPF-Spec.md"
output_path: "by_section/E.17.AUD.OOTD/E.17.AUD.OOTD__006_archetypal-grounding.md"
commit_sha: "1e57ccda08ebbb9d49b7b2190bc2740b72075a13"
heading_path:
  - "E.17.AUD.OOTD — Clarify the Primary Subject of a Publication Unit (PublicationUnit Primary-Subject Discipline)"
  - "E.17.AUD.OOTD:5 — Archetypal grounding"
line_start: 116790
line_end: 116864
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

### E.17.AUD.OOTD:5 - Archetypal grounding

The cases below show alternative outcomes in architecture, operations, episteme publication, a return to comparison, and a changed concern. They do not prescribe a progression.

#### E.17.AUD.OOTD:5.1 - Architecture note shifting into rollout work

A short architecture memo begins with:
`This note is about the proposed service boundary between catalog and checkout.`

Three paragraphs later it says:
`We should therefore assign rollout responsibility to platform and stage migration in two sprints.`

The memo needs more than a lexical repair.
The memo's primary subject began as the service boundary, but its carried move changed from describing or assessing that boundary to proposing responsibility assignment and a two-sprint rollout; its apparent downstream use changed from understanding to planning and decision. None of those changes by itself proves that the `C.2.1` `EntityOfConcern` of an identified carried episteme changed.
Repair the memo in one of two ways:
- keep the note about the boundary and push rollout outside;
- or make the changed move and downstream use explicit and use a downstream decision or rollout publication.

**Repaired two-sentence memo.** `This memo assesses the proposed service boundary between catalog and checkout. Rollout sequencing, responsibility assignment, and approval remain outside this memo.`

**Result.** The author publishes those two sentences and stops. A rollout record opens only if rollout later becomes current work.

#### E.17.AUD.OOTD:5.2 - Operations note shifting into approval

An incident note begins as a comparative review of timing variance and operator context.
It ends as if it already recommends a production action.

The incident episode may remain the primary subject while the foregrounded concern changes and the carried move shifts from comparison to recommendation. Keep the review unit about the episode and the contrast it is surfacing; put action approval in an explicit outside-work or downstream decision text.

Use `C.11` if the new text chooses among already available actions. If an actual approving communication and an instituted permission matter, keep the `A.2.9` communicative Work and the `A.2.8.PER` grant relation separate. Use `A.21` only when a current `OperationalGate(profile)` publishes a gate decision.

#### E.17.AUD.OOTD:5.3 - Semio-heavy text mixing one local section and wider architecture strategy

A semio note starts about one selected pattern section and ends as if it had decided the packaging strategy for the whole overlay.

Here the primary subject broadens from the selected section to the whole overlay, and the carried move broadens from local interpretation to strategy. The unit should state:
- what the note is about now;
- what concern and move it carries over that subject;
- and what wider architecture strategy remains outside the current unit.

#### E.17.AUD.OOTD:5.4 - Unit stabilizes and bounded comparison becomes primary

A review note first shifts between the selected interface boundary, the move it is making over the current evidence, and the rollout implications around that boundary.
After one publication-unit repair it now says:
`This review unit is about the interface-boundary options and the contrast they make visible under the current incident evidence; rollout responsibility and approval remain outside this note.`

At that point the same unit already holds one stable primary subject, one carried comparison move, and one outside-work boundary.
`PublicationUnit Primary-Subject Discipline` has done its job.
If the remaining question is now one bounded comparison between the already pinned options over the same evidence, use `E.17.ID.CR` for that contrast. The unit needs no further stabilization for this purpose.

#### E.17.AUD.OOTD:5.5 - Outside observation changes the live concern or carried claim

A release-readiness note is already explicit that it is about one candidate publication or view and the risk state visible from the current evidence.
Mid-review, an external vendor bulletin and a new field observation change the reported failure boundary for that same candidate.

The candidate may remain the primary subject. What changed first is the evidence-facing concern and the claim the note can support; a later approval or execution question may also change the downstream use. Do not report an `EntityOfConcern` change unless one identified claim-bearing episteme has a different entity participant under `C.2.1`.
Repair the note in one of three ways:
- stop the current unit at the originally declared evidence boundary and open a new downstream record for the changed question;
- explicitly reopen the same unit with the revised concern, claim or carried move, permitted use, and outside-work boundary;
- or use the downstream decision or work pattern whose instructions now fit once approval, execution, or another downstream decision publication becomes the primary question.

The bulletin and field observation remain sources until a support, evidence, or currentness claim makes `A.10` relevant. Use `C.11` for a later choice, `A.2.9` and `A.2.8.PER` for an approving act and its permission effect, `A.15` for a work claim, and `A.21` only for an actual gate decision.

#### E.17.AUD.OOTD:5.6 - Deliberately sectioned multi-subject review packet

A release-readiness group needs one packet for one meeting. The packet contains three sections with distinct headings:

1. **Interface-boundary options** — compares two architecture alternatives.
2. **Incident evidence** — summarizes the observations that discriminate between those alternatives.
3. **Rollout constraints** — states constraints the later approval decision must respect, without assigning work or granting approval.

The local one-subject heuristic does not force three documents. The packet has one umbrella subject that fits all three sections—`the evidence and constraints needed to review the interface-boundary choice`—and one bounded use: inform the review, not approve rollout. Keeping the three section-level subjects together avoids navigation and synchronization cost, and the headings distinguish each section’s move from the others.

An unsectioned version is rejected because readers cannot see the subject and move changes. A short narrative with only one small shift may instead declare that transition. Separate documents become the least-cost choice when the rollout section starts assigning responsibility, serves another audience, needs independent reuse, or becomes an approval input with its own reliance boundary.

