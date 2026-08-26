---
chunk_kind: "child"
pattern_id: "A.3.4"
pattern_title: "U.Transformation: Bounded Change Under Conditions"
section_id: "A.3.4:0"
section_title: "Use This When"
source_path: "FPF-Spec.md"
output_path: "by_section/A.3.4/A.3.4__002_use-this-when.md"
commit_sha: "563f4c8e06a319cbd375b66cdbb2df27a5f8b9ef"
heading_path:
  - "A.3.4 — U.Transformation: Bounded Change Under Conditions"
  - "A.3.4:0 — Use This When"
line_start: 8659
line_end: 8695
dependencies:
  - "A.1"
  - "A.10"
  - "A.11"
  - "A.14"
  - "A.15.1"
  - "A.15.2"
  - "A.15.PROD"
  - "A.22"
  - "A.3"
  - "A.3.1"
  - "A.3.2"
  - "A.3.3"
  - "A.6.1"
  - "A.6.RCD"
  - "A.6.REL"
  - "A.7"
  - "B.2"
  - "B.3"
  - "C.13"
  - "C.2.1"
  - "C.27"
  - "C.27.TA"
  - "C.29"
  - "C.32.P2S"
  - "E.18"
  - "E.18.1"
  - "E.24"
  - "E.24.UK"
  - "F.18"
  - "G.11"
keywords:
  - "actual bounded change"
  - "actual subject facts"
  - "changed referent"
  - "continuity and reidentification"
  - "occurrence boundary"
  - "transformation composition"
---

### A.3.4:0 - Use This When

Use this pattern when a project must decide whether an actual change occurred and identify that one change. Ask: what continuing subject changed, where the change begins and ends, which facts differ before, during, and after it, and what rule makes this one occurrence rather than unrelated observations.

Use it when the working question is:

- what continuing subject changed: an entity, selected structure, presentation carrier, constituent organization, characteristic-bearing referent, or formal object;
- when a specification's claim content changes, which two C.2.1 epistemes exist, whether their `EpistemeEditionRelation` obtains, whether a continuing carrier or constituent organization changed, and whether revision `U.Work` first constituted the later episteme under `A.15.PROD`;
- which actual characteristic-state and direct-relation facts differ across the boundary;
- what temporal extent, formal ordering, or continuity rule identifies this occurrence;
- which additional claim, if any, is actually being made about method, planned work, performed work, mechanism, flow structure, representation, evidence, publication, or a later use, and which pattern answers that claim.

**Primary EntityOfConcern.** One actual `U.Transformation`: the bounded occurrence, not the sentence, plan, trace, formula, or record about it. A task, method, plan, desired state, work occurrence, operation family, morphism, predicate, delta formula, assertion, before-and-after picture, or result record neither proves that the change occurred nor identifies it. Use those objects only in their separate claims about planning, enactment, representation, evidence, or later use.

**Primary working reader.** A practitioner or modeler who must identify one actual change for a current engineering, scientific, formal, documentary, or architectural use before relating it to method, work, flow, evidence, or production. The informative parked-composition branch additionally addresses an FPF author or reviewer only when that use asks whether several changes compose one change or whether that whole could satisfy A.1.

**First useful move.** Name the continuing subject and where the change begins and ends. Write the subject facts that hold before, during, and after that boundary, then state the boundary conditions and the continuity or reidentification rule that make this one occurrence. If the material supplies only a desired state, method, plan, model, trace, or assertion, stop: it has not yet grounded an actual `U.Transformation`.

**Open-world guard.** Not finding a method, work occurrence, evidence item, publication, delivery, acceptance, or later-use relation does not prove that it is absent. It prevents only the particular claim that needs it. Finding one of those objects likewise does not prove that an actual transformation occurred.

**What goes wrong if missed.** Method names become change proof, work traces become laws, process diagrams become execution, dynamics models become permission, temporal trends become intervention claims, mathematical constructions become project-world work, and publications or result records are treated as the change itself.

**What this buys.** The practitioner gets one usable actual-change result without first deciding whether finer changes are its parts. If no composition or holon claim is needed, continue with the ordinary neighboring-object guidance at `4.3`. If such a claim is needed, keep the identified changes and return the parked composition blocker; this pattern does not guess the future architecture. Apply `A.1` only after an accepted architecture supplies the proposed whole and its construction facts. Method, work, flow, representation, evidence, publication, production, and later-use claims stay separate.

**Not this pattern when.**

- If the issue is only a semantic way of doing, use `A.3.1`.
- If the issue is a description of that way, use `A.3.2`.
- If the issue is a state-space and transition-law episteme, use `A.3.3`.
- If the issue is a law-governed operation algebra with admissibility predicates, use `A.6.1` and `E.20`.
- If the issue is planned or dated work, use `A.15.2` or `A.15.1`.
- If the issue is the selected compound transformation-flow structure, its locus, path, path slice, crossing, or flow valuation, use `E.18`.
- If the issue is a graph, algebra, category, tuple, morphism, quotient, fold, refinement, factorization, or wiring expression used to describe that structure mathematically, use `E.18.2` and `C.29`.
- If the issue is a positive temporal aspect of an object or claim, use `C.27.TA`.
- If the issue is adequacy or admissible use of a temporal claim, use `C.27`.
- If the issue is holon recognition without a current actual-change identity or constructive transformation-parthood claim, use `A.1`.

