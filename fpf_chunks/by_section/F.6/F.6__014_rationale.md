---
chunk_kind: "child"
pattern_id: "F.6"
pattern_title: "RoleAssignment and Performed-Work Attribution Check"
section_id: "F.6:12"
section_title: "Rationale"
source_path: "FPF-Spec.md"
output_path: "by_section/F.6/F.6__014_rationale.md"
commit_sha: "f2fdd062c1518c9b1a1be1b6ad795627cffad2f1"
heading_path:
  - "F.6 — RoleAssignment and Performed-Work Attribution Check"
  - "F.6:12 — Rationale"
line_start: 88828
line_end: 88833
dependencies:
  - "A.1.1"
  - "A.10"
  - "A.15"
  - "A.15.1"
  - "A.15.4"
  - "A.2"
  - "A.2.1"
  - "A.2.2"
  - "A.2.5"
  - "A.3.1"
  - "A.3.2"
  - "A.6.REL"
  - "E.10"
  - "E.17"
  - "F.18"
  - "F.4"
  - "F.5"
  - "F.9"
  - "U.Role"
  - "U.RoleAssignment"
  - "U.Work"
keywords:
  - "actual performing U.System"
  - "assignment coverage"
  - "exact U.RoleAssignment"
  - "performedUnderAssignment"
  - "separate assertion and evidence"
  - "world-side attribution"
---

### F.6:12 - Rationale

The direct relation is needed because `U.RoleAssignment` and `U.Work` answer different questions. The assignment says who holds which role under which interpretation and during which episode. The work occurrence says what happened. `performedUnderAssignment` says that this work was performed under that assignment.

Making a log, status, decision, or evidence item a relation participant would confuse world-side attribution with knowledge of attribution. Creating `RoleEnactmentFact` would duplicate the same pair under a second identity. The two-participant relation preserves realism and keeps correction local: changing an evidence use does not rewrite work or assignment; discovering a different performer changes the attribution assertion and, when demonstrated, the selected relation occurrence.

