---
chunk_kind: "child"
pattern_id: "E.17.0"
pattern_title: "U.MultiViewDescribing — Viewpoints, Views & Correspondences"
section_id: "E.17.0:intro"
section_title: "Intro"
source_path: "FPF-Spec.md"
output_path: "by_section/E.17.0/E.17.0__001_intro.md"
commit_sha: "eb2832093c1e482d5fdd4985c3d2011ab240b429"
heading_path:
  - "E.17.0 — U.MultiViewDescribing — Viewpoints, Views & Correspondences"
  - "E.17.0:intro — Intro"
line_start: 54558
line_end: 54575
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

## E.17.0 - `U.MultiViewDescribing — Viewpoints, Views & Correspondences`

> **Tech‑name:** `U.MultiViewDescribing`
> **Plain‑name:** multi‑view describing (viewpoints, views, correspondence for families of descriptions/specifications)

**Status & placement.** Part E (Describing & Publication). Normative architectural pattern.
**Builds on:** C.2.1 `U.EpistemeSlotGraph` (DescribedEntity, Viewpoint, and View slots), A.6.2 `U.EffectFreeEpistemicMorphing`, A.6.3 `U.EpistemicViewing`, A.6.4 `U.EpistemicRetargeting`, A.7 (Strict Distinction; I/D/S versus publication-form and carrier lanes), E.10.D1 (Context), E.10.D2 (I/D/S discipline).
**Used by:** E.17 (MVPK — publication as a specialisation of multi‑view describing for morphisms), E.17.1 `U.ViewpointBundleLibrary`, E.17.2 `TEVB`, E.18:5.12 (E.TGA engineering viewpoint families), domain‑specific description schemes (architecture, safety cases, governance, research).

**Guard (lexical).**

**C.2.1 lane binding.** `U.MultiViewDescribing` does not mint a generic semio kind. When the family describes or views knowledge claims, the claim-bearing value is `U.Episteme`; when that episteme is made available as a published episteme, use `U.EpistemePublication` or governed `U.Episteme` publication. Publication forms, episteme-lane `U.View` values, MVPK faces, source-finding cues, and SCR and RSCR carriers remain separate lanes. If a family crosses into a later FPF pattern or a non-pattern `authoritySourceRef` target, name `governingPatternRef` or `authoritySourceRef` rather than a container label.


* `U.Viewpoint` is the ValueKind of `ViewpointSlot` and denotes **intensional viewpoint specs**, not `SurfaceKind` values or carriers.
* `U.View` is an alias of `U.EpistemeView`, i.e. an **episteme-lane view**, not a document or file. Views are epistemes; `PublicationSurface` and `InteropSurface` are L-SURF `SurfaceKind` values; concrete renderings and carriers remain A.7, SCR, and RSCR concerns.
* `ViewFamilyId` is a lexical tag for **families of viewpoints** (e.g. TEVB), never for view kinds, MVPK `U.View` values, `U.ViewFamily(-)` bundles, or `SurfaceKind` values. MVPK face kinds remain `{PlainView, TechCard, InteropCard, AssuranceLane}`.

