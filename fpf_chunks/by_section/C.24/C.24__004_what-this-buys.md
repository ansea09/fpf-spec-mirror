---
chunk_kind: "child"
pattern_id: "C.24"
pattern_title: "Agentic Tool-Use and Call Planning (C.Agent-Tools-CAL)"
section_id: "C.24:0.2"
section_title: "What this buys"
source_path: "FPF-Spec.md"
output_path: "by_section/C.24/C.24__004_what-this-buys.md"
commit_sha: "7ba40a95a967ca5c69afc63aeca381e6adedc8da"
heading_path:
  - "C.24 — Agentic Tool-Use and Call Planning (C.Agent-Tools-CAL)"
  - "C.24:0.2 — What this buys"
line_start: 52688
line_end: 52699
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

### C.24:0.2 - What this buys

- one tool-agnostic planning record for admissible calls, budgets, stop conditions, and replan triggers
- one explicit enactment-facing plan or bounded checkpoint with objective, budget, stop conditions, and next planned action, without presenting intent as actual Work
- one replayable call graph and assurance record instead of one opaque chain of tool invocations

**Primary working object.** One `ATC.CallPlan : U.WorkPlan` for intended calls. Each planned call selects an exact independently admitted `U.Method`; a current route description is a separate C.2.1 `U.MethodDescription` episteme that describes and may help identify, constrain or justify that Method or intended Work. Actual tool-call Work, its performer System, obtaining assignment, interval, containing system and `enactsMethod` relation remain downstream A.15.1 facts.

**First useful move.** For each planned call, name the exact `methodRef` first, then cite an edition-pinned `methodDescriptionRef` only if its route description is needed. State order, budget, stop/replan condition and next action without claiming that Work occurred.

**Not this pattern when.** If the surviving option or pool policy is unresolved, use C.11 or C.19; if selector-facing publication is current, use G.5. If the question is only what a callable MethodDescription says, use A.3.2/C.2.1. If the question is whether a call actually occurred or what Method it enacted, use A.15.1; if work-entry readiness is the question, use A.15.5.

