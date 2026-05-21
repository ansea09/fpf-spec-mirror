---
chunk_kind: "child"
pattern_id: "C.22"
pattern_title: "Problem Typing & TaskSignature Assignment (Problem-CHR)"
section_id: "C.22:5"
section_title: "Solution — Problem‑CHR (fields) + TaskSignature (S2) attachment (normative)"
source_path: "FPF-Spec.md"
output_path: "by_section/C.22/C.22__006_solution-problem-chr-fields-tasksignature-s2-attachment-normative.md"
commit_sha: "eb2832093c1e482d5fdd4985c3d2011ab240b429"
heading_path:
  - "C.22 — Problem Typing & TaskSignature Assignment (Problem-CHR)"
  - "C.22:5 — Solution — Problem‑CHR (fields) + TaskSignature (S2) attachment (normative)"
line_start: 41366
line_end: 41434
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


