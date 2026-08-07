---
chunk_kind: "child"
pattern_id: "C.24"
pattern_title: "Agentic Tool-Use and Call Planning (C.Agent-Tools-CAL)"
section_id: "C.24:4"
section_title: "Solution — Signature & Realization"
source_path: "FPF-Spec.md"
output_path: "by_section/C.24/C.24__010_solution-signature-realization.md"
commit_sha: "b7ec5a0b1dfa4bdae4cf055188219e89cef61a63"
heading_path:
  - "C.24 — Agentic Tool-Use and Call Planning (C.Agent-Tools-CAL)"
  - "C.24:4 — Solution — Signature & Realization"
line_start: 52750
line_end: 52974
dependencies:
  - "A.1"
  - "A.10"
  - "A.15"
  - "A.15.1"
  - "A.15.2"
  - "A.15.5"
  - "B.1.6"
  - "B.3"
  - "C.11"
  - "C.16"
  - "C.18"
  - "C.19"
  - "C.24"
  - "C.28"
  - "C.5"
  - "E.10.MOVE"
  - "E.11.PUR"
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

**Local value names.**
*`ATC.CallRouteDescription`* is a `U.MethodDescription` with `accessSpec` for one tool service or callable route. Its exact C.2.1 EntityOfConcern is an independently admitted `U.Method`; the description describes and may help identify, constrain or justify that Method or intended Work for one receiving use but is neither the Method nor anything executed;
*`ATC.CallPlan`* is a `U.WorkPlan` specialised for intended tool-call work. Each planned call step selects one exact `U.Method` by `methodRef` and may separately cite a current `ATC.CallRouteDescription` by `methodDescriptionRef`, plus planned order, budget ceilings, stop or replan triggers, and `nextPlannedAction`;
*`ATC.CallGraph`* is an evidence or provenance graph over a ledger of exact actual `U.Work` call occurrences. A graph entry cites the Work occurrence and exact Method; an optional route-description edition helps interpretation but creates neither occurrence nor `enactsMethod`;
*`ATC.Policy`* references `U.EmitterPolicyRef` (E/E-LOG) and local call gates **including BLP tolerances (alpha, delta)**.

**Roles.**
A **System in AgentialRole** prepares or revises one **CallPlan** whose planned steps select exact Methods and may cite separate **CallRouteDescription** editions. Upon enactment, an admitted performer `U.System` performs each actual call as a dated `U.Work` occurrence under an exact obtaining `U.RoleAssignment`; A.15.1 owns the actual `enactsMethod` relation. **Observers** record observations with acceptance checks. Route descriptions stay design-time epistemes; the call plan stays schedule-of-intent; actual call Work stays run-time; service promise content remains a separate acceptance object. None establishes another by record inclusion.

**Operators (Gamma_agential; CAL, conceptual):**

1. `Gamma_agential.eligible(tool, TaskSignature, K_ctx) -> {true|false, notes}`
   *Eligibility gate* based on capability fit, policy allow-list or deny-list, and context K (including safety constraints).

2. `Gamma_agential.enumerate(TaskSignature, K_ctx) -> CandidateSet<ATC.CallRouteDescription>`
   Returns admissible callable route descriptions. It **MAY** delegate to **NQD-CAL** for heterogeneous route families and **MUST** apply the current **E/E-LOG lens** (objectives & telemetry) to tag candidates. Before a candidate enters an enactment-facing plan, its C.2.1 episteme must resolve under the effective reference scheme and identify the exact independently admitted Method; an unresolved route label remains probe material, not a planned enactment.

3. `Gamma_agential.plan(Objective, CandidateSet, Budget, ATC.Policy) -> ATC.CallPlan`
   Produces one **call plan** whose ordered planned-call steps select exact `U.Method` refs and may separately cite selected route-description epistemes. It declares one planned budget envelope (compute, cost, time, risk), one intended call order, and one stop or replan policy. Internal route logic may remain in the cited descriptions; the plan is a `U.WorkPlan`, not a Method, not a MethodDescription, and not yet Work.

4. `Gamma_agential.execute(ATC.CallPlan) -> {ATC.CallGraph, Observations}`
   Executes with **hard gates** (budget, risk, constraint-fit). Each actual call is independently identified as dated `U.Work`, performed by an admitted System under an exact obtaining assignment and related by actual `enactsMethod` to the planned exact Method under A.15.1. The operator logs provenance suitable for B.3 assurance reporting while keeping plan, description, Work, Method and service promise separate.

5. `Gamma_agential.replan(Signals, ATC.CallPlan, BudgetPrime) -> ATC.CallPlanPrime`
   Triggered by sentinel breaches, assurance drops, or policy events; preserves or explicitly revises the ordered exact Method refs, separately cited route descriptions, editioned policy, effective planning context, and other plan content. Changing a description reference does not silently change either the Method or any actual Work history.

6. `Gamma_agential.score(Route or PlanAlternative) -> <ValueProxies, Cost, Risk, FGR_floor>`
   Computes selection signals **without** illegal scalarisation across mixed scales; **uses Pareto comparison under the C.19 E/E-LOG lens** and leaves final dominance to declared policies.

#### C.24:4.1 - Bounded scout/probe cycle for unfamiliar task families

When the choice result is already fixed enough that enactment planning is admissible under `C.24`, but the route across heterogeneous or unfamiliar callable approaches is still uncertain, the system may spend a bounded scout/probe budget before committed rollout and return one checkpoint package that compares the tested routes.

If additional probing could still change which option survives the current `OptionSet`, the budget is still `C.11`-side epistemic budget and the question reroutes upstream. If choice result is already fixed and the uncertainty is only about route or rollout shape, the budget is now enactment budget and the checkpoint belongs in `C.24`.

That `CheckpointReturn` should state the declared utility objective and current `TaskFamily`, the route descriptions or candidate approaches tested, the evidence on each route, the burned and residual actual budget, the recommended next action, and the commit trigger named by value that would justify leaving probe state.

A successful probe does not by itself justify a larger burn or a committed rollout. `C.24` carries the `CheckpointReturn` record and call-plan semantics for this probe loop; `A.15` carries the DesignRunTag split and `E.16` carries the budget partition plus guard and ledger enforcement. Low-human-overlap approaches remain sound only while they stay tied to the declared utility objective, budget boundaries, and evidence locus explicitly.

**Bridge to neighboring patterns.** `ProbeBudget` belongs to `C.11` while it means epistemic budget for further probing before choice. `C.24` carries budgets once they are enactment, tool-call, or rollout budgets. If the question is still which option survives now, apply `C.11`; if it is now pool policy over several still-live candidate lines, apply `C.19`; if it is selector-facing publication of the selected result, apply `G.5`.

**Explicit enactment result.** A conformant `C.24` pass should therefore leave either one enactment-facing `CallPlan` that states the current objective, each planned exact Method ref and any separate route-description ref, planned call order, planned budget envelope, stop or replan condition, and next planned action, or one `CheckpointReturn` that states the current objective or task family, tested Methods and descriptions when recovered, burned and residual actual budget, evidence locus, commit trigger, and recommended next action.

**Unfinished-state rule.** A `C.24` result remains unfinished when a planned call has only a route label and no recovered exact Method, when it cannot say whether execution should continue now, pause at one checkpoint, or reroute, when it confuses Method with description, description with plan, or plan with executed Work, or when it does not state which budget is planned versus already burned and what event would stop or replan the current route.

**Normative Laws (ATC-Laws).**

* **ATC-1 (Model-the-Call, not the App).** One actual tool call is a dated **Work** occurrence that enacts one exact independently admitted **Method** under A.15.1. A current route description is a separate C.2.1 MethodDescription episteme that describes and may help identify, constrain or justify that Method or intended Work; a Service's `U.PromiseContent` is a separate acceptance object. Plans schedule intended calls but are neither Methods, descriptions, service promises, nor actual calls.
* **ATC-2 (Bitter-Lesson Preference).** When two admissible choices are within **delta (assurance)** and **alpha (budget)**, **prefer the more general, scale-benefiting method** whose **slope vector Pareto-dominates** under the declared E/E-LOG objectives; any override **MUST** record a **BLP-waiver** with expiry. (E.2; precedence governed by E.3.)
* **ATC-3 (Budget & Harm Gates).** Plans **SHALL** declare ceilings on compute, cost, wall-time, and risk; execution **MUST** abort or replan on breach. Actual burned or residual budget belongs in `CheckpointReturn`, `CallGraph`, or other work-side reporting, not inside the `CallPlan` field set.
* **ATC-4 (Explore-Share Discipline).** Plans **MUST** declare `explore_share`; defaults **inherit from E/E-LOG profiles**. **Informative defaults**: `0` for safety-critical or deterministic tasks; `approx 0.2-0.4` for ambiguous tasks with heterogeneous tool families. Promotion of illumination telemetry into dominance **requires explicit policy**.
* **ATC-5 (Provenance & Replay).** Every actual call **MUST** emit a **CallGraph** row with its exact Work ref, exact enacted Method ref, performer System, obtaining assignment, Service id, optional cited MethodDescription edition, inputs and outputs (redacted per privacy), `CallPlan` ref, **EmitterPolicyRef**, actual interval, and budget deltas. The graph records these facts; it creates none of them. (NQD/E/E provenance fields apply when used.)
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

What this does not establish: `C.24` does not estimate effects, prove identification, certify fairness, or turn simulation output into realized counterfactual-rung evidence; it governs admissible call planning and redirects causal-use support to `C.28`.

- Planning should reuse the declared source set, decision lens, probe budget, and stopping condition rather than creating one planning-only choice semantics.
- Budgeted sequencing may mix exploitation and exploration, but the declared source set and the declared reason for the next probe must stay recoverable.
- Use planning language such as `probe next`, `hold as archive`, `apply G.5 for shortlist publication`, or `stop for now` only when the relevant lens-side reason is stated directly.
- `explore_share`, `backstop_confidence`, probe budgets, and replan triggers are planning harmonization terms for that same declared choice doctrine.
- They may regulate sequence and stopping; they do not redefine `Front`, `Archive`, `Shortlist`, or `SelectionSlot`.
- If the next planned output is one public `Shortlist` or `RankedShortlist`, `C.24` should name that as a neighbouring-pattern exit to `G.5`, not emit the selector artifact itself.

#### C.24:4.2 - Policy profile and BLP precedence

**ATC-Policy fields (conceptual).**
`{ backstop_confidence, explore_share, risk_bound, cost_ceiling, time_ceiling, tie_breakers, novelty_quota?, wild_bet_quota?, stop_conditions, BLP_delta_alpha, BLP_delta_delta }` - realised by referencing an `E/E-LOG` `EmitterPolicy` and adding Bitter-Lesson-Preference clauses. Defaults inherit from `C.19`; any deviation is editioned.

**BLP precedence.** In conflicts with tactics that hard-code narrow scripts, the Bitter-Lesson Preference applies subject to `E.3/E.5` precedence. Where scripts encode safety-critical gating or regulatory compliance, scripts prevail unless the governing context publishes the override rationale, expiry, measured hazard avoided, and planned re-evaluation window.

#### C.24:4.3 - Didactic quick card

**Agentic Call Plan (public field set).**
`Objective - Context(K) - PlannedCallsInOrder[{MethodRef, MethodDescriptionRef?[edition-pinned]}] - BudgetEnvelope{time_budget, compute_budget, cost_budget, risk_limit} - PolicyRef - Explore-share - StopConditions - ReplanConditions - BLP tolerances - BLP waiver (if any) - Assurance<F,G,R|K,S> - Provenance ids`

#### C.24:4.4 - Explicit enactment outputs and closure rule

A finished `C.24` pass should publish one enactment result rather than one vague statement that the system now has a plan.

Two output shapes are admissible here:

- one enactment-facing `CallPlan`; or
- one bounded `CheckpointReturn` when probing is still the admissible next action inside enactment planning.

A `CallPlan` should state at least these fields:

- current objective;
- ordered planned-call steps, each with an exact `methodRef` and a separate edition-pinned `methodDescriptionRef` only when the route description is current;
- active policy or planning state;
- planned budget envelope or reserved budget;
- stop or replan condition;
- `nextPlannedAction` if the current plan is accepted now.

A `CheckpointReturn` should state at least these fields:

- current task family or objective;
- candidate exact Methods and their separate route-description epistemes tested so far, when recovered;
- evidence on those routes;
- burned and residual actual budget;
- recommended next action;
- explicit commit trigger.

A compact result may therefore look like:

```text
CallPlan(
  objective = answer_question_Q,
  policyRef = ee_policy_v1,
  plannedCallsInOrder = [
    {methodRef = SearchMethod_3, methodDescriptionRef = search_route_v3},
    {methodRef = RetrievalMethod_1, methodDescriptionRef = retrieve_route_v1},
    {methodRef = SynthesisMethod_2, methodDescriptionRef = synthesize_route_v2},
    {methodRef = CodeCheckMethod_1, methodDescriptionRef = code_check_route_v1}
  ],
  plannedBudgetEnvelope = {time<=60_minutes, compute<=x1, cost<=y1, risk<=r1},
  stopOrReplan = low_R_or_cost_ceiling,
  nextPlannedAction = enact_now
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

Close as one enactment-facing `CallPlan` when the choice result is already fixed enough that execution order, gating, and replanning are now the call-planning question. Close as one `CheckpointReturn` when bounded scout/probe work is still admissible inside enactment planning. Return to the neighbouring pattern when the result has actually fallen back into local choice, pool policy, or selector-facing publication.

If the result still does not state what should execute now, what budget is planned or already burned, and what event stops or replans the route, it is still unfinished `C.24` work.

#### C.24:4.4a - Worked closure slice

Two short contrasts keep the closure law practical.

**Known route, execution should begin now.**
When the objective and route are already fixed enough, `C.24` should close as one enactment-facing call plan:

```text
CallPlan(
  objective = produce_patch_and_verify,
  plannedCallsInOrder = [
    {methodRef = InspectRepositoryMethod_4, methodDescriptionRef = inspect_repo_route_v3},
    {methodRef = EditCandidateMethod_2, methodDescriptionRef = edit_candidate_route_v2},
    {methodRef = TargetedTestMethod_7, methodDescriptionRef = run_targeted_tests_route_v5}
  ],
  plannedBudgetEnvelope = {time<=45_minutes, compute<=x2, cost<=y2, risk<=r2},
  stopOrReplan = targeted_tests_fail_twice,
  nextPlannedAction = enact_now
)
```

The plan does not claim that any call happened. If the first call is then performed, identify `ToolCallWork-903 : U.Work`, admitted performer System `RepoAutomationSystem-2`, obtaining assignment `RepoAutomationInspectorAssignment-2`, actual interval `[10:02Z, 10:04Z]`, containing system `RepairRun-81`, and independently obtaining `enactsMethod(ToolCallWork-903, InspectRepositoryMethod_4)`. Its CallGraph row may cite `inspect_repo_route_v3` as `methodDescriptionRef`; neither that description nor the row is the Work occurrence or the enacted Method. The service's `U.PromiseContent` and any acceptance result remain separate.

**Recognizable near misses.** `inspect_repo_route_v3` with no recovered exact `InspectRepositoryMethod_4` cannot support an enactment-facing plan. A `CallPlan` with no actual Work occurrence is still only intent. A tool log row with no independently grounded Work, performer, assignment and Method is evidence material, not execution. A successful response does not by itself prove the service promise was accepted.

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
   **Plan:** select exact `SearchMethod`, `RetrievalMethod`, `SynthesisMethod`, and `CodeCheckMethod` refs in order; separately cite current route descriptions for `search`, `retrieve`, `synthesize`, and `code_check`; declare `explore_share approx 0.4`; replan on sentinel `low_R`.
   The admissible structure here is one declared budget envelope, one explicit route order, and one visible replan trigger.

2. **Program-repair system in agential role.**
   Task: propose a patch against a failing test suite. Candidate tools: repo introspection, static analyzer, unit runner.
   **Plan:** select exact repo-introspection, patch-application, and targeted-test Methods; keep their optional route-description epistemes distinct; use scout quota across patch families before committed rollout.

3. **Lab-automation system in agential role.**
   Task: adjust a wet-lab protocol under drift. Candidate tools: planner, pipetting controller, spectrometer, Bayesian optimizer.
   **Plan:** a bounded probe or pilot can inform the route, but committed rollout waits for the declared commit trigger and assurance floor.

