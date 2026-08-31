---
chunk_kind: "child"
pattern_id: "G.9"
pattern_title: "Parity and Benchmark Harness"
section_id: "G.9:4"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/G.9/G.9__008_solution.md"
commit_sha: "e400eab3757d60a8d05196046bed002dff1839e0"
heading_path:
  - "G.9 — Parity and Benchmark Harness"
  - "G.9:4 — Solution"
line_start: 104744
line_end: 105104
dependencies:
  - "A.19"
  - "A.2.6"
  - "A.21"
  - "C.18"
  - "C.19"
  - "C.21"
  - "C.22.1"
  - "C.23"
  - "C.27"
  - "C.28"
  - "E.10"
  - "E.17"
  - "E.18"
  - "E.5.2"
  - "F.15"
  - "F.17"
  - "F.9"
  - "G.0"
  - "G.4"
  - "G.5"
  - "G.6"
  - "G.7"
  - "G.Core"
  - "U.ClaimScope"
keywords:
  - "adaptation parity"
  - "benchmark plan"
  - "comparator pins"
  - "freshness windows"
  - "parity harness"
  - "selected-set outcomes"
---

### G.9:4 — Solution
#### G.9:4.0 — G.Core linkage (normative)

This pattern is **core‑invariant** and therefore binds to **G.Core** by declaration (not by restating invariants here).

**GCoreLinkageManifest (G.9)** *(normative; expands per `G.Core:4.2`)*
Effective obligations/pins/triggers are computed as **union(expand(sets), explicit deltas)** under `Nil‑elision`.

* `CoreConformanceProfileIds` := {
  `GCoreConformanceProfileId.PartG.AuthoringBase`,
  `GCoreConformanceProfileId.PartG.TriStateGuard`,
  `GCoreConformanceProfileId.PartG.ShippingBoundary`,
  `GCoreConformanceProfileId.PartG.UTSWhenPublicIdsMinted`
  }

* `RSCRTriggerSetIds` := {
  `GCoreTriggerSetId.CGSpecGate`
  }
* `RSCRTriggerKindIds` := {
  `RSCRTriggerKindId.EvidencePathOrSourceRelationEdit`,
  `RSCRTriggerKindId.PenaltyPolicyEdit`,
  `RSCRTriggerKindId.BaselineBindingEdit`,
  `RSCRTriggerKindId.TelemetryDelta`
  }
  *(Pattern-local deltas; cross-tradition or Bridge-calibration causes are wired via `G.9:Ext.CrossTraditionParity` and MUST NOT over-trigger parity runs that use one already recovered meaning and ReferencePlane.)*

* `DefaultsConsumed` := {
  `DefaultId.DominanceRegime`,
  `DefaultId.PortfolioMode`,
  `DefaultId.GammaFoldForR_eff`
  }
  *(Defaults are cited through `G.Core.DefaultGoverningDefinitionIndex` (not restated here); the expected default governing definitions are `CC‑G5.28`, `CC‑G5.23`, and `CC‑G5.4` respectively.)*

* `CorePinSetIds` := {
  `GCorePinSetId.PartG.AuthoringMinimal`,
  `GCorePinSetId.PartG.CrossingVisibilityPins`
  }

* `CorePinsRequired` *(pattern delta; pin names only; all are id‑valued unless noted)* := {
  `ComparatorSpecRef.edition`,
  `entityOfConcernRef?`, `targetRefs[]?`, *(exactly one subject branch)*
  `ClaimScope`, `EvaluationWindow`, `FreshnessWindows`,
  `BaselineSet`, `BaselineBindingRef`,
  `ParityPinSet`,
  `PlannedFillingRows[]?`,
  `EvidenceGraphId`,
  `Budgeting?`,
  `EpsilonDominance?`,
  `UNM_id?`, `NormalizationMethodId[]?`, `NormalizationMethodInstanceId[]?`,
  `SCPRef.edition?`, `MinimalEvidenceRef.edition?`
  }
*(Nil‑elision applies; mode‑specific definition pins are introduced only by the corresponding `GPatternExtension` blocks.)*

* `TriggerAliasMapRef` := `∅`

#### G.9:4.1 — Objects and publication records

All objects below are **notation‑independent**; serialisations (if any) are handled in shipping and interop publication forms, not here.

**(1) `ParityPlan`** *(one exact `U.WorkPlan` episteme; `ParityPlan` is the local application name)*
A plan that fixes *what is being compared* and *under what pinned conditions*.

Minimal fields (conceptual; ids/pins only):

`ParityPlan := ⟨
  ParityPlanId(UTS),                       // continuing plan lineage
  planEdition,                            // one immutable edition
  CGFrameId?,                              // exact cited CG frame when the plan depends on one
  entityOfConcernRef? := EntityOfConcernRef, // one-EntityOfConcern branch only
  targetRefs[]?,                            // exact-target branch only; existing kinds and editions
  groundingHolonRef := GroundingHolonRef,
  referencePlaneRef := ReferencePlane,
  claimScopeRef := ClaimScope,
  EvaluationWindow,
  UNM_id?, NormalizationMethodId[]?, NormalizationMethodInstanceId[]?, // when “normalize, then compare” is required (ids only; semantics come from CN‑Spec / UNM)
  EpsilonDominance?,                       // optional ε-front thinning (ε≥0; id/param; pinned when used)
  PortfolioMode?, DominanceRegime?,         // may be explicit or inherited via DefaultGoverningDefinition (semantics follow G.5)
  BaselineSet,                            // exact method-family or generator-family targets (ids; notation-independent)
  BaselineBindingRef,                      // evidence-backed baseline-set reference that says what counts as baseline
  FreshnessWindows,
  CNSpecRef.edition, CGSpecRef.edition, ComparatorSpecRef.edition, // edition-pinned refs
  SCPRef.edition?,                         // optional (when a specific SCP profile must be pinned/cited)
  MinimalEvidenceRef.edition?,             // optional (when CG-Spec exposes minima profiles by ref)
  Budgeting?,
  ParityPinSet,
  EvidenceGraphId, PathId[], PathSliceId?,
  PlannedFillingRows[]?                    // declaration-local A.15.3 content inside this WorkPlan; no independent row refs
⟩`

`ParityPlanRef := <ParityPlanId, planEdition>` designates one immutable plan edition. Changing its subject, baseline binding, comparator edition, or another active value that can change the run or its interpretation creates a new `planEdition`. The lineage id may remain only while this is still the same continuing plan; old `ParityPlanRef` values continue to resolve their old editions.

Exactly one subject branch is present. Use `entityOfConcernRef` when the report compares results about one EntityOfConcern. Use `targetRefs[]` when the targets themselves are compared; each ref keeps the kind and edition defined by its existing subject pattern. In particular, a G.5 method-family target is an exact `MethodFamilyRowRef`, and a generator-family target is an exact `GeneratorFamilyRowRef`.

For example, a direct comparison of `<ThresholdTrendReview-local, R3>` and `<SpectralResidualReview-local, R2>` puts those two exact row refs in `targetRefs[]`; the plan may explicitly use the same two refs as its `BaselineSet`. A comparison of their results for `Pump-P17` instead puts `Pump-P17` in `entityOfConcernRef`, leaves `targetRefs[]` absent, and uses `BaselineBindingRef` to say how the two method rows supply results about that pump.

`BaselineSet` names the alternatives treated as the comparison baseline; it supplies `targetRefs[]` only when the plan explicitly says that the same exact refs serve both purposes. Otherwise the subject and baseline remain separate, and `BaselineBindingRef` records how that baseline applies to the named subject. These exact values determine what is compared and when the parity claim is usable; do not add `ParityContextId`. If the plan relates expressions with distinct source-local meanings, first recover the exact F.17 cells and establish the required F.9 relation. A shared label, source note, or generic context identifier does not establish comparability.

**(2) `ParityPinSet`** *(pin set)*
A declared set of pins required for reproducibility and audit (editions + policy‑ids + UTS/Path pins).
The concrete contents are *pattern-local* (G.9 declares the pin set), but must satisfy the *core pin discipline* via `G.Core`.

**(3) `ParityReport`** *(UTS publication record; work-result or audit-facing publication record only when the neighboring source exists)*
A UTS-publishable parity publication record produced by running one exact `ParityPlanRef`. By itself it is not a dated `U.Work` occurrence, audit performance, evidence path, assurance result, or gate decision; those claims require A.15 and A.15.1, A.10 and G.6, B.3, or A.21 respectively.

`ParityReport := ⟨
  ParityReportId(UTS),
  parityPlanRef := ParityPlanRef,
  entityOfConcernRef?, targetRefs[]?,        // exactly one subject branch is present
  groundingHolonRef, referencePlaneRef,
  claimScopeRef, EvaluationWindow,
  BaselineSet, BaselineBindingRef, FreshnessWindows,
  CNSpecRef.edition, CGSpecRef.edition, ComparatorSpecRef.edition,
  SCPRef.edition?, MinimalEvidenceRef.edition?,             // echoed iff used/pinned in the plan
  UNM_id?, NormalizationMethodId[]?, NormalizationMethodInstanceId[]?, // echoed iff used in the plan
  OutcomeRefs,                              // selected-set / archive outcomes (as refs to selector outputs)
  EpsilonDominance?,                        // echoed when used
  AbstainReasons[]?,                        // ids/labels (policy-bound) for abstain/degrade; refusal paths included
  TelemetrySummary? := ⟨IlluminationSummary?, coverage?, regret?⟩,  // report-only by default; promotion requires CAL policy-id pins
  GuardOutcomeTraceRef?,                    // pass/degrade/abstain trace + cited reasons (policy-bound)
  EvidenceTrace := ⟨EvidenceGraphId, PathId[], PathSliceId?⟩,
  CrossingPins?,                            // Bridge/CL/Φ/Ψ/Φ_plane pins, when crossings are invoked
  EditionPinsDelta?,                        // explicit list of edition pins actually active during the run
  PolicyPinsDelta?,                         // explicit list of policy-ids actually active during the run
  RSCRRefs[]                                // parity RSCR test ids / trigger emissions
⟩`

The report carries the exact `ParityPlanRef` and echoes the `BaselineBindingRef` used in that edition. For example, if `<PumpParityPlan, E4>` used `PumpBaselineBinding-E7` and a later `E5` changes the binding or comparator, an old report still resolves `E4` and `PumpBaselineBinding-E7`. A missing historical plan edition or binding is an unresolved required input; it is never replaced with the current value.

**Naming discipline.**

* Heads reuse existing U‑types and LEX discipline; no new “strategy” primitive is minted here.
* The older labels `ParityPlan@Context` and `ParityReport@Context` are retired. The suffix named neither identity nor comparison basis; current records are `ParityPlan` and `ParityReport`, with all operative conditions carried in explicit fields and exact refs.
* Tech/Plain twins follow E.10 rules (no drift‑inducing synonyms in Tech).

#### G.9:4.2 — Parity planning (one exact `U.WorkPlan`)

Planning is the act of making the parity run *reproducible by construction*:

1. **Fix the baseline set.** Choose the exact `BaselineSet` (MethodFamilies, and optionally GeneratorFamilies) used as the comparison baseline. When SoS-log or source-maturity values change baseline eligibility or interpretation, cite `SoS‑LOGBundleId?` and the source-maturity ids by reference; acceptance-gate thresholds remain in `G.4` Acceptance.
2. **Bind subject, scope, and evaluation window.** Choose exactly one subject branch: one `entityOfConcernRef`, or exact `targetRefs[]` under their existing kinds and editions. For G.5 families, use `MethodFamilyRowRef` or `GeneratorFamilyRowRef`, not a bare lineage id. Then fix `groundingHolonRef`, `referencePlaneRef = ReferencePlane`, one exact `ClaimScope`, and `EvaluationWindow`; record them without silent widening, narrowing, collapse of an EntityOfConcern into the grounding holon, or window drift.
3. **Define baseline-set reference.** Declare what counts as the baseline and how it applies to the selected subject in `BaselineBindingRef` (for example, through an EvidenceGraph path slice or an upstream shipped package or publication-record id). If `BaselineSet` also supplies the exact compared targets, say so and use the same refs by value; otherwise keep baseline and subject refs distinct.
4. **Equalise window (and budget, if pinned).** Declare a single `FreshnessWindows` and apply it across all baselines; if `Budgeting` is used/pinned, it MUST be shared/pinned across baselines as well.

   When specialization is part of the parity claim, the same plan should also hold constant the declared task family or target scope cut, the work-measure threshold target, adaptation budget, prior exposure declaration, and freshness window; if transfer, retention, downstream exploitation efficiency, downside field, or corridor entry are part of the claim, those pins should be explicit as well, including the baseline relative to which corridor entry is being claimed.

5. **Pin governance, CSLC comparability and admissibility references, and comparator references.** `CNSpecRef`, `CGSpecRef`, and `ComparatorSpecRef` are referenced with explicit edition pins.
6. **Pin measurement/comparator definitions (conditional).** Where parity depends on mode‑specific definition records (e.g., DHC/QD/OEE), pin the relevant definition ids/editions/policies. The minimum required pins are declared by the applicable `Extensions` blocks (e.g., `G.9:Ext.DHCParityPins`, `G.9:Ext.QDArchiveParity`, `G.9:Ext.OEEParity`) and the referenced records they cite.
7. **Bind comparator choice to CG-Spec (CSLC comparability and admissibility).** Any numeric comparison or aggregation MUST be CSLC‑admissible and cite the corresponding CG‑Spec entry (via `ComparatorSpecRef`). If Characteristics differ by unit, scale, or space, the plan MUST declare the ids used for “normalize, then compare” (`UNM_id?`, `NormalizationMethodId[]?`, `NormalizationMethodInstanceId[]?`) — ids only; semantics are defined elsewhere.
8. **Declare order & PortfolioMode semantics.** Parity MUST preserve set‑return semantics; `PortfolioMode` and `DominanceRegime` are either explicitly pinned or cited through `G.Core.DefaultGoverningDefinitionIndex`. IlluminationSummary/coverage/regret remain telemetry unless a CAL policy explicitly promotes them (policy‑id pinned & recorded).
9. **Attach planned fillings when applicable.** If parity depends on planned slot fillings, this WorkPlan contains the relevant A.15.3 rows in `PlannedFillingRows[]`; each row points to a declaration member defined by its own pattern and has no independent reference or identity. Omit the field when no such row is needed.
10. **Publish crossing pins (when invoked).** When expressions have distinct recovered F.17 meanings, establish the required F.9 relation and publish its Bridge and CL pins; ReferencePlane or Kind crossings cite their own exact crossing basis and pins. Penalties affect `R_eff` only (invariants pinned through `G.Core`).

#### G.9:4.3 — Execution protocol (run‑time / selector‑adjacent)

Execution is **one run** under the pinned plan:

1. **Validate CSLC references and pins.** Validate the cited CSLC comparability and admissibility references, active pins, and witnesses; run eligibility or acceptance checks under the plan’s `TaskSignature (S2)` and refuse or abstain on non-admissible operations (record trace; no “fourth status”). If a live `A.21` gate consumes this check, cite its `GateDecisionRef`/`DecisionLogRef`; do not create a `G.9`-local CSLC gate.
2. **Invoke selection/dispatch.** Apply **G.5** under the plan’s pinned refs and emit selector outputs in a form consistent with G.5’s `PortfolioMode` and selected-set semantics.

   When parity is comparing bounded specialization, the report should echo the active specialization profiles or equivalent pins so readers can recover the work-measure threshold target, prior exposure, budget-to-threshold, post-threshold efficiency when relevant, transfer, retention, downside field, and any corridor-entry baseline or evidence note from the parity object itself rather than from later narrative explanation.

3. **Record the comparability mapping when used.** If `UNM_id?`, `NormalizationMethodId[]?`, or `NormalizationMethodInstanceId[]?` was declared, echo it in `ParityReport` or its explicit pins delta. Record the ids and any scoped notes required by the cited specification in the audit pins and SCR; cite the applicable `PathId` values.
4. **Publish trace.** Emit `ParityReport` with the exact `ParityPlanRef`, its `BaselineBindingRef`, EvidenceGraph citations, and all active edition and policy-id pins, so the run can be checked and run again.
5. **Emit telemetry hooks (optional, report‑only).** When telemetry is produced, it is emitted as telemetry pins/events for refresh wiring (not as a silent change in dominance interpretation).

#### G.9:4.3a — Worked parity slice

**Ordinary case: compare two pump-triage method rows.** The team from the G.5 example wants a reproducible comparison of the two exact selector-row editions, not a claim that one Method is universally better. Both rows use the same scheme, units, and ReferencePlane, so no normalization or crossing branch is needed.

```text
ParityPlanRef = <PumpTriageParity, E1>
targetRefs = [<ThresholdTrendReview-local, R3>,
              <SpectralResidualReview-local, R2>]
entityOfConcernRef = absent
groundingHolonRef = PumpMaintenanceProgram-H1
referencePlaneRef = PumpVibrationTriage-RP1
claimScopeRef = PumpFleet-F7-VibrationTriageClaims-E1
EvaluationWindow = 2026-08-01T00:00Z .. 2026-08-07T23:59Z
BaselineSet = [<ThresholdTrendReview-local, R3>,
               <SpectralResidualReview-local, R2>]
BaselineBindingRef = PumpTriageBaselineBinding-E1
FreshnessWindows = { sensorSeries: at-most-24h-old-at-run,
                     evidencePath: at-most-72h-old-at-run }
CNSpecRef.edition = PumpCN-E2
CGSpecRef.edition = PumpCG-E4
ComparatorSpecRef.edition = PumpTriageComparator-E3
ParityPinSet = [PumpVibrationMeasureSpec-E2]
EvidenceGraphId = PumpTriageEvidence-E5
PathId[] = [PumpReadings-P7, ComparatorRun-P3]
PathSliceId = PumpParitySlice-S2
expected selector result = unordered Shortlist
```

The plan explicitly says that `BaselineSet` and `targetRefs[]` contain the same two row refs. `EvaluationWindow` bounds the observations and results included in the comparison. `FreshnessWindows` asks a different question at run or reuse time: whether each required input and evidence path is still recent enough to rely on. A report from this run carries `parityPlanRef=<PumpTriageParity, E1>`, `BaselineBindingRef=PumpTriageBaselineBinding-E1`, the same evidence path, and the unordered `Shortlist`; it does not invent a scalar winner. A cold reader can therefore recover the subject, comparison boundary, two window meanings, measurement and comparator editions, and evidence without opening a causal, crossing, assurance, telemetry, or publication branch.

**Conditional specialization case.** Loop-engineering parity may add further pins after the ordinary comparison boundary above is complete. An evaluation program, benchmark script, or dashboard is part of the evaluation or comparison procedure; it is not the Characteristic being improved.

- Two agentic search setups both claim bounded specialization on the same declared task family.
- Their `ParityPlan` also pins the same threshold target, adaptation budget, prior-exposure declaration, and corridor-entry baseline. One setup reaches threshold sooner but shows low retention and no transfer. The other reaches threshold later, but carries reusable transfer and lower downside field.
- Their CSLC-admissible `ParityReport` states what was held constant, which signals remained telemetry, and why the outcome stays a selected set or partial order rather than collapsing into a scalar winner. These specialization values extend the complete comparison boundary; they do not replace its subject, scope, windows, baseline binding, comparator editions, or evidence.

#### G.9:4.3b — Conditional causal method rung parity

Use this extension only when a parity report compares causal methods or causal-use claims. Start with a cheap screen and stop at degraded parity or abstention when the methods answer different questions.

```text
CausalRungParityScreen:
  comparedMethodsRef
  targetCausalityLadderRungSet
  causalSupportComponentTypeSet
  sameEstimand: yes | no | unclear
  sameOutcomeWindow: yes | no | unclear
  sameTransportEndpoints: yes | no | unclear
  cheapParityStop:
    comparableEnoughForFullRecord |
    crossRungDegrade |
    crossSupportComponentsDegrade |
    differentEstimandAbstain |
    differentOutcomeWindowAbstain |
    differentEndpointsAbstain |
    returnToC28
```

`causalSupportComponentTypeSet` records which methods rely on evidence paths/data regimes, identification, estimates, direct counterfactual sampling, simulation, or transport. Difference is not an automatic ban, but it must be exposed and bridged; one label cannot make unlike components equivalent.

Open the full record only when comparison remains meaningful:

```text
CausalMethodRungParityRecord:
  comparedMethodsRef
  causalUseQuestionRef?: CausalUseQuestionRef
  targetCausalUseClaimKind: CausalUseClaimKind
  targetCausalityLadderRung: CausalityLadderRung
  causalEstimandRef: CausalEstimandRef
  declaredCausalityLadderBridgeOrLossRef?
  interventionBudgetOrActionSetRef?
  causalSupportComponentRefs: CausalSupportComponentRefs
  declaredCausalSupportLossRef?
  causalUseSupportResultRef?: CausalUseSupportResultRef
  causalFollowUpWindowRef
  outcomeMeasureRef
  sourcePopulationRef?
  targetPopulationRef?
  sourceDomainRef?
  targetDomainRef?
  sourceEnvironmentRef?
  targetEnvironmentRef?
  sourceDataGeneratingRegimeRef?
  targetDataGeneratingRegimeRef?
  transportabilityResultRef?
  estimateResultRef?
  parityVerdict: parityEstablished | degraded | abstain
  supportedParityUse
  unsupportedParityUse
```

The record names every changed transport endpoint that matters; population and semantic scheme do not substitute for domain, environment, or data-generating regime. Different rungs, estimands, windows, endpoints, or support components require a bridge/loss, degraded parity, or abstention. G.9 makes the parity conclusion; C.28 supplies the cited causal-support result and does not authorize the benchmark conclusion.

#### G.9:4.9 — Extensions (pattern‑scoped; non‑core)

Most working readers can stop after `G.9:4.3a`. The blocks below are binding-only wiring records used only when the corresponding parity mode is actually active.

The following blocks store **wiring only** (pins/refs/policy‑ids, relevant triggers, and `Uses`), while semantics remains defined in the referenced patterns.

**GPatternExtension block: `G.9:Ext.CrossTraditionParity`**
**GPatternExtension: CrossTraditionParity**
* **PatternScopeId:** `G.9:Ext.CrossTraditionParity`
* **GPatternExtensionId:** `CrossTraditionParity`
* **GPatternExtensionKind:** `DisciplineSpecific`
* **GoverningPatternId:** `G.7`
* **Uses:** `{G.7, F.9, E.18, A.21}`
* **⊑/⊑⁺:** `∅`
* **RequiredPins/EditionPins/PolicyPins (minimum; conditional on use):**
  * `BridgeId/BridgeCardId[]`
  * `BridgeMatrixId?`
  * `CalibrationLedgerId?` / `BCT.id?`
  * `RegressionSetId?` / `SentinelId[]?` *(when sentinel wiring is used)*
  * `CL/CL^k/CL^plane`
  * `Φ(CL) policy-id`, `Φ_plane policy-id`, `Ψ(CL^k) policy-id?`
  * `CrossingBundleId?`
* **RSCRTriggerSetIds:** `{GCoreTriggerSetId.BridgeCalibrationKit}` *(preferred; expands in `G.Core`)*
* **RSCRTriggerKindIds (delta, if any):** `∅`
* **Notes (wiring-only):** This block does not define CL/Φ/Ψ semantics; it only requires the pins needed to cite calibration records and crossing visibility bundles.

**GPatternExtension block: `G.9:Ext.SoSLogGuardNarration`**
**GPatternExtension: SoSLogGuardNarration**
* **PatternScopeId:** `G.9:Ext.SoSLogGuardNarration`
* **GPatternExtensionId:** `SoSLogGuardNarration`
* **GPatternExtensionKind:** `MethodSpecific`
* **GoverningPatternId:** `C.23`
* **Uses:** `{C.23, G.6, G.4}`
* **⊑/⊑⁺:** `∅`
* **RequiredPins/EditionPins/PolicyPins (minimum; conditional on use):**
  * `SoSLogRuleId[]` / `BranchId[]` *(ids as cited labels; semantics come from `C.23`)*
  * `FailureBehaviorPolicyId/SoSLogBranchId`
  * `EvidenceTrace.PathId[]` / `PathSliceId?`
  * `AcceptanceClauseId[]` *(when referenced)*
* **RSCRTriggerKindIds:** `{RSCRTriggerKindId.PolicyPinChange, RSCRTriggerKindId.EvidencePathOrSourceRelationEdit, RSCRTriggerKindId.MaturityRungChange, RSCRTriggerKindId.TelemetryDelta}`
* **Notes (wiring-only):** Explains **why** a parity run degraded/abstained by citing SoS‑LOG ids and evidence paths; does not redefine guard semantics.

**GPatternExtension block: `G.9:Ext.DHCParityPins`**
**GPatternExtension: DHCParityPins**
* **PatternScopeId:** `G.9:Ext.DHCParityPins`
* **GPatternExtensionId:** `DHCParityPins`
* **GPatternExtensionKind:** `MethodSpecific`
* **GoverningPatternId:** `C.21`
* **Uses:** `{C.21}`
* **⊑/⊑⁺:** `∅`
* **Required replay values and pins (minimum; conditional on DHC parity):**
  * `DisciplineRef`
  * `IntendedUse`
  * `ClaimScopeRef`
  * `ComparisonBasis`
  * `CharacteristicRef.edition`
  * `ScaleRef.edition`
  * `UnitRef.edition?`
  * `DHCMethodRef.edition`
  * `MethodRef`
  * `MethodDescriptionRef.edition?`
  * `MeasurementModelRef.edition?`
  * `CalibrationBasisRef?`
  * `TimeOrPopulationBasis`
  * `DHCDefinitionSetRef.edition?`
  * `TargetSliceRef?`
  * `DistanceDefRef.edition?`
* **RSCRTriggerKindIds:** `{RSCRTriggerKindId.EditionPinChange, RSCRTriggerKindId.PolicyPinChange, RSCRTriggerKindId.EvidencePathOrSourceRelationEdit}`
* **Notes (wiring-only):** Carry exactly the active fields of the C.21 replay basis. `TargetSliceRef` appears only when the parity computation consumes that A.2.6 selection and states its relation to `ClaimScopeRef`. Compatible same-semantics readings use the admitted C.16 comparison basis directly; actual distinct-local-sense use also cites the obtaining F.9 relation, direction, admitted use, and loss. C.21 defines the DHC semantics.

**GPatternExtension block: `G.9:Ext.QDArchiveParity`**
**GPatternExtension: QDArchiveParity**
* **PatternScopeId:** `G.9:Ext.QDArchiveParity`
* **GPatternExtensionId:** `QDArchiveParity`
* **GPatternExtensionKind:** `MethodSpecific`
* **GoverningPatternId:** `C.18`
* **Uses:** `{C.18, C.19, G.5}`
* **⊑/⊑⁺:** `∅`
* **RequiredPins/EditionPins/PolicyPins (minimum; conditional on use):**
  * `DescriptorMapRef.edition`
  * `DistanceDefRef.edition`
  * `CharacteristicSpaceRef.edition?` *(when discretisation/topology is referenced)*
  * `EmitterPolicyRef`
  * `InsertionPolicyRef`
* **RSCRTriggerKindIds:** `{RSCRTriggerKindId.EditionPinChange, RSCRTriggerKindId.PolicyPinChange, RSCRTriggerKindId.TelemetryDelta}`
* **Notes (wiring-only):** Post‑2015 QD families are referenced here only as wiring + edition/policy pin obligations (semantics come from `C.18`/`C.19`/`G.5`).

**GPatternExtension block: `G.9:Ext.OEEParity`**
**GPatternExtension: OEEParity**
* **PatternScopeId:** `G.9:Ext.OEEParity`
* **GPatternExtensionId:** `OEEParity`
* **GPatternExtensionKind:** `MethodSpecific`
* **GoverningPatternId:** `C.19`
* **Uses:** `{C.19, G.5}`
* **⊑/⊑⁺:** `∅`
* **RequiredPins/EditionPins/PolicyPins (minimum; conditional on use):**
  * `TransferRulesRef.edition`
  * `EnvironmentValidityRegionId`
  * `ExplorationBudgetPolicyId?`
  * `EvidenceTrace.PathSliceId?` *(for transfer‑keyed events)*
* **RSCRTriggerKindIds:** `{RSCRTriggerKindId.EditionPinChange, RSCRTriggerKindId.PolicyPinChange, RSCRTriggerKindId.TelemetryDelta}`
* **Notes (wiring-only):** Open‑ended parity is expressed as policy/edition pins + telemetry wiring, not as new core norms.

