---
chunk_kind: "child"
pattern_id: "C.30.TGA-FLOW-REL"
pattern_title: "Architecture/TGA Flow-Structure Relation"
section_id: "C.30.TGA-FLOW-REL:4"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/C.30.TGA-FLOW-REL/C.30.TGA-FLOW-REL__005_solution.md"
commit_sha: "16cd31387cff04ab6b0feef22717f82ac54efa8f"
heading_path:
  - "C.30.TGA-FLOW-REL — Architecture/TGA Flow-Structure Relation"
  - "C.30.TGA-FLOW-REL:4 — Solution"
line_start: 53335
line_end: 53437
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
  - "E.10"
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

### C.30.TGA-FLOW-REL:4 - Solution

C.30.TGA-FLOW-REL is the C.30 entry relation to E.18 when an architecture description or architecture structural view uses E.TGA graph/path/crossing/flow-valuation objects as flow/transduction structure relation.

It imports E.18; it does not redefine E.TGA. It supplies only the architecture-description relation:

```text
ArchitectureFlowStructureRelation@TGA ::= {
  architectureDescriptionRef,
  architectureStructuralViewRef?,
  functionalStructureViewRef?,
  flowTransductionStructureViewRef?,
  transductionGraphRef,
  activePathOrSliceRefs,
  crossingBundleRefs?,
  flowValuationRefs?,
  correspondenceRefs,
  sourceReturnCondition?,
  admissibleUse,
  nonAdmissibleUse
}
```

#### C.30.TGA-FLOW-REL:4.1 - Use trigger

Open this pattern only when a live architecture claim depends on one or more E.18 objects:

- `TransductionGraphRef`;
- `PathId` or `PathSliceId`;
- `CrossingBundleRef`;
- `U.Transfer` flow valuation;
- edition, plane, or context pin;
- no-hidden-scalarization or set-return discipline;
- correspondence between functional structure and flow/transduction structure;
- generated or extracted relation graph used as architecture-flow reliance.

If the sentence only says that work occurred, use A.15 or the governing work pattern. If the sentence only says that a graph exists, use E.18. If the sentence uses the graph as mathematical-lens reliance, use C.29.

#### C.30.TGA-FLOW-REL:4.2 - Relation to functional structure

`FunctionalStructureView@Context` under C.30.ASV may cite `ArchitectureFlowStructureRelation@TGA` when flow is live. That relation does not make the TGA graph a functional element. It says that a functional structure view corresponds to or is declared relative to one E.18 graph/path/crossing relation.

```text
FunctionFlowRelationNote:
functionalStructureViewRef:
flowTransductionStructureViewRef:
architectureFlowStructureRelationRef:
functionOrEffect:
pathOrSliceRef:
crossingBundleRef:
preservedStructure:
lostOrHiddenStructure:
admissibleUse:
nonAdmissibleUse:
```

Use this note when the practitioner needs to see whether the function-flow relation changes inspection, split, relation-making, downgrade, exact governing pattern application, candidate generation, or stop.

#### C.30.TGA-FLOW-REL:4.3 - Exact claim-kind applications

| Live claim kind | Governing pattern to apply |
| --- | --- |
| Work occurrence or work result | `A.15` and the governing work-result or P2W relation |
| Gate decision | `A.21` |
| Evidence claim | `A.10` or `G.6` |
| Assurance claim | `B.3` |
| Causal flow or intervention claim | `C.28` |
| Mathematical-lens adequacy | `C.29` |
| Architecture description or view adequacy | `C.30` or `C.30.ASV` |
| Function-like wording | `A.6.F` |
| Interface/signature/module compatibility | `InterfaceSignatureBoundaryNote` or the exact module/interface repair pattern when live |
| Architecture decision | the exact project-side architecture decision pattern when live |

#### C.30.TGA-FLOW-REL:4.4 - E.18:5.12 boundary statement

For the E.TGA-governed flow/transduction structure kind of an architecture description, an architecture-flow description may consist of an E.TGA transduction graph over the described holon plus MVPK faces and correspondences.

Generic architecture description is governed by C.30. E.TGA supplies the flow/transduction substrate and does not define all architecture structure kinds.

This is the E.18:5.12 boundary statement. It is not a TGA rewrite and not a second E.TGA source of truth.

#### C.30.TGA-FLOW-REL:4.5 - Worked slices

**Functional architecture with live flow.** A team says, "The functional architecture is this TGA graph." The repair is:

```text
functionalStructureViewRef: required effects and dependencies
flowTransductionStructureViewRef: flow/path/crossing structure
transductionGraphRef: E.18 graph
activePathOrSliceRefs: current path slices used for the architecture claim
correspondenceRefs: functional effect to flow path relation
nonAdmissibleUse:
  graph as functional architecture itself,
  graph as work occurrence,
  graph as evidence sufficiency,
  graph as gate result,
  graph as project decision
```

**Neural-network dataflow change.** Replacing attention, SSM, convolution, memory/cache, MoE expert-selection, or another block changes architecture only when the changed structure kind and flow/transduction relation are named. A benchmark, ablation, or pruning result may bear on an exact non-architecture claim, but it does not make the flow relation an architecture decision or evidence sufficiency by itself.

**Code-agent relation graph.** A code-agent relation graph with `IMPORTS`, `CALLS_API`, `REGISTRY_WIRES`, or `DATA_FLOWS_TO` edges can be used for an architecture-flow relation only with source edition, observed/inferred/unknown status, typed relation semantics, unexplored regions, and source-return condition when subsequent action relies on hidden distinctions.

