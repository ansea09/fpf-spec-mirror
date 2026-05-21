---
chunk_kind: "child"
pattern_id: "A.3.2"
pattern_title: "U.MethodDescription"
section_id: "A.3.2:8"
section_title: "Conformance Checklist (normative)"
source_path: "FPF-Spec.md"
output_path: "by_section/A.3.2/A.3.2__009_conformance-checklist-normative.md"
commit_sha: "eb2832093c1e482d5fdd4985c3d2011ab240b429"
heading_path:
  - "A.3.2 — U.MethodDescription"
  - "A.3.2:8 — Conformance Checklist (normative)"
line_start: 6199
line_end: 6246
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

### A.3.2:8 - Conformance Checklist (normative)

**CC‑A3.2‑1 (Episteme status).**
`U.MethodDescription` **IS** an `U.Episteme` (knowledge on a carrier). It is **not** a `U.Method` (semantic way), **not** a `U.Work` (execution), **not** a `U.Role` or `U.RoleAssignment` (assignment), **not** a `U.WorkPlan` (schedule), and **not** PBS or SBS content.

**CC‑A3.2‑2 (Context anchoring).**
Every `U.MethodDescription` **MUST** be interpreted **within** a `U.BoundedContext`. Names, Standards, and admissible non‑functional bounds are **local** to that context.

**CC‑A3.2‑3 (Method linkage).**
A `U.MethodDescription` **MUST** declare the `U.Method` it describes. Multiple MethodDescriptions **MAY** describe the same Method (see CC‑A3.2‑8).

**CC‑A3.2‑4 (assignment/time‑free).**
A MethodDescription **SHALL NOT** embed assignees, org units, or calendars. People/units are bound via **`U.RoleAssignment`** at run time; calendars belong to **`U.WorkPlan`**.

**CC‑A3.2‑5 (Structure‑free).**
BoM, PBS, and SBS descriptions **SHALL NOT** be embedded in MethodDescriptions. Reference **interfaces and resources** and constraints instead of listing parts and assemblies.

**CC‑A3.2‑6 (Role and capability requirements).**
A MethodDescription **MAY** state **role kinds** and **capability thresholds** required for enactment. These are **requirements**, not bindings. They are checked at run time against `U.RoleAssignment` and `U.Capability`.

**CC‑A3.2‑7 (Parameterization).**
Parameters **MUST** be **declared** in the Method or MethodDescription; concrete values are **bound** when creating `U.Work`. Default values in a spec are allowed but **SHALL NOT** force a schedule or assignee.

**CC‑A3.2‑8 (Semantic equivalence).**
Two MethodDescriptions **describe the same `U.Method`** in a given context **iff** they entail the **same preconditions**, **guarantee the same postconditions and effects**, and satisfy the **same non-functional bounds** for all admissible inputs and conditions of that context (per A.3.1 CC-A3.1-7). Differences in control flow, search, or notation do **not** break equivalence.

**CC‑A3.2‑9 (Refinement).**
`Spec₂` **refines** `Spec₁` for the same Method iff it **preserves interface**, **does not weaken** postconditions/effects, and **tightens** (or equal) non‑functional bounds under **equal or stronger** preconditions. Declare refinement explicitly in the context.

**CC‑A3.2‑10 (Compatibility claims).**
Claims such as “sound but incomplete” or “complete but potentially unsound” relative to another MethodDescription **MUST** be stated explicitly and scoped to the context (e.g., solver approximations).

**CC‑A3.2‑11 (Executable specs).**
Executability does **not** change status: an executable description (program, script) is still a **MethodDescription**. Its runs are **Work**; its semantics are the **Method** it denotes.

**CC‑A3.2‑12 (Epistemic roles via `U.RoleAssignment`).**
A MethodDescription **MAY** play **epistemic roles** via `U.RoleAssignment` (e.g., `ApprovedProcedureRole`, `RegulatedProcedureRole`) that classify its status. Such bindings **do not** make the spec an actor.

**CC‑A3.2‑13 (Non‑determinism declaration).**
If a MethodDescription permits non‑determinism (e.g., search/optimization), the **space of admissible outcomes** and **acceptance criteria** **MUST** be stated (so that Work can be judged).

**CC‑A3.2‑14 (Bridging across contexts).**
If two contexts use different MethodDescriptions for “the same‑named way,” an explicit **Bridge (`U.Alignment`)** **SHOULD** be provided to map terms/assumptions. Do **not** assume cross‑context identity by name alone.

**CC-A3.2-15 (Causal-use work boundary).**
A MethodDescription **MAY** describe intervention assignment, target-trial emulation, realized-counterfactual sampling, simulation, or causal-evidence collection by naming `U.Method`, `U.MethodDescription`, `U.WorkPlan`, and `U.Work` relations. It **SHALL NOT** be treated as causal-use support, causal-use admissibility, or causal-use verdict by itself. When that work is used causally, the causal-use question, rung, estimand, support basis, support verdict, supported use, and unsupported use **SHALL** be carried by `C.28`.


