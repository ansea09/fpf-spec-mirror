---
chunk_kind: "child"
pattern_id: "A.6.5"
pattern_title: "Relation-Declaration Slot Discipline - SlotKind, ValueKind, RefKind, and participant-designation discipline"
section_id: "A.6.5:8"
section_title: "Common Failure Modes and Repairs"
source_path: "FPF-Spec.md"
output_path: "by_section/A.6.5/A.6.5__009_common-failure-modes-and-repairs.md"
commit_sha: "646b41f84ffef4918ad9bdb34e7b450f0c4903ee"
heading_path:
  - "A.6.5 — Relation-Declaration Slot Discipline - SlotKind, ValueKind, RefKind, and participant-designation discipline"
  - "A.6.5:8 — Common Failure Modes and Repairs"
line_start: 19466
line_end: 19482
dependencies:
  - "A.15.3"
  - "A.6.0"
  - "A.6.1"
  - "A.6.P"
  - "A.6.REL"
  - "A.6.RSIR"
  - "C.2.1"
  - "C.29"
  - "C.3"
  - "E.24.UK"
keywords:
---

### A.6.5:8 - Common Failure Modes and Repairs

| Failure | Why it matters | Repair |
|---|---|---|
| `U.RelationSlotDiscipline` treated as a root kind | A rule set is promoted into an unsupported world-side entity. | Keep A.6.5 as the rule set that constrains `SlotSpec` declarations; apply E.24.UK to any future U-kind candidate. |
| Generic `byRef` without an exact RefKind | A later use cannot tell what referent kind can be resolved. | Declare the exact RefKind, or expand the compact sketch next to its use. |
| Reference treated as the relation participant | A storage or publication choice changes the claimed world-side ontology. | Keep the referent as participant; state refMode only for the receiving assertion or description episteme that carries the designation. |
| One SlotSpec contains a ValueKind written as a list of unrelated alternatives | Different predicate semantics are hidden behind one participant meaning. | Recover the real common ValueKind when one exists; otherwise split the relation kind. |
| One source word names a SlotKind, participant ValueKind, reference, and field | A reader cannot tell which object may be substituted, resolved, or renamed. | Split the meanings: use `...Slot` only for the declaration-local SlotKind, `...Ref` only for an admitted RefKind or reference value of that kind, and neither suffix for the participant ValueKind. Keep the source field name and state its explicit correspondence; for example, distinguish `HolderSystemSlot`, `U.System`, and `Robot_7_Ref : U.EntityRef`. |
| Active grammar used as agency evidence | A relation, method, work, structure, or episteme is said to act. | Recover the acting `U.System`; use the patterns that define the relation, Work, Method, and transformation claims. |
| A universal context, taxonomy, scheme, or model-use SlotSpec added to the `U.SystemRoleAssignment` family or every species | Interpretive or receiving-use material is turned into a world-side participant, and several assignment laws are hidden under one root signature. | Give each assignment species only `HolderSystemSlot`, its declaration-local `AssignedSystemRoleKindSlot`, and any additional participant meaning whose value changes the predicate or occurrence identity. Keep a `KindSignature`, taxonomy episteme, scheme, bridge, or model-use structure with the assertion or receiving use unless another relation independently makes it a participant. |
| Interface language erased or promoted | A recognizable source sentence is replaced by either a generic `U.Interface` or an untyped participant catalogue. | Keep the source word for recognition, state what connects, crosses, or is transferred between which exact entities, recover the definition of the direct relation, and declare only the SlotSpecs that a receiving typed use actually reuses. Stop at A.6.RSIR or a missing-relation result when the relation remains undefined. |
| Result-family catalogue | The word `result` triggers a list of possible relation families, so the reader cannot tell which object continued or what claim to make. | Ask whether the same entity continued or a new entity began. For continuation, name the changed characteristic and actual transformation. For inception, require an admitted identity-inception predicate and its definition. If another concrete verb such as `delivered` is present, recover that one relation and its participants. Return the corresponding missing-relation or missing identity-inception result when the needed definition is absent. |
| A participant designation is promoted into a new qualification ontic | A value or reference in an episteme is mistaken for a further world-side object. | Apply the three-way dispatch in A.6.5:4.6: direct relation fact, assertion episteme, or current local participant kind. |
| A method-description, operation, plan, work, evaluation, card, schema, or record field is called a SlotSpec | A reusable direct-relation participant declaration is invented from representation shape or broad wording. | Require the direct-relation definition and one exact `RelationSignature` and SlotSpec. A receiving semantic field is covered by an explicit declaration against that SlotSpec. An external or independently named representation field keeps its source name and requires an explicit C.29 correspondence. Neither route makes the field a SlotSpec or the designation an actual participant. Handle operation arguments and results under A.6.1 and use the definitions for the other fields. |
| An A.15.3 planned designation is treated as the actual relation participant | Plan content is mistaken for world-side participation and predicate satisfaction. | Keep the row in the WorkPlan; identify any later participant and obtaining relation independently under that relation's definition. |

