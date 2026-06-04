---
chunk_kind: "child"
pattern_id: "C.22"
pattern_title: "Problem Typing & TaskSignature Assignment (Problem-CHR)"
section_id: "C.22:5"
section_title: "Solution — Problem‑CHR (fields) + TaskSignature (S2) attachment (normative)"
source_path: "FPF-Spec.md"
output_path: "by_section/C.22/C.22__006_solution-problem-chr-fields-tasksignature-s2-attachment-normative.md"
commit_sha: "a0c90e3bbfcc0285893cc5bb9d4a88fcd224f00e"
heading_path:
  - "C.22 — Problem Typing & TaskSignature Assignment (Problem-CHR)"
  - "C.22:5 — Solution — Problem‑CHR (fields) + TaskSignature (S2) attachment (normative)"
line_start: 43381
line_end: 43452
dependencies:
  - "C.16"
  - "C.18"
  - "C.19"
  - "C.22.1"
  - "C.23"
  - "E.10"
  - "E.18"
  - "G.0"
  - "G.4"
  - "G.5"
keywords:
  - "Problem‑CHR"
  - "ScopeSlice(G)"
  - "TaskKind"
  - "TaskSignature"
  - "specialization anchor"
  - "unknown handling"
---

### C.22:5 - Solution — **Problem‑CHR** (fields) + **TaskSignature (S2) attachment** *(normative)*

#### C.22:5.1 - Minimal CHR fields (tri‑state aware).
**Selector-side field boundary.** The fields below are live only after problem framing has been stabilized enough to ask eligibility, acceptance, selection, method-family, or policy-governed choice questions. They are not a universal problem-framing checklist and must not replace the `C.22.2` Thin `ProblemCard@Context` pass for a messy signal. Each live field is **CHR-typed** (Characteristic, Scale, Unit, Polarity; MM-CHR discipline). Every predicate admits `unknown` (tri-state). Unknown-handling policy propagates `{degrade|abstain|sandbox}` per Acceptance profile or EvidenceProfile policy (recorded in SCR). (G.4/G.6 alignment)

**Optional extension absence rule.** If QD, OEE, archive, generator, parity, specialization, or another optional relation is not live for the current case, the corresponding optional fields are absent, not `unknown`. Use `unknown` only for a live field whose value is currently unknown. An absent non-live extension does not trigger `{degrade|abstain|sandbox}` propagation.

* **`DataShape`** — data regime and admissible transforms (e.g., tabular, sequence, graph; density; stationarity claims).
* **`NoiseModel`** — uncertainty class and robustness envelope (e.g., iid Gaussian; heavy‑tailed; adversarial budget).
* **`ObjectiveProfile`** — objective heads (**Scale, Unit, Polarity** and **ReferencePlane** declared), polarity, and **admissible order relations** (lexicographic, Pareto, medoid or median where admissible). **Weighted sums across mixed scale types are forbidden**; ordinal heads use order-only guards. For QD tasks, explicitly enumerate quality heads, diversity or descriptor-space heads, and any policy-authorized QD contribution heads; see **DominanceRegime** below. Do not introduce a default QD score. If a scalar or set-scalarization policy is live, cite the governing CAL policy and keep dominance and telemetry roles explicit.
* `RegularityTraits` — method‑relevant structure (**convexity, differentiability, separability, monotonicity**) as CHR‑typed predicates with guard‑macros (e.g., `ORD_COMPARE_ONLY`, `UNIT_CHECK`, `POLARITY_CHECK`). Include `ConditionClass` (e.g., stiffness/κ‑proxies) where applicable.
* **`Constraints`** — explicit hard and soft constraint classes (feasibility predicates; **ResourceEnvelope** and **RiskEnvelope**). **Acceptance-gate thresholds live in `G.4` only; never inside CHR or code paths.**
* `ShiftClass` and stationarity — CHR‑typed claims about regime stability (iid | covariate‑shift | concept‑drift | adversarial). Default=`unknown`. Acceptance or flow use is governed by this field in gating; otherwise abstain.
* `EvidenceGraphRef (A.10)` — carriers & **lane tags (TA/VA/LA)** with **freshness windows**; **no self‑evidence**; default Γ‑fold = **weakest‑link** unless CAL proves an alternative.
* `ScopeSlice(G)` — the **USM claim-bounding scope cut** over **EntityOfConcernRef and scope** (discipline governance in **CG‑Spec**; Domain is a catalog mark only).
* `Size/Scale` — size and condition proxies (**n, m, κ, sparsity**) with **declared units**; unit mismatch ⇒ {sandbox|refuse}.
* **`Freshness`** — validity window for descriptors.
* `Missingness` — **MCAR, MAR, or MNAR** (or mapped equivalents) per **CHR.Missingness**; MUST be honoured by Acceptance and Flows.
* `KindSet` — **`U.Kind[]`** for the selected entities addressed by the TaskKind; separates **EntityOfConcern kind** from **Scope (USM)**.

**QD and Illumination extensions (normative; ties to C.18 and C.19).**

Use this extension block only when QD, illumination archive, set-return, or OEE generator relation is live for the current case. It is not part of every `TaskSignature`.

* **`CharacteristicSpaceRef`** — reference to **`U.CharacteristicSpace`**, with declared **d≥2**; **characteristics are CHR‑typed**; **ReferencePlane** per characteristic; pin edition via **`CharacteristicSpaceRef.edition`**.
* **`ArchiveConfig`** — archive **topology** (grid, CVT, or graph), **resolution** (bins or centroids), **K‑capacity**, **`InsertionPolicyRef`** (elite replacement, dedup, or novelty), and **`DistanceDefRef.edition`** (declare **metric or pseudometric** status and invariances; any normalisation **MUST** cite admissible scale transforms in **CG‑Spec**); admissibility follows CG‑Spec.
* **`EmitterPolicyRef`** — pointer to emitter/governor policy (C.19) applicable to this TaskSignature; **edition id** recorded.
* **`DominanceRegime`** — `{ParetoOnly | ParetoPlusIllumination}`. **Default = `ParetoOnly`** (illumination remains report‑only telemetry unless CAL explicitly authorises `ParetoPlusIllumination`, policy‑id cited).
* **`IlluminationSummary`** — a **telemetry summary over `Diversity_P`**; reported by default; excluded from dominance unless a CAL enables `ParetoPlusIllumination` (policy‑id cited).
* **`IlluminationMap`** *(parity‑run)* — required **IlluminationMap publication** (grid, CVT, or graph per `ArchiveConfig`) recording coverage per niche or cell with `DescriptorMapRef` and `DistanceDefRef.edition`. **Leaderboards as single‑score lists are forbidden**; comparisons **MUST** be under CG‑frames.
* **`PortfolioMode`** — `{Pareto | Archive}`. **Default = `Archive`**: selectors preserve retained archive evidence (QD archives) rather than a single “best” set; ε‑fronts remain admissible for local decisions under CG‑Spec.
* **`Budgeting`** — evaluation, time, and batch **budgets**, including **E/E‑LOG exploration budget** id; units declared (CG‑Spec).
* **`TelemetryHooks`** — **PathSliceId**, **decay and refresh policy ids**, and **edition counters** to record **U.DescriptorMap** and **policy‑id** updates upon illumination gains.
* **`GeneratorIntent`** (OEE) — optional intent to use a registered **`GeneratorFamily`** (G.5), with pointers to **`EnvironmentValidityRegion`**, **`TransferRulesRef`**, and **coverage and regret** reporting expectations.

**Admissibility.** Before any numeric comparison or aggregation, **prove CSLC admissibility** (Scale, Unit, Polarity) and **cite CG‑Spec.Characteristics**; record **ReferencePlane**. **Unknowns** propagate as {degrade|abstain|sandbox}; **no `unknown→0/false` coercions**.

#### C.22:5.2 - TaskSignature (S2) — attachment definition (design‑time + run‑time).
A TaskSignature is the minimal typed record consumed by selector-facing use:
`⟨Context, TaskKind, TaskFamilyRef?, KindSet:U.Kind[], DataShape, NoiseModel, ObjectiveProfile, Constraints{incl. Resource/Risk Envelopes}, ScopeSlice(G), EvidenceGraphRef, Size/Scale, Freshness, Missingness, ShiftClass?, BehaviorSpaceRef?, ArchiveConfig?, EmitterPolicyRef?, DominanceRegime?, PortfolioMode?, Budgeting?, TelemetryHooks?, GeneratorIntent?⟩`

**Minimality rule.** S2 carries only fields required for **Eligibility→Acceptance→admissible selection**; any additional traits derived at design‑time are recorded as provenance (UTS) but **do not expand S2**.

Values are **CHR‑typed** with **provenance**; traits may be **inferred** from CHR and CAL bindings (e.g., *convexity known? differentiable? ordinal vs interval scales?*) and from **USM** scope metadata. Unknowns are tri‑state; **Missingness semantics MUST align with CHR.Missingness** and be honored by Acceptance and Flows.

`TaskKind` names the governing kind of work or problem under this context. `TaskFamilyRef?` names one comparison-relevant family inside that task kind when specialization, transfer, or parity question is live. `TaskSignature` is the context-bound typed attachment record for one current case under that kind and scope cut. `KindSet` continues to name the selected entities addressed by the task kind; it is not a substitute for the task-family reference.

**DesignRunTag hygiene.** Do not mix DesignRunTag in one signature; record **GateCrossings** as **CrossingBundles** (**E.18**; Bridge+UTS through **F.9**, **F.17**, **E.17**, and **E.18**) when importing design‑time traits into run‑time.

##### C.22:5.2.1 - Specialization-claim reference discipline (normative)
Any claim that one holder, dyad, team, or explicitly scoped specialist portfolio acquired usable specialization **SHALL** state one declared `TaskFamilyRef` or `TaskSignature`, one named work-measure threshold target, an adaptation budget, and the freshness or provenance basis for reuse. A method may be selected, refined, or retired as part of that story, but the method is not the bearer of the specialization claim. The attached task-family record should stay rich enough for the same task family and work target to remain admissible in `C.22.1` adaptation signatures, `G.5` specialization profiles, and `G.9` adaptation parity without reconstructing the claim from narrative prose.

Low-human-overlap or newly discovered task families remain admissible when those task-family or signature references are explicit by value.
#### C.22:5.3 - Provenance & planes.
Record **Context** and **ReferencePlane** for each value; on any cross-Context or cross-plane reuse, attach BridgeDescription + UTS row, apply **CL** (and, if planes differ, **CL^plane**) penalties to **R_eff only**; both **Φ(CL)** and (if used) **Φ_plane** MUST be **monotone, bounded, and table‑backed**; **no “distance” language; penalties never mutate F/G.** Record policy‑ids in SCR and cite Bridge ids on crossings.

#### C.22:5.4 - Attachment & use.

* **Eligibility** gates read TaskSignature against each **MethodFamily.Eligibility** (C.23) and **CG‑Spec.MinimalEvidence** for referenced characteristics.
* **Acceptance** clauses (G.4) use these fields for **acceptance-gate threshold predicates** (acceptance-gate thresholds live in Acceptance only).
* **Selection kernel** (G.5.S3) applies an **admissible order** (often partial); **weighted sums across mixed scale types are forbidden**. If only a partial order remains, **return a Pareto (non‑dominated) set** with tie notes. If `PortfolioMode=Archive`, the selector **may** return a **QD archive** (per `ArchiveConfig`) **in addition to** or **instead of** a Pareto set. **Illumination** enters dominance **only** if `DominanceRegime=ParetoPlusIllumination` is **enabled by CAL** (policy id cited); otherwise, QD telemetry values are **reported** but **excluded** from dominance.
* When `GeneratorIntent` is present, G.5-governed selection may use a registered **`GeneratorFamily`** (POET‑class); the selection domain becomes **pairs** `{environment, method}`, with Environment guarded by **`EnvironmentValidityRegion`** and **`TransferRulesRef`** (C.23 wiring). Report **`IlluminationSummary`** as a **telemetry summary over `Diversity_P`** (report‑only by default) in telemetry; dominance remains unaffected unless policy changes as above.

#### C.22:5.5 - Unknowns.
Every field admits `unknown`; downstream **degrade, abstain, or sandbox** behavior is explicit per Acceptance profile or EvidenceProfile; no implicit coercions.

#### C.22:5.6 - Publication.
Output a **ProblemProfile** (...Description) that carries the bound TaskSignature, **UTS** Name Cards for any minted values (twin labels), and SCR-visible provenance (A.10 evidence relations, lane tags, freshness, **ReferencePlane**). **Mark any vendor or tool examples as Plain‑register only (LEX V‑4); they are non‑normative.**

#### C.22:5.7 - Open‑Ended tasks (GeneratorFamily) *(normative)*.
If the problem requires **open‑ended generation** of tasks or environments, S2 **SHALL** include `GeneratorIntent` with pointers to **`EnvironmentValidityRegion`** (admissible region for generated environments), **`TransferRulesRef`** (cross‑environment transfer constraints), and **coverage and regret** telemetry expectations. Selector outputs are then declared sets over **{environment, method}**; **coverage and regret** are reported telemetry values and **IlluminationSummary** is a **telemetry summary** (reported), excluded from dominance unless a **CAL** policy promotes them (policy‑id recorded in SCR; see `DominanceRegime`). Edition increments of **CharacteristicSpaceRef.edition**, **DescriptorMapRef.edition**, **DistanceDefRef.edition**, and (OEE) **`TransferRulesRef.edition`**, and the **policy‑id** associated with illumination increases **SHALL** be recorded in SCR.

