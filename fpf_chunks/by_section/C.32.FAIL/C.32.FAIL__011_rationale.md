---
chunk_kind: "child"
pattern_id: "C.32.FAIL"
pattern_title: "Architecture Failure Recognition and Repair"
section_id: "C.32.FAIL:10"
section_title: "Rationale"
source_path: "FPF-Spec.md"
output_path: "by_section/C.32.FAIL/C.32.FAIL__011_rationale.md"
commit_sha: "3bc659a6f866071f629bf41fc2dd41f2518e579a"
heading_path:
  - "C.32.FAIL — Architecture Failure Recognition and Repair"
  - "C.32.FAIL:10 — Rationale"
line_start: 64817
line_end: 64822
dependencies:
  - "A.10"
  - "A.15"
  - "A.19.CPM"
  - "A.19.SelectorMechanism"
  - "A.20"
  - "A.21"
  - "A.6.F"
  - "A.6.M"
  - "A.6.P"
  - "B.3"
  - "C.11"
  - "C.18"
  - "C.19"
  - "C.19.1"
  - "C.27"
  - "C.29"
  - "C.30"
  - "C.30.AD"
  - "C.30.ASV"
  - "C.30.P"
  - "C.31"
  - "C.32"
  - "C.32.CONWAY"
  - "C.32.MLAO"
  - "C.32.P2S"
  - "C.32.PAD"
  - "E.10"
  - "E.17"
  - "E.18"
  - "E.24.PUB"
  - "G.5"
keywords:
  - "architecture failure cue"
  - "architecture repair cue"
  - "candidate repair"
  - "repair-entry family"
  - "selected-structure relation"
  - "source overread"
  - "stressed architecture object"
---

### C.32.FAIL:10 - Rationale

C.32 needs a failure-recognition subpattern because candidate architecture work repeatedly breaks at the repair-entry point. The useful work is not to collect more warnings. The useful work is to recover the architecture object under stress and make the next repair action reviewable.

The pattern stays intentionally small. It does not establish failure, make a score-based risk finding, select a candidate, or authorize a release. It gives practitioners a disciplined way to go from "something is wrong here" to "this architecture object needs this repair, and this neighboring pattern governs the next claim if it is current."

