---
chunk_kind: "child"
pattern_id: "A.22"
pattern_title: "Structure and Structural Views (STRUCT-CAL)"
section_id: "A.22:7"
section_title: "Conformance Checklist"
source_path: "FPF-Spec.md"
output_path: "by_section/A.22/A.22__008_conformance-checklist.md"
commit_sha: "4b75b56c13f5d61be5238fdbc7c20af5c6f89df7"
heading_path:
  - "A.22 — Structure and Structural Views (STRUCT-CAL)"
  - "A.22:7 — Conformance Checklist"
line_start: 34234
line_end: 34252
dependencies:
  - "A.1"
  - "A.1.1"
  - "A.10"
  - "A.14"
  - "A.15"
  - "A.15.1"
  - "A.2.6"
  - "A.20"
  - "A.21"
  - "A.22.CGUS"
  - "A.3.1"
  - "A.6.0"
  - "A.6.1"
  - "A.6.2"
  - "A.6.3"
  - "A.6.5"
  - "A.6.F"
  - "A.6.P"
  - "A.6.REL"
  - "A.7"
  - "B.3"
  - "C.11"
  - "C.13"
  - "C.16"
  - "C.2.1"
  - "C.2.P"
  - "C.25"
  - "C.28"
  - "C.29"
  - "C.30"
  - "C.30.ASV"
  - "C.30.ILC"
  - "C.30.LCA"
  - "C.30.P"
  - "C.30.STRAT"
  - "C.30.TFS-REL"
  - "C.33"
  - "C.34"
  - "C.35"
  - "E.10"
  - "E.10.D2"
  - "E.17.0"
  - "E.17.1"
  - "E.18"
  - "E.18.3"
  - "E.24"
  - "E.24.PUB"
  - "F.18"
  - "G.5"
  - "G.6"
keywords:
---

### A.22:7 - Conformance Checklist

| ID | Requirement | Failed-check repair |
| --- | --- | --- |
| **CC-A22-1 Base identity.** | The selected `U.Structure` is recoverable from exact independently identified constituents, exact selected obtaining relation occurrences, exact constraints as applied, and one named selection-use frame. | Recover the missing discriminator. If a constituent or obtaining relation lacks a direct governor, stop at that blocker rather than naming a structure from a graph or record. |
| **CC-A22-1a Independent grounding.** | Every constituent and selected relation occurrence keeps its direct identity; a collection, constraint episteme, graph, table, description, view, or publication neither creates them nor makes a relation obtain. | Apply the constituent and direct relation patterns first; treat the visible artifact as a C.29 representation or C.2.1 episteme only when that is what is present. |
| **CC-A22-1b Selection work and result separation.** | When a load-bearing selection claim is current, an exact system performs method-governed dated work through exact participation relations or A.6.1 bindings. Any durable result is a separate C.2.1 episteme, and any accountable choice remains under its decision governor. | Name the acting system, method, work, bindings, and result or decision separately; remove them from structure identity. |
| **CC-A22-1c Reidentification.** | A changed designator, method, work, result episteme, graph, description, or publication leaves the structure unchanged when all four identity discriminators remain unchanged; a changed discriminator reopens identity. | Compare the four discriminators and apply each selected relation occurrence's direct identity rule before reapplying A.22. |
| **CC-A22-2 Non-agentive structure.** | Structure wording does not make the structure, pattern, constraint, graph, or result act, select, optimize, prove, decide, warrant, sense, plan, or adapt. | Name the exact acting system and its work or apply the governing proof, decision, or work pattern; keep A.22 to selected organization. |
| **CC-A22-3 Structure-claim reliance relation boundary.** | When source-description, source-use, base-dependence, grounding, evidence, lens, simulation, extraction, or representation reliance is claimed, the governing A.6.6 relation ontology, source-description ontology, evidence ontology, lens ontology, assurance ontology, causal ontology, gate ontology, decision ontology, or publication ontology is named. | Add the governing pattern, relation kind where the relation is being claimed, validation boundary, admissible use, and non-admissible use, or mark the reliance phrase as carrying no admissible reliance. |
| **CC-A22-4 Description and view separation.** | A structural description, structural view, extracted view, diagram, table, graph, dashboard, or publication face is not treated as the structure itself. | Treat the visible form as description, view, source-description relation, A.6.6 base declaration, publication form, or publication and name the selected structure separately only if selected organization is being claimed. |
| **CC-A22-5 DescriptionContext reuse.** | Description epistemes and specification-use cases reuse `DescriptionContext` and `U.Episteme`; E.17.0 alone governs `U.View` membership, while A.6.3 governs optional viewing construction. No second architecture-local description or view ontology is introduced. | Replace local description or view fields with the imported use qualification, conformance relation, or construction relation governed by the exact neighboring pattern. |
| **CC-A22-6 Structure-use return.** | `StructureUseReturnCondition` is present when hidden selected-structure, source-basis, source-description, evidence, lens, simulation, extraction, or representation distinctions are used for action, assurance, causal use, legal or regulatory review, comparison, or decision reopening. | Add one structure-use return condition or narrow the record's admissible use so the hidden distinction is not relied on. |
| **CC-A22-7 Non-structure claim kind.** | Evidence, assurance, gate, release, causal, dynamics, measurement, work, decision, publication, bridge, and mathematical-lens claims are assigned to their governing patterns. | The check passes when the governing FPF pattern and the claim kind being made are named, while the A.22 record remains limited to selected-structure use. |
| **CC-A22-8 Architecture pattern application.** | Architecture claims use `C.30` and `ArchitectureOf@Context`; A.22 does not treat architecture as a root kind or define C.30-specific records. | Apply C.30 or a C.30 subpattern and keep A.22 only as the selected-structure EntityOfConcern and structure-claim reliance relation. |
| **CC-A22-9 Plain and Tech recovery.** | Plain structure phrases may remain, but if they carry ontological, evidence, causal, assurance, bridge, gate, work, decision, or admissibility claim, the relevant Tech fields and FPF pattern applications are recoverable. | Add the missing Tech fields or demote the Plain phrase to ordinary recognition wording. |
| **CC-A22-10 Useful action.** | The repair leaves a remaining admissible practitioner use: name the structure, name the structure-claim reliance relation record by value, state a structural view, add a `StructureUseReturnCondition`, or apply the FPF pattern that governs the claim kind being made. | Restore that use, or classify the phrase as reduced-use cue, quote-only wording, blocked transfer, or incomplete rewrite. |
| **CC-A22-11 CGUS admission.** | A constraint-governed unfolding claim names several loci, cross-locus constraints, preserved and lost structure, direct governing-pattern exits, admissible next forms, and stop or return conditions. | Use `A.22.CGUS` only after those fields are recoverable; otherwise lower the visible route-shaped artifact to a description, demonstrative slice, README seed, or ordinary cue. |

