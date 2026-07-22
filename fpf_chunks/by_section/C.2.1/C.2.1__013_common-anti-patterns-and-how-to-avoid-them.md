---
chunk_kind: "child"
pattern_id: "C.2.1"
pattern_title: "U.Episteme: Constitution, Empirical Grounding, and Edition Relations"
section_id: "C.2.1:12"
section_title: "Common Anti-Patterns and How to Avoid Them"
source_path: "FPF-Spec.md"
output_path: "by_section/C.2.1/C.2.1__013_common-anti-patterns-and-how-to-avoid-them.md"
commit_sha: "0990ff1d1ccee4587b8f7e16e7a725a8edbe66b4"
heading_path:
  - "C.2.1 — U.Episteme: Constitution, Empirical Grounding, and Edition Relations"
  - "C.2.1:12 — Common Anti-Patterns and How to Avoid Them"
line_start: 40710
line_end: 40725
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

### C.2.1:12 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Actual failure | Repair |
| --- | --- | --- |
| Filled-card ontology | A completed record is treated as what makes an episteme or relation exist. | Recover the C.2.1 identity first. Identify a filled card as an episteme only when its claim content, EntityOfConcern, and effective reference scheme are recoverable; identify its reusable layout, exact carrier, and publication occurrence separately under their direct patterns. |
| Manifest-created declaration | A manifest row, list, citation, identifier, or edition marker is treated as creating declaration identity, `U.Signature` membership, or a dependency. | Identify the declaration episteme through the C.2.1 triple, judge same-individual `U.Signature` membership under A.6.0, and expose a manifest only for actual dependencies or provided names. A readable one-off assertion stops without either. |
| Classification as admission relation | A candidate is said to acquire or lose holonhood when a governing FPF pattern or assertion changes. | Apply the `A.1` constructive criterion for an admitted holon kind; let `E.24.UK` govern only admission of that public kind; identify a separate C.2.1 assertion episteme when project review needs the classification claim. |
| Dependent kind as second identity | `U.MethodDescription`, `U.View`, or another dependent episteme kind is given an extra identity discriminator merely because its direct pattern supplies a membership condition. | Keep the C.2.1 identity of the same episteme individual. Apply the direct pattern only to judge dependent-kind membership; if work changes a C.2.1 discriminator, identify the resulting episteme through that changed discriminator. |
| Context identifier in episteme identity by habit | A surrounding project or model-use context identifier is treated as identifying every episteme used there. | Keep the shared C.2.1 identity context-independent; add claim scope, viewpoint, or bounded model-use structure only through the direct relation on which the current use depends. |
| Grounding by evidence presence | Stored evidence is treated as an automatic empirical-grounding relation. | Recover the direct observation, intervention, measurement, or evaluation relations involving the exact grounding holon and test continuity of `EpistemeEmpiricalGroundingRelation`. Evidence availability or absence alone determines no world-side grounding state; known obtaining or nonobtaining follows the direct structure, while uncertainty about that structure gives an affirmative grounding assertion unresolved reliance for the declared use. |
| Edition work as relation participant | Revision work is inserted into `EpistemeEditionRelation`, so two works appear to create two continuities between the same editions. | Keep earlier and later epistemes as the two participants; recover exact source-to-revision use, enacted-method semantics, actual change facts, any separately governed entity-identity-inception claim, evaluation, and evidence separately. If a required inception claim lacks a current direct governor, return the exact missing-governor blocker. |
| Edition by filename | `v2` or a later timestamp is taken as epistemic succession. | Recover the two episteme identities, then test edition continuity through identified revision work, exact source-to-revision use, enacted-method semantics, and actual change facts. If that test also requires an entity-identity-inception claim, use a current direct governor only when one actually exists; otherwise return the exact missing-governor blocker. |
| Published-episteme kind | Temporary participation in publication is treated as a second durable episteme kind. | Keep the episteme identity and state the exact publication occurrence; use Plain `published episteme` only for that contingent use. |
| View as formatting, generation, or publication | A filtered table, diagram, query result, or published face is called a view because of appearance, construction history, or carrier, and a heading or edge is treated as cross-view correspondence. | Identify the receiving episteme under C.2.1 and apply `E.17.0` conformance for `U.View` membership. Add A.6.3 only for an actual source-to-receiving construction. Apply the exact direct subject-relation governor to correspondence; if none is recoverable, return an exact blocker naming the participants, required predicate and use, and missing governor. |
| Mathematical identity leak | A tuple key or graph node identity becomes episteme identity. | Keep C.29 representation identity separate and use the C.2.1 identity triple. |

