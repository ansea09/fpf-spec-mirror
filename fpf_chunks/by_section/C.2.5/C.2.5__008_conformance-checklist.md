---
chunk_kind: "child"
pattern_id: "C.2.5"
pattern_title: "U.LanguageStateClosureDegree — How Fixed Is the Current Candidate Space?"
section_id: "C.2.5:7"
section_title: "Conformance Checklist"
source_path: "FPF-Spec.md"
output_path: "by_section/C.2.5/C.2.5__008_conformance-checklist.md"
commit_sha: "a4048aafca7f550ddc5dc880c9b488e9c8401434"
heading_path:
  - "C.2.5 — U.LanguageStateClosureDegree — How Fixed Is the Current Candidate Space?"
  - "C.2.5:7 — Conformance Checklist"
line_start: 49804
line_end: 49809
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
  - "CD0–CD5"
  - "candidate-space closure"
  - "closure degree"
  - "frame space"
  - "reopen"
  - "route space"
  - "settledness"
---

### C.2.5:7 - Conformance Checklist
- `CC-C.2.5-1` Closure **SHALL** be declared independently from `F` and `AE` when it matters for routing, docking, or reopening.
- `CC-C.2.5-2` Reopen/backoff moves **SHALL** cite the prior closure state they are relaxing.
- `CC-C.2.5-3` Strong-closure states **SHOULD** name the guard, `governingPatternRef`, or `authoritySourceRef` that makes the closure binding.
- `CC-C.2.5-4` A closure drop **SHALL NOT** silently preserve an endpoint-use claim when the supporting route or publication form no longer supports it.

