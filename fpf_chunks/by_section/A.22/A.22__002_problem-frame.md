---
chunk_kind: "child"
pattern_id: "A.22"
pattern_title: "Structure and Structural Views (STRUCT-CAL)"
section_id: "A.22:1"
section_title: "Problem frame"
source_path: "FPF-Spec.md"
output_path: "by_section/A.22/A.22__002_problem-frame.md"
commit_sha: "4ce2f7202e12c5c519a3466f5e07fe0b92e78a44"
heading_path:
  - "A.22 — Structure and Structural Views (STRUCT-CAL)"
  - "A.22:1 — Problem frame"
line_start: 39820
line_end: 39866
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
  - "E.18.NET"
  - "E.24"
  - "E.24.PUB"
  - "F.18"
  - "G.5"
  - "G.6"
keywords:
---

### A.22:1 - Problem frame

Use this pattern when a practitioner needs to select `U.Structure` as the `EntityOfConcern`: an organization among exact constituents and obtaining relations, selected to expose a relation class, applied constraint, invariant, variation class, preserved arrangement, or lost arrangement that changes the next engineering or reasoning action.

First identify the organization selected for the named use. Recover:

1. identify every constituent independently through the content that defines its kind and identity;
2. recover the exact relation occurrences among those constituents that actually obtain under their direct predicates;
3. state the exact constraints applied to those constituents and relations, plus the named selection-use frame that says what question or action this organization serves;
4. name the resulting selected organization and the admissible action or stop that follows.

When the account deliberately asserts dated selection Work, establish its independent grounds under §4.1. Those facts explain the performed selection and remain outside `U.Structure` identity. If the judgment must persist, identify a separate C.2.1 result episteme whose claim content designates the selected structure.

The four values above can be stated in ordinary prose or recovered from an existing description. The following optional aid also keeps use limits and any separately needed claims visible:

```text
StructureQuestionCard@Project:
  named selection use:
  independently identified constituents:
  exact obtaining relation occurrences selected:
  constraints applied:
  selected structure:
  preserved structure:
  lost, hidden, or excluded structure:
  admissible action:
  stop or non-admissible overread: exact stop or return condition
  grounded non-admissible overread, optional:
  selecting system, method, and dated work, only when dated Work is asserted:
  selection-result episteme, when a durable result is needed:
  claim scope or effective reference scheme of that claim, if current:
  reliance relation, if a neighboring reliance claim is being made:
```

`StructureQuestionCard@Project` is a project-side triage aid for this selected-structure use. It is not a new structure kind. Fill the reliance row only when extraction, coarsening, source-description, base-dependence, grounding, evidence, lens, simulation, representation, or action reliance is being claimed; otherwise leave it unused and keep the move on selected structure.

The `@Project` suffix is a local retrieval cue. If the account separately asserts a composite project `U.Work`, identify that Work and how the current selection, decision or description concerns it. The suffix supplies neither identity nor that relation; the same applies to `ArchitectureStructureKindTriage@Project`.

Stop when the selected organization and next use are clear. Develop a neighboring description, view, publication, extraction, comparison or other claim only when the receiving task needs it.

What goes wrong if A.22 is missed: the practitioner reasons from the visible diagram, source publication, source-use record, lens output, generated representation, project record, or architecture description instead of asking which organization is selected and what loss or reliance boundary matters for action.

What A.22 buys in practice: a practitioner can name selected structure, state preserved and lost structure, name source-basis or lens reliance only when it is being claimed, add a `StructureUseReturnCondition` when loss matters, and apply the FPF definition or test for any non-structure claim being made.

Not this pattern when the question under repair is grounded architecture adequacy, architecture structural-view adequacy, or mathematical-lens use. Use `C.30`, `C.30.ASV`, or `C.29` respectively. For any other claim, use the pattern that defines or tests that claim and keep A.22 only to the selected-structure portion.

For unresolved wording: when the wording still may name a structure, a structure description, an architecture description, a view, a publication form, or another exact claim, use `C.30.P` or `C.30.STRAT` first as triggered. Apply A.22 only after the selected-structure claim or structure-view portion is recoverable.

