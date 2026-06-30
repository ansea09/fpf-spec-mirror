---
chunk_kind: "child"
pattern_id: "A.3.1"
pattern_title: "U.Method: Context-Defined Way of Doing"
section_id: "A.3.1:7"
section_title: "Conformance Checklist"
source_path: "FPF-Spec.md"
output_path: "by_section/A.3.1/A.3.1__008_conformance-checklist.md"
commit_sha: "c859eed90b5ca9d0f717a1ffb13a841a3b52c016"
heading_path:
  - "A.3.1 — U.Method: Context-Defined Way of Doing"
  - "A.3.1:7 — Conformance Checklist"
line_start: 6442
line_end: 6467
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

### A.3.1:7 - Conformance Checklist

**CC-A3.1-1 (Method slot).** `U.Method` is the context-defined semantic way of doing a kind of transformation or enactment. A method claim is not closed by naming a method description, work plan, dated work occurrence, evidence relation, role assignment, capability, mechanism declaration, formal-substrate declaration, publication face, or pattern relation. If one of those claims is also current, state it in its governing pattern and link the positions explicitly.

**CC-A3.1-2 (Context anchoring).** Every method identity is interpreted inside a `U.BoundedContext`. Same name across contexts does not prove same method.

**CC-A3.1-3 (Description relation).** A method should have at least one named `U.MethodDescription` when work, assurance, gate, or audit reliance depends on it. Several descriptions may describe the same method only under a stated method-identity relation or criterion.

**CC-A3.1-4 (Assignment-free method).** A method may state role-kind requirements or capability requirements. It does not bind named people, teams, organizations, or calendar slots.

**CC-A3.1-5 (Runtime-free method).** Dated runs, timestamps, telemetry, logs, and work-result records belong to `U.Work` and associated evidence patterns or source patterns, not to the method identity.

**CC-A3.1-6 (Plan-free method).** Work preparation, schedule, go or no-go date, work authorization, and planned work relation belong to `U.WorkPlan`, gate, authority, or commitment patterns.

**CC-A3.1-7 (Mechanism and formal-substrate separation).** A formal substrate, mathematical-lens use, mechanism declaration, mechanism realization, or control model may provide constraints, invariants, or realization facts used when judging a method claim, or may be linked by typed relation-position claims under `E.10.ARCH:3.1`. It still does not close the method claim unless the current claim states the context-local semantic way of doing and its work-facing identity.

**CC-A3.1-8 (Programming-paradigm neutrality).** Imperative, functional, logical, constraint, object-centric event, effect-handler, and hybrid descriptions are representation choices or description forms until the method slot is recovered.

**CC-A3.1-9 (Graph and representation guard).** A graph path, path slice, query, predicate, table, dashboard, publication face, or pattern relation is not a method or work sequence by layout. Use `C.2.P.DR` when representation wording is overread as imperative action.

**CC-A3.1-10 (Method relation structure and work composition distinction).** Method composition, method-family selection, fallback, refinement, substitution, iteration, decomposition, and work-occurrence composition must stay separate even when they correspond. When method-side relations are current, recover `MethodRelationStructure@BoundedContext`; algebraic, graph, categorical, process-calculus, effect-calculus, matrix, embedding, distributed, or neural notation is a lens or representation over that structure unless a governing pattern states a different object by value.

**CC-A3.1-11 (Parameter and variant discipline).** Parameters may be declared at method or method-description level; concrete values are bound in work planning or work occurrence. Variant identity must be justified by effects, bounds, accepted inputs, and context.

**CC-A3.1-12 (Evidence and assurance boundary).** A method or method description does not by itself prove that work happened, that a result is warranted for the claimed use, that a gate is passed, or that action is authorized. Those claims use the relevant evidence, assurance, gate, temporal, authority, work-plan, or work patterns.

