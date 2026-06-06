---
chunk_kind: "child"
pattern_id: "E.21"
pattern_title: "FPF Pattern-Quality Evaluation CharacteristicSpace"
section_id: "E.21:1"
section_title: "Problem frame"
source_path: "FPF-Spec.md"
output_path: "by_section/E.21/E.21__002_problem-frame.md"
commit_sha: "e3fedf42dc7cb5d12905913b5a0b0e951ed7d254"
heading_path:
  - "E.21 — FPF Pattern-Quality Evaluation CharacteristicSpace"
  - "E.21:1 — Problem frame"
line_start: 67286
line_end: 67299
dependencies:
  - "A.17-A.19"
  - "A.19.ECS"
  - "A.6.P"
  - "C.16"
  - "C.2.P"
  - "C.25"
  - "E.10"
  - "E.19"
  - "E.2.DA"
  - "E.22"
  - "E.23"
  - "E.8"
  - "E.9.DA"
  - "F.18"
  - "J.4"
keywords:
---

### E.21:1 - Problem frame

Use `E.21` when one authored FPF pattern version must be evaluated for quality under the use required by the governing evaluation frame: ordinary practitioner use, authoring input, landing input, release input, external-review input, high-assurance reuse input, canonization input, diagnostic use, expert-only use, source-basis use, or local-reference use. The evaluator does not replace the required `ClaimScope` with an easier one. If the pattern fails the required use, the result is `repairBeforeUse`, `holdForArchitectureDecision`, or `refreshNeeded`; a different use needs a different evaluation frame and does not rescue the current result.

Not this pattern when the evaluated object is one `DRR`, an FPF-level corpus object, a single wording repair, a source-use decision, or a project-side evidence, assurance, gate, release, safety, compliance, work, or decision claim. Use `E.9.DA`, `E.2.DA`, `E.10` and exact precision-restoration neighbours, or the exact project-side pattern for those objects.

First useful move: recover the required scope from the governing request, `E.22` frame, campaign seam, landing check, release check, or review assignment; then name the exact pattern version, required scope, working reader, intended use, and qualification window; then evaluate every coordinate in `RequiredPatternQualityCoordinates` with a value and short rationale.

`floorEvaluation` changes the declared floor and evidence depth. It does not remove coordinates and does not replace the required scope with another one. Fragmentary, wrong-shaped, or weak pattern text is still evaluated under the required scope; weakness receives low coordinate values, repair status, architecture hold, or refresh status.

What goes wrong if missed: pattern quality becomes taste, checklist closure, source count, review state, landing state, or length. Short patterns can pass while missing mature content; long patterns can pass while hiding the first user move; semio material can take over a non-semio pattern.

Primary EntityOfConcern in plain terms: the quality claim of one exact FPF pattern version for a declared use.

