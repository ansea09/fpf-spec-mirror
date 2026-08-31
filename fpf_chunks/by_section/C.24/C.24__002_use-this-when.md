---
chunk_kind: "child"
pattern_id: "C.24"
pattern_title: "Agentic Tool-Use and Call Planning (C.Agent-Tools-CAL)"
section_id: "C.24:0"
section_title: "Use this when"
source_path: "FPF-Spec.md"
output_path: "by_section/C.24/C.24__002_use-this-when.md"
commit_sha: "0c3ef3d3921bb3176096e3e6102dd819c42f6446"
heading_path:
  - "C.24 — Agentic Tool-Use and Call Planning (C.Agent-Tools-CAL)"
  - "C.24:0 — Use this when"
line_start: 53093
line_end: 53106
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

### C.24:0 - Use this when

Use `A.15.7` first when ongoing Work still needs the next action to be chosen from current facts within a domain Method. Enter `C.24` only after that action is fixed and tool or service calls must be planned. A call plan is neither the situation-responsive decision nor proof that the chosen action was performed.


Use `C.24` when a decision has already fixed the action or option and the practical question is now:

- which admitted Methods to call, in what order;
- which time, compute, cost, and risk budget to reserve;
- what stops or replans the route; and
- whether the useful output is a `CallPlan` or a `CheckpointReturn`.

Do not use it to generate candidates, keep a live pool, choose among unresolved options, execute calls, or score completed Work.

