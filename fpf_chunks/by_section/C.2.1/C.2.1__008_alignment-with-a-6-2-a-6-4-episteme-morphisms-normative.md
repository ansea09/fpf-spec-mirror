---
chunk_kind: "child"
pattern_id: "C.2.1"
pattern_title: "U.Episteme - Epistemes and their slot relation"
section_id: "C.2.1:7"
section_title: "Alignment with A.6.2–A.6.4 (episteme morphisms)  (normative)"
source_path: "FPF-Spec.md"
output_path: "by_section/C.2.1/C.2.1__008_alignment-with-a-6-2-a-6-4-episteme-morphisms-normative.md"
commit_sha: "cf12b97913ff82ca8a45ba77d3658ad11e0fdeb6"
heading_path:
  - "C.2.1 — U.Episteme - Epistemes and their slot relation"
  - "C.2.1:7 — Alignment with A.6.2–A.6.4 (episteme morphisms)  (normative)"
line_start: 35340
line_end: 35408
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

### C.2.1:7 - Alignment with A.6.2–A.6.4 (episteme morphisms)  *(normative)*
`U.EpistemeSlotRelation` is the **slot-relation substrate** for the episteme morphism patterns:
* A.6.2 `U.EffectFreeEpistemicMorphing`
* A.6.3 `U.EpistemicViewing`
* A.6.4 `U.EpistemicRetargeting`

#### C.2.1:7.1 - Effect‑free episteme morphisms (A.6.2) over C.2.1
For any `f : X → Y` that is an instance of `U.EffectFreeEpistemicMorphing`:
* **Typed episteme values.**
  X and Y are `U.Episteme` instances realised as `U.EpistemeCard` / `U.EpistemeView` with at least the minimal core components:

  ```
  content            : U.ClaimGraph
  entityOfConcernRef : U.EntityRef      // EntityOfConcernSlot
  groundingHolonRef? : U.HolonRef       // GroundingHolonSlot
  viewpointRef?      : U.ViewpointRef   // ViewpointSlot
  referenceScheme?   : U.ReferenceScheme// ReferenceSchemeSlot (ByValue)
  ```

  Any additional C.2.1+ components (RepresentationScheme, Tokens, Carriers, Operations) are visible to A.6.2 only through their declared SlotKinds (A.6.5).
* **EntityOfConcernChangeMode characteristic.**
  `f` **MUST** declare a **`entityOfConcernChangeMode ∈ {preserve, retarget}`**:
  * `preserve` — `entityOfConcernRef(Y) = entityOfConcernRef(X)` and any change to `groundingHolonRef`/`viewpointRef` must be justified by Bridges/CorrespondenceModel, without changing the EntityOfConcernSlot value;
  * `retarget` — permitted only for A.6.4 species; see below; in this case the characteristic records an intentional change in the pair `<entityOfConcernRef, groundingHolonRef>` under a declared `KindBridge` in the appropriate ReferencePlane.

  This **EntityOfConcernChangeMode** is a CHR-style *characteristic* (A.17) on episteme morphisms, which points directly to `EntityOfConcernSlot`. Avoid introducing a separate “entityOfConcern” term alongside `EntityOfConcern`.

* **Component discipline.**
  P0–P5 from A.6.2 are read **directly** in terms of C.2.1 components:
  * purity ⇒ only C.2.1 components of Y may change; no Work/Mechanism side‑effects;
  * conservativity ⇒ claims in `content_Y` read via `referenceScheme_Y` about the new `<EntityOfConcern, GroundingHolon>` do not go beyond what already follows from `content_X` via `referenceScheme_X` under the declared EntityOfConcernChangeMode and Bridges;
  * functoriality ⇒ composition of such transformations respects the slot structure and ReferenceSchemes.

Any Ep→Ep pattern that operates on `U.Episteme` **MUST** state which C.2.1 slots it reads and which it may write, in terms of SlotKinds/ValueKinds/RefKinds (A.6.5), and then declare itself a species of A.6.2/3/4 as appropriate.

#### C.2.1:7.2 - EpistemicViewing (A.6.3) as entityOfConcern‑preserving projections

`U.EpistemicViewing` is the **EntityOfConcern-preserving** species of A.6.2. Over C.2.1 this means:
* `entityOfConcernRef(Y) = entityOfConcernRef(X)` — the same value in `EntityOfConcernSlot`.
* `groundingHolonRef` is preserved, or changed only within a fixed grounding context (e.g. normalising identifiers for the same lab or runtime).
* `viewpointRef` is either:
  * preserved (internal normalisation under the same viewpoint), or
  * replaced by another `U.ViewpointRef` *within* a `U.MultiViewDescribing` family (E.17.0), with invariants enforced by a CorrespondenceModel.
* `content` and `referenceScheme` are transformed **conservatively**: no new claim content about the same `EntityOfConcern` is introduced.

Typical examples:
* filtering or aggregating `U.ClaimGraph` to a view relevant for a stakeholder group;
* rendering a behavioural specification into a tabular or diagrammatic episteme under a publication viewpoint;
* normalising a logic‑heavy episteme into a more operational one, while keeping the same system EntityOfConcern and context.

In terms of SoTA, EpistemicViewing behaves like a **lens** or **optic** over C.2.1: a focus (SlotKinds for content/representation) is manipulated while the EntityOfConcern is fixed.

#### C.2.1:7.3 - EpistemicRetargeting (A.6.4) as EntityOfConcern-bundle retargeting on episteme morphisms

`U.EpistemicRetargeting` is the species of A.6.2 where **`entityOfConcernChangeMode = retarget`**.
It is always a **morphism between epistemes** (`f : X → Y` in `U.Episteme`), but the adjective “retargeting” refers **not** to the fact that an episteme is mapped to another episteme (this is true for all A.6.2 species), and **not** to a separate entityOfConcern, but specifically to the **change in the EntityOfConcern-bundle** classified by C.2.1:
* `entityOfConcernRef(Y) ≠ entityOfConcernRef(X)` — the value stored for `EntityOfConcernSlot` changes;
* a `KindBridge` must relate `Kind(entityOfConcernRef(X))` and `Kind(entityOfConcernRef(Y))`;
* `groundingHolonRef` may remain the same (e.g. same plant, different subsystem) or be transformed along a Bridge in the same ReferencePlane.

In practice, many retargetings operate on the **`EntityOfConcernSlot`/`GroundingHolonSlot` pair** (for example, when an episteme about a physical module is re-interpreted as an episteme about a function-holon realised in a different environment). The characteristic `entityOfConcernChangeMode` still classifies such morphisms by whether this pair is preserved or intentionally re-identified under a `KindBridge` and reference-plane policy; the episteme on the codomain side is just the usual A.6.2 codomain episteme.

Over C.2.1 this is used for:
* **functional vs structural reinterpretation** (e.g. an episteme about a physical module retargeted to an episteme about the function it realises; StructuralReinterpretation in E.18 becomes a species of A.6.4);
* **signal vs spectrum** transitions (Fourier-style moves where the `EntityOfConcernSlot` value changes from time-domain signal to frequency-domain representation but an invariant, such as energy, is preserved);
* **data vs model** transitions (e.g. retargeting an episteme about raw observations to an episteme about a learnt model, with an invariant such as likelihood or sufficient statistics).

C.2.1 ensures that these retargetings have a **clear domain `EntityOfConcernSlot` value and codomain `EntityOfConcernSlot` value** and that any such move is expressed as a morphism over well-typed slots, not as an unstructured rewrite of “subject” or “object” labels.

