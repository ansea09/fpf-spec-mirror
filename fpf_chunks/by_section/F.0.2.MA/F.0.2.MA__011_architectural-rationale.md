---
chunk_kind: "child"
pattern_id: "F.0.2.MA"
pattern_title: "Synthesize and Allocate Method Contributions"
section_id: "F.0.2.MA:10"
section_title: "Architectural Rationale"
source_path: "FPF-Spec.md"
output_path: "by_section/F.0.2.MA/F.0.2.MA__011_architectural-rationale.md"
commit_sha: "c475118bc1c11d2921b14f74c876e69c24ced3ea"
heading_path:
  - "F.0.2.MA — Synthesize and Allocate Method Contributions"
  - "F.0.2.MA:10 — Architectural Rationale"
line_start: 116777
line_end: 116782
dependencies:
  - "A.3.1.DR"
  - "A.3.1.MR"
  - "A.3.1.QM"
  - "B.1.5.CM"
  - "E.8.ML"
  - "F.0.1"
  - "F.0.2"
keywords:
---

### F.0.2.MA:10 - Architectural Rationale

Source recovery answers what the material says. Conceptual synthesis answers what a cross-source comparison warrants. F.0.2.MA uses those results to settle a Method-specific distribution: what reusable action and condition belong in which description or pattern, and what must stay outside.

Keeping this result separate from A.3.1.DR lets documentary recovery remain faithful even when a later allocation rejects a source proposal. Keeping it separate from Method admission prevents a placement decision from creating a Method. Retaining one small allocation before a corpus-wide map keeps the first useful result affordable.

