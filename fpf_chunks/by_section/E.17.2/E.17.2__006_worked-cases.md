---
chunk_kind: "child"
pattern_id: "E.17.2"
pattern_title: "TEVB - Typical Engineering Viewpoint Bundle for Holons"
section_id: "E.17.2:5"
section_title: "Worked cases"
source_path: "FPF-Spec.md"
output_path: "by_section/E.17.2/E.17.2__006_worked-cases.md"
commit_sha: "3dbce51436bfd718bf49cb0356eebce70c4fc015"
heading_path:
  - "E.17.2 — TEVB - Typical Engineering Viewpoint Bundle for Holons"
  - "E.17.2:5 — Worked cases"
line_start: 80064
line_end: 80094
dependencies:
  - "A.1"
  - "A.22"
  - "A.6.2-A.6.4"
  - "A.6.3"
  - "A.6.6"
  - "A.7"
  - "C.13"
  - "C.2.1"
  - "E.10.D2"
  - "E.17"
  - "E.17.0"
  - "E.17.1"
  - "E.18"
  - "E.24.PUB"
  - "U.View"
  - "U.Viewpoint"
  - "U.ViewpointRef"
keywords:
---

### E.17.2:5 - Worked cases

#### E.17.2:5.1 - Four views of a processing plant

Exact plant `Plant_X : U.System` is the EntityOfConcern of four separately identified epistemes.

- E1 states transformations, capabilities, material-flow effects, and functional boundaries. `ref(VP.Functional)` resolves P1; E1 conforms to P1 and is a functional `U.View`.
- E2 states exact operating methods, states, order, failure, and recovery claims related to the plant. It conforms to P2 designated `VP.Procedural`; it is not a method description because its EntityOfConcern is the plant.
- E3 states exact role assignments, operator systems, automation systems, capabilities, and responsibility structures. It conforms to P3 designated `VP.AllocationResponsibility`; neither E3 nor P3 performs work or assigns a role.
- E4 states constituent equipment holons, dependency structure, pipes, interfaces, substitutability, and change policy. It conforms to P4 designated `VP.ModuleInterface`; the diagram rendering E4 is published in remains separate.

The four conformance occurrences make E1-E4 views. Their shared holon and common bundle do not establish any cross-view realization or consistency relation. Those claims are tested separately.

#### E.17.2:5.2 - Query output missing a required concern

A query constructs episteme Y from plant model X, and A.6.3 records that construction. Y is labelled `functional view`, but it omits the output-condition coverage required by exact P1. Construction obtains; conformance does not. Y is not a `U.View` under P1 until another episteme edition with repaired claim content passes the predicate.

#### E.17.2:5.3 - Responsibility diagram and actual assignment

A responsibility diagram episteme E concerns exact system H. Exact `r_allocation = ref(VP.AllocationResponsibility) : U.ViewpointRef` resolves exact viewpoint episteme P designated by the `VP.AllocationResponsibility` token; `EpistemeViewpointConformanceRelation(E,P)` obtains. One box names `MaintainerRole@Plant`. This mention does not establish that system S holds the role. Exact `U.RoleAssignment` occurrence RA must be recovered under A.2.1; E can then assert or describe RA without becoming RA.

#### E.17.2:5.4 - One view, two publications

Module-interface view E is published as an interactive model and as a printed inspection sheet. Both publication occurrences select the same episteme edition. Their forms and carriers differ; E, its conformance occurrence, and its `U.View` membership do not.

#### E.17.2:5.5 - DDD Context Mapping method and product

A team enacts DDD Context Mapping. The way of doing is one independently admitted `U.Method` under A.3.1; an episteme that substantively describes that method may separately be a `U.MethodDescription` with the method as its exact EntityOfConcern. Neither is a TEVB viewpoint or view by its label.

First determine whether the product is a claim-bearing episteme or only a diagram, form, or carrier. A claim-bearing product called a Context Map is separately identified under C.2.1 as candidate episteme E with its own exact claim content, EntityOfConcern, and effective scheme. It becomes a `U.View` only if one exact viewpoint P admits E's subject and `EpistemeViewpointConformanceRelation(E,P)` obtains. Method enactment, product naming, diagram form, bundle position, publication, and visual resemblance grant no membership. If the map represents independently recovered domain regions or relations, C.29 governs that correspondence; a mere carrier remains with E.24.PUB, and the drawing creates no world-side relation.

