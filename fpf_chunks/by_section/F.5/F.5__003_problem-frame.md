---
chunk_kind: "child"
pattern_id: "F.5"
pattern_title: "Naming Discipline for U-kind Names and RoleDescription Labels"
section_id: "F.5:1"
section_title: "Problem Frame"
source_path: "FPF-Spec.md"
output_path: "by_section/F.5/F.5__003_problem-frame.md"
commit_sha: "373c87917e92123cfa039e24c42a1f122b54fb66"
heading_path:
  - "F.5 — Naming Discipline for U-kind Names and RoleDescription Labels"
  - "F.5:1 — Problem Frame"
line_start: 89539
line_end: 89550
dependencies:
  - "A.15"
  - "A.2"
  - "A.2.1"
  - "A.2.2"
  - "A.2.5"
  - "A.2.7"
  - "A.6.5"
  - "E.10"
  - "E.10.ARCH"
  - "E.24.UK"
  - "F.10"
  - "F.13"
  - "F.14"
  - "F.15"
  - "F.17"
  - "F.18"
  - "F.4"
  - "F.7"
  - "F.8"
  - "F.9"
keywords:
  - "U-kind naming"
  - "lexical rules"
  - "morphology"
  - "naming conventions"
  - "role-description labels"
  - "twin registers"
---

### F.5:1 - Problem Frame

FPF needs names that humans can use without dragging the wrong ontology behind them. A good name is short enough to be used in documents and conversations, but it is not free-floating. It belongs to a recovered meaning.

This pattern keeps two recurrent naming families separate.

First, a U-kind or similar cross-context concept gets its name only after the value is admitted by `E.24.UK`, a Concept-Set row, or a direct governing pattern. The name should be neutral with respect to the witnesses and should name the least shared kind that the admission source actually admits.

Second, a role-description episteme labels one work-facing `U.Role` in one bounded context. The label should fit the local idiom and make the role recognizable. It should not make a holder assignment, capability, method, work occurrence, status, evidence relation, permission, publication, or relation slot look like part of the role value.

The tempting shortcut is to make "Role Description" cover both roles and statuses because both need labels. That is convenient wording, but it creates duplicate ontology. Statuses and evidence uses need names too; they do not become roles because they are named.

