---
chunk_kind: "child"
pattern_id: "C.19"
pattern_title: "Explore-Exploit Live-Pool Governor"
section_id: "C.19:4"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/C.19/C.19__010_solution.md"
commit_sha: "3d098629dc218572089f1890080c17d6f1d9a867"
heading_path:
  - "C.19 — Explore-Exploit Live-Pool Governor"
  - "C.19:4 — Solution"
line_start: 49379
line_end: 49604
dependencies:
  - "A.19.CPM"
  - "A.19.SelectorMechanism"
  - "B.3"
  - "C.11"
  - "C.16"
  - "C.17"
  - "C.18"
  - "C.19"
  - "C.22.PFR"
  - "C.24"
  - "C.28"
  - "C.32"
  - "C.32.P2S"
  - "C.35"
  - "E.17"
  - "E.24.PUB"
  - "G.11"
  - "G.5"
  - "G.9"
keywords:
  - "already-live candidate pool"
  - "audience availability"
  - "change trigger"
  - "explore-exploit"
  - "governing lens"
  - "keep frontier"
  - "narrow to subset"
  - "pool-policy result"
  - "publication face"
  - "publication occurrence"
  - "selector-facing declaration"
  - "sunset line"
  - "widen"
---

### C.19:4 - Solution

#### C.19:4.1a - Causal data and causal-policy exploration hook

When an exploration and exploitation policy collects data to support a causal claim, changes intervention budget, learns a causal policy, evaluates a policy from behavior-policy data or logging-policy data, or treats a counterfactual strategy as a candidate line, the pool-policy claim remains within C.19's scope and cites `C.28` for causal-use support.

Optional `PoolPolicyResult.causalUseSpec?`:

```text
PoolPolicyResult.causalUseSpec? {
  causalUseQuestionRef?: U.CausalUseQuestion
  targetCausalityLadderRung: CausalityLadderRung
  causalUseClaimKind: CausalUseClaimKind
  causalActionPolicyClass?: CausalActionPolicyClass
  causalEvidenceSupportBasis?: CausalEvidenceSupportBasis
  causalUseEvidenceDesignRef?
  offPolicyCausalEvaluationProfileRef?
  causalUseSupportRecordRef?: CausalUseSupportRecordRef
  causalUseSupportVerdict?: CausalUseSupportVerdict
  supportedUse: CausalUseSupportStatement
  unsupportedUse: CausalUseUnsupportedStatement
}
```

The causal-use support tail may be omitted only when the pool-policy result does not reach `CausalUseActivation`: it does not make, publish, rank, retire, deploy, or reuse a causal claim. If exploration or exploitation is justified by effect, counterfactual replay, causal policy support, or causal data collection, the support tail is present or the result is downgraded to a non-causal pool-policy reason.

What changes in practice: a frontier policy that explores "to learn what works", exploits a causal policy, or graduates a line because counterfactual replay looks better must declare the causal-use question, `CausalUseClaimKind`, causality-ladder rung, causal evidence support basis, and supported use and unsupported use before the pool-policy result can carry a causal claim.

What this does not authorize: use `C.19` only for pool treatment. Use `C.28` for causal-use support; no causal identification, causal fairness, off-policy causal evaluation, or counterfactual-realizability rule is supplied here.

Define EmitterPolicy (regime key, params, ε, K, insertion policy, and deduplication threshold) and selection lenses with a fixed pipeline (Eligibility → Dominance → Tie‑breakers); bind provenance (policy id, lens id) and guard promotions of `Surprise` or `Illumination` to dominance to explicit policy declarations.

**Decision-subject clarification.** Attribute any later choice to one declared `DecisionSubject` at explicit `DecisionSubjectGranularity`. Record measurement spaces and admissible policies in the semantic-frame epistemes that state them. Use LOG to describe lenses and policies; that description does not enact a choice.

**EmitterPolicy (named profile).** A context-local, versioned policy with canonical fields:
`{ emitterPolicyId, name?, regimeKey ∈ {UCB, Thompson, BO-EI, GP-UCB, PES, InformationGain, …}, params, explore_share∈[0,1], temperature τ≥0, rebalance_period, wild_bet_quota≥0, backstop_confidence (assurance level), epsilon_dominance ε, cell_capacity K, insertionPolicyRef, dedupThreshold, deduplicationBasisRef, deduplicationUnit }`.
`emitterPolicyId` is cited from a consuming record as `emitterPolicyRef`; `insertionPolicyRef` is a reference to the governed insertion policy; `dedupThreshold` is a declared scalar on the basis and unit named by `deduplicationBasisRef` and `deduplicationUnit`. Casing does not create a second field family.
`EmitterPolicy` is a context-local named policy profile, not a U-kind or a generation operator. A C.18 generation or archive record cites it only when the current pool treatment or insertion and deduplication rules actually use that profile. Use C.18 for generation, archive, and front claims. The profile is not a staffing or budget instruction.
Use the ordinary default tokens defined in `G.Core` and `G.5`. The rules below explain their pool-policy consequences without defining a rival default family.

**Decision-theory bridge.** Use `C.11` for theory-side choice among already-available options and for the meaning of `ProbeBudget`, `ValueOfInformation`, and `ValueOfComputation`. A pool-policy record may use those outputs only as criteria for graduation, keep-frontier, or sunset treatment; it does not restate local choice doctrine.

**Ordinary default references (if policy is unspecified):**
• **Dominance:** consume `DefaultId.DominanceRegime` from `G.Core` and `G.5`; in ordinary Q-front use this means `{Q components}` with `ConstraintFit=pass` as **eligibility gate**.
• **Tie-breakers:** the current policy may use a Novelty coordinate, `DeltaDiversity_P`/`ΔDiversity_P`, Surprise, or Illumination only when it names that tie-breaker. It need not fabricate results for optional tie-breakers it does not use.
  - For Novelty, cite each bearer's exact coordinate-result episteme: a complete C.16 measurement result for a measured value, or a C.2.1 ascription when the declared rule permits a non-measurement reading. Before comparing bearers, confirm compatible Novelty Characteristic and Scale editions, corpus/reference set and inclusion rule, similarity Method and encoder/model editions, ClaimScope, window, uncertainty, and evidence.
  - For Surprise, cite the exact coordinate result and its generative-model and training-basis editions, Scale, ClaimScope, window, uncertainty, and evidence.
  - For `DeltaDiversity_P`, cite the retained set, candidate, measurement-policy and Scale editions, descriptor or distance basis, window, evidence, and resulting marginal reading.
  - Illumination remains telemetry over `Diversity_P` unless the named policy explicitly promotes it. A promoted use still cites the report and its measurement basis.
  The words *Novelty*, *Surprise*, and *diversity* alone are not executable policy inputs.
• **Archive:** `K=1`, `ε=0`, deduplication in `CharacteristicSpace`.
• **Policy family:** one uncertainty-aware explore policy family with one declared regime key and explicit change triggers; `UCB`-class with moderate temperature and `explore_share ≈ 0.3–0.5` is one didactic starter profile, not the semantic default family.
• **Provenance (minimum):** record `DescriptorMapRef.edition`, `DistanceDefRef.edition`, `DHCMethodRef.edition`, `emitterPolicyRef`, `insertionPolicyRef`, scalar `dedupThreshold`, `deduplicationBasisRef`, `deduplicationUnit`, `timeWindow`, and `seeds`.

**Use-value and declared-Q boundary.** `C.16.Q` is the pattern for the selector-context meaning of use-value and its `Objective` form. When use-value participates in the current `Q`, declare `QS.UseValue` as an objective head in that exact `Q` and cite the current Q/comparator basis. When it does not participate in the current `Q`, keep the use-value criterion explicitly outside `Q` as a declared side condition or tie-breaker. A pool-policy record may use either declared position but cannot silently promote use-value into `Q` or construct the Q model.

**Scalarization lenses (policy‑level).** A lens `J_ℓ` declares: (a) hard eligibility conditions (e.g., ConstraintFit=pass), (b) soft aggregation (weights or curves), (c) trust policy (how assurance and CL discounts enter).
**Conformance.** A pool-policy record MUST name the lens used to pick from a frontier; scalarized rankings MUST NOT be presented as “the frontier”; the **`lens id MUST be recorded in provenance of each selection`**.

**Promotion rules (policy).**
- **Tie-breaks.** Use only the constituted and compatible results named by the current policy. Promotion of Surprise or Illumination into the dominance set MUST be declared by lens or policy id and captured in provenance.
- **Graduation.** A candidate line or pool member moves from Explore to Exploit only when eligibility holds and `assuranceResultRef` cites the exact B.3 assurance result whose bounded use supports the applicable `backstop_confidence` threshold for the current scope. An optional profile or its coordinate results may supply evidence about the candidate; the payload itself does not graduate.
- **Sunset or pivot.** A candidate line or pool member that fails the applicable VOI or backstop threshold receives the sunset or pivot treatment at `rebalance_period`. Its optional profile remains evidence, not the treated object.
**Policy logic is not generation or work.** In one C.19 use, compute and record a treatment over an already identified live pool. It does not recompute a C.18 front or archive, update a generator, seed a candidate, constitute dated `U.Work`, create or classify a local system-role kind, create or change an assignment occurrence or its state, establish responsibility, authority, or permission, approve a budget or plan, or authorize enactment. At enactment, recover only the branches that independently obtain; send unresolved claim-bearing “role” wording through `E.10.ROLE`.

**Pool-policy pass (per `rebalance_period`).**
1) Read the current C.18 archive/front reference and its replay boundary; do not recompute either object inside C.19.
2) Record the governing lens and desired policy values, such as `explore_share`, emitter-profile preference, `wild_bet_quota`, or an admitted heterogeneity constraint. These are policy values, not generation actions.
3) Apply eligibility and `backstop_confidence` to the pool-policy question: record graduation pressure and choose exactly one `currentTreatment` from `widen | keep_frontier | narrow_to_subset | sunset_line`. Record this graduation and treatment judgement under C.19.
4) If that judgement requires fresh candidates, a changed emitter mix or temperature, archive insertion, or front recomputation, set `nextQuestionPatternLocator = C.18` and pass only the desired emitter profile, quota or constraint, and the exact generation/archive/front reason. Apply C.18 to decide and record the generation, archive, and front operations.
5) If carrying out the treatment requires dated implementation, planning, staffing, or budget use, pass the policy record to the A.15 family; the policy record itself grants none of them.
6) Emit one `PoolPolicyResult` with `livePool`, `governingLens`, `currentTreatment`, `changeTrigger`, and any inputs required by the next subject pattern. The result may justify keeping, narrowing, graduating, or sunsetting a line without taking over the named next subject pattern's operation.

**Named lenses (heuristics; policy‑level, not norms)**
The following **lens profiles** are **illustrative heuristics**. Practitioners MAY reuse or modify them; they are **not** normative.
• **Frontier‑sweeper** — maintain attention on the full front; promote only when `backstop_confidence` holds.
• **Barbell** — enforce `explore_share ≥ θ` with a `wild_bet_quota`; otherwise exploit top‑trust region.
• **Spike‑first** — pick highest **Use‑Value** subject to `ConstraintFit=pass` and a small **Cost‑to‑Probe** cap.
• **Safety‑first** — minimize **SafetyRisk** subject to `Use‑Value ≥ θ` and `ConstraintFit=pass`.
• **Platform‑option** — maximize **Option‑Value** under probe cost bounds.
• **Pilot-then-scale** — optimize **Use-Value** on the declared pilot scope. Set `currentTreatment = widen` only when `assuranceResultRef` cites the exact B.3 assurance result whose supported scope includes the proposed wider pool, and `changeTrigger` names the satisfied assurance condition and that newly supported scope; otherwise keep the pilot scope.
• **Heterogeneity-first (illustrative profile).** Use only when the applicable policy already admits a heterogeneity constraint or sampler policy. The applicable policy may declare a `FamilyCoverage` or `MinInterFamilyDistance` gate, a family or subfamily quota, or a diversity-promoting sampler; no universal `k`, `δ_family`, quota vector, sampler class, DPP rule, or max-min rule is supplied here. Record only the admitted policy values and ids actually used.
**Conformance (lens recording).** A pool-policy record that uses a lens **MUST** record its **lens id** alongside `emitterPolicyRef`. (This restates and localizes C19-3.)

#### C.19:4.1 - Explicit pool-policy result

**Canonical record vocabulary.** A serialized `PoolPolicyResult` uses the field `governingLens` and exactly one `currentTreatment` token from `widen | keep_frontier | narrow_to_subset | sunset_line`. Reader prose may say *widen*, *keep the frontier*, *narrow to a subset*, or *sunset a line*, but those phrases are labels, not alternate serialized values. Do not use `lens` as a second field name.

At the end of a C.19 use, write one explicit pool-policy record rather than one atmospheric statement that exploration will continue somehow.

That result should state:

- the still-live pool, frontier, or family scope under governance now;
- the governing lens id or policy state;
- `currentTreatment`, chosen from `widen | keep_frontier | narrow_to_subset | sunset_line`;
- the event or threshold that would justify changing that treatment next.

A compact result may therefore state, for example:

- `livePool = frontier_F`
- `governingLens = barbell_policy_v2`
- `currentTreatment = keep_frontier`
- `changeTrigger = backstop_confidence reaches L1 for one retained line`

or, for one narrower family region:

- `livePool = family_region_beta`
- `governingLens = heterogeneity_first`
- `currentTreatment = narrow_to_subset`
- `changeTrigger = quota satisfaction plus a compatible cited C.17 Novelty coordinate result clearing novelty_floor_policy_v2`

Those fields define the result: live pool, governing lens, current treatment, and change trigger.

#### C.19:4.2 - Closure rule over the live pool

A `C.19` pass may close only when one explicit pool and one explicit next treatment are both visible.

- Close as `widen` when the current frontier is too narrow for the declared exploration policy or when the evidence basis is too thin to justify current narrowing.
- Close as `keep_frontier` when several lines must remain live under the current lens and no narrower admissible subset is yet justified.
- Close as `narrow_to_subset` when one declared lens now justifies retaining one smaller internal live set without pretending that one scalar winner has already been chosen.
- Close as `sunset_line` when one line or family region no longer clears the current lens, quota, or backstop requirements.

When the question has stopped being pool policy, finish the pool-policy result and use the exact handoff in `C.19:4.4`; the next pattern is recorded outside `currentTreatment`.

One internal retained subset here is still one pool-treatment result. It is not yet a declared `Shortlist` or `RankedShortlist`, and it has no `ShortlistId` merely by being retained. When a downstream use needs declaration or audience availability, use `C.19:4.4`.

If the result still cannot say which pool remains live, which lens and policy apply, and which event would justify changing the treatment, it is still unfinished pool policy rather than one finished `C.19` result.

#### C.19:4.3 - Minimal pool-policy record

The smallest useful `C.19` record usually states:

- `livePool = ...`
- `governingLens = ...`
- `currentTreatment = widen | keep_frontier | narrow_to_subset | sunset_line`
- `changeTrigger = ...`
- `nextQuestionPatternLocator? = ...` only when the question is no longer pool policy
- `learningProgressSignal? = ...` when an autotelic or capability-discovery reason materially supports widening, keeping the frontier live, or probing one goal region further
- `competenceModelRef? = ...` when the pool policy depends on a model of what the system or method family can learn next
- `goalSpaceExpansionCue? = ...` when the admissible next treatment widens the goal and task palette rather than merely re-ranking current candidates
- `goalSpaceExpansionPolicyRef? = ...` when goal and task space growth is itself governed by one declared archive or curriculum expansion policy
- `assuranceResultRef? = ...` when graduation, scaling, or widening relies on one exact B.3 assurance result and its bounded supported scope
- `whyNotLocalChoice = ...` when the result might otherwise be mistaken for `C.11`

An admissible short record may therefore read:

```text
livePool = frontier_F
governingLens = barbell_policy_v2
currentTreatment = keep_frontier
changeTrigger = backstop_confidence reaches L1 for one retained line
whyNotLocalChoice = several family regions remain live
```

When `currentTreatment = narrow_to_subset`, `livePool` still names one internal retained subset or one live pool subset. It does not yet mint one public `Shortlist`, one public `RankedShortlist`, or one `ShortlistId`. If selector-facing result declaration is now required, the admissible `C.19` record leaves `currentTreatment` as the last pool treatment and fills `nextQuestionPatternLocator = G.5`, with the reason that result declaration rather than pool policy is now current.

Goal and task space growth is one pool-policy doctrine over the archive or curriculum side. When autotelic or capability-discovery pressure is active, cite `goalSpaceExpansionPolicyRef` together with the supporting `learningProgressSignal`, `competenceModelRef`, or `goalSpaceExpansionCue`; that doctrine may justify `widen`, `keep_frontier`, or one further probe decision value, but it does not become default `Q`, does not rename the front, and does not declare one selector-facing shortlist without `G.5`.

If the record does not already state which pool remains live, which lens and policy apply, and what would change that treatment next, it is still one unfinished `C.19` result.

#### C.19:4.3a - Worked closure slice

Three short contrasts keep the closure law practical.

**Several family regions remain live.**
When the point is to keep several lines active under one declared lens, the pool-policy result must not imply that one local choice has already been made:

```text
livePool = frontier_F
governingLens = frontier_sweeper_v3
currentTreatment = keep_frontier
changeTrigger = one retained line reaches backstop_confidence L1
whyNotLocalChoice = three family regions remain live
```

**One region should now be sunset.**
When a region's compatible cited Novelty coordinate result no longer clears the active floor, or the region no longer clears the backstop, state that treatment directly rather than leaving the retirement implicit:

```text
livePool = family_region_beta
governingLens = barbell_policy_v2
currentTreatment = sunset_line
changeTrigger = reopen only if new evidence or quota deficit reactivates the region
whyNotLocalChoice = other regions still remain live under the same pool policy
```

**The pool has already been narrowed and the next question is selector-facing result declaration.**
When one internal retained subset is already explicit and the next question is to declare it for downstream use, close the pool-policy question by naming the applicable pattern instead of presenting that subset as though it were already one selector result:

```text
livePool = retained_subset_{option_B, option_C}
governingLens = pool_policy_completed
currentTreatment = narrow_to_subset
changeTrigger = retained subset is explicit; pool policy is complete
nextQuestionPatternLocator = G.5 because selector-facing result declaration is now current
whyNotLocalChoice = pool governance is already complete
```

#### C.19:4.3b - Cultural and style live pools

Use the same minimal pool-policy record for cultural or style live pools when the current question is how several style, tradition, method-family, work-family, canon, scene, or technique variants remain live under one lens.

```text
PoolPolicyResult:
  livePool:
  governingLens:
  currentTreatment:
  changeTrigger:
  termBridgeRefs?:
  nextQuestionPatternLocator?:
```

The record states pool treatment only. If a label is unstable across communities, first recover its exact source-local meanings through `F.17` and use `F.18` for naming. Include `termBridgeRefs` only for an actual F.9 relation between exact sense cells. That reference identifies the sense relation; it does not by itself support this pool treatment. Any claim that relies on the Bridge for the treatment stays separate from `PoolPolicyResult`: state the named use, direction, correspondence rule, and tolerated loss in a C.2.1 claim, and establish the current A.10 or B.3 reliance required by F.18. If the question becomes the cultural-evolution case, finish the pool-policy result and set `nextQuestionPatternLocator = C.36`. For result declaration, audience availability, or currentness, use the exact exit in `C.19:4.4` rather than extending the pool-policy record.

#### C.19:4.4 - Exit from pool treatment

When fresh candidates, a changed emitter mix or temperature, archive insertion, or front recomputation are current, use `C.18` with the desired policy values and exact reason as the pool-policy pass requires. When the current question is whether one bearer or version should improve, use `E.23` and pass the exact bearer or version, objective or criterion, evidence, and pool-policy reason that made improvement current. A C.19 treatment is neither a generation operation nor an improvement result.

An internal subset retained by `narrow_to_subset` is still the live pool named by one C.19 policy record. It is not a public `Shortlist`, `RankedShortlist`, or `ShortlistId`-bearing selector artefact, and no public selector artefact is emitted by this pool-policy use. `Front` and `Archive` retain their C.18 meanings; a scalarized pick does not rename either one.

When the retained set must be declared for downstream comparison, registry use, or another selector-facing use, finish the pool-policy result and pass `G.5` the exact declared source set, lens or policy id, eligibility conditions, dominance set, tie-breakers, promotion policy, and provenance pins. Use `G.5` to declare the selected-set result and any stable public shortlist identity required by a named use. The C.19 record supplies only the preceding pool treatment and the reason result declaration is now current. If actual audience availability is also current, use `E.17` for a source-backed publication face and return to source and `E.24.PUB` for the publication occurrence and availability.

When the live question becomes which option to choose, finish the pool-policy result and pass the fixed option set and comparison basis to `C.11`; a C.19 subset is not a `ChoiceResult`. When the question becomes enactment or performed work, use `C.24` and the A.15 family. Resource bounds, `CostToProbe`, `ValueOfInformation`, `ValueOfComputation`, `explore_share`, and `backstop_confidence` may explain a pool treatment, but they establish no budget, plan, Work occurrence, local system-role kind, separate System-classification judgment, assignment occurrence or state, responsibility, authority, permission, or enactment. Recover each needed fact independently, and send unresolved claim-bearing “role” wording through `E.10.ROLE`. When edition, source, descriptor, policy, or evidence currentness becomes the live question, use `G.11`; a change trigger in C.19 does not itself perform refresh or create a refreshed edition.

The practical handoff is therefore small: preserve the exact C.18 archive or front reference, the C.19 live-pool treatment and change trigger, and the evidence needed by the named next pattern. Do not duplicate selector-result declaration, publication availability, choice, work, or refresh semantics inside C.19.

