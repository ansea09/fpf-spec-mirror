---
chunk_kind: "child"
pattern_id: "E.17.0"
pattern_title: "U.MultiViewDescribing — Viewpoints, Views & Correspondences"
section_id: "E.17.0:4"
section_title: "Solution — U.MultiViewDescribing as the universal multi‑view scaffold  (normative core)"
source_path: "FPF-Spec.md"
output_path: "by_section/E.17.0/E.17.0__005_solution-u-multiviewdescribing-as-the-universal-multi-view-scaffold-normative-core.md"
commit_sha: "a0c90e3bbfcc0285893cc5bb9d4a88fcd224f00e"
heading_path:
  - "E.17.0 — U.MultiViewDescribing — Viewpoints, Views & Correspondences"
  - "E.17.0:4 — Solution — U.MultiViewDescribing as the universal multi‑view scaffold  (normative core)"
line_start: 61568
line_end: 61775
dependencies:
  - "A.6.2"
  - "A.6.3"
  - "A.6.4"
  - "A.7"
  - "B.5"
  - "C.2.1"
  - "E.10"
  - "E.10.D1"
  - "E.10.D2"
  - "E.17"
  - "E.17.1"
  - "E.17.2"
  - "E.18"
  - "E.TGA"
  - "U.EffectFreeEpistemicMorphing"
  - "U.EpistemeSlotGraph"
  - "U.EpistemicRetargeting"
  - "U.EpistemicViewing"
  - "U.ViewpointBundleLibrary"
keywords:
---

### E.17.0:4 - Solution — `U.MultiViewDescribing` as the universal multi‑view scaffold  *(normative core)*

#### E.17.0:4.1 - Overview

`U.MultiViewDescribing` organises **families of Description epistemes and specification-use Description epistemes** for a shared entity of concern into a multi‑view structure with:

* **explicit viewpoints** (`U.Viewpoint`) as specifications of stakeholder families, concerns, allowed Description kinds and specification-use gates, and conformance rules;
* **episteme-lane views** (`U.View = U.EpistemeView`) as view-epistemes over those Description epistemes and specification-use cases;
* a **CorrespondenceModel** capturing correspondences between Description epistemes, including Description epistemes admitted for specification use and their views across viewpoints.

The pattern's EntityOfConcern class is explicit:

> **EntityOfConcern class:** `EntityOfConcernClass ⊑ U.Entity` — the class of entities of concern
> (typical species: `U.Holon` for engineering holons, `U.Morphism` for morphism publication, `U.Episteme` for meta-describing epistemes).

All members of a `U.MultiViewDescribing` family for that EntityOfConcern class share:

* `EntityOfConcernSlot` value in that `EntityOfConcernClass`, and
* a `BoundedContextRef` (E.10.D1) forming a **DescriptionScope** together with the entity.

Informally:

* Fix an entity `T ∈ EntityOfConcernClass` and a bounded context `C`.
* The **multi‑view family** for `<T,C>` consists of a set of `…Description` / `…Spec` epistemes, each under a declared viewpoint, plus their `U.View` views, together with a correspondence model relating them.

#### E.17.0:4.2 - Core constructs

##### E.17.0:4.2.1 - `EntityOfConcernClass` and DescriptionScope

1. **EntityOfConcernClass.**
   A `U.MultiViewDescribing` instance declares an `EntityOfConcernClass ⊑ U.Entity` that acts as a **species constraint** on the ValueKind of `EntityOfConcernSlot`.

   * In engineering species (TEVB) this is typically `U.Holon` restricted to `U.System` or `U.Episteme`.
   * In MVPK, `EntityOfConcernClass = U.Morphism`.

2. **DescriptionScope (informal).**
   For a fixed `T ∈ EntityOfConcernClass` and `C : U.BoundedContext`, the **DescriptionScope** `Scope(T,C)` is the notional scope under which:

   * all Description epistemes and specification-use Description epistemes have `EntityOfConcernRef = T` and `BoundedContextRef = C` in their DescriptionContext;
   * all views (`U.View`) attached to this family preserve that `EntityOfConcernRef` and `BoundedContextRef` (for Description-derived or specification-use-derived views).

   Formal USM treatment of `U.DescriptionScope` is fixed in E.10/publication-face/form discipline; here we only rely on the intuition “**we are describing this thing, in this context**”.

##### E.17.0:4.2.2 - `U.Viewpoint` (viewpoint specification)

`U.Viewpoint` is already introduced in C.2.1 as the ValueKind of `ViewpointSlot`; E.17.0 fixes its **internal structure** for describing families.

**Definition (normative).**
A `U.Viewpoint` is a viewpoint specification:

* `EntityOfConcernClassSpec ⊑ U.Entity` — the class of entities this viewpoint is defined for (must be compatible with the family’s `EntityOfConcernClass`);
* `StakeholderFamilies : FinSet(U.RoleEnactor)` — stakeholder / RoleEnactor families the viewpoint speaks for (e.g. “safety engineers”, “operations teams”).
* `Concerns : FinSet(U.Concern)` — concern set (qualities, risks, requirements) that matter under this viewpoint.
* `AllowedEpistemeKinds : FinSet(U.EpistemeKindId)` — which Description-episteme kinds and Description-episteme kinds admitted for specification use are admissible as **primary descriptions** and as **derived views** under this viewpoint (e.g. system-behaviour description, test harness spec, safety case, CG-Spec slice).
* `ConformanceRules` — a structured bundle of rules/tests describing when a Description episteme, Description episteme admitted for specification use, or view **conforms** to the viewpoint, including:

  * minimal content requirements (e.g. “must cover all safety‑critical functions”),
  * admissible `U.EpistemicViewing` pipelines to derive views from base descriptions,
  * allowed degrees of incompleteness and evidence requirements (link to GateProfiles/`OperationalGate(profile)` checks and Part F harnesses).

**Slot alignment.**

* `ViewpointSlot` has ValueKind `U.Viewpoint`, RefKind `U.ViewpointRef`; episteme fields are named `viewpointRef : U.ViewpointRef?`.
* For Description epistemes, including Description epistemes admitted for specification use in a `U.MultiViewDescribing` family, `viewpointRef` is **mandatory** as part of `DescriptionContext`.

##### E.17.0:4.2.3 - `U.View` (episteme-lane views)

`U.View` is an alias for `U.EpistemeView`, a species of `U.Episteme` whose kind includes:

* `ClaimGraphSlot` (often a sliced or projected ClaimGraph),
* `EntityOfConcernSlot`,
* `ViewpointSlot`,
* `ReferenceSchemeSlot` (and usually a `RepresentationSchemeSlot` in C.2.1+).

Normatively:

* A `U.View` in `U.MultiViewDescribing` is obtained via a `U.EpistemicViewing` morphism from some base Description episteme or Description episteme admitted for specification use in the family (see 4.3). It **shares the same `entityOfConcernRef`** and usually the same `BoundedContextRef`.
* `ViewSlot` is reserved for **references to such views** in meta‑structures (e.g. correspondence models, MVPK view families), never for carriers.

##### E.17.0:4.2.4 - `U.CorrespondenceModel` (view–view correspondence)

`U.CorrespondenceModel` is an episteme (typically a `U.EpistemeCard`) whose ClaimGraph expresses **correspondence relations between Description epistemes, including Description epistemes admitted for specification use and/or views** within a DescriptionScope:

* cross‑viewpoint correspondences (e.g. “this safety requirement is realised by this design element”),
* structural/behavioural consistency conditions (BX‑style consistency relations),
* change‑impact links (which views must be revisited when some view changes).

`CorrespondenceModel` is **used, but not defined, by A.6.3**: species of `U.CorrespondenceEpistemicViewing` reference it when computing views that depend on multiple epistemes or representation regimes.

#### E.17.0:4.3 - Multi‑view families and their rules/invariants (MVD‑0…MVD‑7)  *(normative)*

We now fix the rules and invariants that any `U.MultiViewDescribing[EntityOfConcernClass]` instance must satisfy.

##### E.17.0:4.3.0 - MVD‑0 - Family objects

For a fixed `EntityOfConcernClass` and bounded context `C`, a **multi‑view family** for an entity `T ∈ EntityOfConcernClass` consists of:

* a (finite) set `DescSpec(T,C)` of Description epistemes, including Description epistemes admitted for specification use such that for each `E ∈ DescSpec(T,C)`:

  * `E : U.Episteme` of some kind in `AllowedEpistemeKinds` of its viewpoint,
  * `subjectRef(E)` decodes to `DescriptionContext(E) = ⟨EntityOfConcernRef = T, BoundedContextRef = C, ViewpointRef(E)⟩`,
  * `viewpointRef(E)` lies in the family’s viewpoint set `Σ ⊆ FinSet(U.Viewpoint)`;
* a set `Views(T,C) ⊆ U.View` of view‑epistemes over those Description epistemes, including Description epistemes admitted for specification use, obtained by declared `U.EpistemicViewing` species (see MVD‑3);
* zero or more `U.CorrespondenceModel` epistemes over `{DescSpec(T,C), Views(T,C)}`.

Families are **scoped**: the same entity in a different `U.BoundedContext` belongs to a different family.

##### E.17.0:4.3.1 - MVD-1 - Viewpoint locality and totality for Description-episteme and specification-use cases

For any multi‑view family:

1. **Viewpoint-totality for Description-episteme and specification-use cases.**
   Each Description episteme or Description episteme admitted for specification use in `DescSpec(T,C)` **MUST** have a `viewpointRef` either:

   * explicitly populated, or
   * deterministically derived from a `U.ViewpointBundle` the family declares (see E.17.1).

   There are no “viewpoint-free” Description epistemes or Description epistemes admitted for specification use inside a `U.MultiViewDescribing` family.

2. **Viewpoint locality.**
   `ViewpointRef` values for `DescSpec(T,C)` must belong to a **finite viewpoint set `Σ`** declared for the family (locally or via a bundle). Cross‑family reuse happens **via bundles and Bridges**, not by silently sharing viewpoints across unrelated scopes.

3. **DescriptionContext alignment.**
   `DescriptionContext(E)` for any Description episteme or Description episteme admitted for specification use in the family must use the **same `EntityOfConcernRef` and `BoundedContextRef`** as the family; any change of EntityOfConcern or context is **outside this family** and must be expressed via `U.EpistemicRetargeting` and/or Context Bridges.

#### E.17.0:4.3.2 - MVD‑2 - Views are EpistemicViewing results

For any `V ∈ Views(T,C)`:

1. There exists a base episteme `E ∈ DescSpec(T,C)` and a morphism `v : E → V` such that:

   * `v` is a species of `U.EpistemicViewing`, i.e. an **effect‑free, entityOfConcern‑preserving** episteme morphism;
   * `entityOfConcernRef(V) = entityOfConcernRef(E) = T`,
   * `BoundedContextRef(V) = BoundedContextRef(E) = C`,
   * `viewpointRef(V)` is either:

     * the same as `viewpointRef(E)` (internal normalisation), or
     * a viewpoint in the same family `Σ`, with the change recorded in the family’s `CorrespondenceModel` (see MVD‑4).

2. No view may be introduced “out of thin air”: every `U.View` in the family is traceable to at least one Description episteme or Description episteme admitted for specification use (or a finite diagram thereof) via a **documented EpistemicViewing pipeline**.

3. Views **do not introduce new EntityOfConcern commitments** about `T` beyond what is licensed by EFEM & EpistemicViewing invariants (no new atomic claims about the same EntityOfConcern). Upgrading the EntityOfConcern-side commitment requires a new Description episteme or Description episteme admitted for specification use under A.7 and E.10.D2, not a view.

#### E.17.0:4.3.3 - MVD‑3 - Applicability profiles for viewings

Any EpistemicViewing species used inside `U.MultiViewDescribing` **MUST**:

* declare an Applicability profile as per EV‑6: permitted `EntityOfConcernClass`, grounding, viewpoint ranges, and representation schemes;
* for Description epistemes, including Description epistemes admitted for specification use in a family:

  * **preserve** `EntityOfConcernRef` and `BoundedContextRef` of `DescriptionContext`,
  * either preserve `ViewpointRef` or change it **within the family’s viewpoint bundle**, with constraints recorded in `CorrespondenceModel`,
  * never widen ClaimScope beyond EFEM/EpistemicViewing allowances.

Any change of EntityOfConcern (even “small”, e.g. subsystem→system) must be expressed via `U.EpistemicRetargeting` and is **not** a MultiViewDescribing view refinement.

#### E.17.0:4.3.4 - MVD‑4 - CorrespondenceModel for cross‑view correspondences

When views or Description epistemes, including Description epistemes admitted for specification use under different viewpoints are meant to be **kept in correspondence** (in ISO 42010 or BX sense), the family **SHALL**:

1. Provide a `U.CorrespondenceModel` episteme whose `ClaimGraph` captures correspondences and consistency relations over `{DescSpec(T,C), Views(T,C)}`.

2. Ensure that any `U.CorrespondenceEpistemicViewing` that depends on multiple epistemes or representation schemes:

   * references that `CorrespondenceModel`, and
   * publishes witnesses (proof objects, trace links) that make diagrams commute up to declared isomorphism (oplax naturality allowed).

3. Treat temporary inconsistency explicitly: there may be states where some correspondences are violated; this is represented as **facts in the correspondence ClaimGraph**, not as hidden weakening of viewing invariants.

#### E.17.0:4.3.5 - MVD‑5 - Separation from publication (MVPK)

`U.MultiViewDescribing` is purely **epistemic**:

* Description epistemes, Description epistemes admitted for specification use, and views live entirely in Ep-space (`U.Episteme`);
* it does **not** define `publication face/form`/`interop publication form` kind, carriers, or rendering;
* MVPK (E.17) sits **on top**:

  * taking morphisms and/or Description epistemes, including Description epistemes admitted for specification use as input,
  * using `U.EpistemicViewing` plus publication‑specific viewpoints,
  * emitting `U.View` instances declared against `publication face/form`/`interop publication form` kind via publication-face/form discipline.

MultiViewDescribing therefore **does not re‑define EntityOfConcern-to-Description or specification-use refinement** (`Describe_EoC_DescEp` plus `specificationUseRef` when a neighbouring gate grants specification force) and does not introduce any `U.Work` on carriers; A.7 carries the describing boundary, A.6.2 and exact neighbouring gates carry specification-use refinement, and E.17 carries publication.

Explanation-facing renderings over the same source `U.Episteme` claims may later be classified by `ExplanationFaithfulnessProfile` on top of existing publication faces, but that profile does not create a second viewpoint calculus here. `U.MultiViewDescribing` continues to govern the epistemic distinction between viewpoints, views, and correspondences.

#### E.17.0:4.3.6 - MVD‑6 - EntityOfConcern and Description-episteme boundary and specification-use alignment

For any `U.MultiViewDescribing` instance:

1. Every `…Description` and `…Spec` episteme in the family must satisfy E.10.D2:

   * be an episteme with `DescriptionContext = ⟨EntityOfConcernRef, BoundedContextRef, ViewpointRef⟩`,
   * be linked to a unique EntityOfConcern via `isDescriptionOf`; when specification force is live, carry a `specificationUseRef` or exact granting-pattern/gate reference rather than a peer `isSpecOf` relation.

2. Viewings and correspondence operations **must not**:

   * collapse the EntityOfConcern for this describing use into the produced Description episteme or Description episteme admitted for specification use,
   * confuse Description epistemes or Description epistemes admitted for specification use with `publication face/form`/`interop publication form` kind or carrier rendering,
   * reinterpret EntityOfConcern without going through A.6.4 retargeting.

#### E.17.0:4.3.7 - MVD‑7 - Slot discipline

All constructs in this pattern **SHALL** respect `U.RelationSlotDiscipline`:

* SlotKinds (`EntityOfConcernSlot`, `ViewpointSlot`, `ViewSlot`, `GroundingHolonSlot`, `ClaimGraphSlot`, `ReferenceSchemeSlot`) and their ValueKinds/RefKinds follow A.6.5 and C.2.1.
* `*Slot` suffix is reserved for SlotKinds; `*Ref` for RefKinds/fields, never for Kinds or objects.
* MultiViewDescribing patterns **must not** invent parallel slot disciplines for relation positions; they reuse SlotKind as the notion of position.

