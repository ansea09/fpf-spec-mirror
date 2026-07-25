---
chunk_kind: "child"
pattern_id: "E.10.D2"
pattern_title: "EntityOfConcern, Description Episteme, and Specification-Use Discipline"
section_id: "E.10.D2:11"
section_title: "Worked examples"
source_path: "FPF-Spec.md"
output_path: "by_section/E.10.D2/E.10.D2__013_worked-examples.md"
commit_sha: "3bc659a6f866071f629bf41fc2dd41f2518e579a"
heading_path:
  - "E.10.D2 — EntityOfConcern, Description Episteme, and Specification-Use Discipline"
  - "E.10.D2:11 — Worked examples"
line_start: 74504
line_end: 74547
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

### E.10.D2:11 - Worked examples

#### E.10.D2:11.1 - Role

`U.Role :: ChangeAuthority` is the EntityOfConcern. `ChangeAuthorityRoleDescription@ITIL4` is a Description episteme with `DescriptionContext = <EntityOfConcernRef(ChangeAuthority), BoundedContextRef(ITIL4), ViewpointRef(RoleViewpoint)>`.

The Description episteme may characterize the role by credential level, mandate window, separation-of-duty criteria, and a role-state relation. The role does not contain the relation description or the checklist. If testable invariants and an acceptance harness are declared, a `ChangeAuthorityRoleSpec@ITIL4` may be admitted for specification use.

#### E.10.D2:11.2 - Method

`U.Method :: BacklogRefinement` is the EntityOfConcern. A team note, practice card, or pseudo-code sketch is a `BacklogRefinementMethodDescription@EssenceContext` when it describes the method. It becomes `BacklogRefinementMethodSpec@EssenceContext` only when checkable method constraints and an acceptance or validation harness are present.

Calendar sessions, chat threads, and tickets are work occurrences or work records. They may use the method description, but they are not the method and not the Description episteme.

#### E.10.D2:11.3 - Architecture

`ArchitectureOf@Context(Holon)` is the EntityOfConcern. An architecture description, structural view, graph, ADR, or dashboard is a Description episteme, view, publication, or carrier about that architecture. The diagram does not become the architecture, and an ADR does not by itself create permission or assurance.

If a structural view uses a mathematical lens, C.29 carries the declared mathematical-lens use question. If an architecture description is used to guide work, A.15.4 and P2W-related patterns carry the work-relevance relation.

#### E.10.D2:11.4 - Episteme as EntityOfConcern

A safety case, DRR, pattern, or source set can itself be the EntityOfConcern. A review note describing that DRR is then a Description episteme about an episteme. A published PDF of the DRR is a carrier or publication relation. This prevents the common slide from "talking about a description" into "talking only about descriptions of descriptions".

#### E.10.D2:11.5 - Boundary-line replay slice

A project note says: "The architecture dashboard approves the deployment role." Applying E.10.D2 does not replace that phrase with one better noun. It recovers the typed FPF values and relations:

```text
E10D2BoundaryLine:
  entityOfConcernRef: ArchitectureOf@Context(PaymentService)
  descriptionEpistemeRef or notLive: PaymentServiceArchitectureDashboardDescription@ReleaseCandidate
  descriptionContext: <ArchitectureOf@Context(PaymentService), ReleaseCandidateContext, OperationsViewpoint>
  specificationUseAdmission: notAdmitted
  neighboringPatternApplicationRefs for non-description claims:
    publication or view use: E.17, E.17.0, or E.17.2
    evidence, assurance, or gate claim: A.10, G.6, B.3, or A.21 only when that exact claim is made
    work-facing role assignment: A.2 or A.2.1 only when an acting holon and bounded work context are named
  admissibleUse: the dashboard publishes or renders an architecture Description episteme or view for operations discussion
  nonAdmissibleUse: the dashboard is not the architecture, not approval, not a gate result, and not a U.RoleAssignment
```

The practical delta is immediate: do not treat the dashboard as permission to deploy or as a role assignment. First name the exact evidence, assurance, gate, work, or publication relation being claimed; if none is present, keep only the description-publication use.

