---
chunk_kind: "child"
pattern_id: "A.3.2"
pattern_title: "U.MethodDescription"
section_id: "A.3.2:10"
section_title: "Parameterization & variability (templates, defaults, configs)"
source_path: "FPF-Spec.md"
output_path: "by_section/A.3.2/A.3.2__011_parameterization-variability-templates-defaults-configs.md"
commit_sha: "04dd733fb18b66d3a640d11758e0af22ea253fd8"
heading_path:
  - "A.3.2 — U.MethodDescription"
  - "A.3.2:10 — Parameterization & variability (templates, defaults, configs)"
line_start: 6265
line_end: 6285
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

### A.3.2:10 - Parameterization & variability (templates, defaults, configs)

**Templates.** A MethodDescription may serve as a **template** with parameters (e.g., temperature set‑points, solver tolerances, objective weights).

**Binding time.**

* **Declare** parameters in the spec;
* **Bind** values when creating `U.Work` (or at an agreed “compile” stage);
* Keep bound values **visible** in the Work record (so runs can be compared).

**Defaults and guards.**

* Defaults are allowed; list **valid ranges** and **guards** (e.g., safety constraints).
* If a default has safety impact, state it explicitly as part of **preconditions**.

**Variants.**

* When variants differ only by **parameter ranges** → keep one Method with one MethodDescription template.
* When variants differ by **Standard** (effects/bounds) → either declare a **refinement** or introduce a **distinct Method** (context decision).


