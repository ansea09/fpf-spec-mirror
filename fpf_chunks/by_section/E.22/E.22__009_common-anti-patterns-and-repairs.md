---
chunk_kind: "child"
pattern_id: "E.22"
pattern_title: "Improvement-Oriented Quality Evaluation Question Framing"
section_id: "E.22:8"
section_title: "Common anti-patterns and repairs"
source_path: "FPF-Spec.md"
output_path: "by_section/E.22/E.22__009_common-anti-patterns-and-repairs.md"
commit_sha: "cb17c555f343780e31e5fea236a74adc69295736"
heading_path:
  - "E.22 — Improvement-Oriented Quality Evaluation Question Framing"
  - "E.22:8 — Common anti-patterns and repairs"
line_start: 70151
line_end: 70163
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

### E.22:8 - Common anti-patterns and repairs

| Anti-pattern | Repair |
|---|---|
| **"Review this" prompt.** The evaluator infers purpose. | Add a `QualityEvaluationQuestionFrame`. |
| **Floor pass sold as excellence.** Readiness is mistaken for exceptional improvement. | State `exceptionalImprovementEvaluation` if wanted. |
| **Frame replaces result.** The question frame names a purpose but returns prose, a two-column value table, or proposal rows without the named evaluation's result form. | Re-run the named evaluation and return its required coordinates, evidence basis, rationales, and payload fields. |
| **Scope laundering.** The frame asks one use, but the result answers an easier, local-only, diagnostic, or evaluator-selected use. | Re-run the named evaluation under the requested use; if another use is needed, open a new frame rather than saving the current result. |
| **Applied-count absorption.** Closure count replaces quality movement. | Re-evaluate the changed object and classify impact. |
| **Goodharted improvement.** Visible values rise while protected qualities worsen, or a `5` target makes the evaluator add apparatus instead of improving content. | Frame the expected movement as a substantive content move, add trade-off protection, reject dominated changes, apply `E.13` when a visible value is replacing the intended value, and require checked `no proposal` dispositions when no worthwhile content move remains. |
| **Recommendation as decision.** A next-move hypothesis is treated as chosen work. | Open the exact decision, work, publication, parity, refresh, evidence, or assurance pattern if that claim is needed. |
| **Lexical repair request.** A finding says only "replace this word" or "avoid that wording." | Rewrite the row as a precision-restoration finding with pre/post kind, relation, admissible use, and scope; if no kind-preserving repair is recoverable, leave it blocking. |

