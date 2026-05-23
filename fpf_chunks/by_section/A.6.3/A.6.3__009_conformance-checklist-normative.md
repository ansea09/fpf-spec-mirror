---
chunk_kind: "child"
pattern_id: "A.6.3"
pattern_title: "U.EpistemicViewing — describedEntity‑preserving morphism"
section_id: "A.6.3:8"
section_title: "Conformance checklist (normative)"
source_path: "FPF-Spec.md"
output_path: "by_section/A.6.3/A.6.3__009_conformance-checklist-normative.md"
commit_sha: "04dd733fb18b66d3a640d11758e0af22ea253fd8"
heading_path:
  - "A.6.3 — U.EpistemicViewing — describedEntity‑preserving morphism"
  - "A.6.3:8 — Conformance checklist (normative)"
line_start: 10174
line_end: 10214
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

### A.6.3:8 - Conformance checklist (normative)

**CC‑A.6.3‑1 - EFEM species and DescribedEntityChangeMode.**
Any pattern that claims to define `U.EpistemicViewing` **SHALL**:

* declare itself a species of `U.EffectFreeEpistemicMorphing` (A.6.2),
* fix `describedEntityChangeMode = preserve`,
* and state its Applicability profile (EoIClass, contexts, viewpoints, representation schemes).

**CC-A.6.3-2 - SlotKind-specific read/write discipline.**
For each species of EpistemicViewing, authors **MUST**:

* list the SlotKinds it **reads** (typically `DescribedEntitySlot`, `GroundingHolonSlot`, `ClaimGraphSlot`, `ViewpointSlot`, `RepresentationSchemeSlot`, `ReferenceSchemeSlot`),
* list the SlotKinds it **writes** (typically `ClaimGraphSlot`, optionally `ViewpointSlot`, `RepresentationSchemeSlot`, `ReferenceSchemeSlot`, and `meta`),
* assert explicitly that `DescribedEntitySlot` is read‑only,
* and state any constraints on `GroundingHolonSlot` / `ViewpointSlot` changes.

This satisfies A.6.5 and C.2.1 checkpoint CC‑C.2.1‑5.

**CC‑A.6.3‑3 - DescriptionContext discipline (for D/S epistemes).**
When domain/codomain epistemes are `…Description`/`…Spec`:
* viewing invariants SHALL be phrased in terms of `DescriptionContext = ⟨DescribedEntityRef, BoundedContextRef, ViewpointRef⟩`,
* `DescribedEntityRef` MUST be preserved,
* `BoundedContextRef` MUST be preserved unless a Bridge is explicitly cited,
* `ViewpointRef` MUST either be preserved or changed within a declared `U.ViewpointBundle`.

**CC‑A.6.3‑4 - Conservativity witness.**
For each species, authoring SHALL provide:
* a clear statement of what counts as a **new intensional claim** in the relevant discipline,
* and a sketch of how conservativity (EV‑3) is checked or approximated (e.g. via KD‑CAL entailment, proof-support invariants, or structural invariants).

**CC‑A.6.3‑5 - Profile classification.**
* Species that do not require a `CorrespondenceModel` MUST be marked as `U.DirectEpistemicViewing`.
* Species that do require such a model MUST be marked as `U.CorrespondenceEpistemicViewing` and SHALL:
  * document the shape of the `CorrespondenceModel`,
  * describe how witness epistemes ensure oplax naturality of compositions.

**CC‑A.6.3‑6 - Separation from Retargeting and Mechanisms.**
* Any species that may change `describedEntityRef` is **not** a conformant EpistemicViewing; it MUST be treated as `U.EpistemicRetargeting` (A.6.4) or as a different pattern.
* Any species that performs measurements, actuation, or other side‑effects MUST be declared as `U.Mechanism`/`U.WorkEnactment` and cannot be an EpistemicViewing.

