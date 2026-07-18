---
chunk_kind: "child"
pattern_id: "A.3.1"
pattern_title: "U.Method: Context-Defined Way of Doing"
section_id: "A.3.1:1"
section_title: "Problem frame"
source_path: "FPF-Spec.md"
output_path: "by_section/A.3.1/A.3.1__002_problem-frame.md"
commit_sha: "1d5c1edd154b636a446b3887a6094be60c60faff"
heading_path:
  - "A.3.1 — U.Method: Context-Defined Way of Doing"
  - "A.3.1:1 — Problem frame"
line_start: 6325
line_end: 6346
dependencies:
  - "A.1"
  - "A.1.1"
  - "A.10"
  - "A.15"
  - "A.15.1"
  - "A.15.2"
  - "A.2"
  - "A.2.1"
  - "A.2.2"
  - "A.2.7"
  - "A.3"
  - "A.3.2"
  - "A.3.3"
  - "A.6.0"
  - "A.6.1"
  - "B.1.5"
  - "C.2.P.DR"
  - "C.20"
  - "C.29"
  - "C.36"
  - "C.36.P"
  - "E.18"
  - "E.18.1"
  - "E.20"
  - "G.11"
  - "G.5"
  - "U.BoundedContext"
  - "U.Capability"
  - "U.RoleAssignment"
keywords:
  - "method"
  - "method composition"
  - "method vs method description vs work"
  - "non-agentive holon"
  - "submethod"
  - "way of doing"
---

### A.3.1:1 - Problem frame

Use this pattern when a project needs to say **how something is done in principle** without prematurely treating that method or practice claim as a document, program, workflow diagram, plan, run log, role assignment, capability statement, mechanism claim, cultural tradition, discipline position, or mathematical-model claim before those positions are recovered.

Typical moments:

* a team says "the method is the code", "the process is the BPMN", "the workflow is the evidence", or "the solver model is the operation";
* a practice, procedure, protocol, proof script, optimization model, control strategy, or recipe is intended for reuse across many runs;
* two descriptions look different but may describe the same way of doing;
* a graph, query, table, dashboard, checklist predicate, or mathematical representation is being interpreted as if it were an instruction sequence;
* work planning, dated work, method description, formal substrate, mechanism, role assignment, cultural-evolution, discipline, and evidence are starting to collapse into one vague "method" or "practice" word.

**Primary EntityOfConcern.** The `EntityOfConcern` is the `U.Method`: the context-local semantic way of doing a kind of transformation or enactment. `U.Method` is a non-agentive holon kind: methods can have submethods, compose into whole methods, and participate as submethods of larger methods. This does not make a method an actor, a method description, a work plan, or a dated work occurrence. A step label or step description is not a method part unless the recovered object is itself a `U.Method`.

**First useful move.** Name the context-local way of doing, the transformation or enactment it is about, and the `transformedEntityOrStructure` from `A.3.4`: the governed object or structure whose state, result, selection, derivation, control relation, or maintained condition changes or is preserved. The method remains this pattern's primary `EntityOfConcern`.

**What goes wrong if missed.** A diagram starts authorizing work, a query plan starts looking like performed work, a program starts looking like proof of operational success, or a graph path starts looking like a route that something followed.

**What this buys.** The project can reuse, compare, describe, plan, enact, and audit a way of doing without confusing the method with its descriptions, runs, mechanisms, mathematical substrates, evidence relations, gates, or authority claims.

**Not this pattern when.** If the current claim is a method description, work plan, dated work occurrence, evidence relation, source relation, mechanism declaration, mathematical-lens use, gate decision, authority claim, or publication-use relation, use the pattern that governs that claim and link it back to the `U.Method` only when the relation is current.

