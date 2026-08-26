---
chunk_kind: "child"
pattern_id: "E.17.2"
pattern_title: "TEVB - Project-local Typical Engineering Viewpoint Bundle Template for Holons"
section_id: "E.17.2:5"
section_title: "Worked cases"
source_path: "FPF-Spec.md"
output_path: "by_section/E.17.2/E.17.2__006_worked-cases.md"
commit_sha: "d064720b072b822cbb2f1d41e555cf08e2904f11"
heading_path:
  - "E.17.2 — TEVB - Project-local Typical Engineering Viewpoint Bundle Template for Holons"
  - "E.17.2:5 — Worked cases"
line_start: 80459
line_end: 80509
dependencies:
  - "A.22"
  - "A.6.3"
  - "A.6.6"
  - "C.13"
  - "C.2.1"
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

The cases below assume one hypothetical project has already constituted exact `L_local`, bound `f_eng`, and resolved `r_functional -> P_functional`, `r_procedural -> P_procedural`, `r_allocation -> P_allocation`, and `r_module -> P_module` under exact `R_L`. They demonstrate a materialized local instance; they do not assert that these values exist in the repository or in another project.

#### E.17.2:5.1 - Four views of a processing plant

Exact plant `Plant_X : U.System` is the EntityOfConcern of four separately identified epistemes.

- E1 states transformations, capabilities, material-flow effects, and functional boundaries. `r_functional` resolves `P_functional`; E1 conforms to that P and is a functional `U.View`.
- E2 states claims about exact admitted method `PlantOperation`, exact A.19.SPR operational-state structure `PlantRunState`, and exact E.18 transformation-flow structure `PlantRunFlow`; its order, failure, and recovery claims designate the exact transition conditions and flow relations in those structures. It conforms to `P_procedural`; it is not a method description because its EntityOfConcern is the plant. No safety-bearing claim or named reliance is present in this case, so no safety-analysis, A.10, or B.3 branch is opened.
- E3 states that `PumpUnit-3` counts as local kind `CoolingCirculatorSystemRole` in the plant slice through a separate C.3.2 judgment over the exact candidate, kind, `KindSignature` edition, and slice; that claim needs no assignment. E3 separately states any obtaining assignments, capabilities, transformations, and governed responsibility structures that are current. It conforms to `P_allocation`; neither E3 nor `P_allocation` makes the classification criterion true, creates an assignment or responsibility relation, or performs Work.
- E4 states constituent equipment holons, dependency structure, pipes, interfaces, substitutability, and change policy. It conforms to `P_module`; the diagram rendering E4 is published in remains separate.

The four conformance occurrences make E1-E4 views. Their shared holon and common local declaration do not establish any cross-view realization or consistency relation. Those claims are tested separately.

#### E.17.2:5.2 - Query output missing a required concern

A query constructs episteme Y from plant model X, and A.6.3 records that construction. Y is labelled `functional view`, but it omits the output-condition coverage required by exact `P_functional`. Construction obtains; conformance does not. Y is not a `U.View` under that P until another episteme edition with repaired claim content passes the predicate.

#### E.17.2:5.2.1 - Ordinary non-safety jam recovery

Candidate procedural episteme `E_jamRecovery` concerns exact conveyor system H. Its ClaimGraph designates exact admitted method `ClearJam`, an exact operational-state structure with `Running`, `Blocked`, and `Resetting` positions, the exact transition conditions between those positions, and the exact E.18 flow relation that resumes only after the blockage sensor is clear. These method, state, and flow facts supply the operational basis for its failure-and-recovery claims. If `EpistemeViewpointConformanceRelation(E_jamRecovery,P_procedural)` obtains, E is a procedural `U.View`.

No claim in this case is safety-bearing, no receiving decision relies on a safety analysis, and no evidence or assurance result is requested. Therefore neither an A.10 evidence path nor a B.3 assurance branch is opened. A later actual clearing remains separately identified `U.Work`; the procedural episteme does not perform it.

#### E.17.2:5.2.2 - Safety-triggered recovery use

Suppose a second claim says that restarting H after the same jam is safe for an exposed operator, and a named restart decision relies on that proposition. The project now identifies the exact safety-analysis episteme and its hazard, guard, and recovery claims; relates the relied-on evidence through A.10; and uses B.3 when the assurance claim or material-reliance threshold is current. The operational method, state transitions, and flow relations remain the same exact operational basis; safety analysis and reliance are added because this claim and decision trigger them, not because every failure or recovery description requires assurance.

#### E.17.2:5.3 - Responsibility diagram and actual assignment

A responsibility-diagram episteme E concerns exact System H. Exact local reference `r_allocation : U.ViewpointRef` resolves exact `P_allocation`; `EpistemeViewpointConformanceRelation(E,P_allocation)` obtains.

**Diagram cue.** One box names `MaintainerSystemRole@Plant`. That spelling can help locate the plant-side definition; by itself it establishes neither an exact local system-role kind, an assigned-kind domain, a C.3.2 judgment, nor an assignment.

**Classification-only claim.** If a current claim says `PumpUnit-3` counts as `CoolingCirculatorSystemRole` for exact `CoolingCirculatorKindSignature-2` and `PlantSlice-7`, recover `J(PumpUnit-3, CoolingCirculatorSystemRole, CoolingCirculatorKindSignature-2, PlantSlice-7) = true` under C.3.2. No assignment is required.

**Assignment claim.** If a separate claim says admitted System S holds an assignment, first recover the exact local kind—here named `MaintainerSystemRole`—through C.3 and declare the exact assigned-kind domain—here named `PlantMaintenanceSystemRoleKindDomain`. The diagram cue identifies neither. Then recover exact `RA : MaintenanceWorkAssignment <: U.SystemRoleAssignment` under A.2.1, with S in `HolderSystemSlot`, `PlantMaintenanceSystemRoleKindDomain` as the declaration-local assigned-kind domain, and `MaintainerSystemRole` as RA's assigned-kind value.

E can assert or describe RA without becoming RA. Any responsibility of S remains a separately governed direct claim.

#### E.17.2:5.4 - One view, two publications

Module-interface view E is published as an interactive model and as a printed inspection sheet. Both publication occurrences select the same episteme edition. Their forms and carriers differ; E, its conformance occurrence, and its `U.View` membership do not.

#### E.17.2:5.5 - DDD Context Mapping method and product

A team enacts DDD Context Mapping. The way of doing is one independently admitted `U.Method` under A.3.1; an episteme that substantively describes that method may separately be a `U.MethodDescription` with the method as its exact EntityOfConcern. Neither is a TEVB viewpoint or view by its label.

First determine whether the product is a claim-bearing episteme or only a diagram, form, or carrier. A claim-bearing product called a Context Map is separately identified under C.2.1 as candidate episteme E with its own exact claim content, EntityOfConcern, and effective scheme. It becomes a `U.View` only if one exact viewpoint P admits E's EntityOfConcern and `EpistemeViewpointConformanceRelation(E,P)` obtains. Method enactment, product naming, diagram form, declaration position, publication, and visual resemblance grant no membership. If the map represents independently recovered domain regions or relations, C.29 defines that correspondence; a mere carrier remains with E.24.PUB, and the drawing makes no represented world-side relation obtain.

