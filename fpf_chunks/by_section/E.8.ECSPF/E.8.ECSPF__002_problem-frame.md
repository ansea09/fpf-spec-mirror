---
chunk_kind: "child"
pattern_id: "E.8.ECSPF"
pattern_title: "Evaluation CharacteristicSpace FPF Pattern Publication Form"
section_id: "E.8.ECSPF:1"
section_title: "Problem frame"
source_path: "FPF-Spec.md"
output_path: "by_section/E.8.ECSPF/E.8.ECSPF__002_problem-frame.md"
commit_sha: "eaafd3a43b9173706e1f8388a3bc94c6445397e4"
heading_path:
  - "E.8.ECSPF — Evaluation CharacteristicSpace FPF Pattern Publication Form"
  - "E.8.ECSPF:1 — Problem frame"
line_start: 57032
line_end: 57051
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

### E.8.ECSPF:1 - Problem frame

Use `E.8.ECSPF` when an evaluation `CharacteristicSpace` constructed or repaired under `A.19.ECS` must be published as an FPF pattern. The live question is not "what values should this evaluated object be judged by?" but "how do we write the FPF pattern publication form so those values remain usable, reviewable, and bounded?"

`A.19.ECS` governs the evaluation characteristic-space specification: evaluated object kind, use scope, contrast cases, coordinate set, value meanings, evidence basis, result-row shape, calibration points, coordinate-specific payloads, missingness, protected trade-offs, status meanings, and stop or reopen conditions. `E.8` governs ordinary FPF authoring form. `E.8.ECSPF` governs their intersection: an FPF pattern whose main payload is a reusable evaluation.

**Not this pattern when.** Use `A.19.ECS` when the characteristic-space specification itself is missing or inadequate. Use `E.8` when the pattern is not an evaluation-characteristic-space pattern. Use `E.21`, `E.9.DA`, `E.2.DA`, `F.18`, `C.25`, or a project-local evaluation when one already supplies the value meanings for the evaluated object and use. Use `E.22` to frame one quality evaluation and `E.23` to run repeated improvement. Use a local rubric, table, or project rule instead of an FPF pattern when the evaluation is not intended for durable FPF reuse.

**First useful move.** Start from the accepted `A.19.ECS` specification. Name the evaluated object kind, declared use, and first action-guiding evaluation use in the pattern's recognition text before presenting coordinate tables or conformance rows.

**FPF-publication boundary.** If the evaluation is local, temporary, or project-specific, do not publish an FPF pattern. Keep the `A.19.ECS` specification in the local publication form and cite the exact FPF neighbours it uses.

**What goes wrong if missed.** An evaluation-characteristic-space pattern becomes a score sheet, review form, checklist, or taxonomy. The coordinate table appears before the working situation. Readers can see values but cannot tell when to use them, what to do after an evaluation result, which objects are outside the declared evaluated-object kind, or which neighbouring pattern governs evidence, assurance, gate, work, decision, naming, measurement, or improvement-loop claims.

**What this buys.** `E.8.ECSPF` lets FPF publish evaluations as real patterns: practitioner-readable first, exact enough for review, and bounded enough that `E.22` and `E.23` can consume them without stealing their values.

**Primary EntityOfConcern in plain terms.** The primary EntityOfConcern is the authored FPF pattern publication form for one evaluation `CharacteristicSpace`.

**Primary working reader.** The first reader is an FPF author or reviewer turning an accepted evaluation characteristic-space specification into a reusable FPF pattern for later practitioners, managers, and stewards.

