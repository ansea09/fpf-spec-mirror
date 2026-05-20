---
chunk_kind: "child"
pattern_id: "C.22"
pattern_title: "Problem Typing & TaskSignature Assignment (Problem-CHR)"
section_id: "C.22:13"
section_title: "Practical reading checks"
source_path: "FPF-Spec.md"
output_path: "by_section/C.22/C.22__014_practical-reading-checks.md"
commit_sha: "LOCAL_TEST"
heading_path:
  - "C.22 — Problem Typing & TaskSignature Assignment (Problem-CHR)"
  - "C.22:13 — Practical reading checks"
line_start: 41515
line_end: 41521
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

### C.22:13 - Practical reading checks

- If two candidate approaches are answering different `TaskKind`s or different `ScopeSlice(G)` cuts, this pattern does not yet license a direct comparison.
- If specialization is the live specialization question, the task-family anchor, threshold target, adaptation budget, and provenance basis should already be recoverable from the attached `TaskSignature`.
- If crossing, normalization, or missingness changes what comparison means, publish that in the signature and its cited refs rather than hiding it in code, local memory, or later prose.
- If `QD` or `OEE` heads are in scope, archive and generator fields belong in the same typed signature rather than in a detached explanatory appendix.

