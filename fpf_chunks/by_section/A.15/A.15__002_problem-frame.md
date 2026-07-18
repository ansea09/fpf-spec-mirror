---
chunk_kind: "child"
pattern_id: "A.15"
pattern_title: "Role–Method–Work Alignment (Contextual Enactment)"
section_id: "A.15:1"
section_title: "Problem frame"
source_path: "FPF-Spec.md"
output_path: "by_section/A.15/A.15__002_problem-frame.md"
commit_sha: "1d5c1edd154b636a446b3887a6094be60c60faff"
heading_path:
  - "A.15 — Role–Method–Work Alignment (Contextual Enactment)"
  - "A.15:1 — Problem frame"
line_start: 22064
line_end: 22080
dependencies:
  - "A.10"
  - "A.12"
  - "A.15"
  - "A.15.1-A.15.5"
  - "A.15.4"
  - "A.15.5"
  - "A.2"
  - "A.20"
  - "A.21"
  - "A.4"
  - "A.6"
  - "A.6.B"
  - "A.6.C"
  - "B.3"
  - "C.24"
  - "C.26.2"
  - "C.28"
  - "C.29"
  - "C.32.P2S"
  - "E.10"
  - "E.10.ARCH"
  - "E.16"
  - "E.17"
  - "E.17.EFP"
  - "E.18.1"
keywords:
  - "U.Method"
  - "U.MethodDescription"
  - "U.Role"
  - "U.WorkPlan"
  - "actual U.Work"
  - "appearance-based reliance boundary"
  - "contextual enactment"
  - "coordinated-work evidence"
  - "role-method-work distinction"
  - "work admission display"
  - "work-entry readiness"
---

### A.15:1 - Problem frame

In any complex system, from a software project to a biological cell, there is a fundamental distinction between **what something is** (its structure), **what a holder is being in context** (role value and `U.RoleAssignment`), **how work is done** (`U.Method` and `U.MethodDescription`), **which holder `U.Capability` instance is relied on** (`A.2.2`), **which statement, evidence relation, or currentness assessment supports that reliance**, **which separate capability-fit, threshold, gate, or admission check is applied when fit is current**, **what work is intended** (`U.WorkPlan`), and **what dated work occurred** (`U.Work`). Confusing these distinctions is a primary source of design flaws, budget overruns, and failed projects. Teams argue over encountered "process" wording without clarifying whether the FPF object under repair is a `U.Method`, a `U.MethodDescription`, a holder `U.Capability` instance, a statement about that instance, a separate capability-fit condition, a `U.WorkPlan`, or a specific `U.Work` occurrence that happened last Tuesday.

This pattern provides the canonical alignment for modeling contextual enactment in FPF. It applies the **Strict Distinction Principle (A.7)** to the passage from holder-in-role assignment and selected method to intended `U.WorkPlan` and dated performed `U.Work`, without making A.15 the whole strict-distinction ontology. It weaves together current governing relations into a single, coherent model:
*   **A.2 and A.2.1:** Provide enactment-facing `U.Role` values and `U.RoleAssignment` as the typed assignment relation with holder, role, bounded-context, window, and justification slots governed through A.6.5-style slot discipline.
*   **A.15.2 and A.15.1:** Separate `U.WorkPlan` intent windows from dated `U.Work` occurrences.
*   **A.3.1 and A.3.2:** Separate `U.Method` from `U.MethodDescription`, so recipes, algorithms, procedures, and encountered "process" wording do not become performed work by word choice.
*   **A.3.4:** Provides `U.Transformation` for bounded change under conditions when the actual change, affected entity, pre/post state, mechanism, method, or work relation is current.
*   **A.10, C.2.1, and E.17:** Keep evidence relations, source relations, publication relations, and carrier relations outside the work-facing role assignment unless a system or acting holon is actually assigned a role for performed work.

The intent of this pattern is to establish a normative, unambiguous vocabulary and set of relations for connecting holder-in-role assignment, recovered method, method-description reference, holder `U.Capability` instances when relied on, separate capability statements or currentness assessments when those are used, separate capability-fit conditions when current, intended work plan, and dated resource-consuming `U.Work`.

To keep plan-occurrence separation explicit, this pattern references **A.15.2 `U.WorkPlan`** for **schedules and calendars** and **A.15.1 `U.Work`** for **dated execution**. Ambiguous terms in project material, such as "process", "workflow", "activity", and "schedule", are handled by `E.10` and `E.10.ARCH`: recover the object under wording repair first, then assign the wording to `U.Method`, `U.MethodDescription`, `U.WorkPlan`, `U.Work`, or another direct governing pattern.

**Terminology note.** The words _action_ and _activity_ are not normative kernel names by themselves. When a generic "doing" cue appears, recover the FPF kind being claimed: **`U.Method`**, **`U.MethodDescription`**, **`U.Work`**, **`U.WorkPlan`**, or a neighboring governed value such as `U.Transformation`, `U.Dynamics`, evidence relation, gate relation, source relation, or publication use.

