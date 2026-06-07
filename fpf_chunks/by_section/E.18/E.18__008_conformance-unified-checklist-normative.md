---
chunk_kind: "child"
pattern_id: "E.18"
pattern_title: "Transduction Graph Architecture (E.TGA)"
section_id: "E.18:7"
section_title: "Conformance — Unified checklist (normative)"
source_path: "FPF-Spec.md"
output_path: "by_section/E.18/E.18__008_conformance-unified-checklist-normative.md"
commit_sha: "18497f0808242ab7c1a31cb5c94898e9f6b6879d"
heading_path:
  - "E.18 — Transduction Graph Architecture (E.TGA)"
  - "E.18:7 — Conformance — Unified checklist (normative)"
line_start: 66239
line_end: 66306
dependencies:
  - "A.2.6"
  - "A.20"
  - "A.21"
  - "A.7"
  - "E.10"
  - "E.17"
  - "E.8"
  - "F.17"
  - "F.9"
  - "G.11"
  - "G.5"
  - "G.9"
keywords:
  - "CSLC normalize-then-compare"
  - "CV⇒GF (ConstraintValidity → GateFit)"
  - "DesignRunTag"
  - "MVPK faces"
  - "OperationalGate(profile)"
  - "PathSlice/Sentinel refresh"
  - "Set-return selection"
  - "SquareLaw"
  - "UNM declaration locus"
  - "edge=U.Transfer (single-edge kind)"
  - "nodes=morphisms"
  - "transduction graph"
---

### E.18:7 - Conformance — **Unified checklist (normative)**

**Conformance use.** This checklist is evidence for the graph/flow/crossing action guidance already stated in the Solution. It is not the first entry text for ordinary use and not a full audit regime by default; an item is applied only when its corresponding graph, crossing, publication, gate, refresh, or assurance move is live. Before applying any item, name the Solution move it tests; if no such practitioner move is live, treat the item as auxiliary-only or not applicable rather than expanding the applied assurance or conformance material.

**Conformance groups.** Ordinary graph/path use starts with graph object, single edge kind, node typing, `CtxState` preservation, and flow valuation. Crossing/launch items apply only when a GateCrossing, `LaunchGate`, `StructuralReinterpretation`, or work-boundary crossing is live. Publication/assurance items apply only when MVPK faces, edition pins, evidence carriers, decision logs, or replay are live. Extension/change items apply only when node-kind scope, budget/refresh behavior, or UNM/comparator editions are being changed or consumed downstream.

| ID | Requirement | Practical test |
|----|-------------|----------------|
| **CC‑TGA‑01 — Single edge kind** | The graph uses exactly one edge kind `U.Transfer`; all plane/Context/edition transitions occur only at nodes via `OperationalGate(profile)`. | Model lint finds no auxiliary edge kinds for unit/plane changes; crossings sit on declared gates. |
| **CC-TGA-02 — Nodes are morphisms** | Nodes are declared `U.Transduction(kind in {Signature, Mechanism, Work, Check, StructuralReinterpretation})` definitions. This enumeration is a **minimal kind baseline**. **Domain-specific species are open-world** and non-exhaustive; they bind to one of these kinds. Adding a **new kind** uses an explicit E.TGA update. `StructuralReinterpretation` nodes are **projection-preserving** (no mutation of `⟨L,P,E⃗,D⟩`) and carry CV/GF obligations per `A.20`, `A.21`, `A.6.4`, and E.TGA. The enumeration is **not** a TGA-local taxonomy: `Signature -> A.6.0`, `Mechanism -> A.6.1`, `Work -> A.15`, `Check -> A.21 OperationalGate`, and `StructuralReinterpretation -> A.6.4 plus E.TGA/A.20` where CV is live. | Type registry shows at least the listed kinds; additional species map to one of them; checks realized as `OperationalGate` (see CC-TGA-06-EX/11). **Lint:** registry/table exposes `{species -> {kind, KindDefinition}}`; missing or mismatched `KindDefinition` fails. |
| **CC‑TGA‑03 — Identity, composition, functorial faces** | Identities exist; path composition associative; publication is functorial: `Emit_s(t₂∘t₁)=Emit_s(t₂)∘Emit_s(t₁)`. | Pick two‑step path; MVPK faces commute (Square witness). |
| **CC‑TGA‑04 — Graph spec** | Spec declares `τ_V, τ_E`, `Γ_time`, Transport/Bridge registries. | Spec file shows typed registries and Γ policy. |
| **CC‑TGA‑05 — CtxState pins** | `CtxState=⟨L,P,E⃗,D⟩` is pinned on ports/tokens; raw `U.Transfer` does **not** write/update it. | Along a raw transfer, ⟨L,P,E⃗,D⟩ is preserved. |
| **CC‑TGA‑06 — Operational gates only** | Any write/update to any member of ⟨L,P,E⃗,D⟩ or entry into `U.WorkEnactment` is mediated by `OperationalGate(profile)` with aggregated `DecisionLog`. | Diff CtxState across edges; if any member differs, exactly one gate exists with DecisionLog. |
| **CC‑TGA‑06‑EX (strictly limited) — Projection retargeting without gate** | A node of kind **`StructuralReinterpretation`** retargets the **published projection** without invoking `OperationalGate` **only if all hold**: **(a)** `⟨L,P,E⃗,D⟩` is preserved; **(b)** any **EntityOfConcernRef** change has a **KindBridge** (`CL^k`) entry on MVPK/**UTS**; **(c)** a **SquareLaw‑retargeting witness** is present (on UTS); **(d)** the operation is **PathSlice‑local** (`PathSliceId` pinned); **(e)** **no plane/unit change** occurs (plane/unit changes remain gated); **(f)** **CV.ReinterpretationEquivalence** (A.20) is `pass`; **(g)** **NoHiddenScalarization** — if the step concerns a comparable return shape, set/partial‑order semantics are preserved and comparators remain ref‑only (current comparator and set-return loci). | UTS row includes `bridgeChannel=Kind` and `CL^k`; SquareLaw‑retargeting witness present; PathSliceId pinned; CV status recorded; no scalarization detected. |
| **CC‑TGA‑07 — CV⇒GF activation predicate** | Until **aggregated `ConstraintValidity` = `pass`**, all **GateFit** checks return `abstain`. | Simulate CV failure ⇒ GateFit `abstain`. |
| **CC‑TGA‑08 — LaunchGate discipline (incl. pre‑run barrier)** | Each `U.WorkEnactment` has exactly one `LaunchGate` assigned as the aggregator for `USM.LaunchGuard`; **mandatory** checks: `FreshnessUpToDate`, `DesignRunTagConsistency`. If preceding step’s CV ≠ `pass`, LaunchGate decision is `block` (cause logged). | Aggregation assignment `GuardOwnerGateId = LaunchGateId(U.WorkEnactment)`; CV≠pass ⇒ `block` with log. |
| **CC‑TGA‑09 — MVPK publication discipline** | Every published node uses MVPK; faces carry `PublicationScopeId`, presence‑pins, **edition ids**, Γ pins; **no I/O duplication** or arithmetic; faces add no new numeric claims. | Cards show `PublicationScopeId`; pins present; no “signature”/math on faces. |
| **CC‑TGA‑10 — Normalize→Compare (CSLC)** | Any comparison cites **UNM/CG‑Spec** editions and **ComparatorSetRef**; ordinal claims are compare‑only; partial orders return sets; edition‑aware set/archive publication records (QD/archives) pin `{DescriptorMapRef, DistanceDefRef, CharacteristicSpaceRef?}.edition`; **any face citing editions includes `BridgeCard + UTS row`**. **NoHiddenScalarization — detection criteria:** (1) return shape is **set/poset**, not scalar; (2) `ComparatorSetRef` is present and edition‑pinned; (3) MVPK faces add **no new numeric claims**; (4) any summarisation is **order‑preserving & set‑valued**; otherwise conformance fails. | Faces show comparator pins; archive pins present; linter rejects edition cites without UTS; scalarisation checks pass. |
| **CC‑TGA‑11 — Crossings gated** | Cross-Context or cross-plane crossings publish **BridgeId + UTS + CL/CL^plane** and are mediated by `OperationalGate(profile)`; **Φ/Φ_plane penalties appear in R-lane only**; EntityOfConcernRef change publishes **KindBridge (CL^k)**. **Exception (StructuralReinterpretation):** a **projection‑only** EntityOfConcernRef retargeting is recorded **without** a gate **iff** **CC‑TGA‑06‑EX** holds; then the UTS row includes `bridgeChannel=Kind`, `CL^k`, and a **retargeting witness**; any plane/unit change falls back to a gated crossing; `PathSliceId` is pinned; UNM reuse cross‑context continues via `Transport`. | The crossing record shows Bridge/UTS/CL pins; penalty placement audited. |
| **CC‑TGA‑12 — Set‑returning selection** | `U.SelectionAndTuning` returns sets/archives under declared comparators (`ParetoOnly` by default) — no covert scalarization. | Selector output is a set/archive; policy id present if escalated. |
| **CC‑TGA‑13 — Budgeted Selection↔Planning loop** | The loop declares **budget / max_iter**; on expiry selector publishes partial‑optimal set + `MethodTuning`; next **PathSlice** scheduled. | Logs show budget stop and slice rollover. |
| **CC‑TGA‑14 — UNM before loop and FreshnessTicket state change** | UNM runs before selection; stale/missing inputs produce **FreshnessTicket/FreshnessRequest** planned in `WorkPlanning` and executed in `WorkEnactment`; calibrations appear as `CalibrateTo(calibrationReference)` with Φ pins. | Ticket state machine Issued→Planned→Executed→Closed; calibrations pinned. |
| **CC‑TGA‑15 — FinalizeLaunchValues only in WorkEnactment** | Only `U.WorkEnactment` performs `FinalizeLaunchValues` and fills launch‑value slots. | Any earlier attempt blocks at LaunchGate; a `FinalizeLaunchValues` witness is present in Work. |
| **CC‑TGA‑16 — Guard aggregation assignment & semantics** | `USM.CompareGuard`/`USM.LaunchGuard` publish the gate assigned to aggregate guard failures; guards are **events**, not GateChecks; failures are aggregated by that gate per profile. | Guard pins show the assigned gate; GuardFail recorded in that gate's DecisionLog. |
| **CC‑TGA‑17 — Assurance ops on Transfer** | On `U.Transfer` only `ConstrainTo/CalibrateTo/CiteEvidence/AttributeTo`; none write/update `⟨L,P,E⃗,D⟩`. | Edge audit shows ops; CtxState unchanged across the edge. |
| **CC-TGA-17a — Assurance operation specifications (normative)** | **ConstrainTo(region/policy)**: tightens declared region/policy; **pre**: region subset current; **post**: `⟨L,P,E⃗,D⟩` unchanged; **idem.** and **monotone** under composition. **CalibrateTo(calibrationReference)**: attaches an **editioned** calibration reference, such as a map or standard, with Phi-policy id; admissible per cited `CG-Spec`; **post**: `⟨L,P,E⃗,D⟩` unchanged; **idem.** on same edition; penalties appear **in R only**. **CiteEvidence(evidenceRef)**: binds evidence references via **SCR/RSCR**; adds no numeric claims; **idem.**; missing carriers => **abstain**. **AttributeTo(provenanceReference)**: provenance only; decision algebra unaffected; **idem.** Hidden GateChecks, plane/unit changes, or edition writes on edges are **forbidden**. | Operation specifications visible on edge audit; violations fail lint. |
| **CC-TGA-18 — Flow = valuation, coupled-flow unity/separation, and slice-local refresh** | Each flow declares valuation `ν` over `U.Transfer` plus `PublicationScopeId` and `PathSliceId`; when several flows are coupled in one graph, development, application, evaluation, refresh, and repair flows are joined by transfer, feedback, return, or edition-change relations while keeping separate governed objects, role assignments, records, evidence, gates, work occurrences, flow-local relation positions for carried objects, and `DesignRunTag` boundaries; refresh is bounded to the addressed slice; re-emit on edition change or selected refresh rule. | Flow publication shows `ν`; a coupled-flow case names which flow is being valued, which flow-local relation position the carried object fills, and which slice is reopened; refresh trigger causes slice-local recompute. |
| **CC‑TGA‑19 — Γ_time on compare/launch** | All compare/launch faces pin `Γ_time`; no implicit *latest*. | Face audit shows Γ pins; LaunchGate blocks on stale. |
| **CC‑TGA‑19a — Γ_time pin shape (normative)** | The `Γ_time` pin is one of: `snapshot(t)`, `interval[t1,t2]` (closed), or `policy(Γ_timeRuleId)` that resolves to either; CV computations record the **resolved time reference** in `DecisionLog` and do not widen Γ at publication time. | DecisionLog shows the resolved reference; linter rejects missing/implicit Γ. |
| **CC‑TGA‑20 — Lean publish‑mode ≠ weaken** | `AssuranceLane‑Lite` changes publication faces only; required GateChecks for the active profile remain intact. | Gate in Lean/Core shows minimal pins; GateChecks list unchanged. |
| **CC-TGA-21 — Decision stability & idempotency witness** | Gate decisions are stable under the equivalence relation recorded by `A.21`; a **witness of equivalence** is present on the DecisionLog record; any change that breaks equivalence triggers re-aggregation. **Minimum lexeme (CV-relevant witness):** `EquivalenceWitness := { keys, E⃗, Γ_time(reference), PathSliceId?, ReturnShapeClass, ComparatorSetRef?, profile }`. | Modify any input outside the declared equivalence => re-aggregation; DecisionLog records the witness; lexeme present. |
| **CC‑TGA‑21a — Decision join (publication algebra)** | Aggregation over GateChecks is the **idempotent, commutative, associative join** on the lattice `abstain ≤ pass ≤ degrade ≤ block` with **neutral = `abstain`** and **absorbing = `block`**. The algebra is conceptual; publications carry only (i) the aggregated **GateDecision** and (ii) its **GateDecisionRationale** recorded in the **DecisionLog**. A **GateDecisionExplanation** is an optional human‑readable narrative derived from the GateDecisionRationale; it is **not** a decision and is not used as one. If aggregated `ConstraintValidity ≠ pass` or the active profile suppresses narratives, any GateFit‑oriented GateDecisionExplanation **does not apply**. | Review a gate with multiple GateChecks: the aggregated decision matches the lattice join; no per‑check arithmetic is introduced on faces. |
| **CC‑TGA‑22 — Errors/unknowns fold by profile** | Errors/timeouts fold to `degrade` under `Lean/Core` and to `block` under `SafetyCritical/RegulatedX`; `unknown` folds per GateCheck policy (safety‑default: `degrade`). | DecisionLog shows folds; profile switch changes fold behavior accordingly. |
| **CC‑TGA‑23 — SquareLaw on crossings** | For every GateCrossing, `gate_out ∘ transfer = transfer' ∘ gate_in`; LaunchGate case is mandatory. | MVPK shows commuting square; inconsistency yields `block/degrade` per profile. |
| **CC‑TGA‑24 — UNM declaration locus** | `CG‑Spec`, `ComparatorSet`, `UNM.TransportRegistryΦ` editions are declared only through the UNM governing locus (others ref‑only). | Declaration records show UNM as the governing locus; others have refs only. |
| **CC‑TGA‑25 — Evidence lanes & DecisionLogs** | AssuranceLane carries GateProfile, GateCheckRef list, edition pins, aggregated decision, `DecisionLogRef`; **evidence pins follow a two-part scheme**: **carriers** are pinned via **`SCR/RSCR`**, and **value annotations** are carried under **`VALATA (VA/LA/TA)`**. | Gate publication faces include these pins; logs retrievable. |
> **Coupling note.** `CC‑TGA‑07 (CV⇒GF)` and `CC‑TGA‑21a (Decision join)` together ensure that any GateFit‑scoped GateCheckRef **returns `abstain`** until the aggregated CV status equals `pass`; CV/GF separation remains intact.
> **Scope note (E.TGA vs neighbor patterns):** Detailed mechanism-scoped checks and publication obligations are governed by the current neighbor patterns named in this pattern's Relations. E.TGA fixes only graph-architecture obligations: single `U.Transfer` edge kind, gate crossings, valuation, publication pins, CV/GF boundary, and slice-local refresh.

**Glossary (additions)**
* *Open‑world species* — non-exhaustive domain-scoped specializations of `U.Transduction` that map to the minimal kind set.
* *Signature (TGA kind)* — `U.Transduction(kind=Signature)`; **identical to** **A.6.0** `U.Signature` (universal block). **Not** a `C.3.2 KindSignature`.
* *KindSignature (C.3.2)* — definition of a `U.Kind` by intent, extent, and formality; **unrelated** to TGA kinds; never a `genus`.
* *Species (domain-scoped)* — typed specialisations `speciesOf(kind=...)` that declare `KindDefinition=<current governing pattern id>` (e.g., `kind=Mechanism; KindDefinition=A.6.1`).
* *KindBridge (`CL^k`)* — a compatibility note on UTS for EntityOfConcernRef/kind transitions; required by CC‑TGA‑06‑EX and crossings (CC‑TGA‑11).
* *Eulerian interpretation* — operational stance where a flow is treated as a valuation over `U.Transfer` and edges perform assurance‑only operations (no token‑passing semantics).
* **GateCheckKind boundary.** `GateCheckKind` is a publication/check lexeme used inside `GateCheckRef`, not a TGA node kind. No `GateCheckKind` becomes `U.Transduction(kind=Check)` unless an `OperationalGate(profile)` node is actually present.

* **GateCheckRef shape (publication lexeme governed by A.21).** Where graph faces carry GateChecks, a **GateCheckRef** is a record
  defined by `A.21`; E.TGA constrains only where graph faces carry such refs along TGA paths.

`GateCheckRef := { aspect, kind, edition, scope }` with:
  `aspect ∈ {ConstraintValidity, GateFit}`, `kind ∈ GateCheckKind`, `edition ∈ Editions`, and `scope ∈ {lane | locus | subflow | profile}`.
* **GateDecision / GateDecisionRationale / GateDecisionExplanation (terminology).**
  — **GateDecision** — the aggregated lattice value produced by `OperationalGate(profile)` for a specific `{GateProfile, GateCheckRef[]}`.
  — **GateDecisionRationale** — the minimal structured rationale **for that GateDecision**: per‑check outcomes, profile‑bound folds, and published evidence or witness references on the DecisionLog; it records **why the GateDecision is admissible** under the active profile.
  — **GateDecisionExplanation** — an optional human‑readable narrative derived from the GateDecisionRationale; it **does not carry decision status**. While aggregated `ConstraintValidity ≠ pass`, GateFit‑scoped checks return `abstain`; any GateFit‑oriented GateDecisionExplanation **does not apply**.
> **Clarity note.** **GateDecision ≠ GateDecisionExplanation**; narratives are optional and derivative of GateDecisionRationale.

* **GateFit (aspect, not an entity).** GateFit names the **aspect** of checks that evaluate **profile‑fit**; there is no separate GateFit entity. “Gate decision under GateFit” means “the gate’s decision computed from GateChecks with `aspect=GateFit`”.

  This shape is publication-only; it introduces no new execution steps and no arithmetic on faces.  (Couples to A.20 or A.21 without duplicating their check catalogs.)
* *VALATA (VA/LA/TA)* — value-annotation scheme used on **AssuranceLane**; **carriers** are referenced via **SCR/RSCR**; detailed evidence obligations live in `A.10` and the named evidence, publication, or crossing pattern for the live case. Included here so evidence pins are self-describing in Part E texts.
* *Transfer vs Transport* — **Transfer** = the sole graph edge kind `U.Transfer`. **Transport** = Φ‑policy/registry‑defined conversions (`TransportRegistry^Φ`) referenced by UNM; “reuse via Transport” refers to the latter.
* *GateCrossing* — a typed node transition that writes/updates a CtxState slot or the kind‑channel; see **S1.b** for the normative list and required pins.
* *Admissible path* — a typed path obeying the GateCrossing discipline (no hidden crossings; witnesses present), Γ‑pinned on compare/launch, and `T^D↔T^R` only at `LaunchGate`; see **S2**.

