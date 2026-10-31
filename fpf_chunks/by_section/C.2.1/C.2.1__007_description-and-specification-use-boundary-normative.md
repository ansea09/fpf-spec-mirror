---
chunk_kind: "child"
pattern_id: "C.2.1"
pattern_title: "U.Episteme: Constitution, Empirical Grounding, and Edition Relations"
section_id: "C.2.1:6"
section_title: "Description and specification-use boundary  (normative)"
source_path: "FPF-Spec.md"
output_path: "by_section/C.2.1/C.2.1__007_description-and-specification-use-boundary-normative.md"
commit_sha: "5018da7d3b2b6a6e722fb76defe5cf991a64ba14"
heading_path:
  - "C.2.1 — U.Episteme: Constitution, Empirical Grounding, and Edition Relations"
  - "C.2.1:6 — Description and specification-use boundary  (normative)"
line_start: 51666
line_end: 51695
dependencies:
  - "A.1"
  - "A.1.1"
  - "A.10"
  - "A.14"
  - "A.2.6"
  - "A.22"
  - "A.3.1"
  - "A.3.2"
  - "A.3.4"
  - "A.6.0"
  - "A.6.1"
  - "A.6.2"
  - "A.6.3"
  - "A.6.3.RT"
  - "A.6.4"
  - "A.6.5"
  - "A.6.REL"
  - "A.7"
  - "B.3"
  - "C.13"
  - "C.2.1"
  - "C.2.P"
  - "C.29"
  - "C.3.2"
  - "E.10.D2"
  - "E.13"
  - "E.17"
  - "E.17.0"
  - "E.24.PUB"
  - "E.24.UK"
  - "F.9"
  - "G.11"
  - "U.Episteme"
  - "U.MethodDescription"
  - "U.Signature"
  - "U.View"
keywords:
---

### C.2.1:6 - Description and specification-use boundary  *(normative)*

In a claim-bearing-result use, “description” designates episteme E, a `U.Episteme` identified by its claim content G, EntityOfConcern T and effective ReferenceScheme R. The word supplies no additional subtype criterion or relation. For a comparison of the claims alone, identify G; for a correction to wording or layout, identify the expression and the meaning it must preserve. Section :4.0.5 explains how to recover the intended object from the actual use.

When these values affect the current description use, keep them recoverable:

| Value | Meaning | Identity status |
| --- | --- | --- |
| `entityOfConcernRef` | designation of the exact EntityOfConcern in the description episteme's constitution relation | its resolved exact EntityOfConcern, not the reference value or designation, is C.2.1 identity-bearing |
| effective `ReferenceScheme` | rules by which the description claims refer to and can be checked against that entity | C.2.1 identity-bearing |
| `viewpointRef`, when current | governed reference resolving to the exact `U.Viewpoint` episteme selected for this describing use under E.17.0 | use qualifier outside episteme identity; work that changes an identity discriminator identifies another episteme independently |
| `claimScopeRef`, when current | designation of the exact `U.ClaimScope` under A.2.6 | claim-use qualifier |
| `modelUseStructureRef`, when current | designation of one independently selected `BoundedModelUseStructure : U.Structure` | optional interpretation qualifier, not a context root |


For specification use, recover all applicable conditions:

1. the exact description episteme and its C.2.1 constitution;
2. checkable claims, invariants, criteria, or acceptance conditions in its ClaimGraph;
3. a named harness, validation, conformance, measurement, or evaluation relation capable of checking those claims for the stated use;
4. when viewpoint selection affects reliance, the named describing use and its exact selected viewpoint are preserved or explicitly updated.

Declared formality, notation discipline, comparators, tolerances, and measurement rules are named when the claims depend on them. They do not substitute for the checkable claims or the harness. If the conditions are absent, call the episteme a description and present proposed criteria as proposals; a `Spec` suffix, schema, signature, approval, or publication does not supply specification force.

Specification use does not create another episteme identity. A revision that changes ClaimGraph, EntityOfConcern, or effective ReferenceScheme identifies another episteme under C.2.1; a changed harness, evaluation result, publication, or relying use changes its own neighboring object or relation.

E.10.D2:4.1.3 applies these conditions to a proposed `...Spec` name.

Self-description uses the same rule. If an episteme describes itself, its EntityOfConcern designation resolves to that episteme. If a review episteme describes it, the review episteme has the first episteme as EntityOfConcern and its own claim content and reference scheme.

