---
chunk_kind: "child"
pattern_id: "E.17.0"
pattern_title: "U.MultiViewDescribing — Viewpoints, Views & Correspondences"
section_id: "E.17.0:3"
section_title: "Forces  (informative)"
source_path: "FPF-Spec.md"
output_path: "by_section/E.17.0/E.17.0__004_forces-informative.md"
commit_sha: "725f0b7b372754cda3f6f4e15184215da568fc4d"
heading_path:
  - "E.17.0 — U.MultiViewDescribing — Viewpoints, Views & Correspondences"
  - "E.17.0:3 — Forces  (informative)"
line_start: 55464
line_end: 55474
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

### E.17.0:3 - Forces  *(informative)*

| Force                                  | Tension                                                                                                                                                                                |
| -------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Universality vs domain idioms**      | One pattern should handle engineering, safety, governance, research, etc. ↔ domain communities expect their own jargon (architecture description, safety case, dossier…).              |
| **Viewpoint locality vs reuse**        | Viewpoints must be local to families of descriptions (`EoIClass`, Context) ↔ we want reusable **viewpoint bundles** (libraries) across projects and domains.                           |
| **I/D/S strictness vs pragmatics**     | Intension ≠ Episteme; D/S are epistemes with DescriptionContext ↔ engineers think in “views over a system”, not in pure I/D/S algebra.                                                 |
| **Slot discipline vs approachability** | C.2.1 and A.6.5 give a clean SlotKind, ValueKind, and RefKind discipline ↔ authors want to talk about “functional view” and “safety view” without carrying all slot jargon in didactic support content. |
| **Epistemic versus publication-form and carrier lanes** | Views (epistemes) must be clearly separated from `PublicationSurface` and `InteropSurface` kinds and carriers ↔ authors often conflate “viewpoint”, “view”, and “document”.                                         |
| **Consistency vs incremental change**  | We want tight correspondence between views ↔ views evolve asynchronously; partial inconsistency must be representable and repairable (BX‑style).                                      |

