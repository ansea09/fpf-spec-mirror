---
chunk_kind: "child"
pattern_id: "A.6.1"
pattern_title: "U.Mechanism - Law‑governed application to a SubjectKind over a BaseType"
section_id: "A.6.1:4"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/A.6.1/A.6.1__005_solution.md"
commit_sha: "04dd733fb18b66d3a640d11758e0af22ea253fd8"
heading_path:
  - "A.6.1 — U.Mechanism - Law‑governed application to a SubjectKind over a BaseType"
  - "A.6.1:4 — Solution"
line_start: 9087
line_end: 9223
dependencies:
  - "A.19"
  - "A.2.6"
  - "A.6.0"
  - "C.16"
  - "E.10.D1"
  - "G.10"
  - "G.11"
keywords:
  - "AdmissibilityConditions"
  - "Bridge‑only"
  - "LawSet"
  - "Mechanism"
  - "OperationAlgebra"
  - "Transport"
---

### A.6.1:4 - Solution

#### A.6.1:4.1 - **Mechanism Intension**

A `U.Mechanism` **publishes**
        `U.Mechanism.Intension := ⟨IntensionHeader, Imports,
                SubjectBlock := ⟨SubjectKind, BaseType, SliceSet, ExtentRule, ResultKind?⟩,
                SlotIndex, OperationAlgebra, LawSet, AdmissibilityConditions,
                Applicability, Transport, Γ_timePolicy, PlaneRegime, Audit⟩`
and admits Realizations that respect it. The shape is **notation‑independent** and **conceptual** (no tooling, storage, or CI metadata).

* **A.6.0 alignment (normative).** `U.Mechanism` is a specialisation of `U.Signature` (A.6.0). A mechanism publication **SHALL** include the universal four‑row Signature Block (*SubjectBlock / Vocabulary / Laws / Applicability*). The canonical mapping is:
  – **SubjectBlock** ↔ `SubjectBlock`
  – **Vocabulary** ↔ `OperationAlgebra` (including inline SlotSpecs per A.6.0:4.1.1 / A.6.5)
  – **Laws** ↔ `LawSet`
  – **Applicability** ↔ `Applicability`
  `SlotIndex` is a mechanism-only **index/projection** over SlotSpecs used by `OperationAlgebra` (and any extra SlotSpecs used only by `AdmissibilityConditions`); it does **not** introduce a fifth Signature row and does not relax A.6.0:4.1.1.
  Mechanism‑only additions are `AdmissibilityConditions`, `Transport`, `Γ_timePolicy`, `PlaneRegime`, and `Audit`; they extend the Signature without contradicting its intension/specification split (A.6.0; CC‑A.6.0‑5).

* **IntensionHeader.** `id` (PascalCase), `version` (SemVer), `status` (draft/review/stable/deprecated).
  **SignatureManifest coupling (normative).** If the mechanism is intended to be imported/reused, it MUST include a `SignatureManifest` (A.6.0:4.4.1) immediately above its Signature Block. When both are present:
  – `IntensionHeader.id = SignatureManifest.id`
  – `IntensionHeader.version = SignatureManifest.version`
  – `IntensionHeader.status = SignatureManifest.status` (when `status` is present)
  – `Imports = SignatureManifest.imports`
  and any public symbols minted by the Mechanism’s Signature Block **MUST** appear in `SignatureManifest.provides`.
  Avoid duplicating `imports/provides` elsewhere: dependency edges and exported names live in the manifest; operational details live in the mechanism.

* **Imports.** (Optional) SignatureIds that supply non‑Kernel symbols used by this mechanism’s Signature Block and/or this mechanism’s operation algebra. If the mechanism includes a `SignatureManifest`, then `Imports` MUST equal `SignatureManifest.imports`. If present, the list MUST be acyclic and MUST respect the layering rule in A.6.0:4.4.1 (E.5.3 + E.10).
* **BaseType.** A `U.Type` the mechanism ranges over. CHR spaces (e.g., a `U.CharacteristicSpace`/chart family) appear here **as types**; outside CHR, use set‑typed `U.Type`s. A conformant `U.Mechanism` publication **MUST NOT** mint a new core type here; it **MUST** reference existing `U.Type`s. If planes differ, state the **ReferencePlane** policy (see *PlaneRegime*).
* **SubjectKind / SliceSet / ExtentRule / ResultKind? / SlotIndex.**
  • **SubjectKind.** The intensional kind acted upon (C.3.1/3.2), separate from quantification.
  • **SliceSet.** The addressable set of Context slices (USM: **ContextSliceSet**).
  • **ExtentRule.** A rule yielding `Extension(SubjectKind, slice)` (C.3.2), used as the quantifier’s domain.
  • **ResultKind?** Optional intensional kind for outputs of `OperationAlgebra`.
  • **SlotIndex.** A set (or map) of SlotSpecs `SlotSpec = ⟨SlotKind, ValueKind, refMode⟩` (A.6.0:4.1.1; A.6.5) covering every argument position used by **OperationAlgebra** and **AdmissibilityConditions**. SlotKinds are stable names for substitution and specialisation; parameter names/indices are presentation only.
    For **Vocabulary-level** operators, SlotSpecs remain declared **in each operator’s parameter block** (A.6.0:4.1.1). `SlotIndex` is an extracted index that **MUST** be mechanically derivable from those declarations (plus any guard-only SlotSpecs). Guard-only SlotSpecs **SHALL** be authored as part of the **AdmissibilityConditions** predicate signatures (not only as prose) so they remain mechanically extractable.
    **Shorthand views (didactic only).** Authors MAY include a simple name→ValueKind list (a `ValueKindView`) as a didactic projection of SlotSpecs, but it SHALL NOT replace SlotSpecs (`SlotKind/ValueKind/refMode`) in normative Mechanism definitions. If present, it MUST be mechanically derivable from `SlotIndex` (e.g., `ValueKindView = π_value(SlotIndex)` by dropping `refMode`). The colloquial label **ParamKind** is permitted only in prose as a synonym for the `ValueKind` component of a SlotSpec; it MUST NOT be introduced as a field name, token, or type.
* **OperationAlgebra.** Named operations whose signatures are expressed over SlotKinds from `SlotIndex` (A.6.5); **no implicit parameters**. For every n‑ary operator, its Vocabulary declaration **SHALL** publish SlotSpec triples per argument position (A.6.0:4.1.1); positional indices are presentation only. Examples:
  • **USM:** `∈, ⊆, ∩, SpanUnion, translate, widen, narrow, refit`.
  • **UNM:** `apply(method)`, `compose`, `quotient(≡_UNM)`; **normalize‑then‑compare**.

* **LawSet.** Equations/invariants (no proofs here). **Admissions/eligibility tests belong under AdmissibilityConditions, not here.** Laws **MUST** be compatible with CHR legality where numeric comparison/aggregation is induced. Examples:
  • **USM:** serial **intersection**; **SpanUnion** only where a **named independence assumption** is satisfied (state features or characteristics, validity window, evidence class); `translate` uses declared Bridges; **Γ_time** is mandatory.
  • **UNM:** **scale‑appropriate** transforms — ratio→positive‑scalar; interval→affine; ordinal→monotone; nominal→categorical; `tabular:LUT(+uncertainty)`.
  *(A conformant `U.Mechanism` publication **MUST NOT** mint a new Kernel token for “certificate”; if such a type is later required, it **MUST** follow DRR/LEX minting.)*

* **AdmissibilityConditions.** Deterministic, **context‑local** *operational* guard predicates that **fail closed** (e.g., “Scope covers TargetSlice” with named **Γ_time**; “NormalizationMethod class + validity window named”). Predicate arguments **SHALL** be declared via SlotSpecs from `SlotIndex` (A.6.5), not as implicit positional parameters. Unknowns **→ {degrade | abstain}**; never coerce to 0/false.

* **Applicability.** Binding to a **`U.BoundedContext`** with stance/plane/time notes and any **CG‑Spec/MM‑CHR** legality claims; cross‑context use is declared via **Transport** only.

* **Transport.** **Bridge‑only** semantics for cross‑context / cross‑plane use: name the Bridge and channel (`Scope|Kind`) per **F.9**, and record **ReferencePlane**(src,tgt) per **C.2.1**. **Terminology:** this `Transport` clause is a declarative policy surface; it does **not** introduce a `U.Transfer` edge (see **E.18** term separation). The Transport clause **MUST NOT** restate CL ladders, `CL^plane`, or Φ/Ψ tables; it **MUST** reference the applicable policy ids / registries instead; penalties **route to R/R_eff only** and **never** mutate F/G (per **B.3**). Crossings are explicit; **no implicit crossings**. Where **USM** or **KindBridge** are used together, apply the **two‑bridge rule** (scope CL and kind `CL^k` penalties handled **separately** to the Reliability channel (**R**/**R_eff**)).

* **Γ_timePolicy.** Point/window/policy; **no implicit “latest.”** Validity windows are **named**; **required** whenever guards reference time.
* **PlaneRegime.** Declare `ReferencePlane` on values/paths; when planes differ, name **CL^plane** and apply a **Φ_plane** policy (Part F/B.3). Plane penalties **do not** change CL; route to **R/R_eff** only; **F/G** stay invariant.

* **Audit.** Conceptual audit surface only (no data/telemetry workflows): crossings are publishable on **UTS**; surface **policy‑ids** rather than tables. Edition pins and regression hooks (if any) are referenced by id; operational details remain out of scope.
* **SignatureBlock alignment.** The referenced Signature’s four‑row Block (A.6.0) is canonical. Any mechanism rendering MUST preserve that block (or an explicit projection of it) and MUST obey A.6.5 for n‑ary argument discipline. SlotKinds and SlotSpecs in `SlotIndex` remain part of the **Vocabulary** row (A.6.0) and **MUST** obey A.6.5.

* **Compatibility with A.6.\*** A.6.1 is a strict specialisation of A.6.0: the canonical four-row Signature Block remains the meaning carrier; additional Mechanism fields (algebra, carriers, evidence) must not introduce new semantic rows or shadow the signature's `imports`/`provides`.

#### A.6.1:4.2 - U.MechMorph - Refinement, Extension, Equivalence & Composition

**Intent.** Provide structure‑preserving **relations & constructors** between mechanisms.
**Definitions.**

* **Refinement** `M′ ⊑ M`: narrows the **SubjectBlock** and/or **SlotSpecs** (ValueKinds/refMode for inherited SlotKinds) and/or **strengthens** `LawSet`/`AdmissibilityConditions` (safe substitution; Liskov‑style). A Refinement **MUST NOT** rename SlotKinds or add new required arguments to inherited operations.
* **Extension** `M ⊑⁺ M″`: **adds operations** (and any new SlotKinds used only by those new operations) without weakening existing Laws/Guards; old programs remain valid (conservative extension).
* **Equivalence** `M ≡ M′`: there exists a bijective mapping between Subjects/ops preserving/reflecting **LawSet** (up‑to‑isomorphism on **BaseType** and **OperationAlgebra**).

* **Quotient** `M/≈`: factor by a **congruence** (e.g., **≡_UNM** for charts).

* **Product** `M×N`: independent **BaseTypes**; ops are component‑wise; ensures **no illegal cross‑ops** (e.g., set‑algebra discipline for `SpanUnion`). Where independence is claimed, **name and justify** the assumption (do not mint new Kernel types here).

##### A.6.1:4.2.1 - Specialisation relation chains (normative)

Many families need a **generic** mechanism at the top (e.g., “select anything”) and progressively **specialised** mechanisms below (e.g., “select a method by decision theory”, “select a telemetry pack”). To keep such specialisation chains **modular** and to prevent leakage across the chain:

1. **Explicit parent + morphism kind.** Any mechanism that specialises another **MUST** name its parent and declare whether the step is a **Refinement** (`⊑`) or an **Extension** (`⊑⁺`). A specialisation family **MUST** be acyclic (a DAG).

2. **SlotKind invariance across levels.** For every inherited operation/guard predicate, SlotKinds are invariant (A.6.5). A specialisation step **MUST NOT** rename an inherited SlotKind, change its documented semantics, or rely on positional re‑ordering instead of SlotKind identity.

3. **ValueKind monotonicity.** A Refinement MAY narrow `ValueKind` (i.e., `ValueKind′ ⊑ ValueKind` in Kind‑CAL) and/or `refMode` for an inherited SlotKind, and MAY strengthen Laws/Guards. It **MUST NOT** widen ValueKinds or relax Guards; otherwise mint a new parent mechanism or publish an adapter mechanism.

4. **No new mandatory inputs to inherited operations.** If a specialisation needs extra inputs, it **MUST** introduce a new operation (Extension) or an adapter mechanism; it **MUST NOT** retrofit new required parameters into an inherited operation signature.

5. **No upward leakage.** A root mechanism in a specialisation chain **SHOULD** mention only the most general ValueKinds required by its SlotSpecs and Laws. Domain-specific policies, generators, and evaluation packs belong in specialised mechanisms that refine slots or add operations.

*Informative selector specialisation-chain sketch.* `SelectorMechanism` can declare a stable slot interface (`CandidateSetSlot`, `ComparisonResultSlot`, `CriteriaSlot`, `ContextSlot`, `SelectionSlot`) with generic ValueKinds. `SelectorMethodMechanism ⊑ SelectorMechanism` then narrows `CandidateSetSlot.ValueKind` to `U.Method` and (by Extension) adds decision‑theory specific slots/ops; an OEE generator is authored as a separate mechanism that produces candidate/criteria packs consumed by the selector.
**Transport** `Bridge⋅M`: lifts across Contexts/planes; names **CL/CL^k/CL^plane** regimes; penalties → **`R_eff` only**; **UTS row** recommended for publication; **ReferencePlane(src,tgt)** recorded. If mapping losses are material, **narrow** the mapped set or publish an **adapter** (best practice).

**Passing example.** `USM′ = USM + “publish named independence‑assumption evidence for SpanUnion”` ⇒ **Refinement** (strengthened law; substitution‑safe).
**Normalization quotient.** `UNM / ≡_UNM` exposes **compare‑on‑invariants** surfaces for CPM/USCM (normalize‑then‑compare).

#### A.6.1:4.3 - U.MechAuthoring - Instantiation template

**MechanismDescription (E.8 Tell–Show–Show; I/D/S‑compliant):**
`Mechanism: U.<Name>`  *(Kernel conceptual description; no tooling fields)*
`Imports: <Signatures / U.Types>` - `SubjectBlock: <SubjectKind, BaseType, SliceSet, ExtentRule, ResultKind?>` - `SlotSpecs: <SlotIndex (A.6.5)>` - `OperationAlgebra: <operators with SlotKinds>` - `LawSet: <equations/invariants>` - `AdmissibilityConditions: <admission predicates with SlotKinds; Γ_time>` - `Transport: <Bridge channels; CL/CL^k/CL^plane named; ReferencePlane(src,tgt)>` - `PlaneRegime: <world|concept|episteme rules>`

#### A.6.1:4.4 - MechFamilyDescription & MechInstanceDescription

* **MechFamilyDescription**: `{Mechanism.Intension, Realizationα, Realizationβ, …}` — each Realization may **tighten** (never relax) Laws (Liskov‑style).

* **MechInstanceDescription**: `{Mechanism.Intension@Context, Windows, named Φ/Ψ/Φ_plane regimes, BridgeIds}` — a **conceptual instance**; operational telemetry/workflows are out of scope.

#### A.6.1:4.5 - Defaults

* **Local‑first semantics.** All judgments are **context‑local**; crossings are **explicit** and **costed** (CL→R only).
* **Compliance‑first comparability.** Numeric comparison/aggregation requires **CG‑Spec** (lawful **SCP**, Γ‑fold, MinimalEvidence); **partial orders return sets**; **no ordinal means**.
* **Tri‑state discipline.** `unknown → {degrade|abstain}`; `sandbox/probe‑only` is a **LOG branch** with a policy‑id (no implicit `unknown→0/false`).
* **R‑only penalties.** **Φ/Ψ/Φ_plane** are **monotone and bounded**; penalties route to **`R_eff` only**; **F/G invariant**.

#### A.6.1:4.6 - Born‑via‑A.6.1 sketch (informative)

**PTM — Publication & Telemetry Mechanism (informative)**
**BaseType:** `SoTA‑Pack(Core)`, `PathId/PathSliceId`, `PolicyId`. **OperationAlgebra:** emit **selector‑ready** packs with parity pins and **telemetry stubs**; listen for edition/illumination bumps; trigger **slice‑scoped** refresh.
**LawSet:** **no change of dominance defaults** unless CAL policy promotes; edition-aware refresh.
**Guards:** **GateCrossing visibility harness** blocks publication on missing crossing attestations (BridgeCard+UTS row, ReferencePlane, CL/CL^k/CL^plane, Φ/Ψ policy-ids), on lane-purity violations (CL→R only; F/G invariant), or on lexical SD violations (E.10).
**Transport/Audit:** **G.10/G.11** publication & refresh semantics (CL routing to **R/R_eff**).

*Informative SoTA:* telemetry hooks align with post‑2015 quality‑diversity families (CMA‑ME/MAE, DQD/MEGA) and open‑ended methods (POET‑class) when monitored via illumination telemetry rather than scored.

#### A.6.1:4.7 - 60‑second didactic script

> *“To mint a mechanism, fill a **Mechanism.Intension**: declare **SubjectBlock** (**SubjectKind**, **BaseType**, **SliceSet**, **ExtentRule**, **ResultKind?**) and **SlotSpecs** (use a `SignatureManifest` if it is reusable); then **OperationAlgebra/Laws/AdmissibilityConditions** and **Γ_time**; define **Transport** (Bridge/CL with penalties to R only), and **Audit** (UTS + Path pins). USM and UNM are already such mechanisms; the same template births comparison, scoring, and publication mechanisms—safely bound to **CG‑Spec**—without leaving the kernel grammar.”*

#### A.6.1:4.8 - Quick “builder’s” checklist (author‑facing)

1. Draft a **run↔design charter**: why this Mechanism, which **guard surfaces** and **comparability** are in scope; which `DesignRunTag`/`CtxState.locus` boundary it mediates; is a **Γ_m (CAL)** builder needed?

* Fill **Mechanism.Intension** (**SubjectBlock**, **SlotSpecs**, **OperationAlgebra**, **LawSet**, **AdmissibilityConditions**, **Applicability**, **Transport**, **Γ_timePolicy**, **PlaneRegime**, **Audit**).

* Bind **CHR legality & CG‑Spec** when comparing/aggregating (ComparatorSet, ScaleComplianceProfile (SCP), MinimalEvidence, Γ‑fold).

Ship **UTS + G.10**; wire **G.11** telemetry (PathSlice‑keyed); ensure penalties **route to `R_eff` only**.

