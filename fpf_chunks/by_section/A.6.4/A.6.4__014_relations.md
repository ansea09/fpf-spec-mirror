---
chunk_kind: "child"
pattern_id: "A.6.4"
pattern_title: "U.EpistemicRetargeting — EntityOfConcern retargeting morphism"
section_id: "A.6.4:10"
section_title: "Relations"
source_path: "FPF-Spec.md"
output_path: "by_section/A.6.4/A.6.4__014_relations.md"
commit_sha: "3d098629dc218572089f1890080c17d6f1d9a867"
heading_path:
  - "A.6.4 — U.EpistemicRetargeting — EntityOfConcern retargeting morphism"
  - "A.6.4:10 — Relations"
line_start: 15625
line_end: 15642
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

### A.6.4:10 - Relations

* **Specialises / is specialised by.**
  * Specialises A.6.2 `U.EffectFreeEpistemicMorphing` as the `entityOfConcernChangeMode = retarget` profile.
  * Complements A.6.3 `U.EpistemicViewing` (EntityOfConcern-preserving EFEM) as the “retargeting” counterpart.

* **Constrained by.**
  * A.6.5 relation-declaration slot discipline for SlotKind, ValueKind, and RefKind rules.
  * C.2.1 for exact claim content, EntityOfConcern, and effective ReferenceScheme, plus any separately current empirical-grounding relation.
  * E.10.D2 (EntityOfConcern, Description-episteme, describing-use, and specification-use discipline).
  * Part F (Bridges, `KindBridge`, ReferencePlane crossings, CL/CL^plane).
  * E.10 (LEX‑BUNDLE naming rules, especially on `…Slot`/`…Ref` and ban on Subject/Object in episteme tech names).

* **Consumed by.**
  * E.18 (`StructuralReinterpretation` and other cross-kind transformation-flow architecture relations).
  * E.17.0/E.17 (for cases where publication needs to move between different EntityOfConcern values but preserve invariants).
  * KD‑CAL/LOG‑CAL rules that reason about retargeting and invariant preservation across different EntityOfConcern values.

