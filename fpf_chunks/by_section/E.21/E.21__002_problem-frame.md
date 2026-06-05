---
chunk_kind: "child"
pattern_id: "E.21"
pattern_title: "FPF Pattern-Quality Evaluation CharacteristicSpace"
section_id: "E.21:1"
section_title: "Problem frame"
source_path: "FPF-Spec.md"
output_path: "by_section/E.21/E.21__002_problem-frame.md"
commit_sha: "eaafd3a43b9173706e1f8388a3bc94c6445397e4"
heading_path:
  - "E.21 — FPF Pattern-Quality Evaluation CharacteristicSpace"
  - "E.21:1 — Problem frame"
line_start: 67288
line_end: 67301
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

Use `E.21` when one authored FPF pattern version must be evaluated for quality under a declared use: ordinary practitioner use, authoring input, landing input, release input, external-review input, high-assurance reuse input, canonization input, or a narrower named use.

Not this pattern when the evaluated object is one `DRR`, an FPF-level corpus object, a single wording repair, a source-use decision, or a project-side evidence, assurance, gate, release, safety, compliance, work, or decision claim. Use `E.9.DA`, `E.2.DA`, `E.10` and exact precision-restoration neighbours, or the exact project-side pattern for those objects.

First useful move: name the exact pattern version, declared scope, working reader, intended use, and qualification window; then evaluate every coordinate in `RequiredPatternQualityCoordinates` with a value and short rationale.

`floorEvaluation` changes the declared floor and evidence depth. It does not remove coordinates. Fragmentary, wrong-shaped, or weak pattern text is still evaluated; weakness receives low coordinate values, repair status, narrowed-use status, or architecture hold.

What goes wrong if missed: pattern quality becomes taste, checklist closure, source count, review state, landing state, or length. Short patterns can pass while missing mature content; long patterns can pass while hiding the first user move; semio material can take over a non-semio pattern.

Primary EntityOfConcern in plain terms: the quality claim of one exact FPF pattern version for a declared use.

