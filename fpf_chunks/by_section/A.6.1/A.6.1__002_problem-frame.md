---
chunk_kind: "child"
pattern_id: "A.6.1"
pattern_title: "U.Mechanism - Reusable Law-Governed Operation Declaration"
section_id: "A.6.1:1"
section_title: "Problem frame"
source_path: "FPF-Spec.md"
output_path: "by_section/A.6.1/A.6.1__002_problem-frame.md"
commit_sha: "0990ff1d1ccee4587b8f7e16e7a725a8edbe66b4"
heading_path:
  - "A.6.1 — U.Mechanism - Reusable Law-Governed Operation Declaration"
  - "A.6.1:1 — Problem frame"
line_start: 11216
line_end: 11235
dependencies:
  - "A.1"
  - "A.1.1"
  - "A.15.1"
  - "A.15.2"
  - "A.19"
  - "A.2.6"
  - "A.22"
  - "A.22.CGUS"
  - "A.3.1"
  - "A.3.2"
  - "A.6.0"
  - "A.6.5"
  - "A.6.REL"
  - "C.2.1"
  - "C.29"
  - "C.3"
  - "E.10"
  - "E.10.ARCH"
  - "E.20"
  - "E.24.PUB"
  - "F.18"
  - "F.9"
  - "G.11"
keywords:
  - "AdmissibilityConditions"
  - "LawSet"
  - "OperationAlgebra"
  - "U.Mechanism"
  - "application binding"
  - "operation application"
  - "operation declaration"
  - "realization"
---

### A.6.1:1 - Problem frame

An engineer needs a reusable declaration of operations, their typed argument and result positions, the laws they preserve, and the conditions under which an operation is admitted. The declared operation family may be used for physical modeling, clinical calculation, selection, normalization, or another named engineering use.

Use this pattern when the working question is:

> What operation family is being declared, which laws govern it, and under which claim scope, time, selected `CHR:ReferencePlane`, and mechanism conditions may its operations be used?

The primary `EntityOfConcern` of this pattern is one `U.Mechanism` episteme. `U.Mechanism` is a dependent durable U-kind governed through the `U.Signature` identity and content settlement; it adds operation and admission semantics to the reusable declaration. The declared operation family remains the episteme's exact `EntityOfConcernRef` rather than becoming the episteme itself.

**Primary working reader and concern.** The reader is an engineer who needs to reuse or compare an operation declaration without confusing it with the method that uses it, the entity that realizes it, the work that evaluates it, or a publication that presents it.

The first useful move is to name the declared operation family and its subject, then state its `OperationAlgebra`, `LawSet`, `AdmissibilityConditions`, and exact Applicability. Inside each reused operation, declare the exact argument and result meanings, kinds, application predicate, extent rule, and identity rule. Open an actual operation-application binding only after one particular application has been independently identified and its actual bound value matters to a receiving claim. Add a dependency manifest only when names are reused across declarations.

What goes wrong if this pattern is missed: implementation behavior, method instructions, evaluation outcomes, and publication metadata enter the declaration as if they were operation laws. A later user cannot tell whether the declaration changed, one realization failed, or only the evidence became stale.

What this buys: the declaration can remain stable while methods, realizers, evaluations, descriptions, and publications evolve under their own patterns.

Do not use this pattern merely because prose contains words such as mechanism, algorithm, process, or workflow. Recover the current object first. Use A.3.1 when the current object is a semantic way of doing, A.15.1 when it is performed work, and the direct system or episteme pattern when it is a physical assembly or a model description.

