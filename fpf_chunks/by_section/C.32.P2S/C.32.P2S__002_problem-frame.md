---
chunk_kind: "child"
pattern_id: "C.32.P2S"
pattern_title: "Problem-to-Structure Architecturing Unfolding"
section_id: "C.32.P2S:1"
section_title: "Problem frame"
source_path: "FPF-Spec.md"
output_path: "by_section/C.32.P2S/C.32.P2S__002_problem-frame.md"
commit_sha: "17edd955485f60cafb16159c7d90e20f4ad21844"
heading_path:
  - "C.32.P2S — Problem-to-Structure Architecturing Unfolding"
  - "C.32.P2S:1 — Problem frame"
line_start: 63679
line_end: 63768
dependencies:
  - "A.15"
  - "A.15.1"
  - "A.15.2"
  - "A.15.5"
  - "A.15.PROD"
  - "A.19.CPM"
  - "A.19.SelectorMechanism"
  - "A.22"
  - "A.22.CGUS"
  - "A.3.4"
  - "A.6.RCD"
  - "B.2"
  - "C.11"
  - "C.16"
  - "C.18"
  - "C.19"
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
  - "C.32.ADA"
  - "C.32.ADR"
  - "C.32.CONWAY"
  - "C.32.FAIL"
  - "C.32.HCS"
  - "C.32.MLAO"
  - "C.32.PAD"
  - "C.33"
  - "C.34"
  - "C.35"
  - "E.17"
  - "E.18"
  - "E.18.3"
  - "E.23"
  - "E.24.PUB"
  - "G.11"
  - "G.5"
keywords:
  - "ArchitectureUnfoldingStructureUse@Project"
  - "ProblemToStructureArchitecturingFlowCard@Project"
  - "actual-structure feedback"
  - "candidate structures"
  - "exact domain work"
  - "expected structures"
  - "governing-pattern-specific return"
  - "independently grounded actual changes"
  - "no-automatic-composition"
  - "problem-to-structure architecturing unfolding"
  - "selected structures"
  - "structural uncertainty"
  - "subject-side actual structures"
---

### C.32.P2S:1 - Problem frame

Use this pattern when an architect or architecture-responsible practitioner starts from architecture-relevant problem pressure that needs to stay connected through selected structures, candidate synthesis, project architecture decision, realization work, actual-structure feedback, and the next governed action.

The common first moment is practical: a required function has no recoverable bearer; an architecture characteristic is failing; a cross-scope residual survives local repair; a modularity, reuse, interface, scale, or description-loss problem blocks action; a transformer holon cannot yet produce the desired transformed holon; or operation shows that expected structures and actual structures diverge.

The first useful output is `ProblemToStructureArchitecturingFlowCard@Project`. The card is a working record of one architecturing flow. It is not a new `U` kind, not an architecture claim, not an architecture decision, not a work plan, not an eval result, and not a publication format. It keeps the connected flow reviewable while each local object remains governed by the pattern that governs the current claim.

For the first pass, fill only the fields that prevent the next wrong move: described holon, bounded context, problem pressure, first governing pattern, one unknown or selected structure slot, and governing pattern for the next claim. Add decision, work, eval, publication, and feedback refs only when the flow reaches the pattern that governs them.

```text
ProblemToStructureArchitecturingFlowCard@Project:
  projectWorkOccurrenceRef?: U.EntityRef constrained to an individual admitted under U.Work
  architecturingFlowCardProjectUseRelationRef?: U.RelationRef governed by the exact architecturing-use or work-use pattern
  flowId:
  describedHolonRef:
  boundedContextRef:
  architectingHolonOrRoleRef?:
  firstGoverningPatternRef:
  problemPressure:
    pressureKind:
    problemPressureSignalRefs?:
    sourceUseRecordRefs?:
    architectureConcernRefs?:
    currentStopOrReturnReason?:
  architectureContent:
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
    actualTransformationRefs?:
    directWorkToChangeGovernorRefs?:
    productionWorkClaimRefs?:
    entityIdentityInceptionClaimRefs?:
    productionCompletionClaimRefs?:
  transformerTransformed?:
    changingRelationRef:
    transformerHolonRef:
    transformedHolonRef:
    transformerSelectedStructureRefs:
    transformedSelectedStructureRefs:
    correspondenceFrameRef:
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

For `ProblemToStructureArchitecturingFlowCard@Project`, `@Project` is a compatibility and retrieval cue only. It establishes no project entity, composite-work identity, context, authority, viewpoint, or parthood. When the card is genuinely used in one actual project, `projectWorkOccurrenceRef` identifies the exact composite Work occurrence admitted under `U.Work` and `architecturingFlowCardProjectUseRelationRef` identifies the direct relation by which architecturing work uses the card. The card, the architecturing work it helps coordinate, and the larger project work remain distinct.

The realization refs are pointers to independently governed objects, not P2S relation kinds. `actualTransformationRefs` resolve only to actual bounded changes independently grounded and identified under `A.3.4`; `directWorkToChangeGovernorRefs` resolve to exact direct subject relations or local claims selected under `A.6.RCD` disposition 2. The three production refs resolve to separate local `A.15.PROD` claims and remain absent when their particular question is not current. `actualStructureRefs` name subject-side `U.Structure` values whose declared substrate and selected relation organization are recovered under `A.22` from directly governed facts that actually obtain; they introduce neither an `ActualStructure` kind nor an actualization relation. `C.30` governs only the corresponding `ArchitectureOf@Context` claim over selected structure refs. `actualStructureDescriptionRefs` name later descriptions of those structures and do not make them actual.

Not this pattern when the current work is only a problem card, only a grounded architecture claim, only a structural view, only a candidate palette, only a project architecture decision, only an ADR-like publication, only work planning, only performed work, only measurement, only a mathematical lens, or only `G.11` currentness, freshness, telemetry, edition, or decay orchestration. Use the pattern named in `Relations` for that narrower claim.

