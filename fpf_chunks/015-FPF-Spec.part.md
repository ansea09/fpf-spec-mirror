### E.17.2:End

## E.17 - Multi‑View Publication Kit (for Morphisms)

> **Tech‑name:** `U.MultiViewPublicationKit` (**MVPK**)  
> **Plain‑name:** Multi‑view publication kit (for morphisms)  
> **Signature (conceptual form):**  `MVPK : (U.Morphism, Σ_viewpoints) ↦ U.ViewFamily` with per‑viewpoint components
> `ViewObj_s : U.Object → U.ViewObj_s` and `Emit_s(-) : U.Morphism → U.ViewMorph_s`,
> such that `(ViewObj_s, Emit_s)` forms a functor `U → View_s(U)`. For each `s ⪯ t`, a **reindexing coercion**
> `PromoteView[s→t]_X : ViewObj_s(X) → ViewObj_t(X)` exists and is **natural in `X`**: for every `f : X → Y`,
> `PromoteView[s→t]_Y ∘ Emit_s(f) = Emit_t(f) ∘ PromoteView[s→t]_X` (see Laws §6.2).
> **Notation:** `Σ_viewpoints` is abbreviated as `Σ` where convenient.
> **Twin‑register aliases (naming discipline):**
> • **Tech:** `Emit_PlainView`, `Emit_TechCard`, `Emit_InteropCard`, `Emit_AssuranceLane`; `PromoteView[s→t]_-`.  
> • **Plain:** `PlainView(x)`, `TechCard(x)`, `InteropCard(x)`, `AssuranceLane(x)`; “Promote to *t*”.

> **USM binding (overview):** `PublicationScope` is a **USM‑class** object that parameterizes MVPK; see §5.0.  
> **Episteme level.** MVPK treats each face as a `U.View` in the sense of C.2.1/E.17.0 (species `U.EpistemeView`). For a morphism `f`, every `Emit_s(f)` is such a view whose `DescribedEntitySlot`/`DescriptionContext` target is `f : U.Morphism` and whose `viewpointRef` is a publication `U.Viewpoint` (`PublicationVPId`) drawn from a `U.ViewpointBundle` (E.17.1/E.17.2). Slot discipline (`ViewSlot`/`ViewRef`) is inherited from C.2.1/A.6.5 and is not redefined in MVPK.

### E.17:1 - Intent

Provide a **disciplined, compositional way to publish morphisms** (arrows) across multiple didactic faces (views/cards) **without adding semantics**, while keeping **viewpoints** (the specifications that constrain views) explicit and auditable. Authors get a small **view‑pack** that, when applied to any `U.Morphism` (including compositions), yields a **family of views** that commute with arrow composition and respect edition/measurement pinning (Part F/G).

### E.17:2 - Problem frame

* Teams routinely need several **faces** of the *same* arrow: a **Tech card** for the catalog, an **Interop card** for machine exchange, a **Plain view** for narrative, and an **Assurance lane** for evidence.    
* Informal “renderings” quietly **drift semantics**; **composite arrows** are often published piecemeal, breaking traceability; **evidence** forgets unit/scale/edition pins.    
* “View” and “viewpoint” are **blurred** in practice; authors conflate **publication** with **mechanism**.    
* L‑SURF requires **Surface token discipline**; Core allows only **PublicationSurface/InteropSurface**; faces are **…View / …Card / …Lane** (no ad‑hoc `…Surface` kinds). 

**MVPK** fixes this by making publication a **typed, functorial projection** from existing D/S‑epistemes via species of `U.EpistemicViewing` (A.6.3/E.17.0, A.7 §5.9/E.10.D2) subject to explicit **viewpoint specs** and **pinning guards**. **Part E is conceptual:** no machine‑exchange formats are specified here.

### E.17:3 - Problem

1. **Semantic drift in publication.** Unchecked “presentations” introduce claims not present in the D/S‑epistemes about the arrow (epistemes with `DescriptionContext = ⟨DescribedEntityRef, BoundedContextRef, ViewpointRef⟩` in the sense of E.10.D2/E.17.0).    
2. **Non‑compositionality.** Publishing `g∘f` yields surfaces that don’t match composing the surfaces of `f` and `g`.    
3. **View vs viewpoint confusion.** A single template is treated as “the view”, with no declared concerns or conformance rules.    
4. **Unpinned numbers.** Numeric claims lack unit/scale/reference‑plane and **edition pins** (Part F/G), undermining auditability.    

### E.17:4 - Forces

| Force | Tension |
| --- | --- |
| **Compositionality vs legibility** | Preserve arrow laws across views ↔ keep each view didactic and audience‑appropriate. |
| **Neutral naming vs domain idioms** | Use vocabulary stable across domains ↔ allow local templates (SOPs, APIs, checklists). |
| **Surface orthogonality (A.7)** | Publication must not mutate I/D/S semantics ↔ authors expect “rich presentations”. |
| **Evidence discipline** | Views must cite CG‑Spec/CHR anchors ↔ authors want compact cards. |

### E.17:5 - Solution — the **MVPK Kit**

#### E.17:5.0 - USM anchoring (normative)
* **PublicationScope (USM).** `U.PublicationScope` is defined in **USM** (A.2.6 §6.5) analogously to `U.WorkScope` and `U.ClaimScope` as a **set‑valued scope object** over `U.ContextSlice`. In MVPK, every emitted `U.View` SHALL declare a `U.PublicationScope` that bounds where that face is admissible.  
  * **Non‑overload rule.** `U.PublicationScope` MUST NOT encode viewpoint choice, MVPK profile selection, or Publication Characteristics (PC); those are governed by `PublicationVPId`/`U.Viewpoint` and MVPK profile rules (§5.1/§5.2/§5.5).
* **Scope lineage.** `U.PublicationScope` participates in the same USM lineage regime as `U.WorkScope`/`U.ClaimScope` (Δ‑moves, editioning and migration rules); MVPK emits faces **under** a declared `PublicationScopeId`.
* **MVPK profile (kit configuration).** The canonical MVPK profiles (MVPK‑Min/Lite/SetReady/Max) fix:
  * (a) the **viewpoint index** `Σ` and its partial order `⪯`,
  * (b) the admissible **Publication characteristics (PC)** and required **pinning contracts**,
  * (c) any cross‑Context/plane constraints (Bridge/CL policies) applicable to emitted faces.
* **L, P, D, E quartet.** The canonical MVPK‑Max profile enumerates exactly four **face kinds**: `PlainView (P)`, `TechCard (T)`, `InteropCard (I)`, `AssuranceLane (A)`. If a program elects to retain the mnemonic **(L, P, D, E)** tuple, it MUST map it 1‑to‑1 onto these **face kinds** and SHALL NOT introduce additional kinds without a USM extension.

#### E.17:5.1 - Terminology (normative)

* **View** (`U.View`): an episteme‑level view (`U.EpistemeView` in the sense of C.2.1/E.17.0) produced *under* a publication viewpoint. In MVPK each face (`PlainView`, `TechCard`, `InteropCard`, `AssuranceLane`) is such a `U.View` whose `DescribedEntitySlot`/`DescriptionContext` target is a `U.Morphism` and whose `viewpointRef` is a publication `U.Viewpoint`.  
  Every MVPK `U.View` **SHALL** declare:  
  `SurfaceKind ∈ {PublicationSurface, InteropSurface}`, `PublicationVPId : U.ViewpointRef`, references to the underlying D/S‑epistemes produced by `Describe_ID`/`Specify_DS` in A.7/E.10.D2, and a `U.PublicationScope` (USM §6.5).  
  Any materialization/rendering is separate **Work on SCR/RSCR carriers** and is not part of `U.View`.
* **Publication vs presentation vs rendering vs representation (guard):**    
    * **Publication** = typed projection from existing D/S‑epistemes about a morphism onto a `U.View`/`PublicationSurface` via species of `U.EpistemicViewing` (A.6.3) under the I/D/S discipline of A.7/E.10.D2.        
    * **Presentation** = rhetorical arrangement of a published carrier; **notation‑neutral**, adds no claims and is **not** a Surface kind.        
    * **Rendering** = display/layout of a carrier, purely graphical/formatting; **Work on carriers** (A.7), not a Surface kind.        
    * **Representation** = episteme↔referent relation (C.2.1/A.6.2–A.6.4); **not** a surface act. Use **publication** and **view** here; treat presentation/rendering as **Work on carriers** (A.7).
* **ISO mapping note.** ISO **viewpoint** → `PublicationVPId` (publication layer); **engineering viewpoint** → `EngineeringVPId` (E.TGA E.18:5.12). An ISO **view** may be a single MVPK face; “bundles” are packaging only.
* **No‑mechanism equivalence:** MVPK **is not** a mechanism; any operational toil (build/render/upload) is **separate Work by a system on carriers** (A.7; see **Laws 5 — No Γ‑leakage** in §6).
* **ViewpointSpec (`U.Viewpoint`)** — a typed specification that declares stakeholders, concerns, conformance rules, allowed **Publication Characteristics**, and pinning requirements per profile. The index set `Σ` consists of identifiers of `U.Viewpoint` instances, typically drawn from `U.ViewpointBundle` species (E.17.1/E.17.2) (see §5.3).

#### E.17:5.2 - Allowed surfaces at Part E (L‑SURF discipline)
Part E restricts the term *Surface* to **PublicationSurface** and **InteropSurface**. Concrete faces SHALL be named **…View / …Card / …Lane**. 

**USM linkage (normative).** Every `U.View` **SHALL** declare a `U.PublicationScope` (USM §6.5).  
For a view **about an episteme** `E`: `PublicationScope(view_E) ⊆ ClaimScope(E)`.  
For a view **about a capability** `C`: `PublicationScope(view_C) ⊆ WorkScope(C)`.  
Cross‑context views **SHALL** cite Bridge + CL; **CL penalties apply to R only** (scope membership unchanged).

**L‑PUBSURF naming discipline**
 * Allowed surface kinds: **PublicationSurface**, **InteropSurface**.
 * Concrete faces MUST be named **…View / …Card / …Lane**.
* The tokens **carrier/bearer/holder** MUST NOT name a `U.View` or any publication entity.  
  Use **`U.View`** (PlainView / TechCard / InteropCard / AssuranceLane) for conceptual publication faces.  
  Reserve **carrier** exclusively for **SCR/RSCR** (symbol/document/data carriers) and **Work on carriers**.
* Avoid geometric metaphors (axis/dimension) for publication artifacts; use **Characteristic/CharacteristicSpace** only when referring to CHR‑MM entities.
* **Non‑collision guard.** `ViewFamilyId` (lexical tag for viewpoint families) MUST NOT be used to name any `U.View` or surface kind; MVPK face kinds remain **{PlainView, TechCard, InteropCard, AssuranceLane}** only.

**MVPK‑Max viewpoints (normative; exactly four; governed by the MVPK profile):**
* `PlainView` (explanatory prose view)    
* `TechCard` (typed catalog card)    
* `AssuranceLane` (evidence bindings/lanes)
* `InteropCard` (conceptual interoperability view; **mapping to concrete exchange formats lives in Annex/Interop; Part E does not specify schemas**)

**Lean profiles (small‑team friendly, optional; as MVPK kit profiles):**
* **MVPK‑Min (F0–F1):** Σ = {`PlainView`, `TechCard‑Lite`}. `AssuranceLane` omitted. No interop face.
* **MVPK‑Lite (F1–F3):** Σ = {`PlainView`, `TechCard‑Lite`, `AssuranceLane‑Lite` gated by crossing trigger}. `InteropCard` only if external consumers exist.
* **MVPK‑SetReady (F3–F5):** add `InteropCard` when replayability or external interchange is required (details outside Part E).
* **Profile‑upgrade triggers:** (i) cross‑Context/plane reuse; (ii) QD/OEE replay needs; (iii) external consumption.
* **“‑Lite” variants (definition):** A *‑Lite* face removes optional fields only (never claims), keeps the same typing as its full counterpart, and MUST retain pins for any numeric content. Upgrading from *‑Lite* to full is a monotone **add‑fields** operation (no retractions).

#### E.17:5.3 - The kit (constructs)

1. **Object component** `ViewObj_s` for each viewpoint (see §5.1), to make types explicit.  
2. **Viewpoint set** `Σ : FinSet(U.Viewpoint)` with declared **partial order** `⪯` for formality/refinement (default chain: `PlainView ⪯ TechCard ⪯ InteropCard`; `AssuranceLane` is **orthogonal** and not ordered with respect to others).  
3. **Emitters** `Emit_s(-) : U.Morphism → U.ViewMorph_s` (one per `s ∈ Σ`).
4. **Coherence** (laws §6) + **Pin Characteristics** policy (UnitType/ScaleKind/ReferencePlane/EditionId) for any numeric/comparable content, grounded in CHR/UNM.    
5. **Interop anchors (conceptual)** for `InteropCard` (concerns/semantics only); **any concrete schema/exchange mapping is outside Part E** (Annex/Interop).

**Result:** `MVPK(f, Σ)` returns `U.ViewFamily(f)` whose components are `Emit_s(f)`. Reindexing across `s ⪯ t` is mediated by total object‑level coercions `PromoteView[s→t]_X` (see §6.2).

#### E.17:5.4 - Intensional I/O vs Publication (normative convention)
1) **I/O are intensional.** The **Input/Output** sections of a morphism describe **intensional** data types (I/D/S) only; they do **not** depend on any publication face.  
2) **No duplication on faces.** MVPK faces **do not duplicate** I/O lists; they publish a **minimal profile**: **presence‑pins**, **CG‑Spec/CHR anchors**, and **EditionId** only.  
3) **Signature reserved to intensional.** Use **“Signature”** exclusively for intensional objects (`U.Signature`, `U.PrincipleFrame`, …). On faces, avoid “signature” and use **TechName/PlainName**.  
4) **Lawful orders, return sets.** Whenever a face shows **selection or comparison**, it **returns sets / lawful partial orders** and **never hides scalarization**; cite a **ComparatorSetRef** for any total order.  
5) **Bridge routing, penalties.** Crossings go via **Bridge + CL**; publish **Φ(CL)/Φ_plane** ids; penalties route to **R only** (never F/G).  
6) **Carrier anchoring & lanes.** On first mention, anchor carriers (**SCR/RSCR**); keep **Work occurrences** distinct from **epistemic claims** via lanes.  
7) **Publication ≠ execution.** No time/resource semantics on faces; any build/render/upload is separate **Work**.

#### E.17:5.5 - Pin & Publication characteristics (normative; never “axes”)
**Intent.** Make pinning and publication‑time measurement claims explicit, typed, and auditable without importing geometric metaphors. This section introduces **Publication characteristics** (PC) as CHR‑grounded, publication‑level facets that can legally appear on MVPK faces.

**Terminology (aligned with CHR‑MM & UNM).**
* **Characteristic** (`U.Characteristic`): a measured aspect as defined in CHR‑MM (entity/relation characteristic with a chosen **Scale**).  
* **CharacteristicSpace** (`U.CharacteristicSpace`): a CHR‑typed product of slots used by dynamics/measurement theories (A.19).  
* **Publication characteristic** (`U.PubCharacteristic`, **PC**): a **declarative facet** that a view/card/lane may expose *about a morphism* under a stated **Viewpoint**. Each PC is **backed by** CHR/CG‑Spec artifacts and **pinned** by {unit/scale/reference‑plane/edition}. PCs are **not** geometry and do **not** define “axes”.

**PC catalog (initial set).** MVPK defines a minimal open set of PCs that are frequently surfaced:
* **PC.Number** — numeric/comparable entries (thresholds, budgets, counts). **Pins required:** unit, scale, reference‑plane, edition.  
* **PC.EvidenceBinding** — bindings to evidence carriers and policies (e.g., PathSliceId, BridgeId, CL notes).  
* **PC.ComparatorSetRef** — an explicit comparator family for lawful partial orders on faces.  
* **PC.CharacteristicSpaceRef?** — optional pointer when a face needs to cite the **space** in which a claim is interpreted (e.g., dominance on a declared space).  
The catalog **MAY** be extended (see “Extensibility” below); PCs **must** remain declarative (no embedded mechanisms).

**Norms (E17‑PC).**
* **E17‑PC‑1 (CHR grounding).** Every PC that yields numeric/comparable content **SHALL** cite CHR/CG‑Spec anchors and carry pins {unit, scale, reference‑plane, edition}.  
* **E17‑PC‑2 (Lexical discipline — no geometry).** Faces and PCs **MUST NOT** use “axis”, “dimension”, or geometric metaphors; use **Characteristic**, **slot**, **CharacteristicSpace** where applicable (**E.10**; see also A.19).  
* **E17‑PC‑3 (No hidden arithmetic).** Faces **MUST NOT** smuggle aggregation/normalization; any such logic lives in **CG‑Spec** (UNM/NormalizationMethod) and is cited by **…Ref.edition**.  
* **E17‑PC‑4 (Plane & crossing).** When a PC depends on **ReferencePlane** or crosses planes/contexts, the face **SHALL** cite `BridgeId` and **CL** policy‑ids; penalties route to the **R‑channel only**.  
* **E17‑PC‑5 (Edition pinning).** PCs that rely on maps or distances **SHALL** pin `DescriptorMapRef.edition`, `DistanceDefRef.edition`, and, if used, `CharacteristicSpaceRef.edition` / `TransferRulesRef.edition`.  
* **E17‑PC‑6 (Viewpoint scope).** Each PC instance declares the **Viewpoint** under which it is valid; promotion `PromoteView[s→t]` **MUST NOT** strengthen claims; at most, it reindexes or annotates.  
* **E17‑PC‑7 (Comparator/SetSemantics edition).** `PC.ComparatorSetRef` and any `SetSemanticsRef` **SHALL carry edition identifiers**; cards MUST be re‑emitted upon edition change with migration notes.

**Surfaces & responsibilities.**
* **PlainView** MAY include **PC.Number** iff fully pinned; otherwise it uses **compare‑only** language.  
* **TechCard** SHOULD carry **PC.Number**, **PC.ComparatorSetRef**, and **PC.CharacteristicSpaceRef?** when faces enable lawful ordering.  
* **AssuranceLane** SHALL carry **PC.EvidenceBinding** and the pins for any numeric claims it relays.  
* **InteropCard** MAY reference PCs conceptually but SHALL remain notation‑neutral in Part E (schemas map in Annex/Interop).

**Rationale.** MVPK is a publication discipline, not a measurement calculus. By naming **Publication characteristics** and pinning them to CHR/UNM, we:
1) prevent geometric leakage (no “axes”);  
2) keep publication neutral yet auditable;  
3) enable lawful set/ordering behavior on faces via explicit **ComparatorSet**;  
4) make plane/crossing obligations first‑class and checkable by declared publication checks / **OperationalGate(profile)** GateChecks.

**Extensibility.**
* **E17‑PC‑Ext‑1 (Open catalog).** New PCs MAY be added under `U.PubCharacteristic` provided they are declarative and CHR/UNM‑grounded.  
* **E17‑PC‑Ext‑2 (Kinding).** New PCs MUST declare `kind ∈ {Number, EvidenceBinding, SelectorHint, …}` and a **pinning contract**.  
* **E17‑PC‑Ext‑3 (Twin‑register names).** Supply **Tech** and **Plain** twins; avoid tokens that collide with E.10 bans; do not coin “…Space” names for publication artifacts.  
* **E17‑PC‑Ext‑4 (Edition discipline).** If a PC depends on a definitional artifact, **edition‑pin** the reference (`…Ref.edition`) and document migration rules.

**Adding invariants (procedure).**
1) Place **new invariants** for PCs in **CG‑Spec** (S‑layer), not on faces; supply acceptance tests.  
2) Version any affected **CharacteristicSpace**; publish embeddings if semantics change; never mutate slots in place.  
3) Update the relevant **GateChecks / GateProfiles** (A.21/A.26; incl. GateCrossing/CrossingSurface checks from **E.18/A.27**) to warn/block on invariant violations; never weaken functorial laws.
4) **Document** edition/migration rules; extend §9 with a conformance item and provide **Lean‑profile downgrade** (advisory vs block) where applicable.

#### E.17:5.6 - Author ergonomics (non‑normative)
*Quick path for authors (three steps and a micro‑template):*
1. **Declare Σ and profile.** Choose `{PlainView, TechCard, …}` and whether faces are full or *‑Lite*.
2. **Pin once, reuse everywhere.** Attach `{UnitType, ScaleKind, ReferencePlane, EditionId}` to the arrow; cards reference these pins by ID (no duplication).
3. **Emit & verify.** Generate all faces from the arrow.

*Guidance:* treat *‑Lite* as **field‑drop only**; never add claims in *‑Lite*. 

### E.17:6 - Laws (normative)

For any composable arrows `X —f→ Y —g→ Z` in `U`, and any `s, t ∈ Σ_viewpoints`:

1. **Functoriality & typing (per‑viewpoint).**  
    * (a) **Identity:** `Emit_s(id_X) = id_{ViewObj_s(X)}`.    
    * (b) **Composition:** `Emit_s(g∘f) = Emit_s(g) ∘ Emit_s(f)`.    
    * (c) **Typing (totality):** if `f : X → Y` then `Emit_s(f) : ViewObj_s(X) → ViewObj_s(Y)` is **total**; ill‑typed composites must be fixed via `ViewObj_s`, not by weakening laws.    
    * *Intuition:* every viewpoint acts functorially on arrows; publication does not break arrow algebra.
2. **Reindexing coherence (monotone refinement + naturality).**    
    * (a) If `s ⪯ t` then the `t`‑view **refines** the `s`‑view for the same morphism (**no content extension**; increased formality/typing only).    
    * (b) For each `s ⪯ t` there are **object‑components** `PromoteView[s→t]_X : ViewObj_s(X) → ViewObj_t(X)` natural in `X`, i.e., for every `f : X → Y`  
      `PromoteView[s→t]_Y ∘ Emit_s(f) = Emit_t(f) ∘ PromoteView[s→t]_X`.    
    * (c) **Coherence:** `PromoteView[s→s]_X = id_{ViewObj_s(X)}`, and if `s ⪯ t ⪯ u` then `PromoteView[s→u]_X = PromoteView[t→u]_X ∘ PromoteView[s→t]_X` for all `X`.         
    * *Defaults:* `PlainView ⪯ TechCard ⪯ InteropCard`.    
    * *Note:* `AssuranceLane` is **orthogonal** to the chain; it binds **evidence‑about‑claims** and MUST NOT introduce new claims **of** the morphism. 
3. **D/S sourcing & EpistemicViewing compatibility (A.7/E.10.D2, A.6.2–A.6.3, E.17.0).**    
    * (a) Inputs to `Emit_s(-)` are **existing D/S‑epistemes** about the same arrow (for example, `MethodDescription`, `MethodSpec`) produced by `Describe_ID` and `Specify_DS`/`Formalize_DS` in A.7/E.10.D2. MVPK does **not** redefine or collapse these I→D→S morphisms.  
    * (b) Each `Emit_s(-)` SHALL be realised as a species of `U.EpistemicViewing` (A.6.3) over those D/S‑epistemes: describedEntity‑preserving, effect‑free and conservative in the sense of A.6.2/A.6.3. Publication adds no new commitments beyond what is present in the referenced D/S‑epistemes.  
    * (c) Edition governance respects `U.EditionSeries`/UTS; rows remain the identity anchors for names; MVPK faces MUST be (re‑)emitted when the underlying D/S editions change.
4. **Pin discipline (Part F/G).**  
     * Any numeric/comparable content in a view SHALL pin {UnitType, ScaleKind, ReferencePlane}. **EditionId MAY be coarse at Lean profiles**; if units/scale are unknown, **declare ordinal/compare‑only** and **forbid arithmetic** until CHR pins are available.  Pins upgrade monotonically with profile and risk.
5. **No Γ‑leakage (publication independence).**  
    Publication morphisms carry **no** Γ\_method / Γ\_time / Γ_work semantics. Any build/render/upload toil is **separate Work by a system on carriers** (A.7).    
     **Lean assurance lane:** `AssuranceLane‑Lite` MAY expose only presence bits for {PathId/PathSlice?, Γ_time window?, BridgeId?}; unknowns propagate (tri‑state) with an explicit {degrade|abstain|sandbox} policy note.
6. **Carrier provenance.**  
    Every emitted view records its **SCR/RSCR ids** on first occurrence (A.7 §5.6).
7. **Isomorphism preservation.**    
    * If `f` is an isomorphism in `U`, then `Emit_s(f)` is an isomorphism in `View_s(U)`; inverses map accordingly.  
8. **Cross‑Context/plane bridging.**    
    * If a view crosses contexts or reference planes, it **SHALL** cite the **Bridge + CL policy ids** (A.7 §5.8, “Bridge routing”). Such crossings MUST be explicit on `TechCard` and `AssuranceLane`.
9. **Totality of publication morphisms.**    
    * Publication maps are total on their domains; when a composition in a view would be ill‑typed, the author **must** fix the object mapping (via `ViewObj_s`) rather than weakening functoriality or reindexing laws.
10. **PublicationScope discipline (subset & composition).**  
    * (a) **Subset law:** If a view `v` is about episteme `E` then `PublicationScope(v) ⊆ ClaimScope(E)`; if about capability `C` then `PublicationScope(v) ⊆ WorkScope(C)`.  
    * (b) **No widening by refinement:** If `s ⪯ t`, then promotion `PromoteView[s→t]` MUST NOT widen `PublicationScope`.  
    * (c) **Compositional bound:** For composable arrows `X —f→ Y —g→ Z`,  
      `PublicationScope(Emit_s(g∘f)) ⊆ PublicationScope(Emit_s(g)) ∩ PublicationScope(Emit_s(f))`.

### E.17:7 - Structure & participants
```
                 Σ_viewpoints
                      │
            ┌─────────┴─────────┐
            │                   │
        Emit_s(-)           Emit_t(-)      … (family)
            │                   │
U :  X ──f──▶ Y ──g──▶ Z    X ──f──▶ Y ──g──▶ Z 
        U.ViewMorph        U.ViewMorph
            │                   │
        Emit_s(f),…         Emit_t(f),…
```
* **Author** chooses `Σ_viewpoints` (declared concerns + conformance rules).    
* **MVPK** emits `U.ViewFamily(f)` for each arrow `f`.    
* **Gate‑based validation** (via declared publication checks / OperationalGate(profile) GateChecks) verifies that pins/anchors/IDs are present and that MVPK laws are respected.

### E.17:8 - Examples (SoTA‑echoing)

1. **Composite service pipeline (Interop + Assurance).**  
    `f: Parse → Normalize`, `g: Normalize → Score`.
    `InteropCard(g∘f)` is an interoperability **view** whose path set equals the **relational composition** of the two cards; `AssuranceLane(g∘f)` cites test artefacts as evidence **carriers** with edition pins. (Carriers, not semantics; concrete envelope formats are outside Part E.)
2. **Control loop morphism (Tech + Plain).**
    * For `h: Setpoint → Actuation`, `TechCard(h)` is a typed card with units; `PlainView(h)` narrates the same mapping with no new claims. (Monotone formalization echoes refinement‑typed stacks.)
3. **Optics‑style compositional views.**
    * Treat each `Emit_s(–)` as a **profunctor optic** from arrow semantics to its projection; then (by optics laws) `Emit_s(g∘f) = Emit_s(g) ∘ Emit_s(f)`. *Modern echo:* profunctor/optic literature (2017–2019) establishes precisely the kind of **compositional view** MVPK requires.  

### E.17:9 - Conformance checklist (normative)

| ID | Requirement | Practical test |
| --- | --- | --- |
| **CC‑MVPK‑0 (Lean publication guard)** | For Lean profiles, a minimal guard runs: (i) set‑returning selection present; (ii) ReferencePlane present; (iii) any crossing cites BridgeId+CL with penalties routed to R only. | Validation report shows presence bits; penalties route to R only. |
| **CC‑MVPK‑1 (Viewpoint explicit)** | Each view declares its **Viewpoint** (stakeholders, concerns, conformance) as a publication `U.Viewpoint`. | Cards show `PublicationVPId` (or equivalent publication‑viewpoint field) and concerns. |
| **CC‑MVPK‑2 (Functoriality)** | `Emit_s(id)` is identity; `Emit_s(g∘f) = Emit_s(g)∘Emit_s(f)`. | Compose two cards and diff with the card of the composite. |
| **CC‑MVPK‑3 (No content extension)** | `PlainView`, `TechCard`, and `InteropCard` add **no new claims** beyond the underlying D/S‑epistemes. | Red‑line vs D/S episteme output (`Describe_ID`/`Specify_DS`) shows only formatting/indexing. |
| **CC‑MVPK‑3b (Boundary claim‑set integrity)** | If a published arrow is a boundary/interface/protocol and an A.6.B routed claim set exists (`L-* / A-* / D-* / E-*`), then any normative text on faces **MUST** be traceable to that claim set (prefer claim‑ID citations); faces **MUST NOT** become a second contract. | Lint flags uncited normative clauses; faces reduce to {claim‑ID citations + informative commentary}. |
| **CC‑MVPK‑4 (Pins & anchors)** | Numbers/thresholds pin {… }. **Lean exception:** at MVPK‑Min/Lite profiles, EditionId MAY remain coarse; ordinal claims are legal only as compare‑only (no means/z‑scores). | Validation shows pins present or compare‑only mode engaged. |
| **CC‑MVPK‑4b (Lean assurance)** | If `AssuranceLane‑Lite` is used, presence bits for {PathSliceId?, BridgeId?} suffice; full artefact lists are deferred. | Presence bits visible; deferred artefacts marked TODO. |
| **CC‑MVPK‑4c (I/O vs publication)** | Faces **do not** restate I/O; they carry **presence‑pins + anchors + EditionId** only. | Face inspection shows no I/O duplication. |
| **CC‑MVPK‑4d (Lawful orders)** | Any selection/comparison on faces **returns sets / lawful partial orders** with a **ComparatorSet** citation. | No hidden scalarization; ComparatorSetRef present. |
| **CC‑MVPK‑4e (Signature on faces — banned)** | The term **“signature”** is **not used** on faces; use **TechName/PlainName**. | Token scan: no “signature” on faces. |
| **CC‑MVPK‑4f (PC discipline)** | Any numeric/comparable publication uses **Publication characteristics** (PC) and carries pins {unit, scale, reference‑plane, edition}. | Cards show PC fields + pins; validation passes. |
| **CC‑MVPK‑4g (No axis/dimension)** | Faces avoid “axis/dimension/plane” metaphors except **ReferencePlane**; use CHR terms (**Characteristic/slot/CharacteristicSpace**). | Lexical check flags none; only `ReferencePlane` appears. |
| **CC‑MVPK‑4h (Edition pins on defs)** | Where maps/distances/spaces are cited, the face pins `DescriptorMapRef.edition`, `DistanceDefRef.edition`, and `CharacteristicSpaceRef.edition?`. | Validation shows edition fields populated. |
| **CC‑MVPK‑4i (Crossings gated)** | Plane/Context crossings cite **Bridge + CL** policies; penalties route to **R‑channel** only. | IDs present; routing verified in harness logs. |
| **CC‑MVPK‑4j (PublicationScope present)** | Each view **declares `U.PublicationScope`** (USM §6.5). | Field present; presence‑bit green. |
| **CC‑MVPK‑4k (Subset‑of underlier)** | For views about epistemes/capabilities, `PublicationScope ⊆ ClaimScope/WorkScope`; reindexing **does not widen** it. | Subset witness passes; promotion diff shows no widening. |
| **CC‑MVPK‑5 (Carrier anchoring)** | First mention includes **SCR/RSCR** ids. | SCR ids visible on the card. |
| **CC‑MVPK‑6 (Γ‑separation)** | No cost/time/data‑spend on publication morphisms. | CI shows proofs/witness artefacts; gate validation passes. |
| **CC‑MVPK‑7 (Reindexing monotone)** | If `s ⪯ t`, then `Emit_s(x) ⪯ Emit_t(x)`. | `TechCard` ≤ `InteropCard` (more structure, same claims). |
| **CC‑MVPK‑8 (Surface discipline)** | Only **PublicationSurface/InteropSurface** are used; faces named …**View/…Card**. | Token scan; no “rendering/presentation” as surface kinds. |
| **CC‑MVPK‑9 (Reindexing naturality)** | Reindexing coercions `PromoteView[s→t]` exist, are total, and commute with composition. | Witness shows `PromoteView[s→t]_Z ∘ Emit_s(g∘f) = (Emit_t(g) ∘ Emit_t(f)) ∘ PromoteView[s→t]_X`. |
| **CC‑MVPK‑10 (Iso‑preservation)** | Isomorphisms in `U` remain isomorphisms under each viewpoint. | Cards show mapped inverses or an iso‑witness. |
| **CC‑MVPK‑11 (Typing & totality)** | Ill‑typed composites are rejected at `ViewObj_s` rather than weakening functoriality. | Type‑check fails early; no “best‑effort” composition in cards. |
| **CC‑MVPK‑12 (Bridge+CL on crossings)** | Any cross‑Context/plane view cites **Bridge + CL** policy ids. | IDs present on `TechCard`/`AssuranceLane`. |

### E.17:10 - Anti‑patterns (with fixes)

1. **“Presentation logic” as semantics.**  
    *Fix:* Move any logic to `Describe_ID`/`Specify_DS` or CG‑Spec/KD‑CAL; keep views declarative; publication adds **zero** claims.    
2. **Publishing only objects.**  
    *Fix:* MVPK **acts on arrows**. Always emit views for `g∘f`, not just for objects `X, Y, Z`.    
3. **Unpinned numbers.**  
    *Fix:* Reject card; supply **pins** and CG/CHR anchors.    
4. **Viewpointless views.**  
    *Fix:* Define Viewpoint; attach concerns + conformance; re‑emit.    
5. **Interop ≡ Tech duplication.**  
    *Fix:* `InteropCard` may refine typing/shape but cannot contradict `TechCard` (reindexing monotone).    

### E.17:11 - Consequences

| Benefit | Why it matters | Trade‑off / Mitigation |
| --- | --- | --- |
| **Arrow‑level traceability.** | Composition preserved across views enables chain‑of‑evidence on pipelines. | Slight authoring overhead → MVPK templates. |
| **Audit‑ready surfaces.** | Pins + CHR anchors make numeric claims verifiable. | Gate‑based validation performs checks. |
| **Terminology hygiene.** | Clear View vs Viewpoint, Publication vs Presentation. | Enforce L‑SURF tokens in CI. |
| **Notation independence.** | Viewpoints talk concerns, not tools. | Provide adapters to local stacks. |

### E.17:12 - SoTA-echoing (post‑2015; conceptual pointers)

* **Profunctor/optic accounts (2017–2019).** Establish **compositional “views”** that compose like arrows—mirrors MVPK’s functorial law.    
* **Refinement‑typed ecosystems (2016→).** Units/scale at type level echo **pin discipline**.    
* **Interoperability & evidence envelopes.** External standards exist, but **their concrete formats live outside Part E** (see Annex/Interop for examples and mappings).

(References are illustrative exemplars of practice; MVPK remains notation‑agnostic.)

### E.17:13 - Relations

* **Builds on:** A.7/E.10.D2 (Strict Distinction & I/D/S discipline), A.6.2–A.6.3 (episteme morphisms, `U.EffectFreeEpistemicMorphing` / `U.EpistemicViewing`), E.17.0 (`U.MultiViewDescribing`), E.8 (Authoring conventions), E.10 (LEX‑BUNDLE incl. L‑SURF), Part F/G (UTS, CG‑Spec, CHR pins).    
* **Constrains:** Any surface‑emitting automation; must treat publication as a species of `U.EpistemicViewing` over existing D/S‑epistemes, not as a new I→D→S mechanism.    
* **Coordinates with:** B‑operators (no Γ‑leakage), C‑cluster (selection/archives: views are publication faces, not selections), **CHR‑MM** (measurement semantics), **UNM** (normalization families).

### E.17:14 - Minimal authoring template (E‑level)

**Header:** `MVPK v⟨edition⟩ — Σ = {PlainView ⪯ TechCard ⪯ InteropCard, AssuranceLane ⟂}`  
**For each arrow `f`:** emit `{Emit_s(f) | s ∈ Σ}` (or use the plain aliases `{PlainView(f), TechCard(f), …}`) with: **PublicationScope**, ViewpointId, pins, CHR/CG anchors, SCR ids, Bridge+CL ids (if crossing), and—if composite—machine‑checkable witnesses that `Emit_s(g∘f) = Emit_s(g)∘Emit_s(f)` **and** for each `s ⪯ t` the naturality square `PromoteView[s→t]_Y ∘ Emit_s(f) = Emit_t(f) ∘ PromoteView[s→t]_X`.

### E.17:15 - Manager’s one‑page review (copy‑paste)

> “We publish every **morphism** under a declared **set of viewpoints** using **MVPK**. Each **view** is **functorial** (identities, composition), **adds no new claims**, and pins **unit/scale/reference‑plane/edition** with **CHR/CG** anchors. **Interop** views clarify concerns/semantics only (concrete exchange lives outside Part E); **Assurance** cites evidence carriers (SCR). Any cross‑Context/plane view cites **Bridge+CL** (Φ→R only). Publication toil is **Work on carriers**, not a mechanism change.” 

### E.17:End

## E.18 - Transduction Graph Architecture** (E.TGA)

> **Tech‑name:** **E.TGA** (pattern label)
> **Plain‑name:** Architecture of the transduction graph
> **Twin labels:** Tech / Plain per E.10; faces emitted via E.17 MVPK (no schemas in Part E). 

### E.18:1 - Intent

Provide a **notation‑independent** architecture for graphs whose vertices are **morphisms (transductions)** and whose edges are **typed transfers**. The architecture is **agnostic to the concrete morphism set** and equips the graph with **publication, comparability, crossing, and budget** disciplines so that **flows** are **valuations over paths** within the same object. Faces appear via **MVPK**; numeric/comparable publication carries **pins** with **Bridge/CL** notes; Φ/CL^plane penalties remain in **R**.  
*Style note:* wording follows the **counterfactual register** of FPF: invariants are stated as model conditions, not deontic obligations (per E.8 style and the assignment).

### E.18:2 - Problem frame

Teams can produce many **valid flows** over the same capability: e.g., the assignment’s reference path
`U.FormalSubstrate → U.PrincipleFrame → U.Mechanism → U.ContextNormalization (UNM) → U.SelectionAndTuning ↔ U.WorkPlanning → U.Work → U.EvaluatingAndRefreshing`
is one **path** among many possible domain paths. Without a common **graph‑level architecture**:

* flows look ad‑hoc and **non‑comparable**;
* cross‑Context **crossings** (plane/Context changes) are undocumented;
* publication surfaces **smuggle arithmetic** or restate I/O;
* set‑returning selection is silently replaced by **single scores**;
* cycles lack **budget** discipline; refresh is **out‑of‑band**.

MVPK already fixes publication drift at the **single‑arrow** level; E.TGA lifts those **publication and comparability laws** to the **graph as a whole**. 

### E.18:3 - Problem

1. **Morphisms ≠ Graph.** A catalog of morphism‑level patterns (e.g., UNM, Selector, Work, Refresh) does not, by itself, explain **how the whole graph is built, constrained, and audited**.
2. **Flow proliferation.** Multiple “reference flows” can be authored; readers need **one orchestration** that keeps them legal and comparable **without privileging any single flow**.
3. **Unsafe publication.** Faces re‑list I/O, hide scalarization, or omit edition/plane pins; cross‑Context reuse lacks **Bridge/CL** citation; **plane penalties** leak to F/G. 
4. **Cycles without norms.** Selection↔Planning loops run without explicit **budget (Γ_time)**, **FreshnessRequest**, or **slice‑scoped** refresh; `FinalizeLaunchValues` (launch‑value slot filling) is performed too early (outside `U.Work` (`U.WorkEnactment`)). 

### E.18:4 - Forces

| Force                                            | Tension                                                                                                                                                                    |
| ------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Universality vs specialization**               | One architecture must host supply chains, water networks, ML functionals, and the assignment’s “first‑principles → work” path, **without** baking in any one morphism set. |
| **Publication neutrality vs auditability**       | Keep faces notation‑neutral and non‑mechanistic ↔ require **pins**, **ComparatorSet**, **Bridge/CL**, and **PublicationScope**.                                            |
| **Set legality vs business pressure for totals** | Preserve **return‑sets / lawful partial orders** ↔ stakeholders demand single numbers.                                                                                     |
| **Cross‑Context reuse vs safety**                | Enable reuse across `U.BoundedContext` ↔ enforce **Bridge/CL** with **R‑only penalties**.                                                                                  |
| **Agility vs reproducibility**                   | Permit evolving CG‑Spec/UNM/Comparator editions ↔ require **edition pins** and **re‑emission** on change.                                                                  |
| **Cycles vs convergence**                        | Allow Selection↔Planning iteration ↔ impose **budget** and **slice‑scoped** refresh to prevent thrash.                                                                     |

### E.18:5 - Solution — the E.TGA kit (graph model + choreography)

#### E.18::5.1 - S1 - Graph object (conceptual)

Define a **typed, editioned, directed multigraph**
`TransductionGraph := (V, E, τ_V, τ_E, Γ_time, Bridge, CL, TransportRegistry^Φ)`
with:

* **Vertices `V`:** instances of `U.Morphism` (open world). Common specialisations **include but are not limited to** the assignment’s set: `U.FormalSubstrate`, `U.PrincipleFrame`, `U.Mechanism`, `U.ContextNormalization (UNM)`, `U.SelectionAndTuning`, `U.WorkPlanning`, `U.Work`, `U.EvaluatingAndRefreshing`. This list is **illustrative**, not exhaustive—the graph **does not depend** on this particular set.
* **Edges `E`:** a **single edge kind `U.Transfer`** (typed) carrying artifacts/tokens; all **plane/Context/edition** changes occur **only at nodes via `OperationalGate(profile)`** with **Bridge + CL** annotations; penalties **→ R only**. Transport conversions pin **Φ‑policies** and editions.
* **Scopes:** `Γ_time` (budgets, horizons), `PublicationScope` for faces (E.17), and **slice ids** for refresh (G.11).

 **CtxState (PS‑projection; closed slots):** `CtxState = ⟨L, P, E⃗, D⟩` is the **projection of E.17 Publication Scope**.
 **Slot definitions (normative):**
  • `L := Locus` — an element of a partially ordered **ContextSlice** poset; addresses *where* claims apply (disciplinary / organizational / holonic slice).
  • `P := ReferencePlane` — the reference plane/units registry id; **no plane/unit declarations or translations** occur in CV; crossings remain gated (A.21).
  • `E⃗ := Edition vector` — a **partial map** `edition_key ↦ EditionId` over named families `{CG‑Spec, ComparatorSet, UNM.TransportRegistryΦ}` and optional `{DescriptorMapRef, DistanceDefRef, CharacteristicSpaceRef}` when cited.
  • `D := DesignRunTag` — `design(T^D)` or `run(T^R)`, used by **LaunchGate** and acceptance/telemetry duties.
 **Invariants.** Raw `U.Transfer` preserves `CtxState` (`⟨L,P,E⃗,D⟩`): it does **not** write/update any CtxState slot; any CtxState write/update (or entry to `U.WorkEnactment`) occurs at `OperationalGate(profile)`.
 **Extension discipline.** Any extra slot beyond ⟨L,P,E⃗,D⟩ **SHALL** be registered in the **E.17/LEX “CtxState Extension Registry”** with slot‑id, intent, partial‑order law (neutral/absorbing), and SquareLaw compatibility; unregistered extensions are non‑conformant.
 **Data‑shape location.** Concrete record shapes for `PathId/PathSliceId`, Γ‑pins, and lineage remain in A.22 `FlowSpec`; E.TGA fixes that **flow = valuation** and that `CtxState` is preserved across raw transfers.

 * **Kinds:** `U.Transduction(kind∈{Signature, Mechanism, Work, Check, StructuralReinterpretation})`.  
  **Exact identification (no TGA‑local taxonomy):**  
  — `Signature` **≡** **A.6.0** `U.Signature` (universal, law‑governed declaration).  
  — `Mechanism` **≡** **A.6.1** `U.Mechanism` (law‑governed application over a SubjectKind/BaseType).  
  — `Work` **≡** **A.15** `U.WorkEnactment` (world‑contact; `FinalizeLaunchValues` only here).  
  — `Check` **≡** `OperationalGate(profile)` (universal **gate**; A.* patternisation pending; CC‑TGA catalog applies).  
  — `StructuralReinterpretation` **≡** a species of **A.6.4** `U.EpistemicRetargeting` used as a graph node in E.TGA. **All retargeting semantics** (slot‑level discipline, `DescribedEntitySlot`/`GroundingHolonSlot` behaviour, invariants, Bridges, witnesses) come from **C.2.1** and **A.6.2–A.6.5**; E.TGA does **not** introduce a TGA‑local variant of retargeting.  
  `OperationalGate ≔ U.Transduction(kind=Check)` with DecisionLog aggregation.  
  The only extra discipline E.TGA adds for `StructuralReinterpretation` is **graph‑local**: CtxState and GateCrossing behaviour are governed by **CC‑TGA‑06‑EX** and **CC‑TGA‑11** (projection‑preserving w.r.t. `⟨L,P,E⃗,D⟩`, PathSlice‑local, and “no plane/unit change without a gate”). 

> **MVPK integration (import).** Every vertex with an external surface is published via **MVPK** faces (`PlainView`, `TechCard`, `AssuranceLane`, `InteropCard`) under a declared **PublicationScope** (E.17). E.TGA **reuses** MVPK’s publication laws (pins, lawful‑order discipline, “no new numeric claims / no I/O re‑listing”) and only adds graph‑level constraints in S3 and **CC‑TGA‑09/10**; it does **not** define a second, local publication semantics. 

**GateCrossing (normative)**
**Definition.** A **GateCrossing** is the typed transition at a node that writes/updates any of:
  (i) `U.BoundedContext` (**Context**), (ii) **ReferencePlane**, (iii) any member of the **Edition vector** `E⃗` (e.g., `CG‑Spec`, `ComparatorSet`, `UNM.TransportRegistryΦ`, `DescriptorMapRef`, `DistanceDefRef`, `CharacteristicSpaceRef`), (iv) **DesignRunTag** (`T^D↔T^R`), or (v) **Kind/describedEntity** (only under `StructuralReinterpretation` subject to **CC‑TGA‑06‑EX**).
**Invariants.** Raw `U.Transfer` preserves `CtxState`; a GateCrossing occurs at exactly one `OperationalGate(profile)` (SquareLaw applies).
**Required pins (minimum).** `BridgeCard + UTS row`; `CL` for scope bridges; `CL^plane` for plane crossings; `CL^k` with `bridgeChannel=Kind` for kind transitions; `PublicationScopeId`; `PathSliceId`; Γ‑pins on compare/launch faces.
**Canonical reference.** `CrossingRef := ⟨GateId, channel, from, to, UTS.RowId, PathSliceId⟩`. Any DecisionLog entry whose rationale depends on a crossing **SHALL** cite `CrossingRef`.
**CrossingSurface (normative)**
**Definition.** A **CrossingSurface** is the published bundle that makes a GateCrossing **auditable and replayable** (crossing visibility). It includes:
* the canonical **`CrossingRef`**;
* the matching **UTS row** (**`UTS.RowId`**) for the crossing;
* the required pins **`PublicationScopeId`** and **`PathSliceId`**;
* where a Bridge is involved: the **BridgeCard** (F.9) and its disclosed fields (`BridgeId`, `bridgeChannel`, **CL** and loss notes; **`CL^k`** when `bridgeChannel=Kind`; **`ReferencePlane(src,tgt)`**);
* where planes differ: **`CL^plane`** and the active **`Φ_plane`** as a **`PolicyIdRef`** (policy-id + resolvable refs; F.8:8.1);
* the active penalty policy identifiers **`Φ(CL)`** (and **`Ψ(CL^k)`** if used) as **`PolicyIdRef`** bundles (policy-id + `PolicySpecRef` + `MintDecisionRef?`; F.8:8.1);
* any additional pins mandated by the active **GateProfile** / GateChecks (A.21) for this crossing.

**Obligation.** Every **GateCrossing MUST publish its CrossingSurface**. Missing or non‑conformant CrossingSurface is a **blocking** defect for downstream consumption (selectors, acceptance, audits).

**Term separation.** **Transfer** denotes the sole edge kind `U.Transfer` (graph edges). **Transport** denotes Φ‑governed conversion **policies/registries** (**`TransportRegistry^Φ`** under UNM). Wording “reuse via Transport” refers to registries/policies, not to an additional graph edge.

#### E.18:5.2 - S2 - Flows as valuations (paths + state + guards)
* A **Flow** is a **valuation** `ν` over `U.Transfer` edges and cut‑sets, paired with an **admissible path** `p = v₀ → … → v_k`. The valuation assigns tokens/states under `CtxState` and records publication events under a declared `PublicationScopeId`. **The concrete pins and identifiers (`PathId`, `PathSliceId`, Γ_time on compare/launch faces) are specified in A.22 `FlowSpec` and A.25 `Sentinel & SubFlow`.** This reflects the “graph ≠ flow” norm (flow = valuation), with gates placed exactly on GateCrossings.  
* **Admissible path (definition).** A path `p` is **admissible** iff:  
  (a) node/edge types match the declared `τ_V, τ_E`;  
  (b) any write/update to any member of `⟨L,P,E⃗,D⟩` (or kind‑retargeting under `StructuralReinterpretation`) appears at **exactly one** `OperationalGate(profile)`;  
  (c) each GateCrossing on `p` has a **SquareLaw witness** (CC‑TGA‑23) and, where applicable, a **SquareLaw‑retargeting witness** (CC‑TGA‑06‑EX);  
  (d) no hidden crossings occur across raw transfers;  
  (e) Γ‑pins are present on compare/launch faces;  
  (f) `T^D↔T^R` occurs **only** at `LaunchGate`.

* `U.Transfer` preserves `CtxState` (`⟨L,P,E⃗,D⟩`) and carries **Assurance‑operations** only (see S3b); any crossing of locus/plane/editions or `T^D↔T^R` is placed at `OperationalGate(profile)`.
* A **PathSlice** is a **slice‑scoped execution window** used for refresh/telemetry; faces pin `PathSliceId`; **re‑emission** happens when any pinned edition changes or `SliceRefresh` is triggered by sentinel rules.

> **Consequences.** The assignment’s “reference flow” is simply one `p` in `TransductionGraph`. Other domains (supply chain, water network, NN functional) instantiate different `p` on the **same architecture**.
> 
**Why "flow = valuation" doesn't kill the "something is flowing" intuition**
There are two complementary perspectives:
* **Lagrangian (intuitive):** "water particles" run through pipes; you "track" tokens.
* **Eulerian (architectural):** you define a **function on edges** ("how much/what passes through each edge under a given regime"), with gate laws. E.TGA deliberately fixes the **Eulerian semantics of flow** at the architectural level: "flow (= valuation) + publication log", while the dynamics of "movement" show up as **re-valuation** over a **PathSlice** (the execution/republishing window) under gate rules and the SquareLaw. This yields comparability, reproducibility, and slice-local refresh.

#### E.18:5.3 - S3 - Publication discipline (faces)

E.TGA **imports E.17** wholesale **and associates MVPK faces with `PublicationScope` (USM)**.  
**MVPK remains the normative source** for:
* the set of face kinds (`PlainView`, `TechCard`, `InteropCard`, `AssuranceLane`),
* pin discipline and Publication Characteristics (PC),
* “no new numeric claims / no I/O re‑listing / no Γ‑semantics on faces”.

E.TGA **does not re‑specify** these laws; it only adds **graph‑level obligations** for faces emitted over transduction paths:

1. **Crossings on faces.** When a face participates in a GateCrossing (S1.b/S9), it **SHALL** cite `BridgeId + UTS row + CL` and publish **Φ(CL)/Φ_plane RuleId**; **penalties remain in R‑lane**.
2. **Gate‑requirement on cited editions.** Any face that references editions of `CG‑Spec` / `ComparatorSet` / `UNM.TransportRegistryΦ` includes **`BridgeCard + UTS row`**; faces without this are treated as **non‑consumable downstream**.  (delegated tests → A.27/A.34)  
3. **ComparatorSet & set returns (graph‑scope).** Any `ComparatorSet` and `SetSemanticsRef` used along a transduction path **SHALL** carry **edition identifiers**; flows **re‑emit** faces on edition change; faces with comparison **return sets / lawful partial orders** (no hidden scalarization), reusing MVPK’s lawful‑order discipline.
4. **Γ_time on compare/launch faces.** All compare/launch faces on E.TGA paths pin `Γ_time`; implicit *latest* is illegal. The **shape and evaluation** of `Γ_time` live in A.26; E.TGA only mandates presence. **CHR avoids acceptance thresholds** (*NoThresholdsInCHR*); thresholding and launches surface in G‑patterns and `U.Work`.  (delegated tests → A.32/A.33). **Unknowns remain tri‑state (`pass|degrade|abstain`) and fold per GateProfile (A.21/A.26).**  

> **Reminder.** MVPK already bans “signature” on faces, I/O re‑listing, arithmetic on faces, and unpinned numeric content (E.17 §5.4–5.5). E.TGA **does not weaken or override** those rules; it only constrains how they are used along transduction paths.

**Lean publish‑mode (AssuranceLane‑Lite).** Lean affects **faces only** (`PlainView`/`AssuranceLane` minimal), not checks; publication shows `GateProfile`, `GateCheckRef[]`, and `DecisionLogRef`; the underlying GateChecks list remains unchanged.

**Decision stability & idempotency (delegated).** Gate decisions are **idempotent** under a congruence relation over inputs; the **witness and equivalence criteria** are specified in **A.41 DecisionLog**. E.TGA **does not** prescribe storage formats, key shapes, or hashing schemes.

**KindBridge admissibility (publication).**  
Treat a step as a **describedEntity/kind** transition (including `StructuralReinterpretation` under CC‑TGA‑06‑EX) **iff** the **UTS row**:
  — satisfies the **minimal Bridge row** obligations of A.27 (identity, `ReferencePlane`, `CL/CL^plane`, edition‑pins for `CG‑Spec` / `ComparatorSet` / `UNM.TransportRegistryΦ`, `ComparatorSetRef`, `BridgeId`, `Φ‑RuleIds`), and  
  — is additionally marked as a **KindBridge** per C.3 (`bridgeChannel=Kind`, `CL^k`, mapping or signature‑translation, order‑preservation claims, loss notes, definedness area, determinism).  
Otherwise this KindBridge explanation does not apply (the step falls back to a gated crossing). When the gate owns the crossing, `CrossingRef` is surfaced and linked from the `DecisionLog`.

#### E.18:5.4 - S4 - Assurance‑operations on `U.Transfer` (counterfactual admissibility)
On `U.Transfer` edges, an operation is interpreted as a **declarative assurance‑operation** **iff** it is one of  
`ConstrainTo(rule)` - `CalibrateTo(map|standard)` - `CiteEvidence(anchor)` - `AttributeTo(agent|role)`; otherwise this explanation does not apply.
Under this interpretation, `CtxState⟨L,P,E⃗,D⟩` is preserved.  
If an effect entails a plane/unit change, the assurance‑operations explanation does not apply and the step is handled as a gated crossing (`OperationalGate(profile)+Bridge+UTS`).  
If Φ assigns penalties, they appear in the R‑lane; otherwise no penalties are surfaced here.

#### E.18:6.5 - S5 - Comparability & aggregation (normalize‑then‑compare; counterfactual form)

The comparison explanation applies under the following admissibility conditions:

* If a path segment intends to compare/aggregate, it is admissible as a comparison **only when** UNM precedes it; UNM is **method‑independent**, publishes **TransportRegistry^Φ** and **CG‑Spec** anchors, and faces cite those editions; otherwise this comparison explanation does not apply.
* If the comparator defines a **lawful partial order**, then returns are **sets/archives** (Pareto/Archive); if a **total order** is declared, it is the one provided by the comparator; otherwise set semantics apply and covert scalarization is out of scope here.
* If a claim is **ordinal‑only**, then only comparisons are surfaced; arithmetic transforms (e.g., means/z‑scores) are out of scope of this explanation and belong to declared comparators or downstream policy.

**Edition‑aware artifacts (e.g., QD archives) MUST pin `DescriptorMapRef.edition` / `DistanceDefRef.edition` (and `CharacteristicSpaceRef.edition` when applicable); refresh is slice‑local.**  (delegated tests → A.34/A.37)  

#### E.18:5.6 - S6 - Cycle discipline (Selection ↔ Planning)

* The architecture centers the loop between `U.SelectionAndTuning` and `U.WorkPlanning`.
* The loop operates under a local **budget / max_iter** in `Γ_time`; at expiry, the selector emits the **current `CandidateSet`** and **`MethodTuning`** with a **partial‑optimality** flag; further improvement rolls into the **next `PathSlice`**.
* **UNM occurs before the loop**; if measurements are missing/stale, UNM emits a **FreshnessRequest** which is **planned** in `U.WorkPlanning` and **executed** in `U.Work`. Transfers, units, and calibrations are surfaced publication‑wise as `CalibrateTo(map|standard)` and pinned to `TransportRegistry^Φ` (**R‑channel only** for penalties).
* **WorkEnactment is the only site for launch‑value slot filling** (`FinalizeLaunchValues / FinalizeLaunchValuesOnlyInWork`). 
> **Refresh orchestration.** Telemetry from `U.WorkEnactment` and publications are **slice‑scoped**, editions re‑pinned, faces **re‑emitted**. 

#### E.18:5.7 - S7 - Selector semantics (G.5) & parity harness (G.9)

* **Selectors return sets.** Default **DominanceRegime** is `ParetoOnly`; **IlluminationSummary** (telemetry summary) and any coverage/regret (telemetry metrics) are **report‑only telemetry** (reported), excluded from dominance **unless** a CAL policy promotes them (policy‑id in SCR).

If `PortfolioMode=Archive`, a **QD archive** may be returned; when generation is in scope, pairs `{environment, method}` are managed under declared **EnvironmentValidityRegion** and **TransferRulesRef**; parity artefacts and `PathSliceId` are pinned on publication. Details of comparator semantics and archive pinning live in **A.28/A.34**.

#### E.18:5.8 - S8 - Guard ownership and handling (USM §1.2)
* **USM.CompareGuard**/**USM.LaunchGuard** **publish `GuardOwnerGateId`**. Guard failures are **events** aggregated by the owner gate (not GateChecks).
* **Ownership rules:** (i) `USM.LaunchGuard.owner = LaunchGateId(U.WorkEnactment)`; (ii) inside a Subflow, `USM.CompareGuard.owner = OperationalGate(InSentinel)`; Join‑nodes cannot own guard pins.

**GateProfile data shape (cross‑reference).** The **entire data shape** (SoD/quorum, declassify, budgets, TOCTOU/freshness windows, editions vector, scopes) is **specified in A.26**. E.TGA **only names** the structure and defers its fields to A.26.

**Bridge‑aware guards (cross‑reference).** USM guards apply bridge‑translation semantics (`translate(Bridge, Scope)`) with CL penalties in R‑lane; the conceptual macro is defined in **A.24 USM.Guards**.

**Error/timeout/unknown (profile‑bound).** GateCheck errors/timeouts fold to **`degrade`** under `Lean|Core` and to **`block`** under `SafetyCritical|RegulatedX`; `unknown` follows the GateCheck’s intensional rule (safety‑default: `degrade`). **The DecisionLog shape and the idempotency witness are defined in A.41; E.TGA does not define storage or key structures.**  

#### E.18:5.9 - S9 - Transport & crossings
* Cross‑Context or cross‑plane edges appear as **GateCrossings** that include a **Bridge** with **CL** policy; **Φ(CL)/Φ_plane** are published; penalties route **to R only**; **Scope membership** (USM) is unchanged by crossings. **SquareLaw is checked within a single `DesignRunTag`; a `T^D↔T^R` change is modelled as a pair of coordinated gates with `DesignRunTagFrom/To` and an external enactor (see A.29).** 
* When *describedEntity/kind* changes across a boundary, declare an explicit **KindBridge (`CL^k`)** in addition to plane/context CL; cross‑context reuse of UNM **must** go via `Transport`, with any `CL^plane` penalties routed to **R‑lane** only.

#### E.18:5.10 - S10 - Non‑mechanism boundary

* Publication is a **typed projection**, not execution. Any build/render/upload is **Work on carriers**; **no Γ‑semantics** may leak into faces. 

#### E.18:5.11 - S11 - Coordination thread (optional)
Introduce **CoordinationFlow** as a named thread laid over `U.TransductionFlow__P2W`; crossings with production flow go via **Bridge+UTS**; coordination publishes **LexicalView** labels only and adds **no checks** or mechanisms.

#### E.18:5.12 - S12 - Viewpoint families → E.TGA constructs (neutral, holonic)

E.TGA does not mint new viewpoint or view kinds. It **imports** the generic multi‑view machinery of E.17.0 `U.MultiViewDescribing`, bundles from E.17.1, and the TEVB engineering bundle from E.17.2. S12 only describes how these existing `U.Viewpoint` / `U.ViewpointBundle` ids are *used* in transduction graphs and in `UTS.ViewpointMap`; intent/concern semantics live in E.17.0–E.17.2.

**Two‑layer use of TEVB and MVPK (ISO 42010 summary, no local re‑definition).**

* **Engineering viewpoints.** For engineering holons, E.TGA assumes a TEVB bundle with `ViewFamilyId = VF.TEVB.ENG`. `EngineeringVPId` is one of `{VP.Functional, VP.Procedural, VP.RoleEnactor, VP.ModuleInterface}`, and TEVB is the normative source for their semantics. E.TGA does not refine these viewpoints.  
* **Publication viewpoints.** Publication viewpoints come from MVPK (E.17); `PublicationVPId` is a `MVPK.ViewpointId` that governs faces under a `PublicationScope`.  
* **Architecture description.** Under ISO 42010, an architecture description for a holon is: (i) an E.TGA transduction graph over that holon, plus (ii) MVPK faces emitted for its morphisms, with correspondences per E.17.0 linking each face to the engineering view(s) it implements. Crossings and penalties follow E.TGA’s gating rules (S9; CC‑TGA‑11/23) but do not change viewpoint semantics.  
* **Separation of roles.** `VP.*` from TEVB are **EngineeringVPId** values only; they are not surfaces. `PublicationVPId` values live in MVPK. The mapping between them is entirely via ISO‑style correspondences and the `UTS.ViewpointMap`; E.TGA does not define a second notion of viewpoint.

**Entities‑of‑interest (summary).**

* **EoI‑ENG.** The engineering entity described by TEVB/E.TGA is a holon (`U.System` or `U.Episteme`) per TEVB’s `EoIClassSpec`. E.TGA does not broaden or narrow this set.  
* **EoI‑PUB.** MVPK may treat the *architecture description* itself as an entity‑of‑interest; publication viewpoints for that AD are defined in MVPK, not here. E.TGA only requires that such faces honour MVPK discipline and E.TGA’s crossing rules.

**Naming rules (aligned with E.17.0/E.17.1/E.17.2).**  
* `ViewFamilyId` is the `U.ViewpointBundle.viewFamilyId` (e.g. `VF.TEVB.ENG` for TEVB); its lexical and ontological discipline is governed by E.17.1.  
* `EngineeringVPId : ViewpointId` is always a `U.ViewpointId` drawn from some bundle (for TEVB, one of `{VP.Functional, VP.Procedural, VP.RoleEnactor, VP.ModuleInterface}`). E.TGA never defines new `VP.*` ids.  
* `PublicationVPId : ViewpointId` is a `MVPK.ViewpointId` defined in E.17; TEVB viewpoints are **never** reused as publication viewpoints (per TEVB guard and MVPK).  
* The legacy unqualified column name `ViewpointId` MUST NOT be used. Where it exists, it is interpreted as `PublicationVPId` and is DEPRECATED (sunset when E.23 is published).

**Terminology guards (no local semantics).**
* Within S12, “viewpoint”, “view” and “correspondence” have exactly the meanings given in E.17.0; “publication surface” means an MVPK face (`PlainView`, `TechCard`, `InteropCard`, `AssuranceLane`) under some `PublicationVPId`.  
* Faces are **carriers for views**: a face is part of a view only when linked via an ISO‑style `CorrespondenceRef` to an engineering `U.View` under some `EngineeringVPId`; S12 does not add extra conditions beyond E.17.0/E.17.2.  
* Labels such as “Functional view”, “Procedural view”, “Role‑Enactor view”, “Module‑Interface view” in this section are lexical aliases for TEVB viewpoints; they MUST NOT be interpreted as extra viewpoint kinds or as surface types.

**Purpose.** Provide a neutral (F.18) mapping from TEVB engineering *viewpoint families* — bundle `VF.TEVB.ENG` with `VP.Functional / VP.Procedural / VP.RoleEnactor / VP.ModuleInterface` — to E.TGA constructs so that the same holon can be described functionally, procedurally, structurally, or as a module‑and‑interface architecture **without changing the underlying graph**. S12 does not introduce new `U.Viewpoint` or `U.View` kinds; it reuses those defined in E.17.0/E.17.2.

**Holon target.** The mapping applies to any holon, with the constraint that only `U.System` enacts `U.Work` (A.3/A.15). Supervisory and structural hierarchies remain distinct (B.2.5).

**Viewpoint family → primary E.TGA constructs (TEVB‑aligned)**  
*All four families referenced below are TEVB engineering viewpoints; the “what …” clauses are interpretive glosses for how they *use* E.TGA constructs. Formal intent/concerns/allowed episteme kinds remain in TEVB (E.17.2).*
1) **Function‑Oriented View (`EngineeringVPId = VP.Functional`, capability‑flow)** — “what transformation is achieved under roles”
    * **Flow substrate:** `U.TransductionFlow__P2W` through nodes `SubstrateFormalization → OntologyAuthoring → CHRAuthoring → PrincipleFraming → MechanismRealization → UNM.Usage (ContextNormalization) → SelectionAndTuning ↔ WorkPlanning → WorkEnactment → EvaluatingAndRefreshing`.
    * **Publication:** MVPK publication surfaces per E.17; comparable claims pin to `CG‑Spec/ComparatorSet` editions; crossings surface via `Bridge+UTS` and `CL/CL^plane` (penalties → **R‑lane** only). 
    * **Checks:** A.20 (CV) inside transformations; A.21 (GateFit) at gates; enforce CSLC/No‑Hidden‑Scalarization per A.28. 
    *  **Holonic note:** `U.Episteme` does not *act*; it is used by systems acting on carriers; `U.Work` appears only for `U.System`. 
2) **Procedure‑Oriented View (`EngineeringVPId = VP.Procedural`, step/time storyboard)** — “what steps occur and when”
    * **Artifacts:** `U.WorkPlan` (A.15.2) for intent/schedule; `U.WorkEnactment` for enactment.
    * **Boundary:** entry into `U.WorkEnactment` is via `OperationalGate(profile)` with `USM.LaunchGuard`; `DesignRunTag` separates design time from run time; `DesignRunTagFrom/To` appear only at gates. 
    * **Holonic note:** Applies to any `U.System` scope (single holon or a supervised sub‑holon cluster); supervisory layering is handled by roles rather than structural mereology (B.2.5).
3) **Role‑Enactor / Device‑Structure View (`EngineeringVPId = VP.RoleEnactor`)** — “what carrier/ports/constraints exist; who typically enacts it”
    * **Artifacts:** Module *interfaces* are `Signature` nodes; module realizations are `MechanismRealization` nodes; inter‑module dependencies traverse `U.Transfer`, with gates on crossings. 
    * **Publication:** MVPK faces are **typed projections**, not executable artifacts; faces add **no new numeric claims** (E.17). Constraints and compatibility appear as CV checks (A.20). 
    * **Holonic note:** Structural mereology (part/whole of the carrier) is modeled in Part A; E.TGA ties interface/exposure semantics to morphisms and gates.
    * **Device‑View reading (Transduction↔Transductor).** The same capability‑flow MAY be read as a **device** that performs the transduction (**transductor**) without changing the graph: model with `Signature` + `Mechanism` only; do **not** introduce extra edge kinds. If describedEntity retargets (function↔element), use `StructuralReinterpretation` with a **`KindBridge (CL^k)`** on **UTS** and a **SquareLaw‑Retargeting witness**; preserve `⟨L,P,E⃗,D⟩` and treat it as a non‑crossing (**CC‑TGA‑06‑EX**; witness shape §4.7).  
    * **Role‑label guard.** `TypicalEnactorRoleName` is **pedagogical only** and MUST NOT be used as a GateFit role; GateFit uses `U.Role` (A.21).
4) **Module‑Interface View (`EngineeringVPId = VP.ModuleInterface`, physical/logical architecture)** — “what modules exist and how they contract across interfaces”
    * **Artifacts:** Module *interfaces* are `Signature` nodes; module realizations are `Mechanism` nodes; inter‑module dependencies traverse `U.Transfer`, with gates on crossings. 
    * **describedEntity note:** Functional↔element reinterpretation follows the **Device‑View reading** rule above (Role‑Enactor family) and **CC‑TGA‑06‑EX**; see **§4.7** for the retargeting witness shape and CV witness linkage.
    * **Holonic note:** The same module may appear as a holon in multiple views; supervisory loops (B.2.5) remain orthogonal to structural composition.
This is an expandable list of viewpoint families; TGA is intentionally viewpoint‑neutral. Additional engineering bundles beyond TEVB (safety, mission, information, …) are introduced as separate `U.ViewpointBundle` species via E.17.1/E.17.2; S12 does not define them.

**Alias families for transduction species (LEX‑only).**
*Scope.* Authors MAY declare `AliasesInViewFamilies[]` for `U.Transduction` species so readers can recognise familiar engineering view families. All semantics come from the referenced bundles (typically TEVB) and MVPK; aliases are purely lexical.

*Norms.*
1. Each `U.Transduction` species MAY publish `AliasesInViewFamilies[]` — an open list of records  
   `{ ViewFamilyId, EngineeringVPId?, Alias : TechASCII }`.  
   * If `ViewFamilyId = VF.TEVB.ENG`, then `EngineeringVPId` MUST be one of `{VP.Functional, VP.Procedural, VP.RoleEnactor, VP.ModuleInterface}` (TEVB; CC‑TEVB‑1/6).  
   * Other `ViewFamilyId` values MUST denote `U.ViewpointBundle` instances defined elsewhere (e.g. safety/assurance/information bundles), not ad‑hoc local families.
2. Aliases are LEX‑only: **no arithmetic, no new claims, no check participation, no `CtxState` slot writes/updates (incl. `DesignRunTag`)**. They do not create MVPK faces.  
3. Aliases MUST NOT be used as `PublicationVPId`; publication viewpoints remain in MVPK.  
4. Twin registers are allowed (Tech/Plain) per E.10; naming follows F.18 local‑first discipline.  
5. Do not name transductions by operands/effects (operation ≠ operand).  
6. `TypicalEnactorRoleName` MAY be added for pedagogy; it SHALL NOT be used as a GateFit role (GateFit uses `U.Role` only).  
7. Morphology: ASCII TitleCase; conjunctions via `And`; for composite actions use `XingAndYing` (or `XAndYing` if grammar requires).  
8. The P2W reference species table (SubstrateFormalization … EvaluatingAndRefreshing with functional/procedural aliases and `TypicalEnactorRoleName`) is **informative** and does not change kind or viewpoint semantics.

**Deliverable — `UTS.ViewpointMap` (normative, TEVB‑aligned).**  
Publish a UTS block named `ViewpointMap` that ties engineering viewpoints (from bundles such as TEVB) to E.TGA constructs and MVPK faces.

*Minimum row schema (per row).*
* `ViewFamilyId` — `U.ViewpointBundle.viewFamilyId` (e.g. `VF.TEVB.ENG` for TEVB, or another bundle id).  
* `EngineeringVPId : ViewpointId` — a viewpoint from that bundle (for TEVB, one of `{VP.Functional, VP.Procedural, VP.RoleEnactor, VP.ModuleInterface}`).  
* `PublicationVPId : ViewpointId?` — MVPK publication viewpoint id that governs faces implementing this engineering view (optional if not publishing).  
* `TargetHolon ∈ {U.System, U.Episteme}` *(extended species may add `{U.PromiseContent|U.MethodFamily}`; if `TargetHolon ≠ U.System`, no `U.Work` enactment appears).*  
* `PrimaryTGAConstructs` — nodes/edges/gates actually used for this `(ViewFamilyId, EngineeringVPId, TargetHolon)` (typically one of the four families above).  
* `Crossings{BridgeId, CL/CL^plane?}` — crossings involved; penalties route to R‑lane only.  
* `EditionPins{…}` whenever comparable claims appear (bind to CG‑Spec/ComparatorSet editions; any face citing editions includes `BridgeCard + UTS` row per MVPK/UNM).  
* `SenseCells[]` (≥ 2 per row), each citing Context name + edition (F.17/E.10 discipline; UTS‑wide coverage rules still apply).  
* *(REQUIRED when publishing)* `CorrespondenceRef[]` — ISO 42010 correspondences linking emitted faces to the engineering view(s) they implement; may cross architecture descriptions.  
* *(RECOMMENDED)* `ConcernsCovered[]` — ISO 42010 stakeholder concerns addressed by this row via GateProfiles/check catalogues.

**Conformance (S12‑scoped).**  
(i) `UTS.ViewpointMap` exists.  
(ii) For each holon that claims TEVB alignment, there are ≥ 4 rows whose `{ViewFamilyId, EngineeringVPId}` cover `{VF.TEVB.ENG × {VP.Functional, VP.Procedural, VP.RoleEnactor, VP.ModuleInterface}}` (per CC‑TEVB‑1/6).  
(iii) Rows that surface editions also include `BridgeCard + UTS` rows per A.27; edition‑bearing faces that lack such rows MUST NOT be used for downstream consumption.  
(iv) Each row has ≥ 2 `SenseCells` and the sheet meets global UTS coverage rules.  
(v) Any `TargetHolon = U.System` that reaches `U.Work` shows `LaunchGate` with `DesignRunTag` consistency.  
(vi) Crossings referenced in `ViewpointMap` follow CC‑TGA‑11; comparability along the mapped paths follows CC‑TGA‑10.  
(vii) Rows MUST NOT use an unqualified `ViewpointId`; they MUST use `EngineeringVPId` and/or `PublicationVPId` explicitly.  
(viii) When faces are published, `CorrespondenceRef[]` MUST be present and resolvable to `U.Viewpoint` ids.  
(ix) Additional bundles (e.g. assurance, information, mission) MAY appear as extra `ViewFamilyId` values but MUST be declared as `U.ViewpointBundle` species; they do not extend `VF.TEVB.ENG`.

### E.18:6 - Archetypal Grounding (Tell–Show–Show; concise)

*Show‑A (Supply chain).* Nodes: procurement → inbound QC (UNM) → selection (supplier set; lawful order) ↔ planning (lotting/schedule; budget) → execution (receipts; **WorkEnactment enacts (world‑contact)**) → refresh (quality telemetry; re‑emit faces). Crossings: vendor Context via **Bridge/CL**; penalties **→ R only**; comparators pinned to CG‑Spec edition. 

*Show‑B (Neural‑net functional).* Nodes: formal substrate (typed tensor ops) → mechanism (combinator algebra) → UNM (dataset normalization; **TransportRegistry^Φ**) → selection (architecture/hyperparam set; Pareto set over accuracy@ratio & FLOPs@ratio) ↔ planning (compute budget horizon) → Work (training runs; Δ anchored) → refresh (parity inserts; slice‑scoped). Faces pin **DescriptorMapRef.edition / DistanceDefRef.edition** when QD metrics are shown; illumination remains a **report-only telemetry metric** by default. 

> *Post‑2015 SoTA echoes (illustrative):* **TAMP/MPC**, **MAP‑Elites / QD (incl. CMA‑ME)**, **refinement‑typed stacks**, **profunctor optics**. **Worked‑examples and Tell–Show–Show vignettes move to A.31/A.34/A.37; E.TGA keeps only the carcass‑level alignment.**

### E.18:7 - Conformance — **Unified checklist (normative)**

| ID | Requirement | Practical test |
|----|-------------|----------------|
| **CC‑TGA‑01 — Single edge kind** | The graph uses exactly one edge kind `U.Transfer`; all plane/Context/edition transitions occur only at nodes via `OperationalGate(profile)`. | Model lint finds no auxiliary edge kinds for unit/plane changes; crossings sit on declared gates. |
| **CC‑TGA‑02 — Nodes are morphisms** | Nodes are intensional `U.Transduction(kind∈{Signature,Mechanism,Work,Check,StructuralReinterpretation})`. This enumeration is a **minimal roles baseline**. **Domain‑specific species are open‑world** and non‑exhaustive; they bind to one of these kinds. Adding a **new kind** requires an explicit E.TGA update. `StructuralReinterpretation` nodes are **projection‑preserving** (no mutation of `⟨L,P,E⃗,D⟩`) and carry CV/GF obligations per A.20/A.21/A.45. **Mapping to A.\*** (normative): the enumeration is **not** a TGA‑local taxonomy; each `kind` is identified 1‑to‑1 with its A.\* anchor: `Signature→A.6.0`, `Mechanism→A.6.1`, `Work→A.15`, `Check→OperationalGate` (until a dedicated A.\* pattern is published). | Type registry shows at least the listed kinds; additional species map to one of them; checks realized as `OperationalGate` (see CC‑TGA‑06‑EX/11). **Lint:** registry/table exposes `{species → {kind, KindDefinition}}`; missing or mismatched `KindDefinition` fails. |
| **CC‑TGA‑03 — Identity, composition, functorial faces** | Identities exist; path composition associative; publication is functorial: `Emit_s(t₂∘t₁)=Emit_s(t₂)∘Emit_s(t₁)`. | Pick two‑step path; MVPK faces commute (Square witness). |
| **CC‑TGA‑04 — Graph spec** | Spec declares `τ_V, τ_E`, `Γ_time`, Transport/Bridge registries. | Spec file shows typed registries and Γ policy. |
| **CC‑TGA‑05 — CtxState pins** | `CtxState=⟨L,P,E⃗,D⟩` is pinned on ports/tokens; raw `U.Transfer` does **not** write/update it. | Along a raw transfer, ⟨L,P,E⃗,D⟩ is preserved. |
| **CC‑TGA‑06 — Operational gates only** | Any write/update to any member of ⟨L,P,E⃗,D⟩ or entry into `U.WorkEnactment` is mediated by `OperationalGate(profile)` with aggregated `DecisionLog`. | Diff CtxState across edges; if any member differs, exactly one gate exists with DecisionLog. |
| **CC‑TGA‑06‑EX (strictly limited) — Projection retargeting without gate** | A node of kind **`StructuralReinterpretation`** MAY retarget the **published projection** without invoking `OperationalGate` **only if all hold**: **(a)** `⟨L,P,E⃗,D⟩` is preserved; **(b)** any **describedEntity** change has a **KindBridge** (`CL^k`) entry on MVPK/**UTS**; **(c)** a **SquareLaw‑retargeting witness** is present (on UTS); **(d)** the operation is **PathSlice‑local** (`PathSliceId` pinned); **(e)** **no plane/unit change** occurs (plane/unit changes remain gated); **(f)** **CV.ReinterpretationEquivalence** (A.20) is `pass`; **(g)** **NoHiddenScalarization** — if the step concerns a comparable return shape, set/partial‑order semantics are preserved and comparators remain ref‑only (cf. A.28). | UTS row includes `bridgeChannel=Kind` and `CL^k`; SquareLaw‑retargeting witness present; PathSliceId pinned; CV status recorded; no scalarization detected. |
| **CC‑TGA‑07 — CV⇒GF activation predicate** | Until **aggregated `ConstraintValidity` = `pass`**, all **GateFit** checks return `abstain`. | Simulate CV failure ⇒ GateFit `abstain`. |
| **CC‑TGA‑08 — LaunchGate discipline (incl. pre‑run barrier)** | Each `U.WorkEnactment` has exactly one `LaunchGate` owning `USM.LaunchGuard`; **mandatory** checks: `FreshnessUpToDate`, `DesignRunTagConsistency`. If preceding step’s CV ≠ `pass`, LaunchGate decision is `block` (cause logged). | Owner resolution `GuardOwnerGateId = LaunchGateId(U.WorkEnactment)`; CV≠pass ⇒ `block` with log. |
| **CC‑TGA‑09 — MVPK publication discipline** | Every surfaced node uses MVPK; faces carry `PublicationScopeId`, presence‑pins, **edition ids**, Γ pins; **no I/O duplication** or arithmetic; faces add no new numeric claims. | Cards show `PublicationScopeId`; pins present; no “signature”/math on faces. |
| **CC‑TGA‑10 — Normalize→Compare (CSLC)** | Any comparison cites **UNM/CG‑Spec** editions and **ComparatorSetRef**; ordinal claims are compare‑only; partial orders return sets; edition‑aware artifacts (QD/archives) pin `{DescriptorMapRef, DistanceDefRef, CharacteristicSpaceRef?}.edition`; **any face citing editions includes `BridgeCard + UTS row`**. **NoHiddenScalarization — detection criteria:** (1) return shape is **set/poset**, not scalar; (2) `ComparatorSetRef` is present and edition‑pinned; (3) MVPK faces add **no new numeric claims**; (4) any summarisation is **order‑preserving & set‑valued**; otherwise conformance fails. | Faces show comparator pins; archive pins present; linter rejects edition cites without UTS; scalarisation checks pass.
| **CC‑TGA‑11 — Crossings gated** | Cross‑Context/plane crossings publish **BridgeId + UTS + CL/CL^plane** and are mediated by `OperationalGate(profile)`; **Φ/Φ_plane penalties → R‑lane only**; describedEntity change publishes **KindBridge (CL^k)**. **Exception (StructuralReinterpretation):** a **projection‑only** describedEntity retargeting is surfaced **without** a gate **iff** **CC‑TGA‑06‑EX** holds; then the UTS row includes `bridgeChannel=Kind`, `CL^k`, and a **retargeting witness**; any plane/unit change falls back to a gated crossing; `PathSliceId` is pinned; UNM reuse cross‑context continues via `Transport`. | Crossing surfaces show Bridge/UTS/CL pins; penalties routing audited. |
| **CC‑TGA‑12 — Set‑returning selection** | `U.SelectionAndTuning` returns sets/archives under declared comparators (`ParetoOnly` by default) — no covert scalarization. | Selector output is a set/archive; policy id present if escalated. |
| **CC‑TGA‑13 — Budgeted Selection↔Planning loop** | The loop declares **budget / max_iter**; on expiry selector publishes partial‑optimal set + `MethodTuning`; next **PathSlice** scheduled. | Logs show budget stop and slice rollover. |
| **CC‑TGA‑14 — UNM before loop & Freshness lifecycle** | UNM runs before selection; stale/missing inputs produce **FreshnessTicket/FreshnessRequest** planned in `WorkPlanning` and executed in `WorkEnactment`; calibrations appear as `CalibrateTo(map|standard)` with Φ pins. | Ticket state machine Issued→Planned→Executed→Closed; calibrations pinned. |
| **CC‑TGA‑15 — FinalizeLaunchValues only in WorkEnactment** | Only `U.WorkEnactment` performs `FinalizeLaunchValues` and fills launch‑value slots. | Any earlier attempt blocks at LaunchGate; a `FinalizeLaunchValues` witness is present in Work. |
| **CC‑TGA‑16 — Guard ownership & semantics** | `USM.CompareGuard`/`USM.LaunchGuard` publish owner gate; guards are **events**, not GateChecks; failures are aggregated by owner’s gate per profile. | Guard pins show owner; GuardFail routed to owner’s DecisionLog. |
| **CC‑TGA‑17 — Assurance ops on Transfer** | On `U.Transfer` only `ConstrainTo/CalibrateTo/CiteEvidence/AttributeTo`; none write/update `⟨L,P,E⃗,D⟩`. | Edge audit shows ops; CtxState unchanged across the edge. |
| **CC‑TGA‑17a — Assurance ops contracts (normative)** | **ConstrainTo(region|policy)**: tightens declared region/policy; **pre**: region⊆current; **post**: `⟨L,P,E⃗,D⟩` unchanged; **idem.** and **monotone** under composition. **CalibrateTo(map|standard)**: attaches **editioned** calibration map/standard with Φ‑policy id; lawful per CG‑Spec; **post**: `⟨L,P,E⃗,D⟩` unchanged; **idem.** on same edition; penalties **→ R only**. **CiteEvidence(anchor)**: binds carriers via **SCR/RSCR**; adds no numeric claims; **idem.**; missing carriers ⇒ **abstain**. **AttributeTo(role|source)**: provenance only; decision algebra unaffected; **idem.** Hidden GateChecks, plane/unit changes, or edition writes on edges are **forbidden**. | Contracts visible on edge audit; violations fail lint. |
| **CC‑TGA‑18 — Flow = valuation & slice‑local refresh** | A flow declares valuation `ν` over `U.Transfer` plus `PublicationScopeId` and `PathSliceId`; **sentinel‑bounded** refresh; re‑emit on edition change or sentinel rule. | FlowSpec shows ν; sentinel bump triggers slice‑local recompute. |
| **CC‑TGA‑19 — Γ_time on compare/launch** | All compare/launch faces pin `Γ_time`; no implicit *latest*. | Face audit shows Γ pins; LaunchGate blocks on stale. |
| **CC‑TGA‑19a — Γ_time pin shape (normative)** | The `Γ_time` pin is one of: `snapshot(t)`, `interval[t1,t2]` (closed), or `policy(Γ_timeRuleId)` that resolves to either; CV computations record the **resolved time basis** in `DecisionLog` and do not widen Γ at publication time. | DecisionLog shows basis; linter rejects missing/implicit Γ. |
| **CC‑TGA‑20 — Lean publish‑mode ≠ weaken** | `AssuranceLane‑Lite` affects faces only; required GateChecks for the active profile remain intact. | Gate in Lean/Core shows minimal pins; GateChecks list unchanged. |
| **CC‑TGA‑21 — Decision stability & idempotency witness** | Gate decisions are stable under the equivalence relation defined in **A.41**; a **witness of equivalence** is present on the DecisionLog surface; any change that breaks equivalence requires re‑aggregation. **Minimum lexeme (CV‑relevant surfaces):** `EquivalenceWitness := { keys, E⃗, Γ_time(basis), PathSliceId?, ReturnShapeClass, ComparatorSetRef?, profile }`. | Modify any input outside the declared equivalence ⇒ re‑aggregation; DecisionLog records the witness (A.41); lexeme present.
| **CC‑TGA‑21a — Decision join (publication algebra)** | Aggregation over GateChecks is the **idempotent, commutative, associative join** on the lattice `abstain ≤ pass ≤ degrade ≤ block` with **neutral = `abstain`** and **absorbing = `block`**. The algebra is conceptual; publications surface only (i) the aggregated **GateDecision** and (ii) its **GateDecisionRationale** recorded in the **DecisionLog**. A **GateDecisionExplanation** is an optional human‑readable narrative derived from the GateDecisionRationale; it is **not** a decision and MUST NOT be used as one. If aggregated `ConstraintValidity ≠ pass` or the active profile suppresses narratives, any GateFit‑oriented GateDecisionExplanation **does not apply**. | Review a gate with multiple GateChecks: the aggregated decision matches the lattice join; no per‑check arithmetic is introduced on faces. |
| **CC‑TGA‑22 — Errors/unknowns fold by profile** | Errors/timeouts fold to `degrade` under `Lean|Core` and to `block` under `SafetyCritical|RegulatedX`; `unknown` folds per GateCheck policy (safety‑default: `degrade`). | DecisionLog shows folds; profile switch changes fold behavior accordingly. |
| **CC‑TGA‑23 — SquareLaw on crossings** | For every GateCrossing, `gate_out ∘ transfer = transfer' ∘ gate_in`; LaunchGate case is mandatory. | MVPK shows commuting square; inconsistency yields `block|degrade` per profile. |
| **CC‑TGA‑24 — UNM single‑writer** | `CG‑Spec`, `ComparatorSet`, `UNM.TransportRegistryΦ` editions are authored only by `UNM.Authoring` (others ref‑only). | Authorship cards: UNM is sole writer; others have refs only. |
| **CC‑TGA‑25 — Evidence lanes & DecisionLogs** | AssuranceLane surfaces GateProfile, GateCheckRef list, edition pins, aggregated decision, `DecisionLogRef`; **evidence pins follow a two‑layer scheme**: **carriers** are pinned via **`SCR/RSCR`**, and **value annotations** are surfaced under **`VALATA (VA/LA/TA)`**. | Gate surfaces include these pins; logs retrievable. |

> **Coupling note.** `CC‑TGA‑07 (CV⇒GF)` and `CC‑TGA‑21a (Decision join)` together ensure that any GateFit‑scoped GateCheckRef **returns `abstain`** until the aggregated CV status equals `pass`; CV/GF separation remains intact. 
> **Authoring note (scope of E.TGA vs A.*):** Detailed, mechanism‑level checks and most publication content are specified in the **A.* patterns** (A.20…A.42). E.TGA fixes only carcass‑level obligations above.

**Glossary (additions)**  
* *Open‑world species* — non‑exhaustive domain‑level specializations of `U.Transduction` that map to the minimal kind set.  
* *Signature (TGA kind)* — `U.Transduction(kind=Signature)`; **identical to** **A.6.0** `U.Signature` (universal block). **Not** a `C.3.2 KindSignature`.  
* *KindSignature (C.3.2)* — intensional definition of a `U.Kind` (intent/extent, F); **unrelated** to TGA kinds; never a `genus`.  
* *Species (domain‑level)* — typed specialisations `speciesOf(kind=…)` that **MUST** declare `KindDefinition=A.*` id (e.g., `kind=Mechanism; KindDefinition=A.6.1`).  
* *KindBridge (`CL^k`)* — a compatibility surface on UTS for describedEntity/kind transitions; required by CC‑TGA‑06‑EX and crossings (CC‑TGA‑11).
* *Eulerian interpretation* — operational stance where a flow is treated as a valuation over `U.Transfer` and edges perform assurance‑only operations (no token‑passing semantics).
* **GateCheckRef shape (publication lexeme, normative here).** Where GateChecks are surfaced, a **GateCheckRef** is a record
  `GateCheckRef := { aspect, kind, edition, scope }` with:
  `aspect ∈ {ConstraintValidity, GateFit}`, `kind ∈ GateCheckKind`, `edition ∈ Editions`, and `scope ∈ {lane | locus | subflow | profile}`. 
* **GateDecision / GateDecisionRationale / GateDecisionExplanation (terminology).**
  — **GateDecision** — the aggregated lattice value produced by `OperationalGate(profile)` for a specific `{GateProfile, GateCheckRef[]}`.
  — **GateDecisionRationale** — the minimal structured support **for that GateDecision**: per‑check outcomes, profile‑bound folds, and surfaced evidence/witness references on the DecisionLog; it records **why the GateDecision is admissible** under the active profile.
  — **GateDecisionExplanation** — an optional human‑readable narrative derived from the GateDecisionRationale; it **does not carry decision status**. While aggregated `ConstraintValidity ≠ pass`, GateFit‑scoped checks return `abstain`; any GateFit‑oriented GateDecisionExplanation **does not apply**.
> **Clarity note.** **GateDecision ≠ GateDecisionExplanation**; narratives are optional and derivative of GateDecisionRationale.

* **GateFit (aspect, not an entity).** GateFit names the **aspect** of checks that evaluate **profile‑fit**; there is no separate GateFit entity. “Gate decision under GateFit” means “the gate’s decision computed from GateChecks with `aspect=GateFit`”.

  This shape is publication‑level only; it introduces no new execution steps and no arithmetic on faces.  (Couples to A.20/A.21 without duplicating their check catalogs.)
* *VALATA (VA/LA/TA)* — value‑annotation scheme used on **AssuranceLane**; **carriers** are referenced via **SCR/RSCR**; detailed obligations live in A.10/A.29. Included here so evidence pins are self‑describing in E‑level texts.
* *Transfer vs Transport* — **Transfer** = the sole graph edge kind `U.Transfer`. **Transport** = Φ‑policy/registry‑defined conversions (`TransportRegistry^Φ`) referenced by UNM; “reuse via Transport” refers to the latter.
* *GateCrossing* — a typed node transition that writes/updates a CtxState slot or the kind‑channel; see **S1.b** for the normative list and required pins.
* *Admissible path* — a typed path obeying the GateCrossing discipline (no hidden crossings; witnesses present), Γ‑pinned on compare/launch, and `T^D↔T^R` only at `LaunchGate`; see **S2**.

### E.18:8 - Gating Profiles (applied to E.TGA)

> Gating is expressed as **publication‑gating** per E.17 profiles. The graph model aligns with the **CC items** listed for the chosen profile; higher profiles include all lower‑profile items.

| Profile                          | Required CC‑items                                         | Additional notes                                                                               |                                                                  |
| -------------------------------- | --------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------- |
| **Lean**                         | 01–06, 08–09, 11–12, 15, 19–21, 25                                                                                                           | Minimal MVPK presence; LaunchGate keeps `FreshnessUpToDate` & `DesignRunTagConsistency`. |
| **Core**                         | **Lean** + 07, 10, 13–14, 16–18, 22–23, 24                                                                                                  | Adds CV⇒GF order, CSLC pins, budgeted loop, guards, valuation/sentinel refresh, error folds, SquareLaw, UNM single‑writer. |
| **Safety‑Critical / RegulatedX** | **Core** + profile‑specific GateChecks (safety envelope, regulator id/editions) with stricter folds per **CC‑TGA‑22**; SquareLaw audits tightened | — |

**Recommended defaults (non‑normative, tie‑in to A.26).** Profiles inherit along a `PathSlice`; local overrides may only **add** GateChecks; weakening requires a new `PathSlice` via sentinel (cf. A.26/A.25).

### E.18:9 - TGA LEX discipline (registration)
Register Tech tokens (ASCII) used by this architecture with twin‑labels: `U.TransductionGraph`, `U.TransductionFlow`, `StructuralReinterpretation`, `OperationalGate`, `GateProfile`, `GateCheckRef`, **`GateCheckKind`**, `DecisionLog`, `USM.CompareGuard`, `USM.LaunchGuard`, `KindBridge`, `SubflowRef`, `FlowEmbed`, `SentinelId`, `PathSliceId`, `SliceRefresh`, `FinalizeLaunchValues`, `VALATA`. Add an ASCII alias **`CLKind`** ↔ Plain `CL^k` (cf. `CLPlane` ↔ `CL^plane`). Reference MVPK E.17 naming for faces.  
**CtxState Extension Registry.** Register any extra CtxState slot beyond ⟨L,P,E⃗,D⟩ with: slot id, informal intent, partial‑order law (with neutral/absorbing), SquareLaw compatibility note, and the owning Gate profile(s) that may change it. Absence of registration ⇒ **non‑conformant**.

### E.18:10 - Consequences

**Benefits.**

1. **Universality with discipline:** one edge kind and explicit gates eliminate “second process ladders” and make cross‑domain flows (ML, supply‑chain, TAMP/MPC, scientific workflows) uniformly analyzable and auditable.
2. **Comparability & replayability:** CSLC and edition‑pinned comparators prevent covert scalarization and enable lawful set returns and reproducible decisions.
3. **Locality of change:** sentinel subflows restrict refresh to affected `PathSlice`s; large graphs remain stable under frequent edition bumps.
4. **Clean design/run fold:** LaunchGate and `DesignRunTagConsistency` stop premature launch‑value slot filling; acceptance and telemetry live where they occur (`U.Work`).
5. **Assurance visibility:** MVPK makes GateProfile/DecisionLog surfaces locally checkable and cacheable for the same `{PathSlice, GateChecks, Editions}`.

**Trade‑offs.**
a) **Higher upfront modeling cost:** explicit Bridge/UTS pins and GateProfiles demand care; mitigated by Lean profile and templates.
b) **Longer edge surfaces:** MVPK faces are verbose by design; Lean surfaces can be used for low‑risk segments.
c) **Tooling alignment:** some incumbent DAG‑only orchestrators conflict with budgeted cycles and set‑return semantics; adapters must project E.TGA semantics to their interop layer (never the other way round).

### E.18:10 - Rationale

E.TGA enforces **strict separation of concerns** (carcass‑level only); **specialized semantics live in A.* patterns**:

* **What the graph is:** typed intensional morphisms and a single transport edge `U.Transfer`.
* **Where/when it may cross contexts:** **only** at `OperationalGate(profile)`, with Bridge+UTS, CL/CL^plane, and Φ routed to R‑lane.
* **How comparability works:** UNM authors units/planes/transports (single writer) and selectors operate **only** on normalized, edition‑pinned comparators, returning sets/archives—not totals. **Edition‑aware pins and archive semantics are tested in A.28/A.34/A.37 (not repeated here).**
* **How change propagates:** sentinel‑bounded `PathSlice` refresh; editions are monotone; LaunchGate is the only binder of launch‑values.

This arrangement guarantees **functorial publication** (commuting squares on crossings) and **orthogonality** of inner technical validity (ConstraintValidity) to context fit (GateFit), which in turn makes gate aggregation **order‑independent** and cements the CV⇒GF activation predicate.

### E.18:11 - SoTA‑Echoing (post‑2015, multi‑Tradition)

> Each item states **Adopt / Adapt / Reject**, and why. Vendor/tool tokens are kept as *informative*, not normative.

1. **Applied category theory (compositional open systems).**
   **Adopt.** Monoidal composition and wiring justify “nodes as morphisms, edges as carriers” and functorial publication of faces; they also provide algebraic laws for joining subflows. (Fong & Spivak, *Seven Sketches in Compositionality*, 2019).

2. **Operads / wiring diagrams / hypergraph categories.**
   **Adopt/Adapt.** Typed ports and decorated cospans model interfaces and “Bridge” junctions; we adapt the operadic composition to require CL/Φ pins on every crossing (publication‑level requirement not present in the math). (Spivak, *Operads of Wiring Diagrams*, 2021; Baez & Fong, *A Compositional Framework for Passive Linear Circuits*, 2015).

3. **Open‑graph/string‑diagram rewriting.**
   **Adapt.** Rewriting systems capture subflow refactors, but E.TGA binds rewrites to edition bumps and sentinel scopes rather than global rewrites, to preserve auditability and replay. (Bonchi et al., *Graphical Linear Algebra*, 2019; Kissinger—survey lineage).

4. **Publication discipline & artefact portability.**  
**Adopt.** Edition‑pinning and immutable registries echo contemporary reproducibility practice; E⃗ stays explicit and compositional at the publication layer.

5. **Reproducibility & content addressability.**  
   **Adopt.** Edition‑pinning and immutable registries echo modern content‑addressable reproducibility (conceptual); E⃗ stays explicit and compositional at the publication layer.

6. **TAMP/MPC (integrated planning and control).**
   **Adopt/Adapt.** The budgeted Selection↔Planning loop follows contemporary TAMP practice; MPC‑style freshness/constraint checks motivate **FreshnessUpToDate** as a hard LaunchGate module and “bind‑in‑Work‑only”. (Garrett, Lozano‑Pérez, Kaelbling, *Integrated Task and Motion Planning*, 2021; Rawlings et al., MPC updates).

7. **Quality‑Diversity (QD) search.**
   **Adopt.** QD (e.g., CMA‑ME, 2020) justifies **set‑return** and archive semantics in `U.SelectionAndTuning`; E.TGA bans covert scalarization that would collapse archives to single “bests”.

8. **Profunctor optics (modular projections).**
   **Adopt/Adapt.** Optics motivate view/projection discipline behind MVPK faces; we adapt by forbidding MVPK faces from introducing new claims (they are pure projections, not transformations). (Pickering, Gibbons, Wu, **Profunctor Optics**, 2019).

*Cross‑tradition note.* Items 1–3 (category‑theoretic), 4–5 (publication/reproducibility concepts), 6 (controls/robotics), 7 (evolutionary search), and 8 (PL/semantics) jointly anchor E.TGA across multiple traditions, per E.8.

### E.18:12 - Bias‑Annotation (per E.8 SG‑bias slot)

* **Acyclic‑bias risk.** Tooling accustomed to DAGs may discourage legal feedback loops; E.TGA explicitly permits loops with budget/sentinel controls (CC‑TGA‑13,‑18).
* **Scalarization‑bias risk.** Cultural defaults to single‑score rankings can suppress Pareto/QD sets; E.TGA requires lawful orders and return‑sets (CC‑TGA‑10,‑12).
* **Interop‑dominance risk.** File/format ecosystems (CWL/RO‑Crate/lineage) can leak into semantics; E.TGA places them in **InteropCard** and keeps intensional semantics in nodes/gates.
* **Over‑formalization risk.** Category‑theoretic formalisms can obscure operational guard‑rails; E.TGA grounds crossings in Bridge/UTS/CL/Φ pins and SquareLaw audits (CC‑TGA‑11,‑17).
* **Retrospective rewrite risk.** Global rewrites break replay; E.TGA confines them to edition bumps and slice‑local refresh (CC‑TGA‑16).

**Mitigations.** Profile‑gated publication, audit of `DecisionLog`, mandatory edition pins, Lean‑to‑Core upgrade paths, and conformance tests tied to PathSlice replay.

### E.18:13 - Relations (explicit pattern‑to‑pattern edges)

> Directed edges (→) are typed as **builds_on / constrains / hosts / specializes / publishes_on / requires / provides_checks_for**.

**Foundations**
* **E.TGA →builds_on→ E.17 MVPK (for Morphisms).** Faces, pins, lanes, functorial publication, Lean/Core/Regulated profiles.
* **E.TGA →builds_on→ A.6.0 U.Signature / A.6.1 U.Mechanism.** Node kinds and intensional content boundaries.
* **E.TGA →builds_on→ A.7 Strict Distinction (I/D/S vs Surface).** No new claims on faces; faces project morphisms.

**Flow semantics & checks**
* **E.TGA →hosts→ A.20 U.Flow (ConstraintValidity scope).** CV checks live inside transformations; no declaration/translation of planes/units in CV; **error/timeout/unknown folds** follow **CC‑TGA‑22** as the **minimum default** (profiles may be stricter).
  **Terminology discipline (A.20 boundary).** In CV scope, publications use **status/witness** language; **GateDecisionRationale/GateDecisionExplanation** are reserved for gating and do not apply to CV.
* **E.TGA →hosts→ A.21 GateProfilization (GateFit scope).** **GateFit-scoped GateChecks** are aggregated by `OperationalGate(profile)` with CV⇒GF activation; the **enumeration and publication shape** of GateChecks live in **A.21**. **Equivalently:** a GateFit decision different from `abstain` appears only when aggregated `ConstraintValidity = pass`; otherwise the **GateDecisionExplanation (GateFit‑oriented)** does not apply.
* **E.TGA →requires→ USM.CompareGuard / USM.LaunchGuard.** Guards publish scope & ownership; guard failures route to owner gate.
* **E.TGA →constrains→ F.* (Bridge+UTS, CL/CL^plane, Φ→R).** A transition is treated as a **Crossing** iff `Bridge+UTS` and the appropriate `CL/CL^plane` are surfaced; otherwise this crossing explanation does not apply. Where Φ defines penalties, they appear in the R‑lane only.
* **Operational interpretation (default): Eulerian.** A flow is a **valuation** over `U.Transfer`; edges carry **assurance‑only operations** (see CC‑TGA‑17); no token‑passing semantics are assumed.

**UNM & comparability**
* **E.TGA →constrains→ UNM.Authoring / UNM.Usage.** Single‑writer for `CG‑Spec/ComparatorSet/UNM.TransportRegistryΦ`; normalize‑then‑compare is mandatory.
* **E.TGA →constrains→ G.5 SelectionAndTuning.** Set‑returning, comparator‑pinned decisions, no hidden scalarization; `MethodTuning` without launch‑value slot filling.
* **E.TGA →constrains→ G.11 EvaluatingAndRefreshing.** EditionBumpProposal, two‑phase commit in UNM.Authoring, path‑local refresh.

**Work boundary**
* **E.TGA →requires→ A.15 U.WorkEnactment (`FinalizeLaunchValuesOnlyInWork`).** Single point of `FinalizeLaunchValues`; `FreshnessUpToDate` hard at LaunchGate; acceptance/telemetry published here.

**Structure & reuse**
* **E.TGA →specializes→ U.TransductionFlow (and its family).** The graph architecture is the common substrate on which flow patterns (e.g., P2W, EvaluatingAndRefreshing) are defined; E.TGA ensures their crossings, guards, and MVPK faces are coherent.
* **E.TGA →publishes_on→ E.17 MVPK views** (`PlainView`, `TechCard`, `InteropCard`, `AssuranceLane`) for every edge/node where publication occurs; Lean mode allowed only as per profile.

### E.18:14 - Conformance evidence (how to show you comply)

1. **Model lint:** run static checks for CC‑TGA‑01…25 (edge kind, gates on crossings, CV⇒GF, guard ownership, single‑writer UNM, SquareLaw).
2. **Publication audit:** sample a commuting square and a sentinel‑bounded subflow; verify pins and DecisionLog behavior on *block/degrade*.
3. **Replay test:** freeze editions; re‑run selection on a PathSlice; observe identical return‑sets; apply a bump; see only affected `PathSlice`s refresh.
4. **StructuralReinterpretation probe:** construct a minimal reinterpretation step; confirm `CL^k` with `bridgeChannel=Kind` on UTS, a SquareLaw‑retargeting witness on UTS, `PathSliceId` pinned, **CV.ReinterpretationEquivalence=pass**, and absence of hidden scalarization.

[20]: https://webstore.ansi.org/preview-pages/ISO/preview_ISO%2B23247-1-2021.pdf?srsltid=AfmBOooAUXpg38IpkTlUFtcCpaMVOjivkewJWDIUd1VemIJO91abNEkG "INTERNATIONAL STANDARD ISO 23247-1"

### E.18:End

## E.19 - Pattern Quality Gates: Review & Refresh Profiles

> **Type:** Architectural pattern
> **Status:** Stable
> **Normativity:** Normative

### E.19:1 - Problem frame

FPF evolves by adding and revising patterns. Over time, the framework accumulates two kinds of risk:

1. **Admission risk** — a newly authored pattern can be structurally compliant yet still fail on ontology, semantics, terminology conflicts and vagueness, scope, SoTA in related disciplines, or cross-context hygiene.

2. **Staleness risk** — older patterns can remain internally consistent while drifting away from contemporary practice and newer parts of FPF, current internal vocabulary, or updated neighboring patterns. The result is “quiet decay”: the pattern still reads well, but becomes misleading, incomplete, or incompatible.

FPF already contains many checklists and constraints, but they are distributed across patterns and suites. Authors and reviewers therefore lack a single, repeatable way to answer: *What should be checked, and how deep, before a pattern is admitted or kept?*

### E.19:2 - Problem

Without a unified, explicit review pattern:

* Different reviewers optimize for formal/template compliance and miss deeper ontological, semantic, and naming issues, producing bureaucratic output that does not improve the enforceable contract.
* Authors “optimize for the visible checklist” and miss hidden obligations (lexical discipline, Bridge hygiene, SoTA‑Echoing quality, scope claims, delta‑class impact).
* Legacy patterns accumulate “conceptual bit-rot” and diverge from current practice, current terminology, or current internal invariants.
* The specification’s normative surface becomes harder to trust: compliance becomes a matter of reviewer taste rather than a repeatable gate.

### E.19:3 - Forces

| Force                                   | Tension                                                                             |
| --------------------------------------- | ----------------------------------------------------------------------------------- |
| **Uniformity vs Fit**                   | One universal checklist is simple ↔ different pattern kinds carry different risks.  |
| **Rigor vs Editorial cost**             | Deep audits increase quality ↔ they must remain feasible for routine updates.       |
| **Stability vs Evolution**              | Canon should stay stable ↔ it must absorb new SoTA and correct mistakes.            |
| **Conceptual purity vs Enforceability** | Core must stay tooling‑agnostic ↔ gates must still be actionable and auditable.     |
| **Local meaning vs Reuse**              | Patterns must remain context‑anchored ↔ authors want to reuse ideas across domains. |
| **Freshness vs timelessness**           | Some claims should be evergreen ↔ others decay and must be refreshed on cadence.    |

### E.19:4 - Solution — Profile-based gates for admission and refresh

Establish **Pattern Quality Gates (PQG)**: a conceptual review mechanism that applies **profiles of checks** rather than a single monolithic checklist.

A **Pattern Check Profile (PCP)** is a named bundle of check families. Profiles are **additive**: every review applies a baseline profile, then adds risk-driven profiles as needed.

**Terminology note (disambiguation).** PQG/PCP are editorial review constructs in the authoring plane (Part E). They are distinct from enactment/runtime gating constructs such as `OperationalGate(profile)` / `GateProfile` (A.21), which govern Work transitions and gate decision policies elsewhere in FPF.

**Mint vs reuse.** This pattern mints **PQG**, **PCP**, and the profile IDs **PCP‑BASE/MOD/PRAG/NORM/SOTA/BRIDGE/SUITE/P2W/TERM/DEONT/REFRESH**. It reuses existing FPF terms (e.g., **Delta‑Class**, **DRR**, **Bridge**, **CL**, **SoTA Synthesis Pack**) without changing their meanings.

#### E.19:4.1 - Define the review target

A review **SHOULD** propose revisions to a target pattern (including didactic restructuring) that positively affect downstream usage and interoperability. Formal/template defects (e.g., non‑compliance with E.8 structure or not conforming to RFC deontic terminology) have lower review priority than semantic/ontological defects or non‑SoTA Solutions, but they also **MUST** be corrected.

E.g. if the header block is missing or incomplete, **continue with ontology and semantic review first**. Treat missing header fields as a mechanical defect to patch (PCP‑BASE #7), not as a reason to stop.

The run **SHOULD** give best-known **Delta‑Class (Δ‑0…Δ‑3)** and record an initial **impact radius** (dependent patterns/tests/relations that need be changed due to pattern norms), using existing definitions where available (e.g., the LEX‑AUTH protocol).

#### E.19:4.2 - Apply the baseline profile to every run

Every run MUST include **PCP‑BASE**, reviewer depth SHOULD prioritize the load-bearing surfaces in E.19:4.2.1.

1. **Internal coherence (problem ↔ contract ↔ solution)**
   The Conformance Checklist matches Problem statement and the Solution (no “orphan requirements” and no “unclaimed obligations”).
2. **Lexical discipline & reserved vocabulary**
   Terms and registers follow lexical rules; ambiguous “everyday” synonyms do not silently replace kernel vocabulary.
3. **SoTA‑Echoing minimum compliance (E.8)**
   SoTA‑Echoing satisfies the E.8 obligations applicable to the pattern kind (Architectural vs Definitional), including post‑2015 sourcing and explicit adopt/adapt/reject stances. If a SoTA Synthesis Pack exists for the topic, SoTA‑Echoing binds to it rather than forking an untracked narrative; any divergence of pattern norms from contemporary practice is explicitly stated as such. SoTA‑Echoing **MUST** be non‑decorative: the Solution and other load‑bearing sections **MUST** align with the declared SoTA stance, or explicitly justify any divergence.
4. **Cross-pattern compatibility & impact radius**
   Relations are consistent with declared dependencies and dependents; declared scope/impact is compatible or explicitly limited.
5. **Didactic grounding**
   Archetypal Grounding is present and teaches the concept with concrete anchors, not only abstractions.
6. **Template & section integrity**
   This is lowest priority for review depth and **SHOULD NOT** consume effort that would displace ontology/semantics/modularity/slots/SoTA checks. 
7. **Modularity & contradiction hygiene**
   The pattern **SHOULD NOT** be overloaded or significantly expand obligations/dependencies without an explicit reason and impact record.
   Checks include: scope containment, split/refactor recommendations when warranted, and contradiction scans against neighbor patterns in Relations.
   The pattern SHOULD balance cohesion and coupling across FPF.
   If the pattern defines specialization or layering, it SHOULD NOT mix slot interfaces or parameters from different levels; use explicit `⊑/⊑⁺` or `Uses` cuts instead.

##### E.19:4.2.1 - Triage: spend depth on load-bearing surfaces without making reviews heavier

PQG is meant to increase *semantic and ontological trust*, not to turn every review into an exhaustive editorial audit on form. To keep reviews feasible while improving the important parts:

* Treat **load-bearing surfaces** as the primary depth targets:
  * the pattern’s **Conformance Checklist** (the enforceable contract): keep items universal, cognitively ergonomic, not overly prohibitive, and avoid duplicating checks that belong to other patterns (modularity),
  * **deontic clauses** (`MUST/SHALL/SHOULD/MAY`) that define obligations on the authoring/validation plane (not laws of nature or mathematical facts; ensure an explicit conformance subject),
  * **admissibility constraints** (`Invariant:` / `Well‑formedness constraint:`) that define valid models (cardinality, typing/kinds, totality) and are written as non‑deontic predicates (no RFC keywords inside the predicate),
  * **definitions and mint/reuse decisions** (new terms, renamed terms, scope claims baked into names, names that are not overloaded and are properly chosen),
  * **cross-context / cross-plane claims** (Bridge hygiene and “sameness” assertions),
  * **SoTA** (when the pattern claims state‑of‑the‑art rather than a popular‑but‑outdated solution or vocabulary),
  * **modularity and Slot discipline of A.6.5** that provide evolvability of FPF,
  * **absence of contradictions in a pattern**,
  * **Relations** that define compatibility and impact radius.
* Treat **low-signal surfaces** as “scan-level” unless they change meaning: headings/formatting, micro-typos, stylistic polish, and non-load-bearing narrative refactors, compliance to deontic RFC.
* **Do not block semantic review on template and RFC compliance defects.** Missing header block fields (E.8 H‑5), missing canonical sections, or a missing footer marker are fixable integrity defects. Patch them quickly and continue with the load-bearing surface checks in the same run.
* **Report ordering (impact-first).** In run outputs and remediation patches, prioritize fixes on ontology, semantic, modularity and SoTA-related load-bearing surfaces first; group low-signal formatting/typos into a single hunk at the end unless they change meaning.

#### E.19:4.3 - Add risk-driven profiles

**PCP‑PRAG (Pragmatic utility & adoption)** — Trigger: the pattern is Normative and claims practice guidance.
Checks include: minimally viable example, non-decorative Consequences/Anti-Patterns, and an explicit “So what?” adoption test.

**PCP‑MOD (Modularity & layering discipline)** — Trigger: the review target shows scope creep or level-mixing (e.g., one pattern bundles universal core rules with frame-specific content and discipline-specific method semantics; or it mixes `Intension`/`Description`/`Spec` roles in one object).
Checks include:

* an explicit **core vs extensions** cut (universal invariants are factored into one stable “core”, and extensions reference it rather than re-stating or mutating it),
* no conflation of **specialization vs dependency**: use `⊑/⊑⁺` for refinement/extension and `Uses` for pipelines; do not mix their semantics,
* no conflation of container roles: **Pack vs Kit vs Suite vs Family** are not interchanged, and “family of implementations” is not used as “set of mechanisms”,
* level hygiene: Description-level artefacts do not grow mechanism semantics; MVPK faces remain projections and do not become “the place of truth”,
* slot-discipline hygiene for any ladder: SlotKind invariance is preserved and inherited operations do not gain new mandatory inputs (A.6.5 / A.6.1 specialization discipline).

**PCP‑REFRESH (Staleness & compatibility refresh)** — Trigger: staleness signals are present (e.g., outdated SoTA rows, renamed/superseded Relations targets, terminology drift, or an explicit refresh window in LAT/DRR).
Checks include:

* refresh‑sensitive claims are identified (time‑bounded or ecosystem‑bounded) and either (a) updated with post‑2015 evidence **and** matching Solution changes, or (b) explicitly scope‑limited and labeled as historical lineage,
* Relations are updated to current pattern IDs; deprecations/renames are handled via explicit continuity notes (no silent relabeling),
* the run records a Delta‑Class and impact radius; if the refresh causes Δ‑2/Δ‑3, it emits/updates a DRR pointer and triggers any required harness/Bridge refresh obligations defined elsewhere (E.15/F.15/F.9).

Trigger overrides are permitted but intentionally rare: a run MAY override a triggered profile only when it can show the trigger’s risk is genuinely absent *in this case*, and the record MUST name (a) why the trigger is a false positive here and (b) what compensating check(s) were applied instead.

**PCP‑NORM (Normative contract integrity)** — Trigger: the pattern introduces or changes normative requirements, introduces new conformance items, or shifts downstream obligations.
Checks include:

* **Delta‑Class (Δ‑0…Δ‑3)** and **impact radius** are explicit (what breaks, who depends on this),
* requirements are testable in principle (conceptually), scoped, and non-contradictory,
* downstream patterns cited in Relations are compatible with the new contract.
* where the change is Δ‑2/Δ‑3 or a new normative pattern is being admitted: a DRR exists and references the PQG findings (pointer is sufficient; no duplicated prose).

**PCP‑SOTA (Evidence & SoTA alignment)** — Trigger: the pattern’s Solution asserts “best practice”, “state-of-the-art”, or introduces new synthesis claims.
Checks include:

* each “best practice / SoTA” claim in the Solution is explicitly **bound** to SoTA‑Echoing rows (or to SoTA Synthesis Pack identifiers when used), rather than floating as ungrounded prescription,
* novel synthesis is not presented as established SoTA: it is either (a) framed as a scoped hypothesis with explicit limits, or (b) promoted into/registered as a SoTA Synthesis Pack entry before the pattern is admitted as normative guidance,
* where traditions disagree materially, the pattern surfaces the disagreement and states why it adopts/adapts/rejects (instead of silently selecting one tradition),
* refresh‑sensitive claims (those likely to decay) are explicitly marked with scope limits, timespan notes, or lineage labeling when appropriate.

**PCP‑BRIDGE (Cross‑context/plane reuse integrity)** — Trigger: the pattern imports claims, terms, or norms across contexts, disciplines, or reference planes.
Checks include:

* explicit Bridge usage where required (no silent identity by spelling),
* Congruence / loss is surfaced where applicable,
* any cross-plane reuse is explicitly acknowledged and its penalties do not leak into unrelated assurances.

**PCP‑SUITE (Mechanism-suite integrity)** — Trigger: the review target introduces or revises a suite-level Description that enumerates multiple distinct mechanisms (e.g., `MechSuiteDescription` or a suite specialization) and/or changes suite obligations, contract pins, or suite protocols.
Checks include:

* the suite remains a **Description-level** object: it enumerates member `U.Mechanism.Intension` refs and declares shared obligations/pins, but does **not** define mechanism blocks (`OperationAlgebra`, `Transport`, `Audit`, …) and is not used as a mechanism node,
* membership has **set semantics**: `mechanisms` is duplicates-free and order carries no semantics; any intended ordering is expressed only in `suite_protocols`,
* suite protocols are **closed over membership**: if `suite_protocols` is present, each protocol step references a member mechanism (no “step points outside the suite”),
* the suite is not a family of implementations: it MUST NOT be encoded as a `MechFamilyDescription` (families remain “many realizations of one mechanism”, not “many mechanisms”),
* the suite does **not** mint transport exceptions: any cross-context/plane/kind obligation remains Bridge-only; loss/penalties route to `R/R_eff` only; the suite does not embed CL/Φ/Ψ/Φ_plane tables (references/pins only),
* CG/CN contract pins remain the single contract surface: if suite protocols include numeric comparison/aggregation/scoring, they cite `CG‑Spec` (SCP + Γ-fold + MinimalEvidence) and (where applicable) `CN‑Spec`, rather than duplicating “local CG‑Spec-like” content,
* suite protocols contain **no hidden tails**: if UNM/UINDM/ULSAM are required, the protocol expresses them as explicit `Uses` steps and suite audit obligations cite the chosen mechanism ids/refs (no “implicit normalization/aggregation inside score/compare/select”),
* gate separation is preserved: mechanisms/guards use tri-state `GuardDecision := {pass|degrade|abstain}` and MUST NOT publish `GateDecision` / `DecisionLog`; `block` remains gate-level only (`OperationalGate(profile)`),
* defaults remain single-sourced: portfolio mode, dominance regime, and unknown/failure behavior are either pinned in `TaskSignature` / a single policy map or not claimed; the suite does not define competing defaults,
* when the suite claims reusable outputs, publish/telemetry is explicit and terminates via existing publication surfaces (e.g., G.10 and/or PTM), not as a hidden tail inside a selection step.

**PCP‑P2W (Planned baseline & slot-fillings seam integrity)** — Trigger: the review target introduces or revises WorkPlanning artifacts that pin planned fillers for an owner’s slots (e.g., `SlotFillingsPlanItem` or specializations), and/or introduces view projections of such artifacts.
Checks include:

* the PlanItem remains a **WorkPlanning baseline** (`U.WorkPlan.PlanItem`, `kind = SlotFillingsPlanItem`), not an execution log and not a mechanism,
* planned slot filling stays **WorkPlanning-only**: plan items publish planned fillers/pins (ByValue or `<RefKind>`) and MUST NOT include launch values, `FinalizeLaunchValues` witnesses, gate decisions, or decision logs (these are `U.WorkEnactment` / gate-level only),
* ownership and scope are explicit and non-leaky:
  * the item targets exactly one slot owner via `target_slot_owner_ref`,
  * `target_slot_owner_ref` is a **Description-level, edition-addressable** slot-owner ref (kit/suite) and MUST NOT be a `U.Mechanism.IntensionRef`,
  * the item carries explicit P2W anchors (bounded context; and CG-frame/path-slice/scope anchors when used for legality/selection baselines),
* time is explicit: the item includes `Γ_time_selector` or `Γ_time_rule_ref` (XOR); implicit “latest/current” is nonconformant,
* `planned_fillings` is the authority: duplicate `slot_kind` rows are nonconformant unless the slot owner declares the slot multi-valued; any “indices” are derivable projections and are not maintained independently,
* crossing information is referenced, not duplicated: the plan item (and any associated views) cite CrossingSurface/Bridge/policy-id pins rather than embedding CL/Φ/Ψ/Φ_plane tables or defining transport edges,
* MVPK projections remain projections: any `U.View` face (TechCard/PlainView/InteropCard/AssuranceLane) over a plan item MUST NOT add new claims, MUST NOT introduce “shadow defaults”, and MUST avoid “signature” language (signatures belong to intensional objects),
* if a view publishes edition pins or makes claims about crossing/comparability/selection/launch, it MUST also carry the required audit/ownership pins (UTS + Path pins, crossing pins, applicable guard-owner pins); missing pins are treated as nonconformance and read fail-closed downstream.

**PCP‑TERM (Terminology & naming protocol)** — Trigger: the pattern introduces new terms, new U.Types, new “unified names”, or redefines existing labels.
Checks include:

* “mint vs reuse” decision is explicit,
* naming follows the local-first naming protocol and avoids scope smuggling (roles/metrics/stages baked into labels; overloaded words used as terms with a local sense). Remediation **SHOULD** use F.18,
* deprecated aliases and continuity rules are respected.

**PCP‑DEONT (Deontic clause hygiene: RFC keywords)** — Trigger: the pattern conflates admissibility/validity constraints with deontic obligations (e.g., uses RFC keywords where a non-deontic `Invariant:` predicate is required).
Checks include:
* Deontic requirements are expressed with RFC-style keywords (see H‑8); 
* obligations are not smuggled into prose as informal imperatives. Admissibility/validity constraints are stated non‑deontically as `Invariant:` / `Well‑formedness constraint:` predicates and referenced from the Conformance Checklist when enforceable. 
* **Subject discipline for RFC keywords.** If a sentence uses RFC keywords, its grammatical subject **MUST** be an agent or a publishable artefact (author, reviewer, tool, model, record, validator). RFC keywords **MUST NOT** modify modeled‑world entities (e.g., “Earth”, “RoleAssignment”, “Role”, “holon”) — express those as `Invariant:` / `Well‑formedness constraint:` predicates instead, and (if needed) reference them from CC items.

#### E.19:4.4 - Decision outcomes

A PQG run **MUST** end with (a) a remediation patch (English, unified diff, fenced) and (b) a compact list of blocking findings.

**Remediation payload (patch-first).** The run MUST provide concrete remediation proposals as a unified diff patch in English in a fenced code block (if patch is huge, acceptable have it in separate file to have all needed details without need to excess brevity), accompanied by a short commentary stating (a) the explicit misses found and (b) any remaining work that was intentionally deferred. This is a user interchange convention, not a tool mandate.

**Report ordering (impact-first).** The patch is the primary artifact. In the short commentary, list findings in descending order of expected impact on semantic trust (load-bearing surfaces first). Template/formatting-only issues belong at the end unless they hide missing content.

**Budget discipline (anti‑lint‑worship).** If the run identifies semantic defects in load-bearing surfaces, remediation MUST prioritize those fixes; purely mechanical edits (formatting, micro-typos) MUST be minimized and MUST NOT dominate the patch by volume.

**Noise discipline.** The run record is a human-facing audit trail. It **SHOULD** be sparse: list findings, deferrals, and decisions; do **not** paste full PASS output. No need emitting per-check “passed” lines; only found problems and remediation/fixes matter.

### E.19:5 - Archetypal Grounding — Tell–Show–Show: System / Episteme

| Scenario | `U.System` grounding | `U.Episteme` grounding |
|---|---|
| **Tell** | A safety-critical engineering team proposes a new pattern describing how to gate a subsystem before deployment. The draft looks polished, but it quietly imports domain terms, assumes cross-team equivalences, and introduces obligations that are not listed in its own checklist. | A research group refreshes an older pattern that summarizes how to evaluate evidence strength. The pattern still reads well, but its SoTA references and terminology no longer match current practice, and its Relations point to patterns that were renamed or superseded. |
| **Show (failure without PQG)** | Reviewers focus on whether the idea is good and whether the template exists. The pattern is admitted, but later users disagree on what it requires because the Conformance Checklist is incomplete and key constraints are only in prose. | The pattern remains unchanged because “nothing looks broken”. Over time, it becomes a conceptual fossil: newcomers treat it as current guidance, but it encodes an outdated stance and stale vocabulary. |
| **Show (repair with PQG profiles)** | PCP‑BASE finds missing internal coherence (requirements in prose not reflected in CC). PCP‑TERM finds naming drift and scope-smuggling in new terms. PCP‑BRIDGE finds implicit cross-context identity claims without explicit alignment. The pattern is revised before admission, and the final CC becomes the canonical contract. | Patch provided explicit decision: updated SoTA‑Echoing with post‑2015 guidance and appropriate Solution changes, limit the scope to “historical lineage” where appropriate, and update Relations to current dependencies. The refreshed pattern becomes trustworthy again, and any remaining historical material is clearly labeled as such. |

### E.19:6 - Bias-Annotation

Lenses tested: **Gov**, **Arch**, **Onto/Epist**, **Prag**, **Did**. Scope: **Universal** (applies to all patterns and all clusters).

Bias risks and mitigations:

* **Governance bias (Gov):** reviewers may over-prioritize “compliance posture” and under-prioritize teaching value.
  *Mitigation:* PCP‑BASE includes didactic grounding and internal coherence checks and priority for ontology and semantics, not to form.
* **Epistemic monoculture (Onto/Epist):** SoTA‑Echoing can become single-tradition name-dropping.
  *Mitigation:* require explicit multi-tradition coverage and usage of F.18 for neutral naming.
* **Pragmatic bias (Prag):** a pattern can be “correct” yet unusable.
  *Mitigation:* consequences and anti-patterns remain mandatory sections, surfacing trade-offs and misuse paths.
* **Didactic bias (Did):** narrative quality can be mistaken for truth.
  *Mitigation:* conformance and SoTA‑Echoing sections bind claims to explicit obligations and lineage.

### E.19:7 - Conformance Checklist

| ID | Requirement | Purpose |
| --- | --- | --- |
| **CC‑E19‑1 (Baseline is mandatory).** | Every PQG run **MUST** apply **PCP‑BASE** to the review target. | Ensures a uniform minimum gate across all pattern kinds. |
| **CC‑E19‑2 (Profile selection is auditable).** | The run record **MUST** state (a) the selected PCPs, (b) the trigger(s) for each non‑BASE profile, and (c) any override decisions. Any override of a triggered profile **MUST** record why the trigger is a false positive and what compensating check(s) were applied instead. | Makes depth decisions repeatable and reviewable. |
| **CC‑E19‑3 (Delta‑Class & impact for breaking change levels).** | If the run proposes or accepts a change that is **Δ‑2/Δ‑3** (per E.15), the run record **MUST** include Delta‑Class, an impact radius, and a DRR pointer; it **MUST** confirm that required harness/Bridge refresh obligations are triggered where applicable. | Keeps evolution controlled and compatible with downstream dependencies. |
| **CC‑E19‑4 (Contract coherence is enforced).** | Remediation **MUST** eliminate “orphan” obligations and “unclaimed” requirements by aligning the target pattern’s Conformance Checklist, deontic clauses, and admissibility constraints with its Solution. | Preserves the CC as the enforceable contract surface. |
| **CC‑E19‑5 (Triage & noise discipline).** | The run **SHOULD** prioritize load‑bearing surfaces (e.g. CC, content of deontic clauses and content of admissibility constraints, definitions, Relations, SoTA, modularity) and keep purely mechanical edits (e.g. RFC format of deontic clauses) minimal. Template defects **MUST** be fixed before admission (or before closing a refresh run) but **MUST NOT** be used to skip semantic review. | Improves semantic trust without turning review into lint and RFC compliance worship. |
| **CC‑E19‑6 (Patch-first output).** | The run output **MUST** include a remediation patch (English, unified diff, fenced) and a compact list of blocking findings, ordered by semantic impact (load‑bearing surfaces first). | Ensures actionability and consistent reporting. |

### E.19:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern                       | Symptom                                                          | Why it fails (force violated)                           | How to avoid / repair                                                |
| ---------------------------------- | ---------------------------------------------------------------- | ------------------------------------------------------- | -------------------------------------------------------------------- |
| **Verdict-only review**            | The run ends with “pass/fail” and prose complaints, but no proposed edits. | Raises editorial cost; reduces repeatability.           | Require a remediation payload: patch-first proposed edits + short commentary; treat the patch as the primary artifact. |
| **Single giant checklist**         | Review becomes a long, unfocused ritual that few complete.       | Increases cost; reduces fit and rigor in practice.      | Use a minimal baseline plus triggered profiles.                      |
| **Template-only compliance**       | All headings exist, but obligations are vague and untestable.    | Looks uniform; fails enforceability and auditability.   | Enforce normative clause hygiene and CC/Solution coherence.          |
| **SoTA name-dropping**             | SoTA‑Echoing is a list of buzzwords with no stance.              | Breaks evidence lineage; invites monoculture.           | Require adopt/adapt/reject with reasons per item.                    |
| **Terminology drift by “synonym”** | Authors swap kernel terms for nicer-sounding words.              | Increases ambiguity; harms cross-pattern composability. | Apply PCP‑TERM and require explicit mini-definitions on first use.   |
| **Typos-first review (lint worship)** | Review time goes to formatting and micro-edits while the normative surface, terms, Bridges, modularity, slot discipline and SoTA stance are barely checked. | Raises editorial cost without raising semantic trust. | Use the triage rule: treat load-bearing surfaces as depth targets; satisfy mechanical checks via auditable lint/harness traces when available. |

### E.19:9 - Consequences

| Benefits                                                                         | Trade-offs / Mitigations                                                                   |
| -------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------ |
| **Repeatable admission decisions** — reviewers share a common gate language.     | More explicit editorial work; mitigated by a small baseline and triggered profiles.        |
| **Higher trust in the normative surface** — CC becomes the enforceable contract. | Authors must align prose and CC carefully; mitigated by coherence checks.                  |
| **Controlled evolution** — runs prevent conceptual bit-rot.              | Periodic workload; mitigated by prioritizing high-dependency and high-risk patterns first. |
| **Less hidden drift** — terminology and cross-context reuse become explicit.     | Some drafts will be delayed; mitigated by early profile selection during authoring.        |

### E.19:10 - Rationale

Patterns are both **teaching artifacts** and **normative contracts**. A specification that grows without explicit quality gates becomes a patchwork: locally good, globally inconsistent. A profile-based gate is the smallest structure that keeps reviews repeatable while remaining sensitive to risk and pattern kind.

The baseline profile protects cross-pattern comparability and editorial sanity. Triggered profiles keep depth where it matters: norms, SoTA claims, cross-context reuse, terminology changes, and legacy refresh.

### E.19:11 - SoTA-Echoing — post-2015 review/validation practice alignment

**Evidence binding note.** If a SoTA Synthesis Pack exists for review/validation or refresh discipline in your Context, cite it and keep this section consistent with it; otherwise treat the table below as a provisional seed that should not be duplicated elsewhere without an explicit update record.

| Claim (E.19 need)                                                      | SoTA practice (post‑2015)                                                                                   | Primary source (post‑2015)                                                                  | Alignment with E.19                                                                       | Adoption status                                                                                              |
| ---------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------ |
| Reviews need explicit criteria, not informal taste.                    | Move from folklore validation to explicit validation methods and documented criteria.                       | Riehle et al. (2020), “Pattern Discovery and Validation Using Scientific Research Methods”. | PCPs make criteria explicit; CC coherence is enforced.                                    | **Adopt.** Keep methods lightweight but explicit.                                                            |
| A stable structure improves comparability and reduces ambiguity.       | Standards specify required viewpoints/concerns and consistency rules for descriptions.                      | ISO/IEC/IEEE 42010:2022 (architecture description).                                         | PCP‑BASE includes structural integrity and internal consistency.                          | **Adopt/Adapt.** Adopt conformance mindset; adapt to pattern-language template and didactic grounding.       |
| Pattern writing benefits from explicit guidance plus critique culture. | Pattern-language communities emphasize clear template usage, consequences, and critique for quality.        | Iba (2021), “How to Write Patterns …” (PLoP 2021).                                          | Baseline checks enforce meaningful sections; anti-patterns make critique concrete.        | **Adopt.** Directly supports admission quality.                                                              |
| “Living” guidance needs refresh discipline.                            | Reporting/review guidance is updated and versioned; reviewers must track changes and report deltas clearly. | Page et al. (2021), PRISMA 2020 statement and explanation papers.                           | Runs require explicit decisions and deltas in SoTA‑Echoing. | **Adapt.** Use the “versioned guidance + explicit deltas” principle without importing tool/process mandates. |

### E.19:12 - Relations

* **Builds on:**

  * `E.8` (authoring conventions; canonical section order; SoTA‑Echoing obligations)
  * `E.10` (lexical discipline and reserved vocabulary)
  * `E.9` (design rationale records for changes that affect semantics)
  * `E.15` (authoring/evolution protocol; harness mindset; refresh planning)
  * `A.6.5` (slot discipline; SlotKind/ValueKind/refMode invariants)
* **Coordinates with:**

  * `F.8` (mint vs reuse decisions)
  * `F.18` (local-first naming protocol)
  * `F.9` (cross-context alignment discipline)
  * `F.15` (conceptual harness and regression framing)
  * `E.17` (MVPK / `U.View` projection discipline)
  * `A.6.7` (`MechSuiteDescription` suite-level semantics)
  * `A.15.3` (`SlotFillingsPlanItem` P2W planned-baseline seam)
  * `G.11` (refresh/decay orchestration principles, where applicable)

### E.19:End

## E.20 - Mechanism Introduction Protocol

> **Type:** Architectural pattern  
> **Status:** Draft  
> **Normativity:** Normative  

### E.20:1 - Problem frame

FPF is intentionally **open‑ended**: new `U.Mechanism.*` intensions, suite compositions, and SoTA‑driven wiring modules can be added over time. This flexibility creates a recurrent authoring problem: introducing a new mechanism (or revising an existing one) tends to touch **multiple semantic owners** across Parts A/E/F/G and can easily create drift:

* semantics leak into the wrong plane (e.g., Part G wiring starts carrying mechanism meaning),
* suites degrade into “meta‑mechanisms” or hidden gates,
* planned baselines (WorkPlanning) are conflated with execution witnesses (WorkEnactment),
* token drift breaks public references, or
* the corpus accumulates dangling references and “workpad commitments” without ownership.

This pattern defines a **repeatable, owner‑routed protocol** for introducing mechanisms that keeps the kernel coherent while remaining extensible.

### E.20:2 - Problem

When a new mechanism (or mechanism family) is introduced without an explicit authoring protocol:

1. **Ownership ambiguity** causes partial changes: a suite enumerates a new `…IntensionRef`, but the canonical `U.Mechanism.Intension` card is missing or inconsistent.
2. **Boundary erosion** occurs: suite descriptions start to define mechanism semantics; method wiring starts to redefine kernel meaning; publication/telemetry becomes a hidden tail.
3. **Plan/enactment confusion** appears: planned slot fillings start to carry launch values, witnesses, or gate decisions.
4. **Terminology drift** breaks citations: renames happen silently; tokens fragment across registers; downstream references become unstable.
5. **Review becomes non‑local**: every introduction is a bespoke scavenger hunt across patterns, making training, review, and refresh unreliable.

### E.20:3 - Forces

| Force | Tension |
|---|---|
| **Extensibility vs Kernel stability** | New mechanisms must be addable ↔ kernel surfaces must remain citeable and minimal. |
| **Single semantic owner vs cross‑cutting impact** | Each artifact needs one owner ↔ introducing a mechanism often spans suites, plans, wiring, and lexicon. |
| **Didactic usability vs auditability** | Humans need clear “cards” and examples ↔ obligations/pins must remain checkable and non-leaky. |
| **SoTA evolution vs semantic integrity** | Methods evolve fast ↔ mechanism meaning must not silently shift via wiring updates. |
| **Local naming freedom vs global reference continuity** | Context‑local labels are necessary ↔ references must remain stable across editions and refactors. |

### E.20:4 - Solution — the Mechanism Introduction Protocol (MIP)

#### E.20:4.0 - Terminology note (disambiguation)

*This protocol is an authoring-plane route map.* It is **not** a suite protocol (`SuiteProtocol` in `MechSuiteDescription`) and is **not** a runtime gating mechanism (`OperationalGate(profile)` or any gate-level decision log).  
MIP governs **how changes are routed to their semantic owners**, not how systems execute.

#### E.20:4.0.1 - Mint vs reuse

**Mints:**
* **MIP** — Mechanism Introduction Protocol (this pattern).
* **MIP-run** — an authoring event that applies this protocol to a concrete change set, captured as a short manifest (recorded as a DRR-linked change record or an equivalent, explicitly citeable change artifact).

**Reuses:**
* `U.Mechanism.Intension` / `U.Mechanism.IntensionRef`, suite descriptions (`MechSuiteDescription` and specializations), WorkPlanning plan items (`SlotFillingsPlanItem` and specializations), alias docking (F.18), RSCR triggers (G.Core), and PQG profiles (E.19).

#### E.20:4.1 - Step 1: Classify the introduction

A MIP-run SHALL first classify the change, because different classes have different owners:

1. **New mechanism kind / new archetypal grounding** (new `U.Mechanism.Intension` archetype).
2. **New mechanism intension within an existing kind** (new `…IntensionRef`, new canonical card).
3. **Mechanism revision** (signature/laws/slots/transport/audit semantics change).
4. **Suite change** (membership, obligations, contract pins, suite protocols, suite audit obligations).
5. **Planned-baseline change** (new or revised `SlotFillingsPlanItem` specialization, or changes to its pins).
6. **Wiring change** (new or revised Part‑G extension modules, SoTA method packs, selectors).
7. **Terminology migration** (renames, token splits/merges, register changes).
8. **Deprecation / supersession / retirement** (marking mechanisms/suites/plan items as deprecated, declaring successors, and preserving citeability; apply E.20:4.9.1).

A single MIP-run MAY span multiple classes, but SHALL treat each class with its correct owner routing (below).

#### E.20:4.2 - Step 2: Declare the semantic owner route map (mandatory)

For every new or modified artifact, the MIP-run SHALL declare **exactly one semantic owner** and route the change there. In FPF, an “owner” is a citeable container that can be patched: a `PatternId` (or `PatternId:SectionPath`) for text, a `PatternScopeId = G.x:Ext.*` for wiring modules, or a `DRRId` (E.9) for a decision/rationale record. The declaration SHALL be captured as a **MIP-run manifest** in a citeable change record (typically DRR-linked) listing, at minimum:

* the change class(es) from E.20:4.1,
* each touched artifact → owner → canonical location (expressed as `PatternId:SectionPath` / `PatternScopeId` / `DRRId`, not as prose),
* any new/changed citeable tokens (`…IntensionRef`, `SlotKind` tokens, `PatternScopeId`, etc.),
* the best-known Delta-Class (Δ‑0…Δ‑3) and an impact radius estimate (E.15) when the run is plausibly Δ‑2/Δ‑3,
* intended RSCR trigger types, and
* the PQG (E.19) profile set used to review the run.

**Note (normative).** If the canonical location is a Part‑G wiring module, it SHALL be cited as a `PatternScopeId` (`G.x:Ext.*`) and the module SHALL declare `SemanticOwnerPatternId` (wiring is binding-only; meaning remains owner-routed).

**Canonical owner route map (normative):**

| Artifact / change kind | Semantic owner | Canonical location | Forbidden move |
|---|---|---|---|
| Mechanism intension meaning (ops/laws/invariants, admissibility, slot contract, transport/audit semantics) | **Mechanism card owner** | Designated mechanism-owner pattern | SHALL NOT “define” the mechanism inside a suite or a wiring module. |
| Suite membership / obligations / contract pins / suite protocols | **Suite owner** | `A.6.7` or `A.6.7.<FamilyKey>` | SHALL NOT smuggle mechanism semantics, **acceptance thresholds / gate criteria**, DecisionLogs, or publish tails into the suite. |
| Planned baseline pins (planned slot fillings; edition-pinned refs; explicit time selector) | **WorkPlanning owner** | `A.15.3` + suite-specific specialization (if needed) | SHALL NOT embed launch values, witnesses, or gate decisions in planning. |
| SoTA method/comparator/generator **definitions** (incl. provenance and evaluation semantics) | **SoTA pack owner** | `G.2` (SoTA synthesis packs) | SHALL NOT rephrase SoTA evolution as kernel semantics. |
| Wiring that binds SoTA packs into flows / tasks | **Extension module owner** | `G.x:Ext.*` (`GPatternExtension` with explicit `PatternScopeId`) | SHALL NOT mint new semantics; SHALL bind/wire only. |
| Token renames and drift management | **Lexical owner** | `F.18` (alias docking) + registers per E.10/F.17 | SHALL NOT silently rewrite tokens or break citations. |
| Change causality taxonomy and regression triggers | **RSCR owner** | `G.Core` | SHALL NOT invent ad hoc “reason kinds” scattered in patterns. |
| Project specializations of a mechanism | **Project owner** | `P.*` patterns (using `⊑/⊑⁺`) | SHALL NOT mutate kernel membership to express project variants. |

**Guard (normative).** Any proposed change that cannot name a semantic owner from the table above SHALL be treated as non-normative workpad content and SHALL NOT be relied upon as an architectural commitment. Such content MAY exist only as explicitly-marked workpad material until routed.

#### E.20:4.3 - Step 3: Card-first canonicalization (eliminate dangling refs)

If the introduction adds a new `U.Mechanism.IntensionRef` anywhere (especially inside a suite):

1. The MIP-run SHALL first create a **canonical mechanism card** at the owning pattern location that publishes the `…IntensionRef` and the minimal identity surface (names, intent, and “this is a distinct mechanism”).
2. The card MAY be a **stub** initially, but SHALL reserve:
  * the stable `…IntensionRef` (and its lexical register entry per E.10/F.17),
   * the intended kind/species placement, and
  * a DRR pointer for completing semantics (including any missing register/twin-label work).

Only after (1) is in place MAY suites or protocols enumerate the new `…IntensionRef`.

#### E.20:4.4 - Step 4: Mechanism semantics completion (what “done” means)

**Definition-of-done note (delegated).** MIP uses two completion checkpoints for mechanism cards:

* **Stub done** — a *resolvable canonical target* created to eliminate dangling references (E.20:4.3). A stub **SHALL** (i) exist at the mechanism-card owner’s canonical location, (ii) reserve and publish the stable `…IntensionRef` (and its lexical/register entries), (iii) set `IntensionHeader.status = draft`, and (iv) carry an explicit DRR pointer for completing semantics. A stub **SHALL** also list the *A.6.1* conformance checklist item IDs it does **not** yet satisfy (without duplicating that checklist here). A stub is sufficient to unblock suite/protocol enumeration, but **MUST NOT** be treated as an “introduced” mechanism for reuse/import decisions.
* **Introduced done** — a mechanism card that can be relied upon as a `U.Mechanism.Intension`. “Introduced done” is defined by *A.6.1* conformance: the card **SHALL** satisfy the applicable *A.6.1:7 Conformance Checklist* items (**CC‑UM.\***), with the baseline items designated by *A.6.1* (e.g., **CC‑UM.0** and **CC‑UM.1**) being the minimum requirement.

The list below is **informative** only (semantic orientation); the normative structure and “done” criteria are delegated to *A.6.1*’s CC items to avoid drift between this protocol and the canonical mechanism definition.

To be considered “introduced” (beyond a stub), a mechanism card SHOULD make the following semantic surfaces explicit:

* **Operation surface**: the named operations that the mechanism provides (signature-level intent).
* **Law / invariant surface**: the invariants that govern the operations (incl. legality constraints when applicable).
* **Admissibility surface**: preconditions/eligibility predicates for valid operation (not a gate decision log, and not per-run outcomes).
* **Slot contract**: required inputs/outputs as slot kinds, with stable kinds and explicit ref modes.
* **Specialisation discipline (when `⊑/⊑⁺` is declared):** explicit parent+morphism kind; SlotKind invariance; monotone ValueKind narrowing; no new mandatory inputs to inherited operations (per A.6.1:4.2.1 / CC‑UM.8).
* **Transport**: declarative transport semantics (no hidden crossings; crossings are surfaced via Bridges where required).
* **Audit obligations**: which evidence anchors must exist when the mechanism is used.

If the mechanism introduces new slot kinds shared across a family/suite, apply E.20:4.5.

#### E.20:4.5 - Step 5: SlotKind lexicon discipline (prevent slot drift)

If the mechanism belongs to a suite or family where multiple member mechanisms share slot vocabulary:

1. The suite owner SHALL provide a **suite-level SlotKind lexicon** (or update it if already present) in the suite owner’s canonical location (`A.6.7` / `A.6.7.<FamilyKey>`), or as a dedicated lexicon card explicitly referenced from there.
2. Mechanism cards SHALL cite slot kinds from that lexicon (rather than minting local near-duplicates).
3. New slot kinds SHALL be introduced into the lexicon first, then referenced by member mechanisms. If any citeable `SlotKind` tokens are minted/renamed, apply E.20:4.9.

This step is specifically intended to prevent the “same idea, different slot token” drift that makes planned baselines and audits non‑portable.

#### E.20:4.6 - Step 6: Suite integration (if the mechanism is a suite member)

If the introduction affects a suite (`MechSuiteDescription` or specialization):

1. **Membership set semantics (WF‑MS‑1).** `mechanisms` is a set: duplicates are nonconformant and list order carries no semantics.
2. **Ordering is only in protocols.** If ordering matters, express it only in `suite_protocols`.
3. **Protocol closure (WF‑MS‑2).** If `suite_protocols` is present, then for every `ProtocolStep` in every `SuiteProtocol`, `step.mechanism ∈ mechanisms`.
4. **No hidden tails.** Required stages (e.g., normalization/aggregation/Γ‑fold) are explicit protocol steps; do not hide them inside other steps.
5. **Guard/gate separation.** Suites and mechanisms SHALL NOT publish `GateDecision`/`DecisionLog`. `AdmissibilityConditions` and tri‑state `GuardDecision` remain mechanism-owned; `OperationalGate(profile)` acceptance thresholds and pass/fail criteria remain gate/acceptance-level concerns.
6. **Suite is descriptive only (WF‑MS‑3/4).** Any publish/telemetry continuation is outside the suite protocol and terminates via publication surfaces (packs/modules); suites SHALL NOT define mechanism blocks (`OperationAlgebra`, `LawSet`, `Transport`, `Audit`, …).

**Kernel stability rule (recommended).** If the suite is a kernel suite, and the change adds a new required stage, prefer creating a **suite variant** rather than mutating the kernel membership. If mutation is unavoidable, pair it with terminology continuity (E.20:4.9) and RSCR triggers (E.20:4.10).

#### E.20:4.7 - Step 7: Planned baseline & P2W seam (if planning is affected)

If the mechanism introduction changes what a WorkPlanning baseline must pin (e.g., selected comparator specs, method descriptions, time selector, guard pins):

1. Introduce or revise a `SlotFillingsPlanItem` specialization under the WorkPlanning owner.
2. The plan item SHALL remain planning-only:
   * pins/refs only (ByValue or `<RefKind>`),
   * no launch values,
   * no `FinalizeLaunchValues` witnesses,
   * no gate decisions or decision logs.
   * time is explicit: include `Γ_time_selector` or `Γ_time_rule_ref` (XOR); implicit “latest/current” is nonconformant.
3. The plan item SHALL target exactly one **Description-level, edition-addressable** slot owner via `target_slot_owner_ref` (typically a kit or suite) and SHALL NOT target a `U.Mechanism.IntensionRef`. If a “standalone mechanism baseline” is required, introduce an explicit Description-level slot-owner wrapper (e.g., a mech kit or a suite-of-one) and target that.

This step exists to keep the P2W seam crisp: planning defines **planned fillers**, enactment witnesses **actual runs**.

#### E.20:4.8 - Step 8: Wiring & SoTA updates (keep method evolution out of kernel)

If the introduction involves methods, comparators, selectors, or other SoTA-sensitive choices:

1. Put method/comparator family semantics in **SoTA packs** (G.2) and reference them by edition‑pinned refs.
2. Pin the chosen SoTA refs for a baseline in WorkPlanning plan items (E.20:4.7); wiring consumes pins rather than silently overriding them.
3. Put flow/task binding logic in **wiring modules** (`GPatternExtension`), with an explicit `PatternScopeId` and declared semantic owner.
4. If a SoTA update requires changing a mechanism’s signature/laws, that semantic change SHALL be performed in the mechanism card owner (A.6.1) and SHALL emit RSCR triggers (E.20:4.10).

#### E.20:4.9 - Step 9: Terminology continuity (alias docking)

If the introduction renames any public token or changes canonical naming:

1. Use lexical alias docking (F.18) so old tokens remain citeable.
2. Update registers and twin labels per lexical discipline.
3. Avoid silent rewrites: the MIP-run SHALL make the migration explicit.

#### E.20:4.9.1 - Deprecation / supersession / retirement (preserve citeability)

If the change class includes deprecation/supersession/retirement (E.20:4.1 #8), the MIP-run SHALL preserve reference continuity while making the status change explicit:

1. **Preserve the canonical target.** The deprecated artifact (mechanism card / suite description / plan item / wiring module) SHALL remain resolvable at its canonical location; deprecation MUST NOT be implemented by removal that would break citations.
2. **Keep the public token citeable.** The deprecated token (`…IntensionRef`, suite token, plan-item token, etc.) SHALL remain citeable. If a successor token/name is introduced, the old token SHALL be alias-docked per F.18 (E.20:4.9).
3. **Declare successor (or “no successor”).** The deprecated artifact SHALL declare a successor pointer (or explicitly declare that there is none) using the project’s established deprecation/supersession fields.
4. **Route downstream updates by owner.** Any required suite membership/protocol changes, WorkPlanning pins, or wiring changes SHALL be performed via their respective semantic owners (E.20:4.2), preferably by introducing a suite variant rather than silently swapping kernel membership.
5. **Emit RSCR triggers.** Deprecation/supersession SHALL emit typed RSCR triggers and extend the regression envelope (E.20:4.10), including checks for dangling refs and alias coverage.

#### E.20:4.10 - Step 10: RSCR triggers + regression envelope

A MIP-run that changes any of:
* mechanism signatures,
* suite membership/protocols,
* planned baseline pins,
* slot vocabulary / SlotKind lexicon,
* terminology/alias docking affecting citeable tokens,
* or other reference surfaces

SHALL emit typed RSCR triggers via the RSCR owner and SHALL extend the regression envelope to include, at minimum:

* no dangling `…IntensionRef` enumerations,
* suite membership set semantics + protocol closure,
* guard/gate separation preservation,
* P2W seam preservation (planning vs enactment).

**Guard (normative).** Trigger kind identifiers (e.g., `RSCRTriggerKindId`) SHALL be selected from the RSCR trigger catalogue owned in `G.Core`. A MIP-run SHALL NOT mint ad hoc trigger kinds (“reason kinds”) scattered in arbitrary patterns/modules.

**Manifest hook (recommended).** The MIP-run manifest SHOULD list emitted trigger types and the regression envelope deltas as checkable items.

#### E.20:4.11 - Step 11: Apply PQG profiles (E.19) and close the run

Every MIP-run SHALL be reviewed using PQG (E.19) with:

* **PCP‑BASE** always, and
* the triggered profiles implied by the change class (at least):
  * **PCP‑SUITE** if any suite surface changed,
  * **PCP‑P2W** if any planned-baseline surface changed,
  * **PCP‑TERM** if any new terms/renames are introduced,
  * **PCP‑SOTA** if SoTA packs are introduced/modified,
  * **PCP‑NORM** if the run introduces/changes normative requirements or conformance items,
  * **PCP‑DEONT** if RFC keyword clauses are introduced/modified (or if invariant/predicate vs deontic form is ambiguous),
  * **PCP‑BRIDGE** if cross-context reuse / crossings / bridges are introduced or changed,
  * **PCP‑REFRESH** if refresh-sensitive claims (SoTA lists, “current practice”, enumerations) are touched,
  * plus any applicable modularity / boundary / normativity profiles required by the delta.

**MIP-run outcomes (normative set).**
A reviewed MIP-run SHALL be closed as one of:

1. **Proceed (single change set).**
2. **Proceed via split routing** (mandatory when semantics were placed in the wrong owner; the change is split into owner-correct patches).
3. **Proceed via suite variant** (preferred when kernel stability is threatened by adding new required stages).
4. **Defer** (insufficient semantics; stub exists but completion is DRR-tracked).
5. **Reject** (violates invariants such as suite-as-gate, plan-as-enactment, or semantic owner ambiguity).

### E.20:5 - Archetypal Grounding *(Tell–Show–Show)*

|  | Tell | Show #1 — add a mechanism to an existing suite *variant* | Show #2 — introduce a new mechanism family + suite |
|---|---|---|---|
| **Scene** | Mechanisms evolve: new stages appear, methods mature, and planning surfaces must remain citeable. | A team wants an additional “stage” in a characterization pipeline, but does not want to mutate the kernel suite. | A new domain needs a mechanism kind not yet present in any existing mechanism-profile cluster (for characterization: `A.19.*`), plus a suite that composes several distinct mechanisms with a P2W hook. |
| **Owner routing** | Each artifact has one semantic owner; changes are routed, not smeared. | 1) Add the new mechanism card under the mechanism owner. 2) Add a suite variant under the suite owner. 3) Pin the variant via a planned-baseline specialization. 4) Wire the variant via a `GPatternExtension`. | 1) Add a new archetypal grounding under oner pattern. 2) Add `A.6.7.<FamilyKey>` describing the suite. 3) Add a suite-specific `SlotFillingsPlanItem` specialization. 4) Add SoTA packs + wiring modules. |
| **Card-first** | No suite enumerates a missing `…IntensionRef`. | Create the new `…IntensionRef` card stub first; then update the suite variant membership. | Create the new kind’s canonical card(s) first; then publish suite membership by `…IntensionRef`. |
| **Suite discipline** | Suites are descriptive: membership, obligations, pins, protocols; not mechanisms and not gates. | The variant’s `suite_protocols` explicitly names the new stage; publish/telemetry remains outside the suite. | The new suite defines shared obligations and allowed pipelines without embedding mechanism semantics. |
| **P2W seam** | Planning pins refs; enactment witnesses runs. | The plan item pins the chosen suite variant and any method/spec refs; no launch values or decision logs. | The plan item specialization defines the planned fillers/pins that downstream flows cite. |
| **SoTA updates** | Methods change faster than kernel meaning; wiring is where choices live. | A `GPatternExtension` selects a post-2015 scoring method by edition‑pinned ref; no kernel mutation required. | The family ships method packs and wiring modules; kernel cards remain the semantic source of mechanism meaning. |

### E.20:6 - Bias-Annotation

Lenses tested: **Governance** (semantic ownership, continuity), **Architecture** (boundary hygiene and modularity), **Onto/Epist** (meaning placement and type discipline), **Pragmatic authoring** (reviewability, split routing), **Didactic** (Tell–Show–Show training affordance).

### E.20:7 - Conformance Checklist (normative)

| ID | Requirement | Purpose |
|---|---|---|
| **CC‑E20‑1 (Owner routing declared).** | Every MIP-run **SHALL** provide a MIP-run manifest that lists each new/changed artifact → exactly one semantic owner → canonical location, and each artifact **SHALL** be authored in the owner’s canonical location. | Prevents “floating commitments” and semantic leakage. |
| **CC‑E20‑2 (Card-first canonicalization).** | Any new `U.Mechanism.IntensionRef` enumerated anywhere **SHALL** resolve to a canonical mechanism card (stub allowed) before suite/protocol enumeration. | Eliminates dangling refs. |
| **CC‑E20‑3 (Suite discipline preserved).** | If a suite is touched, it **SHALL** preserve: membership set semantics, protocol closure, no hidden tails, no gate decisions/logs, no publication payloads. | Prevents suite-as-gate and suite-as-mechanism drift. |
| **CC‑E20‑4 (SlotKind lexicon used when shared).** | If mechanisms share slot vocabulary in a family/suite, a suite-level lexicon **SHALL** exist and member mechanisms **SHALL** cite it. | Stops slot token drift. |
| **CC‑E20‑5 (P2W seam preserved).** | If planned baselines are touched, plan items **SHALL** remain WorkPlanning-only (pins/refs only), **SHALL** target exactly one Description-level slot owner via `target_slot_owner_ref` (and **SHALL NOT** target a `U.Mechanism.IntensionRef`), and **SHALL NOT** contain enactment witnesses, launch values, or gate decisions. | Keeps planning and enactment separable and auditable. |
| **CC‑E20‑6 (Kernel stability handled).** | If a kernel suite would gain a new required stage, the change **SHOULD** be expressed as a suite variant; if mutation occurs, it **SHALL** include continuity measures (alias docking and explicit delta). | Minimizes blast radius of kernel edits. |
| **CC‑E20‑7 (SoTA wiring, not kernel semantics).** | Method/comparator choices **SHALL** be represented via SoTA packs and wiring modules; if a SoTA update requires semantic change, it **SHALL** be made in the mechanism owner and not “by wiring”. | Prevents silent semantic shifts. |
| **CC‑E20‑8 (Terminology continuity).** | Any rename affecting citeable tokens **SHALL** use alias docking and register updates; silent rewrites are non‑conformant. | Preserves reference stability. |
| **CC‑E20‑9 (RSCR triggers + regressions).** | Any semantic or reference-surface change **SHALL** emit RSCR triggers and extend the regression envelope to cover dangling refs + suite closure + guard/gate separation + P2W seam. | Makes change impact explicit and testable. |
| **CC‑E20‑10 (PQG coverage).** | Every MIP-run **SHALL** be reviewed under PQG (E.19) with PCP‑BASE and the triggered profiles implied by the change. | Normalizes review and refresh. |
| **CC‑E20‑11 (Deprecation preserves citeability).** | Any deprecation/supersession/retirement action **SHALL** preserve citeability of the deprecated token (alias docking if renamed), keep the canonical artifact resolvable, and declare a successor pointer or “no successor” explicitly (E.20:4.9.1). | Prevents broken citations and orphaned semantics during evolution. |

### E.20:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Symptom | Why it fails | Repair |
|---|---|---|---|
| **Wiring carries semantics** | Part G extensions start redefining what a mechanism “means”. | Meaning becomes edition-fragile and non-local. | Move semantics back to the mechanism owner; keep extensions as binding only. |
| **Suite becomes a meta-mechanism** | Suite text defines ops/laws or embeds thresholds/decisions. | Breaks level separation; creates hidden gate behavior. | Restore suite as description-only; push thresholds to acceptance/gate level. |
| **Plan becomes enactment** | Plan items contain launch values, witnesses, or decisions. | Destroys P2W seam; breaks audit semantics. | Strip enactment content; pin only refs/policies/time selectors. |
| **Kernel churn by convenience** | New required stage is added directly to kernel suite membership. | Expands blast radius; destabilizes citations. | Prefer suite variant; if not possible, pair with alias docking and explicit deltas. |
| **Token drift by silent rename** | “Just rename UNM to …” without aliasing. | Breaks citations and downstream reasoning. | Use F.18 alias docking; update registers explicitly. |
| **Owner ambiguity** | “We’ll put it somewhere later.” | Guarantees incompleteness and drift. | Declare owner up front; otherwise treat as non-normative. |

### E.20:9 - Consequences

**Benefits**
* Mechanism introductions become **trainable and reviewable** (a repeatable route map).
* Reduces drift by enforcing **single semantic ownership** and preventing semantic leakage.
* Keeps suites descriptive and the P2W seam crisp, improving auditability.
* Supports SoTA evolution without destabilizing kernel meaning.

**Costs**
* Introductions require more explicit routing artifacts (owner map, PQG coverage).
* Some changes will be split into multiple patches (by design), which increases authoring overhead.
* Kernel stability discipline can feel “slow” when a team wants a quick mutation.

### E.20:10 - Rationale

Mechanisms are high-leverage semantic units: a small change can affect suites, planned baselines, wiring modules, and audits. Without a protocol, the corpus tends toward **semantic smearing** (meaning duplicated across planes) and **non-local correctness** (you can’t know what changed without reading everything).

Owner‑routed authoring is a pragmatic compromise: it does not require tooling, yet it produces a stable “map of truth” that makes future review and refresh feasible.

### E.20:11 - SoTA-Echoing

| Need | SoTA practice (post‑2015) | Primary source (post‑2015) | How MIP aligns |
|---|---|---|---|
| Explicit concerns and viewpoints for architecture evolution | Architecture descriptions separate concerns, viewpoints, and stakeholder needs | ISO/IEC/IEEE 42010:2022 | MIP forces explicit owner routing and separates semantic planes (kernel vs wiring vs planning). |
| Repeatable evaluation of pattern quality and change admission | Pattern validation uses explicit criteria and review profiles | Riehle et al., 2020 | MIP requires PQG coverage with triggered profiles rather than ad hoc review. |
| Grounding abstract guidance in teachable vignettes | Pattern languages emphasize grounded, repeatable “Tell–Show–Show” teaching | Iba, 2021 | MIP includes archetypal grounding to make the protocol teachable. |
| Bounded context ownership and boundary hygiene | Context mapping emphasizes ownership and explicit boundary contracts | Vernon, 2016 | MIP’s owner route map is a boundary discipline applied to spec authoring. |
| Modular vocabularies for knowledge systems | Knowledge graph practice emphasizes modular vocabulary control and stable identifiers | Hogan et al., 2021 | MIP’s lexicon discipline + alias docking preserve stable references under evolution. |

### E.20:12 - Relations

**Builds on:**
* **E.8** (pattern structure and normative authoring discipline)
* **E.10 / F.17–F.18** (lexical registers, twin labels, alias docking)
* **E.19** (PQG/PCP profile-based review)
* **E.15** (evolution discipline; DRR/edition thinking)

**Coordinates with:**
* **A.6.1** (`U.Mechanism.Intension` ownership)
* **A.6.7** (`MechSuiteDescription` integrity)
* **A.15.3** (`SlotFillingsPlanItem` and planned baseline seam)
* **E.18** (E.TGA flows that cite planned baselines)
* **G.Core** (RSCR trigger catalogue)
* **G.2** (SoTA synthesis packs)
* **G.x:Ext.\*** (wiring modules via `GPatternExtension`)

**Constrains:**
* Any change set that introduces or revises mechanisms, suites, planned baselines, or wiring in a way that affects citeable surfaces.

### E.20:End

# **Part F — The Unification Suite (U‑Suite): Concept‑Sets, SenseCells & Contextual Role Assignment**

# Cluster F.I — context of meaning & Raw Material

## F.0.1 - Contextual Lexicon Principles

> **One‑sentence summary.** All meanings in FPF are **local to a `U.BoundedContext`** (“Context of meaning”); terms are **spoken with their Context**, and any relation **across Contexts** exists **only** as an explicit **Alignment Bridge** with stated loss/fit.

**Status.** Architectural pattern.
**Builds on:** A.1.1 `U.BoundedContext` (formal frame); A.7 *Strict Distinction* (C‑6); A.8 *Universal Core* (C‑1); A.11 *Ontological Parsimony* (C‑5); A.4 *Temporal Duality* (C‑7); **E.10.D1 D.CTX** (lexical discipline for “Context”).
**Coordinates with.** **F.1** (Context Map via Context Cards), **F.2** (local term capture), **F.3** (intra‑Context clustering), **F.7** (Concept‑Set Table), **F.9** (Alignment & Bridge), **B.3** (Trust & Assurance; CL penalties).

> **Didactic note.** In the Tech register, **Context ≡ `U.BoundedContext`** (per E.10.D1). We use “Context of meaning” as a **metaphor only**; *Context* remains the normative short form for `U.BoundedContext`. The word **anchor** is not used in FPF.

> **Didactic note.** In the Tech register, **Context ≡ `U.BoundedContext`** (per E.10.D1). We use “Context of meaning” as a **metaphor only**; *Context* remains the normative short form for `U.BoundedContext`. The word **anchor** is not used in FPF. The word *plane* is reserved to **CHR:ReferencePlane** only.

**Terminology guard (normative, Part F).** The **row classifier** is **senseFamily**: {Role | Status | Measurement | Type‑structure | Method | Execution}. **Characteristic** (MM‑CHR) names measurable aspects only (A.17–A.19) and MUST NOT be used for row typing in Part F. Avoid the generic word **facet** in Part F; when unavoidable, reference **C.3.5 KindAT (informative facet)** or **Compose‑CAL `U.Facet`** explicitly. Only **CHR:ReferencePlane** is permitted (no bare “plane”); use **I/D/S layer** for intension/description/specification; use **stance** for design vs run.

### F.0.1:1 - Problem Frame

Trans‑disciplinary modelling fails without an explicit discipline for **where words mean what**.

* **Semantic drift.** The same string (“process”, “role”, “service”) slides between domains and editions.
* **Homonym collisions.** One label carries incompatible senses across fields.
* **Hidden synonymy.** Different labels point to the same local sense, but the identity is unstated.
* **Implicit globalism.** Meaning is treated as universal; integration silently re‑writes models.

FPF resolves this by **localising** meaning first, then **explicitly translating** across locales.


### F.0.1:2 - The Three Principles (normative)

#### F.0.1:2.1 - P‑S - **Source Localisation Principle** — *Speak with the Context.*

**Rule.** Every term in a normative FPF artefact **MUST** be bound to a **specific `U.BoundedContext`** (its “Context of meaning”). The binding is explicit in text, notation, or table headers (e.g., **process (BPMN 2.0)**).

**Implications.**

* No free‑floating “global terms”.
* A finite **Context Map** (see **F.1**) is chosen **before** naming work starts.
* If a source intrinsically fixes time stance, the **design/run tag** is carried by the Context (C‑7).

**Reasoning move (conceptual).**
`Context(C) ∧ says(C, term t) ⊢ usable(t@C)`

**Illustration (Enactment line).**
`activity @ PROV‑O (run)` vs `task @ IEC 61131‑3 (run)` vs `process @ BPMN 2.0 (design)`.


#### F.0.1:2.2 - P‑L - **Local Meaning Principle** — *Meaning lives inside the Context.*

**Rule.** The **intended sense** of a term is established **inside its Context** as a **SenseCell**: a small, reconstructible unit of local meaning with **Tech/Plain labels** and a concise gloss. SenseCells are **lexical only** (C‑6): no behaviours, no deontics, no equations.

**Implications.**

* SenseCells are **Context‑scoped**; they do **not** cross Contexts.
* Minimal generality (G‑1) and contextual specification (G‑2) govern naming inside the Context.
* **Intra‑Context clustering** of raw mentions precedes any Cross‑context act (see **F.3**).

**Reasoning move (conceptual).**
`usable(t@C) ∧ fits(gloss, C) ⊢ SenseCell⟨t@C⟩`

**Illustration (KD‑CAL).**
`observation @ SOSA/SSN`: Tech “observation”, Plain “measurement act”; gloss “Result‑bearing act applying a Procedure…”.


#### F.0.1:2.3 - P‑B - **Explicit Bridge Principle** — *across Contexts, only with a bridge.*

**Rule.** Any relation between terms from **different** Contexts **MUST** be stated as an **Alignment Bridge** (see **F.9**): a named mapping between **SenseCell⟨-⟩** items with a declared **relation kind** (e.g., *overlaps*, *broader‑than*, *near‑equivalent*) and a **Congruence Level (CL)** for trust calculus (B.3).

**Implications.**

* No by‑name identity across Contexts; **string equality ≠ sense equality**.
* Bridges carry **loss/fit notes** and are auditable; they can be revised by edition.
* Concept‑Sets (F.7) are built **from bridged cells**, not from surface strings.
* When the surface prose uses umbrella sameness/alignment tokens (“same/equivalent/align/map/…”), treat it as an RPR trigger and repair it via **A.6.9 (RPR‑XCTX)** before granting any naming or substitution licence.

**Reasoning move (conceptual).**
`SenseCell⟨x@A⟩ ↔⟨rel, CL⟩ SenseCell⟨y@B⟩ ⊢ translatable(x@A, y@B, rel, CL)`

**Illustration (Sys‑CAL × Enactment).**
`actuation @ CTRL‑Text` ↔⟨near‑equiv, CL=2⟩ `control‑output @ IEC 61131‑3`.


### F.0.1:3 - Minimal Artefacts (conceptual, notationally neutral)

> These artefacts are **thought‑objects**; they specify **what must exist conceptually**, not how it is stored.

#### F.0.1:3.1 - **Context Card** (for each `U.BoundedContext`)

A terse descriptor used in the **Context Map** (F.1):

* `id` (stable local handle) - `title` - `edition/year`
* `family` (discipline family; informal) - `scope gist`
* `timeStance?` (`design` / `run`, if inherent)
* `trip‑wires` (few lexical caveats that often mislead, e.g., “*process*≠thermo process”)

#### F.0.1:3.2 - **SenseCell** (unit of local meaning, inside one context)

* `label.tech` / `label.plain` (two registers)
* `gloss` (minimal generality, Context‑true)
* `notes?` (warnings, edition shifts)
* **No** behaviour/deontics/equations (C‑6)

> **Where it comes from.** F.2 describes how SenseCells can be *derived* from local term evidence; F.0.1 only **requires** that local meaning be expressible as a SenseCell.

#### F.0.1:3.3 - **Alignment Bridge** (between SenseCells from different Contexts)

* `left: SenseCell⟨-@A⟩`, `right: SenseCell⟨-@B⟩`
* `relation` (e.g., *equivalent‑under‑assumptions*, *overlaps*, *broader‑than*)
* `CL` (Congruence Level; feeds B.3 Trust & Assurance)
* `loss/fit` (explicit statement of what is lost or assumed)


### F.0.1:4 - Invariants (normative)

1. **I‑1 - Context‑qualified usage.** Every normative use of a term is **Context‑qualified** (directly or via table/section headers).
2. **I‑2 - Local‑only cells.** A SenseCell belongs to **exactly one** Context.
3. **I‑3 - senseFamily hygiene.** SenseCells are **lexical**; behaviour, deontics, measurements, proof steps live in their respective patterns (C‑6). 
4. **I‑4 - Time stance fidelity.** If a source fixes `design/run`, the Context Card **carries** it and SenseCells **inherit** it.
5. **I‑5 - No implicit Cross‑context identity.** Cross‑context relations exist **only** as F.9 Bridges with `relation` and `CL`.
6. **I‑6 - Parsimony & heterogeneity hook.** The Context Map is **finite**, **heterogeneous** (≥ 3 families per unification line), and **parsimonious** (F.1).


### F.0.1:5 - Reasoning Primitives (judgement schemata; pure, side‑effect‑free)

*These capture **allowable mental moves**; they do not prescribe storage, APIs, or workflow.*

* **Context qualification**
  `Context(C) ∧ mentions(C, s) ⊢ uses(s@C)`
  *Reading:* If a string *s* is used under Context *C*, we treat it as the local term *s\@C*.

* **Local sense formation**
  `uses(t@C) ∧ gloss_C(t) ⊢ SenseCell⟨t@C⟩`
  *Reading:* A Context‑true gloss yields a SenseCell for *t* inside *C*.

* **Admissible Cross‑context relation**
  `SenseCell⟨x@A⟩ ∧ SenseCell⟨y@B⟩ ∧ declare(rel, CL) ⊢ Bridge(x@A, y@B, rel, CL)`
  *Reading:* Only an explicit declaration generates a Bridge; no name‑matching inferences.

* **Bridge‑to‑Concept‑Set hint** *(for F.7)*
  `Bridge(x@A, y@B, rel≈equiv, CL≥k) ⊢ candidate_same_row(x, y)`
  *Reading:* Strong, near‑equivalence bridges can *nominate* cells for one Concept‑Set row (final decision in F.7).


### F.0.1:6 - Didactic Metaphor (informative)

* **Contexts.** Each `U.BoundedContext` is a **Context**; its **Context Card** is a sign on the door (name, edition, time stance, trip‑wires).
* **Words in a Context.** A **SenseCell** is a dictionary entry pinned to that Context’s wall.
* **Door‑to‑door links.** An **Alignment Bridge** is a labelled passage connecting two Contexts; a **CL** placard says how trustworthy that passage is.

> *We first speak inside Contexts; only then decide which doors to connect—and with what warnings.*


### F.0.1:7 - Placement & Flow

**F.0.1** is the **front door** of Part F. It enables:
**F.1** (choosing Contexts with Context Cards) → **F.2** (deriving SenseCells inside each Context) → **F.3** (stabilising local senses) → **F.7** (building Concept‑Set rows) → **F.9** (stating Bridges).

### F.0.1:8 - Anti‑patterns & remedies

| #       | Anti‑pattern (what goes wrong)   | Symptom in models                                          | Why harmful (conceptual)                            | Remedy (this pattern’s clause)                                                            |
| ------- | -------------------------------- | ---------------------------------------------------------- | --------------------------------------------------- | ----------------------------------------------------------------------------------------- |
| **A1**  | **Global term** (Contextless usage) | “process”, “service”, “role” used without a Context mark      | Meaning drifts; integration silently rewrites sense | **P‑S**: Always speak **term\@context**; qualify via section/table headers if repeated       |
| **A2**  | **String‑match identity**        | Equating *service* (ITIL) with *service* (web‑API) by name | String equality ≠ sense equality                    | **P‑B**: Cross‑context relations exist only as **Bridges** with `relation`+`CL`              |
| **A3**  | **senseFamily mixing in SenseCell**    | Local glosses include behaviours, deontics, equations      | Violates **Strict Distinction** (C‑6); blocks reuse | **P‑L**: SenseCell is **lexical only**; behaviour/deontic math belongs to FPF patterns   |
| **A4**  | **Edition blur**                 | Citing “BPMN” or “ITIL” without edition                    | Underspecified Context; un‑auditable sense shift       | **Context Card** carries `edition/year`; treat materially changed editions as distinct Contexts |
| **A5**  | **Context as type**              | Declaring “PROV‑O is‑a BPMN”                               | Implies inherited meanings between Contexts            | Contexts aren’t types; **no is‑a on Contexts** (E.10.D1). Use Bridges only                       |
| **A6**  | **Bridge without loss/fit**      | Bridge declared as “equivalent” with no assumptions        | Users infer total identity; trust calculus blind    | **P‑B**: Bridge must state `relation` and `CL`, plus a brief **loss/fit** note            |
| **A7**  | **Row from strings**             | Concept‑Set rows built from surface forms                  | Homonyms/synonyms contaminate rows                  | Build rows from **SenseCells**; add only cells connected by acceptable Bridges (F.7)      |
| **A8**  | **Transitivity overreach**       | Chaining weak near‑equivalences as if exact                | Inflates sameness; hides mismatch                   | **Bridge composition** (Sec. 10): compose with **min‑CL** and keep relation weakening     |
| **A9**  | **Domain ≡ Context**                | “Domain” name used as if it were a `U.BoundedContext`      | Domain families are informal; Contexts are formal      | Keep **Domain family** informative on Context Cards; meanings bind to **Contexts** only         |
| **A10** | **Time‑stance confusion**        | Treating `design` and `run` senses as identical            | Crosses senseFamilies; erases execution/spec split         | Carry **time stance** on Context Cards; prefer `design‑spec‑of` / `run‑trace‑of` Bridges     |


### F.0.1:9 - Compact worked examples

> *Each vignette shows (1) two Context Cards (abridged), (2) SenseCells inside Contexts, (3) the Bridge with relation & CL, and (4) a Concept‑Set hint (if any).*

#### F.0.1:9.1 Enactment × Provenance — *process* vs *activity*

* **Context A**: `BPMN_2_0` - *Business Process Model and Notation v2.0 (2011)* - *design*
  **SenseCell⟨process\@BPMN⟩**: Tech “process”; Plain “workflow process”; Gloss “graph of flow nodes/events executed by participants.”

* **Context B**: `PROV_O_2013` - *W3C PROV‑O (2013)* - *run*
  **SenseCell⟨activity\@PROV⟩**: Tech “activity”; Plain “provenance activity”; Gloss “time‑bounded occurrence using/generating entities.”

* **Bridge**: ⟨process\@BPMN⟩ ↔⟨`design‑spec‑of`, **CL=2**, loss: “no concurrency semantics in trace”; fit: “maps to execution plan”⟩ ⟨activity\@PROV⟩

* **Concept‑Set hint**: *No* same‑row nomination (relation ≠ near‑equiv); instead, record a **design↔run** linkage.


#### F.0.1:9.2 - Control × PLC runtime — *actuation* vs *control output*

* **Context A**: `CTRL_Text_Classic` - *control theory primers* - *design*
  **SenseCell⟨actuation\@CTRL⟩**: Tech “actuation”; Plain “control output”; Gloss “signal applied to plant actuators.”

* **Context B**: `IEC_61131_3` - *PLC languages* - *run*
  **SenseCell⟨q‑output\@IEC⟩**: Tech “control‑output”; Plain “PLC output”; Gloss “program‑produced output variable to field I/O.”

* **Bridge**: ⟨actuation\@CTRL⟩ ↔⟨`near‑equivalent`, **CL=2**, loss: “hardware/scan‑cycle specifics absent in CTRL”; fit: “semantics align under linear regime”⟩ ⟨q‑output\@IEC⟩

* **Concept‑Set hint**: *Candidate same‑row* (F.7) with note: “merge permitted at **CL≥2** threshold.”


#### F.0.1:9.3 Measurement × Service — *observation* vs *service metric*

* **Context A**: `SOSA_SSN_2017` - *sensing/observations* - *run*
  **SenseCell⟨observation\@SOSA⟩**: Tech “observation”; Plain “measurement act”.

* **Context B**: `ITIL4_2020` - *services* - *(mixed)*
  **SenseCell⟨slo‑metric\@ITIL⟩**: Tech “service‑level metric”; Plain “service measure”; Gloss “quantity used to evaluate SLOs.”

* **Bridge**: ⟨observation\@SOSA⟩ ↔⟨`provides‑value‑for`, **CL=2**, loss: “organizational context not in SOSA”; fit: “metric results are measurement results.”⟩ ⟨slo‑metric\@ITIL⟩

* **Concept‑Set hint**: Not a same‑row case; this is a **role‑in‑use** relation (measurement feeds status evaluation).


#### F.0.1:9.4 Type reasoning — *subclass‑of* (OWL) vs *is‑a (plain)*

* **Context A**: `OWL2_Profiles` - *description logics*
  **SenseCell⟨subclass\@OWL⟩**: Tech “subclass‑of”; Plain “is‑a”.

* **Context B**: `ENG_Glossary` - *engineering plain usage compendium*
  **SenseCell⟨is‑a\@ENG⟩**: Tech “is‑a (engineering)”; Plain “kind‑of”; Gloss “informal subsumption in specs.”

* **Bridge**: ⟨subclass\@OWL⟩ ↔⟨`near‑equivalent`, **CL=1**, loss: “OWL formal constraints absent in ENG”; fit: “intended subsumption semantics.”⟩ ⟨is‑a\@ENG⟩

* **Concept‑Set hint**: Keep separate rows unless the consuming artefact demands **formal** semantics.


#### F.0.1:9.5 Deontics × Access — *permission* vs *role (RBAC)*

* **Context A**: `ODRL_2_2` - *policy/deontics*
  **SenseCell⟨permission\@ODRL⟩**: Tech “permission”; Plain “allowed action”.

* **Context B**: `NIST_RBAC_2004` - *access control*
  **SenseCell⟨role\@RBAC⟩**: Tech “access‑role”; Plain “permission set”.

* **Bridge**: ⟨permission\@ODRL⟩ ↔⟨`member‑of‑set‑in`, **CL=2**, loss: “contextual obligations not preserved”; fit: “RBAC roles aggregate permissions.”⟩ ⟨role\@RBAC⟩

* **Concept‑Set hint**: Not same row (different **kinds**); useful linkage for Enactment when binding duties to sessions.


### F.0.1:10 - Extended reasoning moves (pure judgement schemata)

> *Judgements are conceptual entailments over Contexts, SenseCells, and Bridges. They carry no storage, workflow, or governance semantics.*

#### F.0.1:10.1 - Context‑qualified use

`Context(C) ∧ mentions(C, s) ⊢ uses(s@C)`
*If s is used under Context C, we treat it as the local term s\@C.*

#### F.0.1:10.2 - Sense formation (local)

`uses(t@C) ∧ gloss_C(t) ⊢ SenseCell⟨t@C⟩`
*A Context‑true gloss yields a SenseCell inside C.*

#### F.0.1:10.3 - Admissible Bridge (creation predicate)

`SenseCell⟨x@A⟩ ∧ SenseCell⟨y@B⟩ ∧ A≠B ∧ rel∈R ∧ cl∈{0,1,2} ⊢ Bridge(x@A,y@B,rel,cl)`
*Only explicit relation `rel` with Congruence Level `cl` constitutes a Bridge.*

**Canonical relation set `R` (didactic catalogue):**
`equivalent‑under‑assumptions` - `near‑equivalent` - `overlaps` - `broader‑than` - `narrower‑than` - `design‑spec‑of` - `run‑trace‑of` - `representation‑of` - `member‑of‑set‑in` - `provides‑value‑for`.

#### F.0.1:10.4 - Bridge composition (attenuating)

`Bridge(a,b,rel₁,cl₁) ∧ Bridge(b,c,rel₂,cl₂) ⊢ Bridge*(a,c,rel*,cl*)`

* `cl* := min(cl₁, cl₂)` (do **not** inflate confidence)
* `rel* := weaken(rel₁, rel₂)` (e.g., near‑equiv ∘ overlaps → overlaps)

*Reading:* Chained passages degrade to the weakest link.

#### F.0.1:10.5 - Non‑identity by stance

`SenseCell⟨x@A(design)⟩ ∧ SenseCell⟨y@B(run)⟩ ∧ ¬declared(Bridge(x,y,near‑equiv,_)) ⊢ ¬same‑row(x,y)`
*Different time stances forbid same‑row unless an explicit near‑equiv Bridge exists.*

#### F.0.1:10.6 - Row viability (Concept‑Set candidacy)

`Cells = {c₁…cₙ} ⊢ row‑viable(Cells) ⇔ connected(Cells, Bridges_{rel∈{equiv,near‑equiv}, cl≥k}) ∧ ¬contradiction(Cells)`

*Reading:* A row is viable if its cells form a connected subgraph via sufficiently strong Bridges and contain no mutually exclusive links.

#### F.0.1:10.7 - Contradiction sieve

`Bridge(a,b,broader) ∧ Bridge(a,b,narrower) ⊢ contradiction(a,b)`
*Incompatible relations across the same pair flag a contradiction for review (conceptually).*

#### F.0.1:10.8 - Non‑bridge implication ban

`name(x) = name(y) ∧ A≠B ⊢ ¬Bridge(x@A, y@B, _, _)`
*String equality across Contexts never implies a Bridge.*


### F.0.1:11 - SCR/RSCR acceptance checks (conceptual)

> *These checks are **content‑oriented**; they validate that a manuscript/model respects Part F principles. No process/tool assumptions are implied.*

#### F.0.1:11.1 - SCR — Static conformance

* **SCR‑F01 (Context‑qualified).** Every normative term is Context‑qualified (directly, or via a scoped header that unambiguously fixes the Context).
* **SCR‑F02 (Local cells).** Each SenseCell belongs to **exactly one** Context; no cell aggregates Cross‑context **senses**.
* **SCR‑F03 (senseFamily hygiene).** SenseCell glosses contain no behaviours/deontics/equations; those appear only in their patterns.
* **SCR‑F04 (Bridges explicit).** Every Cross‑context relation appears as a Bridge with `relation` and `CL` and a short **loss/fit** note.
* **SCR‑F05 (No string identity).** There is no use of string equality to stand in for Cross‑context identity.
* **SCR‑F06 (Time stance fidelity).** Where a Context fixes `design/run`, the SenseCells and any Bridges reflect that stance explicitly.
* **SCR‑F07 (Row viability).** Any Concept‑Set row shown is supported by a connected subgraph of Bridges with **CL ≥ threshold** and no contradictions.

#### F.0.1:11.2 - RSCR — Regression & evolution

* **RSCR‑F01 (Edition split).** When a source edition changes materially, SenseCells tied to the old edition remain; new cells bind to the new Context; Bridges are re‑assessed.
* **RSCR‑F02 (Bridge stability).** If any Bridge endpoint changes gloss/stance, downgrade or retire the Bridge, documenting the **loss/fit** change.
* **RSCR‑F03 (Composition guard).** When composing Bridges in a chain, the resulting `CL` never exceeds the minimal link; relation weakens monotonically.
* **RSCR‑F04 (Heterogeneity + QD guard):** requires ≥3 domain‑families AND MinInterFamilyDistance ≥ δ_family (per the active F1‑Card edition), with QD‑triad evidence (publish Diversity_P and IlluminationSummary on the declared grid/kernel). Near‑alias pairs (per dSig rule) SHALL be flagged and excluded or merged before the guard is evaluated. Record the F1‑Card edition id.

#### F.0.1:11.3 - Publish‑ready summary

An artefact is **ready** with respect to F.0.1 when:

1. **SCR‑F01…F07** hold for all terms, cells, rows, and bridges it presents;
2. **RSCR‑F01…F04** hold under simulated edition/stance changes;
3. Every Cross‑context statement can be read as a **Bridge** or as a composition of Bridges with stated attenuation.


### F.0.1:12 - Quick reference (didactic)

* **Context** = a `U.BoundedContext` with edition, scope, and (if inherent) time stance.
* **SenseCell** = the minimal, lexical unit of meaning inside a Context (Tech/Plain labels + gloss).
* **Bridge** = the only Cross‑context relation, labelled with `relation` and **CL**, plus a short loss/fit note.
* **Concept‑Set row** = a didactic table row collecting **SenseCells** that are sufficiently the‑same‑thing under declared Bridges.

> **Mental checklist:** *Name the Context → speak in the Context → connect Contexts only by labelled bridges → build rows from bridged cells.*

### F.0.1:End

## F.1 - Domain‑Family Landscape Survey

**“Fix the context of meaning before you name anything.”**
**Status.** Architectural pattern.
**Depends on.** E.10.D1 **Lexical Discipline for “Context” (D.CTX)**; **F.0.1 Contextual Lexicon Principles**; A.7 **Strict Distinction (Clarity Lattice)**; A.11 **Ontological Parsimony**.
**Coordinates with.** F.2 **Term Harvesting & Normalisation**; F.3 **Intra‑Context Sense Clustering**; F.4 **Role Description**; F.9 **Alignment & Bridge Across Contexts**; **G.0–G.1** *(Scope/describedEntity handoff)*.  *(Bridges live only in F.9.)*

**Aliases (informative).** *Contexts‑first survey*; *Context cut*.

### F.1:1 - Intent & applicability

**Intent.** Establish a **finite set of U.BoundedContext** (“**context of meaning**”), each tied to an authoritative source or canon within a **domain family**, so that all later moves (term harvesting, clustering, role naming, cross‑context bridges) operate on **local meanings** rather than on drifting, globalised words.

**Applicability.** Use **at the start** of any unification effort for **any FPF pattern** (Enactment (`U.RoleAssignment` + `U.RoleEnactment`), Sys-CAL, KD-CAL, Kind-CAL, LCA-CAL…) and **whenever** a discipline canon materially changes (new edition, re-framing, seminal result).

**Non‑goals.** No tooling, workflow, or editorial roles. No global ontology. No cross‑context equations. This pattern describes **how to think**, not how to store.

### F.1:2 - Problem frame

Without explicit context of meaning:

1. **Word‑drift.** Common words (*process*, *role*, *service*, *model*) silently change sense across disciplines.
2. **Scope mirages.** One influential standard is mistaken for *the* domain.
3. **Retro‑lock.** Old editions become the implicit truth simply because they were “there first”.
4. **Category bleed.** Behavioural roles, epistemic statuses, deontic permissions mix because their contexts were never fixed.
5. **Name inflation.** New U.Types appear just to “stabilise” unstable words.


### F.1:3 - Forces

| Force                        | Tension to resolve                                                                |
| ---------------------------- | --------------------------------------------------------------------------------- |
| **Universality vs locality** | We want cross‑domain unification, but **meaning is local** to a U.BoundedContext. |
| **Breadth vs parsimony**     | Wide coverage prevents bias; too many Contexts defeats understanding.                |
| **Recency vs continuity**    | New editions matter; but working knowledge often trails by years.                 |
| **Didactics vs fidelity**    | Pedagogically simple summaries must remain faithful to the source.                |


### F.1:4 - Core idea (didactic)

**Think in Contexts, not in words.**
A *Context of meaning* is a **U.BoundedContext** (per D.CTX) that encloses a coherent vocabulary and its rules from a **specific, citable canon** (standard, BoK, seminal paper, textbook tradition). You **name and reason** *inside the Context*. When you must step between Contexts, you will **declare a bridge later** (F.9) with explicit losses or mismatches.


### F.1:5 - Minimal vocabulary (this pattern only)

* **U.BoundedContext** (short: **Context** in Tech register). The formal *Context of meaning*.
* **Context** (Tech register alias for **U.BoundedContext**). Use **Context** for pedagogy, **U.BoundedContext** for formal references.
* **Domain family.** An **informative** shelf‑label grouping related Contexts (e.g., *workflow & provenance*; *services & deontics*; *sensing & measurement*; *types & taxonomies*; *control & actuation*). **No semantics** attach; Domain ≠ Context.
* **Context Card.** A **one‑screen** conceptual sketch of a Context (see §7.2).
* **SenseCell** *(appears downstream)*. A **(Context × Local‑Sense)** address; F.3 will mint these after clustering. Mentioned here only to keep the destination in view.


### F.1:6 - Solution — the Contexts‑first survey (conceptual, notation‑free)

**Step 1 — Declare your unification line(s).**
State which FPF pattern threads are in play (e.g., *Enactment + KD‑CAL sensing + Sys‑CAL execution*). This keeps the cut purposeful.

**Step 2 — Cut the landscape by domain families.**
For each line, **select at least three distinct domain families** (heterogeneity guard). Examples:

* *Workflow & provenance* (BPMN 2.0; W3C PROV‑O)
* *Services & deontics* (ITIL 4; ODRL 2.2)
* *Sensing & measurement* (SOSA/SSN; ISO 80000‑1)
* *Types & taxonomies* (OWL 2; FCA corpus)
* *Control & actuation* (state‑space control texts; IEC 61131‑3)

**Step 3 — For each family, sketch 1–3 Context Cards.**
Prefer canonical, widely cited canons. If a field is fragmented, choose one **exemplar** and one **counter‑voice** to surface heterogeneity.

**Step 4 — Make **locality** explicit.**
Treat words as **context‑local**. *Process (BPMN)* ≠ *process (thermodynamics)* ≠ *process (PROV)*. Do not reconcile. Do not average. **Just fix the Contexts.**

**Step 5 — Bound the set.**
Small enough to hold in working memory. As a rule of thumb:

* per unification line: **≥ 3 families**;
* per family: **1–3 Contexts**.
  More only if a missing Context hides a known sense‑split you will certainly need.

**Step 6 — Postpone bridges.**
If two Contexts seem “close”, **resist** collapsing. Note the tension and defer to **F.9 Alignment & Bridge**.

### F.1:7 - What to record (conceptual, not clerical)

**7.1 The two‑minute memory.**
Everything you need to *think correctly later* fits on an eight‑line card. No registries, no workflows, no storage choices.

**7.2 The Context Card (one‑screen sketch).**
*(Each bullet is a thought, not a field.)*

* **Name & edition.** *“BPMN 2.0 (2011)”* • *“W3C PROV‑O (2013)”* • *“ITIL 4 (2020)”*.
* **Domain family.** *workflow* / *provenance* / *services* / *deontics* / *sensing* / *types* / *control* … *(informative only; never used to infer meaning).*
* **Scope gist** *(didactic; ≠ `USM.ScopeSlice(G)`)*. One line that marks the **inside/outside** (“workflow **graphs & participants**”, “provenance **entities/activities/agents**”).
* **Time stance** *(if inherent)*. Does the canon speak **design** (specifications, models) or **run** (occurrences, acts)?
* **Lexical trip‑wires.** Known homonyms or false friends in this Context (*“process ≠ thermodynamic process”*, *“role (RBAC) ≠ behavioural role”*).
* **Neighbour Contexts** *(informative)*. Close cousins that people often conflate (*BPMN ↔ PROV‑O*, *ITIL ↔ ODRL*).
* **Recency note.** *Current* / *superseded* / *candidate* (only as a reminder to yourself which text you mean).
* **Why this Context matters here.** One sentence linking to your unification line (“we will name Executions later; PROV‑O keeps them run‑time”).
* **Diversity signature (dSig).** A 5‑characteristics discrete signature for `U.BoundedContext`: **[Sector, Function, Archetype, Regime, MetricFamily]**. Authors SHOULD pick from local discipline taxonomies. **Publish a `dSigSource` list (five refs/URIs, one per axis) on every Card**, falling back to free‑text only where no canonical term exists. Two Contexts are flagged as **Near‑Duplicate** when ≥3 characteristics match. Publish `dSig` and `dSigSource` on every Card.

> *If your Card spills beyond a screen, you are collecting facts, not fixing meaning.*

F1‑Card (normative artefact): { taxonomyRef, embeddingRef, DistanceDef, δ_family, confidenceBand, calibrationSet, edition, subFamilyDef? }. subFamilyDef (optional): declares the stable partitioning below a domain‑family (e.g., taxonomic sub‑fields or CVT clusters with parent family anchors).  When HET‑FIRST quotas refer to “sub‑family”, they MUST use this declared subFamilyDef.
Declare **DomainDistance** policy (cosine or transport) and δ_family threshold; version as part of DescriptorMapRef. Publish `confidenceBand` (e.g., CI90%) for the calibrated `δ_family`; treat numbers in examples as illustrative, not normative.

### F.1:8 - Invariants (normative, lightweight)

1. **Context ≡ U.BoundedContext.** In this pattern, *Context* always means **U.BoundedContext** (per E.10.D1).
2. **Locality.** Words are **local to their Context**; no global meaning is implied or imported.
3. **Heterogeneity.** Each unification line considers **≥ 3 distinct Domain families** (labels are informative only).
4. **Parsimony.** Prefer few, canonical Contexts per family (1–3) that jointly expose the key sense splits.
5. **No bridging here.** No equivalence or mapping is asserted between Contexts in F.1. (Bridges live in **F.9**.)
6. **Design/run honesty.** If a canon fixes a DesignRunTag, note it. Do not reinterpret.
7. **Didactic primacy.** Each Context Card must be readable by a thoughtful engineer in **under two minutes**.
8. **Domain‑family neutrality.** Domain families **carry no semantics**; they SHALL NOT be used for inheritance, inference, or bridge implication.
9. **Scope naming separation.** `Scope gist` on Cards is **didactic only**; formal *Scope/describedEntity* (=`USM.ScopeSlice(G)` ⊕ `describedEntity(GroundingHolon, ReferencePlane)`) is declared **in G.0–G.1**, not in F.1.
10. **Diversity signature present.** Each Context Card PUBLISHES a `dSig` in the 5‑characteristics form.
11. **Collision rule.** If any pair of Cards has `dSig` matching on ≥3 characteristics, mark **Near‑Duplicate** and either merge  into one slot or replace one by a Context from a different domain‑family. Record action in SCR.

### F.1:9 - Self‑checks (mental, not procedural)

* **The mirror test.** Can you explain *why each Context is inside* your cut **in one breath**? If not, you are surveying for comfort, not for meaning.
* **The homonym ping.** For each frequent word (*process*, *role*, *service*, *model*, *execution*), can you immediately list **the Contexts where it differs**? If not, add the missing Context.
* **The bridge itch.** Feel a strong urge to say “these are the same”? Good. **Write the itch down** and refuse to scratch it here. That’s F.9’s job.
* **The memory rule.** If your entire survey cannot be recalled **without opening a document**, it is too large.


### F.1:10 - Micro‑examples (illustrative only)

*One unification line: Enactment (`U.RoleAssignment` + `U.RoleEnactment`) with sensing and execution.*

* **BPMN 2.0 (2011)** — *workflow family*.
  *Scope gist:* flow nodes, sequence flows, participants (design‑time).
  *Trip‑wires:* “process” here is a **graph**; not a run.
* **W3C PROV‑O (2013)** — *provenance family*.
  *Scope gist:* **Activity** that uses/generates entities (run‑time).
  *Trip‑wires:* “activity/process” here is a **temporal occurrence**.
* **ITIL 4 (2020)** — *services family*.
  *Scope gist:* service as value co‑creation; SLO/SLA (deontic talk nearby).
  *Trip‑wires:* “incident/problem/practice” don’t equal workflow tasks.
* **ODRL 2.2** — *deontics family*.
  *Scope gist:* permissions, prohibitions, duties (design).
  *Trip‑wires:* “duty/obligation” ≠ service guarantee mechanics.
* **SOSA/SSN (2017)** — *sensing family*.
  *Scope gist:* Observation as an act yielding a Result for a property.
  *Trip‑wires:* “observation” ≠ “state”; it’s an **act** with a **procedure**.
* **IEC 61131‑3** — *control languages family*.
  *Scope gist:* tasks that **execute** programs (run‑time).
  *Trip‑wires:* “task/execution” ≠ “workflow process”.

> With only these Contexts fixed, later steps become almost mechanical: F.2 harvests terms **inside** each Context; F.3 clusters **within** each Context; F.4 names roles/statuses pointing to **SenseCells**; F.9 draws the bridges you refused to draw here.

### F.1:11 - Anti‑patterns & remedies

| #       | Anti‑pattern               | Symptom in practice                                                                  | Why it harms thinking                                          | Remedy (conceptual move)                                                                                                |
| ------- | -------------------------- | ------------------------------------------------------------------------------------ | -------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------- |
| **A1**  | **“One‑Book Domain”**      | Everything is justified from a single canon (“X is the domain”).                     | Projectionism; blinds heterogeneity; brittle to new editions.  | Enforce **heterogeneity**: pick **≥ 3 distinct domain families** per unification line (§6 Step 2, §8‑3).                |
| **A2**  | **Context‑less talking**   | Words like *process*, *role*, *service* used without naming a Context.                  | Global words drift; later steps must guess meaning.            | Always **prefix with the Context** in thought and prose: *process (BPMN)*, *activity (PROV)*, *service (ITIL)* (§4, §7.2). |
| **A3**  | **Edition blur**           | “BPMN” or “ITIL” cited with no year or profile.                                      | Inadvertent sense shifts; debates about “what the book says.”  | Cards keep **name + edition** on the first line; think with the exact edition (§7.2).                                   |
| **A4**  | **Phonebook survey**       | Dozens of Contexts; no one can recall the cut.                                          | Violates didactic primacy; people default to global talk.      | **Parsimony rule**: 1–3 Contexts per family, just enough to reveal key sense‑splits (§6 Step 5, §8‑4, §9 “memory rule”).   |
| **A5**  | **Bridge‑by‑stealth**      | Phrases like “these are basically the same” inside the survey.                       | Hides losses; imports meaning across Contexts without scrutiny.   | **No bridging here**; write the *itch to bridge* down and defer to **F.9** (§6 Step 6, §8‑5).                           |
| **A6**  | **Role/status conflation** | *Role (RBAC)* treated as behavioural mask; *duty (ODRL)* treated as service runtime. | Category bleed across families.                                | Cards carry **lexical trip‑wires** (“RBAC role ≠ behavioural role”; “duty ≠ runtime guarantee”) (§7.2).                 |
| **A7**  | **Temporal fudge**         | *Activity* or *execution* discussed without run/design stance.                       | Misplaced assertions; design artefacts treated as occurrences. | Cards note **time stance** when inherent (design vs run) (§7.2, §8‑6).                                                  |
| **A8**  | **Domain = Context**       | A “domain” label used as if it were a Context (e.g., “control” == one context).         | Shelf label mistaken for a canon; sense becomes fuzzy.         | **Domain family is informative only**; Contexts are **U.BoundedContext** tied to specific canons (§5, §7.2).               |
| **A9**  | **Context inheritance**    | Arranging Contexts in is‑a hierarchies (“PROV is‑a BPMN”).                              | Suggests meaning flows by inheritance; erases locality.        | **No is‑a among Contexts**; relations between Contexts live in **F.9 bridges** (§8‑5).                                        |
| **A10** | **Didactic bloat**         | Context Card spills into pages of notes.                                             | Teaching burden overwhelms the core idea.                      | **One‑screen Card**; everything else belongs to later patterns (§7.1–§7.2).                                             |
| **A11** | **Family‑based inference** | Treating Domain‑family membership as implying similarity/equivalence. | Smuggles semantics via shelf labels; breaks locality. | **Domain family is informative only**; locality and any Cross‑context relation must be explicit (F.9). |

### F.1:12 - Worked examples

> Each example shows **the cut** (the Contexts you keep in view) and the **thinking pay‑off** you get *before* any harvesting, clustering, or bridging.

#### F.1:12.1 Enactment (`U.RoleAssignment` + `U.RoleEnactment`) with sensing & execution (service acceptance)

**Unification line.** Enactment + KD‑CAL (sensing) + Sys‑CAL (execution).

**Contexts (six Cards).**

1. **BPMN 2.0 (2011)** — workflow family; **design**; *graph of flow nodes, participants*.
2. **PROV‑O (2013)** — provenance family; **run**; *Activity uses/generates Entities; Agents*.
3. **ITIL 4 (2020)** — services family; **design**; *service, SLO/SLA vocabulary*.
4. **ODRL 2.2** — deontics family; **design**; *permission / prohibition / duty*.
5. **SOSA/SSN (2017)** — sensing family; **run**; *Observation as act with Result*.
6. **IEC 61131‑3** — control languages; **run**; *tasks execute control programs*.

**Thinking pay‑off (examples).**

* You stop saying “*process uptime*” and think **Execution (IEC)** measured by **Observation (SOSA)** compared against **SLO (ITIL)**—three Contexts, three senses.
* You mark a trip‑wire: **RBAC role** (not in this cut) is *not* a **behavioural role (BPMN participant)**.
* You resist equating **PROV Activity** with **BPMN workflow**; later **F.9** may relate them with explicit loss.


#### F.1:12.2 Method quartet with types & measurement (model state graph)

**Unification line.** Method‑CAL + Kind-CAL + KD‑CAL.

**Contexts (five Cards).**

1. **SPEM 2.0 / ISO 24744** — methods family; **design**; *Method / MethodDescription language*.
2. **OWL 2 (profiles)** — types family; **design**; *class, subclass, equivalent class*.
3. **FCA corpus** — types family; **design**; *concept lattices*.
4. **SOSA/SSN (2017)** — sensing family; **run**; *Observation / Procedure*.
5. **ISO 80000‑1 (2022)** — metrology family; **design**; *quantity kinds, units*.

**Thinking pay‑off.**

* You keep **Method** (abstract how‑to) separate from **MethodDescription** (epistemic recipe) and **Execution** (run) because the Contexts already split design vs run.
* You avoid treating **FCA “concept”** as a **U.Type**; later F.9 can bridge OWL classes to FCA concepts with cautions.


#### F.1:12.3 Control & actuation with services (operational SLOs in plants)

**Unification line.** Sys‑CAL + LCA‑CAL (planned) + services/deontics.

**Contexts (five Cards).**

1. **State‑space control texts** — control family; **design**; *controller/plant, feedback*.
2. **IEC 61131‑3** — control languages; **run**; *task, program execution*.
3. **ISA‑95** — integration family; **design**; *levelled layers, interfaces*.
4. **ITIL 4 (2020)** — services family; **design**; *SLO/SLA*.
5. **SOSA/SSN (2017)** — sensing family; **run**; *Observation*.

**Thinking pay‑off.**

* “**Actuation**” is recognised as **control output** (Sys‑CAL), not a *service promise*.
* “**Incident**” (ITIL) is not a plant *fault* (Sys‑CAL); Contexts deter category errors.


### F.1:13 - Reasoning primitives (judgement schemas, notation‑free)

> These are **mental moves**, not queries. They read “given these thoughts, this conclusion is safe to hold (conceptually).”

1. **Context set for a line**
   `line L declared ⊢ Contexts(L) = {C₁,…,Cₙ}`
   *Reading:* For a unification line **L**, the Contexts you deliberately keep in view are `{C₁,…,Cₙ}` (from your Cards).

2. **Heterogeneity check**
   `families(L) = F ⊢ heterogeneous(L) ≡ (|distinct(F)| ≥ 3)`
   *Reading:* Your cut is heterogeneous if it spans at least three **domain families**.

3. **Parsimony check**
   `Contexts(L)=R, families(L)=F ⊢ parsimonious(L) ≡ (∀f∈F: 1≤|R∩f|≤3)`
   *Reading:* Each family contributes a few Contexts, not a phonebook.

4. **Locality assertion**
   `term w, C∈Contexts(L) ⊢ meaning(w)@C is local`
   *Reading:* A word’s sense is **context‑local**; no global meaning is implied.

5. **Time‑stance guard**
   `C has stance s∈{design,run} ⊢ claims@C must respect s`
   *Reading:* If a Context is design‑time, do not make run‑time claims in it (and vice versa).

6. **Trip‑wire recall**
   `C lists tripWires T ⊢ for any w∈T, require Context‑prefix when speaking`
   *Reading:* Words on the trip‑wire list must be spoken with the Context name.

7. **Bridge embargo**
   `C₁≠C₂ ⊢ no‑equivalence(C₁,C₂) within F.1`
   *Reading:* F.1 never asserts equivalence across Contexts; postponement is principled, not procrastination.

8. **Context sufficiency probe**
   `common‑word w used in L ∧ w not covered by any trip‑wire ⊢ consider adding a Context that makes w differ`
   *Reading:* If a frequent word has no deliberate sense‑split in your cut, you may be missing a Context.

9. **Memory rule**
   `|Contexts(L)| too large ⊢ reduce until a careful mind can recite them unaided`
   *Reading:* The survey should live in memory, not in a registry.

### F.1:14 - F1‑Card example (informative)
```
F1-Card v2025‑Q3:
  taxonomyRef: OpenAlex topics/fields (snapshot 2025‑08)
  embeddingRef: SPECTER2(2023) fine‑tuned@OA‑2025‑08
  DistanceDef: cosine on centroid embeddings (window 36 mo)
  δ_family: 0.35 (calibrated on control set; CI90% [0.33,0.37])
  calibrationSet: 120 labeled pairs (same vs different families)
  edition: 2025‑Q3
```
### F.1:15 - Relations (with other patterns)

**Builds on:**
E.10.D1 **Lexical Discipline for “Context” (D.CTX)** — ensures *Context* ≡ *U.BoundedContext* and reserves “Problem Frame” for narrative use.
A.7 **Strict Distinction** — guards object/description/carrier and design/run splits while you cut Contexts.
A.11 **Ontological Parsimony** — motivates the small cut.

**Constrains:**
**F.2** (Term Harvesting): harvest **inside** Contexts named here; every occurrence carries a Context name.
**F.3** (Intra‑Context Sense Clustering): cluster **per Context**; no Cross‑context sense claims.
**F.4** (Role Descriptions): any role/status template must cite a **SenseCell** that lives in a Context from this cut.
**F.9** (Alignment & Bridge): only F.9 may relate Contexts; never F.1–F.4.

**Used by.**
Extention patterns in Part C (Sys‑CAL, KD‑CAL, Kind-CAL, Method‑CAL, LCA‑CAL) as the *lexical starting grid* for their examples and definitions.


### F.1:16 - Migration notes (conceptual)

1. **New edition appears.** Keep the old Card; add a new Card with the new edition. If the sense shifts, treat it as a **new Context**; if it is strictly editorial, mark recency but keep one context.
2. **New family emerges.** If a missing family explains recurrent confusion in your line, admit it with **one exemplar** Context; remove a less informative Context to keep parsimony.
3. **Language variants.** Treat language editions as **separate Contexts** unless the canon itself declares a single normative bilingual mapping.
4. **Trip‑wire growth.** When you notice a recurring confusion, add a crisp trip‑wire to the relevant Card (one line; no essays).
5. **Bridges discovered later.** Do not back‑port bridges into F.1; leave the Cards untouched and record the mapping in **F.9**.
6. **Dormant Contexts.** If a Context no longer contributes to any active line, move it to a *parking shelf* (informative note on the Card) rather than deleting it.


### F.1:17 - Acceptance tests (SCR/RSCR — concept‑level)

#### F.1:17.1 - Static conformance checks (SCR)

* **SCR‑F1‑S01 (Heterogeneity).** For each unification line, the set of Cards spans **≥ 3 distinct domain families**.
* **SCR‑F1‑S02 (One‑screen Cards).** Each Card fits on one screen: name+edition; family; scope gist; time stance (if inherent); 1–3 trip‑wires; neighbour Contexts (optional); recency note.
* **SCR‑F1‑S03 (Locality pledge).** Nowhere in F.1 are Cross‑context equivalences or merges asserted.
* **SCR‑F1‑S04 (Parsimony).** In every family, **1–3** Contexts are kept; if more, a clear sentence justifies each extra Context’s unique sense contribution.
* **SCR‑F1‑S05 (Context discipline).** “Context” is used only as a synonym of **U.BoundedContext**; “domain” appears only as an informative family label.
* **SCR‑F1‑S06 (Temporal honesty).** If a canon fixes DesignRunTag, the Card states it.
* **SCR‑F1‑S07 (Family neutrality).** No claim, classification, or relation in F.1 relies on Domain‑family membership; families appear only as shelf labels on cards.
* **SCR‑F1‑S08 (dSig present).** Every Context Card has a 5‑characteristics `dSig`.
* **SCR‑F1‑S09 (Collision policy).** Any pair with `dSig` match on ≥3 characteristics is either merged or replaced; SCR records the action.

#### F.1:17.2 - Regression checks (RSCR)

* **RSCR‑F1‑E01 (Edition churn).** When a new edition is added, prior Cards remain; no silent replacement.
* **RSCR‑F1‑E02 (Family balance).** Adding/removing Cards does not drop any line below **three families**.
* **RSCR‑F1‑E03 (Trip‑wire coverage).** After introducing a new Context, the trip‑wire lists of neighbouring Contexts are reconsidered and updated if needed.
* **RSCR‑F1‑E04 (No creep).** Periodically apply the **memory rule**: if the cut no longer fits in working memory, shrink it.


### F.1:18 - Didactic distillation (90‑second teaching script)

> “Before you name anything, **fix the context of meaning**. A *Context* is a **U.BoundedContext** tied to a specific canon—*BPMN 2.0*, *PROV‑O*, *ITIL 4*, *SOSA/SSN*, *IEC 61131‑3*, *OWL 2*. Words are **local to Contexts**: *process (BPMN)* is a workflow graph, *activity (PROV)* is a run‑time occurrence, *service (ITIL)* is a promise vocabulary. Cut the landscape so each unification line sees **at least three domain families**, with **one‑screen Cards** per Context (scope gist, time stance, trip‑wires). **Do not bridge** Contexts here—just write down the itch to bridge and defer it. Keep the cut **small enough to remember**. With Contexts fixed, harvesting (F.2), local clustering (F.3), role/status templates (F.4), and explicit Cross‑context bridges (F.9) become straightforward—and you avoid naming ghosts that come from words floating without walls.”

### F.1:End

## F.2 — Term Harvesting & Normalisation

**“Harvest words *inside Contexts*, name them in the Context’s own idiom, and stop there.”**
**Status.** Architectural pattern.
**Depends on.** E.10.D1 **Lexical Discipline for “Context” (D.CTX)**; **F.0.1 Contextual Lexicon Principles** (Source - Local Meaning - Bridge‑Only Crossing); A.7 **Strict Distinction**; A.11 **Ontological Parsimony**.
**Coordinates with.** F.1 **Context Map via Context Cards**; F.3 **Intra‑Context Sense Clustering**; F.4 **Role Description**; F.9 **Alignment & Bridge Across Contexts**.
**Aliases (informative).** *context‑local harvesting*; *Local normalisation*.


### F.2:1 - Intent & applicability

**Intent.** Provide a **conceptual** (notation‑free) discipline for turning *Context‑internal usage* into **context‑local lexical units** ready for later reasoning—without Cross‑context merging and without slipping into governance or tooling. The result is a **small, auditable set of context‑local names and glosses** that faithfully reflect how the canon speaks.

**Applicability.** Use whenever a unification line (from F.1) needs **actual words** to be referenced by patterns in Part C (Extention patterns) or by Role Descriptions (F.4). Re‑enter F.2 when a canon/edition changes or when a new Context is admitted in F.1.

**Non‑goals.** No global labels; no Cross‑context equivalence; no workflow or role descriptions; no storage/API talk. F.2 specifies **how to think**, not how to “run a pipeline”.


### F.2:2 - Problem Frame

Even with Contexts fixed (F.1), three mistakes recur:

1. **Word‑centrism.** Treating a string as if it carried its meaning across Contexts (*process*, *role*, *service*).
2. **Over‑normalisation.** Forcing one spelling/morphology across different canons, erasing Context‑specific cues.
3. **Premature structure.** Smuggling behaviour, deontics, or type structures into what should remain **lexical**.

F.2 prevents these by **localising** meaning and **naming** strictly **inside** each Context.


### F.2:3 - Forces

| Force                      | Tension to resolve                                                               |
| -------------------------- | -------------------------------------------------------------------------------- |
| **Uniformity vs locality** | Desire for consistent names vs Context‑specific idioms that must be preserved.      |
| **Parsimony vs recall**    | Keep the harvested set small vs keep rare but pivotal terms that unlock bridges. |
| **Didactics vs fidelity**  | Two‑register labels (tech/plain) vs fidelity to the canon’s own phraseology.     |
| **Speed vs safety**        | Move fast to enable F.3/F.4 vs avoid any Cross‑context conclusion in F.2.           |


### F.2:4 - Core idea (didactic)

**Harvest *inside* each Context; name *in that Context’s idiom*; do not cross Contexts.**
For every Context (a **U.BoundedContext** from F.1), you gather **attested phrases** as *thought‑cues*, choose a **Local Normal Form (LNF)** that matches the Context’s idiom, attach a **two‑register label** (Tech/Plain), and write a **one‑sentence gloss**. That’s all. You do **not** claim sameness with any other Context; you do **not** embed behaviour or deontics; you do **not** mint U.Types here. These *local lexical units* will become **Local‑Senses** in F.3 and later addressable **SenseCells** (Context × Local‑Sense).


### F.2:5 - Minimal vocabulary (this pattern only)

* **Context** — Tech‑register alias for **U.BoundedContext** (per E.10.D1).
* **Attested phrase** — A short, verbatim cue from the canon that shows how a word is used **in this Context** (citation idea, not a record format).
* **Local Normal Form (LNF)** — The Context‑specific canonical surface you will use when referring to the term in this Context (minimal editing: spelling/hyphenation/casing per the canon).
* **Two‑register label** — **Tech** (engineer‑facing) and **Plain** (pedagogic) forms for the same Context‑local meaning.
* **Gloss (one‑sentence)** — A **Context‑faithful** description of how the canon uses the term, at **minimal generality**.
* **Local lexical unit** — The quintet *(Context, LNF, Tech, Plain, Gloss)*. This is F.2’s only outcome.
* **Homonymy (signal)** — Awareness that the **same string** has **different local lexical units** across Contexts (no relation asserted).
* **SenseCell** *(appears downstream)* — Address **(Context × Local‑Sense)** minted in F.3; mentioned here so you know what you’re preparing.

> *Everything above is a way of thinking. None of it implies a database, statuses, or roles.*


### F.2:6 - Solution — three mental moves (notation‑free)

#### F.2:6.1 - Move A — **Localise the word**

**Question to ask.** *“In which Context am I hearing this word?”*
**Action (mental).** Point to a specific **Context** (from F.1). Grab 1–2 **attested phrases** that are representative **in this Context**.
**Outcome.** You stop thinking “global word” and start thinking “context‑local usage”.

*Micro‑cue.* If you cannot name the Context, do not harvest the word.


#### F.2:6.2 -Move B — **Name it in the Context’s idiom**

**Question to ask.** *“How would this Context itself write it?”*
**Action (mental).** Choose the **LNF** (Context‑conformant spelling/hyphenation). Then write the **two‑register label** and a **one‑sentence gloss** that says **what the canon means here**—nothing more.
**Outcome.** You have a **local lexical unit** *(Context, LNF, Tech, Plain, Gloss)*.

*Micro‑cues.*
• Prefer the canon’s head noun; keep canonical hyphens; avoid invented compounds.
• The **Plain** label should help a non‑specialist; the **Tech** label should match engineers’ eyes.
• The **Gloss** must fit on a single line; defer details to F.3.


#### F.2:6.2 - Move C — **Fence it off**

**Question to ask.** *“What must I refuse to conclude here?”*
**Action (mental).** Explicitly **refuse** to: (1) compare across Contexts, (2) fold morphology that the canon treats as meaningful, (3) embed behaviour, deontics, or type structure.
**Outcome.** A clean, **context‑local** lexical unit that will be safe to cluster in F.3 and safe to bridge (or not) in F.9.


### F.2:7 - Guard‑rails (normative, lightweight)

1. **context‑locality.** Every local lexical unit **MUST** cite a Context (U.BoundedContext from F.1).
2. **Context‑idiom normalisation.** LNF **MUST** respect the Context’s idiom (spelling/hyphenation/casing) and use **minimal edits**.
3. **Two registers.** Each unit **SHOULD** carry both **Tech** and **Plain** labels for didactics; if one is missing, justify.
4. **Minimal generality (G‑1).** The gloss **MUST** be as specific as the Context’s canon requires—no broader.
5. **I/D/S layer hygiene (A.7).** **MUST NOT** include behaviour equations, deontic rules, measurement math, or type axioms; those belong to patterns.
6. **No Cross‑context claims.** **MUST NOT** assert equivalence, subsumption, or similarity with terms in other Contexts (F.9 only).
7. **Edition honesty.** If the Context’s canon has multiple editions with shifting usage, treat them as distinct Contexts in F.1 before harvesting.
8. **Parsimony.** Prefer **few, telling** lexical units over long tails; keep head terms that will power F.3/F.4/F.9.


### F.2:8 - Micro‑examples (illustrative, context‑local)

> Each line is *one* local lexical unit. No relations are implied across lines.

* **Context:** *BPMN 2.0 (2011)* — **LNF:** `process`
  **Tech:** `process` - **Plain:** `workflow process`
  **Gloss:** “Directed graph of flow nodes and sequence flows enacted by participants.”

* **Context:** *PROV‑O (2013)* — **LNF:** `activity`
  **Tech:** `activity` - **Plain:** `temporal occurrence`
  **Gloss:** “Time‑bounded occurrence that uses and generates entities and is linked to agents.”

* **Context:** *ITIL 4 (2020)* — **LNF:** `service‑level‑objective`
  **Tech:** `service‑level‑objective` - **Plain:** `service target`
  **Gloss:** “Target value for a service characteristic within a service promise vocabulary.”

* **Context:** *NIST RBAC (2004)* — **LNF:** `role`
  **Tech:** `access‑role` - **Plain:** `permission role`
  **Gloss:** “Named grouping of permissions assignable via sessions.”

* **Context:** *SOSA/SSN (2017)* — **LNF:** `observation`
  **Tech:** `observation` - **Plain:** `measurement act`
  **Gloss:** “Act applying a procedure to a feature of interest to produce a result.”

* **Context:** *IEC 61131‑3* — **LNF:** `task`
  **Tech:** `task` - **Plain:** `runtime program execution`
  **Gloss:** “Cyclic or event‑driven execution unit for control programs.”


### F.2:9 - Didactic heuristics (informative)

* **Keep the Context prefix in your inner speech.** Say “*process (BPMN)*”, “*activity (PROV)*”.
* **Prefer head nouns.** If the canon says “service‑level objective”, do not shorten it to “objective”.
* **Resist elegance that erases signal.** Hyphens and case often carry the Context’s culture; keep them.
* **Gloss from use, not from opinion.** Quote in your mind, then compress; avoid importing definitions from neighbouring Contexts.

### F.2:10 - Anti‑patterns & remedies

| #       | Anti‑pattern                 | Symptom (in thought or prose)                                        | Why harmful                                                  | Remedy (conceptual move)                                                                                |
| ------- | ---------------------------- | -------------------------------------------------------------------- | ------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------- |
| **A1**  | **Global normal form**       | One “canonical” label reused across Contexts.                           | Erases local meaning; invites stealth bridges.               | Keep **LNF per Context**; any Cross‑context relation belongs to **F.9** only.                                 |
| **A2**  | **String = meaning**         | Assuming identical strings denote one concept across Contexts.          | Homonym collision (*process*, *role*, *service*).            | Always prefix mentally with the **Context**; treat same string in different Contexts as **different units**.  |
| **A3**  | **Over‑normalisation**       | Folding hyphens/case/morphology “for consistency”.                   | Loses the canon’s idiom; breaks citations.                   | **Minimal edits** toward the Context’s idiom; never toward a global house‑style.                           |
| **A4**  | **Headless multiword**       | Truncating to a head (“objective” for “service‑level objective”).    | Ambiguity; collapses scope.                                  | Preserve canonical **head‑modifier** as LNF when meaningful.                                            |
| **A5**  | **Premature structure**      | Embedding behaviour, deontics, units, or type axioms into the gloss. | I/D/S layer mixing (violates A.7); biases later patterns.          | Gloss **usage**, not calculus; structural content belongs to Extention Patterns in Part C.                   |
| **A6**  | **Cross‑context folding**       | “BPMN workflow ≈ PROV activity” written inside F.2.                   | Hidden bridge; unpriced losses.                              | No Cross‑context claims in F.2; write the **itch to bridge** for **F.9**.                                  |
| **A7**  | **Edition blur**             | “BPMN” without year/profile; mixing excerpts across editions.        | Silent sense shift; unrepeatable reasoning.                  | Treat distinct editions as **distinct Contexts** in F.1, then harvest.                                     |
| **A8**  | **Vendor‑dialect elevation** | Treating a DSL/keyword list as “the domain”.                         | Projectionism; narrow idiom dominates.                       | If needed, model the DSL as **one context among others**; keep heterogeneity from F.1.                     |
| **A9**  | **Tail chasing**             | Harvesting hundreds of rare terms.                                   | Cognitive overload; dilutes signal.                          | Keep **head terms** that feed F.3/F.4/F.9; justify rare units by their bridging value.                  |
| **A10** | **Fake symmetry**            | Tech and Plain labels are identical jargon.                          | Didactic failure.                                            | Make **Plain** genuinely explanatory; keep **Tech** faithful to the canon.                              |
| **A11** | **Temporal fudge**           | Using run‑time words in design Contexts (or vice versa).                | Category drift; later contradictions.                        | Respect the Context’s **DesignRunTag** from its Card (F.1 §7.2).                                      |
| **A12** | **Cross‑language collapse**  | Merging bilingual terms as one unit.                                 | Erases idiom‑specific signals; hides normative mapping gaps. | Treat each language edition as its **own Context** unless the canon declares a normative mapping.          |
| **A13** | **Alias inflation**          | Inventing new local names “for clarity”.                             | Strays from the canon; hinders bridging.                     | Prefer the canon’s idiom; keep invented phrasings to the **Plain** register only.                       |
| **A14** | **Role/status conflation**   | RBAC “role” glossed as behavioural role.                             | Cross‑family bleed; wrong assignment later.                         | Call out the Context in the label: **access‑role (RBAC)** vs **participant (BPMN)**; keep senses disjoint. |


### F.2:11 - Worked examples (context‑local only)

> Each line is a **local lexical unit** *(Context, LNF, Tech, Plain, Gloss)*.
> No Cross‑context relation is implied. Later clustering (F.3) and bridges (F.9) may connect them.

#### F.2:11.1 Enactment + sensing

* **Context:** *BPMN 2.0 (2011)* — **LNF:** `process`
  **Tech:** `process` - **Plain:** `workflow process`
  **Gloss:** “Directed graph of flow nodes and sequence flows enacted by participants.”

* **Context:** *PROV‑O (2013)* — **LNF:** `activity`
  **Tech:** `activity` - **Plain:** `temporal occurrence`
  **Gloss:** “Time‑bounded occurrence that uses and generates entities and links to agents.”

* **Context:** *SOSA/SSN (2017)* — **LNF:** `observation`
  **Tech:** `observation` - **Plain:** `measurement act`
  **Gloss:** “Act applying a procedure to a feature of interest to produce a result.”

* **Context:** *ITIL 4 (2020)* — **LNF:** `service‑level‑objective`
  **Tech:** `service‑level‑objective` - **Plain:** `service target`
  **Gloss:** “Target value for a service characteristic within a service promise vocabulary.”

*Thinking pay‑off:* you can phrase “compare **observation** to **service‑level‑objective**” without importing workflow or provenance semantics.


#### F.2:11.2 Sys‑CAL / LCA‑CAL + services

* **Context:** *State‑space control texts* — **LNF:** `actuation`
  **Tech:** `actuation` - **Plain:** `control output`
  **Gloss:** “Signal applied to the plant to influence state/output.”

* **Context:** *IEC 61131‑3* — **LNF:** `task`
  **Tech:** `task` - **Plain:** `runtime program execution`
  **Gloss:** “Cyclic or event‑driven execution unit for control programs.”

* **Context:** *ITIL 4 (2020)* — **LNF:** `incident`
  **Tech:** `incident` - **Plain:** `reported disruption`
  **Gloss:** “Unplanned interruption or reduction in the quality of a service.”

*Thinking pay‑off:* avoids calling a plant fault an “incident” unless you **cross Contexts later** with an explicit bridge.


#### F.2:11.3 Kind-CAL + Method‑CAL + KD‑CAL

* **Context:** *OWL 2 (profiles)* — **LNF:** `subclass‑of`
  **Tech:** `subclass‑of` - **Plain:** `is‑a (type hierarchy)`
  **Gloss:** “C ⊑ D: every instance of C is an instance of D.”

* **Context:** *FCA corpus* — **LNF:** `formal‑concept`
  **Tech:** `formal‑concept` - **Plain:** `extent–intent node`
  **Gloss:** “Maximal (objects, attributes) pair under a Galois connection.”

* **Context:** *SPEM 2.0 / ISO 24744* — **LNF:** `method`
  **Tech:** `method` - **Plain:** `abstract way of doing`
  **Gloss:** “Abstract how‑to independent of specification or execution.”

* **Context:** *SOSA/SSN (2017)* — **LNF:** `procedure`
  **Tech:** `procedure` - **Plain:** `measurement recipe`
  **Gloss:** “Specification guiding how an observation is produced.”

*Thinking pay‑off:* discourages treating an FCA “concept” as a `U.Type`, or a **procedure** as a **method** without later proof.


### F.2:12 - Reasoning primitives (judgement schemas, notation‑free)

> Read each as a **permitted mental move** over the outcomes of F.2.
> Symbols: `R` = Context (U.BoundedContext), `u` = local lexical unit, `s` = surface string.

1. **Localisation**
   `heard(s) ∧ R chosen ⊢ localize(s,R)`
   *You decide to hear `s` only **in** Context `R`.*

2. **Context‑idiom normalisation**
   `localize(s,R) ⊢ LNF_R(s) = ℓ`
   *Within `R`, the **Local Normal Form** for `s` is `ℓ`.*

3. **Unit formation**
   `LNF_R(s)=ℓ ∧ labelTech=t ∧ labelPlain=p ∧ gloss=g ⊢ unit(u) = ⟨R,ℓ,t,p,g⟩`
   *A **local lexical unit** is formed (quintet).*

4. **Lexical‑only guard**
   `unit(u) ⊢ lexicalOnly(u)`
   *No behavioural/deontic/type math is attached to the gloss.*

5. **Homonymy signal (Cross‑context)**
   `LNF_Ra(s)=ℓa ∧ LNF_Rb(s)=ℓb ∧ Ra≠Rb ⊢ homonymy(s) ⊇ {Ra,Rb}`
   *Same string across Contexts is flagged as **different** by default.*

6. **Minimal generality check**
   `unit(u) ⊢ minimal(u) ⇔ gloss(u) says no more than the Context’s usage requires`
   *The gloss fits the Context; broader claims are withheld.*

7. **Two‑register adequacy**
   `unit(u) ⊢ didactic(u) ⇔ (tech(u) faithful) ∧ (plain(u) explanatory)`
   *Tech stays canonical; Plain helps non‑specialists.*

8. **No Cross‑context conclusion**
   `unit(u@Ra), unit(v@Rb), Ra≠Rb ⊢ ¬(u ≡ v) (within F.2)`
   *F.2 never asserts Cross‑context equivalence.*

9. **Ready‑for‑F.3 signal**
   `lexicalOnly(u) ∧ minimal(u) ∧ didactic(u) ⊢ readyF3(u)`
   *A unit is suitable input for **intra‑Context clustering** in F.3.*


### F.2:13 - Relations

**Builds on:**
**F.1** (Contexts fixed; heterogeneity/parsimony in place).
**E.10.D1 D.CTX** (Context ≡ U.BoundedContext; “Problem Frame” reserved for narrative).
**F.0.1** (Source - Local Meaning - Bridge‑Only Crossing).

**Constrains:**
**F.3** (Intra‑Context Sense Clustering): operates **only** on units **from one Context**; produces Local‑Senses and addressable **SenseCells**.
**F.4** (Role Description Definition): may **cite SenseCells**, not raw strings.
**F.9** (Alignment & Bridge): consumes **homonymy signals**; declares explicit Cross‑context mappings with loss policies.

**Used by.**
Extention patterns in Part C when referencing domain idioms (labels stay **context‑local**).


### F.2:14 - Migration notes (conceptual)

1. **New edition appears.** Add a Context in F.1; harvest afresh in F.2 using that Context; do not overwrite earlier units.
2. **Idiomatic update discovered.** If your LNF fought the canon’s idiom, **re‑LNF** within the same context; keep labels/glosses steady unless the canon itself differs.
3. **Ambiguity inside a Context.** If use splits, **mint two units** with distinct glosses; F.3 will sort their relation (same/different Local‑Sense).
4. **Language split.** Treat each language canon as its **own Context**; resist cross‑language merges in F.2.
5. **Tail pruning.** If units accumulate without feeding F.3/F.4/F.9, drop them from the working set; keep head terms that carry bridges.
6. **DSL quarantine.** If a tool dialect is unavoidable, keep it as one context among others; never let it define the idiom for other Contexts.


### F.2:15 - Acceptance tests (SCR/RSCR — concept‑level)

#### F.2:15.1 - Static conformance (SCR)

* **SCR‑F2‑S01 (context‑locality).** Every unit cites a Context from F.1.
* **SCR‑F2‑S02 (Idiomatic LNF).** Each LNF reflects the Context’s spelling/hyphenation/casing with **minimal edits**.
* **SCR‑F2‑S03 (Two registers).** Each unit carries both **Tech** and **Plain** labels; if not, a reason exists tied to didactics.
* **SCR‑F2‑S04 (Lexical‑only).** No gloss contains behaviour, deontics, measurement math, or type axioms.
* **SCR‑F2‑S05 (No Cross‑context claims).** Nowhere does F.2 assert equivalence/similarity/subsumption across Contexts.
* **SCR‑F2‑S06 (Minimal generality).** Glosses match the Context’s use; no globalisation.
* **SCR‑F2‑S07 (Temporal honesty).** For Contexts with fixed DesignRunTag, units and glosses respect it.

#### F.2:15.2 - Regression (RSCR)

* **RSCR‑F2‑E01 (Edition split).** Introducing a new edition yields new units under a new Context; earlier units persist unchanged.
* **RSCR‑F2‑E02 (Normaliser stability).** Adjusting an LNF does not silently widen/narrow the gloss.
* **RSCR‑F2‑E03 (Language split).** Adding a second language yields a second Context; no bilingual collapse in F.2.
* **RSCR‑F2‑E04 (No stealth bridges).** After updates, F.2 still contains **zero** Cross‑context identity claims; any mapping appears only in F.9.
* **RSCR‑F2‑E05 (Head‑term focus).** Periodic check shows the unit set remains small and oriented to F.3/F.4/F.9 needs.


### F.2:16 - Didactic distillation (60‑second script)

> “In F.2 you **harvest inside Contexts**. For each Context, pick the canon’s own phrasing, choose a **Local Normal Form** in that idiom, add **Tech** and **Plain** labels, and write a one‑sentence **Gloss** that matches how that Context talks. Stop there. No bridging, no behaviour, no equations. If the same string appears in another Context, treat it as a **different unit**. These units feed F.3, where you’ll sort senses **within** a Context, and F.9, where you’ll relate Contexts explicitly. This keeps meaning local, names faithful, and later reasoning clean.”

### F.2:End

## F.3 - Intra‑Context Sense Clustering

**“Within one context, decide what ‘the same sense’ really is—before you ever cross Contexts.”**
**Status.** Architectural pattern.
**Depends on.** F.1 **Domain‑Family Landscape Survey**; F.2 **Term Harvesting & Normalisation**; E.10.D1 **Lexical Discipline for “Context” (D.CTX)**; A.7 **Strict Distinction**; A.11 **Ontological Parsimony**.
**Coordinates with.** F.4 **Role Description**; F.7 **Concept‑Set Table**; F.8 **Mint or Reuse Decision**; F.9 **Alignment & Bridge Across Contexts**.
**Aliases (informative).** *context‑local clustering*; *Sense consolidation*.


### F.3:1 - Intent & applicability

**Intent.** Consolidate the **context‑local lexical units** from F.2 into a **small set of Local‑Senses** that actually operate in that **one context (U.BoundedContext)**. Each Local‑Sense receives a crisp, didactic label pair (Tech/Plain) and a short sense statement. The result is an **addressable basis** for later uses (Role Assignment, tables, bridges) that is **still strictly context‑local**.

**Applicability.** Apply **after** F.2 for any Context that will feed naming (F.4/F.5), decision gates (F.8), Cross‑context bridges (F.9), or exemplars in Part C. Use again whenever the canon (edition) **shifts usage** enough to split or merge senses **within the same context**.

**Non‑goals.** No Cross‑context comparison or merging. No behaviour/deontics/type mathematics. No storage schemas or workflows. This is **pure sense‑making** inside one context.


### F.3:2 - Problem Frame

context‑local units (LNF + labels + gloss) from F.2 often **over‑ or under‑differentiate** meaning:

1. **Over‑split:** superficial variants (*service‑level‑objective* vs *SLO*) treated as different “things”.
2. **Under‑split:** one gloss covering **two selectional frames** or incompatible use‑cases.
3. **Drift within a canon:** multi‑chapter texts use the same head differently unless the reader **consolidates** the intended sense.
4. **Didactic mismatch:** engineer‑friendly label and plain label drift apart when units remain too granular.

F.3 repairs this **inside the Context** by clustering “same sense” and distinguishing “different sense”, with **parsimony**.


### F.3:3 - Forces

| Force                     | Tension to resolve                                                                                               |
| ------------------------- | ---------------------------------------------------------------------------------------------------------------- |
| **Parsimony vs fidelity** | Few Local‑Senses ease teaching; too few dilute real distinctions the canon relies on.                            |
| **Usage vs definition**   | Glosses should reflect **how the canon uses the word**, not an imported dictionary definition.                   |
| **Labels vs idiom**       | Tech label must stay in the canon’s idiom; Plain label must help newcomers—without inventing a new sense.        |
| **Stability vs openness** | Consolidated senses must be stable enough for Role Descriptions and tables, yet revisable when the canon’s use clearly splits. |

### F.3:4 - Core idea (didactic)

**Cluster by usage, not by string.**
Inside one context:

* **Same sense** → **Local‑Sense**: a small, coherent usage‑region the canon treats as one idea (even if it has aliases or minor surface variation).
* **Different sense** → **two Local‑Senses**: incompatible selectional frames, entailments, or role in the canon’s own statements.

Each Local‑Sense becomes **addressable** when paired with its Context: **SenseCell = (Context × Local‑Sense)**. SenseCells are **context‑local coordinates**; they do not pre‑judge any Cross‑context mapping.


### F.3:5 - Minimal vocabulary (this pattern only)

* **Context** — short for `U.BoundedContext` (per D.CTX).
* **Unit** — a context‑local lexical unit from F.2 (LNF + Tech/Plain + gloss).
* **Local‑Sense** — the **conceptual cluster** of Units deemed “same sense” **within that Context**.
* **SenseCell** — the **address** for a Local‑Sense: *(Context, Local‑Sense)*. This is what later patterns will **cite**.
* **Counter‑example** — a short, canonical sentence or use that **must not** be covered by the Local‑Sense; it sharpens the boundary.
* **Usage cue** *(informative)* — a clue from usage (collocational patterns, paraphrases, entailments in the canon) that **suggests** merge or split. Cues **do not decide**; the canon’s intent does.


### F.3:6 - Solution — how to think the clustering (notation‑free)

> What follows are **mental moves**, not steps for a team. Use them as probes until the Context’s usage partitions itself naturally.

**6.1 Consolidate aliases into one Local‑Sense.**
If Units differ only by **orthography, abbreviation, or canon‑blessed synonymy** and are **used interchangeably** in the Context’s own sentences, treat them as **one Local‑Sense**.
*Example (ITIL):* *service‑level‑objective* and *SLO* → one Local‑Sense.

**6.2 Split on incompatible selectional frames.**
If the same head pairs with **different kinds of arguments** or plays **different roles** in the canon’s statements (and those roles cannot both be true at once), split.
*Example (BPMN):* *event* as **node type** vs as **occurrence narrative** in a tutorial → two Local‑Senses; adopt the **node type** sense if that is the normative layer.

**6.3 Split on entailments that pull apart.**
If paraphrases lead to **different entailments** (e.g., one implies temporality, another structural position), you have two senses.
*Example (PROV):* *activity* implies **time‑bounded use/generate**; it cannot be the same sense as a **static capability**.

**6.4 Prefer sense minimality.**
If two candidate Local‑Senses never lead to **different conclusions** in the Context’s own use, merge them. If they sometimes do, split them—and record a **counter‑example** to keep the boundary crisp.

**6.5 Keep Tech label idiomatic; Plain label helpful.**
Tech label stays as the canon speaks; Plain label conveys the **function** of the sense to a careful newcomer. Neither label may **broaden** the sense beyond usage.

