---
chunk_kind: "child"
pattern_id: "A.22"
pattern_title: "Structure and Structural Views (STRUCT-CAL)"
section_id: "A.22:1"
section_title: "Problem frame"
source_path: "FPF-Spec.md"
output_path: "by_section/A.22/A.22__002_problem-frame.md"
commit_sha: "eaafd3a43b9173706e1f8388a3bc94c6445397e4"
heading_path:
  - "A.22 — Structure and Structural Views (STRUCT-CAL)"
  - "A.22:1 — Problem frame"
line_start: 28039
line_end: 28072
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
  - "C.30.TGA-FLOW-REL"
  - "E.10"
  - "E.10.D2"
  - "E.17"
  - "E.17.0"
  - "E.17.1"
  - "E.18"
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

Use this pattern when a practitioner needs to select structure as an `EntityOfConcern`: the organization, relation class, constraint, invariant, variation class, preserved arrangement, or lost arrangement that changes a next engineering or reasoning move.

The first A.22 question is positive: what is organized, over which bounded context and substrate, what relation or constraint matters, what is preserved, what is lost, and what use or stop condition follows. Diagrams, graphs, documents, source items, mathematical-lens outputs, project records, and architecture descriptions may help expose that structure; they do not replace the selected structure.
The first useful move is small:

```text
StructureQuestionCard@Project:
declared structure substrate:
bounded context:
candidate structure:
relation, operation, constraint, invariant, or variation class:
what is preserved:
what is lost, hidden, or excluded:
reliance relation, if live: source-description, base-dependence, grounding, evidence, lens, simulation, extraction, or representation
admissible use:
non-admissible use:
governingPatternApplicationRefs, if another claim kind is live:
```

`StructureQuestionCard@Project` is a project-side triage aid for this selected-structure move. It is not a new structure kind; evidence, gate, decision, work, release, publication, source-use, or description-use claims exit to the exact neighboring FPF pattern when they become live.

Ordinary minimum: name the bounded context, the candidate structure, one relation, constraint, invariant, or variation class that changes action, one non-admissible overread, and the exact FPF pattern application or stop. Fill preserved or lost structure, reliance-relation, and source-return fields only when extraction, coarsening, source-description, base-dependence, grounding, evidence, lens, simulation, representation, or action reliance is live. All other fields are conditional and may be `not live`.

Stop at this card when it makes the next structure move clear. Open heavier records only when a named publication, reuse, extraction, coarsening, comparison, lens, architecture-description, or other neighboring claim is live.

What goes wrong if A.22 is missed: architecture becomes a document, a module diagram, a TGA graph, a mathematical-lens output, or a project record; a source, lens output, or view becomes the structure; a coarsened or extracted representation becomes loss-free. Those collapses damage first-principles reasoning because the practitioner cannot see what is organized, what carries the claim, which reliance relation is live, and where the use stops.

What A.22 buys in practice: a practitioner can name selected structure, state preserved and lost structure, name source or lens reliance when it is live, return to source when the loss matters, and send any non-structure claim to the exact FPF pattern that carries it.

Not this pattern when the live question is grounded architecture adequacy, architecture structural-view adequacy, or mathematical-lens use. Use `C.30`, `C.30.ASV`, or `C.29` respectively. For any other live claim, use the exact governing FPF pattern and keep A.22 only to the selected-structure portion.

Thin precision-restoration pointer: if the live issue is still whether wording such as *architecture*, *structure*, *diagram*, *module*, *model*, *view*, *functional architecture*, or a source label such as *layer*, *level*, *tier*, *stack*, *block*, *expert*, *cache*, *router*, or *gate* names a structure, a structure description, an architecture description, a view, a carrier, or another exact receiving-pattern exit, use `C.30.P` and `C.30.STRAT` as triggered before applying A.22. Do not copy either trigger table here; A.22 resumes only after the selected-structure claim or structure-view portion is recoverable.
