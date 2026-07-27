---
chunk_kind: "child"
pattern_id: "E.17.0"
pattern_title: "U.MultiViewDescribing - Viewpoints, Views & Correspondences"
section_id: "E.17.0:2"
section_title: "Problem  (informative, but sharp)"
source_path: "FPF-Spec.md"
output_path: "by_section/E.17.0/E.17.0__003_problem-informative-but-sharp.md"
commit_sha: "60caecb4751fb2a3623a1faaca757d29a19acff9"
heading_path:
  - "E.17.0 — U.MultiViewDescribing - Viewpoints, Views & Correspondences"
  - "E.17.0:2 — Problem  (informative, but sharp)"
line_start: 77072
line_end: 77095
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

### E.17.0:2 - Problem  *(informative, but sharp)*

Without `U.MultiViewDescribing`:

1. **Viewpoints, views, publication-face-kind values, and carrier renderings collapse.**
   In practice, “architecture view”, “diagram”, “spec”, and “published deck” are used interchangeably. This:

   * confuses *episteme* (`U.View`) with publication-face-kind values (`publication face/form` or `interop publication form`) or with a concrete carrier rendering,
   * hides which **concerns and stakeholders** a description is written for,
   * makes it impossible to check whether a given description family is “complete enough” for a chosen viewpoint library.

2. **Descriptions float without viewpoints.**
   EntityOfConcern and Description-episteme boundary and specification-use refinement discipline distinguishes the EntityOfConcern from Description epistemes, including Description epistemes admitted for specification use, but does not, on its own, forbid “view‑from‑nowhere” descriptions (no declared viewpoint). That contradicts the pragmatic stance encoded in C.2.1: **no episteme without concerns**.

3. **Each domain reinvents multi‑view semantics.**
   Architecture, safety cases, governance frameworks, and research engineering processes all use local notions of “view”, “viewpoint”, and “consistency between views”. Without a shared pattern:

   * `E.18`, MVPK, and discipline packs introduce their own “view” rules and invariants, duplicating work;
   * cross‑domain reasoning (e.g. mapping a safety view to an architecture view) becomes ad‑hoc;
   * we cannot give a single formal story for consistency, correspondence, and EpistemicViewing across families of descriptions.

4. **No place to attach correspondence.**
   ISO 42010‑style *correspondences* and modern BX/consistency relations have nowhere canonical to live. We need a **CorrespondenceModel over families of Description epistemes, including Description epistemes admitted for specification use** that integrates with `U.EpistemicViewing`, `U.EpistemicRetargeting`, and C.2.1’s slot relation.

