---
chunk_kind: "child"
pattern_id: "E.17.2"
pattern_title: "TEVB - Typical Engineering Viewpoints Bundle"
section_id: "E.17.2:2"
section_title: "Problem  (informative)"
source_path: "FPF-Spec.md"
output_path: "by_section/E.17.2/E.17.2__003_problem-informative.md"
commit_sha: "4b75b56c13f5d61be5238fdbc7c20af5c6f89df7"
heading_path:
  - "E.17.2 — TEVB - Typical Engineering Viewpoints Bundle"
  - "E.17.2:2 — Problem  (informative)"
line_start: 78082
line_end: 78092
dependencies:
  - "A.1"
  - "A.15"
  - "A.2"
  - "A.2.1"
  - "A.6.2-A.6.4"
  - "A.7"
  - "C.2.1"
  - "E.10.D2"
  - "E.17"
  - "E.17.0"
  - "E.17.1"
  - "E.18"
  - "F.18"
  - "U.MultiViewDescribing"
  - "U.ViewpointBundleLibrary"
keywords:
---

### E.17.2:2 - Problem  *(informative)*

Without TEVB, several failure modes recur:
1. **Inconsistent “functional”, “structural”, and “behavioural” vocabularies.** Different teams define “functional view” or “process view” differently, even within one organisation; `E.18:5.12` then has to guess how to map transformation-flow structures onto whichever interpretation is currently in play.
2. **Architecture frameworks leak into the kernel.** 4+1‑style and similar architectural frameworks get hard‑coded as if they were universal; FPF loses its holonic neutrality and becomes biased to a particular school.
3. **Viewpoints conflated with publication faces and publication forms and files.** “Functional view” is used both for the underlying viewpoint and for a concrete document or dashboard; MVPK faces and publication forms, `E.18` transformation-flow families, and EntityOfConcern and Description-episteme and specification-use distinctions become entangled.
4. **Role leakage into EntityOfConcern and Description-episteme boundary and specification-use discipline.** Engineering views that are about holders, role assignments, responsibilities, or device allocation are written directly in terms of `U.Role`, blurring the boundary between work-facing role patterns (`A.2`, `A.2.1`, `A.15`) and description or specification-use lanes, and breaking A.7 and E.10.D2.
5. **Poor reuse across systems.** Even when organisations want to reuse the same engineering views across products, plants, or models, there is no canonical bundle to import; each programme recreates “its own” functional and structural views.

TEVB makes engineering viewpoint families **first‑class reusable bundles** and pins them to an explicit `EntityOfConcernClass` (engineering holons) so that `E.18`, MVPK and discipline-packs can align on the same vocabulary.

