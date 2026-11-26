---
chunk_kind: "child"
pattern_id: "A.22"
pattern_title: "Structure and Structural Views"
section_id: "A.22:1"
section_title: "Problem frame"
source_path: "FPF-Spec.md"
output_path: "by_section/A.22/A.22__002_problem-frame.md"
commit_sha: "9d38fbfe4ce5b72d8fe05e839cbca0025a5b31cf"
heading_path:
  - "A.22 — Structure and Structural Views"
  - "A.22:1 — Problem frame"
line_start: 41841
line_end: 41889
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

Use this pattern to choose which organization of constituents and relations someone needs to understand a situation, make a decision or design an arrangement. When that organization is claimed as a `U.Structure`, it can be the `EntityOfConcern` in its own right. Its constituents and selected relation occurrences must have independent grounds.

Start from the use that calls for a structural account. Which change of arrangement could change the recipient’s action or the reason for it?

1. Identify the subject and the relations on which the recipient’s decision depends. Two independent organizations can authorize a handover through a relation between them. When composition matters, trace a part to the whole whose use it affects, or trace a whole result to the parts whose arrangement can change it. Another System may use a part's output without containing that part. Where several kinds matter, distinguish, for example, the operations of a Method from the performers or performances it calls for.
2. Choose the relations and constraints that account for that difference. Does the answer depend on a property of each participant, on what one supplies to another or on a condition they must meet together? Identify the participants in each selected relation. Establish each claimed occurrence under its own predicate, including any membership in a whole used in the argument.
3. At the scales the question uses, decide what the description must distinguish. Try an allowed change of arrangement that leaves the proposed description the same. If it changes the required action or its justification, retain the distinction or find a sufficient premise for the original question.
4. State the selection-use frame, the constraints applied, the selected organization and the conclusion it warrants. A design can describe how proposed relations would meet the requirement. Establish that they obtain before using them as the actual structure of an installation.

When the account asserts dated selection Work, establish its independent grounds under §4.1. Those facts explain the performed selection and remain outside `U.Structure` identity. If the judgment must persist, identify a separate C.2.1 result episteme whose claim content designates the selected structure.

The four identity discriminators in §4.1 can be stated in ordinary prose or recovered from an existing description. The following optional aid also keeps use limits and any separately needed claims visible:

```text
StructureQuestionCard@Project:
  named selection use:
  independently identified constituents:
  obtaining relation occurrences selected:
  constraints applied:
  selected structure:
  preserved structure:
  lost, hidden, or excluded structure:
  admissible action:
  stop or non-admissible overread: stop or return condition
  grounded non-admissible overread, optional:
  selecting participant and grounds, when the claim concerns who chose the arrangement:
  selection Method, when the way of choosing matters:
  dated selection Work and its grounds, when that occurrence is asserted:
  selection-result episteme, when a durable result is needed:
  claim scope or effective reference scheme of that claim, if current:
  reliance relation, if a neighboring reliance claim is being made:
```

`StructureQuestionCard@Project` is a project-side triage aid for this selected-structure use. It is not a new structure kind. Fill the reliance row only when extraction, coarsening, source-description, base-dependence, grounding, evidence, lens, simulation, representation, or action reliance is being claimed; otherwise leave it unused and keep the move on selected structure.

The `@Project` suffix is a local retrieval cue. If the account separately asserts a composite project `U.Work`, identify that Work and how the current selection, decision or description concerns it. The suffix supplies neither identity nor that relation; the same applies to `ArchitectureStructureKindTriage@Project`.

Stop when the selected organization and next use are clear. Develop a neighboring description, view, publication, extraction, comparison or other claim only when the receiving task needs it.

What goes wrong if A.22 is missed: the practitioner reasons from the visible diagram, source publication, source-use record, lens output, generated representation, project record, or architecture description instead of asking which organization is selected and what loss or reliance boundary matters for action.

A practitioner can choose the relations an action depends on, explain which arrangements can be treated alike for that action and identify the resulting structure. Use a `StructureUseReturnCondition` when a later decision needs a distinction left out of its description.

Not this pattern when the question under repair is grounded architecture adequacy, architecture structural-view adequacy, or mathematical-lens use. Use `C.30`, `C.30.ASV`, or `C.29` respectively. For any other claim, use the pattern that defines or tests that claim and keep A.22 only to the selected-structure portion.

For unresolved wording: when the wording still may name a structure, a structure description, an architecture description, a view, a publication form, or another claim, use `C.30.P` or `C.30.STRAT` first as triggered. Apply A.22 only after the selected-structure claim or structure-view portion is recoverable.

