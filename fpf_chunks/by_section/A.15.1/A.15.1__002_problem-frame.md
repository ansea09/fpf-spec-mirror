---
chunk_kind: "child"
pattern_id: "A.15.1"
pattern_title: "U.Work"
section_id: "A.15.1:1"
section_title: "Problem Frame"
source_path: "FPF-Spec.md"
output_path: "by_section/A.15.1/A.15.1__002_problem-frame.md"
commit_sha: "c092a1f2299d88d42db012f3184aeff205c13219"
heading_path:
  - "A.15.1 — U.Work"
  - "A.15.1:1 — Problem Frame"
line_start: 21060
line_end: 21065
dependencies:
  - "A.1"
  - "A.1.1"
  - "A.15"
  - "A.2"
  - "A.2.1"
  - "A.2.2"
  - "A.3.1"
  - "A.3.2"
  - "B.1"
  - "B.1.6"
  - "U.BoundedContext"
  - "U.Capability"
  - "U.Method"
  - "U.MethodDescription"
  - "U.Role"
  - "U.RoleAssignment"
  - "U.System"
  - "U.Work"
  - "U.WorkPlan"
keywords:
  - "actuals"
  - "event"
  - "execution"
  - "log"
  - "occurrence"
  - "run"
---

### A.15.1:1 - Problem Frame

After we have agreed **who is assigned** (via **Role assignment**), **what they can do** (via **Capability**), and **how in principle** it should be done (via **Method or MethodDescription**), we still need a precise concept for **what happened as performed work** in real time and space.

That concept is **`U.Work`**: the **dated run-time occurrence** of enacting a `U.Method` by a specific performer under a `U.RoleAssignment`, with concrete parameter bindings, resource consumption, and outcomes, **naming the domain referent changed by the occurrence** (asset, product, or dataset) - **not** merely the manipulation of records about that referent. Managers care about Work because cost, time, defects, and result evidence are booked on performed occurrences. Architects care because Work ties plans and method descriptions to accountable performed work.

