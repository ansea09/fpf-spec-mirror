---
chunk_kind: "child"
pattern_id: "E.18.2"
pattern_title: "Transformation Flow Mathematical Description"
section_id: "E.18.2:4"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/E.18.2/E.18.2__005_solution.md"
commit_sha: "9dd9215969126625d449a40e8ca4d1df9ac903f8"
heading_path:
  - "E.18.2 — Transformation Flow Mathematical Description"
  - "E.18.2:4 — Solution"
line_start: 84191
line_end: 84263
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
  RelatedGovernedClaimRef?:
```

Exactly one of `DescribedTransformationFlowStructureRef?` and `DescribedTransformationFlowStructureNetworkRef?` is present. The first points to one E.18 TFS; the second points to one already selected E.18.NET network. `DescribedSliceOrLocusRef?` may cite an existing path, slice, `FlowPositionRef`, `ExposedFlowPositionRef`, member path, E.18.NET `NetworkCrossFlowRelationRowRef`, or other governed part without copying its owner's fields. `CandidateMathObject` and `ExpressionKind` name the graph, algebra, category, tuple, morphism, quotient, fold, refinement, factorization, wiring, matrix, network expression, or related mathematical object. `PreservedStructure`, `LostStructure`, `DeclaredUse`, and `BoundaryStop` follow the C.29 discipline when the expression is claim-bearing. `PublicationFaceRef?` points to a separate E.17 publication; `RelatedGovernedClaimRef?` points to a separate relation record only when a stronger claim is current. Neither is a local authority slot.

#### E.18.2:4.2 - Expression families

| Expression family | Use when it describes | Required boundary |
|---|---|---|
| graph, hypergraph, network expression, DSM, DMM, MDM, or matrix | dependency, internal transfer, exact cross-member relation, adjacency, interface placement, clustering, or change propagation inside one selected TFS or across one selected TFS network | not the selected TFS or network; E.18 and E.18.NET own those ontic subjects, while E.18.2 owns this description; not work occurrence, gate passage, or evidence |
| mathematical path or path slice | reachability, carried relation, currentness slice, refresh locality, or crossing-local replay | not a project procedure or performed sequence |
| tuple, record, slot relation, or typed relation expression | slot positions, relation arity, locus typing, and value placement | not a new U-kind and not a replacement for A.6.5 slot discipline |
| morphism, composition, category, operad, optic, or wiring expression | composition, interface, substitution, transfer law, or decomposition of selected transformations | not proof that the represented work can be performed or that interfaces are semantically compatible |
| quotient, fold, coarsening, refinement, or factorization | coarser/finer partitioning, aggregation, retained/lost structure, and alternative decomposition | not an identity claim without preserved/lost structure and return condition |
| algebra, semiring, equation system, or constraint system | operation law, conservation, admissible composition, or constraint propagation over the selected structure | not a mechanism, formal substrate, or empirical law unless `A.6.0` governs the formal substrate, `A.6.1` governs the postulate or principle frame, and the relevant evidence pattern is current |
| learned representation, embedding, simulation object, or differentiable surrogate | approximate structure, optimization, similarity, or predictive proxy over transformation-flow structure | not architecture adequacy, OOD guarantee, causal proof, or release readiness by itself |

These families are prompts for recovery, not a taxonomy of new FPF kinds. A local expression may combine several families; the record still names exactly one selected TFS or network subject, one current described part when relevant, and the declared use.

#### E.18.2:4.3 - Five-way subject, description, lens, and publication discriminator

Use this discriminator before writing or accepting a mathematical description:

```text
If the claim selects one TFS or its internal flow structure, use E.18.
If the claim selects independently identified TFS or nested-network members plus exact cross-member relations, use E.18.NET.
If the claim describes exactly one selected TFS or network with mathematics, use E.18.2.
If the claim evaluates that mathematical lens use, use C.29 with the E.18.2 description reference.
If the claim publishes a graph, table, equation, diagram, card, or other face, use E.17 and the governing view or architecture-description pattern.
```

The same visible source may require several records, but each E.18.2 description chooses one described ontic subject branch. A refrigerator principle scheme may include an E.17 publication face, a functional-architecture view, one selected E.18 TFS, a thermodynamic mechanism claim, and an E.18.2 graph or equation description. A network diagram may similarly publish an E.18.2 description of one already selected E.18.NET network. If the expression is evaluated as a lens, C.29 governs adequacy; if it is rendered or published, E.17 governs that publication. Neither record reidentifies the TFS or network.


#### E.18.2:4.4 - Related governed claims

E.18.2 does not carry authority for related governed claims. Use the direct governing pattern when the current claim is:

| Current claim | Use |
|---|---|
| one bounded change under conditions | `A.3.4` |
| one selected transformation-flow structure, flow valuation, path, slice, crossing, or refresh locus | `E.18` |
| one selected network of independently identified TFS or nested-network members and exact cross-member relations | `E.18.NET` |
| selected transformation-flow unfolding structure with constraints, guards, preserved/lost structure, and direct exits | `E.18.3` |
| mathematical-lens adequacy, preserved/lost structure, payoff, or stop condition | `C.29` |
| method, method description, mechanism, signature, work plan, or performed work | `A.3.1`, `A.3.2`, `A.6.1`, `A.6.0`, `A.15.2`, or `A.15.1` |
| evidence, assurance, gate, release, or decision | `A.10`, `B.3`, `A.20`, `A.21`, or `C.11` |
| architecture, structural view, functional structure, module interface, or reusable-structure claim | `C.30`, `C.30.ASV`, `A.6.F`, `A.6.M`, or `C.31` |
| publication face or publication use | `E.17` or `E.17.EFP` |

