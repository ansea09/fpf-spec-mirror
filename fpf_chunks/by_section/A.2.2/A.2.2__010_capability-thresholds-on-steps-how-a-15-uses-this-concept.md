---
chunk_kind: "child"
pattern_id: "A.2.2"
pattern_title: "U.Capability"
section_id: "A.2.2:9"
section_title: "Capability thresholds on steps (how A.15 uses this concept)"
source_path: "FPF-Spec.md"
output_path: "by_section/A.2.2/A.2.2__010_capability-thresholds-on-steps-how-a-15-uses-this-concept.md"
commit_sha: "c092a1f2299d88d42db012f3184aeff205c13219"
heading_path:
  - "A.2.2 — U.Capability"
  - "A.2.2:9 — Capability thresholds on steps (how A.15 uses this concept)"
line_start: 2800
line_end: 2815
dependencies:
  - "A.1"
  - "A.1.1"
  - "A.15"
  - "A.2"
  - "A.2.1"
  - "A.2.3"
  - "A.3"
  - "U.BoundedContext"
  - "U.Dynamics"
  - "U.PromiseContent"
  - "U.RoleAssignment"
keywords:
  - "ability"
  - "action"
  - "measures"
  - "performance"
  - "skill"
  - "work scope"
---

### A.2.2:9 - Capability thresholds on steps (how A.15 uses this concept)

A step in a **Method** may define **required roles** (assignment) and **capability thresholds** (ability). A Work passes the gate if:

1. **assignment check:** the Work’s `performedBy` points to a valid **Role assignment** that covers the step window and satisfies the role relation (including specialization `≤` inside the context).
2. **Ability check:** the **holder** of that Role assignment has a **capability** whose **WorkScope covers the step’s JobSlice** (i.e., declared superset) and whose **WorkMeasures** meet the step’s threshold(s) within `Γ_time(W)` and while the capability’s **QualificationWindow** includes *W*.

**Idioms managers can reuse (plain text):**

* *“S1 requires `IncisionOperatorRole` and Precision ≤ 0.2 mm (OR\_2025 norms) **in window W**.”*
* *“S2 requires `PlannerRole`, **WorkScope ⊇ JobSlice\[W]**, and Optimality ≥ 0.90 on `JS_Schedule_v4`.”*

**What to avoid:**

* Putting “Precision ≤ 0.2 mm” into the Role name. Keep thresholds attached to the **step**; keep **ability** on the **holder**.

