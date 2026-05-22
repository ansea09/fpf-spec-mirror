---
chunk_kind: "child"
pattern_id: "E.17.0"
pattern_title: "U.MultiViewDescribing — Viewpoints, Views & Correspondences"
section_id: "E.17.0:9"
section_title: "Relations  (informative summary)"
source_path: "FPF-Spec.md"
output_path: "by_section/E.17.0/E.17.0__010_relations-informative-summary.md"
commit_sha: "725f0b7b372754cda3f6f4e15184215da568fc4d"
heading_path:
  - "E.17.0 — U.MultiViewDescribing — Viewpoints, Views & Correspondences"
  - "E.17.0:9 — Relations  (informative summary)"
line_start: 55769
line_end: 55788
dependencies:
  - "A.6.2"
  - "A.6.3"
  - "A.6.4"
  - "A.7"
  - "B.5"
  - "C.2.1"
  - "E.10"
  - "E.10.D1"
  - "E.10.D2"
  - "E.17"
  - "E.17.1"
  - "E.17.2"
  - "E.18"
  - "E.TGA"
  - "U.EffectFreeEpistemicMorphing"
  - "U.EpistemeSlotGraph"
  - "U.EpistemicRetargeting"
  - "U.EpistemicViewing"
  - "U.ViewpointBundleLibrary"
keywords:
  - "ISO 42010 alignment"
  - "correspondence model"
  - "description families"
  - "engineering vs publication viewpoints"
  - "entity-of-interest"
  - "multi-view describing"
  - "view"
  - "view vs viewpoint"
  - "viewpoint"
---

### E.17.0:9 - Relations  *(informative summary)*

* **Builds on C.2.1 `U.EpistemeSlotGraph`.**
  Uses `DescribedEntitySlot`, `ViewpointSlot`, `ViewSlot`, `ClaimGraphSlot`, `ReferenceSchemeSlot` as the structural backbone for descriptions, views, and correspondence.

* **Builds on A.6.2–A.6.4.**
  Families rely on `U.EffectFreeEpistemicMorphing` for view‑producing morphisms, `U.EpistemicViewing` for describedEntity‑preserving views, and `U.EpistemicRetargeting` for moves that change the described entity (outside a given family).

* **Constrains E.17 (MVPK).**
  MVPK is a **publication‑specialised MultiViewDescribing for morphisms**: its viewpoints are publication viewpoints; its ViewFamily is a special case of `Views(T,C)` with `T` a morphism; its rules/invariants must respect MVD‑0…MVD‑7.

* **Constrains E.17.1 / E.17.2.**
  `U.ViewpointBundleLibrary` and TEVB provide concrete viewpoint bundles populating `Σ` for particular `EoIClass` (e.g. engineering holons), but they must treat viewpoints as `U.Viewpoint` values in `ViewpointSlot`, not as ad‑hoc tags.

* **Coordinates with E.10.D2 (I/D/S) and E.10 LEX‑BUNDLE.**
  Ensures every D/S episteme in a family has a DescriptionContext, keeps “Describe/Specify” distinct from “Publish”, and respects lexical guards around `View`, `Viewpoint`, `SurfaceKind`, `ViewFamilyId`, `*Slot`, `*Ref`.

* **Coordinates with B.5.* / F‑cluster.**
  Viewpoints’ stakeholder families and concerns link naturally with RoleEnactment (B.5.\*) and Part F role descriptions, assignments, harnesses — without overloading `U.Role` as a coordinate in I/D/S or episteme slots.

