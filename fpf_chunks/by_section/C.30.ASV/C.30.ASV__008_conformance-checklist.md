---
chunk_kind: "child"
pattern_id: "C.30.ASV"
pattern_title: "Architecture Structural View Adequacy (ASV)"
section_id: "C.30.ASV:7"
section_title: "Conformance Checklist"
source_path: "FPF-Spec.md"
output_path: "by_section/C.30.ASV/C.30.ASV__008_conformance-checklist.md"
commit_sha: "11f2345e65e4b2ec5b84c0cecde4c9485834d28d"
heading_path:
  - "C.30.ASV — Architecture Structural View Adequacy (ASV)"
  - "C.30.ASV:7 — Conformance Checklist"
line_start: 62450
line_end: 62467
dependencies:
  - "A.1"
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
  - "C.2.1"
  - "C.2.P"
  - "C.25"
  - "C.28"
  - "C.29"
  - "C.30"
  - "C.30.ILC"
  - "C.30.LCA"
  - "C.30.P"
  - "C.30.TFS-REL"
  - "C.32"
  - "C.32.ADA"
  - "C.32.ADR"
  - "C.32.P2S"
  - "C.32.PAD"
  - "C.33"
  - "C.34"
  - "C.35"
  - "E.10"
  - "E.10.D2"
  - "E.17.0"
  - "E.17.1"
  - "E.17.2"
  - "E.18"
  - "E.24.PUB"
  - "F.18"
  - "G.6"
keywords:
---

### C.30.ASV:7 - Conformance Checklist

| ID | Requirement | Failed-check repair |
| --- | --- | --- |
| **CC-ASV-1 Structure target.** | Every architecture structural view has one exact selected `U.Structure` as its C.2.1 EntityOfConcern. | Name and constitute the selected structure under A.22, or keep the inspected episteme or publication as an architecture question input that does not yet claim to be a structural view. |
| **CC-ASV-2 Structure kind.** | Every architecture structural view names `structureKindRef`. | Use `ArchitectureStructureKindTriage@Project`; if no structure kind changes action, keep the text as ordinary prose or a source note. |
| **CC-ASV-3 Exact episteme and subject trace.** | The view preserves one exact claim graph, one selected-structure EntityOfConcern, effective `U.ReferenceScheme`, and the subject trace to the exact holon and any obtaining `ArchitectureRelation`; optional architecture claim, ClaimScope, empirical grounding, and model-use structure remain separate. | Restore the exact episteme identity and subject trace, or identify a new description before relying on it; do not derive identity from an architecture-claim field or context bundle. |
| **CC-ASV-4 Viewpoint conformance.** | The candidate episteme and exact viewpoint episteme satisfy the fixed five-part E.17.0 predicate, and `viewpointConformanceRelationRef` names the participant-determined obtaining occurrence. A bundle or viewpoint label is only discovery support. | Apply E.17.0. If the predicate does not obtain, keep a structural description or triage result and do not call it `U.View`. |
| **CC-ASV-5 Lost structure.** | The view names hidden or lost structure, especially for query, extraction, coarsening, or publication uses. | Add a one-line hidden-structure note or lost-structure note, or narrow the admissible use so omitted structure is not relied on. |
| **CC-ASV-6 Correspondence.** | Cross-view claims are carried by exact correspondence claims or independently established obtaining relations, not by prose, shared packaging, or graph adjacency alone. | Add a correspondence claim or direct relation, or stop at a single-view statement without a cross-view consistency claim. |
| **CC-ASV-7 No representation/publication collapse.** | A diagram, model, table, dashboard, generated relation graph, ADR, publication occurrence, form, or carrier is kept separate from the view episteme and selected structure. | Name the exact description episteme, any C.29 representation, and the E.24.PUB occurrence/form/carrier separately; claim `U.View` only when E.17.0 conformance obtains. |
| **CC-ASV-8 No single-view architecture.** | If a decision uses an architecture view, it names the affected structures and views, not only one favored diagram. | Add affected structure and view refs, or narrow the decision to the single view's admissible use. |
| **CC-ASV-9 No proof overread.** | The view does not stand in for empirical grounding, evidence, safety proof, causal proof, gate decision, or work record; each such claim needs its own obtaining relation and applicable pattern. | Use `EpistemeEmpiricalGroundingRelation`, `A.10`, `G.6`, `B.3`, `A.20`, `A.21`, or `C.28` for the applicable claim, or mark it unsupported; do not add more ASV fields as a substitute. |
| **CC-ASV-10 Relation or correspondence record named by value.** | Every cross-reference names the exact kind, claim, relation, or record: selected structure, structure kind, viewpoint, conformance occurrence, correspondence claim or relation, allocation record, bridge record, evidence relation, publication relation when publication is current, interface specification, or applicable record kind named by value. | Replace the ambiguous reference with the object that actually carries the claim, or split the sentence into separate objects. |
| **CC-ASV-11 Source return.** | When compression, extraction, coarsening, evidence reuse, publication, or many-to-many allocation hides distinctions, `SourceReturnCondition` is present. | Add one source-return trigger, or narrow the view's admissible use so omitted distinctions are not used for action, assurance, causal use, law-domain review, regulatory review, or reopening. |
| **CC-ASV-12 Architecture-name recovery.** | Every `<X>Architecture` phrase recovers exact selected structure, `<X>StructureKind`, or a declared local relation or claim. | Rewrite the phrase through `ArchitectureStructureKindTriage@Project`; if no relation is being claimed, keep the name as Plain prose and do not let it carry ontology. |
| **CC-ASV-13 Useful action.** | The repair leaves a surviving admissible architecture move: inspect, split, relate, downgrade, generate candidates, state a structural description or view, add correspondence, add source return, use the applicable pattern, or stop. | Restore one move, or classify the phrase as reduced-use cue, quote-only wording, blocked transfer, or incomplete rewrite. |

