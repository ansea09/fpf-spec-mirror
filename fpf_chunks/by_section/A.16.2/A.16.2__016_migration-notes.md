---
chunk_kind: "child"
pattern_id: "A.16.2"
pattern_title: "Reopen / SketchBackoff / Respecify"
section_id: "A.16.2:15"
section_title: "Migration Notes"
source_path: "FPF-Spec.md"
output_path: "by_section/A.16.2/A.16.2__016_migration-notes.md"
commit_sha: "60caecb4751fb2a3623a1faaca757d29a19acff9"
heading_path:
  - "A.16.2 — Reopen / SketchBackoff / Respecify"
  - "A.16.2:15 — Migration Notes"
line_start: 27500
line_end: 27507
dependencies:
  - "A.16"
  - "A.16.0"
  - "A.16.1"
  - "A.6.A"
  - "A.6.P"
  - "B.4.1"
  - "B.5.2"
  - "C.16.Q"
  - "C.2.2a"
  - "C.2.5"
keywords:
  - "authority withdrawal"
  - "backoff"
  - "branch withdrawal"
  - "reopen"
  - "respecify"
  - "retire"
  - "retreat"
---

### A.16.2:15 - Migration Notes

#### A.16.2:15.1 - Migration from regression language
Older language often talks about "going backwards" or "regressing". The preferred migration is to name whether the change is reopen, sketch-backoff, respecify, or retire, and what boundary or authority consequence follows.

#### A.16.2:15.2 - Integration reminder
When retreat affects governing patterns such as `A.6.P`, `A.6.A`, `C.16.Q`, or `A.15`, those governing patterns should be updated explicitly rather than left to drift on stale authority.

