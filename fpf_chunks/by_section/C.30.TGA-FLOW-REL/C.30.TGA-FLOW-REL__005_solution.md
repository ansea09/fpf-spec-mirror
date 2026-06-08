---
chunk_kind: "child"
pattern_id: "C.30.TGA-FLOW-REL"
pattern_title: "Architecture-TGA Flow-Structure Relation"
section_id: "C.30.TGA-FLOW-REL:4"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/C.30.TGA-FLOW-REL/C.30.TGA-FLOW-REL__005_solution.md"
commit_sha: "b22b6993b3e94f7896d5dc1cd011af7bc3f49b0d"
heading_path:
  - "C.30.TGA-FLOW-REL — Architecture-TGA Flow-Structure Relation"
  - "C.30.TGA-FLOW-REL:4 — Solution"
line_start: 54420
line_end: 54565
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

### C.30.TGA-FLOW-REL:4 - Solution

C.30.TGA-FLOW-REL is the C.30 entry relation to E.18 when a grounded architecture claim, selected architecture-relevant structure, architecture structural view, or conditional architecture description uses E.TGA graph, path, crossing, or flow-valuation objects as a flow or transduction structure relation.

It supplies only the architecture-flow relation:

```text
ArchitectureFlowStructureRelation@TGA ::= {
  architectureClaimRef?,
  selectedArchitectureStructureRefs?,
  architectureStructuralViewRef?,
  architectureDescriptionRef?,
  functionalStructureViewRef?,
  flowTransductionStructureViewRef?,
  transductionGraphRef?,
  selectedPathOrSliceRefs?,
  crossingBundleRefs?,
  flowValuationRefs?,
  correspondenceRefs?,
  sourceReturnCondition?,
  admissibleUse,
  nonAdmissibleUse
}
```

At least one architecture-side field and at least one E.18 object field must be named by value. Optional fields stay `not used` unless they change inspection, correspondence, source return, governing-pattern application, or stop.

#### C.30.TGA-FLOW-REL:4.1 - Use trigger

Use this pattern only when a `ArchitectureOf@Context` claim being made, selected architecture-relevant structure, architecture structural view, functional-structure view, flow-structure claim, or conditional `ArchitectureDescription@Context` use depends on one or more E.18 objects:

- `TransductionGraphRef`;
- `PathId` or `PathSliceId`;
- `CrossingBundleRef`;
- `U.Transfer` flow valuation;
- edition, plane, or context pin;
- no-hidden-scalarization or set-return discipline;
- correspondence between functional structure and flow or transduction structure;
- generated or extracted relation graph used as architecture-flow reliance.

If the sentence only says that work occurred, use A.15 or the governing work pattern. If the sentence only says that a graph exists, use E.18. If the sentence uses the graph as mathematical-lens reliance, use C.29.

#### C.30.TGA-FLOW-REL:4.2 - Relation to functional structure

`FunctionalStructureView@Context` under C.30.ASV may cite `ArchitectureFlowStructureRelation@TGA` when a flow relation is being used. That relation does not make the TGA graph a functional element. It says that a functional structure view corresponds to or is declared relative to one E.18 graph, path, or crossing relation.

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

Use this note when the practitioner needs to see whether the function-flow relation changes inspection, split, relation-making, downgrade, claim named by value-governance assignment, candidate generation, or stop.

#### C.30.TGA-FLOW-REL:4.3 - Claim-kind applications named by value

| Claim kind being made | Governing pattern to apply |
| --- | --- |
| Work occurrence or work result | `A.15` and the governing work-result or P2W relation |
| Gate decision | `A.21` |
| Evidence claim | `A.10` or `G.6` |
| Assurance claim | `B.3` |
| Causal flow or intervention claim | `C.28` |
| Mathematical-lens use | `C.29` |
| Architecture description or view adequacy | `C.30` or `C.30.ASV` |
| Function-like wording | `A.6.F` |
| Interface, signature, or module compatibility | `InterfaceSignatureBoundaryNote` or the module-and-interface repair pattern when the corresponding claim is being made |
| Architecture decision | the project-side architecture decision pattern when the corresponding claim is being made |


This table is the single boundary for generic non-flow claims. Elsewhere in this pattern, keep only local false positives that the TGA relation itself makes tempting: graph-as-architecture, graph-as-functional-architecture, flow-as-work-log, crossing-as-gate, valuation-as-score, generated relation-graph proof, and prompt-data-tool flow as authority proof.

#### C.30.TGA-FLOW-REL:4.4 - E.18:5.12 boundary statement

For an E.TGA-governed flow or transduction structure kind used by `ArchitectureOf@Context`, selected architecture-relevant structure, architecture structural view, or conditional `ArchitectureDescription@Context`, an architecture-flow relation may cite an E.TGA transduction graph over the described holon plus MVPK faces and correspondences.

Grounded architecture adequacy and conditional architecture-description use are governed by C.30. E.18 supplies the flow or transduction structure objects and relations; it does not define all architecture structure kinds.

This is the E.18:5.12 boundary statement. It is not a TGA rewrite and not a second E.TGA source of truth.

#### C.30.TGA-FLOW-REL:4.5 - Worked slices

**Functional architecture with a flow relation being claimed.** A team says, "The functional architecture is this TGA graph." The repair is:

```text
functionalStructureViewRef: required effects and dependencies
flowTransductionStructureViewRef: selected E.18 graph structure, path structure, crossing structure, or flow-valuation structure
transductionGraphRef: E.18 graph
selectedPathOrSliceRefs: path slices used for the architecture claim
correspondenceRefs: functional effect to flow path relation
nonAdmissibleUse:
  graph as functional architecture itself,
  graph as work occurrence,
  graph as evidence sufficiency,
  graph as gate result,
  graph as project decision
```

Filled relation record:

```text
ArchitectureFlowStructureRelation@TGA:
architectureClaimRef: ArchitectureOf@CheckoutServiceContext
selectedArchitectureStructureRefs: selected request-handling and payment-authorization flow structure
architectureStructuralViewRef: ArchitectureStructuralView@CheckoutRuntimeFlow
architectureDescriptionRef: not used; the durable architecture description is not being evaluated here
functionalStructureViewRef: FunctionalStructureView@CheckoutRequiredEffects
flowTransductionStructureViewRef: FlowTransductionStructure@PaymentAuthorizationPath
transductionGraphRef: TransductionGraph@Checkout-v3
selectedPathOrSliceRefs: PathSlice@request-to-payment-authorization
crossingBundleRefs: not used
flowValuationRefs: not used
correspondenceRefs: required effect `authorize payment` corresponds to the E.18 path slice; this is correspondence, not identity
sourceReturnCondition: reopen if graph edition, path slice, source observation class, or required-effect declaration changes
admissibleUse: inspect whether the functional structure view depends on the E.18 path slice being used and whether an architecture split or correspondence note is needed
nonAdmissibleUse: graph as functional architecture itself; graph as work occurrence; graph as evidence sufficiency; graph as gate result; graph as project decision
```

Near miss: if the graph has no C.30-side architecture reference named by value, the case stays in `E.18`. If the same sentence is a work log, evidence claim, gate decision, or benchmark result, that non-flow claim is governed by its governing pattern and this relation keeps only the architecture-flow relation.

**Neural-network dataflow change.** Source labels such as attention block, SSM block, convolution block, memory mechanism, cache mechanism, and MoE expert-selection go through `C.30.STRAT` unless the changed item is already recovered. C.30.TGA-FLOW-REL applies only when the changed structure kind and flow or transduction relation are named. A benchmark, ablation, or pruning result may bear on an non-architecture claim named by value, but it does not make the flow relation an architecture decision or evidence sufficiency by itself.

**Code-agent relation graph.** A code-agent relation graph with `IMPORTS`, `CALLS_API`, `REGISTRY_WIRES`, or `DATA_FLOWS_TO` edges can be used for an architecture-flow relation only with source edition, a source observation class selected from {observed, inferred, unknown}, typed relation semantics, unexplored regions, and source-return condition when subsequent action relies on hidden distinctions.

#### C.30.TGA-FLOW-REL:4.6 - Lowering and currentness conditions

Lower, narrow, or reopen the relation at the smallest changed locus when:

- E.18 graph, path, crossing, or flow-valuation semantics change;
- edition, plane, context pin, set-return, or no-hidden-scalarization discipline changes;
- source graph edition, path slice, source observation class, source pin, unexplored region, or source-return condition changes;
- the C.30 architecture locus, selected architecture-relevant structure, architecture structural view, conditional architecture description, or C.30.ASV relation changes;
- functional-flow correspondence changes;
- a non-flow claim is being made and is governed by `C.30.TGA-FLOW-REL:4.3` rather than by this relation;
- C.29, C.16, C.28, A.10, G.6, B.3, A.20, A.21, A.15, C.30, C.30.ASV, A.6.F, C.30.STRAT, or E.18 changes the governing boundary used by the relation.

Admissible repair results are: update the affected reference, add or change correspondence, add or change source-return condition, narrow admissible use, keep the graph claim inside E.18, apply the governing pattern to a non-flow claim, lower to quote-only or reduced-use cue, or block the architecture-flow use.

