---
chunk_kind: "child"
pattern_id: "A.15"
pattern_title: "Role–Method–Work Alignment (Contextual Enactment)"
section_id: "A.15:1"
section_title: "Problem frame"
source_path: "FPF-Spec.md"
output_path: "by_section/A.15/A.15__002_problem-frame.md"
commit_sha: "c092a1f2299d88d42db012f3184aeff205c13219"
heading_path:
  - "A.15 — Role–Method–Work Alignment (Contextual Enactment)"
  - "A.15:1 — Problem frame"
line_start: 20660
line_end: 20674
dependencies:
  - "A.10"
  - "A.12"
  - "A.15.1"
  - "A.15.1-A.15.4"
  - "A.15.4"
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
  - "E.16"
  - "E.17"
  - "E.17.EFP"
keywords:
  - "U.Method"
  - "U.MethodDescription"
  - "U.Role"
  - "U.WorkPlan"
  - "actual U.Work"
  - "contextual enactment"
  - "coordinated-work evidence"
  - "role-method-work distinction"
  - "source-restoration boundary"
  - "work admission display"
---

### A.15:1 - Problem frame

In any complex system, from a software project to a biological cell, there is a fundamental distinction between **what something is** (its structure), **what it is supposed to do** (its role and specified capability), and **what it actually does** (its work). Confusing these distinctions is a primary source of design flaws, budget overruns, and failed projects. Teams argue over a source-side "process" cue without clarifying whether the FPF object under repair is a `U.Method`, a `U.MethodDescription`, a `U.Capability`, a `U.WorkPlan`, or a specific `U.Work` occurrence that happened last Tuesday.

This pattern provides the canonical alignment for modeling contextual enactment in FPF, serving as the ultimate implementation of the **Strict Distinction Principle (A.7)**. It weaves together several foundational concepts into a single, coherent model of how intended work becomes planned and actual `U.Work`:
*   **A.2 (Contextual Role Assignment):** Provides the `Holder#Role:Context` structure for assigning roles.
*   **A.4 (Temporal Duality):** Provides the strict separation between `design-time` and `run-time`.
*   **A.12 (External Transformer):** Ensures that performed `U.Work` is attributed to a transformer-bearing system acting under a `U.RoleAssignment`.

The intent of this pattern is to establish a normative, unambiguous vocabulary and set of relations for describing the passage from role and method capability to planned and actual, resource-consuming `U.Work`.

To keep plan-run separation explicit, this pattern references **A.15.2 `U.WorkPlan`** for **schedules and calendars** and **A.15.1 `U.Work`** for **dated execution**. Ambiguous source terms like "process", "workflow", and "schedule" are constrained by **L-PROC**, **L-FUNC**, and **L-SCHED** (E-cluster): a _workflow_ cue normally resolves to `U.MethodDescription` unless the abstract way-of-doing itself is being claimed as `U.Method`; a _schedule_ cue resolves to `U.WorkPlan`; what _happened_ resolves to `U.Work`.

**Terminology note (L-ACT).** The words _action_ and _activity_ are **not normative** in the kernel. When a generic "doing" is needed, we use the didactic term **enactment** (not a type). Normative references must be to **`U.Method`**, **`U.MethodDescription`**, **`U.Work`**, or **`U.WorkPlan`**. See lexical rules **L-PROC**, **L-FUNC**, **L-SCHED**, and **L-ACT**.

