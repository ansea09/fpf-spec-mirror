---
chunk_kind: "child"
pattern_id: "A.6.4"
pattern_title: "U.EpistemicRetargeting — EntityOfConcern retargeting morphism"
section_id: "A.6.4:6"
section_title: "Consequences"
source_path: "FPF-Spec.md"
output_path: "by_section/A.6.4/A.6.4__010_consequences.md"
commit_sha: "d6af871b3e4e47c952d800a2a418c0634f180aaf"
heading_path:
  - "A.6.4 — U.EpistemicRetargeting — EntityOfConcern retargeting morphism"
  - "A.6.4:6 — Consequences"
line_start: 14623
line_end: 14641
dependencies:
  - "A.6.2"
  - "A.6.3"
  - "A.6.5"
  - "A.7"
  - "C.2"
  - "C.2.1"
  - "C.3"
  - "E.10.D2"
  - "E.18"
  - "F.9"
keywords:
---

### A.6.4:6 - Consequences

* **Clear separation of Viewing vs Retargeting.**
  A.6.3 and A.6.4 now jointly distinguish:
  * **views**: same `EntityOfConcernRef`, possible representation/viewpoint changes;
  * **retargetings**: different `EntityOfConcernRef` under `KindBridge` and invariants.

* **Canonical governing pattern for StructuralReinterpretation.**
  `E.18` `StructuralReinterpretation` receives semantics from `U.EpistemicRetargeting`, not from an ad-hoc special graph-position kind. This reduces duplication and clarifies how CL penalties and Bridges are used.

* **Invariants become first‑class.**
  Retargeting makes invariants explicit and type‑checked: every such morphism must state what it preserves and how that is expressed in KD‑CAL/LOG‑CAL.

* **Safer cross‑plane reasoning.**
  ReferencePlane crossings and kind‑level moves are handled via existing Bridges (Part F), with CL^plane/CL^k penalties and SquareLaw witnesses, instead of hidden in implementation details.

* **Better integration with EntityOfConcern and Description-episteme boundary and specification-use gate.**
  For `…Description`/`…Spec` epistemes, retargeting is the only place where `EntityOfConcernRef` in `DescriptionContext` is allowed to change; all other EntityOfConcern and Description-episteme boundary and specification-use operations (Describe, specification-use refinement, Viewing) keep it fixed.

