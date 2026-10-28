---
chunk_kind: "child"
pattern_id: "C.2.P.DR"
pattern_title: "Repair Claims Based on Declarative Form Alone (Declarative Representation Precision Restoration)"
section_id: "C.2.P.DR:4"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/C.2.P.DR/C.2.P.DR__006_solution.md"
commit_sha: "3f6e02840fe3a22427aed590f9688a9c8f6bf5c8"
heading_path:
  - "C.2.P.DR — Repair Claims Based on Declarative Form Alone (Declarative Representation Precision Restoration)"
  - "C.2.P.DR:4 — Solution"
line_start: 54041
line_end: 54164
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

1. **Identify the expression.** Quote or point to the part that prompted the unsupported inference.
2. **Recover the object or relation at issue.** For example, distinguish a graph path, an evidence relation and a reported state value. Use its subject pattern when that rule is already clear; the selection table below helps when it is not.
3. **Distinguish the direct object from any representation or correspondence use.** When the visible expression represents a separately identified object or claim, name the exact relation and target. When the direct object or relation itself is current and no separate representation claim is needed, keep that direct use; do not relabel the direct object as a representation kind. Record `none` only when the receiving use needs an inspectable account of that distinction.
4. **Recover a source or publication relation when it matters to this claim.** Use the pattern governing that relation and its actual participants.
5. **State the disputed operational claim.** Name the action, result or authority being inferred from the expression.
6. **Apply the claim's subject pattern.** Establish its required grounds or identify what is missing. An actual permission or gate condition comes from that rule.
7. **Preserve the supported use.** The graph may still support a comparison, for example, while leaving action permission unresolved.
8. **Delimit the unsupported claim.** Do not assert the stronger result from appearance alone. Distinguish that missing basis from a use actually blocked by an applicable rule; a separately established result remains usable under its own conditions.
9. **Stop or reopen.** Stop when the repaired statement supports the intended use or the subject pattern supplies the remaining question. Reopen when a changed source, correspondence or intended use can invalidate that result.

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

The ordinary result is the repaired statement and any unresolved condition that changes its use. In the optional note, `BlockedStrongerActionClaim` identifies the assertion that appearance does not establish; it does not by itself declare the underlying action prohibited. Name an actual blocked use and its governing condition separately when applicable. Reuse a suitable subject-pattern record without copying it into another repair note.

Use four plain questions before the claim-and-pattern table: What visible thing am I looking at? What direct object or relation is current? What, if anything, does it represent? Which stronger claim still needs grounds?

| Visible expression or artifact | Exact current direct object or relation | Representation or correspondence use | Stronger action claim blocked |
| --- | --- | --- | --- |
| highlighted graph path | exact E.18 graph path or `PathSlice`, with any flow valuation kept separate | the graphic rendering corresponds to that path when the relation is current; otherwise `none` when the `PathSlice` itself is under inspection | no prescribed route, valve work, or release by the highlight |
| dashboard tile | exact status or state value with its bearer and value frame, plus any current source or publication relation | the tile represents that value only through an exact current relation; otherwise `none` when the publication face itself is the direct object | no gate passage or release permission from green appearance |
| evidence-path expression | descriptive A.10 evidence-provenance path for the named claim or bounded use, citing independently established direct relations | a diagram may represent that descriptive path through an exact current correspondence; otherwise `none` when the path itself is under inspection | no approval, permission, assurance, or release from path shape |
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
| exact dated Work occurrence | Recover every exact actual performer and its obtaining A.2.1 system-role assignment through A.13, then let `A.15.1 U.Work` independently identify the dated occurrence, enacted Method, time, and containing System. A representation claiming the exact Work keeps every actual performer named or recoverable. Keep the underlying assignment facts recoverable; include an assignment identifier in the representation only when the receiving use needs it. Add an F.6 relation through that same obtaining assignment only when the representation or receiving use expressly represents precise assignment-bound attribution. Missing or failed F.6 attribution alone leaves the Work intact while its independent A.13/A.15.1 grounds still hold and blocks only that attribution. | The Work occurrence is not its trace, record, binding, resource use, result, diagram, plan, MethodDescription, source cue, or evidence path. |
| run trace or performed-work record | `C.2.1` for the exact trace or record episteme, plus its direct description, publication, source-use, or evidence-use pattern only when that claim is current | The episteme may designate exact `W`, `RA`, holder `S`, and `performedUnderAssignment(W, RA)` when it makes that attribution; it neither is the Work occurrence nor makes the relation obtain. |
| concrete parameter or participant binding | the exact direct subject-relation pattern, or `A.6.1` for one independently identified operation application and its actual argument or result binding | A declaration, call position, trace field, or type-compatible token establishes no actual binding. |
| performed resource use | the exact direct resource-use relation involving the already identified Work occurrence; use `B.1.6` only when aggregation is current | Resource use is a separately obtaining relation, not a Work field, record field, or result. |
| result or output | identify the exact result entity or episteme first; use `A.15.PROD` when production, entity inception, or production completion is current, and `A.6.RCD` only when the needed direct result relation has no current governor | A binding, record field, Work occurrence, or nearby output label does not identify the result or establish production. |
| FPF pattern application, pattern relation, neighboring-pattern relation, or placement cue | `E.8`, `F.19`, `E.10.ARCH`, or the direct pattern relation named by value | Pattern relations are declarative references or applications. Exit, receiver, route, call, owner, home, or dispatch wording must express a clear ordinary or technical relation; wording alone supplies no action or control semantics. |
| quoted source wording or ordinary navigation | quote-only or ordinary prose | Do not repair ordinary words into FPF terms when no FPF-governed claim is being made. |

#### C.2.P.DR:4.3 - Legitimate path and route settlement

`A.10 evidence path for <claim, effect, or use>` is legitimate when the evidence relation or provenance relation for the named claim, effect, or reliance use is current. `E.18` graph path and `PathSlice` are legitimate when the graph object, path, slice, crossing, or flow valuation is current. Carrier file paths, URLs, mathematical paths, and quoted source paths are legitimate when their notation, source-use function, or use relation is current.

Repair path wording when it carries an unsupported claim about what happens or what may be done. A clear ordinary reference or navigation instruction can remain unchanged.

For a route or unfolding expression, identify the object before selecting its rule:

| Current object | Subject pattern |
| --- | --- |
| constraint-governed `U.Structure` across several constrained loci | `A.22.CGUS` |
| transformation-flow structure, path, path slice, crossing, guard, or valuation | `E.18` and `E.18.3` when unfolding use is current |
| description, diagram, table, graph, route card, slide, README line, or narrative that renders the structure | `A.22.CGUS:4.4` for descriptions of a qualified CGUS and post-qualification demonstrative slices, including the wording `ConstraintGovernedUnfoldingStructureDescription@Context` or `DemonstrativeUnfoldingSlice@Context`; `A.6.3.NAR` for narrative rendering; `E.17` for publication; or the direct description subject pattern |
| reusable semantic way of doing, or a claim-bearing episteme that passes the A.3.2 MethodDescription membership test | `A.3.1` for the method; `A.3.2` for the qualifying episteme |
| work plan, work readiness, or performed work | A.15 family |
| evidence, assurance, gate, decision, architecture, publication, or currentness-refresh claim | the subject pattern for that claim |

Recover the relation the route expression conveys. Direct inspection of a graph object needs no separate represented target or lens account. If a representation or selected structure supports an inference, establish its target and the preservation or loss relevant to that inference under its subject pattern. Use C.29 for a separate mathematical representation or transfer issue; adequate local mathematics or an unambiguous rendering can suffice without a C.29 record.

#### C.2.P.DR:4.4 - Method, algorithm, mechanism, plan, and work settlement

For method-like wording, recover the claimed way of doing and distinguish it from its expression and any actual performance.

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

When the source label hides method, mechanism, formal-substrate, work, evidence, gate, result, or temporal claims, use `E.10.ARCH:3.1` to state the project concern in ordinary words, then identify each exact object and claim separately. Use this pattern to repair only the representation overread and name the subject pattern for the current claim; linked values remain under their own subject patterns rather than becoming one representation-repair claim.

#### C.2.P.DR:4.5 - Programming-paradigm and process-model settlement

A paradigm label helps locate the relevant source semantics. Those semantics, together with the claim being made, determine which FPF question to ask.

The source treatments below expose different distinctions:

- constructor and process-theory lines keep computation, information, dynamics, and procedure close to possible or impossible transformations and compositional realization;
- scoped effects and handlers separate operation syntax, semantic handling, scopes, resources, equations, type information, and effect information;
- Declare-style process models and object-centric event logs distinguish constraints, events, objects, relations, ingestion, transformation, storage, and analysis;
- e-graph and monoidal-rewriting work shows that computation or process representation may be equivalence or composition structure rather than instruction order.

Use the distinction relevant to the case to recover the object or claim, then apply its subject pattern.

