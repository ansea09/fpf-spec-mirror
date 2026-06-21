---
chunk_kind: "child"
pattern_id: "A.6.3"
pattern_title: "U.EpistemicViewing — EntityOfConcern-preserving morphism"
section_id: "A.6.3:4"
section_title: "Solution — U.EpistemicViewing as EFEM profile (entityOfConcernChangeMode = preserve)"
source_path: "FPF-Spec.md"
output_path: "by_section/A.6.3/A.6.3__005_solution-u-epistemicviewing-as-efem-profile-entityofconcernchangemode-preserve.md"
commit_sha: "fe0df9dcb06cfc87c8a6cb2f7cce3ac0d3b64d5e"
heading_path:
  - "A.6.3 — U.EpistemicViewing — EntityOfConcern-preserving morphism"
  - "A.6.3:4 — Solution — U.EpistemicViewing as EFEM profile (entityOfConcernChangeMode = preserve)"
line_start: 11212
line_end: 11415
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

### A.6.3:4 - Solution — `U.EpistemicViewing` as EFEM profile (`entityOfConcernChangeMode = preserve`)

#### A.6.3:4.1 - Informal definition

> **Definition (informal).**
> `U.EpistemicViewing` is the **EntityOfConcern-preserving species** of `U.EffectFreeEpistemicMorphing`.
> A `U.EpistemicViewing v : X→Y`:
>
> * takes an input episteme `X` and produces an output episteme `Y`,
> * preserves the value filling `EntityOfConcernSlot` (`entityOfConcernRef(Y) = entityOfConcernRef(X)`),
> * may refine or re‑express `content : U.ClaimGraph`, `viewpointRef`, `representationSchemeRef`, and `referenceScheme`,
> * is **effect-free and conservative** (no new commitments about the EntityOfConcern),
> * and composes functorially with other epistemic viewings.

In C.2.1 terms `U.EpistemicViewing` behaves like a **lens/optic over the episteme slot relation**: it focuses on some SlotKinds (typically `ClaimGraphSlot`, `ViewpointSlot`, `RepresentationSchemeSlot`, `ReferenceSchemeSlot`) while preserving `EntityOfConcernSlot` (and usually `GroundingHolonSlot`).

#### A.6.3:4.2 - Signature (A.6.0 / A.6.5 alignment)

**Signature header.**
`U.EpistemicViewing` is a morphism profile under A.6.0:

```
SubjectBlock
  SubjectKind    = U.EpistemicViewing
  RangedValueKind = ⟨X:U.Episteme, Y:U.Episteme⟩      // domain/codomain episteme pair
  Quantification = SliceSet := ContextSliceSet;
                   ExtentRule := admissible view morphisms
  ResultKind     = EpMorphism                        // local typed arrow v in the Ep category
```

**Vocabulary (re‑uses A.6.2).**
* **Types.** `U.Episteme`, `SubjectRef`, `EpMorphism`, `U.EpistemicViewing`.
* **Operators.**
  * `id    : EpMorphism(X->X)`
  * `compose(g,f) : EpMorphism(X->Z)` where `f:X->Y`, `g:Y->Z`
  * `apply(v, x:U.Episteme) : U.Episteme`
  * `dom(v), cod(v) : U.Episteme`
  * `subjectRef(-) : SubjectRef`
**SlotKind-specific discipline.**
Domain and codomain epistemes are instances of some `U.Episteme` species (typically `U.EpistemeCard`, `U.EpistemeView`, or `U.EpistemePublication`) whose episteme kinds each provide SlotSpecs (A.6.5) including at least:
  * `EntityOfConcernSlot` (ValueKind `U.Entity`, RefKind `U.EntityRef`),
  * `GroundingHolonSlot?` (ValueKind `U.Holon`, RefKind `U.HolonRef`),
  * `ClaimGraphSlot` (ValueKind `U.ClaimGraph`, by‑value),
  * `ViewpointSlot?` (ValueKind `U.Viewpoint`, RefKind `U.ViewpointRef`),
  * `ReferenceSchemeSlot` (ValueKind `U.ReferenceScheme`, by‑value),
  * and, where C.2.1+ is in use, `RepresentationSchemeSlot`, `ViewSlot` and related slots.

Practical species of EpistemicViewing will very often take `X` and `Y` from the same `U.EpistemeKind`, but the pattern itself only requires that the SlotSpecs of the domain and codomain kinds be **compatible** in the sense of A.6.5, not literally identical.

**Relation to EFEM.**
* Every `U.EpistemicViewing` is an **EFEM morphism** with `entityOfConcernChangeMode = preserve` in the sense of A.6.2/C.2.1.
* It **inherits** P0–P5 from A.6.2, specialised to the case where the value filling `EntityOfConcernSlot` is unchanged.

#### A.6.3:4.3 - Invariants (EV-0...EV-6, over C.2.1 components)

All invariants below are **in addition** to A.6.2 EFEM invariants P0-P5 and SHALL be read directly against C.2.1 components and A.6.5 SlotSpecs.

**EV‑0 - Species & EntityOfConcernChangeMode.**

* Any morphism `v:X→Y` declared as `U.EpistemicViewing` **MUST**:
  * be a species of `U.EffectFreeEpistemicMorphing` (A.6.2), and
  * declare `entityOfConcernChangeMode(v) = preserve`.
* Consequently:
  * `EntityOfConcernSlot` has the **same ValueKind and RefKind** in the episteme kind of `X` and `Y` (same `EntityOfConcernClass ⊑ U.Entity`);
  * `entityOfConcernRef(Y) = entityOfConcernRef(X)` **by definition** of the species.

**EV‑1 - Typed domain/codomain & DescriptionContext behaviour.**

For any `v:X→Y` in `U.EpistemicViewing`:
1. `X` and `Y` are instances of `U.Episteme` species whose episteme kinds both realise at least the core C.2.1 slots (`EntityOfConcernSlot`, `GroundingHolonSlot?`, `ClaimGraphSlot`, `ViewpointSlot?`, `ReferenceSchemeSlot`) and obey A.6.5. Many practical species of EpistemicViewing will take `X` and `Y` from the **same** `U.EpistemeKind`, but the A.6.3 pattern only requires **SlotSpec compatibility** between domain and codomain kinds (in the sense of A.6.5), not literal kind equality.

2. In the SlotKind-specific read/write discipline:
   * `EntityOfConcernSlot` is **read‑only** (no change in `entityOfConcernRef`).
   * `GroundingHolonSlot`, if present, is:
     * either preserved exactly, or
     * changed only within an explicitly declared **grounding context** (e.g. normalising identifiers for the same plant or runtime), justified via a `Bridge` in the same ReferencePlane.
   * `ViewpointSlot`, if present, is:
     * either preserved (internal normalisation under the same viewpoint), or
     * changed only to another `U.ViewpointRef` **within a declared `U.MultiViewDescribing` family** (E.17.0), with a `CorrespondenceModel` providing witnesses.
3. For any episteme that is a `…Description`/`…Spec` (E.10.D2), `subjectRef` decodes to `DescriptionContext = ⟨EntityOfConcernRef, BoundedContextRef, ViewpointRef⟩`. EpistemicViewing MUST:
   * preserve `EntityOfConcernRef`,
   * preserve `BoundedContextRef` (unless a Bridge is explicitly cited),
   * treat `ViewpointRef` as in (2) above.

**EV‑2 - Effect‑free boundary (over EpistemeSlotRelation).**
EpistemicViewing remains **pure** in the EFEM sense:
* It may change **only C.2.1 components of the codomain episteme**:
  * `content : U.ClaimGraph` (e.g. filtering, aggregation, normalisation),
  * `viewpointRef` (under the constraints in EV‑1),
  * `representationSchemeRef` and `ReferenceScheme` (within a fixed representation family or under a declared `CorrespondenceModel`),
  * meta‑components (edition, provenance, status flags).
* It **MUST NOT**:
  * invoke `U.Mechanism` or perform `U.Work` (measure, execute, actuate),
  * create or modify a presentation carrier, publication carrier, file, database, or rendered artifact,
  * cross ReferencePlanes implicitly (plane crossings go through Bridges with CL penalties in Part F).

Any operational machinery (e.g. SAT/SMT solving, simulation, LLM tool‑use) MUST be modelled as a **separate `U.Mechanism`** that produces input epistemes or auxiliary epistemes or carriers consumed by the EpistemicViewing morphism.

**EV-3 - No new commitments about the EntityOfConcern.**

Let `X` and `Y = apply(v,X)` with:
* `content_X`, `referenceScheme_X`,
* `content_Y`, `referenceScheme_Y`,
* shared `entityOfConcernRef` and (typically) `groundingHolonRef`.

Then:
* The set of claims about `<entityOfConcernRef, groundingHolonRef>` obtained by interpreting `content_Y` through `referenceScheme_Y` **MUST NOT strictly extend** what is already entailed, in KD‑CAL/LOG‑CAL, by `content_X` interpreted through `referenceScheme_X` under the same ReferencePlane and context.
* Admissible changes:
  * re‑expression (changing representation, not truth conditions),
  * aggregation (e.g. summarising multiple claims into an explicitly derivable macro‑claim),
  * dropping some information (lossy projection), provided **no new atomic commitments** about the EntityOfConcern are introduced.
* Any deliberate strengthening of behavioural or structural commitments about the same EntityOfConcern **is not a valid EpistemicViewing**; it must be modelled either as:
  * a new or changed EntityOfConcern claim with its own Description epistemes, including Description epistemes admitted for specification use under A.7 and E.10.D2, or
  * an A.6.4 `U.EpistemicRetargeting` plus a new EntityOfConcern claim.

**EV‑4 - Functoriality & correspondence alignment.**

EpistemicViewing **inherits EFEM functoriality** and specialises it:

1. **Direct EpistemicViewing (same representation scheme).**
   Where `representationSchemeRef` and `ReferenceScheme` of `X` and `Y` are the same (up to declared normal forms), EpistemicViewing acts as a **strict functor** on ClaimGraphs:
   * `apply(id, X) = X`,
   * `apply(g ∘ f, X) = apply(g, apply(f, X))`,
   * `content` transformation corresponds to a structural ClaimGraph function.

2. **Correspondence‑based EpistemicViewing (representation changes).**
   When viewing relies on a `CorrespondenceModel` between epistemes or representation schemes:
   * the viewing morphism MUST reference that `CorrespondenceModel`,
   * compositions involving such viewings **MUST** publish witnesses (epistemes or proof epistemes or proof records) that squares commute **up to declared isomorphism** (oplax naturality is allowed, but corrections are deterministic and reproducible),
   * `entityOfConcernRef` and `groundingHolonRef` remain as in EV‑1; any transfer across contexts or planes goes via Bridges, not via hidden behaviour of the viewing.

**EV‑5 - Idempotency & determinism on fixed configuration.**

For any `v:X→Y` in `U.EpistemicViewing`, with fixed:
* `entityOfConcernRef`,
* `groundingHolonRef`,
* `viewpointRef`,
* `representationSchemeRef`,
* `referenceScheme`,
* and fixed `CorrespondenceModel` (if used),

the following MUST hold:
* **Idempotency.** `apply(v, apply(v, X))` is **isomorphic** to `apply(v, X)`:
  * same EntityOfConcern and grounding holon,
  * same viewpoint and representation scheme,
  * ClaimGraphs differ, at most, by declared structural equivalence (e.g. normal form vs source form).
* **Determinism.** For fixed input and configuration, the result is uniquely determined (modulo declared equivalence). Any source of non‑determinism (random seeds, timing, external service state) MUST either:
  * be exposed as part of `content` / `meta` of `X`, or
  * be moved into a Mechanism outside the viewing morphism.

**EV‑6 - Applicability & MultiViewDescribing alignment.**

Each species of `U.EpistemicViewing` MUST:
1. Declare an **Applicability profile** (A.6.0) specifying:
   * permitted `EntityOfConcernClass ⊑ U.Entity` (ValueKind of `EntityOfConcernSlot`),
   * permitted `groundingHolonRef` classes and ReferencePlanes,
   * admissible `viewpointRef` ranges (possibly a named `U.ViewpointBundle`),
   * admissible `representationSchemeRef` families.
1. For Description epistemes, including Description epistemes admitted for specification use in a `U.MultiViewDescribing` family (E.17.0):
   * preserve `EntityOfConcernRef` of `DescriptionContext`,
   * either preserve `ViewpointRef` or change it within the declared viewpoint bundle, with any additional constraints recorded in the family’s `CorrespondenceModel`,
   * never widen `ClaimScope` beyond what EV‑3 permits.
3. Treat **any change of EntityOfConcern** (even if “intuitively minor”, such as moving from subsystem to system) as **out of scope** for A.6.3; such moves belong to A.6.4 `U.EpistemicRetargeting`.

#### A.6.3:4.4 - Profiles: `U.DirectEpistemicViewing` and `U.CorrespondenceEpistemicViewing`

`U.EpistemicViewing` is further structured into two important species; both inherit EV‑0…EV‑6.

1. **`U.DirectEpistemicViewing` — self‑contained views.**
   * Domain and codomain epistemes share:
     * the same `representationSchemeRef` (up to declared normalisation),
     * the same `ReferenceScheme` (or a refinement which is conservative and structurally documented).
   * No external `CorrespondenceModel` is needed: the view is computed **solely from the input episteme** and, optionally, fixed configuration.
   * Typical cases:
     * internal normalisation (sorting, rewriting) of an engineering view;
     * filtering `U.ClaimGraph` to keep only safety‑relevant claims;
     * simplifying a proof‑oriented specification to a more operational form under the same semantics.

1. **`U.CorrespondenceEpistemicViewing` — views relying on correspondence models.**
   * Viewing depends on:
     * one or more subject epistemes (e.g. requirements and design),
     * an explicit `CorrespondenceModel` that relates their ClaimGraphs and representation schemes.
   * The result is an episteme (often an `U.EpistemeView`) whose `entityOfConcernRef` matches that of the primary episteme, but whose content is computed **through** the correspondence links.
   * Typical cases:
     * ISO 42010‑style correspondences between architectural descriptions;
     * cross‑model views in model‑based systems engineering (MBSE), where view content is computed from multiple model fragments;
     * traceability‑based views aggregating requirements, design elements, and tests.

In both profiles:
* `CorrespondenceModel` remains an **episteme-lane publication**, not a new kernel‑type hidden inside A.6.3.
* `U.EpistemicViewing` stays **view‑like**: it reveals what is already there under the correspondence; it does not perform Γ-style construction of new EntityOfConcern claims.

#### A.6.3:4.4.a - Common same-entity specialization notes

Two recurring EntityOfConcern-preserving families can be read as specializations governed by `A.6.3`, provided that EV‑0…EV‑6 remain explicit.

1. **`ConservativeRetextualization`.**
   Use this when the receiving item remains textual and the main change is wording, density, ordering, language, or bounded filtering of already available content. It stays in `A.6.3` only if `entityOfConcernRef` is preserved, no new claims about that entity are minted, and correspondence use does not collapse into bridge or substitution licence.

2. **`RepresentationSchemeTransition`.**
   Use this when the receiving item changes representation scheme or reasoning medium while still preserving the same EntityOfConcern. It stays in `A.6.3` only if representation-factor delta, recoverability, loss, and preserve-vs-retarget boundaries remain explicit. Purely textual rewrites belong with `ConservativeRetextualization`; any change of `EntityOfConcernRef` belongs with `A.6.4`.

These notes do not create new governing patterns. They mark recurring same-entity specialization boundaries that remain subordinate to `U.DirectEpistemicViewing` / `U.CorrespondenceEpistemicViewing` and to the general `A.6.3` invariants.

