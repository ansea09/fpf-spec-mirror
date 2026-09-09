---
chunk_kind: "child"
pattern_id: "G.11"
pattern_title: "Telemetry-Driven Refresh and Decay Orchestrator"
section_id: "G.11:4"
section_title: "Solution — RSCR-driven refresh as a P2W-scoped orchestration kit"
source_path: "FPF-Spec.md"
output_path: "by_section/G.11/G.11__006_solution-rscr-driven-refresh-as-a-p2w-scoped-orchestration-kit.md"
commit_sha: "f4bad21274b54b57071afb2210a8bdb9f61a1c95"
heading_path:
  - "G.11 — Telemetry-Driven Refresh and Decay Orchestrator"
  - "G.11:4 — Solution — RSCR-driven refresh as a P2W-scoped orchestration kit"
line_start: 107191
line_end: 107440
dependencies:
  - "A.6.RCD"
  - "B.3.4"
  - "C.18"
  - "C.19"
  - "C.23"
  - "C.28"
  - "C.32.P2S"
  - "E.18"
  - "F.15"
  - "G.10"
  - "G.12"
  - "G.5"
  - "G.6"
  - "G.7"
  - "G.8"
  - "G.9"
  - "G.Core"
  - "G.Core.TriggerAliasMap.G11"
keywords:
  - "Bridge Sentinels"
  - "PathSlice"
  - "RSCR"
  - "deprecation"
  - "edition-aware"
  - "epistemic debt"
  - "re-shipping"
  - "refresh"
  - "telemetry"
  - "use-qualified currentness"
---

### G.11:4 - Solution — RSCR-driven refresh as a P2W-scoped orchestration kit

#### G.11:4.1 - G.Core linkage (normative)

**GCoreLinkageManifest (normative; canonical shape per `G.Core`; Nil‑elision permitted).**

```text
GCoreLinkageManifest := ⟨
  CoreConformanceProfileIds := {
    GCoreConformanceProfileId.PartG.AuthoringBase,
    GCoreConformanceProfileId.PartG.TriStateGuard,
    GCoreConformanceProfileId.PartG.UTSWhenPublicIdsMinted,
    GCoreConformanceProfileId.PartG.ShippingBoundary
  },

  RSCRTriggerSetIds := {GCoreTriggerSetId.RefreshOrchestration},

  CorePinSetIds := {
    GCorePinSetId.PartG.AuthoringMinimal,
    GCorePinSetId.PartG.CrossingVisibilityPins
  },

  CorePinsRequired := {
    RSCRTriggerKindId,
    RSCRTriggerAliasId?,
    scope: PathSliceId[] | PatternScopeId,
    payloadPins{…},

    RefreshPlanId?,
    RefreshReportId?,
    DeprecationNoticeId?,
    EditionBumpLogId?,

    WorkPlanRef[]?
  },

  DefaultsConsumed := ∅,
  TriggerAliasMapRef := G.Core.TriggerAliasMap.G11
⟩
```

By the `G.Core` **Expansion rule**, the **effective** conformance ids, trigger kinds, and pin obligations for `G.11` are the manifest expansions (profiles, sets, and pin sets) plus the explicit deltas above.

**TriggerAliasIds (visible; labels only).** `{G.11:T0…T7}` (docked via `TriggerAliasMapRef`; aliases are never semantic authorities).

#### G.11:4.2 - Refresh orchestration kit (subject-qualified; conceptual artefacts)

`G.11` defines a kit of authoring-plane artefacts for actual refresh planning and reporting. `RefreshPlanId` is required on a plan and `RefreshReportId` on a report. The linkage manifest applies to the triggers and actions that occur; retaining applicable support creates no trigger, plan or report merely to fill their pins.

1. **`RefreshQueue` (conceptual queue).**
   A queue of refresh candidates keyed by scope (`PathSliceId` preferred; `PatternScopeId` permitted).
   Ordering, prioritization, and batching are policy-bound (and therefore extension-scoped), but every queue item carries canonical trigger kind ids.

2. **`RefreshPlan@Context` (one exact `U.WorkPlan`).**
   A planned refresh is one `U.WorkPlan` episteme under A.15.2. It **does not execute Work** and **does not embed gate decisions**. `RefreshPlan@Context` is only this pattern's application name for the plan; it declares:

   * `RefreshPlanId` (UTS-published id; editioned)
   * `EntityOfConcernRef` and `ReferencePlane` pins (by ref; no implicit widening)
   * `TargetScope := PathSliceId[] | PatternScopeId[]`
   * `PlannedTriggers := RSCRTrigger[]` (canonical trigger kind ids, scope, and payload pins)
   * `PlannedActions := RefreshAction[]` (each action delegates to a subject pattern)
   * `RequiredPins := {EditionPins, PolicyPins, UTS pins, Path pins}` for replayability
   * `PlannedFillingRows[]?` as ClaimGraph content kept inside the WorkPlan under A.15.3 when a value must be pinned against a declaration member defined by its own pattern. A row is addressed only through the WorkPlan and has no separate reference or identity.
3. **`RefreshReport@Context` (record of refresh Work or its audit).**
   An execution or audit report that records:

   * `RefreshReportId` (UTS-published id; editioned)
   * `ExecutedActions[]` with links to cited artefacts governed by cited patterns (e.g., new parity report id, new pack id)
   * `ObservedDeltas` (telemetry deltas, admissibility changes, evidence-relation or source-relation changes) as refs and pins, not as untyped prose
   * `RSCRRefs[]` (any RSCR or regression harness artefacts invoked)
   * `EmittedNotices[] := DeprecationNoticeId[]` and `EditionBumpLogId[]`
   * the canonical trigger kinds actually applied (not only aliases)
4. **`DeprecationNotice@Context` and `EditionBumpLog@Context`.**
   Controlled evolution artefacts that preserve ID-continuity:

   * **DeprecationNotice** explains scope, reason class (canonical trigger kind ids), and successor refs.
   * **EditionBumpLog** records edition increments and the pins that justify them.

   > *Note (normative by delegation).* ID continuity and alias discipline are governed by `G.Core` (do not restate as local rules here).

#### G.11:4.2a - Selected-set, archive, and cultural-variant currentness

Use this line when refresh currentness concerns a selected set, front, Q-front, archive, portfolio lineage, cultural-variant lineage, style or tradition term bridge, path slice, reused `A.6.RCD` predicate definition, or admitted derived relation kind.

```text
RefreshCurrentnessLine@Context:
  governedObjectRef:
  currentnessObjectKind:
  sourceRecordRef:
  editionOrLineagePins:
  affectedPathSliceOrScope:
  subjectPatternLocator:
  receivingUseAndApplicableConditions:
  currentnessConclusion:
  plannedRefreshAction?:
  refreshReportRef?:
```

`currentnessObjectKind` may name, for example, a selected set, `Front`, `Q-front`, `ExplorationArchive`, `Archive`, a cultural lineage, a term bridge, or a reused predicate definition. Use the line only when its recipient needs this structured currentness result; identify the temporal reference and relevant window within its conditions and pins. `plannedRefreshAction?` is absent when no refresh is selected, and `refreshReportRef?` is absent when no such report exists. The line states applicability for a use, not that the subject claim is true or adequately supported. Use `G.5` for selected-set declaration, `E.17` and `E.24.PUB` for publication, `C.18` for archive and front relations, `C.19` for pool treatment, `C.36` for cultural-evolution claims, `F.17` for exact local `SchemeSenseCell`s, `F.18` for name settlement, `F.9` for obtaining Bridges, and `A.6.RCD` for a derived relation kind.

Use the existing result or publication for a needed currentness conclusion or limitation. Use `RefreshPlan@Context`, `RefreshReport@Context`, `DeprecationNotice@Context` or `EditionBumpLog@Context` when the corresponding plan, performed work, deprecation or edition change actually occurs; do not add an empty ticket or notice for unchanged applicability.

When the governed object is a reusable `A.6.RCD` predicate definition or an admitted derived relation kind, the currentness line pins the exact base definitions, named substrate and edition, authorized derivation operation, and applicability scope. A change to any of them reopens the affected derivation and its dependent uses under `A.6.RCD`; G.11 schedules the bounded refresh but does not redefine the relation or derivation.

#### G.11:4.3 - Orchestration semantics (conceptual; delegating to governing definitions)



Use `G.11` to plan scoped actions from typed causes; action semantics remain with their subject patterns.

**4.3.1 Ingestion.**
Consume RSCR triggers from:

* telemetry hooks (e.g., `G.8`, `G.10`, `G.12`),
* freshness and decay events (`B.3.4`),
* evidence, bridge, policy, edition, relied-on base-definition, named-substrate-edition, or derivation-applicability edits (from the respective subject patterns' publication faces, forms, or units).

Every ingested signal is normalized into an `RSCRTrigger` (canonical id, scope, payload pins), with optional alias labels.

**4.3.2 Scope closure (EvidenceGraph-first).**
Compute the minimal dependency closure over:

* cited evidence and source relations, with `G.6` `PathId` and `PathSliceId` refs when a graph path slice is the current math-lens expression,
* declared crossings (`G.7` sentinels; `CrossingBundle` visibility),
* and pinned references (editions and policies).

The closure is a planning-time claim about affected slices, distinct from execution of the planned refresh actions. Interpret a B.3.4 trigger for the receiving claim and use: available information may establish continued applicability, a narrower use, an obtainable refresh need or a necessary suspension. An age-only signal does not determine that disposition. If support remains sufficient, stop with the usable result; retain only the limitation or reason a later recipient needs.

**4.3.3 Planning (P2W boundary).**
When the selected response requires planned refresh, use C.11 and C.19.2 for its marginal contribution, cost, delay and displaced work. Produce `RefreshPlan@Context` for the actions actually selected; possible action forms include:

* `RerunHarvest` (delegates to the selected harvest, source-currentness, or SoTA governing definition named by value, such as `G.1` or `G.2`, when that definition is current)
* `RerunParity` (delegates to `G.9`)
* `RecomputeSelectionOrSetResult` (delegates to `G.5`)
* `RebindBridgeOrCrossing` (delegates changes to the obtaining Bridge to `F.9`, calibration-record changes to `G.7`, and crossing visibility to `E.18` and the applicable visibility harnesses)
* `UpdateEvidenceBindings` (delegates to `G.6`)
* `ReshipPack` (delegates to `G.10`)
* `UpdateBundle` (delegates to `G.8`)
* `UpdateDashboardSlice` (delegates to `G.12`)
* `EmitDeprecationNotice` or `EmitEditionBumpLog` (publication units governed by this pattern)

**4.3.4 Execution and audit.**
When selected actions are performed as Work or Work-bound audit, publish the corresponding `RefreshReport@Context`. A scoped applicability judgement can reuse available information without a new experiment; a plan alone establishes neither performance nor a new observation.
Gating outcomes (admit, degrade, or abstain) follow `G.Core` tri-state semantics and are recorded through policy ids and cited evidence or source relations, rather than as local bespoke outcomes.

#### G.11:4.3a - Causal-use refresh sentinels

When a shipped result consumes C.28, refresh planning watches the causes that can change a supported use, unsupported use, support-result verdict, limits, or downstream decision basis:

| Sentinel | Affected result | Refresh pins |
| --- | --- | --- |
| sampling-realizability shift | `CounterfactualSamplingRealizabilityResult` | target distribution, decision Method and any derivation, physical, ethical, operational, and history constraints, required construction, bound, or obstruction, status, supported use, and unsupported use |
| performed sampling or resulting-data shift | dated sampling Work plus A.10 evidence path and empirical data regime | WorkPlan when used; actual performer identified through A.13; dated Work independently admitted through A.15.1; Method and window; resulting sample or data; provenance and currentness. Add F.6 with the same A.13 assignment only if the refresh decision needs to say exactly under which assignment the Work was performed. F.6 identifies neither performer nor assignment; a missing or failed attribution leaves the Work intact. A realizability result cannot substitute. |
| identification or bound shift | `CausalIdentificationResult` | data-regime refs, assumptions, identifying derivation, bound or failure witness, sensitivity |
| estimate shift | `CausalEstimateResult` | identification or design basis, data, estimator Method, diagnostics, uncertainty, sensitivity, and any live estimation-consistency result |
| target-trial practice shift | protocol and mapping results | question/estimand, protocol-to-data mapping, assumptions, estimate/precision, sensitivity and reporting source edition |
| causal-fairness shift | C.28 support result plus D.5 `BiasAuditReport@Context` | fairness estimand, extra counterfactual-identification assumptions, estimate and consistency result when used, support components and result, affected population, audit limits, and decision |
| causal-representation shift | `CausalVariableRepresentationRecord` | intervention validity, invariance, abstraction fidelity, query preservation, shift and use limits |
| off-policy or causal-RL shift | `OffPolicyCausalEvaluationResult` | behaviour/evaluation policies, horizon/history, confounding, overlap, endpoints, estimator and uncertainty |
| simulation-validation shift | `simulationResultRef` in `CausalSupportComponentRefs` | model assumptions, validation, sensitivity, supported model use and unsupported realized/interventional use |
| transport-endpoint shift | `CausalTransportabilityResult` | source/target population, domain, environment and data-generating regime, assumptions, windows, formula and unresolved limits |

These are payload distinctions under existing G.Core trigger kinds, not new trigger kinds. Reopen only the affected result and downstream uses that consumed it.

#### G.11:4.4 - Extensions (pattern-scoped; non-core)

Discipline-specific refresh strategies and generator-specific wiring live as `GPatternExtension` blocks. Scheduling, ordering, priority, and budget policy for the refresh queue are not separate extension semantics: `G.11` defines the required policy pins on `RefreshQueue` and `RefreshPlan@Context`, while A.15.2 and A.15.3 keep the WorkPlan and its local content separate from dated Work.

##### G.11:Ext.TriggerAliases

**PatternScopeId:** `G.11:Ext.TriggerAliases`
**GPatternExtensionId:** `TriggerAliases`
**GPatternExtensionKind:** `InteropSpecific` (alias docking)
**GoverningPatternId:** `G.Core`
**Uses:** `{G.Core}` (cites `G.Core.TriggerAliasMap.G11`)
**`⊑` and `⊑⁺`:** `∅`
**Required pins, edition pins, and policy pins (minimum):**

* `RSCRTriggerKindId[]` (canonical ids recorded on triggers)
* `RSCRTriggerAliasId?` (e.g., `G.11:T0…T7` as labels only)
* `scope: PathSliceId[] | PatternScopeId`

**RSCRTriggerKindIds:** `{RSCRTriggerKindId.EditionPinChange, RSCRTriggerKindId.PolicyPinChange, RSCRTriggerKindId.TelemetryDelta, RSCRTriggerKindId.FreshnessOrDecayEvent, RSCRTriggerKindId.CrossingBundleEdit, RSCRTriggerKindId.PenaltyPolicyEdit, RSCRTriggerKindId.MaturityRungChange, RSCRTriggerKindId.EvidenceSurfaceEdit}`
**Notes (wiring-only):** This block **does not define** what `T0…T7` mean; it only preserves the labels and requires docking via `G.Core.TriggerAliasMap.G11`.

##### G.11:Ext.DecayAndDebt

**PatternScopeId:** `G.11:Ext.DecayAndDebt`
**GPatternExtensionId:** `DecayAndDebt`
**GPatternExtensionKind:** `DisciplineSpecific`
**GoverningPatternId:** `B.3.4` (use-qualified currentness and interpreted planning debt)
**Uses:** `{B.3.4, G.6}`
**`⊑` and `⊑⁺`:** `∅`
**Required pins, edition pins, and policy pins (minimum):**

* The receiving claim/use and the changed premise or applicable review condition, with source references where published.
* `FreshnessWindowDeclRef?`, `DecayPolicyIdRef?` or `EpistemicDebtBudgetRef?` only when the adopted window, deterioration model or planning measure is used. Their source supplies the meaning; no default expiry or debt budget is required.
* `PathSliceId[]` for the dependent claims and uses actually affected, not every use of an old carrier.

**RSCRTriggerKindIds:** `{RSCRTriggerKindId.FreshnessOrDecayEvent, RSCRTriggerKindId.EvidenceSurfaceEdit, RSCRTriggerKindId.BaselineBindingEdit}`
**Notes (wiring-only):** B.3.4 determines what the trigger means for the use. Continue, narrow, refresh, suspend or an authorized exception remain available where warranted; no Refresh/Deprecate/Waive triad or automatic downgrade is introduced here. Currentness is not assurance of the underlying claim. Budget and priority logic apply only when their interpreted policies are used.

##### G.11:Ext.QDRefreshWiring

**PatternScopeId:** `G.11:Ext.QDRefreshWiring`
**GPatternExtensionId:** `QDRefreshWiring`
**GPatternExtensionKind:** `MethodSpecific`
**GoverningPatternId:** `C.18` (QD semantics; descriptor, distance, and insertion)
**Uses:** `{C.18, C.19, G.5, G.8}`
**`⊑` and `⊑⁺`:** `∅`
**Required pins, edition pins, and policy pins (minimum):**

* `DescriptorMapRef.edition`, `DistanceDefRef.edition`
* `CharacteristicSpaceRef.edition?` (required when a domain-family coordinate is declared by the QD governing definition)
* `InsertionPolicyRef`, `EmitterPolicyRef` (policy-bound)
* `PathSliceId` (archive or illumination scope) and `policy-id` for emitted telemetry triggers

**RSCRTriggerKindIds:** `{RSCRTriggerKindId.TelemetryDelta, RSCRTriggerKindId.EditionPinChange, RSCRTriggerKindId.PolicyPinChange}`
**Notes (wiring-only):** `G.11` does not restate QD semantics; it ensures pins are present so reruns are comparable.

##### G.11:Ext.OEERefreshWiring

**PatternScopeId:** `G.11:Ext.OEERefreshWiring`
**GPatternExtensionId:** `OEERefreshWiring`
**GPatternExtensionKind:** `MethodSpecific`
**GoverningPatternId:** `C.19` (open-ended exploration and exploration-exploitation logistics)
**Uses:** `{C.19, G.5, G.8, G.9}`
**`⊑` and `⊑⁺`:** `∅`
**Required pins, edition pins, and policy pins (minimum):**

* `TransferRulesRef.edition`, `EnvironmentValidityRegion` (when OEE is declared by the subject patterns)
* `GeneratorFamilyId` and `TransferRulesRef` wiring pins (as published by the governing definitions)
* telemetry scope pins (`PathSliceId`, `policy-id`)

**RSCRTriggerKindIds:** `{RSCRTriggerKindId.EditionPinChange, RSCRTriggerKindId.TelemetryDelta, RSCRTriggerKindId.PolicyPinChange}`
**Notes (wiring-only):** Any OEE method semantics live with the governing definition; this module only wires refresh triggers to comparable reruns.

##### G.11:4.4a - Scheduling and priority policy pins

Scheduling strategies (bandit-style allocation, queueing, cadence policies, early stopping, or manual priority rules) may influence the order and budget of refresh work, but they do not define trigger meaning, action semantics, parity semantics, shipping semantics, or Part-G-wide defaults.

`G.11` therefore treats scheduling as policy-bound refresh planning:

* `RefreshPriorityPolicyIdRef` names the policy used to order or prioritize queue items.
* `BudgetDeclRef` names the time, compute, cost, risk, or cadence boundary for the planned refresh.
* `RSCRTriggerKindId[]` still comes from `G.Core`; scheduling policy does not mint trigger kinds.
* planned refresh remains the exact `U.WorkPlan` locally called `RefreshPlan@Context`; executed refresh is recorded in `RefreshReport@Context` or Work-bound audit.

If no priority or budget policy is declared, no scheduling heuristic is admissible by appearance; the plan must either use the ordinary queue order or state the missing policy pin as a blocker.

