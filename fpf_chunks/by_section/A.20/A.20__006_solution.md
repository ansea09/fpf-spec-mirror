---
chunk_kind: "child"
pattern_id: "A.20"
pattern_title: "Flow Constraint Validity — Eulerian"
section_id: "A.20:4"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/A.20/A.20__006_solution.md"
commit_sha: "308edacfa2bdb2c60d07e4e10c0deb1f260a6a31"
heading_path:
  - "A.20 — Flow Constraint Validity — Eulerian"
  - "A.20:4 — Solution"
line_start: 33580
line_end: 33731
dependencies:
  - "A.19.SelectorMechanism"
  - "A.21"
  - "C.18"
  - "C.19"
  - "E.17"
  - "E.18"
  - "F.17"
  - "F.9"
  - "G.11"
  - "G.5"
  - "G.6"
keywords:
  - "ConstraintValidity"
  - "Eulerian"
  - "GateFit"
  - "MVPK"
  - "PathSlice"
  - "Sentinel"
  - "SquareLaw"
  - "TransformationFlowStructure"
  - "flow"
---

### A.20:4 - Solution

#### A.20:4.1 - Intent and scope
**Method and mechanism slot guard.** In A.20, `mechanism` names the law-governed operation structure for the step: signature, operation algebra, law set, applicability, guards, transport, audit, and realization relation. `method` appears only when a method-position claim is being made or when a bound-derivation technique or method description is being cited. A shared source label, project-side name, or recognizable change concern may require linked method and mechanism typed values, but CV records the step-local mechanism constraint, `CV.Status`, and witness or refusal; `A.3.1` and `A.3.2` govern the method claim or method-description claim.

**Intent.** Establish the **ConstraintValidity core** for E.18 transformation-flow valuations: the normative set of **internal step constraints** and how their status and witnesses are carried and aggregated, **independent of `GateProfile` fit** (publication follows MVPK without adding new numeric claims). Where CV refers to mechanism `AdmissibilityConditions`, phrase criteria **counterfactually**: *“If the admissibility conditions hold, then the CV explanation applies; otherwise this explanation does not apply.”* Avoid duty verbs unless stating the **normative** CC minima.

**Scope (genus).** CV covers **intra-step** properties checkable from the transformation step signature and, when the step has mechanism-governed semantics, its mechanism-governing definition. The canonical CV classes are **genus-scoped and non-exhaustive**:
`MechanismUnitsCoherence`, `LawSetInvariants`, `AdmissibilityConditionsSatisfaction`, `LipschitzBounds`, `TypeDomainRange`, and—only for **`StructuralReinterpretation`**—`ReinterpretationEquivalence` (correspondence and reversibility witness).

**Species binding (E.18 transformation-flow family).** The above classes bind to the E.18 locus baseline `{Transformation, Signature, Mechanism, WorkPlanning, Work, Check, StructuralReinterpretation}` with **`OperationalGate = Check locus`**; no additional CV classes are introduced here. Species-specific examples and broader flow specializations stay outside this CV core; `StructuralReinterpretation` semantics are received through `E.18`, `A.6.4`, and this pattern when the CV claim is present.

**Out-of-scope (CV):** declaring or translating `ReferencePlane`, `Units`, or `ComparatorSet`; CSLC comparability beyond internal step preservation; Freshness; Role and Channel; Regulated-X; `DesignRunTagConsistency`. These leave CV and use `E.18`, `A.21`, or the named comparator, selector, archive, refresh, evidence, work, safety, or temporal locus when that relation is being claimed.

#### A.20:4.2 - Primary EntityOfConcern and CV classes

**Flow-valuation scope.** A.20 leaves step kinds abstract; CV and GateFit separation applies to any declared E.18 transformation-flow valuation instantiation.
**Species (E.18 transformation-flow family).** E.18 loci bind to `{Transformation, Signature, Mechanism, WorkPlanning, Work, Check, StructuralReinterpretation}`; this set is a **minimum locus baseline** defined in `E.18`. The **species** space (e.g., UNM declaration and use, `SelectionAndTuning`, `WorkPlanning`, `EvaluatingAndRefreshing`, …) is **open-world** and non-exhaustive. `OperationalGate` is the `Check` locus. `StructuralReinterpretation` is **projection-preserving** (no mutation of `⟨L,P,E⃗,D⟩`) and may retarget **EntityOfConcernRef** under CC-TFS-06-EX; see `E.18` and `A.6.4`.

**`AdmissibilityConditionsSatisfaction`** — **If** the declared admissibility conditions hold on the step’s inputs and context, **then** the CV explanation **applies**; **otherwise** this explanation **does not apply**.
**`LipschitzBounds`** — **If** inputs vary within the stated domain \(X\) and perturbations or noise \(≤ ε\), **then** the step’s estimate remains within **δ** of the reference; **otherwise** this explanation **does not apply**.
**`MechanismUnitsCoherence` and `TypeDomainRange`** — **If** units, types, and domains match the mechanism’s signature and closed-world assumptions for the step, **then** the CV explanation **applies**; **otherwise** this explanation **does not apply**.

**Terminology & bindings (normative)**
* **Status and witness lexicon (E.10 discipline).** In CV scope, publications use **Status and Witness** terminology; **GateDecision…** lexemes belong to GateFit (A.21) and do **not** apply to CV.
* **EntityOfConcernRef = KindBridge.** Any CV mention of selected-entity retargeting is interpreted through **`KindBridge (CL^k)`** on **UTS** under `F.9`, `F.17`, `E.17`, `E.18`, and `C.3.3` when the retargeting or bridge claim is present. CV **does not** declare or translate planes, units, or comparators.
* **Retargeting witness binding.** For an E.18 `StructuralReinterpretation` locus, the CV class **`ReinterpretationEquivalence`** SHALL carry **`CV.WitnessRef := ReinterpWitness`** over the addressed `PathSliceId`; the UTS **`SquareLaw-retargeting` witness** is referenced from MVPK and UTS material and **linked** from the CV witness without duplication.
* **`ReinterpWitness` record shape.** The record shape is defined once in A.20:4.7.

#### A.20:4.3 - MVPK Faces (PlainView - TechCard - InteropCard - AssuranceLane)

Minimum pins on faces that carry CV outcomes (**Lean publication** under the selected MVPK profile, without weakening checks):

* **CtxState pins.** `⟨L,P,E⃗,D⟩` on ports and tokens; raw `U.Transfer` preserves them.
* **Path pins.** `PathId` and `PathSliceId` appear where slice-local refresh or reinterpretation witnesses are relevant; valuation semantics are carried by `E.18` plus `A.20`, with `G.11` when refresh wiring is present.
* **CV pins.** `CV.Status ∈ {abstain, pass, degrade, block}`, `CV.WitnessRef?` (refs only).
* **Edition pins.** If a face cites `CG-Spec`, `ComparatorSet`, or `UNM.TransportRegistryPhi`, the face **includes** the compatibility reference (`BridgeCard + UTS row`, with `CL` and `CL^plane`) under `F.9`, `F.17`, `E.17`, and `E.18` for neighboring use. A.20 references this requirement; it does not introduce or modify Bridge and UTS formats.
* **Face scope.** Each face includes `PublicationScopeId` with an **MVPK profile** value of `Min`, `Lite`, `SetReady`, or `Max` — no new publication-face kinds.
* **Register discipline.** Tech names ASCII; twin labels; required LEX tokens follow E.10 (e.g., `SentinelId`, `PathSliceId`, `SliceRefresh`).

> **No new numeric claims.** MVPK faces carry refs, `CV.Status`, and witness or refusal references only; they do **not** introduce fresh computed scalars beyond what the mechanism already entails (MVPK functoriality).

**CV reference names.** In ordinary A.20 prose, an unpublished CV record may be called `CVRef` or `CVCheckRef` as a plain local convenience. When the record is carried on an `A.21` or `E.18` publication face, use the publication lexeme:
`GateCheckRef := { aspect=ConstraintValidity, kind, edition, scope }` with `scope ∈ {lane, locus, subflow, profile}`. This adds no work-occurrence steps and introduces no numeric claims on faces; it records what CV classes were considered and under which editions. `GateCheckRef(aspect=ConstraintValidity)` is a publication lexeme only; it does not make CV a gate. A.20 retains CV class meaning; A.21 consumes only referenced CV results when a gate relation is being claimed.

#### A.20:4.4 - GateChecks (table) — CV only

**Activation predicate (in `E.18` transformation-flow structures).** *Until aggregated `CV.Status=pass`, all GateFit checks return `abstain` (CV=>GF).*
**Role and channel fit guard (GateFit scope).** GateFit checks that involve roles SHALL use **Kernel `U.Role` tokens** (domain = `U.System`) and SHALL NOT consume `TypicalEnactorRoleName` strings from alias tables.

| CV class | Applies when | Publication minimum |
| --- | --- | --- |
| `TypeDomainRange` | The step has a typed signature, declared domain and range, or SlotKind boundary. | `CV.Status + witness or refusal` for the typed relation. |
| `AdmissibilityConditionsSatisfaction` | The mechanism declares admissibility conditions. | `CV.Status + condition ref + witness or refusal`. |
| `LawSetInvariants` | The mechanism has a law or invariant set. | `CV.Status + invariant ref + witness or refusal`. |
| `MechanismUnitsCoherence` | Quantities, scales, units, or reference planes are actually used. | `CV.Status + quantity, unit, and plane refs`; CV may check coherence against already-governed unit and plane refs, but may not author, translate, bridge, or change units or planes. |
| `LipschitzBounds` for stability claims | A perturbation, sensitivity, robustness, continuity, safety-envelope, or stability claim changes the CV use. | Bound or certificate ref under declared assumptions; no universal Lipschitz certificate demand. |
| `ReinterpretationEquivalence` | The step is `StructuralReinterpretation`. | `CV.Status + ReinterpWitness` scoped to the addressed `PathSliceId`. |
| `ReferencePlaneCrossing`, CSLC, Freshness, Role and Channel, Regulated-X, `DesignRunTagConsistency` | A gate, crossing, comparator, freshness, role, work, safety, or DesignRunTag relation is being claimed. | Not CV-only; use GateFit, `A.21`, or the named neighboring locus. |
CV **SHALL NOT** declare or translate `Units`, `ReferencePlane`, or `ComparatorSet`. Gate-mediated crossings and gate-consumed CSLC checks use `E.18` or `A.21` with UNM declaration and bridge discipline. Comparator use, ranking, selection, set-return, archive semantics, and refresh remain with `A.19.SelectorMechanism`, `C.18`, `C.19`, `G.5`, `G.11`, or `A.21` only when those claims are present.

#### A.20:4.5 - SWP matrix (declaration-locus discipline)

* **Writes (faces).** `CV.Status` (and optional `CV.WitnessRef`) only.
* **Referenced editions (ref-only).** Any `CG‑Spec`, `ComparatorSet`, or `TransportRegistryΦ` editions (when referenced); their declarations remain governed by the UNM declaration locus per CC-TFS‑24.

#### A.20:4.6 - CtxState and GateCrossing

* **Crossings only at `OperationalGate(profile)`** (plane, unit, or context) with a **strict exception** for **`StructuralReinterpretation`**: a **projection‑only retargeting** MAY occur without a gate **iff** `⟨L,P,E⃗,D⟩` is preserved, **KindBridge (`CL^k`)** and a **SquareLaw‑retargeting witness** are present on MVPK and UTS material, and the retargeting is **PathSlice‑local** (`PathSliceId` pinned).
* **Projection and EntityOfConcernRef retargeting loci.** For `StructuralReinterpretation`, A.20 may state the CV witness needed for the step, but it does not define a second semantics of projection, published view, EntityOfConcernRef, or retargeting. Interpret those terms through `A.6.4`, `C.2.1`, `C.2.P`, and the relevant UTS `KindBridge (CL^k)` rows under `F.9`, `F.17`, `E.17`, `E.18`, and `C.3.3` when the retargeting or bridge claim is present.
* **Projection and EntityOfConcernRef retargeting normalization (CV use only).** In that imported interpretation, projection is a change of published view coordinates only, and `EntityOfConcernRef` is a Kind-channel change under `CL^k`. A “no unit or plane change” test SHALL verify that `ReferencePlane(src)=ReferencePlane(tgt)` and `CL^plane` is absent (or `= ⊤`), otherwise the step is a gated crossing.
* **Assurance operations on edges.** `ConstrainTo`, `CalibrateTo`, `CiteEvidence`, and `AttributeTo` reside on `U.Transfer` and do **not** alter `⟨L,P,E⃗,D⟩`; plane or unit changes occur only at gates; Φ and `CL^plane` penalties appear in **R-lane**. EntityOfConcernRef retargeting through the kind channel is recorded as **`KindBridge (CL^k)`** on **UTS** under `F.9`, `F.17`, `E.17`, `E.18`, and `C.3.3`; under CC-TFS-06-EX this may appear without a gate only when it is projection-preserving and PathSlice-local.

Terminology for this crossing slice is defined in A.20:4.2, and `ReinterpWitness` shape is defined in A.20:4.7; A.20:4.6 only applies those bindings to CtxState and GateCrossing.

#### A.20:4.7 - SquareLaw

For any gate‑mediated crossing adjacent to CV‑checked steps:
`gate_out ∘ transfer = transfer' ∘ gate_in`.
Inconsistencies lead to `degrade` or `block` per applicable `GateProfile` (GateFit decision).

**retargeting witness shape (normative, UTS-scoped).** A **SquareLaw‑retargeting witness** is a witness record that demonstrates commutativity of a published‑projection retargeting over the addressed **`PathSliceId`**:
  1) identifies **`PathSliceId`** and **`PublicationScopeId`**;
  2) presents a **bidirectional view mapping** between projections either as an **iso** or as a **profunctor optic** (`get : A→B`, `put : (B×A)→A`) satisfying **Put‑Get and Get‑Put** laws;
  3) enumerates the **commuting squares** for the cut‑set edges considered (ids of transfers before and after the retargeting);
  4) declares properties (**invertible?**, **idempotent?**) and the **definedness area**;
  5) cites the **UTS.RowId** and links the **DecisionLog** entries that rely on this witness.
Realizations via **profunctor optics (post‑2017)** are permitted; the optic laws, including lens laws when the selected optic is a lens, serve as the proof template of commutativity.

**CV witness for reinterpretation (normative, CV-scoped).** `CV.ReinterpretationEquivalence` SHALL carry a **ReinterpretationEquivalenceWitness** distinct from the UTS retargeting witness and scoped to the mechanism state over the same **`PathSliceId`**:
  — `PathSliceId`, `PublicationScopeId`, and **definedness region** (domain constraints);
  — a **pair of internal transformations** (or an optic) with **Put‑Get and Get‑Put** obligations **over mechanism state** (not faces);
  — a **list of commuting squares** for the **adjacent raw transfers** (before and after reinterpretation) showing SquareLaw at CV boundary;
  — an explicit **NoHiddenScalarization assertion** (see §4.9) for any comparable return shape;
  — **edition neutrality**: no new editions are declared; only refs and pins appear.
This CV witness links to the UTS `SquareLaw‑retargeting` witness when present, but does not duplicate UTS fields.

**CV witness binding (normative).** For the CV class **`ReinterpretationEquivalence`**, the witness **SHALL** be a `ReinterpWitness` record:
`ReinterpWitness := { PathSliceId, PublicationScopeId, mapping: {kind ∈ {iso, optic}, laws: [PutGet, GetPut]}, commutingSquares: [TransferId], definedOn: PathSliceId, properties: {invertible?: bool, idempotent?: bool}, UTS.RowId, NoHiddenScalarization: true }`.
The record is **PathSlice‑local** and does not declare or translate planes, units, or comparators.

#### A.20:4.8 - Sentinel and PathSlice (PathSlice-local refresh)

* Flows are **valuations** over `U.Transfer`, re-emitting **slice-locally** under explicit refresh rules or edition bumps carried through `E.18`, `A.20`, and `G.11` when refresh wiring is present. CV contributes to the **prepare and refresh** conditions but does not expand scope beyond the addressed `PathSliceId`.
* **Delimitation and planning (normative).** A `PathSlice` **closes** on: (i) any pinned edition change, (ii) Γ‑window boundary relevant to the face, (iii) `GateProfile` change along the addressed `PathSlice`, or (iv) an explicit sentinel rule. **Concurrency:** at most **one active recompute** per `{PathSliceId}`; parallel recomputes are permitted across **distinct** `PathSliceId`s.
* **CV‑triggered refresh (minimum list).** Re‑emit the addressed `PathSliceId` when any holds: (a) `CV.Status` changes across the lattice; (b) `ReinterpWitness` is added, updated, or withdrawn; (c) `AdmissibilityDecl.edition` or `LipschitzBoundRef.edition` changes; (d) updates arrive from `F.9`, `F.17`, `E.17`, or `E.18` bridge and UTS loci, or from `A.19.SelectorMechanism`, `C.18`, `C.19`, `G.5`, or `G.11` comparator and refresh loci; (e) error or timeout transitions to `CV.Status=pass` for a previously `abstain` or `degrade` CV class.

* **CV‑to‑refresh triggers (normative).** A **SliceRefresh(PathSliceId)** SHALL be scheduled when any of the following occurs:
  (`CVRefreshTrigger.StatusFlip`) a **CV status flip** on the slice (`pass↔degrade`, `pass↔block`, or an error or timeout transition to `degrade` or `block` under `GateProfile` rules);
  (`CVRefreshTrigger.ReinterpretationWitness`) arrival of a new **ReinterpretationEquivalenceWitness** or a change in its **definedness region**;
  (`CVRefreshTrigger.AdjacentFactUpdate`) updates to adjacent **UTS** or **Bridge** facts for the slice (e.g., `CL^k`, `BridgeId`, `Φ` and `Ψ` policy ids) under `F.9`, `F.17`, `E.17`, or `E.18`;
  (`CVRefreshTrigger.ReferencedEditionChange`) edition changes referenced by comparator or selection loci on the slice (`A.19.SelectorMechanism`, `C.18`, `C.19`, `G.5`, or `G.11` when the comparator or selection claim is present) (`ComparatorSetRef.edition`, `DescriptorMapRef.edition`, `DistanceDefRef.edition`, …);
  (`CVRefreshTrigger.FreshnessTicketChange`) **FreshnessTicket** or freshness or currentness relation changes that alter the slice window under `A.21`, `B.3`, or `G.11` when the freshness or currentness claim is present;

  (`CVRefreshTrigger.SentinelRule`) sentinel rules explicitly attached to the **PathSliceId**.
Scheduling is **slice‑local**; recompute does not fan‑out beyond the addressed `PathSliceId`.

  **Id‑scheme:** `PathSliceId := PathId × Γ_time selector × ReferencePlane × SentinelFingerprint × IterationCounter`.
  **Locking for replay:** within a recompute, the effective `E⃗` is **frozen**; outputs carry a **replay fingerprint** resolvable via `DecisionLog`.

#### A.20:4.9 - ReturnShape and CSLC (comparability discipline)

When a comparable, set-valued, archive, or partially ordered return shape is declared for the step, CV checks that the step did not internally destroy that return shape; **no hidden scalarization**. If no declared return shape is being claimed, do not create a ReturnShape or NoHiddenScalarization check. Any comparator citation is **ref-only** and, if editions are cited, SHALL include `Bridge+UTS` through the current bridge and terminology loci (`F.9`, `F.17`, `E.17`, `E.18`). Comparator use, ranking, selection, archive semantics, and refresh remain with `A.19.SelectorMechanism`, `C.18`, `C.19`, `G.5`, `G.11`, or GateFit (`A.21`) when those claims are present. CV only checks preservation of the already-declared return shape inside the current step.

Under **`StructuralReinterpretation`**, **projection changes MUST NOT introduce hidden scalarization**; set‑return semantics remain intact; comparator cites stay ref‑only with UTS discipline.

**Detectable indicators of hidden scalarization (normative checklist).** A face **SHALL** be flagged when any holds:
  (H1) introduction of a **new scalar** not entailed by the mechanism, or any **cardinality‑reducing** fold of a set return (e.g., argmax or best‑of) without a cited **ComparatorSetRef**;
  (H2) omission of a required **ComparatorSetRef** or its **edition pins** where comparison is implied;
  (H3) presence of an **order-imposing coordinate** without a **CoordinatePolicy** and declared scale policy, units, or invalid-operation notes;
  (H4) cross‑plane or cross‑unit numeric combination without a **Bridge+UTS** row;
  (H5) for `StructuralReinterpretation`, any change of return **plane or units** (violates “projection‑only”).
Failing (H1–H5) degrades or blocks per GateProfile (§4.4 and CC-TFS‑21a).

#### A.20:4.10 - Γ‑windows and freshness

* No implicit *latest*. Any face expected to be consumed at compare or launch pins `Γ_time`; freshness checks occur at gates; CV neither issues Freshness tickets nor evaluates staleness. Use `A.21`, `B.3`, `C.27`, or `G.11` when a freshness, temporal-claim, or refresh relation is present.
* **Granularity of Γ (normative).** Γ SHALL be one of: **snapshot** (`effective_at=t`) or **interval** (`[t₀,t₁)` with a named folding policy). Faces SHALL carry the selector used.
* **CV time‑stamping.** Each CV computation records `t_cv` and the **Γ selector** it assumed; replay binds `t_cv` to `PathSliceId`.
* **Temporal policy types (binding).** Γ‑pins refer to the **canonical selectors** of §22 (*`effective_at`*, *`latest_effective_before`*, *`windowed(W, policy)`*) and to **folding policies** that are **IDEM, MONO, and WLNK‑safe**. Units and time scales **SHALL** be explicit. Overrides of the default **weakest‑link** fold **SHALL** cite CAL proofs of monotonicity and boundary behavior.

#### A.20:4.11 - Unknown, timeout, and error policy

Each CV class yields one `CV.Status` value: `abstain`, `pass`, `degrade`, or `block`. Errors and timeouts at CV stage imply **`CV.Status != pass`**; therefore GateFit abstains by the global activation predicate and any GateFit‑oriented explanation **does not apply**. The aggregated `CV.Status` uses the join on `abstain <= pass <= degrade <= block` (neutral = `abstain`; absorbing = `block`).
**Minimal default (`GateProfile`-bound, normative):** **Lean and Core ⇒ error or timeout maps to `degrade`**, **SafetyCritical and RegulatedX ⇒ error or timeout maps to `block`**; `unknown` folds per GateCheck policy (safety‑default: `degrade`). (Consistent with **CC-TFS‑22**.)

#### A.20:4.12 - Idempotency and congruence discipline

Any publication consumed by an `A.21` gate decision uses the `A.21` decision-stability witness for input equivalence and idempotency; use `G.6` or `G.11` when an A.10 evidence relation visibility or refresh-implication claim is present. A.20 does not introduce keys, hashes, or cache policies.

**Minimal lexeme set for CV‑adjacent equivalence (normative).** Where an `A.21` gate decision consumes CV outcomes, the **equivalence witness** SHALL identify at least: `{PathSliceId, GateProfileId, Γ selector (+window bounds if interval), E⃗ editions vector for cited registries, ReturnShape kind (if comparable), CV class and kind set considered}`. Changing any of these breaks equivalence and triggers re-aggregation.

