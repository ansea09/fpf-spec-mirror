---
chunk_kind: "child"
pattern_id: "C.24"
pattern_title: "Agentic Tool-Use and Call Planning (C.Agent-Tools-CAL)"
section_id: "C.24:0"
section_title: "Use this when"
source_path: "FPF-Spec.md"
output_path: "by_section/C.24/C.24__002_use-this-when.md"
commit_sha: "02a8b4bac1f141b1751421bf522e9dc489ae522e"
heading_path:
  - "C.24 — Agentic Tool-Use and Call Planning (C.Agent-Tools-CAL)"
  - "C.24:0 — Use this when"
line_start: 47567
line_end: 47572
dependencies:
  - "A.1"
  - "A.15"
  - "A.15.5"
  - "B.3"
  - "C.11"
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

### C.24:0 - Use this when

- one concrete choice result already exists and the next task is now how to plan, gate, sequence, and replan tool calls admissibly
- the next admissible output should be one enactment-facing `CallPlan` or one `CheckpointReturn`, not one more local choice result or pool-policy result
- budget, assurance, and stop conditions must be visible before calls are burned

