---
chunk_kind: "child"
pattern_id: "A.6.M"
pattern_title: "Module Relation Repair"
section_id: "A.6.M:2"
section_title: "Problem"
source_path: "FPF-Spec.md"
output_path: "by_section/A.6.M/A.6.M__003_problem.md"
commit_sha: "ec66cbef9f337bca279d86e825db0947f90e2598"
heading_path:
  - "A.6.M — Module Relation Repair"
  - "A.6.M:2 — Problem"
line_start: 13786
line_end: 13802
dependencies:
  - "A.10"
  - "A.20"
  - "A.21"
  - "A.6.5"
  - "A.6.B"
  - "A.6.F"
  - "A.6.P"
  - "B.3"
  - "C.11"
  - "C.28"
  - "C.30"
  - "C.30.ASV"
  - "C.30.TGA-FLOW-REL"
  - "C.31"
  - "C.31.RSA"
  - "E.18"
  - "E.20"
  - "G.5"
keywords:
  - "are used only for pattern users"
  - "claims"
  - "component"
  - "conformance items"
  - "evidence records"
  - "interface"
  - "interface specification"
  - "layer"
  - "module relation"
  - "open architecture"
  - "or assurance records. Modeled modules and interfaces are not written as agents with duties"
  - "or publication records"
  - "platform"
  - "port"
  - "records"
  - "stack"
  - "substitutability"
---

### A.6.M:2 - Problem

Engineering teams use module language for several different things:

- a component in a part-whole decomposition;
- a replaceable unit under a declared interface;
- a functional element;
- a software package, neural-network block, hardware board, chiplet, subsystem, service, team boundary, or delivery unit;
- a published API, protocol, signature, port, connector, or endpoint;
- a platform extension point;
- a control relation, deployment scope, or source label such as layer or stack that still needs `C.30.STRAT` recovery;
- an open-architecture claim.

These are useful ordinary words, but they cannot carry the same FPF claim. A module claim is not created by a label. A conforming module-interface claim states how a candidate `U.Holon` relates to a larger `U.Holon` under `VP.ModuleInterface`: boundary, interface specification, admissibility conditions, substitution or change policy, and any live evidence, conformance, or admissible-use expectation.

The practical question is: does this phrase name a module relation, a component relation, a functional allocation, a procedural or work-package relation, a role or enactor relation, a deployment or placement structure, an interface specification, a signature declaration, a port or endpoint slot, a TGA flow crossing, a mechanism realization, a platform grammar, a control relation, an autonomy-like operation claim, a source label that must first go to `C.30.STRAT`, or only plain source wording?

