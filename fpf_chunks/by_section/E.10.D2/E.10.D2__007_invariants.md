---
chunk_kind: "child"
pattern_id: "E.10.D2"
pattern_title: "EntityOfConcern, Description Episteme, and Specification-Use Discipline"
section_id: "E.10.D2:6"
section_title: "Invariants"
source_path: "FPF-Spec.md"
output_path: "by_section/E.10.D2/E.10.D2__007_invariants.md"
commit_sha: "3d19010169827708d0bca36d0551af8323908640"
heading_path:
  - "E.10.D2 — EntityOfConcern, Description Episteme, and Specification-Use Discipline"
  - "E.10.D2:6 — Invariants"
line_start: 60265
line_end: 60282
dependencies:
  - "A.7"
  - "C.2.1"
  - "C.2.3"
  - "D.CTX"
  - "E.10.D1"
  - "F.10"
  - "F.12"
  - "F.15"
  - "F.4"
  - "F.5"
  - "F.8"
  - "F.9"
  - "F.9.1"
  - "U.BoundedContext"
  - "U.EpistemeSlotGraph"
keywords:
  - "Description episteme"
  - "DescriptionContext"
  - "EntityOfConcern"
  - "specification use"
  - "testable"
  - "verifiable"
---

### E.10.D2:6 - Invariants

**D2-1 (Entity-description distinction).** The EntityOfConcern and the Description episteme about it are distinct even when the EntityOfConcern is itself an episteme.

**D2-2 (Specification is admitted use).** Specification is not a peer class beside EntityOfConcern and Description episteme. A `...Spec` is a Description episteme admitted for specification use.

**D2-3 (DescriptionContext).** A Description episteme names or recovers `DescriptionContext = <EntityOfConcernRef, BoundedContextRef, ViewpointRef>`.

**D2-4 (Publication and carrier separation).** Publication faces, publication forms, publication units, carriers, renderings, files, dashboards, and UI surfaces do not become the EntityOfConcern and do not grant specification use by appearance.

**D2-5 (Work separation).** A plan, checklist, or specification-use Description episteme does not execute work. Work occurrences and work results remain under work and P2W patterns.

**D2-6 (Status-state separation).** Epistemic and deontic statuses over epistemes are not role states, system states, or runtime facts unless the exact state pattern grants that interpretation.

**D2-7 (No label-only cross-context sameness).** Identical labels in two bounded contexts or viewpoints do not establish sameness. Use F.9 bridges, A.6.3 views, or A.6.4 retargeting as appropriate.

**D2-8 (ReferencePlane reservation).** Do not call this distinction a plane. Use `ReferencePlane` only where CHR or another exact pattern defines that field.

