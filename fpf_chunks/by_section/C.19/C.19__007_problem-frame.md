---
chunk_kind: "child"
pattern_id: "C.19"
pattern_title: "Explore-Exploit Live-Pool Governor"
section_id: "C.19:1"
section_title: "Problem frame"
source_path: "FPF-Spec.md"
output_path: "by_section/C.19/C.19__007_problem-frame.md"
commit_sha: "02a8b4bac1f141b1751421bf522e9dc489ae522e"
heading_path:
  - "C.19 — Explore-Exploit Live-Pool Governor"
  - "C.19:1 — Problem frame"
line_start: 45439
line_end: 45450
dependencies:
  - "A.19.CPM"
  - "A.19.SelectorMechanism"
  - "B.3"
  - "C.11"
  - "C.16"
  - "C.17"
  - "C.18"
  - "C.24"
  - "C.28"
  - "C.32"
  - "C.32.P2S"
  - "C.35"
  - "G.11"
  - "G.5"
  - "G.9"
keywords:
  - "DecisionSubject clarification"
  - "EmitterPolicy"
  - "InsertionPolicy"
  - "dominance default routing"
  - "explore-exploit"
  - "keep frontier"
  - "lens id"
  - "live candidate pool"
  - "narrow to subset"
  - "pool-policy result"
  - "reroute"
  - "sunset line"
  - "widen"
---

### C.19:1 - Problem frame
C.19 provides named, versioned policies and lenses that govern still-live pool treatment after C.18 generation, archive, or front records exist.

When `C.11` has already made local choice among one fixed `OptionSet` explicit, `C.19` begins where the question becomes policy over several still-live candidate lines, family regions, or frontier segments rather than one more local `ChoiceResult` record.

Immediate failure indicators for this pattern:
- the current pool-policy result cannot name the still-live candidate pool it is governing
- the governing lens or policy state is missing
- the next pool-side treatment exists only as one vague promise to continue exploration later

If the question is still which single option should survive now, apply `C.11`. If the next artifact must already be one enactment-facing plan, apply `C.24`. If the retained set must be published for downstream consumption, apply `G.5`.

