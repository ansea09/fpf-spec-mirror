---
chunk_kind: "child"
pattern_id: "A.16.0"
pattern_title: "U.LanguageStateMoveTrajectory - Optional trajectory-account normal form over the language-state U.CharacteristicSpace"
section_id: "A.16.0:intro"
section_title: "Intro"
source_path: "FPF-Spec.md"
output_path: "by_section/A.16.0/A.16.0__001_intro.md"
commit_sha: "59c455329e49715c64dc1b16f22c1efba6a3cf6f"
heading_path:
  - "A.16.0 — U.LanguageStateMoveTrajectory - Optional trajectory-account normal form over the language-state U.CharacteristicSpace"
  - "A.16.0:intro — Intro"
line_start: 28683
line_end: 28702
dependencies:
  - "A.16"
  - "A.16.1"
  - "A.16.2"
  - "A.19"
  - "A.6.A"
  - "A.6.P"
  - "B.4.1"
  - "B.5.2"
  - "B.5.2.0"
  - "C.16.Q"
  - "C.2.2a"
  - "C.2.LS"
  - "E.10.MOVE"
  - "E.17"
  - "E.17.1"
  - "E.18"
  - "F.9"
  - "F.9.1"
keywords:
  - "fork"
  - "heavy history"
  - "lineage"
  - "merge"
  - "responsibility transfer"
  - "supersedes"
  - "trajectory account"
---

## A.16.0 - `U.LanguageStateMoveTrajectory` - Optional trajectory-account normal form over the language-state `U.CharacteristicSpace`

> **Type:** Architectural (A)
> **Status:** Stable
> **Normativity:** Normative unless marked informative

**Plain-name.** Language-state move trajectory.

**Builds on.**
`C.2.2a`, `A.16`, `A.19`, `E.17`, `E.18`, `E.10`, `F.18`.

**Used by.**
`A.16.1`, `A.16.2`, `B.4.1`, `B.5.2.0`, `A.6.P`, `C.16.Q`, `A.6.A`, `F.9.1`, `E.17.1`.

**Use this when.** Use this pattern when one local language-state move is no longer enough because a reviewable history must keep episteme editions, publication forms, branches, retirements, or losses visible, or because an actual responsibility handoff depends on that history.

**What goes wrong if missed.** Readers treat cue packs, routed cue sets, endpoint-bound publications, and next-use dockings as one thing magically moving; forks, losses, authority changes, and work-requiring crossings become implicit, and an actual responsibility change may be mistaken for semantic docking.

**What this buys.** One optional trajectory account that records lineage, position claims, move kinds, publication forms, losses, and the next use and authority boundary without wrapping every local `A.16` move in heavy history machinery.

