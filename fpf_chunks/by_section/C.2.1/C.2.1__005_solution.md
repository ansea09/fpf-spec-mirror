---
chunk_kind: "child"
pattern_id: "C.2.1"
pattern_title: "U.Episteme: Constitution, Empirical Grounding, and Edition Relations"
section_id: "C.2.1:4"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/C.2.1/C.2.1__005_solution.md"
commit_sha: "9fa2a3596dab58d282d736bcf413cdda4286db0a"
heading_path:
  - "C.2.1 — U.Episteme: Constitution, Empirical Grounding, and Edition Relations"
  - "C.2.1:4 — Solution"
line_start: 50943
line_end: 51318
dependencies:
  - "A.1"
  - "A.1.1"
  - "A.10"
  - "A.14"
  - "A.2.6"
  - "A.22"
  - "A.3.1"
  - "A.3.2"
  - "A.3.4"
  - "A.6.0"
  - "A.6.1"
  - "A.6.2"
  - "A.6.3"
  - "A.6.3.RT"
  - "A.6.4"
  - "A.6.5"
  - "A.6.REL"
  - "A.7"
  - "B.3"
  - "C.13"
  - "C.2.1"
  - "C.2.P"
  - "C.29"
  - "C.3.2"
  - "E.10.D2"
  - "E.13"
  - "E.17"
  - "E.17.0"
  - "E.24.PUB"
  - "E.24.UK"
  - "F.9"
  - "G.11"
  - "U.Episteme"
  - "U.MethodDescription"
  - "U.Signature"
  - "U.View"
keywords:
---

### C.2.1:4 - Solution

Identify each `U.Episteme` through `EpistemeConstitutionRelation`: first state what it says, what exact entity it concerns, and the scheme under which those claims are read. Then name what the reader will do with that episteme. Add a neighboring relation only when the reader's next sentence or action requires it. The conditional branches below supply the relevant direct relation and its test.

**Local episteme mantra.** *Name the claims, what they concern, and the scheme that gives those claims their reference. Stop if identity is all the task needs. Otherwise name the concrete receiving use and add only the neighboring object or relation needed for its next sentence or action. Ask for an unresolved question only in a real inquiry or decision. Update episteme identity only when claim content, EntityOfConcern, or effective reference scheme changes; otherwise update the affected relation or object under its direct pattern.*

The mantra is a recall aid, not a work plan. The application method and stop conditions are carried by sections 4.1-4.9; section 4.10 is a later reference for relation and neighboring-object distinctions.

#### C.2.1:4.0 - First-use completeness questions

Begin with the three questions that identify the episteme. They are identity questions, not fields to fill. When the answers are still being developed, :4.1.1 connects the writing work in C.2.4:4.6 to the resulting constitution judgment.

| Always ask | Exact object recovered |
| --- | --- |
| What is being claimed? | the exact claim content carried by one `ClaimGraph` |
| What exact entity do those claims concern? | one identified `U.Entity` participating as the EntityOfConcern |
| Under which designation and interpretation rules are the claims read, and, where the claims use them, which measurement, comparison, or evaluation rules apply? | the effective `ReferenceScheme` |

If the task needs only the episteme's identity, stop after the three answers. Otherwise state the concrete receiving use. Ask for an unresolved uncertainty or choice only when that use is a real inquiry or decision.

Open a row below only when its first column names the reader's next sentence or action. Each positive answer adds an independently governed object or direct relation; none adds another slot or identity discriminator to the episteme.

| Open this row when the next sentence or action is... | Recover | Subject pattern |
| --- | --- | --- |
| A claim or relation must cite the exact constitution occurrence, not merely say that the episteme exists. | one exact obtaining `EpistemeConstitutionRelation` occurrence, reidentified by the participant triple; designate it when an epistemic receiver needs a reference, or use the occurrence itself as a participant when another direct relation is the receiver | C.2.1:4.2.3 and `A.6.REL` |
| A reader must cite one exact claim inside one exact episteme edition, rather than the whole episteme. | one `ClaimAddress`: an exact episteme-edition reference plus an intrinsic claim identity declared by that edition's exact ClaimGraph; if no such identity resolves uniquely, cite the whole episteme or identify the claim as a separate episteme | C.2.1:4.2.5 |
| A typed interface needs replaceable interpretation rules or exact content, or must recover that value from an addressable episteme. | the receiving range, exact constituent value and any required designation/resolution; keep membership separate from successful use | C.2.1:4.1.2 and :4.2.6 |
| An observer must inspect designated empirical claims against current observation, intervention, measurement, or test relations involving one exact holon. | one exact `EpistemeEmpiricalGroundingRelation` occurrence, its covered claim subgraph, claim-to-world mappings, and grounding holon; recover supporting evaluation or evidence use separately | C.2.1:4.3 and the direct observation, intervention, measurement, test, evaluation, or evidence pattern |
| A description must state the concern from which this episteme is read. | one exact `U.Viewpoint` episteme P and the named describing use that selects P; keep the episteme, its EntityOfConcern, the use, and P distinct | `E.10.D2` and `E.17.0` |
| A team will validate a Description as a specification before relying on it. | the exact Description episteme, checkable claims, and named harness or validation relation; preserve or update the named describing-use viewpoint only when that selection affects reliance | `E.10.D2` and C.2.1:6 |
| A classification assertion must say that this episteme conforms to a viewpoint and is a `U.View`. | one exact obtaining `EpistemeViewpointConformanceRelation` between this episteme and at least one exact `U.Viewpoint` episteme | `E.17.0` |
| A reader must trace how this episteme was constructed from an earlier source episteme. | the exact source and receiving epistemes plus the governed viewing relation; view membership remains a separate conformance judgment | `A.6.3` for construction and `E.17.0` for membership |
| A claim must be restricted to one declared part of the situation under study. | one exact `U.ClaimScope` and its membership relation over `U.ContextSlice` | `A.2.6` |
| A calculation or interpretation must use one selected organization of model use. | one exact `BoundedModelUseStructure` and the relation through which the receiving assertion or use selects it | `A.1.1` and the direct receiving-use pattern |
| A reader proposes to compare, substitute, translate, publish, or otherwise use an obtaining cross-context Bridge. | one ordinary C.2.1 assertion episteme whose EntityOfConcern is that exact Bridge and whose ClaimGraph states the proposed use, direction, correspondence rule, loss tolerance, and polarity; recover reliance and any use that actually happened separately | C.2.1:4.2.3 for claim identity; `F.9` for the Bridge; `A.10` for ordinary evidence reliance; `B.3` only when an actual named assurance claim is current; the direct receiver pattern for any actual use |
| A decision or inference must cite support links among the claims. | the exact `JustificationGraph` content that carries those dependencies | C.2.1:4.4; use `A.10` only when ordinary evidence reliance is current, and `B.3` only when an actual named assurance claim is current |
| A decision or evaluation will accept, reject, or withhold reliance because of evidence. | the exact evidence-use relation; evidence storage alone is insufficient | `A.10` for ordinary evidence reliance; `B.3` only for an actual named assurance claim |
| Reviewers must inspect or revise a classification judgment as an independent claim-bearing object. | one classification assertion episteme about the exact candidate, plus the exact governing criterion | C.2.1:4.2.3 with `A.1` or `C.3.2`; `E.24.UK` only for public U-kind admission |
| A reader must assert that a later episteme revises, refines, or supersedes an earlier one. | one exact `EpistemeEditionRelation` occurrence | C.2.1:4.5 |
| An account must assert that particular Work occurred. | identify the actual performer and admit the dated Work independently; if the account also attributes it to an assignment, test that attribution separately | `A.13` and `A.15.1`; `F.6` only for the stated attribution |
| A publisher must make one selected episteme edition available to a declared audience for a bounded use. | the publication occurrence, publication form, and `U.PresentationCarrier` as distinct objects | `E.17` and `E.24.PUB` |
| A user will calculate, infer, navigate, or inspect through a representation whose available operations matter. | the representation scheme, operations and correspondence needed for that use | the applicable representation pattern; `A.6.3.RT` for a same-EntityOfConcern transition; `C.29` only for an unresolved mathematical-lens choice, transfer or reliance question |
| One receiving System must select, decline, or co-use candidate results of different kinds as representations for the same exact action or decision. | one C.37 use-bounded representation-selection account; keep each direct subject result, optional A.2.4 first-use classification, A.10 reliance path when material, and receiving result separately governed | `C.37` |


Stop when no row describes the next sentence or action. A readable sentence naming the claims, EntityOfConcern, and effective reference scheme is then enough. Do not complete the table as a record. Use section 4.10 only when a later sentence or action actually needs the full relation and neighboring-object reference.

#### C.2.1:4.1 - Identify the episteme by its constitution

The shared C.2.1 identity of one `U.Episteme` is:

```text
<claim content, exact EntityOfConcern, effective ReferenceScheme>
```

`claim content` is the identity-bearing `ClaimGraph` carried as the episteme's constitutive claim structure. Each episteme selects one exact `U.Entity` as the EntityOfConcern of the current claim-bearing whole. Its ClaimGraph may also designate other independently governed entities as participants in relational, comparative, negative, counterfactual, or modal claims.

When the subject really is an admitted relation kind, an already individuated obtaining relation occurrence, an admitted collection-as-whole, or another independently identified joint entity, that object may be the EntityOfConcern. Several participant designations do not by themselves constitute such an object. A negative or counterfactual relation claim can designate the relation kind and its participants in the ClaimGraph without requiring an obtaining world-side occurrence.

Split the ClaimGraph only when it combines independent subjects in a way that makes the selected EntityOfConcern untruthful or breaks the intended identity or comparison use; do not split merely because one predicate connects several participants. The reusable predicate-definition boundary is stricter: before publication, name one truthful exact EntityOfConcern and state what the definition claims about it. If no such single concern can be selected, remain at local compound-claim level.

The effective `ReferenceScheme` supplies the designation and interpretation rules needed to read this ClaimGraph as claims about this EntityOfConcern. Add measurement, comparison, or evaluation rules only when the claims' meaning uses them. The corresponding measurement or evaluation entities and relation occurrences remain under their direct patterns.

A theorem read under a formal vocabulary and calculus needs designation and interpretation rules; it needs measurement or evaluation rules only if its meaning uses them. By comparison, a pump-tolerance episteme uses the applicable units, measurement procedure, and pass/fail criterion to make its claim meaningful; the actual measurement and evaluation occurrences remain neighboring objects rather than episteme constituents.

Changing any identity discriminator yields another episteme. Changing a carrier, layout, rendering, publication occurrence, evidence item, viewpoint assignment, or model-use setting does not by itself yield another episteme. A direct pattern may recognize the same individual as a dependent episteme kind through its stable membership condition, but it does not add another identity discriminator. `A.3.2` governs `U.MethodDescription` membership; `E.17.0` governs `U.Viewpoint` and `U.View` membership through fixed predicates over already identified epistemes. `A.6.3` governs an optional viewing construction between source and receiving epistemes, not view membership. If any work or construction changes claim content, EntityOfConcern, or effective reference scheme, those changed C.2.1 discriminators identify the resulting episteme, not the dependent-kind label.

This identity is constructive. The claim graph and reference scheme are epistemic constituents; the EntityOfConcern remains an independently governed entity related through aboutness and reference. When `EpistemeConstitutionRelation` obtains, their organization yields the whole-level characteristic of being one interpretable claim-bearing whole. The relation occurrence and the resulting episteme are distinct but reidentified from the same three discriminators.

##### C.2.1:4.1.1 - Obtain the content, recover its interpretation, and compare a change

Writing can help obtain the content before it is a finished knowledge object. Following C.2.4:4.6, put the cue or earlier expression beside a proposed claim. Recover what it is about, what is asserted, and the conditions that make that assertion meaningful. Compare the proposal with the observations and reasons that prompted it; use the subject's Method when a missing distinction requires further investigation. Keep unresolved alternatives visible when they affect the next use. A note or partial card can support this work before its content satisfies the episteme-constitution predicate.

**Recover the whole asserted content.** `ClaimGraph` names the semantic claim content organized as a whole: the claims, their participants and predicates, polarity, conditions, and the asserted relations among claims. Include quantification, modal force, and grounds asserted as part of that account where they change what it says. A field named `claim` may carry only part of this content. A graph representation can express it, but graph nodes and edges have the identity of that representation. An episteme describing this content is another object, with the described content as its EntityOfConcern. A separately obtaining justification or evidence relation remains separate unless the account also asserts something about it.

**Recover the effective rules.** `ReferenceScheme` names the rules that actually govern designation and interpretation of this content about its EntityOfConcern. Recover what the expressions designate and how their combinations, qualifications, and inferential uses are read. Include measurement, comparison, or evaluation rules only where the claim's meaning uses them. A document describing those rules is an expression of the scheme; a rule elsewhere in that document enters the effective scheme only when it governs this account. A citation can identify the rules when its selected content is unambiguous; otherwise state the missing rule. An unresolved choice between materially different readings leaves that part of the constitution unresolved.

**Individuate content and rules before assigning a kind.** An exact body of interpreted claim content and an exact collection of operative rules are abstract `U.Entity` individuals under A.1:4.1. For the content, the discriminator is the complete selected claims with their interpreted meanings and asserted organization; for the rule collection, it is the operative rules with their application domains and interpreted dependencies. These discriminators identify the individual independently of the text, graph, document or episteme through which a reader obtains it. Giving those claims or rules under an unambiguous interpretation can designate the individual directly; :4.2.6 also permits designation through an exact episteme edition and selection. Different such designations can return the same individual. Changing any of these identity discriminators identifies another content or rule collection; an expression change that preserves them does not.

This individuation and reference basis permits the content or rules to be an actual relation participant or the EntityOfConcern of an episteme about them. Neither a slot assignment nor a classification judgment supplies that basis. Entity status alone establishes no holonhood, episteme membership or obtaining relation. When the needed interpretation or identity remains unresolved, preserve the partial written result and recover the missing distinction before using it as an exact participant. That limit on the exact use does not prevent writing from helping obtain the content.

**Choose the precision the receiving work needs.** Express the claim and rules well enough to perform the named comparison, interpretation, or revision. Ordinary prose, a diagram with a clear interpretation, or a partial written comparison can be sufficient. Add a C.3.2 classification only when the receiver needs a membership, substitution, or quantified-range judgment; identify the candidates and criterion for that particular classification. Classifying whole epistemes does not establish a kind for each of their constituents. Section :4.2.1 governs a receiving use that specifically needs typed constitution participants.

**Judge identity separately from admissibility and use.** For full episteme identity, compare the complete claim content and its semantic organization, the exact EntityOfConcern, and the effective interpretation rules. Supply the correspondence that makes the preserved claims and their conditions recoverable on both sides. In a formal subject, the declared semantics and a proof or exhaustive comparison may supply it. In ordinary language, use the subject's distinctions and stated bounds to compare what each account commits to; expose an ambiguity that prevents the comparison. Agreement on selected questions establishes only that bounded agreement. A conservative derivation may omit content and therefore does not by itself establish full identity.

A change to asserted meaning or grounds is a content change even if the principal sentence remains. Choosing a different interpretation rule changes the effective scheme even if all signs remain. Making an already determined meaning easier to recover can preserve both; adding a previously unsettled condition or commitment requires a new identity judgment. When only part of the account has been compared, preserve that partial result without asserting equality of the whole. There is no general procedure here for deciding equality of arbitrary natural-language meanings.

**Reconsider what depended on the changed value.** Use :4.8 to locate the change. A :4.2.5 ClaimAddress continues to designate its claim in the original exact episteme while the edition reference resolves and that ClaimGraph declares exactly one claim with the intrinsic identity. To use corresponding content in another episteme, establish the claim-to-claim correspondence and resolve an address in that episteme; the old address remains an address in the original episteme. Changed claims or interpretation can defeat a proposed transfer of empirical coverage, an A.6.6 claim selection, or a predicate evaluation. Retest the affected viewpoint-conformance, edition-continuity, or receiving-use conclusion under its own rule. Reuse an unaffected part only with the correspondence and conditions that support that reuse. A different expression or carrier with the same complete content and scheme leaves episteme identity intact, while its suitability for the receiving action still needs that action's criterion.

##### C.2.1:4.1.2 - Declare the range needed by a receiving interface

Use an exact value directly when the receiving question concerns that value alone. A fixed-scheme operation can put its rules in the operation declaration, as in B.1.3. A reusable typed interface with a variable argument or replaceable participant needs a range: the receiver must be able to distinguish an eligible replacement from an expression that merely looks similar. State that distinction before choosing a type name.

For the recurring interpretation and claim-content uses below, the following declarations identify two C.3 kind individuals over the abstract entities individuated under :4.1.1. The candidate domains retain the distinction between those entities and their documents, graph representations or describing epistemes. Each row supplies the candidate interpretation and membership rule of its C.3.2 KindSignature; no context-slice-dependent extension is needed for these content-fixed individuals.

| Kind individual and candidate domain | Operative membership condition | Value identity and relevant boundary |
| --- | --- | --- |
| `EpistemeInterpretationScheme`: abstract rule-collection entities, identified with their application domains | The collection contains rules determining designation or interpretation of claim expressions: what a designation refers to, how a predicate or combination is read, or how a qualification or inference contributes to the claim's meaning. Its rule domains and imported semantic dependencies belong to the identified collection. | Identify a value by the operative rules, their domains and interpreted dependencies. A collection prescribing only font, page placement or file encoding is a non-member. A document describing a scheme is not the rule collection. A precisely specified partial scheme can be a member while lacking a rule needed by a particular receiver. |
| `NonemptyClaimContent`: abstract content entities, identified as collections of interpreted claims and their selected semantic relations | The collection contains at least one claim with its participant and predicate meanings, polarity, qualifications and asserted interclaim relations. A whole ClaimGraph or an exact nonempty semantic subgraph can satisfy this condition. | Identify a value by that content and semantic organization under the declared interpretation. An empty collection is a non-member. An uninterpreted graph, a carrier and an episteme about the content are not candidates of this content-entity domain. False, conflicting or insufficiently supported claims can still be members. |

Under these candidate interpretations, `EpistemeInterpretationScheme` is a subkind of `U.Entity`, and `NonemptyClaimContent` is a subkind of `U.Entity`. C.3.1's criterion-entailment branch applies: every member must have the independent semantic identity and reference basis in :4.1.1 and therefore satisfies A.1:4.1. A.6.5 can use either range as an entity ValueKind; actual participation still requires the receiving relation's predicate to obtain.

Recover the candidate independently of the classification. C.3.2 first checks that the proposed candidate is a value in the stated domain; then it judges membership as true, false or unknown. Missing knowledge of a needed rule or content relation leaves that judgment unknown. It does not turn a known document into a rule collection, nor turn an unidentified expression into a fully identified value.

For scheme identity, compare the actual rules and domains, including the dependencies that determine their meaning. A restatement can preserve the scheme when an explicit alignment preserves those rules; agreement on a few outputs cannot establish that identity. A changed interpretation rule or domain identifies another scheme even if its name and document remain. For content identity, apply :4.1.1 to the whole selected content. Two designations from different source editions may return the same content under the same scheme. Source, acceptance, currentness and witness qualifications attached to a designation do not enter the designated semantic base merely because they accompany it, as in A.6.6. When the selected content itself asserts such a fact, that assertion belongs to the content being compared. A change of graph encoding preserves content only when the interpretation supplies the complete correspondence; graph shape alone supplies none.

The kinds themselves continue when their candidate domains and operative membership distinctions remain the same under C.3.1's comparison. Rewording the declaration or citing it from another pattern need not create another kind. Replacing the semantic rule/content criterion with the presence of a schema label would create another classification distinction. A change of one member's rules or claims instead identifies another value; it need not change the kind.

These declarations supply a shared range for the receiving interfaces that cite them. A.1.1 uses `EpistemeInterpretationScheme` for its coherence participant R; A.2.6, A.19.CPM and A.19.SelectorMechanism use it for a bound scheme argument. A.6.0's R7/R8 predicates use `NonemptyClaimContent` for exact dependent content and semantic bases. Reusing one criterion preserves the same meaning of admissible input across those interfaces. A receiver adds any narrower language, semantic-domain or representation condition its operation actually needs; that condition does not become another kind merely because another pattern states it. A recurring independently different classification requires its own C.3 declaration.

**Test replacement in the receiving use.** Resolve the proposed value, check the declared range and any narrower input conditions, then apply the receiver's own predicate or operation law. An eligible scheme need not interpret every actual input. Two eligible schemes need not be equal or admit a meaning-preserving translation. An eligible content value need not be a sufficient basis or an actually used premise. Missing interpretation stops the dependent operation; a false subject predicate remains a different result. For a cross-scheme use, establish the required correspondence, F.9 Bridge and bounded-use assertion where the receiving rule requires them, with A.10 reliance or B.3 assurance only under their own conditions. Membership supplies none of these results.

Retest dependent bindings and conclusions when the resolved value or a used rule changes. Reuse unchanged content only with its established correspondence and applicability. Keep the old value and its qualified conclusions available instead of rewriting them as statements about the replacement. These bounded C.3 declarations do not admit public `U.ReferenceScheme` or `U.ClaimGraph`; E.24.UK governs any separately needed durable U-kind proposal.

#### C.2.1:4.2 - Govern the core direct relation

**Tech name:** `EpistemeConstitutionRelation`.

**Plain reading:** these claims, under this reference scheme, are claims about this exact entity and together constitute one episteme.

##### C.2.1:4.2.1 - Participants and the shared reusable-declaration rule

The constitution predicate uses three actual participants, each an exact `U.Entity`. The content and rule collection have the independent semantic identities given in :4.1.1; the EntityOfConcern has its own subject-governed identity. Recover each before judging whether the relation obtains:

| Relation-participant meaning | What identifies the participant for this constitution |
| --- | --- |
| constitutive claim content | the abstract content entity identified by its complete semantic content and organization under :4.1.1; a selected graph representation supplies an expression, not its identity by itself |
| exact EntityOfConcern | one entity independently identified under its subject's rule |
| effective reference scheme | the abstract rule-collection entity identified by the designation and interpretation rules governing this account, with their domains and dependencies, under :4.1.1 |

This is sufficient for a direct constitution judgment with exact values. A reusable typed interface has an additional question: which candidates may replace a participant under its declared range? For that use, A.6.5 requires a complete SlotSpec with an independently governed ValueKind and designation mode. State the candidate domain, membership criterion, identity rule, and applicability needed by the receiver; use C.3.2 for a local classification and E.24.UK for a proposed public U-kind. Carrying the designation ByValue does not remove the membership requirement.

For reusable designation of the EntityOfConcern, `EpistemeConstitutionRelationSignature` declares `EpistemeConstitutionRelation` as its subject and `U.Entity` as the ranged kind for that participant. Its vocabulary includes the relation designator and the SlotSpec below; its laws are the obtaining and participant-determined identity rules in :4.2.2. Its applicability is the reusable designation and typing of the EntityOfConcern in a constitution assertion or description whose claim content and effective rules are recovered under :4.1.1. This declaration's own claim content, relation-kind EntityOfConcern, and effective FPF interpretation identify one declaration episteme; these subject, range, vocabulary, laws, and applicability contents satisfy A.6.0's `U.Signature` predicate.

| SlotKind | Relation-participant meaning | ValueKind | refMode |
| --- | --- | --- | --- |
| `EntityOfConcernSlot` | exact entity the claims concern | `U.Entity` | `U.EntityRef` |

Use this SlotSpec for the EntityOfConcern designation in A.6.REL:5.5 or B.2:5.1. An eligible designation must resolve to an independently identified entity; that typing alone does not establish that the claims concern it or that the constitution predicate obtains. The other two participants remain necessary exact constituents. Section :4.1.2 supplies bounded C.3 ranges for a receiving typed use; this EOC declaration does not thereby acquire further SlotSpecs. A use that additionally needs `ClaimGraphSlot` or `ReferenceSchemeSlot` must select the range appropriate to its participants and complete its declaration under A.6.5. If the available range does not cover that use, establish the missing criterion before claiming the stronger interface. E.24.UK:4.2c separately retains the public U-kind questions. A card field or tuple position acquires none of this declaration meaning by its label alone.

The separately needed `EpistemeEmpiricalGroundingRelationSignature` and `EpistemeEditionRelationSignature` remain declarations over the governed episteme and holon kinds stated in :4.3 and :4.5. Each declaration is first a C.2.1 episteme: its own claim content declares the relation, its EntityOfConcern is that direct relation kind, and its effective scheme gives those declarations meaning. The A.6.0 predicate judges that same individual's `U.Signature` membership; `RelationSignature` is its relation-facing use, with no second identity.

A complete declaration states its relation-kind designator, the SlotSpecs required by its typed use, direct predicate, occurrence identity, applicability, and any actual dependencies or provided names. A manifest may expose those dependencies or names when a consumer needs them. A readable one-off assertion needs neither a signature nor a manifest; assertion wording does not make its relation obtain.

##### C.2.1:4.2.2 - Obtaining and occurrence identity

`EpistemeConstitutionRelation` obtains exactly when the effective reference scheme supplies a coherent designation and interpretation of the claim graph as claims about the exact EntityOfConcern, and the three participants are constitutively organized as one claim-bearing whole whose claims can in principle be evaluated under that scheme. Merely placing three designations in a card does not make the relation obtain.

The relation occurrence is participant-determined by the exact `<ClaimGraph, EntityOfConcern, ReferenceScheme>` triple. The same triple cannot constitute two distinct `U.Episteme` instances under the shared C.2.1 identity rule. Recognition of that individual as a dependent episteme kind adds a membership judgment under the dependent kind's subject pattern, not another constitution occurrence or discriminator. A tuple may represent the triple, but tuple order and storage keys contribute nothing to identity.

The episteme and the relation occurrence are not identical. The relation is the obtaining organization among the three participants. The episteme is the knowledge holon constructively identified through that organization and its whole-level claim-bearing characteristic.

##### C.2.1:4.2.3 - Ordinary assertion, classification assertion, and explicit occurrence use

An ordinary assertion can state that claim content concerns an entity under a scheme without explicitly naming a relation occurrence. For every direct predicate, keep four jobs separate: the direct pattern defines participant meanings, the obtaining predicate, applicability, and the occurrence-identity rule; the current case supplies the facts that satisfy or fail that predicate; the assertion carries affirmative or negative polarity; and a separately governed evaluation or evidence-use relation states supported, refuted, or unresolved reliance when the receiving use needs it. When a receiving relation or claim needs the exact constitution occurrence, inspect the current ClaimGraph, EntityOfConcern, and ReferenceScheme facts against C.2.1's predicate. Only after those facts satisfy the predicate may the participant-determined identity rule individuate the occurrence for designation. The assertion, designation, occurrence, case facts, and reliance judgment remain different objects.

Each classification judgment has one pattern governing its criterion. `A.1` governs constructive recognition of a candidate as an instance of an already admitted holon kind. `C.3.2` governs a local-kind membership judgment. `E.24.UK` governs the ontology-level decision that admits a public U-kind; it does not classify a project candidate. None of these judgments is a direct admission relation created by C.2.1.

When project work needs a classification judgment as a separately reviewable claim, identify one claim-bearing episteme whose exact EntityOfConcern is the candidate entity. For an admitted holon kind, its claim content states affirmative or negative polarity for the exact classification predicate, names the kind, cites the `A.1` constructive criterion and any kind-specific criterion, designates the direct part-relation occurrences used in the assessment, and cites any evidence-use relations that make supported, refuted, or unresolved reliance inspectable for the declared use. For a local kind, its claim content states the same polarity distinction for the candidate, local kind, selected `KindSignature` edition, context slice, and judgment governed by `C.3.2`; its reliance posture remains separate. A value classification inside another claim can remain claim content of that episteme instead of fabricating a value-shaped EntityOfConcern.

The assertion does not create the candidate, admit a U-kind, or make the candidate change kind when an FPF host is renamed or republished. For example, the assertion that Pump #37 satisfies the constructive `U.System` criterion may be revised when evidence changes, while Pump #37 and the criterion it satisfies retain their independently governed identities.

A card that calls a listed collection a holon is still only a classification assertion episteme. Its assertion polarity is affirmative, but the card alone leaves reliance unresolved for any use that requires `A.1` to recover the exact constituents and grounded part relations, their constructive assembly, the whole's reidentification rule, actual compatibility with a governed larger-assembly construction, a composition-grounded whole-level characteristic, and the already admitted holon kind with its kind-specific criterion. The card form supplies none of those facts and does not make the classification predicate true.

The same constitution rule applies when a reader proposes to use an obtaining F.9 Bridge. Say first in ordinary words what the reader proposes to compare, substitute, translate, publish, or otherwise do; name the direction `d`, use-specific correspondence rule `r`, tolerated semantic loss `t`, and affirmative or negative polarity for named use `u`. Identify that statement as one ordinary C.2.1 assertion episteme: the exact Bridge `b` is its EntityOfConcern, its ClaimGraph designates `<u,d,r,t>` and polarity, and its effective ReferenceScheme makes those designations, the rule, and the tolerance interpretable. The exact `<ClaimGraph, b, effective ReferenceScheme>` triple identifies the assertion. Changing `u`, `d`, `r`, `t`, or polarity changes the claim content and therefore the assertion episteme, not fixed Bridge `b`. Keep this local claim form in ordinary wording: it introduces no public U-kind, universal use relation, or durable CamelCase claim name. Reopen F.18 only if an independent later use actually needs a reusable name.

An affirmative bounded-use assertion is one premise for that use; it is neither permission nor proof that the use occurred. A negative assertion leaves an otherwise obtaining Bridge in place. Use A.10 to classify ordinary bounded reliance on the exact evidence-provenance path: `pass` supports only the named use, `degrade` supports only its named narrower use, and another disposition supplies no support for the attempted use.

Use B.3 only when an actual named assurance claim about this bounded use is current. That assurance result remains separate from the Bridge-use assertion and adds assessment Work, System, Method, assignment, bindings, witnesses, or a reusable note only when the assurance use depends on those identities. A direct domain rule may require an assurance claim for a consequential use, but neither consequence nor a display creates the claim. Neither the A.10 nor B.3 branch authorizes the use. If the use actually happened, recover the actual Work under A.15.1, assertion episteme under C.2.1, publication occurrence under E.17, direct relation under its domain predicate, operation application under A.6.1, or another result under its own pattern.

##### C.2.1:4.2.4 - State rule-content and subject assertions

In ordinary prose, cite the PatternID and state the concrete contribution: what the cited content defines, constrains, tests, distinguishes, or helps the practitioner do. This readable branch is normally sufficient. For example, “use A.1 to test constructive holon recognition” states the needed contribution.

Open an exact defining or constraining episteme edition or ClaimGraph only when its identity changes interpretation, migration, conflict analysis, publication, dependency repair, or reuse. Then identify the subject, predicate or constraint, polarity, exact defining content, case facts, and only the scope, time, scheme, or bounded-use qualifications that change the assertion. Do not fabricate an assertion episteme merely to avoid an ordinary pattern citation.

Definition or constraint is not actual rule-content use. State `derivedUsingRuleContent(dependentContent, baseContent)` only when one identified derivation claim used the exact nonempty base subgraph as a formal premise under a declared inference rule. State `evaluatedAgainstRuleContent(dependentContent, baseContent)` only when one identified criterion-selection claim selected that base for one exact bounded evaluation. Consultation, influence, quotation, provenance, evidence, evaluation Work, and later sufficiency establish neither predicate.

An E.4.PFR row is optional and opens only for a named framework-maintenance, edition-impact, comparison, publication/dependency-repair, or refresh receiver. It represents an already identified assertion; it creates neither the assertion nor a pattern-owner fact.

##### C.2.1:4.2.5 - Address one claim inside an exact episteme edition

`U.EpistemeRef` is the admitted RefKind for designating one already identified `U.Episteme`. Under the effective reference scheme of the receiving assertion or description, its resolution method returns exactly one episteme satisfying the C.2.1 identity rule. A value that resolves to none or more than one is unresolved. The reference, its token or serialization, the resolution act, and the episteme remain different objects. Retargeting the reference designates another already identified episteme; it does not revise either episteme.

Use the reusable C.2.1 value `ClaimAddress` only when a receiving claim or work item needs one exact claim inside a larger ClaimGraph:

```text
C.2.1 ClaimAddress ::= <
  exactEpistemeEditionRef: U.EpistemeRef,
  intrinsicClaimIdentity: identity declared by that exact ClaimGraph
>
```

The second component is not a printed node label interpreted by the episteme's general ReferenceScheme. It is a claim identity that the exact ClaimGraph itself declares and preserves across its admissible representations. Resolve the edition first, then require that its ClaimGraph contains exactly one claim with that intrinsic identity. Resolution fails when the edition is unresolved, the identity is absent or non-unique, or the token belongs only to one rendering or serialization.

Two ClaimAddress values are equal only when they resolve the same exact episteme edition and the same intrinsic claim identity in that edition. Reusing the same visible token in another edition does not preserve the address. An `EpistemeEditionRelation` also does not preserve it by itself; a receiving migration rule must state any claim-to-claim correspondence it uses.

When a ClaimGraph declares no stable intrinsic identity for the needed claim, cite the whole episteme or constitute the claim as its own C.2.1 episteme. Do not invent an address from a heading, row number, file location, or display token.

`C.2.1 ClaimAddress` designates claim content carried by the exact edition. It is neither a U-kind nor a RefKind, turns no claim content into a `U.Entity` or another `U.Episteme`, and carries none of the claim content itself. Use `U.EpistemeRef` for the whole episteme and the admitted reference kind for an independently identified entity or relation occurrence.

##### C.2.1:4.2.6 - Resolve a constituent designation to its exact value

Use a constituent designation when the receiving work needs to recover content or rules from an addressable episteme instead of carrying them by value. Ordinary writing can continue with the expressions and rules available in :4.1.1; it need not create a reference or a finished episteme merely to fit these forms.

```text
C.2.1 ClaimContentDesignation ::= <
  exactEpistemeEditionRef: U.EpistemeRef,
  selection: wholeClaimContent | intrinsic semantic selection declared by that ClaimGraph
>

C.2.1 SchemeDesignation ::= <
  exactEpistemeEditionRef: U.EpistemeRef,
  selection: effectiveScheme | schemeDefinedBy(intrinsic semantic selection)
>
```

Resolve the exact episteme first under :4.2.5. For `ClaimContentDesignation`, recover its whole claim content or the uniquely declared selection, retaining the selected claims' semantic qualifications and selected interclaim relations. A single intrinsic claim can use a :4.2.5 ClaimAddress as the selection. A subgraph selection must likewise be declared by the exact ClaimGraph and resolve uniquely across its admissible representations. A row number, heading or diagram position alone supplies no such identity. When that selection is unavailable, carry the exact content by value, cite the whole episteme, or constitute the needed content as its own episteme.

For `SchemeDesignation`, `effectiveScheme` selects the rules governing the source episteme itself. `schemeDefinedBy` selects content that defines one exact rule collection, with its domain and semantic dependencies; interpret that defining content under the source episteme's own effective scheme. A document can describe a different scheme from the one under which the document is read. A mention, name or example of a scheme is insufficient to select all of its rules. Follow an imported rule only through its exact source and interpretation; an unresolved or circular definition with no independently recoverable rules does not resolve the scheme.

Resolution succeeds only when the exact edition, selection and interpretation determine one value. Preserve an unresolved result when the source is absent, selection is ambiguous or a required rule is missing; do not silently choose the latest edition or a nearby document. The receiving interface then checks its declared range and use conditions under :4.1.2. Resolution alone establishes neither membership nor successful use.

These are composite designation values, not new U-kinds or RefKinds. Use an explicit designation field, such as `claimContentDesignation` or `schemeDesignation`, with the applicable C.2.1 form; an A.6.1 `ByRef` argument can specify this resolution method while keeping the resolved value as its argument range. The admitted `U.EpistemeRef` inside the form retains its own referent range. Two designations are the same designation only when they select the same constituent through the same exact episteme edition and selection. Different designations can resolve the same semantic value. Retargeting changes the designation and requires resolution again; it changes neither the old episteme nor the old value.

**Apply the distinctions together.** A declaration D describes a rule set S in ordinary mathematical prose, while S declares a propositional language with material implication and the inference rule that permits `q` from `p` and `p => q`. Selecting D's `effectiveScheme` returns the rules for reading D; selecting the exact content that defines S returns S. A formatting-only stylesheet is an identified rule collection but fails `EpistemeInterpretationScheme` membership. An exact partial S can pass membership and still leave `unless` uninterpreted in a proposed input; a consuming operation requiring that interpretation stops.

For an A.1.1 comparison, let R be the complete S and let M and E have the same effective S. Here the actual participant R is S, the abstract rule collection described by D. R passes the declared range; the coherence claim still requires its independently admitted predicate P to hold for the exact M and E content. Changing the interpretation of `=>` while retaining the signs yields another R and requires a new coherence judgment, including the bridged branch if its conditions now apply. Reprinting D while preserving its complete defining content changes no R.

For an A.6.0 basis use, let the exact dependent content be `q` and the selected base be the two claims `p` and `p => q`, under the stated inference rule. Both are `NonemptyClaimContent`. The base can be sufficient for deriving `q`, but R7 actual use additionally needs the identified derivation claim that used those premises. Replacing the base with the single claim `p` preserves membership and loses that sufficiency under the stated rule. Adding an asserted new reason to the dependent account changes its content even if the field still displays `q`. Two exact editions that designate the same unchanged base under S provide two source qualifications of that semantic base, not two bases merely because the addresses differ. An episteme asserting that this two-claim base is sufficient for deriving `q` under S can take that exact abstract content entity as its EntityOfConcern. That assertion has its own claim content and effective scheme; it does not replace the base it concerns.

#### C.2.1:4.3 - Add empirical grounding through its own relation
**Tech name:** `EpistemeEmpiricalGroundingRelation`.

**Plain reading:** these designated empirical claims of this episteme are inspectable through exact observation, intervention, measurement, or test relations involving this grounding holon.

C.2.1 uses **explicitly designated partial coverage**. For one candidate grounding occurrence, select one exact claim subgraph `C` from the episteme's already constitutive ClaimGraph. `C` may include formal claims but must contain at least one empirical claim. The occurrence says that every empirical claim in `C` is grounded; it says nothing about empirical claims outside `C`. To claim full empirical grounding for the episteme, `C` must contain every empirical claim in that episteme. Purely formal epistemes or selected claim subgraphs fall outside this relation's applicability; their formal derivation and any assurance remain under their applicable rules.

For every empirical claim in `C`, state a concrete claim-to-world mapping under the episteme's effective ReferenceScheme to independently governed direct observation, intervention, measurement, or test relation occurrences involving the exact grounding holon. The mapping names what observation, intervention outcome, measured characteristic, or test result bears on that claim. One measurement involving the same holon cannot ground an unrelated claim.

The selected claim subgraph is by-value predicate content drawn from the episteme's ClaimGraph; it is not a third world-side relation participant, another episteme constituent, or a new U-kind. An assertion about grounding designates that subgraph and the claim-to-world mappings but creates none of the mapped occurrences.

Applying the declaration rule in 4.2.1, `EpistemeEmpiricalGroundingRelationSignature` is one declaration episteme whose exact EntityOfConcern is `EpistemeEmpiricalGroundingRelation`; the same individual has `U.Signature` membership and relation-facing `RelationSignature` use only under `A.6.0`. Its complete declaration includes the covered-claim-subgraph rule, obtaining predicate, maximal-continuous-interval identity rule, applicability, actual dependencies and provided names, and these participant SlotSpecs:

| SlotKind | Relation-participant meaning | ValueKind | refMode |
| --- | --- | --- | --- |
| `GroundedEpistemeSlot` | episteme containing the exact covered claim subgraph | `U.Episteme` | `U.EpistemeRef` |
| `GroundingHolonSlot` | exact holon involved in the mapped observation, intervention, measurement, or test relations | `U.Holon` | `U.HolonRef` |

`EpistemeEmpiricalGroundingRelation` over participants `(E,H)`, with `covered=C`, obtains exactly while exact covered claim subgraph `C` contains at least one empirical claim and every empirical claim in `C` has a current claim-to-world mapping to the required independently governed direct observation, intervention, measurement, or test relation structure involving `H` under E's effective ReferenceScheme. Every mapped relation required by that coverage must obtain. An exact direct evaluation relation counts as part of the empirical test only when the mapping states its concrete use in that test; otherwise evaluation and evidence can support or challenge an assertion about grounding but are not its world-side base.

One occurrence is identified by `<episteme, exact covered claim subgraph, grounding holon, maximal continuous interval during which the complete coverage predicate is true>`. Closing the open end of that interval refines the description of the same occurrence. Demonstrated failure of any required mapping followed by restored complete coverage yields another occurrence. Evidence or evaluation availability alone establishes neither obtaining nor nonobtaining and proves no temporal gap. If the complete coverage predicate is known to obtain, grounding continues without a stored report or work log. If it is known not to obtain, the relation does not obtain. If its truth is unknown, an affirmative grounding assertion has unresolved reliance for the declared use; that posture is not a third world-side grounding state.

The grounding holon need not be identical to the EntityOfConcern. One method-description episteme may have one grounding occurrence for a claim subgraph mapped to exact enactment work and another for a different claim subgraph mapped to the system whose behavior was observed. Each occurrence names its own `C`, `H`, and mappings. Sharing one grounding holon makes comparison inspectable but proves neither the same subject, the same claim content, nor coverage of any unlisted claim.

#### C.2.1:4.4 - Keep neighboring uses under their direct relations

| Current distinction | Relation or object to use | Why it stays outside the core constitution relation |
| --- | --- | --- |
| classification judgment or assertion needed as a separate claim-bearing object | the `A.1` recognition judgment for an admitted holon kind or the `C.3.2` membership judgment for a local kind; one C.2.1 episteme when a receiving review treats the judgment as a separate claim-bearing object | the governing criterion states the membership condition; the classification judgment evaluates the candidate under it; the assertion carries that judgment but neither creates the candidate nor admits the kind |
| claim scope | exact `U.ClaimScope` and its A.2.6 membership semantics | scope delimits where claims hold; it does not identify every episteme |
| concern-bearing viewpoint use | one exact `U.Viewpoint` episteme P selected for one named describing use | selection states the concern under which the description is used; it neither establishes conformance nor enters episteme identity |
| view | the same episteme individual recognized as `U.View` when an exact `EpistemeViewpointConformanceRelation` to at least one exact viewpoint episteme obtains | conformance, source-to-receiving construction, current-use selection, publication, form, and carrier remain different relations or objects |
| bounded model use | optional relation to one `BoundedModelUseStructure : U.Structure` under A.1.1 | model-use organization can qualify interpretation without becoming a universal identity component |
| justification structure | exact `JustificationGraph` content | a justification structure organizes inferential dependencies without becoming claim content |
| evidence use or assurance for a claim | for ordinary bounded reliance, the descriptive A.10 evidence-provenance path, the independently established direct relations it cites, and local `RelianceDisposition`; when an actual named assurance claim is current, the exact B.3 `AssuranceResult` or its non-positive disposition | evidence and assurance can support, narrow, or stop reliance on the claim while the episteme's identity remains fixed |
| publication | exact publication occurrence and publication form under E.17 and E.24.PUB | making an edition available does not constitute or reidentify it |
| presentation carrier | any exact `U.PresentationCarrier` under E.17 and E.24.PUB | bearing a publication form or rendered expression does not constitute or reidentify the episteme |
| representation and admissible operations | the representation scheme, selected elements and operations used for the represented episteme, with any required correspondence or transition governed through :4.0 | a change of scheme or admitted operations can change the available work |

Names ending in `Slot` are admissible here only as SlotKinds inside the exact `RelationSignature` governed by the neighboring direct relation pattern. A card or other episteme form carries participant designations in ordinary fields; it does not acquire SlotKinds by using similar field labels. None of those neighboring SlotSpecs belongs to `EpistemeConstitutionRelationSignature`.

#### C.2.1:4.5 - Relate distinct episteme editions explicitly

**Tech name:** `EpistemeEditionRelation`.

**Plain reading:** this later episteme continues this earlier episteme as an edition under one applicable continuity rule.

`EpistemeEditionRelation` has exactly two direct participants. Applying the declaration rule in 4.2.1, `EpistemeEditionRelationSignature` is one declaration episteme whose exact EntityOfConcern is `EpistemeEditionRelation`; the same individual has `U.Signature` membership and relation-facing `RelationSignature` use only under `A.6.0`. Its complete declaration includes the direct predicate, participant-determined identity, applicability, actual dependencies and provided names, and these SlotSpecs:

| SlotKind | Relation-participant meaning | ValueKind | refMode |
| --- | --- | --- | --- |
| `EarlierEpistemeSlot` | exact episteme continued by the later edition | `U.Episteme` | `U.EpistemeRef` |
| `LaterEpistemeSlot` | exact episteme that continues the earlier edition | `U.Episteme` | `U.EpistemeRef` |

The relation obtains only when all of these conditions hold:

1. the two epistemes have different C.2.1 identities;
2. the later episteme actually uses the earlier episteme as the source for the claimed revision, refinement, or supersession;
3. one applicable edition-continuity policy or rule states which claim, EntityOfConcern, and effective-reference-scheme features must be preserved, which may deliberately change, and what counts as continuation for this episteme family;
4. the exact preserved and deliberately changed features satisfy that rule;
5. no failure condition in that rule classifies the case as a fork, translation, retargeting, or independent reconstruction instead.

Work, an enacted Method, provenance, and change results supply case facts. Their labels do not make continuity true. C.2.P may recover the source expression and source-to-revision use; the direct change patterns supply exact changed features. If the continuity claim separately consumes a first-existence fact, apply the shared boundary in 4.9. A missing required rule or fact blocks only that positive edition claim.

One occurrence is identified by the exact `<earlier episteme, later episteme>` pair. Two revision Work occurrences do not create two edition occurrences for the same pair. The relation is acyclic in its earlier-to-later direction. A renamed file, later publication, shared title, bare provenance edge, or Method named “revision” establishes no occurrence.

Several edition occurrences form a lineage structure only when a receiving use depends on their organization. A separately identified edition collection remains under A.14; collection membership does not establish continuity. `PhaseOf` may describe one unchanged episteme over a proper interval but does not connect two different C.2.1 identities.

When claim content, EntityOfConcern, or effective reference scheme changes, the later object is another episteme. Apply `A.6.4` separately when the current claim is effect-free retargeting between epistemes with different EntitiesOfConcern; retargeting alone does not establish edition continuity. A changed publication form alone identifies neither another episteme nor an edition relation.

#### C.2.1:4.6 - Keep descriptions, cards, publications, and representations downstream
A claim-bearing filled card can itself be an episteme when its claim content, EntityOfConcern, and effective reference scheme are recoverable. The reusable arrangement of that card can instead be a publication form, and a selected graphical or tabular element can participate in a C.29 representation. Identify each object through its own constitution and the direct relation in which it participates; visible shape does not determine its kind.

When a card or other form designates the participants of one direct relation, its field labels may correspond to SlotKinds in that relation's `RelationSignature`, and its field values may be by-value designations or references of the declared refModes. The form is not a filled direct relation occurrence; supplying fields does not make the predicate obtain or provide occurrence identity.

In a relational assertion, the claim graph designates the actual participants and states affirmative or negative polarity for the direct predicate. The direct pattern defines that predicate and the occurrence-identity rule; current case facts determine whether the predicate is satisfied or failed. A forecast, scenario, counterfactual, permission, or another claim family names its exact direct governor rather than using one common catch-all field. Only when an explicit reliance judgment is current for the declared use does `A.10` or the receiving evaluation separately state supported, refuted, or unresolved reliance. An affirmative assertion may designate an occurrence only after the case facts satisfy the predicate and the direct identity rule individuates that occurrence; a negative assertion creates no failed world-side occurrence. In a relation-occurrence description episteme, the EntityOfConcern is that exact already individuated occurrence. The assertion and description retain their own C.2.1 identities. Their forms do not by themselves supply case facts or the occurrence-identity rule, or establish obtaining; evidence supporting the case conclusion and any constitutive contribution are governed separately by the relevant evidence and direct-relation rules.

A designator designates an already recoverable referent. A governed reference resolves to that referent under an effective reference scheme.

For publication, `E.17` and `E.24.PUB` govern the occurrence that makes a selected edition available to a declared audience for a bounded use, the form that expresses it, and the `U.PresentationCarrier` that bears the form. Plain **published episteme** names the episteme's contingent participation in that occurrence. Its C.2.1 identity stays fixed before, during and after that availability relation.


One completed inspection card shows why the distinctions matter. Its filled claims can identify one episteme; its reusable layout can be a publication form; its paper sheet or file can be a presentation carrier; and a publication occurrence can make the selected card episteme edition available to the maintenance team. None of those uses makes the others identical.

Republishing the same claims about the same subject under the same effective scheme with another form or carrier preserves the episteme. Changed claim content, subject or effective scheme identifies another episteme. If the account also needs the rendering Work, use the conditional Work branch in :4.0.

A tuple can represent the identity triple and a graph or hypergraph can represent claim, justification, dependency, or relation structure. Use `C.29` for an unresolved mathematical-lens choice, transfer or reliance question. `ClaimGraph` names the semantic content being represented; `JustificationGraph` names the separately governed inferential organization. Nodes and edges in a selected graph remain representation elements. An explicit correspondence can relate one selected representation element to an independently recovered object, but it neither identifies the two nor makes the representation element a participant of the represented direct relation.

#### C.2.1:4.7 - Preserve description and meta-description recursion

If episteme `E1` describes pump `P`, `P` is the EntityOfConcern participant in the constitution relation that identifies `E1`. If review episteme `E2` describes `E1`, then `E1` is the EntityOfConcern participant for `E2`. The two relations have different triples and therefore identify different epistemes.

An episteme may describe itself when its own identity remains recoverable. Self-reference never closes an assurance argument by itself. Each justification or evaluation path terminates in independently governed evidence, observation, or formal derivation rather than in a cycle of claims that cite one another.

Description and specification use remain distinct. A Description episteme is admitted for specification use only when the E.10.D2 conditions are satisfied: checkable claims and a named harness or validation relation. If the relying use selects a viewpoint, name that describing use and preserve or update its exact selection only when the selection affects reliance. Formal notation alone does not grant specification use or change the episteme's kind.

#### C.2.1:4.8 - Locate the change before updating episteme identity

| Observed change | Disposition |
| --- | --- |
| claim content, EntityOfConcern, or effective reference scheme changes | identify another episteme; use `EpistemeEditionRelation` only for revision, refinement, or supersession when its historical-continuation predicate obtains, and use `A.6.4` separately only for an exact retargeting that satisfies its own predicate; otherwise stop at the new identity without inferring continuity |
| the explicit empirical-claim coverage predicate begins to obtain, ceases to obtain, or is restored | evaluate `EpistemeEmpiricalGroundingRelation` continuity for the exact covered claim subgraph and grounding holon; do not change episteme identity unless a core discriminator also changed |
| an evidence item, evaluation report, evidence store, or work log becomes available or unavailable without an established change in the complete claim-coverage predicate | revise only the separately governed support, warrant, confidence, evidence-use relation, or receiving-use reliance posture that changed; the mapped direct relations still determine world-side grounding and occurrence continuity: known complete coverage continues, known coverage failure remains nonobtaining, and uncertainty about coverage gives an affirmative grounding assertion unresolved reliance rather than a third world-side state |
| candidate episteme E or viewpoint episteme P changes | identify the changed episteme under C.2.1, then test the new exact E/P pair under `E.17.0`; for fixed E and P, conformance cannot change because of evaluator, evidence, project, publication, or current use, so state any changing adequacy or evaluation as a separate claim |
| one named describing use selects one already identified `U.Viewpoint` episteme P | update only that use's exact viewpoint selection; the selection creates no context object, selects no view, and establishes neither conformance, `U.View` membership, nor episteme identity |
| claim scope changes | update the exact `U.ClaimScope` and its A.2.6 membership semantics; do not infer another episteme automatically |
| selected bounded model-use or multi-view structure changes | update the exact collection or structure relation and re-evaluate affected interpretation claims; do not infer another episteme or view family automatically |
| publication form, carrier, rendering, audience, bounded use, or publication occurrence changes | establish the exact E.24.PUB change only; publication is not view membership or episteme succession |
| mathematical or tool representation changes | use `A.6.3.RT` for a same-EntityOfConcern representation transition, or the applicable direct transition pattern for another transition; use `C.29` only for an unresolved mathematical-lens choice, transfer or reliance question |

#### C.2.1:4.9 - Hand episteme transformations to their subject patterns

**Shared identity-inception boundary.** Work or transformation can explain how an entity came about, but C.2.1 by itself establishes neither when that entity first existed nor that the work caused its inception. Open this boundary only when a current receiving claim asks whether a new entity began. Then use the subject's direct inception rule: its pattern defines the predicate and identity rule, and current case facts must satisfy them. If no such rule is recoverable, return one `missing-governor` blocker naming the entity or candidate basis, available case facts, required inception predicate, and receiving use. When the current question is only changed episteme identity, form, representation, view, or publication, do not open this boundary.

When inception is attributed to Work, apply **A.15.PROD:4.5**. Begin with the subject's exact `productIdentitySpecification` and its named applicability predicate or filled local claim for the candidate basis, subject context, and boundary. Then recover actual Work effects and the declared Work-to-change and change-to-identity bases, locate the earliest satisfying `inceptionBoundary`, and identify exact `identityClosingWork`. Designate the resulting entity only on the after-side of that boundary and retain the exact specification and applicability basis used for the claim. A missing required basis stops the positive claim; missing recoverable Work granularity for `identityClosingWork` returns that section's work-granularity blocker.

A.6.2-A.6.4 define episteme-to-episteme morphing, source-to-receiving viewing construction, and retargeting. Identify every source and receiving episteme independently under C.2.1 before testing the exact transformation relation. Each transformation pattern states which identity discriminator is preserved or changed and names the exact correspondence, reinterpretation, or retargeting relation on which it relies. When a possible Bridge between exact F.17 cells is current, use F.9 to test whether that relation obtains. If the morphism relies on that Bridge for a proposed use, state a separate C.2.1 assertion with the Bridge as EntityOfConcern and `<u,d,r,t>` plus polarity in its ClaimGraph, then use A.10 for ordinary evidence reliance or B.3 only when an actual named assurance claim is current; none of those facts makes the morphism application occur. Categorical function, mapping, or tuple notation creates no direct relation occurrence.

For an A.6.3 source-to-receiving viewing construction, the two identified epistemes may retain the same EntityOfConcern while claim content or effective scheme is restricted. `E.17.0` alone judges whether the receiving episteme conforms to an exact viewpoint and therefore has dependent `U.View` membership. Direct authoring or query generation can yield a candidate episteme without an A.6.3 construction, and neither route creates a multi-view family. For retargeting, the EntityOfConcern changes and the case names the exact domain correspondence, retargeting rule, or relation on which it relies. An F.9 Bridge is additional only when the case separately asserts a semantic relation between exact F.17 local senses from different semantic contexts and the F.9 predicate obtains. For a same-EntityOfConcern representation transition, use A.6.3.RT; the represented episteme may remain unchanged while the representation scheme and admitted operations change.

#### C.2.1:4.10 - Relation and neighboring-object reference

| Current object | FPF kind or relation | Subject pattern |
| --- | --- | --- |
| `U.Episteme` | one knowledge holon with identity `<claim content, EntityOfConcern, effective ReferenceScheme>` | C.2.1 |
| `EpistemeConstitutionRelation` occurrence | the obtaining direct relation among the exact claim graph, exact EntityOfConcern, and effective reference scheme that constructively identifies one episteme | C.2.1 and `A.6.REL` |
| `EpistemeEmpiricalGroundingRelation` occurrence | the direct relation between one identified episteme and one exact grounding holon for one exact covered claim subgraph containing at least one empirical claim, while every empirical claim in that subgraph has a current mapping to the required observation, intervention, measurement, or test relations involving that holon; evaluation or evidence supports an assertion unless explicitly mapped as part of the empirical test | C.2.1 and the governing observation, intervention, measurement, test, evaluation, or evidence patterns |
| classification assertion episteme needed as a separate claim-bearing object | a claim-bearing episteme whose EntityOfConcern is the exact candidate and whose claim content states a classification judgment under the exact governing criterion: `A.1` for an admitted holon kind or `C.3.2` for a local kind | C.2.1 for assertion identity; the pattern governing the criterion for the judgment; `E.24.UK` only for public U-kind admission |
| `EpistemeEditionRelation` occurrence | the direct historical continuation relation between one exact earlier episteme and one exact later episteme; exact source use, the applicable continuation policy or rule, and the preserved and deliberately changed claim, EntityOfConcern, and scheme features decide whether it obtains; Work, Method, provenance, and change facts supply case facts only; apply the shared 4.9 inception boundary only when that separate fact is consumed | C.2.1, coordinated with `C.2.P`, A.3.1, A.3.4, and C.2.1:4.9 only for a separately current inception claim |
| `EpistemeConstitutionRelationSignature` | the declaration episteme for reusable EntityOfConcern designation under :4.2.1, with `EntityOfConcernSlot`, `U.Entity`, and `U.EntityRef`; typed replacement of claim content or effective scheme needs additional independently governed ranges and SlotSpecs | C.2.1:4.2.1, `A.6.0`, and `A.6.5` |
| `EpistemeEmpiricalGroundingRelationSignature` or `EpistemeEditionRelationSignature` | one C.2.1 declaration episteme whose EntityOfConcern is its direct relation kind; A.6.0 judges same-individual `U.Signature` membership, and `RelationSignature` is its relation-facing use with the complete semantics and SlotSpecs stated in :4.3 or :4.5 | C.2.1 for declaration identity, `A.6.0` for membership and reusable vocabulary, and `A.6.5` for SlotSpecs |
| `SlotSpec` | one declaration-content component of an identified complete `RelationSignature` | `A.6.5` |
| assertion or description episteme | a claim-bearing episteme that states or describes one of the direct relations | C.2.1 and the direct claim or description pattern |
| `U.MethodDescription` | the same `U.Episteme` individual when A.3.2 recognizes one admitted `U.Method` as its exact EntityOfConcern and its claims, interpreted under the effective `ReferenceScheme`, make at least one substantive claim about that method as a way of doing; mention, bibliographic metadata, or approval alone does not establish membership, and adequacy for a receiving use is evaluated separately | C.2.1 for episteme identity; `A.3.2` for dependent-kind membership |
| `U.View` | the same `U.Episteme` individual when it conforms to at least one exact `U.Viewpoint` episteme; formally, when `EpistemeViewpointConformanceRelation(E,P)` obtains for that pair | C.2.1 for episteme identity; `E.17.0` for dependent-kind membership; `A.6.3` only when source-to-receiving construction is current. Conformance of E to P, that construction, current-use selection, and publication remain separate. |
| describing-use viewpoint selection | one named describing use selects one already identified `U.Viewpoint` episteme through an exact reference; it selects no view | `E.10.D2` and `E.17.0` |
| multi-view collection or organization | an exact C.13 collection only when a receiving use depends on the plurality as a collection, and an exact A.22 `U.Structure` only when that use additionally depends on organization among those views | `C.13`, `A.22`, and the direct organizing relations |
| cross-view correspondence, consistency, realization, trace, or change-impact claim | one exact direct subject relation under its own governor; a C.2.1 episteme may assert or describe it, but a heading, edge, carrier, or E.17 publication invents no relation | the exact direct relation pattern; when none is current, return an exact missing-relation blocker naming the participants, required predicate and use, and missing governor |
| publication occurrence | the occurrence that makes one selected episteme edition available to a declared audience for a declared bounded use | `E.17` and `E.24.PUB` |
| publication form | the arrangement, notation, or rendering convention that expresses the selected episteme edition for that publication use | `E.17` and `E.24.PUB` |
| `U.PresentationCarrier` | the exact physical or digital carrier that bears the publication form | `E.17` and `E.24.PUB` |
| mathematical representation | a mathematical representation used for the stated modeling or reasoning purpose | the applicable mathematical or representation pattern; `C.29` only for an unresolved mathematical-lens question |

This reference table keeps the neighboring objects and relations visible after the application method. Ordinary prose names only the current object and its direct relation. A sentence such as “Model M concerns Pump P under Scheme S” is sufficient until another use needs explicit empirical grounding, a classification assertion, occurrence identity, edition continuity, publication, or representation correspondence.

