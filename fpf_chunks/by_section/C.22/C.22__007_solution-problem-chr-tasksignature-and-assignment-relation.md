---
chunk_kind: "child"
pattern_id: "C.22"
pattern_title: "Task Typing and TaskSignature Assignment (Problem-CHR)"
section_id: "C.22:5"
section_title: "Solution — Problem CHR, TaskSignature, and assignment relation"
source_path: "FPF-Spec.md"
output_path: "by_section/C.22/C.22__007_solution-problem-chr-tasksignature-and-assignment-relation.md"
commit_sha: "72222c13cc1bba009f1ee1f1aca47654db8e5716"
heading_path:
  - "C.22 — Task Typing and TaskSignature Assignment (Problem-CHR)"
  - "C.22:5 — Solution — Problem CHR, TaskSignature, and assignment relation"
line_start: 50890
line_end: 51068
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
  - "F.9"
  - "G.0"
  - "G.4"
  - "G.5"
keywords:
---

### C.22:5 - Solution — Problem CHR, `TaskSignature`, and assignment relation

**Local TaskSignature mantra.** *Stabilize the problem; name the receiving selection question and task kind; keep only traits that can change eligibility, acceptance, or selection; type each live trait; preserve unknowns, scope, and any basis or currentness relation the use relies on; declare the TaskSignature, assign it to the problem-side episteme for that use, and stop before selecting a method.* This is a short repeatable rendering of the C.22 Solution. It is not a selector algorithm, method recommendation, work plan, dated selection occurrence, or `DemonstrativeUnfoldingSlice@Context`.

Apply that formula as follows:

1. Confirm that the problem-side representation is stable enough for selector-facing use; otherwise use `C.22.2`.
2. Name the receiving eligibility, acceptance, or selection question and the `TaskKind`, optional task family, or work target that the signature will declare.
3. Include only the problem traits whose values can change that receiving use. Leave a non-current optional extension absent.
4. Type each live characteristic by scale, unit, polarity, reference plane, and admitted comparison relation before aggregation or comparison.
5. Preserve a live but unknown value as `unknown`; include or reference the exact scope, evidence relation, freshness or edition condition on which later use relies. When cross-semantic reuse is current, resolve the two local senses and test the F.9 Bridge separately; a shared label, scheme, or plane does not establish it.
6. Close with one minimal `TaskSignature`. Pass later eligibility and acceptance claims to `C.23` and `G.4`, and actual method-family selection to `G.5`; do not put their outcomes back into the signature as if they were problem traits.

#### C.22:5.0a - Positive closure, bounded non-use, and local return

Close the C.22 use positively when the direct TaskSignature fields, Vocabulary, Laws, and Applicability are complete and `TaskSignatureAssignmentRelation` recovers the exact problem-side episteme, TaskSignature, receiving-use episteme, effective ReferenceScheme, ClaimScope, and current qualification conditions. Each live characteristic has its scale, unit, polarity, reference plane, admitted comparison relation, and value or explicit `unknown`; every relied-on evidence, freshness, or edition relation is named. When cross-semantic reuse is current, its exact local senses, obtaining F.9 Bridge, and separate bounded-use claim are recoverable. A downstream selector can now consume the assigned signature without guessing, but no eligibility verdict, acceptance result, method recommendation, selector outcome, WorkPlan, or dated Work is claimed.

Close by bounded non-use when problem framing is not stable enough for a TaskSignature declaration, when no selector-facing receiving use is current, or when the current question has already become eligibility, acceptance, selection, planning, or performed work. A non-current optional extension remains absent. If several signatures or assignment relations remain plausible, preserve them as candidates under the governing problem or selection pattern rather than asserting one assignment.

Return to the smallest affected TaskSignature position when its receiving question, exact target, effective ReferenceScheme, ClaimScope, `TaskKind`, task-family reference, characteristic meaning, scale, unit, polarity, reference plane, unknown status, evidence-use relation, freshness condition, or edition changes. Recheck the F.9 endpoint senses, Bridge predicate, bounded-use claim, or reliance result only when that exact dependency changed. Keep the upstream `ProblemCard` and downstream selection history unchanged unless that exact change invalidates them under their own subject patterns.

**Worked local repair.** A machining TaskSignature originally records surface finish as an ordinal visual grade. The named use later adopts measured roughness `Ra` on a ratio scale in micrometres with a named measurement and evidence relation. Repair the affected characteristic head, scale, unit, admitted comparisons, and evidence relation. Keep the machining `TaskKind`, unaffected constraints, scope, and prior Work history. Reopen eligibility, acceptance, or Method-family selection only when its earlier result relied on the replaced finish head; state the new result under the exact downstream predicate with its subject-pattern locator.

#### C.22:5.0b - Apparatus proportionality

Use the lightest signature declaration and assignment relation that the named receiving use can consume:

1. **Minimal selector-facing use.** Materialize one TaskSignature with only the live fields needed by the current eligibility, acceptance, or selection question. This is the ordinary positive result of C.22.
2. **Reliance-bearing use.** Add an addressable `ProblemProfile` episteme only when delayed feedback, audit, transfer, automation, expensive reversal, or another named use relies on replay beyond the local assignment relation. Pin the exact problem-side episteme and edition, TaskSignature edition, receiving use, every relied-on field-basis relation with its subject pattern, qualification window, review trigger, and any current evidence or currentness relation. When this use crosses local meanings, test F.9. Add an actual Bridge and separate bounded-use claim only if its predicate is true; otherwise keep the local values separate and stop that reuse.
3. **Extension-bearing use.** Add QD, OEE, archive, generator, parity, or specialization positions only when that exact downstream relation is current and its direct pattern requires those values.

More fields, publication packaging, name cards, or telemetry do not make the problem better formulated, the TaskSignature more true, or a method more suitable. If no selector-facing receiving use needs a TaskSignature, close by bounded non-use rather than publishing a thin declaration for its own sake.

#### C.22:5.1 - Minimal CHR fields (tri‑state aware).
**Selector-side field boundary.** The fields below are live only after problem framing has been stabilized enough to ask eligibility, acceptance, selection, Method-family, or policy-constrained choice questions. They are not a universal problem-framing checklist and do not replace the `C.22.2` Thin `ProblemCard` pass for a messy signal. Each live characteristic field is **CHR-typed** by Characteristic, Scale, Unit, and Polarity under MM-CHR discipline. A live predicate may preserve `unknown` only when its exact value rule permits it; the cited downstream policy states what follows. This aligns G.4 and G.6 without making their results C.22 values.

**Optional extension absence rule.** If QD, OEE, archive, generator, parity, specialization, or another optional relation is not live for the current case, the corresponding optional fields are absent, not `unknown`. Use `unknown` only for a live field whose value is currently unknown. An absent non-live extension triggers no downstream disposition.

* **`DataShape`** — data regime and admissible transforms (e.g., tabular, sequence, graph; density; stationarity claims).
* **`NoiseModel`** — uncertainty class and robustness envelope (e.g., iid Gaussian; heavy‑tailed; adversarial budget).
* **`ObjectiveProfile`** — objective heads (**Scale, Unit, Polarity** and **ReferencePlane** declared), polarity, and **admissible order relations** (lexicographic, Pareto, medoid or median where admissible). **Weighted sums across mixed scale types are inadmissible**; ordinal heads use order-only guards. For QD tasks, explicitly enumerate quality heads, diversity or descriptor-space heads, and any policy-authorized QD contribution heads; see **DominanceRegime** below. Do not introduce a default QD score. If a scalar or set-scalarization policy is live, cite the governing CAL policy and keep the uses of dominance and telemetry explicit.
* `RegularityTraits` — method-relevant structure (**convexity, differentiability, separability, monotonicity**) as CHR-typed predicates with guard macros (for example, `ORD_COMPARE_ONLY`, `UNIT_CHECK`, `POLARITY_CHECK`). Include `ConditionClass` such as stiffness or kappa proxies where applicable.
* **`Constraints`** — explicit hard and soft constraint classes (feasibility predicates; **ResourceEnvelope** and **RiskEnvelope**). **Acceptance-gate thresholds live in `G.4` only; never inside CHR or code paths.**
* `ShiftClass` and stationarity — CHR‑typed claims about regime stability (iid | covariate‑shift | concept‑drift | adversarial). Default=`unknown`. The cited acceptance or selector policy governs the consequence of that unknown for its receiving use.
* **Evidence and assurance (conditional).** Include an exact **A.10** evidence-use or provenance relation only when the receiving use relies on it. State source edition, currentness, or freshness only to the degree that reliance requires. Open **B.3** only for a named assurance claim or material-reliance threshold, and use only the assurance lanes and fold that its declared policy requires. A TaskSignature by itself requires neither all TA/VA/LA lanes nor a Gamma-fold.
* `ScopeSlice(G)` — the **USM claim-bounding scope cut** over **EntityOfConcernRef and scope** (discipline governance in **CG‑Spec**; Domain is a catalog mark only).
* `SizeAndConditionProfile` — size and condition proxies (**n, m, kappa, sparsity**) with **declared units**; a unit mismatch makes the current comparison unsupported until the direct acceptance or selector policy supplies its governed result.
* **`Freshness` (conditional)** — the validity window for a descriptor only when the receiving use relies on its currentness.
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

#### C.22:5.2 - `TaskSignature` declaration and assignment

`TaskSignature` is a C.2.1 episteme and a species of A.6.0 `U.Signature`. It uses A.6.0 identity and declaration content directly rather than a flat record schema. Add an optional `SignatureManifest` only when dependency replay requires actual imports and provided names; `SignatureId` and edition are designators and currentness handles, not substitutes for identity.

```text
TaskSignature <: U.Signature

EntityOfConcernRef = exact task or work target declared for the named receiving use
effectiveReferenceScheme = exact scheme in which TaskKind, TaskFamilyRef?, KindSet, and characteristic values are interpreted
SubjectKind = TaskKind, one exact C.3 U.Kind value
RangedValueKind = U.Entity
SliceSet = declared A.2.6 claim-scope slices
ExtentRule = entities admitted by KindSet inside those slices
ResultKind = absent; selector outcomes are not TaskSignature values

Vocabulary:
  TaskFamilyRef?
  KindSet
  characteristic bindings with Scale, Unit, Polarity, ReferencePlane, admitted comparison relation, and value or admitted unknown
  constraint relation references
  evidence-use relation references only when the receiving use relies on them
  optional QD, OEE, archive, generator, parity, budget, telemetry, and specialization vocabulary only when current

Laws:
  include only positions that can change eligibility, acceptance, or selection for the declared use
  preserve admitted unknown and distinguish it from absent non-current vocabulary
  apply CHR scale, unit, polarity, ReferencePlane, and comparison legality before aggregation
  keep acceptance verdicts, selector outcomes, selected methods, plans, Work, and performed results outside the signature
  keep each reliance-bearing field connected to its exact basis relation and subject pattern

Applicability:
  exact U.ClaimScope and any required A.2.6 membership
  declared qualification or use window when current
  qualification, freshness, edition, and evidence-use conditions on which use relies
  exact F.17 local senses, an obtaining F.9 Bridge, and a separate bounded-use claim only when cross-semantic reuse is current
```

The field families in C.22:5.1 are projections of Vocabulary and Applicability. They are not extra conceptual rows and do not redefine A.6.0.

The assignment is a separate relation with exactly three direct participants:

```text
TaskSignatureAssignmentRelation <: U.Relation
  ProblemSideEpistemeSlot = <ProblemSideEpistemeSlot, U.Episteme, U.EpistemeRef>
  TaskSignatureSlot = <TaskSignatureSlot, U.Signature, U.EntityRef constrained to TaskSignature>
  ReceivingUseEpistemeSlot = <ReceivingUseEpistemeSlot, U.Episteme, U.EpistemeRef>
```

The relation obtains while the exact receiving use actually adopts that exact TaskSignature as the task-typing declaration for the exact problem-side episteme under the stated scheme, scope, and qualification conditions. Co-publication, a card field, a shared label, or one record row does not make it obtain. One occurrence is identified by the three participants plus its maximal continuous actual assignment extent. A participant change yields another occurrence; actual withdrawal and later readoption yield distinct occurrences even when the same three participants return.

**TaskSignature identity and publication.** The tuple `<declaration content, EntityOfConcernRef, effectiveReferenceScheme>` determines TaskSignature episteme identity under A.6.0 and C.2.1. `SignatureId` and edition designate and track that episteme. A semantic change to direct declaration fields, Vocabulary, Laws, Applicability, the exact target, or the effective scheme creates a revised signature edition. Two E.17 publications, database rows, cards, or files may present the same edition when they resolve to the same tuple and add no new claim. `ProblemProfile` may reference the signature and assignment relation but contains or becomes neither.

**Minimality rule.** Include only declaration positions needed to determine eligibility, acceptance, or admissible selection for the named use. Additional traits remain outside Vocabulary until a later use makes them current.

Values are CHR-typed and tied to the exact measurement, evidence-use, source-use, representation, or scope relation that justifies their use when such a relation is current. Each reliance-bearing field basis names that relation and its subject pattern; generic provenance or support wording is not a replay basis. Unknowns preserve their direct missingness semantics.

**TaskSignature invariants.** A positive assignment satisfies all six conditions:

1. The TaskSignature exposes its exact `EntityOfConcernRef`, effective `U.ReferenceScheme`, direct declaration fields, Vocabulary, Laws, and Applicability.
2. The assignment relation recovers its exact problem-side episteme, exact TaskSignature, exact receiving-use episteme, obtaining conditions, and occurrence extent.
3. Every live field has an admitted filler kind or scale discipline and, under reliance, an exact basis relation with a subject pattern.
4. A live but unrecovered value is `unknown` only where the field's exact value rule permits it and a downstream policy states how the named use handles it.
5. A non-current optional extension is absent; absence and unknown are not interchangeable.
6. Eligibility verdicts, acceptance results, selected methods, selector outcomes, WorkPlans, and Work occurrences are absent from the TaskSignature and remain with their direct patterns.

#### C.22:5.2a - Lowering and withdrawal conditions

Withdraw the assignment for the current receiving use when its problem-side episteme, TaskSignature, receiving-use episteme, scheme, scope, or qualification conditions cannot be recovered. The TaskSignature may remain a valid declaration for another assignment. Use C.22.2 only when the problem-side representation itself is no longer stable enough.

Revise the TaskSignature edition when a direct declaration field, Vocabulary, Law, Applicability claim, `EntityOfConcernRef`, or effective `U.ReferenceScheme` changes. Lower or remove one vocabulary position when its filler kind, scale, unit, polarity, reference plane, direct basis relation, or subject pattern cannot support the claimed use. Preserve `unknown` only when the position remains live and admitted. Split any selected method, selector outcome, acceptance result, plan, or Work occurrence into its subject pattern.

A changed or invalid signature position reopens an earlier downstream result only when that result relied on the changed position. The downstream pattern repairs or supersedes its own result. A revised signature does not imply that the actual Problem disappeared or that prior Work did not occur.

#### C.22:5.2b - Evolution and currentness boundaries

C.22 revises the smallest affected identity or declaration-content component and issues a new TaskSignature edition when semantic content changes. A changed problem formulation requires C.22.2 before a replacement assignment is made. `G.11` governs relied-on source edition, freshness, decay, telemetry, and currentness relations; its result may trigger signature review but does not rewrite the signature by itself. `C.18` and `C.19` govern archive, front, lineage, and live-pool evolution. `G.5` governs selected-set and method-family selector results. `E.23` governs repeated object-version improvement. C.22 introduces no local refresh object and does not rewrite earlier selector results or dated Work without an explicit dependency.

`TaskKind` fills SubjectKind. `TaskFamilyRef?` names one comparison-relevant family in Vocabulary when specialization, transfer, or parity is live. `KindSet` and A.2.6 scope slices determine the ranged extent. None is a record-format field, selected method, or selector result.

**DesignRunTag hygiene.** Do not mix DesignRunTag positions in one signature edition. If design-side information is reused in run-time Work, identify the actual receiving Work and its relations independently. Cite an E.18 structural `GateCrossing` only when a selected transformation-flow use contains that occurrence; it does not require a package and does not establish an F.9 Bridge.

##### C.22:5.2.1 - Specialization-claim reference discipline (normative)
A claim that one holder, dyad, team, or explicitly scoped specialist portfolio acquired usable specialization is complete only when it states one declared `TaskFamilyRef` or `TaskSignature`, one named work-measure threshold target, an adaptation budget, and the freshness or provenance basis for reuse. A method may be selected, refined, or retired as part of that story, but it is not the subject of the specialization claim. The TaskSignature declaration and assignment remain rich enough for the same task family and work target to stay admissible in `C.22.1` adaptation signatures, `G.5` specialization profiles, and `G.9` adaptation parity without reconstructing the claim from narrative prose.

Low-human-overlap or newly discovered task families remain admissible when those task-family or signature references are explicit by value.
#### C.22:5.3 - Provenance, schemes, and planes

Record the effective `U.ReferenceScheme`, `U.ClaimScope`, and any `ReferencePlane` needed to interpret a relied-on value. A difference in scheme or plane opens a comparison question; it does not by itself establish a Bridge, forbid use, or impose a penalty.

For cross-semantic reuse, recover the two exact F.17 local senses and test the direct F.9 predicate. Cite a Bridge only when that predicate is true. Then state the proposed use separately: the action, direction, correspondence rule, tolerated loss, and polarity. If no Bridge obtains, keep the local values separate and return the missing comparison or translation question instead of manufacturing correspondence.

Open A.10 only when evidence or provenance for that bounded use is current. Open B.3 only for a named assurance use or material-reliance threshold; only that B.3 result may use edge-scoped `CL` and the policy it actually declares. An optional local F.9 `CL` note is evidence shorthand, not a use threshold or automatic penalty. A card, gate check, reusable package, or other publication is required only when its own receiving pattern independently needs it. The assignment receives no generic setting participant, and a domain, organization, location label, or shared carrier supplies none of these relations.

#### C.22:5.4 - Attachment & use.

The bullets below state which TaskSignature fields and relations each downstream use reads. C.22 does not execute eligibility, acceptance, selection, archive treatment, or generator-family choice. Their verdicts and returned sets remain results of the named direct patterns.

* **Eligibility** gates read TaskSignature against each **MethodFamily.Eligibility** (C.23) and **CG‑Spec.MinimalEvidence** for referenced characteristics.
* **Acceptance** clauses (G.4) use these fields for **acceptance-gate threshold predicates** (acceptance-gate thresholds live in Acceptance only).
* **Selection kernel** (G.5.S3) applies an **admissible order** (often partial); **weighted sums across mixed scale types are inadmissible**. If only a partial order remains, **return a Pareto (non‑dominated) set** with tie notes. If `PortfolioMode=Archive`, the selector **may** return a **QD archive** (per `ArchiveConfig`) **in addition to** or **instead of** a Pareto set. **Illumination** enters dominance **only** if `DominanceRegime=ParetoPlusIllumination` is **enabled by CAL** (policy id cited); otherwise, QD telemetry values are **reported** but **excluded** from dominance.
* When `GeneratorIntent` is present, G.5-governed selection may use a registered **`GeneratorFamily`** (POET‑class); the selection domain becomes **pairs** `{environment, method}`, with Environment guarded by **`EnvironmentValidityRegion`** and **`TransferRulesRef`** (C.23 wiring). Report **`IlluminationSummary`** as a **telemetry summary over `Diversity_P`** (report‑only by default) in telemetry; dominance remains unaffected unless policy changes as above.

#### C.22:5.5 - Unknowns.
An identity position needed for positive closure cannot be replaced by `unknown`. A live characteristic or predicate may preserve `unknown` only when its exact value rule permits it. The TaskSignature cites the downstream policy that defines or constrains the consequence; C.22 performs no implicit coercion and declares no universal outcome set.

#### C.22:5.6 - Publication.
When a named receiving use needs an addressable publication episteme, output a `C.2.1`-conformant **ProblemProfile** that carries the bound TaskSignature and only the evidence, currentness, F.9 bounded-use, and representation relations on which that use relies. Apply F.18 and F.17 Name Cards when a durable new name is actually being admitted; do not create a card merely because a local field or Bridge is present. Keep vendor or tool examples in Plain explanatory use rather than letting them become normative selector inputs. When no publication reliance is current, the TaskSignature closes without a separate ProblemProfile.

#### C.22:5.7 - Open‑Ended tasks (GeneratorFamily) *(normative)*.
When **open-ended generation** of tasks or environments is current, S2 is complete only when it includes `GeneratorIntent` with pointers to **`EnvironmentValidityRegion`** (admissible region for generated environments), **`TransferRulesRef`** (cross‑environment transfer constraints), and **coverage and regret** telemetry expectations. Selector outputs are then declared sets over **{environment, method}**; **coverage and regret** are reported telemetry values and **IlluminationSummary** is a **telemetry summary** (reported), excluded from dominance unless a **CAL** policy promotes them (policy‑id recorded in SCR; see `DominanceRegime`). Edition increments of **CharacteristicSpaceRef.edition**, **DescriptorMapRef.edition**, **DistanceDefRef.edition**, and (OEE) **`TransferRulesRef.edition`**, and the **policy id** associated with an illumination increase form part of the SCR change record.

