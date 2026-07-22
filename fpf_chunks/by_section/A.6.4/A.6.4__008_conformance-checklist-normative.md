---
chunk_kind: "child"
pattern_id: "A.6.4"
pattern_title: "U.EpistemicRetargeting — EntityOfConcern retargeting morphism"
section_id: "A.6.4:8"
section_title: "Conformance Checklist (normative)"
source_path: "FPF-Spec.md"
output_path: "by_section/A.6.4/A.6.4__008_conformance-checklist-normative.md"
commit_sha: "0990ff1d1ccee4587b8f7e16e7a725a8edbe66b4"
heading_path:
  - "A.6.4 — U.EpistemicRetargeting — EntityOfConcern retargeting morphism"
  - "A.6.4:8 — Conformance Checklist (normative)"
line_start: 14642
line_end: 14688
dependencies:
  - "A.6.2"
  - "A.6.3"
  - "A.6.5"
  - "A.7"
  - "C.2"
  - "C.2.1"
  - "C.3"
  - "E.10.D2"
  - "E.18"
  - "F.9"
keywords:
---

### A.6.4:8 - Conformance Checklist (normative)

**CC‑A.6.4‑1 - EFEM species and EntityOfConcernChangeMode.**
Any pattern that claims to define `U.EpistemicRetargeting` **SHALL**:

* declare itself a species of `U.EffectFreeEpistemicMorphing` (A.6.2),
* fix `entityOfConcernChangeMode = retarget`,
* and state its Applicability profile (EntityOfConcernClass pairs, contexts, viewpoints, representation schemes, invariants).

**CC‑A.6.4‑2 - Slot‑level read/write discipline.**
Each species of EpistemicRetargeting **MUST**:
* list the SlotKinds it **reads** (at least `EntityOfConcernSlot`, `GroundingHolonSlot`, `ClaimGraphSlot`, `ViewpointSlot`, `ReferenceSchemeSlot`, plus any C.2.1+ slots used),
* list the SlotKinds it **writes** (at least `EntityOfConcernSlot`, typically also `ClaimGraphSlot`, `ReferenceSchemeSlot`, and `meta`),
* state explicitly how `GroundingHolonSlot` and `ViewpointSlot` behave (preserved vs bridged),
* reference A.6.5 to show that SlotSpecs remain consistent across domain/codomain kinds.

**CC‑A.6.4‑3 - Bridge & invariant declaration.**
Each species SHALL:
* identify the relevant `KindBridge` species (and, where applicable, plane Bridges),
* declare the invariant(s) it preserves (in KD‑CAL/LOG‑CAL terms),
* sketch how invariant preservation is checked or approximated (e.g. through proofs, tests, or statistical guarantees).

**CC‑A.6.4‑4 - SquareLaw‑retargeting witnesses.**
Retargeting species that interact with `E.18` transformation-flow structures or other graph-level transformation structures **MUST**:
* describe the commutative squares (or more general diagrams) that express “evaluate then retarget = retarget then evaluate” up to equivalence,
* identify the corresponding SquareLaw‑retargeting witnesses and how they are represented as epistemes.

**CC-A.6.4-5 - DescriptionContext behaviour for Description-episteme and specification-use cases.**
For retargetings over `…Description`/`…Spec` epistemes:
* laws MUST be phrased in terms of `DescriptionContext = ⟨EntityOfConcernRef, BoundedContextRef, ViewpointRef⟩`,
* `EntityOfConcernRef` MUST change in a way consistent with the declared `KindBridge`,
* `BoundedContextRef` MUST either be preserved or changed only via explicit Context‑Bridges,
* `ViewpointRef` MUST either be preserved or change within a declared `U.ViewpointBundle`.

**CC‑A.6.4‑6 - Separation from Viewing and Mechanisms.**
* Any species that leaves `entityOfConcernRef` unchanged is **not** a conformant EpistemicRetargeting; it belongs to `U.EpistemicViewing` (A.6.3) or another EFEM species.
* Any species that performs measurements, actuation, or other side‑effects MUST be declared as `U.Mechanism`, performed `U.Work`, or another directly governed work/effect value and cannot be an EpistemicRetargeting.

**CC-A.6.4-7 - Retargeting witness and reopen discipline.**
For every FPF-governed retargeting use, the source EntityOfConcern, receiving EntityOfConcern, `KindBridge`, invariant, preserved commitments, withdrawn or new commitments, admissible predicate changes, admissibility value, retargeting witness, and source-bearing reopen condition are recoverable. If bridge or invariant witnessing is insufficient for the intended use, the case records source-bearing reopen, bridge-only comparison, controlled coarsening, report-only use, exploratory use, or named neighboring-pattern handoff.

**CC-A.6.4-8 - Neighboring-pattern handoff.**
Retargeting wording does not carry work authority, evidence force, assurance force, gate passage, abductive selection, temporal adequacy, dynamics law, control relation, bridge substitution, or transformation-flow path currentness unless the governing FPF pattern and project-side FPF kind or reference named by value are named.

**CC-A.6.4-9 - StructuralReinterpretation boundary.**
When `StructuralReinterpretation`, `PathSliceId`, `CrossingRef`, or `DecisionLogRef` is used, the graph, path, constraint, and gate relations stay with `E.18`, `A.20`, or `A.21`. `StructuralReinterpretation` receives retargeting semantics from `A.6.4`; it is not proof of `entityOfConcernRef` continuity and not an `E.18`-local retargeting kind.

