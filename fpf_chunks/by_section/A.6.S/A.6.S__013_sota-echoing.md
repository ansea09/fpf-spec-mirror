---
chunk_kind: "child"
pattern_id: "A.6.S"
pattern_title: "TargetSignature and optional ConstructorSignature - demand-driven signature engineering"
section_id: "A.6.S:11"
section_title: "SoTA-Echoing"
source_path: "FPF-Spec.md"
output_path: "by_section/A.6.S/A.6.S__013_sota-echoing.md"
commit_sha: "3f6e02840fe3a22427aed590f9688a9c8f6bf5c8"
heading_path:
  - "A.6.S — TargetSignature and optional ConstructorSignature - demand-driven signature engineering"
  - "A.6.S:11 — SoTA-Echoing"
line_start: 24977
line_end: 24990
dependencies:
  - "A.15"
  - "A.15.1"
  - "A.15.2"
  - "A.2"
  - "A.2.1"
  - "A.3.1"
  - "A.3.2"
  - "A.6"
  - "A.6.0"
  - "A.6.2-A.6.6"
  - "A.6.5"
  - "A.6.6"
  - "A.6.B"
  - "A.7"
  - "C.2.1"
  - "E.10"
  - "E.17"
  - "E.17.0"
  - "E.18"
  - "F.6"
keywords:
  - "appear"
  - "quadrant classification is governed by A.6.B)"
---

### A.6.S:11 - SoTA-Echoing

* **Adopt: algebraic effects and effect systems separate operation signatures from handler semantics.**
  The cited effect-system work describes operation signatures independently of how effects are handled (Leijen 2017; Hillerström & Lindley 2018). A.6.S adopts that separation: a TargetSignature declares the boundary, while operation application, construction Work and operational enforcement retain their own identities and rules.

* **Adapt: categorical optics treat “focus” and “round‑trip laws” as a disciplined interface for bidirectional structure.**
  Categorical optics make preservation and round-trip laws explicit for bidirectional structure (Pickering, Gibbons & Wu 2017). A.6.S adapts the practice of stating the laws a constructor use needs. An A.6.3 viewing or A.6.4 retargeting still follows its own rule; this analogy alone establishes neither an optic nor a round-trip law for a particular constructor.

* **Adapt: architecture-description practice relates views to viewpoints and stakeholder concerns.**
  ISO/IEC/IEEE 42010:2022 contributes that discipline. FPF's local adaptation identifies the exact `U.Viewpoint` episteme and tests the selected episteme's `U.View` membership through E.17.0 conformance; a publication face remains the separate form over its source for a bounded reader/use, with membership and A.6.3 construction conditional under §4.4. Any separate `responsibility` or `view-accountability` claim needs its actual participants and governing predicate. A ConstructorSignature is added only when a named receiver reuses the view-producing operation declaration; it is not required to explain how every view was produced.

* **Adopt in spirit: behavioural protocol disciplines treat boundaries as typed interaction protocols with safety commitments.**
  Session and behavioural type practice treats boundaries as protocols with progress and safety properties, which matches the A.6 split between signature laws and mechanism entry gates. A.6.S does not import tooling or typechecking, but it adopts the practice of making boundary interactions explicit and law‑governed (the MPST sources discussed in A.6.1).

