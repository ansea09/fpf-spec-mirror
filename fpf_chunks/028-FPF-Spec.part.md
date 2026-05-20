* **Notes (wiring‑only):** This module wires CHR artefacts to MM‑CHR legality proof obligations; legality semantics are governed by the referenced patterns.

**GPatternExtension: DecayWiring**

* **PatternScopeId:** `G.3:Ext.DecayWiring`
* **GPatternExtensionId:** `DecayWiring`
* **GPatternExtensionKind:** `DisciplineSpecific`
* **GoverningPatternId:** `B.3.4` *(freshness/decay semantics)*
* **Uses:** `{B.3.4, G.6}`
* **⊑/⊑⁺:** `∅`
* **RequiredPins/EditionPins/PolicyPins (minimum):**

  * `FreshnessWindowDeclRef` *(or equivalent window pin, as defined by the governing definition)*
  * `DecayPolicyIdRef?` *(policy-bound; if decay model is referenced by id)*
  * `PathSliceId[]` *(affected evidence carriers / examples that witness drift)*
* **RSCRTriggerKindIds:** `{RSCRTriggerKindId.FreshnessOrDecayEvent, RSCRTriggerKindId.EvidenceSurfaceEdit, RSCRTriggerKindId.PolicyPinChange, RSCRTriggerKindId.BaselineBindingEdit}`
* **Notes (wiring‑only):** CHR does not define decay semantics; it only pins the defined by the governing pattern window/policy and ensures refresh can be triggered on decay events.

**GPatternExtension: QD_OEE_Wiring**

* **PatternScopeId:** `G.3:Ext.QD_OEE_Wiring`
* **GPatternExtensionId:** `QD_OEE_Wiring`
* **GPatternExtensionKind:** `MethodSpecific`
* **GoverningPatternId:** `C.18`
* **Uses:** `{C.18, C.19}`
* **⊑/⊑⁺:** `∅`
* **RequiredPins/EditionPins/PolicyPins (minimum):**

  * `DescriptorMapRef.edition` *(if any Characteristic declares descriptor roles)*
  * `DistanceDefRef.edition` *(if any Characteristic declares distance roles)*
  * `DHCMethodRef.edition` *(if any Characteristic is used as Q / QD-score)*
  * `InsertionPolicyRef?` *(when archive insertion semantics are declared for reproducibility)*
* **RSCRTriggerKindIds:** `{RSCRTriggerKindId.EditionPinChange, RSCRTriggerKindId.PolicyPinChange, RSCRTriggerKindId.TelemetryDelta, RSCRTriggerKindId.FreshnessOrDecayEvent}`
* **Notes (wiring‑only):** QD/OEE semantics are governed by `C.18 and C.19`. CHR only surfaces method‑role declarations
  (via `RoleDecls` or the interop alias `QD.Role`) and the edition/policy pins required for reproducible archive/front interpretation.

### G.3:5 - Archetypal Grounding

**AG‑1 — ML fairness auditing (post‑2015 selective and set‑valued practice).**
*System:* a CG‑Frame for evaluating deployed classifiers across cohorts with explicit abstention/defer behavior.
*CHR authoring:* publish `DemographicParityGap` and `EqualizedOddsGap` as Characteristics with:

* explicit ReferencePlane (deployment population + sampling regime),
* `ObservableOf` (audit protocol + uncertainty model + window),
* interval scale (bounded; zero semantics explicit),
* missingness semantics (cohort sparsity and label noise are typed),
* legality surfaces and guard surfaces that forbid illicit cohort mixing and require explicit proof hooks for aggregation across cohorts.

*Downstream:* CAL acceptance binds thresholds and failure behavior; selector remains set‑returning under partial orders and may treat “defer/abstain” as a first‑class outcome (tri‑state semantics pinned through `G.Core`).

**AG‑2 — Clinical diagnostics (post‑2015 evidence‑aware evaluation).**
*System:* a CG‑Frame for comparing diagnostic pipelines under evolving datasets and protocols.
*CHR authoring:* publish `Sensitivity` and `Specificity` as ratio‑scale, dimensionless Characteristics on `[0,1]`, with:

* explicit `ObservableOf` (trial protocol, inclusion criteria, uncertainty model),
* freshness/decay expectations (protocol drift is modelled as decay),
* legality surfaces that forbid averaging incompatible ordinal labels (e.g., severity grades) and require explicit unit/exposure constraints for any derived rate.

*Downstream:* CAL acceptance governs thresholds and guard‑bands; evidence wiring is cited via Path/PathSlice to make refresh triggers actionable.

**AG‑3 — Quality‑Diversity / Illumination (post‑2015 MAP‑Elites/CMA‑ME lineage).**
*System:* a CG‑Frame where selection returns archives/fronts rather than a single winner.
*CHR authoring:* declare which Characteristics play Q/D/QD‑score roles and pin the metric definitions (descriptor map, distance definition, method editions) so archives are reproducible across runs and refresh can be triggered on edition changes. CHR does not scalarize partial orders; set‑return semantics are pinned through `G.Core`.

### G.3:6 - Bias‑Annotation

CHR authoring is where many biases become “baked in” as measurement choices. Typical risks:

* **Proxy bias:** a convenient observable substitutes for the intended construct. Mitigation: require `ObservableOf` + ReferencePlane + micro‑examples; force explicit “what is being measured” rather than relying on labels.
* **Population and protocol shift:** a characteristic’s meaning changes when the sampling regime or protocol changes. Mitigation: explicit validity windows and freshness/decay expectations; edition pins for protocol definitions; RSCR triggers on freshness/decay events and evidence surface edits.
* **Ordinal misuse bias:** ordinal ratings treated as interval/ratio by convenience. Mitigation: publish scale type + admissible transforms; legality matrix + guard macros; reject coordinate upgrades without proof hooks.
* **Cross‑tradition/cross‑context bias:** imported terms erase local meaning. Mitigation: require explicit imports and loss notes; downstream penalties route to `R_eff` only (pinned through `G.Core`), making loss visible rather than silently altering F/G semantics.
* **Metric gaming bias (QD and evaluation):** changing descriptors/distances changes what “diverse” means. Mitigation: edition‑pin metric definitions and make role declarations explicit (wiring via `C.18 and C.19`).

### G.3:7 - Conformance Checklist (normative)

| ConformanceId     | Statement                                                                                                                                                                                                                             |
| ----------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **CC‑G3‑CoreRef** | `G.3` is conformant only if the applicable `G.Core` obligations declared in `G.3:4.1` are satisfied (effective expansion of profiles/sets + deltas; explicit pins; typed RSCR triggers; defaults with one governing definition).                       |
| CC‑G3‑01          | `CHR Pack@CG‑Frame` is published as a notation‑independent kit payload with the minimum exported objects listed in `G.3:4.2`.                                                                                                         |
| CC‑G3‑02          | Every `CHR.Characteristic` has an explicit declared `Context`, an explicit `ReferencePlane`, and a filled `ObservableOf` field (instrument/protocol + uncertainty model + validity window).                                               |
| CC‑G3‑03          | Every `CHR.Characteristic` declares its `ScaleRef`, `Polarity`, and `UnitSet` (or an explicit “unitless” declaration), plus bounds/zero semantics where applicable.                                                                   |
| CC‑G3‑04          | Missingness is typed in the CHR artefacts such that downstream tri‑state handling is possible without silent coercion. *(Tri‑state semantics are governed by `G.Core`; the typing obligation is CHR‑local.)*                              |
| CC‑G3‑05          | `CHR.Scale` / `CHR.Level` artefacts encode the scale type and admissible transforms, and make illicit arithmetic checkable by downstream consumers.                                                                                   |
| CC‑G3‑06          | Any published `CHR.Coordinate` includes a `CoordinatePolicy` that states preserved invariants and explicit non‑entitlements; coordinates do not silently upgrade measurement structure.                                               |
| CC‑G3‑07          | `CHR.LegalityMatrix` and `CHR.Guards` exist and are referenced by downstream operator authoring; semantics are governed by cited definitions (MM‑CHR and `G.Core`), not duplicated locally.                                                        |
| CC‑G3‑08          | `CHR.AggregationSpecs` are typed and legality‑constrained; where Γ‑fold is required and no explicit override is pinned, cite `DefaultId.GammaFoldForR_eff` through `G.Core.DefaultGoverningDefinitionIndex`. |
| CC‑G3‑09          | If any characteristic is intended for promotion into `CG‑Spec`, the linkage is explicit and edition‑pinned (no shadow ids). *(Governing definition: `G.0`; wiring via `G.3:Ext.CGSpecPromotionWiring`.)*                                             |
| CC‑G3‑10          | UTS Name Cards exist for public ids minted or evolved by the CHR pack (twin labels plus public-id continuity notes). *(Delegation target: `CC‑GCORE‑UTS‑1` via `CC‑G3‑CoreRef`.)*                                                                      |
| CC‑G3‑11          | Worked examples and RSCR tests exist and cite `PathId/PathSliceId`; they cover illegal‑op refusal, unit and scale constraints, polarity invariants, and coordinate non‑entitlements.                                                      |
| CC‑G3‑12          | Thresholds/guard‑bands are not embedded in CHR artefacts; they remain governed by CAL acceptance clauses (`G.4`).                                                                                                                        |
| CC‑G3‑13          | When method‑role declarations are present (via `RoleDecls` and/or `QD.Role` alias), each declaration is **docked** to its governing pattern via a corresponding `G.3:Ext.*` module, and the edition and policy pins required by the governing pattern are surfaced to make downstream interpretation reproducible. *(QD/OEE governing patterns: `C.18` and `C.19`; wiring via `G.3:Ext.QD_OEE_Wiring`.)* |
| CC‑G3‑14          | **Evidence wired.** Each `CHR.Characteristic` links to R‑anchors via `PathId/PathSliceId` (and, where applicable, `A.10` anchor/carrier refs), so downstream evidence discipline (`G.6`) can audit legality and guard claims.            |
| CC‑G3‑15          | An `Archetypal Grounding` section exists with at least two domain‑distinct examples that demonstrate lawful CHR typing/legality and the CHR↔CAL separation (notably: no thresholds in CHR).                                          |
| CC‑G3‑16          | If `EvidenceLanes` are used, lane tags are declared with a citation to their governing pattern taxonomy (`B.3`), and any lane‑dependent tolerances/proof requirements are explicitly pinned (policy‑id / edition refs). Cross‑lane comparison/aggregation is **illegal by default** unless an explicit governing-pattern policy makes it lawful (typically `G.4`), and it must be auditable via evidence paths (`G.6`). |
| CC‑G3‑17          | If the CHR outputs are bound into the planned baseline / suite seam, the binding uses `CHRMechanismSuiteSlotFillingsPlanItem` as defined in `A.19.CHR` + `A.15.3` (no local baseline variants; wiring via `G.3:Ext.SuiteBoundaryLinkage`). |
| CC‑G3‑18          | **Freshness is explicit.** Each `CHR.Characteristic` declares a validity window and either (i) an explicit `NonDecayingDecl` or (ii) a freshness/half‑life statement that is pinned to the governing pattern (`B.3.4`) when policy‑bound (`G.3:Ext.DecayWiring`). Changes in decay windows/policies participate in RSCR via canonical trigger kinds declared in `G.3:4.1`. |


### G.3:8 - Common Anti‑Patterns and How to Avoid Them

* **Hidden cardinalization.** Don’t treat ordinal encodings as interval/ratio; do publish coordinate policies that explicitly preserve order‑only invariants and forbid arithmetic upgrades.
* **Unit laundering.** Don’t add or average quantities with incompatible units; do force explicit unit discipline and legality checks via MM‑CHR governing definitions.
* **Polarity drift.** Don’t rely on “higher is better” implicitly; do publish polarity explicitly and make downstream use auditable.
* **Threshold leakage into CHR.** Don’t embed policy cut‑offs in CHR; do keep thresholds in CAL acceptance artefacts.
* **Unpinned semantics.** Don’t cite “the metric” or “the distance” without edition pins; do require edition‑pinned references when semantics affect interpretation.
* **Unscoped reuse.** Don’t reuse CHR terms across contexts without explicit import and loss notes; do keep crossings explicit and auditable (pinned through `G.Core`).

### G.3:9 - Consequences

* **Legality becomes checkable.** Downstream patterns can reject illegal operations and rely on explicit legality surfaces rather than implicit conventions.
* **Comparability without semantic flattening.** Plural traditions remain representable because CHR preserves local meaning while making lawful relations explicit.
* **Reproducible downstream behavior.** Edition/policy pins make “why did this change?” answerable and RSCR actionable.
* **Authoring overhead.** The pattern shifts effort to up‑front authoring: explicit cards, pins, and tests are non‑optional when CHR becomes a public kit surface.

### G.3:10 - Rationale

CHR is the point where “numbers start moving” *only if* measurement semantics are stable enough to support lawful downstream reasoning. By making scale/unit/polarity explicit, publishing legality and guard surfaces, and requiring provenance pins, CHR authoring prevents downstream mechanisms from silently inventing their own legality assumptions.

Separating core invariants into `G.Core` prevents drift and ensures Part‑G‑wide properties (tri‑state, penalty routing, set‑return semantics, RSCR typing, Default Governing Definition Index) cite `G.Core` as their governing definition, while CHR remains responsible for CHR‑specific kit surfaces.

### G.3:11 - SoTA‑Echoing

This pattern aligns with post‑2015 best practice by:

* treating abstention/defer and set‑valued outcomes as first‑class design objects (consistent with modern selective prediction and set‑valued reporting practice),
* keeping multiobjective and archive‑based reasoning set‑returning rather than silently scalarizing (consistent with QD/illumination and open‑ended evaluation practice after 2015),
* making evaluation semantics reproducible through explicit edition/policy pinning (aligned with the modern emphasis on reproducibility and “specifying the evaluation surface” rather than only reporting metrics),
* modularizing method‑family specifics (QD/OEE, explore‑exploit) via explicit wiring and governing-definition assignment rather than embedding method semantics into universal measurement legality.

### G.3:12 - Relations

**Builds on:** `G.Core`, `G.1`, `G.2`, `G.6` (EvidenceGraph / Path citation), `A.19.CHR`, `A.15.3`, `A.17–A.18/C.16` (MM‑CHR), `F.1–F.9` (Contexts/UTS/Bridges), `B.3` / `B.3.4`, `A.10`, `E.10`, `E.5.1–E.5.3`.
**Uses (via Extensions):** `G.0` (promotion/linkage to `CG‑Spec`), optional `C.18 and C.19` (QD/OEE wiring).
**Publishes to:** `G.4` (admissible operators plus legality and guard macros and freshness pins), `G.5` (role declarations plus pins for reproducibility), `UTS` (Name Cards and public-id continuity notes), RSCR tests and hooks.
**Constrains:** any CAL/LOG/selector usage that consumes CHR (must treat CHR artefacts as typed/legal surfaces, not as prose hints).

### G.3:End

## G.4 - CAL Authoring for a CG-Frame: Operators, Acceptance Clauses, Evidence Wiring

**Tag.** Architectural pattern (publishes `CAL Pack@CG-Frame`; consumes `CHR Pack@CG-Frame`; constrains selector/dispatcher usage; binds GateCrossing discipline; exposes `ReferencePlane` and penalty/guard policy pins to `SCR`)

**Stage.** design‑time (authoring & publication; enables lawful run‑time evaluation)

**Primary output.** A notation‑independent `CAL Pack@CG-Frame` containing:
`CAL.Charter@Context`, `CAL.Operator[]`, `CAL.Acceptance[]`, `CAL.Flow[]`,
`CAL.EvidenceProfiles`, `CAL.ProofLedger`, **optional** `CAL.NQD[]` (when declared),
UTS entries (Name Cards with twin labels and public-id continuity notes, including deprecations and lexical-continuity notes),
RSCR tests, Worked‑Examples, and a `TaskMap@Context` (`TaskMap`; handoff record consumed by `G.5`).

**Primary hooks.** `G.Core` (Part‑G invariants + RSCR trigger catalogue + Default Governing Definition Index), `G.1` (CG‑FrameContext), `G.2` (SoTA Synthesis Pack), `G.3` (CHR Pack), `G.0` (CG‑Spec legality gate), `A.19` (CN‑Spec), `A.18` (CSLC), `A.10` (provenance anchors), `B.3` (trust / freshness / decay), `E.18` + `A.21` + `F.9`/`F.17`/`E.17` (GateCrossing / CrossingBundle harnesses), `G.6` (EvidenceGraph / PathId / PathSliceId; wired via Extensions), `G.5` (Selector & Dispatch), `G.10` (shipping), `G.11` (refresh orchestration), plus Contexts/UTS/LEX disciplines already fixed elsewhere in the spec.

**Non‑duplication note.** Universal Part‑G invariants (no shadow specs, crossing visibility, tri‑state guard, penalties→`R_eff`‑only, set‑return semantics, P2W split, typed RSCR causes, Default Governing Definition Index, shipping boundary) are governed in `G.Core` and are pulled into `G.4` only through the `G.Core linkage` manifest in **G.4:4.1** (and via explicit delegations in CC).

### G.4:1 - Problem frame

A CG‑Frame has:

* a declared `CG-FrameContext` (scope, described entity, plane),
* a plurality of method traditions and claims (SoTA inputs), and
* CHR‑typed measurement constructs (`Characteristic/Scale/Coordinate` + legality guard macros).

Before any run‑time selection, comparison, aggregation, or selected-set formation is executed downstream, the CG‑Frame needs an explicit, auditable **CAL Pack** that:

1. defines *what operators exist* and what they are allowed to do over CHR types,
2. externalizes *fit‑for‑purpose acceptance* as typed predicates (with Context‑local thresholds), and
3. binds these choices to an evidence wiring surface (lanes, provenance anchors, policy pins, and refresh triggers) so that downstream selection, logging, parity, and shipping can cite *stable ids* rather than re‑inventing semantics.

This pattern provides the design‑time authoring kit and the publication surface for CAL artifacts, while delegating Part‑G‑wide invariants to `G.Core` and CN-Spec and CG-Spec legality to `CG‑Spec`/`CN‑Spec`.

### G.4:2 - Problem

Teams repeatedly face drift and ambiguity in the CAL Pack that sits between “typed measurements exist” and “a selector/dispatcher runs”:

* **Illicit operations** slip in (implicit cardinalization, unit laundering, ordinal arithmetic).
* **Acceptance is scattered** (thresholds embedded in code or in CHR prose; predicates not typed; unknown handling inconsistent).
* **Evidence wiring is underspecified** (which provenance anchors matter, what policy ids are in force, what is plane‑scoped, what changes must trigger refresh).
* **Cross‑context imports are silent** (hidden reuse of constructs across contexts or planes/editions without published GateCrossings and loss accounting).
* **Tooling artifacts become semantics** (vendor flags or implementation details substitute for a conceptual specification).

### G.4:3 - Forces

* **Expressiveness vs legality.** CAL must allow useful comparisons/aggregations while staying lawful under CHR typing and legality gates.
* **Pluralism vs comparability.** Multiple method traditions must coexist without forcing premature unification, yet remain cross‑citable and auditable.
* **Decision support vs auditability.** CAL must support selection and selected-set formation while preserving explicit, reviewable assumptions and proofs.
* **Exploration vs assurance.** CAL must support exploratory regimes (probing, novelty, open‑ended search) without letting un‑assured outputs silently become dominance claims.
* **Locality vs portability.** CAL must be Context‑local by default but prepared for explicit reuse via Bridges and published crossing bundles.

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

  * cites `CG-FrameContext`, `describedEntity`, `ReferencePlane`,
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

  * declares result kind (scalar only when lawful; selected-set / set-surface when partial orders remain partial orders),
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

* anchors CAL to the CG‑Frame scope (`CG-FrameContext`, `describedEntity`, `ReferencePlane`),
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
* what the **result kind** is (scalar only where lawful; otherwise selected-set / set-surface).
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

### G.4:5 - Archetypal Grounding

**Tell.** A CG‑Frame must choose and justify a set of candidate methods (possibly a selected set or archive) under explicit legality, evidence, and scope constraints. CHR provides the typed measurement basis; CAL turns it into executable, auditable predicates and flows.

**Show 1 (in‑context CAL pack skeleton).**
Context: R&D selected-set choice. CHR defines `SafetyClass(ord↑)`, `CostUSD_2026(ratio↓)`, `Readiness(nominal)`.

* `CAL.Operator: DominatesPareto`
  Signature over CHR types, precondition references CHR guard macros.
* `CAL.AcceptanceClause: AC_SafetyGate`
  Typed predicate binding `SafetyClass` (and its levels) with Context‑local thresholds; unknown handling uses tri‑state pins.
* `CAL.Flow: Flow_ParetoPortfolio`
  Produces a selected-set result kind; gates by `AC_SafetyGate` and `AC_Budget`.
* `CAL.EvidenceProfile: EP_SafetyEvidence`
  Declares anchor ids and freshness policy pins required for `SCR`.

Downstream, `G.5` consumes only the handoff manifest: clause ids, operator ids, and evidence profile ids (no embedded thresholds).

**Show 2 (explicit cross‑context import).**
A `SafetyClass` value is imported from a different Context or plane. CAL may still author an acceptance clause using that value, but only after the reuse is made explicit as a published crossing bundle and the CAL artifacts cite the relevant ids/pins. The CAL pack remains Context‑local; portability is achieved through explicit crossings and citations, not by silently widening scope.

### G.4:6 - Bias-Annotation

CAL is where “what counts as acceptable” is encoded. Typical bias vectors include:

* threshold‑selection bias (arbitrary floors masquerading as natural laws),
* measurement bias amplified by illegitimate arithmetic or hidden scalarization,
* survivorship bias in Worked‑Examples and probe telemetry,
* Goodhart pressures when report‑only telemetry is accidentally treated as dominance.

The pattern mitigates these by requiring typed acceptance clauses, explicit policy pins, and an auditable proof/justification ledger, while keeping cross‑context reuse explicit and penalized only in the explicit assurance lane.

### G.4:7 - Conformance Checklist (normative)

| ConformanceId     | Statement                                                                                                                                                                                                                                                                                                      |
| ----------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **CC‑G4‑CoreRef** | Conformance with `G.4` requires satisfying the effective `G.Core` obligations referenced by the `GCoreLinkageManifest` in **G.4:4.1** (profiles, pin sets, consumed defaults, and trigger kinds).                                                                                                              |
| **CC‑G4‑01**      | `CAL Pack@CG-Frame` is published as a notation-independent object with stable UTS ids (Name Cards with twin labels) for `CAL.Charter`, `TaskMap`, all operator, acceptance, flow, and evidence carriers, Worked-Examples, and public-id continuity notes, including deprecations and lexical-continuity notes. Tooling/vendor details remain non-normative. |
| **CC‑G4‑02**      | `CAL.Charter@Context` pins `CG-FrameContext`, `describedEntity` (incl. `ReferencePlane`), and the relevant governing spec references by edition pins (`CNSpecRef.edition`, `CGSpecRef.edition`).                                                                                                                     |
| **CC‑G4‑03**      | Every `CAL.Operator` has an explicit CHR‑typed signature and explicit preconditions; any legality guard macros referenced are cited by id (no “implicit legality”).                                                                                                                                             |
| **CC‑G4‑04**      | Every `CAL.Acceptance` binds to CHR ids (`CharacteristicRefs`) and declares unknown handling and failure behavior via pins/refs; thresholds and cutoffs appear only here (not inside CHR artifacts and not inside operator prose). If the clause depends on cross-context, cross-plane, or cross-edition imports, it cites `GateCrossingId[]/CrossingBundleId[]`. |
| **CC‑G4‑05**      | If an acceptance clause, operator, or flow induces numeric comparison/aggregation, it cites the relevant `CG‑Spec.characteristic` ids and links to legality proof refs (CSLC) in the ProofLedger; otherwise it must be authored so that downstream can degrade/abstain rather than perform illegal operations. |
| **CC‑G4‑06**      | Every `CAL.Flow` declares its result kind and the set of gating acceptance clauses; any thinning/selection‑aid policies (e.g., ε‑front selection) are explicitly policy‑bound and do not silently replace the underlying result kind.                                                                      |
| **CC‑G4‑07**      | Every `CAL.EvidenceProfile` declares: provenance anchors (A.10), evidence lanes (`F/G/R`), freshness/decay pins (incl. freshness window + decay/Γ_time selector refs), and any penalty routing policy pins (`Φ(CL)`, `Ψ(CL^k)`, `Φ_plane`) needed for run‑time `SCR` surfacing. It either pins an explicit `ΓFoldRef.edition` override or (if absent) cites `DefaultId.GammaFoldForR_eff` (via `G.Core.DefaultGoverningDefinitionIndex`). Penalty policies affect `R_eff` only and do not define dominance. Any referenced penalty policy family is justified in the ProofLedger (monotone + bounded).  |
| **CC‑G4‑08**      | `CAL.ProofLedger` exists and is UTS‑citable; it links each operator/flow/clause to required proof/justification refs and records explicit degradation conditions when assumptions fail. If an explicit `ΓFoldRef` is pinned, it includes monotonicity + boundedness/boundary behavior proof refs for that fold. |
| **CC‑G4‑09**      | CAL publication includes RSCR tests and Worked‑Examples sufficient to detect illegality (incl. unit laundering / ordinal arithmetic), to exercise authored acceptance/flow behavior, and to validate the authored freshness envelope when it is part of admissibility; missing tests/examples are treated as an auditable gap, not as “assumed OK”. |
| **CC‑G4‑10**      | `TaskMap@Context` (`TaskMap`) is present and provides `G.5` with acceptance clause ids (`AcceptanceClauseId[]`; selector gates), operator/flow ids, and evidence profile ids required for explainability and audit; selector implementations must not embed thresholds or duplicate acceptance semantics.    |
| **CC‑G4‑11**      | Any method/discipline specifics are placed under `G.4:4.5 Extensions` as `GPatternExtension` blocks (stable `PatternScopeId`, explicit governing definition, pins, and RSCR triggers); no extension introduces competing defaults or replaces `G.Core` invariants. |
| **CC‑G4‑12**      | `CAL Pack@CG-Frame` includes public-id continuity records for public ids: deprecations, edition bumps, and lexical-continuity notes. It exposes refresh payload pins, including editions, policies, UTS ids, and, when present, `PathId` and `PathSliceId`, sufficient for `G.11` to plan RSCR without inferring semantics from prose. |
| **CC‑G4‑13**      | When `G.4:Ext.NQD` is present, `CAL.NQD[]` is present and is wired only via the declared governing pattern (`C.18`): at minimum it pins `DescriptorMapRef.edition`, `DistanceDefRef.edition`, and `InsertionPolicyRef`, and it treats archive/illumination summaries as report‑only unless explicitly promoted by a CAL acceptance clause/policy. |
| **CC‑G4‑14** | CAL does not mint new universal types to encode “strategy/policy”. Strategy is expressed as authored flows + acceptance clauses + policy/task pins (and downstream registry/composition in `G.5`); any specialization is introduced only via `GPatternExtension` wiring blocks or cited governing patterns.  |

### G.4:8 - Common Anti-Patterns and How to Avoid Them

* **Hidden thresholds.**
  Avoid: embedding cutoffs in CHR prose or in operator descriptions.
  Prefer: `CAL.AcceptanceClause` with explicit ids and pins.

* **Untyped “score(x)”.**
  Avoid: operators with implicit units and untracked legality assumptions.
  Prefer: explicit CHR‑typed operator signatures + cited legality checks.

* **Silent cross‑context reuse.**
  Avoid: importing constructs across Contexts/planes/editions without published crossings.
  Prefer: explicit crossing artifacts and citations; keep CAL pack Context‑local.

* **Acceptance as implementation detail.**
  Avoid: acceptance embedded in tool logic.
  Prefer: publish acceptance as citable CAL artifacts; downstream consumes ids.

* **Exploratory telemetry treated as dominance.**
  Avoid: letting probe/illumination telemetry quietly become a dispatch criterion.
  Prefer: keep it report‑only unless an explicit policy‑bound acceptance clause authorizes promotion.

### G.4:9 - Consequences

* CAL becomes a stable, citable CAL Pack: operator/acceptance semantics are explicit artifacts, not tacit code behavior.
* Legality failures are surfaced as authoring defects (RSCR‑testable) rather than run‑time surprises.
* Downstream patterns (`G.5`, `G.8`, `G.9`, `G.10`, `G.11`) can reference stable ids/pins without redefining acceptance or operator semantics.
* Method pluralism is supported: multiple calculi can coexist as separate operator/flow/acceptance families, wired via Extensions rather than mixed into the core kit.

### G.4:10 - Rationale

CAL sits at the boundary where typed measurement becomes actionable choice. Making CAL a published, typed, and testable artifact reduces semantic drift and prevents “shadow legality gates” from emerging in tools or in downstream prose.

The design separates concerns:

* CHR governs measurement typing and legality guard macros,
* CG‑Spec and CN‑Spec govern the legality gate and governance card, respectively,
* `G.Core` governs Part‑G invariants and trigger/default discipline,
* `G.4` governs the CAL kit: authoring objects, publication surface, and handoff manifest.

This yields modularity (one governing definition per invariant or default), auditability (pins/ids and proof refs), and extensibility (method families attach through explicit extension modules).

### G.4:11 - SoTA-Echoing

CAL authoring is compatible with post‑2015 best practice families without confusing “popular” with “best‑available”:

* **Risk‑controlled acceptance**: modern conformal / selective / set‑valued prediction families where “abstain” is a first‑class, audited outcome (fits tri‑state gating + explicit calibration pins).
* **Robust acceptance envelopes**: distribution‑shift‑aware and distributionally‑robust acceptance styles, expressed as policy‑pinned predicates rather than hidden heuristics.
* **Modern multi‑objective practice**: preference‑aware, interactive, and set‑returning multi‑objective decision families that preserve partial orders and selected sets.
* **Quality‑Diversity after 2015**: archive‑based search families (e.g., CMA‑ME‑class) attach as wiring via edition‑pinned descriptor/distance/insertion artifacts.
* **Open‑ended exploration after 2015**: environment‑method co‑evolution families (e.g., POET‑class) attach through explicit generator family wiring and policy‑bound acceptance branches.

All of these remain method‑specific semantics and therefore belong in `Extensions` blocks (or their governing patterns), while `G.4` keeps the calculus kit stable and auditable.

### G.4:12 - Relations

**Builds on:** `G.Core` (and the pattern template discipline in `E.8`).

**Uses:** `G.1` (CG‑FrameContext), `G.2` (SoTA Synthesis Pack), `G.3` (CHR Pack), `G.0` (CG‑Spec legality gate), `A.19` (CN‑Spec), `A.18` (CSLC), `A.10` (provenance anchors), `B.3` (trust/freshness/decay), `E.18` + `A.21` + `F.9`/`F.17`/`E.17` (GateCrossing harness).

**Uses (via Extensions):** `G.6` (EvidenceGraph/Path citation; when `G.4:Ext.EvidenceGraphWiring` is present), `C.18` (NQD), `C.19` (E/E‑LOG), `C.23` (SoS‑LOG).

**Used by:** `G.5` (selector/dispatcher), `G.8` (SoS‑LOG bundles), `G.9` (parity), `G.10` (shipping), `G.11` (refresh orchestration).
**Publishes to:** UTS (public ids and public-id continuity records), RSCR (tests and trigger emissions), `G.5` (handoff manifest), and, as cited payload, shipped packs governed by `G.10`.

**Constrains:** any run‑time LOG implementation that executes CAL operators/flows must treat CAL artifacts as citable specifications and must not re‑invent acceptance semantics.

### G.4:End

## G.5 - Multi‑Method Dispatcher & MethodFamily Registry

> **Type:** General (G)
> **Status:** Stable
> **Normativity:** Normative

**Plain-name.** Multi-method dispatcher and method-family registry.

**Intent.** Govern the dispatcher/registry object set for rival method families and publish selector-facing retained-set outcomes without collapsing plurality into one hidden scalar winner.

### G.5:0 - Use this when

- several method families or generator families can admissibly act on the same declared task family or work target
- you need one selector to return a `Shortlist`, `RankedShortlist`, one `SpecialistHandoff`, one other narrowed handoff plan, or one abstain outcome without pretending that there is always one scalar winner
- the published result must carry enough basis pins to support later comparison, handoff, or escalation without changing its declared outcome kind or any applicable public selected-set label

### G.5:0.1 - What goes wrong if missed

- rival families are compared under silent comparator drift, hidden baseline changes, or unspoken crossing costs
- the selector hides one dogmatic winner even when only a partial order is admissible
- selected-set publication gets hidden inside `C.11`, `C.19`, or `C.24`, so the published result no longer makes clear whether it carries local choice, pool policy, enactment, or publication
- exploration, open-ended, or specialization pressure leaks in as one architecture convenience rather than one explicit policy-bound choice

### G.5:0.2 - What this buys

- one registry that keeps rival method families disjoint but dispatchable
- one selector result form that can publish candidate sets, `Shortlist`, `RankedShortlist`, one `SpecialistHandoff`, narrowed handoff plans, or abstain outcomes honestly
- one `DRR/SCR`-addressable trace with explicit basis pins instead of one hidden selector rationale
- one explicit publication closure so the declared outcome kind, any applicable public selected-set label, retained members or handoff content, ordering status, and basis pins are stated directly in the emitted result

Registry and dispatch remain the primary governed question here; selected-set publication is the explicit closure record for that selector question, not a replacement for it.

### G.5:0.3 - First-minute questions

- What selector outcome kind is this result actually emitting: one set-surface outcome such as `Shortlist` or `RankedShortlist`, one `SpecialistHandoff` or other narrowed handoff, or one abstain outcome?
- Which members are being retained or excluded now?
- Does order materially belong to the published result?
- Which basis pins or policy pins must the published result carry?

### G.5:0.4 - First output

The first useful output from this dispatcher/registry question is one published selector outcome: one set-surface outcome such as `Shortlist` or `RankedShortlist`, one `SpecialistHandoff` or other narrowed handoff plan, or one abstain/escalation result, with the outcome kind, any public selected-set label, retained members or handoff content, ordering status when relevant, and basis pins stated in one place.

If that first output still cannot be written honestly, the current publication result is not finished `G.5` publication yet.

G.5 keeps the dispatcher/registry object set here and leaves universal Part-G invariants to `G.Core`; method- or generator-specific semantics stay in their named source patterns and arrive here only through explicit pins.

When `C.11` has already emitted one local choice result, `C.19` one pool-policy posture, or `C.24` one enactment-facing next move, `G.5` begins where the question becomes selector-facing publication of the retained set or narrowed handoff result rather than one more explanation of why the result looked reasonable. A conformant `G.5` pass should therefore publish the retained set, narrowed handoff, or abstain result directly, with its declared outcome kind, any applicable public selected-set label, and basis pins explicit in the result itself.

A publication result remains unfinished if the declared outcome kind, any applicable public selected-set label, retained members or handoff content, ordering status, abstain or escalation condition, or basis pins are still only implicit in upstream notes.

### G.5:1 - Problem frame

A `CG‑FrameContext` (from **G.1**) and a `SoTA Synthesis Pack@CG‑Frame` (from **G.2**) expose multiple rival, internally coherent **method families** (and sometimes **generator families**) that can plausibly act on the same *describedEntity and ReferencePlane*.

At the same time, the typed slot/scale/coordinate definitions from **G.3/G.4** yield admissible calculi and acceptance clauses—enough to formulate *eligibility*, *assurance*, and *legality* constraints, but not enough to pick “the method” without collapsing plurality.

You need a **notation‑independent** way to:

1. register method/generator families as *auditable, versioned* entries,
2. select/compose/fallback among them at run time for a concrete task instance,
3. publish stable selected-set results and stable identities to UTS, and
4. emit RSCR‑relevant triggers and pins without inventing new “shadow specs”.

### G.5:2 - Problem

How to design a **general, auditable dispatcher** that:

* supports **pluralism** (families from competing Traditions stay disjoint) while remaining **dispatchable** (selection is possible and explainable);
* does **not embed algorithmic dogma** in the core selector kernel;
* respects Context boundaries and crossing discipline (Bridge‑only; explicit pins);
* produces **set‑valued outcomes** when only partial orders are admissible;
* cleanly separates:

  * **selector object set/components** (registry + selector facade + publication records),
  * **universal Part‑G invariants** (carried by `G.Core`),
  * **method/generator specifics** (wired only via `Extensions` blocks).

### G.5:3 - Forces

* **Pluralism vs. forced totalisation.** Many selection regimes are inherently partial‑order; forcing a scalar winner often creates illegal semantics.
* **Evidence realism vs. hard gates.** Eligibility/acceptance frequently depends on incomplete evidence; selection must remain auditable under tri‑state unknowns.
* **Reuse vs. leakage.** Cross‑Context reuse is valuable but must be explicit (Bridge + loss notes) and must not silently re‑ground semantics.
* **Exploration vs. exploitation.** Dispatch sometimes must probe alternatives under explicit policy/risk envelopes, but probing must not become an implicit fourth status.
* **Evolvability vs. churn.** Registries evolve (new families, deprecations, edition bumps); continuity must not be broken by “rename by meaning”.

### G.5:4 - Solution
#### G.5:4.6a - Causal method dispatch declarations

Method selection involving causal methods must declare whether a compared method is an observational predictor, an intervention optimizer, a counterfactual strategy, a causal fairness estimator, a causal-RL policy, or a simulation-only method.

Optional `MethodFamily.causalUseDispatchSpec?`:

```text
MethodFamily.causalUseDispatchSpec? {
  causalUseQuestionRef?: U.CausalUseQuestion
  targetCausalityLadderRung: CausalityLadderRung
  causalUseClaimKind: CausalUseClaimKind
  causalActionPolicyClass?: CausalActionPolicyClass
  causalEvidenceSupportBasis?: CausalEvidenceSupportBasis
  causalUseSupportRecordRef?: CausalUseSupportRecordRef
  causalUseSupportVerdict?: CausalUseSupportVerdict
  causalMethodComparisonPosture:
    observationalPredictor |
    interventionOptimizer |
    counterfactualStrategy |
    causalFairnessEstimator |
    causalRLPolicy |
    simulationOnlyMethod
  supportedUse: CausalUseSupportStatement
  unsupportedUse: CausalUseUnsupportedStatement
}
```

`causalMethodComparisonPosture` is a selector-facing method-comparison classification, not a `U.Role`, role assignment, responsibility, or actor position. `simulationOnlyMethod` maps to `CausalEvidenceSupportBasis = simulationOnlyCounterfactualOutputBasis`, bounded simulation-supported use, and unsupported intervention-effect or realized-counterfactual-sample use unless another `C.28` support basis is cited.

What changes in practice: a selector must not compare "methods that improve outcome" unless each causal method declares the causality-ladder rung, causal method comparison posture, and `C.28` support record and verdict when causal-use support is being consumed.

What this does not authorize: `G.5` does not identify causal effects, decide fairness, certify off-policy causal evaluation, or compare cross-rung causal methods as one undifferentiated improvement set; it keeps method dispatch and selected-set publication while `C.28` governs causal-use support.


#### G.5:4.1 - G.Core linkage (normative)

**Builds on:** `G.Core` (Part‑G core invariants; Default Governing Definition Index citation)

**GCoreLinkageManifest (normative; size‑controlled via profiles/sets).**
Effective obligations/pins/triggers are computed by union expansion of the referenced ids (per `G.Core:4.2.1`). Profiles/sets + explicit deltas; `Nil‑elision` applies.

* `CoreConformanceProfileIds :=`

  * `GCoreConformanceProfileId.PartG.AuthoringBase`
  * `GCoreConformanceProfileId.PartG.TriStateGuard`
  * `GCoreConformanceProfileId.PartG.UTSWhenPublicIdsMinted`
  * `GCoreConformanceProfileId.PartG.ShippingBoundary`
* `CorePinSetIds :=`

  * `GCorePinSetId.PartG.AuthoringMinimal`
  * `GCorePinSetId.PartG.CrossingVisibilityPins` *(crossing‑aware use; pins from this set may be intentionally strengthened (optional→required) via `CorePinsRequired`)*
* `CorePinsRequired :=` *(delta over PinSets; pins/refs are id‑only; prefer strengthening optional→required over restating pins already covered by PinSets)*

  * `TaskSignatureRef` *(see `G.5:4.2` / S2)*
  * `MethodFamilyId[]` *(registry keys in scope)*
  * `GeneratorFamilyId[]?` *(when generator families are in scope)*
  * `PathId[]` *(audit citations for “why” and for evidence)*
  * `PathSliceId[]` *(audit citations for “why” and for evidence)*
  * `UTSRowId[]` *(published identities for selected/registered families and selector policy records)*
  * `FailureBehaviorPolicyId?` *(only when degrade/abstain behavior is explicitly policy‑bound)*
  * `SoSLogBranchId?` *(only when degrade/abstain behavior is explicitly policy‑bound)*
* `DefaultsConsumed :=`

  * `DefaultId.GammaFoldForR_eff`
  * `DefaultId.PortfolioMode`
  * `DefaultId.DominanceRegime`
* `RSCRTriggerSetIds :=`

  * `GCoreTriggerSetId.RefreshOrchestration`
    *(payload pins: `TaskSignatureRef`, `CGSpecRef.edition`, `CNSpecRef.edition`, `MethodFamilyId[]`, `GeneratorFamilyId[]?`, `AcceptanceClauseId[]?`, `SoSLogBranchId?`, `FailureBehaviorPolicyId?`, `DescriptorMapRef.edition?`, `DistanceDefRef.edition?`, `TransferRulesRef.edition?`, `InsertionPolicyRef?`, `PathId`, `PathSliceId`, `SCRId`, `DRRId`, `RSCRTestId[]`)*

#### G.5:4.2 - Dispatcher & Registry object set (notation‑independent)

G.5 defines the **object-set components** below. Their purpose is to make dispatch **possible and auditable** without embedding any method-family semantics in the selector kernel.

**S1 — `MethodFamily Registry` (design‑time; per CG‑Frame).**
A registry row represents *a family*, not a single implementation. Minimal fields (conceptual, notationally independent):

* `Identity`: `MethodFamilyId`, `ContextId`, lineage/Tradition notes, `UTSRowId` (twin labels where applicable).
* `EligibilityStandardRef`: a typed predicate record (tri‑state per `G.Core`), expressed in CHR/CAL terms and pinned to the relevant editions.
* `AssuranceProfileRef`: evidence‑lane expectations and assurance-lane pins (SCR‑addressable).
* `LegalityBindings`: explicit references to the **single** governance card and legality gate (`CNSpecRef`, `CGSpecRef`) and to any required legality constraints (e.g., scale/unit legality via CSLC).
* `EvidencePins`: citations to `G.6` (`PathId/PathSliceId`) for claims/guarantees where such claims are asserted.
* `CrossingAllowance`: explicit Bridge/CL allowance pins **only** if cross‑Context operation is claimed.
* `PolicyHooksRef?`: optional pointers to policy records (not defined here; wired via Extensions).

**S1′ — `GeneratorFamily Registry` (design‑time; optional; per CG‑Frame).**
A registry row for families that generate tasks/environments and/or co‑evolve solver families. G.5 carries the registry-entry shape, not the generator semantics:

* `Identity`: `GeneratorFamilyId`, `ContextId`, `UTSRowId`.
* `GeneratorSignatureRef`: conceptual I/O and budget semantics.
* `EnvironmentValidityRegionRef?`: pinned constraints for generated environments/tasks.
* `TransferRulesRef.edition?`: required when the Open-Ended mode is enabled (semantics come from the cited extension refs).
* `CouplerRefs?`: which `MethodFamilyId[]` can be coupled with this generator family.

**S2 — `TaskSignature` façade (design‑time + run‑time).**
A minimal typed record the dispatcher consumes. Its role is **pinning and auditability**, not over‑specification. It must be CHR/CAL‑typed and provenance‑aware.
G.5 treats `TaskSignatureRef` as an input record; it does not define CHR/CAL semantics.

**S3 — `Selection kernel façade` (run‑time; policy‑governed).**
A notation‑independent selector that:

* consumes `TaskSignatureRef` + registry entries + pinned spec refs,
* applies eligibility/assurance gating (tri‑state),
* computes an admissible (possibly partial) order,
* returns one declared selector outcome: most often one set-surface outcome such as `Shortlist` or `RankedShortlist`, but sometimes one `SpecialistHandoff`, one other narrowed handoff, one abstain outcome, or one escalation outcome (per `DefaultId.PortfolioMode` and explicit overrides),
* emits audit records (DRR/SCR‑addressable pins).

**S3.A — `TaskFamilySpecializationProfile@Context` (run‑time; conditional).**
When the real selector question is acquisition of usable specialization on a declared task family, the selector may publish one `TaskFamilySpecializationProfile@Context` for each candidate, one `SpecialistHandoff`, or one narrowed handoff plan. Here `profile` means one selector-time comparison record for bounded specialization, not a new kernel type and not a generic narrative profile. `G.5` carries this selector-time specialization question here; it does not re-govern the adaptation-signature field vocabulary from `C.22.1`.

The profile should therefore cite one `AdaptationSignatureRef` or equivalent pinned field set carrying the declared `TaskFamilyRef` or `TaskSignature`, the work-measure threshold target, prior exposure declaration, time-to-threshold, budget-to-threshold, post-threshold efficiency when relevant, any declared transfer or retention claim, any downside cost or downside on adjacent tasks, and any specialization-entry baseline, specialization-entry evidence, or stepping-stone evidence item that materially affects comparison.

Admission rule for `SpecialistHandoff`: use that handoff kind only when the truthful published result is one heterogeneous handoff bundle whose members occupy different specialization roles that still need to travel together. Do not use it when one ordinary `Shortlist`, `RankedShortlist`, `ExplorationArchive`, or another narrower named result kind already states the result more precisely.

When the declared task family is heterogeneous, the selector may return one `SpecialistHandoff`, one other narrowed handoff plan, or one small admissible set that preserves rival specialists rather than collapsing them into a fake single winner. Low-human-overlap candidates remain admissible only when the profile, evidence basis, and policy constraints are explicit.

**S4 — `Composition & fallbacks` templates (design‑time).**
A library of composition shapes (preconditioner → solver → verifier; cascades; meta‑selectors) **as templates**, legality‑checked and pinned. Concrete strategy semantics stay in the referenced method families; G.5 only carries the composition template.

**S5 — `Publication & telemetry` interface (run‑time).**
A standard publication interface to publish:

* `DRR` (decision rationale) + `SCR` (support/confidence citation) with explicit pins,
* declared selector / selected-set records,
* telemetry pins to refresh orchestration (`G.11`), without governing orchestration.

When the current publication question is selected-set publication rather than one generic registry trace, `Shortlist` is the public selected-set label, `RankedShortlist` is the ordered specialization when order materially belongs to the published result, `ShortlistId` is the emitted public identity, and `ChoiceSet` stays one mathematical gloss rather than the public selected-set label.

**S6 — `Governance & evolution` interface (design‑time).**
Versioning, deprecation, and registry evolution discipline (UTS publication; continuity), without minting new Part‑G‑wide types.

#### G.5:4.3 - Selector head and narrower selector families

Selection/dispatch stays one generic selector head. Narrower selector families may refine it, but they do not redefine the universal invariants pinned through `G.Core`, do not add hidden mandatory inputs beyond pinned policy or edition refs, and do not mutate SlotKinds.

Method- and generator-specific pressures such as `QD` archives, open-ended declared sets, explore/exploit lenses, or preference comparators do not become part of the selector head. They arrive only through explicit extension declarations and the pins those extensions require.

#### G.5:4.4 - Interfaces (minimal I/O record)

| Interface                         | Consumes                                                                                                                                                     | Produces                                                                                                                                                                                                                                                   |
| --------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **G.5‑1 RegisterFamily**          | `SoTA` family cards (from `G.2`), CHR/CAL pins (from `G.3/G.4`), `CNSpecRef.edition`, `CGSpecRef.edition`, `ContextId`                                       | A `MethodFamily` registry row (`MethodFamilyId`, `EligibilityStandardRef`, `AssuranceProfileRef`, `UTSRowId`, pinned refs)                                                                                                                                 |
| **G.5‑2 RegisterGeneratorFamily** | `SoTA` generator family cards (from `G.2`), `ContextId`, pinned refs (including `TransferRulesRef.edition` when applicable)                                  | A `GeneratorFamily` registry row (`GeneratorFamilyId`, `GeneratorSignatureRef`, `UTSRowId`, pinned refs)                                                                                                                                                   |
| **G.5‑3 Select**                  | `TaskSignatureRef`, `MethodFamilyId[]` (in scope), pinned `CNSpecRef/CGSpecRef` (editions), policy refs (if any), audit citation pins (`PathId/PathSliceId`) | `CandidateSet` (set‑returning), declared selector result with `PortfolioMode` recorded, `DRR + SCR` pins; if no admissible candidate exists: return `CandidateSet=∅` plus an escalation hint (`ActionHint`) and the pins required to plan next steps (P2W split applies) |
| **G.5‑4 Compose**                 | `CandidateSet`, composition template refs, pinned legality constraints                                                                                       | Composite strategy template (template‑level; legality‑checked; pinned)                                                                                                                                                                                      |
| **G.5‑5 Telemetry**               | run outcomes + citations + policy/edition pins                                                                                                               | refresh cues (typed RSCR causes + payload pins), parity deltas (if parity harness is in use), telemetry pins (selector‑side; orchestration governing definition is `G.11`)                                                                                              |

#### G.5:4.4a - Worked selector slice

- A catalyst-search team is choosing among three method families for the same declared `TaskSignature` and `C.22.1` adaptation signature.
- The shared profile pins one work-measure threshold target, one freshness window, one prior-exposure declaration, and one adaptation budget. One family reaches threshold quickly but carries high downside on adjacent tasks. One family is slower but transfers cleanly. One family never clears `MinimalEvidence` and must abstain.
- An admissible `G.5` result therefore publishes a set-return shortlist or a narrowed handoff plan, with `DRR/SCR` citing why the third family was excluded and why the first two remain non-dominated. The selector does not invent one scalar winner and does not hide the specialization profile in auxiliary side notes.
- When one upstream `C.19` pass has already narrowed the live pool to one internal retained subset over registered families, `G.5` may publish that result as one `Shortlist` with one `ShortlistId` and explicit basis pins only when selector-facing publication is now the question. Until that emission occurs, the internal retained subset is not yet one public shortlist result.
- When one upstream `C.11` pass has already fixed one local choice over one declared source surface, or one `C.24` pass has already produced one enactment-facing narrowed handoff, `G.5` may publish the selected-set or narrowed-handoff result only when selector-facing publication is now the question. Until this `G.5` emission occurs, the `ChoiceResult`, `CallPlan`, or `CheckpointReturn` is not itself one public `Shortlist`, `RankedShortlist`, or `ShortlistId`-bearing result.

#### G.5:4.4b - Published selected-set result and closure rule

A finished `G.5` pass should publish one explicit selected-set result from the dispatcher/registry question rather than one selector trace that leaves the public result implicit.

Publication here is the closure record for selector work over registered families. It does not replace registry maintenance, dispatcher comparison law, or the upstream pool-policy and local-choice pattern authorities that supplied the retained members.

The admissible selector outcome families here are:

- `SelectorOutcomeKind = SetSurfaceOutcome`, with `SetSurfaceKind = Shortlist` when one retained set is published without one material internal order and `SetSurfaceKind = RankedShortlist` when ordering materially belongs to the result;
- `SelectorOutcomeKind = HandoffOutcome`, with `HandoffKind = SpecialistHandoff` or one other narrowed handoff plan when heterogeneity is the truthful downstream result;
- `SelectorOutcomeKind = AbstainOutcome` when no admissible candidate exists and the truthful result is one abstain;
- `SelectorOutcomeKind = EscalationOutcome` when no admissible candidate exists and the truthful result is one escalation.

`SetSurfaceKind` belongs only inside `SetSurfaceOutcome`. `Shortlist` and `RankedShortlist` are public selector results over registered rows. They are not merely one upstream internal retained subset copied forward under one prettier label. `G.5` is the governing pattern that turns selector state into one public result with one explicit outcome kind, one explicit selected-set label when applicable, one explicit member set or handoff content, and one explicit basis-pin set.

A publication result should state at least these fields:

- the selector outcome kind being emitted;
- the public selected-set label when the outcome is one set-surface outcome;
- retained members, or the narrowed handoff content, or the abstain/escalation condition;
- ordering status when ordering matters;
- basis pins and policy pins sufficient to justify the result;
- one explicit next downstream use posture when the result is a handoff rather than one terminal publication.

A compact result may therefore look like:

```text
SelectorOutcome(
  selectorOutcomeKind = SetSurfaceOutcome,
  setSurfaceKind = Shortlist,
  members = [family_A, family_C],
  shortlistId = shortlist_17,
  ordering = unordered,
  basisPins = [pathSlice_41, scr_22],
  nextUse = downstream_comparison
)
```

or:

```text
SelectorOutcome(
  selectorOutcomeKind = SetSurfaceOutcome,
  setSurfaceKind = RankedShortlist,
  members = [family_B, family_A],
  shortlistId = shortlist_23,
  ordering = ranked,
  basisPins = [pathSlice_77, scr_44],
  nextUse = specialist_handoff
)
```

Close as `SelectorOutcomeKind = SetSurfaceOutcome` with `SetSurfaceKind = Shortlist` when several retained members survive admissibly but no public internal order belongs to the result. Close as `SelectorOutcomeKind = SetSurfaceOutcome` with `SetSurfaceKind = RankedShortlist` when order materially belongs to the published result. Close as `SelectorOutcomeKind = HandoffOutcome` with `HandoffKind = SpecialistHandoff` or one other narrowed handoff when heterogeneity itself is the truthful downstream result. Close as `SelectorOutcomeKind = AbstainOutcome` or `EscalationOutcome` when no admissible candidate exists under the pinned constraints.

If the publication still does not state what public result was emitted, who remained in it, whether order belongs to it, and which pins justify it, then the selector has not yet published one finished `G.5` result.

#### G.5:4.4c - Publication quick card

The smallest useful `G.5` publication card usually states:

- `selectorOutcomeKind = SetSurfaceOutcome | HandoffOutcome | AbstainOutcome | EscalationOutcome`
- `setSurfaceKind = Shortlist | RankedShortlist` when `selectorOutcomeKind = SetSurfaceOutcome`
- `handoffKind = SpecialistHandoff | NarrowedHandoff` when `selectorOutcomeKind = HandoffOutcome`
- `membersOrHandoff = ...`
- `ordering = ranked | unordered | n/a`
- `publicId = ...` when one public identity is emitted
- `basisPins = ...`
- `nextUse = downstream comparison | specialist handoff | escalation | none`

A short conforming card may therefore read:

```text
selectorOutcomeKind = SetSurfaceOutcome
setSurfaceKind = Shortlist
members = [family_A, family_C]
ordering = unordered
shortlistId = shortlist_17
basisPins = [pathSlice_41, scr_22]
nextUse = downstream_comparison
```

If the card does not already state what was published, who survived, whether order belongs to the result, and which pins justify it, the publication is still unfinished `G.5` work.

#### G.5:4.4ca - Derived tradition-view publication stays derived over one declared palette

- If selector work consumes one declared source surface such as `Front`, `Archive`, or one source-surface composition through one derived tradition view such as `TraditionFront` or `TraditionArchive`, treat that derived view as one interpretation view over one declared `SoTAPaletteDescription`, not as the default meaning of `Tradition` or of the palette itself.
- When `SelectorOutcomeKind = SetSurfaceOutcome`, the public selected-set label still closes as `Shortlist` or `RankedShortlist`; when `SelectorOutcomeKind = HandoffOutcome`, the result closes as one `SpecialistHandoff` or one other narrowed handoff. The derived tradition view disciplines the source, not the emitted outcome family.
- When such a derived tradition view is active, publish `SourceSurfaceKind`, use `DerivedViewKind` when the distinction matters to interpretation or later shipping, use `SourceSurfaceComposition` only when several source-surface families were genuinely composed, and keep `BasePaletteRef=SoTAPaletteDescriptionId` recoverable alongside the emitted result.
- If the derivation depends on one declared `Q` or one reachability/coverage rule, cite that declared basis directly in `DRR/SCR` or equivalent basis pins rather than leaving the derivation implicit.
- If no derived tradition view is active, stay with the declared palette, front, archive, or shortlist families already named by the selector record.

#### G.5:4.4d - Worked publication closure slice

Three short contrasts keep the publication law practical.

**Several survivors, no public order belongs to the result.**
When the selector has retained more than one admissible family but no downstream public order belongs to the published result, `G.5` should close as one `Shortlist` over the registered surviving rows:

```text
Shortlist(
  members = [family_A, family_C],
  shortlistId = shortlist_17,
  ordering = unordered,
  basisPins = [pathSlice_41, scr_22],
  nextUse = downstream_comparison
)
```

**Order now materially belongs to the published result.**
When one ordered public handoff is required, `G.5` should say so directly instead of leaving order implicit:

```text
RankedShortlist(
  members = [family_B, family_A],
  shortlistId = shortlist_23,
  ordering = ranked,
  basisPins = [pathSlice_77, scr_44],
  nextUse = specialist_handoff
)
```

**No admissible candidate survives.**
When no family clears the pinned legality or evidence gates, `G.5` should close as one abstain or escalation result rather than as one empty shortlist pretending to be progress:

```text
Abstain(
  blockingPins = [cg_min_evidence, crossing_bundle_missing],
  basisPins = [pathSlice_91, scr_61],
  nextUse = escalation
)
```

The practical distinction is simple: an internal retained subset can remain real upstream without yet being one public selector result. `G.5` begins only when that selector-facing publication question starts, and it closes only after the declared outcome kind, any applicable public selected-set label, surviving members or handoff content, and basis pins are emitted directly.

Most selector-side use can stop after `G.5:4.4d`. The blocks below are extension declarations used only when the corresponding mode is actually active.

All blocks below are extension declarations: they declare `Uses` and required pins, but do not redefine semantics already defined in the referenced patterns.

**GPatternExtension block: `G.5:Ext.EELog`**

* `PatternScopeId`: `G.5:Ext.EELog`
* `GPatternExtensionId`: `EELog`
* `GPatternExtensionKind`: `MethodSpecific`
* `GoverningPatternId`: `C.19`
* `Uses`: `{C.19}`
* `⊑/⊑⁺`: `∅`
* `RequiredPins/EditionPins/PolicyPins (minimum):`

  * `EELensPolicyRef` *(or equivalent lens/policy id carried by `C.19`)*
  * `RiskBudgetRef?`
  * `ProbeAccountingRef?`
  * `FailureBehaviorPolicyId?` *(if degrade behavior is routed through policy)*
* `RSCRTriggerKindIds`: `{RSCRTriggerKindId.PolicyPinChange, RSCRTriggerKindId.TelemetryDelta, RSCRTriggerKindId.FreshnessOrDecayEvent}`
* `Notes (extension discipline; semantics cited):`

  * This block activates exploration/exploitation‑governed dispatch.
  * Post‑2015 examples that typically land here: modern bandit‑style or Bayesian selection under explicit risk budgets; adaptive evaluation/probing regimes; safe‑exploration variants where “abstain/degrade” is policy‑bound.

**GPatternExtension block: `G.5:Ext.SoSLOG`**

* `PatternScopeId`: `G.5:Ext.SoSLOG`
* `GPatternExtensionId`: `SoSLOG`
* `GPatternExtensionKind`: `MethodSpecific`
* `GoverningPatternId`: `C.23`
* `Uses`: `{C.23}`
* `⊑/⊑⁺`: `∅`
* `RequiredPins/EditionPins/PolicyPins (minimum):`

  * `SoSLogRuleId[]`
  * `SoSLogBranchId[]` *(including escalation branches, if used)*
  * `FailureBehaviorPolicyId` *(if degrade behavior is made explicit)*
  * `MaturityRungId[]?` *(when maturity ladders are used as gates; semantics come from `C.23`)*
  * `AdmissibilityLedgerRef?` *(when selector consumes admissibility rows rather than recomputing thresholds)*
* `RSCRTriggerKindIds`: `{RSCRTriggerKindId.PolicyPinChange, RSCRTriggerKindId.MaturityRungChange, RSCRTriggerKindId.EvidenceSurfaceEdit}`
* `Notes (extension discipline; semantics cited):`

  * This block pins dispatch decisions to explicit rule/branch ids, enabling auditable “why” without inventing a fourth acceptance status.

**GPatternExtension block: `G.5:Ext.NQD`**

* `PatternScopeId`: `G.5:Ext.NQD`
* `GPatternExtensionId`: `NQD`
* `GPatternExtensionKind`: `MethodSpecific`
* `GoverningPatternId`: `C.18`
* `Uses`: `{C.18, C.19}`
* `⊑/⊑⁺`: `∅`
* `RequiredPins/EditionPins/PolicyPins (minimum):`

  * `DescriptorMapRef.edition`
  * `DistanceDefRef.edition`
  * `InsertionPolicyRef`
  * `TaskSignatureRef` *(when QD is enabled via TaskSignature flags/traits)*
  * `DHCMethodRef.edition?` *(when diversity/coverage telemetry is pinned to a DHC method)*
* `RSCRTriggerKindIds`: `{RSCRTriggerKindId.EditionPinChange, RSCRTriggerKindId.PolicyPinChange, RSCRTriggerKindId.TelemetryDelta, RSCRTriggerKindId.FreshnessOrDecayEvent}`
* `Notes (extension discipline; semantics cited):`

  * G.5 core remains QD‑agnostic; QD semantics are governed by `C.18`.
  * Post‑2015 families that typically dock here: MAP‑Elites‑class QD (incl. later archive‑centric refinements), CMA‑ME‑class hybrids, modern illumination/coverage telemetry regimes where legality and edition pinning matter.

**GPatternExtension block: `G.5:Ext.OpenEndedFamilyWiring`**

* `PatternScopeId`: `G.5:Ext.OpenEndedFamilyWiring`
* `GPatternExtensionId`: `OpenEndedFamilyWiring`
* `GPatternExtensionKind`: `GeneratorSpecific`
* `GoverningPatternId`: `G.2`
* `Uses`: `{G.2, C.19, C.23}`
* `⊑/⊑⁺`: `∅`
* `RequiredPins/EditionPins/PolicyPins (minimum):`

  * `GeneratorFamilyId[]`
  * `TransferRulesRef.edition` *(mandatory when Open‑Ended is enabled)*
  * `EnvironmentValidityRegionRef?`
  * `CoEvoCouplerRef[]?`
  * `SoSLogBranchId[]?` *(when validity of generated tasks is gated by explicit branches)*
* `RSCRTriggerKindIds`: `{RSCRTriggerKindId.EditionPinChange, RSCRTriggerKindId.PolicyPinChange, RSCRTriggerKindId.TelemetryDelta, RSCRTriggerKindId.FreshnessOrDecayEvent}`
* `Notes (extension discipline; semantics cited):`

  * This block enables declared sets of `{Environment, MethodFamily}` pairs without redefining generator semantics in G.5.
  * Post‑2015 examples typically referenced via `G.2` family cards: POET‑class and later open‑ended/co‑evolutionary regimes, including enhanced variants where transfer policies and validity gates must be edition‑pinned.

#### G.5:4.4e - Selector-facing outcome kinds

- `SelectionSlot` returns one selector outcome, not one forced single winner.
- The emitted result should declare its `SelectorOutcomeKind`.
- `SetSurfaceKind` is required only when `SelectorOutcomeKind = SetSurfaceOutcome`.
- `HandoffKind` is required only when `SelectorOutcomeKind = HandoffOutcome`; `SpecialistHandoff` is one handoff kind, not one set-surface head.
- `Front` names the non-dominated source surface under the declared `DominanceSet`.
- `Archive` names the retained exploration surface under the declared retention policy.
- `Shortlist` names the lens-declared selected surface emitted from `SelectionSlot`.
- `RankedShortlist` names one ordered specialization of that shortlisted surface.
- `ShortlistId` is the emitted public token when the shortlist publication must be carried or cited.
- `ChoiceSet` may be used only as the mathematical set gloss for that shortlist when the set object itself is under analysis; it does not replace the public shortlist head.
- `PortfolioMode` states how the selector operated; it does not rename the emitted set surface.
- The default `PortfolioMode=Archive` means that an unspecified selector/generator posture must preserve retained exploration evidence rather than pretending one current front or selected shortlist has already been emitted. It does not make every returned object an `Archive`, does not override `SetSurfaceKind`, and does not change the declared `DominanceSet`.
- If one selector consumes both a front and an archive, say so explicitly rather than blurring them into one generic portfolio.
- If one selector consumes one derived tradition view, keep that derived view explicit rather than silently treating it as the default meaning of `Tradition`.
- `SetSurfaceKind`, `SourceSurfaceKind`, `SourceSurfaceComposition`, `SubjectKind`, `DerivedViewKind`, `BasePaletteRef`, `PromotionPolicy`, and `RetentionIntent=steppingStone` are declaration fields, refs, or policy pins around the returned outcome; they are not additional emitted set surfaces.
- `SourceSurfaceKind` names the immediate declared source-surface family.
- `SourceSurfaceComposition` is used only when the selector genuinely consumed more than one source-surface family such as `Front+Archive`.
- If that source surface is one derived tradition view, keep the base palette recoverable alongside it.
- `DerivedViewKind` may name which derived tradition view is active when that distinction matters to interpretation or later publication.
- `DerivedViewKind` does not replace `SourceSurfaceKind`, `SetSurfaceKind`, or `Shortlist`.
- `BasePaletteRef` is one cited ref/id, not one kind.
- If one selected result comes from one declared source surface, publish that `SourceSurfaceKind` rather than asking the reader to infer it from one mode flag.
- `PromotionPolicy` is required when tie-break or telemetry signals are promoted into dominance.
- The selector may consume one declared source surface and one declared choice lens without trying to explain the whole reason why another probe was worth its cost.
- When `CostToProbe`, `ValueOfInformation`, `ValueOfComputation`, `explore_share`, `backstop_confidence`, or sequencing pressures matter, keep them explicit in the surrounding choice doctrine instead of smuggling them into set-surface declaration fields.
- Selector-facing results should name the set-surface kind, source-surface kind, derived-view declaration when needed, the emitted shortlist family, and promotion/default routing.
- Those selector-facing field values should use controlled tokens, cited ids, or already-declared head labels rather than selector-local prose values.

### G.5:5 - Archetypal Grounding

**Tell (archetype).**
**System** must choose among rival families without lying about measurement legality, crossings, or evidence. **Episteme** insists that what is chosen must remain comparable, auditable, and stable under refresh.

**Show 1 (multi-Tradition dispatch; unordered shortlist).**
A `CG-Frame` includes multiple decision-theoretic families with different admissibility assumptions. Evidence for some CHR traits is incomplete.
System registers families (S1), then runs `Select` (S3) on a pinned `TaskSignatureRef`. Eligibility is tri-state; some families **abstain** due to missing minimal-evidence pins. Among remaining candidates, only a partial order is admissible, so the selector publishes one `Shortlist` with explicit `basisPins` instead of inventing one scalar winner. No shadow acceptance logic appears in the selector; it consumes pinned acceptance and legality records.

**Show 2 (specialist handoff; ranked publication).**
A bounded-specialization comparison keeps two method families live, but downstream handoff now requires one ordered public result rather than one merely unordered retained set.
The admissible `G.5` result is therefore one `RankedShortlist` with explicit ordering, `ShortlistId`, and handoff-facing `nextUse`, so the publication itself states whether the order is public.

**Show 3 (no admissible survivor; abstain or escalation).**
A frame fails one legality gate and one minimal-evidence gate at the same time.
The truthful `G.5` result is one abstain or escalation publication that names the blocking pins and the next downstream use posture, not one empty shortlist that leaves downstream users unsure whether selection silently failed or admissibly stopped.

### G.5:6 - Bias-Annotation

Potential biases and failure modes this pattern explicitly guards against:

* **Monoculture bias (single Tradition dominance by default).** Mitigation: registry requires explicit eligibility/assurance records; selection is set‑returning under partial orders; method‑specific policies stay explicit pins rather than hard-coded defaults.
* **Hidden scalarisation bias.** Mitigation: set‑return semantics is core‑routed; dominance regimes are explicit and each default cites one declared governing definition.
* **“Tool equals method” bias.** Mitigation: notation independence + prohibition of tool keywords in core registry/eligibility fields; tool choices are outside the core.
* **Cross‑Context leakage bias.** Mitigation: explicit crossing pins only; Bridges + CL are required when crossings occur; no implicit crossings.
* **Survivorship bias in refresh.** Mitigation: RSCR triggers are typed/id‑based; freshness/decay and telemetry deltas are first‑class causes with canonical ids.

### G.5:7 - Conformance Checklist (normative)

| ConformanceId   | Statement |
| --------------- | ----------|
| `CC‑G5‑CoreRef` | **Core conformance bridge.** `G.5` is conformant only if the **effective** `G.Core` obligations referenced by `G.5:4.1 (GCoreLinkageManifest)` are satisfied (after profile/set expansion and explicit deltas). |
| `CC‑G5.0`       | Core standards **SHALL** remain notation‑independent; vendor/tool keywords are forbidden in registry, eligibility, assurance, or selector‑kernel obligations (E.5.*). |
| `CC‑G5.1`       | Every `MethodFamily` **SHALL** declare an `EligibilityStandardRef` using CHR/CAL terms (typed; edition‑pinned where applicable). Standards **SHALL NOT** rely on tool‑specific keywords.  |
| `CC‑G5.2`       | Selection **SHALL** be a pure function of `TaskSignatureRef` + pinned policy/edition refs; side effects are limited to emitting DRR/SCR pins and telemetry/RSCR triggers (no hidden mutation of constraint-bearing spec refs). |
| `CC‑G5.3`       | **Delegated (ID‑continuity).** Cross‑Context use **MUST** follow `G.Core` crossing visibility and penalty routing. **Delegation targets:** `CC‑GCORE‑CROSS‑1`, `CC‑GCORE‑PEN‑1`.  |
| `CC‑G5.4`       | **Default rule for** `DefaultId.GammaFoldForR_eff`. The selector **MUST** default to the weakest‑link rule for `R_eff` and record contributors in SCR; it **MAY** use an alternative Γ‑fold only when provided by an explicitly pinned policy/profile with proof obligations satisfied (monotonicity; boundary behavior). |
| `CC‑G5.5`       | Ordinal scales **MUST NOT** be averaged/subtracted; any aggregation/comparison must respect CHR scale typing and legality constraints (incl. CSLC where applicable). |
| `CC‑G5.6`       | Method and generator family identities **SHALL** be published to UTS with the required naming discipline (twin labels where applicable; deprecations follow lexical continuity rules). *(Core conformance applies; `G.5` adds the registry‑specific publication obligation.)* |
| `CC‑G5.7`       | **Conditional.** If `G.5:Ext.EELog` is present, exploration **MUST** be budgeted under the pinned E/E‑LOG policy; probe outcomes **MUST** feed refresh via canonical RSCR trigger kinds. |
| `CC‑G5.8`       | **CG‑Frame gate enforced.** Selection rejects or abstains from candidates that do not meet the pinned `CG‑Spec.MinimalEvidence` requirements for the characteristics they cite. |
| `CC‑G5.9`       | **Delegated (ID‑continuity).** Set‑return semantics are pinned through `G.Core`. **Delegation target:** `CC‑GCORE‑SET‑1`. Candidate ordering **MUST** be admissible over typed traits and legality constraints. If only a partial order is available, selection **MUST** return one declared selector outcome (for example one `SetSurfaceOutcome` with `Shortlist`/`RankedShortlist`, one `HandoffOutcome` with `SpecialistHandoff`, or another pinned outcome result), with no forced totalisation via illegal scalarisation. |
| `CC‑G5.10`      | **SCR completeness.** SCR **MUST** enumerate Γ‑fold contributors (when used), referenced constraint-bearing spec editions, the evidence citations (`PathId/PathSliceId`) used in gating/rationale, and `MinimalEvidence` gating verdicts *(by lane & carrier, when such gating is relied upon).* |
| `CC‑G5.11`      | **Delegated (ID‑continuity).** Tri‑state eligibility/acceptance semantics and unknown handling are pinned through `G.Core`. **Delegation target:** `CC‑GCORE‑GUARD‑1`. *(Includes the rule that `degrade(...)` is expressed via a pinned FailureBehavior/SoS‑LOG branch id — not as a fourth status.)* |
| `CC‑G5.12`      | **No “universal” cross‑Tradition scoring.** Cross‑Tradition selection **MUST NOT** rely on a single numeric formula not justified by pinned CHR/CAL constraints and the constraint-bearing spec refs. If a triad or selected set **claims universality**, it **MUST** satisfy **explicit, pinned** heterogeneity gates (ids/pins), e.g., `FamilyCoverage ≥ k` and `MinInterFamilyDistance ≥ δ_family`, where `k` and `δ_family` are declared by the pinned policy/TaskSignature/SoTA pack, and cite the relevant **Context Card id (F.1)** in DRR/SCR; otherwise treat the outcome as Context‑local.  |
| `CC‑G5.13`      | **Conditional.** If the selector consumes admissibility/maturity records (e.g., via `G.5:Ext.SoSLOG`), it **MUST NOT** recompute thresholds; it consumes pinned admissibility ledger rows and cites clause/rung ids in audit pins. |
| `CC‑G5.14`      | **Φ(CL) / Φ_plane discipline.** If crossing or plane penalties are applied, the active penalty policy ids (e.g., `Φ(CL)`, `Φ_plane`) **MUST** be explicit in audit pins, and the pinned policies **MUST** satisfy the monotone & bounded requirements asserted by their cited constraint-bearing spec refs and be published via those same cited spec refs (e.g., `CG‑Spec`). SCR **MUST** record the policy‑id in use; penalty routing semantics remain pinned through `G.Core`. |
| `CC‑G5.15`      | Unit and scale legality **MUST** be established via CSLC (A.18) before any aggregation or Γ‑fold; unit and scale mismatches are a fail‑fast defect. |
| `CC‑G5.16`      | Hidden thresholds are forbidden. Thresholds live in explicitly pinned acceptance/eligibility policy records, not in selector prose, LOG shells, or code.  |
| `CC‑G5.17`      | ReferencePlane **MUST** be declared (pinned) for any claim that is used in dispatch, and the selector’s audit records must cite it (including plane‑crossing pins when applicable). |
| `CC‑G5.18`      | Numeric comparisons/aggregations used by dispatch **MUST** cite an admissible, edition‑pinned comparator/spec publication (as provided by the constraint-bearing spec refs); illegal mixes of scale types are forbidden. |
| `CC‑G5.19`      | **Conditional (QD).** If `G.5:Ext.NQD` is present, the required QD telemetry triple (quality/diversity/QD summary) **MUST** be computable and publishable under the pinned descriptor/distance definitions and archive policy, without redefining their semantics in G.5. |
| `CC‑G5.20`      | **Conditional (QD).** QD/illumination summaries are treated as telemetry unless explicitly promoted by a pinned acceptance/policy record; the selector must record the promoting policy id in audit pins. |
| `CC‑G5.21`      | **Conditional (Archive/QD).** Any use of archives **MUST** declare `InsertionPolicyRef` and pin the required editions for reproducibility (e.g., descriptor/distance definitions and any method editions they depend on).  |
| `CC‑G5.22`      | **Conditional (QD).** Twin‑naming discipline for descriptor vs plain space (if used) must be respected (distinct objects; no aliasing).  |
| `CC‑G5.23`      | **Default rule for** `DefaultId.PortfolioMode`. The selector **MUST** expose `PortfolioMode ∈ {Pareto, Archive}` with **default = `Archive`**, and echo it in DRR/SCR and declared selector results when not explicitly overridden by pinned policy/TaskSignature. The default is a retention/evidence-preservation posture, not a public selected-set label, not a dominance default, and not a substitute for `SetSurfaceKind`. `ε`‑fronts are allowed as *local* decision aids under `CG‑Spec` when explicitly pinned.  |
| `CC‑G5.23a`     | **Parity‑run publication.** If parity harness is in use, a selector/generator **MUST** publish a parity run and `ParityCard` to **UTS** (see `G.9`). This obligation remains mandatory irrespective of dominance/`PortfolioMode` policy. |
| `CC‑G5.24`      | **Conditional (Open‑Ended).** If `G.5:Ext.OpenEndedFamilyWiring` is present, the selector **MUST** support declared sets of `{Environment, MethodFamily}` pairs as set‑valued outcomes under explicit pins. |
| `CC‑G5.25`      | **Conditional (Open‑Ended).** In Open‑Ended mode, `TransferRulesRef.edition` is mandatory and **MUST** be visible to telemetry and RSCR triggers.  |
| `CC‑G5.26`      | **Conditional (Archive/QD).** Within any archive niche/cell, ordering and tie‑breaks **MUST** remain admissible over compatible scales; illegal mixed‑scale weighted sums are forbidden. |
| `CC‑G5.27`      | If the selector cites any `GateCrossing`, the corresponding `CrossingBundle` publication **MUST** be present and conformant; missing/non‑conformant `CrossingBundle` blocks downstream consumption. |
| `CC‑G5.28`      | **Default rule for** `DefaultId.DominanceRegime`. `DominanceRegime` **SHALL** default to `ParetoOnly`. Any inclusion of additional telemetry dimensions into dominance (e.g., illumination) requires an explicitly pinned acceptance/policy record and must be recorded in audit pins. **Parity‑run publication (CC‑G5.23a) remains mandatory** irrespective of dominance policy. |
| `CC‑G5.29`      | **Conditional (QD/Open‑Ended).** Any telemetry event that materially changes an archive / retained-set state **MUST** log `PathSliceId`, the active policy id, and the active editions of the relevant definition pins (`DescriptorMapRef.edition`, `DistanceDefRef.edition`, and `TransferRulesRef.edition` when applicable) and expose them to RSCR triggers. |
| `CC‑G5.30`      | **No Strategy minting.** Within `G.5`, “strategy” is a policy‑bound composition template; the pattern **SHALL NOT** mint a new universal `U.Type` named `Strategy` (E.10 discipline). If a stable reference is needed, publish composition/policy ids (e.g., UTS entries) rather than minting a universal type. |
| `CC‑G5.31`      | **Strategy hint on non‑admissible sets.** If selection yields `CandidateSet = ∅`, the selector **SHALL** emit an explicit escalation hint (`ActionHint`) that is **DRR/SCR‑compatible** and auditable: include (at minimum) the top‑3 blocking constraints as cited ids/pins, and (where applicable) the relevant edition pins (e.g., `TransferRulesRef.edition` in Open‑Ended mode) to guide exploration under explicitly pinned lenses (e.g., E/E‑LOG). |
| `CC‑G5.32`      | **Parity‑run publication + admissible roll‑ups.** If parity harness is in use, parity publication is required per `CC‑G5.23a` (ID‑continuity). Any scalar roll‑up or summary view **MUST** be admissible under **CG‑Spec** (no mixed‑scale sums), and published views must preserve set‑return semantics (no single‑score leaderboards as authoritative outputs without an explicit, admissible comparator publication). |
| `CC‑G5.33`      | **Conditional (bounded specialization).** When the selection question is acquisition of usable specialization on a declared `TaskFamilyRef` or `TaskSignature`, selector outputs **SHALL** either publish `TaskFamilySpecializationProfile@Context` or cite equivalent pins carrying the `C.22.1` adaptation-signature fields needed for comparison: work-measure threshold target, prior exposure declaration, time-to-threshold, budget-to-threshold, post-threshold efficiency when relevant, and any declared transfer, retention, downside, or specialization-entry notes. |
| `CC‑G5.34`      | **Selected-set publication label.** When `SelectorOutcomeKind = SetSurfaceOutcome`, the published selected-set label **MUST** be explicit. Use `Shortlist` as the public selected-set label, `RankedShortlist` only when ordering materially belongs to the result, publish `ShortlistId` when one public identifier is emitted, and do not silently let `ChoiceSet` replace that public label. |
| `CC‑G5.34a`     | **Selector outcome typing.** Published selector results **MUST** declare `SelectorOutcomeKind`. `SetSurfaceKind` is required only when `SelectorOutcomeKind = SetSurfaceOutcome`; `HandoffKind` is required only when `SelectorOutcomeKind = HandoffOutcome`. Non-set outcomes **MUST NOT** masquerade as one public selected-set label. |
| `CC‑G5.35`      | **Publication closure.** Any published selector result **MUST** state the declared `SelectorOutcomeKind`, any applicable public selected-set label, retained members or narrowed handoff content, ordering status (when applicable), and basis pins directly in the emitted result rather than relying on upstream `C.11`, `C.19`, or `C.24` notes. |
| `CC‑G5.36`      | **Neighboring-pattern boundary.** If the current question is still local choice among already-available options, pool policy over still-live candidate lines, or enactment planning after choice, `G.5` **MUST** consume the published result from `C.11`, `C.19`, or `C.24` rather than restating those patterns as if publication itself decided the matter. |
| `CC‑G5.37`      | **Derived tradition-view publication discipline.** If the selector publishes one result through a derived tradition view such as `TraditionFront` or `TraditionArchive`, it **MUST** keep the declared base `SourceSurfaceKind` explicit, keep `SoTAPaletteDescription` recoverable through `BasePaletteRef`, and **MUST NOT** let the derived view become the default meaning of `Tradition`, `TraditionPalette`, or the base palette. |
| `CC‑G5.38`      | **Causal method dispatch declarations.** If method selection involves causal methods, each compared method **MUST** declare `causalMethodComparisonPosture` as observational predictor, intervention optimizer, counterfactual strategy, causal fairness estimator, causal-RL policy, or simulation-only method, and **MUST** carry `causalUseSupportRecordRef` and `causalUseSupportVerdict` when it consumes `C.28` causal-use support rather than treating method dispatch as causal certification. |


### G.5:8 - Common Anti-Patterns and How to Avoid Them

* **Anti‑pattern: “Selector as a shadow spec.”**
  *Symptom:* local acceptance/legality rules appear in selector prose/code, diverging from CN/CG/CAL.
  *Avoid:* route all constraint semantics via `CNSpecRef/CGSpecRef` and pinned CAL records; keep G.5 core as a facade.

* **Anti‑pattern: “Implicit crossings.”**
  *Symptom:* cross‑Context reuse is claimed without Bridge/CL pins, or without cited `CrossingBundle`.
  *Avoid:* require explicit crossing pins; block consumption without publication.

* **Anti‑pattern: “Hidden scalarisation.”**
  *Symptom:* partial orders are flattened into single winners “for convenience”.
  *Avoid:* return declared sets; make dominance regimes explicit; keep telemetry report‑only unless promoted by explicit policy.

* **Anti‑pattern: “Method specifics in the selector head.”**
  *Symptom:* QD/OEE/preference models become mandatory for basic dispatch.
  *Avoid:* keep them in `G.5:Ext.*` blocks with explicit pins and `Uses`.

* **Anti‑pattern: “Churn by meaning.”**
  *Symptom:* registry entries are “renamed” to reflect updated interpretation, breaking continuity.
  *Avoid:* version/deprecate; keep stable ids; use explicit edition pins and deprecation notices.

* **Anti‑pattern: “Publication hidden in upstream reasoning.”**
  *Symptom:* the retained set exists only as one implication inside `C.11`, `C.19`, or `C.24`, while `G.5` never names the published selected-set label.
  *Avoid:* publish the selected-set result directly, with explicit label, members, and basis pins, instead of leaving the shortlist implicit in neighboring doctrine.

* **Anti‑pattern: “Published result without closure record.”**
  *Symptom:* a `Shortlist`, narrowed handoff, or abstain result is named, but the emitted result still does not state its members, ordering status, or basis pins.
  *Avoid:* publish the head, retained members, ordering status, abstain or escalation condition, and basis pins directly in `G.5`.

### G.5:9 - Consequences

* **Auditable plurality.** Multiple Traditions can co-exist without forced semantic flattening; dispatch remains explainable and evidence-pinned.
* **Core stability.** Universal invariants are pinned through `G.Core`; method/generator innovation does not churn the selector head.
* **Evolvability.** Registries support growth, retirement, and refresh with typed RSCR causes and explicit payload pins.
* **Composability.** Strategy templates and fallbacks remain legality-checked and portable across implementations.
* **Recoverable publication.** Selected-set results can now travel downstream as explicit shortlist-family, ranked-shortlist, or abstain/escalation results rather than one hidden implication inside upstream reasoning.

### G.5:10 - Rationale

* **Why registries?** Dispatch requires stable, auditable family objects with explicit eligibility and assurance records; otherwise selection collapses into ad-hoc tooling.
* **Why separation via Extensions?** QD/OEE/preference-learning and similar families are fast-moving and method-specific; making them part of the selector head would force a universal semantics and violate strict distinction.
* **Why set-return?** Partial orders are common and often the only admissible representation under heterogeneous scales; set-return preserves semantics and makes tie criteria explicit.
* **Why explicit defaults with one declared source?** Defaults are unavoidable; single-source indexing prevents competing defaults from silently diverging across patterns.
* **Why selected-set publication here?** Once the current question is to publish one retained set for downstream use, the selector should publish that result directly instead of leaving it implicit in local choice, pool-policy, or enactment notes written for other purposes.

### G.5:11 - SoTA-Echoing

This pattern is designed to carry extension declarations for, not redefine, post-2015 SoTA families via `Uses` plus edition and policy pins:

* **Quality-Diversity / illumination (post-2015 refinements).** Archive-centric QD families fit naturally as `G.5:Ext.NQD` extension declarations with explicit descriptor, distance, and insertion pins. The practical implication is to keep publication honest about whether the selector is returning one admissible set, one ranked result, or no admissible survivor at all.
* **Open-Endedness (post-2015 line).** POET-class and later open-ended or co-evolutionary families dock via generator registries plus `TransferRulesRef.edition` pins. The practical implication is to publish pair- or retained-set-shaped results explicitly rather than silently squeezing them into one false single-family winner.


* **Algorithm selection and meta-selection.** Modern selection under uncertainty, robust evaluation, and policy-driven probing dock via explicit policy records and typed telemetry pins, rather than hard-coded scoring rules. The practical safeguard is that the publication label and basis pins must still remain explicit after those policies have acted.
* **Budgeted specialist acquisition.** Current agentic search lines compete on time or budget to threshold plus truthful selected-set return when heterogeneous specialists remain non-dominated, so `G.5` keeps specialization profiles and set-return semantics explicit instead of forcing one static breadth winner.
* **Preference-learning comparators.** Interactive and learned-preference regimes are treated as comparator or policy records with explicit editions when they are actually declared.

SoTA here is treated as **best-known practice for a declared goal and constraint regime**, not whatever is currently popular.
Evidence-source clarification: peer-reviewed anchors carry the most direct support for typed comparison, budget-to-threshold, and truthful selected-set return. Faster-moving workshop, poster, or frontier-exploration lines remain explicit support for specialization-entry or open-ended pressure, not silently equal evidence for every selector claim.

### G.5:12 - Relations

**Builds on (normative):** `G.Core` (core invariants + linkage discipline).

**Uses (conceptual dependencies; cited via pins/ids):**

* Governing spec refs: `A.19 (CN‑Spec)`, `G.0 (CG‑Spec)`.
* Upstream object sets: `G.1 (CG‑Frame Card)`, `G.2 (SoTA Pack)`, `G.3 (CHR Pack)`, `G.4 (CAL Pack)`.
* Evidence & crossings: `G.6 (EvidenceGraph; PathId/PathSliceId)`, `G.7 (Bridge/CL calibration)`, `E.18/A.21 (CrossingBundle/GateChecks)`.
* Planning/enactment boundary: `A.15.3 (SlotFillingsPlanItem)` as the planned baseline anchor (cited, not redefined).
* Causal-use method dispatch: `C.28` when method selection involves causal effect, counterfactual comparison, causal fairness, causal policy, causal RL, or simulation-only causal-use claims.
* Optional method/generator extensions via `G.5:Ext.*`: `C.18`, `C.19`, `C.23`, plus any future extension-bearing patterns that add extra selector pins.
* Mathematical-lens adequacy: open `C.29` when a selector input depends on a load-bearing comparator, distance, descriptor geometry, embedding, normalization, surrogate model, learned representation, QD archive descriptor, model-family label, or model-selection basis whose mathematical object, mapping mode, preserved/lost structure, or stop condition is not yet recoverable. `C.29` may return `NoMLANeeded`, `MLA.LensCandidateNote`, `MLA.OneLine`, `MLA.MiniCard`, `MLA.FullCard`, or `NeighborGoverningLocusNote` for the stated selector use. It does not publish the selected set, selector policy, registry row, shortlist, ranked shortlist, or selector evidence pins; those stay in `G.5` and its governing refs.


**Publishes to:** `UTS` (family ids, selector policy records, and selected-set identities such as `ShortlistId` when one public result is emitted), `G.6` (audit citations), RSCR emission records (typed triggers + payload pins), and downstream packs via `G.10` shipping surfaces.

**Coordinates with:** `C.11` for local choice results, `C.19` for pool-policy records, `C.24` for enactment-facing next-move records, and the accepted Q-Front shortlist-family continuity line when the published selected-set label is one shortlist-family result.

### G.5:End
---

## G.6 - Evidence Graph & Provenance Ledger

**Tag.** Architectural pattern
**Stage.** design‑time (assembly) + run‑time (telemetry ingestion)
**Primary output.** A notation‑independent `EvidenceGraph` + a stable `PathId` / `PathSliceId` citation surface + an SCR projection (“Assurance SCR”) suitable for audit, selection explainability, and refresh/RSCR wiring.
**Primary hooks.** A.10 (evidence anchors/carriers; SCR/RSCR anchoring), B.3 (assurance lanes and `F/G/R` skeleton), F.9 (BridgeCard/CL), G.4 (CAL `EvidenceProfiles` + `ProofLedger` linkage), `G.Core` (Part‑G invariants, RSCR trigger catalogue, default-governing-definition index), E.18/A.21 (GateCrossing + CrossingBundle checks), F.17 (UTS publication), F.15 (RSCR), E.10 (LEX), E.5.* (notation‑independence discipline).
**Non‑duplication note.** Universal Part‑G invariants (no shadow specs; Bridge‑only crossings; tri‑state discipline; penalties→`R_eff` only; P2W split; typed/id‑based RSCR causes; defaults with one governing definition; Δ‑discipline) are governed by `G.Core` and are *cited* via `CC‑GCORE‑*`. This pattern defines only the *EvidenceGraph kit* and its path‑addressable provenance surfaces.

### G.6:1 - Problem frame

SoTA claims, operators, and method families are admitted (or gated) using assurance signals derived from diverse artefacts and anchors. FPF already mandates **Evidence Graph Referring** (A.10), lane discipline, and the assurance skeleton (B.3). What is often still missing in practice is a *first‑class, citable* object that makes the provenance of an admission/decision **addressable**:

* *exactly which* anchors and bindings were used,
* *under which* `ReferencePlane` and `BoundedContext`,
* *with which* explicit crossings and penalty policies,
* *for which* time window (freshness/decay),
* in a way that selectors, audits, and maturity transitions can cite without copying tables or re‑telling a story.

This pattern introduces the missing kit: a typed, lane‑aware `EvidenceGraph` plus stable `PathId` / `PathSliceId` addresses that downstream LOG, UTS, parity, and refresh can cite.

**Why here (not in G.4)?** G.4 governs CAL artefacts (EvidenceProfiles, ProofLedger, acceptance policies). G.6 packages *cross‑artefact provenance* as a graph and mints *path identities* that downstream surfaces can cite without duplicating CAL tables or re‑inventing legality rules.

### G.6:2 - Problem

1. Readers cannot reliably **audit crossing/penalty and decay impacts** on claims without chasing many tables and informal narratives.
2. Cross-Context or cross-plane reuse must remain **Bridge‑only and explicit**, but provenance often hides crossings (or treats them as “obvious”).
3. Selection and maturity decisions need a stable **path address** to re‑check later, including after edition/policy/freshness changes.

### G.6:3 - Forces

| Force                        | Tension                                                                             |
| ---------------------------- | ----------------------------------------------------------------------------------- |
| **Provenance vs agility**    | Fine‑grained audit trails ↔ friction for authors.                                   |
| **Lane purity vs synthesis** | Keep TA/VA/LA separable ↔ publish a unified justification surface.                  |
| **Notation independence**    | Semantics in prose/math ↔ teams want diagrams/tables (informative only).            |
| **Design vs run**            | Design‑time evidence assembly ↔ run‑time telemetry ingestion must not be conflated. |
| **Crossings and planes**     | Crossings must be explicit and penalised correctly ↔ authors want “just reuse it”.  |

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

### G.6:5 - Archetypal Grounding (System / Episteme)

**System (Γ_sys):** *Autonomous brake envelope claim.*
Claim: “Stop within 50 m from 100 km/h.” EvidenceGraph nodes include proof carriers (TA/VA), instrumented track tests (LA/VA), calibration carriers, and an external test lab as an external evidencing role (no self‑evidence). A `PathId` provides a stable justification address; empirical legs are bound to explicit windows; crossings (if any) are explicit and pinned.

**Episteme (Γ_epist):** *Benchmark parity/replication lineage (post‑2015 practice).*
Claim: “Method family M attains parity on ImageNet‑style tasks under a declared evaluation protocol.” EvidenceGraph nodes include replication carriers (LA), legality/metric‑soundness carriers (VA), and tool‑qualification carriers (TA). The cited `PathId` binds the `ReferencePlane`, the scope slice, and the pinned evaluation/legal surfaces (by edition/policy ids rather than prose). When refresh triggers occur (edition pin change, evidence surface edit, decay events), downstream artefacts can re‑cite or re‑compute using the same `PathSliceId` addressing discipline.

### G.6:6 - Bias‑Annotation

Lenses tested: **Gov**, **Arch**, **Onto/Epist**, **Prag**, **Did**.
Scope: Universal for the EvidenceGraph kit; any method‑specific telemetry / `PortfolioMode` wiring is modularized as Extensions and cited to its governing patterns.

### G.6:7 - Conformance Checklist (normative) — **CC‑G6**

| ConformanceId                                     | Requirement                                                                                                                                                                                                                                                                                                                                                                  | Purpose |
| ------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------- |
| **CC‑G6‑CoreRef**                                 | `G.6` is conformant only if it satisfies the **effective** `CC‑GCORE‑*` set expanded from the `GCoreLinkageManifest` in **§4.1** (explicit crossings & pins, penalties→`R_eff` only, P2W split, typed RSCR trigger kinds, defaults with one governing definition, UTS discipline, Δ‑discipline).                                                                                                 | Cite core invariants |
| **CC‑G6‑1 (Anchor & lanes)**                      | Every citable path MUST resolve to A.10 anchors (SCR/RSCR addressable) and MUST declare lane tags (`TA/VA/LA`) on bindings.                                                                                                                                                                                                                                                | Ground auditability |
| **CC‑G6‑2 (No self‑evidence)**                    | Any evidencing `TransformerRole` that certifies the evaluated holon is external; reflexive cases MUST be modelled as a meta‑holon.                                                                                                                                                                                                                                         | Avoid reflexive evidence |
| **CC‑G6‑3 (Context/Plane & crossings)**           | Paths MUST declare `BoundedContext` and `ReferencePlane`, and MUST expose explicit crossing pins when crossings are present. *(Delegation target: `CC‑GCORE‑CROSS‑1`.)*                                                                                                                                                                                                    | Make crossings explicit |
| **CC‑G6‑4 (Penalty routing)**                     | Any crossing/plane penalty wiring visible in G.6 artefacts MUST route penalties to `R_eff` only and MUST preserve `F/G` invariance under penalties. *(Delegation target: `CC‑GCORE‑PEN‑1`.)*                                                                                                                                                                             | Preserve lane purity |
| **CC‑G6‑5 (Γ‑fold discipline + Default Governing Definition Index)** | If a `Γ‑fold` is not explicitly overridden by pinned CAL artefacts, G.6 MUST cite the governing definition of `DefaultId.GammaFoldForR_eff` rather than asserting a local default. If a `Γ‑fold` is explicitly overridden, the path/SCR surface MUST cite the relevant CAL `ProofLedger` ids and publish the override as an auditable pin (not as prose). *(Delegation: `CC‑GCORE‑DEF‑1`; override semantics governed by `G.4`.)* | Keep folding auditable |
| **CC‑G6‑6 (Time/decay/validity binding)**         | Empirical legs MUST expose freshness/time binding (window selector or policy pin) and MUST support an explicit `validUntil`/expiry marker when one is declared (or an equivalent decay/freshness policy pin that implies expiry). Expiry/decay MUST be representable as refresh/RSCR‑relevant change using typed canonical causes. *(Delegation intent: typed causes are governed by G.Core; see `CC‑GCORE‑TRIG‑*`.)*                                  | Enable refresh readiness |
| **CC‑G6‑7 (DesignRunTag split)**                    | Design‑time method descriptions and run‑time work traces MUST NOT be fused into one undifferentiated node; the graph MUST preserve the design↔run boundary via explicit carriers/bridges. *(Delegation intent: P2W split is governed by G.Core; see `CC‑GCORE‑P2W‑1`.)*                                                                                                            | Preserve P2W boundary |
| **CC‑G6‑8 (SCR projection completeness)**         | For any cited `PathId/PathSliceId`, the Assurance SCR view MUST expose at least: lane split, scope/plane pins, freshness/validity binding, explicit crossing pins (and the effective bottleneck `CL`/`CL^k`/`CL^plane` when crossings exist), the effective `Γ‑fold` in force for any `R_eff` folding (default or override, plus CAL `ProofLedger` ids when overridden), and links to contributing A.10 anchors and any CAL evidence/profile refs. | Make decisions auditable |
| **CC‑G6‑9 (Citable PathIds)**                     | Any SoS‑LOG admit/degrade/abstain decision or maturity rung transition that relies on provenance MUST cite `PathId`(s) (or `PathSliceId`(s) when snapshot‑binding is required).                                                                                                                                                                                            | Decision traceability |
| **CC‑G6‑10 (SpanUnion justification note)**       | If a SpanUnion/non‑interaction claim is made across evidence lines, an explicit independence justification MUST be published (as an addressable artefact linked to the path).                                                                                                                                                                                                | Non‑interaction audit |
| **CC‑G6‑11 (UTS hooks)**                          | Evidence carriers and paths minted for citation MUST be UTS‑citable with twin labels and edition pins. *(Delegation target: `CC‑GCORE‑UTS‑1`.)*                                                                                                                                                                                                                           | Stable citations |
| **CC‑G6‑12 (IndependenceCertificate)**            | Independence for SpanUnion claims MUST be carried by an `IndependenceCertificate` (per the relevant certificate pattern) and referenced from SCR/paths.                                                                                                                                                                                                                    | Certificate surface |
| **CC‑G6‑13 (Mandatory provenance pins)**          | Any published/cited path surface MUST expose: `EvidenceGraphId`, `PathId/PathSliceId`, lane split, scope/plane pins, freshness/validity pins when applicable, crossing pins when applicable, and the minimal pin set required by §4.1. When `R_eff` folding is published/relied upon, the effective `Γ‑fold` in force MUST be exposed (default or override, plus CAL `ProofLedger` ids when overridden). When QD/OEE telemetry pins are in use, the extension‑required edition/policy pins MUST also be exposed. | Pin completeness |
| **CC‑G6‑14 (Legality binding; no shadow specs)**  | If numeric operations are cited/used in a path, legality MUST be pinned/cited via `CG‑Spec` rather than asserted locally, and the path/SCR surface MUST fail fast on illegal arithmetic/typing (e.g., CSLC/scale violations); do not “promote” ordinal to cardinal by convention inside G.6. *(Delegation target for “no shadow specs”: `CC‑GCORE‑CN‑CG‑1`.)*                                                                                     | Prevent illicit arithmetic |
| **CC‑G6‑15 (Conditional: QD/OEE telemetry pins)** | *(Conditional)* If `G.6:Ext.QD_OEE_TelemetryPins` is used, the required edition/policy pins from that extension (at minimum `DescriptorMapRef.edition`, `DistanceDefRef.edition`, and the relevant insertion/emitter/transfer policy pins when applicable) MUST be recorded for reproducibility and must participate in RSCR triggering using canonical trigger kind ids.                                                                 | Reproducible archive/OEE |

### G.6:7.5 - Interfaces & Hooks (normative)

Each hook below defines: **Trigger → Obligation → Publishes/Consumes → Invariants**.
Where universal invariants apply (crossings, penalties, trigger typing), this section *cites* `G.Core` rather than redefining semantics.

#### G.6:7.5.1 - H1 — UTS Name Card for EvidenceGraph Nodes

* **Trigger.** A new EvidenceGraph node is minted for an A.10-anchored evidence carrier or evidence role.
* **Obligation.** Mint a UTS Name Card with twin labels (Tech/Plain), citing the declared bounded-context anchor and any required edition pins.
* **Publishes/Consumes.** Publishes: UTS row. Consumes: A.10 anchor metadata.
* **Invariants.** UTS publication and any deprecation/aliasing follow the delegated UTS discipline through `G.Core` and `F.17`.

#### G.6:7.5.2 - H2 — UTS PathCard (PathId/PathSliceId)

* **Trigger.** A new `PathId` (or `PathSliceId`) is minted.
* **Obligation.** Publish a UTS PathCard with twin labels, listing the explicit pins required by §4.1 (context, plane, and time binding, crossing pins if any). If an extension requires additional pins for reproducibility (e.g., `G.6:Ext.QD_OEE_TelemetryPins`), those pins MUST be present when the extension is in use.
* **Publishes/Consumes.** Publishes: UTS row(s). Consumes: EvidenceGraph path metadata + any extension‑required pins.
* **Invariants.** Crossing visibility and penalty routing are delegated to `G.Core` (`CC‑GCORE‑CROSS‑1`, `CC‑GCORE‑PEN‑1`).

#### G.6:7.5.3 - H3 — RSCR Trigger on Evidence‑Impacting Edit (typed; alias‑dockable)

* **Trigger.** Any edit in G.6 that can change a path’s audit‑relevant surface (evidence structure, crossing pins, penalty policy pins, plane binding, freshness binding, edition/policy pins, or telemetry‑bound fields).
* **Obligation.** Emit RSCR triggers **using canonical `RSCRTriggerKindId`** (from `G.Core`) and record affected scope (`PathId/PathSliceId`) plus payload pins required for downstream refresh. If a deprecated `G.6:H3:*` label is recorded, it is recorded as an alias label and docked via `G.Core.TriggerAliasMap.G6`. When `G.6:Ext.BridgeSentinelWiring` is used, include the bridge/sentinel payload pins required by that extension.
* **Publishes/Consumes.** Publishes: RSCR triggers and any associated RSCR test ids. Consumes: relevant pins/refs and CAL artefact references where applicable.
* **Invariants.** Trigger typing and alias docking are delegated to `G.Core` (`CC‑GCORE‑TRIG‑*`). Penalty routing invariants are delegated (`CC‑GCORE‑PEN‑1`).

#### G.6:7.5.4 - H4 — SoS‑LOG Path Citation (selector explainability)

* **Trigger.** A SoS‑LOG rule yields a tri‑state decision for a selection‑relevant pair (e.g., `(TaskSignature, MethodFamily)`), and the decision is justified by evidence.
* **Obligation.** The branch record MUST cite the relevant `PathId/PathSliceId`(s) and the minimal pins required to re‑audit the justification. Any method‑specific attribution fields are handled via Extensions (e.g., `G.6:Ext.SoSLOGPathCitationWiring` for `LensId`/FailureBehavior wiring, `G.6:Ext.BridgeSentinelWiring` for bridge‑monitoring payload pins when cross‑context reuse is invoked, `G.6:Ext.QD_OEE_TelemetryPins` for QD/OEE pins).
* **Publishes/Consumes.** Publishes: an SCR‑visible branch record with cited paths. Consumes: EvidenceGraph path queries.
* **Invariants.** Tri‑state semantics are governed by G.Core (`CC‑GCORE‑GUARD‑1`); G.6 does not add a new decision value.

#### G.6:7.5.5 - H5 — Maturity Rung Transition Justification

* **Trigger.** A maturity rung transition is proposed and justified by evidence.
* **Obligation.** The transition MUST cite one or more `PathId/PathSliceId`(s) and MUST publish an updated maturity entry with those citations. Missing path citations forbid rung advance.
* **Publishes/Consumes.** Publishes: updated UTS entry for maturity artefacts. Consumes: cited paths and A.10 anchors.
* **Invariants.** Any thresholding policy remains governed by CAL/LOG governing definitions; G.6 provides citation, not policy.

#### G.6:7.5.6 - H6 — Bridge/CL Edge Annotation (GateCrossings)

* **Trigger.** An EvidenceGraph edge traverses a declared GateCrossing boundary (context/kind/plane/design↔run/edition).
* **Obligation.** Publish a CrossingBundle‑checkable crossing record with explicit crossing pins (UTS row id, Bridge id/card id if applicable, CL regime pins if applicable, and plane pins if applicable).
* **Publishes/Consumes.** Publishes: crossing row/pins. Consumes: GateCrossing metadata and Bridge artefacts (when present).
* **Invariants.** Crossing visibility is governed by G.Core (`CC‑GCORE‑CROSS‑1`); penalties routing is governed by G.Core (`CC‑GCORE‑PEN‑1`).

#### G.6:7.5.7 - H7 — ReferencePlane penalty policy publication (ids only)

* **Trigger.** A path binds across different reference planes.
* **Obligation.** Publish the relevant policy identifiers (ids only; not tables) required to audit plane effects, alongside the path’s pins.
* **Publishes/Consumes.** Publishes: SCR/UTS fields containing policy ids. Consumes: the governing definition’s policy registries as cited publications or records (do not duplicate tables).
* **Invariants.** Penalty routing is delegated (`CC‑GCORE‑PEN‑1`); no shadow specs (`CC‑GCORE‑CN‑CG‑1`).

#### G.6:7.5.8 - H8 — CrossingBundle exposure (E.18)

* **Trigger.** G.6 artefacts are exported for release or consumed by downstream patterns that require GateCrossing checks.
* **Obligation.** Provide harness‑readable ids/pins so GateCrossing checks can verify: required crossing records exist, lexical constraints hold, and crossing pins are explicit.
* **Publishes/Consumes.** Publishes: checkable ids/pins. Consumes: GateCrossing + lexical rules.
* **Invariants.** Crossing discipline and ID continuity are governed by G.Core (`CC‑GCORE‑CROSS‑1`, `CC‑GCORE‑ID‑*`).

#### G.6:7.5.9 - H9 — SCR surface for assurance provenance

* **Trigger.** A downstream artefact cites a path for audit/selection/maturity.
* **Obligation.** Expose the required provenance fields in SCR views: lane split, context or plane pins, freshness binding, crossing pins (when present), and links to A.10 anchors and CAL refs.
* **Publishes/Consumes.** Publishes: SCR view(s). Consumes: EvidenceGraph paths and cited artefacts governed by cited patterns.
* **Invariants.** Each cited default resolves to its governing definition (`CC‑GCORE‑DEF‑1`).

#### G.6:7.5.10 - H10 — ProofLedger linkage (CAL ↔ G.6)

* **Trigger.** A proof obligation or evidence role is attached to a claim and is represented in G.4 artefacts.
* **Obligation.** Link EvidenceGraph nodes/edges to CAL ProofLedger/EvidenceProfiles entries and to A.10 carriers via the minimal provenance edge vocabulary.
* **Publishes/Consumes.** Publishes: CAL proof refs as pins in the path explanation surface. Consumes: CAL artefacts.
* **Invariants.** G.6 does not redefine CAL proof semantics; it only cites them.

#### G.6:7.5.11 - H11 — Telemetry ingest (selector & probe outcomes)

* **Trigger.** Run‑time outcomes (selection, probes, parity runs, measurement updates) produce observations that bear on previously asserted claims.
* **Obligation.** Ingest the observation as a run‑time evidence line (anchored in A.10), with explicit lane typing and explicit scope/time binding. If method‑specific telemetry pins are required, they are governed by Extensions (e.g., `G.6:Ext.QD_OEE_TelemetryPins`).
* **Publishes/Consumes.** Publishes: new EvidenceGraph nodes/edges + any required UTS rows + typed RSCR triggers when impacts occur. Consumes: run‑time carriers/attestations as conceptual anchors.
* **Invariants.** P2W split is respected (`CC‑GCORE‑P2W‑1`); typed trigger discipline is respected (`CC‑GCORE‑TRIG‑*`).

#### G.6:7.5.12 - Minimal conformance (hooks)

1. UTS publication for minted evidence artefacts and paths (H1–H2), per delegated UTS discipline.
2. Typed RSCR triggers on evidence‑impacting edits (H3) using canonical trigger kind ids.
3. LOG and maturity artefacts cite paths when evidence is used (H4–H5).
4. GateCrossing/crossing records are explicit and checkable when crossings occur (H6–H8).
5. SCR views expose the minimal provenance pins for cited paths (H9–H10).
6. Run‑time telemetry is ingested without collapsing design↔run boundaries (H11).

### G.6:8 - Common Anti-Patterns and How to Avoid Them

* **Narrative‑only provenance (“because story”).**
  **Avoid:** mint `PathId/PathSliceId` and require citation for any decision that claims evidence‑based justification (CC‑G6‑9).
* **Implicit crossings (“same entity, different context”).**
  **Avoid:** represent crossings only via explicit crossing artefacts/pins; treat edition/plane/context changes as explicit crossing‑relevant edits and trigger RSCR (governed by G.Core crossing discipline).
* **Smuggling legality rules into EvidenceGraph prose.**
  **Avoid:** cite/pin legality surfaces (`CG‑Spec` and CAL artefacts); do not introduce local “mini‑CG” rules in G.6 (cite `CC‑GCORE‑CN‑CG‑1`).
* **Unpinned editions/policies (“it’s obvious which version”).**
  **Avoid:** require explicit edition/policy pins on citable paths; treat changes as typed triggers.
* **Alias‑only RSCR causes (“H3: something changed”).**
  **Avoid:** record canonical `RSCRTriggerKindId` as the cause; aliases are labels only and must dock via `G.Core.TriggerAliasMap.G6`.

### G.6:9 - Consequences

**Benefits.** Path‑addressable provenance; crossing/plane effects are auditable by pins rather than folklore; selectors and auditors read the same path-addressable evidence graph; refresh becomes localized (path‑scoped) rather than global “rerun everything”.
**Trade‑offs.** Authors must declare (or pin) time/plane/scope and keep pins explicit; mitigated by reusing CAL EvidenceProfiles and by modularizing method‑specific telemetry as Extensions.

### G.6:10 - Rationale

G.6 concretizes the “because‑graph” implicit in A.10 into a typed, lane‑aware DAG with stable path addresses. It relies on canonical governing definitions for semantics:

* A.10 for anchoring discipline and carrier reality,
* B.3 for the assurance skeleton,
* G.4 for proof/evidence profile semantics,
* `G.Core` for universal crossing, penalty, Default Governing Definition Index, and typed RSCR cause discipline.

This preserves conceptual modularity: G.6 standardizes *addressable provenance*, not a competing legality or selection mechanism.

### G.6:11 - SoTA‑Echoing

This pattern aligns with post‑2015 best practice in reproducibility and evaluation governance by:

* treating **provenance and versioning/pinning** as first‑class audit surfaces (rather than informal “methods” prose),
* enabling **selective re‑evaluation** (path‑scoped refresh) rather than global reruns whenever one policy/edition changes,
* separating **design‑time specifications** from **run‑time traces/telemetry**, matching modern reproducibility and “lineage” practice in complex ML/scientific pipelines,
* keeping **method‑family specifics** (e.g., archive/illumination/QD pins or open‑ended telemetry pins) modular via extension wiring instead of embedding them into the universal provenance core.

### G.6:12 - Relations

**Builds on:** `G.Core`, `A.10` (evidence anchors/carriers; SCR/RSCR), `B.3` (assurance skeleton), `F.9` (BridgeCard/CL), `G.4` (CAL EvidenceProfiles/ProofLedger), `E.18/A.21` (GateCrossing/CrossingBundle checks), `E.10` (lexical rules), `E.5.*` (notation independence), `F.17` (UTS), `F.15` (RSCR).
**Publishes to:** UTS (Name Cards + PathCards), SCR/RSCR surfaces, downstream selectors/LOG by `PathId` citation, refresh/orchestration as typed triggers (consumed by `G.11` when used).
**Used by:** `G.5` (selector explainability and admissibility justifications), `G.8` (SoS‑LOG bundles), `G.9` (parity harness traces), `G.10` (shipping pins and audit payload), `G.11` (refresh orchestration).
**Constrains:** downstream patterns MUST cite paths when evidence is claimed; they MUST treat edits to pinned evidence/crossing/policy/edition/time bindings as refresh‑relevant causes with canonical trigger ids (governed by `G.Core`).

### G.6:End

## G.7 - Cross‑Tradition Bridge Calibration Kit (BridgeMatrix → BridgeCards + BCT/Sentinels)

**Tag.** Architectural pattern
**Stage.** design‑time (calibration + publication) + run‑time (sentinel‑driven telemetry emission; orchestration governed by **G.11**)
**Primary output.** A bridge calibration kit that turns **G.2**’s BridgeMatrix rows into **F.9** `BridgeCard`s and publishes: a `BridgeCalibrationTable (BCT)` + `CalibrationLedger` + `RegressionSet` + `SentinelSet`, plus UTS‑visible crossing rows and RSCR‑ready sentinel triggers scoped to `PathSliceId` / `PatternScopeId`.
**Primary hooks.** `G.Core` (Part‑G invariants + RSCR trigger catalogue + Default Governing Definition Index), **G.2** (BridgeMatrix), **F.9** (BridgeCard + CL/CL^k), **F.3/F.7** (SenseCell anchoring; row bottleneck discipline), **E.18/A.21** (GateCrossing + CrossingBundle checks), **G.6** (PathId/PathSliceId citation surface), **G.5** (downstream consumer for eligibility/selection), **G.11** (refresh orchestration consumer), **B.3** (assurance lanes + penalty policies), **C.21** (DHC accounts such as AlignmentDensity), **C.18 and C.19** (QD/OEE pins when relevant), **C.23** (SoS‑LOG clauses as explainability gates for cross‑Tradition choices), **G.4** (Acceptance hooks/thresholds when bridges are used as selector gates), **E.10** (LEX / strict distinction discipline).
**Working‑Model first.** Prefer a minimal, auditable calibration procedure and worked micro‑cases; escalate to heavier harnesses only where risk warrants (per **E.8**).
**Non‑duplication note.** Universal Part‑G invariants (no shadow specs; Bridge‑only crossings; penalty routing to `R_eff` only; P2W split; typed/id‑based RSCR causes; defaults with one governing definition; Δ‑discipline) are governed by `G.Core` and are *cited* via `CC‑GCORE‑*`. This pattern defines only the *bridge calibration kit* and its surfaces.

### G.7:1 - Problem frame

SoTA synthesis (**G.2**) can legitimately preserve pluralism by exporting a **BridgeMatrix**: a Tradition×Tradition inventory of “comparable constructs” with preliminary notes (candidate correspondences, likely losses, tentative levels). Downstream patterns (CHR/CAL/selector/logging/shipping) cannot consume this safely unless cross‑Context reuse is:

* **materialised** as explicit bridge artefacts (not implied by prose),
* **calibrated** with a small, auditable procedure (so CL/CL^k/plane routing is not a narrative),
* **published** as checkable crossing bundles (UTS + GateCrossing harness),
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

### G.7:5 - Archetypal Grounding (System / Episteme)

**System (Γ_sys):** *Cross‑standard safety assurance comparison (bridge‑first).*
A team must compare a safety assurance claim across two regulatory Traditions (e.g., a “functional safety case” tradition and a “ML system testing” tradition) for the *same physical system scope*. `G.7` forces explicit SenseCell‑level bridges (what exactly is the “hazard”, what is the “evidence carrier”, what is the “pass criterion”), records losses, pins planes, and provides sentinels so that changes in the safety evidence protocol editions trigger path‑local RSCR rather than re‑authoring the entire safety case.

**Episteme (Γ_epist):** *Benchmark protocol pluralism (post‑2015 evaluation practice).*
A research group wants to compare “state‑of‑the‑art” across multiple evaluation Traditions (IID performance, shift robustness, preference‑based evaluation). `G.7` turns “these are comparable” into explicit BridgeCards with declared row scope, pins the evaluation protocol editions, and emits sentinels so that when a benchmark protocol or policy pin changes, downstream selector decisions can be re‑audited by re‑citing the same PathSlice‑scoped evidence.

### G.7:6 - Bias‑Annotation

Lenses tested: **Gov**, **Arch**, **Onto/Epist**, **Prag**, **Did**.
Scope: Universal for the bridge calibration kit; any method‑family or discipline‑specific calibration technique is modularized as `GPatternExtension` and cited to its governing patterns.

### G.7:7 - Conformance Checklist (normative) — **CC‑G7**

| ConformanceId             | Requirement                                                                                                                                                                                                                                                                               | Purpose                                                                        |
| ------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------ |
| **CC‑G7‑CoreRef**         | `G.7` is conformant only if it satisfies the effective `G.Core` obligations declared by the `GCoreLinkageManifest` in **§4.1** (after nil‑elision and expansion of profile/set/pinset ids), including any explicit deltas listed there. | Make universal invariants one governing definition and enforce citation‑based reuse.       |
| **CC‑G7‑BCT‑1**           | For any active `TradPairId` with cross‑Tradition reuse, a `BridgeCalibrationTable (BCT)` **MUST** exist, declare a `FreshnessWindowRef`, and provide `RowEntry` records that cite, at minimum: `RowEntryId`, `ComparableConstructId`, `RowScopeId`, `BridgeCardId[]`, `RowCL_min`, `PlanePins {ReferencePlane(src), ReferencePlane(tgt)}`, `PolicyPins {Φ(CL)}` (and `Ψ(CL^k)?`, `Φ_plane?` when applicable), plus `{RegressionSetId, SentinelSetId}`. | Ensure the kit exists as an auditable object rather than a prose matrix.       |
| **CC‑G7‑BridgeCard‑1**    | Any bridge published by G.7 **MUST** be consumable as an **F.9** `BridgeCard` and **MUST** be SenseCell‑anchored (directly or via explicit SenseCell anchor refs).                                                                                                                        | Prevent “Context‑only” or ambiguous bridges.                                   |
| **CC‑G7‑UTS‑1**           | G.7 outputs **MUST** mint/publish UTS‑citable ids (NameCards/twin labels as applicable) for (a) each BridgeCard (or its NameCard) and (b) each GateCrossing/crossing row that makes bridge use checkable; and **MUST** expose the resulting `UTSRowId[]` in the BCT/Ledger/crossing bundles. *(UTS discipline is delegated to `CC‑GCORE‑UTS‑1`.)* | Make bridge calibration externally citable and checkable.                      |
| **CC‑G7‑RowScope‑1**      | Every BCT row **MUST** declare its `RowScopeId` (what notion of “sameness” is claimed), and any loss notes **MUST** be recorded as citable artefacts (refs/ids), not only narrative text.                                                                                                 | Keep reuse honest and locally bounded.                                         |
| **CC‑G7‑CLRegime‑1**      | Every BCT row **MUST** record `RowCL_min` (and `RowCL_k_min?`, `RowCL_plane_min?` where applicable) and apply the admissibility regime from §4.2.1: `≥2` admissible; `=1` only with cited `WaiverRef[]`; `=0` forbidden for reuse. The honesty rule must be satisfied: ≥1 counterexample for `≤2`, and an explicit stated‑absence disclosure for `=3` when no counterexample is cited. | Make CL/waiver/plane regimes explicit and auditable at kit level.              |
| **CC‑G7‑SCRLinkage‑1**    | Whenever bridge calibration is cited in SCR/Evidence surfaces, the citation **MUST** include `{BridgeCardId[]}` (or `UTSRowId[]` for the bridge artefacts), an explicit row locator (`RowEntryId` or equivalent), `{BCT.id, RegressionSetId}`, and the active policy id pins `{Φ(CL), Ψ(CL^k)?, Φ_plane?}` (ids only; representation governed elsewhere). | Prevent “pins exist but are not visible/auditable” failure mode.               |
| **CC‑G7‑SoSLOG‑Pins‑1**   | When `G.7:Ext.SoSLogClauses` is in use, G.7 outputs **MUST** expose the cited SoS‑LOG rule ids and the relevant `PathId/PathSliceId` evidence citations; any change in those pins **MUST** be RSCR‑relevant per `CC‑GCORE‑TRIG‑1…TRIG‑4`.                                               | Keep cross‑Tradition reuse explainable without embedding C.23 semantics.        |
| **CC‑G7‑Acceptance‑1**    | When `G.7:Ext.AcceptanceHooks` is in use, G.7 outputs **MUST** expose the Acceptance clause ids/policy ids used as gates; thresholds/unknown handling remain governed by Acceptance; any change **MUST** be RSCR‑relevant per `CC‑GCORE‑TRIG‑1…TRIG‑4`.                                           | Keep thresholds and unknowns out of bridges while preserving auditability.     |
| **CC‑G7‑RowBottleneck‑1** | If a comparable construct row aggregates multiple bridge cells, row summaries (e.g., `RowCL_min`) **MUST** follow bottleneck discipline (F.7) and cite a counterexample whenever a cell carries a loss note.                                                                              | Forbid “CL averaging” and enforce loss‑aware summaries.                        |
| **CC‑G7‑PolicyPins‑1**    | G.7 outputs **MUST** publish the *policy id pins* required to audit penalty routing and plane effects (ids only), as required by `CC‑GCORE‑LINK‑1/2` and `CC‑GCORE‑PEN‑1`. G.7 MUST NOT duplicate policy tables or redefine penalty semantics.                                           | Keep penalty routing auditable while preserving single‑governing-pattern policy semantics. |
| **CC‑G7‑GateCrossing‑1**  | Any published crossing rows that rely on bridges **MUST** be checkable via GateCrossing/CrossingBundle harnesses (E.18/A.21): required pins are present; lexical constraints and lane purity checks are runnable.                                                                        | Make crossings checkable, not narrative.                                       |
| **CC‑G7‑Sentinels‑1**     | G.7 **MUST** register `BridgeSentinel` entries for bridges used by live scopes and **MUST** emit typed RSCR triggers (canonical `RSCRTriggerKindId`; see `CC‑GCORE‑TRIG‑1…TRIG‑4`) on calibration‑relevant edits, scoped to the watched `PathSliceId[]` or `PatternScopeId[]`, with the minimum payload pins from §4.1. | Enable targeted refresh rather than pack‑wide reruns.                          |
| **CC‑G7‑QD‑Pins‑1**       | When `G.7:Ext.QDParityPins` is in use, G.7 outputs **MUST** include `{DescriptorMapRef.edition, DistanceDefRef.edition, InsertionPolicyRef}` and treat any change to those pins as RSCR‑relevant per `CC‑GCORE‑TRIG‑1…TRIG‑4`.                                                          | Prevent silent QD telemetry drift.                                             |
| **CC‑G7‑DHC‑Units‑1**     | When AlignmentDensity (or related DHC accounts) are reported, G.7 outputs **MUST** (a) restrict the counted bridge set to rows with `RowCL_min ≥ 2` (treat `CL=3` as “free substitution”, `CL=2` as “guarded” for reporting), (b) include declared units, and (c) cite the relevant DHC method semantics (C.21). G.7 MUST NOT invent arithmetic over ordinal/illegal surfaces. | Keep dashboards and discipline‑health metrics lawful and interpretable.        |

### G.7:8 - Common Anti-Patterns and How to Avoid Them

* **Bridge‑by‑prose (“they have the same sense”).**
  **Avoid:** publish BCT rows + BridgeCards + UTS rows; require SenseCell anchoring and row scopes.
* **SenseFamily jump (scope‑bridge used as kind‑bridge).**
  **Avoid:** keep channel/sense‑family constraints governed by **F.9** visible; use `RowScopeId` to state which channel is claimed, and require `CL^k` + `Ψ(CL^k)` pins when a kind‑channel bridge is invoked (do not “upgrade” a scope‑channel bridge into kind substitution).
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

* **Why a kit (not a new governance card or legality gate)?** Bridge calibration must support many downstream consumers without becoming a competing legality gate; governing-spec semantics remain governed by `CG‑Spec`/`CN‑Spec`.
* **Why BCT + RegressionSet + SentinelSet?** Because calibration without regression tests drifts silently, and regression without sentinels is operationally unusable (refresh becomes global).
* **Why row scopes?** Because “comparable” is not one thing; scope must be explicit to avoid accidental substitution.

### G.7:11 - SoTA‑Echoing (post‑2015, for orientation; non‑normative)

* **Edition‑aware evaluation and dataset shift practice.** Post‑2018 evaluation culture (robustness and shift benchmarks, protocol pinning, reproducibility checklists) motivates treating protocol versions and “what changed” as first‑class pins rather than prose.
* **Preference‑based optimisation families.** Modern preference‑learning lines (late‑2010s → 2020s) show how neighbouring objectives can share intent but diverge in assumptions—an archetypal case for row scope + loss notes.
* **Quality‑Diversity and differentiable QD.** MAP‑Elites successors (CVT variants, CMA‑ME line, differentiable QD ecosystems) emphasise archive/descriptor/distance artefacts whose editions must be pinned for comparability.
* **Open‑ended evolution and transfer‑rule portfolios.** POET‑class work motivates explicit transfer rule editions and environment validity regions as pins when bridges are used for cross‑tradition reporting.

### G.7:12 - Relations

**Builds on:** `G.Core`, `G.2`, `F.3`, `F.7`, `F.9`, `B.3`, `E.10`, `E.18`, `A.21`, `G.6`, `C.21`.
**Optionally uses via Extensions:** **G.4** (Acceptance hooks), **C.23** (SoS‑LOG clauses), **C.18 and C.19** (QD/OEE pins).
**Used by / prerequisite for:** **G.5** (cross‑Tradition eligibility/selection), **G.11** (refresh orchestration), **G.9** (parity across Traditions where bridges are required), **G.10** (shipping surfaces that must cite bridge calibration ids), **G.12** (DHC dashboards when bridge counts/units are surfaced).
**Publishes to:** **UTS** (bridge and crossing rows; twin labels as applicable) and emits RSCR‑ready telemetry/trigger payloads for **G.11**.
**Constrains:** Any downstream consumer that claims cross‑Context/Tradition reuse must use the calibrated bridge artefacts/pins surfaced by this kit (governed by G.Core crossing invariants apply).

### G.7:End

## G.8 - SoS‑LOG Bundles & Maturity Ladders

**Tag.** Architectural pattern (packaging kit).
**Stage.** Design‑time packaging (authoring & publication) with a run‑time consumption facade for `G.5` (selector/registry).
**Primary hooks:** `G.Core` (Part‑G invariants), `C.23` (SoS‑LOG semantics), `C.22` (TaskSignature), `G.4` (Acceptance & EvidenceProfiles), `G.6` (EvidenceGraph & `PathId/PathSliceId`), `G.5` (registry/selector), `G.11` (refresh orchestration), `G.10` (shipping boundary), `F.9` (BridgeCard & CL), `F.17` (UTS), `E.17` (publication faces), `G.7` (bridge calibration & Φ/Ψ/Φ_plane), `F.8` (Policy pins: `PolicySpecRef`/`MintDecisionRef` resolvability), `A.10` (anchors), `E.10` (LEX twin registers), `E.5.2` (notational independence), `E.18/A.21` (GateCrossing visibility and gate checks).

**Non‑duplication note (Phase‑2 universalization).** This pattern introduces **kit-governed packaging surfaces** for SoS‑LOG bundles and maturity ladders. All **Part‑G‑wide invariants** (no shadow specs, Bridge‑only crossings + visibility, tri‑state guard domain, penalties→`R_eff`‑only, set‑return semantics, P2W split, typed RSCR triggers + alias docking, defaults with one governing definition, shipping boundary) are **pinned through `G.Core`** and are not restated here.

**Modularity note (policy‑id pins are reference‑only).** This kit may pin/cite policy ids (e.g., `Φ/Ψ/Φ_plane` policies, `FailureBehaviorPolicyId`, illumination‑promotion policy ids, and E/E‑LOG policy ids) **as references only**. Conformance relies on the policy‑pin resolvability discipline of `F.8:8.1` (i.e., policy ids are not “inlined”; and when newly minted, they are backed by resolvable `PolicySpecRef` + `MintDecisionRef`). `G.8` does not define policy semantics and MUST NOT silently mint policy ids.

### G.8:1 - Problem frame

Method families compete within a `CG‑Frame`, but dispatch is only lawful if (i) admissibility decisions remain **tri‑state** and auditable, (ii) evidence and crossings are **explicitly citable** (by ids, not prose), and (iii) selection preserves **set-return semantics** under partial orders. In practice, SoS‑LOG rules (`C.23`) and “maturity stories” are often distributed across prose, dashboards, and ad‑hoc checklists, with thresholds embedded where they do not belong and with missing pins for evidence paths, crossings, and editions.

This pattern provides the missing packaging kit: a **selector‑facing, UTS‑citable bundle** that binds **(a)** rule ids (semantics governed by `C.23`), **(b)** an ordinal/poset maturity ladder (published as a citable card), and **(c)** explicit wiring to Acceptance (`G.4`), EvidenceGraph (`G.6`), selection/registry (`G.5`), and refresh (`G.11`)—without creating any shadow governing spec refs.

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
| **Interoperability vs. crossing discipline** | Reuse across contexts or planes ↔ prevent implicit crossings (Bridge‑only + visible).                           |

### G.8:4 - Solution — Publish SoS‑LOG bundles and maturity cards as UTS‑citable kit

#### G.8:4.1 - G.Core linkage (normative)

**Builds on:** `G.Core` (Part‑G core invariants; citation/delegation hub)

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
  // Public ids governed by this pattern (strengthen conditional pins where G.8 publishes UTS publication units)
  UTSRowId[],                    // bundle/ledger/card rows + any referenced UTS rows
  SoS‑LOGBundleRef,
  SoSLogRuleId[],
  MethodFamilyId,
  RegistrationContext,

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

**Objects / surfaces (pattern-governed).**

* **`SoS‑LOG.Rule`**
  A rule id that denotes an executable tri‑state decision schema `{pass | degrade(mode) | abstain}` for `(TaskSignature, MethodFamily)`. *(“pass” may be described as “admit” in prose, but the normative tri‑state vocabulary is `G.Core`’s `{pass|degrade|abstain}`.)*
  **Semantics are governed by `C.23`.** `G.8` only packages rule ids and binding pins.

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

  // Scope + spec pins (from GCorePinSetId.PartG.AuthoringMinimal)
  CG-FrameContext,
  describedEntity := ⟨GroundingHolon, ReferencePlane⟩,
  CNSpecRef.edition,
  CGSpecRef.edition,

  MethodFamilyId,
  RegistrationContext,

  SoSLogRuleId[] ,               // ids only; semantics governed by C.23
  ClosedEnums: {DegradeModeEnum, MaturityRungs},  // ids only; UTS-registered closed value sets
  A10EvidenceGraphRef?[] ,        // packaging-time evidence carriers (A.10 anchors) when paths are not yet stable
  MaturityCardRef ,               // UTS ref to maturity card (required; may be embedded but MUST be citable)
  MaturityRungId? ,               // if a specific rung is asserted at packaging time

  // Optional: Acceptance wiring (thresholds remain governed by G.4)
  AcceptanceClauseId[]? ,

  // Optional: Evidence wiring (for later audit & rung transition justification)
  EvidenceGraphId? ,
  PathId[]/PathSliceId[]? ,

  // Optional: cross-context or cross-plane wiring (only when reuse is asserted)
  BridgeId/BridgeCardId? ,
  CL/CL^k/CL^plane? ,
  Φ/Ψ/Φ_plane policy-ids? ,

  // Optional: selector semantics pins (explicit value or resolved via DefaultGoverningDefinitionIndex)
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

**Bundle discipline (normative intent; semantics delegated):**

* `SoS‑LOGBundle@Context` **does not introduce** new legality or normalization rules; it cites the pinned references above.
* Thresholds and numeric gates are cited by id from `G.4` Acceptance (no embedding inside the bundle).
* If cross-context or cross-plane reuse is asserted, crossing pins are made explicit (Bridge/CL/Φ policy ids), and evidence paths are citable when available.

**Binding obligations B1–B5 (packaging‑only; wiring‑only; semantics delegated):**

* **B1 — Evidence wiring.** At packaging time the bundle SHOULD provide resolvable evidence refs (typically `A10EvidenceGraphRef?[]` and/or `EvidenceGraphId?`). At run time, admissibility outcomes SHOULD cite `PathId/PathSliceId` when available (`G.6`), so rung transitions and `degrade/abstain` traces are audit‑stable.
* **B2 — CL/plane routing pins.** When reuse across Context or plane is asserted, the bundle/ledger MUST pin the relevant Bridge/CL/Φ/Ψ/Φ_plane policy ids (reference‑only; resolvable per `F.8:8.1`) and MUST respect the core penalty routing (penalties affect `R_eff` only; `F/G` invariance via `G.Core`).
* **B3 — `PortfolioMode`/QD fields.** If the bundle/ledger exposes `PortfolioMode`/QD fields (e.g., `PortfolioMode=Archive`), it MUST pin the descriptor/distance/insertion/emitter artefacts (editions/policies as applicable). Illumination remains **report‑only** unless explicitly promoted by a `G.4` governing-pattern policy id that is pinned and recorded in the run‑time trace.
* **B4 — Open‑ended fields.** If the bundle binds an open‑ended generator family, it MUST pin `GeneratorFamilyId` and `TransferRulesRef.edition` (and any validity region/coupler policy ids when used). Unknown transfer validity MUST be recorded as `degrade`/branching, not as an ad‑hoc fourth status.
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

This card is a **description** suitable for dispatch/audit and refresh; it is not a competing governing spec ref.

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
**GoverningPatternId:** `C.23`
**Uses:** `{C.23}`
**⊑/⊑⁺:** `∅`
**RequiredPins/EditionPins/PolicyPins (minimum):**

* `SoSLogRuleId[]`
* `SoSLogBranchId[]?`
* `FailureBehaviorPolicyId?` *(when degrade behaviour is policy‑bound)*

**RSCRTriggerSetIds / RSCRTriggerKindIds:** `∅` *(covered by `G.8:4.1`)*
**Notes (wiring‑only):**
* Rule meaning, branch taxonomy, and “probe/sandbox” semantics are governed by `C.23`; this module only binds ids and pins.

#### G.8:5.2 - `G.8:Ext.AcceptanceWiring`

**PatternScopeId:** `G.8:Ext.AcceptanceWiring`
**GPatternExtensionId:** `AcceptanceWiring`
**GPatternExtensionKind:** `MethodSpecific`
**GoverningPatternId:** `G.4`
**Uses:** `{G.4}`
**⊑/⊑⁺:** `∅`
**RequiredPins/EditionPins/PolicyPins (minimum):**

* `AcceptanceClauseId[]`
* `EvidenceProfileId[]?` *(if the ledger/bundle cites evidence profile ids rather than only paths)*
* `PromotionPolicyId?` *(only if telemetry may be promoted into dominance by explicit CAL policy)*

**RSCRTriggerKindIds (optional delta):** `{RSCRTriggerKindId.PolicyPinChange}` *(only if acceptance policies are pinned as ids in the bundle/ledger)*
**Notes (wiring‑only):**
* Thresholds remain governed by `G.4` Acceptance; this module carries only clause ids and policy pins.

#### G.8:5.3 - `G.8:Ext.BridgeReuseWiring`

**PatternScopeId:** `G.8:Ext.BridgeReuseWiring`
**GPatternExtensionId:** `BridgeReuseWiring`
**GPatternExtensionKind:** `InteropSpecific`
**GoverningPatternId:** `G.7`
**Uses:** `{G.7, F.9}`
**⊑/⊑⁺:** `∅`
**RequiredPins/EditionPins/PolicyPins (minimum):**

* `BridgeId/BridgeCardId`
* `CL/CL^k/CL^plane`
* `Φ/Ψ/Φ_plane policy-ids`
* `BridgeCalibrationTableId?`, `RegressionSetId?` *(if cited as calibration evidence)*

**RSCRTriggerSetIds:** `{GCoreTriggerSetId.BridgeCalibrationKit}` *(only if the bundle/ledger explicitly binds calibration records by id)*
**Notes (wiring‑only):**
* Present only when `SoS‑LOGBundle@Context` asserts cross-Context or cross-plane reuse. No additional crossing semantics are defined here.

#### G.8:5.4 - `G.8:Ext.QDArchiveTelemetry`

**PatternScopeId:** `G.8:Ext.QDArchiveTelemetry`
**GPatternExtensionId:** `QDArchiveTelemetry`
**GPatternExtensionKind:** `MethodSpecific`
**GoverningPatternId:** `C.18`
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
**GoverningPatternId:** `C.19`
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
**GoverningPatternId:** `G.5` *(generator family registry surface; algorithm semantics remain external to Part‑G core)*
**Uses:** `{G.5}`
**⊑/⊑⁺:** `∅`
**RequiredPins/EditionPins/PolicyPins (minimum):**

* `GeneratorFamilyId`
* `TransferRulesRef.edition`
* `EnvironmentValidityRegionId?`
* `CouplerPolicyId?`

**RSCRTriggerKindIds:** `{RSCRTriggerKindId.EditionPinChange, RSCRTriggerKindId.PolicyPinChange, RSCRTriggerKindId.TelemetryDelta}`
**Notes (wiring‑only):**
* Open‑ended coverage/regret (or similar) remains telemetry unless explicitly promoted by a governing-pattern policy.

### G.8:6 - Archetypal Grounding (System / Episteme)

**Show‑A — Tri‑state admissibility with set‑valued selection (multi‑criteria).**
A CG‑Frame carries multiple offline/robust decision families (e.g., conservative offline RL and transformer‑based policy models post‑2020). The bundle publishes `RuleId[]` (SoS‑LOG semantics in `C.23`), cites `AcceptanceClauseId[]` for any floors (governed by `G.4`), and emits an `AdmissibilityLedger` whose rows cite `PathSliceId` (when available) for each `pass/degrade/abstain`. `G.5` consumes the ledger and returns a **selected set** under the declared partial order—no scalar “winner”.
**Show‑A — Tri‑state admissibility with set‑valued selection (multi‑criteria).**
A CG‑Frame carries multiple offline/robust decision families (e.g., conservative offline RL and transformer‑based policy models post‑2020). The bundle publishes `SoSLogRuleId[]` (SoS‑LOG semantics in `C.23`), cites `AcceptanceClauseId[]` for any floors (governed by `G.4`), and emits an `AdmissibilityLedger` whose rows cite `PathSliceId` (when available) for each `pass/degrade/abstain`. `G.5` consumes the ledger and returns a **selected set** under the declared partial order—no scalar “winner”.

**Show‑B — QD archive dispatch with edition‑pinned descriptors (post‑2015 QD families).**
A method family uses a modern QD line (e.g., CMA‑ES‑driven archives, differentiable QD variants, and large‑scale JAX‑style QD toolchains). The bundle pins `DescriptorMapRef.edition` and `DistanceDefRef.edition`, plus insertion/emitter policies. Illumination metrics are logged as telemetry; any promotion into dominance is only via explicit CAL policy pins (recorded in the admissibility trace).

**Show‑C — Open‑ended environment–method co‑evolution (post‑2018 open‑ended families).**
A generator family operates in an open‑ended setting (e.g., POET‑style and PAIRED‑style regimes). The bundle carries `TransferRulesRef.edition` and validity region pins; unknown transfer validity triggers a `degrade` branch rather than an ad‑hoc fourth status. Telemetry (coverage/regret proxies) is emitted for refresh planning, not silently turned into dominance.

### G.8:7 - Bias‑Annotation

Lenses tested: **Gov**, **Arch**, **Onto/Epist**, **Prag**, **Did**.
Scope: packaging kit only. Rule semantics remain governed by `C.23`; thresholds remain governed by `G.4`; evidence path semantics remain governed by `G.6`; selection semantics remain governed by `G.5`.

### G.8:8 - Conformance Checklist (CC‑G8)

* **CC‑G8‑CoreRef (G.Core conformance bridge).**
  A conforming `G.8` SHALL satisfy the **effective** set of `CC‑GCORE‑*` obligations implied by `G.8:4.1` (expanded per `G.Core:4.2`), including required pins, trigger sets, and Default Governing Definition Index citation.

* **CC‑G8‑1 (No thresholds in LOG).**
  Any numeric gate, maturity floor, or threshold SHALL be authored as a `G.4` Acceptance artefact and cited by id; the LOG bundle/ladder SHALL NOT embed thresholds.

* **CC‑G8‑2 (Tri‑state discipline; delegated).**
  Guard outcomes SHALL obey the tri‑state domain and unknown handling defined in `G.Core` (delegation to `CC‑GCORE‑GUARD‑1`).
  Any sandbox/probe‑only behaviour SHALL be represented as an explicit `C.23` branch and MUST pin (and record) the controlling policy id (typically an E/E‑LOG policy id via `C.19`), rather than inventing a fourth status or silently coercing unknowns.

* **CC‑G8‑3 (Path citation when evidence is path‑addressable).**
  When `G.6` is in use (or resolvable), every recorded `pass/degrade/abstain` outcome in the `AdmissibilityLedger` MUST cite `PathId/PathSliceId` (run‑time). At packaging time, the bundle/ledger SHALL at minimum provide resolvable evidence refs (e.g., `EvidenceGraphId?` + anchor refs).

* **CC‑G8‑4 (Crossing visibility and penalty routing; delegated).**
  Any cross-Context or cross-plane reuse asserted by the bundle/ledger SHALL satisfy the core crossing visibility and penalty routing invariants (delegation to `CC‑GCORE‑CROSS‑1` and `CC‑GCORE‑PEN‑1`).

* **CC‑G8‑5 (PortfolioMode/dominance hygiene; delegated).**
  The bundle/ledger SHALL treat `PortfolioMode` and dominance fields as pinned inputs and SHALL cite the governing definition for each omitted default through `G.Core.DefaultGoverningDefinitionIndex` (delegation to `CC‑GCORE‑DEF‑1` and `CC‑GCORE‑SET‑1`; governing definitions include `CC‑G5.23` for `DefaultId.PortfolioMode` and `CC‑G5.28` for `DefaultId.DominanceRegime`). It MUST NOT restate default values locally.
  If the bundle/ledger records telemetry that could influence dispatch (e.g., illumination/QD/OEE/open‑ended proxies), such telemetry SHALL remain report‑only unless explicitly promoted by a `G.4` governing-pattern policy id that is pinned and recorded in the run‑time trace.

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
  When a LOG bundle is used to drive or justify a produced selected-set outcome, the producing Work/Audit artefact SHOULD cite the controlling mechanism ids (e.g., parity/shipping/refresh artefact ids) and relevant policy pins; no “black box” provenance.

* **CC‑G8‑11 (SoTA‑of‑description trace).**
  If authoring methods (e.g., discovery, clustering, summarisation) materially shaped rule text or rung definitions, the bundle/card SHOULD cite their method description refs (edition‑pinned) to support cross‑stance traceability.

### G.8:9 - Common Anti‑Patterns and How to Avoid Them

* **Anti‑pattern:** Embedding thresholds inside SoS‑LOG rules or ladder rungs.
  **Avoid:** thresholds live in `G.4` Acceptance; bundle only cites clause ids.

* **Anti‑pattern:** Treating illumination/QD telemetry as a hidden scalar score that changes dominance.
  **Avoid:** keep telemetry report‑only unless explicitly promoted by a governing-pattern policy pin.

* **Anti‑pattern:** Publishing a bundle that “implies” cross‑context reuse without Bridge/CL/Φ pins.
  **Avoid:** if reuse is asserted, publish the crossing pins; otherwise downstream must abstain from reuse.

* **Anti‑pattern:** Re‑defining `PortfolioMode`/`DominanceRegime` defaults in the bundle text.
  **Avoid:** cite each default's governing definition through `G.Core.DefaultGoverningDefinitionIndex`.

* **Anti‑pattern:** Recording RSCR “reasons” as prose labels only.
  **Avoid:** emit canonical `RSCRTriggerKindId` values per `G.Core`.

### G.8:10 - Consequences

* **Positive:** `G.5` receives a stable, citable, selector‑facing artefact without importing rule semantics or threshold logic.
* **Positive:** Audit and refresh become tractable: pins, crossings, evidence paths, and trigger kinds are explicit.
* **Positive:** Maturity remains non‑scalar, reducing illegitimate aggregation and “readiness theater”.
* **Negative:** Requires stricter authoring discipline (UTS publication, pin completeness, explicit wiring).
* **Negative:** If evidence paths are not maintained (`G.6` absent), auditability degrades and downstream must rely on references with lower evidence-support class, or abstain.

### G.8:11 - Rationale

`C.23` governs **rule semantics**, `G.4` governs **thresholding/acceptance**, `G.6` governs **path‑addressable provenance**, and `G.5` governs **selection/registry semantics**. Without a dedicated packaging kit, projects either (i) duplicate semantics inside ad‑hoc “decision bundles” (creating shadow specs), or (ii) leave dispatch un‑auditable. `G.8` keeps these boundaries strict while providing a single, consumable surface.

### G.8:12 - SoTA‑Echoing (informative; post‑2015 practice alignment)

This pattern’s separation of **decision rules**, **acceptance thresholds**, **provenance paths**, and **set‑valued outputs** echoes post‑2015 practice in:

* **Set‑valued / set-returning selection** (multi‑objective and uncertainty‑aware regimes; avoiding forced scalar winners).
* **Quality‑Diversity and archive‑based evaluation** (post‑2015 QD variants emphasize edition‑pinned descriptors/distances and telemetry‑driven refresh).
* **Open‑endedness / curriculum generation** (post‑2018 lines emphasize explicit transfer rules, safe degrade branches, and telemetry‑driven orchestration rather than hidden gates).
* **Reproducibility‑aware publishing** (explicit identifiers, pinned editions/policies, citable traces rather than prose‑only decision rationales).

*(Examples are illustrative; they do not introduce new Part‑G‑wide norms.)*

### G.8:13 - Relations

**Builds on:** `G.Core`, `C.23`, `G.4`, `G.6`, `G.5`, `C.22`
**Uses:** `A.10` (anchors), `F.8` (policy-id resolvability), `F.9`/`F.17`/`E.17` + `G.7` (when cross-Context or cross-plane reuse is asserted), `G.11` (refresh planning/trigger consumption), `G.10` (shipping boundary; if bundled artefacts are shipped), `E.10` (LEX twin registers), `E.5.2` (notation independence), `E.18/A.21` (GateCrossing visibility and gate checks); optional `C.18` (QD) / `C.19` (E/E‑LOG) when those surfaces are declared.
**Publishes to:** `UTS` (bundle/ledger/card), `G.5` (selector/registry consumption), `G.11` (refresh via typed triggers and pinned telemetry)
**Constrains:** any SoS‑LOG packaging that claims FPF conformance for selector‑facing dispatch across method families.

### G.8:14 - Author’s quick checklist (informative)

* [ ] `RuleId[]` are ids only; rule semantics are governed by `C.23` (no re-definition in this bundle).
* [ ] `SoSLogRuleId[]` are ids only; rule semantics are governed by `C.23` (no re-definition in this bundle).
* [ ] Any numeric gates/thresholds are `G.4` Acceptance artefacts cited by id (no thresholds embedded in LOG or rungs).
* [ ] Evidence is citable: at run time use `PathId/PathSliceId` when available; at packaging time provide resolvable `A10EvidenceGraphRef?[]` / `EvidenceGraphId?`.
* [ ] Any cross-Context or cross-plane reuse is explicit: `BridgeId/BridgeCardId`, `CL/CL^k/CL^plane`, and `Φ/Ψ/Φ_plane` policy ids are pinned (policy ids resolvable per `F.8:8.1`).
* [ ] `PortfolioMode` and dominance defaults are not restated: cite each default's governing definition through `G.Core.DefaultGoverningDefinitionIndex` (governing definitions live outside `G.8`, typically `G.5`).
* [ ] QD pins are edition/policy pinned (`DescriptorMapRef.edition`, `DistanceDefRef.edition`, insertion/emitter policies); `CharacteristicSpaceRef.edition` is pinned iff cell boundaries/de‑dup/parity depend on it; **Spaces ≠ Maps**.
* [ ] If open‑ended surfaces are declared, pin `GeneratorFamilyId`, `TransferRulesRef.edition`, and any validity/coupler policy ids; unknown transfer validity is recorded as `degrade`/branching (no “fourth status”).
* [ ] `MaturityRungs` is a closed, UTS‑registered set; the maturity ladder is ordinal/poset with a declared `ReferencePlane`; rung transitions cite evidence.
* [ ] RSCR triggers are emitted as canonical `RSCRTriggerKindId` values (no prose-only “reasons”).
* [ ] Notation independence (`E.5.2`) and twin‑register discipline (`E.10`) are respected for all published heads/ids.
* [ ] If authoring tools materially shaped rule/rung content, cite `AuthoringMethodDescriptionRefs?[]` (edition‑pinned) for cross‑stance traceability.

### G.8:End

## G.9 — Parity / Benchmark Harness

> **Status:** Stable

### G.9:0 — Use this when

- rival method families, method sets, or adaptation paths must be compared under one declared baseline set and freshness window
- you need parity to publish one reproducible report rather than one opaque benchmark score
- downstream selection must recover comparator, normalization, bridge, and evidence pins without relying on one hidden scoring sheet

### G.9:0.1 — What goes wrong if missed

- benchmark numbers mix different windows, baselines, or comparator editions and still pretend to be comparable
- cross-context reuse or normalization mapping stays hidden until a disagreement appears downstream
- parity flattens a partial order into one scalar winner and silently changes what the comparison means

### G.9:0.2 — What this buys

- one `ParityPlan@Context` that fixes baseline, freshness, comparator, and bridge discipline up front
- one `ParityReport@Context` that echoes the active pins, outcomes, and evidence trace by value
- one harness that downstream selection can consume without inventing a `G.9`-local CSLC gate or a shadow governance card

Illumination, coverage, and regret remain telemetry by default. If they are promoted into dominance, that promotion must be one explicit policy-bound choice rather than one hidden scoring convenience.

### G.9:1 — Intent

Provide a **notation‑independent** harness that:

* plans parity runs with explicit scope (`describedEntity`, `ReferencePlane`, window), explicit governance, CSLC comparability and admissibility references, and comparator references (`CNSpecRef`, `CGSpecRef`, `ComparatorSpecRef`) and explicit reproducibility pins (editions + policy‑ids);
* executes parity in a way that is consumable by **G.5** (selected-set outcomes, DRR/SCR evidence trace);
* publishes **ParityReport@Context** suitable for downstream consumption, shipping, and refresh/RSCR wiring.

### G.9:2 — Problem frame

Parity claims become non‑reproducible or non‑comparable when any of the following are implicit:

* evidence window / freshness regime,
* comparator semantics (including any normalization / comparability mapping),
* method‑family “measurement” edition pins (incl. DHC method/spec),
* cross‑Context reuse (Bridge refs, crossing pins, and CL penalty placement),
* dominance and `PortfolioMode` interpretation rules,
* gate outcomes (why a run abstained or degraded).

G.9’s role is to make these recoverable as **pinned and publishable** as a *method of obtaining outputs* (MOO) without introducing new governing spec refs.

### G.9:3 — Forces

* **Pluralism vs comparability.** Multiple Traditions must be comparable *without semantic collapse*.
* **Partial orders.** Many targets are only partially ordered; parity reporting must preserve CSLC-admissible outcome shape (often selected sets or archives rather than a single scalar).
* **Edition sensitivity.** Parity must be robust to silent drift in measurement/comparator definitions. When DHC/QD/OEE modes are used, the required definition pins are introduced only via the corresponding `Extensions` blocks (nil‑elision when unused).
* **Telemetry vs objectives.** IlluminationSummary and coverage/regret are telemetry: **report‑only by default**; dominance changes require explicit CAL policy ids (recorded in audit pins).
* **GateCrossing visibility.** Any crossings/gates used by parity must be visible and auditable via CrossingBundle + GateCrossing checks; failures block parity publication/consumption.
* **Cross‑Context reuse.** Any reuse across contexts or reference planes must carry explicit crossing pins, audit support, and R-channel penalty placement.
* **Refreshability.** Parity must emit RSCR‑relevant causes as canonical ids, with enough pins to re‑run.

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
