---
chunk_kind: "child"
pattern_id: "C.2.1"
pattern_title: "U.Episteme - Epistemes and their slot relation"
section_id: "C.2.1:15"
section_title: "Relations  (overview)"
source_path: "FPF-Spec.md"
output_path: "by_section/C.2.1/C.2.1__017_relations-overview.md"
commit_sha: "b74ecf2b633a2315086198e4aab07c2b61257c27"
heading_path:
  - "C.2.1 — U.Episteme - Epistemes and their slot relation"
  - "C.2.1:15 — Relations  (overview)"
line_start: 37146
line_end: 37171
dependencies:
  - "A.1"
  - "A.6.2-A.6.4"
  - "A.6.5"
  - "A.7"
  - "B.1.3"
  - "C.2"
  - "C.2.1"
  - "E.10.D2"
  - "E.17"
  - "E.17.0-E.17.2"
  - "E.18"
keywords:
---

### C.2.1:15 - Relations  *(overview)*

**Builds on**
* A.1 `U.Holon` — for treating episteme as a holon with components.
* A.6.0 `U.Signature` — for interpreting episteme kinds as n‑ary relations over slots.
* A.6.5 `U.RelationSlotDiscipline` - for SlotKind, ValueKind, and RefKind discipline over episteme slots.
* A.7, E.10.D2 - for the boundary between `EntityOfConcern` and Description episteme discipline, specification use and refinement gates, and the interpretation of `subjectRef` as DescriptionContext.
* C.2 (KD‑CAL, LOG‑CAL) — for ClaimGraph semantics, ReferencePlanes, and Bridges.
* E.8, E.10 — for pattern authoring discipline and lexical guards.

* **Constrains**
* A.6.2–A.6.4 — by fixing the minimal episteme component set those morphisms operate on and by requiring an explicit **EntityOfConcernChangeMode characteristic** (`entityOfConcernChangeMode ∈ {preserve, retarget}`) over `EntityOfConcernSlot`/`GroundingHolonSlot`.
* E.17.0–E.17.2 — by specifying how `EntityOfConcern`, `Viewpoint`, `View` and ReferenceSchemes are represented at episteme level.
* E.17 (MVPK) — by separating `U.View` (episteme) from `U.PresentationCarrier` (publication carrier), and by requiring that publication morphisms be `U.EpistemicViewing` species over C.2.1‑conformant views.
* F.18 (LEX-BUNDLE) - by providing the episteme-specific name cards and guards for EntityOfConcern, GroundingHolon, Viewpoint, View, ReferenceScheme, and their SlotKinds.

**Used by**
* A.6.2 `U.EffectFreeEpistemicMorphing` - as the default episteme slot and value structure for episteme-to-episteme transforms.
* A.6.3 `U.EpistemicViewing` — as the substrate for entityOfConcern‑preserving projections (views).
* A.6.4 `U.EpistemicRetargeting` — as the substrate for EntityOfConcern-bundle retargeting transforms between epistemes (Ep→Ep with `entityOfConcernChangeMode = retarget`).
* E.17.0 `U.MultiViewDescribing`, E.17.1, E.17.2 — to organise families of Description epistemes, including Description epistemes admitted for specification use, under Viewpoints and `EntityOfConcernClass` constraints.
* E.17 (MVPK) — to publish episteme views through publication faces, publication forms, and carriers.
* E.18 - to interpret StructuralReinterpretation and other engineering projections as episteme morphisms over a well-typed `U.EpistemeSlotRelation`.

Together, these relations make `U.EpistemeSlotRelation` the **single normative core** for thinking about epistemes, their EntityOfConcern mapping, their representations, and their transformations across FPF.

