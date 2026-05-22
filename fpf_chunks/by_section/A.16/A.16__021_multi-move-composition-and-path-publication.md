---
chunk_kind: "child"
pattern_id: "A.16"
pattern_title: "Language-State Transduction Coordination"
section_id: "A.16:20"
section_title: "Multi-Move Composition and Path Publication"
source_path: "FPF-Spec.md"
output_path: "by_section/A.16/A.16__021_multi-move-composition-and-path-publication.md"
commit_sha: "725f0b7b372754cda3f6f4e15184215da568fc4d"
heading_path:
  - "A.16 — Language-State Transduction Coordination"
  - "A.16:20 — Multi-Move Composition and Path Publication"
line_start: 21384
line_end: 21397
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

### A.16:20 - Multi-Move Composition and Path Publication

#### A.16:20.1 - Compound move rule
Many published histories are short move chains such as `notice -> stabilize -> route -> projection` into `U.AbductivePrompt`, or `endpoint-pattern-publication-issued -> reopen -> sketchBackoff -> route`. A conforming publication may summarize such a chain only if the intermediate governing pattern transitions remain reconstructible.

#### A.16:20.2 - Move-by-move authority reading
Read authority move by move. A later move to higher closure state, route authority state, or endpoint authority claim does not retroactively authorize earlier lower-articulation forms, and later retreat or retirement does not erase the fact that the later route or endpoint authority state once existed.

#### A.16:20.3 - `A.16.0` threshold
When a move history acquires lineage governance value, publish it through `A.16.0` rather than overloading one local move note with hidden lineage structure.

#### A.16:20.4 - `E.18` threshold
When the history must be published as a path publication in a graph sense, reuse `E.18`. `A.16` still governs move semantics.

