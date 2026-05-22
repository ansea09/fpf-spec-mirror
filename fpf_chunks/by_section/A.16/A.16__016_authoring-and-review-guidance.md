---
chunk_kind: "child"
pattern_id: "A.16"
pattern_title: "Language-State Transduction Coordination"
section_id: "A.16:15"
section_title: "Authoring and Review Guidance"
source_path: "FPF-Spec.md"
output_path: "by_section/A.16/A.16__016_authoring-and-review-guidance.md"
commit_sha: "725f0b7b372754cda3f6f4e15184215da568fc4d"
heading_path:
  - "A.16 — Language-State Transduction Coordination"
  - "A.16:15 — Authoring and Review Guidance"
line_start: 21261
line_end: 21285
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

### A.16:15 - Authoring and Review Guidance

#### A.16:15.1 - Author prompt
When naming a move, the author should say:

- what the source publication form is,
- what the target publication form is,
- which governing pattern governs the target form,
- which MVPK face matters if rendering matters,
- which facet or route-state change justifies the move,
- what authority effect follows,
- and what remains invariant.

#### A.16:15.2 - Review prompt
A reviewer should ask:

- is the move a real transduction or just rhetorical relabeling?
- does the move preserve witnesses and route provenance appropriately?
- is route plurality being confused with lineage fork?
- did a receiving governing pattern silently absorb the publication too early?
- if retreat or retirement occurred, was the authority drop made explicit?

#### A.16:15.3 - Integration reminder
When path publication becomes important as a graph publication in itself, move semantics stay in `A.16`, the optional history package stays in `A.16.0`, and the path publication still belongs to `E.18`.

