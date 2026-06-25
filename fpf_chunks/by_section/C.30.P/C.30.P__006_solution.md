---
chunk_kind: "child"
pattern_id: "C.30.P"
pattern_title: "Architecture and Structure Precision Restoration"
section_id: "C.30.P:4"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/C.30.P/C.30.P__006_solution.md"
commit_sha: "6bbbb622859fbbcddc02b23ea76bee4dd71c6291"
heading_path:
  - "C.30.P — Architecture and Structure Precision Restoration"
  - "C.30.P:4 — Solution"
line_start: 55531
line_end: 55579
dependencies:
  - "A.10"
  - "A.15"
  - "A.19.CPM"
  - "A.19.SelectorMechanism"
  - "A.20"
  - "A.21"
  - "A.22"
  - "A.6.F"
  - "A.6.P"
  - "B.3"
  - "C.11"
  - "C.16"
  - "C.16.P"
  - "C.18"
  - "C.19"
  - "C.2.P"
  - "C.25"
  - "C.28"
  - "C.29"
  - "C.30"
  - "C.30.AD"
  - "C.30.ASV"
  - "C.30.ILC"
  - "C.30.LCA"
  - "C.30.TFS-REL"
  - "C.32"
  - "C.32.CONWAY"
  - "C.32.FAIL"
  - "C.32.MLAO"
  - "E.10"
  - "E.10.ARCH"
  - "E.11"
  - "E.17"
  - "E.8"
  - "G.5"
keywords:
---

### C.30.P:4 - Solution

Repair architecture or structure wording by producing an `architecture-structure repair note` or an equivalent local rewrite.

Minimum fields:

```text
ArchitectureOrStructureRepairNote:
  triggerSpan:
  boundedTextSpanOrPublicationUnit:
  encounteredFPFKindOrReference:
  candidateClaimUses:
  selectedClaimUse:
  sourcePublicationRelationSet?:
  relationClaimSlice?:
  functionOrFunctionalityClaim?:
  structureKindOrArchitectureQuestion?:
  characteristicOrQualityClaimSlice?:
  mathLensClaimSlice?:
  projectSideClaim?:
  governingPatternRef:
  repairedWordingOrDemotion:
  admissibleUse:
  nonAdmissibleUse:
  remainingReaderUse:
  disposition:
```

Use the note only when the repair must remain inspectable. A direct local rewrite is enough when one sentence clearly names the selected-structure claim being made, architecture relation, architecture-description use, structural-view use, source-return relation, or governing pattern.

#### C.30.P:4.1 - Recovery sequence

1. **Capture the trigger.** Copy the architecture or structure wording and the sentence that uses it.
2. **Recover the encountered FPF kind or reference.** Decide whether the text points to a selected structure, architecture claim, description, view, diagram, graph, model, dashboard, ADR, source document, carrier, publication, stratification-wording case or source-label case for `C.30.STRAT`, function, module-interface relation, signature, flow, control, score, quality term, evidence, gate, work, decision, release, or ordinary prose.
3. **Recover source-publication relations before architecture assignment.** If the wording relies on a source, publication, view, face, `PublicationUnit`, dashboard, ADR, file, carrier, or source-return relation, apply `C.2.P` for source-use, source-currentness, and publication relations before assigning the architecture or structure claim.
4. **Choose the governing pattern for the architecture or structure use.**
   - selected structure -> `A.22`;
   - `ArchitectureOf@Context`, selected architecture-relevant structure, or thin conditional `ArchitectureDescription@Context` bridge use -> `C.30`;
   - full `ArchitectureDescription@Context` mechanism -> `C.30.AD`;
   - architecture structural view -> `C.30.ASV`;
   - architecture transformation-flow relation -> `C.30.TFS-REL`;
   - control-structure view -> `C.30.LCA`;
   - cross-scope conflict or frustration triage -> `C.30.ILC`;
   - stratification wording or source-label wording such as `layer`, `level`, `tier`, `stack`, `ladder`, `rung`, `block`, `expert`, `cache`, `router`, or `gate` -> `C.30.STRAT` before choosing the final governing pattern;
   - named C.30 subcase -> that subpattern.
5. **Assign non-architecture claims to their governing patterns.** If the sentence uses architecture wording to carry relation, function or functionality, mathematical-lens, characteristic and scale, quality, evidence, assurance, gate, work, decision, causal-use, release, or method claim, apply the governing pattern for that claim and keep this pattern only for the architecture or structure wording repair.
6. **State admissible and non-admissible use.** Say what the reader may do with the repaired wording and what non-admissible adjacent interpretation is blocked.
7. **Stop C.30.P after assignment.** Stop after the governing pattern or ordinary-prose demotion is named.

