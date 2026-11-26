---
chunk_kind: "child"
pattern_id: "C.24"
pattern_title: "Plan Tool or Service Calls for a Fixed Action (C.Agent-Tools-CAL)"
section_id: "C.24:4"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/C.24/C.24__006_solution.md"
commit_sha: "9d38fbfe4ce5b72d8fe05e839cbca0025a5b31cf"
heading_path:
  - "C.24 — Plan Tool or Service Calls for a Fixed Action (C.Agent-Tools-CAL)"
  - "C.24:4 — Solution"
line_start: 68010
line_end: 68260
dependencies:
  - "A.10"
  - "A.15"
  - "A.15.1"
  - "A.15.2"
  - "B.1.6"
  - "B.3"
  - "C.11"
  - "C.16"
  - "C.18"
  - "C.19"
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
  - "agentic tool-use"
  - "call planning"
  - "route probe"
  - "service calls"
---

### C.24:4 - Solution

#### C.24:4.0 - Local objects and boundaries

- `ATC.CallRouteDescription` is a `U.MethodDescription` whose EntityOfConcern is the selected admitted Method and whose claims explain how that Method is carried out through the route, under A.3.2. When it carries vendor-local route data, it states the vendor or source scheme, exact scheme or API edition, intended use, and selected Method ref before any access details, inputs, outputs, or route limits.
- `ATC.CallPlan` is a `U.WorkPlan` for intended calls. Its steps select Methods and may cite route descriptions.
- `ATC.CheckpointReturn` is a C.2.1 result episteme stating what was tested, the budget used, and which route action follows from a prior decision or is recommended to the holder of the outstanding route decision. The probe itself is dated Work.
- `ATC.CallGraphRef` cites the applicable `G.6` trace representation over actual call Work. The representation records or points to facts; it creates none of them.

`actionBasis` identifies the grounds that fix the action in the present conditions. Use the entries the planning decision relies on.

- `commissionedAction` identifies the operative instruction or commitment, what it requires of the performer, and when the recipient can count the order as fulfilled. Where the terms depend on acceptance or delegated authority, establish those facts. A recipient can commission a fixed result while leaving selection of the Methods to the planner.

- `domainPrescribedAction` identifies the applicable domain Method, the exact prescription and its required action, applicability and stop conditions. An optional intended WorkPlan may carry that intention; it establishes neither authority nor permission. No decision wrapper or ongoing Work is required for this branch.
- `situationResponsiveDecisionEpistemeRef` refers to an episteme identified under C.2.1 because this plan relies on an A.15.7 decision; the episteme states the selected action, deciding System, intended performer, action-changing fact, relevant Method limit, and stop or feedback condition.
- `fixedOptionChoiceResultRef` refers to a C.11 `ChoiceResult` whose result is `choose now`.

Consuming either decision result here preserves its existing result kind.

There is no catch-all `ATC.PolicyRef`. When a constraint branch is current, cite its object: C.19 `PoolPolicyResult` or `EmitterPolicy`, a C.19.1 probe, comparison, local-policy, or waiver result, or a domain constraint whose kind and defining pattern are named. The plan retains applicable time, compute, cost and risk ceilings and its stop or replan conditions.

#### C.24:4.1 - Owned planning operations

C.24 owns only planning and replanning:

```text
planCalls(
  actionBasis,
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

`A.3.1` supplies Method admission. The action basis fixes the action or option being planned; it does not admit the Methods chosen for plan steps.

A commissioned action carries its operative terms and completion conditions. A domain-prescribed basis carries its Method, prescription, required action, applicability and stop conditions. Permission and authority remain independently governed. An A.15.7 basis keeps the selected action, deciding System, intended performer, action-changing fact, relevant domain-Method limit, and stop or feedback condition. A C.11 basis is a `ChoiceResult` whose lawful result is `choose now`; `probe again`, `reject current set`, and `reroute` do not fix an action for C.24.

C.18 may supply generated candidate or front material, and C.19 may supply a live-pool treatment that informed the decision; neither record admits a Method. Comparison comes from the selected evaluation Method and, when scale preference is claimed, `C.19.1`.

A.15.1 governs the actual call or observation Work; `G.6` provides a trace representation when those independently established facts, results and provenance relations must remain replayable. C.24 only constrains what the plan or checkpoint must retain for those later uses.

To construct the route, use the backward construction and forward check in `OPS.11.1:4.2–4.3` for this fixed action:

1. **Recover usable contributions.** Read the available Methods and any needed route descriptions for the results they supply, required inputs, preconditions, relevant effects and limits. Resolve missing interface meaning from the maintained description or provider. Begin with the action's receiving completion conditions.
2. **Work backwards from the required result.** Establish what must hold for the recipient, including conditions that several services must provide together. Choose admitted Methods for the required contributions. For a missing input, trace it to an available source or a qualified supplying Method. For concurrent provision, establish whether all necessary contributions can be available together for the required interval. If a contribution cannot be supplied, return that particular gap rather than adding an ungrounded call.
3. **Check forwards from the available inputs.** Follow a proposed output to the operation that uses it, and follow jointly required contributions to the condition they establish. Check consequential units, scope, access, timing and other use conditions. Reconcile shared resources and applicable budget. Elapsed time is not the sum of resource expenditure when calls overlap. Reuse established interface and performance bounds where adequate. Check whether the proposed calls and their connections supply the entire result promised to the recipient. If a call only prepares the input for delivery or acceptance, include the work still needed and its time and entry conditions in the plan.
4. **Return the route or the unresolved question.** State the calls, useful intermediate results, required ordering or safe parallelism, shared resources and stop or replan conditions. When a later call depends on an earlier result, specify what the person or system making that choice will know in time and what it can then do. For a guaranteed result, check the remaining budget and completion conditions on every reachable branch. If the deciding information arrives after an irreversible choice, establish a route that works across the cases still possible then, or report the missing condition. Use §4.2 for a bounded scout when its result could resolve that question at justified cost. If the action changes, use §0.4 to establish what still fixes it. Stop the work the cancellation ends. If another operative requirement still fixes a remaining action, continue or revise its route on that basis. Refer an open choice to whoever may settle it.


#### C.24:4.2 - Bounded scout or probe cycle

When the action remains fixed but an unresolved route condition could change the continuation, first use adequate interface documentation, existing observations or provider information. Select a bounded scout only when its attainable answer can change the warranted continuation enough to justify its burden, within the applicable budget and permission. State what observation would retain, revise or reject the route before planning that scout. Its actual performance can support a `CheckpointReturn`; an unfamiliar route alone does not require probing.

- If another probe could still change which option survives the `OptionSet`, the budget remains a C.11 probe budget and planning returns there.
- If changed live facts or domain-Method limits could change an A.15.7 action, return there instead.
- If a commission or prescription ceases to apply, establish whether the action still has a sufficient basis. When it reopens, return to its responsible holder before committing further resources.
- If the action or option remains fixed and only route shape or rollout order is uncertain, the probe uses enactment budget and its checkpoint belongs here.

`commitTrigger` names a condition that changes how the proposed `CallPlan` can be used. Identify the plan and what it schedules. When a fresh adoption decision is reserved, return the probe result and the warranted recommendation to its holder. A planner who has that authority may adopt the plan, probe further within budget, or stop. When the authorized holder has already adopted a specified route conditional on the result, establish that the decision is still in force, its condition has been met and any other requirements for adoption hold. The checkpoint can then report which route has taken effect.

Once the route is adopted, check the applicable permission for the planned calls. Evidence of route adoption and entry permission can justify starting the work. To claim execution, establish the dated `U.Work`. Where an autonomy budget governs the route, apply the checkpoint decision and guard or override path in `E.16-S1.A` within that budget and scope.

#### C.24:4.3 - Planning laws

**ATC-1 — Plan the call, not the app.** A plan step selects a Method. A route description, endpoint, service promise, trace row, or response does not become that Method or an actual call.

**ATC-2 — Use the C.19.1 branch that applies.** A bounded call plan with no scale/generalization claim or declared generality policy can proceed under its task, budget and guards. When that claim or policy is current, start with C.19.1's scale-claim probe. Consume its first result: `no scale claim yet`, `local analogy or policy`, `bounded scale comparison`, or `full Scale-Audit selected`. Only the latter two open comparison or audit work.

A completed comparison of usable responses over the receiving budget range, with uncertainty and applicable floors, may then warrant a bounded preference or `no scale-based preference`. A larger slope alone is insufficient; a generality tie-break needs its separate policy basis.

Keep a `BLP-waiver` separate: it is used only when a declared generality preference would otherwise decide the use, and it records rationale, the admitted review System, the direct waiver-review responsibility or missing governor, and expiry or review.

If comparable evidence is absent, stop the empirical preference; do not invent a slope vector or treat a waiver as evidence.

**ATC-3 — Make budgets and harm limits visible.** A `CallPlan` states its applicable planned ceilings. A `CheckpointReturn` or Work-side record states actual burn. The admitted System stops or replans when a named ceiling or safety condition is breached.

**ATC-4 — Keep live-pool exploration declared.** Cite a C.19 `PoolPolicyResult` only while treatment of that still-live pool constrains this plan. Cite its exact `EmitterPolicy` only when the plan uses that profile; then record `explore_share`, including `0` when the current profile explicitly plans none. Do not fabricate either ref after the fixed action or option has made pool treatment irrelevant, and do not silently turn illumination or novelty telemetry into a decision criterion.

**ATC-5 — Preserve the execution basis needed by later use.** An actual call claim retains its dated Work, performer, enacted Method, interval and containing-System relation under A.15.1. When later use needs a replayable account, retain the relevant plan ref, actual budget delta, inputs and outputs subject to privacy, route-description edition used, and G.6 trace reference. The plan and trace do not establish the represented facts by themselves.

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

Each comparison tolerance names its characteristic, bearer, scale, evidence basis, and window. Graduation, rollout, or widening uses a condition defined by the cited result or direct domain pattern.

Plan-local ceilings and stop conditions need no policy object. If another domain constraint is current, give its field the result-kind name and cite its defining pattern; do not put it in a catch-all constraint ref.

When a condition relies on assurance, cite the exact B.3 result and its supported scope; no universal assurance level is inherited from C.19.

#### C.24:4.5 - Causal action-use field

Add the causal field only for a named causal use in which the planned calls are intended to observe, intervene, collect counterfactual-rung evidence, simulate for a causal claim, condition a counterfactual policy, or evaluate a policy causally:

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

An ordinary written plan can supply this content; the schemas above are optional forms. Retain an existing applicable plan when it already states:

- the operative grounds fixing the action, its objective, and the ordered Method refs. These grounds may come from a commission, a domain prescription, an A.15.7 decision or a C.11 `choose now` result;
- route-description refs only when needed, with their source scheme, exact edition, intended use, and selected Method binding;
- dependencies, the simultaneous availability of jointly required services, safe parallelism and any earlier result that governs which later call can be made, when these change the route;
- applicable time, compute, cost or risk budgets, with stop and replan conditions;
- next planned action; and
- an exact C.19 or C.19.1 result, B.3 assurance result, causal-use result, provenance ref, or named domain-constraint result only when that branch is current.

This is enough for an ordinary plan. Do not fill the heavier branches merely to make the record look complete.

#### C.24:4.7 - Closure and worked cases

Close as a `CallPlan` when route order and budgeted enactment are the current question. After a bounded route probe, state in the `CheckpointReturn` whether to probe again, stop, use a previously adopted route whose conditions now hold, or seek the still-required adoption decision. When the action reopens, return to the commission or the corresponding domain prescription, A.15.7 or C.11 decision. Use the applicable neighbouring pattern when pool treatment, selector declaration, readiness, execution or publication becomes the question.

**Domain-prescribed action before Work.**

In a constructed catalogue-maintenance case, CatalogueMethod_3 requires rebuilding a digest when the catalogue’s source checksum changes. That condition is established; no choice of action remains and the rebuild has not begun. Plan the two admitted Methods directly:

```text
CallPlan:
  actionBasis:
    domainPrescribedAction:
      methodRef = CatalogueMethod_3
      prescriptionRef = catalogue_method_v3#changed-source-digest
      prescribedAction = rebuild_digest
      applicabilityAndStop = changed_source_checksum; stop_if_input_version_changes
  objective = digest_for_the_fixed_catalogue_version
  plannedCallsInOrder = [ReadCatalogueMethod_2, BuildDigestMethod_4]
  plannedBudgetEnvelope = {time<=10_minutes, cost<=catalogue_budget, risk<=read_and_derived_file_only}
  stopOrReplan = input_version_changes_or_budget_is_exceeded
  nextPlannedAction = confirm_required_entry_permission_then_run_read
```

The prescription fixes the action, while work-entry permission remains separate. If a permitted route probe is needed, its CheckpointReturn retains this same domainPrescribedAction branch and states the tested Methods, findings, spent/residual budget and next action. A changed prescription or input condition reopens the domain basis. Neither form invents an A.15.7 decision or completed Work.

**A.15.7 decision into a known route.**

During ongoing repository-repair Work, changed source facts make `produce_patch_and_verify` the next action under the current repair Method. Using the steering Method in A.15.7, the responsible maintainer makes that decision. The retained decision names the repair agent as intended performer, the changed-source fact, and test failure as the stop and feedback condition. Because the call plan relies on the decision later, the team retains it in one episteme identified under C.2.1. The episteme describes the situation-responsive decision; it is not a C.11 `ChoiceResult`.

```text
CallPlan:
  actionBasis:
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

An actual call needs its independent A.15.1 grounds; add assignment-bound attribution and a trace representation when the receiving use consumes them.


**Constructing a route from a fixed result.**

The team has accepted a one-off order to deliver this week's report and obtain the recipient's acceptance. That commission fixes the action. The team selects how to carry it out. The maintained interface specifies the timestamp unit, the recipient's week boundary and time zone, and the required report format. Four admitted Methods extract the rows, convert their timestamps, aggregate by week, and render a conforming report. For the specified input size and one sequential performer, they take at most 2, 3, 4 and 1 minutes respectively. The team has 12 minutes.

Work backwards from acceptance. The four calls prepare the report in at most 10 minutes. Their outputs establish that it can be ready to send. The recipient also provides an admitted submission Method. Under its stated conditions it delivers a conforming report and returns the recipient's acceptance within 2 minutes. The intended performer has access, the receiver is available for the full interval, and the prepared report meets its entry conditions. The five-call plan therefore fits the 12-minute budget. The time bound warrants adopting the plan under the stated conditions. To close the actual job by its deadline, establish when this recipient accepted this report. Acceptance after the deadline means the commissioned job finished late. Delivery itself may have been on time. An undated acceptance can establish receipt and acceptance while leaving timeliness open.

If the export already supplies compatible timestamps, the remaining calls fit in 9 minutes. If the submission service promises only to queue the file within 2 minutes, the team can promise timely submission on that basis. A deadline for recipient acceptance still depends on what happens after queuing.

If the timestamp unit or week boundary is missing, recover that interface or receiving condition from its authoritative source. The magnitude of sample numbers does not establish a unit. A changed report requirement returns to the action basis before replanning.

**Unfamiliar route.**

In this constructed repair case, `ci_route_choice_09` fixes the action: produce a candidate patch and run the targeted tests. The proposed `ci_patch_plan_09` orders `EditCandidateMethod_2` and `TargetedTestMethod_7`, has an upper duration bound of 25 minutes, and stops for replanning if the reproduction changes or the tests fail twice. Adoption here requires a supported guarantee that the repair fits the enactment time left after route probing.

Before adopting that plan, the maintainer probes whether the failure can be reproduced reliably enough to guide the patch. For this case, `MinimalReproductionMethod_5` requires the same failure in two consecutive runs on the fixed repository revision, with the trace and reproduction evidence collected on that revision. One such run has completed. The enactment budget covers both this route probing and the planned repair.

```text
CheckpointReturn:
  actionBasis:
    fixedOptionChoiceResultRef = ci_route_choice_09
  objectiveOrTaskFamily = unfamiliar_ci_failure
  testedMethodRefs = [LogTraceMethod_2, MinimalReproductionMethod_5]
  evidenceRefs = [trace_result_1, reproduction_result_1]
  burnedBudget = 15_minutes
  residualBudget = 30_minutes
  recommendedNextAction = repeat_minimal_reproduction_then_return_for_checkpoint_decision_on_ci_patch_plan_09
  commitTrigger = reproduction_is_stable_and_required_evidence_is_current
```

If the repeat establishes the trigger, the maintainer decides whether to end route probing and adopt `ci_patch_plan_09`: produce the patch, then run its targeted tests. The maintainer compares the time remaining after that repeat with the plan's 25-minute upper duration bound and checks the applicable safety or assurance conditions.

A 3-minute repeat leaves 27 minutes, which covers that bound. A 6-minute repeat leaves 24 minutes, so the current bound does not establish the required guarantee. A tighter justified bound for the same route, a qualified alternative route or an independently permitted budget revision may establish fit; otherwise stop.

If the plan is adopted, the repair agent may start its first call only with the required work-entry permission. The checkpoint itself records neither that permission nor a performed call.

**Two vendor routes with one token.**

Vendor A and Vendor B both publish a route called `search`. `vendor_a_search_v2` states scheme `VendorA API`, edition `2026-07`, intended use `repository text search`, and selected Method `RepositoryTextSearchMethod_3`. `vendor_b_search_v5` states scheme `VendorB agent tools`, edition `2026-08`, intended use `web source retrieval`, and selected Method `WebSourceRetrievalMethod_8`. The shared token identifies neither binding; the description fields do. An executable adapter, if used, remains distinct from the Method it implements, and its execution remains separate Work.

**Scale comparison, when current.**

The cheap C.19.1 probe for `BatchSearchMethod_3` and `IndexedSearchMethod_6` returns `bounded scale comparison` for the same repository-search task and `10k–100k files` window. The comparison then uses elapsed time and missed-match rate from `repo_search_benchmark_12`, including uncertainty and cost limits, and warrants a preference for `IndexedSearchMethod_6` only inside that window.

If the evidence for one Method covers only small text files and the evidence for the other covers only large mixed repositories, the task difference leaves their relative performance on the receiving workload open. Return `no scale-based preference`. A tie-break written for established equivalent performance does not apply to that finding. The project can use a local policy that covers the actual case or seek a waiver when overriding a preference that would otherwise decide the use.

**Near misses.** A route label with no recovered Method remains probe material. A plan with no Work is still intent. A trace row does not prove performer, assignment, Method, or service acceptance. If the holder reserved a fresh decision, a satisfied `commitTrigger` still leaves adoption open. A standing conditional adoption can already settle the route when its terms hold.

**Transfer examples.** The same result shape works for research assistance, program repair, and lab automation. The Methods and safety conditions differ; the plan/checkpoint boundary does not.

