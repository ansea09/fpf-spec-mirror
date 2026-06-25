---
chunk_kind: "child"
pattern_id: "E.10.D2"
pattern_title: "EntityOfConcern, Description Episteme, and Specification-Use Discipline"
section_id: "E.10.D2:4"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/E.10.D2/E.10.D2__005_solution.md"
commit_sha: "b0368ed8d883c04d0b261b03f46c28e23d790dc5"
heading_path:
  - "E.10.D2 — EntityOfConcern, Description Episteme, and Specification-Use Discipline"
  - "E.10.D2:4 — Solution"
line_start: 67813
line_end: 67841
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

### E.10.D2:4 - Solution


For any sentence that names an entity and also names description, specification, view, publication, carrier, evidence, evaluation, or work:

1. **Name the EntityOfConcern.** State what item is under concern: for example `U.Role`, `U.Method`, `U.System`, `U.Work`, `U.PromiseContent`, `U.Characteristic`, `U.ArchitectureOf@Context`, or `U.Episteme`.
2. **Name the Description episteme when describing is live.** A `...Description` is a `U.Episteme` that describes the EntityOfConcern under `DescriptionContext = <EntityOfConcernRef, BoundedContextRef, ViewpointRef>`.
3. **Admit specification use only by conditions.** A `...Spec` is a Description episteme admitted for specification use when checkability conditions are present. The conditions must name formal checkability or declared formality, checkable invariants or acceptance criteria, a validation or acceptance harness, and the same DescriptionContext.
4. **Keep publication and carrier relations separate.** A card, document, dashboard, diagram, file, rendering, API description, or interface declaration may publish, encode, render, or expose a Description episteme; it is not thereby the EntityOfConcern and it does not by itself create permission, evidence, gate, assurance, decision, commitment, or work.
5. **Apply the neighboring pattern when another claim becomes live.** Evidence is governed by `A.10` or `G.6`; assurance by `B.3`; status-family, standard-use, and requirement-use distinctions by `F.10`; publication and view mechanics by `E.17`, `E.17.0`, `E.17.2`, or their direct subpatterns; commitments and promises by `F.18` and related patterns; work, work plans, and work-facing role assignments by `A.15`, `A.15.1`, `A.2`, or `A.2.1`; retargeting by `A.6.4`.

When source wording says that a description, source, standard, requirement, evidence item, publication, dashboard, or view "has a role" or "plays a role", recover the typed relation first. It is normally evidence-use, status-use, source-use, publication-use, standard-use, requirement-use, assurance-use, gate-use, or work-relevance wording. Do not create a `U.Role`, `U.RoleAssignment`, or role-state value unless the current claim is about a system or acting holon holding a work-facing role in a bounded work context.

Ordinary minimum:
 write one line that names the EntityOfConcern, the Description episteme or `not live`, the DescriptionContext or missing-context blocker, the specification-use admission value, and the neighboring FPF pattern governing that claim for any live non-description claim.

```text
E10D2BoundaryLine:
  entityOfConcernRef:
  descriptionEpistemeRef or notLive:
  descriptionContext or missingContextBlocker:
  specificationUseAdmission: admitted | notAdmitted | candidateOnly
  neighboringPatternApplicationRefs for non-description claims:
  admissibleUse:
  nonAdmissibleUse:
```

Stop at the boundary line when it makes the next admissible use clear. Open heavier episteme, publication, source, bridge, evidence, assurance, gate, decision, work, or state-family records only when those claims are being made.

