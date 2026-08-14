---
chunk_kind: "child"
pattern_id: "E.18.2"
pattern_title: "Transformation Flow Mathematical Description"
section_id: "E.18.2:4"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/E.18.2/E.18.2__005_solution.md"
commit_sha: "646b41f84ffef4918ad9bdb34e7b450f0c4903ee"
heading_path:
  - "E.18.2 — Transformation Flow Mathematical Description"
  - "E.18.2:4 — Solution"
line_start: 85283
line_end: 85368
dependencies:
  - "A.10"
  - "A.15"
  - "A.20"
  - "A.21"
  - "A.3.4"
  - "A.6.0"
  - "A.6.5"
  - "B.3"
  - "C.2.1"
  - "C.29"
  - "C.30"
  - "C.30.TFS-REL"
  - "E.17"
  - "E.18"
  - "E.18.1"
  - "E.18.3"
  - "E.18.NET"
  - "U.Episteme"
  - "U.Signature"
  - "U.Transformation"
keywords:
---

### E.18.2:4 - Solution

Write a `TransformationFlowMathematicalDescription@Context` only when the mathematical expression changes the current transformation-flow description move. Name exactly one described ontic subject: one E.18 TFS or one E.18.NET network. Keep that subject reference, the mathematical description, any C.29 lens-use judgment, and any E.17 publication face separate. Then decide whether the C.29 lens-use card is needed for adequacy, payoff, preserved/lost structure, or boundary.

#### E.18.2:4.1 - First-use record

Use this compact record for ordinary cases:

```text
TransformationFlowMathematicalDescription@Context:
  # exactly one described ontic subject branch is present:
  DescribedTransformationFlowStructureRef?:
  DescribedTransformationFlowStructureNetworkRef?:
  DescribedSliceOrLocusRef?:
  CandidateMathObject:
  ExpressionKind:
  MappingMode:
  PreservedStructure:
  LostStructure:
  DeclaredUse:
  BoundaryStop:
  C29LensUseRef?:
  PublicationFaceRef?:
```

Exactly one of `DescribedTransformationFlowStructureRef?` and `DescribedTransformationFlowStructureNetworkRef?` is present. The first points to one E.18 TFS; the second points to one already selected E.18.NET network. `DescribedSliceOrLocusRef?` may cite an existing path, slice, `FlowPositionRef`, `ExposedFlowPositionRef`, member path, E.18.NET `NetworkCrossFlowRelationRowRef`, or other independently identified part without copying the fields that define that object. `CandidateMathObject` and `ExpressionKind` name the graph, algebra, category, tuple, morphism, quotient, fold, refinement, factorization, wiring, matrix, network expression, or related mathematical object. `PreservedStructure`, `LostStructure`, `DeclaredUse`, and `BoundaryStop` follow the C.29 discipline when the expression is claim-bearing. `PublicationFaceRef?` points to a separate E.17 publication. The compact record has no generic neighboring-object reference. When a neighboring claim is materially needed, cite its exact C.2.1 claim-bearing episteme in the subject-specific account; identify an ontic subject or relation occurrence only through a separately named, correctly typed reference supplied by the pattern for that claim.

#### E.18.2:4.2 - Expression families

| Expression family | Use when it describes | Required boundary |
|---|---|---|
| graph, hypergraph, network expression, DSM, DMM, MDM, or matrix | dependency, internal transfer, exact cross-member relation, adjacency, interface placement, clustering, or change propagation inside one selected TFS or across one selected TFS network | not the selected TFS or network: apply E.18's one-TFS identity and selection constraints or E.18.NET's membership, boundary, and cross-member relation rules to select that ontic subject; E.18.2 defines only this description; not work occurrence, gate passage, or evidence |
| mathematical path or path slice | reachability, carried relation, currentness slice, refresh locality, or crossing-local replay | not a project procedure or performed sequence |
| tuple, record, slot relation, or typed relation expression | slot positions, relation arity, locus typing, and value placement | not a new U-kind and not a replacement for A.6.5 slot discipline |
| morphism, composition, category, operad, optic, or wiring expression | composition, interface, substitution, transfer law, or decomposition of selected transformations | not proof that the represented work can be performed or that interfaces are semantically compatible |
| quotient, fold, coarsening, refinement, or factorization | coarser/finer partitioning, aggregation, retained/lost structure, and alternative decomposition | not an identity claim without preserved/lost structure and return condition |
| algebra, semiring, equation system, or constraint system | operation law, conservation, admissible composition, or constraint propagation over the selected structure | not a mechanism, formal substrate, or empirical law unless the formal substrate satisfies the A.6.0 declaration test, the postulate or principle frame satisfies the A.6.1 definition and application test, and the relevant evidence test is current |
| learned representation, embedding, simulation object, or differentiable surrogate | approximate structure, optimization, similarity, or predictive proxy over transformation-flow structure | not architecture adequacy, OOD guarantee, causal proof, or release readiness by itself |

These families are prompts for recovery, not a taxonomy of new FPF kinds. A local expression may combine several families; the record still names exactly one selected TFS or network subject, one current described part when relevant, and the declared use.

#### E.18.2:4.3 - Five-way subject, description, lens, and publication discriminator

Use this discriminator before writing or accepting a mathematical description:

```text
If the claim selects one TFS or its internal flow structure, use E.18.
If the claim selects independently identified TFS or nested-network members plus exact cross-member relations, use E.18.NET.
If the claim describes exactly one selected TFS or network with mathematics, use E.18.2.
If the claim evaluates that mathematical lens use, use C.29 with the E.18.2 description reference.
If the claim publishes a graph, table, equation, diagram, card, or other face, use E.17 and the relevant view or architecture-description pattern.
```

The same visible source may require several records, but each E.18.2 description chooses one described ontic subject branch. A refrigerator principle scheme may include an E.17 publication face, a functional-architecture view, one selected E.18 TFS, a thermodynamic mechanism claim, and an E.18.2 graph or equation description. A network diagram may similarly publish an E.18.2 description of one already selected E.18.NET network. If the expression is evaluated as a lens, apply the C.29 adequacy test; if it is rendered or published, identify the E.17 publication face and any current view or architecture-description membership. Neither record reidentifies the TFS or network.


#### E.18.2:4.4 - Related claims

E.18.2 defines only the mathematical-description relation. For any neighboring claim, use the row below that names the exact contribution needed now:

| Current claim | Use |
|---|---|
| one bounded change under conditions | Apply A.3.4's occurrence test and identity rule to identify the changed referent, boundary, actual change facts, and continuity or reidentification basis. |
| one selected transformation-flow structure, flow valuation, path, slice, crossing, or refresh locus | Apply E.18's identity, selection-constraint, and local-value rules to select that exact one-TFS structure and identify the local values used by the claim. |
| one selected network of independently identified TFS or nested-network members and exact cross-member relations | Apply E.18.NET's membership, boundary, and cross-member relation requirements to select the exact members and identify the obtaining cross-member relation occurrences. |
| one A.22-selected CGUS qualified through an independently identified E.18 substrate, with constraints and guarded alternatives whose applied-claim, E.18-event, or independently defined relation basis remains separate, plus preserved/lost structure, neighboring values connected by exact supporting relations, and stop or reconsideration questions | `E.18.3` qualifies that selected CGUS for this substrate use without identifying the substrate or neighboring values |
| mathematical-lens adequacy, preserved/lost structure, payoff, or stop condition | `C.29` returns the bounded lens-use result |
| method | Apply A.3.1's method criteria to identify the exact `U.Method`. |
| method-description membership | `A.3.2` tests one C.2.1 episteme against one admitted `U.Method` |
| mechanism or mechanism application | `A.6.1` supplies the mechanism declaration and exact application binding |
| formal-substrate signature | `A.6.0` supplies the profile-specific signature declaration |
| work plan | Apply A.15.2's plan-identity and intended-work rules to identify the plan and intended-work relations. |
| performed work | Apply A.15.1's occurrence and identity rules to identify the dated `U.Work` occurrence. |
| evidence use | `A.10` supplies the evidence relation for the named reliance |
| assurance use | `B.3` returns the bounded assurance result for that reliance |
| internal step validity | `A.20` returns the constraint-validity result |
| gate profile or decision | `A.21` supplies the gate profile, aggregation, decision, and publication minima |
| release | Apply A.15.1 to test and identify an actual release action as Work; test a separate subject-release claim with its named predicate or return the exact A.6.RCD result. |
| local choice | `C.11` returns the `ChoiceResult` |
| architecture | `C.30` carries the architecture claim |
| architecture structural view | `C.30.ASV` returns the structural-view adequacy result |
| functional structure | `A.6.F` supplies the exact function/bearer claim |
| module interface | `A.6.M` supplies the module-interface relation |
| reusable-structure characteristics | `C.31` carries the reusable-structure claim |
| publication face or explanation-faithfulness use | `E.17` supplies the publication face; `E.17.EFP` returns the explanation-faithfulness result |

