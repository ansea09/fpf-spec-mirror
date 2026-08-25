---
chunk_kind: "child"
pattern_id: "E.18.2"
pattern_title: "Transformation Flow Mathematical Description"
section_id: "E.18.2:1"
section_title: "Problem frame"
source_path: "FPF-Spec.md"
output_path: "by_section/E.18.2/E.18.2__002_problem-frame.md"
commit_sha: "2124f3a0ea03125a5bf495c2ef99f5fbb4c73571"
heading_path:
  - "E.18.2 — Transformation Flow Mathematical Description"
  - "E.18.2:1 — Problem frame"
line_start: 83693
line_end: 83733
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

### E.18.2:1 - Problem frame

Use this pattern when the current EntityOfConcern is a mathematical description of exactly one selected transformation-flow structure, one selected network of such structures, or one independently identified part of that subject. The description may be a graph, hypergraph, category-theory object, algebra, tuple, matrix, network expression, wiring diagram, morphism family, quotient, fold, refinement, factorization, path relation, slice relation, or another formal expression.

The primary EntityOfConcern is `TransformationFlowMathematicalDescription@Context`: a `C.2.1 U.Episteme` specialization whose described ontic subject is exactly one selected `TransformationFlowStructure` under E.18 or one selected `TransformationFlowStructureNetwork@Context` under E.18.NET. E.18.2 does not invent a second local description format. The one-TFS and network reference branches are mutually exclusive; `CandidateMathObject`, `ExpressionKind`, `MappingMode`, `PreservedStructure`, `LostStructure`, and `DeclaredUse` fill claim or description-content slots, while `PublicationFaceRef?` remains a separate publication relation through E.17. E.18.2 keeps five values distinct:

| Value under concern | Pattern contribution used | Boundary |
|---|---|---|
| one selected compound structure of transformations and adjacent loci | E.18 defines one-TFS identity, allowed loci and relations, selection constraints, and local-value rules; apply those rules to select the exact structure | not a mathematical expression merely because a graph or algebra describes it |
| one selected network of independently identified TFS or nested-network members and exact cross-member relations | E.18.NET defines membership, boundary, and cross-member relation requirements; apply those rules to select the exact network and identify its obtaining cross-member relation occurrences | not a graph, record, view, or publication, and not several valuations or one internal subflow |
| mathematical description of exactly one selected TFS or network | `E.18.2` | records represented subject, expression kind, mapping mode, preserved/lost structure, declared use, and the boundary to stronger project claims |
| declared mathematical-lens use and its adequacy | C.29 defines the bounded adequacy test and returned lens-use result; apply it when adequacy, payoff, preserved/lost structure, or a stop condition is claim-bearing | not a local E.18.2 invention |
| rendered graph, table, equation, diagram, or other publication face | `E.17` publishes the face; the applicable view or architecture-description pattern supplies its membership or adequacy result when that claim is current | may publish the mathematical description but neither becomes it nor reidentifies the selected TFS or network |

When the described selected structure is one A.22-selected CGUS qualified under `E.18.3` through an independently identified E.18 substrate, E.18.2 still defines only the mathematical description. A graph, path expression, category object, algebra, tuple, or matrix may describe substrate positions, crossings, and condition labels, but the expression does not decide whether a condition is an applied claim, an E.18 `GuardFail` event, or an independently defined relation occurrence. It may also describe preserved or lost structure, exact supporting relations to independently identified neighboring values, and stop or reconsideration questions, but it remains `TransformationFlowMathematicalDescription@Context` or a C.29 lens-use claim. It does not become the selected CGUS or its substrate and does not carry method, work, evidence, architecture, publication, or refresh authority.

#### E.18.2:1.1 - Use this when

- one selected `TransformationFlowStructure`, one selected `TransformationFlowStructureNetwork@Context`, or an independently identified part of that subject needs a graph, algebra, category, tuple, morphism, quotient, fold, refinement, factorization, wiring, matrix, or network expression;
- a diagram or equation set helps compare composition, decomposition, coarser/finer partitioning, internal transfer, crossing, or refresh inside one TFS, or exact cross-member relations in one selected network, but the mathematical expression itself must not authorize work;
- a source says "graph", "network", "path", "morphism", "algebra", "category", "workflow", "pipeline", "dataflow", or "functional diagram" and the claim being made is the mathematical description of one already selected TFS or TFS network;
- a reader needs to decide whether the visible object is one E.18 TFS, one E.18.NET network, an E.18.2 mathematical description, a C.29 lens-use claim, or only an E.17 publication face.

#### E.18.2:1.2 - What goes wrong if missed

A project source expression, source publication, or diagram can make a graph-shaped expression look like the flow structure itself. Then mathematical neatness silently becomes evidence, work completion, gate readiness, architecture adequacy, or permission to act. The opposite error is also common: every graph-shaped structure is demoted to "just a diagram", so the selected structure, its slices, and its refresh boundaries disappear.

#### E.18.2:1.3 - What this buys

The practitioner can use mathematical structure without overclaiming it. The record names exactly one represented E.18 TFS or E.18.NET network, the expression used, what the expression preserves, what it loses, the declared use, and the result returned after applying the pattern whose Solution answers any stronger claim.

#### E.18.2:1.4 - Not this pattern when

- one selected transformation-flow structure itself is the EntityOfConcern; use `E.18`;
- one selected network of independently identified TFS or nested-network members is the EntityOfConcern; use `E.18.NET`;
- one A.22-selected CGUS whose E.18.3 qualification uses an independently identified E.18 substrate is the EntityOfConcern; use `E.18.3`;
- one bounded transformation is the EntityOfConcern; use `A.3.4`;
- the claim is general mathematical-lens adequacy outside transformation-flow structures; use `C.29`;
- the claim is a publication face or view publication; use `E.17` and the relevant view or architecture-description pattern;
- the claim is work planning, performed work, evidence, assurance, gate fit, gate decision, release, decision, or architecture adequacy; use the applicable row in §4.4 and keep the exact plan, Work, evidence relation, assurance result, gate result, release claim, choice, or architecture result returned there.

