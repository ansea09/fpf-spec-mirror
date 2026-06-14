---
chunk_kind: "child"
pattern_id: "A.16"
pattern_title: "Language-State Move Coordination"
section_id: "A.16:17"
section_title: "Move Package Discipline"
source_path: "FPF-Spec.md"
output_path: "by_section/A.16/A.16__018_move-package-discipline.md"
commit_sha: "7c617d5d0fa1abf94a21bac2dd909f68ed514249"
heading_path:
  - "A.16 — Language-State Move Coordination"
  - "A.16:17 — Move Package Discipline"
line_start: 22530
line_end: 22552
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

### A.16:17 - Move Package Discipline

Publish moves as small typed move notes rather than as narrative adjectives.

#### A.16:17.1 - Minimal move note
A conforming move note should name:

- the **source publication form**,
- the **target publication form**,
- the **target governing pattern**,
- the **move kind**,
- the **facet or route-state changes** that justify the move,
- the **authority effect**,
- and the **witnesses or traces** that preserve continuity.

If those fields already make the move reconstructible, the note does not need `A.16.0`.

#### A.16:17.2 - Source and target must both be typed
"The episteme was refined" is insufficient. `A.16` requires a typed source publication form and a typed target publication form so governing pattern boundaries stay visible.

#### A.16:17.3 - Witness continuity
Keep continuity explicit when anchors, contrasts, traces, or exemplars survive. If continuity breaks, state the break directly rather than smoothing it over in maturity prose.

