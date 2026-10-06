---
chunk_kind: "child"
pattern_id: "C.24"
pattern_title: "Plan Tool or Service Calls for a Fixed Action (C.Agent-Tools-CAL)"
section_id: "C.24:0"
section_title: "Use this when"
source_path: "FPF-Spec.md"
output_path: "by_section/C.24/C.24__002_use-this-when.md"
commit_sha: "94b6c708eadc1a572f7db7788ed2e74df4053b2d"
heading_path:
  - "C.24 — Plan Tool or Service Calls for a Fixed Action (C.Agent-Tools-CAL)"
  - "C.24:0 — Use this when"
line_start: 60948
line_end: 61041
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
  - "agentic tool-use"
  - "call planning"
  - "route probe"
  - "service calls"
---

### C.24:0 - Use this when

Use `A.15.7` first when ongoing Work still needs the next action to be chosen from current facts within a domain Method. Enter `C.24` only after that action is fixed and tool or service calls must be planned. A call plan is neither the situation-responsive decision nor proof that the chosen action was performed.


Use `C.24` when an applicable domain prescription or a completed decision has fixed the action or option and the practical question is now:

- which admitted Methods to call, in what order;
- which time, compute, cost, and risk budget to reserve;
- what stops or replans the route; and
- whether the useful output is a `CallPlan` or a `CheckpointReturn`.

Do not use it to generate candidates, keep a live pool, choose among unresolved options, execute calls, or score completed Work.

#### C.24:0.1 - What goes wrong if missed

- a route is scheduled by an opaque heuristic, so nobody can see which budget is being burned or what should stop it;
- unresolved choice or pool-policy work is smuggled into a plan;
- a route description is mistaken for a Method, a plan for performed Work, or a successful probe for a decision to adopt and execute the route; and
- replanning loses the basis that fixed the action and its conditions.

#### C.24:0.2 - What this buys

- one small, tool-neutral plan that cites the accepted action basis;
- visible budgets, stop conditions, and replan triggers before calls are made;
- one replayable call-trace reference after Work occurs; and
- one bounded checkpoint stating whether to probe again or seek a decision to adopt the proposed route.

**Primary working object.** One `ATC.CallPlan : U.WorkPlan`. Each step selects a `U.Method`. A route description may help locate or constrain that Method, but remains a separate `U.MethodDescription`. Actual calls are dated `U.Work` and remain outside this planning result.

**First useful move.** Identify the applicable domain prescription, A.15.7 decision or C.11 choose-now result that fixes the action. Fill that one branch of `actionBasis`. Then write the ordered Method refs, budget, stop or replan condition, and next planned action. Add route-description refs only where the route cannot be understood without them.

**Not this pattern when.** Use `C.11` while fixed-option choice is unresolved, `C.19` while treatment of a live pool is unresolved, `G.5` when the current task is selector-facing result declaration, `A.15.5` for work-entry readiness, and `A.15.1` when the question is what Work actually occurred or which Method it enacted.

#### C.24:0.3 - First-minute questions

1. Which applicable domain prescription, A.15.7 decision or C.11 choose-now result fixes the action or option now being planned?
2. Does every planned step name an admitted Method, rather than only a vendor route or endpoint label?
3. Which budget is current: a still-upstream probe budget or an enactment/call budget?
4. What event stops or replans the route?
5. Is the useful output a plan, a checkpoint, or a return to a neighbouring pattern?

#### C.24:0.4 - First output

The first useful output is one of these:

```text
CallPlan:
  actionBasis:
    domainPrescribedAction?:
      methodRef
      prescriptionRef
      prescribedAction
      applicabilityAndStop
      intendedWorkPlanRef?
    situationResponsiveDecisionEpistemeRef?  # A.15.7; only when this plan relies on the retained decision
    fixedOptionChoiceResultRef?               # C.11; only a choose-now result
  objective
  plannedCallsInOrder:
    - methodRef
      methodDescriptionRef?          # only when the route description is needed
      dependsOnPlannedStepRefs?      # only when dependency changes the route
      mayRunInParallelWithStepRefs?  # only when safe parallelism matters
  plannedBudgetEnvelope
  stopOrReplan
  nextPlannedAction
```

```text
CheckpointReturn:
  actionBasis:
    domainPrescribedAction?:
      methodRef
      prescriptionRef
      prescribedAction
      applicabilityAndStop
      intendedWorkPlanRef?
    situationResponsiveDecisionEpistemeRef?  # A.15.7
    fixedOptionChoiceResultRef?               # C.11 choose-now result
  objectiveOrTaskFamily
  testedMethodRefs
  testedMethodDescriptionRefs?
  evidenceRefs
  burnedBudget
  residualBudget
  recommendedNextAction
  commitTrigger
```


`nextPlannedAction` and `recommendedNextAction` are local fields, not claims that Work has occurred. Exactly one action-basis branch is present. Add one of the branch-specific refs in C.24:4.4 only when that constraint still affects the plan. A plan with no current policy branch needs no policy placeholder. If neither output can cite its accepted action basis and state what happens next, the C.24 work is unfinished.

If the domain prescription, its applicability or the action it requires changes, reopen that domain basis before revising the plan. If the A.15.7 decision changes, is withdrawn, or no longer fixes the action, reopen the plan and return to A.15.7. If the C.11 `ChoiceResult` changes or no longer says `choose now`, return to C.11. A changed live-pool branch returns separately to C.19. Do not revise the call plan as though its action basis were still settled.

