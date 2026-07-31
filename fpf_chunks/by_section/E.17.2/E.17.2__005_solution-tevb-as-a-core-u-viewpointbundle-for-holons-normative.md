---
chunk_kind: "child"
pattern_id: "E.17.2"
pattern_title: "TEVB - Typical Engineering Viewpoints Bundle"
section_id: "E.17.2:4"
section_title: "Solution — TEVB as a core U.ViewpointBundle for holons  (normative)"
source_path: "FPF-Spec.md"
output_path: "by_section/E.17.2/E.17.2__005_solution-tevb-as-a-core-u-viewpointbundle-for-holons-normative.md"
commit_sha: "373c87917e92123cfa039e24c42a1f122b54fb66"
heading_path:
  - "E.17.2 — TEVB - Typical Engineering Viewpoints Bundle"
  - "E.17.2:4 — Solution — TEVB as a core U.ViewpointBundle for holons  (normative)"
line_start: 78640
line_end: 78879
dependencies:
  - "A.1"
  - "A.15"
  - "A.2"
  - "A.2.1"
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

  That is, TEVB applies to holons that are either `U.System` or `U.Episteme`. Other holon kinds may be added by species patterns but must be justified and documented; the default conformance rule set assumes systems and epistemes.

* **Library placement.**

  TEVB is registered in the core viewpoint library:

  ```
  TEVB.Library : U.ViewpointBundleLibrary
  TEVB.Library.libraryId = FPF.Core.Viewpoints
  TEVB.Library.bundles ⊇ { TEVB.EngBundle }
  ```

  Additional organisational libraries may import and specialise TEVB, but must not redefine `VF.TEVB.ENG` with incompatible semantics.

* **Viewpoint set.**

  TEVB defines a **finite set of canonical engineering viewpoints**:

  ```
  TEVB.EngBundle.viewpoints =
    { VP.Functional, VP.Procedural, VP.AllocationResponsibility, VP.ModuleInterface }
  ```

The selection `{VP.Functional, VP.Procedural, VP.AllocationResponsibility, VP.ModuleInterface}` is the current **NQD-frontier** for engineering holon viewpoints in Part G: it realises a Function-Behaviour-Structure-plus-responsibility (`F-B-S+R`) cut that is non-dominated against candidate families including explicit information or data, assurance or safety, and mission or context viewpoints under the N, U, C, and D characteristics (C.18, G.0). Part G records the SoTA candidate set and rejected alternatives; TEVB only fixes the **core four** where each `VP.* : U.Viewpoint` is defined below. These four are the **only** viewpoints in the core TEVB bundle.

  > **Note.** Other ViewFamilyId values used in the `E.18` transformation-flow viewpoint-family map (for example, assurance-oriented, interoperability-oriented, information-oriented or data-oriented, operational-oriented or deployment-oriented, and mission-oriented or context-oriented labels) remain **lexical families only** for transformation-flow species (E.18:5.12). They do not add viewpoints to TEVB; they are orthogonal to TEVB's `viewpoints` set.

#### E.17.2:4.2 - TEVB engineering viewpoints

Each TEVB viewpoint is a `U.Viewpoint` with:
* `viewpointId : ViewpointId` (concrete identifier, e.g., `VP.Functional`);
* `EntityOfConcernClassSpec` **inherited from the bundle** (`U.Holon` with `System`/`Episteme` kinds);
* `StakeholderFamilies : FinSet(StakeholderFamilyId)` — audience or stakeholder families that are primary readers or concern holders for the viewpoint. These are viewpoint-context values, not work-facing role-assignment values or allocation-responsibility root kinds.
* `Concerns : FinSet(ConcernId)` — engineering concerns this viewpoint foregrounds;
* `AllowedEpistemeKinds : FinSet(U.EpistemeKindRef)` — Description-episteme and specification-use kinds admissible under this viewpoint (all obeying EntityOfConcern and Description-episteme boundary, specification use, and C.2.1 slot disciplines);
* `ConformanceRules : FinSet(RuleId)` — references to checklist items in conformance packs (CV, GF, and engineering checklists).

The subsections below fix the **normative intent and minimal field sets** for each TEVB viewpoint. Species patterns and discipline‑packs may refine `Concerns`, `AllowedEpistemeKinds` and `ConformanceRules`, but must preserve the intent.

##### E.17.2:4.2.1 - `VP.Functional` - functional behavior and capability viewpoint

**Intent.** Look at a holon in terms of what it is required or able to do: capabilities, functional behaviors, and required transformations or effects. If responsibility for those requirements is current, express that responsibility through `VP.AllocationResponsibility` and the work-facing role-assignment patterns rather than making responsibility a functional-viewpoint coordinate. A functional behavior is grounded as `U.Transformation` when the claim is one bounded required change or effect, and as `TransformationFlowStructure` when the behavior is a compound structure of transformations. This viewpoint is not a module view and does not mint `U.Function`.

* **viewpointId.**

  ```
  VP.Functional : ViewpointId  // EngineeringVPId
  ```

* **EntityOfConcernClassSpec.**
  Same as the bundle: `U.Holon` with `System`/`Episteme` kinds.

* **StakeholderFamilies (typical examples).**
  Actual `StakeholderFamilies : FinSet(StakeholderFamilyId)` values are local audience or stakeholder-family refs; labels below are informal and do not create role assignments.
  * System engineering leads and architects (e.g. SysEng-lead enactors).
  * Product owners / capability owners.
  * Reliability / performance engineers when reading capability envelopes.

* **Concerns (typical).**
  * Functional behavior: required `U.Transformation` or `TransformationFlowStructure` under conditions.
  * Capabilities and envelopes provided by the holon (`CapabilityConcerns`).
  * Functioning status: required, possible, intended, observed, degraded, or blocked behavior.
  * Input-and-output signatures or functional-port signatures where accepted or produced states, flows, media, signals, information, work products, or formal objects matter.
  * Compositional semantics of functional behavior in transformation-flow structures.

* **AllowedEpistemeKinds (shape).**
  `VP.Functional` admits Description epistemes and specification-use Description epistemes whose **EntityOfConcernSlot** remains the holon and whose viewpoint content foregrounds the holon's functional behavior, capability, `FunctionalElement@Context`, or transformation-flow relation, e.g.:
  * `SystemFunctionalDescription`, `SystemFunctionalSpec` describing system-level capabilities, functional behavior, and interconnection.
  * `FunctionalElementDescription`, `FunctionalElementSpec` when a `FunctionalElement@Context` locus with behavior, bearer, ports, capability, and allocation is current.
  * `TransformationBehaviorDescription`, `TransformationBehaviorSpec` when the behavior is a bounded `U.Transformation` or selected `TransformationFlowStructure`.
  * `ServiceCapabilityDescription`, `ServiceCapabilitySpec` when the functional viewpoint foregrounds service-facing capability, promise content, delivery work, access point, delivery system, or API/publication description; use current `U.RoleAssignment` only if a work-facing role value is actually assigned for service delivery or service operation.

  All such epistemes satisfy these admissibility checks:
  * obey EntityOfConcern and Description-episteme boundary plus specification-use discipline: `...Description` names a Description episteme about the holon and `...Spec` names specification-use of that Description episteme for declared functional behavior, capability, method, mechanism, port, or promise content;
  * make their `DescriptionContext = <EntityOfConcernRef, BoundedContextRef, ViewpointRef>` explicit, with `ViewpointRef = VP.Functional`;
  * use `A.3.4 FunctioningRef?`, `TransformerRef?`, `InputConditionOrPortRefs?`, and `OutputConditionOrPortRefs?` when the functional-view claim depends on bounded transformation, bearer, input and output boundary, or flow location.

* **ConformanceRules (examples).**
  * Functional behavior is grounded as `U.Transformation` or `TransformationFlowStructure` before function wording carries a claim.
  * `FunctionalElement@Context` remains a functional-view locus, not a module and not `U.Function`.
  * Functional ports and signatures are separated from module interfaces unless an A.6.M module-interface claim is current.
  * When functional views participate in retargeting patterns, they satisfy the relevant A.6.4 retargeting constraints; concrete consumer patterns such as E.18 may impose additional rules.

* **SoTA echo (informative).** `VP.Functional` corresponds to functional views in ISO-aligned architecture descriptions, domain reference architectures, FBS-style design ontologies, SysML and SysML v2 capability and logical architecture models, and logical view slices in 4+1-style frameworks once recast into holon, capability, functional-behavior, and transformation terms.

##### E.17.2:4.2.2 - `VP.Procedural` — process & control viewpoint

**Intent.** Look at a holon in terms of **how behaviours are sequenced and controlled**: method-description structures, state machines, operational procedures, and control logic.

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
  * `ControlLogicDescription`, `ControlLogicSpec` (IEC 61131‑3 style step diagrams and statecharts).
  * `WorkflowDescription`, `WorkflowSpec` (business processes, orchestration logic).

  These epistemes:
  * respect the **order discipline** (Γ_method, Γ_ctx) and A.15 (Role–Method–Work alignment);
  * carry E.10.D2-conformant DescriptionContext with `ViewpointRef = VP.Procedural`.

* **ConformanceRules (examples).**
  * Preconditions and postconditions at step boundaries are explicit and type-checked. Use `A.3.1` for the method as semantic way of doing, `A.3.2` for the method description, and `Gamma_method` only as notation over the recovered method claim.
  * No embedding of Work or calendars inside procedural descriptions (A.7 and E.10.D2).
  * Failure modes and recovery actions are declared and traceable to safety analyses (F.15 harnesses where relevant).

* **SoTA echo (informative).** `VP.Procedural` captures the dynamic and process dimension found in SoTA architecture and MBSE practice: process views in 4+1, operational and behavioural views in defence and enterprise frameworks, behaviour diagrams in SysML (activity, sequence, state, interaction), and procedure-oriented and control-logic-oriented models in industrial standards. TEVB abstracts this into a notation‑agnostic “behaviour over time” viewpoint for holons.

##### E.17.2:4.2.3 - `VP.AllocationResponsibility` - allocation, responsibility, and device-structure viewpoint

**Intent.** Look at a holon in terms of which system or acting holon bears work-facing roles, responsibilities, role assignments, capability allocation, or device-side or system-side responsibility for functional behavior. The viewpoint id `VP.AllocationResponsibility` is an engineering viewpoint id, not a new root kind. When a source-local device or transformer cue names the system that performs or sustains a transformation, recover it as `U.System` or candidate system with a work-facing role assignment such as `TransformerRole@Context`, coordinated with `A.3.4 TransformerRef?`.

* **viewpointId.**

  ```
  VP.AllocationResponsibility : ViewpointId  // EngineeringVPId
  ```

* **EntityOfConcernClassSpec.**

  Same as the bundle.

* **StakeholderFamilies (typical).**
  * Organisational designers and operations managers (`OrgDesignEnactorFamily`).
  * Safety and compliance officers concerned with separation of duties (`SegregationOfDutyEnactorFamily`).
  * Hardware and system engineers concerned with which devices or systems carry which functional behaviors (`DeviceEngineerEnactorFamily`).

* **Concerns (typical).**
  * Which systems or acting holons hold which work-facing roles under which contexts (`RoleAssignmentConcerns`).
  * Which systems or candidate systems fill `TransformerRef?` for transformations or functioning.
  * Allocation of capabilities to devices, systems, subsystems, organizations, scripts, instruments, or manufacturing cells (`CapabilityAllocationConcerns`).
  * Organisational constraints: segregation of duties, responsibilities, escalation relations (`GovernanceConcerns`).
  * Device-view readings of functional transformation-flow descriptions, with source-local device or transformer vocabulary treated as source cue rather than durable FPF kind.

* **AllowedEpistemeKinds (shape).**
  `VP.AllocationResponsibility` admits Description epistemes and specification-use Description epistemes where the **EntityOfConcernSlot** remains the holon and the viewpoint content foregrounds work-facing role values, role assignments, responsibility structure, holder or allocated-holon locus, transformer relation, or capability allocation associated with that holon, e.g.:
  * `RoleDescription`, `RoleSpec` for human, organization, system, or device roles.
  * `RoleAssignmentDescription` for mappings from holder, role value, bounded context, and current window under A.2.1 and A.15.
  * `TransformerRoleAssignmentDescription` for a holder, role value, bounded context, current window, and A.3.4 transformation connected through current `U.RoleAssignment`, not through compact holder-role shorthand.
  * `DeviceAllocationDescription` mapping functional behavior to physical, organizational, or software systems.

  As with other TEVB viewpoints, these are Description epistemes and specification-use cases with `DescriptionContext.ViewpointRef = VP.AllocationResponsibility`.

* **ConformanceRules (examples).**
  * Role vs method vs work vs capability separation is upheld through A.7 and A.15.
  * A role-assignment or responsibility claim uses `U.RoleAssignment` when role assignment, work, responsibility, or capability is current; it does not infer performed work.
  * Device-view reinterpretation from functional flows is expressed as `U.EpistemicRetargeting` with an explicit `KindBridge` witness when the `EntityOfConcernRef` changes.
  * No "role as behavior" conflation: roles and bearer loci stay separate from methods, work, and bounded transformations.

* **SoTA echo (informative).** `VP.AllocationResponsibility` aligns with allocation and responsibility and resource and organizational view clusters in MBSE frameworks, allocation views in UAF/NAF, role-responsibility matrices and RACI-style artefacts, and role-assignment/responsibility slices in usage and operational viewpoints.

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
  * Interface specifications: protocols, schemas, physical connectors, APIs, version and change policies, conformance expectations (`InterfaceConcerns`).
  * Dependency structures and allowed couplings (`DependencyConcerns`).
  * Replaceability and variation points (`VariabilityConcerns`).
  * Correspondence or allocation between modules and functional elements without identity by default.

* **AllowedEpistemeKinds (shape).**
  `VP.ModuleInterface` admits Description epistemes and specification-use Description epistemes where the **EntityOfConcernSlot** remains the holon and the viewpoint content foregrounds the holon's structural architecture, modules, interfaces, and connector arrangements, e.g.:
  * `SystemStructureDescription`, `SystemStructureSpec` for module and connector descriptions.
  * `ModuleInterfaceDescription`, `ModuleInterfaceSpec` for signature, interface specifications, physical interface definitions, and conformance expectations.
  * `ModuleFunctionalAllocationDescription` when module-interface structure is being related to `FunctionalElement@Context` or `FunctionalStructureView@Context` through correspondence or allocation.

  These epistemes describe holon structure, module-interface arrangement, ports and connectors, or structural architecture as viewpoint content about the holon rather than replacing the holon as the `EntityOfConcern`. Functional-to-module reinterpretations between `VP.Functional` and `VP.ModuleInterface` use declared correspondence or allocation or `U.EpistemicRetargeting` + `KindBridge` when the `EntityOfConcernRef` changes.

* **ConformanceRules (examples).**
  * Interfaces are typed and explicitly bound to standards or signature declarations where applicable (`A.6.0`, `A.6.M`, A.6.5).
  * Functional ports are not treated as module interfaces unless the module-interface or substitutability claim is current.
  * No inlining of methods, work, or functional behavior into module structure. Use `A.3.4` for transformation claims, `A.6.F` for function-allocation claims, and `A.15` for work and role-method-work alignment claims.
  * Reinterpretations from functional views into structure respect the applicable `U.EpistemicRetargeting`/Bridge constraints.

* **SoTA echo (informative).** `VP.ModuleInterface` matches structural, implementation, construction, deployment, and interface-focused families in architecture descriptions, IoT and space reference architectures, UAF, NAF, RASDS, SysML-based MBSE, and 4+1 development and physical views, while keeping functional behavior and module-interface claims distinct.

