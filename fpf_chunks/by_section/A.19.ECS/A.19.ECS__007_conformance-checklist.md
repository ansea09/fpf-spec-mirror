---
chunk_kind: "child"
pattern_id: "A.19.ECS"
pattern_title: "Evaluation CharacteristicSpace Construction"
section_id: "A.19.ECS:6"
section_title: "Conformance checklist"
source_path: "FPF-Spec.md"
output_path: "by_section/A.19.ECS/A.19.ECS__007_conformance-checklist.md"
commit_sha: "3d19010169827708d0bca36d0551af8323908640"
heading_path:
  - "A.19.ECS — Evaluation CharacteristicSpace Construction"
  - "A.19.ECS:6 — Conformance checklist"
line_start: 22836
line_end: 22852
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
keywords:
---

### A.19.ECS:6 - Conformance checklist

| Check | Requirement | Why |
|---|---|---|
| `CC-A19ECS-1` | An evaluation characteristic-space specification SHALL name evaluated object kind, use scope, reader scope, and qualification window. | Prevents context-free quality claims. |
| `CC-A19ECS-2` | It SHALL include admissible, below-floor, and not-applicable contrast cases. | Tests evaluated-object-kind discrimination. |
| `CC-A19ECS-3` | Each coordinate SHALL bind one characteristic to one scale or state why it is an ordinal content reading rather than a measurement claim. | Preserves A.17/A.18/C.16/A.19 discipline. |
| `CC-A19ECS-4` | Each coordinate SHALL state value meanings, polarity or no-simple-direction value rule, evidence rule, and missingness rule. | Makes readings replayable. |
| `CC-A19ECS-5` | The specification SHALL state floor, exceptional, status, stop, and reopen meanings for the declared use. | Lets improvement stop locally without claiming final perfection. |
| `CC-A19ECS-6` | Protected trade-offs SHALL be named when improving visible coordinates can harm another live value. | Blocks Goodhart-style improvement. |
| `CC-A19ECS-7` | The specification SHALL not average ordinal coordinates or turn inactive coordinates into hidden pass, waiver, or failure. | Preserves non-scalar comparison. |
| `CC-A19ECS-8` | Wrong-kind objects SHALL be marked not applicable unless the declared use explicitly compares across those object kinds. | Prevents false low scores. |
| `CC-A19ECS-9` | If made reusable beyond one local use, the evaluation characteristic-space specification SHALL make the minimum items in `A.19.ECS:4.3` recoverable by value. If the selected publication form is an FPF pattern, `E.8` also applies to that publication form. | Prevents underspecified evaluations. |
| `CC-A19ECS-10` | If the evaluation itself changes during improvement, the loop record SHALL name the changed evaluation version and the comparability effect on earlier object-version readings. | Prevents silent value drift. |
| `CC-A19ECS-11` | The evaluation characteristic-space specification SHALL assign evidence, assurance, gate, work, decision, publication, naming, measurement, Q-Bundle, OEE/NQD, and mathematical-lens claims to exact neighbouring patterns when those claims are live. | Prevents an evaluation from becoming a second ontology. |
| `CC-A19ECS-12` | A reusable evaluation characteristic-space specification SHALL state what would lower, reopen, or retire the evaluation: missing contrast case, changed use, changed source-use role or source-currentness status, hidden trade-off loss, or corrected neighbouring-pattern claim assignment. | Makes high-value evaluation claims falsifiable instead of permanent praise. |

