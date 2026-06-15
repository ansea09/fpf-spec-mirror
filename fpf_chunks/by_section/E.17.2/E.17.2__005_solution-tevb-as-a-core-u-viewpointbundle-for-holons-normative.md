---
chunk_kind: "child"
pattern_id: "E.17.2"
pattern_title: "TEVB — Typical Engineering Viewpoints Bundle"
section_id: "E.17.2:4"
section_title: "Solution — TEVB as a core U.ViewpointBundle for holons  (normative)"
source_path: "FPF-Spec.md"
output_path: "by_section/E.17.2/E.17.2__005_solution-tevb-as-a-core-u-viewpointbundle-for-holons-normative.md"
commit_sha: "c092a1f2299d88d42db012f3184aeff205c13219"
heading_path:
  - "E.17.2 — TEVB — Typical Engineering Viewpoints Bundle"
  - "E.17.2:4 — Solution — TEVB as a core U.ViewpointBundle for holons  (normative)"
line_start: 64741
line_end: 64980
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

  That is, TEVB applies to holons that are either `U.System` or `U.Episteme`. Other holon kinds MAY be added by species patterns but MUST be justified and documented; the default conformance rule set assumes systems and epistemes.

* **Library placement.**

  TEVB is registered in the core viewpoint library:

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

  > **Note.** Other ViewFamilyId values used in the `E.18` transformation-flow viewpoint-family map (e.g., *Assurance‑Oriented*, *Interoperability‑Oriented*, *Information/Data‑Oriented*, *Operational/Deployment*, *Mission/Context*) remain **lexical families only** for transformation-flow species (E.18:5.12). They do not add viewpoints to TEVB; they are orthogonal to TEVB’s `viewpoints` set.

#### E.17.2:4.2 - TEVB engineering viewpoints

Each TEVB viewpoint is a `U.Viewpoint` with:
* `viewpointId : ViewpointId` (concrete identifier, e.g., `VP.Functional`);
* `EntityOfConcernClassSpec` **inherited from the bundle** (`U.Holon` with `System`/`Episteme` kinds);
* `StakeholderFamilies : FinSet(RoleEnactorFamilyId)` — families of `U.RoleEnactor` that are the primary audience;
* `Concerns : FinSet(ConcernId)` — engineering concerns this viewpoint foregrounds;
* `AllowedEpistemeKinds : FinSet(U.EpistemeKindRef)` — Description-episteme and specification-use kinds admissible under this viewpoint (all obeying EntityOfConcern and Description-episteme boundary, specification use, and C.2.1 slot disciplines);
* `ConformanceRules : FinSet(RuleId)` — references to checklist items in conformance packs (CV/GF/engineering checklists).

The subsections below fix the **normative intent and minimal field sets** for each TEVB viewpoint. Species patterns and discipline‑packs may refine `Concerns`, `AllowedEpistemeKinds` and `ConformanceRules`, but MUST preserve the intent.

##### E.17.2:4.2.1 - `VP.Functional` - functional behavior and capability viewpoint

**Intent.** Look at a holon in terms of what it is required or able to do: capabilities, functional behaviors, required transformations or effects, and functional responsibilities. A functional behavior is grounded as `U.Transformation` when the claim is one bounded required change or effect, and as `TransformationFlowStructure` when the behavior is a compound structure of transformations. This viewpoint is not a module view and does not mint `U.Function`.

* **viewpointId.**

  ```
  VP.Functional : ViewpointId  // EngineeringVPId
  ```

* **EntityOfConcernClassSpec.**
  Same as the bundle: `U.Holon` with `System`/`Episteme` kinds.

* **StakeholderFamilies (typical examples).**
  Actual `StakeholderFamilies : FinSet(U.RoleEnactor)` values are defined in RoleEnactment discipline packs; labels below are informal.
  * System engineering leads and architects (e.g. SysEng-lead enactors).
  * Product owners / capability owners.
  * Reliability / performance engineers when reading capability envelopes.

* **Concerns (typical).**
  * Functional behavior: required `U.Transformation` or `TransformationFlowStructure` under conditions.
  * Capabilities and envelopes provided by the holon (`CapabilityConcerns`).
  * Functioning status: required, possible, intended, observed, degraded, or blocked behavior.
  * Input/output or functional-port signatures where accepted or produced states, flows, media, signals, information, work products, or formal objects matter.
  * Compositional semantics of functional behavior in transformation-flow structures.

* **AllowedEpistemeKinds (shape).**
  `VP.Functional` admits Description epistemes and specification-use Description epistemes whose **EntityOfConcernSlot** remains the holon and whose viewpoint content foregrounds the holon's functional behavior, capability, `FunctionalElement@Context`, or transformation-flow relation, e.g.:
  * `SystemFunctionalDescription`, `SystemFunctionalSpec` describing system-level capabilities, functional behavior, and interconnection.
  * `FunctionalElementDescription`, `FunctionalElementSpec` when a `FunctionalElement@Context` locus with behavior, bearer, ports, capability, and allocation is current.
  * `TransformationBehaviorDescription`, `TransformationBehaviorSpec` when the behavior is a bounded `U.Transformation` or selected `TransformationFlowStructure`.
  * `ServiceCapabilityDescription`, `ServiceCapabilitySpec` when a holon is in Service role.

  All such epistemes satisfy these admissibility checks:
  * obey EntityOfConcern and Description-episteme boundary plus specification-use discipline: `...Description` names a Description episteme about the holon and `...Spec` names specification-use of that Description episteme for declared functional behavior, capability, method, mechanism, port, or promise content;
  * make their `DescriptionContext = <EntityOfConcernRef, BoundedContextRef, ViewpointRef>` explicit, with `ViewpointRef = VP.Functional`;
  * use `A.3.4 FunctioningRef?`, `TransformerRef?`, `InputConditionOrPortRefs?`, and `OutputConditionOrPortRefs?` when the functional-view claim depends on bounded transformation, bearer, input/output boundary, or flow location.

* **ConformanceRules (examples).**
  * Functional behavior is grounded as `U.Transformation` or `TransformationFlowStructure` before function wording carries a claim.
  * `FunctionalElement@Context` remains a functional-view locus, not a module and not `U.Function`.
  * Functional ports/signatures are separated from module interfaces unless an A.6.M module-interface claim is current.
  * When functional views participate in retargeting patterns, they satisfy the relevant A.6.4 retargeting constraints; concrete consumer patterns such as E.18 may impose additional rules.

* **SoTA echo (informative).** `VP.Functional` corresponds to functional views in ISO-aligned architecture descriptions, domain reference architectures, FBS-style design ontologies, SysML/SysML-v2 capability and logical architecture models, and logical view slices in 4+1-style frameworks once recast into holon, capability, functional-behavior, and transformation terms.

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

##### E.17.2:4.2.3 - `VP.RoleEnactor` - role, bearer, and device-structure viewpoint

**Intent.** Look at a holon in terms of who or what bears roles, responsibilities, and functional enactment. This viewpoint covers socio-technical role assignments and device/system-side readings of source-local transformation-flow descriptions. When a source-local device or transformer cue names the system that performs or sustains a transformation, recover it as `U.System` or candidate system bearing `TransformerRole@Context`, coordinated with `A.3.4 TransformerRef?`.

* **viewpointId.**

  ```
  VP.RoleEnactor : ViewpointId  // EngineeringVPId
  ```

* **EntityOfConcernClassSpec.**

  Same as the bundle.

* **StakeholderFamilies (typical).**
  * Organisational designers and operations managers (`OrgDesignEnactorFamily`).
  * Safety and compliance officers concerned with separation of duties (`SegregationOfDutyEnactorFamily`).
  * Hardware/system engineers concerned with which devices or systems carry which functional behaviors (`DeviceEngineerEnactorFamily`).

* **Concerns (typical).**
  * Which holons enact which roles under which contexts (`RoleEnactmentConcerns`).
  * Which systems or candidate systems fill `TransformerRef?` for transformations or functioning.
  * Allocation of capabilities to devices, systems, subsystems, organizations, scripts, instruments, or manufacturing cells (`CapabilityAllocationConcerns`).
  * Organisational constraints: segregation of duties, responsibilities, escalation relations (`GovernanceConcerns`).
  * Device-view readings of functional transformation-flow descriptions, with source-local device or transformer vocabulary treated as source cue rather than durable FPF kind.

* **AllowedEpistemeKinds (shape).**
  `VP.RoleEnactor` admits Description epistemes and specification-use Description epistemes where the **EntityOfConcernSlot** remains the holon and the viewpoint content foregrounds role structure, role enactment, bearer/transformer locus, or capability allocation associated with that holon, e.g.:
  * `RoleDescription`, `RoleSpec` for human, organization, system, or device roles.
  * `RoleEnactmentDescription` for mappings `Holder#Role:Context` under A.15.
  * `TransformerBearerDescription` for `U.System bearing TransformerRole@Context` around an A.3.4 transformation.
  * `DeviceAllocationDescription` mapping functional behavior to physical, organizational, or software systems.

  As with other TEVB viewpoints, these are Description epistemes and specification-use cases with `DescriptionContext.ViewpointRef = VP.RoleEnactor`.

* **ConformanceRules (examples).**
  * Role vs method vs work vs capability separation is upheld through A.7 and A.15.
  * A bearer/role-enactor claim uses `U.RoleAssignment` when role assignment, work, responsibility, or capability is current; it does not infer performed work.
  * Device-view reinterpretation from functional flows is expressed as `U.EpistemicRetargeting` with an explicit `KindBridge` witness when the `EntityOfConcernRef` changes.
  * No "role as behavior" conflation: roles and bearer loci stay separate from methods, work, and bounded transformations.

* **SoTA echo (informative).** `VP.RoleEnactor` aligns with allocation/responsibility and resource/organizational view clusters in MBSE frameworks, allocation views in UAF/NAF, role-responsibility matrices and RACI-style artefacts, and who/what-enacts-which-role slices in usage and operational viewpoints.

##### E.17.2:4.2.4 - `VP.ModuleInterface` - module and interface viewpoint

**Intent.** Look at a holon in terms of modules, interfaces, and structural composition: what parts exist, how they connect, and how interface specifications, substitutability, compatibility, and change policies are stated. This viewpoint is distinct from `VP.Functional`: a module may realize many functional elements, many modules may realize one functional element, a functional element may be abstract before allocation, and a module may have no current functional behavior in the functional view.

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
  * Interface specifications: protocols, schemas, physical connectors, APIs, version/change policies, conformance expectations (`InterfaceConcerns`).
  * Dependency structures and allowed couplings (`DependencyConcerns`).
  * Replaceability and variation points (`VariabilityConcerns`).
  * Correspondence or allocation between modules and functional elements without identity by default.

* **AllowedEpistemeKinds (shape).**
  `VP.ModuleInterface` admits Description epistemes and specification-use Description epistemes where the **EntityOfConcernSlot** remains the holon and the viewpoint content foregrounds the holon's structural architecture, modules, interfaces, and connector arrangements, e.g.:
  * `SystemStructureDescription`, `SystemStructureSpec` for module/connector descriptions.
  * `ModuleInterfaceDescription`, `ModuleInterfaceSpec` for signature, interface specifications, physical interface definitions, and conformance expectations.
  * `ModuleFunctionalAllocationDescription` when module-interface structure is being related to `FunctionalElement@Context` or `FunctionalStructureView@Context` through correspondence or allocation.

  These epistemes describe holon structure, module-interface arrangement, ports/connectors, or structural architecture as viewpoint content about the holon rather than replacing the holon as the `EntityOfConcern`. Functional-to-module reinterpretations between `VP.Functional` and `VP.ModuleInterface` use declared correspondence/allocation or `U.EpistemicRetargeting` + `KindBridge` when the `EntityOfConcernRef` changes.

* **ConformanceRules (examples).**
  * Interfaces are typed and explicitly bound to standards or signature declarations where applicable (`A.6.0`, `A.6.M`, A.6.5).
  * Functional ports are not treated as module interfaces unless the module-interface or substitutability claim is current.
  * No inlining of methods, work, or functional behavior into module structure; use A.3.4/A.6.F/A.15 for those claims.
  * Reinterpretations from functional views into structure respect the applicable `U.EpistemicRetargeting`/Bridge constraints.

* **SoTA echo (informative).** `VP.ModuleInterface` matches structural, implementation, construction, deployment, and interface-focused families in architecture descriptions, IoT and space reference architectures, UAF, NAF, RASDS, SysML-based MBSE, and 4+1 development/physical views, while keeping functional behavior and module-interface claims distinct.

