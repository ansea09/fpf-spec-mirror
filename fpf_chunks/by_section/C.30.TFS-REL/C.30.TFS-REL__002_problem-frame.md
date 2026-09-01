---
chunk_kind: "child"
pattern_id: "C.30.TFS-REL"
pattern_title: "Architecture Transformation-Flow Structure Relation"
section_id: "C.30.TFS-REL:1"
section_title: "Problem frame"
source_path: "FPF-Spec.md"
output_path: "by_section/C.30.TFS-REL/C.30.TFS-REL__002_problem-frame.md"
commit_sha: "3c3f968398a938bc10e83da22d509b7b8f642d83"
heading_path:
  - "C.30.TFS-REL — Architecture Transformation-Flow Structure Relation"
  - "C.30.TFS-REL:1 — Problem frame"
line_start: 61659
line_end: 61734
dependencies:
  - "A.10"
  - "A.15"
  - "A.20"
  - "A.21"
  - "A.22"
  - "A.3.4"
  - "A.6.0"
  - "A.6.5"
  - "A.6.F"
  - "A.6.M"
  - "A.7"
  - "B.3"
  - "C.16"
  - "C.2.P"
  - "C.28"
  - "C.29"
  - "C.30"
  - "C.30.AD"
  - "C.30.ASV"
  - "C.30.STRAT"
  - "C.32"
  - "C.32.CONWAY"
  - "C.32.P2S"
  - "C.33"
  - "C.34"
  - "C.35"
  - "E.10"
  - "E.17.0"
  - "E.18"
  - "E.18.2"
  - "E.18.3"
  - "E.18.NET"
  - "E.24.PUB"
  - "F.18"
  - "G.6"
keywords:
---

### C.30.TFS-REL:1 - Problem frame

Use this pattern when an architecture discussion depends on one exact selected `TransformationFlowStructure`, one selected `TransformationFlowStructureNetwork`, or a current path, path slice, crossing, flow valuation, edition pin, plane pin, context pin, no-hidden-scalarization claim, or mathematical description of the selected flow structure.

The first useful move is small. `ArchitectureTransformationFlowStructureRelation` is a bounded architecture-use record connecting one exact architecture locus to the selected E.18 TFS or E.18.NET network used in the question. The locus can be an actual `ArchitectureRelation` occurrence, exact selected architecture structure, exact architecture-description or structural-view episteme, or bounded architecture claim. When a network is selected, the record also says whether one named containing holon or several explicitly named holons supply the architecture side.

```text
ArchitectureTransformationFlowStructureRelation:
architectureRelationOccurrenceRefs?:
architectureClaimRefs?:
selectedArchitectureStructureRefs?:
architectureStructuralViewRefs?:
architectureDescriptionRefs?:
architectureUseConcernRefs?:
claimScope?: U.ClaimScope, byValue
effectiveReferenceScheme?: U.ReferenceScheme, byValue
modelUseStructureRef?: U.StructureRef
empiricalGroundingRelationRefs?:

functionalStructureViewRefs?:
functionalElementClaimRefs?:
functionalBehaviorClaimRefs?:
requiredOrDesiredEffectClaimRefs?:
actualTransformationRefs?:
transformerSideFillerRefs?:
candidateBearerRefs?:
inputConditionRefs?:
outputConditionRefs?:
functionalPortRefs?:

transformationFlowStructureViewRefs?:
transformationFlowStructureRef?:
transformationFlowStructureNetworkRef?:
networkCrossFlowRelationRowRefs[]?: E.18.NET NetworkCrossFlowRelationRowRef
networkArchitectureUseBranch?: namedContainingHolon | explicitInterHolon
containingHolonRef?:
containingArchitectureRelationRef?:
containingArchitectureClaimRef?:
participatingHolonRefs[]?:
participatingArchitectureRelationRefs[]?:
participatingArchitectureClaimRefs[]?:
noNetworkBearerHolonAsserted?:
transformationFlowUnfoldingStructureRef?:
selectedPathOrSliceRefs?:
crossingBundleRefs?:
flowValuationRefs?:

mathematicalDescriptionRefs?:
mathLensUseRefs?:
correspondenceClaimOrRelationRefs?:
sourcePublicationOrEditionRef?:
representationRefs?:
publicationOccurrenceRefs?:
publicationFormRefs?:
carrierRefs?:
extractionOrProbeLocusRef?:
relationObservationClassRef?:
unexploredRegionRefs?:
hiddenRelationStructureReturnCondition?:
admissibleUse:
stopOrReturnCondition:
groundedNonAdmissibleUse?:
```

This use/trace record connects an exact architecture-side reference to an exact flow-structure reference. Admit every positive architecture, flow, correspondence, grounding, publication, or project relation through its direct pattern before recording it here.

Ordinary minimum: name one exact architecture-side reference, one exact flow-structure reference, the admissible use, and one stop or governing-pattern application. A network use also selects one network architecture-use branch with its required holon and relation or claim refs. Add a grounded non-admissible use only when the current representation or wording makes that exact architecture/TFS confusion live.

Use this record when an actual architecture relation, selected structure, structural-view episteme, functional-structure view, transformation-flow claim, or conditional architecture-description use depends on an E.18 TFS, E.18.NET network, or one of its selected paths, crossings, or valuations. Stop when the architecture-to-flow use and its return condition are clear; route any other current claim to its direct pattern.

What goes wrong if this pattern is missed: a visible flow representation is reused as an architecture, Work, evidence, gate, or decision claim solely by appearance, so the reader can no longer recover the direct predicate that would support that claim.

What this buys in practice: the practitioner can use E.18 for one TFS or E.18.NET for one network while C.30 remains the direct architecture-relation and selected-structure adequacy locus and C.30.ASV remains the architecture-structural-view locus.

Not this pattern when the question is only the TFS or network, a mathematical description, path, crossing, or flow valuation and no architecture use is being made. Use E.18 for one TFS, E.18.NET for one network, E.18.2 for its mathematical description, and C.29 when mathematical-lens use is current. Use C.30 for a direct architecture relation or architecture claim without this flow-structure use; use C.30.AD for a durable architecture description and C.30.ASV/A.6.F for a functional view without it. Apply any other claim's governing pattern and keep C.30.TFS-REL only to the architecture/flow relation.

