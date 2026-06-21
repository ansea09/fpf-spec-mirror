---
chunk_kind: "child"
pattern_id: "C.22"
pattern_title: "Problem Typing & TaskSignature Assignment (Problem-CHR)"
section_id: "C.22:12.1"
section_title: "SoTA-Echoing"
source_path: "FPF-Spec.md"
output_path: "by_section/C.22/C.22__015_sota-echoing.md"
commit_sha: "fe0df9dcb06cfc87c8a6cb2f7cce3ac0d3b64d5e"
heading_path:
  - "C.22 — Problem Typing & TaskSignature Assignment (Problem-CHR)"
  - "C.22:12.1 — SoTA-Echoing"
line_start: 46034
line_end: 46037
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

### C.22:12.1 - SoTA-Echoing

C.22 follows contemporary selector and optimization practice by refusing one universal “best method” view: a typed problem attachment states the task family, admissible characteristics, constraints, evidence, and unknown-handling policy before a selector compares candidates. Modern multi-objective optimization, QD archive practice, open-ended generation, and solver-interface practice all support the same boundary: selection works over typed problem cases and admissible comparison rules, not over prose labels or popularity. The pattern therefore keeps the problem-side record separate from method choice, keeps scalarization in Acceptance or CAL policy, and keeps archive or generator telemetry out of dominance unless a governing policy admits it.

