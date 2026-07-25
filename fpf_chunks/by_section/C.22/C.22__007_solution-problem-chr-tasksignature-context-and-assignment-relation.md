---
chunk_kind: "child"
pattern_id: "C.22"
pattern_title: "Problem Typing & TaskSignature Assignment (Problem-CHR)"
section_id: "C.22:5"
section_title: "Solution — Problem CHR, TaskSignature@Context, and assignment relation"
source_path: "FPF-Spec.md"
output_path: "by_section/C.22/C.22__007_solution-problem-chr-tasksignature-context-and-assignment-relation.md"
commit_sha: "504747d26299e3963dc0457bf48d4e2a791d926a"
heading_path:
  - "C.22 — Problem Typing & TaskSignature Assignment (Problem-CHR)"
  - "C.22:5 — Solution — Problem CHR, TaskSignature@Context, and assignment relation"
line_start: 50098
line_end: 50271
dependencies:
  - "A.6.0"
  - "C.16"
  - "C.18"
  - "C.19"
  - "C.22.1"
  - "C.22.2"
  - "C.23"
  - "C.32.P2S"
  - "E.10"
  - "E.18"
  - "G.0"
  - "G.4"
  - "G.5"
keywords:
---

### C.22:5 - Solution — Problem CHR, `TaskSignature@Context`, and assignment relation

**Local TaskSignature mantra.** *Stabilize the problem; name the receiving selection question and task kind; keep only traits that can change eligibility, acceptance, or selection; type each live trait; preserve unknowns, evidence relations, scope, and currentness; declare the TaskSignature, assign it to the problem-side episteme for that use, and stop before selecting a method.* This is a short repeatable rendering of the C.22 Solution. It is not a selector algorithm, method recommendation, work plan, dated selection occurrence, or `DemonstrativeUnfoldingSlice@Context`.

Apply that formula as follows:

1. Confirm that the problem-side representation is stable enough for selector-facing use; otherwise return to `C.22.2`.
2. Name the receiving eligibility, acceptance, or selection question and the `TaskKind`, optional task family, or work target that the signature will declare.
3. Include only the problem traits whose values can change that receiving use. Leave a non-current optional extension absent.
4. Type each live characteristic by scale, unit, polarity, reference plane, and admitted comparison relation before aggregation or comparison.
5. Preserve a live but unknown value as `unknown`; include or reference the exact scope, evidence relation, freshness or edition condition, and crossing relation on which later use relies.
6. Close with one minimal `TaskSignature`. Pass later eligibility and acceptance claims to `C.23` and `G.4`, and actual method-family selection to `G.5`; do not put their outcomes back into the signature as if they were problem traits.

#### C.22:5.0a - Positive closure, bounded non-use, and local return

Close the C.22 use positively when the four-row TaskSignature declaration is complete and `TaskSignatureAssignmentRelation@Context` recovers the stabilized problem-side episteme, bounded Context, exact signature edition, and receiving use. Each live characteristic has its scale, unit, polarity, reference plane, admitted comparison relation, and value or explicit `unknown`; every relied-on evidence, freshness, edition, or crossing relation is named. A downstream selector can now consume the assigned signature without guessing, but no eligibility verdict, acceptance result, method recommendation, selector outcome, work plan, or dated work is claimed.

Close by bounded non-use when problem framing is not stable enough for a TaskSignature declaration, when no selector-facing receiving use is current, or when the current question has already become eligibility, acceptance, selection, planning, or performed work. A non-current optional extension remains absent. If several signatures or assignment relations remain plausible, preserve them as candidates under the governing problem or selection pattern rather than asserting one assignment.

Return to the smallest affected TaskSignature position when its receiving question, Context, `TaskKind`, task-family or work-target reference, project subject or scope, characteristic meaning, scale, unit, polarity, reference plane, unknown status, evidence relation, freshness condition, edition, or crossing relation changes. Keep the upstream `ProblemCard@Context` and downstream selection history unchanged unless the changed relation actually invalidates them under their own governing patterns.

**Worked local repair.** A machining TaskSignature originally records surface finish as an ordinal visual grade. The receiving use later adopts measured roughness `Ra` on a ratio scale in micrometres with a named measurement and evidence relation. Repair the affected characteristic head, scale, unit, admitted comparisons, and evidence relation. Keep the machining `TaskKind`, unaffected constraints, scope, and prior work history. Reopen eligibility, acceptance, or method-family selection only when its earlier result relied on the replaced finish head; the direct downstream pattern decides the new result.

#### C.22:5.0b - Apparatus proportionality

Use the lightest signature declaration and assignment relation that the named receiving use can consume:

1. **Minimal selector-facing use.** Materialize one TaskSignature with only the live fields needed by the current eligibility, acceptance, or selection question. This is the ordinary positive result of C.22.
2. **Reliance-bearing use.** Add an addressable `ProblemProfile` episteme only when delayed feedback, audit, transfer, automation, expensive reversal, or another named use relies on replay beyond the local assignment relation. Pin the exact problem-side episteme and edition, TaskSignature edition, receiving use, every field-basis relation with its direct governing pattern, qualification window, review trigger, and any current evidence, currentness, or crossing relation.
3. **Extension-bearing use.** Add QD, OEE, archive, generator, parity, or specialization positions only when that exact downstream relation is current and its direct pattern requires those values.

More fields, publication packaging, name cards, or telemetry do not make the problem better formulated, the TaskSignature more true, or a method more suitable. If no selector-facing receiving use needs a TaskSignature, close by bounded non-use rather than publishing a thin declaration for its own sake.

#### C.22:5.1 - Minimal CHR fields (tri‑state aware).
**Selector-side field boundary.** The fields below are live only after problem framing has been stabilized enough to ask eligibility, acceptance, selection, method-family, or policy-governed choice questions. They are not a universal problem-framing checklist and do not replace the `C.22.2` Thin `ProblemCard@Context` pass for a messy signal. Each live characteristic field is **CHR-typed** by Characteristic, Scale, Unit, and Polarity under MM-CHR discipline. A live predicate may preserve `unknown` when its direct pattern admits that value; the cited downstream policy governs what follows. This aligns G.4 and G.6 without making their results C.22 values.

**Optional extension absence rule.** If QD, OEE, archive, generator, parity, specialization, or another optional relation is not live for the current case, the corresponding optional fields are absent, not `unknown`. Use `unknown` only for a live field whose value is currently unknown. An absent non-live extension triggers no downstream disposition.

* **`DataShape`** — data regime and admissible transforms (e.g., tabular, sequence, graph; density; stationarity claims).
* **`NoiseModel`** — uncertainty class and robustness envelope (e.g., iid Gaussian; heavy‑tailed; adversarial budget).
* **`ObjectiveProfile`** — objective heads (**Scale, Unit, Polarity** and **ReferencePlane** declared), polarity, and **admissible order relations** (lexicographic, Pareto, medoid or median where admissible). **Weighted sums across mixed scale types are inadmissible**; ordinal heads use order-only guards. For QD tasks, explicitly enumerate quality heads, diversity or descriptor-space heads, and any policy-authorized QD contribution heads; see **DominanceRegime** below. Do not introduce a default QD score. If a scalar or set-scalarization policy is live, cite the governing CAL policy and keep dominance and telemetry roles explicit.
* `RegularityTraits` — method-relevant structure (**convexity, differentiability, separability, monotonicity**) as CHR-typed predicates with guard macros (for example, `ORD_COMPARE_ONLY`, `UNIT_CHECK`, `POLARITY_CHECK`). Include `ConditionClass` such as stiffness or kappa proxies where applicable.
* **`Constraints`** — explicit hard and soft constraint classes (feasibility predicates; **ResourceEnvelope** and **RiskEnvelope**). **Acceptance-gate thresholds live in `G.4` only; never inside CHR or code paths.**
* `ShiftClass` and stationarity — CHR‑typed claims about regime stability (iid | covariate‑shift | concept‑drift | adversarial). Default=`unknown`. The cited acceptance or selector policy governs the consequence of that unknown for its receiving use.
* `EvidenceGraphRef (A.10)` — evidence carriers and **lane tags TA, VA, and LA** with **freshness windows**; **no self-evidence**; default Γ-fold = **weakest-link** unless CAL establishes an alternative.
* `ScopeSlice(G)` — the **USM claim-bounding scope cut** over **EntityOfConcernRef and scope** (discipline governance in **CG‑Spec**; Domain is a catalog mark only).
* `SizeAndConditionProfile` — size and condition proxies (**n, m, kappa, sparsity**) with **declared units**; a unit mismatch makes the current comparison unsupported until the direct acceptance or selector policy supplies its governed result.
* **`Freshness`** — validity window for descriptors.
* `Missingness` — **MCAR, MAR, or MNAR** (or mapped equivalents) per **CHR.Missingness**; Acceptance and flow use preserve the declared missingness semantics.
* `KindSet` — selected C.3 `U.Kind` values for the entities addressed by the TaskKind; separates **EntityOfConcern kind** from **Scope (USM)**.

**QD and Illumination extensions (normative; ties to C.18 and C.19).**

Use this extension block only when QD, illumination archive, set-return, or OEE generator relation is live for the current case. It is not part of every `TaskSignature`.

* **`CharacteristicSpaceRef`** — reference to **`U.CharacteristicSpace`**, with declared **d≥2**; **characteristics are CHR‑typed**; **ReferencePlane** per characteristic; pin edition via **`CharacteristicSpaceRef.edition`**.
* **`ArchiveConfig`** — archive **topology** (grid, CVT, or graph), **resolution** (bins or centroids), **K‑capacity**, **`InsertionPolicyRef`** (elite replacement, dedup, or novelty), and **`DistanceDefRef.edition`** (declare **metric or pseudometric** status and invariances; normalisation is admissible only when the applied scale transform is admitted by **CG-Spec**); admissibility follows CG‑Spec.
* **`EmitterPolicyRef`** — reference to the emitter policy governed by C.19 and applicable to this TaskSignature; **edition id** recorded.
* **`DominanceRegime`** — `{ParetoOnly | ParetoPlusIllumination}`. **Default = `ParetoOnly`** (illumination remains report‑only telemetry unless CAL explicitly authorises `ParetoPlusIllumination`, policy‑id cited).
* **`IlluminationSummary`** — a **telemetry summary over `Diversity_P`**; reported by default; excluded from dominance unless a CAL enables `ParetoPlusIllumination` (policy‑id cited).
* **`IlluminationMap`** *(parity-run)* — parity-run publication is complete when an **IlluminationMap publication** (grid, CVT, or graph per `ArchiveConfig`) records coverage per niche or cell with `DescriptorMapRef` and `DistanceDefRef.edition`. A single-score leaderboard does not satisfy this comparison use; compare under the declared CG-frame.
* **`PortfolioMode`** — `{Pareto | Archive}`. **Default = `Archive`**: selectors preserve archive evidence (QD archives) rather than a single “best” set; ε‑fronts remain admissible for local decisions under CG‑Spec.
* **`Budgeting`** — evaluation, time, and batch **budgets**, including **E/E‑LOG exploration budget** id; units declared (CG‑Spec).
* **`TelemetryHooks`** — `PathSliceId` only when an E.18 path-slice reference is current, plus **decay and refresh policy ids**, **edition counters**, descriptor-map updates, and **policy-id** updates upon illumination gains.
* **`GeneratorIntent`** (OEE) — optional intent to use a registered **`GeneratorFamily`** (G.5), with pointers to **`EnvironmentValidityRegion`**, **`TransferRulesRef`**, and **coverage and regret** reporting expectations.

**Admissibility.** Before any numeric comparison or aggregation, establish CSLC admissibility for Scale, Unit, and Polarity and cite **CG-Spec.Characteristics**; record **ReferencePlane**. Preserve `unknown` for the downstream policy; do not coerce it to `0` or `false`, and do not invent a C.22-local disposition.

#### C.22:5.2 - `TaskSignature@Context` declaration and assignment

`TaskSignature@Context` is a Context-local species of A.6.0 `U.Signature`. It uses the canonical four-row block rather than a flat record schema. Because eligibility, acceptance, and selector patterns import or cite it, its A.6.0 `SignatureManifest` supplies a stable `SignatureId`, edition, imports, and provided names without adding a fifth semantic row.

```text
TaskSignature@Context <: U.Signature

SubjectBlock:
  SubjectKind = TaskKind, one exact C.3 U.Kind value
  RangedValueKind = U.Entity
  SliceSet = declared A.2.6 subject-scope slices
  ExtentRule = entities admitted by KindSet inside those scope slices
  ResultKind = absent; selector outcomes are not TaskSignature values

Vocabulary:
  TaskFamilyRef?
  KindSet
  characteristic bindings with Scale, Unit, Polarity, ReferencePlane, admitted comparison relation, and value or admitted unknown
  constraint relation references
  evidence-relation references
  optional QD, OEE, archive, generator, parity, budget, telemetry, and specialization vocabulary only when current

Laws:
  include only positions that can change eligibility, acceptance, or selection for the declared use
  preserve admitted unknown and distinguish it from absent non-current vocabulary
  apply CHR scale, unit, polarity, ReferencePlane, and comparison legality before aggregation
  keep acceptance verdicts, selector outcomes, selected methods, plans, work, and performed results outside the signature
  keep each reliance-bearing field connected to its exact basis relation and direct governing pattern

Applicability:
  bounded Context and declared subject scope
  qualification, freshness, edition, and evidence-use conditions on which use relies
  named Bridge and crossing conditions for cross-context or cross-plane use
```

The field families in C.22:5.1 are projections of the `Vocabulary` and `Applicability` rows. They are not extra conceptual rows and do not redefine A.6.0.

The assignment to one problem-side episteme and receiving use is a separate relation:

```text
TaskSignatureAssignmentRelation@Context <: U.Relation:
  BoundedContextSlot = <TaskSignatureAssignmentContextSlot, U.BoundedContext, U.BoundedContextRef>
  ProblemSideRecordSlot = <ProblemSideRecordSlot, U.Episteme, U.EpistemeRef>
  TaskSignatureSlot = <TaskSignatureSlot, U.Signature, U.EntityRef constrained to TaskSignature@Context>
  ReceivingUseDescriptionSlot = <ReceivingUseDescriptionSlot, U.Episteme, U.EpistemeRef>
  direction = ProblemSideRecordSlot -> TaskSignatureSlot for ReceivingUseDescriptionSlot
```

These SlotSpecs and direction are the exact RelationSignature. Relation identity is determined by bounded context, problem-side episteme edition, TaskSignature identity and edition, and receiving-use description. Changing only a publication carrier or serialization changes neither the TaskSignature nor its assignment relation.

**TaskSignature identity and publication.** The signature's `SignatureId`, edition, and four-row semantic content determine its identity. A semantic change to SubjectBlock, Vocabulary, Laws, or Applicability creates a revised signature edition. Two E.17 publications, database records, cards, or files may serialize the same TaskSignature edition when they resolve to that same identity and introduce no new claim. `ProblemProfile` may reference the signature and assignment relation, but it does not contain or become either one.

**Minimality rule.** The signature contains only the declaration positions needed to determine eligibility, acceptance, or admissible selection for the named use. Additional traits remain outside its Vocabulary unless a later use makes them current. Their mere availability does not expand the signature.

Values are CHR-typed and tied to the exact measurement, evidence-use, source-use, representation, or scope relation that justifies their use when such a relation is current. Each reliance-bearing field basis names that relation and its direct governing pattern; generic provenance or support wording is not a replay basis. Traits may be inferred from admitted CHR, CAL, and A.2.6 scope relations. Unknowns preserve their direct Missingness semantics.

**TaskSignature invariants.** A positive assignment satisfies all six conditions:

1. The TaskSignature exposes conformant SubjectBlock, Vocabulary, Laws, and Applicability rows.
2. The assignment relation recovers its Context, exact problem-side episteme edition, exact TaskSignature edition, and receiving-use description.
3. Every live field has an admitted filler kind or scale discipline and, under reliance, an exact basis relation with a direct governing pattern.
4. A live but unrecovered value is `unknown` only where the field's direct pattern admits it and a downstream policy ref states how the receiving use handles it.
5. A non-current optional extension is absent; absence and unknown are not interchangeable.
6. Eligibility verdicts, acceptance results, selected methods, selector outcomes, work plans, and work occurrences are absent from the TaskSignature and remain with their direct patterns.

#### C.22:5.2a - Lowering and withdrawal conditions

Withdraw `TaskSignatureAssignmentRelation@Context` for the current receiving use when its problem-side episteme, Context, TaskSignature edition, or receiving-use description cannot be recovered. The TaskSignature may remain a valid declaration for another assignment. Return to `C.22.2` only when the problem-side representation itself is no longer stable enough.

Revise the TaskSignature edition when one of its SubjectBlock, Vocabulary, Laws, or Applicability claims changes. Lower or remove one vocabulary position when its filler kind, scale, unit, polarity, reference plane, direct basis relation, or governing pattern cannot support the claimed use. Preserve `unknown` only when the position remains live and admitted. If a selected method, selector outcome, acceptance result, plan, or work occurrence appears inside the signature, split that value into its direct governing pattern.

A changed or invalid signature position reopens an earlier downstream result only when that result relied on the changed position. The downstream pattern repairs or supersedes its own result. A revised signature does not imply that the problem disappeared or that prior work did not occur.

#### C.22:5.2b - Evolution and currentness boundaries

C.22 revises the smallest affected four-row position and issues a new TaskSignature edition when semantic content changes. A changed problem formulation returns to `C.22.2` before a replacement assignment is made. `G.11` governs relied-on source edition, freshness, decay, telemetry, and currentness relations; its result may trigger signature review but does not rewrite the signature by itself. `C.18` and `C.19` govern archive, front, lineage, and live-pool evolution. `G.5` governs selected-set and method-family selector results. `E.23` governs repeated object-version improvement. C.22 introduces no local refresh object and does not rewrite earlier selector results or dated work without an explicit dependency.

`TaskKind` fills SubjectKind. `TaskFamilyRef?` names one comparison-relevant family in the Vocabulary when specialization, transfer, or parity is live. `KindSet` and the A.2.6 scope slices determine the ranged extent. None is a record-format field, selected method, or selector result.

**DesignRunTag hygiene.** Do not mix DesignRunTag in one signature edition; record GateCrossings as CrossingBundles under their direct patterns when design-time claims are reused in run-time work.

##### C.22:5.2.1 - Specialization-claim reference discipline (normative)
A claim that one holder, dyad, team, or explicitly scoped specialist portfolio acquired usable specialization is complete only when it states one declared `TaskFamilyRef` or `TaskSignature@Context`, one named work-measure threshold target, an adaptation budget, and the freshness or provenance basis for reuse. A method may be selected, refined, or retired as part of that story, but the method is not the bearer of the specialization claim. The TaskSignature declaration and assignment relation stay rich enough for the same task family and work target to remain admissible in `C.22.1` adaptation signatures, `G.5` specialization profiles, and `G.9` adaptation parity without reconstructing the claim from narrative prose.

Low-human-overlap or newly discovered task families remain admissible when those task-family or signature references are explicit by value.
#### C.22:5.3 - Provenance & planes.
Record **Context** and **ReferencePlane** for each value; on any cross-Context or cross-plane reuse, attach BridgeDescription plus UTS row and apply **CL** and, when planes differ, **CL^plane** penalties to **R_eff only**. The governing policy admits **Φ(CL)** and **Φ_plane** only when they are **monotone, bounded, and table-backed**. Do not use “distance” language; penalties never mutate F and G. Record policy ids in SCR and cite Bridge ids on crossings.

#### C.22:5.4 - Attachment & use.

The bullets below state the contract expected by downstream uses of the assigned TaskSignature. C.22 does not execute eligibility, acceptance, selection, archive treatment, or generator-family choice. Their verdicts and returned sets remain results of the named direct patterns.

* **Eligibility** gates read TaskSignature against each **MethodFamily.Eligibility** (C.23) and **CG‑Spec.MinimalEvidence** for referenced characteristics.
* **Acceptance** clauses (G.4) use these fields for **acceptance-gate threshold predicates** (acceptance-gate thresholds live in Acceptance only).
* **Selection kernel** (G.5.S3) applies an **admissible order** (often partial); **weighted sums across mixed scale types are inadmissible**. If only a partial order remains, **return a Pareto (non‑dominated) set** with tie notes. If `PortfolioMode=Archive`, the selector **may** return a **QD archive** (per `ArchiveConfig`) **in addition to** or **instead of** a Pareto set. **Illumination** enters dominance **only** if `DominanceRegime=ParetoPlusIllumination` is **enabled by CAL** (policy id cited); otherwise, QD telemetry values are **reported** but **excluded** from dominance.
* When `GeneratorIntent` is present, G.5-governed selection may use a registered **`GeneratorFamily`** (POET‑class); the selection domain becomes **pairs** `{environment, method}`, with Environment guarded by **`EnvironmentValidityRegion`** and **`TransferRulesRef`** (C.23 wiring). Report **`IlluminationSummary`** as a **telemetry summary over `Diversity_P`** (report‑only by default) in telemetry; dominance remains unaffected unless policy changes as above.

#### C.22:5.5 - Unknowns.
An identity position needed for positive closure cannot be replaced by `unknown`. A live characteristic or predicate may preserve `unknown` when its direct pattern admits it. The TaskSignature cites the downstream policy that governs the consequence; C.22 performs no implicit coercion and declares no universal outcome set.

#### C.22:5.6 - Publication.
When a named receiving use needs an addressable publication episteme, output a `C.2.1`-conformant **ProblemProfile** that carries the bound TaskSignature and only the evidence, currentness, crossing, and representation relations on which that use relies. Apply F.18 and F.17 Name Cards when a durable new name is actually being admitted; do not create name cards merely because a local field is present. Keep any vendor or tool examples in Plain explanatory use rather than letting them become normative selector inputs. When no publication reliance is current, the TaskSignature closes without a separate ProblemProfile.

#### C.22:5.7 - Open‑Ended tasks (GeneratorFamily) *(normative)*.
When **open-ended generation** of tasks or environments is current, S2 is complete only when it includes `GeneratorIntent` with pointers to **`EnvironmentValidityRegion`** (admissible region for generated environments), **`TransferRulesRef`** (cross‑environment transfer constraints), and **coverage and regret** telemetry expectations. Selector outputs are then declared sets over **{environment, method}**; **coverage and regret** are reported telemetry values and **IlluminationSummary** is a **telemetry summary** (reported), excluded from dominance unless a **CAL** policy promotes them (policy‑id recorded in SCR; see `DominanceRegime`). Edition increments of **CharacteristicSpaceRef.edition**, **DescriptorMapRef.edition**, **DistanceDefRef.edition**, and (OEE) **`TransferRulesRef.edition`**, and the **policy id** associated with an illumination increase form part of the SCR change record.

