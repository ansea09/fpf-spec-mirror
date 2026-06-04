---
chunk_kind: "child"
pattern_id: "E.8.ECSPF"
pattern_title: "Evaluation CharacteristicSpace FPF Pattern Publication Form"
section_id: "E.8.ECSPF:7"
section_title: "Conformance Checklist"
source_path: "FPF-Spec.md"
output_path: "by_section/E.8.ECSPF/E.8.ECSPF__008_conformance-checklist.md"
commit_sha: "3d19010169827708d0bca36d0551af8323908640"
heading_path:
  - "E.8.ECSPF — Evaluation CharacteristicSpace FPF Pattern Publication Form"
  - "E.8.ECSPF:7 — Conformance Checklist"
line_start: 57199
line_end: 57212
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
keywords:
---

### E.8.ECSPF:7 - Conformance Checklist

| Check | Requirement | Why |
|---|---|---|
| `CC-E8ECSPF-1` | The pattern publication form SHALL name the `A.19.ECS` evaluation characteristic-space specification or carry its evaluated object kind, use, eligibility, coordinate set, value meanings, missingness, trade-offs, status, and stop condition by value. | Prevents publication-form/content collapse. |
| `CC-E8ECSPF-2` | Recognition text SHALL state evaluated object kind, declared use, first evaluation use, cheap stop, and not-applicable boundary before dense coordinate tables. | Keeps the pattern usable before it becomes reviewable. |
| `CC-E8ECSPF-3` | The `Solution` SHALL carry the ECS payload rather than leaving it only in conformance rows, SoTA rows, or examples. | Prevents checklist substitution. |
| `CC-E8ECSPF-4` | Worked cases SHALL include passing, below-floor, and not-applicable outcomes. | Tests evaluated-object-kind discrimination. |
| `CC-E8ECSPF-5` | Each coordinate SHALL state value meanings, polarity or no-simple-direction value rule, missingness rule, and protected trade-off when live. | Makes evaluation uses repeatable and bounded. |
| `CC-E8ECSPF-6` | Relations SHALL name exact neighbouring governing patterns for evidence, assurance, gate, work, decision, naming, measurement, OEE/NQD, mathematical-lens, `E.22` quality-read, and improvement-loop claims when those claims are live. | Prevents a second ontology. |
| `CC-E8ECSPF-7` | If the authored publication form is under improvement, `E.21` SHALL evaluate FPF pattern-version quality separately from the evaluation's evaluated object result. | Keeps pattern quality distinct from evaluated object quality. |
| `CC-E8ECSPF-8` | The pattern SHALL not publish a local, temporary, or one-project evaluation as FPF unless reuse scope and neighbouring-pattern claim assignment justify FPF publication. | Blocks needless pattern growth. |
| `CC-E8ECSPF-9` | The publication form SHALL state what would lower, reopen, or retire the published evaluation: changed object kind, changed use, changed use of a cited source, changed source adoption/adaptation/rejection decision, missing contrast case, coordinate-value drift, missingness-rule change, or corrected neighbouring-pattern claim assignment. | Makes maintenance of the evaluation pattern testable. |

