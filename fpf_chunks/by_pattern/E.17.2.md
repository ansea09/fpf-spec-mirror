---
chunk_kind: "parent"
pattern_id: "E.17.2"
pattern_title: "TEVB — Typical Engineering Viewpoints Bundle"
section_id: null
section_title: null
source_path: "FPF-Spec.md"
output_path: "by_pattern/E.17.2.md"
commit_sha: "093d30e806a1466e24032733eb020bb5a5f585cc"
heading_path:
  - "E.17.2 — TEVB — Typical Engineering Viewpoints Bundle"
line_start: 62847
line_end: 63262
dependencies:
  - "A.1"
  - "A.6.2-A.6.4"
  - "A.7"
  - "C.2.1"
  - "E.10.D2"
  - "E.17"
  - "E.17.0"
  - "E.17.1"
  - "E.18"
  - "E.TGA"
  - "F.18"
  - "U.MultiViewDescribing"
  - "U.ViewpointBundleLibrary"
keywords:
---

## E.17.2 - `TEVB — Typical Engineering Viewpoints Bundle`

> **Tech‑name:** `TEVB` (Typical Engineering Viewpoints Bundle, bundle id `VF.TEVB.ENG`)
> **Plain‑name:** typical engineering viewpoints bundle for holons
> **Tag:** Archetypal species of `U.ViewpointBundle` for engineering holons

**Status.** Stable; archetypal, notation‑agnostic species of `U.ViewpointBundle` / `U.ViewpointBundleLibrary`.
It is an engineering‑level bundle over holons; it does not itself constitute an architecture framework or architecture‑specific viewpoint library. Architecture‑focused viewpoint bundles are introduced as separate `U.ViewpointBundle` species that may import TEVB.

**Builds on.**
* **E.17.0 — `U.MultiViewDescribing`.** Supplies the generic notion of `U.Viewpoint`, `U.View`, and `ViewFamily` over an `EntityOfConcernClass ⊑ U.Entity` (here: `EntityOfConcernClass = U.Holon`).
* **E.17.1 — `U.ViewpointBundleLibrary`.** Provides the generic `U.ViewpointBundle`/`ViewFamilyId` structure; TEVB is a concrete bundle (`VF.TEVB.ENG`) in the core library.
* **A.1 — Holon.** Holon kinds `U.System` and `U.Episteme` as the typical engineering entities of concern.
* **A.6.2–A.6.4 — Episteme morphisms.** `U.EffectFreeEpistemicMorphing`, `U.EpistemicViewing`, `U.EpistemicRetargeting` as the generic morphism classes behind engineering views.
* **A.7 and E.10.D2 - Strict Distinction: EntityOfConcern, Description episteme, and Description episteme admitted for specification use.** TEVB uses DescriptionContext; engineering descriptions and specifications under TEVB are Description epistemes and specification-use cases with explicit `ViewpointRef`.
* **C.2.1 — `U.EpistemeSlotGraph`.** Provides `EntityOfConcernSlot`, `ViewpointSlot`, `ViewSlot` and the slot discipline (A.6.5) used by TEVB-aligned Description epistemes and specification-use Description epistemes.

**Used by.**
* **E.18:5.12 — E.TGA viewpoint map.** As a canonical consumer, E.TGA binds its engineering transduction families (Functional, Procedural, Role-Enactor or Device-Structure, Module-Interface) to TEVB viewpoints `VP.Functional`, `VP.Procedural`, `VP.RoleEnactor`, `VP.ModuleInterface`.
* **E.17 (MVPK).** Publication of engineering morphisms uses TEVB engineering viewpoints on the Description-episteme and specification-use side and separate publication-side viewpoints over publication faces and forms.
* **Engineering description and specification-use patterns.** System, method, module-interface and role-related Description-episteme and specification-use patterns for holons (`U.System`, `U.Episteme`) refer to TEVB when declaring their `ViewpointRef`.
* **ISO‑aligned architecture‑description bundles.** Future species patterns for architecture‑specific viewpoint bundles reuse TEVB as the canonical engineering view family (Functional vs Structural etc.) over systems and their epistemes.

**Guard (lexical & ontological).**
**Selected-family scope.** TEVB's engineering viewpoints are scoped by `EntityOfConcernClass = U.Holon` with usual `U.System` and `U.Episteme` cases. ISO 42010 concern/viewpoint/view language is used as architecture-description practice alignment, not as imported FPF ontology.

1. **Engineering scope only.** TEVB applies to `EntityOfConcernClass = U.Holon` with typical cases `U.System` and `U.Episteme`. Using TEVB viewpoints for non‑holonic entities (e.g., pure data structures, abstract theories) requires an explicit species‑level justification; by default it is a conformance violation.
2. **Viewpoint vs publication face/form/carrier.** `VP.Functional`, `VP.Procedural`, `VP.RoleEnactor`, `VP.ModuleInterface` are **viewpoints** (`U.Viewpoint` specifications), not publication face, publication form, rendering, or carrier names. A conforming TEVB use keeps `{PlainView, TechCard, NormsCard, InteropCard, AssuranceLane, ...}` as publication faces/forms under MVPK and does not use `VP.*` ids as carrier or publication-form ids.
3. **EngineeringVPId vs publication-side viewpoint id.** `VP.*` in this pattern are **EngineeringVPId** values (E.18:5.12). MVPK publication uses separate publication-side viewpoint ids, linked to TEVB viewpoints only through correspondences.
4. **No new role coordinates in EntityOfConcern and Description-episteme boundary and specification-use discipline.** TEVB references stakeholder groups via `U.RoleEnactor` families but does not introduce `U.Role` as a coordinate in Description episteme or specification-use case signatures (E.10.D2). Role semantics remain confined to RoleEnactment patterns (A.15, F-R family).
5. **EntityOfConcern retention.** In ordinary TEVB use, `DescriptionContext.EntityOfConcernRef` remains the holon selected by `EntityOfConcernClassSpec`. Capability, Method, procedure/control, role-enactor structure, structural architecture, module, interface, and allocation terms are viewpoint concern/content inside the Description episteme unless the text explicitly opens A.6.4 retargeting with a KindBridge and species-extension rule.
6. **No extra viewpoints inside TEVB.** TEVB defines a **fixed core set** of four engineering viewpoints. Other labels such as “Assurance‑Oriented”, “Interop‑Oriented”, “Information/Data‑Oriented”, “Operational/Deployment”, “Mission/Context” may appear only as **lexical aliases** in E.18:5.12 (e.g. as `ViewFamilyId` / `AliasInViewFamilies` values for transduction species). They do not extend `TEVB.EngBundle.viewpoints` and are not additional `U.Viewpoint` kinds in this bundle; when SoTA or local practice demands explicit assurance, information, or mission viewpoints, provide them as **separate `U.ViewpointBundle` species** imported alongside TEVB rather than by mutating `VF.TEVB.ENG`.
7. **Not an architecture framework.** TEVB is an engineering‑level viewpoint bundle; architecture‑specific viewpoint bundles and architecture frameworks MUST be introduced as separate `U.ViewpointBundle` species that may import TEVB. They keep `VF.TEVB.ENG` as the engineering viewpoint bundle and put architecture-only viewpoints in separate architecture-specific `U.ViewpointBundle` species.

### E.17.2:1 - Problem frame  *(informative)*

Engineering teams almost always talk about systems and their models through a **small set of recurring “views”**:
* *What capabilities and behaviours does the system enact?* — function‑oriented, transduction‑oriented talk.
* *What sequences, workflows, and control logics does it realise?* — procedure/process/state‑oriented talk.
* *Who or what enacts which roles?* — role‑enactment, organisational and socio‑technical talk.
* *How is the system decomposed into modules and interfaces?* — physical/logical architecture talk.

In industry, these lenses show up under many names: *functional view, logical view, behavioural view, process view, structural/physical view, deployment view, responsibility view,* and so on. Modern standards and tools (ISO/IEC/IEEE 42010:2022, INCOSE SE Handbook, SysML v2 “views as queries”) all recognise that **viewpoints should be reusable structures**, not ad‑hoc labels.

In FPF, E.17.0 and E.17.1 give the **generic machinery**:
* `U.Viewpoint` as a viewpoint specification (stakes/concerns/allowed Description kinds and specification-use gates),
* `U.View` as an episteme‑level view (epistema under a viewpoint),
* `U.ViewpointBundle` / `ViewFamilyId` as reusable collections of viewpoints.

E.TGA (E.18:5.12) already assumes a **canonical engineering family** with names like “Functional”, “Procedural”, “Role-Enactor (Device-Structure)”, “Module-Interface”. Without a formal bundle tying these together, those names drift and the mapping between E.TGA, MVPK, EntityOfConcern, Description-episteme boundary, and specification use becomes fragile.

TEVB addresses this by defining a **single, explicit engineering bundle** with a fixed `ViewFamilyId` and a small set of canonical engineering viewpoints over `U.Holon`.

### E.17.2:2 - Problem  *(informative)*

Without TEVB, several failure modes recur:
1. **Inconsistent “functional”, “structural”, and “behavioural” vocabularies.** Different teams define “functional view” or “process view” differently, even within one organisation; E.TGA E.18:5.12 then has to guess how to map transduction graphs onto whichever interpretation is currently in play.
2. **Architecture frameworks leak into the kernel.** 4+1‑style and similar architectural frameworks get hard‑coded as if they were universal; FPF loses its holonic neutrality and becomes biased to a particular school.
3. **Viewpoints conflated with publication faces/forms and files.** “Functional view” is used both for the underlying viewpoint and for a concrete document or dashboard; MVPK faces/forms, E.TGA transduction families, and EntityOfConcern and Description-episteme and specification-use distinctions become entangled.
4. **Role leakage into EntityOfConcern and Description-episteme boundary and specification-use discipline.** Engineering views that are about role-enactors are written directly in terms of `U.Role`, blurring the boundary between RoleEnactment (A.15) and description and specification-use lanes, and breaking A.7 and E.10.D2.
5. **Poor reuse across systems.** Even when organisations want to reuse the same engineering views across products, plants, or models, there is no canonical bundle to import; each programme recreates “its own” functional/structural views.

TEVB makes engineering viewpoint families **first‑class reusable bundles** and pins them to an explicit `EntityOfConcernClass` (engineering holons) so that E.TGA, MVPK and discipline‑packs can align on the same vocabulary.

### E.17.2:3 - Forces  *(informative)*

| Force                                       | Tension                                                                                                                                                                       |
| ------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Universality vs domain idioms**           | We need engineering viewpoints that work for *any* holon (hardware, software, or socio-technical), yet remain recognisable to practitioners steeped in domain-specific frameworks. |
| **Parsimony vs expressiveness**             | A small, stable **NQD-front** set of engineering view families (Function, Behaviour and Process, Role-Enactor, Module-Interface) vs the temptation to proliferate specialised views for every stakeholder group or quality attribute. |
| **Neutral core vs architecture frameworks** | FPF core must stay neutral and not encode a specific framework (4+1, DoDAF, etc.), while still being compatible with them.                                                    |
| **Consistency vs organisational autonomy**  | Central TEVB definitions must be stable, yet individual organisations need room to refine concerns and episteme kinds within the bundle.                                      |
| **EntityOfConcern and Description-episteme boundary plus specification-use clarity vs convenient shortcuts**   | Viewpoints must not re-introduce `Role` as a coordinate in EntityOfConcern and Description-episteme boundary or specification-use discipline, nor blur Description-episteme and specification-use distinctions with publication face, form, or carrier distinctions, even though practitioners informally mix these.             |

TEVB resolves these by fixing a **minimal engineering bundle** and leaving customisation to **species patterns and ViewpointBundleLibrary entries** that refine concerns and allowed episteme kinds without changing the core families.

### E.17.2:4 - Solution — TEVB as a core `U.ViewpointBundle` for holons  *(normative)*

#### E.17.2:4.1 - TEVB bundle identity

TEVB is the **core engineering viewpoint bundle** over holons.

* **Bundle object.** There exists a canonical `U.ViewpointBundle` instance:

  ```
  TEVB.EngBundle : U.ViewpointBundle
  ```

* **ViewFamilyId.**

  ```
  TEVB.EngBundle.viewFamilyId = VF.TEVB.ENG
  ```

  `VF.TEVB.ENG` is reserved for **“Typical Engineering Viewpoints (Engineering)”** in the FPF core ViewpointBundleLibrary.

* **EntityOfConcernClassSpec (holon scope).**

  TEVB is parameterised by

  ```
  TEVB.EngBundle.EntityOfConcernClassSpec =
    { h : U.Holon | holonKind(h) ∈ {U.System, U.Episteme} }
  ```

  That is, TEVB applies to holons that are either `U.System` or `U.Episteme`. Other holon kinds MAY be added by species patterns but MUST be justified and documented; the default conformance profile assumes systems and epistemes.

* **Library placement.**

  TEVB lives in the core viewpoint library:

  ```
  TEVB.Library : U.ViewpointBundleLibrary
  TEVB.Library.libraryId = FPF.Core.Viewpoints
  TEVB.Library.bundles ⊇ { TEVB.EngBundle }
  ```

  Additional organisational libraries MAY import and specialise TEVB, but SHALL NOT redefine `VF.TEVB.ENG` with incompatible semantics.

* **Viewpoint set.**

  TEVB defines a **finite set of canonical engineering viewpoints**:

  ```
  TEVB.EngBundle.viewpoints =
    { VP.Functional, VP.Procedural, VP.RoleEnactor, VP.ModuleInterface }
  ```

The selection `{VP.Functional, VP.Procedural, VP.RoleEnactor, VP.ModuleInterface}` is the current **NQD-frontier** for engineering holon viewpoints in Part G: it realises a Function-Behaviour-Structure-plus-Role (`F-B-S+R`) cut that is non-dominated against candidate families including explicit information or data, assurance or safety, and mission or context viewpoints under the N, U, C, and D characteristics (C.18, G.0). Part G records the SoTA candidate set and rejected alternatives; TEVB only fixes the **core four** where each `VP.* : U.Viewpoint` is defined below. These four are the **only** viewpoints in the core TEVB bundle.

  > **Note.** Other ViewFamilyId values used in E.TGA (e.g., *Assurance‑Oriented*, *Interoperability‑Oriented*, *Information/Data‑Oriented*, *Operational/Deployment*, *Mission/Context*) remain **lexical families only** for transduction species (E.18:5.12). They do not add viewpoints to TEVB; they are orthogonal to TEVB’s `viewpoints` set.

#### E.17.2:4.2 - TEVB engineering viewpoints

Each TEVB viewpoint is a `U.Viewpoint` with:
* `viewpointId : ViewpointId` (concrete identifier, e.g., `VP.Functional`);
* `EntityOfConcernClassSpec` **inherited from the bundle** (`U.Holon` with `System`/`Episteme` kinds);
* `StakeholderFamilies : FinSet(RoleEnactorFamilyId)` — families of `U.RoleEnactor` that are the primary audience;
* `Concerns : FinSet(ConcernId)` — engineering concerns this viewpoint foregrounds;
* `AllowedEpistemeKinds : FinSet(U.EpistemeKindRef)` — Description-episteme and specification-use kinds admissible under this viewpoint (all obeying EntityOfConcern and Description-episteme boundary, specification use, and C.2.1 slot disciplines);
* `ConformanceRules : FinSet(RuleId)` — references to checklist items in conformance packs (CV/GF/engineering checklists).

The subsections below fix the **normative intent and minimal field profiles** for each TEVB viewpoint. Species patterns and discipline‑packs may refine `Concerns`, `AllowedEpistemeKinds` and `ConformanceRules`, but MUST preserve the intent.

##### E.17.2:4.2.1 - `VP.Functional` — capability & transduction viewpoint

**Intent.** Look at a holon in terms of **what it can do** under roles: capabilities, transductions, and functional responsibilities, rather than in terms of modules or procedures.

* **viewpointId.**

  ```
  VP.Functional : ViewpointId  // EngineeringVPId
  ```

* **EntityOfConcernClassSpec.**
  Same as the bundle: `U.Holon` with `System`/`Episteme` kinds.

* **StakeholderFamilies (typical examples).**
  Actual `StakeholderFamilies : FinSet(U.RoleEnactor)` values are defined in RoleEnactment discipline packs; labels below are informal.
  * System engineering leads and architects (e.g. SysEng‑lead enactors).
  * Product owners / capability owners.
  * Reliability / performance engineers when reading capability envelopes.

* **Concerns (typical).**
  * Capabilities and functions provided by the holon (`CapabilityConcerns`).
  * Behaviour under roles (`RoleBehaviourConcerns`).
  * Non‑functional envelopes: throughput, latency, availability, energy, safety (`NFPEnvelopeConcerns`).
  * Compositional semantics of functions/transductions (`TransductionCompositionConcerns`).

* **AllowedEpistemeKinds (shape).**
  `VP.Functional` admits Description epistemes and specification-use Description epistemes whose **EntityOfConcernSlot** remains the holon and whose viewpoint content foregrounds the holon's **Capability**, **Method**, **Mechanism**, or transduction claims under a role, e.g.:
  * `SystemFunctionalDescription`, `SystemFunctionalSpec` (species of `U.EpistemeKind` describing system‑level capabilities and their interconnection).
  * `TransductionDescription`, `TransductionSpec` (E.TGA functional lanes).
  * `ServiceCapabilityDescription`, `ServiceCapabilitySpec` (when a holon is in Service role).

  All such epistemes satisfy these admissibility checks:
  * obey EntityOfConcern and Description-episteme boundary plus specification-use discipline: `…Description` names a Description episteme about the holon and `…Spec` names specification-use case of that Description episteme for declared Capability, Method, Mechanism, or PromiseContent content;
  * make their `DescriptionContext = ⟨EntityOfConcernRef, BoundedContextRef, ViewpointRef⟩` explicit, with `ViewpointRef = VP.Functional`.

* **ConformanceRules (examples).**
  * Functional flows are **total** over their declared domain (no implicit dangling capabilities).
  * Transductions are typed at interfaces (A.6.0, A.6.1) and respect A.6.2/A.6.3 purity/conservativity.
  * When functional views participate in retargeting patterns (e.g. structural reinterpretation species based on `U.EpistemicRetargeting`), they MUST satisfy the relevant retargeting constraints from A.6.4; concrete consumer patterns (such as E.TGA structural reinterpretation, E.18) MAY impose additional rules.

* **SoTA echo (informative).** `VP.Functional` corresponds to the “functional view” in ISO-aligned architecture descriptions and domain reference architectures (functional viewpoints in IoT and space reference architectures, functional and logical layers in sector frameworks), and to the **Function** concern in FBS-style design ontologies. It is also the natural viewpoint-family placement for SysML and SysML-v2 capability and logical architecture models and for “logical view” slices in 4+1-style frameworks, once recast into holon/capability terms.

##### E.17.2:4.2.2 - `VP.Procedural` — process & control viewpoint

**Intent.** Look at a holon in terms of **how behaviours are sequenced and controlled**: workflows, state machines, operational procedures, and control logic.

* **viewpointId.**

  ```
  VP.Procedural : ViewpointId  // EngineeringVPId
  ```

* **EntityOfConcernClassSpec.**

  Same as the bundle.

* **StakeholderFamilies (typical).**
  * Operations and run‑time owners (`OperationsEnactorFamily`).
  * Control engineers and automation specialists (`ControlEngineerEnactorFamily`).
  * Safety engineers concerned with procedural correctness (`SafetyEngineerEnactorFamily`).

* **Concerns (typical).**
  * Control flow and ordering of actions (`OrderConcerns`).
  * State‑machine behaviour and lifecycle (`StateLifecycleConcerns`).
  * Concurrency, synchronisation, and error handling (`ConcurrencyConcerns`).
  * Operational modes and transitions (startup, shutdown, degraded modes) (`OperationalModeConcerns`).

* **AllowedEpistemeKinds (shape).**
  `VP.Procedural` admits Description epistemes and specification-use Description epistemes where the **EntityOfConcernSlot** remains the holon and the viewpoint content foregrounds the holon's Method, procedure, control behaviour, or work-plan content, e.g.:
  * `MethodDescription`, `MethodSpec` for operational procedures (A.3.1–A.3.2).
  * `ControlLogicDescription`, `ControlLogicSpec` (IEC 61131‑3 style step diagrams/statecharts).
  * `WorkflowDescription`, `WorkflowSpec` (business processes, orchestration logic).

  These epistemes:
  * respect the **order discipline** (Γ_method, Γ_ctx) and A.15 (Role–Method–Work alignment);
  * carry E.10.D2-conformant DescriptionContext with `ViewpointRef = VP.Procedural`.

* **ConformanceRules (examples).**
  * Pre/post‑conditions at step boundaries are explicit and type‑checked (A.3.1/A.3.2, Γ_method).
  * No embedding of Work or calendars inside procedural descriptions (A.7 and E.10.D2).
  * Failure modes and recovery actions are declared and traceable to safety analyses (F.15 harnesses where relevant).

* **SoTA echo (informative).** `VP.Procedural` captures the dynamic/process dimension found in SoTA architecture and MBSE practice: process views in 4+1, operational/behavioural views in defence and enterprise frameworks, behaviour diagrams in SysML (activity, sequence, state, interaction), and procedure/control‑oriented models in industrial standards. TEVB abstracts this into a notation‑agnostic “behaviour over time” viewpoint for holons.

##### E.17.2:4.2.3 - `VP.RoleEnactor` — role & device‑structure viewpoint

**Intent.** Look at a holon in terms of **who/what plays which roles** and **how physical/organisational structure enables those role enactments**. This viewpoint covers both socio‑technical role assignments and “device view” readings of transduction graphs (E.TGA).

* **viewpointId.**

  ```
  VP.RoleEnactor : ViewpointId  // EngineeringVPId
  ```

* **EntityOfConcernClassSpec.**

  Same as the bundle.

* **StakeholderFamilies (typical).**
  * Organisational designers and operations managers (`OrgDesignEnactorFamily`).
  * Safety and compliance officers concerned with separation of duties (`SegregationOfDutyEnactorFamily`).
  * Hardware/system engineers concerned with which devices carry which functions (`DeviceEngineerEnactorFamily`).

* **Concerns (typical).**
  * Which holons enact which roles under which contexts (`RoleEnactmentConcerns`).
  * Allocation of capabilities to devices/subsystems (`CapabilityAllocationConcerns`).
  * Organisational constraints: segregation of duties, responsibilities, escalation paths (`GovernanceConcerns`).
  * Device‑view readings of functional graphs (E.TGA Device‑View).

* **AllowedEpistemeKinds (shape).**
  `VP.RoleEnactor` admits Description epistemes and specification-use Description epistemes where the **EntityOfConcernSlot** remains the holon and the viewpoint content foregrounds **role structure, role enactment, or capability allocation** associated with that holon, e.g.:
  * `RoleDescription`, `RoleSpec` (F.4, F.18) for human or system roles.
  * `RoleEnactmentDescription` for mappings `Holder#Role:Context` (A.15).
  * `DeviceAllocationDescription` mapping functions/transductions to physical modules or devices.

  As with other TEVB viewpoints, these are Description epistemes and specification-use cases with `DescriptionContext.ViewpointRef = VP.RoleEnactor`.

* **ConformanceRules (examples).**
  * Role vs Method vs Work vs Capability separation is upheld (A.7, A.15).
  * Device‑view reinterpretation from functional flows MUST be expressed as `U.EpistemicRetargeting` with an explicit `KindBridge` witness (A.6.4). Specific retargeting schemes (for example, E.TGA’s structural reinterpretation in E.18) may add further constraints but are not fixed by TEVB itself.
  * No “role as behaviour” conflation: Roles are masks, behaviours remain Methods/Work.

* **SoTA echo (informative).** `VP.RoleEnactor` aligns with the allocation/responsibility and resource/organisational view clusters seen across MBSE frameworks: allocation views in UAF/NAF, role-responsibility matrices and RACI-style artefacts, and “who/what plays which role” slices in usage and operational viewpoints. Many post-2015 reference architectures treat this concern implicitly; TEVB makes it explicit and holon-centred while remaining compatible with socio-technical and device-allocation practices.

##### E.17.2:4.2.4 - `VP.ModuleInterface` — module & interface viewpoint

**Intent.** Look at a holon in terms of its **modules, interfaces, and structural composition**: what parts exist, how they connect, and how their interface specifications are stated.

* **viewpointId.**

  ```
  VP.ModuleInterface : ViewpointId  // EngineeringVPId
  ```

* **EntityOfConcernClassSpec.**
  Same as the bundle.

* **StakeholderFamilies (typical).**
  * Hardware and software architects responsible for structure (`StructureArchitectEnactorFamily`).
  * Integration and test engineers (`IntegrationEngineerEnactorFamily`).
  * Lifecycle and maintenance planners looking at replaceable units (`MaintenancePlannerEnactorFamily`).

* **Concerns (typical).**
  * Module decomposition and containment (mereology) (`ModuleMereologyConcerns`).
  * Interfaces and specifications — ports, APIs, physical connectors (`InterfaceConcerns`).
  * Dependency structures and allowed couplings (`DependencyConcerns`).
  * Replaceability and variation points (`VariabilityConcerns`).

* **AllowedEpistemeKinds (shape).**
  `VP.ModuleInterface` admits Description epistemes and specification-use Description epistemes where the **EntityOfConcernSlot** remains the holon and the viewpoint content foregrounds the holon's **structural architecture**, modules, interfaces, and connector arrangements, e.g.:
  * `SystemStructureDescription`, `SystemStructureSpec` (module/connector descriptions).
  * `ModuleInterfaceDescription`, `ModuleInterfaceSpec` (signature, interface specifications, physical interface definitions).
  * E.TGA‑style interface/port descriptions over `Signature`/`Mechanism` graphs.

  These epistemes describe holon structure, module-interface arrangement, ports/connectors, or structural architecture as viewpoint content about the holon rather than replacing the holon as the `EntityOfConcern`. Functional↔physical reinterpretations between `VP.Functional` and `VP.ModuleInterface` are expressed via `U.EpistemicRetargeting` + `KindBridge` (A.6.4, E.18) when the `EntityOfConcernRef` changes.

* **ConformanceRules (examples).**
  * Interfaces are typed and explicitly bound to standards where applicable (A.6.0, F‑specs).
  * No inlining of Methods/Work into structure (strict separation of structure vs behaviour).
  * Reinterpretations from functional views into structure MUST respect the applicable `U.EpistemicRetargeting`/Bridge constraints (A.6.4). When combined with a concrete retargeting scheme (e.g. E.TGA structural retargeting, CC‑TGA‑06‑EX), that scheme’s additional rules also apply.

* **SoTA echo (informative).** `VP.ModuleInterface` matches the structural, implementation, and deployment families that dominate SoTA architecture descriptions: development and physical views in 4+1, construction and deployment viewpoints in IoT reference architectures, logical and physical architecture layers in UAF, NAF, and RASDS-style frameworks, and structural and interface-focused models in SysML-based MBSE. TEVB treats all of these as specialisations of a single holonic “modules and interfaces” viewpoint.

### E.17.2:5 - Archetypal grounding  *(informative)*

A minimal TEVB instantiation looks as follows:

```
TEVB.EngBundle :
  U.ViewpointBundle {
    viewFamilyId   = VF.TEVB.ENG
    EntityOfConcernClassSpec   = { h : U.Holon | HolonKind(h) ∈ {System, Episteme} }
    viewpoints     = { VP.Functional, VP.Procedural, VP.RoleEnactor, VP.ModuleInterface }
    LibraryRef     = FPF.Core.Viewpoints
  }
```

Each `VP.*` viewpoint is a `U.Viewpoint` as in E.17.0, with:

* `viewpointId ∈ {VP.Functional, VP.Procedural, VP.RoleEnactor, VP.ModuleInterface}`,
* `EntityOfConcernClassSpec` inherited from `TEVB.EngBundle`,
* `StakeholderFamilies`, `Concerns`, `AllowedEpistemeKinds`, `ConformanceRules` aligned with the subsections above.

**Engineering holon (example).**

Let `Plant_X : U.System` be a production plant, and `ControlStack_X : U.Episteme` be its control and optimisation stack as a holon.

* Under `VP.Functional`, `Plant_X` is viewed as a bundle of capabilities and transductions: material/energy/product flows, optimisation functions, safety envelopes.
* Under `VP.Procedural`, `Plant_X` is viewed as sets of procedures and control sequences: startup/shutdown, normal operation, emergency handling.
* Under `VP.RoleEnactor`, `Plant_X` is viewed as networks of role‑enactors: human operators, controllers, subsystems enacting roles in SOPs and safety cases.
* Under `VP.ModuleInterface`, `Plant_X` is viewed as modules and interfaces: equipment units, pipelines, control modules, buses, and their interfaces and specifications.

Each of these is a **family of Description epistemes and specification-use cases** with `DescriptionContext = ⟨EntityOfConcernRef(Plant_X or ControlStack_X), BoundedContextRef, ViewpointRef=VP.*⟩` and TEVB ensures that E.TGA and MVPK can rely on this common structure.

### E.17.2:6 - Conformance checklist  *(normative)*

**CC‑TEVB‑1 (Bundle identity).**
Any artefact claiming to be “TEVB engineering viewpoints” MUST:

* refer to `viewFamilyId = VF.TEVB.ENG`,
* have `EntityOfConcernClassSpec = {h : U.Holon | HolonKind(h) ∈ {System, Episteme}}`,
* enumerate `viewpoints = {VP.Functional, VP.Procedural, VP.RoleEnactor, VP.ModuleInterface}` and no others.

**CC‑TEVB‑2 (Viewpoint definition).**
Each `VP.*` viewpoint MUST be a well‑formed `U.Viewpoint` per E.17.0:

* `viewpointId` equal to one of the four engineering IDs,
* `EntityOfConcernClassSpec` equal to the bundle’s,
* `StakeholderFamilies`, `Concerns`, `AllowedEpistemeKinds`, `ConformanceRules` explicitly declared.

**CC‑TEVB‑3 (DescriptionContext completeness).**
Every Description episteme or specification-use case participating in a TEVB‑managed multi‑view family for a holon MUST have a `DescriptionContext = ⟨EntityOfConcernRef, BoundedContextRef, ViewpointRef⟩` with:

* `EntityOfConcernRef` referencing a `U.System` or `U.Episteme`,
* `ViewpointRef ∈ {VP.Functional, VP.Procedural, VP.RoleEnactor, VP.ModuleInterface}`,
* `BoundedContextRef` pointing to the engineering context (E.10.D1).

Capability, Method, procedure/control, role-structure, structural-architecture, module, interface, and allocation terms in those descriptions are viewpoint concern/content unless the text explicitly declares an A.6.4 retargeting, KindBridge, and species-extension rule that changes `EntityOfConcernRef`.

**CC‑TEVB‑4 (Separation from PublicationVPs).**
`VP.*` identifiers from TEVB are engineering-viewpoint ids. They do not serve as MVPK publication-side viewpoint ids. Publication-side viewpoints live in MVPK and may **correspond** to TEVB engineering viewpoints through `CorrespondenceModel`, but they are separate symbols.

**CC‑TEVB‑5 (No Role coordinate in EntityOfConcern and Description-episteme boundary or specification use).**
TEVB-aligned descriptions and specification-use cases MAY reference `U.RoleEnactor` families in `StakeholderFamilies` but SHALL NOT add `Role` or `RoleEnactor` as characteristics in Description episteme or specification-use case signatures beyond what A.7 and E.10.D2 already provides. Role semantics stay in RoleEnactment patterns; TEVB just selects concerns.

**CC‑TEVB‑6 (Alignment with consumer viewpoint maps).**
When a pattern defines engineering viewpoint families named “Functional”, “Procedural”, “Role‑Enactor (Device‑Structure)”, or “Module‑Interface” over the same `EntityOfConcernClass` and claims TEVB alignment (for example, E.TGA E.18:5.12 viewpoint map), it MUST bind them to TEVB viewpoints as follows:

* “Functional” → `VP.Functional`,
* “Procedural” → `VP.Procedural`,
* “Role‑Enactor (Device‑Structure)” → `VP.RoleEnactor`,
* “Module‑Interface” → `VP.ModuleInterface`.

Any deviation MUST be explicitly documented as a species‑level extension and MUST NOT reuse `VF.TEVB.ENG`.

### E.17.2:7 - Rationale & SoTA echoing  *(informative)*

#### E.17.2:7.1 - NQD‑grounded choice of the core four

Part G’s NQD discipline treats candidate viewpoint families as points in an N/U/C/D quality space (Use‑Value, Constraint‑Fit, Novelty, Diversity_P). Applied to a SoTA‑harvested candidate set of engineering viewpoints (Functional, Behavioural/Procedural, Structural/Module, Allocation/Role, Information/Data, Assurance/Safety, Mission/Context, Deployment/Operational, Business/Usage), this yields a small Pareto frontier for *engineering holon* viewpoints. On that frontier, the `F–B–S+R` cut implemented by `{VP.Functional, VP.Procedural, VP.RoleEnactor, VP.ModuleInterface}` is the minimal set that:
* spans the Function-Behaviour-Structure ontology used in contemporary design theory while adding an explicit allocation/responsibility concern;
* aligns with the “functional”, “process”, “structural”, and “deployment” clusters recurrent in standards and architecture frameworks;
* stays neutral with respect to domain‑specific qualities (`‑ilities`) and business/mission framing, which are captured in separate Q‑Bundles and governance-oriented viewpoint bundles rather than in TEVB itself.

Other candidates (e.g. dedicated information, assurance, or mission viewpoints) remain important but either duplicate concerns already captured by TEVB (when specialised to engineering holons) or are better modelled as orthogonal quality bundles (C.25) or non-engineering viewpoint bundles (business and governance viewpoint bundles). TEVB therefore pins only the core four and leaves the rest to specialised families.

#### E.17.2:7.2 - Alignment with post‑2015 engineering practice

* Modern architecture standards built on ISO/IEC/IEEE 42010 describe viewpoint libraries in which functional, behavioural/process, structural/deployment, and business/usage concerns are the dominant clusters; sector RAs such as IoT RA 30141 and space‑domain RAs provide explicit functional and construction/implementation viewpoints alongside business/usage and trustworthiness viewpoints. TEVB reuses the functional and construction/structural clusters as `VP.Functional` and `VP.ModuleInterface`, while treating business and trustworthiness as separate bundles.
* Model-based systems engineering practice (INCOSE MBSE guidance, SysML v2 “views-as-queries”, UAF/NAF view grids) converges on a small set of core diagram families: structure vs behaviour vs allocation/responsibility vs requirements/mission. TEVB’s `VP.Procedural` and `VP.RoleEnactor` correspond to the behaviour and allocation/responsibility concerns, respectively, and are designed to be notation-neutral over SysML/UAF/UML/Capella-style models.
* The FBS family of design ontologies (Function–Behaviour–Structure and extensions) provides a widely used conceptual source for separating what a system is for, what it does over time, and what it consists of. TEVB’s four viewpoints intentionally implement an FBS+R split at the holon level: `VP.Functional` ≈ Function, `VP.Procedural` ≈ Behaviour, `VP.ModuleInterface` ≈ Structure, with `VP.RoleEnactor` capturing the explicit mapping from functions/behaviours to role‑enacting carriers.
* Within FPF itself, E.TGA’s “viewpoint families” (Functional, Procedural, Role-Enactor or Device-Structure, Module-Interface, plus assurance, interoperability, data, operational, and mission aliases) are harmonised by letting the **core four** be TEVB viewpoints and treating the rest as lexical or bundle-level overlays, not as new kernel viewpoints.

#### E.17.2:7.3 - Why TEVB stays small

TEVB is deliberately *not* a complete architecture framework. It gives FPF a stable, holon‑centred engineering bundle that:
* is small enough to keep in working memory and to govern via EpistemeSlotGraph discipline;
* is expressive enough to represent mappings from SoTA architecture frameworks (4+1, domain‑specific RAs, UAF/NAF grids, SysML‑based MBSE method kits);
* can be safely combined with additional `U.ViewpointBundle` species (safety/assurance packs, business/mission packs, information/data packs) without mutating the core four;
* sits conceptually **below** architecture‑specific viewpoint libraries, which are introduced as separate `U.ViewpointBundle` species layering TEVB with mission/quality/business viewpoints instead of redefining TEVB.

As SoTA evolves, new bundles can be added or TEVB can gain a new edition with a revised NQD‑frontier, but the TEVB‑A edition fixed here remains the archetypal engineering bundle for holons.

### E.17.2:8 - Relations  *(informative)*

* **Builds on.** E.17.0 (`U.MultiViewDescribing`), E.17.1 (`U.ViewpointBundleLibrary`), A.7 and E.10.D2 (EntityOfConcern and Description-episteme boundary plus specification use), C.2.1 (EpistemeSlotGraph), A.6.2-A.6.4 (episteme morphisms).
* **Constrains.** E.18:5.12 (E.TGA viewpoint map), engineering description and specification-use patterns, MVPK engineering publication profiles.
* **Coordinates with.** MVPK publication face, publication form, publication unit, and publication carrier discipline; F-R family (Role, RoleDescription, RoleSpec); F.18 (naming discipline for ViewFamilyId, ViewpointId, EngineeringVPId, and publication-side viewpoint ids).
* **Non‑goals.** TEVB does not prescribe modelling notations (SysML, BPMN, IEC 61131‑3, etc.), storage formats, or tool APIs. It only fixes the **conceptual viewpoint bundle** that such tools must respect when claiming FPF alignment.

### E.17.2:End

