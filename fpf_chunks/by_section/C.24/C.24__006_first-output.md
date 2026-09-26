---
chunk_kind: "child"
pattern_id: "C.24"
pattern_title: "Plan Tool or Service Calls for a Fixed Action (C.Agent-Tools-CAL)"
section_id: "C.24:0.4"
section_title: "First output"
source_path: "FPF-Spec.md"
output_path: "by_section/C.24/C.24__006_first-output.md"
commit_sha: "61a9542aa8479024cdd174c024079d2a6a15f16d"
heading_path:
  - "C.24 — Plan Tool or Service Calls for a Fixed Action (C.Agent-Tools-CAL)"
  - "C.24:0.4 — First output"
line_start: 60004
line_end: 60055
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

### C.24:0.4 - First output

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

