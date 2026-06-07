---
chunk_kind: "child"
pattern_id: "C.30.TGA-FLOW-REL"
pattern_title: "Architecture-TGA Flow-Structure Relation"
section_id: "C.30.TGA-FLOW-REL:1"
section_title: "Problem frame"
source_path: "FPF-Spec.md"
output_path: "by_section/C.30.TGA-FLOW-REL/C.30.TGA-FLOW-REL__002_problem-frame.md"
commit_sha: "18497f0808242ab7c1a31cb5c94898e9f6b6879d"
heading_path:
  - "C.30.TGA-FLOW-REL — Architecture-TGA Flow-Structure Relation"
  - "C.30.TGA-FLOW-REL:1 — Problem frame"
line_start: 54034
line_end: 54068
dependencies:
  - "A.10"
  - "A.15"
  - "A.20"
  - "A.21"
  - "A.22"
  - "A.6.F"
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
  - "F.18"
  - "G.6"
keywords:
  - "ArchitectureFlowStructureRelation@TGA"
  - "FlowTransductionStructure"
  - "TGA graph relation"
  - "architecture flow relation"
  - "graph/path/crossing"
---

### C.30.TGA-FLOW-REL:1 - Problem frame

Use this pattern when an architecture discussion depends on a Transduction Graph Architecture (TGA) graph, path, path slice, crossing, flow valuation, edition pin, plane pin, context pin, or no-hidden-scalarization claim.

The first useful move is small. `ArchitectureFlowStructureRelation@TGA` is a C.30-side relation record for a live relation between `ArchitectureOf@Context`, selected architecture-relevant structure, architecture structural view, or conditional `ArchitectureDescription@Context` use and the E.18 graph, path, crossing, or flow-valuation relation being used for flow or transduction structure. It names the architecture locus, selected structure or view reference when live, conditional description reference when durable description use is live, the E.18 object, correspondence or source-return condition when live, and the admissible architecture use.

```text
ArchitectureFlowStructureRelation@TGA:
architectureClaimRef:
selectedArchitectureStructureRefs:
architectureStructuralViewRef?:
architectureDescriptionRef?:
functionalStructureViewRef:
flowTransductionStructureViewRef:
transductionGraphRef:
activePathOrSliceRefs:
crossingBundleRefs:
flowValuationRefs:
correspondenceRefs:
sourceReturnCondition?:
admissibleUse:
nonAdmissibleUse:
governingPatternApplicationRefs:
```

Ordinary minimum: name one of `architectureClaimRef`, `selectedArchitectureStructureRefs`, `architectureStructuralViewRef`, or `architectureDescriptionRef` when durable description use is live, one E.18 graph or path-slice reference, the architecture-flow `FlowTransductionStructure`, one blocked overread, and stop or exact governing pattern application. Use crossing, flow-valuation, correspondence, and source-return fields only when they change the next architecture move. All other fields are conditional and may be `not live`.

Use this relation only when a grounded architecture claim, selected architecture-relevant structure, architecture structural view, functional-architecture view, flow-structure claim, or conditional architecture-description use depends on an E.18 graph, path, crossing, or valuation relation. Stop when the architecture flow relation and non-admissible uses are clear. Open a neighboring pattern only when that neighboring claim kind is live.

What goes wrong if this pattern is missed: a TGA graph becomes functional architecture, whole architecture ontology, work sequence, proof, or project decision by appearance.

What this buys in practice: the practitioner can use E.18 for flow or transduction structure while C.30 remains the grounded architecture and selected-structure adequacy locus and C.30.ASV remains the architecture-structural-view locus.

Not this pattern when the live question is a graph, path, crossing, or flow valuation without a live relation to grounded architecture adequacy, conditional architecture-description use, or an architecture structural view. Use E.18 directly. If the live question is an architecture claim or durable architecture description without an E.TGA graph claim, path claim, or crossing claim kind, use C.30. If it is a functional view without flow relation or TGA claim kind, use C.30.ASV and A.6.F. If another live claim is present, use the exact governing pattern and keep C.30.TGA-FLOW-REL only to the architecture-flow relation.

