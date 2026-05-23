---
chunk_kind: "child"
pattern_id: "A.15.3"
pattern_title: "SlotFillingsPlanItem"
section_id: "A.15.3:intro"
section_title: "Intro"
source_path: "FPF-Spec.md"
output_path: "by_section/A.15.3/A.15.3__001_intro.md"
commit_sha: "04dd733fb18b66d3a640d11758e0af22ea253fd8"
heading_path:
  - "A.15.3 — SlotFillingsPlanItem"
  - "A.15.3:intro — Intro"
line_start: 20424
line_end: 20441
dependencies:
  - "A.15.1"
  - "A.15.2"
  - "A.6.5"
  - "A.6.7"
  - "E.10.D1"
  - "E.17"
  - "E.18"
  - "E.19"
  - "E.8"
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
> **Builds on:** pattern template (E.8), `U.WorkPlan` (A.15.2), Work enactment discipline (A.15.1 / TGA), Context discipline (E.10.D1), `MechSuiteDescription` (A.6.7), conformance discipline (E.19), publication/view discipline (E.17; views are projections, not places of meaning)
> **Used by:** planned-baseline requirements from suites/kits; P2W (selection → WorkPlanning → WorkEnactment); Part G universalization
> **Purpose (one line):** provide a universal, context-explicit **planned baseline** that maps a slot-bearing description's `SlotKind`s to **planned fillers**, to be consumed by Work enactment where launch values are finalized.

**Minting notes (informative)**
* **Mint vs reuse:** This pattern mints the kind name `SlotFillingsPlanItem`. It reuses existing Core terms and disciplines (e.g., `U.WorkPlan.PlanItem`, SlotKind/ValueKind/RefKind/refMode discipline, edition pinning, `U.BoundedContext`, and the P2W split between WorkPlanning and WorkEnactment).
* **`SlotFillingsPlanItem` (kind name):** keep the suffix `PlanItem` to preserve the WorkPlanning placement. Do not mint aliases like *SlotBinding…* (conflicts with the A.6.5 binding discipline) or *SlotValue…* (ambiguous slot-bearing description or context).
* **Anchor names:** if any anchors in §4.2 are later materialized as formal field names, keep `…_ref` only for fields whose values are concrete RefKind handles, and keep `…_id` only for identifiers. Avoid introducing generic placeholders like `SpecRef/PolicyRef/GateRef` inside this pattern; prefer existing concrete ref kinds (or a dedicated DRR+LEX step).
* **Row vocabulary:** treat `SlotFillingRow` and `PlannedFiller` as *internal* names of this pattern unless/until a separate DRR+LEX step promotes them to shared tokens.

