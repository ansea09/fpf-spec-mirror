---
chunk_kind: "child"
pattern_id: "A.16"
pattern_title: "Language-State Move Coordination"
section_id: "A.16:7"
section_title: "Conformance Checklist"
source_path: "FPF-Spec.md"
output_path: "by_section/A.16/A.16__008_conformance-checklist.md"
commit_sha: "1eb56cd0cfd6dccad65143e03d28509373bd8dd5"
heading_path:
  - "A.16 — Language-State Move Coordination"
  - "A.16:7 — Conformance Checklist"
line_start: 26983
line_end: 26994
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

### A.16:7 - Conformance Checklist
- `CC-A.16-1` `A.16` **MUST NOT** redefine `F` or publish a second formality-only climb.
- `CC-A.16-2` A conforming move note **MAY** stand alone; `A.16.0` **SHALL NOT** be treated as mandatory wrapper syntax for every move.
- `CC-A.16-3` Every move kind **SHALL** name its preconditions and postconditions over explicit language-state facets, route state, or authority state.
- `CC-A.16-4` Publication form, governing pattern, and MVPK face **SHALL NOT** be collapsed into one unnamed target.
- `CC-A.16-5` Multi-route state inside one governed member **SHALL NOT** be confused with lineage fork across several successor members.
- `CC-A.16-6` `respecify` **SHALL NOT** be used to hide slot-explicit epistemic precision repair that belongs to later repair governing patterns.
- `CC-A.16-7` Retreat or retirement **SHALL** preserve, withdraw, or discard prior witnesses and authority explicitly.
- `CC-A.16-8` Published path structures **SHOULD** reuse `E.18` when a graph publication is needed.
- `CC-A.16-9` `AuthorityState` and `EndpointAdmissionProfile` reuse **SHALL NOT** be treated as new governing patterns, new route-bearing forms, or substitutes for gate or work state.
- `CC-A.16-10` A summarized multi-move publication **SHALL** keep intermediate governing pattern transitions reconstructible; otherwise the case must reopen or publish richer history.

