---
chunk_kind: "child"
pattern_id: "A.6.4"
pattern_title: "EntityOfConcern retargeting"
section_id: "A.6.4:4"
section_title: "Solution — separate the arrow, use claim, current-case judgement, and any application"
source_path: "FPF-Spec.md"
output_path: "by_section/A.6.4/A.6.4__005_solution-separate-the-arrow-use-claim-current-case-judgement-and-any-application.md"
commit_sha: "d064720b072b822cbb2f1d41e555cf08e2904f11"
heading_path:
  - "A.6.4 — EntityOfConcern retargeting"
  - "A.6.4:4 — Solution — separate the arrow, use claim, current-case judgement, and any application"
line_start: 15374
line_end: 15480
dependencies:
  - "A.10"
  - "A.15"
  - "A.20"
  - "A.6.0"
  - "A.6.1"
  - "A.6.2"
  - "A.6.3"
  - "A.6.3.RT"
  - "A.6.5"
  - "A.7"
  - "B.3"
  - "C.2"
  - "C.2.1"
  - "C.29"
  - "C.3"
  - "E.10.D2"
  - "E.17"
  - "E.24.PUB"
  - "F.9"
keywords:
---

### A.6.4:4 - Solution — separate the arrow, use claim, current-case judgement, and any application

#### A.6.4:4.1 - Informal definition

> **Definition.** An **EntityOfConcern-retargeting morphism** is a local `EpMorphism r : X -> Y` whose exact endpoint epistemes concern different exact entities. A separate bounded-use assertion q affirms or denies that one declared invariant makes the stated loss acceptable for one named receiving use under named conditions.

`EntityOfConcernRetargetingMorphism` is a local mathematical subtype under C.29, not a durable kind. This pattern defines that subtype and the practical discipline for claims about its use.

Keep four things distinct:

1. **The arrow `r`.** Within the selected formal substrate, its exact domain X, codomain Y, arrow rule or designator, and declared formal equivalence identify it. The two endpoint epistemes and their different EntitiesOfConcern are recoverable. A changed use claim does not create another arrow.
2. **The bounded-use assertion `q`.** This is a C.2.1 episteme about exact arrow r. Its ClaimGraph states the invariant, visible loss, named receiving use, conditions, and affirmative or negative polarity. Its complete claim content, exact EntityOfConcern, and effective ReferenceScheme identify q. A citation inside q can point to case facts; it does not decide whether those facts satisfy the proposition.
3. **The current-case judgement.** Compare the exact current facts with q's conditions and proposition, and report `satisfies`, `fails`, or `cannot decide`. That result is not q's polarity and does not reidentify q or r. Use A.20 only when the case raises an internal-constraint check, A.10 only for a current evidence-use claim, and B.3 only for a current assurance claim or its material-reliance threshold. Otherwise the named rule and direct case facts are enough.
4. **Any application occurrence.** If a system actually computes, authors, or otherwise produces or changes an episteme by using the declared operation, identify that A.6.1 application, its argument and result bindings, the performing system, and any Work separately. The mathematical statement `r : X -> Y` alone names no occurrence.

The smallest useful practitioner account still asks six cheap questions:

| Question | What it recovers |
| --- | --- |
| Which source and receiving epistemes are related? | exact endpoints X and Y of r |
| Which different entities do they concern? | the independently identified EntityOfConcern pair |
| What exactly does q affirm or deny? | invariant, visible loss, named receiving use, conditions, and polarity |
| Which current facts bear on that proposition? | the direct case basis |
| What do those facts show? | `satisfies`, `fails`, or `cannot decide` |
| If the case cannot be decided, what is missing? | the exact missing fact and reopen condition |

These answers may be one short paragraph; they require no new record form or assurance package. Add preserved or withdrawn commitment lists, predicate changes, grounding, scheme, scope, operating conditions, viewpoint selections, evidence, currentness, or a durable result only when they change the proposition, judgement, or receiving action. Add an F.9 Bridge only when the same case separately claims a semantic relation between two exact F.17 local senses.

When the judgement is `fails`, do not use an affirmative q as support for that case. When it is `cannot decide`, keep the source material, name the exact missing fact and what would reopen the question, and stop. Failure of an affirmative q does not by itself establish a negative q; a negative assertion needs its own claim content and case basis.

#### A.6.4:4.2 - Formal declaration and object boundaries

Repeated formal use may be declared in an A.6.0 `U.Signature(profile=FormalSubstrate)` episteme. That declaration is about the local subtype `EntityOfConcernRetargetingMorphism`; it is not the subtype, one arrow, a use claim, or an application occurrence.

```text
SubjectKind     = local formal subtype EntityOfConcernRetargetingMorphism of EpMorphism
RangedValueKind = admitted ordered-pair range over exact U.Episteme values satisfying the declared endpoint-kind constraints
ResultKind      = omitted; r is the declared subject, not an operation result
Applicability   = selected formal substrate and endpoint and arrow-family conditions
```

`X` and `Y` are exact C.2.1 epistemes. `r : X -> Y` is one local mathematical arrow under C.29. Its identity uses the exact endpoints, arrow rule or designator, and the selected substrate's equivalence criterion; the endpoints alone do not identify it. The declaration states which parts of X and Y's claim content, exact EntityOfConcern, and effective ReferenceScheme remain the same or differ. If r's rule reads a representation or another separately obtaining relation, it names the exact occurrence and compares endpoint facts without changing that occurrence.

A.6.4 reuses the one A.6.2 formal model: category `Ep`, endpoint-only thin category `EoCBase`, `dom`, `cod`, identities, `compose`, and the declared mapping `α`. For retargeting arrow r, `α(r)=u_{α(X),α(Y)}` is the unique formal endpoint arrow between the independently different EntitiesOfConcern. It records only that endpoint difference and deliberately forgets r's arrow rule; it is not an independently declared domain or world-side relation. The local characteristic `entityOfConcernChangeMode(r)=retarget` records the same endpoint difference. No function evaluation or second retargeting calculus is implied.

The bounded-use assertion q, current-case judgement, and any application occurrence remain separate. Grounding, representation, an F.9 Bridge, evidence, publication, Work, gate, currentness, and assurance also remain separate objects or claims under their direct patterns. Add A.6.5 SlotSpecs only inside an exact reusable direct-relation declaration; they are not fields of r, X, Y, or q.

#### A.6.4:4.3 - Laws (ER-0...ER-6)

These laws refine A.6.2 for the local retargeting subtype. They do not assert durable U-kind membership.

**ER-0 - Arrow class and endpoint basis.**

An arrow `r : X -> Y` is in the local retargeting subtype only when X and Y are exact C.2.1 epistemes, `entityOfConcernChangeMode(r)=retarget`, and their exact EntitiesOfConcern differ. A shared label, kind name, diagram, implementation, use claim, or F.9 card identifies neither r nor its endpoints by itself.

**ER-1 - Arrow identity and neighboring facts.**

1. The selected formal substrate supplies r's arrow rule or designator and equivalence criterion; same endpoints alone do not identify an arrow.
2. The declaration states which parts of X and Y's claim content, exact EntityOfConcern, and effective ReferenceScheme remain the same or differ. It names any separately obtaining representation or other relation that r's rule reads and the endpoint facts compared; r does not change that occurrence.
3. Grounding, scope, operating condition, representation, and any viewpoint selected for a describing use remain separate values or relations.
4. A different scheme, scope, context, or plane does not by itself create an F.9 Bridge. Cite F.9 only for an actually claimed direct relation between two exact F.17 local senses.

**ER-2 - Separate use proposition and current-case judgement.**

For each named receiving use, one separate C.2.1 assertion q affirmatively or negatively states whether the source claims conservatively support the declared invariant in the receiving episteme and whether the visible loss is acceptable under the named conditions. The same r may have different q assertions for different uses without changing arrow identity.

A separate current-case judgement applies q to the exact current facts and returns `satisfies`, `fails`, or `cannot decide`. A direct fact, proof, test, or obtaining relation can supply the ordinary case basis. Open A.20 only for an internal-constraint claim, A.10 only for evidence use, and B.3 only for assurance or its material-reliance threshold. None identifies r, changes q's polarity, or turns `cannot decide` into support.

**ER-3 - Composition and separately claimed final use.**

Two retargeting arrows with an exact matching middle episteme compose in the parent Ep category; A.6.2 category closure supplies the composite and requires it to satisfy the parent laws. The composite remains in the A.6.4 retargeting subtype only when its final endpoint EntitiesOfConcern differ and its other subtype laws hold. A round trip whose final endpoints concern the same exact entity is a preserve-mode EFEM arrow in the parent class, not an A.6.4 retargeting arrow.

A claim that an admitted composite is suitable for a final use is another q: it states the final source and receiving entities, preserved invariant, accumulated loss, receiving use, conditions, and polarity. A separate judgement applies that proposition to the final current case.

No universal SquareLaw follows. A consumer that claims two evaluation routes equivalent, or relies on a correspondence between epistemes, identifies the routes or correspondence, comparison rule, tolerated difference, and witness under the direct governor of that claim.

**ER-4 - Determinism and repeat boundary.**

Determinism, reversibility, and idempotence may be properties of the declared arrow only when the selected formal substrate states the exact domain, equality or equivalence, and evidence used to test them. A repeat property of an operation or application is a different claim: it follows from the rule and inputs of that operation or application. The mathematical statement `r : X -> Y` says nothing about execution or repetition. Ambient time, randomness, solver state, and external services belong to an explicitly declared operation or mechanism.

**ER-5 - Applicability and optional semantic-Bridge branch.**

The formal declaration states admissible endpoint families and material mathematical conditions. Each q separately states the invariant, loss boundary, receiving use, case conditions, and affirmative or negative polarity; the current-case judgement states whether the facts satisfy it. F.9 is triggered only for a separately claimed relation between two exact local senses. Optional `CL` summarizes evidence about that Bridge; it is neither a retargeting threshold nor a participant in r or q.

Legacy `KindBridge` plus mandatory `CL`, and generic SquareLaw-retargeting interfaces, are not reactivated here. A consumer that still needs one identifies a current direct governor or stops at `missing-governor`.

**ER-6 - Separate application, Work, and resulting episteme.**

An arrow that preserves the EntityOfConcern belongs to the A.6.3 preserving branch rather than this subtype. When a system measures, computes, fits, translates, authors, or otherwise changes an episteme, identify the A.6.1 application and bindings when current, the performing system and Work, and the resulting C.2.1 episteme separately. The arrow can relate those epistemes without performing that activity or creating a universal production relation.

#### A.6.4:4.4 - Boundary with representation, explanation, transformation-flow structure, and neighboring claims

A.6.4 is triggered only by an independently established change of exact EntityOfConcern. A changed kind, ontology frame, predicate set, mathematical domain, or notation is a recognition cue that reopens the C.2.1 identity test; none decides the branch by itself.

Boundary rules:
- if the EntityOfConcern is preserved and the main change is representation scheme or reasoning medium, use `A.6.3.RT`;
- if the EntityOfConcern is preserved and the main change is explanation mode, explanatory stance, or explanation-facing publication, use `E.17.EFP`;
- if the same case also asserts a semantic relation between two exact local senses from different semantic contexts, test `F.9` separately and cite a Bridge only when its predicate obtains; use `F.9.1` only for an optional stance note about that already constituted use claim. A domain correspondence, mathematical rule, or direct case fact that supports q does not by itself open F.9;
- if a legacy consumer asks for `KindBridge`, `CL`, or a universal SquareLaw-retargeting witness without a current direct governor, stop at `missing-governor` rather than making that apparatus constitutive in A.6.4;
- if the receiving item is useful only under narrower declared use with visible loss and source-bearing reopen, use `A.6.3.CSC`;
- if decoded or latent output is interpretable but not tied to source claim, access relation, recoverability evidence, admissible-use value, and remaining reader action, keep it report-only, exploratory, source-bearing reopen, or in the named neighboring pattern;
- if a `StructuralReinterpretation`, `PathSliceId`, `CrossingRef`, or `DecisionLogRef` is present, use `E.18`, `A.20`, or `A.21` for graph, path, constraint, and gate relations. Those references do not prove semantic continuity or retargeting admissibility by themselves;
- if changed problem formulation changes abductive prompt, candidate generation, rival-set formation, selected prime hypothesis, plausibility filtering, or abductive reopen, use `B.5.2`;
- if the receiving item is used as work, evidence, assurance, gate passage, temporal claim, dynamics law, or control relation, use `A.15`, `A.10`, `B.3`, `A.21`, `C.27`, `A.3.3`, or another pattern that defines or tests the current claim.

A.6.4 defines arrow r, bounded-use assertion q, and the separate current-case judgement that E.18 may place at a `StructuralReinterpretation` locus. That placement identifies none of them and does not make the judgement `satisfies`.

