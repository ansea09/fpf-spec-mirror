---
chunk_kind: "child"
pattern_id: "A.6.1"
pattern_title: "U.Mechanism - Reusable Law-Governed Operation Declaration"
section_id: "A.6.1:4"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/A.6.1/A.6.1__005_solution.md"
commit_sha: "2ada413629b846ef308222d16489a82cb5b40a71"
heading_path:
  - "A.6.1 — U.Mechanism - Reusable Law-Governed Operation Declaration"
  - "A.6.1:4 — Solution"
line_start: 11698
line_end: 11935
dependencies:
  - "A.1"
  - "A.1.1"
  - "A.10"
  - "A.15.1"
  - "A.15.2"
  - "A.19"
  - "A.2.6"
  - "A.22"
  - "A.22.CGUS"
  - "A.3.1"
  - "A.3.2"
  - "A.6.0"
  - "A.6.5"
  - "A.6.RCD"
  - "A.6.REL"
  - "B.3"
  - "C.2.1"
  - "C.29"
  - "C.3"
  - "E.10"
  - "E.10.ARCH"
  - "E.20"
  - "E.24.PUB"
  - "F.18"
  - "F.9"
  - "G.11"
keywords:
  - "AdmissibilityConditions"
  - "LawSet"
  - "OperationAlgebra"
  - "U.Mechanism"
  - "application binding"
  - "operation application"
  - "operation declaration"
  - "realization"
---

### A.6.1:4 - Solution

Use `U.Mechanism` as the dependent durable U-kind for a reusable law-governed operation declaration episteme. Identify it through C.2.1. Put operation vocabulary, typed argument and result declarations, application rules, laws, admission conditions, and applicability in its content. Keep each actual application and binding, realizing entity and realization occurrence, method, Work, evaluation, evidence, description, representation, and publication as its own object or relation. Section 4.7 routes each question to the pattern that can identify it.

**Local mechanism mantra.** *Name the operation family and subject. Declare exact arguments, results, application rules, laws, admission conditions, and applicability. Bind actual values only in one independently identified exact application. State a realization relation only when a named realizer satisfies its predicate. Keep method, work, evidence, description, and publication separate.*

This mantra is Plain recall wording. Its imperative grammar does not create an executable sequence. When condition-governed continuation is current, A.22.CGUS governs that structure.

Grammar does not classify the object. Plain recall wording remains a mnemonic aid. A prescribed order of performed work belongs to the direct method-description or work-plan pattern. A condition-governed executable sequence is admitted as a CGUS; when a presentation selects one traversal through that admitted CGUS, it is a separate `DemonstrativeUnfoldingSlice@Context` whose EntityOfConcern is the CGUS.

#### A.6.1:4.1 - Admit and identify U.Mechanism

`U.Mechanism` is a dependent durable U-kind governed through `U.Signature` and therefore through `U.Episteme`. Its identity is:

```text
<content, EntityOfConcernRef, effectiveReferenceScheme>
```

The dependence reuses the `U.Signature` identity settlement and governing pattern. It is not parthood and does not make `U.Mechanism` a root beside `U.Episteme`.

Use this early object-and-relation guide:

| Current object | Exact reading |
|---|---|
| `U.Mechanism` | The reusable declaration episteme governed here. |
| declared operation family | The exact subject identified by `EntityOfConcernRef`; its direct kind is preserved. |
| realizing entity | The entity claimed to realize the declaration; it keeps its own direct kind. |
| mechanism-realization relation | The direct relation between the mechanism episteme and a realizing entity under stated scope and time. |
| mechanism description | A C.2.1 episteme about the `U.Mechanism` episteme when such meta-description is actually needed. |
| mechanism publication | An E.24.PUB use that presents the episteme without changing its identity. |

A machine part does not become `U.Mechanism` by being called a mechanism. For example, a pump assembly remains a `U.System`; this pattern governs a reusable operation declaration to which a realizing entity may be related while retaining its direct kind.

#### A.6.1:4.2 - State mechanism content

The following is a conceptual content outline, not a mandatory record or publication layout. The field and content-group names do not admit new U-kinds, relation kinds, SlotKinds, RefKinds, application records, or work objects.

```text
U.Mechanism content:
  EntityOfConcernRef
  effectiveReferenceScheme
  SubjectKind
  RangedValueKind
  ResultKind?
  SliceSet?
  ExtentRule?
  OperationAlgebra:
    OperationDeclaration*:
      operationDesignator
      ArgumentDeclaration*:
        argumentDesignator
        argumentMeaning
        ValueKind
        bindingDesignationRule
        bindingPredicate
        cardinality?
      ResultDeclaration*:
        resultDesignator
        resultMeaning
        ValueKind
        bindingDesignationRule
        bindingPredicate
        cardinality?
      ApplicationPredicate
      ApplicationIdentityRule
      ApplicationExtentRule
  LawSet
  AdmissibilityConditions
  Applicability
  SignatureManifest?
```

The content components have distinct jobs:

| Content component | Meaning and use |
|---|---|
| `EntityOfConcernRef` | Identifies the exact declared operation family. |
| effective `U.ReferenceScheme` | Supplies the meaning under which the content identifies this episteme. A changed effective reference scheme changes episteme identity. |
| `SubjectKind`, `RangedValueKind`, and optional `ResultKind` | Name the declared subject and value range, plus a distinct result kind when current. No additional container kind is implied. |
| optional `SliceSet` and `ExtentRule` | Use only when membership of the same `SubjectKind` can differ across selected `U.ContextSlice` values. `SliceSet` names those addressable slices; `ExtentRule` maps one selected slice to `Extension(SubjectKind, slice)` by stating how membership is judged there. Leave both out for a time interval, time-varying result, measurement series, operation-application extent, value or result range, arbitrary change function, changing dataset, or claim-bearing mathematical set representation; C.29 owns the last case. |
| `OperationAlgebra` | Contains one exact `OperationDeclaration` for every reused operation. Each argument and result declaration gives a declaration-local designator, semantic meaning, exact ValueKind, binding designation rule, binding predicate, and any semantic cardinality. The application predicate says what applying that operation means; the extent and identity rules distinguish its particular applications. |
| `LawSet` | States equations, invariants, closure conditions, and other reusable regularities of the declared operations. |
| `AdmissibilityConditions` | States predicates that decide whether one proposed operation application is admitted under current values and conditions. |
| Applicability | Delimits declaration use by exact `U.ClaimScope`, selected time value, selected `CHR:ReferencePlane` when current, and mechanism-specific conditions. Cite `GammaTimePolicy` only when the temporal selection rule matters. When the selected `CHR:ReferencePlane` value is `world`, `WorldRegime in {prep, live}` may distinguish preparation from live use. |
| `SignatureManifest` | Names actual imported and provided declaration content when dependency replay matters. It is not a second U-kind or publication manifest. |

Choose the three headline fields before listing operation positions. In plain terms: name the common kind of thing this operation family is about in `SubjectKind`, and name the common value domain over which the family ranges in `RangedValueKind`. Add `ResultKind` only when one distinct family-level result kind is current. For every operation, point to the argument or result meaning that carries each current family-level role; extra arguments and results keep their own exact ValueKinds. A collection or reference wrapper likewise keeps its own ValueKind and must state how it refers to or contains the family-level kind. If the operations do not share one truthful subject-and-range pair, do not hide that fact in a union, `Any`, or an input/output list: split the declaration or stop. If several result kinds are only operation-local, omit the singular family-level `ResultKind` and keep them in their exact `ResultDeclaration`s.

`OperationDeclaration`, `ArgumentDeclaration`, and `ResultDeclaration` are declaration-content terms, not U-kinds, direct-relation participants, actual values, or records. A `bindingDesignationRule` says whether a binding carries the value itself or one exact governed reference that resolves to it; a stored token or compatible reference does not establish a binding. An operation index may be derived from the operation designators for retrieval, but it is not another semantic content group.

A.6.5 SlotSpecs are not used here. They declare participant meanings only inside a `RelationSignature` for one already governed direct relation kind. A.6.1 argument and result declarations instead govern the named values of an operation application. Mathematical operand order remains a C.29 representation unless an explicit correspondence relates it to these independently declared operation meanings.

Keep neighboring facts outside mechanism identity-bearing content. Cite an F.9 Bridge only when two exact `SchemeSenseCell` values are being related across semantic contexts and its predicate obtains. Cite an actual application binding only when the downstream claim asserts which value the application used or returned. Evaluation, subject participation, evidence use, and realization each require their own obtaining predicate. A new neighboring occurrence or binding does not change `U.Mechanism` identity unless it reveals changed semantic content. A stable designator can refer to a mechanism episteme; file path, publication state, release label, and layout do not enter episteme identity merely because a tool stores them beside the content.

#### A.6.1:4.3 - State meaning and applicability without a generic context slot

Meaning and applicability answer different questions:

- the effective `U.ReferenceScheme` determines how the declaration content is interpreted;
- `U.ClaimScope` identifies the entities and relations to which the current use claim applies;
- the applicability interval states when that use is claimed;
- the selected `CHR:ReferencePlane` states the world, conceptual, or epistemic referent mode when that distinction is current;
- mechanism-specific conditions state assumptions that affect operation admission;
- optional `modelUseStructureRef : U.StructureRef` cites one selected `BoundedModelUseStructure` only when its relations delimit or change mechanism use.

Do not replace these values with one generic context field. Do not add `modelUseStructureRef` merely to preserve an old context column.

When one proposed receiving use spans different local senses, take these steps. First, use F.9 only to test the exact `SchemeSenseCell` correspondence and identify an obtaining Bridge. Second, state a separate current C.2.1 claim about whether that Bridge suits this use, in this direction, under this correspondence rule, and within this loss tolerance; give the claim affirmative or negative polarity. Third, choose the reliance branch from the consequence of the proposed use:

- when the receiver makes no assurance claim and the use does not meet B.3's material-reliance threshold, use A.10. Name the exact current evidence-provenance relation, this bounded use, the unsupported stronger use, its window, and the reopen or stop condition; proceed only with `RelianceDisposition=pass` for this bounded use;
- when the receiver makes an assurance claim or the threshold is met, enter B.3 and first ask whether a current assurance claim exists. A met threshold requires the minimum reliance safety assurance record and its accountable contest boundary, but it creates no positive claim. Proceed only when a positive current assurance claim with a sufficient record carries this bounded assurance use; otherwise state the no-assurance-claim or insufficient-record disposition and narrow or stop the use.

A Bridge, bounded-use claim, or reliance result neither admits an operation application nor says that reuse or Work occurred. A.6.1 `AdmissibilityConditions` still decide whether the proposed operation application is admitted; the actual application and bindings remain under A.6.1, and dated Work remains under A.15.1.

For example, let `BridgeDoseTerms-7` be the obtaining F.9 Bridge between exact cells `WardDoseValueCell` and `ProtocolDoseValueCell` under its exact `BridgePredicateProfile`. The separate C.2.1 claim for reusing the protocol mechanism in the ward-to-protocol prescribing direction is negative because the use rule cannot meet the ward's zero tolerance for changing the dose unit or scale. That reuse stops before reliance. It also stops when the bounded-use claim is absent, when A.10 does not return `RelianceDisposition=pass` for an ordinary bounded use, or when B.3 supplies no positive current assurance claim with a sufficient record for an assurance-bearing use. None of those outcomes makes the Bridge cease to obtain or makes an operation application admitted or actual.

A changed effective `U.ReferenceScheme` identifies another mechanism episteme through C.2.1. A changed selected `CHR:ReferencePlane` returns to CHR; a changed `BoundedModelUseStructure` returns to A.1.1/A.22. If the project also claims that a plane transition or model-use change relation occurred, name its admitted predicate and participants or stop that claim. In every branch, name the exact source and target objects, the comparison or relation actually asserted, and the meaning or structure it preserves and loses. Any reliability claim remains under its direct reliability relation; neither a Bridge nor transition wording alters Formality or Guarantee by itself.

Numeric comparison and aggregation use A.19 and the direct measurement and scale patterns. Orders are declared before arithmetic is applied, units are made compatible before values are combined, and any reduction to one score cites its governing scalarization relation.

#### A.6.1:4.4 - Separate laws, admission, evaluation, and evidence

`LawSet` states regularities of the declared operations. `AdmissibilityConditions` decide whether one proposed application may proceed under current values and declared conditions. If a mechanism uses `admit`, `degrade`, or `abstain`, those are declared application dispositions with declared effects; they are not automatically the operation's result algebra.

A recognition-evaluation operation declares its own finite result value `true | false | unknown`. It returns `true` when its governed bound argument values determine that the candidate satisfies the selected world-side criterion, `false` when they determine that the candidate fails it, and `unknown` when missing evidence or an unavailable dependency prevents either determination. `unknown` is neither `false`, non-obtaining, a third candidate state, nor a receiving-work disposition. One admissible application can therefore return `unknown`.

World-side satisfaction or failure follows the direct criterion and candidate facts whether or not the project can currently determine them. Measurements, evidence, and assurance may support or warrant claims about those facts or about the returned judgment. If an exact evidence or interpretation-basis episteme is also a declared operation argument, its actual binding establishes only that the application used that value under the declared argument meaning. It does not make the criterion true, make the evidence correct, or constitute the candidate.

A separately materialized evaluation-result or classification-assertion episteme remains under C.2.1. Its claim content may state the returned value, while exact evidence and assurance relations govern support or warrant and G.11 governs edition currentness. Neither the episteme nor its currentness is the operation result value itself. Thus a mechanism realization may obtain while current evidence is insufficient to rely on it, and an evaluation may return a value without changing mechanism identity.

#### A.6.1:4.5 - Bind one actual operation application exactly

Use the readable direct forms first:

```text
During exact application P of declared operation O, value V is bound under argument declaration a.
Exact application P returns value R under result declaration r.
```

A particular application is an occurrence of the `ApplicationPredicate` declared for exact operation O. The exact operation declaration supplies the application identity and extent rules; the phrase *operation application* does not admit a public `OperationApplication` U-kind, one universal application relation kind, or a work record. Its identity rule must name the semantically relevant application locus and boundary: for example, one physical cycle, one calculation invocation from call to return, or one comparison act from selected operands to returned judgment. If none of those examples fits, name the domain event that starts and ends the application. A trace identifier can designate that occurrence but cannot identify it by storage convention alone. If the declaration supplies no truthful application predicate, extent rule, or identity rule at the granularity required by the receiving claim, the actual application is blocked rather than reconstructed from a method name, plan row, log, or nearby result.

An *operation-application binding* is an occurrence of one declaration-local binding predicate under that exact application. Its direct participants are the exact application occurrence and the exact bound entity or value. The exact mechanism episteme and the named argument or result declaration govern the predicate; they are not substituted for the actual value. An argument binding obtains only when the value actually participates in P under the declared argument meaning, resolves under the binding designation rule, satisfies the declared ValueKind and cardinality, and lies within P's governed extent. A result binding obtains only when P actually returns that value under the declared result meaning; type compatibility, a planned filling, a method-description field, a stored reference, or a matching token establishes neither binding.

One binding occurrence is identified by `<exactApplicationOccurrence, exactMechanismEpisteme, operationDesignator, argumentOrResultDesignator, exactBoundValue, maximalContinuousBindingExtent>`. The extent lies within the exact application extent; a result-binding extent cannot begin before that result is returned. Repeated applications remain distinct through their independently governed application identities, and the same value bound under two declaration-local meanings yields two distinct bindings. A declaration may state a different cardinality or binding-continuity rule only when that semantics is part of the exact operation declaration.

The controlled phrase *operation-application binding* names this family of declaration-local binding occurrences; it is not a renamed universal work-participant, input, output, result, evidence, or production relation kind. A result binding says which value the application returned. It does not say that dated work produced or first constituted that entity, that a result episteme exists, or that another claim should rely on it.

A dated performance is a separate Work individual admitted under `U.Work` by A.15.1. When a work claim also relies on one already identified application and its bindings, identify the Work occurrence independently. Name the admitted performer System `S` and the obtaining assignment `RA`; verify that `S = RA.HolderSystemSlot`, that `RA` covers the attributed Work extent, and that F.6 `performedUnderAssignment(W, RA)` obtains. State the Work temporal extent and the actual `enactsMethod -> U.Method` and `executedWithin -> U.System` relations. Add a work-to-referent relation, performed resource use, continuity policy, or work mereology only when the claim asserts that relation and its own predicate obtains. A.6.1 does not identify the Work occurrence. If neither an exact direct subject relation nor a truthful A.6.1 application binding governs a claimed actual participant, retain the exact missing-governor blocker.

#### A.6.1:4.6 - State realization as a direct relation

Use the readable direct form first:

```text
Entity E realizes U.Mechanism M for ClaimScope S during interval T.
```

The relation has these positions when typed reuse needs them:

| Relation position | Value kind | Meaning |
|---|---|---|
| declared mechanism | `U.Mechanism` | The declaration whose operations and laws are current. |
| realizing entity | `U.Entity` or a narrower direct kind | The entity claimed to realize the declaration; its direct kind remains unchanged. |
| realization scope | `U.ClaimScope` | The exact entities and relations for which the realization claim is made. |
| derived realization extent | temporal interval | The maximal continuous interval over which the realization predicate obtains; this is an identity contribution, not a writable participant. |

The realization predicate obtains when the realizing entity provides the declared operations and preserves the declared laws for admitted uses in the stated scope and interval. A refined mechanism declaration may narrow Applicability or strengthen laws or admission conditions only with the preserved and changed semantic content stated explicitly. The realizing entity realizes the exact mechanism episteme named in the relation; it neither creates nor constitutes a refinement or edition relation. A claimed realization is lowered when it relaxes a declared law, bypasses an admission condition, or relies on undeclared operation meanings.

The non-derived participants are the declared mechanism, realizing entity, and realization scope. When a later use needs one occurrence distinguished from another, its direct identity is `<declaredMechanism, realizingEntity, realizationScope, maximalContinuousRealizationInterval>`. The interval is derived as the maximal continuous interval over which the realization predicate obtains. A new evaluation window or a gap in available evidence does not split the occurrence; demonstrated cessation followed by later realization does.

Ordinary use stops at the readable sentence. If another claim must refer to or compare one realization occurrence, the direct relation pattern and A.6.REL govern explicit occurrence identity. Evidence, evaluation, application, and binding occurrences remain supporting or use-side neighbors rather than realization participants.

#### A.6.1:4.7 - Keep mechanism, application, method, work, and description questions separate

One project concern can need several linked values. Recover each by its working question:

| Working question | Governing object and pattern |
|---|---|
| What reusable operation declaration is current? | `U.Mechanism` under A.6.1. |
| What particular operation application and actual argument or result values are current? | The exact declaration-local application and operation-application binding occurrences under A.6.1. |
| What semantic way of doing is selected? | `U.Method` under A.3.1. |
| What episteme describes that method? | `U.MethodDescription` under A.3.2. |
| What work is intended? | `U.WorkPlan` under A.15.2. |
| What dated work occurred? | One Work occurrence admitted under `U.Work` by A.15.1. |
| What entity realizes the mechanism? | The entity's direct kind plus the mechanism-realization relation in A.6.1. |
| What supports a claim about admission, application, result, or realization? | Domain-local evaluation, measurement, evidence, assurance, and currentness relations under their direct patterns. |
| How is the mechanism represented or published? | A.6.3, A.6.3.RT, and E.24.PUB. |

A method description may cite a mechanism declaration. An independently governed selector result or one actual A.6.1 application may select a method, and an exact direct constraint relation may constrain one; the mechanism declaration does not act merely by being named. An operation declaration may type a `U.Method` as an argument or result only when that is the operation's declared meaning; one actual application may then bind an exact method value. Neither the declaration nor binding establishes a planned assignment, actual `enactsMethod`, or dated work occurrence. One exact Work occurrence admitted under `U.Work` may enact the method; the claim about that occurrence may cite the independently identified application and bindings under A.15.1, while performer assignment, extent, containing system, resources, affected referent, continuity, and neighboring result or effect claims remain separately governed.

#### A.6.1:4.8 - State exact comparison claims among mechanism declarations

State a mechanism-declaration comparison only when its predicate is defined and the case facts satisfy it. A relation label alone admits neither a relation kind nor an occurrence.

| Current comparison claim | Exact preservation test |
|---|---|
| refinement | Preserves the inherited operation, argument, result, application, and binding meanings selected by the claim; states every narrowed Applicability or strengthened law or admission condition; and makes no substitution claim outside the retained applicability. |
| conservative extension | Adds exact operation declarations or declared optional arguments or results while preserving the meanings, application predicates, identity and extent rules, laws, and admitted uses of inherited operations. |
| equivalence | Supplies an explicit mapping that preserves and reflects the selected operation declarations, argument and result meanings, binding meanings, application predicates, identity and extent rules, and law and admission structure. |

These rows test declaration content; they do not admit a relation kind or occurrence. If the corpus already admits the exact comparison relation, use its direct pattern. If one case-specific comparison claim is enough, use A.6.RCD disposition 2 only after its exact claim subject, constructor, endpoint facts, and preservation facts are recoverable; otherwise return A.6.RCD's exact missing-substrate or missing-governor result. When the same predicate must be reused across cases, apply A.6.RCD's reusable predicate-definition branch. If a downstream use instead needs comparison occurrences with their own identity and no relation kind has been admitted, return `missing-governor[mechanism-comparison-occurrence]`; a label such as *refinement* or the adjective *direct* does not fill that gap.

In every branch, identify the exact endpoint mechanism epistemes, their effective `U.ReferenceScheme` values, claim scope, comparison predicate, and preserved and changed semantic content. Changed C.2.1 identity discriminators identify another episteme. If historical continuation matters to the comparison or receiving use, test the separate `EpistemeEditionRelation(earlierMechanismEpisteme, laterMechanismEpisteme)` under C.2.1. The two endpoint epistemes remain distinct participants; refinement, extension, equivalence, a shared name, or a later date establishes neither that relation nor one continuing episteme.

**Continuing revision and replacement contrast.** `FixtureSelectionMechanism-R2` has changed claim content relative to `FixtureSelectionMechanism-R1`, so it is another mechanism episteme. In the continuing branch, exact revision work, source use, method semantics, and change facts satisfy C.2.1's edition-continuity predicate. `EpistemeEditionRelation(FixtureSelectionMechanism-R1, FixtureSelectionMechanism-R2)` then lets G.11 follow the lineage to the later episteme, but every current application and realization claim is still re-evaluated against R2's own applicability and laws; an R1 realization does not automatically realize R2. In the replacement branch, `FixtureSelectionMechanism-Alt1` has another C.2.1 identity and no obtaining edition relation to R1. Treat it as an independent declaration: carry forward neither R1 currentness nor its realization claims, and compare or select Alt1 only through its own applicability and an exact comparison predicate.

`transport` is not a generic A.6.1 mechanism relation. If the current question is cross-context `SchemeSenseCell` correspondence, use one exact F.9 Bridge and infer neither mechanism identity nor equivalence from it. A changed effective reference scheme identifies another episteme; changed `CHR:ReferencePlane` or model-use organization returns to its direct owner. Compare mechanism content only after those exact endpoints and relations have been recovered.

Quotient, product, categorical morphism, and similar constructions are mathematical-lens claims under C.29 when they are current. The lens states which mechanism content is preserved and lost. Mathematical notation does not create an application, binding, realization occurrence, or mechanism U-kind by form.

#### A.6.1:4.9 - Keep description, representation, and publication separate

`U.Mechanism` is already an episteme. A second episteme that explains, summarizes, or compares it is a C.2.1 meta-description whose `EntityOfConcernRef` identifies the mechanism episteme. A diagram, equation set, program, or table is a representation governed by A.6.3 and A.6.3.RT when representation transition matters. An E.24.PUB publication relation makes one selected episteme edition available; an information-carrier relation may carry that publication, but neither relation becomes the mechanism episteme.

A grouping of several mechanism epistemes and realizations may be selected as a `U.Structure` or shown through a `U.View` when that structure or view is current. The grouping does not admit another root kind by itself.

#### A.6.1:4.10 - Use progressive explicitness

Use five degrees of explicitness:

1. A direct sentence names one operation and its condition clearly enough for present work.
2. A `U.Signature` is identified when reusable vocabulary, laws, or applicability matter.
3. A `U.Mechanism` is identified when reusable operation and admission semantics matter.
4. One particular application and its exact argument or result bindings are identified only when a downstream claim asserts that the application occurred or that one exact value participated or was returned.
5. A mechanism-realization relation occurrence is explicitly individuated only when another claim relies on that occurrence identity.

These are thresholds of explicitness, not an executable continuation. If a use needs condition-governed entries, branches, returns, or stops, A.22.CGUS governs that structure.

#### A.6.1:4.11 - Change the exact object that changed

When mechanism content, `EntityOfConcernRef`, or the effective `U.ReferenceScheme` changes, identify another `U.Mechanism` episteme under C.2.1. A changed operation, argument or result declaration, application predicate, application identity or extent rule, law, admission predicate, applicability claim, or relied-on dependency therefore changes the declaration episteme when its semantic content changes.

Call that later episteme an edition of an earlier mechanism episteme only when the exact C.2.1 `EpistemeEditionRelation` obtains. With that relation, G.11 may follow the lineage to discover the later declaration and then re-evaluate its applicability, applications, bindings, and realizations. Without it, keep the later declaration as a non-continuing replacement and open those current-use and realization questions independently. A shared label, refinement claim, later publication, or changed filename supplies no continuity.

A new particular application or binding, new realizer, failed evaluation, new evidence item, changed work occurrence, returned value, or new publication does not change the mechanism episteme by itself. Repair that neighboring object and the affected relation. Reconsider the declaration only when the change overturns relied-on mechanism-content semantics.

Use E.20 when introducing a new mechanism declaration or changing the governing assignment of mechanism semantics. Use G.11 when the question is currentness, freshness, selection of a continuing later episteme, or decay of a relied-on declaration or cited source episteme.

