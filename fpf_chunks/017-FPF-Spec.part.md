- `TaskSignature` attachment means attaching one typed problem record to one declared task family or work target; it does **not** pre-bind a method.
- `ScopeSlice(G)` means the claim-bounding scope cut over `describedEntity/scope`; it is not an evidence-path slice and not a baseline-set slice.
- `threshold` is not one undifferentiated family here:
  - articulation and closure thresholds stay with cue or prompt governing patterns such as `B.4.1` and `B.5.2.0`
  - acceptance-gate thresholds stay with `G.4`
  - the work-measure threshold target used in specialization claims is only the declared success mark for the current task family or work target
### C.22:2 - Problem Frame (DesignRunTag split; crossing-visible)

**method‑first stance**
In FPF a **Problem** exists when a Holder or external **Transformer** cannot cite a known **Method** (or specialisation thereof) that satisfies the current **TaskSignature** under the declared **ScopeSlice(G)**. Problem‑solving therefore entails **strategizing** (selecting or synthesising a method). The resulting **strategy/policy** is a composition under **G.5/E/E‑LOG** and **is not** a new kernel type.
**Unknown‑first discipline.** Author S2 with `unknown` traits rather than coercions; **SoS‑LOG** branches MUST specify `{admit|degrade|abstain|sandbox}` handling for `unknown` via closed enums registered at UTS.

Un‑typed "problems" collapse into **informal prose**; selectors cannot **filter or abstain** admissibly; acceptance-gate thresholds leak into scoring; cross‑Context reuse is by name, not Bridge. We need a Context‑local descriptor that (i) obeys **MM‑CHR legality** (Scale/Unit/Polarity proven before any aggregation), (ii) records **Assurance lanes (TA/VA/LA)** per **A.10** and **ReferencePlane**, (iii) carries **tri‑state unknowns** explicitly, and (iv) **publishes crossing attestations** (**BridgeCard + UTS row**) with **Φ(CL)/Φ_plane** policy‑ids.

### C.22:3 - Problem

Without typed descriptors, **Eligibility/Acceptance** degenerate into prose; **illegal ops** creep in (ordinal means; unit mixing); **cross‑plane comparisons** lose **CL/Φ** routing (**penalties to R_eff only**).

### C.22:4 - Forces

| Force                        | Tension                                                                                                                           |
| ---------------------------- | --------------------------------------------------------------------------------------------------------------------------------- |
| **Parsimony vs sufficiency** | Fewer fields to avoid ceremony **vs** enough to drive lawful gating.                                                              |
| **Unknowns**                 | Many traits are **unknown** at intake → tri‑state semantics must propagate to Acceptance without silent coercions.                |
| **CHR legality**             | **No mean on ordinals; no unit mixing**; polarity & scale type must be declared *before* aggregation.                             |
| **Locality vs portability**  | Problem is **in‑room**; still must cross **via Bridges**, with **CL** and (if planes differ) **CL^plane** penalties → **R** only. |


### C.22:5 - Solution — **Problem‑CHR** (fields) + **TaskSignature (S2) attachment** *(normative)*

#### C.22:5.1 - Minimal CHR fields (tri‑state aware).
Each field is **CHR‑typed** (Characteristic/Scale/Unit/Polarity; MM‑CHR discipline). Every predicate admits `unknown` (tri‑state). Unknowns must propagate to {degrade|abstain|sandbox} per Acceptance/EvidenceProfile policy (recorded in SCR). (G.4/G.6 alignment)

* **`DataShape`** — data regime & admissible transforms (e.g., tabular, sequence, graph; density; stationarity claims).
* **`NoiseModel`** — uncertainty class / robustness envelope (e.g., iid Gaussian; heavy‑tailed; adversarial budget).
* **`ObjectiveProfile`** — objective heads (**Scale/Unit/Polarity** and **ReferencePlane** declared), polarity, and **admissible order relations** (lexicographic, Pareto, medoid/median where legal). **Weighted sums across mixed scale types are forbidden**; ordinal heads use order‑only guards. For QD tasks, explicitly enumerate **Q (quality)**, **D (diversity)**, and **QD‑score** heads; see **DominanceRegime** below.
* `RegularityTraits` — method‑relevant structure (**convexity/differentiability/separability/monotonicity**) as CHR‑typed predicates with guard‑macros (e.g., `ORD_COMPARE_ONLY`, `UNIT_CHECK`, `POLARITY_CHECK`). Include `ConditionClass` (e.g., stiffness/κ‑proxies) where applicable.
* **`Constraints`** — explicit hard/soft constraint classes (feasibility predicates; **ResourceEnvelope**/**RiskEnvelope**). **Acceptance-gate thresholds live in `G.4` only; never inside CHR or code paths.**
* **`ShiftClass/Stationarity`** — CHR‑typed claims about regime stability (iid | covariate‑shift | concept‑drift | adversarial). Default=`unknown`. Acceptance/Flows MUST honor this in gating or abstain.
* `EvidenceGraphRef (A.10)` — carriers & **lane tags (TA/VA/LA)** with **freshness windows**; **no self‑evidence**; default Γ‑fold = **weakest‑link** unless CAL proves an alternative.
* `ScopeSlice(G)` — the **USM claim-bounding scope cut** over **describedEntity/scope** (discipline governance in **CG‑Spec**; Domain is a catalog mark only).
* `Size/Scale` — size/condition proxies (**n, m, κ, sparsity**) with **declared units**; unit mismatch ⇒ {sandbox|refuse}.
* **`Freshness`** — validity window for descriptors.
* `Missingness` — **MCAR/MAR/MNAR** (or mapped equivalents) per **CHR.Missingness**; MUST be honoured by Acceptance/Flows.
* `KindSet` — **`U.Kind[]`** for the described entities addressed by the TaskKind; separates **describedEntity Kind** from **Scope (USM)**.

**QD / Illumination extensions (normative; ties to C.18 and C.19).**
* **`CharacteristicSpaceRef`** — reference to **`U.CharacteristicSpace`**, with declared **d≥2**; **characteristics are CHR‑typed**; **ReferencePlane** per characteristic; pin edition via **`CharacteristicSpaceRef.edition`**.
* **`ArchiveConfig`** — archive **topology** (grid/CVT/graph), **resolution** (bins/centroids), **K‑capacity**, **`InsertionPolicyRef`** (elite replacement/dedup/novelty), and **`DistanceDefRef.edition`** (declare **metric/pseudometric** status and invariances; any normalisation **MUST** cite lawful scale transforms in **CG‑Spec**); legality follows CG‑Spec.
* **`EmitterPolicyRef`** — pointer to emitter/governor policy (C.19) applicable to this TaskSignature; **edition id** recorded.
* **`DominanceRegime`** — `{ParetoOnly | ParetoPlusIllumination}`. **Default = `ParetoOnly`** (illumination remains report‑only telemetry unless CAL explicitly authorises `ParetoPlusIllumination`, policy‑id cited).
* **`IlluminationSummary`** — a **telemetry summary over `Diversity_P`**; **published** by default; excluded from dominance unless a CAL enables `ParetoPlusIllumination` (policy‑id cited).
* **`IlluminationMap`** *(parity‑run)* — required **publication artefact** (grid/CVT/graph per `ArchiveConfig`) recording coverage per niche/cell with `DescriptorMapRef`/`DistanceDefRef.edition`. **Leaderboards as single‑score lists are forbidden**; comparisons **MUST** be under CG‑frames.
* **`PortfolioMode`** — `{Pareto | Archive}`. **Default = `Archive`**: selectors preserve retained archive evidence (QD archives) rather than a single “best” set; ε‑fronts remain admissible for local decisions under CG‑Spec.
* **`Budgeting`** — evaluation/time/batch **budgets**, including **E/E‑LOG exploration budget** id; units declared (CG‑Spec).
* **`TelemetryHooks`** — **PathSliceId**, **decay/refresh policy ids**, and **edition counters** to record **U.DescriptorMap** and **policy‑id** updates upon illumination gains.
* **`GeneratorIntent`** (OEE) — optional intent to invoke a **`GeneratorFamily`** (G.5) with pointers to **`EnvironmentValidityRegion`**, **`TransferRulesRef`**, and **coverage/regret** reporting expectations.

**Legality.** Before any numeric comparison/aggregation, **prove CSLC legality** (Scale/Unit/Polarity) and **cite CG‑Spec.Characteristics**; publish **ReferencePlane**. **Unknowns** propagate as {degrade|abstain|sandbox}; **no `unknown→0/false` coercions**.

#### C.22:5.2 - TaskSignature (S2) — attachment definition (design‑time + run‑time).
A TaskSignature is a minimal typed record the selector consumes:
`⟨Context, TaskKind, TaskFamilyRef?, KindSet:U.Kind[], DataShape, NoiseModel, ObjectiveProfile, Constraints{incl. Resource/Risk Envelopes}, ScopeSlice(G), EvidenceGraphRef, Size/Scale, Freshness, Missingness, ShiftClass?, BehaviorSpaceRef?, ArchiveConfig?, EmitterPolicyRef?, DominanceRegime?, PortfolioMode?, Budgeting?, TelemetryHooks?, GeneratorIntent?⟩`


**Minimality rule.** S2 carries only fields required for **Eligibility→Acceptance→lawful selection**; any additional traits derived at design‑time are published as provenance (UTS) but **do not expand S2**.

Values are **CHR‑typed** with **provenance**; traits may be **inferred** from CHR/CAL bindings (e.g., *convexity known? differentiable? ordinal vs interval scales?*) and from **USM** scope metadata. Unknowns are tri‑state; **Missingness semantics MUST align with CHR.Missingness** and be honored by Acceptance/Flows.

`TaskKind` names the governing kind of work or problem under this context. `TaskFamilyRef?` names one comparison-relevant family inside that task kind when specialization, transfer, or parity question is live. `TaskSignature` is the context-bound typed attachment record for one current case under that kind and scope cut. `KindSet` continues to name the described entities governed by the task kind; it is not a substitute for the task family anchor.

**DesignRunTag hygiene.** Do not mix DesignRunTag in one signature; **publish GateCrossings** as **CrossingBundles** (**E.18**; Bridge+UTS through **F.9**, **F.17**, **E.17**, and **E.18**) when importing design‑time traits into run‑time.

##### C.22:5.2.1 - Specialization-claim anchoring (normative)
Any claim that one holder, dyad, team, or explicitly scoped specialist portfolio acquired usable specialization **SHALL** anchor that claim to one declared `TaskFamilyRef` or `TaskSignature`, one named work-measure threshold target, an adaptation budget, and the freshness or provenance basis for reuse. A method may be selected, refined, or retired as part of that story, but the method is not the bearer of the specialization claim. The attached task-family record should stay rich enough for `C.22.1` adaptation signatures, `G.5` specialization profiles, and `G.9` adaptation parity to attach to the same task family and work target without reconstructing the claim from narrative prose.

Low-human-overlap or newly discovered task families remain admissible when those anchors are explicit by value.
#### C.22:5.3 - Provenance & planes.
Record **Context**, **ReferencePlane** for each value; on any cross-Context or cross-plane reuse, attach BridgeDescription + UTS row, apply **CL** (and, if planes differ, **CL^plane**) penalties to **R_eff only**; both **Φ(CL)** and (if used) **Φ_plane** MUST be **monotone, bounded, and table‑backed**; **no “distance” language; penalties never mutate F/G.** Publish policy‑ids in SCR and cite Bridge ids on crossings.

#### C.22:5.4 - Attachment & use.

* **Eligibility** gates read TaskSignature against each **MethodFamily.Eligibility** (C.23) and **CG‑Spec.MinimalEvidence** for referenced characteristics.
* **Acceptance** clauses (G.4) use these fields for **acceptance-gate threshold predicates** (acceptance-gate thresholds live in Acceptance only).
* **Selection kernel** (G.5.S3) applies a **lawful order** (often partial); **weighted sums across mixed scale types are forbidden**. If only a partial order remains, **return a Pareto (non‑dominated) set** with tie notes. If `PortfolioMode=Archive`, the selector **may** return a **QD archive** (per `ArchiveConfig`) **in addition to** or **instead of** a Pareto set. **Illumination** enters dominance **only** if `DominanceRegime=ParetoPlusIllumination` is **enabled by CAL** (policy id cited); otherwise, QD metrics are **reported** but **excluded** from dominance.
* When `GeneratorIntent` is present, G.5 may dispatch to a registered **`GeneratorFamily`** (POET‑class); the selection surface becomes **pairs** `{environment, method}`, with Environment guarded by **`EnvironmentValidityRegion`** and **`TransferRulesRef`** (C.23 wiring). Report **`IlluminationSummary`** as a **telemetry summary over `Diversity_P`** (report‑only by default) in telemetry; dominance remains unaffected unless policy changes as above.

#### C.22:5.5 - Unknowns.
Every field supports `unknown`; downstream **degrade/abstain/sandbox** behavior is explicit per Acceptance/EvidenceProfile; no implicit coercions.

#### C.22:5.6 - Publication.
Emit a **ProblemProfile** (…Description) that carries the bound TaskSignature, **UTS** Name Cards for any minted values (twin labels), and SCR‑visible provenance (A.10 anchors, lane tags, freshness, **ReferencePlane**). **Mark any vendor/tool examples as Plain‑register only (LEX V‑4); they are non‑normative.**

#### C.22:5.7 - Open‑Ended tasks (GeneratorFamily) *(normative)*.
If the problem requires **open‑ended generation** of tasks/environments, S2 **SHALL** include `GeneratorIntent` with pointers to **`EnvironmentValidityRegion`** (lawful support of generated environments), **`TransferRulesRef`** (cross‑environment transfer constraints), and **coverage/regret** telemetry expectations. Selector outputs are then declared sets over **{environment, method}**; **coverage/regret** are **telemetry metrics** (reported) and **IlluminationSummary** is a **telemetry summary** (reported), excluded from dominance unless a **CAL** policy promotes them (policy‑id recorded in SCR; see `DominanceRegime`). Edition increments of **CharacteristicSpaceRef.edition**/**DescriptorMapRef.edition**/**DistanceDefRef.edition** and (OEE) **`TransferRulesRef.edition`**, and the **policy‑id** that caused illumination increases **SHALL** be recorded in SCR.


### C.22:6 - Archetypal Grounding (Tell–Show–Show)

*Tell–Show–Show hook (per E.8):* label examples as **Show‑1 (continuous ODE)** and **Show‑2 (MIP)** and cite CHR guard‑macros in‑line so engineers can see **which field drove which gate**.  **Explicitly annotate which S2 fields triggered each Eligibility/Acceptance decision** (e.g., `service_level@ordinal → ORD_COMPARE_ONLY`, `budget@ratio → unit alignment check`).

**A. Differential equations (continuous systems, solver choice).**
*ProblemProfile.* `DataShape=ODE, stiff?=unknown, Size/Scale={n≈10^3}, ObjectiveProfile={↓error@ratio, ↑throughput@ratio}, Constraints={budget≤X, safety_gate@ordinal}, RegularityTraits={Lipschitz known?=unknown, Jacobian sparsity=high}, Missingness=MAR`.
*Attachment.* Selector reads TaskSignature; **eligibility** filters MethodFamilies that require known stiffness or differentiability (unknown ⇒ **degrade/abstain** per family); **Acceptance** enforces `safety_gate` as **ordinal predicate**, not averaged (ORD\_COMPARE\_ONLY), and budgets with **unit‑aligned sums** (ratio). The selector returns a **Pareto set**; no cross‑ordinal weighting.

**B. Mixed‑integer optimisation (planning/scheduling).**
*ProblemProfile.* `DataShape=MIP, NoiseModel=deterministic, ObjectiveProfile={↓cost@ratio, ↑service_level@ordinal}, Constraints={SLA hard, workforce soft}, RegularityTraits={convex_relaxation=available}, Size/Scale={vars~10^5}, Missingness=MCAR`.
*Attachment.* **CG‑Spec** forbids means over **service\_level** (ordinal); **Acceptance** holds acceptance-gate thresholds; **Eligibility** checks convex‑relaxation availability; **Selection** applies **lexicographic** guard (assumption‑fit ≻ evidence‑fit ≻ resource), compute **R\_eff** with Γ‑fold, route **CL** to **R** only; if partial order remains, return a **Pareto set**.

> *Contemporary anchors (informative):* modern **Julia** ecosystems illustrate the “**general call outside, specialised implementations inside**” ethos (e.g., DifferentialEquations.jl, JuMP), aligning with C.22→G.5 multi‑method dispatch under NFL.

**C. Quality-Diversity archive / declared set (illumination).**
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
* **AP‑4** **DesignRunTag chimera** signatures (mixing stances).
* **AP‑5** **Domain** treated as governance (attach governance to **U.Discipline/CG‑Spec**, not Domain).
* **AP‑6** Implicit handling of data‑shift (assume iid); **Remedy:** declare `ShiftClass` (or `unknown`) and gate via Acceptance.
* **AP‑7** Tool/vendor tokens in normative text; **Remedy:** move to Plain‑register note; keep Tech anchors on CHR/CAL ids (LEX V‑4).
**Remedies:** tri-state predicates; admissible order relations (lexi/Pareto/median/medoid); **GateCrossing visibility** via Bridge+UTS+CL/CL^plane (penalties → R only); Domain stitched to **D.CTX + UTS** only.
**Remedies:** tri‑state predicates; admissible order relations (lexi/Pareto/median/medoid); explicit **GateCrossing** publication via **CrossingBundle** (BridgeCard + UTS row + `CL/Φ` policy‑ids; **E.18/F.9/F.17/E.17/A.21** where live); Domain stitched to **D.CTX + UTS** only.

### C.22:9 - Conformance Checklist (normative)

0. **Minimal S2.** S2 contains only fields necessary for Eligibility/Acceptance/selection; any extra derived traits remain provenance.
1. **TaskSignature present (S2).** All TaskKinds **publish** a TaskSignature with all fields declared and **CHR‑typed**; `unknown` supported for each.
2. **CHR legality proven.** Any numeric comparison/aggregation **cites CG‑Spec** by **Characteristic id** and proves **CSLC legality**; **no mean on ordinals; no unit mixing**.
3. **Unknowns propagate.** Unknowns **must** map to {pass|degrade|abstain} in **Acceptance**/**Eligibility**; no implicit coercions; behavior recorded in **SCR**.
4. **Evidence lanes.** **A.10 anchors** + **Assurance lanes (TA/VA/LA)** + **freshness windows** recorded; **Γ‑fold** default=weakest‑link unless proved otherwise.
5. **ReferencePlane guarded.**  ReferencePlane noted **per value and per ObjectiveProfile head**; on crossings apply **CL** (and **CL^plane** if planes differ); **Φ(CL)/Φ_plane** are **monotone, bounded, table‑backed and documented in the `CG‑Spec`**; penalties → **R_eff only** (F/G invariant).
6. **Acceptance thresholds live in CAL.** No acceptance-gate thresholds in CHR or code paths; only in **G.4 AcceptanceClauses**.
7. **Selector legality.** Selection uses **admissible (possibly partial) orders**; **weighted sums across mixed scale types are forbidden**; return a **Pareto set** when appropriate.
8. **Crossings published (visibility).** Any cross-stance/cross-Context reuse emits **BridgeCard/BridgeDescription + UTS row** with CL notes and (if planes differ) CL^plane + Φ_plane.
9. **UTS twin labels.** All exported cards publish **Name Cards** with twin labels; Bridges carry loss notes.
10. **GateCrossing checks.** Published TaskSignature and any referenced crossings satisfy: (i) stance tagging (if used; informative only), (ii) **CrossingBundle** presence/consistency (**E.18**; **F.9**; **F.17**; **E.17**; **A.21** when gate checks are live), (iii) **LanePurity** (CL→R only; F/G invariant; Φ tables present), and (iv) **Lexical SD** (**E.10**). Failures are **blocking** under the active GateProfile / GateChecks (**A.21**).
11. **QD fields (when QD is in scope).** If `PortfolioMode=Archive` or QD heads are present, **CharacteristicSpaceRef** (d>=2), **ArchiveConfig** (topology, resolution, K, `InsertionPolicyRef`, `DistanceDefRef.edition`), and **EmitterPolicyRef** **SHALL** be present and CHR-typed; characteristics declare **ReferencePlane**.
12. **DominanceRegime default.** `DominanceRegime` **defaults to `ParetoOnly`**; inclusion of illumination in dominance **MUST** be enabled by a **CAL.Acceptance policy**; the policy id **SHALL** be published in SCR.
13. **Telemetry.** **PathSliceId**, **refresh/decay policies**, and **edition counters** for **CharacteristicSpaceRef**/**DistanceDefRef**/**EmitterPolicyRef** **SHALL** be recorded; any illumination increase **SHALL** log the **policy-id** that triggered it.
14. **GeneratorIntent (when OEE is in scope).** `GeneratorIntent` **SHALL** cite **`EnvironmentValidityRegion`** and **`TransferRulesRef`** (ids resolvable in G.5/C.23); absence => `Abstain` for OEE dispatch.
15. **Budgets.** `Budgeting` (eval/time/batch) **SHALL** declare units and E/E-LOG exploration budget id when used.
16. **Archive legality.** `DistanceDefRef.edition` and any novelty measures **SHALL** be CSLC-lawful and **editioned**; illegal ops => **Abstain**.
17. **Planes.** **ReferencePlane** **SHALL** be declared for all QD heads or characteristics; plane crossings apply **Phi\_plane** (penalty to **R** only).
18. **Unknowns.** Unknown QD fields **map** to `{degrade|abstain|sandbox}`; no coercions.

19. **Specialization claims anchored.** Any declared specialization on this TaskSignature **SHALL** name the task family/work target, named work-measure threshold target, adaptation budget, freshness or provenance basis for reuse, and enough attachment detail for `C.22.1`, `G.5`, and `G.9` to consume the same claim admissibly.

### C.22:10 - Interfaces & Data Paths

*Inputs.* `ProblemProfile` (…Description), CG-Spec ids, Evidence Graph Ref (A.10), D.CTX; (if QD) CharacteristicSpaceRef/ArchiveConfig/EmitterPolicyRef configs; (if OEE) GeneratorIntent.
 *Produces.* `TaskSignature@Context` (S2) with provenance; **SCR-visible** fields; UTS Name Cards for any minted traits; (if QD/OEE) archive / `PortfolioMode` semantics and telemetry hooks declared.
 *Consumed by.* **G.5** (Eligibility/Selection kernel), **G.4** (Acceptance/Evidence), **C.23** (admit/degrade/abstain rules; maturity ladder).

### C.22:11 - Consequences (informative)

* **Lawful selection.** Dispatch is **explainable** and **audit-ready**; every reason in/out cites TaskSignature fields, CG-Spec rows, and Gamma-fold contributors.
* **Local first, portable later.** Context-local semantics are primary; Bridges make portability **deliberate and costed** (penalties to **R** only).
* **Frictionless downstream.** G.1-G.5 consume a **single, typed** Standard; thresholds are cleanly separated into **Acceptance**; unknowns are not guessed.
* **QD/OEE-ready.** Typed QD and GeneratorIntent fields make **declared set-surface** and **open-ended** workflows **first-class**, with lawful dominance, editioned distances, and policy-aware illumination.

### C.22:12 - Relations
**Builds on:** **C.16 MM-CHR**, **G.0 CG-Spec**. **Coordinates with:** **G.4 Acceptance**, **G.5 Selector**, **C.18 NQD-CAL**, **C.19 E/E-LOG**, **C.23 Method-SoS-LOG**. **Constrained by:** **E.10 (LEX/I/D/S)**, **E.18 (GateCrossing visibility and publication gating)**.

### C.22:13 - Practical reading checks

- If two candidate approaches are answering different `TaskKind`s or different `ScopeSlice(G)` cuts, this pattern does not yet license a direct comparison.
- If specialization is the live specialization question, the task-family anchor, threshold target, adaptation budget, and provenance basis should already be recoverable from the attached `TaskSignature`.
- If crossing, normalization, or missingness changes what comparison means, publish that in the signature and its cited refs rather than hiding it in code, local memory, or later prose.
- If `QD` or `OEE` heads are in scope, archive and generator fields belong in the same typed signature rather than in a detached explanatory appendix.

### C.22:14 - Goldilocks hook (design‑time)

When generating candidate solutions for a **TaskKind**, target **“goldilocks”** slots (feasible‑but‑hard) so that the TaskSignature is informative (neither trivial nor impossible); this aligns with **G.1** (target goldilocks, abductive provenance) and ensures the **TaskSignature is informative** (neither trivial nor impossible) for **G.5** selection.

### C.22:End

## C.22.1 - Task-family adaptation signature

> **Status:** Stable

**One-screen purpose (manager-first).**
Make a specialization claim publishable as one typed adaptation record over a declared `TaskFamilyRef` or `TaskSignature`, so later selector and parity work compares the same threshold target, budget burn, prior exposure, transfer, durability, downside, and corridor-entry field rather than reconstructing that story from narrative prose.

**Builds on.** `C.22` (TaskSignature attachment and task-family anchoring), `C.19.1` (`BLP` compatibility), `A.15` (role, method, work-plan, and work-occurrence split for scout/probe work), `C.24` (`CheckpointReturn` planning semantics), `E.16` (budget enforcement).
**Coordinates with.** `G.5` (selector specialization profiles), `G.9` (adaptation parity), `G.11` (later telemetry and refresh reuse).
**Keywords.** adaptation signature; task-family specialization; time-to-threshold; budget-to-threshold; prior exposure; corridor entry; stepping stone; transfer; retention; downside field.

### C.22.1:1 - Problem frame

Final task score alone does not tell whether a holder, dyad, or bounded specialist portfolio acquired usable specialization quickly, under what budget, with what prior exposure, whether the resulting competence transferred, or whether it entered a genuinely new solution corridor. If those elements are not published together, the adaptation claim splinters across task typing, probe notes, selector prose, and parity notes, and later readers can no longer tell what exactly was being compared.

### C.22.1:2 - Problem

FPF needs one compact way to publish a bounded specialization claim on the same declared task family and work target without retyping the task anchor from `C.22` or silently pushing the adaptation-signature question into selector/parity prose.

### C.22.1:3 - Use this when

- the governed claim is not only that a holder or dyad solved a task, but how fast it acquired usable specialization on a declared task family
- comparison must stay honest about the work-measure threshold target, prior exposure, adaptation budget, transfer field, and reuse window
- movement into a new solution corridor or stepping-stone family is part of the real novelty claim

### C.22.1:4 - What goes wrong if missed

- adaptation claims collapse into vague `got better` language with no declared work-measure threshold target or budget-to-threshold account
- parity later compares outcomes that were reached under different prior exposure, different work-measure threshold targets, or different reuse windows
- nonhuman or unfamiliar solution corridors are either romanticized as novelty or dismissed as noise because the corridor entry was never typed

### C.22.1:5 - What this buys

- adaptation speed becomes reviewable by value on the same declared `TaskFamily` and work target
- later `G.5 / G.9` portfolio and parity work can compare the same specialization object instead of reconstructing it from narrative prose
- stepping-stone or solution-corridor movement becomes visible as one typed part of the adaptation claim rather than one afterthought

### C.22.1:6 - Forces

| Force | Tension |
| :--- | :--- |
| Threshold crossing vs final score | A static outcome can look similar even when one system specialized much faster or more cheaply than another. |
| Local novelty vs reproducible evidence | Corridor-entry claims matter, but they are easy to over-romanticize when no baseline or entry evidence is published. |
| Task anchor vs adaptation-signature question | The section must keep the adaptation-signature question readable without retyping task anchoring from `C.22` or turning selector/parity law into the same pattern. |
| Reuse upside vs specialization cost | Transfer, retention, and downside matter to the same claim even when the first threshold crossing looks impressive. |

### C.22.1:7 - Solution — one adaptation signature over the `C.22` anchor

- Use one shared adaptation-signature field set for this question. `G.5`, `G.9`, and later notes may cite or consume it, but they should not silently rename threshold, prior-exposure, transfer, downside, or corridor-entry terms.
- When specialization is the governed question, publish one adaptation signature bound to the declared `TaskFamilyRef` or `TaskSignature`, not one generic improvement claim.
- The signature should expose at least:
  - `thresholdTarget`
  - `timeToThreshold`
  - `budgetToThreshold`
  - `postThresholdEfficiency?`
  - `priorExposureDeclaration`
  - `transferTarget?`
  - `transferGain?`
  - `retentionWindow?`
  - `downsideEffect?`
  - `corridorEntryBaseline?`
  - `corridorEntryEvidence?`
  - `steppingStoneEvidence?`
- These fields stay anchored to the same work target and work-measure threshold semantics already declared by `C.22`, so adaptation is typed as movement toward usable specialization rather than as an ungrounded growth story.
- `C.22` continues to carry the declared task-family anchor, task typing, and baseline `TaskSignature`. `C.22.1` narrows the adaptation-signature question to threshold timing, reuse, downside, and corridor-entry disclosure over that existing anchor.

### C.22.1:8 - Corridor, transfer, and durability discipline

- If the adaptation claim depends on entering a new solution corridor, publish the `corridorEntryBaseline` first: the prior repertoire, baseline set, or comparison family relative to which corridor entry is being claimed.
- Then publish the `corridorEntryEvidence` that marks real entry into that corridor rather than exotic accident, for example a reproducible solution class, a stable descriptor shift, or one explicit stepping-stone sequence.
- If a stepping stone mattered, publish the stepping-stone evidence as part of the adaptation signature rather than treating it as retrospective color.
- Corridor or stepping-stone notes do not replace the work-measure threshold account; they explain why the adaptation path matters, not whether the threshold was actually reached.
- A fast threshold result is not yet enough to claim durable specialization.
- If transfer to a neighboring task family is claimed, name the transfer target and the observed gain explicitly.
- If retention is claimed, name the reuse or retention window rather than letting durability hide inside one isolated run.
- If specialization harms neighboring task families, narrows reusable competence, or creates de-specialization cost, publish that in `downsideEffect?` rather than telling only the upside story.
- If post-threshold performance matters to later exploitation, publish `postThresholdEfficiency?` so the claim is not trapped at the threshold-crossing moment only.

### C.22.1:9 - Worked moment

- Two agentic research setups both eventually reach an acceptable threshold on a new catalyst-search task family.
- One of them reaches threshold after a small probe budget, shows a declared transfer gain on one adjacent task family, and records that the winning path entered a previously unused solution corridor.
- The other reaches threshold only after much larger budget and without any reusable transfer.
- The adaptation signature makes that difference publishable without pretending that both runs express the same specialization story.

### C.22.1:10 - Consequences

- Threshold speed, budget burn, prior exposure, and post-threshold efficiency become part of the same reviewable object instead of one after-the-fact prose explanation.
- Selector and parity surfaces can consume a stable upstream specialization object without minting shadow vocabularies.
- Corridor-entry and downside fields stay visible in the same claim that celebrates the specialization gain, reducing romanticized novelty talk.

### C.22.1:11 - Rationale

The reader needs one place where the adaptation claim stays whole. `C.22` keeps the task family and work target explicit. `A.15`, `C.24`, and `E.16` may generate the probe, checkpoint, and budget evidence. `G.5` and `G.9` later compare several candidates or parity runs. `C.22.1` keeps the specialization story readable across those surfaces by making threshold timing, reuse, downside, and corridor-entry field recoverable in one short read instead of forcing the reader to reconstruct it from scattered notes.

### C.22.1:12 - SoTA-Echoing

**Claim 1.** Current frontier adaptation work judges usable specialization by threshold-crossing under bounded resources, not by terminal score alone.

**Practice source, local alignment, and adoption decision.** Contemporary frontier lines in refinement-heavy `QD`, self-play/task-discovery, and agentic adaptation repeatedly separate threshold target, budget burn, transfer evidence, and reuse evidence from one final benchmark score. This pattern **adopts** that practical field set, **adapts** it through one `TaskFamilyRef` or `TaskSignature`-bound adaptation signature, and **rejects** generic `got better` narratives that leave threshold and budget semantics implicit.

**Claim 2.** Current open-ended exploration work treats corridor entry and stepping stones as evidence-bearing novelty signals rather than decorative commentary.

**Practice source, local alignment, and adoption decision.** Contemporary `QD`/`OEE` and nonhuman-domain exploration lines distinguish real corridor entry from one exotic sample by asking for explicit baseline, stable descriptor shift, reproducible solution class, or an explicit stepping-stone trace. This pattern **adopts** explicit corridor baseline/evidence discipline, **adapts** it as declared adaptation-signature fields, and **rejects** novelty talk that names no baseline or evidence basis.

**Claim 3.** Current selector and parity practice needs one stable shared field set for specialization claims.

**Practice source, local alignment, and adoption decision.** Current selector and parity surfaces stay reviewable only when compared candidates reuse the same published field set for threshold, prior exposure, transfer, retention, downside, and corridor-entry field. This pattern **adopts** that reuse discipline, **adapts** it by publishing one stable adaptation-signature field set here, and **rejects** silent downstream field redefinition in `G.5` or `G.9`.

**Evidence-source note.** Peer-reviewed frontier anchors carry the most direct support for threshold, budget, and parity claims, while fast-moving frontier lines remain explicit support for corridor-entry and open-ended exploration pressure rather than a flattened single evidence-support status.

| Source-bound anchor family | What it disciplines in this pattern |
| --- | --- |
| `QD` / `OEE` corridor-entry work | Corridor baseline, descriptor shift, stepping-stone evidence, and whether novelty is reproducible rather than one exotic sample. |
| Agentic adaptation benchmarks | Threshold target, time-to-threshold, budget-to-threshold, prior exposure, and post-threshold efficiency under a declared task-family anchor. |
| Transfer / retention evaluation | Transfer target, retention window, downside, and reuse evidence so specialization speed is not confused with one isolated threshold crossing. |

### C.22.1:13 - Relations

**C.27 temporal-claim relation.**

- C.27 may flag: a claim that a holder, dyad, team, specialist portfolio, method, or agent acquires usable specialization faster on one declared `TaskFamilyRef` or `TaskSignature`.
- This pattern keeps: threshold target, time-to-threshold, budget-to-threshold, prior exposure, transfer, retention, downside, corridor-entry evidence, and adaptation-signature fields.
- Non-admissible use: generic "learns faster" wording without task-family anchors does not create a C.27 profile or a complete adaptation signature; faster threshold crossing is not durable specialization unless transfer, retention, downside, and corridor-entry evidence are stated when claimed.

- Exit: downgrade to Dyn1 trend when only a trend is live; use C.24 when the question is only tool-use planning; use C.22.1 when specialization is the governed question.

**Builds on:** `C.22` TaskSignature anchoring, `C.19.1` `BLP` compatibility, `A.15` role, method, work-plan, and work-occurrence separation, `C.24` scout/probe and `CheckpointReturn` semantics, `E.16` budget enforcement.
**Coordinates with:** `G.5` selector specialization profiles, `G.9` adaptation parity, `G.11` later telemetry/refresh reuse.
**Constrained by:** `E.10` lexical discipline and `E.19` pattern-quality review when this child section is newly landed or materially revised.

### C.22.1:14 - Not this pattern when

- the claim only needs to name the task family and work-measure threshold target, with no adaptation-speed or transfer claim at all; ordinary `C.22` anchoring is enough
- the live question is already selector or parity law across candidate selected sets; that belongs to `G.5 / G.9`
- the text cannot yet declare one work-measure threshold target, one prior-exposure stance, or one evidence basis for corridor entry

### C.22.1:15 - Conformance checklist

- `CC-C22.1-1` An adaptation signature **SHALL** bind to one declared `TaskFamily` or `TaskSignature`, one work target, and one work-measure threshold target rather than one generic improvement story.
- `CC-C22.1-2` An adaptation signature **SHALL** publish `timeToThreshold`, `budgetToThreshold`, and `priorExposureDeclaration`; if threshold was not reached, the signature **SHALL** say so explicitly instead of implying success.
- `CC-C22.1-3` Any declared transfer, retention, post-threshold-efficiency, downside, corridor-entry, or stepping-stone claim **SHALL** be explicit by value with the target, baseline, or evidence basis named, not left as narrative garnish.
- `CC-C22.1-4` This pattern may refine specialization timing and reuse claims over the declared `C.22` anchor, but it **SHALL NOT** redefine acceptance-gate thresholds, task-family attachment, or selector/parity law governed by another FPF pattern.
- `CC-C22.1-5` Downstream selector/parity surfaces **SHALL** cite or consume the same published adaptation-signature field set rather than silently redefining threshold, prior-exposure, transfer, retention, downside, or corridor-entry terms.

### C.22.1:End
## C.23 - MethodFamily Evidence & Maturity (Method‑SoS‑LOG)

*LOG (logic) for deductive shells for admissibility*
*First use expansion:* **SoS‑LOG = Science‑of‑Science LOG** (LEX short‑form discipline applied).

**RegistrationContext.** For this pattern, *RegistrationContext* means the `U.BoundedContext` where a `MethodFamily` is registered (LEX D.CTX).

**Builds on.** **G.5** (MethodFamily registry/selector), **G.4** (Acceptance & EvidenceProfiles), **C.22** (TaskSignature S2), **C.18 NQD‑CAL** (QD/illumination), **C.19 E/E‑LOG** (emitters/policies), **B.3** (Assurance lanes & `R_eff`), **A.10** (Evidence Graph Ref), **E.10** (LEX), **E.18** (GateCrossing / CrossingBundle visibility). **Coordinates with.** **G.6** (EvidenceGraph), **G.8** (LOG bundling), **G.9** (Parity), **G.11** (Refresh).

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

**R0 — CG‑Spec gate (precondition, RegistrationContext).** Before R1–R3, verify **CG‑Spec.MinimalEvidence** for every CHR characteristic referenced by *f*’s Acceptance/Flows **in the registered `U.BoundedContext`**; failure ⇒ `Abstain` with reasons (no silent sandbox). Publish the **CG‑Spec ids** consulted.
*Rationale:* selector legality requires the CG‑Spec gate to be explicit, not implicit in prose. Publish associated **ReferencePlane** notes alongside the consulted ids.

**R0.QD — QD/OEE pre‑gates (if applicable).** If S2 declares **BehaviorSpaceRef/ArchiveConfig/EmitterPolicyRef** or `PortfolioMode=Archive`, verify:
(i) **CharacteristicSpaceRef** characteristics are CHR‑typed, d≥2, **ReferencePlane** per characteristic declared;
(ii) **ArchiveConfig** is lawful (topology, resolution, **K**>0, `InsertionPolicyRef`, `DistanceDef` with **edition id** and declared metric/pseudometric status);
(iii) **EmitterPolicyRef** present (with **edition id**);
 (iv) **DominanceRegime** present; if absent, **default= ParetoOnly**.
 Failure of any ⇒ `Abstain` with reasons.

**R1 — Admit.** `Admit` **IFF**
(a) S2 satisfies **Eligibility** predicates of *f* (tri‑state aware),
(b) **EvidenceProfile minima** referenced by Acceptance/Flows for *f* are met (lanes/anchors/freshness) **in the registered `U.BoundedContext`** (post R0),
(c) all relevant **CAL.AcceptanceClauses** (G.4) evaluate to true under lawful CHR comparisons,
(d) any **maturity gating** (e.g., a floor on Maturity rungs) is expressed as an **AcceptanceClause** and referenced here by id (no thresholds inside LOG).
*LOG never sets thresholds; it only executes and cites Acceptance verdicts.*

**R2 — Degrade.** If (a) holds but (b) or (c) is **partially** satisfied or **unknown**, return `Degrade(mode)` where `mode ∈ {scope‑narrow | sandbox | probe‑only}` and **emit scope notes** (USM Scope(G), Γ_time). Record which S2 unknowns or Evidence minima caused the degrade. **LOG‑Degrade** never changes **CHR scales or planes**; it **narrows Scope (G)** or **execution mode**.
**Note (CAL vs LOG).** CAL‑level **`degrade.order`** (fall‑back to order‑only comparisons) is governed by **G.4**/**CG‑Spec** and is **not** a LOG mode. **SoS‑LOG never overrides CAL outcomes**; a LOG branch **only narrows** `Scope(G)` or **execution mode** (e.g., `sandbox`, `probe‑only`), it **does not** alter CHR scales or admissible orders.
`probe‑only` MUST cite an **E/E‑LOG policy id** (exploration budget) and Acceptance‑bound guards.

**R3 — Abstain.** If S2 violates **Eligibility** *or* **R0** fails, return `Abstain` (with reasons). **Abstain** is mandatory on **illegal CHR operations** (e.g., ordinal means) and when **Bridge/CL** requirements are unmet.

**R4 — CL routing.** Any cross-Context or cross-plane reuse must cite **Bridge ids** (with loss notes). Apply **Φ(CL)** and (if planes differ) **Φ_plane** that are **monotone, bounded, table‑backed**; **publish policy‑ids** in the SCR; **penalties reduce `R_eff` only**; **F/G must remain invariant**.

**R5 — Proof hooks.** Every branch **MUST** cite **Evidence Graph Ref** (A.10), lane tags (TA/VA/LA), freshness windows, and (if bridged) **Bridge ids + loss notes**; the decision is **SCR‑visible**. When **G.6 EvidenceGraph** is present, also **publish EvidenceGraph path id(s)** for the branch (admit/degrade/abstain). **No self‑evidence**.

**R6 — QD archive / PortfolioMode semantics (if applicable).** If `PortfolioMode=Archive`, `Admit` may return a **QD archive** (per `ArchiveConfig`) instead of only a Pareto set. Unless **CAL** authorises `DominanceRegime=ParetoPlusIllumination` (**policy‑id recorded in SCR**), **IlluminationSummary** is a **report‑only telemetry summary** and any **coverage/regret** are **telemetry metrics** (reported) that **do not** affect dominance.

**R7 — GeneratorFamily branches (open‑ended).** If S2 includes `GeneratorIntent`, SoS‑LOG **MUST**:
 (i) verify **`EnvironmentValidityRegion`** is declared and lawful;
 (ii) verify **`TransferRulesRef`** exists; if `unknown` ⇒ `Degrade(scope‑narrow)` or `Abstain` per family policy;
 (iii) treat the selection surface as **pairs `{environment, method}`**; publish **coverage/regret** and **IlluminationSummary** as **report‑only telemetry** (IlluminationSummary = telemetry summary; coverage/regret = telemetry metrics); dominance participation per **R6**.

**R8 — Telemetry & Refresh hooks.** On any illumination increase or archive change, publish **edition increments** for **CharacteristicSpaceRef**/**DistanceDefRef** and the **policy‑id** (Emitter/Acceptance) that caused the change; expose **PathSliceId** for refresh/decay in SCR.

> *Aphorism.* **“Admit on admissibility and sufficiency; degrade on uncertainty; abstain on inadmissibility.”**

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
— `MILP`: **Eligibility** requires `convex_relaxation=available`; **MaturityCard**=`L3` in the registered `U.BoundedContext` ⇒ `Admit`.
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
*Rules.* `Admit` yields declared sets over `{environment, method}`; `Degrade(scope‑narrow)` if `TransferRules`=`unknown`; telemetry publishes **coverage/regret** and **IlluminationSummary** with **edition/policy‑id** on improvements.

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
| **CC‑C23.5** | Cross-Context or cross-plane use **MUST** cite a **Bridge**; **Φ(CL)**/**Φ\_plane** **MUST** be monotone, bounded, table‑backed; penalties **→ `R_eff` only**.                                      | Keeps F/G invariant; legal CL routing.        |                                                                    |                        |
| **CC‑C23.6** | **No thresholds** in CHR or Maturity; thresholds **live only** in **AcceptanceClauses** (G.4).                                                                                             | Separation of concerns.                       |                                                                    |                        |
| **CC‑C23.7** | `MaturityCard` **SHALL NOT** be turned into a global scalar; treat as **poset**; any ordering **MUST** be lawful over CHR types.                                                           | Forbids cross‑scale scalarisation.            |                                                                    |                        |
| **CC‑C23.8** | Publish to **UTS** with twin labels; run **GateCrossing visibility checks** on cited crossings: **CrossingBundle** attestation (**E.18/F.9/F.17/E.17/A.21** where live), **LanePurity**, and **Lexical SD** (**E.10**) under GateChecks/GateProfile (**A.21**). | Publication & crossing visibility hygiene. |                                                                    |                        |
| **CC‑C23.9** | All enumerations (e.g., `Degrade(mode)`, Maturity rungs) **SHALL** declare a **closed value set** and **Scale kind**, and be registered at UTS (LEX enum clarity).                          | Avoids lexical drift; lawful typing.          |                                                                    |                        |
| **CC‑C23.10** | **RSCR tests** cover negative/refusal paths (illegal CHR ops; CG‑Spec gate fail; Bridge missing; **Φ table/policy‑id missing**; **Lexical SD violations (E.10)**); ensure **branch coverage** (Admit/Degrade/Abstain, unknown). |
| **CC‑C23.11** | If QD fields are in scope, **R0.QD** **MUST** pass: lawful **CharacteristicSpaceRef** (d≥2, characteristics typed, planes declared per characteristic), **ArchiveConfig** (topology/resolution/K, `InsertionPolicyRef`, **editioned** `DistanceDef`), **EmitterPolicyRef** present. | QD legality gate. | |
| **CC‑C23.12** | **DominanceRegime** **SHALL** default to `ParetoOnly`; switching to `ParetoPlusIllumination` **MUST** be authorised by **CAL** and cited by id in SCR.                                    | Prevents implicit scalarisation.              |                                                                    |                        |
| **CC‑C23.13** | If `PortfolioMode=Archive`, LOG **MUST** allow archive outputs (R6) and publish **IlluminationSummary** as a report-only telemetry metric unless CAL opts‑in to dominance participation.                         | Lawful archive semantics.                     |                                                                    |                        |
| **CC‑C23.14** | If `GeneratorIntent` present, **R7** **MUST** verify **EnvironmentValidityRegion** and **TransferRulesRef**; outputs are declared **{environment, method}** sets; coverage/regret telemetry published. | OEE legality & telemetry. | |
| **CC‑C23.15** | On illumination increases/archive changes, **edition increments** (BehaviorSpace/DistanceDef/EmitterPolicy) and the **policy‑id** responsible **SHALL** be logged (R8).                   | Reproducibility & refresh.                    |                                                                    |                        |

### C.23:8 - Consequences

* **Explainable admission.** Every *Admit/Degrade/Abstain* is backed by **anchored** evidence and explicit unknown handling (selector reports are SCR‑linked).
* **Run‑safe pluralism.** Multiple families can co‑exist with **policy‑governed** exploration (E/E‑LOG) and maturity‑aware gating.
* **Portable governance.** Bridge hygiene and CL routing make cross‑Tradition reuse **deliberate and costed** (penalties to **R** only).

### C.23:9 - Rationale

The ladder and LOG shells align with FPF’s **Assurance calculus**: **F** (form) is governed by artefact kind, **G** (scope) by USM slices, and **R** (reliability) accumulates via WLNK then **Φ(CL)** penalties. Treating maturity as **evidence‑typed rungs**—rather than a “score”—avoids illegal arithmetic and lets **DesignRunTag** values remain separate via `DesignRunTag` discipline (A.4) and explicit GateCrossings. This mirrors contemporary **science‑of‑science** insights: replication, benchmarking, and field health indicators are the **currency** of maturity, not anecdote.  ([Science][19])

### C.23:10 - Relations

**Builds on:** **G.5** (selector consumes these rules), **G.4** (Acceptance & EvidenceProfiles), **C.22** (S2 typing), **C.18 NQD‑CAL**, **C.19 E/E‑LOG**, **B.3** (Assurance tuple & WLNK).
**Publishes to:** **UTS** (MaturityCards, rule ids), **SCR/RSCR** (branch coverage; parity hooks).
**Constrains:** **G.8** (LOG Bundling must cite MaturityCards), **G.9** (parity harness draws baselines per rung), **G.11** (refresh windows per rung & decay), **G.5** (Open‑Ended Family mode for GeneratorFamily).
**Outcome.** The pattern introduces **new content** (LOG shells + maturity poset + degrade modes + publication Standard) and **does not duplicate** CG‑Spec legality rules, CHR guard‑macros, or CAL acceptance mechanics; it *integrates* them into **admissibility logic** for MethodFamilies.

### C.23:End

## C.24 - Agentic Tool‑Use & Call‑Planning (C.Agent‑Tools‑CAL)

> **Type:** Calculus (C)
> **Status:** Stable
> **Normativity:** Normative

**Plain-name.** Agentic tool-use and call planning.

**Intent.** Govern admissible tool-call planning and replanning under explicit budget, assurance, and policy while keeping upstream choice, pool policy, planning, and execution distinct.

**Instantiates / Refines Pillars.** `E.2` `P-3` Scalable Formality, `P-7` Pragmatic Utility, `P-10` Open-Ended Evolution, `P-11` SoTA Alignment, and the Bitter-Lesson Preference: prefer scalable, general methods that benefit from more data or compute over fragile hand-tuned heuristics when assurance and cost stay comparable.

**Depends on.** A-kernel (`A.1–A.15`) for holonic basics and Role-Method-Work separation; `B.3` Trust & Assurance (`F–G–R` with CL penalties); `E.3/E.5` (precedence and Guard-Rails); `C.5` `Resrc-CAL`; `C.18` `NQD-CAL` (candidate generation and declared set surfaces); `C.19` `E/E-LOG` (explore-exploit policies); optional `Compose-CAL` and `KD-CAL` where available.

**Coordinates with.** `U.WorkPlan` and `U.PromiseContent` bindings (acceptance gates), Working-Model publication discipline per `B.3`, and Evidence/Provenance (`G.6`).

### C.24:0 - Use this when

- one concrete choice posture already exists and the next task is now how to plan, gate, sequence, and replan tool calls admissibly
- the next lawful artifact should be one enactment-facing `CallPlan` or one `CheckpointReturn`, not one more local choice result or pool-policy result
- budget, assurance, and stop conditions must be visible before calls are burned

### C.24:0.1 - What goes wrong if missed

- calls get scheduled by ad-hoc heuristics, so the plan cannot say which budget is being burned or what event should stop or replan execution
- planning quietly collapses into execution, or execution quietly inherits unresolved upstream choice and pool-policy questions
- a successful probe is mistaken for committed rollout even though the commit trigger was never made explicit

### C.24:0.2 - What this buys

- one tool-agnostic planning record for admissible calls, budgets, stop conditions, and replan triggers
- one explicit enactment record with objective, budget, stop conditions, and next move
- one replayable call graph and assurance record instead of one opaque chain of tool invocations

### C.24:0.3 - First-minute questions

- Has one choice posture already been fixed with enough decision support that planning may begin now?
- Which budget is being burned now: enactment budget, tool-call budget, or still one upstream probe budget?
- What event stops or replans the route?
- Is the next lawful artifact one `CallPlan`, one `CheckpointReturn`, or one reroute?

### C.24:0.4 - First output

The first useful output is either one enactment-facing `CallPlan` with the current objective, cited route descriptions, the planned budget envelope, the stop or replan condition, and the next move stated explicitly in one place, or one bounded `CheckpointReturn` with the current objective or task family, the burned and residual actual budget, the commit trigger, and the recommended next action stated explicitly in one place.

If that first output still cannot be written honestly, the current planning result is not finished `C.24` planning yet.

### C.24:1 - Problem frame

Modern systems in agential roles increasingly rely on tool-call planning: selecting admissible tool-service routes, arranging intended call work, and replanning under uncertainty. Without a calculus:

* calls are scheduled by **ad-hoc heuristics**,
* **budgets** (compute, cost, wall-time) are implicit,
* **assurance** and **policy provenance** are lost, and
* systems in agential roles either over-constrain themselves with brittle scripts or wander without guard-rails.

This CAL provides the **conceptual API for thought** that lets any implementation (LLM-based, search-based, code-based, robotic) plan calls **admissibly**, **auditably**, and **scalably**. (Role-Method-Work alignment; didactic primacy.)

Immediate failure indicators for this pattern:

* the current planning result cannot say whether one choice posture already exists,
* the current text cannot distinguish route description, call plan, and executed call work,
* the budget being burned is still only probing-before-choice budget rather than enactment or tool-call budget, or
* the next lawful artifact is still undefined as one enactment-facing plan, one `CheckpointReturn`, or one reroute.

If the live question is still which fixed option should survive now, apply `C.11`. If it is still pool policy over several still-live candidate lines, apply `C.19`. If it is already public selected-set publication, apply `G.5`.

### C.24:2 - Problem
We need a **tool-agnostic** way to (i) identify **admissible route descriptions**, (ii) compose one **call work plan** that cites them, (iii) allocate an **explore/exploit** share, (iv) enforce **budget & harm** gates, and (v) **replan** on signals—**without** baking domain-specific heuristics into the core and **without** collapsing `U.MethodDescription`, `U.WorkPlan`, and `U.Work` into one object.

### C.24:3 - Forces

| Force                                    | Tension                                                                                                                 |
| ---------------------------------------- | ----------------------------------------------------------------------------------------------------------------------- |
| **General methods vs. hand-craft**       | Scalable, model-centric search ↔ short-term wins of bespoke scripts (guarded by **Bitter-Lesson Preference**).        |
| **Assurance vs. Autonomy**               | F-G-R gates & CL penalties ↔ system latitude to sequence calls and learn online.                                       |
| **Exploration vs. Delivery**             | Exploration share for illumination ↔ delivery SLAs and cost ceilings (E/E-LOG policy).                                |
| **Route vs. plan vs. execution**         | `U.MethodDescription` ↔ `U.WorkPlan` ↔ `U.Work` ↔ service promises (`U.PromiseContent`).                              |

### C.24:4 - Solution — Signature & Realization

**Types (aliases).**
*`ATC.CallRouteDescription`* ≡ `U.MethodDescription` with `accessSpec` for one tool service or callable route;
*`ATC.CallPlan`* ≡ `U.WorkPlan` specialised for intended tool-call work; it cites one or more `ATC.CallRouteDescription` editions plus planned order, budget ceilings, stop or replan triggers, and next move;
*`ATC.CallGraph`* ≡ Evidence/Provenance graph over a `U.Work` ledger;
*`ATC.Policy`* references `U.EmitterPolicyRef` (E/E-LOG) and local call gates **including BLP tolerances (alpha, delta)**.

**Roles.**
A **System in AgentialRole** prepares or revises one **CallPlan** that cites one or more **CallRouteDescription** editions. Upon enactment, a **Performer** executes **Work** (calls), and **Observers** record **Observations** with acceptance checks. Route descriptions stay design-time; the call plan stays schedule-of-intent; actual call work stays run-time. (A.15 strict distinction.)

**Operators (Gamma_agential; CAL, conceptual):**

1. `Gamma_agential.eligible(tool, TaskSignature, K_ctx) -> {true|false, notes}`
   *Eligibility gate* based on capability fit, policy allow-list or deny-list, and context K (including safety constraints).

2. `Gamma_agential.enumerate(TaskSignature, K_ctx) -> CandidateSet<ATC.CallRouteDescription>`
   Returns admissible callable route descriptions. It **MAY** delegate to **NQD-CAL** for heterogeneous route families and **MUST** apply the current **E/E-LOG lens** (objectives & telemetry) to tag candidates.

3. `Gamma_agential.plan(Objective, CandidateSet, Budget, ATC.Policy) -> ATC.CallPlan`
   Produces one **call plan** that cites the selected route descriptions, declares one planned budget envelope (compute, cost, time, risk), one intended call order, and one stop or replan policy. Internal route logic remains in the cited method descriptions; the plan is a `U.WorkPlan` that cites method descriptions, not a method description and not yet work.

4. `Gamma_agential.execute(ATC.CallPlan) -> {ATC.CallGraph, Observations}`
   Executes with **hard gates** (budget, risk, constraint-fit) and logs provenance suitable for B.3 assurance reporting (design-time and run-time separated).

5. `Gamma_agential.replan(Signals, ATC.CallPlan, BudgetPrime) -> ATC.CallPlanPrime`
   Triggered by sentinel breaches, assurance drops, or policy events; preserves editioned policy, cited route descriptions, and context.

6. `Gamma_agential.score(Route or PlanAlternative) -> <ValueProxies, Cost, Risk, FGR_floor>`
   Computes selection signals **without** illegal scalarisation across mixed scales; **uses Pareto comparison under the C.19 E/E-LOG lens** and leaves final dominance to declared policies.

#### C.24:4.1 - Bounded scout/probe cycle for unfamiliar task families

When the choice posture is already fixed enough that enactment planning is lawful, but the route across heterogeneous or unfamiliar callable approaches is still uncertain, the system may spend a bounded scout/probe budget before committed rollout and return one checkpoint package that compares the tested routes.

If additional probing could still change which option survives the current `OptionSet`, the budget is still `C.11`-side epistemic budget and the question reroutes upstream. If choice posture is already fixed and the uncertainty is only about route or rollout shape, the budget is now enactment budget and the checkpoint belongs in `C.24`.

That `CheckpointReturn` should state the declared utility target and current `TaskFamily`, the route descriptions or candidate approaches tested, the evidence on each route, the burned and residual actual budget, the recommended next action, and the exact commit trigger that would justify leaving probe state.

A successful probe does not by itself support a larger burn or a committed rollout. `C.24` carries the `CheckpointReturn` record and call-plan semantics for this probe loop; `A.15` carries the DesignRunTag split and `E.16` carries the budget partition plus guard and ledger enforcement. Low-human-overlap approaches remain sound only while they stay tied to the declared utility target, budget boundaries, and evidence basis explicitly.

**Bridge to neighboring patterns.** `ProbeBudget` belongs to `C.11` while it means epistemic budget for further probing before choice. `C.24` carries budgets once they are enactment, tool-call, or rollout budgets. If the question is still which option survives now, apply `C.11`; if it is now pool policy over several still-live candidate lines, apply `C.19`; if it is selector-facing publication of the selected result, apply `G.5`.

**Explicit enactment result.** A conformant `C.24` pass should therefore leave either one enactment-facing `CallPlan` that states the current objective, the cited route descriptions or planned call order, the planned budget envelope, the stop or replan condition, and the next move, or one `CheckpointReturn` that states the current objective or task family, the burned and residual actual budget, the evidence basis, the commit trigger, and the recommended next action.

**Unfinished-state rule.** A `C.24` result remains unfinished when it cannot say whether execution should continue now, pause at one checkpoint, or reroute, when it confuses route description with plan or plan with executed work, or when it does not state which budget is planned versus already burned and what event would stop or replan the current route.

**Normative Laws (ATC-Laws).**

* **ATC-1 (Model-the-Call, not the App).** A tool call is one **Work** instance that enacts a referenced **MethodDescription** promised by a **Service**; plans schedule intended calls and cite route descriptions but are neither the route descriptions themselves nor the calls. (A.15.)
* **ATC-2 (Bitter-Lesson Preference).** When two admissible choices are within **delta (assurance)** and **alpha (budget)**, **prefer the more general, scale-benefiting method** whose **slope vector Pareto-dominates** under the declared E/E-LOG objectives; any override **MUST** record a **BLP-waiver** with expiry. (E.2; precedence governed by E.3.)
* **ATC-3 (Budget & Harm Gates).** Plans **SHALL** declare ceilings on compute, cost, wall-time, and risk; execution **MUST** abort or replan on breach. Actual burned or residual budget belongs in `CheckpointReturn`, `CallGraph`, or other work-side reporting, not inside the plan surface.
* **ATC-4 (Explore-Share Discipline).** Plans **MUST** declare `explore_share`; defaults **inherit from E/E-LOG profiles**. **Informative defaults**: `0` for safety-critical or deterministic tasks; `approx 0.2-0.4` for ambiguous tasks with heterogeneous tool families. Promotion of illumination telemetry into dominance **requires explicit policy**.
* **ATC-5 (Provenance & Replay).** Every call **MUST** emit a **CallGraph** with: Service id, cited MethodDescription edition, inputs and outputs (redacted per privacy), `CallPlan` ref, **EmitterPolicyRef**, and budget deltas. (NQD/E/E provenance fields apply when used.)
* **ATC-6 (Assurance-First Decisions).** Selection **MUST** respect B.3: WLNK minima on F/R (weakest-link floors), CL penalties on integration, and **no** chimera scores across design-time and run-time scopes. Publish **<F,G,R>** for the typed claim `this plan is admissible under K,S`.
* **ATC-7 (Notation/Vendor Independence).** Core pattern text **MUST NOT** encode vendor-specific tokens; bindings occur in Context via Bridges/Profiles. (Lexical guard-rails.)

#### C.24:4.1a - Planning under budget must consume the same declared doctrine
#### C.24:4.1b - Causal action-use spec for call plans

When a tool-call plan selects observation, intervention, counterfactual-rung evidence collection, counterfactual policy conditioning, or off-policy causal evaluation work, the `CallPlan` carries an optional causal action-use spec and cites `C.28` for the causal-use authority.

Optional `CallPlan.causalActionUseSpec?`:

```text
CallPlan.causalActionUseSpec? {
  causalUseQuestionRef?: U.CausalUseQuestion
  targetCausalityLadderRung: CausalityLadderRung
  causalUseClaimKind: CausalUseClaimKind
  naturalBehaviorPolicyRef?: NaturalBehaviorPolicyRef
  evaluationPolicyRef?: EvaluationPolicyRef
  causalEvidenceSupportBasis?: CausalEvidenceSupportBasis
  causalInterventionSpecRef?
  counterfactualConditioningRef?
  counterfactualSamplingRealizabilityProfileRef?
  causalUseEvidenceDesignRef?
  offPolicyCausalEvaluationProfileRef?
  causalUseSupportRecordRef?: CausalUseSupportRecordRef
  causalUseSupportVerdict?: CausalUseSupportVerdict
  supportedUse: CausalUseSupportStatement
  unsupportedUse: CausalUseUnsupportedStatement
}
```

The causal action-use tail may be omitted only when the call plan does not reach `CausalUseActivation`: it is not using the call sequence as causal support, not choosing between observation/intervention/counterfactual-policy regimes, and not publishing the result as causal evidence. If the plan says the call will prove, estimate, improve, prevent, or counterfactually establish an outcome, the support tail is present or the wording is downgraded.

What changes in practice: a call plan that probes, intervenes, samples, simulates, or evaluates a policy for a causal purpose must state `CausalUseClaimKind` and the causal regime of the planned action before execution evidence is treated as support for a causal-use claim.

What this does not authorize: `C.24` does not estimate effects, prove identification, certify fairness, or turn simulation output into realized counterfactual-rung evidence; it governs admissible call planning and redirects causal-use support to `C.28`.


- Planning should reuse the declared source surface, decision lens, probe budget, and stopping posture rather than creating one planning-only choice semantics.
- Budgeted sequencing may mix exploitation and exploration, but the declared source surface and the declared reason for the next probe must stay recoverable.
- Use planning language such as `probe next`, `hold as archive`, `apply G.5 for shortlist publication`, or `stop for now` only when the relevant lens-side reason is stated directly.
- `explore_share`, `backstop_confidence`, probe budgets, and replan triggers are planning harmonization terms for that same declared choice doctrine.
- They may regulate sequence and stopping; they do not redefine `Front`, `Archive`, `Shortlist`, or `SelectionSlot`.
- If the next planned move is one public `Shortlist` or `RankedShortlist`, `C.24` should name that as a reroute target to `G.5`, not emit the selector artifact itself.

#### C.24:4.2 - Policy profile and BLP precedence

**ATC-Policy fields (conceptual).**
`{ backstop_confidence, explore_share, risk_bound, cost_ceiling, time_ceiling, tie_breakers, novelty_quota?, wild_bet_quota?, stop_conditions, BLP_delta_alpha, BLP_delta_delta }` - realised by referencing an `E/E-LOG` `EmitterPolicy` and adding Bitter-Lesson-Preference clauses. Defaults inherit from `C.19`; any deviation is editioned.

**BLP precedence.** In conflicts with tactics that hard-code narrow scripts, the Bitter-Lesson Preference applies subject to `E.3/E.5` precedence. Where scripts encode safety-critical gating or regulatory compliance, scripts prevail unless the governing context publishes the override rationale, expiry, measured hazard avoided, and planned re-evaluation window.

#### C.24:4.3 - Didactic quick card

**Agentic Call Plan (public surface).**
`Objective - Context(K) - RouteRefsInOrder[edition-pinned] - BudgetEnvelope{time/compute/cost/risk} - PolicyRef - Explore-share - Stop/Replan conditions - BLP tolerances - BLP waiver (if any) - Assurance<F,G,R|K,S> - Provenance ids`

#### C.24:4.4 - Explicit enactment outputs and closure rule

A finished `C.24` pass should publish one enactment result rather than one vague statement that the system now has a plan.

Two output shapes are lawful here:

- one enactment-facing `CallPlan`; or
- one bounded `CheckpointReturn` when probing is still the lawful next move inside enactment planning.

A `CallPlan` should state at least these fields:

- current objective;
- cited route descriptions or planned call order;
- active policy or planning posture;
- planned budget envelope or reserved budget;
- stop or replan condition;
- next move if the current plan is accepted now.

A `CheckpointReturn` should state at least these fields:

- current task family or objective;
- candidate routes tested so far;
- evidence on those routes;
- burned and residual actual budget;
- recommended next action;
- explicit commit trigger.

A compact result may therefore look like:

```text
CallPlan(
  objective = answer_question_Q,
  policyRef = ee_policy_v1,
  routeRefsInOrder = [search_route_v3, retrieve_route_v1, synthesize_route_v2, code_check_route_v1],
  plannedBudgetEnvelope = {time<=60_minutes, compute<=x1, cost<=y1, risk<=r1},
  stopOrReplan = low_R_or_cost_ceiling,
  nextMove = enact_now
)
```

or:

```text
CheckpointReturn(
  taskFamily = unfamiliar_lab_protocol,
  testedRoutes = [route_A, route_B],
  burnedBudget = 2_runs,
  residualBudget = 1_run,
  recommendedNextAction = probe_route_B_once_more,
  commitTrigger = route_B_clears_assurance_floor_L1
)
```

Close as one enactment-facing `CallPlan` when the choice posture is already fixed enough that execution order, gating, and replanning are now the governed question. Close as one `CheckpointReturn` when bounded scout/probe work is still lawful inside enactment planning. Reroute when the result has actually fallen back into local choice, pool policy, or selector-facing publication.

If the result still does not state what should execute now, what budget is planned or already burned, and what event stops or replans the route, it is still unfinished `C.24` work.

#### C.24:4.4a - Worked closure slice

Two short contrasts keep the closure law practical.

**Known route, execution should begin now.**
When the objective and route are already fixed enough, `C.24` should close as one enactment-facing call plan:

```text
CallPlan(
  objective = produce_patch_and_verify,
  routeRefsInOrder = [inspect_repo_route, edit_candidate_route, run_targeted_tests_route],
  plannedBudgetEnvelope = {time<=45_minutes, compute<=x2, cost<=y2, risk<=r2},
  stopOrReplan = targeted_tests_fail_twice,
  nextMove = enact_now
)
```

**Unfamiliar route, one bounded scout pass still lawful.**
When the route is still uncertain inside enactment planning, `C.24` should close as one `CheckpointReturn`:

```text
CheckpointReturn(
  taskFamily = unfamiliar_ci_failure,
  testedRoutes = [log_trace_route, minimal_repro_route],
  burnedBudget = 1_probe_cycle,
  residualBudget = 2_probe_cycles,
  recommendedNextAction = run_minimal_repro_once_more,
  commitTrigger = repro_is_stable_and_assurance_floor_L1_holds
)
```

The practical distinction is simple: if route order and budgeted execution are already the governed question, emit one `CallPlan`; if bounded scout work is still the governed question inside planning, emit one `CheckpointReturn`.

1. **Research-assistance system in agential role.**
   Task: answer a novel technical question. Candidate tools: retrieval, structured web search, code runner, table or plot generator.
   **Plan:** cite route descriptions for `search`, `retrieve`, `synthesize`, and `code_check`; declare `explore_share approx 0.4`; replan on sentinel `low_R`.
   The lawful structure here is one declared budget envelope, one explicit route order, and one visible replan trigger.

2. **Program-repair system in agential role.**
   Task: propose a patch against a failing test suite. Candidate tools: repo introspection, static analyzer, unit runner.
   **Plan:** keep repo-introspection, patch-application, and targeted-test route descriptions distinct; use scout quota across patch families before committed rollout.

3. **Lab-automation system in agential role.**
   Task: adjust a wet-lab protocol under drift. Candidate tools: planner, pipetting controller, spectrometer, Bayesian optimizer.
   **Plan:** a bounded probe or pilot can inform the route, but committed rollout waits for the declared commit trigger and assurance floor.

### C.24:6 - Bias-Annotation

Lexical firewall and notation independence apply; no vendor tokens; mixed-scale characteristics are never averaged; route descriptions remain distinct from `U.WorkPlan`, and both remain distinct from executed `U.Work`; a successful probe remains distinct from committed rollout until the commit trigger is satisfied.

### C.24:7 - Conformance Checklist

1. **CC-ATC-1 - Declared separation.** `ATC.CallRouteDescription` is a `MethodDescription`; `ATC.CallPlan` is a `U.WorkPlan` that cites route descriptions; execution is `Work`; acceptance is via `U.PromiseContent`. No method-side route logic or actual burn is smuggled into the `U.WorkPlan` surface.
2. **CC-ATC-2 - Budgets on record.** `time/compute/cost/risk` ceilings exist ex ante; stop conditions listed.
3. **CC-ATC-3 - E/E policy.** `EmitterPolicyRef` (or equivalent) and `explore_share` are editioned and logged.
4. **CC-ATC-4 - Assurance tuple.** Publish the typed claim `Plan admissible under K,S` with `<F,G,R>` and CL penalties traceable in the `CallGraph` SCR. Design-time and run-time never merged.
5. **CC-ATC-5 - BLP waiver discipline.** Any heuristic override against a general method includes expiry and re-evaluation date.
6. **CC-ATC-6 - Provenance minimum.** Record `{PromiseContentRef, CallPlanRef, MethodDesc.edition, EmitterPolicyRef, DescriptorMapRef? (if NQD), DistanceDefRef? (if NQD), TimeWindow, Seeds?, Dedup?}`.
7. **CC-ATC-7 - Notation independence.** No vendor tokens in conceptual text; bindings via Bridges or Profiles only.
8. **CC-ATC-8 - BLP tolerances declared.** `alpha/delta` tolerances are present in `ATC.Policy` or referenced via the active `E/E-LOG` profile.
9. **CC-ATC-9 - `CheckpointReturn` for bounded specialization.** When one route still uses scout/probe discipline on a new task family, it SHALL publish one `CheckpointReturn` with candidate routes, evidence, burned/residual actual budget, next action, and commit trigger; a successful probe alone never counts as committed rollout.
10. **CC-ATC-10 - Recoverable enactment closure.** When `C.24` returns one enactment-facing call plan or one `CheckpointReturn`, the `CallPlan` SHALL state current objective, route refs in order, planned budget envelope, stop or replan condition, and next move, while `CheckpointReturn` SHALL state burned/residual actual budget plus next action and commit trigger.
11. **CC-ATC-11 - Neighboring-pattern boundary.** If the live question is still fixed-option choice, pool policy over several live lines, or selector-facing publication, `C.24` SHALL apply `C.11`, `C.19`, or `G.5` rather than restating those patterns.
12. **CC-ATC-12 - Role discipline.** User-facing prose and emitted artifacts SHALL speak about systems in agential roles or equivalent typed performers, not one generic `agent` head, when that generic head would blur the holder kind.
13. **CC-ATC-13 - Causal action-use spec.** If one `CallPlan` selects observation, intervention, counterfactual-rung evidence collection, counterfactual policy conditioning, or off-policy causal evaluation for a causal purpose, it SHALL carry `CallPlan.causalActionUseSpec?` with `targetCausalityLadderRung`, `causalUseClaimKind: CausalUseClaimKind`, supported use, unsupported use, and a `C.28` causal-use support reference rather than letting call-planning vocabulary certify the causal claim.


### C.24:8 - Common Anti-Patterns and How to Avoid Them

- **Treating route description as plan.** Avoid by keeping callable logic in `ATC.CallRouteDescription` and keeping `ATC.CallPlan` as one `U.WorkPlan` that cites it.
- **Treating planning as execution.** Avoid by publishing actual burn only through `CheckpointReturn`, `Work`, and `CallGraph`, not inside the plan surface.
- **Burning enactment budget while the live question is still upstream choice or pool policy.** Avoid by rerouting unresolved fixed-option choice to `C.11` and unresolved live-pool governance to `C.19` before building one call plan.
- **Counting a successful probe as committed rollout.** Avoid by publishing one `CheckpointReturn` with a visible commit trigger instead of smuggling rollout through a positive scout result.
- **Hiding stop conditions or replan triggers.** Avoid by making them part of the public plan surface rather than one private implementer intuition.

### C.24:9 - Consequences

- tool use under systems in agential roles becomes inspectable as one lawful plan, not one opaque sequence of calls
- downstream work receives one explicit enactment record with objective, route refs, budget envelope, stop conditions, and next move
- the cost is stricter discipline around route-description versus plan versus work separation, explicit budgets, and visible policy posture before execution begins

### C.24:10 - Rationale

`C.24` exists because tool-use systems fail in a distinctive way: they can look adaptive while actually hiding route choice, budget burn, stop conditions, and replan logic inside one opaque execution chain. A separate planning calculus is therefore necessary so that tool use remains auditable, replayable, and governable before the first irreversible call is made.

- Contemporary tool-use systems in agential roles work best when planning, feedback, and replanning stay explicit rather than collapsing into one brittle script. The practical implication is to publish one `U.WorkPlan` that cites route descriptions and carries stop or replan triggers before execution.
- Post-2015 search, optimization, and agentic systems also show that bounded probing is useful but dangerous when it silently becomes commitment. The safeguard here is the explicit `CheckpointReturn` plus visible commit trigger and one explicit split between planned budget envelope and burned actual budget.
- Scaling-first practice favors general, learnable methods over fragile hand-tuned tactics when assurance and cost remain comparable. The practical implication is not blind optimism but disciplined BLP: when a narrow heuristic wins, record the waiver, expiry, and re-evaluation window.

### C.24:12 - Relations

**C.27 temporal-claim relation.**

- C.27 may flag: a tool-use plan claiming that tool use changes debugging, learning, search, repair, rollout, narrowing, uncertainty reduction, stabilization, or stop/replan rate.
- This pattern keeps: call planning, tool-use sequence, budget, stop/replan, and work trace.
- Non-admissible use: tool-call count, more context, or faster narrowing is effort evidence or input evidence at most; it is not task-success, reasoning-quality, evidence-quality, repair-success, cost, or validity-window evidence by itself.

- Exit: a speed-up claim names task outcome, evaluation harness, repair-success basis when claimed, cost or budget posture, validity window, stop or replan condition, and non-admissible use as a benchmark claim; C.24 remains the tool-use pattern.

Builds on: `A.15` Role-Method-Work alignment (planning vs execution vs service), `B.3` Trust & Assurance (`F-G-R/CL`), `C.5 Resrc-CAL`, `C.18 NQD-CAL` (candidate generation and declared set surfaces), and `C.19 E/E-LOG` (policies). Coordinates with `C.28` when a call plan is used to observe, intervene, collect counterfactual-rung evidence, condition a counterfactual policy, or evaluate a policy for causal-use support. Constrains: any `U.PromiseContent` used as a tool MUST expose acceptance conditions and observation hooks sufficient for `B.3` reporting. Enables: human-facing Working-Model surfaces with policy and assurance disclosures while keeping design-time and run-time separated.

### C.24:End


## C.25 - Q-Bundle: Authoring "-ilities" as Structured Quality Bundles

> **Type:** Definitional (D)
> **Status:** Stable
> **Normativity:** Normative unless marked informative

**Plain-name.** Quality-bundle normal form.

**Builds on.**
`A.2.6` (USM scope algebra), `A.6.1 U.Mechanism`, `C.16 MM-CHR`, `A.18 CSLC`, `B.3 Trust & Assurance Calculus`.

**Coordinates with.**
`C.17-C.19` for quality-related measurement families, `A.15` for method, work-plan, or work-occurrence gating, and `A.6.Q` for evaluative classification into explicit quality endpoints.

### C.25:1 - Problem frame

Engineering quality language repeatedly drifts into one of two invalid simplifications: either every `-ility` is treated as one scalar characteristic, or every engineering-quality statement is left as loose evaluative prose. A conforming engineering corpus therefore needs a uniform discipline that keeps lawful measurements, scope declarations, mechanisms, statuses, and evidence visibly separated without inventing a new kernel ontology.

### C.25:2 - Problem

Without a normal form for engineering quality families:

1. **Composite families are scalarized illegally.**
   Terms such as *resilience*, *security*, or *maintainability* are treated as if one number exhausted them.
2. **Scope is confused with measurement.**
   A claim's `ClaimScope` / `WorkScope` is spoken of as if it were a magnitude rather than a USM set-valued applicability object.
3. **Mechanism and status are mistaken for evidence or metrics.**
   Presence of redundancy, certification, or audit controls is described as if it were itself a measurement value.
4. **Guards become unstable.**
   Admission checks silently mix scope coverage, numerical thresholds, mechanism presence, and evidence freshness in one phrase.
5. **Evaluative routing remains underspecified.**
   After `A.6.Q` repairs a bare quality term, the admissible endpoint is unclear unless FPF distinguishes single-CHR cases from bundle-shaped quality families.

### C.25:3 - Forces

| Force | Tension |
|---|---|
| **Simplicity vs category hygiene** | Authors want one convenient quality label; the framework must still keep CHR, USM, mechanism, and status roles distinct. |
| **Comparability vs local applicability** | Measures should compare legally across contexts, while scope remains context-local and set-valued. |
| **Thin ontology vs practical authoring** | The pattern should regularize quality authoring without creating a new heavy kernel family for every `-ility`. |
| **Endpoint clarity vs expressive breadth** | Some quality terms really are one characteristic; others are bundles. The endpoint rule must cover both without ambiguity. |

### C.25:4 - Solution - Q-Bundle normal form

`C.25` defines a lightweight authoring normal form for engineering quality families. A publisher facing a quality term first decides whether the intended endpoint is:

- **one lawful CHR characteristic**, or
- **one structured quality bundle** whose measurable slots, scope slots, mechanisms, statuses, and evidence remain explicit.

#### C.25:4.1 - Endpoint split

Use a **single `U.Characteristic`** when the quality claim is genuinely one measurable aspect with one declared scale and ordinary CHR legality.

Use a **Q-Bundle** when the quality family depends on more than one of the following:

- one or more measurable characteristics,
- a declared claim/work scope,
- mechanism or status requirements,
- qualification windows,
- evidence anchors that are not reducible to one scalar.

#### C.25:4.2 - Q-Bundle shape

`Q-Bundle := <Name, Carrier, ClaimScope?, WorkScope?, Measures[CHR], QualificationWindow?, Mechanisms?, Status?, Evidence?>`

The pattern adds no new Kernel kind for these slots. It reuses existing kinds and keeps them in one disciplined authoring surface.

#### C.25:4.3 - Field roles

- **Name.** The engineering quality family label, such as `Availability`, `Resilience`, or `Security`.
- **Carrier.** The bearer of the quality claim: typically `U.System`, `U.PromiseContent`, or `U.Episteme`.
- **ClaimScope / WorkScope.** USM sets over `U.ContextSlice` describing where the claim holds or where the capability can deliver. These are **set-valued scope objects**, not characteristics.
- **Measures[CHR].** One or more lawful CHR characteristics, each bound to one declared scale.
- **QualificationWindow.** The temporal policy under which the quality claim is judged.
- **Mechanisms / Status.** References to `U.Mechanism` realizations, control presences, certification states, or similar gating structures. They are not measurements.
- **Evidence.** Anchors that justify the measures, mechanisms, or scope claims.

#### C.25:4.4 - Guard reading

A conforming quality guard typically has the conceptual form:

`Scope covers TargetSlice AND Measures meet thresholds AND QualificationWindow is valid AND required Mechanisms/Status are present`

This keeps coverage, thresholding, and admissibility in separate typed slots instead of hiding them inside one quality adjective.

### C.25:5 - Archetypal Grounding

**Tell.** A quality family is not automatically one metric. Sometimes it is one characteristic; often it is a structured bundle whose measurable, scope, and mechanism slots must remain explicit.

**Show (Availability).** Availability may be authored as one CHR-centric bundle with `AvailabilityRatio[%]` as the principal measure, a declared service/time scope, and explicit redundancy mechanisms. The measure is scalar; the scope is not.

**Show (Resilience / Security).** Resilience or security usually requires more than one measure, plus scenario scope, mechanism references, and qualification windows. Treating either as one scalar "quality score" erases the bundle structure that the claim actually needs.

### C.25:6 - Bias-Annotation

The pattern biases authors toward explicit decomposition. That bias is intentional. It is better to publish a visibly structured quality bundle than to gain short-term convenience by collapsing scope, measures, and mechanisms into one overloaded quality label.

### C.25:7 - Conformance Checklist

- `CC-C.25-1` If an engineering quality claim is intended as one measurement characteristic, the publisher **SHALL** bind it to one named `U.Characteristic` with one declared scale.
- `CC-C.25-2` If the claim requires multiple measures, scope slots, mechanism slots, status slots, or qualification windows, the publisher **SHALL** use a Q-Bundle rather than an undeclared scalar surrogate.
- `CC-C.25-3` `ClaimScope` and `WorkScope` **SHALL** remain USM set-valued scope objects; they **MUST NOT** be treated as ordinal or numeric quality levels.
- `CC-C.25-4` Mechanism or status slots **MUST NOT** be conflated with `Measures[CHR]`.
- `CC-C.25-5` Any scalar comparison or thresholding inside a Q-Bundle **SHALL** apply only to declared CHR measures, not to scope slots.
- `CC-C.25-6` Cross-context penalties and bridge losses **SHALL** route to `R` per `B.3` / `F.9`; they **MUST NOT** silently alter the type of the bundle's `F`, scope, or CHR type authority.

### C.25:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | What it looks like | How FPF prevents it |
|---|---|---|
| **One-number `-ility`** | `Resilience = 82` with no declaration of what is being measured and what scope/scenario is intended. | `CC-C.25-2` requires a Q-Bundle when the family is composite. |
| **Scope as metric** | The claim treats wider applicability as a higher quality value rather than as a larger USM set. | `CC-C.25-3` keeps scope set-valued and non-CHR. |
| **Mechanism equals quality** | Presence of a mechanism or certificate is reported as if it were the measurement itself. | `CC-C.25-4` keeps mechanism/status slots distinct from measures. |
| **Collapsed guard prose** | One sentence mixes coverage, thresholds, windows, and mechanisms without typed separation. | `C.25` rewrites the claim into explicit slots and typed guard factors. |

### C.25:9 - Consequences

| Benefit | Trade-off / Mitigation |
|---|---|
| **Category hygiene.** Scope, measurement, mechanism, and status no longer collapse into one term. | Slightly heavier authoring surface; mitigation: only composite cases need the full bundle. |
| **Portable comparison.** CHR measures compare legally, while scope remains governed by USM set algebra. | Authors must declare scales and scope explicitly. |
| **Cleaner gating.** Method/work guards can read the same structure without hidden semantics. | Requires discipline in separating guard factors. |
| **Better endpoint classification.** `A.6.Q` can terminate in either one characteristic or one Q-Bundle with a clear endpoint pattern. | Requires a first-pass endpoint decision during authoring. |

### C.25:10 - Rationale

Engineering quality language is useful precisely because it groups recurring concerns under memorable family labels. The same grouping becomes dangerous when those labels are mistaken for one universal metric. `C.25` preserves the family labels but forces the underlying structure to stay typed and visible.

### C.25:11 - SoTA-Echoing

Contemporary engineering quality practice routinely mixes service-level measures, capability windows, scenario envelopes, mechanism presence, certification state, and evidence traces. `C.25` adopts that practical richness but refuses the common shortcut of compressing the whole family into one undefined score.

### C.25:12 - Relations
**C.27 temporal-claim relation.**

- C.27 may flag: a quality-family statement where agility, resilience, adaptability, recovery, or robustness depends on braking, redirection, stabilization, recovery rate, or rhythm under effort.
- This pattern keeps: quality-family bundle structure, scope, mechanism/status slots, evidence, qualification window, and failure mode.
- Non-admissible use: temporal adequacy is not quality adequacy; speed, recovery, or rhythm becomes quality content only when C.25 declares the quality family, scope, mechanism/status slots, evidence, and failure mode.
- Exit: use C.27 to state the dynamic slot only when it changes admissible use; do not make every quality bundle carry dynamic slots.

- **Builds on:** `A.2.6` for scope algebra, `A.6.1` for mechanism references, and `C.16 / A.18` for CHR legality.
- **Coordinates with:** `C.2.2a`, `A.16.0`, `B.3` for assurance penalties, `A.15` for gate use, `A.6.Q` for evaluative classification, `C.17, C.18, and C.19` for adjacent quality-family measures, and `F.9 / F.9.1` when cross-context bundle comparison or bridge stance annotation is required.
- **Constrains:** engineering quality authoring whenever a quality term would otherwise drift between single-CHR and composite-bundle readings.
#### C.25:12.1 - Endpoint role in evaluative classification

Within language-state trajectories and their endpoint docks, `C.25` is the system-side endpoint pattern for engineering quality families after evaluative classification from `A.6.Q`. `evaluativeAscription(...)` may remain a transitional repair record, but it is **not** the universal resting place when the admissible endpoint is a single `Characteristic`, a `Q-Bundle`, or an explicit objective-oriented quality bundle.


### C.25:13 - Decision Test: Single Characteristic or Bundle?

The most common authoring failure is not in the bundle syntax itself; it is in choosing the wrong endpoint shape. The quickest useful test is to ask what would make the quality claim false.

#### C.25:13.1 - Use one `U.Characteristic` when

A quality claim should terminate in one lawful CHR characteristic only when all of the following hold together:

- one measurable aspect is actually doing the evaluative work,
- one declared scale is enough to compare relevant cases,
- the bearer and scope are already clear without introducing extra quality slots,
- mechanism or status presence is not itself part of the core quality head,
- and downstream gates can read the claim without needing a bundle decomposition.

Examples include a narrowly declared `AvailabilityRatio[%]`, a specific latency percentile, or one response-time threshold under one fixed window.

#### C.25:13.2 - Use a `Q-Bundle` when

A quality claim belongs in `C.25` when one family label is standing over several distinct typed concerns, for example:

- several measures are needed together,
- scenario or claim scope is load-bearing,
- mechanism presence or certification state constrains admissibility,
- qualification windows alter the reading materially,
- or one scalar head would hide which part of the family is actually failing.

The bundle is not a fallback for laziness. It is the explicit authoring form for claims whose truth conditions are already composite.

#### C.25:13.3 - Borderline cases

Some quality families contain both a bundle-shaped form and a narrow single-characteristic form. For example, a service team may use:

- one CHR characteristic for a very narrow uptime commitment, and
- one Q-Bundle for the broader service-availability family that includes scope, windows, failover mechanisms, and evidence.

This is legitimate as long as the text states clearly which head is currently in play. The single-characteristic form does not replace the broader family; it selects one evaluative slice of it.

### C.25:14 - Slot Interaction Law

The practical payoff of `C.25` is not just that it names the slots. It also stabilizes how those slots interact.

#### C.25:14.1 - Scope and measure remain orthogonal

`ClaimScope` and `WorkScope` answer **where** or **under what contextual slice** the quality claim holds. `Measures[CHR]` answer **how** a measurable aspect behaves. A broader scope is not a larger measurement value; a narrower scope is not a penalty value. Scope is governed by set inclusion and coverage, not by scalar order.

#### C.25:14.2 - Mechanism and status are gating slots

Mechanisms and statuses may be load-bearing for admissibility, but they do not become measurements merely because they matter. A redundancy mechanism may be required for claiming a resilience bundle, and a certification status may be required for external publication, yet neither slot is itself the `Measures[CHR]` head.

This matters because many quality arguments fail by turning mechanism presence into an implicit hidden score.

#### C.25:14.3 - Qualification windows are not decorative

A quality claim that depends on rolling windows, observation periods, maintenance intervals, or disruption horizons must publish that temporal qualifier explicitly. If the truth of the quality claim changes when the window changes, then the window is part of the declared bundle record rather than optional commentary.

#### C.25:14.4 - Report-only summary proxies

A publisher may compute a report-only summary proxy for convenience, for example a compact quality summary-surface value or an oversight-facing composite score. Such a proxy is lawful only if:

- it is explicitly declared as a **report-only proxy**,
- the underlying bundle slots remain visible,
- and no norm, gate, or bridge silently substitutes the proxy for the bundle itself.

This prevents a convenience summary from becoming a covert replacement for the typed quality claim.

### C.25:15 - Worked Quality Families

#### C.25:15.1 - Availability family

A narrow service commitment may use `AvailabilityRatio[%]` as one characteristic. A broader availability family usually still needs a bundle because the claim depends on:

- declared service and time scope,
- observation and qualification window,
- one or more mechanism slots such as failover or redundancy,
- and evidence tying the measurement to declared observation conditions.

The bundle form makes it possible to distinguish "the measurement fell short" from "the measurement is fine but the declared mechanism prerequisite was absent".

#### C.25:15.2 - Resilience family

Resilience is almost never one scalar. It commonly binds together:

- disruption scenario scope,
- restoration-related measures such as `MTTR`, `RTO`, or `RPO`,
- recovery mechanisms and preparedness states,
- and scenario-specific evidence about drills, restorations, or incident traces.

Trying to compress this into a single resilience value usually destroys the difference between fast recovery in one scenario and structural fragility in another.

#### C.25:15.3 - Security family

Security claims routinely combine:

- trust-zone or attack-class scope,
- measurable characteristics such as patch latency, control coverage, or response interval,
- control-set and certification slots,
- and evidence from audit, observation, or incident review.

`C.25` therefore treats broad security-family claims as bundle-shaped unless the claim has already been narrowed to one admissible CHR characteristic.

#### C.25:15.4 - Maintainability and evolvability

Maintainability or evolvability claims often drift into pure rhetoric. In `C.25`, they become usable only when the publisher separates:

- the declared scope of systems or change classes,
- the measurable slots (for example change lead time, defect reintroduction rate, restoration interval, review load),
- the enabling mechanisms (modularity rules, test harnesses, interface discipline),
- and the window or evidence conditions under which those measures were observed.

This is exactly the kind of quality family that looks scalar in speech but turns composite once the claim is made explicit.

### C.25:16 - Authoring and Review Guidance

#### C.25:16.1 - For authors

Authors should begin with the question: *what is the actual head of this quality claim?* If the truthful answer is "several measures plus scope plus mechanism constraints," start with a bundle and narrow only if a later slice genuinely deserves one CHR head.

A useful authoring order is:

1. name the family label,
2. identify the bearer,
3. publish scope,
4. publish measures,
5. add mechanism/status slots,
6. publish qualification window,
7. bind evidence,
8. and only then consider whether a report-only summary proxy is needed.

#### C.25:16.2 - For assessors

A checking reader should ask:

- whether the chosen endpoint shape is lawful,
- whether any scope slot has been smuggled into scalar language,
- whether mechanism presence has been mistaken for a metric,
- whether the window is truly optional or actually load-bearing,
- and whether any summary proxy is trying to replace the underlying bundle.

In practice, most defects are visible as soon as the checking reader asks what exactly one reported number stands for.

#### C.25:16.3 - For gate designers and assurance leads

Gate designers should resist writing guards against vague family labels such as *resilience must be high*. A conforming gate should instead name the relevant bundle slots:

- coverage over the target slice,
- threshold satisfaction on declared measures,
- qualification-window validity,
- and any required mechanism or status slots.

This keeps the gate auditable and prevents later disputes about what the family label was supposed to mean.

### C.25:17 - Migration and Boundary Notes

#### C.25:17.1 - Migration from bare quality requirements

Legacy phrases such as *quality requirement*, *security requirement*, or *availability requirement* should not survive as bare heads when the underlying endpoint is actually a characteristic or bundle. The migration rule is:

- choose the endpoint shape first,
- then bind the requirement or commitment to that explicit head.

`A.6.Q` may still be the entry repair, but `C.25` is the resting place once the engineering quality family has been made explicit.

#### C.25:17.2 - Boundary to assurance penalties

Cross-context transport, bridge loss, or plane mismatch do not change whether the endpoint is one characteristic or one bundle. Those effects route to `R` and its penalties. `C.25` therefore should not be used to hide assurance degradation inside the quality-family ontology.

#### C.25:17.3 - Boundary to publication convenience

A report, summary surface, or executive summary may expose only one slice of a Q-Bundle, but the underlying authoring structure remains the bundle. Publication convenience is not a reason to collapse the ontology at the source.

#### C.25:15.5 - Serviceability and supportability

Serviceability, supportability, and adjacent family labels often look simple in prose but become composite as soon as operational use is declared. A lawful bundle for this family may need:

- support-scope slices,
- measured restoration or service intervals,
- mechanism slots for support mechanisms, access discipline, or replacement procedures,
- and evidence from service traces or support records.

The lesson is the same as elsewhere in `C.25`: once the truth of the family claim depends on several typed contributors, the bundle should stay explicit.

#### C.25:17.4 - Boundary to description-side and selector-side evaluation

`C.25` is for engineering quality families whose bearer is a system-side, promise-side, or explicit quality-bearing artifact. It does **not** automatically cover:

- viewpoint-fit or architecture-description adequacy claims, which may belong in viewpoint or evaluative-ascription patterns,
- or selector/objective heads where *quality* means use-value under a search or portfolio frame.

This boundary matters because the same word *quality* appears across those zones. `A.6.Q` may be the common repair entry, but the resting endpoint depends on what is actually being evaluated.
### C.25:18 - Bundle Decomposition and Comparison Law

#### C.25:18.1 - Local decomposition rule
A family label may remain stable while its internal slots differ materially across contexts. Conforming comparison therefore starts by aligning the bundle decomposition: scope slots with scope slots, measure slots with measure slots, mechanism/status slots with their own kinds, and evidence/window slots with their own kinds. Comparing one bundle's measure directly to another bundle's mechanism claim is a category error even if both sit under the same family label.

#### C.25:18.2 - Narrow slice versus whole family
A context may admissibly extract one narrow slice from a broader Q-Bundle and publish that slice as a single CHR characteristic, but the publication should say that the slice is only one member of the broader family. What is not admissible is to report the slice as though it exhausted the entire family claim.

#### C.25:18.3 - Cross-context family comparison
Cross-context comparison of quality families should proceed through explicit bundle alignment and, where needed, `F.9` bridge discipline on the relevant heads or slots. The bundle ontology stays in `C.25`; bridge loss, translation-relation adequacy, and cross-context penalties remain outside the bundle itself.

### C.25:19 - Gate, Proxy, and Reporting Discipline

#### C.25:19.1 - Report-only summary proxy
A context may publish a summary proxy for reporting convenience, but the proxy remains secondary to the Q-Bundle. The proxy should state what it summarizes and what it leaves out. No report-only proxy may replace the bundle in norms, gates, or endpoint ontology.

#### C.25:19.2 - Gate binding rule
When a gate uses a quality family, the gate should bind to explicit bundle slots: declared scope, specific measures, qualification window, and any required mechanism or status slots. Gate authors should not rely on the family label alone, because labels invite different local decompositions.

#### C.25:19.3 - Roll-up caution
A summary publication or review may aggregate several bundle instances, but the roll-up must remain visibly downstream from the underlying bundle structure. If the roll-up begins to drive local engineering decisions directly, the governing bundle slots should be surfaced again rather than hiding them behind one summary score.

### C.25:20 - Review Matrix and Migration Tests

A checking reader can test a Q-Bundle with five questions:

1. **Is the endpoint shape admissible?** One characteristic where one characteristic is live, one bundle where several typed contributors are load-bearing.
2. **Are scope and mechanism slots kept distinct from measures?**
3. **Is any summary number trying to replace the bundle?**
4. **Would a gate still be auditable if the family label were removed?**
5. **If the claim crosses contexts, is bridge work kept in `F.9` rather than hidden inside the family bundle?**

Migration from legacy family prose should therefore recover bundle shape first, then choose whether any narrow slice deserves a separate CHR publication.

### C.25:20a - Viability-envelope, quantum-like, and temporal-claim relation note

Use `C.25` when the live question is a quality bundle, "-ility" decomposition, proxy metric, trade-off, gate, or report. A viability claim should not become quantum-like merely because it involves uncertainty, feedback, several qualities, or changing operating conditions; a temporal claim should not become a Q-Bundle merely because the working phrase mentions speed, cadence, rhythm, or recovery.

Practical reading:

1. Decide whether the quality claim is one lawful Characteristic or a Q-Bundle.
2. If it is a bundle, name bearer, scope, measures, qualification window, mechanisms/status, and evidence.
3. Ask whether the claim is really viability-envelope work: protected promise/function, viable region/bounds, several variables, disturbance, sensors/probes, actuators, boundary conditions, adaptation cost, and failure mode.
4. If one proxy or bundle is enough, stay in `C.25`.
5. If the envelope reading depends on a probe, sensor, frame, export, action, coarsening, or boundary interaction that changes what can be said admissibly, the remaining viability-envelope question belongs with `C.26.3`.
6. If the sentence is an intervention-sensitive temporal claim about rate-change under effort, window, resistance, or cadence, inspect `C.27` for the smallest honest temporal-claim adequacy card before using the quality label for action.
7. State viable region/bounds, trade-off, admissible use, non-admissible use, and failure mode before viability language is used for action.

Minimum viability-envelope note:

| Field | Required content |
| --- | --- |
| Bearer | System, service, organization, team, model, process, or role configuration whose viability is at stake |
| Protected promise / function | The promise, function, use, operating regime, or stakeholder value the envelope protects |
| Variables | Which qualities, constraints, resources, risks, or state descriptors define the envelope |
| Viable region / bounds | What counts as inside, near edge, degraded, or outside the envelope for this use |
| Disturbance class | What perturbation, demand shift, environment change, probe, or boundary condition stresses the envelope |
| Actuators | What work, design move, policy, boundary change, sensor change, or resource change can move the bearer |
| Trade-off / loss | What gets worse, hidden, coarsened, delayed, or made more expensive |
| Admissible use | Which action, decision, relation, or triage use the envelope reading can carry |
| Non-admissible use | Which release, audit, assurance, or universal quality claim requiring additional support it does not support |
| Failure mode | What it means to leave the envelope or to mistake one proxy for the envelope |

Useful outputs:

- a Q-Bundle when the issue is quality decomposition;
- a `C.26.3` envelope-regulation note when probes/actuators/boundary conditions change the lawful viability reading;
- a `C.27` temporal-claim adequacy card when rate-change, effort, window, resistance, or cadence changes the admissible use;
- no QL wording when ordinary quality-bundle, proxy, feedback, or control tuning carries the work.

### C.25:End
## C.26 - Quantum-Like Modeling Lens

> Type: Architectural pattern
> Status: Stable
> Normativity: Normative unless explicitly marked informative

### C.26:1 - Problem frame

FPF already has local patterns for decisions, boundaries, bridges, work, measurement, search, and quality bundles. Some real architecture cases still break when those patterns are applied as if every read, question, dashboard, workshop, bridge, or simplified representation were a passive view of a stable state.

Use this pattern when the ordinary FPF pattern remains active but misses one extra representational issue: the act of probing, framing, exporting, comparing, or coarsening changes what can admissibly be inferred from the represented state. The useful move is small. Add a quantum-like mathematical lens only where it tells the user how to avoid a concrete representational mistake.

This pattern is not a physics claim. In FPF, `quantum-like` names a detached mathematical and representational lens, comparable in role to probability, calculus, optimization, or state-space modeling. It is cheap as a QL-lite note and expensive only when the claim becomes reusable law, assurance evidence, empirical superiority, formal reconstruction, or ontology.

Unifying principle: use QL to cheapen the first correct move, not to make the first mention more expensive.

| Working view | Value |
| --- | --- |
| Primary reader | Architect, method author, steward, or manager deciding whether QL wording improves a concrete FPF representation. |
| Governed object | A local use of quantum-like mathematical language in pattern prose or work guidance. |
| Governed move | Admit, select another applicable pattern body, narrow, or escalate the QL wording by ordinary FPF pattern, QL cue, payoff, minimal admissible output, and local stop. |
| Outside work | Physical quantum claims, general ontology, ordinary uncertainty/complexity, ordinary DDD locality, ordinary compression, and search/regime generation. |
| What changes in practice | The writer stops asking "does quantum-like help here?" and asks "what representational mistake does this lens prevent here?" |

What this lens buys in practice:

| QL support | Practical gain |
| --- | --- |
| Probe-aware design | Design a workshop, dashboard, API read, survey, readiness check, or metric publication as a state-shaping interaction when it is not only a readout. |
| Comparison-frame discipline | Notice earlier that two options, scores, or judgments cannot be compared in one frame without a bridge, coupling, or declared joint-comparison route. |
| Export humility | Stop false cross-context substitution quickly: a carried value, report, or label may not export the same state for the intended use. |
| Low-recoverability distributed-state reading | Talk about team, organization, market, or service-mesh behavior without inventing a group mind and without reducing the state to one report. |
| Envelope-first viability | Move from "which single metric wins?" to a viability envelope with variables, sensors, actuators, costs, and failure modes. |
| Admissible coarsening use | Use a cheaper state representation when it helps, while keeping source, loss, admissible use, non-admissible use, and reopen condition visible. |

Plain glosses:
- `quantum-like`: a detached mathematical / representational lens, not a claim about what the target is made of.
- `probe`: an operation that both produces an output and may change the represented state or admissible use of the output.
- `frame`: a probe frame, measurement frame, comparison frame, or model frame. If the text means FPF semantic context, say `U.BoundedContext` or bounded context explicitly.
- `state`: the represented condition relevant to the current decision, not a generic new `U.State` kind.
- `state update`: a typed update claim. When load-bearing, say whether the update is a system change, work change, epistemic reading update, carrier update, emitted-output update, formal model update, or update-law change; do not let one phrase carry all of them.
- `context`: not a shorthand for frame. Use it only in explicit FPF terms such as `U.BoundedContext`, bounded context, or cross-context bridge.
- `export`: a carried representation whose use may lose timing, coordination, role, use conditions, confidence, or relation structure.
- `coarsening`: an intentionally cheaper state representation with declared loss and reopen conditions.

Phrase hygiene:

| Risky phrase | Better FPF phrase |
| --- | --- |
| Dashboard changed the state. | Dashboard publication or use changed work behavior or evidence conditions. |
| Metric acted as observer. | Measurement/publication regime functioned as a probe interaction. |
| Organization knows. | Coordinated work traces support a low-recoverability state reading over a declared collective bearer. |
| Market is entangled with product team. | Ordinary market, feedback, negotiation, and organizational-coupling routes fail; local reads or exports are not admissibly comparable or reusable without declaring the probe, frame, update, or export relation. |
| Boundary collapsed after workshop. | Workshop work selected or created a local boundary reading for this decision window. |
| State cannot be copied. | No faithful-enough export supports the intended cross-context use. |
| Same metric in two contexts. | Same-named result under different measurement or comparison frames. |
| Quantum-like service health. | Viability-envelope reading affected by probe, export, or coarsening cue. |

Example style:

| Style | Example |
| --- | --- |
| Bad | The team's quantum-like distributed state collapsed after the readiness dashboard observation. |
| Better | The readiness dashboard was not a passive read: its publication changed team behavior, so the dashboard result cannot be used alone as pre-publication readiness evidence. |
| Best | Apply `C.16` to ordinary metric issues and `B.3` to release assurance. Retain `C.26.1` only for the residual false passive-read issue: dashboard publication changed readiness behavior in window W. Decision diff: do not use the dashboard as sole release evidence; add independent work traces and record non-admissible use. |

Informative bilingual translation note:

| English | Prefer in Russian / bilingual use | Risk |
| --- | --- | --- |
| `probe` | probe / пробное воздействие / считывающее взаимодействие | "измерение" is too narrow; "зонд" sounds too physical. |
| `state reading` | чтение состояния / state-reading claim | "состояние" without reading sounds ontological. |
| `frame` | рамка сравнения / probe frame / model frame | "контекст" can collide with bounded context. |
| `instrument` | instrument-like operation / операция-инструмент | "прибор" sounds too physical. |
| `distributed state` | distributed-state reading | "распределённое состояние" sounds like a new object. |
| `faithful-enough export` | достаточно верный перенос для заявленного use | "копия" suggests an impossible-copy ideal. |

### C.26:2 - Problem

Without this pattern, teams make five recurring mistakes.

They treat a probe as a neutral read when the probe changes later answers or behavior. They combine two posterior-looking outputs as if both came from one shared sample space. They export a team state, dashboard value, or context-map result as if it were a faithful-enough export for the intended use. They compress a large state representation for speed and then reuse the shortcut outside its admissible-use scope. They let words such as `quantum`, `entanglement`, `collapse`, or `field` import ontology that the model never earned.

The result is not merely loose wording. The team may approve a release from a dashboard whose publication and operational use changed the work it was supposed to report, average incompatible risk estimates, copy a local decision into another bounded context after the bridge lost the live coordination, or claim a speed gain because the representation was low-bit, linear, symbolic, or compressed without naming the loss.

### C.26:3 - Forces

| Force | Tension |
| --- | --- |
| Ordinary FPF patterns first | `C.11`, `A.6`, `F.9`, `A.15`, `C.25`, `C.16`, `A.10`, `B.3`, `C.18`, `C.19`, and `A.19` already do real work. QL wording must add only the remaining state, probe, or export cue. |
| Lightweight use vs claims requiring additional evidence | A local diagnostic note should be cheap; reusable guidance, assurance, physical claims, or superiority claims need heavier evidence and explicit neighboring-pattern selection. |
| Useful math vs misleading vocabulary | Quantum-like formalisms help with order, contextual probability, incompatible probes, instruments, and open information systems; popular quantum words easily overclaim. |
| Representation cost vs representation loss | A cheaper state representation may be the right engineering move, but only if the source, shortcut, loss, admissible use, and reopen condition stay visible. |
| Recognition vs assurance | Working readers need fast entry; the assurance surface needs enough typed fields to prevent pattern-role theft, impossible-copy overread, and hidden ontology. |

### C.26:4 - Solution

Start with the ordinary FPF pattern. Add this lens only when ordinary wording would falsely treat a probe, question, metric, dashboard, API read, workshop, bridge, comparison frame, or coarsened representation as passive, stable, jointly comparable, or faithfully exportable. The main entry question for the whole cluster is: "What should the user do with this lens so that the representational mistake does not arise here?"

Action path:

1. Name the ordinary FPF pattern that already carries the baseline question.
2. Name the concrete representational mistake: passive read, shared comparison frame, false faithful-enough export claim for the intended use, exact-state shortcut, or unsupported coarsened representation.
3. Test the positive QL cue and the negative activation list.
4. Fill the QL-lite card if the cue survives.
5. Emit one practical result: use ordinary pattern only, add QL-lite note, select one C.26 child pattern as the applicable pattern body, add evidence/assurance, or drop the QL wording.
6. Escalate only when the claim becomes reusable, assurance-bearing, formal, empirical-superiority-bearing, or ontology-bearing.

C.26 ordinary output: produce one of these, then stop or select the neighboring applicable pattern body:

- no C.26 pattern selection because the ordinary FPF pattern carries the case;
- QL-lite note with the minimum sufficient field set;
- use the ordinary pattern that carries the live question;
- escalation to evidence, assurance, or formal-model work when the claim’s evidence or authority demand requires it.

Keep the entry cost proportional to the use. A QL situation does not begin with a full record.

| Working view | Use it when | Ordinary output |
| --- | --- | --- |
| Recognition note | The reader only needs to see that an ordinary FPF pattern plus a QL cue may prevent a representational mistake. | Five-field QL-lite note, local stop, and next action. |
| Decision-bearing record | The QL reading changes a boundary, bridge, work, measurement, viability, or representation decision. | Typed fields for carrier, window, rival, loss, minimal admissible output, admissible use, non-admissible use, and neighboring-pattern handoff. |
| Assurance record | The claim becomes reusable law, audit and evidence support, release-facing support, empirical-superiority claim, formal reconstruction, or ontology-bearing claim. | Evidence graph, measurement relation or assurance relation, source-support role, rival-model comparison, and explicit escalation outside QL-lite. |

Do not make the decision-bearing or assurance record the ordinary entry cost. The everyday pattern move is a small recognition note plus a bounded action.

Affordability by working-reader situation:

| Working-reader situation | Use |
| --- | --- |
| Practitioner or architect | Three-to-five-field recognition note plus decision diff. |
| FPF pattern author | Full card, examples, neighboring-pattern selection, and local anti-cases. |
| Checking reader | Pattern-application check plus false-positive and false-negative tests. |
| Assurance or audit reader | Full evidence record with `B.3`, `A.10`, and `C.16` integration. |
| Research or formalization reader | M3 or M4 formal model, rival models, and empirical or theoretical support. |

Do not require a practitioner or architect to produce a researcher-level record when the claim is only recognition or local-working support posture.

Checking discipline:

| Checking failure | Repair |
| --- | --- |
| "QL word appeared, escalate to assurance." | Ask what claim and evidence demand are actually live. |
| "This sounds metaphorical, remove it." | Ask what representational mistake the wording prevents. |
| "Use ordinary FPF only." | Name the ordinary FPF pattern that carries the residual claim. |
| "No quantum-like unless mathematically formalized." | Allow QL-lite when it prevents local false reading and no formal claim is made. |
| "Everything with feedback is QL." | Apply `C.16`, `C.25`, or `A.15` first to ordinary feedback, control, and metric-gaming cases. |

Cluster maxim: quantum-like wording does not raise assurance load by default. Assurance load rises only when the claim itself is reused, contested, evidence-bearing, release-facing, high-impact, comparative, formal, or ontology-bearing.

Pattern-local-note dependency rule: when an existing FPF pattern cites `C.26` or a `C.26.*` child, the pattern's ordinary action guidance and conformance text remain primary. The citation means only: if a residual QL cue remains after the ordinary FPF pattern has carried its part, use this lens for that residue. It does not make every citing-pattern case depend on the full C.26 record or on every child-pattern semantic.

QL boundary selection:

| Gate question | Applicable FPF pattern |
| --- | --- |
| Is this ordinary boundary, interface, API, or protocol ambiguity? | `A.6` and boundary/interface patterns. |
| Is this ordinary bridge, export, substitution, or loss across contexts? | `F.9` / `F.9.1`. |
| Is this ordinary measurement, metric gaming, scale, coordinate, or noise? | `C.16`. |
| Is this ordinary evidence, provenance, method, or carrier issue? | `A.10` and, when assurance-bearing, `B.3`. |
| Is this ordinary work, routine, incentive, alignment, or authority issue? | `A.15` and neighboring work/authority patterns. |
| Is this ordinary quality-bundle, viability, feedback, or dynamics tuning? | `C.25`, `U.Dynamics`, and measurement or work patterns. |
| Is this ordinary representation transduction or controlled coarsening? | `A.6.3.RT`, `A.6.3.CSC`, and ordinary representation patterns. |
| Does residual false passive read, false shared frame, false faithful export, unsupported state reading, or QL-specific coarsening remain? | Use `C.26` or the relevant `C.26.*` child with the minimum sufficient field set. |

The default output is a QL-lite card:

| Field | Question |
| --- | --- |
| Ordinary FPF pattern | Which FPF pattern already carries the baseline question? |
| QL cue or formal cue | Which order effect, frame effect, incompatible probe structure, response-replicability tension, measurement-changing-state, no faithful-enough export under the declared probe, frame, or use, bridge loss or export loss, mutual interaction whose local reads and exports are no longer admissibly comparable or reusable without declaring the probe, frame, or update relation, open-information-system update whose update rule, probe frame, or export admissibility is part of the modeling condition, or state-representation coarsening effect changes the admissible reading? |
| Representational payoff | What mistake does the lens prevent, or what cheaper representation does it support? |
| Minimal admissible output | What may be concluded or done now? |
| Decision diff | What would be done incorrectly under the ordinary false reading, and what changes after QL repair? |
| Local stop or neighboring-pattern handoff | Which use is non-admissible under this card, and which neighboring FPF pattern governs that use? |

Decision diff examples:

| False reading | QL repair | Decision diff |
| --- | --- | --- |
| Dashboard passively shows release readiness. | Dashboard publication changes readiness behavior. | Do not use dashboard alone as release evidence; add independent work traces or redesign metric publication. |
| Workshop discovered the boundary. | Workshop also created the boundary meaning. | Do not export workshop result as timeless domain fact; record window, participants, carriers, and unresolved rivals. |
| Service is healthy because latency is green. | Viability envelope is degraded by support load and promise failure. | Add envelope variables and actuators; do not greenlight based on latency alone. |
| Summary preserves architecture state. | Summary is a coarsened shortcut with declared loss. | Use for orientation only; return to source for release or design lock. |

Minimum viable QL-lite note:

```text
Ordinary patterns: C.16 + A.15.
Mistake prevented: dashboard result would be read as passive release-readiness evidence.
Probe effect: publication changed team behavior during W.
Decision diff: do not use dashboard alone for release; add independent work traces.
Stop: not a reusable QL model, not assurance evidence, not physical quantum claim.
```

This is enough for `QLP-0` / `QLP-1` ordinary working use unless the claim is reused, externalized, contested, assurance-facing, comparative, formal, or ontology-bearing.

Use the `C.11` mini-output discipline across the cluster: finish with one next move, not with an interesting label.

| Mini-output | Cluster meaning |
| --- | --- |
| Use / choose now | The low-recoverability reading is enough for the declared local action or decision. |
| Probe again | One named probe, order/frame test, measurement, source check, or bridge check could still change the result. |
| Reroute | The live question belongs to another FPF pattern rather than QL-lite. |
| No QL wording | Ordinary uncertainty, measurement, work, bridge, quality, or search patterns carry the case. |

Retire QL when the residual cue disappears. If `A.6`, `F.9`, `C.16`, `A.10`, `B.3`, `A.15`, `C.25`, `A.6.3.CSC`, `A.6.3.RT`, or another ordinary FPF pattern now carries the claim without a false passive read, false shared frame, false faithful export, unsupported distributed-state reading, or QL-specific coarsening residue, remove QL wording from the active working note or pattern prose.

Use the lens only after the activation test survives both sides. QL remains active only when the ordinary FPF pattern cannot admissibly treat the output as a passive read, a shared-frame comparison, a faithful-enough export, or a use-scope-preserving state representation. Bridge loss, feedback, coupling, openness, compression, and coarsening are not QL cues unless they change the admissible state, probe, frame, or export reading for the current use. C.26 carries the full negative activation catalog; child and citing patterns should repeat only the local non-trigger that is frequent enough to matter for that pattern.

Canonical cue grammar:

| Cue family | QL only if |
| --- | --- |
| Probe / order / frame | The operation changes the admissible reading of the output, comparison, or represented state. |
| Export or bridge | The export is not faithful enough for the intended use, and ordinary bridge and loss discipline does not fully carry the remaining export/use issue. |
| Distributed-state reading | Coordinated behavior, trace pattern, or work result supports a low-recoverability state reading no single carrier faithfully exports, after ordinary rivals are checked. |
| Viability envelope | Probe, sensor, actuator, export, boundary condition, or coarsening changes the admissible viability reading. |
| Coarsening | The reduced-detail state representation depends on a QL cue plus declared loss, admissible use, non-admissible downstream use, and reopen trigger; ordinary compression or abstraction alone is not enough. |


| Positive activation pressure | Negative activation test |
| --- | --- |
| Load-bearing order effect, frame effect, incompatible probe structure, response-replicability tension, measurement-changing-state, no faithful-enough export under the declared probe, frame, or use, bridge export of the state that is not faithful enough for the current use, mutual interaction where neither side's output can be used as a faithful-enough local export of the joint state under the intended decision frame after ordinary feedback relations are tried, or state-representation coarsening whose admissible use changes because of a declared QL cue. | No QL activation from discreteness, tokenization, low-bit quantization, stochasticity, ordinary uncertainty, nonlinearity, complexity, ordinary coupling, ordinary feedback, emergence, tacit knowledge, ordinary openness, ordinary compression, ordinary coarsening, ordinary DDD locality, ordinary API boundary, ordinary bridge loss, ordinary feedback control, or impressive quantum-like vocabulary alone. |


Practical payoff in ordinary prose:

- "the metric reported readiness" becomes "the metric publication or measurement regime functioned as a probe interaction that changed readiness behavior";
- "two risk scores disagree" becomes "the two scores may come from non-shared comparison frames with no declared admissible joint comparison route";
- "the workshop discovered the split" becomes "the workshop was a probe whose order and framing changed alignment and local meaning";
- "the team knows" becomes "coordinated work evidences a low-recoverability distributed-state reading with carriers, window, and export loss";
- "this smaller model is enough" becomes "this coarsened state representation carries only its declared admissible-use scope and reopen condition".

#### C.26:4.1 - Inherited QL boundary

Invariant `QL-NQ`: within FPF, `quantum-like` is a detached mathematical and representational modeling lens. It may use quantum-theory-derived structures such as contextual probability, Hilbert-like state spaces, non-Boolean logic, instruments, operator-like update, order effects, open-system descriptions, or incompatible probes.

`Quantum-like` does not assert physical quantum substrate, microscopic quantum process, qubits, quantum computation, physical entanglement, nonlocal causality, literal collapse, mystical observer effects, social substance, or collective mind. A physical-quantum claim is a different claim and needs separate physical or empirical support outside this pattern cluster.

Child patterns inherit `QL-NQ`. They should not restate the global boundary as local guidance unless they are repairing a specific confused phrase.

#### C.26:4.2 - Pattern selector
##### C.26:4.2.1 - Causal-use exit before QL retention

Before retaining `QL-lite`, `QL-NQ`, or a quantum-like framing for a live claim, check whether the actual question is intervention, counterfactual comparison, causal effect, causal fairness, causal policy, off-policy causal evaluation, or realizability of counterfactual-rung data. If so, redirect the claim/question to `C.28` before any quantum-like retention.


```text
CC-C26-CAUSAL-EXIT:
If the live question is intervention, counterfactual comparison,
causal effect, causal fairness, causal policy, or realizability of counterfactual-rung data,
redirect the claim/question to C.28 before retaining QL-lite or QL-NQ.
```

What changes in practice: "the model is quantum-like" cannot be used to skip causality-ladder rung declaration, causal identification, causal evidence support basis, or counterfactual sampling realizability.

What this does not authorize: `C.26` does not become a causal-use pattern and does not treat counterfactual material as a quantum-like subcase; it keeps quantum-like modeling discipline and sends causal-use support to `C.28`.


Use this as a diagnostic sequence before retaining QL wording. DDD, microservice domain analysis, and ordinary boundary/bridge patterns stay first for bounded contexts, service cuts, integration points, and exported meaning; QL is retained only when a workshop, probe, export, or frame changes what can admissibly be inferred.


1. Measurement, metric, scale, method, evidence, or assurance load goes first to measurement and evidence patterns: `C.16`, `A.10`, or `B.3`.
2. Bridge, translation, publication, rendering, or exported-loss question goes first to bridge and publication patterns: `F.9`, `E.17`, or `E.17.EFP`.
3. Causal intervention, command, work enactment, role alignment, or routine question goes first to work and authority patterns: `A.15` and the relevant neighboring pattern.
4. Boundary/interface wording, service-interface typing, bridge endpoint, relation precision, or lexeme-collision question goes first to boundary and language patterns: `A.6`, `A.6.B`, `A.6.P`, `A.7`, `E.10`, or `F.18`.
5. Quality, viability, feedback, or control-tuning question goes first to quality, dynamics, and measurement patterns: `C.25`, `U.Dynamics`, and `C.16`.
6. Suspect option menu, unknown alternative, local plateau, basin movement, or candidate-generation question goes first to search and regime patterns: `B.5.2`, `C.18`, `C.19`, or `A.19`.
7. Retain QL only for the remaining declared state, probe, export, frame, open-information-system, or coarsening cue.

C.26 does not choose among options, generate missing alternatives, or settle `C.11` decision quality. It can mark that the available readings sit in non-shared comparison frames or lack a declared admissible joint comparison route; the choice/search output still belongs to `C.11`, `B.5.2`, `C.18`, `C.19`, or `A.19`.

| If the live question is mainly... | First FPF pattern | Add QL only when... |
| --- | --- | --- |
| Choice, comparison, or question order | `C.11` | incompatible probes, order effects, non-shared comparison frames, or no declared admissible joint comparison route change the choice-state reading. |
| Boundary interaction or interface reading | `A.6`, `A.6.B`, `A.6.P` | the probe or interaction changes the represented state, export validity, or viability decision. |
| Cross-context bridge or publication export | `F.9`, `E.17`, `E.17.EFP` | the exported state is not faithful under the current probe and bridge conditions. |
| Work enactment or coordinated behavior | `A.15`, with `A.10` / `B.3` for evidence | coordinated work evidences a low-recoverability distributed-state reading not faithfully exportable as one representation. |
| Measurement, metric, score, or dashboard | `C.16`, `A.10`, `B.3` | the measurement regime, publication act, or operational use functions as a probe interaction that updates the represented state. |
| Viability or quality bundle | `C.25`, `U.Dynamics`, `A.6`, `A.15` | envelope regulation depends on probe, boundary condition, actuator, export, or coarsened state representation. |
| Candidate generation or option-menu suspicion | `B.5.2`, `C.18`, `C.19`, `A.19` | QL wording only marks that the current frame may be suspect; search patterns generate alternatives. |
| Representation shortcut | CSC, RT, ordinary abstraction, representation learning, POMDP, search-space pruning | the shortcut depends on contextual probability, incompatible probes, instrument-like update, open-information-system update rule, probe-frame, or export-admissibility cue, or lossy state export. |

#### C.26:4.3 - Escalation by evidence or authority demand

| Claim-use posture | Use | Required basis |
| --- | --- | --- |
| Ordinary FPF pattern | QL is not needed. | Use the ordinary FPF pattern plainly. |
| QL-lite note | Local diagnosis, model note, or worked recognition. | Fill the five-field card. |
| Reusable pattern prose | A pattern, example, or neighboring note will repeat the move. | Add typed state, probe, or export fields, source support, and local anti-cases. |
| Decision or assurance use | The claim affects boundary, release, audit, evidence, or work decision. | Add rival explanations, evidence posture, loss notes, and explicit neighboring-pattern selection. |
| Ontology or physical claim | A physical substrate, new ontology, or empirical superiority is asserted. | This pattern does not support the claim; use a separate physical or empirical support outside this pattern cluster. |
For QL claims that carry decision, assurance, ontology, physical-substrate, or empirical-superiority use, compare rival model families before retaining QL as load-bearing. Failure of a simple Bayesian or passive-read model is not yet evidence for QL necessity; it is evidence for trying richer classical, causal, performative, instrument, active-sensing, or representation-abstraction rivals before QL carries the claim:


| Rival family | Use first | Keep QL active only when |
| --- | --- | --- |
| Classical Bayesian, nonparametric Bayesian, or ordinary probabilistic update | `C.11`, measurement and evidence patterns, and model-expansion patterns | incompatible sample spaces, contextual probability, order-sensitive query structure, or failure of ordinary total-probability composition remains active. |
| Causal intervention or ordinary world-state change model | `A.15`, boundary patterns, and evidence patterns | the intervention is also being used as a read, export, comparison, or optimization of the state it changes. |
| Performative prediction, strategic response, or dashboard-induced behavior | `C.16`, `A.10`, `B.3`, `C.26.1`, and viability/work patterns | instrument-like state update, incompatible probes, or non-faithful state export remains after the ordinary behavior account is written. |
| POMDP, active sensing, active inference, or experimental design | `A.3`, `C.16`, `U.Dynamics`, and action-cost patterns | the formal claim also involves incompatible probe frames, contextual probability, or state-representation loss. |
| State abstraction, representation learning, surrogate modeling, sketching, or ordinary compression | `A.6.3.CSC`, `A.6.3.RT`, `A.19`, `F.9`, and ordinary representation patterns | the shortcut depends on contextual, instrument-like, open-information-system update/probe/export-admissibility, or incompatible-probe structure rather than ordinary abstraction engineering. |
| Causal abstraction or approximate causal abstraction | Use first when the shortcut claims to preserve intervention, explanation, manipulation, or cross-scale structure. | contextual probability, incompatible probes, instrument-like update, open-information-system update rule/probe-frame/export-admissibility, or lossy state export remains after the causal-abstraction mapping between source-scale and target-scale states and interventions is stated. |


Math reveal sequence:

| Mathematical-formality posture | Use | Form |
| --- | --- | --- |
| M0 - no math | Everyday FPF use. | Plain-language QL-lite note: false passive read, output, admissible use, and stop. |
| M1 - structural sketch | A reader needs to see why ordinary comparison or export fails. | Diagram or table: probes, frames, carriers, export loss, unsupported comparison. |
| M2 - toy formalization | Pattern example, education, or contested architecture claim. | Small finite-state, matrix, or instrument-like toy model, explicitly non-authoritative. |
| M3 - decision-bearing formal model | Reusable guidance or high-impact decision. | Declared assumptions, rival models, validation/evidence, and failure conditions. |
| M4 - formal assurance / research claim | `QLP-3` assurance or reusable-law claim. | Full formal reconstruction, baseline, proof/data, source constraints, and limitations. |

Most C.26 use should stay at M0 or M1.

Evidence posture is escalation by consequence, not an admission gate. `QLP-0` or `QLP-1` is the ordinary entry posture for quick QL-lite use; `QLP-2` / `QLP-3` appears only when the claim is reused, contested, decision-bearing, assurance-facing, high-impact, or made part of reusable pattern action guidance or conformance text.

Evidence posture scales by use:

| Level | Use | Required content |
| --- | --- | --- |
| `QLP-0` recognition | Example, teaching case, or local recognition prompt. | Claim, example, ordinary FPF pattern, QL cue, and local stop. |
| `QLP-1` local working use | Local architecture discussion, triage, or provisional design reasoning. | `QLP-0` content plus evidence carrier, time window, uncertainty/confidence posture, and stop/reroute condition. |
| `QLP-2` decision-bearing use | Boundary decision, bridge/export use, viability move, work claim, or representation shortcut changes what the team should do. | `QLP-1` content plus rival explanations, export/loss note when live, minimal admissible output, selected applicable pattern body, admissible use, and non-admissible use. |
| `QLP-3` assurance or reusable guidance use | The claim is used for assurance, audit, durable pattern action guidance or conformance text, reusable relation/name/measure, or high-stakes decision support. | `QLP-2` content plus `A.10` and `B.3` assurance posture, `C.16` template if measured, documented bridge and loss path, source-support role, and explicit local stop or inherited-boundary note. |

#### C.26:4.4 - Recognition case matrix

| Case | First applicable pattern body | QL cue to test | Local stop |
| --- | --- | --- | --- |
| Domain workshop changes the split | `A.1.1`, `F.9`, `C.26.1` | The workshop is both evidence and intervention; question order or facilitation frame changes split recommendation, team alignment, and local meaning. | Do not replace DDD with QL; keep bounded-context law and bridge fields active. |
| Same label across bounded contexts | `F.9`, `A.6.P` | API extraction or team alignment changes operational state, or export loses the relation that matters. | Same label is not same entity; ordinary bridge may be enough. |
| Organization acts from a latent decision | `A.15`, `A.10`, `B.3`, `C.26.2` | Coordinated role-work, records, commitments, traces, and routines evidence a low-recoverability state no participant faithfully reports. | Do not infer a group mind or timeless culture. |
| Survey, dashboard, policy, or API read of culture | `C.16`, `A.10`, `F.9`, `C.26.1`, `C.26.2` | The probe may change the state it evidences, and the export may lose load-bearing structure. | Treat the output as carrier/probe, not as the state itself. |
| Service boundary under load | `C.25`, `A.6`, `A.15`, `C.26.3` | Viability depends on changing caching, throttling, routing, staffing, protocol, bridge, or context split. | Do not reduce viability to one green metric. |
| Moving body or sensor to see the missing face | active/embodied inference routes, `C.26:4.5` state-representation coarsening card | The system spends energy, time, risk, attention, or coordination to obtain a discriminating observation. | Do not call ordinary sensing or active inference quantum-like without a QL cue. |
| Glass memory / hysteresis | `C.26.1`, `C.26.3`, `U.Dynamics` | Prior state constrains current response; state history or retained trace changes admissible reading. | Do not force dynamics variables unless load-bearing. |
| Cell-like service situation | service, boundary, work, viability patterns first | Cell-like criteria may clarify boundary, controlled exchange, protected invariants, repair, state-continuity, and resource analogue. | Retain analogy only when it changes a decision beyond ordinary service-facet language. |
| Suspect option menu | `B.5.2`, `C.18`, `C.19`, `A.19` | Current options may be products of the current measurement frame. | QL only marks suspicion; search patterns generate alternatives. |

#### C.26:4.5 - State-representation coarsening card

This card discipline is active when a fuller state representation is too detailed, unstable, unavailable, or expensive for the current bounded decision and a reduced-detail state representation is useful only under a declared QL cue. It is not a standalone speed pattern, not a standalone coarsening pattern, and not a new state-representation kind.

C.26 does not carry ordinary coarsening. `A.6.3.CSC` carries controlled coarsened rendering; `A.6.3.RT` carries same-described-entity representation-scheme transition; `A.19`, `U.Dynamics`, modeling patterns, and ordinary abstraction patterns carry ordinary state abstraction. C.26 carries only the residual QL cue plus the loss/use boundary for this shortcut.

Question-to-pattern map:

| Main question | First FPF pattern or relation |
| --- | --- |
| Coarsened rendering of source episteme or source publication for narrower use | `A.6.3.CSC` |
| Same-described-entity representation-scheme or reasoning-medium transition | `A.6.3.RT` |
| Cross-context equivalence, substitution, projection, export, or loss | `F.9` / `F.9.1` |
| Measurement coordinate, scale, score, result, or dashboard reading | `C.16` |
| Evidence carrier, provenance, method, support, or time window | `A.10` |
| Assurance claim, release support, audit, readiness, or compliance use | `B.3` |
| Search-space pruning, option generation, or missing alternatives | `C.18`, `C.19`, `A.19` |
| Residual QL state, probe, frame, export, or coarsening cue after those patterns act | `C.26` |

Start with this coarsening mini-card:

| Mini-entry | Question |
| --- | --- |
| Source | Which fuller state representation, trace set, model, measurement scheme, or dynamics account loses distinctions in the shortcut? |
| Shortcut | Which smaller representation is being used instead, and for which bounded decision or action class? |
| Loss | Which precision, distinction, uncertainty, comparability, traceability, or relation structure is lost? |
| Admissible use | Which bounded decision, probe, comparison, time-window reading, or action class remains admissible for this reduced-detail state representation? |
| Reopen trigger | Which dispute, drift, failure, threshold crossing, bridge demand, or decision change sends the team back to the source-bearing episteme or source publication? |

For the representation shortcut itself, fill this coarsening card:

| Field | Question |
| --- | --- |
| Source representation | Which fuller model, state space, trace set, measurement scheme, probability model, dynamics model, or representation loses distinctions in the shortcut? |
| Coarsened representation | Which typed, symbolic, finite, operator-like, Hilbert-like, rough-set, low-bit, or source-loss-affected representation is used instead? |
| Shortcut mechanism | Which projection, typed-state reduction, finite-dimensional representation, operator-like update, rough-set approximation, state aggregation, compression, or linearization is doing the representational work? |
| Shortcut purpose | Which bounded decision, probe, comparison, time-window reading, or action class needs the reduced-detail state representation? |
| What is lost | Which precision, distinction, uncertainty, compatibility, traceability, causal detail, or cross-context relation is lost? |
| Loss budget | How much loss is accepted for this decision, probe, comparison, route, or time window? |
| Admissible use | For which decisions, probes, comparisons, candidate-route selections, or time windows does the shortcut preserve the required distinctions? |
| Non-admissible use | For which claims, audits, bridges, comparisons, future actions, or high-stakes decisions does the shortcut lack the required distinctions, source support, or recoverability? |
| Ordinary routes still active | Which ordinary abstraction, causal abstraction / approximate causal abstraction, state aggregation, representation learning, POMDP simplification, heuristic compression, CSC, RT, or low-bit implementation route remains sufficient if the QL cue is absent? |
| Evidence / formal source | Which model, trace, experiment, source, or formal argument supports the shortcut rather than merely naming it quantum-like? |
| Reopen trigger | Which dispute, drift, threshold crossing, failure, audit, bridge demand, or decision change requires returning to the source representation or ordinary FPF pattern? |

If the text claims that the shortcut is faster, cheaper, more compressed, more linear, more stable, or more tractable, add this claim declaration. The claim is separate from the coarsening card: the card controls the reduced-detail state representation; the declaration controls the performance or tractability assertion.

| Declaration field | Question |
| --- | --- |
| Baseline representation and cost | What ordinary model or route is too expensive, and by which resource: time, memory, measurement, coordination, latency, energy, risk, attention, cognitive load, privacy, or social cost? |
| New representation | Which changed representation creates the claimed gain? |
| Mechanism | Which compression, linearization, operator-state update, reduced information-state encoding, shortcut, or approximation mechanism creates the gain? |
| Claimed gain | What exactly becomes faster, cheaper, more stable, smaller, or more tractable? |
| Loss / error budget | Which precision, expressivity, compatibility, comparability, evidence-support class, traceability, or future-use loss is accepted for the intended use? |
| Admissible use | For which decisions, probes, comparisons, candidate-route selections, time windows, or action classes does the declared gain meet the required threshold? |
| Non-admissible use | For which claims, audits, bridges, comparisons, future actions, or high-stakes decisions does the declared gain fail the required threshold? |
| Ordinary alternatives | Which ordinary compression, approximation, abstraction, feature-engineering, active-inference, search, POMDP, or low-bit route was tried or remains sufficient? |
| Evidence / formal source | Which source, model, trace, worked case, benchmark, or formal analogy supports the claimed mechanism? |
| Reopen trigger | Which dispute, drift, threshold crossing, failure, audit, bridge demand, or decision change requires returning to the source representation or ordinary FPF pattern? |

No speed, compression, linearity, or tractability claim follows merely from the words `linear`, `operator`, `quantum-like`, `quantized`, `tokenized`, `low-bit`, `finite-dimensional`, `compressed`, or `symbolic`.

If the shortcut carries a transition-speed, stabilization, or control claim, add the optional dynamics card:

| Dynamics field | Question |
| --- | --- |
| Rate / acceleration | Which transition, inference, recovery, sensing, routing, or stabilization rate matters? |
| Inertia | What makes the represented state, work routine, boundary condition, or model slow to change? |
| Damping / resistance | What absorbs, slows, filters, or resists the transition? |
| Effort or actuator capacity | Which action, probe, resource, or authority relation can change the transition fast enough? |
| Evidence | Which trace, model, experiment, or operational observation supports the dynamic reading? |

### C.26:5 - Archetypal Grounding


Tell: A reliability dashboard says "Ready" after a new readiness metric is published. Before publication, teams treated incidents as local triage. After publication, they change priorities to satisfy the metric, while unmeasured recovery work gets delayed.

Show, System side: the delivery system, teams, dashboard, incident-handling cycle, and release decision form one operational situation. The dashboard is not only a window; it is part of the work ecology because it changes attention, escalation, and behavior.

Show, Episteme side: the QL-lite card says the ordinary FPF patterns are `C.16`, `A.10`, `B.3`, and `C.25`. The QL cue is an instrument-like metric publication that changes readiness behavior. The minimal admissible output is "treat the dashboard as probe-coupled evidence, not release proof." The local stop is release approval without fuller evidence.

Second grounding: a large state-space model is too expensive for triage, so the team uses four typed operational states. That shortcut is admissible only if the source model, state reduction, loss, admissible use, and reopen trigger remain explicit. The shortcut helps choose a work response; it does not prove the four states are the full system.

### C.26:6 - Bias-Annotation

This pattern intentionally biases authors toward ordinary FPF patterns before QL vocabulary. That bias prevents prestige use of the word `quantum-like` and keeps the mathematical lens useful rather than theatrical.

It also biases authors toward minimal admissible outputs. In ordinary use, the right result is often "apply the neighboring FPF pattern", "do not merge these comparison frames", "mark this dashboard as an instrument", or "return to the source representation if the shortcut fails", not a new doctrine about the target system.

The pattern may under-admit some mathematically valid QL models when the author cannot explain the practical payoff. That is acceptable for FPF pattern prose: a model that cannot say what it buys the working reader is not ready for Core-facing law.

### C.26:7 - Conformance Checklist

| ID | Check |
| --- | --- |
| CC-C26.1 | The text names the ordinary FPF pattern before admitting QL wording. |
| CC-C26.2 | The text states the QL cue as a probe, order, frame, export, comparison, open-information-system update/probe/export-admissibility, or coarsening effect, not as vague complexity. |
| CC-C26.3 | The text states a practical representational payoff. |
| CC-C26.4 | The text states the minimal admissible output. |
| CC-C26.5 | The text states a local stop or neighboring-pattern handoff. |
| CC-C26.6 | The text inherits `QL-NQ` and does not repeat global physical-quantum exclusions as local guidance. |
| CC-C26.7 | If a representation shortcut is used, the coarsening card names source, shortcut, loss, admissible use, non-admissible use, and reopen trigger. |
| CC-C26.8 | A speed, compression, linearity, or tractability claim declaration names baseline representation and cost, changed representation, mechanism, claimed gain, loss budget or error budget, ordinary alternatives, evidence source or formal source, and reopen trigger. |
| CC-C26.9 | If the claim becomes reusable, assurance-bearing, measurement-like, relation-minting, high-stakes, or superiority-claiming, the text escalates beyond QL-lite. |
| CC-C26.10 | The text does not mint `U.Probe`, generic `U.State`, `U.DistributedState`, `U.Lens`, a new boundary kind, or a social-substance kind. |
| CC-C26.11 | A cold reader can tell what changes in practice in the first minute. |
| CC-C26-CAUSAL-EXIT | If the live question is intervention, counterfactual comparison, causal effect, causal fairness, causal policy, off-policy causal evaluation, or realizability of counterfactual-rung data, the text redirects the claim/question to `C.28` before retaining QL-lite or QL-NQ. |


### C.26:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Symptom | Repair |
| --- | --- | --- |
| Quantum-like as prestige word | The case is only complex, uncertain, nonlinear, discrete, or hard to measure. | Use ordinary FPF patterns. Admit QL only with a declared cue and payoff. |
| Precautionary suppression | QL wording is rejected because it is unusual, while no ordinary FPF pattern has carried the residual false passive read, false export, false comparison frame, unsupported distributed-state reading, or single-metric viability mistake. | Name the ordinary FPF pattern that carries the residual claim. If no such pattern can be named, allow QL-lite at recognition or local-working support posture. |
| Physical overread | The text sounds as if organizations, services, or teams are physically quantum systems. | Cite inherited `QL-NQ`; rewrite the claim as mathematical or representational. |
| Passive dashboard | A metric or score is used as a neutral fact after its publication or operational use changed behavior. | Use measurement and evidence patterns and, if needed, `C.26.1`. |
| Faithful-copy export | A survey, report, API response, or context map is treated as the live state itself. | Use bridge/export loss, `C.26.2`, or ordinary publication patterns. |
| Speed or compression slogan | A shortcut is called fast, cheaper, linear, low-bit, symbolic, or compressed without a declared claim. | Write the speed, compression, or linearity claim declaration: baseline representation and cost, changed representation, mechanism, claimed gain, loss budget or error budget, ordinary alternatives, evidence source or formal source, and reopen trigger. Keep the coarsening card only for the representation shortcut itself. |
| Hidden search problem | The option menu is frame-bound, but the text tries to solve it by naming QL. | Use QL only as a suspicion cue; apply search patterns to generation and regime movement. |
| Cell-like service jump | A service is called cell-like because it has a boundary or internal state. | Unpack service facets first: boundary, controlled exchange, internal state, health maintenance, adaptive behavior, coupling protocol, resource-metabolism analogue, protected invariants, repair, and state-continuity. Retain the analogy only when it changes a boundary, viability, repair and state-continuity, or resource-exchange decision. |

Near-miss taxonomy:

| Near miss | Why not QL by itself |
| --- | --- |
| Feedback loop | Ordinary dynamics/control unless admissible reading, export, or comparison is affected. |
| Metric gaming | Ordinary metric/incentive problem unless measurement publication changes the state reading. |
| Uncertainty | Ordinary epistemic uncertainty unless context, probe, or frame changes variable identity or comparison law. |
| Complexity | Ordinary complexity unless shortcut, export, or probe issue remains. |
| Compression | `A.6.3.CSC`, `A.6.3.RT`, modeling, or implementation pattern first; QL only for state-representation residue. |
| DDD bounded context | `A.6` / `F.9` first; QL only if workshop, probe, or export changes state reading. |
| Low-bit or quantized implementation | Engineering representation first; not QL because it is "quantized". |
| Collective behavior | `A.15`, distributed cognition, routines, and evidence patterns first; QL only for low-recoverability state-reading residue. |

#### C.26:8.1 - Cluster conformance scenarios

Use these as quick applicability tests. A good C.26 use leaves one practical output, not just a clever label.

| Scenario | Expected route | Avoid | Expected output |
| --- | --- | --- | --- |
| Dashboard readiness improves because teams optimize the displayed metric. | `C.16` / `A.15` first; `C.26.1` only if the output is reused as a passive readiness read after state-shaping publication. | Treating the dashboard value as release evidence by itself. | Redesign metric publication or add independent work traces before release use. |
| Workshop "discovers" a boundary but also creates alignment and local meaning. | `A.6` / `A.15` first; `C.26.1` for false pre-probe discovery reading. | Exporting the workshop result as a timeless domain fact. | Record window, participants, carriers, unresolved rivals, and bridge/export limits. |
| API read warms cache and changes downstream timing. | Interface semantics, `A.6`, and `C.16` first; `C.26.1` if the read result is reused as passive state export. | Saying the API read simply copied state. | Mark the read as non-neutral for that timing window or redesign the read path. |
| Two service health reports use different measurement frames. | `C.16` / `F.9` first; `C.26` only if no admissible shared comparison frame remains. | Averaging the scores as one posterior-looking value. | Name the frame difference and either build an admissible comparison route or stop comparison. |
| Team survey says "aligned", but incident behavior contradicts it. | `A.10` / `A.15` / `B.3` first; `C.26.2` if coordinated work traces support a low-recoverability distributed-state reading. | Treating survey output as the team state. | State a low-recoverability carrier/window-bound reading and the rival explanations. |
| Market "expects" a feature because many actors change behavior. | Declare bearer/traces; ordinary market, incentive, and evidence explanation first; `C.26.2` only for residual low-recoverability state reading. | Inventing a market mind. | Name actor traces, window, rivals, and the least-supported behavior-based reading. |
| Latency is green while support load and customer promise degrade. | `C.25` / `C.16` first; `C.26.3` if viability reading is probe/export/frame/coarsening-distorted. | Calling one green metric viability. | Add envelope variables, actuators, costs, and failure mode. |
| Summary compresses an architecture decision for executives. | `A.6.3.CSC` first; no QL unless a state-representation shortcut has QL residue. | Treating the summary as full architecture state. | Use for orientation only; return to source for release or design lock. |
| Diagram translates the same system into graph form. | `A.6.3.RT` first; no QL unless incompatible representation, probe, or export cue remains. | Calling any diagram a QL state model. | Declare representation-scheme change, reasoning-medium change, and source tether. |
| Low-bit model approximates expensive simulation. | Modeling, approximation, compression, or implementation pattern first; QL only if the shortcut claim depends on QL state, probe, or frame admissibility. | Treating low-bit or linear form as QL activation. | Name baseline, shortcut, loss budget or error budget, ordinary alternatives, and reopen trigger. |
| Assurance load is raised only because the word "quantum-like" appears. | Keep QL-lite unless decision, release, audit, reusable-law, comparative, formal, or ontology-bearing claim exists. | Escalating because of vocabulary alone. | Keep recognition or local-working support posture, or retire QL if ordinary patterns now carry the residue. |
| Author claims QL is faster or better than a classical method. | Require baseline, metric, mechanism, evidence or formal argument, loss/use declaration, ordinary alternatives, and reopen trigger. | Accepting superiority rhetoric. | Either write the claim declaration or remove the speed/superiority claim. |

QL can also generate better design options:

| Problem | QL-inspired design option |
| --- | --- |
| Dashboard changes behavior destructively. | Delay publication, split private/public metrics, add independent sampling, or publish confidence/loss boundaries. |
| Workshop creates alignment but masquerades as discovery. | Record pre-workshop hypotheses, post-workshop commitments, and created boundary meaning separately. |
| API read disturbs state. | Add non-mutating read, shadow read, sampling window, idempotence declaration, or separate observation channel. |
| Metrics in two contexts are not comparable. | Build a bridge/coupling record or stop comparison. |
| Summary is overused as source. | Add admissible-use label and return-to-source trigger. |
| Viability scalar hides damage. | Build envelope variables and actuators; add a failure-mode sensor. |

#### C.26:8.2 - AI and LLM work-cycle route examples

LLM-mediated work cycles often create the same representational mistakes C.26 repairs: false passive read, false faithful summary, false shared comparison frame, and shortcut without loss/use declaration. This does not make LLMs quantum-like.

| AI case | Route |
| --- | --- |
| LLM summary of an architecture record | `A.6.3.CSC`, `A.6.3.RT`, and `A.10` first; C.26 coarsening only if a state-representation shortcut is being overused. |
| Prompted model evaluation changes model or prompt behavior | `C.16` / `B.3` first; `C.26.1` only if the eval output is treated as a passive model-state read. |
| Agent work cycle "discovers" requirements | `A.15` / `A.10` / `A.6` first; `C.26.1` only if the interaction created the requirement framing. |
| Synthetic personas "represent market state" | `A.10` / `B.3` first; `C.26.2` only if a low-recoverability state-reading claim is carefully bounded with non-admissible use visible. |

### C.26:9 - Consequences

This pattern gives FPF a single place to define QL-lite and the inherited non-quantum boundary. That reduces repeated disclaimers in child patterns and makes ordinary use lighter.

Cluster success criteria:

| Criterion | Good indicator |
| --- | --- |
| Fewer false passive reads | Dashboards, workshops, API reads, and reports are less often treated as neutral state copies. |
| Fewer invalid comparisons | Same-named metrics from different contexts are not silently compared. |
| Better bridge records | `F.9` records more often include admissible export use and non-admissible export use. |
| Better release/evidence discipline | `B.3` / `A.10` are invoked only when the claim’s evidence or authority demand requires them. |
| Less metaphorical leakage | Fewer `field`, `collapse`, `entanglement`, and `group mind` phrases appear in normative text. |
| Faster local notes | Practitioners can write QL-lite notes without full audit cards. |
| More retirements | QL wording is removed when ordinary FPF patterns carry the claim. |

The best outcome may be fewer but better QL mentions.

Do not retrofit QL into existing FPF examples merely because they involve measurement, context, service boundaries, feedback, coarsening, or distributed work. Patch only examples where a named false passive read, false shared frame, false faithful export, low-recoverability distributed-state reading, or QL-specific coarsening residue changes the decision.

The cost is authoring discipline. A writer must name the ordinary FPF pattern, the actual QL cue, and the local stop. That is more work than saying "context matters", but it prevents the most expensive mistake: treating a changed, thinned, or frame-bound representation as if it were a full state.

The state-representation coarsening card makes speed and tractability claims more honest. It lets teams use cheaper state descriptions while keeping loss and reopen conditions visible.

### C.26:10 - Rationale

The cluster stays small on purpose. A single giant "Quantum-Like Architecture" pattern would hide distinct modeling concerns. Scattering the lens across local pattern bodies would repeat the same definition and boundary notes. This modeling-lens pattern lets the common lens live once while child patterns carry their own governed objects.

The key rule is simple: quantum-like is not quantum. Once that is typed, FPF can use the math lens normally. The lens earns its keep when it prevents a passive-read, one-space comparison, faithful-copy, or exact-state shortcut.

Evidence is not prestige. Literature supports the modeling move; local evidence supports the local state, export, or probe claim. A source anchor can justify why order effects, contextual probability, instrument-like readings, or open-system modeling are legitimate modeling patterns. It does not prove that this dashboard changed this team's state, that this workshop changed a boundary, or that this export lost the live coordination. That proof or evidence still belongs under `A.10`, `C.16`, `A.15`, `B.3`, and the ordinary pattern for the local claim.

### C.26:11 - SoTA-Echoing

| Pattern claim | Practice source | Pattern implication |
| --- | --- | --- |
| Mathematical objects can be transferred as modeling lenses without claiming the target domain is made of the source-domain stuff. | Wigner on mathematical usefulness, Jaynes on probability as logic of science, and Khrennikov on quantum formalism outside physics. | Treat QL as a math-lens transfer card: explain the useful structure first, then state the inherited boundary. |
| Quantum-like is a mathematical or representational modeling lens, not a physical claim about the modeled system. | Basieva, Khrennikov, and Ozawa on quantum-like modeling in biology with open-system and instrument language. | Keep `QL-NQ` as non-entailment, not as the main claim; use detached mathematical modeling where state, probe, or export cue is real. |
| Linear quantum-like representation can make selected information-state processing more tractable if the representation and loss profile are declared. | Basieva-Khrennikov-Ozawa linearity / speed-up / stability arguments and finite-dimensional matrix-calculus discussions. | Support the state-representation coarsening card discipline; block blanket "quantum-like is faster" claims unless baseline cost, shortcut, loss, and reopen trigger are named. |
| Quantum probability is useful where inference is contextual, previous judgments change state, or possibilities interfere, but QL is not automatically the only formal route. | Quantum cognition work, quantum-instrument work, and process-theory cautions about classical instrument alternatives. | Use QL-lite as useful abstract modeling, not as proof of non-classical necessity. |
| DDD, microservice, active-inference, and measurement practice already supply ordinary FPF patterns. | DDD and microservice domain analysis, active-inference measurement-as-action work, performative prediction, metric-induced behavior. | Keep ordinary FPF patterns first; add QL only for the remaining state, probe, export, frame, or coarsening cue. |


#### C.26:11.1 - Selected operational source anchors

This section is intentionally short. It carries operational anchors for using the pattern, not an expanded bibliography.

| Claim | Source family | Practical implication |
| --- | --- | --- |
| Mathematical formalisms can be transferred as modeling lenses without claiming the target domain is made of the source-domain stuff. | [Wigner on mathematical usefulness](https://www.organism.earth/library/document/unreasonable-effectiveness-of-mathematics), [Jaynes on probability as logic](https://openlibrary.org/books/OL22584017M/PROBABILITY_THEORY_THE_LOGIC_OF_SCIENCE), and Khrennikov's quantum-like modeling line. | Treat QL as a math-lens transfer: name the useful structure, the ordinary FPF pattern, and the local stop before any claim requiring additional evidence or authority. |
| Quantum-like open-system and instrument formalisms can model state and probe interaction without physical quantum ontology. | [Basieva, Khrennikov, and Ozawa](https://www.sciencedirect.com/science/article/pii/S0303264720301994) and [arXiv](https://arxiv.org/abs/2010.15573), plus [Khrennikov on open systems](https://www.mdpi.com/1099-4300/25/6/886). | Keep `QL-NQ` central and use QL only where probe, instrument, open-information-system update rule, probe frame, export admissibility, or state export cue changes the admissible reading. |
| Question order, contextual judgment, and instrument-like operations are practical cues, but not automatic proof that QL is necessary. | [Quantum instruments for question-order effects](https://www.sciencedirect.com/science/article/pii/S0022249620301152), [Quantum Cognition](https://www.annualreviews.org/content/journals/10.1146/annurev-psych-033020-123501), and [process-theory non-exclusivity](https://arxiv.org/abs/2604.08604). | Use QL-lite when order/frame/probe effects change the result; keep classical instrument, Bayesian, causal, and ordinary measurement rivals live. |
| Same-content-looking measurements under different probe or measurement frames should not be silently treated as the same random variable or as jointly distributed. | [Contextuality-by-Default](https://www.sciencedirect.com/science/article/abs/pii/S0022249616300207). | Use QL when the frame changes variable identity, joint availability, or admissible comparison; otherwise keep the ordinary measurement, bridge, or bounded-context pattern. |

| Viability and active sensing often mix reading and acting, but ordinary control and measurement patterns remain primary. | [Free-energy and quantum-cognition link](https://www.frontiersin.org/articles/10.3389/fnbot.2022.910161/full), [physiological regulation and FEP](https://www.sciencedirect.com/science/article/pii/S0149763423004281), [active inference behavior](https://www.sciencedirect.com/science/article/pii/S0301051123002612), and [smart-building active inference](https://arxiv.org/abs/2503.18161). | For viability cases, name sensors, probes, actuators, and envelope variables first; retain QL only for remaining probe, frame, export, or coarsening cue. |
| Boundaries and contexts are already disciplined by ordinary architecture and DDD practice. | [Computational boundary of a self](https://philpapers.org/rec/LEVTCB-3), [Markov blankets of life](https://philarchive.org/rec/KIRTMB), [Azure domain analysis](https://learn.microsoft.com/en-us/azure/architecture/microservices/model/domain-analysis), and [DDD 2025 SLR](https://www.sciencedirect.com/science/article/pii/S0164121225002055). | Apply ordinary FPF patterns first to boundary, interface, bounded-context, bridge, and microservice questions; add QL only where the interaction changes the state or export being read. |
| Low-bit, tokenized, compressed, geometric, or neural representations may be useful shortcuts without being QL activation. | [1-bit LLMs](https://arxiv.org/abs/2402.17764), [implicit continuity in language models](https://arxiv.org/abs/2504.03933), [emergent quantumness in neural networks](https://arxiv.org/abs/2012.05082), and [covariant gradient descent](https://arxiv.org/abs/2504.05279). | Keep implementation substrate, geometry, compression, and representation shortcuts in ordinary FPF patterns unless a declared QL cue changes the admissible use. |
| Unknown alternatives and regime movement are search/generation problems, not QL claim authority. | [Open-endedness](https://arxiv.org/abs/2406.04268) and [quality-diversity through AI feedback](https://openreview.net/forum?id=owokKCrGYr). | Use QL only to mark a suspect frame; apply search or regime patterns to generation of alternatives. |


### C.26:12 - Relations

**C.28 causal-use relation.**

- C.28 governs causal-use question, causality-ladder rung, causal estimand, identification, counterfactual sampling realizability, causal evidence support basis, causal-use verdict, causal fairness, causal policy, and causal method parity.
- This pattern keeps residual quantum-like probe, frame, order, export, or coarsening discipline after ordinary causal-use explanation has been tried.
- Non-admissible use: intervention, causal effect, causal fairness, causal policy, counterfactual comparison, causal method parity, or counterfactual-rung-data realizability do not activate quantum-like modeling by themselves.
- Exit: when the live question is causal, cite `C.28` before retaining QL-lite or QL-NQ.


**C.27 temporal-claim relation.**

- C.27 may flag: ordinary state/rate/rate-change, effort-window, rhythm, braking, coasting, or intervention-timing claims before any quantum-like cue is considered.
- This pattern keeps: residual quantum-like probe, frame, order, export, or coarsening discipline.
- Non-admissible use: discreteness, finite differences, typed states, state-space reduction, tokenization, dashboards, probes, measurement plans, speed words, rhythm words, or Dyn2 words do not activate quantum-like modeling by themselves.
- Exit: use C.27 and ordinary FPF patterns first; use C.26 only where residual probe, frame, order, export, or coarsening cue remains after those relations are named.


- Builds on: `E.8`, `E.9`, `C.11`, `C.16`, `C.25`, `A.6`, `A.6.P`, `F.9`, `A.15`, `A.10`, `B.3`, `A.3`, `C.18`, `C.19`, `A.19`.
- Constrains: QL wording in `C.26.1`, `C.26.2`, and `C.26.3`.
- Carries: state-representation coarsening as a card inside `C.26:4.5`, not as a separate pattern.
- Does not cover: physical quantum claims, a generic probe ontology, a generic state ontology, a service/cell pattern, or a field-like synchronization pattern.
- Name posture: `Quantum-Like Modeling Lens` is a pattern label for a modeling lens and modeling discipline, not `U.Lens`, not `QuantumLikeArchitecture`, not `Quantum Substrate`, not `Quantum Ontology`, and not a universal architecture doctrine.

### C.26:12b - C.29 MLA relation

> `C.26` is an MLA-compatible specialization for quantum-like modeling. It carries a pre-filled adequacy profile for QL work: preserved structure includes order, probe, and contextual-probability effects when supported; lost structure includes physical quantum ontology; the canonical stop condition remains `QL-NQ`. A QL-lite note does not inherit a blank full MLA card. A full MLA-compatible profile is needed only when the QL claim is decision-bearing, reusable, publication-bearing, assurance-bearing, bridge-bearing, or formal-model-bearing.

### C.26:End
## C.26.1 - Probe-Coupled Boundary Interaction

> Type: Architectural pattern
> Status: Stable
> Normativity: Normative unless explicitly marked informative

### C.26.1:1 - Problem frame

Use this pattern when a boundary read, meeting, metric, API read, dashboard, workshop, survey, split, bridge, or message is being used as if it merely revealed or transferred state, but the probe or interaction changes the represented state enough to alter the architecture decision.

This is the main everyday entry into the QL cluster. It is useful because many teams already know how to talk about boundaries, interfaces, metrics, and workshops. The missing move is to notice when the act of reading or crossing the boundary participates in the state being read.

| Working surface | Value |
| --- | --- |
| Primary reader | Architect, platform lead, domain modeler, or manager judging a boundary read, workshop, dashboard, metric, API read, or bridge result. |
| Governed object | A boundary interaction being used as evidence, export, comparison, or decision input. |
| Governed move | Replace false passive-read or unjustified lossless-transfer wording with a probe-coupled boundary decision and reroute where needed. |
| Outside work | Ordinary message passing, ordinary causal intervention, ordinary API semantics, bridge loss alone, and generic relation-token minting. |
| What changes in practice | The team records what the probe changed before using its output as architecture evidence. |

Plain glosses:
- `passive read`: treating a workshop, metric, dashboard, API read, survey, or message as if it only reports state.
- `probe-coupled`: the read/export/intervention participates in the represented state enough to change the lawful decision.
- `coupling channel`: the concrete workshop, metric, message, API, dashboard, meeting, bridge, or event stream through which the effect travels.
- `export loss`: what the carried output cannot faithfully carry into another context or decision.

### C.26.1:2 - Problem

Architecture work often treats boundary interactions as passive. A dashboard "shows readiness". A workshop "discovers the context map". An API read "returns state". A meeting "collects alignment". A message "transfers a decision".

Sometimes that is good enough. Sometimes it is false for the current decision. Publishing the dashboard changes readiness behavior. Running the workshop changes alignment and local meaning. Reading the API changes timing assumptions. Sending the message changes trust, escalation, or error handling. Splitting the service changes the viability envelope that the split was meant to optimize.

When the false passive reading survives, the team may keep the wrong boundary, trust the wrong export, combine incomparable outputs, or redesign the system around an artifact that partly created what it reports.

### C.26.1:3 - Forces

| Force | Tension |
| --- | --- |
| Boundary discipline vs probe sensitivity | `A.6` and `F.9` already govern boundaries and bridges; this pattern adds only the state-changing or export-changing probe relation. |
| Intervention vs readout | Many actions change the world ordinarily. QL is active only when the action is being used as a read, export, comparison, or optimization of the state it changes. |
| Lean use vs evidence-support class | A working team needs a small card; release, audit, or measurement claims need evidence and measurement-governing patterns or records. |
| Coupling words vs relation tokens | Words such as coupling, interaction, and export are plain explanatory wording until `A.6.P` / `F.18` ratifies a reusable relation token. |

### C.26.1:4 - Solution

Before accepting a passive read or unjustified lossless-transfer reading, ask whether the probe or interaction changed what the output may admissibly mean.

C.26.1 is active only when the interaction both participates in the represented state and its output is being used as evidence, export, comparison input, or decision input as if it were passive. Mere behavior change, ordinary feedback, or ordinary influence is not enough.

A probe-coupled interaction may be useful and intentionally state-shaping. The repair is not to avoid it; the repair is to stop using its output as if it were a neutral pre-probe read.

Start with this recognition note:

| Mini-entry | Question |
| --- | --- |
| Ordinary governing pattern | Which ordinary FPF pattern already carries the baseline boundary, bridge, measurement, work, or viability question? |
| False passive read | Which reading would be false: "the dashboard, workshop, API read, survey, message, or bridge just reports state"? |
| Probe effect | What changed because of the probe, intervention, export, order, frame, or boundary crossing? |
| Practical change | What does the team do differently now: mark probe-coupled, redesign the probe, order, or frame, rewrite bridge or export, add evidence, or apply a neighboring FPF pattern? |
| Stop or neighboring-pattern handoff | Which use is unsupported by this note, and which FPF pattern carries that use? |

Use the fuller decision-bearing record below when the boundary result will be reused, contested, used as evidence, or used to change an architecture decision.

Full decision-bearing record:

| Field | Question |
| --- | --- |
| Boundary | Which boundary, role relation, authority relation, context bridge, service interface, team boundary, or system edge is crossed or queried? |
| Probe or interaction | Which workshop, dashboard, API read, metric, meeting, survey, message, event stream, or other typed probe lane is active? |
| QL cue or formal cue | Which instrument-like update, order sensitivity or frame sensitivity, incompatible-probe structure, no faithful-enough export under the declared probe, frame, or use, or mutual interaction whose local reads and exports are no longer admissibly comparable or reusable without declaring the probe, frame, or update relation makes ordinary passive-read wording false? |
| False passive reading | What discovery, neutral observation, one-way transfer, or unjustified lossless-message reading would be false? |
| Pre-probe hypothesis | What did the team think the boundary state, alignment, readiness, context cut, or export validity was before the probe? |
| Observed or inferred post-probe state | What changed, stabilized, became visible, became non-exportable, or lost admissible use because of the probe or interaction? |
| Update class, if load-bearing | Is the update a system change, work change, epistemic reading update, carrier update, emitted-output update, formal model update, or update-law change? |
| State-change evidence | Which traces, changed decisions, changed labels, changed priorities, behavior shifts, timing changes, or export failures support the state-change reading? |
| Uncertainty / confidence posture | What remains inferred, approximate, disputed, probe-dependent, or not yet distinguishable? |
| State history / memory, if load-bearing | State this only when path dependence, order effect, hysteresis, or retained trace changes the current lawful reading. |
| Decision | What changes now: mark probe-coupled, redesign probe, order, or frame, add evidence, rewrite bridge or export, split, merge, orchestrate differently, or apply a neighboring FPF pattern? |
| Decoupling / redesign option | Can the probe, order, frame, bridge, metric, dashboard, API read, or boundary interaction be redesigned so the needed output is less state-changing or more faithfully exportable? |

#### C.26.1:4.1 - Activation boundary

This pattern is active only when the interaction both participates in the represented state and its output is being used as evidence, export, comparison input, or decision input as if it were passive. A passive-read, unjustified lossless-transfer, one-way-message, or ordinary-bridge treatment must be materially false for the current decision.

Ordinary influence is not enough. A meeting that changes attention is ordinary work unless the meeting output is later used as a passive reading of alignment. An API call that is a mutating operation by its interface semantics is ordinary service/API semantics unless the call result is used as a neutral state export. A feature flag that changes behavior is ordinary intervention unless the flag readout is being used as evidence of the state it changes.

Performative prediction is also an important ordinary rival. If a prediction, score, or metric changes behavior because people act on it, but no incompatible probe frame, order-sensitive reading, contextual-probability cue, or instrument-like state/export support load remains, try performative-prediction analysis and the ordinary `C.16`, `A.10`, and `B.3` patterns first. Keep C.26.1 only for the residual probe admissibility question.


#### C.26.1:4.2 - Finish conditions

The pattern emits one of these results:

| Result | Meaning |
| --- | --- |
| Keep boundary, mark probe-coupled | The boundary remains, but the read/export is no longer treated as passive. |
| Redesign probe/order/frame | The workshop, dashboard, API read, survey, metric, or question order changes to reduce distortion. |
| Redesign bridge/export | The bridge/export gains loss notes, use scope, confidence, and return-to-source path. |
| Split/merge/orchestrate differently | Boundary structure changes because the interaction changes the phenomenon. |
| Apply `F.9` | Only bridge and loss remains live. |
| Apply `C.16` | The probe is really a standard measurement with declared scale, method, evidence, and result. |
| Apply `A.15` | The hard part is work enactment rather than probe-coupled reading. |
| Apply `C.25` | Viability-envelope regulation is primary. |

#### C.26.1:4.3 - Probe-coupled context-cut worked use slice

This worked use slice is not a standalone pattern. It tests DDD and bounded-context work when the context cut is not only discovered but also changes meaning, coordination, export validity, or viability.

Ask: was the bounded-context cut merely discovered, or did the workshop, dashboard, API extraction, bridge, split, merge, or orchestration change alignment, ownership, vocabulary, export validity, or viability?

| Slice field | Example content |
| --- | --- |
| Case | A product organization considers splitting payment handling out of a checkout bounded context after repeated payment-failure incidents. |
| Ordinary DDD finding | Checkout and Payment use different local meanings for `Order.status`, `PaymentFailure`, and `Retryable`; an ordinary `F.9` bridge is needed. |
| Probe / intervention | The event-storming workshop starts from payment-failure dashboards and asks teams to place incidents by owner, customer impact, and recovery path. |
| Post-probe reading | Product, Support, and Payment start treating payment failure as a customer-risk gate, not only a technical retry condition. |
| Evidence | Incident labels are reclassified, escalation changes, backlog priority changes, and the dashboard query is rewritten. |
| Export loss | Copying `PaymentFailure = customer risk` into both contexts loses the difference between retryable technical failure, promise breach, and support escalation trigger. |
| Decision output | Keep the split, mark the workshop result as probe-coupled, add `F.9` loss notes, and add a payment-risk escalation promise to the boundary design. |

#### C.26.1:4.4 - Governed object and operational sequence

The governed object is a boundary interaction used as evidence, export, comparison input, or architecture decision input. The interaction may be a meeting, question sequence, dashboard, metric, API read, survey, workshop, event stream, canary, test harness, service split, bridge, message, or management review. The pattern is active only when that interaction participates in the represented state enough that passive-read or unjustified lossless-transfer wording would change the decision.

The pattern governs one move: convert an apparently passive boundary read into a typed probe-coupled boundary decision. That decision says what the interaction read, what it changed, what the output can support, what it cannot support, and which neighboring FPF pattern takes over if the question is really bridge, measurement, evidence, work, decision, or viability.

Action path:

1. Name the boundary or relation being crossed.
2. Name the probe lane, including the concrete artifact or work act that produced the output.
3. State the false passive reading: what the team would have assumed if the probe were only a window.
4. State the pre-probe hypothesis and the observed or inferred post-probe state.
5. State the evidence carriers and uncertainty posture.
6. State the export loss, memory, order effect, or frame effect that makes the output not faithful enough for the declared use.
7. Choose the finish result: keep boundary with probe note, redesign probe, order, or frame, redesign bridge or export, change the split, merge, or orchestration, or apply a neighboring FPF pattern.

Required output: produce a probe-coupled interaction reading, a corrected use of the output, and, when it would reduce the problem, a redesign or decoupling move for the probe, order, frame, bridge, metric, dashboard, API read, or boundary interaction.

This sequence is deliberately small. It is the boundary analogue of the `C.11` local choice pass: the pattern should end with a usable result, not with a richer vocabulary label.

#### C.26.1:4.5 - Well-formed probe-coupled boundary state

A probe-coupled boundary decision is usable only when the record states all of the following:

- the boundary, context bridge, service interface, team boundary, role relation, authority relation, or system edge involved;
- the probe lane and output carrier;
- the state reading before the interaction and the state reading after the interaction;
- the state-change evidence, including traces, changed labels, changed priorities, changed timings, changed routines, changed bridge fields, or changed downstream decisions;
- the local stop condition: which use the output does not support without another pattern;
- the neighboring FPF pattern that would carry the other claim.

The record is unfinished when any of these remains true:

- the output is named, but the operation that produced it is hidden;
- the operation is named, but the state that changed is not named;
- the state changed, but the decision that changes because of that fact is not named;
- the bridge/export loss is stated only as a vague warning rather than as a concrete non-admissible use;
- the same interaction is alternately treated as evidence, command, measurement, and bridge without role split.

The minimal admissible output is often enough: "this dashboard value is probe-coupled evidence for readiness behavior under window W"; "this workshop work changed alignment and therefore the workshop note cannot be treated as passive discovery"; "this API read is a non-neutral observation under these interface semantics"; "this context cut needs both `F.9` bridge loss and C.26.1 probe-coupling treatment."

#### C.26.1:4.6 - Probe, observable, output, and carrier split

Do not identify the thing being asked with the method that asks it, the output that appears, or the output carrier.

| Role | Boundary-facing question |
| --- | --- |
| Observable or output dimension | What readiness, status, alignment, failure, response, risk, split, promise, or boundary condition is being read? |
| Probe method | Which dashboard, API read, workshop order, survey, canary, incident review, event stream, or meeting format acts on the situation? |
| Measurement / interaction scheme | What timing, threshold, sampling rule, question order, aggregation, publication path, or access path shapes the output? |
| Output or result record | What score, label, context map, API response, survey answer, incident class, readiness status, or bridge field was emitted? |
| State update | What behavior, alignment, meaning, trust, priority, escalation, or timing changed because of the probe? |
| Evidence carrier | Which log, dashboard export, meeting note, trace, decision record, ticket history, context map, or API result carries the output? |

This split prevents a common mistake: "the dashboard says ready" hides at least four objects. The dashboard definition, the displayed result, the behavior it changes, and the readiness decision are distinct.

#### C.26.1:4.7 - Reroute and disambiguation guide

Use this guide when a draft says that a boundary, system, team, or service is "coupled", "aligned", "interacting", "measured", "exported", "synchronized", or "read".

| Trigger surface | First question | If yes | If no |
| --- | --- | --- | --- |
| "The dashboard shows readiness." | Did publishing or using the dashboard change readiness behavior, escalation, staffing, or release posture? | Use C.26.1; state probe, update, evidence, and admissible use. | Use `C.16`, `A.10`, `B.3`, or ordinary reporting. |
| "The workshop discovered the boundary." | Did question order, framing, participants, or artifacts change local meaning, ownership, trust, or viability? | Use C.26.1 with this context-cut worked use slice; add `F.9` if bridge/export loss is live. | Use ordinary DDD / `F.9` bounded-context work. |
| "The API read returns state." | Is the read path state-changing under interface semantics, timing, cache, consistency, or downstream behavior? | Use C.26.1 if the result is later treated as a passive read. | Use ordinary API semantics, measurement, or data freshness. |
| "The message transferred the decision." | Did the message change authority, trust, escalation, timing, or local meaning enough that copy or transfer is false? | Use C.26.1 and apply the relevant work or authority pattern to commitments or authority. | Use publication, bridge, or work enactment patterns. |
| "The split improved viability." | Did the split/probe alter the viability envelope being evaluated? | Coordinate with `C.26.3`. | Use ordinary boundary, quality-bundle, or architecture patterns. |

When relation wording is load-bearing, do not mint a relation token here. Keep the sentence as local explanatory prose or apply `A.6.P` or `F.18` to reusable relation work.

#### C.26.1:4.8 - Positive examples and near misses

| Case | Supported C.26.1 use | Near miss and neighboring-pattern handoff |
| --- | --- | --- |
| Readiness dashboard | The readiness score changes team behavior: teams stop surfacing borderline failures because the dashboard is watched by release management. The score is probe-coupled evidence, not a passive readiness copy. | If the dashboard only reports a well-defined measure with no behavior-changing or frame-changing effect, use `C.16` plus evidence patterns. |
| API consistency check | A "read" through a cache warms entries and changes later latency, so the readout changes the performance state later used in the decision. | If the call is simply a mutating operation by interface semantics, use ordinary API/work semantics and say so plainly. |
| Survey order | Asking "who owns incidents?" before "which context owns payment failure?" changes the resulting context map and escalation plan. | If different answers merely reveal unresolved meanings, use `F.9` / `A.6.P` first. |
| Event-storming workshop | The workshop produces a map and also changes team alignment, local vocabulary, and backlog priority. | If it only documents known differences, use ordinary DDD and bridge fields. |
| Service split | Splitting Checkout and Payment changes recovery paths and support load, so the split is part of the phenomenon being evaluated. | If the split only reduces deployment coupling with no probe/export effect, use ordinary boundary and quality patterns. |
| Incident metric | Publishing "cache failover is the primary risk" shifts attention, staffing, and reproduction work. | If the metric is only a report of already-carried evidence, use `A.10` / `B.3`. |

The positive examples are intentionally ordinary. QL value here is not exotic formalism; it is noticing that a read, metric, workshop, or interface often participates in the state it later claims to report.

#### C.26.1:4.9 - Evidence posture for probe-coupled claims

Use the least-committing evidence posture that still supports the intended use.

| Evidence posture | Admissible use | Typical carriers |
| --- | --- | --- |
| `QLP-0` recognition | Flag a likely probe-coupled situation for local discussion. | Meeting note, dashboard screenshot, issue comment, context-map draft. |
| `QLP-1` local working use | Change a local probe/order/frame, bridge note, or boundary decision in a team setting. | Before/after labels, changed tickets, changed dashboard query, changed escalation path, changed architecture note. |
| `QLP-2` decision-bearing / reusable use | Publish as a repeatable FPF example or organization guideline, or use the reading in a local decision with consequence. | Multiple cases, comparison with ordinary routes, named uncertainty, near-miss cases. |
| `QLP-3` assurance or reusable-law use | Use in release, audit, contractual, reusable-law, or high-impact decision support. | Evidence graph, measurement method, assurance tuple, traceable source references, rival explanation comparison. |

Do not make `QLP-3` the ordinary entry cost. Most practical C.26.1 use lives at `QLP-0` or `QLP-1`, with escalation only when the output is reused or carries higher consequence.

### C.26.1:5 - Archetypal Grounding


Tell: A team runs a service-boundary workshop after a series of incidents. The first map says "Payments is separate from Checkout". A week later, incident triage and backlog priorities have changed because the workshop reframed payment failure as a customer-promise risk.

Show, System side: the teams, services, dashboards, event stream, workshop format, and escalation routine are part of the boundary situation. The workshop is not only a carrier of information; it changes alignment and future work.

Show, Episteme side: the minimal evidence-bound claim is not "the workshop discovered the true topology." It is "the workshop work functioned as a probe lane that changed the represented boundary state and exposed export loss across Checkout and Payment." The next admissible move is a boundary or probe decision plus `F.9` bridge notes.

### C.26.1:6 - Bias-Annotation

This pattern biases authors against passive-reading convenience. That bias is useful when dashboards, workshops, surveys, and API reads are treated as if they carry state without changing it.

The pattern also biases authors against overusing QL. It keeps ordinary intervention, ordinary message passing, ordinary bridge loss, ordinary API semantics, and ordinary work enactment with their existing FPF patterns when no probe-coupled reading remains.

### C.26.1:7 - Conformance Checklist

| ID | Check |
| --- | --- |
| CC-C26.1.1 | The boundary, role relation, authority relation, bridge, split, or queried system edge is named. |
| CC-C26.1.2 | The active probe or interaction lane is typed as work, method, measurement, speech act, interaction channel, evidence carrier, bridge/export act, or API/service operation; any quantum-instrument wording is recorded only as a modeling analogy unless formalized elsewhere. |
| CC-C26.1.3 | Observable, probe method, measurement scheme or interaction scheme, emitted output or result record, update class, and evidence carrier are separated when they carry the claim. |
| CC-C26.1.4 | The QL cue or formal cue is named, or the case is handled without QL wording. |
| CC-C26.1.5 | The false passive reading or unjustified lossless-transfer reading is stated. |
| CC-C26.1.6 | The pre-probe hypothesis and observed/inferred post-probe state are stated without fake precision. |
| CC-C26.1.7 | State-change evidence and uncertainty/confidence posture are stated. |
| CC-C26.1.8 | State history, memory, path dependence, or order/frame sensitivity is stated when load-bearing. |
| CC-C26.1.9 | The state change, export loss, or viability change caused by the probe/interaction is stated. |
| CC-C26.1.10 | The output is one of the pattern finish conditions. |
| CC-C26.1.11 | The decoupling, probe-redesign, order-redesign, frame-redesign, bridge-redesign, or boundary-redesign option is stated when it could reduce the problem. |
| CC-C26.1.12 | The local evidence posture is stated when the claim is reused, contested, or higher consequence. |
| CC-C26.1.13 | Ordinary intervention, bridge, work, measurement, and viability routes are tried before QL wording is retained. |
| CC-C26.1.14 | Coupling or interaction wording is not minted as a reusable relation token without `A.6.P` / `F.18`. |
| CC-C26.1.15 | The pattern inherits `QL-NQ` from `C.26` instead of restating the inherited boundary as local law. |

### C.26.1:8 - Common Anti-Patterns and How to Avoid Them


| Anti-pattern | Symptom | Repair |
| --- | --- | --- |
| Every interaction is QL | Any message, meeting, or API call is called probe-coupled. | Require a false passive-read, export, comparison, or optimization use. |
| Causal action mistaken for probe | A deployment or command changes the world, and QL is invoked. | Use intervention or work-governing patterns unless the action is being used as a readout of the state it changes. |
| Bridge loss alone | Export loses local meaning, but no state-changing probe is live. | Use `F.9` with loss notes. |
| Context-word drift | `context` means probe frame in one sentence and `U.BoundedContext` in the next. | Use `U.BoundedContext` only for semantic context; otherwise say probe frame, model frame, or measurement setup. |
| Relation token leakage | `coupledBy(...)` appears as if already ratified. | Keep it as local drafting form or apply `A.6.P` and `F.18`. |

### C.26.1:9 - Consequences

This pattern makes boundary decisions more honest. It turns "the workshop showed the split" into "the workshop both showed and changed the split-relevant state." It turns "the dashboard says ready" into "the dashboard is probe-coupled evidence with a limited decision use."

The cost is that some familiar artifacts lose false authority. Dashboards, workshops, surveys, API reads, and messages remain useful, but they no longer get to pretend they are always neutral windows.

### C.26.1:10 - Rationale

The pattern exists because boundary work is where the QL lens becomes practically visible fastest. Teams already experience dashboard effects, workshop effects, order effects, and bridge loss. The pattern gives those experiences a lightweight, typed, ordinary-pattern-compatible form.

The pattern is not a generic interaction theory. It is a boundary/probe repair for cases where passive read or unjustified lossless-transfer reading is materially false.

### C.26.1:11 - SoTA-Echoing

| Pattern claim | Practice source | Pattern implication | Adoption stance |
| --- | --- | --- | --- |
| A probe or instrument can produce both an output and a state update; the output alone does not specify the operation. | [Quantum-instrument modeling of question order, response replicability, and QQ-equality](https://www.sciencedirect.com/science/article/pii/S0022249620301152). | Ask what operation produced both output and update before treating dashboards, API reads, workshops, surveys, or metrics as passive reads. | Adapt the instrument/update lesson; do not import a full organization ontology. |
| Contextual judgment and order effects are common enough to be a practical modeling cue. | [Quantum Cognition](https://www.annualreviews.org/content/journals/10.1146/annurev-psych-033020-123501). | Treat question order, workshop order, and dashboard framing as possible state-shaping operations when they change the decision. | Adopt as a recognition cue with critical limits. |
| Classical instrument models may explain some sequential-decision data, so QL is useful but not uniquely necessary by default. | [Quantum-like Cognition in Process Theories: An Analysis](https://arxiv.org/abs/2604.08604). | Keep rival routes visible; QL remains a modeling lens, not a necessity claim. | Use as non-exclusivity discipline. |
| A prediction, score, or metric can change the target distribution because people act on it, without requiring a QL probe reading. | [Performative Prediction](https://proceedings.mlr.press/v119/perdomo20a.html). | Move dashboard-induced or score-induced behavior to performative-prediction and ordinary measurement, intervention, or work patterns unless a residual incompatible-probe, order, contextual-probability, or instrument-like export support load remains. | Adopt as a classical rival path that sharpens when C.26.1 is actually useful. |

| Boundaries can be modeled by what a system can measure, model, and affect, while mathematical boundary descriptions are not new worldly substances. | [The Computational Boundary of a Self](https://philpapers.org/rec/LEVTCB-3) and [The Markov blankets of life](https://philarchive.org/rec/KIRTMB). | Make the boundary/probe relation explicit without reifying the boundary or coupling phrase. | Adapt for boundary-function discipline. |
| Bounded-context and microservice practice already governs ordinary domain cuts and integration points. | [Use domain analysis to model microservices](https://learn.microsoft.com/en-us/azure/architecture/microservices/model/domain-analysis) and [DDD in software development: a 2025 SLR](https://www.sciencedirect.com/science/article/pii/S0164121225002055). | Use C.26.1 only when the cut, workshop, bridge, dashboard, API extraction, split, or merge changes represented boundary state or export validity. | Use DDD as baseline; add C.26.1 only for the probe-coupled support load. |

Worked-use-slice discipline from these rows:

- start from the ordinary FPF pattern before QL wording;
- show the concrete operation that produced the output;
- show the state update or export loss that changes the decision;
- keep relation tokens local unless `A.6.P` / `F.18` gives them a reusable declaration;
- keep source-formalism language as modeling support, not as pattern-body ontology.

### C.26.1:12 - Relations


- Builds on: `C.26`, `A.6`, `A.6.B`, `A.6.P`, `F.9`, `A.15`, `C.16`, `A.10`, `B.3`, `C.25`, `A.1.1`.
- Coordinates with: `C.26.2` when coordinated work evidences a non-exportable distributed state; `C.26.3` when the boundary interaction changes a viability envelope.
- Carries: a worked use slice inside `C.26.1:4.3`, not a standalone pattern or relation token.
- Does not mint: `U.Probe`, a new boundary kind, or reusable relation predicates.
- Name posture: `Probe-Coupled Boundary Interaction` names a boundary and probe relation, not `Entangled Boundary`, `CoupledBy(...)`, `Interaction Field`, `State-Changing Communication`, or a reusable relation token. Relation wording remains local until `A.6.P` and `F.18` ratify it.

### C.26.1:End
## C.26.2 - Enacted Distributed State Evidence

> Type: Architectural pattern
> Status: Stable
> Normativity: Normative unless explicitly marked informative

### C.26.2:1 - Problem frame

Use this pattern when coordinated work, behavior, or trace patterns give evidence that a team, organization, service mesh, market, or other collective system is acting from a state that no single participant report, survey, policy sentence, dashboard, or API export faithfully carries.

The pattern supports only a minimal evidence-bound claim. It lets an author say that coordinated work, behavior, or trace patterns are consistent with a distributed-state reading during a declared window, while keeping the claim tied to carriers, probes, rival explanations, and export loss.

| Working surface | Value |
| --- | --- |
| Primary reader | Architect, incident lead, organizational analyst, or manager judging whether coordinated work, behavior, or trace patterns evidence a minimal collective-state reading. |
| Governed object | An evidence-bound state reading over a declared collective `U.System`. |
| Governed move | Infer only the minimal carrier-bound and window-bound state claim, name rivals, and state export and probe limits. |
| Outside work | Group-mind ontology, survey-as-state, timeless culture claims, ordinary routine claims, and formal measurement not governed by `C.16`. |
| What changes in practice | The team can use coordinated work, behavior, or trace patterns as evidence without pretending one report faithfully exports the whole state. |

Plain glosses:
- `collective bearer`: the declared team, organization, service mesh, market slice, or other `U.System` whose coordinated work, behavior, or trace pattern is being read.
- `coordinated work or behavior`: role-work, service behavior, market participant traces, routine, commitment, artifact use, or coordinated action.
- `distributed-state reading`: a minimal evidence-bound interpretation of coordinated work or behavior, not a new hidden group entity.
- `carrier`: a log, trace, artifact, commitment, routine, dashboard, report, API response, or document that grounds but does not equal the state.
- `faithful-enough export`: a representation good enough for the current decision; when it is not faithful enough, state what was lost and why.

### C.26.2:2 - Problem

Teams often need to talk about latent alignment, readiness, market posture, service-mesh behavior, or an enacted "we already decided" before one explicit representation exists. Without a pattern, they oscillate between two bad options.

One option is magic language: "the organization knows", "the culture decided", "the market wants", or "the service mesh understands". The other option is false reduction: a survey answer, policy sentence, dashboard, or report is treated as the whole state.

Both fail. Coordinated behavior may evidence a real working state, but it does not automatically identify a durable mind, internal representation, causal mechanism, or faithful-enough export for the intended use.

### C.26.2:3 - Forces

| Force | Tension |
| --- | --- |
| Work evidence vs explicit report | Coordinated work may provide more direct evidence than any one report, but the report is often the only portable carrier. |
| Minimal evidence-bound claim vs useful claim | The pattern must say something useful without claiming group mind or durable hidden ontology. |
| Evidence vs measurement | Some cases have formal measures; many have traces, commitments, routines, and artifacts instead. |
| Export need vs export loss | The state often must be summarized for a decision, but the summary may lose the coordination that matters. |
| Primary source family vs QL lens | Distributed cognition, team cognition, routines, and socio-technical evidence are primary; QL enters only when probe, frame, or export effects are load-bearing. |

### C.26.2:4 - Solution

Model the claim as evidence-bound `U.Episteme` over a declared collective `U.System`. Do not make the distributed state a bearer-independent thing. Do not treat a survey, dashboard, report, or API response as the state itself.

If the bearer is a market slice or service mesh, declare whether it is a collective `U.System`, delivery system, trace population, or evidence set. Do not infer systemhood from coordinated-looking traces alone.

The primary evidence family is coordinated work, service behavior, market participant traces, distributed cognition, routine dynamics, team cognition, work traces, and socio-technical evidence. QL enters only when probe, frame, export, incompatible read, or carrier/export structure that is not faithful enough for the declared use changes the admissible state reading.

The canonical EDSE move is to separate the factorable part from the coordination residue before making the minimal state reading:

1. state what ordinary routines, policies, incentives, shared stimuli, dashboard-following, or copied artifacts explain;
2. state what the carriers show;
3. state what residue remains as a minimal state reading;
4. state what action this residue supports.

Start with this recognition note:

| Mini-entry | Question |
| --- | --- |
| Collective bearer | Whose coordinated work or behavior is being read: which team, organization, service mesh, market slice, or other declared collective system? |
| Carriers / window | Which traces, artifacts, work results, commitments, dashboards, API responses, or records ground the reading, and during which window? |
| Minimal state reading | What is the minimal state reading supported by the coordinated work or behavior, or by the trace pattern? |
| Rival | Which ordinary rival explanation remains live: policy, routine, shared stimulus, dashboard-following, copied artifact, or propagation effect? |
| Practical change | What can be done now without exceeding the evidence: adjust communication, triage, routing, planning, probe design, or return to a fuller evidence record? |

Use the fuller EDSE record below when the reading will change coordination, be reused, be contested, support evidence, or leave the immediate local discussion.

Full EDSE record:

| Field | Question |
| --- | --- |
| Collective bearer | Which declared collective `U.System` is being described? |
| Observed coordinated work, behavior, and trace pattern | Which role-work, service behavior, market participant traces, routine, commitment, artifact use, or coordinated action is observed? |
| State reading | Which minimal state reading is consistent with the work? |
| QL cue or formal cue if retained after ordinary work, evidence, or routine explanation | Which probe, export loss, incompatible frame, compound-system decomposition, or no faithful-enough export under the declared probe, frame, and use makes ordinary work and evidence wording insufficient after ordinary explanations have been tried? |
| Evidence carriers | Which logs, traces, records, commitments, artifacts, dashboards, API responses, or documents ground the reading? |
| Probe or measurement approximation | Which survey, dashboard, API read, interview, trace query, metric, or publication approximates the state, and how may that probe change, thin, or frame the state reading? |
| Attempted export and faithful-enough criterion | What export was attempted, and what would count as faithful enough for the current decision? |
| Loss cause and higher-fidelity export | Why is the current export not faithful enough, and could a more discriminating probe, bridge, representation, or time window produce a higher-fidelity export? |
| Time window | During which window does the claim hold? |
| Persistence posture | Is the reading momentary, recurring, stabilized for the incident/release/window, or expected to persist under stated conditions? |
| Decay and refresh condition | What would make the reading expire, refresh, lose support, or need a new probe? |
| Reprobe cost | What does it cost in time, risk, disruption, attention, coordination, privacy, or evidence quality to check again? |
| Rival explanation not ruled out | Which ordinary explanation remains possible? |
| Minimal supported claim | What may be said without exceeding the evidence, carrier set, time window, or export limit? |
| Supported action or use | Which planning, communication, incident, routing, bridge, evidence, or decision move may now be taken without exceeding the claim? |

#### C.26.2:4.1 - Minimal claim principle

Preferred wording stays close to observed work:

- "During window W, the incident-response organization acted consistently with a rollback-readiness posture, evidenced by release timing, escalation criteria, and shared trace use."
- "The service mesh exhibited a coordinated throttling regime under policy P, evidenced by route changes and saturation traces."
- "Market traces support an expectation-shift claim under probe Q, with media amplification still a rival explanation."

Avoid wording that asserts a heavier claim, such as "the organization decided", "the market knows", or "the team has a distributed mind", unless another FPF pattern and evidence requirement independently support it.

#### C.26.2:4.2 - Finish conditions

This pattern emits one of these results:

| Result | Meaning |
| --- | --- |
| Minimal evidence-bound state assertion | State the collective bearer, observed coordinated work, behavior, or trace pattern, carriers, time window, confidence posture or assurance posture, rivals, and export limit. |
| Export-loss repair | Keep the state reading minimal and add a bridge or publication note about what the attempted report, survey, API response, dashboard, or policy sentence lost. |
| Probe-coupled neighboring-pattern handoff | Apply `C.26.1` when the survey work, dashboard publication or use, interview, API operation, or publication act changed the state being evidenced. |
| Measurement or evidence neighboring-pattern handoff | Apply `C.16`, `A.10`, or `B.3` when the main support requirement is scale, method, evidence, assurance, or audit posture. |
| Work or authority neighboring-pattern handoff | Apply `A.15` or the relevant authority or work pattern when a command, routine, incentive, or playbook explains the coordination without remaining export or probe support requirement. |
| No EDSE claim | Drop the distributed-state wording when the carriers, window, rivals, or minimal admissible output cannot be stated. |

#### C.26.2:4.3 - Rival explanation rule

Before using this pattern, name the principal ordinary rivals:

| Rival | Repair |
| --- | --- |
| Policy, command, coercion, or management pressure | Use work-claim or authority-claim patterns unless export or probe loss remains live. |
| Shared incentive or common external stimulus | Keep the claim as parallel response if that explains the coordination. |
| Routine, habit, script, or playbook | State the routine; avoid current-state wording that requires additional evidence. |
| Dashboard-following, metric gaming, or social desirability | Use `C.26.1` and evidence patterns for probe-caused change. |
| Copied artifact, template, policy sentence, or API response | Use `F.9`, E.17 publication, or bridge loss before EDSE. |
| Diffusion, contagion, media amplification, or signaling | Use the appropriate propagation or evidence pattern and keep only the remaining work-enacted state claim. |

#### C.26.2:4.4 - Export-loss discipline

The phrase "not faithfully exportable under current probe and bridge conditions" is supported only when the text says:

- what export was attempted;
- what would have counted as faithful enough for the current decision;
- what state, coordination, evidence path, timing, role alignment, option structure, survivor relation, or use limit was lost;
- whether the loss comes from bridge, measurement, representation, audience, timing, state change, or another cause;
- whether a more discriminating probe, bridge, representation, or time window could produce a higher-fidelity export.

#### C.26.2:4.5 - Compound-state decomposition card

When the distributed-state reading is load-bearing, state the decomposition explicitly. Its practical purpose is the canonical EDSE move: ordinary rivals first, carriers second, coordination residue third, admissible use or action invitation fourth.

| Field | Question |
| --- | --- |
| Whole system | Which collective `U.System` is being read, and under what boundary? |
| Subsystems | Which teams, roles, services, markets, routines, artifacts, or work lanes are locally readable? |
| Local state readings | What can be said about each part without inventing a shared inner representation? |
| Correlation or coordination evidence | Which traces, timing, work transfers, commitments, artifact uses, or role-work alignments show coordination? |
| Factorable part | Which part of the behavior is explained by policy, routine, shared stimulus, incentive, dashboard following, or copied artifact? |
| Coordination residue | What remains as a minimal distributed-state reading after the ordinary rival explanations are named? |
| Minimal supported claim | What evidence-bound claim survives for the declared time window and carrier set? |
| Supported action or use | Which planning, communication, incident, routing, bridge, evidence, or decision move may now be taken without exceeding that minimal claim? |

#### C.26.2:4.6 - Governed object and claim floor

The governed object is an evidence-bound `U.Episteme` reading over coordinated work, behavior, or trace patterns by a declared collective `U.System`. The pattern does not govern an inner group entity, a culture substance, a market mind, a hidden service intelligence, or a reusable kernel state kind.

The governed move is to turn coordinated work, behavior, or trace patterns into the minimal useful state reading while keeping the reading bound to:

- the collective bearer and its boundary;
- the observed work and evidence carriers;
- the time window and persistence support;
- the probe or export conditions;
- the ordinary rival explanations;
- the current export loss and higher-fidelity export possibility;
- the next neighboring FPF pattern if a claim requiring additional evidence is needed.

This pattern is useful because many real work states are enacted before they are articulable. A team may behave as if a release freeze exists before any single person states it cleanly. A service mesh may exhibit one routing posture before any one dashboard carries the whole situation. A market may shift expectations before any one survey faithfully exports the shift. The pattern lets FPF say that much, and no more, without pretending that one carrier is the state.

#### C.26.2:4.7 - Operational evidence sequence

Action path:

1. Name the collective bearer as a declared `U.System` boundary, not a bare social label.
2. Name the coordinated work, behavior, or trace pattern being read through `A.15`: actions, routines, commitments, role-work, service behavior, market participant traces, artifacts, or timing.
3. Name the evidence carriers through `A.10` so the reading is inspectable.
4. State the time window, persistence support, decay/refresh condition, reprobe cost, and ordinary rival explanations.
5. Name the candidate state reading only as a minimal evidence-bound `U.Episteme` reading.
6. State the attempted export and what it lost.
7. State the minimal supported claim, the supported action or use it carries now, and the other uses that remain unsupported by this reading.
8. Add `B.3` assurance only when consequence level, audit, release, or accountability use demands it.

Required output: produce a minimal evidence-bound distributed-state reading, the time window that bounds it, the live rival explanations, and the supported bounded action or use that follows from that reading.

The pass is complete only when the resulting sentence can survive without magical collective wording. A good output sounds like:

> During incident window W, the incident-response organization acted consistently with rollback-readiness posture P, evidenced by deployment queue changes, escalation messages, rollback artifacts, and support-routing changes; this reading is not faithfully exported by survey S because S loses timing, role-work, and trace linkage.

That sentence is narrower than "the organization decided", but it is much more useful. It supports adjusting incident communication and release-triage posture during window W; it does not support a durable culture claim or release-readiness assurance claim.

#### C.26.2:4.8 - Well-formed EDSE record

A usable EDSE record has this shape:

```text
EnactedDistributedStateEvidence(
  collectiveBearer = ...,
  boundary = ...,
  observedCoordinatedWork = ...,
  evidenceCarriers = ...,
  probeOrExport = ...,
  timeWindow = ...,
  persistenceSupport = ...,
  ordinaryRivals = ...,
  factorablePart = ...,
  coordinationResidue = ...,
  exportLoss = ...,
  minimalSupportedClaim = ...,
  boundedActionSupported = ...,
  unsupportedUse = ...
)
```

The syntax is illustrative. The content is not optional when the state reading is used for a decision.

Well-formedness constraints:

- `collectiveBearer` is a declared collective system, not a metaphorical subject.
- `evidenceCarriers` are inspectable publication units, traces, records, commitments, logs, or work-result records.
- `timeWindow` bounds the claim; persistence beyond that window needs its own support.
- `ordinaryRivals` include at least the principal policy, incentive, routine, shared stimulus, dashboard-following, copied-artifact, or social-desirability explanation that could explain the same coordination.
- `minimalSupportedClaim` states only what survives after rivals and export loss are named.
- `unsupportedUse` names the neighboring claim or use that the current claim does not carry without applying the exact neighboring FPF pattern that governs that claim.

#### C.26.2:4.9 - Carrier, probe, report, and state split

The pattern keeps four objects separate:

| Object | Role in the claim |
| --- | --- |
| Enacted work | What people, services, routines, artifacts, or market participants actually did in coordination. |
| Evidence carrier | The log, trace, ticket, meeting note, deployment record, dashboard export, report, API response, or policy text that makes some part of the work inspectable. |
| Probe / approximation | The survey, dashboard query, interview, trace query, report request, metric, or publication act that frames the state reading. |
| Distributed-state reading | The minimal `U.Episteme` claim inferred from coordinated work or behavior under carriers, window, rivals, and export limits. |

A survey can be an evidence carrier and a probe. It is not the distributed state. A policy can be a carrier or a routine explanation. It is not automatically evidence that everyone shares one state. A dashboard can be a carrier, a probe, and a behavior-changing instrument. It is not automatically faithful enough for the intended use.

#### C.26.2:4.10 - Case bank and near misses

| Case | Supported C.26.2 reading | Near miss or neighboring-pattern handoff |
| --- | --- | --- |
| Incident release freeze | Teams stop releases, prepare rollback evidence, redirect support work, and change escalation before a written decision appears. | If a manager issued a clear command and the work merely followed it, use work and authority patterns with evidence, not EDSE. |
| Service-mesh throttling regime | Route changes, saturation traces, retry patterns, and on-call routines show a coordinated throttling state under policy P. | If one controller rule fully explains the behavior, state the rule and use ordinary system/dynamics evidence. |
| Market expectation shift | Pricing, support inquiries, partner messages, and risk notes move together after a public signal. | If media amplification or common stimulus explains the movement, keep only that propagation/evidence claim. |
| Team "already decided" posture | Backlog changes, review comments, and role assignments show that the team is acting under an unstated decision. | If the claim is only a vibe or a few statements, do not use EDSE; gather carriers or keep it as informal observation. |
| Survey of culture | Survey answers conflict, but work traces show a stable escalation habit. | Treat the survey as a probe and possible export loss; do not make it the state itself. |
| Dashboard-following organization | Teams coordinate around the public metric after the metric becomes visible. | Apply `C.26.1` for probe-caused change; EDSE may carry only the residual coordinated-state reading. |

#### C.26.2:4.11 - Evidence posture and confidence

EDSE claims become useful when the text says how much consequence the evidence can carry.

| Evidence posture | Admissible use | Additional support requirement |
| --- | --- | --- |
| `QLP-0` recognition | Flag a possible enacted state for discussion or triage. | Name bearer, work, carriers, and time window. |
| `QLP-1` local working use | Adjust local planning, incident response, or communication. | Add rivals, export loss, persistence, and reprobe condition. |
| `QLP-2` decision-bearing / reusable use | Publish as a repeatable example or internal practice, or let the reading change a bounded decision. | Add case comparison, near misses, and evidence-carrier discipline. |
| `QLP-3` assurance or reusable-law use | Use for release, audit, legal, accountability, reusable-law, or high-impact allocation. | Apply `A.10`, `B.3`, `C.16`, and the relevant authority or work patterns. |

For `QLP-0` or low-consequence `QLP-1`, do not force persistence, decay, or reprobe-cost fields when the claim is explicitly momentary and the bounded action is local. Name the bearer, carriers, window, minimal reading, rival, practical change, and local stop; add the fuller temporal fields only when reuse, contest, or consequence makes them load-bearing.

The ordinary EDSE claim is minimal but actionable. It says: "this coordinated work or behavior supports this bounded reading for this use." It does not say: "the collective has one hidden durable state that a report can copy."

### C.26.2:5 - Archetypal Grounding


Tell: During an incident, several teams independently stop non-critical releases, reroute support, and prepare rollback evidence before any single manager issues a written decision. Later, a survey asks whether "we had decided to freeze release", and answers conflict.

Show, System side: the collective bearer is the incident-response organization during a declared incident window. Its carriers include deployment logs, meeting records, escalation messages, rollback preparation, support routing, and release queue changes.

Show, Episteme side: the supported claim is minimal. The organization acted consistently with a release-freeze readiness posture during window W. The claim does not say every participant knew the same proposition or that the coordination exists apart from the declared evidence carriers. A management directive, playbook, or dashboard effect remains a rival unless evidence narrows it.

### C.26.2:6 - Bias-Annotation

This pattern biases authors toward minimal evidence-bound claims and explicit evidence. That may feel conservative, but it makes distributed-state language usable without magic.

It also biases authors to keep primary grounding in distributed cognition, team cognition, organizational routines, socio-technical work, and evidence practice. The QL lens is secondary and only becomes active when probing, exporting, or comparing the state changes or loses load-bearing structure.

### C.26.2:7 - Conformance Checklist

| ID | Check |
| --- | --- |
| CC-C26.2.1 | The collective bearer is a declared `U.System` or collective system, not a bare group label. |
| CC-C26.2.2 | Observed coordinated work, behavior, and trace pattern is named. |
| CC-C26.2.3 | Evidence carriers and time window are named. |
