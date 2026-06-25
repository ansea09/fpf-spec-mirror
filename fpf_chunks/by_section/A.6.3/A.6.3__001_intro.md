---
chunk_kind: "child"
pattern_id: "A.6.3"
pattern_title: "U.EpistemicViewing — EntityOfConcern-preserving morphism"
section_id: "A.6.3:intro"
section_title: "Intro"
source_path: "FPF-Spec.md"
output_path: "by_section/A.6.3/A.6.3__001_intro.md"
commit_sha: "b0368ed8d883c04d0b261b03f46c28e23d790dc5"
heading_path:
  - "A.6.3 — U.EpistemicViewing — EntityOfConcern-preserving morphism"
  - "A.6.3:intro — Intro"
line_start: 11098
line_end: 11120
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
keywords:
---

## A.6.3 - `U.EpistemicViewing` — EntityOfConcern-preserving morphism
> **Status:** Stable
> **Type:** Definitional ontic pattern

**One‑line summary.** `U.EpistemicViewing` is the **EntityOfConcern-preserving** species of `U.EffectFreeEpistemicMorphing`: an effect‑free projection between epistemes that may change content and representation, but **never changes what the episteme is about** (the value filling `EntityOfConcernSlot` in C.2.1).
**Use this pattern when** a project needs a view, query, projection, normalization, or representation change over an episteme while preserving the same EntityOfConcern.

**What goes wrong if missed.** A view becomes a retargeting, a publication rendering becomes the episteme relation, or a representation lens silently changes what the episteme is about.

**What this buys.** A.6.3 gives the preserve branch of EFEM: `EntityOfConcernSlot` is read-only, slot changes are declared, and publication, retargeting, mechanism, and work claims stay outside viewing.

**EntityOfConcern preservation discipline.** A.6.3 names the preserve branch of the C.2.1 EntityOfConcern preservation law: `entityOfConcernRef(Y) = entityOfConcernRef(X)` and `EntityOfConcernSlot` is read-only. Source-side spellings are source wording only; conformant text normalizes them to `EntityOfConcern*` before use.

**Placement.** After **A.6.2 `U.EffectFreeEpistemicMorphing`**, before **A.6.4 `U.EpistemicRetargeting`**.

**Builds on.**
A.6.0 `U.Signature`; A.6.2 `U.EffectFreeEpistemicMorphing`; A.6.5 `U.RelationSlotDiscipline`; A.7 and E.10.D2 (EntityOfConcern and Description-episteme boundary and specification use/refinement discipline, `DescriptionContext`); C.2.1 `U.Episteme — Epistemes and their slot relation`; C.2 (KD‑CAL/LOG‑CAL, `subjectRef`, ReferencePlane).

**Used by.**
E.17.0 `U.MultiViewDescribing`; E.17 (MVPK — Multi‑View Publication Kit); E.17.1/E.17.2 (Viewpoint bundle libraries, TEVB); B.5.3 (Role‑EpistemicViewing); discipline packs for architecture, safety, and ML/LLM‑based representations.

**Body-level U-kind settlement.** `U.EpistemicViewing` is the governed durable value in this pattern. It reuses `U.EffectFreeEpistemicMorphing` and `U.Episteme`; episteme card, view, and publication names are dependent C.2.1/E.17 values when those patterns govern them. `ClaimGraph`, `Viewpoint`, `ReferenceScheme`, and `RepresentationScheme` are C.2.1/A.6.5 slot fillers or ValueKinds. `SubjectRef` is source wiring through `DescriptionContext`. `EpMorphism` is the local mathematical-lens arrow value for viewing, not a root U-kind.

