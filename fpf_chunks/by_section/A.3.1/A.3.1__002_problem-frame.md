---
chunk_kind: "child"
pattern_id: "A.3.1"
pattern_title: "U.Method: Context-Defined Way of Doing"
section_id: "A.3.1:1"
section_title: "Problem frame"
source_path: "FPF-Spec.md"
output_path: "by_section/A.3.1/A.3.1__002_problem-frame.md"
commit_sha: "02a8b4bac1f141b1751421bf522e9dc489ae522e"
heading_path:
  - "A.3.1 — U.Method: Context-Defined Way of Doing"
  - "A.3.1:1 — Problem frame"
line_start: 6168
line_end: 6189
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
  - "A.3"
  - "A.3.2"
  - "A.3.3"
  - "A.6.0"
  - "A.6.1"
  - "B.1.5"
  - "C.2.P.DR"
  - "C.29"
  - "E.18"
  - "E.18.1"
  - "E.20"
  - "G.5"
  - "U.BoundedContext"
  - "U.Capability"
  - "U.RoleAssignment"
keywords:
  - "abstract process"
  - "how-to"
  - "procedure"
  - "recipe"
---

### A.3.1:1 - Problem frame

Use this pattern when a project needs to say **how something is done in principle** without prematurely treating that method claim as a document, program, workflow diagram, plan, run log, role assignment, capability statement, mechanism claim, or mathematical-model claim before those positions are recovered.

Typical moments:

* a team says "the method is the code", "the process is the BPMN", "the workflow is the evidence", or "the solver model is the operation";
* a procedure, protocol, proof script, optimization model, control strategy, or recipe must be reused across many runs;
* two descriptions look different but may describe the same way of doing;
* a graph, query, table, dashboard, checklist predicate, or mathematical representation is being interpreted as if it were an instruction sequence;
* work planning, dated work, method description, formal substrate, mechanism, and evidence are starting to collapse into one vague "method" word.

**Primary EntityOfConcern.** The `EntityOfConcern` is the `U.Method`: the context-local semantic way of doing a kind of transformation or enactment.

**First useful move.** Name the context-local way of doing, the transformation or enactment it is about, and the `EntityOfConcern` whose state, result, selection, derivation, control relation, or maintained condition changes or is preserved.

**What goes wrong if missed.** A diagram starts authorizing work, a query plan starts looking like performed work, a program starts looking like proof of operational success, or a graph path starts looking like a route that something followed.

**What this buys.** The project can reuse, compare, describe, plan, enact, and audit a way of doing without confusing the method with its descriptions, runs, mechanisms, mathematical substrates, evidence relations, gates, or authority claims.

**Not this pattern when.** If the current claim is a method description, work plan, dated work occurrence, evidence relation, source relation, mechanism declaration, mathematical-lens use, gate decision, authority claim, or publication-use relation, use the pattern that governs that claim and link it back to the `U.Method` only when the relation is current.

