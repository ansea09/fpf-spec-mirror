---
chunk_kind: "child"
pattern_id: "C.30.TGA-FLOW-REL"
pattern_title: "Architecture Transformation-Flow Structure Relation"
section_id: "C.30.TGA-FLOW-REL:1"
section_title: "Problem frame"
source_path: "FPF-Spec.md"
output_path: "by_section/C.30.TGA-FLOW-REL/C.30.TGA-FLOW-REL__002_problem-frame.md"
commit_sha: "cb17c555f343780e31e5fea236a74adc69295736"
heading_path:
  - "C.30.TGA-FLOW-REL — Architecture Transformation-Flow Structure Relation"
  - "C.30.TGA-FLOW-REL:1 — Problem frame"
line_start: 55541
line_end: 55579
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
  - "E.10"
  - "E.17"
  - "E.17.0"
  - "E.18"
  - "E.18.2"
  - "F.18"
  - "G.6"
keywords:
  - "architecture structural view"
  - "architecture-to-transformation-flow relation"
  - "functional behavior"
  - "selected structure"
  - "transformation-flow structure"
---

### C.30.TGA-FLOW-REL:1 - Problem frame

Use this pattern when an architecture discussion depends on a selected `TransformationFlowStructure`, its path, path slice, crossing, flow valuation, edition pin, plane pin, context pin, no-hidden-scalarization claim, or mathematical description.

The first useful move is small. `ArchitectureTransformationFlowStructureRelation@Context` is a C.30-side relation record for a relation being used between `ArchitectureOf@Context`, selected architecture-relevant structure, architecture structural view, or conditional `ArchitectureDescription@Context` use and the E.18 selected transformation-flow structure being used for architecture work. It names the architecture locus, selected structure or view reference when used in the relation, conditional description reference when durable description use is being made, any functional element, functional behavior, transformer or candidate bearer, and input/output or functional-port references that change the relation, the E.18 selected structure or locus, any E.18.2 mathematical description used, correspondence or source-return condition when used in the relation, and the admissible architecture use.

```text
ArchitectureTransformationFlowStructureRelation@Context:
architectureClaimRef?:
selectedArchitectureStructureRefs?:
architectureStructuralViewRef?:
architectureDescriptionRef?:
functionalStructureViewRef?:
functionalElementRefs?:
functionalBehaviorRefs?:
transformerOrCandidateBearerRefs?:
inputOutputOrFunctionalPortRefs?:
transformationFlowStructureViewRef?:
transformationFlowStructureRef?:
selectedPathOrSliceRefs?:
crossingBundleRefs?:
flowValuationRefs?:
mathematicalDescriptionRefs?:
correspondenceRefs?:
sourceReturnCondition?:
admissibleUse:
nonAdmissibleUse:
```

Ordinary minimum: name at least one architecture-side reference (`architectureClaimRef`, `selectedArchitectureStructureRefs`, `architectureStructuralViewRef`, or `architectureDescriptionRef` when durable description use is being made), at least one E.18-side reference (`transformationFlowStructureRef`, `selectedPathOrSliceRefs`, `crossingBundleRefs`, or `flowValuationRefs`), one blocked overread, and stop or governing-pattern application. Use functional-structure, functional-element, functional-behavior, transformer/bearer, input/output or functional-port, transformation-flow-structure, mathematical-description, crossing, flow-valuation, correspondence, and source-return fields only when they change the next architecture move. All other fields are conditional and may be `not used`.

Use this relation only when a grounded architecture claim, selected architecture-relevant structure, architecture structural view, functional-architecture view, transformation-flow-structure claim, or conditional architecture-description use depends on an E.18 selected structure, path, crossing, or valuation relation. Stop when the architecture-to-transformation-flow relation and non-admissible uses are clear. If another claim is being made, that claim is governed by its governing pattern and this relation remains only the architecture-to-transformation-flow relation.

What goes wrong if this pattern is missed: a transformation-flow diagram, graph-shaped mathematical description, path slice, or flow valuation becomes functional architecture, whole architecture ontology, performed-work occurrence, work-result record, evidence, gate passage, or project decision by appearance.

What this buys in practice: the practitioner can use E.18 for selected transformation-flow structure while C.30 remains the grounded architecture and selected-structure adequacy locus and C.30.ASV remains the architecture-structural-view locus.

Not this pattern when the question under repair is a selected transformation-flow structure, mathematical description, path, crossing, or flow valuation without a relation being used for grounded architecture adequacy, conditional architecture-description use, or an architecture structural view. Use E.18 directly for the selected structure and E.18.2/C.29 when the mathematical description or lens-use claim is current. If the question under repair is an architecture claim or durable architecture description without a transformation-flow-structure relation, use C.30. If it is a functional view without transformation-flow relation, use C.30.ASV and A.6.F. If another claim being made is present, use the governing pattern and keep C.30.TGA-FLOW-REL only to the architecture-to-transformation-flow relation.

