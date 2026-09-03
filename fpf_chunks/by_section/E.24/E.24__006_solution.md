---
chunk_kind: "child"
pattern_id: "E.24"
pattern_title: "U.Ontic and Ontic Introduction Discipline"
section_id: "E.24:4"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/E.24/E.24__006_solution.md"
commit_sha: "353d59d1c2167344cfff99cadbf413c587c14a66"
heading_path:
  - "E.24 — U.Ontic and Ontic Introduction Discipline"
  - "E.24:4 — Solution"
line_start: 90957
line_end: 91415
dependencies:
  - "A.19.ECS"
  - "A.6.0"
  - "A.6.3"
  - "A.6.5"
  - "A.6.RCD"
  - "A.6.REL"
  - "B.3.5"
  - "C.13"
  - "C.2.1"
  - "C.29"
  - "E.10"
  - "E.10.ARCH"
  - "E.14"
  - "E.17.0"
  - "E.21"
  - "E.24"
  - "E.24.CD"
  - "E.24.PUB"
  - "E.24.UK"
  - "E.8"
  - "E.9"
  - "E.9.DA"
  - "F.18"
  - "U.View"
keywords:
---

### E.24:4 - Solution

The defining `ClaimGraph` located here states `U.Ontic` as the FPF kind for a connected action-facing ontology unit. Before dependent uses rely on that unit, the accepted ontic-introduction decision states its primary subject kind, exact identity, constitution, or recognition rule, the smallest exact relation set needed by dependent use, any identity-bearing direct relation selected by an exact identity assertion, any reusable RelationSignature declarations, rule-content locators, named dependent-use reliance, and non-use boundary.

`Connected` is an admission condition here, not a metaphor. The decision names the smallest set of independently defined relations that makes the subject usable across the named dependent uses and states why each relation belongs. When an exact identity assertion selects one identity-bearing direct relation, say so; otherwise do not invent a head relation. `Action-facing` means that the decision names a dependent use whose outcome changes when that coordination is absent—for example comparison, preservation, teaching, publication, reference, work, or decision use. Topic adjacency and a shared label satisfy neither condition.

Keep two layers explicit:

1. **Instance layer.** For each included direct relation kind, name the actual participant meanings and admitted actual-participant kinds supplied by its exact defining `ClaimGraph`. An obtaining occurrence relates those actual participants; it does not relate their kinds, the relation kind, a pattern, a `RelationSignature`, or the ontology unit.
2. **Ontology and declaration layer.** The ontic-introduction decision episteme states which subject kind, identity rule, relation kinds, declaration epistemes, rule-content locators, and dependent-use reliance claims belong in this ontology unit. Those are typed claims in the decision episteme unless an independently defined declaration-dependency, inclusion, or reliance relation is actually current. Do not call them world-side direct relations merely because the ontology unit coordinates them.

The ontology unit is connected when every included relation kind has its instance-layer participants, exact predicate, and defining `ClaimGraph`, every included declaration is tied to the relation use it declares, and every dependent use names the exact identity rule, direct relation rule, or declaration it relies on. The decision marks any identity-bearing edge explicitly. This typed account establishes ontology-level coordination; it fabricates no relation occurrence among kinds, declarations, pattern descriptions, or the ontic.

Named dependent-use reliance states each dependent use, its pattern-description locator when useful, and the identified ontic identity, direct relation rule, or `RelationSignature` declaration on which it relies. A pattern name without that reliance basis is insufficient.

Reidentify one `U.Ontic` by its primary subject kind, the exact identity, constitution, or recognition rule supplied by its defining `ClaimGraph`, and the minimal relation set selected for dependent use. Include an identity-bearing direct relation only when an exact identity assertion selects one. Only a change to the subject kind, identity rule, or relation set used by a named dependent use can reopen ontic identity; a change in how the subject is described, published, viewed, represented, or named does not. Use the typed object map in `E.24:4.3a` for those neighboring objects.

Keep the subject under decision separate from every means of stating, presenting, or inspecting it. Open a neighboring row in `E.24:4.3a` only when that object's identity or direct relation changes the current choice or receiving use. A decision or description remains a C.2.1 episteme; availability, viewpoint conformance, and mathematical correspondence do not alter the subject's identity.

Keep direct verbs with their exact subjects and predicates: a designator designates, a reference resolves, an episteme contains claim content, a publication occurrence makes one edition available, a publication form expresses it for that use, and a carrier bears the form. The typed map supplies the exact assertion, defining or constraining `ClaimGraph`, pattern locator, and stop for each current object; visible co-occurrence on a card supplies none of them.

When a durable ontic is selected, its branch of the ontic-introduction decision states at least:

- the primary governed subject kind and the named receiving use—such as comparison, preservation, teaching, publication, reference, work, or decision use—for which coherent identity and relation rules matter;
- the exact identity, constitution, or recognition rule supplied by the defining `ClaimGraph`;
- the smallest set of independently defined direct relations needed by named dependent use, with the practical use each relation enables;
- one identity-bearing direct relation only when an exact identity assertion selects it and its defining `ClaimGraph` states participants, predicate, and occurrence identity;
- any `RelationSignature` epistemes used to declare reusable SlotSpecs for relation-participant meanings actually reused;
- the current FPF patterns that define or constrain the subject kind, identity rule, and selected direct relations;
- the pattern that defines or constrains the durable ontic;
- the named dependent-pattern reliance: each dependent pattern and the identified ontic identity, direct relation rule, or `RelationSignature` declaration on which it relies without copying that rule or declaration.

A project entity does not fill an ontic. It keeps its own kind and may participate in the ontic's direct relation or in a neighboring direct relation. A SlotSpec belongs to a `RelationSignature` declaration. An assertion or description episteme may designate the world-side participants by value or reference and claim that the direct predicate obtains. The participant, SlotSpec, designation, assertion, and relation occurrence remain different objects.

FPF ontology is therefore not one flat class list and not a collection of filled records. A durable ontic is one connected ontology unit over a small group of direct kinds and relations, linked at the ontology layer by the typed claims in its decision episteme. At the instance layer, only actual participants enter obtaining direct-relation occurrences. The same project entity may participate in relations governed by several ontics without changing its kind or becoming part of a second ontology.

The accepted decision uses `U.Ontic` because one ontology unit needs stable identity and one exact rule-content locus for relation rules reused by dependent uses. Without it, their descriptions duplicate or disagree about that shared basis. Every other current object retains the exact predicate, subject assertion, and defining or constraining `ClaimGraph` named in `E.24:4.3a`.

The cost is kernel growth and metamodel risk. Repetition, a reusable layout, or ontology-shaped wording does not make any object a `U.Ontic`. Admit one only when the decision supplies stable identity, the minimal relation set actually reused across dependent uses, existing-rule-content checks, and a non-use boundary.

U-kind admission is a neighboring E.24-family question, not the main body of E.24. Both hosts use the one `E24FamilySettlementDecision` schema in `E.24:4.0a`:

- a durable ontic is a connected action-facing ontology unit;
- durable `U.*` kindhood is admitted only through an accepted `UKindAdmissionResult` under that shared schema;
- an ontic may coordinate already admitted kinds, and a new kind may reuse an already accepted ontic settlement;
- when the same case needs both a new ontic and a new public U-kind, one atomic co-decision returns a separate `OnticSettlementResult` and `UKindAdmissionResult`; neither is evidence for the other inside that decision;
- every non-ontic object keeps the kind, relation, exact subject assertion, and defining or constraining `ClaimGraph` selected by the typed object map.

Use `E.24.UK` only when a candidate claims durable U-kind force. E.24 consumes its exact accepted result when that result changes the ontic settlement; naming or placement alone supplies neither output.

#### E.24:4.0 - Constructive Foundation And Math-Lens Boundary

If a reader asks where an FPF ontic gets constructive grounding, follow its exact identity or grounding assertion and defining or constraining `ClaimGraph`. E.24 records a locator for that rule and only the relations needed by dependent use; it does not turn declarations, descriptions, publication objects, views, or representations into grounding participants. Their exact predicates, assertions, and rule-content locators remain in `E.24:4.3a`.

For structural identity claims, the constructive chain is `E.14 -> B.3.5 -> C.13`: Working-Model relation first, declared `validationMode`, `tv:groundedBy`, and a reconstructible `Γ_m.sum`, `Γ_m.set`, or `Γ_m.slice` trace. The `Γ_m` trace is the reconstructible grounding object cited through `tv:groundedBy` under B.3.5. If a graph, tuple, or another mathematical expression represents that trace, the expression is a separate C.29 representation. Neither the trace nor its representation becomes the public relation vocabulary, and this structural grounding apparatus is not required for non-structural ontics.

For a non-structural ontic, use the exact identity, grounding, or recognition assertion and defining `ClaimGraph` located by its direct subject-pattern reference. Open `E.24.UK` only for U-kind admission, C.2.1 only for an episteme's identity, `E.24.PUB` only for current availability, and the other rows of `E.24:4.3a` only when their selection question is true.

`A.14`, `B.2`, and `A.15.1` carry BORO- and CCO-compatible identity and occurrence discipline. They support the constructive foundation; they do not create a separate durable-kind ontology.

Before a dependent pattern relies on the ontic, classify each current object with `E.24:4.3a`. The selection question—not a shared label or visual container—decides whether the object is a world-side participant, relation occurrence, reusable declaration, claim-bearing episteme, publication object, view or representation, source expression, or durable ontology unit.

An encountered card illustrates the rule. Its claims, reusable layout, diagram elements, and carrier are separately governed only when their own identity and direct relation are established; the word `card` identifies none of them and does not make the collection an ontic.

When several current pattern descriptions already contain rule content for the same project concern, select an ontic only if one exact identity rule and minimal relation set must be reused across their dependent uses. Keep every otherwise current object in its `E.24:4.3a` row; shared topic or proximity cannot fuse their kinds. At the ontology layer, state reliance on exact relation rules without inventing an occurrence whose participants are the kind, pattern, or ontic.

Build the decision evidence in this order; do not select a disposition first and then backfill reasons:

1. **Current case and stable decision subject.** State the working expression or source claim, one independently identified pre-judgment candidate entity, proposal episteme, or source-construct entity with its direct identity governor, and the named receiving use. Use that fixed object as the decision episteme's EntityOfConcern. Record source-use status and provenance here when current; they do not settle the ontology disposition.
2. **Existing-governor reuse and non-duplication.** Name the current direct patterns checked by value. State which current claim they already close, or the exact coordination they fail to supply. Reject a new umbrella when it would merely rename those governed objects or copy their rules.
3. **Identity, constitution, or recognition.** State the exact rule supplied by the subject's subject pattern and what would reidentify the subject across the receiving use. Do not replace several required facts with an invented universal relation.
4. **Typed connectivity and dependent use.** Use `E.24:4.3a` to classify only the objects that the dependent use consumes. Name each needed direct relation, its exact predicate and definition source, any identity-bearing relation selected by its occurrence-identity rule, each declaration actually reused, and each dependent assertion's exact reliance basis. Omit every neighboring map row whose selection question is false.
5. **Disposition, branch result, and boundary—fill last.** Keep the decision EntityOfConcern from step 1. From steps 1–4, record exactly one branch payload: the closing assertions and direct patterns; the bounded episteme, its declared use, and stop; the selected ontology-unit individual and subject pattern; or the unresolved reason and missing evidence. Add an explanatory overread only when it passes F.19:4's full independent-ground, plausible-reader, contribution, and smallest-clear-correction test.

A relation-participant meaning belongs in one selected direct relation only when that relation's predicate depends on an actual participant having that meaning and the exact defining `ClaimGraph` states the admitted kind of that participant. When typed reuse is needed, a compatible `RelationSignature` declares that admitted kind as the SlotSpec's `ValueKind`. Another entity remains under its own direct relation when that relation already expresses the needed use. Reuse pressure can justify a `RelationSignature`; it cannot turn a neighboring relation, record field, or mathematical operand into a participant or SlotKind of another relation.

Optional-in-use status belongs to a declaration or description. It does not mean that a world-side relation occurrence has an unfilled participant. A missing designation leaves the assertion incomplete or the participant unknown to the current user. It does not show that the participant is absent, and it does not make the direct predicate obtain or cease.

Not every ontic needs every map row. Open one only when its selection question changes the named receiving use; otherwise omit it and keep the object under its subject pattern.

Keep annotation proportional. E.24 calls for recovery only where wording can change ontic identity, a direct relation, participant meaning, a reusable SlotSpec declaration, a description claim, admissible use, or the reliance basis of a dependent pattern. If readable domain prose already preserves those objects, do not replace it with declaration syntax merely to show that an ontic exists.

This differs from pure ontology engineering because FPF patterns are written for action: they may define or constrain a kind or predicate, state an admission test, frame a judgement, or give practical guidance. That does not make every pattern episteme a `U.MethodDescription` or every subject a `U.Method`. An engineer-manager uses the applicable claims and guidance to decide what can be done, claimed, relied on, repaired, compared, or stopped. If the current claim says that an E.24 episteme describes an ontic-introduction Method, apply A.3.1 and A.3.2 to identify that Method and show that the episteme substantively describes how it is done. The accepted ontic-introduction decision supplies the object discipline for those practical choices; the pattern text itself performs no action.

Precision restoration uses the same discipline without turning it into lexical style. First recover the source-side entities, direct relations, assertions, descriptions, and defining or constraining `ClaimGraph` sources compressed by the wording. Then repair toward a current FPF ontic only when one accepted ontic-introduction decision states how those objects are coordinated. If no such ontic exists, state the exact subject assertions, cite their pattern-description locators, keep only the needed claims in a bounded local episteme under C.2.1, or open an E.24 ontic-introduction decision.

When a source expression opens the ontic-introduction question, preserve its source-to-use path independently of the ontology disposition. Name the exact expression and its source episteme; name the source publication occurrence when availability through that occurrence matters; recover the entities, relations, and claims actually carried forward; and set the source-use status to quote-only, reduced use, or one selected stronger use with the smallest condition that licenses it. Keep that trace beside a durable-ontic, bounded-episteme, or direct-use disposition whenever both are current. If no governed payload has been selected, mark the ontology disposition unresolved and retain source-only inquiry material rather than treating provenance as an ontology answer. When a stronger-use condition occurs, reopen the source expression through `C.2.P` or the direct source-use pattern instead of treating the repaired noun as a substitute for the source relation.

When an `E.10.ARCH` wording-use restoration row opened the case, retain its four coordinates inside that source-to-use trace: `semanticAreaBaseConcept` is the source cue, `semanticArea` is the selected Part-F row or bounded row-set, `semanticAreaSenseFamily` prevents theme-level overgeneralization, and `ontologicalNeighborhood` is the applicability neighborhood used to recover the subject kind, relations, and subject patterns. These are coordinates of the wording repair under E.8 and E.10.ARCH. They are not components or identity criteria of `U.Ontic`; a subject discovered directly through engineering work does not need them.

The defining `ClaimGraph` located at E.24 states the admission conditions for `U.Ontic`, and E.24 gives practical guidance for the decision. The ontology unit, its identity rule, selected direct relations, declarations, claim-bearing epistemes, publication occurrences and forms, carriers, views, and representations remain distinct. Self-use does not establish a `U.MethodDescription`; apply A.3.1 and A.3.2 only when a separate Method and MethodDescription claim matters.

#### E.24:4.0a - Shared E.24-Family Settlement and Atomic Co-decision

E.24 and E.24.UK use this one schema without weakening or restating it differently. `MinimalGovernedRelationSet` means the smallest independently defined direct-relation rules needed by named dependent use. It does not require one universal head relation. `IdentityBearingDirectRelationIfSelected` is filled only when an exact identity assertion under its defining `ClaimGraph` selects such a relation; otherwise it is explicitly `none`.

```text
E24FamilySettlementDecision:
  DecisionEpistemeIdentity:
    ClaimGraph:
    EntityOfConcern: one independently identified pre-judgment candidate entity, proposal episteme, or source-construct entity; unchanged by the disposition.
    EntityOfConcernIdentityGovernor:
    EffectiveReferenceScheme:
  CandidateInputs:
    ReceivingUseAndVisibleResult:
    PrimaryGovernedSubjectKind:
    SubjectIdentityConstitutionOrRecognitionRule:
    CandidatePublicSpellingIfAny?: naming pressure only; it establishes neither the governed object nor admission.
    ProposedDurableUKindIfAny:
      GovernedIndividuals:
      DurableMembershipRuleAndReferenceScheme:
      IntendedExtentAndNonMemberBoundary:
      RootInclusionImplicationIfSameIndividualDependent?:
      ExactDependenceRelationAndDiscriminatorsIfIdentityDependent?:
    ExistingGovernorAndNonDuplicationResult:
    MinimalGovernedRelationSet:
      DirectRelationKind:
      ParticipantMeaningsAndAdmittedActualParticipantKinds:
      ObtainingAndOccurrenceIdentityRule:
      DirectGovernor:
      DependentUseEnabled:
    IdentityBearingDirectRelationIfSelected: exact direct relation entry | none.
    ReusableDeclarationsActuallyConsumed:
    NamedDependentPatternReliance:
    NonUseBoundary:
    ReopenCondition:
  Outputs:
    OntologyDispositionResult?:
      Disposition: subject-pattern-use | bounded-local-episteme | durable-ontic | unresolved-stop.
      DirectUseResult?:
        ExactClosingAssertionRefs:
        DirectPatternLocators:
      BoundedEpistemeResult?:
        BoundedEpistemeRef:
        DeclaredUseAndStop:
      DurableOnticResult?:
        OnticSettlementResultRef:
        SelectedOnticRef:
        OnticSubjectPatternLocator:
      UnresolvedResult?:
        UnresolvedReason:
        MissingEvidenceOrRuleRefs:
    OnticSettlementResult?:
      OnticSettlementResultRef:
      SelectedOnticRefOrBootstrapSchemaRef:
      PrimaryGovernedSubjectKind:
      SubjectIdentityRule:
      MinimalGovernedRelationSet:
      NamedDependentPatternReliance:
      NonUseAndReopenBoundary:
    UKindAdmissionResult?:
      UKindAdmissionResultRef:
      AdmissionDisposition: root | same-individual-dependent | identity-dependent | reuse | local-kind | reject.
      SubjectPatternLocator:
      DurableMembershipAndExtentResultIfPositive?:
      BranchSpecificResultRef:
      NonUseAndReopenBoundary:
  DecisionMode: ontic-only | U-kind-only | atomic ontic-plus-U-kind.
```

When the E.24 ontology-disposition question is current, fill exactly one branch field inside `OntologyDispositionResult`; the decision EntityOfConcern remains fixed and the selected payload stays in that field. A changed result changes the decision's ClaimGraph and therefore identifies another decision episteme under C.2.1; state any edition continuity explicitly. In `ontic-only`, cite the already accepted U-kind result consumed by the ontic and omit a new `UKindAdmissionResult`. In `U-kind-only`, cite the already accepted ontic settlement and omit a new `OnticSettlementResult`. Use `atomic ontic-plus-U-kind` only when neither needed output already exists. The two outputs are evaluated from the same candidate inputs, remain provisional while either branch is unresolved, and become accepted together only when both branches pass. One output must never cite the other as an already accepted premise from the same decision. If one branch fails, retain the independently valid existing objects and record the exact `reuse`, `local-kind`, `reject`, or unresolved result; do not manufacture the missing output to save the other.

The bootstrap co-decision is `E24-CO-UONTIC-BOOT-01`. Its EntityOfConcern is the exact source-construct entity defined by E.24:4 for the kind `U.Ontic`; it does not presuppose an admitted `U.Ontic` or a pre-existing ontic instance. From that common input it returns two distinct accepted outputs: `E24-OS-UONTIC-BOOT-01`, which accepts this shared settlement schema as the direct rule for identifying future ontology-unit individuals, and `E24UK-AR-UONTIC-BOOT-01`, which admits the root kind `U.Ontic`. The schema, pattern, decision episteme, and kind are not thereby instances of `U.Ontic`; each concrete ontology-unit individual still needs an ordinary `OnticSettlementResult`. No relation-about-relation or relation from the kind to itself is invented for the bootstrap.

E.24 is compatible with modular ontology and ontology-design-pattern practice: modular ontology libraries and ontology design patterns show why reusable small ontology structures matter, and recent process-modeling work reports loss of reuse when process patterns remain implicit. E.24 is narrower and more FPF-specific: it governs the decision whether FPF should introduce a durable action-facing ontic, rather than importing an external microtheory or treating every reusable repair table as ontology.

If the three resolved ontology dispositions need reusable comparison, use `A.19.ECS` to construct the evaluation `CharacteristicSpace`: retain the current subject assertions and relations, add one bounded local episteme for a declared use, or add a durable ontic with its own rule content. The `A.19.ECS` locator establishes neither a Method nor a MethodDescription; apply A.3.1 and A.3.2 only if those identities matter. E.24 supplies the candidate dispositions and their ontic constraints, while characteristic selection and evaluation remain separate A.19.ECS assertions. Source-use status remains an independent provenance choice, not a fourth candidate, and a comparison result does not establish ontic identity.

Within this split, the rule content located at E.24 states the distinction among the ontic, the claim-bearing decision episteme, reusable declarations, and publication-side objects, plus the ontic-introduction decision needed before dependent uses rely on a durable ontic. Publication-section rules, adequacy scales, wording-use restoration rules, and evaluation of the resulting FPF pattern-set structures remain separate exact assertions whose `ClaimGraph` sources are located through the neighboring patterns named above.

Use the current split this way:

- use `E.24` for `U.Ontic` identity, the primary governed subject kind, exact identity or constitution rule, minimal governed relation set, subject patterns, named dependent-pattern reliance, and non-use boundary;
- use `E.24.CD` when the current problem is detecting and characterizing an apparent subject before deciding whether it should enter an E.24 ontic-introduction decision at all; `E.24.CD` supplies detection and characterization only and selects no E.24 disposition. `Local use frame` is not an E.24 disposition: recover whether the payload needs direct subject-assertion use, a bounded local episteme under C.2.1, a durable ontic, or an unresolved stop; record any source-use status separately.
- use `E.24.PUB` when the current problem is the distinction among the ontic, an ontic-description episteme, the publication occurrence that makes one selected edition available, the publication form that expresses it for that use, and the `U.PresentationCarrier` that bears the form; use `E.17.0` for `U.View` membership, A.6.3 for optional viewing construction, and `C.29` for a representation;
- use `A.19.ECS` only when the contested question is how to construct an evaluation `CharacteristicSpace` for comparing the resulting FPF pattern-set structures after retaining the subject-pattern relations, adding one bounded local episteme whose claims cite them for a declared use, or adding a durable ontic and its subject pattern.

This split keeps E.24 ontic-first. Questions about candidate detection, publication discipline, and contested evaluation remain separate exact subject assertions under their own defining or constraining `ClaimGraph` sources rather than becoming sections that turn E.24 into a general discovery, documentation, or scoring pattern.


Introduce or rely on a durable FPF ontic only after the ontic-introduction decision satisfies four checks.

#### E.24:4.1 - Check 1: Existing Rule-Content Check

Name the current claim under decision and ask whether an existing exact defining or constraining `ClaimGraph` already states its rule content.

Use existing rule content first. If the case is method semantics, resolve the defining `ClaimGraph` located at `A.3.1`; if it is method description, use `A.3.2`; if it is mechanism meaning, use `A.6.1` and `E.20`; if it is work planning or dated work, use `A.15.2` or `A.15.1`. For evidence, gate, source, assurance, decision, release, publication, or another case, name the exact current subject assertion and its defining or constraining `ClaimGraph`, with the pattern id only as locator, before selecting direct rule-content use. If no current rule content can be recovered by value, that disposition is unavailable; use the other E.24 dispositions rather than treating the topic word as authority.

Do not introduce a durable ontic only because several patterns are near each other or because one source word appears often.

For a candidate relation kind, recover the exact participants and test the current direct relations against their exact predicates, assertions, and defining `ClaimGraph` sources. If one direct relation closes the named dependent-use claim, use that settlement and stop. If none closes it, `A.6.RCD` may derive the needed claim and return a local-claim, predicate-definition, derived-kind-candidate, or primitive-kind-candidate disposition. A local compound claim or reusable predicate-definition episteme is not a relation kind. A derived-kind candidate proceeds only with a proposed direct subject settlement of its base dependencies, obtaining, applicability, and occurrence identity; a primitive candidate proceeds only with a candidate standalone defining `ClaimGraph` that supplies its own obtaining and occurrence identity. E.24 uses the direct settlement or A.6.RCD result and does not repeat the derivation method.

#### E.24:4.2 - Check 2: Stable Identity Test

A candidate qualifies as a durable ontic only when it has stable identity beyond one local wording issue, source expression, or bounded local episteme used for first explanation.

Ask:

1. What exact candidate entity, proposal episteme, or source-construct entity is independently identifiable before judgment, and what direct rule identifies it as the fixed EntityOfConcern of the decision episteme?
2. Which exact result payload follows from each available disposition without replacing that fixed EntityOfConcern: closing assertions, a bounded episteme, a selected ontology-unit individual, or an unresolved reason?
3. What changes the identity of that ontic?
4. What does not change ontic identity, even if an ontic-description episteme, publication form, notation, view, or presentation carrier changes?
5. Which direct world-side relations and grounding conditions are required for identity?
6. Which dependent patterns may rely on that identity?
If those questions cannot be answered, keep any needed coordination in a bounded local episteme under C.2.1 or use the subject patterns without another coordination episteme.

Test the invariant against the subject before filling a relation field:

| Governed subject | Identity, constitution, or recognition rule | Relation-set consequence |
| --- | --- | --- |
| Holon or System | A.1's exact candidate, constituents, constructive part relations and assembly, reidentification, whole-level characteristic, larger-assembly compatibility, and any kind-specific condition | keep those facts under their subject patterns; A.1 explicitly forbids compressing them into one universal relation signature |
| Method | A.3.1's semantic way-of-doing identity and any independently governed method-holarchy facts | name only the direct relations needed by dependent method use; no head relation is presumed |
| Work | A.15.1's dated occurrence identity and continuity rule | performer, enacted method, affected referent, resources, and results stay under their exact direct relations or A.6.1 bindings |
| Transformation | A.3.4's independently identified actual bounded change at the selected resolution | work, flow, production, representation, and receiving-use relations remain separate; no core relation is invented |
| Episteme | C.2.1's constitution rule | `EpistemeConstitutionRelation` is identity-bearing because C.2.1 explicitly selects it; empirical grounding, edition, conformance, and publication remain neighboring relations |
| Relation | A.6.REL plus each direct relation pattern's obtaining and occurrence-identity rule | the ontology unit coordinates common occurrence discipline with those direct rules; no relation-to-relation head occurrence is required |

#### E.24:4.3 - Check 3: Direct Relation and Declaration Test

An ontic-introduction decision identifies each direct relation needed by the selected use before it introduces reusable SlotSpecs in a separate `RelationSignature` episteme. It singles out one identity-bearing relation only when the subject's subject pattern does.

One-screen first-use card:

Choose the branch with three observable thresholds before opening the ontology object map:

- **Direct use closes the case** when one readable claim under current subject patterns gives the named receiving use what it needs. Point to that claim and stop; do not add a coordination episteme or ontic.
- **A bounded local episteme is needed** when one named receiving use must read several already governed claims together, but no other current pattern relies on their package as reusable ontology. Identify that one episteme under C.2.1 and keep every governed object under its direct pattern.
- **A durable ontic is needed** only when multiple current patterns must reuse the same independently identified ontology unit and would otherwise duplicate or disagree about its identity or constitution and minimal relation set.

If none of the three thresholds can yet be demonstrated, record an unresolved stop. Source provenance remains the separate source-use status from F05 and can accompany any of the three resolved branches.

The following card is the cheap first-use summary. State the recognizable situation, the use that must close, and the exact subject; run the three thresholds; then fill `ontologyDispositionResult` last. Work and decision are examples of receiving use, alongside comparison, preservation, teaching, publication, and reference use.

Treat a filled card as the decision episteme only when its claim content, fixed pre-judgment `decisionEntityOfConcern`, and effective ReferenceScheme are recoverable under C.2.1. The branch payload is a result about that candidate, not the candidate's replacement. If the result later changes, identify the changed ClaimGraph as another decision episteme and state any edition continuity separately. A working phrase, topic cluster, draft heading, or list is not that exact subject. If no candidate entity, proposal episteme, or source construct is independently recoverable, the card remains an inquiry prompt.

```text
OnticIntroductionFirstUse:
  currentSituation: one recognizable sentence naming the current claim or source expression.
  receivingUse: the exact comparison, preservation, teaching, publication, reference, work, decision, or other use that must close.
  decisionEntityOfConcern: one independently identified pre-judgment candidate entity, proposal episteme, or source-construct entity; it stays fixed across the branch result.
  decisionEntityOfConcernGovernor: the direct rule that identifies that candidate before judgment.
  branchThresholdResult:
    directUseCloses: yes or no; the one readable claim and current pattern that close the receiving use.
    boundedCoordinationNeeded: yes or no; the several governed claims that must be read together for this use, plus confirmation that no current pattern relies on their package as ontology.
    durableReuseNeeded: yes or no; the multiple current patterns that must reuse one ontology unit and the identity, constitution, or relation-set disagreement that would otherwise recur.
  ontologyDispositionResult:
    disposition: fill last from those thresholds: subject-pattern-use | bounded-local-episteme | durable-ontic | unresolved-stop.
    directUseResult?: exact closing assertion and direct pattern locators.
    boundedEpistemeResult?: exact bounded episteme, its declared use, and stop.
    durableOnticResult?: exact ontic-settlement result, selected ontic, and subject-pattern locator.
    unresolvedResult?: exact unresolved reason and the missing evidence or rule.
  sourceUseStatusIfCurrent?: quote-only | reduced use | selected stronger source use; omit when no source-use claim is current and keep exact provenance when it is.
  blockedLocalOverread: the nearest tempting object, kind, relation, or authority that this result does not create or license.
```

Every candidate receives one truthful branch result. Ordinary direct, bounded, and unresolved cases stop at this card: direct use needs only its current closing assertion, and bounded use adds only the C.2.1 coordination required by that use. Omit source, publication, view, representation, Work, U-kind, and other neighboring-object fields when no such claim is current; absence is enough and needs no blank or `not current` value.

##### E.24:4.3a - Authoritative Typed Object Map

Open only rows whose selection question is true for the chosen branch. Later sections point here instead of repeating the inventory.

| Object class | Selection question | Record by value and subject pattern |
| --- | --- | --- |
| World-side participant | Does an obtaining predicate require this actual object in one participant meaning? | actual object, admitted kind, participant meaning, and the direct relation pattern; a SlotSpec or designation is not the participant |
| Relation occurrence | Is the current claim that one direct predicate obtains among actual participants? | relation kind, participants, obtaining condition, occurrence identity, and direct governor; use this row for the one readable claim that closes direct use |
| Reusable declaration | Does another use need the same participant typing without asserting an occurrence? | `RelationSignature` episteme and only the reused `SlotSpec = <SlotKind, ValueKind, refMode>` declarations under A.6.5 |
| Claim-bearing episteme | Does the receiving use need an assertion, description, decision, or several governed claims read together? | C.2.1 identity, exact EntityOfConcern, ClaimGraph, effective ReferenceScheme, declared use, and stop; a bounded episteme governs no new ontology |
| Durable ontology unit | Must multiple current patterns reuse one independently identified unit or otherwise duplicate or disagree about identity, constitution, or the minimal relation set? | ontology-unit individual, primary subject kind, identity or constitution rule, minimal relation set and governors, governing ontic pattern, E.24.UK result when current, and dependent reliance |
| Publication object | Is availability of one selected episteme edition to an audience current? | under E.24.PUB/E.17, distinguish the publication occurrence, selected edition, audience and use, form that expresses it, and carrier that bears the form |
| View | Does one identified episteme conform to an exact viewpoint for the receiving use? | E.17.0 conformance for the same episteme as `U.View`; A.6.3 construction only when that history is current; viewpoint use does not change episteme identity |
| Representation | Does a declared modeling or reasoning use need an explicit correspondence? | C.29 representation, its elements, effective representation scheme, and explicit correspondence to an independently identified object; representation does not change that object's identity |
| Source expression | Does source wording or provenance change what use is authorized? | exact expression, source episteme, current source publication occurrence when relevant, carried content, source-use status, admissible use, and smallest stronger-use condition |
| Dependent-pattern reliance | Does another current pattern consume this accepted result? | that pattern and the exact ontic identity, direct relation rule, or reusable declaration it relies on; do not copy the rule |

Before opening the full `OnticIntroductionDecision` form, run two guards. First, state the subject's identity, constitution, or recognition rule and the smallest relation set the named dependent use needs. For every included direct relation, write one readable sentence naming its participants and predicate; mark it identity-bearing only when its subject pattern does. Only then declare `SlotKind`, `ValueKind`, and `refMode` under A.6.5 for a relation whose typed reuse is current; when `refMode` is a `RefKind`, name that declared `RefKind`. Second, treat bare *role* as an E.10.ROLE trigger and ask only whether the current ontic decision has confused a world-side participant, a local system-role kind and its A.2/C.3.2 classification, an exact A.2.1 assignment occurrence, or a declaration-local participant meaning in an A.6.5 reusable declaration. Keep the participant under its direct subject pattern and use F.6 only when Work attribution is current. E.24 does not reconstruct any assignment signature or occurrence rule, and bare *role* supplies no common head for these objects.

When an encountered card, table, schema, diagram, or record is current, apply the selection question in `E.24:4.3a` to each proposed use. Visible shape and field co-occurrence identify no episteme, publication object, representation, relation kind, or obtaining occurrence. Only an identified `U.System` performs description, rendering, or publication work.

Introducing an ontic organizes kinds, direct relation rules, declarations, and named dependent-pattern reliance in FPF. It does not create or individuate any project-side relation occurrence. For each such occurrence, apply the direct predicate and domain identity rule under A.6.REL. A designator may designate the already reidentified occurrence; a governed reference may resolve to it; an assertion or description episteme may carry a claim and designation about it. A publication occurrence instead makes one selected episteme edition available and neither designates nor creates the world-side occurrence.

Worked durable-branch replay:

The detailed replay below is opened only after the first-use thresholds select a durable ontic. Its pre-judgment subject is `EpistemeOnticProposal_v1`, identified under C.2.1 by `EpistemeOnticProposalClaims_v1` about source construct `E24-Episteme-Ontic-Candidate-v1` under `FPF-Ontic-Proposal-Scheme-2026`; it exists before and is not identical to the selected `EpistemeOntic`. The replay applies the object map to a pump-maintenance specification. C.2.1 actually selects an identity-bearing constitution relation for the Episteme ontic; the named project triple is one witness. Other ontics use their own identity rule and need not imitate this relation shape.

```text
OnticIntroductionDecisionReplay:
  primaryGovernedSubjectKind: `U.Episteme`.
  receivingUse: FPF authors compare and maintain dependent episteme patterns against one shared identity and relation set; maintenance engineers then apply those rules to the PumpStation37 specification while its grounding, views, evidence, editions, and publications change.
  decisionEpistemeIdentity:
    claimGraph: `PumpMaintenanceOnticDecisionClaims_v1`.
    entityOfConcern: `EpistemeOnticProposal_v1`; this fixed proposal episteme is not the selected ontic.
    effectiveReferenceScheme: `FPF-Ontic-Decision-Scheme-2026`.
  ontologyDispositionResult:
    disposition: durable-ontic.
    durableOnticResult: `E24-OS-EPISTEME-ONTIC-01`, selecting `EpistemeOntic` under E.24.
  e24FamilySettlement:
    decisionMode: ontic-only.
    existingUKindAdmissionResultRef: `E24UK-AR-UEPISTEME-RG-01`.
    onticSettlementResultRef: `E24-OS-EPISTEME-ONTIC-01`.
    atomicCoDecisionRef: none; no new public U-kind is proposed in this replay.
  onticRootIfSelected: `EpistemeOntic`, one explicitly designated ontology-unit individual of kind `U.Ontic`. E.24 reidentifies it from the primary governed subject kind `U.Episteme` and the identity-bearing direct relation kind `EpistemeConstitutionRelation`, including that relation's predicate, participant meanings, and admitted actual-participant kinds. It is neither the `U.Episteme` kind nor any PumpStation37 episteme.
  identityBearingDirectRelationIfSelected: `EpistemeConstitutionRelation`, governed by C.2.1. Its participant meanings are constitutive claim content, exact EntityOfConcern, and effective reference scheme; its admitted actual-participant kinds are `U.ClaimGraph`, `U.Entity`, and `U.ReferenceScheme`. It obtains when the scheme makes the claim graph interpretable and evaluable as claims about the exact entity and the three participants form one claim-bearing whole; the participant triple identifies the occurrence. The PumpStation37 consuming witness is the distinct occurrence among `MaintenanceClaims_v7`, `PumpStation37`, and `StationMaintenanceReferenceScheme_2026`; that project occurrence neither is nor identifies `EpistemeOntic`.
  reusableDeclarationsIfNeeded: `EpistemeConstitutionRelationSignature` with the three SlotSpecs declared in `C.2.1`, only where another pattern needs reusable participant typing.
  minimalGovernedRelationSet:
    instanceLayer: `EpistemeConstitutionRelation` among actual claim graph, EntityOfConcern, and reference scheme is identity-bearing; `EpistemeEmpiricalGroundingRelation`, `EpistemeEditionRelation`, `EpistemeViewpointConformanceRelation`, and `EpistemePublicationRelation` retain the actual participants and predicates supplied by C.2.1, E.17.0, and E.24.PUB when their named use is current. A.6.3 construction and A.10 evidence use remain separate and join only under their own current governors.
    ontologyDeclarationLayer: this decision episteme says that `EpistemeOntic` coordinates the `U.Episteme` identity rule and those exact relation rules and declarations for the named dependent patterns. It asserts no world-side relation whose participants are `EpistemeOntic`, `U.Episteme`, a relation kind, a signature, or a pattern.
  claimBearingEpistemesIfNeeded: the independently identified `EpistemeOnticProposal_v1` remains the decision's EntityOfConcern. The PumpStation37 episteme and its constitution occurrence are separate consuming witnesses; a separate assertion about that occurrence is added only when that claim is current.
  viewIfNeeded: exact maintenance episteme E is the same individual as a `U.View` only when E.17.0 conformance to exact maintenance viewpoint P obtains; any source episteme and A.6.3 construction remain separate.
  representationIfNeeded: a wiring-diagram representation remains under C.29 and corresponds to independently recovered objects.
  publicationOccurrenceIfNeeded: if the specification edition is made available to the maintenance team for scheduled repair work, name that selected edition, audience, bounded use, and publication occurrence.
  publicationFormIfNeeded: name the form that expresses the selected edition for that use.
  presentationCarrierIfNeeded: name the identified paper sheet, file, display, or other `U.PresentationCarrier` that bears the form.
  dependentPatterns: `E.17.0` relies on the same C.2.1 episteme identity plus exact viewpoint conformance when the specification is admitted as a `U.View`; `A.6.3` relies on the independently identified source and receiving epistemes only when viewing construction is current. Neither pattern copies the constitution rule.
  blockedLocalOverread: grounding holon, viewpoint, view, evidence, edition work, publication occurrence, form, carrier, and representation are not extra participants of `EpistemeConstitutionRelation`.
```

The full replay form is heavier:

Every candidate gets a truthful branch result, but ordinary direct, bounded, and unresolved cases stop at the one-screen card. Open the full form only when dependent patterns will rely on a proposed durable ontic, the current claim changes admissible use, or a receiving use needs a replayable reason why bounded C.2.1 coordination was insufficient. A durable branch is load-bearing because its threshold already requires reuse by multiple current patterns.

The following fuller code block is an optional publication form for one claim-bearing ontic-introduction decision episteme. When a guard above opens it, include only rows activated by the selected branch and receiving use. Omit every inactive neighboring-object or assurance row; the labels are prompts, not fields that must be filled, and they are not world-side participants, SlotSpecs, or components of the selected ontic.

```text
OnticIntroductionDecision:
  OntologyDispositionResult:
    Disposition: fill last from the existing-governor, identity, connectivity-or-constitution, dependent-use, and non-duplication evidence; durable-ontic | bounded-local-episteme | subject-pattern-use | unresolved-stop.
    DirectUseResultIfSelected: exact closing assertion and direct pattern locators; detailed governed object below.
    BoundedEpistemeResultIfSelected: exact bounded-episteme reference, declared use, and stop; identity details below.
    DurableOnticResultIfSelected: exact OnticSettlementResult, selected ontic, and ontic subject-pattern locator; settlement details below.
    UnresolvedResultIfSelected: exact unresolved reason and missing evidence or rule.

  SourceUseStatusIfCurrent: quote-only | reduced use | selected stronger source use; omit when source use is not current.
  WorkingSubjectExpressionIfCurrent: wording that opened a source-driven inquiry; never used as an EntityOfConcern without independent identification.
  SourceExpressionUseIfCurrent:
    ExactSourceExpression:
    SourceEpistemeIfRecoverable:
    SourcePublicationOccurrenceIfCurrent:
    RecoveredEntitiesRelationsAndClaims:
    CurrentAdmissibleUse:
    StrongerUseCondition:
    WordingUseRestorationCoordinatesIfE10ARCHOpenedTheCase:
      SemanticAreaBaseConcept:
      SemanticArea:
      SemanticAreaSenseFamily:
      OntologicalNeighborhood:
  DecisionEpistemeIdentity:
    ClaimGraph:
    EntityOfConcern: one independently identified pre-judgment candidate entity, proposal episteme, or source-construct entity; never a result selected by the branch.
    EntityOfConcernIdentityGovernor:
    EffectiveReferenceScheme:
  DirectGovernedObjectIfSelected:
  BoundedLocalEpistemeIfSelected:
    EpistemeIdentity:
    EntityOfConcern:
    ClaimGraph:
    EffectiveReferenceScheme:
    DeclaredBoundedUseAndStop:
  SelectedOnticNameIfAny:
  PrimaryGovernedSubjectKind:
  ReceivingUse: exact comparison, preservation, teaching, publication, reference, work, decision, or other use and how absent coordination changes it.
  SelectedOnticIfDurableDisposition:
  StableIdentityCriterion:
  IdentityOrConstitutionRule:
    DirectGoverningPattern:
  E24FamilySettlement:
    DecisionMode: ontic-only | U-kind-only | atomic ontic-plus-U-kind.
    SharedCandidateInputsRef: exact CandidateInputs block governed by E.24:4.0a.
    ExistingAcceptedOnticOrUKindResultRefsIfReused:
    AtomicCoDecisionRefIfBothNew?:
    OnticSettlementResultRefIfAny?:
    UKindAdmissionResultRefIfAny?:
  UKindOutputIfCurrent:
    SharedDecisionRef: exact `E24FamilySettlementDecision` governed only by E.24:4.0a; do not fill another E.24.UK decision form.
    DecisionMode: U-kind-only | atomic ontic-plus-U-kind.
    ExistingAcceptedOnticSettlementRefIfReused?: required for U-kind-only; omit when the atomic decision creates both outputs.
    UKindAdmissionResultRef: exact `UKindAdmissionResult` output.
    AdmissionDisposition: exactly one value from E.24.UK's closed set: root | same-individual-dependent | identity-dependent | reuse | local-kind | reject.
    BranchSpecificResultRefIfRequired: the exact membership, dependence, reused-kind, local-declaration, or recovered-object result required by that disposition.
    LocalGainCostAndDuplicateOntologyRisk: the decision-changing rationale; not another disposition or decision form.
  MinimalGovernedRelationSet:
    InstanceLayer: for every included direct relation, its actual participant meanings and kinds, predicate, occurrence identity, direct governor, and the named use it enables.
    OntologyDeclarationLayer: the exact decision claims that include each kind, relation rule, declaration, or pattern and state each dependent reliance; an actual declaration-side relation is named only when independently governed.
  IdentityBearingDirectRelationIfSelected:
    DirectRelationKind:
    DirectGoverningPattern:
    ParticipantMeanings:
    AdmittedActualParticipantKinds:
    ObtainingCondition:
    OccurrenceIdentityRule:
    RelationSignatureIfNeeded:
      SlotSpecs:
  DependentKindsIfAny:
  NeighboringGovernedEntitiesOutsideSelectedRelationSet:
  ClaimBearingEpistemesIfNeeded:
  ViewsIfNeeded:
  RepresentationsIfNeeded:
  PublicationUsesIfNeeded:
    PublicationOccurrence:
    SelectedEpistemeEdition:
    DeclaredAudienceAndBoundedUse:
    PublicationForm:
    PresentationCarrier:
  GoverningPatterns:
    OnticGoverningPatternIfSelected:
    SubjectKindIdentityAndRelationPatterns:
    NeighboringDirectRelationPatterns:
    DirectUsePatternsBeforeNewOntic:
  ExistingGoverningPatternsReused:
  DependentPatternReliance: for each named dependent pattern, the exact ontic identity, direct relation rule, or RelationSignature declaration relied on.
  RelationLabelsThatAreNotNewKinds:
  NonUseBoundary:
```

No candidate inherits a `U.*` decision from E.24. Give every candidate a truthful one-screen branch result; complete the full form only when one of its three guards is true, and then only by the rows that guard, branch, and receiving use activate.

When typed reuse needs a declaration of one selected direct relation, its `RelationSignature` uses A.6.5 and the E.24 decision defines no second slot discipline; the direct relation retains its exact predicate and defining `ClaimGraph`. A SlotKind names one participant meaning only inside the selected `RelationSignature`, and its ValueKind constrains the admitted kind of the actual participant corresponding to that SlotSpec. Neither the SlotKind label nor its wording decides that kind; an exact participant-kind assertion does.

#### E.24:4.4 - Check 4: Exact Rule-Content and Dependent-Use Test

State:

- the pattern governing the selected durable ontic;
- the exact defining `ClaimGraph` for each relation in the minimal set, and which relation is identity-bearing when an exact subject assertion selects one;
- each dependent pattern and the identified ontic identity, direct relation rule, or `RelationSignature` declaration on which it relies;
- each draft ToC row, planned pattern label, or absent subject-pattern section that remains non-governing.

Naming, publication placement, and evaluation remain neighboring authoring work under `F.18`, `E.8`, `E.9.DA`, and `E.21`. The ontic-introduction decision may point to those next moves, but none establishes ontic identity or replaces the subject pattern.

If the decision selects a durable ontic, write the pattern that defines or constrains it before dependent patterns rely on it. If the decision selects only a bounded local episteme, identify that episteme under C.2.1 and state its non-governing bounded use and claims by value. If no pattern governing the proposed durable ontic is written, do not cite that candidate as governing current FPF use.

#### E.24:4.4a - Recover broad rule-content, provision, and support wording before admission

Do not admit a generic governance, provision, support, or rule-locus ontic merely because several patterns use those words. First freeze the exact source occurrence and recover what it says by value: an exact subject assertion, defining or constraining ClaimGraph, direct relation, Work occurrence, Method or MethodDescription, promise or commitment content, source use, publication, evidence, assurance, authority, access, or ordinary-language claim. The recovered C.2.1 assertion is the preservation object for that occurrence; a shared dispatch table, field name, or word family is not.

A broad candidate fails the durable-ontic test when its proposed members have no common identity or membership rule and no non-duplicative receiving use. In that case E.24 supplies no umbrella object. Keep each narrow recovered meaning under its existing pattern and use E.24.UK for the associated U-kind question with an occurrence-local `reject`. The rejection's `RejectedCandidateRecoveryRef` must resolve the exact preserved assertion. If the occurrence has not yet been recovered, leave its material wording unchanged rather than deleting content under a lexical rule.

This rule blocks generic `U.Provision`, `U.Support`, `SupportRelation`, governance relation kinds or occurrences, and rule-locus description kinds unless a later, independently accepted case supplies exact individuals, identity, membership, non-members, and a receiver that cannot use existing assertions and relations. It does not block genuine service-provision Work, operational support Work, evidence support, source use, publication support, human or institutional authority, or another exact relation whose own predicate obtains.

#### E.24:4.5 - Bounded Local Episteme Decision

Use a bounded local episteme when one application family needs a readable coordination of entities and direct relations that are already governed elsewhere, but no new durable ontology unit is justified.

A bounded local episteme is a `U.Episteme` identified under C.2.1, not a new U-kind. Select one independently identified EntityOfConcern before writing claims. It may be a world-side entity or individuated occurrence under an exact subject assertion, an admitted collection-as-whole or selected `U.Structure`, or an identified source, expression, or pattern-set architecture object. The selection test is the same: every claim must concern that one object. If several unrelated subjects remain and no admitted whole or selected structure unifies them, split the claims. A phrase or list cannot stand in for the missing subject.

For that bounded use:

- name the application concern, exact EntityOfConcern, and direct pattern that identifies it;
- state why every carried claim concerns that one object;
- identify each other governed entity and direct relation designated by those claims;
- cite the pattern governing each direct relation rather than restating its participant or identity rules;
- state the tempting ontic overread that the episteme does not license;
- stop before dependent patterns treat this one episteme as a durable ontology unit.

**Positive example.** `Pump37MaintenanceCoordination_v1` has exact Pump #37 as its EntityOfConcern. Its ClaimGraph may designate the current maintenance plan, dated work, enacted method, and direct relations because every claim explains how this exact pump is maintained for the named scheduling decision. Pump #37's A.1 identity is independent of the coordinating episteme.

**Blocked example.** The expression `workflow` points variously to a method, work plan, dated work, and transformation-flow structure, but no one identified entity, admitted collection-as-whole, or selected structure yet unifies those claims. Do not make the word or the four-item list an EntityOfConcern. Keep the source inquiry material and split any already valid direct claims until one exact subject is recovered.

Precision restoration may use a bounded episteme when one receiving use needs several mapped claims read together. The episteme coordinates those claims for that use; every referenced object and relation still uses the subject pattern named in `E.24:4.3a`.

