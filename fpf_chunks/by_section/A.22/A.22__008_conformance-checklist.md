---
chunk_kind: "child"
pattern_id: "A.22"
pattern_title: "Structure and Structural Views (STRUCT-CAL)"
section_id: "A.22:7"
section_title: "Conformance Checklist"
source_path: "FPF-Spec.md"
output_path: "by_section/A.22/A.22__008_conformance-checklist.md"
commit_sha: "205de763b710fe9f2baecbcdae132ec8fdbbe38c"
heading_path:
  - "A.22 — Structure and Structural Views (STRUCT-CAL)"
  - "A.22:7 — Conformance Checklist"
line_start: 29477
line_end: 29491
dependencies:
  - "A.1"
  - "A.10"
  - "A.14"
  - "A.15"
  - "A.20"
  - "A.21"
  - "A.6.2"
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
  - "C.30"
  - "C.30.AD"
  - "C.30.ASV"
  - "C.30.ILC"
  - "C.30.LCA"
  - "C.30.P"
  - "C.30.STRAT"
  - "C.30.TFS-REL"
  - "E.10"
  - "E.10.D2"
  - "E.17"
  - "E.17.0"
  - "E.17.1"
  - "E.18"
  - "E.24"
  - "E.24.PUB"
  - "F.18"
  - "G.5"
  - "G.6"
keywords:
  - "architecture-description boundary"
  - "preserved and lost structure"
  - "selected structure"
  - "source return"
  - "structural description"
  - "structural view"
  - "structure"
---

### A.22:7 - Conformance Checklist

| ID | Requirement | Failed-check repair |
| --- | --- | --- |
| **CC-A22-1 Selected structure EntityOfConcern.** | An FPF-governed structure claim names `U.Structure` or an existing FPF kind or relation named by value record; it does not mint an architecture-adjacent root kind. | Replace the broad noun with `U.Structure` or assign the claim to the existing FPF kind or relation named by value record. |
| **CC-A22-2 Non-agentive structure.** | Structure wording does not make the structure act, optimize, prove, decide, warrant, sense, plan, or adapt. | Apply the governing pattern for the agency, proof, decision, or work claim and keep A.22 to selected organization. |
| **CC-A22-3 Structure-claim reliance relation boundary.** | When source, base-dependence, grounding, evidence, lens, simulation, extraction, or representation reliance is claimed, the governing A.6.6 relation ontology, source-description ontology, evidence ontology, lens ontology, assurance ontology, causal ontology, gate ontology, decision ontology, or publication ontology is named. | Add the governing pattern, relation kind where the relation is being claimed, validation boundary, admissible use, and non-admissible use, or mark the reliance phrase as carrying no admissible reliance. |
| **CC-A22-4 Description and view separation.** | A structural description, structural view, extracted view, diagram, table, graph, dashboard, or publication face is not treated as the structure itself. | Treat the visible form as description, view, source-description relation, A.6.6 base declaration, publication form, or publication and name the selected structure separately only if selected organization is being claimed. |
| **CC-A22-5 DescriptionContext reuse.** | Description epistemes and specification-use cases reuse `DescriptionContext`, `U.Episteme`, `U.View`, `A.6.3`, and `E.17` machinery; no second architecture-local description and view ontology is introduced. | Replace local description and view fields with the imported DescriptionContext fields or assign the claim to the existing governing pattern. |
| **CC-A22-6 Source return.** | `SourceReturnCondition` is present when hidden source-side distinctions are used for action, assurance, causal use, legal or regulatory review, comparison, or decision reopening. | Add one source-return condition or narrow the record's admissible use so the hidden distinction is not relied on. |
| **CC-A22-7 Non-structure claim kind.** | Evidence, assurance, gate, release, causal, dynamics, measurement, work, decision, publication, bridge, and mathematical-lens claims are assigned to their governing patterns. | Name the governing FPF pattern and the claim kind being made; do not add fields to A.22 to absorb it. |
| **CC-A22-8 Architecture pattern application.** | Architecture claims use `C.30` and `ArchitectureOf@Context`; A.22 does not treat architecture as a root kind or define C.30-specific records. | Apply C.30 or a C.30 subpattern and keep A.22 only as the selected-structure EntityOfConcern and structure-claim reliance relation. |
| **CC-A22-9 Plain and Tech recovery.** | Plain structure phrases may remain, but if they carry ontological, evidence, causal, assurance, bridge, gate, work, decision, or admissibility claim, the relevant Tech fields and FPF pattern applications are recoverable. | Add the missing Tech fields or demote the Plain phrase to ordinary recognition wording. |
| **CC-A22-10 Useful action.** | The repair leaves a surviving admissible practitioner move: name the structure, name the structure-claim reliance relation named by value, state a structural view, add a `SourceReturnCondition`, or apply the FPF pattern that governs the claim kind being made. | Restore that move, or classify the phrase as reduced-use cue, quote-only wording, blocked transfer, or incomplete rewrite. |

