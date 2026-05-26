---
chunk_kind: "child"
pattern_id: "E.18"
pattern_title: "Transduction Graph Architecture (E.TGA)"
section_id: "E.18:5"
section_title: "Solution - E.TGA graph model and relation disciplines"
source_path: "FPF-Spec.md"
output_path: "by_section/E.18/E.18__006_solution-e-tga-graph-model-and-relation-disciplines.md"
commit_sha: "ae1ff1c7a231a2ec78d244b40d7805a5538c6608"
heading_path:
  - "E.18 — Transduction Graph Architecture (E.TGA)"
  - "E.18:5 — Solution - E.TGA graph model and relation disciplines"
line_start: 62416
line_end: 62672
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

### E.18:5 - Solution - E.TGA graph model and relation disciplines
**Dominant Solution moves.** In ordinary E.TGA use, keep five moves primary: name one graph object; distinguish the graph from a flow valuation; place gates only on crossings or the `U.WorkEnactment` boundary; preserve normalize-before-compare and set-return discipline; and keep cycles under budget plus `PathSlice` refresh. S12 viewpoint mapping remains conditional support when engineering or publication viewpoint mapping is live.

#### E.18:5.1 - S1 - Graph object (conceptual)

Define a **typed, editioned, directed multigraph**
`TransductionGraph := (V, E, τ_V, τ_E, Γ_time, Bridge, CL, TransportRegistry^Φ)`
with:

* **Vertices `V`:** instances of `U.Morphism` (open world). Common specialisations **include but are not limited to** the P2W illustrative set: `U.FormalSubstrate`, `U.PrincipleFrame`, `U.Mechanism`, `U.ContextNormalization (UNM)`, `U.SelectionAndTuning`, `U.WorkPlanning`, `U.Work`, `U.EvaluatingAndRefreshing`. This list is **illustrative**, not exhaustive—the graph **does not depend** on this particular set.
* **Edges `E`:** a **single edge kind `U.Transfer`** (typed) carrying carrier refs and token refs; all **plane/Context/edition** changes occur **only at nodes via `OperationalGate(profile)`** with **Bridge + CL** annotations; penalties **→ R only**. Transport conversions pin **Φ‑policies** and editions.
* **Scopes:** `Γ_time` (budgets, horizons), `PublicationScope` for faces (E.17), and **slice ids** for refresh (G.11).

 **CtxState (PS‑projection; closed slots):** `CtxState = ⟨L, P, E⃗, D⟩` is the **projection of E.17 Publication Scope**.
 **Slot definitions (normative):**
  • `L := Locus` — an element of a partially ordered **ContextSlice** poset; addresses *where* claims apply (disciplinary / organizational / holonic slice).
  • `P := ReferencePlane` — the reference plane/units registry id; **no plane/unit declarations or translations** occur in CV; crossings remain gated (A.21).
  • `E⃗ := Edition vector` — a **partial map** `edition_key ↦ EditionId` over named families `{CG‑Spec, ComparatorSet, UNM.TransportRegistryΦ}` and optional `{DescriptorMapRef, DistanceDefRef, CharacteristicSpaceRef}` when cited.
  • `D := DesignRunTag` — `design(T^D)` or `run(T^R)`, used by **LaunchGate** and acceptance/telemetry duties.
 **Invariants.** Raw `U.Transfer` preserves `CtxState` (`⟨L,P,E⃗,D⟩`): it does **not** write/update any CtxState slot; any CtxState write/update (or entry to `U.WorkEnactment`) occurs at `OperationalGate(profile)`.
 **Extension discipline.** A conforming use registers any extra slot beyond ⟨L,P,E⃗,D⟩ in the **E.17/LEX “CtxState Extension Registry”** with slot‑id, intent, partial‑order law (neutral/absorbing), and SquareLaw compatibility; unregistered extensions are non‑conformant.
 **Data-shape location.** E.TGA names the graph and valuation obligations for `PathId`, `PathSliceId`, Γ-pins, and lineage: flow is a valuation over `U.Transfer`, raw transfer preserves `CtxState`, and path or slice evidence is carried through this pattern plus `A.20`, with `G.6` or `G.11` where evidence-path visibility or refresh wiring is live. Use these current loci for path and slice currentness.


 * **Kinds:** `U.Transduction(kind∈{Signature, Mechanism, Work, Check, StructuralReinterpretation})`.
  **Exact identification (no TGA‑local taxonomy):**
  — `Signature` **≡** **A.6.0** `U.Signature` (universal, law‑governed declaration).
  — `Mechanism` **≡** **A.6.1** `U.Mechanism` (law‑governed application over a SubjectKind/BaseType).
  — `Work` **≡** **A.15** `U.WorkEnactment` (world‑contact; `FinalizeLaunchValues` only here).
  — `Check` **≡** `OperationalGate(profile)` (universal **gate**; `A.21` governs gate profile, check aggregation, decision, and publication minima).
  — `StructuralReinterpretation` **≡** the E.TGA placement of **A.6.4** `U.EpistemicRetargeting` as a graph node; it is not a new retargeting kind. **All retargeting semantics** (slot-scoped discipline, `DescribedEntitySlot`/`GroundingHolonSlot` behaviour, invariants, Bridges, witnesses) come from **C.2.1** and **A.6.2–A.6.5**; E.TGA does **not** introduce a TGA-local variant of retargeting.

  `OperationalGate ≔ U.Transduction(kind=Check)` with DecisionLog aggregation.
  The only extra discipline E.TGA adds for `StructuralReinterpretation` is **graph-local**: CtxState and GateCrossing behaviour are governed by **CC-TGA-06-EX** and **CC-TGA-11** (projection-preserving w.r.t. `⟨L,P,E⃗,D⟩`, PathSlice-local, and "no plane/unit change without a gate"). `StructuralReinterpretation` is not a gate exception; it carries a recorded witness condition for saying no GateCrossing occurred. If any `CtxState` slot, plane/unit, edition, or design/run boundary changes, the case is a GateCrossing again.

> **MVPK integration (import).** Every vertex with an external publication face is published via **MVPK** faces (`PlainView`, `TechCard`, `AssuranceLane`, `InteropCard`) under a declared **PublicationScope** (E.17). E.TGA **reuses** MVPK’s publication laws (pins, declared-order discipline, “no new numeric claims / no I/O re‑listing”) and only adds graph-scope constraints in S3 and **CC‑TGA‑09/10**; it does **not** define a second, local publication semantics.

**GateCrossing (normative)**
**Definition.** A **GateCrossing** is the typed transition at a node that writes/updates any of:
  (i) `U.BoundedContext` (**Context**), (ii) **ReferencePlane**, (iii) any member of the **Edition vector** `E⃗` (e.g., `CG‑Spec`, `ComparatorSet`, `UNM.TransportRegistryΦ`, `DescriptorMapRef`, `DistanceDefRef`, `CharacteristicSpaceRef`), (iv) **DesignRunTag** (`T^D↔T^R`), or (v) **Kind/describedEntity** (only under `StructuralReinterpretation` subject to **CC‑TGA‑06‑EX**).
**Invariants.** Raw `U.Transfer` preserves `CtxState`; a GateCrossing occurs at exactly one `OperationalGate(profile)` (SquareLaw applies).
**Required pins (minimum).** `BridgeCard + UTS row`; `CL` for scope bridges; `CL^plane` for plane crossings; `CL^k` with `bridgeChannel=Kind` for kind transitions; `PublicationScopeId`; `PathSliceId`; Γ‑pins on compare/launch faces.
**Canonical reference.** `CrossingRef := ⟨GateId, channel, from, to, UTS.RowId, PathSliceId⟩`. Any DecisionLog entry whose rationale depends on a crossing cites `CrossingRef`.
**CrossingBundle (normative)**
**Definition.** A **CrossingBundle** is the published bundle that makes a GateCrossing **auditable and replayable** (crossing visibility). It includes:
* the canonical **`CrossingRef`**;
* the matching **UTS row** (**`UTS.RowId`**) for the crossing;
* the required pins **`PublicationScopeId`** and **`PathSliceId`**;
* where a Bridge is involved: the **BridgeCard** (F.9) and its disclosed fields (`BridgeId`, `bridgeChannel`, **CL** and loss notes; **`CL^k`** when `bridgeChannel=Kind`; **`ReferencePlane(src,tgt)`**);
* where planes differ: **`CL^plane`** and the active **`Φ_plane`** as a **`PolicyIdRef`** (policy-id + resolvable refs; F.8:8.1);
* the active penalty policy identifiers **`Φ(CL)`** (and **`Ψ(CL^k)`** if used) as **`PolicyIdRef`** bundles (policy-id + `PolicySpecRef` + `MintDecisionRef?`; F.8:8.1);
* any additional pins mandated by the active **GateProfile** / GateChecks (A.21) for this crossing.

**CrossingBundle rule.** Every **GateCrossing publishes its CrossingBundle**. Missing or non-conformant CrossingBundle is a **blocking** defect for downstream uses that rely on the crossing (selectors, acceptance, audits). A local descriptive graph with no downstream crossing consumption is not over-penalized by this CrossingBundle rule.

**Term separation.** **Transfer** denotes the sole edge kind `U.Transfer` (graph edges). **Transport** denotes Φ‑governed conversion **policies/registries** (**`TransportRegistry^Φ`** under UNM). Wording “reuse via Transport” refers to registries/policies, not to an additional graph edge.

#### E.18:5.2 - S2 - Flows as valuations (paths + state + guards)
* A **Flow** is a **valuation** `ν` over `U.Transfer` edges and cut-sets, paired with an **admissible path** `p = v0 -> ... -> vk`. The valuation assigns tokens or states under `CtxState` and records publication events under a declared `PublicationScopeId`. The concrete pins and identifiers (`PathId`, `PathSliceId`, Γ_time on compare and launch faces) are governed here as path and slice publication obligations and by `A.20` when CV witnesses are live; use `G.6` for evidence-path visibility and `G.11` for refresh wiring. This reflects the “graph != flow” norm (flow = valuation), with gates placed exactly on GateCrossings.
* **Admissible path (definition).** A path `p` is **admissible** iff:
  (a) node/edge types match the declared `τ_V, τ_E`;
  (b) any write/update to any member of `⟨L,P,E⃗,D⟩` (or kind‑retargeting under `StructuralReinterpretation`) appears at **exactly one** `OperationalGate(profile)`;
  (c) each GateCrossing on `p` has a **SquareLaw witness** (CC‑TGA‑23) and, where applicable, a **SquareLaw‑retargeting witness** (CC‑TGA‑06‑EX);
  (d) no hidden crossings occur across raw transfers;
  (e) Γ‑pins are present on compare/launch faces;
  (f) `T^D↔T^R` occurs **only** at `LaunchGate`.

* `U.Transfer` preserves `CtxState` (`⟨L,P,E⃗,D⟩`) and carries **Assurance‑operations** only (see S3b); any crossing of locus/plane/editions or `T^D↔T^R` is placed at `OperationalGate(profile)`.
* A **PathSlice** is a **slice‑scoped execution window** used for refresh/telemetry; faces pin `PathSliceId`; **re‑emission** happens when any pinned edition changes or `SliceRefresh` is triggered by sentinel rules.

> **Consequences.** The P2W reference flow is simply one `p` in `TransductionGraph`. Other domains (supply chain, water network, NN functional) instantiate different `p` on the **same architecture**.
>
**Why "flow = valuation" doesn't kill the "something is flowing" intuition**
There are two complementary perspectives:
* **Lagrangian (intuitive):** "water particles" run through pipes; you "track" tokens.
* **Eulerian (architectural):** you define a **function on edges** ("how much/what passes through each edge under a given regime"), with gate laws. E.TGA deliberately fixes the **Eulerian semantics of flow** at the architectural scope: "flow (= valuation) + publication log", while the dynamics of "movement" show up as **re-valuation** over a **PathSlice** (the execution/republishing window) under gate rules and the SquareLaw. This yields comparability, reproducibility, and slice-local refresh.

#### E.18:5.3 - S3 - Publication discipline (faces)

E.TGA **imports E.17** wholesale **and associates MVPK faces with `PublicationScope` (USM)**.
**MVPK remains the normative source** for:
* the set of face kinds (`PlainView`, `TechCard`, `InteropCard`, `AssuranceLane`),
* pin discipline and Publication Characteristics (PC),
* “no new numeric claims / no I/O re‑listing / no Γ‑semantics on faces”.

E.TGA **does not re‑specify** these laws; it only adds **graph-scope obligations** for faces emitted over transduction paths:

1. **Crossings on faces.** When a face participates in a GateCrossing (S1.b/S9), it cites `BridgeId + UTS row + CL` and publishes **Φ(CL)/Φ_plane RuleId**; **penalties remain in R‑lane**.
2. **Gate requirement on cited editions.** Any face that references editions of `CG-Spec`, `ComparatorSet`, or `UNM.TransportRegistryPhi` includes **`BridgeCard + UTS row`**; faces without this are treated as **non-consumable downstream**. Bridge and terminology-synchronization checks are received through `F.9`, `F.17`, `E.17`, and `E.18`; selection and comparator pressure stays with `A.19.SelectorMechanism`, `C.18`, `C.19`, `G.5`, or `G.11` when live.
3. **ComparatorSet & set returns (graph‑scope).** Any `ComparatorSet` and `SetSemanticsRef` used along a transduction path carries **edition identifiers**; flows **re‑emit** faces on edition change; faces with comparison **return sets and declared partial orders** (no hidden scalarization), reusing MVPK’s declared-order discipline.
4. **Γ_time on compare and launch faces.** All compare and launch faces on E.TGA paths pin `Γ_time`; implicit *latest* is not admissible. `A.21` carries current GateProfile binding and minimum profile semantics; E.TGA paths include the pin. **CHR avoids acceptance thresholds** (*NoThresholdsInCHR*); thresholding and launches are carried by `A.21`, Part G, and `U.Work` where live. Unknowns remain tri-state (`pass|degrade|abstain`) and fold per the active GateProfile (`A.21`).

> **Reminder.** MVPK already bans “signature” on faces, I/O re‑listing, arithmetic on faces, and unpinned numeric content (E.17 §5.4–5.5). E.TGA **does not weaken or override** those rules; it only constrains how they are used along transduction paths.

**Lean publish‑mode (AssuranceLane‑Lite).** Lean changes **publication faces only** (`PlainView`/`AssuranceLane` minimal), not checks; publication shows `GateProfile`, `GateCheckRef[]`, and `DecisionLogRef`; the underlying GateChecks list remains unchanged.

**Decision stability & idempotency (gate-local).** Gate decisions are stable under a declared equivalence relation over the pins used by `A.21`; the witness is recorded as `DecisionLog` or `EquivalenceWitnessRef`, with `G.6` or `G.11` used when evidence-path visibility or refresh implications are live. E.TGA **does not** prescribe storage formats, key shapes, or hashing schemes.

**KindBridge admissibility (publication).**
Treat a step as a **describedEntity/kind** transition (including `StructuralReinterpretation` under CC‑TGA‑06‑EX) **iff** the **UTS row**:
  — satisfies the minimal bridge and terminology-synchronization obligations of `F.9`, `F.17`, `E.17`, and `E.18` where live (identity, `ReferencePlane`, `CL/CL^plane`, edition pins for `CG-Spec`, `ComparatorSet`, `UNM.TransportRegistryPhi`, `ComparatorSetRef`, `BridgeId`, and `Phi-RuleIds`), and
  — is additionally marked as a **KindBridge** per C.3 (`bridgeChannel=Kind`, `CL^k`, mapping or signature‑translation, order‑preservation claims, loss notes, definedness area, determinism).
Otherwise this KindBridge explanation does not apply (the step falls back to a gated crossing). When the crossing is gate-mediated, `CrossingRef` is cited and linked from the `DecisionLog`.

#### E.18:5.4 - S4 - Assurance‑operations on `U.Transfer` (counterfactual admissibility)
On `U.Transfer` edges, an operation is interpreted as a **declarative assurance‑operation** **iff** it is one of
`ConstrainTo(rule)` - `CalibrateTo(calibrationReference)` - `CiteEvidence(anchor)` - `AttributeTo(provenanceReference)`; otherwise this explanation does not apply.
Under this interpretation, `CtxState⟨L,P,E⃗,D⟩` is preserved.
If a claimed assurance operation would change plane or units, the assurance-operations explanation does not apply and the step is handled as a gated crossing (`OperationalGate(profile)+Bridge+UTS`).

If Φ assigns penalties, they appear in the R‑lane; otherwise no penalties appear here.

#### E.18:5.5 - S5 - Comparability & aggregation (normalize‑then‑compare; counterfactual form)

The comparison explanation applies under the following admissibility conditions:

* If a path segment intends to compare/aggregate, it is admissible as a comparison **only when** UNM precedes it; UNM is **method‑independent**, publishes **TransportRegistry^Φ** and **CG‑Spec** anchors, and faces cite those editions; otherwise this comparison explanation does not apply.
* If the comparator defines a **declared partial order**, then returns are **sets/archives** (Pareto/Archive); if a **total order** is declared, it is the one provided by the comparator; otherwise set semantics apply and covert scalarization is out of scope here.
* If a claim is **ordinal‑only**, then only comparison results are published; arithmetic transforms (e.g., means/z‑scores) are out of scope of this explanation and belong to declared comparators or downstream policy.

**Edition-aware set/archive publication records (e.g., QD archives) pin `DescriptorMapRef.edition`, `DistanceDefRef.edition`, and `CharacteristicSpaceRef.edition` when applicable; refresh is slice-local. Comparator, archive, and refresh checks are received through `A.19.SelectorMechanism`, `C.18`, `C.19`, `G.5`, `G.9`, and `G.11` when live.**

#### E.18:5.6 - S6 - Cycle discipline (Selection ↔ Planning)

* The architecture centers the loop between `U.SelectionAndTuning` and `U.WorkPlanning`.
* The loop operates under a local **budget / max_iter** in `Γ_time`; at expiry, the selector emits the **current `CandidateSet`** and **`MethodTuning`** with a **partial‑optimality** flag; further improvement rolls into the **next `PathSlice`**.
* **UNM occurs before the loop**; if measurements are missing/stale, UNM emits a **FreshnessRequest** which is **planned** in `U.WorkPlanning` and **executed** in `U.Work`. Transfers, units, and calibrations are published as `CalibrateTo(calibrationReference)` and pinned to `TransportRegistry^Φ` (**R‑channel only** for penalties).
* **WorkEnactment is the only site for launch‑value slot filling** (`FinalizeLaunchValues / FinalizeLaunchValuesOnlyInWork`).
> **Refresh orchestration.** Telemetry from `U.WorkEnactment` and publications are **slice‑scoped**, editions re‑pinned, faces **re‑emitted**.

#### E.18:5.7 - S7 - Selector semantics (G.5) & parity harness (G.9)
E.TGA checks that set-return, archive preservation, and comparator refs remain visible along the path. It does not define selector, archive, dominance, or comparator semantics; those remain with `A.19.SelectorMechanism`, `C.18`, `C.19`, `G.5`, `G.9`, and `G.11` where live.

* **Selectors return sets.** Default **DominanceRegime** is `ParetoOnly`; **IlluminationSummary** (telemetry summary) and any coverage/regret telemetry quantities are **report-only telemetry** (reported), excluded from dominance **unless** a CAL policy promotes them as declared dominance inputs (policy-id in SCR).

If `PortfolioMode=Archive`, a **QD archive** can be returned; when generation is in scope, pairs `{environment, method}` are managed under declared **EnvironmentValidityRegion** and **TransferRulesRef**; parity records and `PathSliceId` are pinned on publication. Comparator semantics and archive pinning are received through `A.19.SelectorMechanism`, `C.18`, `C.19`, `G.5`, `G.9`, and `G.11` when live.

#### E.18:5.8 - S8 - Guard aggregation assignment and handling (USM §1.2)
* **USM.CompareGuard**/**USM.LaunchGuard** **publish `GuardOwnerGateId`**. Guard failures are **events** aggregated by the declared gate (not GateChecks).
* **Aggregation-assignment rules:** (i) `USM.LaunchGuard.aggregationGate = LaunchGateId(U.WorkEnactment)`; (ii) inside a Subflow, `USM.CompareGuard.aggregationGate = OperationalGate(InSentinel)`; Join-nodes cannot be assigned as guard-pin aggregation gates.

**GateProfile data shape (cross-reference).** `A.21` carries the current GateProfile binding and minimum profile semantics. E.TGA names the structure only where graph crossings need it; fuller profile-matrix support is not a separate current authority unless a current governing pattern explicitly admits it.

**Bridge-aware guards (cross-reference).** USM guards apply bridge-translation semantics (`translate(Bridge, Scope)`) with CL penalties in R-lane; guard vocabulary is received through **A.2.6**, while gate aggregation remains in `A.21`.

**Error/timeout/unknown (profile-bound).** GateCheck errors/timeouts fold to **`degrade`** under `Lean\|Core` and to **`block`** under `SafetyCritical\|RegulatedX`; `unknown` follows the GateCheck's intensional rule (safety-default: `degrade`). The `A.21` DecisionLog record and equivalence witness carry decision stability; E.TGA does not define storage or key structures.

#### E.18:5.9 - S9 - Transport & crossings
* Cross‑Context or cross‑plane edges appear as **GateCrossings** that include a **Bridge** with **CL** policy; **Φ(CL)/Φ_plane** are published; penalties appear **in R only**; **Scope membership** (USM) is unchanged by crossings. **SquareLaw is checked within a single `DesignRunTag`; a `T^D↔T^R` change is modelled as a pair of coordinated gates with `DesignRunTagFrom/To` and the selected `A.15` work or publication locus for the live case.**
* When *describedEntity/kind* changes across a boundary, declare an explicit **KindBridge (`CL^k`)** in addition to plane/context CL; cross-context reuse of UNM uses `Transport`, with any `CL^plane` penalties published in **R-lane** only.

#### E.18:5.10 - S10 - Non‑mechanism boundary

* Publication is a **typed projection**, not execution. Any build/render/upload is **Work on carriers**; faces do **not** carry Γ-semantics.

#### E.18:5.11 - S11 - Coordination thread (optional)
Coordination wording may be published as **LexicalView** labels over `U.TransductionFlow__P2W`; it is orientation-only unless a bridge, crossing, work, or gate relation is explicitly live. It adds no current graph node kind, checks, or mechanisms. Crossings with production flow use **Bridge+UTS** and the current bridge or crossing loci.

#### E.18:5.12 - S12 - Viewpoint families → E.TGA constructs (neutral, holonic)
**S12 status.** S12 is secondary support for a live viewpoint-family mapping claim. It is not the ordinary E.TGA core for naming a graph object, flow valuation, path slice, or crossing.

E.TGA does not mint new viewpoint or view kinds. It **imports** the generic multi‑view machinery of E.17.0 `U.MultiViewDescribing`, bundles from E.17.1, and the TEVB engineering bundle from E.17.2. S12 only describes how these existing `U.Viewpoint` / `U.ViewpointBundle` ids are *used* in transduction graphs and in `UTS.ViewpointMap`; intent/concern semantics are governed by E.17.0–E.17.2.

**Two-part use of TEVB and MVPK (ISO 42010 summary, no local re‑definition).**

* **Engineering viewpoints.** For engineering holons, E.TGA assumes a TEVB bundle with `ViewFamilyId = VF.TEVB.ENG`. `EngineeringVPId` is one of `{VP.Functional, VP.Procedural, VP.RoleEnactor, VP.ModuleInterface}`, and TEVB is the normative source for their semantics. E.TGA does not refine these viewpoints.
* **Publication viewpoints.** Publication viewpoints come from MVPK (E.17); `PublicationVPId` is a `MVPK.ViewpointId` that governs faces under a `PublicationScope`.
* **Architecture relation.** E.TGA can describe a flow/transduction-structure view of an `ArchitectureOf@Context` claim when `DescriptionContext`, described holon, bounded context, and structure kind are explicit. It does not define architecture itself, and a TGA graph is not the functional architecture by default. Use `C.30`, `C.30.ASV`, and `C.30.TGA-FLOW-REL` when the graph is used as architecture-description support. Crossings and penalties follow E.TGA gating rules (S9; CC-TGA-11/23) but do not change viewpoint semantics.
* **Separation of roles.** `VP.*` from TEVB are **EngineeringVPId** values only; they are not publication faces. `PublicationVPId` values live in MVPK. The mapping between them is entirely via ISO‑style correspondences and the `UTS.ViewpointMap`; E.TGA does not define a second notion of viewpoint.

**Entities‑of‑interest (summary).**

* **EoI‑ENG.** The engineering entity described by TEVB/E.TGA is a holon (`U.System` or `U.Episteme`) per TEVB’s `EoIClassSpec`. E.TGA does not broaden or narrow this set.
* **EoI‑PUB.** MVPK can treat the *architecture description* itself as an entity‑of‑interest; publication viewpoints for that AD are defined in MVPK, not here. E.TGA only checks that such faces honour MVPK discipline and E.TGA’s crossing rules.

**Naming rules (aligned with E.17.0/E.17.1/E.17.2).**
* `ViewFamilyId` is the `U.ViewpointBundle.viewFamilyId` (e.g. `VF.TEVB.ENG` for TEVB); its lexical and ontological discipline is governed by E.17.1.
* `EngineeringVPId : ViewpointId` is always a `U.ViewpointId` drawn from some bundle (for TEVB, one of `{VP.Functional, VP.Procedural, VP.RoleEnactor, VP.ModuleInterface}`). E.TGA never defines new `VP.*` ids.
* `PublicationVPId : ViewpointId` is a `MVPK.ViewpointId` defined in E.17; TEVB viewpoints are **never** reused as publication viewpoints (per TEVB guard and MVPK).
* The unqualified field name `ViewpointId` is not valid in S12 rows. Use `EngineeringVPId` and/or `PublicationVPId` explicitly; any imported row with an unqualified `ViewpointId` is normalized to `PublicationVPId` before the row is used.

**Terminology guards (no local semantics).**
* Within S12, “viewpoint”, “view” and “correspondence” have exactly the meanings given in E.17.0; “publication face” means an MVPK face (`PlainView`, `TechCard`, `InteropCard`, `AssuranceLane`) under some `PublicationVPId`.
* Faces are **carriers for views**: a face is part of a view only when linked via an ISO‑style `CorrespondenceRef` to an engineering `U.View` under some `EngineeringVPId`; S12 does not add extra conditions beyond E.17.0/E.17.2.
* Labels such as “Functional view”, “Procedural view”, “Role‑Enactor view”, “Module‑Interface view” in this section are lexical aliases for TEVB viewpoints; they are not interpreted as extra viewpoint kinds or as publication-face types.

**Purpose.** Provide a neutral (F.18) mapping from TEVB engineering viewpoint families - bundle `VF.TEVB.ENG` with `VP.Functional / VP.Procedural / VP.RoleEnactor / VP.ModuleInterface` - to E.TGA constructs so that the same holon can be described through functional, procedural, role-enactor, or module-interface viewpoints while the E.TGA construct scope remains explicit. S12 does not introduce new `U.Viewpoint` or `U.View` kinds, and it does not claim that all such views share one underlying graph unless the graph, described entity, and correspondence refs are declared.

**Holon target.** The mapping applies to any holon, with the constraint that only `U.System` enacts `U.Work` (A.3/A.15). Supervisory and structural hierarchies remain distinct (B.2.5).

**Viewpoint family → primary E.TGA constructs (TEVB‑aligned)**
*All four families referenced below are TEVB engineering viewpoints; the “what …” clauses are interpretive glosses for how they *use* E.TGA constructs. Formal intent/concerns/allowed episteme kinds remain in TEVB (E.17.2).*
1) **Function‑Oriented View (`EngineeringVPId = VP.Functional`, capability‑flow)** — “what transformation is achieved under roles”
    * **Flow substrate:** `U.TransductionFlow__P2W` through nodes `U.FormalSubstrate → U.PrincipleFrame → U.Mechanism → U.ContextNormalization (UNM) → U.SelectionAndTuning ↔ U.WorkPlanning → U.Work → U.EvaluatingAndRefreshing`.
    * **Publication:** MVPK publication faces per E.17; comparable claims pin to `CG‑Spec/ComparatorSet` editions; crossings are published through `Bridge+UTS` and `CL/CL^plane` (penalties → **R‑lane** only).
    * **Checks:** A.20 (CV) inside transformations; A.21 (GateFit) at gates; comparator, set-return, and No-Hidden-Scalarization discipline is carried through `A.19.SelectorMechanism`, `C.18`, `C.19`, `G.5`, `G.9`, and `G.11` when live.
    *  **Holonic note:** `U.Episteme` does not *act*; it is used by systems acting on carriers; `U.Work` appears only for `U.System`.
2) **Procedure‑Oriented View (`EngineeringVPId = VP.Procedural`, step/time storyboard)** — “what steps occur and when”
    * **FPF constructs:** `U.WorkPlan` (A.15.2) for intent/schedule; `U.WorkEnactment` for enactment.
    * **Boundary:** entry into `U.WorkEnactment` is via `OperationalGate(profile)` with `USM.LaunchGuard`; `DesignRunTag` separates design time from run time; `DesignRunTagFrom/To` appear only at gates.
    * **Holonic note:** Applies to any `U.System` scope (single holon or a supervised sub‑holon cluster); supervisory structure is handled by roles rather than structural mereology (B.2.5).
3) **Role‑Enactor / Device‑Structure View (`EngineeringVPId = VP.RoleEnactor`)** — “what carrier/ports/constraints exist; who typically enacts it”
    * **FPF constructs:** Module *interfaces* are `Signature` nodes; module realizations are `Mechanism` nodes; inter‑module dependencies traverse `U.Transfer`, with gates on crossings.

    * **Publication:** MVPK faces are **typed projections**, not `U.Work` records or execution carriers; faces add **no new numeric claims** (E.17). Constraints and compatibility appear as CV checks (A.20).
    * **Holonic note:** Structural mereology (part/whole of the carrier) is modeled in Part A; E.TGA ties interface/exposure semantics to morphisms and gates.
    * **Device‑View reading (Transduction↔Transductor).** The same capability‑flow can be read as a **device** that performs the transduction (**transductor**) without changing the declared E.TGA graph object: model with `Signature` + `Mechanism` only; do **not** introduce extra edge kinds. If describedEntity retargets (function↔element), use `StructuralReinterpretation` with a **`KindBridge (CL^k)`** on **UTS** and a **SquareLaw‑Retargeting witness**; preserve `⟨L,P,E⃗,D⟩` and treat it as a non‑crossing (**CC‑TGA‑06‑EX**; witness shape §4.7).
    * **Role‑label guard.** `TypicalEnactorRoleName` is **pedagogical only** and is not used as a GateFit role; GateFit uses `U.Role` (A.21).
4) **Module‑Interface View (`EngineeringVPId = VP.ModuleInterface`, physical/logical module structure)** — “what modules exist and how they specify commitments and constraints across interfaces”
    * **FPF constructs:** Module *interfaces* are `Signature` nodes; module realizations are `Mechanism` nodes; inter‑module dependencies traverse `U.Transfer`, with gates on crossings.
    * **describedEntity note:** Functional-view-to-element-structure reinterpretation follows the **Device‑View reading** rule above (Role‑Enactor family) and **CC‑TGA‑06‑EX**; see **§4.7** for the retargeting witness shape and CV witness linkage.
    * **Holonic note:** The same module can appear as a holon in multiple views; supervisory loops (B.2.5) remain orthogonal to structural composition.
This is an expandable list of viewpoint families; TGA is intentionally viewpoint‑neutral. Additional engineering bundles beyond TEVB (safety, mission, information, …) are introduced as separate `U.ViewpointBundle` species via E.17.1/E.17.2; S12 does not define them.

**Alias families for transduction species (LEX‑only).**
*Scope.* A pattern or domain profile can declare `AliasesInViewFamilies[]` for `U.Transduction` species so practitioners can recognise familiar engineering view families. All semantics come from the referenced bundles (typically TEVB) and MVPK; aliases are purely lexical.

*Norms.*
1. Each `U.Transduction` species can publish `AliasesInViewFamilies[]` — an open list of records
   `{ ViewFamilyId, EngineeringVPId?, Alias : TechASCII }`.
   * If `ViewFamilyId = VF.TEVB.ENG`, then `EngineeringVPId` is one of `{VP.Functional, VP.Procedural, VP.RoleEnactor, VP.ModuleInterface}` (TEVB; CC‑TEVB‑1/6).
   * Other `ViewFamilyId` values denote `U.ViewpointBundle` instances defined elsewhere (e.g. safety/assurance/information bundles), not ad‑hoc local families.
2. Aliases are LEX‑only: **no arithmetic, no new claims, no check participation, no `CtxState` slot writes/updates (incl. `DesignRunTag`)**. They do not create MVPK faces.
3. Aliases are not used as `PublicationVPId`; publication viewpoints remain in MVPK.
4. Twin registers are allowed (Tech/Plain) per E.10; naming follows F.18 local‑first discipline.
5. Do not name transductions by operands or output states (operation != operand or output state).

6. `TypicalEnactorRoleName` can be added for pedagogy; it is not used as a GateFit role (GateFit uses `U.Role` only).
7. Morphology: ASCII TitleCase; conjunctions via `And`; for composite actions use `XingAndYing` (or `XAndYing` if grammar calls for it).
8. The P2W illustrative species row (`U.FormalSubstrate` … `U.EvaluatingAndRefreshing` with functional/procedural aliases and `TypicalEnactorRoleName`) is **informative** and does not change kind or viewpoint semantics.

**Conditional deliverable — `UTS.ViewpointMap` (TEVB-aligned when live).**
Publish a UTS block named `ViewpointMap` only when an engineering or publication viewpoint-family mapping claim is made or consumed. Ordinary E.TGA use does not require `UTS.ViewpointMap` when the live question is only the graph object, flow valuation, path slice, or crossing.

*Minimum row schema (per row, when `ViewpointMap` is live).*
* `ViewFamilyId` — `U.ViewpointBundle.viewFamilyId` (e.g. `VF.TEVB.ENG` for TEVB, or another bundle id).
* `EngineeringVPId : ViewpointId` — a viewpoint from that bundle (for TEVB, one of `{VP.Functional, VP.Procedural, VP.RoleEnactor, VP.ModuleInterface}`).
* `PublicationVPId : ViewpointId?` — MVPK publication viewpoint id that governs faces implementing this engineering view (optional if not publishing).
* `TargetHolon ∈ {U.System, U.Episteme}` *(extended species can add `{U.PromiseContent|U.MethodFamily}`; if `TargetHolon ≠ U.System`, no `U.Work` enactment appears).*
* `PrimaryTGAConstructs` — nodes/edges/gates actually used for this `(ViewFamilyId, EngineeringVPId, TargetHolon)` (typically one of the four families above).
* `Crossings{BridgeId, CL/CL^plane?}` — crossings involved; penalties appear in R-lane only.
* `EditionPins{...}` whenever comparable claims appear (bind to CG-Spec/ComparatorSet editions; any face citing editions includes `BridgeCard + UTS` row per MVPK/UNM).
* `SenseCells[]` (at least two per row), each citing Context name + edition (F.17/E.10 discipline; UTS-wide coverage rules still apply).
* *(REQUIRED when publishing)* `CorrespondenceRef[]` — ISO 42010 correspondences linking emitted faces to the engineering view(s) they implement; can cross architecture descriptions.
* *Optional support* `ConcernsCovered[]` — ISO 42010 stakeholder concerns addressed by this row via GateProfiles/check catalogues.

**Conformance (S12-scoped, only when `ViewpointMap` is live).**
(i) `UTS.ViewpointMap` exists when a viewpoint-family mapping claim is made or consumed.
(ii) For each holon that claims TEVB alignment, there are at least four rows whose `{ViewFamilyId, EngineeringVPId}` cover `{VF.TEVB.ENG × {VP.Functional, VP.Procedural, VP.RoleEnactor, VP.ModuleInterface}}` (per CC-TEVB-1/6).
(iii) Rows that carry edition identifiers also include `BridgeCard + UTS` rows through `F.9`, `F.17`, `E.17`, and `E.18`; edition-bearing faces that lack such rows are not admissible for downstream consumption.
(iv) Each row has at least two `SenseCells` and the sheet meets global UTS coverage rules.
(v) Any `TargetHolon = U.System` that reaches `U.Work` shows `LaunchGate` with `DesignRunTag` consistency.
(vi) Crossings referenced in `ViewpointMap` follow CC-TGA-11; comparability along the mapped paths follows CC-TGA-10.
(vii) Rows do not use an unqualified `ViewpointId`; they use `EngineeringVPId` and/or `PublicationVPId` explicitly.
(viii) When faces are published, `CorrespondenceRef[]` is present and resolvable to `U.Viewpoint` ids.
(ix) Additional bundles (e.g. assurance, information, mission) can appear as extra `ViewFamilyId` values but are declared as `U.ViewpointBundle` species; they do not extend `VF.TEVB.ENG`.

