(d) **reuse across Contexts** via **both** scope and kind bridges—**without** inventing new scales or conflating **G**, **F**, and **R**.

**Audience.** Engineering managers and reviewers who must read/author guards that are **legible, deterministic, and auditable** in context.


### C.3.A:2 - Context & Problem

Projects often:

* treat **“more abstract wording”** as wider **G**,
* glue claims with incompatible **describedEntity** (kinds),
* move typed content across Contexts without **declared bridges**,
* or bake **AT** (abstraction vibe) into decision logic.

**C.3.A** fixes this by supplying guard macros that:
— **separate** typed compatibility (kinds) from **Scope** coverage (USM),
— require **both** bridges where needed,
— push congruence penalties to **R** only, and
— forbid **AT** in guards.


### C.3.A:3 - Solution Overview (what these guards do)

All guards in this Annex share three invariants:

1. **Fail‑closed.** If any required predicate is undefined/false, the guard **denies** the transition.
2. **Deterministic.** Given a fixed **TargetSlice** (with explicit **Γ\_time**) and published declarations, evaluation yields one outcome.
3. **Separation of concerns.**
   *Typed compatibility* (same‑Context `⊑` or **KindBridge**) is **not** Scope.
   *Scope coverage* is a USM set‑membership judgment over **Context slices**.
   *Assurance penalties* (**Φ(CL)** for scope bridges; **Ψ(`CL^k`)** for kind bridges) reduce **R** only.


### C.3.A:4 - Normative Guard Macros

> **Notation.** “**SHALL**” clauses are normative obligations. “Notes” are informative reminders. Names like `Guard_TypedClaim` are editorial handles; Contexts may alias them, but **MUST** preserve semantics. Macro names (e.g., `Guard_TypedClaim`) are editorial handles; Contexts may alias them provided the logical obligations are preserved.


#### C.3.A:4.1 - **Guard\_TypedClaim** — admit a claim quantified over a kind

**Intent.** Approve a state transition that asserts Claim **C** which quantifies over `U.Kind` **k** at **TargetSlice**.

**Guard\_TypedClaim(C, k, TargetSlice, thresholds?)** — **SHALL** include, in this order:

1. **ScopeCoverage.** `U.ClaimScope(C) covers TargetSlice`. *(USM A.2.6)*
2. **Γ\_time declared.** TargetSlice **SHALL** specify **Γ\_time** (point/window/policy). No “latest”. *(A.2.6)*
3. **Kind definedness.** `MemberOf(?, k, TargetSlice)` is **defined and deterministic**. *(C.3.2 K‑05/K‑07)*
4. **Typed compatibility.**
   4.1 **same Context**: if C expects `k′`, require `k ⊑ k′`. *(C.3.1)*
   4.2 **Cross Context**: if Contexts differ, require a declared **KindBridge** that maps `k → k′` and publishes **`CL^k ≥ c`** with loss notes. *(C.3.3)*
5. **Assurance penalties (R only).** If step 4.2 used a KindBridge, the guard **SHALL** apply a monotone penalty **Ψ(`CL^k`)** to **R**. If a **Scope bridge** was used to move C’s Scope (USM), apply **Φ(CL)** to **R**. *(C.2.2 + C.3.3 + Part B)*
6. **Evidence freshness (if trust is implied).** Freshness windows and expiry checks **SHALL** be separate predicates (not Scope). *(C.2.2)*
7. **Formality threshold (if ESG mandates).** If the Context gates rigor, require `U.Formality(C) ≥ F_k`. *(C.2.3)*

**Prohibitions.**
— **AT forbidden.** KindAT **MUST NOT** appear in this guard. *(C.3.5 AT‑01/02)*
— **No “domain” placeholders.** Guards **SHALL** name an addressable **TargetSlice**, not a fuzzy “domain”.


#### C.3.A:4.2 - **Guard\_TypedJoin** — compose two typed claims/specs (A → B)

**Intent.** Permit composition where **A** produces facts over `k_A` and **B** consumes `k_B`.

**Guard\_TypedJoin(A, k\_A; B, k\_B; TargetSlice)** — **SHALL** include:

1. **TypedCompat.**
   1.1 **same Context**: require `k_A ⊑ k_B`.
   1.2 **Cross Context**: require **KindBridge** mapping `k_A → k′_B` with **`CL^k ≥ c`** and `k′_B ⊑ k_B`.
2. **ScopeSerial.** Compute `Scope_serial = ClaimScope(A) ∩ ClaimScope(B)`. Require `Scope_serial covers TargetSlice`. *(A.2.6)*
3. **Penalties (R only).** Apply **Ψ(`CL^k`)** if a KindBridge was used; apply **Φ(CL)** if a Scope bridge was used. *(C.2.2 / Part B / C.3.3)*
4. **Freshness.** Guard **SHALL** assert required freshness windows for evidence **along the serial path**.
5. **No type‑by‑scope.** The guard **MUST NOT** widen Scope to “fix” a type mismatch; remedies are subkind introduction, adapter, or bridge.

**Mask awareness.** If B expects a **RoleMask(k\_B)**: either show A’s outputs already satisfy mask constraints, or add a documented **mask adapter** (see 4.3) and treat any **contextual** constraints as part of **ScopeSerial**.


#### C.3.A:4.3 - **Guard\_MaskedUse** — use a RoleMask with a kind

**Intent.** Use `U.Kind` **k** under a **RoleMask** **m** in Context **R**.

**Guard\_MaskedUse(k, m, TargetSlice)** — **SHALL** include:

1. **MaskRegistered.** `RoleMask(k, m, version)` is **registered and versioned**. *(C.3.4 RM‑06)*
2. **MaskDeterminism.** All mask constraints are **observable** on TargetSlice; if the mask narrows membership, it **SHALL** be deterministic. *(RM‑03)*
3. **MaskType clarity.** Mask **SHALL** declare its type: constraint / vocabulary / composite. *(RM‑04)*
4. **Promotion cue.** If mask is reused widely as a de‑facto subkind, editors **SHOULD** promote it to an explicit `⊑` link. *(RM‑05)*
5. **Cross‑context use.** If `TargetSlice.Context ≠ owner(k).Context`, require:
   5.1 **KindBridge** with **`CL^k ≥ c`**;
   5.2 **MaskAdapter** (if constraints need translation), deterministic;
   5.3 Penalty **Ψ(`CL^k`)** to **R**. *(RM‑07 + C.3.3)*
6. **ScopeCoverage.** `U.ClaimScope(artifact) covers TargetSlice`. *(A.2.6)*

**Prohibitions.**
— **Mask ≠ Kind.** Guards **MUST NOT** treat the mask name as a synonym for the Kind. *(RM‑06)*

#### C.3.A:4.4 - **Guard\_SpanUnion\_Typed** — publish parallel coverage across independent support lines

**Intent.** Publish **SpanUnion** of scopes for **the same typed claim** supported by **independent** lines `L₁…Lₙ`.

**Guard\_SpanUnion\_Typed(C, k, {Lᵢ})** — **SHALL** include:

1. **Per‑line discipline.** For each line `Lᵢ`, first satisfy **Guard\_TypedClaim(C, k, Sliceᵢ)** (or its Cross‑context variant) at the relevant slices/supports.
2. **Independence justification.** Publisher **SHALL** include a partition or certificate showing that essential components of `Lᵢ` are **disjoint** from `Lⱼ` (no shared weakest link). *(A.2.6 §7.3)*
3. **Published scope.** `Scope_published = SpanUnion({Sᵢ})`, where each `Sᵢ` is the serial scope for line `Lᵢ`.
4. **No overreach.** The union **MUST NOT** include slices not covered by any `Sᵢ`.
5. **Typed consistency.** The **describedEntity** (kind **k**) is **the same** across lines; if not, normalize via subkinds or adapters before union.

**Note.** Independence and union rules are USM‑native; this macro ties them to typed claims without adding new algebra.


#### C.3.A:4.5 - **Guard\_XContext\_Typed** — Cross‑context typed reuse (both bridges)

**Intent.** Reuse **C** quantified over **k** in another Context’s **TargetSlice**.

**Guard\_XContext\_Typed(C, k, TargetSlice)** — **SHALL** include:

1. **Scope bridge.** There **exists** a Scope Bridge **b\_s** `(source = owner(C).Context, target = TargetSlice.Context)` with **CL ≥ c\_s**. *(Part B)*
2. **Kind bridge.** There **exists** a KindBridge **b\_k** `(source = owner(k).Context, target = TargetSlice.Context)` with **`CL^k ≥ c_k`**. *(C.3.3)*
3. **Mapped scope coverage.** `Scope′ = translate(b_s, ClaimScope(C))` and `Scope′ covers TargetSlice`.
4. **Mapped kind definedness.** `k′ = translate(b_k, k)` and `MemberOf(?, k′, TargetSlice)` is **defined**.
5. **Penalties (R only).** Apply **Φ(CL(b\_s))** and **Ψ(`CL^k(b_k)`)** to **R**.
6. **Loss notes.** Publisher **SHALL** attach loss notes from both bridges (rig bias, collapsed subkinds, etc.).

**Prohibitions.**
— **Do not** “merge” bridges; Scope and Kind are orthogonal channels.
— **Do not** alter **F** or **G** due to `CL`/`CL^k`; penalties land in **R** only.


### C.3.A:5 - Evaluation Semantics & Order (normative)

**E‑01 (Order of checks).** Guards **SHALL** check **typed compatibility first** (same‑Context `⊑` or KindBridge), **then** Scope coverage (USM), **then** apply penalties to **R** and verify freshness.

**E‑02 (Determinism).** Given fixed inputs (slices, bridges, versions), evaluation **MUST** be deterministic. “Latest” time, unversioned Standards, or implicit mappings are disallowed.

**E‑03 (Fail‑closed).** Undefined membership (`MemberOf`) or missing bridge **MUST** cause guard failure.

**E‑04 (No AT in guards).** AT is an editorial facet and **MUST NOT** be referenced. *(C.3.5 AT‑01/02)*

**E‑05 (Weakest link on congruence).** For chained bridges, effective **CL** / **`CL^k`** is the **minimum** of links.

**E‑06 (Separation of predicates).** Scope coverage and evidence freshness **SHALL** be distinct predicates; do not fold freshness into Scope or kinds.

**Evaluation order.** Apply checks in the order defined in **§5 (E‑01)**: typed compatibility → Scope coverage → penalties to **R** → freshness.


### C.3.A:6 - Conformance Checklist (normative)

| ID        | Requirement                                                                                                                              |
| --------- | ---------------------------------------------------------------------------------------------------------------------------------------- |
| **GC‑01** | Guards that admit/compose typed claims **SHALL** use **Guard\_TypedClaim** or **Guard\_TypedJoin** (or proven‑equivalent Context aliases).  |
| **GC‑02** | Guards that use RoleMasks **SHALL** use **Guard\_MaskedUse** (or equivalent) and comply with RM‑01…RM‑07.                                |
| **GC‑03** | Cross‑context typed reuse **SHALL** use **Guard\_XContext\_Typed** with **both** bridges; penalties **MUST** route to **R** (Φ/Ψ), not to F/G. |
| **GC‑04** | All guards **SHALL** declare **Γ\_time** explicitly and **SHALL** fail closed on undefined membership or missing bridges.                |
| **GC‑05** | Guards **MUST NOT** reference **AT**; any such reference **MUST** be removed or replaced with ΔF/ΔG/ΔR predicates.                       |
| **GC‑06** | Scope union **MUST** follow USM **SpanUnion** rules (independence justification); typed union **MUST NOT** change describedEntity.             |

#### C.3.A:6.1 - What counts as “proven‑equivalent” (editorial rule)

A Context may adopt a different surface phrasing **iff** the Context’s guard contains **all** obligations listed in the relevant macro, in the same logical roles (typed compatibility, Scope coverage, R penalties, freshness).

#### C.3.A:6.2 - Where penalties land (assurance calculus hook)

**Norm.** **Φ(CL)** (scope congruence) and **Ψ(`CL^k`)** (kind congruence) are **monotone non‑increasing** functions into **R**. Contexts **SHALL** calibrate them per policy; this Annex does not prescribe numeric forms.

#### C.3.A:6.3 - Minimal conceptual formulas (informative)

* **R after bridges:** `R_final = R_base × Φ(CL_scope) × Ψ(CL_kind)` (concept only).
* **No arithmetic on F/G.** F is ordinal (thresholds only); G is set‑valued (membership only).


### C.3.A:7 - Decision Trees (informative)

**D1 - Admitting a typed claim**

1. **same Context?** If **yes** → check `⊑` (`k ⊑ k′` if expected). If **no** → require **KindBridge**.
2. **Scope coverage?** Compute `covers(TargetSlice)`.
3. **Membership defined?** `MemberOf(?, k(′), TargetSlice)` defined? If **no** → deny.
4. **Bridges used?** Apply penalties **Φ/Ψ** to **R**.
5. **Freshness?** Check windows. **Optional**: `F ≥ F_k` if ESG mandates.

**D2 - Composing A → B**

1. Typed: `k_A ⊑ k_B` or **KindBridge** to `k′_B ⊑ k_B`.
2. Scope: `Scope(A) ∩ Scope(B)` covers TargetSlice.
3. Penalties: apply **Φ/Ψ** to **R**.
4. Freshness: along serial path.
5. If **mask** expected: either A implies it or add **mask adapter**.

**D3 - Union across lines**

1. Prove per‑line typed admission.
2. Provide independence partition.
3. Publish **SpanUnion**; no extrapolation.


### C.3.A:8 - Guard Anti‑patterns & Remedies (informative)

| Anti‑pattern                                     | Why it’s wrong                         | Remedy                                                             |
| ------------------------------------------------ | -------------------------------------- | ------------------------------------------------------------------ |
| **Widening G** to “fit” a type mismatch          | Conflates describedEntity with applicability | Introduce subkind, adapter, or KindBridge; keep G honest           |
| **Using mask name as kind**                      | Hides constraints; breaks determinism  | Register mask; reference constraints; promote to subkind if stable |
| **Ignoring `CL^k`** in Cross‑context classification | Under‑counts risk; silent drift        | Require KindBridge; apply **Ψ(`CL^k`)** to **R**                   |
| **Inferring Scope from Extension size**          | Scope ≠ Extension                      | Keep Scope (where) distinct from Extension (which instances)       |
| **Implicit “latest”** time                       | Non‑deterministic; non‑auditable       | Declare **Γ\_time** policy explicitly                              |
| **Gating on AT**                                 | AT is a facet, not a Characteristic    | Replace with ΔF thresholds or Scope/Evidence predicates            |


### C.3.A:9 - Worked Examples (informative, brief)

> Detailed scenarios remain in **C.3 §11**. This Annex sketches how the macros apply; cross‑reference as needed.

**E1 — Safety braking policy (same Context).**
Use **Guard\_TypedClaim**: `PassengerCar ⊑ Vehicle` passes; `ClaimScope` ∩ plant scopes covers TargetSlice; no bridges → no penalties; freshness checked.

**E2 — Cross‑plant reuse (both bridges).**
Use **Guard\_XContext\_Typed**: Scope bridge (CL=2) narrows temp; KindBridge (`CL^k=2`) collapses EV subkind. Apply **Φ(2)**×**Ψ(2)** to **R**; publish loss notes.

**E3 — API rule with adapter.**
Use **Guard\_TypedJoin**: producer `Request` → consumer expects `AuthenticatedRequest`. Either prove `⊑` or add adapter; Scope remains separate (API v2.3 with Γ\_time window).

**E4 — Masked clinic cohort across jurisdiction.**
Use **Guard\_MaskedUse** + **Guard\_XContext\_Typed**: registered mask, deterministic DOB constraint; KindBridge `CL^k=1`; Scope bridge CL depends on coding; penalties to **R**; Scope narrowed to overlap.


### C.3.A:10 - Rationale (why an Annex) (informative)

* **Focus.** Keeps **guard mechanics** together, easing adoption in ESG/Method templates.
* **Separation.** Prevents leakage of AT/typed flavor into “Scope math”.
* **Auditability.** Standard shapes let reviewers check determinism, bridges, penalties, and freshness quickly.
* **Inter‑pattern glue.** Hooks **USM**, **Kind‑CAL**, **Bridges**, and **F–G–R** without inventing new scales.

#### C.3.A:Annex A - How typed reasoning plugs into **Compliance & Regulatory Alignment**  \[A/I]

> **For managers.** This section shows how to make **regulatory adoption and reuse** precise, auditable, and portable using **Kinds**, **KindBridges** (with a kind‑bridge congruence level, noted as **CL^k** for editors), and **USM Scope**. It cleanly separates *what the law is about* from *where and when it applies*, and routes any cross‑jurisdiction uncertainty to **R** (assurance). It never changes **F** (form) or **G** (scope) to hide mismatches.


##### C.3.A:A.1 Purpose & fit

**What this solves.** Regulations and standards name classes of things (“**Adult person**,” “**Class II medical device**,” “**Personal data**,” “**Lease**”). In one context they are native; in another they are foreign. Without typed reasoning, teams either (a) hand‑translate terms (silently changing meaning), or (b) reduce everything to Context labels (“domain = EU”), which cannot be checked by guards.

**What we add.**

1. Model regulatory categories as **Kinds** (with `KindSignature` and `⊑`),
2. map them across Contexts with **KindBridges** and **type‑congruence `CL^k`**,
3. express **Claim scope (G)** over **Context slices** that explicitly list *jurisdiction, version, and a time selector (Γ_time)*, and
4. apply **R‑penalties** (`Ψ(CL^k)`and, if scope is bridged,`Φ(CL)`) while **keeping F and G unchanged**.


##### C.3.A:A.2 Normative obligations

**Conformance.** A model or authoring action conforms to A.2 iff it satisfies **C‑REG‑1..C‑REG‑8** below.

**C‑REG‑1 (Regulatory kinds).** Regulatory categories **SHALL** be represented as `U.Kind` in the authority’s Context (e.g., `AdultPerson@RegY`, `MedicalDeviceClassII@FDA`, `PersonalData@GDPR`, `Lease@IFRS`). Each such kind **SHALL** have a `KindSignature` with a declared **F** level (C.3.2).

**C‑REG‑2 (KindBridge).** Cross‑context reuse of a regulatory category **MUST** declare a **KindBridge** with a kind‑bridge congruence level (**CL^k**) and **loss notes** (C.3.3). The mapping **SHALL** preserve the “is‑a / subkind‑of” direction and **MUST NOT** invert it.

**C‑REG‑3 (Scope is USM).** Regulatory **applicability** (jurisdiction, effective dates, product families, platforms) **SHALL** be expressed as **Claim scope (G)** over `U.ContextSlice`, with an explicit **time selector (Γ_time)**. Applicability **MUST NOT** be encoded into kinds.

**C‑REG‑4 (No synonym shortcuts).** Editors **MUST NOT** treat legal terms as synonyms of local kinds without a KindBridge. Any term alignment **SHALL** be documented (mapping + `CL^k` + loss notes).

**C‑REG‑5 (Determinism).** `MemberOf(e, k_reg, slice)` **MUST** be deterministically evaluable when used in guards (no “latest law” or unstated grace periods).

**C‑REG‑6 (Penalties land in R).** When a claim or guard relies on Cross‑context classification (membership decided via a KindBridge), the receiving Context **MUST** apply the **kind‑bridge penalty** (based on **CL^k**) to **R**; if the **Scope** is also bridged, apply the **scope‑bridge penalty** (based on **CL**) to **R** as well. **Invariant:** penalty routing changes **R** only; **F** and **G** remain unchanged.

**C‑REG‑7 (Editioning).** Changes in law/regulator guidance that alter membership or applicability **SHALL** be recorded as content changes: update `KindSignature` (kinds) and/or update **Claim scope** (ΔG±). Guards **MUST** name a time selector (Γ_time) and **MUST NOT** rely on an implicit “latest” time.

**C‑REG‑8 (Masks, not clones).** Local process nuances (e.g., clinic‑specific cohort definitions) **SHALL** be captured with **RoleMasks** over the adopted kind; editors **MUST NOT** clone a new kind unless a stable **subkind** is warranted.


##### C.3.A:A.3 Guard macros (ready to use)

**(a) `Guard_RegAdopt` — adopt a regulatory requirement into a Context (Plain: check scope, map the legal category, and account for penalties)**

Use when an internal policy is defined by reference to an authority’s category.

```
Inputs: Claim P (policy), RegKind k_reg in Context R_auth, TargetSlice S_local
Guard_RegAdopt(P, k_reg, S_local):
  1. ScopeCoverage:       U.ClaimScope(P) covers S_local                 // USM
  2. Γ_time:              S_local specifies Γ_time (no "latest")         // USM
  3. KindBridge:          a KindBridge exists that maps the legal category to a local kind, with **CL^k** at least the minimum policy level
  4. MemberOfDefined:     MemberOf(?, k_local, S_local) is defined       // determinism
  5. Penalties→R:         apply the **kind‑bridge penalty** (based on CL^k) to **R**
  6. ScopeBridge?         if the policy’s scope lives in the authority’s Context, translate it via a Scope Bridge; apply the **scope‑bridge penalty** (based on CL) to **R**
  7. EvidenceFreshness:   freshness windows for any bound evidence hold  // C.2.2
```

**(b) `Guard_RegChange` — react to a regulatory change (Plain: re‑issue the kind and/or scope and refresh penalties)**

```
Inputs: Reg change Δ (new edition, guidance), impacted kinds/claims
Guard_RegChange(Δ):
  1. Identify impact:      does Δ alter KindSignature (membership) or Scope predicates?
  2. If KindSignature:     version k_reg; update KindBridge; re-evaluate CL^k; update loss notes
  3. If Scope:             publish ΔG± (widen/narrow) to Claim scope; update guards
  4. Reassess penalties:   recompute Ψ(CL^k), Φ(CL) → R
  5. Γ_time discipline:    set sunrise/sunset; forbid implicit retroactivity in guards
```

**(c) `Guard_RegXContextUse` — cross‑jurisdiction use with both bridges (Plain: move scope and kind, then account for both penalties)**

```
Guard_RegXContextUse(P, k_reg@R_auth, S_local@R_local):
  1. Scope bridge:      a Scope Bridge from the authority Context to the local context exists with CL at least the policy minimum; the translated scope covers the local slice
  2. Kind bridge:       a KindBridge maps the legal category to a local kind with **CL^k** at least the policy minimum
  3. MemberOfDefined:   MemberOf(?, k_local, S_local) is defined
  4. Penalties→R:       apply the **scope‑bridge** and **kind‑bridge** penalties to **R**
  5. Loss-guided narrow: optionally narrow Scope' where known losses are material (best practice)
```


##### C.3.A:A.4 Worked examples  \[I]

**(1) Healthcare — “Adult” dosage rule across jurisdictions**

*Reg source.* Jurisdiction Y defines `AdultPerson@RegY` (AT around K2, F4) with **age at least 18**; your hospital Context uses `AdultPatient` (**age at least 21**).
*Claim.* “For all `x ∈ AdultPatient`: dosage ≤ D/kg for drug M.”
*Adoption.*

* **KindBridge.** Map `AdultPerson@RegY → AdultPatient`; **`CL^k = 1`**; **loss note:** boundary mismatch (18↔21).
* **Scope.** `{jurisdiction=Y, formulary=M, time selector (Γ_time)=from 2026‑01‑01}`.
* **Guard.** `Guard_RegAdopt` passes; **R** penalized by `Ψ(1)`. Policy narrows Scope to mapped cohort (age≥21) for in‑house use.
* **Change.** If Y changes adult to ≥19 (new edition), run `Guard_RegChange`: version the kind, refresh the bridge, re‑assess `CL^k`, update guards.

**(2) Privacy — GDPR↔CCPA PII across Contexts**

*Reg kinds.* `PersonalData@GDPR`, `PersonalInformation@CCPA`.
*Internal kind.* `PersonalData@Product` with masks per data store.
*Policy claim.* “No sharing of `SensitiveAttribute` outside processors.”
*Adoption.*

* **KindBridges.** `SensitiveAttribute@GDPR → SensitiveAttribute@Product` (**`CL^k=2`**); `SensitivePersonalInformation@CCPA → SensitiveAttribute@Product` (**`CL^k=1`**, loss: biometric nuance).
* **Scope.** Two policies with **SpanUnion** over `{jurisdiction=EU}` and `{jurisdiction=CA}`, each with its own **Γ\_time** windows and evidence freshness.
* **Guards.** For CA, apply stronger **R** penalty (`Ψ(1)`), and narrow to the mapped subset (exclude ambiguous fields).
* **Do not.** Do not rename GDPR terms to local labels **without a KindBridge**.

**(3) Export control — US EAR “600‑series” classification**

*Reg kind.* `EAR600SeriesItem@US` (AT≈K2, F3→F4 as predicates are formalized).
*Local kind.* `Product@Company`.
*Work scope.* `{destination=countries, end_use, time selector (Γ_time)=shipment date}` for the shipping capability.
*Adoption.*

* **KindBridge.** Map `EAR600SeriesItem@US → Product@Company`; `CL^k=2` (loss: component kit edge cases); loss notes recorded.
* **Capability guard (Method–Work).**

  * `U.WorkScope(Ship)` covers `JobSlice` (destination, end use, time).
  * `MemberOf(product, EAR600_mapped, JobSlice)` defined (classification present).
  * Apply `Ψ(2)` to **R** (classification uncertainty) and, if reusing US scope text, `Φ(CL_scope)` too.
* **Outcome.** Shipment admitted only for allowed destinations; higher **R** may require manual review.

**(4) Finance — IFRS vs US GAAP “Lease”**

*Reg kinds.* `Lease@IFRS`, `Lease@USGAAP`.
*Local kind.* `LeaseStandard@Corp` used in policy “recognize lease liabilities.”
*Adoption.*
* **KindBridge.** `Lease@IFRS → LeaseStandard@Corp` (**`CL^k=2`**; loss: short‑term exceptions differ).
* **Scope.** `{jurisdiction=IFRS, Γ_time=financial period, ledger=v7}`.
* **Evidence.** LA plans cover subkinds (operating vs finance) per your classification; the kind‑bridge congruence level (CL^k) drives extra testing near boundary cases.


##### C.3.A:A.5 Design guidance & pitfalls  \[I]

**Do this.**

* **Treat regulatory categories as Kinds.** Put the *definition* into `KindSignature` (aim for **F4** predicates where practical).
* **Make time explicit.** In guards, require a **time selector (Γ_time)** for effective dates and grace periods. Forbid “latest”.
* **Publish bridges with loss notes.** If two jurisdictions’ categories are “almost the same,” say *how*, rate **`CL^k`**, and note what is lost.
* **Split “where” from “what.”** Keep **Scope (G)** over `U.ContextSlice` (jurisdiction, plant, Standard versions) separate from **MemberOf** on the kind.
* **Route uncertainty to R.** Use `Ψ(CL^k)` and `Φ(CL)`; never modify **F/G** to hide ambiguity.

**Avoid this.**

* **Synonym games.** Don’t alias “Adult” to local `AdultPatient` in prose. Use a **KindBridge**.
* **Scope by labels.** “Domain = EU” is not a guard. Use explicit `U.ContextSlice` fields (jurisdiction, version, time selector) and **Scope** predicates.
* **Hiding time.** Never rely on “current law”; always fix **Γ\_time** (point/window/policy).
* **Widening G to compensate for type gaps.** If kinds don’t line up, introduce a **subkind**, add a **mask/adapter**, or **narrow**; don’t “make the scope bigger”.


##### C.3.A:A.6 Migration checklist  \[I]

1. **Inventory** regulatory references in policies/specs.
2. **Create Kind cards** for referenced legal categories (intent summary, `KindSignature` + **F**, known subkinds, AT tag if helpful).
3. **Publish KindBridges** to your local kinds with `CL^k` and loss notes.
4. **Rewrite guards** to use **Scope coverage** (USM) plus `MemberOf` on the mapped kind; add an explicit **time selector (Γ_time)**.
5. **Wire penalties**: `Ψ(CL^k)` and `Φ(CL)` lower **R**; refresh evidence windows.
6. **Catalog RoleMasks** for local nuances; promote frequently reused masks to **subkinds**.


##### C.3.A:A.7 Manager’s one‑page pattern  \[I]

* **Question 1 — Where does the rule apply?** → **Scope (G)** over **Context slices** (jurisdiction, plant, Standard, and a **time selector (Γ_time)**).
* **Question 2 — About what things?** → **Kind** (regulatory category) with a **KindBridge** if foreign.
* **Gate recipe.** **Scope covers the TargetSlice** and **membership for the mapped kind is defined**, and **both bridges are present where needed**; then **apply bridge penalties to R** and decide.
* **Change handling.** New law edition? Update `KindSignature`/Bridge (kinds) and/or **Scope** (ΔG); never rely on “latest.”
* **Accountability.** Keep **loss notes**, **CL/CL^k**, and **Γ\_time** in the decision record.


#### C.3.A:Annex B - How typed reasoning plugs into **Assurance Lanes (VA/LA/TA) & Evidence design**  \[A/I]

**Intent (manager’s view).** Typed reasoning turns “prove/test/qualify” into a **repeatable plan**. By making *what the rule talks about* explicit (named **Kinds**, their **subkinds**, and optional **RoleMasks**), you can:

1. design **proof obligations** that actually quantify over the right things (VA),
2. build **test plans** that cover the **right variants/subkinds** in the **right context slices** (LA), and
3. isolate **tool risk** (TA) instead of letting it bleed into scope or type semantics.

**Invariant reminders.**
— **Scope (G)** is *where* a claim holds — expressed over `U.ContextSlice` (with an explicit time selector, **Γ_time**).
— **Kind membership** is *which things* the claim ranges over inside that slice — checked with `MemberOf(… , kind, slice)`.
— **Bridge penalties**: the **scope‑bridge penalty** (based on **CL**) and the **kind‑bridge penalty** (based on **CL^k**) both lower **R** (assurance). They never change **F** (form) or **G** (scope).

##### C.3.A:B.1 What you get with typed assurance  \[I]

* **Targeted proofs (VA).** If a policy says “for every **PassengerCar** …” (notation hint: ∀x:PassengerCar), the VA lane now has a clear target. You can prove obligations **once for the kind** (and its subkinds), instead of re‑proving per ad‑hoc label.
* **Subkind‑aware test plans (LA).** Test matrices are indexed by **subkinds** (and RoleMasks) × **context slices**; coverage stops being accidental.
* **Deterministic guards.** A test/proof either **applies** to the TargetSlice and Kind (`Scope covers & MemberOf defined`) or it doesn’t. No “latest,” no silent widening.
* **Clean tool boundaries (TA).** You qualify the **prover/model‑checker/classifier** once and route **tool confidence** to TA, not to “broadened” claims.


##### C.3.A:B.2 Normative obligations for evidence design

**EA‑1 (Two checks).** Every VA/LA artifact that supports a typed claim **SHALL** bind **both**:

* **Scope predicate**: `U.ClaimScope(Claim) covers TargetSlice` (with explicit `Γ_time`), and
* **Kind predicate**: `MemberOf(?, k, TargetSlice)` is **defined** (deterministic).

**EA‑2 (Subkind coverage).** When a claim quantifies over `k`, target‑contexts **SHALL** justify LA coverage **per relevant subkind** of `k` (or **per RoleMask** if masks stand in for stable subkinds). “Representative set” **MUST** be stated explicitly.

**EA‑3 (Independence for unions).** If a published **SpanUnion** of evidence lines is used to enlarge covered area, **independence** of lines **SHALL** be documented (no shared weakest link).

**EA‑4 (Bridges accounted).** If a VA/LA artifact travels across Contexts:

* **Scope movement** **SHALL** use a Scope Bridge (Part B) with **CL** and apply the **scope‑bridge penalty** to **R**.
* **Kind movement** **SHALL** use a **KindBridge** (§ C.3.3) with **CL^k** and apply the **kind‑bridge penalty** to **R**.
  Neither movement **SHALL** alter **F** or **G**.

  Neither movement **SHALL** alter **F** nor **G**.

**EA‑5 (Freshness).** LA evidence **SHALL** declare freshness windows tied to `Γ_time` (no implicit “latest”). Expiry **MUST** fail guards closed until refreshed.

**EA‑6 (No scope‑by‑wording).** Editors **MUST NOT** widen **G** by rewriting a claim to sound “more general.” Widening **G** (ΔG+) is permitted **only** with new support that truly enlarges the set of slices.

**EA‑7 (TA separation).** Tool qualification (TA) **SHALL** be tracked independently. VA/LA guards **MUST NOT** substitute “tool is trusted” for content proof/coverage.


##### C.3.A:B.3 Designing the **evidence matrix**  \[I]

A practical way to plan LA/VA is a **matrix**:

| Row set                       | Column set                                                   | Cell content                                                                                                           |

| ----------------------------- | ------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------- |
| **Kinds** (subkinds or masks) | **Context slices** (Standard versions, env ranges, `Γ_time`) | **Evidence unit** (proof fragment, test batch, monitoring window), with **Scope** and **MemberOf** predicates attached |

* **Choose rows.** Start with the kind and list **relevant subkinds** (notation hint: kᵢ is a subkind of k) or stable **RoleMasks**.
* **Choose columns.** Split your declared **Scope (G)** into **named slices** you intend to support (e.g., “dry, speed up to 50” and “wet, speed up to 40” with specific rigs and versioned Standards).
* **Fill cells.** Attach one or more **evidence units** per cell (proof obligations for VA; test campaigns/monitoring windows for LA). Mark **bridged** cells and their **CL/CL^k** penalties to **R**.

> **Tip.** For formal kinds and “up‑to‑iso” kinds (AT K2/K3), expect **more rows** (more variants to cover). For instance‑like kinds (AT K0), expect **fewer rows** and **tighter columns** (narrow slices, stricter freshness).


##### C.3.A:B.4 VA lane — proofs that match the kind  \[A/I]

**What VA contributes.** Proofs reduce ambiguity and eliminate many LA burdens when they **truly quantify over the intended kind** and **live in the declared Scope**.

**VA‑patterns (informative):**

* **Proof over the Kind (F7–F8).** “For every **PassengerCar**, the property holds” (notation hint: ∀x:PassengerCar). If the property depends on subkind‑specific rules, split lemmas per subkind.
* **Proof‑carrying components.** When the content is **F8** (dependent types), the build rejects violations; LA can shrink to **conformance smoke** within the slices.
* **Up‑to‑iso (AT K3).** Equational reasoning “up‑to‑iso” is acceptable **only** if the KindSignature works at that level and receivers accept **KindBridge** that preserves equivalences.

**VA‑obligations (normative):**

* **VA‑1.** A proof artifact **SHALL** cite the **Kind** it quantifies over and reference the **Claim scope** slices it assumes.
* **VA‑2.** Cross‑context acceptance of proofs **SHALL** use both bridges (Scope+Kind) and apply **Φ/Ψ** penalties to **R** (never to F/G).
* **VA‑3.** If the proof relies on **tool kernels**, their **TA** status **SHALL** be disclosed; weakening TA **MUST NOT** be “paid for” by silent scope widening.

**Mini‑example (VA).**
Policy P: “∀ x: PassengerCar. stoppingDistance(x) ≤ 50 m on dry at speed≤50.”
— **Kind**: `PassengerCar ⊑ Vehicle` (K2), signature F4 (predicates).
— **Scope**: `{surface=dry, speed≤50, rig=v3, Γ_time=rolling 180 d}`.
— **Proof**: a proof assistant lemma over `PassengerCar` (tool choice is context‑local).
— **Reuse** to Plant‑B: a Scope Bridge with **CL=2** (rig bias) and a KindBridge with **CL^k=3** (same classification). Apply the **scope‑bridge penalty** for CL=2 and the **kind‑bridge penalty** for CL^k=3 to **R**.


##### C.3.A:B.5 LA lane — tests & monitoring that cover the right variants  \[A/I]

**What LA contributes.** Empirical assurance for claims with executable semantics or physical interfaces; especially when F ≤ F6 or when stochastic/real‑world effects matter.

**LA‑patterns (informative):**

* **Cover by subkind.** Test at least one representative per subkind; add more where variability inside a subkind matters.
* **Boundary probing.** Concentrate tests near **KindSignature** and **Scope** boundaries (e.g., temp limits, speed caps).
* **Hybrid checks (F6).** When software controllers interact with physical systems, ensure **both sides** declare obligations; include their interaction cases in the matrix.
* **Monitoring windows.** For live systems, define **Γ\_time policies** (e.g., rolling 30 d) and tie alerts to **kind‑aware metrics** (“error rate per `ServiceInstance`”).

**LA‑obligations (normative):**

* **LA‑1.** Each test campaign **SHALL** specify **rows/columns** in the evidence matrix and attach **Scope/MemberOf** predicates to each run.
* **LA‑2.** Freshness windows **SHALL** be explicit and enforced in guards (no “latest”).
* **LA‑3.** If a **KindBridge** merges subkinds, test plans **SHALL** be adjusted (more cells, stricter acceptance), and the **kind‑bridge penalty** (based on CL^k) applied to **R**.
* **LA‑4.** Publishing **SpanUnion** coverage requires the independence note (which support lines differ).

**Mini‑example (LA).**
Claim: “For all `x ∈ Vehicle`: brakeDistance ≤ 50 m on dry, ≤ 40 m on wet.”
— **Rows**: `{PassengerCar, LightTruck}`.
— **Columns**: `{dry, ≤50}`, `{wet, ≤40}` with rigs and versions.
— **Cells**: PC/dry covered by track tests; LT/wet by simulation + surrogate tests (independent lines → SpanUnion allowed).
— **Bridge** to jurisdiction Y collapses EV vs ICE ⇒ `CL^k=2`. Apply **Ψ(2)** to **R**; add extra wet tests to compensate.


##### C.3.A:B.6 TA lane — tool qualification where it belongs  \[A/I]

**What TA contributes.** Confidence in **provers, checkers, model‑checkers, data classifiers** and pipelines. TA is about the **machinery**, not the **claim** or **kind** semantics.

**TA‑patterns (informative):**

* **Prover kernels.** Audit/qualification of the kernel version used for VA proofs.
* **Automated Model‑checkers.** Qualification against seeded faults; document limits (precision, nondeterminism).
* **Classifiers used for `MemberOf`.** If membership uses ML or rules engines, qualify the **classifier** separately; any drift monitoring belongs to LA freshness.

**TA‑obligations (normative):**

* **TA‑1.** Tools critical to VA/LA **SHALL** declare their qualification status and version; guards **SHALL** reference these declarations when they matter.
**TA‑2.** Lower tool qualification **MUST NOT** be hidden by relaxing **F** or widening **G**. target‑contexts may offset it by demanding **more evidence** in **R** (for example, extra tests), per policy.


##### C.3.A:B.7 Guard macros for evidence planning & attachment

**Guard\_EvidencePlan\_Typed** — approve a plan that is adequate for a typed claim.
*Plain reading.* The first macro checks that the plan names the rows (kinds or masks) and columns (slices), that scope and membership can be checked for each cell, that any Cross‑context moves declare bridges, and that penalties are budgeted in **R**.

```
1. MatrixDeclared:    Evidence matrix rows = {subkinds or masks of k}; columns = {TargetSlices within ClaimScope}
2. ScopeBound:        For each column, ClaimScope covers that slice with explicit Γ_time
3. KindBound:         MemberOf(?, k, slice) is defined (deterministic) for all planned slices
4. BridgeBudgeted:    If cross-context:
                        (a) Scope Bridge(s) declared with CL → attach the **scope‑bridge penalty** to the **R** budget
                        (b) KindBridge(s) declared with CL^k → attach the **kind‑bridge penalty** to the **R** budget
5. FreshnessPolicy:   LA freshness windows specified per slice; monitoring plan defined (if live)
6. IndependenceNote:  If SpanUnion is claimed, independence justification attached
7. TADecls:           Tools and their TA status listed; residual risk routed to R (not to F/G)
```

**Guard\_EvidenceAttach\_Typed** — attach concrete evidence to a state change.
*Plain reading.* The second macro checks that each attached evidence unit clearly states which row and column it covers, binds scope and membership in a reproducible way, applies bridge penalties to **R**, and respects freshness.

```
1. CellMatch:         Each evidence unit cites (subkind/mask, slice) it covers
2. PredicateBinding:  Evidence embeds Scope and MemberOf predicates (or references them verifiably)
3. BridgeApplied:     If evidence is bridged, apply the **scope‑bridge** and/or **kind‑bridge** penalties to **R**; record loss notes
4. FreshnessMet:      Evidence within declared freshness; else guard fails closed
5. VA/LA Mix:         If VA present, verify it matches the quantified Kind; if LA fills gaps, show matrix deltas
6. TAConsistent:      Tool versions match TA declarations used at planning time
```


##### C.3.A:B.8 Anti‑patterns & remedies

| Anti‑pattern                       | Why it’s risky                                | Remedy                                                              |
| ---------------------------------- | --------------------------------------------- | ------------------------------------------------------------------- |
| “We tested one golden case.”       | Hides variant risk; ignores subkinds.         | Build a subkind‑indexed matrix; add boundary tests per column.      |
| “Latest data suffices.”            | Non‑deterministic; un‑auditable.              | Declare `Γ_time` windows; fail closed on expiry.                    |
| “Tool is trusted, so we’re done.”  | Confuses TA with VA/LA; misses content risk.  | Keep TA separate; add VA proofs or LA tests as needed.              |
| Bridging without penalties         | Understates risk; mapping gaps surface later  | Apply **scope‑bridge** and **kind‑bridge** penalties to **R**; publish loss notes. |
| Widening G to cover evidence gaps. | Conflates applicability with available tests. | Keep G honest; expand matrix or lower claim scope explicitly (ΔG−). |
| Inferring scope from how many items match    | Scope is not the same as membership      | Keep **Scope** (where it applies) distinct from **membership** (which items match in the slice). |

##### C.3.A:B.9 End‑to‑end example (manager’s cheat‑sheet)  \[I]

**Scenario.** You want to publish “∀ x: PassengerCar. brakeDistance ≤ 50 m dry; ≤ 40 m wet” across two plants.

1. **Kinds.** `PassengerCar ⊑ Vehicle` (K2, signature F4).
2. **Scope (G).** `{surface in {dry, wet}, speed limits, rig version, time selector (Γ_time)=rolling 180 days}` in Plant‑A.
3. **VA.** Prove the property for **PassengerCar** using a proof assistant, and cite the **Scope** slices it assumes.
4. **LA.** Build an evidence matrix with rows `{PassengerCar}` and columns `{dry, up to 50}` and `{wet, up to 40}`, including rig variants; add boundary tests near the limits.
5. **TA.** Qualify the prover kernel and the automated checker used for wet surrogates.
6. **Bridge.** To Plant‑B: a **Scope Bridge** with **CL=2** (rig bias) and a **KindBridge** with **CL^k=3** (same classification).
7. **Penalties.** Apply the **scope‑bridge penalty** for CL=2 and the **kind‑bridge penalty** for CL^k=3 to **R**. Per policy, add extra test cells in Plant‑B to compensate for rig bias.
8. **Guards.** Use `Guard_EvidenceAttach_Typed` on the state change; include freshness checks.

**Outcome.** A defensible, auditable publication: typed, scoped, with clear evidence coverage and explicit risk penalties — no conflation of abstraction with applicability, and no tool risk smuggled into content.

#### C.3.A:Annex C. ESG guards

**Status note.** This profile restates the guard semantics from **§4** for ESG/Method contexts. It does **not** add obligations; where wording diverges, **§4 controls**.

##### C.3.A:C.1 **ESG** guard obligations (normative)

When a state transition publishes or affirms a claim that quantifies over kinds, the guard **SHALL**:

1. **Scope coverage (USM).**
   `U.ClaimScope(Claim) covers TargetSlice` (singleton or finite set) and TargetSlice **declares `Γ_time`** (no “latest”).

2. **Typed definedness.**
   A **deterministic membership check** is available for every kind used by the claim in the **TargetSlice**. If membership cannot be evaluated in that context, the guard **fails closed**.

3. **Typed compatibility (same Context).**
 If a downstream consumer expects a specific kind, then for each kind used by the claim either:
* the used kind is an **is‑a / subkind‑of** the expected kind, or
* a documented **RoleMask** for the expected kind is used and its constraints are **met and observable** in the **TargetSlice**.

3. **Typed compatibility (Cross‑context).**
  If any referenced kind is **used across Contexts**, a **KindBridge** **SHALL** be declared with a published **type‑congruence level** (minimum acceptable level per Context policy), order preserved (no inversions), and **loss notes**.  
The guard **SHALL** apply the **kind‑bridge penalty** to **R**.

4. **Scope translation (Cross‑context claim use).**
If the Claim’s scope originates in another target‑context, a **Scope Bridge** with a published **congruence level** is required; apply the **scope‑bridge penalty** to **R**.

6. **Formality threshold (if gated).**
   If the ESG state requires rigor, enforce `U.Formality(Claim) ≥ F_k` (C.2.3).
   (*Note:* Raising F does **not** widen G; do not substitute.)

7. **Evidence freshness (R).**
   Where the new state implies trust, assert freshness windows and confirm **no expired bindings**.

**Prohibitions (normative).**

* Do **not** widen **G** to “hide” a type mismatch. Fix typed compatibility (introduce a subkind, use a RoleMask, publish a KindBridge) or reject.
* Do **not** treat a **mask name** as a kind—masks must be **registered** and **deterministic**.
* Do **not** infer G from the size of a kind’s **Extension**; **Scope ≠ Extension**.


##### C.3.A:C.2 - **Method–Work** guard obligations (normative)

To admit a **capability** for a specific **Work** step at **JobSlice**, the guard **SHALL**:

1. **Work scope coverage (USM).**
   The capability’s **Work scope** covers the **JobSlice**, and the **JobSlice** includes an explicit **time selector (Γ_time)**.


2. **Measures & qualification.**
   **All** required `U.WorkMeasures` hold at JobSlice and the `U.QualificationWindow` is **valid at `Γ_time`**.

3. **Typed inputs (same Context).**
   For each declared input kind (or RoleMask), assert:
   * **Membership check available:** the system can deterministically decide whether the input belongs to the expected kind in this **JobSlice**.
   * **Compatibility:** the provided input kind is an **is‑a / subkind‑of** the expected kind, or the **RoleMask** constraints are satisfied and observable.

3. **Typed outputs / post‑conditions (if declared).**
   If the capability guarantees an output kind `k_out`, record the obligation to **demonstrate** `MemberOf(output, k_out, JobSlice)` (typically via conformance tests or audits).

4. **Cross‑context typed use.**
   If inputs/outputs are typed in a different target‑context than the capability or JobSlice:
   * **KindBridge(s)** are required with a published **type‑congruence level** and **loss notes**; apply the **kind‑bridge penalty** to **R**.
   * If the capability resides in another target‑context, a **Scope Bridge** with a published **congruence level** is required; apply the **scope‑bridge penalty** to **R**.

4. **No substitution by G.**
   Do not “fix” a typed mismatch by widening the **Work scope**. Use an **adapter** or a **RoleMask**, or reject.


##### C.3.A:C.3 - Guard macros (ready‑to‑use)

**ESG\_TypedGate(Claim, TargetSlice, Kinds, thresholds)**
*Manager view:* The following macros are for editors; target‑contexts may automate them if desired. Managers can read the comments on each step; the checks are the same ones described in Plain language above.

```
1  assert ClaimScope(Claim) covers TargetSlice                 // USM
2  assert Γ_time(TargetSlice) is explicit                  // no "latest"
3  for each kind k in Kinds used by Claim:
4      assert membership_defined(k, TargetSlice)               // C.3.2 K-07
5  if same-Context typed expectations exist:
6      assert is_subkind(k, k_expected) OR meets_mask_constraints(k_expected, TargetSlice)
7  if cross-context kinds:
8      assert KindBridge(k, k') with type_congruence ≥ c_kind and loss notes
9      apply_kind_bridge_penalty(type_congruence)
10 if cross-context scope:
11     assert ScopeBridge(Claim.Context, TargetSlice.Context) with congruence ≥ c_scope
12     apply_scope_bridge_penalty(congruence)
13 if F-threshold applies: assert Formality(Claim) ≥ F_k        // C.2.3
14 if trust implied: assert Fresh(evidence, window) AND NoExpiredBindings
```

**MethodWork\_TypedGate(Capability, JobSlice, Inputs/Outputs, thresholds)**

```
1  assert WorkScope(Capability) covers JobSlice                // USM
2  assert Γ_time(JobSlice) is explicit
3  assert WorkMeasures(JobSlice) satisfied AND QualificationWindow holds
4  for each expected input-kind k_in:
5      assert membership_defined(k_in, JobSlice)
6      assert is_subkind(k_input, k_in) OR meets_mask_constraints(k_in, JobSlice)
7  if declared output-kind k_out: record obligation to show MemberOf(output,k_out,JobSlice)
8  if cross-context kinds: assert KindBridge(… ) with type_congruence ≥ c_kind; apply_kind_bridge_penalty(type_congruence)
9  if cross-context capability/scope: assert ScopeBridge(… ) with congruence ≥ c_scope; apply_scope_bridge_penalty(congruence)
```

##### C.3.A:C.4 - Worked examples (manager‑focused)

**(A) ESG — Promote a braking policy to *Effective*.**
*Claim.* “For all **vehicles**: braking distance is **≤ 50 m** on dry and **≤ 40 m** on wet.”
*TargetSlice.* `{surface∈{dry,wet}, speed≤50 km/h, rig=v3, Γ_time=rolling 180 d}`
*Kinds.* `Vehicle` (K2, `KindSignature` at F4); the consumer subsystem expects `PassengerCar`.
**Guard.**

1. **Scope** covers TargetSlice (USM ✓).
2. **Definedness** of `MemberOf(?, Vehicle, TargetSlice)` ✓.
3. **Typed compatibility:** `PassengerCar ⊑ Vehicle` ✓.
4. **No bridges** → no penalties.
5. **F‑threshold:** `Formality(Claim) ≥ F4` ✓.
6. **Freshness:** evidence ≤ 180 days ✓.
   **Result:** Transition allowed. F/R apply weakest‑link on support paths; G remains the set declared.


**(B) Method–Work — Admit “RiskScore” step with typed input.**
*Capability.* `ComputeRiskScore` expects `AuthenticatedRequest`; promises SLOs (latency ≤ 50 ms, error ≤ 0.5 %).
*JobSlice.* `{api=v2.3, region=eu‑west, Γ_time=now, traffic_class=gold}`
*Inputs.* Producer emits `Request` (no auth guarantee).
**Guard.**

1. **Work scope** covers JobSlice; **Measures** & **QualificationWindow** ✓.
2. **Typed inputs:** `MemberOf(?, AuthenticatedRequest, JobSlice)` must hold. Not true for raw `Request`.
3. **Remedy:** insert an **adapter** that enforces/attests auth → yields `AuthenticatedRequest`.
4. **No Cross‑context** → no bridges.
   **Result:** Admitted **with adapter**; Scope unchanged; R relies on adapter evidence. Widening Work scope is **not** acceptable to bypass typed mismatch.


**(C) Cross‑context ESG — Adopt policy across plants.**
*Claim Context.* `SafetyLab@2026`. *target Context.* `PlantB@EU`.
*Kinds.* `Vehicle ↦ TransportUnit` via **KindBridge** with **`CL^k=2`** (EV/ICE collapsed); **Scope Bridge** from lab to plant with **CL=2** (rig bias ±2 %).
**Guard.**

1. Translate **Scope** and **cover** `TargetSlice_B`.
2. Translate **Kind** and ensure `MemberOf(?, TransportUnit, TargetSlice_B)` is **defined**.
3. Apply the **scope‑bridge penalty (level 2)** and the **kind‑bridge penalty (level 2)** to **R**; publish loss notes.
   **Result:** Transition allowed with reduced **R**; G is the **mapped** set; F unchanged.


##### C.3.A:C5 - Anti‑patterns & remedies (normative where noted)

| Anti‑pattern                                      | Why it’s wrong                                 | Remedy                                                                              |
| ------------------------------------------------- | ---------------------------------------------- | ----------------------------------------------------------------------------------- |
| Widening **G** to “make kinds match”              | Conflates **describedEntity** with **applicability** | Introduce **subkind**, **RoleMask**, or **KindBridge**; keep G honest.              |
| Using a **mask name** as a kind                   | Hides constraints; breaks determinism          | Register mask; ensure constraints are observable; promote to **subkind** if reused. |
| Ignoring **`CL^k`** when classifying across Contexts | Under‑counts risk                              | Require **KindBridge**; apply **Ψ(`CL^k`)** to **R**; record loss notes.            |
| Inferring **Scope** from the size of the **Extension** | Scope is not the same as Extension            | Keep **Scope** (where it applies) distinct from **Extension** (which items count in the slice). |
| Implicit “**latest**” time                        | Non‑deterministic guard                        | Require explicit **`Γ_time`** (point/window/policy).                                |


### C.3.A:End

## C.13 — Constructional Mereology (Compose‑CAL)

### C.13:1 - Intent

Provide a single, generative calculus for part–whole structure so that **all** structural relations in FPF are *constructed* (not merely declared) from three primitives and thereby inherit extensional identity by design. The calculus is hidden from day‑to‑day users behind relation aliases; its artefacts are traces that witness how a whole arises from its parts.

Also known as *“Γₘ mereology”*, *“constructor‑based composition”*.

**Layer.** *calculus.*
**Depends on.** Kernel only (no upward imports).
**Consumed by.** CT2R‑LOG (B.3.5) Working‑Model alias logic and any FPF pattern that needs part–whole semantics. Compose‑CAL does **not** import alias definitions; it merely emits traces that others may reference.

Compose‑CAL introduces a **single construction operator Γₘ** with exactly three constructors—**sum**, **set**, **slice**—sufficient to build structural wholes, collections‑as‑wholes, and aspects **without** extending the Kernel’s type set. No “parallel” or “temporal slice” constructor is added. Every construction yields a **trace** that serves as the witness for structure. Human‑facing relations such as *ComponentOf*, *MemberOf*, *AspectOf* are defined elsewhere as **Working‑Model aliases** and are *grounded* in these traces; Compose‑CAL itself remains purely generative and extensional.


### C.13:2 - Problem frame & Problem

FPF presents a unified structural backbone used across disciplines. Historically, sub‑relations like *ComponentOf* or *MemberOf* were **declared** directly. This maximised usability but provided no generative guarantee that a new subtype was extensionally well‑behaved or reducible to common mereology.

Declared lists of part‑of sub‑relations **scale poorly** and **lack identity guarantees**. Engineers ask for a *single dial* (“is x part of y?”), while ontologists need a principled foundation that (a) avoids Kernel bloat and (b) proves that wholes are nothing over and above their parts. Adding yet another bespoke relation (e.g., *PortionOf*) should not entail schema surgery or ad‑hoc rules.

### C.13:3 - Forces

* **Parsimony (C‑5).** Add no core types if composition suffices; keep the constructor set minimal.
* **Minimal Kernel (P‑1).** Generativity must live in a calculus pattern, not in Kernel axioms and postulates.
* **Cognitive asymmetry.** Everyday users want “one part‑of query”; specialists accept complexity backstage.
* **Trans‑disciplinary unification.** Every pattern that needs mereology should reuse one *generative* basis.
* **Green‑field strictness.** With no legacy to break, we can require grounding for new structural edges.

### C.13:4 - Solution

#### C.13:4.1 - Solution sketch

**Compose‑CAL SHALL provide Γₘ with three and only three constructors:**
1. **`Γₘ.sum(parts:Set[U.Entity])`** — returns a whole *W* such that each *p* in *parts* stands in **KernelPartOf(p, W)**.
2. **`Γₘ.set(elems:Set[U.Entity])`** — returns a **collection** *C*; each *e* in *elems* stands in a calculus‑internal **mero:KernelPartOf(e, C)** under **member‑as‑part** semantics (publication alias: typically **`ut:MemberOf`**). **Counts/order** (e.g., parallel/serial factors) are **not carried here**; they live in method/time families adjacent to structure.  *Note:* although `mero:KernelPartOf` is transitive in the calculus, the **published** `MemberOf` alias remains **non‑transitive** by design (see A.14 guards). 
3. **`Γₘ.slice(entity:U.Entity, facet:U.Facet)`** — returns an **aspect** *S* such that **mero:KernelPartOf(S, entity)** and *S* carries the declared **facet**. Temporal facets are excluded here.
   
+**Note.** The calculus names an internal backbone **`mero:KernelPartOf`**; the Kernel’s public `ut:PartOf`/**A.14** catalogue remain unchanged. Publish only via Working‑Model aliases (CT2R‑LOG).

+The calculus emits a **trace** for every construction; Structural aliases **MUST** be *grounded by* exactly one such trace.

**Non‑goals (clarifications).**
* No extra constructors for “parallelism” or “time slices”; parallelism is modelled via **set** (with order handled in `Γ_method`), and temporal parts live in the appropriate temporal/system calculus. This preserves parsimony.
* Compose‑CAL does not define user‑visible relation names; those belong to the alias layer.

#### C.13:4.2 - Normative Standard (high‑level)

* **C13‑N1.** *Extensional identity.* Two Γₘ results are identical iff they have the same parts under the same constructor and facet conditions.
* **C13-N2.** *Structural grounding stance.* Every **structural** edge **MUST** reference **exactly one** Γₘ trace as its grounding witness **and SHALL declare `validationMode = axiomatic`** (see B.3.5 / E.14). **Structural edges MUST NOT** be published in `postulate` or `inferential` stances.
* **C13‑N3.** *Algebraic laws.* `Γₘ.sum` and `Γₘ.set` are **commutative** and **idempotent** over their inputs; `Γₘ.slice` composes only by facet‑compatible refinement.
* **C13‑N4.** *Acyclicity & antisymmetry.* Structural part‑of induced by Γₘ is transitive, antisymmetric, and acyclic at the level of entities. *(Formal axioms appear later in this pattern.)*
* **C13‑N5.** *Separation of concerns.* Γₘ provides constructions and traces; naming, aliasing and human‑level relation taxonomies are defined outside Compose‑CAL (see B.3.5 for the CT2R‑LOG handshake).
* **C13‑N6.** *Member vs component.* `Γₘ.set` yields **collections** whose Working‑Model alias is **MemberOf**; authors **SHALL NOT** infer **ComponentOf** from **MemberOf** without a separate `Γₘ.sum` narrative.
* **C13‑N7.** *Domain guard.* Do **not** apply Compose‑CAL to roles, methods, or works (see A.12/A.15): these are outside mereology.

#### C.13:4.3 - Scope, applicability, terms & notation

+Use Compose-CAL whenever a claim concerns **structural containment** of entities (assemblies, collections, aspects). Compose-CAL is *not* used for epistemic relations between knowledge artefacts; those are **epistemic** relations and may be justified by **Logical/Mapping** and/or **Empirical Validation** with an explicit `validationMode ∈ {inferential, postulate}`. Compose-CAL is neutral with respect to domain (mechanical, biological, software, etc.).

* **Γₘ** — the mereological construction operator of this calculus.
* **trace** — a minimal, inspectable witness that a constructor was applied to given inputs to yield a whole (or aspect).
* **structural part‑of** — the structural relation induced by Γₘ; user‑facing aliases (e.g., *ComponentOf*, *MemberOf*) are separate patterns that **must** point back to traces.
  
 **Alias readiness.** Typical CT2R mappings:  
* **ComponentOf** ⇢ `sum` narrative;  
* **MemberOf** ⇢ `set` narrative;  
* **AspectOf** ⇢ `slice` narrative;  
* **PortionOf** ⇢ `slice(entity, facet="material/spatial‑region")` **plus** metrical semantics (A.14);  
* **ConstituentOf** (logical/content) ⇢ `sum` narrative over conceptual parts. *(Material mixtures are **not** `ConstituentOf`; use `PortionOf` or `ComponentOf` per A.14.)*
 
### C.13:5 - Archetypal Grounding *(System / Episteme duo)*

> **Tell–Show–Show.** Compose‑CAL is a thinking‑level calculus for building structural wholes from parts. We *show* it twice—first on a **System** (structural) and then on an **Episteme** case (where constructive grounding is *not* the primary mode).

#### C.13:5.1 - **System** (structural; constructive grounding)

**Story.** A **Skid** is assembled from its **Pump**, **Motor**, **Baseframe**, and **Manifold**.

**Constructive grounding (Γ\_m).**
Narrate a *sum* of parts: “Skid = sum{Pump, Motor, Baseframe, Manifold}.” This uses **`Γ_m.sum`** to obtain a whole whose parts stand in **KernelPartOf**; the resulting Working‑Model relation engineers publish is **`ut:ComponentOf`** on each edge from part to whole. The mapping “*sum → ComponentOf*” reflects the intended aliasing between constructive traces and human‑facing mereology.

**Facets and collections.** 
Need the **inspection surface**? Narrate **`Γₘ.slice(Skid, "spatial")`** and publish **`ut:AspectOf`**. Need a group of **Transfer interactions**? Narrate **`Γₘ.set{…}`** and publish **`ut:MemberOf`**—this is a **collection-as-whole**, not a sub‑assembly; no component identity is implied without a separate **`Γₘ.sum`** narrative.

**Plane separation.**
Assembly **order** and **time** are *not* encoded here: parallel lines and schedules live in method/time families and are described adjacent to, not inside, the part‑tree.

#### C.13:5.2 - **Episteme** (knowledge‑bearing; non‑constructive first)

**Story.** A **Mass‑Flow Representation** is used to stand for a measured flow in a plant dataset.

**Grounding choice.** 
Here the Working‑Model relation (e.g., **RepresentationOf**) is **epistemic**. Authors typically justify it by *inferential* or *postulate* stances (argument or calibration cues), not by a mereological construction; constructive traces remain optional. This preserves the firewall between structure and knowledge claims while keeping a clear path to stronger assurance if the team later reframes part of the representation structurally (e.g., sets of interactions as a **`Γ_m.set`** for a flow bundle).

#### C.13:5.3 - Scope justification

* **Universality.** The trio **sum / set / slice** appears across mechanical assemblies, biological complexes, and organizational artifacts; aliasing to **ComponentOf / MemberOf / AspectOf** provides a stable Working‑Model surface for those domains.
* **Parsimony.** No “parallel” or “temporal slice” constructor is added; time slices belong in the temporal calculus, and parallelism is modelled as a **set** plus method metadata.

### C.13:6 - Bias‑Annotation *(cognitive anti‑patterns and counter‑moves)*

| Bias (name)                       | Symptom                                                                                                         | Counter‑move (conceptual)                                                                                                    | Where to look                               |
| --------------------------------- | --------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------- |
| **Constructor‑centrism**          | Treating the trace as “the real thing” and the Working‑Model edge (e.g., **ComponentOf**) as merely decorative. | Re‑affirm **Working‑Model first** (publish in `ut:*Of`), then attach constructive narratives only when assurance demands it. | B.3.5 (Working‑Model relations & grounding) |
| **Collection ↔ Composition swap** | Using **MemberOf** to stand in for **PartOf**, then inferring structural identity.                              | Keep **set** outputs as *collections*; use **sum** for wholes with extensional identity.                                     | A.14 (Advanced Mereology)                   |
| **Temporal leakage**              | Smuggling sequence/phase into part‑trees.                                                                       | Route order/time to their planes; **no** “temporal slice” constructor in Compose‑CAL.                                        | B.1.\* (Γ\_method / Γ\_time)                |
| **Over‑slicing**                  | Multiplying aspects until identity becomes opaque.                                                              | Declare the **facet** explicitly; stop when aspects no longer aid recognition of the same whole.                             | A.14 (Aspect/Phase distinction)             |
| **Feature creep**                 | Proposing a new constructor for a special case.                                                                 | Reduce to **sum / set / slice**; if reduction fails across ≥ 3 domains, reconsider the modelling plane before adding power.  | C‑5 (Parsimony)                             |
| **Axiomatic inflation**           | Demanding constructive traces for epistemic links by default.                                                   | Use *inferential* / *postulate* where appropriate; reserve *axiomatic* for structural identity.                              | B.3.5 (validation modes)                    |


### C.13:7 - Conformance Checklist *(normative, calculus‑level)*

The following regulate **how to think and write** when invoking Compose‑CAL. They are notation‑agnostic and conceptual.

| ID                                         | Requirement                                                                                                                                                                                    | Purpose                                                                 |
| ------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------- |
| **CC‑C13‑1 (Three moves only).**           | Authors **SHALL** construct structural narratives using exactly **`Γ_m.sum`**, **`Γ_m.set`**, and **`Γ_m.slice`**. No additional constructors are introduced in this calculus.                 | Preserve **parsimony** and cross‑domain comparability.                  |
| **CC‑C13‑2 (Kernel invariants).**          | Constructive narratives **SHALL** respect **KernelPartOf** invariants (transitivity, antisymmetry, acyclicity) and yield extensional identity for wholes.                                      | Keep structural identity intelligible and replayable.                   |
| **CC‑C13‑3 (Algebraic laws).**        | `sum`/`set` are commutative & idempotent; `slice` composes only with facet‑compatible refinement. | Make traces **peer‑reconstructible** and easy to replay in thought. |
| **CC‑C13‑4 (No order/time in mereology).** | Authors **SHALL NOT** encode execution order, parallelism, or temporal coverage via constructors; such concerns belong to method/time planes and are stated adjacent to structure.             | Maintain the plane firewall.                                            |
| **CC‑C13‑5 (Narratability).**              | Each constructive trace **SHALL** be narratable in plain language **without introducing new primitives**.                                                                                      | Enforce human‑first clarity; uphold C‑5.                                |
| **CC‑C13‑6 (Alias alignment).**            | When Publishing Working‑Model relations for structural content, authors **SHOULD** align “sum→ComponentOf”, “set→MemberOf (or pattern‑specific)”, “slice→AspectOf” in their explanatory prose. | Keep alias semantics stable across Contexts.                               |
| **CC-C13-7 (CT2R-LOG handshake).**     | For every **structural** edge on the Working-Model, authors **SHALL** set `validationMode=axiomatic` and point **`tv:groundedBy`** to exactly **one** Γₘ trace (`sum|set|slice`). *Legacy “Tier-1” wording deprecated; express formality via **F** per C.2.3.* | Clean bridge to the Working-Model alias layer; decouples relation kind from legacy “tiers”. |
| **CC‑C13‑8 (Member ≠ Component).**         | A **set** output remains a *collection*; authors **SHALL NOT** infer **ComponentOf** from **MemberOf**. When an integrated assembly is intended, provide a separate **`Γ_m.sum`** narrative.   | Prevent membership→component conflation.                                 |
| **CC‑C13‑9 (Facet explicitness).**         | **Slice** narratives **SHALL** name the **facet** used; temporal facets are excluded (handled elsewhere).                                                                                      | Keep aspects precise and non‑temporal.                                  |
| **CC‑C13‑10 (No roles in mereology).** | Do not apply Γₘ to `U.Role`, `U.Method`, or `U.Work`; these are outside mereology (A.12/A.15). | Preserve the plane firewall. |
| **CC‑C13‑11 (Member non‑transitive).** | When publishing `MemberOf`, do not rely on transitive closure across collection‑of‑collections; surface semantics remain non‑transitive per A.14. | Prevent Member→Component drift. |

> **Author’s note.** Compose‑CAL is a calculus for **constructive** reasoning about structure. Publishing remains in the **Working‑Model** layer (see B.3.5); constructive narratives are attached when the team seeks stronger assurance, never as a substitute for clear human‑facing relations.

### C.13:8 - Consequences

**Benefits**

 * **Extensional clarity.** Every structural claim is reconstructed from `Γ_m.sum | Γ_m.set | Γ_m.slice`: **sum** establishes component‑assembly identity; **set** establishes collection identity; **slice** yields aspects as parts—without expanding the Kernel.
* **Human–first publication, formal–on‑demand.** Teams keep publishing **Working‑Model** relations (e.g., `ut:ComponentOf`), while **assurance** is attached as needed via a constructive grounding narrative and `tv:groundedBy` (see B.3.5).
* **Separation of planes preserved.** Order/parallelism and temporal coverage remain in `Γ_method` / `Γ_time`; structure is never overloaded to carry them, avoiding recurrent category errors.
* **Uniformity across domains.** The same triad models mechanical assemblies, socio‑technical memberships, and informational wholes without domain‑specific constructors or ad‑hoc exceptions.
* **Didactic economy.** Authors learn one compact calculus; reviewers gain a predictable place to look for constructive justification when `validationMode = axiomatic` (B.3.5 alignment).
* **Compositional reuse.** Traces are reusable fragments of reasoning; complex wholes are narratable as sums of sub‑traces, with sets for concurrency and slices for aspect selection.

**Trade‑offs / Mitigations**

* **Discipline cost at higher assurance.** Writing a concise grounding narrative for axiomatic claims takes effort. *Mitigation:* reuse the micro‑templates in this pattern’s Grounding section and keep narratives notation‑free.
* **Over‑use risk.** Temptation to treat collections as integrated assemblies. *Mitigation:* keep **MemberOf** distinct from **ComponentOf**; both `set` and `sum` yield wholes, but only **`sum`** establishes **component** structure and assembly identity.
* **Temporal leakage risk.** Authors may try to smuggle time into structure via “temporal slices.” *Mitigation:* use `Γ_time` for temporal statements and `slice` only for intensional aspects, not for time windows.

> **One‑line takeaway.** Compose‑CAL gives a minimal, universal *how‑it‑was‑built* story for any structural edge, without disturbing the human‑first publication surface defined in B.3.5.


### C.13:9 - Rationale (informative)

**Why exactly three moves?**
`sum`, `set`, and `slice` are jointly sufficient and minimally overlapping:

* **`sum`** creates an **integrated whole** from parts and thereby establishes **component** structure (assembly identity).
* **`set`** creates a **collection‑as‑whole**; members are **parts of the collection** under member‑as‑part semantics, but **no component integration** is implied.
* **`slice`** returns an **aspect as part** of its bearer (facet‑constrained, e.g., spatial/material); temporal facets are excluded here.

All three moves create new entities; **sum** is the only move that establishes **component** identity. Neither `set` nor `slice` changes the identity of their inputs, and `set` never upgrades membership to component status. Temporal coverage and workflow order are handled in their own planes.

This separation mirrors long‑standing distinctions between composition, collection, and aspect, while enforcing **parsimony**: no additional constructors are introduced into the Kernel (C‑5). The calculus remains **notation‑agnostic**: its meanings are given in prose and mathematics; any diagrams are illustrative only, in line with the Notational‑Independence guard‑rail (E.5).

**Why constructive grounding lives outside the publication surface.**
FPF privileges **Working‑Model** relations as the canonical form for communication and design. Compose‑CAL supplies the **constructive shoulder** of the **Assurance Layer**: when authors choose `validationMode = axiomatic`, they narrate the whole as a `sum` of parts (with optional `set` and `slice` scaffolding) and point to that narrative via `tv:groundedBy`. This keeps the text readable while preserving a path to stronger assurance (B.3 family, Authoring Template).

**Why order/time are out of scope.**
Correctness‑by‑sequence and temporal coverage are orthogonal to **parthood**. Encoding them as parts breeds contradictions (e.g., “phase‑as‑component”). Compose‑CAL deliberately refuses any “serial/parallel/temporal constructor,” delegating such concerns to `Γ_method` and `Γ_time` and aligning with B.1’s flavour separation.


### C.13:10 - Relations

**Builds on**

* **A.14 Advanced Mereology.** Uses its structural catalogue (Component/Portion/Aspect vs Member) as the *target* of constructive narratives; never collapses Member into Part.
* **E.5 Guard‑Rails (Notational Independence).** Meanings are given in prose; diagrams are illustrative only.  
* **E.5 Guard‑Rails (Unidirectional Dependency).** Compose‑CAL depends **downward** only; it never imports alias layers or higher planes.
* **E.8 Authoring Conventions.** Conforms to the canonical pattern template (Grounding section for architectural patterns; CC placement).

**Coordinates with**
* **B.3.5 CT2R‑LOG.** `tv:groundedBy` refers (conceptually) to Compose‑CAL traces when `validationMode = axiomatic`; **Working‑Model** relations remain the publication interface.
* **B.1 flavours.** Keeps order (`Γ_method`) and time (`Γ_time`) outside structure; may co‑appear in narratives when relevant but never as constructors.
* **Kind-CAL / Lang‑CHR.** Provide the Mapping shoulder of assurance (labels, type alignment) that complements constructive narratives in this pattern.
* **KD‑CAL.** Provides the Logical shoulder when authors justify relations inferentially instead of constructively.
* **C.16 (Measurement substrate).** Supplies quantitative hooks when a constructive narrative benefits from explicit counts/ratios (e.g., cardinalities, coverage), while keeping metrics distinct from mereology.

**Constrains**
* Any pattern that **creates** or **reasons about** structural wholes SHOULD narrate them using only `sum | set | slice`.
* Structural publication MUST NOT encode order/time; such claims belong to their dedicated flavours.
* Introducing new structural constructors requires a separate parsimony argument and is discouraged unless the triad cannot narrate the case without ambiguity.

**Provides**
* A minimal generative basis (`Γ_m.sum | Γ_m.set | Γ_m.slice`) and the corresponding reading discipline for constructive narratives.
* A stable interface with CT2R‑LOG for `tv:groundedBy` links under `validationMode = axiomatic`.

### C.13:End

## C.16 - Measurement & Metrics Characterization (MM‑CHR)

### C.16:1 - Intent (Normative)

**Name.** *Measurement & Metrics Characterization (MM‑CHR).* This is a user‑oriented name: in user‑facing narrative we may say *metrics*; in **Tech** register we speak **Characteristic / Scale / Level / Coordinate / Value / Score / Unit / ScoringMethod**; in **Formal** register we use `U.DHCMethod(Ref)` / `U.Measure` / `U.Unit` / `U.EvidenceStub`.
**Intent.** Provide a **transdisciplinary substrate for measurement** that any FPF pattern can rely on: a small, stable set of intensional constructs and relations—**`U.DHCMethodRef`**, **`U.Measure`**, **`U.Unit`**, **`U.EvidenceStub`**—disciplined by **CSLC** (*Characteristic / Scale / Level / Coordinate*) so that every recorded value is **interpretable**, and any claim of “comparability” is **auditable** (physics lab time‑of‑flight, figure‑skating judging, architectural modularity, etc.). **C.16** does **not** re‑define **Characteristic** (A.17) nor the CSLC kernel Standard (A.18); instead, it **exports** the measurement substrate that *binds* an FPF pattern’s measurable notions to **one Characteristic and one Scale** and frames a **conceptual link to evidence**. This characterization is **notation‑neutral**, **tool‑agnostic**, and **open‑ended** (no “lifecycle” narrative; evolution proceeds via **RSG** moves with checklists).

**One‑minute mental model (didactic; non‑normative).**
* **Template** (`U.DHCMethod`) says what a value *means*: the **Characteristic**, **Scale** (and **Unit** when applicable), plus **polarity** and applicability.
* **Reading** (`U.Measure`) says what was claimed about a **subject**: a value on that Scale, with a **time stance** and (when required) an **EvidenceStub**.
* **Direct comparability** is conservative: *same template*; everything else requires a **named, cited** transformation or equivalence owner.

**Non‑ownership boundary (single‑writer).** C.16 is **not** the semantic owner for (i) characterization mechanisms (e.g., normalization / indicatorization / scoring / comparison / selection), (ii) any normalization/equivalence notions (method tokens, “invariant value” notions, equivalence relations), (iii) contract routing policies (comparability modes, legality gates), or (iv) suite protocol obligations. Those belong to their single owners (e.g., the CN/CG contract surfaces and the CHR mechanism owner patterns). C.16 may **cite** such owners when motivating evidence or interpretability, but MUST NOT introduce or restate their terminology or laws.

**Outcomes.**
(1) A uniform way for FPF patterns to *declare* what is measured and *read* what has been measured; (2) explicit **Characteristic anchoring** and **Scale typing** per CSLC; (3) principled **comparability** and **polarity** (declared at the template level); (4) **traceability** via conceptual evidence stubs; (5) seamless alignment with cross‑domain quantity notions (ISO 80000, ISO/IEC 25024, QUDT, SOSA/SSN, Verspoor) through Unification rows (Part F). 

### C.16:2 - Scope & Status (Normative)

**Scope.** **C.16** specifies the **measurement substrate** for FPF patterns: the roles of `U.DHCMethodRef`, `U.Measure`, `U.Unit`, `U.EvidenceStub`; their **CSLC discipline** (by reference to A.17/A.18); and **evidence linkage semantics** at the level of *conceptual conditions*. It defines **direct interpretability** and **direct comparability** (same template), and it equips other patterns to state—and audit—stronger comparability claims by **citing** their single owners. It **exports** these constructs for all FPF patterns (KD‑CAL, Arch‑CAL, etc.) without prescribing domain formulae, procedures, or any CHR mechanism semantics.

**Status.** **Normative** C.16 **depends on** A.17 (canonical **Characteristic**) and A.18 (minimal **CSLC** in Kernel). Where C.16 cites external CG‑frames, the stance is through **Part F** rows and **Bridges** (with CL and loss notes), not by vocabulary import. 

**Out of scope.** No computational recipes, no workflow prescriptions, no governance/process guidance. No definitions of normalization/indicatorization/scoring/comparison/selection mechanisms, no comparability routing policies, and no legality gate specifications. C.16 concerns **objects of thought** (intensions) and their **validity conditions** for measurement claims, not records or tooling. (Implementation guidance, if any, belongs outside Part C.)


### C.16:3 - Problem & Context (Informative)

#### C.16:3.1 - The problem C.16 solves

Across FPF patterns, people say “score”, “metric”, “rating”, “property”. Without a shared substrate, numbers drift: *42 of what? on which scale? comparable to whom?* C.16 eliminates drift by requiring every metric notion to **bind** to **one** Characteristic and **one** Scale, and by **separating** intensional anchors from descriptions and ScoringMethods. The result is **portable meaning**: a measure is always readable as a **Coordinate on a declared Scale of a named Characteristic**, with a principled path to evidence. 

#### C.16:3.2 - Context and prior art

* **Kernel canon.** A.17 makes **Characteristic** the sole canonical anchor for measurability; A.18 fixes **CSLC** as the minimal sufficiency for interpretability. C.16 relies on both.
* **Cross‑domain alignment.** The MM‑CHR family already maps FPF U.Types to **ISO 80000‑1 (Quantity)**, **ISO/IEC 25024 (Data‑quality Characteristic)**, **QUDT (QuantityKind/QuantityValue)**, **W3C SOSA/SSN (Observable/Observed/Result)**, and domain “feature/metric” usage (Verspoor, TF Metrics). C.16 uses these rows **as Bridges** (Part F), preserving local senses and documenting losses.  
* **Open‑ended evolution.** FPF replaces “lifecycle” with **Role‑State Graph (RSG)** style state checklists (A.2.5): movement is along **certified states** with checklists; re‑entry is allowed when distinctions change. C.16 uses this device only to frame **readiness** and **revision** of metric notions conceptually (no processes implied).


### C.16:4 - Forces (Informative)

**F1 — Interpretability first.** A value detached from its Characteristic/Scale is meaningless; CSLC supplies minimum context.
**F2 — Transdisciplinarity.** Physics, architecture, curation, sport judging—*one* substrate must cover all while respecting scale types and polarity.
**F3 — Intension vs description.** Confusing the **Characteristic** (intensional object) with its rubric or exemplar text (descriptions) corrupts claims; C.16 keeps them distinct.
**F4 — Comparability without coercion.** Ordinal ≠ interval; ratio admits unit change, ordinal does not; polarity matters for “better/worse”. C.16 encodes these **as conceptual constraints**, not formulas.
**F5 — Evidence sufficiency.** A measure should be *checkable in principle*; evidence is a **conceptual link** (not storage advice).
**F6 — Lexical discipline.** One canon in normative register; narrative labels are didactic only (Part E). C.16 reuses E.10’s **register mapping**.


### C.16:5 - Solution Outline (Normative)

**S1 — Exported objects.** C.16 **exports** four intensional constructs to be used by any FPF pattern:

1. **`U.DHCMethod`** — a *measurement template* (a Definition) that binds **one `U.Characteristic`** to **one Scale form**, with declared **polarity** and (optionally) a **citation point** to the semantic owner of any non‑trivial equivalence/comparability claim that is relied upon elsewhere (e.g., a Bridge or a declared transformation owner). **References** to this template use `U.DHCMethodRef`. It is an *intensional specification*, not a record layout.
2. **`U.Measure`** — an *assertion* that a **subject** occupies a **Coordinate** (or **Level**, if discrete) on that Scale; the measure **references** its template and carries a **conceptual pointer to evidence** (`U.EvidenceStub`).
3. **`U.Unit`** — the *unit kind* associated with the Scale where applicable (physical quantities, normalized “points”, “stars”, “%”); unit coherence is part of comparability conditions.
4. **`U.EvidenceStub`** — a *conceptual locator* of grounds for the asserted value (type, identifier, brief summary, optional integrity notion); sufficiency criteria are **conceptual** (see §9, later).

**S2 — Comparability stance (boundary‑aware).** C.16 states only the **direct** comparability condition for measurement claims: *same template* (hence, same Characteristic + Scale + Unit semantics by reference to A.17/A.18). Any comparability claim that relies on transformations (normalization, scoring, aggregation, cross‑context transport, bridge losses, legality gating) MUST cite its single semantic owner (CN/CG surfaces and/or the relevant mechanism cards). C.16 does not define those transformations or their laws. (Details: §7–§8 in later parts.)

**S3 — Evidence stance.** A measure that, by its template, **requires** evidence, is **inadmissible** without a meaningful `U.EvidenceStub`. C.16 defines **what it means conceptually** for evidence to “connect” the subject, the Characteristic, and its symbolic description; mechanisms are out of scope. (Details: §9 in later parts.)

**S4 — RSG framing (open‑endedness).** Readiness, calibration, and revision of metric notions are expressed as **RSG node moves with checklists** (e.g., “characteristic anchored”, “Scale typed”, “Unit coherent”, “ScoringMethod declared”), allowing **re‑entry** when distinctions change; there is no terminal “lifecycle”. (Details: §10, later.)


#### C.16:5.1 - Lexical Discipline & Registers (Normative)

**L1 — Canon.** Use **Characteristic / Scale / Level / Coordinate / Value / Score / Unit / ScoringMethod** in **Tech** register; their `U.*` counterparts in **Formal**. Narrative labels (e.g., *axis*, *points*, *stars*) are **didactic only**, and are mapped at first mention to the Tech canon (E.10). 
**L1‑bis — “metric”.** The noun *metric* is **not** a Tech‑register canonical token for measurables; use **Characteristic / Scale / Coordinate / Score / ScoringMethod**. It **may** appear in the pattern title and in the Formal names `U.DHCMethodRef` / `U.Measure`. Do not use *metric* as a synonym for **Characteristic** or **Score** in normative prose.
**L2 — Intension vs Description.** Keep **intensional objects** (`U.DHCMethodRef`, `U.Characteristic`) distinct from **descriptions** (rubrics, exemplars) and from **claims** (`U.Measure`). No collapsing of names across these layers.
**L3 — No synonym sprawl.** In normative clauses do **not** substitute *dimension/axis/property/feature* for **Characteristic**; A.17 governs canonicalization. (C.16 inherits A.17’s rename policy.)
**L4 — Bridge‑only unification.** Cross‑vocabulary sameness appears only via **F.9 Bridges** with **CL** and **loss notes**; C.16’s lexicon is the *source* side for measurement rows.
**L5 — Plain‑register shorthand.** In **Plain** register *metric* MAY be used as shorthand for “template + readings”, but on first use it MUST be mapped to **`U.DHCMethod` (template)** and **`U.Measure` (reading)**, and to the Tech canon terms that matter for meaning.
**L6 — No CHR‑mechanism terminology ownership.** Tokens and laws owned by characterization mechanisms (e.g., normalization method tokens, invariant‑value notions, indicatorization policy terms) MUST be introduced only by their owner patterns. C.16 may mention them only as **cited** external terms, never as locally defined canon.

#### C.16:5.2 - Relations (pointers; details later)

**To A.17 / A.18.** C.16 *uses* A.17’s canonical **Characteristic** and A.18’s **CSLC sufficiency**; it neither re‑states nor weakens them.
**To Part F.** C.16 is the **exporting pattern** behind measurement rows in UTS/Bridges (e.g., **result‑value** ↔ SOSA `Result`, ISO `QuantityValue`).
**To Arch‑CAL.** Architectural qualities (*Coupling, Cohesion, Evolvability*) become **Characteristics** measured via C.16 templates; architectural dynamics read as trajectories in **CharacteristicSpace** (A.17 context).

#### C.16:5.3 - Normative Core Model (types & Standards)

> **Position.** MM‑CHR does **not** redefine kernel terms; it **binds** them to an FPF‑level Standard that every metric must satisfy. Canonical vocabulary and CSLC duties are inherited from **A.17**/**A.18** and referenced here without duplication.
> 
> **Source of Truth** A.17/A.18 are the sole sources of truth for Canon and CSLC; C.16 **adopts by reference** and **forbids restatements** of their definitions. C.16 only **exports** `U.*` constructs, comparability stance, evidence semantics, and RSG touch‑points.
>
> **CHR boundary reminder.** Any notion that belongs to characterization mechanisms (normalization, indicatorization, scoring, aggregation, comparison, selection) appears in C.16 only as a **pointer** to its semantic owner. C.16 MUST NOT become a shadow owner for any such terminology or laws.

##### C.16:5.3.1 - `U.DHCMethod` — the metric definition (normative)

##### C.16:5.3.1 - `U.DHCMethod` — the measurement template (normative)

**Role.** An intensional **Standard** that fixes *what is measured* and *how values must be read*—without producing any values itself. It is a *Definition*, not a Measure. **References** to this template use `U.DHCMethodRef`. *(Didactic: think “the meaning contract for a reading”.)*

**R‑MT‑1 (CSLC anchor).** A DHCMethod **SHALL** bind to **exactly one** `U.Characteristic` and **exactly one** **Scale‑form** admissible for that Characteristic (cf. A.18). Level is **optional** (used when the scale is enumerated); otherwise values are given directly as Coordinates.

**R‑MT‑2 (Unit).** If the scale carries units (interval/ratio), the template **SHALL** designate a **Unit** of presentation. For ordinal/nominal scales, unit may be absent or a nominal label (e.g., “stars”). (Old MM‑CHR Annex A already listed these structural elements; here we fix the conceptual obligation. )

**R‑MT‑3 (Polarity).** For any ordered scale, the template **SHALL** declare polarity (*higher‑is‑better / lower‑is‑better / target‑is‑best*), as a semantic reading aid and as an input to consuming patterns. If polarity is *target‑is‑best*, the template **SHALL** name the target value (or target set) and MAY cite (by reference) the semantic owner of any tolerance/fall‑off convention used by downstream mechanisms or methods. C.16 does **not** standardize tolerance/fall‑off semantics; those belong to the semantic owner of the relevant scoring/normalization/selection mechanism or method description.

**R‑MT‑4 (Applicability).** A template **SHALL** state the **applicability frame** (what kinds of subjects it meaningfully applies to) in conceptual terms; this is a property of the definition, not of any measure.

**R‑MT‑5 (Intension vs description).** The template is an **intensional object**. Any rubric, checklist, or prose that explains it is a **Description**; they are related but not identical (E.10 discipline).

**R‑MT‑6 (Cardinality hint).** A Template **MAY** declare its intended **cardinality semantics** for a subject within a **time stance** (e.g., *latest‑only*, *at‑most‑one‑per‑day*, *time series*).
Where declared, claims outside that semantics are **inadmissible conceptually** (they must be reframed or versioned). *Purpose:* prevent silent duplicates and mixed regimes without imposing storage logic.

**R‑MT‑7 (MAY).** `UncertaintyPolicy` — optional conceptual guidance on how uncertainty is expressed/read (e.g., band/CI/quantile), without prescribing methods/tools.
*(Informative examples: calibrated probability with a confidence band; a prediction interval; a set‑valued reading such as a prediction set.)*
    

##### C.16:5.3.2 - `U.Measure` — the recorded reading (normative)

**Role.** A **claim** that a subject occupies a **Coordinate** (or named **Level**) on the template’s scale, backed by a minimal pointer to its grounds.

**R‑ME‑1 (Template binding).** Every Measure **SHALL** reference exactly one DHCMethodRef; its **Value/Coordinate** must be **valid** for that template’s scale (type, range, category).

**R‑ME‑2 (Subject).** A Measure **SHALL** identify its **subject‑of‑measurement** (the bearer) unambiguously in the same Context of meaning as the template’s applicability frame.

**R‑ME‑3 (Evidence stub).** Where the template requires it, a Measure **SHALL** include an **EvidenceStub**—a conceptual pointer sufficient to support independent reasoning about the claim’s origin. (The old spec framed this as “traceability/provenance”; we keep only the **conceptual** role here. )

**R‑ME‑4 (Time stance).** A Measure **SHALL** carry a **time stance** (e.g., “as‑observed at T”, or “as‑aggregated over W”), expressed conceptually; it disambiguates the reading’s intended window without prescribing formats.

**R‑ME‑5 (Entity vs relation).** If the Characteristic is **relational**, the subject is a **tuple** (pair, k‑tuple); the wording of the claim reflects that arity and the template’s relation topology (cf. A.17).

**R‑ME‑6 (MAY).** `UncertaintyStub` — optional conceptual pointer to the adopted uncertainty estimation for this Measure, **if** required by the template.

> *Informative anchor.* The old Annex B example “Article Completeness” illustrates the split template/measure/evidence; **C.16** keeps the split but forbids storage‑level talk.

##### C.16:5.3.3 - `U.Unit` — semantics of quantities (normative)

**Role.** A conceptual marker of **quantity kind** and admissible **conversions** within that kind; not every scale requires it.

**R‑UN‑1 (Quantity kind).** Where units apply, the template **SHALL** indicate the **quantity kind** (e.g., Time, Length, Dimensionless‑Score). Units are meaningful only **within** one kind.

**R‑UN‑2 (Convertibility).** Comparisons across different units are permitted **iff** they are **convertible** by kind‑preserving transformation (ratio/interval scales); for ordinal/nominal scales, no numeric conversions exist. (Old Annex A listed conversion hints; here we assert the conceptual boundary. )

**R‑UN‑3 (Canonical labels).** `%` denotes “fraction×100”; “points” denotes dimensionless magnitudes used for scores; “stars” denotes discrete ordinal marks. These are **labels** of representation, not new characteristics.

**R‑UN‑4 (Quantity‑kind bridge).** A Template on an interval/ratio Scale **SHOULD** name the underlying **quantity kind** (e.g., ISO 80000/QUDT category) to enable safe external bridges. This does **not** import external vocabularies; it declares an alignment point.

##### C.16:5.3.4 - `U.EvidenceStub` — pointer to grounds (normative)

**Role.** A compact **tie** from a Measure to the grounds sufficient for **reasoned audit** (not a repository prescription).

**R‑EV‑1 (Minimal sufficiency).** An EvidenceStub **SHALL** carry, at minimum, a **type‑of‑ground** and an **identifier** sufficient to retrieve or reconstruct the grounds in the appropriate Context of meaning.

**R‑EV‑2 (Compositionality).** Multiple grounds may be **composed** as a finite set; composition is **commutative/associative/idempotent** at the level of stubs, enabling conceptual merge of corroborations.

**R‑EV‑3 (Soundness axiom).** A Measure is **MM‑CHR‑admissible** only if at least one **auditable chain of grounds** can be stated from the bearer to the Characteristic via an appropriate Description (Object–Concept–Symbol triangle in the episteme). *(Note:* mechanism‑level admissibility gates (e.g., legality/evidence thresholds in CG‑frames or CHR mechanisms) are owned elsewhere; C.16 defines only the conceptual “has grounds” link.)
**R‑EV‑3 (Soundness axiom).** A Measure is **MM‑CHR‑admissible** only if at least one **auditable chain of grounds** can be stated that connects:
`bearer (subject) → grounds → Characteristic → Coordinate/Level on the declared Scale`,
in the appropriate Context of meaning. *(Informative: this is the object–concept–symbol triangle.)*  
*(Boundary note:* mechanism‑level admissibility gates (e.g., legality/evidence thresholds in CG‑frames or CHR mechanisms) are owned elsewhere; C.16 defines only the conceptual “has grounds” link.)

#### C.16:5.4 - Polarity, Comparability, and ScoringMethods (normative)

> **Notation.** To avoid clashes with the kernel’s global aggregation symbol, this FPF pattern denotes a **ScoringMethod** (score‑level mapping) by **𝒢** (calligraphic 𝒢).

**R‑POL‑1 (Declared polarity).** Every ordered scale **SHALL** declare polarity at the **template**. Any disclosed scoring method **𝒢** that issues a **Score** for that template **SHALL** be order‑compatible with the declared polarity semantics (monotone for ↑/↓ polarity; target‑aware only when the target semantics is explicitly declared and cited where it depends on external conventions).

**R‑CMP‑1 (Direct comparability).** Two readings are **directly comparable** only when they reference the **same `U.DHCMethodRef`** (hence share Characteristic + Scale + Unit semantics by reference to A.17/A.18). “Same‑template” is the only comparability relation defined by C.16.
*(Clarification:* sharing a name, unit label, or scale type across distinct templates is **not** sufficient for comparability in MM‑CHR; cross‑template comparability must be established via **R‑CMP‑2**.)*

**R‑CMP‑2 (Transformed comparability is cited, not defined).** If a comparison relies on any transformation or routing step (e.g., normalization, indicatorization, scoring, aggregation, cross‑context transport, bridge conversions, legality gates), that step **SHALL** be **named and cited** via its single semantic owner. C.16 does not define such transformations, their law sets, or their admissibility conditions.

**R‑G𝒢‑1 (ScoringMethod disclosure).** If a pattern issues a **Score** (a value on a score scale), its scoring method **𝒢 : Coordinate → Score** **SHALL** be identified **by reference** to its semantic owner (e.g., a method description card), and SHALL disclose:
(i) a **bounded codomain** / score range, and  
(ii) an explicit **order‑compatibility statement** (e.g., monotonicity) consistent with the template’s declared polarity.  
When reproducibility matters, the reference SHOULD be edition‑pinned (per the owner’s authoring discipline).  
C.16 does not define scoring methods; it only requires that a score be interpretable as a reading on a declared scale.

**R‑G𝒢‑2 (Ordinal respect).** For ordinal inputs, any cited scoring method must be **order‑preserving**; interval assumptions **MUST NOT** be smuggled in. *(Normative source for scale legality remains A.18; C.16 only enforces “no silent semantics upgrade”.)*


#### C.16:5.5 - Entity vs Relation bindings (normative clarifications)

**R‑ER‑1 (Arity preservation).** If the Characteristic is `U.EntityCharacteristic`, the subject is **one** bearer; if `U.RelationCharacteristic`, the subject is a **k‑tuple** (k ≥ 2). The Measure’s claim text **SHALL** reflect this arity.

**R‑ER‑2 (Relation scale).** Relation‑valued scales **SHALL** fix their symmetry/antisymmetry and directionality (e.g., distance symmetric; influence directional), at the **template** level.

**R‑ER‑3 (Bridge to CG‑frames).** In architectural CG‑frames, **Coupling/Cohesion** are Characteristics over **modules** (structure) or **roles** (function). Their measures are relational (**Coupling**) or unary (**Cohesion** within an element), but both live in the same MM‑CHR substrate. (Alignment hinted in the old mapping rows across contexts. )


#### C.16:5.6 - Acceptance (conceptual, RSG‑aware)

> Acceptance here is **thought‑level**. It uses the **Role‑State Graph (A.2.5)** pattern to organise mental checks—no “lifecycle” narratives.

**SCR‑C16‑A (Template sufficiency).** You can check—without invoking tooling—that the template has:
(i) a fixed **Characteristic** (A.17),  
(ii) a typed **Scale form** (A.18), and  
(iii) coherent **Unit** semantics where applicable (plus declared polarity for ordered scales).

**SCR‑C16‑B (Reading sufficiency).** For a given subject, you can check that the reading:
(i) cites the template,  
(ii) states a value valid for the Scale (Coordinate/Level),  
(iii) states a time stance,  
(iv) names **𝒢** when a Score is issued, and  
(v) provides EvidenceStub(s) where the template requires them.

**SCR‑C16‑C (Comparability).** When two readings are placed side‑by‑side, you can state in one breath whether they are **comparable as‑is** or only **after 𝒢**, and **why**.

**SCR‑C16‑D (Evidence adequacy).** For any required EvidenceStub, you can sketch at least one **auditable chain of grounds** from the subject to the Characteristic via a Description in the right Context.


#### C.16:5.7 Cross‑references & anchors

* **A.17 (CHR‑NORM).** Canonical **Characteristic** and Entity/Relation split; lexical rules and alias sunset.
* **A.18 (CSLC‑KERNEL).** One Characteristic + one Scale per template; Level optional; operation guard by scale type.
* **Annex C (old MM‑CHR).** Cross‑domain alignment hints for Characteristics/Observations/Quantities across ISO 80000, ISO/IEC 25024, QUDT, SOSA/SSN (used here only as conceptual witnesses).

### C.16:6 - Scale‑type legality quick reference (Informative)

> **Didactic note.** This table is a memory aid for engineers and managers. It does **not** introduce new legality rules. Normative legality of operations by scale type is owned by **A.18 (CSLC)** (and, where mechanized in CG‑frames, by the relevant legality profiles).
> If any row below conflicts with A.18, treat it as an illustrative example and follow A.18.

| Scale type   | Comparisons    | Location          | Differences        | Ratios                   | Admissible summaries                                  | Typical anti‑patterns (forbidden)                                   |
| ------------ | -------------- | ----------------- | ------------------ | ------------------------ | ----------------------------------------------------- | ------------------------------------------------------------------- |
| **Nominal**  | =, ≠           | mode, frequencies | —                  | —                        | counts, proportions                                   | averaging labels; ordering categories without a declared order      |
| **Ordinal**  | <, =, > (rank) | median, quantiles | **not meaningful** | —                        | order‑respecting summaries (median rank, percentiles) | arithmetic mean of ranks; variance on ranks; linear blends of ranks |
| **Interval** | <, =, >        | mean location     | Δ meaningful       | ratio **not** meaningful | mean, sd of **differences**, correlation              | ratio claims (“twice as hot” in °C); geometric mean                 |
| **Ratio**    | <, =, >        | mean location     | Δ meaningful       | ratios meaningful        | arithmetic/geometric means, cv, growth rates          | adding heterogeneous units; log on nonpositive values               |

**Reminders (informative; see A.18 for normative rules).**
G‑1 (Order). On ordinal, transforms should be **monotone**.
G‑2 (Differences). On interval/ratio, **Δ** is meaningful; on ordinal/nominal, it is undefined.
G‑3 (Ratios). Only ratio Scales admit **x/y** semantics; interval/ordinal/nominal do not.
G‑4 (Unit coherence). Interval/ratio arithmetic presumes compatible units (or a declared conversion).
G‑5 (Target polarity). If polarity is targeted, comparisons use distance‑from‑target semantics as declared by the relevant owner (template + cited method/mechanism).

*(These rules line up with the MM‑CHR exposition of CSLC and term discipline; A.17 fixes the lexical side.)* 

### C.16:7 - Evidence Semantics (Normative)

#### C.16:7.1 - What an Evidence Stub is (and is not)

**Definition.** `U.EvidenceStub` is a **conceptual pointer** that ties a **measure** to the **grounds** sufficient for independent checking (observations, arguments, lawful transformations). It is not the run log, not the carrier, and not the intensional characteristic itself. This keeps **intension–description–specification** distinct per E.10.D2 and the Clarity Lattice.

**Rule Σ‑1.** Whether evidence is **required** is a **property of the metric template**; if required, each `U.Measure` **SHALL** include an `U.EvidenceStub`.
**Rule Σ‑2.** Evidence composition is **commutative, associative, idempotent** at the concept level (sets/multisets of grounds); combining grounds can never *reduce* what is knowable about the measure’s warrant.
**Rule Σ‑3.** *Soundness minimum:* there exists a conceptual chain linking **bearer → Characteristic → Scale/Unit → admissible method/episteme**. (No “free‑floating numbers”.)
**Rule Σ‑4.** Any declared *agreement* construct used as evidence (e.g., dual readings, panels) **SHALL** respect the template’s scale type (per A.18) (e.g., order‑based concordance for ordinal; tolerance‑based agreement for interval/ratio).
**Note (boundary).** CG‑frame evidence thresholds (e.g., “minimal evidence” gates used by selection/scoring/comparison mechanisms) are owned elsewhere. C.16 defines only the EvidenceStub semantics that such gates may cite.
*Anchors:* MM‑CHR units/evidence notion; Strict Distinction and the separation of objects from their descriptions/specs.


### C.16:8 - Integration with RSG & Dynamics (Normative/Clarifying)

#### C.16:8.1 - RSG (Role‑State Graph) touch‑points

MM‑CHR **supplies recognisers** used in **State Checklists**. A checklist criterion **may** refer to a measure (e.g., “Cohesion ≥ T on ordinal ladder”), but the **state itself remains intensional**; the checklist is its **description**, and a **StateAssertion** is an evidence‑backed verdict over a Window. No lifecycle language is implied; RSGs are open‑ended graphs with re‑entry edges.

**Rule RSG‑M1.** When a checklist cites a measure, it **SHALL** do so by **Characteristic + Scale semantics** (and unit if applicable), not by colloquial aliases; Tech/Formal registers apply. **Rule RSG‑M2.** Thresholds in checklists **MUST** respect the scale type (no ratio talk on interval scales; no arithmetic on ordinal ladders).

#### C.16:8.2 - Dynamics & CharacteristicSpace

`U.Dynamics.stateSpace` is a **CharacteristicSpace**—a named set of Characteristics with units/topology. MM‑CHR provides the **measurement side** of that space; patterns specify the **transition law**. Architectural or epistemic **dynamics** are then *trajectories in the declared CharacteristicSpace*. **No** procedural or storage commitments are implied.

### C.16:9 - Conformance Checklist (Normative)

> *Thought‑level acceptance conditions for authors and reviewers; they constrain meaning, not tooling.*

**CC‑MCHR‑1 - CSLC anchoring.** Each `U.DHCMethodRef` binds **exactly one** `U.Characteristic` and **exactly one** scale; each `U.Measure` carries a value valid for that scale (cf. A.18).
**CC‑MCHR‑2 - Polarity declared.** Every **ordered** scale in a template declares **polarity**; any **Score** via 𝒢 is monotone w.r.t. that polarity.
**CC‑MCHR‑3 - Unit coherence.** Claims that compare or combine values are **grounded in unit coherence** (or declared conversions for interval/ratio).
**CC‑MCHR‑4 - Comparability honesty.** Ordered comparisons are asserted **only** when **R‑CMP‑1** holds (same‑template direct comparability) or when a **named, cited** transformation owner is provided per **R‑CMP‑2**; otherwise authors use qualitative/set‑level language.
**CC‑MCHR‑5 - Evidence sufficiency.** Where evidence is required by the template, the measure’s grounds are **conceptually sufficient** to retrace the claim; composition respects **Σ‑1…Σ‑4**.
**CC‑MCHR‑6 - RSG alignment.** If a measure gates a **state** in an RSG, the checklist criteria **respect scale semantics** and the **intensional vs description** split. No lifecycle phrasing; use RSG open‑ended moves.
**CC‑MCHR‑7 - Dynamics awareness.** Where discussions involve change, the **CharacteristicSpace** is **named** (characteristics, units, topology) and separated from the **transition law**.
**CC‑MCHR‑8 - Lexical guard‑rails.** Tech identifiers and headings use **Characteristic/Scale/Level/Value/Score/Unit/ScoringMethod**; aliases (axis/dimension/points/stars) appear **only** in explanatory Plain register with a first‑mention mapping to the Tech canon.

### C.16:10 - Invariants & Anti‑Patterns *(Normative unless marked “Informative”)*

#### C.16:10.1 - Invariants (N‑rules)

**N‑1 — One Characteristic + one Scale per template.**
Every `U.DHCMethodRef` binds *exactly one* **Characteristic** and *exactly one* **Scale** (its type + admissible range or level‑set). This is the CSLC sufficiency condition for interpretability.

**N‑2 — Value validity.**
A `U.Measure` holds a **Value** that is *admissible* for the template’s Scale (numeric range, categorical level); when a **Level** is used, it is among the named rungs declared for that Scale.

**N‑3 — Polarity is declared at the template.**
For ordered Scales, the template states the comparison direction (↑ better / ↓ better / target‑is‑best). Any **ScoringMethod mapping** to **Score** preserves that monotonic ordering. *(Note: we use “ScoringMethod mapping” instead of the Greek letter used elsewhere in FPF to avoid symbol conflicts.)*
For ordered Scales, the template states the comparison direction (↑ better / ↓ better / target‑is‑best). Any scoring method **𝒢** that issues a **Score** is order‑compatible with that declared polarity semantics.

**N‑4 — Unit coherence.**
Within one template there is one *primary* **Unit** of expression (or an explicit level‑set for non‑numeric Scales). Conversions are conceptually allowed only where the Scale supports meaningful arithmetic (interval/ratio); nominal/ordinal Scales are not subject to numeric conversions.

**N‑5 — Comparability guard.**
Two Measures are comparable *iff* they share the same template (hence, the same Characteristic + Scale + Unit) **or** stand in an explicit comparability relation whose single semantic owner is cited (e.g., an F‑cluster Bridge, or a cited characterization mechanism’s declared equivalence). Otherwise, comparability is not presumed.

**N‑6 — Evidence as conceptual anchoring.**
If a template requires it, each Measure includes an **EvidenceStub** that conceptually links the Value to its grounds; absence where required makes the Measure inadmissible for use. *(This is a conceptual obligation; no process mechanics are implied.)*

**N‑7 — Arity clarity.**
If the Characteristic is relational (applies to a pair/tuple), the subject of measurement is the relation itself; the reading must not be re‑described as a unary property of either participant.

**N‑8 — Open‑ended evolution; graph, not lifecycle.**
When MM‑CHR is used in change reasoning, movement happens in a **CharacteristicSpace** and along a **Role‑State Graph (RSG)**. There is no lifecycle terminal; revisions may re‑enter earlier framing nodes as per A.17. *(Conceptual control structure only.)*


#### C.16:10.2 - Anti‑Patterns (A‑rules) — with cures

**A‑1 — Scale drift under the same template.**
*Smell:* the Scale meaning (bounds, categories) shifts while the template ID remains.
*Cure:* version the template; declare the relation in the Unification suite.

**A‑2 — Arithmetic on ordinal.**
*Smell:* averaging “stars” or ranking labels as if they were intervals.
*Cure:* either keep order‑respecting operations only, or introduce a **ScoringMethod** that defines a proper Score range.

**A‑3 — Unit soup.**
*Smell:* mixing milliseconds and seconds for the same template, or “%” and “points” for one Scale.
*Cure:* one primary Unit per template; conversions (when meaningful) are declared conceptually, not ad‑hoc.

**A‑4 — Alias leakage.**
*Smell:* “axis/dimension/point/ladder” in normative identifiers or headings.
*Cure:* use only canonical tokens in normative prose; narrative labels are allowed *solely* in Plain register with first‑mention mapping (A.17).

**A‑5 — Multi‑Characteristic stuffing.**
*Smell:* one template tries to carry a vector of Values for several Characteristics.
*Cure:* separate templates (one Characteristic each) and compose coordinates explicitly when needed.

**A‑6 — Evidence afterthought.**
*Smell:* Measures required to have grounds are introduced without an intelligible EvidenceStub.
*Cure:* treat the EvidenceStub as part of the measurement claim itself, not an accessory.

**A‑7 — Template mutation after Measures exist.**
*Smell:* retro‑editing Characteristic/Scale/Unit of an active template.
*Cure:* immutability of that triad post‑use; publish a successor template if the concept changes.

**A‑8 — Score‑of‑everything.**
*Smell:* collapsing heterogeneous Values into a single “points” Score without declared ScoringMethod and SCP.
*Cure:* retain the Value on its Scale; add an explicit scoring method (by reference to its owner) and an explicit legality profile (owned elsewhere) only when there is a justified need for a Score.

### C.16:11 - Cross‑Domain Vignettes *(Informative, transdisciplinary)*

> *Each vignette shows an CSLC‑conformant template → measure, without duplicating the A.17/A.18 glossaries.*

**V‑A (Architecture — relational property).**
Characteristic: **Coupling** (relational) between modules; Scale: ordinal {Low, Med, High}; Unit: level‑labels; Polarity: ↓ better.
Reading: subsystem pair ⟨M₁, M₂⟩ gets **Med**; **ScoringMethod** (optional) maps levels monotonically to a bounded Score for comparative dashboards.

**V‑B (Physics — interval/ratio).**
Characteristic: **ResponseTime**; Scale: ratio with non‑negative reals; Unit: seconds; Polarity: ↓ better.
Reading: subject S has **0.237 s**; direct comparability holds with readings on the **same template**; cross‑template comparability requires an explicitly cited equivalence/Bridge/transformation owner.

**V‑C (Performing arts — ordinal).**
Characteristic: **EdgeControlQuality**; Scale: ordinal levels 1…5; Unit: level‑labels; Polarity: ↑ better.
Reading: performance P gets **4**; any aggregation remains order‑respecting. If a numeric dashboard score is needed, cite a scoring method **𝒢** that maps levels monotonically to a bounded Score.

**V‑D (AI ethics — ratio).**
Characteristic: **ParityGap** (difference of positive rates); Scale: interval with symmetric bounds; Unit: percentage points; Polarity: ↓ better (0 is target).
Reading: model M on cohort C shows **3.2 pp**; evidence points conceptually to the derivation rationale (inputs, reference cohorts).

### C.16:12 - Relations & Placement *(Informative)*

**Kernel.** MM‑CHR *imports* the canonical Characteristic vocabulary and the CSLC discipline fixed by A.17 and A.18; it does not redefine them. CharacteristicSpace reasoning (for change) lives in the patterns that consume MM‑CHR readings.

**Using patterns.** KD‑CAL, Arch‑CAL and others *instantiate* templates and produce measures; MM‑CHR remains a neutral measurement substrate. Trade‑off analyses and architectural trajectories operate over coordinates that MM‑CHR makes available, not inside MM‑CHR.

**Unification (F‑cluster).** External standards (e.g., ISO 80000 quantity types; W3C SOSA/SSN observable properties; QUDT units/quantity kinds) are related via Concept‑Set rows and Bridges; MM‑CHR treats those alignments as context supplied by F‑patterns, not as local re‑definitions.

### C.16:End

## C.17 - Characterising Generative Novelty & Value (Creativity‑CHR)

**Status.** Mechanism specification (**CHR**) — normative where stated.
**Depends on.** A‑kernel (A.1–A.15), **CHR‑CAL** (C.7), **MM‑CHR** measurement infrastructure (C.16), **KD‑CAL** and **Sys‑CAL** for carriers and holons, **Decsn‑CAL** (utility), **Norm‑CAL** (constraints/ethics).
**Coordinates with.** **B.5.2.1 NQD** (abductive generator) for search instrumentation, **Agency-CHR** (C.9) for agential capacity, B-cluster trust/assurance (B.3), Canonical Evolution Loop (B.4), Role Assignment & Enactment Cycle (Six-Step) (F.6) and Naming Discipline for U.Types & Role Names (F.5).
**Guard‑rails.** Obeys E‑cluster authoring rules (Notational Independence; DevOps Lexical Firewall; Unidirectional Dependency).

**What this pattern provides (exports):**

This pattern exports **Characteristics** and measurement templates **only**. It **does not** export any Γ\_\* operators, portfolio composition rules, or selection/scalarization policies; those live in **C.18 NQD-CAL** and **C.19 E/E-LOG** (or **Decsn-CAL** for decision lenses). A Context _publishes_ the measurement space and admissible policies; a decision is taken by an _agent in role_ using a _named lens_ within that space.

* **`U.CreativitySpace`** — a **CharacteristicSpace** (CHR) with named **Characteristics** and scale metadata for evaluating creative work/outcomes **inside a `U.BoundedContext`**.
* **`U.CreativityProfile`** — a vector of coordinates in `U.CreativitySpace` attached by a **`U.Evaluation`** to a specific **Outcome** (usually an `U.Episteme` produced by `U.Work`).
* **Core Characteristics (kernel nucleus; Context‑extensible):**
1. **`Novelty@context`** — distance from a **`ReferenceBase`** in the current Context/time window; ∈ \[0, 1].
2. **`Use‑Value`** *(alias: `ValueGain`)* — measured or predicted improvement against a **declared objective**; interval/ratio scale per Context.
3. **`Surprise`** — negative log‑likelihood under a **GenerativePrior**; bits or nats.
4. **`ConstraintFit`** — degree of **must‑constraint** satisfaction (Norm‑CAL / Service acceptance); ∈ \[0, 1].
5. **Diversity_P (portfolio-level)** — coverage/dispersion (set-level). **Illumination** is a **report-metric over Diversity_P** (coverage/QD-score summaries). It is **report-only** and **never** part of the primary dominance test.
6. **`AttributionIntegrity`** — provenance/licensing discipline for lawful, transparent recombination; ∈ \[0, 1].
7. **`FamilyCoverage`** — (count, polarity ↑, scope=portfolio, unit=families, provenance: F1‑Card)
8. **`MinInterFamilyDistance`** — (ratio [0,1] or metric units, polarity ↑, scope=portfolio, DistanceDef@F1‑Card)
9. **`AliasRisk`** —  (ratio [0,1], polarity ↓, diagnostic; drop if dSig ≥3/5 characteristics collide)
10. **`U.DomainDiversitySignature (dSig)`** — 5‑tuple over discrete characteristics **[Sector, Function, Archetype, Regime, MetricFamily]**  attached to each `U.BoundedContext`. Used for **Near‑Duplicate** diagnostics and `AliasRisk`. Policy: flag as Near‑Duplicate when ≥3 characteristics match; see F.1 invariants and SCR‑F1‑S08..S09. 
11. **Note (AliasRisk binding).** `AliasRisk` MAY be computed using `dSig` collision diagnostics; a Context MUST declare the collision rule and policy id in DescriptorMap provenance when AliasRisk is reported.

* **Supporting types (linking points):**

  * **`U.ReferenceBase`** — the domain‑local corpus (by Context & time window) used to compute `Novelty@context`.
  * **`U.SimilarityKernel`** — a declared similarity metric class for the Context (text/image/design/code/etc.), with invariance notes.
  * **`U.GenerativePrior`** — a predictive model over the Context’s artifacts/behaviours used to compute `Surprise`.
  * **`U.CreativeEvaluation`** — a specialisation of `U.Evaluation` that yields a `U.CreativityProfile` and the Evidence Graph Ref.
  * **`EffortCost`** *(advisory)* — resource outlay to achieve the outcome; from WorkLedger (Resrc‑CAL). *(For normalization and planning; not itself “creativity.”)*

* **Operators (first tranche):** `composeProfiles` (set → portfolio), `dominates` (partial order in space), `frontier` (Pareto set), `normaliseByEffort`. *(Formal laws introduced in Quarter 2.)*
* **Relations (informative; not exported):** dominance relation (partial order in the space), frontier predicate (Pareto set), portfolio composition view. *C.17 exports no operators; these are mathematical relations only.*
* 
> **Scope note.** This pattern **does not** define who is “a creative person.” It characterises **creative outcomes and episodes** as **observed in Work** and **expressed as Epistemes**. Agency (capacity to originate) is measured in **Agency‑CHR (C.9)**; here we measure **what came out** and **how it scores** against stated goals and references.  A **Context publishes** the measurement space and admissible policies; a **decision is made by an agentic system in role**, using a named lens within that space. CHR exports **no Γ‑operators** and **no team workflow rules**.

### C.17:1 - Motivation & Intent (manager’s read‑first)

**Problem we solve.** Teams talk past each other about “creativity”: some prize **novelty**, others **business value**, others **originality** or **risk‑managed invention**. Without a shared, context‑local measurement space, reviews derail, portfolios drift, and safety constraints are waived ad‑hoc.

**Intent.** Provide a **small, universal measurement kit** that turns “this is creative” into **checkable, context‑local statements** — grounded in **evidence**, aligned to **objectives**, and **composable** from individuals to portfolios.

**Manager’s one‑screen summary (what you can do with it):**

1. **Score** a design/code/theory change on **Novelty–Value–Surprise–ConstraintFit** with declared references and models.
2. **Compare** options in a **Pareto sense** (no single magic score forced).
3. **Consider** constraints as a **coordinate** in the space; compare options on **frontiers** while keeping Context for high‑novelty options
4. **Track** a portfolio’s **Diversity** to avoid local maxima and groupthink.
5. **Defend** decisions with an auditable **CreativeEvaluation** that cites **what was new relative to which base**, **how value was measured**, and **why this counts here**.


### C.17:2 - Forces

| Force                                | Tension we must resolve                                                                                                                 |
| ------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------- |
| **Universality vs. domain detail**   | One kit must serve hardware design, software, policy, and science, yet let each Context pick similarity kernels, priors, and value models. |
| **Invention vs. constraint**         | Creative leaps are valuable; safety, ethics, and acceptance are non‑negotiable.                                                         |
| **Local truth vs. Cross‑context reuse** | Meaning is context‑local (A.1.1); yet we need Bridges to compare across organisations/disciplines.                                         |
| **Single score vs. frontier**        | Management wants a number; reality is multi‑objective.                                                                                  |
| **Randomness vs. intention**         | Random noise looks “novel” yet useless; planned recombination can be highly creative.                                                   |

**Design answer.** A **context‑local CreativitySpace** with a **small set of characteristics**, each with **clear measurement templates** and **Evidence Graph Ref**; composition uses **frontiers and partial orders**, not forced scalarisation.


### C.17:3 - Solution Overview — The context‑local CreativitySpace

**Idea.** Creativity is **not a type**; it is a **profile** measured on an **outcome** (episteme) or **episode** (set of works) **inside a bounded context**. The context supplies the **ReferenceBase**, **SimilarityKernel**, **GenerativePrior**, **objective function(s)**, and **acceptance constraints**.

**Objects in play (A‑kernel alignment):**

* A **system** (person, team, service) performs **`U.Work`** under a role (A.2).
* That work yields a **carrier** (doc/model/design/code), i.e., an **`U.Episteme`**.
* We apply a **`U.CreativeEvaluation`** to that episteme (and linked work) to produce a **`U.CreativityProfile`** with evidence.

**Cre­ativitySpace (first‑class CHR):**
`U.CreativitySpace(Context) := 〈Novelty@context, ValueGain, Surprise, ConstraintFit, Diversity_P, AttributionIntegrity, EffortCost?〉`
with **scale**/**unit** metadata from **MM‑CHR** (C.16), and Context‑specific **measurement methods** bound by **MethodDescription**.

**Design/run split (A.4):**

* **Design‑time**: score **concepts** or **specs** against **surrogate value models** and **priors**; record **assumptions** (USM scopes; A.2.6).
* **Run‑time**: recompute **ValueGain** and **ConstraintFit** from Work evidence (service acceptance, KPIs) and refresh **Surprise** if priors update.


### C.17:4 - Vocabulary (CHR terms & D‑stubs)

> Names are **context‑local**; below are kernel terms. Roles like “Designer/Reviewer” are contextual (A.2). **Documents don’t act** (A.7/A.12); they are **evaluated**.

1. **`U.ReferenceBase`** *(D).* A curated, versioned **set of artifacts** (epistemes) and/or behaviours that define “what exists already” **in this Context and time window**.
   **Conformance (RB‑1):** must declare **inclusion criteria**, **time span (`TimeWindow`)**, and **coverage notes**.

2. **`U.SimilarityKernel`** *(D).* A declared **metric family** with invariances (e.g., text: cosine over embeddings, image: LPIPS, code: AST graph edit).
   **Conformance (SK‑1):** must cite **MethodDescription** and **test corpus**; state **limits**.

3. **`U.GenerativePrior`** *(D).* A model that yields **likelihood** of artifacts given the Context’s history (n‑gram/LM, design grammar, trend model).
   **Conformance (GP‑1):** must publish **training slice**, **fit method**, **perplexity/fit metrics**, and **refresh policy**.

4. **`U.CreativeOutcome`** *(D).* Any **`U.Episteme`** put forward for creative evaluation (e.g., new design, algorithm, spec, policy draft).
   **Note.** If the outcome is a **system change** without a single carrier, attach the evaluation to a **bundle** (set) of carriers referenced from Work.

5. **`U.CreativeEvaluation`** *(D).* A **`U.Evaluation`** that outputs a **`U.CreativityProfile`** and anchors to **ReferenceBase**, **Kernel/Prior**, **objective(s)**, **acceptance tests**, and **Work evidence**.

6. **`U.CreativityProfile`** *(D).* The **coordinate tuple** in `U.CreativitySpace` with provenance to the above inputs and **USM scopes**.
   **Conformance (CP‑1):** profile **must** include **scales/units**, **scopes**, **confidence bands** (B.3), and the **edition** of space definitions.


### C.17:5 - The Core Characteristics (kernel nucleus)

Each characteristic is specified per **MM‑CHR (C.16)** with: **name**, **intent**, **carrier**, **polarity**, **scale type**, **measurement template**, **evidence**, **scope (USM)**, and **didactic cues**. *Context profiles MAY add characteristics; kernel characteristics MAY NOT be removed without a Bridge.*

#### C.17:5.1 - `Novelty@context` — “How unlike the known set is this?”

* **Intent.** Quantify **distinctness** of the outcome relative to **`U.ReferenceBase`** (global or targeted slice).
* **Carrier.** `U.Episteme` (the outcome).
* **Polarity.** Higher is “more novel.”
* **Scale.** **\[0, 1]**; ratio (0 = duplicate under kernel; 1 = maximally distant).
* **Measurement template (normative pattern):**

  1. Declare **ReferenceBase** `B` and **TimeWindow** window.
  2. Declare **SimilarityKernel** `σ` and its invariances.
  3. Compute **`Novelty@context := 1 − max_{b∈B} sim_σ(outcome, b)`**, or a robust variant (top‑k mean).
  4. Publish **sensitivity note** (how results shift with kernel/`B`).
* **Evidence.** Kernel/version id; top‑k neighbours with distances; ablation on invariances.
* **Scope hooks (USM).** `B` **must** be a declared **slice**; Cross‑context use needs a **Bridge** with **CL** and **loss notes**.
* **Didactic cues.**

  * **Not** “randomness.” Noise has high novelty, low value.
  * **Local, not global.** Novelty is **to this Context now**, not timeless originality.

#### C.17:5.2 - `Use‑Value` *(alias: `ValueGain`)* — “What good did this add under our objective?”

* **Intent.** Quantify **benefit** vs a baseline objective (Decsn‑CAL utility, Service acceptance, KPI).
* **Carrier.** Outcome (episteme) with **Work** evidence.
* **Polarity.** Higher is better.
* **Scale.** Interval/ratio, unit **declared by the Context** (e.g., ΔSNR, % defects, profit/period).
* **Measurement templates (pick one):**

  * **Measured:** `ValueGain := metric_after − metric_before` (declare counterfactual method).
  * **Predicted:** `E[ValueGain | model]` with error bars; update post‑run.
  * **Evidence.**  Declared **objective/criterion**; measurements or credible predictions; counterfactual method (A/B, back‑test, causal inference).
  * **Scope.** State the **context window** used for the objective; claims outside that window are **informative only**.
  * **Didactic cues.**

  * Value is **relative to stated objective**; if the objective is wrong, the value reflects it.
  * Keep **counterfactual discipline**; otherwise “gain” is storytelling.

#### C.17:5.3 - `Surprise` — “How improbable under our learned world?”

* **Intent.** Capture **unexpectedness** given **`U.GenerativePrior`**.
* **Carrier.** Outcome.
* **Polarity.** Higher surprise = more unexpected.
* **Scale.** **bits** or **nats**: `Surprise := −log p_prior(outcome)`.
* **Measurement template:**

  1. Declare **GenerativePrior** (training slice, model class).
  2. Encode outcome for the prior; compute likelihood proxy.
  3. Publish calibration curve (reliability diagram / PIT histogram).
* **Evidence.** Model cards; fit metrics; OOD diagnostics; refresh policy.
* **Scope.** Training slice declared as **ContextSlice**; Bridges penalise **R** (trust), not the value itself (A.2.6).
* **Didactic cues.**

  * **Novelty vs Surprise:** high novelty under one kernel may be low surprise under a broad prior; publish both.

#### C.17:5.4 - `ConstraintFit` — “Did it honour the non‑negotiables?”

* **Intent.** Ensure **mandatory constraints** (safety, ethics, standards, SLOs) are satisfied.
* **Carrier.** Outcome + Work evidence.
* **Polarity.** Higher is **better** (1 = all mandatory satisfied).
* **Scale.** **\[0, 1]**, ratio or pass/fail.
* **Measurement template:** declare **set `C_must`** (Norm‑CAL / Service acceptance), compute **`ConstraintFit := |{c∈C_must : pass(c)}| / |C_must|`**; optionally weight per criticality.
* **Evidence.** Checklists, tests, audits; Who/Role performed the **SpeechActs** (approvals/waivers).
* **Scope.** Constraints are **context‑local**; Cross‑context requires **Bridge**; waivers are **SpeechAct Work** with RSG gates (A.2.5).
* **Interpretation note.** Low `ConstraintFit` signals tension with declared **must‑constraints** and warrants reframing or redesign; **this pattern does not prescribe go/no‑go rules**.

#### C.17:5.5 - `Diversity_P` *(portfolio‑level)* — “Are we exploring the space?”

* **Intent.** At the **set** level, avoid myopic exploitation; promote **coverage**.
* **Carrier.** A **set** of outcomes.
* **Polarity.** Higher means **broader coverage** (not “better” per se).
* **Scale.** Set‑functional; Context defines metric (e.g., **average pairwise distance**, **k‑cover** over features).
* **Template.** Declare **kernel** and **covering policy**; compute score and **coverage map (illumination)**; relate to **USM ClaimScopes**.
* **Alignment note.** The **illumination/coverage** view corresponds to *IlluminationScore* used by **B.5.2.1 NQD‑Generate**; no separate characteristic is introduced here—measure it as part of `Diversity_P`.
* **Evidence.** Distance matrix/cover plots; sensitivity to kernel.
* **Didactic cue.** Use **Diversity\_P** to **shape portfolios**, not to pick single winners.
* **Marginal gain (for generators)** — normative. For a candidate h and current set S, ΔDiversity_P(h | S) := Diversity_P(S ∪ {h}) − Diversity_P(S). Contexts using NQD SHALL compute D as this marginal and publish the Diversity_P definition alongside the CharacteristicSpace/kernel and TimeWindow.

**Heterogeneity Characterisation**
* FamilyCoverage  (polarity ↑) — count of distinct domain‑families covered by a portfolio/triad; unit: families; window: declared.
* MinInterFamilyDistance (polarity ↑) — min distance between selected families in DescriptorMap; unit: per DistanceDef; window: declared.
* AliasRisk (polarity ↓) — collinearity/near‑duplicate risk indicator for contextual signatures; unit: score (0–1) with policy id.


**Lexical special case (F.18 naming).**  
For **lexical CandidateSets** used by Name Cards (F.18), **Diversity_P SHALL be computed over head-term families, not over raw strings**. Variants that share the same lexical head (e.g., “Reference plane”, “Plane of reference”, “Planar reference”) **MUST** be treated as one family for coverage and distance; only candidates with distinct heads contribute to lexical Diversity_P. This aligns lexical use of Diversity_P with `FamilyCoverage` / `AliasRisk` and prevents inflating diversity by near-synonyms of a single head.


#### C.17:5.6 - `AttributionIntegrity` — “Did we credit sources and licences correctly?”

* **Intent.** Discourage “novelty theft”; ensure **recombination** is **lawful and transparent**.
* **Carrier.** Outcome + provenance graph.
* **Polarity.** Higher is better.
* **Scale.** **\[0, 1]**; fraction of **required attributions/licence duties** satisfied.
* **Template.** Trace graph coverage against Context policy; licence constraints as **Norm‑CAL** rules.
* **Evidence.** PROV‑style links; licence scans; acknowledgements.
* **Didactic cue.** High `AttributionIntegrity` signals lawful and transparent recombination; low values indicate unacceptable practice in most Contexts.  
* **Default role.** `AttributionIntegrity` is **measurable but non‑dominant**. It MAY serve as a **policy filter/tie‑break** (C.19). If certain attribution duties are **must‑constraints**, they belong to **ConstraintFit** (Norm‑CAL) and act as **eligibility gates**. It is **not** part of the default dominance set.
* **Dominance & gating note (normative).** `AttributionIntegrity` is a measurable **Characteristic**; it is **not** in the default dominance set. Contexts MAY use it as a **filter** or **tie‑break** via policy (C.19). Legal/ethical **must‑fit** checks live in **ConstraintFit** (Norm‑CAL); failing those blocks eligibility **before** dominance.

#### C.17:5.7 - `EffortCost` *(advisory)* — “What did it take?”

* **Intent.** Normalise comparisons by cost; not part of “creativity” per se.
* **Carrier.** WorkLedger.
* **Polarity.** Lower is better when used as denominator.
* **Scale.** Resource units (hours, energy, \$).
* **Template.** Sum cost categories over Work that produced the outcome.
* **Evidence.** Time/resource logs; BOM deltas.
* **Didactic cue.** Use **`CreativityPerCost := f(Novelty@context, ValueGain, Surprise)/EffortCost`** for operations planning, not for excellence awards.


### C.17:6 - Conformance Checklist (first tranche)

| ID                                        | Requirement (normative)                                                                                                                                                                  | Purpose / audit hint                                          |
| ----------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------- |
| **CC‑CR‑1 (context‑locality)**               | Every **CreativityProfile** **MUST** name the **`U.BoundedContext`** and the **edition** of `U.CreativitySpace`.                                                                         | Prevents Cross‑context slippage.                                 |
| **CC‑CR‑2 (Declared bases)**              | **Novelty@context** claims **MUST** declare `ReferenceBase`, `SimilarityKernel`, and `TimeWindow`; **Surprise** claims **MUST** declare `GenerativePrior` and its training slice.                 | Makes “new to whom?” and “unexpected under what?” explicit.   |
| **CC‑CR‑3 (Objective anchor)**            | **ValueGain** **MUST** reference the **objective** (KPI/utility) and **counterfactual method** (if predicted, the model).                                                                | Stops free‑form value stories.                                |
| **CC‑CR‑4 (Must‑fit)**                    | If **must** constraints exist, **ConstraintFit** **MUST** be present; enactment decisions **SHALL** treat `ConstraintFit<1` as **fail**, unless an explicit **waiver SpeechAct** exists. | Keeps safety & ethics non‑negotiable.                         |
| **CC‑CR‑5 (Evidence)**                    | Each coordinate **MUST** have Evidence Graph Ref (neighbours, tests, logs, model cards).                                                                                                   | Enables audit & replication.                                  |
| **CC‑CR‑6 (Scopes)**                      | Profiles **MUST** include **USM scopes** (ClaimScope/WorkScope) relevant to measurement; off‑scope claims are advisory.                                                                  | Ties numbers to where they hold.                              |
| **CC‑CR‑7 (No scalarisation by default)** | The pattern **SHALL NOT** force a single scalar “creativity score.” If a Context defines one, it **MUST** publish the weighting and its drift policy.                                   | Keeps decisions on a Pareto frontier unless a policy opts‑in. |
| **CC‑CR‑8 (Bridge discipline)**           | Cross‑context comparisons **MUST** use a **Bridge** with **CL** and recorded **losses**; any mapped coordinate **MUST** note penalties in the **R** lane, not silently alter the value.     | Honest portability.                                           |


### C.17:7 - Manager’s Quick‑Start (apply in 5 steps)

1. **Name the Context** *(context + edition)*.
2. **Pick measurement defaults** *(kernel, prior, objective, constraints)* from the Context’s handbook.
3. **Score outcome** → `Novelty@context`, `Use‑Value`, `Surprise`, `ConstraintFit`.
4. **Decide by frontier**: shortlist **non‑dominated** options; use **ConstraintFit** as a gate; apply **policy** if a scalar is approved.
5. **Record a CreativeEvaluation** with evidence; if crossing Contexts, attach the **Bridge id**.

> **Mental check.** *New to our base? Helpful to our objective? Unexpected under our model? Safe & licenced?*
> If any answer is “unknown,” you are **not done measuring**.


### C.17:8 - Archetypal Grounding (three domains)

**(a) Manufacturing design change)**
*Outcome.* New impeller geometry for Pump‑37.
*Context.* `PlantHydraulics_2026`.
*Novelty@context* 0.42 (shape‑descriptor kernel vs last 5 years).
*ValueGain.* +6.8% flow @ same power (bench Work).
*Surprise.* 1.3 bits (within evolutionary trend prior).
*ConstraintFit.* 1.0 (materials, safety, noise).
*Decision.* **Frontier winner**: modest novelty, clear value, safe. Portfolio keeps **Diversity\_P** by also funding one high‑surprise concept for exploration.

**(b) Software architecture refactor)**
*Outcome.* New concurrency model for ETL.
*Context.* `DataPlatform_2026`.
*Novelty\_G.* 0.27 (AST/edit kernel vs internal corpus).
*ValueGain.* −20% latency, −35% p95 stalls (A/B Work).
*Surprise.* 0.5 bits (trend prior expected co‑routines).
*ConstraintFit.* 0.83 (fails SoD—same author as reviewer).
*Decision.* Return for **SoD fix**; then likely adopt. Creativity is **not** a waiver over governance.

**(c) Scientific hypothesis)**
*Outcome.* A new scaling law claim.
*Context.* `GraphDynamics_2026`.
*Novelty\_G.* 0.66 (formula kernel vs literature base).
*ValueGain.* Predicted: explains 12 prior anomalies (model check).
*Surprise.* 3.7 bits (strongly unexpected under prior).
*ConstraintFit.* 1.0 (ethics N/A; evidence roles bound with decay windows).
*Decision.* Fund **replication Work**; track **R** decay per policy.


### C.17:9 - Anti‑Patterns (fast fixes)

| Anti‑pattern                   | Why it fails                                                                  | Fix with this FPF pattern                                                        |
| ------------------------------ | ----------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| **“Creativity = randomness.”** | Noise yields high `Novelty@context`, low `ValueGain` and often low `ConstraintFit`. | Evaluate **all four** characteristics; require ConstraintFit=1 for musts.                   |
| **Global originality claims.** | Ignores context‑local meaning and current corpus.                                | Declare **Context & ReferenceBase**; cross Contexts only via **Bridge**.               |
| **One magic score.**           | Hides trade‑offs; fragile under drift.                                        | Decide on **Pareto frontier**; publish scalar only with explicit weights/policy. |
| **Hand‑wavy value.**           | No objective → no audit.                                                      | Tie to **Service/KPI** or **utility**; state **counterfactual**.                 |
| **Silent borrowing.**          | Legal/ethical risk; reputational damage.                                      | Track **AttributionIntegrity**; licence scans in evidence.                       |


### C.17:10 - Relations

* **A.2 Role & A.15 Run‑alignment.** Creative **Work** is performed by **systems in roles**; outcomes are **epistemes**. Creativity is **measured by `U.Evaluation`**, not “done by a document.”
* **B.3 Trust/Assurance.** Coordinates carry **confidence bands**; Bridges lower **R** by **CL**. Evidence roles (A.2.4) bind datasets/benchmarks used in measurements.
* **C.9 Agency‑CHR.** Agency measures **capacity to originate**; a high‑agency system may still output low‑creativity outcomes (and vice versa with strong scaffolding).
* **A.2.6 USM (Scope).** All measurements sit on **ContextSlices**; `G‑ladder` is explicitly **not** used (C.17 follows A.2.6’s set‑valued scopes).
* **D‑cluster ethics.** **ConstraintFit** is where **must** constraints, ethics, and safety bind the evaluation; waivers are explicit **SpeechActs**.


### C.17:11 - Authoring Aids (didactic cards)

* **Write the Context.** Context + edition on every profile.
* **Name the base & kernel.** Without them, `Novelty@context` is undefined.
* **State the objective.** Value without a KPI is a story.
* **Publish priors.** Surprise needs a trained model with cards.
* **Gate by musts.** `ConstraintFit` < 1 blocks enactment unless waived.
* **Prefer frontiers.** Shortlist non‑dominated options; let governance decide trade‑offs.
* **Bridge explicitly.** Cross‑context talk needs CL and loss notes.

### C.17:12 - CSLC recap and the Creativity CharacteristicSpace

**Purpose.** Ground “creativity” as a **measurable family of characteristics** (CHR) rather than a role, capability, or virtue. Each characteristic is scoped to a **`U.BoundedContext`**, evaluated on **`U.Work`** (episodes), **artifacts** (epistemes, e.g., design sketches, models), or **holders** (systems/teams) via **MM‑CHR** exports (`U.DHCMethodRef`, `U.Measure`, `U.Unit`, `U.EvidenceStub`), using the **CSLC** discipline (*Characteristic / Scale / Level / Coordinate*).

> **Strict Distinction (A.7) reminders.**
> *Creativity is not a Role* (no one “plays CreativityRole”). It’s a **characterisation** of outcomes/process.
> *Creativity is not Work* (no resource deltas). Work **produces** artifacts we later characterise.
> *Creativity is not a service promise clause* (no external promise). Promise clauses are judged from Work; creativity may correlate with value.

#### C.17:12.1 - The Creativity CharacteristicSpace (CHR‑SPACE)

The core **characteristics** below are **kernel‑portable** names; Contexts **specialise** them (rename if needed, but keep semantics). Each characteristic declares: **what we measure**, **on what carrier**, **typical scale**, and **where it lives** in FPF.

| Characteristics (kernel name)       | What it captures (intuitive)                                 | Measured on           | Typical scale (CSLC)                               | Lives with / checked by              |
| ------------------------ | ------------------------------------------------------------ | --------------------- | -------------------------------------------------- | ------------------------------------ |
| **Novelty\@context**        | Distance from known ideas **in this Context**                   | Artifact / Work set   | Ratio or bounded \[0..1] via *similarity→distance* | `KD‑CAL` corpus + `U.BoundedContext` |
| **Use‑Value**            | Benefit vs a **declared objective**                          | Artifact / Evaluation | Ordinal (Fail/Partial/Pass) or scalar KPI          | `B.3` Evidence & `U.Evaluation`      |
| **Surprise**             | Unexpectedness under the Context’s **GenerativePrior**          | Artifact              | bits or nats (−log‑likelihood)                     | Prior cards & calibration            |
| **ConstraintFit**        | Degree of **must‑constraints** satisfied while exploring     | Work / Artifact       | % satisfied (0–100)                                | `Norm‑CAL` + step guards             |
| **Diversity_P**          | Portfolio **coverage/dispersion** (incl. coverage map view)  | Set of artifacts      | Set‑functional; coverage index                     | `Γ_ctx` fold + USM ClaimScopes       |
| **AttributionIntegrity** | Lawful & transparent **provenance/licensing**                | Artifact + provenance | \[0,1]                                              | PROV + Norm‑CAL                      |

> **Locality.** **Every characteristic is context‑local** (e.g., **Novelty\@context**). Cross‑context claims **must** use a **Bridge** and record **CL** penalties (B.3). No global novelty.

#### C.17:12.2 - Context extensions & policy‑level characteristics (non‑kernel)

The following **context‑local** characteristics remain available but are **not** part of the kernel nucleus; use them as **derived** or **policy** measures:

* **ReframeDelta** — change in the **problem frame** that improves solvability (episteme‑pair; ordinal).
* **Compositionality** — degree of **re‑use and new relations** among parts (artifact; boolean + structure score).
* **Transferability\@X** — portability to **Context X** via a Bridge (artifact; ordinal + CL penalty).
* **DiversityOfSearch** — breadth of **approach classes tried** (work set; count/rate).
* **Time‑to‑First‑Viable** — elapsed time to first **Use‑Value = Pass** (work; duration).
* **Risk‑BudgetedExperimentation** — planned vs realized exploration share (workplan vs work; ratio; policy gate).

> **Compatibility note.** This split removes duplicate “core lists” and aligns C.17 with **B.5.2.1 NQD** and **C.16/A.17–A.18**: the **kernel nucleus** captures creativity *qualities*; the items above instrument **process/policy** or **portfolio shaping**.

#### C.17:12.3 - Scale choices (CSLC discipline)

For each characteristic, **declare the scale** explicitly (nominal / ordinal / interval / ratio). **Do not** average ordinal scores; fold with medians or distributional summaries. Choose **units** (when applicable) and **coordinate** semantics (e.g., what “distance” means).

* *Novelty\@context.*
  Coordinate = `1 − max_similarity(candidate, corpus)` with a declared encoder (text, graph, CAD). Unitless in \[0..1]. Document encoder & corpus freeze (`A.10` Evidence Graph Ref).
* *Use‑Value.*
  `Pass` iff **acceptanceSpec** (from `U.PromiseContent` or Decision KPI) is met from **Work** evidence; else `Partial`/`Fail`. For scalar KPIs, publish mean ± CI and the acceptance threshold; predicted values carry error bars and are updated post‑run.
* *ConstraintFit.*
  Ratio = satisfied / declared **must** constraints. Constraints are `Norm‑CAL` rules; **count only declared** ones (no unspoken “norms”).


#### C.17:12.4 - Metric templates (normative kernels + manager‑ready variants)

 **Template syntax (MM‑CHR):**
`U.DHCMethod { name, context, carrierKind, definition, unit?, scale, EvidencePin, acceptanceHook? }`
*Note:* Data instances carry `DHCMethodRef` pointing to this template.

##### C.17:12.4.1 - Templates (kernel definitions)

1. **`MT.Novelty@context`**

* **carrierKind:** Artifact|WorkOutput.
* **definition:** `1 − max_sim(encode(x), encode(y))` over y in **ReferenceSet**@Context.
* **scale:** ratio \[0..1].
* **EvidencePin:** `{ReferenceSetId, EncoderId, Version}`; frozen by `A.10`.
* **notes:** Publish encoder & corpus drift in RSCR.

2. **`MT.Use‑Value`**

* **carrierKind:** Work (fulfillment) → artifact (decision memo).
* **definition:** Evaluation of an outcome against a declared **objective/criterion** for the current context (or predicted value with explicit model & error).
* **scale:** ordinal {Fail, Partial, Pass} or scalar KPI.
* **EvidencePin:** links to `U.Work` that **fulfilPromiseContent\`**; cite acceptanceSpec edition.

3. **`MT.ConstraintFit`**

* **carrierKind:** Work / Artifact.
* **definition:** `|{c∈C_must : pass(c)}| / |C_must|` within the **MethodDescription** scope; optional weighting by criticality allowed if declared.
* **scale:** ratio \[0..1].
* **EvidencePin:** constraint list from **Norm‑CAL**; checks from Work telemetry.

4. **`MT.ReframeDelta`**

* **carrierKind:** Episteme pair (ProblemStatement v0→v1).
* **definition:** Categorise frame change as {None, Local, BoundaryShift, Systemic}; **justify** with a Scope diff (`A.2.6 U.ContextSlice` delta) and causal map simplification.
* **scale:** ordinal 0–3.
* **EvidencePin:** diff artifact + Bridge notes if Cross‑context.

5. **`MT.DiversityOfSearch`**

* **carrierKind:** Work set (episode).
* **definition:** Count of **distinct approach classes** tried (domain‑local typology) / time.
* **scale:** count; derived rate.
* **EvidencePin:** tagged Work items; typology lives in the Context glossary.

6. **`MT.Compositionality`**

* **carrierKind:** Artifact.
* **definition:** set aggregator (Compose‑CAL) of reused components ≥ K and presence of novel relation among ≥ 2 parts.
* **scale:** boolean + secondary “structure score” (e.g., depth or edge novelty).
* **EvidencePin:** component graph + provenance of parts.

7. **`MT.Transferability@X`**

* **carrierKind:** Artifact.
* **definition:** Applicability in target **Context X** via a **Bridge**; report **CL** and residual scope slice.
* **scale:** ordinal {not portable, portable with loss, near‑iso}; record CL (0–3).
* **EvidencePin:** Bridge id + pilot Work in X.

8. **`MT.Time‑to‑First‑Viable`**

* **carrierKind:** Work episode.
* **definition:** elapsed wall‑clock to first `UsefulnessEvidence = Pass`.
* **scale:** duration.
* **EvidencePin:** first passing `U.Work` id.

9. **`MT.Risk‑BudgetedExperimentation`**

* **carrierKind:** WorkPlan vs Work.
* **definition:** `(Planned exploratory spend) / (Allowed risk budget)` and realised counterpart; flag **overrun**.
* **scale:** ratio + policy gate (pass/fail).
* **EvidencePin:** WorkPlan ledger vs `WorkLedger`.

##### C.17:12.4.2 - Manager’s quick checks (plain‑language adapters)

* **Novelty** without a **frozen corpus** is **storytelling**—freeze corpus, fix encoder, then score.
* **Use‑Value** without a **consumer‑facing acceptance** is a **proxy**—bind to a **Service** or explicit Objective.
* **Diversity** counts **approach classes**, not color‑swap variants—publish your typology.

### C.17:13 - Novelty & transfer are **context‑local** (Bridges mandatory)

**Rule N‑1 (Locality).** `Novelty@context` is defined **only** within its `U.BoundedContext`. **Never** compare scores across Contexts without an **Alignment Bridge** (F.9).

**Rule N‑2 (Directional mapping).** A Bridge may assert a **directional** substitution (e.g., *Novelty\@DesignLab → Novelty\@Manufacturing* with CL = 2, **loss:** aesthetics encoder absent). Reverse mapping is **not** implied.

**Rule N‑3 (Penalty to R, not to G).** Cross‑context novelty **does not** change scope **G**; it **reduces R** (reliability) by the **CL penalty** (B.3), unless validated by pilot Work in the target Context.

**Practical pattern.** Publish novelty **with its Context tag** and—when reused—attach the **Bridge id** and target‑context **pilot** outcomes.


### C.17:14 - Anti‑Goodhart guard (use creativity metrics safely)

> **Goodhart’s Law:** “When a measure becomes a target, it ceases to be a good measure.” — We bake in **guards** so creativity scoring **improves** outcomes instead of gaming them.

#### C.17:14.1 - Guard‑rails (normative)

* **G‑1 Paired appraisal.** **Never** assess **Novelty** in isolation; pair it with **Use‑Value** or **ConstraintFit** to avoid proxy myopia
* **G‑2 Frozen references.** Novelty requires **frozen corpus + encoder**; changes create a **new edition** and **RSCR** rerun. Portfolio/selection heuristics are **policy-level** (see **C.19**); do not “reward” Illumination beyond its role as a report-metric.
* **G‑3 Time‑lag sanity.** Include a **post‑fact check** (e.g., 30–90‑day retention or cost‑to‑serve delta) before celebrating “creative wins.”
* **G‑4 Exploration budget.** Tie **DiversityOfSearch** to **Risk‑BudgetedExperimentation**; flag overspend.
* **G‑5 No ordinal averaging.** Do not average **ordinal** scales; use distributions/medians or convert only under declared models.

#### C.17:14.2 - Conformance Checklist — **CC‑C17‑M (metrics & guards)**

| ID             | Requirement                                                                                                                            | Practical test                                                              |
| -------------- | -------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------- |
| **CC‑C17‑M.1** | Each metric instance **MUST** cite its **Context**, **edition**, and **evidence hooks** (corpus/encoder, acceptanceSpec, constraint set). | Scorecard lists `ContextId`, `Edition`, and hook ids resolvable via `A.10`. |
| **CC‑C17‑M.2** | **Novelty** scores **MUST NOT** be used to approve Work without a **paired gate** (**Use‑Value** **or** **ConstraintFit**).               | Find decisions referencing novelty; check co‑gate present.                  |
| **CC‑C17‑M.3** | Cross‑context reuse **MUST** cite a **Bridge** and record **CL**; **R** is penalised accordingly.                                         | Scorecards with foreign Context tag lacking Bridge → **fail**.                 |
| **CC‑C17‑M.4** | Ordinal metrics **MUST** be summarised with medians/distributions, not means, unless a declared model justifies numeric treatment.     | Reports using a mean on ordinal without model → **fail**.                   |
| **CC‑C17‑M.5** | Metric templates **MUST** be versioned; changing encoder, reference set, or acceptanceSpec **creates a new edition**.                  | Diff shows changed hooks without edition bump → **fail**.                   |


### C.17:15 - Worked mini‑cases (engineer‑manager focus)

> **All names are context‑local; bridges and editions are explicit.**
> We show **(a)** what is measured, **(b)** who acts, **(c)** what is accepted, and **(d)** how evidence flows.

#### C.17:15.1 - Case A — Hardware ideation sprint (manufacturing design)

* **Context.** `DesignLab_2026`.
* **Objective.** Reduce fastener count by ≥ 30 % without tooling changes.
* **MethodDescription.** “Morphological matrix ideation v2.”
* **Work.** 1‑day sprint, 6 sessions.
* **Metrics.** `Novelty@context` (encoder: CAD‑graph v1; ReferenceSet: in‑house assemblies), `ConstraintFit` (no‑tooling‑change), `Use‑Value` (acceptance: Pass if sim shows ≤ +5 % assembly time).
* **Roles.** Performers = design cell (#TransformerRole); Observer = methods coach (#ObserverRole ⊥).
* **Outcome.** 22 candidates; 4 **Pass** usefulness; best `Novelty`=0.41 with **100 %** constraints respected; `Time‑to‑First‑Viable` = 3 h 40 m.
* **Evidence.** Scorecard episteme holds metrics; links to Work ids; acceptance tied to internal **promise content** “Design‑for‑Assembly Simulation”.

**Manager’s read.** “We didn’t just produce ‘novel’ shapes; 4 passed the sim and respected constraints, within the day.”


#### C.17:15.2 - Case B — Data‑science hypothesis generation (health analytics)

* **Context.** `Cardio_2026`.
* **Objective.** Find a new risk factor candidate for readmission (< 30 days).
* **MethodDescription.** “Causal discovery v3 + clinician review.”
* **Metrics.** `DiversityOfSearch` (approach classes: feature ablation, IVs, DAG‑learners), `Novelty@context` (text encoder over prior hypotheses), `Use‑Value` (AUROC uplift ≥ 0.03 on hold‑out), `Transferability@Hospital_B` (Bridge CL=2).
* **Roles.** SRE pipeline (#ObserverRole) computes metrics; clinicians (#ReviewerRole) set acceptance; data squad (#TransformerRole) performs experiments.
* **Outcome.** Two candidates; one meets AUROC uplift; **Transferability** requires follow‑up (CL penalty).
* **Evidence.** Episteme bundle: model cards, hold‑out plots, Bridge note.

**Manager’s read.** “One candidate works **here**; plan a pilot at Hospital B (we recorded CL=2).”


#### C.17:15.3 - Case C — Product squad reframing (software UX)

* **Context.** `SaaS_Onboarding_2026`.
* **Objective.** Reduce time‑to‑value (TTV) by 20 %.
* **MethodDescription.** “JTBD interviews + onboarding flow experiments.”
* **Metrics.** `ReframeDelta` (BoundaryShift: split onboarding into ‘job setup’ and ‘first result’), `Use‑Value` (TTV ‑22 % on A/B), `Risk‑BudgetedExperimentation` (within cap), `Compositionality` (reuse of existing workflow widgets).
* **Roles.** UX researcher (#ObserverRole), squad (#TransformerRole), product ops (#ReviewerRole).
* **Outcome.** Frame changed; TTV target passed; experiments within budget.
* **Evidence.** Reframing episteme with Scope diff + A/B report.

**Manager’s read.** “We changed the problem frame and proved the value drop—within risk limits.”


#### C.17:15.4 What these cases illustrate (tie‑backs)

* **Locality.** All novelty/usefulness claims are **Context‑tagged**; Cross‑context steps use **Bridges** with **CL**.
* **Dual‑gate.** Novelty never acts alone; usefulness/constraints co‑gate decisions.
* **SoD & Evidence.** Observers are **separate** from performers; metrics live on **epistemes** with **frozen hooks**; Work proves fulfillment.


### C.17:16 - Working examples

#### C.17:16.1 - Software (algorithmic/architectural ideation)

**Kernel characteristics (↑/↓/gate).**
Novelty↑ (algorithmic / compositional), Use‑Value↑ (targeted user/job metric), ConstraintFit=gate (resource/latency envelope), Cost‑to‑Probe↓ (hours to runnable spike), Evidence‑Level↑ (tests/benchmarks confidence), Option‑Value↑ (paths unlocked), RegretRisk↓ (blast radius if wrong).

**Priors.**

* Novelty prior **skeptical** beyond nearest known family (discount by conceptual distance).
* Evidence prior at **L0** (B.3) until benchmarks exist; regression tests act as **ObserverRole** evidence.

**Context card (one screen).**

* Γ\_bundle: Cost = sum; ConstraintFit = AND; Novelty = subadditive; Evidence = min (chain) / SpanUnion (indep).

#### C.17:16.2 - Hardware (mechanical/electro‑mechanical concepting)**

**Kernel characteristics.**
Novelty↑ (principle/material), Use‑Value↑ (performance delta), ConstraintFit=gate (manufacturability window), Time‑to‑Probe↓ (bench jig), Cost‑to‑Probe↓, SafetyRisk↓ (hazard), Evidence‑Level↑ (bench data), Option‑Value↑ (platform reuse).

**Priors.**

* SafetyRisk has **WLNK** priority (R must cover hazard chain).
* ConstraintFit must pass **manufacturing gate** before frontier inclusion.

**Context card.**
* Γ\_bundle: Hazard = max; ConstraintFit = AND; Cost = sum+coupling; Evidence = min on chain; Scope via **WorkScope** (A.2.6).

#### C.17:16.3 - Policy design (rules/standards/programs)

**Kernel characteristics.**
Novelty↑ (institutional), Use‑Value↑ (measurable social/operational effect), ConstraintFit=gate (legal/operational), Cost‑to‑Probe↓ (pilot), Evidence‑Level↑ (triangulated), EthicalRisk↓ (D‑cluster), Option‑Value↑ (coalitions/pathways), Scope (ClaimScope G) explicit.

**Priors.**
* EthicalRisk uses **status‑only** eligibility conditions; Evidence aging (decay) is **fast**; cross‑context Bridges carry **CL** penalties.

**Context card.**
* Γ\_bundle: EthicalRisk = max; ConstraintFit = AND (legal & operational); Cost = sum; Evidence = min/SpanUnion; Scope = ClaimScope (A.2.6).

### C.17:17 - Consequences & fit (for engineer‑managers)

* You can **reason on paper** about creativity: compare with **dominance**, pick along a **frontier**, and steer exploration with a few **policy characteristics**.
* Changes to the space (**scales, eligibility conditions, operators**) are handled by **RSCR**, so decisions are **explainable over time**.
* The **Context handbooks** are a **thinking OS**: one screen to start ideating without importing tool stacks or management playbooks.

### C.17:18 - Relations

* **Builds on**: B.1 Γ‑algebra (WLNK/COMM/IDEM/MONO), B.3 Trust & Assurance (F–G–R, CL), A.2.6 USM (Claim/Work scopes), A.10 Evidence Graph Referring.
* **Coordinates with**: A.2 Role suite (Observer/Evidence roles for probes), A.15 (Work & plans for probes), C.16 MM‑CHR (scale polarity & units). **C.18 NQD-CAL** (generation/illumination operators Γ_nqd.\*) and **C.19 E/E-LOG** (policies, selection, and portfolio rules). This CHR remains measurement-only.
* **Defers to**: F.9 Bridges for Cross‑context transfers; D‑cluster for ethical/speech‑act gates.

### C.17:19 - Quick reference cards (tear‑out)

* **Dominance test**: apply **signs** + **eligibility conditions** + **trust**; then partial order.
* **Frontier use**: **show frontier** + **name the lens** that picked your choice.
* **Portfolio policy**: keep `ExploreShare` and `WildBetQuota`; set `BackstopConfidence`; rebalance on cadence.

### C.17:20 - Conformance Checklist (pattern‑level, normative)

> *Pass these and your CS modelling remains a thinking architecture, not a team‑management manual.*

**CC‑C17‑1 (context‑local CS).**
Every **CreativitySpace** (the characteristic set where ideation and selection are measured) **MUST** be defined *inside one* `U.BoundedContext`; all characteristics and their scales are local to that Context. (Bridges with CL penalties are required across Contexts; see §C.17.16.)

**CC‑C17‑2 (Characteristics, not “characteristics”).**
Each CS dimension **SHALL** be a named **Characteristic** per **MM‑CHR**, with kind (`qualitative`, `ordinal`, `interval`, `ratio`, or `set‑valued`), unit/scale, polarity, and admissible operations. No free‑floating coordinates. (A.CHR‑NORM / A.CSLC‑Kernel.)

**CC‑C17‑3 (Profile ≠ plan).**
A **Profile** is a *state description over characteristics* (what the option *is* in CS); a **Plan** or **Method** is *how you will act*. Never encode choices or schedules into the profile.

**CC‑C17‑4 (Portfolio = set + rule).**
A **Portfolio** is a set of candidate profiles **plus** a selection rule (objective + constraints) declared *in the same Context*. Presenting only a scatterplot is non‑conformant.

**CC‑C17‑5 (Dominance operator well‑typed).**
A dominance claim **MUST** name the **characteristic subset and polarity** under which it is evaluated. Dominance on incomparable scales (or mixed polarities without explicit transformation) is invalid.

**CC‑C17‑6 (Frontier from rule, not from taste).**
A **Frontier** (Pareto or constraint‑bound) **SHALL** be computed from the declared selection rule; drawing a “nice hull” by eye fails conformance.

**CC‑C17‑7 (Search–Exploit as **dynamics**, not policy dogma).**
Exploration/exploitation **MUST** be expressed as a **dynamics on the portfolio measure(s)** (e.g., exploration share as a function of marginal value of information), *not* as a prescriptive budget recipe. (Design‑time statements belong to Decsn‑CAL; see §C.17.16.)

**CC‑C17‑8 (Evidence Graph Referring for scores).**
Any numeric score in a profile **MUST** cite its **MeasurementTemplate** (MM‑CHR) and the **observation/evaluation** that yielded it. No anonymous numbers.

**CC‑C17‑9 (Separable uncertainty lanes).**
Keep **aleatory** vs **epistemic** uncertainty separate on characteristics; their combination rule **MUST** be stated (e.g., interval arithmetic, conservative bound).

**CC‑C17‑10 (Time is explicit).**
Comparisons across iterations **MUST** state `TimeWindow` (snapshot window) and whether *drift* or *refit* occurred (§C.17.14). “Latest” is not a time selector.

**CC‑C17‑11 (No proxy collapse).**
If a composite “creativity index” is used, its **aggregation algebra** (weights, monotone transforms) **MUST** be declared; the primitive characteristics remain queryable.

**CC‑C17‑12 (Work stays on Work).**
Resource/time actuals and run logs live on `U.Work`; CS never carries actuals. We reason **about** profiles/portfolios; we do not audit operations here.


### C.17:21 - Worked‑Context Handbooks (concept cards, not runbooks)

> *Each Context publishes one page per card. These are **thinking kernels**: priors, objectives, admissible characteristics, and example transforms. No staffing, no process charts.*

**(a) Kernel Card — “What is a creative win here?”**

* **Context:** `<Context/Edition>`
* **Purpose Characteristic(s):** what “win” means (e.g., *Novelty*, *Usefulness*, *Adoptability*), with polarity and admissible ops.
* **Constraint Characteristics:** *Risk*, *Cost of change*, *Time to learn*, etc.
* **Objective** *(Decsn‑CAL pointer)*: Maximise `<purpose>` subject to declared constraints.
* **Frontier Rule:** Pareto over `{purpose ↑, risk ↓, cost ↓, time ↓}`.
* **Evidence Hooks:** which observations/evaluations populate each characteristic.

**(b) Priors Card — “What we believe before seeing data.”**

* **Default priors** on uncertainty for each characteristic (e.g., Beta for adoption probability).
* **Bridge policy:** minimal CL acceptable for imported profiles.
* **Exploration prior:** initial exploration share as a function of prior entropy.

**(c) Objective Variants Card — “Admissible objective shapes.”**

* Catalog the *few* objective forms this Context allows (lexicographic tie‑break, ε‑constraint, max‑min fairness), with **didactic pictures** of their frontiers.
* State when to switch objective (e.g., during bootstrapping vs exploitation).

**(d) Ready‑to‑use transforms** *(MM‑CHR aligned)*

* Monotone maps (e.g., log utility), normalizations, ordinal→interval “do & don’t” (only with evidence of order‑to‑interval validity).
* **Forbidden transforms** list (e.g., averaging ordinal ranks).

These cards are *conceptual fixtures*; **Tooling** may implement them, **Pedagogy** may teach them, but **C.17** only standardises their content as **thinking affordances**.

### C.17:22 - Placement sanity‑check across the pattern language *(avoid scope creep)*

* **MM‑CHR (C.16):** defines **Characteristic/Scale/Unit/Measure** and the *characterisation discipline*. **All** CS dimensions live there; C.17 **uses** them, never re‑defines scales.
* **A.CHR‑SPACE (A.19):** exports **CharacteristicSpace & Dynamics hooks**; C.17 is a **Contexted specialisation** for creative reasoning (profiles/portfolios/selection).
* **Decsn‑CAL (C.11):** hosts **objective functions, constraints, preference orders, utility proofs**, and the **search–exploit dynamics** as decision policies. C.17 only **names** the hooks (objective, rule), keeps policy math out.
* **KD‑CAL (C.2) & B.3 (Trust):** carry **evidence provenance**, **assurance** and **congruence penalties (CL)** for Cross‑context reuse. C.17 requires anchors; it does not invent confidence calculus.
* **Compose‑CAL (C.13):** governs **set/union/slice** aggregation; the portfolio set is a **Γ\_m.set** over profiles; frontier is derived **without** ad‑hoc geometry.
* **B.4 Canonical Evolution Loop:** where *Run→Observe→Refine→Deploy* sits. C.17 supplies the **view** in which refinement is judged.

**Out of scope here:** team staffing, budgeting workflows, data‑governance procedures, ticket states, any “how to manage people”. This pattern organises **thought**, not **teams**.

### C.17:23 - Anti‑patterns & canonical rewrites (conceptual hygiene)

1. **characteristic‑speak.** “Along the novelty characteristic…” → **Rewrite:** “Along the **Novelty characteristic** (ordinal; higher is better)…”.
2. **Pretty hulls.** Drawing a convex hull and calling it a frontier → **Rewrite:** compute Pareto under declared characteristic polarities.
3. **Ordinal arithmetic.** Averaging ranks or Likert values → **Rewrite:** either treat as **ordinal** and use **order‑safe** operators, or justify an interval mapping via MM‑CHR evidence.
4. **Proxy tyranny.** Single composite index driving choice unseen → **Rewrite:** publish **primitive characteristics**, index formula, and sensitivity.
5. **Policy‑as‑math.** “10% wild bets” as a rule → **Rewrite:** declare an **exploration dynamics** tied to value‑of‑information; if keeping a heuristic, label it as such.
6. **Global meaning.** Porting a profile from another Context by name → **Rewrite:** attach a **Bridge** with CL and loss notes; adjust trust, not scales.
7. **Plan‑profile blur.** Putting milestones into profiles → **Rewrite:** move schedules to `U.WorkPlan`; keep CS for *how options compare*, not *how to execute*.

### C.17:24 - Minimal didactic cards (one screen each)

**(1) Profile Card**

* **Option id & Context**
* **Characteristics table** (value, unit/scale, uncertainty split)
* **Evidence Graph Ref** (Observation/Evaluation ids)
* **Notes** (bridges used, CL penalties)

**(2) Portfolio‑with‑Rule Card**

* **Set of candidate profiles (refs)**
* **Objective & constraints** (Decsn‑CAL pointer)
* **Dominance subset** & **Frontier snapshot** (with TimeWindow)
* **Delta vs previous** (entered/exited/moved)

**(3) Search–Exploit Card** *(conceptual)*

* **Exploration share** as function of **marginal VOI** (symbolic)
* **Update cadence** (TimeWindow policy)
* **Stop conditions** (e.g., VOI below threshold; risk bound reached)

**(4) RSCR Summary Card**

* **What changed?** (refit/Δ±)
* **Sentinels status**
* **Frontier churn**
* **Bridge CL drift**

These cards are **thinking scaffolds**; they do not prescribe org process.

### C.17:25 - Consequences (informative)

| Benefit                    | Why it matters                                                                                                                    |
| -------------------------- | --------------------------------------------------------------------------------------------------------------------------------- |
| **context‑local rigour**      | Creative comparison is made decidable *where meaning lives*; Cross‑context reuse is explicit and penalised only in trust, not scale. |
| **Frontier honesty**       | Decisions rest on declared characteristics and polarities; frontiers follow rules, not taste.                                     |
| **Temporal comparability** | RSCR prevents silent drift; “better/worse” claims retain meaning over iterations.                                                 |
| **Method independence**    | Any tooling can implement the cards; C.17 remains a conceptual API for thought.                                                   |

**Trade‑offs:** upfront ceremony (declare characteristics, polarity, TimeWindow) and disciplined bridges. The payoff is comparability and explainability.

### C.17:26- Open questions (non‑normative, research hooks)**

* **Information geometry of CS:** can certain Contexts justify canonical distance metrics across characteristics without violating MM‑CHR parsimony?
* **Multi‑agent exploration:** how to couple individual CS frontiers into a *co‑exploration* equilibrium without importing team governance?
* **Learning‑to‑rank vs measurement:** what minimal evidence suffices to treat an ordinal characteristic as interval for the purpose of frontier estimation?

### C.17:End

## C.18 - Open‑Ended Search Calculus (NQD‑CAL)

**Status.** Calculus specification (**CAL**). Exports `Γ_nqd.*` operators for open‑ended, illumination‑style generation. **ΔKernel = 0** (no kernel primitives added). *Minting note:* this CAL **does not mint** new U‑types; it defines **CAL‑records** that MAY alias to registered U‑types where present via **E.10/UTS**.

**Depends on.** A‑kernel (A.1–A.15), **MM‑CHR** (C.16) for measurements, **KD‑CAL** for similarity/corpora, **Sys‑CAL** for carriers, **Decsn‑CAL** (objectives; advisory), **Compose‑CAL** (set aggregation; advisory).

**Coordinates with.** **B.5.2.1** (binding), **C.17 Creativity‑CHR** (characteristics & scales), **C.19 E/E‑LOG** (policies: emitter selection, explore/exploit).

**Exports (CAL; no U‑type minting here).**
 - Records: `NQD.DescriptorMap` (alias of `U.DescriptorMap` if minted), `NQD.NQDArchive` (alias of `U.NQDArchive`), `NQD.Niche`, `NQD.ArchiveCell`, `NQD.EmissionSeed?`, `U.EmitterPolicyRef`, `U.InsertionPolicyRef`, `U.IlluminationSummary`, and `NQD.CandidateSet` (alias of `Set<U.Hypothesis>`).

### C.18:1 - Problem frame
Open‑ended search (NQD) equips FPF with illumination‑style generation and Pareto/portfolio selection in multi‑criteria, partially ordered spaces; it feeds G.5 without scalarising ordinal or mixed‑scale characteristics.

### C.18:2 - Problem
Without a disciplined NQD calculus, contexts (a) conflate illumination telemetry with dominance, (b) lose reproducibility due to undeclared DescriptorMap/DistanceDefRef.editions, and (c) perform illegal aggregations across scales.

### C.18:3 - Forces
• Posets vs. scalarisation — selectors must return sets (Pareto/archive) rather than illegal weighted sums across mixed scales.
• Exploration vs. exploitation — emitters must adapt while preserving provenance and editioning.
• Telemetry metric vs. objective — Illumination (coverage/QD‑score) informs health but is not a dominance characteristic by default.
• Reproducibility vs. adaptivity — budgets, ε, K, and InsertionPolicy must be edition‑tracked.

### C.18:4 - Solution
Provide Γ_nqd.* operators and U.Types for DescriptorMap, Archive/Niche, policies, and illumination telemetry summaries; bind measurement legality to MM‑CHR and policy control to E/E‑LOG. (Exports/Type notes/Operator specs below are normative parts of this Solution.)

- Operators (Γ):
  - `Γ_nqd.generate(seed?, EmitterPolicyRef, Budget, DescriptorMapRef, QualityMeasuresRef, NoveltyMetricRef, CoverageGrid, CellCapacity K=1, EpsilonDominance ε=0, DedupThreshold?, InsertionPolicyRef?) → CandidateSet<U.Hypothesis>`
  - `Γ_nqd.updateArchive(Archive, CandidateSet, InsertionPolicyRef?) → Archive'`
  - `Γ_nqd.illuminate(Archive) → IlluminationSummary{coverage, QD-score, occupancyEntropy, filledCells}` (report‑only telemetry summary; not a dominance characteristic unless a policy explicitly promotes it).
  - `Γ_nqd.selectFront(Archive|CandidateSet, characteristics={Q components, Novelty@context, ΔDiversity_P, …}) → ParetoFront`

**Type notes.**
- `U.DescriptorMap (Tech; twin‑labelled Plain) : Hypothesis → ℝ^d` (declares encoder, invariances, version, **CharacteristicSpaceRef**). Publish Tech/Plain per **E.10**; declare `DescriptorMapRef.edition` and `DistanceDefRef.edition`. **Dimensionality rule.** **Require `d≥2` only when QD/illumination surfaces are active**; for non‑QD contexts `d≥1` is lawful.
- `NQD.CandidateSet` ≡ `Set<U.Hypothesis>` with attached per‑item vectors `{Q_i, N_i, D_i:=ΔDiversity_P, S_i?, provenance_i}`.
- `U.NQDArchive` holds per‑cell elites and genealogy refs; context‑local.
- `U.Niche` is a region in CharacteristicSpace (grid bucket / CVT centroid / cluster).
- `U.EmitterPolicyRef` points to a named policy in **C.19 E/E‑LOG**.
- `U.InsertionPolicyRef` — named archive‑update policy (e.g., `replace_if_better | replace_worst | bounded_age | bounded_regret`); versioned.
- `U.IlluminationSummary` is a **telemetry summary** over `Diversity_P` (see C.17), not a dominance characteristic.

**Operator specs (normative).**
- `Γ_nqd.generate(… )` SHALL:
  (a) respect **Budget**,  
  (b) compute `{Q_i}` (vector), `N_i` (Novelty@context), `D_i := ΔDiversity_P(h_i | Pool)` under the same CharacteristicSpace & TimeWindow as the Pool, and optional `S_i` (Surprise),
  (c) deduplicate by `DedupThreshold` in CharacteristicSpace,  
  (d) record `DescriptorMapRef.edition`, `DistanceDefRef.edition`, `EmitterPolicyRef`, `ε`, `K`, `Seeds`, and genealogy references (parent/seed ids) to enable replay and selection auditing.
- `Γ_nqd.updateArchive` SHALL apply local competition per cell (keep up to K elites), preserve genealogy, and **enact the declared `InsertionPolicyRef`**; default is `replace_if_better` with deterministic tie‑breakers.
- `Γ_nqd.illuminate` SHALL return coverage and QD‑score computed against the declared grid and archive edition.
- `Γ_nqd.selectFront` SHALL compute the (ε‑)Pareto front over the declared characteristics; **Illumination** is excluded by default (report‑only).  

**Pipeline:** apply **Eligibility (ConstraintFit=pass)** → **Dominance (default set from C.19; by default `{Q components}` only)** → **Tie‑breakers (`Novelty@context`, `ΔDiversity_P`, `Surprise`; `Illumination` telemetry metric)**.
**Pure academic QD-mode:** Contexts MAY elect a _pure‑QD_ mode (dominance on `Q` only; `N/ΔD` used via archive occupancy and tie‑breakers). Any deviation SHALL be declared by policy id and recorded in provenance.

**Reproducibility & editions.** Each call SHALL emit provenance sufficient for replay: `{DHCMethodRef.edition, DescriptorMapRef.edition, EmitterPolicyRef (params), **InsertionPolicyRef**, DedupThreshold?, ε, K, Seeds, TimeWindow}`.
Telemetry hook: whenever IlluminationSummary increases (Δcoverage>0 or ΔQD‑score>0), the Context SHALL emit a Telemetry(PathSlice) record that cites {EmitterPolicyRef, DescriptorMapRef.edition, DistanceDefRef.edition, InsertionPolicyRef?, TimeWindow}. (Aligns with G.6/G.7/G.11 portfolio/edition constraints.)

**Measurement alignment.** `Novelty@context`, `Use‑Value (ValueGain)`, `Surprise`, `Diversity_P` SHALL be measured per **C.17** (MM‑CHR templates). **IlluminationSummary** is a telemetry summary over `Diversity_P` (coverage/QD‑score); when CharacteristicSpace includes domain‑family cells, publish grid id and FamilyCoverage, plus **DescriptorMapRef.edition/DistanceDefRef.edition**.
.

### C.18:5 - Conformance Checklist
- **C18‑1** Declare `DescriptorMap` (encoder, invariances, corpus edition) before generation.
- **C18‑1b** When used in F/G triads, DescriptorMap SHALL declare a domain‑family coordinate (grid/cells) and reference an F1‑Card::DistanceDefRef & δ_family.
- **C18‑1c**  When a domain‑family coordinate is declared, the Context SHALL compute and publish **AliasRisk** for each front/portfolio emission, together with the dSig collision rule and the policy id. AliasRisk is computed against `U.DomainDiversitySignature (dSig)`; **the DescriptorMap SHALL publish**: (i) `collisionRuleId` (near‑duplicate threshold, e.g. “≥3 characteristics equal”),  (ii) `dSigSource` pointers used for coding the five characteristics. The collision rule and formula **MUST** be part of `DescriptorMap` provenance (see **Creativity‑CHR**, Heterogeneity Characterisation).
- **C18‑2** Record `EmitterPolicyRef` (policy id from C.19) and parameter set.
- **C18‑3** Compute `D = ΔDiversity_P(h | Pool)` under the same DescriptorMap & TimeWindow as the Pool (see C.17).
- **C18‑4** Exclude Illumination from dominance unless policy explicitly promotes it.
- **C18‑5** Keep `Use‑Value` separate from assurance scores; do not alter `F/G/R` semantics (see B.3, C.17 §Use‑Value).
- **C18‑6** Emit full provenance; thinning after front computation MUST be recorded.
- **C18‑7** Before computing any front, apply **ConstraintFit = pass** as a hard eligibility filter.

**Defaults.** Normative defaults **live in C.19 (EmitterPolicy)** and are **not restated** here. Minimum provenance remains: `DescriptorMapRef.edition` and `DistanceDefRef.edition`, `DHCMethodRef.edition`, `EmitterPolicyRef`, `InsertionPolicyRef`, `TimeWindow`, `Seeds`, `DedupThreshold?`; also record `FamilyCoverage/MinInterFamilyDistance`.

**Didactic quickstart (Context).**
1) Pick 2–4 Quality coordinates and a simple DescriptorMap (2–4 dims).  
2) Set defaults: `K=1`, `ε=0`, a conservative `EmitterPolicy`.  
3) Run `Γ_nqd.generate` to fixed Budget; inspect the front; log coverage (IlluminationSummary).  
4) Apply abductive plausibility filters; promote prime hypothesis to L0.

### C.18:6 - Archetypal Grounding
**System.** Legged‑robot gait exploration: Q = forward speed & energy efficiency (ratio), D = morphology/coordination descriptors (ℝ^d); Archive = CVT grid; Illumination reports coverage without entering dominance.
"**Episteme.** SoTA palette synthesis: Q = Use‑Value proxies per C.17 (ratio/interval as legal), D = method‑family niches; publish DescriptorMapRef.edition and DistanceDefRef.edition for reproducible fronts.

### C.18:7 - Bias‑Annotation
Lexical firewall and notation independence apply; no vendor/tool tokens; ordinal characteristics never averaged; illumination treated as report‑only telemetry unless a policy promotes it. (E.5.1, E.5.2, C.16)

### C.18:8 - Consequences
• Portfolio honesty (no forced scalarisation). • Reproducibility (editioned maps/policies). • Healthy diversity signals via telemetry metrics.

### C.18:9 - Rationale
Post‑2015 Quality‑Diversity (MAP‑Elites & successors) demonstrates illumination efficacy; NQD‑CAL captures these ideas while preserving MM‑CHR legality and LOG governance.

### C.18:10 - Relations
Builds on: C.16, C.2. Coordinates with: B.5.2.1 (binding), C.17, C.19, G.5, G.6, G.11.

### C.18:End

## C.18.1 - Scaling‑Law Lens Binding (SLL)

**One‑screen purpose (manager‑first).**
Make **generation/selection** scale‑savvy: at the level of **conceptual descriptors**, declare (a) **which monotone knobs** we would scale, (b) the **ScaleWindow** over which we claim behaviour, and (c) the **elasticity class** we observed—**without** imposing numeric fits or vendor tools at Core level. This surfaces knees early and keeps comparisons lawful and fair across families. (Parity is handled by **G.9**; illumination remains a **report-only telemetry** unless a CAL policy promotes it.)  

**Builds on.** C.16 (MM‑CHR), C.17 (Creativity‑CHR), C.18 (NQD‑CAL); advisory: C.5 (Resrc‑CAL).
**Coordinates with.** C.19 (E/E‑LOG), G.5 (Selector & Registry), G.9 (Parity Harness), G.10 (Shipping), G.11 (Refresh‑Telemetry), C.24 (Agent‑Tools‑CAL).
**Keywords.** scaling law; **Scale Variables (S)**; ScaleWindow; knee; diminishing returns; **iso‑scale parity**; **UNM/NormalizationMethod‑based mapping**; **scale‑probe**; **DoE** (design‑of‑experiments); segmented regression; knee detection.

### C.18.1:1 - Problem frame

Teams often say a method “**scales**” without disclosing **which resources**, **across what window**, and **how** outcomes respond (convex rise → knee → plateau). Without that, parity is skewed (unequal budgets, unmatched windows), coverage/illumination report-metrics leak into dominance, and “knees” are found late. SLL supplies a notation‑independent **lens** to make scale behaviour explicit and comparable. 

### C.18.1:2 - Problem

Omitting **Scale Variables** and the comparison window causes: (i) **unfair parity** (compute/data/FoA mismatched), (ii) **illumination/coverage report-metric  creep** into dominance by default, (iii) late detection of knees and budget waste. **G.9** already forbids scalarising mixed scales and mandates equal **FreshnessWindows**/**pinned editions**; SLL complements this with **ScaleWindow** & elasticity. 

### C.18.1:3 - Forces

Notation independence vs useful scaling heuristics; local context vs cross‑context generality; **telemetry vs objectives** (illumination stays report‑only telemetry unless policy promotes it); early exploration vs reproducible policy.

### C.18.1:4 - Solution — *binding lens for generator/selector profiles* (normative)

#### C.18.1:4.1 - Types (aliases; ΔKernel = 0).
`SLL.Profile` is an **annotation** on a `MethodFamily/Generator` or a `Selector` profile; **no new U.Types** are minted (LEX discipline). 

#### C.18.1:4.2 - Fields (conceptual descriptors).

* **S — Scale Variables.** Minimal set of **monotone knobs** for the Context: `compute` (steps/tokens/FLOPs/time/energy), `data` (size/quality), `model capacity` (params/branches), `iteration budget`, **`freedom‑of‑action (FoA)`**/**environment richness**, etc. Declare **units** via **Resrc‑CAL** and bind to a **ScaleWindow**. Where training/inference trade, **name the phase** the claim concerns.
* **ScaleWindow.** Declared range of `S` values for which behaviour claims hold (editioned). This is **distinct from** **FreshnessWindow** used by parity. 
* **Scale‑Probe.** At least **two** (preferably **≥ 3**) **parity‑respecting** points in `S` within the ScaleWindow, recorded with **replicates/seeds** and **CI/error bars** to support elasticity classification. Pick points via a **small factorial or Latin‑hypercube** when multiple knobs vary.
* **ElasticityClass** `χ ∈ {rising, knee, flat, declining}` — a **qualitative** class; numeric exponents/fits live in domain annexes, not Core.
* **ParityNotes.** `iso‑scale parity?` flag (and **loss notes** if not achieved), plus **Bridge/Φ/Ψ** IDs when crossing contexts (penalties **route to R only**). 

#### C.18.1:4.3 - Norms (SLL).

* **SLL‑1 (Declaration).** Any profile **claiming scale behaviour SHALL** declare `S` and a **ScaleWindow** for the Context.
* **SLL‑2 (Probe).** Early investigation **SHALL** include a **scale‑probe** (≥ 2 points in `S`, with replicates/CI) and record **χ**. Multi‑knob probes **SHALL** hold unspecified knobs fixed or pinned, and disclose invariants.
* **SLL‑3 (Parity).** Where `S` is declared, comparisons **SHALL** ensure **iso‑scale parity** and lawful **UNM/NormalizationMethod‑based mapping** across heterogeneous knobs (e.g., FLOPs↔tokens) **before** comparing outcomes; **FreshnessWindows/editions** must be equal/pinned per **G.9**. Record **seeds/replicates**, ComparatorSet, and policy‑ids in telemetry/SCR. 
* **SLL‑4 (Selection lens).** Within the **same Context and ScaleWindow**, if other heads (N/U/C) are tied, selectors **MAY** use illumination as a tie‑breaker, but it **SHALL NOT** change default dominance; illumination remains **report‑only telemetry** unless a CAL policy promotes it.
* **SLL‑5 (Knee test).** A **knee** is **claimed** only where a monotone rise is followed by a **statistically significant** slope drop across adjacent probe points within the ScaleWindow; thresholds (e.g., Δslope & CI level) are **policy‑defined** (E/E‑LOG) and must be cited. Absent such evidence, classify as **rising**.
* **SLL‑6 (Telemetry invariants).** Probes **SHALL** export seeds/replicates, edition pins, policy‑ids, and Resrc‑CAL units to **G.11**.

#### C.18.1:4.4 - Method — minimal SoTA probe recipe (notation‑agnostic; informative).
1) **Choose knobs** `S` that are plausibly monotone in the Context (compute/data/capacity/FoA).  
2) **Pick 3–5 probe points** per active knob (edge/mid/edge) under iso‑scale parity; use a **fractional factorial** if >2 knobs.  
3) **Run replicates** (≥ 3 preferred) and **bootstrap** 95% CI on the primary objective(s); log seeds.  
4) **Estimate local slopes** on a log‑log grid; apply **piecewise/segmented regression** or a **knee detector** (e.g., L‑curve/Kneedle) to support `χ`.  
5) **Record invariants** (pinned knobs, safety envelope) and publish **SLL.Card@Context**.  
6) **If χ changes** across the window, split the ScaleWindow and re‑classify per segment.

### C.18.1:5 - Interfaces — minimal I/O (conceptual)

**G.9 Plan/Run Parity** consumes `S`/ScaleWindow to align budgets, **pin editions**, and perform **UNM/NormalizationMethod‑based mapping**; **G.11** carries **policy‑id**, **PathSliceId**, seeds/replicates, CI level, and edition pins per parity CC. 

### C.18.1:6 - Conformance Checklist (CC‑SLL)

1. `S` declared **or** `S = N/A` with rationale.
2. **Scale‑probe** performed; **χ** recorded with **replicates/CI**; invariants disclosed.
3. **iso‑scale parity** or **loss notes** + penalties **→ R only**; editions/seeds pinned; ComparatorSet cited.
4. If used as tie‑breaker, the selector cites **χ** and **lens id** in **E/E‑LOG** provenance.
5. Knee claims cite the **policy threshold** and CI level used.

### C.18.1:7 - Anti‑patterns & remedies

Hidden budget mismatches; averaging ordinals across families; **illumination in dominance by default**; unpinned editions; slope claims without **replicates/CI**; training/inference phase mixing → **cure** with **G.9** parity (equal windows/editions; normalize‑then‑compare; return sets), phase‑label the claim, and record slope uncertainty per Scale‑Audit discipline.  

### C.18.1:8 - Archetypal grounding (post‑2015; informative)

* **LLM scaling.** Kaplan‑style & **Chinchilla‑optimal** regimes; **Mixture‑of‑Experts** and **retrieval‑augmented** families shift effective capacity with different inference budgets; prompt‑policies often transfer better than narrow pipelines.
* **RL/Planning.** Model‑based optimization & general agents vs hand‑tuned controllers; slopes reported wrt budget/FoA under safety envelopes.
* **QD/OEE.** MAP‑Elites, **CMA‑ME**, **DQD**, **QDax**; **POET/Enhanced‑POET** families: coverage/illumination as telemetry metrics; parity uses fixed grids/spaces and edition pins.  

### C.18.1:9 - Payload — exports

`SLL.Card@Context` (UTS row; editioned):
`⟨S{knobs, units, phase}, ScaleWindow, Scale‑Probe{points≥2, design=one‑liner, seeds, CI}, ElasticityClass χ, ParityNotes{iso‑scale?|loss, invariants}, BridgeIds?/Φ/Ψ, PolicyIds? (E/E‑LOG), PathSliceId?⟩`.

**UTS row template (conceptual; pencil‑ready).**
`SLL.Card@Context := S=(COMPUTE|DATA|CAPACITY|FOA; units=…; phase=TRAIN|INFER), ScaleWindow=[LOW…HIGH], Probe=(points=…, design=factorial|LHD, seeds=…, CI=…), χ=rising|knee|flat|declining, ParityNotes=(iso=true|false; invariants=…), Bridge/Φ/Ψ=(…), PolicyIds=(…), PathSliceId=(…)`.

### C.18.1:10 - Relations

**Builds on:** C.16/17/18. **Coordinates with:** C.19 (lenses/policies), **G.5** (set‑returning selector), **G.9** (parity; **ParetoOnly** default; UNM/NormalizationMethod‑based mapping), **G.10** (shipping). 

> *Pedagogical cue.* **Say what you would scale, probe it twice, and use the slope‑class to steer.**

### C.18.1:End

## C.19 - Explore–Exploit Governor (E/E‑LOG)

**Status.** Logic specification (**LOG**). Defines exploration/exploitation policies and selection lenses. **No Γ operators** are exported; policies parameterize calls in **C.18 NQD‑CAL**.

### C.19:1 - Problem frame
The E/E governor provides named, versioned policies and lenses that steer NQD generation/selection under lawful dominance and provenance constraints.

### C.19:2 - Problem
Ad‑hoc exploration mixes ordinal and interval folds, silently scalarises posets, and loses lens/policy provenance—undermining legality and reproducibility.

### C.19:3 - Forces
• Trust gates vs. discovery — graduation requires backstop confidence while maintaining explore_share.
• Heterogeneity vs. focus — fairness quotas by family vs. depth on proven lines.
• Lens expressiveness vs. audit — scalarised choices must not be called 'the frontier' and MUST record lens ids.

### C.19:4 - Solution
Define EmitterPolicy (class, params, ε, K, insertion/dedup) and selection lenses with a fixed pipeline (Eligibility → Dominance → Tie‑breakers); bind provenance (policy id, lens id) and guard promotions of Surprise/Illumination to dominance to explicit policy declarations.

**Agency note.** Decisions are taken by a **system in role**. **Contexts publish** measurement spaces and admissible policies as **semantic frames**; LOG profiles lenses and policies but does **not** enact choices.
**Depends on.** **C.18 NQD‑CAL** (generators), **C.17 Creativity‑CHR** (measurements), **Decsn‑CAL** (objectives/constraints, scalarization lenses), **B.3** (trust adjustments), **Compose‑CAL** (set aggregation; advisory).

**EmitterPolicy (named profile).** A context‑local, versioned policy with fields:
`{ name, class ∈ {UCB, Thompson, BO‑EI, GP‑UCB, PES, …}, params, explore_share∈[0,1], temperature τ≥0, rebalance_period, wild_bet_quota≥0, backstop_confidence (assurance level), epsilon_dominance ε, cell_capacity K, **insertion_policy**, **dedup_threshold** }`.
Policies are referenced as `U.EmitterPolicyRef` by NQD generator call (C.18) and are conceptual lenses, not staffing/budget instructions.

**Defaults (if policy is unspecified):**  
• **Dominance:** `{Q components}` with `ConstraintFit=pass` as **eligibility gate**.  
• **Tie‑breakers:** `Novelty@context`, `ΔDiversity_P`, `Surprise`; `Illumination` (telemetry over Diversity_P: coverage/QD‑score) MAY be used as a tie‑breaker but is **not** in the dominance set.  
• **Archive:** `K=1`, `ε=0`, deduplication in `CharacteristicSpace`.  
• **Policy:** UCB‑class with moderate temperature; `explore_share ≈ 0.3–0.5`.  
• **Provenance (minimum):** record `DescriptorMapRef.edition`, `DistanceDefRef.edition`, `DHCMethodRef.edition`, `EmitterPolicyRef`, `InsertionPolicyRef`, `dedup_threshold?`, `TimeWindow`, `Seeds`.

**Scalarization lenses (policy‑level).** A lens `J_ℓ` declares: (a) hard eligibility conditions (e.g., ConstraintFit=pass), (b) soft aggregation (weights/curves), (c) trust policy (how assurance/CL discounts enter).  
**Conformance.** A Context MUST name the lens used to pick from a frontier; scalarized rankings MUST NOT be presented as “the frontier”; the **`lens id MUST be recorded in provenance of each selection`**.

**Promotion rules (policy).**  
- **Tie‑breaks.**  `Surprise` and `Illumination` MAY act as tie‑breakers; **promotion into the dominance set MUST be declared by lens or policy id** and captured in provenance.
- **Graduation.** Profiles graduate from Explore→Exploit when **backstop_confidence** (B.3 level) and eligibility conditions are met.  
- **Sunset/Pivot.** Profiles failing VOI/backstop thresholds are sunset or pivoted at `rebalance_period`.

**Explore/Exploit loop (per rebalance_period).**
1) Recompute frontier with trust discounts.  
2) Enforce `explore_share` (minimum attention on high‑Novelty, not‑yet‑proven profiles).  
3) Update generator `temperature τ` / emitter mix.  
4) Apply `backstop_confidence` to graduate; sunset stale probes.  
5) Satisfy `wild_bet_quota` by seeding fresh high‑Novelty candidates.
6) HET‑FIRST — apply group‑fairness quotas by domain‑family and/or DPP/Max‑min repulsion before exploit lenses; log quotas and sampler policy id.

**Named lenses (heuristics; policy‑level, not norms)**
The following **lens profiles** are **illustrative heuristics**. Contexts MAY reuse/modify them; they are **not** normative.
• **Frontier‑sweeper** — maintain attention on the full front; promote only when `backstop_confidence` holds.  
• **Barbell** — enforce `explore_share ≥ θ` with a `wild_bet_quota`; otherwise exploit top‑trust region.  
• **Spike‑first** — pick highest **Use‑Value** subject to `ConstraintFit=pass` and a small **Cost‑to‑Probe** cap.  
• **Safety‑first** — minimize **SafetyRisk** subject to `Use‑Value ≥ θ` and `ConstraintFit=pass`.  
• **Platform‑option** — maximize **Option‑Value** under probe cost bounds.  
• **Pilot‑then‑scale** — optimize **Use‑Value** on pilot scope with `BackstopConfidence ≥ L1`; widen `G` once **R** holds.  
• **Heterogeneity‑first (policy id).** Eligibility → Dominance → Tie‑breakers; Hard gate: FamilyCoverage ≥ k, MinInterFamilyDistance ≥ δ_family; Fairness quotas: ≤1 candidate per sub‑family at pre‑front sampling; DPP/Max‑min sampler allowed.
**Conformance (lens recording).** A decision that uses any lens **MUST** record its **lens id** alongside `EmitterPolicyRef`. (This restates and localizes C19‑3.)

### C.19:5 - Conformance Checklist
- **C19‑1** Each NQD generator call (C.18) **SHALL** cite `U.EmitterPolicyRef` (policy id + params) **and the active `InsertionPolicyRef`/`dedup_threshold` when not inherited**.
- **C19‑2** The characteristic set & signs used for dominance **MUST** be declared; eligibility conditions applied first. *(References to C.18 generator operators are descriptive only; LOG exports no Γ.)*
- **C19‑3** If a lens is used, its id MUST be recorded; do not label scalarized top‑1 as “frontier”.  
- **C19‑4** Promotion of Surprise/Illumination into dominance MUST be explicit in policy.  
- **C19‑5** USM/RSG gate applies: policy actions SHALL operate within the Context’s scope and enactable RSG states.
- **C19‑6** Each selection lens **MUST** implement and document the pipeline` Eligibility (ConstraintFit=pass) → Dominance (declared set) → Tie‑breakers (declared)`. Any **promotion** of Surprise/Illumination into the dominance set **MUST** be named by lens/policy id and recorded in provenance.
- **C19‑7 (LEX‑AUTH trigger).** Any change to `EmitterPolicy` defaults that affects domain‑family quotas/samplers (HET‑FIRST), or any change to `DescriptorMap` family coordinates, `DistanceDef`, or the `δ_family` threshold MUST be authored via **E.15 LEX‑AUTH** with a published **LAT**; the DRR SHALL carry the LAT pointer (see **CC‑DRR.6**). Record policy/card ids in SCR.
- **C19‑8**  When the Heterogeneity‑first lens is used, provenance MUST include: (i) the family‑quota vector (including the default triad quota k), (ii) the subFamilyDef id (from F1‑Card) if sub‑family quotas apply, (iii) the sampler class, seed, and policy id.

**Illumination & Diversity_P.** Illumination is **report‑only telemetry over `Diversity_P`** (coverage/QD‑score; published as `IlluminationSummary`). It informs exploration health and tie‑breaks; it is **not** a dominance characteristic by default.

When **Name Cards** (F.18) use NQD-CAL for lexical search, the underlying `DescriptorMap` and `Diversity_P` **MUST** follow the **head-term family** discipline:  
– group label candidates into families by lexical head (base noun/verb, ignoring minor prepositions and inflection);  
– compute `Diversity_P` and any illumination/coverage telemetry over these families (cf. `FamilyCoverage`, `AliasRisk`), not over individual string variants.  
This requirement prevents treating small morphological tweaks of one head as a “diverse” frontier and keeps lexical NQD-fronts honest.

**Baseline profile (informative, context‑local template).**
`EmitterPolicy#NQD-Default-2025`:
    class=`UCB`, explore_share=`0.3–0.5`, temperature `τ=moderate`,
    rebalance_period=`Context default`, wild_bet_quota=`≥0`,
    backstop_confidence=`policy L1`, epsilon_dominance=`ε=0`,
    cell_capacity=`K=1`.
Contexts MAY clone/adjust; if used, record its id in provenance.

**Didactic quickstart (Context).**
- Start with policy class = `UCB` or `Thompson`; set `explore_share≈0.3–0.5`, `τ` moderate.  
- Name the dominance set: `{Q components, Novelty@context, ΔDiversity_P}` with `ConstraintFit=pass` as gate.  
  *(Use‑Value / Cost‑to‑Probe may appear in **lenses** or **constraints**; they are **not** in the default dominance set.)*
- Pick a lens for the final choice (or stick to frontier if undecided); record the lens id in the decision memo.

### C.19:6 - Archetypal Grounding
**System.** Policy‑driven A/B of architectural variants: Eligibility = constraint‑fit; Dominance = {Q components, Novelty@context, ΔDiversity_P}; lens = 'Frontier‑sweeper' vs 'Barbell'.
**Episteme.** Method‑family portfolio in SoTA pack: fairness quotas across traditions; lens id recorded; Illumination used as tie‑breaker only unless promoted.

### C.19:7 - Bias‑Annotation
No global scalarisation of partial orders; ordinal scales excluded from arithmetic; all selections record lens id and policy id; notation/tool neutrality.

### C.19:8 - Consequences
• Transparent exploration budgets. • Repeatable lens‑based selections. • Heterogeneity preserved without illegal aggregates.

### C.19:9 - Rationale
Post‑2015 exploration practice (bandits/BO/RL with QD) shows policies must be explicit, auditable, and editioned; LOG provides that governance.

### C.19:10 - Relations
Builds on: Decsn‑CAL, B.3. Coordinates with: C.18, C.17, G.5, G.9.

### C.19:End

## C.19.1 - Bitter‑Lesson Preference (BLP)

**One‑screen purpose (manager‑first).**
Establish, at **governing policy** level, the empirical **Bitter Lesson**: **prefer general, scale‑amenable methods**—those that improve with **more data/compute/capacity and greater freedom‑of‑action**—over narrow hand‑crafted heuristics **when safety and legality are equal**. Exceptions require a transparent **Scale‑Audit** under the parity harness. 

**Builds on.** C.19 (E/E‑LOG), C.24 (Agent‑Tools‑CAL; **ATC‑2**), B.3 (Assurance), E.3 (Precedence), E.5 (Guard‑Rails).
**Coordinates with.** G.5 (Selector), G.8 (SoS‑LOG Bundles), G.9 (Parity), G.11 (Refresh‑Telemetry), A.0 (On‑Ramp).
**Keywords.** general‑method preference; scale‑amenability; **BLP‑waiver**; iso‑scale parity; **Scale‑Audit**; slope vector; **α/δ tolerances**.

### C.19.1:1 - Problem frame

Bespoke heuristics can win locally but **do not scale**; general methods (search/learning/planning) **improve with scale** and transfer across bridges/planes. Without a standing policy, selectors drift toward hand‑craft and single‑winner leaderboards, violating parity and lawful orders. 

### C.19.1:2 - Policy clauses (normative; synchronized with Core)

**BLP‑1 — Scale‑Audit requirement.**
Any DRR that selects a **narrower/hand‑engineered** method over a **general/scalable** alternative **MUST** include a **Scale‑Audit**:
(a) **Parity harness**: equal **FreshnessWindows**, a common **ComparatorSet**, **replicates/seeds**, **portfolio‑first** evaluation; **Dominance = ParetoOnly** unless a CAL policy says otherwise (policy‑id cited).  
(b) **Budget sweeps**: vary **compute**, **data**, and **FoA** within a fixed safety envelope; **pin** any unsweepable knob and record the invariant. 
(c) **Slopes & uncertainty**: report ∂quality/∂compute, ∂quality/∂data, and (where applicable) ∂coverage/∂FoA, with **CI/error bars** and **edition/policy pins** in telemetry. Use **bootstrapped CIs** or repeated‑seed estimates; disclose heteroscedasticity handling.
(d) **Resources**: publish **Resrc‑CAL** accounts (time/energy/FLOPs) and assurance deltas (B.3). 
(e) **Objective vector**: list **Q/Risk/Cost** and—**only if policy promotes them**—illumination/coverage telemetry metrics. 
(f) **DoE recipe**: for ≥2 active knobs, apply a **fractional factorial** or **Latin‑hypercube** with ≥ 3 levels per knob to avoid aliasing; justify any lower design.  
(g) **Knee & regret tests**: if claiming a heuristic wins, show either (i) a **knee** inside the audited window for the general method (per SLL‑5 policy thresholds) or (ii) **budget‑constrained regret** over the sweep where the heuristic dominates within CI.

**BLP‑2 — Preference rule (with α/δ tolerances).**
Among admissible options with comparable assurance (within **δ**) and budget (within **α**), prefer the method whose **slope vector** **Pareto‑dominates** over the audited range; if no dominance within error bounds, prefer the **more general** method; else resolve by the **E/E‑LOG** tie‑breakers declared in policy. (Agentic contexts implement this as **ATC‑2**; **BLP_delta_α/δ** live in **ATC.Policy**.)  

> **BLP‑2.1 — Valid waiver grounds (override transparency).**
> Overrides of BLP‑2 are allowed **only** when:
> • **Deontic override:** regulation/ethics make the general method inapplicable (E.5/E.3).
> • **Scale‑probe overturn:** under **iso‑scale parity** in the declared **ScaleWindow**, the heuristic **sustainedly outperforms** with uncertainty accounted for.
> • **Complementary bias:** the heuristic is an **inductive bias** that **improves** the general method **without blocking scale** (graceful degradation as `S` grows).
> All overrides record a **BLP‑waiver** with rationale, owner, and expiry/review in the DRR. 

**BLP‑3 — Minimal‑prescription default.**
Author **rules‑as‑prohibitions** (negative constraints) instead of stepwise scripts; encode limits in **Φ policy tables** (and **Φ_plane**) and allow agents to **sequence autonomously** within those constraints. Scripts are permissible only when mandated by safety/regulation or with compelling DRR evidence reviewed under E.3/E.5. 

**BLP‑4 — Heuristic‑Debt register (mandatory).**
Any admitted heuristic is recorded as **Heuristic Debt** with scope, owner, expiry/review window, and a de‑hardening plan; track in **CalibrationLedger/BCT** and cite in SCR. 

**BLP‑5 — Continuous‑learning posture.**
Where product policy allows, enable **feedback‑driven adaptation** (preference learning, critique loops) within Guard‑Rails and privacy controls; disabling adaptation requires DRR justification and review date. 

**BLP‑6 — Precedence & safeguards.**
BLP is constitutional (instantiates **P‑10/P‑11/P‑7/P‑1**), but **does not supersede Guard‑Rails (E.5) or precedence rulings (E.3)**. Where **NQD/E/E‑LOG** promotes illumination into dominance, **BLP adopts that lens** for the audited window.  

**BLP‑7 — Publication discipline.**
Scale‑Audit artefacts **SHALL** be exported to **G.11** with edition pins, CI level, α/δ, ComparatorSet, and **BLP.Policy@Context** reference so downstream selectors can reuse evidence without re‑running audits.

### C.19.1:3 - Conformance Checklist (CC‑BLP)

1. **α/δ tolerances** declared in DRR or via policy profile (and CI level stated).
2. DRR includes a **Scale‑Audit** (BLP‑1a–g) with slopes, **CI**, edition/policy pins, and Resrc‑CAL.
3. Selection cites **BLP‑2** and precedence checks.
4. Any heuristic is logged as **Heuristic‑Debt** with expiry and de‑hardening plan.
5. Authoring defaults to **rules‑as‑prohibitions**; deviations are DRR‑justified and safety‑anchored.
6. **Resrc‑CAL** accounts and assurance deltas reported.
7. **Replicate counts/seeds** and **confidence intervals** recorded for slope estimates; heteroscedasticity handling disclosed.
8. Audit artefacts exported to **G.11** with **BLP.Policy@Context** id.

### C.19.1:4 - Anti‑patterns & remedies

Single‑winner leaderboards; hidden budget mixing; promoting illumination into dominance **without policy**; missing edition pins; heuristics without expiry; slope estimates without CI or with aliased designs → **remedy** with G.9 parity + edition pins, explicit **policy‑ids**, DRR publication, **Heuristic‑Debt** entries, and BLP‑1f DoE discipline. 

### C.19.1:5 - Archetypal grounding (post‑2015; informative)

* **LLMs:** prompt‑programs, **retrieval‑augmented** and **MoE** policies vs narrow task‑specific pipelines; portfolio‑first selection across editions/budgets.
* **RL & planning:** model‑based optimization/general agents vs hand‑coded controllers (subject to α/δ and safety).
* **Preference learning:** **RLHF ↔ DPO** families.
* **QD/OEE:** MAP‑Elites/**CMA‑ME**/**DQD**/**QDax**; **POET/Enhanced‑POET**; illumination remains **report‑only telemetry** unless policy promotes it. 

### C.19.1:6 - Payload — exports

`BLP.Policy@Context` (UTS row; editioned):
`⟨PreferenceDefault, α/δ tolerances + CI, Scale‑Audit recipe (G.9 link; DoE), WaiverRegister{reason, owner, expiry}, E/E‑LOG lens policy‑ids, ATC.PolicyRef? (agentic), G.11.TelemetryPins⟩`.

**UTS row template (conceptual; pencil‑ready).**
`BLP.Policy@Context := PreferenceDefault=(prefer‑general|neutral), α/δ=(α=…, δ=…, CI=…), Scale‑Audit=(parity=G.9; sweep=S={…}; DoE=factorial|LHD; kneeTest=policy‑τ), WaiverRegister=[{reason=…, owner=…, expiry=…}], E/E‑LOG=(policyIds=…), ATC.PolicyRef=(…), TelemetryPins=(edition=…, seeds=…, comparatorSet=…)`.

### C.19.1:7 - Relations

**Depends on:** **G.5/G.9** (selector/parity), **G.11** (refresh telemetry), **C.5** (Resrc‑CAL), **C.18** (NQD‑CAL), **C.19** (E/E‑LOG), **F.7/F.9** (Bridges, CL/Φ/Ψ). **Constrained by:** **E.5** Guard‑Rails and **E.3** precedence. 

> *Memory hook.* **Prefer what scales; explain when you don’t.**

### C.19.1:End

## C.20 - Composition of `U.Discipline` (Discipline‑CAL)

**Builds on.** **C.2 KD‑CAL** (F–G–R & CL routing), **A.19/G.0 CG‑Spec** (comparability), **F.9 Bridges** (cross‑Context alignment), **E.10 LEX** (registers & twin labels). **Coordinates with.** **C.21** (Discipline‑CHR, field health), **C.23** (Method‑SoS‑LOG), **F.17–F.18** (UTS). 

### C.20:1 - Problem Frame
Disciplines persist as *knowledge canons* (epistemes), *codified practices & standards*, and *institutional carriers* (journals, bodies, curricula). FPF needs a typed, provenance‑preserving way to **compose** these into a reusable **holon of talk** that travels across contexts *lawfully*. Composition must honour KD‑CAL lanes and the CG‑Spec Standard so that any numeric comparison or aggregation remains auditable and legal.

### C.20:2 - Problem
Without a **composition calculus** for disciplines:
* fields degenerate into labels; editions and rival **Traditions/Lineages** blur;  
* cross‑Context reuse silently drops meaning (no Bridge/CL), or performs illegal aggregations (means on ordinals; unit mixing);  
* selectors (Part G) cannot lawfully gate methods because maturity/evidence are not tied to a field’s canon and carriers.

### C.20:3 - Forces
| Force | Tension |
|---|---|
| **Pluralism vs Cohesion** | Rival traditions must co‑exist ↔ a discipline holon must present a coherent public surface. |
| **Locality vs Federation** | Meaning is context‑local (rooms) ↔ reuse needs Bridges with CL and recorded loss notes. |
| **Rigor vs Agility** | CG‑Spec legality, KD‑CAL lanes ↔ practical authoring and edition flow (UTS/DRR). |
| **Didactic surface vs Assurance depth** | Human‑readable Discipline Card ↔ auditable F–G–R & provenance. |

### C.20:4 - Solution — the **Discipline holon** and Γ_disc

#### C.20:4.1 - U.Types (minting & registers)
* **`U.Discipline`** — a **Holon** that composes an **EpistemeCanon**, **Standards/Practices**, and **Organisational Carriers** into a durable **unit of talk** (R‑core name; twin labels).  
* **`U.AppliedDiscipline`**, **`U.Transdiscipline`** — subtypes of `U.Discipline`.  (**Kernel U‑types; LEX‑governed**).
* **`U.Tradition`**, **`U.Lineage`** — auxiliary holons that organise variants/editions within a `U.Discipline`.  

**Placement/LEX.** `U.Discipline` and its subtypes are **Kernel U‑types** introduced under the **Open‑Ended Kernel** & **Ontological Parsimony** guards (**A.5**, **A.11**) and registered per **E.10/F.17**. This CAL **uses** them, it does not redefine them. If not yet present in A‑cluster, mark as **“provisionally minted”** and open a DRR to finalize placement (E.10 V‑ladder). 

All are **UTS‑published** with **twin labels**; minting follows **E.10** registers/prefix policy and **A.11** parsimony.

#### C.20:4.2 - What a `U.Discipline` is / is not
* A `U.Discipline` is **not** a `U.BoundedContext` and **not** a **Domain**. **Domain** remains a *catalog label* (stitched to D.CTX + UTS): **Discipline ≠ Domain** is enforceable via **E.10 LexicalCheck**; any cross‑Domain/Context reuse **MUST** cite a **Bridge (F.9) + CL + loss notes**; penalties to **R** only; **F/G invariant** (USM/KD‑CAL). 
* **Comparability** of a discipline flows **only through** the discipline’s **CG‑Spec** entries (no ad‑hoc formulas).  
* Cross‑Context/Tradition reuse **MUST** use **Bridge(s)** with **CL** and loss notes; **CL penalties route to R** (KD‑CAL/B.3); **F/G remain invariant**.  
* Public naming surfaces obey **LEX** (I/D/S; twin labels; banned heads); “discipline column” is **didactic only** and **carries no semantics** (enforced by LexicalCheck).

#### C.20:4.3 - Constructor **Γ_disc** (CAL export)
*Signature.*  
`Γ_disc : ⟨EpistemeCanon, StandardsSet, OrgCarriers, {Bridges}, Policy⟩ → U.Discipline`  
*Intent.* Fold the three constituents into a `U.Discipline`, **preserving provenance**, publishing UTS cards, and enabling lawful comparability via referenced **CG‑Spec** rows.  
*Obligations.*  
1) **Provenance & lanes.** Each imported episteme/standard declares **A.10 anchors** and lane tags **{TA, VA, LA}**; freshness windows are recorded.  
2) **Assurance fold.** Use KD‑CAL weakest‑link on R with **Φ(CL)** (and, where applicable, **Φ_plane** for ReferencePlane crossings) **table‑backed and monotone**; publish policy ids. For any justification **path P**, compute **`R_eff(P) = max(0, min_i R_i − Φ(CL_min(P)))`**; for parallel independent lines to the *same* claim take **`R(Γ) = max_P R_eff(P)`**; **`F(Γ)=min`** along used paths. No thresholds inside CHR/CAL (Acceptance‑only). Unknowns propagate as {pass|degrade|abstain} to Acceptance. 
3) **CG‑Spec guard.** Any numeric comparison/aggregation in Discipline reports **MUST** cite the discipline’s **CG‑Spec** with lawful **ScaleComplianceProfile (SCP)**, **Γ‑fold**, and **MinimalEvidence**; units/scale/polarity legality via **MM‑CHR/CSLC** precedes aggregation.  
4) **Scale/Unit/Polarity legality.** Before any comparison/aggregation, **prove legality via MM‑CHR/CSLC** and cite **CG‑Spec characteristic ids** used in the fold (A.17–A.19).
5) **ReferencePlane guard.** When crossings touch `world|concept|episteme`, apply **CL_meta** and route penalties to **R** only; record **plane** on the UTS row.
6) **Edition discipline.** Changes to canons/standards that alter computed ⟨F,G,R⟩ **create a new edition**; DRR captures the rationale; UTS lifecycle records transitions.  
7) **No stealth globalisation.** Cross‑Context mappings are **by Bridge only**; “by‑name reuse” is forbidden** even with similar labels.

#### C.20:4.4 - Discipline ESG (state graph, informative surface)

Export a **Discipline.ESG** with named states and guarded transitions (e.g., *Emerging → Consolidating → Codified → Fragmenting*), where **guards reference C.21 metrics** (CHR‑typed; **Scale/Unit/Polarity + freshness windows**) and cite **CG‑Spec ids**; **all thresholds live only in AcceptanceClauses** (G.4). ESG is **descriptive**; all gating remains in CHR/CAL/LOG packs.

### C.20:5 - Archetypal Grounding *(Tell–Show–Show)*

| Slot | **System** (safety code in a factory) | **Episteme** (discipline canon across editions) |
|---|---|---|
| **Object** | Production line with hazardous operations | “Safety engineering” as *describedEntity target* (accident models, tolerable risk) |
| **Concept** | Acceptance clauses & evaluation templates bound to rigs/windows | Canon texts: causality models, design rules, proofs/benchmarks (e.g., **formal knowledge bases**, **proof artefacts**, **concept schemas**) |
| **Symbol** | Local SOP/notation sets for checklists | Notation packages (CLIF, RDF/TriG, proof scripts) |
| **Γ_disc assembly** | Fold {line‑specific standard, plant procedures, certifying unit} into **`Discipline: Safety‑Plant‑A`** | Fold {canon papers, formal models, journals/committee} into **`Discipline: Safety‑Engineering`** with **Traditions** (e.g., system safety vs resilience engineering) |
| **Evidence lanes** | LA test campaigns (freshness windows), VA design proofs, TA tool quals | VA proofs over kinds, LA replications/meta‑analyses; TA for checkers |

### C.20:6 - Bias‑Annotation
**Lenses:** Governance (naming/UTS), Architecture (CAL+CHR split), Onto/Epist (discipline ≠ domain; triangle fidelity), Pragmatic (authoring/editions), Didactic (twin labels; System/Episteme scenes). **Scope:** context‑local; no “global discipline”.

### C.20:7 - Conformance Checklist (normative)
| ID | Requirement | Purpose |
|---|---|---|
| **CC‑C20‑1 (CG‑Spec linkage).** | A `U.Discipline` **SHALL** declare the **CG‑Spec** ids and **CHR characteristic ids** behind any comparison/aggregation; thresholds live only in **Acceptance** clauses referenced by those CG‑Specs. | Auditable comparability; no illegal ops. |
| **CC‑C20‑2 (Bridge‑only reuse).** | Any cross‑Context/Tradition use **SHALL** cite **Bridge id + CL + loss notes**; penalties **route to R only**; **F/G invariant**. | Prevent silent globalisation; align with KD‑CAL. |
| **CC‑C20‑3 (ReferencePlane).** For any crossing touching `world|concept|episteme`, **publish plane** and apply **Φ(CL)** (and **Φ_plane**, where applicable) — both **MUST** be **monotone, bounded, table‑backed**; **unknowns** propagate as **{pass|degrade|abstain}** into **Acceptance** with **SCR note**; **no silent `unknown→0`**. |
| **CC‑C20‑4 (Γ_disc integrity).** | `Γ_disc` **MUST** record lane tags and freshness windows for all imported evidence; **Φ(CL)** **MUST** be monotone and table‑backed per policy. | Deterministic assurance; hygiene of penalties. |
| **CC‑C20‑5 (Edition & DRR).** | Discipline editions **SHALL** be recorded via **UTS lifecycle** with DRR links; no silent rewrites or renames. | Traceable evolution. |
| **CC‑C20‑6 (LEX/I‑D‑S).** | `U.Discipline` names **SHALL** follow **LEX** (twin labels; registers; banned heads). **Domain** mentions are catalog‑only. | Register hygiene; avoid “Domain = Discipline”. |
| **CC‑C20‑7 (Crossing visibility hooks).** | Any **cross‑stance / cross‑Context / cross‑plane** reference in Discipline materials **SHALL** publish a **CrossingSurface** for the crossing (**E.18**; Bridge+UTS **A.27**; BridgeCard **F.9**) and expose it via `Expose_CrossingHooks` (**G.10‑3**). Published crossings **MUST** be checkable for **LanePurity** (CL→R only; F/G invariant; Φ tables present) and **Lexical SD** (**E.10**) under the active GateProfile / GateChecks (**A.21**). | Prevents implied crossings; makes provenance auditable & replayable. |
| **CC‑C20‑8 (Discipline column is didactic).** | Any use of a “discipline column” in tables is **didactic only**; semantics are carried by **UTS rows + Bridges**; **Domain** remains a catalog stitch (**E.10/F.17**). |  |
| **CC‑C20‑9 (Lexical firewall).** | Normative sections remain **notation/tool‑neutral**; vendor/tool tokens are avoided (see **E.5.1**). |  |

#### C.20:7.1 - Canonical rewrites (anti‑ambiguity)
* “TDD discipline” → **`Tradition: Test‑Driven`** *(Plain twin keeps “Tradition”)*.  
* “Safety Discipline Owner” → **`Holder#DisciplineStewardRole:Safety‑Context`**.  
* “ClinicalSafetyDomain Governance” → **`DisciplineSpec: Clinical‑Safety`** with comparability in **CG‑Spec**; the **Domain** mention remains a **D.CTX + UTS** catalog stitch.

### C.20:8 - Consequences
**Benefits.** Auditable field composition; lawful federation across traditions; selector‑ready maturity/evidence linkage; didactic surface for stewardship.  
+**Trade‑offs.** Discipline authoring requires CG‑Spec literacy and Bridge hygiene; paid back by safe reuse and clearer governance.

### C.20:9 - Rationale
The calculus keeps **describedEntity local**, **comparability lawful**, and **assurance explicit**. It aligns with KD‑CAL’s weak‑link folds and CL routing, with CG‑Spec’s **ScaleComplianceProfile (SCP)** and **Γ‑fold** rules, and with LEX twin‑label governance. It avoids “phlogiston disciplines” by tying fields to measurable CHRs (C.21) and evidence lanes.

### C.20:10 - Relations
**Builds on.** KD‑CAL (C.2); CG‑Spec (A.19/G.0); Bridges (F.9); LEX (E.10).  
**Coordinates with.** C.21 (field‑health CHRs), C.22 (Problem‑CHR), C.23 (Method‑SoS‑LOG).  
**Constrains.** G.2 **MUST** publish **TraditionCards**/**BridgeMatrix** sufficient for `Γ_disc` to assemble **≥2 Traditions** and **≥3 `U.BoundedContext`** per SoTA synthesis to avoid monoculture. G.5 selector **SHALL** cite Discipline **CG‑Spec ids** and **EvidenceGraph** rows when admitting families.

### C.20:End

## C.21 - Field Health & Structure (Discipline-CHR)

> *Purpose.* Give FPF a **typed, auditable** way to speak about the *health, maturity, and structure* of a scientific/engineering **discipline**, without collapsing into taste, anecdotes, or single-number scores. The pattern defines a **portable set of Characteristics** and guards (legality, freshness, scope) that any Context can specialize.

*This pattern supplies the CHR “vocabulary of health” for disciplines. C.20 composes the discipline; C.21 measures its health; Part G (G.2, G.12) harvests SoTA and operationalizes dashboards; Bridges keep meaning honest; penalties touch **R** only.*

 **Status & placement.** Part C (Kernel Extention Specifications) → Cluster C.I (Core CHRs/CALs). 
  **Depends on:** **MM-CHR** (C.16), **KD-CAL** (C.2), **USM/Scope** (A.2.6), **Trust & Assurance** (B.3), **E.10 (LEX‑BUNDLE)**. 
  **Coordinates with:** **C.20 Discipline‑CAL** (what a `U.Discipline` is), **G.2** (SoTA palette), **G.12** (dashboard), **G.0** (CG‑Spec registry).

### C.21:1 - Problem Frame

FPF treats *disciplines* as first-class holons (see **C.20**): they aggregate epistemes, practices, standards, institutions, and observed Work. Teams routinely say “the field is fragmented,” “standards are converging,” or “replication is improving,” but these claims are rarely **typed** (scale/unit/polarity) or **auditable** (evidence lanes, freshness, scope). C.21 supplies the CHR layer—named Characteristics with CSLC typing—so disciplines can be compared lawfully (CG‑Spec) and monitored through time (G.12).  Each published value MUST declare ReferencePlane ∈ {world|concept|episteme} and DisciplineId (U.Discipline@UTS); cross‑plane use applies CL^plane in Assurance (penalty to R_eff only). 

### C.21:2 - Problem

Narrative health claims cause three recurrent failure modes:

1. **Illegality.** Averaging ordinals, mixing units, or comparing incommensurate Contexts ⇒ nonsense roll-ups.
2. **Staleness.** Health “scores” rarely declare **freshness windows** or evidence lanes (TA/VA/LA).
3. **Scope slippage.** “The field” is left implicit; cross-Context reuse lacks **Bridges & CL**, leading to silent semantic loss. Any numeric comparison/aggregation MUST cite a **CG‑Spec** row (characteristics, lawful **ScaleComplianceProfile (SCP)**, **Γ‑fold**, MinimalEvidence) before computation.

### C.21:3 - Forces

| Force                            | Tension                                                                                                                    |
| -------------------------------- | -------------------------------------------------------------------------------------------------------------------------- |
| **Comparability vs nuance**      | Need global pictures without erasing local meaning (Context, traditions, cohorts).                                         |
| **Ordinal vs interval/ratio**    | Powerful stats tempt illegal ops on ranks and categories.                                                                  |
| **Local evidence vs federation** | Health must be computed *in room* (Context slice) yet projectable across rooms via Bridges & CL (penalties to **R** only). |
| **Recency vs stability**         | Health evolves; dashboards must reflect **freshness**, not just cumulative history.                                        |

### C.21:4 - Solution — **Discipline Health Characterisation (DHC)**

#### C.21:4.0 - Ontology quick sheet (normative, clarifying)
**What “DHC” is.** DHC is a **CHR vocabulary pack** (intensional) that defines **Characteristics** + **Scales/Units/Polarity** for discipline health; it is not a document or a run.
**Artifacts.**
• **`U.DHCPack`** (I‑layer name; published as an episteme): the **slot set** (Characteristic/Scale declarations) for a Context.  
• **`U.DHCMethodSpec`** (S‑layer): the **computational specification(s)** for deriving each DHC slot (e.g., replication‑window definition, CD‑index class), table‑backed; multiple per slot allowed, editioned separately.  
• **`U.DHCSeries`** (episteme w/ `EditionSeries`): a **time‑indexed publication** of computed DHC readings for a Discipline×Context, each value bound to `…Ref.edition` for every referenced method/metric/distance.
**Edition subjects.**  
(i) **DHCPack.edition** — when the **slot semantics** (Characteristic/Scale) change.  
(ii) **DHCMethodSpecRef.edition** — when a **computation method** (formula/class/policy) changes.  
(iii) **DHCSeries.edition** — when the **published series** changes its content (not carriers).  
**Publication.** Releases are **Work** on Carriers; **no** edition change unless content changes per `U.EditionSeries`.  
**Ref discipline.** All bindings to packs/methods/distances **SHALL** use `…Ref.edition` (dot on the Ref).

Define a **portable minimal set** of CHR **slots**. Each slot is **CHR-typed** (Characteristic, Scale/Unit/Polarity per **A.17–A.18**), **Context-local**, and guarded by **USM** (Claim scope **G**), **freshness windows**, and **evidence lanes** (TA/VA/LA).  Contexts MAY extend the set; MUST NOT alter scale types illegally. 

**“Health” is a vector** of CHR‑typed coordinates; **no single scalar** is implied. Lawful scalarization lives in **Acceptance** (G.4) under an explicit **CG‑Spec ScaleComplianceProfile (SCP)** and **Γ‑fold** rules, and is never embedded in CHR.

#### C.21:4.1 - Core Characteristics (kernel-portable names)

1. **ReproducibilityRate** *(ratio ∈ [0,1]; polarity ↑; ReferencePlane=episteme; CG‑Spec‑bound)*
   Fraction of tested claims/benchmarks that independent teams **replicate** under a declared **ContextSlice** and **Γ\_time** window. **Lane tags:** LA (validation) with TA (typing) for protocols.

2. **StandardisationLevel** *(ordinal; polarity ↑; ReferencePlane=episteme)*
   {none, *emerging*, *de facto*, *de jure*}. **No mean.** Use medoid/mode; legal comparisons are ≤/=/> only. Tracks convergence on vocabularies, interfaces, or procedures.

3. **AlignmentDensity** *(ratio; polarity ↑; ReferencePlane=episteme; CG‑Spec‑bound)*  
   Density of **Substitution Bridges** (same **senseFamily**, CL≥2) between major `U.Tradition`s **per 100 DHC‑SenseCells** (G.2 F‑hooks) in the SoTA palette.  Substitution rule:  free substitution permitted at **CL=3**; at **CL=2** substitute only with extra‑guard (count in reporting, but this is not «free substitution») Units: `bridges_per_100_cells`. Cross‑Context use requires Bridge+CL; penalties → **R_eff** only.

 4. **DisruptionBalance** *(interval; polarity = target band; ReferencePlane=episteme; CG‑Spec‑bound)*  
  Relative share of **disruptive vs consolidating** works within **Γ_time** using a **registered CD‑index class** (editioned; cite **method id** in UTS). **Default plane:** *episteme*. Publish the **target band** via **Acceptance (G.4)**; not in CHR.
   
  5. **EvidenceGranularity** *(Context-declared: ordinal|ratio; polarity ↑; ReferencePlane=episteme)*  
   If ratio: units = `claims_per_artifact` or `anchors_per_claim` (declare). If ordinal: publish level names and **ORD_COMPARE_ONLY**.
   Fineness of evidential units and declared envelopes (experiment cards, benchmark tasks, audit granules). Encourages *smaller, well-scoped* claims over monoliths.

  6. **MetaDiversity** *(portfolio dispersion; polarity ↑ to band; ReferencePlane=episteme; CG‑Spec‑bound)*  
  Use entropy/HHI **over MethodFamily/Tradition shares** (method edition id in UTS); publish **guard‑band** as **Acceptance** binding; cross‑ordinal scalarisation is forbidden.
  Entropy/Herfindahl-type dispersion across `U.Tradition`s, method families, or data regimes, bounded by a **Context-declared guard-band** (too low ⇒ monoculture; too high ⇒ incoherence).

> **Typing & legality.** Each slot **MUST** declare **Scale/Unit/Polarity**; illegal ops (e.g., mean on ordinals; unit mixing) are **fail-fast** per **A.18/MM-CHR**.

#### C.21:4.2 - Guard Macros (normative)

* **ORD\_COMPARE\_ONLY(x)** — for **StandardisationLevel** (ordinal).
* **UNIT\_CHECK(x)** — forbid cross-unit aggregation (AlignmentDensity, ReproducibilityRate).
* **POLARITY_CHECK(x)** — enforce declared polarity (↑/↓/target-band) per MM‑CHR.
* **FRESHNESS(x; window)** — ensure values come from evidence within declared **Γ_time**; record **valid_until**; stale ⇒ {degrade|abstain} at Acceptance.
* **PLANE_NOTE(x)** — record **ReferencePlane**; compute **CL^plane** on crossings; penalties → **R_eff** only.
* **LANE\_TAGS(x; {TA|VA|LA})** — annotate contribution lanes.
* **SCOPE\_COVERS(x; TargetSlice)** — enforce **USM** coverage of the computation.
* **BRIDGE_CL(x; id, CL≥k)** — on cross‑Context roll‑ups, require **Bridge** with **CL**; penalties route to **R** only. If planes differ, apply **CL^plane** and cite **Φ_plane** policy id. **Hint:** for **AlignmentDensity** reporting, set **k=2** (CL≥2); **CL=3** counts as *free substitution*.

#### C.21:4.3 - Legality Matrix (extract)

| Operation     | ReproducibilityRate (ratio) | StandardisationLevel (ordinal) | AlignmentDensity (ratio) | DisruptionBalance (interval) |
| ------------- | --------------------------: | -----------------------------: | -----------------------: | ---------------------------: |
| mean          |                      **OK** |                     **FORBID** |                   **OK** |                       **OK** |
| median        |                          OK |                         **OK** |                       OK |                           OK |
| compare (<,>) |                          OK |                         **OK** |                       OK |                           OK |
| unit mix      |                  **FORBID** |                            n/a |               **FORBID** |                          n/a |

*Note:* For **MetaDiversity/EvidenceGranularity (ordinal)** use **median/mode**; forbid affine ops; unit mix always fails.

### C.21:5 - Interfaces & Data Paths

* **Inputs.** `U.Discipline` from **C.20** (composition), SoTA **Palette**/**BridgeMatrix** from **G.2** (**DHC‑SenseCells** included), EvidenceProfiles from **G.4/G.6**.
* **Outputs.** Per‑Context **DHC rows** (these six slots), **UTS** Name Cards with twin labels (E.5/F.17–F.18), **Registry/RSCR hooks** on method edition changes; feeds **G.12** (time‑series).
* **Cross-Context reuse.** Only via **F.9 Bridges** with **CL** and **loss notes**; **Φ(CL)** penalties applied to **R** (never F/G).

### C.21:6 - Archetypal Grounding (three fields)

#### C.21:6.1 - Computer Vision (Benchmarks 2015→)
* **ReproducibilityRate.** Ratio of independently reproduced results on ImageNet-style tasks within **rolling 24 mo** (LA lane).
* **StandardisationLevel.** *de facto* for dataset specs and metrics in *Vision\_2024*; *emerging* for robustness protocols.
* **DisruptionBalance.** Use an editioned CD‑index class (e.g., Wu‑style disruption family) with method id; publish target band via Acceptance; annotate ReferencePlane=episteme.
* **AlignmentDensity.** Bridges with **CL≥2** across sub-traditions (supervised vs self-supervised).
* **MetaDiversity.** Entropy across method families (CNN/ViT/Hybrid) kept within guard-band to avoid monoculture.

#### C.21:6.2 - Biomedicine (Gene–Disease Associations)
* **ReproducibilityRate.** Fraction of associations replicated in independent cohorts within **Γ\_time(36 mo)**; LA lane with TA (typing of protocols).
* **StandardisationLevel.** *de jure* for certain reporting guidelines; *emerging* for pre-registration norms.
* **EvidenceGranularity.** Move from “paper-level” to *claim-level* units (Context raises the score).
* **DisruptionBalance.** Target band discourages sustained “novelty spikes” unbacked by replication.

#### C.21:6.3 - Software Performance Engineering (SPE)
* **StandardisationLevel.** *emerging* → *de facto* for SLO taxonomies and trace schemas across vendors.
* **AlignmentDensity.** CL-rated Bridges between tracing ecosystems.
* **ReproducibilityRate.** Share of publicly replicable perf claims in rolling windows.
* **MetaDiversity.** Balance across load models, failure modes, and toolchains.

#### C.21:6.4 - Decision‑Making (2015→)
• ReproducibilityRate — share of causal effect estimates replicated across independent datasets within Γ_time; LA lane.
• StandardisationLevel — *emerging* for identification checklists; *de facto* for SCM notation in leading stacks (ordinal; no means).
• AlignmentDensity — CL‑rated Bridges between SCM/DoWhy‑style and RL/BO traditions per 100 DHC‑SenseCells.
• MetaDiversity — dispersion across method families (SCM/RL/BO/DT) within guard‑band; entropy/HHI (units declared in CG‑Spec).

#### C.21:6.5 - Evolutionary Architecture (software)
• ReproducibilityRate — fraction of architecture fitness results reproduced on independent workloads (rolling 18–24 mo; LA lane).
• StandardisationLevel — *de facto* for ADR/ATAM patterns; *emerging* for continuous fitness protocols.
• AlignmentDensity — Bridges across ATAM/SAAM/ADR style guides (CL≥2) normalised per 100 DHC‑SenseCells.
• MetaDiversity — portfolio dispersion across patterns (microservices, event‑driven, layered) with guard‑bands; no ordinal arithmetic.

### C.21:7 - Measurement & Publication Procedure (authoring harness)

1. **Declare Context & TargetSlice.** (USM) Name editions, Standards, env params, `Γ_time`.
2. **Collect evidence.** Bind sources via **G.6 EvidenceGraph**; tag lanes and freshness.
3. **Compute DHC slots.** Enforce **Legality Matrix** and Guard Macros.
4. **Bridge (if needed).** Map via **F.9**; attach **CL** and **loss notes**; apply **R** penalties.
5. **Publish to UTS.** Name Cards (Tech/Plain), twin labels; **bind `DHCMethodSpecRef.edition`**, `DistanceDefRef.edition`, and, where templates are used, `DHCMethodRef.edition`; register RSCR triggers (method change, ScoringMethod/NormalizationMethod edits).
6. **Dashboard.** Feed G.12 with time-series and guard-bands (disruption, diversity).

### C.21:8 - Bias-Annotation (E-cluster lenses)

* **Didactic.** Plain names + twin labels; one-screen tables for managers.
* **Architectural.** No ordinals averaged; all cross-Context movement goes through Bridges+CL; penalties never touch F/G.
* **Pragmatic.** Freshness-aware; unknowns tri-state; values are decision-support, not trophies.
* **Epistemic.** Evidence lanes explicit; reproducibility is LA, typing is TA; validation distinct from verification in dashboards.

### C.21:9 - Conformance Checklist (normative)

**CC-C.21-1 (CHR typing).** Every DHC slot **MUST** declare **Characteristic + Scale/Unit/Polarity**, with CSLC legality proved before any aggregation.
**CC-C.21-2 (Freshness).** Published values MUST carry Γ_time selector and freshness window; stale rows escalate to {degrade|abstain} in **G.4 Acceptance**.
**CC-C.21-3 (Plane).** ReferencePlane declared; cross‑plane re‑use publishes **CL^plane** (policy id) alongside CL; both penalties route to **R_eff**.
**CC‑C.21‑4 (DesignRunTag).** Every DHC row SHALL declare **DesignRunTag ∈ {design, run}**; design‑ and run‑characteristics **not mixing** in one value/aggregate.
**CC-C.21-5 (Lane tags).** Each value **MUST** tag **TA/VA/LA** lanes of contributing evidence.
**CC-C.21-6 (Ordinal discipline).** **StandardisationLevel** is ordinal; **no means**, **no z-scores**.
**CC-C.21-7 (Scope).** All computations declare **TargetSlice**; **USM** membership is decidable and deterministic.
**CC-C.21-8 (Bridges).** Cross-Context comparisons/publishers **MUST** cite **Bridge id + CL**; penalties route to **R\_eff**, never to F/G.
**CC-C.21-9 (UTS).** Publish DHC rows as **UTS Name Cards** with **twin labels** (Tech/Plain).
**CC‑C.21‑10 (Registry).** DHC methods are table-backed; silent method changes are forbidden (**bump `DHCMethodSpecRef.edition` + RSCR trigger**). 
**CC-C.21-11 (Unknowns).** Unknown inputs propagate tri-state {pass|degrade|abstain} to Acceptance; **no `unknown→0` coercion**.
**CC-C.21-12 (No tool/vendor tokens).** Core narrative follows **E.5.1** (Lexical Firewall).
**CC-C.21-13 (CG‑Spec citation).** Any numeric operation (comparison/aggregation) in DHC **MUST** refer to **CG‑Spec** (characteristics, **ScaleComplianceProfile (SCP)**, **Γ‑fold**, MinimalEvidence).
**CC-C.21-14 (Φ‑policies).** **Φ(CL)** and **Φ_plane** — **monotone** and **table‑backed**; published by policy id.
**CC‑C.21‑15 (Ref discipline).** Any edition pinning **SHALL** appear as `…Ref.edition` on the relevant reference field (DHCPack/MethodSpec/DistanceDef/DHCMethodRef); bare `…Edition` fields are non‑conformant.
**CC‑C.21‑16 (Role kit, informative).** Use standard roles from F.4: `DisciplineStewardRole` (governs DHCPack), `DHCMethodAuthorRole`, `DHCSeriesPublisherRole`. Roles are **design‑time**; values are **run‑ or design‑stance** per slot and must declare **ReferencePlane**.

### C.21:10 - Consequences

**Benefits.** Lawful comparisons; freshness-aware governance; explicit cross-tradition alignment; dashboards that don’t lie by averaging ranks.
**Costs.** Some ceremony (scales, windows, lanes, bridges), offset by template macros and UTS automation.
**Risks avoided.** “Phlogiston disciplines” (charisma-driven fields) fail DHC audits; **No-Free-Lunch** preserved by G.5 (selector returns sets, not universal scalars).

### C.21:11 - Rationale (post-2015 signals & practice)

* **Replication & credibility (2015→).** Field-level health in SciSci emphasizes **replicability**, *fresh* evidence windows, and claim-level units—captured by **ReproducibilityRate** and **EvidenceGranularity**.
* **Disruption vs consolidation (2019→).** Empirical “disruption indices” distinguish papers that open new lines from those that refine—hence **DisruptionBalance** with *target bands*, not monotone “more is better.”
* **Standardization waves (2016→).** Package/ecosystem norms show ordinal trajectories (none→emerging→de facto→de jure); **ordinal typing** prevents illegal arithmetic.
* **Plural traditions (ongoing).** Mature fields maintain **bridges** with explicit **loss notes**; **AlignmentDensity** rewards CL-rated bridges without semantic collapse.

*(Names are illustrative of contemporary practice; the CHR is notation-agnostic and tool-neutral.)*

### C.21:12 - Relations

* **Builds on:** **A.17–A.18** (Characteristic/CSLC), **A.2.6** (USM scopes), **B.3** (assurance lanes), **C.16** (MM-CHR templates).
* **Coordinates with:** **C.20** (what a `U.Discipline` *is*), **G.2** (SoTA palette and BridgeMatrix), **G.12** (Dashboard operationalization), **G.9** (parity harness for fair comparisons).
* **Constrains:** **G.10** (pack ships DHC rows + method ids), **G.11** (refresh windows/decay), **G.5** (selector may reference DHC only via admissible predicates; no cross‑ordinal scalarisation). **Coordinates:** **F.9** (Bridges for cross‑Tradition comparisons).

### C.21:13 - Annex — Author’s quick template (copy-paste)

```
C.21.DHC(Context: <name/edition>; TargetSlice: <tuple>; Γ_time: <policy>)
  ReproducibilityRate:
    value: <0..1>   lane: LA   window: <…>   scope: <…>
  StandardisationLevel:
    value: {none|emerging|de_facto|de_jure}   compare_only: true
  AlignmentDensity:
    value: <ratio>   units: bridges_per_100_DHC_SenseCells   CL_min: 2   scope: <…>
  DisruptionBalance:
    value: <−1..1>   method: <CD-index class / edition>   target_band: [l,u]
  EvidenceGranularity:
    value: <ordinal|ratio per Context>   notes: <…>
  MetaDiversity:
    value: <entropy/HHI>   target_band: [l,u]
Guards: ORD_COMPARE_ONLY(StandardisationLevel), UNIT_CHECK(*), FRESHNESS(*), LANE_TAGS, SCOPE_COVERS, BRIDGE_CL(if x-Context)
Publish: UTS twin labels; RSCR triggers on method edition change.
```

### C.21:End

## C.22 - Problem Typing & TaskSignature Assignment (Problem-CHR)

**Purpose.** Give FPF a **lawful, minimal, and portable** way to speak about “the problem we face” so that the **selector** (G.5) can legally admit/abstain without prose or guesswork. We do this by (i) **typing problems** with CHR‑grounded traits and (ii) **binding** them to a **TaskSignature (S2)** that downstream patterns can consume. The Standard is **Context‑local**, evidence‑anchored, tri‑state‑aware, and bridge‑savvy. TaskSignature is *minimal* but sufficient for **eligibility**, **acceptance**, and **policy‑governed** choice. 

**Status & placement.** Part C (Kernel Extentions Specifications) → Cluster C.I (Core CHRs/CALs).
**Depends on:** **C.16 MM‑CHR** (measurement legality), **G.5** (selector S2/S3), **G.0** (CG‑Spec invariants).
**Coordinates with:** **G.4** (Acceptance/Evidence profiles), **C.23** (MethodFamily admissibility & maturity), **C.18 NQD‑CAL** (QD/illumination), **C.19 E/E‑LOG** (emitters/policies), **E.10** (LEX).

### C.22:1 - Intent

Operationalise No‑Free‑Lunch discipline in selection by ensuring every run‑time decision sees a **typed TaskSignature (S2)**, not a paragraph, and that **“problem”** (method unknown) is cleanly separated from **“task”** (method known; signature bound). The signature is the **smallest CHR‑typed set** sufficient to drive **Eligibility → Acceptance → policy‑governed selection** without illegal arithmetic or silent coercions; crossings are auditable (Bridge+CL → **R_eff only**).
### C.22:2 - Problem Frame (design/run split; crossing-visible)

**method‑first stance**
In FPF a **Problem** exists when a Holder or external **Transformer** cannot cite a known **Method** (or specialisation thereof) that satisfies the current **TaskSignature** under the declared **ScopeSlice(G)**. Problem‑solving therefore entails **strategizing** (selecting or synthesising a method). The resulting **strategy/policy** is a composition under **G.5/E/E‑LOG** and **is not** a new kernel type.  
