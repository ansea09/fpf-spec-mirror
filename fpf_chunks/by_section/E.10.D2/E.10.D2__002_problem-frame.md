---
chunk_kind: "child"
pattern_id: "E.10.D2"
pattern_title: "EntityOfConcern, Description Episteme, and Specification-Use Discipline"
section_id: "E.10.D2:1"
section_title: "Problem frame"
source_path: "FPF-Spec.md"
output_path: "by_section/E.10.D2/E.10.D2__002_problem-frame.md"
commit_sha: "cf12b97913ff82ca8a45ba77d3658ad11e0fdeb6"
heading_path:
  - "E.10.D2 — EntityOfConcern, Description Episteme, and Specification-Use Discipline"
  - "E.10.D2:1 — Problem frame"
line_start: 61292
line_end: 61320
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

### E.10.D2:1 - Problem frame

Use this pattern when FPF-governed wording names something under concern and also names a description, view, specification, publication, file, card, diagram, dashboard, work record, evidence item, assurance result, gate result, or decision around it.

The first useful move is to ask five questions:

1. What is the `EntityOfConcern`?
2. Which Description episteme describes it, if describing is live?
3. Which `DescriptionContext = <EntityOfConcernRef, BoundedContextRef, ViewpointRef>` bounds that description?
4. Is specification use admitted by explicit checkability, acceptance, validation, formality, or harness conditions, or is this only a Description episteme?
5. Which neighboring FPF pattern carries any publication, carrier, evidence, assurance, gate, decision, commitment, promise, work, view, bridge, retargeting, or state-family claim?

Not this pattern when the question under repair is already an evidence path named by value, assurance claim, gate decision, commitment, work occurrence, bridge, representation transition, source relation, or state-family field. Use the neighboring pattern governing that claim for that claim and use E.10.D2 only to keep the EntityOfConcern, Description episteme, and specification-use boundary readable.

FPF frequently has to say that some item is being described: a role, method, system, work occurrence, promise content, characteristic, architecture, episteme, view, or another FPF entity. The old short memory of "entity, description words, and rules" remains useful, but it becomes harmful when it is taught as three peer kinds.

The working distinction is sharper:

* the **EntityOfConcern** is the item under concern;
* the **Description episteme** is the claim-bearing episteme that describes that item under one bounded context and viewpoint;
* **specification use** is an admitted use or refinement of a Description episteme, not a separate peer class;
* publication faces, publication forms, carriers, renderings, work occurrences, gate decisions, evidence relations, and assurance claims remain outside this boundary unless a neighboring pattern makes one of them the EntityOfConcern.

This matters whenever wording such as `RoleDescription`, `ArchitectureDescription`, `MethodSpec`, `ServiceSpec`, "the diagram is the architecture", "the card authorizes work", or "the file is the method" could make readers confuse the item under concern with a description, a publication, a carrier, a work occurrence, or a granted use.

What goes wrong if E.10.D2 is missed: specification-looking words become authority, a publication becomes the thing described, a file becomes the method, an approval state over an episteme becomes a runtime state, or two descriptions with the same label are treated as the same EntityOfConcern across contexts.

What E.10.D2 buys in practice: the practitioner can name the item under concern, keep the Description episteme inspectable, admit specification use only when checkability exists, and apply the governing FPF pattern for every other claim being made.

