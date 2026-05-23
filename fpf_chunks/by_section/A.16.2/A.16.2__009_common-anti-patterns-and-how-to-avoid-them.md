---
chunk_kind: "child"
pattern_id: "A.16.2"
pattern_title: "Reopen / SketchBackoff / Respecify"
section_id: "A.16.2:8"
section_title: "Common Anti-Patterns and How to Avoid Them"
source_path: "FPF-Spec.md"
output_path: "by_section/A.16.2/A.16.2__009_common-anti-patterns-and-how-to-avoid-them.md"
commit_sha: "04dd733fb18b66d3a640d11758e0af22ea253fd8"
heading_path:
  - "A.16.2 — Reopen / SketchBackoff / Respecify"
  - "A.16.2:8 — Common Anti-Patterns and How to Avoid Them"
line_start: 22071
line_end: 22077
dependencies:
  - "A.16"
  - "A.16.0"
  - "A.16.1"
  - "A.6.A"
  - "A.6.P"
  - "A.6.Q"
  - "B.4.1"
  - "B.5.2"
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

### A.16.2:8 - Common Anti-Patterns and How to Avoid Them
- **Shame-driven concealment.** Teams hide the retreat. Publish the move.
- **Silent downgrade.** The publication loses closure state, route authority state, or endpoint authority claim but no one updates the route or authority state.
- **Retreat as erasure.** Earlier witnesses disappear even though they remain valid.
- **Respecify as silent repair.** `respecify` is used to hide a real semantic rewrite that belongs to later repair governing patterns.
- **Silent branch disappearance.** A branch stops mattering, but no retirement or supersession note is published.

