---
chunk_kind: "child"
pattern_id: "A.2.9"
pattern_title: "U.SpeechAct (Communicative Work Kind, Occurrences, and Records)"
section_id: "A.2.9:5"
section_title: "Archetypal Grounding (Tell–Show–Show)"
source_path: "FPF-Spec.md"
output_path: "by_section/A.2.9/A.2.9__008_archetypal-grounding-tell-show-show.md"
commit_sha: "504747d26299e3963dc0457bf48d4e2a791d926a"
heading_path:
  - "A.2.9 — U.SpeechAct (Communicative Work Kind, Occurrences, and Records)"
  - "A.2.9:5 — Archetypal Grounding (Tell–Show–Show)"
line_start: 6286
line_end: 6370
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
  - "actual communicative occurrence"
  - "admitted speech-act Work kind"
  - "authority-grounding assignment"
  - "evidence carrier"
  - "institutional target and effect"
  - "optional SpeechActRecord"
  - "performing U.System"
  - "publication relation"
  - "utterance description"
---

### A.2.9:5 — Archetypal Grounding (Tell–Show–Show)

#### A.2.9:5.1 — Tell (universal rule)

When governance or gating depends on “someone said/did X”, identify **that saying/doing** as an actual Work occurrence `SA : U.SpeechAct`. Add a `SpeechActRecord` only to state relied-on claims about it, and keep the utterance text and carriers separate. If the occurrence creates obligations, recommendations-as-duty, or prohibitions, cite explicit `U.Commitment` objects; if it creates strong permission, cite an explicit `GrantedPermissionRelation@Context`. The act institutes neither effect without the exact context policy.

#### A.2.9:5.2 — Show #1 (system archetype: change-control approval gates a deployment)

**Situation (messy prose):**
“Change is approved, so the pipeline may deploy.”

**Conformant modeling sketch.** The first line names the actual Work individual. The following episteme reports claims about it; those claims must be true independently.

* Actual occurrence: `SA-Approve-4711 : U.SpeechAct`

* `SA-Approve-4711-Record : SpeechActRecord`

  * `speechActOccurrenceRef = SpeechActRef(SA-Approve-4711)`
  * `actTypes = {SpeechActTypeRef(Approval@ChangeControl)}`
  * `performedBy = U.EntityRef(CAB_Chair_A)` where `CAB_Chair_A : U.System`
  * `performedUnderAssignment = RoleAssignmentRef(CAB_Chair_A@ApproverRole@ChangeControl)`
  * `enactsMethodRef = U.EntityRef(ChangeApprovalMethod_v3)`; the actual `enactsMethod` relation independently obtains
  * `methodDescriptionRef = EpistemeRef(ChangeApprovalProcedure_v3)`
  * `reliancePosture = relianceReady`
  * `executedWithin = ChangeControlBoardSystem`
  * `window = [t,t]`
  * `judgementContextRef = ChangeControl`
  * `utteranceSubjectRefs = {ChangeRequestId(4711)}`
  * `institutionalTargetRefs = {GrantedPermissionRelationRef@ChangeControl(PER-Deploy-4711)}`
  * `utteranceRefs = {EpistemeRef(ChangeTicket#4711)}`
  * `carrierRefs = {CarrierRef(TicketSystemRecord#4711)}`
  * `institutes.permissions = {GrantedPermissionRelationRef@ChangeControl(PER-Deploy-4711)}`

* `GrantedPermissionRelation@ChangeControl PER-Deploy-4711`

  * `beneficiaryRef = RoleAssignmentRef(OpsBot#DeployerRole:CD_Pipeline_v7)`
  * `permittedActionSpecificationRef = EpistemeRef(DeployChange4711WorkSpecification)`
  * `institutingSpeechActRef = SA-Approve-4711`
  * `grantorAssignmentRef = RoleAssignmentRef(CAB_Chair_A@ApproverRole@ChangeControl)`
  * `grantValidityPolicyRef = EpistemeRef(ChangeControlGrantPolicy_v3)`
  * `scope`, `validityWindow`, and revocation stance are explicit.

The utterance is about `ChangeRequestId(4711)`; its policy-selected institutional target and demonstrated effect are the separately obtaining grant occurrence. Nothing here claims that the change-request entity itself changed.

* Gate predicate `A-Gate-Deploy-4711` independently states whether deployment entry conditions hold. It may check `exists SpeechAct(type=Approval, utteranceSubjectRefs includes ChangeRequestId(4711), performedBy=CAB_Chair_A, performedUnderAssignment role=ApproverRole, within 90d)`, consume the current grant occurrence, and apply other prerequisites; passing the gate neither institutes nor equals the grant.

This preserves:

* kind vs actual act vs record vs utterance text vs carrier vs enduring grant,
* explicit performer and grant beneficiary,
* time window and policy for currentness,
* explicit provenance from the grant to the instituting act, and
* the distinction between strong permission and an admissibility gate.

#### A.2.9:5.3 — Show #2 (episteme archetype: publishing a spec edition without making the spec an agent)

**Situation (anti-pattern):**
“The interface spec declares MUST/SHALL requirements.”

**Conformant modeling sketch.** `SA-Publish-API-v12` is the actual occurrence; the record is a separate episteme about it.

* Actual occurrence: `SA-Publish-API-v12 : U.SpeechAct`

* `SA-Publish-API-v12-Record : SpeechActRecord`

  * `speechActOccurrenceRef = SpeechActRef(SA-Publish-API-v12)`
  * `actTypes = {SpeechActTypeRef(Publish@APISpecContext), SpeechActTypeRef(DeclareNorms@APISpecContext)}`
  * `performedBy = U.EntityRef(StandardsEditor_A)` where `StandardsEditor_A : U.System`
  * `performedUnderAssignment = RoleAssignmentRef(StandardsEditor_A@PublisherRole@APISpecContext)`
  * `enactsMethodRef = U.EntityRef(SpecPublicationMethod_v12)`; the actual `enactsMethod` relation independently obtains
  * `methodDescriptionRef = EpistemeRef(SpecReleaseProcedure_v12)`
  * `reliancePosture = relianceReady`
  * `executedWithin = SpecPublicationSystem`
  * `window = [t,t]`
  * `judgementContextRef = APISpecContext`
  * `utteranceSubjectRefs = {EpistemeRef(APISpec_v12)}`
  * `institutionalTargetRefs = {EpistemeRef(APISpec_v12)}`
  * `utteranceRefs = {EpistemeRef(APISpec_v12)}`
  * `carrierRefs = {CarrierRef(GitTag:v12), CarrierRef(SignedReleaseArtifact:v12)}`
  * `institutes.publicationRelations = {EpistemePublicationRelationRef(APISpec-v12-Publication)}`

* `APISpec-v12-Publication : EpistemePublicationRelation` separately names the selected `APISpec_v12` edition, audience declaration, bounded-use declaration, publication form, and exact carrier; it obtains only while that edition is available under E.24.PUB.

The same `APISpec_v12` episteme is both the subject of the publication utterance and the object made available by the publication relation, but those are different relations. The act does not thereby change the spec's claim content or make the episteme an actor. If `D-StdStatus-APISpec_v12-Published` is needed, keep it as a separate C.2.1 claim about the publication occurrence and cite its evidence through A.10; do not put the claim in `institutes`. Norms live in the **published utterance descriptions**, while the **act of publication** is performed by `StandardsEditor_A` under its publisher assignment.

