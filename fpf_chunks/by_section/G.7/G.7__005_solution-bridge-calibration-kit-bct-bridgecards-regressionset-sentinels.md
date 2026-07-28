---
chunk_kind: "child"
pattern_id: "G.7"
pattern_title: "Cross‑Tradition Bridge Calibration Kit (BridgeMatrix → BridgeCards + BCT/Sentinels)"
section_id: "G.7:4"
section_title: "Solution — Bridge calibration kit (BCT + BridgeCards + RegressionSet/Sentinels)"
source_path: "FPF-Spec.md"
output_path: "by_section/G.7/G.7__005_solution-bridge-calibration-kit-bct-bridgecards-regressionset-sentinels.md"
commit_sha: "17edd955485f60cafb16159c7d90e20f4ad21844"
heading_path:
  - "G.7 — Cross‑Tradition Bridge Calibration Kit (BridgeMatrix → BridgeCards + BCT/Sentinels)"
  - "G.7:4 — Solution — Bridge calibration kit (BCT + BridgeCards + RegressionSet/Sentinels)"
line_start: 98747
line_end: 99018
dependencies:
  - "A.21"
  - "B.3"
  - "C.18"
  - "C.19"
  - "C.21"
  - "C.23"
  - "E.10"
  - "E.18"
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
    ReferencePlane(src),
    ReferencePlane(tgt),
    UTSRowId[],
    PathId[]/PathSliceId[]
  },
  DefaultsConsumed := ∅,
  TriggerAliasMapRef := ∅
⟩`

* **Expansion rule.** Effective `CoreConformanceIds`, `RSCRTriggerKindIds`, and `CorePinsRequired` are obtained by expanding the cited profile/set ids and unioning with the explicit ids above (see `G.Core` nil‑elision + expansion rule).
* **Conditional pins.**
  * `BridgeCardRef.edition` is required iff BridgeCards are published as editioned artefacts.
  * Sentinel scopes MAY be recorded as `PatternScopeId[]` when path surfaces are not available (and SHALL then be present in sentinel records and emitted trigger payload pins).
* **CN/CG note.** `CC‑GCORE‑CN‑CG‑1` is included via `GCoreConformanceProfileId.PartG.AuthoringBase` and is exercised only when the governance card and legality gate (e.g., `CNSpecRef.edition` / `CGSpecRef.edition`) are explicitly pinned; penalty/guard policy ids (`Φ(CL)`, `Ψ(CL^k)`, `Φ_plane`) are policy pins, not governance cards or legality gates.

*(payload pins, minimum: affected members of the effective `CorePinsRequired` (after expansion) plus any pins introduced by active extensions (e.g., QD parity pins), scoped to the watched `PathSliceId[]`/`PathId[]`/`PatternScopeId[]`.)*

#### G.7:4.2 - Kit objects (surface governed by this patterns)

This pattern defines the *bridge calibration kit* as a set of minimal, checkable surfaces. Semantics of `BridgeCard` and CL typing are governed by **F.9**; G.7 adds calibration records and publication/wiring surfaces.

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
BridgeCardId[],
RowCL_min, RowCL_k_min?, RowCL_plane_min?,
LossNoteRef[]?, CounterExampleRef[]?, CounterExampleAbsenceRef?, WaiverRef[]?,
RegressionSetId, SentinelSetId,
PolicyPins: { Φ(CL), Ψ(CL^k)?, Φ_plane? },
PlanePins: { ReferencePlane(src), ReferencePlane(tgt) },
ExtensionPins?: { [GPatternExtensionId]: { …ids… } }
⟩`

**(B) CalibrationLedger — object.**
A `CalibrationLedger` is the auditable “row narrative” that remains *pin‑first*: it records what was calibrated, what was lost, and which artefacts/policies witness that.

Minimal fields:

`CalibrationLedger := ⟨
LedgerId, TradPairId,
Entries[]  // each entry cites RowEntryId, BridgeCardId(s), CL‑minima, waivers (if any), loss notes, counterexamples, UTS rows, and (when run) regression-run/delta refs
⟩`

**(C) RegressionSet — object.**
A `RegressionSet` is a small set of regression probes/checks that are runnable against the BCT row entries. It exists to detect drift (bridge edits, policy edits, plane edits, edition pin changes) and to provide the evidential payload for RSCR triggers.

Minimal fields:

`RegressionSet := ⟨ RegressionSetId, TradPairId, TestCaseId[], ExpectedOutcomesRef?, RegressionRunRef? ⟩`

##### G.7:4.2.1 - CL / CL^k admissibility regime and plane guard (kit‑local; normative)

This subsection is kit-governed (G.7) and complements (but does not duplicate) `G.Core` penalty routing and tri‑state guard semantics.

**Admissibility regimes (row‑level, minimal).**
* `RowCL_min` MUST take a value in `{3,2,1,0}` (value set and CL meaning are governed by F.9; G.7 governs the admissibility regime).
* Default admissibility for cross‑Tradition reuse:
  * `RowCL_min ≥ 2` ⇒ admissible for reuse (subject to downstream guards/policies).
  * `RowCL_min = 1` ⇒ **NOT** admissible unless an explicit `WaiverRef[]` is cited; any reuse under waiver is **guarded-only** (no substitution semantics).
  * `RowCL_min = 0` ⇒ forbidden for reuse; it MAY remain in BCT as a documented non‑bridge with loss notes/counterexamples.
* **Honesty rule (row‑level):**
* if `RowCL_min ≤ 2`, at least one `CounterExampleRef[]` MUST be cited;
* if `RowCL_min = 3` and `CounterExampleRef[]` is empty, a citable `CounterExampleAbsenceRef` MUST be provided (explicit “searched‑none found / no known counterexample” disclosure);
  * if any `LossNoteRef[]` is present, the row MUST NOT be presented as “free substitution” in any consumer surface.

**Kind channel (`CL^k`) (conditional).**
If a row relies on bridges in the `Kind` channel, then `RowCL_k_min` and `Ψ(CL^k)` pin MUST be present, and the same admissibility regimes apply to `RowCL_k_min`.

**Plane guard (`CL^plane`) (conditional).**
If `ReferencePlane(src)` and `ReferencePlane(tgt)` differ (or plane routing is explicitly invoked), then:
* `RowCL_plane_min` and `Φ_plane` pin MUST be present;
* if either plane pin is absent, the row is non‑conformant (no implicit plane defaulting);
* any “blocking” outcome must be representable downstream via `G.Core` tri‑state guard (`abstain` or a policy‑bound `degrade(mode=…)`), without introducing additional statuses in G.7;
* plane effects MUST NOT rewrite `CL/CL^k`; their impact is routed via the pinned policy ids and `G.Core` penalty semantics.

**(D) SentinelSet & BridgeSentinel — object.**
A `SentinelSet` is a watch‑list that connects bridge calibration changes to RSCR‑ready triggers scoped to downstream consumption.

Minimal fields:

`BridgeSentinel := ⟨
SentinelId,
watchedBridgeIds: BridgeCardId[],
watchedScope: PathSliceId[] | PathId[] | PatternScopeId[],
payloadPins: { BCT.id, RegressionSetId, FreshnessWindowRef, PolicyPins, PlanePins, UTSRowId[] }
⟩`

`SentinelSet := ⟨ SentinelSetId, BridgeSentinel[] ⟩`

#### G.7:4.3 - Minimal calibration procedure (auditable; table‑backed; bridge‑first)

For each Tradition‑pair and each comparable construct row from **G.2**:

1. **Materialise bridge artefacts.** Produce (or reuse) **F.9** `BridgeCard`s for the concrete `SenseCell`‑level alignments required by the row scope.
   *Note.* “SenseCell anchoring” is a kit requirement: if a row is authored at a coarser token level, the SenseCell anchors must be explicitly cited (F.3 discipline).
2. **Record row scope and losses.** Author a `RowScopeId` and record loss notes as first‑class citations (e.g., `LossNoteRef[]`), not as informal footnotes.
   Also record `RowCL_min` (and `RowCL_k_min?`, `RowCL_plane_min?` when applicable) and cite `WaiverRef[]` if any row is intentionally kept at `=1` for guarded-only reuse.
3. **Plane pins (no hidden plane mixing).** Record source `ReferencePlane` pins and target `ReferencePlane` pins and the relevant policy id pins for plane routing (ids only; do not duplicate policy tables).
4. **Policy pins for penalty routing.** Record the policy id pins needed to audit penalty routing (ids only). Penalty semantics cite `CC‑GCORE‑PEN‑1` through `G.Core`; G.7’s responsibility is to make the pins explicit and published.
5. **Row bottleneck discipline.** When a row aggregates multiple bridge cells, row summarisation uses bottleneck semantics (F.7) and carries a counterexample citation whenever any cell is loss‑noted.
6. **Regression and sentinel wiring.** Create/update the `RegressionSet` and `SentinelSet`. Any calibration change that can affect downstream audit (CL/CL^k/plane pins, relevant policy ids, edition pins for involved telemetry surfaces, freshness window) emits typed RSCR triggers (canonical ids; scope + payload pins).
   If the regression harness is run, record a citable `RegressionRunRef` (or equivalent run/delta reference) and attach it to the relevant ledger entries (pin‑first; no narrative-only deltas).

#### G.7:4.4 - Publication surfaces (UTS + GateCrossing harness)

A conformant G.7 publication:

* publishes UTS‑citable identifiers for `BridgeCard`s and any GateCrossing/crossing rows that rely on them,
* ensures crossing bundles are checkable via **E.18/A.21** harnesses (lexical SD, lane purity, required pin presence),
* emits RSCR triggers using canonical `RSCRTriggerKindId` and attaches the minimum payload pins listed in §4.1.
* ensures evidence-facing citations are pin-complete: whenever bridge calibration is cited in SCR/Evidence surfaces, the citation MUST include `{BCT.id, RegressionSetId}` and the active policy id pins `{Φ(CL), Ψ(CL^k)?, Φ_plane?}` (ids only; representation is governed by `G.6`/SCR).

#### G.7:4.5 - Worked mini‑examples (informative; post‑2015; row scopes + loss notes)

> These are **working models**, not equivalence claims. They illustrate how row scope + loss notes constrain safe reuse.

1. **Preference‑learning objective (Method; RowScope = “training‑objective‑intent”).**
   *Cells:* `RLHF@Context‑A` ↔ `DPO@Context‑B` ↔ `IPO@Context‑C`
   *RowCL_min:* 2 (guarded)
   *Loss notes:* different inductive biases (reward model vs direct preference likelihood; sensitivity to preference noise model; implicit regularisation forms).
   *Use:* cross‑Tradition *didactic alignment* and eligibility hints; thresholds/acceptance remain governed by CAL.

2. **Robustness evaluation (Measurement; RowScope = “metric‑family‑intent”).**
   *Cells:* `Accuracy@IID` ↔ `Robustness@ShiftBench` (e.g., distribution‑shift benchmarks common in post‑2019 practice)
   *RowCL_min:* 2
   *Loss notes:* shift taxonomy differs; comparability depends on pinned protocol editions and window selection; “robustness” is not a scalar substitute for accuracy.

3. **Quality‑Diversity archive comparability (Measurement; RowScope = “DescriptorMap‑only”).**
   *Cells:* `MAP‑Elites grid indices` ↔ `CVT‑MAP‑Elites centroids` ↔ `CMA‑ME archive`
   *RowCL_min:* 2
   *Loss notes:* discretisation vs centroidal tessellation; archive pressure differs; drift occurs if `DistanceDef` or insertion policy changes.
   *Use:* admissible cross-reporting of QD telemetry when edition pins are explicit.

4. **Open‑ended transfer semantics (Method; RowScope = “transfer‑rule intent”).**
   *Cells:* `POET‑class transfer rule` ↔ `Enhanced‑POET‑class transfer rule` ↔ “modern open‑ended transfer variants”
   *RowCL_min:* 2
   *Loss notes:* environment validity region differs; transfer timing and selection pressures differ; pinning transfer rule editions is mandatory for audit.

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
  * `DeclaredUnitsRef?` *(units declaration style per governing definition; e.g., “bridges_per_100_DHC_SenseCells”)*
* **RSCRTriggerKindIds:** `{RSCRTriggerKindId.TelemetryDelta, RSCRTriggerKindId.PolicyPinChange, RSCRTriggerKindId.EditionPinChange}`
* **Notes (wiring‑only):**
  * G.7 stores the *counts and declared units* as a surface; C.21 governs the meaning and legality constraints.
  * When reporting AlignmentDensity, the counted bridge set is typically restricted to `CL ≥ 2` (treat `CL=3` as “free substitution”, `CL=2` as “guarded” for reporting); conformance is enforced by `CC‑G7‑DHC‑Units‑1` while semantics remain governed by `C.21`.

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

