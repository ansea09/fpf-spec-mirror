---
chunk_kind: "child"
pattern_id: "A.2.5"
pattern_title: "RoleStateRelation - Windowed Role-State Recognition and Work Admission"
section_id: "A.2.5:11"
section_title: "Rationale"
source_path: "FPF-Spec.md"
output_path: "by_section/A.2.5/A.2.5__014_rationale.md"
commit_sha: "2729cfe5a3e4a86da8632aabcb859488c06a2d51"
heading_path:
  - "A.2.5 — RoleStateRelation - Windowed Role-State Recognition and Work Admission"
  - "A.2.5:11 — Rationale"
line_start: 4719
line_end: 4726
dependencies:
  - "A.15"
  - "A.2.1"
keywords:
  - "RSG"
  - "enactability"
  - "role state"
  - "role-state evolution"
  - "state machine"
---

### A.2.5:11 - Rationale

The pattern starts from the world-side relation because state claims can matter before a record exists. A robot can cease to satisfy its inspection predicate before a dashboard refreshes. A credential decision can constitute an institutional state before a certificate is published. A supported assertion is therefore necessary for reliance but is not the world-side state's truth-maker by default.

Using uninterrupted predicate truth as the identity boundary distinguishes repeated episodes even when assignment and predicate values stay the same. An assertion or occurrence description may state the known actual extent and refine an open end to a closed end without creating another occurrence.

The direct relation also explains why role state is not capability and not work. Capability says what operations a system can perform in an envelope. Role state says whether a current assignment satisfies one predicate over a window. Work says what change actually occurred. A method, gate, or work pattern may depend on all three, but no one of them proves the others.

