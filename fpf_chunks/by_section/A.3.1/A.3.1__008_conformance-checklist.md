---
chunk_kind: "child"
pattern_id: "A.3.1"
pattern_title: "U.Method: Context-Defined Way of Doing"
section_id: "A.3.1:7"
section_title: "Conformance Checklist"
source_path: "FPF-Spec.md"
output_path: "by_section/A.3.1/A.3.1__008_conformance-checklist.md"
commit_sha: "60caecb4751fb2a3623a1faaca757d29a19acff9"
heading_path:
  - "A.3.1 — U.Method: Context-Defined Way of Doing"
  - "A.3.1:7 — Conformance Checklist"
line_start: 7182
line_end: 7209
dependencies:
  - "A.1"
  - "A.1.1"
  - "A.10"
  - "A.15.1"
  - "A.15.2"
  - "A.2"
  - "A.2.1"
  - "A.2.2"
  - "A.2.7"
  - "A.22"
  - "A.3"
  - "A.3.2"
  - "A.3.3"
  - "A.6.0"
  - "A.6.1"
  - "A.6.5"
  - "A.6.REL"
  - "B.1.5"
  - "C.2.1"
  - "C.2.P.DR"
  - "C.20"
  - "C.29"
  - "C.36"
  - "C.36.P"
  - "E.18"
  - "E.18.1"
  - "E.20"
  - "F.9"
  - "G.11"
  - "G.5"
  - "U.BoundedContext"
  - "U.Capability"
  - "U.RoleAssignment"
keywords:
---

### A.3.1:7 - Conformance Checklist

**CC-A3.1-1 (Method identity).** `U.Method` is the context-defined semantic way of doing a kind of transformation or enactment. A method claim is not closed by naming a method description, work plan, dated work occurrence, evidence relation, role assignment, capability, mechanism declaration, formal-substrate declaration, publication face, or pattern relation. If one of those claims is also current, state it in its governing pattern and link the governed objects explicitly.

**CC-A3.1-2 (Context anchoring).** Every method identity is interpreted inside a `U.BoundedContext`. Same name across contexts does not prove same method.

**CC-A3.1-3 (Description relation).** A method should have at least one named `U.MethodDescription` when work, assurance, gate, or audit reliance depends on it. Several descriptions may describe the same method only under a stated method-identity relation or criterion.

**CC-A3.1-4 (Assignment-free method).** A method may state role-kind admission conditions or capability-fit conditions. These are method-side admissibility conditions, not deontic obligations by default. The method does not bind named people, teams, organizations, or calendar allocations.

**CC-A3.1-5 (Runtime-free method).** Dated runs are Work individuals admitted under `U.Work`; their performer, temporal, participation, and resource-use facts obtain through exact direct relations. Telemetry, logs, and result records remain separately governed evidence, source, measurement, evaluation, production, delivery, acceptance, or other claim objects; none belongs to method identity by being associated with a run.

**CC-A3.1-6 (Plan-free method).** Work preparation, schedule, go or no-go date, work authorization, and planned work relation belong to `U.WorkPlan`, gate, authority, or commitment patterns.

**CC-A3.1-7 (Mechanism and formal-substrate separation).** A formal substrate, mathematical-lens use, mechanism declaration, mechanism realization, or control model may provide constraints, invariants, or realization facts used when judging a method claim, or may be linked through exact direct relations recovered under `E.10.ARCH:3.1`. It still does not close the method claim unless the current claim states the context-local semantic way of doing and its work-facing identity.

**CC-A3.1-8 (Programming-paradigm neutrality).** Imperative, functional, logical, constraint, object-centric event, effect-handler, and hybrid descriptions are representation choices or description forms until the exact method claim is recovered.

**CC-A3.1-9 (Graph and representation guard).** A graph path, path slice, query, predicate, table, dashboard, publication face, or pattern relation is not a method or work sequence by layout. Use `C.2.P.DR` when representation wording is overread as imperative action.

**CC-A3.1-10 (Method holon, method relation structure, and work composition distinction).** Method-holon composition, method-family selection, fallback, refinement, substitution, iteration, decomposition, and work-occurrence composition remain separate even when they correspond. When submethods are assembled into a whole method, govern the result as `U.Method` with `B.1.5` when order-sensitive composition is current. A step label, step description, order edge, work-plan item, event-log segment, telemetry interval, engine stroke label, detector component, or graph node is not a submethod until it is recovered as a `U.Method` with method-level preconditions, effects, interface or boundary, and whole-method relation. A temporal work part may enact the same whole method during a slice, and an episode may split continuity without changing method identity. When method-side relations are current without whole-method assembly, select a `U.Structure` under `A.22` and designate it `MethodRelationStructure@BoundedContext` for the current use; that designation admits no new durable U-kind, method holon, or closed relation type. Algebraic, graph, categorical, process-calculus, effect-calculus, matrix, embedding, distributed, or neural notation is a lens or representation over the selected method object or structure unless a governing pattern states a different object by value.

**CC-A3.1-11 (Practice wording recovery).** When source wording says `practice`, record the recovered claim kind before accepting a method statement: `U.Method`, method family or method relation structure, `U.MethodDescription`, `U.WorkPlan`, dated Work occurrence admitted under `U.Work`, role assignment or role relation, bounded context, discipline, cultural-evolution case, canon or memory episteme, recognition or selection regime, mediation system, evidence relation, source label, or quote-only wording.

**CC-A3.1-12 (Parameter and variant discipline).** Parameters may be stated as method semantics or described by `U.MethodDescription`. A `U.WorkPlan` may state planned values only against the exact governed declaration current for the plan. An actual value or participant is established only through its exact direct subject relation or A.6.1 operation-application binding; neither method nor description makes it actual. Effects, bounds, admitted participant meanings, and context establish variant identity.

**CC-A3.1-13 (Evidence and assurance boundary).** A method or method description does not by itself prove that work happened, that a result is warranted for the claimed use, that a gate is passed, or that action is authorized. Those claims use the relevant evidence, assurance, gate, temporal, authority, work-plan, or work patterns.

