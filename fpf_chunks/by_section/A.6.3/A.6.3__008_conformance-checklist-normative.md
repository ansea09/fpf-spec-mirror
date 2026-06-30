---
chunk_kind: "child"
pattern_id: "A.6.3"
pattern_title: "U.EpistemicViewing — EntityOfConcern-preserving morphism"
section_id: "A.6.3:8"
section_title: "Conformance Checklist (normative)"
source_path: "FPF-Spec.md"
output_path: "by_section/A.6.3/A.6.3__008_conformance-checklist-normative.md"
commit_sha: "c859eed90b5ca9d0f717a1ffb13a841a3b52c016"
heading_path:
  - "A.6.3 — U.EpistemicViewing — EntityOfConcern-preserving morphism"
  - "A.6.3:8 — Conformance Checklist (normative)"
line_start: 11512
line_end: 11552
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

### A.6.3:8 - Conformance Checklist (normative)

**CC‑A.6.3‑1 - EFEM species and EntityOfConcernChangeMode.**
Any pattern that claims to define `U.EpistemicViewing` **SHALL**:

* declare itself a species of `U.EffectFreeEpistemicMorphing` (A.6.2),
* fix `entityOfConcernChangeMode = preserve`,
* and state its Applicability profile (EntityOfConcernClass, contexts, viewpoints, representation schemes).

**CC-A.6.3-2 - SlotKind-specific read/write discipline.**
For each species of EpistemicViewing, the definition **MUST**:

* list the SlotKinds it **reads** (typically `EntityOfConcernSlot`, `GroundingHolonSlot`, `ClaimGraphSlot`, `ViewpointSlot`, `RepresentationSchemeSlot`, `ReferenceSchemeSlot`),
* list the SlotKinds it **writes** (typically `ClaimGraphSlot`, optionally `ViewpointSlot`, `RepresentationSchemeSlot`, `ReferenceSchemeSlot`, and `meta`),
* assert explicitly that `EntityOfConcernSlot` is read‑only,
* and state any constraints on `GroundingHolonSlot` / `ViewpointSlot` changes.

This satisfies A.6.5 and C.2.1 checkpoint CC‑C.2.1‑5.

**CC‑A.6.3‑3 - DescriptionContext discipline (for Description epistemes, including Description epistemes admitted for specification use).**
When domain/codomain epistemes are `…Description`/`…Spec`:
* viewing invariants SHALL be phrased in terms of `DescriptionContext = ⟨EntityOfConcernRef, BoundedContextRef, ViewpointRef⟩`,
* `EntityOfConcernRef` MUST be preserved,
* `BoundedContextRef` MUST be preserved unless a Bridge is explicitly cited,
* `ViewpointRef` MUST either be preserved or changed within a declared `U.ViewpointBundle`.

**CC‑A.6.3‑4 - Conservativity witness.**
For each species, the definition SHALL provide:
* a clear statement of what counts as a **new commitment about the EntityOfConcern** in the relevant discipline,
* and a sketch of how conservativity (EV‑3) is checked or approximated (e.g. via KD‑CAL entailment, proof or structural invariants).

**CC‑A.6.3‑5 - Profile classification.**
* Species that do not require a `CorrespondenceModel` MUST be marked as `U.DirectEpistemicViewing`.
* Species that do require such a model MUST be marked as `U.CorrespondenceEpistemicViewing` and SHALL:
  * document the shape of the `CorrespondenceModel`,
  * describe how witness epistemes ensure oplax naturality of compositions.

**CC‑A.6.3‑6 - Separation from Retargeting and Mechanisms.**
* Any species that may change `entityOfConcernRef` is **not** a conformant EpistemicViewing; it MUST be treated as `U.EpistemicRetargeting` (A.6.4) or as a different pattern.
* Any species that performs measurements, actuation, or other side‑effects MUST be declared as `U.Mechanism`, performed `U.Work`, or another directly governed work/effect value and cannot be an EpistemicViewing.

