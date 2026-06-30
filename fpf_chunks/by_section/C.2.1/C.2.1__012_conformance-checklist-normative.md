---
chunk_kind: "child"
pattern_id: "C.2.1"
pattern_title: "U.Episteme - Epistemes and their slot relation"
section_id: "C.2.1:11"
section_title: "Conformance Checklist  (normative)"
source_path: "FPF-Spec.md"
output_path: "by_section/C.2.1/C.2.1__012_conformance-checklist-normative.md"
commit_sha: "e264bfb1cdeecdfe1b7407deba14165475c20ac7"
heading_path:
  - "C.2.1 — U.Episteme - Epistemes and their slot relation"
  - "C.2.1:11 — Conformance Checklist  (normative)"
line_start: 37386
line_end: 37451
dependencies:
  - "A.1"
  - "A.6.2-A.6.4"
  - "A.6.5"
  - "A.7"
  - "B.1.3"
  - "C.2"
  - "C.2.1"
  - "E.10.D2"
  - "E.17"
  - "E.17.0-E.17.2"
  - "E.18"
keywords:
---

### C.2.1:11 - Conformance Checklist  *(normative)*

**CC‑C.2.1‑1 - Minimal core components for episteme species.**
Any species of `U.Episteme` that participates in the boundary between `EntityOfConcern` and Description episteme discipline, specification use and refinement, or E.17 multi-view and publishing **MUST** be representable as `U.EpistemeCard` or `U.EpistemeView` with at least:

```
content            : U.ClaimGraph
entityOfConcernRef : U.EntityRef
groundingHolonRef? : U.HolonRef
viewpointRef?      : U.ViewpointRef
referenceScheme?   : U.ReferenceScheme      // ByValue
meta               : ...                      // edition, provenance, status (A.7 and F.15)
```

and corresponding SlotSpecs consistent with A.6.5 (`EntityOfConcernSlot`, `GroundingHolonSlot`, `ClaimGraphSlot`, `ViewpointSlot`, `ReferenceSchemeSlot`).

**CC‑C.2.1‑2 - No durable U-kind for “EntityOfConcern” or “GroundingHolon”.**
Patterns **MUST NOT** introduce durable U-kinds `U.EntityOfConcern` or `U.GroundingHolon`:
* EntityOfConcernSlot has ValueKind `U.Entity` ( species‑constrained via EntityOfConcernClass if needed),
* GroundingHolonSlot has ValueKind `U.Holon`.

Plain terms "EntityOfConcern value" and "grounding holon" are allowed only as **slot-filler descriptions** under the declared SlotKind, ValueKind, and RefKind discipline.

**CC-C.2.1-3 - SlotKind, ValueKind, and RefKind discipline.**
All episteme‑related slots, including `EntityOfConcernSlot`, `GroundingHolonSlot`, `ClaimGraphSlot`, `ViewpointSlot`, `ViewSlot`, `ReferenceSchemeSlot` (and any extensions in C.2.1+), **MUST**:
* follow the naming discipline of A.6.5 (`*Slot` for SlotKinds, `*Ref` only for RefKinds or fields),
* declare a ValueKind and refMode (`ByValue` or a RefKind),
* be used consistently across patterns that refer to the same conceptual position.

**CC‑C.2.1‑4 - DescriptionContext wiring.**
Any episteme species whose name or pattern claims to be a `…Description` or `…Spec` in the sense of E.10.D2 **MUST**:
* expose `subjectRef : U.SubjectRef`,
* provide a decoding to `DescriptionContext = ⟨EntityOfConcernRef, BoundedContextRef, ViewpointRef⟩`,
* ensure that `EntityOfConcernRef` matches `entityOfConcernRef` (EntityOfConcernSlot), and
* ensure that `ViewpointRef` matches `viewpointRef` or is derivable from a `U.ViewpointBundle` under documented rules.

**CC‑C.2.1‑5 - Morphism declarations over slots.**
Any pattern in A.6.2–A.6.4, E.17, E.18, or discipline packs that defines morphisms between epistemes **SHALL**:
* state whether it is a species of `U.EffectFreeEpistemicMorphing`, `U.EpistemicViewing`, or `U.EpistemicRetargeting`,
* declare its `entityOfConcernChangeMode` (`preserve` or `retarget`),
* name which SlotKinds it reads and writes,
* state its behaviour on `entityOfConcernRef`, `groundingHolonRef`, `viewpointRef`, and `referenceScheme`.

**CC-C.2.1-5a - Episteme and publication relation-position split for semio-facing terms.**
Any pattern, publication-form profile, evidence-use note, or FPF-facing term that uses pre-FPF sign vocabulary, explanation, publication, source cues, authority-looking cases, or reader reliance **MUST** name the claim-bearing value as `U.Episteme`, `U.EpistemePublication`, or a declared species of `U.Episteme`. When publication is current, it **MUST** separately name the publication form, `U.View` or MVPK face, carrier or rendering, source-finding cue, and either `governingPatternRef` or `authoritySourceRef` when interpretation or use depends on a named authority reference. It **MUST NOT** use generic semio wording, generic source wording, generic project-work wording, or container-placement wording as solution terms.

**CC-C.2.1-6 - Semantic-triangle usage guard.**

If a semantic triangle or parallelogram diagram appears in a pattern or tutorial, there must be an explicit note that:
* it is a didactic projection of `U.EpistemeSlotRelation`, and
* normative laws are stated in terms of C.2.1 slots, graph-valued fillers such as `ClaimGraph`, and morphisms, not in terms of triangle corners.

**CC-C.2.1-7 - KD-CAL and ReferencePlane alignment.**
Any pattern that evaluates or compares epistemes (KD-CAL, LOG-CAL, CHR, CG-Spec, etc.) **MUST** point out:
* how `U.ClaimGraph` is interpreted in a ReferencePlane,
* how `GroundingHolonSlot` figures into measurement or validation,

**CC‑C.2.1‑8 - Context locality and Bridges.**
Any `U.Episteme` species that is consumed by KD-CAL, LOG-CAL, or CHR-based patterns **SHALL** declare a `U.BoundedContextRef`; all F-G-R computations and C.2.1 slot interpretations are **context-local**. Cross-context use **MUST** proceed via an explicit Bridge with CL and Phi-policy (F.9 and B.3), with penalties applied to the R component only; F and the slot structure from C.2.1 remain unchanged.

**CC‑C.2.1‑9 - Carriers and Work outside episteme content.**
C.2.1 **inherits** the current A.7 strict distinction plus C.2.1 slot-relation, E.17 publication and carrier, A.10 evidence-use and provenance, B.3 assurance, A.2 and A.2.1 role-assignment, A.15 work, and A.3.4 transformation discipline: `U.PresentationCarrier` values, publication-side values, `U.Work` occurrences, and role assignments **MUST NOT** be treated as parts of `U.Episteme` or as values of any SlotKind in `U.EpistemeSlotRelation`. Episteme content stays in `U.ClaimGraph` and `U.ReferenceScheme`; evidence enters only through an A.10 evidence-provenance graph relation or B.3 assurance-evidence input that points to evidence-producing or evidence-interpreting `U.Work` occurrences, carrier and source-currentness records, and role assignments when those are current. Changing carriers or re-publishing work alone does **not** change the episteme determined by the filled `content`, `entityOfConcernRef`, and effective `referenceScheme` positions in its `U.BoundedContext`.

**CC‑C.2.1‑10 - Reflexive entityOfConcern guard.**
When an episteme uses C.2.1 to speak **about** another episteme (ReferencePlane = episteme), or about itself (self-describing or meta-specification cases), patterns **SHALL** ensure that the resulting JustificationGraph and evaluation chains are **acyclic** along justification paths. Reflexive `describe` or citation edges may exist as literature references, but they MUST NOT form minimal justification cycles for acceptance or KD-CAL assurance decisions; the trust calculus MUST always bottom out in separated evidence relation material, such as evidence-producing or evidence-interpreting `U.Work` plus an A.10 evidence-provenance graph relation or B.3 assurance-evidence input, rather than in purely self-referential claims.

