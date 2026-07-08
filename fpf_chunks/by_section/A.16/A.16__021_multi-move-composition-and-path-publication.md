---
chunk_kind: "child"
pattern_id: "A.16"
pattern_title: "Language-State Move Coordination"
section_id: "A.16:20"
section_title: "Multi-Move Composition and Path Publication"
source_path: "FPF-Spec.md"
output_path: "by_section/A.16/A.16__021_multi-move-composition-and-path-publication.md"
commit_sha: "c927fef1dac0f4d5f8ca93deef8a52de75e3f77b"
heading_path:
  - "A.16 — Language-State Move Coordination"
  - "A.16:20 — Multi-Move Composition and Path Publication"
line_start: 23854
line_end: 23867
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

### A.16:20 - Multi-Move Composition and Path Publication

#### A.16:20.1 - Compound move rule
Many published histories are short move chains such as `notice -> stabilize -> route -> projection` into `U.AbductivePrompt`, or `endpoint-pattern-publication-issued -> reopen -> sketchBackoff -> route`. A conforming publication may summarize such a chain only if the intermediate governing pattern transitions remain reconstructible.

#### A.16:20.2 - Move-by-move authority reading
Read authority move by move. A later move to higher closure state, route authority state, or endpoint authority claim does not retroactively authorize earlier lower-articulation forms, and later retreat or retirement does not erase the fact that the later route or endpoint authority state once existed.

#### A.16:20.3 - `A.16.0` threshold
When a move history acquires lineage governance value, publish it through `A.16.0` rather than overloading one local move note with hidden lineage structure.

#### A.16:20.4 - `E.18` threshold
When the history must be published as a path publication in a graph sense, reuse `E.18`. `A.16` still governs move semantics.

