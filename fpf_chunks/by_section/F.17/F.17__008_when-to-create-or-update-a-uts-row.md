---
chunk_kind: "child"
pattern_id: "F.17"
pattern_title: "Unified Term Sheet"
section_id: "F.17:6"
section_title: "When to create or update a UTS row"
source_path: "FPF-Spec.md"
output_path: "by_section/F.17/F.17__008_when-to-create-or-update-a-uts-row.md"
commit_sha: "f2fdd062c1518c9b1a1be1b6ad795627cffad2f1"
heading_path:
  - "F.17 — Unified Term Sheet"
  - "F.17:6 — When to create or update a UTS row"
line_start: 92725
line_end: 92737
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

### F.17:6 - When to create or update a UTS row

Create or update a UTS row when at least one condition is present:

- the name will be public, Core-facing, or reused across bounded contexts;
- a row id is needed for later examples, checks, dashboards, training material, or tool interface labels;
- a role name, status-family name, slot name, relation name, or local concept name is being reused outside the immediate local repair;
- a bridge claim is being used for cross-context term reuse;
- a name-card decision from `F.18` needs a compact reader-facing term row;
- a direct pattern changes the governed object in a way that changes the name, local sense, bridge, or admissible use.

Do not create a row only because a word was noticed. First recover the kind, relation, slot position, and admissible use under the direct governing pattern.

