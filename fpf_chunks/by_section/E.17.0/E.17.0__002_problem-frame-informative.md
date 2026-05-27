---
chunk_kind: "child"
pattern_id: "E.17.0"
pattern_title: "U.MultiViewDescribing — Viewpoints, Views & Correspondences"
section_id: "E.17.0:1"
section_title: "Problem frame  (informative)"
source_path: "FPF-Spec.md"
output_path: "by_section/E.17.0/E.17.0__002_problem-frame-informative.md"
commit_sha: "562813fb466950d9c49bc6d2e76ec2626f4df697"
heading_path:
  - "E.17.0 — U.MultiViewDescribing — Viewpoints, Views & Correspondences"
  - "E.17.0:1 — Problem frame  (informative)"
line_start: 58458
line_end: 58475
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

### E.17.0:1 - Problem frame  *(informative)*

Complex systems (social‑technical, cyber‑physical, organisational) are routinely described from **many perspectives**:

* functional vs structural vs deployment vs behavioural views,
* safety vs performance vs cost vs governance views,
* formal specs vs operational runbooks vs regulatory dossiers.

Post‑2015 MBSE and architecture practice emphasise **viewpoints and views** (ISO 42010, SysML v2), and contemporary model‑based toolchains treat views as **queries or projections over shared models** rather than independent documents.

In FPF terms:

* the things we talk about — systems, methods, services, epistemes — are `U.Entity` or `U.Holon` values in `DescribedEntitySlot`;
* descriptions and specifications of those things are `U.Episteme` instances (`…Description` or `…Spec`) with a **DescriptionContext** = `⟨DescribedEntityRef, BoundedContextRef, ViewpointRef⟩`;
* episteme-lane views are `U.View` (`U.EpistemeView`) that slice ClaimGraphs under specific viewpoints and representation schemes.

What we lack without this pattern is a **universal way to organise families of descriptions/specifications under multiple viewpoints** — for any entity‑of‑interest, not only for architecture, and without collapsing “view” into “document” or “diagram”.

