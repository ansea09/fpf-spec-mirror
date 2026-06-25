---
chunk_kind: "child"
pattern_id: "E.10.D2"
pattern_title: "EntityOfConcern, Description Episteme, and Specification-Use Discipline"
section_id: "E.10.D2:16"
section_title: "Current repair actions"
source_path: "FPF-Spec.md"
output_path: "by_section/E.10.D2/E.10.D2__018_current-repair-actions.md"
commit_sha: "b0368ed8d883c04d0b261b03f46c28e23d790dc5"
heading_path:
  - "E.10.D2 — EntityOfConcern, Description Episteme, and Specification-Use Discipline"
  - "E.10.D2:16 — Current repair actions"
line_start: 68058
line_end: 68071
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

### E.10.D2:16 - Current repair actions

Use these repairs when live FPF prose violates this pattern:

1. Replace old `DescribedEntity*`, `EntityOfInterest`, `EoI`, and `EoIClass` wording with `EntityOfConcern`, `EntityOfConcernRef`, `EntityOfConcernClass`, or the local FPF kind named by value. Retain old spellings only as source-side trigger wording.
2. Replace peer-layer I-D-S wording with EntityOfConcern, Description episteme, and specification-use admission wording.
3. Replace "contains role characteristic space, role-state relation, or checklist" with "is characterized through the Description episteme by role characteristic space, role-state relation, or checklist".
4. Replace carrier identity with "carrier encodes" or "publication exposes" wording.
5. Replace generic "object under description" talk with the EntityOfConcern named by value and its `DescriptionContext`.
6. Replace `...Spec` names that lack specification-use admission with `...Description`.

7. For permission, evidence, assurance, gate, decision, promise, commitment, work, publication, view, bridge, or retargeting claims, apply the neighboring pattern governing that exact claim instead of keeping the claim as local semio guard prose.
8. Replace "role of this description, source, standard, evidence, or publication" wording with the exact typed relation: evidence-use, status-use, source-use, publication-use, standard-use, requirement-use, assurance-use, gate-use, or work-relevance relation. Use `U.RoleAssignment` only for work-facing roles held by systems or acting holons.

