---
chunk_kind: "child"
pattern_id: "A.16"
pattern_title: "Language-State Move Coordination"
section_id: "A.16:22"
section_title: "Review Matrix for Integration Integrity"
source_path: "FPF-Spec.md"
output_path: "by_section/A.16/A.16__023_review-matrix-for-integration-integrity.md"
commit_sha: "1602a8d0a6934a99a79ead914610b070cedd86d2"
heading_path:
  - "A.16 — Language-State Move Coordination"
  - "A.16:22 — Review Matrix for Integration Integrity"
line_start: 27344
line_end: 27355
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

### A.16:22 - Review Matrix for Integration Integrity

A reviewer can test an `A.16` move or move chain with six questions:

1. **Are the source publication form and target publication form typed?** If not, the move is too vague.
2. **Are the cited pattern's concrete contribution and the face kept distinct from the form?** If not, the move collapses positions.
3. **Is the authority effect explicit?** If not, the endpoint rule and use boundary will drift.
4. **Is route plurality being confused with lineage fork?** If yes, the history is being misread.
5. **Are intermediate move publications suppressed in a way that changes the reading?** If yes, the chain is over-compressed.
6. **Has `A.16` started to replace an endpoint rule or a trajectory wrapper?** If yes, use the applicable endpoint pattern or `A.16.0` explicitly.

This matrix keeps the integration layer narrow while still making its move semantics inspectable.
