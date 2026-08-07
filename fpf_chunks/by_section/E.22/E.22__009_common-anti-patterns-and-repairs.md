---
chunk_kind: "child"
pattern_id: "E.22"
pattern_title: "Improvement-Oriented Quality Evaluation Question Framing"
section_id: "E.22:8"
section_title: "Common anti-patterns and repairs"
source_path: "FPF-Spec.md"
output_path: "by_section/E.22/E.22__009_common-anti-patterns-and-repairs.md"
commit_sha: "1602a8d0a6934a99a79ead914610b070cedd86d2"
heading_path:
  - "E.22 — Improvement-Oriented Quality Evaluation Question Framing"
  - "E.22:8 — Common anti-patterns and repairs"
line_start: 87409
line_end: 87424
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

### E.22:8 - Common anti-patterns and repairs

| Anti-pattern | Repair |
|---|---|
| **"Review this" prompt.** The evaluator infers purpose. | Add a `QualityEvaluationQuestionFrame` with exact object version, space, criterion, ClaimScope, consumer, purpose, and boundary. |
| **Context-labelled frame.** Project, domain, dashboard, cadence, or context label supplies identity or evaluation scope. | Identify the frame by its C.2.1 claim content and exact EntityOfConcern; bind the exact `U.ClaimScope` and other use values separately. |
| **Floor pass sold as excellence.** Readiness is mistaken for exceptional improvement. | State `exceptionalImprovementEvaluation` if wanted. |
| **Frame replaces result.** The question frame names a purpose but returns prose, a two-column value table, or proposal rows without the named evaluation's result form. | Re-run the named evaluation as dated Work with its direct method enactment or A.6.1 operation application and return its declared coordinates, evidence basis, rationales, payload fields, and typed result binding or direct result relation. |
| **Description performs evaluation.** A method description, characteristic-space specification, expected evidence basis, role assignment, or result-form description is treated as evaluation Work or its result. | Keep each description and assignment separate; identify one dated A.15.1 Work occurrence, the direct evaluation application, actual evidence use, and result under their exact governors. |
| **Scope laundering.** The frame asks one use, but the result answers an easier, local-only, diagnostic, or evaluator-selected use. | Re-run the named evaluation under the requested `U.ClaimScope`; if another use is needed, open a new frame rather than saving the current result. |
| **Applied-count absorption.** Closure count replaces re-evaluation of the changed object. | Re-evaluate the changed object and classify impact. |
| **Goodharted improvement.** Visible values rise while protected qualities worsen, or a `5` target makes the evaluator add apparatus instead of improving content. | Frame the expected evaluation effect as a substantive content change, add trade-off protection, reject dominated changes, apply E.13 when a visible value replaces the intended value, and admit `no proposal` only when checked positions show that no worthwhile content improvement remains. |
| **Recommendation as decision.** A follow-up hypothesis is treated as chosen work. | Open the exact decision, work, publication, parity, refresh, evidence, or assurance pattern if that claim is needed. |
| **Finding as actual Problem.** A low coordinate, finding, or floor miss is treated as a Problem occurrence. | Keep the evaluation result epistemic; cite C.22.PFR only when its actual-condition and criterion-applicability participants make one ProblematicFor occurrence obtain. |
| **Lexical repair request.** A finding says only "replace this word" or "avoid that wording." | Rewrite the row as a precision-restoration finding with kind, relation, admissible use, and scope before and after repair; if no kind-preserving repair is recoverable, leave it blocking. |

