---
chunk_kind: "child"
pattern_id: "A.6.2"
pattern_title: "U.EffectFreeEpistemicMorphing — Effect‑free morphisms of epistemes"
section_id: "A.6.2:4"
section_title: "Solution — define U.EffectFreeEpistemicMorphing once"
source_path: "FPF-Spec.md"
output_path: "by_section/A.6.2/A.6.2__005_solution-define-u-effectfreeepistemicmorphing-once.md"
commit_sha: "3d098629dc218572089f1890080c17d6f1d9a867"
heading_path:
  - "A.6.2 — U.EffectFreeEpistemicMorphing — Effect‑free morphisms of epistemes"
  - "A.6.2:4 — Solution — define U.EffectFreeEpistemicMorphing once"
line_start: 12991
line_end: 13172
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

### A.6.2:4 - Solution — define `U.EffectFreeEpistemicMorphing` once

#### A.6.2:4.1 - Informal definition

> **Definition.** A `U.EffectFreeEpistemicMorphing` (EFEM) is a class of **episteme→episteme morphisms** that:
>
> * operate **only** on exact epistemes identified under C.2.1 and state by value what happens to their claim content, EntityOfConcern, and effective ReferenceScheme; any grounding or viewpoint selected for a named describing use remains separate;
> * are **effect‑free** (no Work, no Mechanism application, no mutation of systems or carriers);
> * are **conservative** in what they claim about the EntityOfConcern: no new EntityOfConcern commitment may appear unless it is a logical consequence under the declared ReferenceScheme, correspondence, or bridge invariant;
> * are **functorial** (identities and composition behave as expected on the category of epistemes);
> * declare an explicit **EntityOfConcernChangeMode in {preserve, retarget}**, controlling how the EntityOfConcern changes, and explicitly preserve or change every material scheme, grounding, scope, or selected describing-use viewpoint rather than decoding a compound context value.

The category-theory **objects** of the EFEM universe are exact `U.Episteme` values of admitted dependent kinds; an episteme may also be the same individual as a `U.View` when E.17.0 conformance obtains. Publication form, carrier, and `EpistemePublicationRelation` occurrence remain separate from that episteme. The **arrows** are EFEM morphisms `f : X → Y` satisfying the P0-P5 laws below.

Specialisations:

* `U.EpistemicViewing` (A.6.3) — EFEM with `EntityOfConcernChangeMode = preserve`.
* `U.EpistemicRetargeting` (A.6.4) — EFEM with `EntityOfConcernChangeMode = retarget`, tied to KindBridges/ReferencePlanes.

#### A.6.2:4.2 - Direct signature components (A.6.0 alignment)

As a `U.Signature`, EFEM declares the following direct A.6.0 components, specialised to episteme-to-episteme morphisms. They are declaration content, not fields of an additional container kind.

```
SubjectKind     = U.EffectFreeEpistemicMorphing
RangedValueKind = pair of U.Episteme values <X, Y>
ResultKind      = EpMorphism
SliceSet        = ContextSliceSet
ExtentRule      = admissible EFEM morphisms in each selected slice
```

`X` and `Y` are respectively the domain and codomain epistemes. `EpMorphism` is the local mathematical-lens arrow value `f : X -> Y` in the `Ep` category. `SliceSet` and `ExtentRule` are current here because later viewing and retargeting declarations rely on the admitted morphism family varying by selected slice; they are not mandatory signature filler.

**Vocabulary (core operators & kinds)**

* **Types**
  * `U.Episteme` (as holon, including any same-individual admitted dependent episteme kind or `U.View` membership); publication is contingent participation in exact E.24.PUB relations, not an episteme species.
  * `U.EpistemeKind` (an admitted dependent kind of `U.Episteme`; it does not make the episteme a relation record or give it participant slots).
  * `SubjectRef` (legacy source wiring name only). When it occurs, recover the exact episteme and EntityOfConcern; recover the effective scheme when it changes interpretation and any selected viewpoint only for the named describing use. It does not define another EntityOfConcern family or a compound context value.
  * `EpMorphism` (local arrow value in `Ep`, defined here and interpreted through C.29 when the mathematical-lens use is current).
  * `U.EntityOfConcernChangeMode = {preserve, retarget}` (enumeration; no new durable U-kind named “EntityOfConcern”).

* **Operators (arrow algebra)**

  * `id_X : EpMorphism(X->X)` for any episteme `X`.
  * `compose(g,f) : EpMorphism(X->Z)` where `f : X->Y`, `g : Y->Z`.
  * `apply(f, x:U.Episteme) : U.Episteme`.
  * `dom(f), cod(f) : U.Episteme`.
  * `subjectRef(E) : SubjectRef` only as a legacy source projection; conformant use resolves E and its EntityOfConcern, then names any material scheme or use-level viewpoint separately.
  * `entityOfConcernChangeMode(f) : U.EntityOfConcernChangeMode`  // EFEM‑level characteristic from C.2.1.

Each operator that takes epistemes as arguments names by value the C.2.1 discriminators it reads or changes: claim content, exact EntityOfConcern, and effective ReferenceScheme. It names any empirical-grounding, representation, view-conformance, or describing-use viewpoint relation separately. When an exact reusable relation declaration is current, its A.6.5 SlotSpecs describe that relation's participant meanings; they are not fields of an episteme.

**Laws row** and **Applicability** are given by P0–P5 and the Scope clause below.

#### A.6.2:4.3 - Laws P0–P5 (normative)

All laws below are **admissibility predicates**: a morphism advertised as an instance of `U.EffectFreeEpistemicMorphing` satisfies them.

##### A.6.2:4.3.1 - P0 — Typed episteme and value-and-relation profile (C.2.1-grounded)

For any EFEM morphism `f : X→Y`:

1. **Typed epistemes.** `X` and `Y` are epistemes of declared kinds `K_X, K_Y : U.EpistemeKind`, each identified under C.2.1 by exact claim content, one EntityOfConcern, and one effective ReferenceScheme. Grounding and representation relations are added only when current; a viewpoint selected for a named describing use remains outside episteme identity.

2. **Value and use projection.** For each episteme `E`—and separately for a named describing use when one is current—EFEM laws may refer to:
   * `content(E) : U.ClaimGraph` — E's exact identity-bearing claim content;
   * `entityOfConcernRef(E) : U.EntityRef` — designates E's exact EntityOfConcern;
   * `selectedViewpointRef?(use) : U.ViewpointRef` — only when the named describing use selects one exact viewpoint; this is not a component of E's identity;
   * `referenceScheme?(E) : U.ReferenceScheme` — E's effective designation and interpretation scheme;
   * `representationSchemeRef?(E) : U.RepresentationSchemeRef` — only when an exact C.29 representation scheme and correspondence relation are current for E; this is not a C.2.1 identity component;
   * `meta(E)` — any separately current C.2.1 edition relation, A.10 provenance or evidence relation, or named status value, each with its exact predicate and participants. An EFEM species may use those values, but none becomes an episteme-identity component by appearing here.

   When grounding matters, name the exact grounding relation, its grounding holon, and the claims it covers; grounding is not another component of episteme identity.

3. **Declared `EntityOfConcernChangeMode`.**
   Each EFEM species **declares** a fixed `EntityOfConcernChangeMode ∈ {preserve, retarget}`. At the level of individual morphisms:

   * if `entityOfConcernChangeMode(f) = preserve`, then `entityOfConcernRef(Y) = entityOfConcernRef(X)`; any current grounding relation is preserved or changed separately;
   * if `entityOfConcernChangeMode(f) = retarget`, then `entityOfConcernRef(Y) ≠ entityOfConcernRef(X)` in general and the record names a **KindBridge** between the two EntityOfConcern values (A.6.4 / F.9).

4. **Legacy SubjectRef and describing-use discipline.**
   For Description epistemes, including those admitted for specification use, resolve legacy `subjectRef(E)` to exact E and its EntityOfConcern. State separately whether the morphism preserves or changes claim content, EntityOfConcern, grounding, effective scheme when material, and any viewpoint selected for a named describing use. Viewpoint selection is neither identity nor conformance.

##### A.6.2:4.4.2 - P1 — Purity (no external effects)

EFEM morphisms are **pure functions on epistemes**:
* Applying `f : X→Y` **does not**:
  * change any `U.System` or `U.Holon` state;
  * perform `U.Work` or run a `U.Mechanism` (A.6.1) with operational guards;
  * create, update, or mutate a presentation carrier, publication carrier, file, database, message bus, or IDE artifact.
* The **only** state change introduced by EFEM is the replacement of input epistemes by output epistemes according to `apply(f, X) = Y`; P2-P5 constrain every change to an identity value or neighboring relation.

Any operation that requires **measurements, simulations, solver calls, or tool use with external side-effects** is modelled as a `U.Mechanism`/`U.Work` that **produces new epistemes**, which may then be related by EFEM morphisms.

##### A.6.2:4.3.3 - P2 — Conservativity (no new EntityOfConcern commitments)

Let `content_X = content(X)`, `content_Y = content(Y)`, with associated `referenceScheme_X`, `referenceScheme_Y`, `entityOfConcernRef_X`, and `entityOfConcernRef_Y`. Interpret each `content` via its `ReferenceScheme`. When the claim depends on grounding, identify the source and receiving grounding relations and holons separately. Then:

> The set of **claims about the EntityOfConcern values** that can be interpreted from `Y` **introduces no new atomic commitments** beyond those that are logical consequences of the claims interpreted from `X`, possibly after applying a declared correspondence between representation/reference schemes.

Intuitively:

* EFEM may:
  * delete information (projection/abstraction);
  * normalise or re‑express information (e.g., reordering ClaimGraph, changing notation via a ReferenceScheme/RepresentationScheme correspondence);
  * add **meta‑claims about the episteme** itself (edition, source, status, witness entries).

* EFEM may **not**:
  * assert new atomic facts about the EntityOfConcern values or grounding holons beyond what is derivable from input ClaimGraphs under the declared ReferenceSchemes and any named grounding relations;
  * silently widen the scope of claims or cross a ReferencePlane without the exact scope or plane relation required for that move.

Where `entityOfConcernChangeMode(f) = retarget`, conservativity is understood **relative to a declared invariant** of the KindBridge (A.6.4): e.g., conservation of energy for a Fourier transform, or preservation of functional behaviour for a structural reinterpretation.

##### A.6.2:4.3.4 - P3 — Functoriality (identity, composition, correspondence)

We work in the category **Ep** whose objects are epistemes (species of `U.Episteme`) and whose arrows are EFEM morphisms satisfying P0–P2, together with the functor

```
α : Ep → Ref
```

that maps each episteme to the reference designating its exact EntityOfConcern, `entityOfConcernRef(E)`, in the selected mathematical description. EFEM instances with `entityOfConcernChangeMode(f) = preserve` are vertical morphisms for α (`α(f) = id`), while those with `entityOfConcernChangeMode(f) = retarget` reindex along a declared `KindBridge` in **Ref**.

1. **Identities.** For each episteme `X`, there exists `id_X : X→X` such that:

   ```text
   apply(id_X, X) = X
   compose(id_Y, f) = f = compose(f, id_X)
   ```

   `id_X` preserves the episteme's claim content, EntityOfConcern, effective ReferenceScheme, and every other declared episteme value. If the same named describing use is carried through the identity morphism, its selected viewpoint also remains unchanged as a separate use qualification.

2. **Composition.** For `f : X→Y`, `g : Y→Z`, the composite `h = compose(g,f)` is an EFEM morphism `X→Z` with:

   ```
   apply(h, X) = apply(g, apply(f, X))
   entityOfConcernChangeMode(h) = combine(entityOfConcernChangeMode(f), entityOfConcernChangeMode(g))   // as per species-specific rules
   ```

and P0–P2 hold for `h`. For example, two `preserve` morphisms compose to `preserve`; `preserve` after `retarget` is `retarget` if the KindBridge composition exists.

3. **Correspondence-aware composition.** When EFEM changes a representation scheme or effective ReferenceScheme, name the exact C.29 or A.6.3.RT correspondence or transition relation that must commute. Composition respects that relation up to the declared isomorphism or oplax-naturality rule; any witness episteme remains a separately identified value.

##### A.6.2:4.3.5 - P4 — Idempotence & determinism (on fixed configuration)

For any EFEM morphism `f : X→Y` with fixed configuration (episteme kinds, `EntityOfConcernChangeMode` characteristic, KindBridge/CorrespondenceModel where needed):

1. **Determinism.**
   For the same input episteme `X`, the same separately declared inputs, and the same fixed configuration, `apply(f, X)` yields the same output episteme `Y` up to declared structural equivalence such as normal form or alpha-renaming. There is no dependence on ambient time, randomness, network state, or solver heuristics unless these are encoded as explicit inputs.

2. **Idempotence (up to declared equivalence).**
   Re‑applying the same EFEM to its own output yields no further essential change:

   ```text
   apply(f, apply(f, X)) ≅ apply(f, X)
   ```

   where `≅` denotes the structural equivalence declared for the episteme kinds in question (e.g., ClaimGraph normalisation).

Species MAY weaken idempotence to “idempotent after normalisation”; if so, the normalisation step is itself specified as an EFEM morphism and the composite be idempotent.

##### A.6.2:4.3.6 - P5 — Applicability, scope & compatibility

Each EFEM species **publishes** an Applicability clause:

* **EntityOfConcernClass / EntityOfConcern class.**
  A constraint on the admitted kinds of the exact EntityOfConcern, expressed for example as `EntityOfConcernClass ⊑ U.Entity`: “epistemes whose claims concern a `U.Holon` that is a system of type X”.

* **Grounding holon and operating conditions.**
  Name the exact grounding holon and the lab, runtime, organizational, scope, or other operating conditions that bound applicability when they matter. These conditions do not form a universal context object.

* **Representation/ReferenceSchemes.**
  Enumerates admissible `RepresentationScheme`/`ReferenceScheme` pairs and any required CorrespondenceModels.

* **Viewpoint discipline.**
  For Description epistemes, including Description epistemes admitted for specification use, EFEM specifies which `U.Viewpoint`s (E.17.0) are admissible and how it interacts with `U.MultiViewDescribing` families (e.g., “works only on engineering viewpoints from TEVB” or “viewpoint‑agnostic normalisation”).

Applying EFEM **outside** its Applicability (e.g., wrong EntityOfConcernClass, missing grounding holon, incompatible Viewpoint) is **non‑conformant**: a conformant implementation rejects such attempts or models them as different mechanisms/works, not as EFEM.

Use that actually relates distinct F.17 local senses or crosses a ReferencePlane is **not part of EFEM**. Apply the exact F.9 Bridge or plane relation and A.6.1 transport when those relations are current, then feed the resulting epistemes into EFEM. Different source labels or operating conditions alone create no Bridge.

