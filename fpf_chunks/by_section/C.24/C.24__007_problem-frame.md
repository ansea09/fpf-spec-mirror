---
chunk_kind: "child"
pattern_id: "C.24"
pattern_title: "Agentic Tool-Use and Call Planning (C.Agent-Tools-CAL)"
section_id: "C.24:1"
section_title: "Problem frame"
source_path: "FPF-Spec.md"
output_path: "by_section/C.24/C.24__007_problem-frame.md"
commit_sha: "646b41f84ffef4918ad9bdb34e7b450f0c4903ee"
heading_path:
  - "C.24 — Agentic Tool-Use and Call Planning (C.Agent-Tools-CAL)"
  - "C.24:1 — Problem frame"
line_start: 52989
line_end: 53008
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

Modern tool-using Systems increasingly rely on tool-call planning: selecting admissible tool-service routes, arranging intended call Work, and replanning under uncertainty. A local agential-system-role classification or assignment is included only when the current claim needs that separate fact. Without a calculus:

* calls are scheduled by **ad-hoc heuristics**,
* **budgets** (compute, cost, wall-time) are implicit,
* **assurance** and **policy provenance** are lost, and
* tool-using Systems either over-constrain their plans with brittle scripts or wander without guard-rails.

This CAL provides the **conceptual API for thought** that lets any implementation (LLM-based, search-based, code-based, robotic) plan calls **admissibly**, **auditably**, and **scalably**. It keeps the planning System, any separately current classification or assignment, selected Methods, intended plan, and actual Work distinct.

Immediate failure indicators for this pattern:

* the current planning result cannot say whether one choice result already exists,
* the current text cannot distinguish exact Method, route-description episteme, call plan, and executed call Work,
* the budget being burned is still only probing-before-choice budget rather than enactment or tool-call budget, or
* the next admissible output is still undefined as one enactment-facing plan, one `CheckpointReturn`, or one neighbouring-pattern exit.

If the question under repair is still which fixed option should survive now, apply `C.11`. If it is still pool policy over several still-live candidate lines, apply `C.19`. If it is already selector-facing result declaration, apply `G.5`. If that result already exists and must be presented or made available to an audience, use `E.17` for its source-backed publication face and return to source and `E.24.PUB` for the publication occurrence and availability.

