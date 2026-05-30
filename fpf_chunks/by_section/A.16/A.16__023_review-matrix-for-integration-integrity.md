---
chunk_kind: "child"
pattern_id: "A.16"
pattern_title: "Language-State Transduction Coordination"
section_id: "A.16:22"
section_title: "Review Matrix for Integration Integrity"
source_path: "FPF-Spec.md"
output_path: "by_section/A.16/A.16__023_review-matrix-for-integration-integrity.md"
commit_sha: "2e112078bb209e5e3a511c3bd1aa6b1b2e299efe"
heading_path:
  - "A.16 — Language-State Transduction Coordination"
  - "A.16:22 — Review Matrix for Integration Integrity"
line_start: 21867
line_end: 21878
dependencies:
  - "A.16.0"
  - "A.16.0-A.16.2"
  - "A.16.1"
  - "A.16.2"
  - "A.18"
  - "A.19"
  - "A.6.A"
  - "A.6.P"
  - "A.6.Q"
  - "B.4.1"
  - "B.5.2.0"
  - "C.2.2a"
  - "C.2.4"
  - "C.2.5"
  - "C.2.6"
  - "C.2.7"
  - "C.2.LS"
  - "E.18"
keywords:
  - "admissible moves"
  - "handoff"
  - "language-state"
  - "reopen"
  - "respecify"
  - "retire"
  - "sketch-backoff"
  - "transduction"
---

### A.16:22 - Review Matrix for Integration Integrity

A reviewer can test an `A.16` move or move chain with six questions:

1. **Are the source publication form and target publication form typed?** If not, the move is too vague.
2. **Are governing pattern and face kept distinct from the form?** If not, the move collapses layers.
3. **Is the authority effect explicit?** If not, receiving governing pattern boundaries will drift.
4. **Is route plurality being confused with lineage fork?** If yes, the history is being misread.
5. **Are intermediate move publications suppressed in a way that changes the reading?** If yes, the chain is over-compressed.
6. **Has `A.16` started to impersonate a receiving governing pattern or a trajectory wrapper?** If yes, the relevant receiving governing pattern or `A.16.0` threshold needs to be named explicitly.

This matrix keeps the integration layer narrow while still making its move semantics inspectable.
