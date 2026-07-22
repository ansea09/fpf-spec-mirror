---
chunk_kind: "child"
pattern_id: "E.8.ECSPF"
pattern_title: "Evaluation CharacteristicSpace FPF Pattern Publication Form"
section_id: "E.8.ECSPF:7"
section_title: "Conformance Checklist"
source_path: "FPF-Spec.md"
output_path: "by_section/E.8.ECSPF/E.8.ECSPF__008_conformance-checklist.md"
commit_sha: "0990ff1d1ccee4587b8f7e16e7a725a8edbe66b4"
heading_path:
  - "E.8.ECSPF — Evaluation CharacteristicSpace FPF Pattern Publication Form"
  - "E.8.ECSPF:7 — Conformance Checklist"
line_start: 70704
line_end: 70721
dependencies:
  - "A.19.ECS"
  - "C.25"
  - "E.2.DA"
  - "E.21"
  - "E.22"
  - "E.23"
  - "E.8"
  - "E.9.DA"
  - "F.18"
  - "F.19"
keywords:
---

### E.8.ECSPF:7 - Conformance Checklist

| Check | Requirement | Why |
|---|---|---|
| `CC-E8ECSPF-1` | The pattern publication form SHALL name the `A.19.ECS` evaluation characteristic-space specification or carry its evaluated object kind, use, object-kind-fit rule, coordinate set, value meanings, evidence basis, result-row shape, calibration points, coordinate-specific payloads, missingness, trade-offs, status, and stop condition by value. | Prevents publication-form/content collapse. |
| `CC-E8ECSPF-2` | Recognition text SHALL state evaluated object kind, declared use, first evaluation use, FPF-publication boundary, and object-kind boundary before dense coordinate tables. | Keeps the pattern usable before it becomes reviewable. |
| `CC-E8ECSPF-3` | The `Solution` SHALL carry the ECS payload rather than leaving it only in conformance rows, SoTA rows, or examples. | Prevents checklist substitution. |
| `CC-E8ECSPF-4` | Worked cases SHALL include passing, below-floor, and outside-declared-object-kind boundary outcomes. | Tests evaluated-object-kind discrimination. |
| `CC-E8ECSPF-5` | Each coordinate SHALL state value meanings, polarity or no-simple-direction value rule, missingness rule, and protected trade-off when applicable to the declared evaluation use. | Makes evaluation uses repeatable and bounded. |
| `CC-E8ECSPF-6` | Relations SHALL name governing patterns for evidence, assurance, gate, work, decision, naming, measurement, OEE/NQD, mathematical-lens, `E.22` quality-evaluation, and improvement-loop claims when the publication form makes those claims. They SHALL keep pattern application and relation kind explicit, keep simple relations free of phrase apparatus, and keep ordinary references or architecture-placement reasoning out of publication-form evaluation prose. | Prevents a second ontology or apparatus-overwrapped publication form. |
| `CC-E8ECSPF-6a` | Wording, naming, or precision-restoration repairs in an evaluation-characteristic-space pattern SHALL include a kind-restoration check for the evaluated object, relation or claim kind, current ontic slot, relation position, use relation, or claim kind when live, admissible use, and scope before and after the repair, plus the governing pattern when another pattern governs the kind under repair, relation, claim, or position. | Prevents evaluation patterns from inheriting lexical cleanup as ontology drift. |
| `CC-E8ECSPF-7` | If the authored publication form is under improvement, `E.21` SHALL evaluate FPF pattern-version quality separately from the evaluation's evaluated object result. | Keeps pattern quality distinct from evaluated object quality. |
| `CC-E8ECSPF-8` | The pattern SHALL not publish a local, temporary, or one-project evaluation as FPF unless reuse scope and governing patterns for outside claims justify FPF publication. | Blocks needless pattern growth. |
| `CC-E8ECSPF-9` | The publication form SHALL state what would lower, reopen, or retire the published evaluation: changed object kind, changed use, changed use of a cited source, changed source adoption/adaptation/rejection decision, missing contrast case, coordinate-value drift, missingness-rule change, or corrected governing pattern for an outside claim. | Makes maintenance of the evaluation pattern testable. |
| `CC-E8ECSPF-10` | The publication form SHALL state the required result row shape and evidence basis. If values need external, comparator, projection, worked-case, or currentness evidence, the result form SHALL require that evidence by value or lower the coordinate. | Prevents a published evaluation from accepting prose impressions or two-column value lists as results. |
| `CC-E8ECSPF-11` | Reusable evaluation patterns SHALL publish calibration points for common adjacent-value disagreements and any coordinate-specific evidence payload needed to reach floor or exceptional values. | Makes the same evaluation usable by more than one evaluator. |
| `CC-E8ECSPF-12` | The publication form SHALL keep `E.21` values, `PatternQualityStatus`, corpus-projection evidence, README/ToC/E.11/I.2 alignment, card/retrieval evidence, cold-reader evidence, monolith parity, landing evidence, developer/reviewer/executor correspondence, and other quality-carrier facts out of the pattern. These facts belong in the `E.21` result, `E.19` run record, README/ToC/E.11/I.2, card/retrieval/projection carrier, or release/landing evidence carrier unless the role test shows that the publication form's own `EntityOfConcern` and user-facing action are that evaluation/projection work. | Prevents quality of the publication form from replacing the evaluation published by the pattern. |

