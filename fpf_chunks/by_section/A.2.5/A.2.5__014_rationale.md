---
chunk_kind: "child"
pattern_id: "A.2.5"
pattern_title: "SystemRoleAssignmentStateRelation - Assignment-State Recognition and Work Admission"
section_id: "A.2.5:11"
section_title: "Rationale"
source_path: "FPF-Spec.md"
output_path: "by_section/A.2.5/A.2.5__014_rationale.md"
commit_sha: "421266f0a37ab295b1ffd9e214ace6541e21f5be"
heading_path:
  - "A.2.5 — SystemRoleAssignmentStateRelation - Assignment-State Recognition and Work Admission"
  - "A.2.5:11 — Rationale"
line_start: 5202
line_end: 5209
dependencies:
  - "A.15"
  - "A.15.1"
  - "A.2"
  - "A.2.1"
  - "A.2.2"
  - "A.2.7"
  - "A.21"
  - "A.6.5"
  - "A.6.REL"
  - "C.3"
keywords:
  - "Work admission"
  - "assignment-state predicate"
  - "assignment-state relation"
  - "evidence boundary"
  - "state condition"
  - "time window"
---

### A.2.5:11 - Rationale

The pattern starts from the world-side relation because state truth can matter before a record exists. A robot can cease to satisfy its inspection predicate before a dashboard refreshes. A credential decision can constitute an institutional condition before a certificate is published. A supported assertion is needed for some reliance uses but is not the world's truth-maker by default.

Using uninterrupted predicate truth as the identity boundary distinguishes repeated episodes even when assignment and predicate stay the same. A description may refine an open interval's end without creating another occurrence; a genuine false gap does create a boundary.

Assignment state is neither capability nor Work. Capability says what operations a system can perform in an envelope. `SystemRoleAssignmentStateRelation` says whether one current assignment satisfies one predicate over an interval. Work says what was actually performed. A Method, gate, or Work pattern may depend on all three, but none proves the others.

