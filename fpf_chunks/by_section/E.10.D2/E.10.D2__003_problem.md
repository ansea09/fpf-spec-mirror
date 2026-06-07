---
chunk_kind: "child"
pattern_id: "E.10.D2"
pattern_title: "EntityOfConcern, Description Episteme, and Specification-Use Discipline"
section_id: "E.10.D2:2"
section_title: "Problem"
source_path: "FPF-Spec.md"
output_path: "by_section/E.10.D2/E.10.D2__003_problem.md"
commit_sha: "18497f0808242ab7c1a31cb5c94898e9f6b6879d"
heading_path:
  - "E.10.D2 — EntityOfConcern, Description Episteme, and Specification-Use Discipline"
  - "E.10.D2:2 — Problem"
line_start: 60147
line_end: 60154
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

### E.10.D2:2 - Problem

1. **Entity-description collapse.** A text treats the `EntityOfConcern` as if it were identical to the Description episteme, the diagram, the card, the file, or the work record.
2. **Specification inflation.** A text calls any detailed write-up a `...Spec` although no checkability, acceptance condition, or harness relation is present.
3. **Publication or carrier substitution.** A publication face, document, dashboard, schema file, or generated view is treated as the described entity or as the authority for work.
4. **Context and viewpoint loss.** A Description episteme is read as global even though FPF descriptions are bounded by `DescriptionContext = <EntityOfConcernRef, BoundedContextRef, ViewpointRef>`.
5. **Status and state leakage.** Epistemic or deontic statuses over epistemes are used as if they were role states, system states, or runtime facts about the EntityOfConcern.

