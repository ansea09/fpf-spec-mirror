---
chunk_kind: "child"
pattern_id: "C.30.ASV"
pattern_title: "Architecture Structural View Adequacy (ASV)"
section_id: "C.30.ASV:1"
section_title: "Problem frame"
source_path: "FPF-Spec.md"
output_path: "by_section/C.30.ASV/C.30.ASV__002_problem-frame.md"
commit_sha: "8bb4989c9be7fa4b33f0bb7537e4611676ee3087"
heading_path:
  - "C.30.ASV — Architecture Structural View Adequacy (ASV)"
  - "C.30.ASV:1 — Problem frame"
line_start: 60274
line_end: 60314
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

### C.30.ASV:1 - Problem frame

Use this pattern when you have a structural description of one selected architecture-relevant `U.Structure` and need to decide whether that same description is also a `U.View` under one exact viewpoint.

The first useful move is small. In ordinary prose, name the described holon or actual `ArchitectureRelation` when known, the selected structure, the smallest useful structure-kind set, any qualifier that changes interpretation, and the next architecture move. If one or two sentences make those values clear, stop.

For example: “The failover diagram describes runtime-interaction and control structures, but it hides the actual failover relation. Recover that relation before relying on the diagram as a view.” This is already a usable triage result. Use `ArchitectureStructureKindTriage@Project` only when the result must be retained, compared, or handed on.

```text
ArchitectureStructureKindTriage@Project:
  projectWorkOccurrenceRef?: U.EntityRef constrained to U.Work
  architectureStructuralViewProjectUseRelationRef?: U.RelationRef, only when a named pattern defines this project-use relation and the occurrence obtains
  architectureClaimRef?: U.EpistemeRef constrained to ArchitectureClaim
  architectureRelationOccurrenceRef?: ArchitectureRelationRef
  describedHolonRef?: U.HolonRef
  candidateViewEpistemeRef?: U.EpistemeRef
  exactViewpointRef?: U.ViewpointRef
  viewpointConformanceRelationRef?: EpistemeViewpointConformanceRelationRef
  claimScope?: U.ClaimScope, byValue
  effectiveReferenceScheme?: U.ReferenceScheme, byValue
  modelUseStructureRef?: U.StructureRef
  candidateStructureKindRefs: FinSet(ArchitectureStructureKindRef)
  smallestUsefulStructureKindRefs: FinSet(ArchitectureStructureKindRef)
  selectedStructureRefs?: FinSet(U.StructureRef)
  claimPatternRefs?: FinSet(PatternRef), if another claim is being made
  admissibleArchitectureMove:
  stopCondition:
```

`@Project` is a compatibility and retrieval cue for a project-side use record. It supplies no project identity, authority, context, viewpoint, parthood, or Work occurrence. When one actual project matters to this triage, `projectWorkOccurrenceRef` identifies the composite `U.Work` recovered under `A.15.6`. Include `architectureStructuralViewProjectUseRelationRef` only when a named pattern defines the relation by which this use concerns that Work and an occurrence of the relation obtains. A Work reference alone does not establish project locality. If locality matters but that relation is not yet defined, use A.6.RCD before filling the field; otherwise omit both project-local fields. `claimPatternRefs` points only to patterns that define or test separate claims; it does not identify a pattern-application occurrence.

Start with `C.30` when the actual architecture relation, exact selected structure, or architecture claim is unclear. Use C.30.ASV only when a structural description over selected architecture-relevant structure changes the next architecture use. Use the full `ArchitectureStructuralView` record only when one exact description episteme passes E.17.0 conformance to an exact viewpoint and the view changes action, selected reliance relation, correspondence, source return, publication, comparison, or another non-ASV claim or use.

What goes wrong if C.30.ASV is missed: one favored diagram, module view, TEVB viewpoint, generated relation graph, control sketch, or neural-network block diagram is treated as the architecture, selected structure, `U.View`, or proof without naming the exact description episteme, selected structure kind, viewpoint-conformance occurrence, hidden or lost structure, correspondence, and next architecture use.

What C.30.ASV buys in practice: the practitioner can distinguish description identity, selected structure and structure kind, exact viewpoint conformance, representation, and publication before relying on a view. Construction history, hidden or lost structure, correspondence, source return, and admissible use remain separately inspectable.

Do not use C.30.ASV when the question is only about a general architecture claim, subject-side `ArchitectureRelation`, structure as such, selected transformation-flow relation, mathematical graph description, transformation-flow path relation, or crossing relation. Use `C.30`, `A.22`, `E.18`, `E.18.2`, `C.29`, or `C.30.TFS-REL` as appropriate. If the view is used for another claim, use the applicable pattern for that claim and keep C.30.ASV only for the view portion.

Thin precision-restoration pointer: if the issue under repair is still whether *view*, *architecture view*, *architecture structural view*, *diagram*, *model*, *graph*, *layer*, or *functional architecture* names a structural description, a `U.View`, an architecture description, a representation, a publication occurrence, a publication form, a source relation, or another claim or relation named by value, use `C.30.P` first. Do not copy the `C.30.P` trigger table here; apply C.30.ASV only after the architecture structural-view claim or non-ASV claim named by value is recoverable.

