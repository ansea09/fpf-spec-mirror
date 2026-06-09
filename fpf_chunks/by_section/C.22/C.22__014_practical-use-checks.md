---
chunk_kind: "child"
pattern_id: "C.22"
pattern_title: "Problem Typing & TaskSignature Assignment (Problem-CHR)"
section_id: "C.22:13"
section_title: "Practical use checks"
source_path: "FPF-Spec.md"
output_path: "by_section/C.22/C.22__014_practical-use-checks.md"
commit_sha: "093d30e806a1466e24032733eb020bb5a5f585cc"
heading_path:
  - "C.22 — Problem Typing & TaskSignature Assignment (Problem-CHR)"
  - "C.22:13 — Practical use checks"
line_start: 44165
line_end: 44171
dependencies:
  - "C.16"
  - "C.18"
  - "C.19"
  - "C.22.1"
  - "C.23"
  - "E.10"
  - "E.18"
  - "G.0"
  - "G.4"
  - "G.5"
keywords:
  - "Problem‑CHR"
  - "ScopeSlice(G)"
  - "TaskKind"
  - "TaskSignature"
  - "specialization anchor"
  - "unknown handling"
---

### C.22:13 - Practical use checks

- If two candidate approaches are answering different `TaskKind`s or different `ScopeSlice(G)` cuts, a direct comparison is not admissible yet.
- If specialization is the live specialization question, the task-family reference, threshold target, adaptation budget, and provenance basis should already be recoverable from the attached `TaskSignature`.
- If crossing, normalization, or missingness changes what comparison means, state that in the signature and its cited refs rather than hiding it in code, local memory, or later prose.
- If `QD` or `OEE` heads are in scope, archive and generator fields belong in the same typed signature rather than in a detached explanatory appendix.

