---
chunk_kind: "child"
pattern_id: "C.30.ASV"
pattern_title: "Architecture Structural View Adequacy (ASV)"
section_id: "C.30.ASV:1"
section_title: "Problem frame"
source_path: "FPF-Spec.md"
output_path: "by_section/C.30.ASV/C.30.ASV__002_problem-frame.md"
commit_sha: "504747d26299e3963dc0457bf48d4e2a791d926a"
heading_path:
  - "C.30.ASV — Architecture Structural View Adequacy (ASV)"
  - "C.30.ASV:1 — Problem frame"
line_start: 60237
line_end: 60266
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
  - "E.17"
  - "E.17.0"
  - "E.17.1"
  - "E.17.2"
  - "E.18"
  - "E.24.PUB"
  - "F.18"
  - "G.6"
keywords:
  - "ArchitectureStructureKindRef"
  - "VF.ARCH.STRUCTURE"
  - "architecture structural view"
  - "correspondence"
  - "hidden or lost structure"
  - "source return"
  - "structure kind"
  - "viewpoint bundle"
---

### C.30.ASV:1 - Problem frame

Use this pattern when an architecture discussion needs a view over selected architecture-relevant `U.Structure` refs in an `ArchitectureOf@Context` claim.

The first useful move is `ArchitectureStructureKindTriage@Project`: name the architecture claim or pre-claim described holon and bounded context, the smallest useful `ArchitectureStructureKindRef` set, the selected structure or structure-kind under consideration, and the next admissible architecture move.

```text
ArchitectureStructureKindTriage@Project:
  architectureClaimRef?:
  describedHolonRef?:
  boundedContextRef?:
  candidateStructureKindRefs:
  smallestUsefulStructureKindRefs:
  primaryGoverningPatternApplicationRef:
  admissibleArchitectureMove:
  stopCondition:
```

`@Project` guard: in this triage name, `@Project` marks a project-side use card for first-pass architecture-structure triage. It is not `U.Project`, not a bounded context, not project authority, and not a part-whole relation. If one of those claims is current, use the governing project, context, authority, or part-whole pattern named by value.

Start with `C.30` when the architecture claim itself is unclear. Use C.30.ASV only when a structural view over selected architecture-relevant structure changes the next architecture use. Use a full `ArchitectureStructuralView@Context` only when the view changes action, selected reliance relation, correspondence, source return, publication, comparison, or another governing-pattern use.

What goes wrong if C.30.ASV is missed: one favored diagram, module view, TEVB viewpoint, generated relation graph, control sketch, or neural-network block diagram is treated as the architecture view or proof without naming the selected structure kind, hidden or lost structure, correspondence, and next architecture use.

What C.30.ASV buys in practice: the practitioner can bind selected structure kind to view record, viewpoint, construction mode, selected relations, hidden or lost structure, correspondence, source-return condition, and admissible use before relying on that view.

Not this pattern when the question under repair is only the general architecture claim, structure as such, selected transformation-flow relation, mathematical graph description, transformation-flow path relation, or crossing relation. Use `C.30`, `A.22`, `E.18`, `E.18.2`, `C.29`, or `C.30.TFS-REL` as appropriate. If the view is used for another claim being made, use the governing pattern and keep C.30.ASV only to the view portion.

Thin precision-restoration pointer: if the issue under repair is still whether *view*, *architecture view*, *architecture structural view*, *diagram*, *model*, *graph*, *layer*, or *functional architecture* names a structural view, an architecture description, a publication face, a publication form, a source relation, or another governed claim or relation named by value, use `C.30.P` first. Do not copy the `C.30.P` trigger table here; apply C.30.ASV only after the architecture structural-view claim or non-ASV claim named by value is recoverable.

