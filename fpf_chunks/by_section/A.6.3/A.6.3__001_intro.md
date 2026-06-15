---
chunk_kind: "child"
pattern_id: "A.6.3"
pattern_title: "U.EpistemicViewing — EntityOfConcern-preserving morphism"
section_id: "A.6.3:intro"
section_title: "Intro"
source_path: "FPF-Spec.md"
output_path: "by_section/A.6.3/A.6.3__001_intro.md"
commit_sha: "c092a1f2299d88d42db012f3184aeff205c13219"
heading_path:
  - "A.6.3 — U.EpistemicViewing — EntityOfConcern-preserving morphism"
  - "A.6.3:intro — Intro"
line_start: 10979
line_end: 10991
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

**One‑line summary.** `U.EpistemicViewing` is the **EntityOfConcern-preserving** species of `U.EffectFreeEpistemicMorphing`: an effect‑free projection between epistemes that may change content and representation, but **never changes what the episteme is about** (the value filling `EntityOfConcernSlot` in C.2.1).
**EntityOfConcern preservation discipline.** A.6.3 names the preserve branch of the C.2.1 EntityOfConcern preservation law: `entityOfConcernRef(Y) = entityOfConcernRef(X)` and `EntityOfConcernSlot` is read-only. Earlier source-side spellings are source-migration wording only; conformant text normalizes them to `EntityOfConcern*` before use.

**Placement.** After **A.6.2 `U.EffectFreeEpistemicMorphing`**, before **A.6.4 `U.EpistemicRetargeting`**.

**Builds on.**
A.6.0 `U.Signature`; A.6.2 `U.EffectFreeEpistemicMorphing`; A.6.5 `U.RelationSlotDiscipline`; A.7 and E.10.D2 (EntityOfConcern and Description-episteme boundary and specification use/refinement discipline, `DescriptionContext`); C.2.1 `U.Episteme — Epistemes and their slot relation`; C.2 (KD‑CAL/LOG‑CAL, `subjectRef`, ReferencePlane).

**Used by.**
E.17.0 `U.MultiViewDescribing`; E.17 (MVPK — Multi‑View Publication Kit); E.17.1/E.17.2 (Viewpoint bundle libraries, TEVB); B.5.3 (Role‑EpistemicViewing); discipline packs for architecture, safety, and ML/LLM‑based representations.

