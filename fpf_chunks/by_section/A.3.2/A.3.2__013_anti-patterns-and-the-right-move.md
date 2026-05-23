---
chunk_kind: "child"
pattern_id: "A.3.2"
pattern_title: "U.MethodDescription"
section_id: "A.3.2:12"
section_title: "Anti‑patterns (and the right move)"
source_path: "FPF-Spec.md"
output_path: "by_section/A.3.2/A.3.2__013_anti-patterns-and-the-right-move.md"
commit_sha: "04dd733fb18b66d3a640d11758e0af22ea253fd8"
heading_path:
  - "A.3.2 — U.MethodDescription"
  - "A.3.2:12 — Anti‑patterns (and the right move)"
line_start: 6303
line_end: 6313
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

### A.3.2:12 - Anti‑patterns (and the right move)

* **Spec = run.** “Yesterday’s process log is our spec.” → The log is **Work**; write a **MethodDescription** and link runs to it.
* **Who/time in the spec.** “Step 3 by Alice at 02:00 daily.” → Use **RoleAssigning** at run time; schedule via **WorkPlan**.
* **Stuffing BoM.** Listing parts and assemblies inside the spec. -> Reference **interfaces and resources**; keep PBS and SBS separate.
* **Algorithm‑only bias.** Treating code as “real spec” and SOPs as “notes.” → Both are **MethodDescription**; judge by Standards, not by format.
* **Hiding non‑determinism.** Solver model with no acceptance criteria. → Declare admissible outcome set and tests.
* **Silent parameter capture.** Hard‑coding values without declaring parameters. → Declare parameters with ranges; bind at Work creation.
* **Undeclared variant drift.** Copy‑pasting specs and tweaking silently. → Use **VariantOf** with stated deltas or declare a refinement.


