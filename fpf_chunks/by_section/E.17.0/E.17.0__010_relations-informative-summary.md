---
chunk_kind: "child"
pattern_id: "E.17.0"
pattern_title: "U.MultiViewDescribing - Viewpoints, Views & Correspondences"
section_id: "E.17.0:9"
section_title: "Relations  (informative summary)"
source_path: "FPF-Spec.md"
output_path: "by_section/E.17.0/E.17.0__010_relations-informative-summary.md"
commit_sha: "c927fef1dac0f4d5f8ca93deef8a52de75e3f77b"
heading_path:
  - "E.17.0 — U.MultiViewDescribing - Viewpoints, Views & Correspondences"
  - "E.17.0:9 — Relations  (informative summary)"
line_start: 72502
line_end: 72521
dependencies:
  - "A.15"
  - "A.2"
  - "A.2.1"
  - "A.6.2"
  - "A.6.3"
  - "A.6.4"
  - "A.7"
  - "C.2.1"
  - "E.10"
  - "E.10.D1"
  - "E.10.D2"
  - "E.17"
  - "E.17.1"
  - "E.17.2"
  - "E.18"
  - "U.EffectFreeEpistemicMorphing"
  - "U.EpistemeSlotRelation"
  - "U.EpistemicRetargeting"
  - "U.EpistemicViewing"
  - "U.ViewpointBundleLibrary"
keywords:
---

### E.17.0:9 - Relations  *(informative summary)*

* **Builds on C.2.1 `U.EpistemeSlotRelation`.**
  Uses `EntityOfConcernSlot`, `ViewpointSlot`, `ViewSlot`, `ClaimGraphSlot`, `ReferenceSchemeSlot` as the structural backbone for descriptions, views, and correspondence.

* **Builds on A.6.2–A.6.4.**
  Families rely on `U.EffectFreeEpistemicMorphing` for view‑producing morphisms, `U.EpistemicViewing` for entityOfConcern‑preserving views, and `U.EpistemicRetargeting` for moves that change the EntityOfConcern (outside a given family).

* **Constrains E.17 (MVPK).**
  MVPK is a **publication‑specialised MultiViewDescribing for morphisms**: its viewpoints are publication viewpoints; its ViewFamily is a special case of `Views(T,C)` with `T` a morphism; its rules and invariants must respect MVD‑0…MVD‑7.

* **Constrains E.17.1 / E.17.2.**
  `U.ViewpointBundleLibrary` and TEVB provide concrete viewpoint bundles populating `Σ` for particular `EntityOfConcernClass` (e.g. engineering holons), but they must treat viewpoints as `U.Viewpoint` values in `ViewpointSlot`, not as ad‑hoc tags.

* **Coordinates with E.10.D2 (EntityOfConcern and Description-episteme boundary and specification use) and E.10 LEX‑BUNDLE.**
  Ensures every Description episteme or Description episteme admitted for specification use in a family has a DescriptionContext, keeps “Describe and specification-use” distinct from “Publish”, and respects lexical guards around `View`, `Viewpoint`, `publication-face kind`, `ViewFamilyId`, `*Slot`, `*Ref`.

* **Coordinates with A.2/A.2.1/A.15 and the Part F role-description and role-name cluster.**
  Viewpoints' stakeholder families and concern entries may mention work-facing roles, holders, assignments, responsibilities, or role names, but those claims remain governed by `A.2`, `A.2.1`, `A.15`, and Part F. MultiViewDescribing does not overload `U.Role` as a slot value in EntityOfConcern and Description-episteme boundary and specification use or episteme slot relations.

