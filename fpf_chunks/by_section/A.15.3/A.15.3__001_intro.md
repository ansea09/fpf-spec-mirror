---
chunk_kind: "child"
pattern_id: "A.15.3"
pattern_title: "SlotFillingsPlanItem"
section_id: "A.15.3:intro"
section_title: "Intro"
source_path: "FPF-Spec.md"
output_path: "by_section/A.15.3/A.15.3__001_intro.md"
commit_sha: "9a9c1b14df894386c664cf49a9ccbbd4a4063100"
heading_path:
  - "A.15.3 — SlotFillingsPlanItem"
  - "A.15.3:intro — Intro"
line_start: 25853
line_end: 25891
dependencies:
  - "A.15.1"
  - "A.15.2"
  - "A.15.5"
  - "A.6.1"
  - "A.6.5"
  - "A.6.RCD"
  - "C.2.1"
  - "E.17"
  - "E.24.PUB"
  - "U.WorkPlan"
keywords:
  - "WorkPlan claim content"
  - "actual-use predicate"
  - "baseline replay"
  - "concrete RefKind and policy"
  - "direct owner"
  - "edition pin"
  - "exact declaration member"
  - "intended-performance designator"
  - "no actuality by plan"
  - "open-world omission"
  - "participant/argument/result meaning"
  - "positive planned designation"
  - "semantic cardinality"
---

## A.15.3 - SlotFillingsPlanItem

> **Tech-name:** `SlotFillingsPlanItem`
> **Plain-name:** planned-filling plan item
> **Short code:** `SFPI`
> **Type:** WorkPlanning pattern
> **Status:** Stable
> **Normativity:** Normative unless explicitly marked informative
> **Placement:** Part A -> A.15 work family
> **Builds on:** `C.2.1` episteme identity, `A.15.2 U.WorkPlan`, `A.6.5` relation-declaration SlotSpec discipline, `A.6.1` operation declarations, and the pattern that defines any other target member
> **Used by:** plans that must remember a chosen future relation participant, operation argument, expected result, or another value tied to an already declared member before work begins
> **One-line purpose:** record inside one `U.WorkPlan` which value is intended for one already declared member; the declaration defines how later actual use is judged, while A.15.3 records only the intention and makes nothing actual.

**At a glance.** Use `SlotFillingsPlanItem` when a plan must preserve a concrete choice before Work begins—for example, `Robot_8_Ref` as the planned holder for a future system-role assignment, with the assignment species named separately, or `Pump_37_Ref` as the planned `candidate` in a recognition operation. Point to the declaration member that already defines that position, record the planned value and conditions, and later compare them with what actually happened without rewriting the plan. A field name, compatible type, Method phrase, form position, or plan label is not such a declaration.

**Use this when.** Use this pattern only when the choice points to a member already defined in a `RelationSignature`, an A.6.1 `OperationDeclaration`, or another declaration whose own pattern states both the member's meaning and the rule for its later actual use. If the plan merely says *use this method*, *reserve this resource*, or *meet this threshold* without reusing such a member, keep ordinary A.15.2 plan content. A planned row establishes no dated work, relation participant, operation application, returned value, change, delivery, or outcome.

**First useful object.** One `PlanItem` inside an identified `U.WorkPlan` with at least one row that names the intended future use, declaration edition, declaration-local member, planned value or designation, and the conditions under which that choice applies. The row follows the member's designation rule and semantic cardinality; it does not redefine either.

**Working use order.**

1. Identify the `U.WorkPlan` edition and the future performance being planned. Keep the WorkPlan's already identified present EntityOfConcern unchanged.
2. Open the declaration that will be used later and choose one member it actually defines. Verify that the declaration's own pattern states both what that member means and what must hold for actual use.
3. Record the declaration edition, its local member designator, and the planned value or designation. Do not substitute a description, record, form field, or matching label.
4. Apply the member's ValueKind, designation rule, and semantic cardinality. Add conditions and edition pins only when they can change which planned value is effective. State prohibitions, exclusions, and completeness as separate plan claims; omission is not prohibition.
5. When the later use occurs, identify the dated work and each actual participant or binding independently. Compare actual with planned under a stated comparison policy; preserve the cited plan instead of backfilling it.

**Ordinary use.** One row is enough: declaration edition, member designator, planned value or designation, and the condition under which it is intended. The declaration's own pattern must already define the member and its later actual-use rule.

**Reliance-bearing use.** Add concrete reference kinds, declaration or value edition pins, alternative-selection conditions, target-declared cardinality, and a later comparison policy only when coordination, replay, audit, or work-entry preparation would change without them.

**Stop condition.** Finish with one of three results. (1) The row resolves to an existing declaration member, and the planned value meets its ValueKind, designation, cardinality, and condition rules. (2) No reusable member is needed, so the choice stays ordinary A.15.2 plan content. (3) Typed reuse is needed but the member, its meaning, its actual-use rule, or the pattern that defines them is missing; return `missing-governor` for that planned use. Do not invent a SlotSpec, wrapper declaration, generic field, or actual-use relation here.

**What goes wrong if missed.** A plan silently turns method prose or a schema field into a slot, treats type compatibility as planned or actual participation, treats omission or an empty filler as a prohibition, or later edits the baseline to match what happened.

**What this buys.** The team can later say what it intended, what actually happened, and whether the two differ, while the declaration, plan, work, and actual participation remain separate objects.

**Not this pattern when.** Use the exact declaration predicate and ClaimGraph located through `A.6.5`, `A.6.1`, or another declared-member source when defining the member; use A.15.2 for ordinary intended work without a planned filling; use A.15.1 for dated work; and use the exact applicable predicates for actual relation participation, operation bindings, methods, evidence, assurance, gates, acceptance, results, publication, or representation.

