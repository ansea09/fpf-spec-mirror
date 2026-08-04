---
chunk_kind: "child"
pattern_id: "E.17.2"
pattern_title: "TEVB - Typical Engineering Viewpoint Bundle for Holons"
section_id: "E.17.2:intro"
section_title: "Intro"
source_path: "FPF-Spec.md"
output_path: "by_section/E.17.2/E.17.2__001_intro.md"
commit_sha: "8b727cba9e893a467b82aab9da84fb7d6d945480"
heading_path:
  - "E.17.2 — TEVB - Typical Engineering Viewpoint Bundle for Holons"
  - "E.17.2:intro — Intro"
line_start: 79843
line_end: 79858
dependencies:
  - "A.1"
  - "A.22"
  - "A.6.2-A.6.4"
  - "A.6.3"
  - "A.6.6"
  - "A.7"
  - "C.13"
  - "C.2.1"
  - "E.10.D2"
  - "E.17"
  - "E.17.0"
  - "E.17.1"
  - "E.18"
  - "E.24.PUB"
  - "U.View"
  - "U.Viewpoint"
  - "U.ViewpointRef"
keywords:
---

## E.17.2 - TEVB - Typical Engineering Viewpoint Bundle for Holons
> **Status:** Stable

**Use this when.** A team needs one small reusable family of engineering viewpoints for descriptions of a holon, so that functional, procedural, allocation-responsibility, and module-interface claims remain distinguishable and comparable.

**First useful result.** One exact `U.ViewpointBundleLibrary` edition and its exact TEVB bundle edition, whose `ViewFamilyId` is `VF.TEVB.ENG`; one exact holon as the candidate episteme's EntityOfConcern; and one singular exact `U.ViewpointRef` from that bundle edition resolving the exact TEVB viewpoint episteme P used for the current E/P conformance judgment. Add construction, cross-view, evaluation, or publication objects only when the next work depends on them.

> **Tech-name:** `TEVB`
> **Plain-name:** typical engineering viewpoint bundle for holons

TEVB is one governed `U.ViewpointBundle` packaged by E.17.1. It is not an architecture framework, a method, a set of publication forms, or a second entity beside its four referenced viewpoint epistemes. It fixes a conceptual viewpoint bundle but prescribes no modelling notation, storage format, or tool API.

**Builds on:** E.17.0 for `U.Viewpoint`, `EpistemeViewpointConformanceRelation`, and `U.View`; E.17.1 for bundle packaging by `U.ViewpointRef`; C.2.1 for episteme identity; C.13 for the constituent collections of viewpoint conventions; A.22 for their selected structures; A.6.6 and E.17.0 for exact constituent-dependency relations; A.6.3 for optional view construction; E.24.PUB for publication.

**Used by:** E.18 transformation-flow descriptions, E.17 multi-view publication, architecture-description patterns, and domain patterns that need a reusable engineering concern family for holons.

