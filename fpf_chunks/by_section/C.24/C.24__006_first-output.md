---
chunk_kind: "child"
pattern_id: "C.24"
pattern_title: "Agentic Tool-Use and Call Planning (C.Agent-Tools-CAL)"
section_id: "C.24:0.4"
section_title: "First output"
source_path: "FPF-Spec.md"
output_path: "by_section/C.24/C.24__006_first-output.md"
commit_sha: "d1f696e7c7767705206a8cacd9f6ed48e4dc5b02"
heading_path:
  - "C.24 — Agentic Tool-Use and Call Planning (C.Agent-Tools-CAL)"
  - "C.24:0.4 — First output"
line_start: 52377
line_end: 52384
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

### C.24:0.4 - First output

The first useful output is either one enactment-facing `CallPlan` with the current objective, cited route descriptions, the planned budget envelope, the stop or replan condition, and the next planned action stated explicitly in one place, or one bounded `CheckpointReturn` with the current objective or task family, the burned and residual actual budget, the commit trigger, and the recommended next action stated explicitly in one place.

In C.24, move-like wording is plan-local shorthand only when it means `nextPlannedAction` inside a `CallPlan` or `recommendedNextAction` inside a `CheckpointReturn`. It does not name a general project move, pattern-use recommendation, work-entry readiness relation, performed work, or a whole `U.WorkPlan`. If the current source wording asks which FPF pattern use is recommended, use `E.11.PUR`; if it asks whether intended work is ready to start, use `A.15.5`; if it uses move-like wording outside C.24 call planning, restore the project concern with `E.10.MOVE`.

If that first output still cannot be written honestly, the current planning result is not finished `C.24` planning yet.

