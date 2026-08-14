---
chunk_kind: "child"
pattern_id: "A.6.2"
pattern_title: "U.EffectFreeEpistemicMorphing — Effect‑free morphisms of epistemes"
section_id: "A.6.2:3"
section_title: "Forces"
source_path: "FPF-Spec.md"
output_path: "by_section/A.6.2/A.6.2__004_forces.md"
commit_sha: "7205ce8cea50eb778520a026373b2b7bcbc43fbb"
heading_path:
  - "A.6.2 — U.EffectFreeEpistemicMorphing — Effect‑free morphisms of epistemes"
  - "A.6.2:3 — Forces"
line_start: 12974
line_end: 12990
dependencies:
  - "A.1"
  - "A.6.0"
  - "A.6.1"
  - "A.6.3"
  - "A.6.4"
  - "A.6.5"
  - "C.2.1"
  - "C.3"
  - "E.10.D2"
  - "E.17"
  - "E.17.0"
  - "E.18"
  - "U.EpistemicRetargeting"
  - "U.EpistemicViewing"
  - "U.Mechanism"
  - "U.Signature"
keywords:
---

### A.6.2:3 - Forces

* **Epistemic purity vs operational power.**
  Effect-free episteme transforms are attractive precisely because they can be reasoned about algebraically and composed freely. But the more operational power they are given (IO, solver calls, measurements), the less they remain “pure” and the more they belong under `U.Mechanism` or performed `U.Work` as defined in A.15.

* **Preserve vs retarget.**
  Viewing is entityOfConcern‑preserving; reinterpretation along a KindBridge is entityOfConcern-retargeting. Both are important, but **they must be distinguished and witnessed differently**.

* **Conservativity vs usefulness.**
  EFEM should be **conservative**: no new commitments about the EntityOfConcern beyond what input epistemes already entail. At the same time, transformations may *factor*, *aggregate*, or *normalise* content, which may drop information or change representation when the loss and interpretation rule are explicit.

* **Locality vs reference planes and Bridges.**
  Epistemes live on **reference planes** (C.2.1). When a use relates distinct source-local senses or crosses a reference plane, apply the exact F.9 Bridge or plane relation and its reliance consequences. EFEM cannot hide either change inside a “pure” content rewrite.

* **EntityOfConcern and Description-episteme boundary and specification-use refinement.**
  The EntityOfConcern is not identical to the Description episteme produced by this use; it may itself be `U.Episteme` when an episteme is under concern. `...Description` names a Description episteme, and `...Spec` names a Description episteme admitted for specification use only when its claims are checkable and the named harness or validation relation can test them. When a describing use selects a viewpoint, name that use and exact viewpoint separately; selection is neither an episteme constituent nor conformance. EFEM states whether claim content, EntityOfConcern, grounding, effective scheme when material, and any selected use-level viewpoint are preserved or changed, while keeping EntityOfConcern, Description episteme, specification use, publication form, publication unit, carrier, and rendering distinct (A.7, E.10.D2).

