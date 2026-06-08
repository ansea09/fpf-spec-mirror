---
chunk_kind: "parent"
pattern_id: "A.6.1"
pattern_title: "U.Mechanism - Law‑governed application to a SubjectKind over a BaseType"
section_id: null
section_title: null
source_path: "FPF-Spec.md"
output_path: "by_pattern/A.6.1.md"
commit_sha: "b22b6993b3e94f7896d5dc1cd011af7bc3f49b0d"
heading_path:
  - "A.6.1 — U.Mechanism - Law‑governed application to a SubjectKind over a BaseType"
line_start: 9192
line_end: 9517
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

## A.6.1 - U.Mechanism - Law‑governed application to a SubjectKind over a BaseType

**One-line summary.** A `U.Mechanism` is a specialisation of `U.Signature` (A.6.0): its **Vocabulary** is an explicit **OperationAlgebra** whose operators publish **SlotSpecs** (A.6.5), its **Laws** are a **LawSet**, and it adds **AdmissibilityConditions** (operational guards) plus a named **Transport** clause for cross-context use. Transport is **Bridge-only** (per **F.9**) with penalties recorded only in the **Reliability** channel (**R**, or **R_eff** when distinguished) (per **B.3**); **F and G** remain invariant; **CL^plane** follows **C.2.1 CHR:ReferencePlane**. Realizations MAY be published, but MUST be monotone with respect to the Mechanism’s **LawSet** and any imported Signature laws and MUST treat imported signatures as opaque by using `imports`, `provides`, and ClaimIds.

**Status.** Normative \[A\] in **Part A (Kernel)**.

**Placement.** Immediately **after A.6.0** as **A.6.1**. **USM (A.2.6)** and **UNM (A.19 and C.16)** become **instances conforming to A.6.1** (no semantic change to either).

**Mint vs reuse.** This pattern mints the Kernel lexemes `U.Mechanism`, `U.MechMorph`, and `U.MechanismDeclarationTemplate`, plus the descriptive record names `MechanismDescription`, `MechFamilyDescription`, and `MechInstanceDescription`. It reuses `U.Signature` (A.6.0), `U.Type`, `U.BoundedContext`, and Part F Bridge, CL, and ReferencePlane terms without changing them; it does **not** mint new `U.Type` core types.

**Type.** Architectural pattern (kernel‑level; notation‑independent).

**LEX.TokenClass (E.10).** Declared here for the tokens minted by this pattern (see **E.10:7.1**).
* `LEX.TokenClass(U.Mechanism) = KernelToken`
* `LEX.TokenClass(U.MechMorph) = KernelToken`
* `LEX.TokenClass(U.MechanismDeclarationTemplate) = KernelToken`
* `LEX.TokenClass(MechanismDescription) = KernelToken`
* `LEX.TokenClass(MechFamilyDescription) = KernelToken`
* `LEX.TokenClass(MechInstanceDescription) = KernelToken`

### A.6.1:0 - Use and boundary

Use this pattern when a reusable declaration has to do more than name a signature: it must declare a law-governed operation algebra, operational admissibility predicates, context-local applicability, and explicit cross-context or cross-plane Transport for a `U.Mechanism`.

Do not use this pattern when the claim being made is only a reusable declaration with no operational guards; use A.6.0. Do not use it to authorize work, pass a gate, certify evidence, choose a method, publish telemetry, or prove a result. Those claims use the work, gate, evidence, method, publication, or result patterns that cite the mechanism when needed.

First useful move: write the mechanism declaration as a specialization of the four-row A.6.0 Signature Block, then add only the mechanism-specific fields: `OperationAlgebra`, `LawSet`, `AdmissibilityConditions`, `Transport`, `Γ_timePolicy`, `PlaneRegime`, and `Audit`. If cross-context use is live, name the Bridge and the Reliability penalty relation before any reuse claim is made.

What goes wrong if missed: an implementation recipe, a policy rule, a telemetry package, or a cross-context reuse habit can masquerade as mechanism law. Downstream work then cannot tell which operations are lawful, which admissibility predicates fail closed, and which losses affect Reliability rather than Formality or Guarantee.

What this buys: USM, UNM, selection mechanisms, normalization mechanisms, scoring mechanisms, and publication mechanisms can be compared, refined, extended, transported, and realized without hiding law, guard, time, plane, or Reliability assumptions.

### A.6.1:1 - Problem frame

Give FPF **one uniform kernel shape** for things like **USM** (set-algebra on context slices) and **UNM** (classes of admissible normalizations with ≡\_UNM) so practitioners can **define, compare, refine, compose, and port** mechanisms **without re-inventing the mechanism language**; all cross-context use is **Bridge-only** with **CL penalties recorded in R or R_eff**, never in **F or G**.

### A.6.1:2 - Problem

Without a kernel abstraction, scope, normalization, and comparison constructs proliferate with incompatible algebras and guard predicates; cross-context reuse lacks a visible **Bridge and CL penalty relation**; comparability drifts into **illegal scalarisation** (e.g., ordinal means). FPF already curbs this via **A.6.0** (Signature discipline, `SignatureManifest`), **USM** (scope algebra and Γ_time), **UNM** (normalize-then-compare), and **CG-Spec** (lawful comparators and ScoringMethods), but lacks a **common kernel kind** for “mechanism.”

### A.6.1:3 - Forces

**Locality vs transport.** Semantics are **context-local**; crossing contexts is **Bridge-only** (Part F and B.3); penalties are recorded in **R or R_eff**; **F and G** stay invariant.

**Expressivity vs legality.** Rich operators must stay inside **CHR legality** and **CG-Spec** constraints: no ordinal averages and no cross-unit arithmetic without lawful unit alignment.

**Time determinacy.** Explicit **Γ_time**; no implicit *latest*. (Required in USM’s `ContextSlice`.)

**Slot clarity vs specialisation depth.** Multi‑level specialisations require explicit **SlotSpecs** (A.6.5) and monotone refinement of **ValueKinds**; SlotKinds are stable across levels (no implicit positional parameters).

**Signature hygiene.** Obey `SignatureManifest` discipline (A.6.0:4.4.1): explicit `imports` and `provides`, acyclic imports, and no redeclare. Treat imported signatures as **opaque**: reference only their `provides` symbols and ClaimIds, and keep realizations monotone.

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

### A.6.1:5 - Archetypal Grounding

#### A.6.1:5.1 - **U.Scope (Claim, Work, Publication) — USM as a U.Mechanism instance** (informative example)

* **Imports:** `U.ContextSliceSet`; Part F.9 **Bridge**; **C.2.1 ReferencePlane** (noted for crossings); **C.2.2 F–G–R**; **C.2.3 U.Formality**.
* **BaseType:** `U.ContextSliceSet`.
* **SliceSet:** `U.ContextSliceSet` (addressable `U.ContextSlice`s).
* **SubjectKind:** `U.Scope` with specializations `U.ClaimScope` (G), `U.WorkScope`, and `U.PublicationScope`.
* **OperationAlgebra:** `∈, ⊆, ∩, SpanUnion, translate, widen, narrow, refit`.
* **LawSet:** serial **intersection**; **SpanUnion** only where a **named independence assumption** is satisfied (state features or characteristics, validity window, evidence class); **translate** uses declared **Bridges**; **Γ_time** is **mandatory**.
* **AdmissibilityConditions:** deterministic **“Scope covers TargetSlice”**; **fail-closed**; `unknown → {degrade, abstain}` (no implicit `unknown→0` and no implicit `unknown→false`).
* **Transport:** **Bridge-only** with **CL**; penalties are recorded in **`R_eff`**; **F and G** stay invariant; publish UTS notes.
* **Γ_timePolicy:** `point`, `window`, or `policy`; **no implicit “latest.”**
* **PlaneRegime:** *not applicable to scope sets* (scope is set-valued over `ContextSlice`, no value-plane); **CL^plane** not applicable.

### A.6.1:6 - Bias-Annotation *(informative)*

This pattern intentionally biases Mechanism declaration toward explicit signatures and laws, context-local semantics, and auditable reuse.

* **Gov (governance).** Bias toward publishable declaration rows, conformance checks, and explicit policy-ids for crossings. Risk: perceived declaration overhead. Mitigation: reuse the `MechanismDeclaration` template; keep Realizations opaque and put operational details outside the Kernel.
* **Arch (architecture).** Bias toward locality-first semantics and **Bridge-only** transport with costs recorded in **R or R_eff**. Risk: reduced convenience for ad-hoc cross-context reuse. Mitigation: publish adapter mechanisms and make crossings explicit via `Transport` (CC-UM.3 and CC-UM.4).
* **Onto and Epist (ontology and epistemology).** Bias toward lawful comparability (CHR legality; CG-Spec binding) and against illegal scalarisation (e.g., ordinal means). Risk: some heuristic scoring practices become non-conformant. Mitigation: represent uncertainty explicitly and use `unknown → {degrade, abstain}` rather than coercions (CC-UM.7).
* **Prag (practice).** Bias toward notation-independence and against tool or vendor tokens in the Kernel. Risk: teams may want to inline CI or telemetry fields. Mitigation: keep audit surfaces conceptual (`Audit`) and reference operational hooks by id only (CC-UM.6).
* **Did (didactic).** Bias toward explicit SlotKinds and SlotSpecs over positional parameters. Risk: steep learning curve. Mitigation: allow non-normative projections (`ValueKindView`) and include a “60-second” script plus a mechanism declaration checklist (A.6.1:4.7 and 4.8).

### A.6.1:7 - Conformance Checklist (normative)

| ID | Requirement |
|----|-------------|
| **CC‑UM.0** | **A.6.0 alignment:** a conformant `U.Mechanism` publication **MUST** include the four-row `U.Signature` Block (A.6.0). `OperationAlgebra` (including inline SlotSpecs per A.6.0:4.1.1 and A.6.5) is the **Vocabulary** row, `LawSet` the **Laws** row, and `Applicability` the **Applicability** row; the universal block remains the comparability signature block. Any `SlotIndex` is an index projection and **MUST NOT** be treated as a fifth Signature row. |
| **CC‑UM.1** | **Complete MechanismDeclaration:** a conformant `U.Mechanism` publication **MUST** publish: `DeclarationHeader(id, version, publicationState); Imports; SubjectBlock (SubjectKind, BaseType, SliceSet, ExtentRule, ResultKind?); SlotIndex (A.6.5); OperationAlgebra; LawSet; AdmissibilityConditions; Applicability; Transport (Bridge named; ReferencePlane); Γ_timePolicy; PlaneRegime; Audit`. `DeclarationHeader.id` **MUST** be PascalCase; `version` **MUST** follow SemVer; `publicationState ∈ {draft, candidate, stable, deprecated}`. Eligibility and admission tests **MUST** be expressed as `AdmissibilityConditions`, not as `LawSet`. If the mechanism is intended to be imported or reused, it **MUST** also include a `SignatureManifest` per **CC-A.6.0-18**, consistent with `DeclarationHeader` and `Imports` (A.6.1:4.1). |
| **CC‑UM.2** | **Monotone realization (signature-law discipline):** if a mechanism publishes (or implies) any realization of a signature, that realization MUST satisfy the signature’s LawSet (and imported laws) and MAY only tighten (never relax) them. Realizations MUST treat imported signatures as **opaque**: reference only symbols in `provides` (A.6.0:4.4.1) and cite ClaimIds (A.6.B). Do not mint a parallel signature header; use `SignatureManifest`. |
| **CC‑UM.3** | **Bridge-only transport:** for any cross-context or cross-plane use, `Transport` **MUST** name the BridgeId and channel (F.9) and **MUST** record `ReferencePlane(src,tgt)` (C.2.1); when planes differ it **MUST** name `CL^plane`. Implicit crossings **MUST NOT** occur. When typed reuse is involved, the two-bridge rule **MUST** apply: scope CL and kind `CL^k` penalties are recorded separately in **R** or **R_eff**. `Transport` is a declarative policy surface and **MUST NOT** be used to introduce a `U.Transfer` edge (E.18 term separation). It **MUST NOT** restate CL, Φ, Ψ, or Φ_plane policy tables; it **MUST** reference policy ids or registries. |
| **CC‑UM.4** | **R-only penalty recording:** any CL, `CL^k`, or `CL^plane` penalties declared or incurred by `Transport` **MUST** reduce the Reliability channel only (**R**, or **R_eff** when distinguished) per **B.3**; they **MUST NOT** mutate **F or G**. |
| **CC‑UM.5** | **CG-Spec binding:** if the Mechanism defines or induces any numeric comparison or aggregation, it **MUST** bind to **CG-Spec and MM-CHR** (lawful **SCP**, Γ-fold, MinimalEvidence; normalize-then-compare) and obey CHR legality: partial orders **MUST** return sets; ordinal means **MUST NOT** be computed; interval or ratio arithmetic **MUST** occur only with unit alignment (CSLC-proven). |
| **CC‑UM.6** | **E.8 and E.10 compliance:** the A.6.1 publication **MUST** include Tell-Show-Show under **“Archetypal Grounding”** and **MUST** respect Plain and Tech registers plus EntityOfConcern and Description separation. Any new `U.*` token, including any new `U.Type`, **MUST** have an accepted FPF naming and kind decision plus a `LEX.TokenClass` entry; `BaseType` **MUST** reference an existing `U.Type` (no in-place minting), and any new `U.Type` required for that reference **MUST** be minted outside the mechanism definition. Non-specification surfaces **MUST** end with **“…Description”**. Core narrative **MUST NOT** include tool or vendor tokens. |
| **CC‑UM.7** | **Unknowns tri-state:** guard predicates in `AdmissibilityConditions` **MUST** be deterministic, context-local, and fail-closed; they **MUST** define `unknown → {degrade, abstain}` and **MUST NOT** coerce unknowns to 0 or false. Sandbox and probe branches **MUST** live in **SoS-LOG** (not Acceptance). |
| **CC‑UM.8** | **Multi‑level specialisation discipline:** if a Mechanism declares itself as `⊑` or `⊑⁺` of another Mechanism, it **MUST** satisfy A.6.1:4.2.1 (explicit parent+morphism kind; SlotKind invariance; monotone ValueKind narrowing; no new mandatory inputs to inherited ops). |
| **CC‑UM.9** | **SlotIndex is a view:** `SlotIndex` **MUST** be mechanically derivable from (i) the per‑operator SlotSpecs in `OperationAlgebra` (A.6.0:4.1.1) plus (ii) any guard‑only SlotSpecs **declared with** `AdmissibilityConditions` predicate signatures; it **MUST NOT** contradict those SlotSpecs. Any didactic `ValueKindView` (or “ParamKind” lists) are non‑normative projections only. |
| **CC‑UM.10 (Multiple realizations rationale).** | If multiple Realizations are published for the same MechanismDeclaration, the mechanism publication **SHOULD** provide a short trade-off rationale (why and when to choose which), without introducing new obligations beyond the referenced Signature and ClaimIds. |

### A.6.1:8 - Common Anti-Patterns and How to Avoid Them *(informative)*

| Anti-pattern | What it looks like | Remedy |
| --- | --- | --- |
| **SlotIndex treated as a 5th Signature row** | Reviews start comparing mechanisms by `SlotIndex` only; SlotSpecs disappear from operator declarations. | Keep SlotSpecs **inline per operator**; treat `SlotIndex` as a derived projection only (CC‑UM.0, CC‑UM.9). |
| **Admission tests put in LawSet** | “Eligibility” and “coverage” checks appear as laws; implementations silently diverge. | Move operational guards to `AdmissibilityConditions` (CC‑UM.1). |
| **Implicit crossings or hidden CL policy tables** | A mechanism is reused across Contexts or planes without a declared BridgeId or ReferencePlane; CL, Φ, or Ψ tables get copied into local prose. | Crossings must be explicit and **Bridge-only**; `Transport` references policy ids or registries (CC-UM.3). |
| **Penalties leak into F or G** | A plane, kind, or scope mismatch is handled by mutating Formality or Guarantee claims. | Record penalties in **R or R_eff only**; keep **F and G** invariant (CC-UM.4). |
| **Illegal scalarisation** | Ordinal means or cross-unit arithmetic is performed “because we need a number”. | Bind numeric comparison or aggregation to CG-Spec, MM-CHR, and CSLC; keep partial orders set-valued (CC-UM.5). |
| **Specialisation breaks SlotKind identity** | Refinements rename SlotKinds or add mandatory parameters to inherited operations. | SlotKinds are invariant; refinements only narrow ValueKinds or guards; add new operations via Extension (CC-UM.8). |
| **Unknown coerced to 0 or false** | Guard failures silently become “false” or scores become 0. | Use tri-state discipline: `unknown → {degrade, abstain}`; probing lives in LOG branches (CC-UM.7). |
| **In-place minting of BaseType** | A mechanism definition introduces a new `U.Type` ad hoc. | `BaseType` references an existing `U.Type`; mint new types through an accepted FPF naming and kind decision outside the mechanism (CC-UM.6). |

### A.6.1:9 - Consequences (informative)

* **Uniform kernel shape.** Scope, normalization, comparison families can be declared and compared without lexical drift.
* **Auditable reuse.** GateCrossings are UTS-visible via **CrossingBundle** (**E.18**); penalties are transparent (**R only**), with **LanePurity** and **lexical precision** (E.10) checks runnable (GateChecks in **A.21**; Bridge and UTS discipline through **F.9**, **F.17**, **E.17**, and **E.18**).
* **Scalarisation avoids illegality.** Partial orders remain set-valued; cross-scale arithmetic is blocked by **CG-Spec and CSLC**.

### A.6.1:10 - Rationale (informative)

Binding mechanisms to an explicit **Signature -> Realization** discipline (A.6.0 `SignatureManifest` plus CC-UM.2 monotonicity and opacity) keeps reuse safe: signatures and laws carry the boundary semantics; realizations may vary but cannot relax laws. It also makes cross-context Bridge crossings explicit and records costs in `R_eff`, never in F or G.

### A.6.1:11 - SoTA-Echoing (post-2015 practice alignment) *(informative)*

**Purpose.** To show how the FPF concept of a *Mechanism* (law-governed signature with guards and transport) aligns with, and improves upon, leading research and engineering practices after 2015.
All comparisons are *informative*: they serve didactic continuity, not new normative force.

#### A.6.1:11.1 - Contemporary references (post-2015 sources)

**SoTA binding note (E.8:11).** This section cites primary post-2015 sources directly as the current source-use form for mechanism semantics. When a current ClaimSheet, CorpusLedger, or BridgeMatrix id is available for the same source decision, cite that id instead of repeating the source narrative.

1. **Algebraic effects and handlers** (post-2015 effect systems and handler implementations) — **Adopt and Adapt.** They motivate the split “operation signature vs handling”; A.6.1 keeps `OperationAlgebra` explicit and adds `LawSet`, `AdmissibilityConditions`, and `Γ_time` so legality and time are not implicit. *(e.g., Hillerström and Lindley, 2018; Multicore and OCaml-5 effect handlers, 2021–2022).*

2. **Typed semantic translation frameworks** (institution-style morphisms and functorial data migration) — **Adapt.** A.6.1 uses explicit refinement, extension, and quotient structure (`U.MechMorph`) but requires cross-Context transport to be **Bridge-only** with penalties recorded in **R or R_eff**. *(e.g., Spivak and Schultz, 2017; CQL practice, 2017–2023).*

3. **Policy-as-Code** (declarative guard and risk rules) — **Adapt.** A.6.1 turns runtime policies into deterministic, fail-closed `AdmissibilityConditions` with named Γ_time windows; evaluators and tool binding stay out of Core. *(e.g., Open Policy Agent and Rego, 2016+; UL 4600:2020; ISO 21448:2019).*

4. **Session and typestate types** (post-2015 protocol safety) — **Adapt.** Protocol constraints inform how guards can restrict legal operator sequences, but A.6.1 keeps boundary semantics as signature and laws and surfaces sequencing constraints as explicit guard predicates rather than hidden state. *(e.g., Scalas and Yoshida, 2016–2018; mainstream session-type toolchains, 2017–2024).*

5. **Lawful measurement and calibrated uncertainty** (monotone and calibrated learning, conformal prediction) — **Adopt and Adapt.** Modern calibrated methods show why comparability must be explicit; A.6.1 binds induced numeric operations to **CG-Spec and CSLC** and forbids illegal scalarisation (e.g., ordinal means). *(e.g., Romano et al., 2019; Angelopoulos and Bates, 2021).*

Each source corresponds to a distinct *Tradition*: formal semantics, categorical algebra, compliance automation, protocol safety, and lawful AI.

#### A.6.1:11.2 - Alignment with A.6.1 fields and concepts

| A.6.1 construct (claim) | SoTA practice (post-2015) | Primary sources (post-2015) | Alignment delta encoded by A.6.1 | Adopt, Adapt, or Reject |
| --- | --- | --- | --- | --- |
| **OperationAlgebra and LawSet** | Algebraic effects and handlers separate operation signatures from handlers. | Hillerström and Lindley (2018); OCaml-5 and Multicore OCaml effect handlers (2021–2022). | FPF keeps operator signatures explicit, adds an explicit `LawSet`, and treats admissibility and time as separate surfaces (no hidden context). | Adopt and Adapt |
| **U.MechMorph** (Refine, Extend, Quotient) | Institution-style morphisms and functorial data migration provide typed signature translations and quotients. | Spivak and Schultz (2017); CQL ecosystem papers and docs (2017–2023). | FPF reuses the morphism structure but requires cross-Context use to be stated as `Transport` with an explicit `BridgeId` (F.9) and CL, CL^k, and CL^plane regimes; penalties are recorded in `R` or `R_eff` only (B.3). | Adapt |
| **AdmissibilityConditions and Γ_timePolicy** | Policy-as-Code makes guard and risk predicates executable and reviewable. | Open Policy Agent and Rego (2016+); UL 4600:2020; ISO 21448:2019. | FPF treats policy predicates as deterministic, fail-closed guards with named validity windows; it forbids implicit “latest” and avoids embedding evaluators in Core. | Adapt |
| **AdmissibilityConditions** (sequencing) | Session and typestate disciplines constrain legal operation sequences. | Scalas and Yoshida (2016–2018); post-2017 multiparty session type toolchains. | FPF uses guards to make sequencing constraints explicit and auditable, while leaving the kernel boundary semantics as signature and laws (no hidden automata). | Adapt |
| **CG-Spec and MM-CHR binding** | Calibrated and monotone ML plus conformal prediction make uncertainty and monotonicity explicit. | Romano et al. (2019); Angelopoulos and Bates (2021). | FPF requires scale legality (CSLC) and forbids ordinal averaging; partial orders remain set-valued unless a lawful scorer is declared. | Adopt and Adapt |

#### A.6.1:11.3 - Adopt, Adapt, and Reject summary

* **Adopt.** The “explicit operations and explicit laws” stance from modern semantics work, and the calibrated and monotone stance from lawful ML, because both reduce hidden assumptions.

* **Adapt.** Typed translation ideas and policy‑as‑code idioms into a kernel form that is Context‑local by default, with explicit guards (`AdmissibilityConditions`) and explicit time windows (`Γ_timePolicy`) instead of implicit recency.

* **Reject.** Tool‑bound semantics, automatic recency heuristics, and any cross‑scale arithmetic without CSLC proof; A.6.1 also rejects implicit cross-Context or cross-plane reuse.

* **Cross-Context or cross-plane delta (E.8:11).** Whenever a SoTA practice would reuse semantics across Contexts or planes, A.6.1 requires an explicit `BridgeId` (F.9) plus CL, `CL^k`, `CL^plane`, Φ, Ψ, and Φ_plane policy-ids (B.3), with penalties recorded in `R` or `R_eff` only and never mutating `F` or `G`.

#### A.6.1:11.4 - Holonic repeatability

The same correspondence holds at **every holonic level**:
a part-holon declares its own `OperationAlgebra`, `LawSet`, and `AdmissibilityConditions`; a whole-holon merges them via Bridges; a meta-holon re-binds mechanisms under a new Γ-closure. All penalties remain in **R** or **R_eff**, while **F** and **G** invariants propagate intact.

### A.6.1:12 - Relations (quick pointers)

Builds on **A.6.0**; instantiates **A.2.6 USM** (ContextSlice, Γ_time, intersection, SpanUnion, translate) and **A.19** plus **C.16** UNM (classes, ≡\_UNM, validity windows); uses **Part B** (Bridges, CL, CL^k, CL^plane; **no implicit crossings**); binds **CG-Spec** for any numeric comparison or aggregation; telemetry and publication use **G.10** and **G.11**.

### A.6.1:12a - P2W Mechanism Use Relation

When `E.18.1` reaches a mechanism cue, this pattern carries the mechanism meaning: `OperationAlgebra`, `LawSet`, `AdmissibilityConditions`, effect realization when declared, transport, and mechanism descriptions. P2W may name the cue and governing pattern, but it does not define these mechanism relations locally.

If the issue under repair is new mechanism introduction, mechanism stabilization, or method-related mechanism use, use the current `E.20` governing pattern when live. A P2W citation of a mechanism does not select a method, execute work, pass a gate, prove evidence, or certify a result.

### A.6.1:12b - Lowering, repair, and refresh conditions

A `U.Mechanism` remains usable while its MechanismDeclaration, imported signatures, SlotSpecs, LawSet, AdmissibilityConditions, Applicability, Transport, Γ_timePolicy, PlaneRegime, and Audit relations remain recoverable and monotone with respect to A.6.0.

Repair the mechanism, or mint a new mechanism when monotone repair is impossible, if any of these conditions holds:

* an inherited SlotKind is renamed, widened, or given a new required argument;
* a realization relaxes a law, bypasses an admissibility predicate, or depends on hidden structure inside an imported signature;
* a cross-context or cross-plane reuse claim lacks BridgeId, ReferencePlane, CL, CL^k, CL^plane, or Reliability penalty relation;
* a numeric comparison or aggregation is no longer legal under CG-Spec, MM-CHR, CSLC, or the current characteristic-space declarations;
* a Γ_timePolicy, validity window, or “latest” assumption changes an admissibility result;
* a current SoTA change in algebraic effects, session types, typed semantic translation, Policy-as-Code, calibrated uncertainty, or context normalization changes the operation algebra, guard discipline, morphism relation, or transport boundary.

Do not repair the mechanism merely because one work occurrence, telemetry publication, evidence record, gate decision, method choice, or realization version changed. Repair the object governed by that later relation unless the change alters the MechanismDeclaration, its imported signature relation, or the monotone relation between a realization and the MechanismDeclaration.

### A.6.1:End

