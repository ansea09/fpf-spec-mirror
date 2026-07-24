---
chunk_kind: "child"
pattern_id: "A.3.4"
pattern_title: "U.Transformation: Bounded Change Under Conditions"
section_id: "A.3.4:0"
section_title: "Use This When"
source_path: "FPF-Spec.md"
output_path: "by_section/A.3.4/A.3.4__002_use-this-when.md"
commit_sha: "f2fdd062c1518c9b1a1be1b6ad795627cffad2f1"
heading_path:
  - "A.3.4 — U.Transformation: Bounded Change Under Conditions"
  - "A.3.4:0 — Use This When"
line_start: 7719
line_end: 7753
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

Use this pattern when a project needs to identify an **actual bounded change** itself: which exact governed referent changed, over which extent or ordered boundary, under which boundary conditions, and which actual subject facts make the before-to-after difference one occurrence of change.

Use it when the working question is:

- what exact entity, structure, episteme, characteristic-bearing referent, or formal object changed;
- which actual characteristic-state and direct-relation facts differ across the boundary;
- what temporal extent, formal ordering, or continuity rule identifies this occurrence;
- whether method, planned work, performed work, mechanism, flow structure, representation, evidence, publication, or a later receiving use is also current and therefore needs its own direct relation.

**Primary EntityOfConcern.** One exact `U.Transformation`: an independently identified actual bounded change. A task, method, plan, desired state, work occurrence, operation family, morphism, predicate, delta formula, trace, assertion, obtaining relation occurrence, before-and-after picture, or result record establishes neither that change nor its identity. Such objects can describe, plan, enact, constrain, represent, support, or use a transformation only through their own governed relations.

**Primary working reader.** A practitioner or modeler who must identify one actual change for a current engineering, scientific, formal, documentary, or architectural use before relating it to method, work, flow, evidence, or production. The heavier composition and admission branch additionally addresses an FPF author or reviewer only when that practitioner use needs positive transformation-part or holon claims.

**First useful move.** Name the exact changed referent and the actual boundary across which it changed. Recover the actual pre-boundary, during-boundary, and post-boundary subject facts under their direct patterns. State the temporal extent or formal ordering and the boundary conditions that delimit the occurrence. If the available material is only a desired state, method, plan, model, trace, or assertion, stop: the actual `U.Transformation` has not yet been grounded.

**Open-world guard.** Failure to recover a method, work occurrence, evidence item, publication, delivery, acceptance, or receiving-use relation proves none of those absent. It only blocks or lowers the claim that depends on that exact relation. Conversely, their presence does not establish that an actual transformation occurred.

**What goes wrong if missed.** Method names become change proof, work traces become laws, process diagrams become execution, dynamics models become permission, temporal trends become intervention claims, mathematical constructions become project-world work, and publications or result records are treated as the change itself.

**What this buys.** A practitioner can identify one actual bounded change at the resolution needed by the current use without settling whether finer parts obtain; that identification establishes neither parthood nor partlessness. Exact transformation composition is grounded only when needed, and only a grounded composite is tested against A.1. Method, work, flow, representation, evidence, publication, production, and receiving-use claims remain with their direct governors.
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

