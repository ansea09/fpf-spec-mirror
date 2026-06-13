---
chunk_kind: "child"
pattern_id: "E.17.0"
pattern_title: "U.MultiViewDescribing — Viewpoints, Views & Correspondences"
section_id: "E.17.0:3"
section_title: "Forces  (informative)"
source_path: "FPF-Spec.md"
output_path: "by_section/E.17.0/E.17.0__004_forces-informative.md"
commit_sha: "cb17c555f343780e31e5fea236a74adc69295736"
heading_path:
  - "E.17.0 — U.MultiViewDescribing — Viewpoints, Views & Correspondences"
  - "E.17.0:3 — Forces  (informative)"
line_start: 63514
line_end: 63524
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
  - "U.EpistemeSlotRelation"
  - "U.EpistemicRetargeting"
  - "U.EpistemicViewing"
  - "U.ViewpointBundleLibrary"
keywords:
---

### E.17.0:3 - Forces  *(informative)*

| Force                                  | Tension                                                                                                                                                                                |
| -------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Universality vs domain idioms**      | One pattern should handle engineering, safety, governance, research, etc. ↔ domain communities expect their own jargon (architecture description, safety case, dossier…).              |
| **Viewpoint locality vs reuse**        | Viewpoints must be local to families of descriptions (`EntityOfConcernClass`, Context) ↔ we want reusable **viewpoint bundles** (libraries) across projects and domains.                           |
| **EntityOfConcern and Description-episteme boundary and specification-use strictness vs pragmatics** | The EntityOfConcern for this describing use is not the produced Description episteme or its specification use, although an episteme may itself be the current EntityOfConcern; Description is an episteme use and Specification is a checkability/formality/harness-gated use or refinement of a Description episteme with `DescriptionContext` ↔ engineers think in “views over a system”, not in pure slot-relation algebra. |
| **Slot discipline vs approachability** | C.2.1 and A.6.5 give a clean SlotKind, ValueKind, and RefKind discipline ↔ working users need to talk about “functional view” and “safety view” without carrying all slot jargon in didactic explanatory text. |
| **Epistemic versus publication-form and carrier lanes** | Views (epistemes) must be clearly separated from `publication face/form` and `interop publication form` kinds and carriers ↔ working practice often conflates “viewpoint”, “view”, and “document”.                                         |
| **Consistency vs incremental change**  | We want tight correspondence between views ↔ views evolve asynchronously; partial inconsistency must be representable and repairable (BX‑style).                                      |

