---
chunk_kind: "child"
pattern_id: "G.0"
pattern_title: "Define Admissible Comparison and Aggregation for a Frame (CG-Spec)"
section_id: "G.0:4"
section_title: "Solution — CG‑Spec as the design-time legality gate"
source_path: "FPF-Spec.md"
output_path: "by_section/G.0/G.0__005_solution-cg-spec-as-the-design-time-legality-gate.md"
commit_sha: "e307edbd91c04c1d85661bd309b9944fac251937"
heading_path:
  - "G.0 — Define Admissible Comparison and Aggregation for a Frame (CG-Spec)"
  - "G.0:4 — Solution — CG‑Spec as the design-time legality gate"
line_start: 126882
line_end: 127100
dependencies:
  - "A.10"
  - "A.17"
  - "A.18"
  - "A.19"
  - "A.19.CN"
  - "B.3"
  - "C.16"
  - "C.18"
  - "C.19"
  - "C.23"
  - "E.10"
  - "E.5"
  - "E.5.2"
  - "F.9"
  - "G.1"
  - "G.2"
  - "G.3"
  - "G.4"
  - "G.5"
  - "G.6"
  - "G.7"
  - "G.Core"
keywords:
  - "CG-Frame"
  - "CG-Spec"
  - "CL-routing"
  - "ComparatorSet"
  - "MinimalEvidence"
  - "RSCRTriggerKindId"
  - "ReferencePlane"
  - "ScaleComplianceProfile (SCP)"
  - "admissible comparison and aggregation"
  - "edition pins"
  - "evidence requirements"
  - "Γ-fold"
  - "Φ(CL)"
  - "Φ_plane"
---

### G.0:4 - Solution — CG‑Spec as the design-time legality gate

`CG‑Spec` is a **notation-independent** UTS-published object that, for a given `CG‑Frame`, defines:

* the **ComparatorSet** (explicit, finite, typed) permitted in this frame,
* the **ScaleComplianceProfile** (SCP) that constrains lawful operations per characteristic,
* **MinimalEvidence** requirements per characteristic (lanes, carriers, any applicable freshness windows or crossing conditions, and failure behavior),
* the frame’s **penalty and trust folding wiring** (by explicit policy ids and edition pins),
* **AcceptanceStubs** as design-time templates (thresholds remain governed by CAL, not by CG‑Spec),
* optional method-family hooks (e.g., illumination/QD or explore↔exploit guards) *as wiring only*, with semantics governed by the corresponding patterns.

`CG‑Spec` constrains downstream gate checks by being *referenced and pinned*; it is not itself an admissibility mechanism.

#### G.0:4.1 - G.Core linkage (normative)

**Builds on:** `G.Core` (Part-G core invariants; governing-pattern citation)

**GCoreLinkageManifest (normative).**

Effective obligations/pins/triggers are computed by union expansion of the referenced ids (per `G.Core:4.2`).
Profiles/sets + explicit deltas; `Nil‑elision` applies.

* `CoreConformanceProfileIds :=`
  * `GCoreConformanceProfileId.PartG.AuthoringBase`
  * `GCoreConformanceProfileId.PartG.TriStateGuard`
  * `GCoreConformanceProfileId.PartG.UTSWhenPublicIdsMinted`
* `CorePinSetIds :=`
  * `GCorePinSetId.PartG.AuthoringMinimal`
  * `GCorePinSetId.PartG.CrossingVisibilityPins`
* `CorePinsRequired :=` *(delta over PinSets)*
  * `UTSRowId[]`
  * `ReferenceMap`
  * `ComparatorSetRef.edition`
  * `SCPRef.edition`
  * `ΓFoldRef.edition?`
  * `MinimalEvidenceRef.edition?`
  * `FailureBehaviorPolicyId?`
* `DefaultsConsumed := {DefaultId.GammaFoldForR_eff}` *(governing definition: `CC‑G5.4` per `G.Core.DefaultGoverningDefinitionIndex`)*
* `RSCRTriggerSetIds := {GCoreTriggerSetId.CGSpecGate}`
* `RSCRTriggerKindIds :=` *(delta over TriggerSets)*
  * `RSCRTriggerKindId.EvidenceSurfaceEdit`
  * `RSCRTriggerKindId.TokenizationOrNameChange`
  * `RSCRTriggerKindId.DefaultGoverningDefinitionChange`
* `TriggerAliasMapRef := ∅`

#### G.0:4.2 - CG‑Spec object model (normative)

`CG‑Spec` is authored per `CG‑Frame`. It SHALL:

* be **published to UTS** as a notation-independent object,
* reference CHR characteristics by id (measurement semantics remain governed by CHR packs),
* constrain what comparisons and aggregations are lawful in this frame via explicit comparator specs and SCP bindings,
* declare minimal evidence gates per characteristic, including explicit failure behavior wiring,
* cite `CN‑Spec` for normalization/comparability policies (no duplication and no shadow specs),
* publish edition pins and policy ids so downstream selection, parity, shipping, and refresh can be reproducible and RSCR-aware.

#### G.0:4.3 - CG‑Spec conceptual model (normative)

```
CG‑Spec :=
⟨
  UTS.id, Edition,
  Context, Purpose, Audience,

  Scope := USM.ScopeSlice(G) ⊕ Boundary{TaskKinds, ObjectKinds},

  entityOfConcern := ⟨GroundingHolon, ReferencePlane ∈ {world|concept|episteme}⟩,
  WorldRegime? ∈ {prep|live},          // only refines ReferencePlane=world; introduces no new planes

  ReferenceMap := minimal map{term/id → UTS|CHR|SoTA-pack refs},

  CNSpecRef := ⟨CN‑Spec ref, CNSpecRef.edition⟩,          // CN‑Spec is the governance card defined in A.19.CN (one governing definition)

  Characteristics := [CHR.Characteristic.id…],          // pointers only; authored in G.3 CHR pack

  // Edition-addressable segments (pins MUST be exposed)
  ComparatorSet := ⟨ComparatorSetId, ComparatorSetRef.edition, [ComparatorSpec…]⟩,
  SCP := ⟨SCPId, SCPRef.edition, map Characteristic.id → SCPEntry⟩,
  MinimalEvidence := ⟨MinEvId, MinimalEvidenceRef.edition?, map Characteristic.id → MinEvidenceEntry⟩,  // min pin: CGSpecRef.edition

  Γ‑fold := ⟨GammaFoldId, ΓFoldRef.edition?,   // pin the actual model/policy when a numerical fold is used
             defaultRef := DefaultId.GammaFoldForR_eff,
             override? := ⟨overrideRef, proof_refs, boundary_notes⟩
           ⟩,

  // Penalty routing and plane policies are by explicit policy ids.
  // For semantics (tri-state, receiving-use loss, model-bound assurance penalties, crossing visibility, set-return), cite G.Core and its governing definitions. The policy fields below are conditional; supply every reference required by the selected use or model.
  CL‑Routing? := ⟨policy_id, map Bridge.CL → penalty_spec⟩, // when the selected use or model maps Bridge.CL to a penalty
  Φ? := ⟨phi_policy_id?, phi_table_ref?, psi_policy_id?, phi_plane_policy_id?⟩, // when any of these policies is used

  AcceptanceStubs := [AcceptanceStubId…],     // templates only; thresholds remain governed by CAL (G.4)

  // Optional hooks are wiring-only; semantics are governed by governing definitions.
  E/E‑LOG Guard? := ⟨policy_id, pins…⟩,
  Illumination? := ⟨
    Q_refs ⊆ Characteristics, D_refs ⊆ Characteristics,
    DescriptorMapRef.edition?, DistanceDefRef.edition?, DHCMethodRef.edition?,
    InsertionPolicyRef?, PromotionPolicyId?
  ⟩,

  RSCR := ⟨
  RSCRTestId[]?,             // SHOULD cover: illegal_op_refusals; unit and scale legality checks; freshness windows; // partial-order scalarisation refusals; threshold semantics; declared-model penalty calculations when used (including a selected CL→R_eff model);
                            // and refusal of degrade.order on unit mismatches (MM‑CHR).
    RSCRTriggerKindId[]
  ⟩,

  Naming := UTS Name Cards (designations under F.17/F.18 plus bridge notes),
  PublicIdContinuity := ⟨governing definition, DRR link, refresh cadence, decay and aging policy, deprecations⟩,
  Provenance := ⟨carrier types, SoTA-pack refs, DRR/SCR linkage⟩
⟩
```

**Local typing notes (normative, non-exhaustive).**

* `ComparatorSpec` MUST be typed against SCP/CHR constraints. Examples of lawful comparators are frame-local choices and are authored here (e.g., dominance where lawful; lexicographic over typed traits; medoid/median for ordinal where lawful; explicit weighted sums only where legality is proven and units are aligned).
* `MinimalEvidenceEntry` MUST declare: lane requirements, evidence carriers, freshness window (if any), and explicit failure behavior wiring. The semantics of `{pass|degrade|abstain}` and `degrade(mode=…)` are delegated to `G.Core`.

#### G.0:4.4 - Interfaces (normative)

| Interface          | Consumes                             | Produces / constrains                                                      |
| ------------------ | ------------------------------------ | -------------------------------------------------------------------------- |
| **G.0‑1 Charter**  | CG‑Frame brief, USM scope signals    | `CG‑Spec.Scope`, `entityOfConcern`, `ReferenceMap`                         |
| **G.0‑2 SCP**      | CHR pack refs (G.3), legality proofs | `CG‑Spec.SCP` + bindings to lawful operators/aggregators                   |
| **G.0‑3 Evidence** | SoTA inputs (G.2), source and carrier provenance account (A.10)   | `CG‑Spec.MinimalEvidence`, `Γ‑fold` segment pins, `CL‑Routing`, `Φ` ids    |
| **G.0‑4 Publish**  | All above                            | Versioned `CG‑Spec@UTS` plus Name Cards, public-id continuity records, and RSCR tests and trigger kinds  |
| **G.0‑5 Expose_CrossingHooks** | `CG‑Spec` + pins required by an applicable E.18 flow crossing or A.21 gate | Inputs for that crossing’s `GateChecks`: the required plane, intent, lane and lexical SD checks |
| **→ G.1**          | `CG‑Spec`                            | Generator guardrails (Comparator/SCP/MinEv pins); degrade/abstain wiring   |
| **→ G.2**          | `CG‑Spec`                            | Harvesting inclusion/exclusion and crossing policy constraints             |
| **→ G.3**          | `CG‑Spec`                            | Required CHR characteristics/scales/operators to exist                     |
| **→ G.4**          | `CG‑Spec`                            | Acceptance templates; evidence minima; Γ‑fold override proof hooks         |
| **→ G.5**          | `CG‑Spec`                            | Eligibility gates and explainability pins (Path/UTS/policy ids)            |
| **→ G.6**          | `CG‑Spec`                            | EvidenceGraph/SCR pinning surface (policy ids + Path/PathSlice discipline) |

#### G.0:4.5 - CG‑Spec authoring chassis (informative)

Begin with the receiving question and the available material: the task or decision request, descriptions of the subject and operating conditions, binding requirements, candidate methods, and existing observations. Reuse an adequate frame. When its criteria are not yet known, establish them before filling the specification.

##### G.0:4.5.1 - Obtain the comparison basis

1. **Recover the decision and its conditions.** Use C.39.RQ:4.1 to work backward from what the receiving result must enable and forward from the available ways of obtaining it. Inspect the request, relevant commitments or rules, and the descriptions of actual use. For each consequential success or failure, ask which property of the subject makes that difference. Recover a binding limit from its applicable requirement or authorized allocation; an observed value establishes performance under its conditions, not the limit the receiver must accept. Where two uses need different conditions, retain distinct scope slices.
2. **Turn the differences into characteristics.** A.19.ECS:4.2 supplies the construction: start with cases that would satisfy, fail or fall outside the use; identify the properties that distinguish them; split a compound property when its components can vary independently; and establish each characteristic’s subject, meaning, scale, units and observation procedure through G.3/C.16. Existing domain definitions and validated procedures can supply these results directly. If the needed characteristic or procedure is unavailable, return that particular construction to its competent supplier, with the decision it prevents.
3. **Choose the comparisons the question needs.** For each proposed comparison, state what relation between results would change the receiving decision. Match that relation to the characteristics’ lawful operations: equality of categories, an order where justified, or a numerical operation whose scale, units and assumptions permit it. Retain separate coordinates when trade-offs have not been resolved. A weighted total requires a justified aggregation and the receiving preference basis. G.0 then enumerates this finite set of comparators and its legality conditions.
4. **Obtain the evidence minima from the claim.** Follow each required characteristic and comparator back to what would establish its inputs and applicability: for example, a traceable observation under the relevant operating conditions, an exact proof for a formal claim, or a justified transfer from a different population. Reuse the applicable domain qualification, measurement or acceptance method. Specify the carriers, conditions and checks it requires, and the consequence when they are missing or fail. G.2 can recover missing source support; G.4 carries the acceptance policy. A currentness window is needed when the claim’s use depends on it; a numerical support fold needs its actual model under B.3/C.2.2.
5. **Return the supported frame and its limit.** The available material may establish all required criteria, disqualify an operation, or leave a particular criterion, authority, measurement procedure or transfer premise unresolved. Keep those outcomes separate. Identify the source, responsible authority, observation or method construction that could settle an unresolved premise, and which comparison must wait for it. A descriptive comparison can remain useful when a required acceptance judgement is unavailable; it must retain that receiving-use limit.

**Worked construction.** A team must compare compression methods for a specified archive batch on one host. The available request says “choose a method that fits the backup operation”; the maintenance allocation gives a 15-minute window and a 2 GiB memory allowance, while the archive requirement demands lossless recovery. The batch inventory and host configuration establish the scope. Working backward exposes three required properties: recovery identity, elapsed time and peak memory. Recovery identity is tested by comparing the recovered contents with the original batch; time and memory use the stated measurement procedures and units. The requirements supply the pass limits. Among passing alternatives, an additional request to reduce storage permits comparison by compressed size; without a preference for trading time against size, the frame retains those coordinates separately.

The available reports now have a precise use. A report that tested recovery on the same batch supplies that observation; a report giving a 12-minute mean on a different host needs a justified transfer or a measurement on the receiving host. That mean does not establish a guarantee of fitting the allocated window. If the receiving requirement is a guaranteed upper bound, the chosen qualification method must supply that bound; otherwise fit remains unestablished. If the allocation is absent, the team can compare observed times and memory but must obtain the applicable allocation before claiming acceptance. If the receiving question changes to archival space efficiency with no execution-window requirement, the performance observations remain usable while the 15-minute gate no longer governs that comparison.

##### G.0:4.5.2 - Bind and publish the established basis

1. **Charter the frame.** Declare `Context`, `Scope`, `entityOfConcern`, boundary examples/non-examples, and `ReferenceMap` from the receiving question and established conditions.
2. **Bind ComparatorSet, SCP and characteristics.** Enumerate the permitted comparator forms obtained above; bind each to the CHR characteristics and its scale, unit, polarity and other legality conditions. Cite existing characteristic ids or publish new ones under UTS discipline.
3. **Declare MinimalEvidence.** For each characteristic, bind the required lanes/carriers, any applicable freshness window or crossing allowance, and explicit failure behavior (tri-state semantics delegated to `G.Core`). Keep unresolved prerequisites visible with the operations they prevent.
4. **Pin the support-composition basis.** Cite `DefaultId.GammaFoldForR_eff` for the model-qualified rule. A numerical fold or loss pins its actual receiving model, compatible inputs, dependency assumptions, and justification refs; monotonicity and boundedness alone are insufficient. When no common aggregate is justified, the referenced rule retains separate support and a bounded synthesis. Publish any actually used Φ/CL policy ids; keep acceptance thresholds in G.4.
5. **Publish and register regression tests.** Publish `CG‑Spec@UTS` with edition-pinned segments; register RSCR tests for the frame’s legality surfaces and evidence minima. Preserve public-id continuity and deprecation notes. State the refresh triggers and any cadence justified by the frame’s use; emit canonical trigger ids when their conditions obtain.

#### G.0:4.6 - Extensions (pattern-scoped; non-core)

All blocks below are `GPatternExtension` modules (PatternScopeId; not new PatternIds). They store wiring only and cite governing patterns.

**GPatternExtension: SpecRefSurfaces**

* **PatternScopeId:** `G.0:Ext.SpecRefSurfaces`
* **GPatternExtensionId:** `SpecRefSurfaces`
* **GPatternExtensionKind:** `InteropSpecific`
* **GoverningPatternId:** `A.19.CN`
* **Uses:** `{A.19.CN}`
* **⊑/⊑⁺:** `∅`
* **RequiredPins/EditionPins/PolicyPins (minimum):**

  * `CNSpecRef.edition` (and any CN-side policy ids referenced by `CG‑Spec` fields)
* **RSCRTriggerKindIds:** `{RSCRTriggerKindId.EditionPinChange, RSCRTriggerKindId.PolicyPinChange, RSCRTriggerKindId.LegalitySurfaceEdit}`
* **Notes (wiring-only):** `CG‑Spec` SHALL cite CN‑Spec; it SHALL NOT restate normalization/comparability semantics.

**GPatternExtension: BridgeAndCLWiring**

* **PatternScopeId:** `G.0:Ext.BridgeAndCLWiring`
* **GPatternExtensionId:** `BridgeAndCLWiring`
* **GPatternExtensionKind:** `InteropSpecific`
* **GoverningPatternId:** `F.9`
* **Uses:** `{F.9, G.7}`
* **⊑/⊑⁺:** `∅`
* **RequiredPins/EditionPins/PolicyPins (minimum):**

  * `BridgeCardId/BridgeId` (when the use relies on the corresponding semantic bridge)
  * `CL` / `CL^k` and `Φ`/`Φ_plane` policy ids (when the corresponding calibration or loss model is used)
* **RSCRTriggerKindIds:** `{RSCRTriggerKindId.CrossingBundleEdit, RSCRTriggerKindId.PolicyPinChange, RSCRTriggerKindId.ReferencePlaneEdit}`
* **Notes (wiring-only):** Crossing semantics and penalty routing are delegated to `G.Core`; this module only lists the required pins used by `CG‑Spec` entries.

**GPatternExtension: SoTAPaletteInputs**

* **PatternScopeId:** `G.0:Ext.SoTAPaletteInputs`
* **GPatternExtensionId:** `SoTAPaletteInputs`
* **GPatternExtensionKind:** `DisciplineSpecific`
* **GoverningPatternId:** `G.2`
* **Uses:** `{G.2}`
* **⊑/⊑⁺:** `∅`
* **RequiredPins/EditionPins/PolicyPins (minimum):**

  * `SoTA-Pack@CG‑Frame` refs used to justify comparator admissibility, evidence minima, and crossing allowances (e.g., claim sheets, operator inventory, bridge matrix ids)
* **RSCRTriggerKindIds:** `{RSCRTriggerKindId.EvidenceSurfaceEdit, RSCRTriggerKindId.CrossingBundleEdit, RSCRTriggerKindId.FreshnessOrDecayEvent}`
* **Notes (wiring-only):** Any SoTA palette/tradition semantics are governed by `G.2`. `G.0` only requires that `CG‑Spec` entries cite the needed SoTA artefacts for auditability.

**GPatternExtension: QDAndExplorationHooks**

* **PatternScopeId:** `G.0:Ext.QDAndExplorationHooks`
* **GPatternExtensionId:** `QDAndExplorationHooks`
* **GPatternExtensionKind:** `MethodSpecific`
* **GoverningPatternId:** `C.18`
* **Uses:** `{C.18, C.19, C.23}`
* **⊑/⊑⁺:** `∅`
* **RequiredPins/EditionPins/PolicyPins (minimum):**

  * `DescriptorMapRef.edition?`, `DistanceDefRef.edition?`, `InsertionPolicyRef?`
  * `FailureBehaviorPolicyId` / SoS‑LOG branch policy id when `degrade(mode=…)` is used
* **RSCRTriggerKindIds:** `{RSCRTriggerKindId.EditionPinChange, RSCRTriggerKindId.PolicyPinChange, RSCRTriggerKindId.TelemetryDelta, RSCRTriggerKindId.FreshnessOrDecayEvent}`
* **Notes (wiring-only):** `CG‑Spec` may declare optional QD/exploration hooks; semantics remain governed by the referenced method patterns.

