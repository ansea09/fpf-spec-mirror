---
chunk_kind: "child"
pattern_id: "F.6"
pattern_title: "SystemRoleAssignment and Performed-Work Attribution Check"
section_id: "F.6:12"
section_title: "Rationale"
source_path: "FPF-Spec.md"
output_path: "by_section/F.6/F.6__014_rationale.md"
commit_sha: "5801dc610c657ac7b1efee349b18e80ce6d7df6f"
heading_path:
  - "F.6 — SystemRoleAssignment and Performed-Work Attribution Check"
  - "F.6:12 — Rationale"
line_start: 91348
line_end: 91355
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
  - "A.3"
  - "A.6.9"
  - "A.6.REL"
  - "C.3.3"
  - "E.10.ROLE"
  - "E.17"
  - "F.18"
  - "F.4"
  - "F.5"
  - "F.9"
keywords:
  - "Work attribution"
  - "exact assignment occurrence"
  - "holder equality"
  - "performedUnderAssignment"
  - "performer System"
  - "separate evidence"
  - "temporal coverage"
---

### F.6:12 - Rationale

The direct relation is needed because assignment and Work have different occurrence identities. `performedUnderAssignment` is an additional world-side fact, not a field stored inside either participant. A separate assertion can say that the assignment obtains, the Work occurred, or their attribution relation obtains.

Using the family ValueKind in F.6 does not license a family-wide assignment signature. It lets F.6 project the actual holder from each occurrence through its species-declared holder slot while preserving any commission, position, locus, or other real participant. Creating a generic assignment for F.6 would duplicate the episode and weaken attribution identity.

Making a log, status, decision, or evidence item a participant would confuse attribution with knowledge of attribution. Creating `RoleEnactmentFact` would duplicate Work and the same relation. Treating a matching holder and temporal coverage as enough would instead attribute one Work to every overlapping assignment held by its performer. The two-participant relation avoids both errors: the case fact linking Work to assignment is checked separately, while assertions and evidence can change without rewriting the Work, assignment, or their link.

