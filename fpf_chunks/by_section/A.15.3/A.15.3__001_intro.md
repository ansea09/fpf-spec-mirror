---
chunk_kind: "child"
pattern_id: "A.15.3"
pattern_title: "SlotFillingsPlanItem"
section_id: "A.15.3:intro"
section_title: "Intro"
source_path: "FPF-Spec.md"
output_path: "by_section/A.15.3/A.15.3__001_intro.md"
commit_sha: "cb17c555f343780e31e5fea236a74adc69295736"
heading_path:
  - "A.15.3 — SlotFillingsPlanItem"
  - "A.15.3:intro — Intro"
line_start: 21236
line_end: 21274
dependencies:
  - "A.15.1"
  - "A.15.2"
  - "A.6.5"
  - "A.6.7"
  - "E.10.D1"
  - "E.17"
  - "E.18"
  - "E.19"
  - "E.TGA"
  - "U.WorkPlan"
keywords:
  - "P2W seam"
  - "WorkPlanning"
  - "edition pins"
  - "guard pins"
  - "planned baseline"
  - "planned filler"
  - "slot-bearing description"
  - "variance trail"
  - "Γ_time selector"
---

## A.15.3 - SlotFillingsPlanItem

> **Tech-name:** `SlotFillingsPlanItem`
> **Plain-name:** planned slot-fillings baseline item (planned baseline)
> **Type:** Architectural (A)
> **Status:** Stable
> **Normativity:** Normative (unless explicitly marked informative)
> **Placement:** Part A → A.15 (Work & WorkPlanning)
> **Builds on:** `U.WorkPlan` (A.15.2), performed-work occurrence discipline (A.15.1 and E.TGA), Context discipline (E.10.D1), `MechSuiteDescription` (A.6.7), and publication/view discipline (E.17; views are projections, not places of meaning)
> **Used by:** planned-baseline requirements from suites or kits; P2W (selection -> WorkPlanning -> WorkEnactment); Part G universalization
> **Purpose (one line):** provide a universal, context-explicit **planned baseline** that maps a slot-bearing description's `SlotKind`s to **planned fillers**, to be consumed by Work enactment where launch values are finalized.

**At a glance.** Use `SlotFillingsPlanItem` when a `U.WorkPlan` needs a planned baseline saying which planned fillers will occupy which `SlotKind`s of one slot-bearing description before work is enacted.

**Use this when.** Use this pattern when planned references, policies, spec pins, method-description references, evidence pin refs, or crossing-policy pins must be fixed for a P2W work-planning slice, and the plan must stay distinct from launch values, gate decisions, evidence, and performed work.

**First output.** One `SlotFillingsPlanItem` with exactly one `target_slot_bearing_description_ref`, explicit `bounded_context_ref`, EntityOfConcern ref, time selector or time rule, authoritative planned-filling rows, and any expected guard, evidence, edition, or crossing pins needed before work enactment.

**Working action path.**
1. Name the slot-bearing description whose `SlotKind` set is being filled.
2. Name the EntityOfConcern and grounding holon or reference plane when needed.
3. Name context, time selector or time rule, and any P2W slice or publication scope needed for reproducibility.
4. Fill the authoritative rows by `SlotKind`, using ByValue or ByRef with concrete RefKinds and edition pins when needed.
5. Keep derived indices, views, guard pins, evidence pins, and crossing pins as projections or expectations; do not turn them into execution, gate, evidence, or launch-value claims.

**Ordinary use.** For a minimal baseline, context, time selector, target slot-bearing description, EntityOfConcern ref, and planned-filling rows are enough.

**Reliance-bearing use.** Use the fuller record when reproducibility, launch guard preparation, crossing expectations, suite or kit reuse, Part G universalization, or P2W carry-through depends on the baseline.

**Stop condition.** Stop once planned fillers are explicit enough for the intended WorkPlanning move, or lower the claim to a plan cue, source-gap note, relation governed by another FPF pattern, or blocked kind-definition gap without claiming a conforming planned baseline.

**Not this pattern when.** Not this pattern when the live object is the slot-bearing description itself, a mechanism definition, a performed-work occurrence, a gate decision, a launch-value witness, evidence, assurance, or a publication view. Use the corresponding governing pattern and return here only for the planned slot-filling baseline.

**Name and reference discipline (informative)**
* **Kind reuse:** This pattern uses the kind name `SlotFillingsPlanItem`. It reuses existing Core terms and disciplines (e.g., `U.WorkPlan.PlanItem`, SlotKind, ValueKind, RefKind, and refMode discipline, edition pinning, `U.BoundedContext`, and the P2W split between WorkPlanning and WorkEnactment).
* **`SlotFillingsPlanItem` (kind name):** keep the suffix `PlanItem` to preserve the WorkPlanning placement. Do not mint aliases like *SlotBinding…* (conflicts with the A.6.5 binding discipline) or *SlotValue…* (ambiguous slot-bearing description or context).
* **Anchor names:** if a §4.2 anchor is materialized as a formal field name, keep `…_ref` only for fields whose values are concrete RefKind handles, and keep `…_id` only for identifiers. Avoid introducing generic placeholders such as `SpecRef`, `PolicyRef`, or `GateRef` inside this pattern; use existing concrete ref kinds. When no concrete ref kind exists, the planned-baseline claim is blocked until a governing FPF pattern defines the kind.
* **Row vocabulary:** treat `SlotFillingRow` and `PlannedFiller` as internal names of this pattern. Do not treat them as shared tokens outside this pattern unless a governing FPF pattern defines them.

