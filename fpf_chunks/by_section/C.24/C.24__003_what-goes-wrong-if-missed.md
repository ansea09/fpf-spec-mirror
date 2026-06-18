---
chunk_kind: "child"
pattern_id: "C.24"
pattern_title: "Agentic Tool-Use and Call Planning (C.Agent-Tools-CAL)"
section_id: "C.24:0.1"
section_title: "What goes wrong if missed"
source_path: "FPF-Spec.md"
output_path: "by_section/C.24/C.24__003_what-goes-wrong-if-missed.md"
commit_sha: "cf12b97913ff82ca8a45ba77d3658ad11e0fdeb6"
heading_path:
  - "C.24 — Agentic Tool-Use and Call Planning (C.Agent-Tools-CAL)"
  - "C.24:0.1 — What goes wrong if missed"
line_start: 45489
line_end: 45494
dependencies:
  - "A.1"
  - "A.15"
  - "B.3"
  - "C.11"
  - "C.18"
  - "C.19"
  - "C.24"
  - "C.28"
  - "C.5"
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

### C.24:0.1 - What goes wrong if missed

- calls get scheduled by ad-hoc heuristics, so the plan cannot say which budget is being burned or what event should stop or replan execution
- planning quietly collapses into execution, or execution quietly inherits unresolved upstream choice and pool-policy questions
- a successful probe is mistaken for committed rollout even though the commit trigger was never made explicit

