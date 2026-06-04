---
chunk_kind: "child"
pattern_id: "E.10.D2"
pattern_title: "EntityOfConcern, Description Episteme, and Specification-Use Discipline"
section_id: "E.10.D2:3"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/E.10.D2/E.10.D2__004_solution.md"
commit_sha: "3d19010169827708d0bca36d0551af8323908640"
heading_path:
  - "E.10.D2 — EntityOfConcern, Description Episteme, and Specification-Use Discipline"
  - "E.10.D2:3 — Solution"
line_start: 60198
line_end: 60221
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

### E.10.D2:3 - Solution

For any sentence that names an entity and also names description, specification, view, publication, carrier, evidence, evaluation, or work:

1. **Name the EntityOfConcern.** State what item is under concern: for example `U.Role`, `U.Method`, `U.System`, `U.Work`, `U.PromiseContent`, `U.Characteristic`, `U.ArchitectureOf@Context`, or `U.Episteme`.
2. **Name the Description episteme when describing is live.** A `...Description` is a `U.Episteme` that describes the EntityOfConcern under `DescriptionContext = <EntityOfConcernRef, BoundedContextRef, ViewpointRef>`.
3. **Admit specification use only by conditions.** A `...Spec` is a Description episteme admitted for specification use when checkability conditions are present. The conditions must name formal checkability or declared formality, checkable invariants or acceptance criteria, a validation or acceptance harness, and the same DescriptionContext.
4. **Keep publication and carrier relations separate.** A card, document, dashboard, diagram, file, rendering, or API surface may publish, encode, render, or expose a Description episteme; it is not thereby the EntityOfConcern and it does not by itself create permission, evidence, gate, assurance, decision, commitment, or work.
5. **Exit to the neighboring pattern when another claim becomes live.** Evidence goes to evidence patterns; assurance to assurance patterns; gate decisions to gate patterns; commitments and promises to F.18 and related patterns; work to work and P2W patterns; publication and view mechanics to E.17/A.6.3/C.2.P; retargeting to A.6.4.

Ordinary minimum: write one line that names the EntityOfConcern, the Description episteme or `not live`, the DescriptionContext or missing-context blocker, the specification-use admission value, and the exact neighboring FPF pattern for any live non-description claim.

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

Stop at the boundary line when it makes the next admissible move clear. Open heavier episteme, publication, source, bridge, evidence, assurance, gate, decision, work, or state-family records only when those claims are live.
