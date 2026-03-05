1. **`U.EpistemeCard`.**
   A species of `U.Episteme` whose components correspond one‑to‑one to slots of some `U.EpistemeKind`:
   * `content : U.ClaimGraph` (for `ClaimGraphSlot`),
   * `describedEntityRef : U.EntityRef` (for `DescribedEntitySlot`),
   * `groundingHolonRef? : U.HolonRef` (for `GroundingHolonSlot`),
   * `viewpointRef? : U.ViewpointRef` (for `ViewpointSlot`),
   * `referenceScheme? : U.ReferenceScheme` (for `ReferenceSchemeSlot`),
   * optionally `representationSchemeRef? : U.RepresentationSchemeRef` (C.2.1+),
   * `meta : Edition/Provenance/Status…`.
     Minimal episteme identity is the pair `⟨content, describedEntityRef⟩` within a `U.BoundedContext`; all other fields are optional at the genus level but may be mandatory in species. Changes that alter `content` or the effective `referenceScheme` (or that intentionally re‑identify `describedEntityRef`) **SHALL** be realised as new phases in an `U.EditionSeries` (PhaseOf chain) under A.14/A.7. Changes confined to `U.PresentationCarrier` / surfaces or other publication artefacts **do not** create a new episteme; they are captured as `U.Work` / publication events over the same `U.Episteme`.
2. **`U.EpistemePublication`.**
   A species representing **epistemes that have been published** onto surfaces (MVPK). It:
   * has at least the components of `U.EpistemeCard`,
   * plus references to `U.Surface` / `U.Face` artefacts (E.17, L‑SURF),
   * but **does not** re‑interpret these surfaces as parts of the episteme; carriers remain external.
3. **`U.EpistemeView`.**
   As defined in §4.1.5, a species of `U.Episteme` representing a **view** under a specific `U.Viewpoint`.
   Its components are a specialisation of `U.EpistemeCard`:
   * ClaimGraph often restricted/projection of a base description/specification,
   * Viewpoint fixed,
   * ReferenceScheme tailored to that viewpoint.

**Alignment requirement.**
For any of these species, the pattern **MUST** state explicitly:
* which `U.EpistemeKind` it realises, and
* how each component maps to a SlotKind/RefKind under `U.RelationSlotDiscipline`.

This ensures that A.6.2–A.6.4 can treat any `U.Episteme*` uniformly as both:
* an object in the category **Ep**, and
* a structured holon with components.

##### C.2.1:4.2.4 - SlotKind / ValueKind / RefKind discipline for DescribedEntity & GroundingHolon

C.2.1 adopts **A.6.5 `U.RelationSlotDiscipline`** wholesale. For the two key positions:
1. **DescribedEntitySlot.**
   * `SlotKind = DescribedEntitySlot`;
   * `ValueKind = U.Entity` (species may constrain to `EoIClass ⊑ U.Entity`);
   * `RefKind = U.EntityRef` (or a species thereof);
   * normative field name in episteme cards: `describedEntityRef : U.EntityRef`.
     No kernel type named `U.DescribedEntity` is introduced; the phrase “described entity” always means “an instance of `U.Entity` in the role filling `DescribedEntitySlot`”.
1. **GroundingHolonSlot.**
   * `SlotKind = GroundingHolonSlot`;
   * `ValueKind = U.Holon`;
   * `RefKind = U.HolonRef`;
   * normative field name: `groundingHolonRef? : U.HolonRef`.
     There is no kernel type `U.GroundingHolon`; “grounding holon” is a **slot occupant name**.
Any episteme that previously mixed slot/value/ref concepts (e.g., using `DescribedEntityRef` as if it were a type) **MUST** be migrated to this discipline over time; C.2.1 provides the normative anchor, and F.18 / discipline packs provide the migration guide.

#### C.2.1:4.3 - Minimal epistemic morphisms (informal schema)

> **Note.** The full mathematical treatment (categories Ep and Ref, describedEntity functor `α : Ep → Ref`, and effect‑free morphisms) lives in A.6.2–A.6.4. Here we fix only the **object‑level relations** that C.2.1 expects to exist between its positions.

At the level of `U.EpistemeCard` components and SlotKinds, we assume the following **primitive relations** (not all are functions):

1. **`describedEntitySet : U.Episteme → P(U.Entity)`**
   *derivable from `DescribedEntitySlot` and `ReferenceScheme`*
   * For an episteme `E`, `describedEntitySet(E)` is (at least) the singleton containing the entity referenced by `describedEntityRef(E)`; in more complex cases, it may be a finite set or bundle of entities, determined by `ReferenceScheme`.
   * The **functorial DescribedEntity mapping** `δ_E : Ep → Ref` used in A.6.2–A.6.4 is the categorical lift of this relation: it forgets episteme internals and keeps only the object in the ReferencePlane determined by the pair `<DescribedEntitySlot, GroundingHolonSlot>`.

2. **`grounds : (U.Entity, U.Holon) ⇝ GroundingRelation`**
   *relates described entities to grounding holons*
   * Captures how values of `DescribedEntitySlot` are **situated** in holons that make evaluation possible (labs, infrastructures, organisations).
   * Need not be total or functional; an entity may admit multiple grounding holons, or none.

3. **`designates : (U.ReferenceScheme, U.ClaimGraph, U.Entity, U.Holon) ⇝ DesignationProfile`**
   *how claims are read as statements about entities in contexts*
   * Specifies, for each claim in `content` and each `<describedEntityRef, groundingHolonRef>`, what property/relation it purports to state, and under what conditions.

4. **`satisfies / evaluatesTo : (U.ClaimGraph, U.ReferenceScheme, U.Holon) → TruthProfile/SuccessProfile`**
   *evaluation of claims under a reference scheme and grounding*
   * Forms the bridge to KD‑CAL’s `F, G, R` evaluation; details are given in C.2 and B.3.

5. **View-related morphisms** (to be connected with A.6.3):
   * `viewProject : (U.Episteme, U.Viewpoint) → U.View`
     — effect-free, **DescribedEntity-preserving** projection that slices `ClaimGraph` and specialises `ReferenceScheme` under a given viewpoint.
   * `viewEmbed : U.View → U.Episteme`
     — embedding of a view back into the wider episteme, typically as a reference with correspondence proofs.

5. **Reflexive describedEntity guard.**
   When `DescribedEntitySlot` or `ReferenceScheme` picks out an episteme or claim that includes the referring claim itself (**ReferencePlane = episteme**), publishers **SHALL** ensure that the induced justification/evaluation structure is **acyclic per evaluation chain**: reflexive describedEntities may exist as literature handles, but they MUST NOT form a minimal support cycle for acceptance or KD‑CAL assurance. Self‑reference is allowed as a citation pattern, not as a way to close justification loops.

These are **not yet laws**; they are the **hooks** that A.6.2–A.6.4 will formalise into:
* `U.EffectFreeEpistemicMorphing` (Ep→Ep morphisms over this structure),
* `U.EpistemicViewing` (describedEntity‑preserving Ep→Ep),
* `U.EpistemicRetargeting` (describedEntity‑retargeting Ep→Ep).

### C.2.1:5 - Legacy semantic triangle as didactic view  *(informative)*

**Position.** The classical semiotic or semantic triangle (“Symbol–Concept–Object”, Ogden–Richards/Frege–Carnap style) is **not** the normative ontology for epistemes in FPF. For `U.Episteme`, it is treated as a **didactic projection** of the richer hypergraph `U.EpistemeSlotGraph`:
* **“Symbol” corner** ≈ {`U.RepresentationToken`, `U.RepresentationScheme`, `U.PresentationCarrier`} when C.2.1+ is in use; in the minimal core this is collapsed into whichever external artefact happens to carry `U.ClaimGraph`.
* **“Concept” corner** ≈ `U.ClaimGraph` + `U.ReferenceScheme` under a chosen `U.Viewpoint`. This is the intensional content plus its interpretation recipe.
* **“Object” corner** ≈ the occupant of `DescribedEntitySlot` (ValueKind `U.Entity`) plus the occupant of `GroundingHolonSlot` (ValueKind `U.Holon`) and the grounding relation between them.

Under this reading the triangle is a **three‑node quotient** of the `U.EpistemeSlotGraph`:
```
(Symbol)      = RepresentationToken + Scheme + Carrier
(Concept)     = ClaimGraph + ReferenceScheme (+ Viewpoint)
(Object)      = DescribedEntity + GroundingHolon
```

All **viewpoints, operations, carriers and reference planes** are suppressed in the classical diagram. The cost of this suppression is precisely the confusion that motivates C.2.1:
* describing becomes an single unlabeled arrow,
* inference regimes disappear,
* measurement and grounding are invisible.

**Didactic use.** C.2.1 allows the triangle **only** in the following cases:
1. As an **introductory picture** in guidance material (“this is the coarse triangle; the actual pattern is the episteme slot graph”).
2. As a **quotient diagram**: an explicit note that “this figure ignores viewpoint, grounding, carrier, and operationality; see C.2.1 for the full structure”.
3. As a **legacy alignment aid** when mapping to standards or literature that speak only in triangle terms.

**Guard.** Any pattern or documentation page that uses a “semantic triangle” diagram **MUST** either:
* explicitly state “this is a didactic projection of C.2.1 `U.EpistemeSlotGraph`”, or
* treat it as a legacy reference when aligning with external standards.

The triangle **MUST NOT** be used as a kernel‑level ontology or as a basis for morphism laws. All normative reasoning about epistemes proceeds via the slots and components of `U.EpistemeSlotGraph`.

### C.2.1:6 - Interaction with I/D/S and DescriptionContext  *(normative)*

C.2.1 is the **episteme‑layer carrier** that I/D/S discipline (A.7, E.10.D2) relies on. The link is made via `DescriptionContext`.

#### C.2.1:6.1 - DescriptionContext over C.2.1 components

For any episteme that is a **Description** or a **Specification** in the sense of E.10.D2, the field `subjectRef : U.SubjectRef` is interpreted as a **DescriptionContext triple**:
```
DescriptionContext = ⟨DescribedEntityRef, BoundedContextRef, ViewpointRef⟩
```

where:
* `DescribedEntityRef : U.EntityRef` — occupies `DescribedEntitySlot` (ValueKind `U.Entity`, species often constrained via EoIClass ⊑ `U.Entity`).
* `BoundedContextRef : U.BoundedContextRef` — points to the context that fixes vocabulary, units, and legal inferences for this description (E.10.D1).
* `ViewpointRef : U.ViewpointRef` — occupies `ViewpointSlot` (ValueKind `U.Viewpoint`) and determines which concerns, role‑enactor families, and conformance rules apply.

**Normative requirement (IDS‑13).**
For every `…Description` / `…Spec` episteme:
1. `subjectRef` **SHALL** be decodable to a well‑formed DescriptionContext triple.
2. `DescribedEntityRef` from that triple **SHALL** be identical to the field `describedEntityRef` that fills `DescribedEntitySlot` in the corresponding `U.EpistemeCard`/`U.EpistemeView`.
3. `ViewpointRef` in DescriptionContext **SHALL** agree with `viewpointRef` in the episteme card or be uniquely derivable from a `U.ViewpointBundle` in E.17.1 (with the derivation rule documented).

Intensions (I‑layer) such as `U.System`, `U.Method`, `U.Role` **do not** inhabit C.2.1 directly; they are the *targets* of I→D operations (`Describe_ID`) and appear as values of `DescribedEntitySlot` in resulting descriptions/specs.

#### C.2.1:6.2 - I→D and D→S morphisms over C.2.1

* **Describing (`Describe_ID : I → D`).**
  Produces an episteme whose:
  * `content : U.ClaimGraph` encodes the descriptive claims about the intension,
  * `describedEntityRef` points to the intension’s entity,
  * `groundingHolonRef` (if present) fixes where the description is evaluated or tested,
  * `viewpointRef` selects the describing viewpoint.

  `Describe_ID` is **conformant** to A.6.2 but not an Ep→Ep morphism (domain is Intension, codomain is Episteme). C.2.1 provides the **codomain schema** and ensures that the resulting Description has a valid DescriptionContext.

* **Specifying/Formalising (`Specify_DS/Formalize_DS : D → S`).**
  Takes a Description episteme and returns a Specification episteme with:
  * the same `describedEntityRef`,
  * the same `BoundedContextRef` and `ViewpointRef` (hence same DescriptionContext),
  * a `content : U.ClaimGraph` that raises formality F (F≥4) and adds test harness hooks, but is conservative with respect to the underlying intension.

  As an Ep→Ep morphism, `Specify_DS` is a **species of A.6.2** and must obey the invariants over the C.2.1 slots (DescribedEntityChangeMode = preserve; no change to DescribedEntity; ClaimGraph refinement only).

C.2.1 does **not** define I/D/S; it only insists that any `…Description`/`…Spec` species that claims to respect I/D/S discipline must:
* implement `U.EpistemeCard` or `U.EpistemeView` **with** `content`, `describedEntityRef`, `groundingHolonRef?`, `viewpointRef?`, and `referenceScheme?` fields, and
* wire these fields into `subjectRef` as DescriptionContext.

### C.2.1:7 - Alignment with A.6.2–A.6.4 (episteme morphisms)  *(normative)*
`U.EpistemeSlotGraph` is the **object‑level substrate** for the episteme morphism patterns:
* A.6.2 `U.EffectFreeEpistemicMorphing`
* A.6.3 `U.EpistemicViewing`
* A.6.4 `U.EpistemicRetargeting`

#### C.2.1:7.1 - Effect‑free episteme morphisms (A.6.2) over C.2.1
For any `f : X → Y` that is an instance of `U.EffectFreeEpistemicMorphing`:
* **Typed objects.**
  X and Y are `U.Episteme` instances realised as `U.EpistemeCard` / `U.EpistemeView` with at least the minimal core components:

  ```
  content            : U.ClaimGraph
  describedEntityRef : U.EntityRef      // DescribedEntitySlot
  groundingHolonRef? : U.HolonRef       // GroundingHolonSlot
  viewpointRef?      : U.ViewpointRef   // ViewpointSlot
  referenceScheme?   : U.ReferenceScheme// ReferenceSchemeSlot (ByValue)
  ```

  Any additional C.2.1+ components (RepresentationScheme, Tokens, Carriers, Operations) are visible to A.6.2 only through their declared SlotKinds (A.6.5).
* **DescribedEntityChangeMode characteristic.**
  `f` **MUST** declare a **`describedEntityChangeMode ∈ {preserve, retarget}`**:
  * `preserve` — `describedEntityRef(Y) = describedEntityRef(X)` and any change to `groundingHolonRef`/`viewpointRef` must be justified by Bridges/CorrespondenceModel, without changing the DescribedEntitySlot value;
  * `retarget` — permitted only for A.6.4 species; see below; in this case the characteristic records an intentional change in the pair `<describedEntityRef, groundingHolonRef>` under a declared `KindBridge` in the appropriate ReferencePlane.

  This **DescribedEntityChangeMode** is a CHR-style *characteristic* (A.17) on episteme morphisms, which points directly to `DescribedEntitySlot`. Avoid introducing a separate “describedEntity” term alongside `DescribedEntity`. 
  
* **Component discipline.**
  P0–P5 from A.6.2 are read **directly** in terms of C.2.1 components:
  * purity ⇒ only C.2.1 components of Y may change; no Work/Mechanism side‑effects;
  * conservativity ⇒ claims in `content_Y` read via `referenceScheme_Y` about the new `<DescribedEntity, GroundingHolon>` do not go beyond what already follows from `content_X` via `referenceScheme_X` under the declared DescribedEntityChangeMode and Bridges;
  * functoriality ⇒ composition of such transformations respects the slot structure and ReferenceSchemes.

Any Ep→Ep pattern that operates on `U.Episteme` **MUST** state which C.2.1 slots it reads and which it may write, in terms of SlotKinds/ValueKinds/RefKinds (A.6.5), and then declare itself a species of A.6.2/3/4 as appropriate.

#### C.2.1:7.2 - EpistemicViewing (A.6.3) as describedEntity‑preserving projections

`U.EpistemicViewing` is the **DescribedEntity-preserving** species of A.6.2. Over C.2.1 this means:
* `describedEntityRef(Y) = describedEntityRef(X)` — the same value in `DescribedEntitySlot`.
* `groundingHolonRef` is preserved, or changed only within a fixed grounding context (e.g. normalising identifiers for the same lab or runtime).
* `viewpointRef` is either:
  * preserved (internal normalisation under the same viewpoint), or
  * replaced by another `U.ViewpointRef` *within* a `U.MultiViewDescribing` family (E.17.0), with invariants enforced by a CorrespondenceModel.
* `content` and `referenceScheme` are transformed **conservatively**: no new intensional claims about the same DescribedEntity are introduced.

Typical examples:
* filtering or aggregating `U.ClaimGraph` to a view relevant for a stakeholder group;
* rendering a behavioural specification into a tabular or diagrammatic episteme under a publication viewpoint;
* normalising a logic‑heavy episteme into a more operational one, while keeping the same described system and context.

In terms of SoTA, EpistemicViewing behaves like a **lens** or **optic** over C.2.1: a focus (SlotKinds for content/representation) is manipulated while the DescribedEntity is fixed.

#### C.2.1:7.3 - EpistemicRetargeting (A.6.4) as DescribedEntity-bundle retargeting on episteme morphisms

`U.EpistemicRetargeting` is the species of A.6.2 where **`describedEntityChangeMode = retarget`**.
It is always a **morphism between epistemes** (`f : X → Y` in `U.Episteme`), but the adjective “retargeting” refers **not** to the fact that an episteme is mapped to another episteme (this is true for all A.6.2 species), and **not** to a separate describedEntity, but specifically to the **change in the DescribedEntity-bundle** selected by C.2.1:
* `describedEntityRef(Y) ≠ describedEntityRef(X)` — the value stored for `DescribedEntitySlot` changes;
* a `KindBridge` must relate `Kind(describedEntityRef(X))` and `Kind(describedEntityRef(Y))`;
* `groundingHolonRef` may remain the same (e.g. same plant, different subsystem) or be transformed along a Bridge in the same ReferencePlane.

In practice, many retargetings operate on the **target bundle** `<DescribedEntitySlot, GroundingHolonSlot>` (for example, when an episteme about a physical module is re-interpreted as an episteme about a function-holon realised in a different environment). The characteristic `describedEntityChangeMode` still classifies such morphisms by whether this bundle is preserved or intentionally re-identified under a `KindBridge` and reference-plane policy; the episteme on the codomain side is just the usual A.6.2 target object.


Over C.2.1 this is used for:
* **functional vs structural reinterpretation** (e.g. an episteme about a physical module retargeted to an episteme about the function it realises; StructuralReinterpretation in E.TGA becomes a species of A.6.4);
* **signal vs spectrum** transitions (Fourier‑style moves where the object‑of‑talk changes from time‑domain signal to frequency‑domain representation but an invariant, such as energy, is preserved);
* **data vs model** transitions (e.g. retargeting an episteme about raw observations to an episteme about a learnt model, with an invariant such as likelihood or sufficient statistics).

C.2.1 ensures that these retargetings have a **clear source and target** at the DescribedEntitySlot and that any such move is expressed as a morphism over well‑typed slots, not as an unstructured rewrite of “subject” or “object” labels.

### C.2.1:8 - Alignment with E.17.* (Multi‑View Describing & Publication)  *(normative)*

`U.EpistemeSlotGraph` underpins the E.17 cluster:
* E.17.0 `U.MultiViewDescribing`
* E.17.1 `U.ViewpointBundleLibrary`
* E.17.2 `TEVB — Typical Engineering Viewpoints Bundle`
* E.17 `MVPK — Multi‑View Publication Kit`

#### C.2.1:8.1 - Multi‑View Describing (E.17.0)

`U.MultiViewDescribing` organises **families of descriptions/specifications** over a shared entity‑of‑interest:
* The **EoIClass** parameter of E.17.0 is a species constraint on the ValueKind of `DescribedEntitySlot` (`EoIClass ⊑ U.Entity`).
* Each member of a multi‑view family is a `…Description`/`…Spec` episteme with:
  * `describedEntityRef` into that EoIClass,
  * `viewpointRef` drawn from a `U.ViewpointBundle`,
  * `subjectRef` decoding to DescriptionContext.

Within this pattern:
* `U.Viewpoint` is **exactly** the ValueKind of `ViewpointSlot` in C.2.1.
* `U.View` is `U.EpistemeView`, a species of `U.Episteme` whose `content` is already restricted to a particular `U.Viewpoint` and often also to a particular `U.RepresentationScheme`.

C.2.1 thus supplies the **per‑episteme** structure that E.17.0 rearranges into multi‑view families.

#### C.2.1:8.2 - Viewpoint bundles (E.17.1/E.17.2)

`U.ViewpointBundleLibrary` and TEVB specialise the `U.Viewpoint` node:
* A ViewpointBundle is a **set of `U.Viewpoint` instances** tailored to a class of DescribedEntities (e.g., holons in engineering contexts).
* TEVB fixes `EoIClass = U.Holon` (typically `U.System` or `U.Episteme`) and provides canonical engineering viewpoints: functional, structural, role‑enactor, interface‑oriented, etc.

From the C.2.1 perspective:

* these bundles populate the ValueKind of `ViewpointSlot`;
* engineering episteme species that want to be “TEVB‑aligned” must restrict `viewpointRef` to TEVB’s `EngineeringVPId` set, while keeping the same DescribedEntitySlot discipline.

#### C.2.1:8.3 - MVPK (E.17) as publication over C.2.1 views

MVPK treats `U.View` (i.e. `U.EpistemeView`) as its primary input:
* it uses `U.EpistemicViewing` species (A.6.3) to generate publication‑oriented views from engineering or logical views;
* it then packages these `U.View` epistemes into `U.Surface` artefacts via publication viewpoints and faces.

C.2.1’s distinction between:

* `U.Viewpoint` (intensional, epistemic perspective) and
* `U.PresentationCarrier` (surface in C.2.1+ and L‑SURF)

keeps **epistemic perspective and physical medium separate**:
* MVPK operates only on epistemes (Views) and then on carriers;
* the same View can be realised on multiple carriers without changing its describedEntity or ClaimGraph.

Any MVPK species that claims to be C.2.1‑conformant **MUST**:
* treat `U.View` as a `U.EpistemeView` with a valid C.2.1 core,
* document which C.2.1 slots it reads/writes (typically only representation/carrier‑related ones, leaving `DescribedEntitySlot` and `GroundingHolonSlot` untouched),
* refrain from introducing new claims about the described entity beyond what is in the source `U.View`’s ClaimGraph.

### C.2.1:9 - Bias‑annotation  *(informative)*

**Episteme‑first and pragmatics‑first.**
The pattern assumes that *nothing is a meaningful episteme* unless it is **about something for someone under some perspective**. This follows the pragmatic turn in semantics: describedEntity and concerns are not afterthoughts but part of the core structure. The graph is therefore built around slots for DescribedEntity, GroundingHolon, Viewpoint and ClaimGraph, not around abstract “propositions in the void”.

**Operational/representational bias.**
C.2.1+ anticipates that certain RepresentationSchemes are **operational** in Novaes’ sense (supporting direct syntactic inference, like pen‑and‑paper arithmetic or proof states) while others are **purely notational**. The pattern remains neutral on which schemes are used but bakes in a place for operations and carriers so that:

* symbol‑manipulating tools (SAT/SMT, proof assistants, classical programming languages),
* distributed/latent representations (LLM embeddings, latent protocols like “DroidSpeak”, “Coconut”‑style communication),
* hybrid ReAct‑style agent loops

can all be treated as different species operating over the same `U.EpistemeSlotGraph`. There is a bias towards making these operational differences **explicit** instead of hiding them behind “the model”.

**Viewpoint and stakeholder bias.**
The pattern leans on the ISO‑style idea that viewpoints encode **stakeholder concerns and role‑families**, but it generalises this beyond architecture. `U.Viewpoint` is intentionally intensional and not bound to any single discipline; still, the examples are skewed toward engineering and epistemic use‑cases.

**Didactic bias.**
The pattern is written to be teachable: semantic triangles are kept as didactic projections; examples like stools on lab rigs, services and SLAs, and model‑evaluation epistemes are deliberately simple. This may under‑represent more exotic epistemes (e.g. artistic, legal, or socio‑technical ones), but the intention is that these use the same slots with different species‑level constraints.

### C.2.1:10 - Conformance checklist  *(normative)*

**CC‑C.2.1‑1 - Minimal core components for episteme species.**
Any species of `U.Episteme` that participates in I/D/S discipline or in E.17 multi‑view/publishing **MUST** be representable as `U.EpistemeCard`/`U.EpistemeView` with at least:

```
content            : U.ClaimGraph
describedEntityRef : U.EntityRef
groundingHolonRef? : U.HolonRef
viewpointRef?      : U.ViewpointRef
referenceScheme?   : U.ReferenceScheme      // ByValue
meta               : …                      // edition, provenance, status (A.7/F.15)
```

and corresponding SlotSpecs consistent with A.6.5 (`DescribedEntitySlot`, `GroundingHolonSlot`, `ClaimGraphSlot`, `ViewpointSlot`, `ReferenceSchemeSlot`).

**CC‑C.2.1‑2 - No kernel type for “DescribedEntity” or “GroundingHolon”.**
Patterns **MUST NOT** introduce kernel types `U.DescribedEntity` or `U.GroundingHolon`:
* DescribedEntitySlot has ValueKind `U.Entity` ( species‑constrained via EoIClass if needed),
* GroundingHolonSlot has ValueKind `U.Holon`.

Plain terms “described entity” and “grounding holon” are allowed only as **role descriptions** of slot occupants.

**CC‑C.2.1‑3 - SlotKind/ValueKind/RefKind discipline.**
All episteme‑related slots, including `DescribedEntitySlot`, `GroundingHolonSlot`, `ClaimGraphSlot`, `ViewpointSlot`, `ViewSlot`, `ReferenceSchemeSlot` (and any extensions in C.2.1+), **MUST**:
* follow the naming discipline of A.6.5 (`*Slot` for SlotKinds, `*Ref` only for RefKinds/fields),
* declare a ValueKind and refMode (`ByValue` or a RefKind),
* be used consistently across patterns that refer to the same conceptual position.

**CC‑C.2.1‑4 - DescriptionContext wiring.**
Any episteme species whose name or pattern claims to be a `…Description` or `…Spec` in the sense of E.10.D2 **MUST**:
* expose `subjectRef : U.SubjectRef`,
* provide a decoding to `DescriptionContext = ⟨DescribedEntityRef, BoundedContextRef, ViewpointRef⟩`,
* ensure that `DescribedEntityRef` matches `describedEntityRef` (DescribedEntitySlot), and
* ensure that `ViewpointRef` matches `viewpointRef` or is derivable from a `U.ViewpointBundle` under documented rules.

**CC‑C.2.1‑5 - Morphism declarations over slots.**
Any pattern in A.6.2–A.6.4, E.17, E.TGA, or discipline packs that defines morphisms between epistemes **SHALL**:
* state whether it is a species of `U.EffectFreeEpistemicMorphing`, `U.EpistemicViewing`, or `U.EpistemicRetargeting`,
* declare its `describedEntityChangeMode` (preserve/retarget),
* name which SlotKinds it reads and writes,
* state its behaviour on `describedEntityRef`, `groundingHolonRef`, `viewpointRef`, and `referenceScheme`.

**CC‑C.2.1‑6 - Semantic‑triangle usage guard.**
If a semantic triangle or parallelogram diagram appears in a pattern or tutorial, there must be an explicit note that:
* it is a didactic projection of `U.EpistemeSlotGraph`, and
* normative laws are stated in terms of C.2.1 nodes and morphisms, not in terms of triangle corners.

**CC‑C.2.1‑7 - KD‑CAL / ReferencePlane alignment.**
Any pattern that evaluates or compares epistemes (KD‑CAL/LOG‑CAL, CHR, CG‑Spec, etc.) **MUST** point out:
* how `U.ClaimGraph` is interpreted in a ReferencePlane,
* how `GroundingHolonSlot` figures into measurement or validation,

**CC‑C.2.1‑8 - Context locality and Bridges.**
Any `U.Episteme` species that is consumed by KD‑CAL / LOG‑CAL / CHR‑based patterns **SHALL** declare a `U.BoundedContextRef`; all F–G–R computations and C.2.1 slot interpretations are **context‑local**.  Cross‑context use **MUST** proceed via an explicit Bridge with CL / Φ‑policy (F.9/B.3), with penalties routed to R‑lanes only; F and the slot structure from C.2.1 remain unchanged.

**CC‑C.2.1‑9 - Carriers and Work outside episteme content.**
C.2.1 **inherits** A.7/A.12’s separation obligations: `U.PresentationCarrier` / `U.Surface` artefacts and `U.Work` instances **MUST NOT** be treated as parts of `U.Episteme` or as values of any SlotKind in `U.EpistemeSlotGraph`. Episteme content stays in `U.ClaimGraph` and `U.ReferenceScheme`; evidence enters only via `U.EvidenceRole` bindings that point to external `U.Work` / carriers (A.10/B.3). Changing carriers or re‑publishing work alone does **not** change the episteme determined by ⟨content, describedEntityRef, referenceScheme⟩ in its `U.BoundedContext`.

**CC‑C.2.1‑10 - Reflexive describedEntity guard.**
When an episteme uses C.2.1 to speak **about** another episteme (ReferencePlane = episteme), or about itself (self‑describing or meta‑specification cases), patterns **SHALL** ensure that the resulting JustificationGraph / evaluation chains are **acyclic** along support paths. Reflexive `describe` / citation edges may exist as literature anchors, but they MUST NOT form minimal support cycles for acceptance or KD‑CAL assurance decisions; the trust calculus MUST always bottom out in external evidence (`U.Work` with `U.EvidenceRole`) rather than in purely self‑referential claims.

### C.2.1:11 - Consequences  *(informative)*

**Benefits**
* **Single, extensible episteme core.**
  C.2.1 gives a small, stable set of positions (DescribedEntity, GroundingHolon, ClaimGraph, Viewpoint, View, ReferenceScheme) and components (`U.EpistemeCard`, `U.EpistemeView`, `U.EpistemePublication`) on which all higher‑level patterns depend. This avoids the proliferation of “epistemic objects” and “facets” with overlapping semantics.
**Transparent DescribedEntity & grounding discipline.**
  The pair (`DescribedEntitySlot`, `GroundingHolonSlot`) is no longer hidden inside ad-hoc “SubjectRef” fields or semantic triangles: both are explicit, typed slots. This makes retargeting, viewing and correspondence laws (A.6.2–A.6.4, E.17.0) easier to state and check.
* **Better fit for contemporary representation practice.**
  By distinguishing ClaimGraph, RepresentationScheme, Tokens, Carriers and Operations (in C.2.1+), the pattern matches contemporary SoTA views of notation and formalism:
  * formal languages as cognitive artefacts and de‑semanticisation tools (Novaes),
  * operational iconicity and medium‑sensitive reasoning (Krämer, Malafouris),
  * hybrid symbolic–neural workflows (e.g. ReAct, tool‑augmented LLMs, latent protocols).
  FPF can model both symbol‑heavy and latent‑heavy workflows without privileging either.
* **Uniform substrate for multi‑view description and publication.**
  MultiViewDescribing, viewpoint bundles (TEVB), and MVPK all land on the same episteme core. This avoids the current “views vs viewpoints vs faces” confusion and leaves “architecture” as a domain‑specific specialisation rather than a competing meta‑ontology.
* **Tooling alignment.**
  Slot discipline plus explicit episteme components map cleanly to implementation types (records, row‑typed schemas, effectful handlers). Tools can generate code, schemas or telemetry from episteme species without guessing what “subject”, “context” or “object” mean.

**Trade‑offs / costs**
* **More explicit structure.**
  Authors must declare slots, ValueKinds and references explicitly, and keep DescriptionContext consistent. This is more upfront work than writing ad‑hoc “Subject/Object” fields, but it pays off in substitution safety and cross‑pattern reuse.
* **Migration effort.**
  Legacy uses of “EpistemicObject”, “Facet”, “Subject”/“Object”, and raw `…Ref` fields will need refactoring into C.2.1 slots + A.6.5 SlotSpecs. Migration notes and aliasing can ease the transition, but mechanical cleanup will still be required.
* **Exposure of representation biases.**
  Being explicit about RepresentationSchemes and Operations may surface disagreements about which representations are “primary” in a team or discipline. C.2.1 does not resolve these disagreements; it only makes them visible and therefore debatable.

#### C.2.1:12 - Relations  *(overview)*

**Builds on**
* A.1 `U.Holon` — for treating episteme as a holon with components.
* A.6.0 `U.Signature` — for interpreting episteme kinds as n‑ary relations over slots.
* A.6.5 `U.RelationSlotDiscipline` — for SlotKind/ValueKind/RefKind discipline over episteme slots.
* A.7, E.10.D2 — for I/D/S discipline and the Interpretation of `subjectRef` as DescriptionContext.
* C.2 (KD‑CAL, LOG‑CAL) — for ClaimGraph semantics, ReferencePlanes, and Bridges.
* E.8, E.10 — for pattern authoring discipline and lexical guards.

* **Constrains**
* A.6.2–A.6.4 — by fixing the minimal episteme component set those morphisms operate on and by requiring an explicit **DescribedEntityChangeMode characteristic** (`describedEntityChangeMode ∈ {preserve, retarget}`) over `DescribedEntitySlot`/`GroundingHolonSlot`.
* E.17.0–E.17.2 — by specifying how `DescribedEntity`, `Viewpoint`, `View` and ReferenceSchemes are represented at episteme level.
* E.17 (MVPK) — by separating `U.View` (episteme) from `U.PresentationCarrier` (surface), and by requiring that publication morphisms be `U.EpistemicViewing` species over C.2.1‑conformant views.
* F.18 (LEX‑BUNDLE) — by providing the episteme‑specific name cards and guards for DescribedEntity/GroundingHolon/Viewpoint/View/ReferenceScheme and their SlotKinds.

**Used by**
* A.6.2 `U.EffectFreeEpistemicMorphing` — as the default episteme object structure for episteme‑to‑episteme transforms.
* A.6.3 `U.EpistemicViewing` — as the substrate for describedEntity‑preserving projections (views).
* A.6.4 `U.EpistemicRetargeting` — as the substrate for DescribedEntity-bundle retargeting transforms between epistemes (Ep→Ep with `describedEntityChangeMode = retarget`).
* E.17.0 `U.MultiViewDescribing`, E.17.1, E.17.2 — to organise families of D/S‑epistemes under Viewpoints and EoI classes.
* E.17 (MVPK) — to publish episteme views as surfaces.
* E.TGA — to interpret StructuralReinterpretation and other engineering projections as episteme morphisms over a well‑typed `U.EpistemeSlotGraph`.

Together, these relations make `U.EpistemeSlotGraph` the **single normative core** for thinking about epistemes, their DescribedEntity mapping, their representations, and their transformations across FPF.

### C.2.1:End

## C.2.2 - Reliability R in the F–G–R triad

> Reliability (R) is a conservative, evidence-bound warrant signal for a typed claim under an explicit claim scope (G). Cross-context reuse is **Bridge-only**: scope may be re-expressed via `translate(Bridge,·)` (often narrowing), while congruence penalties route to **R only**.

> **Type:** Architectural (A)
> **Status:** Stable

### C.2.2:1 - Problem frame

KD‑CAL asks a simple operational question: *“Where can I safely use this claim?”*
FPF answers with a minimal “epistemic location” built from three coordinates and one bridge qualifier:

* **F** (Formality) describes *how the claim is expressed* and how strongly it supports verification workflows (C.2.3).
* **G** (Claim scope) describes *where the claim is asserted to apply* as a set-like object (A.2.6).
* **R** (Reliability) describes *how strongly the claim is warranted* by linked evidence under that scope.
* **CL / CL^k / CL^plane** (Congruence Levels) describe *lossy transport* when claims are reused across contexts, kinds, or planes (B.3, C.3).
  CL values live on **edges/bridges** (not on the claim as a “4th coordinate”).

In practice, the triad is frequently used before it is made explicit:

* Authors implicitly “average” disparate evidence and report a single confidence.
* Teams treat higher formality (F) as if it automatically implies higher warrant (R).
* Scope growth is smuggled in through phrasing instead of explicit scope operators (A.2.6).
* Cross-context reuse occurs without explicit bridges and without routing congruence loss into R.

This pattern makes **R** explicit in KD‑CAL and fixes the **triad discipline** required by Kind‑CAL (C.3) and the Trust & Assurance calculus (B.3).

### C.2.2:2 - Problem

FPF needs a reliability coordinate that is:

1. **Auditable.** A reader can trace R to concrete evidence and see how reuse penalties were applied.
2. **Composable.** R can be propagated through claim graphs conservatively, without illegal scale arithmetic.
3. **Orthogonal.** R is not conflated with F (expression) or G (scope).
4. **Bridge-safe.** Any loss from transport across contexts/kinds/planes is explicit and affects **R only**. 
5. **Minimal.** The solution does not introduce new core types or new face-kinds.

### C.2.2:3 - Forces

| Force                                         | Tension                                                                                                            |
| --------------------------------------------- | ------------------------------------------------------------------------------------------------------------------ |
| **Single number vs multi-tradition evidence** | People want one scalar ↔ evidence comes from heterogeneous practices (proofs, tests, telemetry, expert review).    |
| **Rigor vs humility**                         | Claims need to be usable in decisions ↔ overconfident scores are dangerous and hard to unwind.                     |
| **Formal vs empirical warrant**               | Proof can be decisive in a formal theory ↔ real-world deployment requires empirical adequacy and drift management. |
| **Scope realism vs marketing scope**          | Narrow scopes raise R ↔ incentives push for broad statements with hidden preconditions.                            |
| **Reuse vs semantic loss**                    | Reuse is valuable ↔ reuse across contexts/kinds/planes is inherently lossy.                                        |
| **Toolability vs expressive freedom**         | A validator needs crisp rules ↔ authors want flexible narratives and domain nuance.                                |

### C.2.2:4 - Solution

#### C.2.2:4.1 - Canonical triad contract

**Definition DEF‑C2.2‑1 (Epistemic location).**
An epistemic location for a claim `c` is the tuple:

`Loc(c | K, S) = ⟨F(c), G(c), R_eff(c)⟩`

where:

* `F(c)` is Formality (C.2.3), treated as an **ordinal**.
* `G(c)` is Claim scope (A.2.6), treated as a **set-like scope object**.
* `R_eff(c)` is Effective reliability for `c`, treated as a **ratio-scale** scalar in `[0,1]` (or an **ordinal proxy** at **[M‑0/M‑1]**; see §4.5.A).
  `R_eff` is computed **pathwise** (DEF‑C2.2‑3): when more than one admissible justification path exists, publish multiple path records (PathId rows) and cite which PathId(s) a guard/decision consumed (see §4.8.A / G.6). Any collapse to a single scalar is an explicitly declared Γ‑policy (no implicit averaging).

A location is always understood *relative to* a bounded context and the assurance carriers used elsewhere in FPF:
* `K` is the declared `U.BoundedContext`.
* `S ∈ {design, run}` is the claim’s stance carrier (no design/run chimeras).
* `ReferencePlane` is declared where applicable; plane crossings apply `CL^plane` and penalize **R only**.
* When the claim is published on the Working‑Model surface, the author also declares `validationMode ∈ {postulate, inferential, axiomatic}` (E.14 / B.3).

**Mode-to-lane hint (informative).** `validationMode` sets the *default expectation* for which assurance lane carries the initial burden (B.3.3 / B.3.5).
It does **not** add a new axis and does **not** change the meaning of `R`:
* `axiomatic` → VA-dominant (constructive grounding / proof artifacts); if `ReferencePlane=world`, LA may still be required.
* `inferential` → VA+TA-dominant (reasoned chain + typing/alignment assurance); LA is optional and scope-bound.
* `postulate` → LA-dominant (empirical validation with freshness/decay); VA is optional.
In all modes, **R remains warrant**, not ontological truth; “proof ⇒ R=1 in the world” is a category error.

**Profile note (informative; fold compatibility).** Some profiles treat empirical `R` as N/A for strictly **axiomatic** lines and use a tagged proxy `R_proxy := F` (`line=formal`) for folding, as an explicit proxy rather than an implicit “F⇒R” rule (B.1.3).

`⟨F,G,R⟩` is an **assurance tuple**, not a `U.CharacteristicSpace`; do not draw “trajectories” in `⟨F,G,R⟩`.

#### C.2.2:4.2 - What Reliability R means in KD‑CAL

**Definition DEF‑C2.2‑2 (Reliability as warrant).**
`R` is a conservative, evidence-bound indicator of how strongly the claim “holds as stated” under its declared scope and context. It is interpreted as a *warrant strength*, not as truth.

**Prophylactic clarification.**

* A higher `R` means “the evidence and its relevance supports relying on this claim under this scope.”
* A higher `F` means “the claim’s form is amenable to stronger checking and reuse,” but does not itself imply the claim is warranted.
* A larger `G` means “the claim applies to more cases,” but does not itself imply the claim is warranted in those cases.

#### C.2.2:4.3 - Pathwise weakest-link propagation (series vs parallel)

KD‑CAL’s default Γ‑fold is **weakest‑link** on the *entailment spine* (the premises/lemmas actually needed), computed per justification path. It is conservative, monotone, and auditable.

**Definition DEF‑C2.2‑3 (Pathwise weakest-link fold).**
Let `P` be a justification path for claim `c`. Let `SpineClaims(P)` be the required supports on the entailment spine, and let `SpineBridges(P)` be the bridges actually traversed on that spine (scope bridges, kind bridges, plane/notation transports where applicable).

Define the raw warrant of the path as:

`R_raw(P) = min_{i ∈ SpineClaims(P)} R_eff(i)`

and compute the effective warrant of the path by applying congruence penalties (see §4.5 for policy shape):

`R_eff(P) = Π(R_raw(P); Φ(CL_min(P)), Ψ(CL^k_min(P)), Φ_plane(CL^plane_min(P)))`

**Spine discipline.** The `min` is taken over the *entailment spine* only (no satellites, no “nice-to-have” citations).

This matches the KD‑CAL propagation rule (C.2:4.3) and the Trust & Assurance skeleton (B.3): weakest-link on the spine, penalize only by the worst (lowest) congruence encountered on the path (no averaging).

**Parallel support (optional, declared).**
If the same claim `c` has multiple **independent** justification paths `{P_j}` (OR‑style support), the default is:

`R_eff(c) = max_j R_eff(P_j)`

Independence is recorded as an explicit note (e.g., separate rigs/datasets/proof lines), per CC‑C.2.2‑10 and the KD‑CAL composition rule (C.2:4.3).
If the “multiple paths” actually cover **different** scope slices, do not use `max` to hide weaker slices; instead publish distinct `G_path` (SpanUnion‑style coverage) and keep per‑path `R_eff` traceable (A.2.6 / C.2:4.3).

**Conflict detection (no averaging).**
If the evidence graph supports both `p` and `¬p` with overlapping scope, do **not** average. Separate by context/scope, or mark the claim **provisional** with explicit conflict edges until resolved.

#### C.2.2:4.4 - Congruence penalties route to R only (no silent widening)

Cross-context reuse and cross-kind reuse are treated as **transport with loss**, and loss is expressed as a penalty that reduces `R`.

**Invariant INV‑C2.2‑1 (R-only penalty routing).**
For any transport step that uses a bridge with a declared congruence level, the transported claim preserves its **F** value, re-expresses its scope via an explicit **scope translation** (`translate`) when needed, and only its **R** value is decreased by congruence penalties:

`F_out = F_in`
`G_out = translate(Bridge, G_in)`  *(identity only for within-context identity use; cross-context use is undefined without a Bridge)*
`R_out ≤ R_in`

Claim scope may be *re-expressed* by an explicit translation, but must not be silently widened:

`G_out = translate(Bridge, G_in)`  (may narrow / drop unmappable slices; never widen without an explicit ΔG)

**No implicit translation.** Translation between contexts never occurs implicitly: if the target context differs, an explicit Bridge (with declared CL and loss note) is mandatory; otherwise the reuse is non-conformant.
**No implicit translation.** Cross‑Context reuse is conformant only via an explicit Bridge (declared CL + loss note) and an explicit `translate(Bridge,·)`; see **CC‑C.2.2‑4**.

This invariant is why KD‑CAL guard macros and crossing surfaces can be simple: transport never silently *widens* a claim; it either (i) translates/narrows scope explicitly, and/or (ii) reduces warrant.

`translate` is the USM operator (A.2.6). It may drop unmappable slices and may include refit-like normalization; **this is not a penalty**. Any further narrowing is an explicit Δ‑move (ΔG−) under A.2.6. Congruence loss (CL/CL^k/CL^plane) still routes to **R only**.

**Notation/plane transports.** NotationBridge and plane transports contribute to the relevant `CL*_min(P)` bottlenecks for the path; they do not “lower F” by penalty. If an author actually rewrites a claim into a different formality level, that is a new episteme (ΔF), not “transport”.

#### C.2.2:4.4.A - Worked micro-example: `translate(G)` + penalty (A.2.6:12.2)

**Source context:** `MaterialsLab@2026`. Claim:

> `c:` “Adhesive X retains ≥85% tensile strength on Al6061 for 2 h at 120–150 °C.”

* `G_src := {substrate=Al6061, temp∈[120,150]°C, dwell≤2h, Γ_time=window(1y), rig=Calib‑v3}`
* `Loc_src(c) = ⟨F_src, G_src, R_raw⟩`

**Target context:** `AssemblyFloor@EU‑PLANT‑B`. Reuse requires a declared Bridge `b`:

* Bridge `Bridge#MatLab_to_PlantB` maps lab rig → plant rig and introduces a measurement correction; `CL(Bridge#MatLab_to_PlantB)=2` with loss note “±2 °C bias.”
* **Scope translation:** `G_tgt := translate(b, G_src)` which (in this case) narrows the temperature span to `[122,148]°C` due to the correction.
* **Penalty routing:** using policy `Φ=Φ_v1`, compute
  `R_eff := max(0, R_src − Φ_v1(CL(Bridge#MatLab_to_PlantB)))`.

**Key point:** `G` changed only because `translate(b,·)` explicitly re-expressed the *same entitlement* in the target Context’s slice vocabulary; the **congruence loss** still affects **R only**. If authors decide that only `[125,145]°C` is safe to claim on the floor, that is an explicit **ΔG−** decision (scope edit), not a congruence penalty.

#### C.2.2:4.5 - Effective reliability under transport (policy-defined, monotone, bounded)

When a claim is reused via bridges, `R_eff` is computed by applying penalties determined by congruence levels.

**Definition DEF‑C2.2‑4 (Effective reliability under transport).**
Let:

* `CL` be the congruence level of a scope bridge (B.3).
* `CL^k` be the congruence level of a kind bridge (C.3).
* `CL^plane` be the congruence level of a plane transport bridge (B.3 / plane patterns).

Let `Φ`, `Ψ`, and `Φ_plane` be **policy-defined**, **monotone**, **bounded**, **table-backed** penalty policies applied on the relevant edges:
* `Φ(CL)` — scope/context Bridge penalty (CL).
* `Ψ(CL^k)` — KindBridge penalty (CL^k) when kinds are mapped.
* `Φ_plane(CL^plane)` — plane-crossing penalty when `ReferencePlane` differs.

**Important (direction of monotonicity).** Congruence ladders are “polarity up” (higher CL = better fit). Per **CC‑G0‑Φ** and the Trust & Assurance skeleton, penalty tables are monotone **decreasing** in their CL ladders (if `CL1 < CL2` then `Φ(CL1) ≥ Φ(CL2)`, analogously for `Ψ` and `Φ_plane`) and bounded so that `R_eff` remains within `[0,1]` after clipping. Penalty magnitudes are not required to lie in `[0,1]` (tables may exceed 1 to force `R_eff → 0` under the subtractive default); what matters is monotonicity, boundedness, and published policy identifiers.

Define:

`R_eff(P) = clip_0^1( Π(R_raw(P); Φ(CL_min(P)), Ψ(CL^k_min(P)), Φ_plane(CL^plane_min(P))) )`

where each `*_min(P)` is the **lowest** congruence level encountered on the entailment spine of `P` for that dimension (a bottleneck; no averages), and `clip_0^1(x)` truncates to `[0,1]`.

**Default (safe) instantiation (subtractive).**
When policies are expressed as subtractive penalties, a safe default is:

`R_eff(P) = max(0, R_raw(P) − Φ(CL_min(P)) − Ψ(CL^k_min(P)) − Φ_plane(CL^plane_min(P)) )`

This generalises the B.3 skeleton to multiple congruence ladders (scope vs kind vs plane) without introducing new axes. If a dimension is not present on the path, its penalty term is treated as neutral (`0` in the subtractive default).

**Provisional marking.**
Default admissibility thresholds for reuse are set by Bridge calibration profiles (e.g., G.7). Typically, `CL=1` requires an explicit waiver to proceed and `CL=0` is inadmissible; this pattern only specifies that such thresholds gate transport before any numeric penalty is meaningful.

#### C.2.2:4.5.A - Math-by-level gating (B.1.3:4.3)

* **[M‑0/M‑1]** allow **ordinal** comparisons only (no arithmetic on `R_eff`); Φ/Ψ/Φ_plane may be qualitative (“low/med/high”). Publish evidence links + lane tags.
* **[M‑2/L1]** numeric `R_eff` requires referencing numeric, table-backed policy identifiers for Φ/Ψ/Φ_plane (and Π if not default), plus reproducibility tags for empirical legs; otherwise treat the claim as [M‑1] semantics.

#### C.2.2:4.6 - Evidence lanes are not new axes

KD‑CAL does not add new global coordinates beyond F–G–R. Instead, it requires that reliability be *explainable* via **assurance lanes** (B.3.3):

* **TA** (Typing assurance): semantic/type alignment sufficient for transport and composition.
* **VA** (Verification assurance): logical/algorithmic checking, proof, model checking, static guarantees.
* **LA** (Validation assurance): empirical adequacy under declared conditions, tests, benchmarks, telemetry.

Lane reporting is how KD‑CAL supports the common research distinction between logical soundness and empirical adequacy **without introducing new global axes**.
Lanes remain **separable** in SCR/Notes; they are not averaged into a “single tradition score”.

#### C.2.2:4.7 - Scope operations are kind-safe (and use the ClaimScope algebra)

Reliability is meaningless if scope operations are applied to ill-typed entities.

**Well-formedness constraint WFC‑C2.2‑1 (Type before scope).**
Let `G1` and `G2` be claim scopes associated to described entities of kinds `K1` and `K2`. A scope operation that combines them (e.g., `G1 ∩ G2` for serial intersection, `SpanUnion({G_i})` for parallel coverage, or `translate(Bridge, G)` for cross‑context reuse) is defined only if:
* `K1 = K2`, or
* (same `U.BoundedContext`) `K1 ⊑ K2` or `K2 ⊑ K1` (an explicit kind relation/cast is named), or
* (cross‑Context) there exists a declared **KindBridge** relating `K1` and `K2` with an explicit `CL^k` (C.3).

This constraint prevents “type-by-scope” anti-patterns where scope manipulation is used to hide type mismatch.

#### C.2.2:4.8 - Minimal authoring recipe

A minimal, conforming KD‑CAL authoring flow for reliability is:

1. **Fix the typed claim.** State the claim as a typed proposition about a described entity (Kind‑CAL, C.3).
2. **Declare claim scope.** Write `G` explicitly using A.2.6 operators; avoid scope-by-wording.
3. **Declare stance carriers.** Declare `K=U.BoundedContext`, `S ∈ {design, run}`, and (where relevant on Working‑Model surfaces) `validationMode ∈ {postulate, inferential, axiomatic}`; declare `ReferencePlane` if crossings are in play.
4. **Bind evidence.** Attach evidence stubs and lane tags (TA/VA/LA) and validity windows / decay policy where applicable (B.3.3, B.3.4).
5. **Choose Γ-mode.** Declare whether the support is **series** (required) or **parallel** (independent lines to the same claim).
6. **Compute R_raw.** Use the weakest-link fold on the entailment spine; for parallel support, use `max` only with an explicit independence note.
7. **Declare bridges on reuse.** If you reuse across contexts/kinds/planes/notations, declare the bridge(s) (including NotationBridge where applicable) and their CLs.
   Cross‑Context reuse is conformant only when an explicit Bridge is declared; CL admissibility rules apply (waiver or forbid) before any numeric penalty is meaningful (see **CC‑C.2.2‑4**).
   **Reuse note (FPF discipline).** When this section refers to “reuse/portability across contexts/planes”, interpret it as Bridge-only reuse per §4.4: e.g., Bridge `Bridge#MatLab_to_PlantB` with `CL=2` and an explicit loss note, applying policy ids `Φ=Φ_v1` (and, where applicable, `Ψ=Ψ_v2`, `Φ_plane=Φ_plane_v1`) to reduce `R_eff` only.

8. **Compute R_eff.** Apply the declared penalty policies into `R` (never into `F` or `G`), and publish `⟨F,G,R_eff⟩` with traceable references and policy identifiers.

A reliable claim is not a loud claim; it is a claim that can be *carried*.

#### C.2.2:4.8.A - Authoring template: Path summary row (copy/paste)

When publishing `R_eff` for a claim, authors SHOULD include a compact, claim-local **path summary**. This is intentionally shaped so it can be turned into tooling later (EvidenceGraph/PathId in G.6) without introducing new Core types or face-kinds.

| PathId | Entailment spine (required supports) | CL_min | CL^k_min | CL^plane_min | Policy-id(s) (Φ / Ψ / Φ_plane) | R_raw | R_eff | Lane tags (TA/VA/LA) | valid_until |
| ------ | ----------------------------------- | ------ | -------- | ----------- | ------------------------------ | ----- | ----- | --------------------- | ---------- |
| P‑1    | `c ← {c_a, c_b, c_c}`               | 2      | 3        | —           | `Φ=Φ_v1`, `Ψ=Ψ_v2`             | 0.82  | 0.67  | {TA, LA}              | 2026‑09‑30 |

Notes:
* `CL_*_min` values are **bottlenecks** on the relevant path/dimension (no averaging).
* `valid_until` is the **earliest** expiry across empirical legs (or `—` / “fenced to TheoryVersion” for non-decaying proof legs).
* If you publish multiple admissible paths, include multiple rows and cite which PathId(s) your decision/guard consumed.

### C.2.2:5 - Archetypal Grounding

Informative; non-binding.

#### C.2.2:5.1 - System illustration

**System.** A brake controller `S` has a claim:

> `c1:` “For road friction μ ∈ [0.2, 0.9] and vehicle mass m ∈ [900, 2200] kg, wheel slip stays in [0.05, 0.25] under ABS control.”

* `F(c1)=F5` because the controller and constraints are expressed as a machine-checkable model plus executable test harness (C.2.3).
* `G(c1)` is the declared operating envelope (A.2.6) as a product set in `(μ, m, speed, tire)` space.
* Evidence:

  * VA: model-checking of a simplified plant/controller model (strong, but only for the simplified plant).
  * LA: HIL simulation + track tests under sampled conditions with recorded telemetry windows (freshness required).
  * TA: typed alignment between “μ” in simulations, “μ” in the estimation pipeline, and “μ” inferred from real-world sensors.

If telemetry is reused from the track context to the road context, a scope bridge is declared with `CL=2`. Using the default monotone penalty table (B.3), the LA contribution is reduced, and the derived `R_eff(c1)` drops accordingly. The claim’s envelope `G(c1)` does not change; only the warrant for transporting the evidence does.

#### C.2.2:5.2 - Episteme illustration

**Episteme.** A paper asserts two claims about an algorithm `A`:

* `c2:` “A terminates for all inputs in domain D.” (axiomatic / proof-carrying)
* `c3:` “A achieves ≥ 0.92 F1 on dataset family F under deployment preprocessing P.” (empirical)

`c2` can achieve high VA with a proof artifact; its LA lane may be N/A, but its TA lane remains relevant because the intended meaning of “domain D” must align with the implementation’s input model.
`c3` requires LA evidence and a freshness/shift policy because dataset and preprocessing drift change the scope and the warrant. If `c3` is reused from a lab dataset context to a production context, a bridge with explicit CL is required, and `R_eff` is reduced until new in-context evidence is attached.

### C.2.2:6 - Bias-Annotation

Informative; non-binding.

Lenses tested: **Gov**, **Arch**, **Onto/Epist**, **Prag**, **Did**. Scope: **Universal**.

* **Onto/Epist bias:** High formality is often mistaken for high warrant (“proof therefore true in the world”). This pattern mitigates by forcing LA/TA visibility and by routing transport loss into R rather than mutating the claim.
* **Prag bias:** Teams may Goodhart R by narrowing scope or selecting easy tests. This pattern mitigates by requiring explicit scope declaration and by making scope changes first-class (A.2.6).
* **Gov bias:** Overconfident reuse across contexts is a recurring failure mode in governance settings. This pattern mitigates by forcing explicit bridges and penalties for reuse.
* **Did bias:** A single scalar is seductive; it hides what kind of warrant exists. Lane reporting keeps the scalar honest.

### C.2.2:7 - Conformance Checklist

Normative.

| ID                                            | Requirement                                                                                                                                                                                                                 | Purpose                                                                       |
| --------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------- |
| **CC‑C.2.2‑1 (Triad publication).**           | Authors of a KD‑CAL location **SHALL** publish `⟨F,G,R_eff⟩` as a bundle for a specific claim, rather than publishing `R` alone.                                                                                            | Prevents decontextualised confidence scores.                                  |
| **CC‑C.2.2‑2 (R-only penalty routing).**      | A conforming implementation of KD‑CAL transport **SHALL** satisfy **INV‑C2.2‑1**.                                                                                                                                           | Ensures bridges reduce warrant without silently mutating expression or scope. |
| **CC‑C.2.2‑3 (Weakest-link fold).**           | A conforming implementation of KD‑CAL reliability propagation **SHALL** use **DEF‑C2.2‑3** as the default for required supports, unless an alternative Γ‑fold is explicitly declared and remains monotone and conservative. | Prevents confidence laundering through aggregation.                           |
| **CC‑C.2.2‑4 (Bridge visibility for reuse).** | Authors **SHALL** declare explicit bridges with CL values for any cross-context, cross-kind, or cross-plane reuse that affects `R_eff`.                                                                                     | Makes transport loss auditable and machine-checkable.                         |
| **CC‑C.2.2‑5 (Penalty policy visibility).**   | Authors or tooling **SHALL** reference the active policy identifiers used for `Φ`, `Ψ`, `Φ_plane` **and** the penalty aggregation rule `Π` (if not the default) when computing `R_eff`.                                   | Ensures repeatability and prevents hidden policy drift.                       |
| **CC‑C.2.2‑6 (Type before scope).**           | Authors and validators **SHALL** enforce **WFC‑C2.2‑1** for scope composition operations.                                                                                                                                   | Prevents ill-typed scope algebra from creating incoherent reliability claims. |
| **CC‑C.2.2‑7 (Evidence binding).**            | Authors **SHALL** bind any asserted `R_eff` to evidence references that enable TA/VA/LA inspection, consistent with the assurance lane discipline (B.3.3) and evidence decay discipline (B.3.4).                            | Keeps R grounded and updateable.                                              |
| **CC‑C.2.2‑8 (No ordinal arithmetic).**       | Validators **SHALL** reject any computation that treats `F` or `CL` as if they were ratio-scale numbers (e.g., averaging, subtraction), except where explicitly permitted as a policy-defined penalty function on `R`. Validators **SHALL** also reject arithmetic over `R_eff` when it is published as an **ordinal proxy** ([M‑0/M‑1]). | Enforces CSLC legality and prevents silent scalarisation.                     |
| **CC‑C.2.2‑9 (Stance carriers declared).**    | Authors **SHALL** declare `U.BoundedContext K`, `S ∈ {design, run}`, and (where applicable) `ReferencePlane` and `validationMode`, and **SHALL NOT** merge design- and run-time assurance into one score.                 | Prevents design/run chimera and makes interpretation auditable.              |
| **CC‑C.2.2‑10 (Parallel requires independence).** | Authors **SHALL** treat `max`-composition of support paths as admissible **only** when an explicit independence justification is recorded; otherwise supports are treated as one entangled line and remain weakest-link. | Prevents confidence inflation by double-counting correlated evidence.         |

### C.2.2:8 - Common Anti-Patterns and How to Avoid Them

Informative; non-binding.

| Anti-pattern               | Symptom                                                                                       | Why it fails                                                     | How to avoid / repair                                                                                    |
| -------------------------- | --------------------------------------------------------------------------------------------- | ---------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- |
| **Averaging assurance**    | A mean/weighted sum of `R` values is reported as “confidence”.                               | It violates WLNK and is usually illegal scale arithmetic.        | Use weakest-link `min` on the entailment spine, then apply congruence penalties into `R` only.          |
| **Truth-by-score**         | `R=0.9` is treated as “the claim is true.”                                                    | R is warrant strength, not ontological truth.                    | Require explicit evidence links and scope; treat R as decision warrant only.                             |
| **Scope laundering**       | The claim’s applicability grows by wording changes while `G` is unchanged.                    | It silently widens scope, making comparisons meaningless.        | Use A.2.6 operators and treat scope changes as explicit revisions.                                       |
| **Bridge laundering**      | A claim is reused in a new context without a bridge, and R is carried over unchanged.         | It hides semantic loss and encourages overconfident reuse.       | Declare bridges with CL and recompute `R_eff` using penalties.                                           |
| **Design/run chimera**     | Design-time proofs and run-time telemetry are mixed as if they were the same evidence object. | Evidence belongs to different stances and decays differently.    | Separate lanes and validity windows; treat crossings explicitly.                                         |
| **Ordinal arithmetic**     | CL or F levels are averaged to produce a pseudo-score.                                        | It violates scale legality and produces non-auditable numbers.   | Keep CL/F ordinal; convert only via declared penalty tables on R.                                        |
| **Many-weak-makes-strong** | Numerous low-quality supports are combined to inflate confidence.                             | It violates the weakest-link intent of conservative propagation. | Default to `min` for required supports; allow `max` only with explicit independence arguments.          |

### C.2.2:9 - Consequences

Informative; non-binding.

| Benefits                                                                                                     | Trade-offs and mitigations                                                                                                                         |
| ------------------------------------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Comparability.** Different claims can be compared in a disciplined way when F and G are explicit.          | **Conservatism.** Weakest-link propagation can feel pessimistic; mitigate by making support structure explicit and improving the weakest evidence. |
| **Auditability.** Transport loss is visible and localised to R.                                              | **Overhead.** Declaring bridges and evidence links is work; mitigate with templates and reuse of standard lane schemas.                            |
| **Upgradeable knowledge.** R can improve incrementally as evidence accumulates, without rewriting the claim. | **Scalar temptation.** People still want one number; mitigate by requiring lane breakdown visibility behind the number.                            |

### C.2.2:10 - Rationale

A triad only works if each coordinate has a single job.

* **G carries entitlement.** It states where the claim is asserted to apply. If G is implicit, teams argue about “what was meant” instead of updating scope.
* **F carries checkability.** It states how much the claim’s form supports mechanised scrutiny and reuse. If F is conflated with R, formalisation becomes a rhetorical weapon.
* **R carries warrant.** It states how much evidence supports relying on the claim under G. If R is not conservative, weak supports can be laundered into strong confidence.

Routing congruence loss into **R only** prevents a subtle but pervasive failure mode: transport across contexts/kinds/planes does not silently rewrite the claim; it only reduces how confidently we should carry it.

Weakest-link propagation is chosen because it is the simplest rule that is monotone, conservative, and auditable. When better combination rules exist, they can be introduced as explicit Γ‑policies, but the default must be safe.

### C.2.2:11 - SoTA-Echoing

Normative.

**SoTA pack binding note.** If a SoTA Synthesis Pack exists for KD‑CAL reliability / cross‑context warrant transport in your Context (G.2), cite its ClaimSheet IDs / CorpusLedger entries / BridgeMatrix rows here. Otherwise, record `SoTA-Pack: TBD/none` and treat this section as the seed (do not fork it silently elsewhere).

| Practice claim                                                                                                      | Post‑2015 source anchor                                                                   | Alignment to this pattern                                                                                                                                                           | Adoption status                                                                                                      |
| ------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- |
| Verification and validation should be distinguished and tied to evidence quality, not to rhetoric.                  | ASME V&V 40‑2018 (model credibility assessment).                                          | This pattern separates VA and LA lanes and binds `R_eff` to evidence and declared scope rather than to narrative confidence.                                                        | **Adopt**, with KD‑CAL’s conservative fold as an explicit default.                                                   |
| Trustworthiness is context- and risk-dependent and requires explicit documentation of limits.                       | NIST AI Risk Management Framework 1.0 (2023).                                             | This pattern makes limits first-class via `G` and makes reuse loss explicit via CL penalties rather than informal caveats.                                                          | **Adapt**, because FPF treats transport loss as an epistemic penalty, not as a purely organisational risk statement. |
| Safety arguments should make claims, evidence, and assumptions explicit and reviewable.                             | UL 4600 (2020) and related assurance-case practice in autonomous systems.                 | This pattern treats `R` as an auditable warrant signal whose inputs are explicit evidence items and whose reuse requires explicit transport justification.                          | **Adopt**, while remaining notation-independent and avoiding tool mandates.                                          |
| Empirical results should be accompanied by structured provenance and usage conditions to enable reuse and critique. | “Datasheets for Datasets” (Gebru et al., 2018) and “Model Cards” (Mitchell et al., 2019). | This pattern’s scope discipline and lane reporting make empirical warrant portable only when its conditions are explicit; cross‑Context reuse is Bridge-only (e.g., `Bridge#MatLab_to_PlantB`, `CL=2`, `Φ=Φ_v1`), and congruence loss routes to `R_eff` only. | **Adopt**, with congruence penalties as the reuse control mechanism.                                                 |
| Reproducibility requires packaging evidence and making it re-checkable by others.                                   | ACM Artifact Review and Badging (updated practices post‑2015) and The Turing Way (2019).  | This pattern treats evidence as something that can be inspected across TA/VA/LA lanes and allows reliability to decay when evidence becomes stale or non-replayable.                | **Adapt**, because FPF treats decay and transport penalties as first-class calculus elements.                        |
| Strong inference benefits from “severe tests” rather than from accumulation of weak confirmations.                  | Mayo (2018) on severity in statistical inference.                                         | Weakest-link propagation and explicit scope declarations discourage superficial confirmation piling and encourage explicit, discriminating evidence.                                | **Adapt**, because KD‑CAL is agnostic to frequentist vs Bayesian inference but requires auditability.                |

### C.2.2:12 - Relations

**Builds on:** C.2 (KD‑CAL overview), A.2.6 (Claim scope and operators), C.2.3 (Formality F), B.3 (Trust & Assurance calculus), B.1.3 (Γ‑fold patterns), B.3.3 (assurance lanes), B.3.4 (refresh/decay), C.3 (Kind‑CAL and kind bridges), F.9 (Bridges & CL), G.6 (EvidenceGraph PathId discipline), G.7 (Bridge calibration / admissibility thresholds).
**Coordinates with:** C.16 (MM‑CHR evidence discipline), E.14 (working-model assertions), E.18/A.27 (crossing surfaces), C.25 (Q‑Bundle, for avoiding confusion between epistemic reliability and system reliability).
**Used by:** C.3.3 (cross-kind reuse discipline), guard macro bundles in C.3.A and C.21, and any acceptance/gating logic that consumes `R_eff` while preserving `F` and `G`.
**Clarifies:** The KD‑CAL meaning of reliability implicit in C.2:4.1 and the transport clauses referenced across B.3 and C.3.

### C.2.2:End


## C.2.3 - Unified Formality Characteristic F

> **One‑line summary.** Defines **Formality (F)** as a single, ordinal **Characteristic** (`U.Formality`) with **polarity “up”**, anchored by a **default ladder F0…F9** from **free prose** to **proof‑grade foundations**. This unifies how rigor is declared and compared across all epistemes and contexts, and supplies the **F‑coordinate** in the F–G–R assurance space.

**Status.** Normative pattern in **KD‑CAL / Part C.2**. It **replaces** the legacy “modes/tiers” language and any parallel “formality ladders.” The letter **F** hereafter denotes the **Formality** characteristic in the **F–G–R** triple.

**Scope.** Conceptual only. The pattern **does not** prescribe workflows, toolchains, or team procedures. It specifies *what Formality is and how to measure/declare it*, so that any team can think and communicate rigor with the same yardstick.

**Non‑goals.**
– Not a publication process, not a governance gate.
– Not a reliability metric (R) and not a scope/abstraction metric (G).
– Not tied to any notation, repository layout, or CI/CD practice.


### C.2.3:1 - Context

Transdisciplinary work (physics, software, systems, policy, data) needs a **shared notion of rigor** that travels across context of meaning. A controller invariant stated in a theorem prover, a research hypothesis framed in constrained English, and a managerial decision rule written as acceptance criteria must be **comparable**—not by their domain lore, but by **how strictly they are expressed**.

Historically, FPF texts carried **multiple signals of rigor** (narrative “modes,” editorial tiers, ad‑hoc “formal vs. informal” talk). These signals mixed with status labels (e.g., “Draft/Effective”), obscuring whether an “approved” artifact was **actually precise** or merely **organizationally accepted**. To reason soundly in KD‑CAL and to compose artifacts safely, we standardize a **single Formality characteristic F**:

* **Portable:** works for math, code, models, requirements, policies.
* **Ordinal & minimal:** few clear anchors from “sketch” to “foundations.”
* **Composable:** participates in the F–G–R calculus and weak‑link invariants.
* **Context‑extensible:** Contexts may introduce **intermediate anchors** without breaking comparability.


### C.2.3:2 - Problem

Absent a unified **F**:

1. **Rigor whiplash.** Either everything is forced into premature formalism (blocking exploration), or informal artifacts drift into high‑assurance use (creating silent risks).
2. **Incomparability.** Each Context’s labels mean different things. Reviewers, integrators, and auditors cannot align expectations or compute trustworthy composites.
3. **Lost continuity.** Moving from sketch to proof often becomes a **rewrite**, severing provenance; the same idea looks like different artifacts at each “mode,” inviting translation errors.
4. **Confused roles.** Status (e.g., “accepted here”) gets conflated with rigor (“precise enough”), undermining governance and the KD‑CAL trust math.


### C.2.3:3 - Forces

| Force                                             | Tension to resolve                                                                                                                             |
| ------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------- |
| **Human ↔ Formal system**                         | Natural language is fast and legible; formal systems are unambiguous and checkable. We need a spectrum, not a cliff.                           |
| **Local freedom ↔ Global comparability**          | Contexts must be free to set thresholds; cross‑context reasoning requires a shared scale and anchors.                                          |
| **Readability ↔ Precision**                       | Rich narrative aids understanding; tight syntax prevents misinterpretation. The characteristic must not force one at the expense of the other. |
| **Open‑world thinking ↔ Closed‑world guarantees** | Exploration benefits from openness; certification needs explicit closure. F must support gradual “closing” without renaming the artifact.      |


### C.2.3:4 - Solution — The **Formality Characteristic F**

#### C.2.3:4.1 - Identity and Type (MM‑CHR)

* **Name:** `U.Formality` (nicknamed **F** in F–G–R).
* **Type:** `U.Characteristic`.
* **Scale:** **ordinal** (no arithmetic; comparisons and thresholds only).
* **Polarity:** **up** (higher ⇒ more strictly and unambiguously expressed).
* **Unit:** **formality step** (qualitative anchor).
* **Value domain:** default anchors **F0…F9** (see §4.4).
* **Carrier:** any `U.Episteme` (claim/theory/spec/model/policy/etc.).
* **Notation‑agnostic:** the same F semantics apply regardless of symbol system; bridges between notations do **not** change F (they may affect R via CL, see C.2.2).

**Normative reading.** “F = k” states *how strictly the content is expressed*, not whether it is true (R) nor how broadly it applies (G).


#### C.2.3:4.2 - Relationship to KD‑CAL (F–G–R)

* **F in the triple.** F is the **Formality coordinate** in the F–G–R assurance space. It influences trust **indirectly**: higher F reduces ambiguity, enabling stronger evidence and safer composition, but **does not** substitute for evidence (R) or scope (G).
* **Composition invariant (weakest‑link).** For any composite episteme,
  **F\_composite = min(F\_parts on support paths)**.
  *Rationale:* the formal rigor of a whole cannot exceed its least‑formal essential part.
* **Orthogonality.** Changing **G** (envelope/scope) or **R** (evidence) does not, by itself, change **F**; conversely, raising **F** does not imply broader G or higher R.


#### C.2.3:4.3 - Extensibility and Local Anchors

FPF provides **default anchors F0…F9** (next subsection). **Contexts MAY**:

* introduce **intermediate anchors** (e.g., F6.5) or **named sub‑anchors** (e.g., “F4‑OCL” vs “F4‑TLA‑constraints”),
* publish **domain exemplars** for anchors,
* define **thresholds** (e.g., “claims of type X must be F≥7”).

**Constraints (normative):**

* **Monotonic order is preserved.** New anchors **MUST NOT** invert or blur the ordering.
* **Anchor meaning is conserved.** Local elaborations **SHALL** map to the nearest global anchor without shifting global semantics (e.g., anything called “F8.x” remains **proof‑grade**).
* **No proxy scales.** Do **not** invent alternative “formality modes/tiers” as surrogates; use **F** explicitly.


#### C.2.3:4.4 - Default **F0…F9** Anchors (overview)

> *Full anchor definitions with cross‑disciplinary examples appear in §5 (next part). Below is the overview for orientation.*

* **F0 — Unstructured prose.** Free narrative; ambiguous; human interpretation only.
* **F1 — Scoped notes.** Informal but term‑consistent scope; clearer than F0.
* **F2 — Structured outline.** Template present; coherent sections; criteria mostly “TBD”.
* **F3 — Controlled narrative.** Complete template; constraints sketched in constrained NL or pseudo‑formal phrasing.
* **F4 — First‑order constraints.** Explicit invariants/properties expressible at ≈FOL level (checkable conditions exist).
* **F5 — Executable math/algorithmics.** Precisely defined computational semantics; outcomes checkable by execution/simulation.
* **F6 — Hybrid formalism.** Mixed discrete/continuous methods; model‑checking or equivalent obligations identified.
* **F7 — Higher‑order verified.** Core claims encoded and checked in HOL‑style systems.
* **F8 — Dependent/constructive proofs.** Proof‑carrying content (programs‑as‑proofs).
* **F9 — Univalent/higher foundations.** Equality‑as‑structure; frontier‑grade formal foundations.

**Intent of anchors.** They form a **gentle gradient** from “thinker‑friendly” (F0–F3) through “formalizable” (F4–F6) to **proof‑grade** (F7–F9), allowing the **same artifact** to climb without renaming or forking.


#### C.2.3:4.5 - Usage Obligations (declaration, not governance)

* **Declare F.** Every normative episteme **SHALL** declare its **F** (one value) in its context. There is **no default**.
* **Use F in reasoning.** Any comparison, composition, or alignment that depends on rigor **SHOULD** reference **F** explicitly rather than implicit labels like “draft/final.”
* **Do not conflate F with status.** Status systems (ESG/RSG) may **refer** to F in their guards, but **F ≠ status**. This pattern defines **what** rigor is, not **when** a Context should require it.


### C.2.3:5 - Canonical Anchors **F0…F9** (normative)

> **How to read this section.** Each anchor defines *what is minimally true* of an episteme to be rated at that level — across disciplines. The anchors are **ordinal**: F7 is strictly more formal than F6, etc. Levels are **about expression**, not truth; Reliability (R) and ClaimScope (G) are separate.

For every anchor we state **Definition**, **Inclusion criteria**, **Non‑examples** (to prevent over‑rating), and **Indicative artifacts** (cross‑disciplinary, post‑2015).


#### C.2.3:5.1 - **F0 — Unstructured Prose**

**Definition.** Free natural language; ambiguous; unstated assumptions; no required sections; meaning depends on reader context.
**Inclusion criteria.** Narrative exists but lacks stable structure; terms may shift meaning; no explicit acceptance/denial conditions.
**Non‑examples.** Any document with a consistent outline and stable vocabulary is at least F1.
**Indicative artifacts.** Whiteboard photos; impromptu email threads; notes from a hallway discussion; an ad‑hoc wiki page with mixed jargon.


#### C.2.3:5.2 - **F1 — Scoped Notes**

**Definition.** Informal narrative with a **consistent scope** and **stable terms**; some headings; the central claim/problem is bounded.
**Inclusion criteria.** Key terms are used consistently; scope is named (e.g., “for single‑node scheduling”); still no explicit criteria.
**Non‑examples.** If each requirement already names a check or scenario, that is F2+.
**Indicative artifacts.** A design note that consistently uses the same nouns/verbs and states “this applies to v2 of the service”; a lab memo defining a focus population.


#### C.2.3:5.3 - **F2 — Structured Outline**

**Definition.** A **complete template** (Context/Problem/Forces/Solution/…) is populated; content is coherent end‑to‑end; criteria are mostly placeholders.
**Inclusion criteria.** All expected sections exist; cross‑references are consistent; open items are marked (e.g., “TBD acceptance”).
**Non‑examples.** If acceptance criteria are explicit per claim, that is F3+.
**Indicative artifacts.** A draft pattern/spec with fully populated sections but qualitative language; an experiment plan with all slots filled yet non‑operational metrics.


#### C.2.3:5.4 - **F3 — Controlled Narrative**

**Definition.** Narrative remains human‑readable but uses **constrained phrasing**; each claim has a **clear, singular interpretation**.
**Inclusion criteria.** Use of controlled NL or disciplined templates (e.g., “shall/if/then”); per‑claim **acceptance statements** exist in prose.
**Non‑examples.** If properties are encoded as logical constraints or typeable Standards, that is F4+.
**Indicative artifacts.** Requirements written in Attempto‑style controlled English; decision rules with explicit pre‑/post‑conditions phrased in a fixed schema.


#### C.2.3:5.5 - **F4 — First‑Order Constraints**

**Definition.** Key claims are expressible at **≈ first‑order logic** (FOL) granularity; invariants/constraints are **explicit and checkable in principle**.
**Inclusion criteria.** Each critical statement can be rendered as a predicate over well‑typed variables; conflict/consistency checks are conceivable.
**Non‑examples.** Bare unit tests or executable code without stated invariants is not automatically F4.
**Indicative artifacts.** TLA+ or OCL constraints on a model; an API spec where pre/postconditions and invariants are written as logic‑like rules; well‑typed schema constraints with quantification over entities.


#### C.2.3:5.6 - **F5 — Executable Math / Algorithmics**

**Definition.** Content has **precise execution semantics**; results can be checked by **running** (simulation or computation).
**Inclusion criteria.** A model is encoded so that outcomes are deterministic (modulo declared randomness); simulations/tests demonstrate the claims’ executable shape.
**Non‑examples.** “It runs” without a statement of what is guaranteed is not enough; opaque notebooks with side effects but no declared semantics stay F3–F4.
**Indicative artifacts.** Differential‑equation models in code; a reference implementation with clear Standard comments linked to tests; an ML training recipe where the algorithmic pipeline and metrics are fully explicit (yet not proven).


#### C.2.3:5.7 - **F6 — Hybrid Formalism**

**Definition.** Combination of **discrete and continuous** reasoning or multiple formal layers; **model‑checking obligations** or equivalent are identified and traceable.
**Inclusion criteria.** Hybrid claims (e.g., controller + plant) are spelled out with both sides’ formalisms and the glue; property checks are specified.
**Non‑examples.** A prose description of cyber‑physical behavior without model obligations is ≤F5.
**Indicative artifacts.** Safety envelopes for autonomous motion expressed as state‑space invariants plus controller logic; hybrid automata with stated safety properties; Standards linking simulation to discrete decisions.


#### C.2.3:5.8 - **F7 — Higher‑Order Verified**

**Definition.** Core claims are encoded in a **higher‑order logic (HOL)** or equivalent, and **machine‑checked**; proof scripts or structured proofs exist.
**Inclusion criteria.** The kernel/tool verifies each inference step; failing changes break proofs.
**Non‑examples.** A hand proof attached to F4 constraints without machine checking remains F4–F5.
**Indicative artifacts.** A theorem in Isabelle/HOL or HOL‑Light proving a protocol invariant; a verified algebraic property of a cryptographic scheme.


#### C.2.3:5.9 - **F8 — Dependent / Constructive Proofs**

**Definition.** **Programs‑as‑proofs** (Curry–Howard) or **dependent type** artifacts; proof terms are part of the artifact; compilation/type‑check is verification.
**Inclusion criteria.** Types capture the property; changing the property changes the type and breaks the build.
**Non‑examples.** A typed program whose types do not encode the critical property is ≤F5.
**Indicative artifacts.** A Coq/Lean implementation whose type encodes sortedness/safety; a certified compiler pass with proof objects maintained by the build.


#### C.2.3:5.10 - **F9 — Univalent / Higher Foundations**

**Definition.** Frontier‑grade **higher foundations** (e.g., homotopy type theory / univalence); equality is treated as **structure**; proofs live at that level.
**Inclusion criteria.** Equivalences are recognized as identities by construction; properties rely on higher equalities.
**Non‑examples.** Any proof that does not hinge on higher‑dimensional equality is ≤F8.
**Indicative artifacts.** Formal developments where isomorphic structures are path‑equal by univalence; higher‑inductive types used to encode core invariants.


#### C.2.3:5.11 - Cross‑anchor cautions (normative)

* **Execution ≠ Proof.** Running code/examples (F5) is not a proof (F7+) unless proof obligations are explicitly encoded and checked.
* **Schema ≠ Semantics.** Parseable schemas (F2) are not logical constraints (F4) without semantic predicates.
* **Labels ≠ Levels.** “Approved,” “Final,” or “Published” are **status labels** and have no bearing on F unless they explicitly bind to these anchors.


### C.2.3:6 - Assigning **F** in Practice (guidance)

This section is **informative**. It offers practical heuristics so engineers‑managers can triage artifacts quickly and consistently.

#### C.2.3:6.1 - Three questions to place a first guess

1. **Can a competent reader misread the claim?**
   If yes, you are likely ≤F2. If no (unique reading by construction), you are ≥F3.
2. **Are constraints stated as predicates over typed things?**
   If yes, you are around **F4**; if they are only executable tests without predicates, you’re **F5**.
3. **Would a tool *reject* an incorrect change?**
   If “only by rerunning examples,” that’s **F5**; if “because the logic kernel/type checker refuses it,” that’s **F7–F8**.

#### C.2.3:6.2 - Decision steps (quick rubric)

* **Has complete template?** If not, **F0–F1**. If yes →
* **Are per‑claim acceptances written (even informal)?** If not, **F2**. If yes →
* **Are they predicate‑like (quantifiers, implies, forall/exists)?** If yes, **F4**; if no, **F3**.
* **Is there an executable model with declared semantics?** If yes, **F5–F6** (hybrid if both discrete/continuous).
* **Are core properties machine‑proved?** If yes, **F7**; if types carry the property, **F8**; if higher equivalence is essential, **F9**.

#### C.2.3:6.3 - Litmus tests (do/don’t)

* **Do** point to the **lowest** rigor segment that is essential to the artifact; **F is capped by the weakest required part**.
* **Do** keep **F** independent from **R** and **G**: a well‑verified but informal hypothesis is **low F, high R**; a formal theorem without empirical content is **high F, R=N/A or VA‑lane only**.
* **Don’t** “average” levels: a long F8 appendix does not make an F3 body F8; F sticks to the **claim** or the **episteme**, not to page counts.
* **Don’t** upgrade F just because a tool was used; tooling matters only if the **content** reaches the anchor’s semantics.

#### C.2.3:6.4 - Anti‑patterns

* **Terminology inflation.** Calling acceptance criteria a “specification” without predicates → F3 at most.
* **Notebook mirage.** Treating an executable notebook with hidden state as formal proof → remains F5 without explicit obligations.
* **Schema worship.** Equating JSON Schema validity with logical safety → F2/F3, not F4.
* **Proof‑by‑CI.** “The pipeline is green” is not a logic kernel; without proofs or dependent types, F≤F6.

#### C.2.3:6.5 - Edge cases and how to rate them

* **Generated docs from formal sources.** Rate **by the source**, not the rendered prose. If the source is F7 proofs, the generated PDF remains **F7** as long as it is a faithful view.
* **Natural‑language with embedded formulas.** If formulas are illustrative only, keep **F3**; if they define obligations and are checkable, move **F4–F6** accordingly.
* **Standards in code comments.** If they constrain behavior and are enforced (e.g., via runtime/type checks), consider **F4–F5**; otherwise **F3**.
* **Hybrid ML systems.** The training procedure (executable) suggests **F5**; safety guards as formal constraints can raise parts to **F4/F6**; certified components may reach **F7/F8**.

#### C.2.3:6.6 - Raising **F** (ΔF moves, informative)

Typical **ΔF** steps (see KD‑CAL motion primitives):

* **F2→F3:** Introduce controlled phrasing; per‑claim acceptances.
* **F3→F4:** Recast acceptances as typed predicates/invariants.
* **F4→F5:** Provide executable semantics with declared Standards.
* **F5→F7:** Encode properties in a proof‑capable logic; prove core invariants.
* **F7→F8/9:** Migrate property into types / adopt higher‑equality foundations.

> **Note.** ΔF does not require changing **G** or **R**. Many projects raise F while holding scope and evidence constant, then tackle R (validation) separately.

### C.2.3:7 - Conformance (normative)

This section defines what it means to **use F correctly** in KD‑CAL. All “**SHALL**/**MUST**/**SHOULD**/**MAY**” statements here are normative.

#### C.2.3:7.1 - Declaration & Semantics

* **CC‑F‑1 (Declaration).** Every normative `U.Episteme` **SHALL** declare exactly one value for `U.Formality` (**F ∈ {F0…F9}**, or a context‑defined sub‑anchor that maps to one of these).
* **CC‑F‑2 (Ordinality).** F is an **ordinal Characteristic**: implementations **MUST NOT** perform arithmetic on F; only comparisons and thresholds are valid.
* **CC‑F‑3 (Polarity).** The polarity of F is **up**: a larger F value denotes **strictly greater or equal** expressive rigor than a smaller one.
* **CC‑F‑4 (No proxies).** Contexts **MUST NOT** introduce alternative “formality modes/tiers” as surrogates for F. If additional labels are desired, they **SHALL** be published as named **sub‑anchors** of F (see §4.3).

#### C.2.3:7.2 - Locality, Extensibility, and Anchors

* **CC‑F‑5 (Local extensibility).** A bounded context **MAY** introduce intermediate anchors (e.g., F6.5) and domain‑named anchors (e.g., “F4‑OCL”), **provided that** (a) the global F0…F9 order is preserved, and (b) each sub‑anchor is explicitly mapped to a parent anchor.
* **CC‑F‑6 (Anchor conservation).** Sub‑anchors **SHALL NOT** redefine the global meaning of their parent anchor (e.g., anything under F8 remains **proof‑grade**).

#### C.2.3:7.3 - Composition & Granularity

* **CC‑F‑7 (Weakest‑link fold).** For any composite episteme (theory, spec, model), the effective Formality **F\_composite** along any essential support path **SHALL** be computed as the **minimum** F of its essential parts on that path.
* **CC‑F‑8 (Granularity rule).** If different parts of an episteme carry different F values, the **episteme‑level F** is the **minimum** over all **essential** parts (non‑essential/illustrative parts are excluded).
* **CC‑F‑9 (No averaging).** Implementations **MUST NOT** average or otherwise combine F values numerically; the min rule suffices.

#### C.2.3:7.4 - Orthogonality & Non‑Interference

* **CC‑F‑10 (Orthogonality to G/R).** Changes in scope/envelope (G) or evidence (R) **SHALL NOT** alter F unless the **expression form** of the claims changes. Conversely, raising F **SHALL NOT** be interpreted as raising R or broadening G.
* **CC‑F‑11 (Notation‑agnostic).** Changing notations or carriers (Symbol side) **does not** change F if the claim graph and its formal content are preserved. Any translation loss is accounted for by **CL** penalties in R, not by altering F.

#### C.2.3:7.5 - Bridges & Cross‑Context Use

* **CC‑F‑12 (Bridges keep F stable).** When a claim is used across bounded contexts via a Bridge, the original F value **SHALL** be preserved in attribution. If the receiving context requires a different expression form, it **MUST** produce a **new episteme** (with its own F).
* **CC‑F‑13 (CL is for trust, not F).** Any mismatch across contexts **SHALL** be handled via Congruence Level (CL) and its effect on R; CL **MUST NOT** be used to down‑rate F.

#### C.2.3:7.6 - Traceability & Change

* **CC‑F‑14 (Observable basis).** An assigned F **SHALL** be justifiable by observable content (e.g., presence of predicates/invariants for F4; mechanized proofs for F7+).
* **CC‑F‑15 (ΔF disclosure).** A **ΔF** move (raising or, if justified by discovered error, lowering F) **SHALL** be recorded as a content change to the episteme. Whether a context versions that change is outside this pattern’s scope.


### C.2.3:8 - Composition & Interaction (normative + informative notes)

#### C.2.3:8.1 - Inside one episteme (normative)

* **Essential paths.** Identify essential parts/claims that are required for the episteme’s truth. Apply **min‑F** along each support path; the **episteme‑level F** is the min over essential paths (CC‑F‑7, CC‑F‑8).
* **Episteme‑about (ReferencePlane=episteme).** Descriptions about other claims/epistemes carry their **own** F and do **not** raise the target’s F; any cross‑plane penalty flows via **CL^plane → R**.

> **Note (informative).** A long formal appendix (F8) attached to a largely narrative body (F3) does **not** make the whole F8; the episteme remains **F3** unless the core claims move into the formal appendix.

#### C.2.3:8.2 - Relation to **G** (scope/envelope) (normative)

* F concerns the **expression form** of the claim; G concerns its **claim scope**. Tightening the envelope without changing how the claim is expressed does not change F; re‑expressing the claim in a stricter form (e.g., predicates) can raise F without changing G.

> **Caution (informative).** Raising F often **reveals** hidden assumptions, which may lead to a **ΔG** (narrower envelope). Treat this as a **separate** change: update G explicitly rather than smuggling scope changes under F.

#### C.2.3:8.3 - Relation to **R** (evidence/assurance) (normative)

* **F ≠ R.** Proof‑grade expression (F7+) still requires binding to appropriate assurance lanes (VA/LA/TA) in the trust calculus; empirical claims may have high R with low F if they remain informal.
* **Decay independence.** F **does not decay** with time; R may decay (empirical freshness) or shift due to CL. Tool assurance (TA) is tracked independently of F.

> **Note (informative).** Higher F typically **enables** stronger R (easier to test or prove), but no automatic relationship is assumed.

#### C.2.3:8.4 - CL & Bridges (normative)

* **CL effects.** Using content across context boundaries requires a Bridge with a CL rating. CL affects **R** (penalties) and **never** changes **F** (CC‑F‑12/13).
* **Semantic change ⇒ new episteme.** If a cross‑context mapping **alters** the claim (e.g., coarsens predicates, drops obligations), treat it as a **new episteme** with its own F rather than “the same F with lower CL.”

#### C.2.3:8.5 - Motion primitives (informative)

* **ΔF** raises or (rarely) lowers the rigor of expression. Plan ΔF moves independently of **ΔG**/**ΔR**: projects often alternate “raise F” (make the claim checkable) with “raise R” (gather proof/validation) at a fixed G.
* **Cost signals.** Typical costs: authoring overhead (F3→F4), model encoding (F4→F5/6), proof engineering (F6→F7/8). The benefit is reduced ambiguity and safer composition.

#### C.2.3:8.6 - Gaps & thresholds (informative)

* **F‑gap** = ordinal difference between two F anchors (no arithmetic). Large gaps signal translation risk: an F8‑level component will not accept informal inputs (F2) except via additional formalization (ΔF) or robust alignment (CL‑guarded).


### C.2.3:9 - Worked Examples (informative)

> Each mini‑case states the artifact, assigns **F**, and notes interactions with **G/R**. Examples are deliberately cross‑disciplinary to stress transdisciplinary comparability.

#### C.2.3:9.1 - Research hypothesis (physics)

**Artifact.** Short note proposing a new scaling law; clear vocabulary; scope “low‑Reynolds flows in microchannels.”
**F.** **F3** (controlled narrative with per‑claim acceptance in prose).
**G/R.** G is a narrow physical envelope; R is initially low (hypothesis).
**Next ΔF.** Recast acceptance as predicates over variables → **F4**; encode a simple simulation harness → **F5**.

#### C.2.3:9.2 - API specification (software)

**Artifact.** REST API doc with request/response schemas and explicit pre/postconditions; invariants like “idempotent under retry.”
**F.** **F4** (first‑order constraints).
**G/R.** G = stated resource model; R improves via conformance tests (independent).
**Next ΔF.** Reference implementation and executable test suite with declared Standards → **F5**; model‑check idempotence under failure injection → **F6**.

#### C.2.3:9.3 - Safety controller (cyber‑physical)

**Artifact.** Controller with plant model; safety distance invariant and braking envelope defined and verified in a hybrid model checker.
**F.** **F6** (hybrid formalism with obligations checked).
**G/R.** G = operating envelope (speed ranges, road conditions); R increases via track tests and simulation coverage.
**Next ΔF.** Encode key invariants in HOL and prove monotonicity → **F7**; migrate safety property into dependent types in the control kernel → **F8**.

#### C.2.3:9.4 - Decision policy (management)

**Artifact.** Escalation policy: if risk score ≥ θ and budget slack ≤ β, escalate to committee; otherwise defer.
**F.** **F3→F4** depending on phrasing. If the thresholds and variables are typed and the rule is predicate‑like, rate **F4**.
**G/R.** G = organizational scope (which portfolios, time windows); R entails retrospective calibration (did escalations match outcomes?).

#### C.2.3:9.5 - Verified algorithm (theory/software)

**Artifact.** Sorting function implemented with a dependent type ensuring output is ordered and a permutation of input; proof included.
**F.** **F8** (dependent/constructive proof).
**G/R.** G = data types and preconditions; R (empirical) is irrelevant; VA lane suffices (proof stands).

#### C.2.3:9.6 - ML classifier (data/ML)

**Artifact.** Training pipeline fully specified; metrics defined; OOD detection configured; no formal invariants.
**F.** **F5** (executable algorithmic semantics).
**G/R.** G = data distributions and deployment envelope; R grows with validation/monitoring.
**Next ΔF.** Add formal constraints for safety (e.g., monotonicity in features) → **F4/F6** for those aspects; certified post‑processing may achieve **F7** for a slice.

#### C.2.3:9.7 - Meta‑specification (method description)

**Artifact.** A guideline on how to review specs; it includes checklists and litmus tests.
**F.** **F3–F4** depending on whether checks are predicates.
**Interaction.** Its F does **not** lift the F of the reviewed artifacts; it only affects **R** via better CL (clearer alignments and fewer losses).

### C.2.3:10 - Authoring & Review Guidance (informative)

This section helps engineering managers, architects, and researchers **assign F consistently**, plan **ΔF moves**, and **review** claims without slipping into status/process language.

#### C.2.3:10.1 - For authors — placing and raising **F**

* **Start honest.** If you’re drafting ideas in plain prose, declare **F0–F1**. You are not “behind”; you’re **appropriately early**.
* **Stabilize vocabulary first.** Move to **F2–F3** by making terms stable and acceptance statements unambiguous (controlled phrasing).
* **Name predicates next.** When acceptance can be written as **typed predicates** (“for all …, if … then …”), you have reached **F4**.
* **Give semantics to execution.** When readers can **run** a model/algorithm with *declared* semantics and see outcomes aligned with the predicates, you are in **F5** (hybrid + obligations → **F6**).
* **Prove what matters.** When the **logic kernel/type system** will **reject** incorrect changes to core claims, you are at **F7–F8**; if equality as structure is essential, **F9**.
* **Keep identity.** Prefer **ΔF** on the *same* episteme (raising rigor stepwise) over creating new documents; this keeps provenance and reduces translation error.

**Typical ΔF plan:** *Sketch (F1) → Controlled narrative (F3) → Predicates (F4) → Executable semantics (F5/6) → Machine‑checked core (F7/8).* Scope (G) and evidence (R) can remain fixed while F rises.

#### C.2.3:10.2 - For reviewers — verifying the declared **F**

Use **observable checks**:

* **F2?** Template is complete; terms don’t drift; “TBD” acceptance is explicitly marked.
* **F3?** Every claim has a **single reading** via constrained phrasing; hidden ambiguity is flagged.
* **F4?** Each critical claim is **predicate‑like** (typed variables, quantifiers/implication allowed); conflicts are **checkable in principle**.
* **F5?** Executable **semantics are declared**; runs/tests are not ad‑hoc but trace back to claims.
* **F6?** Hybrid obligations are **identified and linked** (discrete + continuous, or layered formalisms).
* **F7/8?** Incorrect edits to core claims are **rejected by the kernel/type system**; proof/scripts or proof‑objects exist and are traceable.
* **F9?** Higher equalities are **first‑class** (e.g., univalence), and core results rely on them.

**Failure modes to watch:** “green CI” as proof; schema validation treated as semantics; notebooks without declared semantics; long formal appendix while the main claim stays informal (rate by the **weakest essential part**).

#### C.2.3:10.3 - For integrators & architects — using **F** in composition

* **Plan around the minimum.** In any composition, **F\_composite = min F\_parts** along essential paths. Identify the **bottleneck F** first; your ΔF effort goes there.
* **Mind the F‑gaps.** Large ordinal gaps (e.g., F7 vs F2) imply translation risks and alignment costs. Either **raise** the low‑F part or insert **bridges** with explicit scope and confidence impacts (handled in **R** via **CL**).
* **Don’t upgrade by proximity.** An F8 component does not “elevate” an F3 neighbor. Keep F independent and visible.

#### C.2.3:10.4 - For assurance leads — relating **F** to **G/R** without conflation

* **F enables, R assures.** Raising **F** makes evidence easier to formulate and check; it does not **create** evidence. Rate R separately (calibration/validation/monitoring vs proof lanes).
* **G is separate.** Tightening **G** (scope/envelope) may accompany ΔF (as assumptions become explicit) — treat this as a **ΔG** move, not a side effect.
* **Use thresholds explicitly.** If a context expects “formalized before use,” write guard conditions as **`F ≥ k`**, not as status labels.

#### C.2.3:10.5 - Common pitfalls & remedies

| Pitfall                                   | Remedy                                                                                          |
| ----------------------------------------- | ----------------------------------------------------------------------------------------------- |
| Calling structured prose a “formal spec.” | If acceptance isn’t predicate‑like, rate **≤F3** and plan **ΔF: prose → predicates (F4)**.      |
| Treating runnable code as proof.          | Declare **F5**; add **stated obligations** and property checks to progress **F6–F7**.           |
| Averaging F across parts.                 | Use **min over essential parts**; if unsure which parts are essential, audit the support graph. |
| Letting status leak into F.               | Keep **status** (e.g., “accepted here”) separate; **F** is about expression only.               |


### C.2.3:11 - Glossary & Notation (normative where noted)

**Formality (F).** `U.Formality` — an **ordinal Characteristic** with polarity **up**; default anchors **F0…F9** (§5). *(Normative)*

**Anchor (F‑anchor).** A named qualitative milestone on the F scale (e.g., F4 “first‑order constraints”). Sub‑anchors are context‑local refinements that **preserve order**. *(Normative)*

**ΔF.** A change to the expression form that alters F (usually **up**). Record as an episteme content change. *(Normative)*

**Essential part/path.** A part or claim without which the episteme’s central assertion does not hold. Composition applies **min‑F** along essential support paths. *(Normative)*

**Predicate / Invariant.** A typed, checkable statement about objects/states; at **F4** and above, critical claims are expressed as such.

**Machine‑checked / Proof‑carrying.** Content for which a logic kernel/type system rejects incorrect changes (F7+) or where programs and proofs are the same artifact (F8).

**Higher equality / Univalence.** Treatment of equivalence as identity in higher foundations relevant at **F9**.

**Notation & examples.**

* Declare as `F = Fk` (e.g., `F = F4`).
* Sub‑anchor: `F = F4[OCL]` or `F = F7[HOL]`.
* Thresholds in prose: “requires **F ≥ F6** for core claims.”
* Mixed parts: list per part if useful (e.g., “Body F3; Appendix proofs F7 — **episteme F3**”).


### C.2.3:12 - Change Log & Patch Notes (normative migration)

**12.1 Supersession.**
This pattern **supersedes** the legacy “modes/tiers” language. Any references to “M‑mode/F‑mode”, “publication tiers”, or parallel “formality ladders” are **deprecated**. From now on, **Formality** is expressed **only** as **F** with default anchors **F0…F9** (and optional sub‑anchors per §4.3).

**12.2 Impacted cross‑references.**

* **C.2.2 (F–G–R).** Replace any generic “F‑ladder” description with a normative reference to **C.2.3** and treat **F** in the triple as defined here (including **min‑F** composition).
* **ESG/RSG text.** Where guards previously referenced “modes/tiers,” rewrite guards as **`F ≥ Fk`** conditions.
* **Meta‑descriptions.** Ensure meta‑artifacts carry **their own F** and do not “lift” a target artifact’s F; use **CL→R** for cross‑context penalties, not F changes.

**12.3 Transitional guidance.**

* **Legacy artifacts without F.** Assign an initial F by applying the rubric in **§6**; record the assignment as a content attribution (not as a status change).
* **Legacy labels in prose.** Replace them with explicit **F** declarations. If prose implies mixed rigor, rate by the **weakest essential** segment (see §7.3).
* **No dual systems.** Do not keep “modes” alongside F; remove proxies and speak **F directly**.

**12.4 Backward compatibility (non‑normative note).**
During editorial refresh, it is acceptable to annotate historical records with both the **new F** and the legacy note for provenance. Forward‑looking reasoning and composition, however, **SHALL** use **F only**.

**12.5 Versioning & edits.**
Raising or (exceptionally) lowering **F** constitutes a **content change** (ΔF). Whether such a change triggers a new edition in a given Context is **outside this pattern**; respect the Context’s edition policy while keeping **F** accurate.

### C.2.3:End

## C.3 - Kinds, Intent/Extent, and Typed Reasoning (Kind‑CAL)

> **One‑line summary.** Establishes **`U.Kind`** as the **minimal, context‑local intensional carrier** of “what a statement is about,” separates **intent** (KindSignature + its own **F**) from **extent** (*which* instances belong to the kind **in a given Context slice**), and situates **typed reasoning** alongside **USM Scope (G)** and **F–G–R** without conflation. Details of the core objects and operations live in **C.3.1–C.3.5**; guard shapes are standardized in **C.3.A**.

**Status.** Normative in **Part C**. Identifier **C.3**. This pattern lays the **architectural invariant** and manager‑level guidance. The **mechanics** are defined by its child patterns.

**Readers.** Engineering managers, architects, and assurance leads who must reason about *typed claims* across Contexts without mixing up **describedEntity** (Kinds), **applicability** (**G**), and **assurance** (**R**).

**Depends on.**
— **A.2.6 USM** (Context slices & Scopes): **`U.ClaimScope` = G**, **`U.WorkScope`**, ∈/∩/**SpanUnion**/translate, **Γ\_time** policy, Bridges + **CL** (scope).
— **C.2.2 F–G–R**: weakest‑link composition; penalties to **R** for Cross‑context congruence (CL).
— **C.2.3 Unified Formality F**: F0…F9 as an **ordinal Characteristic** (expression rigor).

**Sub‑patterns (normative unless noted).**
— **C.3.1** - `U.Kind` & `U.SubkindOf` (partial order).
— **C.3.2** - `KindSignature` (**intent**, with **F**) & `Extension/MemberOf` (**extent** in a slice).
— **C.3.3** - **KindBridge** & **`CL^k`** (type‑congruence; penalties route to **R**).
— **C.3.4** - **RoleMask** (context‑local adaptation without cloning kinds).
— **C.3.5** - **KindAT** (K0…K3, **informative facet**, not a Characteristic).
— **C.3.A** - **Typed Guard Macros** (annex): admit/compose, masks, Cross‑context reuse; AT is **forbidden** in guards.

**Deprecations.**
— “**Generality ladder**” for **G**; **G is Scope** only (set‑valued over `U.ContextSlice`).
— Any “**Kind scope**” characteristic (Kinds carry **intent/extent**, not Scope).
— **Mark as legacy** any uses of **‘validity’ as a Characteristic** or **‘operation’ as a Scope‑like Characteristic**; **redirect** to **`U.ClaimScope`** / **`U.WorkScope`** (A.2.6) for applicability. Editors SHOULD add glossary redirects in Part E.

**Editorial note (cut‑over).** Content formerly in C.3 that defined guard shapes, decision trees, and macro anti‑patterns now resides in **C.3.A**. Membership **evaluation obligations** live in **C.3.2** with `MemberOf`.


### C.3:1 - Purpose & Rationale

**What you get.**

1. A **neutral typed layer**: name *what* a claim quantifies over (**Kinds**) without binding to any particular “type technology” (OWL, PL types, shapes…).
2. A clean **split of characteristics**:
   – **Scope (G)** = *where* a claim holds (USM, set‑valued over **Context slices**).
   – **Kind extent** = *which instances* belong to a kind **inside** a given slice.
   – **F** = *how strictly* content is expressed (C.2.3).
   – **R** = *how well supported* (evidence & congruence penalties).
3. **Typed reuse across Contexts**: a dedicated **KindBridge** with **`CL^k`** (type‑congruence), so you can predict risk **without** touching F or G.
4. **Manager‑oriented maps**: when to invest in **formalization** (F), when to expand/narrow **Scope** (ΔG), when to test across **subkinds** (R), and what kind of **bridge** you should expect.

**Why it helps.**
Teams routinely overspend on proofs for **instance‑level** questions and underspecify scope for **class‑level** claims. By naming the **Kind**, you plan **ΔF/ΔR** correctly and keep **G honest**. Typed checks also block unsafe compositions (“we were talking about different things”).


### C.3:2 - Context

Cross‑disciplinary work mixes artifacts that *look like “types”* but behave differently: ontology classes, schema “shapes,” programming types, BORO super/sub categories, ad‑hoc labels. At the same time, **USM** made “scope” precise. What was missing was a *small, neutral* notion of **describedEntity** that (a) **does not** re‑invent a global “type system,” (b) composes with USM and F–G–R, and (c) lets Contexts keep their idioms—**with bridges** when crossing boundaries.


### C.3:3 - Problem

1. **Scope–type conflation.** Authors try to widen **G** by “abstracting the wording,” yielding claims that *sound* general but are only supported on a thin slice.
2. **Silent drift across Contexts.** A “vehicle” here is not the same as a “transport unit” there; reuse proceeds without a declared mapping or risk accounting.
3. **Wasteful planning.** Without a signal about the *kind‑level*, teams either over‑formalize single‑slice decisions or under‑test class‑level claims (no variant coverage along subkinds).
4. **Unsafe composition.** Claims about incompatible “things” get composed because the describedEntity was implicit in prose.


### C.3:4 - Forces

| Force                             | Tension to resolve                                                                                 |
| --------------------------------- | -------------------------------------------------------------------------------------------------- |
| **Local freedom vs global sense** | Contexts need their own vocabularies; Cross‑context work needs a common skeleton for **describedEntity**.      |
| **Minimality vs utility**         | The notion of kind must be tiny yet powerful enough to guide ΔF/ΔR/bridges/composition.            |
| **Intent vs extent**              | Kinds come with a **definition** and a **population in place**; both are needed and must not mix.  |
| **Typed discipline vs F–G–R**     | Typed safety must not distort **G** (Scope) nor introduce a parallel “assurance math.”             |
| **Abstraction vs applicability**  | “Higher abstraction” is **not** “wider applicability”; the framework must make this split obvious. |


### C.3:5 - Solution — Architectural Decisions (overview)

**C.3‑D1 — `U.Kind` is intensional and context‑local.**
Kinds name *what a claim quantifies over*. They form a partial order **`⊑`** (**SubkindOf**). *(See C.3.1.)*

**C.3‑D2 — Separate **intent** and **extent**.**
— **KindSignature(k)**: the intensional content (predicates/invariants/Standards). It carries its **own F** (C.2.3).
— **Extension(k, slice)**/**MemberOf**: which instances belong to `k` **in a given `U.ContextSlice`**. *(See C.3.2.)*

**C.3‑D3 — Kinds do **not** carry Scope.**
**Scope** lives with **claims/capabilities** (USM): a set of **Context slices** where the statement holds. Kinds carry **intent/extent** only. *(USM A.2.6 + C.3.2.)*

**C.3‑D4 — Typed reuse across Contexts is explicit.**
Use a **KindBridge** with **`CL^k`** (type‑congruence) and loss notes. Its effect is **only via R** penalties; **F/G remain unchanged**. *(See C.3.3.)*

**C.3‑D5 — Local adaptation without cloning.**
Use a **RoleMask** to bind a kind to Context‑specific constraints/aliases; promote to a **subkind** if the mask becomes stable and widely reused. *(See C.3.4.)*

**C.3‑D6 — An **informative** “abstraction tier” exists for Kinds (AT: K0…K3).**
A facet (not a Characteristic) that helps plan **ΔF/ΔR** and forecast bridge style; **AT never appears in guards**. *(See C.3.5.)*

**C.3‑D7 — Guard shapes are standardized and fail‑closed.**
Typed compatibility first (same‑Context **`⊑`** or **KindBridge**), then **Scope coverage** (USM), then **R** penalties and freshness. *(See C.3.A.)*

> **Manager’s picture — Two characteristics (keep them separate).**
> – **characteristic 1 (USM, G):** *Where* the claim holds → set of **Context slices**; composed by ∈ (membership) / ∩ (intersection) / **SpanUnion** (union across independent lines) / translate (scope mapping).
> – **characteristic 2 (Kind extent):** *Which instances* in a **given slice** belong to the kind → `MemberOf(e, k, slice)`.
> **Never “widen G” by abstract wording; widen only by ΔG with support.**


### C.3:6 - Core Concepts (informative summary; authoritative norms live in C.3.1–C.3.5)


> This section fixes the **Standard** of terms used in C.3 and points to the sub‑patterns for complete mechanics. All “**SHALL/MUST**” statements here are normative.

**Editorial note.** This section is **informative**. It restates manager‑level takeaways and **points to** the canonical, normative rules in **C.3.1–C.3.5**. Where this section summarizes a rule, treat the cited sub‑pattern (and rule ID) as the **source of truth**.


#### C.3:6.1 - `U.Kind` & `U.SubkindOf (⊑)`

**Definition.** `U.Kind` is a **context‑local intensional object** naming a “kind of thing” that claims may quantify over.
**Order.** `U.SubkindOf (⊑)` is a **partial order** (reflexive, transitive, antisymmetric). We write `k₁ ⊑ k₂`.

**Summary of norms** *(authoritative text: **C.3.1 K‑01–K‑02**)*.
— Contexts treat `⊑` as a partial order and document any computed meets/joins if they provide them.
— Kinds do not carry Scope; Scope remains on claims/capabilities (USM).

> *Full treatment:* **C.3.1** (definitions, invariants, examples).


#### C.3:6.2 - **KindSignature** (intent) & **F**

**Definition.** `KindSignature(k)` is the **intent**: predicates/invariants/Standards that define the kind in the Context. Its expression rigor has an explicit **`U.Formality`** (C.2.3).

**Summary of norms** *(authoritative text: **C.3.2 K‑03–K‑04**)*.
— `KindSignature(k)` declares its F (C.2.3). Claim‑level F does **not** auto‑inherit; weakest‑link applies on the claim’s own support paths.
— If a signature change alters membership, treat it as a content change (Contexts may version kinds).

> *Full treatment:* **C.3.2** (signature/intent with F; relation to claims).


#### C.3:6.3 - **Extension** & **MemberOf** (extent in a slice)

**Definition.** `Extension(k, slice) ⊆ EntitySet(slice)` = set of instances that belong to `k` **in the given `U.ContextSlice`**. `MemberOf(e, k, slice)` is the membership predicate: `e ∈ Extension(k, slice)`.

**Summary of norms** *(authoritative text: **C.3.2 K‑05–K‑08**)*.
— Membership is deterministic for a fixed `(k, slice)` (no hidden “latest”).
— If `k₁ ⊑ k₂`, then `Extension(k₁,slice) ⊆ Extension(k₂,slice)` for all slices.
— Definedness may be bounded; outside it, guards fail closed.
— Keep **Scope (G)** and **MemberOf** as distinct guard predicates.

> *Full treatment:* **C.3.2** (extent semantics, examples, authoring hints).


#### C.3:6.4 - **KindBridge** & **`CL^k`** (type‑congruence)

**Summary of norms** *(authoritative text: **C.3.3 KB‑01–KB‑12**)*.
— A KindBridge states Contexts/versions, kind mapping/rules, preserved order links, **`CL^k`** anchors, loss notes, and definedness.
— No inversions of preserved subkind links; collapses must be declared.
— When classification depends on a KindBridge, apply a monotone penalty **Ψ(`CL^k`)** to **R** (scope‑bridge **Φ(CL)** applies separately). **F** and **G** remain unchanged.
— Chaining uses weakest‑link on **`CL^k`**.

> *Full treatment:* **C.3.3** (bridge shape, anchors, examples).


#### C.3:6.5 - **RoleMask** (adaptation without cloning)

**Definition.** `U.RoleMask(kind, Context)` is a **named binding** that carries constraints (optional **narrowing** of membership), vocabulary/notation aliases, and intended use for local procedures—**without** creating a new Kind.

**Summary of norms** *(authoritative text: **C.3.4 RM‑01–RM‑08**)*.
— Masks are registered/versioned; constraints are observable/deterministic at guard time.
— Do not treat masks as kind synonyms; promote frequently reused constraint masks to explicit subkinds (`⊑`).


> *Full treatment:* **C.3.4** (mask taxonomy, guard discipline, promotion rule).


#### C.3:6.6 - **KindAT (K0…K3)** — *informative facet*

**Status.** A **facet** attached to `U.Kind`, not a Characteristic: no algebra, **never** used in guards or composition.

**Anchors (intentional view).**
**K0** Instance; **K1** Behavioral pattern; **K2** Formal kind/class; **K3** Up‑to‑Iso.

**Use.** Helps plan **ΔF/ΔR** and forecast bridge style (e.g., K3↔K3 suggests up‑to‑iso mapping). Do **not** conflate AT with **G** or **R**.

> *Full treatment:* **C.3.5** (manager heuristics, anti‑misuse).


#### C.3:6.7 - Quick examples (two‑characteristic awareness)

**E‑Sketch 1 — Policy over `Vehicle`.**
Claim: “For all `x ∈ Vehicle`: brakeDistance(x) ≤ 50 m (dry), ≤ 40 m (wet).”
– **describedEntity:** `Vehicle` (Kind, typically K2) — *what* we quantify over.
– **Scope (G):** `{surface∈{dry,wet}, speed≤50, rig=v3, Γ_time=rolling 180d}` — *where* the claim holds.
– **Extent in slice:** which instances the lab currently classifies as `Vehicle` (via `MemberOf`).
Typed checks happen **before** Scope intersection; **G** is not widened by “abstract wording.”

**E‑Sketch 2 — API rule over `AuthenticatedRequest`.**
Producer A emits `Request`; consumer B expects `AuthenticatedRequest`.
– If `Request ⊑ AuthenticatedRequest` **does not** hold, add an **adapter** or adopt a **subkind**; do **not** force fit by widening **G**.
– Scope remains independent (API version, Γ\_time policy); evidence/freshness sits in **R**.

### C.3:7 - How to use typed reasoning

### C.3:7.1 How typed reasoning plugs into **F–G–R & USM**

#### C.3:7.1.1 - The basic shape of a typed claim (manager view)

A typed claim has two independent parts:

1. **describedEntity (Kind).** *Which things the statement talks about.*
   “For every item of kind **k** in the **target context** (the selected **TargetSlice**) …”.
   — The **definition** of kind **k** lives in **KindSignature(k)** (with its **F**, C.3.2).
   — **Which items count as “k”** is evaluated in the **TargetSlice** (C.3.2) by a deterministic membership check.

2. **Applicability (Scope, G).** *Where the statement holds.*
   `U.ClaimScope(Claim)` is the **collection of contexts** where the claim is valid (USM A.2.6). Guards test: “Scope **covers** the TargetSlice”.

**Discipline.** The guard first checks **typed compatibility** (in the same Context: “is‑a / subkind‑of”; across Contexts: a **KindBridge**, C.3.3), then **Scope coverage** (USM), then **R** freshness and any bridge congruence penalties. See **C.3.A Guard\_TypedClaim**.


#### C.3:7.1.2 - Composition of typed claims

**Rule C‑T‑1 (typed pre‑check).** To compose a **producer claim** with a **consumer claim**, where the producer quantifies over kind **k (source)** and the consumer expects kind **k (expected)**:

* **same Context:** require **“is‑a / subkind‑of”** to hold (the source kind is a subkind of the expected kind) (C.3.1).
* **Cross‑context:** require a **KindBridge** that maps the source kind to a **local kind that is a subkind of the expected kind** in the target Context (C.3.3). If neither holds, the composition is **unsafe**; introduce a subkind, add an adapter (or a RoleMask), or decline.

* **Role‑aware option (same Context):** if the consumer expects a **RoleMask** over the expected kind, you may satisfy the mask’s explicit constraints (C.3.4) instead of changing kinds, provided those constraints are observable at gate time.

**Rule C‑T‑2 (scope after type).** After typed compatibility is satisfied, compute Scope as in USM:

* **Serial path:** take the **intersection** of the contributors’ claim scopes.
* **Parallel independent lines:** use **SpanUnion** of the serial scopes (only if independence is justified).

**Rule C‑T‑3 (no type‑by‑scope).** A kind mismatch **MUST NOT** be “fixed” by widening **G**. Changes in describedEntity require **subkind introduction**, **signature edits**, or a **KindBridge**—not a scope change.

**Manager hint.** First confirm the **port shape** matches (kinds line up), then check the **operating area** (scope), and finally look at **confidence** (evidence freshness plus any bridge congruence penalties).


#### C.3:7.1.3 - F–G–R with typed claims (what changes, what doesn’t)

* **F (Formality).**
  – **Claim‑level F** follows C.2.3 (weakest‑link along the claim’s support paths).
  – **KindSignature F** is declared **on the kind** (C.3.2) and influences claims **only** if the claim essentially depends on those predicates (weakest‑link again).
  – **Raising F** can *reveal* hidden assumptions (which may trigger ΔG in the claim), but **does not change G** by itself.

* **G (Scope).**
  – Always **set‑valued over Context slices** (USM A.2.6).
  – Typed reasoning does not alter G’s algebra (∈/∩/SpanUnion/translate).
  – Never infer Scope from “how general the wording sounds.”

* **R (Reliability).**
  – Evidence freshness/decay (validation windows) remains separate from Scope coverage.
  – **Cross‑context penalties** split cleanly: a **scope‑bridge penalty** (USM) and a **kind‑bridge penalty** (C.3.3). Both **reduce R only**; neither changes **F** or **G**.

**Manager rule of thumb.**
Start with the reliability from your support; then **apply the scope‑bridge penalty**; then **apply the kind‑bridge penalty**. Each step can only reduce reliability.  
You never add or average **F/G**: you **compose scope** per USM rules and apply **weakest‑link** for F/R along support paths.


#### C.3:7.1.4 - ESG gating with typed claims

* **Gate on F**, if your Context requires rigor before use (e.g., `U.Formality(Claim) ≥ F4`).
* **Gate on Scope coverage** (USM) and an explicit **time selector** (Γ_time) policy.
* **Gate on R freshness** and **minimum congruence** for bridges (e.g., `CL ≥ 2`, `CL^k ≥ 2`).
* **Do not** gate on **AT** (C.3.5); it is an informative facet only.
* Use **C.3.A guard macros** to keep guards short and auditable.

#### C.3:7.2 - How typed reasoning plugs into the CAL chain (Lang‑CHR → Role‑CAL)

> **Intent.** Show a clear, end‑to‑end path a manager can follow to take a typed claim from words to safe reuse across Contexts—without any tool or data‑governance assumptions. Each stage says **what it supplies**, **what it needs**, and **what it hands off** to the next stage.


##### C.3:7.2.1 - **Lang‑CHR** — stable words first

**What it supplies.** A disciplined vocabulary and controlled phrasing so that terms like *Vehicle*, *AuthenticatedRequest*, *AdultPatient* have **one meaning** in the Context.

**What it requires.** Authors use controlled narrative (C.2.3 **F3**) at minimum: single‑meaning terms, explicit “shall / if / then”, and no drifting synonyms.

**Hand‑off.** A small, curated lexicon entry for each candidate *Kind‑word*; these become **`U.Kind` names** in the next step.

> *Manager hint.* If two teams cannot agree on the noun, you are not ready to type the claim. Resolve the noun in Lang‑CHR before introducing a Kind.


##### C.3:7.2.2 - **Kind‑CAL** (this Part) — name the *describedEntity*

**What it supplies.**
• **`U.Kind`** objects for those nouns; a partial order **`⊑`** (subkind‑of).
• **KindSignature(k)** (intent), with declared **F**.
• **Extension(k, slice)** and **`MemberOf(e,k,slice)`** (extent).
• (Optional) **AT (K0…K3)** as an **informative facet**.

**What it requires.**
• Deterministic membership (no “latest” defaults) and a clear rule for where membership is defined in each context.
• No “Kind scope”: Scope remains with claims/capabilities (USM).

> *Manager hint.* Use the kind’s **AT tag** only as a planning signal (where to invest rigor and tests). AT never gates decisions and never widens scope.

**Hand‑off.** Typed quantifier sites for claims: “∀ x ∈ **Extension(k, slice)** …”, plus a visible **`⊑`** lattice for compatibility checks down the line. Typed claim sites written in Plain language: “for every item of kind **k** in the **target context** …”, plus a visible **subkind‑of** lattice for compatibility checks down the line.

> *Manager hint.* Decide early whether your Kind is K0 (instance‑ish) or K2 (formal class). It sets your **ΔF/ΔR** budget expectations.


##### C.3:7.2.3 - **Structure‑CAL** — give Kinds usable shape

**What it supplies.** Structural building blocks **on Kinds**:
• **combinations** (“and”),
• **alternatives** (“either/or”),
• **records** (named fields),
• **functions** (inputs to outputs),
plus relations like **has‑attribute** and **part‑kind**, and the minimal invariants those structures must respect.

**What it requires.**
• Do not hide Scope inside structure.
• Put structural rules into the **KindSignature** as checkable statements (ideally **F4+**).

**Hand‑off.** Typed *ports and shapes* of claims/specifications (“this policy expects `PassengerCar × ControllerConfig`”), making compatibility checks crisp before any Scope math.

> *Manager hint.* If two claims expect different shapes (for example, one needs “Vehicle with ABS”, the other just “Vehicle”), plan a **subkind** or an **adapter**. Do not “solve” it by rewording the claim.

**Note (informative).** If a Context declares structural constructors on kinds (e.g., product/sum/record/function), editors SHOULD document the corresponding **Extension** inclusion laws for those constructors. Keep Scope in USM; do not hide it in structure.


##### C.3:7.2.4 - **Compose‑CAL** — compose with typed pre‑checks

**What it supplies.** The **order of checks** you must follow for safe composition:

1. **Typed compatibility**: in the same Context, the producer’s kind **is a subkind of** the consumer’s kind; across Contexts, a **KindBridge** maps the producer’s kind to a local kind that fits, with an acceptable **kind‑bridge congruence level** (C.3.3).
2. **Scope checks** (USM): along dependency paths, take the **intersection** of scopes; use **SpanUnion** only when support lines are truly independent.
3. **Assurance wiring**: apply the **scope‑bridge penalty** and the **kind‑bridge penalty** to **R**; check evidence freshness separately.

**What it requires.** Independence justification for **SpanUnion**; no “type‑by‑scope” fixes.

**Hand‑off.** A typed, scope‑checked composition that survives audit because each risk is accounted for in **R**.

> *Manager hint.* Run the **typed pre‑check** first. It is the cheapest failure to catch and prevents “scope gymnastics” that mask a type mismatch.


##### C.3:7.2.5 - **CT2R‑LOG** — speak the logic, keep the math honest

**What it supplies.**
• A clear logical reading of your typed claim: “for every item of kind **K**, condition **φ** holds” (or “there exists an item …”).
• Rules for refinement and substitution that respect the **subkind‑of** relation.
• When appropriate (K3), reasoning that treats structures as **equivalent up to isomorphism** (useful where exact identity is the wrong notion).

**What it requires.**
• Pick a logic that matches the **Formality** you declare (e.g., machine‑checked logic for higher **F**).
• When the logic travels across Contexts, use a **KindBridge** to keep meaning aligned; any mismatch is reflected as a **kind‑bridge penalty** in **R**.

**Hand‑off.** Proof obligations or reasoning templates that are consistent with your Kind/Structure setup and do not alter **G**.  **Shall‑note CT2R‑1.** Transferring typed formulas that depend on `MemberOf` across Contexts **uses a KindBridge**; any mismatch is accounted as **Ψ(`CL^k`)** in **R**. **F** and **G** remain unchanged. For **up‑to‑iso** situations, see **C.3.5 (AT)** for when K3 is appropriate.

> *Manager hint.* If your proof keeps failing when you move between Contexts, add a **bridge at the Kind level**; do not try to “fix” it by changing scope.


##### C.3:7.2.6 - **Role‑CAL** — adapt without cloning

**What it supplies.** **RoleMask(kind, Context)**: a named, registered adaptation (extra constraints or local aliases, with optional narrowing) that reuses the **same** kind instead of creating a new one.

**What it requires.**
• Constraints must be testable at gate time and give deterministic answers.
• If a constraint mask is reused often, **promote it to a subkind**.

**Hand‑off.** Context‑specific views that keep identity intact and make typed guards practical (“use `PaymentAccount@PCI` mask in these steps”).

> *Manager hint.* If the same mask appears in several guards, **promote** it to a subkind. This reduces future bridge and audit effort.


##### C.3:7.2.7 - Mini end‑to‑end example (manager‑oriented)

> **Scenario.** A risk gate for API requests must be reused by another program across Contexts.

**Lang‑CHR.** Settle on *Request*, *AuthenticatedRequest*, *RiskScore*, *BudgetSlack*; write them in controlled phrases (F3).

**Kind‑CAL.**
• Define `Kind Request` (K2) and a **subkind** `AuthenticatedRequest ⊑ Request`;  publish a **KindBridge** for the PCI taxonomy with **kind‑bridge congruence level 2** (loss note: token class is collapsed).
• Membership `MemberOf(e, AuthenticatedRequest, slice)` is deterministic under API v2.3 and Γ\_time policy.

**Structure‑CAL.**
• `AuthenticatedRequest` is a **record kind** with fields (headers, tokenProof, body); invariants relate tokenProof to headers.

**Compose‑CAL.**
• Policy P says in Plain terms: “for every **AuthenticatedRequest** in the **target context**, deny the call when **riskScore** is at or above the set **risk threshold** and **budgetSlack** is at or below the set **budget limit**.”
• Another service S expects `PCIRequest`. Typed pre‑check: does `AuthenticatedRequest ⊑ PCIRequest`? No.
• Remedy: adapter A proves `AuthenticatedRequest → PCIRequest` in this Context; if reusing across Contexts, publish a **KindBridge** for the PCI taxonomy with **`CL^k=2`** (loss: token class collapsed).

**CT2R‑LOG.**
• State P in a state P in a proof‑checked logic (where appropriate for F7+), so that changes to token rules break proofs. Proofs rely on the **AuthenticatedRequest** definition, not on the consumer’s scope.

**Role‑CAL.**
• Register a **RoleMask** over `PCIRequest` for the consuming team; guards must be able to test the mask’s constraints at gate time.

**Outcome.**
• **Typed guard** approves only when: (i) the type pre‑check passes (same‑Context subkind‑of or a KindBridge with an acceptable congruence level), (ii) **Scope** covers the target context (API v2.3, explicit time selector), and (iii) **R** reflects the **scope‑bridge** and **kind‑bridge** penalties and evidence is fresh.
• No one widened Scope to hide a type mismatch; the adapter + bridge made the semantics explicit and auditable.


> **Takeaway.** If you keep these six hand‑offs in view—words → kinds → structure → composition → logic → roles—you get **predictable reviews**, **clean risk accounting**, and **reusable claims** that travel across Contexts without silent meaning drift.

#### C.3:7.3 - Compliance & Regulatory Alignment — profile

Treat regulatory categories as **Kinds**, carry their **intent** in `KindSignature` with declared **F**, move them across Contexts with a **KindBridge** (type‑congruence **`CL^k`** + loss notes), and express applicability as **Claim scope** over `U.ContextSlice` (with explicit **Γ_time**). Any Cross‑context uncertainty is routed to **R** via **Ψ(`CL^k`)** (kind) and **Φ(CL)** (scope); **F** and **G** remain unchanged.

> **Authoritative obligations and guard macros** (C‑REG‑1…8, Guard_RegAdopt / Guard_RegChange / Guard_RegXContextUse) and worked scenarios live in **C.3.A, Annex A (Regulatory adoption profile)**.


#### C.3:7.4 - How typed reasoning plugs into **Assurance Lanes (VA/LA/TA) & Evidence design**

**Intent (manager’s view).** Typed reasoning turns “prove/test/qualify” into a **repeatable plan** by making *what the rule talks about* explicit (named **Kinds**, their **subkinds**, optional **RoleMasks**) and keeping **Scope (G)** over `U.ContextSlice` separate from **membership** inside the slice. Cross‑context uncertainty (Scope Bridge **CL**, KindBridge **`CL^k`**) always routes to **R** as penalties **Φ/Ψ**; it never changes **F** or **G**.

**Evidence matrix (sketch).**

| Row set                       | Column set                                                   | Cell content                                                                                                           |
| ----------------------------- | ------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------- |
| **Kinds** (subkinds or masks) | **Context slices** (Standard versions, env ranges, `Γ_time`) | **Evidence unit** (proof fragment, test batch, monitoring window), with **Scope** and **MemberOf** predicates attached |

*Tip.* For formal kinds and “up‑to‑iso” kinds (AT K2/K3), expect **more rows** (variants). For instance‑like kinds (AT K0), expect **fewer rows** and **tighter columns** (narrow slices, stricter freshness).

> **Authoritative evidence obligations and guard macros** (planning/attachment, VA/LA/TA duties, anti‑patterns) are in **C.3.A, Annex B**.

#### C.3:7.5 - How typed reasoning plugs into **ESG and Method–Work gating**

> Intent. Make state changes and work admissions deterministic, auditable, and safe by separating (1) **typed compatibility** (what the statement or capability is about) from (2) **scope coverage** (where it holds or can run). Any Cross‑context uncertainty is routed to **R** (reliability) only—never to **F** (form) or **G** (scope).


##### C.3:7.5.1 - Scope & fit

This subsection defines **normative guard obligations** for:

* **ESG** (Episteme State Graph) transitions whose assertions **quantify over kinds**, and
* **Method–Work** admissions where a **capability** expects inputs/outputs of specified kinds.

It reuses:

* **USM** (A.2.6): `U.ClaimScope` (G) and `U.WorkScope` coverage + `Γ_time`,
* **Kind‑CAL core** (C.3.1–C.3.2): `U.Kind`, `MemberOf(e,k,slice)`, `⊑`,
* **KindBridge** (C.3.3) with **`CL^k`** and loss notes,
* **Scope Bridge** (Part B) with **CL** and loss notes,
* **RoleMask** (C.3.4) when local adaptations of a kind are used,
* **Formality F** (C.2.3) when transitions gate on rigor,
* **Assurance R** (C.2.2) for evidence freshness and penalties Φ/Ψ.

**Guard macros.** The **normative guard shapes** for ESG and Method–Work (**Guard_TypedClaim**, **Guard_TypedJoin**, **Guard_MaskedUse**, **Guard_XContext_Typed**) are specified in **Annex C.3.A**. Use those shapes; the present section is a manager‑level overview only.

##### C.3:7.5.2 - Inputs & roles (at guard time)

* **TargetSlice** — the specific context you are deciding for: Context, versioned Standards, environment parameters, and an explicit **time selector (Γ_time)**.
* **Typed carriers**

  * **ESG:** the **Claim** quantifies over one or more **Kinds** (e.g., “for all vehicles in the target context …”).
  * **Method–Work:** the **Capability** declares expected input/output kinds (and possibly RoleMasks).
* **Thresholds** (context‑local policy):

  * Minimum **F** level for the Claim (if the Context gates on rigor),
  * Minimum **congruence** for **scope bridges**,
  * Minimum **type‑congruence** for **KindBridges**,
  * Evidence **freshness windows** (R‑lane).
* **Evidence bundle** (if the transition implies trust): references, dates, windows.


##### C.3:7.5.3 - Manager’s 7‑step checklist (operational)

1. **Name the slice.** Write the full `TargetSlice`/`JobSlice` tuple including **`Γ_time`**.
2. **Check coverage.** Claim/Work scope **covers** the slice (USM).
3. **Check typed definedness.** A deterministic membership check is available in this context for every kind you use (and any masks are registered).
4. **Check typed compatibility.** same Context: `⊑` (or mask constraints met). Cross‑context: **KindBridge** with **`CL^k ≥ c`**.
5. **Bridge scope if needed.** Scope Bridge with **CL ≥ c** for Cross‑context scope.
6. **Apply penalties to R.** Apply the **scope‑bridge penalty** and the **kind‑bridge penalty**; then check evidence **freshness** windows.
7. **(If gated) Check F.** Enforce `Formality ≥ F_k` for the transition.

> **Remember:** **F** and **G** never change because of bridges; only **R** is penalized. AT (K0…K3) is informative and **not** used in guards.


##### C.3:7.5.4 - Cross‑references

* **USM / A.2.6:** Scope coverage, `Γ_time`, serial **∩**, **SpanUnion**, Bridge+CL.
* **Kind‑CAL / C.3.1–C.3.4:** `U.Kind`, `⊑`, `MemberOf`, RoleMask, KindBridge + **`CL^k`**.
* **Formality / C.2.3:** `U.Formality` thresholds (when ESG gates on rigor).
* **Assurance / C.2.2:** Freshness windows; **Φ(CL)** and **Ψ(`CL^k`)** penalties to **R** (weakest‑link on paths).

This subsection is **normative** for guards in ESG and Method–Work that **use kinds**.

### C.3:8 - Cross‑context typed reuse & assurance accounting

#### C.3:8.1 - The **two‑bridge rule** (mandatory)

When any part of the use crosses Contexts:

1. **Scope Bridge** (USM/Part B) with **CL** → penalty **Φ(CL)** to **R**.
2. **KindBridge** (C.3.3) with **`CL^k`** → penalty **Ψ(`CL^k`)** to **R**.

Both bridges carry **loss notes**; neither changes **F** or **G**. See **C.3.A Guard\_XContext\_Typed**.


#### C.3:8.2 - Narrowing after mapping (best practice)

If a bridge’s loss notes indicate material mismatch (dropped invariants, collapsed subkinds):

* **Narrow the mapped Scope** to areas where those losses are benign.
* **Or** introduce an **adapter** (plus evidence) that restores the needed properties in the target Context.
* Document the decision; the penalties still land in **R**.


#### C.3:8.3 - Typical Cross‑context patterns (manager’s catalog)

* **Name‑level overlap only (low `CL^k`).**
  Expect significant Ψ penalty. Limit quantification, add local checks, or refuse reuse until the kind mapping is improved.

* **Up‑to‑iso mapping (high `CL^k`).**
  Often seen for K3 kinds. Ψ penalty is small; treat as “shape‑preserving” transfer. Still apply the appropriate **Φ(CL)** for Scope.

* **Mask‑to‑subkind evolution.**
  If receivers repeatedly use the same **RoleMask** to make a transfer safe, promote it to an explicit **subkind** and update the bridge to preserve that link.


#### C.3:8.4 - Decision pattern (fast path)

1. **Typed pre‑check:** `k_A ⊑ k_B` (same Context) **or** `KindBridge(k_A → k′_B)` with acceptable **`CL^k`**.
2. **Scope coverage:** `translate(Scope_A)` covers `TargetSlice_B`.
3. **Apply penalties:** **Φ(CL\_scope)** and **Ψ(`CL^k`)** to **R**.
4. **Freshness:** windows/decay for all bound evidence.
5. **Publish:** a short “Bridge and Loss Notes” box; include any **narrowing** or **adapters** used.


### C.3:9 - Authoring guidance (engineers‑managers)

#### C.3:9.1 - When to mint a `U.Kind`

Create a Kind when:

* multiple claims refer to the **same “describedEntity”** using unstable labels;
* you need **subkinds** (refinement) or repeated **RoleMasks**;
* different Contexts must **map** this “describedEntity” via bridges;
* you need to **quantify** over a population (and plan variant coverage) instead of over a single exemplar.

Avoid creating a Kind for **one‑off** instance references—prefer a clear **K0** facet or just a literal exemplar in the claim.


#### C.3:9.2 - Writing a **KindSignature** (and picking **F**)

* Start with a concise **intent**: the invariants/constraints that make membership meaningful.
* Aim for **F4** (predicate‑like) if the kind is intended for reuse; rise to **F7+** only where proof‑grade is justified.
* Use **observable** terms (no “latest”); if a Standard matters, **name its version**.
* If defining a Kind reveals systematic **narrowings** in use, introduce explicit **subkinds** (`⊑`) rather than accumulating opaque masks.

> **Example (sketch).**
> `Kind Vehicle` — intent: “has VIN; has brake system; has propulsion {ICE, EV, Hybrid}; …” (F4 predicates).
> Subkind: `PassengerCar ⊑ Vehicle`.
> RoleMask: `Vehicle@ABSRequired` for processes that demand ABS (deterministic constraints; candidates for promotion to subkind if widely reused).


#### C.3:9.3 - Setting the **AT** facet (K0…K3)

Use **AT** to **aim effort**, not to gate:

* **K0**: instance/cohort — focus **R** on the TargetSlice; don’t over‑formalize.
* **K1**: behavioral pattern — clarify Standards; plan ΔF (F3→F4).
* **K2**: formal class — invest in F4–F7; plan **variant coverage** across subkinds in **R**.
* **K3**: up‑to‑iso — expect high‑quality bridges; consider F7–F9 for critical invariants.

Never treat **AT** as “wider/narrower” **G**.


#### C.3:9.4 - Writing a typed claim (with USM blocks)

**Skeleton.**

* **Kinds used:** `Vehicle` (K2), subkinds `PassengerCar`.
* **Claim scope (G):** `surface∈{dry,wet}; speed≤50; rig=v3; Γ_time=rolling 180d`.
* **Statement:** `∀ x ∈ Extension(Vehicle, TargetSlice) …`
* **Guards:** use **C.3.A Guard\_TypedClaim**; if Cross‑context, add **Guard\_XContext\_Typed** (two‑bridge rule).

**Tip.** Keep **Scope**, **MemberOf definedness**, **F thresholds**, and **freshness** as **separate** guard predicates—the auditor should be able to tick each box independently.


#### C.3:9.5 - Minimal “Kind card” contents (Context catalog)

* **Name** and **intent summary** (KindSignature snippet + **F**).
* **`⊑` links** (parents/children).
* **Examples of `MemberOf@slice`** (what membership looks like in practice).
* **Known RoleMasks** (type, constraints, determinism).
* **Known KindBridges** (source/target Contexts, **`CL^k`**, loss notes, definedness).
* *(Optional)* **AT** facet with one‑line rationale.


### 10 - Review & integration guidance

#### C.3:10.1 - Reviewer’s 8‑point checklist

1. **Named describedEntity.** Does the claim state **what** it quantifies over (`U.Kind`)?
2. **Scope explicit.** Is **G** declared (no “domain” placeholders, no implicit “latest”)?
3. **Typed compatibility.** For compositions, do we have `⊑` (same Context) or a **KindBridge**?
4. **RoleMasks.** If used, are they **registered**, **deterministic**, and not masquerading as kinds?
5. **Two‑bridge rule.** For Cross‑context use, do we have **both** Scope Bridge (**CL**) and **KindBridge** (**`CL^k`**)?
6. **Penalties.** Are **Φ(CL)** and **Ψ(`CL^k`)** applied to **R**, not smuggled into F/G?
7. **Freshness.** Are validation/monitoring windows separate from Scope coverage?
8. **Evidence fit.** For class‑level claims, does the test plan cover **subkinds/variants**?


#### C.3:10.2 - Integrator’s composition playbook (typed first, then scope)

* **Step 1:** Check `k_A ⊑ k_B` (or KindBridge).
* **Step 2:** Compute **Scope\_serial** = `Scope(A) ∩ Scope(B)` (USM).
* **Step 3:** If parallel supports exist, **SpanUnion** them (only where independent).
* **Step 4:** Apply **Φ**/**Ψ** penalties to **R**; enforce freshness.
* **Step 5:** If a **mask** is repeatedly required, consider promoting it to a **subkind**.


#### C.3:10.3 - Assurance lead: wiring penalties and windows

* Identify channels used: **Scope bridge? KindBridge?**
* Apply **Φ(CL)** and **Ψ(`CL^k`)** to **R** (monotone; higher congruence ⇒ smaller penalty).
* Verify **freshness windows** for all bound evidence (independent of bridges).
* Publish a **one‑box summary**: bridges, levels, loss notes, any narrowing/adapters, net impact on **R**.


#### C.3:10.4 - Red flags (stop‑the‑line)

* “**We widened G because we reworded the type.**” → **Reject**; redo as subkind/bridge or revise Scope honestly.
* “**Mask equals kind.**” → **Refactor**; register mask properly or promote to subkind.
* “**Cross‑context without KindBridge.**” → **Block**; demand mapping and **`CL^k`**.
* “**No Γ\_time.**” → **Block**; add explicit time policy (point/window/rolling).


### C.3:11 - Worked examples (end‑to‑end)

+> *Each example shows the typed pre‑check, Scope composition, penalties to **R**, and the managerial decision. Full guard clauses for these scenarios are in **Annex C.3.A**.*

#### C.3:11.1 - Cyber‑physical braking policy across labs and plants

**Claim (Lab Context).**
“∀ `x ∈ Vehicle`: brakingDistance(x) ≤ 50 m (dry), ≤ 40 m (wet).”
**Kinds.** `Vehicle` (K2, KindSignature F4); subkind `PassengerCar ⊑ Vehicle`.
**Scope (Lab).** `{surface∈{dry,wet}, speed≤50, rig=v3, Γ_time=rolling 180d}`.

**Reuse at Plant B.**
– **KindBridge:** `Vehicle ↦ TransportUnit` with **`CL^k=2`** (loss: EV subkind collapsed).
– **Scope Bridge:** `Lab → PlantB` with **CL=2** (rig bias ±2 %).
– **Narrowing:** loss notes indicate wet‑surface bias; Plant B **narrows** mapped Scope to temp/adhesion ranges with acceptable bias.

**Decision.**
Typed pre‑check: **OK** via KindBridge. Scope coverage after translate/narrow: **OK**.
Penalties: apply **Φ(2)** and **Ψ(2)** to **R**; freshness windows checked.
**Outcome:** Adopt with reduced **R**; action item: qualify rig v4 to raise CL in the future.


#### C.3:11.2 - API decision rule with adapter and subkind promotion

**Consumer claim.**
“∀ `x ∈ AuthenticatedRequest`: deny if riskScore(x) ≥ θ ∧ budgetSlack ≤ β.”

**Producer reality.**
Service A emits `Request` (no auth guarantee).
**Option A:** A proves it emits `AuthenticatedRequest` (introduce subkind or strengthen Standard).
**Option B:** Insert **adapter** that filters/annotates `Request → AuthenticatedRequest`.

**Typed check.**
Before: no `Request ⊑ AuthenticatedRequest`. After **Option B**: adapter supplies the guarantee; repeated use leads to promoting **mask** to **subkind**.

**Scope.**
API v2.3; Γ\_time = rolling 30 d.
**R.**
No Cross‑context reuse; no Φ/Ψ. Evidence: adapter correctness on the TargetSlice.

**Outcome.**
Adopt via Option B; open task: generalize producer to subkind and remove adapter later.


#### C.3:11.3 - Clinical dosage rule across jurisdictions (bridge + mask)

**Claim (Hospital X).**
“∀ `x ∈ AdultPatient`: dosage ≤ D per kg for drug M.”
**Kind.** `AdultPatient` (K2, F4).
**Mask.** `AdultPatient@ClinicMask` narrows to the clinic’s cohort (deterministic DOB policy).

**Reuse in Jurisdiction Y.**
– **KindBridge:** `AdultPatient ↦ AdultPerson_Y`, **`CL^k=1`** (18 vs 21 years boundary).
– **Scope Bridge:** coding systems differ (CL depends on mapping quality).
– **Narrowing:** restrict Scope to datasets where DOB granularity supports boundary reconciliation.

**Decision.**
Typed pre‑check via KindBridge: **OK**. Scope coverage after translate/narrow: **OK**.
Penalties: **Φ(CL\_scope)** and **Ψ(1)** applied to **R**.
**Outcome:** Adopt with strong **R** penalty; plan: negotiate a harmonized boundary to raise `CL^k`.


#### C.3:11.4 - ML fairness constraint with typed quantification

**Claim (Product Context).**
“∀ `x ∈ EligiblePerson`: TPR difference ≤ δ across groups `G`.”

**Kind.** `EligiblePerson` transitions from **K1→K2** as attributes and cohorts are formalized (KindSignature F4).
**Scope.** `{pipeline=P, features=F, Γ_time=rolling 180 d}`.

**Cross‑context use.**
Model team Context has `Resident` with different feature basis.
– **KindBridge:** `EligiblePerson ↦ Resident` with **`CL^k=1`** (feature loss).
– **Scope Bridge:** `pipeline P → P′`, **CL=2**.

**Decision.**
Typed pre‑check **OK** via bridges; mapped Scope **covers** the subset where features align.
Apply **Φ(2)** and **Ψ(1)** to **R**; restrict groups to mapped subset; require monitoring freshness.
**Outcome:** Adopt with reduced **R** and a mitigation note; action items: improve feature mapping and raise KindSignature F.

### C.3:12 - Anti‑patterns & how to fix them

> *Use this section as a “red flags” sheet in reviews. Each item links to a concrete remedy that preserves F–G–R & USM discipline (F/G/R separation, USM algebra, typed pre‑checks).*

| Anti‑pattern (what goes wrong)                                   | Why it’s wrong (conceptual fault)                                                               | The fix (normative/informative pointers)                                                                                                              |
| ---------------------------------------------------------------- | ----------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------- |
| **“We widened G because we reworded the type.”**                 | Confuses **describedEntity** (kind) with **applicability** (scope). Abstract wording ≠ broader scope. | Keep typed pre‑check separate (C.3.1 `⊑` or C.3.3 KindBridge). Widen **G** only via **ΔG+** with support (USM A.2.6).                                 |
| **“Kind scope” block attached to a Kind.**                       | Kinds don’t carry Scope; they carry **intent/extent**.                                          | Remove the block. Scope stays on claims/capabilities (USM). If you meant classifier definedness, state it via **K‑07** (C.3.2).                       |
| **Inferring scope from extension size.**                         | **Scope ≠ Extension**; extension is “which instances in a slice,” not “where the claim holds.”  | Keep **G** set‑valued over `U.ContextSlice` (USM). Use `MemberOf` only inside the typed quantifier.                                                   |
| **Mask used as a hidden kind (“just call it the masked kind”).** | Opaque drift; reviewers can’t see constraints.                                                  | Register a **RoleMask** (C.3.4). If reused across guards, **promote to subkind** with `⊑`.                                                            |
| **Cross‑context reuse with only one bridge.**                       | Contexts differ on two characteristics: Scope **and** Kind.                                                   | Apply the **two‑bridge rule**: Scope Bridge (**CL** → Φ) **and** KindBridge (**`CL^k`** → Ψ). Both penalties land in **R**.                           |
| **Using AT (K0…K3) as a gate/threshold.**                        | AT is an **informative facet**, not a Characteristic; gating on AT recreates a G‑ladder.        | Remove AT from guards. Use it only to **aim ΔF/ΔR** and to set **bridge expectations** (C.3.5).                                                       |
| **“Automated execution success proves the type claim.”**                            | Execution success (F5/6) is not proof (F7+); also confuses **R** with **F**.                    | If you need proof‑grade properties, raise **F** for the claim/KindSignature (C.2.3) or restrict the claim. Keep **R** as evidence freshness/coverage. |
| **Hidden “latest” in membership or scope checks.**               | Non‑deterministic evaluation; unverifiable audit trail.                                         | Declare **Γ\_time** explicitly in Scope (USM). Membership must be **deterministic** (C.3.2 K‑05/K‑07).                                                |
| **Fixing type mismatch by “unioning scopes.”**                   | G‑union cannot repair **describedEntity** mismatches.                                                 | Introduce a **subkind**, add an **adapter** (+evidence), or define a **KindBridge**.                                                                  |
| **Collapsing subkinds silently in a bridge.**                    | Reviewers don’t see lost distinctions → false confidence.                                       | Record **loss notes** on the KindBridge (C.3.3 KB‑11); consider **narrowing** mapped Scope or adding an adapter.                                      |


### C.3:13 - Governance & conformance pull‑ups

> *Contexts adopt Kind‑CAL by meeting the **Context‑level** obligations below. They summarize, not duplicate, the formal requirements in **C.3.1–C.3.5** and **C.3.A**. Use this as an adoption checklist.*

#### C.3:13.1 - Context‑level obligations (must‑haves)

1. **Kinds & order.** Maintain a Context catalog of `U.Kind` with an explicit **partial order** `⊑`.
   – Conformance: **C.3.1** (K‑01/K‑02).

2. **Kind signatures (intent).** For each Kind, publish a **KindSignature** with declared **F** (C.2.3).
   – Conformance: **C.3.2** (K‑03/K‑04).

3. **Deterministic membership.** Ensure `MemberOf(e,k,slice)` is **deterministic**; declare any definedness domain.
   – Conformance: **C.3.2** (K‑05/K‑07).

4. **Typed guards.** When a claim quantifies over kinds, guards SHALL use the **typed guard macros** (or equivalents) from **C.3.A**; **Scope coverage** and **typed checks** are separate predicates.

5. **Role masks.** If a local projection is needed, register a **RoleMask** (type: constraint/vocabulary/composite); avoid cloning kinds.
   – Conformance: **C.3.4** (RM‑01…RM‑06).

6. **Two‑bridge rule for Cross‑context use.**
   – **Scope Bridge** (Part B) with **CL** → Φ(CL) to **R**.
   – **KindBridge** (C.3.3) with **`CL^k`** → Ψ(`CL^k`) to **R**.
   – Conformance: **C.3.3** (KB‑01…KB‑10).

7. **Decision records.** For each typed state change, record: **TargetSlice tuple**, typed compatibility outcome (`⊑` or KindBridge), **Scope coverage**, applied **Φ/Ψ** penalties to **R**, and **freshness** checks.

#### C.3:13.2 - ESG / Method‑Work template inserts (normative snippets)

* **Kinds used:** list `U.Kind` and any expected **subkinds** or **RoleMasks**.
* **Claim scope (G):** explicit predicates over `U.ContextSlice` inc. **Γ\_time**.
* **Typed guard lines:**
  – same Context: `k_A ⊑ k_B` *checked*.
  – Cross Context: `KindBridge(k_A → k′_B)`, `CL^k ≥ c_k` *checked*.
* **Scope bridge lines:** `Bridge(Context_A → Context_B)`, `CL ≥ c_s` *checked*.
* **Assurance lines:** `Φ(CL)`, `Ψ(CL^k)` applied to **R**; **freshness windows** hold.

#### C.3:13.3 - Audits & levels of adoption (informative)

* **USM‑Typed‑Ready.** Catalog exists; `⊑` declared; guard macros installed.
* **USM‑Typed‑Guarded.** All typed claims use **C.3.A** guard shapes; **Γ\_time** explicit; two‑bridge rule enforced.
* **USM‑Typed‑Auditable.** Decision records capture **TargetSlice**, typed checks, bridges, penalties, freshness.
* **USM‑Typed‑Composed.** Compositions use typed pre‑check before Scope algebra; independence justified for **SpanUnion**.


### C.3:14 - Migration & editorial impact

> *Apply these edits incrementally; you do not need to stop other work. The aim is to eliminate synonym drift, restore F/G/R separation, and make typed reasoning routine.*

#### C.3:14.1 - Inventory & refactor (steps)

1. **Inventory** claims that implicitly talk about “things” (vehicles, requests, accounts, cohorts…).
2. **Name kinds** for recurring “describedEntity”; start at **K1**; promote to **K2** as invariants stabilize.
3. **Extract KindSignature** (aim **F4**); declare **F**.
4. **Refactor claims** to typed quantification: `∀ x ∈ Extension(k, slice) …` plus **Scope (G)** predicates.
5. **Publish bridges** where reuse is Cross‑context: Scope Bridge (**CL**) and KindBridge (**`CL^k`**) with loss notes; wire penalties **Φ/Ψ** to **R**.
6. **Normalize masks**: register RoleMasks; if reused, promote to subkinds (`⊑`).

#### C.3:14.2 - Edits to other parts (normative redirects, no new math)

* **A.2.6 (USM).**
  – Add “no Scope on kinds” note.
  – In typed examples, show `MemberOf` definedness + Scope coverage.
  – Two‑bridge rule for Cross‑context typed reuse.

* **C.2.2 (F–G–R).**
  – Replace any “generality/abstraction” wording with **Claim scope (G)**.
  – Before scope composition, require typed pre‑check (`⊑` or KindBridge).
  – Distinguish penalties: **Φ(CL)** vs **Ψ(`CL^k`)** → both to **R**.

* **C.2.3 (F).**
  – Add note: **KindSignature** has its own **F**; claim‑level F remains by weakest‑link.

* **Part B (Bridges).**
 – Introduce **KindBridge** with **`CL^k`**, monotone order preservation, loss notes; determinism.
 – Chaining uses **min** of levels (weakest‑link) **for both** **CL** (Scope bridges) **and** **`CL^k`** (KindBridges).


* **Role‑CAL.**
  – Add **RoleMask** for kinds; determinism; promotion rule to subkind when reused.

* **Compose‑CAL.**
  – Add typed pre‑check before Scope algebra; forbid “type‑by‑scope”.

* **Part E (Lexicon).**
  – Add: `U.Kind`, `U.SubkindOf (⊑)`, `KindSignature`(+F), `Extension`, `MemberOf`, `U.RoleMask`, **KindBridge**, `CL^k`, **AT (kinds, facet)**.
  – Mark as **legacy aliases** (not characteristic names): *generality (as ladder), kind scope, validity (as characteristic), capability envelope*; redirect to **Claim/Work scope** or **Kind** entries.

#### C.3:14.3 - Backwards compatibility

* Historical prose may keep legacy words. **Guards, conformance text, and state assertions** MUST use the Kind‑CAL/USM vocabulary and guard shapes.
* When annotating older records, add a small “typed note” box: **Kinds**, **Scope**, **Bridges (CL/`CL^k`)**, **loss notes**, **penalties to R**.


### C.3:15 - Extended rationale & design notes  \[I]

> *This section explains the design choices that keep Kind‑CAL compact and interoperable with F–G–R & USM without drifting into tooling or technology stacks.*

#### C.3:15.1 - Why **no Scope on kinds**

Scope answers **“where the claim holds”** (set of Context slices, USM); kinds answer **“what the claim is about”**. Putting Scope on kinds would either (a) duplicate claim Scope, or (b) smuggle applicability into a classifier. We prevent both by: **intent/extent on kinds** (C.3.2), **Scope on claims/capabilities** (USM).

#### C.3:15.2 - Why **two bridges** (Scope vs Kind)

Contexts diverge along **context** (Standards, parameters, time) and **classification** (what counts as a member). A single bridge hides which characteristic is mismatched. Two explicit bridges keep fixes targeted: **ΔG / narrowing** for context misfit; **subkind/adapter** for classification misfit. Both risks land in **R** as separate penalties (**Φ/Ψ**).

#### C.3:15.3 - Why **AT is a facet**

AT (K0…K3) improves **planning** (ΔF/ΔR, bridge style) and **navigation** without introducing new algebra. Making AT a Characteristic would recreate a “G‑ladder,” blur applicability with abstraction, and invite gating on AT. As a facet, AT remains helpful but **toothless in math**, which is precisely what we want.

#### C.3:15.4 - Why **RoleMask** and not “clone a kind”

Operational tweaks (extra constraints, local aliases) are real but temporary. Cloning kinds creates drift and duplicate bridges. **RoleMask** documents the tweak **without breaking identity**; promotion to subkind occurs when practice stabilizes. This keeps catalogs small and bridges honest.

#### C.3:15.5 - Fit with **Compose‑CAL** and **LOG‑CAL**

Typed pre‑checks (same‑Context `⊑` or KindBridge) act like **port compatibility** before any Scope arithmetic. LOG‑CAL benefits from explicit quantification `∀ x : Kind` with substitution rules aligned to `⊑`. Neither alters F/G/R algebra; they prevent category mistakes before we do trust math.

#### C.3:15.6 - CT2R lens (intuition)

A **KindBridge** behaves like a **functor** that (approximately) preserves structure between Contexts; **`CL^k`** is a practical knob for “how functorial” it is. At **K3** (up‑to‑iso), this is literal: we expect bridges to preserve equivalences, hence higher `CL^k` and smaller Ψ penalties.

### C.3:15bis - Rationale (Part E form)

**Problem.** (recap)
— Authors conflate *describedEntity* with *applicability*, widening G by abstract wording.
— Cross‑context reuse drifts semantically without declared mappings or risk accounting.
— Planning misfires: over‑formalization for instance claims; under‑testing for class claims.
— Unsafe compositions when describedEntity is implicit.

**Forces.** (recap)
— Local freedom vs global sense; minimality vs utility; intent vs extent; typed discipline vs F–G–R; abstraction vs applicability.

**Decision (C.3‑D1…D7).**
— D1: `U.Kind` is intensional and context‑local (`⊑` partial order).
— D2: Separate intent (KindSignature + F) and extent (Extension/MemberOf@slice).
— D3: No Scope on kinds (Scope lives with claims/capabilities via USM).
— D4: Typed reuse is explicit: KindBridge + `CL^k`, penalties route to **R** only.
— D5: Local adaptation via RoleMask; promote stable masks to subkinds.
— D6: AT (K0…K3) as **facet**, not a Characteristic; never used in guards.
— D7: Guard shapes: typed pre‑check → scope coverage → penalties/freshness.

**Consequences.**
(+) Predictable Cross‑context reuse: two‑bridge rule, separate penalties (Φ/Ψ) to **R**.  
(+) Manager‑friendly planning: AT guides ΔF/ΔR; typed pre‑check blocks category mistakes.  
(+) Clean F–G–R discipline: no “G‑ladder,” no hidden scope inside classifiers.  
(−) Editorial discipline required: no “Kind scope”; masks must be cataloged; promote when stable.  
(−) Initial bridge authoring cost; mitigated by loss‑notes and reuse.

**Alternatives considered.**
— *Global U.Type*: rejected as either too thin or too prescriptive across Contexts.  
— *“Kind scope” in USM*: rejected; duplicates/obscures Scope vs Extension split.

**Known uses.**
— §11.1 (cyber‑physical braking); §11.2 (API with adapter); §11.3 (clinical dosage); §11.4 (ML fairness).  
— ESG guard shapes in **C.3.A**; typed pre‑check in Compose‑CAL (§7.2.4).

**Related patterns.**
A.2.6 (USM), C.2.2 (F–G–R), C.2.3 (F), Part B (Bridges), Role‑CAL, Compose‑CAL, C.3.1–C.3.5, C.3.A.

### C.3:16 - Quick reference for managers

#### C.3:16.1 - 10‑minute start

1. Name the **Kind** your claim talks about.
2. Write **Scope (G)** as slice predicates (with **Γ\_time**).
3. If composing, check **`⊑`** or **KindBridge** first.
4. Use the **typed guard macro** (C.3.A).
5. Route bridge levels to **R** (Φ/Ψ); check freshness.

#### C.3:16.2 - 30‑day rollout plan

Week 1: Inventory & name Kinds (K1); adopt guard macros.
Week 2: Draft **KindSignature** for the top 5 Kinds (aim **F4**); register masks.
Week 3: Wire **two‑bridge rule** into ESG; add CL/`CL^k` lines to decision templates.
Week 4: Promote repeated masks to subkinds; publish first **KindBridge** records with loss notes.


### C.3:17 - Local glossary (reading aid)

> *Canonical definitions live in sub‑patterns; this list is for quick recall while reading C.3.*

* **`U.Kind`** — Minimal intensional “type/kind” object; carries **KindSignature** and **`⊑`** (C.3.1/C.3.2).
* **`U.SubkindOf (⊑)`** — Partial order on kinds (C.3.1).
* **KindSignature(k)** — Predicate‑like intent that defines the kind; has its own **F** (C.3.2).
* **Extension(k, slice)** — Set of instances of `k` **inside** a `U.ContextSlice` (C.3.2).
* **MemberOf(e, k, slice)** — Boolean membership predicate (C.3.2).
* **RoleMask(k, Context)** — Registered adaptation (constraints/aliases; optional narrowing), no new kind (C.3.4).
* **KindBridge** — Cross‑context mapping for kinds (intent/order) with **`CL^k`** and loss notes (C.3.3).
* **`CL^k`** — Kind‑congruence level; penalty **Ψ(`CL^k`)** goes to **R** (C.3.3).
* **AT (K0…K3)** — Informative facet of a Kind; aids planning/navigation; never used in guards (C.3.5).
* **Guard macros** — Typed guard shapes for ESG/composition (C.3.A).

> *End of C.3. See **C.3.1–C.3.5** and **C.3.A** for the referenced mechanics and guard macros.*

### C.3:End


## C.3.1 - U.Kind & SubkindOf (Core)

> **One‑line summary.** Defines **`U.Kind`** as a **minimal, context‑local intensional carrier** for “what a claim is about,” and **`U.SubkindOf (⊑)`** as a **partial order** over kinds. **Kinds do not carry Scope.** Scope remains on **claims/capabilities** (USM). This core pattern supplies only identity, locality, and ordering; **intent & membership** (`KindSignature`, `Extension/MemberOf`) are specified in **C.3.2**, bridges & congruence in **C.3.3**, masks in **C.3.4**, and the AT facet in **C.3.5**.

**Status.** Normative in **Part C**. Identifier **C.3.1**.
**Audience.** Engineering managers, architects, assurance leads.

**Dependencies.**

* **A.2.6 USM (Unified Scope Mechanism).** *Scope* is a set‑valued **USM property** over `U.ContextSlice` on **claims/capabilities**; algebra: `∈` (membership), `∩` (intersection), `SpanUnion` (union across independent lines), `translate` (scope mapping).
* **C.2.2 F–G–R.** F = formality of expression; **G = Claim scope**; R = assurance/evidence; weakest‑link for F/R; CL penalties feed **R**, not **F/G**.
* **C.2.3 U.Formality (F).** Ordinal F0…F9; no arithmetic; applies to all content, including Kind signatures (defined in **C.3.2**).
* **Part B Bridges & CL.** Generic (scope) bridges and CL; **Kind bridges** are specialized in **C.3.3**.

**Non‑goals.**

* No data governance or repository/notation mandates.
* No membership or signature semantics here (defined in **C.3.2**).
* No Cross‑context mapping/congruence here (defined in **C.3.3**).
* No role/mask mechanics here (defined in **C.3.4**).
* No AT facet mechanics here (defined in **C.3.5**).

### C.3.1:1 - Purpose & Audience

This pattern gives **one small, stable vocabulary** to say *what* a claim ranges over (its **describedEntity**) without entangling that with *where it applies* (Scope) or *how well it is supported* (R). For managers:

* It prevents the costly mistake “more abstract wording ⇒ wider scope.”
* It enables **typed composition** (you cannot combine claims about incompatible “things”).
* It keeps **Scope** and **Assurance** math unchanged and predictable.


### C.3.1:2 - Context

across Contexts, “type” means OWL class, SHACL shape, code type, BORO category, etc. A **neutral, minimal** object is needed to name *the kind of entities* a claim quantifies over **without** importing a full type system or altering USM. **`U.Kind`** fills that role; **ordering** between kinds captures “is‑a/refines” relationships a Context relies on.


### C.3.1:3 - Problem

1. **Scope–Type conflation.** Teams broaden G by “abstracting” prose, not by adding supported slices.
2. **Unsafe composition.** Claims are joined though they talk about different “things.”
3. **Cross‑context drift.** Without an explicit core notion of kind, bridges blur describedEntity vs applicability.


### C.3.1:4 - Forces

| Force                          | Tension to resolve                                                        |
| ------------------------------ | ------------------------------------------------------------------------- |
| **Minimality vs utility**      | Keep the core tiny yet sufficient for composition and governance.         |
| **Locality vs reuse**          | Kinds are context‑local, but projects reuse claims across Contexts via bridges. |
| **describedEntity vs applicability** | Ordering should not leak into Scope; kinds must not carry G.              |
| **Neutrality vs specificity**  | Avoid committing to any particular type/ontology stack or notation.       |


### C.3.1:5 - Solution — Core Objects (overview)

* **`U.Kind`** — a **context‑local intensional** object naming a “kind of thing” claims may quantify over.
* **`U.SubkindOf (⊑)`** — a **partial order** on kinds (reflexive, transitive, antisymmetric). `k₁ ⊑ k₂` reads “`k₁` refines `k₂`.”

> **No Scope on kinds.** Scope is for **claims/capabilities** (USM). Kinds supply **describedEntity only**; **membership** and **signature** live in **C.3.2**.


### C.3.1:6 - Norms & Invariants (normative)

**C3.1‑K‑01 (Partial order).** `U.SubkindOf (⊑)` **SHALL** be a **partial order** on `U.Kind`: reflexive, transitive, antisymmetric. Editors **SHALL** document any Context‑specific meets/joins if they supply them (optional).

**C3.1‑K‑02 (No Scope on kinds).** A `U.Kind` **MUST NOT** carry a Scope value. Scope lives with **claims** (`U.ClaimScope` = **G**) and **capabilities** (`U.WorkScope`) per **A.2.6**.
*Rationale pointer:* see **C.3.2** for the **intent/extent vs Scope** split.

**C3.1‑K‑03 (Identity & locality).** A `U.Kind` is **context‑local**. Cross‑context mapping of kinds is handled by **KindBridge** (see **C.3.3**); such mapping **MUST NOT** be conflated with Scope bridging.

**C3.1‑K‑04 (Naming).** A Context **SHALL** assign stable identifiers to kinds and **SHOULD** catalog parent/child `⊑` links. Synonyms/aliases **SHALL** point to the canonical kind id.

**C3.1‑K‑05 (Separation of concerns).** This core **does not** define kind intent or membership; those are specified in **C.3.2** (`KindSignature` with its own F; `Extension/MemberOf` and determinism).


### C.3.1:7 - Interactions (informative)

* **With USM (A.2.6).** Guards that quantify over a kind use **two** predicates: “Scope covers TargetSlice” (USM) **and** whatever **membership** predicate is defined for the kind (see **C.3.2**). Kinds themselves carry **no Scope**.
* **With F–G–R (C.2.2).** This pattern does not alter the triple; typed checks happen **before** scope algebra, preventing invalid compositions.
* **Order of checks reference.** See **Annex C.3.A §5 (E‑01)** for the normative evaluation order: typed compatibility first, then Scope coverage, then penalties to **R** and freshness.
* **With Formality (C.2.3).** A **KindSignature** (C.3.2) declares its **F**; claims retain their own F via weakest‑link.
* **With Bridges (Part B).** Use **KindBridge** (C.3.3) for describedEntity; use **Scope Bridge** (Part B) for applicability. Penalties land in **R** via different channels.


### C.3.1:8 - Authoring & Review (informative)

**When to mint a kind.**
Mint a `U.Kind` when claims repeatedly quantify over “the same sort of thing” and you need: (i) safe composition, (ii) clear Cross‑context mapping, (iii) a place to collect invariants (in **C.3.2**).

**Don’t over‑mint.**
If a local constraint is temporary or purely procedural, prefer a **RoleMask** (C.3.4) over a new subkind.

**Review prompts.**

1. Does the draft introduce a new *describedEntity* concept? → consider a kind.
2. Does prose hint at “is‑a” relationships? → capture as `⊑`, not as scope widening.
3. Are authors trying to widen scope by abstracting wording? → stop; widen **G** only via **ΔG** (USM) with support.


### C.3.1:9 - Examples (informative, technology‑neutral)

1. **Vehicle/PassengerCar.**
   Mint `Kind Vehicle`. Later add `PassengerCar ⊑ Vehicle`. Claims about **Vehicle** may be reused by narrowing to **PassengerCar** without touching **G**. Scope remains an independent predicate over `U.ContextSlice`.

2. **Request/AuthenticatedRequest.**
   If multiple policies speak about “authenticated requests,” declare `AuthenticatedRequest ⊑ Request`. Do **not** widen G to compensate for missing authentication; either change the producer’s kind or insert an adapter (C.3.2/C.3.4) while keeping G honest.


### C.3.1:10 - Conformance checklist (normative)

| ID            | Requirement                                                                                             |
| ------------- | ------------------------------------------------------------------------------------------------------- |
| **C3.1‑K‑01** | `U.SubkindOf (⊑)` is a **partial order** (reflexive, transitive, antisymmetric).                        |
| **C3.1‑K‑02** | `U.Kind` **does not carry Scope**. Scope remains on claims/capabilities per **A.2.6**.                  |
| **C3.1‑K‑03** | Kinds are **context‑local**; Cross‑context mapping uses **KindBridge** (C.3.3), not Scope bridges.            |
| **C3.1‑K‑04** | Kinds have **stable ids**; synonyms redirect; Contexts catalog `⊑` links.                                  |
| **C3.1‑K‑05** | **No intent/membership** in this core; refer to **C.3.2** for `KindSignature` and `Extension/MemberOf`. |


### C.3.1:11 - Rationale (informative)

**Why a tiny core?**
Contexts differ wildly in “type” practice. A large, prescriptive core would either (a) force one Tradition’s semantics on all, or (b) become an empty label. The **smallest powerful** core—identity + ordering—gives managers and integrators what they need (safe composition, predictable edits) and leaves intent/membership/bridges/masks to focused sub‑patterns.

**Why “no Scope on kinds”?**
**Scope** (USM) answers “**where** a claim/capability holds” over `U.ContextSlice`. Kinds answer “**what** the claim ranges over.” Blending them recreates the failure mode we are removing (“higher abstraction ⇒ wider scope”). The right split is:

* **Kind**: intensional name + order (`⊑`) *(this pattern)*; intent & membership *(C.3.2)*.
* **Scope**: set of context slices *(A.2.6)*.
* **Assurance**: evidence & penalties *(C.2.2 / Part B)*.

### C.3.1:End

## C.3.2 - KindSignature (+F) & Extension/MemberOf

> **One‑line summary.** Specifies the **intent and extent** of kinds: (**i**) a **`KindSignature(k)`** (the intensional definition of kind `k`) that **declares its own Formality F**; (**ii**) an **`Extension(k, slice) ⊆ U.EntitySet(slice)`** and the **membership predicate** `MemberOf(e, k, slice)` that are **deterministic per `U.ContextSlice`**; (**iii**) **monotonicity** of extension under `SubkindOf`; (**iv**) a **definedness policy** that fails **closed** outside its domain. **Kinds still carry no Scope** (that rule lives in C.3.1); Scope stays on **claims/capabilities** (USM). This pattern gives managers and reviewers the **observable basis** to check “what counts as a member here and now” without entangling applicability (G) or assurance (R).

**Status.** Normative in **Part C**. Identifier **C.3.2**.
**Audience.** Engineering managers, architects, assurance leads, editors.

**Depends on.**

* **C.3.1** (*U.Kind & SubkindOf Core*): kinds are context‑local; `⊑` is a partial order; kinds carry **no Scope**.
* **A.2.6 USM** (*Context slices & Scopes*): Claim scope (G) and Work scope live on claims/capabilities; algebra `∈` (membership), `∩` (intersection), `SpanUnion` (union across independent lines), `translate` (scope mapping).
* **C.2.3 U.Formality (F)**: ordinal F0…F9; no arithmetic; weakest‑link composition applies to content that depends on the signature.
* **C.2.2 F–G–R**: assurance calculus; CL penalties feed **R**, not **F/G**.
* **Part B (Scope Bridges & CL).** CL (scope congruence) and scope translation live in Part B/USM; **kind‑congruence `CL^k`** and kind mapping live in **C.3.3** (KindBridge).

**Non‑goals.**

* No Scope semantics here (USM); no bridge semantics here (C.3.3).
* No repository/notation mandates; this is concept‑level, not tooling.

### C.3.2:1 - Purpose & Audience

This pattern makes **describedEntity testable** in a Context:

* Authors get a place to write **what defines a kind** (`KindSignature`) and at **what rigor (F)**.
* Reviewers can ask **deterministic** questions: *“Given this `TargetSlice`, which entities are in `k`?”*
* Managers can plan **ΔF** (raise signature rigor) and **ΔR** (evidence over members) **without** changing **G** (applicability).

**No tooling assumption.** The pattern is **conceptual** and notation‑neutral (no OWL/SHACL/type‑system requirement); it specifies reviewer‑checkable obligations that managers can read in plain language.

### C.3.2:2 - Context

Different Contexts encode “type” intent differently (predicates, schemas, ontologies, Standards). Regardless of notation, a team must be able to answer, reproducibly: **who belongs to the kind at this slice?** If this is not stable, claims quantified over the kind are unverifiable, bridges are opaque, and composition becomes unsafe.


### C.3.2:3 - Problem

1. **Ambiguous membership.** Membership depends on tacit “latest” states or unwritten defaults.
2. **Signature opacity.** A kind’s definition is scattered; no single place to declare rigor (**F**) or assumptions.
3. **Order violations.** Subkind hierarchies do not guarantee subset behavior in practice.
4. **Scope leakage.** Teams smuggle applicability (G) into kind definitions, recreating G‑ladders by another name.


### C.3.2:4 - Forces

| Force                              | Tension to resolve                                                                                   |
| ---------------------------------- | ---------------------------------------------------------------------------------------------------- |
| **Local freedom vs comparability** | Contexts need their own notations, but membership must be checkable in a common style.                  |
| **Expressivity vs determinism**    | Rich intent is welcome, but membership must be deterministic given `slice`.                          |
| **Intent vs applicability**        | Define “what counts” (intent/extent) without encoding “where valid” (G).                             |
| **Rigor vs cost**                  | Raising signature F has cost; the framework must support low‑F drafts and high‑F safety cores alike. |


### C.3.2:5 - Solution — Objects & Standards (overview)

* **`KindSignature(k)`** — the **intensional** definition of kind `k` in the Context; it **declares `U.Formality`** per C.2.3.
* **`U.EntitySet(slice)`** — the set (or well‑defined universe) of **entities addressable in a given `U.ContextSlice`**.
* **`Extension(k, slice) ⊆ U.EntitySet(slice)`** — **which entities** belong to `k` **at** `slice`.
* **`MemberOf(e, k, slice)`** — membership predicate: `e ∈ Extension(k, slice)`.

**Design split.**

* **Intent** lives in **`KindSignature`** (with F).
* **Extent** is **computed per `slice`** via `MemberOf`.
* **Applicability** (where a **claim** holds) remains a **Scope** on the claim (USM) and **MUST NOT** be encoded into `KindSignature`.


### C.3.2:6 - Norms & Invariants (normative)

> IDs **C3.2‑K‑03…K‑08** correspond to the rules announced in C.3; additional local rules use **C3.2‑S‑\***.

#### C.3.2:6.1 - Signature & Formality

**C3.2‑K‑03 (Signature F).** Every `KindSignature(k)` **SHALL declare `U.Formality`** per C.2.3 (F0…F9).
— *Note:* Raising signature F **does not** automatically raise claim‑level F; claims follow weakest‑link along their **own** support paths.

**C3.2‑K‑04 (Signature change = content change).** Any change to `KindSignature(k)` that **alters membership** (i.e., would change `Extension(k, slice)` for some `slice`) **SHALL** be recorded as a **content change** (Contexts may version kinds).

#### C.3.2:6.2 - Extension & Membership

**C3.2‑K‑05 (Deterministic membership).** For fixed `(k, slice)`, `MemberOf(e, k, slice)` **MUST** be deterministically evaluable **from observable content in `slice`**.
— Implication: **“latest” is forbidden**; `Γ_time` must be explicit on `slice` (A.2.6).
— If a classifier makes external assumptions, they **MUST** be named in `KindSignature`.

**C3.2‑K‑06 (Monotone in `⊑`).** If `k₁ ⊑ k₂`, then for **every** `slice`:
`Extension(k₁, slice) ⊆ Extension(k₂, slice)`.

**C3.2‑K‑07 (Definedness & fail‑closed).** Each Context **MAY** restrict the **domain of definedness** for `MemberOf(–, k, –)` (e.g., only when a Standard or dataset is present at a given version). Outside that domain, `MemberOf` **MUST** be treated as **not defined** for guard purposes, and guards **MUST fail closed** (deny). Implementations MAY internally return `False`, but there **MUST** be no path where undefined membership yields implicit success.

**C3.2‑K‑08 (Separation from G).** Guards **SHALL** keep **Scope coverage** (USM) and **membership** **as separate predicates**:
“`U.ClaimScope(Claim) covers TargetSlice` **AND** `MemberOf(?, k, TargetSlice)` is defined/used”.

#### C.3.2:6.3 - Entity set & time

**C3.2‑S‑01 (`U.EntitySet`).** A Context **SHALL** document what counts as `U.EntitySet(slice)` (e.g., “rows in dataset D at version v,” “live objects in service S at build b,” “ontology individuals at vocabulary v”). This documentation **MUST** be stable and addressable via the `slice` tuple.
**C3.2‑S‑02 (Time).** `slice` **SHALL** specify **`Γ_time`** (point/window/policy). Membership **MUST NOT** rely on implicit recency. 

`U.EntitySet(slice)` **MUST NOT** expand implicitly via external defaults or time; its extent is fixed by the `slice` tuple (see **C3.2‑S‑02**).

### C.3.2:7 - Interactions & Placement (informative)

* **With C.3.1.** Kinds carry identity and `⊑`; **no Scope** on kinds. This pattern adds the **intent/extent** layer under those constraints.
* **With A.2.6 (USM).** A typed claim’s guard normally evaluates, in the order specified by **Annex C.3.A §5 (E‑01)**: (1) typed compatibility, (2) **Scope coverage** at `TargetSlice`, (3) **`MemberOf(?, k, TargetSlice)`** definedness and any instantiation, followed by penalties to **R** and freshness checks. Use **Guard_TypedClaim** / **Guard_TypedJoin** rather than ad‑hoc shapes.
* **With C.2.3 (F).** Signature F influences claims **only if** the claim **depends on** the signature content; weakest‑link min applies along the claim’s support path.
* **With C.3.3 (KindBridge).** When `MemberOf` is computed via a **kind mapping across Contexts**, kind‑congruence `CL^k` contributes a **monotone penalty to **R** only (Ψ(`CL^k`)); **F/G MUST NOT** be adjusted. 
* **With Role‑CAL (C.3.4).** A **RoleMask** may **narrow** membership (context‑local adaptation). Frequent masks that encode stable narrowing **SHOULD** be promoted to subkinds (`⊑`).


### C.3.2:8 - Authoring & Review Guidance (informative)

#### C.3.2:8.1 - Authoring `KindSignature`

* **Be explicit and observable.** Prefer predicate‑like clauses over prose (“has VIN format …”; “axles ≥ 2”).
* **Bind to versions.** Name Standards/schemas by version; avoid “current.”
* **Declare F honestly.** F3 for controlled narrative is fine in early phases; aim F4+ for durable kinds; consider F7+ for safety‑critical cores.
* **Name assumptions.** If membership requires external conditions (e.g., calibrated rig), put them in the signature.

#### C.3.2:8.2 - Authoring membership

* **Define `U.EntitySet(slice)`.** Write it down once per Context, make it addressable via the `slice` tuple, and reuse.
* **Determinism first.** No hidden IO, no implicit time; membership must be recomputable from the slice.
* **Document definedness.** If `MemberOf` is undefined without a Standard, say so; guards will fail closed.
* **Respect `⊑`.** If you declare `k₁ ⊑ k₂`, verify subset behavior (C3.2‑K‑06).

#### C.3.2:8.3 - Review checklist (10 minutes)

1. Is **signature F** declared? Is the signature sufficient to evaluate membership?
2. Is **`U.EntitySet(slice)`** documented and addressable?
3. Is **membership deterministic** with explicit `Γ_time` (no “latest”)?
4. If `⊑` links exist, does **subset behavior** hold at sample slices?
5. Are **Scope** and **membership** kept **separate** in guards?
6. Any **Cross‑context** classification? If yes, is **KindBridge** referenced (C.3.3)?


### C.3.2:9 - Worked Examples (informative)

#### C.3.2:9.1 - Vehicle (signature F4) and membership

**KindSignature(Vehicle)** *(F4)*:

* `hasVIN(x)` is true and parseable;
* `axles(x) ≥ 2`;
* `hasBrakeSystem(x)`;
* Standards: `registryAPI v1.4`; `Γ_time` policy: rolling 365 d for registry fields.

**`U.EntitySet(slice)`**: “records in `registryAPI v1.4` for plant `A` at build `b`, as of `Γ_time`.”
**`Extension(Vehicle, slice)`**: all records satisfying the predicates **in that `slice`**.
**Monotonicity:** `PassengerCar ⊑ Vehicle` ⇒ `Extension(PassengerCar, s) ⊆ Extension(Vehicle, s)`.

#### C.3.2:9.2 - AuthenticatedRequest (definedness & fail‑closed)

**KindSignature(AuthenticatedRequest)** *(F4)*:

* `Request` with `authHeader` present and `authSignature` valid according to `AuthStandard v2.3`;
* `Γ_time`: point in time for key validity check.

**Definedness:** `MemberOf(–, AuthenticatedRequest, slice)` is **undefined** if `AuthStandard v2.3` is **absent** in `slice` ⇒ guards **fail closed** (C3.2‑K‑07).

#### C.3.2:9.3 - Clinical cohort (low‑F signature; deterministic membership)

**KindSignature(AdultPatient)** *(F3→F4 as it hardens)*:

* `ageYears(x, Γ_time) ≥ N` (jurisdictional N varies; recorded in the Context’s signature note).
* `EntitySet(slice)`: EHR `ehr‑east v7.5` @ `Γ_time`;
* Membership deterministic if DOB present; undefined otherwise (fail closed).


### C.3.2:10 - Anti‑patterns & Remedies (informative)

| Anti‑pattern                                         | Why it’s wrong                        | Remedy                                                              |
| ---------------------------------------------------- | ------------------------------------- | ------------------------------------------------------------------- |
| Using “latest” implicitly in membership              | Non‑deterministic; unreproducible     | Require explicit `Γ_time`; treat freshness separately in **R**      |
| Encoding Scope (“only in EU plant”) in the signature | Confuses applicability with describedEntity | Move such conditions to **Claim scope (G)**; keep signature general |
| Declaring `k₁ ⊑ k₂` but not ensuring subset behavior | Breaks typed reasoning                | Tighten `KindSignature` or drop the `⊑` link                        |
| Treating RoleMask as a different kind                | Catalog sprawl; hidden semantics      | Keep mask as adaptation; promote to subkind if widely reused        |
| Membership relying on external, unnamed assumptions  | Hidden dependencies; review fatigue   | Name assumptions in the signature; point to Standards/versions      |


### C.3.2:11 - Rationale (informative)

#### C.3.2:11.1 - Why give **F** to `KindSignature`?

Because rigor in the **definition of a kind** materially affects how safely teams can quantify over it. A signature at **F4** (predicate‑like) makes membership checkable in principle; **F7+** (machine‑checked) can support proof‑carrying development. Keeping this **separate from claim‑level F** prevents “signature formalization” from inflating unrelated claims.

#### C.3.2:11.2 - Why **Extension** is not **Scope**

* **Extension** answers: *“Which entities count as `k` **in this slice**?”*
* **Scope (G)** answers: *“In which slices does **this claim** hold?”*
  Blending the two recreates the old failure mode where “more abstract wording” was treated as “wider applicability.” USM already gives the set‑algebra for G; Kind‑CAL supplies the **typed universe** the claim quantifies over.

#### C.3.2:11.3 - Why **determinism** and **fail‑closed**?

Guards must be **reproducible** and **auditable**: same `slice` ⇒ same membership result. If inputs are missing (undefinedness), the safest default is **deny** (fail closed), prompting either a richer slice or a scope/claim change.


### C.3.2:12 - Conformance checklist (normative)

| ID            | Requirement                                                                                     |
| ------------- | ----------------------------------------------------------------------------------------------- |
| **C3.2‑K‑03** | Every `KindSignature(k)` **declares `U.Formality`** (F0…F9).                                    |
| **C3.2‑K‑04** | Signature changes that alter membership are **content changes** (Contexts may version kinds).      |
| **C3.2‑K‑05** | `MemberOf(e, k, slice)` is **deterministic** for fixed `(k, slice)` (no “latest”).              |
| **C3.2‑K‑06** | **Monotonicity:** if `k₁ ⊑ k₂` then `Extension(k₁, s) ⊆ Extension(k₂, s)` for all `s`.          |
| **C3.2‑K‑07** | **Definedness:** outside domain, membership **fails closed**; guards deny use.                  |
| **C3.2‑K‑08** | **Separation:** guards keep **Scope coverage** (USM) and **membership** as distinct predicates. |
| **C3.2‑S‑01** | The Context **documents `U.EntitySet(slice)`** (stable, addressable via `slice`).                |
| **C3.2‑S‑02** | `slice` **specifies `Γ_time`**; membership **must not** rely on implicit recency.               |


### C.3.2:End

## C.3.3 - KindBridge & CL^k — Cross‑context Mapping of Kinds

> **One‑line summary.** Defines **`KindBridge`** as the normative mechanism for moving **kinds** (their **intent** and selected **subkind‑of** links) between bounded contexts (“Contexts”). A bridge declares **how a source kind maps to a target kind**, which parts of the **`⊑`** order are preserved or collapsed, and publishes a **type‑congruence level `CL^k`** with **loss notes** and a **definedness area**. **`CL^k` penalties apply only to Reliability (R)** when a claim depends on Cross‑context classification; **F** (formality) and **G** (Claim scope) remain unchanged. Scope translation continues to use the **USM Bridge + CL** channel; **KindBridge** is a **separate, parallel channel** for describedEntity.

**Status.** Normative in **Part C**. Identifier **C.3.3**.
**Audience.** Engineering managers, architects, assurance leads, editors.

**Depends on.**

* **C.3.1 — U.Kind & SubkindOf (Core):** kinds are context‑local intensional objects; `⊑` is a partial order; kinds **do not carry Scope**.
* **C.3.2 — KindSignature (+F) & Extension/MemberOf:** signature declares its own **F**; membership `MemberOf(e,k,slice)` is **deterministic** per `U.ContextSlice`.
* **A.2.6 — USM (Context slices & Scopes):** Claim scope (**G**) and Work scope live on claims/capabilities; scope bridging and **CL** penalties are defined there.
* **C.2.2 — F–G–R:** weakest‑link; penalties land in **R**, not **F/G**.
* **C.2.3 — U.Formality (F):** signature rigor.

**Non‑goals.**
— No repository/notation mandates; conceptual only.
— No Scope mapping here (that’s USM); **KindBridge** maps **kinds**, not scopes.
— No new arithmetic on `CL^k`; it reuses the **ordinal anchor semantics** of CL (Part B) but applies to kinds.

### C.3.3:1 - Purpose & Audience

Cross‑context reuse fails in two **orthogonal** ways:

1. **Applicability** (G): *where* the claim holds (handled by USM Scope Bridge).
2. **describedEntity** (Kind): *what* the claim quantifies over (handled by **KindBridge**).

**C.3.3** gives managers an explicit, auditable channel for **(2)**, so a team can say, with evidence: *“`Vehicle` in Lab maps to `TransportUnit` in Plant with `CL^k=2`; the EV subkind collapses; here’s what we lost.”* Guards stay deterministic; assurance math stays clean (penalties in **R** only).


### C.3.3:2 - Context

Contexts use different **classifications**: ontology classes vs shape Standards, regulatory cohorts vs app types, etc. Informal “same‑name” reuse silently mutates describedEntity. USM already made scope moves explicit. **KindBridge** does the same for kinds: **declare the mapping**, rate its **congruence**, and capture known **losses**.


### C.3.3:3 - Problem

1. **Semantic drift.** Moving a claim into a target‑context with a different taxonomy changes “what counts” without anyone noticing.
2. **Hidden order breaks.** Subkind relationships invert or vanish; downstream proofs/tests are misapplied.
3. **Entangled channels.** Teams conflate “scope mapping” with “kind mapping,” making it impossible to assign penalties coherently.
4. **Incomputable guards.** “We map it somehow” yields non‑deterministic classification at guard time.


### C.3.3:4 - Forces

| Force                                    | Tension to resolve                                                                              |
| ---------------------------------------- | ----------------------------------------------------------------------------------------------- |
| **Minimal disclosure vs precision**      | Bridges must be light to write yet precise enough to avoid semantic drift.                      |
| **Local autonomy vs global reuse**       | Each target‑context keeps its vocabulary; reuse requires explicit, reviewable mappings.                   |
| **Typed safety vs agility**              | We need typed compatibility checks without blocking exploratory reuse.                          |
| **Separate channels vs operator burden** | Two channels (Scope & Kind) must be explicit, but guard writers shouldn’t drown in boilerplate. |


### C.3.3:5 - Solution — The **KindBridge** object (overview)

A **KindBridge** connects **source** Context **A** and **target** Context **B** for a set of kinds. It declares:

1. **Mapping of kinds**: either to named target kinds or via **signature translation** rules.
2. **Order preservation**: which `⊑` links are preserved (monotone), which are **collapsed**, and which are **unknown** (not claimed).
3. **Type‑congruence `CL^k`**: reuses the **same anchors/labels** as **CL** (Part B) but applies to kind intent/order (not to Scope). *Gloss:* higher `CL^k` ⇒ closer preservation of kind intent and declared `⊑` links.
4. **Loss notes**: human‑readable list of invariants and subkinds **not preserved**.
5. **Definedness area**: the subset of `U.ContextSlice` characteristics where the mapping is **intended** to be used (e.g., certain Standards/versions).
6. **Determinism**: fixed versions + mapping rules ⇒ deterministic result (no “latest”).

**Effect on assurance.** When a **claim** in B depends on classification that goes through this bridge, **reduce R** by a monotone penalty **Ψ(`CL^k`)**. **Do not** change **F** or **G**.


### C.3.3:6 - Norms & Invariants (normative)

> The following formalize the **KB‑01…KB‑12** rules announced in C.3.

#### C.3.3:6.1 - Subject & Scope of a KindBridge

**KB‑01 (Subject).** A KindBridge **maps**:

* one or more **KindSignature**(s) from source to target; and
* an **explicitly declared subset of `⊑` links** (which it claims to preserve or collapse).

**KB‑02 (No Scope).** A KindBridge **MUST NOT** map Claim/Work scope (**G**). Scope translation uses the **USM Bridge + CL** channel (A.2.6, Part B).

**No blended score.** Congruence for Scope (**CL**) and for Kind (**CL^k**) **MUST NOT** be aggregated into a single “interoperability” score in guards; each channel is assessed and penalized **separately**. See **Annex C.3.A §5 (E‑06)**.


#### C.3.3:6.2 - Declaration & Shape

**KB‑03 (Declaration).** A KindBridge record **SHALL** include:

1. source/target Contexts and vocabulary/Standard **versions**;
2. a **kind mapping** per source kind `k`: either a **named** target kind `k′` or a **signature translation rule** that constructs the **target‑context** `KindSignature(k′)` (the result is owned and versioned in the target Context);
3. an **order preservation claim** for any `k₁ ⊑ k₂` it covers: *preserved* / *collapsed* / *unknown*;
4. **`CL^k`** value (using the CL anchor ladder) labeled **“kind‑congruence”**;
5. **loss notes** (non‑preserved invariants, collapsed subkinds, equality quirks);
6. **definedness area** (constraints on `U.ContextSlice` dimensions where the bridge is meant to apply).

**KB‑04 (Determinism & local evaluation).** Given fixed Context versions and mapping rules, **translateₖ** **MUST** be deterministic (no implicit “latest”). After mapping to `k′`, **membership SHALL be evaluated using the target Context’s own `KindSignature(k′)` and `MemberOf(–, k′, –)`**; source‑context membership results **MUST NOT** be reused as truth in guards (they may be cited as evidence in **R**).

#### C.3.3:6.3 - Order & Monotonicity

**KB‑05 (Monotone order).** If the bridge claims to **preserve** `k₁ ⊑ k₂`, then in the target Context **`translateₖ(k₁) ⊑′ translateₖ(k₂)`** **MUST** hold.
**KB‑06 (No inversions).** The bridge **MUST NOT** assert preserved links that **invert** order. If real‑world constraints force reversal, the link **MUST** be marked **not preserved** with a **loss note**.
**KB‑07 (Collapse semantics).** Marking a link as **collapsed** is allowed (two subkinds mapped to one target kind), but the record **SHALL** list the merged subkinds and any properties thereby lost.

#### C.3.3:6.4 - Congruence & Assurance

**KB‑08 (Anchor reuse & AT neutrality).** **`CL^k`** reuses the **ordinal anchor semantics** of CL (Part B) but applies **to kinds**. Editors **SHALL** label it explicitly as **kind‑congruence** to avoid confusion with Scope CL. **KindBridge records MUST NOT compute or alter KindAT (C.3.5 AT‑04); AT is editorial and independent of `CL^k`.**
**KB‑09 (Effect on R only).** When a claim in the target Context depends on `MemberOf(–, translateₖ(k), TargetSlice)`, a **monotone penalty `Ψ(CL^k)`** **SHALL** reduce **R** (alongside any `Φ(CL)` penalty from the Scope Bridge). Implementations **MUST NOT** adjust **F or G** due to `CL^k`.
**KB‑10 (Chaining).** For a chain of bridges, **effective `CL^k` = min** of the links (weakest‑link).

#### C.3.3:6.5 - Loss Notes & Definedness

**KB‑11 (Loss notes).** Bridges **SHALL** publish human‑readable **loss notes**: which invariants of `KindSignature` are **not preserved**, which subkinds are **collapsed**, and any **higher‑equality** caveats (e.g., up‑to‑iso only).
**KB‑12 (Definedness & guard use).** The bridge’s **definedness area** **SHALL** be stated. Guards **MUST fail closed** outside it (i.e., if a classification relies on the bridge where it is not defined, the guard denies use).


### C.3.3:7 - Interactions (informative)

#### C.3.3:7.1 - With USM Scope bridges (two channels)

When using a claim across Contexts, expect **two concurrent bridges**:

* **Scope Bridge (USM)**: maps **G**; publishes **CL**; penalty **Φ(CL)** to **R**.
* **KindBridge (this pattern)**: maps **kinds**; publishes **`CL^k`**; penalty **Ψ(`CL^k`)** to **R**.

**Discipline:** compute both; **do not** collapse them into one “interoperability score.”

 See **Annex C.3.A §5 (E‑01)** for the normative evaluation order in guards.

#### C.3.3:7.2 - With membership (C.3.2)

After mapping `k` to `k′ = translateₖ(k)`, the **target Context** evaluates membership **as usual**: `MemberOf(e, k′, TargetSlice)`. If the bridge provides a **signature translation**, that definition becomes the **local** `KindSignature(k′)` (versioned per target Context policy).

#### C.3.3:7.3 - With Role masks (C.3.4)

If a claim uses a **RoleMask(k)** across Contexts, you need:

* a **KindBridge** for `k` (`CL^k` + loss notes), and
* a documented **mask adapter** (how mask constraints translate).
  Penalties still land in **R**. If the mask’s effect is stable and widely reused, consider promoting it to a **subkind** on the target side.

#### C.3.3:7.4 - With guards (Annex C.3.A)

Use the **`Guard_XContext_Typed`** macro (Annex C.3.A), which requires **both bridges** and applies **both penalties** to **R**:

* find Scope bridge (CL≥threshold), translate **G**, check coverage;
* find KindBridge (`CL^k≥threshold`), translate **kind**, check **membership definedness**;
* apply **Φ(CL)** and **Ψ(`CL^k`)** to **R**; keep **F/G** untouched.


### C.3.3:8 - Authoring, Review & Rating Guidance (informative)

#### C.3.3:8.1 - Authoring a KindBridge

* **Start narrow & honest.** Declare only the kinds and `⊑` links you **actually preserve**; mark the rest **unknown**.
* **Prefer named targets.** If the target already has a suitable kind, map to it; use **signature translation** only when necessary, and list what’s preserved vs weakened vs dropped.
* **Write loss notes in plain language.** Example: “EV vs ICE subkinds collapsed; battery‑health invariants dropped.”
* **Fix the definedness area.** Bind to target Standards/versions and any environment selectors essential to classification.
* **Assign `CL^k` from exemplars.** Calibrate on concrete counter‑examples and preserved properties; resist optimistic ratings.

#### C.3.3:8.2 - Review playbook (10 minutes)

1. **Two bridges present?** Scope Bridge **and** KindBridge?
2. **Order claims honest?** Any `⊑` inversions? Collapses disclosed?
3. **`CL^k` plausible?** Based on preserved properties, not name similarity?
4. **Loss notes present?** Will they force narrowing of Scope or extra tests?
5. **Definedness area clear?** Guard will **fail closed** outside it?
6. **Penalties wired to R?** No hidden tweaks to **F/G**?

#### C.3.3:8.3 - Rating `CL^k` (rules of thumb)

* **High `CL^k`**: signature equivalence or **up‑to‑iso**; `⊑` fragment preserved; only cosmetic losses.
* **Medium `CL^k`**: some invariants weakened; selected subkinds collapsed; order preserved on critical path.
* **Low `CL^k`**: name‑only correspondences; properties diverge; order not preserved. Expect significant **R** penalty and/or adapters.


### C.3.3:9 - Worked Examples (informative)

#### C.3.3:9.1 - Vehicle → TransportUnit (manufacturing)

**Source kind:** `Vehicle` (K2, signature F4).
**target Context:** `PlantB`, kind `TransportUnit` exists.

**KindBridge:**

* `Vehicle ↦ TransportUnit`; **order**: preserves `PassengerCar ⊑ Vehicle`; **collapses** `EV ⊑ Vehicle` into `TransportUnit` (no EV subkind).
* **`CL^k=2`** (mid); **loss notes:** “battery‑health invariants not carried”; **definedness:** only for `registryAPI v1.4`, `Γ_time` in last 365 d.

**Use:** Claim quantified over `Vehicle` crosses to `PlantB`.
**Guards:** scope bridge CL=2 (rig bias); kind bridge `CL^k=2`; both penalties reduce **R**. **F/G** unchanged.

#### C.3.3:9.2 - AuthenticatedRequest across services (software)

**Source kind:** `AuthenticatedRequest` defined by `AuthStandard v2.3`.
**target Context:** `Frontend` with different auth header scheme.

**KindBridge:** signature translation (`authHeader` → `x‑auth`), preserves “signature valid” property; **`CL^k=3`** (high).
**Loss notes:** none; **definedness:** only where `AuthStandard v2.3` is in scope.

**Effect:** Rules quantified over `AuthenticatedRequest` can be reused; **R** penalty small (Ψ(3) near 1). Scope remains independent (API v2.3).

#### C.3.3:9.3 - AdultPatient across jurisdictions (clinical)

**Source kind:** `AdultPatient` (≥ 18 at `Γ_time`).
**target Context:** `JurisdictionY` uses ≥ 21.

**KindBridge:** `AdultPatient ↦ AdultPerson_Y` with boundary mismatch; **`CL^k=1`**.
**Loss notes:** “Boundary 18 vs 21; map narrows to ≥ 21”.
**Guard:** Require **mask adapter** or **narrow Scope** to cohorts where DOB is known and ≥ 21. **R** penalty strong; **F/G** remain as declared.


### C.3.3:10 - Anti‑patterns & Remedies (informative)

| Anti‑pattern                                 | Why it’s wrong                         | Remedy                                                                              |
| -------------------------------------------- | -------------------------------------- | ----------------------------------------------------------------------------------- |
| One “interop score” for both kind & scope    | Blurs channels; corrupts penalties     | Use **two bridges**; apply **Φ(CL)** (Scope) and **Ψ(`CL^k`)** (Kind) **separately** |
| Claiming preserved `⊑` while inverting order | Makes typed reasoning unsound          | Mark as **not preserved**; add **loss note**; consider adapter or subkind redesign  |
| Hiding collapses                             | Overstates coverage                    | List collapsed subkinds explicitly; plan extra **R** for lost granularity           |
| “Latest mapping”                             | Non‑deterministic; non‑auditable       | Version bridges; bind to Standards/versions; **fail closed** outside definedness    |
| Using KindBridge to widen G                  | Conflates describedEntity with applicability | Keep Scope edits in **USM** (ΔG±); KindBridge never widens Scope                    |
| Adjusting F/G for poor `CL^k`                 | Violates F–G–R & USM separation             | Route consequences to **R** only; consider narrowing Scope or adding adapters       |


### C.3.3:11 - Conformance Checklist (normative)

| ID        | Requirement                                                                                                                                          |
| --------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- |
| **KB‑01** | A KindBridge **maps** `KindSignature`(s) and an explicitly declared subset of `⊑` links.                                                             |
| **KB‑02** | A KindBridge **MUST NOT** map Scope; Scope uses USM Bridge (Part B).                                                                                 |
| **KB‑03** | Bridge records **SHALL** include Contexts/versions, kind mapping/rules, order‑preservation claims, **`CL^k`**, **loss notes**, and **definedness area**. |
| **KB‑04** | Mapping **MUST** be **deterministic** given fixed versions/rules (no “latest”).                                                                      |
| **KB‑05** | Preserved order links **MUST** stay **monotone**: `k₁ ⊑ k₂` ⇒ `translateₖ(k₁) ⊑′ translateₖ(k₂)`.                                                    |
| **KB‑06** | **No inversions**: preserved links cannot invert order; otherwise mark **not preserved** and add loss notes.                                         |
| **KB‑07** | **Collapses** are allowed but **MUST** list merged subkinds and lost properties.                                                                     |
| **KB‑08** | **`CL^k`** **SHALL** reuse CL anchors and be labeled **“kind‑congruence.”**                                                                           |
| **KB‑09** | **Penalties:** when classification uses KindBridge, apply **Ψ(`CL^k`)** to **R**; **MUST NOT** adjust **F/G**.                                        |
| **KB‑10** | **Chaining:** effective `CL^k` across a chain is **min** (weakest‑link).                                                                              |
| **KB‑11** | **Loss notes** **SHALL** enumerate non‑preserved invariants and collapsed subkinds.                                                                  |
| **KB‑12** | **Definedness:** bridge **SHALL** state its valid area; guards **fail closed** outside it.                                                           |

**Integration requirements with Part B (bridges):**

* **B‑P1.** Part B (Bridges) **SHALL** list **KindBridge** as a distinct bridge class alongside USM Scope bridges.
* **B‑P2.** Part B **SHALL** state that **`CL^k` penalties route to R** via a monotone **Ψ**, never to **F/G**.
* **B‑P3.** Part B **SHALL** define **chaining = min** for both **CL** and **`CL^k`** (weakest‑link).
* **Templates.** ESG/Method templates should expose fields for **Scope Bridge (CL)** and **KindBridge (`CL^k`)** with loss notes & definedness.

### C.3.3:End

## C.3.4 - RoleMask — Contextual Adaptation of Kinds (without cloning)

> **One‑line summary.** Defines **`U.RoleMask(kind, Context)`** as a **context‑local adaptation** of a `U.Kind` that (a) adds **constraints** and/or **vocabulary bindings**, and (b) may **narrow** membership **deterministically** within a `U.ContextSlice`, **without creating a new kind**. RoleMasks are catalogued, versioned, and guard‑addressable; frequent, stable constraint masks **SHOULD be promoted** to explicit **subkinds**. Cross‑context use of a RoleMask requires a **KindBridge** (for kinds) and, when needed, a **MaskAdapter** (for mask constraints). All penalties route to **R**; **F/G** remain unchanged.


**Status.** Normative in **Part C**. Identifier **C.3.4**.
**Audience.** Engineering managers, architects, reviewers, editors.

**Depends on.**

* **C.3.1 — U.Kind & SubkindOf (Core):** kinds are intensional; `⊑` is a partial order; kinds **carry no Scope**.
* **C.3.2 — KindSignature (+F) & Extension/MemberOf:** signature F; deterministic `MemberOf(e,k,slice)`; `EntitySet(slice)`.
* **C.3.3 — KindBridge & CL^k:** Cross‑context kind mapping; `CL^k` penalties → **R** only.
* **A.2.6 — USM (Context slices & Scopes):** Claim/Work scope (**G**) over `U.ContextSlice`; bridges and **CL** for scope.
* **C.2.2 — F–G–R; C.2.3 — U.Formality (F).**

**Non‑goals.**
— No repository/notation mandates; conceptual only.
— RoleMask is **not** a governance tier, data policy, or “mini‑type system.”
— RoleMask does **not** redefine Scope; context conditions belong to **USM**.

### C.3.4:1 - Purpose (manager’s view)

Teams often need a **local projection** of a widely used kind:

* **Constraint:** “For our procedure, take `Vehicle` **with ABS** only.”
* **Vocabulary:** “Here, `AuthHeader` is called `X‑Auth`.”

If each team clones a fresh kind, catalogs fragment and bridges multiply. **RoleMask** is the disciplined alternative: **keep the kind identity**, apply **declared constraints and bindings**, and make the mask **first‑class** (registered, versioned, guard‑addressable). When a mask becomes stable “de‑facto subkind,” **promote** it to `⊑`.

**Benefits:** fewer near‑duplicates, cleaner Cross‑context reuse, deterministic guards, and auditable narrowing instead of hand‑wavy “this is the version we mean.”


### C.3.4:2 - Context

Kinds (C.3.1/3.2) name **what** claims quantify over; USM (A.2.6) governs **where** claims hold. In practice, procedures need **local tailoring** of kinds for a role/process (compliance profile, product line, cohort). RoleMask gives that tailoring **without** mutating describedEntity (Kind) or applicability (Scope).


### C.3.4:3 - Problem

1. **Kind sprawl.** Teams mint near‑duplicate kinds (“Account\_PCI”, “Account\_Ledger”), and alignment decays.
2. **Hidden constraints.** Informal “we only accept …” statements leak into prose; guards can’t check them deterministically.
3. **Scope conflation.** Contextual requirements (jurisdiction, API version) get smuggled into “type” talk, blurring Scope vs Kind.
4. **Cross‑context fragility.** Masks don’t travel unless their constraints are mapped; teams reuse names and hope.


### C.3.4:4 - Forces

| Force                                   | Tension to resolve                                                                                           |
| --------------------------------------- | ------------------------------------------------------------------------------------------------------------ |
| **Local specialization vs common core** | Need Context‑specific tailoring **without forking** kinds.                                                      |
| **Expressivity vs determinism**         | Masks must express real constraints **and** be **deterministically checkable** at guard time.                |
| **Context vs entity constraints**       | Conditions over **ContextSlice** (Scope) vs conditions over **entities** (membership) must be split cleanly. |
| **Reuse vs proliferation**              | Encourage reuse and promotion to subkind when stable; avoid a mask zoo.                                      |


### C.3.4:5 - Solution — **RoleMask** (overview)

A **RoleMask** is a **named, versioned binding** `U.RoleMask(kind, Context)` that:

1. **Adds constraints** (entity‑level predicates only),
2. **Binds vocabulary/notation** (aliases, field maps) for the Context/process,
3. **May declare context expectations** (selectors over `U.ContextSlice`, e.g., jurisdiction, API version). **These are enforced via USM Scope guards** (A.2.6) and **do not** change mask membership.
4. **May narrow membership**: `Extension_mask(k, s) ⊆ Extension(k, s)` (entity‑level narrowing only),
5. **Never creates a new kind**; identity stays with `k`.
6. **Is guard‑addressable** and **deterministic** (no “latest”).

**Mask types (declared):**

* **Constraint mask** — adds constraints; may narrow membership;
* **Vocabulary mask** — aliases only; no membership change;
* **Composite mask** — both.

**Separation discipline.**

* **Entity‑level predicates** (e.g., “hasABS(x)”) → **mask membership** (narrowing).
* **Context conditions** (e.g., “jurisdiction=EU”, “API=v2.3”) → **USM Scope** guards (intersection), **not** mask membership.
  Masks **may carry both kinds** of information, but guards must route them into the **right channel**.


### C.3.4:6 - Norms & Invariants (normative)

> The following formalize and expand **RM‑01…RM‑08** referenced in C.3.

#### C.3.4:6.1 - Definition & Shape

**RM‑01 (Definition).** `U.RoleMask(kind, Context)` **SHALL** be a named, versioned record with:
(a) **intent** (what role/procedure the mask serves),
(b) **constraints** (entity‑level predicates; optional context requirements),
(c) **vocabulary/notation bindings**,
(d) **membership narrowing** definition (if any),
(e) **intended guard use**.

**RM‑02 (Not a new kind).** A RoleMask **MUST NOT** introduce a new `U.Kind`. If the domain needs a stable refinement, Contexts **SHALL** publish an explicit `SubkindOf` node (C.3.1).

**RM‑03 (Determinism).** Membership under a mask (if defined) **MUST** be **deterministic** given `slice` and published constraints; implicit “latest” is forbidden.

**RM‑04 (Mask taxonomy).** A mask **SHALL** declare its type: **constraint / vocabulary / composite**.
— **Vocabulary masks** MUST NOT change membership;
— **Constraint/composite masks** MAY narrow membership **only via entity‑level predicates**.

#### C.3.4:6.2 - Separation of channels

**RM‑05 (Context vs entity).**

* Predicates about **entities** (features, attributes) MAY narrow membership: `Extension_mask(k, s) ⊆ Extension(k, s)`.
* Predicates about **ContextSlice** (jurisdiction, Standards, Γ\_time) **SHALL** be enforced via **USM Scope** guards (A.2.6). Masks **MUST NOT** hide Scope requirements inside membership checks.

**Guard routing.** Enforce ContextSlice predicates via **USM Scope** (A.2.6) and entity predicates via **membership**; see **Annex C.3.A §4.3 (Guard_MaskedUse)** and **§5 (E‑01)** for the normative order of checks.

**RM‑06 (Guard use).** Guards **MAY** reference a RoleMask by name **only** if the mask is **registered, versioned, and its constraints are observable** at guard time. Mask names **MUST NOT** be treated as kind synonyms.

#### C.3.4:6.3 - Promotion & Catalog

**RM‑07 (Promotion rule).** A constraint mask reused broadly and stably **SHOULD** be promoted to an explicit **subkind** with a `⊑` link; retire the mask or keep it as a vocabulary wrapper. Editors **SHALL** track promotions in the catalog.

**RM‑08 (Catalog).** Contexts **SHALL** catalog masks (name, version, type, intent, constraints, bindings, examples, related subkinds, known bridges/adapters). Redundant masks **SHOULD** be consolidated.

#### C.3.4:6.4 - Cross‑context use

**RM‑09 (Bridges & adapters).** If a claim uses `MemberOf(–, RoleMask(k), TargetSlice)` across Contexts, the receiving Context **SHALL** require:
(a) a **KindBridge** for `k` (`CLᵏ`, loss notes), and
(b) a **MaskAdapter** — a documented, deterministic mapping of the mask’s **entity‑level constraints** and **vocabulary bindings** into the target Context — whenever those constraints/bindings differ.
Penalties **MUST** route to **R**: `Ψ(CLᵏ)` for kind, plus any **Φ(CL)** for scope bridge.

**RM‑10 (Definedness & fail‑closed).** Mask evaluation **SHALL** state its definedness area; outside it, guards **fail closed**.


### C.3.4:7 - Invariants & Non‑goals (normative)

* **No Scope leakage.** RoleMasks **cannot** widen/narrow **Claim scope (G)**; any context conditions are enforced by USM guards.
* **Identity preservation.** The carrier kind remains `k`; RoleMask does not change describedEntity.
* **Weakest‑link unaffected.** RoleMasks do not alter weakest‑link rules on **F/R**; guards **route entity predicates to membership** and **context predicates to USM Scope**.

### C.3.4:8 - Interactions (informative)

#### C.3.4:8.1 - With Kinds & Subkinds (C.3.1)

Use RoleMask for **procedural tailoring**. If the tailoring becomes **conceptual** and stable, **introduce a subkind** with `⊑` and update references.

#### C.3.4:8.2 - With Membership & Signature (C.3.2)

* **Entity‑level constraints** live in mask membership (deterministic).
* **Signature F** belongs to the kind; raising F in the signature does not auto‑change masks.

#### C.3.4:8.3 - With KindBridge (C.3.3)

A RoleMask crossing Contexts needs **two artifacts**: the KindBridge (`CL^k`, loss notes) and a **MaskAdapter** (how constraints/aliases translate). **R** gets both penalties; **F/G** stay intact. If the adapter systematically narrows membership in the target Context, consider **target‑side subkind**.

#### C.3.4:8.4 - With Guards (Annex C.3.A)

Use **`Guard_MaskedUse`** (Annex **C.3.A §4.3**). It requires:
— mask registration & determinism;
— Scope coverage (A.2.6), **Γ\_time** explicit;
— where Cross‑context: KindBridge (`CL^k`) + MaskAdapter + penalties → **R**.
— **Cross‑context combo.** When masks cross Contexts, use **`Guard_MaskedUse`** together with **`Guard_XContext_Typed`** (Annex **C.3.A §4.5**) so both bridges are checked and both penalties (**Φ(CL)** and **Ψ(CLᵏ)**) land in **R**.
— **Order of checks.** Follow **Annex C.3.A §5 (E‑01)**: typed compatibility first, then Scope coverage, then penalties to **R** and freshness.

### C.3.4:9 - Anti‑patterns & Remedies (informative)

| Anti‑pattern                                      | Why it’s wrong                         | Remedy                                                                                |
| ------------------------------------------------- | -------------------------------------- | ------------------------------------------------------------------------------------- |
| Mask as “new type”                                | Duplicates kind; breaks alignment      | Keep the kind; if stable refinement → publish **subkind** (`⊑`).                      |
| Hiding Scope in mask membership                   | Conflates channels; non‑portable       | Move context conditions to **USM** guards; keep only entity predicates in membership. |
| Unregistered mask in guards                       | Non‑deterministic; un‑auditable        | Register & version the mask; fail closed otherwise.                                   |
| Cross‑context use without KindBridge/MaskAdapter     | Silent semantic drift                  | Require **KindBridge** + **MaskAdapter**; apply `Ψ(CL^k)` and any `Φ(CL)` to **R**.    |
| Mask proliferation (ten masks that mean the same) | Catalog entropy; inconsistent behavior | Consolidate; promote frequently used constraints to **subkinds**.                     |
| Treating mask name as kind synonym                | Hides constraints; invites misuse      | In prose, say “`RoleMask(k, name)`”; in guards, reference mask fields explicitly.     |


### C.3.4:10 - Worked Examples (informative)

#### C.3.4:10.1 - `Vehicle@ABSOnly` (constraint mask)

**Kind.** `Vehicle` (K2, signature F4).
**Mask.** `Vehicle@ABSOnly` — entity‑level predicate `hasABS(x)=true`; type **constraint**.
**Guards.** `MemberOf(–, Vehicle@ABSOnly, TargetSlice)` defined & deterministic; **Scope** (surface/speed/rig/Γ\_time) checked separately.
**Promotion?** If ABS‑only becomes a conceptual category, publish `VehicleWithABS ⊑ Vehicle` and retire the mask.

#### C.3.4:10.2 - `AuthenticatedRequest@Frontend` (vocabulary mask)

**Kind.** `AuthenticatedRequest` defined by `AuthStandard v2.3`.
**Mask.** `@Frontend` binds `authHeader → X‑Auth` (aliases only); **no** narrowing; type **vocabulary**.
**Cross‑context.** If reused in another Context, require **KindBridge** for the kind; **no** MaskAdapter needed (aliases are local).
**R.** Only scope bridge penalties apply (if any).

#### C.3.4:10.3 - `AdultPatient@Clinic` (composite mask) across jurisdictions

**Kind.** `AdultPatient` (≥ 18 at `Γ_time`).
**Mask.** `@Clinic`: entity constraint “DOB present”; context hint “EHR system = X” (this part routes to Scope). Type **composite**.
**Cross‑context.** Jurisdiction Y uses ≥ 21 → **KindBridge** with `CL^k=1`; **MaskAdapter** maps DOB fields.
**Guards.** Scope bridge (coding system) + KindBridge + MaskAdapter; penalties **Ψ(1)** (kind) + **Φ(CL)** (scope) to **R**.
**Outcome.** Allowed with reduced R; consider target‑side subkind `AdultPerson_Y`.


### C.3.4:11 - Authoring & Review Guidance (informative)

#### C.3.4:11.1 - Authoring a RoleMask card

**Fields (suggested).** `name`, `kind`, `type (constraint/vocabulary/composite)`, `intent`, `constraints (entity vs context split)`, `bindings`, `membership definition (if any)`, `definedness`, `examples`, `known bridges/adapters`, `promotion note`.
**Rules of thumb.**

* Keep entity predicates **small and testable**.
* Put **context** in Scope, not in membership.
* If ≥ 3 teams reuse the same constraint mask → **promotion** review.

#### C.3.4:11.2 - Reviewer 7‑point checklist

1. Mask **registered** and **versioned**?
2. **Type** declared correctly (constraint/vocabulary/composite)?
3. Entity vs context **split** respected?
4. **Determinism** (no “latest”) satisfied?
5. Guard **routes** context to **USM** and entity to **membership**?
6. Any Cross‑context use has **KindBridge** + **MaskAdapter** with penalties **to R**?
7. **Promotion** warranted (stable, reused) or consolidation needed?


### C.3.4:12 - Conformance Checklist (normative)

| ID        | Requirement                                                                                                                                                |
| --------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **RM‑01** | RoleMask **SHALL** be a named, versioned record with intent, constraints, bindings, membership definition (if any), and intended guard use.                |
| **RM‑02** | RoleMask **MUST NOT** introduce a new `U.Kind`; stable refinements **SHALL** be modeled as subkinds (`⊑`).                                                 |
| **RM‑03** | Mask membership (when defined) **MUST** be deterministic given `slice` and mask fields; implicit “latest” forbidden.                                       |
| **RM‑04** | Mask **SHALL** declare its type: constraint / vocabulary / composite; vocabulary masks **MUST NOT** change membership.                                     |
| **RM‑05** | Context conditions **SHALL** be enforced via **USM Scope** guards; membership narrowing **MAY** use entity predicates only.                                |
| **RM‑06** | Guards **MAY** reference a mask only if it is **registered, versioned**, and its constraints are **observable**; mask names **MUST NOT** be kind synonyms. |
| **RM‑07** | Frequently reused constraint masks **SHOULD** be **promoted** to subkinds; editors **SHALL** track promotions.                                             |
| **RM‑08** | Contexts **SHALL** catalog masks; redundant masks **SHOULD** be consolidated.                                                                                 |
| **RM‑09** | Cross‑context masked use **SHALL** declare a **KindBridge** (`CL^k`) and any **MaskAdapter**; penalties **MUST** reduce **R** only.                            |
| **RM‑10** | Mask definedness **SHALL** be stated; guards **fail closed** outside the defined area.                                                                     |

### C.3.4:End

## C.3.5 - KindAT — Intentional Abstraction Facet for Kinds (K0…K3)

> **One‑line summary.** Defines **KindAT** as an **informative facet** attached to `U.Kind` that classifies the **intentional abstraction stance** of a kind—**K0 Instance**, **K1 Behavioral Pattern**, **K2 Formal Kind/Class**, **K3 Up‑to‑Iso**—to **guide ΔF/ΔR planning, bridge expectations, catalog/search, and refactoring**. **KindAT is not a Characteristic**: it has **no algebra**, **no thresholds**, and **MUST NOT** appear in guards or composition math. All assurance remains in **F–G–R**; typed semantics remain in **C.3.1–C.3.4**.

**Status.** Mixed:
— **Informative** for the anchors, heuristics, examples, and guidance.
— **Normative** for the **usage rules** that forbid employing AT in guards/composition and constrain its placement.

**Placement.** Part C (Kinds), identifier **C.3.5**. Audience: engineering managers, architects, editors, assurance leads.

**Depends on.**
— **C.3.1** (`U.Kind`, `U.SubkindOf (⊑)`), **C.3.2** (`KindSignature` + F, `Extension/MemberOf`), **C.3.3** (KindBridge + `CL^k`), **C.3.4** (RoleMask).
— **A.2.6 USM** (Claim/Work scope over `U.ContextSlice`), **C.2.2 F–G–R**, **C.2.3 U.Formality (F)**.
— **MM‑CHR** distinction **Facet vs Characteristic** (editors).

**Non‑goals.**
— No numerical scale, no gating, no composition operators, no “quality” scoring.
— No effect on **F**, **G**, or **R** besides **planning hints**.

### C.3.5:1 - Purpose (manager’s view)

Teams constantly decide **how far to formalize** and **how broadly to validate**:

* *Are we speaking about **this cohort** (instances), about **things that behave like X** (pattern), about a **formal class** with invariants, or about objects **up to isomorphism**?*
* *Given that stance, should we invest in **F4 predicates**, **F7 proofs**, or **R** across variants?*
* *What kind of **KindBridge** is realistic (coarse mapping vs up‑to‑iso), and what **`CL^k`** should we expect?*

**KindAT** answers these with a **small, shared vocabulary (K0…K3)** that is **safe to use** (cannot distort F/G/R) yet **actionable** for planning and catalog/search.


### C.3.5:2 - Context & Rationale

#### C.3.5:2.1 - The orthogonality we preserve

* **G (Claim scope)** is **where** a claim holds (A.2.6).
* **Kinds** give **what** a claim is about (C.3.1/3.2).
* **R** is assurance (evidence, freshness, penalties).
* **F** is expression rigor (C.2.3).

Teams often **conflate abstraction with applicability** (“sounds general ⇒ applies broadly”) or **over‑engineer proofs** where **slice‑checks** suffice. AT separates these concerns.

#### C.3.5:2.2 - Why a facet, not a Characteristic

Per **MM‑CHR**, **Characteristics** (e.g., F, G) carry algebra and appear in guards/composition. **KindAT** is only a **tag** on `U.Kind`:

* **No algebra, no thresholds**, not used in guards.
* **Editorial placement** only: on kinds, not on claims.
* **Planning signal**: what ΔF and ΔR typically pay off; what bridge style to expect.

This keeps AT **useful** without risking a “second G” or back‑door quality scores.

#### C.3.5:2.3 - Design choice recap (moved from C.3 §15.2)

* Making AT a Characteristic would **duplicate** G’s role and encourage gating.
* As a **facet**, AT remains a **catalog/navigation and planning device**, not an assurance dimension.


### C.3.5:3 - **Anchors K0…K3** (informative)

> **How to read.** Each anchor states the **intentional stance** of the kind, **inclusion cues**, **non‑examples** (to prevent misuse), and **planning hints** (ΔF/ΔR/bridge expectations). Anchors are **context‑local editorial tags** on `U.Kind`.

#### C.3.5:3.1 - **K0 — Instance‑level**

**Intent.** The kind denotes **exemplars** or a **tightly curated set**; often a named cohort or a concrete template.
**Cues.** Membership relies on listing or direct identity features; little to no general invariants.
**Non‑examples.** Any kind with stable, general invariants belongs in **K2**.
**Planning hints.** Focus **R on TargetSlice** (executable checks, F5/6); avoid premature proof engineering. Bridges are **instance‑maps**; expect **low `CL^k`** outside the Context.

#### C.3.5:3.2 - **K1 — Behavioral Pattern**

**Intent.** The kind is a **role/behavioral** pattern (“things that act like …”), typically stated via Standards or controlled NL, not a full type.
**Cues.** “Duck‑typing” flavor; Standards reference behavior/state transitions.
**Non‑examples.** If you can state global invariants as predicates, consider **K2**.
**Planning hints.** Invest in **F3→F4** (predicate‑like acceptances); **R** must test **behavioral diversity**; bridges are **pattern maps** with moderate `CL^k`.

#### C.3.5:3.3 - **K2 — Formal Kind/Class**

**Intent.** A **formal class** with explicit **invariants/relations** (ontology class, type with Standards).
**Cues.** Predicate‑like signature, subkind lattice, invariants reviewed.
**Non‑examples.** Pure examples/cohorts (K0); informal roles (K1).
**Planning hints.** Raise **KindSignature F** to **F4+**, consider **F7** for safety‑critical cores; **R** should cover **subkinds/variants**; bridges are **type‑maps**, `CL^k` often medium/high.

#### C.3.5:3.4 - **K3 — Up‑to‑Iso**

**Intent.** Defined **up to isomorphism/equivalence** (category‑theoretic flavor; “equal as structure,” not by identity); equality‑as‑structure matters.
**Cues.** Statements invariant under isomorphism; reasoning by equivalence classes.
**Non‑examples.** Classes where identity matters beyond structure.
**Planning hints.** Expect **up‑to‑iso** bridges; `CL^k` can be high where equivalence is respected. **F7–F9** likely for key properties; **R** focuses on **witnesses of equivalence** at interfaces.

### C.3.5:4 - Manager Heuristics (informative)

| Decision area       | K0                               | K1                          | K2                                         | K3                                      |
| ------------------- | -------------------------------- | --------------------------- | ------------------------------------------ | --------------------------------------- |
| **ΔF investment**   | Prefer F5/6 executable semantics | F3→F4 acceptance predicates | F4→F7 (predicates/proofs)                  | F7→F9 (proof‑carrying, higher equality) |
| **ΔR design**       | Slice‑focused checks             | Behavioral diversity        | Variant/subkind coverage                   | Equivalence witnesses at boundaries     |
| **Bridge style**    | Instance map                     | Pattern map                 | Type map                                   | Up‑to‑iso / functorial                  |
| **Expected `CL^k`** | Low outside Context                 | Medium                      | Med/High                                   | High where iso holds                    |
| **Refactoring**     | Aggregate to K2 when stable      | Crystallize invariants → K2 | Maintain lattice; promote masks → subkinds | Keep iso constraints explicit           |


### C.3.5:5 - Misuse & Antidotes (informative)

* **“Higher AT ⇒ wider G.”** *Wrong.* **G** changes only via **ΔG** (USM). AT does not alter scope.
* **“Gate on AT.”** *Wrong.* Use **F** thresholds and scope/evidence guards; AT is never a gate.
* **“Depth in `⊑` ⇒ AT.”** *Wrong.* AT is about **intentional stance**, not graph depth.
* **“AT on claims.”** *Wrong.* AT tags **`U.Kind` only**.
* **“AT as quality score.”** *Wrong.* Use **F** and **R** for rigor/reliability.


### C.3.5:6 - **Usage Rules (normative)**

> These are the **only** normative constraints in this pattern. Everything else is guidance.

**AT‑01 (Facet, not Characteristic).** KindAT **SHALL** be treated as a **Facet** per MM‑CHR: it has **no algebra, no thresholds**, and **MUST NOT** appear in guards or composition math.

**AT‑02 (Placement).** If recorded, KindAT **SHALL** be attached to **`U.Kind`** (or its catalog card). It **MUST NOT** be attached to claims/capabilities or used as a proxy for **G**/**F**/**R**.

**AT‑03 (Editorial discipline).** Editors **SHALL NOT** write text implying “higher AT widens scope” or “higher AT increases rigor/reliability.” Any such text **MUST** be revised to reference **ΔG**/**F**/**R** explicitly.

**AT‑04 (Bridge neutrality).** **KindBridge** records **MUST NOT** compute or adjust AT; they may include *informative* remarks about likely anchor alignment. `CL^k` is independent of AT and is assessed from signature/order preservation.

**AT‑05 (Catalog).** Contexts that use AT **SHOULD** record it in **Kind catalog entries** alongside: signature snippet & **F**, subkinds, RoleMasks, KindBridges. Absence of AT implies **“not set”**, not K0.


### C.3.5:7 - Authoring & Review Guidance (informative)

#### C.3.5:7.1 - How to tag (fast rubric)

* If the card lists **concrete items/cohorts**, tag **K0**.
* If the card defines **behavioral obligations** in prose/templates but few global invariants, tag **K1**.
* If the card states **predicates/invariants** and participates in a **subkind lattice**, tag **K2**.
* If the card explicitly reasons **up to isomorphism**, tag **K3**.

#### C.3.5:7.2 - Review checklist (5 minutes)

1. Is the **carrier** a **`U.Kind`** (not a claim)?
2. Does the **tag** match the **signature** (intent)?
3. Are **ΔF**/**ΔR** implications noted for planning (not gating)?
4. Any **RoleMasks** that should be promoted to subkinds (K2 hygiene)?
5. Any **Cross‑context reuse** that suggests **bridge style** (pattern/type/iso)?


### C.3.5:8 - Integration Notes (informative)

* **With C.3.1/3.2 (Kinds, Signature, Extension).** AT guides *how* to evolve signature **F** and *what* R coverage is sensible; it **does not** change membership semantics.
* **With C.3.3 (KindBridge).** AT hints at likely **bridge style** (instance‑map / pattern‑map / type‑map / up‑to‑iso), but **`CL^k`** is still computed from signature/order preservation; penalties route to **R**.
* **With C.3.4 (RoleMask).** Persistent K1‑style masks often warrant **promotion to K2 subkinds**.
* **With A.2.6 (USM).** All scope decisions remain under **G**. AT text should never be used to infer coverage.
* **With C.2.3 (F).** AT does not raise/lower **F**; it **suggests** where raising F is cost‑effective.


### C.3.5:9 - Worked Mini‑Examples (informative)

* **K0 (Instance).** `Account_US_GAAP_2025_Q1_Cohort`. Plan **R** slice checks; avoid type‑maps across Contexts.
* **K1 (Behavior).** `CacheableRequest` (“idempotent under retry; cache key well‑formed”). Raise **F3→F4**; design **R** for failure‑mode diversity; expect **pattern bridges**.
* **K2 (Formal).** `Account` with invariants (balance = debits−credits; posting rules). Raise **F4+**; plan **R** over `Asset`/`Liability` subkinds; bridge via **type maps**.
* **K3 (Up‑to‑Iso).** `UndirectedGraph` up to node relabeling. Expect **up‑to‑iso bridges**; proofs at **F7+**; **R** checks interface equivalence witnesses.


### C.3.5:10 - Conformance Checklist (normative)

| ID        | Requirement                                                                                                   |
| --------- | ------------------------------------------------------------------------------------------------------------- |
| **AT‑01** | KindAT is treated as **Facet** (no algebra/thresholds); **MUST NOT** appear in guards/composition.            |
| **AT‑02** | AT **MUST** be attached to **`U.Kind`** only (if used); not to claims/capabilities.                           |
| **AT‑03** | Editorial text **MUST NOT** imply AT alters **F/G/R**; revise to name **ΔF/ΔG/ΔR** instead.                   |
| **AT‑04** | KindBridge **MUST NOT** compute/alter AT; `CL^k` is assessed independently.                                   |
| **AT‑05** | If a Context catalogs AT, it **SHOULD** include it in Kind cards with signature **F**, subkinds, masks, bridges. |

### C.3.5:End

## C.3.A - Typed Guard Macros for Kinds + USM (Annex)

> **One‑line summary.** Provides **normative guard macros** that combine **USM Scope** (A.2.6) with **Kind‑CAL** (C.3.x) so authors can gate state changes and compositions that **quantify over kinds** without conflating **describedEntity** (Kinds) with **applicability** (Scope **G**) or **assurance** (**R**). Includes **decision trees, anti‑patterns, and examples** (informative). **AT (KindAT)** is **never** used in guards.

**Status.** Mixed:
— **Normative**: guard macro clauses, evaluation order, fail‑closed discipline, conformance checklist.
— **Informative**: …  decision trees, anti‑patterns, worked examples, macro skeletons.

**Placement.** Part C (Kinds), identifier **C.3.A** (Annex). Audience: engineering managers, editors, reviewers, assurance leads.

**Depends on.**
— **A.2.6 USM**: `U.ContextSlice`, `U.ClaimScope` (**G**), `U.WorkScope`, ∈/∩/**SpanUnion**/translate, **Γ\_time** policy, Bridge + **CL** (scope).
— **C.3.1**: `U.Kind`, `U.SubkindOf (⊑)`; **C.3.2**: `KindSignature` (with **F**) and `Extension/MemberOf`; **C.3.3**: **KindBridge** + `CL^k` (kind‑congruence) & loss notes; **C.3.4**: **RoleMask**.
— **C.3.5**: **KindAT** (facet) — **explicitly forbidden** in guards.
— **C.2.2 F–G–R**: weakest‑link, penalties to **R** only; **C.2.3 F**: F0…F9 (expression rigor).
— **Part B Bridges & CL**: scope bridge semantics and CL ladder.

### C.3.A:1 - Purpose & Audience

**Purpose.** Give Contexts a **single set** of guard shapes to:
(a) **admit** typed claims safely,
(b) **compose** typed claims/specs,
(c) **use** RoleMasks properly, and
