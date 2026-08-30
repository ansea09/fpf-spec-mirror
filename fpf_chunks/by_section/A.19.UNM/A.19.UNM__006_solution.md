---
chunk_kind: "child"
pattern_id: "A.19.UNM"
pattern_title: "Unified Normalization Mechanism (UNM)"
section_id: "A.19.UNM:4"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/A.19.UNM/A.19.UNM__006_solution.md"
commit_sha: "8bb4989c9be7fa4b33f0bb7537e4611676ee3087"
heading_path:
  - "A.19.UNM — Unified Normalization Mechanism (UNM)"
  - "A.19.UNM:4 — Solution"
line_start: 32588
line_end: 32784
dependencies:
keywords:
  - "CV→NCV"
  - "NormalizationFixSpec"
  - "NormalizationInvariant[*]"
  - "NormalizationMethodId"
  - "NormalizationMethodInstanceId"
  - "fail-closed tri-state guard (pass"
  - "normalization"
  - "validity window (no implicit “latest”)"
  - "≡_UNM"
---

### A.19.UNM:4 - Solution

UNM is a `U.Mechanism` that normalizes coordinate values using declared method classes, producing:
- normalized values (`NCV`),
- an induced congruence `≡_UNM`,
- and (when needed) a representative policy (`NormalizationFix`) for quotient objects.

UNM is **not** a bag of algorithms. It is a **canonical semantic surface**:
- **Routing** lives in `CN_Spec.normalization` and `CN_Spec.comparability.mode`.
- **Evidence/calibration legitimacy** lives in `C.16 (MM‑CHR)`.
- **Method families** can be supplied by SoTA packs and wired via extensions, without mutating UNM’s surface.

#### A.19.UNM:4.0 - Vocabulary (normative)

**NormalizationMethodId.** A stable token naming a normalization method *kind*, used in `CN_Spec.normalization.methods`.

**NormalizationMethod.** The method *kind* (class) that defines:
1) the **invariants** it preserves (`NormalizationInvariant[*]`),
2) its **closure rules** (composition, and inverses where defined), and
3) its **validity rules** (admitted bearer, scope, qualification window, reference or comparison basis, and intended-use constraints).

**NormalizationMethodDescription.** An editioned epistemic description of a normalization method (bounds, validity region/window, scope constraints, and evidence links governed by `C.16`).
**NormalizationMethodDescriptionRef.** A ref to an editioned `NormalizationMethodDescription`, used in `CN_Spec.normalization.method_descriptions`.

**NormalizationMethodInstanceId.** A stable token naming a concrete, declared application of a normalization method to specific coordinate(s)/slot(s) in a base `U.CharacteristicSpace`, with a named validity window and (when required) evidence pins. Used in `CN_Spec.normalization.instances`.

**NormalizationMethodInstance.** The instance binding itself (conceptual); referenced in specs/logs/gates by `NormalizationMethodInstanceId`.

**CV (CoordinateValue).** A raw coordinate value for a **named measurable slot** in a chart: conceptually `⟨slot_id, raw_value⟩` (plus any chart/slice scoping needed by the chart). UNM re‑parameterizes `CV → NCV` under declared invariants and validity constraints.

**NCV (NormalizedCharacteristicValue).** A normalized **value** for a coordinate (UNM does **not** “normalize characteristics”; it normalizes coordinate values under declared invariants).

**`≡_UNM` (UNM-congruence).** The equivalence relation induced by one chosen `NormalizationMethodInstance` for its declared characteristic-space and CN-Spec editions, bearer, scope/window, reference or comparison basis, and intended comparison.
Two charts (or chart items/views) are `≡_UNM` iff they are related by a finite chain of admissible transformations that preserve the declared invariants.

**NormalizationInvariant.** A named invariant (e.g., unit alignment, polarity, reference plane) declared in `CN_Spec.normalization.invariants` and/or the selected `NormalizationMethodDescription`. Preserving the declared `NormalizationInvariant[*]` is the core admissibility claim for a normalization method instance.

**NormalizationFixSpec.** A declared policy selecting a canonical representative of a `≡_UNM` equivalence class when downstream consumers require a concrete chart item/view. Bound via `CN_Spec.normalization.fix` (otherwise keep quotient objects abstract).
**UNM_id.** An optional identifier in `CN_Spec.normalization.UNM_id?` selecting the UNM **mechanism instance** used by this CN‑frame. This is routing/governance; it is distinct from `NormalizationMethodInstanceId` (method/application).
**ValidityWindow.** A named validity window attached to a `NormalizationMethodInstanceId`, bounding where/when the instance is admissible (no implicit “latest”).

**Relation and reuse boundary.** A normalized value remains tied to the exact normalization-method instance and edition, characteristic-space and CN-Spec editions, bearer, scope and window, reference or comparison basis, evidence, and intended comparison. Reusing it does not by itself establish a transfer relation. Cite an F.9 Bridge or a plane relation only when that relation actually obtains, and state the receiving use separately.
**Lexical guard (strict distinction).** Avoid the word **`map`** / **`mapping`** for UNM transforms (especially `Map`), because `Map` is a specialized FPF term and creates ontology drift. Prefer “normalization”, “re‑parameterization”, “transform under invariants”.
Legacy κ‑notation for normalization is retired; do not re‑introduce it.

#### A.19.UNM:4.1 - UNM as a `U.Mechanism.Intension` (normative)

**Scope note.** This Mechanism.Intension is authored to the `U.Mechanism.Intension` **shape** governed by `A.6.1`. It defines only UNM’s stable *semantic surface*. It does **not** bind project pins (editions/policy‑ids), which belong to the P2W seam (`A.15.3` + `A.19.CHR`), and it does **not** emit `GateDecision`/`GateLog`. It may emit tri‑state `GuardDecision` and Audit pins.

**IntensionHeader**
- `IntensionId`: `UNM`
- `IntensionRef`: `UNM.IntensionRef`
- `Name`: Unified Normalization Mechanism
- `Status`: Stable
- `Version`: `v1.0`
- `SuiteRole`: CHR.normalize (when enabled by CN/CHR routing)

**Imports (cite, don’t duplicate)**
- `A.6.1` (shape: `U.Mechanism.Intension`, specialization discipline)
- `A.6.5` (slot discipline; SlotIndex is a projection)
- `A.19.CHR:4.2` (CHR suite boundary / membership)
- `A.19.CHR:4.2.1` (CHR SlotKind Lexicon)
- `A.19.CHR:4.5` (suite protocols: ordering/optionality; suite closure)
- `A.19.CN` (CN-frame routing: `normalization`, `comparability.mode`)
- `G.0` (CG-frame admissibility gates where required downstream)
- `C.16` (evidence carriers; calibration/validity for normalization legitimacy)
- `A.17/A.18` (measurement meaning & scale lawfulness; not redefined here)

**SubjectBlock**
- `SubjectKind`: `NormalizationMethod classes` (with induced `≡_UNM` over admitted chart items or views)
- `GovernedValueDomain`: coordinate values (`CV`) for named measurable slots in the exact `U.CharacteristicSpace` and CN-Spec editions; UNM normalizes **values**, not characteristics
- `BearerAndUseBoundary`: the exact bearer, scope and window, reference or comparison basis, evidence, and intended comparison declared for those values
- `ExtentRule`: “coordinate values admitted by the selected CN-Spec for this bearer and use, within the normalization-method instance's declared validity window”
- `ResultKinds`:
  - `NormalizedCharacteristicValue (NCV)`
  - `UNM-congruence (≡_UNM)`
  - optional quotient objects and/or `Normalization-fixed` representatives (via `NormalizationFixSpec`)
**SlotIndex (derived projection; minimum)**
- `CharacteristicSpaceSlot : ⟨ValueKind = U.CharacteristicSpace, refMode = U.CharacteristicSpaceRef⟩`
- `CNSpecSlot : ⟨ValueKind = CN‑Spec, refMode = CNSpecRef⟩`
- The `CNSpecSlot` resolves the exact bearer, claim scope and selected slices, qualification window, reference or comparison basis, evidence requirements, and intended comparison; these qualify the use and do not form a generic setting SlotKind.

UNM‑specific slots (must be alias‑docked into the CHR SlotKind lexicon if used across the suite):
- `NormalizationMethodInstanceSlot : ⟨ValueKind = NormalizationMethodInstanceId, refMode = ByValue⟩`
- `NormalizationMethodDescriptionSlot? : ⟨ValueKind = NormalizationMethodDescription, refMode = NormalizationMethodDescriptionRef⟩`
- `NormalizationInvariantSetSlot? : ⟨ValueKind = NormalizationInvariant[*], refMode = ByValue⟩`
- `NormalizationMethodInstancePairSlot? : ⟨ValueKind = NormalizationMethodInstanceId[2], refMode = ByValue⟩`  *(used only by `compose`; roles = {inner, outer})*
- `CoordinateValueSlot : ⟨ValueKind = CV, refMode = ByValue⟩`
- `NCVSlot : ⟨ValueKind = NCV, refMode = ByValue⟩`
- `UNMCongruenceSlot : ⟨ValueKind = UNM‑congruence (≡_UNM), refMode = ByValue⟩`
- `NormalizationFixSlot? : ⟨ValueKind = NormalizationFixSpec, refMode = ByValue⟩`

**Authoring note (didactic).** `NormalizationMethodDescriptionSlot`, `NormalizationInvariantSetSlot`, and `NormalizationFixSlot` are typically *resolved/derived* from `CN_Spec.normalization.{method_descriptions,invariants,fix}` plus the selected `NormalizationMethodInstanceId`. They are listed here because they participate in eligibility/audit semantics — not because every operation takes them as explicit inputs.

**Relation note (not a SlotKind).** A Bridge, kind relation, or plane relation is cited only when the use relies on that obtaining relation. Its declaration and receiving use remain separate from the UNM SlotIndex.

**OperationAlgebra (conceptual)**
1) `apply`
   - Preconditions: `UNM_Eligibility(…) ∈ {pass, degrade}` (fail‑closed; `abstain` ⇒ no NCV output).
   - Inputs: `NormalizationMethodInstanceSlot`, `CoordinateValueSlot`, `CharacteristicSpaceSlot`, `CNSpecSlot`; the selected CN-Spec supplies the exact bearer, scope/window, basis, evidence requirements, and intended comparison.
   - Outputs: `NCVSlot` (+ availability of `UNMCongruenceSlot` for the same method instance)

2) `compose`
   - Purpose: build a composed method (only when explicitly declared lawful).
   - Inputs: `NormalizationMethodInstancePairSlot` (roles = {inner, outer}), `CharacteristicSpaceSlot`, `CNSpecSlot`; both instances must be admitted for the same declared bearer, scope/window, basis, and intended use.
   - Output: `NormalizationMethodInstanceSlot` (new composed `NormalizationMethodInstanceId`), with an explicit validity window and evidence pins.

3) `quotient(≡_UNM)`
- Inputs: `CharacteristicSpaceSlot` (or chart view), `NormalizationMethodInstanceSlot`
- Output: quotient object under `UNMCongruenceSlot`
  (When a concrete representative is required, `NormalizationFixSlot` (`NormalizationFixSpec`) must be declared and used.)

**LawSet (UNM laws; identifiers are stable)**
- **UNM‑L0 (Values, not characteristics).** UNM produces `NCV` as a **value** under declared invariants; it does not redefine the underlying characteristic meaning (measurement meaning remains governed by A.17/A.18 and evidence by C.16).
- **UNM‑L1 (Declared method class gate).** A normalization method instance is admissible only if its method is declared in the allowed method class set: `{ratio:scale, interval:affine, ordinal:monotone, nominal:categorical, tabular:LUT(+uncertainty)}`.
- **UNM‑L1a (Method semantics are governed by the method).** `NormalizationMethod` defines invariants, closure (composition / inverses where defined), and validity rules. UNM consumes these declarations; it does not invent extra admissibility.
- **UNM‑L2 (Congruence is first-class).** Each chosen method instance induces `≡_UNM` over charts/views; equality/comparability decisions that rely on normalization are defined on the quotient (or on a declared fix), not on raw labels.
- **UNM-L2a (Declared-basis locality).** `≡_UNM` holds only for the selected method instance, characteristic-space and CN-Spec editions, bearer, scope and window, reference or comparison basis, and intended comparison. A later use must show that those premises still hold or constitute a new result.
- **UNM‑L3 (Fail‑closed).** If admissibility/evidence is insufficient (or required inputs are missing/stale), UNM does not silently coerce; it yields `abstain` or `degrade` (tri‑state guard discipline) and may surface an explicit freshness/work request (see A.19.UNM:4.5).
  *Didactic reading:* `abstain` ⇒ no lawful NCV/comparability for this slice; `degrade` ⇒ NCV may be produced but must be treated as policy‑gated and auditable (never “quietly good enough”).
- **UNM‑L4 (No implicit indicatorization).** `NCV` does not imply “indicator”; indicator status is a separate policy step (UINDM).
- **UNM-L5 (Relation before reuse).** When a receiving comparison depends on an F.9 Bridge, kind relation, or plane relation, cite the exact obtaining relation, its direction, what it preserves or loses, and the receiving use. A change of bearer, scope, corpus, scale, method, or window is not by itself such a relation. Supported penalties route to the **R-lane only** (never to F/G; if scalarized, into `R_eff`).
- **UNM‑L6 (Time explicitness).** Validity windows are named; no implicit “latest”.
- **UNM‑L7 (Auditability).** The applied method and CN-Spec editions, normalized values, bearer, scope and window, comparison basis, evidence pins, intended comparison, and any actually relied-on Bridge, kind relation, or plane relation must be auditable as refs or pins.
- **UNM-L8 (No shadow writers).** Downstream patterns cite the exact method, CN-Spec, basis, and evidence editions they use; they do not re-author those anchors or make a registry substitute for them.
- **UNM‑L9 (No publish/telemetry ops).** UNM defines no publish/telemetry step. Any publication/telemetry is out of suite closure and does not mutate UNM semantics (`NCV`, `≡_UNM`, quotient/fix); only Audit pins are produced here.

**AdmissibilityConditions**
Definition (UNM‑Eligibility):
`UNM_Eligibility(NormalizationMethodInstanceSlot, CoordinateValueSlot, CharacteristicSpaceSlot, CNSpecSlot) → GuardDecision`
where `GuardDecision ∈ {pass | degrade | abstain}` and follows this predicate semantics:
- **pass** iff all of the following hold:
  - (**CN-Spec binding**) the selected `NormalizationMethodInstanceId` is declared in `CN_Spec.normalization.instances` (or an equivalent declared surface), its method kind is included in `CN_Spec.normalization.methods`, and (if present) it satisfies `normalization.admissible_reparameterizations`; the exact characteristic-space and CN-Spec editions, bearer, claim scope and selected slices, qualification window, reference or comparison basis, and intended comparison are recoverable;
  - (**Target coordinate binding**) the input `CV`’s `slot_id` belongs to the method instance’s declared bound coordinate set;
  - (**Scale‑regime compatibility**) the method kind is compatible with the coordinate’s regime (`ratio:scale | interval:affine | ordinal:monotone | nominal:categorical | tabular:LUT(+uncertainty)`) and preserves the declared `NormalizationInvariant[*]` (from `CN_Spec.normalization.invariants` and/or the method description);
  - (**Validity window**) the method instance’s validity window covers the active slice/time policy (no implicit “latest”);
  - (**Evidence sufficiency when routed into governance**) when `comparability.mode = normalization-based` (or downstream uses `NCV` in gated decisions), the method instance’s evidence pins satisfy `CN_Spec.comparability.minimal_evidence` (structure typically gated by `G.0`; evidence semantics governed by `C.16`).
- **degrade** iff all non‑evidence conditions above hold, but the evidence check does not pass and the declared failure behavior permits producing a policy‑gated degraded `NCV` rather than abstaining.
- **abstain** otherwise (including missing binding, coordinate mismatch, out‑of‑window validity, or evidence failure when the declared failure behavior is abstain).

**Applicability**
UNM is applicable when:
- `CN_Spec.comparability.mode = normalization-based`, or
- a declared downstream step requires “compare-on-invariants” and thus requires explicit normalization.
UNM is typically skipped when `comparability.mode = coordinatewise` (unless an explicit downstream step requires a declared quotient/fix anyway).

**Relation and reuse boundary**
- A normalized value remains local to the exact method instance and edition, characteristic-space and CN-Spec editions, bearer, scope and window, reference or comparison basis, evidence, and intended comparison recorded for it.
- If a receiving use depends on a relation between distinct source-local meanings, cite the exact F.9 Bridge, its direction, what it preserves or loses, and that receiving use. If reference planes differ and the comparison depends on their relation, cite the exact plane relation as a separate claim.
- A changed bearer, scope, corpus, scale, method, or window does not by itself establish either relation. If the bearer kind also changes, state the separate kind relation rather than hiding it inside a Bridge. Any loss penalty remains on the R-lane and is used only when the corresponding relation claim supports it.
**Γ_timePolicy**
- Default: `point` (no implicit “latest”).
- If normalization relies on time windows, the validity window is part of the method instance and must be declared.

**PlaneRegime**
- A normalized value keeps the reference plane declared for its input and intended comparison; normalization creates no implicit plane crossing.
- When a comparison actually relies on a relation between different planes, cite that exact relation, its direction and loss, and keep its use separate from the normalization result.
**Audit**
Audit records MUST include:
- `CNSpecRef.edition` + `comparability.mode`, the exact `U.CharacteristicSpace` edition, and the evaluated bearer
- (when present) `CN_Spec.normalization.UNM_id` (the selected UNM mechanism instance id for this CN-Spec)
- chosen `NormalizationMethodInstanceId`, its validity window, and any `NormalizationMethodDescriptionRef.edition`
- declared `NormalizationInvariant[*]` and `NormalizationFixSpec` (if used)
- any declared admissible re-parameterizations (if present in `CN_Spec.normalization`)
- claim scope and selected slices, reference or comparison basis, intended comparison, and all evidence pins used by the instance
- an exact F.9 Bridge, kind relation, or plane relation only when the recorded result or receiving use actually relies on it, including direction, preserved or lost meaning, and the receiving use
- any emitted `FreshnessRequest` / work request identifiers (when applicable; see A.19.UNM:4.5)

#### A.19.UNM:4.2 - CN-frame wiring: `normalization` and comparability routing (normative-by-reference)

**Tell.** CN-frame does not “do normalization”; it **routes** normalization.
- `comparability.mode ∈ {coordinatewise, normalization-based}` governs whether comparisons are done directly or “normalize-then-compare”.
- `normalization.UNM_id?` selects the UNM mechanism instance used by this CN-frame.
- `normalization.methods / instances / method_descriptions / invariants / fix` provide the declared surface that UNM consumes.
(If present) `normalization.admissible_reparameterizations` constrain which re‑parameterizations count as “admissible” under the declared invariants.
(See CN-frame definition in `A.19.CN`; `A.19.CN` remains the governing pattern of the CN-frame surface. This section only states the UNM consumption/interpretation constraints and does not introduce a shadow spec.)

#### A.19.UNM:4.3 - Evidence and calibration are governed by MM‑CHR (normative-by-reference)

UNM does not claim “this normalization is legitimate” by decree.
Instead, the legitimacy claim is supported by evidence carriers, calibration records, and validity records governed by `C.16 (MM‑CHR)` and referenced from the chosen `NormalizationMethodInstance`.

#### A.19.UNM:4.4 - Didactic rule: quotients or fixes, never “labels” (normative)

When UNM is used to support comparability/acceptance:
- Think in **invariants and equivalence classes** (quotients), not in labels.
- If a concrete representative is needed, declare a `NormalizationFix` explicitly.
Do not silently treat an arbitrary representative as canonical.

#### A.19.UNM:4.5 - P2W and transformation-flow integration note (normative-by-reference)

When UNM is used inside transformation-flow structures/graphs (e.g., `E.18`):
- UNM occurs **before** selection/decision steps.
- If required measurements are **missing or stale**, UNM does not “guess a number”; it surfaces an explicit **freshness/work request** that must be planned in `U.WorkPlanning` and executed in `U.WorkEnactment`.
- A receiving step cites the exact normalized values, method and CN-Spec editions, bearer, scope/window, comparison basis, evidence and intended use. It cites a Bridge, kind relation or plane relation only when its conclusion actually relies on that obtaining relation and keeps any supported loss on the R-lane.
- Downstream consumers cite editioned method, basis and evidence anchors as refs and do not re-author them.

