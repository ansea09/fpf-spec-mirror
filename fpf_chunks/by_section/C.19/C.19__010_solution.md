---
chunk_kind: "child"
pattern_id: "C.19"
pattern_title: "Explore-Exploit Live-Pool Governor"
section_id: "C.19:4"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/C.19/C.19__010_solution.md"
commit_sha: "504747d26299e3963dc0457bf48d4e2a791d926a"
heading_path:
  - "C.19 — Explore-Exploit Live-Pool Governor"
  - "C.19:4 — Solution"
line_start: 49000
line_end: 49244
dependencies:
  - "A.19.CPM"
  - "A.19.SelectorMechanism"
  - "B.3"
  - "C.11"
  - "C.16"
  - "C.17"
  - "C.18"
  - "C.24"
  - "C.28"
  - "C.32"
  - "C.32.P2S"
  - "C.35"
  - "G.11"
  - "G.5"
  - "G.9"
keywords:
  - "DecisionSubject clarification"
  - "EmitterPolicy"
  - "InsertionPolicy"
  - "dominance default routing"
  - "explore-exploit"
  - "keep frontier"
  - "lens id"
  - "live candidate pool"
  - "narrow to subset"
  - "pool-policy result"
  - "reroute"
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

**Decision-subject clarification.** Later choices are attributed to one declared `DecisionSubject` at explicit `DecisionSubjectGranularity`. **Contexts publish** measurement spaces and admissible policies as **semantic frames**; LOG profiles lenses and policies but does **not** enact choices.
**Depends on.** **C.18** for archive and front stewardship, **C.16** for characteristic and measurement claims, **A.19.CPM** and **A.19.SelectorMechanism** for comparison and selection kernels, **B.3** for assurance-sensitive confidence claims, and **G.5** and **G.11** for selected-set publication and refresh.

**EmitterPolicy (named profile).** A context‑local, versioned policy with fields:
`{ name, regimeKey ∈ {UCB, Thompson, BO‑EI, GP‑UCB, PES, InformationGain, …}, params, explore_share∈[0,1], temperature τ≥0, rebalance_period, wild_bet_quota≥0, backstop_confidence (assurance level), epsilon_dominance ε, cell_capacity K, **insertion_policy**, **dedup_threshold** }`.
Policies are referenced by C.18 generation and archive records and are conceptual lenses, not staffing or budget instructions.
Ordinary default tokens remain governed by `G.Core` and `G.5`; `C.19` explains their pool-policy consequences but does not become one rival default authority.

**Decision-theory bridge.** `C.11` governs theory-side choice among already-available options and the meaning of `ProbeBudget`, `ValueOfInformation`, and `ValueOfComputation`. `C.19` may consume such outputs only as criteria for pool policy, graduation, keep-frontier, or sunset treatment; it does not re-govern local choice doctrine.

**Ordinary default references (if policy is unspecified):**
• **Dominance:** consume `DefaultId.DominanceRegime` from `G.Core` and `G.5`; in ordinary Q-front use this means `{Q components}` with `ConstraintFit=pass` as **eligibility gate**.
• **Tie‑breakers:** `Novelty@context`, `ΔDiversity_P`, `Surprise`; `Illumination` (telemetry over Diversity_P, including coverage and QD‑score) MAY be used as a tie‑breaker but is **not** in the dominance set.
• **Archive:** `K=1`, `ε=0`, deduplication in `CharacteristicSpace`.
• **Policy family:** one uncertainty-aware explore policy family with one declared regime key and explicit change triggers; `UCB`-class with moderate temperature and `explore_share ≈ 0.3–0.5` is one didactic starter profile, not the semantic default family.
• **Provenance (minimum):** record `DescriptorMapRef.edition`, `DistanceDefRef.edition`, `DHCMethodRef.edition`, `EmitterPolicyRef`, `InsertionPolicyRef`, `dedup_threshold?`, `TimeWindow`, `Seeds`.

**Scalarization lenses (policy‑level).** A lens `J_ℓ` declares: (a) hard eligibility conditions (e.g., ConstraintFit=pass), (b) soft aggregation (weights or curves), (c) trust policy (how assurance and CL discounts enter).
**Conformance.** A Context MUST name the lens used to pick from a frontier; scalarized rankings MUST NOT be presented as “the frontier”; the **`lens id MUST be recorded in provenance of each selection`**.

**Promotion rules (policy).**
- **Tie‑breaks.**  `Surprise` and `Illumination` MAY act as tie‑breakers; **promotion into the dominance set MUST be declared by lens or policy id** and captured in provenance.
- **Graduation.** Profiles graduate from Explore→Exploit when **backstop_confidence** (B.3 level) and eligibility conditions are met.
- **Sunset or pivot.** Profiles failing VOI or backstop thresholds are sunset or pivoted at `rebalance_period`.

**Explore and exploit loop (per rebalance_period).**
1) Recompute frontier with trust discounts.
2) Enforce `explore_share` (minimum attention on high‑Novelty, not‑yet‑proven profiles).
3) Update generator `temperature τ` and emitter mix.
4) Apply `backstop_confidence` to graduate; sunset stale probes.
5) Satisfy `wild_bet_quota` by seeding fresh high‑Novelty candidates.
6) HET‑FIRST — apply group‑fairness quotas by domain family when the fairness constraint is current; apply a DPP sampler policy or Max-min repulsion policy when diversity sampling is current; when both constraints are current, record both policy ids before exploit lenses.

**Named lenses (heuristics; policy‑level, not norms)**
The following **lens profiles** are **illustrative heuristics**. Contexts MAY reuse or modify them; they are **not** normative.
• **Frontier‑sweeper** — maintain attention on the full front; promote only when `backstop_confidence` holds.
• **Barbell** — enforce `explore_share ≥ θ` with a `wild_bet_quota`; otherwise exploit top‑trust region.
• **Spike‑first** — pick highest **Use‑Value** subject to `ConstraintFit=pass` and a small **Cost‑to‑Probe** cap.
• **Safety‑first** — minimize **SafetyRisk** subject to `Use‑Value ≥ θ` and `ConstraintFit=pass`.
• **Platform‑option** — maximize **Option‑Value** under probe cost bounds.
• **Pilot‑then‑scale** — optimize **Use‑Value** on pilot scope with `BackstopConfidence ≥ L1`; widen `G` once **R** holds.
• **Heterogeneity‑first (policy id).** Eligibility → Dominance → Tie‑breakers; Hard gate: FamilyCoverage ≥ k, MinInterFamilyDistance ≥ δ_family; Fairness quotas: ≤1 candidate per sub‑family at pre‑front sampling; a DPP sampler policy or Max-min repulsion policy may be used only when its sampler policy id is recorded.
**Conformance (lens recording).** A decision that uses any lens **MUST** record its **lens id** alongside `EmitterPolicyRef`. (This restates and localizes C19-3.)

#### C.19:4.1 - Explicit pool-policy result

A finished `C.19` pass should publish one explicit pool-policy result rather than one atmospheric statement that exploration will continue somehow.

That result should state:

- the still-live pool, frontier, or family scope under governance now;
- the governing lens id or policy state;
- the current treatment, chosen from `widen`, `keep frontier`, `narrow to subset`, or `sunset line`;
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
- Close as `keep frontier` when several lines must remain live under the current lens and no narrower admissible subset is yet justified.
- Close as `narrow to subset` when one declared lens now justifies retaining one smaller internal live set without pretending that one scalar winner has already been chosen.
- Close as `sunset line` when one line or family region no longer clears the current lens, quota, or backstop requirements.

When the question has stopped being pool policy, C.19 closes by naming the next governing pattern outside `currentTreatment`: `C.11` for local choice, `C.24` for enactment planning, `G.5` for selector-facing publication, `G.11` for refresh, or another direct governing pattern when the recovered relation is different.

One internal retained subset here is still one pool-treatment result. It is not yet one public `Shortlist`, `RankedShortlist`, or `ShortlistId`-bearing selector artifact. If the retained subset must be published for downstream comparison, selector-facing publication, or registry-facing consumption, `C.19` closes only by using `G.5`.

If the result still cannot say which pool remains live, which lens governs it, and which event would justify changing the treatment, it is still unfinished pool policy rather than one finished `C.19` result.

#### C.19:4.3 - Minimal pool-policy record

The smallest useful `C.19` record usually states:

- `livePool = ...`
- `governingLens = ...`
- `currentTreatment = widen | keep frontier | narrow to subset | sunset line`
- `changeTrigger = ...`
- `nextGoverningPatternRef? = ...` only when the question is no longer pool policy
- `learningProgressSignal? = ...` when an autotelic or capability-discovery reason materially supports widening, keeping the frontier live, or probing one goal region further
- `competenceModelRef? = ...` when the pool policy depends on a model of what the system or method family can learn next
- `goalSpaceExpansionCue? = ...` when the admissible next treatment widens the goal and task palette rather than merely re-ranking current candidates
- `goalSpaceExpansionPolicyRef? = ...` when goal and task space growth is itself governed by one declared archive or curriculum expansion policy
- `whyNotLocalChoice = ...` when the result might otherwise be mistaken for `C.11`

An admissible short record may therefore read:

```text
livePool = frontier_F
lens = barbell_policy_v2
currentTreatment = keep_frontier
changeTrigger = backstop_confidence reaches L1 for one retained line
whyNotLocalChoice = several family regions remain live
```

When `currentTreatment = narrow_to_subset`, `livePool` still names one internal retained subset or one live pool subset. It does not yet mint one public `Shortlist`, one public `RankedShortlist`, or one `ShortlistId`. If selector-facing publication is now required, the admissible `C.19` record leaves `currentTreatment` as the last pool treatment and fills `nextGoverningPatternRef = G.5`, with the reason that publication rather than pool policy is now current.

Goal and task space growth is one pool-policy doctrine over the archive or curriculum side. When autotelic or capability-discovery pressure is active, cite one `GoalSpaceExpansionPolicyRef` together with the supporting `LearningProgressSignal`, `CompetenceModelRef`, or `GoalSpaceExpansionCue`; that doctrine may justify `widen`, `keep frontier`, or one further probe decision value, but it does not become default `Q`, does not rename the front, and does not publish one selector-facing shortlist without `G.5`.

If the record does not already state which pool remains live, what governs it, and what would change that policy treatment next, it is still one unfinished `C.19` result.

#### C.19:4.3a - Worked closure slice

Three short contrasts keep the closure law practical.

**Several family regions remain live.**
When the point is to keep several lines active under one declared lens, `C.19` should not pretend it has already made one local choice:

```text
livePool = frontier_F
lens = frontier_sweeper_v3
currentTreatment = keep_frontier
changeTrigger = one retained line reaches backstop_confidence L1
whyNotLocalChoice = three family regions remain live
```

**One region should now be sunset.**
When one region no longer clears the active novelty floor or backstop, `C.19` should say so directly rather than leaving that retirement implicit:

```text
livePool = family_region_beta
lens = barbell_policy_v2
currentTreatment = sunset_line
changeTrigger = reopen only if new evidence or quota deficit reactivates the region
whyNotLocalChoice = other regions still remain live under the same pool policy
```

**The pool has already been narrowed and the next question is selector-facing publication.**
When one internal retained subset is already explicit and the next question is to publish it for downstream use, `C.19` closes by naming the governing pattern instead of naming that subset as though it were already one public shortlist artifact:

```text
livePool = retained_subset_{option_B, option_C}
lens = pool_policy_completed
currentTreatment = narrow_to_subset
changeTrigger = retained subset is explicit; pool policy is complete
nextGoverningPatternRef = G.5 because selector-facing publication is now current
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
  selectedSetPublicationRef?:
  refreshRef?:
```

The record governs pool treatment only. If the label itself is unstable across communities, use `F.17`, `F.18`, and `F.9`. If the question is the cultural-evolution case, use `C.36`. If the internal retained subset must become public, use `G.5`. If the issue is source or edition currentness, use `G.11`.

#### C.19:4.4 - Bounded shortlist from declared source sets



- Treat `Shortlist` as the set emitted by one named lens from one declared source set, not as a synonym for `Front`.
- If the mathematical set object must be named, treat it as the choice set underlying that shortlist rather than as one second public head.
- When the current Context consumes the ordinary default `DefaultId.DominanceRegime`, keep `DominanceSet` equal to the declared current `Q` tuple and cite that consumed default rather than re-governing it here.
- `Novelty@context`, `DeltaDiversity_P`, `Surprise`, and `IlluminationSummary` stay outside default dominance unless one declared `PromotionPolicy` promotes them.
- If `Use-Value` belongs in `Q`, declare it there; do not let it drift between core objective and side note.
- `ExplorationArchive` is the exploration-specific specialization of `Archive`; use `Archive` as the wider family head only when that exploration-specific subtype does not matter.
- Resource bounds govern how much probing, comparison, or retention is warranted, but they do not by themselves redefine the front.
- Decision under budget may draw from the front, from the archive, or from both, but the source set and the decision lens must be explicit.
- The selected-set kernel floor here is:
  - one set-return comes first
  - one named lens acts over that declared return
  - one `Shortlist` is emitted from that lens-declared source set
  - one `ShortlistId` may later name that shortlist when it must be carried as one stable public token
  - one `RankedShortlist` may appear later when the shortlist is explicitly ordered
- `PortfolioMode` may state how the selector operated, but it does not rename the emitted set result.
- When the comparison question becomes load-bearing, the minimum mathematical substrate should stay visible:
  - the compared candidates live in one declared outcome or characteristic space
  - the archive may depend on one declared search, niche, or reachability space
  - the shortlisted result is emitted from one explicit selected-set return rather than from one hidden scalar winner
- When a context-local creativity or novelty characteristic remains outside the declared `Q` tuple, keep that distinction visible rather than treating it as one silent override of the current dominance basis.

#### C.19:4.4.1 - First public wording for shortlisted outputs

- Prefer wording like `shortlist from the declared Q-Front under LensId=...` over wording that makes the shortlisted result sound like one second front.
- When one stable emitted object must be cited across documents or tools, say `ShortlistId for that shortlist` rather than letting the token name replace the shortlist result itself.
- If the shortlist later acquires order, say `RankedShortlist` and keep the prior shortlist result recoverable.
- Reserve `choice set underlying that shortlist` for mathematical discussion, proofs, or object-level set operations.

#### C.19:4.4.2 - Choice doctrine stays source-set explicit

- State the declared source set and the declared decision lens in the same place as the shortlisted-choice rule.
- `CostToProbe`, `ValueOfInformation`, `ValueOfComputation`, `explore_share`, and `backstop_confidence` may appear here when they justify choice from one declared source set.
- Those terms explain why another probe, defer, or stop decision is warranted; they do not rename `Front`, `Archive`, or `Shortlist`.
- When teams need a fuller account of budgeted probing or sequencing, add that as one separate resource-aware choice explanation rather than overloading the shortlist doctrine itself.
- Selector-facing publications should keep speaking about the emitted set and its source set rather than trying to explain the whole budgeted-choice rationale there.

