---
chunk_kind: "child"
pattern_id: "E.22"
pattern_title: "Improvement-Oriented Quality Evaluation Question Framing"
section_id: "E.22:1"
section_title: "Problem frame"
source_path: "FPF-Spec.md"
output_path: "by_section/E.22/E.22__002_problem-frame.md"
commit_sha: "d77339d7056433de3ee55ad863860ee4b3006f6f"
heading_path:
  - "E.22 — Improvement-Oriented Quality Evaluation Question Framing"
  - "E.22:1 — Problem frame"
line_start: 79899
line_end: 79912
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
  - "F.19"
  - "G.11"
  - "G.5"
  - "G.9"
keywords:
---

### E.22:1 - Problem frame

Use `E.22` when someone is about to ask for a quality evaluation, quality review, returned-finding absorption, improvement proposal, or follow-up hypothesis over an object version named by value, and the question needs to say what kind of evaluation is wanted before the evaluator starts.

`E.22` frames the question. It does not evaluate the object. The values, coordinates, statuses, and stop meanings come from the named object-under-improvement evaluation: for example `E.21` for one pattern version, `E.9.DA` for one `DRR`, `E.2.DA` for an FPF-level object, `C.25` for an engineering quality bundle, or another declared characteristic space, scale set, rubric, or review profile. `E.19` is different: it supplies an admission or refresh review gate and findings profile. Use `E.19` as the object-under-improvement evaluation only when the object being evaluated is an `E.19` review-profile result itself. For one FPF pattern version, `E.21` supplies the coordinate values and `PatternQualityStatus`; `E.19` may later check that the `E.21` result is valid, sufficient for the release seam, and not overread as project evidence, release, gate, assurance, or work.

Not this pattern when the question is already scoped and one direct evaluation is enough. Run the object-under-improvement evaluation directly. Use `E.23` when repeated improvement across passes is needed.

First useful move: write a `QualityEvaluationQuestionFrame` naming the object version, the object-under-improvement evaluation, the purpose, the floor or improvement aim, protected trade-offs, expected evidence basis, and expected result form.

What goes wrong if missed: "review this" can mean too many different things. A floor check may be mistaken for exceptional improvement, a review may suggest work without naming quality movement, absorption may count closed rows without re-evaluating the changed object, or a follow-up suggestion may be overread as a decision, work plan, gate, evidence, assurance, or release.

Primary EntityOfConcern in plain terms: the framed quality-evaluation question for one object version.

