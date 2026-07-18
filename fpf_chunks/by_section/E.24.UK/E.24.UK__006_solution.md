---
chunk_kind: "child"
pattern_id: "E.24.UK"
pattern_title: "U-kind Admission and Ontic Settlement"
section_id: "E.24.UK:4"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/E.24.UK/E.24.UK__006_solution.md"
commit_sha: "89fcd508edbf9a49dc956955a42884fbca43f88c"
heading_path:
  - "E.24.UK — U-kind Admission and Ontic Settlement"
  - "E.24.UK:4 — Solution"
line_start: 83153
line_end: 83345
dependencies:
  - "A.11"
  - "A.3.2"
  - "A.6.0"
  - "A.6.3"
  - "A.6.5"
  - "A.6.REL"
  - "A.8"
  - "C.2.1"
  - "C.29"
  - "C.3"
  - "C.3.1"
  - "C.3.2"
  - "E.10"
  - "E.17.0"
  - "E.24"
  - "E.24.CD"
  - "E.24.PUB"
  - "F.18"
  - "U.MethodDescription"
  - "U.View"
  - "U.Viewpoint"
keywords:
---

### E.24.UK:4 - Solution

Treat durable U-kind admission as an ontology decision about one candidate classificatory distinction, not as a relation between a public name and a settlement. Recover the governed individuals, identity or membership rule, intended extent, non-member boundary, and action-facing claims first. Record the decision in a DRR or another claim-bearing episteme under `E.9`; the decision creates no project-side `U.Relation` occurrence.

Every admitted durable U-kind has one primary E.24-compatible settlement. For a newly admitted durable kind, that settlement establishes exactly one of these forms:

- a root U-kind for a governed subject whose identity and extent are carried by its direct pattern;
- a same-individual dependent U-kind whose direct pattern adds a stable membership condition to individuals already admitted under one root U-kind;
- an identity-dependent U-kind whose direct pattern identifies a distinct individual through an exact dependence on one named root-kind individual plus every additional discriminator.

When no new durable U-kind is admitted, the same decision instead records `reuse` of an exact already admitted durable U-kind, `local-kind` under one exact C.3.2 declaration, or `reject` with the recovered non-kind object and its direct governor.

A public Tech label follows the admission decision through `F.18`. The spelling can improve retrieval, but it supplies neither the classified individuals nor their identity, membership, or extent. `U.Ontic` names the ontology-unit kind and does not replace the subject kind governed by that ontology unit.

Use this compact decision episteme when the admission is contested or load-bearing:

```text
UKindAdmissionDecision:
  CandidateGovernedIndividuals:
  CandidateIdentityOrMembershipRule:
  IntendedExtentAndNonMemberBoundary:
  ActionFacingClaimsEnabled:
  ExistingKindAndRelationCoverage:
  E24SettlementRef:
  DirectGoverningPatternRef:
  AdmissionDisposition: root | same-individual-dependent | identity-dependent | reuse | local-kind | reject
  DependentRootUKindRef?:
  SameIndividualMembershipRuleRef?:
  IdentityDependenceRelationAndDiscriminators?:
  ReusedUKindRef?:
  LocalKindDeclarationRef?:
  RejectedCandidateRecoveryRef?:
  CandidateSpelling?:
  NamingPatternIfAdmitted?:
  ReopenCondition:
```

`AdmissionDisposition` is the only disposition field. Supply only the detail required by its value: `DependentRootUKindRef` plus `SameIndividualMembershipRuleRef` for `same-individual-dependent`; `DependentRootUKindRef` plus `IdentityDependenceRelationAndDiscriminators` for `identity-dependent`; `ReusedUKindRef` for `reuse`; `LocalKindDeclarationRef` for `local-kind`; and `RejectedCandidateRecoveryRef` for `reject`. The root case is already completed by `E24SettlementRef` and `DirectGoverningPatternRef`.

The decision episteme describes the selected ontology settlement. It is neither the candidate kind nor any individual classified by that kind. `CandidateSpelling` and `NamingPatternIfAdmitted` remain optional because admission can be settled before the final public name.

#### E.24.UK:4.1 - Positive Test For A Durable U-kind

Test a proposed new durable U-kind against these eight conditions. It may receive `root`, `same-individual-dependent`, or `identity-dependent` only if all eight hold:

1. **Governed individuals.** The candidate classifies identifiable governed individuals, not source expressions, declaration fields, table columns, reference suffixes, publication forms, or mathematical representation elements.
2. **Stable identity or membership.** The direct pattern supplies an identity, grounding, recognition, or membership rule that reidentifies individuals and determines whether they enter the intended extent.
3. **Reviewable witness.** The settlement cites the exact operational witness. For a relation kind, this is the direct relation pattern that governs relation-participant meanings, obtaining, and occurrence identity. For another candidate, use its direct constructive, classificatory, or typed-membership witness. A signature, Concept-Set row, formal declaration, or mathematical trace counts only when its governing pattern states the correspondence to the governed individuals.
4. **Action-facing need.** FPF users need to state, compare, constrain, transform, or otherwise reason about those individuals under this kind; a wording preference alone does not qualify.
5. **Non-duplication.** Existing U-kinds, direct relations, declaration SlotKinds, local C.3 kinds, and selected structures cannot preserve the needed distinction without this durable kind.
6. **Direct governing locus.** One primary governing pattern or accepted governed source set states the kind's identity or membership, intended extent, admissible use, and non-use boundary.
7. **E.24-compatible settlement.** The proposed durable kind has a root, same-individual-dependent, or identity-dependent settlement; the decision names the primary governed subject kind, identity or membership rule, direct governing pattern, named dependent-pattern reliance, and non-use boundary.
8. **By-value dependence.** Current or selected dependent patterns actually rely on the kind by value rather than only repeating its label.

If any positive-admission condition fails, do not force the candidate into a durable root or dependent form. Select `reuse` when an admitted durable kind already covers the distinction, `local-kind` when bounded C.3.2 classification is sufficient, or `reject` when no classificatory distinction remains. Recover the exact direct relation, declaration component, selected structure, episteme, publication form, representation element, or source wording that carries the current claim. Only after disposition is settled may `F.18`, `F.17`, `F.8`, or `F.5` select and expose a public name.

#### E.24.UK:4.2 - Six Admission Dispositions And Current Examples

The typed `AdmissionDisposition` has exactly six values:

1. **`root`.** The candidate classifies individuals whose identity, extent, and recognition are governed by its primary direct pattern.
2. **`same-individual-dependent`.** The candidate classifies individuals already admitted under one root U-kind. The root pattern keeps individual identity; the dependent pattern adds a stable membership condition and an action-facing use.
3. **`identity-dependent`.** The candidate classifies a distinct individual whose identity cannot be stated without one exact dependence on a named root-kind individual. The dependent pattern states that dependence and every additional identity discriminator.
4. **`reuse`.** The needed individuals and distinction are already covered by one admitted durable U-kind. Reuse that exact kind and its direct governing pattern; do not admit a duplicate root or dependent kind.
5. **`local-kind`.** Record this non-admission exit only with one exact current C.3.2 declaration through `LocalKindDeclarationRef`. The distinction remains local under the C.3 family and does not become a root or dependent durable U-kind; E.24.UK does not restate the declaration's internal mechanics.
6. **`reject`.** No durable or local classificatory distinction survives recovery. Keep the exact relation, declaration component, selected structure, episteme, publication object, representation element, or source wording that carries the claim. A contingent qualification whose membership is only temporary participation in a relation belongs here; use Plain relation-defined wording when useful.

Only `root`, `same-individual-dependent`, and `identity-dependent` admit the candidate as a durable U-kind. `reuse`, `local-kind`, and `reject` are distinct exits, not weakened dependent admissions.

The following table is the authoritative disposition for every candidate used as an admission example in this pattern:

| Candidate | `AdmissionDisposition` and constructive form | Governing identity or membership rule | Boundary that preserves the disposition |
| --- | --- | --- | --- |
| `U.System` | `root`; retained root U-kind | `A.1` remains the direct owner of system identity and recognition | role assignment, capability, method enactment, performed work, transformation participation, and evidence remain neighboring relations; none makes an otherwise failing candidate a system |
| `U.Episteme` | `root`; retained root U-kind | `C.2.1` identifies one episteme by exact claim content, exact EntityOfConcern, and effective `U.ReferenceScheme` through `EpistemeConstitutionRelation` | carrier, viewpoint, publication, and dependent-kind membership add no second episteme identity |
| `U.Method` | `root`; retained root U-kind | `A.3.1` governs one semantic way of doing and its method-holarchy identity and composition rules | method description, mechanism, work plan, and dated work remain different governed objects |
| `U.Work` | `root`; retained root U-kind | `A.15.1` is the sole direct owner of the dated performed occurrence and of the judgment that records resolve to it under the declared work-identity tolerances and continuity-policy description | actual change, A.6.1 result-position bindings, domain results, delivery, acceptance, evaluation, and downstream effects retain separate direct owners; none is a work-identity discriminator or a generic work-result relation |
| `U.Relation` | `root`; retained root U-kind | `A.6.REL` supplies common occurrence discipline and each direct relation pattern supplies participant meanings, obtaining, and occurrence identity | an assertion, description, designator, reference, tuple, or graph edge is not the obtaining occurrence |
| `U.WorkPlan` | `same-individual-dependent` under `U.Episteme`; retained | `A.15.2` recognizes an episteme whose content declares intended `U.Work` over a horizon through plan items and their organization; C.2.1 keeps identity | planned methods, role conditions, windows, budgets, and acceptance targets are plan content or neighboring relations and do not make the intended work occur |
| `U.RoleAssignment` | `same-individual-dependent` under `U.Relation`; retained | `A.2.1` governs an obtaining relation occurrence among holder system, role value, role-taxonomy episteme, and effective reference scheme, continuing while the predicate obtains without interruption for those participants | an interval belongs to an assertion or occurrence description; a model-use structure qualifies only a narrower receiving use unless a direct species makes it required |
| `U.Capability` | `identity-dependent` under the named holder `U.System`; retained | `A.2.2` identifies the holder's ability through holder identity, work family or result class, envelope, measure set, qualification window, and currentness condition | evidence, evaluation, assignment, and actual work remain neighboring relations and do not constitute the capability by record presence |
| `U.MethodDescription` | `same-individual-dependent` under `U.Episteme`; retained | `A.3.2` admits an already identified episteme whose exact EntityOfConcern is one admitted `U.Method` and whose claims, interpreted under the effective `U.ReferenceScheme`, make at least one substantive claim about that method as a way of doing: its transformation or enactment concern, applicability, precondition, effect, bound, or internal method composition; C.2.1 keeps identity | naming the method, giving bibliographic metadata, or stating approval alone does not establish membership; claims about the internal organization of one composite method retain that composite `U.Method` as EntityOfConcern, while claims about an independent relation structure among several methods have the selected `U.Structure` as EntityOfConcern and do not meet this membership rule; adequacy for a receiving use and changes of C.29 representation, publication occurrence, publication form, `U.PresentationCarrier`, approval claim, or work occurrence remain separate |
| `U.Viewpoint` | `same-individual-dependent` under `U.Episteme`; retained | C.2.1 identifies exact episteme P whose EntityOfConcern is one A.22-selected viewpoint-convention `U.Structure`; E.17.0 recognizes membership of that same P only when its fixed claims state the target-kind criterion, exact concerns and stakeholder or audience referents when current, independently admitted episteme kinds, semantic-form and coverage rules, completeness or omission rules, and the describing-use frame; under the effective reference scheme, `ViewpointId i` designates exact P and resolving `U.ViewpointRef r` that uses i yields P, while i, r, and P remain distinct | neither designation nor reference resolution grants `U.Viewpoint` or `U.View` membership; E.17.0 owns membership; `DescriptionContext` is a separate one-viewpoint use qualification whose `viewpointRef` resolves P, selects no view, and establishes no conformance |
| `U.View` | `same-individual-dependent` under `U.Episteme`; retained | E.17.0 recognizes membership of the same episteme E when `EpistemeViewpointConformanceRelation(E,P)` obtains for at least one exact admitted `U.Viewpoint` episteme P; C.2.1 keeps E identity | direct authoring and A.6.3 viewing are construction routes only; selection, rendering, carrier, query execution, publication occurrence, or graphical appearance establishes no view membership |
| candidate already covered by one admitted durable U-kind | `reuse`; no new durable U-kind | the exact `ReusedUKindRef`, its accepted E.24 settlement, and its current direct governing pattern remain authoritative | reuse creates no rival identity, extent, or public kind; naming work may expose an already admitted name but does not admit another kind |
| classificatory distinction with one exact current C.3.2 declaration reference | `local-kind`; no durable U-kind | `LocalKindDeclarationRef` points to that exact declaration; the C.3 family remains the direct owner | the distinction remains local under the C.3 family and does not become a root or dependent durable U-kind; without the exact reference, `local-kind` does not close by label |
| `U.EpistemePublication` | `reject`; no durable U-kind | an episteme keeps its C.2.1 identity before, during, and after contingent participation as the selected edition in `EpistemePublicationRelation` | use Plain `published episteme` only in a claim that states obtaining participation and identifies or permits recovery of the exact E.24.PUB publication occurrence; Plain wording is neither a reference nor a designator and does not resolve |

Each row carries exactly one of the six dispositions. The retained same-individual kinds do not gain another constitution relation or identity discriminator; their direct patterns judge membership of the already identified root individual. The identity-dependent case identifies a different individual through its declared dependence. The `reuse`, `local-kind`, and `reject` rows remain non-admission exits.

Consumer repair follows the disposition, not one replacement word. Method-description claims retain `U.MethodDescription`; exact viewpoint and view claims retain `U.Viewpoint` and `U.View` only under E.17.0 membership. Every lexical or source use of the rejected spelling `U.EpistemePublication` is recovered by its claim as the selected `U.Episteme`, exact `EpistemePublicationRelation` occurrence, publication form, or `U.PresentationCarrier`; the rejected kind has no occurrences to retype.

Thus `dependent` describes an admission and identity architecture. It is not a shorthand for every object named in a record, every participant of a relation, or every qualifier used to interpret an episteme.

#### E.24.UK:4.2.1 - Accepted Root Settlement For `U.Relation`

FPF has already admitted `U.Relation`; project users do not repeat this ontology decision. The root kind classifies individuable obtaining relation occurrences. A direct relation can obtain before a system explicitly individuates, names, describes, or references one occurrence, but admission under this root requires the direct relation pattern to supply an occurrence-identity rule.

| Admission condition | `U.Relation` settlement by value |
|---|---|
| governed individuals | the extent contains exactly those obtaining relation occurrences for which a direct relation pattern supplies an occurrence-identity rule |
| stable identity or membership | each direct relation pattern states how one occurrence is reidentified and distinguished from another; participant identity, maximal continuous obtaining, constituting work, or another domain discriminator is used only when that pattern selects it |
| reviewable witness | `A.6.REL` supplies the common occurrence discipline; the direct relation pattern supplies relation-participant meanings, the obtaining condition, and the relation-specific identity rule |
| action-facing need | comparisons, qualifications, change claims, nested relations, and receiving direct relations can depend on one occurrence being distinguishable from another |
| non-duplication | relation-kind-specific assertions do not provide one common kind for a relation occurrence used as the EntityOfConcern of an episteme or as a participant of another direct relation |
| direct governing locus | `A.6.REL` governs the root occurrence distinction and progressive individuation; each direct relation pattern governs whether its relation obtains and how its occurrences are identified |
| E.24-compatible settlement | the root subject is the individuable obtaining relation occurrence; its semantic area is direct relation obtaining and occurrence identity; A.6.0, A.6.5, C.2.1, F.18, and C.29 remain neighboring declaration, claim, naming, reference, and representation patterns |
| by-value dependence | A.1 part-relation admission, relation-occurrence descriptions, and direct relations whose participant kind admits `U.Relation` rely on this root by value |

The admission does not force explicit materialization of every obtaining relation. Ordinary engineering prose can stop at the direct relation sentence. A system performs explicit-individuation work only when a named receiving episteme, direct relation, or operation-application assertion depends on occurrence identity. The accepted Tech label `U.Relation` is governed separately through its F.18 NameCard; the label does not establish the extent.

Apply that positive extent rule before classifying a nearby object. A semantic predicate is rule content in the direct relation pattern; participant satisfaction states the criterion for relation obtaining. A relational assertion or relation-occurrence description is a `U.Episteme` under `C.2.1`; its content can claim that the relation obtains or designate one occurrence as its EntityOfConcern. A designator or reference is governed by `F.18` and stands in its exact designation or reference relation to an already individuable occurrence. A filled claim-bearing project record is a `U.Episteme`, while the reusable form of that record remains under `E.24.PUB`. A data-model or diagram element is a `C.29` representation element. Each is connected to the relation occurrence only by its explicit description, publication, designation, reference, or representation relation.

The rule is not lexical. An individuable publication-relation occurrence is itself a `U.Relation` because its own direct publication pattern supplies obtaining and identity. A row that represents that occurrence remains a representation element. Reidentify the current object under its direct pattern instead of inferring membership from words such as relation, edge, link, record, or reference.

#### E.24.UK:4.3 - Combined Admission Order

Use existing rules in this order:

1. Recover the source use and governed EntityOfConcern.
2. If the current question is typed claim quantification, apply C.3, C.3.1, and C.3.2 as needed. When the admission decision under E.24.UK records `local-kind`, `LocalKindDeclarationRef` points to one exact current C.3.2 declaration; the C.3 family remains the direct owner of the local distinction.
3. Recover the identity, grounding, or recognition rule for the candidate: direct governing pattern, C.3 membership and extent rule, Concept-Set witnesses, an A.6 `U.Signature` identified by `<content, EntityOfConcernRef, effectiveReferenceScheme>` and carrying direct `SubjectKind` and `RangedValueKind` declarations plus `ResultKind`, `SliceSet`, or `ExtentRule` when those distinctions are current, an imported symbol bound by that signature, CT2R/Compose-CAL constructive grounding when the claim is structural, formal-substrate/principle-frame declaration, or another accepted operational identity test. For a relation-kind candidate, recover the direct governing relation pattern and its obtaining and occurrence-identity rules as part of the same witness.
4. If durable FPF kindhood is claimed, apply E.24-compatible settlement, A.11 parsimony, and A.8 universal-core testing when kernel-level status is claimed.
5. If the candidate names participation in a direct relation, keep the participant's independently governed kind and the direct relation. If it names a reusable declaration component, use one A.6.5 SlotSpec. If it names an assertion or description field, keep the designation inside that `U.Episteme`. If it names a selected structure, reusable form, or representation element, apply `A.22`, `E.24.PUB`, or `C.29` respectively.
6. Only after the governed object and admission decision are stable, use F.8 for mint-or-reuse and F.5, F.18, or F.17 for naming and publication.

| Source | Contribution |
| --- | --- |
| C.3 | Typed claim quantification, intent, extent, membership, kind bridge, and typed guards. |
| C.3.1 | `U.SubkindOf` partial order over `U.Kind`, not dependent-U-kind relation. |
| C.3.2 | Exact current declaration referenced through `LocalKindDeclarationRef`; the C.3 family remains its direct owner. |
| E.14, B.3.5, and C.13 | Working-Model first, CT2R alias-plus-grounding, and Compose-CAL `Γ_m` traces for structural identity claims. |
| A.6.0 and A.6.1 | Construction-facing declaration shape: `SubjectKind`, `RangedValueKind`, `SliceSet`, `ExtentRule`, vocabulary, laws, applicability, realization, and argument-slot discipline. |
| A.8 | Universal-core test for kernel-level U-kind claims. |
| A.11 | Composition and parsimony before adding a new core concept. |
| E.24 | Ontic settlement and distinction among ontic, description episteme, publication, and form. |
| F.8 | Mint-or-reuse decision after recovered kind and use. |
| F.5 | Naming after recovered meaning; naming does not do ontology. |

#### E.24.UK:4.4 - Source Ontology Conversion Guide

Use this short conversion guide when a source ontology, schema, standard, class hierarchy, or top-level ontology uses words such as type, class, category, object type, entity type, kind, or subtype. BFO-style, ISO-style, OWL/RDF, database-schema, programming-language, and discipline-local type systems are source ontologies or representation regimes; they do not become FPF `U.*` names by translation.

First recover the source construct by value:

- source name and source ontology or schema;
- source identity rule, membership rule, extent rule, or recognition rule;
- source relations such as is-a, part-of, realizes, participates-in, depends-on, or equivalent local relations;
- intended source use: classification, query, modeling, exchange, validation, reasoning, implementation, or documentation.

Then select the FPF object:

| Source construct use | FPF recovery |
| --- | --- |
| claim quantification, membership, extent, subkind, or kind bridge | C.3 `U.Kind`, C.3.1 `U.SubkindOf`, and typed-reasoning rules |
| public durable FPF kind needed across patterns | E.24.UK durable U-kind admission, then E.24-compatible settlement |
| a reusable coordination of one primary governed subject kind, its identity rule, core direct relation, named neighboring direct relations, and dependent-pattern reliance | E.24 ontic settlement with explicit reuse of every already governed kind and relation |
| imported formal symbol or declared range in a signature or mechanism | A.6 `U.Signature` identified by `<content, EntityOfConcernRef, effectiveReferenceScheme>` with direct `SubjectKind` and `RangedValueKind` declarations, a symbol bound by that signature, a Concept-Set row, or an admitted durable U-kind |
| source-name alignment across contexts | F.9 bridge, F.17 term row, F.18 naming, and explicit loss notes |
| implementation or serialization category | representation, publication form, record field, schema field, or direct implementation artifact governed by the relevant pattern |

A source "type" may become an FPF kind and may require an ontic, but only after these tests. If the source construct only supplies local classification or exchange syntax, keep it as C.3 typed reasoning, bridge material, representation material, or source wording. Do not create a rival FPF type layer beside durable U-kind governance and E.24 ontic settlement.

#### E.24.UK:4.5 - Structural Location Rule

A `U.*` spelling in a pattern title, host filename, monolith heading, or ToC row is stronger than a prose occurrence. Structural locations orient readers to the governed object.

Use this rule:

- **Prose occurrence:** recover the local claim and direct governing pattern.
- **Table row or record field:** recover whether it is one SlotSpec, one assertion or description field, one reusable-form element, or an already governed object.
- **Heading:** retain `U.*` only when the section really governs that object or directly references an already admitted U-kind.
- **Pattern title or host filename:** retain `U.*` only when the pattern's primary EntityOfConcern is that root or dependent U-kind.
- **ToC row:** retain `U.*` only when the row points to a pattern that carries the settlement; otherwise name the direct governed object or repair the wording with E.10.

Do not keep a false `U.*` structural name for memory or search convenience. Use a Plain label, local heading, Name Card, Concept-Set row, relation name, record field, or quoted source wording when that is the actual object.

#### E.24.UK:4.6 - Failed U-kind Admission Dispatch

When a candidate distinction fails the positive test, keep the actual object under its existing kind and direct governing pattern:

| Candidate actually names | Recovery under its direct owner |
| --- | --- |
| an entity participating in one direct relation | keep the entity's independently governed kind; let the direct relation pattern state its participant meaning, obtaining condition, and occurrence identity |
| a reusable relation-declaration component | use `SlotSpec = <SlotKind, ValueKind, refMode>` under `A.6.5`; the SlotKind is local to that declaration |
| a participant designation or another assertion or description field | keep the by-value designation or reference value inside the receiving `U.Episteme`; the field does not become the world-side participant or a U-kind |
| a selected organization of direct relations | classify the selected organization as one `U.Structure` under `A.22`; the relation-specific structure name is not thereby another U-kind |
| a claim-bearing record or card | classify the filled claim-bearing object as `U.Episteme`; classify its reusable arrangement as the publication-form participant only when `PublicationFormExpressionRelation` obtains; use the exact E.24.PUB publication occurrence and `U.PresentationCarrier` when availability is current |
| a graph, tuple, algebraic, or other formal representation element | use the exact `C.29` mathematical or representation lens and state its correspondence to the represented object when that correspondence matters |
| a measure, metric, or indicator | recover the measured characteristic, scale, evaluation operation, and reading through `C.16.P`, `A.19`, or the direct evaluation pattern |
| a quoted source label or discipline term | retain it as source wording with its local sense and direct FPF recovery under `E.10` and `E.10.ARCH` |
| a desire for a public name | finish object recovery first, then apply `F.8` and the applicable `F.5`, `F.17`, or `F.18` naming pattern |

