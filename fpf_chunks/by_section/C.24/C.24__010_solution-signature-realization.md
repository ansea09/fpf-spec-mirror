---
chunk_kind: "child"
pattern_id: "C.24"
pattern_title: "Agentic Tool-Use and Call Planning (C.Agent-Tools-CAL)"
section_id: "C.24:4"
section_title: "Solution — Signature & Realization"
source_path: "FPF-Spec.md"
output_path: "by_section/C.24/C.24__010_solution-signature-realization.md"
commit_sha: "e3fedf42dc7cb5d12905913b5a0b0e951ed7d254"
heading_path:
  - "C.24 — Agentic Tool-Use and Call Planning (C.Agent-Tools-CAL)"
  - "C.24:4 — Solution — Signature & Realization"
line_start: 44843
line_end: 45054
dependencies:
  - "A.1"
  - "A.15"
  - "B.3"
  - "C.11"
  - "C.18"
  - "C.19"
  - "C.24"
  - "C.28"
  - "C.5"
  - "E.23"
  - "E.3"
  - "E.5"
  - "G.5"
  - "G.6"
  - "G.9"
  - "U.PromiseContent"
  - "U.WorkPlan"
keywords:
---

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

When the choice posture is already fixed enough that enactment planning is admissible under `C.24`, but the route across heterogeneous or unfamiliar callable approaches is still uncertain, the system may spend a bounded scout/probe budget before committed rollout and return one checkpoint package that compares the tested routes.

If additional probing could still change which option survives the current `OptionSet`, the budget is still `C.11`-side epistemic budget and the question reroutes upstream. If choice posture is already fixed and the uncertainty is only about route or rollout shape, the budget is now enactment budget and the checkpoint belongs in `C.24`.

That `CheckpointReturn` should state the declared utility objective and current `TaskFamily`, the route descriptions or candidate approaches tested, the evidence on each route, the burned and residual actual budget, the recommended next action, and the exact commit trigger that would justify leaving probe state.

A successful probe does not by itself justify a larger burn or a committed rollout. `C.24` carries the `CheckpointReturn` record and call-plan semantics for this probe loop; `A.15` carries the DesignRunTag split and `E.16` carries the budget partition plus guard and ledger enforcement. Low-human-overlap approaches remain sound only while they stay tied to the declared utility objective, budget boundaries, and evidence locus explicitly.

**Bridge to neighboring patterns.** `ProbeBudget` belongs to `C.11` while it means epistemic budget for further probing before choice. `C.24` carries budgets once they are enactment, tool-call, or rollout budgets. If the question is still which option survives now, apply `C.11`; if it is now pool policy over several still-live candidate lines, apply `C.19`; if it is selector-facing publication of the selected result, apply `G.5`.

**Explicit enactment result.** A conformant `C.24` pass should therefore leave either one enactment-facing `CallPlan` that states the current objective, the cited route descriptions or planned call order, the planned budget envelope, the stop or replan condition, and the next move, or one `CheckpointReturn` that states the current objective or task family, the burned and residual actual budget, the evidence locus, the commit trigger, and the recommended next action.

**Unfinished-state rule.** A `C.24` result remains unfinished when it cannot say whether execution should continue now, pause at one checkpoint, or reroute, when it confuses route description with plan or plan with executed work, or when it does not state which budget is planned versus already burned and what event would stop or replan the current route.

**Normative Laws (ATC-Laws).**

* **ATC-1 (Model-the-Call, not the App).** A tool call is one **Work** instance that enacts a referenced **MethodDescription** promised by a **Service**; plans schedule intended calls and cite route descriptions but are neither the route descriptions themselves nor the calls. (A.15.)
* **ATC-2 (Bitter-Lesson Preference).** When two admissible choices are within **delta (assurance)** and **alpha (budget)**, **prefer the more general, scale-benefiting method** whose **slope vector Pareto-dominates** under the declared E/E-LOG objectives; any override **MUST** record a **BLP-waiver** with expiry. (E.2; precedence governed by E.3.)
* **ATC-3 (Budget & Harm Gates).** Plans **SHALL** declare ceilings on compute, cost, wall-time, and risk; execution **MUST** abort or replan on breach. Actual burned or residual budget belongs in `CheckpointReturn`, `CallGraph`, or other work-side reporting, not inside the `CallPlan` field set.
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

- Planning should reuse the declared source set, decision lens, probe budget, and stopping posture rather than creating one planning-only choice semantics.
- Budgeted sequencing may mix exploitation and exploration, but the declared source set and the declared reason for the next probe must stay recoverable.
- Use planning language such as `probe next`, `hold as archive`, `apply G.5 for shortlist publication`, or `stop for now` only when the relevant lens-side reason is stated directly.
- `explore_share`, `backstop_confidence`, probe budgets, and replan triggers are planning harmonization terms for that same declared choice doctrine.
- They may regulate sequence and stopping; they do not redefine `Front`, `Archive`, `Shortlist`, or `SelectionSlot`.
- If the next planned move is one public `Shortlist` or `RankedShortlist`, `C.24` should name that as a neighbouring-pattern exit to `G.5`, not emit the selector artifact itself.

#### C.24:4.2 - Policy profile and BLP precedence

**ATC-Policy fields (conceptual).**
`{ backstop_confidence, explore_share, risk_bound, cost_ceiling, time_ceiling, tie_breakers, novelty_quota?, wild_bet_quota?, stop_conditions, BLP_delta_alpha, BLP_delta_delta }` - realised by referencing an `E/E-LOG` `EmitterPolicy` and adding Bitter-Lesson-Preference clauses. Defaults inherit from `C.19`; any deviation is editioned.

**BLP precedence.** In conflicts with tactics that hard-code narrow scripts, the Bitter-Lesson Preference applies subject to `E.3/E.5` precedence. Where scripts encode safety-critical gating or regulatory compliance, scripts prevail unless the governing context publishes the override rationale, expiry, measured hazard avoided, and planned re-evaluation window.

#### C.24:4.3 - Didactic quick card

**Agentic Call Plan (public field set).**
`Objective - Context(K) - RouteRefsInOrder[edition-pinned] - BudgetEnvelope{time_budget, compute_budget, cost_budget, risk_limit} - PolicyRef - Explore-share - StopConditions - ReplanConditions - BLP tolerances - BLP waiver (if any) - Assurance<F,G,R|K,S> - Provenance ids`

#### C.24:4.4 - Explicit enactment outputs and closure rule

A finished `C.24` pass should publish one enactment result rather than one vague statement that the system now has a plan.

Two output shapes are admissible here:

- one enactment-facing `CallPlan`; or
- one bounded `CheckpointReturn` when probing is still the admissible next move inside enactment planning.

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

Close as one enactment-facing `CallPlan` when the choice posture is already fixed enough that execution order, gating, and replanning are now the call-planning question. Close as one `CheckpointReturn` when bounded scout/probe work is still admissible inside enactment planning. Return to the neighbouring pattern when the result has actually fallen back into local choice, pool policy, or selector-facing publication.

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

**Unfamiliar route, one bounded scout pass still admissible.**
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

The practical distinction is simple: if route order and budgeted execution are already the call-planning question, emit one `CallPlan`; if bounded scout work is still the call-planning question inside planning, emit one `CheckpointReturn`.

1. **Research-assistance system in agential role.**
   Task: answer a novel technical question. Candidate tools: retrieval, structured web search, code runner, table or plot generator.
   **Plan:** cite route descriptions for `search`, `retrieve`, `synthesize`, and `code_check`; declare `explore_share approx 0.4`; replan on sentinel `low_R`.
   The admissible structure here is one declared budget envelope, one explicit route order, and one visible replan trigger.

2. **Program-repair system in agential role.**
   Task: propose a patch against a failing test suite. Candidate tools: repo introspection, static analyzer, unit runner.
   **Plan:** keep repo-introspection, patch-application, and targeted-test route descriptions distinct; use scout quota across patch families before committed rollout.

3. **Lab-automation system in agential role.**
   Task: adjust a wet-lab protocol under drift. Candidate tools: planner, pipetting controller, spectrometer, Bayesian optimizer.
   **Plan:** a bounded probe or pilot can inform the route, but committed rollout waits for the declared commit trigger and assurance floor.

