---
chunk_kind: "child"
pattern_id: "A.15.3"
pattern_title: "SlotFillingsPlanItem: Plan a Value for an Existing Declaration Member"
section_id: "A.15.3:7"
section_title: "Conformance Checklist"
source_path: "FPF-Spec.md"
output_path: "by_section/A.15.3/A.15.3__008_conformance-checklist.md"
commit_sha: "c475118bc1c11d2921b14f74c876e69c24ced3ea"
heading_path:
  - "A.15.3 — SlotFillingsPlanItem: Plan a Value for an Existing Declaration Member"
  - "A.15.3:7 — Conformance Checklist"
line_start: 30151
line_end: 30169
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

### A.15.3:7 - Conformance Checklist

| ID | Requirement | Practical test |
| --- | --- | --- |
| CC-A15.3-01 | The item is declaration-local WorkPlan content. | Its designator resolves inside one cited WorkPlan episteme; no independent PlanItem identity or row authority is claimed. |
| CC-A15.3-02 | The WorkPlan keeps its already identified present EntityOfConcern; the item separately names the future performance being planned. | Use the intended-performance designator as plan content; the EntityOfConcern resolves to the already identified present subject. |
| CC-A15.3-03 | Every row points to one declaration episteme and member whose pattern defines both member meaning and actual-use predicate. | The declaration reference, local member designator, family, defining pattern, and predicate route all resolve; A.15.3 states only the intention. |
| CC-A15.3-04 | Relation rows use only conforming A.6.5 SlotSpecs inside cited `RelationSignature` epistemes. | Resolve `HolderSystemSlot` inside the particular species signature, including its predicate and participant meanings; the Robot_8 row in §5.1 awaits that declaration. Hypothetical `PartHolonSlot` and `WholeHolonSlot` retain their named blocker. |
| CC-A15.3-05 | Operation rows use A.6.1 argument or result declarations. | Mechanism episteme, operation designator, member designator, ValueKind, designation rule, binding predicate, and cardinality resolve together. |
| CC-A15.3-06 | Any other target has a pattern that explicitly defines it. | Missing member meaning, actual-use predicate, or defining pattern yields `missing-governor`, not a generic target. |
| CC-A15.3-07 | The planned value follows the member's ValueKind, designation rule, and cardinality. | A single-valued target has at most one effective planned value; conditions and a resolution rule select among alternatives, while multivalued and ordering semantics come from the declaration. |
| CC-A15.3-08 | A row states a positive intention. | Omission is open-world; prohibitions, exclusions, required absence, and completeness use separate plan claims rather than empty or negated fillers. |
| CC-A15.3-09 | Planned filling remains planned. | Read each row as the positive intention defined in §4.0, keeping its intended performance and applicability conditions explicit. |
| CC-A15.3-10 | Plan revision follows C.2.1 WorkPlan identity. | Changed identity-bearing content identifies another WorkPlan episteme; edition continuity is asserted only when `EpistemeEditionRelation` obtains, and PlanItems gain no separate edition ontology. |
| CC-A15.3-11 | Later actual facts are established independently. | Establish actual relation participation and operation bindings under their direct predicates. Identify Work under A.15.1 only when that dated occurrence claim is needed; none follows from a plan row. |
| CC-A15.3-12 | Later comparison preserves the cited baseline and polarity. | Substitution or variance uses a stated comparison policy; a missing-filler or negative result needs its closure or negative criterion and case facts. |
| CC-A15.3-13 | Edition, reference, and policy pins are concrete and decision-relevant. | No implicit *latest*, generic RefKind, generic PolicyRef, publication face, or conflicting pin controls a row. |
| CC-A15.3-14 | Conditions retain their own grounds; a view alone adds no plan authority. | Cite the governing conditions from their own patterns. Trace a view to its WorkPlan; any new planned row or rule requires the corresponding plan revision. |

