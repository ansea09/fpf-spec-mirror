---
chunk_kind: "child"
pattern_id: "B.1.5"
pattern_title: "Gamma_method - Order-Sensitive Method Composition and Work Enactment"
section_id: "B.1.5:4"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/B.1.5/B.1.5__005_solution.md"
commit_sha: "4e277189a17b8f9bd3dcdda5df58623d9085ede9"
heading_path:
  - "B.1.5 — Gamma_method - Order-Sensitive Method Composition and Work Enactment"
  - "B.1.5:4 — Solution"
line_start: 42234
line_end: 42421
dependencies:
  - "A.1"
  - "A.15"
  - "A.15.1"
  - "A.15.2"
  - "A.2"
  - "A.2.1"
  - "A.22"
  - "A.22.CGUS"
  - "A.3.1"
  - "A.3.2"
  - "A.6.0"
  - "A.6.RCD"
  - "A.6.REL"
  - "B.1"
  - "B.1.4"
  - "B.1.5"
  - "B.1.6"
  - "B.2"
  - "B.3"
  - "C.13"
  - "C.2.1"
  - "E.10"
  - "E.24"
  - "E.24.PUB"
  - "E.24.UK"
  - "F.6"
  - "G.5"
  - "U.Signature"
  - "U.Work"
keywords:
  - "A.6.RCD claim disposition"
  - "assurance hooks"
  - "capability continuity"
  - "composite-Method boundary account"
  - "method composition"
  - "method relation structure"
  - "method/work granularity"
  - "methodPartOf"
  - "order-sensitive method"
  - "submethod"
  - "typed join"
  - "work enactment"
---

### B.1.5:4 - Solution

A.3.1 first identifies the exact candidate `U.Method` and every exact part method. B.1.5 does not create their `U.Method` membership. It asks the narrower question: do these already identified methods, contributions, constraints, and boundary decisions warrant the claim that the candidate Method is composite?

Start with the smallest useful composition claim:

1. Name the same exact A.3.1 candidate Method and exact A.3.1 part methods.
2. In ordinary domain language, state the candidate's reusable whole action, what each part contributes, and the order, guard, adapter, or join condition that the whole action actually needs.
3. For every whole-forming statement other than B.1.5's narrow `methodPartOf`, use A.6.RCD's lightest sufficient disposition: an existing direct predicate, a local compound claim, or a reusable predicate-definition episteme. A convenient edge label is not a relation-kind admission.
4. Add stable relation-occurrence identity, typed declarations, publication, or assurance only when a named dependent use consumes that extra result. Submit any relation-kind candidate to the exact E.24/E.24.UK admission predicates rather than admitting it here.
5. If the whole action, boundary, contribution, or reidentification rule is still missing, stop the composite claim. Retain any independently supported description, plan, structure, or other result under its subject pattern.

**Minimal positive.** `BuildAndVerifyPumpUnit` is already an exact A.3.1 Method. Its construction rule requires frame assembly, motor installation, connector adaptation when the installed connector does not meet the test precondition, and functional testing; installation and any required adaptation must finish before testing, and adapter failure stops the whole before test. These plain claims, exact `methodPartOf` facts, and the whole identity rule can warrant the composite-method qualification without minting one relation kind per arrow.

**Discriminating non-composite.** `AssessVitals`, `ClassifyUrgency`, and `RouteToCare` can support readable result-to-precondition and guarded-dispatch claims while still lacking one reusable whole action, complete boundary, and whole reidentification rule. Keep those claims local and do not call their organization a composite Method. Select an A.22 `U.Structure` only if a real receiving use needs a load-bearing selected organization.

When a receiving use relies on the composition account—for example, planning, Method substitution, or assurance—check the complete questions below. They guide reading; they do not declare a schema or relation signature.

```text
Composite-method qualification:
  candidate whole method: one exact U.Method already identified under A.3.1
  part methods: a non-empty set of exact U.Method values already identified under A.3.1
  method-part occurrences defined in B.1.5: methodPartOf(part method, whole method)
  other whole-forming claims and constraints:
    exact order, independence, guard, iteration, fallback, adapter, and join meanings used here
    each closed at A.6.RCD's lightest sufficient disposition
  whole semantics:
    generic participants, applicability, preconditions,
    intended effects or preserved conditions, invariants, bounds,
    accepted inputs and outputs, failure and stop conditions
  boundary decisions:
    exposed, forwarded, and encapsulated interactions
  identity and reidentification:
    what keeps this whole the same and what identifies another method
  enactment boundary:
    exact U.Work may enact the method only through A.15.1 enactsMethod
  other independently supported results if composition is incomplete:
    for example, a description, plan, selected structure, selector result, or Work claim
    use A.15.4 when reliance on appearance needs repair
```

#### B.1.5:4.1 - Recover Parts Before Composition

Do not start from the word "step". Start from the object claim.

An apparent step can be:

- a `U.Method` submethod;
- a description constituent inside `U.MethodDescription`;
- a plan item inside `U.WorkPlan`;
- a dated `U.Work` occurrence or work part;
- an order, fallback, or selector claim among independently identified objects;
- a mathematical or representation lens over selected relations;
- mechanism or formal-substrate material;
- quoted wording that does not yet carry a method claim.

Only an independently identified `U.Method` can be a method part; keep the other objects under their own patterns.

B.1.5 directly governs `MethodPartOfRelation`, expressed in Plain register as `methodPartOf(partMethod, wholeMethod)`. Both participants are exact `U.Method` values already identified under A.3.1. The predicate obtains exactly when the whole Method's stable construction rule names the part Method as a required contributor or as an admitted alternative for a required contribution, and that contribution participates in the whole's reusable action. It establishes neither A.14 structural-component parthood, a work part, nor a transformation part.

One `methodPartOf` occurrence is determined by the ordered pair `<part Method, whole Method>`. Every bounded alternative already admitted by the whole's construction rule can stand in `methodPartOf` at the same time; dated Work selecting one alternative does not start, end, or recur the other occurrences. For the same two exact Methods, the relation is atemporal: there is no silent cessation and later recurrence. If the construction rule changes so that a part is newly admitted or no longer admitted, the composite Method must be reidentified or the claim remains unresolved; reidentifying either participant gives another pair. This is why the participant pair is sufficient for the narrow family defined in B.1.5 even when actual enactments vary.

The same part Method may also stand in `methodPartOf` relations to several different whole Methods. Test every pair against the construction rule of its own whole. Each whole keeps its own reusable action, applicability, boundary, constraints, interfaces, accepted variations, and reidentification rule. One supported pair says nothing about another and creates no unique containing Method, discipline-wide whole, kind inheritance, transitivity, fusion, or common-whole closure.

A source label, list membership, diagram containment, shared name, registry entry, description membership, plan position, or work decomposition does not make `methodPartOf` obtain. When the test fails, keep the apparent step under its subject pattern and do not add a negative part merely to complete a diagram.

#### B.1.5:4.2 - Test The Composite-Method Qualification

First identify the exact candidate Method under A.3.1 from its reusable action, participant meanings, applicability, preconditions, intended result or preserved condition, bounds, and failure or stop conditions. If that Method cannot yet be identified, require A.3.1. B.1.5 then tests whether already identified part Methods and exact whole-forming facts justify calling that same candidate a composite Method; it does not create the candidate's Method identity.

State each whole-forming fact in ordinary domain language before choosing its representational or ontological disposition. The words *serial*, *parallel*, *guarded*, *iterative*, *fallback*, *adapter*, and *join* do not settle the claim by themselves.

| Composition cue | What the current claim must let a practitioner decide |
| --- | --- |
| serial | which earlier and later Methods participate in which whole, and which accepted result or preserved condition of the earlier Method must satisfy which precondition of the later Method before continuation |
| parallel | which branch Methods may proceed without a mutual order, the independence condition, and the exact join condition that must hold before the whole continues |
| guarded choice | which alternative Method is selected, the exact selection condition, what happens when no guard or several guards hold, and which whole contains that choice |
| iteration | which part Method repeats, what establishes another iteration, and the exact stop or failure condition |
| refinement or substitution | which Method may replace which other Method, for which use, and which whole semantics, joins, and exposed interactions must remain invariant |
| fallback or dispatch | which primary and alternative Methods are involved, the exact trigger for using the alternative, and whether the statement belongs to this whole or only to a selector registry |
| adapter or typed join | which upstream result meaning satisfies which downstream precondition, which adapter Method or governed correspondence is needed when those meanings differ, and which condition or failure route governs continuation |

Before using a first–then or vertical list as Method architecture, make both checks.

1. **Preserve real order.** Ask what must finish or become true before another Method can start or continue. Name the Methods, the required result or condition, any join or adapter, and the failure or stop route. Keep a genuine first–then result as an unfolding or order claim; its position does not make it a subject level.
2. **Test simultaneous contribution.** Choose a representative working situation and ask whether several Methods contribute without forming one before-after chain. They may be enacted in one Work whole or in overlapping Work occurrences. When asserting particular dated occurrences, identify those Work individuals and their obtaining A.15.1 enactment relations. Co-occurrence alone establishes no Method part, composite Method, Work part, or level.

Both answers may be true. A Method can contain a real ordered segment while other Methods contribute during the same broader Work. The source's reading order and the fact that several Methods are used together decide neither which Methods are parts of one whole nor whether any level exists.

Then use A.6.RCD. Reuse an existing direct predicate when one already governs the needed claim. Otherwise stop at a local compound claim when it closes this use, or publish a reusable predicate-definition episteme when several uses need the same rule. Continue to a relation-kind candidate only when a named receiver needs stable occurrence semantics that claim content cannot supply; E.24 and E.24.UK decide admission. A label such as `precedesInMethod` is readable claim language, not admission evidence, and an ordinary composition claim needs no invented occurrence.

Keep definition, signature, kind, and edition distinct. A predicate-definition episteme may independently satisfy ordinary A.6.0 `U.Signature` membership. It is not a `RelationSignature`; that specialization opens only for an admitted relation kind. Changed predicate-definition or signature content identifies another episteme under C.2.1. Treat and connect the two epistemes as editions through `EpistemeEditionRelation` only when C.2.1's historical-continuation test passes: exact source use and the applicable continuation rule identify which claim, EntityOfConcern, and scheme features must be preserved or may deliberately change, and the current facts satisfy that rule. Revision or supersession Work, Method, provenance, and change facts are evidence for this test; no label establishes continuity. Otherwise the later episteme is a non-continuing replacement. The changed content triggers review of dependent claims; it does not by itself prove another relation kind or relation occurrence. If a relation kind is independently admitted, its direct pattern or declaration defines applicability and occurrence identity, while current case facts establish obtaining, continuation, or cessation where relevant.

When the receiving use needs to combine order information, apply B.1.4 to the selected inputs, actual combining rule, and required order, join or independence conditions. State the `OrderSpec`, the required ordering over the identified positions, in adequate prose or the representation consumed by the receiver; identify each claimed relation occurrence under its own predicate. An adequate explanation or existing account may suffice. Materialize a separate aggregation record only when the receiver needs it. The account and optional notation describe the composition facts; they add no Method identity discriminator and make no relation obtain.

The composite-method qualification holds only when the candidate Method also has its own reusable semantic action, generic participant meanings, applicability, preconditions, intended effects or preserved conditions, invariants, bounds, accepted inputs and outputs, failure and stop conditions, and interface decisions. Its identity includes the exact part Methods and construction architecture on which those semantics depend. Cite an effective reference scheme or claim scope only when its variation changes a Method meaning or the use of a claim about that Method; neither is a generic container.

State the reidentification rule with the qualification. The same exact candidate continues through only those parameter changes, reorderings, or part substitutions that its A.3.1 identity rule already permits while preserving the whole action, applicability, preconditions, intended result or preserved condition, bounds, required joins, and interface boundary. A change outside those permitted variations identifies another `U.Method`. Use B.2 when a separate higher-level reidentification or emergence claim is current; a B.2 label is not needed to state an ordinary B.1.5 rule.

#### B.1.5:4.3 - Keep Order Out Of Structural Mereology

Source cues such as `SerialStepOf`, `ParallelFactorOf`, guarded choice, iteration, fallback, adapter, and typed join call attention to possible whole-forming claims. They are not admission evidence, they need not become relation kinds, they are not A.14 component parthood, and they do not make `methodPartOf` obtain by themselves.

Use A.14 for structural parts of a holon, C.13 for their construction account when needed, and B.3.5 when the additional assurance profile is elected. Use B.1.5 for the contribution of reusable ways of doing to a larger reusable way. A project may need both claims; each retains its own participants and truth conditions.

B.1.4 can supply an order aggregation, partial-order test, or join/independence account. Recover the selected inputs and combining rule, including the required ordering specified by `OrderSpec`; B.1.5 still decides whether the Methods and their construction facts constitute one composite `U.Method`.

When the current claim is a proper temporal restriction of one unchanged non-Work carrier, apply that subject's direct identity rule and A.14/B.1.4 rather than B.1.5. For MethodDescription history, compare the C.2.1 identity triples and assert `EpistemeEditionRelation` only when its historical-continuation predicate obtains. For Work intervals, episodes, performed parts, retries, resumptions, or later occurrences, apply A.15.1's exact relations; generic `PhaseOf` is not their substitute. A temporal boundary becomes a B.2-family question only when a separate whole-reidentification, closure, or supervision claim remains. Order, temporal restriction, episteme edition, Work segmentation, structural parthood, method composition, and whole reidentification remain different claims even when one source diagram uses one line for all of them.

#### B.1.5:4.4 - Expose The Composite Method Interface

The candidate Method's reusable action includes a boundary decision for each interaction:

- **exposed:** a caller system may rely on the interaction as part of the whole Method;
- **forwarded:** a caller system may address an internal submethod interaction through a declared designation or adapter;
- **encapsulated:** the interaction is internal and cannot be relied on from outside the whole Method.

An exposure decision contributes to Method identity whenever changing it changes the reusable action or its admissible boundary. That identity consequence does not wait for an outside party to rely on the Method. A named caller, planner, auditor, substituting-method selection use, or assurance use instead determines when the decision must be stated explicitly or published for reuse. Name the interaction, precondition, result or preserved condition, failure route, and any adapter needed for each exposed or forwarded case.

##### B.1.5:4.4.1 - Composite-Method Boundary Account and Publication Form

State the boundary decisions in clear sentences: what a caller may request, what it must supply, what result or preserved condition it may rely on, and what stops the interaction. Name any needed adapter, order condition, bound, or assurance limit. Explain an encapsulated interaction when a plausible caller could otherwise rely on it. This can complete an internal boundary account.

When a receiver needs the published account, say which MethodDescription edition is available, to which declared audience, for which bounded use, through which expression and carrier. A.3.2 and C.2.1 identify the description; E.24.PUB supplies the publication relations and their progressive explicitness. Name a reusable *boundary-account form* only when its arrangement rules matter. The form, its conforming expression and the carrier retain separate identities.

For disputed availability or publication identity, recover E.24.PUB's five participants `<description edition, audience declaration, bounded-use declaration, expression, carrier>`, its supporting expression and bearing relations, and the maximal continuous availability interval. If form conformance is used, the same expression must support the form-mediated claims. Publication activity is separate; identify dated publication Work only when that occurrence is asserted. Names and links retain their own designation meaning.

Optional prompts for the receiving account:

- the described Method and the description edition used;
- exposed and forwarded interactions, accepted input meanings, preconditions, intended results or preserved conditions;
- required invariants, failure routes and stops;
- order or join conditions, adapters and applicable bounds that affect the receiver's use;
- the audience and bounded use when the account is published.

Use an existing adequate account without adding a form. These presentation prompts supply no Method parts or composition facts.

#### B.1.5:4.5 - Keep Method Qualification And Work Occurrence Separate

B.1.5 evaluates and grounds the composite-method qualification of an exact `U.Method` already identified under A.3.1. A separately constituted `U.MethodDescription` may state that composition claim. Neither object creates performed Work.

One dated `U.Work` occurrence enacts one exact `U.Method` only when the A.15.1 method-enactment relation obtains. Recover each exact actual performer through A.13; A.15.1 then independently identifies the Work, time, containing System, and enacted Method. F.6 enters only when the Method-enactment account also consumes precise assignment-bound attribution through the same obtaining A.13 assignment; missing or failed F.6 alone leaves independently grounded Work and enactment intact. If the same finding invalidates a premise consumed by A.13 or A.15.1 admission, recheck that premise and its dependent conclusions while preserving independently grounded history and relations. The performing System acts under the recovered relations. An assertion or occurrence description may cite those facts and the MethodDescription used.

Parameter bindings, affected referents, resource use, telemetry, retries, results, actual transformations, production, evidence, evaluation, delivery, and acceptance remain separate objects and direct relations under their own governors. They do not become method parts, method identity fields, or generic Work outcomes merely because a report places them beside the Work.

The composition link is not one-to-one. A Work occurrence may enact the whole method without exposing every submethod as a separate work part. An exact A.15.1 `TemporalPartOf_work` may enact the same whole method during its selected interval. An A.15.1 episode may span several method factors, repeat one factor, or be split by evidence policy without changing the method identity. Conversely, a work part does not establish a submethod. A work part enacts a submethod only when that submethod is already an independently identified `U.Method` and a separate `enactsMethod(workPart, submethod)` occurrence obtains.

**Reader check.** Before saying that a work part enacts a submethod, name both sides:

- the occurrence-side object: parent `U.Work`, obtaining work-part relation, interval or boundary, and exact performer System recovered through A.13; only when this reader check expressly consumes precise assignment-bound attribution, also name the exact covering A.2.1 assignment and obtaining F.6 relation; add any separately obtaining resource or evidence relation only when used;
- the method-side object: exact A.3.1 submethod, `methodPartOf` occurrence, whole-forming claim at its A.6.RCD disposition, preconditions, intended result or preserved condition, interface boundary, and whole-Method identity;
- the cross-side fact: the exact `enactsMethod(workPart, submethod)` occurrence.

If one of these grounds is missing, leave that claim unresolved while retaining the independently supported claims. A Work part and a submethod each need their own grounds. Keep a method-description node, evidence segment, mechanism material, system-component behavior, or `A.15.4` appearance-based reliance repair request under its subject pattern.

For an ordinary working question—what larger work is being done through this action now—use **B.1.5.EW**. It recovers the constitutive connections at the needed grain and shows how a changed encompassing condition changes the action. An ongoing whole need not be completed, and its constituents need not all act at once. When changing a constituent for use in one or several wholes, **B.1.5.RS** follows the change through their entry conditions, interactions and required results. The qualifications above still decide the corresponding Method and Work claims.

##### B.1.5:4.5.1 - Planning And Performed-Work Obligations

B.1.5 has three common use positions, but they are positions in use, not U-kinds:

- **Planning or description-side use.** To plan enactment, recover the Methods, `methodPartOf` facts, other whole-forming claims at their A.6.RCD dispositions, needed order and joins, interface boundary, invariants, and whole-level commitments. A resulting `U.WorkPlan` uses A.15.2 and may cite the MethodDescription edition on which it relies. Identify dated planning Work under A.13 and A.15.1 only when that occurrence is asserted; planning and its product remain separate from Method identity.
- **Performed-work use.** Recover each exact actual performer through A.13, let A.15.1 independently admit the Work, and recover the exact `enactsMethod` occurrence for the whole Work. Add the exact covering A.2.1 assignment and F.6 relation only when this use expressly consumes precise assignment-bound attribution; missing or failed F.6 alone leaves independently grounded Work and enactment intact. If the same finding invalidates a premise consumed by A.13 or A.15.1 admission, recheck that premise and its dependent conclusions while preserving independently grounded history and relations. Check capability fit or admission only when the work-entry decision consumes those claims; then check preconditions, order conformance, and exposed or forwarded interactions through their subject patterns. State resource use, evidence, and results only through their own obtaining relations. None becomes part of the method.
- **Assurance use.** Identify cutset submethods, fragile typed joins, adapter points, mapping congruence or CL-sensitive edges, and the envelope or scope in which the composite method is expected to hold. B.3 and related assurance patterns evaluate those hooks; B.1.5 only makes them visible.

Useful invariants remain: a single recovered submethod composed alone does not create a surprising new Method; order is deterministic only under the exact order claims and conditions at their selected A.6.RCD dispositions; any throughput or quality bound must name its characteristic, critical path, and weakest-link basis; a claim that improving a submethod, adapter, or typed join improves the composite must name the characteristic and conditions under which that improvement transfers.

##### B.1.5:4.5.2 - Stop Before Transformation Composition

Method composition and Work decomposition establish no `U.Transformation` part, composite transformation, transformation atomism, or `TransformationPartOfRelation`. Even when several method parts address the same referent and one Work enacts the whole method, identify each actual transformation independently under A.3.4. If a claim needs transformation composition and no direct transformation-composition governor supplies its participants, obtaining rule, and occurrence identity, return `missing-governor[transformation-composition]` for the proposed whole and independently identified changes. Do not infer either composition or indivisibility from the gap.

#### B.1.5:4.6 - Select A Structure Below The Whole-Method Threshold

When the organization itself answers a needed question, use A.22 to select a `U.Structure` over independently identified Methods and obtaining relations. State its four identity discriminators: constituents, selected relation occurrences, applied constraints, and use frame. Ordinary prose or an existing adequate description can supply them. A deliberately asserted dated selection Work needs its own A.13/A.15.1 grounds; add an operation binding or result episteme when the receiving claim needs one. A local comparison can also suffice without selecting a structure. `MethodRelationStructure` is a local designator for a selected structure, not a new U-kind.

Typical cases:

- a fallback registry selects among alternatives but supplies no whole method;
- a workflow diagram relates method descriptions but does not recover method parts;
- a method family has independently governed refinement, substitution, or dispatch relations;
- a graph or algebra represents selected method relations as a lens;
- the same method labels occur under different effective reference schemes, while the local senses have not been resolved and any F.9 Bridge would establish only sense correspondence, not method identity;
- a work plan orders tasks but does not define one reusable method.

The selected structure is a dependent organization for its named use. It does not create its constituents or relations, become a Method, or supply holonhood. Conversely, the internal construction of one exact Method whose composite qualification has been established does not become a second generic structure merely because a diagram can display it. Select a `U.Structure` only when that organization itself changes the next question or action.

A selected structure is useful when the question concerns relation organization and does not require a composite Method.

