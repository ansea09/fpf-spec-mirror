---
chunk_kind: "child"
pattern_id: "A.19.ECS"
pattern_title: "Evaluation CharacteristicSpace Construction"
section_id: "A.19.ECS:6"
section_title: "Conformance checklist"
source_path: "FPF-Spec.md"
output_path: "by_section/A.19.ECS/A.19.ECS__008_conformance-checklist.md"
commit_sha: "504747d26299e3963dc0457bf48d4e2a791d926a"
heading_path:
  - "A.19.ECS — Evaluation CharacteristicSpace Construction"
  - "A.19.ECS:6 — Conformance checklist"
line_start: 28435
line_end: 28456
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

### A.19.ECS:6 - Conformance checklist

| Check | Requirement | Why |
|---|---|---|
| `CC-A19ECS-1` | An evaluation characteristic-space specification SHALL name evaluated object kind, use scope, reader scope, and qualification window. | Prevents context-free quality claims. |
| `CC-A19ECS-2` | It SHALL include admissible, below-floor, and outside-declared-object-kind boundary contrast cases. | Tests evaluated-object-kind discrimination. |
| `CC-A19ECS-3` | Each coordinate SHALL bind one characteristic to one scale or state why it is an ordinal content evaluation rather than a measurement claim. | Preserves A.17/A.18/C.16/A.19 discipline. |
| `CC-A19ECS-4` | Each coordinate SHALL state value meanings, polarity or no-simple-direction value rule, evidence rule, and missingness rule. | Makes values replayable. |
| `CC-A19ECS-5` | The specification SHALL state floor, exceptional, status, stop, and reopen meanings for the declared use. | Lets improvement stop locally without claiming final perfection. |
| `CC-A19ECS-6` | Protected trade-offs SHALL be named when improving visible coordinates can harm another live value. | Blocks Goodhart-style improvement. |
| `CC-A19ECS-7` | The specification SHALL not average ordinal coordinates or turn undeclared coordinates into hidden pass, waiver, or failure. | Preserves non-scalar comparison. |
| `CC-A19ECS-8` | Wrong-kind objects SHALL return to evaluation selection before opening, or receive an explicit object-kind-fit defect/value when the evaluation has already been invoked. | Keeps the declared coordinate table complete after invocation and prevents false low scores before the suitable evaluation is selected. |
| `CC-A19ECS-9` | If made reusable beyond one local use, the evaluation characteristic-space specification SHALL make the minimum items in `A.19.ECS:4.3` recoverable by value. If the selected publication form is an FPF pattern, `E.8` also applies to that publication form. | Prevents underspecified evaluations. |
| `CC-A19ECS-10` | If the evaluation itself changes during improvement, the loop record SHALL name the changed evaluation version and the comparability effect on earlier object-version evaluations. | Prevents silent value drift. |
| `CC-A19ECS-11` | The evaluation characteristic-space specification SHALL state any evidence, assurance, gate, work, decision, publication, naming, measurement, Q-Bundle, OEE/NQD, mathematical-lens, or related claim as a direct governing-pattern application or named relation by value when that claim is being made. The coordinate Solution carries the evaluation construction itself; reference boilerplate, architecture-placement rationale, and coordination with another governing pattern stay in relations, rationale, source-basis, or decision-rationale material unless they change a coordinate. | Prevents an evaluation from becoming a second ontology or reference boilerplate. |
| `CC-A19ECS-12` | A reusable evaluation characteristic-space specification SHALL state what would lower, reopen, or retire the evaluation: missing contrast case, changed use, changed source-use relation or source-currentness status, hidden trade-off loss, or corrected neighbouring-pattern claim assignment. | Makes high-value evaluation claims falsifiable instead of permanent praise. |
| `CC-A19ECS-13` | A reusable evaluation characteristic-space specification SHALL define the result-row shape and require a short rationale for every coordinate value. | Prevents prose impressions and two-column tables from being mistaken for evaluation results. |
| `CC-A19ECS-14` | It SHALL define the evaluation evidence basis and any coordinate-specific evidence payload needed for source-currentness, comparator, corpus-projection, worked-case, retrieval, or external-currentness claims. Missing or unchecked evidence lowers the coordinate that needs it. | Makes values replayable without creating an "inactive" or "not evaluated" escape route. |
| `CC-A19ECS-15` | It SHALL publish calibration points for common adjacent-value disagreements whenever the evaluation is expected to be reused by different evaluators. | Keeps `3`, `4`, and `5` from drifting into evaluator temperament. |
| `CC-A19ECS-16` | It SHALL declare where result evidence, corpus-projection evidence, retrieval evidence, comparator evidence, currentness evidence, and quality-status evidence live. These payloads SHALL stay in the evaluation result, evidence basis, projection carrier, or selected publication carrier unless the evaluated object itself is that carrier. If the payload implies a user-facing action for another evaluated object, publish that move or boundary, not the carrier proof. This is an evaluation-payload placement rule, not a lexical ban: evidence-use payloads do not enter live evaluated-object text merely because they are true or useful to authors or evaluators. | Prevents evaluation evidence from leaking into the evaluated object's method or live text. |
| `CC-A19ECS-17` | If construction or repair changes coordinate wording or evaluation wording, the specification SHALL require a pre/post kind-restoration check for evaluated object kind, characteristic kind, relation or claim kind, current ontic slot, relation position, use relation, or claim kind when live, admissible use, and scope, plus the governing pattern when another pattern governs the kind under repair, relation, claim, or position. | Prevents coordinate cleanup from changing what the evaluation evaluates. |

