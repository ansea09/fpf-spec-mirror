---
chunk_kind: "child"
pattern_id: "A.19.ECS"
pattern_title: "Evaluation CharacteristicSpace Construction"
section_id: "A.19.ECS:7"
section_title: "Common Anti-Patterns and How to Avoid Them"
source_path: "FPF-Spec.md"
output_path: "by_section/A.19.ECS/A.19.ECS__009_common-anti-patterns-and-how-to-avoid-them.md"
commit_sha: "b7ec5a0b1dfa4bdae4cf055188219e89cef61a63"
heading_path:
  - "A.19.ECS — Evaluation CharacteristicSpace Construction"
  - "A.19.ECS:7 — Common Anti-Patterns and How to Avoid Them"
line_start: 29060
line_end: 29074
dependencies:
  - "A.17-A.19"
  - "C.16"
  - "C.25"
  - "E.2.DA"
  - "E.21"
  - "E.22"
  - "E.23"
  - "E.8.ECSPF"
  - "E.9.DA"
  - "F.18"
  - "F.19"
keywords:
---

### A.19.ECS:7 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Symptom | Repair |
|---|---|---|
| **Scale set from air.** | Coordinates appear because they are familiar. | Rebuild from evaluated object kind, use, contrast cases, failure modes, domain tradition, first principles, and current source-use relation. |
| **Wrong-kind object forced through the table.** | Objects outside the declared kind are either scored as weak members of that kind or silently exempted from declared coordinates. | Add an object-kind-fit rule and boundary cases: before opening, return to a suitable evaluation; after invocation, record an explicit object-kind-fit defect/value or repair status. |
| **Checklist masquerading as characteristic space.** | A list of tasks is treated as coordinates. | Convert each task row to an evaluated EntityOfConcern property with a characteristic, scale, value meaning, and evidence rule, or move it to work planning. |
| **One total quality score.** | Several ordinal values are averaged. | Use coordinates, statuses, dominance or comparison rule, and protected trade-offs; do not scalarize unless an neighboring pattern governing the claim explicitly declares the operation. |
| **Improvement without floor.** | A loop continues because more change is possible. | State floor, exceptional meaning, stop condition, and reopen condition. |
| **Hidden value drift.** | The evaluation changes while old evaluations are compared as if nothing changed. | Version the evaluation and state comparability, bridge, or retirement. |
| **Evaluation theft.** | The new evaluation starts governing evidence, assurance, gate, work, decision, or publication truth. | Return each claim to the neighboring pattern governing the claim and leave only the value evaluation here. |
| **Result prose as evaluation.** | An evaluator returns a narrative, two-column table, checklist count, or value list without evidence basis and short rationales. | Define the result-row shape, require short rationales and evidence basis, and lower any coordinate whose needed evidence is missing or unchecked. |
| **Evidence basis as evaluated-object method.** | Corpus projection, retrieval, currentness, comparator, monolith-parity, quality-status evidence, or role-turn correspondence is written in the evaluated object as if it were what the evaluated-object user does. | Move the evidence to the evaluation result, evidence basis, projection carrier, or selected publication carrier; keep only the user action or boundary that the evidence justifies. |
| **Coordinate wording as ontology change.** | A coordinate or repair name sounds cleaner, but changes the evaluated object kind, characteristic kind, relation or claim kind, admissible use, or scope. | Treat it as a changed evaluation decision, recover the pre/post kind relation, and repair or reopen the evaluation rather than accepting lexical cleanup. |

