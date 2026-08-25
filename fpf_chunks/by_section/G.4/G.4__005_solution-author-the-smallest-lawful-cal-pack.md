---
chunk_kind: "child"
pattern_id: "G.4"
pattern_title: "CAL Authoring for a CG-Frame: Operators, Acceptance Clauses, Evidence Wiring"
section_id: "G.4:4"
section_title: "Solution — author the smallest lawful CAL pack"
source_path: "FPF-Spec.md"
output_path: "by_section/G.4/G.4__005_solution-author-the-smallest-lawful-cal-pack.md"
commit_sha: "2124f3a0ea03125a5bf495c2ef99f5fbb4c73571"
heading_path:
  - "G.4 — CAL Authoring for a CG-Frame: Operators, Acceptance Clauses, Evidence Wiring"
  - "G.4:4 — Solution — author the smallest lawful CAL pack"
line_start: 99483
line_end: 99714
dependencies:
  - "A.10"
  - "A.15.1"
  - "A.18"
  - "A.19"
  - "A.2.1"
  - "A.21"
  - "A.6.1"
  - "B.3"
  - "C.11"
  - "C.18"
  - "C.19"
  - "C.2.1"
  - "C.23"
  - "E.17"
  - "E.18"
  - "E.8"
  - "F.17"
  - "F.6"
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
  - "CAL Pack@CG-Frame"
  - "Context charter"
  - "acceptance clause"
  - "legal flow"
  - "pass \\"
  - "typed operator card"
---

### G.4:4 - Solution — author the smallest lawful CAL pack

#### G.4:4.0 - Practitioner authoring path C1–C9

Complete these actions in order; widen a step only when its stated input is needed by the current task.

1. **C1 — Charter the scope.** Name `CG-FrameContext`, the exact `entityOfConcern`, `ReferencePlane`, task, and the editions of the governance and legality records being relied on. State the assumption envelope in ordinary language.
2. **C2 — Declare one typed operator.** Give it a stable id, CHR-typed signature, preconditions, result kind, and failure behavior. This is an `A.6.1` operation declaration, not evidence of an application.
3. **C3 — Declare one acceptance clause.** Bind the exact Characteristic and result episteme, the threshold or predicate, the Context, unknown handling, and the stated stop, degrade, or abstain behavior. If the clause claims statistical risk or coverage control, also name the loss, target, calibration population and window, sampling or exchangeability assumptions, declared treatment of shift, and the exact policy that states the guarantee.
4. **C4 — Compose only a legal flow.** Cite the operators and gating clauses, preserve the lawful result kind, and keep a selected set when no lawful scalarization exists. A declared DAG is possible composition, not performed work.
5. **C5 — Name the minimum evidence/currentness need.** Cite the exact A.10 source/provenance anchors and G.11 window needed to judge the clause. Do not turn an evidence profile, citation, or graph membership into a verdict or actual reliance.
6. **C6 — Add an extension only when the task needs one.** Select its current subject pattern first, then pin only the descriptor, distance, insertion, exploration, branch, or path records that change the present CAL action. Otherwise omit the extension.
7. **C7 — Record proof or an explicit gap.** For every operator, flow, or clause, cite the legality/monotonicity/boundedness justification actually required; when it is missing, publish the gap and the consequent degrade/abstain behavior.
8. **C8 — Exercise declaration behavior.** Provide one worked authoring example and focused conformance tests for illegal operations, `pass | fail | unknown`, freshness, and failure behavior. The example and test remain declarations/test records unless separately grounded dated work is named.
9. **C9 — Publish and hand off.** Mint stable ids and continuity notes, then emit the smallest `TaskMap` from the task to eligible operator/flow ids, gating clause ids, and required evidence/currentness refs. Use G.11 for change refs; G.4 defines no refresh rule or runtime occurrence or result.

The authoring path is complete when a cold reader can reconstruct the plain acceptance sentence from the published ids and can also say what still has to happen at runtime. The maintainer-facing manifests, schemas, interfaces, and optional extension blocks below make the same pack machine-citable; they do not add another practitioner sequence.

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
* `CAL.Operator[]` — UTS‑published typed operation declarations governed by `A.6.1`; a card declares possible arguments, result kinds, and conditions but does not assert that an operation ran:

  * explicit signature over CHR types,
  * explicit preconditions/postconditions (incl. legality guard macros references),
  * explicit provenance/evidence hooks (by ids/pins, not by tool behavior).
* `CAL.Acceptance[]` — typed predicate declarations with Context‑local thresholds; a clause declares how an actual application is judged but is not itself a verdict:

  * binds to CHR characteristic ids (and, when inducing numeric comparison/aggregation, to `CG‑Spec.characteristic` ids),
  * exposes unknown handling and failure behavior via policy pins.
* `CAL.Flow[]` — legality‑checked declarations of possible operator composition; a declared DAG is not performed work:

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

#### G.4:4.4 - Interfaces (minimal I/O surface)

| Interface                 | Consumes                                            | Produces                                                                                  |
| ------------------------- | --------------------------------------------------- | ----------------------------------------------------------------------------------------- |
| `G.4-1 Charter`           | `CG-FrameContext`, SoTA inputs, `CHR Pack@CG-Frame` | `CAL.Charter@Context` + `TaskMap@Context` (`TaskMap`)  |
| `G.4-2 Operators`         | CHR typing + SoTA operator inventory                | `CAL.Operator[]` (UTS ids; typed signatures; refs to evidence profiles & guards)  |
| `G.4-3 Acceptance`        | Task intent + policy pins + CHR characteristics     | `CAL.Acceptance[]` (typed; thresholds; freshness envelope pins; failure behavior refs)    |
| `G.4-4 Flows`             | Operator cards + admissible aggregators             | `CAL.Flow[]` (legality‑checked compositions; declared result kind)                        |
| `G.4-5 NQD Surface`       | Task intent + policy pins + (optional) QD/OEE inputs | `CAL.NQD[]` (descriptor/distance/insertion refs + edition pins; optional)  |
| `G.4-6 Publish`           | All above + proofs + examples  | Versioned `CAL Pack@CG-Frame`, UTS entries, RSCR tests, Worked‑Examples, public-id continuity notes |

#### G.4:4.4a - Declaration-to-runtime evaluation boundary (normative)

A CAL pack is a reusable design-time declaration. A stored operator card, clause, flow, `TaskMap`, proof-ledger row, test, or evidence-profile reference establishes neither an actual participant nor performed evaluation. When a CAL declaration is applied, recover the runtime chain explicitly:

1. Name one exact `EvaluationMethod` (`U.Method`). Its `U.MethodDescription` may state generic participants, parameters, effects, and evaluation conditions, but it carries no actual-participant slots and no intrinsic claim that a test, proof, or acceptance event occurred.
2. Cite the exact `CAL.Operator`, `CAL.Flow`, and `CAL.Acceptance` declarations as `A.6.1` operation semantics. If the runtime application needs argument and result bindings, use the exact `A.6.1` declaration and application bindings; do not infer them from a compatible signature, `TaskMap`, or stored reference.
3. Ground one dated `EvaluationWork` as `U.Work` and point to its complete A.15.1/F.6 basis. Recover the evaluated or affected referent, actual resources, and every concrete participant through its direct subject relation or an `A.6.1` application binding. A compact CAL account may omit only an assignment identifier unused by its receiving claim. Ordinary activity not claimed as `U.Work` does not enter this branch.
4. State the local result under its direct predicate and pattern. A `CAL.Acceptance` application yields its exact `pass | fail | unknown` verdict; use A.19 for comparison and selection results, C.16 for measurement results, and C.11 for a decision result. No generic evaluation-result or work-result field substitutes for these objects.
5. When a durable assertion is needed, constitute one `C.2.1` result episteme whose ClaimGraph states that local result, evaluated subject, interpretation basis, polarity or domain status, and uncertainty when current. The episteme is not the domain result and does not create it.
6. Attach source recovery and provenance through A.10/G.6 and currentness through G.11. For an ordinary bounded use below B.3's material-reliance threshold, state the exact A.10 evidence-provenance path and local `RelianceDisposition`; enter B.3 only for an assurance claim or material reliance. A citation, ledger edge, evidence profile, disposition, or assurance record does not establish the work, participant, application, or local result it describes.
7. A later selector, acceptance action, or decision is another governed occurrence. It relies on the result episteme through an exact premise, reference, decision-use, or operation-argument relation; mere storage, citation, or graph membership does not establish actual use.

This chain keeps declaration, execution, local result, result episteme, provenance, bounded reliance, currentness, acceptance, and decision independently recoverable.

#### G.4:4.5 - Extensions (pattern‑scoped; non‑core)

`G.4` supports method‑family and discipline‑specific calculus variations exclusively via pattern‑scoped extensions.

**GPatternExtension block: `G.4:Ext.EvidenceGraphWiring`**
- **PatternScopeId:** `G.4:Ext.EvidenceGraphWiring`
- **GPatternExtensionId:** `EvidenceGraphWiring`
- **GPatternExtensionKind:** `InteropSpecific`
- **GoverningPatternId:** `G.6`
- **Entry:** use only when this CAL pack must cite a shared, addressable G.6 path or slice across more than one downstream consumer.
- **Stop:** omit the block when a local A.10 source-to-use account is sufficient; remove it when no current clause, proof, or example cites the path.
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
- **Entry:** use only when the current task applies a C.18 quality-diversity/archive method and its descriptor, distance, insertion, or archive policy must be pinned for CAL use.
- **Stop:** omit or retire the block when the task has no current archive/QD clause or when those refs no longer change a CAL action.
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
- **Entry:** use only when the current task has a C.19-governed exploration/exploitation budget or probe-accounting rule that changes a CAL clause or failure branch.
- **Stop:** omit or retire the block when no current CAL action consumes those C.19 refs.
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
- **Entry:** use only when C.23-governed SoS-LOG branches currently explain a CAL degrade/abstain path.
- **Stop:** omit or retire the block when those branch/rule ids no longer change a current CAL clause, flow, or explanation.
- **Uses:** `{C.23}`
- **⊑/⊑⁺:** `∅`
- **RequiredPins/EditionPins/PolicyPins (minimum):**
  - `SoSLogRuleId[]`
  - `SoSLogBranchId[]`
  - `FailureBehaviorPolicyId`
- **RSCRTriggerSetIds:** `∅`
- **RSCRTriggerKindIds:** `{RSCRTriggerKindId.PolicyPinChange, RSCRTriggerKindId.MaturityRungChange, RSCRTriggerKindId.TelemetryDelta}`
- **Notes (wiring‑only):** This block only pins branch/rule ids for degrade/abstain explanation; it does not redefine rule semantics.

