**Unknown‑first discipline.** Author S2 with `unknown` traits rather than coercions; **SoS‑LOG** branches MUST specify `{admit|degrade|abstain|sandbox}` handling for `unknown` via closed enums registered at UTS.
Un-typed “problems” collapse into **informal prose**; selectors cannot **filter/abstain** lawfully; thresholds leak into scoring; cross-Context reuse is by name, not Bridge. We need a Context-local descriptor that (i) obeys **MM-CHR legality** (Scale/Unit/Polarity proven before any aggregation), (ii) records **Assurance lanes (TA/VA/LA)** per **A.10** and **ReferencePlane**, (iii) carries **tri-state unknowns** explicitly, and (iv) **publishes crossing attestations** (**BridgeCard + UTS row**) with **Φ(CL)/Φ_plane** policy-ids.
Un‑typed “problems” collapse into **informal prose**; selectors cannot **filter/abstain** lawfully; thresholds leak into scoring; cross‑Context reuse is by name, not Bridge. We need a Context‑local descriptor that (i) obeys **MM‑CHR legality** (Scale/Unit/Polarity proven before any aggregation), (ii) records **

### C.22:3 - Problem

Without typed descriptors, **Eligibility/Acceptance** degenerate into prose; **illegal ops** creep in (ordinal means; unit mixing); **cross‑plane comparisons** lose **CL/Φ** routing (**penalties to R_eff only**). 

### C.22:4 - Forces

| Force                        | Tension                                                                                                                           |
| ---------------------------- | --------------------------------------------------------------------------------------------------------------------------------- |
| **Parsimony vs sufficiency** | Fewer fields to avoid ceremony **vs** enough to drive lawful gating.                                                              |
| **Unknowns**                 | Many traits are **unknown** at intake → tri‑state semantics must propagate to Acceptance without silent coercions.                |
| **CHR legality**             | **No mean on ordinals; no unit mixing**; polarity & scale type must be declared *before* aggregation.                             |
| **Locality vs portability**  | Problem is **in‑room**; still must cross **via Bridges**, with **CL** and (if planes differ) **CL^plane** penalties → **R** only. |


### C.22:5 - Solution — **Problem‑CHR** (fields) + **TaskSignature (S2) binding** *(normative)*

#### C.22:5.1 - Minimal CHR fields (tri‑state aware).
Each field is **CHR‑typed** (Characteristic/Scale/Unit/Polarity; MM‑CHR discipline). Every predicate admits `unknown` (tri‑state). Unknowns must propagate to {degrade|abstain|sandbox} per Acceptance/EvidenceProfile policy (recorded in SCR). (G.4/G.6 alignment)

* **`DataShape`** — data regime & admissible transforms (e.g., tabular, sequence, graph; density; stationarity claims).
* **`NoiseModel`** — uncertainty class / robustness envelope (e.g., iid Gaussian; heavy‑tailed; adversarial budget).
* **`ObjectiveProfile`** — objective heads (**Scale/Unit/Polarity** and **ReferencePlane** declared), polarity, and **lawful orders** (lexicographic, Pareto, medoid/median where legal). **Weighted sums across mixed scale types are forbidden**; ordinal heads use order‑only guards. For QD tasks, explicitly enumerate **Q (quality)**, **D (diversity)**, and **QD‑score** heads; see **DominanceRegime** below.
* `RegularityTraits` — method‑relevant structure (**convexity/differentiability/separability/monotonicity**) as CHR‑typed predicates with guard‑macros (e.g., `ORD_COMPARE_ONLY`, `UNIT_CHECK`, `POLARITY_CHECK`). Include `ConditionClass` (e.g., stiffness/κ‑proxies) where applicable.
* **`Constraints`** — explicit hard/soft constraint classes (feasibility predicates; **ResourceEnvelope**/**RiskEnvelope**). **Thresholds live in Acceptance (G.4) only; never inside CHR or code paths.**
* **`ShiftClass/Stationarity`** — CHR‑typed claims about regime stability (iid | covariate‑shift | concept‑drift | adversarial). Default=`unknown`. Acceptance/Flows MUST honor this in gating or abstain.
* `EvidenceGraphRef (A.10)` — carriers & **lane tags (TA/VA/LA)** with **freshness windows**; **no self‑evidence**; default Γ‑fold = **weakest‑link** unless CAL proves an alternative.
* `ScopeSlice(G)` — **USM** slice of **describedEntity/scope** to bound claims (discipline governance in **CG‑Spec**; Domain is a catalog mark only).
* `Size/Scale` — size/condition proxies (**n, m, κ, sparsity**) with **declared units**; unit mismatch ⇒ {sandbox|refuse}.
* **`Freshness`** — validity window for descriptors.
* `Missingness` — **MCAR/MAR/MNAR** (or mapped equivalents) per **CHR.Missingness**; MUST be honoured by Acceptance/Flows.
* `KindSet` — **`U.Kind[]`** of objects‑of‑talk addressed by the TaskKind; separates **describedEntity (Kind)** from **Scope (USM)**.

**QD / Illumination extensions (normative; ties to C.18/C.19).**
* **`CharacteristicSpaceRef`** — reference to **`U.CharacteristicSpace`**, with declared **d≥2**; **characteristics are CHR‑typed**; **ReferencePlane** per characteristic; pin edition via **`CharacteristicSpaceRef.edition`**.
* **`ArchiveConfig`** — archive **topology** (grid/CVT/graph), **resolution** (bins/centroids), **K‑capacity**, **`InsertionPolicyRef`** (elite replacement/dedup/novelty), and **`DistanceDefRef.edition`** (declare **metric/pseudometric** status and invariances; any normalisation **MUST** cite lawful scale transforms in **CG‑Spec**); legality follows CG‑Spec.
* **`EmitterPolicyRef`** — pointer to emitter/governor policy (C.19) applicable to this TaskSignature; **edition id** recorded.
* **`DominanceRegime`** — `{ParetoOnly | ParetoPlusIllumination}`. **Default = `ParetoOnly`** (illumination remains report‑only telemetry unless CAL explicitly authorises `ParetoPlusIllumination`, policy‑id cited).
* **`IlluminationSummary`** — a **telemetry summary over `Diversity_P`**; **published** by default; excluded from dominance unless a CAL enables `ParetoPlusIllumination` (policy‑id cited).
* **`IlluminationMap`** *(parity‑run)* — required **publication artefact** (grid/CVT/graph per `ArchiveConfig`) recording coverage per niche/cell with `DescriptorMapRef`/`DistanceDefRef.edition`. **Leaderboards as single‑score lists are forbidden**; comparisons **MUST** be under CG‑frames.
* **`PortfolioMode`** — `{Pareto | Archive}`. **Default = `Archive`**: selectors **publish portfolios** (QD archives) rather than a single “best” set; ε‑fronts remain admissible for local decisions under CG‑Spec.
* **`Budgeting`** — evaluation/time/batch **budgets**, including **E/E‑LOG exploration budget** id; units declared (CG‑Spec).
* **`TelemetryHooks`** — **PathSliceId**, **decay/refresh policy ids**, and **edition counters** to record **U.DescriptorMap** and **policy‑id** updates upon illumination gains.
* **`GeneratorIntent`** (OEE) — optional intent to invoke a **`GeneratorFamily`** (G.5) with pointers to **`EnvironmentValidityRegion`**, **`TransferRulesRef`**, and **coverage/regret** reporting expectations.

**Legality.** Before any numeric comparison/aggregation, **prove CSLC legality** (Scale/Unit/Polarity) and **cite CG‑Spec.Characteristics**; publish **ReferencePlane**. **Unknowns** propagate as {degrade|abstain|sandbox}; **no `unknown→0/false` coercions**.

#### C.22:5.2 - TaskSignature (S2) — binding definition (design‑time + run‑time).
A TaskSignature is a minimal typed record the selector consumes:
`⟨Context, TaskKind, KindSet:U.Kind[], DataShape, NoiseModel, ObjectiveProfile, Constraints{incl. Resource/Risk Envelopes}, ScopeSlice(G), EvidenceGraphRef, Size/Scale, Freshness, Missingness, ShiftClass?, BehaviorSpaceRef?, ArchiveConfig?, EmitterPolicyRef?, DominanceRegime?, PortfolioMode?, Budgeting?, TelemetryHooks?, GeneratorIntent?⟩`


**Minimality rule.** S2 carries only fields required for **Eligibility→Acceptance→lawful selection**; any additional traits derived at design‑time are published as provenance (UTS) but **do not expand S2**. 

Values are **CHR‑typed** with **provenance**; traits may be **inferred** from CHR/CAL bindings (e.g., *convexity known? differentiable? ordinal vs interval scales?*) and from **USM** scope metadata. Unknowns are tri‑state; **Missingness semantics MUST align with CHR.Missingness** and be honored by Acceptance/Flows. 

**Design/Run hygiene.** Do not mix DesignRunTag in one signature; **publish GateCrossings** as **CrossingSurface** bundles (**E.18**; Bridge+UTS **A.27**; BridgeCard **F.9**) when importing design‑time traits into run‑time.

#### C.22:5.3 - Provenance & planes.
Record **Context**, **ReferencePlane** for each value; on any cross‑Context/plane reuse, attach BridgeDescription + UTS row, apply **CL** (and, if planes differ, **CL^plane**) penalties to **R_eff only**; both **Φ(CL)** and (if used) **Φ_plane** MUST be **monotone, bounded, and table‑backed**; **no “distance” language; penalties never mutate F/G.** Publish policy‑ids in SCR and cite Bridge ids on crossings.

#### C.22:5.4 - Binding & use.

* **Eligibility** gates read TaskSignature against each **MethodFamily.Eligibility** (C.23) and **CG‑Spec.MinimalEvidence** for referenced characteristics.
* **Acceptance** clauses (G.4) use these fields for **threshold predicates** (thresholds live in Acceptance only).
* **Selection kernel** (G.5.S3) applies a **lawful order** (often partial); **weighted sums across mixed scale types are forbidden**. If only a partial order remains, **return a Pareto (non‑dominated) set** with tie notes. If `PortfolioMode=Archive`, the selector **may** return a **QD archive** (per `ArchiveConfig`) **in addition to** or **instead of** a Pareto set. **Illumination** enters dominance **only** if `DominanceRegime=ParetoPlusIllumination` is **enabled by CAL** (policy id cited); otherwise, QD metrics are **reported** but **excluded** from dominance.
* When `GeneratorIntent` is present, G.5 may dispatch to a registered **`GeneratorFamily`** (POET‑class); the selection surface becomes **pairs** `{environment, method}`, with Environment guarded by **`EnvironmentValidityRegion`** and **`TransferRulesRef`** (C.23 wiring). Report **`IlluminationSummary`** as a **telemetry summary over `Diversity_P`** (report‑only by default) in telemetry; dominance remains unaffected unless policy changes as above.

#### C.22:5.5 - Unknowns.
Every field supports `unknown`; downstream **degrade/abstain/sandbox** behavior is explicit per Acceptance/EvidenceProfile; no implicit coercions. 

#### C.22:5.6 - Publication.
Emit a **ProblemProfile** (…Description) that carries the bound TaskSignature, **UTS** Name Cards for any minted values (twin labels), and SCR‑visible provenance (A.10 anchors, lane tags, freshness, **ReferencePlane**). **Mark any vendor/tool examples as Plain‑register only (LEX V‑4); they are non‑normative.**

#### C.22:5.7 - Open‑Ended tasks (GeneratorFamily) *(normative)*.
If the problem requires **open‑ended generation** of tasks/environments, S2 **SHALL** include `GeneratorIntent` with pointers to **`EnvironmentValidityRegion`** (lawful support of generated environments), **`TransferRulesRef`** (cross‑environment transfer constraints), and **coverage/regret** telemetry expectations. Selector outputs are then portfolios over **{environment, method}**; **coverage/regret** are **telemetry metrics** (reported) and **IlluminationSummary** is a **telemetry summary** (reported), excluded from dominance unless a **CAL** policy promotes them (policy‑id recorded in SCR; see `DominanceRegime`). Edition increments of **CharacteristicSpaceRef.edition**/**DescriptorMapRef.edition**/**DistanceDefRef.edition** and (OEE) **`TransferRulesRef.edition`**, and the **policy‑id** that caused illumination increases **SHALL** be recorded in SCR.


### C.22:6 - Archetypal Grounding (Tell–Show–Show)

*Tell–Show–Show hook (per E.8):* label examples as **Show‑1 (continuous ODE)** and **Show‑2 (MIP)** and cite CHR guard‑macros in‑line so engineers can see **which field drove which gate**.  **Explicitly annotate which S2 fields triggered each Eligibility/Acceptance decision** (e.g., `service_level@ordinal → ORD_COMPARE_ONLY`, `budget@ratio → unit alignment check`).

**A. Differential equations (continuous systems, solver choice).**
*ProblemProfile.* `DataShape=ODE, stiff?=unknown, Size/Scale={n≈10^3}, ObjectiveProfile={↓error@ratio, ↑throughput@ratio}, Constraints={budget≤X, safety_gate@ordinal}, RegularityTraits={Lipschitz known?=unknown, Jacobian sparsity=high}, Missingness=MAR`.
*Binding.* Selector reads TaskSignature; **eligibility** filters MethodFamilies that require known stiffness or differentiability (unknown ⇒ **degrade/abstain** per family); **Acceptance** enforces `safety_gate` as **ordinal predicate**, not averaged (ORD\_COMPARE\_ONLY), and budgets with **unit‑aligned sums** (ratio). The selector returns a **Pareto set**; no cross‑ordinal weighting.

**B. Mixed‑integer optimisation (planning/scheduling).**
*ProblemProfile.* `DataShape=MIP, NoiseModel=deterministic, ObjectiveProfile={↓cost@ratio, ↑service_level@ordinal}, Constraints={SLA hard, workforce soft}, RegularityTraits={convex_relaxation=available}, Size/Scale={vars~10^5}, Missingness=MCAR`.
*Binding.* **CG‑Spec** forbids means over **service\_level** (ordinal); **Acceptance** holds thresholds; **Eligibility** checks convex‑relaxation availability; **Selection** applies **lexicographic** guard (assumption‑fit ≻ evidence‑fit ≻ resource), compute **R\_eff** with Γ‑fold, route **CL** to **R** only; if partial order remains, return a **Pareto set**.

> *Contemporary anchors (informative):* modern **Julia** ecosystems illustrate the “**general call outside, specialised implementations inside**” ethos (e.g., DifferentialEquations.jl, JuMP), aligning with C.22→G.5 multi‑method dispatch under NFL.

**C. Quality‑Diversity portfolio (illumination).**
*ProblemProfile.* `DataShape=policy‑search; ObjectiveProfile={↑reward@ratio, ↑coverage@ratio (report‑only)}, DominanceRegime=ParetoOnly, PortfolioMode=Archive, CharacteristicSpaceRef(d=3, characteristics=CHR‑typed), ArchiveConfig(grid, res=32×32×16, K=1, InsertionPolicyRef=elite‑replace, DistanceDefRef.edition=v1), EmitterPolicyRef=v2, Budgeting{eval=1e6}, TelemetryHooks{PathSliceId=…}`.
*Binding.* Selector may return an **archive**; **coverage/illumination** are **reported** but **excluded** from dominance (default). Any change of `DistanceDefRef.edition`/Emitter policy is **editioned** and logged in SCR.

**D. Open‑ended environment generation (POET‑class).**
*ProblemProfile.* `GeneratorIntent{GeneratorFamilyRef=…, EnvironmentValidityRegion=… (CHR‑typed), TransferRulesRef=…, CoverageMetric=…}`, `PortfolioMode=Archive`.
*Binding.* Selector outputs **{environment, method}** pairs that pass Eligibility; **TransferRules** govern cross‑environment policy reuse; telemetry reports **coverage/regret** and **IlluminationSummary** with **edition/policy‑id** when improved.

### C.22:7 - Bias‑Annotation (LEX/discipline guards)

* **No minted “Strategy” head.** “Strategy/policy” are *roles/lenses* inside G.5; do **not** introduce a new `U.Type` “Strategy”.
* **No minted `U.Type` “Strategy”.** Strategy/policy are roles/lenses inside G.5 Compose under E/E‑LOG; keep “strategy” as Plain where pedagogically needed.
* **Transdiscipline vs domain.** Comparability flows through **`U.Discipline` CG‑Spec**; “Domain” is a catalog mark stitched to D.CTX + UTS; do **not** attach norms to Domain labels.
* **Plain twins & head‑anchoring.** Use Description/Spec morphology correctly (I/D/S; E.10.D2). 

### C.22:8 - Anti‑patterns (normative):
* **AP‑1** Pre‑binding a Method into S2 (“problem as if task”); **Remedy:** keep S2 method‑agnostic; bind only lawful traits.
* **AP‑2** Silent `unknown→false/0` in Eligibility/Acceptance.  
* **AP‑3** Cross‑ordinal averaging / ordinal–interval scalar mixes.  
* **AP‑4** **Design/run chimera** signatures (mixing stances).  
* **AP‑5** **Domain** treated as governance (attach governance to **U.Discipline/CG‑Spec**, not Domain).  
* **AP‑6** Implicit handling of data‑shift (assume iid); **Remedy:** declare `ShiftClass` (or `unknown`) and gate via Acceptance.
* **AP‑7** Tool/vendor tokens in normative text; **Remedy:** move to Plain‑register note; keep Tech anchors on CHR/CAL ids (LEX V‑4).
**Remedies:** tri-state predicates; lawful orders (lexi/Pareto/median/medoid); **GateCrossing visibility** via Bridge+UTS+CL/CL^plane (penalties → R only); Domain stitched to **D.CTX + UTS** only.
**Remedies:** tri‑state predicates; lawful orders (lexi/Pareto/median/medoid); explicit **GateCrossing** publication via **CrossingSurface** (BridgeCard + UTS row + `CL/Φ` policy‑ids; **E.18/A.27/F.9**); Domain stitched to **D.CTX + UTS** only.

### C.22:9 - Conformance Checklist (normative)

0. **Minimal S2.** S2 contains only fields necessary for Eligibility/Acceptance/selection; any extra derived traits remain provenance.
1. **TaskSignature present (S2).** All TaskKinds **publish** a TaskSignature with all fields declared and **CHR‑typed**; `unknown` supported for each.
2. **CHR legality proven.** Any numeric comparison/aggregation **cites CG‑Spec** by **Characteristic id** and proves **CSLC legality**; **no mean on ordinals; no unit mixing**.
3. **Unknowns propagate.** Unknowns **must** map to {pass|degrade|abstain} in **Acceptance**/**Eligibility**; no implicit coercions; behavior recorded in **SCR**.
4. **Evidence lanes.** **A.10 anchors** + **Assurance lanes (TA/VA/LA)** + **freshness windows** recorded; **Γ‑fold** default=weakest‑link unless proved otherwise.
5. **ReferencePlane guarded.**  ReferencePlane noted **per value and per ObjectiveProfile head**; on crossings apply **CL** (and **CL^plane** if planes differ); **Φ(CL)/Φ_plane** are **monotone, bounded, table‑backed and documented in the `CG‑Spec`**; penalties → **R_eff only** (F/G invariant).
6. **Acceptance thresholds live in CAL.** No thresholds in CHR or code paths; only in **G.4 AcceptanceClauses**. 
7. **Selector legality.** Selection uses **admissible (possibly partial) orders**; **weighted sums across mixed scale types are forbidden**; return a **Pareto set** when appropriate. 
8. **Crossings published (visibility).** Any cross-stance/cross-Context reuse emits **BridgeCard/BridgeDescription + UTS row** with CL notes and (if planes differ) CL^plane + Φ_plane.
9. **UTS twin labels.** All exported cards publish **Name Cards** with twin labels; Bridges carry loss notes. 
10. **GateCrossing checks.** Published TaskSignature and any referenced crossings satisfy: (i) stance tagging (if used; informative only), (ii) **CrossingSurface** presence/consistency (**E.18**; **A.27**; **F.9**), (iii) **LanePurity** (CL→R only; F/G invariant; Φ tables present), and (iv) **Lexical SD** (**E.10**). Failures are **blocking** under the active GateProfile / GateChecks (**A.21**).
11. **QD fields (when QD is in scope).** If `PortfolioMode=Archive` or QD heads are present, **CharacteristicSpaceRef** (d>=2), **ArchiveConfig** (topology, resolution, K, `InsertionPolicyRef`, `DistanceDefRef.edition`), and **EmitterPolicyRef** **SHALL** be present and CHR-typed; characteristics declare **ReferencePlane**.
12. **DominanceRegime default.** `DominanceRegime` **defaults to `ParetoOnly`**; inclusion of illumination in dominance **MUST** be enabled by a **CAL.Acceptance policy**; the policy id **SHALL** be published in SCR.
13. **Telemetry.** **PathSliceId**, **refresh/decay policies**, and **edition counters** for **CharacteristicSpaceRef**/**DistanceDefRef**/**EmitterPolicyRef** **SHALL** be recorded; any illumination increase **SHALL** log the **policy-id** that triggered it.
14. **GeneratorIntent (when OEE is in scope).** `GeneratorIntent` **SHALL** cite **`EnvironmentValidityRegion`** and **`TransferRulesRef`** (ids resolvable in G.5/C.23); absence => `Abstain` for OEE dispatch.
15. **Budgets.** `Budgeting` (eval/time/batch) **SHALL** declare units and E/E-LOG exploration budget id when used.
16. **Archive legality.** `DistanceDefRef.edition` and any novelty measures **SHALL** be CSLC-lawful and **editioned**; illegal ops => **Abstain**.
17. **Planes.** **ReferencePlane** **SHALL** be declared for all QD heads/axes; plane crossings apply **Phi\_plane** (penalty to **R** only).
18. **Unknowns.** Unknown QD fields **map** to `{degrade|abstain|sandbox}`; no coercions.

### C.22:10 - Interfaces & Data Paths

*Inputs.* `ProblemProfile` (…Description), CG-Spec ids, Evidence Graph Ref (A.10), D.CTX; (if QD) CharacteristicSpaceRef/ArchiveConfig/EmitterPolicyRef configs; (if OEE) GeneratorIntent.
 *Produces.* `TaskSignature@Context` (S2) with provenance; **SCR-visible** fields; UTS Name Cards for any minted traits; (if QD/OEE) archive/portfolio semantics and telemetry hooks declared.
 *Consumed by.* **G.5** (Eligibility/Selection kernel), **G.4** (Acceptance/Evidence), **C.23** (admit/degrade/abstain rules; maturity ladder).

### C.22:11 - Consequences (informative)

* **Lawful selection.** Dispatch is **explainable** and **audit-ready**; every reason in/out cites TaskSignature fields, CG-Spec rows, and Gamma-fold contributors. 
* **Local first, portable later.** Context-local semantics are primary; Bridges make portability **deliberate and costed** (penalties to **R** only). 
* **Frictionless downstream.** G.1-G.5 consume a **single, typed** Standard; thresholds are cleanly separated into **Acceptance**; unknowns are not guessed.
* **QD/OEE-ready.** Typed QD and GeneratorIntent fields make **portfolio** and **open-ended** workflows **first-class**, with lawful dominance, editioned distances, and policy-aware illumination.

### C.22:12 - Relations
**Builds on:** **C.16 MM-CHR**, **G.0 CG-Spec**. **Coordinates with:** **G.4 Acceptance**, **G.5 Selector**, **C.18 NQD-CAL**, **C.19 E/E-LOG**, **C.23 Method-SoS-LOG**. **Constrained by:** **E.10 (LEX/I/D/S)**, **E.18 (GateCrossing visibility / publication gating)**.

### C.22:13 - Author's quick checklist

1. **Write the ProblemProfile.** Context, TaskKind, ObjectKinds, USM **ScopeSlice(G)**, describedEntity (GroundingHolon, ReferencePlane). 
2. **Fill TaskSignature (S2).** Populate all fields; mark `unknown` explicitly; align **Missingness** with CHR semantics. 
3. **Bind CG-Spec ids.** For any numeric comparison/aggregation you expect downstream, cite **CG-Spec.Characteristics** and prove **CSLC** legality. 
4. **Attach Evidence Graph Ref.** Lanes (TA/VA/LA), carriers, freshness windows; set **Gamma-fold** default; no self-evidence. 
+5. **Publish crossings.** If importing across a **GateCrossing** boundary, mint **BridgeDescription + UTS row**; record **CL/CL^plane**; penalties **→ R only**. 
6. **Keep thresholds in Acceptance.** Move any thresholds (gate numbers) into **G.4**;  wire **RSCR** refusal tests (illegal ops; unit/scale checks; **tri-state unknowns**; CL->R routing; **Phi tables present**).
7. **Run GateCrossing checks** on the signature and crossings: stance tagging (if used; informative only), **CrossingSurface** presence/consistency (**E.18/A.27/F.9**), **LanePurity**, and **Lexical SD** (**E.10**); attach **UTS Name Cards** with twin labels.
8. **Bias audit.** Check E.5.4 and C.21 hooks if the problem lives *inside* a discipline dashboard or SoTA pack.


### C.22:14 - Goldilocks hook (design‑time)

When generating candidate solutions for a **TaskKind**, target **“goldilocks”** slots (feasible‑but‑hard) so that the TaskSignature is informative (neither trivial nor impossible); this aligns with **G.1** (target goldilocks, abductive provenance) and ensures the **TaskSignature is informative** (neither trivial nor impossible) for **G.5** selection.

### C.22:End

## C.23 - MethodFamily Evidence & Maturity (Method‑SoS‑LOG)

*LOG (logic) for deductive shells for admissibility*
*First use expansion:* **SoS‑LOG = Science‑of‑Science LOG** (LEX short‑form discipline applied).

**HomeContext.** For this pattern, *HomeContext* means the `U.BoundedContext` where a `MethodFamily` is registered (LEX D.CTX).

**Builds on.** **G.5** (MethodFamily registry/selector), **G.4** (Acceptance & EvidenceProfiles), **C.22** (TaskSignature S2), **C.18 NQD‑CAL** (QD/illumination), **C.19 E/E‑LOG** (emitters/policies), **B.3** (Assurance lanes & `R_eff`), **A.10** (Evidence Graph Ref), **E.10** (LEX), **E.18** (GateCrossing / CrossingSurface visibility). **Coordinates with.** **G.6** (EvidenceGraph), **G.8** (LOG bundling), **G.9** (Parity), **G.11** (Refresh).     

### C.23:1 - Problem frame

Families of methods compete inside a CG‑Frame. The selector (G.5) must **admit, degrade, or abstain** per family **without** universal scores, using **typed** problem descriptors and **auditable** evidence. Maturity of a family (how far it has travelled from “clever idea” to “run‑safe”) must be **visible to LOG** rules yet **separate from thresholds** (which live only in **AcceptanceClauses**, G.4). 

### C.23:2 - Problem

Unstructured “readiness” stories and undisciplined evidence lead to:

* (i) **Illicit scalarisation** across mixed scale types,
* (ii) **Prose‑only** gating that a dispatcher cannot execute,
* (iii) Cross‑Context reuse without Bridges/CL, and
* (iv) Immature families leaking into production.
  We need a **notation‑independent LOG layer** that turns **TaskSignature (S2)** + **EvidenceProfiles** into **executable rules** for *admit / degrade / abstain*, **routing any CL penalties to `R_eff` only** (never mutating **F/G**). 

### C.23:3 - Forces

* **Pluralism vs. dispatchability.** Competing Traditions expose different invariants; selection must compare **without semantic flattening**.
* **Maturity vs. opportunity.** Open‑ended exploration (E/E‑LOG) must coexist with **run‑safe** exploitation; *immature ≠ forbidden* → provide safe **degrade** paths.
* **Unknowns (tri‑state).** Missing or `unknown` S2 fields must propagate **explicitly** to *degrade/abstain/sandbox*; no silent coercions.
* **Lexical discipline.** Head‑anchoring, I/D/S separation, Bridge hygiene; **no tool names in Core**.


### C.23:4 - Solution — **Method‑SoS‑LOG**: deductive shells over Eligibility & Evidence

#### C.23:4.1 - Objects & heads (LEX/I‑D‑S)

*Tech heads; Plain twins are published via UTS.*
**`MethodFamily`** (registered in G.5) carries **Eligibility** and artefact identity; **`MaturityCard`** (this pattern) carries evidence‑aware maturity; **`SoS‑LOG.Rule`** (this pattern) is an executable rule schema that returns one of `{Admit | Degrade(mode) | Abstain}` for a `(TaskSignature, MethodFamily)` pair. Descriptions live as `…Description`; when harnessed they become `…Spec`. 

#### C.23:4.2 - Rule schema (normative)

For each `MethodFamily` **f**, author an **executable** rule set:

```
LOG.Deduce_f(TaskSignature S2) → {Admit | Degrade(mode) | Abstain}
```

with the following **branch obligations**:

**R0 — CG‑Spec gate (precondition, HomeContext).** Before R1–R3, verify **CG‑Spec.MinimalEvidence** for every CHR characteristic referenced by *f*’s Acceptance/Flows **in the home Context**; failure ⇒ `Abstain` with reasons (no silent sandbox). Publish the **CG‑Spec ids** consulted. 
*Rationale:* selector legality requires the CG‑Spec gate to be explicit, not implicit in prose. Publish associated **ReferencePlane** notes alongside the consulted ids.

**R0.QD — QD/OEE pre‑gates (if applicable).** If S2 declares **BehaviorSpaceRef/ArchiveConfig/EmitterPolicyRef** or `PortfolioMode=Archive`, verify:
(i) **CharacteristicSpaceRef** characteristics are CHR‑typed, d≥2, **ReferencePlane** per characteristic declared;
(ii) **ArchiveConfig** is lawful (topology, resolution, **K**>0, `InsertionPolicyRef`, `DistanceDef` with **edition id** and declared metric/pseudometric status);
(iii) **EmitterPolicyRef** present (with **edition id**);
 (iv) **DominanceRegime** present; if absent, **default= ParetoOnly**.
 Failure of any ⇒ `Abstain` with reasons.

**R1 — Admit.** `Admit` **IFF**
(a) S2 satisfies **Eligibility** predicates of *f* (tri‑state aware),
(b) **EvidenceProfile minima** referenced by Acceptance/Flows for *f* are met (lanes/anchors/freshness) **in the home Context** (post R0),
(c) all relevant **CAL.AcceptanceClauses** (G.4) evaluate to true under lawful CHR comparisons,
(d) any **maturity gating** (e.g., a floor on Maturity rungs) is expressed as an **AcceptanceClause** and referenced here by id (no thresholds inside LOG).
*LOG never sets thresholds; it only executes and cites Acceptance verdicts.*

**R2 — Degrade.** If (a) holds but (b) or (c) is **partially** satisfied or **unknown**, return `Degrade(mode)` where `mode ∈ {scope‑narrow | sandbox | probe‑only}` and **emit scope notes** (USM Scope(G), Γ_time). Record which S2 unknowns or Evidence minima caused the degrade. **LOG‑Degrade** never changes **CHR scales or planes**; it **narrows Scope (G)** or **execution mode**. 
**Note (CAL vs LOG).** CAL‑level **`degrade.order`** (fall‑back to order‑only comparisons) is governed by **G.4**/**CG‑Spec** and is **not** a LOG mode. **SoS‑LOG never overrides CAL outcomes**; a LOG branch **only narrows** `Scope(G)` or **execution mode** (e.g., `sandbox`, `probe‑only`), it **does not** alter CHR scales or admissible orders.
`probe‑only` MUST cite an **E/E‑LOG policy id** (exploration budget) and Acceptance‑bound guards.

**R3 — Abstain.** If S2 violates **Eligibility** *or* **R0** fails, return `Abstain` (with reasons). **Abstain** is mandatory on **illegal CHR operations** (e.g., ordinal means) and when **Bridge/CL** requirements are unmet. 

**R4 — CL routing.** Any cross‑Context/plane reuse must cite **Bridge ids** (with loss notes). Apply **Φ(CL)** and (if planes differ) **Φ_plane** that are **monotone, bounded, table‑backed**; **publish policy‑ids** in the SCR; **penalties reduce `R_eff` only**; **F/G must remain invariant**.

**R5 — Proof hooks.** Every branch **MUST** cite **Evidence Graph Ref** (A.10), lane tags (TA/VA/LA), freshness windows, and (if bridged) **Bridge ids + loss notes**; the decision is **SCR‑visible**. When **G.6 EvidenceGraph** is present, also **publish EvidenceGraph path id(s)** for the branch (admit/degrade/abstain). **No self‑evidence**.

**R6 — QD portfolio semantics (if applicable).** If `PortfolioMode=Archive`, `Admit` may return a **QD archive** (per `ArchiveConfig`) instead of only a Pareto set. Unless **CAL** authorises `DominanceRegime=ParetoPlusIllumination` (**policy‑id recorded in SCR**), **IlluminationSummary** is a **report‑only telemetry summary** and any **coverage/regret** are **telemetry metrics** (reported) that **do not** affect dominance.

**R7 — GeneratorFamily branches (open‑ended).** If S2 includes `GeneratorIntent`, SoS‑LOG **MUST**:
 (i) verify **`EnvironmentValidityRegion`** is declared and lawful;
 (ii) verify **`TransferRulesRef`** exists; if `unknown` ⇒ `Degrade(scope‑narrow)` or `Abstain` per family policy;
 (iii) treat the selection surface as **pairs `{environment, method}`**; publish **coverage/regret** and **IlluminationSummary** as **report‑only telemetry** (IlluminationSummary = telemetry summary; coverage/regret = telemetry metrics); dominance participation per **R6**.

**R8 — Telemetry & Refresh hooks.** On any illumination increase or archive change, publish **edition increments** for **CharacteristicSpaceRef**/**DistanceDefRef** and the **policy‑id** (Emitter/Acceptance) that caused the change; expose **PathSliceId** for refresh/decay in SCR.

> *Aphorism.* **“Admit on lawfulness and sufficiency; degrade on uncertainty; abstain on illegality.”**

#### C.23:4.3 - Maturity ladder (poset, not a scalar; Description, not Spec)

Publish a **`MethodFamily.MaturityCardDescription@Context`** (UTS enum ids; **Scale kind = ordinal**; **ReferencePlane declared**). Do **not** embed thresholds here; any **maturity floors** used for admission are authored as **G.4 AcceptanceClause** and referenced by id from R1.

* **L0 — Anecdotal.** Claims exist; lanes sparse; examples ad‑hoc.
* **L1 — Worked‑Examples.** Multiple **worked examples** with lane tags and **Scope slices** declared; *no replication yet*.
* **L2 — Replicated.** Independent replication(s) in distinct Context slices (publish D.CTX + UTS rows), lane separation observed, decay windows explicit.
* **L3 — Benchmark‑Severe.** Repeated wins or parity on **community baselines** or **severe tests**; cross‑Tradition bridges declared with **loss notes**.

*Optional rung (for QD/OEE‑heavy families; ordinal, closed enum):*
* **L4 — QD‑Hardened.** Archive stability under declared **InsertionPolicy/DistanceDef** editions; reproducible **IlluminationSummary** improvements under controlled budgets; OEE generators pass **EnvironmentValidityRegion** severe tests.

**Norms.**
**M1.** The ladder is **lane‑aware** (TA/VA/LA) and **freshness‑aware**; it is **not** a global numeric score. Declare **Scale kind=ordinal** and the **closed enumeration** of rungs; register the enum at **UTS** (twin labels; editioned).
**M2.** Transitions **MUST** be justified by **EvidenceGraph** paths (once G.6 is available) and UTS publication; missing anchors ⇒ no advance.
**M3.** Any **maturity floor** used for admission (e.g., “run‑critical Context requires ≥L2”) **MUST** be authored as a **CAL.AcceptanceClause** and referenced by id from R1; SoS‑LOG does **not** embed thresholds.
**M4.** Declare **ReferencePlane** for the MaturityCard; on ReferencePlane crossings apply published **Φ_plane** policy (penalty to **R_eff only**), with Bridge id and loss notes.

> *Rationale note.* Treating maturity as a **poset** aligns with B.3’s lane calculus and avoids **scalarisation across ordinal/ratio** scales; assurance penalties remain on **R**, never **F/G**.

#### C.23:4.4 - Unknowns & Shift classes (tri‑state discipline)

**U1. (LEX).** Enumerations for `Degrade(mode)` and Maturity rungs **MUST** be declared as **closed value sets** and **registered at UTS** (twin labels). **Lexical SD** (**E.10**) applies.
**U2.** Every S2 field is tri‑state; `unknown` **MUST** map to a branch (`Degrade` or `Abstain`) declared on the **family** (no coercions). Each branch publishes a **branch‑id** and (where used) a `mode` from a **closed enum** registered at **UTS** (LEX enum clarity).
**U3.** `ShiftClass` semantics follow **C.22**. If `ShiftClass ∈ {covariate‑shift, concept‑drift, adversarial}` or `unknown`, default outcome is `Degrade(scope‑narrow)` unless a CAL.AcceptanceClause explicitly guards the regime.

#### C.23:4.5 - Publication & wiring

**W1.** Each family publishes a **`MaturityCardDescription@Context`** (UTS twin labels; ReferencePlane declared) and **registers SoS‑LOG rule ids**; editions are versioned and **RSCR‑tested for branch‑coverage** (Admit/Degrade/Abstain, unknown paths). **Φ(CL)/Φ_plane policy‑ids** must be present in SCR where applicable.
**W2. Admissibility Ledger.** Publish an **`AdmissibilityLedger@Context`**: rows = `(MethodFamilyId, RuleId, MaturityRung, BranchIds, BridgeIds, ΦPolicyIds, EvidenceGraphPathIds?, DominanceRegime, PortfolioMode, Edition)`, UTS‑registered; this ledger is the **selector‑facing** export.
**W3. Strategy token.** Do **not** mint a `U.Type` “Strategy”; strategy remains a **composition** inside G.5 (`Compose`) under **E/E‑LOG**.
**W4.** Selector (G.5) **consumes** these rules; results appear in the **Dispatcher Report** with reasons in/out and cited anchors/bridges.

### C.23:5 - Archetypal Grounding (Tell–Show–Show)

*(Plain register for pedagogy; Core remains notation‑independent per E.10/E.8.)*

**Show‑1 - Continuous dynamics (ODE task).**
*S2 excerpt.* `DataShape=ODE; stiff?=unknown; Size≈10^3; Objective={↓error@ratio, ↑throughput@ratio}; Constraints={safety_gate@ordinal}; Jacobian_sparsity=high; Missingness=MAR`.
*Families.* `Implicit‑BDF` vs `Explicit‑RK` vs `Symplectic`.
*Rules.*
— `Implicit‑BDF`: **Eligibility** tolerates `stiff?=unknown` if `Jacobian_sparsity=high` (guarded precondition); **MaturityCard**=`L3` (replicated & benchmarked). Outcome: `Admit`.
— `Explicit‑RK`: requires `stiff?=false`; with `unknown` ⇒ `Degrade(sandbox)` (probe).
— `Symplectic`: eligible only when `Hamiltonian=true`; here ⇒ `Abstain`.
*Didactic anchor.* This mirrors C.22’s typed‑signature discipline and CHR legality (no ordinal means; unit alignment for **ratio**).

> Contemporary ecosystem examples of these families (post‑2015) are organised in **DifferentialEquations.jl**, which exposes multiple solver **families** under one call surface—precisely the pattern G.5 expects. ([Journal of Open Research Software][17])

**Show‑2 - Planning/scheduling (MIP task).**
*S2 excerpt.* `DataShape=MIP; NoiseModel=deterministic; Objective={↓cost@ratio, ↑service_level@ordinal}; Size≈10^5 vars; convex_relaxation=available`.
*Families.* `MILP (branch‑and‑bound)`, `Constraint‑Programming`, `Heuristic meta‑search`.
*Rules.*
— `MILP`: **Eligibility** requires `convex_relaxation=available`; **MaturityCard**=`L3` in the home Context ⇒ `Admit`.
— `Constraint‑Programming`: **MaturityCard**=`L2`; Acceptance demands `service_level≥B` (ordinal predicate). With `B` met but baseline parity unknown ⇒ `Degrade(scope‑narrow)`.
— `Heuristic meta‑search`: **MaturityCard**=`L1` ⇒ `Degrade(sandbox)` or `Abstain` depending on RSCR parity policy.
*Didactic anchor.* Selector returns a **Pareto set** (no cross‑ordinal weighting), as required by G.5.

> Contemporary “single call / many solvers” packaging that motivates MethodFamily rows is exemplified by **JuMP** (2017–2022), which cleanly separates **model description** from solver choice. ([Miles Lubin][18])

— *DifferentialEquations.jl* illustrates **family‑based** solver packaging (multi‑method under one interface), 2017–2024 ecosystem. ([Journal of Open Research Software][17])
— *JuMP* illustrates **model/solver separation** and registry‑like selection (2021–2022 papers, site). ([Miles Lubin][18])
— *Science of Science* review (2018) supports the emphasis on replication/benchmarks in maturity assessment. ([Science][19])

**Show‑3 - QD archive (policy search).**
*S2 excerpt.* `PortfolioMode=Archive; CharacteristicSpaceRef(d=2); ArchiveConfig(CVT, res=1k cells, K=1, DistanceDefRef.edition=v2, InsertionPolicyRef=dyn‑elite); EmitterPolicyRef=v3; DominanceRegime=ParetoOnly`.
*Rules.* `Admit` returns an **archive**; illumination **reported**; changes to `DistanceDef`/Emitter **editioned** in SCR; dominance remains **ParetoOnly**.

**Show‑4 - Open‑ended GeneratorFamily (POET‑class).**
*S2 excerpt.* `GeneratorIntent{GeneratorFamilyRef=GF‑01, EnvironmentValidityRegion=EVR‑A, TransferRulesRef=TR‑A, CoverageMetric=…}; PortfolioMode=Archive`.
*Rules.* `Admit` yields portfolios over `{environment, method}`; `Degrade(scope‑narrow)` if `TransferRules`=`unknown`; telemetry publishes **coverage/regret** and **IlluminationSummary** with **edition/policy‑id** on improvements.

[17]: https://openresearchsoftware.metajnl.com/articles/10.5334/jors.151 "DifferentialEquations.jl – A Performant and Feature-Rich … "
[18]: https://mlubin.github.io/pdf/jump-sirev.pdf "JuMP: A Modeling Language for Mathematical Optimization"
[19]: https://www.science.org/doi/10.1126/science.aao0185 "Science of science"

### C.23:6 - Bias‑Annotation

**Principle‑taxonomy lenses.** *Universality* (trans‑discipline), *Didactic primacy* (Tell–Show–Show), *Open‑ended evolution* (refresh‑ready), *Lexical firewall* (no tool names in Core), *Notation independence*. Limits: Worked examples reference widely‑used ecosystems **in Plain register** only. 

### C.23:7 - Conformance Checklist (normative)

| ID           | Requirement                                                                                                                                                                                | Purpose                                       |                                                                    |                        |
| ------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | --------------------------------------------- | ------------------------------------------------------------------ | ---------------------- |
| **CC‑C23.1** | Each `MethodFamily` **SHALL** publish a `MaturityCard` with rung justification via **A.10** anchors (lanes, freshness windows) and (if bridged) **Bridge ids** with **CL** and loss notes. | Makes maturity **auditable** and lane‑typed.  |                                                                    |                        |
| **CC‑C23.2** | `SoS‑LOG` rules **MUST** be **executable** (no prose‑only) and cite: Eligibility test result; CG‑Spec gate verdict; EvidenceProfile minima; Acceptance verdict; Γ‑fold contributors; **EvidenceGraph PathId/PathSliceId**; CL/Φ policy‑ids. |
| **CC‑C23.3** | Enumerations used by the rules (**Degrade(mode)**; Maturity rungs) **SHALL** be **closed** and **UTS‑registered** (twin labels). |
| **CC‑C23.4** | **Unknowns** in S2 **SHALL** map to `{degrade | abstain | sandbox}` with explicit **branch‑ids**; no `unknown→0/false` coercions.                                                          | Tri‑state discipline.                          |                                                                    |                        |
| **CC‑C23.5** | Cross‑Context/plane use **MUST** cite a **Bridge**; **Φ(CL)**/**Φ\_plane** **MUST** be monotone, bounded, table‑backed; penalties **→ `R_eff` only**.                                      | Keeps F/G invariant; legal CL routing.        |                                                                    |                        |
| **CC‑C23.6** | **No thresholds** in CHR or Maturity; thresholds **live only** in **AcceptanceClauses** (G.4).                                                                                             | Separation of concerns.                       |                                                                    |                        |
| **CC‑C23.7** | `MaturityCard` **SHALL NOT** be turned into a global scalar; treat as **poset**; any ordering **MUST** be lawful over CHR types.                                                           | Forbids cross‑scale scalarisation.            |                                                                    |                        |
| **CC‑C23.8** | Publish to **UTS** with twin labels; run **GateCrossing visibility checks** on cited crossings: **CrossingSurface** attestation (**E.18/A.27/F.9**), **LanePurity**, and **Lexical SD** (**E.10**) under GateChecks/GateProfile (**A.21**). | Publication & crossing visibility hygiene. |                                                                    |                        |
| **CC‑C23.9** | All enumerations (e.g., `Degrade(mode)`, Maturity rungs) **SHALL** declare a **closed value set** and **Scale kind**, and be registered at UTS (LEX enum clarity).                          | Avoids lexical drift; lawful typing.          |                                                                    |                        |
| **CC‑C23.10** | **RSCR tests** cover negative/refusal paths (illegal CHR ops; CG‑Spec gate fail; Bridge missing; **Φ table/policy‑id missing**; **Lexical SD violations (E.10)**); ensure **branch coverage** (Admit/Degrade/Abstain, unknown). |
| **CC‑C23.11** | If QD fields are in scope, **R0.QD** **MUST** pass: lawful **CharacteristicSpaceRef** (d≥2, characteristics typed, planes declared per characteristic), **ArchiveConfig** (topology/resolution/K, `InsertionPolicyRef`, **editioned** `DistanceDef`), **EmitterPolicyRef** present. | QD legality gate. | |
| **CC‑C23.12** | **DominanceRegime** **SHALL** default to `ParetoOnly`; switching to `ParetoPlusIllumination` **MUST** be authorised by **CAL** and cited by id in SCR.                                    | Prevents implicit scalarisation.              |                                                                    |                        |
| **CC‑C23.13** | If `PortfolioMode=Archive`, LOG **MUST** allow archive outputs (R6) and publish **IlluminationSummary** as a report-only telemetry metric unless CAL opts‑in to dominance participation.                         | Lawful archive semantics.                     |                                                                    |                        |
| **CC‑C23.14** | If `GeneratorIntent` present, **R7** **MUST** verify **EnvironmentValidityRegion** and **TransferRulesRef**; outputs are **{environment, method}** portfolios; coverage/regret telemetry published. | OEE legality & telemetry. | |
| **CC‑C23.15** | On illumination increases/archive changes, **edition increments** (BehaviorSpace/DistanceDef/EmitterPolicy) and the **policy‑id** responsible **SHALL** be logged (R8).                   | Reproducibility & refresh.                    |                                                                    |                        |

### C.23:8 - Consequences

* **Explainable admission.** Every *Admit/Degrade/Abstain* is backed by **anchored** evidence and explicit unknown handling (selector reports are SCR‑linked).
* **Run‑safe pluralism.** Multiple families can co‑exist with **policy‑governed** exploration (E/E‑LOG) and maturity‑aware gating.
* **Portable governance.** Bridge hygiene and CL routing make cross‑Tradition reuse **deliberate and costed** (penalties to **R** only).

### C.23:9 - Rationale

The ladder and LOG shells align with FPF’s **Assurance calculus**: **F** (form) is governed by artefact kind, **G** (scope) by USM slices, and **R** (reliability) accumulates via WLNK then **Φ(CL)** penalties. Treating maturity as **evidence‑typed rungs**—rather than a “score”—avoids illegal arithmetic and lets **design/run** remain separate via `DesignRunTag` discipline (A.4) and explicit GateCrossings. This mirrors contemporary **science‑of‑science** insights: replication, benchmarking, and field health indicators are the **currency** of maturity, not anecdote.  ([Science][19])

### C.23:10 - Relations

**Builds on:** **G.5** (selector consumes these rules), **G.4** (Acceptance & EvidenceProfiles), **C.22** (S2 typing), **C.18 NQD‑CAL**, **C.19 E/E‑LOG**, **B.3** (Assurance tuple & WLNK).   
**Publishes to:** **UTS** (MaturityCards, rule ids), **SCR/RSCR** (branch coverage; parity hooks).
**Constrains:** **G.8** (LOG Bundling must cite MaturityCards), **G.9** (parity harness draws baselines per rung), **G.11** (refresh windows per rung & decay), **G.5** (Open‑Ended Family mode for GeneratorFamily).
**Outcome.** The pattern introduces **new content** (LOG shells + maturity poset + degrade modes + publication Standard) and **does not duplicate** CG‑Spec legality rules, CHR guard‑macros, or CAL acceptance mechanics; it *integrates* them into **admissibility logic** for MethodFamilies.

### C.23:End

## C.24 - Agentic Tool‑Use & Call‑Planning (C.Agent‑Tools‑CAL)

**Status.** Calculus specification (**CAL**). Defines the conceptual calculus for **agentic selection and sequencing of tool calls** under budgets, trust gates, and policy. **ΔKernel = 0** (no kernel primitives added). *Minting note:* this CAL **does not mint** new U‑types; it **aliases** canonical U‑types where appropriate via **E.10/UTS**.

**Instantiates / Refines Pillars.** E.2 P‑3 Scalable Formality, P‑7 Pragmatic Utility, P‑10 Open‑Ended Evolution, P‑11 SoTA Alignment, and the **Bitter‑Lesson Preference** (prefer scalable, general methods that benefit from more data/compute over fragile hand‑tuned heuristics when assurance/cost are comparable).

**Depends on.** A‑kernel (A.1–A.15) for holonic basics and **Role–Method–Work** separation; **B.3** Trust & Assurance (F–G–R with CL penalties); **E.3/E.5** (precedence & Guard‑Rails); **C.5** Resrc‑CAL; **C.18** NQD‑CAL (candidate generation/portfolio); **C.19** E/E‑LOG (explore–exploit policies); **optional** Compose‑CAL and KD‑CAL (knowledge dynamics) where available.

**Coordinates with.**
U.WorkPlan and U.PromiseContent bindings (acceptance gates), Working‑Model publication discipline (**per B.3**), Evidence/Provenance (G.6).

### C.24:1 - Problem frame

Modern systems increasingly rely on **agents** that can **choose tools** (services/methods) and **plan sequences** of calls to achieve objectives in uncertain contexts. Without a calculus:

* calls are scheduled by **ad‑hoc heuristics**,
* **budgets** (compute, cost, wall‑time) are implicit,
* **assurance** and **policy provenance** are lost, and
* agents either over‑constrain themselves with brittle scripts or wander without guard‑rails.

This CAL provides the **conceptual API for thought** that lets any implementation (LLM‑based, search‑based, code‑based, robotic) plan calls **lawfully**, **audibly**, and **scalably**. (Role–Method–Work alignment; didactic primacy.)  

### C.24:2 - Problem
We need a **tool‑agnostic** way to (i) identify **admissible tools**, (ii) **score** candidate call sequences, (iii) allocate an **explore/exploit** share, (iv) enforce **budget & harm** gates, and (v) **replan** on signals—**without** baking domain‑specific heuristics into the core and **without** violating B.3 assurance discipline. 

### C.24:3 - Forces

| Force                              | Tension                                                                                                        |
| ---------------------------------- | -------------------------------------------------------------------------------------------------------------- |
| **General methods vs. hand‑craft** | Scalable, model‑centric search ↔ short‑term wins of bespoke scripts (guarded by **Bitter‑Lesson Preference**). |
| **Assurance vs. Autonomy**         | F‑G‑R gates & CL penalties ↔ agent freedom to sequence calls and learn online.                                 |
| **Exploration vs. Delivery**       | Exploration share for illumination ↔ delivery SLAs and cost ceilings (E/E‑LOG policy).                         |
| **Separation of concerns**         | Planning (MethodDescription) ↔ execution (Work) ↔ service promises (U.PromiseContent).                                |

### C.24:4 - Solution — Signature & Realization

**Types (aliases).**
*`ATC.CallSpec`* ≡ `U.MethodDescription` with `accessSpec` for a tool service;
*`ATC.CallPlan`* ≡ `U.WorkPlan` specialised for tool invocations;
*`ATC.CallGraph`* ≡ Evidence/Provenance graph over a `U.Work` ledger;
*`ATC.Policy`* references `U.EmitterPolicyRef` (E/E‑LOG) and local call gates **including BLP tolerances (α, δ)**.

**Roles.**
A **System in AgentialRole** composes a **Plan** (MethodDescription); upon enactment, a **Performer** executes **Work** (calls), and **Observers** record **Observations** with acceptance checks. (A.15 strict distinction.) 

**Operators (Γ_agent; CAL, conceptual):**

1. `Γ_agent.eligible(tool, TaskSignature, K_ctx) → {true|false, notes}`
   *Eligibility gate* based on capability fit, policy allow‑list/deny‑list, and context K (incl. safety constraints).

2. `Γ_agent.enumerate(TaskSignature, K_ctx) → CandidateSet<ATC.CallSpec>`
   Returns admissible calls. **MAY** delegate to **NQD‑CAL** for portfolio enumeration when families are heterogeneous and **MUST** apply the current **E/E‑LOG lens** (objectives & telemetry) to tag candidates.

3. `Γ_agent.plan(Objective, CandidateSet, Budget, ATC.Policy) → ATC.CallPlan`
   Produces a **call plan** with steps `{pre, call, post}`, *explicit budgets* (compute, cost, time, risk), and **E/E policy** (explore_share, tie‑breakers, stop‑conditions). The plan is a MethodDescription, not Work.  

4. `Γ_agent.execute(ATC.CallPlan) → {ATC.CallGraph, Observations}`
   Executes with **hard gates** (budget, risk, constraint‑fit) and logs provenance suitable for B.3 assurance reporting (design/run separated). 

5. `Γ_agent.replan(Signals, ATC.CallPlan, Budget′) → ATC.CallPlan′`
   Triggered by sentinel breaches, assurance drops, or policy events; preserves **editioned** policy and context. (Design/run separation; Working‑Model handshake.) 

6. `Γ_agent.score(Plan or Step) → ⟨ValueProxies, Cost, Risk, FGR_floor⟩`
   Computes selection signals **without** illegal scalarisation across mixed scales; **uses Pareto comparison under the C.19 E/E‑LOG lens** and defers final dominance to declared policies. 

**Normative Laws (ATC‑Laws).**

* **ATC‑1 (Model‑the‑Call, not the App).** A tool call is a **Work** instance that enacts a referenced **MethodDescription** promised by a **Service**; plans schedule calls but are **not the calls**. (A.15.)
* **ATC‑2 (Bitter‑Lesson Preference).** When two admissible choices are within **δ (assurance)** and **α (budget)**, **prefer the more general, scale‑benefiting method** whose **slope vector Pareto‑dominates** under the declared E/E‑LOG objectives; any override **MUST** record a **BLP‑waiver** with expiry. (E.2; precedence governed by E.3.)
* **ATC‑3 (Budget & Harm Gates).** Plans **SHALL** declare ceilings on compute, cost, wall‑time, and risk; execution **MUST** abort or replan on breach. (Assurance ties to B.3; design/run kept separate.)
* **ATC‑4 (Explore‑Share Discipline).** Plans **MUST** declare `explore_share`; defaults **inherit from E/E‑LOG profiles**. **Informative defaults**: `0` for safety‑critical or deterministic tasks; `≈0.2–0.4` for ambiguous tasks with heterogeneous tool families. Promotion of illumination telemetry into dominance **requires explicit policy**.
* **ATC‑5 (Provenance & Replay).** Every call **MUST** emit a **CallGraph** with: Service id, MethodDescription edition, inputs/outputs (redacted per privacy), **EmitterPolicyRef**, and budget deltas. (NQD/E/E provenance fields apply when used.)
* **ATC‑6 (Assurance‑First Decisions).** Selection **MUST** respect B.3: WLNK minima on F/R (weakest‑link floors), CL penalties on integration, and **no** chimera scores across design/run. Publish **⟨F,G,R⟩** for the *typed claim* “this plan is admissible under K,S”.
* **ATC‑7 (Notation/Vendor Independence).** Core pattern text **MUST NOT** encode vendor‑specific tokens; bindings occur in Context via Bridges/Profiles. (Lexical guard‑rails.)


### C.24:5 - Policy Block (normative, profile‑able)

**ATC‑Policy fields (conceptual):**
`{ backstop_confidence, explore_share, risk_bound, cost_ceiling, time_ceiling, tie_breakers, novelty_quota?, wild_bet_quota?, stop_conditions, BLP_delta_α, BLP_delta_δ }` — realized by referencing an **E/E‑LOG EmitterPolicy** and adding **BLP** clauses. Defaults inherit from E/E‑LOG; any deviation is editioned.

**BLP Precedence.** In conflicts with tactics that hard‑code narrow scripts, **BLP** applies **subject to E.3/E.5 precedence**. Where scripts encode **safety‑critical gating or regulatory compliance**, scripts **prevail** unless a DRR records: (i) **override rationale**, (ii) **expiry**, (iii) **measured hazard** avoided, and (iv) planned **re‑evaluation** window (P‑10 evolution duty).

### C.24:6 - Archetypal Grounding (informative; non‑binding)

1. **LLM Research Agent (knowledge work).**
   Task: answer a novel technical question. Candidate tools: retrieval, structured web search, code runner, table/plot generator.
   **Plan:** `enumerate → plan(explore_share≈0.4) → call(search→retrieve→synthesise→code‑check) → replan on sentinel (low R)`; **BLP** favours **general retrieval + prompting policies** over hand‑coded, per‑site scrapers unless assurance demands otherwise. (Echoes SoTA: *ReAct* (2022), *Self‑Ask* (2022), *Reflexion* (2023), *Tree‑of‑Thoughts* (2023), *Toolformer* (2023).)

2. **Program Repair Agent (systems/software).**
   Task: propose a patch against a failing test suite. Candidate tools: repo introspection, static analyzer, unit runner.
   **Plan:** prefer **search‑and‑learn loops** with test‑guided feedback over fixed “if error X then patch Y” tables; exploration quota enforces trials across patch families before exploitation. (Aligns with post‑2019 automated program repair lines and *SWE‑bench*‑style agent loops.)

3. **Lab Automation Agent (physical).**
   Task: adjust a wet‑lab protocol under drift. Candidate tools: planner, pipetting controller, spectrometer, Bayesian optimizer.
   **Plan:** **BLP** drives toward **model‑based optimization** under budgeted sample counts; heuristics remain as **policy‑documented** fallbacks with expiry. (Resonates with quality‑diversity and BO practice since 2015, mirrored by NQD/E/E policies.) 

### C.24:7 - Conformance Checklist (CC‑AT)

1. **CC‑ATC‑1 — Declared separation.** Plan is a `MethodDescription`; execution is `Work`; acceptance is via `U.PromiseContent`. No schedule inside specs; schedules live in `U.WorkPlan`.
2. **CC‑ATC‑2 — Budgets on record.** `time/compute/cost/risk` ceilings exist **ex ante**; stop conditions listed.
3. **CC‑ATC‑3 — E/E policy.** `EmitterPolicyRef` (or equivalent) and `explore_share` are editioned and logged.
4. **CC‑ATC‑4 — Assurance tuple.** Publish the **typed claim** “Plan admissible under K,S” with **⟨F,G,R⟩** and CL penalties traceable in the **CallGraph** SCR. Design/run never merged.
5. **CC‑ATC‑5 — BLP waiver discipline.** Any heuristic override against a general method includes **expiry** and **re‑evaluation** date.
6. **CC‑ATC‑6 — Provenance minimum.** Record `{PromiseContentRef, MethodDesc.edition, EmitterPolicyRef, DescriptorMapRef? (if NQD), DistanceDefRef? (if NQD), TimeWindow, Seeds?, Dedup?}`.
7. **CC‑ATC‑7 — Notation independence.** No vendor tokens in conceptual text; bindings via Bridges/Profiles only.
8. **CC‑ATC‑8 — BLP tolerances declared.** **α/δ** tolerances are present in `ATC.Policy` or referenced via the active E/E‑LOG profile.

### C.24:8 - Consequences

*Positive.* Portable agent patterns; **auditable autonomy**; lawful exploration; faster hypothesis cycles via BLP; replayable call graphs; decision‑grade Working‑Model surfaces.
*Trade‑offs.* Requires explicit budgets/policies; BLP may defer quick wins from bespoke scripts; stronger logging discipline.

### C.24:9 - Rationale (post‑2015 SoTA alignment, informative)

* **Scaling‑first methods** (language‑model and representation‑learning scaling laws; subsequent data/compute‑balanced scaling) empirically support **BLP**: general, learnable mechanisms tend to dominate as budgets rise—hence **ATC‑2**.
* **Tool‑use agents** in the literature (*ReAct*, *Self‑Ask*, *Reflexion*, *Toolformer*, *Tree‑of‑Thoughts*, open‑ended *Voyager*‑style skill acquisition) all benefit from **explicit planning + feedback**, exactly what CC‑AT‑2/3/6 encode.
* **Quality‑Diversity & BO** practice motivates the **explore_share** default and the distinction between **dominance vs. illumination telemetry** (kept separate unless policy promotes).  

### C.24:10 - Relations

* **Builds on:** A.15 Role–Method–Work alignment (planning vs execution vs service), B.3 Trust & Assurance (F–G–R/CL), C.5 Resrc‑CAL, C.18 NQD‑CAL (candidate/portfolio), C.19 E/E‑LOG (policies).    
* **Constrains:** Any `U.PromiseContent` used as a “tool” MUST expose acceptance conditions and observation hooks sufficient for B.3 reporting. 
* **Enables:** Human‑centric Working‑Model surfaces with policy/assurance disclosures (design/run separated). 

### C.24:11 - Bias‑Annotation

*Lexical firewall* and *notation independence* apply; no vendor tokens; mixed‑scale characteristics are never averaged; illumination remains a **report only telemetry** unless a policy promotes it into dominance.  

#### C.24:12 - Didactic Quick Card (1‑screen crib)

**Agentic Call Plan (public):**
*Objective - Context(K) - Budget{time/compute/cost/risk} - PolicyRef (E/E‑LOG) - Explore‑share - Steps[ pre/ call /post ] - Stop‑conditions - **BLP tolerances (α,δ)** - BLP‑note (if any) - Assurance⟨F,G,R|K,S⟩ - Provenance ids.*

### C.24:End

## C.25 - Q‑Bundle: Authoring “‑ilities” as Structured Quality Bundles

**Status & placement.** Part C (measurement/comparability); **Definitional pattern reusing Core patterns (**A.2.6 USM**; **A.6.1 Mechanism**; **C.16 MM‑CHR / A.18 CSLC**). Intended as a **lightweight authoring aid** for Contexts; it adds no new kernel types.  (A.6.1; A.2.6 § 6.2; C.16/A.18). 

### C.25:1 - Problem frame
Provide a **minimal, uniform shape** for engineering “‑ilities” so authors either (a) declare a **single CHR characteristic** (when truly measurable on one scale), or (b) publish a **structured bundle** that keeps **measures** (CHR) distinct from **scope** (USM set) and **mechanism/status** slots. This prevents conflation of **set‑algebra** (scope) with **numeric measurement** (CHR) and keeps assurance math stable.  (A.2.6 § 6.2; C.16).

### C.25:2 - Problem (recurring)
*‑ilities* are often treated as if they were **single metrics**, while in practice many are **composites** whose evaluation depends on (i) **declared context‑of‑use** (Scope), (ii) **one or more CHR measures** (SLIs/SLOs), and (iii) **supporting mechanisms/statuses**. Collapsing these into “one number” invites illegal arithmetic and breaks USM locality.  (A.2.6; C.16).

### C.25:3 - Forces
**Locality vs comparability.** Scope must remain **context‑local** (USM) while measures remain **legally comparable** (CSLC). 
**Mechanism vs measure.** Presence of a mechanism (A.6.1) is not itself a measurement, yet may gate admissibility and influence **R**.  (A.6.1; C.16/A.18).

### C.25:4 - Solution — Q‑Bundle normal form (Tell → Show → Show; E.8 order)
**Definition.**  
`Q‑Bundle := ⟨ Name, Carrier, ClaimScope?, WorkScope?, Measures[CHR], QualificationWindow?, Mechanisms?, Status?, Evidence? ⟩`

**Fields (conceptual; reuse existing types).**
* **Name.** The quality family label (e.g., *Availability*, *Resilience*).  
* **Carrier.** `U.System | U.PromiseContent | U.Episteme` (what bears the quality).  
* **ClaimScope / WorkScope.** **USM** set(s) over `U.ContextSlice` (where the claim holds / where the capability can deliver). **Set‑valued; not CHR.**  (A.2.6 § 6.2).  
* **Measures[CHR].** One or more **CHR Characteristics bound to one Scale each** (e.g., `AvailabilityRatio[%]`, `RTO[min]`). **These are the measurable slots.** (C.16/A.18).  
* **QualificationWindow.** Time policy used by guards (point/window/rolling).  
* **Mechanisms / Status.** References to **A.6.1 U.Mechanism** realizations (e.g., redundancy policy, audit/trace) or certification/status flags. **Not measurements.** (A.6.1).  
* **Evidence (optional).** Anchors/stubs per A.10 or C.16 to justify measures/mechanisms.

**Conformance (minimal).**
1) If a publisher intends to use an “‑ility” as a **single measurement axis**, they **MUST** bind it to a **named `U.Characteristic` + CSLC Scale** and cite that axis in guards/UTS; otherwise publish a **Q‑Bundle**. (C.16/A.18).  
2) **Scope** remains **USM set‑valued**; guards use **membership/coverage** (“Scope covers TargetSlice”), never ordinal/averaging on G. (A.2.6 § 6.2).  
3) **Mechanisms/Status** MAY gate admissibility but **MUST NOT** be conflated with **Measures**; penalties from Bridges/planes route to **R** only. (A.6.1; Part B).

### C.25:5 - Micro‑catalogue (worked mini‑sketches)
**Availability (often Q‑CHR).**  
*Scope:* observation window + region/tier (USM). *Measure:* `AvailabilityRatio[%]` (CHR). *Mechanisms:* redundancy/failover (A.6.1). **Guard:** Scope covers TargetSlice ∧ SLI/SLO satisfied.  

**Resilience (Q‑CMP).**  
*Scope:* disruption scenarios (USM). *Measures:* `MTTR`, `RTO`, `RPO` (CHR set). *Mechanisms:* drills/restore runbooks. **Guard:** scenario‑specific gates; **R** absorbs penalties from crossings.  

**Security (Q‑MECH/Q‑CMP).**  
*Scope:* trust zones/attack classes (USM). *Measures:* time‑to‑patch, coverage proportions (CHR). *Mechanisms/Status:* control sets, certs. **Guard:** policy/mechanism present ∧ measures thresholds ∧ Scope match.

### C.25:6 - Relations
**Builds on.** **A.2.6** (USM scope algebra, set‑valued; no CSLC), **A.6.1** (mechanism intensions and guards), **C.16/A.18** (measurement legality: one Characteristic ↔ one Scale).  
**Coordinates with.** **B.3** (R/CL penalties only), **A.15** (Method–Work gates use Scope + Measures + Windows).

### C.25:7 - Consequences (brief)
* **No category errors.** Authors cannot “average scope” or treat mechanisms as measurements.  
* **Portable comparisons.** Numbers compare on CHR Scales; scope composes by set algebra.  
* **Cleaner gates.** Admission checks become `Scope covers TargetSlice ∧ Measures met ∧ Window valid`.

### C.25:8 - Quick authoring checklist (lintable)
* If the term is an **‑ility**, choose: **CHR axis** (bind to Characteristic+Scale) **or** **Q‑Bundle**.  
* Ensure any scope is **USM** (set over `U.ContextSlice`); no “G‑levels.”  
* Cite mechanisms/status separately; route crossings’ penalties to **R** only.

### C.23:End


# **Part D – Multi-scale Ethics & Conflict‑Optimisation**

| §       | ID & Title                           |  Concise reminder — “what belongs here”                                         |
| ------- | ------------------------------------ |  ------------------------------------------------------------------------------ |
| **D.1** | **Axiological Neutrality Principle** |  No built‑in value hierarchy; ethics expressed as explicit preference lattices. |
| **D.2** | **Multi‑Scale Ethics Framework**     |  Four nested arenas: *Self → Team → Ecosystem → Planet*; scoping rules.         |
| D.2.1   | Local‑Agent Ethics                   |  Duties & permissions for a single `U.System` or `U.Agent`.                     |
| D.2.2   | Group‑Ethics Standards               |  Collective norms, veto mechanisms, subsidiarity rule.                          |
| D.2.3   | Ecosystem Stewardship                |  Inter‑FPF externalities; tragedy‑of‑commons mitigations.               |
| D.2.4   | Planetary‑Scale Precaution           |  Catastrophic‑risk anchors; long‑termism discount curves.                       |
| **D.3** | **Holonic Conflict Topology**        |  Typology of clashes: resource, goal, epistemic, temporal.                      |
| D.3.1   | Conflict Detection Logic (LOG‑use)   |  Formal predicates (`conflictsWith`, `mitigatedBy`) and satisfiability checks.  |
| D.3.2   | Conflict Routing Protocol            |  From local negotiation → external mediation → DRR appeal.                      |
| **D.4** | **Trust‑Aware Mediation Calculus**   |  Resolution algorithm blends value‑weights with B.3 trust scores.               |
| D.4.1   | Fair‑Share Negotiation Operator      |  Nash‑like but bias‑corrected; imports `Resrc‑CAL` cost functions.              |
| D.4.2   | Assurance‑Driven Override            |  When safety evidence overrides utility maximisation.                           |

## D.5 - Bias-Audit & Ethical Assurance

### D.5:1 - **Problem Frame**

FPF is designed to produce reliable, objective, and trustworthy holons. However, formal correctness (`FV` score) and empirical validation (`EV` score) are not sufficient on their own. Any artifact created by humans or trained on human-generated data is susceptible to hidden cognitive, cultural, and algorithmic biases. A perfectly verified control system can still be unsafe if its requirements were based on a biased assumption about operator behavior. A highly accurate machine learning model can be deeply unfair if its training data was not representative.

### D.5:2 - **Problem**

Without a formal, repeatable method for surfacing and mitigating these biases, FPF models risk becoming "flawed by design." This leads to three critical failure modes:

1.  **Systemic Harm:** The deployed holon, despite meeting all its technical specifications, causes unintended negative consequences for certain groups or in certain contexts.
2.  **Eroded Trust:** Stakeholders or the public lose trust in the system (and its creators) when its inherent biases are exposed after deployment.
3.  **Hidden Risk:** The assurance case appears strong on paper, but it is built on a foundation of unexamined and potentially dangerous assumptions, creating a significant hidden risk.

### D.5:3 - **Forces**

| Force | Tension |
| :--- | :--- |
| **Objectivity vs. Inevitable Subjectivity** | How to strive for objective, neutral models while acknowledging that all creation is influenced by the subjective perspectives of the creators. |
| **Speed of Delivery vs. Depth of Reflection** | How to integrate a thoughtful ethical review process without paralyzing the agile, iterative cycles of development. |
| **Expertise vs. Inclusivity** | How to leverage specialized ethical expertise without disenfranchising the core engineering team from moral responsibility. |
| **Process vs. Culture** | Is ethical assurance a bureaucratic checklist to be completed, or a cultural practice of continuous self-critique? |

### D.5:4 - **Solution**

FPF introduces the **Bias-Audit Cycle (BA-Cycle)**, a lightweight, iterative ceremony designed to integrate ethical reflection directly into the engineering development cycle. It is not a one-time gate but a continuous loop of inquiry.

#### D.5:4.1 - The Bias-Audit Cycle: Four Phases

The cycle consists of four distinct phases, aligned with the project's natural rhythm.

| Phase | Trigger | Core Activity | Output |
| :--- | :--- | :--- | :--- |
| **BA-0: Kick-off** | Project start or major new feature. | **Framing the ethical scope.** The team identifies potential areas of bias and creates an initial, living document called the **Bias Register**. | A skeleton Bias Register with initial questions. |
| **BA-1: Rapid Scan**| End of each sprint or design session. | **Continuous lightweight check.** A rotating member of the core team (the *Engineer-Scrutineer*) quickly scans recent changes against a checklist, flagging potential issues in the Bias Register. | Updated Bias Register with new items flagged for discussion. |
| **BA-2: Panel Review**| Before a major integration or release decision (e.g., before moving to the `Evidence` state). | **Deep, multi-perspective critique.** A small panel, including individuals in roles like **Ethicist**, **Domain Sociologist**, and **UX Design Critic**, reviews the flagged items and proposes concrete mitigations. | A structured, auditable artifact called the **Bias-Audit Report**, documenting findings and required actions. |
| **BA-3: Closure** | At the release freeze. | **Ensuring accountability.** The facilitator confirms that all "blocking" issues from the Bias-Audit Report have either been resolved or have a documented, accepted risk. | The final Bias-Audit Report is marked as *resolved* or *risk-accepted* for that release. |

#### D.5:4.2 - The Bias Taxonomy: A Shared Language for Critique

To structure the audit, FPF provides a minimal, extensible taxonomy of common bias categories.

| Code | Bias Category | Manager's View: The Simple Question to Ask |
| :--- | :--- | :--- |
| **REP** | **Representation Bias** | "Whose voice, data, or perspective is missing from this model?" |
| **ALG** | **Algorithmic Bias** | "Could our automated rule or formula unintentionally amplify unfairness for minority or edge cases?" |
| **VIS** | **Visual Framing Bias** | "Does this diagram, color choice, or dashboard visualization steer the user towards a preferred conclusion?" |
| **MET** | **Metric Proxy Bias** | "Are we chasing a metric that is easy to measure, at the expense of the real, harder-to-measure objective?" (Connects to ADR-015) |
| **LNG** | **Lexical Bias** | "Do our naming choices (e.g., 'master/slave', 'blacklist/whitelist') encode unintended value judgments or historical baggage?" |

> **Didactic Note for Managers: This is Risk Management, Not a Philosophy Seminar**
>
> The Bias-Audit Cycle is FPF's "immune system." It's designed to find and neutralize hidden assumptions before they become costly product failures or public relations disasters. Think of it like a security audit, but for the ethical and social integrity of your system.
>
> *   **It's not about being "perfect"; it's about being "aware."** The goal is not to eliminate all bias (an impossible task) but to make your team's biases explicit, documented, and consciously managed.
> *   **It's cost-effective.** The lightweight "Rapid Scan" catches most issues early, during a sprint. The more intensive "Panel Review" is reserved for key moments, ensuring that expert time is used efficiently.
> *   **It creates a defensible record.** The Bias-Audit Reports provide a clear, auditable trail showing that your team has taken a systematic and responsible approach to identifying and mitigating potential harms. In an era of increasing scrutiny on AI and autonomous systems, this record is not just good practice—it's a critical business asset.

#### D.5:4.3 - Normative Artifacts

The Bias-Audit Cycle produces two key conceptual artifacts that serve as the auditable record of ethical deliberation.

*   **The Bias Register:**
    *   **Nature:** A living, evolving **episteme** that serves as a repository of questions, concerns, and potential biases identified throughout a holon's evolution.
    *   **Content:** It is a structured collection of inquiries, organized by the Bias Taxonomy (REP, ALG, etc.). It is continuously updated during the Rapid Scans (BA-1) and represents the "running log" of ethical and bias-related considerations for the project.

*   **The Bias-Audit Report:**
    *   **Nature:** A formal, versioned **episteme** that documents the findings of the Panel Review (BA-2).
    *   **Content:** It contains a structured record of findings. Each finding is a `U.Episteme` with attributes for:
        *   `biasCode`: The category from the Bias Taxonomy.
        *   `severity`: An ordinal level (`high`, `medium`, `low`).
        *   `description`: A narrative explaining the issue.
        *   `mitigation`: A proposed `U.Method` or `U.ConstraintRule` to address the issue.
        *   `status`: A state (`blocking`, `resolved`, `risk-accepted`).
    *   **Conceptual Example:**
        *   `finding-01`: An episteme with `biasCode: REP`, `severity: high`, and a `description` stating that the training data for a recognition holon lacks representation from certain demographics. The `mitigation` would be a `U.Method` for acquiring a balanced dataset, and the `status` would be `blocking` until this method is executed and its outcome validated.

### D.5:5 - **Conformance Checklist**

*   **CC-D5.1 (Cycle Mandate):** Any project developing a holon that interacts with or makes decisions about humans **MUST** conduct the Bias-Audit Cycle.
*   **CC-D5.2 (Artifact Mandate):** The project **MUST** maintain a **Bias Register** and produce a **Bias-Audit Report** before any major release.
*   **CC-D5.3 (Blocking Issue Mandate):** A release **SHALL NOT** be considered conformant if its latest Bias-Audit Report contains any unresolved findings with `status: blocking`. The issue must either be moved to `resolved` (mitigated) or `risk-accepted` (formally signed off by a designated authority).
*   **CC-D5.4 (Role Mandate):** The Panel Review (BA-2) **MUST** involve at least three individuals representing distinct perspectives, ideally aligning with the roles of *Ethicist*, *Domain Sociologist*, and *UX Design Critic* from the Intellect Stack.

### D.5:6 - **Common Anti-Patterns and How to Avoid Them**

| Anti-Pattern | Manager's View: What It Looks Like | How FPF Prevents It (Conceptually) |
| :--- | :--- | :--- |
| **The "Ethics Ghetto"** | One person is the "ethics officer," and the rest of the engineering team sees bias as "not my job." | The **Rapid Scan (BA-1)** is a conceptual activity performed by a rotating member of the core team. This distributes the responsibility for ethical reflection across all roles. |
| **The "Checklist Charade"** | The team mechanically answers "yes/no" to bias questions just before a release, without any real reflection, simply to satisfy a process requirement. | The **Panel Review (BA-2)** is a moment of deep, multi-perspective critique that a perfunctory checklist cannot survive. The requirement for a structured **Bias-Audit Report** also forces concrete findings and mitigation methods, not just checkmarks. |
| **The "Bias Whack-a-Mole"** | The team fixes one bias issue, only for another to pop up, because they are only addressing symptoms. | The **Bias Taxonomy** encourages a more systematic approach. By considering categories like Representation (REP) and Metric Proxy (MET), the team is prompted to look for root causes (e.g., flawed data collection methods or poorly chosen objectives) rather than just patching individual algorithmic flaws. |

### D.5:7 - **Consequences**

| Benefits | Trade-offs / Mitigations |
| :--- | :--- |
| **Proactive Risk Mitigation:** The cycle surfaces and addresses potential ethical and social harms *before* they are deployed, preventing costly failures and reputational damage. | **Additional Ceremony:** The cycle introduces new conceptual steps and artifacts into the workflow. *Mitigation:* The process is designed to be lightweight and to align with existing agile cadences (e.g., the Rapid Scan is a brief conceptual check at the end of a sprint). |
| **Creates an Auditable Ethical Record:** The Bias-Audit Reports provide a transparent, defensible trail demonstrating that the organization has a systematic process for managing ethical risks. | **Finding the Right Expertise:** It may be challenging to find individuals to fill the required roles. *Mitigation:* These roles represent perspectives, not necessarily formal job titles. The key is the diversity of viewpoints. |
| **Builds a Culture of Responsibility:** By making ethical reflection a routine part of the engineering process, the cycle fosters a culture where every team member is empowered and expected to think critically about the broader impact of their work. | - |
| **Improves Holon Quality:** Designing for a wider range of users and edge cases, as prompted by the audit, often leads to more robust, user-friendly, and innovative holons. | - |

### D.5:8 - **Rationale**

Formal correctness is not a substitute for moral responsibility. This pattern recognizes that bias is not an occasional flaw but a systemic feature of any human-led design process. The Bias-Audit Cycle is FPF's formal mechanism for managing this reality. It is a direct implementation of the **Cross-Disciplinary Bias Audit Guard-Rail (E.5.4)**.

By integrating this cycle into the core reasoning workflow, FPF moves ethical assurance from a peripheral, often-ignored "nice-to-have" into a central, non-negotiable component of engineering excellence. It ensures that the powerful tools of formal reasoning and validation provided by FPF are always directed towards creating holons that are not only correct, but also conscionable.

### D.5:9 - **Relations**

*   **Implements:** The `Cross-Disciplinary Bias Audit` Guard-Rail (E.5.4).
*   **Complements:** `D.4 Trust-Aware Mediation Calculus` by providing inputs on fairness and value alignment; `B.3.4 Evidence Decay & Epistemic Debt` by questioning the longevity of assumptions about social context.
*   **Operationalizes:** The conceptual roles of `Ethicist`, `Domain Sociologist`, and `UX Design Critic` from the Intellect Stack.

### D.5:End


| D.5.1   | Taxonomy‑Guided Audit Templates      |  Onto / Arch / Prag / Did dimensions; sampling guidance.                        |
| D.5.2   | Assurance Metrics Roll‑up            | Composite “Ethical Risk Index”, traceable to Evidence Graph Ref.                 |


# **Part E - FPF Constitution and Authoring Cluster**

# Section E‑I - The FPF Constitution

## E.1 - Vision & Mission: “Operating System for Thought”

### E.1:1 - Problem frame
Modern engineering, science, and strategy all suffer from **conceptual overload**: dozens of domain tools, drifting vocabularies, and disconnected “best practices” splinter ideas as they travel from napkin sketch to certified deliverable. Stakeholders—*Engineers, Researchers, Learners*—lack a single, evolvable scaffold that can carry an insight across that span.

### E.1:2 - Problem
Absent such a scaffold, every discipline re‑invents epistemology and systems thinking, spawning silos, steep learning curves, and brittle life‑cycle models. Previous attempts either froze agility in rigid hierarchies or dissolved rigour in tool‑centric jargon.

### E.1:3 - Forces

| Force                           | Tension                                                                 |
| ------------------------------- | ----------------------------------------------------------------------- |
| **Conceptual Unity**            | Freedom to evolve ↔ invariant principles that prevent vocabulary drift. |
| **Rigor vs Agility**            | Formal verifiability ↔ rapid, iterative exploration.                    |
| **Universality vs Specificity** | Domain‑agnostic kernel ↔ problem‑specific leverage.                     |
| **Didactic Clarity**            | Human comprehension ↔ abstract purity and density.                      |
| **Physical Grounding**          | Abstract constructs ↔ a *material Transformer* that proves feasibility.     |

**Mission Statement**

> *Enable any motivated system/actor/agent/transformer — human or AI — to transform a raw idea into a reproducible, auditable change in the physical world through incremental, falsifiable cycles.*

**Vision Statement**

> *Reliable reasoning should be as accessible as version control: clone the conceptual kernel, extend it with domain patterns, and commit decisions that remain traceable across time, scale, and discipline.*

### E.1:4 - Solution — *FPF as an Operating System for Thought*
FPF delivers a **generative scaffold** realised as:

1. a **Kernel** of non‑derivable, cross‑domain **first principles**;
2. pluggable **patterns**—Systemic Calculus, Knowledge Dynamics, etc.—that instantiate those principles;
3. a **pattern language** (*Architectural* ► why/ how; *Definitional* ► what) with embedded **Conformance Checklist (CC)**;
4. **Design Rationale Records (DRRs)** that govern safe, auditable evolution;
5. three **core invariants** that every artefact must honour

   * **Evolvability** — change is expected and governed;
   * **Cross‑Scale Coherence** — the same algebra binds parts to wholes at any level;
   * **Didactic Transparency** — each element exposes its own reasoning path.

### E.1:5 - ** Conformance Checklist**

| ID              | Requirement                                                                                                                                          | Rationale                                       |
| --------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------- |
| **CC‑Vision.1** | Every composite artefact **MUST** cite a *material Transformer* that can, in principle, perform the aggregation (`Γ(D,C)`) that produced it.             | Ensures physical feasibility and auditability.  |
| **CC‑Vision.2** | Every normative rule **MUST** demonstrably support at least one core invariant (*Evolvability, Cross‑Scale Coherence, Didactic Transparency*).       | Keeps the Canon lean and purpose‑driven.        |
| **CC‑Vision.3** | Conceptual text **MUST NOT** contain tokens black‑listed by the **DevOps Lexical Firewall** (`yaml`, `docker`, …).                                   | Preserves layer purity and tool‑agnostic core.  |
| **CC‑Vision.4** | A conformant artefact **MUST** state a measurable benefit for at least one of the three roles (*Engineer, Researcher, Learner*) or justify omission. | Aligns success with stakeholder trajectories.   |

### E.1:6 - Consequences

*Positive* — Unified language accelerates cross‑disciplinary discovery; regulators can audit claim lineages; learners acquire concepts through the spec itself.
*Trade‑offs* — Authors face an initial learning curve and must trace every rule to an invariant; disciplined traceability is required to prevent variant sprawl.

### E.1:7 - Relations & Precedence
Pattern E.1 governs **E.2 Eleven Pillars** and the Guard‑Rail set **A.5–A.8**; any later pattern that conflicts with E.1 **MUST** be revised via a DRR before entering the Canon.

*“Purpose without a scaffold is wishful thinking; a scaffold without purpose is cargo‑cult—FPF welds the two into disciplined imagination.”*

### E.1:End

## E.2 - The Eleven Pillars

### E.2:1 - Problem frame
Pattern E.1 set the FPF mission as an **operating system for thought**. To turn that mission into a durable architecture, FPF needs a small, explicit constitution—principles that remain stable while everything built on top of them can evolve. Without such invariants, domain silos, vocabulary drift, and tool‑centric shortcuts quickly erode coherence and reproducibility across disciplines.

### E.2:2 - Problem
Frameworks without binding first principles wobble between two extremes: rigid dogmas that kill adaptation and amorphous guidelines that invite cognitive chaos. In either case, reasoning fragments, auditability collapses, and physical impact suffers.

### E.2:3 - Forces
| Force                          | Tension                                                |
| ------------------------------ | ------------------------------------------------------ |
| **Foundational Stability**     | Immutable core ↔ perpetual adaptation to new knowledge |
| **Cognitive Load**             | Minimal elegance ↔ comprehensive coverage              |
| **Rigor vs Accessibility**     | Formal soundness ↔ intuitive entry for non‑specialists |
| **Universality vs Modularity** | Domain‑agnostic scope ↔ plug‑in extensibility          |
| **Pragmatic Grounding**        | Abstract invariants ↔ measurable, falsifiable outcomes |

### E.2:4 - Solution
FPF rests on **eleven non‑negotiable pillars**. Each pillar is a binding constraint that every artefact, pattern, and design‑rationale record (DRR) **must** honour. Together they form the load‑bearing structure that guarantees evolvability, cross‑scale coherence, and didactic clarity.

| ID       | Pillar                         | Essence                                                                                                                   |
| -------- | ------------------------------ | ------------------------------------------------------------------------------------------------------------------------- |
| **P‑1**  | **Cognitive Elegance**         | Highlight decisive structure, eliminate ornamental formalism; separate data governance from thinking.                     |
| **P‑2**  | **Didactic Primacy**           | Human comprehension outranks theoretical or tooling purity.                                                               |
| **P‑3**  | **Scalable Formality**         | A single artefact can mature step‑by‑step from informal guess to formally assured state without forks or rewrites.        |
| **P‑4**  | **Open‑Ended Kernel**          | The Kernel contains only meta‑concepts; all domain knowledge lives in external patterns.                       |
| **P‑5**  | **FPF Layering**           | Patterns are modular, declarative extensions that can be added, replaced, or removed without destabilising the core. |
| **P‑6**  | **Lexical Stratification**     | Every core concept is expressible in four registers: plain name, technical term, formal U.Type, and mathematical symbol.  |
| **P‑7**  | **Pragmatic Utility**          | Proofs, metrics, and models exist to achieve real‑world objectives; falsification is rewarded over confirmation.          |
| **P‑8**  | **Cross‑Scale Consistency**    | Composition algebras (aggregation, boundary, emergence) are invariant across material systems, knowledge, and methods.    |
| **P‑9**  | **State Explicitness**         | Every artefact declares its state (`design‑time`, `run‑time`, etc.); transitions are cheap, traceable, auditable.         |
| **P‑10** | **Open‑Ended Evolution**       | Every entity is expected to evolve indefinitely; cycles must remain cheap, safe, and cognitively rewarding.               |
| **P‑11** | **State‑of‑the‑Art Alignment** | The kernel and extension domain-specific patterns track reliable contemporary knowledge and update when the SoTA advances.                     |

> Any DRR that contradicts a pillar must first amend this constitutional pattern.

### E.2:5 - Conformance Checklist

| ID         | Requirement                                                                                                                       | Purpose                               |
| ---------- | --------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------- |
| **CC‑P‑1** | Every architectural pattern **must** list which pillar(s) it instantiates or refines.                                             | Guarantees constitutional grounding.  |
| **CC‑P‑2** | Every DRR proposing a normative change **must** include a “Pillar Impact Analysis.”                                               | Makes constitutional review explicit. |
| **CC‑P‑3** | Tooling and pedagogical artefacts **should** document which pillar(s) shape their design.                                         | Upholds P‑2 (Didactic Primacy).       |
| **CC‑P‑4** | An pattern is conformant only if its invariants reference **≥ 3** pillars, demonstrating cross‑scale and pragmatic alignment. | Prevents narrow, siloed extensions.   |
| **CC‑P‑5** | When two lawful approaches exist, authors **SHOULD** prefer methods whose **empirical capability slope** is **non‑negative** over the **audited scale window** (data, compute, **freedom‑of‑action**) and **MUST** justify any exception **via** a **BLP Scale‑Audit** (**BLP‑1**) with **declared tolerances** *(α = budget; δ = assurance; units specified)*. | Embeds Bitter‑Lesson preference; curbs heuristic debt. |
 
### E.2:6 - Policy — Bitter‑Lesson Preference (BLP)

**Intent.** Favor **general, computation‑leveraged**, and **freedom‑of‑action** methods over hand‑tuned, brittle heuristics *when safety and legality are held constant*. This codifies the empirical trend that methods which scale with **data, compute, and search breadth** outpace bespoke rule‑engineering. **Applicability:** beyond ML, this policy covers **search/optimization**, **control**, **simulation‑based inference**, and other computational sciences where capability improves with scale and exploration. When **NQD/E/E‑LOG** promotes **novelty/coverage (illumination)** telemetry into dominance (via an explicit **CAL** policy; **policy‑id recorded in SCR**), these telemetry metrics are included in BLP comparisons for the audited window.

**BLP‑1 — Scale‑Audit Requirement.** Any DRR that selects a more specialized/hand‑engineered method over a general/scalable alternative **MUST** include a **Scale‑Audit**:
* (a) **Parity harness**: same **ComparatorSet**, **freshness window**, and **evaluation seeds/replicates**; portfolio‑first evaluation (see **G.5/G.9**). Dominance criterion: **Pareto‑only** by default across the declared objective vector; any alternative requires a documented waiver by **Gov‑CAL** under **E.3** precedence.
* (b) **Budgets**: sweep **compute** (**steps/tokens/params/time/energy**, as applicable), **data** (size/quality), and **freedom‑of‑action** (from script‑like instructions → minimal prohibitions) **under a fixed risk/safety envelope**. If any parameter cannot be swept, **pin** it and record the invariant.
* (c) **Slopes & uncertainty**: report ∂quality/∂compute, ∂quality/∂data, and (where applicable) ∂coverage/∂**freedom‑of‑action** and **∂novelty/∂budget**; include **error bars/CI** from multi‑seed trials; publish edition pins and policy‑IDs in SCR/telemetry (**G.11**).
* (d) **Resources**: publish **Resrc‑CAL** accounts (time/energy/FLOPs) and assurance deltas (B.3).  
* (e) **Objective declaration**: list the **objective vector** (quality, risk, cost, **and any illumination telemetry explicitly promoted into dominance via CAL** with **policy‑id recorded in SCR**) used for Pareto comparison.

**BLP‑2 — Preference Rule.** Given lawfulness and comparable assurance (within δ) and budget (within α), prefer the method whose **slope vector** is **Pareto‑dominant** over the audited range (per **BLP‑1c/1e**). If no dominance holds within error bounds, prefer the **more general** method (fewer domain‑specific heuristics, greater transfer via Bridges Φ/Ψ); otherwise resolve via **E/E‑LOG** tie‑breakers declared in policy.

**BLP‑3 — Minimal‑Prescription Default.** Author **rules‑as‑prohibitions** (negative constraints) over step‑by‑step scripts. Encode limits in **Φ policy tables** (and **Φ_plane** where applicable) instead of procedural checklists; allow the agent/system to sequence functions autonomously under those constraints (SoS‑LOG). **Pre/post‑conditions and test harnesses remain permitted**; **scripts** are permissible only when mandated by safety/regulation, or with compelling evidence recorded in the DRR **and reviewed under E.3 precedence / E.5 Guard‑Rails**.

**BLP‑4 — Heuristic‑Debt Register.** Any hand‑tuned rule admitted for pragmatic reasons **MUST** be registered as **Heuristic Debt** with: scope, owner, expiry/review window, measurable replacement target under BLP‑2, and a de‑hardening/sunset plan. Track in **CalibrationLedger/BCT (Baseline Change Tracker)** and cite in SCR.

**BLP‑5 — Continuous‑Learning Posture.** Where product policy allows, enable **feedback‑driven adaptation** (e.g., preference learning, critique loops) within Guard‑Rails (**E.5**) and privacy/regulatory controls, with appropriate opt‑outs where required. Disabling adaptation requires DRR justification and a review date.

**BLP‑6 — Precedence & Safeguards.** BLP is a **Gov/Arch** policy instantiated by Pillars **P‑10 (Open‑Ended Evolution)**, **P‑11 (SoTA Alignment)**, **P‑7 (Pragmatic Utility)**, and **P‑1 (Cognitive Elegance)**. It does **not** override safety/ethics (**E.5**) **nor** E.3 precedence rulings; where BLP conflicts with Guard‑Rails, **Guard‑Rails prevail**. When **NQD/E/E‑LOG** elevates illumination to dominance for exploration mandates, BLP **adopts that lens** rather than overriding it.

*Informative SoTA contexts (post‑2015):* portfolio‑first selection across **LLM prompt‑programming vs fine‑tuned task models**; **preference‑learning families (RLHF ↔ DPO)**; **QD archives (MAP‑Elites/CMA‑ME/DQD/QDax)**; **open‑ended environment–method co‑evolution (POET‑class)**; **offline RL vs Decision Transformer parity**; and beyond ML, **optimization/control** (model‑based planning vs hand‑tuned controllers) and **simulation‑based inference** in the sciences. These are **illustrative only**; use the parity harness instead of single‑winner leaderboards.

### E.2:7 - Conformance Checklist — BLP

| ID            | Requirement                                                                                                     | Purpose                                       |
| ------------- | --------------------------------------------------------------------------------------------------------------- | --------------------------------------------- |
| **CC‑BLP.1**  | Tolerances **α (budget)** and **δ (assurance)** are declared in the DRR or referenced via policy profile.      | Makes BLP decisions reproducible.             |
| **CC‑BLP.2**  | DRR includes a **Scale‑Audit** (BLP‑1a–e) with published slopes and pinned editions/policy‑IDs.               | Makes scale behavior auditable.               |
| **CC‑BLP.3**  | Selection decision cites **BLP‑2** and lists the governing pillars and precedence checks.                      | Ties choice to constitution.                  |
| **CC‑BLP.4**  | Any admitted heuristic is logged as **Heuristic Debt** with expiry/review and de‑hardening plan.               | Prevents silent drift toward brittle rules.   |
| **CC‑BLP.5**  | Default authoring uses **rules‑as‑prohibitions**; deviations are DRR‑justified and safety‑anchored.            | Preserves agent autonomy under constraints.   |
| **CC‑BLP.6**  | Resource accounts (time/energy/FLOPs) and assurance deltas are reported via **Resrc‑CAL** and B.3.             | Avoids “free heuristic” illusions.            |
| **CC‑BLP.7**  | **Replicate counts/seeds** and **confidence intervals** for slope estimates are recorded.                      | Prevents spurious slope inferences.           |

### E.2:8 - Relations
* **Instantiates pillars:** P‑10, P‑11, P‑7, P‑1.  
* **Depends on:** **G.5/G.9** (admission/comparator/selector & parity harness), **G.11** (refresh telemetry), **C.5** (Resrc‑CAL), **C.18** (NQD‑CAL), **C.19** (E/E‑LOG), **F.7/F.9** (Bridges, CL/Φ/Ψ).  
* **Constrained by:** **E.5** Guard‑Rails (DevOps Lexical Firewall; Notational Independence; Cross‑Disciplinary Bias Audit) and **E.3** precedence.

### E.2:9 - Definitions
**α (budget tolerance)** may be relative or absolute; declare units (e.g., % cost, wall‑time, energy). **δ (assurance tolerance)** is the permissible delta in assurance under **B.3**; declare measure and floor(s).

### E.2:10 - Consequences

*Positive*

* Provides an explicit “north star” for every contributor.
* Delivers a falsifiable checklist for evaluating proposals.
* Builds trust in high‑assurance domains through transparency.

*Trade‑offs*

* Constitutional review adds friction to rapid, informal changes.
* Amending the pillar set itself demands high‑bar governance.

### E.2:11 - Rationale

The pillars are distilled from systems engineering, philosophy of science, software architecture, and ontology design. They interlock: *Cognitive Elegance* (P‑1) enables *Didactic Primacy* (P‑2); *Open‑Ended Kernel* (P‑4) and *FPF Layering* (P‑5) make *Open‑Ended Evolution* (P‑10) and *SoTA alignment* (P‑11) feasible; *Cross‑Scale Consistency* (P‑8) provides the algebraic backbone for *Scalable Formality* (P‑3). This minimal yet sufficient set balances stability with change, rigor with accessibility, and abstraction with measurable impact.

### E.2:12 - Relations
* **Depends on:** `pat:constitutional/vision` – pillars operationalise the mission.
* **Refined by:** All subsequent patterns in the Core Specification.
* **Governs:** Every DRR, tool, and pedagogical artefact linked to FPF.

*These pillars are not a cage but the load‑bearing columns of a workshop where ideas can be safely built, dismantled, and evolved.*

### E.2:End


## E.3 - Principle Taxonomy & Precedence Model

### E.3:1 - Problem frame
Pattern E.2 supplies eleven immutable pillars, yet experience shows that a **flat list of principles invites ambiguity**: reviewers cannot decide which pillar overrules another  and “dead‑letter” rules accumulate. 

### E.3:2 - Problem

When two pillars or derived principles pull in opposite directions, architectural decisions stall—or worse, drift toward the loudest voice. Without an explicit **taxonomy and precedence cascade**, FPF risks devolving into subjective debate, breaking its claim to be a rigorously *auditable* “operating system for thought.”

### E.3:3 - Forces
| Force                                 | Tension                                                            |
| ------------------------------------- | ------------------------------------------------------------------ |
| **Categorical Clarity**               | Coherent grouping ↔ preservation of individual nuance              |
| **Deterministic Conflict Resolution** | Predictable hierarchy ↔ flexibility for context‑specific overrides |
| **Evolutionary Stability**            | Durable core ↔ adaptability to new knowledge                       |

### E.3:4 - Solution
#### E.3:4.1 - **Principle Taxonomy**
   Every principle is an instance of `U.Principle` assigned **exactly one** class ∈ { `Gov`, `Arch`, `Epist`, `Prag`, `Did` }.

   | Class                                    | Scope & Purpose                           | Example Pillars                                   |   |
   | ---------------------------------------- | ----------------------------------------- | ------------------------------------------------- | - |
   | **Gov** (Governance)                     | Change process, community decision‑making | P‑10 Open‑Ended Evolution - P‑11 SoTA             |   |
   | **Arch** (Architectural)                 | Macro‑structure & invariants              | P‑1 Cognitive Elegance - P‑4 Kernel               |   |
   | **Epist** (Epistemological and Ontological) | Semantics, evidence, trust                | P‑3 Scalable Formality - P‑8 Consistency          |   |
   | **Prag** (Pragmatic)                     | Real‑world value & cost/benefit           | P‑7 Pragmatic Utility                             |   |
   | **Did** (Didactic)                       | Cognition & learnability                  | P‑2 Didactic Primacy - P‑6 Lexical Stratification |   |

   *Epistemological* sub‑concerns (reasoning, falsifiability) reside inside **Onto**, avoiding category sprawl yet keeping semantics and trust in one bucket.

 #### E.3:4.2 - **Precedence Stack**

   | Level | Governing Artefact                    | Overrides        |
   | ----- | ------------------------------------- | ---------------- |
   | 0     | **Vision & Mission** (E.1)            | everything       |
   | 1     | **Eleven Pillars** (E.2)              | all below        |
   | 2     | **Principles** (this pattern)         | patterns & DRRs  |
   | 3     | Architectural / Definitional patterns | local rules      |
   | 4     | Tooling & Pedagogy                    | informative only |

**Within the precedence stack** the default order is:
`Gov ≫ Arch ≫ Epist ≫ Prag ≫ Did`

 **Graph Rule** — The precedence graph MUST be acyclic; any new edge that would form a cycle is **rejected**.
 
Governance principle vs Architectural principle clash: e.g. Core release schedule (Gov) outranks performance‑tuning (Prag)

### E.3:5 - Conformance Checklist

| ID          | Requirement                                                                                                          | Purpose                          |
| ----------- | -------------------------------------------------------------------------------------------------------------------- | -------------------------------- |
| **CC‑PT.1** | Every principle record **MUST** state `class` and may list `precedence_over[]`.                                      | Enables deterministic overrides. |
| **CC‑PT.2** | Precedence graph **MUST** be acyclic.    | Prevents circular law.           |
| **CC‑PT.3** | Any DRR introducing/modifying a principle **MUST** include a *Pillar Impact Analysis* and proposed precedence edges impact on each affected Pillar (P‑1… P‑11)| Aligns evolution with Pillars.   |

### E.3:6 - Illustrative Conflict Resolution

1. **The Conflict**  
   * **P‑1 Cognitive Elegance** (`Arch`) demands an unambiguous term for “part–whole” entities, pushing us toward **Holon**.  
   * **P‑2 Didactic Primacy** (`Did`) values immediate practitioner familiarity, pushing us to retain **System**.

2. **Risk of Stalemate**  
   Without a precedence cascade, the discussion would collapse into subjective argument: *“purity beats clarity!”* vs *“clarity beats purity!”*.

3. **Applying the Precedence Model**  
   * Default order: **Gov ≫ Arch ≫ Epist ≫ Prag ≫ Did**.  
   * `Arch` outranks `Did`; therefore **P‑1** takes formal precedence over **P‑2**.

4. **Principled Decision**  
   We adopted **Holon** to satisfy the higher‑priority principle and mitigated the didactic cost by:  
   * declaring `System ≡ U.System ⊑ U.Holon`,  
   * providing aliases and an “On‑Ramp” tutorial.

> *The precedence rule did not merely name a winner; it compelled a solution that honoured both principles in proportion to their rank.*

**Precedence (high → low).** Law & Regulation → **E.5 Guard‑Rails** → **B.3 Trust & Assurance** → **E.3 governance decisions** → **E/E‑LOG policies** (editioned) → **BLP (E.2)** → Product Policies → Implementation Tactics.

**Notes.**
* BLP is a constitutional policy (see E.2 / “BLP”), but **does not supersede** E.5 Guard‑Rails nor B.3 assurance floors; it **does govern** ties among lawful, comparable‑assurance options.
* Wherever **NQD/E/E‑LOG** promotes illumination telemetry to dominance (via an explicit **CAL** policy; **policy‑id recorded in SCR**), **BLP adopts that lens** rather than overriding it (see E.2 BLP‑6).
* Any exception to policy **MUST** include a DRR with rationale and expiry.
* **BLP Override (Waiver).** When a narrower hand‑engineered method is selected over a general/scalable alternative **within declared tolerances** (α = budget, δ = assurance), the DRR **MUST** include:
  - a **BLP Scale‑Audit** (see E.2 **BLP‑1**) covering compute/data/**freedom‑of‑action** sweeps and slope/uncertainty reporting,
  - the **tolerances** α/δ and objective vector used (E.2 **BLP‑1e**),
  - a **Heuristic‑Debt** entry (owner, scope, expiry/review, de‑hardening plan) per E.2 **BLP‑4**,
  - an **AutonomyProfileId** (see **E.3‑ABL**) and the GateDecision authority (see **Gate‑decision authority map** below).
**Portfolio‑first parity.** All precedence decisions that compare methods **MUST** use the G.5/G.9 parity harness and **Pareto** dominance; scalarisation across mixed scales/units is **prohibited** (B.3).

**BLP — Bitter‑Lesson Hooks into Precedence**
1) **Tie‑breaking.** If two lawful options are **within δ** assurance and **within α** budget, prefer the option whose **slope vector Pareto‑dominates** over the audited window; if no dominance, prefer the **more general** method. (E.2 **BLP‑2**.)
2) **Script‑vs‑Search conflicts.** For conflicts between **procedural scripts** and **general search/learning**, scripts prevail **only** when mandated by E.5 or regulation, or when a DRR records a **BLP‑waiver** with expiry and hazard rationale (E.2 **BLP‑3/6**).
3) **Publication.** Precedence rulings that reference BLP **MUST** publish editioned policy‑IDs, edition pins, and **Resrc‑CAL** accounts to the SCR (E.2 **BLP‑1d**; G.11).

**ABL — Autonomy‑Budget & Oversight Profiles (GateProfile)**
This section defines an **extensible family of autonomy oversight profiles** for agentic tool use: each profile specifies (i) a budget envelope, (ii) a Freedom‑of‑Action (FoA) descriptor, and (iii) the required **gate‑decision publication** to authorize execution under that envelope. The familiar labels **L0…L4** are treated here as **profile identifiers** (not a fixed managerial ladder): projects MAY introduce additional profiles or sub‑profiles by minting new profile ids, provided they publish the same fields (budgets, FoA, decision roles, telemetry contracts) and keep profile changes explicit and auditable.

| ProfileId | Name                         | Freedom‑of‑Action (FoA)                  | Explore‑Share (default) | Typical Use                                     | GateDecision authority |
|---------:|------------------------------|------------------------------------------|-------------------------|-------------------------------------------------|------------------------|
| **L0** | Scripted Execution           | **Whitelist only**; fixed scripts        | 0                       | Compliance‑critical, deterministic procedures   | Engineer‑of‑Record (EoR) |
| **L1** | Constrained Sequencing       | Negative constraints; **single‑tool**    | ≤ 0.10                  | Low‑risk automation with bounded novelty        | EoR + Peer Review |
| **L2** | Supervised Autonomy          | Multi‑tool plans; bounded replanning     | 0.20 (±0.10)            | Ambiguous tasks; moderate budget                | Team Lead + Safety |
| **L3** | Auditable Autonomy           | Multi‑step, self‑replanning; adaptive    | 0.30 (±0.10)            | Production agents with learning under guard‑rails | Product + Safety + Legal |
| **L4** | Open‑Ended / Research Mode   | Broad FoA within sandbox & rails         | 0.40–0.50               | Illumination‑first exploration, sandboxes only  | Governance Board (Gov‑CAL) |

**Normative requirements by profile.**
* **Budgets.** Each profile **MUST** declare ceilings for **time / compute / cost / risk** and a FoA descriptor; units must be explicit (Resrc‑CAL). Budgets are **hard gates** at run‑time (C.Agent‑Tools‑CAL **ATC‑3**).
* **Profile binding & change visibility.** Every CallPlan **MUST** declare the active profile id. Any profile change is a **GateCrossing** (E.18) and **MUST** be published (DecisionLog entry + pinned policy‑ids), so an auditor can reconstruct which profile governed which Window.
* **Assurance floors.** **B.3** WLNK minima on **F** and **R** apply at all profiles. Any profile‑specific tightening (e.g., higher required **R_eff** or stricter CL/Φ policies for broader FoA) **MUST** be declared on the profile and pinned by policy‑id. Pre‑deployment **assurance deltas** MUST be recorded for L2+.
* **Exploration discipline.** `explore_share` MUST be explicit in the **CallPlan** (C.Agent‑Tools‑CAL **ATC‑4**). Deviations from defaults require DRR justification.
* **Provenance.** L1+ MUST emit a **CallGraph** with Service/Method editions, EmitterPolicyRef, budget deltas, and observation hooks (C.Agent‑Tools‑CAL **ATC‑5/6**).
* **BLP conformance.** For L2+, selection MUST apply **BLP** (E.2 **BLP‑2**) with **α/δ** tolerances declared in the plan policy. Any admitted heuristic requires a **Heuristic‑Debt** entry (E.2 **BLP‑4**).
* **Learning/Adaptation.** L3–L4 MAY enable **feedback‑driven adaptation** within E.5 Guard‑Rails and privacy controls; L0–L2 default **off** unless a DRR documents mitigation (E.2 **BLP‑5**).
* **Human‑in‑the‑Loop (HITL).** HITL obligations are expressed as **gate decisions and pause/resume hooks**, not an implicit “approval ladder”:
  * **L0–L1:** execution MAY start only after an explicit **GateDecision** authorizing the CallPlan is present in the declared window.
  * **L2:** sentinels MUST be able to pause execution; resumption requires a new **GateDecision** recorded in the DecisionLog.
  * **L3:** the profile MUST declare periodic review windows; continued execution across a review boundary requires an explicit **GateDecision**.
  * **L4:** continuous telemetry review; the default locus is **sandboxed**; leaving the sandbox requires an explicit **GateCrossing** with a published CrossingSurface (E.18 + F.9/A.27).

**Gate‑decision authority map (default signers; who may author GateDecisions).**
* **L0:** EoR or appointed maintainer.
* **L1:** EoR **and** peer reviewer (two‑person rule).
* **L2:** Team Lead **and** Safety representative.
* **L3:** Product Owner **and** Safety **and** Legal/Privacy.
* **L4:** **Gov‑CAL Board** (multi‑disciplinary) with documented scope, time‑boxed **trial budget**, and rollback criteria.

**Profile promotion / demotion triggers.**
* **Promote** a profile when repeated **BLP‑consistent** results show stable assurance within δ and budget adherence within α for ≥ **N_policy** runs (declare **N_policy** in the active profile). Promotion is not implicit: a **GateDecision** **MUST** authorize the profile change and cite the slope evidence (E.2 **BLP‑1c**).
* **Demote** a profile when: (i) a sentinel breaches risk or budget, (ii) assurance drops below floors, (iii) policy changes, or (iv) a significant **heuristic‑debt** item expires without replacement. Demotion **MUST** be published as a GateCrossing with updated budgets/policies pinned.

### E.3:7 - **Conformance Checklist — E.3 ↔ BLP Interop**

| ID          | Requirement                                                                                                          | Purpose                          |
| ----------- | -------------------------------------------------------------------------------------------------------------------- | -------------------------------- |
| **CC‑E3.10** | Precedence list includes **BLP** explicitly **below** E/E‑LOG and **above** product tactics; conflicts handled via **BLP‑waiver** discipline. | Makes BLP’s standing auditable. |
| **CC‑E3.11** | Every DRR that overrides BLP **MUST** include a **Scale‑Audit** (E.2 **BLP‑1**) and a **Heuristic‑Debt** entry (E.2 **BLP‑4**). | Prevents silent heuristic drift. |
| **CC‑E3.12** | Each agentic plan declares an **AutonomyProfileId** (e.g., L0–L4) with explicit budgets, `explore_share`, and **E/E‑LOG EmitterPolicyRef**. | Aligns autonomy with assurance. |
| **CC‑E3.13** | L1+ executions emit **CallGraphs** with editioned policy/method ids and budget deltas; L3+ include adaptation status. | Ensures replayability & audit. |
| **CC‑E3.14** | Profile changes follow **promotion/demotion** triggers and are published as GateCrossings with edition pins in the SCR. | Keeps autonomy under control. |

### E.3:8 - Consequences
*Positive* — Turns subjective debate into objective, traceable decisions; high‑impact conflicts surface early.

### E.3:9 - Rationale
The chosen taxonomy mirrors FPF’s layered dependency: **Governance** rules how change occurs; **Architecture** shapes what can exist; **Epistemology** secures meaning and trust; **Pragmatics** and **Didactics** ensure usefulness and learnability. Explicit override edges supply the flexibility experts need, while the default hierarchy keeps day‑to‑day design deterministic—a “living constitution” that remains both human‑intelligible and machine‑enforceable.

### E.3:10 - Relations
* **Depends on:** `pat:constitutional/vision`, `pat:constitutional/pillars`
* **Governs:** All subsequent patterns and DRRs; Guard‑Rail patterns reference CC‑PT.\

> *“A taxonomy sorts principles; precedence gives them order—together they convert debate into design.”*

### E.3:End

## E.4 - FPF Artefact Architecture

### E.4:1 - Problem frame

The FPF ecosystem produces a wide range of artifacts, from timeless, normative principles to rapidly evolving pedagogical materials and executable tools. If these different types of artifacts are mingled without a clear architectural separation, the ecosystem becomes difficult to navigate, govern, and maintain. Users cannot easily distinguish binding rules from helpful advice, and the entire framework's release cycle becomes coupled to its most volatile component.

### E.4:2 - Problem

How can we structure the FPF ecosystem to ensure a clean separation of concerns between normative concepts, didactic materials, and executable tooling? A formal architecture is required to maintain conceptual purity, enable independent evolution of components, and provide a clear map for all stakeholders.

### E.4:3 - Forces

| Force | Tension |
| :--- | :--- |
| **Stability vs. Agility** | The conceptual core must evolve slowly and deliberately ↔ tools and tutorials must iterate quickly to keep pace with technology and user needs. |
| **Authority vs. Accessibility** | Users need to know which rules are normative and binding ↔ they also need accessible, non-normative guides to help them learn. |
| **Modularity vs. Cohesion** | The different artifact families must be able to evolve independently ↔ they must remain part of a single, coherent FPF ecosystem. |

### E.4:4 - Solution

The FPF ecosystem is formally stratified into three canonical **artefact families**. Each family has a distinct purpose and is governed by different rules, ensuring a clear separation of concerns. The interaction between these families is governed by the **Unidirectional Dependency Principle** (see Guard-Rail E.5.3).

1.  **The Conceptual Core (The Canon):** This family contains the **normative** pattern language of FPF. It is the single source of truth for all universal concepts, rules, and invariants. It is defined to be tool-agnostic and notation-independent. This family represents the timeless "law" of FPF.

2.  **The Tooling Reference:** This family contains **executable artifacts** that implement or verify the normative rules of the Core. This includes reference linters, simulators, and data schemas. This family is the "instrument" that makes the law of the Core operational.

3.  **The Pedagogical Companion:** This family contains **non-normative, didactic materials** designed to help humans learn and apply FPF. This includes tutorials, worked examples, and playbooks. This family is the "textbook" that explains both the law and the instruments.

### E.4:5 - Archetypal Grounding (System / Episteme)

*   **For a `U.System`:**
    *   **Conceptual Core:** Defines the universal pattern `U.System`.
    *   **Tooling Reference:** Provides a modeling language profile or a serialization schema for modeling systems.
    *   **Pedagogical Companion:** Provides a tutorial on how to model a water pump using that profile.

*   **For an `U.Episteme`:**
    *   **Conceptual Core:** Defines `U.Episteme` and the F-G-R characteristics.
    *   **Tooling Reference:** Provides the reference linting tool to automatically score epistemes.
    *   **Pedagogical Companion:** Provides a case study on how a scientific theory's R-score evolves over time.

### E.4:6 - Conformance Checklist

| ID | Requirement |
| :--- | :--- |
| **CC-E.4.1** | Every artifact in the FPF ecosystem **MUST** declare which of the three families (Core, Tooling, Pedagogy) it belongs to. |
| **CC-E.4.2** | The content of each artifact **MUST** be consistent with the defined purpose of its family (e.g., no normative rules in the Pedagogical Companion). |
| **CC‑E.4.3** | Artefacts in the Tooling or Pedagogy families SHALL NOT be imported by artefacts in the Conceptual Core. |

### E.4:7 - Consequences

| Benefits | Trade-offs / Mitigations |
| :--- | :--- |
| **Clear Separation of Concerns:** Users and contributors can immediately identify the nature and authority of any given artifact. | **Requires Discipline:** Authors must be careful to place new content in the correct artifact family. |
| **Decoupled Release Cycles:** The Core can maintain a stable, slow release cadence, while the Tooling and Pedagogy artifact family can evolve rapidly. | - |
| **Architectural Clarity:** Provides a simple, powerful mental model for navigating the entire FPF ecosystem. | - |

### E.4:8 - Rationale

This pattern establishes the macro-architecture of the entire FPF ecosystem. By separating the timeless "why" and "what" (the Conceptual Core) from the practical "how" (Tooling) and the educational "how-to-learn" (Pedagogy), it creates a system that is simultaneously stable, agile, and accessible. This layered architecture is a proven pattern in large-scale systems, from the OSI model in networking to the structure of modern operating systems, and it is essential for FPF's long-term health and scalability.

### E.4:9 - Relations

*   **Instantiates:** **P-5 (FPF Layering)** at a macro-level.
*   **Is Constrained by:** **E.5.3 (Unidirectional Dependency)**.
*   **Is Foundation For:** The entire authoring and governance model, as it defines the "territories" where different rules apply.

> *“A canon without a rationale is scripture; a rationale without a canon is gossip. FPF keeps both, fused in patterns.”*

### E.4:End

## E.5 - Four Guard‑Rails of FPF

### E.5:1 - Problem frame
FPF positions itself as a **timeless, universal “operating system for
thought.”**  Collaborative projects of this scope face four predictable
entropic pulls:

1. **Implementation gravity** – concept prose accretes tool jargon.  
2. **Notation lock‑in** – one diagram style becomes “the language.”  
3. **Convenience cycles** – quick fixes create reverse dependencies.  
4. **Disciplinary monoculture** – implicit bias colours “universal” rules.

Left unchecked, these forces erode Pillars **P‑1 Cognitive Elegance**,
**P‑4 Open‑Ended Kernel** and **P‑5 FPF Layering**.

### E.5:2 - Problem
Without explicit, non‑negotiable protectors the Conceptual Core would
slowly:

* entangle with transient technology terms,  
* hard‑freeze into a single dialect,  
* devolve into a tightly coupled “big ball of mud”,  
* betray its trans‑disciplinary promise.

### E.5:3 - Forces

| Force | Tension |
|-------|---------|
| **Purity vs Pragmatism** | Preserve pristine concepts ↔ need real examples. |
| **Universality vs Convention** | Rules valid across domains ↔ convenience of one familiar notation. |
| **Modularity vs Integration** | Independent layers ↔ temptation to cross‑link for speed. |
| **Objectivity vs Perspective** | Neutral framework ↔ Transformers’ unavoidable cultural lens. |

### E.5:4 - Solution — the Four Guard‑Rails
FPF establishes **four architecturally enforced guard‑rails** that every Core, Tooling, and Pedagogy artefact must obey.  They function as an “immune system” resisting each entropic pull.
**Scope note (conceptual, not lint).** These guard‑rails regulate the **architecture of thought**—concepts, claims, and their relations. They **do not** mandate tools, file formats, notations, or workflows; any linting or automation lives outside the Core and is optional, provided it preserves these conceptual constraints.


| # | Guard‑Rail | Protects against |
|---|------------|------------------|
| **GR‑1** | **DevOps Lexical Firewall** | Implementation, governance, automatisation and DevOps concerns gravity |
| **GR‑2** | **Notational Independence** | Notation lock‑in |
| **GR‑3** | **Unidirectional Dependency** | Convenience cycles |
| **GR‑4** | **Cross‑Disciplinary Bias Audit** | Disciplinary monoculture |

Concrete rules for each rail live in patterns **E.5.1 – E.5.4**.

### E.5:5 - Archetypal Grounding (System / Episteme)

| Guard‑Rail | `U.System` example | `U.Episteme` example |
|------------|-------------------|----------------------|
| GR‑1 | Definition of `U.System` never cites file formats or build scripts. | Definition of `U.Episteme` avoids naming specific proof engines. |
| GR‑2 | Pump boundary invariant is true in plain text or any diagram. | F‑G‑R semantics hold in algebraic or graph notation alike. |
| GR‑3 | A sizing helper imports Core invariants; Core never imports helper tutorials. | Learning guide cites R‑score; Core never cites guide. |
| GR‑4 | Bias audit removes thermo‑mechanical jargon from a “universal” pattern. | Audit replaces physics‑centric metaphors in a trust pattern. |

### E.5:6 - Conformance Checklist

| ID | Requirement | Purpose |
|----|-------------|---------|
| **CC‑GR.1** | Every new Core pattern **SHALL** cite, in its *Relations* section, the guard‑rail(s) it relies on or may affect. | Ensures traceability and deliberate rule interaction. |
| **CC‑GR.2** | Artefacts classified as Tooling or Pedagogy **MUST NOT** violate any rule in GR‑1 through GR‑4. | Keeps entropic forces outside the Conceptual Core. |
| **CC‑GR.3** | A revision to any guard‑rail pattern **REQUIRES** a Design‑Rationale Record that (a) states the reason, and (b) includes a Pillar‑impact analysis per E.3 precedence model. | Aligns evolution with higher‑level principles. |
| **CC‑GR.4** | The aggregate of guard‑rail rules **MUST** remain internally consistent and acyclic; no guard‑rail may override another without explicit precedence edges. | Preserves deterministic governance. |
| **CC‑GR.5** | Every Core pattern **MUST** anchor its primary subject with a declared **ReferencePlane** (`world | concept | episteme`) at first mention. | Keeps Core about “life” objects (extensional/intensional) rather than their paperwork, and aligns with CHR:ReferencePlane. |
*All CC‑GR duties are **conceptual**. Any automated checks are **informative only** and live in Tooling/Pedagogy.*

### E.5:7 - Consequences

| Benefits | Trade‑offs / Mitigations |
|----------|-------------------------|
| **Long‑term integrity** – stops slow drift of the Core toward jargon, notation lock‑in, and hidden cycles. | Authors must run a guard‑rail checklist before submission. *Mitigation:* template auto‑inserts the checklist. |
| **Stable yet evolvable ecosystem** – Core stays timeless while Tooling & Pedagogy can iterate rapidly. | Early stage contributions may feel constrained; examples in the Pedagogical Companion show compliant paths. |
| **Trust & auditability** – stakeholders can verify the framework’s purity independently. | Adds overhead to governance; justified by safety and longevity. |

### E.5:8 - Rationale
A constitution without enforcement degrades into *dead‑letter rules*.  
The four guard‑rails translate abstract Pillars into **concrete, testable
constraints**.  Grouping them under one umbrella pattern:

* gives newcomers a single “safety index” to consult,  
* makes compliance binary (*pass / amend*),  
* provides a stable anchor for future automated conformance tools—without
  mentioning any specific engine, thus honouring GR‑1 itself.

They collectively instantiate Pillars **P‑1**, **P‑2**, **P‑4**, **P‑5**
and reinforce the precedence order defined in **E.3**.

### E.5:9 - Relations

* **Comprises:**  
  * `pat:guard/devops‑firewall` (E.5.1) – GR‑1  
  * `pat:guard/notational‑independence` (E.5.2) – GR‑2  
  * `pat:guard/unidirectional‑dependency` (E.5.3) – GR‑3  
  * `pat:guard/bias‑audit` (E.5.4) – GR‑4
* **Depends on:**  
  * `pat:constitution/pillars` (E.2)  
  * `pat:constitution/principle‑taxonomy` (E.3)
* **Constrains:** every Core, Tooling, and Pedagogy artefact; all DRRs.

### E.5:End

## E.5.1 - DevOps Lexical Firewall

### E.5.1:1 - Problem frame
The FPF Core is meant to remain valid across decades and technology
generations.  Implementation details—file formats, build pipelines,
runtime flags—evolve rapidly and differ between domains.  When such
terms invade normative prose, the Core ages as quickly as the tools it
mentions.

### E.5.1:2 - Problem
*Conceptual erosion*: a rule that cites a transient technology becomes
obsolete when that technology fades, forcing unnecessary Core revisions
and fragmenting historical audits.

### E.5.1:3 - Forces

| Force | Tension |
|-------|---------|
| **Timelessness** | Concepts must survive tool turnover. |
| **Pedagogic clarity** | Examples need concreteness ↔ too much concreteness hard‑codes technology. |
| **Cross‑domain reach** | Physical‑system engineers and knowledge‑theorists use different stacks. |

### E.5.1:4 - Solution
Establish a **Lexical Firewall** around the **Conceptual Core** *(conceptual constraint; not a build‑time linter)*:

1. **Forbidden lexicon**  
   Normative patterns **SHALL NOT** contain tool‑or file‑specific words
   (e.g. protocol keywords, file extensions, IDE commands).  
   Permissible wording: “a reference parser”, “a serialisation schema”.

2. **Indirection rule**  
   When a Core concept needs an executable illustration, the pattern
   cites the **Tooling Reference family** artefact by *conceptual name*,
   never by concrete path or syntax.

3. **Glossary pointer**  
   If an unavoidable technical term appears, it is defined in a *Tooling Glossary* outside the Core and referenced by conceptual alias—not embedded.
*Non‑normative automation.* Machine checks **MAY** exist in Tooling; they are advisory and **MUST NOT** be imported into the Core.

### E.5.1:5 - Archetypal Grounding (System / Episteme)

| Scenario | `U.System` example | `U.Episteme` example |
|----------|-------------------|----------------------|
| **Normative text** | “A system boundary must expose at least one conserved‑quantity flow.” (No mention of modelling language.) | “An episteme records its F–G–R coordinates.” (No mention of proof syntax.) |
| **Illustrative link** | A modelling profile resides in the Tooling family; Core cites it as “the reference system‑profile”. | A linting routine lives in Tooling; Core cites it as “the reference episteme‑checker”. |

### E.5.1:6 - Conformance Checklist

| ID | Requirement |
|----|-------------|
| **CC‑LFW.1** | A Core pattern **SHALL** fail review if it contains implementation‑specific tokens. |
| **CC‑LFW.2** | References to executable artefacts **MUST** use conceptual names, not file paths or command strings. |
| **CC‑LFW.3** | Pedagogical examples inside Core **MAY** describe behaviour, but **MUST NOT** embed code snippets. |

### E.5.1:7 - Consequences

| Benefits | Trade‑offs / Mitigations |
|----------|-------------------------|
| Core stays evergreen and cross‑domain. | Authors must relocate concrete examples to Tooling or Pedagogy. |
| Reviewers can machine‑scan for banned tokens. | Requires a small vocabulary allow‑list; maintained in Tooling Guide. |

### E.5.1:8 - Rationale
Language shapes thought.  By firewalling transient jargon, we uphold
**P‑1 Cognitive Elegance** (clarity), **P‑2 Didactic Primacy** (domain‑neutral
exposition) and **P‑5 FPF Layering** (clean separation between Core
and Tooling).  The rule is content‑agnostic and thus itself immune to the
very decay it prevents.

### E.5.1:9 - Relations
* **Parent umbrella:** `pat:constitution/guard‑rails` (E.5)  
* **Constrains:** every pattern in Conceptual Core  
* **Instantiates pillars:** P‑1, P‑2, P‑5

### E.5.1:End

## E.5.2 - Notational Independence

### E.5.2:1 - Problem frame
FPF concepts must travel across academic disciplines, modelling tools,
and future notations we cannot yet foresee. If a normative pattern binds
its *meaning* to one diagram style, file syntax, or markup dialect, the
concept ages as soon as the notation does.

### E.5.2:2 - Problem
*Semantic lock‑in*: when a definition relies on a particular glyph set or
diagram grammar, alternative communities either translate it—risking
drift—or ignore FPF altogether.

### E.5.2:3 - Forces

| Force | Tension |
|-------|---------|
| **Expressiveness** | Diagrams and formal grammars aid precision ↔ they should never become the definition itself. |
| **Longevity** | A 20‑year horizon ↔ notation life‑cycles of 3‑5 years. |
| **Cross‑discipline adoption** | Mathematicians prefer algebraic syntax; engineers prefer schematics. |

### E.5.2:4 - Solution — Notational Independence Guard‑Rail *(conceptual; semantics over syntax; not a notation mandate)*

1. **Semantics primacy**  
   Normative content **SHALL** define concepts in linguistic form first
   (plain English + mathematics if needed). Visual or syntax examples
   are secondary illustrations.

2. **Equivalence clause**  
   When an official alternate notation exists, the pattern must state:
   *“Representation A and Representation B are semantically equivalent
   under mapping M.”*

3. **Reference indirection**  
   If the Core cites a diagram, it does so by *conceptual role*
   (“reference boundary schematic”) rather than by file or syntax name.

4. **Conceptual prefix neutrality**  
   FPF **conceptual prefixes** (e.g., `U.`, `Γ_`, `ut:`, `tv:`, `ev:`, `mero:`) are  **cognitive namespaces**, not syntax tokens. Core patterns **MUST NOT**  tie their meaning to any concrete serialisation or URI scheme for these prefixes; any expansions are **illustrative only** and live in Tooling or Pedagogy.

5. **Cards and other "forms"**
Cards, tables and other "forms" exist in FPF core only as conceptual model, not as data model, thus no need to data-related notation or notation for lint. Comformance checklist and quards is also conceptual, argumentation like "this will ease machine check" is forbidden, no machine checking is intended in core; machine checks and linters live only in Tooling.

### E.5.2:5 - Archetypal Grounding (System / Episteme)

| Scenario | `U.System` example | `U.Episteme` example |
|----------|-------------------|----------------------|
| Definition | Boundary of a pump is expressed in prose plus set notation; a diagram is illustrative. | F‑G‑R characteristics defined textually; a triple‑store serialisation is illustrative. |
| Alternate rendering | Same pump semantics rendered in a lattice diagram or a tabular sheet remain valid. | R‑scores plotted in a heatmap or listed in CSV remain equivalent. |

### E.5.2:6 - Conformance Checklist

| ID | Requirement |
|----|-------------|
| **CC‑NI.1** | A Core pattern **MUST NOT** embed semantics that hinge on one specific notation. |
| **CC‑NI.2** | Illustrative renderings **SHALL** be marked “informative”. |
| **CC‑NI.3** | When multiple official renderings exist, the pattern **MUST** declare the semantic mapping between them. |
| **CC‑NI.4** | If a **conceptual prefix** appears in Core, its expansion (if shown) **SHALL** be marked *informative* and **MUST NOT** be required to interpret the semantics. |

### E.5.2:7 - Consequences

| Benefits | Trade‑offs / Mitigations |
|----------|-------------------------|
| Ensures FPF survives notation turnover. | Authors invest time describing mappings; mitigated by reusable mapping templates. |
| Lowers entry barrier for domains using different diagram traditions. | Excessive illustrations can bloat pages; guidance in Pedagogical Companion limits scope. |

### E.5.2:8 - Rationale
Language and diagrams are tools, not truths. By elevating semantics over
syntax, FPF maintains **P‑1 Cognitive Elegance** and **P‑2 Didactic
Primacy** while safeguarding **P‑5 FPF Layering**: tooling layers can
add new renderers without Core edits.

### E.5.2:9 - Relations
* **Parent umbrella:** `pat:constitution/guard‑rails` (E.5)  
* **Constrains:** every normative Core pattern and official alternate rendering  
* **Instantiates pillars:** P‑1, P‑2, P‑5

### E.5.2:End

## E.5.3 - Unidirectional Dependency

### E.5.3:1 - Problem frame
FPF separates artefacts into stable **Conceptual Core**, executable
**Tooling Reference**, and fast‑evolving **Pedagogical Companion** (see
E.4 Artefact Architecture).  If dependencies can point *both* ways,
volatile layers will eventually drag the Core into rapid revision
cycles or introduce domain‑specific bias.

### E.5.3:2 - Problem
*Architectural gravity*: a tutorial or helper script adds a new feature,
Core patterns import it “temporarily,” and within months the supposedly
timeless layer depends on transient assets—breaking Pillar **P‑5
FPF Layering**.

### E.5.3:3 - Forces

| Force | Tension |
|-------|---------|
| **Agility vs Stability** | Tooling must iterate quickly ↔ Core must remain slow and deliberate. |
| **Reuse vs Isolation** | Authors want to reuse helper concepts ↔ Core cannot depend on volatile code. |
| **Simplicity** | Rule must be testable and unambiguous ↔ must allow legitimate upward imports. |

### E.5.3:4 - Solution — One‑Way, Acyclic Imports
Define a strict **partial order** over artefact families **and guard meaning flow** (see **E.10 V‑1**): imports point only **upward** in stability, and **no Core semantics** may derive from Tooling/Pedagogy. No linters or machine checking in Conceptual Core.

**`imports` is a dependency DAG, not a specialisation relation (normative).** Whenever an artefact exposes an explicit `imports : [...]` list (e.g., `SignatureManifest.imports` in A.6.0), treat `imports` as **dependency edges** governed by this section: the induced `imports` graph MUST be **acyclic** (a DAG) and MUST respect the declared direction. `imports` MUST NOT be used to encode *specialisation* (e.g., `⊑` / `⊑⁺` between mechanisms); specialisation relations are declared separately via the relevant morphism/ladder rules (e.g., A.6.1 `U.MechMorph`).

Pedagogical Companion  ⟶  Tooling Reference  ⟶  Conceptual Core

1. **Allowed edges**  
   Dependencies **MAY** point **only upward** (toward greater semantic
   stability). No cycle is ever permitted.

2. **No downward import**  
   Core artefacts **SHALL NOT** import Tooling or Pedagogy artefacts.
   Tooling artefacts **SHALL NOT** import Pedagogy artefacts.

3. **Future layers**  
   Any new family is inserted below an existing one or becomes part of
   the Tooling or Pedagogy strata; the ordering extends accordingly.

### E.5.3:5 - Archetypal Grounding (System / Episteme)

| Layer | `U.System` illustration | `U.Episteme` illustration |
|-------|------------------------|---------------------------|
| Core | Definition of `U.System` and boundary invariant. | Definition of F‑G‑R characteristics. |
| Tooling | “Reference system‑profile” that checks boundary flow; *imports* Core invariants. | “Episteme‑scoring routine” that calculates R‑score; *imports* Core characteristics. |
| Pedagogy | Tutorial using the system‑profile to model a pump; *imports* profile and Core term. | Case study explaining R‑score evolution; *imports* scoring routine and Core term. |
| **Forbidden** | Core pattern importing measurement script. | Core pattern importing R‑score web dashboard. |

### E.5.3:6 - Conformance Checklist

| ID | Requirement |
|----|-------------|
| **CC‑UD.1** | Dependency graph among all artefacts **MUST** be acyclic. |
| **CC‑UD.2** | An artefact **SHALL** import only from its own family or any family above it in the order. |
| **CC‑UD.3** | A DRR that introduces a downward edge **SHALL** be automatically rejected. |

### E.5.3:7 - Consequences

| Benefits | Trade‑offs / Mitigations |
|----------|-------------------------|
| Core stays free of tool churn and tutorial bias. | Authors must create abstraction layers in Tooling instead of inserting hooks into Core. |
| Release cadence decoupled: Core (slow), Tooling (medium), Pedagogy (fast). | Slight duplication when multiple tools target same concept; mitigated by shared Core definitions. |

### E.5.3:8 - Rationale
One‑way import graphs are a proven safeguard in operating systems
(kernel vs user land) and layered protocols. Here the rule operationalises
Pillars **P‑4 Open‑Ended Kernel** and **P‑5 FPF Layering**, ensuring
that innovation happens “below” without contaminating the timeless Core.

### E.5.3:9 - Relations
* **Parent umbrella:** `pat:constitution/guard‑rails` (E.5)  
* **References layer definition:** `pat:constitution/artefact‑architecture` (E.4)  
* **Instantiates pillars:** P‑4, P‑5  
* **Constrains:** All artefact imports recorded in DRRs or SCRs

### E.5.3:End

## E.5.4 - Cross‑Disciplinary Bias Audit

### E.5.4:1 - Problem frame
FPF calls itself trans‑disciplinary, but every author carries implicit
metaphors from a home domain. If those metaphors leak into “universal”
patterns, practitioners from other fields disengage or mis‑interpret the
rules.

### E.5.4:2 - Problem
Unrecognised bias hides in wording, examples, unit choices or principle
weighting. Once embedded in normative language, such bias is hard to
remove and contradicts Pillars **P‑2 Didactic Primacy** and **P‑8
Cross‑Scale Consistency**.

### E.5.4:3 - Forces

| Force | Tension |
|-------|---------|
| **Neutrality** | One voice for all disciplines ↔ need for relatable examples. |
| **Conciseness** | Audit guidance must be brief ↔ must cover multiple bias types. |
| **Longevity** | Guidance must survive emergence of new domains. |

### E.5.4:4 - Solution — Principle‑Taxonomy‑Guided Bias Audit

1. **Bias‑Lens set**  
   Every normative pattern is assessed through **five lenses** that match the
   Principle classes from **E.3**:  
   `Gov`, `Arch`, `Onto/Epist`, `Prag`, `Did`.

2. **Equilibrium question**  
   For each lens ask:  
   *“Does the pattern over‑privilege this class or silence it?”*  
   *Examples:*  
   *   Over‑reliance on `Onto/Epist` precision may ignore `Prag` cost.  
   *   Dominant `Arch` metaphors may alienate `Did` audiences.

3. **Scope‑or‑Balance rule**  
   * If imbalance is found and universality is intended, re‑phrase to
     restore balance.  
   * If imbalance is intentional (domain‑specific pattern), mark the
     scope explicitly: *“Applies primarily to thermodynamic systems.”*

4. **Audit trace**  
   The pattern carries a short **Bias‑Annotation** paragraph recording
   which lenses were tested and any scoping statement. No workflow checklists or
   reviewer metadata or other data and data format and data governance tips is stored in the Core.

### E.5.4:5 - Archetypal Grounding (System / Episteme)

| Bias lens | Example imbalance | Conceptual correction |
|-----------|------------------|-----------------------|
| `Arch` vs `Did` | Pump pattern uses abstract category theory terms. | Add plain‑language boundary narrative or move abstraction to appendix. |
| `Onto/Epist` vs `Prag` | Episteme trust score defined with complex logic but no guidance on empirical cost. | Add pragmatic note on evidence collection burden or scope the pattern. |

### E.5.4:6 - Conformance Checklist

| ID | Requirement | Purpose |
|----|-------------|---------|
| **CC‑BA.1** | Each Core pattern **SHALL** include a *Bias‑Annotation* listing the five lenses and any declared scope limitation. | Ensures explicit reflection on bias. |
| **CC‑BA.2** | A pattern labelled “universal” **MUST NOT** privilege a single lens without justification or scoping note. | Preserves trans‑disciplinary integrity. |
| **CC‑BA.3** | If scope is declared, the pattern **SHALL** reference the mapping or rationale that enables cross‑domain translation. | Keeps pathways open for other calculi. |
| **CC‑BA.4 (QD‑triad evidence for “universal”).** | Any pattern that labels itself **“universal”** SHALL cite **A.8 CC‑UC 1 + CC‑UC 2** and attach the **QD evidence** (Diversity_P + IlluminationSummary, with edition and binning) or else **scope** the claim to its home Context. | preserves domain quality diversity |

### E.5.4:7 - Consequences

| Benefits | Trade‑offs / Mitigations |
|----------|-------------------------|
| Neutral, inclusive language attracts wider adoption. | Authors spend a few extra lines on Bias‑Annotation; mitigated by template snippet. |
| Bias is surfaced at writing time, not after publication. | — |

### E.5.4:8 - Rationale
Coupling the audit directly to the Principle Taxonomy keeps the guard‑rail
**concept‑driven**, not workflow‑driven. No mention of review boards,
CI‑jobs, or checklists appears in the Core; such mechanics belong in the
Tooling Guide. This guard‑rail therefore satisfies **GR‑1** (Firewall)
while securing Pillars **P‑2, P‑7 Pragmatic Utility, P‑8**.

### E.5.4:9 - Relations
* **Parent umbrella:** `pat:constitution/guard‑rails` (E.5)  
* **Depends on:** `pat:constitution/principle‑taxonomy` (E.3)  
* **Constrains:** All normative patterns claiming universality

### E.5.4:End


## E.6 - Didactic Architecture of the Specification

### E.6:1 - Problem frame
FPF addresses readers from at least two characteristics of diversity:

* **Disciplinary** – systems engineers, knowledge scientists, ethicists.  
* **Experience** – newcomers need intuition; experts need rigour.

Past drafts mixed governance mandates with domain examples, producing a
steep learning curve and repeated “forward‑reference” detours.

### E.6:2 - Problem
If core ideas are buried under formalism or scattered across parts,
readers either give up or misuse the framework. We need a **fixed
narrative scaffold** that guides cognitive load from low to high while
keeping normative sections discoverable.

### E.6:3 - Forces

| Force | Tension |
|-------|---------|
| **Cognitive Load** | Early clarity ↔ eventual formal depth. |
| **Conceptual Integrity** | Foregoing examples risks abstraction ↔ too many examples delay axioms. |
| **Uniform Flow** | Single, predictable roadmap ↔ flexibility for future parts. |

### E.6:4 - Solution — “On‑Ramp to Archetypes first, Authoring last” sequence

The "On-Ramp First" Macro-Structure: The specification is ordered to create a smooth cognitive ramp:
* It begins with an informal, non-normative Preface (The On-Ramp), which uses storytelling and concrete examples (System and Episteme) to build intuition.
* It then proceeds through the normative Parts (A-D), moving from the foundational kernel to the rich patterns of trans-disciplinary reasoning.
* It concludes with the authoring rules (Part E) and appendices, ensuring that this "meta" content does not obstruct the primary learning path.

1. **Preface (On‑Ramp)**  
   Informal tour; introduces `U.System` and `U.Episteme` via concrete
   stories before any normative language appears.

2. **Part A Kernel**  
   Minimal holonic ontology and the Transformer principle give readers
   the essential vocabulary.

3. **Part B Trans‑disciplinary Reasoning**  
   Tell‑Show‑Show pedagogy: universal rule → Sys‑CAL example →
   KD‑CAL example.

4. **Part C Extention Patterns**  
   Domain‑specific calculi expand on the examples already seen.

5. **Part D Ethics & Conflict Optimisation**  
   Shows reflective patterns only after readers grasp holonic reasoning.

6. **Part E Authoring**  
   Constitution, guard‑rails, and contributor rules come last; novices
   can postpone reading.

7. **Appendices (Annexes)**  
   Tutorials, tooling guides, and migration scripts live here.

### E.6:5 - Archetypal Grounding (System / Episteme)

| Narrative layer | First sight of `U.System` | First sight of `U.Episteme` |
|-----------------|---------------------------|-----------------------------|
| Preface | Coffee‑machine story (pump as system). | Meta‑analysis story (study bundle as episteme). |
| Part A | Formal definition inherits boundary invariant. | Formal definition inherits F‑G‑R coordinates. |
| Part B Tell‑Show‑Show | Γ\_sys example: assemble pump. | Γ_epist example: merge study bundle. |

### E.6:6 - Conformance Checklist

| ID | Requirement |
|----|-------------|
| **CC‑DA.1** | Each Part **SHALL** open with a one‑paragraph situational “hook” before formal text. |
| **CC‑DA.2** | Every architectural pattern **MUST** implement Tell‑Show‑Show: universal rule plus System & Episteme illustrations. |
| **CC‑DA.3** | Governance patterns (**Part E**) **SHALL NOT** appear before the Kernel in the main document flow. |

### E.6:7 - Consequences

| Benefits | Trade‑offs / Mitigations |
|----------|-------------------------|
| Smooth learning curve; readers can stop at their needed depth. | Template discipline required; mitigated by authoring guide (E.8). |
| Reduces forward‑reference clutter; each concept is primed before formal use. | Preface evolves when new archetypes added; handled via On‑Ramp revision DRR. |

### E.6:8 - Rationale
Educational research shows retention improves when abstract rules are
immediately paired with contrasting illustrations. By fixing the reading
order and mandating Tell‑Show‑Show inside every architectural pattern, FPF
embeds pedagogy into its architecture, realising Pillars **P‑2 Didactic
Primacy** and **P‑1 Cognitive Elegance** without weakening rigour.

### E.6:9 - Relations
* **Depends on:** `pat:constitution/guard‑rails` (GR‑1 ensures example jargon stays outside Core).  
* **Constrains:** Placement of all Parts, patterns, and appendices.  
* **Instantiates pillars:** P‑1, P‑2
  
### E.6:End

## E.7 - Archetypal Grounding Principle

### E.7:1 - Problem frame
Universal rules are powerful only when readers can grasp them. In FPF the
Conceptual Core speaks in substrate‑agnostic language: `U.Holon`,
Γ‑aggregation, MHT emergence. Practitioners need to “see” those rules in
familiar matter—physical hardware or bodies of knowledge—before they can
reuse them.

### E.7:2 - Problem
A purely abstract statement risks two failures:

1. **Didactic failure** – readers dismiss the pattern as “too meta,”
   violating Pillar **P‑2 Didactic Primacy**.  
2. **Unproven universality** – without cross‑domain instantiation the rule
   remains an untested claim.

### E.7:3 - Forces

| Force | Tension |
|-------|---------|
| **Universality vs Concreteness** | Abstract law ↔ concrete example. |
| **Brevity vs Clarity** | Spec should stay concise ↔ dual examples add length. |
| **Rigour vs Accessibility** | Formal semantics ↔ intuitive narrative. |

### E.7:4 - Solution — mandatory *Archetypal Grounding* subsection

Every architectural pattern **SHALL** include a dedicated
section, titled exactly **“Archetypal Grounding,”** that *shows* how the
abstract law SCRs in FPF’s two canonical holon flavours:

1. **`U.System`** – the archetype of a **physical, operational holon**.  
2. **`U.Episteme`** – the archetype of an **abstract, epistemic holon**.

This enforces a repeatable **Tell‑Show‑Show** rhythm:

| Stage | Content |
|-------|---------|
| **Tell** | `Solution` section states the universal rule. |
| **Show #1** | `Archetypal Grounding` – concrete `U.System` example. |
| **Show #2** | Same section – parallel `U.Episteme` example. |

### E.7:5 - Archetypal Grounding (of this pattern itself)

| Universal rule | `U.System` instantiation | `U.Episteme` instantiation |
|----------------|--------------------------|----------------------------|
| “Every architectural pattern requires grounding.” | Pattern *D.1 Algebra of Aggregation* illustrates Γ\_sys on assembling a water pump. | The same pattern illustrates Γ_epist on merging a meta‑analysis. |

### E.7:6 - Conformance Checklist

| ID | Requirement | Purpose |
|----|-------------|---------|
| **CC‑AG.1** | Every architectural pattern in Parts A, B, C, D, E **SHALL** contain a subsection headed exactly *“Archetypal Grounding”*. | Guarantees consistent Tell‑Show‑Show rhythm. |
| **CC‑AG.2** | The Archetypal Grounding subsection **MUST** illustrate the rule with both `U.System` *and* `U.Episteme`. | Demonstrates trans‑disciplinary reach. |
| **CC‑AG.3** | If a rule intentionally applies to only one substrate, the subsection **SHALL** state the scope limitation and justify it against the five Principle‑Taxonomy lenses (`Gov`, `Arch`, `Onto/Epist`, `Prag`, `Did`). | Prevents silent bias; links to Bias‑Audit guard‑rail. |
| **CC‑AG.4** | Patterns lacking a compliant Archetypal Grounding subsection **MAY NOT** progress to “Accepted” status. | Enforces discipline without referring to workflow mechanics. |

### E.7:7 - Consequences

| Benefits | Trade‑offs / Mitigations |
|----------|-------------------------|
| **Immediate clarity** – readers see abstract laws in action. | Patterns grow by one short table; mitigated by consistent template snippet. |
| **Proof of universality** – every rule is self‑documenting across substrates. | Authors must think cross‑domain; fosters richer patterns. |
| **Narrative cohesion** – recurring System/Episteme protagonists create a memorable storyline. | — |
|Built-in Proof of Universality: The specification consistently demonstrates its trans-disciplinary claims, building trust and credibility. | — |

### E.7:8 - Rationale
Tell‑Show‑Show is a proven pedagogical sequence. By making it normative,
FPF hard‑codes **P‑2 Didactic Primacy** into the fabric of every architectural
pattern while still honouring **P‑1 Cognitive Elegance**—the grounding
section replaces brittle ad‑hoc anecdotes with a disciplined dual
example. Linking scope‑justification to the five Principle lenses ties the
pattern to the **Taxonomy‑Guided Bias Audit** and keeps governance
language out of the Core.

### E.7:9 - Relations

* **Implements macro flow:** `pat:authoring/didactic‑architecture` (E.6)  
* **References base types:** `pat:kernel/holon` (A.1) (`U.System`, `U.Episteme`)  
* **Interacts with bias guard‑rail:** `pat:guard/bias‑audit` (E.5.4) via CC‑AG.3  
* **Constrains:** Authoring template in `pat:authoring/pattern‑template` (E.8)

### E.7:End

## E.8 - FPF Authoring Conventions & Style Guide

> **Type:** Architectural (A)  
> **Status:** Stable  
> **Normativity:** Normative (unless explicitly marked informative)

### E.8:1 - Problem frame
FPF grows through the addition of patterns written by authors from many
disciplines. Without a shared structure *and* voice, the framework would
fracture, violating Pillars **P‑1 Cognitive Elegance** and
**P‑2 Didactic Primacy**.

### E.8:2 - Problem
*Structural drift* and *stylistic fragmentation* threaten three qualities:

1. **Comparability** – readers cannot align patterns lacking common
   headings.  
2. **Narrative cohesion** – prose swings from dry jargon to informal
   blog style.  
3. **Auditability** – missing sections hide safety checks
   (Archetypal Grounding, Bias‑Annotation).

### E.8:3 - Forces

| Force | Tension |
|-------|---------|
| **Uniformity vs Expressiveness** | Consistent template ↔ freedom for diverse domains. |
| **Rigor vs Readability** | Formal precision ↔ engaging prose. |
| **Brevity vs Completeness** | Concise patterns ↔ mandated safety subsections. |

### E.8:4 - Solution — One template, enriched by style principles

#### E.8:4.1 - Canonical Pattern Template
Within each pattern, the **canonical** section headings **SHALL** appear in the order below.
For each **canonical content section heading (1–12)**, the `<Title>` component (after the heading separator, e.g. ` - `) **MUST** start with the canonical section title (case-insensitive match; canonical capitalisation preferred); an optional clarifier after an em dash is allowed (e.g., `Solution — …`).
The **Footer marker** (section **13**, if present) is a sentinel and is governed by **H‑9** rather than the standard `<FullId> - <Title>` shape.

**Extensibility.**
Authors **MAY** add additional sections. Prefer expressing them as subsections under the nearest canonical section (e.g., `4.1`, `4.1.1` under *Solution*). If an additional top-level section is necessary, it **MUST NOT** delete or reorder the canonical sections and its title **MUST NOT** shadow a canonical title.

**Mandatory vs optional.**
* Canonical sections **1–13** are mandatory in every pattern.
* The escape hatch `Not applicable` is permitted **only** where explicitly stated below; when used, it **MUST** include a short justification (1 paragraph).

**Template:**
- **Title line:** Hashes + FullId + ` - ` + Pattern Title; optional `(informative)` note.
- **Header block:** Type, Status; optional Normativity override.
1. **Problem frame**
2. **Problem**
3. **Forces**
4. **Solution**
5. **Archetypal Grounding** (Tell–Show–Show; System / Episteme; `Not applicable` allowed only with justification)
6. **Bias‑Annotation**
7. **Conformance Checklist**
8. **Common Anti‑Patterns and How to Avoid Them** (`Not applicable` allowed only with justification)
9. **Consequences**
10. **Rationale**
11. **SoTA‑Echoing** (post‑2015 practice alignment; terminology drift & deltas; `Not applicable` allowed only with justification)
12. **Relations**
13. **Footer marker** 

**Footer marker.** End each pattern with a single visible sentinel heading line on its own: `### <PatternId>:End`. This makes truncation detectable even when HTML comments are stripped or surfaced by editors. The footer marker is intentionally content‑free: **do not** place prose under it.

*Note.* Pattern boundaries are still parseable by scanning for the next pattern heading (`## …`), but an explicit `:End` marker helps retrieval pipelines (and LLM prompts) distinguish “this chunk is the whole pattern” from “this chunk was cut mid‑pattern”.

##### E.8:4.1.1 - Heading & ID discipline (human tooling + retrieval)
FPF is often consumed through full‑text search and retrieval (RAG). A reader or an LLM may see a subsection without its parent headings, so headings must be **self‑identifying**.

**H‑1 (Heading shape).** Every pattern heading and every subsection heading inside a pattern **SHALL** follow:
`<hashes> <FullId> - <Title> (optional note of non‑normativity)`

*Exception.* The **Footer marker** is a sentinel heading and is governed by **H‑9**, not by the standard `<FullId> - <Title>` shape.

**H‑2 (Heading separator).** The canonical separator between `<FullId>` and `<Title>` is ` - ` (ASCII, space-hyphen-space).
Legacy text may use ` - `; tooling **SHOULD** treat the two as equivalent, and authors **SHOULD** migrate to ` - ` when touching a heading.

**H‑3 (FullId).** `FullId` is the full hierarchical address.
For a **pattern heading** it is the pattern ID (e.g., `A.2`, `E.10.D1`).
For **headings inside a pattern**, append dot‑separated ordinal section numbers after the colon (`:`) (e.g., `A.2:4.4`, `E.10.D2:3`).
*Exception:* the Footer marker uses the reserved sentinel token `:End` as defined in **H‑9**.
The colon (`:`) is **reserved** for section paths and **MUST NOT** appear in pattern IDs.

**H‑4 (Ordinals).** Ordinals in section paths **SHOULD** track the canonical template numbering (**1 = Problem frame**, …, **13 = Footer marker**) to maximise cross‑pattern comparability. During refactors or in legacy patterns, ordinals **MAY** be local. In that case, the **canonical section title at the start of `<Title>`** is the semantic key; readers and tools **MUST NOT** infer section semantics from the ordinal alone.
*Note:* the Footer marker itself is exempt from ordinal encoding; it uses the reserved token `:End` (see **H‑9**).

**H‑5 (Where kind and normativity live).** Pattern **kind** (e.g., Architectural / Definitional) **MUST** be declared in the **Header block**, not encoded into the heading text. Normativity (**normative** / **informative**) **MUST** also live in the Header block when it deviates from the default. If a reminder is needed for readers, authors **MAY** add a short parenthetical note at the end of the heading (e.g., `(informative)` / `(non‑normative)`), but headings **MUST NOT** use square‑bracket tags.

**H‑6 (Heading levels).** Heading levels **MUST** preserve a fixed offset between structural layers (Part or Cluster (flat) → Pattern → Pattern sections):
* Part and Cluster headings **MUST** use `#` (level 1) across the file.
* A Pattern heading **MUST** use `##` (level 2).
* Inside a pattern, each nested section **MUST** add exactly one `#` per level (e.g., `## A.2 - …`, `### A.2:2 - …`, `#### A.2:2.1 - …`).

**H‑7 (Ellipsis discipline).** Authors **MUST NOT** use **three consecutive full stops/dots** (`...`) as punctuation in headings or narrative prose. Authors **MUST** use the Unicode ellipsis `…` (U+2026) instead. For editorial elisions in quotations, authors **SHOULD** prefer `[…]` to make the omission explicit and distinguish it from retrieval truncation.
*Exception:* literal three‑dot sequences that are part of an external language’s syntax **MAY** appear **only inside code spans or fenced code blocks**.

**H‑8 (Normative keywords).** The key words **MUST**, **MUST NOT**, **REQUIRED**, **SHALL**, **SHALL NOT**, **SHOULD**, **SHOULD NOT**, **RECOMMENDED**, **MAY**, and **OPTIONAL** are to be interpreted as described in RFC 2119, as clarified by RFC 8174 (only when capitalised). Authors **SHOULD** avoid informal deontic phrasing (“need to”, “is required to”) in normative clauses.

**Deontics vs admissibility.** Use RFC keywords only for **deontic obligations** (requirements on authors, reviewers, implementers/tooling, or published artefacts) — i.e., things an agent can choose to do or omit. Do **not** use RFC keywords to state **definitions**, **structural invariants**, **typing rules**, or other **admissibility conditions** of the modeled world.

When you need an enforceable constraint that is *mathematical* rather than *deontic*, express it as a non‑deontic predicate using one of: `Definition:`, `Invariant:`, or `Well‑formedness constraint:` (optionally with formal quantifiers). Prefer mathematical terms like `cardinality 1..1 (total)` / `0..1 (partial)` / `0..n` over deontic adjectives like “mandatory/optional” when the intent is cardinality, not duty.

**Admissibility predicate discipline (recommended shape).**
When expressing admissibility/validity constraints as predicates (`Definition:` / `Invariant:` / `Well‑formedness constraint:`):
* Authors **MUST NOT** use RFC keywords inside the predicate block.
* Authors **SHOULD** give each predicate a stable identifier and short name (e.g., `RA‑1 (Locality)`, `RE‑3 (Method gate)`), so that Conformance Checklist items can reference it without re‑authoring the rule.
* Authors **SHOULD** write the constraint as a declarative predicate (optionally quantified), e.g., `role ∈ Roles(context)`, rather than as “X MUST …”.
* If the constraint needs to be enforceable as part of a pattern’s contract, authors **SHOULD** reference the predicate identifier from the Conformance Checklist (and/or call out validator behaviour), rather than duplicating the predicate with RFC keywords.

**H‑9 (Footer marker sentinel).** Footer marker **SHALL** be a single heading line whose `FullId` is the pattern ID followed by the reserved sentinel token `:End` (no ordinals, no title, no square‑bracket tags): 
`### <PatternId>:End`
It is the only allowed heading *inside* a pattern whose section token is non‑numeric. It **MUST** be the final line of the pattern and **MUST NOT** carry any prose. Tooling and readers **MUST** treat it as a boundary sentinel, not as a semantic section.

*Unification note:* historic A‑ and D‑templates differed only by the presence/absence of **Bias‑Annotation** and **Relations**; the unified template keeps the headings everywhere while allowing explicit `Not applicable` statements when justified.
The Alexandrian pattern canon historically calls *Problem frame* “Context”. FPF avoids that label because **Context** is already overloaded in FPF (e.g., `U.BoundedContext` and its Plain‑register label).

#### E.8:4.2 - Stylistic Principles (S‑0 … S‑13)

| # | Principle | Guideline |
|---|-----------|-----------|
| S‑0 | Narrative Flow Seven‑Step Heuristic | Authors are encouraged to structure major paragraphs or subsections using the seven‑step mnemonic. |
| S‑1 | Density without Jargon | Short declarative sentences; tool names belong in Pedagogy/Tooling. |
| S‑2 | Internal Cohesion | Inline references to Pillars and related patterns. |
| S‑3 | Embedded Mini‑Definitions | Gloss a new term in parentheses on first appearance. |
| S‑4 | Contextualisation | Brief historical or disciplinary lineage anchors. |
| S‑5 | Prophylactic Clarification | Pre‑empt common misreadings inside the prose. |
| S‑6 | Quotable Closers | Finish Solution or Consequences with a memorable aphorism. |
| S‑7 | Generative over Prescriptive | Present rules as enabling constraints, not bureaucracy. |
| S‑8 | Trans‑disciplinary Tie‑ins | Illustrate using at least two distinct fields. |
| S‑9 | Physical Grounding Reference | Link abstractions to a `Transformer` or physical process. |
| S‑10 | Punchy Blocks | ≤ 5 sentences per paragraph; lists for clarity. |
| S‑11 | Narrative Flow | Ensure sections read as a continuous story, not bullet soup. |
| S‑12 | Full sentences over tags | Avoid “keyword soup”. Each list item SHOULD contain a subject and a verb; prefer 2–4 sentence micro‑paragraphs to bare tag lists. |
| S‑13 | SoTA‑Echo craft | In the SoTA‑Echoing section, present: **claim → practice → source → alignment → adoption status (adopt/adapt/reject)**; cite Bridges & CL when crossing Contexts/planes. |

Authors use the principles as a *scaffold*, not a straitjacket: the goal
is coherent, engaging insight.

**S‑0 (Narrative Flow Seven‑Step Heuristic) — explanation**
Narrative flow is recommended to follow these steps: **Hook → Frame → Weave → Anchor → Bridge → Flow → Close**.

Brief explanations: 
| Step       | Purpose in a paragraph/section                             |
| ---------- | ---------------------------------------------------------- |
| **Hook**   | Grab attention with a vivid image or paradox.              |
| **Frame**  | State the specific question or problem space.              |
| **Weave**  | Connect to earlier patterns or Pillars.                    |
| **Anchor** | Tie to a concrete System/Episteme or physical process.     |
| **Bridge** | Show the implication for the upcoming claim or rule.       |
| **Flow**   | Deliver the formal content or argument.                    |
| **Close**  | End with a quotable line or payoff that reinforces memory. |

Narrative Flow Heuristic also operationalises S‑1 (Density w/o Jargon), S‑2 (Internal Cohesion), S‑4 (Contextualisation), and S‑6 (Quotable Closers).

#### E.8:4.3 - Autonomy authoring stub (mandatory when autonomy is claimed)
If a pattern or example claims **autonomy** for any Role/Method/Service:
1) Add a subsection **“Autonomy (RoC‑E.16)”** that lists:
   * `AutonomyBudgetDeclRef` (id, version, Scope (G), Γ_time),
   * `Aut-Guard policy-id (PolicyIdRef)`,
   * `OverrideProtocolRef` (SpeechAct names, SoD),
   * pointer to where **Green‑Gate** applies in the Method steps,
   * where **AutonomyLedgerEntry** is recorded on `U.Work`.
2) Include one **Tell‑Show‑Show** vignette that demonstrates **depletion** and **override** handling.
3) Use **LEX‑BUNDLE** terms (Scope (G), Γ_time, Role/Method/Work). Avoid “validity”, “process”, “actor”, “system”, “mechanism” unless mapped to kernel types.

### E.8:5 - Archetypal Grounding (System / Episteme)

| Template element | `U.System` illustration | `U.Episteme` illustration |
|------------------|------------------------|---------------------------|
| Section order | Pump‑assembly pattern follows sections **1–12** (and, optionally, **13**). | Meta‑analysis pattern follows the same sections. |
| S‑1 Density w/o Jargon | “The pump boundary is the sealing plane.” | “This episteme raises **F (Formality)** by making falsifiers testable.” |
| Hook‑Weave‑Anchor | Opens with field anecdote → weaves in Γ‑core → anchors to motor torque. | Opens with historical paradox → weaves in **A.10** anchors → anchors to peer‑review data. |

*Note:* Prefer examples that reuse FPF’s own characteristics vocabulary (e.g., **F (Formality)** rather than “F‑score”) unless you explicitly mean an external metric and name it as such.

### E.8:6 - Bias‑Annotation
Lenses tested: **Gov**, **Arch**, **Onto/Epist**, **Prag**, **Did**. Scope: **Universal** for the authoring conventions in this pattern.
This guidance biases toward **Did** (readability, narrative flow) and **Arch** (template regularity) by design; the mitigation is explicit optionality (`Not applicable`) and the requirement to justify omissions in‑text.

### E.8:7 - Conformance Checklist

**CC style (canonical).**
Conformance Checklist items are obligations/conditions in the **authoring plane**: they constrain artefacts that claim conformance (and the reviewers/validators that accept them). A CC clause of the form “X SHALL …” is to be read as “In a conforming artefact, X SHALL …”, not as a deontic statement about the modeled world.

**Preferred wording for new or edited CC items:** start with an explicit conformance subject (e.g., “Authors …”, “Reviewers …”, “A conforming implementation …”, “A validator …”). If a CC item is enforcing an admissibility predicate, it **SHOULD** cite the predicate’s identifier (from a `Definition:` / `Invariant:` / `Well‑formedness constraint:` block) rather than restating the predicate as “X MUST …”. For boundary/interface/protocol/contract patterns, prefer A.6.B‑routed claim IDs (L/A/D/E) or cite an existing Claim Register (A.6.B:7) instead of restating mixed prose.

| ID | Requirement | Purpose |
|----|-------------|---------|
| **CC‑SG.0 (Heading discipline).** | Pattern and subsection headings **SHALL** follow **H‑1 … H‑9** (FullId prefix, reserved punctuation, heading levels, ellipsis discipline). The Footer marker **SHALL** follow **H‑9**. | Makes chunks self‑contained; reduces ambiguity between author elision and retrieval truncation. |
| **CC‑SG.1** | Every new pattern **SHALL** follow the section order defined in the Canonical Template (Title block → … → Footer marker). | Guarantees structural comparability. |
| **CC‑SG.2 (Grounding required).** | Every pattern **MUST** include an *Archetypal Grounding* section. If **System** or **Episteme** grounding is inapplicable, authors **MUST** state `Not applicable` and give a one‑paragraph justification. | Keeps patterns teachable and reduces “definition‑only” ambiguity. |
| **CC‑SG.3** | The *Bias‑Annotation* section **SHALL** cite the five Principle‑Taxonomy lenses and declare either “Universal” or an explicit scope limitation. | Keeps cross‑disciplinary neutrality explicit (ties to Guard‑Rail 4). |
| **CC‑SG.4** | Deontic normative sentences **MUST** use only RFC‑style keywords (see **H‑8**); RFC keywords **MUST NOT** appear inside `Definition:`/`Invariant:`/`Well‑formedness constraint:` blocks. When enforceable, admissibility/validity predicates **SHOULD** be referenced by id from the Conformance Checklist (rather than duplicated as “X MUST …”). Informal deontic verbs are prohibited in normative clauses. | Prevents ambiguity between obligation language and model validity; improves auditability. |
| **CC‑SG.5** | Pattern prose **SHOULD** demonstrate adherence to Style Principles **S‑0 … S‑13**; reviewers are empowered to request revision when clarity or didactic quality suffers. | Embeds common narrative voice without rigid policing. |
| **CC‑SG.6 (SoTA‑Echo required).** | Every pattern **SHALL** include a **SoTA‑Echoing** section and clearly state divergence of its Solution from SoTA with explanation of why. Architectural patterns **SHALL** satisfy the full obligations below; Definitional patterns **MAY** satisfy the reduced obligations (terminology drift + ≥ 1 post‑2015 primary source) when a full SoTA comparison is not meaningful. | Ensures explicit lineage and guards against vocabulary drift. |
| **CC‑SG.7 (Post‑2015, multi‑Tradition).** | For Architectural patterns, SoTA‑Echoing **SHALL** cite ≥ 3 post‑2015 sources across ≥ 2 Traditions; each item **MUST** carry adoption status (adopt/adapt/reject) with reason. | Guards against monoculture; makes intent explicit. |
| **CC‑SG.8 (Bridge & CL on reuse).** | Any cross‑Context or plane reuse mentioned in SoTA‑Echoing **MUST** cite **Bridge id + CL** and (if planes differ) **Φ(CL)**/**Φ_plane** policy‑ids; penalties **→ R_eff** only. | Safe, auditable reuse. |
| **CC‑SG.9 (Lexical hygiene).** | The term **mapping** **SHALL NOT** appear in SoTA‑Echoing except in the precise E.10 sense; use **alignment/Bridge/relation** instead. | Avoids overloading reserved vocabulary. |
| **CC‑SG.10 (No keyword soup).** | SoTA‑Echoing items **MUST** be written as sentences (not bare noun phrases); bullet lists are acceptable only with complete clauses. | Improves didactic quality and comparability. |
| **CC‑SG.11 (Anti‑patterns).** | Every pattern **SHALL** include a **Common Anti‑Patterns and How to Avoid Them** section. It **MAY** be `Not applicable` only with a one‑paragraph justification. | Makes misuse paths explicit and reduces review churn. |
| **CC‑SG.12 (Boundary routing).** | If a pattern’s subject is a boundary/interface/protocol/contract (API boundary, protocol, connector, “contract” description, or a published boundary surface), it **MUST** either (a) provide an **A.6.B**‑routed atomic claim set (`L-*`/`A-*`/`D-*`/`E-*`, with stable IDs), or (b) explicitly cite an existing **A.6.B Claim Register** / routed claim set that it reuses. | Pulls A.6.B into the authoring contour; prevents “contract soup” and makes review lintable. |

### E.8:8 - Common Anti‑Patterns and How to Avoid Them

These failure modes recur in drafts and in downstream application. They are predictable ways the Forces in this pattern get violated.

| Anti‑pattern | Symptom | Why it fails (force violated) | How to avoid / repair |
|-------------|---------|------------------------------|-----------------------|
| **Template cargo‑culting** | Headings exist, but each section is a thin bullet list with no narrative. | Satisfies Uniformity but loses Readability and Didactic Primacy. | Use S‑0 narrative flow per section; write 2–4 sentence micro‑paragraphs before any list/table. |
| **Un‑grounded abstractions** | Problem/Solution stay abstract; no concrete System/Episteme Tell–Show–Show. | Breaks teachability and makes misuse likely. | Fill Archetypal Grounding first; then back‑propagate concrete nouns into Problem/Forces/Solution. |
| **SoTA name‑dropping** | SoTA‑Echoing is a list of nouns/buzzwords with no adopt/adapt/reject rationale. | Violates CC‑SG.7 and CC‑SG.10; readers cannot audit alignment. | For each source, state what is adopted/adapted/rejected and why (complete clauses, 2–4 sentences). |
| **Tool‑bound normativity** | A vendor tool, file format, or schema is described as required to apply the pattern. Data governance implied. | Violates Guard‑Rails (lexical firewall; notation independence, data governance absence); reduces portability and conceptual clarity. | Keep normative content conceptual; move tooling and data governance into Context‑local Profiles. |
| **Hidden trade‑offs** | Solution sounds universally good; Consequences lists only benefits. | Removes decision‑support value; applicability cannot be judged. | In Consequences, include at least one trade‑off and a mitigation; if none exists, explain why. |

### E.8:9 - Consequences

| Benefits | Trade‑offs / Mitigations |
|----------|-------------------------|
| **Predictable skeleton** – readers instantly know where to find context, forces, and criteria. | Limits author freedom in macro layout; mitigated by flexibility inside the Solution subsection. |
| **Cohesive voice** – S‑principles give FPF a recognisable style, aiding memorability. | Reviewers must read for style, not only semantics; checklists ease load. |
| **Embedded pedagogy** – Tell‑Show‑Show and Hook → Close heuristics turn the spec into a self‑teaching text. | Slightly longer patterns; justified by better comprehension and fewer clarifying DRRs. |

### E.8:10 - Rationale
Structure and style function as FPF’s *grammar*. By unifying what were
once separate “template” and “style guide” patterns, authors face a
single reference point that satisfies:

* **P‑1 Cognitive Elegance** – uniform, minimal surprises.  
* **P‑2 Didactic Primacy** – narrative flow, dual archetype examples.  
* Guard‑Rails 1 & 2 – no tool jargon, no notation lock‑in inside prose.

A unified template also improves retrieval: a chunk containing `A.2:<n> - Bias‑Annotation` remains self‑identifying even when parent headings are missing, and the recommended footer marker makes truncation detectable.

International and industry standards often speak in terms of *conformance criteria*. FPF uses the label **Conformance Checklist** to make adoption easier for engineers and managers.

### E.8:11 - SoTA‑Echoing  *(normative; lineage & deltas to contemporary State‑of‑the‑Art)*

**Purpose.** Make each pattern’s relationship to contemporary practice explicit and comparable without importing tooling or data governance. This section is prose‑first and notation‑independent.

**Minimum contents (obligations).**
1) **Evidence binding (no duplicate SoTA).** If a **SoTA Synthesis Pack** exists (G.2), this section **SHALL cite** its **ClaimSheet IDs** / **CorpusLedger entries** / **BridgeMatrix rows** as the source‑of‑truth for claims and report `adopt/adapt/reject` **consistent with those IDs**. Avoid forking an untracked SoTA narrative.
2) **Sources (post‑2015).** For **Architectural patterns**, cite ≥ 3 primary SoTA sources (standards/papers/books), with at least **two independent Traditions**. For **Definitional patterns**, cite ≥ 1 post‑2015 primary source and, where relevant, a short note on terminology drift/deprecations.
3) **Practice alignment.** For each cited item, state **what is adopted/adapted/rejected** and **why** (2–4 sentences).
4) **Scale legality.** If numeric operations are implied, bind to ComparatorSet/CG‑Spec and declare partial‑order stance (no hidden scalarisation).
5) **Cross‑Context reuse.** Any reuse across `U.BoundedContext` must surface Bridge+CL/Φ_plane policy‑ids (penalties affect only `R_eff`).
6) **Lexical hygiene.** Avoid “mapping” unless you mean an explicit Bridge/translation relation with loss notes.

**Writing guidance (readability).**
*Write short paragraphs, not tag lists.* For each Tradition, provide (a) a one‑sentence capsule of the practice, (b) a one‑sentence comparison to the pattern’s Solution, (c) a one‑sentence adoption status with reason. Where helpful, add one **System** and one **Episteme** micro‑example (Tell–Show–Show).

**Format: human‑first.** A small table is allowed, but each row **MUST** be accompanied by 1–2 sentences as above. Vendor/tool tokens, file formats, or data schemas are out of scope.

#### E.8:11.1 - SoTA alignment for this pattern (E.8 self‑echo)

| Claim (E.8 need) | SoTA practice (post‑2015) | Primary source (post‑2015) | Alignment with E.8 | Adoption status |
|---|---|---|---|---|
| Pattern texts must be teachable, not just “correct”. | Use a stable skeleton (context/problem/forces/solution/actions/consequences) plus illustration and checklists to keep patterns readable and actionable. | Iba (2021), “How to Write Patterns …” (PLoP 2021 PLoPourri). | Canonical Template mirrors the skeleton and adds Archetypal Grounding + Conformance Checklist as first‑class sections. | **Adopt/Adapt.** Adopt the skeleton; adapt by making bias and conformance explicit sections. |
| Pattern quality needs explicit validation beyond folklore. | Critique of ad‑hoc validation (incl. “rule of three”) and push toward more rigorous discovery/validation methods. | Riehle et al. (2020), “Pattern Discovery and Validation Using Scientific Research Methods”. | E.8 encodes validation as Conformance Checklist + SoTA‑Echoing with adoption status and evidence binding. | **Adopt.** Adopt auditability goals; keep the mechanism lightweight (checklists + evidence binding). |
| Governance should constrain structure, not mandate tools. | Specify conformance and structure; do not prescribe processes, notations, tools, or recording media. | ISO/IEC/IEEE 42010:2022 (architecture description). | E.8 is template‑ and conformance‑centric, with guard‑rails against tool/notation lock‑in in core narrative. | **Adopt.** Direct alignment. |
| Pattern languages are networks; visuals often mislead. | Systematic surveys report low consensus on what to visualise and ambiguous/inexpressive visuals; relations need clear definition in text. | Quirino, Barcellos, Falbo (2018), survey of visual notations for software pattern languages (SBES 2018). | E.8 requires a Relations section and keeps diagrams optional, placing primacy on textual structure and explicit links. | **Adapt.** Use the finding as rationale for text‑first, relation‑explicit authoring. |

### E.8:12 - Relations

* **Builds on:** E.6, E.7  
* **Constrained by:** Guard‑Rails E.5.1–E.5.4 (lexical firewall, notation independence, etc.)  
* **Constrains:** All patterns; the DRR template references the same section order.  

### E.8:End

## E.9 - Design‑Rationale Record (DRR) Method

### E.9:1 - Problem frame
FPF is engineered for Pillar **P‑10 Open‑Ended Evolution**: its normative
rules must adapt as new calculi and insights arrive. But change without a
record of *why* leads to conceptual erosion and undermines auditability.
Hence FPF requires an explicit **Design‑Rationale Record (DRR)**—a
durable *conceptual artefact* that precedes every normative change.

### E.9:2 - Problem
Direct edits to the Core, absent a structured rationale, trigger three
systemic hazards:

1. **Lost provenance** – future authors cannot infer the reasoning behind
   a rule; intent decays.  
2. **Implicit assumptions** – discarded alternatives vanish from memory,
   so debates resurface and churn repeats.  
3. **Conceptual drift** – incremental tweaks slip past the Eleven Pillars
   and Principle Taxonomy lenses, blurring the framework’s foundations.

### E.9:3 - Forces

| Force | Tension |
|-------|---------|
| **Agility vs Rigour** | Evolve swiftly ↔ demonstrate deliberate, Pillar‑aligned decisions. |
| **Transparency vs Efficiency** | Provide a public argument trail ↔ avoid bureaucratic drag on minor edits. |
| **Clarity vs Conciseness** | Capture full reasoning ↔ prevent meta‑text from bloating the Core itself. |

### E.9:4 - Solution — the DRR as a structured argument
Any proposal to add, modify or deprecate a `NORM`, `A`, `D`, or `GOV`
rule **MUST** be accompanied by a **Design‑Rationale Record**. By default,
it contains exactly four conceptual components (below); a lightweight
editorial variant is permitted by CC‑DRR.5.

| Component | Guiding question | Typical content |
|-----------|------------------|-----------------|
| **Problem frame** | *Why are we talking about this?* | Problem statement, triggering insight, or external change. |
| **Decision** | *What will we do?* | Precise normative text to enter the specification. |
| **Rationale** | *Why is this the right thing?* | Comparison of alternatives, Pillar check, taxonomy‑lens balance. |
| **Consequences** | *What happens next?* | Expected benefits, trade‑offs, impacted patterns, risk notes. |

The DRR lives **outside** the normative Core. Upon acceptance, its
*Decision* **SHALL** be applied to the relevant pattern(s) as explicit
normative text (the change is "in the Core"; the DRR is not).

To preserve **P‑2 Didactic Primacy** without duplicating meta‑text,
stable and reusable parts of the DRR’s *Rationale* and *Consequences*
**SHOULD** be **distilled** into the **informative** sections of the
affected pattern(s) (Rationale, Consequences, SoTA‑Echoing, Archetypal
Grounding; per the Pattern Template, E 8). The full DRR remains
external as provenance.

### E.9:5 - Archetypal Grounding (System / Episteme)

| Holon flavour | DRR analogue | Four components illustrated |
|---------------|--------------|-----------------------------|
| **`U.System`** (physical) | Engineering Change Order for pump motor upgrade. | Context: inefficiency; Decision: switch to brushless DC; Rationale: energy gain vs cost; Consequences: new control schema + supplier change. |
| **`U.Episteme`** (knowledge) | Foundational theory revision paper. | Context: conflicting data; Decision: introduce new axiom; Rationale: explains legacy & new data, Pillar alignment; Consequences: fresh predictions, update to curricula. |

### E.9:6 - Conformance Checklist

| ID | Requirement | Purpose |
|----|-------------|---------|
| **CC‑DRR.1** | Any **semantic** change (Δ‑2/Δ‑3) to a `NORM`, `A`, `D`, or `GOV` pattern **SHALL** be preceded by an accepted DRR containing Problem‑frame (Context), Decision, Rationale, Consequences. | Prevents undocumented semantic edits. |
| **CC‑DRR.1a** | When the proposed change is expressed as a (new or revised) pattern written in the standard template (E 8), the DRR **MAY** satisfy its four components by **pointing to** the corresponding pattern sections, rather than duplicating prose. | Avoids “double writing” while keeping the argument recoverable. |
| **CC‑DRR.2** | The *Rationale* element **MUST** assess the proposal against **all Eleven Pillars** and the five Principle‑Taxonomy lenses (`Gov`, `Arch`, `Onto/Epist`, `Prag`, `Did`). | Keeps evolution aligned and cross‑disciplinary. |
| **CC‑DRR.3** | The DRR **SHALL** list every pattern it supersedes, amends, or risks impacting. | Maintains explicit impact graph. |
| **CC‑DRR.4** | Once approved, the *Decision* text **SHALL** be inserted into the Core as the normative change. Other DRR sections **MAY** be distilled into **informative** pattern sections (Rationale/Consequences/SoTA‑Echoing/Grounding) but **SHALL NOT** introduce new normative constraints except via explicit `NORM`/`A`/`D`/`GOV` text. | Preserves brevity while keeping the Core teachable. |
| **CC‑DRR.5** | Minor, non‑substantive edits (Δ‑0/Δ‑1; e.g., typos, wording clarity, didactic rearrangements) **MAY** follow a lightweight DRR variant containing Problem‑frame (Context) + Decision only (“no semantic change”), provided they do not alter semantics. | Avoids bureaucratic drag on editorial work. |
| **CC‑DRR.6 (LAT pointer)** | For Δ‑2/Δ‑3 changes to part F or part G patterns, the DRR **SHALL** include a non‑normative pointer (id/URI) to a published LEX‑AUTH Trace (LAT) archived as `U.Work`; the LAT is evidence, not normative prose. | Binds high‑impact changes to re‑runnable authoring evidence without importing tooling. |

### E.9:7 - Consequences

| Benefits | Trade‑offs / Mitigations |
|----------|-------------------------|
| **Complete audit trail** – every semantic normative change carries a structured “why”. | Adds deliberate friction; mitigated by CC‑DRR.5 (Δ‑0/Δ‑1 lightweight) and CC‑DRR.1a (pointer‑based DRRs). |
| **Higher decision quality** – Pillar & lens check surfaces hidden conflicts early. | Authors must learn taxonomy; template checklist shortens ramp‑up. |
| **Institutional memory** – prevents re‑litigation of rejected alternatives. | DRR archive grows; index stored in a non‑normative annex. |

### E.9:8 - Rationale
FPF evolves by **explicit, reviewable deltas** rather than silent edits.
The DRR is the *minimal structured argument* that keeps **P‑10
Open‑Ended Evolution** compatible with **P‑1 Cognitive Elegance** and
**P‑2 Didactic Primacy**: the Core stays succinct and teachable, while
the “why” is recoverable. Pointer‑based DRRs (CC‑DRR.1a) prevent
duplicated prose, and distillation into informative pattern sections
(CC‑DRR.4) keeps the spec itself learnable.

### E.9:9 - Relations

* **Instantiates:** P‑10 Open‑Ended Evolution, P‑2 Didactic Primacy  
* **Template governed by:** `pat:authoring/pattern‑template` (E 8)  
* **Interacts with:** `pat:guard/bias‑audit` (E 5.4) via lens check  
* **Complemented by:** `pat:authoring/code‑of‑conduct` (E 12) – etiquette for DRR debate  

### E.9:End

## E.10 - Unified Lexical Rules for FPF (LEX‑BUNDLE)
*Definitional pattern; normative for all FPF pattern text and for any Context that claims FPF conformance.*

**Status & placement.** Part E.10 (“Lexical Discipline & Stratification”); complements **E.10.D1 (D.CTX)**, **E.10.D2 (I/D/S)**, and the **DesignRunTag / CtxState boundary discipline** (**A.15**; **E.18**), and is referenced by F‑cluster naming practices (F.4–F.8). This bundle consolidates all lexical constraints in one place so authors can cite **“LEX‑BUNDLE”** instead of listing rules scattered across documents.

**Builds on:** A.7 **Strict Distinction (Clarity Lattice)**; E.5 Guard‑Rails (DevOps Lexical Firewall; Notational Independence; Unidirectional Dependency); F.5 **Naming Discipline for U.Types & Roles**.
**Coordinates with.** A.2/A.15 (Role–Method–Work alignment), A.10 (Evidence Graph Referring), B.1/B.3 (Γ‑algebras & assurance), F‑cluster (context of meaning; Bridges).


### E.10:1 - Problem context

**Intent.** Provide one **normative** rule‑set that makes FPF language **unambiguous, composable across contexts, and teachable** by design. Authors, reviewers, and tooling can point to **LEX‑BUNDLE** as the single source of truth for:

* **Vertical stratification** (Kernel ↔ Extensions ↔ Context ↔ Instance);
* **Twin registers** (Tech/Plain) with safe synonyms;
* **Naming morphology** (allowed suffixes & style) for the kernel’s core objects;
* **Minimal Generality** tests (names are neither parochial nor vacuous);
* **Canonical rewrites** for overloaded words (e.g., *process*, *function*, *service*);
* **Conformance checks** (lintable) and minimal examples.

**Scope.** Applies to:
(a) **Core** (Parts A–G), (b) **Extensions patterns specs** (CAL/LOG/CHR), (c) **Context glossaries** that claim FPF conformity, and (d) **Diagrams/prose** in normative text. It **does not** constrain Tooling or Pedagogy wording other than where they quote Core semantics.


### E.10.2 - Problem

1. **Polysemy drift.** *Process, function, service, agent, activity* slide between structure, recipe, execution, and promise.
2. **Cross‑context collision.** A label (e.g., *Owner*) is assumed “global” though meanings differ per `U.BoundedContext`.
3. **Name bloat vs. parochialism.** Either hyper‑specific domain names leak into core types, or vague umbrella names obscure invariants.
4. **I/D/S collapse.** Authors mix **intension** (the thing), **description** (how we describe it), and **specification** (testable criteria).
5. **Register soup.** Tech terms bleed into Plain pedagogy and vice‑versa, inviting category errors.


### E.10:3 - Forces

| Force                          | Tension to resolve                                                                         |
| ------------------------------ | ------------------------------------------------------------------------------------------ |
| **Universality vs. local fit** | Kernel must stay universal while allowing domain nuance in a Context of meaning.              |
| **Brevity vs. clarity**        | Short names help, but only if morphology signals the right kernel slot.                    |
| **Stability vs. evolution**    | Names should survive refactors; yet we must accommodate new roles/types without explosion. |
| **Pedagogy vs. precision**     | Plain words aid learners; Tech labels anchor formal checks.                                |


### E.10:4 - Solution — the **LEX‑BUNDLE** rule‑set (overview)

**LEX‑BUNDLE** aka **ULR (Unified Lexical Rules)** is a compact set of **register, naming, and rewrite** rules with conformance checks.

1. **Vertical Stratification Ladder** (E.10 → four strata);
2. **Twin‑Register Discipline** (Tech/Plain pairs);
3. **Minimal Generality (MG)** principle + tests;
4. **Morphology & Style** (suffixes, casing, reserved prefixes);
5. **Canonical Rewrites** for overloaded words (L‑rules);
6. **Conformance Checklist (CC‑LEX)** and **Regression Stubs (RSCR‑LEX)**.

Below are the **normative clauses** 

### E.10:5 - Vertical Stratification Ladder (four strata; no cross‑bleed)

> **Rule V‑0 (Strata).** Every lexical item in a conformant text belongs to exactly one **stratum**:

1. **Kernel** — `U.*` types, kernel relations, invariants (e.g., `U.Holon`, `U.Role`, `U.Method`, `U.Work`, `U.PromiseContent`).
2. **Extension patterns** — CAL/LOG/CHR exports (e.g., **Sys‑CAL**, **KD‑CAL**, **Agency‑CHR**) that **extend** but do not override Kernel.
3. **Context** — a **`U.BoundedContext`** with its **Glossary, Invariants, Roles**, and **Bridges** (local Context of meaning).
4. **Instance** — concrete identifiers (holders, role assignments, works, carriers).

**V‑1 (Unidirectional meaning).** Meaning **flows downward** only: Kernel → Extention patterns → Context → Instance. No stratum may redefine a higher stratum’s term; it may only **specialise** or **bridge** it.

**V‑2 (Strata vs authoring stances).** The four lexical strata above constrain **tokens**. They are independent of an artefact’s **stance** (its `CtxState` pins such as `DesignRunTag`, `ReferencePlane`, and `Locus`). Strata answer “what words mean here”; stance answers “where this claim lives in the flow” and which evidence‑lane expectations apply.

**V‑3 (Citation style).** When a Context term is used, its **Context** must be visible at first mention (e.g., `OwnerRole:ITIL_2020`). If an author needs Cross‑context reuse, they **MUST** cite a **Bridge** with a stated **Congruence Level (CL)** (see F.9).

**V‑4 (Firewall).** Tooling/Pedagogy idioms shall not leak into Kernel prose (DevOps Lexical Firewall). CI/CD jargon, file formats, or API names **MUST NOT** appear in Core definitions. (Pedagogy may use them **as examples** only, in the **Plain** register, with Tech anchors present.)

### E.10:6 - Ontology Guards

#### E.10:6.1 - Tech register ontology guards

> **Purpose.** This section stabilises the Tech register of the kernel lexicon by enforcing head‑anchored naming, explicit *object‑of‑talk*, I/D/S morphology, disciplined treatment of **Role / Holder**, and Domain usage consistent with **D.CTX** and **UTS**. It aligns with **F.4 Role Description (RCS/RSG)**, **F.11 Method Quartet Harmonisation**, and **F.17 UTS**. **Scope:** Guidance is **register‑agnostic** and applies to the whole FPF; examples are illustrative and MUST pass Minimal Generality & Domain Anchoring (MG-DA) and other rules of lexical governance pattern E*. This guidance applies to kernel and non‑kernel components (including Part G and patterns in Part C) and SHOULD be reused across extensions.
> 
**Onto1 — Head‑anchoring**  *(use Kernel heads + pass LEX.TokenClass / I/D/S gates)*
* **Rule:** The **head noun of a term MUST explicitly signal the kind** (`System`, `Holon`, `Role`, `Work`, `Episteme`, `Tradition`, `Lineage`, `Characteristic`, `Method`, `Profile`, `Description`, `Spec`, `Flow`, `Card`, `Pack`, `Dashboard`, …).
* **Figurative heads** with obvious overload (“Tradition”, “family”, “process”, “function”) are **forbidden in the kernel**. Use **plain twins** only with a 1:1 Tech mapping and declare **`LEX.TokenClass`** for the Tech token. They **MAY** appear **only in the Plain register** as 1:1 twin‑mappings to a Tech token, but **MUST NOT** appear in the Tech register. Plain language should minimise lexical error from overloaded terms; use plain‑twin lexical guards.
  * **Do:** `IncidentDashboard`, `MethodSpec`, `TraditionProfile`, `FlowDescription`.
  * **Don’t:** `IncidentBoard`, `TDD Tradition`, `Production Process` (kernel), `Service Function` (kernel).

 **Onto2 — I/D/S on the surface (Intension/Description/Specification morphology)**  *(ref. E.10.D2)*
* **Rule:** Any **intensional** object is a bare head: `Method`, `Tradition`, `Characteristic`. Any **description** appends **`…Description`**: `MethodDescription`, `TraditionDescription`. Any **testable specification** appends **`…Spec`** and presupposes acceptance criteria and harnesses (normative in **E.10.D2**). E.g., *Algorithm* is a species of `MethodDescription` for a computer (a system in the role of information transformer); **If** expressed in a formal language **and** bundled with acceptance tests, it is **`MethodSpec`** (per **F.11**). **If** expressed as pseudo‑code, it is **`MethodDescription`**.
* **Extension:** Apply the same pattern to non‑method objects where appropriate: `FlowDescription`/`FlowSpec`, `SystemDescription`/`SystemSpec`.
* **Do:** `SamplingMethod` - `SamplingMethodDescription` - `SamplingMethodSpec`.
* **Don’t:** `SamplingAlgorithm` (when it is just prose), `SamplingProcessSpec` (head not signalling kind).

**Onto3 — Roles, Holders, and Carriers (holonic)**  *(ref. F.4 / F.5)*
* **Rule:** The playable intention is named **`…Role`** and described through **F.4 Role Description** (RCS/RSG), e.g., `SafetyOfficerRole`, `ReviewerRole`. The party **assuming a role** is the **Holder**. Use the **`Holder#Role:Context`** pattern to type the assumption (where `Context` is a `U.BoundedContext`), e.g., `Team‑Alpha (U.Holon) is Holder#SafetyOfficerRole:Plant‑Ops`. **Carrier** is **reserved for a system that bears a symbol of episteme** (`U.Episteme`, `Tradition`, `Lineage`, `Profile`, repertoire) **independent of any concrete role assumption**, e.g., `LeanTraditionCarrier`, `CalibrationLineageCarrier`. Avoid **`Artefact`** as a head in the kernel: it is ambiguous between a Carrier (e.g., document), a system “made by” some transformer, or an episteme abstracted from its carrier.
* **Register note:** Job titles (`Reviewer`, `Owner`, `Lead`) belong in the **Plain** register and MUST twin‑map to explicit Tech `…Role` tokens.
* **Why:** This resolves the inconsistent “role carrier vs role holder” usage: **use “Holder” for holonic role assumption**, keep **“Carrier”** for the *system that bears a symbol of episteme*. 
* **Migration note.** Legacy `…CarrierRole` **MUST be rewritten** to `Holder#…Role:Context`. Use SCR‑LEX to enforce the rewrite.
* **Do:** `ReviewerRole` (or `AssessorRole`), `Holder#ReviewerRole:Journal‑Issue‑42` (or `Holder#AssessorRole:Procurement‑Lot‑42`); `LeanTraditionCarrier (U.Holon)`, independent of any particular role.
**Don’t:** `Reviewer` (as a kernel type), `ReviewerCarrier` (to mean a role holder), `SystemReviewer` (role collapsed into a type).

**Onto4 — Domain only as a catalog mark**  *(ref. E.10.D1 D.CTX; publish stitching on UTS)*
* **Rule:** `Domain` is **not a kernel kind** and carries **no semantics, inheritance, or reasoning rights**. It is a **catalog mark** that groups several `U.BoundedContext` entries.
* **Required stitching (see D.CTX & UTS).** Any use of `Domain` **MUST** present: 1. the enumerated list of `ContextId` in **D.CTX**, and 2. the corresponding **UTS strings** (F.17) with twin labels.
* **“Discipline ≠ Domain.”** _Domain_ labels are **catalog‑only (D.CTX + UTS)**; **Discipline** is a **CG‑Spec‑governed holon** (`U.Discipline`). Cross‑use requires **Bridge (F.9) + CL**; **LexicalCheck** MUST fail texts that equate Domain with Discipline.
* **Governance.** **No “Domain … governance”.** Rules of comparability/aggregation belong to **Discipline/CG‑Spec** (ComparatorSet, ScaleComplianceProfile (SCP), MinimalEvidence, Γ‑fold, CL‑routing), *not* to `Domain`. Prefer `DomainFamily` + stitching over inventing new “Domain” types.
* **Do:** `DomainBundle: ClinicalSafety → {ContextId: AdverseEvents, DeviceLabelling, …} + UTS twins`.
* **Don’t:** `ClinicalSafetyDomain` as a type with inheritance; `Domain Governance` sections in Tech.

**Onto5 — Always state the **object‑of‑talk**
* **Rule.** The definition or first line of a gloss **MUST state what the term is about**: a `U.Holon`/`U.System`, a `U.Episteme` (`Tradition`, `Lineage`, `Profile`), a `Role`, a `Work` execution, a `Characteristic`, or a `Carrier`.
* **Do:** “**Object‑of‑talk:** `ReviewerRole` — a role intention playable by a holon within an editorial context.”
* **Don’t:** “Reviewer — a person who …” (blurs kind and object‑of‑talk).

**Onto6 — Bans and canonical rewrites**  *(mirror E.10 § 9 L‑rules; do not duplicate tables)*
* `process / function / activity` → **`Work` / `MethodDescription` / `Flow`** (context‑dependent).
* `Tradition` → **`Tradition`** (Tech); leave “Tradition” only as a Plain twin with an adjacent Tech label.
* `domain` → **`DomainFamily` + {ContextId list} + UTS twins**.
* legacy `…CarrierRole` → **`Holder#…Role:Context`**.
* ambiguous `Owner` in role names → prefer **`StewardRole` / `CustodianRole` / explicit responsibility head**.
* job titles (`owner`, `lead`, `champion`) in the kernel → **use explicit `…Role` names**; keep titles in Plain with twin‑labels.
* **Do:** `FlowDescription: ReturnsHandling`, `Tradition: Test‑Driven`, `Holder#CustodianRole:Asset‑Ledger`.
* **Don’t:** `Returns Process`, `TDD Tradition` (kernel), `Ledger Owner` (underspecified).

**Worked mini‑examples across arenas**
1. **Software engineering:** `BuildFlowDescription`, `CIHarnessSpec`; `Holder#MaintainerRole:Repo‑X`. Avoid `Build Process`, `Repo Owner`.
2. **Applied research / experimentation:** `SamplingMethodSpec`, `CalibrationLineageCarrier`; `Holder#ReviewerRole:Grant‑Call‑Y`.  Avoid `Sampling Algorithm` (if prose), `Lab Owner`.
3. **Production / service management:** `ShiftWork`, `SafetyOfficerRole`; `Holder#SafetyOfficerRole:Plant‑Ops`.  Avoid `Safety Officer` as a type, `SafetyDomain Governance`.
4. **Operations research / optimisation:**  `RoutingMethodDescription`, `CostCharacteristic`; `Holder#ModelStewardRole:OR‑Program`.  Avoid `Routing Function`, `Model Owner`.
5. **Healthcare / clinical ops:** `CarePathwayFlowDescription`, `MedicationAdministrationWork`; `Holder#AttendingPhysicianRole:Ward‑12`. Avoid `Care Process`, `Ward Owner`.
6. **Finance & accounting:** `ReconciliationMethodSpec`, `JournalPostingWork`; `Holder#TreasuryStewardRole:Liquidity‑Book`. Avoid `Reconciliation Process`, `Account Owner` (underspecified).
7. **Legal / compliance:** `RetentionPolicySpec`, `InvestigationWork`; `Holder#DataProtectionOfficerRole:Org‑X`. Avoid `Compliance Function`, `Data Owner` (underspecified).
8. **Cloud / IT operations:** `IncidentFlowDescription`, `RunbookMethodSpec`; `Holder#OnCallEngineerRole:Service‑Y`. Avoid `Incident Process`, `Service Owner` (underspecified).
9. **Logistics / supply chain:** `PickingWork`, `RoutingMethodSpec`; `Holder#DispatcherRole:Hub‑Z`. Avoid `Picking Process`, `Fleet Owner`.
10. **Construction / civil engineering:** `PermitAcquisitionFlowDescription`, `InspectionMethodSpec`; `Holder#SiteStewardRole:Project‑Lot‑17`. Avoid `Inspection Process`, `Site Owner`.
11. **Emergency response:** `TriageMethodDescription`, `EvacuationFlowDescription`; `Holder#IncidentCommanderRole:Event‑R`. Avoid `Triage Function`, `Incident Owner`.
12. **Agriculture:** `IrrigationFlowDescription`, `SoilSamplingMethodSpec`; `Holder#FieldStewardRole:Plot‑17`. Avoid `Irrigation Process`, `Field Owner`.

**Checklist before minting a KernelToken**
* Head noun signals kind (Onto1).
* I/D/S morphology correct (Onto2).
* If role‑related: **Role vs Holder vs Carrier** separation observed; holonic scope explicit (Onto3).
* Any Domain mention stitched to D.CTX and UTS; **no norms on Domain** (Onto4, Onto6).
* Object‑of‑talk declared (Onto5).
* SCR‑LEX rewrites checked / legacy forms migrated (Onto6).
> **Note on registers.** Keep figurative or business‑casual terms in the **Plain** register only, with strict **twin‑label** links to the Tech token (LEX‑BUNDLE). In the **Tech** register, speak in KL‑CAL: **episteme‑about‑epistemes** (Tradition, Lineage, Profile), not in catalogue‑admin idioms.

* **Onto‑Deon — Deontic lexicon guard (Core register)**  
**Rule.** In the Conceptual Core, avoid using **“Standard”** as the head noun of an *intensional object* name unless the object is an explicit **deontic speech-act** under the **Gov** lens (cf. E.3).

For interface/boundary invariants and public commitments of **things** (holons, interfaces, ports), prefer intensional names like **InterfaceContract**, **ComplianceProfile**, **AcceptanceSpec**, **InteropProfile**, etc.

Use the word **standard** for an **artefact** (Description/Specification) that is *intended to be complied with* (and that has explicit compliance checks).

If an intensional object is currently named `… Standard`, rename it to a proper intensional name, and (optionally) add a separate Description/Specification artefact that contains the standard text and the intended compliance checks.
 **Rewrite hints (Tech → Tech).**  
 `publication Standard` → `publication standard`;  
 `frame Standard` → `frame standard`;  
 `measurement Standard` → `measurement standard`;  
 `Method Interface Standard (MIC)` → `Method Interface Standard (MIS)` *(alias acceptable during transition)*;  
 `Boundary‑Inheritance Standard (BIC)` → `Boundary‑Inheritance Standard (BIS)` *(alias acceptable during transition)*.  
 **Rationale.** Keeps Core prose centred on **intensional objects** and their boundary invariants; reserves deontic obligations for governance contexts and **U.PromiseContent**‑like promises. Do **not** misuse “plane”: deontic speech‑acts are analysed via the **Gov** lens, while **ReferencePlane** remains `{world | concept | episteme}`.

### E.10:6.2 - Twin‑Register Discipline (Tech / Plain)

**Plain twin (LEX).** A registry entry pairing the **authoritative Tech label** with a **display‑only Plain label** for one `U.Type` **in one `U.BoundedContext`**; governed by **PTG (Plain Twin Governance; in the LEX registry)** and referenced by `Twin‑Map ID (LEX)`. *“Plain twin” ≠ the **Plain register** (the register is where twins may be used; the twin is the 1:1 mapping).*
**Convention.** In this spec, **Plain** (capitalized) names the register; **plain twin** (lowercase) names the 1:1 mapping entry.

> **Rule R‑0 (Registers).** Every Kernel and Extenstion patterns concept has a **Tech label** (the testable semantic token) and an optional **Plain label** (didactic synonym). The **Tech label is authoritative**; the Plain label is permitted *only* in expository text and must map 1:1 to the Tech meaning inside the current **Context**.

#### E.10:6.2.1 - Allowed pairs (normative table; examples)

| **Tech (authoritative)** | **Plain (didactic)**                        | **Notes & guards**                                                                           |
| ------------------------ | ------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `U.System`               | system, machine, team                        | Bare “service” is **never** a safe Plain twin for `U.System`; treat it as an **always‑unpack** token (L‑SERV, A.6.8). Avoid “service‑instance”; prefer “system instance”, “service access point”, or “service offering” depending on facet. |
| `U.Episteme`             | body of knowledge, document, dataset, model | Pair must respect **Carrier vs Content** (A.7).                                              |
| `U.Method`               | how‑to, procedure (abstract)                | Do **not** call this “process” (L‑PROC).                                                     |
| `U.MethodDescription`    | recipe, SOP, playbook, code, spec‑text      | If testable, call out **Spec** explicitly per E.10.D2 (I/D/S).                               |
| `U.Work`                 | run, execution, activity, job, case         | Never use “process” or “procedure” here.                                                     |
| `U.Role`                 | role, hat, mask                             | Always **context‑indexed** per D.CTX.                                                        |
| `U.PromiseContent`              | promise, offering, service offering         | Never equate to provider system or API (L‑SERV).                                             |
| `U.Capability`           | ability, capacity (within bounds)           | Separate from Role/Method/Work; must carry **envelope & measures**.                          |
| `U.Dynamics`             | law of change, model of evolution           | Not a capability or a method.                                                                |

**R‑1 (Plain first‑use).** At first use in a section, show **Tech label** and (optionally) the Plain twin: *“…a `U.Method` (the **how‑to**), described by a `U.MethodDescription` (the **recipe**) …”*
**R‑2 (No unpaired Plain in CC).** Conformance Checklists must use **Tech labels** only.

Domains can mint aliases inside their `U.BoundedContext` glossary; all aliases must map 1:1 to a Tech label (**SenseCell** row in the Context’s **Concept-Set Table**), and if exported across Contexts, via an **Alignment Bridge** (with **CL/Loss**).

 Make “plain twins” (reader‑friendly labels) **safe by construction**, not just style. The plain twin must **not** change kind, scope, or reader expectations versus the canonical Tech name; it is **display‑only** and **context‑local**.

* **Tech name (tech)** — the canonical, kernel‑conformant label used in **normative** clauses (e.g., `U.RoleAssignment`, `TransformerRole`).
* **Plain twin (plain)** — a didactic **display alias** permitted in **expository** prose and UI surfaces **inside one `U.BoundedContext`**.

> **Principle:** *Meaning lives in the Tech name; the plain twin may never move meaning.* (Locality is enforced by `U.BoundedContext` and Bridges.)

#### E.10:6.2.2 - Plain Twin Safety constraints (normative)

**CC‑TWIN‑1 - One‑to‑one & local.**
Each Tech name has **at most one** plain twin **per `U.BoundedContext`**; the same plain twin **MUST NOT** point at more than one Tech name in the same Context.

**CC‑TWIN‑2 - Sense‑equivalence proof.**
A plain twin **MUST** bind to the **same SenseCell** as its Tech name in that Context (F.3/F.7). Authors **MUST** record at least one **counter‑example test** showing how the twin could be misread and why it still passes **in this Context** (SenseCell notes).

**CC‑TWIN‑3 - Head‑term discipline (HND).**
The plain twin **MUST** preserve the **head term** of the Tech name, or append an explicit bracketed head on **first use**:

* Roles keep **“(role)”**, Services keep **“(service)”**, Methods keep **“(method)”**, Work keeps **“(work record)”**, Capability keeps **“(capability)”**.
  *Examples:*
  `TransformerRole` → “**Transformer (role)**”,
  `U.PromiseContent` → “**Service (service)**”,
  `U.Work` → “**work (work record)**”.

**CC‑TWIN‑4 - Kind‑consistent.**
A plain twin **MUST NOT** map across **Kinds** (C.3). If the twin’s everyday reading could denote a different Kind (e.g., *Tradition* = organization, corpus, domain), it is **forbidden** unless qualified by a bracketed head and **Context gloss** on first use (see CC‑TWIN‑7).

 **CC‑TWIN‑5 - Ambiguity stop‑list.**
The following base nouns are **reserved** and **MUST NOT** be used as unqualified plain twins: *Tradition, service, process, function, model, system, method, standard, library, dataset, evidence, activity, task, action*.
They are allowed **only** with an explicit head per **CC‑TWIN‑3** and a **Context gloss** (CC‑TWIN‑7). *(This list MAY be extended in the registry.)*

**CC‑TWIN‑6 - No cross‑context by label.**
Plain twins are **not portable**. Reuse in another `U.BoundedContext` requires a **Bridge** with CL and loss notes; names alone carry no authority.

**CC‑TWIN‑7 - First‑use gloss.**
At first occurrence in a document or screen, a plain twin **MUST** be shown as **“Plain twin \[Tech name] — Context gloss”**, e.g.:
“**Transformer (role)** \[**TransformerRole**] — *mask borne by a system to enact a method step in OR\_2025*”.

**CC‑TWIN‑8 - Normative surface ban.**
Plain twins **MUST NOT** appear in **Conformance Checklists, predicates, type signatures, or acceptance clauses**. Only Tech names are normative. (Plain twins are strictly didactic.)

**CC‑TWIN‑9 - Twin budget.**
**At most one** plain twin per Tech name per Context. Synonym piles are prohibited (control vocabulary sprawl; see F.14).

**CC‑TWIN‑10 - Registry entry & DRR.** 
Every plain twin **MUST** have a **registry entry** (in the LEX registry) recording: `tech`, `plain`, `context`, `head`, **SenseFidelity = {3,2,1,0}**, ambiguity notes, counter‑examples, DRR id. Any change requires a **DRR**. 

**CC‑TWIN‑11 - Tests.**
 Twin entries **MUST** pass the **Twin Harness** (see F.15): *Head term*, *Kind consistency*, *SenseCell match*, *Stop‑list compliance*, and *First‑use gloss*.

### E.10:7 - Minimal Generality & Domain Anchoring (MG-DA) — names neither parochial nor vacuous

> **Principle (MG-DA).** A minted name is **as general as necessary and no more**, and its **head noun is anchored to the object‑of‑talk**. First classify the **NameToken (name of a concept: term, lexical unit) itself** using **`LEX.TokenClass`**, then apply the guardrails corresponding to that class: kernel tokens must unify **across domains**; discriminator/context tokens must make the **domain legible** *from the name itself*. Names too general to have obvious domain are **banned**. 

#### E.10:7.1 - `LEX.TokenClass` (meta‑lexical; not a USM Scope)
**Definition.** `LEX.TokenClass : NameToken → {KernelToken | ContextToken | DiscriminatorToken}`.  
This is a **Characteristic on NameTokens** (symbols), used by the LEX registry and MG-DA lints.
It is **not** a USM scope and carries **no** truth/validity semantics.

#### E.10:7.2 - `KernelToken` — Minimal Generality (MG‑K)
**MG‑K1 (Tri‑domain witness, MUST).** Maintain a DRR/Glossary note with **≥ 3 heterogeneous arenas** where the invariants hold (e.g., manufacturing, healthcare, cloud ops). If you cannot, narrow to a Context name or move qualifiers into **RCS** (Role Characterisation Space).
**MG‑K2 (No parochial nouns, MUST).** Kernel names **MUST NOT** contain domain nouns (*Ticket, Microservice, Patient, Developer*). Such nouns belong in **Context** or as **RCS Characteristics**.
**MG‑K3 (No vacuity, MUST).** Avoid vacuous heads (*Thing, Event, Process, Resource*). Use existing kernel heads (`U.Holon`, `U.Work`, `U.Method`, `U.Resrc`, …).
**MG‑K4 (Intent over mechanism, MUST).** Kernel type/role names encode **intent**, not mechanism. Mechanisms (algorithms, hardware form, recipe flavors) live in **RCS** or **Capability**.
**MG‑K5 (Notation independence, SHOULD).** The intensional meaning is separable from any one notation/toolchain.
**MG‑K6 (Refactoring safety, MUST).** If a name fails MG, do **not** mutate it silently. Record a DRR and apply F.13 **Lexical Continuity & Deprecation** (aliases; Bridges for Cross‑context mappings).

#### E.10:7.3 - `DiscriminatorToken` / `ContextToken` — Domain Anchoring (DA‑D)
**DA‑D1 (Object‑of‑talk anchoring, MUST).** The head noun names the **object being classified** (e.g., *Sense*, *Context*, *Role*, *Bridge*, *Characteristic*). Readers can answer “**X of what?**” without external context.
**DA‑D2 (Characteristic, not axis, MUST).** Enumerated properties are named as **Characteristic**  within a **CharacteristicSpace** (MM‑CAL). Avoid spatial metaphors (*axis, dimension, plane, lane, tier, layer*) unless the metaphor is a **pattern‑defined primitive** in this spec.
**DA‑D3 (Enum clarity, MUST).** If the term denotes an enumeration, (a) the value set is **small and closed**, (b) membership criteria are obvious from the definition, (c) the **object‑of‑talk** is explicit in the name (e.g., `SenseFamily`, not bare *Family*, *RowPlane* or overly general *Facet*).
**DA‑D4 (Anti‑recipe, MUST).** Do not bake *how‑to* or local methods into discriminator names; those belong in `U.Method/MethodDescription` or **Capability**.
**DA‑D5 (Mapping discipline, MUST).** Cross‑context readings go through a **Bridge** (F.9). Discriminator names must not suggest global identity.
**DA‑D6 (Register discipline, SHOULD).** Keep normative tokens stable; synonyms live in **Plain** register only and must not appear in constraints/tests.
**DA‑D7 (Ban generic combinators, MUST).** Reject vague composites like *NameUseMode*, *NamingScope*, *RowFacet/RowPlane/RowLane*. Each candidate must pass **DA‑D1** and **DA‑D3** (object‑anchored head and explicit **CharacteristicSpace**).

#### E.10:7.4  - Global tests (apply after 7.2/7.3)
**MG-DA‑T1 (Three‑arena witness).** If **`LEX.TokenClass`(t)=KernelToken**, you **MUST** provide the tri‑domain witnesses (7.2‑MG‑K1). Otherwise this is **SHOULD** (document at least one contrasting arena).
**MG-DA‑T2 (Object‑of‑talk).** The head noun uniquely signals the subject area; avoid free‑floating metaphors. **MG-DA‑T3 (Anti‑recipe).** Remove mechanism/implementation words; relocate to Method/Capability/RCS.
**MG-DA‑T4 (Enum clarity).** For enumerations, list the closed value set and its CharacteristicSpace.
**MG-DA‑T5 (Collision & Uniqueness, MUST).** Before merge, run a **full‑text search** over the corpus and the **Reserved‑Names registry**. The candidate **MUST NOT** collide with any existing token used in another sense anywhere in FPF. If a collision exists, either rename or raise a DRR to deprecate the prior token.
**MG-DA‑T6 (Teaching swap).** In didactic prose (E.10.D2), the term can be swapped in **without caveats**. 
**MG-DA‑T7 (Intensional ground, MUST).** The definition card states the intensional criterion for membership explicitly; reviewers can check membership without reading external narrative.

#### E.10:7.5 - Compatibility with USM (how tokens and scopes meet)
**USM applies to acts, not tokens.** Mint/rename/use are **LexicalActs** that carry a USM scope. `LEX.TokenClass` constrains **where** a token may be used via an **AllowedScopes** policy:
**Conformance rule.** For any usage `u` of a token `t`: `LEX.TokenClass(t)=c  ⇒  USM.Scope(u) ∈ AllowedScopes(c).`

The LEX registry defines `AllowedScopes(c)` (e.g., `KernelToken` usage in normative kernel constraints is allowed; in Plain register outside a glossary is restricted; Context emissions of `KernelToken` require a Bridge/alias, etc.).

**Audit.** Violations are flagged as **SCR‑LEX‑Sxx** (see acceptance tests below).

#### E.10:7.6 - Metaphor guidance (non‑binding heuristics)
Prefer **object‑anchored heads** to metaphors. If a metaphor is unavoidable, ensure it is (a) explicitly defined by a pattern here, and (b) unambiguous within the **NameClass**. Example families (use sparingly):
* **Progression metaphors** (*level, tier, ladder*): only where a **gate/upgrade** is defined by the pattern.  
* **Separation metaphors** (*lane, track*): only where parallel, non‑interfering flows are enforced by rules.  
* **Grouping metaphors** (*family, class*): only for **small, closed enumerations** attached to a clearly named object‑of‑talk (e.g., `SenseFamily` rather than bare *Family*).

#### E.10:7.7 - Short‑form and acronym discipline
**SF‑1 (First expansion, MUST).** On first use, expand the term; place the short‑form in parentheses (e.g., “Minimal Generality & Domain Anchoring (**MG-DA**)”).  
**SF‑2 (Uniqueness, MUST).** Register short‑forms in the **Reserved‑Names** list; run the collision check (7.4‑MG-DA‑T5).  
**SF‑3 (Form, SHOULD).** Prefer typographic separators (**MG-DA**) to fused acronyms (**MGDA**). Use the fused form only in code or identifiers where punctuation is disallowed, and only after registration.

#### E.10:7.8 - Examples (illustrative, canonical)
Prefer **`U.PromiseContent`** (promise) over *BusinessService*; **`U.Capability`** over *Function*; **`U.Dynamics`** over *NaturalProcess*; **`U.WorkPlan`** over *ScheduleProcess*.  
Do **not** mint *ETLService* at kernel level—model ETL as `MethodDescription`; the **Service** is “data delivered under acceptance.”

#### E.10:7.9 - Acceptance & regression checks (LEX/USM)
**SCR‑LEX‑S01 (TokenClass declaration).** Every normative token has a declared `LEX.TokenClass`.
**SCR‑LEX‑S02 (Collision & uniqueness).** Full‑text + Reserved‑Names check passes (no other meaning in FPF).
**SCR‑LEX‑S03 (Object‑of‑talk anchoring).** Heads name the object classified (DA‑D1).
**SCR‑LEX‑S04 (CharacteristicSpace).** Enumerations declare their value set and space (DA‑D2/3).
**SCR‑LEX‑S05 (USM compatibility).** For each LexicalAct, `USM.Scope ∈ AllowedScopes(LEX.TokenClass)`.
**SCR‑LEX‑S06 (Slot/Ref suffix discipline).** Any token with suffix **`…Slot`** or **`…Ref`** is either (a) a **SlotKind**/**RefKind** declared under A.6.5, or (b) a episteme field whose type is a RefKind; no ValueKind or other type class may end with these suffixes.
**SCR‑LEX‑S07 (Manifest `provides` covers SlotKinds/RefKinds).** If a `SignatureManifest` is present (A.6.0), its `provides` list MUST include any public **SlotKinds** (`…Slot`) and **RefKinds** (`…Ref`) introduced by that signature/mechanism (in addition to types/relations/operators), so SD/lexical linters can treat them as exported API surface.
**RSCR‑LEX‑E01 (Banned generics).** Reject tokens matching the banned combinators list (DA‑D7).
**RSCR‑LEX‑E02 (Metaphor hygiene).** If a metaphor is used, show the pattern that defines it; otherwise rename.
**RSCR‑LEX‑E03 (Strategy token minting).** Reject new Kernel tokens named **Strategy**/**Policy** as kinds; model them as **lenses/flows/compositions** inside **G.5** or as **…Description/…Spec** in Contexts. (Prevents kernel overloading; aligns with C.22 “no minted Strategy head”.)

### E.10:8 - Morphology & Lexical Form (LEX.Morph)

> **Principle.** Form follows **object‑of‑talk**. A token’s morphology (suffix/prefix/casing) must (a) express **what kind of thing** it names, (b) respect **MG-DA** (Minimal Generality & Domain Anchoring), and (c) pass **LEX.TokenClass** gates:
> `LEX.TokenClass(token) ∈ {KernelToken | ContextToken | DiscriminatorToken}`.
> Morphological choices never override **I/D/S layers** or **CHR\:ReferencePlane** semantics.

#### E.10:8.0 - Casing & basic forms

**M‑0 (Casing and categories).**
Types & role kinds: **UpperCamelCase** (`IncisionOperatorRole`, `MethodDescription`).
Relations/verbs: **lowerCamelCase** (`performedBy`, `isExecutionOf`, `bindsMethod`).
IDs/instances: **flat with delimiters** (context‑defined) but never collide with type forms (e.g., `W#Seam134`, `ctx:Hospital.OR_2025`).
**Register discipline:** normative tokens use the Technical register; Plain synonyms are allowed in prose only, never in constraints.


#### E.10:8.1 - Reserved suffixes (gated by LEX.TokenClass and I/D/S)

> **Use tables as a whitelist.** Rows indicate **when** a suffix is permitted and **what it means**. “Layer gate” prevents I/D/S confusion; “Examples” are illustrative.

| **Suffix**              | **Kind named** (object‑of‑talk)            | **Layer gate**                       | **LEX.TokenClass gate**         | **Examples**                                      | **Forbidden misuses (typical)**                                       |
| ----------------------- | ------------------------------------------ | ------------------------------------ | ------------------------------- | ------------------------------------------------- | --------------------------------------------------------------------- |
| **`Role`**              | **Role kind** (intensional)                | I‑layer                              | KernelToken/ContextToken        | `TransformerRole`, `ApproverRole`                 | Appearing in BoM/mereology; mixing with run logs.                     |
| **`Method`**            | **Abstract way of doing** (recipe type)    | I‑layer                              | KernelToken/ContextToken        | `SteriliseInstrumentMethod`                       | Versioning on `Method` (version the `MethodDescription` instead).     |
| **`MethodDescription`** | **Recipe/description** (notation‑agnostic) | D‑layer                              | KernelToken/ContextToken        | `JS_Schedule_v4_MethodDescription`                | Calling it “process”; encoding runtime actuals here.                  |
| **`…Spec`**             | **Testable specification** (acceptance‑bound) | S‑layer                              | KernelToken/ContextToken        | `MethodSpec`, `FlowSpec`, `SystemSpec`            | Using “Spec” without acceptance tests/harness; putting runtime actuals here. |
| **`Work`**              | **Execution** (runs or kinds of runs)      | (run artefact; not I/D/S)            | KernelToken/ContextToken        | `SpeechActWork`, `W#Seam134`                      | Plans/schedules; design‑time recipes.                                 |
| **`WorkPlan`**          | **Schedule of intent**                     | D‑layer (plan artefact)              | ContextToken                    | `MaintenanceWorkPlan_Q3`                          | Logging actuals; claiming execution.                                  |
| **`Service`**           | **External promise object**                | I‑layer (Standarded intension)       | KernelToken/ContextToken        | `ObjectStorageService`, `PassportIssuanceService` | Naming teams/APIs as “Service”.                                       |
| **`Capability`**        | **System ability**                         | I‑layer                              | KernelToken/ContextToken        | `ScheduleGenerationCapability`                    | Mislabeling roles or methods as capabilities.                         |
| **`Dynamics`**          | **Law/model of change**                    | I‑layer                              | KernelToken/ContextToken        | `LotkaVolterraDynamics`                           | Using for abilities (`Capability`) or recipes (`Method`).             |
| **`Observation`**       | **Observation record/kind**                | (run artefact; not I/D/S)            | ContextToken/DiscriminatorToken | `VibrationObservation`                            | Mixing with `MethodDescription` or `Evaluation`.                      |
| **`Evaluation`**        | **Evaluation artefact**                    | D/S‑layer (epistemic episteme)              | ContextToken/DiscriminatorToken | `CalibrationEvaluation`                           | Using to name roles or methods.                                       |
| **`EvidenceRole`**      | **Role in evidence assembly**              | I‑layer (role kind)                  | KernelToken/ContextToken        | `WitnessStatementEvidenceRole`                    | Using as a generic “evidence”.                                        |
| **`Episteme`**          | **Epistemic knowledge unit** (structural)  | D/S‑layer                            | KernelToken/ContextToken        | `TraceabilityEpisteme`                            | Colliding with CHR **ReferencePlane** (never suffix “Plane”).         |
| **`System`/`Holon`**    | **Substantial entity**                     | I‑layer                              | KernelToken/ContextToken        | `AnesthesiaSystem`, `OrderFulfillmentHolon`       | Using to denote Context or run artefact.                              |
| **`Boundary`**          | **System boundary**                        | I‑layer                              | KernelToken/ContextToken        | `SterileFieldBoundary`                            | Using as a role or method.                                            |
| **`Objective`**         | **Target state**                           | I/D‑layer (depends on formalization) | KernelToken/ContextToken        | `HemostasisObjective`                             | Encoding acceptance tests here (put tests in Spec/MethodDescription). |
| **`Requirement`**       | **Obligation at acceptance**               | D/S‑layer                            | KernelToken/ContextToken        | `LatencyRequirement`                              | Using as a role or capability.                                        |
| **`BoundedContext`**    | **Context card**                           | (meta‑structural; not I/D/S)         | ContextToken                    | `ITIL_2020_BoundedContext`                        | Treating Context as domain; minting `U.*` inside a Context.           |
| **`Surface`**              | Publication/Interop surface (episteme)   | D/S-layer (publication)     | ContextToken                     | PublicationSurface, InteropSurface       | StructureSurface, MechanismSurface, PortfolioSurface |
| **`Card`**                 | UTS/record unit (episteme)               | D-layer (publication)       | ContextToken                     | MethodCard, ExternalIndexCard            | Encoding runtime actuals; using as a ‘Service’  |
 
| **Suffix** | **Lexical class** | **Meaning / Ontology** | **Where it lives** | **Examples / Notes** |
|--- |--- |--- |--- |--- |
| **Space** | Intensional kind | A typed **state space** (finite product of Characteristic×Scale slots); no procedures | Kernel A.19; CHR/space consumers | `CharacteristicSpace`, `CreativitySpace`. Edition of a Space is a **phase** of the episteme that defines it. |
| **SpaceRef** | Pointer | Registry reference to a Space | Data fields / UTS | `CharacteristicSpaceRef`. Use **`.edition`** on the **Ref** when pinning a historical phase. |
| **Map** | Intensional kind (method) | A **mapping method** from subjects to coordinates in a declared Space (encoder/featurizer) | Kernel/Method family (I‑layer), described/spec’d via I/D/S | `DescriptorMap` (declares invariances, corpus typing). Not a record or file. |
| **MapRef** | Pointer | Registry reference to a **Map** | Data fields / UTS | `DescriptorMapRef`. Pin the method phase via **`DescriptorMapRef.edition`**. |
| **Def** | S‑layer alias (CG‑Spec family) | A **definition/specification artifact** that fixes a **formula** or **distance** over a space; *synonym of …Spec* **within CG‑Spec registries only** | Part G (CG‑Spec family) | `DistanceDef` ≍ `DistanceSpec`. Prefer **…Spec** in new normative prose; **…Def** retained where already published. |
| **DefRef** | Pointer | Registry reference to a **…Spec/…Def** | Data fields / UTS | `DistanceDefRef`. Use **`DistanceDefRef.edition`** to pin the exact formula edition. |
| **Spec** | S‑layer | Testable invariants bound to acceptance harnesses | E.10 & A.21 | For stable, testable definitions; **normative** by default; S‑layer, Spec‑gated | Use for normative calculi and scoring/normalization specifications. |
| **Slot** | Structural position | Named **argument position** in a relation/morphism signature (SlotKind in A.6.5) | Kernel A.6.0/A.6.5 | `DescribedEntitySlot`, `GroundingHolonSlot`. Always names a *position*; never used for ValueKinds or episteme fields. |
| **Ref** | Pointer | **Reference/identifier** to a registry item of some ValueKind (RefKind in A.6.5), not the thing itself | Data fields / UTS; RefKind types | `U.EntityRef`, `U.HolonRef`; episteme fields `…Ref : U.EntityRef`. Reserved for **RefKinds** and episteme fields typed as them; `…Ref` **never** carries content and is never used for ValueKinds or SlotKinds. |
| **Series** | Governance object | A **PhaseOf chain** (“editions”) for an episteme | Edition governance | `U.EditionSeries`. Holds immutability and provenance rules. |
| **.edition** | Attribute (on **Ref**) | The **phase id** of the **referenced artifact**; attaches to `…Ref`, not to the artifact’s name | Data fields / UTS | Use `XRef.edition`, **not** bare `XEdition` fields. Lower camelCase for keys. |

**Notes.**
• **Kernel‑only ban list** remains in § 8.3.
• **CHR guard:** the only token that may use the word *plane* is **CHR:ReferencePlane**.
• **Axis/dimension metaphors** are deprecated; use **Characteristic / CharacteristicSpace** where an enumeration is intended (see § 7).

**Not only suffix guard**
* Suffixes are strongly related to kinds and **should** be clearly guarded by MG-DA.
* Other morphemes (not only suffixes) also **must** respect kinds. For example, **Space is a geometric concept** — **never** use it as a suffix (`…Space…`) or other morpheme in beginning or in the middle of a term to name non‑geometric entities (e.g. prefer **Set/Kid/Kit** instead of **Space** where membership is intended).

**L‑SURF — disciplined use of *Surface* **
* **Definition.** *Surface* is reserved for **publication/interoperability surfaces** (UTS, shipping, interop) that present lawful, plane‑aware summaries for human/selector consumption. A **Surface is a bundle of views** (ISO 42010 sense) packaged for a stated **audience** and **purpose**, with declared **viewpoint**. Surfaces are **conceptual** (E.5.2); serialisations live in Annex/Interop. Surfaces package **D/S** projections produced via `Describe_ID` / `Specify_DS` (A.7) and do **not** change object ontology.
* **Allowed:** `PublicationSurface`, `InteropSurface` (G.10/G.13).  
* **Forbidden:** `StructureSurface`, `MechanismSurface`, any `…Surface` that denotes a structural, mechanistic or measurement object.  
* **Preferred alternatives:** use `…Boundary` (structural border), `…View` (publication view), or `…Card` (UTS record).

**L‑SPACE — disciplined use of *Space* **
* Use *Space* only for **CHR‑grounded measurement/state constructs** (e.g., `CharacteristicSpace` per A.19). Do **not** coin generic `…Space` for sets/portfolios or publication artefacts. Publish portfolios/archives as **sets** via lawful selectors; surface them on UTS as **views/cards**, not as spaces. 
* **Field‑name guard (Kernel blocks).** In **Kernel conceptual blocks** (e.g., A.6.0/A.6.1 lists), **do not** name a field `…Space`; reserve *Space* to the **types** (CHR/ReferencePlane families). Use **BaseType** as the field name and let the referenced `U.Type` carry `…Space` where appropriate; otherwise, for set‑valued universes, use `…Set`.
* Space is geomertic concept, neve use it even not as a suffix for naming non-geometric spaces (e.g. instead of Sets with membership)

**L‑ROLE — disciplined use of *Role***
* **Role** is always **Role Enactment for the `U.Holon`/`U.System` kind** (agentive use).
* **Param‑slot / relation‑endpoint guard.** Do **not** use the morpheme **`Role`** for **formal parameter positions** in operator algebra declarations (`OperationAlgebra`) or Signature arguments. Reserve **`Role`** for **agentive kinds** only (A.2/F.4/F.6). Prefer SlotKinds + SlotSpecs (A.6.5) to type formal slots; if a didactic list is useful, use a `ValueKindView` (name→ValueKind) projection derived from SlotSpecs/SlotIndex. Same for similar situations (table columns, tuple placements): use MG-DA with domain‑**specific** terminology, never “Role”. 

#### E.10:8.2 - Forbidden suffixes & the DevOps, Data Governance and Repository-Workflow Lexical Firewall

**M‑F (Forbidden in Kernel tokens).** In KernelToken names, do **not** use: *…Function*, *…Process*, *…Task*, *…Activity*. These are ambiguous or vacuous—map using § 6 typing rules (often to `Method`, `MethodDescription`, or `Work`).

**M‑FW (Tool/file markers).** Tooling/file suffixes (*…API*, *…JSON*, *…YAML*, *…CI*, *…Kafka*, *…Postgres*) are **not** part of conceptual names. Place them in **Context** glossaries or operational configs (DevOps Lexical Firewall). Kernel names never carry tool/format/notation marks. It is pure conceptual, no data management and data governance intended.

#### E.10:8.3 - Prefix discipline

**M‑P1 (Reserved prefixes).** `U.` reserved for **Kernel types**; `Γ_` for algebraic operators; `CAL/LOG/CHR` for **pattern packages**. Never mint `U.*` inside a Context.

**M‑P2 (Edition markers).** Apply explicit edition/version markers to **Contexts** and to `MethodDescription` / `Service`—**not** to `Method` (e.g., `BPMN_2.0_BoundedContext`, `JS_Schedule_v4_MethodDescription`, `PassportIssuanceService_v2025`).  Authors MAY annotate Context or Service names for didactics.
**Norms (edition vs release vs version).**
1) **edition** — the **content phase** of an episteme (Concept/Object/Symbol where Symbol‑only notation swaps do not force a phase). Lives in `U.EditionSeries`. Never embedded in labels (see R‑RD‑7); bind via data: `…Ref.edition`. 
2) **release** — a **Work** of making a **Carrier** public; may carry tags/dates; does **not** change episteme identity or phase.
3) **version** — a **tooling/carrier** identifier (file/package/code). Use only in Tooling/Pedagogy families; not in Core names.

**Property discipline.** When a field pins a referenced artifact’s phase, write it as **`<Thing>Ref.edition`** (dot notation), never as a standalone `…Edition` key. E.g., replace `DHCMethodEdition` with `DHCMethodRef.edition`.

#### E.10:8.4 - Morphology tests (apply with § 7 MG-DA)

**M‑1 (Slot test).** The candidate fits **one** slot in the Strict Distinction lattice (Object ≠ Description ≠ Carrier; Role ≠ Method ≠ Work). If not, **rename** or split.

**M‑2 (Object‑of‑talk anchoring).** The head noun names the **object being classified** (Role/Method/Service/Work/Context/Characteristic). No free‑floating metaphors.

**M‑3 (Family congruence).** Where eligibility clarity is needed, add a **Context‑specific characteristic** (RCS) as a qualifier (e.g., `NormativeStandardRole`). Do **not** fake families with bare metaphors (no `RowPlane`, `senseFamily`, `…Lane`).

**M‑4 (Run vs design).** Use **`Work`** only for executions; use **`MethodDescription`** for recipes; never cross.

**M‑5 (Kernel parochiality).** KernelToken names carry **no domain nouns**; push domain markers to Context or RCS.

**M‑6 (Vacuity ban).** Avoid vacuous heads (*Thing, Event, Process, Resource*). Use established kernel heads (`U.Holon`, `U.Work`, `U.Method`, `U.Resrc`, …).

**M‑7 (Notation independence).** Intensional meaning survives notation/tool swaps.

**M‑8 (Collision & uniqueness).** Before merge, run **full‑text** + **Reserved‑Names** checks; the token must not collide with any other meaning anywhere in FPF (cf. § 7 MG-DA‑T5).

#### E.10:8.5 - Alias hygiene

Aliases live **only** inside a **Context Glossary** and map to **one** technical label with an **equivalence** note (≡). No global aliases.

#### E.10:8.6 - Compatibility with USM (acts vs tokens)

**LEX applies to tokens; USM applies to acts.** Mint/rename/use are **LexicalActs** that carry a USM scope (e.g., ClaimScope, WorkScope). LEX constrains **where** a token form may appear via **AllowedScopes** policies:

`LEX.TokenClass(t)=c  ⇒  USM.Scope(usage) ∈ AllowedScopes(c)`.

Example: using a `KernelToken` in a Context constraint may require a Bridge/alias; logging `Work` inside a MethodDescription violates M‑4 and the policy.

#### E.10:8.7 - Acceptance & regression checks (LEX/USM)

* **SCR‑MOR‑S01 (Suffix whitelist).** Every normative token with a reserved suffix matches § 8.1 row semantics and passes Layer gates.
* **SCR‑MOR‑S02 (Kernel bans).** KernelToken names contain none of the forbidden suffixes (§ 8.2).
* **SCR‑MOR‑S03 (Prefixes).** Reserved prefixes obey § 8.3; no `U.*` minted in Context.
* **SCR‑MOR‑S04 (Run/design gate).** `Work` appears only for executions; `MethodDescription` has no runtime actuals.
* **SCR‑MOR‑S05 (Collision).** Full‑text + Reserved‑Names checks pass (no other sense of the token elsewhere).
* **SCR‑MOR‑S06 (Object‑of‑talk).** Heads pass M‑2; no bare metaphors as heads.
* **RSCR‑MOR‑E01 (DevOps firewall).** Tool/file suffixes quarantined to Context; none leak into KernelToken names.
* **RSCR‑MOR‑E02 (USM compliance).** For each LexicalAct, verify `USM.Scope ∈ AllowedScopes(LEX.TokenClass)` (see § 7.5).

#### E.10:8.8 - Autonomy lexicon (L‑AUTO )
**Forbidden (Core):** bare “validity”, “actor/agent” (as free‑standing nouns), “kill switch”, “process” for behavior, “envelope” when used **as scope**.
**Use instead:** *Scope (G)* for epistemic scope; *WorkScope* for capability bounds; *RoleAssignment* for who acts; *SpeechAct* for overrides; *SafeStop* instead of “kill switch”.
**Named prefixes (policy & registry):**
* `aut:` for AutonomyBudgetDecl fields (e.g., `aut:action_tokens`, `aut:risk_bands`);
* `guard:` for guard checks bound to `AdmissibilityConditionsId`;
* `ovr:` for override SpeechActs (`ovr:PauseAutonomy`, `ovr:ResumeAutonomy`, …).

**Notes.**
1) Scope‑sensitive guards **must** declare the **Γ_time** window selector used for admission checks.
2) Proper names of patterns/components that already include “Agent/Agency” (e.g., *Agency‑CHR*, *Agent‑Tools‑CAL*) are permitted as **titled terms**; avoid re‑introducing “agent” as a free‑standing noun in new prose.

#### E.10:8.9 - LEX-CHR-STRICT — Reserve *Characteristic* for CSLC-measurable aspects

**Intent.** Prevent calling **non-measurable** objects (sets, statuses, scopes, policies, bridges, contexts, guards) “characteristics”.

**Rule L-CHR-S1 (Reservation).** Use **Characteristic** **only** for variables that **declare a CSLC scale** (nominal/ordinal/interval/ratio) with admissible values/units/polarity (Part C.16/A.17–A.18).  
**Rule L-CHR-S2 (USM).** `U.Scope` / `U.ClaimScope (G)` / `U.WorkScope` are **USM scope objects**, not Characteristics; they **must not** appear in any `CharacteristicSpace`.  
**Rule L-CHR-S3 (Status).** ESG/RSG statuses and deontic/epistemic statuses — **not Characteristics**; its statuses/states.  
**Rule L-CHR-S4 (Lexical classifiers).** Lexical classifiers/tags — **Facets**/**attributes**; do not name them as Characteristics, if not declared **CSLC**.
**Checks.**  
— **CC-L-CHR-1.** `scope characteristic(s)` is banned in Core/Context.  
— **CC-L-CHR-2.** `CharacteristicSpace` near `Scope` — error.  
— **CC-L-CHR-3.** Canonical rewrite: `F–G–R characteristics` → `F–G–R components`.

#### E.10:8.10 - LEX‑QA‑1 — Using “‑ility/‑ilities” terms (availability, reliability, …)

**Rule.** Tokens ending with **‑ility/‑ilities** or widely used quality names (**Availability, Reliability, Security, Safety, Scalability, Maintainability, Usability**, …) are **Quality‑Family labels**, not automatically CHR **Characteristics**.  

**Authoring choice:**  
— To use such a term as a **CHR** characteristic (axis), **bind** it to a **named `U.Characteristic` with one CSLC Scale** (A.18) and refer to that Characteristic in guards/UTS;  
— Otherwise **publish a Q‑Bundle** (see **C.25**) that includes **Measures (CHR)** (the measurable slots) and, where relevant, **Scope** (USM set over `U.ContextSlice`) and windows/mechanism/status fields.  

**Rationale.** Scope is **set‑valued** (USM) and **not** a CHR measurement; mechanisms/statuses are governance artefacts. Keeping them outside the CHR CSLC avoids illegal scalarisation and preserves set‑algebra semantics for scope.  (A.2.6 § 6.2; A.6.1; C.16/A.18). 


### E.10:9 - Canonical rewrites for overloaded words (LEX L‑rules; normative)

> **What this section does.** LEX L‑rules standardise **how we speak** in Core/Context by mapping overloaded everyday words to **canonical FPF concepts**.
> **What this section does not do.** It does **not** restate naming (see **§ 7 MG-DA**) or morphology/casing/suffix rules (see **§ 8 LEX.Morph**); it **depends** on them.
> **Guards.** Tokens are classified by **`LEX.TokenClass ∈ {KernelToken, ContextToken, DiscriminatorToken}`** (§ 7.1). Only **CHR:ReferencePlane** may use the bare word *plane*; I/D/S are **layers**; enumerations are **Characteristics** in a **CharacteristicSpace** **only when a CSLC scale is declared; otherwise treat such slots as non-measurable attributes (not Characteristics)**.

#### E.10:9.1 - Hard bans and canonical rewrites (single table; normative)

