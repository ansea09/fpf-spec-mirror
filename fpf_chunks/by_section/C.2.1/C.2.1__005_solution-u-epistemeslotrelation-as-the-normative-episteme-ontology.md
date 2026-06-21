---
chunk_kind: "child"
pattern_id: "C.2.1"
pattern_title: "U.Episteme - Epistemes and their slot relation"
section_id: "C.2.1:4"
section_title: "Solution - U.EpistemeSlotRelation as the normative episteme ontology"
source_path: "FPF-Spec.md"
output_path: "by_section/C.2.1/C.2.1__005_solution-u-epistemeslotrelation-as-the-normative-episteme-ontology.md"
commit_sha: "fe0df9dcb06cfc87c8a6cb2f7cce3ac0d3b64d5e"
heading_path:
  - "C.2.1 — U.Episteme - Epistemes and their slot relation"
  - "C.2.1:4 — Solution - U.EpistemeSlotRelation as the normative episteme ontology"
line_start: 36139
line_end: 36523
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

### C.2.1:4 - Solution - `U.EpistemeSlotRelation` as the normative episteme ontology

#### C.2.1:4.0 - Overview

For `U.Episteme`, `U.EpistemeSlotRelation` is the normative **small, typed n-ary relation with SlotSpecs** over the core episteme positions. It is not a graph object and not a tuple object. Under `C.29`, the same slot relation may be viewed as a tuple for filled-value reasoning or as a graph or hypergraph diagram for dependency reasoning, but those are mathematical-lens views. Graph-valued fillers such as `U.ClaimGraph` remain real graph-kinds inside the relation.

**Positions and slots.**
  Minimal **kernel SlotKinds** (with their ValueKinds) that every episteme can refer to, following A.6.5:
  * `EntityOfConcernSlot`  (ValueKind `U.Entity` or a declared subkind) -> *"what this episteme is about"*;
  * `GroundingHolonSlot`   (ValueKind `U.Holon`) -> *"where this is grounded and in what holon"*;
  * `ClaimGraphSlot`       (ValueKind `U.ClaimGraph`) -> *"what is being said (claim content)"*;
  * `ReferenceSchemeSlot`  (ValueKind `U.ReferenceScheme`) -> *"how we read claims as statements about entities"*;
  * `ViewpointSlot`        (ValueKind `U.Viewpoint`) -> *"under which viewpoint we read or validate this episteme"*;
  * `ViewSlot`             (ValueKind `U.View`) -> *"a view-episteme produced under a viewpoint"*.

* **Slots and signatures.**
  These positions are realised as **SlotKinds** with associated **ValueKinds** and **RefKinds** under `U.RelationSlotDiscipline` (A.6.5). An **episteme kind** (`U.EpistemeKind`) is a **signature** over these slots.

* **Episteme as n-ary relation and as holon.**
  Each concrete episteme instance can be seen both as:

  * a **filled value assignment** over this slot relation; when C.29 tuple reasoning is current, the assignment may be viewed as a tuple view without becoming a second episteme kind, and
  * a **holon with components** (`U.EpistemeCard`, `U.EpistemeView`, `U.EpistemePublication`) whose fields correspond to those slots.

`U.Episteme` is thus the holon type whose components are *disciplined* by the `U.EpistemeSlotRelation`; C.2.1 fixes that discipline.

* **Morphisms.**
  Simple **epistemic morphisms** (EntityOfConcern-reference mapping, grounding, encoding, evaluation) are expressed as ordinary relations or functions between these positions and their graph-valued or non-graph-valued fillers. A.6.2-A.6.4 then specify general laws for effect-free morphisms over `U.Episteme`.

* **Symbol-Concept-Object triangle as didactic projection.**
  The classic Symbol-Concept-Object triangle becomes a **didactic view** of this slot relation, not the normative ontology; it is simply the projection to:

  * `Symbol` ~= a subset of `U.RepresentationScheme`/`U.RepresentationToken`,
  * `Concept` ~= `U.ClaimGraph`,
  * `Object` ~= `{EntityOfConcern, ReferenceScheme}`.

The rest of this pattern fixes the **minimal core** needed by KD-CAL, A.6.2-A.6.4 and E.17.*. The representational nodes (`U.RepresentationScheme`, `U.RepresentationToken`, `U.PresentationCarrier`, `U.RepresentationOperation`) are introduced as an **extension C.2.1+**, preserving the slot-relation boundary and profile defined here.

#### C.2.1:4.1 - Minimal epistemic positions (nodes & slots)

This section defines the **minimal position set** for `U.EpistemeSlotRelation` and the associated **SlotKinds**. These are the positions that A.6.2-A.6.4 and E.17.* can rely on.

##### C.2.1:4.1.1 - `EntityOfConcernSlot` — “what this episteme is about”

**Tech:** `EntityOfConcernSlot` (SlotKind), `entityOfConcernRef : U.EntityRef` (Ref slot in tuples or cards).
**Plain:** *EntityOfConcern value*, *entity of concern*. The plain phrase helps readers name the slot value; it is not a current Tech head.

**Intent.** Provide a **single, explicit slot** for the entity (or entities) that an episteme is about, preventing conflation of Object, Reference, and Context.

**Normative definition.**

1. `EntityOfConcernSlot` is a **SlotKind** in the sense of A.6.5 `U.RelationSlotDiscipline`.

   * Its **ValueKind** is `U.Entity`.
   * Its **RefKind** is `U.EntityRef` (or a species thereof) and **MUST** be realised in data as a field named `entityOfConcernRef : U.EntityRef` (E.10 discipline).
1. Species of `U.EpistemeKind` **MAY** constrain the ValueKind to a subtype `EntityOfConcernClass ⊑ U.Entity` (for example, “the entity of concern is always a `U.Holon` and, more specifically, a `U.System` or `U.Episteme`”). The subtype **MUST NOT** be named `U.EntityOfConcern`; “EntityOfConcern value” is a local slot-use phrase, not a durable U-kind.
2. When source wording or a draft uses `U.EpistemicObject` as a separate kind, repair it as **"`U.Entity` filling `EntityOfConcernSlot`"** and keep the source wording only as source wording governed by E.10 and F.18.

**Didactic cue.**
“Ask: *What, exactly, is this description about?* That is the EntityOfConcern.”

##### C.2.1:4.1.2 - `GroundingHolonSlot` - where this is grounded and in what holon

**Tech:** `GroundingHolonSlot` (SlotKind), `groundingHolonRef : U.HolonRef?`.
**Plain:** *grounding holon*, *holon‑of‑grounding*, *engagement context*.

**Intent.** Capture the **material–social holon** (system, lab, infrastructure, organisation, runtime environment) with respect to which an episteme’s claims are **tested, calibrated or validated**.

**Normative definition.**

1. `GroundingHolonSlot` is a **SlotKind** with:

   * **ValueKind** `U.Holon`,
   * **RefKind** `U.HolonRef` (or a species thereof),
   * and recommended field name `groundingHolonRef? : U.HolonRef` in episteme cards or views.
2. `GroundingHolonSlot` is **optional** at the minimal core: an episteme may be **un‑grounded** at M‑mode (e.g., purely mathematical), but any episteme used for **empirical evaluation or assurance** under KD‑CAL **SHALL** either:

   * populate `groundingHolonRef`, or
   * declare explicitly that no such grounding is possible (e.g., counterfactuals, abstract logics), with consequences reflected in KD‑CAL `R`.
3. The phrase *“grounding holon”* is **plain‑register**; there is no durable U-kind `U.GroundingHolon`. It always means “the holon currently filling `GroundingHolonSlot` for this episteme.”

**Didactic cue.**
"Ask: *In which lab, organisation, or world-slice do we test or observe this?* That is the GroundingHolon."

##### C.2.1:4.1.3 - `U.ClaimGraph` and `ClaimGraphSlot` — claim content

**Tech:** `U.ClaimGraph` (ValueKind), `ClaimGraphSlot` (SlotKind).
**Plain:** *claim graph*, *claim content*.

**Intent.** Reuse the existing KD‑CAL notion of **ClaimGraph** as the episteme’s **claim body**, but make its slot value use explicit.

**Normative definition.**

1. `U.ClaimGraph` is the **ValueKind** for `ClaimGraphSlot`:

   * nodes: typed claims (definitions, axioms, theorems, requirements, properties, assumptions);
   * edges: logical, derivational, or refinement relations, as already defined in C.2.
2. `ClaimGraphSlot` is a **SlotKind** whose instances are always **stored by value** in core patterns:

   * `content : U.ClaimGraph` is the normative field in `U.EpistemeCard` / `U.EpistemeView`;
   * C.2.1 **MUST NOT** introduce `U.ClaimGraphRef` as a ValueKind. Any reference type for ClaimGraphs, if needed, is a **RefKind** defined by discipline packs on top of `U.ClaimGraph`.
3. `ClaimGraphSlot` is **mandatory**: every `U.EpistemeKind` that uses C.2.1 **SHALL** have exactly one `ClaimGraphSlot`.

**Didactic cue.**
“Ask: *What is actually being claimed, defined, required, proved?* That is the ClaimGraph.”

##### C.2.1:4.1.4 - `U.Viewpoint` and `ViewpointSlot` — perspective of concerns and validators

**Tech:** `U.Viewpoint` (ValueKind), `ViewpointSlot` (SlotKind), `viewpointRef : U.ViewpointRef?`.
**Plain:** *viewpoint*, *perspective*, *stakeholder perspective*.

**Intent.** Provide a **first-class reusable catalogue** for ISO-style viewpoints and their generalisations, as used by E.17.0 `U.MultiViewDescribing`, MVPK, and TEVB.

**Normative definition.**

1. `U.Viewpoint` is the type of **viewpoint specifications**:

   * system or acting-holon families with current role assignments and stakeholder groups the viewpoint speaks for,
   * their **concerns**,
   * allowed **kinds of Description epistemes and Description epistemes admitted for specification use**,
   * and **conformance rules** for views under this viewpoint.
     (The internal structure of `U.Viewpoint` is fixed in E.17.0, not here.)
2. `ViewpointSlot` is a **SlotKind** with:

   * **ValueKind** `U.Viewpoint`,
   * **RefKind** `U.ViewpointRef`,
   * normative field name `viewpointRef? : U.ViewpointRef` on episteme cards or views.
3. For Description epistemes, including Description epistemes admitted for specification use, under E.10.D2, `viewpointRef` is a **mandatory part of `DescriptionContext`**; C.2.1 treats that as a **species-level constraint**, not as a universal requirement for all epistemes.
4. `ViewpointSlot` may be unset in purely internal, pre‑viewpoint epistemes (e.g., raw formal developments), but any episteme that participates in **MultiViewDescribing** (E.17.0) **MUST** set it or be deterministically associated to it via a `ViewpointBundle`.

**Didactic cue.**
“Ask: *Who is this for, and what do they need to see to accept it?* That is the Viewpoint.”

##### C.2.1:4.1.5 - `U.EpistemeView` / `U.View` and `ViewSlot` — episteme‑level views

**Tech:** `U.EpistemeView` (species of `U.Episteme`), selected short form `U.View`; `ViewSlot` (SlotKind); `viewRef : U.ViewRef`.
**Plain:** *view*, *epistemic view*.

**Intent.** Distinguish **view‑epistemes** (views **of** Description epistemes or Description epistemes admitted for specification use) from both:

* the underlying Description epistemes or Description epistemes admitted for specification use themselves, and
* the MVPK literal `publication-face form` and `interop publication form` values of `publication-face kind`, plus the publication-side carriers and renderings on which views are made available (E.17, publication-face-kind discipline, and A.10 carrier and source-currentness relations when evidence or reliance use is current).

**Normative definition.**

1. `U.EpistemeView` is a **species of `U.Episteme`** whose episteme kind includes, at minimum:

   * one `ClaimGraphSlot` (typically a **sliced or projected ClaimGraph**),
   * one `EntityOfConcernSlot`,
   * one `ViewpointSlot`,
   * and appropriate `ReferenceSchemeSlot`.
2. `U.View` is the **selected short form** for `U.EpistemeView` in E-cluster patterns (especially E.17.*), used where the word “view” is conventional.
3. `ViewSlot` is a **SlotKind** whose:

   * **ValueKind** is `U.View`,
   * **RefKind** is `U.ViewRef` (or `U.EpistemeViewRef` species),
   * intended usage is **in meta‑structures** such as `U.MultiViewDescribing` families and MVPK.
4. `ViewSlot` **MUST NOT** be confused with publication-face labels, `publication-face kind` declarations, or carrier slots: a concrete MVPK face that is a view is represented as `U.View` or `U.EpistemeView`, while the face label, publication-form profile, literal `publication-face form` or `interop publication form` `publication-face kind` value, and carrier or rendering remain separate relation positions.

**Didactic cue.**
“Ask: *Which particular slice of the description under this viewpoint are we talking about?* That is the View.”

##### C.2.1:4.1.6 - `U.ReferenceScheme` and `ReferenceSchemeSlot` — interpreting ClaimGraph as claims about entities

**Tech:** `U.ReferenceScheme` (ValueKind), `ReferenceSchemeSlot` (SlotKind); `referenceScheme? : U.ReferenceScheme`.
**Plain:** *reference scheme*, *interpretation scheme*, *description scheme*.

**Intent.** Separate **what is being said** (ClaimGraph) from **how claims are read as statements about entities and contexts** (designation, measurement, evaluation envelopes), without reifying the referents themselves as a vertex.

**Normative definition.**

1. `U.ReferenceScheme` is a **component type of epistemes**, not an external entity:

   * it determines how nodes of `U.ClaimGraph` are mapped to **properties or relations** over values of `EntityOfConcernSlot`,
   * it specifies **measurement and evaluation templates** (how to test claims on `GroundingHolon`),
   * it fixes **claim-scope predicates and admissible regions** over declared `U.ContextSlice` selectors (and, where needed, references to domain spaces used inside those selectors).
2. `ReferenceSchemeSlot` is a **SlotKind** with:

   * **ValueKind** `U.ReferenceScheme`,
   * **no RefKind in the minimal core** (ReferenceSchemes are stored by value as `referenceScheme? : U.ReferenceScheme` fields on episteme cards or views).
     Discipline packs **may** introduce `U.ReferenceSchemeRef` as a **RefKind**, but **must not** repurpose it as a new ValueKind.
3. `ReferenceScheme` is the place where Object-vertex concerns are split into explicit claim-to-EntityOfConcern and claim-to-grounding rules:

   * it does **not** “contain” the EntityOfConcern value or grounding referent,
   * it carries the **rules** that tie claims to entities and groundings.

**Didactic cue.**
“Ask: *Given this ClaimGraph, how exactly do we treat it as talking about these entities in these contexts, and how do we test it?* That is the ReferenceScheme.”

##### C.2.1:4.1.7 - Minimal slot relation and extension C.2.1+

The **minimal `U.EpistemeSlotRelation` core** for C.2.1 consists of positions (the episteme core SlotKinds of A.6.5 CC-A.6.5-5):
* `EntityOfConcernSlot` (ValueKind `U.Entity`),
* `GroundingHolonSlot` (ValueKind `U.Holon`),
* `ClaimGraphSlot` (ValueKind `U.ClaimGraph`),
* `ViewpointSlot` (ValueKind `U.Viewpoint`),
* `ViewSlot` (ValueKind `U.View`),
* `ReferenceSchemeSlot` (ValueKind `U.ReferenceScheme`).

This pattern **only fixes these positions** and their SlotSpec discipline. It does not turn every graph-valued value into a tuple and does not turn the tuple into a graph.
The **extension C.2.1+** (second step of the refactor) adds:
* `U.RepresentationScheme` and `RepresentationSchemeSlot`,
* `U.RepresentationToken` and `RepresentationTokenSlot`,
* `U.PresentationCarrier` and `PresentationCarrierSlot`,
* `U.RepresentationOperation` and `RepresentationOperationSlot` (with inference regime annotations),

without changing:
* the definition of `U.EpistemeKind`,
* the minimal `U.EpistemeCard` interface,
* or the assumptions A.6.2-A.6.4 and E.17.* make about episteme components.

In C.2.1+ `U.PresentationCarrier`, publication-face-kind values, MVPK face, carrier, and rendering relations remain **publication-side carriers, faces, forms, units, or rendering relations**, not semantic parts of the episteme:
`U.PresentationCarrier` values are linked to `U.Episteme` and `U.View` via MVPK and publication-face-kind discipline relations, such as `isCarriedBy` and MVPK face relations, and **MUST NOT** be counted as components when reasoning about episteme identity, EntityOfConcernSlot filling, GroundingHolonSlot filling, or KD-CAL morphisms. Changing carriers, publication faces, publication forms, units, or renderings alone **never** changes the `U.Episteme` instance determined by C.2.1; it only produces `U.Work` occurrences that publish or republish the same `U.Episteme`.

##### C.2.1:4.1.8 - Attached epistemic structures (non-slot components)

`U.EpistemeSlotRelation` deliberately does **not** reify every episteme-adjacent structure as a slot. Several key structures remain **attached, non-slot components** of `U.Episteme`:
* **`JustificationGraph`** - the argument and evidence graph for nodes of `U.ClaimGraph` (A.10 and B.3).
* **`EvidenceBindings`** - per-claim evidence-use bindings, A.10 evidence-provenance refs, or B.3 assurance-evidence refs that connect claims to evidence-producing or evidence-interpreting `U.Work` occurrences, role assignments when current, carrier and source-currentness records, and publication or carrier relations.
* **`EditionSeries`** - the `PhaseOf` chain of episteme editions (A.14) with change-class annotations (symbol-only vs ClaimGraph vs ReferenceScheme changes).
* **`ScopeCard` and `U.ClaimScope`** - USM scope values (A.2.6) describing where the episteme's claims hold.

These attached structures are **not extra positions** of `U.EpistemeSlotRelation`; they hang off the `U.ClaimGraph` and `U.ReferenceScheme` pair and are governed by KD-CAL (C.2), A.10, and B.3. C.2.1 only requires that an episteme which participates in KD-CAL exposes them in a way that keeps **ClaimGraph, ReferenceScheme, Evidence, EditionSeries, and `ClaimScope`** clearly distinguishable.

#### C.2.1:4.2 - Episteme as n‑ary relation and as holon

To prevent confusion between **EntityOfConcern values**, their **descriptions**, and the **slots they fill in an episteme**, C.2.1 explicitly treats epistemes both as:

1. **n‑ary relations with a signature** (slots & values), and
2. **holons with components** (fields & parts).

##### C.2.1:4.2.1 - `U.EpistemeKind` — episteme as a typed n‑ary relation

**Tech:** `U.EpistemeKind` (ValueKind).

**Intent.** Provide a **signature‑level** description of an episteme as an n‑ary relation whose arguments are governed by `SlotKind`/`ValueKind`/`RefKind` triples per A.6.5.

**Normative definition.**

1. Every episteme that participates in KD‑CAL **belongs to some `U.EpistemeKind`**.
   The kind determines:

   * which **SlotKinds** appear (`EntityOfConcernSlot`, `GroundingHolonSlot`, `ClaimGraphSlot`, `ViewpointSlot`, `ViewSlot`, `ReferenceSchemeSlot`, …),
   * the **ValueKind** for each slot (declared through C.3 `U.Kind`, an admitted durable U-kind, a direct governed value kind, a Concept-Set row, or an imported signature symbol),
   * the **RefKind** used to store it in episteme (when applicable).
1. `U.EpistemeKind` is a **special case** of `U.Signature` (A.6.0), with its slots governed by `U.RelationSlotDiscipline` (A.6.5). C.2.1 **MUST NOT** define an alternative slot discipline.
2. For the minimal core, every `U.EpistemeKind` **MUST** include:
   * exactly one `ClaimGraphSlot`,
   * at least one `EntityOfConcernSlot`,
   * and at least one `ReferenceSchemeSlot`.
     Inclusion of `GroundingHolonSlot`, `ViewpointSlot`, `ViewSlot` **MAY** be species-level constraints (mandatory for Description epistemes, including Description epistemes admitted for specification use, optional for others).

**Didactic cue.**
“An `EpistemeKind` is the *kind declaration* for an episteme: which positions it has and what can go into them.”

##### C.2.1:4.2.2 - Filled episteme value assignment and C.29 tuple view

**Tech:** filled episteme value assignment over `U.EpistemeSlotRelation`; C.29 tuple view when tuple reasoning is current.

**Intent.** Model a filled use of an episteme's slot relation without making tuple, graph, or publication form into the ontology head.

**Normative definition.**

1. A filled episteme value assignment supplies one governed value or reference for each asserted SlotKind in the associated `U.EpistemeKind`:
   * for each SlotKind in the associated `U.EpistemeKind`, a value of the slot's **ValueKind** or a reference value of **RefKind**, if the kind is configured as such.
2. The filled assignment is **notation-agnostic** and **carrier-agnostic**: it does not know about files, formats, publication faces, publication forms, or carriers.
   It exists to give A.6.2-A.6.4 a minimal notion of "episteme as a filled point over the episteme SlotRelation".
3. Under `C.29`, the same filled assignment may be viewed as a tuple when tuple reasoning is the selected mathematical lens. That tuple view is a mathematical-lens representation of the filled SlotRelation, not a second episteme kind and not a replacement for graph-valued fillers such as `U.ClaimGraph`.
4. In ordinary episteme work, the filled assignment rarely appears directly; it is typically **induced** by `U.EpistemeCard` and `U.EpistemeView` (which add component structure and meta-information).

**Didactic cue.**
"A filled episteme assignment says *what fills which slots*; if C.29 asks for tuple reasoning, read that assignment as a tuple view."

##### C.2.1:4.2.3 - `U.EpistemeCard`, `U.EpistemePublication`, `U.EpistemeView` — holonic realisations

**Tech:** `U.EpistemeCard`, `U.EpistemePublication`, `U.EpistemeView` (species of `U.Episteme`).

**Intent.** Provide **holon-level structures** that engineers can work with (components, mereology, provenance), while keeping them aligned with `U.EpistemeKind` and `U.EpistemeSlotRelation`.

**Normative definition.**

1. **`U.EpistemeCard`.**
   A species of `U.Episteme` whose components correspond one‑to‑one to slots of some `U.EpistemeKind`:
   * `content : U.ClaimGraph` (for `ClaimGraphSlot`),
   * `entityOfConcernRef : U.EntityRef` (for `EntityOfConcernSlot`),
   * `groundingHolonRef? : U.HolonRef` (for `GroundingHolonSlot`),
   * `viewpointRef? : U.ViewpointRef` (for `ViewpointSlot`),
   * `referenceScheme? : U.ReferenceScheme` (for `ReferenceSchemeSlot`),
   * optionally `representationSchemeRef? : U.RepresentationSchemeRef` (C.2.1+),
   * `meta : Edition, Provenance, Status...`.
     Minimal episteme identity is the pair `⟨content, entityOfConcernRef⟩` within a `U.BoundedContext`; all other fields are optional at the genus level but may be mandatory in species. Changes that alter `content` or the effective `referenceScheme` (or that intentionally re-identify `entityOfConcernRef`) **SHALL** be realised as new phases in an `U.EditionSeries` (PhaseOf chain) under A.14 and A.7. Changes confined to `U.PresentationCarrier`, publication-side values, MVPK face, carrier, or rendering relations **do not** create a new episteme; they are captured as publication work over the same `U.Episteme`.
2. **`U.EpistemePublication`.**
   A species representing **epistemes that have been published** through publication faces, publication forms, or MVPK relations. It:
   * has at least the components of `U.EpistemeCard`,
   * plus references to MVPK `U.View`, face identity, literal `publication-face form` or `interop publication form` `publication-face kind` values, publication-scope fields, profile fields, and external carrier or rendering refs as required by E.17 and publication-face-kind discipline,

   * but **does not** re-interpret face labels, `publication-face kind` values, or carriers or renderings as parts of the episteme; carriers remain external.

3. **`U.EpistemeView`.**
   As defined in §4.1.5, a species of `U.Episteme` representing a **view** under a specific `U.Viewpoint`.
   Its components are a specialisation of `U.EpistemeCard`:
   * ClaimGraph often a restricted projection of a base description and specification-useification,
   * Viewpoint fixed,
   * ReferenceScheme tailored to that viewpoint.

**Alignment requirement.**
For any of these species, the pattern **MUST** state explicitly:
* which `U.EpistemeKind` it realises, and
* how each component maps to a SlotKind or RefKind under `U.RelationSlotDiscipline`.

This ensures that A.6.2–A.6.4 can treat any `U.Episteme*` uniformly as both:
* a category-theory object in the category **Ep**, and
* a structured holon with components.

##### C.2.1:4.2.3a - Episteme, publication, view, carrier, cue, and authority-reference relation positions  *(normative)*

C.2.1 is the default FPF pattern for claim-bearing units. Do not mint a generic `U.SemioObject`, `U.SemioticObject`, `U.SignObject`, `U.WorkingObject`, or `U.SourceMaterial` when the claim-bearing unit in question should be modeled as an episteme. Use `U.Episteme` or a declared species of `U.Episteme`.

When the same claim-bearing unit is available to readers, tools, or downstream work as a published episteme, name that relation position as `U.EpistemePublication` or as a governed `U.Episteme` publication. Then keep the adjacent relation positions separate:

* **publication form** - the concrete form in which the episteme is made available for some use, such as a cue pack, transfer-prepared claim set, prompt form, partial normal form, record, card, table, or local C.29 output;
* **view, including MVPK face** - `U.View` or `U.EpistemeView` under a declared `U.Viewpoint`, including MVPK faces such as `PlainView`, `TechCard`, `InteropCard`, or `AssuranceLane`;
* **carrier or rendering** - the document, dashboard, generated screen, trace file, transport envelope, display, or A.10 carrier and source-currentness record that bears or renders a publication;
* **source-finding cue** - a badge, tile, heading, signature-looking mark, credential display, generated explanation, or other cue that helps find a source but does not by itself create an authority-reference relation;
* **governing pattern reference and authority-reference field** - `governingPatternRef` when one FPF pattern governs admissible interpretation or use; `authoritySourceRef` when a non-pattern authority-source referent such as an external standard, editioned register, decision record, gate decision, policy source, or role-assignment or status register carries the relevant authority. The publication records this reference; it does not become the referenced authority.

For latent, distributed, reconstructed, or model-state material, do not call the encountered material a `U.Episteme` merely because it can be decoded into prose, embedded in a vector space, or shown as a dashboard cue. It becomes an episteme only when the needed C.2.1 positions are recoverable for the current use: at least the `EntityOfConcernSlot`, `ClaimGraphSlot`, `ReferenceSchemeSlot` or equivalent interpretation rule, and any current grounding, viewpoint, view, publication, carrier, source-use, evidence, or authority-reference relation named by the direct governing pattern.

No publication form, view, face, carrier, rendering, source-finding cue, dashboard signal, credential display, generated explanation, FPF pattern file, or FPF pattern section is itself a substitute for a governed `U.Episteme`, an evidence relation, an assurance claim, a gate decision, a permission, a role claim, a status claim, or a `U.Work` occurrence. If the next move concerns work, keep candidate reliance, `U.WorkPlanning`, planned work, actual `U.Work`, work result, and work-result measurement in their own work-side patterns rather than storing them inside the episteme or its carrier.

##### C.2.1:4.2.4 - SlotKind, ValueKind, and RefKind discipline for EntityOfConcern and GroundingHolon

C.2.1 adopts **A.6.5 `U.RelationSlotDiscipline`** wholesale. For the two key positions:
1. **EntityOfConcernSlot.**
   * `SlotKind = EntityOfConcernSlot`;
   * `ValueKind = U.Entity` (species may constrain to `EntityOfConcernClass ⊑ U.Entity`);
   * `RefKind = U.EntityRef` (or a species thereof);
   * normative field name in episteme cards: `entityOfConcernRef : U.EntityRef`.
     No durable U-kind named `U.EntityOfConcern` is introduced; the phrase “EntityOfConcern value” always means “an instance of `U.Entity` filling `EntityOfConcernSlot`”.
1. **GroundingHolonSlot.**
   * `SlotKind = GroundingHolonSlot`;
   * `ValueKind = U.Holon`;
   * `RefKind = U.HolonRef`;
   * normative field name: `groundingHolonRef? : U.HolonRef`.
     There is no durable U-kind `U.GroundingHolon`; “grounding holon” is a **slot-filler phrase**.
Any episteme text that mixes slot, value, and ref concepts (e.g., using `EntityOfConcernRef` as if it were a type) **MUST** be repaired to this discipline when the claim is current; C.2.1 provides the normative reference, and F.18 or the relevant discipline pattern governs any naming decision.

#### C.2.1:4.3 - Minimal epistemic morphisms (informal schema)

> **Note.** The full mathematical treatment (categories Ep and Ref, entityOfConcern functor `α : Ep → Ref`, and effect‑free morphisms) lives in A.6.2–A.6.4. Here we fix only the **episteme-slot relations** that C.2.1 expects to exist between its positions.

At the level of `U.EpistemeCard` components and SlotKinds, we assume the following **primitive relations** (not all are functions):

1. **`entityOfConcernSet : U.Episteme → P(U.Entity)`**
   *derivable from `EntityOfConcernSlot` and `ReferenceScheme`*
   * For an episteme `E`, `entityOfConcernSet(E)` is (at least) the singleton containing the entity referenced by `entityOfConcernRef(E)`; in more complex cases, it may be a finite set or bundle of entities, determined by `ReferenceScheme`.
   * The **functorial EntityOfConcern mapping** `δ_E : Ep → Ref` used in A.6.2–A.6.4 is the categorical lift of this relation: it forgets episteme internals and keeps only the EntityOfConcern value in the ReferencePlane determined by the pair `<EntityOfConcernSlot, GroundingHolonSlot>`.

2. **`grounds : (U.Entity, U.Holon) ⇝ GroundingRelation`**
   *relates EntityOfConcern values to grounding holons*
   * Captures how values of `EntityOfConcernSlot` are **situated** in holons that make evaluation possible (labs, infrastructures, organisations).
   * Need not be total or functional; an entity may admit multiple grounding holons, or none.

3. **`designates : (U.ReferenceScheme, U.ClaimGraph, U.Entity, U.Holon) ⇝ DesignationProfile`**
   *how claims are read as statements about entities in contexts*
   * Specifies, for each claim in `content` and each `<entityOfConcernRef, groundingHolonRef>`, what property or relation it purports to state, and under what conditions.

4. **`satisfies` or `evaluatesTo : (U.ClaimGraph, U.ReferenceScheme, U.Holon) -> TruthProfile or SuccessProfile`**
   *evaluation of claims under a reference scheme and grounding*
   * Forms the bridge to KD‑CAL’s `F, G, R` evaluation; details are given in C.2 and B.3.

5. **View-related morphisms** (to be connected with A.6.3):
   * `viewProject : (U.Episteme, U.Viewpoint) → U.View`
     — effect-free, **EntityOfConcern-preserving** projection that slices `ClaimGraph` and specialises `ReferenceScheme` under a given viewpoint.
   * `viewEmbed : U.View → U.Episteme`
     — embedding of a view back into the wider episteme, typically as a reference with correspondence proofs.

5. **Reflexive entityOfConcern guard.**
   When `EntityOfConcernSlot` or `ReferenceScheme` picks out an episteme or claim that includes the referring claim itself (**ReferencePlane = episteme**), publishers **SHALL** ensure that the induced justification and evaluation structure is **acyclic per evaluation chain**: reflexive describe or citation handles may exist as literature handles, but they MUST NOT form a minimal justification cycle for acceptance or KD-CAL assurance. Self-reference is allowed as a citation pattern, not as a way to close justification loops.

These are **not yet laws**; they are the **hooks** that A.6.2–A.6.4 will formalise into:
* `U.EffectFreeEpistemicMorphing` (Ep→Ep morphisms over this structure),
* `U.EpistemicViewing` (entityOfConcern‑preserving Ep→Ep),
* `U.EpistemicRetargeting` (entityOfConcern‑retargeting Ep→Ep).

