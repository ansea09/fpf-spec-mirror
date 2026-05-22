---
chunk_kind: "child"
pattern_id: "A.6.4"
pattern_title: "U.EpistemicRetargeting — describedEntity‑retargeting morphism"
section_id: "A.6.4:10"
section_title: "Relations"
source_path: "FPF-Spec.md"
output_path: "by_section/A.6.4/A.6.4__011_relations.md"
commit_sha: "725f0b7b372754cda3f6f4e15184215da568fc4d"
heading_path:
  - "A.6.4 — U.EpistemicRetargeting — describedEntity‑retargeting morphism"
  - "A.6.4:10 — Relations"
line_start: 11980
line_end: 11997
dependencies:
  - "A.1"
  - "A.6.2"
  - "C.2"
  - "C.2.1"
  - "E.18"
  - "E.TGA"
  - "F.9"
  - "U.EpistemeSlotGraph"
  - "U.EpistemicRetargeting"
keywords:
  - "KindBridge"
  - "SquareLaw-retargeting"
  - "StructuralReinterpretation"
  - "describedEntity shift"
  - "retargeting"
  - "subject retargeting"
---

### A.6.4:10 - Relations

* **Specialises / is specialised by.**
  * Specialises A.6.2 `U.EffectFreeEpistemicMorphing` as the `describedEntityChangeMode = retarget` profile.
  * Complements A.6.3 `U.EpistemicViewing` (describedEntity‑preserving EFEM) as the “retargeting” counterpart.

* **Constrained by.**
  * A.6.5 `U.RelationSlotDiscipline` for SlotKind/ValueKind/RefKind discipline.
  * C.2.1 `U.EpistemeSlotGraph` for episteme components and `DescribedEntitySlot`/`GroundingHolonSlot`.
  * E.10.D2 (I/D/S discipline; `DescriptionContext`).
  * Part F (Bridges, `KindBridge`, ReferencePlane crossings, CL/CL^plane).
  * E.10 (LEX‑BUNDLE naming rules, especially on `…Slot`/`…Ref` and ban on Subject/Object in episteme tech names).

* **Consumed by.**
  * E.18 (E.TGA StructuralReinterpretation and other cross‑kind architecture transformations).
  * E.17.0/E.17 (for cases where publication needs to move between different entities‑of‑interest but preserve invariants).
  * KD‑CAL/LOG‑CAL rules that reason about retargeting and invariant preservation across different described entities.

