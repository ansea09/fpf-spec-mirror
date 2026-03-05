**Primary output.** A bridge calibration kit that turns **G.2**’s BridgeMatrix rows into **F.9** `BridgeCard`s and publishes: a `BridgeCalibrationTable (BCT)` + `CalibrationLedger` + `RegressionSet` + `SentinelSet`, plus UTS‑visible crossing rows and RSCR‑ready sentinel triggers scoped to `PathSliceId` / `PatternScopeId`.
**Primary hooks.** `G.Core` (Part‑G invariants + RSCR trigger catalogue + default-ownership index), **G.2** (BridgeMatrix), **F.9** (BridgeCard + CL/CL^k), **F.3/F.7** (SenseCell anchoring; row bottleneck discipline), **E.18/A.21** (GateCrossing + CrossingSurface checks), **G.6** (PathId/PathSliceId citation surface), **G.5** (downstream consumer for eligibility/selection), **G.11** (refresh orchestration consumer), **B.3** (assurance lanes + penalty policies), **C.21** (DHC accounts such as AlignmentDensity), **C.18/C.19** (QD/OEE pins when relevant), **C.23** (SoS‑LOG clauses as explainability gates for cross‑Tradition choices), **G.4** (Acceptance hooks/thresholds when bridges are used as selector gates), **E.10** (LEX / strict distinction discipline).
**Working‑Model first.** Prefer a minimal, auditable calibration procedure and worked micro‑cases; escalate to heavier harnesses only where risk warrants (per **E.8**).
**Non‑duplication note.** Universal Part‑G invariants (no shadow specs; Bridge‑only crossings; penalty routing to `R_eff` only; P2W split; typed/id‑based RSCR causes; single‑owner defaults; Δ‑discipline) are owned by `G.Core` and are *cited* via `CC‑GCORE‑*`. This pattern defines only the *bridge calibration kit* and its surfaces.

### G.7:1 - Problem frame

SoTA synthesis (**G.2**) can legitimately preserve pluralism by exporting a **BridgeMatrix**: a Tradition×Tradition inventory of “comparable constructs” with preliminary notes (candidate correspondences, likely losses, tentative levels). Downstream patterns (CHR/CAL/selector/logging/shipping) cannot consume this safely unless cross‑Context reuse is:

* **materialised** as explicit bridge artefacts (not implied by prose),
* **calibrated** with a small, auditable procedure (so CL/CL^k/plane routing is not a narrative),
* **published** as checkable crossing surfaces (UTS + GateCrossing harness),
* **refreshable** in a *targeted* way (path‑scoped RSCR rather than whole‑pack reruns).

`G.7` packages this into a kit: `BCT` + `BridgeCard` publication + `RegressionSet`/`SentinelSet` wiring, so that later patterns can satisfy core invariants without re‑inventing cross‑Tradition machinery.

### G.7:2 - Problem

1. Cross‑Tradition comparisons are frequently attempted via informal “synonymy” or ad‑hoc mappings, causing silent meaning drift and hidden crossings.
2. Plane mismatches (world ↔ concept ↔ episteme, or other `ReferencePlane` shifts) are often ignored, or conflated with “semantic sameness”, causing wrong downstream confidence.
3. Calibration changes (CL/CL^k/plane or their policy pins) must trigger **targeted** re‑checks; pack‑wide reweaves are too costly and too slow.
4. If bridges are involved in QD/illumination or other edition‑sensitive telemetry, **edition pins** must be tracked (otherwise comparisons become irreproducible after a map/distance/policy update).
5. Row‑level summaries (for matrix rows / comparable construct groups) tend to be averaged or “smoothed”, which is incompatible with bottleneck semantics and loss honesty.

### G.7:3 - Forces

| Force                                    | Tension                                                                                                                                                                   |
| ---------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Comparability vs local authority**     | Enable comparisons across Traditions ↔ avoid overriding Context‑local meaning.                                                                                            |
| **Auditability vs authoring throughput** | Require explicit artefacts, losses, and pins ↔ keep the calibration procedure light enough to be used.                                                                    |
| **Targeted refresh vs safety**           | Emit path‑local RSCR triggers ↔ ensure triggers are typed and carry enough payload pins for audit and rerun planning.                                                     |
| **Plane awareness vs “one story”**       | Explicitly surface `ReferencePlane` and plane penalties ↔ avoid turning plane discussion into a second semantics of “sameness”.                                           |
| **QD comparability vs metric drift**     | Enable cross‑context reporting of archive/illumination telemetry ↔ enforce edition‑aware pins for descriptor/distance/policies only when those modes are actually in use. |

### G.7:4 - Solution — Bridge calibration kit (BCT + BridgeCards + RegressionSet/Sentinels)

#### G.7:4.1 - G.Core linkage (normative)

**Builds on:** `G.Core` (Part‑G core invariants; routing/delegation hub)

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
* **CN/CG note.** `CC‑GCORE‑CN‑CG‑1` is included via `GCoreConformanceProfileId.PartG.AuthoringBase` and is exercised only when contract surfaces (e.g., `CNSpecRef.edition` / `CGSpecRef.edition`) are explicitly pinned; penalty/guard policy ids (`Φ(CL)`, `Ψ(CL^k)`, `Φ_plane`) are policy pins, not contract surfaces.

*(payload pins, minimum: affected members of the effective `CorePinsRequired` (after expansion) plus any pins introduced by active extensions (e.g., QD parity pins), scoped to the watched `PathSliceId[]`/`PathId[]`/`PatternScopeId[]`.)*

#### G.7:4.2 - Kit objects (pattern‑owned surfaces)

This pattern defines the *bridge calibration kit* as a set of minimal, checkable surfaces. Semantics of `BridgeCard` and CL typing are owned by **F.9**; G.7 adds calibration artefacts and publication/wiring surfaces.

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

This subsection is kit‑owned (G.7) and complements (but does not duplicate) `G.Core` penalty routing and tri‑state guard semantics.

**Admissibility regimes (row‑level, minimal).**
* `RowCL_min` MUST take a value in `{3,2,1,0}` (value set and CL meaning are owned by F.9; G.7 owns the admissibility regime).
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
3. **Plane pins (no hidden plane mixing).** Record `ReferencePlane` pins for source/target and the relevant policy id pins for plane routing (ids only; do not duplicate policy tables).
4. **Policy pins for penalty routing.** Record the policy id pins needed to audit penalty routing (ids only). Penalty semantics are core‑owned (route via `CC‑GCORE‑PEN‑1`); G.7’s responsibility is to make the pins explicit and published.
5. **Row bottleneck discipline.** When a row aggregates multiple bridge cells, row summarisation uses bottleneck semantics (F.7) and carries a counterexample citation whenever any cell is loss‑noted.
6. **Regression and sentinel wiring.** Create/update the `RegressionSet` and `SentinelSet`. Any calibration change that can affect downstream audit (CL/CL^k/plane pins, relevant policy ids, edition pins for involved telemetry surfaces, freshness window) emits typed RSCR triggers (canonical ids; scope + payload pins).
   If the regression harness is run, record a citable `RegressionRunRef` (or equivalent run/delta reference) and attach it to the relevant ledger entries (pin‑first; no narrative-only deltas).

#### G.7:4.4 - Publication surfaces (UTS + GateCrossing harness)

A conformant G.7 publication:

* publishes UTS‑citable identifiers for `BridgeCard`s and any GateCrossing/crossing rows that rely on them,
* ensures crossing surfaces are checkable via **E.18/A.21** harnesses (lexical SD, lane purity, required pin presence),
* emits RSCR triggers using canonical `RSCRTriggerKindId` and attaches the minimum payload pins listed in §4.1.
* ensures evidence-facing citations are pin-complete: whenever bridge calibration is cited in SCR/Evidence surfaces, the citation MUST include `{BCT.id, RegressionSetId}` and the active policy id pins `{Φ(CL), Ψ(CL^k)?, Φ_plane?}` (ids only; representation is owned by `G.6`/SCR).

#### G.7:4.5 - Worked mini‑examples (informative; post‑2015; row scopes + loss notes)

> These are **working models**, not equivalence claims. They illustrate how row scope + loss notes constrain safe reuse.

1. **Preference‑learning objective (Method; RowScope = “training‑objective‑intent”).**
   *Cells:* `RLHF@Context‑A` ↔ `DPO@Context‑B` ↔ `IPO@Context‑C`
   *RowCL_min:* 2 (guarded)
   *Loss notes:* different inductive biases (reward model vs direct preference likelihood; sensitivity to preference noise model; implicit regularisation forms).
   *Use:* cross‑Tradition *didactic alignment* and eligibility hints; thresholds/acceptance remain CAL‑owned.

2. **Robustness evaluation (Measurement; RowScope = “metric‑family‑intent”).**
   *Cells:* `Accuracy@IID` ↔ `Robustness@ShiftBench` (e.g., distribution‑shift benchmarks common in post‑2019 practice)
   *RowCL_min:* 2
   *Loss notes:* shift taxonomy differs; comparability depends on pinned protocol editions and window selection; “robustness” is not a scalar substitute for accuracy.

3. **Quality‑Diversity archive comparability (Measurement; RowScope = “DescriptorMap‑only”).**
   *Cells:* `MAP‑Elites grid indices` ↔ `CVT‑MAP‑Elites centroids` ↔ `CMA‑ME archive`
   *RowCL_min:* 2
   *Loss notes:* discretisation vs centroidal tessellation; archive pressure differs; drift occurs if `DistanceDef` or insertion policy changes.
   *Use:* lawful cross‑reporting of QD telemetry when edition pins are explicit.

4. **Open‑ended transfer semantics (Method; RowScope = “transfer‑rule intent”).**
   *Cells:* `POET‑class transfer rule` ↔ `Enhanced‑POET‑class transfer rule` ↔ “modern open‑ended transfer variants”
   *RowCL_min:* 2
   *Loss notes:* environment validity region differs; transfer timing and selection pressures differ; pinning transfer rule editions is mandatory for audit.

#### G.7:4.6 - Extensions (pattern‑scoped; non‑core)

> Extensions carry *wiring only* (pins/editions/policy‑ids + which semantic owners are used). They MUST NOT redefine core invariants or defaults.

**GPatternExtension: MatrixIntake**

* **PatternScopeId:** `G.7:Ext.MatrixIntake`
* **GPatternExtensionId:** `MatrixIntake`
* **GPatternExtensionKind:** `InteropSpecific`
* **SemanticOwnerPatternId:** `G.2` *(BridgeMatrix semantics and comparable-construct inventory)*
* **Uses:** `{G.2, F.9}`
* **⊑/⊑⁺:** `∅`
* **RequiredPins/EditionPins/PolicyPins (minimum):**

  * `BridgeMatrixId` (and, if editioned: `BridgeMatrixRef.edition`)
  * `BridgeMatrixRowRef[]` *(row‑level anchors for intake; owner‑defined; e.g., `PatternScopeId` / `UTSRowId` / row ids)*
  * `ComparableConstructId[]` *(row keys; if the source does not supply a stable id, `G.7` mints one while preserving `BridgeMatrixRowRef` as the provenance anchor)*
  * `LossNoteRef[]?` *(if exported by `G.2`; otherwise authored in `G.7` and cited from the `CalibrationLedger`)*
* **RSCRTriggerKindIds:** `{RSCRTriggerKindId.CrossingSurfaceEdit, RSCRTriggerKindId.EvidenceSurfaceEdit, RSCRTriggerKindId.EditionPinChange}`
* **Notes (wiring‑only):** This module binds “row candidates” from G.2 to the BCT/Ledger intake without copying G.2 semantics into G.7.

**GPatternExtension: DHCAccounting**

* **PatternScopeId:** `G.7:Ext.DHCAccounting`
* **GPatternExtensionId:** `DHCAccounting`
* **GPatternExtensionKind:** `DisciplineSpecific`
* **SemanticOwnerPatternId:** `C.21` *(DHC metric semantics, including AlignmentDensity)*
* **Uses:** `{C.21}`
* **⊑/⊑⁺:** `∅`
* **RequiredPins/EditionPins/PolicyPins (minimum; conditional on use):**

  * `AlignmentDensityMethodRef.edition?`
  * `DeclaredUnitsRef?` *(units declaration style per owner; e.g., “bridges_per_100_DHC_SenseCells”)*
* **RSCRTriggerKindIds:** `{RSCRTriggerKindId.TelemetryDelta, RSCRTriggerKindId.PolicyPinChange, RSCRTriggerKindId.EditionPinChange}`
* **Notes (wiring‑only):**
  * G.7 stores the *counts and declared units* as a surface; C.21 owns the meaning and legality constraints.
  * When reporting AlignmentDensity, the counted bridge set is typically restricted to `CL ≥ 2` (treat `CL=3` as “free substitution”, `CL=2` as “guarded” for reporting); conformance is enforced by `CC‑G7‑DHC‑Units‑1` while semantics remain owned by `C.21`.

**GPatternExtension: QDParityPins**

* **PatternScopeId:** `G.7:Ext.QDParityPins`
* **GPatternExtensionId:** `QDParityPins`
* **GPatternExtensionKind:** `InteropSpecific`
* **SemanticOwnerPatternId:** `C.18` *(QD artefact semantics; uses C.19 for exploration/logging pins as needed)*
* **Uses:** `{C.18, C.19}`
* **⊑/⊑⁺:** `∅`
* **RequiredPins/EditionPins/PolicyPins (minimum; conditional on use):**

  * `DescriptorMapRef.edition`
  * `DistanceDefRef.edition`
  * `InsertionPolicyRef` *(policy id or pinned policy ref, per owner semantics)*
* **RSCRTriggerKindIds:** `{RSCRTriggerKindId.EditionPinChange, RSCRTriggerKindId.PolicyPinChange, RSCRTriggerKindId.TelemetryDelta, RSCRTriggerKindId.FreshnessOrDecayEvent}`
* **Notes (wiring‑only):** Enforces reproducibility of cross‑Context archive/illumination comparisons without pulling QD semantics into the core bridge kit.
  The pins from this module should be attached via `RowEntry.ExtensionPins[QDParityPins]` (or an equivalent extension‑pin map) and included in `BridgeSentinel.payloadPins` whenever the watched scope consumes QD telemetry.

**GPatternExtension: SoSLogClauses**

* **PatternScopeId:** `G.7:Ext.SoSLogClauses`
* **GPatternExtensionId:** `SoSLogClauses`
* **GPatternExtensionKind:** `InteropSpecific`
* **SemanticOwnerPatternId:** `C.23` *(SoS‑LOG rule and branch semantics; G.7 does not redefine meaning)*
* **Uses:** `{C.23, G.6}`
* **⊑/⊑⁺:** `∅`
* **RequiredPins/EditionPins/PolicyPins (minimum; conditional on use):**
  * `SoSLogRuleId[]` *(or owner‑equivalent ids)*
  * `FailureBehaviorPolicyId?` *(policy id, when degrade behavior is bound)*
  * `PathId/PathSliceId` citations for explainability (via `G.6`)
  * `BridgeCardId[]` (bridges whose reuse is being justified)
* **RSCRTriggerKindIds:** `{RSCRTriggerKindId.PolicyPinChange, RSCRTriggerKindId.EvidenceSurfaceEdit, RSCRTriggerKindId.CrossingSurfaceEdit, RSCRTriggerKindId.MaturityRungChange}`
* **Notes (wiring‑only):** Ensures cross‑Tradition bridge reuse decisions can be justified by citing SoS‑LOG clauses and evidence paths, without embedding SoS‑LOG semantics into G.7.

**GPatternExtension: AcceptanceHooks**

* **PatternScopeId:** `G.7:Ext.AcceptanceHooks`
* **GPatternExtensionId:** `AcceptanceHooks`
* **GPatternExtensionKind:** `MethodSpecific`
* **SemanticOwnerPatternId:** `G.4` *(Acceptance/threshold/unknown handling; G.7 does not define thresholds)*
* **Uses:** `{G.4}`
* **⊑/⊑⁺:** `∅`
* **RequiredPins/EditionPins/PolicyPins (minimum; conditional on use):**
  * `AcceptanceClauseId[]` *(or owner‑equivalent ids)*
  * `AcceptancePolicyId?` *(policy id when acceptance behavior is pinned)*
  * `BridgeCardId[]` (bridges whose calibrated status is being used as a gate input)
* **RSCRTriggerKindIds:** `{RSCRTriggerKindId.PolicyPinChange, RSCRTriggerKindId.BaselineBindingEdit, RSCRTriggerKindId.LegalitySurfaceEdit}`
* **Notes (wiring‑only):** When bridges are used as selector gates, thresholds and unknown-handling remain Acceptance-owned; this module only pins the linkage and refresh relevance.

**GPatternExtension: AdvancedCalibrationProcedures (Phase‑3 seed)**

* **PatternScopeId:** `G.7:Ext.AdvancedCalibrationProcedures`
* **GPatternExtensionId:** `AdvancedCalibrationProcedures`
* **GPatternExtensionKind:** `Phase3Seed`
* **SemanticOwnerPatternId:** `owner TBD`
* **Uses:** `{ }`
* **⊑/⊑⁺:** `∅`
* **RequiredPins/EditionPins/PolicyPins:** `owner TBD`
* **RSCRTriggerKindIds:** `{RSCRTriggerKindId.CrossingSurfaceEdit, RSCRTriggerKindId.PenaltyPolicyEdit, RSCRTriggerKindId.ReferencePlaneEdit}`
* **Notes (seed; non‑normative):** Placeholder for domain‑specific / statistical calibration families beyond the minimal auditable procedure (e.g., uncertainty‑aware calibration, probabilistic mapping). No Part‑G‑wide norms are introduced.

### G.7:5 - Archetypal Grounding (System / Episteme)

**System (Γ_sys):** *Cross‑standard safety assurance comparison (bridge‑first).*
A team must compare a safety assurance claim across two regulatory Traditions (e.g., a “functional safety case” tradition and a “ML system testing” tradition) for the *same physical system scope*. `G.7` forces explicit SenseCell‑level bridges (what exactly is the “hazard”, what is the “evidence carrier”, what is the “pass criterion”), records losses, pins planes, and provides sentinels so that changes in the safety evidence protocol editions trigger path‑local RSCR rather than re‑authoring the entire safety case.

**Episteme (Γ_epist):** *Benchmark protocol pluralism (post‑2015 evaluation practice).*
A research group wants to compare “state‑of‑the‑art” across multiple evaluation Traditions (IID performance, shift robustness, preference‑based evaluation). `G.7` turns “these are comparable” into explicit BridgeCards with declared row scope, pins the evaluation protocol editions, and emits sentinels so that when a benchmark protocol or policy pin changes, downstream selector decisions can be re‑audited by re‑citing the same PathSlice‑scoped evidence.

### G.7:6 - Bias‑Annotation

Lenses tested: **Gov**, **Arch**, **Onto/Epist**, **Prag**, **Did**.
Scope: Universal for the bridge calibration kit; any method‑family or discipline‑specific calibration technique is modularized as `GPatternExtension` and cited to its semantic owners.

### G.7:7 - Conformance Checklist (normative) — **CC‑G7**

| ConformanceId             | Requirement                                                                                                                                                                                                                                                                               | Purpose                                                                        |
| ------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------ |
| **CC‑G7‑CoreRef**         | `G.7` is conformant only if it satisfies the effective `G.Core` obligations declared by the `GCoreLinkageManifest` in **§4.1** (after nil‑elision and expansion of profile/set/pinset ids), including any explicit deltas listed there. | Make universal invariants single‑owner and enforce citation‑based reuse.       |
| **CC‑G7‑BCT‑1**           | For any active `TradPairId` with cross‑Tradition reuse, a `BridgeCalibrationTable (BCT)` **MUST** exist, declare a `FreshnessWindowRef`, and provide `RowEntry` records that cite, at minimum: `RowEntryId`, `ComparableConstructId`, `RowScopeId`, `BridgeCardId[]`, `RowCL_min`, `PlanePins {ReferencePlane(src), ReferencePlane(tgt)}`, `PolicyPins {Φ(CL)}` (and `Ψ(CL^k)?`, `Φ_plane?` when applicable), plus `{RegressionSetId, SentinelSetId}`. | Ensure the kit exists as an auditable object rather than a prose matrix.       |
| **CC‑G7‑BridgeCard‑1**    | Any bridge published by G.7 **MUST** be consumable as an **F.9** `BridgeCard` and **MUST** be SenseCell‑anchored (directly or via explicit SenseCell anchor refs).                                                                                                                        | Prevent “Context‑only” or ambiguous bridges.                                   |
| **CC‑G7‑UTS‑1**           | G.7 outputs **MUST** mint/publish UTS‑citable ids (NameCards/twin labels as applicable) for (a) each BridgeCard (or its NameCard) and (b) each GateCrossing/crossing row that makes bridge use checkable; and **MUST** expose the resulting `UTSRowId[]` in the BCT/Ledger/crossing surfaces. *(UTS discipline is delegated to `CC‑GCORE‑UTS‑1`.)* | Make bridge calibration externally citable and checkable.                      |
| **CC‑G7‑RowScope‑1**      | Every BCT row **MUST** declare its `RowScopeId` (what notion of “sameness” is claimed), and any loss notes **MUST** be recorded as citable artefacts (refs/ids), not only narrative text.                                                                                                 | Keep reuse honest and locally bounded.                                         |
| **CC‑G7‑CLRegime‑1**      | Every BCT row **MUST** record `RowCL_min` (and `RowCL_k_min?`, `RowCL_plane_min?` where applicable) and apply the admissibility regime from §4.2.1: `≥2` admissible; `=1` only with cited `WaiverRef[]`; `=0` forbidden for reuse. The honesty rule must be satisfied: ≥1 counterexample for `≤2`, and an explicit stated‑absence disclosure for `=3` when no counterexample is cited. | Make CL/waiver/plane regimes explicit and auditable at kit level.              |
| **CC‑G7‑SCRLinkage‑1**    | Whenever bridge calibration is cited in SCR/Evidence surfaces, the citation **MUST** include `{BridgeCardId[]}` (or `UTSRowId[]` for the bridge artefacts), an explicit row locator (`RowEntryId` or equivalent), `{BCT.id, RegressionSetId}`, and the active policy id pins `{Φ(CL), Ψ(CL^k)?, Φ_plane?}` (ids only; representation owned elsewhere). | Prevent “pins exist but are not visible/auditable” failure mode.               |
| **CC‑G7‑SoSLOG‑Pins‑1**   | When `G.7:Ext.SoSLogClauses` is in use, G.7 outputs **MUST** expose the cited SoS‑LOG rule ids and the relevant `PathId/PathSliceId` evidence citations; any change in those pins **MUST** be RSCR‑relevant per `CC‑GCORE‑TRIG‑1…TRIG‑4`.                                               | Keep cross‑Tradition reuse explainable without embedding C.23 semantics.        |
| **CC‑G7‑Acceptance‑1**    | When `G.7:Ext.AcceptanceHooks` is in use, G.7 outputs **MUST** expose the Acceptance clause ids/policy ids used as gates; thresholds/unknown handling remain Acceptance-owned; any change **MUST** be RSCR‑relevant per `CC‑GCORE‑TRIG‑1…TRIG‑4`.                                           | Keep thresholds and unknowns out of bridges while preserving auditability.     |
| **CC‑G7‑RowBottleneck‑1** | If a comparable construct row aggregates multiple bridge cells, row summaries (e.g., `RowCL_min`) **MUST** follow bottleneck discipline (F.7) and cite a counterexample whenever a cell carries a loss note.                                                                              | Forbid “CL averaging” and enforce loss‑aware summaries.                        |
| **CC‑G7‑PolicyPins‑1**    | G.7 outputs **MUST** publish the *policy id pins* required to audit penalty routing and plane effects (ids only), as required by `CC‑GCORE‑LINK‑1/2` and `CC‑GCORE‑PEN‑1`. G.7 MUST NOT duplicate policy tables or redefine penalty semantics.                                           | Keep penalty routing auditable while preserving single‑owner policy semantics. |
| **CC‑G7‑GateCrossing‑1**  | Any published crossing rows that rely on bridges **MUST** be checkable via GateCrossing/CrossingSurface harnesses (E.18/A.21): required pins are present; lexical constraints and lane purity checks are runnable.                                                                        | Make crossings checkable, not narrative.                                       |
| **CC‑G7‑Sentinels‑1**     | G.7 **MUST** register `BridgeSentinel` entries for bridges used by live scopes and **MUST** emit typed RSCR triggers (canonical `RSCRTriggerKindId`; see `CC‑GCORE‑TRIG‑1…TRIG‑4`) on calibration‑relevant edits, scoped to the watched `PathSliceId[]` or `PatternScopeId[]`, with the minimum payload pins from §4.1. | Enable targeted refresh rather than pack‑wide reruns.                          |
| **CC‑G7‑QD‑Pins‑1**       | When `G.7:Ext.QDParityPins` is in use, G.7 outputs **MUST** include `{DescriptorMapRef.edition, DistanceDefRef.edition, InsertionPolicyRef}` and treat any change to those pins as RSCR‑relevant per `CC‑GCORE‑TRIG‑1…TRIG‑4`.                                                          | Prevent silent QD telemetry drift.                                             |
| **CC‑G7‑DHC‑Units‑1**     | When AlignmentDensity (or related DHC accounts) are reported, G.7 outputs **MUST** (a) restrict the counted bridge set to rows with `RowCL_min ≥ 2` (treat `CL=3` as “free substitution”, `CL=2` as “guarded” for reporting), (b) include declared units, and (c) cite the relevant DHC method semantics (C.21). G.7 MUST NOT invent arithmetic over ordinal/illegal surfaces. | Keep dashboards and discipline‑health metrics lawful and interpretable.        |

### G.7:8 - Common Anti-Patterns and How to Avoid Them

* **Bridge‑by‑prose (“they mean the same thing”).**
  **Avoid:** publish BCT rows + BridgeCards + UTS rows; require SenseCell anchoring and row scopes.
* **SenseFamily jump (scope‑bridge used as kind‑bridge).**
  **Avoid:** keep channel/sense‑family constraints owned by **F.9** visible; use `RowScopeId` to state which channel is claimed, and require `CL^k` + `Ψ(CL^k)` pins when a kind‑channel bridge is invoked (do not “upgrade” a scope‑channel bridge into kind substitution).
* **Plane blindness (“concept = world”).**
  **Avoid:** record plane pins and policy id pins; keep plane effects auditable and separable from CL/CL^k semantics.
* **CL smoothing / averaging.**
  **Avoid:** enforce row bottleneck summaries and counterexample citations for loss‑noted cells.
* **Pack‑wide refresh on a local bridge edit.**
  **Avoid:** register sentinels scoped to `PathSliceId` and emit typed RSCR triggers with minimal payload pins.
* **QD metric drift by unpinned artefacts.**
  **Avoid:** enable `G.7:Ext.QDParityPins` only when needed and require edition/policy pins when enabled.

### G.7:9 - Consequences

* **Auditable pluralism.** Cross‑Tradition reuse becomes explicit, loss‑aware, and checkable.
* **Targeted, edition‑aware refresh.** Calibration drift triggers path‑scoped RSCR rather than expensive global reruns.
* **Downstream cleanliness.** Selectors/logging/shipping can cite bridges and policy pins without inventing local crossing rules or shadow specs.

### G.7:10 - Rationale

* **Why a kit (not a new contract surface)?** Bridge calibration must support many downstream consumers without becoming a competing legality gate; contract semantics remain owned by `CG‑Spec`/`CN‑Spec`.
* **Why BCT + RegressionSet + SentinelSet?** Because calibration without regression tests drifts silently, and regression without sentinels is operationally unusable (refresh becomes global).
* **Why row scopes?** Because “comparable” is not one thing; scope must be explicit to avoid accidental substitution.

### G.7:11 - SoTA‑Echoing (post‑2015, for orientation; non‑normative)

* **Edition‑aware evaluation and dataset shift practice.** Post‑2018 evaluation culture (robustness and shift benchmarks, protocol pinning, reproducibility checklists) motivates treating protocol versions and “what changed” as first‑class pins rather than prose.
* **Preference‑based optimisation families.** Modern preference‑learning lines (late‑2010s → 2020s) show how neighbouring objectives can share intent but diverge in assumptions—an archetypal case for row scope + loss notes.
* **Quality‑Diversity and differentiable QD.** MAP‑Elites successors (CVT variants, CMA‑ME line, differentiable QD ecosystems) emphasise archive/descriptor/distance artefacts whose editions must be pinned for comparability.
* **Open‑ended evolution and transfer‑rule portfolios.** POET‑class work motivates explicit transfer rule editions and environment validity regions as pins when bridges are used for cross‑tradition reporting.

### G.7:12 - Relations

**Builds on:** `G.Core`, `G.2`, `F.3`, `F.7`, `F.9`, `B.3`, `E.10`, `E.18`, `A.21`, `G.6`, `C.21`.
**Optionally uses via Extensions:** **G.4** (Acceptance hooks), **C.23** (SoS‑LOG clauses), **C.18/C.19** (QD/OEE pins).
**Used by / prerequisite for:** **G.5** (cross‑Tradition eligibility/selection), **G.11** (refresh orchestration), **G.9** (parity across Traditions where bridges are required), **G.10** (shipping surfaces that must cite bridge calibration ids), **G.12** (DHC dashboards when bridge counts/units are surfaced).
**Publishes to:** **UTS** (bridge and crossing rows; twin labels as applicable) and emits RSCR‑ready telemetry/trigger payloads for **G.11**.
**Constrains:** Any downstream consumer that claims cross‑Context/Tradition reuse must use the calibrated bridge artefacts/pins surfaced by this kit (core‑owned crossing invariants apply).

### G.7:End

## G.8 - SoS‑LOG Bundles & Maturity Ladders

**Tag.** Architectural pattern (packaging kit).
**Stage.** Design‑time packaging (authoring & publication) with a run‑time consumption facade for `G.5` (selector/registry).
**Primary hooks:** `G.Core` (Part‑G invariants), `C.23` (SoS‑LOG semantics), `C.22` (TaskSignature), `G.4` (Acceptance & EvidenceProfiles), `G.6` (EvidenceGraph & `PathId/PathSliceId`), `G.5` (registry/selector), `G.11` (refresh orchestration), `G.10` (shipping boundary), `F.9` (BridgeCard & CL), `G.7` (bridge calibration & Φ/Ψ/Φ_plane), `F.8` (Policy pins: `PolicySpecRef`/`MintDecisionRef` resolvability), `A.10` (anchors), `E.10` (LEX twin registers), `E.5.2` (notational independence), `E.18/A.21/A.27` (GateCrossing visibility).

**Non‑duplication note (Phase‑2 universalization).** This pattern introduces **kit‑owned packaging surfaces** for SoS‑LOG bundles and maturity ladders. All **Part‑G‑wide invariants** (no shadow specs, Bridge‑only crossings + visibility, tri‑state guard domain, penalties→`R_eff`‑only, set‑return semantics, P2W split, typed RSCR triggers + alias docking, single‑owner defaults, shipping boundary) are **routed via `G.Core`** and are not restated here.

**Modularity note (policy‑id pins are reference‑only).** This kit may pin/cite policy ids (e.g., `Φ/Ψ/Φ_plane` policies, `FailureBehaviorPolicyId`, illumination‑promotion policy ids, and E/E‑LOG policy ids) **as references only**. Conformance relies on the policy‑pin resolvability discipline of `F.8:8.1` (i.e., policy ids are not “inlined”; and when newly minted, they are backed by resolvable `PolicySpecRef` + `MintDecisionRef`). `G.8` does not define policy semantics and MUST NOT silently mint policy ids.

### G.8:1 - Problem frame

Method families compete within a `CG‑Frame`, but dispatch is only lawful if (i) admissibility decisions remain **tri‑state** and auditable, (ii) evidence and crossings are **explicitly citable** (by ids, not prose), and (iii) selection preserves **set/portfolio semantics** under partial orders. In practice, SoS‑LOG rules (`C.23`) and “maturity stories” are often distributed across prose, dashboards, and ad‑hoc checklists, with thresholds embedded where they do not belong and with missing pins for evidence paths, crossings, and editions.

This pattern provides the missing packaging kit: a **selector‑facing, UTS‑citable bundle** that binds **(a)** rule ids (semantics owned by `C.23`), **(b)** an ordinal/poset maturity ladder (published as a citable card), and **(c)** explicit wiring to Acceptance (`G.4`), EvidenceGraph (`G.6`), selection/registry (`G.5`), and refresh (`G.11`)—without creating any shadow contract surfaces.

### G.8:2 - Problem

1. **Selector needs a stable input artefact.** `G.5` cannot consume “maturity narratives” and scattered SoS‑LOG snippets without re‑authoring semantics or inventing implicit defaults.
2. **Thresholds leak into LOG.** Numeric gates are often embedded directly into rule text or ladder rungs, blurring the boundary between LOG decisions (`C.23`) and Acceptance thresholds (`G.4`).
3. **Auditability is brittle.** Decisions (`pass/degrade/abstain`) lack stable, citable links to evidence paths (`G.6`) and crossing pins (Bridge/CL/Φ policy ids), so later re‑checks and RSCR become ad‑hoc.
4. **Telemetry contaminates decision semantics.** QD/OEE/illumination signals are frequently treated as dominance inputs without explicit policy pins; edition drift then silently changes outcomes.
5. **Refresh is under‑specified.** Bundle evolution (rules, ladders, pins, policies, editions) must be RSCR‑addressable via typed trigger kinds, not by free‑text “reasons”.

### G.8:3 - Forces

| Force                                        | Tension                                                                                                      |
| -------------------------------------------- | ------------------------------------------------------------------------------------------------------------ |
| **Pluralism vs. dispatchability**            | Preserve multiple method families and partial orders ↔ still provide a consumable artefact for `G.5`.        |
| **Auditability vs. authoring friction**      | Fine‑grained pins and citations ↔ keeping authoring lightweight and notation‑independent.                    |
| **Maturity as poset vs. scalar ranking**     | Maturity is inherently non‑scalar ↔ teams want a “single readiness number”.                                  |
| **Telemetry richness vs. decision hygiene**  | Rich QD/OEE telemetry ↔ avoid illegitimate promotion into dominance without explicit policy.                 |
| **Design‑time packaging vs. run‑time trace** | Authoring produces stable bundles ↔ run‑time produces branch‑specific path traces and admissibility ledgers. |
| **Interoperability vs. crossing discipline** | Reuse across contexts/planes ↔ prevent implicit crossings (Bridge‑only + visible).                           |

### G.8:4 - Solution — Publish SoS‑LOG bundles and maturity cards as UTS‑citable kit

#### G.8:4.1 - G.Core linkage (normative)

**Builds on:** `G.Core` (Part‑G core invariants; routing/delegation hub)

**GCoreLinkageManifest (normative; size‑controlled).**
*(Canonical shape, Nil‑elision, and Expansion rule are per `G.Core:4.2`.)*

**Separation rule (Phase‑2).** Method‑/generator‑specific pins are **normatively specified** only inside `Extensions` as `GPatternExtension` modules (see `G.8:5.*`). The bundle/ledger schema may mention such fields only as **extension‑gated optionals**, with the authoritative pin/edition/policy requirements stated in the corresponding extension block. The core linkage manifest lists only base‑kit pins and Part‑G‑wide linkage.

`GCoreLinkageManifest := ⟨
CoreConformanceProfileIds := {
GCoreConformanceProfileId.PartG.AuthoringBase,
GCoreConformanceProfileId.PartG.TriStateGuard,
GCoreConformanceProfileId.PartG.UTSWhenPublicIdsMinted,
GCoreConformanceProfileId.PartG.ShippingBoundary
},

RSCRTriggerSetIds := { GCoreTriggerSetId.EvidenceGraphKit },

CorePinSetIds := {
GCorePinSetId.PartG.AuthoringMinimal,
},

CorePinsRequired := {
  // Pattern-owned public ids (strengthen conditional pins where G.8 publishes UTS artefacts)
  UTSRowId[],                    // bundle/ledger/card rows + any referenced UTS rows
  SoS‑LOGBundleRef,
  SoSLogRuleId[],
  MethodFamilyId,
  HomeContext,

  // Closed value sets (ids only; UTS-registered)
  DegradeModeEnum,
  MaturityRungs,

  // Maturity ladder pins
  MaturityCardRef,               // required; recommended: published as separate UTS artefact
  MaturityRungId?,               // iff a specific rung is asserted at packaging/run-time

  // Evidence / provenance pins
  A10EvidenceGraphRef?[],        // packaging-time A.10 carriers (when PathId/PathSliceId not yet available)
  EvidenceGraphId?,              // iff resolvable to G.6 EvidenceGraph
  PathId[]/PathSliceId[]?,       // run-time ledgers typically have them

  // Authoring traceability (SoTA-of-description)
  AuthoringMethodDescriptionRefs?[],  // edition-pinned method-description refs
},

DefaultsConsumed := {
DefaultId.PortfolioMode,
DefaultId.DominanceRegime,
DefaultId.GammaFoldForR_eff
},
⟩`

*(RSCR payload pins typically include: `SoS‑LOGBundleRef`, `SoSLogRuleId[]`, `MaturityRungId?`, and `EvidenceGraphId/PathId/PathSliceId?`.  
Crossing payload pins (Bridge/CL/Φ/Ψ/Φ_plane) are introduced **only when reuse is asserted**, via `G.8:Ext.BridgeReuseWiring`.  
Method-/generator‑specific payload pins are listed only inside the relevant `GPatternExtension` blocks in `G.8:5`.)*

*(Conditionality note for defaults.)* Include `DefaultId.GammaFoldForR_eff` in `DefaultsConsumed` **only if** the bundle/ledger exports aggregated `R_eff` summaries (otherwise Nil‑elide it).

#### G.8:4.2 - Kit: objects and naming discipline (LEX heads; twin‑register safe)

**Objects / surfaces (pattern‑owned).**

* **`SoS‑LOG.Rule`**
  A rule id that denotes an executable tri‑state decision schema `{pass | degrade(mode) | abstain}` for `(TaskSignature, MethodFamily)`. *(“pass” may be described as “admit” in prose, but the normative tri‑state vocabulary is `G.Core`’s `{pass|degrade|abstain}`.)*
  **Semantics are owned by `C.23`.** `G.8` only packages rule ids and binding pins.

* **`SoS‑LOGBundle@Context`**
  A selector‑facing, notation‑independent packaging object published to UTS.

* **`AdmissibilityLedger@Context`**
  A run‑time ledger view that records admissibility outcomes, cited evidence paths, branch tokens, and the pins required for audit/refresh.

* **`MethodFamily.MaturityCardDescription@Context`**
  A maturity ladder description published as a citable artefact: **ordinal/poset**, closed rungs, `ReferencePlane` declared; no thresholds inside.

**Naming discipline (E.10 + “Spaces ≠ Maps”).**

* Technical heads are normative; Plain twins are didactic only and MUST NOT cross kinds.
* Do **not** alias `CharacteristicSpace` and `DescriptorMap`.

  * `DescriptorMapRef` is a **map‑reference** (typically used with QD archives).
  * `CharacteristicSpaceRef` is a **space‑reference** (grid/cell semantics, if used).
* Editions are pinned on `…Ref.edition` fields (not on informal names).

#### G.8:4.3 - `SoS‑LOGBundle@Context` schema (conceptual; notation‑independent)

A conforming bundle is a UTS‑published object whose internal representation is free, but whose **field meanings** are stable:

```
SoS-LOGBundle@Context :=
⟨
  UTS.id := SoS‑LOGBundleRef,
  Edition,

  // Scope + contract pins (from GCorePinSetId.PartG.AuthoringMinimal)
  CG-FrameContext,
  describedEntity := ⟨GroundingHolon, ReferencePlane⟩,
  CNSpecRef.edition,
  CGSpecRef.edition,

  MethodFamilyId,
  HomeContext,

  SoSLogRuleId[] ,               // ids only; semantics owned by C.23
  ClosedEnums: {DegradeModeEnum, MaturityRungs},  // ids only; UTS-registered closed value sets
  A10EvidenceGraphRef?[] ,        // packaging-time evidence carriers (A.10 anchors) when paths are not yet stable
  MaturityCardRef ,               // UTS ref to maturity card (required; may be embedded but MUST be citable)
  MaturityRungId? ,               // if a specific rung is asserted at packaging time

  // Optional: Acceptance wiring (thresholds remain owned by G.4)
  AcceptanceClauseId[]? ,

  // Optional: Evidence wiring (for later audit & rung transition justification)
  EvidenceGraphId? ,
  PathId[]/PathSliceId[]? ,

  // Optional: cross-context/plane wiring (only when reuse is asserted)
  BridgeId/BridgeCardId? ,
  CL/CL^k/CL^plane? ,
  Φ/Ψ/Φ_plane policy-ids? ,

  // Optional: selector semantics pins (explicit value or resolved via DefaultOwnershipIndex)
  PortfolioMode? ,
  DominanceRegime? ,

  // Optional: QD / OEE pins (only when those surfaces are declared)
  CharacteristicSpaceRef.edition? ,
  DescriptorMapRef.edition? ,
  DistanceDefRef.edition? ,
  EmitterPolicyRef? ,
  InsertionPolicyRef? ,
  // Optional: Open-ended pins (only when those surfaces are declared)
  GeneratorFamilyId? ,
  EnvironmentValidityRegionId? ,
  CouplerPolicyId? ,
  TransferRulesRef.edition? ,

  // Optional: branch/failure wiring (policy-bound)
  FailureBehaviorPolicyId? ,
  SoSLogBranchId[]? ,

  // Optional: authoring traceability (SoTA-of-description)
  AuthoringMethodDescriptionRefs?[] ,

  Notes
⟩
```

**Bundle discipline (normative intent; semantics routed):**

* `SoS‑LOGBundle@Context` **does not introduce** new legality or normalization rules; it cites the contract surfaces pinned above.
* Thresholds and numeric gates are cited by id from `G.4` Acceptance (no embedding inside the bundle).
* If cross‑context/plane reuse is asserted, crossing pins are made explicit (Bridge/CL/Φ policy ids), and evidence paths are citable when available.

**Binding obligations B1–B5 (packaging‑only; wiring‑only; semantics routed):**

* **B1 — Evidence wiring.** At packaging time the bundle SHOULD provide resolvable evidence refs (typically `A10EvidenceGraphRef?[]` and/or `EvidenceGraphId?`). At run time, admissibility outcomes SHOULD cite `PathId/PathSliceId` when available (`G.6`), so rung transitions and `degrade/abstain` traces are audit‑stable.
* **B2 — CL/plane routing pins.** When reuse across Context/plane is asserted, the bundle/ledger MUST pin the relevant Bridge/CL/Φ/Ψ/Φ_plane policy ids (reference‑only; resolvable per `F.8:8.1`) and MUST respect the core penalty routing (penalties affect `R_eff` only; `F/G` invariance via `G.Core`).
* **B3 — Portfolio/QD fields.** If the bundle/ledger exposes QD/portfolio fields (e.g., `PortfolioMode=Archive`), it MUST pin the descriptor/distance/insertion/emitter artefacts (editions/policies as applicable). Illumination remains **report‑only** unless explicitly promoted by a `G.4` owner policy id that is pinned and recorded in the run‑time trace.
* **B4 — Open‑ended fields.** If the bundle binds an open‑ended generator family, it MUST pin `GeneratorFamilyId` and `TransferRulesRef.edition` (and any validity region/coupler policy ids when used). Unknown transfer validity MUST route to `degrade`/branching, not to an ad‑hoc fourth status.
* **B5 — Telemetry hooks.** On any material telemetry event (illumination increase, archive insertion, probe accounting update, open‑ended coverage/regret proxy update), the emitted telemetry pins SHOULD include the controlling policy ids plus the relevant edition pins (e.g., `DescriptorMapRef.edition`, `DistanceDefRef.edition`, `TransferRulesRef.edition`) and, when available, `PathSliceId` to keep RSCR planning auditable.

#### G.8:4.4 - `AdmissibilityLedger@Context` (run‑time view; selector‑facing)

A conforming ledger is a UTS‑published view (or a view‑projection of a Work/Audit artefact) with rows of the form:

`⟨ MethodFamilyId, SoSLogRuleId, GuardDecision ∈ {pass|degrade|abstain}, DegradeMode?/SoSLogBranchId[]?, MaturityRungId?, AcceptanceClauseId[]?, EvidencePathRefs?, CrossingPins?, PortfolioMode?, DominanceRegime?, Edition ⟩`

Where `EvidencePathRefs` are typically `PathId[]/PathSliceId[]` when `G.6` is in use (or resolvable), and “CrossingPins” are the explicit Bridge/CL/Φ policy pins when reuse is asserted.

#### G.8:4.5 - Maturity ladder as a citable poset (published card)

`MethodFamily.MaturityCardDescription@Context` is published with:

* closed rungs (UTS‑registered identifiers),
* `Scale kind = ordinal` and a declared `ReferencePlane`,
* (optional) explicit poset edges / precedence constraints,
* rung transition justifications that cite evidence paths (typically `G.6` paths).

This card is a **description** suitable for dispatch/audit and refresh; it is not a competing contract surface.

#### G.8:4.6 - Interfaces (minimal I/O standard; conceptual)

| Interface                               | Consumes                                                                                   | Produces                                                                              |
| --------------------------------------- | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------- |
| **G.8‑1 `Publish_LOGBundle`**           | `MethodFamilyId`, `SoSLogRuleId[]` (C.23), pins to Acceptance/Evidence/Crossings (as applicable) | `SoS‑LOGBundle@Context` (UTS row)                                                     |
| **G.8‑2 `Publish_AdmissibilityLedger`** | Bundle + run‑time branch outcomes + evidence path refs (when available)                    | `AdmissibilityLedger@Context` (UTS row or UTS‑citable view)                           |
| **G.8‑3 `Publish_MaturityCard`**        | Ladder description + (optional) evidence path refs for rung transitions                    | `MaturityCardDescription@Context` (UTS row; editioned)                                |
| **G.8‑4 `Expose_TelemetryHooks`**       | QD/OEE/archive/open‑ended telemetry signals (when declared)                                | telemetry pins for refresh (`…Ref.edition`, policy‑ids, `PathSliceId` when available) |

### G.8:5 - Extensions (pattern‑scoped; non‑core)

`G.8` keeps method/generator specificity out of the core kit. Any such specificity appears as `GPatternExtension` blocks with stable **PatternScopeId**s.

#### G.8:5.1 - `G.8:Ext.SoSLOGWiring`

**PatternScopeId:** `G.8:Ext.SoSLOGWiring`
**GPatternExtensionId:** `SoSLOGWiring`
**GPatternExtensionKind:** `MethodSpecific`
**SemanticOwnerPatternId:** `C.23`
**Uses:** `{C.23}`
**⊑/⊑⁺:** `∅`
**RequiredPins/EditionPins/PolicyPins (minimum):**

* `SoSLogRuleId[]`
* `SoSLogBranchId[]?`
* `FailureBehaviorPolicyId?` *(when degrade behaviour is policy‑bound)*

**RSCRTriggerSetIds / RSCRTriggerKindIds:** `∅` *(covered by `G.8:4.1`)*
**Notes (wiring‑only):**
* Rule meaning, branch taxonomy, and “probe/sandbox” semantics are owned by `C.23`; this module only binds ids and pins.

#### G.8:5.2 - `G.8:Ext.AcceptanceWiring`

**PatternScopeId:** `G.8:Ext.AcceptanceWiring`
**GPatternExtensionId:** `AcceptanceWiring`
**GPatternExtensionKind:** `MethodSpecific`
**SemanticOwnerPatternId:** `G.4`
**Uses:** `{G.4}`
**⊑/⊑⁺:** `∅`
**RequiredPins/EditionPins/PolicyPins (minimum):**

* `AcceptanceClauseId[]`
* `EvidenceProfileId[]?` *(if the ledger/bundle cites evidence profile ids rather than only paths)*
* `PromotionPolicyId?` *(only if telemetry may be promoted into dominance by explicit CAL policy)*

**RSCRTriggerKindIds (optional delta):** `{RSCRTriggerKindId.PolicyPinChange}` *(only if acceptance policies are pinned as ids in the bundle/ledger)*
**Notes (wiring‑only):**
* Thresholds remain owned by `G.4` Acceptance; this module carries only clause ids and policy pins.

#### G.8:5.3 - `G.8:Ext.BridgeReuseWiring`

**PatternScopeId:** `G.8:Ext.BridgeReuseWiring`
**GPatternExtensionId:** `BridgeReuseWiring`
**GPatternExtensionKind:** `InteropSpecific`
**SemanticOwnerPatternId:** `G.7`
**Uses:** `{G.7, F.9}`
**⊑/⊑⁺:** `∅`
**RequiredPins/EditionPins/PolicyPins (minimum):**

* `BridgeId/BridgeCardId`
* `CL/CL^k/CL^plane`
* `Φ/Ψ/Φ_plane policy-ids`
* `BridgeCalibrationTableId?`, `RegressionSetId?` *(if cited as calibration evidence)*

**RSCRTriggerSetIds:** `{GCoreTriggerSetId.BridgeCalibrationKit}` *(only if the bundle/ledger explicitly binds calibration artefacts by id)*
**Notes (wiring‑only):**
* Present only when `SoS‑LOGBundle@Context` asserts cross‑Context/plane reuse. No additional crossing semantics are defined here.

#### G.8:5.4 - `G.8:Ext.QDArchiveTelemetry`

**PatternScopeId:** `G.8:Ext.QDArchiveTelemetry`
**GPatternExtensionId:** `QDArchiveTelemetry`
**GPatternExtensionKind:** `MethodSpecific`
**SemanticOwnerPatternId:** `C.18`
**Uses:** `{C.18, G.5}`
**⊑/⊑⁺:** `∅`
**RequiredPins/EditionPins/PolicyPins (minimum):**

* `DescriptorMapRef.edition`
* `DistanceDefRef.edition`
* `EmitterPolicyRef`
* `InsertionPolicyRef`
* `CharacteristicSpaceRef.edition?` *(required iff cell boundaries / de‑dup / parity depend on the space definition)*

**RSCRTriggerKindIds:** `{RSCRTriggerKindId.TelemetryDelta, RSCRTriggerKindId.EditionPinChange, RSCRTriggerKindId.PolicyPinChange}`
**Notes (wiring‑only):**
* Archive/illumination signals are telemetry; promotion into dominance is only via explicit `G.4` policy pins.

#### G.8:5.5 - `G.8:Ext.ExploreExploitTelemetry`

**PatternScopeId:** `G.8:Ext.ExploreExploitTelemetry`
**GPatternExtensionId:** `ExploreExploitTelemetry`
**GPatternExtensionKind:** `MethodSpecific`
**SemanticOwnerPatternId:** `C.19`
**Uses:** `{C.19}`
**⊑/⊑⁺:** `∅`
**RequiredPins/EditionPins/PolicyPins (minimum):**

* `ExploreExploitBudgetPolicyId?`
* `ProbeAccountingId?`

**RSCRTriggerKindIds:** `{RSCRTriggerKindId.TelemetryDelta, RSCRTriggerKindId.PolicyPinChange}`
**Notes (wiring‑only):**
* When “probe/sandbox” is used, the controlling policy ids are pinned and recorded in the ledger/bundle trace.

#### G.8:5.6 - `G.8:Ext.OpenEndedWiring`

**PatternScopeId:** `G.8:Ext.OpenEndedWiring`
**GPatternExtensionId:** `OpenEndedWiring`
**GPatternExtensionKind:** `GeneratorSpecific`
**SemanticOwnerPatternId:** `G.5` *(generator family registry surface; algorithm semantics remain external to Part‑G core)*
**Uses:** `{G.5}`
**⊑/⊑⁺:** `∅`
**RequiredPins/EditionPins/PolicyPins (minimum):**

* `GeneratorFamilyId`
* `TransferRulesRef.edition`
* `EnvironmentValidityRegionId?`
* `CouplerPolicyId?`

**RSCRTriggerKindIds:** `{RSCRTriggerKindId.EditionPinChange, RSCRTriggerKindId.PolicyPinChange, RSCRTriggerKindId.TelemetryDelta}`
**Notes (wiring‑only):**
* Open‑ended coverage/regret (or similar) remains telemetry unless explicitly promoted by an owner policy.

### G.8:6 - Archetypal Grounding (System / Episteme)

**Show‑A — Tri‑state admissibility with set‑valued selection (multi‑criteria).**
A CG‑Frame hosts multiple offline/robust decision families (e.g., conservative offline RL and transformer‑based policy models post‑2020). The bundle publishes `RuleId[]` (SoS‑LOG semantics in `C.23`), cites `AcceptanceClauseId[]` for any floors (owned by `G.4`), and emits an `AdmissibilityLedger` whose rows cite `PathSliceId` (when available) for each `pass/degrade/abstain`. `G.5` consumes the ledger and returns a **portfolio set** under the declared partial order—no scalar “winner”.
**Show‑A — Tri‑state admissibility with set‑valued selection (multi‑criteria).**
A CG‑Frame hosts multiple offline/robust decision families (e.g., conservative offline RL and transformer‑based policy models post‑2020). The bundle publishes `SoSLogRuleId[]` (SoS‑LOG semantics in `C.23`), cites `AcceptanceClauseId[]` for any floors (owned by `G.4`), and emits an `AdmissibilityLedger` whose rows cite `PathSliceId` (when available) for each `pass/degrade/abstain`. `G.5` consumes the ledger and returns a **portfolio set** under the declared partial order—no scalar “winner”.

**Show‑B — QD archive dispatch with edition‑pinned descriptors (post‑2015 QD families).**
A method family uses a modern QD line (e.g., CMA‑ES‑driven archives, differentiable QD variants, and large‑scale JAX‑style QD toolchains). The bundle pins `DescriptorMapRef.edition` and `DistanceDefRef.edition`, plus insertion/emitter policies. Illumination metrics are logged as telemetry; any promotion into dominance is only via explicit CAL policy pins (recorded in the admissibility trace).

**Show‑C — Open‑ended environment–method co‑evolution (post‑2018 open‑ended families).**
A generator family operates in an open‑ended setting (e.g., POET‑style and PAIRED‑style regimes). The bundle carries `TransferRulesRef.edition` and validity region pins; unknown transfer validity triggers a `degrade` branch rather than an ad‑hoc fourth status. Telemetry (coverage/regret proxies) is emitted for refresh planning, not silently turned into dominance.

### G.8:7 - Bias‑Annotation

Lenses tested: **Gov**, **Arch**, **Onto/Epist**, **Prag**, **Did**.
Scope: packaging kit only. Rule semantics remain owned by `C.23`; thresholds remain owned by `G.4`; evidence path semantics remain owned by `G.6`; selection semantics remain owned by `G.5`.

### G.8:8 - Conformance Checklist (CC‑G8)

* **CC‑G8‑CoreRef (G.Core conformance bridge).**
  A conforming `G.8` SHALL satisfy the **effective** set of `CC‑GCORE‑*` obligations implied by `G.8:4.1` (expanded per `G.Core:4.2`), including required pins, trigger sets, and default‑ownership routing.

* **CC‑G8‑1 (No thresholds in LOG).**
  Any numeric gate, maturity floor, or threshold SHALL be authored as a `G.4` Acceptance artefact and cited by id; the LOG bundle/ladder SHALL NOT embed thresholds.

* **CC‑G8‑2 (Tri‑state discipline; delegated).**
  Guard outcomes SHALL obey the tri‑state domain and unknown handling defined in `G.Core` (delegation to `CC‑GCORE‑GUARD‑1`).  
  Any sandbox/probe‑only behaviour SHALL be represented as an explicit `C.23` branch and MUST pin (and record) the controlling policy id (typically an E/E‑LOG policy id via `C.19`), rather than inventing a fourth status or silently coercing unknowns.

* **CC‑G8‑3 (Path citation when evidence is path‑addressable).**
  When `G.6` is in use (or resolvable), every recorded `pass/degrade/abstain` outcome in the `AdmissibilityLedger` MUST cite `PathId/PathSliceId` (run‑time). At packaging time, the bundle/ledger SHALL at minimum provide resolvable evidence refs (e.g., `EvidenceGraphId?` + anchor refs).

* **CC‑G8‑4 (Crossing visibility and penalty routing; delegated).**
  Any cross‑Context/plane reuse asserted by the bundle/ledger SHALL satisfy the core crossing visibility and penalty routing invariants (delegation to `CC‑GCORE‑CROSS‑1` and `CC‑GCORE‑PEN‑1`).

* **CC‑G8‑5 (Portfolio/dominance hygiene; delegated).**
  The bundle/ledger SHALL treat portfolio/dominance fields as pinned inputs and SHALL route any omitted defaults via the single‑owner Default Ownership Index (delegation to `CC‑GCORE‑DEF‑1` and `CC‑GCORE‑SET‑1`; owners include `CC‑G5.23` for `DefaultId.PortfolioMode` and `CC‑G5.28` for `DefaultId.DominanceRegime`). It MUST NOT restate default values locally.  
  If the bundle/ledger records telemetry that could influence dispatch (e.g., illumination/QD/OEE/open‑ended proxies), such telemetry SHALL remain report‑only unless explicitly promoted by a `G.4` owner policy id that is pinned and recorded in the run‑time trace.

* **CC‑G8‑6 (QD/OEE edition discipline).**
  When QD/OEE surfaces are declared, the bundle/ledger MUST pin the relevant editions and policies (`DescriptorMapRef.edition`, `DistanceDefRef.edition`, insertion/emitter policies, and `TransferRulesRef.edition` when applicable).  
  `CharacteristicSpaceRef.edition` is **required iff** cell boundaries / de‑dup rules / parity depend on the space definition, and MUST NOT be used as a substitute for `DescriptorMapRef.edition`.

* **CC‑G8‑7 (Maturity is ordinal/poset).**
  Maturity ladders SHALL be authored as ordinal/poset descriptions with **closed** rung ids (`MaturityRungs`, UTS‑registered) and a declared `ReferencePlane`, and SHALL be published as a citable UTS artefact (editioned; twin‑register safe).  
  Rung transitions, when asserted, MUST be justifiable by citable evidence paths (when available).

* **CC‑G8‑8 (Spaces ≠ Maps).**
  `CharacteristicSpace` and `DescriptorMap` SHALL remain strictly distinct kinds; naming and twin‑register discipline must be respected.

* **CC‑G8‑9 (Notational independence).**
  The bundle, ledger, and maturity card SHALL remain notation‑independent (per `E.5.2`); any serialization choice is non‑normative and belongs outside Part‑G core.

* **CC‑G8‑10 (MOO cross‑reference).**
  When a LOG bundle is used to drive or justify a produced portfolio outcome, the producing Work/Audit artefact SHOULD cite the controlling mechanism ids (e.g., parity/shipping/refresh artefact ids) and relevant policy pins; no “black box” provenance.

* **CC‑G8‑11 (SoTA‑of‑description trace).**
  If authoring methods (e.g., discovery, clustering, summarisation) materially shaped rule text or rung definitions, the bundle/card SHOULD cite their method description refs (edition‑pinned) to support cross‑stance traceability.

### G.8:9 - Common Anti‑Patterns and How to Avoid Them

* **Anti‑pattern:** Embedding thresholds inside SoS‑LOG rules or ladder rungs.
  **Avoid:** thresholds live in `G.4` Acceptance; bundle only cites clause ids.

* **Anti‑pattern:** Treating illumination/QD telemetry as a hidden scalar score that changes dominance.
  **Avoid:** keep telemetry report‑only unless explicitly promoted by an owner policy pin.

* **Anti‑pattern:** Publishing a bundle that “implies” cross‑context reuse without Bridge/CL/Φ pins.
  **Avoid:** if reuse is asserted, publish the crossing pins; otherwise downstream must abstain from reuse.

* **Anti‑pattern:** Re‑defining `PortfolioMode`/`DominanceRegime` defaults in the bundle text.
  **Avoid:** cite the single owners via `G.Core.DefaultOwnershipIndex`.

* **Anti‑pattern:** Recording RSCR “reasons” as prose labels only.
  **Avoid:** emit canonical `RSCRTriggerKindId` values per `G.Core`.

### G.8:10 - Consequences

* **Positive:** `G.5` receives a stable, citable, selector‑facing artefact without importing rule semantics or threshold logic.
* **Positive:** Audit and refresh become tractable: pins, crossings, evidence paths, and trigger kinds are explicit.
* **Positive:** Maturity remains non‑scalar, reducing illegitimate aggregation and “readiness theater”.
* **Negative:** Requires stricter authoring discipline (UTS publication, pin completeness, explicit wiring).
* **Negative:** If evidence paths are not maintained (`G.6` absent), auditability degrades and downstream must rely on weaker refs or abstain.

### G.8:11 - Rationale

`C.23` owns **rule semantics**, `G.4` owns **thresholding/acceptance**, `G.6` owns **path‑addressable provenance**, and `G.5` owns **selection/registry semantics**. Without a dedicated packaging kit, projects either (i) duplicate semantics inside ad‑hoc “decision bundles” (creating shadow specs), or (ii) leave dispatch un‑auditable. `G.8` keeps these boundaries strict while providing a single, consumable surface.

### G.8:12 - SoTA‑Echoing (informative; post‑2015 practice alignment)

This pattern’s separation of **decision rules**, **acceptance thresholds**, **provenance paths**, and **set‑valued outputs** echoes post‑2015 practice in:

* **Set‑valued / portfolio‑first selection** (multi‑objective and uncertainty‑aware regimes; avoiding forced scalar winners).
* **Quality‑Diversity and archive‑based evaluation** (post‑2015 QD variants emphasize edition‑pinned descriptors/distances and telemetry‑driven refresh).
* **Open‑endedness / curriculum generation** (post‑2018 lines emphasize explicit transfer rules, safe degrade branches, and telemetry‑driven orchestration rather than hidden gates).
* **Reproducibility‑aware publishing** (explicit identifiers, pinned editions/policies, citable traces rather than prose‑only decision rationales).

*(Examples are illustrative; they do not introduce new Part‑G‑wide norms.)*

### G.8:13 - Relations

**Builds on:** `G.Core`, `C.23`, `G.4`, `G.6`, `G.5`, `C.22`
**Uses:** `A.10` (anchors), `F.8` (policy-id resolvability), `F.9` + `G.7` (when cross‑Context/plane reuse is asserted), `G.11` (refresh planning/trigger consumption), `G.10` (shipping boundary; if bundled artefacts are shipped), `E.10` (LEX twin registers), `E.5.2` (notation independence), `E.18/A.21/A.27` (GateCrossing visibility); optional `C.18` (QD) / `C.19` (E/E‑LOG) when those surfaces are declared.
**Publishes to:** `UTS` (bundle/ledger/card), `G.5` (selector/registry consumption), `G.11` (refresh via typed triggers and pinned telemetry)
**Constrains:** any SoS‑LOG packaging that claims FPF conformance for selector‑facing dispatch across method families.

### G.8:14 - Author’s quick checklist (informative)

* [ ] `RuleId[]` are ids only; rule semantics are owned by `C.23` (no re-definition in this bundle).
* [ ] `SoSLogRuleId[]` are ids only; rule semantics are owned by `C.23` (no re-definition in this bundle).
* [ ] Any numeric gates/thresholds are `G.4` Acceptance artefacts cited by id (no thresholds embedded in LOG or rungs).
* [ ] Evidence is citable: at run time use `PathId/PathSliceId` when available; at packaging time provide resolvable `A10EvidenceGraphRef?[]` / `EvidenceGraphId?`.
* [ ] Any cross‑Context/plane reuse is explicit: `BridgeId/BridgeCardId`, `CL/CL^k/CL^plane`, and `Φ/Ψ/Φ_plane` policy ids are pinned (policy ids resolvable per `F.8:8.1`).
* [ ] Portfolio/dominance defaults are not restated: route via `G.Core.DefaultOwnershipIndex` (owners live outside `G.8`, typically `G.5`).
* [ ] QD pins are edition/policy pinned (`DescriptorMapRef.edition`, `DistanceDefRef.edition`, insertion/emitter policies); `CharacteristicSpaceRef.edition` is pinned iff cell boundaries/de‑dup/parity depend on it; **Spaces ≠ Maps**.
* [ ] If open‑ended surfaces are declared, pin `GeneratorFamilyId`, `TransferRulesRef.edition`, and any validity/coupler policy ids; unknown transfer validity routes to `degrade`/branching (no “fourth status”).
* [ ] `MaturityRungs` is a closed, UTS‑registered set; the maturity ladder is ordinal/poset with a declared `ReferencePlane`; rung transitions cite evidence.
* [ ] RSCR triggers are emitted as canonical `RSCRTriggerKindId` values (no prose-only “reasons”).
* [ ] Notation independence (`E.5.2`) and twin‑register discipline (`E.10`) are respected for all published heads/ids.
* [ ] If authoring tools materially shaped rule/rung content, cite `AuthoringMethodDescriptionRefs?[]` (edition‑pinned) for cross‑stance traceability.

### G.8:End

## G.9 — Parity / Benchmark Harness

**Tag:** Architectural pattern
**Stage:** design‑time planning **+** run‑time execution (selector‑adjacent)
**Primary hooks:** **G.Core** (core invariants & linkage catalogues), **G.5** (selector & portfolio semantics), **G.6** (EvidenceGraph, `PathId`/`PathSliceId`), **G.4** (Acceptance & CAL predicates), **G.0** (CG‑Spec legality surface), **A.19** (CN‑Spec contract surface), **C.22** (TaskSignature S2), **C.23** (SoS‑LOG branches & maturity; guard narration), **C.18/C.19** (QD & E/E‑LOG pins, when used), **G.7** (Bridge calibration / CL regimes; BCT/Sentinels), **F.15** (RSCR parity/regression harness), **F.9** (Bridges & CL), **G.11** (refresh orchestration), **G.10** (shipping), **E.18/A.21/A.27** (GateCrossing & CrossingSurface), **E.5.2** (notation‑independence), **E.10** (LEX discipline).

**Why this exists.** “Benchmarking” rival MethodFamilies/Traditions routinely fails for reasons that are *not* about compute: window mismatch, silent edition drift, unpinned comparator semantics, covert cross‑Context reuse, or “making a scalar winner” out of a partial order. **G.9** provides a **ParityPlan@Context** (WorkPlanning) and a **ParityReport@Context** (Work/Audit) that make parity runs **reproducible and audit‑addressable**, so that downstream selection (via **G.5**) can consume parity outcomes *without inventing new legality gates or “shadow” contract surfaces*.
Illumination/coverage/regret signals are treated as **telemetry (report‑only by default)**; any promotion of telemetry into dominance is an **explicit CAL policy** and MUST be recorded via a pinned **policy‑id** in audit pins (the harness does not “smuggle” objectives).

**Modularity note.** G.9 does **not** redefine CN‑Spec, CG‑Spec, CHR, Acceptance, or SoS‑LOG semantics. It only **pins and wires** the relevant refs/editions/policy‑ids, executes parity as a **selector‑adjacent** harness, and publishes an auditable trace (EvidenceGraph paths + pins).

### G.9:1 — Intent

Provide a **notation‑independent** harness that:

* plans parity runs with explicit scope (`describedEntity`, `ReferencePlane`, window), explicit contract surfaces (`CNSpecRef`, `CGSpecRef`, `ComparatorSpecRef`) and explicit reproducibility pins (editions + policy‑ids);
* executes parity in a way that is consumable by **G.5** (portfolio/set outcomes, DRR/SCR evidence trace);
* publishes **ParityReport@Context** suitable for downstream consumption, shipping, and refresh/RSCR wiring.

### G.9:2 — Problem frame

Parity claims become non‑reproducible or non‑comparable when any of the following are implicit:

* evidence window / freshness regime,
* comparator semantics (including any normalization / comparability mapping),
* method‑family “measurement” edition pins (incl. DHC method/spec),
* cross‑Context reuse (bridges / plane routing / CL penalties),
* dominance/portfolio interpretation rules,
* gate outcomes (why a run abstained or degraded).

G.9’s role is to force these to be **pinned and publishable** as a *method of obtaining outputs* (MOO) without introducing new contract surfaces.

### G.9:3 — Forces

* **Pluralism vs comparability.** Multiple Traditions must be comparable *without semantic collapse*.
* **Partial orders.** Many targets are only partially ordered; parity reporting must preserve lawful outcome shape (often portfolios/archives rather than a single scalar).
* **Edition sensitivity.** Parity must be robust to silent drift in measurement/comparator definitions. When DHC/QD/OEE modes are used, the required definition pins are introduced only via the corresponding `Extensions` blocks (nil‑elision when unused).
* **Telemetry vs objectives.** IlluminationSummary and coverage/regret are telemetry: **report‑only by default**; dominance changes require explicit CAL policy ids (recorded in audit pins).
* **GateCrossing visibility.** Any crossings/gates used by parity must be visible and auditable via CrossingSurface + GateCrossing checks; failures block parity publication/consumption.
* **Cross‑Context reuse.** Any reuse across contexts/planes must be explicit, auditable, and penalty‑routed.
* **Refreshability.** Parity must emit RSCR‑relevant causes as canonical ids, with enough pins to re‑run.

### G.9:4 — Solution

#### G.9:4.0 — G.Core linkage (normative)

This pattern is **core‑invariant‑bearing** and therefore binds to **G.Core** by declaration (not by restating invariants here).

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
  *(Owners are routed via `G.Core.DefaultOwnershipIndex` (not restated here); expected owners include `CC‑G5.28`, `CC‑G5.23`, `CC‑G5.4` respectively.)*

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

#### G.9:4.1 — Objects and surfaces

All objects below are **notation‑independent**; serialisations (if any) live under shipping/interop ownership, not here.

**(1) `ParityPlan@Context`** *(WorkPlanning surface)*
A plan that fixes *what is being compared* and *under what pinned conditions*.

Minimal fields (conceptual; ids/pins only):

`ParityPlan@Context := ⟨  
  ParityPlanId(UTS),  
  CGFrameId?,                              // or CG-FrameContext id/scope anchor used by the owner surfaces
  describedEntity := ⟨GroundingHolon, ReferencePlane⟩,
  UNM_id?, NormalizationMethodId[]?, NormalizationMethodInstanceId[]?, // when “normalize, then compare” is required (ids only; semantics owned by CN‑Spec / UNM)
  EpsilonDominance?,                       // optional ε-front thinning (ε≥0; id/param; pinned when used)
  PortfolioMode?, DominanceRegime?,         // may be explicit or routed via DefaultOwnership (semantics owned by G.5)
  HomeContextId,  
  BaselineSet,                            // method-family / generator-family baseline scope (ids; notation-independent)  
  BaselineBindingRef,                      // e.g., EvidenceGraph/PathSlice binding to “what counts as baseline”  
  FreshnessWindows,  
  CNSpecRef.edition, CGSpecRef.edition, ComparatorSpecRef.edition, // edition-pinned refs
  SCPRef.edition?,                         // optional (when a specific SCP profile must be pinned/cited)
  MinimalEvidenceRef.edition?,             // optional (when CG-Spec exposes minima profiles by ref)
  Budgeting?,  
  ParityPinSet,  
  PlanItemRefs[]?                          // references to A.15.3 SlotFillingsPlanItem (planned baseline), when parity depends on planned slot fillings  
⟩`

**(2) `ParityPinSet`** *(surface)*
A declared set of pins required for reproducibility and audit (editions + policy‑ids + UTS/Path pins).
The concrete contents are *pattern‑local* (G.9 owns the surface), but must satisfy the *core pin discipline* via G.Core.

**(3) `ParityReport@Context`** *(Work / Audit surface)*
A publication object produced by executing a ParityPlan.

`ParityReport@Context := ⟨  
  ParityReportId(UTS),  
  ParityPlanId,  
  BaselineSet, FreshnessWindows,  
  CNSpecRef.edition, CGSpecRef.edition, ComparatorSpecRef.edition,  
  SCPRef.edition?, MinimalEvidenceRef.edition?,             // echoed iff used/pinned in the plan
  UNM_id?, NormalizationMethodId[]?, NormalizationMethodInstanceId[]?, // echoed iff used in the plan
  OutcomeRefs,                              // portfolio / archive / set outcomes (as refs to selector outputs)  
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

1. **Fix the baseline set.** Choose the `BaselineSet` (MethodFamilies, and optionally GeneratorFamilies) to compare; where parity context matters, cite `SoS‑LOGBundleId?` / maturity‑rung ids by reference (thresholds remain in `G.4` Acceptance).
2. **Bind scope.** Fix `describedEntity := ⟨GroundingHolon, ReferencePlane⟩` and record it in the plan (no silent widening/narrowing).
3. **Define baseline binding.** Declare what counts as “baseline set” and how it is cited (e.g., `BaselineBindingRef` pointing to an EvidenceGraph slice or an upstream shipped artefact id).
4. **Equalise window (and budget, if pinned).** Declare a single `FreshnessWindows` and apply it across all baselines; if `Budgeting` is used/pinned, it MUST be shared/pinned across baselines as well.
5. **Pin contract surfaces.** `CNSpecRef`, `CGSpecRef`, and `ComparatorSpecRef` are referenced with explicit edition pins.
6. **Pin measurement/comparator definitions (conditional).** Where parity depends on mode‑specific artefacts (e.g., DHC/QD/OEE), pin the relevant definition ids/editions/policies. The minimum required pins are declared by the applicable `Extensions` blocks (e.g., `G.9:Ext.DHCParityPins`, `G.9:Ext.QDArchiveParity`, `G.9:Ext.OEEParity`) and the owner surfaces they cite.
7. **Bind comparator choice to CG‑Spec (legality).** Any numeric comparison/aggregation MUST be CSLC‑lawful and cite the corresponding CG‑Spec entry (via `ComparatorSpecRef`). If Characteristics differ by unit/scale/space, the plan MUST declare the ids used for “normalize, then compare” (`UNM_id?`, `NormalizationMethodId[]?`, `NormalizationMethodInstanceId[]?`) — ids only; semantics is owned elsewhere.
8. **Declare order & portfolio semantics.** Parity MUST preserve set‑return semantics; `PortfolioMode`/`DominanceRegime` are either explicitly pinned or routed via `G.Core.DefaultOwnershipIndex`. IlluminationSummary/coverage/regret remain telemetry unless a CAL policy explicitly promotes them (policy‑id pinned & recorded).
9. **Attach planned baselines (when applicable).** If parity depends on planned slot fillings, the plan cites the relevant `SlotFillingsPlanItem` refs (A.15.3) via `PlanItemRefs[]` rather than embedding a competing baseline object (nil‑elision when unused).
10. **Route crossings (when invoked).** Cross‑Context/plane/Kind reuse requires explicit Bridge/CL/Φ pins; penalties route to `R_eff` only (invariants routed via `G.Core`).

#### G.9:4.3 — Execution protocol (run‑time / selector‑adjacent)

Execution is **one run** under the pinned plan:

1. **Gate on legality & pins.** Validate pins and legality‑gate availability; run eligibility/acceptance checks under the plan’s `TaskSignature (S2)` and refuse/abstain on illegal ops (record trace; no “fourth status”).
2. **Invoke selection/dispatch.** Call **G.5** under the plan’s pinned refs and emit selector outputs in a form consistent with G.5’s portfolio semantics.
3. **Record comparability mapping (when used).** If `UNM_id?` / `NormalizationMethodId[]?` / `NormalizationMethodInstanceId[]?` were declared, **echo them** in `ParityReport@Context` (or in its explicit pins deltas) and record their ids (and any scoped notes required by the owner surface) in audit pins/SCR; cite the applicable `PathId`s.
4. **Publish trace.** Emit `ParityReport@Context` with EvidenceGraph citations and all active pins (editions/policy‑ids), so the run can be re‑checked and re‑run.
5. **Emit telemetry hooks (optional, report‑only).** When telemetry is produced, it is emitted as telemetry pins/events for refresh wiring (not as a silent change in dominance interpretation).

#### G.9:4.9 — Extensions (pattern‑scoped; non‑core)

The following blocks store **wiring only** (pins/refs/policy‑ids, relevant triggers, and `Uses`), while semantics is owned by the referenced patterns.

**GPatternExtension block: `G.9:Ext.CrossTraditionParity`**
**GPatternExtension: CrossTraditionParity**
* **PatternScopeId:** `G.9:Ext.CrossTraditionParity`
* **GPatternExtensionId:** `CrossTraditionParity`
* **GPatternExtensionKind:** `DisciplineSpecific`
* **SemanticOwnerPatternId:** `G.7`
* **Uses:** `{G.7, F.9, E.18, A.21}`
* **⊑/⊑⁺:** `∅`
* **RequiredPins/EditionPins/PolicyPins (minimum; conditional on use):**
  * `BridgeId/BridgeCardId[]`
  * `BridgeMatrixId?`
  * `CalibrationLedgerId?` / `BCT.id?`
  * `RegressionSetId?` / `SentinelId[]?` *(when sentinel wiring is used)*
  * `CL/CL^k/CL^plane`
  * `Φ(CL) policy-id`, `Φ_plane policy-id`, `Ψ(CL^k) policy-id?`
  * `CrossingSurfaceId?`
* **RSCRTriggerSetIds:** `{GCoreTriggerSetId.BridgeCalibrationKit}` *(preferred; expands in `G.Core`)*  
* **RSCRTriggerKindIds (delta, if any):** `∅`
* **Notes (wiring-only):** This block does not define CL/Φ/Ψ semantics; it only requires the pins needed to cite calibration artefacts and crossing visibility surfaces.

**GPatternExtension block: `G.9:Ext.SoSLogGuardNarration`**
**GPatternExtension: SoSLogGuardNarration**
* **PatternScopeId:** `G.9:Ext.SoSLogGuardNarration`
* **GPatternExtensionId:** `SoSLogGuardNarration`
* **GPatternExtensionKind:** `MethodSpecific`
* **SemanticOwnerPatternId:** `C.23`
* **Uses:** `{C.23, G.6, G.4}`
* **⊑/⊑⁺:** `∅`
* **RequiredPins/EditionPins/PolicyPins (minimum; conditional on use):**
  * `SoSLogRuleId[]` / `BranchId[]` *(ids as cited labels; semantics owned by C.23)*
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
* **SemanticOwnerPatternId:** `C.21`
* **Uses:** `{C.21}`
* **⊑/⊑⁺:** `∅`
* **RequiredPins/EditionPins/PolicyPins (minimum; conditional on use):**
  * `DHCMethodRef.edition`
  * `DHCMethodSpecRef.edition?` *(when the owner distinguishes method vs method‑spec editions)*
* **RSCRTriggerKindIds:** `{RSCRTriggerKindId.EditionPinChange, RSCRTriggerKindId.PolicyPinChange, RSCRTriggerKindId.EvidenceSurfaceEdit}`
* **Notes (wiring-only):** Declares the pins required to make DHC‑based parity reproducible and RSCR‑refreshable; semantics of DHC lives in `C.21`.

**GPatternExtension block: `G.9:Ext.QDArchiveParity`**
**GPatternExtension: QDArchiveParity**
* **PatternScopeId:** `G.9:Ext.QDArchiveParity`
* **GPatternExtensionId:** `QDArchiveParity`
* **GPatternExtensionKind:** `MethodSpecific`
* **SemanticOwnerPatternId:** `C.18`
* **Uses:** `{C.18, C.19, G.5}`
* **⊑/⊑⁺:** `∅`
* **RequiredPins/EditionPins/PolicyPins (minimum; conditional on use):**
  * `DescriptorMapRef.edition`
  * `DistanceDefRef.edition`
  * `CharacteristicSpaceRef.edition?` *(when discretisation/topology is referenced)*
  * `EmitterPolicyRef`
  * `InsertionPolicyRef`
* **RSCRTriggerKindIds:** `{RSCRTriggerKindId.EditionPinChange, RSCRTriggerKindId.PolicyPinChange, RSCRTriggerKindId.TelemetryDelta}`
* **Notes (wiring-only):** Post‑2015 QD families are referenced here only as wiring + edition/policy pin obligations (semantics owned by `C.18`/`C.19`/`G.5`).

**GPatternExtension block: `G.9:Ext.OEEParity`**
**GPatternExtension: OEEParity**
* **PatternScopeId:** `G.9:Ext.OEEParity`
* **GPatternExtensionId:** `OEEParity`
* **GPatternExtensionKind:** `MethodSpecific`
* **SemanticOwnerPatternId:** `C.19`
* **Uses:** `{C.19, G.5}`
* **⊑/⊑⁺:** `∅`
* **RequiredPins/EditionPins/PolicyPins (minimum; conditional on use):**
  * `TransferRulesRef.edition`
  * `EnvironmentValidityRegionId`
  * `ExplorationBudgetPolicyId?`
  * `EvidenceTrace.PathSliceId?` *(for transfer‑keyed events)*
* **RSCRTriggerKindIds:** `{RSCRTriggerKindId.EditionPinChange, RSCRTriggerKindId.PolicyPinChange, RSCRTriggerKindId.TelemetryDelta}`
* **Notes (wiring-only):** Open‑ended parity is expressed as policy/edition pins + telemetry wiring, not as new core norms.

**GPatternExtension block: `G.9:Ext.RobustEvaluationProtocols`** *(Phase‑3 seed)*
**PatternScopeId:** `G.9:Ext.RobustEvaluationProtocols`
**GPatternExtensionId:** `RobustEvaluationProtocols`
**GPatternExtensionKind:** `Phase3Seed`
**SemanticOwnerPatternId:** `owner TBD`
**Uses:** `{G.0, A.19}`
**⊑/⊑⁺:** `∅`
**RequiredPins/EditionPins/PolicyPins (minimum):**

* `ComparatorSpecRef.edition`
* `CNSpecRef.edition`
* `UncertaintyPolicyId?` / `CalibrationPolicyId?` *(ids only; semantics owner TBD)*
**RSCRTriggerKindIds:** `{RSCRTriggerKindId.PolicyPinChange, RSCRTriggerKindId.EditionPinChange}`
**Notes (seed; wiring-only):**
Intended docking point for post‑2015 robust evaluation idioms (e.g., set‑valued / conformal‑style reporting, distribution‑shift aware benchmarking) once an owner pattern is established.

### G.9:5 — Interfaces (minimal I/O; conceptual)

| Interface                          | Consumes                                                                                                                                         | Produces                                                                                        |
| ---------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------- |
| **G.9‑1 `Plan_Parity`**            | `BaselineSet`, `BaselineBindingRef`, `FreshnessWindows`, `Budgeting?`, `EpsilonDominance?`, `CNSpecRef.edition`, `CGSpecRef.edition`, `ComparatorSpecRef.edition`, `SCPRef.edition?`, `MinimalEvidenceRef.edition?`, `UNM_id?`, `NormalizationMethodId[]?`, `NormalizationMethodInstanceId[]?`, `ParityPinSet`, `PlanItemRefs[]?` | `ParityPlan@Context` (UTS entry; edition‑pinned)                                                |
| **G.9‑2 `Run_Parity`**             | `ParityPlan@Context`, `TaskSignatureRef` (S2), **G.5‑3 Select**                                                                                  | Selector outputs (portfolio/archives/sets as refs), DRR+SCR pins with `PathId[]`/`PathSliceId?` |
| **G.9‑3 `Publish_ParityReport`**   | Run artefacts + trace + active pins                                                                                                              | `ParityReport@Context` (UTS entry; audit‑addressable; emits canonical RSCR ids)                 |
| **G.9‑4 `Expose_ParityTelemetry`** | Telemetry deltas (archive changes, coverage/regret signals, etc.)                                                                                | Telemetry events carrying `PathSliceId?`, policy‑ids, and edition pins for refresh wiring       |

*Surfaces are conceptual; serialisations belong to shipping/interop ownership (see G.10 / interop annexes), not to G.9.*

### G.9:6 — Conformance Checklist (CC‑G9)

**CC‑G9‑CoreRef (normative; mandatory).**
G.9 conforms only if it satisfies the **effective** set of `CC‑GCORE‑*` declared in **G.9:4.0 GCoreLinkageManifest** (including trigger typing, default ownership routing, and P2W split).

1. **CC‑G9.1 — Equal windows (and budgets) & pinned contract editions (local).**
   A ParityPlan **SHALL** declare a single `FreshnessWindows` shared across baselines. If `Budgeting` is used/pinned, it **SHALL** be shared across baselines as well. `ParityPinSet` **SHALL** include the edition pins required by the referenced contract/comparator surfaces (at minimum `CNSpecRef.edition`, `CGSpecRef.edition`, `ComparatorSpecRef.edition`).
   If the parity run depends on planned slot fillings (WorkPlanning baseline), the plan **SHALL** cite the relevant `SlotFillingsPlanItem` refs via `PlanItemRefs[]` (nil‑elision when not applicable).

2. **CC‑G9.2 — Mode‑specific definition pins are declared via Extensions (local; conditional).**
   When parity depends on mode‑specific artefacts beyond the pinned contract surfaces (e.g., DHC/QD/OEE), the ParityPlan/Report **SHALL** include the corresponding `GPatternExtension` blocks and satisfy their `RequiredPins/EditionPins/PolicyPins` (typically carried inside `ParityPinSet`, and echoed via pins deltas in audit):
   * DHC parity → `G.9:Ext.DHCParityPins`
   * QD archive parity → `G.9:Ext.QDArchiveParity`
   * OEE parity → `G.9:Ext.OEEParity`

3. **CC‑G9.3 — Lawful orders & lawful arithmetic (delegation point + local constraint).**
   Delegated to `CC‑GCORE‑SET‑1` (and the relevant G.5 portfolio semantics). Additionally: any numeric comparison/aggregation invoked by parity **SHALL** be CSLC‑lawful and cite the corresponding CG‑Spec entry; illegal operations (e.g., ordinal means / mixed‑scale weighted sums) **SHALL** be refused or abstained with path‑cited trace (routing only; semantics owned by CG‑Spec/MM‑CHR).

4. **CC‑G9.4 — Normalization discipline (local, routing only).**
   If Characteristics differ by unit/scale/space, the ParityPlan **SHALL** cite the lawful comparability mapping by id (`UNM_id?`, `NormalizationMethodId[]?`, `NormalizationMethodInstanceId[]?`) and compare only after that mapping is applied (“normalize, then compare”).  
   If such mapping ids are used, the ParityReport **SHALL** echo the same ids (directly or via explicit pins deltas) so the run is reproducible/auditable without out‑of‑band context.  
   The harness **SHALL NOT** define a local mapping.

5. **CC‑G9.5 — Dominance/portfolio interpretation & telemetry separation (local).**
   ParityPlan/ParityReport **SHALL** either (i) explicitly pin the applicable regime/mode via refs/policy‑ids, or (ii) cite the owners of `DefaultId.DominanceRegime` and `DefaultId.PortfolioMode` via `G.Core.DefaultOwnershipIndex`. Any non‑default “promotion” behaviour must be policy‑bound and recorded via policy‑id pins.
   IlluminationSummary/coverage/regret **SHALL** be treated as telemetry (report‑only by default); any promotion into dominance is an explicitly pinned CAL policy and MUST be recorded in audit pins/SCR.

6. **CC‑G9.6 — Epsilon‑front thinning (local; conditional).**
   If ε‑front thinning is used, `EpsilonDominance (ε≥0)` **SHALL** be explicit in the plan/report and pinned (param/id) such that the same ε is reproducible.

7. **CC‑G9.7 — Crossing routing (delegation point).**
   Delegated to `CC‑GCORE‑CROSS‑1` and `CC‑GCORE‑PEN‑1`. This item remains as a stable delegation point for Bridge/plane routing visibility and penalty routing discipline.

8. **CC‑G9.8 — Evidence trace completeness (local).**
   A ParityReport **SHALL** include an EvidenceTrace with `EvidenceGraphId` and the relevant `PathId[]` (and `PathSliceId?` when needed), covering both inclusions and refusals/abstains/degrades.

9. **CC‑G9.9 — Telemetry hooks are emitted with pins (local).**
   When parity emits telemetry for refresh, emitted telemetry **SHALL** carry the active edition pins and policy‑ids needed to re‑run parity (including the active subset of `ParityPinSet` relevant to the emitted event).
   In particular, telemetry items SHOULD cite `PathSliceId` when available, and **SHALL** include the policy id governing the telemetry interpretation.
   Mode‑specific definition pins **SHALL** be included as declared by the active `Extensions` blocks (e.g., `G.9:Ext.QDArchiveParity`, `G.9:Ext.OEEParity`, including `EnvironmentValidityRegionId` when OEE parity is in scope).

10. **CC‑G9.10 — RSCR parity tests are published (local).**
   Parity publication **SHALL** include RSCR parity tests (via `F.15` harness refs) that cover negative/refusal paths relevant to this plan (missing pins, edition drift, missing bridge calibration refs, etc.).

11. **CC‑G9.11 — GateCrossing visibility (delegation point).**
    Delegated to `CC‑GCORE‑CROSS‑1` and the applicable GateCrossing/CrossingSurface harness checks (E.18/A.21/A.27). This remains a stable delegation point.

12. **CC‑G9.12 — Tech‑register lexical discipline (local).**
    Tech prose and heads **SHALL** follow E.10: do not introduce drift‑prone primitives (e.g., “metric” as a Tech primitive); reference the owner’s canonical terms and pinned refs.

13. **CC‑G9.13 — MOO disclosure for parity (local).**
    `Run_Parity` / `Publish_ParityReport` **SHALL** record the ParityHarness identity (UTS ids) and the active pins required to interpret the outcome (editions + policy‑ids), so parity remains auditable without relying on “decision logs”.

### G.9:7 — Anti‑patterns and remedies

* **AP‑1 Hidden edition drift.** Remedy: require edition pins in `ParityPinSet`; treat changes as RSCR‑relevant via canonical trigger kinds.
* **AP‑2 Baseline set is informal prose.** Remedy: require `BaselineBindingRef` and EvidenceTrace pins.
* **AP‑3 Comparator semantics are “whatever the code did”.** Remedy: `ComparatorSpecRef.edition` (and any normalization/comparability refs) must be cited and pinned.
* **AP‑4 Cross‑Context reuse without visible routing.** Remedy: cite bridge/plane routing artefacts and crossing visibility surfaces (delegated to G.Core).
* **AP‑5 Parity report becomes a hidden scoring sheet.** Remedy: preserve lawful outcome shape and keep telemetry as telemetry unless explicitly policy‑promoted by owner patterns.
* **AP‑6 “Metric” as a primitive in Tech.** Remedy: use `DHCMethodRef`/`U.Measure`/`DistanceDefRef` with editions; “metric” may appear only in Plain with an explicit pointer to canonical terms.
* **AP‑7 Hidden spec drift (spec‑level pins missing).** Remedy: pin `DHCMethodSpecRef.edition` and register RSCR tests that fail on spec edition changes; refuse parity reuse on unpinned spec editions.

### G.9:8 — Archetypal grounding (informative; SoTA‑oriented)

**Show‑A — Multi‑tradition parity for decision systems (post‑2015 practice).**
ParityPlan pins a rolling evidence window and comparator refs; ParityReport publishes a set/portfolio outcome plus the evidence trace. Typical “rival families” include modern preference‑learning comparators, causal decision pipelines, offline‑RL evaluation pipelines, and robust BO‑style selectors—compared without collapsing everything into a single scalar.

**Show‑B — QD parity (MAP‑Elites lineage → CMA‑ME / DQD / QDax‑class).**
ParityPlan pins descriptor/distance definitions and archive insertion policy editions. ParityReport includes archive outcomes and telemetry deltas needed for refresh, without silently converting illumination summaries into dominance.

**Show‑C — Open‑ended parity (POET lineage and modern open‑ended generator families).**
ParityPlan pins transfer rule editions and exploration policy refs. ParityReport publishes portfolio outcomes plus transfer‑keyed traces (PathSlice), enabling refresh reruns when any pinned policy changes.

### G.9:9 — Payload (what this pattern exports)

**Exports (UTS‑publishable, edition‑pinned):**

* `ParityPlan@Context` (WorkPlanning artefact)
* `ParityReport@Context` (Work/Audit artefact)
* DRR+SCR refs (by id) and (when applicable) `PortfolioPackRef?`/selector output refs (by id), for downstream consumption.
* Telemetry pins/events (by id), for refresh wiring (`G.11`) and RSCR harnesses (`F.15`).

### G.9:10 — Relations

**Builds on:** `G.Core`, `G.5`, `G.6`, `G.4`, `F.15`, `E.18`, `A.21`, `A.27`, `E.5.2`, `E.10`.
**Publishes to:** **UTS** (plan/report ids), **G.11** (refresh wiring), **G.10** (shipping surface; parity artefacts are cited payloads).
**Uses:** **G.0**, **A.19**, **F.9**.
**Uses (optional, via Extensions):** **G.7**, **C.18/C.19** (QD/OEE wiring), **C.23** (SoS‑LOG narration and failure‑policy pins).

### G.9:11 — Author’s quick checklist (non‑normative)

1. Bind `describedEntity` + `ReferencePlane`; define a baseline binding ref (don’t leave it as prose).
2. Pin `CNSpecRef.edition`, `CGSpecRef.edition`, `ComparatorSpecRef.edition`.
3. Declare `FreshnessWindows` and enforce it across baselines (and budgets, if pinned).
4. Declare `ParityPinSet` (editions + policy‑ids + evidence pins) and attach `PlanItemRefs[]` when planned baseline matters.
5. Run once; publish `ParityReport@Context` with EvidenceTrace and active pins; emit telemetry pins for refresh as needed.

### G.9:End

## G.10 - SoTA Pack Shipping

**Tag:** Architectural pattern (conceptual; notation‑independent; pack‑boundary owner)
**Stage:** release‑time composition and publication; edition‑aware; **GateCrossing‑gated** via `E.18` CrossingSurface (and the relevant GateCrossing harness patterns).
**Builds on:** `G.Core` (Part‑G core invariants and routing); upstream pack/kit owners as cited artefacts (not redefined here).
**Owns (scope boundary):** *shipping* of Part‑G outputs as a **pack** (`SoTA‑Pack(Core)`), including the pack‑level publication kit: (i) selector‑facing portfolio/parity surface, (ii) PathId/PathSlice citation surface, (iii) telemetry pins for refresh planning, and (iv) optional interop ingestion as citation‑only notes.
**Does not own:** contract surfaces (`CN‑Spec`, `CG‑Spec`), CHR/CAL semantics, selection semantics, evidence semantics, bridge calibration semantics, refresh orchestration (these remain with their owners and are **cited**).

### G.10:1 - Problem frame — Shipping without smuggling semantics

Part G produces many **kit‑owned** and **suite‑owned** artefacts (harvest packs, CHR/CAL packs, evidence graphs, bridge calibration artefacts, log bundles, parity reports). Without an explicit **pack‑boundary owner**, “shipping” tends to become:

* an ad‑hoc folder/export ritual (tool‑locked, not citable), or
* a silent re‑specification layer (shipping accidentally redefines legality, defaults, or selection semantics), or
* a brittle hand‑off that cannot support RSCR/refresh (no actionable pins/editions/policies attached).

`G.10` fixes the pack boundary: it defines the **single, normative shipping surface** for Part‑G outputs — **`SoTA‑Pack(Core)`** — and a minimal choreography for making shipped artefacts **selector‑ready** and **audit‑citable**, while delegating all Part‑G‑wide invariants to `G.Core` (routing/delegation, not restatement).

### G.10:2 - Problem — Why naive shipping breaks reuse, legality, and refresh

Naive shipping fails (conceptually) when any of the following occurs:

1. **Format-as-contract.** A concrete export format is treated as “the pack,” turning a tool choice into a semantic authority.
2. **Editionless hand‑offs.** Shipped artefacts omit the edition/policy pins required to replay or compare outcomes, so parity and RSCR become non‑actionable.
3. **Pack smuggles semantics.** Shipping reintroduces “convenience” rules (hidden scalarisation, competing defaults, private gate decisions), fragmenting the contract surface.
4. **Invisible crossings.** Cross‑context/plane reuse is present, but the pack does not expose the crossing surfaces and penalty policy pins needed for audit and refresh planning.
5. **No method‑of‑obtaining‑output disclosure.** Consumers receive outcomes without a minimal, citable trail of *which mechanisms/policies/editions produced them*.
6. **Refresh orphaning.** Telemetry and decay signals exist, but the shipped artefact provides no stable scope keys (`PathId` / `PathSliceId`) and no payload pins for RSCR triggers.

### G.10:3 - Forces

| Force                                              | Tension                                                                                          |
| -------------------------------------------------- | ------------------------------------------------------------------------------------------------ |
| **Notation independence**                          | Make packs portable across tools ↔ still make them concrete enough to be used.                   |
| **Completeness vs minimality**                     | Ship enough to be selector‑ready ↔ avoid duplicating owner semantics.                            |
| **Continuity vs evolvability**                     | Preserve public IDs across edition bumps ↔ allow legitimate upgrades and deprecations.           |
| **Cross‑context reuse vs honesty**                 | Enable reuse across Traditions/contexts ↔ keep crossings explicit and auditable.                 |
| **Telemetry usefulness vs semantic contamination** | Export useful signals ↔ avoid turning telemetry into dominance/acceptance without pinned policy. |
| **Fast shipping vs refreshability**                | Ship quickly ↔ ensure RSCR triggers can be planned and scoped (P2W‑path aware).                  |

### G.10:4 - Solution — `SoTA‑Pack(Core)` as the shipping object and publication kit

`G.10` defines a **pack‑owned** shipping surface: a notation‑independent object that **cites** all upstream artefacts by stable ids/refs and exposes the minimum pins required to (a) consume the result via selection, (b) audit it via path citations and crossing surfaces, and (c) refresh it via typed RSCR triggers.

#### G.10:4.1 - G.Core linkage (normative)

**Builds on:** `G.Core` (Part‑G core invariants; single‑owner routing)

**GCoreLinkageManifest (G.10)** *(normative; expands per `G.Core:4.2`; `Nil‑elision` applies)*
Effective obligations/pins/triggers are computed as **union(expand(sets), explicit deltas)** under `Nil‑elision`.

* `CoreConformanceProfileIds` := {
  `GCoreConformanceProfileId.PartG.AuthoringBase`,
  `GCoreConformanceProfileId.PartG.TriStateGuard`,
  `GCoreConformanceProfileId.PartG.UTSWhenPublicIdsMinted`,
  `GCoreConformanceProfileId.PartG.ShippingBoundary`
  }

* `RSCRTriggerSetIds` := { `GCoreTriggerSetId.RefreshOrchestration` }
  *(payload pins: `PackId(UTS)`, `publicationScopeId`, `CNSpecRef.edition`, `CGSpecRef.edition`, `PlanItemRefs := SlotFillingsPlanItemRef[]`, `AuditPins`, `UTSRowId[]`, `PathId/PathSliceId`, crossing policy pins, `TelemetryPinIds`, relevant upstream artefact ids)*

* `DefaultsConsumed` := {
  `DefaultId.PortfolioMode`,
  `DefaultId.DominanceRegime`,
  `DefaultId.GammaFoldForR_eff`
  }
  *(Owners are routed via `G.Core.DefaultOwnershipIndex` and are not restated here.)*

* `CorePinSetIds` := {
  `GCorePinSetId.PartG.AuthoringMinimal`,
  `GCorePinSetId.PartG.CrossingVisibilityPins`
  }

* `CorePinsRequired` *(pattern delta; pin names only; id‑valued unless noted)* := {
  `PackId(UTS)`,
  `publicationScopeId`,
  `contextSliceId?`,

  `PlanItemRefs := SlotFillingsPlanItemRef[]?` *(WorkPlanning planned baseline refs)*,
  `AuditPins` *(pack‑level pin bundle: edition pins (only on `…Ref.edition`), policy‑ids, UTS/Path pins; ids only)*,

  `UTSRowId[]`,
  `PathId[]?`, `PathSliceId[]?`,
  `CrossingSurfaceIds := CrossingSurfaceId[]?`,
  `TelemetryPinIds := TelemetryPinId[]?`,
  `PortfolioSurfaceId?`,

  `MOOManifestId?` *(method‑of‑obtaining‑output disclosure; conceptual object id)*
  }
  *(Optional pins from `CrossingVisibilityPins` MAY be strengthened to unconditional by listing them above; `G.10` typically strengthens `UTSRowId[]` and path/crossing surfaces when the pack is publicly shipped.)*

* `TriggerAliasMapRef` := `∅` *(no local trigger tokens in Phase‑2)*

> **Mode‑specific definition pins.** Any additional pins required for QD/OEE/interop shipping are introduced only by `GPatternExtension` blocks in `G.10:4.6` (never smuggled into the core linkage).

#### G.10:4.2 - `SoTA‑Pack(Core)` object model (normative; notation‑independent)

`SoTA‑Pack(Core)` is a **shipment object** (a *pack*, not a kit and not a suite) that **cites** upstream artefacts and exposes pack‑level pins required for downstream use.

```
SoTA‑Pack(Core) :=
⟨
  PackId(UTS),
  publicationScopeId,
  contextSliceId?,
  CG-FrameContext,
  describedEntity := ⟨GroundingHolon, ReferencePlane⟩,

  // Contract surfaces (refs + edition pins; semantics owned by their patterns)
  CNSpecRef := ⟨A.19 ref, CNSpecRef.edition⟩,
  CGSpecRef := ⟨G.0 ref,  CGSpecRef.edition⟩,

  // Selector-facing portfolio/parity surface (conceptual; no formats mandated)
  PortfolioSurfaceId?,        // produced by `G.10‑1` as part of composition; may cite ε and the applicable pinned regime/mode refs

  // Cited payload packs/kits (ids only; semantics owned by the cited owners)
  SoTAHarvestPackId?          // e.g., G.2 output id
  CHRPackId?                  // G.3 output id
  CALPackId?                  // G.4 output id
  EvidenceGraphId?            // G.6 output id
  BridgeMatrixId?             // G.2/G.7 cited id
  BridgeCalibrationTableId?   // G.7 output id
  SoSLOGBundleId?             // G.8 output id
  ParityReportId?             // G.9 output id
  DashboardSliceId?           // G.12 output id (optional)
  InteropSurfaceId?           // G.13 output id (optional)

  // Path citation surface (ids only; semantics owned by A.10/G.6)
  PathIds := PathId[]?,
  PathSliceIds := PathSliceId[]?,

  // Planned baseline + audit pins (P2W-aware; ids only)
  PlanItemRefs := SlotFillingsPlanItemRef[]?,
  AuditPins := { id pins… },                 // editions only on `…Ref.edition`; includes policies, UTS/Path pins, crossing pins

  // Crossing visibility surface (per GateCrossing; ids only)
  CrossingSurfaceIds := CrossingSurfaceId[]?,

  // Telemetry hooks for refresh planning (ids only; PathSlice-keyed; policy-id pinned)
  TelemetryPinIds := TelemetryPinId[]?,

  // Method-of-obtaining-output (MOO) disclosure (conceptual; ids only)
  MOOManifestId?,

  Notes?
⟩

#### G.10:4.2.1 - Portfolio surface (normative; pack‑owned; owner‑delegating)

`PortfolioSurfaceId` identifies the **selector‑facing** pack surface. It is **wiring + citation** only:
it MUST NOT redefine selection/portfolio semantics (owned by `G.5`) or parity semantics (owned by `G.9`).
Mode‑specific definition pins (QD/OEE/interop) are introduced only via `G.10:Ext.*` blocks.

```
PortfolioSurface@Context :=
⟨
  PortfolioSurfaceId,
  PackId(UTS),
  CG-FrameContext,
  describedEntity,

  // Portfolio semantics (values may be explicit or resolved via DefaultOwnershipIndex)
  portfolioMode?,
  dominanceRegime?,
  ε?,

  // Selector-facing roster + provenance hooks (ids only)
  MethodFamilyIds := MethodFamilyId[]?,
  GeneratorFamilyIds := GeneratorFamilyId[]?,
  ParityReportId?,
  SCRId[]?, DRRId[]?,

  // Pin reuse: prefer referencing the enclosing pack’s AuditPins bundle
  AuditPins?,
  Notes?
⟩
```

*Presence rule:* `PortfolioSurfaceId` MAY be omitted only when the shipped pack is *inputs‑only*
(e.g., shipping CHR/CAL/evidence without any selector‑consumable portfolio/shortlist output).
```

**Interpretation constraints (normative by delegation).** Any universal invariants governing (i) contract‑surface ownership, (ii) crossing visibility and penalty routing, (iii) tri‑state guards, (iv) set‑return semantics, (v) P2W split, (vi) defaults, and (vii) RSCR trigger typing are **not restated here** and are enforced via `G.Core` routing (see `CC‑G10‑CoreRef`).

#### G.10:4.3 - Shipping choreography (normative; owner‑delegating)

`G.10` prescribes a minimal, owner‑delegating sequence for composing a shipped pack:

1. **S‑1 — Gather & pin.** Collect upstream artefact ids and verify the **required pins** implied by the linkage manifest (edition pins, policy pins, UTS/Path pins).
2. **S‑2 — Compose `SoTA‑Pack(Core)` + MOO disclosure.** Assemble the pack object and attach a **`MOOManifest`** that lists the referenced mechanisms/policies/editions that produced the shipped outcomes (ids only; semantics stay with owners).
3. **S‑3 — Publish portfolio/parity surface (selector‑facing).** Produce a selector‑readable `PortfolioSurfaceId` with the parity/definition pins required for reproducibility; do not mandate formats.
4. **S‑4 — Anchor and publish path citations.** Ensure A.10 anchors exist and publish/record `PathId/PathSliceId` citations required for downstream explainability (e.g., `C.23/H4`) and maturity rung changes.
5. **S‑5 — Expose CrossingSurface.** For each GateCrossing relevant to the shipped artefacts, expose the required `CrossingSurface` references (fail fast on missing or non‑conformant surfaces when required).
6. **S‑6 — Emit telemetry pins for refresh planning.** Whenever illumination increases or archive/OEE wiring changes, emit PathSlice‑keyed telemetry with policy‑id and the active `…Ref.edition` pins (and QD `EmitterPolicyRef`/`InsertionPolicyRef` when applicable).
7. **S‑7 — Publish to UTS (twin labels).** Mint/refresh UTS Name Cards needed to cite the pack and shipped heads (Tech/Plain twins when required); cross‑Context identity travels only via Bridges with CL and loss notes.
8. **S‑8 — Optional: ingest interop surface.** If `G.13` interop is in use, ingest/cite `InteropSurface@Context` as annotation-only notes, pinning external index editions; do not redefine interop semantics.

#### G.10:4.4 - Interfaces & hooks (selector‑ and audit‑facing)

| ID         | Interface (conceptual)     | Consumes                                                          | Produces                                                |
| ---------- | -------------------------- | ----------------------------------------------------------------- | ------------------------------------------------------- |
| **G.10‑1** | `Compose_SoTA_Pack`        | G.* outputs, ComparatorSet, Bridges, editions, SCR/DRR deltas     | `SoTA‑Pack(Core)` (UTS row + surfaces) + `AuditPins` (+ `MOOManifestId?`) (+ `PortfolioSurfaceId?`) |
| **G.10‑2** | `Publish_UTS`              | `PackId(UTS)`, `UTSRowId[]`, deprecation/edition‑bump notes       | UTS rows/Name Cards for the pack and shipped heads (incl. twins when required) |
| **G.10‑3** | `Expose_CrossingHooks`     | GateCrossings, lanes/planes/contexts                              | **CrossingSurface** (**E.18:CrossingSurface**) per GateCrossing; **fail** on missing/non‑conformant surfaces |
| **G.10‑4** | `Pack_MOO`                 | referenced mechanism/policy/edition ids                           | `MOOManifestId` (ids only; owner‑delegating) |
| **G.10‑5** | `Emit_TelemetryPins`       | Illumination/archive/OEE events                                   | PathSlice‑keyed telemetry: `policy‑id`, `…Ref.edition` (+ QD/OEE pins when applicable) |
| **G.10‑6** | `Publish_PathCitations`    | A.10 anchors, PathIds                                             | PathId/PathSlice citations for `C.23/H4` & rung changes |
| **G.10‑7** | `Ingest_InteropSurface?`   | (optional) `G.13 InteropSurface@Context`                          | Annotated pack notes citing external‑index editions     |

*Surfaces remain **conceptual** per **E.5.2**; RO‑Crate/ORKG/OpenAlex mappings belong to **Annex/Interop** and do not affect Core conformance.*

> **Note.** Any concrete serialisation/export is *not* part of this interface set. Serialisation belongs to interop/annex ownership and must not become a semantic authority.

#### G.10:4.5 - Consequence of ownership (normative boundary statement)

`G.10` is the **single owner** of “shipping” in Part G *(by delegation to `CC‑GCORE‑SKP‑1`)*.
Other `G.x` patterns may produce artefacts that are shipped, but they must not embed shipping obligations; they cite `G.10` shipping surfaces instead.

#### G.10:4.6 - Extensions (pattern‑scoped; non‑core)

All method‑/generator‑/interop‑specific shipping wiring lives here as `GPatternExtension` blocks.

##### GPatternExtension — `G.10:Ext.QDArchiveShippingPins`

**PatternScopeId:** `G.10:Ext.QDArchiveShippingPins`
**GPatternExtensionId:** `QDArchiveShippingPins`
**GPatternExtensionKind:** `MethodSpecific`
**SemanticOwnerPatternId:** `C.18` *(QD/NQD semantics live with the owner; this block is wiring-only.)*
**Uses:** `{C.18, G.5, G.8, G.11}`
**⊑/⊑⁺:** `∅`
**RequiredPins/EditionPins/PolicyPins (minimum):**

* `DescriptorMapRef.edition`
* `DistanceDefRef.edition`
* `DHCMethodRef.edition?`
* `DHCMethodSpecRef.edition?`
* `EmitterPolicyRef` *(policy‑id / ref)*
* `InsertionPolicyRef` *(policy‑id / ref)*
* `CharacteristicSpaceRef` *(id/ref; iff archive partitioning is declared)*
* `CharacteristicSpaceRef.edition?` *(iff partitioning depends on an editioned space definition)*
* `PathSliceId[]` *(to bind telemetry/refresh scope when archive behaviour is present)*

**RSCRTriggerSetIds:** `∅` *(covered by `G.10` core linkage via `GCoreTriggerSetId.RefreshOrchestration`)*
**Notes (wiring only):**
* This block never redefines archive semantics; it only states which pins must be present in the shipped pack when QD archive fields are present.

##### GPatternExtension — `G.10:Ext.OEEShippingPins`

**PatternScopeId:** `G.10:Ext.OEEShippingPins`
**GPatternExtensionId:** `OEEShippingPins`
**GPatternExtensionKind:** `GeneratorSpecific`
**SemanticOwnerPatternId:** `G.5` *(generator family registry / transfer wiring is owned upstream; this block is pack‑wiring only.)*
**Uses:** `{G.5, G.11}`
**⊑/⊑⁺:** `∅`
**RequiredPins/EditionPins/PolicyPins (minimum):**

* `TransferRulesRef.edition`
* `EnvironmentValidityRegion?` *(id/ref; iff an explicit region is declared as part of generator family wiring)*
* `PathSliceId[]` *(scope key for refreshable generator telemetry when present)*

**RSCRTriggerSetIds:** `∅` *(covered by the core trigger set)*
**Notes (wiring only):**
* “Open‑endedness” semantics remain owner‑defined; the pack only carries the pins required to make the shipped claim replayable/auditable.

##### GPatternExtension — `G.10:Ext.InteropCitation`

**PatternScopeId:** `G.10:Ext.InteropCitation`
**GPatternExtensionId:** `InteropCitation`
**GPatternExtensionKind:** `InteropSpecific`
**SemanticOwnerPatternId:** `G.13` *(interop semantics live with `G.13`; this block only cites ids/pins.)*
**Uses:** `{G.13}`
**⊑/⊑⁺:** `∅`
**RequiredPins/EditionPins/PolicyPins (minimum):**

* `InteropSurfaceId`
* `ExternalIndexRef.edition`
* `ClaimMapperRef.edition`
* `PlaneMapRef.edition?`
* `MappingPolicyRef`

**RSCRTriggerSetIds:** `∅` *(covered by the core trigger set)*
**Notes (wiring only):**
* This block only records that an interop surface contributed to the shipped pack’s provenance; it does not redefine any crosswalk semantics.

### G.10:5 - Consequences

**Benefits**

* A shipped result becomes **selector‑ready** and **audit‑citable** without turning file formats into a contract.
* Shipping is no longer a semantic “backdoor”: pack‑level semantics remain owner‑delegated.
* RSCR/refresh becomes operationally viable because pack‑level scope keys and payload pins are present.

**Costs / trade‑offs**

* Shipping becomes more explicit (more pins and explicit surfaces), which raises authoring overhead.
* If upstream owners fail to provide citable ids/pins, `G.10` cannot paper over the gap; shipping will block or ship a visibly incomplete pack (depending on policy‑bound failure behaviour, routed via owners).

### G.10:6 - Bias‑Annotation (informative)

Lenses tested: **Gov**, **Arch**, **Onto/Epist**, **Prag**, **Did**.

* **Format bias (Arch/Prag).** Strong temptation to treat a popular export format as “the pack”.  
  *Mitigation:* keep Core surfaces conceptual (E.5.2); move serialisation recipes to Annex/Interop; keep conformance on semantics.
* **Centralisation bias (Gov).** A single shipping owner can become a bottleneck.  
  *Mitigation:* keep shipping ownered, but push mode/method specifics into explicit `G.10:Ext.*` wiring blocks and cite semantic owners.
* **Telemetry→dominance bias (Onto/Prag).** Shipping pipelines often “promote” telemetry proxies (illumination/coverage) into ranking.  
  *Mitigation:* preserve the telemetry/order separation and require explicit CAL policy‑id for any promotion; record the policy‑id in audit pins/telemetry.
* **Interop authority bias (Onto/Epist).** External indexes can silently override local legality/typing.  
  *Mitigation:* `G.10‑6` ingests interop only as cited notes (editions + mapping policy refs), never as a replacement contract surface.

### G.10:7 - Archetypal grounding (informative; post‑2015 method families)

**World‑plane (benchmark shipping).**
A CG‑Frame ships a portfolio that includes a QD archive (e.g., MAP‑Elites‑class / CMA‑ME‑class families) and a generator family (e.g., POET‑class environment generation). The shipped `SoTA‑Pack(Core)` cites the CHR/CAL packs and pins the QD/OEE wiring via the extension blocks so that downstream parity and refresh can be scoped to the affected `PathSliceId`s rather than forcing a global rebuild.

**Episteme‑plane (synthesis shipping).**
A CG‑Frame ships a pluralistic set of admissible methods gathered from post‑2015 literature streams (living review + synthesis pack). The shipped pack carries explicit contract‑surface refs, evidence path citations, and method‑of‑obtaining‑output disclosure; downstream selection uses set‑valued outcomes and can schedule refresh when the synthesis pack or key pins change.

### G.10:8 - Conformance checklist (CC‑G10)

This pattern inherits order/illumination, evidence, and bridge/penalty legality from the cited owners (not restated here). Shipping‑specific requirements:

| ID  | Statement   | Verification notes (conceptual)  |
| --- | ----------- | -------------------------------- |
| **CC‑G10‑CoreRef** | The pattern satisfies the **effective** `G.Core` obligations declared by `G.10:4.1` (after profile/set/pin‑set expansion under `Nil‑elision`). | Check that the linkage manifest is present and that the expanded obligations are not contradicted. |
| **CC‑G10.1 (Notation‑independent).** | The pack MUST NOT rely on any specific file syntax; cards/tables are conceptual; tool serialisations are informative only. | Look for format‑free conceptual fields; any serialisation is explicitly non‑normative. |
| **CC‑G10.2 (Pack parity pins).** | If QD/OEE fields are present, pin `DescriptorMapRef.edition`, `DistanceDefRef.edition`, (optional) `DHCMethodRef.edition` / `DHCMethodSpecRef.edition` when used, and (OEE) `TransferRulesRef.edition`; include `CharacteristicSpaceRef` (+ `CharacteristicSpaceRef.edition` when it affects partitioning reproducibility); for QD archive semantics also pin `EmitterPolicyRef` and `InsertionPolicyRef`. | Verify the corresponding `G.10:Ext.*` block is present and the pins appear in AuditPins and (when relevant) in telemetry pins. |
| **CC‑G10.3 (Telemetry discipline).** | Any illumination increase or archive edit SHALL log `PathSliceId`, the active `policy‑id`, the active editions of the pinned `…Ref` fields (incl. OEE `TransferRulesRef.edition`), and the active `EmitterPolicyRef`/`InsertionPolicyRef` when applicable. | Verify emitted telemetry is PathSlice‑keyed and carries the required pins; ensure causes are recorded using canonical trigger kinds (alias labels optional only). |
| **CC‑G10.4 (UTS publication & twins).** | All shipped heads appear on UTS with Tech/Plain twins **per delegated UTS discipline**; cross‑Context identity (when present) is routed via Bridges with CL and loss notes **per delegated crossing discipline**. | Verify UTS rows exist and that any cross‑Context identity is routed via Bridge artefacts with visible CL/loss notes. |
| **CC‑G10.5 (MOO surfaced in shipping).** | For every portfolio set or archive published, the pack SHALL list the applicable generation/parity mechanism ids (e.g., QD `EmitterPolicyRef`/`InsertionPolicyRef`, parity harness ids, method refs where the method definition is generative) and the active policy‑id(s) in SCR‑visible bindings and telemetry pins (ids only; owner‑delegating). | Verify `MOOManifestId` is present when outcomes are intended for downstream use and does not redefine semantics. |
| **CC‑G10.6 (Pack completeness as a citation surface).** | The pack cites all included upstream artefacts by id/ref and exposes the required pins (`AuditPins`, UTS/Path pins, CrossingSurfaceIds when required). | Verify all present payload artefacts have ids and the pins needed to cite/replay them. |
| **CC‑G10.7 (CrossingSurface exposure).** | For each GateCrossing relevant to shipped artefacts, the pack exposes the relevant `CrossingSurfaceIds` (or records that no such crossings exist) **per delegated crossing visibility discipline**, and shipping fails fast on missing/non‑conformant crossing surfaces when required. | Verify crossing surface presence/absence is honest and aligned with the shipped artefacts’ declared crossings. |
| **CC‑G10.8 (Baseline binding is explicit when used).** | If the shipped pack claims a planned baseline, `PlanItemRefs := SlotFillingsPlanItemRef[]` are present (WorkPlanning artefacts, cited; no execution logs). | Verify plan items are cited by id and the pack does not ship “decisions/logs” as authoritative artefacts. |
| **CC‑G10.9 (Extension‑scoped wiring).** | If QD/OEE/interop fields are present, the corresponding `GPatternExtension` block is present and its required pins/editions/policies are recorded in AuditPins and in emitted telemetry pins when those pins affect refreshability. | Verify conditional wiring is not silently omitted when the mode is used. |

### G.10:8.1 - Anti‑patterns and remedies

* **AP‑1 Format‑as‑contract.** Remedy: keep Core surfaces conceptual (E.5.2); move serialisation to Annex/Interop; enforce `CC‑G10.1`.
* **AP‑2 Hidden edition drift.** Remedy: require `…Ref.edition` pins in AuditPins and treat edition changes as RSCR‑relevant via canonical trigger kinds.
* **AP‑3 “QD archive present” but missing definition pins.** Remedy: enforce `CC‑G10.2` and the `G.10:Ext.QDArchiveShippingPins` wiring.
* **AP‑4 Telemetry silently becomes dominance.** Remedy: keep telemetry report‑only unless an explicit CAL policy promotes it; require policy‑id recorded (ties to `CC‑G10.3` and MOO discipline).
* **AP‑5 No PathSlice key → refresh becomes global.** Remedy: enforce PathSlice‑keyed telemetry and path citations (`G.10‑4`, `G.10‑5`).
* **AP‑6 Cross‑Context reuse without visible routing.** Remedy: require `CrossingSurfaceIds` + Bridge/CL policy pins; fail fast on missing/non‑conformant surfaces (`CC‑G10.7`).
* **AP‑7 Interop ingestion rewrites semantics.** Remedy: ingest interop as cited notes only; semantics remain in `G.13` (`G.10‑6`, `G.10:Ext.InteropCitation`).

### G.10:8.2 - SoTA‑Echoing (post‑2015, for orientation)

* **Research‑object packaging & provenance.** Post‑2015 practice increasingly treats “release artefacts” as *packages with explicit provenance, versions, and minimal replay pins* (e.g., modern research‑object and RO‑Crate‑class approaches). `G.10` mirrors the “package‑as‑citation‑surface” idea while keeping semantics owner‑delegated.
* **Reproducibility regimes in ML/AI.** Contemporary reproducibility checklists, artifact evaluation/badging, and benchmark reporting norms motivate: explicit version pins, explicit method disclosure, and separating telemetry summaries from decision criteria unless policy‑promoted.
* **Scholarly KG interoperability.** ORKG/OpenAlex‑class ecosystems highlight the need to treat external mappings as *interop notes with editions*, not as replacement contract surfaces — matching the `G.10‑6` and `G.10:Ext.InteropCitation` stance.

### G.10:9 - Relations

**Builds on:** `G.Core`; consumes/cites owner artefacts from `G.2` (harvest pack), `G.3` (CHR pack), `G.4` (CAL pack), `G.6` (EvidenceGraph), `G.7` (bridge calibration), `G.8` (SoS‑LOG bundle), `G.9` (parity report), optional `G.12` (dashboard slice), optional `G.13` (interop surface).
**Publishes to / used by:** UTS (pack identity), selector‑facing consumers (via `G.5`), audit/assurance surfaces (SCR/RSCR), refresh orchestration (`G.11`).
**Constrains:** tooling exports are downstream; serialisation and repository integration are explicitly non‑normative here.

### G.10:End

## G.11 - Telemetry-Driven Refresh & Decay Orchestrator

**Tag.** Architectural pattern (architectural; notation-independent)
**Status.** Stable
**Normativity.** Normative (unless explicitly marked informative)

**Stage.** run-time + maintenance-time (selective re-computation, republication, and controlled deprecation)

**Primary outputs (kit surfaces).** `RefreshQueue`, `RefreshPlan@Context` (WorkPlanning artefact), `RefreshReport@Context` (Work/Audit artefact), `DeprecationNotice@Context`, `EditionBumpLog@Context`.

**Primary hooks.** `G.Core` (RSCR trigger catalogue + alias docking + default ownership index), `G.6` (EvidenceGraph; `PathId`/`PathSliceId`), `G.7` (Bridge Sentinels; CL/Φ/plane policy pins), `G.5` (set-returning selection/dispatch), `G.8` (SoS-LOGBundle telemetry hooks), `G.9` (parity reruns), `G.10` (shipping hooks and pack-level telemetry pins), `G.12` (dashboard telemetry pins), `B.3.4` (freshness/decay), `E.18` (GateCrossing/CrossingSurface visibility), optional `C.18/C.19` (QD/E–E policy pins), `C.23` (SoS-LOG branches / maturity ladders).

**Non-duplication note (Phase-2).**
This pattern **does not** (i) define the meaning of RSCR trigger kinds, (ii) introduce “shadow specs” for CN/CG legality, (iii) redefine tri-state guards / penalties / set-return semantics, (iv) re-own shipping or harvesting, or (v) mint new `RSCRTriggerKindId` / default owners (design-time changes live in `G.Core` and are recorded via DRR, `E.9`).
All such universal norms are **cited via `G.Core`** and enforced through **delegation** in this pattern’s conformance checklist.

### G.11:1 - Problem frame — Keeping shipped SoTA current without global rebuilds

Part G produces shipped, selector-ready artefacts (packs, bundles, evidence graphs, parity reports, dashboards). Once shipped, they are exposed to:

* **telemetry** (illumination/archive changes, parity outcomes, dashboard deltas),
* **decay** (freshness windows expire; epistemic debt grows),
* **edition drift** (descriptor/distance/transfer rules bump; policy pins evolve),
* **bridge evolution** (CL/plane penalties or calibrations update).

Without an explicit orchestration surface, refresh becomes either:

* a brittle set of ad-hoc “full rerun” rituals, or
* an audit-only posture that silently accumulates drift.

`G.11` is the **Part G owner** of the **refresh orchestration kit**: it turns typed refresh causes into **scoped plans** and **auditable execution reports**, while delegating all cause semantics and universal invariants to `G.Core`.

### G.11:2 - Problem — Why naive refresh breaks comparability and legality

A refresh loop fails (conceptually) when any of the following happens:

1. **Full-rerun mania.** Minor edits (e.g., a single Bridge calibration) trigger pack-wide rebuilds without a traceable scope rationale.
2. **Editionless telemetry.** Telemetry signals are recorded without edition pins, making reruns non-comparable and parity-unreplayable.
3. **Alias-as-semantics.** Legacy trigger labels (e.g., `T0…T7`) are treated as if they define meaning, fragmenting refresh semantics across patterns.
4. **Silent crossings.** Refresh actions implicitly change crossing assumptions (UTS/Path/policy pins) without a visible CrossingSurface.
5. **Orchestration smuggles semantics.** Refresh introduces new default behaviors (dominance/portfolio/Γ-fold) or coerces partial orders into scalars “for convenience.”

### G.11:3 - Forces — Minimal recomputation under strict invariants

* **Minimal scope vs. completeness.** Refresh must be *as local as possible* (slice-scoped), but still include a defensible dependency closure over evidence and crossings.
* **Operational urgency vs. auditability.** Refresh is triggered by run-time telemetry and decay, yet must remain auditable as Work (pins, refs, paths), not as opaque “decisions.”
* **Legacy stability vs. semantic unification.** Existing trigger labels must remain usable, but their meaning must be single-owner and id-based.
* **Modularity vs. orchestration power.** `G.11` must coordinate harvesting/parity/shipping without re-implementing them or importing discipline-specific method semantics into core.
* **Policy-bound behavior vs. “smart defaults.”** Ordering of refresh, priority heuristics, and budget handling are valuable—but must live as policy-bound extensions, not as hidden universal rules.

### G.11:4 - Solution — RSCR-driven refresh as a P2W-scoped orchestration surface

#### G.11:4.1 - G.Core linkage (normative)

**GCoreLinkageManifest (normative; canonical shape per `G.Core`; Nil‑elision permitted).**

`GCoreLinkageManifest := ⟨
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

    RefreshPlanId,
    RefreshReportId,
    DeprecationNoticeId?,
    EditionBumpLogId?,

    SlotFillingsPlanItemRef[]?
  },

  DefaultsConsumed := ∅,
  TriggerAliasMapRef := G.Core.TriggerAliasMap.G11
⟩`

By the `G.Core` **Expansion rule**, the **effective** conformance ids / trigger‑kinds / pin‑obligations for `G.11` are the manifest expansions (profiles/sets/pin‑sets) plus the explicit deltas above.

**LegacyTriggerAliasIds (visible; labels only).** `{G.11:T0…T7}` (docked via `TriggerAliasMapRef`; aliases are never semantic authorities).

#### G.11:4.2 - Refresh orchestration kit (pattern-owned; conceptual surfaces)

`G.11` defines a minimal kit of *authoring-plane* artefacts that make refresh explicit and auditable.

1. **`RefreshQueue` (conceptual surface).**
   A queue of refresh candidates keyed by scope (`PathSliceId` preferred; `PatternScopeId` permitted).
   Ordering, prioritization, and batching are policy-bound (and therefore extension-scoped), but every queue item carries canonical trigger kind ids.

2. **`RefreshPlan@Context` (WorkPlanning artefact).**
   A planned refresh is a WorkPlanning object that **does not execute Work** and **does not embed gate decisions**. It declares:

* `RefreshPlanId` (UTS-published id; editioned)
* `describedEntity` and `ReferencePlane` pins (by ref; no implicit widening)
* `TargetScope := PathSliceId[] | PatternScopeId[]`
* `PlannedTriggers := RSCRTrigger[]` (canonical trigger kind ids + scope + payload pins)
* `PlannedActions := RefreshAction[]` (each action delegates to an owner pattern)
* `RequiredPins := {EditionPins, PolicyPins, UTS/Path pins}` for replayability
* `PlanItemRefs := SlotFillingsPlanItemRef[]` (when planning baselines or reruns requires explicit planned slot fillings)

3. **`RefreshReport@Context` (Work/Audit artefact).**
   An execution report (Work or Audit artefact) that records:

* `RefreshReportId` (UTS-published id; editioned)
* `ExecutedActions[]` with links to invoked owner artefacts (e.g., new parity report id, new pack id)
* `ObservedDeltas` (telemetry deltas, legality changes, evidence-path changes) as refs/pins—not as untyped prose
* `RSCRRefs[]` (any RSCR / regression harness artefacts invoked)
* `EmittedNotices[] := DeprecationNoticeId[]` and `EditionBumpLogId[]`
* the canonical trigger kinds actually applied (not only aliases)

4. **`DeprecationNotice@Context` and `EditionBumpLog@Context`.**
   Controlled evolution artefacts that preserve ID-continuity:

* **DeprecationNotice** explains scope, reason class (canonical trigger kind ids), and successor refs.
* **EditionBumpLog** records edition increments and the pins that justify them.

> *Note (normative by delegation).* ID continuity and alias discipline are governed by `G.Core` (do not restate as local rules here).

#### G.11:4.3 - Orchestration semantics (conceptual; delegating to owners)

`G.11` turns typed causes into scoped actions without owning the semantics of those actions.

**4.3.1 Ingestion.**
Consume RSCR triggers from:

* telemetry hooks (e.g., `G.8`, `G.10`, `G.12`),
* freshness/decay events (`B.3.4`),
* evidence/bridge/policy/edition edits (from the respective owners’ publication surfaces).

Every ingested signal is normalized into an `RSCRTrigger` (canonical id, scope, payload pins), with optional alias labels.

**4.3.2 Scope closure (EvidenceGraph-first).**
Compute the minimal dependency closure over:

* cited evidence paths (`G.6` `PathId/PathSliceId`),
* declared crossings (`G.7` sentinels; `CrossingSurface` visibility),
* and pinned contract surfaces (editions/policies).

The closure is a *planning-time claim* (“these slices are affected”), not a Work-time output.

**4.3.3 Planning (P2W seam).**
Produce `RefreshPlan@Context` that schedules actions of the form:

* `RerunHarvest` (delegates to `G.2`/`G.1`/owner; if used)
* `RerunParity` (delegates to `G.9`)
* `RecomputeSelectionOrPortfolio` (delegates to `G.5`)
* `RebindBridgeOrCrossing` (delegates to `G.7` and visibility harnesses)
* `UpdateEvidenceBindings` (delegates to `G.6`)
* `ReshipPack` (delegates to `G.10`)
* `UpdateBundle` (delegates to `G.8`)
* `UpdateDashboardSlice` (delegates to `G.12`)
* `EmitDeprecationNotice` / `EmitEditionBumpLog` (pattern-owned publication surfaces)

**4.3.4 Execution + audit.**
Execute planned actions as Work (or Work-bound audit) and publish `RefreshReport@Context`.
Gating outcomes (admit / degrade / abstain) follow `G.Core` tri-state semantics and are recorded via policy ids and cited evidence paths, rather than as local bespoke statuses.

#### G.11:4.4 - Extensions (pattern-scoped; non-core)

All discipline-specific refresh strategies, scheduling heuristics, and generator-specific wiring live as `GPatternExtension` blocks.

##### G.11:Ext.LegacyTriggers

**PatternScopeId:** `G.11:Ext.LegacyTriggers`
**GPatternExtensionId:** `LegacyTriggers`
**GPatternExtensionKind:** `InteropSpecific` (back-compat / alias docking)
**SemanticOwnerPatternId:** `G.Core`
**Uses:** `{G.Core}` (cites `G.Core.TriggerAliasMap.G11`)
**⊑/⊑⁺:** `∅`
**RequiredPins / EditionPins / PolicyPins (minimum):**

* `RSCRTriggerKindId[]` (canonical ids recorded on triggers)
* `RSCRTriggerAliasId?` (e.g., `G.11:T0…T7` as labels only)
* `scope: PathSliceId[] | PatternScopeId`

**RSCRTriggerKindIds:** `{RSCRTriggerKindId.EditionPinChange, RSCRTriggerKindId.PolicyPinChange, RSCRTriggerKindId.TelemetryDelta, RSCRTriggerKindId.FreshnessOrDecayEvent, RSCRTriggerKindId.CrossingSurfaceEdit, RSCRTriggerKindId.PenaltyPolicyEdit, RSCRTriggerKindId.MaturityRungChange, RSCRTriggerKindId.EvidenceSurfaceEdit}`
**Notes (wiring-only):** This block **does not define** what `T0…T7` mean; it only preserves the labels and requires docking via `G.Core.TriggerAliasMap.G11`.

##### G.11:Ext.DecayAndDebt

**PatternScopeId:** `G.11:Ext.DecayAndDebt`
**GPatternExtensionId:** `DecayAndDebt`
**GPatternExtensionKind:** `DisciplineSpecific`
**SemanticOwnerPatternId:** `B.3.4` (freshness/decay semantics)
**Uses:** `{B.3.4, G.6}`
**⊑/⊑⁺:** `∅`
**RequiredPins / EditionPins / PolicyPins (minimum):**

* `FreshnessWindowDeclRef` (or equivalent window pin, as defined by the owner)
* `DecayPolicyIdRef` / `EpistemicDebtBudgetRef` (policy-bound)
* `PathSliceId[]` (affected evidence carriers)

**RSCRTriggerKindIds:** `{RSCRTriggerKindId.FreshnessOrDecayEvent, RSCRTriggerKindId.EvidenceSurfaceEdit, RSCRTriggerKindId.BaselineBindingEdit}`
**Notes (wiring-only):** Any budget/priority logic remains policy-bound; `G.11` only wires decay events to refresh planning.

##### G.11:Ext.QDRefreshWiring

**PatternScopeId:** `G.11:Ext.QDRefreshWiring`
**GPatternExtensionId:** `QDRefreshWiring`
**GPatternExtensionKind:** `MethodSpecific`
**SemanticOwnerPatternId:** `C.18` (QD semantics; descriptor/distance/insertion)
**Uses:** `{C.18, C.19, G.5, G.8}`
**⊑/⊑⁺:** `∅`
**RequiredPins / EditionPins / PolicyPins (minimum):**

* `DescriptorMapRef.edition`, `DistanceDefRef.edition`
* `CharacteristicSpaceRef.edition?` (required when a domain-family coordinate is declared by the QD owner)
* `InsertionPolicyRef`, `EmitterPolicyRef` (policy-bound)
* `PathSliceId` (archive/illumination scope) + `policy-id` for emitted telemetry triggers

**RSCRTriggerKindIds:** `{RSCRTriggerKindId.TelemetryDelta, RSCRTriggerKindId.EditionPinChange, RSCRTriggerKindId.PolicyPinChange}`
**Notes (wiring-only):** `G.11` does not restate QD semantics; it ensures pins are present so reruns are comparable.

##### G.11:Ext.OEERefreshWiring

**PatternScopeId:** `G.11:Ext.OEERefreshWiring`
**GPatternExtensionId:** `OEERefreshWiring`
**GPatternExtensionKind:** `MethodSpecific`
**SemanticOwnerPatternId:** `C.19` (open-ended exploration / E–E logistics)
**Uses:** `{C.19, G.5, G.8, G.9}`
**⊑/⊑⁺:** `∅`
**RequiredPins / EditionPins / PolicyPins (minimum):**

* `TransferRulesRef.edition`, `EnvironmentValidityRegion` (when OEE is declared by the owner patterns)
* `GeneratorFamilyId` / `TransferRulesRef` wiring pins (as published by the owners)
* telemetry scope pins (`PathSliceId`, `policy-id`)

**RSCRTriggerKindIds:** `{RSCRTriggerKindId.EditionPinChange, RSCRTriggerKindId.TelemetryDelta, RSCRTriggerKindId.PolicyPinChange}`
**Notes (wiring-only):** Any OEE method semantics live with the owner; this module only wires refresh triggers to comparable reruns.

##### G.11:Ext.SchedulingHeuristics (Phase-3 seed)

**PatternScopeId:** `G.11:Ext.SchedulingHeuristics`
**GPatternExtensionId:** `SchedulingHeuristics`
**GPatternExtensionKind:** `Phase3Seed`
**SemanticOwnerPatternId:** `owner TBD`
**Uses:** `{G.11}`
**⊑/⊑⁺:** `∅`
**RequiredPins / EditionPins / PolicyPins (minimum):**

* `RefreshPriorityPolicyIdRef` (policy-bound)
* `BudgetDeclRef` (time/compute/cost/risk ceilings; policy-bound)

**RSCRTriggerKindIds:** `{RSCRTriggerKindId.TelemetryDelta, RSCRTriggerKindId.FreshnessOrDecayEvent, RSCRTriggerKindId.MaturityRungChange}`
**Notes (seed, non-normative):** Scheduling strategies (bandit-style, queueing, cadence policies) are valuable but must not become Part‑G‑wide norms.

### G.11:5 - Archetypal Grounding — System / Episteme (informative; Tell–Show–Show)

**`U.System` illustration — Safety-critical maintenance loop (pump + calibration).**
A centrifugal pump is serviced under a documented procedure (method description). Sensors report vibration drift (telemetry), and a calibration standard is updated (edition bump). `G.11` does not “rebuild the whole maintenance doctrine”: it emits a refresh plan scoped to the affected inspection slices (paths) and publishes a refresh report with pins to the updated standard edition and the evidence paths. Deprecation notices are issued for obsolete thresholds in the procedure’s acceptance clauses (by owner pattern), preserving ID continuity.

**`U.Episteme` illustration — Living review / benchmark pack (claims + parity).**
A claim sheet behind a shipped SoTA pack changes (new evidence, retraction, or revised measurement definition). Bridges are recalibrated, affecting CL/plane penalties. `G.11` ingests canonical trigger kinds, computes the minimal closure over affected `PathSliceId`s, schedules targeted parity reruns, then re-ships the pack through the shipping owner—while publishing an edition bump log that makes the evolution replayable.

### G.11:6 - Bias-Annotation (informative)

Lenses tested: **Gov**, **Arch**, **Onto/Epist**, **Prag**, **Did**.

* **Arch bias (toward explicit wiring).** Risk: authors feel “over-pinned.” Mitigation: keep the minimum pin set small; push scheduling sophistication into extensions/policies.
* **Gov bias (toward audit over speed).** Risk: refresh becomes bureaucratic. Mitigation: the kit is intentionally thin (queue/plan/report), while action semantics remain delegated to owners.
* **Onto/Epist bias (toward single-owner semantics).** Risk: teams try to localize trigger meaning for convenience. Mitigation: alias docking is allowed, but semantics stay in `G.Core`.
* **Prag bias (toward minimal recomputation).** Risk: under-refresh if closure is too narrow. Mitigation: require closure rationale and allow explicit “scope wideners” as policy-bound pins.
* **Did bias (toward readable, reusable artefacts).** Risk: oversimplified examples. Mitigation: maintain System+Episteme grounding and keep SoTA-echoing explicit.

### G.11:7 - Conformance Checklist (normative)

| ID                                                    | Requirement                                                                                                                                                                                                                                                                                                                                     | Purpose / Notes                                                                                                            |
| ----------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- |
| **CC‑G11‑CoreRef**                                    | A conforming `G.11` artefact **MUST** satisfy the **effective** core conformance set implied by the `GCoreLinkageManifest` in `G.11:4.1` (profile expansion + explicit deltas; delegated to `G.Core`).                                                                                                                                       | Phase‑2 bridge clause: `G.11` is conformant only if the relevant `G.Core` invariants and trigger discipline are satisfied. |
| **CC‑G11.1 (Slice-scoped planning).**                 | A conforming `RefreshPlan@Context` **SHALL** be scoped to `PathSliceId[]` (preferred) or `PatternScopeId[]` and **SHALL** record canonical `RSCRTriggerKindId` for each planned cause. Pack-wide reruns **MAY** occur only if the declared dependency closure spans all slices; the closure rationale **SHALL** be recorded.                    | Prevents full-rerun mania while keeping a safety escape hatch explicit and auditable.                                      |
| **CC‑G11.2 (Edition discipline; QD/OEE wiring).**     | When QD and/or OEE are active, a conforming `RefreshPlan@Context` and `RefreshReport@Context` **SHALL** satisfy the required pin/edition/policy wiring of the applicable extension blocks (`G.11:Ext.QDRefreshWiring` and/or `G.11:Ext.OEERefreshWiring`). **`.edition` SHALL apply only on `…Ref`.** Missing required pins **SHALL** block publication. | Keeps replayability strict while moving method‑specific pin lists into `Extensions` (Phase‑2 modularity).                  |
| **CC‑G11.3 (Telemetry‑metric legality).**             | If a refresh publishes Illumination/QD/OEE outcomes, it **SHALL** publish **Q/D/QD‑score** (and any coverage/regret) as **telemetry metrics** and **IlluminationSummary** as a **telemetry summary**; these values **SHALL be excluded from dominance** unless a CAL policy explicitly promotes them, and the promoting **policy‑id SHALL be recorded** in SCR‑visible evidence bindings (via the cited owners).                                                                                                      | Prevents covert scalarisation and keeps “telemetry vs order” separation explicit.                                          |
| **CC‑G11.4 (Bridge penalties).**                      | Any refresh reacting to Bridge/plane changes **SHALL** satisfy `CC‑GCORE‑PEN‑1` (delegation), and **SHALL** publish `CL/CL^k/CL^plane` and the relevant `Φ/Ψ/Φ_plane` policy‑ids with loss notes so penalties route to `R_eff` only (F/G invariant).                                                                                                                                | Keeps penalty routing auditable during refresh.                                                                            |
| **CC‑G11.5 (Selector invariants).**                   | Any orchestrated re‑selection or portfolio update **SHALL** (i) satisfy `CC‑GCORE‑SET‑1` (delegation), and (ii) call the selector owner (`G.5`) under an unchanged lawful `ComparatorSet` (edition‑pinned where applicable), returning **sets** (Pareto/Archive) and introducing **no scalarisation** inside `G.11`.                                                                                                                       | Prevents refresh from changing order semantics.                                                                            |
| **CC‑G11.6 (Crossing visibility).**                   | All refresh actions that touch cross‑context reuse **SHALL** satisfy `CC‑GCORE‑CROSS‑1` (delegation) and the GateCrossing visibility harness (e.g., `E.18`): `CrossingRef` + BridgeCard + UTS + `CL/Φ_plane` policy‑ids. Missing/non‑conformant crossings **SHALL** block publication.                                                                                                                                 | Prevents “silent crossings” under refresh.                                                                                 |
| **CC‑G11.7 (Decay governance).**                      | When refresh is triggered by freshness/decay events, the refresh outputs **SHALL** choose and record a governance outcome (**Refresh / Deprecate / Waive**) with **budget notes** (policy‑bound), and **SHALL** publish the decision via `DeprecationNotice@Context` (and related pins) and SCR‑visible evidence bindings (via `G.6` / cited owners).                                                                                                                                                | Turns epistemic debt into explicit, comparable governance artefacts.                                                       |
| **CC‑G11.8 (No default smuggling).**                  | A conforming `G.11` refresh artefact **SHALL NOT** introduce new defaults for portfolio/dominance/Γ‑fold/guard behavior. If orchestrated steps rely on defaults, the artefact **SHALL** cite the single owner (via `G.Core.DefaultOwnership` and the invoked owner patterns) rather than restating defaults inside `G.11`.                                                                                                                                            | Protects single‑owner default discipline under orchestration pressure.                                                     |
| **CC‑G11.9 (Targeted RSCR before republication).**    | Before any refresh result is republished downstream (e.g., parity report updates, pack re‑shipping, dashboard slice updates), the execution **SHALL** run or cite a targeted RSCR/regression check for the affected scope and record `RSCRRefs[]` (or equivalent) in `RefreshReport@Context`; exceptions **SHALL** be expressed as `degrade/abstain` outcomes (policy‑bound) rather than silent skips.                                                                                         | Preserves “refresh ≠ vibes” by making regression gating explicit and slice‑scoped.                                         |

### G.11:8 - Common Anti-Patterns and How to Avoid Them (informative)

| Anti-pattern                       | Symptom                                                           | Why it fails                                             | Repair                                                                            |
| ---------------------------------- | ----------------------------------------------------------------- | -------------------------------------------------------- | --------------------------------------------------------------------------------- |
| **Full-rerun mania**               | Any edit triggers a global rebuild                                | Costs explode; drift hides (no scope rationale)          | Enforce slice-scoped plans (CC‑G11.1); require closure rationale for global scope |
| **Editionless telemetry**          | Telemetry lacks `…Ref.edition`                                    | Reruns are non-comparable; parity breaks                 | Block publication on missing pins (CC‑G11.2)                                      |
| **Alias-as-semantics**             | `T*` labels are treated as meaning                                | Trigger meaning fragments; regressions become untestable | Dock aliases via `G.Core.TriggerAliasMap.G11`; record canonical ids               |
| **Silent crossing during refresh** | Refresh changes context/plane assumptions without crossings       | Violates crossing visibility; penalties become hidden    | Require crossing pins + E.18 visibility; block publication (CC‑G11.6)             |
| **Default smuggling**              | Refresh introduces “helpful” default dominance/portfolio behavior | Competing defaults appear; downstream arguments drift    | Cite owners via `G.Core.DefaultOwnership` (CC‑G11.8)                              |
| **Debt-by-prose**                  | “We decided not to refresh” exists only in narrative              | Not comparable; cannot be tested                         | Emit a DeprecationNotice (incl. a Waive outcome, if used) with pins (CC‑G11.7)    |

### G.11:9 - Consequences (informative)

* **Selective, replayable upkeep.** Refresh becomes a controlled planning/execution loop rather than an implicit “maintenance vibe.”
* **Stable semantics with flexible operations.** Trigger meaning is centralized (`G.Core`), while scheduling sophistication can evolve as policy-bound extensions.
* **Clear ownership boundaries.** Orchestration coordinates owners; it does not redefine their semantics (shipping remains `G.10`, selection remains `G.5`, etc.).
* **Cost: pin discipline overhead.** Authors must carry enough ids/editions/policies to make refresh comparable. This is intentional: it replaces hidden drift with explicit wiring.

### G.11:10 - Rationale (informative)

`G.11` is intentionally a **thin orchestration owner**:

* The refresh loop is powerful enough to coordinate reruns and republishing, but **too thin to become a second spec**. That is why trigger semantics, invariants, and defaults are delegated to `G.Core`.
* The kit is split across the **P2W seam** so that planning artefacts remain planning artefacts and executed work remains auditably executed work.
* Legacy stability is maintained by allowing trigger aliases (`T0…T7`) while prohibiting them from becoming semantic authorities.

### G.11:11 - SoTA-Echoing — Post‑2015 practices aligned (informative)

Each entry follows: **claim → practice → source → alignment → adoption status**.

1. **Continuous refresh is necessary in deployed evaluation pipelines.**
   Practice: production ML systems use monitoring + retraining / reevaluation triggers and insist on reproducibility hooks.
   Source: Breck et al., *The ML Test Score* (2017); Amershi et al., *Software Engineering for Machine Learning* (2019).
   Alignment: `G.11` formalizes triggers as typed causes and forces edition/policy pins for replay.
   Adoption: **Adopt/Adapt** (adapted to id-based, PathSlice-scoped refresh rather than “retrain everything”).

2. **Non-stationarity requires explicit drift/decay handling, not ad-hoc updates.**
   Practice: continual learning emphasizes non-stationarity as a first-class maintenance condition.
   Source: Parisi et al., *Continual Lifelong Learning with Neural Networks* (2019); De Lange et al., *A Continual Learning Survey* (2021).
   Alignment: `B.3.4` supplies decay semantics; `G.11` wires decay events into refresh planning and controlled deprecation.
   Adoption: **Adapt** (refresh of conceptual artefacts and evidence closures, not untracked model mutation).

3. **Quality-Diversity requires archive semantics and comparability under descriptor/distance evolution.**
   Practice: QD methods treat the archive as the primary result and track changes under policy/edition conditions.
   Source: contemporary QD families such as CMA‑ME (post‑2018) and differentiable QD lines (post‑2019).
   Alignment: QD-specific meaning lives with the owner patterns; `G.11:Ext.QDRefreshWiring` ensures edition pins and scope pins exist so targeted archive refresh is lawful.
   Adoption: **Adopt** (set/archive preservation; no covert scalarization).

4. **Open-endedness co-evolves environments and agents; transfer rules must be versioned.**
   Practice: POET-class open-ended systems require explicit transfer rules and environment validity constraints.
   Source: Wang et al., POET (2019) and subsequent POET extensions (2020+).
   Alignment: `G.11:Ext.OEERefreshWiring` requires `TransferRulesRef.edition` and scope pins so refresh reruns remain comparable and auditable.
   Adoption: **Adopt/Adapt** (adapted to Part‑G pin/UTS publication discipline).

5. **Efficient orchestration benefits from bandit/early-stopping scheduling—but it must not become semantics.**
   Practice: modern hyperparameter/experiment scheduling uses bandit-style resource allocation and asynchronous early stopping.
   Source: Async Hyperband / BOHB-style work (2018+) as representative post‑2015 scheduling practice.
   Alignment: scheduling lives as policy-bound extension (`G.11:Ext.SchedulingHeuristics`) so core semantics remain stable.
   Adoption: **Adapt** (useful practice, but quarantined outside core norms).

### G.11:12 - Relations

**Builds on:** `G.Core` (Part‑G invariants; RSCR trigger catalogue; alias docking; default ownership index), `G.6` (EvidenceGraph, `PathId/PathSliceId`), `G.7` (Bridge sentinels; CL/Φ/plane pins), `G.5` (selector & set-return), `G.8` (bundle telemetry hooks), `G.9` (parity), `G.10` (shipping hooks), `B.3.4` (freshness/decay), `E.18` (GateCrossing visibility).
**Coordinates with:** `G.12` (dashboard telemetry pins), optional `C.18/C.19` (QD/E–E pins), `C.23` (SoS-LOG branches and maturity ladders), `F.15` (RSCR harness surfaces, when present).
**Publishes to:** UTS (refresh plan/report, deprecations, edition bumps), and to the relevant owner patterns’ publication surfaces via delegated actions.

### G.11:End

## G.12 — DHC Dashboards (Discipline‑Health time‑series; lawful telemetry; generation‑first)

**Tag:** Architectural kit pattern (conceptual; notation‑independent; dashboard‑kit owner)

**Stage:** design‑time authoring **→** run‑time computation & publication (series and slices); **refresh/RSCR‑wired**

**Primary hooks:** **G.Core** (core invariants, linkage catalogues, RSCR trigger catalogue, default ownership index), **C.21** (DHC slots + `DHCPack` / `DHCMethodSpec` / `DHCSeries` artefacts), **G.6** (EvidenceGraph; `PathId`/`PathSliceId` citation), **G.7** (Bridge calibration / CL & `Φ/Ψ/Φ_plane` policy surfaces; when crossings/plane routing is used), **G.11** (telemetry‑driven refresh/decay orchestration), **G.5** (selector portfolios / set‑returning outputs, when dashboard consumes performance trade‑offs), **A.19** (CN‑Spec contract surface), **G.0** (CG‑Spec legality gate), **F.17/F.18** (UTS + twin labels), **E.5.2** (notation independence), **E.10** (LEX discipline).
*(Optional, extension‑gated hooks:* **G.2** (SoTA palette & DHC alignment hooks), **C.18/C.19** (QD / E‑E / OEE telemetry pins), **G.8** (SoS‑LOG bundle & maturity ladder view), **G.10** (shipping inclusion of dashboard slices).)*

**Why this exists.** **C.21** defines *what* lawful “discipline health” slots are (CHR‑typed; scale/legality aware; freshness‑windowed), but it does not, by itself, provide a **generation‑first** method for producing **edition‑pinned, evidence‑citable DHC time series** that remain refreshable under RSCR.
**G.12** is that dashboard method: it defines the **dashboard kit surfaces** (`DHCSeries@Context`, `DHCRow@Context`, `DashboardSlice@Context`, telemetry pins) and a pipeline for computing and publishing DHC readings **without shadow specs**, **without illicit arithmetic**, and **without smuggling scalar winners** out of partial orders or telemetry.

**Modularity note.** G.12 owns **dashboard artefacts and wiring** only. It **does not** own CN‑Spec / CG‑Spec / CHR / CAL / selection semantics / evidence semantics / shipping / refresh heuristics. It binds to those owners via refs/pins/editions/policy‑ids and keeps any method‑/generator‑specific panels strictly inside **Extensions** (`GPatternExtension` blocks).

### G.12:1 — Intent

Produce **lawful, reproducible, refresh‑aware discipline‑health dashboards** by turning **C.21** DHC definitions into:

1. a **UTS‑published** time series (`DHCSeries@Context`) whose rows are evidence‑citable by **`PathId`/`PathSliceId`**,
2. a dashboard slice surface (`DashboardSlice@Context`) that is **view‑only** (no hidden re‑aggregation or “new objectives”), and
3. **telemetry pins** that allow **G.11** to plan **slice‑scoped refresh** (rather than “rerun everything”).

### G.12:2 — Problem frame

Dashboards routinely drift or become illegal when they:

* mix scales (ordinal treated as interval; “average maturity level”),
* hide normalization and re‑parameterization (“normalized score” with no CN‑Spec pins),
* silently cross Contexts or planes (implicit reuse without explicit Bridge/Plane routing),
* fail to pin editions of computation methods, descriptor spaces, or distances,
* turn portfolios/archives into a single scalar “winner” by dashboard fiat,
* cannot refresh selectively (no actionable telemetry pins; only narrative “this changed”).

We need a **dashboard kit** that makes the *method of obtaining dashboard values* explicit and auditable, while keeping universal invariants single‑owned in **G.Core**.

### G.12:3 — Forces

* **Legality and comparability are contract‑owned.** Dashboards must not invent local legality/acceptance/normalization “mini‑specs”; they pin and cite **CN‑Spec** and **CG‑Spec** surfaces (routed via **G.Core**).
* **Ordinal discipline is non‑negotiable.** The most common dashboard failure mode is illicit arithmetic on ranks/categories; the kit must make “compare‑only” enforceable.
* **Set‑returning discipline survives into views.** Dashboards must not silently scalarize partial orders or selector portfolios; any scalarization/promotion is an explicit owner policy (routed via **G.Core**; semantics owned by the relevant pattern/policy).
* **Edition‑awareness is the difference between “trend” and “drift”.** If the method definition changes, the dashboard must either (i) fork series edition, or (ii) emit telemetry and refresh slices under pinned conditions.
* **RSCR must be actionable.** Causes are emitted as **canonical ids** (typed trigger kinds + id‑valued pins), not prose.

### G.12:4 — Solution — Compute and publish DHC series lawfully, with RSCR‑ready telemetry

#### G.12:4.0 — G.Core linkage (normative)

This pattern is **core‑invariant‑bearing** and therefore binds to **G.Core** by declaration (not by restating invariants here).

**GCoreLinkageManifest (G.12)** *(normative; expands per `G.Core:4.2`)*
Effective obligations/pins/triggers are computed as **union(expand(sets), explicit deltas)** under `Nil‑elision`.

* `CoreConformanceProfileIds` := {
  `GCoreConformanceProfileId.PartG.AuthoringBase`,
  `GCoreConformanceProfileId.PartG.TriStateGuard`,
  `GCoreConformanceProfileId.PartG.UTSWhenPublicIdsMinted`,
  `GCoreConformanceProfileId.PartG.ShippingBoundary`
  }

* `RSCRTriggerSetIds` := {
  `GCoreTriggerSetId.BridgeCalibrationKit`
  }

* `RSCRTriggerKindIds` := {
  `RSCRTriggerKindId.LegalitySurfaceEdit`
  }
  *(Any additional causes required by optional dashboard panels MUST be introduced only by the corresponding `GPatternExtension` blocks in `G.12:4.9`.)*

* `DefaultsConsumed` := `∅`
  *(Default routing for `DefaultId.PortfolioMode` / `DefaultId.DominanceRegime` is only relevant when portfolio outputs are consumed; see `G.12:Ext.PortfolioTelemetry`.)*

* `CorePinSetIds` := {
  `GCorePinSetId.PartG.AuthoringMinimal`,
  `GCorePinSetId.PartG.CrossingVisibilityPins`
  }

* `CorePinsRequired` *(pattern delta; pin names only; all are id‑valued unless noted)* := {
  `DHCSeriesId`,
  `TargetSlice` *(USM tuple; varies only by `Γ_time` across rows; no implicit “latest”)*,
  `Γ_time` *(time selector / freshness window; required per row; series MAY additionally declare a window‑family spec)*,
  `DHCSlotId[]` *(C.21‑owned typed DHC slots; each resolves to `CharacteristicId` + scale/unit/polarity + reference plane binding + lane discipline)*,
  `DHCMethodSpecRef.edition`,
  `DHCMethodRef.edition`,
  `PathSliceId[]`
  }
  *(Nil‑elision applies. All other definition pins are conditional: they MUST appear only when actually used and when their semantic owner/extension is present (e.g., UNM/normalization pins, QD/OEE telemetry pins, transfer rules pins, pack inclusion pins).)*

* `TriggerAliasMapRef` := `∅`

#### G.12:4.1 — Objects (LEX heads; twin‑register discipline)

All objects below are **notation‑independent**; serialisations (if any) live under shipping/interop ownership, not here.

**(1) `DHCSeries@Context`** *(UTS‑published dashboard series; C.21‑grounded)*
A time‑indexed publication of computed DHC readings for a `Discipline × ContextSlice`, aligned with `U.DHCSeries` semantics from **C.21** and pinned to method/contract refs.

Minimal fields (conceptual; ids/pins only):

`DHCSeries@Context := ⟨  
  DHCSeriesId,  
  CG-FrameContext,  
  describedEntity := ⟨GroundingHolon, ReferencePlane⟩,  
  TargetSlice,                         // USM tuple; time series varies Γ_time across rows (explicit, no implicit “latest”)  
  DHCSlotId[],                         // slot set selected from C.21 (typed DHC slots; not “just Characteristic ids”)  
  DHCPackRef.edition?,  
  DHCMethodSpecRef.edition,  
  WindowSpec?,                         // optional window-family spec used to generate per-row Γ_time  
  CNSpecRef.edition, CGSpecRef.edition,  
  EvidenceGraphId?,                    // if resolvable; else row-level Path pins suffice  
  DashboardSliceId[]?,                 // published view slices (optional)  
  TelemetryPinSetId?                   // wiring to refresh (conceptual)  
⟩`

**(2) `DHCRow@Context`** *(one timepoint / window reading; Work/Audit‑citable)*
A single computed row of the series.

`DHCRow@Context := ⟨  
  DHCRowId,  
  DHCSeriesId,  
  Γ_time,  
  DesignRunTag = run,  
  DHCSlotId,  
  value, units/scaleRef?, compareOnly?,  
  stance ∈ {pass|degrade|abstain},  
  DHCMethodRef.edition, DHCMethodSpecRef.edition,  
  PathSliceId[], PathId[]?, EvidenceGraphId?,  
  evidenceLaneTags? := {TA|VA|LA},  
  crossingPins? := ⟨BridgeId[], PlaneMapRef.edition?, CL/CL^k/CL^plane?, Φ/Ψ/Φ_plane policy‑ids…⟩  
⟩`

**(3) `DashboardSlice@Context`** *(view surface; non‑semantic)*
A view‑friendly grouping over one or more series/rows. It MUST NOT introduce new aggregation/legality semantics; it is a projection over already computed, pinned, citable rows.

`DashboardSlice@Context := ⟨  
  DashboardSliceId(UTS),  
  DHCSeriesId(UTS)[],  
  SliceAnnotations?,                  // labels, grouping metadata, explanatory text  
  ViewSpecId?,                        // view template id (policy‑bound; no semantics implied)  
  IncludedRowIds?  
⟩`

**(4) `DHCTelemetryPin`** *(refresh wiring pin; id‑based causes)*
A conceptual telemetry pin emitted to refresh/orchestration (owner: **G.11**) with canonical trigger kind ids.

`DHCTelemetryPin := ⟨  
  triggerKindId: RSCRTriggerKindId,  
  scope: PathSliceId[] | PatternScopeId,  
  payloadPins: { …ids… }              // editions, policy‑ids, UTS row ids, window ids, etc.  
⟩`

**Ref discipline.** `.edition` SHALL appear only on `…Ref` (per **E.10**). Dashboard artefacts that mint public ids publish **Tech/Plain twins** (UTS discipline).

#### G.12:4.2 — Method‑of‑Obtaining Output (generation‑first; design‑time → run‑time)

**Stage A — Author & bind (design‑time)**

A1. **Select the DHC slot set (owner: C.21).**
Choose `DHCSlotId[]` from **C.21** (typed DHC slots), and declare the series scope explicitly as `TargetSlice` (USM tuple) plus an explicit time selector (`Γ_time` per row; optionally a `WindowSpec` that generates the row windows). Do not restate slot semantics in the dashboard kit; cite the C.21 owners.

A2. **Bind contract surfaces (owners: A.19, G.0).**
Pin `CNSpecRef.edition` and `CGSpecRef.edition`. Any normalization or numeric comparability assumptions are expressed by explicit CN‑Spec artefacts (ids/refs) and any numeric legality requirements cite CG‑Spec artefacts (SCP / MinimalEvidence / Γ‑fold pins as applicable). The dashboard does not introduce local “shadow specs”.
If the dashboard series/slice actually uses cross‑Context or cross‑plane routing, it MUST additionally pin the relevant crossing and penalty‑policy surfaces as ids (Bridge/CL/plane ids, `Φ/Ψ/Φ_plane` policy‑ids, `PlaneMapRef.edition?`) and cite their semantic owners (typically `G.7` for bridge calibration/CL kits, routed via `G.Core`). The dashboard MUST NOT encode a dashboard‑local “penalty regime”.

A3. **Pin computation methods (owner: C.21).**
For each slot/method used to compute a time series value, record `DHCMethodSpecRef.edition` and `DHCMethodRef.edition` (table‑backed, per C.21). The dashboard series is edition‑aware: if a method spec changes, the dashboard either forks the series edition or emits telemetry and refreshes under explicit pins.

A4. **Declare optional panels via Extensions only.**
If the dashboard depends on (i) selector portfolio outputs, (ii) QD illumination / archive telemetry, (iii) open‑endedness telemetry, (iv) maturity ladder views, or (v) pack inclusion, then the relevant `GPatternExtension` block(s) in `G.12:4.9` MUST be present and their pins MUST be satisfied.

**Stage B — Compute rows (run‑time; Work/Audit)**

B1. **Resolve evidence by Path (owner: G.6).**
Compute rows from evidence cited as `PathSliceId[]` (and `PathId[]` when needed), under the declared window/freshness regime. Preserve lane discipline and handle missingness using tri‑state stances (routed via **G.Core**).

B2. **Compute slot values using pinned methods (owner: C.21).**
Compute each slot value by applying the pinned `DHCMethodRef.edition`/`DHCMethodSpecRef.edition` under the pinned contract surfaces. Enforce “no illicit arithmetic” for ordinals/categoricals as a dashboard‑kit obligation (see CC‑G12.\*).
Any cross‑Context/plane use is expressed only via explicit crossing pins (Bridge/Plane routing) and policy ids (routed via **G.Core**).

B3. **Emit RSCR‑actionable telemetry pins (owner: G.11).**
When any of the declared pins/editions/policies/windows/evidence slices change, emit `DHCTelemetryPin` events with canonical `RSCRTriggerKindId` and payload pins sufficient for **slice‑scoped** refresh planning.

**Stage C — Publish series & slices (run‑time; publication)**

C1. **Publish `DHCRow@Context` and `DHCSeries@Context` as UTS artefacts.**
Mint/publish UTS rows with Tech/Plain twins and include the required pins (window, reference plane, method editions, evidence paths).

C2. **Publish `DashboardSlice@Context` as a view‑only projection.**
Slices are groupings/annotations over already computed rows; they must not redefine legality, acceptance, or scalarization.

C3. **Wire refresh via telemetry pins (no orchestration ownership).**
Dashboards emit pins; refresh orchestration remains owned by **G.11**.

#### G.12:4.9 — Extensions (pattern‑scoped; non‑core)

> **Extension rule (Phase‑2).** Anything method‑, generator‑, or view‑family‑specific belongs here, as `GPatternExtension` modules. These modules may add **mode‑specific definition pins** and additional RSCR trigger kinds, but MUST NOT redefine Part‑G‑wide invariants or defaults.

##### `G.12:Ext.SoTAPalette` — SoTA palette & DHC alignment hooks (optional)

**PatternScopeId:** `G.12:Ext.SoTAPalette`
**GPatternExtensionId:** `SoTAPalette`
**GPatternExtensionKind:** `InteropSpecific`
**SemanticOwnerPatternId:** `G.2` *(SoTA palette + DHC alignment hooks semantics live in G.2; G.12 only wires them)*
**Uses:** `{G.2}`
**⊑/⊑⁺:** `∅`

**RequiredPins/EditionPins/PolicyPins (minimum):**

* `SoTA_PackRef.edition?`
* `DHC-SenseCellId[]?` *(when series pins to DHC alignment hooks / sense‑cell inventories)*
* `DHCAlignmentHookId[]?`

**RSCRTriggerKindIds (delta):** `∅`

##### `G.12:Ext.PortfolioTelemetry` — selector/portfolio integration panel

**PatternScopeId:** `G.12:Ext.PortfolioTelemetry`
**GPatternExtensionId:** `PortfolioTelemetry`
**GPatternExtensionKind:** `MethodSpecific`
**SemanticOwnerPatternId:** `G.5` *(portfolio semantics and set‑return discipline)*
**Uses:** `{G.5, G.6}`
**⊑/⊑⁺:** `∅`

**RequiredPins/EditionPins/PolicyPins (minimum):**

* `TaskSignatureRef?` *(when portfolio semantics depend on TaskSignature traits)*
* `DominanceRegime` *(resolved via `DefaultId.DominanceRegime` owner routing; publish the resolved regime, do not invent a local default)*
* `PortfolioMode` *(resolved via `DefaultId.PortfolioMode` owner routing; publish the resolved mode)*
* `SCRId/DRRId` *(or equivalent selector evidence pins, when dashboard row depends on selector outcomes)*

**DefaultsConsumed:** {`DefaultId.DominanceRegime`, `DefaultId.PortfolioMode`} *(owners routed via `G.Core.DefaultOwnershipIndex`; no local defaults)*

**RSCRTriggerKindIds (delta):** `∅` *(base triggers suffice; any extra triggers must be explicit)*

**Notes (wiring‑only):**

* The dashboard may visualise portfolio/Archive telemetry, but MUST keep set‑returning semantics; any scalar “headline number” is a view projection, not a legality‑bearing decision.

##### `G.12:Ext.QDTelemetry` — illumination / archive telemetry panel

**PatternScopeId:** `G.12:Ext.QDTelemetry`
**GPatternExtensionId:** `QDTelemetry`
**GPatternExtensionKind:** `MethodSpecific`
**SemanticOwnerPatternId:** `C.18` *(QD / NQD‑CAL semantics; descriptor/distance/insertion policy)*
**Uses:** `{C.18, G.5, G.11}`
**⊑/⊑⁺:** `∅`

**RequiredPins/EditionPins/PolicyPins (minimum):**

* `DescriptorMapRef.edition`
* `DistanceDefRef.edition`
* `CharacteristicSpaceSpecRef.edition?` *(iff the descriptor/axis space is editioned as a published surface; required for view reproducibility)*
* `InsertionPolicyRef`
* `EmitterPolicyRef?`
* `ArchiveSnapshotRef?` *(id/pin for the published archive snapshot, if any)*
* `PathSliceId[]` *(scope for refresh; slice‑keyed)*

**RSCRTriggerKindIds (delta):** `∅` *(base trigger set already includes `RSCRTriggerKindId.TelemetryDelta`; add only genuinely additional kinds here)*

**Notes (wiring‑only):**

* Illumination/coverage signals are treated as telemetry. Any promotion of telemetry into selection dominance is owned elsewhere (typically CAL policy; routed via `G.Core`).
* If descriptor axes/dimensions are surfaced as published identifiers (not just local UI text), they MUST follow the Tech/Plain twin‑label discipline (UTS Name Cards); otherwise they remain non‑normative view annotations.

##### `G.12:Ext.OpenEndedTelemetry` — open‑endedness / transfer telemetry panel

**PatternScopeId:** `G.12:Ext.OpenEndedTelemetry`
**GPatternExtensionId:** `OpenEndedTelemetry`
**GPatternExtensionKind:** `GeneratorSpecific`
**SemanticOwnerPatternId:** `C.19` *(E/E‑LOG & exploration accounting; generator/transfer telemetry wiring)*
**Uses:** `{C.19, G.5, G.11}`
**⊑/⊑⁺:** `∅`

**RequiredPins/EditionPins/PolicyPins (minimum):**

* `TransferRulesRef.edition` *(when transfer rules are part of the telemetry interpretation)*
* `EnvironmentValidityRegionId?`
* `ProbeBudgetPolicyId?`
* `PathSliceId[]`

**RSCRTriggerKindIds (delta):** `∅` *(base trigger set already includes `RSCRTriggerKindId.TelemetryDelta`; add only genuinely additional kinds here)*

**Notes (wiring‑only):**

* Open‑endedness metrics are telemetry‑level artefacts; dashboards must not silently convert them into “dominance objectives”.

##### `G.12:Ext.MaturityLadderPanel` — maturity ladder view (optional)

**PatternScopeId:** `G.12:Ext.MaturityLadderPanel`
**GPatternExtensionId:** `MaturityLadderPanel`
**GPatternExtensionKind:** `DisciplineSpecific`
**SemanticOwnerPatternId:** `G.8` *(maturity ladder semantics in SoS‑LOG bundle/maturity cards)*
**Uses:** `{G.8, G.6, G.11}`
**⊑/⊑⁺:** `∅`

**RequiredPins/EditionPins/PolicyPins (minimum):**

* `MaturityCardRef`
* `MaturityRungId?`
* `PathId/PathSliceId` *(evidence citations for rung claims)*

**RSCRTriggerKindIds (delta):** `{RSCRTriggerKindId.MaturityRungChange}`

##### `G.12:Ext.PackInclusion` — shipping inclusion stub (optional)

**PatternScopeId:** `G.12:Ext.PackInclusion`
**GPatternExtensionId:** `PackInclusion`
**GPatternExtensionKind:** `InteropSpecific`
**SemanticOwnerPatternId:** `G.10` *(shipping owner)*
**Uses:** `{G.10}`
**⊑/⊑⁺:** `∅`

**RequiredPins/EditionPins/PolicyPins (minimum):**

* `SoTA‑PackId`
* `DashboardSliceId(UTS)` *(or `DHCSeriesId(UTS)` when shipping series directly)*
* `CNSpecRef.edition`, `CGSpecRef.edition` *(as shipped pins, per G.10 wiring)*

**RSCRTriggerKindIds (delta):** `∅`

**Notes (wiring‑only):**

* This module is a wiring stub: it does not define shipping behaviour; it only states which dashboard artefacts may be cited by `SoTA‑Pack(Core)`.

##### `G.12:Ext.ViewFamilySeed` — advanced view families (Phase‑3 seed; owner TBD)

**PatternScopeId:** `G.12:Ext.ViewFamilySeed`
**GPatternExtensionId:** `ViewFamilySeed`
**GPatternExtensionKind:** `Phase3Seed`
**SemanticOwnerPatternId:** `owner TBD`
**Uses:** `{}`
**⊑/⊑⁺:** `∅`

**Notes (Phase‑3 seed; non‑normative):**

* Placeholder for advanced dashboard view families (e.g., embedding‑based similarity panels, predictive drift detectors, change‑point overlays). Any such module must remain policy‑bound and must not introduce new Part‑G‑wide norms.

### G.12:5 — Interfaces (conceptual; kit surface)

| ID  | Interface   | Consumes   | Produces  |
| --- | ----------- | ---------- | --------- |
| **G.12‑1 `Create_DHCSeries`** | Create/bind a DHC series scope (C.21‑grounded; edition‑aware) | `DHCSlotId[]`, `DHCPackRef.edition?`, `DHCMethodSpecRef.edition`, `TargetSlice` (USM), `WindowSpec?`, `ReferencePlane`, `CNSpecRef.edition`, `CGSpecRef.edition` | `DHCSeries@Context` (UTS artefact; edition‑aware) |
| **G.12‑2 `Update_DHCSeries`** | Compute/update one or more rows under pinned conditions (run‑time; Work/Audit‑citable) | `PathSliceId[]`, `EvidenceGraphId?`, `DHCMethodRef.edition`, `DHCMethodSpecRef.edition`, `Γ_time`, crossing pins (if any) | `DHCRow@Context[]` (UTS artefacts; stance + pins; `DesignRunTag = run`) |
| **G.12‑3 `Integrate_PortfolioTelemetry`** *(extension‑gated)* | Integrate selector/portfolio evidence into a slice/series | See `G.12:Ext.PortfolioTelemetry` | Extension‑gated fields / telemetry pins |
| **G.12‑4 `Integrate_QDTelemetry`** *(extension‑gated)* | Integrate QD illumination/archive telemetry | See `G.12:Ext.QDTelemetry` | Extension‑gated fields / telemetry pins |
| **G.12‑5 `Integrate_OEETelemetry`** *(extension‑gated)* | Integrate open‑endedness / transfer telemetry | See `G.12:Ext.OpenEndedTelemetry` | Extension‑gated fields / telemetry pins |
| **G.12‑6 `Publish_DashboardSlice`** | Publish a view slice as a projection over computed rows | `DHCSeriesId(UTS)[]`, `DHCRowId(UTS)[]?`, `SliceAnnotations?` | `DashboardSlice@Context` (UTS artefact; view‑only) |
| **G.12‑7 `Emit_TelemetryPins`** | Emit RSCR‑actionable telemetry pins for refresh | `RSCRTriggerKindId`, `scope`, `payloadPins` | `DHCTelemetryPin[]` (consumed by `G.11`) |

(*No file formats are introduced here; serialisation recipes live under shipping/interop ownership.*)

### G.12:6 — Conformance checklist (CC‑G12, normative)

| CC ID   | Requirement  | Verification notes  |
| ------- | ------------ | ------------------- |
| **CC‑G12‑CoreRef** | The pattern satisfies the **effective** `G.Core` obligations declared by `GCoreLinkageManifest (G.12)` (profiles/sets/deltas expanded per `G.Core:4.2`).    | Evidence: the manifest is present; required pins/defaults/triggers are accounted for; no local restatement overrides core owners.  |
| **CC‑G12.1** | **DHC slot typing (C.21‑grounded).** Every published dashboard value is indexed by a **C.21‑authored** `DHCSlotId` (typed DHC slot: `CharacteristicId` + scale/unit/polarity + reference plane binding + lane discipline) and is scoped by an explicit `TargetSlice` + `Γ_time`. | Evidence: row/series references `DHCSlotId` and pins `ReferencePlane` and `Γ_time` (or a series `WindowSpec` that yields row Γ_time). |
| **CC‑G12.2** | **Edition discipline (no drift).** Every published time‑series value carries `DHCMethodRef.edition` and any other definition‑pins actually used to obtain it (e.g., `DescriptorMapRef.edition`, `DistanceDefRef.edition`, `UNM_id`, `NormalizationMethodInstanceId[]`, `ComparatorSetRef.edition?`). No free‑text versioning. | Check that `.edition` appears only on `…Ref`; check presence of all definition pins used by the pipeline; extension pins appear only when their extension blocks are present. |
| **CC‑G12.3** | **Contract citation for numeric operations (no shadow specs; no illicit arithmetic).** Any numeric operation in the dashboard pipeline is legal only under explicit **CG‑Spec** and **CN‑Spec** pins (e.g., `SCPRef.edition`, `MinimalEvidenceRef.edition`, `ΓFoldRef.edition?` when used), and any normalization is explicit (`UNM_id` + `NormalizationMethodInstanceId[]` etc). Ordinal/categorical slots remain **compare‑only** (no illicit arithmetic). | Check that operations cite pinned owners; reject “normalize, then compare” without explicit UNM pins; reject arithmetic over ordinal slots unless an owner‑declared lawful mapping exists. |
| **CC‑G12.4** | **Set‑returning selection is preserved.** If the dashboard consumes selection/portfolio outputs, it MUST preserve set‑return semantics and MUST publish the resolved `DominanceRegime` and `PortfolioMode` by citing the single owners (via `G.Core.DefaultOwnershipIndex`) rather than inventing local defaults. Any promotion of illumination/telemetry into dominance MUST cite the owner policy (typically CAL) and be auditable via evidence paths. | Check for set/portfolio outputs; check that any scalar headline is view‑only; check citations to owner defaults/policies. |
| **CC‑G12.5** | **UTS publication discipline.** `DHCSeries@Context` and its rows (and any published slices) are published as UTS artefacts with Tech/Plain twins and stable identifiers; deprecations/edition bumps follow the canonical UTS discipline. | Check stable ids + twin labels; check that publication does not smuggle “gate decisions” as authoritative artefacts. |
| **CC‑G12.6** | **Bridge/plane routing is explicit when used.** If a series crosses contexts or planes, the rows MUST cite the Bridge/PlaneMap routing (`BridgeId[]`, `CL/CL^k/CL^plane`, `Φ/Ψ/Φ_plane policy‑ids`, `PlaneMapRef.edition?`) and respect penalty routing to `R_eff` only (semantics routed via `G.Core`). | Check presence of crossing pins when contexts/planes differ; check that any loss is expressed via R‑lane impact only. |
| **CC‑G12.7** | **Telemetry sufficiency for slice‑scoped RSCR.** Emitted dashboard telemetry pins MUST (i) use canonical `RSCRTriggerKindId`, (ii) include `scope` (PathSliceId[] or PatternScopeId) and the touched `…Ref.edition`/policy/window pins, and (iii) block publication when required pins are missing. Each published row is evidence‑citable by `PathSliceId[]` under explicit `Γ_time`. | Check: no free‑text causes; payload includes path/window/editions/policies; missing pins block publish; row has PathSliceId[] and Γ_time. |
| **CC‑G12.8** | **Extension gating.** If any extension‑owned fields/pins appear, the corresponding `G.12:Ext.*` module is present and satisfied. | E.g., QD pins require `G.12:Ext.QDTelemetry`; maturity panel requires `G.12:Ext.MaturityLadderPanel`; SoTA palette hooks require `G.12:Ext.SoTAPalette`; pack inclusion requires `G.12:Ext.PackInclusion`. |

### G.12:7 — Bias‑Annotation (informative)

* **Didactic:** dashboard artefacts publish pins and paths first; views second.
* **Architectural:** no “dashboard‑local contract surfaces”; invariant routing is via `G.Core`.
* **Pragmatic:** slice‑scoped refresh is enabled by canonical trigger ids + payload pins.
* **Epistemic:** compare‑only ordinals and explicit provenance prevent “trend‑as‑drift”.

### G.12:8 — Consequences

* **Dashboards become reproducible artefacts, not screenshots.** A `DHCRow@Context` is re‑derivable under pinned editions and evidence windows.
* **Selective maintenance becomes possible.** Telemetry pins let `G.11` refresh what changed (path slice / window / method edition), rather than rerunning the entire pipeline.
* **Illicit scalarization is structurally discouraged.** Set‑returning and contract‑owned semantics are preserved into the dashboard layer.

### G.12:9 — Relations

**Builds on:** `G.Core`, `C.21`, `G.6`, `G.11`, `A.19`, `G.0`, `F.17/F.18`, `E.5.2`, `E.10`.
**Coordinates with:** `G.5` *(when portfolio/set outputs are consumed)*, `G.7` *(when crossings/plane routing or `CL/Φ/Ψ/Φ_plane` policy pins are used)*, `G.8` *(when maturity ladder view is included)*, `G.10` *(when dashboard slices are shipped)*.
**Constrains:** dashboard consumers: dashboards are projections over pinned, evidence‑citable rows; they do not mint new contract semantics.

### G.12:10 — Author’s quick checklist

1. Declare the dashboard series scope: `TargetSlice` (USM tuple), `ReferencePlane`, and an explicit `Γ_time` regime (per‑row; optionally a `WindowSpec` that yields the row windows).
2. Select `DHCSlotId[]` and cite **C.21** (do not restate slot semantics).
3. Pin `DHCMethodSpecRef.edition` and `DHCMethodRef.edition` for every computed slot/value (plus any other definition pins actually used).
4. Ensure rows are evidence‑citable by `PathSliceId[]` and include explicit `Γ_time` (row is run‑time: `DesignRunTag = run`).
5. Publish UTS artefacts with twins and the required pins.
6. Emit canonical telemetry pins (`RSCRTriggerKindId` + scope + payload pins) for `G.11`.
7. If SoTA palette hooks / portfolio / QD / OEE / maturity / shipping panels are needed, add the corresponding `G.12:Ext.*` blocks and satisfy their pins.

### G.12:11 — Worked micro‑examples (informative; SoTA‑oriented)

**(A) Decision‑making discipline dashboard (multi‑tradition).**
Slots (from **C.21**): *ReproducibilityRate* (freshness‑windowed), *StandardisationLevel* (ordinal), *AlignmentDensity* (bridge density over DHC‑SenseCells), *MetaDiversity* (operator family diversity), *DisruptionBalance* (target‑band metric).
Evidence: citation graphs, benchmark traces, and bridge calibrations are referenced via `PathSliceId[]`.
Optional panels:

* `G.12:Ext.PortfolioTelemetry` to visualise set‑returning method portfolios without forcing a scalar winner.
* `G.12:Ext.QDTelemetry` to include illumination/archive telemetry using modern QD families (e.g., CMA‑ME / policy‑gradient QD variants / surrogate‑assisted illumination lines) as telemetry.

**(B) Evolutionary software architecture dashboard (open‑endedness‑aware).**
Slots: stability/reproducibility metrics, standardisation stages (ordinal), cross‑paradigm alignment density, and disruption balance.
Optional panels:

* `G.12:Ext.OpenEndedTelemetry` to include open‑endedness telemetry (environment diversity / transfer events) using POET‑style and related post‑2015 open‑ended generation families, while keeping such signals in telemetry unless an explicit owner policy promotes them.

### G.12:End

## G.13 - External Interop Hooks for SoTA Discipline Packs (conceptual)

**Tag.** Architectural kit pattern (conceptual interop kit; notation‑independent; normative when used)
**Stage.** *design‑time registration & alignment* → *run‑time ingestion, telemetry, refresh*
**Primary hooks.** `G.Core` (Part‑G core invariants + trigger catalogue + default ownership), `G.2` (SoTA Synthesis Pack), `G.3` (CHR Pack), `G.4` (CAL Pack), `G.5` (selector & registries), `G.6` (EvidenceGraph + PathId/PathSliceId), `G.7` (BridgeMatrix + CL/planes), `G.8` (SoS‑LOG bundle surfaces), `G.9` (parity harness), `G.10` (shipping), `G.11` (refresh orchestration), `G.12` (dashboards), `A.19` (CN‑Spec), `A.18` (CSLC legality), `G.0` (CG‑Spec), `F.17` (UTS), `E.5.2` (notation independence), `E.18/A.21/A.27` (GateCrossing/CrossingSurface checks).

**Status.** Draft (Phase‑2 universalized; `G.Core` linkage explicit)
**Normativity.** Normative when used (when any `G.13` surface is authored/emitted/consumed); informative otherwise.

**Non‑duplication note (Phase‑2 universalization).** This pattern **does not restate** Part‑G‑wide invariants (contract‑surface single‑ownership, crossing visibility, penalty routing, set‑return discipline, typed RSCR triggers, default ownership, Δ‑discipline). Those are **single‑owned** in `G.Core` and referenced here via the linkage manifest and CC delegations (*cite, don’t duplicate*).

### G.13:1 - Problem frame

FPF already supports lawful characterization, evidence wiring, selector‑side set returns, parity, shipping, dashboards, and refresh. What remains frictionful in practice is **interoperability with external scholarly indexes and discipline repositories** (concept registries, paper/claim graphs, dataset registries, taxonomy stores, “science‑of‑science” indicator feeds), which teams routinely use as *inputs* when authoring a SoTA discipline pack.

Without an explicit **conceptual interop kit**, authors tend to build one‑off pipelines whose “implied semantics” leak into the framework: edition drift becomes invisible, cross‑plane/context reuse becomes implicit, and external signals quietly start acting like a shadow contract surface.

`G.13` provides the missing kit: **conceptual registration, alignment, and telemetry hooks** that let external sources be wired into the Part‑G pipeline (**G.2 → G.5 → G.9 → G.10 → G.11**, and optionally **G.12**) while preserving Part‑G invariants via `G.Core`.

### G.13:2 - Problem

External sources publish **claim‑adjacent signals** (citations, concept graphs, “task/method” tags, replication links, dataset usage, disruption‑style indicators, benchmark metadata). These are useful for *generation* (palette building, portfolio exploration, candidate bridge discovery), not only for audit. But typical interop practices create predictable failure modes:

* **Contract‑surface leakage.** External numeric signals get treated as if they were lawful “scores” without explicit binding to CHR/CAL/CG surfaces.
* **Implicit crossings.** Cross‑context and cross‑plane reuse happens through opaque transformations, without explicit exposure of the crossing surface pins needed downstream.
* **Edition drift + refresh brittleness.** Snapshots change, schemas drift, indicator definitions get revised; without edition‑pinned interop surfaces and typed trigger causes, parity and dashboard stability degrade.
* **Evidence disconnect.** “Derived features” are produced without explicit EvidenceGraph anchoring, making later refutation/repair expensive.
* **Format‑as‑norm.** A convenient serialisation (KG export, JSON schema, RO‑Crate, etc.) becomes treated as the specification, undermining notation independence.

### G.13:3 - Forces

| Force                           | Tension                                                                                                |
| ------------------------------- | ------------------------------------------------------------------------------------------------------ |
| **Notation independence**       | Useful serialisations vs the requirement that conformance is judged on **conceptual** surfaces.        |
| **Pluralism vs parity**         | Diverse scholarly traditions and indexes vs lawful, edition‑aware comparability and reproducibility.   |
| **Interop as generation input** | Interop should speed SoTA authoring, not merely decorate audit reports.                                |
| **Planes & bridges**            | Cross‑plane/context reuse must remain explicit and auditable rather than implicit in “aligners”.       |
| **Telemetry vs dominance**      | External telemetry should inform exploration and refresh without silently changing selector semantics. |
| **Operational drift**           | External sources evolve; interop must be refresh‑ready by construction (typed causes + payload pins).  |

### G.13:4 - Solution — Conceptual interop kit: registered sources, alignment cards, feature derivations, and RSCR‑wired telemetry

#### G.13:4.1 - G.Core linkage (normative)

**Builds on:** `G.Core`.

**GCoreLinkageManifest (normative).**
*(Canonical form, Nil‑elision, and Expansion rule are defined in `G.Core`.)*

`GCoreLinkageManifest := ⟨
  CoreConformanceProfileIds := {
    GCoreConformanceProfileId.PartG.AuthoringBase,
    GCoreConformanceProfileId.PartG.UTSWhenPublicIdsMinted,
    GCoreConformanceProfileId.PartG.ShippingBoundary
  },
  RSCRTriggerSetIds := {GCoreTriggerSetId.SoTAHarvestSynthesis},
  RSCRTriggerKindIds := {RSCRTriggerKindId.BaselineBindingEdit},   // delta: planned‑baseline linkage edits can be interop‑relevant

  CorePinSetIds := {
    GCorePinSetId.PartG.AuthoringMinimal,
    GCorePinSetId.PartG.CrossingVisibilityPins
  },

  CorePinsRequired := {
    // Interop pins (G.13‑specific; avoid duplicating `GCorePinSetId.PartG.CrossingVisibilityPins`)
    ExternalIndexRef.edition,
    ClaimMapperRef.edition?,
    MappingPolicyRef?,
    PlaneMapRef.edition?,
    ScaleEmbeddingSpecRef.edition?,

    EvidenceGraphId?,
    InteropSurfaceId?
  },

  DefaultsConsumed := {DefaultId.PortfolioMode, DefaultId.DominanceRegime}
⟩`

**Payload‑pin note (informative).** When emitting RSCR triggers for interop‑driven changes, payload pins should include the edited edition/policy identifiers, the impacted scope, and the applicable crossing‑visibility pins (per `GCorePinSetId.PartG.CrossingVisibilityPins`) when crossings/UTS/paths are involved.

#### G.13:4.2 - Interop kit objects & surfaces (pattern‑owned; notation‑independent)

All objects below are **conceptual**. Any concrete serialisation belongs to Annex/Interop or tooling notes and is not normative for Part‑G conformance.

* **`ExternalIndexCard@Context`** — registration of an external source and its snapshot.

  **Shape (conceptual):**
  `⟨ ExternalIndexId, ProviderName?, ExternalIndexType, CoverageScope, Licence?, ExternalEdition, FreshnessWindow?, describedEntity := ⟨GroundingHolon, ReferencePlane⟩, Notes? ⟩`

  **Intent.** Create a stable, citable “source card” so downstream artefacts can pin the *card edition* via `ExternalIndexRef.edition`, while the provider snapshot remains visible as `ExternalEdition` (do not echo provider snapshot ids into downstream cards; cite refs instead).

* **`ClaimMapperCard@Context`** — a conceptual “mapping recipe” that yields FPF‑native artefacts from an external source.

  **Shape (conceptual):**
  `⟨ MapperId, ExternalIndexId, MappingPolicyRef, Targets{ClaimSheet|BridgeHints|SoSFeatureSet|UTSProposals}, PlaneMapRef?, ScaleEmbeddingSpecRef?, EvidenceGraphId?, CSLCProofStubs? ⟩`

  **Notes.**

  * This is **not** a shadow legality gate. It is an interop surface that **cites** owners (`A.19`, `G.0`, `G.3`, `G.4`) and publishes the required pins for downstream audit/refresh.
  * When cross‑plane or cross‑context reuse is implicated, the alignment outputs must route via the existing crossing surfaces (see `G.Core` linkage).
  * Avoid “edition echo”: downstream artefacts cite `ExternalIndexRef.edition` and `ClaimMapperRef.edition` (and optional `PlaneMapRef.edition` / `ScaleEmbeddingSpecRef.edition`) rather than copying snapshot ids/editions as free fields.

* **`SoSFeatureTransform@Context`** — declares how external signals become **CHR‑typed** SoS features (for DHC/dashboard usage and/or SoS‑LOG rule evaluation).

  **Shape (conceptual):**
  `⟨ SoSFeatureTransformId, Inputs{ClaimSheetId[] | ExternalSignalsRef}, SoSFeatureSetId, FeatureTypingRefs{CharacteristicId/ScaleId/CoordinateId}, ReferencePlane, EvidenceGraphId?, PathSliceId[]?, ProofHooks? ⟩`

  **Notes.**

  * The derivation is a **typing + provenance** surface; it does not introduce new comparators or new contract surfaces.

* **`ScaleEmbeddingSpec@Context`** — optional constraints for representation/space alignment used inside an alignment recipe.

  **Shape (conceptual):**
  `⟨ ScaleEmbeddingSpecId, IntendedUse, AllowedTransformFamily, RequiredPins{NormalizationMethodRef.edition?}, ProhibitedCoercions ⟩`

  **Design intent.** Make any representation alignment *explicitly constrained* and edition‑pinned, instead of silently “creating a new scale”.
  **LEX/UTS note (informative).** `ScaleEmbeddingSpec` is a new LEX head; when it mints a public id it must be published to UTS with twin labels (see `G.Core` / UTS profile).

* **`IndexTelemetryPin`** — an emitted refresh input that makes interop changes RSCR‑visible.

  **Shape (conceptual; RSCR‑typed):**
  `⟨ triggerKindId: RSCRTriggerKindId, scope: PathSliceId[] | PathId[] | PatternScopeId, payloadPins{ExternalIndexId, ExternalIndexRef.edition, ClaimMapperRef.edition?, MappingPolicyRef?, PlaneMapRef.edition?, ScaleEmbeddingSpecRef.edition?, PathId[]?, PathSliceId[]?, UTSRowId[]?, …} ⟩`

  **Routing.** Emitted to `G.11` as refresh input; recorded with canonical `RSCRTriggerKindId` causes.

* **`InteropSurface@Context`** — a selector‑/dashboard‑facing summary of what interop artefacts exist and how they are pinned.

  **Shape (conceptual):**
  `⟨ InteropSurfaceId, ExternalIndexId, ExternalIndexRef.edition, MapperId?, ClaimMapperRef.edition?, MappingPolicyRef?, SoSFeatureSetId?, EvidenceGraphId?, PathSliceId[]?, PlaneMapRef.edition?, ScaleEmbeddingSpecRef.edition?, UTSRowId[] ⟩`

  **Publication.** Published to UTS with twin labels as applicable.

#### G.13:4.3 - Generation‑first interop flow (notation‑independent; owner‑delegating)

1. **Register source editions.** Author `ExternalIndexCard@Context` for each external source/snapshot used for SoTA authoring, including `ExternalEdition` and the `describedEntity` plane anchor.
2. **Author mapping recipes.** Create `ClaimMapperCard@Context` describing which FPF artefacts are produced (ClaimSheets, BridgeHints, feature sets, UTS proposals), and which policies/specs constrain the mapping (policy refs + optional `PlaneMapRef` / `ScaleEmbeddingSpecRef`).
3. **Produce FPF‑native inputs.** Use the alignment recipe outputs as inputs to:

   * `G.2` harvesting (ClaimSheets / operator & object inventories / candidate bridge hints),
   * `G.3` CHR typing (when numeric signals are formalized as CHR characteristics/scales/coordinates),
   * `G.4` acceptance/threshold policies (when a downstream decision requires explicit CAL policy rather than telemetry),
   * `G.12` dashboards (when derived SoS features are used as DHC slots).
4. **Feed selection/parity/shipping without smuggling semantics.**

   * `G.5` consumes the produced artefacts under its own contract surfaces and returns set‑valued outcomes (selector semantics remain owned by `G.5` + `G.Core`).
   * `G.9` parity consumes pinned editions/windows and produces traceable parity reports.
   * `G.10` shipping may include interop surfaces **as cited artefacts**; `G.13` does not own shipping.
5. **Emit telemetry and refresh causes.** Any change in external editions, alignment policies, plane maps, or embedding specs emits:

   * a canonical `RSCRTriggerKindId` (per `G.Core`),
   * a scope (`PathSliceId[]` and/or `PatternScopeId`),
   * payload pins (editions/policies/UTS rows),
     enabling `G.11` to plan slice‑scoped refresh.

#### G.13:4.4 - Interfaces — minimal I/O standard (conceptual; kit‑only)

| ID   | Interface   | Consumes  | Produces   |
| ---- | ----------- | --------- | ---------- |
| **G.13‑1 `Register_ExternalIndex`**  | Register `ExternalIndexCard@Context` | Provider metadata, scope, **ExternalEdition**, freshness, describedEntity anchor   | `ExternalIndexCard@Context` (+ UTS row when published)   |
| **G.13‑2 `Map_ClaimsToFPF`**   | Apply `ClaimMapperCard@Context`   | `ExternalIndexCard@Context`, `MappingPolicyRef`, optional `PlaneMapRef`/`ScaleEmbeddingSpecRef`, optional EvidenceGraph hooks | `ClaimSheet@Context`, `BridgeHints`, optional `SoSFeatureSet@Context`, optional UTS proposals |
| **G.13‑3 `Derive_SoSFeatures`**  | Produce CHR‑typed SoS features  | ClaimSheets / external signals refs, CHR typing refs, legality proof hooks | `SoSFeatureSet@Context` (CHR‑typed; provenance pinned)   |
| **G.13‑4 `Publish_InteropSurface`**  | Publish interop summary | outputs of G.13‑2/‑3, UTS refs | `InteropSurface@Context` (+ UTS rows/twins) |
| **G.13‑5 `Emit_IndexTelemetryPin`** | Emit refresh input  | edition/policy changes + scope + payload pins  | telemetry to `G.11` (typed causes + payload pins)   |
| **G.13‑6 `Wire_To_SoTA_Pack`** | Provide shipping hook  | `InteropSurface@Context` + citations to upstream artefacts  | `G.10` pack hooks (as cited payload; no serialisation mandated)  |

### G.13:5 - Extensions (pattern‑scoped; non‑core)

`G.13` keeps provider/method specifics out of the kit core. Any such specificity appears as `GPatternExtension` blocks with stable **PatternScopeId**s. These modules are **wiring‑only**: they bind pins/editions/policies and cite the semantic owner rather than redefining semantics.

#### G.13:5.1 - `G.13:Ext.ExternalIndexProviderWiring` *(Phase‑3 seed)*

**PatternScopeId:** `G.13:Ext.ExternalIndexProviderWiring`
**GPatternExtensionId:** `ExternalIndexProviderWiring`
**GPatternExtensionKind:** `Phase3Seed`
**SemanticOwnerPatternId:** `owner TBD` *(Annex/Interop or a future dedicated interop owner)*
**Uses:** `{G.13}`
**⊑/⊑⁺:** `∅`
**RequiredPins/EditionPins/PolicyPins (minimum):**

* `ExternalIndexType`
* `ExternalEdition` *(as published on `ExternalIndexCard@Context`)*
* `Licence?`
* `CoverageScope`
* `ProviderChangePolicyId?` *(if provider‑specific “schema drift” handling exists)*

**RSCRTriggerSetIds / RSCRTriggerKindIds:** `∅` *(covered by `G.13:4.1`)*
**Notes (seed; wiring‑only):**

* Provider‑specific ingestion choices (e.g., OpenAlex‑class, Crossref‑class, ORKG‑class, discipline repositories) **must not** become Part‑G‑wide norms in Phase‑2. This module only records which provider cards exist and which editions/policies are pinned.

#### G.13:5.2 - `G.13:Ext.EmbeddingBasedAlignment` *(Phase‑3 seed; method‑specific wiring stub)*

**PatternScopeId:** `G.13:Ext.EmbeddingBasedAlignment`
**GPatternExtensionId:** `EmbeddingBasedAlignment`
**GPatternExtensionKind:** `Phase3Seed`
**SemanticOwnerPatternId:** `owner TBD` *(Annex/Interop or a future dedicated interop owner; Phase‑3 owner decision required)*
**Uses:** `{G.13, A.19, E.5.2}`
**⊑/⊑⁺:** `∅`
**RequiredPins/EditionPins/PolicyPins (minimum):**

* `ScaleEmbeddingSpecRef.edition`
* `NormalizationMethodRef.edition?` *(when a declared normalization/representation transform is used)*
* `MappingPolicyRef`
* `EvidenceGraphId?` *(when evidence paths for alignment decisions are published)*

**RSCRTriggerSetIds / RSCRTriggerKindIds:** `∅` *(covered by `G.13:4.1`)*
**Notes (wiring‑only; post‑2015 practice orientation):**

* “Embedding‑based” techniques are treated as **declared transforms** constrained by `ScaleEmbeddingSpec` and/or `NormalizationMethod` references, rather than as implicit semantics.
* The module binds editions and policies; it does not define what is “similar enough”.

#### G.13:5.3 - `G.13:Ext.EntityResolutionAndAliasDocking` *(interop‑specific; Phase‑3 seed)*

**PatternScopeId:** `G.13:Ext.EntityResolutionAndAliasDocking`
**GPatternExtensionId:** `EntityResolutionAndAliasDocking`
**GPatternExtensionKind:** `Phase3Seed`
**SemanticOwnerPatternId:** `owner TBD` *(likely UTS‑adjacent; requires Phase‑3 owner decision)*
**Uses:** `{F.17, E.10}`
**⊑/⊑⁺:** `∅`
**RequiredPins/EditionPins/PolicyPins (minimum):**

* `UTSRowId[]` *(for externally‑sourced entities that become publicly citable)*
* `ExternalIdAliasSetId?` *(labels only; canonical ids remain UTS ids)*
* `TokenizationPolicyId?`

**RSCRTriggerSetIds / RSCRTriggerKindIds:** `∅` *(covered by `G.13:4.1`)*
**Notes (seed; wiring‑only):**

* This module exists to prevent “ID drift by renaming” for externally sourced entities. It is intentionally a Phase‑3 seed until a single semantic owner is chosen.

### G.13:6 - Archetypal grounding (informative; SoTA‑oriented)

**System.** *Software architecture portfolio design.*
Register an external scholarly index edition for “software architecture” concept neighborhoods. Align extracted technique/tactic claims into ClaimSheets and derive a CHR‑typed feature set (e.g., evidence depth, maturity). Use `G.5` to select a **set** of tactics under multi‑objective tradeoffs, and ship a SoTA pack that cites the interop surface.

**Episteme.** *Science‑of‑science discipline dashboard.*
Align external claim graphs (replication, standardisation, disruption‑style proxies) into CHR‑typed features for DHC series. Publish a dashboard slice that cites the external edition and alignment policy; refresh triggers fire when the external edition updates.

**OEE/QD.** *Open‑ended environment generation.*
Register external environment/task taxonomies as index cards. Align them into generator‑family registries (as cited artefacts), keeping coverage/regret strictly as telemetry inputs. Use refresh to re‑align when the taxonomy edition changes.

### G.13:7 - Bias‑Annotation (informative)

* **Vendor/tool bias.** The kit names conceptual surfaces only; it avoids vendor‑specific file formats or tooling claims.
* **Metric‑authority bias.** External indicators are treated as *inputs* that must be typed, pinned, and evidenced; they are not authority by default.
* **Representation bias.** Representation/embedding choices are forced into explicit `Spec` + edition pins (no hidden semantics).
* **Discipline bias.** Interop supports pluralism by preserving explicit crossings and versioned alignments instead of forcing a single canonical external ontology.

### G.13:8 - Conformance Checklist (CC‑G13; applies when G.13 surfaces are used)

1. **CC‑G13‑CoreRef.** *(normative)* `G.13` implementations **MUST** satisfy the *effective* `G.Core` obligations declared by `G.13:4.1` (`GCoreLinkageManifest`), including trigger typing, default‑ownership routing, and crossing‑visibility pin discipline.

2. **CC‑G13‑InteropIsNotAContractSurface.** *(delegated)* Interop surfaces **MUST NOT** introduce shadow legality/comparability gates; they cite `CN‑Spec`/`CG‑Spec`/CHR/CAL owners and publish pins instead.
   → delegate to `CC‑GCORE‑CN‑CG‑1`.

3. **CC‑G13‑CrossingsAreExplicitWhenInteropTouchesPlanesOrContexts.** *(delegated)* Any cross‑plane/context reuse implied by alignment **MUST** be made explicit through the crossing visibility discipline.
   → delegate to `CC‑GCORE‑CROSS‑1`.

4. **CC‑G13‑PlanePenaltyPoliciesAreOwneredAndPinned.** *(local; owner‑citing)* If `PlaneMapRef` is used (or alignment implies plane‑level penalties), interop surfaces **MUST** publish the relevant policy‑id pins via the crossing‑visibility discipline, and any such policies **MUST** satisfy the constraints owned by `CG‑Spec` (cite `CC‑G0‑Φ`). Interop surfaces **MUST NOT** define interop‑local penalty functions.

5. **CC‑G13‑SetReturnPreserved.** *(delegated)* Interop **MUST NOT** introduce hidden scalarisation or forced single‑winner selection.
   → delegate to `CC‑GCORE‑SET‑1`.

6. **CC‑G13‑DefaultClaimsAreCitationsOnly.** *(delegated)* Any mention of defaults (e.g., dominance regime, portfolio mode) is a **citation** to the single owner in `G.Core.DefaultOwnershipIndex`, not a local default statement.
   → delegate to `CC‑GCORE‑DEF‑1`.

7. **CC‑G13‑EditionDisciplineForInteropCards.** *(local)* `ExternalIndexCard@Context` and `ClaimMapperCard@Context` **MUST** expose edition pins (`ExternalIndexRef.edition`, `ClaimMapperRef.edition`). Any interop surface published to UTS **MUST** cite the relevant `…Ref.edition` values (incl. `PlaneMapRef.edition?`, `ScaleEmbeddingSpecRef.edition?`) when present.
   FPF edition keys **MUST** appear only on `…Ref.edition` pins when a reference is present. Provider snapshot labels (e.g., `ExternalEdition` on `ExternalIndexCard@Context`) may exist on the source card, but **MUST NOT** be copied into downstream artefacts as free‑floating “edition fields”; downstream artefacts cite the corresponding `…Ref.edition` pins instead.
   In particular, interop transforms **MUST NOT** perform illicit arithmetic on ordinal/compare‑only scales (e.g., averaging or subtraction); any aggregation must be via lawful CAL operators with explicit scale legality (cite `A.18` / `CC‑G0‑CSLC`).

8. **CC‑G13‑SoSFeaturesAreCHRTypedAndLegal.** *(local; owner‑citing)* If `SoSFeatureTransform@Context` is used, produced SoS features **MUST** be CHR‑typed via `FeatureTypingRefs{CharacteristicId/ScaleId/CoordinateId}` (owner: `G.3`) and any legality/units obligations must be satisfied via CSLC/CG owners (cite `A.18` / `G.0` / `G.4`; do not invent interop‑local legality gates).

9. **CC‑G13‑TelemetryEmitsCanonicalTriggerKinds.** *(delegated)* Interop‑driven changes (external edition bumps, mapping policy changes, plane‑map edits, embedding‑spec edits) **MUST** emit canonical `RSCRTriggerKindId` causes with explicit scope and payload pins.
   → delegate to `CC‑GCORE‑TRIG‑1`, `CC‑GCORE‑TRIG‑2`, `CC‑GCORE‑TRIG‑3`, `CC‑GCORE‑TRIG‑4`.

10. **CC‑G13‑IDContinuityForExternallySourcedIdentifiers.** *(delegated)* Interop publication **MUST** follow Δ‑discipline: no “renaming by meaning”; use aliases/deprecations as required.
   → delegate to `CC‑GCORE‑ID‑1`, `CC‑GCORE‑ID‑2`.

11. **CC‑G13‑NotationIndependence.** *(local)* Conformance is judged on the conceptual objects in `G.13:4.2`. Any serialisation is non‑normative and must not redefine semantics.
   *(Cites `E.5.2` for notation independence.)*

### G.13:9 - Common Anti‑Patterns and How to Avoid Them

* **Anti‑pattern: “Format == spec”.** Treating an export schema (KG dump, JSON, RO‑Crate, etc.) as the normative definition.
  **Remedy:** Keep `ExternalIndexCard` / `ClaimMapperCard` / `InteropSurface` as the conceptual contract; treat serialisation as an appendix/tooling concern.

* **Anti‑pattern: Hidden scale invention.** An embedding similarity becomes a “score” without explicit typing/binding.
  **Remedy:** Require `ScaleEmbeddingSpecRef` + edition pins and bind any derived features through CHR/CAL owners.

* **Anti‑pattern: Implicit plane/context reuse.** Reusing external concept graphs across contexts without explicit crossing pins.
  **Remedy:** Publish crossing visibility pins and route through bridge/plane owners; never fuse contexts “inside the aligner”.

* **Anti‑pattern: Edition‑free dashboards.** Feeding externally derived rows into dashboards without pinned editions/policies.
  **Remedy:** Pin `ExternalIndexRef.edition` and `ClaimMapperRef.edition`; emit RSCR triggers on changes.

* **Anti‑pattern: Interop asserts defaults.** “Interop decides dominance regime / portfolio mode.”
  **Remedy:** Treat defaults as citations only (single owner in `G.Core.DefaultOwnershipIndex`).

### G.13:10 - Consequences

* **Interop becomes refresh‑ready.** External source drift produces typed RSCR causes with scopes/payload pins; refresh becomes slice‑scoped rather than global guesswork.
* **Generation‑first authoring becomes cheaper.** External sources become controlled inputs into SoTA synthesis and portfolio exploration, not ad‑hoc audit decoration.
* **Conceptual hygiene improves.** Explicit cards + edition pins reduce semantic leakage from tools/formats/providers.
* **Cross‑tradition reuse becomes auditable.** Plane/context reuse is surfaced as crossings rather than embedded assumptions.

### G.13:11 - Rationale

FPF is a conceptual framework for disciplined creative work, not a data governance system. External scholarly infrastructure is valuable precisely because it provides fast, wide coverage—but without an explicit interop kit, that value is purchased by silently importing semantics (implicit comparisons, unpinned editions, hidden transformations).

`G.13` resolves the tension by turning “interop” into **first‑class conceptual wiring**: cards/surfaces that pin editions, cite owners, expose provenance hooks, and produce typed refresh causes, while leaving domain/tool specifics in `Extensions` (or Phase‑3 owners).

### G.13:12 - SoTA‑Echoing (post‑2015, for orientation; non‑normative)

* **Scholarly claim graphs & open indexes.** Open research KGs and open scholarly indexes encourage claim‑level representations and concept taxonomies as interop substrates (post‑2015 ecosystem: KG‑style contribution graphs; open indexing initiatives). Treat these as *sources* registered via `ExternalIndexCard`, not as semantic owners.

* **Neural representations for scientific text.** Transformer‑based scientific encoders (e.g., SciBERT‑class; citation‑aware paper representations such as SPECTER‑class; later retrieval‑oriented scientific embedding families) are useful as *alignment heuristics*. In FPF terms, they belong behind `ScaleEmbeddingSpec` + pinned editions/policies (see `G.13:Ext.EmbeddingBasedAlignment`).

* **Schema matching & entity resolution (deep‑learning era).** Modern matcher families (deep entity matching, contrastive representation alignment, GNN‑assisted graph alignment) help populate interop cards, but must not become “implicit semantics”; record their use as policy‑bound wiring in extensions.

* **Systematic review process modernisation.** PRISMA‑2020‑class workflow records (post‑2015 practice) are valuable as evidence anchors and coverage telemetry; treat them as evidenced inputs (EvidenceGraph anchors + pinned editions/windows), not as legality gates.

* **QD / Illumination and OEE portfolios.** Post‑2015 QD (MAP‑Elites successors, CMA‑ME line, differentiable QD toolkits) and OEE (POET‑class and related environment/method co‑evolution lines) often rely on external taxonomies and environment corpora. Interop should expose those as pinned external editions and keep coverage/regret as telemetry inputs—never as implicit dominance.

### G.13:13 - Relations

**Builds on:** `G.Core`.
**Imports:** `G.2`, `G.3`, `G.4`, `G.5`, `G.6`, `G.7`, `G.9`, `G.10`, `G.11`, `A.19`, `A.18`, `G.0`, `F.17`, `E.5.2`, `E.18`.
**Publishes to:** UTS (twin labels where applicable); refresh inputs to `G.11`; shipping hook surfaces to `G.10` (as cited artefacts).
**Relates to:** `G.12` (dashboards), `G.8` (SoS‑LOG bundle surfaces) when interop‑derived artefacts are consumed there.

### G.13:14 - Author’s quick checklist (informative)

1. Register each external source snapshot as an `ExternalIndexCard@Context` with explicit `ExternalEdition`.
2. Author a `ClaimMapperCard@Context` with explicit `MappingPolicyRef` and required edition pins.
3. If you derive SoS features, declare a `SoSFeatureTransform@Context` and cite CHR typing refs and provenance hooks.
4. Publish an `InteropSurface@Context` that cites all active `…Ref.edition` values and UTS rows.
5. On any external edition or policy change, emit canonical RSCR trigger causes with explicit scope + payload pins.
6. Keep provider/tool specifics in `Extensions` (or Phase‑3 seed) and do not let formats redefine semantics.

### G.13:End

# **Part H – Glossary & Definitional Pattern Index**

| §   | ID & Title                     | Concise reminder                                               |
| --- | ------------------------------ | ---- | -------------------------------------------------------------- |
| H.1 | Alphabetic Glossary            |  Every `U.Type`, relation & operator with four‑register naming. |
| H.2 | Definitional Pattern Catalogue |  One‑page micro‑stubs of every definitional pattern for quick lookup.  |
| H.3 | Cross‑Reference Maps           |  Bidirectional links: Part A ↔ Part C ↔ Part B terms.           |


# **Part I – Annexes & Extended Tutorials**

| §   | ID & Title                  |  Concise reminder                                                |
| --- | --------------------------- | --- | --------------------------------------------------------------- |
| I.1 | Deprecated Aliases          |  Legacy names kept for backward compatibility.                   |
| I.2 | Detailed Walk‑throughs      |  Step‑by‑step modelling of a pump + proof + dev‑ops pipeline.    |
| I.3 | Change‑Log (auto‑generated) |  Version history keyed to DRR ids.                               |
| I.4 | External Standards Mappings |  Trace tables to ISO 15926, BORO, CCO, Constructor‑Theory terms. |


# **Part J – Indexes & Navigation Aids**

| §   | ID & Title               |  Concise reminder                                        |
| --- | ------------------------ | --- | ------------------------------------------------------- |
| J.1 | Concept‑to‑Pattern Index |  Quick jump from idea (“boundary”) to pattern (§, id).   |
| J.2 | Pattern‑to‑Example Index |  Table listing every archetypal grounding vignette.      |
| J.3 | Principle‑Trace Index    |  Maps each Pillar / C‑rule / P‑rule to concrete clauses. |

# **Part K  – Lexical debt**
## Mandatory replacement map for measurement terms

> **Rule:** In all **normative** content (specifications, data schemas, etc.), the deprecated terms **“axis”** and **“dimension”** (and their plural or compound forms) **MUST NOT** be used to denote a measurable aspect. Use **Characteristic** in the Tech register instead. Other colloquial terms should be mapped to canonical terms as listed below. In **Plain** narrative, the legacy words may appear _only on first use_ and only if paired with their canonical equivalent for clarity.

| Legacy Term (context) | **Replace with** (Tech register) | Plain register allowance | Canonical Reference |
| --- | --- | --- | --- |
| axis (of measurement); dimension (of a system or quality) | **(disallowed in Core prose)** → use **Characteristic** | No parenthetical allowance in Core; use **Characteristic / Measure / Coordinate** only | A.17 (CHR-NORM) |
| point (on an axis); data point | **Coordinate** (on a Scale) | “point” _(in explanations only, e.g. “a point on the scale”)_ | A.18 (CSLC-KERNEL) |
| metric value; raw score | **Coordinate** (or **Value**) | “value” _(acceptable in plain usage when context is clear, but formally it’s a Coordinate tied to a Characteristic)_ | A.18, C.16 |
| score (composite or normalized) | **Score** (produced via a **ScoringMethod**) | “score” _(if needed in narrative, ensure it’s explained as a result of a defined ScoringMethod)_ | A.17/A.18 (ScoringMethod/Score) |
| unit dimension; unit axis | **Unit** (of a Scale) | “unit” _(plain usage okay)_ | A.18 (Scale/Unit) |
| metric (as a noun) | **Avoid in Tech and as primitive** → use **`U.DHCMethodRef` / `U.Measure` / Score** | “metric” _(Plain only on first use, with pointer to canonical terms)_ | C.16 § 5.1 (L5), A.18 |

## Migration debt from A.2.6 (Scope, ClaimScope, WorkScope)

### Deprecations (normative)

The following terms **MUST NOT** name scope characteristics in normative text, guards, or conformance blocks:

* *applicability*, *envelope*, *generality*, *capability envelope*, *validity* (as a characteristic name).

Use instead:

* **`U.ClaimScope`** (*Claim scope*, nick **G**) for epistemes;
* **`U.WorkScope`** (*Work scope*) for capabilities;
* **`U.Scope`** only when explaining the abstract mechanism (not in guards).

### Affected locations and required edits (normative)

Editors SHALL apply the following replacements:

1. **Part C.2.2 (F–G–R).**

   * Replace any internal definition of “Generality” with a normative reference to **A.2.6 §6.3** (*Claim scope (G)*).
   * Where “abstraction level” is mentioned as G, replace with “Claim scope (where the claim holds)”; keep **AT** (AbstractionTier) only as optional didactics (non‑G).
   * Ensure composition examples use **intersection/SpanUnion** for G, not ordinal “more/less general”.

2. **Part C.2.3 (Formality F).**

   * No change to F itself.
   * Any example that implies “raising F widens G” MUST be rephrased: F changes expression form; G changes only via **ΔG**.

3. **Part A.2.2 (Capabilities).**

   * Replace “capability envelope/applicability” with **`U.WorkScope`**.
   * Method–Work gates MUST test **Work scope covers JobSlice**, with **measures** and **qualification windows** bound.

4. **Part B (Bridges & CL).**

   * Add a note: **CL penalties apply to R**, not to **F/G**; mapping MAY recommend **narrowing** the mapped scope (best practice).

5. **Part E (Lexicon).**

   * Add entries for **Claim scope (G)**, **Work scope**, **Scope** (mechanism).
   * Mark listed deprecated terms as **legacy aliases** allowed only in explanatory notes.

6. **ESG & Method–Work templates.**

   * Replace any “applicability”/“envelope” guard phrasing with **ScopeCoverage** (see §10).
   * Require explicit **`Γ_time`** selectors in all scope‑sensitive guards.

### Migration playbook (informative)

1. **Inventory** scope‑like phrases across your Context (search: applicability, envelope, generality, capability envelope, valid\*).
2. **Classify** each occurrence as **Claim scope** (episteme) or **Work scope** (capability); replace any “scope characteristic(s)” with “scope type” or “USM scope object” depending on sentence grammar.
3. **Rewrite** guards to use `Scope covers TargetSlice` + explicit **`Γ_time`**; remove “latest”.
4. **Publish** any required **Bridges** with **CL** for Cross‑context usage.
5. **Document** ΔG changes separately from evidence freshness (R).

### Backwards compatibility (informative)

Legacy artifacts MAY keep their historical phrasing in body prose. All **guards, conformance checklists, and state assertions** MUST be rewritten to the USM terms and semantics.

### Change Log (normative migration record)

* **A.2.6 introduced.** Defines `U.ContextSlice`, `U.Scope`, `U.ClaimScope (G)`, `U.WorkScope`; sets algebra and guard patterns.
* **Deprecated labels.** “applicability / envelope / generality / capability envelope / validity” as characteristic names.
* **Edits required.** C.2.2 (G = Claim scope), A.2.2 (Work scope for capabilities), Part B (CL→R note), Part E (Lexicon updates), ESG/Method–Work guard templates (ScopeCoverage + `Γ_time`).
* **No change.** C.2.3 (F) unchanged; its examples updated only for wording consistency.
