---
chunk_kind: "child"
pattern_id: "C.30"
pattern_title: "Grounded Architecture and Selected-Structure Adequacy"
section_id: "C.30:7"
section_title: "Conformance Checklist"
source_path: "FPF-Spec.md"
output_path: "by_section/C.30/C.30__008_conformance-checklist.md"
commit_sha: "ec66cbef9f337bca279d86e825db0947f90e2598"
heading_path:
  - "C.30 — Grounded Architecture and Selected-Structure Adequacy"
  - "C.30:7 — Conformance Checklist"
line_start: 51784
line_end: 51798
dependencies:
  - "A.10"
  - "A.15"
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
  - "C.30.TGA-FLOW-REL"
  - "E.10"
  - "E.10.D2"
  - "E.17"
  - "E.17.0"
  - "E.17.1"
  - "E.17.2"
  - "E.18"
  - "F.18"
  - "G.6"
keywords:
  - "ArchitectureOf@Context"
  - "architecture claim"
  - "architecture question card"
  - "architecture-description boundary"
  - "artifact-as-architecture guard"
  - "grounded architecture"
  - "selected structure"
---

### C.30:7 - Conformance Checklist

| ID | Requirement | Failed-check repair |
| --- | --- | --- |
| **CC-C30-1 Grounded architecture name.** | An FPF-governed architecture claim names the described holon, bounded context, selected structures, structure kinds, artifact role, admissible use, and non-admissible use. | Rewrite the phrase through `ArchitectureQuestionCard@Project` or demote it to Plain recognition wording. |
| **CC-C30-2 No `U.Architecture`.** | The pattern use does not mint or rely on a root `U.Architecture`. | Use `ArchitectureOf@Context` over selected A.22 structures, or assign the claim to another existing kind. |
| **CC-C30-3 EntityOfConcern and Description-episteme boundary plus specification-use separation.** | Architecture claim, structure, description, view, publication face, carrier, decision, evidence, and work stay distinct. | Downgrade the artifact or carrier to its description, specification-use, or publication role and name the claim or non-architecture claim kind separately. |
| **CC-C30-4 ArchitectureOf record.** | Architecture descriptions and views point through `ArchitectureOf@Context`; the described holon is recovered through `architectureClaimRef.describedHolonRef`. | Add `ArchitectureOf@Context` or split direct holon description from architecture-claim description. |
| **CC-C30-5 DescriptionContext reuse.** | `ArchitectureDescription@Context` reuses `DescriptionContext` and existing DescriptionContext machinery; it does not redefine viewpoint or publication ontology. | Replace local fields with imported DescriptionContext fields, apply `C.30.AD` when the full architecture-description mechanism is live, or assign the publication or view claim to E.17, A.6.3, or E.17.0. |
| **CC-C30-6 Small output before heavy record.** | Ordinary use may stop at `ArchitectureQuestionCard@Project` when one next architecture move and exact governing pattern application is clear. | Remove needless full-record expansion or explain which full-mode trigger is live. |
| **CC-C30-7 Structure-kind boundary.** | Structural-view claims apply `C.30.ASV`; module, function, flow, control, work, evidence, scale, and decision claims do not collapse into C.30. | Name the structure kind, open the structural view if needed, or assign the claim to the exact governing pattern. |
| **CC-C30-8 Characteristic assignment.** | Quality, measure, score, metric, modularity, and `ility` wording recovers its bearer and governing pattern before use. | Add `ArchitectureCharacteristicAssignment`, or narrow the sentence to ordinary non-FPF-governed recognition. |
| **CC-C30-9 Non-architecture claim kind.** | Evidence, assurance, causal, gate, work, decision, publication-authority, mathematical-lens, measurement, and release claims are assigned to their governing patterns. | Name the exact governing FPF pattern and the live claim kind; do not add fields to C.30 to absorb it. |
| **CC-C30-10 Useful action.** | The repaired wording leaves a surviving admissible action: name the architecture claim, downgrade an artifact, open an architecture structural view, add a source or reliance relation, return to source, or apply the exact governing pattern that carries the live claim kind. | Restore that action, or classify the phrase as reduced-use cue, quote-only wording, blocked transfer, or incomplete rewrite. |

