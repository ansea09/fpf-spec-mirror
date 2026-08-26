---
chunk_kind: "child"
pattern_id: "C.24"
pattern_title: "Agentic Tool-Use and Call Planning (C.Agent-Tools-CAL)"
section_id: "C.24:4"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/C.24/C.24__010_solution.md"
commit_sha: "c7ac61bbaa8d3c10165b1a5a4a350956c87d77c9"
heading_path:
  - "C.24 — Agentic Tool-Use and Call Planning (C.Agent-Tools-CAL)"
  - "C.24:4 — Solution"
line_start: 51730
line_end: 51899
dependencies:
  - "A.10"
  - "A.15"
  - "A.15.1"
  - "A.15.2"
  - "A.15.7"
  - "B.1.6"
  - "B.3"
  - "C.11"
  - "C.16"
  - "C.18"
  - "C.19"
  - "C.19.1"
  - "C.2.1"
  - "C.28"
  - "C.5"
  - "E.17"
  - "E.23"
  - "E.24.PUB"
  - "G.5"
  - "G.6"
  - "G.9"
  - "U.PromiseContent"
keywords:
---

### C.24:4 - Solution

#### C.24:4.0 - Local objects and boundaries

- `ATC.CallRouteDescription` is a `U.MethodDescription` for one callable route. When it carries vendor-local route data, it states the vendor or source scheme, exact scheme or API edition, intended use, and selected Method ref before any access details, inputs, outputs, or route limits. It is not the Method or anything executed.
- `ATC.CallPlan` is a `U.WorkPlan` for intended calls. Its steps select Methods and may cite route descriptions.
- `ATC.CheckpointReturn` is a C.2.1 result episteme stating what was tested, what budget was burned, and what route action is recommended next. It is not the tested Work.
- `ATC.CallGraphRef` cites the applicable `G.6` trace representation over actual call Work. The representation records or points to facts; it creates none of them.

`decisionBasis` contains exactly one of two references. `situationResponsiveDecisionEpistemeRef` refers to an episteme identified under C.2.1 because this plan relies on an A.15.7 decision; the episteme states the selected action, deciding System, intended performer, action-changing fact, relevant Method limit, and stop or feedback condition. `fixedOptionChoiceResultRef` refers to a C.11 `ChoiceResult` whose result is `choose now`. The first is not a `ChoiceResult`, and the second does not become a situation-responsive decision by being consumed here.

There is no catch-all `ATC.PolicyRef`. When a constraint branch is current, cite its actual object: C.19 `PoolPolicyResult` or `EmitterPolicy`, a C.19.1 probe, comparison, local-policy, or waiver result, or a domain constraint whose kind and defining pattern are named. Time, compute, cost, risk, stop, and replan ceilings remain fields of this plan.

State the distinction among Method, route description, plan, and Work here and apply it throughout. Repeat a qualifier only when it changes identity, action, stop, or reliance at that locus.

#### C.24:4.1 - Owned planning operations

C.24 owns only planning and replanning:

```text
planCalls(
  decisionBasis,
  objective,
  admittedMethodRefs,
  routeDescriptionRefs?,
  budget
) -> CallPlan

revisePlan(
  currentCallPlanRef,
  checkpointOrSignalRefs,
  residualBudget
) -> CallPlan | CheckpointReturn | neighborExit
```

`A.3.1` supplies Method admission. The decision basis fixes the action or option being planned; it does not admit the Methods chosen for plan steps. An A.15.7 basis keeps the selected action, deciding System, intended performer, action-changing fact, relevant domain-Method limit, and stop or feedback condition. A C.11 basis is a `ChoiceResult` whose lawful result is `choose now`; `probe again`, `reject current set`, and `reroute` do not fix an action for C.24. C.18 may supply generated candidate or front material, and C.19 may supply a live-pool treatment that informed the decision; neither record admits a Method. Comparison comes from the selected evaluation Method and, when scale preference is claimed, `C.19.1`. Actual execution, observations, and provenance rows come from dated Work and `G.6`. C.24 only constrains what the plan or checkpoint must retain for those later uses.


#### C.24:4.2 - Bounded scout or probe cycle

When the accepted decision basis permits enactment planning but the usable route is still unfamiliar, the admitted System may perform a bounded scout pass and return a `CheckpointReturn`.

If another probe could still change which option survives the `OptionSet`, the budget remains a C.11 probe budget and planning returns there. If changed live facts or domain-Method limits could change an A.15.7 action, return there instead. If the action or option remains fixed and only route shape or rollout order is uncertain, the probe uses enactment budget and its checkpoint belongs here.

A successful probe is not a commitment. Commitment needs the named `commitTrigger`, enough residual budget, and any separately required safety or assurance condition.

#### C.24:4.3 - Planning laws

**ATC-1 — Plan the call, not the app.** A plan step selects a Method. A route description, endpoint, service promise, trace row, or response does not become that Method or an actual call.

**ATC-2 — Use the actual C.19.1 branch.** Start with C.19.1's scale-claim probe. Consume its actual first result: `no scale claim yet`, `local analogy or policy`, `bounded scale comparison`, or `full Scale-Audit selected`. Only the latter two open comparison or audit work. A completed comparison may then warrant a bounded preference or `no scale-based preference`. Keep a `BLP-waiver` separate: it is used only when a declared generality preference would otherwise decide the use, and it records rationale, the admitted review System, the direct waiver-review responsibility or missing governor, and expiry or review. If comparable evidence is absent, stop the empirical preference; do not invent a slope vector or treat a waiver as evidence.

**ATC-3 — Make budgets and harm limits visible.** A `CallPlan` states its planned ceilings. A `CheckpointReturn` or Work-side record states actual burn. The admitted System stops or replans when a named ceiling or safety condition is breached.

**ATC-4 — Keep live-pool exploration declared.** Cite a C.19 `PoolPolicyResult` only while treatment of that still-live pool constrains this plan. Cite its exact `EmitterPolicy` only when the plan actually uses that profile; then record `explore_share`, including `0` when the current profile explicitly plans none. Do not fabricate either ref after the fixed action or option has made pool treatment irrelevant, and do not silently turn illumination or novelty telemetry into a decision criterion.

**ATC-5 — Preserve replay after execution.** Each actual call is recovered as dated Work with its performer, enacted Method, interval, containing system when material, plan ref, actual budget delta, inputs and outputs subject to privacy, and any route-description edition used. Cite the applicable G.6 trace representation. The plan and trace do not establish these facts by themselves.

**ATC-6 — Add assurance only for a named use.** When a planning or rollout decision depends on assurance, name the target claim and use, then cite the B.3 result with its basis, disposition, limits, and reopen condition. No policy label or confidence level substitutes for that result.

**ATC-7 — Bind vendor routes to the selected Method.** Vendor-specific tokens belong in an edition-pinned `ATC.CallRouteDescription` that recovers the vendor or source scheme, exact scheme or API edition, intended use, and selected Method ref. Access details, inputs, outputs, and limits may follow. An arbitrary profile, executable adapter, or F.9 Bridge does not satisfy this binding. When executable adaptation is current, identify the Method, MethodDescription, System, and performed Work through their direct patterns. Cite an F.9 Bridge only when its relation independently obtains between two local meanings.

#### C.24:4.4 - Policy and comparison branches

Add only the branch that still constrains this plan:

```text
CallPlan optional branch fields:
  poolPolicyResultRef?             # C.19; only while live-pool treatment still matters
  emitterPolicyRef?                # C.19; only when this exact versioned profile is used
  scaleClaimProbeResultRef?        # C.19.1 first result
  scaleComparisonResultRef?        # only when the probe selected a bounded comparison
  scaleAuditResultRef?             # only when the probe selected a full Scale-Audit
  blpLocalPolicyRef?               # C.19.1 local policy or analogy, not empirical evidence
  blpWaiverRef?                    # separate from the comparison result
  explore_share?                   # only with the applicable C.19 branch
  risk_bound
  cost_ceiling
  time_ceiling
  stop_conditions
  tie_breakers?
  comparison_tolerances?
  assuranceResultRef?              # only for a named assurance use
```

Each comparison tolerance names its characteristic, bearer, scale, evidence basis, and window. Graduation, rollout, or widening uses a concrete condition defined by the cited result or direct domain pattern. Plan-local ceilings and stop conditions need no policy object. If another domain constraint is current, give its field the actual result-kind name and cite its defining pattern; do not put it in a catch-all constraint ref. When a condition relies on assurance, cite the exact B.3 result and its supported scope; no universal assurance level is inherited from C.19.

#### C.24:4.5 - Causal action-use field

Add the causal field only when the planned calls are intended to observe, intervene, collect counterfactual-rung evidence, simulate for a causal claim, condition a counterfactual policy, or evaluate a policy causally:

```text
CallPlan.causalActionUseSpec?:
  causalUseQuestionRef: CausalUseQuestionRef
  targetCausalityLadderRung: CausalityLadderRung
  causalUseClaimKind: CausalUseClaimKind
  causalActionPolicyClass?: CausalActionPolicyClass
  causalEvidenceDesignRef?
  causalSupportComponentRefs?
  causalUseSupportResultRef?: CausalUseSupportResultRef
  supportedUse
  unsupportedUse
```

The field states the planned causal use and any support already consumed. It does not estimate an effect, prove identification, certify fairness, or turn simulation output into realized counterfactual evidence. Use `C.28` for those support questions.

#### C.24:4.6 - Public quick card

Record:

- exactly one decision-basis reference—an A.15.7 decision episteme or a C.11 `choose now` `ChoiceResult`—plus the objective and ordered Method refs;
- route-description refs only when needed, with their source scheme, exact edition, intended use, and selected Method binding;
- dependencies or safe parallelism only when they change the route;
- time, compute, cost, and risk budgets plus stop and replan conditions;
- next planned action; and
- an exact C.19 or C.19.1 result, B.3 assurance result, causal-use result, provenance ref, or named domain-constraint result only when that branch is current.

This is enough for an ordinary plan. Do not fill the heavier branches merely to make the record look complete.

#### C.24:4.7 - Closure and worked cases

Close as a `CallPlan` when route order and budgeted enactment are the current question. Close as a `CheckpointReturn` when one bounded route probe remains justified. Return to A.15.7 or C.11 when the corresponding decision basis reopens; return to the applicable neighboring pattern when pool treatment, selector declaration, readiness, execution, or publication becomes the current question.

**A.15.7 decision into a known route.**

During ongoing repository-repair Work, changed source facts make `produce_patch_and_verify` the next action under the current repair Method. Using the steering Method in A.15.7, the responsible maintainer makes that decision. The retained decision names the repair agent as intended performer, the changed-source fact, and test failure as the stop and feedback condition. Because the call plan relies on the decision later, the team retains it in one episteme identified under C.2.1. The episteme describes the situation-responsive decision; it is not a C.11 `ChoiceResult`.

```text
CallPlan:
  decisionBasis:
    situationResponsiveDecisionEpistemeRef = patch_action_decision_17
  objective = produce_patch_and_verify
  plannedCallsInOrder =
    - methodRef = InspectRepositoryMethod_4
      methodDescriptionRef = inspect_repo_route_v3
    - methodRef = EditCandidateMethod_2
      methodDescriptionRef = edit_candidate_route_v2
    - methodRef = TargetedTestMethod_7
      methodDescriptionRef = targeted_tests_route_v5
  plannedBudgetEnvelope = {time<=45_minutes, compute<=x2, cost<=y2, risk<=r2}
  stopOrReplan = targeted_tests_fail_twice
  nextPlannedAction = enact_now
```

The plan claims no call occurred. If the first call is performed, recover its dated Work, performer, assignment where current, Method, interval, plan ref, and trace representation through the direct patterns.


**Unfamiliar route.**

```text
CheckpointReturn:
  decisionBasis:
    fixedOptionChoiceResultRef = ci_route_choice_09
  objectiveOrTaskFamily = unfamiliar_ci_failure
  testedMethodRefs = [LogTraceMethod_2, MinimalReproductionMethod_5]
  evidenceRefs = [trace_result_1, reproduction_result_1]
  burnedBudget = 1_probe_cycle
  residualBudget = 2_probe_cycles
  recommendedNextAction = run_minimal_reproduction_once_more
  commitTrigger = reproduction_is_stable_and_required_evidence_is_current
```

**Two vendor routes with one token.** Vendor A and Vendor B both publish a route called `search`. `vendor_a_search_v2` states scheme `VendorA API`, edition `2026-07`, intended use `repository text search`, and selected Method `RepositoryTextSearchMethod_3`. `vendor_b_search_v5` states scheme `VendorB agent tools`, edition `2026-08`, intended use `web source retrieval`, and selected Method `WebSourceRetrievalMethod_8`. The shared token identifies neither binding; the description fields do. An executable adapter, if used, remains a separate Method, and its execution remains separate Work.

**Scale comparison, when current.** The cheap C.19.1 probe for `BatchSearchMethod_3` and `IndexedSearchMethod_6` returns `bounded scale comparison` for the same repository-search task and `10k–100k files` window. The comparison then uses elapsed time and missed-match rate from `repo_search_benchmark_12`, including uncertainty and cost limits, and warrants a preference for `IndexedSearchMethod_6` only inside that window. If one Method is evidenced only on small text files and the other only on large mixed repositories, the comparison returns `no scale-based preference`. A project may separately cite a local policy or `BLP-waiver`; neither changes the empirical result.

**Near misses.** A route label with no recovered Method remains probe material. A plan with no Work is still intent. A trace row does not prove performer, assignment, Method, or service acceptance. A successful probe without a commit trigger is not rollout.

**Transfer examples.** The same result shape works for research assistance, program repair, and lab automation. The Methods and safety conditions differ; the plan/checkpoint boundary does not.

