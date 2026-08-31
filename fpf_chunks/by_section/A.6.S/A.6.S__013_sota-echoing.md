---
chunk_kind: "child"
pattern_id: "A.6.S"
pattern_title: "TargetSignature and optional ConstructorSignature - demand-driven signature engineering"
section_id: "A.6.S:11"
section_title: "SoTA-Echoing"
source_path: "FPF-Spec.md"
output_path: "by_section/A.6.S/A.6.S__013_sota-echoing.md"
commit_sha: "0c3ef3d3921bb3176096e3e6102dd819c42f6446"
heading_path:
  - "A.6.S — TargetSignature and optional ConstructorSignature - demand-driven signature engineering"
  - "A.6.S:11 — SoTA-Echoing"
line_start: 21053
line_end: 21066
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
  Contemporary effect systems emphasise that an operation signature can be described independently of how effects are handled. A.6.S adopts that separation here: the TargetSignature remains the boundary declaration, while any operation application, construction Work, and operational enforcement remain separately identified. This echoes row-typed algebraic effects and modern handler formulations (Leijen 2017; Hillerström & Lindley 2018).

* **Adapt: categorical optics treat “focus” and “round‑trip laws” as a disciplined interface for bidirectional structure.**
  Optics offer a compact mathematical language for “what is preserved” under a transformation and when updates are coherent. A.6.S adapts this mindset to boundary evolution: viewing corresponds to projection, and retargeting corresponds to an explicit transition with stated preservation claims. Profunctor optics provide a post‑2015 reference point for this style of interface reasoning (Pickering, Gibbons & Wu 2017).

* **Adapt: architecture description standards formalise `U.Viewpoint` and `U.View` responsibility and reduce semantic drift across representations.**
  ISO/IEC/IEEE 42010 treats views as products of viewpoints, with explicit stakeholder concerns and responsibility. A.6.S uses only the view-accountability lesson: when MVPK publication is current, each face is an explicit view of the exact source episteme. A ConstructorSignature is added only when a named receiver reuses the view-producing operation declaration; it is not required to explain how every view was produced.

* **Adopt in spirit: behavioural protocol disciplines treat boundaries as typed interaction protocols with safety commitments.**
  Session and behavioural type practice treats boundaries as protocols with progress and safety properties, which matches the A.6 split between signature laws and mechanism entry gates. A.6.S does not import tooling or typechecking, but it adopts the practice of making boundary interactions explicit and law‑governed (e.g., modern MPST practice as cited in A.6.1).

