---
chunk_kind: "child"
pattern_id: "F.17"
pattern_title: "Unified Term Sheet"
section_id: "F.17:2"
section_title: "Problem frame"
source_path: "FPF-Spec.md"
output_path: "by_section/F.17/F.17__003_problem-frame.md"
commit_sha: "3bc659a6f866071f629bf41fc2dd41f2518e579a"
heading_path:
  - "F.17 — Unified Term Sheet"
  - "F.17:2 — Problem frame"
line_start: 92349
line_end: 92362
dependencies:
  - "A.10"
  - "A.15.1"
  - "A.19.SPR"
  - "A.2"
  - "A.2.1"
  - "A.2.7"
  - "A.22.CGUS"
  - "A.6.5"
  - "A.6.P"
  - "B.3"
  - "C.2.P"
  - "E.10"
  - "E.10.D2"
  - "E.10.MOVE"
  - "E.11"
  - "E.17"
  - "F.1"
  - "F.1-F.12"
  - "F.10"
  - "F.14"
  - "F.15"
  - "F.17"
  - "F.18"
  - "F.2"
  - "F.3"
  - "F.4"
  - "F.5"
  - "F.6"
  - "F.7"
  - "F.8"
  - "F.9"
  - "G.11"
keywords:
---

### F.17:2 - Problem frame

Unification work often succeeds locally and then fails in reuse. A term looks stable in one section, but another reader cannot see which bounded context, local sense, bridge, name-card decision, or direct governing pattern was used. Teams then invent new labels, import a local tradition as if it were universal, or treat a teaching block as if it were an ontology.

The damage is practical:

- local meanings become global slogans;
- one row silently mixes a role, a role description, a status value, a capability claim, and a work assignment;
- public names drift because no row id, edition, or name-card reference stays stable;
- cross-context sameness is asserted by spelling rather than by an `F.9` bridge;
- examples in other patterns cite a term but not the term decision that makes the example portable.

`F.17` fixes this by making the term row itself reviewable. Each row says what kind of thing is being named, where the local senses came from, what bridge is claimed, which name was selected, and which direct pattern owns the underlying object.

