---
chunk_kind: "child"
pattern_id: "A.3.2"
pattern_title: "U.MethodDescription"
section_id: "A.3.2:1"
section_title: "Context (plain‑language motivation)"
source_path: "FPF-Spec.md"
output_path: "by_section/A.3.2/A.3.2__002_context-plain-language-motivation.md"
commit_sha: "eb2832093c1e482d5fdd4985c3d2011ab240b429"
heading_path:
  - "A.3.2 — U.MethodDescription"
  - "A.3.2:1 — Context (plain‑language motivation)"
line_start: 6058
line_end: 6070
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

### A.3.2:1 - Context (plain‑language motivation)

Projects need a **stable way to express “how it is written”**—the recipe, code, SOP, rule set, or formal proof—**without confusing it** with:

* the **semantic “way of doing”** (that is `U.Method`),
* the **assignment** (that is `U.RoleAssignment`),
* the **ability** (that is `U.Capability`),
* the **execution** (that is `U.Work`), or
* the **calendar plan** (that is `U.WorkPlan`).

`U.MethodDescription` gives this anchor. It treats **algorithms, programs, proofs, SOPs, BPMN diagrams, solver models, playbooks** as **one class of epistemes**: *knowledge on a carrier that describes a Method*. This unifies software and “paper” procedures and lets teams switch notations without breaking the model.


