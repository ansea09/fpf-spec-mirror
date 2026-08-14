---
chunk_kind: "child"
pattern_id: "A.6.2"
pattern_title: "U.EffectFreeEpistemicMorphing — Effect‑free morphisms of epistemes"
section_id: "A.6.2:intro"
section_title: "Intro"
source_path: "FPF-Spec.md"
output_path: "by_section/A.6.2/A.6.2__001_intro.md"
commit_sha: "7205ce8cea50eb778520a026373b2b7bcbc43fbb"
heading_path:
  - "A.6.2 — U.EffectFreeEpistemicMorphing — Effect‑free morphisms of epistemes"
  - "A.6.2:intro — Intro"
line_start: 12915
line_end: 12938
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
> **Type:** Definitional ontic pattern

**One-line summary.** `U.EffectFreeEpistemicMorphing` (EFEM) is the universal class of **effect-free, law-constrained morphisms between epistemes**. An EFEM morphism transforms one exact episteme into another and states what happens to claim content, the exact EntityOfConcern, and the effective ReferenceScheme when that scheme is material. Grounding and any viewpoint selected for a named describing use remain separately identified. The morphism declares `EntityOfConcernChangeMode` as either `preserve` or `retarget` under C.2.1.

**Use this pattern when** a project needs to transform an episteme into another episteme while preserving the distinction between episteme-only change, EntityOfConcern retargeting, publication rendering, mechanism application, and performed work.

**What goes wrong if missed.** A view, retargeting, refinement, representation change, publication rendering, mechanism application, or work occurrence is treated as the same operation, so the project can no longer tell whether the EntityOfConcern changed or only the episteme changed.

**What this buys.** EFEM gives one law-constrained episteme-to-episteme morphism discipline with explicit preserve/retarget mode, clear boundaries among actual values, declaration-local participant meanings, and references, plus conservativity and composition conditions.

**Placement.** After **A.6.1 `U.Mechanism`** and before any specialisations (`A.6.3 U.EpistemicViewing`, `A.6.4 U.EpistemicRetargeting`).

**Builds on.**
A.6.0 `U.Signature` for subject, vocabulary, laws, and applicability; A.6.1 `U.Mechanism`; A.6.5 for declaration-local SlotSpecs; C.2.1 for `U.Episteme` identity and direct constitution, empirical-grounding, and edition relations; E.10.D2 for the EntityOfConcern, Description-episteme, describing-use, and specification-use boundary; and C.3 plus F.9 for kind-level and exact cross-local reasoning.

**Used by.**
A.6.3 `U.EpistemicViewing`; A.6.4 `U.EpistemicRetargeting`; E.17.0 `U.MultiViewDescribing`; E.17 (MVPK); E.18 (structural reinterpretation over transformation-flow structure).

**EntityOfConcern change-mode discipline.** EFEM uses `EntityOfConcernChangeMode` for the preserve/retarget characteristic over the exact C.2.1 EntityOfConcern designated by `entityOfConcernRef`. Earlier source-side spellings must be normalized to the EntityOfConcern family before conformant use and do not define a second EntityOfConcern ontology.

**Body-level U-kind settlement.** `U.EffectFreeEpistemicMorphing` is the durable value defined in this pattern. `U.Episteme` is reused from C.2.1; an episteme card, view, or publication is a dependent episteme or publication value only when C.2.1 and E.17 define or constrain it. `ClaimGraph` and `ReferenceScheme` are C.2.1 values, while a viewpoint selected for one describing use is a separate use qualification. `SubjectRef` is only a legacy source-wiring name: recover the exact episteme, its EntityOfConcern, and any material scheme or use-level viewpoint instead of treating the name as a second ontology. `EpMorphism` below is the local mathematical-lens arrow value for the episteme category, not a root U-kind. Claims about performed Work use A.15.1; mechanism application uses A.6.1 and E.20; publication form, face, and carrier use E.17 and E.24.PUB. None is an EFEM claim merely because the same source mentions it.

