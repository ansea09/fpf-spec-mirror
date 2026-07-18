---
chunk_kind: "child"
pattern_id: "E.10.D2"
pattern_title: "EntityOfConcern, Description Episteme, and Specification-Use Discipline"
section_id: "E.10.D2:7"
section_title: "Reasoning primitives"
source_path: "FPF-Spec.md"
output_path: "by_section/E.10.D2/E.10.D2__009_reasoning-primitives.md"
commit_sha: "1d5c1edd154b636a446b3887a6094be60c60faff"
heading_path:
  - "E.10.D2 — EntityOfConcern, Description Episteme, and Specification-Use Discipline"
  - "E.10.D2:7 — Reasoning primitives"
line_start: 71954
line_end: 71995
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

### E.10.D2:7 - Reasoning primitives

**Description link.**

```
EntityOfConcernRef(T), BoundedContextRef(C), ViewpointRef(Vp)
  |- isDescriptionOf(TDesc, T, C, Vp)
```

`TDesc` is the Description episteme about EntityOfConcern `T` in bounded context `C` under viewpoint `Vp`.

**Specification-use admission.**

```
isDescriptionOf(TDesc, T, C, Vp)
  and checkableInvariants(TSpec)
  and validationOrAcceptanceHarness(TSpec)
  and sameDescriptionContext(TSpec, TDesc)
  |- admittedForSpecificationUse(TSpec, T, C, Vp)
```

Only under those conditions may the episteme be named `TSpec`.

**Characterization relation.**

```
isDescriptionOf(RoleDesc, U.Role, C, Vp)
  and characterizes(RoleDesc, RoleCharacteristicSpace)
  and characterizes(RoleDesc, RoleStateRelation@BoundedContext)
  |- RoleDesc characterizes U.Role by those structures @C,Vp
```

The role is characterized through the Description episteme. The structures are not silently parts of the role.

**Evaluation relation.**

```
evidence E satisfies criteria K within window W
  |- attestation(subject has state, status, or result S @C within W)
```
Evaluation produces an attestation in a window. It does not mutate the EntityOfConcern.

