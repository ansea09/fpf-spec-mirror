---
chunk_kind: "child"
pattern_id: "C.24"
pattern_title: "Agentic Tool-Use and Call Planning (C.Agent-Tools-CAL)"
section_id: "C.24:1"
section_title: "Problem frame"
source_path: "FPF-Spec.md"
output_path: "by_section/C.24/C.24__007_problem-frame.md"
commit_sha: "8b727cba9e893a467b82aab9da84fb7d6d945480"
heading_path:
  - "C.24 — Agentic Tool-Use and Call Planning (C.Agent-Tools-CAL)"
  - "C.24:1 — Problem frame"
line_start: 52696
line_end: 52715
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

### C.24:1 - Problem frame

Modern systems in agential roles increasingly rely on tool-call planning: selecting admissible tool-service routes, arranging intended call work, and replanning under uncertainty. Without a calculus:

* calls are scheduled by **ad-hoc heuristics**,
* **budgets** (compute, cost, wall-time) are implicit,
* **assurance** and **policy provenance** are lost, and
* systems in agential roles either over-constrain themselves with brittle scripts or wander without guard-rails.

This CAL provides the **conceptual API for thought** that lets any implementation (LLM-based, search-based, code-based, robotic) plan calls **admissibly**, **auditably**, and **scalably**. (Role-Method-Work alignment; didactic primacy.)

Immediate failure indicators for this pattern:

* the current planning result cannot say whether one choice result already exists,
* the current text cannot distinguish exact Method, route-description episteme, call plan, and executed call Work,
* the budget being burned is still only probing-before-choice budget rather than enactment or tool-call budget, or
* the next admissible output is still undefined as one enactment-facing plan, one `CheckpointReturn`, or one neighbouring-pattern exit.

If the question under repair is still which fixed option should survive now, apply `C.11`. If it is still pool policy over several still-live candidate lines, apply `C.19`. If it is already public selected-set publication, apply `G.5`.

