---
chunk_kind: "child"
pattern_id: "C.32.P2S"
pattern_title: "Problem-to-Structure Architecturing Unfolding"
section_id: "C.32.P2S:1"
section_title: "Problem frame"
source_path: "FPF-Spec.md"
output_path: "by_section/C.32.P2S/C.32.P2S__002_problem-frame.md"
commit_sha: "9dd9215969126625d449a40e8ca4d1df9ac903f8"
heading_path:
  - "C.32.P2S — Problem-to-Structure Architecturing Unfolding"
  - "C.32.P2S:1 — Problem frame"
line_start: 64575
line_end: 64686
dependencies:
  - "A.1"
  - "A.1.SCR"
  - "A.1.STM"
  - "A.15.6"
  - "A.22"
  - "A.22.CGUS"
  - "A.3.4"
  - "B.2"
  - "C.22.2"
  - "C.25"
  - "C.29"
  - "C.30"
  - "C.30.AD"
  - "C.30.ASV"
  - "C.30.ILC"
  - "C.30.TFS-REL"
  - "C.31"
  - "C.32"
  - "C.32.ACE"
  - "C.32.ACS"
  - "C.32.CONWAY"
  - "C.32.FAIL"
  - "C.32.HCS"
  - "C.32.MLAO"
  - "C.33"
  - "C.34"
  - "C.35"
  - "E.17"
  - "E.18"
  - "E.18.3"
  - "E.24.PUB"
keywords:
---

### C.32.P2S:1 - Problem frame

Use this pattern when an architect or architecture-responsible practitioner has a stated external-use hypothesis for one project system-of-interest and must carry the resulting architecture pressure through selected structures, candidate synthesis, project architecture decision, realization Work, actual-structure feedback, and the next governed action. If the expected change outside the system, beneficiary or relying use, project designation, boundary hypothesis, or required functioning is not yet intelligible, stop before internal architecture and recover that missing basis through its direct owner.

The common first moment is practical: a required function has no recoverable bearer; an architecture characteristic is failing; a cross-scope residual survives local repair; a modularity, reuse, interface, scale, or description-loss problem blocks action; one typed Work, communication, tool, method, deployment, evidence, selected-structure, or architecture-side source cannot yet sustain the transformed-side architecture content needed for the changed referent; or operation shows that expected structures and actual structures diverge.

The first useful output is `ProblemToStructureArchitecturingFlowCard@Project`. The card is a working `U.Episteme` about one project-local P2S architecturing transformation flow, not the flow itself, the P2S method, a `U.MethodDescription`, or any planned or performed `U.Work`. It is not a new `U` kind, not an architecture claim, not an architecture decision, not a work plan, not an eval result, and not a publication format. It keeps the connected flow reviewable while each local object remains governed by the pattern that governs the current claim.

For the first pass, fill only the fields that prevent the next wrong move: described holon, bounded context, problem pressure, first governing pattern, one unknown or selected structure slot, and governing pattern for the next claim. Add decision, work, eval, publication, and feedback refs only when the flow reaches the pattern that governs them.

```text
ProblemToStructureArchitecturingFlowCard@Project:
  projectWorkOccurrenceRef?: U.EntityRef constrained to an individual admitted under U.Work
  architecturingFlowCardProjectUseRelationRef?: U.RelationRef governed by the exact architecturing-use or work-use pattern
  flowId:
  describedHolonRef:
  boundedContextRef:
  architectingSystemRef?: U.EntityRef constrained to U.System
  architectingRoleAssignmentRef?: U.EntityRef constrained to U.RoleAssignment, required when an architecting-role claim is current

  firstGoverningPatternRef:
  problemPressure:
    acceptedProblemCardRef?: U.EpistemeRef resolving to one exact C.22.2 ProblemCard
    actualProblematicForRelationRef?: U.RelationRef resolving to one exact C.22.PFR occurrence, only when an actual Problem is independently current

    pressureKind:
    problemPressureSignalRefs?:
    sourceUseRecordRefs?:
    architectureConcernRefs?:
    currentStopOrReturnReason?:
  architectureContent:
    architectureQuestionCardRef?: U.EpistemeRef resolving to one exact C.30 ArchitectureQuestionCard@Project
    architectureClaimRefs[]?: exact C.30 ArchitectureClaimRefs
    currentArchitectureRelationRefs[]?: exact obtaining C.30 ArchitectureRelation refs

    candidateStructureKindRefs:
    selectedStructureRefs?:
    expectedStructureRefs?:
    actualStructureRefs?:
    architectureCharacteristicRefs:
    architectureCharacteristicCriteriaSetRef?:
    qBundleRefs?:
    candidateSynthesisRef?:
  structuralInformation:
    unknownStructure:
    selectedStructure:
    expectedStructure:
    actualStructure:
    capturedInDescriptionsOrDecisions:
    handedToMethodsOrWork:
    latentOrHiddenStructure:
    lostStructure:
    strongerStructureInspectionReturnCondition:
  decisionAndWorkDocking:
    candidateSetOrPaletteRef?:
    selectedSetRef?:
    architectureDecisionRef?:
    adrProjectionRef?:
    methodDescriptionRefs?:
    workPlanRefs?:
    readinessRefs?:
    performedWorkRefs?:
    performedUnderAssignmentRelationRefs?: exact F.6 relation refs when performance attribution is current

    actualTransformationRefs?:
    directWorkToChangeGovernorRefs?:
    productionWorkClaimRefs?:
    entityIdentityInceptionClaimRefs?:
    productionCompletionClaimRefs?:
  architectureInfluenceCorrespondence?:
    changedReferentRef:
    actualTransformationRef?: U.EntityRef constrained to U.Transformation, only when independently grounded under A.3.4
    influenceSourceRows[]?: asserted influence facts only
      influenceSourceRef:
      influenceSourceKindRef:
      exactInfluenceRelationRef: U.RelationRef under its direct governor
      influenceGoverningPatternRef:
    influenceSourceArchitectureMaps[]?:
      influenceSourceHolonRef:
      influenceSourceArchitectureRelationRef?: exact obtaining C.30 ArchitectureRelation ref
      influenceSourceArchitectureClaimRef?: exact C.30 ArchitectureClaimRef for modal content
      influenceSourceSelectedStructureRefs:
    transformedHolonRef:
    transformedArchitectureRelationRef?: exact obtaining C.30 ArchitectureRelation ref
    transformedArchitectureClaimRef?: exact C.30 ArchitectureClaimRef for modal content
    transformedSelectedStructureRefs:
    correspondenceFrameOrPairRowRef: C.32.CONWAY synthesis-local frame or exact pair-row ref
  feedback:
    evalProgramRefs?:
    evalResultRefs?:
    actualStructureDescriptionRefs?:
    measurementRefs?:
    operationOrUseObservationRefs?:
    functionalCharacteristicImplications?:
    freshnessOrDecaySignalRefs?:
    governingPatternSpecificReturnOrRepair:
      c32NextSynthesisExit?
      c32PadOrAdaDecisionRepairOrSupersessionExit?
      e23ImprovementCycleRef?
      g11CurrentnessRefreshRef?
      e18TransformationFlowRefreshRef?
      c18C19ArchiveFrontPoolUpdateRef?
      c30DescriptionOrViewLossRepairRef?
  governingPatternForNextClaim:
```

For `ProblemToStructureArchitecturingFlowCard@Project`, `flowId` designates the exact project-local P2S architecturing transformation flow that is the card's C.2.1 EntityOfConcern. The claims carried by the filled card and the effective `U.ReferenceScheme` for its designations remain recoverable; changed claim content, changed flow EntityOfConcern, or changed effective reference scheme identifies another card episteme. `@Project` is a compatibility and retrieval cue only. It establishes no project entity, composite-work identity, context, authority, viewpoint, or parthood. When the card is genuinely used in one actual project, `projectWorkOccurrenceRef` identifies the exact composite Work occurrence admitted under `U.Work` and `architecturingFlowCardProjectUseRelationRef` identifies the direct relation by which architecturing work uses the card. The card, the architecturing work it helps coordinate, and the larger project work remain distinct.

The problem, architecting-side, realization, and architecture refs are pointers to independently governed objects, not P2S relation kinds. `acceptedProblemCardRef` resolves to one C.22.2 C.2.1 episteme; the nested signal and pressure fields neither constitute that card nor make an actual Problem obtain. `actualProblematicForRelationRef` is present only for an independently obtaining C.22.PFR occurrence. `architectingSystemRef` and any A.2.1 `architectingRoleAssignmentRef` remain distinct; when performance is current, `performedWorkRefs` and exact F.6 `performedUnderAssignment` refs retain the actual performer projection and assignment coverage. `actualTransformationRefs` resolve only to actual bounded changes independently grounded and identified under `A.3.4`; `directWorkToChangeGovernorRefs` resolve to exact direct subject relations or local claims selected under `A.6.RCD` disposition 2. The three production refs resolve to separate local `A.15.PROD` claims and remain absent when their particular question is not current. `actualStructureRefs` name subject-side `U.Structure` values whose declared substrate and selected relation organization are recovered under `A.22` from directly governed facts that actually obtain; they introduce neither an `ActualStructure` kind nor an actualization relation. C.30 keeps the exact described holon, obtaining `ArchitectureRelation` occurrences, selected structures, and any affirmative, negative, unresolved, candidate, required, desired, or expected `ArchitectureClaim` content separate. `actualStructureDescriptionRefs` name later descriptions of those structures and do not make them actual.

Not this pattern when the current work is only a problem card, only a grounded architecture claim, only a structural view, only a candidate palette, only a project architecture decision, only an ADR-like publication, only work planning, only performed work, only measurement, only a mathematical lens, or only `G.11` currentness, freshness, telemetry, edition, or decay orchestration. Use the pattern named in `Relations` for that narrower claim.

