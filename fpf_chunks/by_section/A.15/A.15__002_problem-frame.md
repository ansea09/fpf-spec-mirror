---
chunk_kind: "child"
pattern_id: "A.15"
pattern_title: "Role–Method–Work Alignment"
section_id: "A.15:1"
section_title: "Problem frame"
source_path: "FPF-Spec.md"
output_path: "by_section/A.15/A.15__002_problem-frame.md"
commit_sha: "1602a8d0a6934a99a79ead914610b070cedd86d2"
heading_path:
  - "A.15 — Role–Method–Work Alignment"
  - "A.15:1 — Problem frame"
line_start: 24007
line_end: 24023
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

In any complex system, from a software project to a biological cell, there is a fundamental distinction between **what something is** (its structure), **which role a holder is assigned under an exact role-taxonomy episteme and effective reference scheme** (`U.Role` and `U.RoleAssignment`), **how work is done** (`U.Method` and `U.MethodDescription`), **which holder `U.Capability` instance is relied on** (`A.2.2`), **which statement, evidence relation, or currentness assessment supports that reliance**, **which separate capability-fit, threshold, gate, or admission check is applied when fit is current**, **what work is intended** (`U.WorkPlan`), **which world-side dated Work occurrence happened** (an individual admitted under `U.Work`), and **which separate assertion or record describes it**. Confusing these distinctions is a primary source of design flaws, budget overruns, and failed projects. Teams argue over encountered "process" wording without clarifying whether the FPF object under repair is a `U.Method`, a `U.MethodDescription`, a holder `U.Capability` instance, a statement about that instance, a separate capability-fit condition, a `U.WorkPlan`, an actual Work occurrence, or an episteme about that occurrence.

This pattern provides the canonical role-method-work enactment alignment in FPF. It applies the **Strict Distinction Principle (A.7)** to the passage from holder-in-role assignment and selected method to intended `U.WorkPlan`, an actual Work occurrence admitted under `U.Work`, and any separate episteme about it, without making A.15 the whole strict-distinction ontology. It brings the current relations together in a single, coherent model:
*   **A.2 and A.2.1:** Provide enactment-facing `U.Role` values and `U.RoleAssignment` as the typed assignment relation with exactly four generic participants: holder `U.System`, `U.Role`, exact role-taxonomy episteme, and effective `U.ReferenceScheme`. The actual assignment extent is the maximal continuous interval over which that relation obtains; declared windows and justification or source claims remain assertion or description content.
*   **A.15.2 and A.15.1:** Separate `U.WorkPlan` intent from actual dated Work occurrences admitted under `U.Work`, and separate both from assertions or records that designate them.
*   **A.3.1 and A.3.2:** Separate `U.Method` from `U.MethodDescription`, so recipes, algorithms, procedures, and encountered "process" wording do not become performed work by word choice.
*   **A.3.4:** Provides `U.Transformation` for bounded change under conditions when the actual change, affected entity, pre/post state, mechanism, method, or work relation is current.
*   **A.10, C.2.1, and E.17:** Keep evidence relations, source relations, publication relations, and carrier relations outside the work-facing role assignment unless a system or acting holon is actually assigned a role for performed work.

The intent of this pattern is to establish a normative, unambiguous vocabulary and set of relations for connecting holder-in-role assignment, recovered method, method-description reference, holder `U.Capability` instances when relied on, separate capability statements or currentness assessments when those are used, separate capability-fit conditions when current, intended work plan, actual dated resource-consuming Work occurrences admitted under `U.Work`, and separate epistemes about them.

To keep plan-occurrence separation explicit, this pattern references **A.15.2 `U.WorkPlan`** for **schedules and calendars** and **A.15.1** for admission under **`U.Work`** and identification of dated Work individuals. For ambiguous project terms such as "process", "workflow", "activity", and "schedule", use `E.10` and `E.10.ARCH`: recover the object under wording repair first, then assign the wording to `U.Method`, `U.MethodDescription`, `U.WorkPlan`, the `U.Work` kind or one Work individual admitted under it, or the pattern that defines or tests the other claim.

**Terminology note.** The words _action_ and _activity_ are not normative kernel names by themselves. When a generic "doing" cue appears, recover the FPF object or kind being claimed: **`U.Method`**, **`U.MethodDescription`**, **`U.WorkPlan`**, one Work individual admitted under **`U.Work`** or the kind itself when kind-level classification is current, or a value defined elsewhere such as `U.Transformation`, `U.Dynamics`, an evidence relation, gate relation, source relation, or publication use.

