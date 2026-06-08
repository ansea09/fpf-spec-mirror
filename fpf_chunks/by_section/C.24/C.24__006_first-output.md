---
chunk_kind: "child"
pattern_id: "C.24"
pattern_title: "Agentic Tool-Use and Call Planning (C.Agent-Tools-CAL)"
section_id: "C.24:0.4"
section_title: "First output"
source_path: "FPF-Spec.md"
output_path: "by_section/C.24/C.24__006_first-output.md"
commit_sha: "21e2101c100964de121c37408b37563ee0cdbf8c"
heading_path:
  - "C.24 — Agentic Tool-Use and Call Planning (C.Agent-Tools-CAL)"
  - "C.24:0.4 — First output"
line_start: 45037
line_end: 45042
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

### C.24:0.4 - First output

The first useful output is either one enactment-facing `CallPlan` with the current objective, cited route descriptions, the planned budget envelope, the stop or replan condition, and the next move stated explicitly in one place, or one bounded `CheckpointReturn` with the current objective or task family, the burned and residual actual budget, the commit trigger, and the recommended next action stated explicitly in one place.

If that first output still cannot be written honestly, the current planning result is not finished `C.24` planning yet.

