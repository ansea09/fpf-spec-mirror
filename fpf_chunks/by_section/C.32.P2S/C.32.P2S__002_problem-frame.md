---
chunk_kind: "child"
pattern_id: "C.32.P2S"
pattern_title: "Problem-to-Structure Architecturing Transformation Flow"
section_id: "C.32.P2S:1"
section_title: "Problem frame"
source_path: "FPF-Spec.md"
output_path: "by_section/C.32.P2S/C.32.P2S__002_problem-frame.md"
commit_sha: "6bbbb622859fbbcddc02b23ea76bee4dd71c6291"
heading_path:
  - "C.32.P2S — Problem-to-Structure Architecturing Transformation Flow"
  - "C.32.P2S:1 — Problem frame"
line_start: 58913
line_end: 58989
dependencies:
  - "A.15"
  - "A.15.1"
  - "A.15.2"
  - "A.15.5"
  - "A.19.CPM"
  - "A.19.SelectorMechanism"
  - "A.3.4"
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
  - "E.23"
  - "E.24.PUB"
  - "G.11"
  - "G.5"
keywords:
  - "ProblemToStructureArchitecturingFlowCard@Project"
  - "actual-structure feedback"
  - "architecture work flow"
  - "owner-specific return"
  - "problem-to-structure architecturing flow"
  - "selected structures"
  - "structural uncertainty"
---

### C.32.P2S:1 - Problem frame

Use this pattern when an architect or architecture-responsible practitioner starts from architecture-relevant problem pressure that needs to stay connected through selected structures, candidate synthesis, project architecture decision, realization work, actual-structure feedback, and the next owner-specific action.

The common first moment is practical: a required function has no recoverable bearer; an architecture characteristic is failing; a cross-scope residual survives local repair; a modularity, reuse, interface, scale, or description-loss problem blocks action; a transformer holon cannot yet produce the desired transformed holon; or operation shows that expected structures and actual structures diverge.

The first useful output is `ProblemToStructureArchitecturingFlowCard@Project`. The card is a local project record of one architecturing flow. It is not a new `U` kind, not an architecture claim, not an architecture decision, not a work plan, not an eval result, and not a publication format. It keeps the connected flow reviewable while each local object remains governed by its owner pattern.

For the first pass, fill only the fields that prevent the next wrong move: described holon, bounded context, problem pressure, first governing owner, one unknown or selected structure slot, and neighboring owner for the next claim. Add decision, work, eval, publication, and feedback refs only when the flow reaches the owner pattern that governs them.

```text
ProblemToStructureArchitecturingFlowCard@Project:
  flowId:
  describedHolonRef:
  boundedContextRef:
  architectingHolonOrRoleRef?:
  firstGoverningOwnerRef:
  problemPressure:
    pressureKind:
    sourceSignalRefs?:
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
    sourceReturnCondition:
  decisionAndWorkDocking:
    candidateSetOrPaletteRef?:
    selectedSetRef?:
    architectureDecisionRef?:
    adrProjectionRef?:
    methodDescriptionRefs?:
    workPlanRefs?:
    readinessRefs?:
    performedWorkRefs?:
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
    measurementRefs?:
    operationOrUseObservationRefs?:
    functionalCharacteristicImplications?:
    freshnessOrDecaySignalRefs?:
    ownerSpecificReturnOrRepair:
      c32NextSynthesisExit?
      c32PadOrAdaDecisionRepairOrSupersessionExit?
      e23ImprovementCycleRef?
      g11CurrentnessRefreshRef?
      e18TransformationFlowRefreshRef?
      c18C19ArchiveFrontPoolUpdateRef?
      c30DescriptionOrViewSourceReturnRef?
  neighboringOwnerForNextClaim:
```

Not this pattern when the current work is only a problem card, only a grounded architecture claim, only a structural view, only a candidate palette, only a project architecture decision, only an ADR-like publication, only work planning, only performed work, only measurement, only a mathematical lens, or only `G.11` currentness, freshness, telemetry, edition, or decay orchestration. Use the owner named in `Relations` for that narrower claim.

