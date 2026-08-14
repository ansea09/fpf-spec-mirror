---
chunk_kind: "child"
pattern_id: "C.19"
pattern_title: "Explore-Exploit Live-Pool Governor"
section_id: "C.19:4"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/C.19/C.19__010_solution.md"
commit_sha: "7205ce8cea50eb778520a026373b2b7bcbc43fbb"
heading_path:
  - "C.19 — Explore-Exploit Live-Pool Governor"
  - "C.19:4 — Solution"
line_start: 49695
line_end: 49917
dependencies:
  - "A.15"
  - "A.19.CPM"
  - "A.19.SelectorMechanism"
  - "B.3"
  - "C.11"
  - "C.16"
  - "C.17"
  - "C.18"
  - "C.22.PFR"
  - "C.24"
  - "C.28"
  - "C.32"
  - "C.32.P2S"
  - "C.35"
  - "E.17"
  - "E.23"
  - "E.24.PUB"
  - "G.11"
  - "G.5"
  - "G.9"
keywords:
  - "already-live candidate pool"
  - "change trigger"
  - "explore-exploit"
  - "governing lens"
  - "keep frontier"
  - "narrow to subset"
  - "pool-policy result"
  - "sunset line"
  - "widen"
---

### C.19:4 - Solution

#### C.19:4.1a - Causal data and causal-policy exploration hook

When an exploration and exploitation policy collects data to support a causal claim, changes intervention budget, learns a causal policy, evaluates a policy from behavior-policy data or logging-policy data, or treats a counterfactual strategy as a candidate line, the pool-policy result keeps `C.19` authority and cites `C.28` for causal-use support.

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

What this does not authorize: `C.19` does not become causal identification, causal fairness, off-policy causal evaluation, or counterfactual-realizability authority; it governs pool treatment and redirects causal-use support to `C.28`.

Define EmitterPolicy (regime key, params, ε, K, insertion policy, and deduplication threshold) and selection lenses with a fixed pipeline (Eligibility → Dominance → Tie‑breakers); bind provenance (policy id, lens id) and guard promotions of `Surprise` or `Illumination` to dominance to explicit policy declarations.

**Decision-subject clarification.** Later choices are attributed to one declared `DecisionSubject` at explicit `DecisionSubjectGranularity`. **Contexts state** measurement spaces and admissible policies as **semantic frames**; LOG profiles lenses and policies but does **not** enact choices.
**Depends on.** **C.18** for archive and front stewardship, **C.16** for characteristic and measurement claims, **A.19.CPM** and **A.19.SelectorMechanism** for comparison and selection kernels, **B.3** for assurance-sensitive confidence claims, and **G.5** and **G.11** for selector-facing set-result declaration and refresh.

**EmitterPolicy (named profile).** A context-local, versioned policy with canonical fields:
`{ emitterPolicyId, name?, regimeKey ∈ {UCB, Thompson, BO-EI, GP-UCB, PES, InformationGain, …}, params, explore_share∈[0,1], temperature τ≥0, rebalance_period, wild_bet_quota≥0, backstop_confidence (assurance level), epsilon_dominance ε, cell_capacity K, insertionPolicyRef, dedupThreshold, deduplicationBasisRef, deduplicationUnit }`.
`emitterPolicyId` is cited from a consuming record as `emitterPolicyRef`; `insertionPolicyRef` is a reference to the governed insertion policy; `dedupThreshold` is a declared scalar on the basis and unit named by `deduplicationBasisRef` and `deduplicationUnit`. Casing does not create a second field family.
`EmitterPolicy` is a context-local named policy profile, not a U-kind or a generation operator. A C.18 generation or archive record cites it only when that profile actually governs the current pool treatment or its insertion and deduplication policy. Use C.18 for generation, archive, and front claims. The profile is not a staffing or budget instruction.
Ordinary default tokens remain governed by `G.Core` and `G.5`; `C.19` explains their pool-policy consequences but does not become one rival default authority.

**Decision-theory bridge.** `C.11` governs theory-side choice among already-available options and the meaning of `ProbeBudget`, `ValueOfInformation`, and `ValueOfComputation`. `C.19` may consume such outputs only as criteria for pool policy, graduation, keep-frontier, or sunset treatment; it does not re-govern local choice doctrine.

**Ordinary default references (if policy is unspecified):**
• **Dominance:** consume `DefaultId.DominanceRegime` from `G.Core` and `G.5`; in ordinary Q-front use this means `{Q components}` with `ConstraintFit=pass` as **eligibility gate**.
• **Tie‑breakers:** `Novelty@context`, `ΔDiversity_P`, `Surprise`; `Illumination` (telemetry over Diversity_P, including coverage and QD‑score) MAY be used as a tie‑breaker but is **not** in the dominance set.
• **Archive:** `K=1`, `ε=0`, deduplication in `CharacteristicSpace`.
• **Policy family:** one uncertainty-aware explore policy family with one declared regime key and explicit change triggers; `UCB`-class with moderate temperature and `explore_share ≈ 0.3–0.5` is one didactic starter profile, not the semantic default family.
• **Provenance (minimum):** record `DescriptorMapRef.edition`, `DistanceDefRef.edition`, `DHCMethodRef.edition`, `emitterPolicyRef`, `insertionPolicyRef`, scalar `dedupThreshold`, `deduplicationBasisRef`, `deduplicationUnit`, `timeWindow`, and `seeds`.

**Use-value and declared-Q boundary.** `C.16.Q` is the pattern for the selector-context meaning of use-value and its `Objective` form. When use-value participates in the current `Q`, declare `QS.UseValue` as an objective head in that exact `Q` and cite the current Q/comparator basis. When it does not participate in the current `Q`, keep the use-value criterion explicitly outside `Q` as a declared side condition or tie-breaker. A named C.19 lens may consume either declared position but cannot silently promote use-value into `Q` or construct the Q model.

**Scalarization lenses (policy‑level).** A lens `J_ℓ` declares: (a) hard eligibility conditions (e.g., ConstraintFit=pass), (b) soft aggregation (weights or curves), (c) trust policy (how assurance and CL discounts enter).
**Conformance.** A Context MUST name the lens used to pick from a frontier; scalarized rankings MUST NOT be presented as “the frontier”; the **`lens id MUST be recorded in provenance of each selection`**.

**Promotion rules (policy).**
- **Tie‑breaks.**  `Surprise` and `Illumination` MAY act as tie‑breakers; **promotion into the dominance set MUST be declared by lens or policy id** and captured in provenance.
- **Graduation.** Profiles graduate from Explore→Exploit only when eligibility holds and `assuranceResultRef` cites the exact B.3 assurance result whose bounded use supports the profile's declared `backstop_confidence` threshold for the current scope.
- **Sunset or pivot.** Profiles failing VOI or backstop thresholds are sunset or pivoted at `rebalance_period`.

**Policy logic is not generation or work.** One C.19 pass computes and records a treatment over an already identified live pool. It does not recompute a C.18 front or archive, update a generator, seed a candidate, constitute dated `U.Work`, create or classify a local system-role kind, create or change an assignment occurrence or its state, establish responsibility, authority, or permission, approve a budget or plan, or authorize enactment. At enactment, recover only the branches that independently obtain; send unresolved claim-bearing “role” wording through `E.10.ROLE`.

**Pool-policy pass (per `rebalance_period`).**
1) Read the current C.18 archive/front reference and its replay boundary; do not recompute either object inside C.19.
2) Record the governing lens and desired policy values, such as `explore_share`, emitter-profile preference, `wild_bet_quota`, or an admitted heterogeneity constraint. These are policy values, not generation actions.
3) Apply eligibility and `backstop_confidence` to the pool-policy question: record graduation pressure and choose exactly one `currentTreatment` from `widen | keep_frontier | narrow_to_subset | sunset_line`. Record this graduation and treatment judgement under C.19.
4) If that judgement requires fresh candidates, a changed emitter mix or temperature, archive insertion, or front recomputation, set `nextQuestionPatternLocator = C.18` and pass only the desired emitter profile, quota or constraint, and the exact generation/archive/front reason. C.18 decides and records the generation, archive, and front operations.
5) If carrying out the treatment requires dated implementation, planning, staffing, or budget use, pass the policy record to the A.15 family; the policy record itself grants none of them.
6) Emit one `PoolPolicyResult` with `livePool`, `governingLens`, `currentTreatment`, `changeTrigger`, and any inputs required by the next subject pattern. The result may justify keeping, narrowing, graduating, or sunsetting a line without taking over the named next subject pattern's operation.

**Named lenses (heuristics; policy‑level, not norms)**
The following **lens profiles** are **illustrative heuristics**. Contexts MAY reuse or modify them; they are **not** normative.
• **Frontier‑sweeper** — maintain attention on the full front; promote only when `backstop_confidence` holds.
• **Barbell** — enforce `explore_share ≥ θ` with a `wild_bet_quota`; otherwise exploit top‑trust region.
• **Spike‑first** — pick highest **Use‑Value** subject to `ConstraintFit=pass` and a small **Cost‑to‑Probe** cap.
• **Safety‑first** — minimize **SafetyRisk** subject to `Use‑Value ≥ θ` and `ConstraintFit=pass`.
• **Platform‑option** — maximize **Option‑Value** under probe cost bounds.
• **Pilot-then-scale** — optimize **Use-Value** on the declared pilot scope. Set `currentTreatment = widen` only when `assuranceResultRef` cites the exact B.3 assurance result whose supported scope includes the proposed wider pool, and `changeTrigger` names the satisfied assurance condition and that newly supported scope; otherwise keep the pilot scope.
• **Heterogeneity-first (illustrative profile).** Use only when the current Context already admits a heterogeneity constraint or sampler policy. The profile may apply a declared `FamilyCoverage` or `MinInterFamilyDistance` gate, a declared family or subfamily quota, or a diversity-promoting sampler; C.19 supplies no universal `k`, `δ_family`, quota vector, sampler class, DPP rule, or max-min rule. Record only the admitted policy values and ids actually used.
**Conformance (lens recording).** A pool-policy record that uses a lens **MUST** record its **lens id** alongside `emitterPolicyRef`. (This restates and localizes C19-3.)

#### C.19:4.1 - Explicit pool-policy result

**Canonical record vocabulary.** A serialized `PoolPolicyResult` uses the field `governingLens` and exactly one `currentTreatment` token from `widen | keep_frontier | narrow_to_subset | sunset_line`. Reader prose may say *widen*, *keep the frontier*, *narrow to a subset*, or *sunset a line*, but those phrases are labels, not alternate serialized values. Do not use `lens` as a second field name.

A finished `C.19` pass should write one explicit pool-policy record rather than one atmospheric statement that exploration will continue somehow.

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
- `changeTrigger = quota satisfaction plus one explicit novelty floor`

Those fields define the result: live pool, governing lens, current treatment, and change trigger.

#### C.19:4.2 - Closure rule over the live pool

A `C.19` pass may close only when one explicit pool and one explicit next treatment are both visible.

- Close as `widen` when the current frontier is too narrow for the declared exploration policy or when the evidence basis is too thin to justify current narrowing.
- Close as `keep_frontier` when several lines must remain live under the current lens and no narrower admissible subset is yet justified.
- Close as `narrow_to_subset` when one declared lens now justifies retaining one smaller internal live set without pretending that one scalar winner has already been chosen.
- Close as `sunset_line` when one line or family region no longer clears the current lens, quota, or backstop requirements.

When the question has stopped being pool policy, C.19 closes by naming the applicable pattern outside `currentTreatment`. Use `C.11` for local choice, `C.24` for enactment planning, `G.5` for selector-facing result declaration, `E.17` for a source-backed publication face and return to source, `E.24.PUB` for the publication occurrence and audience availability, or `G.11` for refresh. Name another applicable pattern when the recovered relation is different.

One internal retained subset here is still one pool-treatment result. It is not yet one declared `Shortlist` or `RankedShortlist`, and it has no `ShortlistId` merely by being retained. If downstream comparison, registry use, or another selector-facing use needs the set result stated, close the C.19 pass and use `G.5`. If that declared result must then be available to an audience, use `E.17` for its source-backed publication face and return to source and `E.24.PUB` for the publication occurrence and availability.

If the result still cannot say which pool remains live, which lens governs it, and which event would justify changing the treatment, it is still unfinished pool policy rather than one finished `C.19` result.

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

If the record does not already state which pool remains live, what governs it, and what would change that policy treatment next, it is still one unfinished `C.19` result.

#### C.19:4.3a - Worked closure slice

Three short contrasts keep the closure law practical.

**Several family regions remain live.**
When the point is to keep several lines active under one declared lens, `C.19` should not pretend it has already made one local choice:

```text
livePool = frontier_F
governingLens = frontier_sweeper_v3
currentTreatment = keep_frontier
changeTrigger = one retained line reaches backstop_confidence L1
whyNotLocalChoice = three family regions remain live
```

**One region should now be sunset.**
When one region no longer clears the active novelty floor or backstop, `C.19` should say so directly rather than leaving that retirement implicit:

```text
livePool = family_region_beta
governingLens = barbell_policy_v2
currentTreatment = sunset_line
changeTrigger = reopen only if new evidence or quota deficit reactivates the region
whyNotLocalChoice = other regions still remain live under the same pool policy
```

**The pool has already been narrowed and the next question is selector-facing result declaration.**
When one internal retained subset is already explicit and the next question is to declare it for downstream use, `C.19` closes by naming the applicable pattern instead of naming that subset as though it were already one selector result:

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
CulturalLivePoolPolicyResult@Context:
  livePool:
  governingLens:
  currentTreatment:
  changeTrigger:
  termBridgeRefs?:
  culturalEvolutionCaseRef?:
  selectedSetResultRef?:
  refreshRef?:
```

The record states pool treatment only. If the label itself is unstable across communities, use `F.17`, `F.18`, and `F.9`. If the question is the cultural-evolution case, use `C.36`. If the internal retained subset needs a selector-facing result, use `G.5`. If that result already exists and must be available to an audience, use `E.17` for its source-backed publication face and return to source and `E.24.PUB` for the publication occurrence and availability. If the issue is source or edition currentness, use `G.11`.

#### C.19:4.4 - Exit From Pool Treatment To Result Declaration, Publication, Or Choice

An internal subset retained by `narrow_to_subset` is still the live pool named by one C.19 policy record. It is not a public `Shortlist`, `RankedShortlist`, or `ShortlistId`-bearing selector artefact, and C.19 does not emit any of those objects. `Front` and `Archive` retain their C.18 meanings; a scalarized pick does not rename either one.

When the retained set must be declared for downstream comparison, registry use, or another selector-facing use, close C.19 and pass `G.5` the exact declared source set, lens or policy id, eligibility conditions, dominance set, tie-breakers, promotion policy, and provenance pins. Use `G.5` to declare the selected-set result and any stable public shortlist identity required by a named use. The C.19 record supplies only the preceding pool treatment and the reason result declaration is now current. If actual audience availability is also current, use `E.17` for a source-backed publication face and return to source and `E.24.PUB` for the publication occurrence and availability.

When the live question becomes which option to choose, close C.19 and pass the fixed option set and comparison basis to `C.11`; a C.19 subset is not a `ChoiceResult`. When the question becomes enactment or performed work, use `C.24` and the A.15 family. Resource bounds, `CostToProbe`, `ValueOfInformation`, `ValueOfComputation`, `explore_share`, and `backstop_confidence` may explain a pool treatment, but they establish no budget, plan, Work occurrence, local system-role kind, separate System-classification judgment, assignment occurrence or state, responsibility, authority, permission, or enactment. Recover each needed fact independently, and send unresolved claim-bearing “role” wording through `E.10.ROLE`. When edition, source, descriptor, policy, or evidence currentness becomes the live question, use `G.11`; a change trigger in C.19 does not itself perform refresh or create a refreshed edition.

The practical handoff is therefore small: preserve the exact C.18 archive or front reference, the C.19 live-pool treatment and change trigger, and the evidence needed by the named next pattern. Do not duplicate selector-result declaration, publication availability, choice, work, or refresh semantics inside C.19.

