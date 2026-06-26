---
chunk_kind: "child"
pattern_id: "A.22"
pattern_title: "Structure and Structural Views (STRUCT-CAL)"
section_id: "A.22:1"
section_title: "Problem frame"
source_path: "FPF-Spec.md"
output_path: "by_section/A.22/A.22__002_problem-frame.md"
commit_sha: "02a8b4bac1f141b1751421bf522e9dc489ae522e"
heading_path:
  - "A.22 — Structure and Structural Views (STRUCT-CAL)"
  - "A.22:1 — Problem frame"
line_start: 30240
line_end: 30273
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
  - "C.33"
  - "C.34"
  - "C.35"
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

### A.22:1 - Problem frame

Use this pattern when a practitioner needs to select `U.Structure` as the `EntityOfConcern`: the organization, relation class, constraint, invariant, variation class, preserved arrangement, or lost arrangement that changes a next engineering or reasoning action.

The first A.22 question is positive: what is organized, over which bounded context and declared substrate, which relation, constraint, invariant, or variation matters, what is preserved, what is lost or hidden, and which admissible use or stop condition follows.

The first useful move is small:

```text
StructureQuestionCard@Project:
  declared structure substrate:
  bounded context:
  selected structure:
  relation, operation, constraint, invariant, or variation class:
  preserved structure:
  lost, hidden, or excluded structure:
  reliance relation, if being claimed:
  admissible use:
  non-admissible overread:
  governingPatternApplicationRefs, if another claim is being made:
```

`StructureQuestionCard@Project` is a project-side triage aid for this selected-structure use. It is not a new structure kind. Fill the reliance row only when extraction, coarsening, source-description, base-dependence, grounding, evidence, lens, simulation, representation, or action reliance is being claimed; otherwise leave it unused and keep the move on selected structure.

Stop at this card when it makes the next structure use clear. Open heavier records only when a named description, view, publication, extraction, coarsening, comparison, mathematical-lens, architecture-description, or other neighboring claim is being made.

What goes wrong if A.22 is missed: the practitioner reasons from the visible diagram, source, lens output, generated representation, project record, or architecture description instead of asking which organization is selected and what loss or reliance boundary matters for action.

What A.22 buys in practice: a practitioner can name selected structure, state preserved and lost structure, name source or lens reliance only when it is being claimed, add a `SourceReturnCondition` when loss matters, and apply the FPF pattern that governs any non-structure claim being made.

Not this pattern when the question under repair is grounded architecture adequacy, architecture structural-view adequacy, or mathematical-lens use. Use `C.30`, `C.30.ASV`, or `C.29` respectively. For any other claim being made, use the governing FPF pattern and keep A.22 only to the selected-structure portion.

Thin precision-restoration pointer: when the wording still may name a structure, a structure description, an architecture description, a view, a publication form, or another governed claim, use `C.30.P` or `C.30.STRAT` first as triggered. Apply A.22 only after the selected-structure claim or structure-view portion is recoverable.

