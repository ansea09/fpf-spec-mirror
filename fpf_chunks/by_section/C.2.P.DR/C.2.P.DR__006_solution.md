---
chunk_kind: "child"
pattern_id: "C.2.P.DR"
pattern_title: "Declarative Representation Precision Restoration"
section_id: "C.2.P.DR:4"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/C.2.P.DR/C.2.P.DR__006_solution.md"
commit_sha: "d7a7123459d158c6d5f0d304d6170c4aa69af71b"
heading_path:
  - "C.2.P.DR — Declarative Representation Precision Restoration"
  - "C.2.P.DR:4 — Solution"
line_start: 45004
line_end: 45129
dependencies:
  - "A.10"
  - "A.15.1"
  - "A.15.2"
  - "A.15.4"
  - "A.19"
  - "A.19.SPR"
  - "A.20"
  - "A.21"
  - "A.3.1"
  - "A.3.2"
  - "A.3.4"
  - "A.6.0"
  - "A.6.1"
  - "A.7"
  - "B.3"
  - "C.16"
  - "C.2.1"
  - "C.2.P"
  - "C.29"
  - "E.10"
  - "E.10.ARCH"
  - "E.17"
  - "E.18"
  - "E.18.1"
  - "E.20"
  - "E.8"
  - "F.19"
keywords:
---

### C.2.P.DR:4 - Solution

Repair declarative-representation overread by separating the visible expression, the direct object or relation, and any representation use before naming the subject pattern for the current claim.

The repair order is:

1. **Name the visible expression or artifact.** Quote or identify the graph highlight, file, query text, predicate display, dashboard tile, table, publication face, path diagram, carrier path, mathematical expression, method-description expression, or pattern sentence that prompted the overread.
2. **Recover the exact current direct object or relation.** Name the graph structure, `PathSlice`, flow valuation, evidence or provenance relation, state predicate or value, query or formal object, publication face or occurrence, formal substrate, claim-bearing episteme, source relation, carrier-side object, pattern relation, or other direct outcome under its own governor. This is a list of alternative recovery outcomes, not representation kinds in one ontology.
3. **Distinguish the direct object from any representation or correspondence use.** When the visible expression represents a separately identified object or claim, name the exact relation and target. When the direct object or relation itself is current and no separate representation claim is needed, keep that direct use; do not relabel the direct object as a representation kind. Record `none` only when the receiving use needs an inspectable account of that distinction.
4. **Recover source or publication relation when current.** If a face, source chain, generated explanation, copied text, dashboard, file path, or publication unit is current, use the publication pattern or source-use pattern governing that relation.
5. **Name the tempting stronger action claim.** Say what the visible expression is being asked to do by resemblance: route, call, dispatch, invoke, run, flow, send, receive, authorize, release, prove, prescribe, execute, select, pass a gate, or record work.
6. **Select the subject pattern.** Use the direct pattern when the object or relation is already recovered; otherwise use this pattern only long enough to recover the direct outcome, any representation use, and the blocked stronger claim.
7. **State retained use.** Keep the weaker useful use: graph structure, evidence relation, source-finding, state predicate, publication face, exact representation use, formal-substrate input, candidate method reading, or pattern relation.
8. **State the blocked stronger action claim.** Block only the stronger claim that is not recoverable.
9. **Stop or reopen.** Stop when the subject pattern can carry the next claim. Before stopping, ask what claim, evidence relation, gate relation, safety relation, method relation, work relation, or source relation would become less reviewable if the visible expression were accepted as the stronger claim. Reopen if a later source changes the visible expression, direct object or relation, representation relation or target, source currentness, subject pattern, or intended use.

#### C.2.P.DR:4.1 - DeclarativeRepresentationRepair note

Use this compact note only when the receiving use needs an inspectable repair of FPF-governed wording:

```text
DeclarativeRepresentationRepair:
  VisibleExpressionOrArtifact:
  CurrentDirectObjectOrRelation:
  RepresentationOrCorrespondenceUse: <exact relation and represented target> | none
  SourceOrPublicationRelation:
  TemptingStrongerActionClaim:
  RecoveredGoverningPattern:
  RetainedUse:
  BlockedStrongerActionClaim:
  StopOrReopenCondition:
```

The ordinary result is the repaired wording, exact direct outcome, any current representation use, retained use, blocked stronger claim, and needed stop or reopen condition. The optional note records these values when the receiving use needs them to remain inspectable. If the subject pattern already supplies a suitable record, use it without duplicating the repair note here.

Use four plain questions before the claim-and-pattern table: What visible thing am I looking at? What direct object or relation is current? What, if anything, does it represent? What stronger action claim must remain blocked?

| Visible expression or artifact | Exact current direct object or relation | Representation or correspondence use | Stronger action claim blocked |
| --- | --- | --- | --- |
| highlighted graph path | exact E.18 graph path or `PathSlice`, with any flow valuation kept separate | the graphic rendering corresponds to that path when the relation is current; otherwise `none` when the `PathSlice` itself is under inspection | no prescribed route, valve work, or release by the highlight |
| dashboard tile | exact status or state value with its bearer and value frame, plus any current source or publication relation | the tile represents that value only through an exact current relation; otherwise `none` when the publication face itself is the direct object | no gate passage or release permission from green appearance |
| evidence-path expression | exact A.10 evidence or provenance relation for the named claim or effect | a diagram may represent that relation; otherwise `none` when the relation itself is current | no approval, permission, assurance, or release from path shape |
| solver file | exact publication form or carrier-side object, and whichever formal substrate, claim-bearing episteme, method, mechanism declaration, plan, run, or evidence relation is independently current | the solver expression corresponds to separately identified claims or a formal object when that relation is stated; otherwise `none` | no method, mechanism, performed work, result, or evidence by file form or executability |
| publication table | exact publication face or form and source relation, with table values or claims kept under their subject patterns | the table corresponds to a separately identified object or claim only when the exact relation is current; otherwise `none` | no evidence, approval, gate passage, or action authority from table layout |

#### C.2.P.DR:4.2 - Subject pattern selection

| If recovery shows... | Use this subject pattern | Keep this boundary |
| --- | --- | --- |
| graph object, graph path, `PathSlice`, crossing, flow valuation, transformation-flow structure relation, or graph expression over that structure | `E.18`, `E.18.2`, or `E.18.1` when P2W carry-through is current | Graph structure or path structure is not work route, method narrative, evidence result, or pattern dispatch by layout. |
| evidence relation or provenance relation for a claim, effect, or reliance use | `A.10` | Evidence path is not approval, permission, gate passage, release, safety, work occurrence, or assurance by itself. |
| state, status value, readiness, validity, or predicate-like value whose bearer and value frame is hidden | `A.19.SPR` or the direct status-value or state-value pattern | A predicate or state-like value is not a workflow, gate, or proof unless the subject pattern says so. |
| publication face, source expression, generated explanation, dashboard face, publication unit, or source-chain relation | `E.17`, `E.17.EFP`, `C.2.P`, `A.15.4`, or source-use pattern named by value | Publication and source visibility do not create work, evidence, authority, release, or gate passage. |
| mathematical representation, formal object, formal substrate, invariant, or mathematical-lens output | `A.6.0`, `C.29`, or direct mathematical pattern | Mathematical representation is not method, mechanism, proof of project result, or work execution until that claim is separately recovered. |
| context-local semantic way of doing | `A.3.1 U.Method` | A method claim is not closed by code, diagram, proof script, plan, run, or mechanism declaration; use `E.10.ARCH:3.1` only to recover the project concern and then recover each linked typed value under its own subject pattern. |
| already identified `U.Episteme` with one admitted `U.Method` as its exact `EntityOfConcern` and at least one substantive claim about that method as a way of doing | `A.3.2 U.MethodDescription` | Code, SOP, proof-script, solver-model, process-model, protocol, recipe, and diagram forms are clues only. A name, citation, approval, runnable form, or representation correspondence does not establish membership. |
| law-governed operation algebra, laws, admissibility predicates, transport, audit, realization, or governing-definition assignment | `A.6.1` and `E.20` | Mechanism meaning is not selected by saying "algorithm" or "method"; it needs mechanism fields. |
| planned work, intended window, resource budget, acceptance criterion, or source “role requirement” | `A.15.2 U.WorkPlan` for the plan. Resolve a “role requirement” separately to its exact local system-role kind, separate System-classification judgment, future assignment condition, capability, participant relation, or other direct condition; if unresolved, use `E.10.ROLE`. | A plan is not a Method, MethodDescription, evidence, gate passage, performed Work, or assignment occurrence. A required kind or condition does not create the future assignment. |
| exact dated Work occurrence | Recover every exact actual performer and its obtaining A.2.1 system-role assignment through A.13, then let `A.15.1 U.Work` independently identify the dated occurrence, enacted Method, time, and containing System. A representation claiming the exact Work keeps every actual performer named or recoverable. Keep the underlying assignment facts recoverable; include an assignment identifier in the representation only when the receiving use needs it. Add an F.6 relation through that same obtaining assignment only when the representation or receiving use expressly represents precise assignment-bound attribution. Missing or failed F.6 leaves the Work intact and blocks only that attribution. | The Work occurrence is not its trace, record, binding, resource use, result, diagram, plan, MethodDescription, source cue, or evidence path. |
| run trace or performed-work record | `C.2.1` for the exact trace or record episteme, plus its direct description, publication, source-use, or evidence-use pattern only when that claim is current | The episteme may designate exact `W`, `RA`, holder `S`, and `performedUnderAssignment(W, RA)` when it makes that attribution; it neither is the Work occurrence nor makes the relation obtain. |
| concrete parameter or participant binding | the exact direct subject-relation pattern, or `A.6.1` for one independently identified operation application and its actual argument or result binding | A declaration, call position, trace field, or type-compatible token establishes no actual binding. |
| performed resource use | the exact direct resource-use relation involving the already identified Work occurrence; use `B.1.6` only when aggregation is current | Resource use is a separately obtaining relation, not a Work field, record field, or result. |
| result or output | identify the exact result entity or episteme first; use `A.15.PROD` when production, entity inception, or production completion is current, and `A.6.RCD` only when the needed direct result relation has no current governor | A binding, record field, Work occurrence, or nearby output label does not identify the result or establish production. |
| FPF pattern application, pattern relation, neighboring-pattern relation, or placement cue | `E.8`, `F.19`, `E.10.ARCH`, or the direct pattern relation named by value | Pattern relations are declarative references or applications, not exits, receivers, routes, calls, owners, homes, or dispatches. |
| quoted source wording or ordinary navigation | quote-only or ordinary prose | Do not repair ordinary words into FPF terms when no FPF-governed claim is being made. |

#### C.2.P.DR:4.3 - Legitimate path and route settlement

`path` is not banned.

`A.10 evidence path for <claim, effect, or use>` is legitimate when the evidence relation or provenance relation for the named claim, effect, or reliance use is current. `E.18` graph path and `PathSlice` are legitimate when the graph object, path, slice, crossing, or flow valuation is current. Carrier file paths, URLs, mathematical paths, and quoted source paths are legitimate when their notation, source-use function, or use relation is current.

The defect is not the word. The defect is hidden ontology: the sentence treats a representation as if something literally ran, flowed, executed, authorized, released, proved, selected, or prescribed action without first naming the exact direct object or relation and its subject pattern.

When the representation is route-shaped, loop-shaped, graph-shaped, diffusion-like, or workflow-like, ask first which object is current:

| Current object | Subject pattern |
| --- | --- |
| constraint-governed `U.Structure` across several constrained loci | `A.22.CGUS` |
| transformation-flow structure, path, path slice, crossing, guard, or valuation | `E.18` and `E.18.3` when unfolding use is current |
| description, diagram, table, graph, route card, slide, README line, or narrative that renders the structure | `ConstraintGovernedUnfoldingStructureDescription@Context`, `DemonstrativeUnfoldingSlice@Context`, `A.6.3.NAR`, `E.17`, or the direct description subject pattern |
| reusable semantic way of doing, or a claim-bearing episteme that passes the A.3.2 MethodDescription membership test | `A.3.1` for the method; `A.3.2` for the qualifying episteme |
| work plan, work readiness, or performed work | A.15 family |
| evidence, assurance, gate, decision, architecture, publication, or currentness-refresh claim | the subject pattern for that claim |

Do not repair route-shaped wording by replacing it with another route-shaped word. Always recover the visible expression, exact direct object or relation, representation or correspondence use or `none`, retained use, blocked stronger action claim, subject pattern, and stop or reopen condition. When the representation use is `none`, that is enough to close the repair; do not require a represented target, preserved and lost structure, or a mathematical-lens admissible-use account. When an exact representation, mathematical-lens, or selected-structure use is current, also name its target, the preserved and lost structure, and the admitted and blocked uses required by C.29 or that structure's subject pattern.

#### C.2.P.DR:4.4 - Method, algorithm, mechanism, plan, and work settlement

Do not repair `algorithm`, `program`, `solver`, `proof`, `recipe`, `method`, `workflow`, `process`, `procedure`, `access path`, `query plan`, or `control strategy` by choosing one fashionable replacement.

**Method-description membership guard.** A code file, SOP, proof script, solver model, process model, protocol, recipe, diagram, or query plan is only a representation clue. First identify the claim-bearing episteme under C.2.1. Apply A.3.2 only when that same episteme has one admitted `U.Method` as its exact `EntityOfConcern` and at least one claim says how that method is done, such as its transformation or enactment concern, applicability, precondition, intended effect or preserved condition, bound, generic participant meaning, or internal method composition. A name, author, citation, approval, file form, runnable configuration, or representation correspondence alone is a near-miss. If the test fails, do not assign `U.MethodDescription`; keep the representation, publication, plan, dated work, result, formal substrate, mechanism declaration, evidence, or source use with its subject pattern. A representation or publication change does not decide membership. If claim content, exact method, or effective reference scheme changes, C.2.1 first identifies the resulting episteme; then apply A.3.2 to that individual.

Recover what the source is actually about and what it asserts:

| Current claim | Subject pattern |
| --- | --- |
| context-local semantic way of doing a transformation or enactment | `A.3.1 U.Method` |
| transformation or enactment kind stated inside a current method claim | keep it as one method-identity field or claim content under A.3.1; it is not a peer `U.Method` |
| independently grounded actual bounded change | `A.3.4 U.Transformation` |
| possible, required, desired, intended, planned, predicted, modeled, or asserted change | keep it as claim content under the exact requirement, architecture, capability-gap, functional-view, method, work-plan, dynamics-model, publication, or other subject pattern; wording alone admits no `U.Transformation` |
| already identified episteme whose exact `EntityOfConcern` is one admitted `U.Method` and whose claims include at least one substantive way-of-doing claim | `A.3.2 U.MethodDescription` |
| formal substrate, signature, postulates, laws, or mathematical declaration | `A.6.0`; use `C.29` when mathematical-lens use is current |
| operation algebra, admissibility predicates, transport, audit, realization, or mechanism-governing-definition assignment | `A.6.1` and `E.20` |
| planned work | `A.15.2 U.WorkPlan` |
| dated performed work | `A.15.1 U.Work` |
| evidence relation or provenance relation for a claim | `A.10` |
| wording quoted from source with no FPF-governed use | quote-only source wording |

**Cooling contrast.** A reusable cooling procedure can be `U.Method` only after the context-local way of doing, its transformation or enactment kind, transformed referent or structure, preconditions, and intended effects are recovered. “Required cooling effect” alone is claim content, not a method. If a later cooling episode actually changes the governed loop state, that occurrence remains a separate A.3.4 `U.Transformation` and needs its own changed referent, boundary, conditions, actual facts, and continuity or reidentification basis.

When the source label hides method, mechanism, formal-substrate, work, evidence, gate, result, or temporal claims, use `E.10.ARCH:3.1` to state the project concern in ordinary words, then identify each exact object and claim separately. For this host, repair only the representation overread and name the subject pattern for the current claim; linked values remain under their own subject patterns rather than becoming one representation-repair claim.

#### C.2.P.DR:4.5 - Programming-paradigm and process-model settlement

Imperative, functional, logical, constraint, object-centric event, effect-handler, pipeline, orchestration, Declare-style, SQL-like, e-graph, hypergraph, or process-mining wording is a clue to identify the visible expression, direct object or relation, any representation use, and current claim. It is not a decision procedure by itself.

Current practice makes the old contrast between imperative and declarative labels too weak as a final ontology:

- constructor and process-theory lines keep computation, information, dynamics, and procedure close to possible or impossible transformations and compositional realization;
- scoped effects and handlers separate operation syntax, semantic handling, scopes, resources, equations, type information, and effect information;
- Declare-style process models and object-centric event logs distinguish constraints, events, objects, relations, ingestion, transformation, storage, and analysis;
- e-graph and monoidal-rewriting work shows that computation or process representation may be equivalence or composition structure rather than instruction order.

Use those lines as guardrails: recover the exact FPF-governed object, relation, claim, or representation use and its subject pattern instead of replacing one programming-paradigm label with another.

