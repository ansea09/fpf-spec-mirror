---
chunk_kind: "child"
pattern_id: "A.2.9"
pattern_title: "U.SpeechAct (Communicative Work Object)"
section_id: "A.2.9:5"
section_title: "Archetypal Grounding (Tell–Show–Show)"
source_path: "FPF-Spec.md"
output_path: "by_section/A.2.9/A.2.9__008_archetypal-grounding-tell-show-show.md"
commit_sha: "0990ff1d1ccee4587b8f7e16e7a725a8edbe66b4"
heading_path:
  - "A.2.9 — U.SpeechAct (Communicative Work Object)"
  - "A.2.9:5 — Archetypal Grounding (Tell–Show–Show)"
line_start: 6227
line_end: 6291
dependencies:
  - "A.10"
  - "A.15.1"
  - "A.2"
  - "A.2.1"
  - "A.2.6"
  - "A.2.8"
  - "A.6.C"
  - "A.7"
  - "U.Work"
keywords:
  - "act≠utterance≠carrier"
  - "approval/authorization/publication/revocation"
  - "communicative work"
  - "institutes"
  - "judgement context"
  - "provenance"
  - "speech act"
  - "window/freshness"
---

### A.2.9:5 — Archetypal Grounding (Tell–Show–Show)

#### A.2.9:5.1 — Tell (universal rule)

When governance or gating depends on “someone said/did X”, model **that saying/doing** as a `U.SpeechAct` (a Work occurrence), and keep the utterance text and carriers separate. If it creates obligations, recommendations-as-duty, or prohibitions, cite explicit `U.Commitment` objects; if it creates strong permission, cite an explicit `GrantedPermissionRelation@Context`. The act institutes neither effect without the exact context policy.

#### A.2.9:5.2 — Show #1 (system archetype: change-control approval gates a deployment)

**Situation (messy prose):**
“Change is approved, so the pipeline may deploy.”

**Conformant modeling sketch:**

* `U.SpeechAct SA-Approve-4711`

  * `actTypes = {SpeechActTypeRef(Approval@ChangeControl)}`
  * `performedBy = RoleAssignmentRef(CAB_Chair as ApproverRole@ChangeControl)`
  * `isExecutionOf = MethodDescriptionRef(ChangeApprovalProcedure_v3)`
  * `executedWithin = ChangeControlBoardSystem`
  * `window = [t,t]`
  * `affected = {ChangeRequestId(4711)}`
  * `utteranceRefs = {EpistemeRef(ChangeTicket#4711)}`
  * `carrierRefs = {CarrierRef(TicketSystemRecord#4711)}`
  * `institutes.permissions = {U.EntityRef(PER-Deploy-4711)}`

* `GrantedPermissionRelation@ChangeControl PER-Deploy-4711`

  * `beneficiaryRef = RoleAssignmentRef(OpsBot#DeployerRole:CD_Pipeline_v7)`
  * `permittedActionSpecificationRef = EpistemeRef(DeployChange4711WorkSpecification)`
  * `institutingSpeechActRef = SA-Approve-4711`
  * `grantorAssignmentRef = RoleAssignmentRef(CAB_Chair as ApproverRole@ChangeControl)`
  * `grantValidityPolicyRef = EpistemeRef(ChangeControlGrantPolicy_v3)`
  * `scope`, `validityWindow`, and revocation stance are explicit.

* Gate predicate `A-Gate-Deploy-4711` independently states whether deployment entry conditions hold. It may check `exists SpeechAct(type=Approval, affected includes ChangeRequestId(4711), performedBy role=ApproverRole, within 90d)`, consume the current grant occurrence, and apply other prerequisites; passing the gate neither institutes nor equals the grant.

This preserves:

* act vs text vs carrier vs enduring grant,
* explicit performer and grant beneficiary,
* time window and policy for currentness,
* explicit provenance from the grant to the instituting act, and
* the distinction between strong permission and an admissibility gate.

#### A.2.9:5.3 — Show #2 (episteme archetype: publishing a spec edition without making the spec an agent)

**Situation (anti-pattern):**
“The interface spec declares MUST/SHALL requirements.”

**Conformant modeling sketch:**

* `U.SpeechAct SA-Publish-API-v12`

  * `actTypes = {SpeechActTypeRef(Publish@APISpecContext), SpeechActTypeRef(DeclareNorms@APISpecContext)}`
  * `performedBy = RoleAssignmentRef(StandardsEditor as PublisherRole@APISpecContext)`
  * `isExecutionOf = MethodDescriptionRef(SpecReleaseProcedure_v12)`
  * `executedWithin = SpecPublicationSystem`
  * `window = [t,t]`
  * `affected = {EpistemeRef(APISpec_v12)}`
  * `utteranceRefs = {EpistemeRef(APISpec_v12)}`
  * `carrierRefs = {CarrierRef(GitTag:v12), CarrierRef(SignedReleaseArtifact:v12)}`
  * `institutes.statusClaims = {ClaimIdRef(D-StdStatus-APISpec_v12-Published)}` (if modeled)

Norms live in the **published utterance descriptions** (spec clauses as L/A/D/E-classified claims), but the **act of publication** is a speech act performed by an accountable role. This avoids “the spec promises/commits” category errors while preserving auditability.

