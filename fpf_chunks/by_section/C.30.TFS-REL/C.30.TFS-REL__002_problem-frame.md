---
chunk_kind: "child"
pattern_id: "C.30.TFS-REL"
pattern_title: "Architecture Transformation-Flow Structure Relation"
section_id: "C.30.TFS-REL:1"
section_title: "Problem frame"
source_path: "FPF-Spec.md"
output_path: "by_section/C.30.TFS-REL/C.30.TFS-REL__002_problem-frame.md"
commit_sha: "2ada413629b846ef308222d16489a82cb5b40a71"
heading_path:
  - "C.30.TFS-REL — Architecture Transformation-Flow Structure Relation"
  - "C.30.TFS-REL:1 — Problem frame"
line_start: 62244
line_end: 62297
dependencies:
  - "A.10"
  - "A.15"
  - "A.20"
  - "A.21"
  - "A.22"
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
  - "C.30.ASV"
  - "C.30.STRAT"
  - "C.32"
  - "C.32.CONWAY"
  - "C.32.P2S"
  - "C.33"
  - "C.34"
  - "C.35"
  - "E.10"
  - "E.17"
  - "E.17.0"
  - "E.18"
  - "E.18.2"
  - "E.18.3"
  - "E.18.NET"
  - "F.18"
  - "G.6"
keywords:
---

### C.30.TFS-REL:1 - Problem frame

Use this pattern when an architecture discussion depends on a selected `TransformationFlowStructure`, one selected `TransformationFlowStructureNetwork`, or a current path, path slice, crossing, flow valuation, edition pin, plane pin, context pin, no-hidden-scalarization claim, or mathematical description of the selected flow structure.

The first useful move is small. `ArchitectureTransformationFlowStructureRelation@Context` relates one named architecture locus to the selected E.18 TFS or E.18.NET network used in the architecture question. It names the architecture claim, selected structure or view, conditional description use, relevant functional and flow refs, mathematical or publication source when current, correspondence, hidden-structure return, admissible use, and—when a network is selected—whether one named containing holon or several explicitly named holons supply the architecture side.

```text
ArchitectureTransformationFlowStructureRelation@Context:
architectureClaimRef?:
selectedArchitectureStructureRefs?:
architectureStructuralViewRef?:
architectureDescriptionRef?:
functionalStructureViewRef?:
functionalElementRefs?:
functionalBehaviorRefs?:
transformerSideFillerRefs?:
candidateBearerRefs?:
inputConditionRefs?:
outputConditionRefs?:
functionalPortRefs?:
transformationFlowStructureViewRef?:
transformationFlowStructureRef?:
transformationFlowStructureNetworkRef?:
networkCrossFlowRelationRowRefs[]?: E.18.NET NetworkCrossFlowRelationRowRef
networkArchitectureUseBranch?: namedContainingHolon | explicitInterHolon
containingArchitectureClaimRef?:
participatingArchitectureClaimRefs[]?:
noArchitectureOfNetworkBearerAsserted?:
transformationFlowUnfoldingStructureRef?:
selectedPathOrSliceRefs?:
crossingBundleRefs?:
flowValuationRefs?:
mathematicalDescriptionRefs?:
mathLensUseRefs?:
correspondenceRefs?:
sourcePublicationOrEditionRef?:
extractionOrProbeLocusRef?:
relationObservationClassRef?:
unexploredRegionRefs?:
hiddenRelationStructureReturnCondition?:
admissibleUse:
nonAdmissibleUse:
```

Ordinary minimum: name at least one architecture-side reference (`architectureClaimRef`, `selectedArchitectureStructureRefs`, `architectureStructuralViewRef`, `architectureDescriptionRef` when durable description use is being made, `containingArchitectureClaimRef`, or `participatingArchitectureClaimRefs[]`), at least one flow-structure reference (`transformationFlowStructureRef`, `transformationFlowStructureNetworkRef`, `transformationFlowUnfoldingStructureRef`, `selectedPathOrSliceRefs`, `crossingBundleRefs`, or `flowValuationRefs`), one blocked overread, and stop or governing-pattern application. A network use also selects exactly one network architecture-use branch and supplies its required architecture claim refs. Use the remaining conditional fields only when they change the next architecture move; otherwise mark them `not used`.

Use this relation only when a grounded architecture claim, selected architecture-relevant structure, architecture structural view, functional-architecture view, transformation-flow-structure claim, or conditional architecture-description use depends on an E.18 TFS, an E.18.NET network, or one of the selected TFS's paths, crossings, or valuations. Stop when that architecture-to-flow-structure relation and its non-admissible uses are clear. If another claim is being made, apply its governing pattern and keep this record to the architecture relation.

What goes wrong if this pattern is missed: a transformation-flow diagram, graph-shaped mathematical description, path slice, or flow valuation becomes functional architecture, whole architecture ontology, performed-work occurrence, work-result record, evidence, gate passage, or project decision by appearance.

What this buys in practice: the practitioner can use E.18 for one TFS or E.18.NET for one network while C.30 remains the grounded architecture and selected-structure adequacy locus and C.30.ASV remains the architecture-structural-view locus.

Not this pattern when the question is only the TFS or network, a mathematical description, path, crossing, or flow valuation and no architecture relation is being claimed. Use E.18 for one TFS, E.18.NET for one network, E.18.2 for its mathematical description, and C.29 when mathematical-lens use is current. Use C.30 for an architecture claim or durable architecture description without this flow-structure relation; use C.30.ASV and A.6.F for a functional view without it. Apply any other claim's governing pattern and keep C.30.TFS-REL only to the architecture relation.

