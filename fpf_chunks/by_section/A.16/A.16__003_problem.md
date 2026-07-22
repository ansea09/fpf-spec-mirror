---
chunk_kind: "child"
pattern_id: "A.16"
pattern_title: "Language-State Move Coordination"
section_id: "A.16:2"
section_title: "Problem"
source_path: "FPF-Spec.md"
output_path: "by_section/A.16/A.16__003_problem.md"
commit_sha: "0990ff1d1ccee4587b8f7e16e7a725a8edbe66b4"
heading_path:
  - "A.16 — Language-State Move Coordination"
  - "A.16:2 — Problem"
line_start: 26330
line_end: 26332
dependencies:
  - "A.16"
  - "A.16.0"
  - "A.16.0-A.16.2"
  - "A.16.1"
  - "A.16.2"
  - "A.18"
  - "A.19"
  - "A.6.A"
  - "A.6.P"
  - "B.4.1"
  - "B.5.2.0"
  - "C.16.Q"
  - "C.2.2a"
  - "C.2.4"
  - "C.2.5"
  - "C.2.6"
  - "C.2.7"
  - "C.2.LS"
  - "E.10.MOVE"
  - "E.18"
keywords:
  - "admissible language-state move"
  - "language-state"
  - "move"
  - "reopen"
  - "respecify"
  - "responsibility transfer"
  - "retire"
  - "sketch-backoff"
---

### A.16:2 - Problem
Without a dedicated coordination pattern, authors either misuse `F0-F9`, force every cue into anomaly/problem language too early, let reopen and backoff happen informally with no explicit guards, or over-wrap every local move in a meta-account that should have remained optional.

