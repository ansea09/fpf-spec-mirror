---
chunk_kind: "child"
pattern_id: "G.4"
pattern_title: "CAL Authoring for a CG-Frame: Operators, Acceptance Clauses, Evidence Wiring"
section_id: "G.4:4"
section_title: "Solution — CAL authoring kit and publication surface"
source_path: "FPF-Spec.md"
output_path: "by_section/G.4/G.4__005_solution-cal-authoring-kit-and-publication-surface.md"
commit_sha: "3d19010169827708d0bca36d0551af8323908640"
heading_path:
  - "G.4 — CAL Authoring for a CG-Frame: Operators, Acceptance Clauses, Evidence Wiring"
  - "G.4:4 — Solution — CAL authoring kit and publication surface"
line_start: 78493
line_end: 78792
dependencies:
  - "A.10"
  - "A.18"
  - "A.19"
  - "A.21"
  - "B.3"
  - "C.18"
  - "C.19"
  - "C.23"
  - "E.17"
  - "E.18"
  - "E.8"
  - "F.17"
  - "F.9"
  - "G.0"
  - "G.1"
  - "G.10"
  - "G.11"
  - "G.2"
  - "G.3"
  - "G.4"
  - "G.5"
  - "G.6"
  - "G.8"
  - "G.9"
  - "G.Core"
keywords:
  - "CAL authoring"
  - "RSCRTriggerKindId"
  - "acceptance clauses"
  - "edition pins"
  - "evidence profiles"
  - "legality gates"
  - "operators"
  - "tri-state admissibility"
  - "Γ-fold hooks"
  - "Φ/Ψ/Φ_plane policy pins"
---

### G.4:4 - Solution — CAL authoring kit and publication surface

#### G.4:4.1 - G.Core linkage (normative)

**Builds on:** `G.Core` (Part‑G core invariants; citation/delegation hub)

**GCoreLinkageManifest (normative).** Canonical shape, Nil‑elision, and the Expansion rule are defined in `G.Core`.

`GCoreLinkageManifest := ⟨
CoreConformanceProfileIds := {
GCoreConformanceProfileId.PartG.AuthoringBase,
GCoreConformanceProfileId.PartG.TriStateGuard,
GCoreConformanceProfileId.PartG.UTSWhenPublicIdsMinted,
GCoreConformanceProfileId.PartG.ShippingBoundary
},

CorePinSetIds := {
GCorePinSetId.PartG.AuthoringMinimal,
GCorePinSetId.PartG.CrossingVisibilityPins
},

CorePinsRequired := {
UTSRowId[],                 // CAL artefacts are public ids (Name Cards plus public-id continuity notes)
ΓFoldRef.edition?            // only when an explicit Γ‑fold override is pinned (otherwise use DefaultId)
},

// consumed iff no explicit `ΓFoldRef.edition` override is pinned
DefaultsConsumed := { DefaultId.GammaFoldForR_eff },

RSCRTriggerSetIds := { GCoreTriggerSetId.SoTAHarvestSynthesis },
RSCRTriggerKindIds := {      // deltas (Expansion rule applies)
  RSCRTriggerKindId.PenaltyPolicyEdit,
  RSCRTriggerKindId.DefaultGoverningDefinitionChange,
  RSCRTriggerKindId.BaselineBindingEdit
}
⟩`

By the `G.Core` Expansion rule, the effective conformance ids / trigger kinds / pin obligations for `G.4` are the expansions of the referenced profiles/sets/pin‑sets plus the explicit deltas above.

Notes (normative intent, delegated semantics):

* The semantics of tri‑state outcomes, penalty routing, set‑return discipline, crossing visibility, P2W split, typed RSCR causes, and the Default Governing Definition Index are governed in `G.Core` and are not redefined here.
* EvidenceGraph/Path pins (when used) are declared only via **`G.4:Ext.EvidenceGraphWiring`** in **G.4:4.5** (so `G.Core linkage` stays minimal and does not “pull in” `G.6` by default).
* Method‑specific pins (e.g., QD descriptor/distance/insert policy pins; open‑ended transfer rules pins) MUST appear only in **Extensions** blocks (see **G.4:4.5**) and MUST NOT introduce competing defaults.

#### G.4:4.2 - `CAL Pack@CG-Frame` surface (kit governed by this pattern)

`CAL Pack@CG-Frame` is the CG‑Frame’s published CAL Pack. Minimally, it provides:

* `CAL.Charter@Context` — scope anchor for this CAL pack:

  * cites `CG-FrameContext`, `entityOfConcern`, `ReferencePlane`,
  * cites the governance card and legality gate (`CNSpecRef`, `CGSpecRef`) by edition pins,
  * records the “assumption envelope” that acceptance predicates rely on (without minting a new governance card or legality gate).
  * emits `TaskMap@Context` (`TaskMap`) as the canonical handoff record to `G.5` (task→gates/flows/evidence pins).
* `CAL.Operator[]` — typed operator cards (UTS‑published):

  * explicit signature over CHR types,
  * explicit preconditions/postconditions (incl. legality guard macros references),
  * explicit provenance/evidence hooks (by ids/pins, not by tool behavior).
* `CAL.Acceptance[]` — typed predicates with Context‑local thresholds:

  * binds to CHR characteristic ids (and, when inducing numeric comparison/aggregation, to `CG‑Spec.characteristic` ids),
  * exposes unknown handling and failure behavior via policy pins.
* `CAL.Flow[]` — legality‑checked compositions of operator cards:

  * declares result kind (scalar only when lawful; selected-set / set-result when partial orders remain partial orders),
  * records which acceptance clauses gate which flows.
* `CAL.EvidenceProfiles` — evidence wiring surface:

  * lane tags (`F/G/R`) / provenance anchors / policy pins needed for `SCR` and audit surfaces,
  * explicit freshness/decay hooks (freshness window + decay/Γ_time selectors) as pinned policies/refs (not prose).
  * explicit `ReferencePlane` + penalty routing policy ids (`Φ(CL)`, `Ψ(CL^k)`, `Φ_plane`) as citable pins; any such policy family is justified in `CAL.ProofLedger` (monotone + bounded).
* **Optional** `CAL.NQD[]` — QD/OEE‑related calculus surfaces when declared:

  * descriptor/distance/insertion artifacts are pinned by ids/editions,
  * semantics are governed by method‑specific governing definitions (e.g., `C.18`, `C.19`) and not redefined by CAL.
* `CAL.ProofLedger` — a proof/justification ledger:

  * links legality, monotonicity, boundedness, and other soundness obligations to operator/flow/clause ids.
* Publication artifacts:

  * UTS Name Cards (twin labels) for all public ids,
  * RSCR tests ids and Worked‑Examples ids,
  * deprecation notices and edition bump notes as public-id continuity records.

Boundary discipline (normative):

* **No shadow specs**: CAL artefacts cite `CN‑Spec`/`CG‑Spec` and do not introduce competing “local specs” (delegated; see `CC‑GCORE‑CN‑CG‑1` via **CC‑G4‑CoreRef**).
* **No shipping governance:** CAL does not govern shipping; see `CC-GCORE-SKP-1` via **CC-G4-CoreRef**.
* **No refresh governing-definition assignment**: CAL does not govern refresh orchestration; it only publishes pins/payload for refresh (governing definition: `G.11`).

**Minimal schema fragments (notation‑independent; fields for citation, not an implementation schema):**

```
CAL.Pack@CG-Frame :=
 ⟨ calPackId, charterId, taskMapId, operatorIds[], acceptanceClauseIds[], flowIds[],
 evidenceProfileIds[], proofLedgerId, nqdIds[]?,
    utsRowIds[], workedExampleIds[], rscrTestIds[], publicIdContinuityNoteIds[] ⟩

CAL.Operator :=
  ⟨ operatorId(UTS), signature(CHR-typed), preconditions[], postconditions[],
  evidenceProfileRefs[]?, failureBehaviorRef?, crossingRefs[]? ⟩

CAL.Acceptance :=
  ⟨ clauseId(UTS), characteristicRefs[], cgSpecCharacteristicRefs[]?,
    predicateRef, unknownHandlingRef, failureBehaviorRef,
    evidenceProfileRefs[]?, crossingRefs[]? ⟩

CAL.Flow :=
  ⟨ flowId(UTS), dag(operatorIds, edges), gateClauses(acceptanceClauseIds),
    resultKind, decisionAidPolicyRef? ⟩

CAL.EvidenceProfile :=
  ⟨ evidenceProfileId(UTS), lanes(F/G/R), anchors(A.10)[],
    freshnessPolicyPins[]?, penaltyPolicyPins[]?, ΓFoldRef.edition? ⟩
```

#### G.4:4.3 - CAL authoring chassis C1–C9 (kit governed by this pattern)

**C1 — CAL Charter (scope anchor).**
Authors declare a `CAL.Charter@Context` that:

* anchors CAL to the CG‑Frame scope (`CG-FrameContext`, `entityOfConcern`, `ReferencePlane`),
* pins the relevant governance card and legality gate refs (`CNSpecRef.edition`, `CGSpecRef.edition`),
* records the local assumption envelope used by acceptance predicates (as explicit statements to be audited, not as hidden algorithmic assumptions),
* declares which CAL artifacts are intended to be cited downstream (UTS ids).
* emits a `TaskMap@Context` (`TaskMap`) that binds each declared `TaskSignature` (or task family) to:
  * eligible `CAL.FlowId[]` / `CAL.OperatorId[]`,
  * gating `AcceptanceClauseId[]` (ids of `CAL.Acceptance` clauses),
  * required `CAL.EvidenceProfileId[]`,
  * and any required policy pins/edition pins for reproducibility.
  This is the canonical “handoff manifest” consumed by `G.5` (thresholds remain only inside `CAL.Acceptance`).

**C2 — Operator Cards (typed & lawful).**
Each `CAL.Operator` is a UTS‑published, typed unit with:

* `OperatorId (UTS)`,
* `Signature` over CHR types,
* `Preconditions` (including references to CHR guard macros where applicable),
* `Postconditions / invariants`,
* `EvidenceProfileRef[]` (or an explicit “none”),
* `FailureBehaviorRef` (policy‑bound) for safe degradations and non‑catastrophic fallbacks.

**C3 — Acceptance Clauses (typed predicates; thresholds live here).**
Each `CAL.Acceptance` is a UTS‑published predicate with:

* stable `ClauseId (UTS)` for citation,
* explicit `CharacteristicRefs` (CHR ids) used by the predicate,
* `CGSpecRefs?` required iff the clause induces numeric comparison/aggregation,
* `EvidenceProfileRefs?` identifying evidence consulted (so `SCR` can surface the relevant pins),
* explicit **freshness envelope** (freshness window + decay/Γ_time selector refs/pins) when evidence recency is part of admissibility,
* `UnknownHandling` as a tri‑state choice (via `G.Core` semantics),
* `FailureBehaviorRef` (policy‑bound) for degrade/abstain behavior.
* `GateCrossingId[]` / `CrossingBundleId[]` **iff** the clause relies on cross-context, cross-plane, or cross-edition imports (no “silent reuse”).
  Missing required crossing artefacts is a conformance failure and blocks publication of the affected clause/flow (GateCrossing harness: `E.18`/`A.21`/`F.9`/`F.17`/`E.17`; crossing invariants: `G.Core`).

**C4 — Aggregation & comparison flows (safe by construction).**
`CAL.Flow` composes operators into legality‑checked DAGs and declares:

* which acceptance clauses gate the flow,
* which operator outputs are decision‑relevant vs report‑only,
* what the **result kind** is (scalar only where lawful; otherwise selected-set / set-result).
* any thinning/decision‑aid policy (e.g., ε‑front selection) as an explicit policy pin that **does not** silently replace the declared result kind.

**C5 — Evidence wiring surface.**
`CAL.EvidenceProfile` makes evidence hooks explicit:

* provenance anchor references (A.10‑style carriers/anchors, cited by id),
* lane tags (`F/G/R`) for each evidence contribution (no implicit lane mixing; penalties route only to `R_eff` as governed by `G.Core`),
* pinned policy ids for penalty routing and freshness/decay handling (incl. freshness window + decay/Γ_time selector pins; and `Φ(CL)`/`Ψ(CL^k)`/`Φ_plane` policy ids when used),
* declared inputs needed for `SCR` fields at run‑time (without embedding run‑time “gate decisions” into design‑time artifacts).

**C6 — NQD/OEE surface (optional; method‑specific semantics delegated).**
If the CG‑Frame declares QD/OEE‑style regimes, CAL may publish `CAL.NQD[]` as a **surface** that:

* declares descriptor space and distance/insertion artifacts by ids and edition pins,
* records archive/illumination intent and “report‑only vs dominance” gating as explicit policy pins,
* **does not** redefine QD/OEE semantics (those remain governed by method‑specific patterns such as `C.18` / `C.19` and are wired via `Extensions`).

**C7 — ProofLedger (soundness & legality obligations).**
`CAL.ProofLedger` links each operator/flow/clause to:

* legality proof refs (incl. CSLC refs when numeric comparison/aggregation is induced),
* monotonicity/boundedness/stability proof refs for penalty/aggregation policies where relevant,
  * in particular: if an explicit `ΓFoldRef` is pinned (override), ProofLedger includes monotonicity + boundedness/boundary behavior proof refs for that fold.
* explicit statements of degradation conditions (what must happen when assumptions fail).

**C8 — Publication + RSCR + Bridges.**
CAL publication emits:

* UTS entries (Name Cards + twin labels) for all CAL ids,
* Worked‑Examples that exercise legality and acceptance claims,
* RSCR tests ensuring:

  * illegality is detected (e.g., forbidden ordinal arithmetic),
  * guard macro use is coherent,
  * flow legality checks are exercised,
  * acceptance clauses behave as authored on examples.

Any cross-context, cross-plane, or cross-edition import required by CAL publication is handled through GateCrossing/CrossingBundle discipline (as governed by `G.Core`), and CAL publication is blocked if required crossing artifacts are missing.

**C9 — Packaging & refresh readiness (without governing orchestration).**
CAL pack versions:

* record changes as edition‑pinned updates,
* publish deprecation notices and public-id continuity notes for public ids,
* emit RSCR‑relevant trigger payload pins (editions/policies/UTS ids/paths) for refresh orchestration (governing definition: `G.11`).

#### G.4:4.4 - Interfaces (minimal I/O surface)

| Interface                 | Consumes                                            | Produces                                                                                  |
| ------------------------- | --------------------------------------------------- | ----------------------------------------------------------------------------------------- |
| `G.4-1 Charter`           | `CG-FrameContext`, SoTA inputs, `CHR Pack@CG-Frame` | `CAL.Charter@Context` + `TaskMap@Context` (`TaskMap`)  |
| `G.4-2 Operators`         | CHR typing + SoTA operator inventory                | `CAL.Operator[]` (UTS ids; typed signatures; refs to evidence profiles & guards)  |
| `G.4-3 Acceptance`        | Task intent + policy pins + CHR characteristics     | `CAL.Acceptance[]` (typed; thresholds; freshness envelope pins; failure behavior refs)    |
| `G.4-4 Flows`             | Operator cards + admissible aggregators             | `CAL.Flow[]` (legality‑checked compositions; declared result kind)                        |
| `G.4-5 NQD Surface`       | Task intent + policy pins + (optional) QD/OEE inputs | `CAL.NQD[]` (descriptor/distance/insertion refs + edition pins; optional)  |
| `G.4-6 Publish`           | All above + proofs + examples  | Versioned `CAL Pack@CG-Frame`, UTS entries, RSCR tests, Worked‑Examples, public-id continuity notes |

#### G.4:4.5 - Extensions (pattern‑scoped; non‑core)

`G.4` supports method‑family and discipline‑specific calculus variations exclusively via pattern‑scoped extensions.

**GPatternExtension block: `G.4:Ext.EvidenceGraphWiring`**
- **PatternScopeId:** `G.4:Ext.EvidenceGraphWiring`
- **GPatternExtensionId:** `EvidenceGraphWiring`
- **GPatternExtensionKind:** `InteropSpecific`
- **GoverningPatternId:** `G.6`
- **Uses:** `{G.6}`
- **⊑/⊑⁺:** `∅`
- **RequiredPins/EditionPins/PolicyPins (minimum):**
  - `EvidenceGraphId?`
  - `PathId[]/PathSliceId[]`
  - `UTSRowId[]` (for cited artifacts)
- **RSCRTriggerSetIds:** `∅`
- **RSCRTriggerKindIds:** `{RSCRTriggerKindId.EvidenceSurfaceEdit, RSCRTriggerKindId.EditionPinChange, RSCRTriggerKindId.PolicyPinChange}`
- **Notes (wiring‑only):** This block does not define EvidenceGraph semantics; it only fixes that CAL proofs/examples may cite evidence by Path ids.

**GPatternExtension block: `G.4:Ext.NQD`**
- **PatternScopeId:** `G.4:Ext.NQD`
- **GPatternExtensionId:** `NQD`
- **GPatternExtensionKind:** `MethodSpecific`
- **GoverningPatternId:** `C.18`
- **Uses:** `{C.18}`
- **⊑/⊑⁺:** `∅`
- **RequiredPins/EditionPins/PolicyPins (minimum):**
  - `DescriptorMapRef.edition`
  - `DistanceDefRef.edition`
  - `InsertionPolicyRef`
  - `ArchiveRef?`
  - `TaskSignatureRef?` (if activation is TaskSignature‑bound)
- **RSCRTriggerSetIds:** `∅`
- **RSCRTriggerKindIds:** `{RSCRTriggerKindId.EditionPinChange, RSCRTriggerKindId.PolicyPinChange, RSCRTriggerKindId.TelemetryDelta, RSCRTriggerKindId.FreshnessOrDecayEvent}`
- **Notes (wiring‑only):** CAL does not redefine QD semantics; it only pins the descriptor, distance, and insertion records needed for reproducible archive behavior. Any archive/illumination summaries (e.g., coverage / QD‑score / occupancyEntropy / filledCells) are published as report‑only outputs unless an explicit CAL acceptance clause/policy authorizes promotion.

**GPatternExtension block: `G.4:Ext.EELog`**
- **PatternScopeId:** `G.4:Ext.EELog`
- **GPatternExtensionId:** `EELog`
- **GPatternExtensionKind:** `MethodSpecific`
- **GoverningPatternId:** `C.19`
- **Uses:** `{C.19}`
- **⊑/⊑⁺:** `∅`
- **RequiredPins/EditionPins/PolicyPins (minimum):**
  - `ExploreExploitBudgetPolicyRef`
  - `ProbeAccountingRef?`
  - `FailureBehaviorRef?` (if probe/sandbox is policy‑bound)
- **RSCRTriggerSetIds:** `∅`
- **RSCRTriggerKindIds:** `{RSCRTriggerKindId.PolicyPinChange, RSCRTriggerKindId.TelemetryDelta, RSCRTriggerKindId.FreshnessOrDecayEvent}`

**GPatternExtension block: `G.4:Ext.SoSLogBranches`**
- **PatternScopeId:** `G.4:Ext.SoSLogBranches`
- **GPatternExtensionId:** `SoSLogBranches`
- **GPatternExtensionKind:** `MethodSpecific`
- **GoverningPatternId:** `C.23`
- **Uses:** `{C.23}`
- **⊑/⊑⁺:** `∅`
- **RequiredPins/EditionPins/PolicyPins (minimum):**
  - `SoSLogRuleId[]`
  - `SoSLogBranchId[]`
  - `FailureBehaviorPolicyId`
- **RSCRTriggerSetIds:** `∅`
- **RSCRTriggerKindIds:** `{RSCRTriggerKindId.PolicyPinChange, RSCRTriggerKindId.MaturityRungChange, RSCRTriggerKindId.TelemetryDelta}`
- **Notes (wiring‑only):** This block only pins branch/rule ids for degrade/abstain explanation; it does not redefine rule semantics.

**GPatternExtension block: `G.4:Ext.AcceptanceRiskControl`** *(Phase‑3 seed)*
- **PatternScopeId:** `G.4:Ext.AcceptanceRiskControl`
- **GPatternExtensionId:** `AcceptanceRiskControl`
- **GPatternExtensionKind:** `Phase3Seed`
- **GoverningPatternId:** `governing pattern not yet selected`
- **Uses:** `∅`
- **⊑/⊑⁺:** `∅`
- **RequiredPins/EditionPins/PolicyPins (minimum):**
  - `RiskControlPolicyRef`
  - `CalibrationWindowRef?`
  - `CoverageTargetRef?`
- **RSCRTriggerSetIds:** `∅`
- **RSCRTriggerKindIds:** `{RSCRTriggerKindId.PolicyPinChange, RSCRTriggerKindId.TelemetryDelta, RSCRTriggerKindId.FreshnessOrDecayEvent}`
- **Notes (non‑normative seed):** Intended for post‑2015 acceptance families such as conformal risk control / set‑valued selective prediction, distributionally‑robust acceptance envelopes, and calibrated abstention policies; semantics must be governed elsewhere before becoming normative.

