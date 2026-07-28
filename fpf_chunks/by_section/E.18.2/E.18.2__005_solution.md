---
chunk_kind: "child"
pattern_id: "E.18.2"
pattern_title: "Transformation Flow Mathematical Description"
section_id: "E.18.2:4"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/E.18.2/E.18.2__005_solution.md"
commit_sha: "4b75b56c13f5d61be5238fdbc7c20af5c6f89df7"
heading_path:
  - "E.18.2 — Transformation Flow Mathematical Description"
  - "E.18.2:4 — Solution"
line_start: 82549
line_end: 82617
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
  - "U.Episteme"
  - "U.Signature"
  - "U.Transformation"
keywords:
  - "C.29 boundary"
  - "algebraic description"
  - "graph expression"
  - "mathematical description"
  - "path expression"
  - "transformation-flow math"
---

### E.18.2:4 - Solution

Write a `TransformationFlowMathematicalDescription@Context` only when the mathematical expression changes the current transformation-flow description move. Keep the selected structure reference and the expression relation separate. Then decide whether the C.29 lens-use card is needed for adequacy, payoff, preserved/lost structure, or boundary.

#### E.18.2:4.1 - First-use record

Use this compact record for ordinary cases:

```text
TransformationFlowMathematicalDescription@Context:
  DescribedTransformationFlowStructureRef:
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

`DescribedTransformationFlowStructureRef` points to the selected E.18 structure. `DescribedSliceOrLocusRef?` names a path, slice, crossing, flow valuation, transformation locus, signature locus, mechanism locus, work-plan locus, work locus, evidence locus, result locus, or refresh locus when the expression describes only part of the structure. `CandidateMathObject` and `ExpressionKind` name the graph, algebra, category, tuple, morphism, quotient, fold, refinement, factorization, wiring, matrix, network, or related mathematical object. `PreservedStructure`, `LostStructure`, `DeclaredUse`, and `BoundaryStop` follow the C.29 discipline when the expression is claim-bearing. `RelatedGovernedClaimRef?` points to the separate relation record only when a stronger claim is being made; it is not a local authority slot.

#### E.18.2:4.2 - Expression families

| Expression family | Use when it describes | Required boundary |
|---|---|---|
| graph, hypergraph, network, DSM, DMM, MDM, or matrix | dependency, transfer, adjacency, interface placement, clustering, or change propagation inside a selected transformation-flow structure | not the selected structure unless E.18 says so; not work occurrence, gate passage, or evidence |
| mathematical path or path slice | reachability, carried relation, currentness slice, refresh locality, or crossing-local replay | not a project procedure or performed sequence |
| tuple, record, slot relation, or typed relation expression | slot positions, relation arity, locus typing, and value placement | not a new U-kind and not a replacement for A.6.5 slot discipline |
| morphism, composition, category, operad, optic, or wiring expression | composition, interface, substitution, transfer law, or decomposition of selected transformations | not proof that the represented work can be performed or that interfaces are semantically compatible |
| quotient, fold, coarsening, refinement, or factorization | coarser/finer partitioning, aggregation, retained/lost structure, and alternative decomposition | not an identity claim without preserved/lost structure and return condition |
| algebra, semiring, equation system, or constraint system | operation law, conservation, admissible composition, or constraint propagation over the selected structure | not a mechanism, formal substrate, or empirical law unless `A.6.0` governs the formal substrate, `A.6.1` governs the postulate or principle frame, and the relevant evidence pattern is current |
| learned representation, embedding, simulation object, or differentiable surrogate | approximate structure, optimization, similarity, or predictive proxy over transformation-flow structure | not architecture adequacy, OOD guarantee, causal proof, or release readiness by itself |

These families are prompts for recovery, not a taxonomy of new FPF kinds. A local expression may combine several families; the record still names one selected structure, one current described slice or locus when relevant, and the declared use.

#### E.18.2:4.3 - Four-way discriminator

Use this discriminator before writing or accepting a mathematical description:

```text
If the claim selects or audits the compound structure in the project, use E.18.
If the claim describes that selected structure with mathematics, use E.18.2.
If the claim evaluates the mathematical lens use, use C.29 with an E.18.2 reference.
If the claim publishes a view, diagram, card, table, or equation face, use E.17 and the governing view or architecture-description pattern.
```

The same source expression or publication may require several records. A refrigerator principle scheme may include a publication face, a functional-architecture view, a selected `TransformationFlowStructure`, a thermodynamic mechanism claim, and a mathematical graph or equation description. E.18.2 writes only the mathematical-description relation. If the same expression is also used as a mathematical lens for world-side adequacy, C.29 governs the lens-use adequacy; if it is only a published face, E.17 governs publication use.


#### E.18.2:4.4 - Related governed claims

E.18.2 does not carry authority for related governed claims. Use the direct governing pattern when the current claim is:

| Current claim | Use |
|---|---|
| one bounded change under conditions | `A.3.4` |
| selected compound structure, flow valuation, path, slice, crossing, or refresh locus | `E.18` |
| selected transformation-flow unfolding structure with constraints, guards, preserved/lost structure, and direct exits | `E.18.3` |
| mathematical-lens adequacy, preserved/lost structure, payoff, or stop condition | `C.29` |
| method, method description, mechanism, signature, work plan, or performed work | `A.3.1`, `A.3.2`, `A.6.1`, `A.6.0`, `A.15.2`, or `A.15.1` |
| evidence, assurance, gate, release, or decision | `A.10`, `B.3`, `A.20`, `A.21`, or `C.11` |
| architecture, structural view, functional structure, module interface, or reusable-structure claim | `C.30`, `C.30.ASV`, `A.6.F`, `A.6.M`, or `C.31` |
| publication face or publication use | `E.17` or `E.17.EFP` |

