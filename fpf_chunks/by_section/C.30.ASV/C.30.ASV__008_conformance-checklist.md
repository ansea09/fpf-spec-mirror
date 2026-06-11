---
chunk_kind: "child"
pattern_id: "C.30.ASV"
pattern_title: "Architecture Structural View Adequacy (ASV)"
section_id: "C.30.ASV:7"
section_title: "Conformance Checklist"
source_path: "FPF-Spec.md"
output_path: "by_section/C.30.ASV/C.30.ASV__008_conformance-checklist.md"
commit_sha: "3f9a2dd65b0df9cf6bed602fb1f189162060954f"
heading_path:
  - "C.30.ASV — Architecture Structural View Adequacy (ASV)"
  - "C.30.ASV:7 — Conformance Checklist"
line_start: 53777
line_end: 53794
dependencies:
  - "A.10"
  - "A.15"
  - "A.20"
  - "A.21"
  - "A.22"
  - "A.6.3"
  - "A.6.F"
  - "A.6.M"
  - "A.7"
  - "B.3"
  - "C.11"
  - "C.16"
  - "C.2.P"
  - "C.25"
  - "C.28"
  - "C.29"
  - "C.30"
  - "C.30.ILC"
  - "C.30.LCA"
  - "C.30.P"
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
  - "ArchitectureStructureKindRef"
  - "VF.ARCH.STRUCTURE"
  - "architecture structural view"
  - "correspondence"
  - "hidden/lost structure"
  - "source return"
  - "structure kind"
  - "viewpoint bundle"
---

### C.30.ASV:7 - Conformance Checklist

| ID | Requirement | Failed-check repair |
| --- | --- | --- |
| **CC-ASV-1 Structure target.** | Every architecture structural view names `structureRefs` or a recoverable selected-structure reference. | Name the selected structure reference, or downgrade the artifact to an architecture question, diagram, note, or publication that does not claim to be a structural view. |
| **CC-ASV-2 Structure kind.** | Every architecture structural view names `structureKindRef`. | Run `ArchitectureStructureKindTriage@Project`; if no structure kind changes action, keep the text as ordinary prose or a source note. |
| **CC-ASV-3 Same selected architecture claim.** | The view preserves `architectureClaimRef`, `DescriptionContext`, and the claim record's `describedHolonRef` and `boundedContextRef` unless explicit retargeting or a bridge is declared. | Restore the same claim record and bounded context, or add an explicit retargeting or bridge note before using the view. |
| **CC-ASV-4 Viewpoint discipline.** | The view is under `VF.ARCH.STRUCTURE` or another declared architecture-specific bundle, rather than an ad-hoc tag. | Assign the view to `VF.ARCH.STRUCTURE`, a declared local viewpoint bundle, or a governing pattern; otherwise keep the label as Plain recognition wording. |
| **CC-ASV-5 Lost structure.** | The view names hidden or lost structure, especially for query, extraction, coarsening, or publication uses. | Add a one-line hidden-structure note or lost-structure note, or narrow the admissible use so omitted structure is not relied on. |
| **CC-ASV-6 Correspondence.** | Cross-view relations are carried by `correspondenceModelRefs` or correspondence records, not by prose alone. | Add a correspondence note or stop at a single-view statement without cross-view consistency claim. |
| **CC-ASV-7 No publication collapse.** | A diagram, model, table, dashboard, generated relation graph, or ADR is kept as publication, record, or carrier, not the architecture structural view itself. | Keep the artifact as publication or carrier and name the source episteme or view; do not require a full architecture view unless it changes the next move. |
| **CC-ASV-8 No single-view architecture.** | If a decision uses an architecture view as decision claim, it names the affected structures and views, not only one favored diagram. | Add affected structure and view refs, or narrow the statement to the single view's admissible use. |
| **CC-ASV-9 No proof overread.** | The view does not act as evidence, safety proof, causal proof, gate decision, or work record without a named governing pattern. | Assign the claim being made to `A.10`, `G.6`, `B.3`, `A.20`, `A.21`, `C.28`, or mark the proof, evidence, gate, or assurance use unsupported; do not add more C.30.ASV fields as a substitute. |
| **CC-ASV-10 Relation or correspondence record named by value.** | Every cross-reference names the kind named by value, relation, or record: selected structure, structure kind, viewpoint, correspondence record, allocation record, bridge record, evidence relation, publication carrier when a publication relation is being made, interface specification, or governing record named by value. | Replace the ambiguous reference with the kind, relation, or record that actually carries the claim, or split the sentence into separate records. |
| **CC-ASV-11 Source return.** | When compression, extraction, coarsening, evidence reuse, publication, or many-to-many allocation hides distinctions, `SourceReturnCondition` is present. | Add one source-return trigger, or narrow the view's admissible use so omitted distinctions are not used for action, assurance, causal use, legal review, regulatory review, or reopening. |
| **CC-ASV-12 Architecture-name recovery.** | Every `<X>Architecture` phrase recovers `<X>StructureKind` or a declared local relation. | Rewrite the phrase through `ArchitectureStructureKindTriage@Project`; if no relation is being claimed, keep the name as Plain prose and do not let it carry ontology. |
| **CC-ASV-13 Useful action.** | The repair leaves a surviving admissible architecture move: inspect, split, relate, downgrade, assign to a governing pattern, generate candidates, stop, state a structural view, add correspondence, add source return, or apply the governing pattern. | Restore one move, or classify the phrase as reduced-use cue, quote-only wording, blocked transfer, or incomplete rewrite. |

