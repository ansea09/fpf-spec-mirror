---
chunk_kind: "child"
pattern_id: "E.10.D2"
pattern_title: "EntityOfConcern, Description Episteme, and Specification-Use Discipline"
section_id: "E.10.D2:9"
section_title: "Worked examples"
source_path: "FPF-Spec.md"
output_path: "by_section/E.10.D2/E.10.D2__010_worked-examples.md"
commit_sha: "093d30e806a1466e24032733eb020bb5a5f585cc"
heading_path:
  - "E.10.D2 — EntityOfConcern, Description Episteme, and Specification-Use Discipline"
  - "E.10.D2:9 — Worked examples"
line_start: 60795
line_end: 60818
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

### E.10.D2:9 - Worked examples

#### E.10.D2:9.1 - Role

`U.Role :: ChangeAuthority` is the EntityOfConcern. `ChangeAuthorityRoleDescription@ITIL4` is a Description episteme with `DescriptionContext = <EntityOfConcernRef(ChangeAuthority), BoundedContextRef(ITIL4), ViewpointRef(RoleViewpoint)>`.

The Description episteme may characterize the role by credential level, mandate window, separation-of-duty criteria, and a role-state graph. The role does not contain the graph or the checklist. If testable invariants and an acceptance harness are declared, a `ChangeAuthorityRoleSpec@ITIL4` may be admitted for specification use.

#### E.10.D2:9.2 - Method

`U.Method :: BacklogRefinement` is the EntityOfConcern. A team note, practice card, or pseudo-code sketch is a `BacklogRefinementMethodDescription@EssenceContext` when it describes the method. It becomes `BacklogRefinementMethodSpec@EssenceContext` only when checkable method constraints and an acceptance or validation harness are present.

Calendar sessions, chat threads, and tickets are work occurrences or work records. They may use the method description, but they are not the method and not the Description episteme.

#### E.10.D2:9.3 - Architecture

`ArchitectureOf@Context(Holon)` is the EntityOfConcern. An architecture description, structural view, graph, ADR, or dashboard is a Description episteme, view, publication, or carrier about that architecture. The diagram does not become the architecture, and an ADR does not by itself create permission or assurance.

If a structural view uses a mathematical lens, C.29 carries the declared mathematical-lens use question. If an architecture description is used to guide work, A.15.4 and P2W-related patterns carry the work-relevance relation.

#### E.10.D2:9.4 - Episteme as EntityOfConcern

A safety case, DRR, pattern, or source bundle can itself be the EntityOfConcern. A review note describing that DRR is then a Description episteme about an episteme. A published PDF of the DRR is a carrier or publication relation. This prevents the common slide from "talking about a description" into "talking only about descriptions of descriptions".

