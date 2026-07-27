---
chunk_kind: "child"
pattern_id: "A.15.3"
pattern_title: "SlotFillingsPlanItem"
section_id: "A.15.3:intro"
section_title: "Intro"
source_path: "FPF-Spec.md"
output_path: "by_section/A.15.3/A.15.3__001_intro.md"
commit_sha: "60caecb4751fb2a3623a1faaca757d29a19acff9"
heading_path:
  - "A.15.3 — SlotFillingsPlanItem"
  - "A.15.3:intro — Intro"
line_start: 25108
line_end: 25146
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
> **Builds on:** `C.2.1` episteme identity, `A.15.2 U.WorkPlan`, `A.6.5` relation-declaration SlotSpec discipline, `A.6.1` operation declarations, and the direct pattern governing any other target declaration
> **Used by:** intended-work planning that must preserve exact desired participant, operation-argument, operation-result, or other explicitly governed declaration choices before performed work occurs
> **One-line purpose:** state a positive planned designation against one exact governed declaration member whose direct pattern owns the member's reusable participant, argument, or result meaning and corresponding later actual-use predicate; A.15.3 owns only the planning intention and makes nothing actual.

**At a glance.** Use `SlotFillingsPlanItem` when one exact `U.WorkPlan` must say that a future work use is intended to supply a particular value or designation under an exact declared participant, argument, or result meaning. The target's direct pattern owns that reusable meaning and its corresponding later actual-use predicate; A.15.2 and A.15.3 own the intended-use claim. A broad field name, compatible value kind, meaning-only declaration, method-description phrase, schema position, or plan label is not enough.

**Use this when.** Use this pattern when intended work depends on a planned participant designation for one `RelationSignature` SlotSpec, a planned value or designation for one A.6.1 `ArgumentDeclaration` or `ResultDeclaration`, or a planned filling for another exact declaration member whose direct pattern explicitly owns the member's reusable meaning and corresponding later actual-use predicate. The item preserves what was intended; it establishes no dated work, actual relation participant, operation application, returned value, change, result, delivery, or outcome.

**First useful object.** One `PlanItem` content component inside an exact `U.WorkPlan`, containing at least one planned-filling row whose intended-performance designator, target declaration edition, declaration-local member designator, direct owner of the member meaning and corresponding actual-use predicate, planned value or designation, effective designation rule, semantic cardinality, and planning conditions are recoverable.

**Working use order.**

1. Identify the exact `U.WorkPlan` edition, its already identified present EntityOfConcern, and the intended-performance designator under A.15.2.
2. For each planned filling, recover one exact declaration member and the direct pattern that owns the member's reusable participant, argument, or result meaning and corresponding later actual-use predicate.
3. Point to one exact declaration edition and one declaration-local member designator; do not point to a description or record merely because it displays an input, output, role, field, or slot.
4. State the positive planned value or designation under that member's declared ValueKind, designation rule, semantic cardinality, and exact planning conditions. Keep exclusions, prohibitions, and completeness claims as separately governed plan claims.
5. At later use, identify any dated work and every actual participant or binding independently under their direct patterns. Compare actual and planned claims without rewriting the plan.

**Ordinary use.** One row with an exact declaration reference, exact member designator, exact direct owner of the member meaning and corresponding actual-use predicate, positive planned value or designation, and the condition under which it is intended is enough.

**Reliance-bearing use.** Add declaration-edition pins, value-edition pins when the value is edition-bearing, concrete reference kinds, target-declared cardinality or alternative-selection conditions, and an exact later comparison policy only when coordination, replay, audit, or work-entry preparation depends on them.

**Stop condition.** Stop when every relied-on row resolves to one exact governed declaration member whose direct pattern owns the member's reusable meaning and corresponding later actual-use predicate, while A.15.3 supplies only the intended-use claim. If no reusable declaration member is needed, retain the choice as ordinary A.15.2 plan content. If a planned filling is needed but the declaration member, reusable meaning, corresponding actual-use predicate, or their direct owner is missing, record the exact missing-governor blocker; do not manufacture a SlotSpec, description wrapper, generic field declaration, or actual-use relation in this pattern.

**What goes wrong if missed.** A plan silently turns method prose or a schema field into a slot, treats type compatibility as planned or actual participation, treats omission or an empty filler as a prohibition, or later edits the baseline to match what happened.

**What this buys.** A compact, replayable account of what exact declaration use was intended, while declaration semantics, plan content, dated work, and actual participation remain independently recoverable.

**Not this pattern when.** Not this pattern when the current object is the declaration itself (`A.6.5`, `A.6.1`, or its direct pattern), an ordinary intended-work claim with no planned filling (`A.15.2`), dated performed work (`A.15.1`), an actual relation participant or operation-application binding, a method or method description (`A.3.1` or `A.3.2`), evidence or assurance (`A.10` or `B.3`), a gate or acceptance verdict, a result episteme, publication use, or a representation field.

