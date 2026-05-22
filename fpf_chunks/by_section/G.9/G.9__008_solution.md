---
chunk_kind: "child"
pattern_id: "G.9"
pattern_title: "Parity / Benchmark Harness"
section_id: "G.9:4"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/G.9/G.9__008_solution.md"
commit_sha: "725f0b7b372754cda3f6f4e15184215da568fc4d"
heading_path:
  - "G.9 — Parity / Benchmark Harness"
  - "G.9:4 — Solution"
line_start: 72841
line_end: 73162
dependencies:
  - "A.19"
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
  `RSCRTriggerKindId.EvidenceSurfaceEdit`,
  `RSCRTriggerKindId.PenaltyPolicyEdit`,
  `RSCRTriggerKindId.BaselineBindingEdit`,
  `RSCRTriggerKindId.TelemetryDelta`
  }
  *(Pattern‑local deltas; cross‑tradition / bridge‑calibration causes are wired via `G.9:Ext.CrossTraditionParity` and MUST NOT over‑trigger baseline (within‑context) parity runs.)*

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
  `FreshnessWindows`,
  `BaselineSet`, `BaselineBindingRef`,
  `ParityPinSet`,
  `PlanItemRefs[]?`,
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

**(1) `ParityPlan@Context`** *(WorkPlanning record)*
A plan that fixes *what is being compared* and *under what pinned conditions*.

Minimal fields (conceptual; ids/pins only):

`ParityPlan@Context := ⟨
  ParityPlanId(UTS),
  CGFrameId?,                              // or CG-FrameContext id/scope anchor cited by the referenced frame records
  describedEntity := ⟨GroundingHolon, ReferencePlane⟩,
  UNM_id?, NormalizationMethodId[]?, NormalizationMethodInstanceId[]?, // when “normalize, then compare” is required (ids only; semantics come from CN‑Spec / UNM)
  EpsilonDominance?,                       // optional ε-front thinning (ε≥0; id/param; pinned when used)
  PortfolioMode?, DominanceRegime?,         // may be explicit or inherited via DefaultGoverningDefinition (semantics follow G.5)
  ParityContextId,
  BaselineSet,                            // method-family / generator-family baseline scope (ids; notation-independent)
  BaselineBindingRef,                      // evidence-backed baseline-set reference that says what counts as baseline
  FreshnessWindows,
  CNSpecRef.edition, CGSpecRef.edition, ComparatorSpecRef.edition, // edition-pinned refs
  SCPRef.edition?,                         // optional (when a specific SCP profile must be pinned/cited)
  MinimalEvidenceRef.edition?,             // optional (when CG-Spec exposes minima profiles by ref)
  Budgeting?,
  ParityPinSet,
  PlanItemRefs[]?                          // references to A.15.3 SlotFillingsPlanItem (planned baseline), when parity depends on planned slot fillings
⟩`

**(2) `ParityPinSet`** *(pin set)*
A declared set of pins required for reproducibility and audit (editions + policy‑ids + UTS/Path pins).
The concrete contents are *pattern-local* (G.9 declares the pin set), but must satisfy the *core pin discipline* via `G.Core`.

**(3) `ParityReport@Context`** *(UTS publication record; work-result or audit-facing publication record only when the neighboring source exists)*
A UTS-publishable parity publication record produced by running a `ParityPlan@Context`. By itself it is not a dated `U.Work` occurrence, audit performance, evidence path, assurance result, or gate decision; those claims require `A.15`/`A.15.1`, `A.10`/`G.6`, `B.3`, or `A.21` respectively.

`ParityReport@Context := ⟨
  ParityReportId(UTS),
  ParityPlanId,
  BaselineSet, FreshnessWindows,
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

**Naming discipline.**

* Heads reuse existing U‑types and LEX discipline; no new “strategy” primitive is minted here.
* Tech/Plain twins follow E.10 rules (no drift‑inducing synonyms in Tech).

#### G.9:4.2 — Parity planning (design‑time / WorkPlanning)

Planning is the act of making the parity run *reproducible by construction*:

1. **Fix the baseline set.** Choose the `BaselineSet` (MethodFamilies, and optionally GeneratorFamilies) to compare; where parity context matters, cite `SoS‑LOGBundleId?` and source-maturity ids by reference (acceptance-gate thresholds remain in `G.4` Acceptance).
2. **Bind scope.** Fix `describedEntity := ⟨GroundingHolon, ReferencePlane⟩` and record it in the plan (no silent widening/narrowing).
3. **Define baseline-set reference.** Declare what counts as “baseline set” and how it is cited (e.g., `BaselineBindingRef`, the evidence-backed baseline-set reference, pointing to an EvidenceGraph path slice or an upstream shipped package or publication-record id).
4. **Equalise window (and budget, if pinned).** Declare a single `FreshnessWindows` and apply it across all baselines; if `Budgeting` is used/pinned, it MUST be shared/pinned across baselines as well.

When specialization is part of the parity claim, the same plan should also hold constant the declared task family or target scope cut, the work-measure threshold target, adaptation budget, prior exposure declaration, and freshness window; if transfer, retention, downstream exploitation efficiency, downside field, or corridor entry are part of the claim, those pins should be explicit as well, including the baseline relative to which corridor entry is being claimed.

5. **Pin governance, CSLC comparability and admissibility references, and comparator references.** `CNSpecRef`, `CGSpecRef`, and `ComparatorSpecRef` are referenced with explicit edition pins.
6. **Pin measurement/comparator definitions (conditional).** Where parity depends on mode‑specific definition records (e.g., DHC/QD/OEE), pin the relevant definition ids/editions/policies. The minimum required pins are declared by the applicable `Extensions` blocks (e.g., `G.9:Ext.DHCParityPins`, `G.9:Ext.QDArchiveParity`, `G.9:Ext.OEEParity`) and the referenced records they cite.
7. **Bind comparator choice to CG-Spec (CSLC comparability and admissibility).** Any numeric comparison or aggregation MUST be CSLC‑admissible and cite the corresponding CG‑Spec entry (via `ComparatorSpecRef`). If Characteristics differ by unit, scale, or space, the plan MUST declare the ids used for “normalize, then compare” (`UNM_id?`, `NormalizationMethodId[]?`, `NormalizationMethodInstanceId[]?`) — ids only; semantics are defined elsewhere.
8. **Declare order & PortfolioMode semantics.** Parity MUST preserve set‑return semantics; `PortfolioMode` and `DominanceRegime` are either explicitly pinned or cited through `G.Core.DefaultGoverningDefinitionIndex`. IlluminationSummary/coverage/regret remain telemetry unless a CAL policy explicitly promotes them (policy‑id pinned & recorded).
9. **Attach planned baselines (when applicable).** If parity depends on planned slot fillings, the plan cites the relevant `SlotFillingsPlanItem` refs (A.15.3) via `PlanItemRefs[]` rather than embedding a competing baseline object (nil‑elision when unused).
10. **Publish crossing pins (when invoked).** Cross-Context or cross-plane/Kind reuse requires explicit Bridge/CL/Φ pins; penalties affect `R_eff` only (invariants pinned through `G.Core`).

#### G.9:4.3 — Execution protocol (run‑time / selector‑adjacent)

Execution is **one run** under the pinned plan:

1. **Validate CSLC references and pins.** Validate the cited CSLC comparability and admissibility references, active pins, and witnesses; run eligibility or acceptance checks under the plan’s `TaskSignature (S2)` and refuse or abstain on non-admissible operations (record trace; no “fourth status”). If a live `A.21` gate consumes this check, cite its `GateDecisionRef`/`DecisionLogRef`; do not create a `G.9`-local CSLC gate.
2. **Invoke selection/dispatch.** Apply **G.5** under the plan’s pinned refs and emit selector outputs in a form consistent with G.5’s `PortfolioMode` and selected-set semantics.

When parity is comparing bounded specialization, the report should echo the active specialization profiles or equivalent pins so readers can recover the work-measure threshold target, prior exposure, budget-to-threshold, post-threshold efficiency when relevant, transfer, retention, downside field, and any corridor-entry baseline or evidence note from the parity object itself rather than from later narrative explanation.

3. **Record comparability mapping (when used).** If `UNM_id?` / `NormalizationMethodId[]?` / `NormalizationMethodInstanceId[]?` were declared, **echo them** in `ParityReport@Context` (or in its explicit pins deltas) and record their ids (and any scoped notes required by the cited governing spec ref) in audit pins/SCR; cite the applicable `PathId`s.
4. **Publish trace.** Emit `ParityReport@Context` with EvidenceGraph citations and all active pins (editions/policy‑ids), so the run can be re‑checked and re‑run.
5. **Emit telemetry hooks (optional, report‑only).** When telemetry is produced, it is emitted as telemetry pins/events for refresh wiring (not as a silent change in dominance interpretation).

#### G.9:4.3a — Worked parity slice

- Two agentic search setups both claim bounded specialization on the same declared task family.
- The `ParityPlan` pins the same freshness window, threshold target, adaptation budget, prior-exposure declaration, comparator editions, and corridor-entry baseline. One setup reaches threshold sooner but shows low retention and no transfer. The other reaches threshold later, but carries reusable transfer and lower downside field.
- A CSLC-admissible `ParityReport@Context` therefore states what was held constant, which signals remained telemetry, and why the outcome stays a governed selected set or partial order rather than collapsing into a scalar winner. The reader can recover the practical comparison from the parity slice itself before reading any optional wiring blocks.

#### G.9:4.3b — Conditional causal method rung parity

Use this conditional extension only when a parity report compares causal methods or causal-use claims. The parity report starts with a cheap screen and may stop at degraded parity or abstain when methods plainly answer different causal uses.

```text
CausalRungParityScreen:
  comparedMethodsRef: ComparedMethodSetRef
  targetCausalityLadderRungSet: {CausalityLadderRung...}
  causalEvidenceSupportBasisSet: {CausalEvidenceSupportBasis...}
  sameEstimand: yes | no | unclear
  sameOutcomeWindow: yes | no | unclear
  cheapParityStop: CausalRungParityScreenOutcome
```

```text
CausalRungParityScreenOutcome =
    comparableEnoughForFullRecord |
    crossRungDegrade |
    crossSupportBasisDegrade |
    differentEstimandAbstain |
    differentOutcomeWindowAbstain |
    returnToC28
```

Open the full `CausalMethodRungParityRecord` only when `CausalRungParityScreenOutcome = comparableEnoughForFullRecord`. Other outcomes are admissible cheap stops: degraded parity, abstain, or apply `C.28`, without fabricating a full parity record.

`targetCausalityLadderRungSet` is the first parity check. Here `CausalityLadderRung` is a cited causal-use taxonomy value, not a maturity level, upgrade ladder, or superiority scale. If the set has more than one causality-ladder rung and no declared bridge and loss makes the comparison meaningful, the screen returns `crossRungDegrade` rather than treating the methods as peers.

`causalEvidenceSupportBasisSet` is the second parity check. If methods depend on different causal support bases and no declared support-loss or bridge makes the comparison meaningful, the screen returns `crossSupportBasisDegrade`.

`sameEstimand = no` returns `differentEstimandAbstain` unless the report names a shared estimand, a bridge and loss relation, or a reason the comparison is intentionally non-parity. A scalar parity result is not admissible across different estimands by default.

`sameOutcomeWindow = no` returns `differentOutcomeWindowAbstain` unless the report pins a common follow-up window or declares the window loss. A method that wins at one horizon is not parity-superior at another horizon by default.

Parity reports comparing causal methods then carry a `CausalMethodRungParityRecord`:

```text
CausalMethodRungParityRecord:
  comparedMethodsRef
  causalUseQuestionRef?: U.CausalUseQuestion
  targetCausalUseClaimKind: CausalUseClaimKind
  targetCausalityLadderRung: CausalityLadderRung
  estimandRef: U.CausalEstimand
  declaredCausalityLadderBridgeOrLossRef?
  interventionBudgetOrActionSetRef?
  causalEvidenceSupportBasis: CausalEvidenceSupportBasis
  declaredCausalEvidenceSupportLossRef?
  causalUseSupportRecordRef?
  causalUseSupportVerdict?: CausalUseSupportVerdict
  causalFollowUpWindowRef
  outcomeMeasureRef
  sourcePopulationRef?
  targetPopulationRef?
  causalTransportabilityProfileRef?
  estimationValidityClassRef?
  causalParameterEstimationProfileRef?
  parityVerdict: parityEstablished | degraded | abstain
  supportedParityUse
  unsupportedParityUse
```

Parity reports comparing causal methods fill this record so the "same" claims are checkable by fields rather than prose:

- comparedMethodsRef;
- targetCausalityLadderRung;
- targetCausalUseClaimKind: CausalUseClaimKind;
- estimandRef;
- interventionBudgetOrActionSetRef;
- causalEvidenceSupportBasis;
- causalUseSupportRecordRef and causalUseSupportVerdict when a `C.28` support record or verdict is being consumed;
- causalFollowUpWindowRef;
- outcomeMeasureRef;
- declaredCausalityLadderBridgeOrLossRef where causality-ladder rungs differ;
- causalTransportabilityProfileRef where source population, target population, domain, context, or evidence regime differs;
- causalParameterEstimationProfileRef where estimation validity, uncertainty, nuisance handling, or sensitivity differs;
- degraded or abstain posture where parity cannot be established.

Causality-ladder parity is a degrade/abstain condition, not a universal comparison ban. Cross-rung method comparisons must name `declaredCausalityLadderBridgeOrLossRef` and cannot become superiority claims by default.

What changes in practice: one benchmark cannot compare a predictive model, an interventional action/effect question optimizer, and a counterfactual comparison question strategy as one undifferentiated "method improvement" set.

What this does not authorize: `G.9` does not decide causal identification, causal fairness, or counterfactual sampling realizability; it keeps parity/benchmark harness authority and sends causal-use support to `C.28`.

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
* **RSCRTriggerKindIds:** `{RSCRTriggerKindId.PolicyPinChange, RSCRTriggerKindId.EvidenceSurfaceEdit, RSCRTriggerKindId.MaturityRungChange, RSCRTriggerKindId.TelemetryDelta}`
* **Notes (wiring-only):** Explains **why** a parity run degraded/abstained by citing SoS‑LOG ids and evidence paths; does not redefine guard semantics.

**GPatternExtension block: `G.9:Ext.DHCParityPins`**
**GPatternExtension: DHCParityPins**
* **PatternScopeId:** `G.9:Ext.DHCParityPins`
* **GPatternExtensionId:** `DHCParityPins`
* **GPatternExtensionKind:** `MethodSpecific`
* **GoverningPatternId:** `C.21`
* **Uses:** `{C.21}`
* **⊑/⊑⁺:** `∅`
* **RequiredPins/EditionPins/PolicyPins (minimum; conditional on use):**
  * `DHCMethodRef.edition`
  * `DHCMethodSpecRef.edition?` *(when the cited DHC method spec distinguishes method vs method-spec editions)*
* **RSCRTriggerKindIds:** `{RSCRTriggerKindId.EditionPinChange, RSCRTriggerKindId.PolicyPinChange, RSCRTriggerKindId.EvidenceSurfaceEdit}`
* **Notes (wiring-only):** Declares the pins required to make DHC‑based parity reproducible and RSCR‑refreshable; semantics of DHC lives in `C.21`.

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

