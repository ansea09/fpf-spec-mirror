---
chunk_kind: "child"
pattern_id: "E.10.D2"
pattern_title: "EntityOfConcern, Description Episteme, and Specification-Use Discipline"
section_id: "E.10.D2:8"
section_title: "Neighboring use routing"
source_path: "FPF-Spec.md"
output_path: "by_section/E.10.D2/E.10.D2__010_neighboring-use-routing.md"
commit_sha: "563f4c8e06a319cbd375b66cdbb2df27a5f8b9ef"
heading_path:
  - "E.10.D2 — EntityOfConcern, Description Episteme, and Specification-Use Discipline"
  - "E.10.D2:8 — Neighboring use routing"
line_start: 75124
line_end: 75190
dependencies:
  - "A.1.1"
  - "A.10"
  - "A.2.6"
  - "A.3.2"
  - "A.7"
  - "B.3"
  - "C.2.1"
  - "C.2.3"
  - "C.29"
  - "E.10"
  - "E.10.D1"
  - "E.17"
  - "E.17.0"
  - "E.24.PUB"
  - "F.15"
  - "F.4"
  - "F.5"
  - "F.8"
  - "F.9"
  - "G.11"
keywords:
  - "Description episteme"
  - "DescriptionContext"
  - "EntityOfConcern"
  - "specification use"
  - "testable"
  - "verifiable"
---

### E.10.D2:8 - Neighboring use routing

Open a neighboring object only after naming the receiving use and recovering the description episteme. The same episteme can participate in several of the uses below; each use retains its own subject pattern, participants, obtaining condition, and identity.

#### E.10.D2:8.1 - Describing use, viewpoint, and view

For one named describing use, state that the use selects one exact `U.Viewpoint` episteme P when that selection changes what is read or checked. It says from which concern-bearing viewpoint the already identified episteme is being read for that use.

That selection:

* does not acquire C.2.1 episteme identity;
* does not establish `EpistemeViewpointConformanceRelation`;
* does not admit or remove same-individual `U.View` membership;
* selects no receiving view and performs no A.6.3 viewing construction;
* may change between two describing uses while the episteme remains unchanged.

Call the same episteme a `U.View` only when it conforms to at least one exact `U.Viewpoint` episteme under E.17.0's fixed membership rule. Direct authoring and A.6.3 source-to-receiving construction can produce an episteme but grant no view membership. A rendering, publication form, or carrier-borne display is not a view by appearance. If one use must select several viewpoints, first identify their exact C.13 collection and any organization the use actually needs; do not overload one context qualification.

#### E.10.D2:8.2 - Scope, model use, grounding, evidence, and currentness

Use A.2.6 when the receiving use depends on the exact claim scope and its context-slice membership. Use A.1.1 when the receiving use depends on one exact `BoundedModelUseStructure`. Neither scope nor structure becomes a description constituent merely because a table displays it.

Use C.2.1 empirical grounding only when claims must be mapped to exact observation, intervention, measurement, or test relations involving one grounding holon. Use A.10 when the use relies on an exact evidence-provenance path; use B.3 when an assurance claim is made or its material-reliance threshold is met. Evidence, assurance, or an evaluation result can support an assertion about a description or its specification use; none makes the subject-side claim true, changes the EntityOfConcern, or mutates the description episteme. State the exact validity or reliance window when that receiving use depends on one.

Use G.11 when currentness of the description edition, evidence path, harness, viewpoint, publication, or another neighbor matters to the receiving use. A currentness judgment applies to that exact object or relation; it is not a generic status field of the EntityOfConcern.

Where claims cross reference schemes, first recover the exact F.17 source and receiving senses and the obtaining F.9 Bridge needed by the direct use. A separate current C.2.1 claim states whether that Bridge is suitable for the named bounded use, direction, correspondence rule, and loss tolerance; A.10 or B.3 separately governs reliance. A Bridge, profile, card, or shared spelling is neither a licence nor proof that comparison, translation, or work occurred.

#### E.10.D2:8.3 - Edition, publication, form, and carrier

Changed ClaimGraph, EntityOfConcern, or effective ReferenceScheme identifies another episteme under C.2.1. When the receiving use also claims continuity between two epistemes, use the exact C.2.1 edition relation. A version label, file history, publication order, shared name, or collection membership establishes neither another episteme nor edition continuity.

Use E.24.PUB to distinguish these actual publication-side objects and relations:

| Current object or relation | What it does | What it does not establish |
|---|---|---|
| selected episteme edition | carries the claim content made available | publication occurrence, form, carrier, audience access, or reliance |
| audience-declaration episteme | states the audience criterion | that a concrete receiver obtained, read, understood, or relied on the edition |
| bounded-use-declaration episteme | states supported operations or decisions, conditions, and excluded stronger uses | permission, acceptance, assurance, or actual work by itself |
| publication form | expresses the selected edition for the declared publication use | episteme identity or a durable public form kind by position |
| `U.PresentationCarrier` | physically or digitally bears the publication form | the episteme, the form, or the EntityOfConcern |
| publication occurrence | makes the selected edition available to the declared audience for the declared bounded use | expression, bearing, access work, reading, or reliance |

The subject pattern keeps the verbs exact: `PublicationFormExpressionRelation` relates edition, form, and bounded-use declaration; `PublicationFormBearingRelation` relates form and carrier; `EpistemePublicationRelation` governs bounded availability of the selected edition through that form and carrier. Rendering, printing, uploading, indexing, or access-control work remains dated `U.Work` performed by systems. Plain “published episteme” names contingent participation in a publication occurrence, not a durable `U.EpistemePublication` kind.

One encountered thing can enter several relations without their objects collapsing. A completed inspection card may be a claim-bearing episteme; its reusable layout may be a publication form; a sheet or file may be a carrier; and a publication occurrence may make the selected card-episteme edition available to a maintenance team for one bounded use. Each claim is recovered independently.

#### E.10.D2:8.4 - Representation

Use C.29 when notation elements, diagram elements, tuple positions, graph nodes, table cells, schemas, or tool structures stand in an explicit representation correspondence to independently recovered objects for a declared modeling or reasoning use. A representation can change what users can inspect or calculate without becoming the represented entity, episteme, direct relation occurrence, or proof that the represented predicate obtains.

A diagram therefore has distinct branches:

* if its exact ClaimGraph, EntityOfConcern, and effective ReferenceScheme satisfy C.2.1, the selected claim-bearing whole is an episteme;
* if that same episteme conforms to an exact viewpoint, E.17.0 may admit it as a `U.View`;
* its graphical arrangement may separately be a publication form or a C.29 representation according to the receiving use;
* a screen, sheet, or file may bear the form as a carrier;
* a publication occurrence may make one selected episteme edition available.

No branch follows from visual appearance, generation history, a heading, or a repository path.

#### E.10.D2:8.5 - Work, status, and authority

Only admitted systems perform authoring, evaluation, revision, publication, viewing, query, rendering, and use work under the corresponding work relations. The resulting episteme, publication, carrier, trace, or evaluation result does not perform that work.

Epistemic and deontic statuses over epistemes are not `SystemRoleAssignmentStateRelation` occurrences, system states, or runtime facts about the EntityOfConcern. A gate verdict, permission, commitment, acceptance, requirement use, standard use, source use, or Work authorization needs the pattern that defines, constrains, or tests that claim. Neither a description nor its publication grants those effects by label, approval mark, or availability.

