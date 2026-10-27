---
chunk_kind: "child"
pattern_id: "C.30.P"
pattern_title: "Clarify Architecture and Structure Wording (Precision Restoration)"
section_id: "C.30.P:4"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/C.30.P/C.30.P__006_solution.md"
commit_sha: "00a27c2889bb2f7b8e0a7669075826e74d4dd270"
heading_path:
  - "C.30.P — Clarify Architecture and Structure Wording (Precision Restoration)"
  - "C.30.P:4 — Solution"
line_start: 71912
line_end: 71960
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
  - "architecture description"
  - "architecture wording"
  - "diagram"
  - "model"
  - "precision restoration"
  - "structural view"
  - "structure wording"
---

### C.30.P:4 - Solution

Repair architecture or structure wording by producing an `architecture-structure repair note` or an equivalent local rewrite.

An optional note can organize the following information; include only what the repair needs:

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
  relationFunctionClaimRef:
  repairedWordingOrDemotion:
  admissibleUse:
  nonAdmissibleUse:
  remainingReaderUse:
  disposition:
```

Use the note only when the repair must remain inspectable. A direct local rewrite is enough when one sentence clearly names the selected-structure claim being made, architecture relation, architecture-description use, structural-view use, source-return relation, or subject pattern.

#### C.30.P:4.1 - Recovery sequence

1. **Read the span.** Read the architecture or structure wording in its sentence and the nearby context needed to recover its meaning. Keep a copy only when the repair needs an inspectable record.
2. **Recover the object and claim.** Identify the subject, predicate, participants and intended use. Distinguish, for example, a selected structure from its description, or an architecture claim from a score or decision. Use the assignment table below for the unresolved kind; keep ordinary prose when no formal distinction changes the claim.
3. **Recover source-publication relations before architecture assignment.** If the wording relies on a source, publication, view, face, `PublicationUnit`, dashboard, ADR, file, carrier, or source-return relation and a source-use, source-currentness, or publication distinction remains hidden, apply `C.2.P` before assigning the architecture or structure claim. If that distinction and its subject pattern are already recoverable, use the subject pattern directly.
4. **Choose the subject pattern for the architecture or structure use.**
   - selected structure -> `A.22`;
   - `ArchitectureRelation`, bounded `ArchitectureClaim`, or its initial description question -> `C.30`;
   - architecture-description identity, correspondence or use -> `C.30.AD`;
   - architecture structural view -> `C.30.ASV`;
   - architecture transformation-flow relation -> `C.30.TFS-REL`;
   - control-structure view -> `C.30.LCA`;
   - cross-scope conflict or frustration triage -> `C.30.ILC`;
   - stratification wording or source-label wording such as `layer`, `level`, `tier`, `stack`, `ladder`, `rung`, `block`, `expert`, `cache`, `router`, or `gate` -> `C.30.STRAT` while the label's technical meaning remains unclear, before choosing the final subject pattern;
   - named C.30 subcase -> that subpattern.
5. **Assign non-architecture claims to their subject patterns.** If the sentence uses architecture wording to carry relation, function or functionality, mathematical-lens, characteristic and scale, quality, evidence, assurance, gate, work, decision, causal-use, release, or method claim, apply the subject pattern for that claim and keep this pattern only for the architecture or structure wording repair.
6. **Preserve the useful conclusion.** State what the repaired wording supports. Add a blocked interpretation only when a plausible reader could take it here and the distinction changes the conclusion or action.
7. **Stop C.30.P after assignment.** Stop after the subject pattern or ordinary-prose demotion is named.

