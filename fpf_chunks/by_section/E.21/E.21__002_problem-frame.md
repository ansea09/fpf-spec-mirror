---
chunk_kind: "child"
pattern_id: "E.21"
pattern_title: "FPF Pattern-Quality Evaluation CharacteristicSpace"
section_id: "E.21:1"
section_title: "Problem frame"
source_path: "FPF-Spec.md"
output_path: "by_section/E.21/E.21__002_problem-frame.md"
commit_sha: "0990ff1d1ccee4587b8f7e16e7a725a8edbe66b4"
heading_path:
  - "E.21 — FPF Pattern-Quality Evaluation CharacteristicSpace"
  - "E.21:1 — Problem frame"
line_start: 83480
line_end: 83495
dependencies:
  - "A.17-A.19"
  - "A.19.ECS"
  - "A.6.P"
  - "C.16"
  - "C.2.P"
  - "C.25"
  - "E.10"
  - "E.11"
  - "E.19"
  - "E.2.DA"
  - "E.22"
  - "E.23"
  - "E.8"
  - "E.9.DA"
  - "F.18"
  - "F.19"
  - "I.2"
keywords:
---

### E.21:1 - Problem frame

Use this when one authored FPF pattern of concern must be evaluated for quality under the use required by the governing evaluation frame: ordinary practitioner use, authoring input, landing input, release input, external-review input, high-assurance reuse input, canonization input, or another explicitly requested pattern-quality use. The evaluator does not replace the required `ClaimScope` with an easier one. If the pattern fails the required use, the result is `repairBeforeUse`, `holdForArchitectureDecision`, or `refreshNeeded`; a different use needs a different evaluation frame and does not rescue the current result.

Not this pattern when the evaluated object is one `DRR`, an FPF-level corpus object, a single wording repair, a source-use decision, or a project-side evidence, assurance, gate, release, safety, compliance, work, or decision claim. Use `E.9.DA`, `E.2.DA`, `E.10` and precision-restoration neighboring patterns named by value, or the project-side pattern governing the claim for those objects.

First useful move: recover the required scope from the governing request, `E.22` frame, campaign seam, landing check, release check, or review assignment; then name the governing pattern of concern, required scope, working reader, intended use, and qualification window; then evaluate every coordinate in `RequiredPatternQualityCoordinates` with a value and short rationale.

`floorEvaluation` changes the declared floor and expected evidence economy. It never creates a partial `E.21`, inactive coordinates, overlay-trigger shortcuts, narrowing to an easier use, blocker-only substitution, or a permission to skip precision-restoration discharge. Fragmentary, wrong-shaped, or weak pattern text is still evaluated under the required scope; weakness receives low coordinate values, repair status, architecture hold, or refresh status.

What goes wrong if missed: pattern quality becomes taste, checklist closure, source count, review state, landing state, or length. Short patterns can pass while missing mature content; long patterns can pass while hiding the first user-facing action; semio material can take over a non-semio pattern.

What this pattern buys: one scoped quality claim over one pattern of concern, one complete coordinate set, explicit evidence basis, adjacent-value rationales, and a visible stop, repair, hold, or refresh status.

Primary EntityOfConcern in plain terms: the quality claim of one governing FPF pattern of concern for a declared use.

