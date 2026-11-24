---
chunk_kind: "child"
pattern_id: "G.9"
pattern_title: "Parity and Benchmark Harness"
section_id: "G.9:4"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/G.9/G.9__006_solution.md"
commit_sha: "cadc8eb15721be464193af85206e345f34a64b04"
heading_path:
  - "G.9 — Parity and Benchmark Harness"
  - "G.9:4 — Solution"
line_start: 140605
line_end: 140988
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
  - "pairwise relations"
  - "parity harness"
  - "selection when commissioned"
---

### G.9:4 — Solution
#### G.9:4.0 — G.Core linkage (normative)

This pattern binds to **G.Core** through the following manifest.

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
  *(Pattern-local deltas; cross-tradition or Bridge-calibration causes are wired via `G.9:Ext.CrossTraditionParity` and MUST NOT over-trigger parity runs that use one already recovered meaning and ReferencePlane.)*

* `DefaultsConsumed` := {
  `DefaultId.DominanceRegime`,
  `DefaultId.PortfolioMode`,
  `DefaultId.GammaFoldForR_eff`
  }
  *(Use each default when its operation needs it. G.Core.DefaultGoverningDefinitionIndex identifies the governing definitions CC‑G5.28, CC‑G5.23 and CC‑G5.4 respectively.)*

* `CorePinSetIds` := {
  `GCorePinSetId.PartG.AuthoringMinimal`,
  `GCorePinSetId.PartG.CrossingVisibilityPins`
  }

* `CorePinsRequired` *(pattern delta; pin names only; all are id‑valued unless noted)* := {
  `ComparatorSpecRef.edition`,
  `TaskSignatureRef?`, `TaskMapRef?`, *(when a selector consumes the parity result; TaskMapRef only when its G.4 CAL gates are current)*
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

**(1) `ParityPlan`** *(one `U.WorkPlan` episteme; `ParityPlan` is the local application name)*
A plan that fixes *what is being compared* and *under what pinned conditions*.

Minimal fields (conceptual; ids/pins only):

```text
ParityPlan := ⟨
  ParityPlanId(UTS),                       // continuing plan lineage
  planEdition,                            // one immutable edition
  CGFrameId?,                              // exact cited CG frame when the plan depends on one
  TaskSignatureRef?, TaskMapRef?,           // conditional G.5 input; TaskMap only for current G.4 CAL gates
  entityOfConcernRef? := EntityOfConcernRef, // one-EntityOfConcern branch only
  targetRefs[]?,                            // exact-target branch only; existing kinds and editions
  groundingHolonRef?,                       // required for the empirical grounding used by this claim
  referencePlaneRef := ReferencePlane,
  claimScopeRef := ClaimScope,
  EvaluationWindow,
  UNM_id?, NormalizationMethodId[]?, NormalizationMethodInstanceId[]?, // when “normalize, then compare” is required (ids only; semantics come from CN‑Spec / UNM)
  EpsilonDominance?,                       // optional ε-front thinning (ε≥0; id/param; pinned when used)
  PortfolioMode?, DominanceRegime?,         // cite each when the operation uses it, explicitly or through its governing default
  BaselineSet,                            // exact alternatives serving as the baseline, under their existing kinds and applicable editions
  BaselineBindingRef,                      // evidence-backed baseline-set reference that says what counts as baseline
  FreshnessWindows,
  CNSpecRef.edition, CGSpecRef.edition, ComparatorSpecRef.edition, // edition-pinned refs
  SCPRef.edition?,                         // optional (when a specific SCP profile must be pinned/cited)
  MinimalEvidenceRef.edition?,             // optional (when CG-Spec exposes minima profiles by ref)
  Budgeting?,
  ParityPinSet,
  EvidenceGraphId, PathId[], PathSliceId?,
  PlannedFillingRows[]?                    // declaration-local A.15.3 content inside this WorkPlan; no independent row refs
⟩
```

`ParityPlanRef := <ParityPlanId, planEdition>` designates one immutable plan edition. Changing its subject, baseline binding, comparator edition, or another active value that can change the run or its interpretation creates a new `planEdition`.

When a G.5 selector consumes this comparison, pin its `TaskSignatureRef` in the plan. If that selector uses G.4 CAL gates, also pin its `TaskMapRef` and require the map's task-signature reference to match. Omit these selector inputs from a parity run that needs no selector.

A later edition may retain the lineage ID only if it continues the same plan. Earlier `ParityPlanRef` values still resolve their original editions.

Exactly one subject branch is present. Use `entityOfConcernRef` when the report compares results about one EntityOfConcern. Use `targetRefs[]` when the targets themselves are compared; each ref keeps the kind and edition defined by its existing subject pattern. In particular, a G.5 method-family target is an exact `MethodFamilyRowRef`, and a generator-family target is an exact `GeneratorFamilyRowRef`.

For example, a comparison of `<ThresholdTrendReview-local, R3>` and `<SpectralResidualReview-local, R2>` puts those two row refs in `targetRefs[]`; the plan may explicitly use the same two refs as its `BaselineSet`. A comparison of their results for `Pump-P17` instead puts `Pump-P17` in `entityOfConcernRef`, leaves `targetRefs[]` absent, and uses `BaselineBindingRef` to say how the two method rows supply results about that pump.

`BaselineSet` names the alternatives whose results provide the baseline. Keep their existing kinds. A reference identifies the applicable edition or condition when a change would affect the comparison. If the same exact alternatives are also the objects being compared, the same refs may occur in `targetRefs[]`. Otherwise `BaselineBindingRef` explains how the baseline bears on the named subject. Two service arrangements may use the same method with different allocations of work. For a comparison of those arrangements, an exact reference to the current arrangement can provide the baseline. A G.5 method-family baseline retains its exact family-row reference.

These values determine what is compared and when the parity claim is usable; do not add `ParityContextId`. If the plan relates expressions with distinct source-local meanings, first recover the exact F.17 cells and establish the required F.9 relation. A shared label, source note, or generic context identifier does not establish comparability.

**(2) `ParityPinSet`** *(pin set)*
A declared set of pins required for reproducibility and audit (editions + policy‑ids + UTS/Path pins).
G.9 specifies the contents of `ParityPinSet` under the common pin rules in `G.Core`.

**(3) `ParityReport`** *(UTS publication record; work-result or audit-facing publication record only when the neighboring source exists)*
A UTS-publishable parity publication record produced by a parity run under one `ParityPlanRef`. Work or audit occurrence claims use `A.15`/`A.15.1`; evidence-path claims use `A.10`/`G.6`; a separate named assurance claim uses `B.3`; and a gate decision uses `A.21` under its applicable profile. Keep each such occurrence, path, or result distinct from the report.

```text
ParityReport := ⟨
  ParityReportId(UTS),
  parityPlanRef := ParityPlanRef,
  entityOfConcernRef?, targetRefs[]?,        // exactly one subject branch is present
  TaskSignatureRef?, TaskMapRef?,           // echoed when the selector branch is used
  groundingHolonRef?, referencePlaneRef,    // echo the empirical ground when used
  claimScopeRef, EvaluationWindow,
  BaselineSet, BaselineBindingRef, FreshnessWindows,
  CNSpecRef.edition, CGSpecRef.edition, ComparatorSpecRef.edition,
  SCPRef.edition?, MinimalEvidenceRef.edition?,             // echoed iff used/pinned in the plan
  UNM_id?, NormalizationMethodId[]?, NormalizationMethodInstanceId[]?, // echoed iff used in the plan
  OutcomeRefs,                              // parity/comparison results; G.5 output refs only when selection is current
  EpsilonDominance?,                        // echoed when used
  AbstainReasons[]?,                        // ids/labels (policy-bound) for abstain/degrade; refusal paths included
  TelemetrySummary? := ⟨IlluminationSummary?, coverage?, regret?⟩,  // report-only by default; promotion requires CAL policy-id pins
  GuardOutcomeTraceRef?,                    // pass/degrade/abstain trace + cited reasons (policy-bound)
  EvidenceTrace := ⟨EvidenceGraphId, PathId[], PathSliceId?⟩,
  CrossingPins?,                            // Bridge/CL/Φ/Ψ/Φ_plane pins, when crossings are invoked
  EditionPinsDelta?,                        // explicit list of edition pins actually active during the run
  PolicyPinsDelta?,                         // explicit list of policy-ids actually active during the run
  RSCRRefs[]                                // parity RSCR test ids / trigger emissions
⟩
```

The report carries the `ParityPlanRef` and echoes the `BaselineBindingRef` used in that edition. For example, if `<PumpParityPlan, E4>` used `PumpBaselineBinding-E7` and a later `E5` changes the binding or comparator, an old report still resolves `E4` and `PumpBaselineBinding-E7`. A missing historical plan edition or binding is an unresolved required input; it is never replaced with the current value.

**Naming discipline.**

* Head names follow the existing kind definitions and LEX discipline.
* The older labels `ParityPlan@Context` and `ParityReport@Context` are retired. The suffix did not identify the object or the comparison basis. Use `ParityPlan` and `ParityReport`, with all operative conditions carried in explicit fields and exact refs.
* Tech/Plain twins follow E.10 rules (no drift‑inducing synonyms in Tech).

#### G.9:4.2 — Parity planning (one `U.WorkPlan`)

Start with the conclusion the report must support. Comparing how two methods perform on the same work holds that work fixed. Comparing the arrangements for providing a service can require following the different work, assistance and outcomes each arrangement produces under the same external conditions. Decide how far to follow the parts and their interaction by asking where a difference could change the recipient’s judgement. The time spent on one operation may settle a question about that operation. It may leave waiting between operations, or the work of another participant, decisive for the service as a whole.

If the comparison basis is yours to design, try keeping the proposed benchmark answers the same while varying an allowed method, use or dependence between parts. Could the recipient then need a different conclusion or a different explanation for it? Bring the missing distinction into the task, comparator or grounds for transfer. A known relation may already establish the answer throughout the intended range. If the task and comparator were supplied, check their applicability and use them. Record the conditions that make the resulting comparison repeatable:

1. **Fix the baseline set.** Choose the exact alternatives whose results will serve as the baseline, and justify their relevance to the comparison. Keep the actual kind of each alternative. When a G.5 family supplies a baseline, identify its exact method-family or generator-family row edition. If SoS-log or source-maturity values change its eligibility or interpretation, cite `SoS‑LOGBundleId?` and the source-maturity ids. G.4 Acceptance governs any applicable acceptance thresholds.
2. **Bind subject, scope, and evaluation window.** Choose exactly one subject branch: one `entityOfConcernRef`, or exact `targetRefs[]` under their existing kinds and editions. For G.5 families, use `MethodFamilyRowRef` or `GeneratorFamilyRowRef`, not a bare lineage id. Record the `ReferencePlane`, `ClaimScope` and `EvaluationWindow`. An empirical claim identifies its `groundingHolonRef`. For a comparison of two proven operation-count bounds on a formal domain, identify the bounds, their proofs and the domain. A computer that stores a proof supplies no empirical premise merely by storing it.
3. **Define baseline-set reference.** Declare what counts as the baseline and how it applies to the selected subject in `BaselineBindingRef` (for example, through an EvidenceGraph path slice or an upstream shipped package or publication-record id). If `BaselineSet` also supplies the exact compared targets, say so and use the same refs by value; otherwise keep baseline and subject refs distinct.
4. **Set common comparison conditions.** Apply one declared `FreshnessWindows` policy to all baselines. If the commission compares alternatives under a common resource allowance, pin that allowance in `Budgeting`. Preserve any difference in staffing, expenditure or assistance that defines the alternatives being compared. Under the same external demand, these differences and their consequences can be precisely what the recipient needs to understand.

    For a comparison of acquisition under equal training opportunities, hold the task family, threshold, adaptation budget, prior exposure and freshness conditions fixed as the claim requires. Identify what each candidate performed and what assistance it had. For a comparison of complete arrangements, record the training, staffing and support included in each and assess what each can deliver in the intended conditions. When transfer, retention, later efficiency, downside or corridor entry matters, keep the observations and baseline supporting that claim under C.22.1:8.

5. **Pin governance, CSLC comparability and admissibility references, and comparator references.** `CNSpecRef`, `CGSpecRef`, and `ComparatorSpecRef` are referenced with explicit edition pins.
6. **Pin measurement/comparator definitions (conditional).** Where parity depends on mode‑specific definition records (e.g., DHC/QD/OEE), pin the relevant definition ids/editions/policies. The minimum required pins are declared by the applicable `Extensions` blocks (e.g., `G.9:Ext.DHCParityPins`, `G.9:Ext.QDArchiveParity`, `G.9:Ext.OEEParity`) and the referenced records they cite.
7. **Bind comparator choice to CG-Spec.** Any numeric comparison or aggregation MUST be CSLC-admissible and cite the corresponding CG-Spec entry (`ComparatorSpecRef`). Compare corresponding coordinates on compatible scales and bases. A Pareto comparator can compare kWh with kWh and minutes with minutes in their own units. When a coordinate needs conversion or the admitted operation uses normalization, declare the applicable `UNM_id?`, `NormalizationMethodId[]?` and `NormalizationMethodInstanceId[]?` and establish that the mapping preserves the distinctions the comparator uses.
8. **Declare the required result.** An admitted A.19.CPM comparison returns relation or poset tokens. Preserve established incomparability. `CompareEligibility` can also withhold comparison if required evidence is missing. Pin the dominance regime when using dominance, including for a frontier. Pin the portfolio mode when the operation uses one. Each can cite its applicable default through `G.Core.DefaultGoverningDefinitionIndex`. IlluminationSummary, coverage and regret remain telemetry unless a cited CAL policy promotes them.
9. **Attach planned fillings when applicable.** If parity depends on planned slot fillings, this WorkPlan contains the relevant A.15.3 rows in `PlannedFillingRows[]`; each row points to a declaration member defined by its own pattern and has no independent reference or identity. Omit the field when no such row is needed.
10. **Publish the relation and its receiving use (when invoked).** For distinct recovered F.17 meanings, establish the F.9 relation and the separate bounded-use claim and matching reliance. Cite G.7 calibration, CL and policy pins when that account uses them; its summary does not decide parity admissibility. Kind correspondence also requires receiving admissibility and fresh target classification under C.3.3. A plane relation keeps its own basis. Any numerical assurance penalty follows the applicable B.3 model for the named use.

#### G.9:4.3 — Execution protocol (run‑time / selector‑adjacent)

For one run under the pinned plan, follow these steps:

1. **Validate CSLC references and pins.** Validate the cited CSLC comparability and admissibility references, active pins, and witnesses. Apply the eligibility or acceptance checks required by the pinned comparison and refuse or abstain on non-admissible operations. When using G.5, record its branch trace in its own result vocabulary and use the planned `TaskSignatureRef`. Add the matching `TaskMapRef` when that selector uses G.4 CAL gates. If a live `A.21` gate consumes this check, cite its `GateDecisionResult` and add a `DecisionLog` only when needed for audit or reuse. The profile application and its action consequence remain governed by A.21; do not create a `G.9`-local CSLC gate.
2. **Run the comparison and any required selection.** Apply the pinned comparator to the admissible comparison inputs and retain its lawful result shape in `ParityReport`. If a selector-facing result is required, apply **G.5** under the plan's exact task and conditional map refs and publish its declared outcome. An ordinary parity or benchmark report ends without G.5 when no selector result is needed.

   Under componentwise minimization, A=(8,3) and B=(10,2) trade cost against time. An admitted comparison can return the singleton `{A ∥ B}`. If A and B are all eligible candidates, both are nondominated. Add C=(7,2) and the frontier becomes `{C}` while the relation between A and B stays the same. Under a comparator that admits intervals, take A=(8,[3,4]) and B=(10,2). Every allowed value for A’s time still gives incomparability. With A’s time in [1,4], A may dominate B or the two may trade off. Report only what the approved comparison supports. If two bounds used as evidence about the same profile contradict each other, resolve that conflict before reporting a relation. If the profiles are consistent and none meets the requested limits, that can settle the eligibility question. Separately, if a required calibration is missing, apply the evidence policy. An admitted narrower comparison can return only its justified tokens. An `abstain` decision leaves the comparison slot unbound.

    For a bounded-specialization comparison, the report should include the active specialization profiles or equivalent pins so readers can recover the work-measure threshold target, prior exposure, budget-to-threshold, post-threshold efficiency when relevant, transfer, retention, downside field, and any corridor-entry baseline or evidence note from the report.

3. **Record the comparability mapping when used.** If `UNM_id?`, `NormalizationMethodId[]?`, or `NormalizationMethodInstanceId[]?` was declared, echo it in `ParityReport` or its explicit pins delta. Record the ids and any scoped notes required by the cited specification in the audit pins and SCR; cite the applicable `PathId` values.
4. **Publish trace.** Emit `ParityReport` with the `ParityPlanRef`, its `BaselineBindingRef`, conditional selector input refs, EvidenceGraph citations, and all active edition and policy-id pins, so the run can be checked and run again.

   Give the recipient the conclusion the report supports about the named methods, work or arrangements. When practice extends beyond the benchmark tasks, explain the relation that carries the conclusion to that practice, or delimit the result to the conditions compared. The distinction matters empirically: a systematic review of language-model benchmarks found widespread gaps in how their tasks and scores were related to the capabilities they claimed to measure. [Bean et al., 2025](https://proceedings.neurips.cc/paper_files/paper/2025/hash/1967e0fc3aa6cbbace562f5cb8e3954e-Abstract-Datasets_and_Benchmarks_Track.html)
5. **Emit telemetry for refresh when produced.** Publish the telemetry pins or events used for refresh. Treat the values as report-only unless a CAL policy promotes them and its ID is recorded.

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
TaskSignatureRef = PumpVibrationTriage-T1
TaskMapRef = absent                         // this G.5 case uses no G.4 CAL gate
ParityPinSet = [PumpCN-E2, PumpCG-E4, PumpTriageComparator-E3, PumpVibrationMeasureSpec-E2]
EvidenceGraphId = PumpTriageEvidence-E5
PathId[] = [PumpReadings-P7, ComparatorRun-P3]
PathSliceId = PumpParitySlice-S2
requested selector output = unordered Shortlist if selection is supported
```

The plan explicitly says that `BaselineSet` and `targetRefs[]` contain the same two row refs. `EvaluationWindow` bounds the observations and results included in the comparison. `FreshnessWindows` asks a different question at run or reuse time: whether each required input and evidence path is still recent enough to rely on.

For this example the team requests an unordered shortlist. The comparison report carries `parityPlanRef=<PumpTriageParity, E1>`, `BaselineBindingRef=PumpTriageBaselineBinding-E1` and the evidence path. Applying G.5 determines whether a shortlist is warranted and which rows qualify. Naming the requested form in the plan settles neither question. If the commission ends with comparing these rows, deliver the established comparison relation.

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

`causalSupportComponentTypeSet` records which methods rely on evidence paths/data regimes, identification, estimates, direct counterfactual sampling, simulation, or transport. Expose the difference and justify the proposed comparison under its causal-support conditions; a shared label does not make unlike components equivalent.

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

For an ordinary parity comparison that uses none of these modes, you can stop after the worked case in §4.3a. Use §4.3b when comparing causal methods or causal-use claims, and the extension blocks below when their mode is active.

The extensions specify only the pins, references, policy IDs, triggers and links needed for each mode. The referenced patterns define what these mean.

**GPatternExtension block: `G.9:Ext.CrossTraditionParity`**
**GPatternExtension: CrossTraditionParity**
* **PatternScopeId:** `G.9:Ext.CrossTraditionParity`
* **GPatternExtensionId:** `CrossTraditionParity`
* **GPatternExtensionKind:** `DisciplineSpecific`
* **GoverningPatternId:** `G.7`
* **Uses:** `{G.7, F.9, E.18, A.21}`
* **⊑/⊑⁺:** `∅`
* **RequiredPins/EditionPins/PolicyPins (minimum; conditional on use):**
  * `BridgeId/BridgeCardId[]` *(for an actual F.9 sense correspondence; cite a card when used)*
  * `BridgeMatrixId?`
  * `CalibrationLedgerId?` / `BCT.id?`
  * `RegressionSetId?` / `SentinelId[]?` *(when sentinel wiring is used)*
  * `CL/CL^k/CL^plane` *(only the channel values consumed or required by the calibration or named assurance account)*
  * `Φ(CL) policy-id`, `Φ_plane policy-id`, `Ψ(CL^k) policy-id?` *(only when the receiving model or assurance account requires that policy)*
  * `CrossingBundleId?` *(required for an actual flow/gate use whose governing rule requires the bundle)*
* **RSCRTriggerSetIds:** `{GCoreTriggerSetId.BridgeCalibrationKit}` *(preferred; expands in `G.Core`)*
* **RSCRTriggerKindIds (delta, if any):** `∅`
* **Notes:** Apply the channel and receiving-use conditions of G.Core:4.2.3. A kind or plane correspondence keeps its own relation and receiving grounds; it creates no F.9 Bridge. The pins cite the calibration, loss model or crossing bundle consumed.

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
* **RSCRTriggerKindIds:** `{RSCRTriggerKindId.EditionPinChange, RSCRTriggerKindId.PolicyPinChange, RSCRTriggerKindId.EvidenceSurfaceEdit}`
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
  * `CharacteristicSpaceRef` with separate `characteristicSpaceDescriptionRef: U.EpistemeRef` *(when discretisation/topology is referenced; resolve the same-space pair under A.19:5.1.1.1)*
  * `EmitterPolicyRef`
  * `InsertionPolicyRef`
* **RSCRTriggerKindIds:** `{RSCRTriggerKindId.EditionPinChange, RSCRTriggerKindId.PolicyPinChange, RSCRTriggerKindId.TelemetryDelta}`
* **Notes:** Pin the QD definitions used by the comparison; their semantics remain in `C.18`, `C.19` and `G.5`.

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
* **Notes (wiring-only):** For open-ended parity, cite the policies and editions above and connect their telemetry to refresh. The extension adds no core rule.

