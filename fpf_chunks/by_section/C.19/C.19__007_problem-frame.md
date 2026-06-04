---
chunk_kind: "child"
pattern_id: "C.19"
pattern_title: "Explore–Exploit Governor (E/E‑LOG)"
section_id: "C.19:1"
section_title: "Problem frame"
source_path: "FPF-Spec.md"
output_path: "by_section/C.19/C.19__007_problem-frame.md"
commit_sha: "a0c90e3bbfcc0285893cc5bb9d4a88fcd224f00e"
heading_path:
  - "C.19 — Explore–Exploit Governor (E/E‑LOG)"
  - "C.19:1 — Problem frame"
line_start: 42588
line_end: 42599
dependencies:
  - "B.3"
  - "C.11"
  - "C.17"
  - "C.18"
  - "C.24"
  - "C.28"
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
The E/E governor provides named, versioned policies and lenses that steer NQD generation/selection under lawful dominance and provenance constraints.

When `C.11` has already made local choice among one fixed `OptionSet` explicit, `C.19` begins where the question becomes policy over several still-live candidate lines, family regions, or frontier segments rather than one more local `ChoiceResult` record.

Immediate failure indicators for this pattern:
- the current pool-policy result cannot name the still-live candidate pool it is governing
- the governing lens or policy state is missing
- the next pool-side treatment exists only as one vague promise to continue exploration later

If the question is still which single option should survive now, apply `C.11`. If the next artifact must already be one enactment-facing plan, apply `C.24`. If the retained set must be published for downstream consumption, apply `G.5`.

