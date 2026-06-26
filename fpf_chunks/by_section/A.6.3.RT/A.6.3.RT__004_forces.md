---
chunk_kind: "child"
pattern_id: "A.6.3.RT"
pattern_title: "Representation-Scheme Transition: EntityOfConcern-Preserving Representation-Scheme Transition"
section_id: "A.6.3.RT:3"
section_title: "Forces"
source_path: "FPF-Spec.md"
output_path: "by_section/A.6.3.RT/A.6.3.RT__004_forces.md"
commit_sha: "02a8b4bac1f141b1751421bf522e9dc489ae522e"
heading_path:
  - "A.6.3.RT — Representation-Scheme Transition: EntityOfConcern-Preserving Representation-Scheme Transition"
  - "A.6.3.RT:3 — Forces"
line_start: 12389
line_end: 12396
dependencies:
  - "A.10"
  - "A.15"
  - "A.20"
  - "A.21"
  - "A.3.3"
  - "A.6.2"
  - "A.6.3"
  - "A.6.3.CR"
  - "A.6.3.CSC"
  - "A.6.4"
  - "A.7"
  - "B.3"
  - "B.5.2"
  - "C.2.7"
  - "C.26"
  - "C.27"
  - "E.10.D2"
  - "E.17"
  - "E.17.0"
  - "E.17.EFP"
  - "E.17.ID.CR"
  - "E.18"
  - "F.18"
  - "F.9"
  - "F.9.1"
keywords:
---

### A.6.3.RT:3 - Forces

- **Same entity, different reasoning medium.** Teams need different representational forms without silently changing the EntityOfConcern.
- **Legibility vs recoverability.** A clearer representation is useful only if users can still recover how it relates to source claims, source-relation records, and pins.
- **Representation change vs EntityOfConcern shift.** A new notation or geometry can make structure more visible, but it must not silently become a new EntityOfConcern or a new ontology.
- **Recoverability before decode ambition.** Start from cases where recoverability can be reviewed directly before leaning on decode-mediated reconstruction.
- **Governing-pattern restraint.** This pattern must stay under `A.6.3`, not swallow explanation governance, retargeting, bridge work, or carrier work.

