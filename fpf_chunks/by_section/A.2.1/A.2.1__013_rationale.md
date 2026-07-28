---
chunk_kind: "child"
pattern_id: "A.2.1"
pattern_title: "U.RoleAssignment - System Role Assignment"
section_id: "A.2.1:11"
section_title: "Rationale"
source_path: "FPF-Spec.md"
output_path: "by_section/A.2.1/A.2.1__013_rationale.md"
commit_sha: "4b75b56c13f5d61be5238fdbc7c20af5c6f89df7"
heading_path:
  - "A.2.1 — U.RoleAssignment - System Role Assignment"
  - "A.2.1:11 — Rationale"
line_start: 2802
line_end: 2809
dependencies:
  - "A.1.1"
  - "A.15"
  - "A.15.1"
  - "A.2"
  - "A.2.2"
  - "A.2.5"
  - "A.2.7"
  - "A.3.1"
  - "A.3.2"
  - "A.6.5"
  - "A.6.9"
  - "A.6.REL"
  - "C.2.1"
  - "F.6"
  - "F.9"
  - "U.Role"
keywords:
  - "AssignmentInterval"
  - "assignment occurrence"
  - "effective ReferenceScheme"
  - "holder System"
  - "performedUnderAssignment"
  - "role value"
  - "role-taxonomy episteme"
---

### A.2.1:11 - Rationale

`U.RoleAssignment` is admitted because a role value and holder identity answer different questions. `U.Role` is the admitted kind for role values; one exact role value carries the work-facing participation meaning. One obtaining assignment occurrence `RA : U.RoleAssignment` relates one admitted System to that role value through one role-taxonomy episteme and one effective reference scheme over its maximal continuous extent. A separately identified assignment assertion or description may designate those four participants and state the occurrence's temporal extent. `U.Work` is the admitted kind for work individuals; one `W : U.Work` is the world-side dated occurrence. A separate assertion or record may say that `W` occurred and state its obtaining relations.

The assignment is a relation occurrence, not a relation value stored in a row. Its participant meanings and temporal episode provide the domain identity required by `A.6.REL`. This prevents two opposite errors: treating every role label as a complete assignment, and requiring explicit assignment-occurrence individuation for casual recognition text.

The role-taxonomy episteme and effective reference scheme provide semantic locality directly. They remove the need for mandatory `U.BoundedContext`. A selected model-use structure remains available to a receiving assertion or work use without becoming an agent, role taxonomy, generic assignment participant, or identity component.

