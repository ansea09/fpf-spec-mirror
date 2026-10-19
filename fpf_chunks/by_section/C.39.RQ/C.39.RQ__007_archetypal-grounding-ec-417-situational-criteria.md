---
chunk_kind: "child"
pattern_id: "C.39.RQ"
pattern_title: "Construct Situated Method Requirements"
section_id: "C.39.RQ:5"
section_title: "Archetypal Grounding — EC-417 Situational Criteria"
source_path: "FPF-Spec.md"
output_path: "by_section/C.39.RQ/C.39.RQ__007_archetypal-grounding-ec-417-situational-criteria.md"
commit_sha: "9a8471b145233a83524724caa5d7eb50ee151185"
heading_path:
  - "C.39.RQ — Construct Situated Method Requirements"
  - "C.39.RQ:5 — Archetypal Grounding — EC-417 Situational Criteria"
line_start: 83232
line_end: 83277
dependencies:
  - "A.3.1"
  - "C.11"
  - "C.11.DUA"
  - "C.32.MWA.PP"
  - "C.39.MF"
keywords:
---

### C.39.RQ:5 - Archetypal Grounding — EC-417 Situational Criteria

The situation family is a safety-relevant controller change combining firmware and supplier-originated harness geometry under a fixed release calendar. The intended Work produces one released change with traceable affected requirements, implementation revisions, verification results, evidence status, and human release authority. Some cases have signed supplier evidence before integration; others have only versioned provisional evidence until later. AI support may suggest trace links but may not receive confidential geometry or decide release.

Three views describe the same release Work. The project view exposes dates, allocations, and authority; the process view exposes recurring supplier-evidence, integration, verification, and release-result correspondences; the case view exposes how new evidence changes the next decision for one release. These views help find criteria. They create neither additional Work nor a Method.

Required Method contributions are stated without selecting an architecture: produce the affected hardware verification result; integrate the implementation against an explicitly versioned evidence state; produce signed supplier approval or an explicit missing-approval stop; and return release, withhold, or next-slot authorization under named human authority. Evidence reconciliation and trace review are additional candidate contributions, not pre-admitted Methods.

The alternative labels refer to [the timing and capacity comparison in C.32.MWA.PP §5.3](https://github.com/ailev/FPF/blob/main/FPF-Spec.md#c32mwapp53---possible-future-alternatives-a-b-and-b2). In A, the team waits for signed supplier evidence before integrating the software. In B2, it integrates from a versioned provisional edition and reconciles it with signed evidence before safety closure. Most preparation of the changes between those editions goes to the supplier-configuration role, keeping the safety engineer within the peak limit. A is a choice before integration; recovery R applies when closure fails after B2 integration.

The case admits three human Systems and keeps their decision Work, assignments, permissions, authority, and results explicit:

| Admitted human System | Performed decision Work and result | Covering Work assignment | Independently obtaining permission or direct decision-authority relation |
| --- | --- | --- | --- |
| `TraceReviewer-17` | named `W-TraceAcceptReject-17` occurrences issue one accept/reject result for each AI trace suggestion | `ASG-TraceReview-17` covers that Work for EC-417 from `D-21` through `D0` | `PERM-TraceAcceptReject-17` permits subject `TraceReviewer-17` to accept or reject EC-417 AI trace suggestions in that window, on the basis of `TraceReviewCharter-17`; reliance requires a current matching entry in `DecisionRightsRegister-17` and the linked human-decision record |
| `SafetyReviewer-17` | `W-SafetyEvidenceDecision-17` issues accept/reject of the evidence conditions for B2 entry, safety closure, or recovery | `ASG-SafetyReview-17` covers that Work from `D-21` through the next authorized slot | `AUTH-SafetyEvidence-17` is the direct decision-authority relation for subject `SafetyReviewer-17`, that evidence-decision scope, and that window, on the basis of `SafetyDecisionCharter-17`; reliance requires a current matching `DecisionRightsRegister-17` entry and linked safety-decision record |
| `ReleaseDecider-17` | `W-ReleaseDecision-17` issues the branch-entry and release, withhold, or next-slot decision results | `ASG-ReleaseDecision-17` covers that Work from the `D-21` checkpoint through the next authorized slot | `AUTH-ReleaseDecision-17` is the direct decision-authority relation for subject `ReleaseDecider-17`, selection of `A` or authorization of at most three `B2` trials and the named release disposition, and that window, on the basis of `ReleaseDecisionCharter-17`; reliance requires a current matching `DecisionRightsRegister-17` entry and linked release-decision record |

Assignments, permission relations, and authority relations each need their own basis. Each performed Work occurrence and decision result also needs its own record; none is established by an assignment, permission, or authority relation alone. Responsibility, access, capability, assignment, permission, authority, performed Work, and decision result therefore remain separately testable. The AI provider is a separate System and is holder or subject of none of these assignments or relations.

| Criterion | Actual subject and decision level | Requirement, variation, and bound | Evidence needed and truthful stop |
| --- | --- | --- | --- |
| `SC-TRACE-01` | EC-417 receiving result and its requirement/implementation/verification correspondence | every affected safety requirement links to one or more named current implementation revisions and one or more named verification results; every correspondence link remains inspectable, while representation format may vary | versioned trace record; an affected requirement with no current implementation-revision link or no verification-result link is `failed` and stops safety closure |
| `SC-CONF-01` | supplier-geometry information and AI-provider access relation | confidential supplier geometry stays outside the AI provider; using no AI is allowable | access configuration and handling record; any provider exposure is `failed` and stops the AI-supported route |
| `SC-ASSIGN-01` | the three admitted human Systems, their decision Work, and `ASG-TraceReview-17`, `ASG-SafetyReview-17`, and `ASG-ReleaseDecision-17` | every performed decision-Work occurrence has a named System that matches the holder, Work scope, and window of its covering assignment | assignment and Work records; a missing assignment, holder mismatch, uncovered Work, or out-of-window occurrence is `failed` without erasing the Work occurrence |
| `SC-AUTH-01` | `PERM-TraceAcceptReject-17`, `AUTH-SafetyEvidence-17`, `AUTH-ReleaseDecision-17`, and the governed decision results | every AI suggestion receives `TraceReviewer-17` accept/reject within the permission scope; safety and release decisions remain within their named subjects, scopes, windows, and bases; the AI provider has no release authority | current matching `DecisionRightsRegister-17` entries plus linked human, safety, and release decision records; missing permission or authority, an unnamed result, an out-of-scope decision, or authority delegated to the AI provider is `failed` |
| `SC-EVID-01` | provisional and signed hardware-evidence inputs, their relation, and the safety-closure guard | provisional evidence may be used before closure only with explicit edition and uncertainty; signed evidence supersedes it for safety-closure reliance, while the provisional edition, uncertainty, earlier Work use, and relation to the later signed evidence remain traceable | version/uncertainty fields, earlier-use record, signed supplier evidence, and inspectable provisional-to-signed relation; missing signed evidence at closure stops release |
| `SC-REV-01` | integration Work and the implementation state | rollback remains possible within one hour until `D-1`; the project may choose a signed-first or provisional-first branch before entry | replayable rollback demonstration for the current toolchain; inability to restore within one hour is `failed` for an early-integration route |
| `SC-CAP-01` | hardware-verification and safety-evidence capabilities of the named performers | hardware verification and safety evidence judgment require current capability for the named controller, rig, and safety scope; capability grants neither assignment, permission, nor release authority | current capability evidence for each named performer; the separate assignment, permission, and decision-authority conditions must also hold, and missing capability stops the contribution that needs it |
| `SC-TECH-01` | PLM/CI support, pinout schema, test-rig access, and their relations to Work | the evidence version used by integration remains recoverable; required verification has a named rig/access route; equivalent tools are allowed when they preserve the same result and evidence conditions | configuration, schema-edition, and access records; an unknown input edition or unavailable verification route is `unknown` and blocks reliance |
| `SC-BURDEN-01` | safety-engineer allocation on the peak safety day | safety demand stays at or below `0.40` of an eight-hour day (`3.20 h`); burden shifted to another performer remains visible rather than disappearing | allocation and time estimate for the selected day; demand above `0.40` is `failed` for the proposed structure, not proof that any one Method is unfit |
| `SC-BOARD-01` | each joint-board Work occurrence | each board lasts at most 45 minutes; one or two boards are allowable when the evidence and burden criteria remain satisfied | calendar and actual-duration record; a planned board above 45 minutes fails the coordination-burden criterion |
| `SC-STOP-01` | `W-ReleaseDecision-17`, its covering assignment, `AUTH-ReleaseDecision-17`, and the receiving result | no release occurs without signed evidence, required verification, a covering assignment, and the direct release-decision authority relation; delay to a later authorized slot is allowable | release record citing evidence, assignment, authority relation, and decision result; any missing non-negotiable yields withhold or next-slot, not silent waiver |

The criteria leave serious alternatives open. A signed-first alternative may wait for supplier evidence; a provisional-first alternative may integrate earlier and reconcile later; preparation may sit with the safety engineer or with the supplier-configuration role. C.39.RQ does not choose among them. A later individual qualification may apply contribution, capability, access, and evidence criteria to each identified Method or candidate account. A later architecture comparison must inspect combined peak demand, timing, covering assignments, permission and decision-authority relations, provider access, and burden transfer. Passing one row or staying below `0.40` does not establish fit of the whole proposed structure.

The criteria set is adequate for its next use when every non-negotiable row has an observable test, the remaining variations are explicit, and unknowns are routed to their actual subject. It stops the current route immediately on missing signed evidence at closure, confidential geometry exposure, a missing or mismatched covering assignment, permission, or direct decision-authority relation, unavailable required capability or verification route, rollback beyond one hour for an early-integration proposal, peak safety demand above `0.40`, or a joint board above 45 minutes. Reopen when the change class, supplier information boundary, evidence timing, toolchain, performer assignment, release authority, capacity window, or receiving-result acceptance rule changes.

#### C.39.RQ:5.1 - Retain Approval and Question a Duplicate Trace Record

Consider two disputed requirements in the same release situation. The supplier's signed approval establishes which pinout the supplier endorses; the provisional file alone leaves a material possibility of implementing an unendorsed connection. That protective contribution supports retaining the approval condition for release. A cheaper trace procedure does not supply the missing supplier decision, and the present release authority still withholds release when the required approval is absent.

The other requirement is a second manual copy of every trace link. In this constructed case, the versioned authoritative trace already exposes the same links and failed correspondences to the review, and the duplicate copy adds no check or independent information. Producing it consumes time needed to inspect a changed safety requirement. On those supplied facts, the criteria author can finish with a recommendation to remove the duplicate-copy obligation while preserving the trace and review that detect the actual defect. A different case in which the second check detects a consequential omission can support retention.

The recommendation names the governing trace-record rule and the authority needed to amend it. It does not treat the release decider's authority as authority to change that rule. If timely amendment is unavailable, the current rule remains in force and the release arrangement must use a permissible continuation or a later slot. The present recommendation and its limit are complete; a new experiment is selected only if an obtainable result could change the appraisal enough to warrant its full burden.

