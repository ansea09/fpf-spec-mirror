---
chunk_kind: "child"
pattern_id: "B.1.5"
pattern_title: "Gamma_method - Order-Sensitive Method Composition and Work Enactment"
section_id: "B.1.5:4"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/B.1.5/B.1.5__005_solution.md"
commit_sha: "7205ce8cea50eb778520a026373b2b7bcbc43fbb"
heading_path:
  - "B.1.5 — Gamma_method - Order-Sensitive Method Composition and Work Enactment"
  - "B.1.5:4 — Solution"
line_start: 36434
line_end: 36623
dependencies:
  - "A.1"
  - "A.15"
  - "A.15.1"
  - "A.15.2"
  - "A.22"
  - "A.3.1"
  - "A.3.2"
  - "A.6.0"
  - "A.6.1"
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
  - "C.29"
  - "E.10"
  - "E.20"
  - "E.24"
  - "E.24.PUB"
  - "E.24.UK"
  - "G.5"
  - "U.MethodDescription"
  - "U.PresentationCarrier"
  - "U.Signature"
  - "U.Structure"
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
5. If the whole action, boundary, contribution, or reidentification rule is still missing, stop the composite claim and keep the useful lower object under its subject pattern.

**Minimal positive.** `BuildAndVerifyPumpUnit` is already an exact A.3.1 Method. Its construction rule requires frame assembly, motor installation, connector adaptation when the installed connector does not meet the test precondition, and functional testing; installation and any required adaptation must finish before testing, and adapter failure stops the whole before test. These plain claims, exact `methodPartOf` facts, and the whole identity rule can warrant the composite-method qualification without minting one relation kind per arrow.

**Discriminating non-composite.** `AssessVitals`, `ClassifyUrgency`, and `RouteToCare` can support readable result-to-precondition and guarded-dispatch claims while still lacking one reusable whole action, complete boundary, and whole reidentification rule. Keep those claims local and do not call their organization a composite Method. Select an A.22 `U.Structure` only if a real receiving use needs a load-bearing selected organization.

When a caller system, planner system, substituting-method selection use, auditor, or assurance use needs a reliance-bearing account, check the complete coordinates below. This is a reading checklist, not a schema, record, `RelationSignature`, or set of `SlotSpec`s.

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
  lower disposition if construction is incomplete:
    selected U.Structure | U.MethodDescription | U.WorkPlan | U.Work |
    G.5 selector | lens | A.15.4 appearance-based reliance repair request
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

Only the first case can be a method part. Do not mint `U.StepSpec`, `U.StepMethod`, `U.MethodStep`, or `U.MethodAlgebra` for the others.

B.1.5 directly governs `MethodPartOfRelation`, expressed in Plain register as `methodPartOf(partMethod, wholeMethod)`. Both participants are exact `U.Method` values already identified under A.3.1. The predicate obtains exactly when the whole Method's stable construction rule names the part Method as a required contributor or as an admitted alternative for a required contribution, and that contribution participates in the whole's reusable action. It establishes neither A.14 structural-component parthood, a work part, nor a transformation part.

One `methodPartOf` occurrence is determined by the ordered pair `<part Method, whole Method>`. Every bounded alternative already admitted by the whole's construction rule can stand in `methodPartOf` at the same time; dated Work selecting one alternative does not start, end, or recur the other occurrences. For the same two exact Methods, the relation is atemporal: there is no silent cessation and later recurrence. If the construction rule changes so that a part is newly admitted or no longer admitted, the composite Method must be reidentified or the claim remains unresolved; reidentifying either participant gives another pair. This is why the participant pair is sufficient for the narrow family defined in B.1.5 even when actual enactments vary.

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
| adapter or typed join | which exact adapter `U.Method`, upstream result meaning, downstream precondition, conversion condition, and failure route make the join admissible |

Then use A.6.RCD. Reuse an existing direct predicate when one already governs the needed claim. Otherwise stop at a local compound claim when it closes this use, or publish a reusable predicate-definition episteme when several uses need the same rule. Continue to a relation-kind candidate only when a named receiver needs stable occurrence semantics that claim content cannot supply; E.24 and E.24.UK decide admission. A label such as `precedesInMethod` is readable claim language, not admission evidence, and an ordinary composition claim needs no invented occurrence.

Keep definition, signature, kind, and edition distinct. A predicate-definition episteme may independently satisfy ordinary A.6.0 `U.Signature` membership. It is not a `RelationSignature`; that specialization opens only for an admitted relation kind. Changed predicate-definition or signature content identifies another episteme under C.2.1. Treat and connect the two epistemes as editions through `EpistemeEditionRelation` only when C.2.1's historical-continuation test passes: an exact system performed revision, refinement, or supersession Work under a Method whose semantics establish continuation, the earlier episteme participated through the exact source-to-revision use, and governed change facts support the claim. Otherwise the later episteme is a non-continuing replacement. The changed content triggers review of dependent claims; it does not by itself prove another relation kind or relation occurrence. If a relation kind is independently admitted, its direct pattern or declaration defines applicability and occurrence identity, while current case facts establish obtaining, continuation, or cessation where relevant.

When several admitted order occurrences must be reviewed together, use B.1.4's `OrderSpec`, exact ordered-relation designations, and join or independence conditions in a separate bounded-use aggregation record. The record and optional `Gamma_ctx` notation neither participate in Method identity nor make any relation obtain. When the order statements remain local claims rather than admitted relation occurrences, compare those claim contents directly and do not pretend that an `OrderSpec` has occurrences to aggregate.

The composite-method qualification holds only when the candidate Method also has its own reusable semantic action, generic participant meanings, applicability, preconditions, intended effects or preserved conditions, invariants, bounds, accepted inputs and outputs, failure and stop conditions, and interface decisions. Its identity includes the exact part Methods and construction architecture on which those semantics depend. Cite an effective reference scheme or claim scope only when its variation changes a Method meaning or the use of a claim about that Method; neither is a generic container.

State the reidentification rule with the qualification. The same exact candidate continues through only those parameter changes, reorderings, or part substitutions that its A.3.1 identity rule already permits while preserving the whole action, applicability, preconditions, intended result or preserved condition, bounds, required joins, and interface boundary. A change outside those permitted variations identifies another `U.Method`. Use B.2 when a separate higher-level reidentification or emergence claim is current; a B.2 label is not needed to state an ordinary B.1.5 rule.

#### B.1.5:4.3 - Keep Order Out Of Structural Mereology

Source cues such as `SerialStepOf`, `ParallelFactorOf`, guarded choice, iteration, fallback, adapter, and typed join call attention to possible whole-forming claims. They are not admission evidence, they need not become relation kinds, they are not A.14 component parthood, and they do not make `methodPartOf` obtain by themselves.

Use A.14, C.13, and B.3.5 when the claim is about structural parts of a holon. Use B.1.5 when the claim is about how reusable ways of doing construct a larger reusable way of doing. The same project may need both, but the relation occurrences and truth conditions remain separate.

Use B.1.4 when a receiving use needs an inspectable order aggregation, partial-order test, or join/independence account. Its `OrderSpec` and optional notation describe already recovered order occurrences; B.1.5 still decides whether those methods and relations construct one composite `U.Method`.

When the current claim is a proper temporal restriction of one unchanged non-Work carrier, apply that subject's direct identity rule and A.14/B.1.4 rather than B.1.5. For MethodDescription history, compare the C.2.1 identity triples and assert `EpistemeEditionRelation` only when its historical-continuation predicate obtains. For Work intervals, episodes, performed parts, retries, resumptions, or later occurrences, apply A.15.1's exact relations; generic `PhaseOf` is not their substitute. A temporal boundary becomes a B.2-family question only when a separate whole-reidentification, closure, or supervision claim remains. Order, temporal restriction, episteme edition, Work segmentation, structural parthood, method composition, and whole reidentification remain different claims even when one source diagram uses one line for all of them.

#### B.1.5:4.4 - Expose The Composite Method Interface

The candidate Method's reusable action includes a boundary decision for each interaction:

- **exposed:** a caller system may rely on the interaction as part of the whole Method;
- **forwarded:** a caller system may address an internal submethod interaction through a declared designation or adapter;
- **encapsulated:** the interaction is internal and cannot be relied on from outside the whole Method.

An exposure decision contributes to Method identity whenever changing it changes the reusable action or its admissible boundary. That identity consequence does not wait for an outside party to rely on the Method. A named caller, planner, auditor, substituting-method selection use, or assurance use instead determines when the decision must be stated explicitly or published for reuse. Name the interaction, precondition, result or preserved condition, failure route, and any adapter needed for each exposed or forwarded case.

#### B.1.5:4.4.1 - Composite-Method Boundary Account and Publication Form

When a named receiver must reuse the boundary account, first identify one exact claim-bearing `U.MethodDescription` episteme under A.3.2 and C.2.1. Its claim content concerns the exact composite Method and states the exposed, forwarded, and encapsulated interactions. Then keep the publication-side objects and designation content below separate.

In B.1.5, *composite-Method boundary account* is the local Plain phrase for this MethodDescription claim content. A *boundary-account form* is the separately identified reusable arrangement used to present that content when publication is load-bearing. Neither phrase creates a new kind or acronym. The separate A.10 instantiation card keeps its different design-time use for Precedes, Choice, Join, guards, and exceptions.

1. A bounded-use-declaration episteme states the operations or decisions supported by this publication, the conditions of that use, and the excluded stronger use.
2. An audience-declaration episteme states the audience criterion. The actual audience consists of entities admitted by that declaration; those entities are not substituted for the declaration episteme as a publication-relation participant.
3. An independently identified reusable boundary-account arrangement is a publication-form participant only while E.24.PUB `PublicationFormExpressionRelation(description edition, boundary-account form, bounded-use declaration)` obtains.
4. A paper card, poster, page, file, or screen must first be identified independently as a physical or digital `U.PresentationCarrier`; E.24.PUB `PublicationFormBearingRelation(carrier, boundary-account form)` then states which form it bears.
5. An actual system performs separate rendering, printing, uploading, indexing, or access-granting publication Work. That Work may establish or restore availability, but it is not the publication occurrence or one of its participants.
6. One `EpistemePublicationRelation` occurrence, with the exact five participants `<description edition, audience-declaration episteme, bounded-use-declaration episteme, boundary-account form, carrier>`, makes the edition available to the declared audience for the declared use throughout its maximal continuous interval of availability. The relation occurrence is not performed by the publishing system, and the boundary-account form does not publish itself.
7. Names, labels, and links that designate the Method or description edition remain separately governed designation content. Neither the form nor the carrier establishes designation merely by displaying similar words.

```text
Reader-facing boundary-account prompts:
  described Method, exact MethodDescription edition, and effective reference scheme when its variation changes the Method meaning or claim use
  named audience criterion and bounded use, including any excluded stronger use, when publication is load-bearing
  exposed and forwarded interactions
  accepted input or call meaning
  preconditions and intended result or preserved condition
  failure and stop routes
  invariants
  exact B.1.4 order aggregation or OrderSpec only when the receiver relies on its order, join, or independence limits
  applicability, bounds, and quality or assurance envelope only when they limit the interaction on which the receiver relies
  adapter, typed-join, and assurance references only when the receiver uses them
  plain rationale for each encapsulated interaction on which misuse is likely
```

These prompts organize presentation; they are not direct-relation `SlotSpec`s, relation participants, Method parts, or a schema that creates a Method. None supplies the world-side `methodPartOf` facts or any other whole-forming claim. For a lightweight internal use, state the few boundary decisions in clear sentences and stop; do not create a description edition, declaration episteme, boundary-account form, carrier, publication Work, or publication occurrence by ritual.

#### B.1.5:4.5 - Keep Method Qualification And Work Occurrence Separate

B.1.5 evaluates and grounds the composite-method qualification of an exact `U.Method` already identified under A.3.1. A separately constituted `U.MethodDescription` may state that composition claim. Neither object creates performed Work.

One dated `U.Work` occurrence enacts one exact `U.Method` only when the A.15.1 method-enactment relation obtains. A.15.1 identifies its performers, time, and containing System; F.6 identifies the assignment under which each System performed it. The System acts and the assignment does not. A short Method-enactment explanation may omit an assignment identifier that no later claim uses. An assertion or occurrence description may cite those facts and the MethodDescription used; the Work occurrence does not store a card or record.

Parameter bindings, affected referents, resource use, telemetry, retries, results, actual transformations, production, evidence, evaluation, delivery, and acceptance remain separate objects and direct relations under their own governors. They do not become method parts, method identity fields, or generic Work outcomes merely because a report places them beside the Work.

The composition link is not one-to-one. A Work occurrence may enact the whole method without exposing every submethod as a separate work part. An exact A.15.1 `TemporalPartOf_work` may enact the same whole method during its selected interval. An A.15.1 episode may span several method factors, repeat one factor, or be split by evidence policy without changing the method identity. Conversely, a work part does not establish a submethod. A work part enacts a submethod only when that submethod is already an independently identified `U.Method` and a separate `enactsMethod(workPart, submethod)` occurrence obtains.

**Reader check.** Before saying that a work part enacts a submethod, name both sides:

- the occurrence-side object: parent `U.Work`, obtaining work-part relation, interval or boundary, performer system, covering assignment, and any separately obtaining resource or evidence relation;
- the method-side object: exact A.3.1 submethod, `methodPartOf` occurrence, whole-forming claim at its A.6.RCD disposition, preconditions, intended result or preserved condition, interface boundary, and whole-Method identity;
- the cross-side fact: the exact `enactsMethod(workPart, submethod)` occurrence.

If any side is missing, lower only that side. Do not repair a missing submethod by inventing a work part, and do not repair a missing work part by inventing a submethod. Keep a method-description node, evidence segment, mechanism material, system-component behavior, or `A.15.4` appearance-based reliance repair request under its subject pattern.

#### B.1.5:4.5.1 - Planning And Performed-Work Obligations

B.1.5 has three common use positions, but they are positions in use, not U-kinds:

- **Planning or description-side use.** A planner system performing planning Work recovers the exact Methods, `methodPartOf` occurrences, whole-forming claims at their A.6.RCD dispositions, any justified order aggregation, typed joins or adapters, interface boundary, invariants, and whole-level commitments. A resulting exact `U.WorkPlan` may cite the MethodDescription edition on which it relies; neither the planning Work nor the plan is the reader that defines Method identity.
- **Performed-work use.** Recover the exact `enactsMethod` occurrence for the whole Work. Check the performer system and covering assignment, plus capability fit or admission only when the work-entry decision consumes those claims; then check preconditions, order conformance, and exposed or forwarded interactions through their subject patterns. State resource use, evidence, and results only through their own obtaining relations. None becomes part of the method.
- **Assurance use.** Identify cutset submethods, fragile typed joins, adapter points, mapping congruence or CL-sensitive edges, and the envelope or scope in which the composite method is expected to hold. B.3 and related assurance patterns evaluate those hooks; B.1.5 only makes them visible.

Useful invariants remain: a single recovered submethod composed alone does not create a surprising new Method; order is deterministic only under the exact order claims and conditions at their selected A.6.RCD dispositions; any throughput or quality bound must name its characteristic, critical path, and weakest-link basis; strengthening a submethod, adapter, or typed join should not make the composite Method worse unless a stated side condition changes.

#### B.1.5:4.5.2 - Stop Before Transformation Composition

Method composition and Work decomposition establish no `U.Transformation` part, composite transformation, transformation atomism, or `TransformationPartOfRelation`. Even when several method parts address the same referent and one Work enacts the whole method, identify each actual transformation independently under A.3.4. If a claim needs transformation composition and no direct transformation-composition governor supplies its participants, obtaining rule, and occurrence identity, return `missing-governor[transformation-composition]` for the proposed whole and independently identified changes. Do not infer either composition or indivisibility from the gap.

#### B.1.5:4.6 - Select A Structure Below The Whole-Method Threshold

Use A.22 when independently identified Methods and already obtaining relations are useful to one question or action but do not construct one whole Method. For an actual load-bearing selection, first name the selecting system, selection Method, dated selection Work and bindings, and any result episteme needed to preserve the decision. Then name all four structure discriminators: exact constituents, exact selected obtaining relation occurrences, applied constraints, and the use frame. For a one-off hypothetical comparison, state the comparison and stop without asserting a selected `U.Structure`. `MethodRelationStructure` may be used as a local readable designator only for an actually selected structure; it is not a U-kind, relation kind, Method holon, or identity field.

Typical cases:

- a fallback registry selects among alternatives but supplies no whole method;
- a workflow diagram relates method descriptions but does not recover method parts;
- a method family has independently governed refinement, substitution, or dispatch relations;
- a graph or algebra represents selected method relations as a lens;
- the same method labels occur under different effective reference schemes, while the local senses have not been resolved and any F.9 Bridge would establish only sense correspondence, not method identity;
- a work plan orders tasks but does not define one reusable method.

The selected structure is a dependent organization for its named use. It does not create its constituents or relations, become a Method, or supply holonhood. Conversely, the internal construction of one exact Method whose composite qualification has been established does not become a second generic structure merely because a diagram can display it. Select a `U.Structure` only when that organization itself changes the next question or action.

This lower object is not a failure. It is the right governed object when relation organization is useful but whole-method construction is not current.

