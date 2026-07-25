---
chunk_kind: "child"
pattern_id: "A.6.4"
pattern_title: "U.EpistemicRetargeting — EntityOfConcern retargeting morphism"
section_id: "A.6.4:4"
section_title: "Solution — U.EpistemicRetargeting as EFEM profile (entityOfConcernChangeMode = retarget)"
source_path: "FPF-Spec.md"
output_path: "by_section/A.6.4/A.6.4__005_solution-u-epistemicretargeting-as-efem-profile-entityofconcernchangemode-retarget.md"
commit_sha: "504747d26299e3963dc0457bf48d4e2a791d926a"
heading_path:
  - "A.6.4 — U.EpistemicRetargeting — EntityOfConcern retargeting morphism"
  - "A.6.4:4 — Solution — U.EpistemicRetargeting as EFEM profile (entityOfConcernChangeMode = retarget)"
line_start: 14552
line_end: 14809
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

### A.6.4:4 - Solution — `U.EpistemicRetargeting` as EFEM profile (`entityOfConcernChangeMode = retarget`)

#### A.6.4:4.1 - Informal definition

> **Definition (informal).**
> `U.EpistemicRetargeting` is the **EntityOfConcern retargeting species** of `U.EffectFreeEpistemicMorphing`.
> A `U.EpistemicRetargeting r : X->Y`:
>
> * takes an input episteme `X` and produces an output episteme `Y`,
> * **changes** the value filling `EntityOfConcernSlot` (`entityOfConcernRef(Y) != entityOfConcernRef(X)`),
> * relates the kinds of the source and receiving EntityOfConcern values via an explicit `KindBridge` in the appropriate ReferencePlane,
> * preserves a declared **invariant** across the pair of entities (e.g. energy, behaviour, sufficient statistics),
> * is **effect-free** at the level of Work/Mechanism (EFEM discipline),
> * and composes functorially with other retargetings and viewings.

In C.2.1 terms, `U.EpistemicRetargeting` **re-indexes** an episteme along a base-level bridge: it moves the `EntityOfConcernSlot` (and often the `<EntityOfConcernSlot, GroundingHolonSlot>` bundle) along a `KindBridge`, while re-expressing `content : U.ClaimGraph` and `referenceScheme` so that the declared invariant continues to hold at the receiving EntityOfConcern.

#### A.6.4:4.1.a - Retargeting witness decision block

When a retargeting claim has FPF-governed use, the receiving text makes these decision-block fields recoverable:

| Field | Required interpretation |
| --- | --- |
| `sourceEpistemeOrPublication` | The source `U.Episteme`, `U.EpistemePublication`, episteme-lane `U.View`, or specific source publication being retargeted or cited. |
| `receivingEpistemeOrPublication` | The receiving episteme, publication, view, diagram, table, functional description, explanation, `StructuralReinterpretation`, or `E.18`-facing publication item. |
| `sourceEntityOfConcern` | The EntityOfConcern before retargeting. |
| `receivingEntityOfConcern` | The EntityOfConcern after retargeting. |
| `kindBridgeAndInvariant` | The `KindBridge`, reference-plane relation, and invariant that make the retargeting admissible. |
| `groundingAndContext` | Grounding holon, bounded context, reference plane, reference scheme, viewpoint, and view as far as the intended use needs. |
| `claimOrCommitmentUnderTest` | The claim, invariant, commitment, relation, or project-side use whose retargeted admissibility is being judged. |
| `preservedCommitments` | What the receiving item still carries from the source under the declared invariant. |
| `withdrawnOrNewCommitments` | What the receiving item drops, narrows, adds, widens, or changes. |
| `admissiblePredicateChanges` | Which predicates or claim forms become admissible or inadmissible after `entityOfConcernRef` changes. |
| `admissibilityValue` | The source-claim, bridge, or invariant witness value for the intended use named by value. |
| `retargetingWitness` | The reason the changed EntityOfConcern interpretation is admissible now. |
| `counterWitness` | Any fact that weakens retargeting admissibility, such as missing bridge, invariant failure, unwitnessed predicate transfer, source contradiction, or hidden work/evidence/gate reliance. |
| `lossAndRecoverability` | Preserved distinctions, lost distinctions, recoverability goal, recoverability evidence, and source-bearing reopen condition. |
| `admissibleUse` | The admissible use named by value now. |
| `nonAdmissibleUse` | The downstream work, evidence, gate, assurance, bridge, decision, abductive, transformation-flow path, temporal, or dynamics use that is not carried by the current item. |
| `neighboringGoverningPatternRef` | The FPF pattern that governs the neighboring claim being made, when one is present. |
| `remainingAdmissibleReaderAction` | One short plain line saying what the reader may now do or which neighboring pattern now carries the claim being made. |

The decision block is not a new FPF kind, record, profile, publication form, or hidden evidence or justification object. It is a recoverable field set for retargeting cases. Ordinary local retargeting can stay compact when the source EntityOfConcern, receiving EntityOfConcern, bridge, invariant, and remaining reader action are already explicit.

If the bridge or invariant is insufficient for the intended use, the receiving item can still be useful, but the current disposition is source-bearing reopen, bridge-only comparison, controlled coarsening, report-only use, exploratory use, or named neighboring-pattern handoff. Do not keep an unnamed middle state where the retargeted item remains rhetorically useful but no FPF disposition is stated.

#### A.6.4:4.2 - Signature (A.6.0 / A.6.5 alignment)

**Signature header.**
`U.EpistemicRetargeting` is a morphism profile under A.6.0, specialised from EFEM:

```
SubjectBlock
  SubjectKind    = U.EpistemicRetargeting
  RangedValueKind = ⟨X:U.Episteme, Y:U.Episteme⟩      // episteme pair
  Quantification = SliceSet := ContextSliceSet;
                   ExtentRule := admissible retargeting morphisms
  ResultKind     = EpMorphism                        // local typed arrow r in the Ep category
```

**Vocabulary (re‑uses A.6.2).**

* **Types.** `U.Episteme`, `SubjectRef`, `EpMorphism`, `U.EpistemicRetargeting`.
* **Operators.**

  * `id    : EpMorphism(X->X)`
  * `compose(g,f) : EpMorphism(X->Z)` where `f:X->Y`, `g:Y->Z`
  * `apply(r, x:U.Episteme) : U.Episteme`
  * `dom(r), cod(r) : U.Episteme`
  * `subjectRef(-) : SubjectRef`
* **Slot‑level discipline.**
  Domain and codomain epistemes are instances of some `U.Episteme` species (typically `U.EpistemeCard`, `U.EpistemeView`, or `U.EpistemePublication`) whose episteme kinds each provide SlotSpecs (A.6.5) including at least:

  * `EntityOfConcernSlot` (ValueKind `U.Entity`, RefKind `U.EntityRef`, usually restricted to an `EntityOfConcernClass ⊑ U.Entity`),
  * `GroundingHolonSlot?` (ValueKind `U.Holon`, RefKind `U.HolonRef`),
  * `ClaimGraphSlot` (ValueKind `U.ClaimGraph`, by‑value),
  * `ViewpointSlot?` (ValueKind `U.Viewpoint`, RefKind `U.ViewpointRef`),
  * `ReferenceSchemeSlot` (ValueKind `U.ReferenceScheme`, by‑value),
  * and, where C.2.1+ is in use, `RepresentationSchemeSlot`, `ViewSlot` and related slots.

The pattern only requires **SlotSpec compatibility** between domain and codomain kinds (in the sense of A.6.5); they need not be literally the same kind.

**Relation to EFEM and Viewing.**

* Every `U.EpistemicRetargeting` is an **EFEM morphism** with `entityOfConcernChangeMode = retarget` in the sense of A.6.2/C.2.1.
* It **inherits** EFEM laws P0–P5 and adds retargeting‑specific obligations ER‑0…ER‑6 below.
* `U.EpistemicViewing` (A.6.3) covers the complementary case `entityOfConcernChangeMode = preserve`, where the EntityOfConcern does not change.

#### A.6.4:4.3 - Laws (ER‑0…ER‑6, over C.2.1 components)

All laws below are **in addition** to A.6.2’s EFEM laws P0–P5 and SHALL be read directly against C.2.1 components and A.6.5 SlotSpecs.

**ER‑0 - Species & EntityOfConcernChangeMode.**

* Any morphism `r:X→Y` declared as `U.EpistemicRetargeting` **MUST**:
  * be a species of `U.EffectFreeEpistemicMorphing` (A.6.2), and
  * declare `entityOfConcernChangeMode(r) = retarget`.
* Consequently:
 * the pair `<EntityOfConcernSlot, GroundingHolonSlot>` is the **retargeted EoC/grounding bundle** for the change (as in C.2.1 §7.3: EntityOfConcern‑bundle retargeting),
 * `EntityOfConcernSlot` is **write‑enabled** (unlike Viewing) but only under the constraints below,
  * there exist entities `T₁, T₂ : U.Entity` such that:
    * `entityOfConcernRef(X) = T₁`,
    * `entityOfConcernRef(Y) = T₂`,
    * `T₁ ≠ T₂` (as Ref/identity), and
    * `Kind(T₁)` and `Kind(T₂)` are related by a `KindBridge` in Part F’s sense (with declared CL^k).

**ER‑1 - Typed domain/codomain & EntityOfConcern‑bundle behaviour.**

For any `r:X→Y` in `U.EpistemicRetargeting`:

1. `X` and `Y` are instances of `U.Episteme` species whose episteme kinds both realise at least the core C.2.1 slots (`EntityOfConcernSlot`, `GroundingHolonSlot?`, `ClaimGraphSlot`, `ViewpointSlot?`, `ReferenceSchemeSlot`) and obey A.6.5.

2. At the SlotKind level:

   * `EntityOfConcernSlot`:
     * **MUST change** (`entityOfConcernRef(Y) ≠ entityOfConcernRef(X)`),
     * the ValueKinds for the slot in the domain and codomain kinds **MUST** be related via an `EntityOfConcernClass` pair that the `KindBridge` covers (e.g. `PhysicalModule` ↔ `FunctionHolon`, `Signal` ↔ `Spectrum`, `Dataset` ↔ `StatisticalModel`).

   * `GroundingHolonSlot`, if present:
     * is either preserved by reference equality (`groundingHolonRef(Y) = groundingHolonRef(X)`), or
     * changed only along a declared holon‑Bridge in the same ReferencePlane (for example, moving from one runtime to another under a deployment bridge) with CL^plane penalties recorded in Part F.

   * `ViewpointSlot`, if present:
     * is either preserved, or
     * changed only within a declared `U.ViewpointBundle` (E.17.1/E.17.2), with the corresponding `CorrespondenceModel` explaining how the invariant is maintained under the new viewpoint.

1. For any episteme that is a `…Description`/`…Spec` (E.10.D2), `subjectRef` decodes to `DescriptionContext = ⟨EntityOfConcernRef, BoundedContextRef, ViewpointRef⟩`. Under EpistemicRetargeting:
   * `EntityOfConcernRef` **MUST** change from `T₁` to `T₂` as in ER‑0,
   * `BoundedContextRef` is:
     * either preserved, or
     * changed along an explicit Context‑Bridge (E.10.D1, Part F),
   * `ViewpointRef` is treated as in (2) above (preserved or mapped within a bundle), and any resulting change in admissible claims is governed by ER‑2.

The pair `<EntityOfConcernSlot, GroundingHolonSlot>` is treated as a **retargeted EoC/grounding bundle**: many practical retargetings work at the level of this bundle rather than EntityOfConcern alone, especially where `E.18` `StructuralReinterpretation` is used.

**ER‑2 - Invariant-based conservativity (lossy but admissible).**

Let `X` and `Y = apply(r,X)` with:
* `entityOfConcernRef(X) = T₁`, `entityOfConcernRef(Y) = T₂`,
* `KindBridge(T₁,T₂)` and associated invariant `Inv` declared for this species (e.g. energy, behavioural relation, likelihood),
* `content_X`, `referenceScheme_X`,
* `content_Y`, `referenceScheme_Y`,
* `groundingHolonRef_X`, `groundingHolonRef_Y`.

Then:
1. There MUST exist a KD‑CAL/LOG‑CAL expression of `Inv` such that:
   * all claims about `Inv` that can be derived by interpreting `content_Y` through `referenceScheme_Y` relative to `<T₂, groundingHolonRef_Y>`
     **are entailed by**
     claims about `Inv` derivable from `content_X` through `referenceScheme_X` relative to `<T₁, groundingHolonRef_X>`.

2. Retargeting, as an EFEM instance, **may**:
   * discard information not needed to maintain `Inv` (lossy summarisation),
   * change representation schemes (e.g. time vs frequency domain),
   * move to different abstraction planes or ReferencePlanes (with Bridges and CL penalties declared),
   but **MUST NOT** violate the declared invariant.

3. Any intended change that adds commitments about `Inv` beyond what is derivable from `X` **is not a valid EpistemicRetargeting**. It must be modelled as:
   * a change of EntityOfConcern claim (new Description episteme or Description episteme admitted for specification use under A.7 and E.10.D2), or
   * a chain of retargetings and EntityOfConcern claim updates explicitly recorded in KD‑CAL/LOG‑CAL.

**ER‑3 - Functoriality, α‑reindexing & SquareLaw witnesses.**

EpistemicRetargeting **inherits EFEM functoriality** and specialises it to the retargeting case:

1. At the `Ep` level:
   * `apply(id, X) = X` (no retargeting),
   * `apply(r₂ ∘ r₁, X) = apply(r₂, apply(r₁, X))` whenever domains/codomains match,
   * the composite `r₂∘r₁` has `entityOfConcernRef(X) = T₁` and `entityOfConcernRef(cod(r₂∘r₁)) = T₃`, with a composed `KindBridge(T₁,T₃)` whenever the Bridges of `r₁` and `r₂` compose.

2. At the `Ref` level, under `α : Ep → Ref`:
   * each retargeting `r` induces a base arrow `α(r) : R₁→R₂` in `Ref`, compatible with the `KindBridge` used in ER‑0,
   * the square formed by:
     * `X→Y` in `Ep` (retargeting),
     * `α(X)→α(Y)` in `Ref` (base retargeting),
     * any measurement or evaluation morphisms on either side,
       **MUST** commute **up to a declared SquareLaw‑retargeting witness** (Part F / `E.18`), documenting that evaluating then retargeting vs retargeting then evaluating yields equivalent results (modulo CL‑penalties).

2. When retargetings use CorrespondenceModels between epistemes (e.g. aligning detailed hardware layouts with function networks), they MUST:
   * reference the CorrespondenceModel explicitly,
   * publish witness epistemes that certify commutativity of key squares, analogous to EV‑4 but now across **different EntityOfConcern values.**

**ER‑4 - Idempotency & determinism on fixed Bridge/invariant.**

For any `r:X→Y` in `U.EpistemicRetargeting`, with fixed:
* `KindBridge(T₁,T₂)` and ReferencePlane policies,
* invariant `Inv`,
* configuration (ContextSlice, representation families, CorrespondenceModels),

the following MUST hold:

* **Idempotency.**
  Applying `r` twice does not further change the EntityOfConcern or invariant‑relevant content:
  * `apply(r, apply(r, X))` is **isomorphic** (in the EFEM sense) to `apply(r, X)`,
  * `entityOfConcernRef` is already `T₂` after the first application,
  * `content` and `referenceScheme` differ at most by declared structural equivalence (e.g. normal forms at the receiving EntityOfConcern).

* **Determinism.**
  For fixed input `X` and fixed Bridge/invariant configuration, the result is uniquely determined modulo declared equivalence. Any source of non‑determinism (randomness, time, external service state) MUST either:
  * be made explicit as part of `content`/`meta` of `X`, or
  * be moved to a `U.Mechanism` outside the retargeting morphism.

**ER‑5 - Applicability, EntityOfConcernClass pairs & CL‑discipline.**

Each species of `U.EpistemicRetargeting` MUST declare an **Applicability profile** (A.6.0) that includes:

1. **EntityOfConcernClass pairs.**
   Admissible pairs of `EntityOfConcernClass`es (ValueKinds of `EntityOfConcernSlot` for domain and codomain), for example:
   * `(PhysicalModule, FunctionHolon)`,
   * `(Signal, Spectrum)`,
   * `(Dataset, StatisticalModel)`.

   For each such pair, the pattern MUST reference the appropriate `KindBridge` species in Part F.

2. **Grounding constraints.**
   Permitted classes of `groundingHolonRef` and ReferencePlanes, including whether:
   * grounding must stay within the same holon,
   * or may move along specific holon Bridges with CL^plane penalties.

3. **Viewpoint/context constraints.**
   Whether retargeting is allowed for all viewpoints or only for specific `U.ViewpointBundle`s (TEVB etc.), and any requirements on `BoundedContextRef`.

4. **CL‑discipline.**
   Minimum CL^k and CL^plane required for the Bridges used, aligning with F.9 and the `E.18` `StructuralReinterpretation` rules.

Any attempt to apply a retargeting outside this Applicability profile is **ill‑typed**.

**ER‑6 - Compatibility with Viewing and Mechanisms.**

1. **Separation from Viewing.**

   * Any morphism that **does not change** `entityOfConcernRef` (and keeps `EntityOfConcernChangeMode = preserve`) belongs to A.6.3 `U.EpistemicViewing`, not to `U.EpistemicRetargeting`.
   * Any morphism that **does** change `entityOfConcernRef` **MUST NOT** be declared as `U.EpistemicViewing`; it is either:
     * a `U.EpistemicRetargeting`, or
     * a more general pattern that composes several retargetings and EntityOfConcern claim changes.

   In any composite `V∘r` or `r∘V`, entityOfConcern changes are localised to retargeting steps; Viewing steps are always `entityOfConcernChangeMode = preserve`.

2. **Separation from Mechanisms.**

   * Retargeting MAY depend on outputs produced by `U.Mechanism` (e.g., computing a Fourier transform, fitting a model), but those are separate Work/Mechanism steps.
   * `U.EpistemicRetargeting` itself remains **effect‑free**: it rearranges epistemes, slots and ClaimGraphs, but does not perform measurements or actuation.

#### A.6.4:4.4 - Boundary with representation, explanation, transformation-flow structure, and neighboring claims

`U.EpistemicRetargeting` is triggered by changed EntityOfConcern, EntityOfConcern kind, ontology frame, admissible predicate set, or invariant-bearing receiving EntityOfConcern. It is not triggered by changed wording, changed representation scheme, changed explanation mode, or publication formatting alone.

Boundary rules:
- if the EntityOfConcern is preserved and the main change is representation scheme or reasoning medium, use `A.6.3.RT`;
- if the EntityOfConcern is preserved and the main change is explanation mode, explanatory stance, or explanation-facing publication, use `E.17.EFP`;
- if the source and receiving items are only bridge-only comparison, analogy, equivalence, or substitution relation, use `F.9` or `F.9.1` instead of interpreting the bridge as identity;
- if the receiving item is useful only under narrower declared use with visible loss and source-bearing reopen, use `A.6.3.CSC`;
- if decoded or latent output is interpretable but not tied to source claim, access relation, recoverability evidence, admissible-use value, and remaining reader action, keep it report-only, exploratory, source-bearing reopen, or in the named neighboring pattern;
- if a `StructuralReinterpretation`, `PathSliceId`, `CrossingRef`, or `DecisionLogRef` is present, use `E.18`, `A.20`, or `A.21` for graph, path, constraint, and gate relations. Those references do not prove semantic continuity or retargeting admissibility by themselves;
- if changed problem formulation changes abductive prompt, candidate generation, rival-set formation, selected prime hypothesis, plausibility filtering, or abductive reopen, use `B.5.2`;
- if the receiving item is used as work, evidence, assurance, gate passage, temporal claim, dynamics law, or control relation, use `A.15`, `A.10`, `B.3`, `A.21`, `C.27`, `A.3.3`, or the neighboring governing pattern.

`StructuralReinterpretation` in `E.18` receives retargeting semantics from this pattern. It is not an `E.18`-local retargeting kind and not proof that the source and receiving items preserve the same `entityOfConcernRef`.

