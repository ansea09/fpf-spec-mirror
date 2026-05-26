---
chunk_kind: "child"
pattern_id: "G.6"
pattern_title: "Evidence Graph & Provenance Ledger"
section_id: "G.6:4"
section_title: "Solution — EvidenceGraph (notation‑independent; lane‑aware; path‑addressable)"
source_path: "FPF-Spec.md"
output_path: "by_section/G.6/G.6__005_solution-evidencegraph-notation-independent-lane-aware-path-addressable.md"
commit_sha: "ae1ff1c7a231a2ec78d244b40d7805a5538c6608"
heading_path:
  - "G.6 — Evidence Graph & Provenance Ledger"
  - "G.6:4 — Solution — EvidenceGraph (notation‑independent; lane‑aware; path‑addressable)"
line_start: 75379
line_end: 75545
dependencies:
  - "A.10"
  - "A.21"
  - "B.3"
  - "C.18"
  - "C.19"
  - "C.23"
  - "E.10"
  - "E.18"
  - "E.5"
  - "E.5.2"
  - "F.15"
  - "F.17"
  - "F.9"
  - "G.10"
  - "G.11"
  - "G.4"
  - "G.5"
  - "G.7"
  - "G.8"
  - "G.9"
  - "G.Core"
  - "G.Core.TriggerAliasMap.G6"
keywords:
  - "CrossingBundle"
  - "EvidenceGraph"
  - "GateCrossing"
  - "PathId"
  - "PathSliceId"
  - "SCR/RSCR"
  - "TriggerAliasMap"
  - "UTS PathCard"
  - "lane tags (TA/VA/LA)"
  - "provenance"
  - "Γ-fold pinning"
---

### G.6:4 - Solution — EvidenceGraph (notation‑independent; lane‑aware; path‑addressable)

#### G.6:4.1 - G.Core linkage (normative)

**Builds on:** `G.Core` (Part‑G core invariants; citation/delegation hub)

**GCoreLinkageManifest (normative; size‑controlled).**

`GCoreLinkageManifest := ⟨
  CoreConformanceProfileIds := {
    GCoreConformanceProfileId.PartG.AuthoringBase,
    GCoreConformanceProfileId.PartG.UTSWhenPublicIdsMinted
  },
  RSCRTriggerSetIds := { GCoreTriggerSetId.EvidenceGraphKit },
  CorePinSetIds := {
    GCorePinSetId.PartG.AuthoringMinimal,
    GCorePinSetId.PartG.CrossingVisibilityPins
  },
  CorePinsRequired := {
    EvidenceGraphId,
    EvidenceGraphRef.edition?,   // iff editioned as a published artefact
    PathId[]/PathSliceId[],      // strengthened (unconditional for G.6)
    UTSRowId[],                  // strengthened (UTS Name Cards + PathCards are required outputs)
    Γ_timePolicy?,               // iff empirical legs exist (or equivalently: window id carried by PathSliceId)
    ΓFoldRef.edition?,           // iff an explicit Γ-fold artefact is pinned
    CAL.ProofLedgerId[]?         // iff Γ-fold is overridden (cite CAL ProofLedger ids; governed by G.4)
  },
  DefaultsConsumed := { DefaultId.GammaFoldForR_eff },
  TriggerAliasMapRef? := G.Core.TriggerAliasMap.G6
⟩`

**Conditional add‑on (tri‑state guard).** If `G.6` is used to publish or consume guard outcomes (e.g., via `G.6:Ext.SoSLOGPathCitationWiring`), additionally require:
`CoreConformanceProfileIds += { GCoreConformanceProfileId.PartG.TriStateGuard }`.

*(Nil‑elision + expansion rule are per `G.Core:4.2`.)*

#### G.6:4.2 - EvidenceGraph (object; surface governed by the kit)

**Definition (object).** An `EvidenceGraph` is a **typed DAG** whose nodes are resolvable to A.10 anchors/carriers and evidencing roles, and whose edges represent minimal, normative provenance relations suitable for audit and path citation.

* **Nodes.** Each node is an A.10‑anchored evidence carrier or evidence role (e.g., a proof carrier, a measurement record carrier, a tool‑qualification carrier). Nodes MUST remain grounded in A.10 anchors and MUST NOT introduce mereological structure (A.10 firewall).
  * **Node kinds (explicit; stable).** Nodes MUST have an explicit kind tag `nodeKind ∈ {U.EvidenceRole, SymbolCarrier, TransformerRole, MethodDescription, Observation}` (as used in the existing Part‑G vocabulary), so downstream projections can remain notation‑independent and audit‑checkable.
  * **Extension pins.** Method‑family‑specific pins (e.g., QD/OEE) MUST NOT be introduced as new “core node kinds”; they are carried as additional pins only when the relevant `GPatternExtension` is in use and are recorded on UTS PathCards / SCR projections as required by that extension.
* **Edges (minimal normative vocabulary).** The pattern admits a small set of provenance edges sufficient for audit:

  * `verifiedBy` (formal line),
  * `validatedBy` (empirical line),
  * `fromWorkSet` (run‑time trace provenance),
  * `happenedBefore` (temporal ordering),
  * `derivedFrom` (controlled derivation).
  * *(Informative only)* `usedCarrier`, `interpretedBy` MAY appear as authoring aids, but MUST NOT be relied on for conformance checks (their semantics remain non‑normative in G.6).
    Additional narrative edges MAY exist as informative annotations but MUST NOT be relied on for conformance checks.
* **Lane tags.** Every binding on a path is lane‑typed with `assuranceUse ∈ {TA, VA, LA}` (lane separation remains explicit through to SCR projections; no silent cross‑lane averaging).
* **Externality (no self‑evidence).** Any evidencing `TransformerRole` that would certify the evaluated holon MUST be modelled as external (or model a meta‑holon explicitly); G.6 does not permit reflexive “self‑evidence” shortcuts.
* **Context and plane attachment.** Nodes and claims carry `BoundedContext` and `ReferencePlane`. Any movement across context/kind/plane/design↔run/edition boundaries is represented via explicit GateCrossing/CrossingBundle artefacts (with crossing pins routed per `G.Core`).

#### G.6:4.3 - PathId and PathSliceId (citable justification addresses)

**PathId (address for justifications).** A `PathId` is a stable identifier minted for a **claim‑local, lane‑typed** path in an `EvidenceGraph` under a declared scope slice (including a time selector where applicable) and a declared `ReferencePlane`. A `PathId` is meant to be citable from downstream artefacts (LOG, UTS, parity, shipping) without duplicating evidence tables.

A `PathId` citation surface SHALL include, at minimum:

* the lane split (TA/VA/LA) for the path,
* the explicit crossing pins (when crossings are traversed),
* the freshness/time attachment status for empirical legs (when present), including any explicit `validUntil`/expiry marker when one is declared (or a decay/freshness policy pin that implies expiry),
* the pinned policy identifiers relevant to the path’s penalty/trust wiring (policy ids are cited; policies remain governed elsewhere),
* the effective crossing‑trust “bottleneck” information when crossings exist (e.g., lowest `CL`/`CL^k`/`CL^plane` encountered on the cited slice),
* the effective `Γ‑fold` in force for any published/relied‑upon `R_eff` projection (default or explicit override), and (when overridden) the cited CAL `ProofLedger` ids that justify the override,
* the `EvidenceGraphId` and enough addressability to resolve the path to SCR/RSCR anchors.

**PathSliceId (time‑ & plane‑lifted snapshot).** A `PathSliceId` denotes a **release‑quality snapshot key** for a path under explicit time/plane binding (e.g., window policy + `ReferencePlane`) and is intended as the address used when refresh/RSCR wants *path‑granular* recomputation.

*The universal definition of “what kinds of changes force refresh” is governed by `G.Core` (typed trigger kinds). G.6 only makes the slice addressable and pin‑complete.*

When downstream methods require additional edition/policy pins for reproducibility (e.g., archive/illumination/QD surfaces), such pins are specified by the relevant `GPatternExtension` module(s) and are treated as *required pins when that extension is used*.

#### G.6:4.4 - Assurance and legality binding (delegation‑first; no shadow specs)

G.6 does not redefine B.3 or legality rules; it binds evidence paths to existing governing definitions:

* **Assurance skeleton.** Lane separation and the `F/G/R` skeleton are as per B.3. Any statement about penalty routing or default Γ‑fold is delegated to `G.Core` and the Default Governing Definition Index (do not restate).
* **CAL linkage.** When a path claims a proof obligation or an override (e.g., an explicit Γ‑fold override), it MUST cite the relevant CAL `ProofLedger` / `EvidenceProfiles` artefacts (G.4) rather than inventing local semantics.
* **Legality binding.** If a path includes numeric comparisons/aggregations, the legality surface MUST be *cited* via `CG‑Spec` (G.0) rather than re‑implemented in G.6 prose.

#### G.6:4.5 - Conceptual interface (notation‑independent surface; informative shapes)

These are conceptual shapes, not tool APIs (E.5 discipline).

* `Explain(pathId | pathSliceId)` → returns a citation‑ready explanation bundle: lane split, relevant pins (crossings/policies/editions), freshness binding, and links to contributing anchors (A.10) and any CAL evidence/profile refs.
* `PathsFor(claim, scopeSlice, referencePlane)` → enumerates admissible paths, returning `PathId[]` with enough metadata to support selection/audit queries.
* `Snapshot(pathId | pathSliceId)` → emits a release‑grade snapshot record (SCR/RSCR‑grade) whose keys are citable and whose pins are explicit.

#### G.6:4.6 - Extensions (pattern‑scoped; non‑core)

All blocks below are `GPatternExtension` modules (PatternScopeId‑scoped, **not** new PatternIds). They store wiring only and cite governing patterns.

**GPatternExtension: LegacyTriggerAliases**

* **PatternScopeId:** `G.6:Ext.LegacyTriggerAliases`
* **GPatternExtensionId:** `LegacyTriggerAliases`
* **GPatternExtensionKind:** `InteropSpecific`
* **GoverningPatternId:** `G.Core`
* **Uses:** `{G.Core}` *(cites `G.Core.TriggerAliasMap.G6`; does not redefine meanings)*
* **⊑/⊑⁺:** `∅`
* **RequiredPins/EditionPins/PolicyPins (minimum):**

  * `RSCRTriggerKindId` (canonical id recorded)
  * `RSCRTriggerAliasId?` *(e.g., deprecated human labels such as `G.6:H3:...` recorded as labels only)*
  * `scope: PathSliceId[] | PathId[] | PatternScopeId`
  * `TriggerAliasMapRef := G.Core.TriggerAliasMap.G6` *(docking reference)*
* **RSCRTriggerKindIds:** `{RSCRTriggerKindId.EvidenceSurfaceEdit, RSCRTriggerKindId.CrossingBundleEdit, RSCRTriggerKindId.PenaltyPolicyEdit, RSCRTriggerKindId.ReferencePlaneEdit, RSCRTriggerKindId.EditionPinChange, RSCRTriggerKindId.PolicyPinChange}`
* **Notes (wiring‑only):** This module preserves ergonomics/back‑compat by allowing `G.6:H3:*` labels, while requiring that recorded causes use canonical `RSCRTriggerKindId` (per `CC‑GCORE‑TRIG‑3`).

**GPatternExtension: SoSLOGPathCitationWiring**

* **PatternScopeId:** `G.6:Ext.SoSLOGPathCitationWiring`
* **GPatternExtensionId:** `SoSLOGPathCitationWiring`
* **GPatternExtensionKind:** `InteropSpecific`
* **GoverningPatternId:** `C.23`
* **Uses:** `{C.23, C.19, G.5, G.11}` *(SoS‑LOG decisions cite paths; optional lens/attribution wiring is governed by C.19; refresh consumes triggers)*
* **⊑/⊑⁺:** `∅`
* **RequiredPins/EditionPins/PolicyPins (minimum):**

  * `SoSLogRuleId[]` / `BranchId[]` *(as cited labels; semantics governed by C.23)*
  * `FailureBehaviorPolicyId` *(when `degrade(mode=...)` is used)*
  * `PathId[] | PathSliceId[]` (the cited justification addresses)
  * `LensId?` *(when a C.19 lens is used for attribution/explainability; id only; semantics governed by C.19)*
* **RSCRTriggerKindIds:** `{RSCRTriggerKindId.EvidenceSurfaceEdit, RSCRTriggerKindId.MaturityRungChange, RSCRTriggerKindId.TelemetryDelta, RSCRTriggerKindId.PolicyPinChange}`
* **Notes (wiring‑only):** G.6 does not define LOG semantics; it defines the *path‑citation surface* that LOG must cite.

**GPatternExtension: BridgeSentinelWiring**

* **PatternScopeId:** `G.6:Ext.BridgeSentinelWiring`
* **GPatternExtensionId:** `BridgeSentinelWiring`
* **GPatternExtensionKind:** `InteropSpecific`
* **GoverningPatternId:** `G.7`
* **Uses:** `{G.7, G.11}` *(bridge/sentinel semantics and calibration records are governed by G.7; refresh orchestration is governed by G.11)*
* **⊑/⊑⁺:** `∅`
* **RequiredPins/EditionPins/PolicyPins (minimum; conditional on use):**

  * `BridgeId/BridgeCardId`
  * `RegressionSetId?` / `SentinelId[]?` *(as published by G.7, when sentinel wiring is used)*
  * `PathId[] | PathSliceId[]` *(paths that cite the bridge and must be re‑audited on bridge/sentinel changes)*
* **RSCRTriggerKindIds:** `{RSCRTriggerKindId.CrossingBundleEdit, RSCRTriggerKindId.PenaltyPolicyEdit, RSCRTriggerKindId.FreshnessOrDecayEvent, RSCRTriggerKindId.EditionPinChange, RSCRTriggerKindId.PolicyPinChange}`
* **Notes (wiring‑only):** This module requires that bridge/sentinel changes re‑trigger RSCR **path‑locally** for affected `PathId/PathSliceId` scopes, without redefining sentinel semantics (governed by G.7) and without inventing new trigger kinds (governed by `G.Core`).

**GPatternExtension: QD_OEE_TelemetryPins**

* **PatternScopeId:** `G.6:Ext.QD_OEE_TelemetryPins`
* **GPatternExtensionId:** `QD_OEE_TelemetryPins`
* **GPatternExtensionKind:** `MethodSpecific`
* **GoverningPatternId:** `C.18` *(QD artefact semantics); uses `C.19` for exploration/logging/lens wiring as needed*
* **Uses:** `{C.18, C.19}`
* **⊑/⊑⁺:** `∅`
* **RequiredPins/EditionPins/PolicyPins (minimum; conditional on use):**

  * `DescriptorMapRef.edition`
  * `DistanceDefRef.edition`
  * `InsertionPolicyRef` *(policy id or pinned policy ref, per governing definition semantics)*
  * `EmitterPolicyRef?`
  * `LensId?` *(when a C.19 lens is used in selection/telemetry attribution)*
  * `TransferRulesRef.edition?` / `EnvironmentValidityRegionRef?` *(when open‑ended / transfer events are in scope)*
* **RSCRTriggerKindIds:** `{RSCRTriggerKindId.TelemetryDelta, RSCRTriggerKindId.EditionPinChange, RSCRTriggerKindId.PolicyPinChange, RSCRTriggerKindId.FreshnessOrDecayEvent}`
* **Notes (wiring‑only):** This module enforces reproducibility of archive/illumination and open‑ended telemetry *when those surfaces are used*, without pulling QD/OEE semantics into the EvidenceGraph core.

---

