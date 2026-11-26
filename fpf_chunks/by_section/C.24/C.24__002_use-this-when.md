---
chunk_kind: "child"
pattern_id: "C.24"
pattern_title: "Plan Tool or Service Calls for a Fixed Action (C.Agent-Tools-CAL)"
section_id: "C.24:0"
section_title: "Use this when"
source_path: "FPF-Spec.md"
output_path: "by_section/C.24/C.24__002_use-this-when.md"
commit_sha: "9d38fbfe4ce5b72d8fe05e839cbca0025a5b31cf"
heading_path:
  - "C.24 — Plan Tool or Service Calls for a Fixed Action (C.Agent-Tools-CAL)"
  - "C.24:0 — Use this when"
line_start: 67878
line_end: 67986
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

### C.24:0 - Use this when

Use `A.15.7` first when ongoing Work still needs the next action to be chosen from current facts within a domain Method. Enter `C.24` only after that action is fixed and tool or service calls must be planned. A call plan is neither the situation-responsive decision nor proof that the chosen action was performed.


Use `C.24` when an operative instruction, commitment, domain prescription or decision has fixed the action or option and the practical question is now:

- which admitted Methods to call, in what order;
- which applicable time, compute, cost or risk budget to reserve;
- what stops or replans the route; and
- whether the useful output is a `CallPlan` or a `CheckpointReturn`.

Do not use it to generate candidates, keep a live pool, choose among unresolved options, execute calls, or score completed Work.

#### C.24:0.1 - What goes wrong if missed

- a route is scheduled by an opaque heuristic, so its budget use and stop conditions are hidden;
- unresolved choice or pool-policy work is hidden in a plan;
- a route description is mistaken for a Method, a plan for performed Work, or a successful probe for a decision to adopt and execute the route; and
- replanning loses the basis that fixed the action and its conditions.

#### C.24:0.2 - What this buys

- one small, tool-neutral plan that cites the accepted action basis;
- visible budgets, stop conditions, and replan triggers before calls are made;
- recoverable call facts and provenance when later use needs an execution account; and
- a checkpoint explaining whether to probe again, stop or proceed along an applicable route, and who still needs to decide.

**Primary working object.** One `ATC.CallPlan : U.WorkPlan`. Each step selects a `U.Method`. A route description may help locate or constrain that Method, but remains a separate `U.MethodDescription`. Actual calls are dated `U.Work` and remain outside this planning result.

**First useful move.** Recover what fixes the action and its completion conditions. An accepted one-off commission may already name the required result and recipient while leaving the route for the planner to choose. Establish which required results are already available and what still has to be done with them. If a usable result can be delivered as ordered, plan its delivery. If the order requires a fresh performance, include it. Reuse an adequate known route for the remaining work.

Otherwise, work backwards from the required result to admitted Methods and their needed inputs, then follow the proposed route forwards from the available inputs as in section 4.1.

Return the supported ordered calls, applicable budget and stop or replan conditions, or the particular missing contribution or condition. Add route-description refs where they are needed to understand or qualify the route.

**Not this pattern when.** Use `C.11` while fixed-option choice is unresolved, `C.19` while treatment of a live pool is unresolved, `G.5` when the current task is selector-facing result declaration, `A.15.5` for work-entry readiness, and `A.15.1` when the question is what Work actually occurred or which Method it enacted.

#### C.24:0.3 - First-minute questions

1. What fixes the action or option, who can change it, and which choices about the route remain yours?
2. What still has to reach the recipient? Work back to the available inputs and choose the admitted Methods whose results can supply the missing contributions.
3. Which budget is current: a still-upstream probe budget or an enactment/call budget?
4. What event stops or replans the route?
5. Is the useful output a plan, a checkpoint, or a return to a neighbouring pattern?

#### C.24:0.4 - First output

The first useful output is one of these:

```text
CallPlan:
  actionBasis:
    commissionedAction?:
      operativeInstructionOrCommitmentRef
      actionAndCompletionConditions
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
      runWhen?                       # earlier observable condition selecting this call on a branching route
      mayRunInParallelWithStepRefs?  # only when safe parallelism matters
  plannedBudgetEnvelope
  stopOrReplan
  nextPlannedAction
```

```text
CheckpointReturn:
  actionBasis:
    commissionedAction?:
      operativeInstructionOrCommitmentRef
      actionAndCompletionConditions
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


`nextPlannedAction` and `recommendedNextAction` are local fields. Cite the grounds sufficient to fix this action. Where an instruction fixes the deliverable and a binding prescription fixes a further condition, retain both. One sufficient ground can stand on its own.

Add one of the branch-specific refs in C.24:4.4 only when that constraint still affects the plan. A plan with no current policy branch needs no policy placeholder.

If neither output can cite its accepted action basis and state what happens next, the C.24 work is unfinished.

When an instruction, prescription or decision changes, establish what still fixes this action under the governing terms. Another sufficient ground can keep the action fixed. A withdrawal that cancels the work calls for stopping it. If a choice reopens, return it to the holder of the commission, the domain Method, A.15.7 or C.11 as appropriate. A changed live-pool branch returns to C.19.

