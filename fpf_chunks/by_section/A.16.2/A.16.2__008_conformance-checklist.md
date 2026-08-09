---
chunk_kind: "child"
pattern_id: "A.16.2"
pattern_title: "Reopen / SketchBackoff / Respecify"
section_id: "A.16.2:7"
section_title: "Conformance Checklist"
source_path: "FPF-Spec.md"
output_path: "by_section/A.16.2/A.16.2__008_conformance-checklist.md"
commit_sha: "036c056e98c38522172c6b7b3ad08214281cc4e4"
heading_path:
  - "A.16.2 — Reopen / SketchBackoff / Respecify"
  - "A.16.2:7 — Conformance Checklist"
line_start: 27993
line_end: 27999
dependencies:
  - "A.16"
  - "A.16.0"
  - "A.16.1"
  - "A.6.A"
  - "A.6.P"
  - "B.4.1"
  - "B.5.2"
  - "C.16.Q"
  - "C.2.2a"
  - "C.2.5"
keywords:
  - "authority withdrawal"
  - "backoff"
  - "branch withdrawal"
  - "reopen"
  - "respecify"
  - "retire"
  - "retreat"
---

### A.16.2:7 - Conformance Checklist
- `CC-A.16.2-1` Retreat or retirement moves **SHALL** cite the trigger or counter-evidence that justifies them.
- `CC-A.16.2-2` A retreat or retirement move **SHALL NOT** silently preserve endpoint authority if the target form no longer supports it.
- `CC-A.16.2-3` Reopen / backoff / respecify / retire moves **SHOULD** preserve witnesses and trace links whenever still valid.
- `CC-A.16.2-4` The target articulation, closure, and route-authority state **SHALL** be explicit when the move substantively changes any of them.
- `CC-A.16.2-5` `respecify` **SHALL NOT** be used to smuggle slot-explicit epistemic precision repair out of governing patterns.

