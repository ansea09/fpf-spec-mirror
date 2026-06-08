---
chunk_kind: "child"
pattern_id: "A.6.1"
pattern_title: "U.Mechanism - Law‑governed application to a SubjectKind over a BaseType"
section_id: "A.6.1:4"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/A.6.1/A.6.1__006_solution.md"
commit_sha: "b22b6993b3e94f7896d5dc1cd011af7bc3f49b0d"
heading_path:
  - "A.6.1 — U.Mechanism - Law‑governed application to a SubjectKind over a BaseType"
  - "A.6.1:4 — Solution"
line_start: 9244
line_end: 9380
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

#### A.6.1:4.1 - **Mechanism Declaration**

A `U.Mechanism` **publishes**
        `MechanismDeclaration := ⟨DeclarationHeader, Imports,
                SubjectBlock := ⟨SubjectKind, BaseType, SliceSet, ExtentRule, ResultKind?⟩,
                SlotIndex, OperationAlgebra, LawSet, AdmissibilityConditions,
                Applicability, Transport, Γ_timePolicy, PlaneRegime, Audit⟩`
and admits Realizations that respect it. The shape is **notation‑independent** and **conceptual** (no tooling, storage, or CI metadata).

* **A.6.0 alignment (normative).** `U.Mechanism` is a specialisation of `U.Signature` (A.6.0). A mechanism publication **SHALL** include the universal four-row Signature Block (*SubjectBlock, Vocabulary, Laws, Applicability*). The canonical mapping is:
  – **SubjectBlock** ↔ `SubjectBlock`
  – **Vocabulary** ↔ `OperationAlgebra` (including inline SlotSpecs per A.6.0:4.1.1 and A.6.5)
  – **Laws** ↔ `LawSet`
  – **Applicability** ↔ `Applicability`
  `SlotIndex` is a mechanism-only **index projection** over SlotSpecs used by `OperationAlgebra` and any extra SlotSpecs used only by `AdmissibilityConditions`; it does **not** introduce a fifth Signature row and does not relax A.6.0:4.1.1.
  Mechanism-only additions are `AdmissibilityConditions`, `Transport`, `Γ_timePolicy`, `PlaneRegime`, and `Audit`; they extend the Signature without contradicting the A.6.0 separation between declaration and realization.

* **DeclarationHeader.** `id` (PascalCase), `version` (SemVer), `publicationState` (draft, candidate, stable, or deprecated).
  **SignatureManifest coupling (normative).** If the mechanism is intended to be imported or reused, it MUST include a `SignatureManifest` (A.6.0:4.4.1) immediately above its Signature Block. When both are present:
  – `DeclarationHeader.id = SignatureManifest.id`
  – `DeclarationHeader.version = SignatureManifest.version`
  – `DeclarationHeader.publicationState = SignatureManifest.publicationState` (when `publicationState` is present)
  – `Imports = SignatureManifest.imports`
  and any public symbols minted by the Mechanism’s Signature Block **MUST** appear in `SignatureManifest.provides`.
  Avoid duplicating `imports` and `provides` elsewhere: dependency edges and exported names live in the manifest; operational details live in the mechanism.

* **Imports.** (Optional) SignatureIds that supply non-Kernel symbols used by this mechanism’s Signature Block or this mechanism’s operation algebra. If the mechanism includes a `SignatureManifest`, then `Imports` MUST equal `SignatureManifest.imports`. If present, the list MUST be acyclic and MUST respect the stratum dependency rule in A.6.0:4.4.1 (E.5.3 and E.10).
* **BaseType.** A `U.Type` the mechanism ranges over. CHR spaces (e.g., a `U.CharacteristicSpace` or chart family) appear here **as types**; outside CHR, use set-typed `U.Type`s. A conformant `U.Mechanism` publication **MUST NOT** mint a new core type here; it **MUST** reference existing `U.Type`s. If planes differ, state the **ReferencePlane** policy (see *PlaneRegime*).
* **SubjectKind, SliceSet, ExtentRule, ResultKind?, and SlotIndex.**
  • **SubjectKind.** The EntityOfConcern kind acted upon (C.3.1 and C.3.2), separate from quantification.
  • **SliceSet.** The addressable set of Context slices (USM: **ContextSliceSet**).
  • **ExtentRule.** A rule yielding `Extension(SubjectKind, slice)` (C.3.2), used as the quantifier’s domain.
  • **ResultKind?** Optional output kind for outputs of `OperationAlgebra`.
  • **SlotIndex.** A set of SlotSpecs `SlotSpec = ⟨SlotKind, ValueKind, refMode⟩` (A.6.0:4.1.1; A.6.5) covering every argument position used by **OperationAlgebra** and **AdmissibilityConditions**. SlotKinds are stable names for substitution and specialisation; parameter names and numeric indices are presentation only.
    For **Vocabulary-level** operators, SlotSpecs remain declared **in each operator’s parameter block** (A.6.0:4.1.1). `SlotIndex` is an extracted index that **MUST** be mechanically derivable from those declarations (plus any guard-only SlotSpecs). Guard-only SlotSpecs **SHALL** be declared as part of the **AdmissibilityConditions** predicate signatures (not only as prose) so they remain mechanically extractable.
    **Shorthand views (didactic only).** A mechanism publication MAY include a simple name-to-ValueKind list (a `ValueKindView`) as a didactic projection of SlotSpecs, but it SHALL NOT replace SlotSpecs (`SlotKind`, `ValueKind`, `refMode`) in normative Mechanism definitions. If present, it MUST be mechanically derivable from `SlotIndex` (e.g., `ValueKindView = π_value(SlotIndex)` by dropping `refMode`). The colloquial label **ParamKind** is permitted only in prose as a synonym for the `ValueKind` component of a SlotSpec; it MUST NOT be introduced as a field name, token, or type.
* **OperationAlgebra.** Named operations whose signatures are expressed over SlotKinds from `SlotIndex` (A.6.5); **no implicit parameters**. For every n‑ary operator, its Vocabulary declaration **SHALL** publish SlotSpec triples per argument position (A.6.0:4.1.1); positional indices are presentation only. Examples:
  • **USM:** `∈, ⊆, ∩, SpanUnion, translate, widen, narrow, refit`.
  • **UNM:** `apply(method)`, `compose`, `quotient(≡_UNM)`; **normalize‑then‑compare**.

* **LawSet.** Equations and invariants (no proofs here). **Admission and eligibility tests belong under AdmissibilityConditions, not here.** Laws **MUST** be compatible with CHR legality where numeric comparison or aggregation is induced. Examples:
  • **USM:** serial **intersection**; **SpanUnion** only where a **named independence assumption** is satisfied (state features or characteristics, validity window, evidence class); `translate` uses declared Bridges; **Γ_time** is mandatory.
  • **UNM:** **scale‑appropriate** transforms — ratio→positive‑scalar; interval→affine; ordinal→monotone; nominal→categorical; `tabular:LUT(+uncertainty)`.
  *(A conformant `U.Mechanism` publication **MUST NOT** mint a new Kernel token for “certificate” inside the mechanism definition. Any needed Kernel token requires an accepted FPF naming and kind decision under E.10 and F.18.)*

* **AdmissibilityConditions.** Deterministic, **context-local** *operational* guard predicates that **fail closed** (e.g., “Scope covers TargetSlice” with named **Γ_time**; “NormalizationMethod class + validity window named”). Predicate arguments **SHALL** be declared via SlotSpecs from `SlotIndex` (A.6.5), not as implicit positional parameters. Unknowns **→ {degrade, abstain}**; never coerce to 0 or false.

* **Applicability.** Binding to a **`U.BoundedContext`** with stance, plane, time notes, and any **CG-Spec and MM-CHR** legality claims; cross-context use is declared via **Transport** only.

* **Transport.** **Bridge-only** semantics for cross-context or cross-plane use: name the Bridge and channel (`Scope` or `Kind`) per **F.9**, and record **ReferencePlane**(src,tgt) per **C.2.1**. **Terminology:** this `Transport` clause is a declarative policy surface; it does **not** introduce a `U.Transfer` edge (see **E.18** term separation). The Transport clause **MUST NOT** restate CL, `CL^plane`, Φ, or Ψ policy tables; it **MUST** reference the applicable policy ids or registries instead; penalties are recorded in **R or R_eff only** and **never** mutate **F or G** (per **B.3**). Crossings are explicit; **no implicit crossings**. Where **USM** and **KindBridge** are used together, apply the **two-bridge rule**: scope CL and kind `CL^k` penalties are handled **separately** in the Reliability channel (**R** or **R_eff**).

* **Γ_timePolicy.** Point, window, or policy; **no implicit “latest.”** Validity windows are **named**; **required** whenever guards reference time.
* **PlaneRegime.** Declare `ReferencePlane` on values or paths; when planes differ, name **CL^plane** and apply a **Φ_plane** policy (Part F and B.3). Plane penalties **do not** change CL; record them in **R or R_eff** only; **F and G** stay invariant.

* **Audit.** Conceptual audit surface only (no data or telemetry workflow): crossings are publishable on **UTS**; cite **policy-ids** rather than copying policy tables. Edition pins and regression hooks, if any, are referenced by id; operational details remain out of scope.
* **SignatureBlock alignment.** The referenced Signature’s four‑row Block (A.6.0) is canonical. Any mechanism rendering MUST preserve that block (or an explicit projection of it) and MUST obey A.6.5 for n‑ary argument discipline. SlotKinds and SlotSpecs in `SlotIndex` remain part of the **Vocabulary** row (A.6.0) and **MUST** obey A.6.5.

* **Compatibility with A.6.\*** A.6.1 is a strict specialisation of A.6.0: the canonical four-row Signature Block remains the declaration locus; additional Mechanism fields must not introduce new semantic rows or shadow the signature's `imports` and `provides`.

#### A.6.1:4.2 - U.MechMorph - Refinement, Extension, Equivalence, and Composition

**Intent.** Provide structure-preserving **relations and constructors** between mechanisms.
**Definitions.**

* **Refinement** `M′ ⊑ M`: narrows the **SubjectBlock** or **SlotSpecs** (`ValueKind` or `refMode` for inherited SlotKinds) and strengthens `LawSet` or `AdmissibilityConditions` (safe substitution; Liskov-style). A Refinement **MUST NOT** rename SlotKinds or add new required arguments to inherited operations.
* **Extension** `M ⊑⁺ M″`: **adds operations** and any new SlotKinds used only by those new operations without weakening existing Laws or Guards; old programs remain valid (conservative extension).
* **Equivalence** `M ≡ M′`: there exists a bijective mapping between Subjects and operations preserving and reflecting **LawSet** (up-to-isomorphism on **BaseType** and **OperationAlgebra**).

* **Quotient** `M` by `≈`: factor by a **congruence** (e.g., **≡_UNM** for charts).

* **Product** `M×N`: independent **BaseTypes**; ops are component‑wise; ensures **no illegal cross‑ops** (e.g., set‑algebra discipline for `SpanUnion`). Where independence is claimed, **name and justify** the assumption (do not mint new Kernel types here).

##### A.6.1:4.2.1 - Specialisation relation chains (normative)

Many families need a **generic** mechanism at the top (e.g., “select anything”) and progressively **specialised** mechanisms below (e.g., “select a method by decision theory”, “select a telemetry pack”). To keep such specialisation chains **modular** and to prevent leakage across the chain:

1. **Explicit parent + morphism kind.** Any mechanism that specialises another **MUST** name its parent and declare whether the step is a **Refinement** (`⊑`) or an **Extension** (`⊑⁺`). A specialisation family **MUST** be acyclic (a DAG).

2. **SlotKind invariance across levels.** For every inherited operation or guard predicate, SlotKinds are invariant (A.6.5). A specialisation step **MUST NOT** rename an inherited SlotKind, change its documented semantics, or rely on positional re-ordering instead of SlotKind identity.

3. **ValueKind monotonicity.** A Refinement MAY narrow `ValueKind` (i.e., `ValueKind′ ⊑ ValueKind` in Kind-CAL) or `refMode` for an inherited SlotKind, and MAY strengthen Laws or Guards. It **MUST NOT** widen ValueKinds or relax Guards; otherwise mint a new parent mechanism or publish an adapter mechanism.

4. **No new mandatory inputs to inherited operations.** If a specialisation needs extra inputs, it **MUST** introduce a new operation (Extension) or an adapter mechanism; it **MUST NOT** retrofit new required parameters into an inherited operation signature.

5. **No upward leakage.** A root mechanism in a specialisation chain **SHOULD** mention only the most general ValueKinds required by its SlotSpecs and Laws. Domain-specific policies, generators, and evaluation packs belong in specialised mechanisms that refine slots or add operations.

*Informative selector specialisation-chain sketch.* `SelectorMechanism` can declare a stable slot interface (`CandidateSetSlot`, `ComparisonResultSlot`, `CriteriaSlot`, `ContextSlot`, `SelectionSlot`) with generic ValueKinds. `SelectorMethodMechanism ⊑ SelectorMechanism` then narrows `CandidateSetSlot.ValueKind` to `U.Method` and, by Extension, adds decision-theory specific slots and operations; an OEE generator is declared as a separate mechanism that produces candidate and criteria packs consumed by the selector.
**Transport** `Bridge⋅M`: lifts across Contexts or planes; names **CL**, **CL^k**, and **CL^plane** regimes; penalties are recorded in **`R_eff` only**; a **UTS row** may publish the crossing; **ReferencePlane(src,tgt)** is recorded. If mapping losses are material, **narrow** the mapped set or publish an **adapter**.

**Passing example.** `USM′ = USM + “publish named independence‑assumption evidence for SpanUnion”` ⇒ **Refinement** (strengthened law; substitution‑safe).
**Normalization quotient.** `UNM` quotiented by `≡_UNM` exposes **compare-on-invariants** surfaces for CPM and USCM (normalize-then-compare).

#### A.6.1:4.3 - U.MechanismDeclarationTemplate - Instantiation Template

**MechanismDescription (E.8 Tell–Show–Show; strict-distinction-compliant):**
`Mechanism: U.<Name>`  *(Kernel conceptual description; no tooling fields)*
`Imports: <Signatures and U.Types>` - `SubjectBlock: <SubjectKind, BaseType, SliceSet, ExtentRule, ResultKind?>` - `SlotSpecs: <SlotIndex (A.6.5)>` - `OperationAlgebra: <operators with SlotKinds>` - `LawSet: <equations and invariants>` - `AdmissibilityConditions: <admission predicates with SlotKinds; Γ_time>` - `Transport: <Bridge channels; CL, CL^k, and CL^plane named; ReferencePlane(src,tgt)>` - `PlaneRegime: <world, concept, or episteme rules>`

#### A.6.1:4.4 - MechFamilyDescription and MechInstanceDescription

* **MechFamilyDescription**: `{MechanismDeclaration, Realizationα, Realizationβ, …}` — each Realization may **tighten** and must never relax Laws (Liskov-style).

* **MechInstanceDescription**: `{MechanismDeclaration@Context, Windows, named Φ, Ψ, and Φ_plane regimes, BridgeIds}` — a **conceptual instance**; operational telemetry workflows are out of scope.

#### A.6.1:4.5 - Defaults

* **Local‑first semantics.** All judgments are **context‑local**; crossings are **explicit** and **costed** (CL→R only).
* **Compliance-first comparability.** Numeric comparison or aggregation requires **CG-Spec** (lawful **SCP**, Γ-fold, MinimalEvidence); **partial orders return sets**; **no ordinal means**.
* **Tri-state discipline.** `unknown → {degrade, abstain}`; `sandbox` and `probe-only` are **LOG branches** with policy-ids (no implicit `unknown→0` and no implicit `unknown→false`).
* **R-only penalties.** **Φ**, **Ψ**, and **Φ_plane** are **monotone and bounded**; penalties are recorded in **`R_eff` only**; **F and G** stay invariant.

#### A.6.1:4.6 - Born‑via‑A.6.1 sketch (informative)

**PTM — Publication and Telemetry Mechanism (informative)**
**BaseType:** `SoTA-Pack(Core)`, `PathId`, `PathSliceId`, `PolicyId`. **OperationAlgebra:** emit **selector-ready** packs with parity pins and **telemetry stubs**; listen for edition or illumination bumps; trigger **slice-scoped** refresh.
**LawSet:** **no change of dominance defaults** unless CAL policy promotes; edition-aware refresh.
**Guards:** **GateCrossing visibility harness** blocks publication on missing crossing attestations (BridgeCard plus UTS row, ReferencePlane, CL, CL^k, CL^plane, and Φ or Ψ policy-ids), on lane-purity violations (CL penalties recorded in R only; F and G invariant), or on lexical precision violations (E.10).
**Transport and Audit:** **G.10** and **G.11** publication and refresh semantics (CL penalties recorded in **R or R_eff**).

*Informative SoTA:* telemetry hooks align with post-2015 quality-diversity families (CMA-ME, MAE, DQD, and MEGA) and open-ended methods (POET-class) when monitored via illumination telemetry rather than scored.

#### A.6.1:4.7 - 60‑second didactic script

> *“To mint a mechanism, fill a **MechanismDeclaration**: declare **SubjectBlock** (**SubjectKind**, **BaseType**, **SliceSet**, **ExtentRule**, **ResultKind?**) and **SlotSpecs** (use a `SignatureManifest` if it is reusable); then **OperationAlgebra**, **LawSet**, **AdmissibilityConditions**, and **Γ_time**; define **Transport** (Bridge and CL with penalties recorded in R only), and **Audit** (UTS plus E.18 PathId pins). USM and UNM are already such mechanisms; the same template produces comparison, scoring, and publication mechanisms safely bound to **CG-Spec** without leaving the kernel grammar.”*

#### A.6.1:4.8 - Mechanism Declaration Checklist

1. State why this Mechanism is needed, which **guard predicates** and **comparability claims** are in scope, which `DesignRunTag` or `CtxState.locus` boundary it mediates, and whether a **Γ_m (CAL)** builder is needed.

* Fill **MechanismDeclaration** (**SubjectBlock**, **SlotSpecs**, **OperationAlgebra**, **LawSet**, **AdmissibilityConditions**, **Applicability**, **Transport**, **Γ_timePolicy**, **PlaneRegime**, **Audit**).

* Bind **CHR legality and CG-Spec** when comparing or aggregating (ComparatorSet, ScaleComplianceProfile (SCP), MinimalEvidence, Γ-fold).

Publish **UTS** and **G.10** relations; cite **G.11** telemetry when live; ensure penalties are recorded in `R_eff` only.

