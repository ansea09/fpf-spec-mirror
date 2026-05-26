---
chunk_kind: "child"
pattern_id: "C.30.TGA-FLOW-REL"
pattern_title: "Architecture/TGA Flow-Structure Relation"
section_id: "C.30.TGA-FLOW-REL:1"
section_title: "Problem frame"
source_path: "FPF-Spec.md"
output_path: "by_section/C.30.TGA-FLOW-REL/C.30.TGA-FLOW-REL__002_problem-frame.md"
commit_sha: "ae1ff1c7a231a2ec78d244b40d7805a5538c6608"
heading_path:
  - "C.30.TGA-FLOW-REL — Architecture/TGA Flow-Structure Relation"
  - "C.30.TGA-FLOW-REL:1 — Problem frame"
line_start: 51361
line_end: 51394
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
  - "C.28"
  - "C.29"
  - "C.30"
  - "C.30.ASV"
  - "E.10"
  - "E.10.SEMIO"
  - "E.17"
  - "E.17.0"
  - "E.18"
  - "F.18"
  - "G.6"
keywords:
  - "ArchitectureFlowStructureRelation@TGA"
  - "FlowTransductionStructure"
  - "TGA graph support"
  - "architecture flow relation"
  - "graph/path/crossing"
---

### C.30.TGA-FLOW-REL:1 - Problem frame

Use this pattern when an architecture discussion depends on a Transduction Graph Architecture (TGA) graph, path, path slice, crossing, flow valuation, edition pin, plane/context pin, or no-hidden-scalarization claim.

The first useful move is small. `ArchitectureFlowStructureRelation@TGA` is a C.30-side relation record that links an architecture description or architecture structural view to E.18 graph, path, crossing, or flow-valuation support; it is not the graph, not the architecture, not an architecture decision, and not a complete architecture view by itself.

```text
ArchitectureFlowStructureRelation@TGA:
architectureDescriptionRef:
architectureStructuralViewRef:
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
neighboringPatternExitRefs:
```

Ordinary minimum: name either `architectureStructuralViewRef` or `architectureDescriptionRef`, one E.18 graph or path-slice reference, the supported `FlowTransductionStructure`, one blocked overread, and stop or neighboring exit. Use crossing, flow-valuation, correspondence, and source-return fields only when they change the next architecture move. All other fields are conditional and may be `not live`.

Use this relation only when a functional-architecture or flow-structure claim needs E.18 graph/path/crossing/valuation support. Stop when the architecture flow relation and non-admissible uses are clear. Do not open work, evidence, assurance, gate, causal, mathematical-lens, P2W, or architecture-decision support unless that claim kind is live.


What goes wrong if this pattern is missed: a TGA graph becomes functional architecture, whole architecture ontology, work sequence, evidence path, gate result, causal flow proof, assurance support, or project decision by appearance.

What this buys in practice: the practitioner can use E.18 for flow/transduction structure while C.30 remains the governing architecture-description locus and C.30.ASV remains the architecture-structural-view locus.

Not this pattern when the live question is a graph, path, crossing, or flow valuation without architecture-description claim kind. Use E.18 directly. If the live question is architecture description without E.TGA graph/path/crossing claim kind, use C.30. If it is a functional view without flow/TGA claim kind, use C.30.ASV and A.6.F. If it is work, evidence, assurance, gate, causal use, mathematical-lens adequacy, P2W, or decision support, use the exact neighboring pattern and keep C.30.TGA-FLOW-REL only to the architecture-flow relation.

