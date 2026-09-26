---
chunk_kind: "child"
pattern_id: "C.24"
pattern_title: "Plan Tool or Service Calls for a Fixed Action (C.Agent-Tools-CAL)"
section_id: "C.24:0.2"
section_title: "What this buys"
source_path: "FPF-Spec.md"
output_path: "by_section/C.24/C.24__004_what-this-buys.md"
commit_sha: "61a9542aa8479024cdd174c024079d2a6a15f16d"
heading_path:
  - "C.24 — Plan Tool or Service Calls for a Fixed Action (C.Agent-Tools-CAL)"
  - "C.24:0.2 — What this buys"
line_start: 59983
line_end: 59995
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

### C.24:0.2 - What this buys

- one small, tool-neutral plan that cites the accepted action basis;
- visible budgets, stop conditions, and replan triggers before calls are made;
- one replayable call-trace reference after Work occurs; and
- one bounded checkpoint when more route probing is justified but commitment is not.

**Primary working object.** One `ATC.CallPlan : U.WorkPlan`. Each step selects a `U.Method`. A route description may help locate or constrain that Method, but remains a separate `U.MethodDescription`. Actual calls are dated `U.Work` and remain outside this planning result.

**First useful move.** Identify the applicable domain prescription, A.15.7 decision or C.11 choose-now result that fixes the action. Fill that one branch of `actionBasis`. Then write the ordered Method refs, budget, stop or replan condition, and next planned action. Add route-description refs only where the route cannot be understood without them.

**Not this pattern when.** Use `C.11` while fixed-option choice is unresolved, `C.19` while treatment of a live pool is unresolved, `G.5` when the current task is selector-facing result declaration, `A.15.5` for work-entry readiness, and `A.15.1` when the question is what Work actually occurred or which Method it enacted.

