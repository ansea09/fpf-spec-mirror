---
chunk_kind: "child"
pattern_id: "A.6.2"
pattern_title: "U.EffectFreeEpistemicMorphing — Effect‑free morphisms of epistemes"
section_id: "A.6.2:intro"
section_title: "Intro"
source_path: "FPF-Spec.md"
output_path: "by_section/A.6.2/A.6.2__001_intro.md"
commit_sha: "cf12b97913ff82ca8a45ba77d3658ad11e0fdeb6"
heading_path:
  - "A.6.2 — U.EffectFreeEpistemicMorphing — Effect‑free morphisms of epistemes"
  - "A.6.2:intro — Intro"
line_start: 10493
line_end: 10509
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

## A.6.2 - `U.EffectFreeEpistemicMorphing` — Effect‑free morphisms of epistemes
> **Status:** Stable

**One‑line summary.** `U.EffectFreeEpistemicMorphing` (EFEM) is the universal class of **effect-free, law-constrained morphisms between epistemes**. An EFEM morphism rewrites episteme components (ClaimGraph, `entityOfConcernRef`, optional `groundingHolonRef`, `viewpointRef`, `referenceScheme`, and—where C.2.1+ is in use—`representationSchemeRef` and related slots, plus meta) in a **conservative, functorial, reproducible** way, with an explicit mode for what happens to the **EntityOfConcernSlot** (`EntityOfConcernChangeMode ∈ {preserve, retarget}`) as defined by `C.2.1 U.EpistemeSlotRelation`.

**Placement.** After **A.6.1 `U.Mechanism`** and before any specialisations (`A.6.3 U.EpistemicViewing`, `A.6.4 U.EpistemicRetargeting`).

**Builds on.**
A.6.0 `U.Signature` (subject/vocabulary/laws/applicability); A.6.1 `U.Mechanism`; A.6.5 `U.RelationSlotDiscipline`; C.2.1 `U.Episteme — Epistemes and their slot relation`; E.10.D2 (EntityOfConcern and Description-episteme boundary and specification use/refinement gates); C.3.* (Kind‑CAL / KindBridge for EntityOfConcern classes).

**Used by.**
A.6.3 `U.EpistemicViewing`; A.6.4 `U.EpistemicRetargeting`; E.17.0 `U.MultiViewDescribing`; E.17 (MVPK); E.18 (structural reinterpretation over transformation-flow structure).

**EntityOfConcern change-mode discipline.** EFEM uses `EntityOfConcernChangeMode` for the preserve/retarget characteristic over C.2.1's EntityOfConcernSlot / entityOfConcernRef family. Earlier source-side spellings must be normalized to the EntityOfConcern family before conformant use and do not define a second EntityOfConcern ontology.

**Body-level U-kind settlement.** `U.EffectFreeEpistemicMorphing` is the governed durable value in this host. `U.Episteme` is reused from C.2.1; episteme species such as episteme card, view, and publication are dependent episteme or publication values only when C.2.1/E.17 governs them. `ClaimGraph`, `ReferenceScheme`, `Viewpoint`, and related names are ValueKinds or SlotKinds inside the C.2.1 episteme slot relation and A.6.5 SlotSpec discipline. `SubjectRef` is source-migration wiring that decodes through `DescriptionContext`; it is not a second EntityOfConcern ontology. `EpMorphism` below is the local mathematical-lens arrow value for the episteme category, not a root U-kind. Claims about performed work, mechanism application, or presentation carriers leave EFEM and use A.15, A.6.1, E.17, or the direct publication pattern.

