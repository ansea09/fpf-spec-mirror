---
chunk_kind: "child"
pattern_id: "A.16"
pattern_title: "Language-State Move Coordination"
section_id: "A.16:14"
section_title: "Worked Move Notes"
source_path: "FPF-Spec.md"
output_path: "by_section/A.16/A.16__015_worked-move-notes.md"
commit_sha: "205de763b710fe9f2baecbcdae132ec8fdbbe38c"
heading_path:
  - "A.16 — Language-State Move Coordination"
  - "A.16:14 — Worked Move Notes"
line_start: 22193
line_end: 22220
dependencies:
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
  - "E.18"
keywords:
  - "admissible move"
  - "handoff"
  - "language-state"
  - "move"
  - "reopen"
  - "respecify"
  - "retire"
  - "sketch-backoff"
---

### A.16:14 - Worked Move Notes

#### A.16:14.1 - Incident-control move note
An operator alert note about a production disturbance may move:

`notice -> stabilize -> route -> operationalize`

The alert note does not need to become an anomaly statement immediately. It may first become a cue pack, then a routed cue set, and only then a typed operational form under the governing pattern.

#### A.16:14.2 - Inquiry move note
An inquiry cue pack about a model-vs-observation discrepancy may move:

`notice -> stabilize -> route -> projection -> formalize`

Later, if the selected framing over-commits, the admissible continuation may be:

`reopen -> sketchBackoff -> respecify`

#### A.16:14.3 - Retired branch
A routed cue set may initially keep both evaluative and abductive routes live. If later review shows the evaluative branch was unsupported, the admissible continuation is not silent disappearance but explicit retirement of that branch, while the abductive branch remains current.

#### A.16:14.4 - False-maturity leap to reject
The following is not admissible:

`notice -> gate decision`

unless explicit intermediate publication and governing pattern transitions justify it. The trajectory discipline exists precisely to block such invisible leaps.

