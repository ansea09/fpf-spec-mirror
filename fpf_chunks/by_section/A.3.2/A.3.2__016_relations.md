---
chunk_kind: "child"
pattern_id: "A.3.2"
pattern_title: "U.MethodDescription"
section_id: "A.3.2:15"
section_title: "Relations"
source_path: "FPF-Spec.md"
output_path: "by_section/A.3.2/A.3.2__016_relations.md"
commit_sha: "04dd733fb18b66d3a640d11758e0af22ea253fd8"
heading_path:
  - "A.3.2 — U.MethodDescription"
  - "A.3.2:15 — Relations"
line_start: 6334
line_end: 6341
dependencies:
  - "A.1.1"
  - "A.15"
  - "A.2"
  - "A.2.1"
  - "A.2.2"
  - "A.3"
  - "A.3.1"
  - "C.28"
  - "U.BoundedContext"
  - "U.Capability"
  - "U.Dynamics"
  - "U.Method"
  - "U.Role"
  - "U.RoleAssignment"
  - "U.WorkPlan"
keywords:
  - "SOP"
  - "U.Episteme"
  - "code"
  - "model"
  - "recipe"
  - "specification"
---

### A.3.2:15 - Relations

* **Builds on:** A.3.1 `U.Method` (the semantic way it describes); A.1.1 `U.BoundedContext`.
* **Coordinates with:** A.2 `U.Role`, A.2.1 `U.RoleAssignment` (who enacts it); A.2.2 `U.Capability` (ability thresholds); A.15 Role–Method–Work (linking `isExecutionOf` to runs); `C.28` when intervention, target-trial, counterfactual-sampling, simulation, or causal-evidence work is used to support a causal-use claim.
* **Informs:** `U.WorkPlan` (plans reference MethodDescriptions); `U.Dynamics` (models that specs may assume); Epistemic Role patterns (status of specs RoleStateGraph + State Assertion).
* **Lexical guards:** E.10.y **L‑PROC** (do not call MethodDescription “process” when you mean Work/WorkPlan); E.10.x **L‑FUNC** (avoid “function/functionality” confusion).


