---
chunk_kind: "child"
pattern_id: "A.6.0"
pattern_title: "U.Signature - Reusable Law-Governed Declaration Episteme"
section_id: "A.6.0:4"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/A.6.0/A.6.0__005_solution.md"
commit_sha: "2ada413629b846ef308222d16489a82cb5b40a71"
heading_path:
  - "A.6.0 — U.Signature - Reusable Law-Governed Declaration Episteme"
  - "A.6.0:4 — Solution"
line_start: 11293
line_end: 11478
dependencies:
  - "A.15.1"
  - "A.17"
  - "A.18"
  - "A.19.CPM"
  - "A.19.SelectorMechanism"
  - "A.19.UNM"
  - "A.2.6"
  - "A.3.1"
  - "A.6.0"
  - "A.6.1"
  - "A.6.5"
  - "A.6.RCD"
  - "A.6.REL"
  - "A.7"
  - "C.16"
  - "C.2.1"
  - "C.22"
  - "C.29"
  - "C.3"
  - "E.10"
  - "E.18.1"
  - "E.24.PUB"
  - "E.24.UK"
  - "F.9"
keywords:
---

### A.6.0:4 - Solution

Use `U.Signature` as the dependent durable U-kind for a reusable law-governed declaration episteme. Identify the episteme through its content, exact `EntityOfConcernRef`, and effective `U.ReferenceScheme`. Let the declaration state its vocabulary, laws, and applicability. Keep the declared subject and every later realization under their direct kinds and relations.

**Local signature mantra.** *Name the subject of the reusable declaration and the range of values or results it covers. List the terms another user may reuse, the laws that user must preserve, and where those laws apply. Add relation-participant declarations, operation inputs or results, slice-and-membership rules, or dependencies only when one named reuse calls for them. Keep implementations, evaluations, work, and publication outside the declaration.*

In FPF terms, the subject is the exact `EntityOfConcernRef`; `SubjectKind`, `RangedValueKind`, and optional `ResultKind` state the declared subject and range; and `Vocabulary`, `Laws`, and `Applicability` state the reusable terms, regularities, and use boundary. Add A.6.5 SlotSpecs only when a reusable `RelationSignature` must preserve the same participant meanings and types. Add A.6.1 operation arguments or results only for a current mechanism declaration. Add `SliceSet` and `ExtentRule` only when the same declared kind can have different members at selected context slices. Declare a dependency only when another signature actually relies on imported or provided names or laws. If the named reuse still works without an optional addition, leave that addition out. Implementations and realizations remain under A.6.1, evaluations under their direct evaluation patterns, work under A.15.1, and publication under E.24.PUB. The mantra is Plain recall wording. Its imperative grammar does not assert condition-governed continuation. When such executable continuation is current, its object is a Constraint-Governed Unfolding Structure (CGUS) governed by A.22.CGUS.

#### A.6.0:4.1 - Admit and identify U.Signature

`U.Signature` is a same-individual dependent durable U-kind under `U.Episteme`. C.2.1 first identifies one episteme through one `EpistemeConstitutionRelation` by its complete claim content, exact independently governed `EntityOfConcern`, and effective `U.ReferenceScheme`. The claim graph and reference scheme are epistemic constituents; the `EntityOfConcern` is not. A.6.0 adds a stable membership condition and practitioner-facing declaration use to that already identified individual. It adds no second constitution relation, identity discriminator, assembly, composition rule, or holon test.

An already identified episteme is a `U.Signature` exactly when, under its effective `U.ReferenceScheme`, its complete identity-bearing claim content carries a reusable law-governed declaration about its exact `EntityOfConcern` and includes all of the following with substantive meaning:

- direct `SubjectKind` and `RangedValueKind` declarations that identify the declared subject and value range;
- `Vocabulary` that supplies the designators needed to reuse the declaration;
- `Laws` that state the reusable predicates, equations, invariants, closure conditions, or other declared regularities;
- `Applicability` that bounds where those claims are used;
- `ResultKind`, `SliceSet`, `ExtentRule`, and dependency, import, or provided-name declarations only when those distinctions are current for the declaration.

Judge the complete claim content, not a selected subset or the presence of field names. A minimal directly authored signature may carry the declaration content required by the A.6.0 membership predicate in one claim graph without citing any smaller episteme. A signature may instead cite separately identified source or dependency epistemes, provided its own claim graph names the dependency relation and the declaration meaning thereby reused. Those source epistemes remain separate individuals connected through their governing dependency, source-use, edition, or other direct relations; they are not components assembled into the signature, and their citation alone does not establish signature membership.

E.24.UK governs the one-time public admission of the dependent kind. In project work, authoring a new declaration candidate, or revising a declaration so that its claim content, exact `EntityOfConcern`, or effective `U.ReferenceScheme` changes, yields a resulting C.2.1 discriminator triple. When the one `EpistemeConstitutionRelation` for that triple obtains, C.2.1 identifies the resulting episteme; A.6.0 then judges whether that already identified individual satisfies the `U.Signature` membership predicate, without adding a second constitution occurrence or identity discriminator. An optional separately reviewable membership judgment is another classification-assertion episteme whose exact `EntityOfConcern` is the candidate; that assertion neither creates the candidate nor admits the public kind. Citing, comparing, or reusing an unchanged episteme, or judging its membership without changing a C.2.1 discriminator, creates neither another episteme nor another constitution occurrence.

The signature keeps the C.2.1 identity of the same episteme. Two designations resolve to that same individual only while the complete claim content, exact `EntityOfConcern`, and effective `U.ReferenceScheme` are unchanged. Changing any discriminator identifies another `U.Episteme`; call that new individual a `U.Signature` only if it independently satisfies the membership predicate above. State an edition, refinement, or supersession relation only when its own direct predicate obtains.

The declared subject remains the independently governed `EntityOfConcern`, not the signature. A realization of the declaration remains under its direct pattern. A description whose `EntityOfConcern` is the signature is another episteme. Publication occurrence, publication form, `U.PresentationCarrier`, and C.29 representation remain separate objects and relations; publication or visible form establishes neither identity nor membership. G.11 currentness and every later work or use likewise remain neighboring judgments and relations rather than signature identity components.

#### A.6.0:4.2 - Write the minimum declaration content

The four content groups are semantic components, not a mandatory visual table. A publication form may present them as paragraphs, a table, formal declarations, or another representation. A publication occurrence makes a selected episteme edition available through that form without changing its content.

| Content group | Content and use |
|---|---|
| `SubjectKind`, `RangedValueKind`, optional `ResultKind`, `SliceSet`, and `ExtentRule` | Name the declared subject and value range, plus a distinct result kind when current. When membership of the same `SubjectKind` can differ across context slices, `SliceSet` names the addressable `U.ContextSlice` values to consider and `ExtentRule` states how membership is judged at one selected slice, thereby determining `Extension(SubjectKind, slice)`. No additional container kind is implied. |
| `Vocabulary` | Declares the public designators for value kinds, relation kinds, operators, and other independently identified declared objects. A `RelationSignature` may include SlotSpecs under A.6.5; each SlotSpec gives a declaration-local SlotKind name and the exact participant ValueKind and designation mode. A mechanism may include operation argument and result declarations under A.6.1. A vocabulary token does not by itself admit a durable U-kind. |
| `Laws` | States semantic predicates, equations, invariants, closure conditions, and other declared regularities. A.6.1 governs an operation-admission predicate for a mechanism; A.3.1 governs the method, and A.15.1 governs the dated work occurrence that enacts it, including direct F.6 `performedUnderAssignment` attribution to the exact covering `U.RoleAssignment`. Writing the operation-admission predicate as a condition does not make it a signature law. |
| `Applicability` | States the exact `U.ClaimScope` and any other use qualifiers current for this declaration, such as a relevant time interval or selected `CHR:ReferencePlane`. Cite an optional `modelUseStructureRef : U.StructureRef` only when an independently selected model-use structure changes interpretation. |

`SubjectKind` and `RangedValueKind` are declaration-content components. They do not create a second hierarchy beside C.3 or E.24.UK. A.2.6 supplies addressable `U.ContextSlice` values; C.3.2 governs the membership judgment and any optional materialized `KindExtension` representation. `SliceSet` is not a generic space, time interval, numeric or result range, or changing dataset. `ExtentRule` is not an arbitrary change function: it tells how the declared kind's members are determined at one named slice. A time selector may be part of a `U.ContextSlice`; a value or result range stays in `RangedValueKind` or `ResultKind`; changing data stays with its direct owner; and a claim-bearing mathematical set representation opens C.29 separately. Leave both fields out unless membership of the same declared kind can differ across the named slices.

Applicability and meaning remain distinct. The effective `U.ReferenceScheme` is part of episteme identity. The exact `U.ClaimScope` delimits use; when current for the declaration, a relevant time interval, selected `CHR:ReferencePlane`, or selected `BoundedModelUseStructure : U.Structure` further delimits or organizes applicability. None replaces the reference scheme or claim scope.

#### A.6.0:4.3 - Use RelationSignature for reusable relation declaration

`RelationSignature` is the relation-facing use of one `U.Signature`. It is not a second U-kind.

Its `EntityOfConcernRef` identifies one exact already admitted direct relation kind. If `A.6.RCD` settles a derived relation kind, that kind counts here only after its direct subject settlement states the participant meanings, exact base-definition and named-substrate dependencies, obtaining and applicability laws, and a direct occurrence-identity rule. The derivation or predicate definition may be cited as a dependency, but a predicate-definition episteme whose `EntityOfConcern` is the reusable predicate definition rather than the admitted relation kind is not a `RelationSignature`. Its content declares:

- the relation-kind designator;
- one `SlotSpec` for each world-side participant meaning that needs reusable typed declaration;
- the direct pattern's obtaining predicate and declared laws, restated for reuse without claiming that the predicate is satisfied;
- applicability of those claims;
- the occurrence-identity rule supplied by the direct relation pattern, restated for reuse without applying it to any occurrence;
- for an admitted derived relation kind, the exact base relation definitions, named substrate and authorized derivation operation, and applicability dependencies already established by the direct subject settlement.

The direct relation pattern remains authoritative for when the relation obtains and how an individuated occurrence keeps identity. The signature declares those rules for reuse; it does not make the predicate true and does not create an occurrence.

A direct relation may obtain before anyone writes a signature. Ordinary prose may therefore stop at:

> During Shift-17, Robot-7 holds InspectorRole as interpreted by MaintenanceRoles-2026 under Maintenance-Scheme-A.

This is an A.2.1 assignment assertion about the already admitted `U.RoleAssignment` relation kind. A.2.1 defines the direct assignment predicate and occurrence-identity rule; the actual assignment history for Robot-7 and Shift-17 determines whether the predicate is satisfied. When several patterns need to reuse the four participant meanings, predicate, and identity rule, the A.2.1 `RelationSignature` becomes useful: its A.6.5 SlotSpecs declare those meanings for typed assertion and F.6 work-attribution reuse. When another claim needs to refer to this particular assignment episode, A.6.REL governs explicit individuation.

#### A.6.0:4.4 - Declare participant meanings and operation parameters under different specializations

For each world-side participant meaning whose reusable declaration is current, a `RelationSignature` declares one A.6.5 SlotSpec. The following code sketch is a compact representation of that declaration, not the world-side relation or its participants:

```text
SlotSpec := <SlotKind, ValueKind, refMode>
refMode := ByValue | RefKind
```

| Component | Meaning in a RelationSignature |
|---|---|
| `SlotKind` | The declaration-local name by which this `RelationSignature` distinguishes one participant meaning of its EntityOfConcern relation kind. It is not a participant, system role, or mathematical operand. |
| `ValueKind` | The exact world-side kind admitted for the relation participant. |
| `refMode` | How a receiving episteme, such as an assertion, description, or occurrence record, carries a participant designation: by value or through one exact governed RefKind. That designation denotes the actual participant. The relation occurrence itself does not store the reference, and the occurrence record is not that occurrence. |

A.6.5 governs these declarations of participant meanings. Use the exact A.2.1 SlotKind names for this admitted example: `HolderSystemSlot`, `RoleValueSlot`, `RoleTaxonomyEpistemeSlot`, and `EffectiveReferenceSchemeSlot`. They expose the four participant distinctions without making the assignment interval, a selected model-use structure, or performed work into another participant. Do not force SlotSpecs into a one-off assertion that has no receiving typed use.

A formal or mechanism declaration may instead need named operation arguments and a result. A.6.1 governs that `OperationAlgebra`; C.29 governs any mathematical operand order, product, function, or tuple used to represent it. Those operation parameters do not become `RelationSignature` SlotSpecs or SlotKinds merely because the same notation uses angle brackets or numbered arguments. When a relation claim consumes a mathematical representation, state an explicit correspondence between the representation's operands and the independently declared SlotSpecs.

#### A.6.0:4.5 - Expose real declaration dependencies

Open a `SignatureManifest` only after this test. Add an import when removing one named provider would leave this declaration unable to interpret a required non-local term or unable to replay one of its stated laws; name the provider and the exact required term or law. Add a provide entry when this declaration introduces a named term or law and one named dependent declaration relies on it. A background citation, similar vocabulary, shared publication, list membership, or convenient replay order is not a dependency.

The compatible heading is retained for dependent patterns; it names neither another U-kind nor one uniform ontic object. It co-locates entries with three roles: `id` is an identity-neutral display designator; `signatureRef` and its optional `.edition` pin form a governed reference to an already recoverable signature episteme; and `imports` and `provides` may carry or represent dependency and name-or-law introduction claims in the signature's exact `U.ClaimGraph`. Co-location makes neither every entry identity-bearing claim content nor any entry a relation occurrence.

The compatible section may carry entries with these roles:

| Entry | Meaning |
|---|---|
| `id : SignatureId` | An identity-neutral display designator or representation metadata for one already independently identified signature episteme. It is not a governed reference and does not enter the C.2.1 identity triple. |
| `signatureRef : U.EpistemeRef` | A governed reference resolving to the already identified signature episteme selected for replay. Changing its serialization preserves the referent only while resolution returns that same episteme under the effective reference scheme. |
| `signatureRef.edition` | An optional edition pin on `signatureRef` for one already recoverable episteme edition. The pin neither enters the C.2.1 identity triple nor establishes that an `EpistemeEditionRelation` obtains. |
| `imports` | When the signature's exact `U.ClaimGraph` states that interpretation requires a named term or that replay requires an exact law claim from a named provider declaration, this entry carries that claim content or visibly represents it. Name both provider and required term or law. The designators, governed references, or list membership alone establish no dependency or source-use occurrence. |
| `provides` | When the signature's exact `U.ClaimGraph` states that it introduces a public term or law on which a named dependent declaration relies, this entry carries that claim content or visibly represents it. Public SlotKinds and RefKinds can be named terms. Being listed establishes no consumer dependency by itself. |

A change confined to the spelling of `id` or the serialization of `signatureRef` preserves episteme identity only when the reference still resolves to the same episteme and its exact claim content, exact EntityOfConcern, and effective `U.ReferenceScheme` remain unchanged. Changing `signatureRef.edition` selects another already recoverable edition; it does not by itself establish an edition relation, historical continuity, or `U.Signature` membership for the referent. If a C.2.1 identity discriminator changes, A.6.0:4.10 governs the resulting identity.

Use these dependency-manifest predicates:

- **SM-1 Term-and-law resolution.** Every required non-local term or exact law claim resolves under the effective reference scheme to the one named provider declaration that supplies it.
- **SM-2 No redeclaration and legal direction.** A provided term or law is not also supplied by a transitive import under the same effective reference scheme, and the claimed provider-to-consumer direction matches the predicate of the exact dependency or source-use relation rather than a drawn arrow or list order.
- **SM-3 Replay order and cycles.** A selected one-pass provider-to-consumer replay method requires an acyclic ordering of the recovered dependency designations. A cycle means that this replay method cannot run; it does not by itself prove that every semantic dependency in the cycle is prohibited. Apply each exact dependency governor to its edge. If no current governor decides whether the semantic cycle is legal, return an exact missing-governor blocker instead of deleting an edge or inventing an order. Any graph, cycle check, or ordering notation remains a C.29 representation.
- **SM-4 Export boundary.** A dependent declaration relies on provided names and cited laws, not on private publication layout or implementation detail.

The remove-the-provider test above identifies a candidate dependency; it does not make a relation obtain. State the exact dependency or source-use relation only after its direct predicate is satisfied for the named provider, consumer, term or law, and use. A citation, manifest entry, list membership, or replay result can support an assertion about that relation but does not create the relation occurrence. A provider or provider-edition change may require resolution, replay, or currentness review; it changes the consumer signature's identity only when the consumer's own claim content, exact EntityOfConcern, or effective reference scheme changes.

A governed reference to a separately identified object is not an exported vocabulary name merely because that reference appears in the signature.

#### A.6.0:4.6 - Specialize declaration use without minting another root kind

A signature profile is a constrained use of the same `U.Signature` kind. The profile states which content is current and which neighboring patterns govern later use.

**`profile = FormalSubstrate`.** Declare vocabulary and terms, inference kinds, formal laws, applicability, and the actual declaration dependencies carried in the signature's claim content. A.6.1 separately governs `OperationAlgebra`, operation designators, typed argument and result positions, admission conditions, application, and realization. An A.6.1 declaration may cite the FormalSubstrate signature; that citation does not make the operation part of this signature. When a mathematical object is selected as a lens for another entity, C.29 governs the lens-use claim; usefulness does not make the mathematical object a signature.

**`profile = PrincipleFrame`.** Write the postulates and invariants, then name the observable distinction each one requires: what must be observed or compared to tell whether the frame's claim holds. Cite the separately identified characteristic or measurement declaration that makes that distinction checkable; units, scales, `CHR:ReferencePlane` values, comparators, and normalizations remain under A.17, A.18, C.16, CHR, A.19.CPM, and A.19.UNM. If the text decides whether a proposed operation application, run, or gate may proceed, move that decision to A.6.1 or the direct evaluation and gate pattern, including A.21/C.11 where applicable. A PrincipleFrame may state what a decision must respect, but it is not that admission decision. When its claim crosses a context or effective reference scheme, use the exact F.9 bridge and state what is preserved and lost. Cited declarations remain independently identified objects, not extra PrincipleFrame identity components.

State a relation between two signatures directly as refinement, conservative extension, equivalence, or another independently governed relation only when that relation's own predicate obtains. Before using the refinement label, compare all three reusable content duties: `Vocabulary`, `Laws`, and `Applicability`. Name the terms preserved, added, or removed; the laws preserved, strengthened, or changed; and whether the population, time, `CHR:ReferencePlane`, and claim scope stay the same, narrow, or widen. An unexplained applicability widening fails the refinement claim; use another direct relation whose predicate explicitly permits the widening instead of hiding it under `refinement`. Use a C.29 morphism only when a mathematical structure-preservation claim is actually current.

#### A.6.0:4.7 - Keep declaration, realization, and use under their direct patterns

| Current object or claim | Governing pattern |
|---|---|
| Constitution and C.2.1 identity of the exact claim-bearing episteme, including a separately identified relation-occurrence description episteme | C.2.1; the direct object or relation pattern still governs the described EntityOfConcern |
| Reusable declaration episteme and `U.Signature` membership | A.6.0 |
| Relation obtaining and explicitly individuated occurrence | Direct relation pattern and A.6.REL |
| `RelationSignature` SlotSpecs and participant-designation discipline | A.6.5 |
| Mechanism `OperationAlgebra`, typed argument and result positions, admission conditions, application, and realization | A.6.1 |
| Method | A.3.1 |
| Performed work | A.15.1 |
| Optional source-to-receiving-episteme viewing construction | A.6.3 |
| Same-EntityOfConcern representation-scheme transition | A.6.3.RT |
| Cross-reference-scheme, cross-plane, or cross-model-use-structure use with explicit preservation and loss | F.9 for the exact bridge relation; the direct pattern for the affected meaning or structure remains authoritative |
| Numeric comparison, normalization, units, scales, and measurement | A.19.CPM and A.19.UNM, together with A.17, A.18, C.16, and the direct measurement pattern when each object or relation is current |
| Actual mathematical or diagrammatic lens, operand mapping, or correspondence use | C.29 |
| Current representation-factor bundle for governed episteme publication positions | C.2.7 |
| Publication-face use and the distinct publication occurrence, form, and carrier relations | E.17 for the publication-face use profile; E.24.PUB for the direct occurrence, form, and carrier relations |
| Evidence-use or status-use relation | A.2.4 |
| Evidence-provenance graph or path | A.10 |
| Assurance claim or reliance-safety assurance record | B.3 |
| Operational gate profile and the decision that uses its result | A.21 and C.11 |

The rows name the direct patterns that govern these common adjacent objects and claims. Their co-location is only a compact representation and does not change any governing pattern's scope.

#### A.6.0:4.8 - Add explicit objects only for a named receiving use

Make three decisions by naming the next sentence, comparison, tool, or declaration that must work:

1. **State the direct relation and stop.** Use this branch when the task only asks whether the A.2.1 assignment predicate holds for the named holder, role, taxonomy episteme, and reference scheme during the named episode. For example, `During Shift-17, Robot-7 holds InspectorRole as interpreted by MaintenanceRoles-2026 under Maintenance-Scheme-A` is a complete current assignment assertion. State an affirmative or negative claim under A.2.1, or an exact governed modal claim when that family is current. The A.2.1 predicate defines the test; the actual assignment history decides the case. Add an A.10 or receiving-evaluation reliance judgment only when the task separately asks whether to rely on the assertion.
2. **Share one declaration.** Reuse or author a signature when at least two named claims or consumers must use the same participant meanings, vocabulary, laws, or applicability. For example, a staffing assertion and an F.6 work-attribution consumer that must interpret `HolderSystemSlot`, `RoleValueSlot`, `RoleTaxonomyEpistemeSlot`, `EffectiveReferenceSchemeSlot`, and the same A.2.1 assignment predicate can cite one `RelationSignature`. One sentence that merely repeats the word `assigned` does not open this branch. When a declaration is authored, C.2.1 identifies the episteme from its own claim content, exact EntityOfConcern, and effective reference scheme; A.6.0 then judges `U.Signature` membership.
3. **Distinguish one occurrence.** Open occurrence identity only when a later claim must refer to that same occurrence, compare or qualify it, track its beginning, continuation, cessation, or change, or use it as a participant of another relation. For example, F.6 work attribution must cite the exact covering assignment episode, and a staffing history that compares Shift-17 with a later reassignment must apply A.2.1's uninterrupted-obtaining same-versus-new-occurrence rule. A roster-row identifier that merely designates an assertion identifies neither the assignment occurrence nor a new occurrence; use F.18 only after A.2.1 has distinguished the occurrence to which a reference should resolve.

These are the `receiving-use` thresholds. They concern three different objects and are not stages that construct a relation or episteme from need. The stop is observable: the target direct assertion, shared declaration for the named consumers, or occurrence-referencing claim can be written without another unresolved object. Authoring, selecting, reusing, or explicitly individuating is motivated by that target but supplies no identity criterion and creates neither the episteme nor the relation occurrence. Selecting or reusing an unchanged episteme leaves its identity unchanged; neither a reference nor a log entry creates its referent. A claim about condition-dependent entries, branches, returns, or stops is a CGUS claim governed by A.22.CGUS.

#### A.6.0:4.9 - Recover formal-substrate and PrincipleFrame uses by direct governing relation

| Current claim | Direct governed use |
|---|---|
| Author, select, or cite a formal declaration | Use `U.Signature(profile=FormalSubstrate)` with its subject, vocabulary, inference kinds, laws, applicability, and real dependencies. |
| Use a mathematical object to preserve selected structure while hiding other structure | Use C.29 and state the mathematical-lens relation. |
| Declare, apply, or realize an operation | Use A.6.1 for the `OperationAlgebra`, typed argument and result positions, admission conditions, application, and realization; cite a FormalSubstrate signature only when that named dependency is current. |
| Carry an encountered distinction toward later work | Use E.18.1 for the carry-through relation; that relation does not decide signature, operation, or lens adequacy. |

The same independently identified formal object or episteme can participate in these different uses while retaining its own identity and kind. Its identity does not decide which declaration, dependency, operation, lens, or carry-through relation is current.

For a `PrincipleFrame`, write one postulate or invariant together with the observable difference that would count for or against it. Cite a characteristic, measurement, unit, scale, reference plane, comparator, or normalization declaration only when that declaration is needed to state or check that difference; an informative citation is not a dependency. Do not put an operation-admission, run-acceptance, or gate-passage verdict into the frame. If the frame's claim is carried into another context or reference scheme, name the F.9 bridge occurrence and its preservation and loss before using the claim there. A cited declaration may be superseded, or an independently obtaining dependency relation may cease or be replaced, without retroactively changing the PrincipleFrame's identity. Changing the PrincipleFrame's own citation or dependency claim changes its claim content and therefore identifies another episteme; the same follows when its exact EntityOfConcern or effective reference scheme changes. Any edition, refinement, or supersession relation between the two epistemes must independently obtain and must pass the Vocabulary-Laws-Applicability comparison above.

#### A.6.0:4.10 - Change the exact object that changed

Apply C.2.1 first. Every `U.Episteme` is identified by exact claim content carried by one exact `U.ClaimGraph`, one exact EntityOfConcern, and one effective `U.ReferenceScheme`. Changing any member of this mandatory triple identifies another episteme. That episteme is a `U.Signature` only when it independently satisfies A.6.0 membership. A changed discriminator, `SignatureId`, or `signatureRef.edition` value does not by itself establish signature membership or historical continuity.

A change to `imports` or `provides` changes the consumer signature's identity only when it changes that signature's own claim content. A changed provider or provider edition can instead leave the consumer episteme unchanged while requiring the named dependency or source-use assertion, resolution result, replay result, or currentness judgment to be reconsidered.

A changed later use does not change the signature unless the change alters one of its C.2.1 identity discriminators. For example, a new mechanism realization remains a new realization, and a new publication layout remains a new publication form.

Connect two different epistemes by `EpistemeEditionRelation`, refinement, supersession, or another independently governed continuity relation only when that relation's own predicate obtains under its direct governor. Revision work, shared title, changed identifier, citation, or sequence alone establishes no such occurrence.

When a once-current signature becomes stale while its identity remains recoverable, G.11 governs currentness and selection among recoverable editions. G.11 creates neither a later episteme nor an edition, refinement, or supersession relation.

Reopen declaration authoring when a proposed change affects the signature's exact claim content, EntityOfConcern, effective reference scheme, declared dependency, Vocabulary, Laws, Applicability, or the boundary of a FormalSubstrate, PrincipleFrame, or other admitted profile. The revised claim-bearing candidate is another C.2.1 episteme; A.6.0 judges its signature membership again, and any edition, refinement, or supersession relation remains a separate claim under its direct governor. Also reopen the affected declaration element when current problem-owning-domain or formal-method SoTA changes the term, inference form, law shape, applicability condition, or realization boundary being declared.

When a governed kind name, `SubjectKind`, `RangedValueKind`, SlotKind, RefKind, or exported term is renamed, rerun E.10 and F.18. Accept the rename only when a cold reader can still recover the same FPF kind, declaration use, and practical action; otherwise keep the old name or return the naming defect. Do not revise the signature merely because a realization, work occurrence, measurement, Bridge use, evidence-use relation, publication, provider currentness, or G.11 selection changed. Update that neighboring object under its direct owner, and reopen the signature only if its own claim or dependency content must change.

