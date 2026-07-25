---
chunk_kind: "child"
pattern_id: "E.22"
pattern_title: "Improvement-Oriented Quality Evaluation Question Framing"
section_id: "E.22:1"
section_title: "Problem frame"
source_path: "FPF-Spec.md"
output_path: "by_section/E.22/E.22__002_problem-frame.md"
commit_sha: "504747d26299e3963dc0457bf48d4e2a791d926a"
heading_path:
  - "E.22 — Improvement-Oriented Quality Evaluation Question Framing"
  - "E.22:1 — Problem frame"
line_start: 84154
line_end: 84169
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

Use `E.22` when someone is about to ask for a quality evaluation, quality review, returned-finding absorption, improvement proposal, or follow-up hypothesis over an object version named by value, and the question needs to say what kind of evaluation is wanted before the evaluator starts.

`E.22` frames the question. It does not evaluate the object. The governing evaluation pattern description names the method to apply; an optional semantic evaluation method is the method itself. A characteristic-space specification, Q-Bundle description, rubric description, review-profile description, evidence-basis description, and result-form description constrain or describe that evaluation. None of those specifications performs the evaluation or substitutes for its governing method. For example, `E.21`, `E.9.DA`, or `E.2.DA` may govern evaluation of one FPF object, while `A.19.ECS` and `C.25` supply supporting quality-model descriptions. `E.19` instead governs an admission or refresh review gate and findings profile. Use `E.19` as the evaluation method only when its review result is itself the object under evaluation; otherwise its later gate check remains distinct from the quality evaluation.

Not this pattern when the question is already scoped and one direct evaluation is enough. Run the object-under-improvement evaluation directly. Use `E.23` when repeated improvement across passes is needed.

First useful move: write a `QualityEvaluationQuestionFrame@Context` naming the object version and a `QualityEvaluationUseDeclaration@Context`. In that declaration, name the governing evaluation pattern separately from its quality-model, evidence-basis, and result-form descriptions; then state the purpose, floor or improvement aim, and protected trade-offs.

What goes wrong if missed: "review this" can mean too many different things. A floor check may be mistaken for exceptional improvement, a review may suggest work without naming a changed evaluation result, absorption may count closed rows without re-evaluating the changed object, or a follow-up suggestion may be overread as a decision, work plan, gate, evidence, assurance, or release.

What this buys in practice: requester and evaluator start with the same object version, evaluation purpose, value source, protected trade-offs, evidence basis, and result form. A small floor question can stay small, while a request for proposals or trade-off analysis returns the additional information needed for a later improvement decision.

Primary EntityOfConcern in plain terms: the framed quality-evaluation question for one object version.

