---
chunk_kind: "child"
pattern_id: "A.6.4"
pattern_title: "U.EpistemicRetargeting — describedEntity‑retargeting morphism"
section_id: "A.6.4:8"
section_title: "Conformance checklist (normative)"
source_path: "FPF-Spec.md"
output_path: "by_section/A.6.4/A.6.4__009_conformance-checklist-normative.md"
commit_sha: "04dd733fb18b66d3a640d11758e0af22ea253fd8"
heading_path:
  - "A.6.4 — U.EpistemicRetargeting — describedEntity‑retargeting morphism"
  - "A.6.4:8 — Conformance checklist (normative)"
line_start: 11911
line_end: 11957
dependencies:
  - "A.1"
  - "A.6.2"
  - "C.2"
  - "C.2.1"
  - "E.18"
  - "E.TGA"
  - "F.9"
  - "U.EpistemeSlotGraph"
  - "U.EpistemicRetargeting"
keywords:
  - "KindBridge"
  - "SquareLaw-retargeting"
  - "StructuralReinterpretation"
  - "describedEntity shift"
  - "retargeting"
  - "subject retargeting"
---

### A.6.4:8 - Conformance checklist (normative)

**CC‑A.6.4‑1 - EFEM species and DescribedEntityChangeMode.**
Any pattern that claims to define `U.EpistemicRetargeting` **SHALL**:

* declare itself a species of `U.EffectFreeEpistemicMorphing` (A.6.2),
* fix `describedEntityChangeMode = retarget`,
* and state its Applicability profile (EoI‑pairs, contexts, viewpoints, representation schemes, invariants).

**CC‑A.6.4‑2 - Slot‑level read/write discipline.**
Each species of EpistemicRetargeting **MUST**:
* list the SlotKinds it **reads** (at least `DescribedEntitySlot`, `GroundingHolonSlot`, `ClaimGraphSlot`, `ViewpointSlot`, `ReferenceSchemeSlot`, plus any C.2.1+ slots used),
* list the SlotKinds it **writes** (at least `DescribedEntitySlot`, typically also `ClaimGraphSlot`, `ReferenceSchemeSlot`, and `meta`),
* state explicitly how `GroundingHolonSlot` and `ViewpointSlot` behave (preserved vs bridged),
* reference A.6.5 to show that SlotSpecs remain consistent across domain/codomain kinds.

**CC‑A.6.4‑3 - Bridge & invariant declaration.**
Each species SHALL:
* identify the relevant `KindBridge` species (and, where applicable, plane Bridges),
* declare the invariant(s) it preserves (in KD‑CAL/LOG‑CAL terms),
* sketch how invariant preservation is checked or approximated (e.g. through proofs, tests, or statistical guarantees).

**CC‑A.6.4‑4 - SquareLaw‑retargeting witnesses.**
Retargeting species that interact with E.TGA or other graph-level transductions **MUST**:
* describe the commutative squares (or more general diagrams) that express “evaluate then retarget = retarget then evaluate” up to equivalence,
* identify the corresponding SquareLaw‑retargeting witnesses and how they are represented as epistemes.

**CC‑A.6.4‑5 - D/S‑context behaviour.**
For retargetings over `…Description`/`…Spec` epistemes:
* laws MUST be phrased in terms of `DescriptionContext = ⟨DescribedEntityRef, BoundedContextRef, ViewpointRef⟩`,
* `DescribedEntityRef` MUST change in a way consistent with the declared `KindBridge`,
* `BoundedContextRef` MUST either be preserved or changed only via explicit Context‑Bridges,
* `ViewpointRef` MUST either be preserved or change within a declared `U.ViewpointBundle`.

**CC‑A.6.4‑6 - Separation from Viewing and Mechanisms.**
* Any species that leaves `describedEntityRef` unchanged is **not** a conformant EpistemicRetargeting; it belongs to `U.EpistemicViewing` (A.6.3) or another EFEM species.
* Any species that performs measurements, actuation, or other side‑effects MUST be declared as `U.Mechanism`/`U.WorkEnactment` and cannot be an EpistemicRetargeting.

**CC-A.6.4-7 - Retargeting witness and reopen discipline.**
For every load-bearing retargeting use, the source described entity, receiving described entity, `KindBridge`, invariant, preserved commitments, withdrawn or new commitments, admissible predicate changes, support posture, retargeting witness, and source-bearing reopen condition are recoverable. If bridge or invariant support is insufficient for the intended use, the case records source-bearing reopen, bridge support, controlled coarsening, report-only use, exploratory use, or named neighboring-pattern handoff.

**CC-A.6.4-8 - Neighboring-pattern handoff.**
Retargeting wording does not carry work authority, evidence force, assurance force, gate passage, abductive selection, temporal adequacy, dynamics law, control relation, bridge substitution, or TGA-path currentness unless the exact governing FPF pattern and exact project-side FPF kind or reference are named.

**CC-A.6.4-9 - StructuralReinterpretation boundary.**
When `StructuralReinterpretation`, `PathSliceId`, `CrossingRef`, or `DecisionLogRef` is used, the graph, path, constraint, and gate relations stay with `E.18`, `A.20`, or `A.21`. `StructuralReinterpretation` receives retargeting semantics from `A.6.4`; it is not proof of same-described-entity continuity and not a TGA-local retargeting kind.

