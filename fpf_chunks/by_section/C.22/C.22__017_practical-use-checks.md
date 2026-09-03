---
chunk_kind: "child"
pattern_id: "C.22"
pattern_title: "Task Typing and TaskSignature Assignment (Problem-CHR)"
section_id: "C.22:14"
section_title: "Practical Use Checks"
source_path: "FPF-Spec.md"
output_path: "by_section/C.22/C.22__017_practical-use-checks.md"
commit_sha: "59c455329e49715c64dc1b16f22c1efba6a3cf6f"
heading_path:
  - "C.22 — Task Typing and TaskSignature Assignment (Problem-CHR)"
  - "C.22:14 — Practical Use Checks"
line_start: 52016
line_end: 52022
dependencies:
  - "A.6.0"
  - "C.16"
  - "C.18"
  - "C.19"
  - "C.22.1"
  - "C.22.2"
  - "C.23"
  - "C.32.P2S"
  - "E.10"
  - "E.18"
  - "F.9"
  - "G.0"
  - "G.4"
  - "G.5"
keywords:
---

### C.22:14 - Practical Use Checks

- If two candidate approaches are answering different `TaskKind`s or different `ScopeSlice(G)` cuts, a direct comparison is not admissible yet.
- If specialization is the live specialization question, the task-family reference, threshold target, adaptation budget, and provenance basis should already be recoverable from the assigned `TaskSignature` edition.
- If crossing, normalization, or missingness changes what comparison means, state that in the signature and its cited refs rather than hiding it in code, local memory, or explanatory prose.
- If `QD` or `OEE` heads are in scope, archive and generator fields belong in the same typed signature rather than in a detached explanatory appendix.

