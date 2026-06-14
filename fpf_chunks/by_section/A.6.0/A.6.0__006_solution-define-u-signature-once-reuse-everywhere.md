---
chunk_kind: "child"
pattern_id: "A.6.0"
pattern_title: "U.Signature - Universal, law‑governed declaration for a SubjectKind on a BaseType"
section_id: "A.6.0:4"
section_title: "Solution — Define U.Signature once, reuse everywhere"
source_path: "FPF-Spec.md"
output_path: "by_section/A.6.0/A.6.0__006_solution-define-u-signature-once-reuse-everywhere.md"
commit_sha: "7c617d5d0fa1abf94a21bac2dd909f68ed514249"
heading_path:
  - "A.6.0 — U.Signature - Universal, law‑governed declaration for a SubjectKind on a BaseType"
  - "A.6.0:4 — Solution — Define U.Signature once, reuse everywhere"
line_start: 9744
line_end: 9906
dependencies:
  - "A.2.6"
  - "A.6.1"
  - "A.6.5"
  - "D.CTX"
  - "E.10"
  - "E.10.D1"
  - "E.5.3"
  - "E.8"
  - "U.Mechanism"
  - "U.RelationSlotDiscipline"
keywords:
  - "RFC 2119"
  - "applicability"
  - "bounded context"
  - "laws"
  - "signature"
  - "vocabulary"
---

### A.6.0:4 - Solution — **Define `U.Signature` once, reuse everywhere**

**Definition.** A **`U.Signature`** is a **public, law-governed declaration** for a named **SubjectKind** on a declared **BaseType**. The Signature **SHALL** expose an explicit **SliceSet** and **ExtentRule**; if quantification is context-independent, the declaration **MUST** use a trivial `SliceSet` (e.g., a singleton) and a constant `ExtentRule` rather than omitting these fields. A Signature (i) introduces a **vocabulary** (types, relations, operators), (ii) states **laws** (axioms and invariants; no operational admissions), and (iii) records **applicability** (where and under which contextual assumptions the declarations hold). Dependencies (**imports**) and exported names (**provides**) are declared in a `SignatureManifest` (see §4.4.1) and are **not** part of the four-row Signature Block. **Discipline for argument-position typing is delegated to A.6.5 `U.RelationSlotDiscipline`: whenever the Vocabulary declares an n-ary relation or operator, SlotSpecs for its parameter positions SHALL be provided as in §4.1.1 and A.6.5.**

Where the **Vocabulary** introduces an **n‑ary relation or morphism**, the Signature **SHALL**, for each parameter position `i`, declare a `SlotSpec_i = ⟨SlotKind_i, ValueKind_i, refMode_i⟩` as defined in **A.6.5 `U.RelationSlotDiscipline`**. SlotSpecs live inside the per‑relation parameter block of the **Vocabulary** row and **MUST NOT** introduce additional rows beyond the four‑row Signature Block.

**Arrow form (typing for MVPK).** Express a Signature as a **morphism**
`SigDecl : ⟨SubjectBlock⟩ → ⟨Vocabulary × Laws × Applicability⟩`
where `SubjectBlock = ⟨SubjectKind, BaseType, SliceSet, ExtentRule, ResultKind?⟩`. This makes `U.Signature` directly consumable by **E.17 MVPK** (publication of morphisms) without adding semantics on faces (no new claims; pins for any numeric content).

*Guard clarification (normative).* **Operational guard predicates** (run‑time or admission guards) **BELONG ONLY** to **A.6.1 Mechanisms**. A Signature may express **domain and type constraints** as declaration-level constraints (e.g., restricting an operator’s domain) but **SHALL NOT** encode operational admissions.

*Guidance for `profile=FormalSubstrate` signatures.* Signatures that declare a formal-deductive profile (e.g., *FormalSubstrate*) MAY include, **as vocabulary elements**, an **EffectDiscipline** (algebraic, row, or graded effect signatures) and **InferenceKind** enumerations; handler semantics are **out of scope** for Signatures (see §4.3). The universal block remains conceptual and contains **no** run-time admissions or AdmissibilityConditions.

**Naming discipline.** The `Subject` **MUST** be a **single‑sense** noun phrase; avoid synonyms or aliases within the same Signature.

A `U.Signature` is conceptual: it contains no implementation, no packaging or CI metadata, and no Γ-builders. If a family wants to expose a Γ‑like *builder or aggregator*, publish it **outside** the Signature Block (typically as an **A.6.1** Mechanism‑level operator) and **namespace** it under the Signature id; do not treat Γ as part of the canonical Vocabulary.

#### A.6.0:4.1 - The **Signature Block (universal form)**

The **four conceptual rows** (“SubjectBlock, Vocabulary, Laws, and Applicability”) give a repeatable, holon‑stable pattern across mathematics → physics → engineering:
* **SubjectBlock** = *what it’s about + how quantified* (axiomatics + domain of interpretation),
* **Vocabulary and Laws** = *principles and laws* (postulates and constraints),
* **Applicability** = *where they hold in practice* (bounded context and time).

Every `U.Signature` **SHALL** present a **four‑row conceptual block** (names are universal; family‑specific aliases are mapped below):

1. **SubjectBlock** — ⟨**SubjectKind**, **BaseType**, **SliceSet**, **ExtentRule**, **ResultKind?**⟩.
   *SubjectKind* names the EntityOfConcern kind declared by the signature (C.3); *BaseType* is the `U.Type` the signature ranges over (CHR Spaces appear here **as types**, not as field names); *SliceSet* addresses the quantification domain (USM; e.g., **ContextSliceSet**); *ExtentRule* computes `Extension(SubjectKind, slice)` (C.3.2); *ResultKind?* (optional) is the output kind when outputs differ from the SubjectKind.
   **Editorial split (allowed).** Authors **MAY** render the **SubjectBlock** as two adjacent lines — **Subject** *(SubjectKind, BaseType)* and **Quantification** *(SliceSet, ExtentRule, ResultKind?)* — **without changing semantics**. Even when visually split, SubjectBlock counts as **one** conceptual row.

   **Semantic functions of the SubjectBlock kinds (informative)**
   * **SubjectKind (EntityOfConcern kind).** The EntityOfConcern kind declared by the signature (C.3.1), ordered by `⊑`. It carries no Scope.
   * **BaseType (ranged-over type).** The `U.Type` over which values or entities are ranged. In CHR regimes this may be a `U.CharacteristicSpace` **type**; elsewhere it is a set‑typed `U.Type`.
   * **SliceSet (addressability).** The addressable set of `U.ContextSlice`s (USM). It identifies where **extent** is computed; it is not a “space” unless CHR.
   * **ExtentRule (extent).** A rule yielding `Extension(SubjectKind, slice)` (C.3.2); this is the quantifier’s domain, computed per slice.
   * **ResultKind? (outputs).** Optional: the output kind for operations declared in *Vocabulary* (use when outputs differ in kind from the SubjectKind).

2. **Vocabulary** — names and sorts of the public **types, relations, and operators** this signature commits to (no handler semantics; no AdmissibilityConditions). For each **n‑ary relation or morphism** in the Vocabulary, parameters **SHALL** be declared via **SlotSpecs** `SlotSpec_i = ⟨SlotKind, ValueKind, refMode⟩` per **A.6.5 `U.RelationSlotDiscipline`**. SlotKinds and RefKinds **MUST** follow the `…Slot` and `…Ref` lexical discipline in **A.6.5** and **E.10 (LEX‑BUNDLE)**; ValueKinds **MUST** remain free of these suffixes.
   (No additional rows beyond the four‑row Signature Block.)

3. **Laws (Axioms and Invariants)** — equations and order and closure laws that are context‑local truths under the stated Applicability (no proofs here). **Operational guard predicates belong to Mechanisms (A.6.1)**, not to Signatures.

4. **Applicability (Scope and Context)** — conditions under which the laws are valid (bounded context, plane, stance, time notions). Applicability **MUST** bind a **`U.BoundedContext`** (D.CTX). Applicability here is the *context of meaning* for the Signature’s vocabulary and laws; it **MUST NOT** be used to encode claim‑level applicability, which remains a **Scope** on claims (`USM` and `C.3.2`). Cross‑context use **MUST NOT** be implicit; if intended, **name** the Bridge (conceptual reference only). When numeric comparability is implied, **bind** legality to **CG‑Spec and MM‑CHR** (normalize‑then‑compare; lawful scales and units).

*Mapping to existing families (normative aliases).*
— **A.6.1 (Mechanism).** *SubjectBlock* ↔ **SubjectKind, BaseType, and the remaining SubjectBlock fields**; *Vocabulary* ↔ **OperationAlgebra**; *Laws* ↔ **LawSet**; *Applicability* remains contextual; **AdmissibilityConditions** — separate field of mechanism (not in the `U.Signature`).
— **Task, Problem, and Discipline signatures (C.22, G-cluster).** These **SHALL** be introduced as **species of `U.Signature`** that reuse the same four-row Block (SubjectBlock, Vocabulary, Laws, and Applicability); any extra per-family views are projections only (no new conceptual rows).

*Optional projection views (normative).* Publications MAY include additional **projection views** (e.g., a Dependency View listing `imports` and `provides`, or an Assurance View listing audit and evidence hooks), but such views:
1) MUST be mechanically derivable from `SignatureManifest` + the four‑row Block (and referenced ClaimIds where used), and
2) MUST NOT introduce new semantics, obligations, or “extra rows”.

##### A.6.0:4.1.1 - SlotSpec for argument positions (normative; see A.6.5)

For every **n‑ary relation or operator** declared in the **Vocabulary** row, the Signature **SHALL** assign, to each argument position, a **SlotSpec** triple:

```text
SlotSpec_i := ⟨SlotKind_i, ValueKind_i, refMode_i⟩
```

where:
* **SlotKind_i** is a named position in the relation or operator (Tech name with `…Slot` suffix) whose semantics are documented (see A.6.5).
* **ValueKind_i** is the FPF type (`U.Kind` or kernel‑level type) of admissible values at that position.
* **refMode_i** is either `ByValue` or a **RefKind** (e.g., `U.EntityRef`, `U.HolonRef`), indicating whether the episteme stores values directly or references or identifiers.

Full discipline and lexical rules for **SlotKind, ValueKind, and RefKind** are given in A.6.5 `U.RelationSlotDiscipline` and E.10 (§8.1). A.6.0 requires that every vocabulary‑level relation or operator that takes arguments **declare** these SlotSpecs; downstream patterns MAY provide templates for common shapes (e.g., episteme slots in C.2.1).

**Mini‑example (informative).** For an episteme kind `ModelEvaluationResultKind`, a simplified episteme might expose:
* `entityOfConcernRef : U.MethodRef`
* `datasetRef : U.EntityRef`
* `metricRef : U.CharacteristicRef`
* `groundingHolonRef : U.HolonRef`
* `claimGraph : U.ClaimGraph`

A SlotSpec table then states:

| Parameter (episteme field)   | SlotKind              | ValueKind          | refMode                |
| ---------------------- | --------------------- | ------------------ | ---------------------- |
| `entityOfConcernRef`   | `EntityOfConcernSlot` | `U.Method`         | `U.MethodRef`          |
| `datasetRef`           | `DatasetSlot`         | `U.Entity`         | `U.EntityRef`          |
| `metricRef`            | `MetricSlot`          | `U.Characteristic` | `U.CharacteristicRef`  |
| `groundingHolonRef`    | `GroundingHolonSlot`  | `U.Holon`          | `U.HolonRef`           |
| `claimGraph`           | `ClaimGraphSlot`      | `U.ClaimGraph`     | `ByValue`              |

This example illustrates the intended interpretation: **parameters are typed twice**—once by their **ValueKind** (what sort of value fills the position) and once by **refMode** (by‑value or which RefKind). SlotKinds (with `…Slot` suffix) give stable names for substitution laws and EntityOfConcern statements across patterns.

#### A.6.0:4.2 - Profile specialisations (normative; structure‑preserving)
To enable first‑principles signature specializations without minting new Kernel kinds, apply **profiles** to `U.Signature`:

* **`profile = FormalSubstrate`** — *formal‑deductive specialization*
  **Vocabulary:** `TermRegister` (ref-only), **InferenceKinds** (ref-only), **EffectDiscipline** (operation and effect signatures).
  **Laws:** equational and structural axioms of the calculus; **no handler semantics**.
  **Applicability:** binds a `U.BoundedContext` for conceptual declaration use; **no units, ReferencePlane, or Transport** on faces.
  **MVPK pins:** **`No‑Realization` pin (mandatory)** on `PlainView` and `TechCard` asserting that handler semantics live only in **A.6.1 `U.Mechanism::U.EffectRealization`**.
  **Faces:** On MVPK faces, **`InferenceKindsAllowed`** MAY present a **ref‑only subset** of the enumerated **`InferenceKinds`**; Signatures do not add handler semantics.

* **`profile = PrincipleFrame`** — *postulates + measurability intent (CHR‑binding)*
  **Vocabulary:** **PostulateSet** (in the calculus imported), **CHR-Binding presence** (ref-only to characteristic or observation profiles), **Ontology references** (ref-only to ontology types or morphisms used to name subject-matter entities).
  **Laws:** timeless and order-free invariants; **no operational admissions**.
  **Applicability:** binds a `U.BoundedContext`; **Signatures SHALL NOT publish units, ReferencePlane, ComparatorSet, or Transport** (first mention is in **UNM**).
  **MVPK pins:** **`NoReferencePlaneOnSignature`** (alias: **`NoReferencePlaneOnPF`**) and **`UNM‑priority`** (units, planes, comparators, and Transport are declared only by **`U.ContextNormalization`** and cited by edition or ref-id where needed).

**Profile morphism discipline.** See §4.6 for the **structure‑preserving morphism** requirements for profile application.

#### A.6.0:4.3 - Effect-discipline and handler-semantics split (normative)

If a Signature’s **Vocabulary** includes an **EffectDiscipline** (operation and effect signatures), the Signature **SHALL NOT** declare **handler semantics** or any **EffectRealization**. Such realizations are declared only under **A.6.1 `U.Mechanism`** and cited by **ref-id** on faces where needed. This mirrors the modern algebraic-effects separation between *operation signatures* and *handlers* while keeping A.6.0 purely conceptual.

#### A.6.0:4.4 - Declaration Rules (strict-distinction-aware; lexically disciplined)

* **EntityOfConcern, Description, and specification-use separation.** A signature states the subject kind and laws; Realizations (if any) carry specification-use constraints. Do not mix tutorial text or operational recipes into the Block. Do **not** include **AdmissibilityConditions** or run‑time admissions here.
* **Context discipline.** Bind Applicability to a **`U.BoundedContext`**. If cross‑context use is intended, **name** the crossing and **reference** the Bridge (Part F and B.3); A.6.0 does **not** prescribe **compatibility and loss tables (CL, including `CL^plane`)** or penalty formulas.
* **Stratification.** Use LEX‑BUNDLE registers and strata; do not redefine Kernel names in lower strata (no cross‑bleed).
* **Signature manifest.** If the signature is intended to be imported or reused, publish a `SignatureManifest` immediately above the Block with explicit `id`, `imports`, and `provides` lists (§4.4.1). Keep the universal four‑row Block free of dependency and export metadata.

* **Realization discipline (normative extension point).** If a family publishes any *Realization* of a `U.Signature`, each Realization **MUST** (i) declare which `SignatureId` it implements, (ii) satisfy the Signature’s **Laws** (and imported laws) and **MAY** tighten them but **MUST NOT** relax them, and (iii) treat imported Signatures as **opaque**—it **MUST NOT** depend on their internal structure beyond what is exported via `provides` and cited via ClaimIds. Realization-specific build, tooling, and test metadata belongs to the Realization record or publication, not to the `U.Signature` Block.

##### A.6.0:4.4.1 - SignatureManifest (imports and provides; normative)

A `U.Signature` MAY be prefixed with a lightweight manifest that makes boundary dependencies explicit **without** introducing a separate “module system”.

**SignatureManifest** fields (conceptual; concrete syntax is editorial):

- `id : SignatureId` — stable identifier for cross-references.
- `version : SemVer` (optional; **required when the signature is imported or reused**).
- `publicationState : {draft | candidate | stable | deprecated}` (optional).
- `imports : [SignatureId]` — other signatures whose **provides** are referenced by this signature (directed edges; possibly empty).
- `provides : [SymbolId]` — the **only** new public symbols minted by this signature that downstream text may depend on (**types, relations, operators, SlotKinds, RefKinds**).

**Norms (boundary hygiene):**

- **Acyclicity.** The directed graph induced by `imports` MUST be acyclic.
- **Stratum dependency.** `imports` **MUST** respect **E.5.3** (Unidirectional Dependency) and **E.10** strata and token-class discipline; do not import from a lower stratum or across a forbidden dependency direction.
- **No redeclare.** `provides(S)` MUST NOT re‑declare any symbol already provided by any transitive import of `S`.
- **No ghost dependencies (vocabulary symbols).** Any non-Kernel **SymbolId** referenced in the **SubjectBlock** or **Vocabulary** rows (including `BaseType`, `ResultKind?`, operator names, SlotKinds, ValueKinds, RefKinds) that is **not** provided by this signature MUST be provided by some imported signature. ClaimIds, BridgeIds, policy-ids, and EditionIds are exempt because they identify claims, bridges, policies, or editions rather than vocabulary symbols exported by this Signature.
- **Law reference.** When downstream text depends on laws or constraints from an imported signature, it SHOULD cite the corresponding **ClaimId** (A.6.B), not paraphrase prose.

The A.6.0 four-row Block remains the canonical meaning locus for Vocabulary, Laws, and Applicability. The manifest only declares dependency edges and exported names.

* **Token hygiene.** Do **not** mint new `U.*` tokens inside a Signature without an accepted FPF naming and kind decision; prefer referencing existing Kernel or Extension `U.Type`s.

*MVPK publication discipline for Signatures (normative).* When publishing a `U.Signature` via MVPK (E.17), faces **SHALL** be typed projections that add **no new claims**; any numeric or comparable statement **MUST** pin unit, scale, reference-plane, and **EditionId** to **CG-Spec and MM-CHR** where applicable. For `profile=FormalSubstrate` signatures, faces **MUST** carry a **No-Realization pin** (handlers and realizers absent). For Principle-level signatures, faces **MUST NOT** introduce units, ReferencePlane, or Transport (first mention occurs in UNM).

#### A.6.0:4.5 - Specialisation knobs (for downstream patterns)

A.6.0 exposes **three** conceptual knobs; downstream patterns (A.6.1, method or discipline specifications) may **tighten** them:

1. **Builder policy.** The Block MUST NOT export Γ-builders. If a family publishes a Γ-like builder or aggregator, it MUST be outside the Block (typically as an **A.6.1** Mechanism-level operator), explicitly marked optional, and namespaced under the Signature id.

2. **Transport clause.** If cross-context or cross-plane use is part of the design, the signature **may declare** a conceptual Transport clause; **A.6.1** gives a concrete schema (Bridge, **CL, CL^k, and CL^plane**; Bridges per **F.9**, penalties per **B.3**, **CL^plane** per **C.2.1**), but A.6.0 remains agnostic about penalty shapes.

3. **Morphisms.** Families may define `SigMorph` (refinement, conservative extension, equivalence, quotient, product) to relate signatures; **A.6.1** instantiates this for mechanisms. Where such morphisms, or downstream **substitution and retargeting** laws (e.g., **A.6.2–A.6.4**), act on **n‑ary relations or morphisms**, they **SHALL** express their access, update, and retargeting discipline in terms of **SlotSpecs**  (SlotKind, ValueKind, RefKind) rather than unnamed parameter indices, using **A.6.5 `U.RelationSlotDiscipline`** as the normative slot calculus.

#### A.6.0:4.6 - Profile‑specialisation as a structure‑preserving morphism (normative)
Profile application `ι_profile : U.Signature → U.Signature(profile=…)` **SHALL** be a **structure‑preserving morphism**:
— **SubjectBlock** is preserved up to α‑renaming (SubjectKind and BaseType unchanged; ResultKind? only added when it exists in the universal intent).
— **Vocabulary** is **monotone** (adds or refines names and sorts without contradicting existing ones).
— **Laws** are **monotone** (add or strengthen axioms; never weaken).
— **Applicability** is **restrictive** (binds or tightens `U.BoundedContext`; never widens implicitly).
— No **AdmissibilityConditions**, **operational guards**, or **handler semantics** are introduced by the profile (those live under **A.6.1**).
This makes `profile=FormalSubstrate` and `profile=PrincipleFrame` *morphisms* in the sense of kernel specialisation and enables SigMorph reasoning (refinement or conservative extension).

