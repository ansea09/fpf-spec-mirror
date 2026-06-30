---
chunk_kind: "child"
pattern_id: "E.17.0"
pattern_title: "U.MultiViewDescribing - Viewpoints, Views & Correspondences"
section_id: "E.17.0:intro"
section_title: "Intro"
source_path: "FPF-Spec.md"
output_path: "by_section/E.17.0/E.17.0__001_intro.md"
commit_sha: "e264bfb1cdeecdfe1b7407deba14165475c20ac7"
heading_path:
  - "E.17.0 — U.MultiViewDescribing - Viewpoints, Views & Correspondences"
  - "E.17.0:intro — Intro"
line_start: 71891
line_end: 71913
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

## E.17.0 - `U.MultiViewDescribing` - Viewpoints, Views & Correspondences
> **Status:** Stable
**Use this when.** A team has several descriptions or specification-use descriptions of the same entity of concern and needs to say which viewpoint each description uses, which view it yields, and which correspondences keep those views comparable without turning a diagram, document, or publication face into the described entity itself.

**First output.** One `DescriptionContext` with `EntityOfConcernRef`, `BoundedContextRef`, `ViewpointRef`, the resulting view or view family, and any correspondence relation needed for the current comparison.

> **Tech‑name:** `U.MultiViewDescribing`
> **Plain‑name:** multi‑view describing (viewpoints, views, correspondence for families of Description epistemes and specification-use Description epistemes)

**Status & placement.** Stable; Part E (Describing & Publication). Normative architectural pattern.
**Builds on:** C.2.1 `U.EpistemeSlotRelation` (EntityOfConcern, Viewpoint, and View slots), A.6.2 `U.EffectFreeEpistemicMorphing`, A.6.3 `U.EpistemicViewing`, A.6.4 `U.EpistemicRetargeting`, A.7 (Strict Distinction; EntityOfConcern and Description-episteme boundary and specification-use gate versus publication-form and carrier relation positions), E.10.D1 (Context), E.10.D2 (EntityOfConcern and Description-episteme boundary and specification-use refinement discipline).
**Used by:** E.17 (MVPK — publication as a specialisation of multi‑view describing for morphisms), E.17.1 `U.ViewpointBundleLibrary`, E.17.2 `TEVB`, E.18:5.12 (transformation-flow viewpoint-family map), domain‑specific description schemes (architecture, safety cases, governance, research).

**Kind, relation, and use guard.**

**Family indexing rule.** `U.MultiViewDescribing` indexes families by `EntityOfConcernClass`, `EntityOfConcernRef`, bounded context, and viewpoint. `EoIClass*` and `DescribedEntity*` wording does not create a second view-family ontology; use the EntityOfConcern family.

**C.2.1 relation-position binding.** `U.MultiViewDescribing` does not mint a generic semio kind. When the family describes or views knowledge claims, the claim-bearing value is `U.Episteme`; when that episteme is made available as a published episteme, use `U.EpistemePublication` or governed `U.Episteme` publication. Publication forms, episteme-side `U.View` values, MVPK faces, source-finding cues, SCR and RSCR carriers remain separate relation positions. If a family crosses into another FPF pattern or a non-pattern `authoritySourceRef` destination, name `governingPatternRef` or `authoritySourceRef` rather than a container label.

* `U.Viewpoint` is the ValueKind of `ViewpointSlot` and denotes **viewpoint specifications**, not `publication-face kind` values or carriers.
* `U.View` is the selected short form for `U.EpistemeView`, i.e. an **episteme-side view**, not a document or file. Views are epistemes; literal `publication face/form` and `interop publication form` are accepted `publication-face kind` values under publication-face-kind discipline; concrete renderings and carriers remain A.7, SCR, and RSCR concerns.
* `ViewFamilyId` is a lexical tag for **families of viewpoints** (e.g. TEVB), never for view kinds, MVPK `U.View` values, `U.ViewFamily(-)` bundles, or `publication-face kind` values. MVPK face kinds remain `{PlainView, TechCard, InteropCard, AssuranceLane}`.

