---
chunk_kind: "parent"
pattern_id: "C.30.TGA-FLOW-REL"
pattern_title: "Architecture-TGA Flow-Structure Relation"
section_id: null
section_title: null
source_path: "FPF-Spec.md"
output_path: "by_pattern/C.30.TGA-FLOW-REL.md"
commit_sha: "21e2101c100964de121c37408b37563ee0cdbf8c"
heading_path:
  - "C.30.TGA-FLOW-REL — Architecture-TGA Flow-Structure Relation"
line_start: 54181
line_end: 54471
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

## C.30.TGA-FLOW-REL - Architecture-TGA Flow-Structure Relation

> **Type:** Architectural pattern
> **Status:** Stable
> **Normativity:** Normative unless explicitly marked informative

### C.30.TGA-FLOW-REL:1 - Problem frame

Use this pattern when an architecture discussion depends on a Transduction Graph Architecture (TGA) graph, path, path slice, crossing, flow valuation, edition pin, plane pin, context pin, or no-hidden-scalarization claim.

The first useful move is small. `ArchitectureFlowStructureRelation@TGA` is a C.30-side relation record for a relation being used between `ArchitectureOf@Context`, selected architecture-relevant structure, architecture structural view, or conditional `ArchitectureDescription@Context` use and the E.18 graph, path, crossing, or flow-valuation relation being used for flow or transduction structure. It names the architecture locus, selected structure or view reference when used in the relation, conditional description reference when durable description use is being made, the E.18 object, correspondence or source-return condition when used in the relation, and the admissible architecture use.

```text
ArchitectureFlowStructureRelation@TGA:
architectureClaimRef?:
selectedArchitectureStructureRefs?:
architectureStructuralViewRef?:
architectureDescriptionRef?:
functionalStructureViewRef?:
flowTransductionStructureViewRef?:
transductionGraphRef?:
selectedPathOrSliceRefs?:
crossingBundleRefs?:
flowValuationRefs?:
correspondenceRefs?:
sourceReturnCondition?:
admissibleUse:
nonAdmissibleUse:
```

Ordinary minimum: name at least one architecture-side reference (`architectureClaimRef`, `selectedArchitectureStructureRefs`, `architectureStructuralViewRef`, or `architectureDescriptionRef` when durable description use is being made), at least one E.18 object reference (`transductionGraphRef`, `selectedPathOrSliceRefs`, `crossingBundleRefs`, or `flowValuationRefs`), the architecture-flow `FlowTransductionStructure`, one blocked overread, and stop or governing-pattern application. Use functional-structure, flow-structure, crossing, flow-valuation, correspondence, and source-return fields only when they change the next architecture move. All other fields are conditional and may be `not used`.

Use this relation only when a grounded architecture claim, selected architecture-relevant structure, architecture structural view, functional-architecture view, flow-structure claim, or conditional architecture-description use depends on an E.18 graph, path, crossing, or valuation relation. Stop when the architecture-flow relation and non-admissible uses are clear. If another claim is being made, that claim is governed by its governing pattern and this relation remains only the architecture-flow relation.

What goes wrong if this pattern is missed: a TGA graph becomes functional architecture, whole architecture ontology, performed-work occurrence, work-result record, proof, or project decision by appearance.

What this buys in practice: the practitioner can use E.18 for flow or transduction structure while C.30 remains the grounded architecture and selected-structure adequacy locus and C.30.ASV remains the architecture-structural-view locus.

Not this pattern when the question under repair is a graph, path, crossing, or flow valuation without a relation being used for grounded architecture adequacy, conditional architecture-description use, or an architecture structural view. Use E.18 directly. If the question under repair is an architecture claim or durable architecture description without an E.TGA graph claim, path claim, or crossing claim kind, use C.30. If it is a functional view without flow relation or TGA claim kind, use C.30.ASV and A.6.F. If another claim being made is present, use the governing pattern and keep C.30.TGA-FLOW-REL only to the architecture-flow relation.

### C.30.TGA-FLOW-REL:2 - Problem

Grounded architecture claims, selected architecture-relevant structures, architecture structural views, and conditional architecture descriptions often need E.18 objects when they discuss flow or transduction structure, functional dependencies, data movement, control paths, evidence flows, neural-network dataflow, or code-agent relation graphs.

C.30.TGA-FLOW-REL prevents that collapse by requiring the selected architecture-side reference, such as `ArchitectureOf@Context`, structure ref, structural view, or conditional description use, before any E.18-governed graph, path, or crossing object gets architecture use.

### C.30.TGA-FLOW-REL:3 - Forces

| Force | Tension |
| --- | --- |
| Flow relation vs architecture takeover | E.TGA graph, path, or crossing relation can be essential, but it does not become all architecture ontology. |
| Functional view vs flow view | A functional structure view may need a flow relation, but a graph, path, or crossing object is not a functional element by itself. |
| Graph precision vs work overread | E.18 gives precise graph, path, and flow-valuation objects; work occurrence and work results remain outside TGA unless their own pattern governs the claim being made. |
| No-hidden-scalarization vs architecture scoring | E.18 set-return and no-hidden-scalarization discipline can inform architecture reasoning, but it does not become a general architecture score. |
| Small relation vs unneeded non-architecture apparatus | A project often needs one relation record, not a full C.29 lens card, evidence path, assurance case, or decision record. |
| E.18 stability vs C.30 integration | A TGA-based architecture claim, selected flow or transduction structure, architecture structural view, or conditional architecture-description use needs a relation to E.18 without rewriting E.TGA as generic architecture adequacy theory. |

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

### C.30.TGA-FLOW-REL:5 - Archetypal Grounding

| Tell-Show-Show row | Grounding |
| --- | --- |
| Tell | A practitioner sees a graph or path and wants to use it for a grounded architecture claim, selected architecture-relevant structure, architecture structural view, or conditional architecture description. C.30.TGA-FLOW-REL asks whether the graph is E.18-governed flow or transduction relation for the selected architecture locus, and names its non-admissible uses. |
| Show: `U.System` | A software system, plant, AI agent, neural network, vehicle, or supply chain may have flow or transduction structure. The graph can inform architecture reasoning about that structure without carrying the non-flow claims named in `C.30.TGA-FLOW-REL:4.3`. |
| Show: `U.Episteme` | A TGA graph, generated relation graph, code-agent probe, neural-network diagram, dashboard, or architecture note is an episteme, view, or publication. It can publish or substantiate the flow relation only when its E.18 object, context pins, correspondence, source-return condition, and admissible use are recoverable. |

### C.30.TGA-FLOW-REL:6 - Bias-Annotation

Lenses tested: **Arch**, **Onto**, **Epist**, **Prag**, **Did**, **Gov**. Scope: architecture-flow relations using E.18 objects.

| Bias risk | Mitigation |
| --- | --- |
| Graph-as-architecture bias | The pattern states that grounded architecture adequacy and conditional architecture-description use stay with C.30, while structural views stay with C.30.ASV. |
| Function-flow collapse | Functional structure and flow or transduction structure are related, not identical. |
| Non-flow claim overread | The relation table assigns non-flow claim kinds to their governing patterns. |
| Mathematical overread | Mathematical-lens use of a graph or valuation is governed by C.29. |
| Check-only bias | Conformance checks include repair moves and stop conditions. |

This checklist verifies the preceding guidance after the practitioner has chosen the selected move; it is not a required project control form and not a substitute for the card, note, relation, or repair move above.

### C.30.TGA-FLOW-REL:7 - Conformance Checklist

| ID | Requirement | Failed-check repair |
| --- | --- | --- |
| **CC-TGA-FLOW-1 E.18 object.** | The relation names the E.18 graph, path, slice, crossing, or flow valuation object it uses. | Add the E.18 object reference named by value or use C.30 or C.30.ASV without TGA relation.
 |
| **CC-TGA-FLOW-2 Architecture locus.** | The relation names `ArchitectureOf@Context`, selected architecture-relevant structure, architecture structural view, or conditional `ArchitectureDescription@Context` use it relates to. | Add `architectureClaimRef`, `selectedArchitectureStructureRefs`, `architectureStructuralViewRef`, or `architectureDescriptionRef` when durable description use is being made; otherwise keep the graph claim inside E.18 only. |
| **CC-TGA-FLOW-3 Functional and flow separation.** | Functional structure and flow or transduction structure remain separate unless a correspondence is declared. | Add `FunctionFlowRelationNote` or remove the functional-architecture claim from the graph sentence. |
| **CC-TGA-FLOW-4 No TGA architecture takeover.** | The TGA graph is not treated as generic architecture ontology or all architecture structure kinds. | Assign grounded architecture claims, selected architecture-relevant structures, or conditional architecture-description use to C.30 and keep this pattern to flow or transduction structure. |
| **CC-TGA-FLOW-5 No work overread.** | A graph, path, or slice is not treated as work occurrence or work result. | Assign the work claim to A.15 or the governing work-result pattern. |
| **CC-TGA-FLOW-6 No evidence, assurance, or gate overread.** | The relation is not used as evidence sufficiency, assurance claim, gate decision, or release permission without evidence named by value, assurance, gate, or release pattern application. | Assign the claim being made to A.10, G.6, B.3, A.20, A.21, or the release locus named by value when a release claim is being made. |
| **CC-TGA-FLOW-7 Causal and mathematical boundaries.** | Causal or intervention claims and mathematical-lens claims are assigned to C.28 and C.29. | Apply those governing patterns or narrow the relation's admissible use. |
| **CC-TGA-FLOW-8 Pin and scalarization boundary.** | Edition, context, and plane pins plus no-hidden-scalarization claims remain E.18-governed. | Add E.18 pin and set-return references or remove the comparison or selection claim. |
| **CC-TGA-FLOW-9 Source return.** | Extracted, generated, coarsened, or partial graphs state source-return conditions when hidden distinctions affect action. | Add source-return condition or narrow the admissible use. |
| **CC-TGA-FLOW-10 Useful action.** | The repair leaves a surviving move: name graph, path, or crossing relation; add correspondence; return to source; assign the claim being made to a governing pattern; or stop. | Restore that move, or classify the phrase as reduced-use cue, quote-only wording, blocked transfer, or incomplete rewrite. |
| **CC-TGA-FLOW-11 Lowering and currentness.** | The relation states the smallest changed locus when E.18 semantics or pins, source observation class, architecture locus, correspondence, source return, or neighboring governing boundary changes. | Update the affected reference, narrow admissible use, keep the graph claim inside E.18, apply the governing pattern to the non-flow claim, lower the relation, or block architecture-flow use. |

### C.30.TGA-FLOW-REL:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Symptom | Repair |
| --- | --- | --- |
| **Graph-as-architecture** | The E.18 graph is called the architecture. | Use C.30 for the grounded architecture claim, selected architecture-relevant structure, or conditional architecture description, and keep this relation only for flow or transduction structure. |
| **Graph-as-functional-architecture** | A TGA graph is treated as the functional architecture itself. | Split functional structure from flow or transduction structure and add correspondence. |
| **Flow-as-work-log** | Path or slice wording is treated as work occurrence. | Assign occurrence or result claims to A.15 or P2W and keep TGA as graph or path relation. |
| **Crossing-as-gate-result** | A crossing relation is treated as gate passage. | Assign gate-decision claims to A.21 and keep crossing relation under E.18. |
| **Valuation-as-score** | A flow valuation is used as a generic architecture score. | State E.18 valuation and set-return discipline; assign measurement, characterization, selection, or candidate-set claims to `C.16` or an admitted governing pattern when those claims are being made. |
| **Generated relation-graph proof** | A code-agent relation graph or probe output is used as proof of architecture understanding or safety. | Recover source, source observation class selected from {observed, inferred, unknown}, hidden structure, and evidence or assurance pattern governing the claim applications. |
| **Prompt-data-tool flow as authority proof** | A prompt, data, or tool-flow graph is treated as permission for tool action or proof that authority is safe. | Keep the graph as a flow relation. A path from untrusted content to tool action is governed by `SecurityTrustBoundaryStructure`, C.24, E.16, A.20, or A.21 when those claim kinds are being made. |

### C.30.TGA-FLOW-REL:9 - Consequences

| Benefit | Cost or trade-off |
| --- | --- |
| E.18 graph, path, and crossing discipline becomes usable for grounded architecture claims, selected architecture-relevant structures, architecture structural views, and conditional architecture descriptions. | A conforming use names the C.30 architecture record, selected structure ref, C.30.ASV structural-view reference, or conditional architecture-description ref that uses the TGA relation. |
| Functional structure and flow or transduction structure stay separable. | Concise "the graph is the architecture" prose is repaired before it is used for an FPF claim kind or admissible-use boundary. |
| Non-flow claim kinds are assigned to their governing patterns. | More governing patterns are named when practitioners try to overuse the graph. |
| The E.18:5.12 boundary statement stays narrow. | Generic architecture adequacy remains outside E.18. |

### C.30.TGA-FLOW-REL:10 - Rationale

E.TGA is already the governing FPF pattern for transduction graphs, paths, crossings, flow valuations, and related pins. Architecture needs to use that work without letting it become generic architecture ontology. The smallest stable relation is therefore a C.30-side record that points to E.18 objects and states admissible and non-admissible architecture use.

This pattern also protects functional architecture. A functional structure view may correspond to flow or transduction structure, but function and flow are different structure kinds. The relation is useful precisely because it preserves that difference while allowing correspondence.

### C.30.TGA-FLOW-REL:11 - SoTA-Echoing

| Practice or source line | C.30.TGA-FLOW-REL adoption | Action consequence | Boundary |
| --- | --- | --- | --- |
| E.18 E.TGA graph, path, crossing, and flow-valuation discipline | Adopt E.18 as the governing source for graph, path, crossing, and valuation objects. | The pattern names E.18 references rather than redefining graph or flow semantics. | E.18 does not become generic architecture ontology or architecture-description ontology. |
| ISO/IEC/IEEE 42010:2022 and multi-view architecture practice | Adapt view and correspondence discipline to architecture-flow reliance. | Flow or transduction views relate to grounded architecture claims, selected architecture-relevant structures, architecture structural views, or conditional architecture descriptions through C.30, C.30.ASV, and correspondence refs. | Architecture views do not become proof, evidence, gates, or decisions. |
| MBSE and SysML v2 view and relation practice | Adapt model-derived flow views and path views as Description-episteme source relations. | A model-derived flow view states source, selection, hidden or lost structure, and admissible use. | Tool models do not override FPF E.18 or C.30 relations. |
| Neural-network dataflow and GonzoML architecture-operation corpus | Adopt practitioner flow-structure recognition for block replacement, path-selection, memory and cache placement, MoE expert-selection, pruning, distillation, ablation, and compute, memory, and latency tradeoffs. | Keep block, cache, expert, router, gate, and similar words as `C.30.STRAT` source labels until the flow or transduction structure is recovered; C.30.TGA-FLOW-REL applies only when that recovered structure changes the architecture move. | Benchmarks, ablations, pruning masks, or architecture-search outputs do not become evidence sufficiency, assurance, gate passage, or architecture decision by themselves. |
| Theory of Code Space and arXiv:2603.00601 code-agent relation graph probing | Adapt relation graphs with source observation class selected from {observed, inferred, unknown} and partial-observability warnings. | Generated code relation graphs can be used for flow relation only with typed relation semantics, source pins, unexplored regions, and source return. | Do not mint `U.CodeSpace`; do not treat probe output as internal belief proof, architecture adequacy, assurance, or release evidence or release claim. |

**Currentness front.** The governing currentness sources are E.18 object semantics and pins, C.30 and C.30.ASV architecture-side relation law, the source observation class, and the non-flow governing patterns named in `C.30.TGA-FLOW-REL:4.3`. When one changes, the relation changes only at the affected reference, correspondence, source-return condition, admissible-use boundary, or governing-pattern assignment.

### C.30.TGA-FLOW-REL:12 - Relations

Builds on: `C.30`, `C.30.ASV`, `A.22`, `A.6.F`, `E.18`, `E.17`, `E.17.0`, `A.7`, `E.10`, `C.2.P`, and `F.18`.

Coordinates with: `C.30.STRAT`, `A.15`, `A.20`, `A.21`, `A.10`, `G.6`, `B.3`, `C.28`, `C.29`, `C.16`, admitted measurement, selection, or candidate-set governing patterns when those claims are being made, `InterfaceSignatureBoundaryNote`, and the module-and-interface repair pattern when a module or interface claim is being made.

Neighboring claims stay with their governing patterns: `C.30.STRAT` for stratification wording and source-label repair, `E.18` for graph, path, crossing, and flow-valuation discipline, `C.30` for grounded architecture and selected-structure adequacy, `C.30.ASV` for architecture structural-view adequacy, `A.6.F` for function-use repair, and the non-flow governing patterns named in `C.30.TGA-FLOW-REL:4.3`. `C.30.TGA-FLOW-REL` governs only the architecture-TGA flow-structure relation being claimed.

### C.30.TGA-FLOW-REL:End

