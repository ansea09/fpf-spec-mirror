---
chunk_kind: "child"
pattern_id: "F.6"
pattern_title: "RoleAssignment and Performed-Work Attribution Check"
section_id: "F.6:12"
section_title: "Rationale"
source_path: "FPF-Spec.md"
output_path: "by_section/F.6/F.6__014_rationale.md"
commit_sha: "60caecb4751fb2a3623a1faaca757d29a19acff9"
heading_path:
  - "F.6 — RoleAssignment and Performed-Work Attribution Check"
  - "F.6:12 — Rationale"
line_start: 88870
line_end: 88875
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

The direct relation is needed because `U.RoleAssignment` and `U.Work` admit different kinds of world-side occurrence. One obtaining assignment occurrence `RA` relates its holder System to a role value under one interpretation and throughout one episode; one Work individual `W : U.Work` is the dated Work occurrence. `performedUnderAssignment(W, RA)` either obtains or does not obtain as the additional world-side attribution between them. A distinct assertion or record may designate `RA` and `W`, state that `RA` obtains, state that `W` occurred, or state that the attribution relation obtains.

Making a log, status, decision, or evidence item a relation participant would confuse world-side attribution with knowledge of attribution. Creating `RoleEnactmentFact` would duplicate the same pair under a second identity. The two-participant relation preserves realism and keeps correction local: changing an evidence use does not rewrite work or assignment; discovering a different performer changes the attribution assertion and, when demonstrated, the selected relation occurrence.

