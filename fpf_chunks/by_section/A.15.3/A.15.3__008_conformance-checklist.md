---
chunk_kind: "child"
pattern_id: "A.15.3"
pattern_title: "SlotFillingsPlanItem"
section_id: "A.15.3:7"
section_title: "Conformance Checklist"
source_path: "FPF-Spec.md"
output_path: "by_section/A.15.3/A.15.3__008_conformance-checklist.md"
commit_sha: "fe0df9dcb06cfc87c8a6cb2f7cce3ac0d3b64d5e"
heading_path:
  - "A.15.3 — SlotFillingsPlanItem"
  - "A.15.3:7 — Conformance Checklist"
line_start: 22270
line_end: 22289
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

### A.15.3:7 - Conformance Checklist

| ID | A conforming `SlotFillingsPlanItem`... | Check |
| --- | --- | --- |
| CC-A15.3-01 | is a `U.WorkPlan.PlanItem` with `kind = SlotFillingsPlanItem`. | It contains planned rows, not logs, actuals, or step logic. |
| CC-A15.3-02 | targets exactly one slot-bearing description. | `target_slot_bearing_description_ref` names a Description episteme with SlotSpecs; multiple targets use multiple PlanItems. |
| CC-A15.3-03 | keeps mechanism identity outside the PlanItem. | `MechanismDefinitionRef` is not the target unless a governing description wrapper exposes the planned slots. |
| CC-A15.3-04 | names EntityOfConcern and bounded context. | The baseline says what it is about and where the planned use is bounded. |
| CC-A15.3-05 | names a time selector or time rule when currentness, latest, reproducibility, or launch preparation matters. | No implicit "latest" controls a reliance-bearing baseline. |
| CC-A15.3-05a | uses exactly one time selector form when time is required. | Both-present and both-absent time baselines are nonconforming for reliance-bearing use. |
| CC-A15.3-06 | uses planned-filling rows as the authoritative row source. | Views, cards, and indices are derivable projections only. |
| CC-A15.3-07 | uses concrete RefKinds for ByRef fillers. | No generic `Ref`, generic `SpecRef`, or untyped placeholder carries the planned filler. |
| CC-A15.3-08 | preserves target SlotKind meaning. | The PlanItem chooses fillers; it does not redefine SlotKinds. |
| CC-A15.3-09 | keeps guard-preparation refs separate from gate results. | Later gate passage is recorded under the gate pattern. |
| CC-A15.3-10 | keeps evidence-reference pins separate from evidence-use. | Later evidence and assurance are governed by A.10, B.3, G.6, or the current evidence pattern. |
| CC-A15.3-11 | keeps crossing-preparation refs separate from crossing witnesses. | Crossing refs cite expected Bridge, policy, reference-plane, or published-baseline support only; they do not embed CL/Phi/Psi tables or claim that a crossing occurred. |
| CC-A15.3-12 | keeps launch values and actuals out of the plan. | Performed work records launch values, substitutions, and variance. |
| CC-A15.3-13 | preserves cited baselines after work. | A changed plan becomes a new edition or new PlanItem; performed work records variance against the cited baseline. |
| CC-A15.3-14 | gives lowering and refresh conditions. | Missing target description, exposed SlotKind set, context, time, RefKind, edition pin, guard ref, evidence pin, crossing-policy ref, or variance relation lowers or reopens the claim. |

