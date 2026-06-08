---
chunk_kind: "child"
pattern_id: "E.17.2"
pattern_title: "TEVB — Typical Engineering Viewpoints Bundle"
section_id: "E.17.2:4"
section_title: "Solution — TEVB as a core U.ViewpointBundle for holons  (normative)"
source_path: "FPF-Spec.md"
output_path: "by_section/E.17.2/E.17.2__005_solution-tevb-as-a-core-u-viewpointbundle-for-holons-normative.md"
commit_sha: "21e2101c100964de121c37408b37563ee0cdbf8c"
heading_path:
  - "E.17.2 — TEVB — Typical Engineering Viewpoints Bundle"
  - "E.17.2:4 — Solution — TEVB as a core U.ViewpointBundle for holons  (normative)"
line_start: 62957
line_end: 63187
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

