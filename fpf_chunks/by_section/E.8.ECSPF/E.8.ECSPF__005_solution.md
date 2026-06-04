---
chunk_kind: "child"
pattern_id: "E.8.ECSPF"
pattern_title: "Evaluation CharacteristicSpace FPF Pattern Publication Form"
section_id: "E.8.ECSPF:4"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/E.8.ECSPF/E.8.ECSPF__005_solution.md"
commit_sha: "3d19010169827708d0bca36d0551af8323908640"
heading_path:
  - "E.8.ECSPF — Evaluation CharacteristicSpace FPF Pattern Publication Form"
  - "E.8.ECSPF:4 — Solution"
line_start: 57145
line_end: 57184
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

### E.8.ECSPF:4 - Solution

When an `A.19.ECS` specification is selected for durable FPF publication, author the evaluation as an `E.8` pattern with these additional placement rules:

1. **Keep the evaluation characteristic-space specification separate from the publication form.** The pattern publishes an evaluation `CharacteristicSpace`; it is not itself the evaluated object, the evaluation result, the improvement loop, or the evidence record.
2. **Put recognition before coordinates.** The opening text names evaluated object kind, declared use, first evaluation use, cheap stop, what goes wrong, and what the pattern buys before any dense table.
3. **Place the `A.19.ECS` specification by value.** The `Solution` carries the record shape, local names, eligibility rule, coordinate set, value meanings, missingness rule, protected trade-offs, status meanings, and stop or reopen condition.
4. **Use worked slices as the discriminating-case test.** Archetypal Grounding and worked cases include a passing evaluated object, a below-floor evaluated object, and a not-applicable object.
5. **Keep checklist rows secondary.** Conformance checks verify that the evaluation is recoverable and usable. They do not become the user's method.
6. **Keep outside claims with exact neighbours.** Relations and non-use boundaries name the exact neighbour for evidence, assurance, gate, work, decision, naming, measurement, OEE/NQD, mathematical lens, `E.22` quality-read, and improvement-loop claims.
7. **Evaluate the publication form with `E.21`.** When the FPF pattern publication form is under quality improvement, `E.21` evaluates the FPF pattern version's quality. The evaluation coordinates inside the pattern continue to judge the evaluated object declared by that evaluation.

#### E.8.ECSPF:4.1 - Canonical placement table

| E.8 section | ECS-specific payload |
|---|---|
| `Problem frame` | Evaluated object kind, declared use, first useful evaluation use, cheap stop, what goes wrong without this evaluation, and what practical move the evaluation enables. |
| `Problem` | Failure modes that the evaluation prevents: wrong-kind scoring, hidden value drift, proxy value, one-score collapse, missingness confusion, or neighbour theft. |
| `Forces` | Tensions among reuse, coordinate count, readability, measurement legality, trade-off protection, local stop, and open-ended improvement. |
| `Solution` | `A.19.ECS` record shape, local names, eligibility rule, coordinate set, value meanings, evidence and missingness rules, protected trade-offs, status meanings, stop and reopen conditions. |
| `Archetypal Grounding` | At least one passing evaluated object, one below-floor evaluated object, and one not-applicable object. |
| `Bias-Annotation` | Known skew in source examples, reader family, domain tradition, measurement preference, benchmark preference, or FPF-internal reuse. |
| `Conformance Checklist` | Checks that the specification is recoverable, not that a reviewer likes the evaluated object. |
| `Common Anti-Patterns` | Score-sheet pattern, checklist-as-solution, table-first recognition failure, neighbour theft, one total score, hidden value drift. |
| `Consequences` | What a conforming evaluation use permits, what it does not permit, and which neighbours govern claims that exceed the evaluation. |
| `Rationale` | Why this coordinate set and publication-form are selected, including relation to `A.19.ECS` and exact existing evaluations. |
| `SoTA-Echoing` | Current practice that changes evaluated-object selection, coordinate choice, value meaning, missingness, comparison, or stop discipline. |
| `Relations` | `A.19.ECS`, `E.8`, `E.21`, `E.22`, `E.23`, and exact domain or neighbour patterns. |

#### E.8.ECSPF:4.2 - Local names and kind settlement

| Local name | Role | Non-use boundary |
|---|---|---|
| `EvaluationCharacteristicSpaceFPFPatternPublicationForm` | The authored FPF pattern body that publishes one evaluation `CharacteristicSpace`. | Not the evaluated object being evaluated, evaluation result, improvement loop, evidence record, or release approval. |
| `ECSPayload` | The by-value `A.19.ECS` specification inside the pattern. | Not an arbitrary table or checklist. |
| `RecognitionEvaluationUseLine` | Early line saying what object is evaluated, for which use, and what the first admissible evaluation use does. | Not a slogan or pattern-title paraphrase. |
| `DiscriminatingCaseBank` | Passing, below-floor, and not-applicable worked slices. | Not only positive examples. |
| `NeighbourExitBlock` | Exact neighbouring FPF pattern applications for claims outside the evaluation. | Not a general directory of possibly related patterns. |
| `PatternVersionQualityEvaluation` | Optional `E.21` evaluation over the authored pattern publication form. | Not a replacement for the evaluation for one evaluated object kind. |

