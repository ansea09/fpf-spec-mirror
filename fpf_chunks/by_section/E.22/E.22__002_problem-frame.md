---
chunk_kind: "child"
pattern_id: "E.22"
pattern_title: "Improvement-Oriented Quality Evaluation Question Framing"
section_id: "E.22:1"
section_title: "Problem frame"
source_path: "FPF-Spec.md"
output_path: "by_section/E.22/E.22__002_problem-frame.md"
commit_sha: "7f7c592f4d633e54cdb202d622d6e0e05df41517"
heading_path:
  - "E.22 — Improvement-Oriented Quality Evaluation Question Framing"
  - "E.22:1 — Problem frame"
line_start: 86465
line_end: 86484
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

`E.22` frames the question. It does not evaluate the object. `evaluationPatternLocator` identifies the FPF pattern description containing the evaluation predicate or constraint; an optional `semanticEvaluationMethodRef` names the separately identified `U.Method` used for that evaluation. A characteristic-space specification, Q-Bundle description, rubric description, review-profile description, evidence-basis description, and result-form description constrain or describe that evaluation. None of those specifications performs the evaluation or substitutes for the subject assertion or semantic Method. For example, `E.21`, `E.9.DA`, or `E.2.DA` may supply the predicate for evaluating one FPF object, while `A.19.ECS` and `C.25` supply supporting quality-model descriptions. `E.19` instead defines an admission or refresh review-gate and findings profile. Use `E.19` as `evaluationPatternLocator` only when its review result is itself the object under evaluation; otherwise its later gate check remains distinct from the quality evaluation.

Not this pattern when the question is already scoped and one direct evaluation is enough. Run the object-under-improvement evaluation directly. Use `E.23` when repeated improvement across passes is needed.

First useful move: write a `QualityEvaluationQuestionFrame` for one object version and a `QualityEvaluationUseDeclaration`. Name the selected `CharacteristicSpace`, the by-value predicate and any admitted comparator, one `U.ClaimScope`, and the work or decision that will consume the result. Keep the evaluation pattern and optional semantic Method separate from the quality-model, evidence-basis, and result-form descriptions. State an evaluator eligibility, independence, capability, or planned condition only when it changes the question or admissibility of the result; name one intended evaluator only when that identity is itself part of the question. Then state the purpose, floor or improvement aim, and protected trade-offs.

Here *move* is Plain wording for writing the frame. It is not a shared Move identity, selected repair, WorkPlan, performed `U.Work`, or actual `U.Transformation`; if dated framing work itself matters, A.15 governs that separate occurrence.

What goes wrong if missed: "review this" can mean too many different things. A floor check may be mistaken for exceptional improvement, a review may suggest work without naming a changed evaluation result, absorption may count closed rows without re-evaluating the changed object, or a follow-up suggestion may be overread as a decision, work plan, gate, evidence, assurance, or release.

What this buys in practice: requester and evaluator start with the same object version, selected characteristic space, criterion or comparator, evaluation scope, consuming use, evaluation purpose, value source, protected trade-offs, evidence basis, and result form. A small floor question can stay small, while a request for proposals or trade-off analysis returns the additional information needed for a later improvement decision.

Primary EntityOfConcern in plain terms: the framed quality-evaluation question for one object version.

A below-floor value, finding, improvement aim, or need for evaluation is not by itself an actual Problem. If the consuming use relies on an actual Problem, cite one current C.22.PFR `ProblematicForRelation` occurrence with its direct participants and temporal identity; the frame, evaluation, result, and evidence may support a claim about it but neither create nor split it.

