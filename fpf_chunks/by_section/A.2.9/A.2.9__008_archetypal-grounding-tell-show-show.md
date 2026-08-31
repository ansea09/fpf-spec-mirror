---
chunk_kind: "child"
pattern_id: "A.2.9"
pattern_title: "U.SpeechAct (Communicative Work Kind, Occurrences, and Records)"
section_id: "A.2.9:5"
section_title: "Archetypal Grounding (Tell–Show–Show)"
source_path: "FPF-Spec.md"
output_path: "by_section/A.2.9/A.2.9__008_archetypal-grounding-tell-show-show.md"
commit_sha: "0c3ef3d3921bb3176096e3e6102dd819c42f6446"
heading_path:
  - "A.2.9 — U.SpeechAct (Communicative Work Kind, Occurrences, and Records)"
  - "A.2.9:5 — Archetypal Grounding (Tell–Show–Show)"
line_start: 7538
line_end: 7622
dependencies:
  - "A.10"
  - "A.13"
  - "A.15.1"
  - "A.2"
  - "A.2.1"
  - "A.2.6"
  - "A.2.8"
  - "A.6.C"
  - "A.7"
  - "F.6"
  - "U.Method"
  - "U.SystemRoleAssignment"
  - "U.Work"
keywords:
  - "A.13-qualified actual performer"
  - "containment"
  - "enacted Method"
  - "evidence carrier"
  - "independently admitted speech-act Work"
  - "institutional target and effect"
  - "named receiving use"
  - "optional SpeechActRecord"
  - "publication relation"
  - "response versus achievement"
  - "same obtaining assignment"
  - "separate later performedUnderAssignment"
  - "smallest repair or stop"
  - "time"
  - "utterance description"
---

### A.2.9:5 — Archetypal Grounding (Tell–Show–Show)

#### A.2.9:5.1 — Tell (universal rule)

When a named receiving use is current, first state who should understand or do what, what evidence would be enough, and the smallest repair or stop. Keep the act of communicating, its wording and medium, observed response, achieved use, later effect, causal contribution, and authority or permission questions distinct.

When governance or gating depends on “someone said or did X”, first identify that saying or doing as `SA : U.SpeechAct` through the A.13-qualified performer, grounded communicative history, Method, extent, and containment required by A.15.1. Then, if the gate relies on the exact assignment under which it was performed, establish F.6 separately through the same A.13 assignment. Add a `SpeechActRecord` only to state relied-on claims about the already admitted act, and keep any MethodDescription, optional channel, utterance text, and carriers separate. If the occurrence institutes an obligation, recommendation-as-duty, or prohibition, cite a separately obtaining `U.Commitment`; if it institutes strong permission, cite a `GrantedPermissionRelation@Context`. The act institutes neither effect without an applicable policy or rule and independently satisfied conditions. The record creates neither Work nor attribution.

**Receiving-use worked slice.** An engineer sends a threshold-change note to an operator. The named use is that the operator can identify the new threshold and the next safe action; the engineer should also be able to recover the reason for the change later. The operator replies “Got it” but updates the wrong parameter. That reply is evidence of a response, not achievement of the named use. The parameter update is a later action and world change; it does not by itself show that the note caused the change. Use A.10 when the evidentiary claim needs support and C.28 before claiming causal contribution.

**Persistent observation-only record slice.** After A.13 supplies the performer basis and A.15.1 independently admits `SA-Threshold-Change-17 : U.SpeechAct`, a later review needs a durable observation that the threshold note occurred but makes no claim about the exact assignment under which it was sent. `SA-Threshold-Change-17-Record : SpeechActRecord` states the occurrence and actual-performer references, actual Method and containment references, act window, recognition taxonomy and scheme, act type, utterance-description locator, and carrier; it sets `reliancePosture = observationOnly` and omits `performedUnderAssignmentRef`. This record can preserve the observation and support receiving-use replay, but it cannot satisfy a guard, gate, or claim that depends on exact assignment-bound attribution. If that use later becomes current, establish F.6 for the already admitted act through the same obtaining A.13 assignment and add the resolving reference.

The smallest repair may be a clearer threshold sentence or a changed table, followed by evidence that addresses the named use. If the operator lacks permission to make the change, return that blocker instead of repeating the message. If a later need adds audit use, apply it to later communication or a separately named reevaluation. It does not turn “Got it” into achievement of the earlier use.


#### A.2.9:5.2 — Show #1 (system archetype: change-control approval gates a deployment)

**Situation (messy prose):**
“Change is approved, so the pipeline may deploy.”

**Conformant modeling sketch.** The first line names the actual communicative Work. The record then states claims about that occurrence; the assignment, Method, recognition classification, policy and grant must each obtain independently. Because the deployment gate relies on exact assignment-bound attribution, this attribution-bearing record must include `performedUnderAssignmentRef` and its F.6 relation must obtain for the already admitted act through the same A.13 assignment.

* Actual occurrence: `SA-Approve-4711 : U.SpeechAct`.
* Performer and assignment: `ApproverSystemRole` is an exact local agential system-role kind whose criterion for this use is the capacity to issue the policy-recognized approval act under the board procedure; `CAB_Chair_A` is classified under it for this scope and window, and evidence supports that core classification without a Grade or autonomy-profile claim. `ChangeControlApproverAssignment` is a declared `U.SystemRoleAssignment` species. Under A.2.1 it declares the ordered holder and assigned-kind positions, their domains `U.System` and `ChangeControlApproverSystemRoleKindDomain`, its direct predicate and applicability, and its occurrence-identity rule. Occurrence `CAB_Chair_A_ApproverAssignment_2026` obtains with admitted System `CAB_Chair_A` as holder, `ApproverSystemRole` as assigned-kind value, and an extent covering the act; it is the same assignment used by A.13 and F.6. `CAB_Chair_A` performs `SA-Approve-4711` under that assignment. Taxonomy `ChangeControlSystemRoles_v3` and `ChangeControlReferenceScheme_2026` interpret the assertion rather than becoming assignment participants. The assignment grounds attribution; it does not act or confer authority by form.
* Actual Method and containing-system relations: `enactsMethod(SA-Approve-4711, ChangeApprovalMethod_v3)` independently obtains, with `ChangeApprovalMethod_v3 : U.Method`. `ChangeControlWorkBoundaryRelations` declares `ApprovalWorkOccursWithinBoardBoundary(work, system)` for the board-system delimitation and act window; occurrence `ApprovalWorkWithinBoardBoundary-4711` obtains for `SA-Approve-4711` and `ChangeControlBoardSystem`.
* `SA-Approve-4711-Record : SpeechActRecord` states:
  * `speechActOccurrenceRef = SpeechActRef(SA-Approve-4711)`;
  * `actualPerformerSystemRef = U.EntityRef(CAB_Chair_A)`;
  * `performedUnderAssignmentRef = U.RelationRef(PerformedUnderApprovalAssignment-4711)`, resolving to the F.6 relation between `SA-Approve-4711` and `CAB_Chair_A_ApproverAssignment_2026`;
  * `enactsMethodRef = U.EntityRef(ChangeApprovalMethod_v3)`;
  * `methodDescriptionRef = EpistemeRef(ChangeApprovalProcedure_v3)`, a separate C.2.1 episteme used here to identify and constrain the Method;
  * `recognitionTaxonomyRef = EpistemeRef(ChangeControlSpeechActTaxonomy_v3)`;
  * `effectiveReferenceScheme = ChangeControlReferenceScheme_2026`;
  * `policyOrProcedureRef = EpistemeRef(ChangeControlApprovalPolicy_v3)`, current for this approval and grant use;
  * `channelRef = U.EntityRef(CAB_TicketChannel)`;
  * `actTypes = {SpeechActTypeRef(Approval)}` under that taxonomy and scheme;
  * `reliancePosture = relianceReady`, `workContainmentRelationRefs = {U.RelationRef(ApprovalWorkWithinBoardBoundary-4711)}`, and `window = [2026-06-12T10:03Z, 2026-06-12T10:04Z]`;
  * `utteranceSubjectRefs = {ChangeRequestId(4711)}`;
  * `institutionalTargetRefs = {GrantedPermissionRelationRef@Context(PER-Deploy-4711)}`;
  * `utteranceDescriptionLocators = {U.EpistemeRef(ChangeTicket#4711)}` and `carrierRefs = {CarrierRef(TicketSystemRecord#4711)}`;
  * `institutes.permissions = {GrantedPermissionRelationRef@Context(PER-Deploy-4711)}`.

`PER-Deploy-4711 : GrantedPermissionRelation@Context` obtains separately under A.2.8.PER:

* `beneficiarySystemRoleAssignmentRef = U.RelationRef(OpsBotDeployerAssignment-CD_Pipeline_v7)`, resolving to the assignment occurrence and its declared `U.SystemRoleAssignment` species;
* `permittedActionSpecificationRef = EpistemeRef(DeployChange4711WorkSpecification)`;
* `institutingSpeechActRef = SA-Approve-4711`;
* `grantorSystemRoleAssignmentRef = U.RelationRef(CAB_Chair_A_ApproverAssignment_2026)`;
* `grantValidityPolicyRef = EpistemeRef(ChangeControlGrantPolicy_v3)` under `ChangeControlReferenceScheme_2026`; the separately cited `ChangeControlApprovalPolicy_v3` supplies the act-to-grant instituting rule;
* scope, revocation stance, and validity interval `[2026-06-12T10:04Z, 2026-06-19T10:04Z]` are explicit.

The one-minute speech-act interval and seven-day grant interval are different facts even though the latter begins when the former ends.


The utterance is about `ChangeRequestId(4711)`; its policy-selected target and demonstrated effect are the separately obtaining grant. Nothing here claims that the change-request entity itself changed. Gate predicate `A-Gate-Deploy-4711` may check `exists SpeechAct(type=Approval, utteranceSubjectRefs includes ChangeRequestId(4711), actualPerformerSystemRef=CAB_Chair_A, performedUnderAssignmentRef=PerformedUnderApprovalAssignment-4711, within 90d)`, consume the current grant, and apply other prerequisites; passing the gate neither institutes nor equals the grant. No F.9 Bridge is needed merely because a pipeline consumes the result: this case uses one exact taxonomy, scheme, and policy. A Bridge becomes current only if another receiving use actually translates or compares a different local meaning.

**Near misses.** A ticket row alone is a carrier-backed claim, not the act. `ChangeApprovalProcedure_v3` is a MethodDescription, not what the act enacts. A current approver assignment does not prove that approval Work occurred. Without the exact current policies, the occurrence remains communicative Work but establishes no grant.

This case retains kind versus occurrence versus record, utterance versus carrier, explicit performer and grant beneficiary, exact act and grant intervals, current policy bases, provenance from grant to instituting act, and strong permission versus admissibility gate as independently judgeable distinctions.

#### A.2.9:5.3 — Show #2 (episteme archetype: publishing a spec edition without making the spec an agent)

**Situation (anti-pattern):**
“The interface spec declares MUST/SHALL requirements.”

**Conformant modeling sketch.** `SA-Publish-API-v12 : U.SpeechAct` is the act. `PublisherSystemRole` is an exact local agential system-role kind whose criterion for this use is the capacity to execute the policy-recognized publication act; `StandardsEditor_A` is classified under it for this scope and window, and evidence supports that core classification without a Grade or autonomy-profile claim. `StandardsPublicationAssignment` is a declared `U.SystemRoleAssignment` species. Under A.2.1 it declares the ordered holder and assigned-kind positions, their domains `U.System` and `PublisherSystemRoleKindDomain`, its direct predicate and applicability, and its occurrence-identity rule. Occurrence `StandardsEditor_A_PublisherAssignment_v12` obtains with admitted System `StandardsEditor_A` as holder, `PublisherSystemRole` as assigned-kind value, and an extent covering the act; it is the same assignment used by A.13 and F.6. `StandardsEditor_A` performs the act under that assignment. Taxonomy `StandardsSystemRoles_v12` and `APISpecReferenceScheme_v12` interpret the assertion but are not assignment participants. The Work enacts Method `SpecPublicationMethod_v12`; `SpecReleaseProcedure_v12` is only a separate description of that Method.

`SpecPublicationWorkBoundaryRelations` declares `PublicationWorkOccursWithinSpecSystemBoundary(work, system)` for the publication-system delimitation and act window; occurrence `PublicationWorkWithinSpecSystemBoundary-v12` obtains for `SA-Publish-API-v12` and `SpecPublicationSystem`. `SA-Publish-API-v12-Record : SpeechActRecord` states:

* `speechActOccurrenceRef = SpeechActRef(SA-Publish-API-v12)`;
* `actualPerformerSystemRef = U.EntityRef(StandardsEditor_A)` and `performedUnderAssignmentRef = U.RelationRef(PerformedUnderPublisherAssignment-v12)`, resolving to the F.6 relation between the act and `StandardsEditor_A_PublisherAssignment_v12`;
* `enactsMethodRef = U.EntityRef(SpecPublicationMethod_v12)` and `methodDescriptionRef = EpistemeRef(SpecReleaseProcedure_v12)`;
* `recognitionTaxonomyRef = EpistemeRef(APISpecSpeechActTaxonomy_v12)` and `effectiveReferenceScheme = APISpecReferenceScheme_v12`;
* `policyOrProcedureRef = EpistemeRef(APISpecPublicationPolicy_v12)` and optional `channelRef = U.EntityRef(StandardsReleaseChannel)`;
* `actTypes = {SpeechActTypeRef(Publish), SpeechActTypeRef(DeclareNorms)}` under that taxonomy and scheme;
* `reliancePosture = relianceReady`, `workContainmentRelationRefs = {U.RelationRef(PublicationWorkWithinSpecSystemBoundary-v12)}`, and `window = [2026-06-14T09:00Z, 2026-06-14T09:06Z]`;
* `utteranceSubjectRefs = {EpistemeRef(APISpec_v12)}`, `institutionalTargetRefs = {EpistemeRef(APISpec_v12)}`, `utteranceDescriptionLocators = {U.EpistemeRef(APISpec_v12)}`, and `carrierRefs = {CarrierRef(GitTag:v12), CarrierRef(SignedReleaseArtifact:v12)}`;
* `institutes.publicationRelations = {EpistemePublicationRelationRef(APISpec-v12-Publication)}`.

`APISpec-v12-Publication : EpistemePublicationRelation` separately names the selected `APISpec_v12` edition, audience declaration, bounded-use declaration, publication form, exact carrier, availability interval and governing publication conditions under E.24.PUB. It obtains only while that exact edition remains available under those conditions. Its interval need not equal the six-minute publishing act. The same episteme can be both utterance subject and publication object without those relations becoming identical.

The act does not change the spec's claim content or make the episteme an actor. If `D-StdStatus-APISpec_v12-Published` is needed, keep it as a separate C.2.1 claim about the exact publication relation and cite its evidence through A.10; do not put the claim in `institutes`. Norms live in the published utterance description, while `StandardsEditor_A` performs the publishing Work. Another audience or scheme needs F.9 only when a receiving use actually translates or substitutes the local act or policy meaning.

**Bounded non-use.** If the only question is what `APISpec_v12` says, stop at A.7/C.2/E.17. If the question is whether it is available to an audience, use E.24.PUB. If the question is evidentiary support for a status claim, use A.10. Keep A.2.9 only when the actual communicative Work occurrence itself matters.

