---
chunk_kind: "child"
pattern_id: "A.6.RCD"
pattern_title: "Needed Relation Claim Derivation and Relation-Kind Admission"
section_id: "A.6.RCD:4"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/A.6.RCD/A.6.RCD__006_solution.md"
commit_sha: "0990ff1d1ccee4587b8f7e16e7a725a8edbe66b4"
heading_path:
  - "A.6.RCD — Needed Relation Claim Derivation and Relation-Kind Admission"
  - "A.6.RCD:4 — Solution"
line_start: 16158
line_end: 16307
dependencies:
  - "A.11"
  - "A.6.0"
  - "A.6.5"
  - "A.6.REL"
  - "B.3"
  - "C.2.1"
  - "C.29"
  - "E.24"
  - "E.24.UK"
  - "F.18"
  - "F.9"
  - "G.11"
keywords:
---

### A.6.RCD:4 - Solution

Name the blocked receiving claim and participants. Reuse a current relation when it suffices. Derive only what the selected substrate warrants. Publish reusable predicate semantics only for repeated subject use. Admit a relation kind only with its direct obtaining and occurrence-identity laws. Stop when the receiving use works.

#### A.6.RCD:4.1 - Execute the demand-first method

1. **Name the receiver.** State the exact claim, check, decision, or continuation that cannot proceed, and what answer would close it.
2. **Recover participants and direct relations.** Use `A.6.P` to name the actual participant referents under their relation-participant meanings and retrieve the smallest plausible base from direct governing patterns and their obtaining laws. Similar tokens, shared field names, or adjacent graph edges are not a base.
3. **Choose the least constructor admitted by the current substrate.** State the constructor semantics and the base claim content it consumes. Do not infer an operator from punctuation or notation.
4. **Replay three things.** Test one positive case, one discriminating failure case, and the named receiving use. Keep hidden intermediates, polarity, scope, time, and base-definition editions visible when they change the result.
5. **Select the lightest disposition.** Choose exactly one of the four dispositions in section 4.3 and stop at its stopping rule.
6. **Open reusable semantics only when repeated subject use needs the same rule.** Identify one truthful `C.2.1` `EntityOfConcern`, state participant meanings, derivation, applicability, and dependencies, and keep the definition distinct from a `RelationSignature`.
7. **Open kind admission only when occurrence semantics are consumed.** A derived kind needs a direct subject settlement with obtaining, applicability, base dependencies, and a non-optional occurrence-identity rule. A primitive candidate additionally carries the failed derivation, the exact action-facing distinction lost, its own obtaining and recurrence laws, independent receiving uses, and a standalone governing-pattern obligation.

Use this compact working note only while the decision is live:

```text
A.6.RCD working note:
  blockedReceivingUse:
  participantMeanings:
  candidateBaseRelationClaims:
  selectedSubstrateAndEdition:
  constructorSemantics:
  positiveCase:
  discriminatingFailureCase:
  receivingUseReplay:
  disposition:
  predicateDefinitionEntityOfConcernIfCurrent:
  directSubjectSettlementIfKindCurrent:
  stopOrReturn:
```

The note is a pattern-local prompt. A filled, claim-bearing use is an episteme under `C.2.1`; the printed shape is not a new record kind, `RelationSignature`, relation kind, or relation occurrence.

#### A.6.RCD:4.2 - Respect substrate authority

A constructor probe is usable only when the selected substrate defines its inputs, output claim, applicability, and relevant laws. The following table is a non-exhaustive set of recurring single-substrate semantic probes. It is neither a universal operator registry nor a claim that any substrate supports the whole list.

| Recurring single-substrate semantic probe | Minimum semantics to recover | Boundary |
| --- | --- | --- |
| typed restriction | the base predicate, restricted participant kind or condition, and scope | a narrower claim is not automatically a new relation kind |
| participant permutation or converse | participant correspondence, polarity, and whether the direct subject ontology treats the inverse reading as the same occurrence | syntax does not decide occurrence identity |
| composition | the two or more base predicates, exact shared participant, order or direction, and intermediate witness policy | a hidden intermediate does not disappear from semantics because a query projects it away |
| projection | the source claim, retained participants, hidden participants, and existential or other projection law | projection can yield claim content without yielding an occurrence-identity rule |
| conjunction | all conjuncts, their common applicability, and one truth condition for the compound claim | co-truth does not create a cross-subject relation kind |
| negation or complement | the substrate's closed-world, open-world, constructive, probabilistic, or other negation law | absence of a base assertion is not automatically a negative relation fact |
| transitive or path closure | admitted edge relation, direction, path rule, zero-length policy, cycle policy, and subject structure | a graph path is a representation or witness; it is not the obtaining relation occurrence |
| aggregation | the population or collection, grouping rule, aggregated value, aggregation operator, empty or duplicate treatment, scope, and applicability | an aggregate or scalar summary does not silently become a relation predicate or occurrence |
| probabilistic operator | the event or sample space, random variables or events, probability operator or model, conditioning, threshold or decision rule, applicability, and uncertainty boundary | a probability, likelihood, or posterior does not silently become a relation predicate, and shared event labels do not bridge algebras |

**Cross-algebra claim-use boundary.** An explicit direct subject rule governs every joint receiving use of separately derived claims from different algebras, whether the use stays within one `U.BoundedContext` and one ReferencePlane or crosses contexts or planes. That rule states which claims are used and for what receiving use; it does not thereby define a cross-algebra constructor, a new predicate, or a relation occurrence. When the joint receiving use additionally depends on sense alignment across `U.BoundedContext`s or ReferencePlanes, authors MUST cite, in addition to that direct rule, the applicable `F.9` Bridge id, `CL`, Loss Notes, admitted-use statement, and the applicable ReferencePlane policy pin when planes differ. F.9 governs the declared alignment and its admitted cross-context use; it does not create the receiving-use relation, decision use, predicate, or relation occurrence. Any assurance penalty from that crossing reduces only `B.3` `R_eff`; it does not change `F` or `G`. One local same-context and same-plane joint use, one local single-substrate derivation, and bounded SoTA comparison require no fictitious Bridge.

A local compound claim needs recoverable constructor semantics, but it does not need a separately materialized substrate document. Authors MUST name and pin the substrate when the derivation is nontrivial, intended for interoperability, used as proof, or becomes a reusable predicate definition. If no current substrate supplies the proposed operator, return a missing-substrate blocker rather than improvising a universal constructor algebra.

#### A.6.RCD:4.3 - Select one of four dispositions

| Disposition | Test | Result | Stop |
| --- | --- | --- | --- |
| **1. Existing direct relation** | One current direct relation already has the needed participant meanings, obtaining condition, applicability, and receiving-use meaning. | State the readable direct claim under that pattern. | Stop. Do not derive a synonym predicate or duplicate relation kind. |
| **2. Local compound relation-bearing claim** | A substrate-admitted composition of governed base predicates closes this one receiving use, and no repeated definition or occurrence semantics is needed. | Put positive or negative compound claim content in one identified `C.2.1` episteme. An unresolved information-sufficiency or reliance assessment stays with the evaluation or evidence pattern; it is not a third predicate value. | Stop. Introduce no relation kind, `RelationSignature`, or `U.Relation` occurrence. |
| **3. Reusable predicate semantics, with derived-kind continuation only when needed** | Several uses in one direct subject practice need the same parameterized rule. | Publish one predicate-definition episteme. If those uses also need stable relation-occurrence semantics, return a derived-kind candidate plus its proposed direct subject settlement covering obtaining, applicability, base dependencies, and occurrence identity; route that candidate to `E.24` and `E.24.UK`, and to `A.11` when parsimony is current, for admission. | Stop at the definition unless occurrence semantics are named and the proposed settlement is supplied. A definition is not a kind; neither the proposal nor its direct subject pattern admits the kind. The route to `A.6.0` declaration opens only for an admitted result. |
| **4. Primitive relation kind** | Every accepted derivation loses one exact action-facing distinction, and the candidate has independent receiving uses plus its own obtaining, recurrence, applicability, and occurrence-identity laws. | Carry the candidate to `A.11`, `E.24`, and `E.24.UK`, and author a standalone direct subject pattern. | Stop or block if the failed derivation, lost distinction, independent use, direct pattern, or identity law is absent. A convenient name never passes this test. |

These are economy dispositions, not maturity stages. Later need can reopen a local claim or definition. The four dispositions do not impose a required maturity ladder on any application.

#### A.6.RCD:4.4 - Keep the governed objects distinct

| Object | What it is | What it is not |
| --- | --- | --- |
| existing direct relation occurrence | one obtaining `U.Relation` occurrence under its direct pattern | not its assertion, signature, identifier, or graph edge |
| local compound relation-bearing claim | claim content in one `C.2.1` episteme, asserting or denying satisfaction of a substrate-admitted compound predicate | not a relation kind and not a relation occurrence |
| reusable predicate-definition episteme | one `C.2.1` episteme in the direct subject pattern whose claims define parameterized predicate semantics | not a `RelationSignature` and not a classifier of relation occurrences |
| admitted derived relation kind | a classificatory distinction over relation occurrences, with obtaining defined through governed base relations | not the definition episteme; it needs its own direct subject settlement and identity rule |
| admitted primitive relation kind | a classificatory distinction whose needed action-facing semantics cannot be preserved by accepted derivation | not a reward for a familiar word or notation |
| claim or derivation representation | formula tokens, formula trees, query paths, graph elements, tables, diagrams, or other `C.29` representation elements | not satisfaction, obtaining, admission, or occurrence identity |
| designator or governed reference | a name or reference associated with an already settled definition episteme, relation kind, or individuated occurrence | not one token that silently creates or identifies all three |

#### A.6.RCD:4.5 - Settle a reusable predicate definition truthfully

A reusable predicate-definition episteme has one exact `C.2.1` `EntityOfConcern`. State what the definition claims about that value and why the repeated subject uses concern it. The `EntityOfConcern` can be a promise-content edition, a subject structure, a governed decision-work occurrence, or another exact subject value when that is truthful for the case. It is not a union of every participant, base assertion, formula, receiver, and publication that appears nearby.

Its content states:

- parameter and participant meanings;
- the exact base-relation claims and their direct governing patterns;
- the derivation rule under the selected substrate;
- polarity, scope, time, and applicability;
- base-definition and substrate dependencies plus their editions when current;
- positive and discriminating cases;
- the admissible claim use and the non-admissible occurrence or ontology overread.

If no single truthful `EntityOfConcern` can be selected, keep the needed results as local compound claims. Do not manufacture a union concern to make the definition publishable.

#### A.6.RCD:4.6 - Prepare derived or primitive relation-kind admission only with occurrence semantics

When a named receiver consumes occurrence semantics, A.6.RCD returns a relation-kind candidate and the settlement material needed for admission: a derived-kind candidate plus its proposed direct subject settlement, or a primitive-kind candidate plus its candidate standalone direct pattern. `E.24` and `E.24.UK` decide admission; `A.11` decides parsimony when that question is current. Neither a proposed settlement nor a candidate direct pattern admits the kind. For a candidate that is admitted, the resulting direct subject settlement states:

1. the classified relation occurrences and exact participant meanings;
2. the obtaining predicate and applicability;
3. for a derived kind, the exact derivation law and base-definition dependencies;
4. a direct occurrence-identity rule that distinguishes repetition;
5. recurrence, cessation, and continuation conditions when those distinctions matter;
6. at least one named receiving use that consumes occurrence semantics;
7. the standalone direct governing pattern.

An admitted relation kind never has `identity intentionally absent`. Ordinary use can omit explicit individuation, occurrence records, and designators because no receiver consumes them; the direct identity rule still exists.

A pure converse preserves one base occurrence only when the direct subject ontology explicitly says that inverse wording concerns the same occurrence. Restriction, projection, composition, closure, aggregation, and hidden intermediates require an explicit identity decision. Their syntax does not decide whether the derived occurrence inherits one base identity, is constituted as a composite occurrence, or has a new direct identity rule. If no truthful rule is available, remain at local-claim or predicate-definition level.

Authors MAY publish under `A.6.0` a `RelationSignature` whose `EntityOfConcern` is that exact kind only after the kind is admitted. The signature declares reusable SlotSpecs and restates the direct laws; it does not admit the kind or make an occurrence obtain.

#### A.6.RCD:4.7 - Separate recognition from assurance

**Recognition branch for ordinary receiving use.** Ask only:

1. What receiving claim or action is blocked?
2. Who or what are the exact participants, and under which meanings?
3. Does one current direct relation already answer it?
4. If not, what smallest substrate-admitted compound claim answers it?
5. Which of the four dispositions lets the receiver proceed now?

The ordinary branch can stop at a readable direct claim or one readable compound claim. It does not require a named substrate document, predicate-definition publication, relation kind, signature, explicit occurrence, or designator when the receiving use consumes none of them.

**Assurance branch for DPF and FPF authors.** DPF and FPF authors use this branch whenever they author a compound claim, reusable predicate definition, or relation-kind admission candidate, including a durable local compound claim that stops at disposition 2. In addition, verify:

- exact base patterns, definitions, editions, and applicability;
- selected substrate and constructor semantics;
- positive case, discriminating failure case, and receiving-use replay;
- one truthful definition `EntityOfConcern` when reusable semantics are published;
- dependency and currentness conditions;
- direct occurrence-identity and recurrence rules for every admitted relation kind;
- representation correspondence without representation-to-world collapse;
- naming only after the exact definition episteme, kind, or occurrence is settled;
- evidence, assurance, gate, and decision claims under their own governing patterns.

Passing the assurance branch does not make evidence constitutive of relation obtaining. It makes the derivation and admission decision replayable for the declared use.

#### A.6.RCD:4.8 - Stop and return deliberately

Stop at the first disposition that closes the named receiving use. Return to this pattern when:

- a relied-on base relation or predicate definition changes;
- the selected substrate edition or constructor semantics changes;
- applicability, polarity, participant meaning, scope, time, or hidden-intermediate policy changes;
- the derivation becomes unreadable, computationally unsuitable, or unable to interoperate for the declared use;
- repeated consumers begin to need one reusable definition or stable occurrence identity;
- a purported primitive gains an accepted lossless derivation, or a derived kind loses a truthful identity rule.

`G.11` governs currentness, dependency closure, and scoped refresh when a relied-on base definition, substrate edition, or applicability settlement changes. Re-evaluate only affected claims and dependent kinds; do not rebuild a global relation registry.

