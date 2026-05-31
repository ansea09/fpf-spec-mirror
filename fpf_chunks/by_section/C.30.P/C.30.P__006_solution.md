---
chunk_kind: "child"
pattern_id: "C.30.P"
pattern_title: "Architecture and Structure Precision Restoration"
section_id: "C.30.P:4"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/C.30.P/C.30.P__006_solution.md"
commit_sha: "16cd31387cff04ab6b0feef22717f82ac54efa8f"
heading_path:
  - "C.30.P — Architecture and Structure Precision Restoration"
  - "C.30.P:4 — Solution"
line_start: 52005
line_end: 52051
dependencies:
  - "A.10"
  - "A.15"
  - "A.20"
  - "A.21"
  - "A.22"
  - "A.6.F"
  - "A.6.P"
  - "B.3"
  - "C.11"
  - "C.16"
  - "C.16.P"
  - "C.2.P"
  - "C.25"
  - "C.28"
  - "C.29"
  - "C.30"
  - "C.30.ASV"
  - "C.30.ILC"
  - "C.30.LCA"
  - "C.30.TGA-FLOW-REL"
  - "E.10"
  - "E.10.ARCH"
  - "E.17"
  - "E.8"
  - "J.4"
keywords:
---

### C.30.P:4 - Solution

Repair architecture/structure wording by producing an `architecture-structure repair note` or an equivalent local rewrite.

Minimum fields:

```text
ArchitectureOrStructureRepairNote:
  triggerSpan:
  boundedTextSpanOrPublicationUnit:
  encounteredObjectKind:
  candidateLiveObjects:
  selectedLiveObject:
  sourceOrPublicationStack?:
  relationClaimSlice?:
  functionCarrier?:
  structureKindOrArchitectureQuestion?:
  characteristicOrQualityClaimSlice?:
  mathematicalLensClaimSlice?:
  projectSideClaim?:
  exactReceivingPattern:
  repairedWordingOrDemotion:
  admissibleUse:
  nonAdmissibleUse:
  remainingReaderMove:
  disposition:
```

Use the note only when the repair must remain inspectable. A direct local rewrite is enough when one sentence clearly names the live object and exact receiving pattern.

#### C.30.P:4.1 - Recovery sequence

1. **Capture the trigger.** Copy the architecture or structure wording and the sentence that uses it.
2. **Recover the encountered object.** Decide whether the text points to a selected structure, architecture claim, description, view, diagram, graph, model, dashboard, ADR, source document, carrier, publication, function, module/interface, signature, flow, control, score, quality term, evidence, gate, work, decision, release, or ordinary prose.
3. **Recover source/publication first when live.** If the wording relies on a source, publication, view, face, `PublicationUnit`, dashboard, ADR, file, carrier, or source-return relation, apply `C.2.P` for the source/current and publication stack before assigning the architecture or structure claim.
4. **Choose the architecture/structure object.**
   - selected structure -> `A.22`;
   - architecture claim or architecture description -> `C.30`;
   - architecture structural view -> `C.30.ASV`;
   - TGA-flow relation -> `C.30.TGA-FLOW-REL`;
   - control-structure view -> `C.30.LCA`;
   - cross-scope conflict/frustration triage -> `C.30.ILC`;
   - exact C.30 subcase -> that subpattern.
5. **Exit non-architecture claims.** If the sentence uses architecture wording to carry relation, function-like carrier, mathematical lens, characteristic/scale, quality, evidence, assurance, gate, work, decision, causal-use, release, or method force, send that force to the exact pattern and keep this pattern only for the architecture/structure wording repair.
6. **State admissible and non-admissible use.** Say what the reader may do with the repaired wording and what non-admissible adjacent interpretation is blocked.
7. **Return to the subject pattern.** Stop after the exact receiving pattern or ordinary-prose demotion is named.

