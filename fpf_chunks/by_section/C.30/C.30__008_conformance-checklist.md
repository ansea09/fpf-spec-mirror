---
chunk_kind: "child"
pattern_id: "C.30"
pattern_title: "Grounded Architecture and Selected-Structure Adequacy"
section_id: "C.30:7"
section_title: "Conformance Checklist"
source_path: "FPF-Spec.md"
output_path: "by_section/C.30/C.30__008_conformance-checklist.md"
commit_sha: "56440a9f2e252d7fd462f43470a433dd03413e19"
heading_path:
  - "C.30 — Grounded Architecture and Selected-Structure Adequacy"
  - "C.30:7 — Conformance Checklist"
line_start: 59233
line_end: 59247
dependencies:
  - "A.1"
  - "A.10"
  - "A.15"
  - "A.19.CPM"
  - "A.19.SelectorMechanism"
  - "A.20"
  - "A.21"
  - "A.22"
  - "A.6.3"
  - "A.6.F"
  - "A.6.P"
  - "A.7"
  - "B.3"
  - "C.11"
  - "C.16"
  - "C.18"
  - "C.19"
  - "C.2.1"
  - "C.2.P"
  - "C.25"
  - "C.28"
  - "C.29"
  - "C.30.AD"
  - "C.30.ASV"
  - "C.30.ILC"
  - "C.30.LCA"
  - "C.30.P"
  - "C.30.STRAT"
  - "C.30.TFS-REL"
  - "C.32"
  - "C.32.ADA"
  - "C.32.ADR"
  - "C.32.CONWAY"
  - "C.32.MLAO"
  - "C.32.P2S"
  - "C.32.PAD"
  - "C.33"
  - "C.34"
  - "C.35"
  - "E.10"
  - "E.10.D2"
  - "E.17"
  - "E.17.0"
  - "E.17.1"
  - "E.17.2"
  - "E.18"
  - "E.24.PUB"
  - "F.18"
  - "G.5"
  - "G.6"
keywords:
  - "ArchitectureOf@Context"
  - "architecture claim"
  - "architecture question card"
  - "architecture-description boundary"
  - "artifact-as-architecture guard"
  - "candidate architecture use"
  - "grounded architecture"
  - "selected structure"
---

### C.30:7 - Conformance Checklist

| ID | Requirement | Failed-check repair |
| --- | --- | --- |
| **CC-C30-1 Grounded architecture name.** | A conforming use distinguishes actual subject relations and selected A.22 structure from candidate or expected content, identifies an obtaining `ArchitectureRelation` only when its predicate is satisfied, and gives every `ArchitectureClaim` one exact EntityOfConcern and effective reference scheme. It also names concern, admissible-use frame, and the exact source, description, view, representation, publication form, or other direct use of inspected material. | Rewrite through `ArchitectureQuestionCard@Project`; recover the direct relation, retain modal content only in the claim, or demote the phrase to Plain recognition wording. |
| **CC-C30-2 No `U.Architecture`.** | The pattern use does not mint or rely on a root `U.Architecture`. | Recover the exact A.22 structure and direct `ArchitectureRelation`, or keep candidate or expected content in a claim and use the pattern that defines or tests any other claim. |
| **CC-C30-3 EntityOfConcern and Description-episteme boundary plus specification-use separation.** | Actual subject relation, selected structure, `ArchitectureRelation`, claim, description, view, representation, publication occurrence, publication form, carrier, decision, evidence, and Work stay distinct. | Recover the exact object doing each job; a description, specification use, diagram, list, file, or publication creates no subject-side architecture fact. |
| **CC-C30-4 Exact description subject.** | Every architecture description has one exact C.2.1 EntityOfConcern—holon, obtaining `ArchitectureRelation`, or selected structure—and effective `U.ReferenceScheme`; architecture-claim refs remain optional content or trace. | Recover the exact subject and scheme, or split the description from the bounded architecture claim. |
| **CC-C30-5 View and publication boundary.** | The same description episteme is `U.View` only through an independently obtaining E.17.0 conformance relation to one exact viewpoint; representation, publication occurrence, form, carrier, and publication currentness remain separate. | Apply `C.30.AD`, `E.17.0`, C.29, and E.24.PUB to the exact objects; remove any view membership inferred from authoring, query, bundle, diagram, file, rendering, or publication. |
| **CC-C30-6 Small output before heavy record.** | Ordinary use may stop once one next architecture move and the applicable pattern for any separate claim are clear; use `ArchitectureQuestionCard@Project` only when the result must be retained, compared, or handed on. | Remove needless card or full-record expansion, or explain which persistence or full-mode trigger is present. |
| **CC-C30-7 Structure-kind boundary.** | Structural-view claims apply `C.30.ASV`; module, function, flow, control, work, evidence, scale, and decision claims do not collapse into C.30. | Name the structure kind, state the structural view if needed, or use the pattern that defines or tests the separate claim. |
| **CC-C30-8 Characteristic assignment.** | Quality, measure, score, metric, modularity, and `ility` wording recovers its bearer and the applicable characteristic pattern before use. | Add `ArchitectureCharacteristicAssignment`, or keep the phrase as ordinary recognition wording rather than a C.30 claim. |
| **CC-C30-9 Non-architecture claim kind.** | For each evidence, assurance, causal, gate, work, decision, publication-use authority, mathematical-lens, measurement, or release claim, name its kind and the FPF pattern that defines or tests it. | Keep the C.30 record limited to architecture and selected-structure adequacy. |
| **CC-C30-10 Useful action.** | The repaired wording leaves a surviving admissible action: name the architecture claim, recover the exact use of inspected material, state an architecture structural view, add a source or reliance relation, add a `SourceReturnCondition`, or apply the FPF pattern that defines or constrains the claim kind being made. | Restore that action, or classify the phrase as reduced-use cue, quote-only wording, blocked transfer, or incomplete rewrite. |

