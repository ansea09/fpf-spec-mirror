---
chunk_kind: "child"
pattern_id: "C.2.5"
pattern_title: "U.LanguageStateClosureDegree"
section_id: "C.2.5:7"
section_title: "Conformance Checklist"
source_path: "FPF-Spec.md"
output_path: "by_section/C.2.5/C.2.5__008_conformance-checklist.md"
commit_sha: "b7ec5a0b1dfa4bdae4cf055188219e89cef61a63"
heading_path:
  - "C.2.5 — U.LanguageStateClosureDegree"
  - "C.2.5:7 — Conformance Checklist"
line_start: 43784
line_end: 43789
dependencies:
  - "A.16"
  - "A.16.0"
  - "A.16.1"
  - "A.16.2"
  - "A.18"
  - "B.4.1"
  - "B.5.2.0"
  - "C.2.2a"
  - "C.2.4"
  - "C.2.LS"
keywords:
  - "candidate-space closure"
  - "closure degree"
  - "reopen"
  - "rival routes"
  - "settledness"
---

### C.2.5:7 - Conformance Checklist
- `CC-C.2.5-1` Closure **SHALL** be declared independently from `F` and `AE` when it matters for routing, docking, or reopening.
- `CC-C.2.5-2` Reopen/backoff moves **SHALL** cite the prior closure state they are relaxing.
- `CC-C.2.5-3` Strong-closure states **SHOULD** name the guard, `governingPatternRef`, or `authoritySourceRef` that makes the closure binding.
- `CC-C.2.5-4` Endpoint authority **SHALL NOT** survive a closure drop silently when the supporting route or publication form no longer holds.

