---
chunk_kind: "child"
pattern_id: "A.3.2"
pattern_title: "U.MethodDescription: Description Episteme for a Way of Doing"
section_id: "A.3.2:4"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/A.3.2/A.3.2__005_solution.md"
commit_sha: "9208be543f1ede0f53eb24604bf97fd2f121dd24"
heading_path:
  - "A.3.2 — U.MethodDescription: Description Episteme for a Way of Doing"
  - "A.3.2:4 — Solution"
line_start: 8725
line_end: 8844
dependencies:
  - "A.1.1"
  - "A.10"
  - "A.15.1"
  - "A.15.2"
  - "A.2"
  - "A.2.1"
  - "A.2.2"
  - "A.22"
  - "A.3.1"
  - "A.6.1"
  - "A.6.5"
  - "B.1.5"
  - "B.3"
  - "C.2.1"
  - "C.2.P.DR"
  - "C.28"
  - "C.29"
  - "E.10"
  - "E.10.ARCH"
  - "E.24.PUB"
  - "E.24.UK"
  - "F.18"
  - "F.19"
  - "F.6"
  - "F.9"
  - "U.Method"
  - "U.Work"
  - "U.WorkPlan"
keywords:
  - "claim-bearing episteme"
  - "exact U.Method EntityOfConcern"
  - "method-description membership"
  - "representation versus publication versus plan versus Work"
  - "same method versus equivalent descriptions"
  - "substantive way-of-doing claim"
---

### A.3.2:4 - Solution

#### A.3.2:4.1 - Definition

`U.MethodDescription` is a same-individual dependent kind of `U.Episteme`. Membership holds when the already identified episteme has one admitted `U.Method` as its exact `EntityOfConcern` and its claims, interpreted under the effective `U.ReferenceScheme`, make at least one substantive claim about that method as a way of doing. Such a claim may state the method's transformation or enactment concern, generic participant meanings, applicability, precondition, intended effect or preserved condition, bound, or internal method composition. These are claims about method semantics, not planned assignments or actual participation. Naming the method, giving bibliographic metadata, or stating approval alone does not establish membership.

The C.2.1 claim content, exact `EntityOfConcern`, and effective `U.ReferenceScheme` remain the identity discriminators of the episteme; A.3.2 adds no second identity. Whether the claims are detailed, current, or reliable enough for a particular planning, enactment, comparison, audit, revision, publication, or teaching use is a separate evaluation. A new receiving use alone neither creates a new method description nor removes membership.

If someone claims empirical grounding, state the C.2.1 `EpistemeEmpiricalGroundingRelation`. If a proposed use depends on a test, write the tested claim, criterion, evidence path, and result under the evaluation, evidence, or assurance pattern that defines them. Do not add these as method-description fields or let a test change membership.

An assertion or description episteme about one dated Work occurrence may cite `methodDescriptionRef` when its claim depends on that description edition. Recover each performing `U.System` and its obtaining assignment of a local agential system-role kind under A.13. Independently admit the Work under A.15.1, including its obtaining `enactsMethod` relation to the Method. Only when precise assignment-bound attribution is claimed, use F.6 `performedUnderAssignment` with that same obtaining assignment of a separately declared `U.SystemRoleAssignment` species.

#### A.3.2:4.2 - Representation-agnostic stance

Begin with the claim-bearing episteme, then distinguish how its claims are made available:

* a `C.29` representation stands in a declared correspondence to the represented claims;
* an `E.24.PUB` publication form expresses the selected episteme edition for one publication use;
* a `U.PresentationCarrier` bears that publication form.

Only the claim-bearing episteme can meet the membership rule in 4.1; keep its representation, form, carrier, and publication occurrence separate.

The representation may use procedural text, code, a diagram, functional composition, a typed pipeline, a state machine, event rules, constraints, a solver formulation, a proof script, a statistical model, or a combination of notations. Notation choice does not decide membership. Read each assertion separately: use A.6.0 or C.29 when it asserts a formal object, A.6.1 or E.20 when it declares an operation family and laws, A.15.2 when it states intended Work, and A.10 or B.3 when another claim relies on it as evidence or assurance.

#### A.3.2:4.3 - Method-description claim content

The membership threshold is positive but small: at least one claim must answer a method-side question about the way of doing. A name, author, citation, catalogue entry, or approval status does not answer such a question. This threshold distinguishes description from mention; it is not a completeness test for a receiving use.

Name the receiving use before asking whether this method-description edition is adequate for it. A receiving use is not required for `U.MethodDescription` membership. If no use is current, stop at the membership result and make no adequacy claim.

| Proposed use | Where that use belongs | What to check in this edition |
| --- | --- | --- |
| membership only | A.3.2 judges the already identified C.2.1 episteme | no adequacy judgment; do not fabricate a receiver |
| preparing planned work | A.15.2 is the pattern for the `U.WorkPlan`; a gate, authority, or evaluation claim stays with its own pattern | does this edition state the applicability, preconditions, parameters, bounds, and stops that the plan cites? |
| enacting or recording dated work | A.15.1 is the pattern for the Work occurrence; its assertion may cite `methodDescriptionRef` when the edition matters | does this edition state the method claims used by that enactment or record? Actual participants and results still need their own relations. |
| comparing, revising, or auditing claim content | C.2.1 identifies each episteme and any persisted comparison or audit result; the concrete evaluation, evidence, or assurance claim stays with its subject pattern | which method claims are preserved, absent, stale, or incompatible for this comparison or audit? |
| publishing or teaching | C.2.1 is the pattern for the claim-bearing or teaching episteme; E.24.PUB is the pattern for publication occurrence and form; use A.15.1 only for teaching Work that actually happened | does this edition preserve the method distinctions needed by this audience or teaching use? |

A.3.2 creates no universal method-description-use relation. Name the concrete receiving object and the pattern that defines or tests the current claim about it. Comparing claim sets, revising a publication, or checking teaching content does not require a fabricated Work occurrence or decision object.

Then inspect the claim concerns that matter for that named use:

| Claim concern | Question for the named receiving use |
| --- | --- |
| Method described | Which admitted `U.Method` is the episteme's `EntityOfConcern`, and under which effective reference scheme is it identified? |
| Transformation or enactment concern | What way of changing, producing, deciding, learning, or checking does the method organize? |
| Generic participant and boundary meanings | Which kinds of entities, resources, conditions, or interfaces may participate in a future enactment, and what method-side meaning does each have? These are semantic claims, not `RelationSignature` SlotSpecs, `OperationAlgebra` positions, planned fillers, or actual participants. |
| Preconditions | Under which states, guards, invariants, participant conditions, or environmental conditions can the method be used? |
| Intended effects | Which postconditions, intended effects, preserved conditions, and failure semantics are claimed for the method? |
| Bounds | Which latency, precision, cost, safety, reliability, uncertainty, or other local bounds constrain the method? |
| System-role kinds and capabilities | Which local system-role kinds and capability thresholds matter for enactment? |
| Parameters | Which values may vary between work occurrences, over which ranges, and when are they bound? |
| Evaluation conditions | Which criterion compares which concrete Work occurrence, referent, measurement, or result, and which pattern contains the defining content for that comparison? |
| Internal composition | Which admitted methods are parts of one composite method, and what organization constructs that whole? |
| Variation, edition, and refinement | Which claim content is preserved or changed, and is the current claim about another episteme edition, equivalence of claim content, or refinement of the method itself? |
| Edition and publication use | Which episteme edition is relied on, and does its publication use affect currentness or availability? |

Calendars, assignees, work authorization, gate passage, and dated execution witnesses are governed by planning, assignment, gate, or work-occurrence patterns. They may cite a method description.

A `U.MethodDescription` describes one admitted Method. It is not the `RelationSignature` that declares participants for one relation kind, the A.6.1 `OperationAlgebra` content that declares arguments and results for an operation family, the `U.WorkPlan` that states intended work, a dated Work occurrence, or any actual-participation relation of that occurrence.

#### A.3.2:4.4 - Method-description acceptance and use boundaries

A project may accept, regulate, prefer, deprecate, or forbid a method description for one stated use, organization, or policy scope. Record that separate publication, gate, authority, or policy claim under its own pattern. It does not establish `U.MethodDescription` membership.

When a method description is used to prepare or enact work, keep the chain explicit:

1. C.2.1 identifies one episteme through its claim content, exact `EntityOfConcern`, and effective `U.ReferenceScheme`; A.3.2 judges that same episteme to be `U.MethodDescription`. Plainly saying that the method description describes the method is shorthand for this constitution and membership judgment, not another binary relation occurrence.
2. `U.WorkPlan` may cite that episteme when preparing dated work.
3. Recover each performing `U.System` and its obtaining assignment of a local agential system-role kind under A.13. A.15.1 independently admits the dated Work and its `enactsMethod` relation to the Method. If precise assignment-bound attribution is claimed, F.6 `performedUnderAssignment` uses that same obtaining assignment of a separately declared `U.SystemRoleAssignment` species. A separate assertion cites `methodDescriptionRef` only when its claim depends on that edition.
4. The word *result* is only a cue. Ask which claim is being made: an A.6.1 application returned a value, a referent changed under A.3.4, Work produced something under A.15.PROD, or a measurement, evaluation, delivery, or acceptance occurred. If the use needs a Work-to-result relation and no exact predicate is defined for it, keep Work and result separate and state `missing-predicate[work-to-result]`. A log, trace, measurement, or result episteme supports another claim only through its evidence relation.

#### A.3.2:4.5 - Method, mechanism, and formal-substrate boundary

Do not classify by the source word alone. First say in plain words what someone is trying to change, produce, select, derive, control, or maintain and what the sentence asserts about it. Then use `E.10.ARCH:3.1` to separate method, mechanism, formal-object, plan, Work, and result claims; write each claim under its own pattern.

For A.3.2 ask only: is this episteme about one admitted Method, and does at least one claim say how that Method is done? If the same source also asserts a mechanism, formal declaration, work plan, dated Work, evidence use, gate, result, publication, or temporal claim, state that claim separately.

Use these claim checks instead of forcing distinct claims into one generic relation:

* A **method-description membership judgment** identifies one admitted `U.Method` as the episteme's exact `EntityOfConcern` and finds at least one substantive claim about that method as a way of doing.
* A **method claim** states the reusable way of doing, its participant meanings, applicability, conditions, intended result or preserved condition, and bounds.
* A **formal-substrate claim** concerns the selected formal object, structure, invariant, or mathematical declaration used for reasoning.
* A **mechanism-declaration claim** concerns the law-governed operation family, direct subject and range fields, operation algebra, law set, admissibility predicates, and applicability. Transport, audit, realization, evaluation, and evidence-use relations remain separately governed neighboring claims.
* A **work claim** concerns one dated occurrence independently admitted under A.15.1: each performing System with its A.13 core, including an obtaining assignment of a separately declared species, the enacted Method, temporal extent, and containing System. Add F.6 attribution through that same assignment only when precise assignment-bound attribution is asserted. Add participant, resource, or work-to-referent claims only through relations that actually obtain; otherwise return the corresponding missing-governor result.

Connect these claims only through an admitted relation whose predicate and participants are present. If no pattern or declaration defines the needed relation, keep the objects separate rather than inferring dual typing.
Example: a `U.MethodDescription` episteme for a scheduling Method can meet the membership rule while a MILP file represents some of its claims. Another episteme may describe the mathematical formulation; a selector mechanism may declare operations over candidate Methods; a dated solver run is Work; and an issued production-schedule episteme is a separate result. Use that result as evidence only through a current A.10 path and its bounded disposition. Without that path, keep the result available but do not rely on it as evidence for another claim.

#### A.3.2:4.6 - Constructor and process-theory note

In the constructor-theory and process-theory interpretation used here, both informational and physical procedures are understood through possible or impossible transformations. That motivates a broad method-description kind without making software code privileged:

* an episteme about an information-transformation method may be represented through a program, proof script, or solver model;
* an episteme about a material, energetic, organizational, or mixed-transformation method may be represented through a procedure, lab protocol, or control recipe;
* an assertion or description about dated Work may cite a method description. Establish the performing System's A.13 core with its obtaining assignment, then independently admit the Work and its `enactsMethod` relation under A.15.1. Use F.6 `performedUnderAssignment` with that same assignment only for a claimed precise assignment-bound attribution;
* a mechanism may declare law-governed operation structure for transformations, but that mechanism claim is separate from the method-description claim.

This interpretation explains why FPF can treat many representation forms uniformly after the current claim and described method are recovered.

#### A.3.2:4.7 - Declarative representation boundary

Some method descriptions use declarative representations: constraint sets, graph patterns, state predicates, SQL-like queries, policy rules, e-graphs, monoidal diagrams, or process constraints. Do not translate such representations into an imperative route unless the method claim actually states an ordered action structure.

Even a representation that runs or is internally consistent may have more than one sound interpretation. If a comparison depends on variables and their bindings, surrounding context, or an e-graph kept across compiler stages, say what counts as equal. Agreement under one such rule does not by itself show whether the Method is the same, whether the claims are equivalent, or whether one episteme edition continued into another.

Use `C.2.P.DR` when a graph path, evidence path, query plan, predicate, checklist, publication face, or neighboring-pattern relation is treated as an action route by its form or layout alone. Recover the direct object or relation and any separate representation use, then check whether the source actually asserts the proposed order. State a genuine ordered Method or WorkPlan as its own subject assertion with the exact defining or constraining ClaimGraph.

#### A.3.2:4.8 - Composite methods and independent method structures

When claims concern relations among methods, first determine whether the related methods construct one admitted composite `U.Method`.

If admitted methods are actual method parts whose organization constitutes one composite method under `A.3.1` and, when order-sensitive composition is current, `B.1.5`, the composite `U.Method` remains the exact `EntityOfConcern`. A `U.MethodDescription` can make substantive claims about that composite method's internal organization without changing its object of concern to an independently selected structure.

Description nodes, workflow boxes, code blocks, proof-script blocks, diagram paths, and table rows are representation constituents. They do not become method parts by position in the description. A constituent can participate in method-holon composition only after the recovered object is itself an admitted `U.Method`.

If a selected relation structure instead connects several methods as alternatives, substitutes, fallbacks, comparison candidates, or members of a family without constituting one composite method, the selected `U.Structure` is the exact `EntityOfConcern` under `A.22` and C.2.1. The resulting episteme can describe that structure, but the present rule does not classify it as `U.MethodDescription`.

An algebraic, graph, categorical, process-calculus, effect-calculus, matrix, embedding, distributed, or neural representation can be used to express or analyze either case. Its correspondence to claims is governed separately through `C.29`. A work plan, work occurrence, method-family registry, or selector result also keeps its own governed object and subject pattern.

