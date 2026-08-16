---
chunk_kind: "child"
pattern_id: "C.30.TFS-REL"
pattern_title: "Architecture Transformation-Flow Structure Relation"
section_id: "C.30.TFS-REL:1"
section_title: "Problem frame"
source_path: "FPF-Spec.md"
output_path: "by_section/C.30.TFS-REL/C.30.TFS-REL__002_problem-frame.md"
commit_sha: "3d098629dc218572089f1890080c17d6f1d9a867"
heading_path:
  - "C.30.TFS-REL — Architecture Transformation-Flow Structure Relation"
  - "C.30.TFS-REL:1 — Problem frame"
line_start: 62509
line_end: 62583
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
nonAdmissibleUse:
```

This is a use/trace record, not a universal direct `U.Relation` declaration and not an obtaining-condition shortcut. Each positive `architectureRelationOccurrenceRef`, flow relation, cross-member relation, correspondence relation, empirical-grounding relation, publication occurrence, or project/work relation is admitted and made actual only by its direct owner. The record, diagram, description, or list creates none of them.

Ordinary minimum: name at least one exact architecture-side reference (`architectureRelationOccurrenceRefs`, `selectedArchitectureStructureRefs`, `architectureStructuralViewRefs`, `architectureDescriptionRefs`, or a bounded `architectureClaimRefs` entry) and at least one flow-structure reference (`transformationFlowStructureRef`, `transformationFlowStructureNetworkRef`, `transformationFlowUnfoldingStructureRef`, `selectedPathOrSliceRefs`, `crossingBundleRefs`, or `flowValuationRefs`), one blocked overread, and one stop or governing-pattern application. A network use also selects exactly one network architecture-use branch and supplies its required exact holon and relation/claim refs. Use the remaining fields only when they change the next architecture move; otherwise mark them `not used`.

Use this record only when an actual architecture relation, selected architecture-relevant structure, exact structural-view episteme, functional-structure view, transformation-flow-structure claim, or conditional architecture-description use depends on an E.18 TFS, an E.18.NET network, or one of the selected TFS's paths, crossings, or valuations. Stop when that architecture-to-flow-structure use and its non-admissible overreads are clear. If another claim is being made, apply its governing pattern and keep this record to the architecture/flow boundary.

What goes wrong if this pattern is missed: a transformation-flow diagram, graph-shaped mathematical description, path slice, flow valuation, requirement, or functional-view row becomes functional architecture, whole architecture ontology, actual `U.Transformation`, performed Work, work-result record, evidence, gate passage, or project decision by appearance.

What this buys in practice: the practitioner can use E.18 for one TFS or E.18.NET for one network while C.30 remains the direct architecture-relation and selected-structure adequacy locus and C.30.ASV remains the architecture-structural-view locus.

Not this pattern when the question is only the TFS or network, a mathematical description, path, crossing, or flow valuation and no architecture use is being made. Use E.18 for one TFS, E.18.NET for one network, E.18.2 for its mathematical description, and C.29 when mathematical-lens use is current. Use C.30 for a direct architecture relation or architecture claim without this flow-structure use; use C.30.AD for a durable architecture description and C.30.ASV/A.6.F for a functional view without it. Apply any other claim's governing pattern and keep C.30.TFS-REL only to the architecture/flow relation.

