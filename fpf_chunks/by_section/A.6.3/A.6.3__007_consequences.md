---
chunk_kind: "child"
pattern_id: "A.6.3"
pattern_title: "U.EpistemicViewing — describedEntity‑preserving morphism"
section_id: "A.6.3:6"
section_title: "Consequences"
source_path: "FPF-Spec.md"
output_path: "by_section/A.6.3/A.6.3__007_consequences.md"
commit_sha: "eb2832093c1e482d5fdd4985c3d2011ab240b429"
heading_path:
  - "A.6.3 — U.EpistemicViewing — describedEntity‑preserving morphism"
  - "A.6.3:6 — Consequences"
line_start: 10126
line_end: 10150
dependencies:
  - "A.6.0"
  - "A.6.2"
  - "A.6.5"
  - "A.7"
  - "B.5.3"
  - "C.2"
  - "C.2.1"
  - "E.10.D2"
  - "E.17"
  - "E.17.0"
  - "E.17.1"
  - "E.17.2"
  - "E.18"
  - "E.TGA"
  - "U.EffectFreeEpistemicMorphing"
  - "U.EpistemeSlotGraph"
  - "U.MultiViewDescribing"
  - "U.RelationSlotDiscipline"
  - "U.Signature"
keywords:
  - "ClaimGraph"
  - "CorrespondenceModel"
  - "Direct vs Correspondence Viewing"
  - "EpistemicViewing"
  - "RepresentationScheme"
  - "Viewpoint"
  - "describedEntity preservation"
  - "displayed fibration"
  - "episteme"
  - "optics"
  - "view"
---

### A.6.3:6 - Consequences

* **Clear separation of viewing vs retargeting.**
  `U.EpistemicViewing` and `U.EpistemicRetargeting` (A.6.4) now **cleanly separate**:

  * “view of the same entity” vs “description of a different entity under a bridge”, and
  * vertical morphisms (`α` fixed) vs retargeting morphisms (α changes under KindBridge).

* **Stable backbone for multi‑view patterns.**
  Multi‑view description (E.17.0), viewpoint bundle libraries (E.17.1/E.17.2), and MVPK publication now share a **single notion of view morphism**, aligned with C.2.1 slots and the I/D/S discipline.

* **SlotKind-specific discipline for tools.**
  Tools implementing views (queries, projections, report generators, LLM‑based summarisation) must declare:

  * which SlotKinds they read,
  * which SlotKinds they may write,
  * and that `DescribedEntitySlot` is preserved.
    This removes ambiguity around subject/described-entity changes and supports robust static checking.

* **Alignment with modern view/query practices.**
  The pattern aligns with:
  * ISO 42010:2011/2022 and its focus on **viewpoints**, **views**, and **correspondences** over an entity‑of‑interest;
  * SysML v2 “views‑as‑queries” paradigm, where views are queries over a stable model, not new models;
  * post‑2015 work on **optics** and **displayed categories**, treating views as structured projections over a fibred category of epistemes.

