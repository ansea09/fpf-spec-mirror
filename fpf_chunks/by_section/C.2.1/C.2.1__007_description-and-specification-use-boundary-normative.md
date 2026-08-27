---
chunk_kind: "child"
pattern_id: "C.2.1"
pattern_title: "U.Episteme: Constitution, Empirical Grounding, and Edition Relations"
section_id: "C.2.1:6"
section_title: "Description and specification-use boundary  (normative)"
source_path: "FPF-Spec.md"
output_path: "by_section/C.2.1/C.2.1__007_description-and-specification-use-boundary-normative.md"
commit_sha: "322625be006f38158e4e7d600f662558f03df77a"
heading_path:
  - "C.2.1 — U.Episteme: Constitution, Empirical Grounding, and Edition Relations"
  - "C.2.1:6 — Description and specification-use boundary  (normative)"
line_start: 41135
line_end: 41154
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

A Description episteme is a `U.Episteme` whose exact EntityOfConcern is the entity being described. Description does not create a second kind beside ordinary epistemes; it names the current relation and use of one episteme.

For a description use, keep these values recoverable:

| Value | Meaning | Identity status |
| --- | --- | --- |
| `entityOfConcernRef` | designation of the exact EntityOfConcern in the description episteme's constitution relation | its resolved exact EntityOfConcern, not the reference value or designation, is C.2.1 identity-bearing |
| effective `U.ReferenceScheme` | rules by which the description claims refer to and can be checked against that entity | C.2.1 identity-bearing |
| `viewpointRef`, when current | governed reference resolving to the exact `U.Viewpoint` episteme selected for this describing use under E.17.0 | use qualifier outside episteme identity; work that changes an identity discriminator identifies another episteme independently |
| `claimScopeRef`, when current | designation of the exact `U.ClaimScope` under A.2.6 | claim-use qualifier |
| `modelUseStructureRef`, when current | designation of one independently selected `BoundedModelUseStructure : U.Structure` | optional interpretation qualifier, not a context root |

When a filled card used to describe the entity has recoverable claim content, EntityOfConcern, and effective reference scheme, it is one episteme carrying these values. Its reusable layout can be a publication form, and the exact sheet or file that bears that layout can be a `U.PresentationCarrier`. The episteme, form, and carrier are not direct relation occurrences, and none makes a viewpoint, scope, or model-use relation obtain.

Use `E.10.D2` to keep the EntityOfConcern, its Description episteme, and specification use distinct. A Description episteme is admitted for specification use only when its claims are checkable and a named harness or validation relation can test them. Preserve or update a selected viewpoint only for the named describing use whose reliance depends on it. The suffix `Spec`, formal notation, approval appearance, or publication in a repository does not grant that use.

Self-description uses the same rule. If an episteme describes itself, its EntityOfConcern designation resolves to that episteme. If a review episteme describes it, the review episteme has the first episteme as EntityOfConcern and its own claim content and reference scheme.

