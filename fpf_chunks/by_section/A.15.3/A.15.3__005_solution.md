---
chunk_kind: "child"
pattern_id: "A.15.3"
pattern_title: "SlotFillingsPlanItem"
section_id: "A.15.3:4"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/A.15.3/A.15.3__005_solution.md"
commit_sha: "fe0df9dcb06cfc87c8a6cb2f7cce3ac0d3b64d5e"
heading_path:
  - "A.15.3 — SlotFillingsPlanItem"
  - "A.15.3:4 — Solution"
line_start: 22069
line_end: 22223
dependencies:
  - "A.10"
  - "A.15.1"
  - "A.15.2"
  - "A.20"
  - "A.21"
  - "A.6.5"
  - "A.6.7"
  - "B.3"
  - "C.27.TA"
  - "E.10.D1"
  - "E.10.D2"
  - "E.17"
  - "E.18"
  - "E.18.1"
  - "E.19"
  - "E.20"
  - "G.11"
  - "G.6"
  - "U.RelationSlotDiscipline"
  - "U.Work"
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

### A.15.3:4 - Solution

#### A.15.3:4.1 - Definition

`SlotFillingsPlanItem` is a kind of `U.WorkPlan.PlanItem` whose content is one planned slot-filling baseline for one slot-bearing description in one bounded context.

It is:

- produced inside work planning;
- tied to one target description episteme that supplies SlotSpecs;
- pinned enough to replay what was planned;
- cited later by performed `U.Work` when variance, substitutions, launch values, telemetry, or result records are written.

It is not:

- the target slot-bearing description;
- a `MechanismDefinitionRef`;
- a gate decision, evidence item, assurance result, publication truth, or performed-work occurrence;
- a second slot ontology beside A.6.5.

#### A.15.3:4.2 - Core fields

A conforming `SlotFillingsPlanItem` states these fields when the corresponding claim is current:

1. **Plan identity**
   - `plan_item_id`
   - `kind = SlotFillingsPlanItem`
   - `work_plan_ref`
   - optional `plan_item_edition`

2. **Target slot-bearing description**
   - `target_slot_bearing_description_ref`
   - The target is a Description episteme that declares SlotSpecs, such as a suite description, kit description, method-description family, or other description governed by its own pattern.
   - Do not target `MechanismDefinitionRef` directly. If a mechanism-level baseline is needed, introduce or cite a description that exposes the slots being planned.
   - When the target description's SlotSpecs are edition-sensitive, the target ref is edition-pinned.

3. **EntityOfConcern and context**
   - `entity_of_concern_ref`
   - `bounded_context_ref`
   - optional `grounding_holon_ref` when the EntityOfConcern is not itself a holon and the current comparison or reference-plane claim needs grounding;
   - optional `reference_plane_ref` only when the governing measurement, CHR, or comparison pattern defines that field.

4. **Time selector or time rule**
   - `time_selector_ref` or `time_rule_ref`
   - Use this when "current", "latest", reproducibility, comparability, launch preparation, or source-currentness matters.
   - When time is required, use exactly one of the two forms; both-present and both-absent baselines are nonconforming.

5. **Planning scope refs**
   - optional `cg_frame_ref`, `p2w_carry_through_ref`, `publication_scope_ref`, `suite_ref`, or `kit_ref` when those relations are current;
   - these refs locate the planned baseline, but they do not add planned rows by themselves.

6. **Guard-preparation refs**
   - optional expected guard or policy refs, such as compare-guard or launch-guard preparation refs;
   - these refs name what later work or gate checks should be prepared to use;
   - the PlanItem records preparation, not the guard result.

7. **Evidence-reference pins**
   - optional concrete pin refs naming where evidence is expected to be placed or cited later;
   - a pin ref is not evidence and does not create evidence sufficiency.

8. **Crossing-preparation refs**
   - optional refs for expected cross-context or cross-plane support, such as BridgeCard refs, policy-id refs, reference-plane refs, or already-published CrossingBundle baseline refs;
   - these refs state expected crossing support only;
   - they are not crossing witnesses, do not embed CL/Phi/Psi tables, and do not claim that a crossing occurred.

9. **Authoritative planned-filling rows**
   - `planned_fillings[]`, each row with:
     - `row_id`;
     - `slot_kind`, taken from the target description's SlotSpecs;
     - `planned_filler`, written ByValue or ByRef with a concrete RefKind;
     - optional `edition_pin`;
     - optional `planning_note`.
   - If the target SlotSpec is single-valued, there is at most one row for that SlotKind.
   - If both a row and its referenced filler carry edition pins, they agree or the baseline is nonconforming.

10. **Derived projections**
   - optional cards, views, indices, or summaries;
   - each projection is derivable from `planned_fillings`;
   - any projection that adds rows, defaults, or semantics is a publication-use or view-use error under E.17.

11. **Variance policy**
   - how later performed `U.Work` cites this baseline;
   - how substitutions, missing fillers, extra fillers, launch values, or edition changes are recorded in the performed-work or gate relation.

#### A.15.3:4.3 - Compact record form

```text
SlotFillingsPlanItem:
  plan_item_id:
  kind: SlotFillingsPlanItem
  work_plan_ref:
  target_slot_bearing_description_ref:
  entity_of_concern_ref:
  bounded_context_ref:
  time_selector_ref or time_rule_ref:
  planning_scope_refs:
  guard_preparation_refs:
  evidence_reference_pins:
  crossing_preparation_refs:
  planned_fillings:
    - row_id:
      slot_kind:
      planned_filler:
      filler_mode: ByValue | ByRef(<ConcreteRefKind>)
      edition_pin:
      planning_note:
  derived_projection_refs:
  variance_policy:
```

#### A.15.3:4.4 - Relation to performed work

A `SlotFillingsPlanItem` is not a launch-value finalization witness and not a record that work occurred.

When a performed `U.Work` occurrence uses the baseline, the work record cites the PlanItem edition and records launch values, performed values, substitutions, missing planned fillers, extra fillers, telemetry, outcomes, and variance under A.15.1 or the governing gate, evidence, result, or archive pattern.

Do not backfill the plan to match what happened. If the plan changed before the work, create a new PlanItem edition or new PlanItem as appropriate. If the work differed from the plan, record variance in the performed-work relation.

#### A.15.3:4.5 - Relation to suites, kits, and mechanism introduction

A suite, kit, or mechanism-introduction pattern may require a planned-baseline ref. That requirement does not make the suite or mechanism text the baseline.

Use:

- the suite or kit pattern for the meaning of the suite or kit;
- A.6.5 for SlotSpec discipline inside the target description;
- A.15.3 for the plan instance that chooses planned fillers;
- A.15.1 for performed work and variance;
- `A.20` and `A.21`, `A.10` and `B.3`, or `E.17` when gate, evidence, assurance, or publication-use claims become current.

#### A.15.3:4.6 - Variants

Specialized PlanItem kinds are allowed only when the target governing pattern needs extra planned fields.

Example:

```text
CHRMechanismSuiteSlotFillingsPlanItem <: SlotFillingsPlanItem
  target_slot_bearing_description_ref = CHRMechanismSuiteDescriptionRef
  required_slots = {NormalizationMethodSlot, IndicatorPolicySlot, ComparatorSpecSlot}
```

The specialization may add fields needed by that suite, but it still inherits the WorkPlanning-only boundary: no performed-work actuals, no launch-value witnesses, no gate decisions, and no publication-view semantics.

#### A.15.3:4.7 - Local boundaries

| Source wording | A.15.3 recovery |
| --- | --- |
| "Use the latest spec" | Lower to a plan cue until time selector and edition-pinned target or filler refs are named. |
| "The mechanism uses this comparator" | Use the mechanism or suite pattern for mechanism meaning; use A.15.3 only if this is a planned filler for a plan instance. |
| "The card says the planned refs" | Use E.17 for the publication-use or view-use relation; the card is only a projection unless the PlanItem rows are present. |
| "The gate passed" | Use `A.20` and `A.21` or the gate pattern. The PlanItem can prepare refs for later gate use but does not pass the gate. |
| "Evidence pin" | Use A.15.3 only for the planned pin ref. Evidence-use and sufficiency are governed by `A.10`, `B.3`, `G.6`, or another governing evidence pattern. |
| "The work used different fillers" | Use A.15.1 for performed work and variance; do not rewrite the cited plan to erase the difference. |

