---
chunk_kind: "child"
pattern_id: "G.11"
pattern_title: "Decide Whether and How to Refresh SoTA Packs and Related Results (Telemetry and Decay)"
section_id: "G.11:4"
section_title: "Solution — RSCR-driven refresh as a P2W-scoped orchestration kit"
source_path: "FPF-Spec.md"
output_path: "by_section/G.11/G.11__006_solution-rscr-driven-refresh-as-a-p2w-scoped-orchestration-kit.md"
commit_sha: "9fa2a3596dab58d282d736bcf413cdda4286db0a"
heading_path:
  - "G.11 — Decide Whether and How to Refresh SoTA Packs and Related Results (Telemetry and Decay)"
  - "G.11:4 — Solution — RSCR-driven refresh as a P2W-scoped orchestration kit"
line_start: 131551
line_end: 131816
dependencies:
  - "A.10.1"
  - "A.6.RCD"
  - "B.3.4"
  - "C.11.DUA"
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

Use the following artifacts for refresh planning and reporting. `RefreshPlanId` is required on a plan and `RefreshReportId` on a report. The linkage manifest applies to the triggers and actions that occur; retaining applicable support creates no trigger, plan or report merely to fill their pins.

1. **`RefreshQueue` (conceptual queue).**
   A queue of refresh candidates keyed by affected scope (`PathSliceId` refs preferred where graph-expressed; `PatternScopeId` permitted). One candidate may cover several dependent slices.
   Ordering, prioritization and batching use declared policies; every queue item carries canonical trigger kind ids.

2. **`RefreshPlan@Context` (one exact `U.WorkPlan`).**
   A planned refresh is one `U.WorkPlan` episteme under A.15.2. It **does not execute Work** and **does not embed gate decisions**. `RefreshPlan@Context` is only this pattern's application name for the plan; it declares:

   * `RefreshPlanId` (UTS-published id; editioned)
   * `EntityOfConcernRef` and `ReferencePlane` pins (by ref; no implicit widening)
   * `TargetScope := PathSliceId[] | PatternScopeId[]`
   * `PlannedTriggers := RSCRTrigger[]` (canonical trigger kind ids, scope, and payload pins)
   * `PlannedActions := RefreshAction[]` (each action delegates to a subject pattern)
   * `RequiredPins`: exact affected source and result editions, policy pins and scope for replayability; UTS pins for public identities actually used; graph Path pins when the selected scope is graph-expressed or an independently applicable receiving contract requires them.
   * `PlannedFillingRows[]?` as ClaimGraph content kept inside the WorkPlan under A.15.3 when a value must be pinned against a declaration member defined by its own pattern. A row is addressed only through the WorkPlan and has no separate reference or identity.
3. **`RefreshReport@Context` (record of refresh Work or its audit).**
   An execution or audit report that records:

   * `RefreshReportId` (UTS-published id; editioned)
   * `ExecutedActions[]` with independently admitted A.15.1 Work refs and their A.13-qualified actual performer refs, plus links to the resulting artifacts under their subject patterns (for example, a new parity report or pack id). Add F.6 attribution only when the receiving use consumes it.
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

Use this line when a recipient needs a structured currentness result concerning a selected set, front, Q-front, archive, portfolio lineage, cultural-variant lineage, style or tradition term bridge, path slice, reused `A.6.RCD` predicate definition, or admitted derived relation kind.

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

Normalize each ingested signal into an `RSCRTrigger` with its canonical id, scope and payload pins; retain an alias label when used.

**4.3.2 Scope closure over the actual dependencies.**
Start from the changed premise and the receiving question. Establish the minimal dependency closure that includes every actual dependent use whose claim, action or required check can change. Minimality excludes unrelated uses; it does not select the fewest nodes or stop at the first affected slice. Follow:

* cited evidence and source relations, using G.6 `PathId` and `PathSliceId` refs where those dependencies are graph-expressed;
* declared crossings, including G.7 sentinels and required `CrossingBundle` visibility; and
* pinned editions and policies consumed by the receiving result.

Recover the exact direct use at each step. A common evidence item, causal assumption, calibration or policy can feed several paths and a result that combines them. Include those branches and the combining use before choosing actions. Repeated citations to one basis do not make it independent support. G.6 provides the representation and indexes; A.10.1 supplies source-change discovery, direct-use tests and coverage limits when the existing account is insufficient. Graph reachability alone establishes no dependence. Keep an unresolved branch explicit and continue independently resolved branches.

For a nongraph result, name the exact source, receiving result/use and dependency under `PatternScopeId`. Use `PathSliceId` when the scope is graph-expressed or independently required by the receiving contract. This closure states which conclusions need reconsideration; it neither performs their subject judgement nor commits every affected use to a rerun. Apply the subject rules with available evidence. An affected branch may retain the same supported conclusion, acquire a narrower use, need refresh or require suspension; an independent result remains reusable on its own qualified basis.

Interpret a B.3.4 trigger for the receiving claim and use. Age alone does not select a disposition. Stop when the present basis gives the warranted answer; keep only a limitation or reason that a later recipient needs. If a subject judgement reveals another consequential dependency, return it to the scope before planning dependent work.

**4.3.3 Planning (P2W boundary).**
Use C.11.DUA to compare further inquiry with the warranted answer already available. Select an attainable action for what it can change at the receiving horizon, including its full cost, delay and displaced work. C.11 and, where applicable, C.19.2 supply the choice; binding evidence and authority requirements remain in force. Produce `RefreshPlan@Context` only for the planned actions selected. Possible action forms include:

* `RerunHarvest` (delegates to the selected harvesting or SoTA method, such as `G.2`; use `G.1` additionally only when its generator-kit cards or wiring must change)
* `RerunParity` (delegates to `G.9`)
* `RecomputeSelectionOrSetResult` (delegates to `G.5`)
* `RebindBridgeOrCrossing` (delegates changes to the obtaining Bridge to `F.9`, calibration-record changes to `G.7`, and crossing visibility to `E.18` and the applicable visibility harnesses)
* `UpdateEvidenceBindings` (updates the provenance representation under G.6 after any changed direct relation or subject result has been established under its own governor)
* `ReshipPack` (delegates to `G.10`)
* `UpdateBundle` (delegates to `G.8`)
* `UpdateDashboardSlice` (delegates to `G.12`)
* `EmitDeprecationNotice` or `EmitEditionBumpLog` (publication units governed by this pattern)

**4.3.4 Execution and audit.**
When selected actions are performed as Work or Work-bound audit, identify the actual performers and independently admitted occurrences and publish the corresponding `RefreshReport@Context`. Assess the returned subject results for each receiving use, including any result that combines refreshed and retained branches. Reuse sufficient existing observations where applicable; a plan supplies no new observation or performance.
Gating outcomes (admit, degrade, or abstain) follow `G.Core` tri-state semantics and are recorded through policy ids and cited evidence or source relations, rather than as local bespoke outcomes.

#### G.11:4.3a - Causal-use refresh sentinels

When a shipped result consumes C.28, inspect the following changes when they can alter supported or unsupported use, a support-result verdict, its limits or a downstream decision basis:

| Sentinel | Affected result | Refresh pins |
| --- | --- | --- |
| sampling-realizability shift | `CounterfactualSamplingRealizabilityResult` | target distribution, decision Method and any derivation, physical, ethical, operational, and history constraints, required sampling construction or obstruction, unresolved questions, status, supported use, and unsupported use |
| performed sampling or resulting-data shift | dated sampling Work plus A.10 evidence path and empirical data regime | WorkPlan when used; actual performer identified through A.13; dated Work independently admitted through A.15.1; Method and window; resulting sample or data; provenance and currentness. Add F.6 with the same A.13 assignment only if the refresh decision needs to say exactly under which assignment the Work was performed. F.6 identifies neither performer nor assignment; a missing or failed attribution leaves the Work intact. A realizability result cannot substitute. |
| identification or bound shift | `CausalIdentificationResult` | data-regime refs, assumptions, identifying derivation, bound or failure witness, sensitivity |
| estimate shift | `CausalEstimateResult` | identification or design basis, data, estimator Method, diagnostics, uncertainty, sensitivity, and any live estimation-consistency result |
| target-trial practice shift | protocol and mapping results | question/estimand, protocol-to-data mapping, assumptions, estimate/precision, sensitivity and reporting source edition |
| causal-fairness shift | C.28 support result plus D.5 `BiasAuditReport@Context` | fairness estimand, extra counterfactual-identification assumptions, estimate and consistency result when used, support components and result, affected population, audit limits, and decision |
| causal-representation shift | `CausalVariableRepresentationRecord` | intervention validity, invariance, abstraction fidelity, query preservation, shift and use limits |
| off-policy or causal-RL shift | `OffPolicyCausalEvaluationResult` | behaviour/evaluation policies, horizon/history, confounding, overlap, endpoints, estimator and uncertainty |
| simulation-validation shift | `simulationResultRef` in `CausalSupportComponentRefs` | model assumptions, validation, sensitivity, supported model use and unsupported realized/interventional use |
| transport-endpoint shift | `CausalTransportabilityResult` | source/target population, domain, environment and data-generating regime, assumptions, windows, formula and unresolved limits |

These are payload distinctions under existing G.Core trigger kinds. Apply §4.3.2 to every result and receiving use that consumes the changed causal basis, including several results sharing an assumption or data source.

#### G.11:4.4 - Extensions (pattern-scoped; non-core)

Discipline-specific refresh strategies and generator-specific wiring use `GPatternExtension` blocks. Queue scheduling uses the policy pins on `RefreshQueue` and `RefreshPlan@Context` described in §4.4a. A.15.2 and A.15.3 keep the WorkPlan and its local content separate from dated Work.



##### G.11:4.4.1 - GPatternExtension — G.11:Ext.TriggerAliases


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



##### G.11:4.4.2 - GPatternExtension — G.11:Ext.DecayAndDebt


**PatternScopeId:** `G.11:Ext.DecayAndDebt`
**GPatternExtensionId:** `DecayAndDebt`
**GPatternExtensionKind:** `DisciplineSpecific`
**GoverningPatternId:** `B.3.4` (use-qualified currentness and interpreted planning debt)
**Uses:** `{B.3.4, G.6}`
**`⊑` and `⊑⁺`:** `∅`
**Required pins, edition pins, and policy pins (minimum):**

* The receiving claim/use and the changed premise or applicable review condition, with source references where published.
* `FreshnessWindowDeclRef?`, `DecayPolicyIdRef?` or `EpistemicDebtBudgetRef?` only when the adopted window, deterioration model or planning measure is used. Their source supplies the meaning; no default expiry or debt budget is required.
* Exact dependent claims and uses actually affected, expressed as `PatternScopeId` for nongraph scope or `PathSliceId[]` for graph scope. Retain graph pins when an independently applicable profile requires them; carrier age alone does not select every use of that carrier.

**RSCRTriggerKindIds:** `{RSCRTriggerKindId.FreshnessOrDecayEvent, RSCRTriggerKindId.EvidenceSurfaceEdit, RSCRTriggerKindId.BaselineBindingEdit}`
**Notes (wiring-only):** B.3.4 determines what the trigger means for the use. Continue, narrow, refresh, suspend or an authorized exception remain available where warranted; no Refresh/Deprecate/Waive triad or automatic downgrade is introduced here. Currentness is not assurance of the underlying claim. Budget and priority logic apply only when their interpreted policies are used.



##### G.11:4.4.3 - GPatternExtension — G.11:Ext.QDRefreshWiring


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
* Exact archive or illumination scope and `policy-id` for emitted telemetry triggers: `PatternScopeId` for nongraph scope; `PathSliceId` when graph-expressed or required by an independently applicable parity, evidence or shipping contract.

**RSCRTriggerKindIds:** `{RSCRTriggerKindId.TelemetryDelta, RSCRTriggerKindId.EditionPinChange, RSCRTriggerKindId.PolicyPinChange}`
**Notes (wiring-only):** `G.11` does not restate QD semantics; it ensures pins are present so reruns are comparable.



##### G.11:4.4.4 - GPatternExtension — G.11:Ext.OEERefreshWiring


**PatternScopeId:** `G.11:Ext.OEERefreshWiring`
**GPatternExtensionId:** `OEERefreshWiring`
**GPatternExtensionKind:** `MethodSpecific`
**GoverningPatternId:** `C.19` (open-ended exploration and exploration-exploitation logistics)
**Uses:** `{C.19, G.5, G.8, G.9}`
**`⊑` and `⊑⁺`:** `∅`
**Required pins, edition pins, and policy pins (minimum):**

* `TransferRulesRef.edition`, `EnvironmentValidityRegion` (when OEE is declared by the subject patterns)
* `GeneratorFamilyRowRef = <GeneratorFamilyId, rowEdition>` and `TransferRulesRef` wiring pins (as published by G.5 and the governing definitions); resolve the exact row edition used by the affected result
* exact telemetry scope and `policy-id`: `PatternScopeId` for nongraph scope; `PathSliceId` when graph-expressed or required by an independently applicable parity, evidence or shipping contract.

**RSCRTriggerKindIds:** `{RSCRTriggerKindId.EditionPinChange, RSCRTriggerKindId.TelemetryDelta, RSCRTriggerKindId.PolicyPinChange}`
**Notes (wiring-only):** Any OEE method semantics live with the governing definition; this module only wires refresh triggers to comparable reruns.

##### G.11:4.4a - Scheduling and priority policy pins

Scheduling strategies (bandit-style allocation, queueing, cadence policies, early stopping, or manual priority rules) may influence the order and budget of refresh work, but they do not define trigger meaning, action semantics, parity semantics, shipping semantics, or Part-G-wide defaults.

`G.11` therefore treats scheduling as policy-bound refresh planning:

* `RefreshPriorityPolicyIdRef` names the policy used to order or prioritize queue items.
* `BudgetDeclRef` names the time, compute, cost, risk, or cadence boundary for the planned refresh.
* `RSCRTriggerKindId[]` still comes from `G.Core`; scheduling policy does not mint trigger kinds.
* planned refresh remains the exact `U.WorkPlan` locally called `RefreshPlan@Context`; executed refresh is recorded in `RefreshReport@Context` or Work-bound audit.

Use an applicable ordinary queue-order rule when it already settles the scheduling choice. If a needed priority or budget rule is missing, resolve that choice under its governing authority before the plan relies on it; missing required policy pins remain a blocker. A heuristic supplies no policy merely by appearing in a queue.

