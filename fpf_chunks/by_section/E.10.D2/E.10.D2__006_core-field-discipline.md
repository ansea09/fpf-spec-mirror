---
chunk_kind: "child"
pattern_id: "E.10.D2"
pattern_title: "EntityOfConcern, Description Episteme, and Specification-Use Discipline"
section_id: "E.10.D2:4.1"
section_title: "Core field discipline"
source_path: "FPF-Spec.md"
output_path: "by_section/E.10.D2/E.10.D2__006_core-field-discipline.md"
commit_sha: "d1f696e7c7767705206a8cacd9f6ed48e4dc5b02"
heading_path:
  - "E.10.D2 — EntityOfConcern, Description Episteme, and Specification-Use Discipline"
  - "E.10.D2:4.1 — Core field discipline"
line_start: 75265
line_end: 75298
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

### E.10.D2:4.1 - Core field discipline


#### E.10.D2:4.1.1 - EntityOfConcern

`EntityOfConcern` means the item under concern in the current claim. It is not a universal "object" bucket and not an authoring target. It may be a system-side entity, an episteme, a relation, a characteristic, a work occurrence, a pattern, or another FPF kind named by value.

When the EntityOfConcern is itself an episteme, the same distinction still holds. The episteme under concern is not automatically identical to a Description episteme about that episteme, and a publication of that episteme is still a publication relation.

#### E.10.D2:4.1.2 - Description episteme

A Description episteme is a `U.Episteme` whose `subjectRef` is interpreted through:

```
DescriptionContext = <EntityOfConcernRef, BoundedContextRef, ViewpointRef>
```

It may carry labels, glosses, characterizations, state-machine diagrams, structural views, criteria, diagrams, examples, or other claim-bearing content about the EntityOfConcern. Those parts remain episteme content. They do not become parts of the EntityOfConcern unless a separate FPF pattern establishes that relation.

#### E.10.D2:4.1.3 - Specification-use admission

Use a `...Spec` name only when the Description episteme is admitted for specification use under all applicable conditions:

1. **Checkability.** The claimed invariants or acceptance conditions are checkable.
2. **Declared formality or equivalent discipline.** The text states the formal mode, notation discipline, measurement criterion, comparator, or other named checkability condition that makes checking possible.
3. **Harness or validation relation.** The text names the acceptance harness, conformance or regression check, validation method, measurement procedure, source-currentness/provenance record, or neighboring FPF relation that will check the specification use.
4. **Same DescriptionContext.** The specification-use episteme preserves or explicitly updates `EntityOfConcernRef`, `BoundedContextRef`, and `ViewpointRef`.

If any condition is absent, use `...Description` and state the live criteria informatively or as candidates without claiming specification use.

#### E.10.D2:4.1.4 - Publication, carrier, and work boundary

`U.PresentationCarrier` or another explicitly named carrier relation bears, encodes, transports, or renders an episteme publication; it is publication-side in C.2.1+ rather than a semantic part of `U.Episteme`. A publication face, publication form, or publication unit makes an episteme available. A rendering, UI rendering, or front-end view displays it. A work occurrence uses it or acts under it. None of those relations changes the EntityOfConcern or upgrades a Description episteme to specification use by itself.

