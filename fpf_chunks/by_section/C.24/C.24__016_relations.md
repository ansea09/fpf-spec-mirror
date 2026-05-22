---
chunk_kind: "child"
pattern_id: "C.24"
pattern_title: "Agentic Tool‑Use & Call‑Planning (C.Agent‑Tools‑CAL)"
section_id: "C.24:12"
section_title: "Relations"
source_path: "FPF-Spec.md"
output_path: "by_section/C.24/C.24__016_relations.md"
commit_sha: "725f0b7b372754cda3f6f4e15184215da568fc4d"
heading_path:
  - "C.24 — Agentic Tool‑Use & Call‑Planning (C.Agent‑Tools‑CAL)"
  - "C.24:12 — Relations"
line_start: 43059
line_end: 43070
dependencies:
  - "A.1"
  - "A.15"
  - "B.3"
  - "C.11"
  - "C.18"
  - "C.19"
  - "C.28"
  - "C.5"
  - "E.2"
  - "E.3"
  - "E.5"
  - "G.5"
  - "G.6"
  - "G.9"
  - "U.PromiseContent"
  - "U.WorkPlan"
keywords:
  - "BLP tolerances"
  - "CallGraph"
  - "CallPlan"
  - "CallRouteDescription"
  - "CheckpointReturn"
  - "agential tool use"
  - "budget and harm gates"
  - "enactment budget"
  - "route-vs-plan-vs-work distinction"
  - "stop/replan condition"
  - "tool-call budget"
---

### C.24:12 - Relations

**C.27 temporal-claim relation.**

- C.27 may flag: a tool-use plan claiming that tool use changes debugging, learning, search, repair, rollout, narrowing, uncertainty reduction, stabilization, or stop/replan rate.
- This pattern keeps: call planning, tool-use sequence, budget, stop/replan, and work trace.
- Non-admissible use: tool-call count, more context, or faster narrowing is effort evidence or input evidence at most; it is not task-success, reasoning-quality, evidence-quality, repair-success, cost, or validity-window evidence by itself.

- Exit: a speed-up claim names task outcome, evaluation harness, repair-success basis when claimed, cost or budget posture, validity window, stop or replan condition, and non-admissible use as a benchmark claim; C.24 remains the tool-use pattern.

Builds on: `A.15` Role-Method-Work alignment (planning vs execution vs service), `B.3` Trust & Assurance (`F-G-R/CL`), `C.5 Resrc-CAL`, `C.18 NQD-CAL` (candidate generation and declared set surfaces), and `C.19 E/E-LOG` (policies). Coordinates with `C.28` when a call plan is used to observe, intervene, collect counterfactual-rung evidence, condition a counterfactual policy, or evaluate a policy for causal-use support. Constrains: any `U.PromiseContent` used as a tool MUST expose acceptance conditions and observation hooks sufficient for `B.3` reporting. Enables: human-facing Working-Model surfaces with policy and assurance disclosures while keeping design-time and run-time separated.

