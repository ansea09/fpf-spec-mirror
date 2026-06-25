---
chunk_kind: "child"
pattern_id: "C.11"
pattern_title: "Decision Theory (Decsn-CAL)"
section_id: "C.11:10"
section_title: "Rationale"
source_path: "FPF-Spec.md"
output_path: "by_section/C.11/C.11__011_rationale.md"
commit_sha: "792091cf6f89f21f3423d75c72238bb0982777f2"
heading_path:
  - "C.11 — Decision Theory (Decsn-CAL)"
  - "C.11:10 — Rationale"
line_start: 42470
line_end: 42481
dependencies:
  - "A.13"
  - "A.18"
  - "A.19"
  - "A.6.5"
  - "A.6.P"
  - "C.18"
  - "C.19"
  - "C.24"
  - "C.26"
  - "C.9"
  - "G.5"
keywords:
  - "ChoiceResult"
  - "ChoiceRule"
  - "DecisionSubject"
  - "OptionSet"
  - "ValueOfComputation"
  - "ValueOfInformation"
  - "choose now"
  - "comparison basis"
  - "decision theory"
  - "non-shared comparison frame"
  - "probe again"
  - "probe-worthiness"
  - "question order"
  - "reject current set"
  - "reroute"
---

### C.11:10 - Rationale

A live option set and a live choice among that set are not the same question as generating options, governing a candidate pool, or sequencing execution. Keeping that distinction explicit is what makes the doctrine usable rather than ceremonial.

`DecisionSubject` is the better default chooser term because decision theory often applies to persons, teams, organizations, and other system-bearing collectivities. `Agent` remains useful, but only when an explicit agency claim is actually being made.

A minimal mathematical floor is necessary because choice doctrine without one stable object stack quickly turns into verbal drift. But a pattern also fails if it keeps only the object names and never shows how those objects discipline an actual choice. That is why `Solution` here is procedural: it must carry the path from `OptionSet` through one `ChoiceRule` to one `ChoiceResult`, including the stop-or-probe decision, rather than only one survey of neighboring theories.

The practical gain of that procedure is not elegance for its own sake. It is that later search, policy, publication, and planning work receive one explicit result instead of one hand-waving claim that deliberation happened somewhere upstream.

At the same time, this pattern should not pretend that one full quantum-like or geometry-heavy package is already settled just because those neighboring lines are real.

