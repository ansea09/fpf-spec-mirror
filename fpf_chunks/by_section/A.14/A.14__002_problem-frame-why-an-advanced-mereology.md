---
chunk_kind: "child"
pattern_id: "A.14"
pattern_title: "Advanced Mereology: Components, Portions, Aspects & Phases"
section_id: "A.14:1"
section_title: "Problem frame - why an advanced mereology?"
source_path: "FPF-Spec.md"
output_path: "by_section/A.14/A.14__002_problem-frame-why-an-advanced-mereology.md"
commit_sha: "792091cf6f89f21f3423d75c72238bb0982777f2"
heading_path:
  - "A.14 — Advanced Mereology: Components, Portions, Aspects & Phases"
  - "A.14:1 — Problem frame - why an advanced mereology?"
line_start: 20579
line_end: 20595
dependencies:
  - "A.1"
  - "A.15"
  - "A.15.1"
  - "A.3.1"
  - "A.3.2"
  - "A.3.4"
  - "A.7"
  - "B.1"
  - "B.1.1"
  - "B.2"
  - "B.3.5"
  - "C.13"
keywords:
  - "ComponentOf"
  - "PhaseOf"
  - "PortionOf"
  - "composition"
  - "mereology"
  - "part-of"
---

### A.14:1 - Problem frame - why an advanced mereology?

FPF’s holonic modelling relies on **part–whole** relations to build *structural* and *conceptual* holarchies for admitted holons such as systems, epistemes, work occurrences, bounded contexts, and disciplines. But `U.Holon` is **not** a synonym for every bounded object. `U.Role` and `U.Method` are governed FPF values with their own relation discipline; they are not admitted holon kinds merely because source speech treats them as "things." Role relation structures, method relation structures, method descriptions, work plans, and work occurrences enter A.14 only through their direct governing patterns and admitted carriers. Early drafts distinguished structural vs. conceptual parthood (e.g., **ComponentOf**, **ConstituentOf**) but practical modelling kept hitting two recurrent gaps:

1. **Quantities vs. parts.** Engineers routinely need “some of the fuel”, “the first 10 pages”, “a 30% subset of data”. This is not a component; it is a **portion** of a stuff‑like whole, governed by measures and conservation.

2. **Change vs. replacement.** Authors need to say “the prototype **before calibration**”, “v2 of the spec”, “shift 1 vs. shift 2 of the same run”. That is not a new whole; it is a **phase** of the same carrier across time.

This section introduces two **normative** sub‑relations of `partOf` that close those gaps and lock them to the rest of the kernel:

* **PortionOf** — metrical, measure‑preserving parthood of stuffs and other measurables.
* **PhaseOf** — temporal parthood of the *same* carrier across an interval.

It also restates guard‑rails that keep **role values** and **method values** outside A.14 mereology, while allowing **describing epistemes** such as `U.MethodDescription` and `U.WorkPlan` to use ordinary episteme parthood and versioning like any other `U.Episteme`. It also clarifies how **MemberOf** fits: membership and collection-as-whole grounding start with A.14, C.13, and B.3.5 as appropriate; acting collective systems require `U.System` admission plus role, method, work, and evidence owners; whole reidentification uses B.2 only when existing-whole explanations fail.

**Publication note (Working-Model first).** Read A.14 together with **E.14 Human-Centric Working-Model** and **B.3.5 CT2R-LOG**: publish relations in the **Working-Model** relation layer; when assurance is sought, **ground downward**. For structural claims that require extensional identity, use the **Constructive** shoulder via **Compose-CAL Γ_m (sum | set | slice)**; order/time stay outside mereology (Γ_time / Γ_method).

