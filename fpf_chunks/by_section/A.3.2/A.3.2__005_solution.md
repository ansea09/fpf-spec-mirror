---
chunk_kind: "child"
pattern_id: "A.3.2"
pattern_title: "U.MethodDescription: Description Episteme for a Way of Doing"
section_id: "A.3.2:4"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/A.3.2/A.3.2__005_solution.md"
commit_sha: "3bc659a6f866071f629bf41fc2dd41f2518e579a"
heading_path:
  - "A.3.2 — U.MethodDescription: Description Episteme for a Way of Doing"
  - "A.3.2:4 — Solution"
line_start: 7115
line_end: 7220
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

The C.2.1 claim content, exact `EntityOfConcern`, and effective `U.ReferenceScheme` remain the identity discriminators of the episteme; A.3.2 adds no second identity. Whether the claims are detailed, current, or reliable enough for a particular planning, enactment, comparison, audit, or review use is a separate evaluation. A new receiving use alone neither creates a new method description nor removes membership.

Empirical grounding, when current, uses the exact C.2.1 `EpistemeEmpiricalGroundingRelation`. Formal or empirical testing and receiving-use evaluation use the separately governed evaluation, evidence, or assurance relations required by that use. Neither grounding nor testing is an intrinsic method-description field or an identity or membership condition.

The assertion or description episteme about an exact dated Work occurrence admitted under `U.Work` may cite the method description through `methodDescriptionRef` when its receiving claim depends on that edition. The independently obtaining `performedBy` and `enactsMethod` relations involving that Work individual connect it to the exact performer assignment and enacted method. The description itself neither performs work nor is enacted.

#### A.3.2:4.2 - Representation-agnostic stance

Begin with the claim-bearing episteme, then distinguish how its claims are made available:

* a `C.29` representation stands in a declared correspondence to the represented claims;
* an `E.24.PUB` publication form expresses the selected episteme edition for one publication use;
* a `U.PresentationCarrier` bears that publication form.

These are different objects and relations. None becomes `U.MethodDescription` by appearance. Only the claim-bearing episteme, not its representation, form, carrier, or publication occurrence, can meet the membership rule in 4.1.

The representation may use procedural text, code, a diagram, functional composition, a typed pipeline, a state machine, event rules, constraints, a solver formulation, a proof script, a statistical model, or a combination of notations. Notation choice does not decide membership. The same representation may also correspond to claims about a formal substrate, mechanism, work plan, or evidence; recover each current claim and governed object separately.

#### A.3.2:4.3 - Method-description claim content

The membership threshold is positive but small: at least one claim must answer a method-side question about the way of doing. A name, author, citation, catalogue entry, or approval status does not answer such a question. This threshold distinguishes description from mention; it is not a completeness test for a receiving use.

For the work or decision that will rely on the episteme, inspect the claim concerns that matter there:

| Claim concern | Question for the current work or decision |
| --- | --- |
| Method described | Which admitted `U.Method` is the exact `EntityOfConcern`, and under which effective reference scheme is it identified? |
| Transformation or enactment concern | What way of changing, producing, deciding, learning, or checking does the method organize? |
| Generic participant and boundary meanings | Which kinds of entities, resources, conditions, or interfaces may participate in a future enactment, and what method-side meaning does each have? These are semantic claims, not `RelationSignature` SlotSpecs, `OperationAlgebra` positions, planned fillers, or actual participants. |
| Preconditions | Under which states, guards, invariants, participant conditions, or environmental conditions can the method be used? |
| Intended effects | Which postconditions, intended effects, preserved conditions, and failure semantics are claimed for the method, without asserting an actual result? |
| Bounds | Which latency, precision, cost, safety, reliability, uncertainty, or other local bounds constrain the method? |
| Roles and capabilities | Which role kinds and capability thresholds matter for enactment? |
| Parameters | Which values may vary between work occurrences, over which ranges, and when are they bound? |
| Evaluation conditions | Which separately governed criteria or comparators would evaluate a work occurrence, affected referent, measurement, evaluation result, or other direct object for the receiving use? |
| Internal composition | Which admitted methods are parts of one composite method, and what organization constructs that whole? |
| Variation, edition, and refinement | Which claim content is preserved or changed, and is the current claim about another episteme edition, equivalence of claim content, or refinement of the method itself? |
| Edition and publication use | Which episteme edition is relied on, and does its publication use affect currentness or availability? |

Calendars, assignees, work authorization, gate passage, and dated execution witnesses are governed by planning, assignment, gate, or work-occurrence patterns. They may cite a method description but do not become its claim content merely because they appear beside it.

A `U.MethodDescription` describes one exact method. It is not the `RelationSignature` that declares participant SlotSpecs for one admitted direct relation kind, not the A.6.1 `OperationAlgebra` content that declares typed arguments and results for one operation family, not the `U.WorkPlan` that states particular intended work, and not a dated Work occurrence admitted under `U.Work` or any of that occurrence's actual participant relations.

#### A.3.2:4.4 - Method-description acceptance and use boundaries

A method description may be accepted, regulated, preferred, deprecated, or forbidden in a bounded context. That is a separate publication, gate, authority, or policy claim. Such a claim neither establishes membership nor turns the description into work, evidence, a gate decision, or a mechanism.

When a method description is used to prepare or enact work, keep the chain explicit:

1. C.2.1 identifies one episteme through its claim content, exact `EntityOfConcern`, and effective `U.ReferenceScheme`; A.3.2 judges that same episteme to be `U.MethodDescription`. Plainly saying that the method description describes the method is shorthand for this constitution and membership judgment, not another binary relation occurrence.
2. `U.WorkPlan` may cite that episteme when preparing dated work.
3. Independently obtaining `performedBy -> U.RoleAssignment` and actual `enactsMethod -> U.Method` relations involve the exact dated Work occurrence admitted under `U.Work`, not the method description; a separate assertion cites `methodDescriptionRef` only when the receiving claim depends on that description edition.
4. A boundary word such as *result* does not select one work-result relation. Recover the exact affected entity, actual change, A.6.1 operation-result binding, local A.15.PROD production-work, entity-identity-inception, or production-completion claim, measurement or evaluation result, delivery, acceptance, or other direct relation current for the use. Result, log, trace, and measurement epistemes participate in evidence or assurance only through their governing relations.

#### A.3.2:4.5 - Method, mechanism, and formal-substrate boundary

Do not decide method, mechanism, or formal substrate by the source word alone. When a source expression or project concern appears to name changing, producing, selecting, deriving, controlling, or maintaining an `EntityOfConcern`, use `E.10.ARCH:3.1` to recover the project concern first and then assign separately governed typed FPF values.

For this host, keep the local question thin: does this already identified `U.Episteme` describe the exact `U.Method` named as its EntityOfConcern? If the same source expression or project concern also raises mechanism, formal-substrate, work-plan, dated-work, evidence, source-use, gate, result, publication, or temporal claims, identify those governed objects and direct relations separately and apply their own patterns.

Use these claim checks instead of forcing distinct claims into one generic relation:

* A **method-description membership judgment** identifies one admitted `U.Method` as the episteme's exact `EntityOfConcern` and finds at least one substantive claim about that method as a way of doing.
* A **method claim** concerns the context-defined semantic way of doing.
* A **formal-substrate claim** concerns the selected formal object, structure, invariant, or mathematical declaration used for reasoning.
* A **mechanism-declaration claim** concerns the law-governed operation family, direct subject and range fields, operation algebra, law set, admissibility predicates, and applicability. Transport, audit, realization, evaluation, and evidence-use relations remain separately governed neighboring claims.
* A **work claim** concerns a dated occurrence with its performer assignment, enacted method, temporal extent, resources, affected referent, and separately governed actual participant relations; witnesses and results retain their own direct governors.

Connect these claims only through the exact direct relations their governing patterns admit. Do not infer that one individual instantiates both `U.Method` and `U.Mechanism`, or that a method description is work, merely because one expression supports several claims.
Example: a scheduling-method episteme can meet the membership rule while a MILP file represents some of its claims. A separately identified episteme can make claims about the mathematical formulation as a formal substrate; a selector mechanism can declare admissible selection operations over candidate methods; a scheduled solver run is work; an issued production-schedule episteme remains a separately governed result and can support another claim only through an exact evidence-use relation. Those claims may be linked, but one does not close the others.

#### A.3.2:4.6 - Constructor and process-theory note

In the constructor-theory and process-theory interpretation used here, both informational and physical procedures are understood through possible or impossible transformations. That motivates a broad method-description kind without making software code privileged:

* an episteme about an information-transformation method may be represented through a program, proof script, or solver model;
* an episteme about a material, energetic, organizational, or mixed-transformation method may be represented through a procedure, lab protocol, or control recipe;
* an assertion or description about an exact dated Work occurrence admitted under `U.Work` may cite a method description, while the independently obtaining `performedBy` and `enactsMethod` relations involving that Work individual identify the performer assignment and enacted method; no actor or `TransformerRole` follows from the description;
* a mechanism may declare law-governed operation structure for transformations, but that mechanism claim is separate from the method-description claim.

This note is not a license to call every algorithm-looking expression a method description. It only explains why FPF can treat many representation forms uniformly after the current claim and described method are recovered.

#### A.3.2:4.7 - Declarative representation boundary

Some method descriptions use declarative representations: constraint sets, graph patterns, state predicates, SQL-like queries, policy rules, e-graphs, monoidal diagrams, or process constraints. Do not translate such representations into an imperative route unless the method claim actually states an ordered action structure.

If the source turns a graph path, evidence path, query plan, predicate, checklist, publication face, or pattern relation into a route, dispatch, call sequence, work-control sequence, or work workflow by metaphor, apply `C.2.P.DR` before assigning the direct governing pattern.

#### A.3.2:4.8 - Composite methods and independent method structures

When claims concern relations among methods, first determine whether the related methods construct one admitted composite `U.Method`.

If admitted methods are actual method parts whose organization constitutes one composite method under `A.3.1` and, when order-sensitive composition is current, `B.1.5`, the composite `U.Method` remains the exact `EntityOfConcern`. A `U.MethodDescription` can make substantive claims about that composite method's internal organization without changing its object of concern to an independently selected structure.

Description nodes, workflow boxes, code blocks, proof-script blocks, diagram paths, and table rows are representation constituents. They do not become method parts by position in the description. A constituent can participate in method-holon composition only after the recovered object is itself an admitted `U.Method`.

If a selected relation structure instead connects several methods as alternatives, substitutes, fallbacks, comparison candidates, or members of a family without constituting one composite method, the selected `U.Structure` is the exact `EntityOfConcern` under `A.22` and C.2.1. The resulting episteme can describe that structure, but the present rule does not classify it as `U.MethodDescription`.

An algebraic, graph, categorical, process-calculus, effect-calculus, matrix, embedding, distributed, or neural representation can be used to express or analyze either case. Its correspondence to claims is governed separately through `C.29`. A work plan, work occurrence, method-family registry, or selector result also keeps its own governed object and governing pattern.

