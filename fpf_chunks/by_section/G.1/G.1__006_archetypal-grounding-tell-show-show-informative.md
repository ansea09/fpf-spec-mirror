---
chunk_kind: "child"
pattern_id: "G.1"
pattern_title: "Author a Reusable CG-Frame Generator and Selector Kit"
section_id: "G.1:5"
section_title: "Archetypal Grounding — Tell–Show–Show (informative)"
source_path: "FPF-Spec.md"
output_path: "by_section/G.1/G.1__006_archetypal-grounding-tell-show-show-informative.md"
commit_sha: "1e57ccda08ebbb9d49b7b2190bc2740b72075a13"
heading_path:
  - "G.1 — Author a Reusable CG-Frame Generator and Selector Kit"
  - "G.1:5 — Archetypal Grounding — Tell–Show–Show (informative)"
line_start: 135637
line_end: 135657
dependencies:
  - "A.10"
  - "A.15.2"
  - "A.15.3"
  - "A.19.CN"
  - "C.17"
  - "C.18"
  - "C.19"
  - "C.23"
  - "E.10"
  - "E.19"
  - "E.8"
  - "G.0"
  - "G.10"
  - "G.11"
  - "G.2"
  - "G.3"
  - "G.4"
  - "G.5"
  - "G.Core"
keywords:
  - "CGFrameLibraryId"
  - "CGKitId manifest"
  - "RSCR linkage surfaces"
  - "RefreshReadinessCardId"
  - "ShortlistId"
  - "SoTA_SetId"
  - "UTS/Name Cards"
  - "VariantPoolId"
  - "and set-result scaffold"
  - "edition pins"
  - "generator"
  - "generator chassis"
  - "selector"
  - "set-result outcome"
  - "set-return selection"
  - "shipping and refresh boundaries"
  - "six-card kit (M1-M6)"
---

### G.1:5 - Archetypal Grounding — Tell–Show–Show (informative)

**Tell.** Use the six cards to reconstruct the frame, sources and candidate pool used for a selected set, the artefacts indexed for publication and the changes that can trigger refresh. The manifest identifies the cards in that kit edition.

**Show A (R&D multi‑criteria decisions).**

* **M1:** define `CG‑FrameContext` for “R&D decision options”, pin `CNSpecRef/CGSpecRef` editions, and publish `entityOfConcern` + `ReferencePlane`.
* **M2:** build `SoTA_SetId` via `G.2` using a living-review funnel with a declared update cadence and source-selection reporting (for example, PRISMA-style reporting) and publish UTS stubs for reusable constructs.
* **M3:** emit a `VariantPoolId` where each candidate cites its emitter policy and provenance; if QD is used, wire `DescriptorMapRef.edition` and `DistanceDefRef.edition` via `G.1:Ext.NQD`.
* **M4:** produce `ShortlistId` as a selected-set / shortlist surface via `G.5`, with acceptance predicates sourced from `G.4`.
* **M5:** publish a `CGFrameLibraryId` indexing the chosen CHR/CAL/LOG bundles and UTS rows; register RSCR tests.
* **M6:** declare refresh readiness (telemetry pins + canonical RSCR trigger kinds) and wire to `G.11`.

**Show B (clinical operations; safety‑first acceptability).**

* **M1:** scope a CG‑Frame around dose adjustment decisions; pin legality and evidence minima explicitly.
* **M2:** harvest SoTA models and safety constraints as a reconstructible set (governed by `G.2`).
* **M3:** generate policy‑constrained candidate protocols; emitter trace and evidence pins are mandatory.
* **M4:** return the shortlisted protocols as a set, which may have one member. Choosing one from a shortlist of several requires an explicit decision policy.
* **M5/M6:** publish and wire refresh (decay events, policy changes, and evidence updates retrigger along the P2W path).

