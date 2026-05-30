---
chunk_kind: "child"
pattern_id: "A.22"
pattern_title: "Structure and Structural Views (STRUCT-CAL)"
section_id: "A.22:1"
section_title: "Problem frame"
source_path: "FPF-Spec.md"
output_path: "by_section/A.22/A.22__002_problem-frame.md"
commit_sha: "2e112078bb209e5e3a511c3bd1aa6b1b2e299efe"
heading_path:
  - "A.22 — Structure and Structural Views (STRUCT-CAL)"
  - "A.22:1 — Problem frame"
line_start: 28501
line_end: 28533
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
  - "C.30.ASV"
  - "C.30.ILC"
  - "C.30.LCA"
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
  - "architecture-description claim"
  - "preserved/lost structure"
  - "selected structure"
  - "source return"
  - "structural description"
  - "structural view"
  - "structure"
---

### A.22:1 - Problem frame

Use this pattern when a practitioner needs to say what organization, relation class, constraint, invariant, variation class, or preserved/lost arrangement is being discussed, without turning a diagram, graph, table, document, mathematical lens, source item, base, evidence path, mathematical-lens output, decision, or architecture description into the structure itself.

The first useful move is small:

```text
StructureQuestionCard@Project:
declared structure substrate:
bounded context:
candidate structure:
relation, operation, constraint, invariant, or variation class:
what is preserved:
what is lost, hidden, or excluded:
source/base/evidence/lens reading, if reliance is live:
admissible use:
non-admissible use:
governingPatternApplicationRefs, if another claim kind is live:
```

`StructureQuestionCard@Project` is a project-side triage aid, not a new structure kind, not a D/S publication, not evidence, and not a decision.

Ordinary minimum: name the bounded context, the candidate structure, one relation, constraint, invariant, or variation class that changes action, one non-admissible overread, and the exact FPF pattern application or stop. Fill preserved or lost structure, source/base/evidence/lens reading and source-return fields only when extraction, coarsening, source/base/evidence/lens reliance, or action reliance is live. All other fields are conditional and may be `not live`.

Stop at this card when it makes the next move clear. Open the heavier records below only when publication, reuse, extraction, coarsening, comparison, evidence, assurance, C.29 lens use, architecture description, or cross-case source/lens reuse is live.


What goes wrong if A.22 is missed: architecture becomes a document, a module diagram, a TGA graph, a mathematical-lens output, or a decision record; a source, lens output, or evidence item becomes the structure; a view becomes the described object; a coarsened or extracted representation becomes loss-free. Those collapses damage first-principles reasoning because the practitioner cannot see what is organized, what carries the claim, which source/base/evidence/lens reading is live, and where the use stops.

What A.22 buys in practice: a practitioner can name selected structure, name the exact source, base, evidence, or lens reading, publish a structural view, state preserved and lost structure, return to source when the loss matters, or name the exact FPF pattern application that carries evidence, assurance, gate, decision, work, release, architecture-description, or mathematical-lens claim kind.

Not this pattern when the live question is architecture-description adequacy. Use `C.30`. If the live question is an architecture structural view, use `C.30.ASV`. If it is mathematical-lens adequacy, use `C.29`. If it is evidence, assurance, gate, decision, work, release, or project authority, use the exact governing FPF pattern and keep A.22 only to the structure carrier or structure-view portion.

