---
chunk_kind: "child"
pattern_id: "A.12"
pattern_title: "Acting-Side Externalization and Reflexive Split"
section_id: "A.12:5"
section_title: "Archetypal Grounding (Worked Cases)"
source_path: "FPF-Spec.md"
output_path: "by_section/A.12/A.12__007_archetypal-grounding-worked-cases.md"
commit_sha: "ef9ded2cb965193aa2484c84f06d65770439cef8"
heading_path:
  - "A.12 — Acting-Side Externalization and Reflexive Split"
  - "A.12:5 — Archetypal Grounding (Worked Cases)"
line_start: 24027
line_end: 24103
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

CalibrationController-R17 acts on SensorSuite-R17; both are parts of Robot-R17. The precise account below takes their A.1 recognition and two independently obtaining A.14 `ComponentOf` relations as premises, then distinguishes performer admission, Work, attribution and change:

```text
ReflexiveSplit@RobotInternals:
  containingHolonRef: Robot-R17
  actingPartOrSubsystemRef: CalibrationController-R17
  changedPartOrSubsystemRef: SensorSuite-R17
  holonDelimitationRelationRefs: ComponentOf(CalibrationController-R17, Robot-R17); ComponentOf(SensorSuite-R17, Robot-R17), each independently obtaining under A.14

ActingSideExternalization@RobotCalibration:
  changedSubjectRef: SensorSuite-R17, the exact continuing U.Holon identified under A.1 for this claim
  actingEntityRef: CalibrationController-R17
  actingSystemRef: CalibrationController-R17, the same entity after it satisfies the complete A.1 U.System criterion
  actingSystemA13CoreRef: A.13 core for CalibrationController-R17 as precise performer in this action, including CalibrationAssignment-R17 as the same obtaining assignment
  actingSystemRoleAssignmentRef: CalibrationAssignment-R17, one obtaining work-facing U.SystemRoleAssignment held by CalibrationController-R17
  transformationRef: SensorCalibrationTransformation-R17, independently admitted under A.3.4 as a bounded change of SensorSuite-R17
  workOccurrenceRef: CalibrationWork-R17, independently admitted under A.15.1 from its performance history, enacted Method, temporal extent, and containing-System relation; because this case claims exact assignment-bound attribution, F.6 afterward relates the already admitted Work to CalibrationAssignment-R17
  strongerOwnerRefs: A.1 identities of SensorSuite-R17 and CalibrationController-R17; A.14 part relations; A.13 performer core including A.2.1 CalibrationAssignment-R17; A.15.1 CalibrationWork-R17; F.6 performed-under-assignment relation; A.3.4 SensorCalibrationTransformation-R17
```

Robot-R17 remains the containing holon. CalibrationWork-R17 and SensorCalibrationTransformation-R17 are separate admitted objects. The A.13 core includes CalibrationAssignment-R17; after independent A.15.1 Work admission, this case’s additional F.6 attribution uses that same obtaining assignment. The references name the admissions used by the example; each admission still needs its stated basis.

#### A.12:5.2 - Document Cross-Reference Update

Source wording: "the document updates its cross-references."

BuildRunner-4 updates the cross-references in PublicationFile-17. BuildScriptEpisteme-9 describes CrossReferenceUpdateMethod-3 under A.3.2; the script is the MethodDescription, not the acting entity or the Method merely by its form. This case follows the publication carrier through the update.

The bounded case-local continuity rule treats PublicationFile-17 as the same carrier only if the file object opened for the build still exists when the build closes, every write asserted to update PublicationFile-17 targets that same open object, and the build neither deletes and recreates that file, atomically replaces it, nor substitutes another carrier. E.24.PUB states which publication form the carrier bears; it does not supply this case-local identity rule. If a continuity fact fails, identify the replacement carrier rather than asserting a transformation of one continuing file. If carrier identity is unresolved, stop before asserting that change. A changed C.2.1 episteme discriminator selects the separate episteme-edition reading.

```text
ActingSideExternalization@DocumentBuild:
  changedSubjectRef: PublicationFile-17, the exact continuing U.PresentationCarrier reidentified by the bounded case-local continuity rule stated above
  actingEntityRef: BuildRunner-4
  actingSystemRef: BuildRunner-4, the same entity after it satisfies the complete A.1 U.System criterion
  actingSystemA13CoreRef: A.13 core for BuildRunner-4 as precise performer in this action, including CrossReferenceUpdateAssignment-27 as the same obtaining assignment
  methodRef: CrossReferenceUpdateMethod-3, admitted under A.3.1
  methodDescriptionRef: BuildScriptEpisteme-9, admitted under A.3.2 as a description of CrossReferenceUpdateMethod-3
  actingSystemRoleAssignmentRef: CrossReferenceUpdateAssignment-27, one obtaining work-facing U.SystemRoleAssignment held by BuildRunner-4
  transformationRef: PublicationCarrierChange-27, independently admitted under A.3.4 from the build boundary, the before/during/after carrier-state facts below, and the bounded case-local continuity rule
  workOccurrenceRef: DocumentBuildWork-27, independently admitted under A.15.1 from its performance history, enacted CrossReferenceUpdateMethod-3, temporal extent, and containing-System relation; because this case claims exact assignment-bound attribution, F.6 afterward relates the already admitted Work to CrossReferenceUpdateAssignment-27
  evidenceRelationRefs: BuildLogEvidenceRelation-27, one exact A.10 evidence-provenance relation supporting the DocumentBuildWork-27 occurrence claim
  strongerOwnerRefs: E.24.PUB PublicationFormBearingRelation for the before/after bearing facts; bounded case-local PublicationFile-17 continuity rule, not E.24.PUB; A.1 recognition of BuildRunner-4; A.13 performer core including A.2.1 CrossReferenceUpdateAssignment-27; A.15.1 DocumentBuildWork-27; F.6 performed-under-assignment relation; A.7 carrier/episteme distinction; A.3.1 CrossReferenceUpdateMethod-3; A.3.2 BuildScriptEpisteme-9; A.3.4 PublicationCarrierChange-27; A.10 BuildLogEvidenceRelation-27
```

Before the boundary, exact `PublicationFormBearingRelation(PublicationFile-17, CrossReferencePublicationForm-26)` obtains and the borne form contains stale form-level link addresses. During the boundary, the same open file object remains in place while its link-address state is rewritten; the build log records no replacement event. After the boundary, exact `PublicationFormBearingRelation(PublicationFile-17, CrossReferencePublicationForm-27)` obtains and the borne form contains the refreshed addresses. Those facts, the build-open/build-close boundary, and the case-local continuity rule ground `PublicationCarrierChange-27` under A.3.4. They do not decide episteme identity: if claim content, EntityOfConcern, or the effective reference scheme changed, C.2.1 identifies another episteme and any historical continuation needs a separately governed edition relation.

An episteme-edition case instead identifies predecessor and successor epistemes plus their edition relation. A reference-relation case identifies one relation occurrence and its defining rule. Keep those accounts separate from the carrier-change case; they are not alternative values for its singular fields.

#### A.12:5.3 - Lathe And Workpiece

Source wording: "the lathe makes the workpiece, so the workpiece belongs to the lathe during manufacturing."

Lathe-3 is the acting participant; Workpiece-8 is the changed subject. That distinction does not establish that Workpiece-8 is part of Lathe-3. Test any such parthood claim independently under A.14 or its defining part-whole rule. The precise account separates the admitted Work and change:

```text
ActingSideExternalization@Machining:
  changedSubjectRef: Workpiece-8, the exact continuing U.Holon identified under A.1 for this claim
  actingEntityRef: Lathe-3
  actingSystemRef: Lathe-3, the same entity after it satisfies the complete A.1 U.System criterion
  actingSystemA13CoreRef: A.13 core for Lathe-3 as precise performer in this action, including MachiningAssignment-8 as the same obtaining assignment
  actingSystemRoleAssignmentRef: MachiningAssignment-8, one obtaining work-facing U.SystemRoleAssignment held by Lathe-3
  transformationRef: MachiningTransformation-8, independently admitted under A.3.4 as a bounded change of Workpiece-8
  workOccurrenceRef: MachiningWork-8, independently admitted under A.15.1 from its performance history, enacted Method, temporal extent, and containing-System relation; because this case claims exact assignment-bound attribution, F.6 afterward relates the already admitted Work to MachiningAssignment-8
  strongerOwnerRefs: A.1 identities of Workpiece-8 and Lathe-3; A.13 performer core including A.2.1 MachiningAssignment-8; A.15.1 MachiningWork-8; F.6 performed-under-assignment relation; A.3.4 MachiningTransformation-8
```

`MachiningWork-8` and `MachiningTransformation-8` are independently identified; this account asserts no Work-to-change relation between them.

The additional proposed claim is: "Lathe-3 transmits cutting force to Workpiece-8 during MachiningTransformation-8." To decide whether it supports a boundary-crossing explanation, a defining rule must supply the force-transfer or crossing relation kind, obtaining predicate, applicability and occurrence identity. This case supplies no such rule: that is its A.6.RCD `missing-governor`, and `holonBoundaryCrossingRelationRef` stays unfilled. The missing rule leaves this extension open; the acting/changed distinction remains usable and parthood still requires its own test.

