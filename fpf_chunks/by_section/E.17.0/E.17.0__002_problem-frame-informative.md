---
chunk_kind: "child"
pattern_id: "E.17.0"
pattern_title: "U.MultiViewDescribing - Viewpoints, Views & Correspondences"
section_id: "E.17.0:1"
section_title: "Problem frame  (informative)"
source_path: "FPF-Spec.md"
output_path: "by_section/E.17.0/E.17.0__002_problem-frame-informative.md"
commit_sha: "fe0df9dcb06cfc87c8a6cb2f7cce3ac0d3b64d5e"
heading_path:
  - "E.17.0 — U.MultiViewDescribing - Viewpoints, Views & Correspondences"
  - "E.17.0:1 — Problem frame  (informative)"
line_start: 65540
line_end: 65557
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

### E.17.0:1 - Problem frame  *(informative)*

Complex systems (social‑technical, cyber‑physical, organisational) are routinely described from **many perspectives**:

* functional vs structural vs deployment vs behavioural views,
* safety vs performance vs cost vs governance views,
* formal specs vs operational runbooks vs regulatory dossiers.

Post‑2015 MBSE and architecture practice emphasise **viewpoints and views** (ISO 42010, SysML v2), and contemporary model‑based toolchains treat views as **queries or projections over shared models** rather than independent documents.

In FPF terms:

* the things we talk about — systems, methods, services, epistemes — are `U.Entity` or `U.Holon` values in `EntityOfConcernSlot`;
* descriptions and specifications of those things are `U.Episteme` instances (`…Description` or `…Spec`) with a **DescriptionContext** = `⟨EntityOfConcernRef, BoundedContextRef, ViewpointRef⟩`;
* episteme-side views are `U.View` (`U.EpistemeView`) that slice ClaimGraphs under specific viewpoints and representation schemes.

What we lack without this pattern is a **universal way to organise families of Description epistemes and specification-use Description epistemes under multiple viewpoints** — for any entity of concern, not only for architecture, and without collapsing “view” into “document” or “diagram”.

