---
chunk_kind: "child"
pattern_id: "E.8.ECSPF"
pattern_title: "FPF Pattern Publication Form for Evaluation Guidance"
section_id: "E.8.ECSPF:1"
section_title: "Problem frame"
source_path: "FPF-Spec.md"
output_path: "by_section/E.8.ECSPF/E.8.ECSPF__002_problem-frame.md"
commit_sha: "72222c13cc1bba009f1ee1f1aca47654db8e5716"
heading_path:
  - "E.8.ECSPF — FPF Pattern Publication Form for Evaluation Guidance"
  - "E.8.ECSPF:1 — Problem frame"
line_start: 72523
line_end: 72542
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

### E.8.ECSPF:1 - Problem frame

Use this pattern when an accepted `EvaluationCharacteristicSpaceSpec` constructed or repaired under `A.19.ECS` has been selected for durable FPF publication, and an author must turn it into a practitioner-facing pattern. The question is not "what values should this object be judged by?" but "how should the pattern teach this evaluation so its values remain usable, reviewable, and bounded?"

`A.19.ECS` guides an author in constructing or repairing the evaluation characteristic-space specification: evaluated object kind and, when needed, the object version; declared use, working reader, qualification window, contrast cases, object-kind-fit rule, coordinate and scale bindings, value meanings and preferred movement, evidence and missingness rules, result-row shape, adjacent-value rationales, calibration points, any triggered coordinate payload, protected trade-offs, any declared comparison rule, status meanings, neighbouring-pattern exits, and stop, reopen, `E.22`, and `E.23` conditions. `E.8` supplies the ordinary FPF authoring form. `E.8.ECSPF` tells the author how to carry the accepted specification into that form. The specification, its `CharacteristicSpace`, the authored pattern content, a later evaluation of an object, and the result of that evaluation remain different things.

**Not this pattern when.** Use `A.19.ECS` when the characteristic-space specification itself is missing or inadequate. Use `E.8` when the pattern is not an evaluation-characteristic-space pattern. Use `E.21`, `E.9.DA`, `E.2.DA`, `F.18`, `C.25`, or a project-local evaluation when one already supplies the value meanings for the evaluated object and use. Use `E.22` to frame one quality evaluation and `E.23` to run repeated improvement. Use a local rubric, table, or project rule instead of an FPF pattern when the evaluation is not intended for durable FPF reuse.

**First useful move.** Start from the accepted `A.19.ECS` specification. Before presenting coordinate tables or conformance rows, name the evaluated object kind, declared use, working reader, qualification window, and first action-guiding evaluation use in the pattern's recognition text.

**FPF-publication boundary.** If the evaluation is local, temporary, or project-specific, do not publish an FPF pattern. Keep the `A.19.ECS` specification in the local publication form and cite the FPF neighbouring patterns named by value it uses.

**What goes wrong if missed.** The pattern, the accepted specification, the evaluation, and its result collapse into one supposed object. The pattern then becomes a score sheet, review form, checklist, or taxonomy. The coordinate table appears before the working situation. Readers can see values but cannot tell when to use them, what to do after an evaluation result, which objects are outside the declared evaluated-object kind, or which neighbouring pattern supplies the needed evidence, assurance, gate, work, decision, naming, measurement, or improvement guidance.

**What this buys.** `E.8.ECSPF` lets an author publish evaluation guidance as a real pattern: practitioner-readable first, exact enough for review, and bounded enough for a later evaluator to use with the framing guidance in `E.22` or the repeated-improvement guidance in `E.23`.

**Primary EntityOfConcern in plain terms.** The primary EntityOfConcern is the authored FPF pattern content and its publication form for one accepted evaluation characteristic-space specification.

**Primary working reader.** The first reader is an FPF author or reviewer turning an accepted evaluation characteristic-space specification into a reusable FPF pattern for later practitioners, managers, and stewards.

