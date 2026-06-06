---
chunk_kind: "child"
pattern_id: "E.22"
pattern_title: "Improvement-Oriented Quality Evaluation Question Framing"
section_id: "E.22:1"
section_title: "Problem frame"
source_path: "FPF-Spec.md"
output_path: "by_section/E.22/E.22__002_problem-frame.md"
commit_sha: "e3fedf42dc7cb5d12905913b5a0b0e951ed7d254"
heading_path:
  - "E.22 — Improvement-Oriented Quality Evaluation Question Framing"
  - "E.22:1 — Problem frame"
line_start: 67594
line_end: 67607
dependencies:
  - "A.19.ECS"
  - "C.17-C.19"
  - "C.25"
  - "E.10"
  - "E.19"
  - "E.2.DA"
  - "E.21"
  - "E.23"
  - "E.9.DA"
  - "G.11"
  - "G.5"
  - "G.9"
keywords:
---

### E.22:1 - Problem frame

Use `E.22` when someone is about to ask for a quality evaluation, quality review, returned-finding absorption, improvement proposal, or next-move hypothesis over an exact object version, and the question needs to say what kind of evaluation is wanted before the evaluator starts.

`E.22` frames the question. It does not evaluate the object. The values, coordinates, statuses, and stop meanings come from the named object-under-improvement evaluation: for example `E.21` for one pattern version, `E.9.DA` for one `DRR`, `E.2.DA` for an FPF-level object, `E.19` for an admission or refresh review profile, `C.25` for an engineering quality bundle, or another declared characteristic space, scale set, rubric, or review profile.

Not this pattern when the question is already scoped and one direct evaluation is enough. Run the object-under-improvement evaluation directly. Use `E.23` when repeated improvement across passes is live.

First useful move: write a `QualityEvaluationQuestionFrame` naming the object version, the object-under-improvement evaluation, the purpose, the floor or improvement aim, protected trade-offs, expected evidence basis, and expected result form.

What goes wrong if missed: "review this" can mean too many different things. A floor check may be mistaken for exceptional improvement, a review may suggest work without naming quality movement, absorption may count closed rows without re-evaluating the changed object, or a next-move suggestion may be overread as a decision, work plan, gate, evidence, assurance, or release.

Primary EntityOfConcern in plain terms: the framed quality-evaluation question for one object version.

