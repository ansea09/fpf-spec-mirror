---
chunk_kind: "child"
pattern_id: "A.12"
pattern_title: "Acting-Side Externalization and Reflexive Split"
section_id: "A.12:5"
section_title: "Archetypal Grounding (Worked Cases)"
source_path: "FPF-Spec.md"
output_path: "by_section/A.12/A.12__007_archetypal-grounding-worked-cases.md"
commit_sha: "7ba40a95a967ca5c69afc63aeca381e6adedc8da"
heading_path:
  - "A.12 — Acting-Side Externalization and Reflexive Split"
  - "A.12:5 — Archetypal Grounding (Worked Cases)"
line_start: 23390
line_end: 23459
dependencies:
  - "A.1"
  - "A.1.1"
  - "A.10"
  - "A.14"
  - "A.15"
  - "A.15.1"
  - "A.2.1"
  - "A.2.6"
  - "A.2.7"
  - "A.3.4"
  - "A.6.RCD"
  - "A.7"
  - "B.2.5"
  - "C.13"
  - "C.2.1"
  - "E.17"
  - "E.24.PUB"
  - "F.6"
keywords:
---

### A.12:5 - Archetypal Grounding (Worked Cases)

#### A.12:5.1 - Robot Self-Calibration

Source wording: "the robot calibrates itself."

Recovered A.12 use:

```text
ReflexiveSplit@RobotInternals:
  containingHolonRef: Robot-R17
  actingPartOrSubsystemRef: CalibrationController-R17
  changedPartOrSubsystemRef: SensorSuite-R17
  holonDelimitationRelationRefs: ComponentOf(CalibrationController-R17, Robot-R17); ComponentOf(SensorSuite-R17, Robot-R17), each independently obtaining under A.14

ActingSideExternalization@RobotCalibration:
  changedSubjectRef: SensorSuite-R17, the exact continuing U.Holon identified under A.1 for this claim
  actingEntityRef: CalibrationController-R17
  actingSystemRef: CalibrationController-R17, the same entity after A.1 recognizes it under U.System
  actingRoleAssignmentRef: CalibrationAssignment-R17, one obtaining work-facing U.RoleAssignment held by CalibrationController-R17
  transformationRef: SensorCalibrationTransformation-R17, independently admitted under A.3.4 as a bounded change of SensorSuite-R17
  workOccurrenceRef: CalibrationWork-R17, performed under CalibrationAssignment-R17 through F.6
  strongerOwnerRefs: A.1 identities of SensorSuite-R17 and CalibrationController-R17; A.14 part relations; A.2.1 CalibrationAssignment-R17; F.6 performed-under-assignment relation; A.3.4 SensorCalibrationTransformation-R17; A.15.1 CalibrationWork-R17
```

The robot remains the containing holon. The two `ComponentOf` occurrences make the internal entity positions explicit. The companion acting-side frame carries the same-entity A.1 reading and names an obtaining assignment, exact Work, and independently admitted transformation through their direct owners. The fact that the change occurs inside Robot-R17 does not remove the acting side.

#### A.12:5.2 - Document Cross-Reference Update

Source wording: "the document updates its cross-references."

This case chooses the carrier-change reading rather than combining it with an episteme-edition or relation-occurrence reading. It invokes no reusable FPF carrier-identity owner. Its bounded case-local rule treats `PublicationFile-17` as the same carrier only if the file object opened for the build still exists when the build closes, every write targets that same open object, and the build neither deletes and recreates the file, atomically replaces it, nor substitutes another carrier. E.24.PUB governs what publication form that carrier bears; it does not supply this carrier identity. If a continuity fact fails, identify a replacement carrier and do not assert a transformation of one continuing file; if carrier identity is unresolved, stop. A changed C.2.1 episteme discriminator selects the separate episteme-edition reading, not carrier continuity.

```text
ActingSideExternalization@DocumentBuild:
  changedSubjectRef: PublicationFile-17, the exact continuing U.PresentationCarrier reidentified by the bounded case-local continuity rule stated above
  actingEntityRef: BuildRunner-4
  actingSystemRef: BuildRunner-4, the same entity after A.1 recognizes it under U.System
  methodRef: CrossReferenceUpdateMethod-3, admitted under A.3.1
  methodDescriptionRef: BuildScriptEpisteme-9, admitted under A.3.2 as a description of CrossReferenceUpdateMethod-3
  actingRoleAssignmentRef: CrossReferenceUpdateAssignment-27, one obtaining work-facing U.RoleAssignment held by BuildRunner-4
  transformationRef: PublicationCarrierChange-27, independently admitted under A.3.4 from the build boundary, the before/during/after carrier-state facts below, and the bounded case-local continuity rule
  workOccurrenceRef: DocumentBuildWork-27, performed under CrossReferenceUpdateAssignment-27 through F.6
  evidenceRelationRefs: BuildLogEvidenceRelation-27, one exact A.10 evidence-provenance relation supporting the DocumentBuildWork-27 occurrence claim
  strongerOwnerRefs: E.24.PUB PublicationFormBearingRelation for the before/after bearing facts; bounded case-local PublicationFile-17 continuity rule, not E.24.PUB; A.1 recognition of BuildRunner-4; A.7 carrier/episteme distinction; A.3.1 CrossReferenceUpdateMethod-3; A.3.2 BuildScriptEpisteme-9; A.2.1 CrossReferenceUpdateAssignment-27; F.6 performed-under-assignment relation; A.3.4 PublicationCarrierChange-27; A.15.1 DocumentBuildWork-27; A.10 BuildLogEvidenceRelation-27
```

Before the boundary, exact `PublicationFormBearingRelation(PublicationFile-17, CrossReferencePublicationForm-26)` obtains and the borne form contains stale form-level link addresses. During the boundary, the same open file object remains in place while its link-address state is rewritten; the build log records no replacement event. After the boundary, exact `PublicationFormBearingRelation(PublicationFile-17, CrossReferencePublicationForm-27)` obtains and the borne form contains the refreshed addresses. Those facts, the build-open/build-close boundary, and the case-local continuity rule ground `PublicationCarrierChange-27` under A.3.4. They do not decide episteme identity: if claim content, EntityOfConcern, or the effective reference scheme changed, C.2.1 identifies another episteme and any historical continuation needs a separately governed edition relation.

The document does not act. The build script is the exact MethodDescription episteme in this case, not the acting entity or the Method by form. An episteme-edition case instead identifies predecessor and successor epistemes plus their exact edition relation. A reference-relation case instead identifies one exact relation occurrence and its direct governor. Each variant receives its own account; neither is inserted as an alternative value in this frame's singular fields.

#### A.12:5.3 - Lathe And Workpiece

Source wording: "the lathe makes the workpiece, so the workpiece belongs to the lathe during manufacturing."

Recovered A.12 use:

```text
ActingSideExternalization@Machining:
  changedSubjectRef: Workpiece-8, the exact continuing U.Holon identified under A.1 for this claim
  actingEntityRef: Lathe-3
  actingSystemRef: Lathe-3, the same entity after A.1 recognizes it under U.System
  actingRoleAssignmentRef: MachiningAssignment-8, one obtaining work-facing U.RoleAssignment held by Lathe-3
  transformationRef: MachiningTransformation-8, independently admitted under A.3.4 as a bounded change of Workpiece-8
  workOccurrenceRef: MachiningWork-8, performed under MachiningAssignment-8 through F.6
  strongerOwnerRefs: A.1 identities of Workpiece-8 and Lathe-3; A.2.1 MachiningAssignment-8; F.6 performed-under-assignment relation; A.3.4 MachiningTransformation-8; A.15.1 MachiningWork-8
```

`MachiningWork-8` and `MachiningTransformation-8` are independently identified; this account asserts no work-to-change relation between them. The additional sentence needed for a positive crossing claim is: "Lathe-3 transmits cutting force to Workpiece-8 during MachiningTransformation-8." No current direct pattern in this case supplies an admitted relation kind, obtaining predicate, applicability, and occurrence-identity rule for that sentence. Result: `A.6.RCD missing-governor[receiving use: decide whether this force-transfer claim supports a boundary-crossing explanation without a parthood inference; participants: Lathe-3 and Workpiece-8; missing owner: direct force-transfer or crossing relation]`; `holonBoundaryCrossingRelationRef` stays unfilled. Fixture, control, and material-removal claims would need their own exact participants and direct owners. Neither the independently identified Work nor transformation establishes parthood; use part-whole owners only for a separately supported part-whole claim.

