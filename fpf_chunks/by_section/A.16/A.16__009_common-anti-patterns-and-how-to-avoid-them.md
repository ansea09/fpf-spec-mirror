---
chunk_kind: "child"
pattern_id: "A.16"
pattern_title: "Language-State Move Coordination"
section_id: "A.16:8"
section_title: "Common Anti-Patterns and How to Avoid Them"
source_path: "FPF-Spec.md"
output_path: "by_section/A.16/A.16__009_common-anti-patterns-and-how-to-avoid-them.md"
commit_sha: "504747d26299e3963dc0457bf48d4e2a791d926a"
heading_path:
  - "A.16 — Language-State Move Coordination"
  - "A.16:8 — Common Anti-Patterns and How to Avoid Them"
line_start: 26513
line_end: 26520
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

### A.16:8 - Common Anti-Patterns and How to Avoid Them
- **Trajectory-wrapper inflation.** Do not wrap every local move in `A.16.0`. Publish a local move note unless history has lineage governance value.
- **Governing-pattern-as-form collapse.** Do not write as if `A.6.P`, `B.5.2`, or `A.15` were publication forms. Name the pattern-governed form and the governing pattern separately.
- **Form-face collapse.** Do not treat an MVPK face as if it were the publication form itself. Name both when both matter.
- **Irreversible maturity story.** Reopen, sketch-backoff, respecify, and retirement are admissible moves, not failures of the trajectory discipline.
- **Silent branch retirement.** Do not let one route or branch disappear without a retirement or supersession note.
- **Route and fork confusion.** Several live routes in one `RoutedCueSet` are not yet a lineage fork.

