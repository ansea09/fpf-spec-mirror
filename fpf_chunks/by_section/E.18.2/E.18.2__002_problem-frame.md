---
chunk_kind: "child"
pattern_id: "E.18.2"
pattern_title: "Transformation Flow Mathematical Description"
section_id: "E.18.2:1"
section_title: "Problem frame"
source_path: "FPF-Spec.md"
output_path: "by_section/E.18.2/E.18.2__002_problem-frame.md"
commit_sha: "b0368ed8d883c04d0b261b03f46c28e23d790dc5"
heading_path:
  - "E.18.2 — Transformation Flow Mathematical Description"
  - "E.18.2:1 — Problem frame"
line_start: 74744
line_end: 74778
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

### E.18.2:1 - Problem frame

Use this pattern when the current EntityOfConcern is a mathematical description of a selected transformation-flow structure, path, path slice, flow valuation, crossing, or compound transformation arrangement. The description may be a graph, hypergraph, category-theory object, algebra, tuple, matrix, network expression, wiring diagram, morphism family, quotient, fold, refinement, factorization, path relation, slice relation, or another formal expression.

The primary EntityOfConcern is `TransformationFlowMathematicalDescription@Context`: a `C.2.1 U.Episteme` specialization whose described entity is a selected `TransformationFlowStructure` or one selected part of it. E.18.2 does not invent a second local description format. In C.2.1 slot terms, `DescribedTransformationFlowStructureRef` fills the entity-of-concern slot, `CandidateMathObject`, `ExpressionKind`, `MappingMode`, `PreservedStructure`, `LostStructure`, and `DeclaredUse` fill the claim or description-content slots, and `PublicationFaceRef?` stays a publication relation through `E.17`. E.18.2 keeps three values distinct:

| Value under concern | Governing pattern | Boundary |
|---|---|---|
| selected compound structure of transformations and adjacent loci | `E.18` | not a mathematical expression merely because it can be described by a graph or algebra |
| mathematical description of that selected structure | `E.18.2` | records represented structure, expression kind, mapping mode, preserved/lost structure, declared use, and the boundary to stronger project claims |
| declared mathematical-lens use and its adequacy | `C.29` | not a local E.18.2 invention; use C.29 fields when adequacy, preserved/lost structure, payoff, or stop condition is claim-bearing |

#### E.18.2:1.1 - Use this when

- a selected `TransformationFlowStructure`, path, slice, crossing, or flow valuation needs a graph, algebra, category, tuple, morphism, quotient, fold, refinement, factorization, wiring, matrix, or network expression;
- a diagram or equation set helps compare composition, decomposition, coarser/finer partitioning, transfer, crossing, refresh, or coupled-flow relations, but the mathematical expression itself must not authorize work;
- a source says "graph", "network", "path", "morphism", "algebra", "category", "workflow", "pipeline", "dataflow", or "functional diagram" and the claim being made is the mathematical description of a selected transformation-flow structure;
- a reader needs to know whether the mathematical expression is only a publication face, a C.29 lens-use claim, an E.18 selected structure claim, or an E.18.2 description claim.

#### E.18.2:1.2 - What goes wrong if missed

A project source or diagram can make a graph-shaped expression look like the flow structure itself. Then mathematical neatness silently becomes evidence, work completion, gate readiness, architecture adequacy, or permission to act. The opposite error is also common: every graph-shaped structure is demoted to "just a diagram", so the selected structure, its slices, and its refresh boundaries disappear.

#### E.18.2:1.3 - What this buys

The practitioner can use mathematical structure without overclaiming it. The record names the represented `TransformationFlowStructure`, the expression used, what the expression preserves, what it loses, the declared use, and the governing relation for any stronger claim.

#### E.18.2:1.4 - Not this pattern when

- the selected compound structure itself is the EntityOfConcern; use `E.18`;
- one bounded transformation is the EntityOfConcern; use `A.3.4`;
- the claim is general mathematical-lens adequacy outside transformation-flow structures; use `C.29`;
- the claim is a publication face or view publication; use `E.17` and the relevant view or architecture-description pattern;
- the claim is work planning, performed work, evidence, assurance, gate fit, gate decision, release, decision, or architecture adequacy; use the direct governing pattern.

