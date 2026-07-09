---
chunk_kind: "child"
pattern_id: "A.15.3"
pattern_title: "SlotFillingsPlanItem"
section_id: "A.15.3:4"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/A.15.3/A.15.3__005_solution.md"
commit_sha: "d77339d7056433de3ee55ad863860ee4b3006f6f"
heading_path:
  - "A.15.3 — SlotFillingsPlanItem"
  - "A.15.3:4 — Solution"
line_start: 22688
line_end: 22880
dependencies:
  - "A.10"
  - "A.15.1"
  - "A.15.2"
  - "A.15.5"
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
  - "E.24"
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

#### A.15.3:4.0 - Planned slot-filling ontic

`A.15.3` governs the planned slot-filling ontic: a bounded planning relation in which one `U.WorkPlan.PlanItem` states which planned fillers are intended for which SlotKinds of one slot-bearing description before performed work occurs.

Keep three levels distinct:

- the planned slot-filling ontic: the E.24 ontic-level SlotRelation architecture for planned fillers of SlotKinds before performed work;
- `SlotFillingsPlanItem`: one filled `U.WorkPlan.PlanItem` value over that ontic for one bounded planning use;
- a card, table, view, schema, checklist, or document that publishes or projects a `SlotFillingsPlanItem` value.

By E.24 and E.24.UK, this is not an ontic without a kind settlement. The selected settlement reuses the root `U.WorkPlan` U-kind and admits `SlotFillingsPlanItem` as a dependent durable plan-item U-kind within `U.WorkPlan`; its filled instances are values inside a `U.WorkPlan`. The planned slot-filling ontic is the ontic-level SlotRelation that gives that dependent U-kind its identity and filler discipline. It does not introduce an independent root U-kind, a C.3 subkind claim, or a publication form. The stable identity is the planned-baseline relation among one work plan, one target slot-bearing description edition, one EntityOfConcern, one bounded context, one time selector or time rule when required, and one planned-filling row set. Changing the planned baseline before work creates a new PlanItem edition or a new PlanItem; performed-work variance does not rewrite the cited baseline.

The ontic keeps these objects distinct:

- `SlotFillingsPlanItem`: the dependent plan-item U-kind in this settlement; a filled value lives inside a `U.WorkPlan`, and the dependent U-kind does not introduce an independent root U-kind, the ontic-level SlotRelation itself, or a second slot ontology.
- `target_slot_bearing_description_ref`: the Description episteme whose SlotSpecs supply the SlotKinds being planned.
- `planned_fillings[]`: the row set that connects each selected SlotKind to a planned filler, filler mode, and edition pin when current.
- preparation refs: guard, evidence-reference, crossing-policy, time, context, or source-currentness refs that prepare later work without becoming evidence, a gate decision, or performed work.
- performed-work variance relation: the later `U.Work`, gate, evidence, result, archive, or variance relation that states what happened against the cited baseline.

Ontic-level `onticSlotRelation`:

| Slot group | Required or optional-in-use | Filler discipline |
| --- | --- | --- |
| Plan identity | Required | `plan_item_id`, `kind = SlotFillingsPlanItem`, `work_plan_ref`, and optional `plan_item_edition`; governed by `A.15.2` and this pattern. |
| Target slot-bearing description | Required | One Description episteme that exposes SlotSpecs; governed by the target description pattern and `A.6.5`. |
| EntityOfConcern, context, and time | Required for a conforming baseline | `entity_of_concern_ref`, `bounded_context_ref`, and `time_selector_ref` or `time_rule_ref` when reproducibility, currentness, or comparison depends on time. |
| Planned-filling rows | Required | Each row names a SlotKind from the target description, planned filler, ByValue or concrete RefKind mode, and edition pin when current; filler values keep their own governing patterns. |
| Preparation refs | Optional-in-use | Guard, readiness-preparation, evidence-reference, crossing-policy, source-currentness, bridge, or refresh refs; they prepare later relations but do not become `WorkEntryReadiness@Context`, gate decisions, evidence sufficiency, crossings, or performed work. |
| Derived projections | Optional-in-use | Cards, records, tables, views, indices, or summaries are E.17 publication or view-use projections; they are not the ontic and not row authority. |
| Variance policy | Required for reliance-bearing use | Names how later `U.Work`, gate, evidence, result, archive, or variance relations cite the baseline and record substitutions, missing fillers, extra fillers, launch values, or edition changes. |

A conforming instance fills only the slots that are current to the planning claim. Optional refs stay absent when the project does not rely on them. The open-world assumption is preserved: not writing an optional planned filler does not say that no such project value exists; it only says the current planned-baseline claim does not rely on it.

Use this ontic whenever a suite, kit, comparison, selector, archive, refresh, work-entry-readiness check, or P2W carry-through needs project-specific editions, policy ids, evidence-reference pins, bridge ids, method-description refs, or other planned fillers. Use the neighboring governing pattern when the current object is mechanism meaning, comparison result, selection result, work-entry readiness, performed work, evidence, gate passage, publication-use, source-currentness, or refresh.

This ontic is selected because dependent patterns need a shared settlement. Without it, suite, comparison, selector, archive, refresh, and P2W patterns would each invent a local baseline field, a local planned-pin phrase, or a local warning that planned values are not performed values. With this ontic, they cite `A.15.3` and keep their own EoC thin.

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
   - optional refs for expected cross-context or cross-plane bridge or crossing relations, such as BridgeCard refs, policy-id refs, reference-plane refs, or already-published CrossingBundle baseline refs;
   - these refs state expected bridge or crossing relations only;
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

