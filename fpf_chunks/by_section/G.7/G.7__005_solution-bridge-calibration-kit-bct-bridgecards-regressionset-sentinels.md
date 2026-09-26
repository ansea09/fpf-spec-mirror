---
chunk_kind: "child"
pattern_id: "G.7"
pattern_title: "Cross‑Tradition Bridge Calibration Kit (BridgeMatrix → BridgeCards + BCT/Sentinels)"
section_id: "G.7:4"
section_title: "Solution — Bridge calibration kit (BCT + BridgeCards + RegressionSet/Sentinels)"
source_path: "FPF-Spec.md"
output_path: "by_section/G.7/G.7__005_solution-bridge-calibration-kit-bct-bridgecards-regressionset-sentinels.md"
commit_sha: "61a9542aa8479024cdd174c024079d2a6a15f16d"
heading_path:
  - "G.7 — Cross‑Tradition Bridge Calibration Kit (BridgeMatrix → BridgeCards + BCT/Sentinels)"
  - "G.7:4 — Solution — Bridge calibration kit (BCT + BridgeCards + RegressionSet/Sentinels)"
line_start: 114177
line_end: 114457
dependencies:
  - "A.21"
  - "B.3"
  - "C.18"
  - "C.19"
  - "C.21"
  - "C.23"
  - "C.3.3"
  - "E.10"
  - "E.18"
  - "F.17"
  - "F.3"
  - "F.7"
  - "F.9"
  - "G.10"
  - "G.11"
  - "G.12"
  - "G.2"
  - "G.4"
  - "G.5"
  - "G.6"
  - "G.9"
  - "G.Core"
keywords:
  - "BridgeCalibrationTable (BCT)"
  - "BridgeCard"
  - "BridgeSentinel"
  - "Congruence Level (CL/CL^k/CL^plane)"
  - "GateCrossing"
  - "PathSliceId"
  - "RSCRTriggerKindId"
  - "ReferencePlane"
  - "RegressionSet"
  - "SentinelSet"
  - "UTS"
  - "bridge calibration"
  - "loss notes"
  - "waivers"
  - "Φ(CL)/Ψ(CL^k)/Φ_plane policy pins"
---

### G.7:4 - Solution — Bridge calibration kit (BCT + BridgeCards + RegressionSet/Sentinels)

#### G.7:4.1 - G.Core linkage (normative)

**Builds on:** `G.Core` (Part‑G core invariants; citation/delegation hub)

**GCoreLinkageManifest (normative).**

`GCoreLinkageManifest := ⟨
  CoreConformanceProfileIds := {
    GCoreConformanceProfileId.PartG.AuthoringBase,
    GCoreConformanceProfileId.PartG.TriStateGuard,
    GCoreConformanceProfileId.PartG.UTSWhenPublicIdsMinted
  },
  RSCRTriggerSetIds := { GCoreTriggerSetId.BridgeCalibrationKit },
  CorePinSetIds := { GCorePinSetId.PartG.CrossingVisibilityPins },
  CorePinsRequired := {
    BridgeCalibrationTableId (BCT.id),
    RegressionSetId,
    SentinelSetId,
    FreshnessWindowRef,
    CalibrationLedgerId,
    RowScopeId,
    ReferencePlane(src)?,
    ReferencePlane(tgt)?,
    UTSRowId[]?,
    PathId[]?/PathSliceId[]?
  },
  DefaultsConsumed := ∅,
  TriggerAliasMapRef := ∅
⟩`

* **Expansion rule.** Effective `CoreConformanceIds`, `RSCRTriggerKindIds`, and `CorePinsRequired` are obtained by expanding the cited profile/set ids and unioning with the explicit ids above (see `G.Core` nil‑elision + expansion rule).
* **Conditional pins.**
  * Relation, calibration and policy pins follow the channel/use conditions in G.Core:4.2.3. Source/target planes are required for an actual plane claim or another rule that consumes them; UTS and Path pins follow actual public-name and path uses.
  * `BridgeCardRef.edition` is required iff an F.9 BridgeCard is published as an editioned artefact.
  * Sentinel scopes MAY be recorded as `PatternScopeId[]` when path surfaces are not available (and SHALL then be present in sentinel records and emitted trigger payload pins).
* **CN/CG note.** `CC‑GCORE‑CN‑CG‑1` is included via `GCoreConformanceProfileId.PartG.AuthoringBase` and is exercised only when the governance card and legality gate (e.g., `CNSpecRef.edition` / `CGSpecRef.edition`) are explicitly pinned; penalty/guard policy ids (`Φ(CL)`, `Ψ(CL^k)`, `Φ_plane`) are policy pins, not governance cards or legality gates.

*(payload pins, minimum: affected members of the effective `CorePinsRequired` (after expansion) plus any pins introduced by active extensions (e.g., QD parity pins), scoped to the watched `PathSliceId[]`/`PathId[]`/`PatternScopeId[]`.)*

#### G.7:4.2 - Kit objects (surface governed by this pattern)

This pattern defines the *bridge calibration kit* as a set of minimal, checkable surfaces. **F.9** governs `BridgeCard` and CL meaning; **C.3.3** governs `KindBridge` and `CL^k` when the kind channel is used. G.7 adds calibration records and publication/wiring surfaces.

**(A) BridgeCalibrationTable (BCT) — object.**
A `BridgeCalibrationTable` is a per‑Tradition‑pair registry of calibrated bridge entries.

Minimal fields (conceptual):

`BridgeCalibrationTable := ⟨
BCT.id, TradPairId, FreshnessWindowRef,
RowEntries[]
⟩`

**Source provenance (when sourced from `G.2`).** If the BCT is derived from a `G.2` BridgeMatrix, publish `BridgeMatrixId` (+ `BridgeMatrixRef.edition` when editioned) and row‑level linkage via `G.7:Ext.MatrixIntake` (wiring‑only), rather than duplicating G.2 semantics in core.

Where each `RowEntry` minimally binds:

`RowEntry := ⟨
RowEntryId, ComparableConstructId, RowScopeId,
BridgeCardId[]?, KindBridgeAssertionRef[]?, PlaneRelationRef[]?,
RowCL_min?, RowCL_k_min?, RowCL_plane_min?, CalibrationBasisRef,
LossNoteRef[]?, CounterExampleRef[]?, CounterExampleAbsenceRef?, ReceivingUseClaimRef[]?, ReceivingPolicyRef[]?, WaiverRef[]?,
RegressionSetId, SentinelSetId,
PolicyPins?: { Φ(CL)?, Ψ(CL^k)?, Φ_plane? },
PlanePins?: { ReferencePlane(src), ReferencePlane(tgt) },
ExtensionPins?: { [GPatternExtensionId]: { …ids… } }
⟩`

**(B) CalibrationLedger — object.**
A `CalibrationLedger` is the auditable “row narrative” that remains *pin‑first*: it records what was calibrated, what was lost, and which artefacts/policies witness that.

Minimal fields:

`CalibrationLedger := ⟨
LedgerId, TradPairId,
Entries[]  // cite RowEntryId, relation/card refs, calibration basis and supported summaries, losses, counterexamples or search disclosure, UTS rows and any regression-run/delta refs; keep receiving-use/policy claims and a policy exception distinct
⟩`

**(C) RegressionSet — object.**
A `RegressionSet` is a small set of regression probes/checks that are runnable against the BCT row entries. It exists to detect drift (bridge edits, policy edits, plane edits, edition pin changes) and to provide the evidential payload for RSCR triggers.

Minimal fields:

`RegressionSet := ⟨ RegressionSetId, TradPairId, TestCaseId[], ExpectedOutcomesRef?, RegressionRunRef? ⟩`

##### G.7:4.2.1 - Interpret calibration and assess a receiving use separately

**Calibration question.** State which correspondence, direction, scope, source editions and evidence the row assesses. Keep an F.9 sense correspondence, a C.3.3 kind correspondence and an applicable plane relation under their separate predicates. A record or favourable summary makes none of them obtain.

For a stated F.9 correspondence, optional CL shorthand means: `0` contradicted, `1` weakly comparable, `2` bounded support with explicit counterexamples, and `3` matched stated invariants with no current material counterexample. Cite the actual calibration basis. A kind-channel value follows C.3.3; a plane-channel value requires its own declared calibration rule. One channel cannot raise or replace another.

**Summary meaning.** Use `RowCL_min` only when a non-empty set of cells shares the declared ordinal scale and calibration question and the receiving report needs its weakest calibrated level. Cite that cell set and keep each loss recoverable. Apply the same condition independently to kind or plane summaries. An empty, mixed or unresolved basis has no such minimum; publish the separate results or the precise gap. A minimum is a calibration summary, not an admissibility result, and ordinal values are not averaged.

**Evidence honesty.** Preserve actual counterexamples and losses. Level 2 needs its cited bounded-support counterexample; level 0 identifies the contradiction. Weak or incomplete evidence must be disclosed rather than dressed as a discovered counterexample. At level 3, when none is cited, supply a citable search/absence account stating what was examined and that none was found or is currently known. This reports the search basis, not universal absence. A loss-noted row cannot be presented as free substitution.

**Receiving use.** For an F.9 use, state the separate claim with its use, direction, correspondence rule, loss tolerance and polarity; obtain matching A.10 reliance, or the B.3 result when an actual named assurance claim is current. A C.3.3 use separately checks receiving admissibility and target classification. Missing classification evidence remains unknown. Authorization, when required, follows its own rule. No CL level supplies these results.

A receiving policy may impose an additional threshold for one named use. Cite that use, the policy's justification and authority, and its other necessary premises. The threshold is an additional policy condition, not F.9's general law. A `WaiverRef` identifies an authorized exception to that policy only: it supplies no missing correspondence, target fact, suitable-use claim or evidence. Preserve any narrower allowed use and its independently supported conditions.

**Plane and loss policies.** When a receiving use relies on a plane relation, name the source and target planes, its predicate, calibration basis and applicable policy. Missing required plane information leaves that use unresolved. Keep any downstream `abstain` or policy-bound `degrade` under its receiving guard. Plane evidence does not rewrite CL or CL^k; a numerical loss requires its own receiving model and policy, with the consequence in R only.

**(D) SentinelSet & BridgeSentinel — object.**
A `SentinelSet` is a watch‑list that connects bridge calibration changes to RSCR‑ready triggers scoped to downstream consumption.

Minimal fields:

`BridgeSentinel := ⟨
SentinelId,
watchedRowEntryIds: RowEntryId[],
watchedRelationRefs: exact references to the correspondences assessed by those rows,
watchedScope: PathSliceId[] | PathId[] | PatternScopeId[],
payloadPins: { BCT.id, RegressionSetId, FreshnessWindowRef, affected RowEntryId[], watchedRelationRefs, PolicyPins?, PlanePins?, UTSRowId[]? }
⟩`

`SentinelSet := ⟨ SentinelSetId, BridgeSentinel[] ⟩`

#### G.7:4.3 - Minimal calibration procedure (auditable; table‑backed; bridge‑first)

For each Tradition‑pair and each comparable construct row from **G.2**:

1. **Recover the correspondence being calibrated.** For an F.9 row, resolve the exact F.17 sense cells and profile, then produce or reuse its BridgeCard. A kind-channel row cites the C.3.3 kind endpoints and assertion; a plane row cites its own relation and rule. A coarser source label must be resolved to those actual endpoints before calibration.
2. **Record row scope and losses.** Author a `RowScopeId` and record loss notes as first‑class citations (e.g., `LossNoteRef[]`), not as informal footnotes.
   Record the calibration basis and any meaningful channel summary under §4.2.1. If a receiving use is named, cite its separate suitability/classification and reliance results. Cite a waiver only for its exact authorized policy exception; it does not repair missing evidence.
3. **Resolve any plane claim.** If the row or receiving use consumes a plane relation, record its exact reference, source and target planes, governing rule and any plane policy actually applied. A kind-only or sense-only row creates no plane claim.
4. **Expose policies actually used.** Record policy and model references for a named threshold, exception, numerical loss or assurance calculation. Calibration without such a receiving use needs no invented Φ/Ψ/Φ_plane policy. Applied penalties retain G.Core's R/R_eff-only rule.
5. **Summarize only a common calibration basis.** Use the minimum only under §4.2.1's shared-scale and shared-question conditions. Retain each actual loss and counterexample; otherwise report the separate cell results or the unresolved basis.
6. **Regression and sentinel wiring.** Create/update the `RegressionSet` and `SentinelSet`. Any calibration change that can affect downstream audit (CL/CL^k/plane pins, relevant policy ids, edition pins for involved telemetry surfaces, freshness window) emits typed RSCR triggers (canonical ids; scope + payload pins).
   If the regression harness is run, record a citable `RegressionRunRef` (or equivalent run/delta reference) and attach it to the relevant ledger entries (pin‑first; no narrative-only deltas).

#### G.7:4.4 - Publication surfaces (UTS + GateCrossing harness)

A conformant G.7 publication:

* publishes the exact correspondence references for each row, including BridgeCards for F.9 rows and UTS identifiers when the naming/publication rule requires them,
* makes an independently governed E.18 crossing or A.21 gate checkable through its applicable harness, preserving lexical, lane and required-pin constraints,
* emits RSCR triggers using canonical `RSCRTriggerKindId` and attaches the minimum payload pins listed in §4.1.
* keeps SCR/Evidence citations complete for their actual use: include the row locator, exact correspondence basis and `{BCT.id, RegressionSetId}`, plus the policy/model pins actually consumed by the reliance or assurance claim. Representation follows G.6/SCR when that surface is used.

#### G.7:4.5 - Worked mini‑examples (informative; post‑2015; row scopes + loss notes)

> These worked rows use illustrative calibration values and source scopes. Actual calibration needs its stated evidence. Each receiving use still has a separate rule and loss tolerance.

1. **Preference‑learning objective (Method; RowScope = “training‑objective‑intent”).**
   *Cells:* `RLHF@Context‑A` ↔ `DPO@Context‑B` ↔ `IPO@Context‑C`
   *RowCL_min:* 2 (calibrated bounded support in this worked case)
   *Loss notes:* different inductive biases (reward model vs direct preference likelihood; sensitivity to preference noise model; implicit regularisation forms).
   *Proposed use:* a didactic comparison of objective intent. Its separate claim must limit the comparison to that intent and retain the listed differences; method eligibility and acceptance require their own rule.

2. **Robustness evaluation (Measurement; RowScope = “metric‑family‑intent”).**
   *Cells:* `Accuracy@IID` ↔ `Robustness@ShiftBench` (e.g., distribution‑shift benchmarks common in post‑2019 practice)
   *RowCL_min:* 2
   *Loss notes:* shift taxonomy differs; comparability depends on pinned protocol editions and window selection; “robustness” is not a scalar substitute for accuracy.

3. **Quality‑Diversity archive comparability (Measurement; RowScope = “DescriptorMap‑only”).**
   *Cells:* `MAP‑Elites grid indices` ↔ `CVT‑MAP‑Elites centroids` ↔ `CMA‑ME archive`
   *RowCL_min:* 2
   *Loss notes:* discretisation vs centroidal tessellation; archive pressure differs; drift occurs if `DistanceDef` or insertion policy changes.
   *Proposed use:* cross-reporting only the named descriptor-map relation under explicit edition pins and an affirmative bounded-use claim with passing reliance. Edition pins alone do not make the telemetry comparable.

4. **Open‑ended transfer semantics (Method; RowScope = “transfer‑rule intent”).**
   *Cells:* `POET‑class transfer rule` ↔ `Enhanced‑POET‑class transfer rule` ↔ “modern open‑ended transfer variants”
   *RowCL_min:* 2
   *Loss notes:* environment validity region differs; transfer timing and selection pressures differ; pinning transfer rule editions is mandatory for audit.

**Paired receiving case — Vehicle to TransportUnit.** Use C.3.3 §9.1's exact source and target kind declarations, pinned scheme editions, `registryAPI v1.4` and selected time window. In row `VehicleTransportOrder`, record the obtaining KindBridge, preserved PassengerCar/Vehicle subkind order and collapsed EV distinction, with the reported `CL^k=2` and battery-health loss. This is the kind channel; an F.9 sense Bridge is added only if the receiving claim separately relies on one.

For a G.5 shortlist of independently admitted Methods for a transport review, suppose the applicability criterion uses only the preserved transport/passenger order and explicitly ignores propulsion. The row can support that narrow applicability comparison after receiving admissibility, fresh target classification of the subject vehicles and the matching evidence-reliance result pass. The Methods' other eligibility criteria remain applicable. For a battery-health review whose Method-selection rule needs EV/battery information, the same correspondence fails that use because the required distinction is lost. A favourable CL value or a waiver cannot supply the battery premise. The correspondence and calibration can stay unchanged while these two use conclusions differ. Use these two questions as a paired RegressionSet probe when this row is reused: recover the transport-order premise for the first and expose the missing battery premise for the second. Recheck the affected use after its criterion or the row's preservation/loss basis changes.

In C.3.3 §9.3's AdultPatient/AdultPerson_Y case, the age-boundary loss and `CL^k=1` remain evidence about the kind correspondence. An authorized policy exception does not supply an unresolved date of birth; the receiving classification stays unknown.

**Choose pins for the actual use.** These cases apply the same conditions to a compact result and to the fuller kit:

| Use | What the result must retain |
| --- | --- |
| VehicleTransportOrder kind-only calibration | its C.3.3 kind endpoints, assertion, CL^k calibration basis, battery-health loss, row/freshness and kit references; a live sentinel can use PatternScopeId. No sense Bridge, plane relation or loss policy follows from this row. |
| F.9 sense-only calibration | exact F.17 sense endpoints, obtaining Bridge, BridgeCard and any reported CL basis; add neither a kind correspondence nor a plane claim without its own basis. |
| Plane-only calibration | the independently governed plane relation, planes and calibration rule/basis; add a numerical loss policy only if that receiving model is used. Plane change alone supplies no F.9 Bridge. |
| A G.2 harvest with no crossing, or a suite contract reused on another entity of the same kind | ordinary source/edition and applicability information; no crossing pin set is instantiated merely from the harvest, entity change or a new declaration edition. |
| A use relying on both a sense and kind correspondence | both independently established relations and their receiving conditions; neither channel replaces the other. |
| A safety-assurance comparison using an F.9 calibration, a defined plane-loss model and an A.21 gate | the exact Bridge/Card and row, BCT/regression/freshness evidence, actual plane relation and model/policy pins, matching A.10/B.3 reliance and assurance grounds, and every required gate anchor. A required missing pin leaves that use unresolved; favourable calibration alone grants no permission. |

#### G.7:4.6 - Extensions (pattern‑scoped; non‑core)

> Extensions carry *wiring only* (pins/editions/policy‑ids + which governing patterns are applied). They MUST NOT redefine core invariants or defaults.

**GPatternExtension: MatrixIntake**

* **PatternScopeId:** `G.7:Ext.MatrixIntake`
* **GPatternExtensionId:** `MatrixIntake`
* **GPatternExtensionKind:** `InteropSpecific`
* **GoverningPatternId:** `G.2` *(BridgeMatrix semantics and comparable-construct inventory)*
* **Uses:** `{G.2, F.9}`
* **⊑/⊑⁺:** `∅`
* **RequiredPins/EditionPins/PolicyPins (minimum):**

  * `BridgeMatrixId` (and, if editioned: `BridgeMatrixRef.edition`)
  * `BridgeMatrixRowRef[]` *(row‑level anchors for intake; defined by the governing pattern; e.g., `PatternScopeId` / `UTSRowId` / row ids)*
  * `ComparableConstructId[]` *(row keys; if the source does not supply a stable id, `G.7` mints one while preserving `BridgeMatrixRowRef` as the provenance anchor)*
  * `LossNoteRef[]?` *(if exported by `G.2`; otherwise authored in `G.7` and cited from the `CalibrationLedger`)*
* **RSCRTriggerKindIds:** `{RSCRTriggerKindId.CrossingBundleEdit, RSCRTriggerKindId.EvidenceSurfaceEdit, RSCRTriggerKindId.EditionPinChange}`
* **Notes (wiring‑only):** This module binds “row candidates” from G.2 to the BCT/Ledger intake without copying G.2 semantics into G.7.

**GPatternExtension: DHCAccounting**

* **PatternScopeId:** `G.7:Ext.DHCAccounting`
* **GPatternExtensionId:** `DHCAccounting`
* **GPatternExtensionKind:** `DisciplineSpecific`
* **GoverningPatternId:** `C.21` *(DHC metric semantics, including AlignmentDensity)*
* **Uses:** `{C.21}`
* **⊑/⊑⁺:** `∅`
* **RequiredPins/EditionPins/PolicyPins (minimum; conditional on use):**

  * `AlignmentDensityMethodRef.edition?`
  * `DeclaredUnitsRef?` *(the C.21 Unit for the reported quantity; AlignmentDensity uses `obtaining_relations/100_compared_cells`)*
* **RSCRTriggerKindIds:** `{RSCRTriggerKindId.TelemetryDelta, RSCRTriggerKindId.PolicyPinChange, RSCRTriggerKindId.EditionPinChange}`
* **Notes (wiring‑only):**
  * G.7 stores the *counts and declared units* as a surface; C.21 governs the meaning and legality constraints.
  * When reporting AlignmentDensity, follow C.21's declared F.17 cell set and count only exact obtaining directed F.9 relations. Preserve each counted relation's orientation and admitted-use qualifier, and keep observed loss in its evidence account. CL values neither change that count definition nor grant substitution; `CC‑G7‑DHC‑Units‑1` checks the report's units and cited method.

**GPatternExtension: QDParityPins**

* **PatternScopeId:** `G.7:Ext.QDParityPins`
* **GPatternExtensionId:** `QDParityPins`
* **GPatternExtensionKind:** `InteropSpecific`
* **GoverningPatternId:** `C.18` *(QD artefact semantics; uses C.19 for exploration/logging pins as needed)*
* **Uses:** `{C.18, C.19}`
* **⊑/⊑⁺:** `∅`
* **RequiredPins/EditionPins/PolicyPins (minimum; conditional on use):**

  * `DescriptorMapRef.edition`
  * `DistanceDefRef.edition`
  * `InsertionPolicyRef` *(policy id or pinned policy ref, per governing definition semantics)*
* **RSCRTriggerKindIds:** `{RSCRTriggerKindId.EditionPinChange, RSCRTriggerKindId.PolicyPinChange, RSCRTriggerKindId.TelemetryDelta, RSCRTriggerKindId.FreshnessOrDecayEvent}`
* **Notes (wiring‑only):** Enforces reproducibility of cross‑Context archive/illumination comparisons without pulling QD semantics into the core bridge kit.
  The pins from this module should be attached via `RowEntry.ExtensionPins[QDParityPins]` (or an equivalent extension‑pin map) and included in `BridgeSentinel.payloadPins` whenever the watched scope consumes QD telemetry.

**GPatternExtension: SoSLogClauses**

* **PatternScopeId:** `G.7:Ext.SoSLogClauses`
* **GPatternExtensionId:** `SoSLogClauses`
* **GPatternExtensionKind:** `InteropSpecific`
* **GoverningPatternId:** `C.23` *(SoS‑LOG rule and branch semantics; G.7 does not redefine meaning)*
* **Uses:** `{C.23, G.6}`
* **⊑/⊑⁺:** `∅`
* **RequiredPins/EditionPins/PolicyPins (minimum; conditional on use):**
  * `SoSLogRuleId[]` *(or governing definition‑equivalent ids)*
  * `FailureBehaviorPolicyId?` *(policy id, when degrade behavior is bound)*
  * `PathId/PathSliceId` citations for explainability (via `G.6`)
  * `BridgeCardId[]` (bridges whose reuse is being justified)
* **RSCRTriggerKindIds:** `{RSCRTriggerKindId.PolicyPinChange, RSCRTriggerKindId.EvidenceSurfaceEdit, RSCRTriggerKindId.CrossingBundleEdit, RSCRTriggerKindId.MaturityRungChange}`
* **Notes (wiring‑only):** Ensures cross‑Tradition bridge reuse decisions can be justified by citing SoS‑LOG clauses and evidence paths, without embedding SoS‑LOG semantics into G.7.

**GPatternExtension: AcceptanceHooks**

* **PatternScopeId:** `G.7:Ext.AcceptanceHooks`
* **GPatternExtensionId:** `AcceptanceHooks`
* **GPatternExtensionKind:** `MethodSpecific`
* **GoverningPatternId:** `G.4` *(Acceptance/threshold/unknown handling; G.7 does not define thresholds)*
* **Uses:** `{G.4}`
* **⊑/⊑⁺:** `∅`
* **RequiredPins/EditionPins/PolicyPins (minimum; conditional on use):**
  * `AcceptanceClauseId[]` *(or governing definition‑equivalent ids)*
  * `AcceptancePolicyId?` *(policy id when acceptance behavior is pinned)*
  * `BridgeCardId[]` (bridges whose calibrated status is being used as a gate input)
* **RSCRTriggerKindIds:** `{RSCRTriggerKindId.PolicyPinChange, RSCRTriggerKindId.BaselineBindingEdit, RSCRTriggerKindId.LegalitySurfaceEdit}`
* **Notes (wiring‑only):** When bridges are used as selector gates, thresholds and unknown-handling remain governed by Acceptance; this module only pins the linkage and refresh relevance.

**GPatternExtension: AdvancedCalibrationProcedures (Phase‑3 seed)**

* **PatternScopeId:** `G.7:Ext.AdvancedCalibrationProcedures`
* **GPatternExtensionId:** `AdvancedCalibrationProcedures`
* **GPatternExtensionKind:** `Phase3Seed`
* **GoverningPatternId:** `governing pattern not yet selected`
* **Uses:** `{ }`
* **⊑/⊑⁺:** `∅`
* **RequiredPins/EditionPins/PolicyPins:** `pending governing-pattern selection`
* **RSCRTriggerKindIds:** `{RSCRTriggerKindId.CrossingBundleEdit, RSCRTriggerKindId.PenaltyPolicyEdit, RSCRTriggerKindId.ReferencePlaneEdit}`
* **Notes (seed; non‑normative):** Placeholder for domain‑specific / statistical calibration families beyond the minimal auditable procedure (e.g., uncertainty‑aware calibration, probabilistic mapping). No Part‑G‑wide norms are introduced.

