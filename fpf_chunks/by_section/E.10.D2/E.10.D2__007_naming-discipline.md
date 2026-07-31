---
chunk_kind: "child"
pattern_id: "E.10.D2"
pattern_title: "EntityOfConcern, Description Episteme, and Specification-Use Discipline"
section_id: "E.10.D2:5"
section_title: "Naming discipline"
source_path: "FPF-Spec.md"
output_path: "by_section/E.10.D2/E.10.D2__007_naming-discipline.md"
commit_sha: "d1f696e7c7767705206a8cacd9f6ed48e4dc5b02"
heading_path:
  - "E.10.D2 — EntityOfConcern, Description Episteme, and Specification-Use Discipline"
  - "E.10.D2:5 — Naming discipline"
line_start: 75299
line_end: 75308
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
  - "U.EpistemeSlotRelation"
keywords:
  - "Description episteme"
  - "DescriptionContext"
  - "EntityOfConcern"
  - "specification use"
  - "testable"
  - "verifiable"
---

### E.10.D2:5 - Naming discipline

**Default suffix.** Use `...Description` for a Description episteme unless specification-use admission is explicit.

**Reserved suffix.** Use `...Spec` only for a Description episteme admitted for specification use. Do not use `Spec` as a synonym for "detailed", "important", "official-looking", "formal-looking", or "stored in a schema".

**Entity names.** Use the bare FPF kind named by value for the EntityOfConcern: `Role`, `Method`, `System`, `Architecture`, `Characteristic`, `PromiseContent`, `Work`, `Episteme`, or another kind named by value. Do not append `Description`, `Spec`, `Card`, `View`, or `Carrier` unless the episteme, view, publication, or carrier is the actual EntityOfConcern.

**DescriptionContext names.** Use `EntityOfConcernRef`, `BoundedContextRef`, and `ViewpointRef` for Description episteme addressing. Do not revive `DescribedEntityRef`, `EntityOfInterest`, or peer-layer I-D-S wording.

