---
chunk_kind: "child"
pattern_id: "A.3.1"
pattern_title: "U.Method"
section_id: "A.3.1:1"
section_title: "Context (plain‑language motivation)"
source_path: "FPF-Spec.md"
output_path: "by_section/A.3.1/A.3.1__002_context-plain-language-motivation.md"
commit_sha: "093d30e806a1466e24032733eb020bb5a5f585cc"
heading_path:
  - "A.3.1 — U.Method"
  - "A.3.1:1 — Context (plain‑language motivation)"
line_start: 5910
line_end: 5925
dependencies:
  - "A.1"
  - "A.1.1"
  - "A.15"
  - "A.2"
  - "A.2.1"
  - "A.2.2"
  - "A.3"
  - "B.1"
  - "U.BoundedContext"
  - "U.Capability"
  - "U.Dynamics"
  - "U.PromiseContent"
  - "U.Role"
  - "U.RoleAssignment"
  - "U.WorkPlan"
keywords:
  - "abstract process"
  - "how-to"
  - "procedure"
  - "recipe"
---

### A.3.1:1 - Context (plain‑language motivation)

Teams must talk about **how** something is done without entangling:

* **Who** is assigned (that is **Role**/**RoleAssigning**),
* **Whether** the holder can do it (that is **Capability**), and
* **What actually happened** (that is **Work**).

`U.Method` supplies the *how*—the **abstract way of performing a transformation**, independent of a specific run, a specific assignee, or a specific notation. It works across paradigms:

* **Imperative** (step‑graphs, SOPs, BPMN),
* **Functional** (pure mappings and compositions, no “steps”),
* **Logical/constraint/optimization** (goals, rules, admissible solutions).

In FPF, a **system** bearing a **TransformerRole** *enacts* a `U.Method` (producing **Work**) by following a **MethodDescription**—an episteme that describes the method in some representation.

