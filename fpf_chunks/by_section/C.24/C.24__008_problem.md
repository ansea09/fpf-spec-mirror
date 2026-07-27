---
chunk_kind: "child"
pattern_id: "C.24"
pattern_title: "Agentic Tool-Use and Call Planning (C.Agent-Tools-CAL)"
section_id: "C.24:2"
section_title: "Problem"
source_path: "FPF-Spec.md"
output_path: "by_section/C.24/C.24__008_problem.md"
commit_sha: "60caecb4751fb2a3623a1faaca757d29a19acff9"
heading_path:
  - "C.24 — Agentic Tool-Use and Call Planning (C.Agent-Tools-CAL)"
  - "C.24:2 — Problem"
line_start: 51955
line_end: 51957
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

### C.24:2 - Problem
We need a **tool-agnostic** way to (i) identify **admissible route descriptions**, (ii) compose one **call work plan** that cites them, (iii) allocate an **explore/exploit** share, (iv) enforce **budget & harm** gates, and (v) **replan** on signals—**without** baking domain-specific heuristics into the core and **without** collapsing `U.MethodDescription`, `U.WorkPlan`, and `U.Work` into one object.

