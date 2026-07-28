---
chunk_kind: "child"
pattern_id: "A.16"
pattern_title: "Language-State Move Coordination"
section_id: "A.16:19"
section_title: "Worked Failure and Recovery Cases"
source_path: "FPF-Spec.md"
output_path: "by_section/A.16/A.16__020_worked-failure-and-recovery-cases.md"
commit_sha: "4b75b56c13f5d61be5238fdbc7c20af5c6f89df7"
heading_path:
  - "A.16 — Language-State Move Coordination"
  - "A.16:19 — Worked Failure and Recovery Cases"
line_start: 26912
line_end: 26928
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

### A.16:19 - Worked Failure and Recovery Cases

#### A.16:19.1 - Premature endpoint capture
A low-articulation cue is observed and quickly described as if it were already a requirement. Under `A.16`, this is rejected because the move history is missing: the publication should first be noticed, stabilized, and route-published. The recovery is not to defend the over-committing label, but to reopen and publish the earlier route-bearing form.

#### A.16:19.2 - Silent route drift
A note begins as evaluative pressure but later starts driving work planning. If this shift is not published, the route drift remains invisible. `A.16` requires either a new route-bearing publication, an explicit operationalization note, or an explicit responsibility transfer to a governing pattern.

#### A.16:19.3 - admissible retreat after over-formalization
A note is formalized too early into a relation-like shape, but later review shows the anchors are still unstable. The correct continuation is not to leave the relation form in place and quietly reinterpret it. The correct continuation is `reopen -> sketchBackoff`, preserving what still holds and lowering the authority of what no longer does.

#### A.16:19.4 - Silent branch disappearance
A route-bearing publication originally kept two candidate routes live. Later text talks only as if one route ever existed. Reviewers should treat that as silent branch laundering unless the abandoned route was explicitly retired, merged, or shown never to have become a distinct branch.

#### A.16:19.5 - Form-governing pattern-face collapse
A note says only `the move publishes a Tech face` or `the move enters A.6.P` and never names the actual publication form. That wording is non-conforming because it collapses three different layers into one phrase. The repair is to name the publication form first, then the governing pattern, then the MVPK face if the face matters for rendering or review.

