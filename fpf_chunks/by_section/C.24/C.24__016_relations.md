---
chunk_kind: "child"
pattern_id: "C.24"
pattern_title: "Agentic Tool-Use and Call Planning (C.Agent-Tools-CAL)"
section_id: "C.24:12"
section_title: "Relations"
source_path: "FPF-Spec.md"
output_path: "by_section/C.24/C.24__016_relations.md"
commit_sha: "308edacfa2bdb2c60d07e4e10c0deb1f260a6a31"
heading_path:
  - "C.24 — Agentic Tool-Use and Call Planning (C.Agent-Tools-CAL)"
  - "C.24:12 — Relations"
line_start: 52905
line_end: 52916
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

### C.24:12 - Relations

**C.27 temporal-claim relation.**

- C.27 may flag: a tool-use plan claiming that tool use changes debugging, learning, search, repair, rollout, narrowing, uncertainty reduction, stabilization, or stop/replan rate.
- This pattern keeps: call planning, tool-use sequence, budget, stop/replan, and work trace.
- Non-admissible use: tool-call count, more context, or faster narrowing is effort evidence or input evidence at most; it is not task-success, reasoning-quality, evidence-quality, repair-success, cost, or validity-window evidence by itself.

- Exit: a speed-up claim names task outcome, evaluation harness, repair-success evidence locus when claimed, cost or budget condition, validity window, stop or replan condition, and non-admissible use as a benchmark claim; C.24 remains the tool-use pattern.

Builds on: `A.15` Role-Method-Work alignment (planning vs execution vs service), `B.3` Trust and Assurance (`F-G-R` with `CL`), `C.5 Resrc-CAL`, `C.18 NQD-CAL` (candidate generation and declared set results), and `C.19 E/E-LOG` (policies). Coordinates with `C.28` when a call plan is used to observe, intervene, collect counterfactual-rung evidence, condition a counterfactual policy, or evaluate a policy for causal-use support. Coordinates with `E.23` when a repeated quality-improvement loop is enacted through tool-using agents: `C.24` carries call plans, checkpoint returns, tool-call budgets, stop or replan conditions, and the separation among `CallRouteDescription`, call plan, and executed work; it does not restate the `E.23` loop method, BLP comparison and cost discipline, or other object-under-improvement evaluations governed by their direct patterns. Coordinates with `E.10.MOVE`, `E.11.PUR`, and `A.15.5` when source wording about a move is not plan-local `nextPlannedAction` or `recommendedNextAction`. Constrains: any `U.PromiseContent` used as a tool MUST expose acceptance conditions and observation hooks sufficient for `B.3` reporting. Enables: human-facing Working-Model publication forms with policy and assurance disclosures while keeping design-time and run-time separated.

