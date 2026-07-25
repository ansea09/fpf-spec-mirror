---
chunk_kind: "child"
pattern_id: "A.15.3"
pattern_title: "SlotFillingsPlanItem"
section_id: "A.15.3:7"
section_title: "Conformance Checklist"
source_path: "FPF-Spec.md"
output_path: "by_section/A.15.3/A.15.3__008_conformance-checklist.md"
commit_sha: "504747d26299e3963dc0457bf48d4e2a791d926a"
heading_path:
  - "A.15.3 — SlotFillingsPlanItem"
  - "A.15.3:7 — Conformance Checklist"
line_start: 25237
line_end: 25255
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
| CC-A15.3-01 | The item is declaration-local WorkPlan content, not a U-kind, record, or relation occurrence. | Its designator resolves inside one exact WorkPlan edition; no independent PlanItem identity rule or row authority is claimed. |
| CC-A15.3-02 | The enclosing WorkPlan retains one already identified present EntityOfConcern, while the item names an intended-performance designator. | No possible future performance is treated as an existing entity, reference target, or dated Work merely because it is planned. |
| CC-A15.3-03 | Every row targets one exact declaration edition and member with one direct owner of the reusable member meaning and corresponding actual-use predicate. | Declaration ref, member designator, family, direct-owner pattern, and predicate route are recoverable; A.15.3 owns only the intended-use claim. |
| CC-A15.3-04 | Relation-participant rows target only A.6.5 SlotSpecs inside exact RelationSignatures. | A method description, schema field, plan field, or operation argument is never called a SlotSpec. |
| CC-A15.3-05 | Operation rows target exact A.6.1 ArgumentDeclarations or ResultDeclarations. | Mechanism edition, operation designator, member designator, binding rule, predicate, and cardinality resolve together. |
| CC-A15.3-06 | Any other target has an explicit direct declaration owner. | Missing reusable meaning, corresponding actual-use predicate, or owner yields a blocker rather than a generic target. |
| CC-A15.3-07 | Planned value or designation follows the target member's ValueKind, designation rule, and semantic cardinality. | For a single-valued target, exact conditions and a resolution rule make at most one planned value effective; multivalued and ordering semantics come only from the target declaration, not row count or layout. |
| CC-A15.3-08 | The row is a positive intended-use claim. | Omission is open-world; prohibition, exclusion, required absence, and completeness are separate governed plan claims rather than empty or negated fillers. |
| CC-A15.3-09 | Planned filling remains planned. | No row establishes dated work, direct-relation obtaining, operation application, argument binding, returned result, change, production, delivery, acceptance, or outcome. |
| CC-A15.3-10 | Plan revision follows C.2.1 WorkPlan identity. | Changing identity-bearing row content identifies the resulting plan episteme edition; no standalone PlanItem edition ontology is invented. |
| CC-A15.3-11 | Later actual facts keep direct governors. | Work, relation participants, and A.6.1 bindings are independently identified rather than inferred from a plan row. |
| CC-A15.3-12 | Later comparison preserves the cited baseline and truthful polarity. | Substitution or variance is a neighboring governed claim; missing-filler or negative results require an applicable closure or negative criterion rather than absent records. |
| CC-A15.3-13 | Edition, reference, and policy pins are use-driven and concrete. | No implicit “latest,” generic RefKind, generic PolicyRef, publication face, or incompatible duplicate pin controls a reliance-bearing row. |
| CC-A15.3-14 | Conditions and projections stop at their direct owners. | Time, location, readiness, evidence, gate, bridge, publication, and comparison claims are cited rather than absorbed; cards and views add no rows or semantics. |

