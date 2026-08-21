---
chunk_kind: "child"
pattern_id: "C.24"
pattern_title: "Agentic Tool-Use and Call Planning (C.Agent-Tools-CAL)"
section_id: "C.24:0.4"
section_title: "First output"
source_path: "FPF-Spec.md"
output_path: "by_section/C.24/C.24__006_first-output.md"
commit_sha: "f0b498ddfdf562242984ff7ab7a2557b55af6690"
heading_path:
  - "C.24 — Agentic Tool-Use and Call Planning (C.Agent-Tools-CAL)"
  - "C.24:0.4 — First output"
line_start: 51179
line_end: 51213
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
  - "C.19.1"
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

### C.24:0.4 - First output

The first useful output is one of these:

```text
CallPlan:
  upstreamChoiceResultRef
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
  upstreamChoiceResultRef
  objectiveOrTaskFamily
  testedMethodRefs
  testedMethodDescriptionRefs?
  evidenceRefs
  burnedBudget
  residualBudget
  recommendedNextAction
  commitTrigger
```

`nextPlannedAction` and `recommendedNextAction` are local fields, not claims that Work has occurred. Add one of the branch-specific refs in C.24:4.4 only when that exact constraint still affects the plan. A plan with no current policy branch needs no policy placeholder. If neither output can cite the accepted upstream result and state what happens next, the C.24 work is unfinished.

If that upstream result changes, is withdrawn, or no longer fixes the option or route, reopen the plan and return to `C.11` or `C.19` as applicable. Do not revise the route as though the choice were still settled.

