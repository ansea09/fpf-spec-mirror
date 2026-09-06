---
chunk_kind: "child"
pattern_id: "A.1.1"
pattern_title: "Bounded Model-Use Structure and DDD Bounded-Context Recovery"
section_id: "A.1.1:4"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/A.1.1/A.1.1__006_solution.md"
commit_sha: "9208be543f1ede0f53eb24604bf97fd2f121dd24"
heading_path:
  - "A.1.1 — Bounded Model-Use Structure and DDD Bounded-Context Recovery"
  - "A.1.1:4 — Solution"
line_start: 1966
line_end: 2182
dependencies:
  - "A.1"
  - "A.14"
  - "A.15.1"
  - "A.15.PROD"
  - "A.2"
  - "A.2.1"
  - "A.2.6"
  - "A.22"
  - "A.3.1"
  - "A.3.4"
  - "A.6.0"
  - "A.6.5"
  - "A.6.REL"
  - "C.2.1"
  - "C.2.P"
  - "C.29"
  - "E.17.0"
  - "E.24.PUB"
  - "F.17"
  - "F.18"
  - "F.9"
keywords:
---

### A.1.1:4 - Solution

Recover the Plain **bounded context** as one `BoundedModelUseStructure`, governed as a `U.Structure`. Identify it from one exact model episteme, exact already-admitted model-use holons, the selected organization of obtaining model-applicability, actual model-use, and fixed-content model-expression-coherence occurrences, exact applied constraint claims used by the selection judgment, and one exact selection-use frame. Each `U.ClaimScope` remains only a participant of its selected `ModelApplicabilityRelation`; a separate applied constraint claim may refer to that scope or its A.2.6 membership predicate. A bare scope, slice, membership outcome, boundary display, or carrier enters no A.22 discriminator. No boundary crossing participates in this identity. A later model edition has another C.2.1 episteme identity; continuity across it additionally requires exact `EpistemeEditionRelation(earlierModelEpisteme, laterModelEpisteme)` and the A.1.1 continuity rule.

#### A.1.1:4.1 - Select structure, not another holon

Use the four A.22 identity discriminators. The following sketch is a description of the selected organization, not the structure itself and not a relation signature:

```text
BoundedModelUseStructure : U.Structure
  exact constituents:
    one selected model episteme
    exact admitted model-use holons
  exact selected obtaining relations:
    ModelApplicabilityRelation occurrences
    ModelUseRelation occurrences
    ModelExpressionCoherenceRelation occurrences
  exact applied constraint claims used by the selection judgment:
    one exact C.2.1 constraint proposition may refer to a U.ClaimScope or its A.2.6 membership predicate
    other exact applicability, coherence, release, or use-rule constraint propositions applied here
    no bare scope, slice, membership outcome, boundary display, or carrier episteme
  one named selection-use frame:
    exact question
    admissible action
    stop or return condition
  optional nearest non-admissible overread: explanatory only, subject to F.19:4's plausible-reader test
```

A selection-use frame is the exact plain value formed by the question, admissible action, and stop or return condition; it is not a new kind, card, or record. A phrase such as *current use*, *appropriate structure*, or *bounded-model-use frame* does not fill it. Changing one of those three values changes that identity discriminator. An optional nearest non-admissible overread may explain the use when it passes F.19:4's plausible-reader test; that explanation is outside the frame's identity.

The structure depends on its constituents and selected relation organization. It is not a holon whose parts are the substrate systems, Work, methods, or epistemes. Their identities, direct part relations, and any construction or whole-reidentification questions remain separately governed.

#### A.1.1:4.2 - Recover the direct relations

A.1.1 states each direct predicate and its occurrence-identity rule. An obtaining occurrence is an instance of a relation kind already admitted under `U.Relation`; its existence does not depend on a project deciding to expose it. A named receiving use may justify explicit individuation and reference under `A.6.REL`. A reusable `RelationSignature` episteme declares the participant SlotSpecs. An assertion or occurrence description may designate the actual participants by value or reference. Each table below is a readable presentation of one signature declaration.

The two named temporal-extent ValueKinds below are local to A.1.1, not U-kinds. They can type a temporal extent stated in an assertion or occurrence description; they are not participant ValueKinds in either RelationSignature. For `ModelApplicabilityRelation` and `ModelUseRelation`, the direct obtaining history determines the maximal continuous extent used by the occurrence-identity rule. A filled assertion may state an open or closed extent.

| Local ValueKind | Boundary and continuity semantics |
|---|---|
| `ModelApplicabilityInterval` | The maximal interval during which one fixed model episteme remains applicable to one fixed holon under one fixed claim scope, interpreted by that model episteme's own effective reference scheme. |
| `ModelUseInterval` | The maximal interval within one fixed work occurrence for which exact F.6 `performedUnderAssignment(work, assignment)` obtains, during which that assignment's holder actually uses one fixed model concerning one fixed use-locus holon. |

For these two temporally varying relation kinds, continued obtaining extends the same open occurrence; a demonstrated gap ends it, and later resumption begins another occurrence. `ModelExpressionCoherenceRelation` instead has the participant-determined identity declared below: it has no temporal-extent discriminator. Revising an assertion changes the episteme, not any world-side occurrence.

**`ModelApplicabilityRelation`.** Its participants are one model episteme, one exact holon, and one declared claim scope. Its predicate asks whether that model applies to that holon over the exact `U.ContextSlice` values delimited by that scope. The model episteme's C.2.1 effective reference scheme supplies the interpretation basis; it is not a fourth participant.

| SlotKind | ValueKind | refMode | Participant meaning |
|---|---|---|---|
| `ApplicableModelEpistemeSlot` | `U.Episteme` | `U.EpistemeRef` | The model episteme whose distinctions and predicates are applied. |
| `ModelApplicabilityHolonSlot` | `U.Holon` | `U.HolonRef` | The exact holon about which the model is applicable. |
| `ApplicabilityClaimScopeSlot` | `U.ClaimScope` | `ByValue` | The scope whose A.2.6 `member(slice, scope)` predicate delimits the claim. |

**Well-formedness constraint `WF-A1.1-APP`.** `ModelApplicabilityRelation(M,H,S)` obtains exactly when `S` is the model-declared applicability scope or `scopeSubset(S, modelDeclaredScope(M))`, both scope expressions are interpreted under `effectiveReferenceScheme(M)`, and the model's declared applicability conditions hold for `H` over every slice `x` for which `member(x,S)` is true. `coversSet(S,T)` applies only when `T` is an exact finite `ContextSliceSet`.

When `S` imports a local sense from another semantic setting, the interpretation branch exists exactly when the source and receiving F.17 `SchemeSenseCell` values are resolved and an F.9 `Bridge` obtains in the source-to-model orientation. Different schemes, shared spelling, or a Bridge Card does not establish that branch.

**Well-formedness constraint `WF-A1.1-APP-USE`.** A positive applicability assertion or structure selection that relies on the imported branch is admissible only when a separate current C.2.1 claim affirmatively states that the Bridge is suitable for this named scope-comparison use, direction, rule, and loss tolerance. The same use must have an exact A.10 evidence-provenance relation. Ordinary reliance requires `RelianceDisposition=pass`. If an actual named assurance claim about that use is current, require its B.3 `AssuranceResult` for the same bounded use: only `supported-for-use` supports the attempted assurance use, while `narrowed` supports only its stated narrower use. A direct domain rule may require such a claim.

**Use guidance.** If the Bridge, bounded-use claim, or selected reliance branch is missing, return respectively `missing claim-scope interpretation bridge`, `missing claim-scope interpretation use claim`, or `missing claim-scope interpretation reliance`. These stops block the receiving assertion or selection; they do not make an otherwise obtaining Bridge false. Any membership judgment, operation application, assertion, or Work remains under A.2.6, A.6.1, C.2.1, or A.15.1.

The occurrence is reidentified from the actual identities of the model episteme, holon, and claim scope together with the derived maximal continuous `ModelApplicabilityInterval`. Repeating the model's effective scheme adds no independent discriminator.
**`ModelUseRelation`.** Its participants are one exact system-role-assignment occurrence, one model episteme, one performed Work occurrence, and one exact use-locus holon. Its predicate is actual use of that model content by the assignment holder while that system performs the same Work concerning that holon.

| SlotKind | ValueKind | refMode | Participant meaning |
|---|---|---|---|
| `ModelUserSystemRoleAssignmentSlot` | `U.SystemRoleAssignment` | `U.RelationRef` | The system-role-assignment occurrence paired with the Work by exact F.6 `performedUnderAssignment`. |
| `UsedModelEpistemeSlot` | `U.Episteme` | `U.EpistemeRef` | The model episteme whose content is actually used. |
| `ModelUseWorkSlot` | `U.Work` | `U.WorkRef` | The performed Work in which use occurs. |
| `ModelUseLocusHolonSlot` | `U.Holon` | `U.HolonRef` | The exact holon concerning which the model is used. |

**Well-formedness constraint `WF-A1.1-USE`.** `ModelUseRelation(A,M,W,H)` obtains exactly when F.6 `performedUnderAssignment(W,A)` obtains and `HolderSystem(A)` actually uses the content of `M` while performing `W` concerning `H`. The holder system is derived, not copied as a fifth participant. A method, if current, remains related to `W` under A.3.1.

The occurrence is reidentified from the four participant identities and the derived maximal continuous `ModelUseInterval`. A useful probe holds those participants fixed and asks whether a relevant model-content change can change how the Work is performed; availability or mention alone is not actual use.
Scope delimitation is not another direct relation kind here. The `U.ClaimScope` participating in `ModelApplicabilityRelation` is a set-valued scope over `U.ContextSlice`; A.2.6 governs its primitive membership predicate. A membership assertion or an evaluation result is an episteme about that predicate.

**Local predicate-value declaration.** `ModelExpressionCoherencePredicate` is an A.1.1-local `ValueKind`, not a U-kind and not an evaluation procedure. A by-value candidate belongs to this kind only when it declares (1) the ordered model-content and expression-content input meanings, (2) the exact comparison domain and local senses, (3) a Boolean truth condition, (4) the treatment of required congruence and permitted loss, and (5) every dependency whose absence makes application stop rather than return `false`. Two predicate values are identical exactly when those five by-value components are identical. A changed input meaning, domain, truth condition, congruence or loss rule, or dependency identifies another predicate value; a changed label, evaluator, evidence set, result episteme, representation, or publication does not. A label or procedure lacking the complete five-part declaration is not a member.

**`ModelExpressionCoherenceRelation`.** Its participants are one exact model episteme, one exact expression episteme, one by-value criterion admitted as `ModelExpressionCoherencePredicate`, and one exact `U.ReferenceScheme` used as the comparison basis.

| SlotKind | ValueKind | refMode | Participant meaning |
|---|---|---|---|
| `CoherenceModelEpistemeSlot` | `U.Episteme` | `U.EpistemeRef` | The model episteme whose fixed claims supply one side. |
| `CoherentExpressionEpistemeSlot` | `U.Episteme` | `U.EpistemeRef` | The expression episteme assessed against that model. |
| `ModelExpressionCoherencePredicateSlot` | `ModelExpressionCoherencePredicate` | `ByValue` | The admitted five-part criterion value; its label, evaluator, result, or evidence cannot substitute for it. |
| `ModelExpressionCoherenceReferenceSchemeSlot` | `U.ReferenceScheme` | `ByValue` | The shared scheme or the receiving comparison basis used by the admitted bridged branch. |

**Well-formedness constraint `WF-A1.1-COH`.** `ModelExpressionCoherenceRelation(M,E,P,R)` obtains exactly when either (a) `R` equals the C.2.1 effective schemes of both epistemes, or (b) `P` resolves every differing source and receiving F.17 `SchemeSenseCell` pair and names an obtaining F.9 `Bridge` for each required correspondence; and, after that semantic branch is established, the fixed predicate value `P` returns true for the fixed claim contents of `M` and `E` under `R`. An unresolved cell, missing Bridge, shared spelling, common label, Bridge Card, or mere interpretability establishes no bridged branch.

The Bridge profile carries relation semantics only. Comparison direction, use-specific rule, permitted loss, and reliance belong to the separate bounded-use claim and reliance path.

**Well-formedness constraint `WF-A1.1-COH-USE`.** A receiving assertion or structure selection that relies on a bridged coherence occurrence is admissible only when a separate current C.2.1 claim affirmatively states that the Bridge is suitable for this fixed-content comparison use, direction, rule, and loss tolerance compatible with `P`. The same use must have an exact A.10 evidence-provenance relation. Ordinary reliance requires `RelianceDisposition=pass`. If an actual named assurance claim about that use is current, require its B.3 `AssuranceResult` for the same bounded use: only `supported-for-use` supports the attempted assurance use, while `narrowed` supports only its stated narrower use. Establish any required authorization separately.

**Use guidance.** Return `missing model-expression interpretation bridge`, `missing model-expression interpretation use claim`, or `missing model-expression interpretation reliance` for the corresponding missing condition. A use stop does not make the Bridge or predicate false and does not erase or reidentify an otherwise obtaining coherence occurrence. Comparison Work, an assertion episteme, and an A.22 selection use remain separate.

One occurrence is participant-determined by `<M,E,P,R>`; it has no temporal-extent discriminator and no later recurrence for the same tuple. Changed claim content identifies another episteme and tuple. Changed predicate value or comparison scheme likewise changes the tuple. Changed evidence, bounded-use claim, reliance result, card, publication, evaluator, or timestamp does not.
Maintenance remains one separate dated Work individual: recover each exact actual performer through A.13 and let A.15.1 independently admit the occurrence. Add F.6 through the same obtaining A.13 assignment only when the maintenance account or its receiving use expressly consumes precise assignment-bound attribution; F.6 identifies neither assignment nor performer, and missing or failed attribution leaves the Work intact. Its affected-referent, resource, parameter, premise, method-enactment, and operation-application facts use their direct relations or A.6.1 bindings. C.2.1 identifies any report or repaired episteme separately; only an exact A.15.PROD entity-inception claim may relate that episteme's first existence to the performed maintenance. An exact evaluator may separately be recovered through A.13 and perform independently admitted evaluation Work, with F.6 added only for a consumed precise attribution. C.2.1 identifies any result episteme asserting whether the coherence predicate holds, and only its exact A.15.PROD inception basis may relate its first existence to that performed Work. Neither that result episteme nor its provenance is the coherence occurrence. Failed maintenance work remains actual work even when the changed episteme tuple has no obtaining coherence occurrence.

`BoundedModelUseStructure` selects obtaining participant-determined `ModelExpressionCoherenceRelation` occurrences. Maintenance methods and Work remain separate objects even when they change the receiving decision; if their organization must itself be selected, that is a distinct A.22 structure and does not enter this bounded-model-use identity.

**Coherence-work stress cases.** Coherence can obtain before any selected maintenance episode. Successful maintenance that leaves both episteme identities fixed leaves the same participant tuple; maintenance that changes expression claim content gives another C.2.1 episteme and a different tuple to evaluate. Failed maintenance may leave a changed expression episteme and a separately identified evaluation result while the new tuple has no obtaining coherence occurrence. Automated integration work and non-software maintenance use the same separation among fixed-content correspondence, work, result, evaluation, evidence, and provenance.

**Occurrence-identity stress case.** Exact F.6 `performedUnderAssignment(InspectionWork-42, InspectorAssignment-17)` obtains, and its holder `Robot-7` uses `DefectModel-3` concerning `Pump-6` during that work. An observation at 10:00 supports continued obtaining of the same occurrence whose `ModelUseInterval` began at 09:00 and remains open; it does not create another occurrence. If model use demonstrably stops at 10:15 and resumes at 10:30 during the same work occurrence and assignment attribution, the resumption begins a second model-use occurrence. Correcting an assertion's timestamp without evidence of a world-side gap changes only that assertion.

**Use guidance — unsupported crossing.** First identify both endpoint `BoundedModelUseStructure` values without the crossing and state source, target, direction, required fit, permitted loss, and claim scope. **Well-formedness constraint `WF-A1.1-CROSS`.** A positive cross-structure member exists only when a current direct pattern supplies compatible endpoint SlotKinds, an obtaining crossing predicate, an occurrence-identity rule, and all four A.22 discriminators; the proposal, F.9 sense Bridge, label, diagram, or card supplies none of them. Otherwise preserve the six-part proposal, omit it from both endpoint identities and every positive cross-structure member, and return `missing CROSS-LOCALITY-BRIDGE governor`.

A.1.1 is the subject pattern for these three relation kinds. `A.6.0` governs their RelationSignature epistemes, `A.6.5` governs the SlotSpecs inside those declarations, and `A.6.REL` governs progressive explicit individuation. A.2.6 separately governs claim-scope membership. `BoundedModelUseStructure` is the selected organization of the resulting occurrences under those scope values; no context record copies their participants.

#### A.1.1:4.2a - Use the settled public relation names

The direct definitions, SlotSpecs, obtaining constraints, and occurrence-identity rules above govern the three relation kinds. A.1.1 uses only the settled Tech labels and their shortest Plain relation sentences:

| Tech label | Plain relation sentence | Nearest non-use |
|---|---|---|
| `ModelApplicabilityRelation` | this model applies to this holon within this claim scope | not scope membership, an applicability assertion, or the derived interval |
| `ModelUseRelation` | this assignment's holder uses this model during this Work concerning this holon | not availability, method application, Work, assignment, or a use record |
| `ModelExpressionCoherenceRelation` | this model content and this expression content satisfy this declared coherence criterion under this comparison scheme | not maintenance, implementation, evaluation, evidence, or the predicate value itself |

F.18 and F.17 carry candidate-name history, public-row state, lineage, and refresh evidence. `ModelExpressionCoherencePredicate` remains an A.1.1-local five-part criterion ValueKind; it has no public F.17 row unless a later durable naming use independently reopens F.18.

#### A.1.1:4.3 - Identify continuity through model use

At one observation time, the structure has the four A.22 discriminators:

1. exact independently identified constituents—the selected model episteme and admitted model-use holons;
2. exact selected obtaining applicability, use, and coherence occurrences;
3. exact applied constraint claims used by this selection, each with a recoverable proposition and C.2.1 identity; a claim may refer to one `U.ClaimScope` or its membership predicate, but the bare scope, membership outcome, boundary display, or carrier is not this discriminator; and
4. one exact named selection-use frame containing its question, admissible action, and stop or return condition. An optional explanatory guard follows F.19:4 and remains outside those four discriminators.

No crossing or proposed six-part crossing record enters those discriminators.

At a later observation time, reidentify the same structure only when every continuing constituent is reidentified under its direct rule; any replacement model is connected by exact C.2.1 `EpistemeEditionRelation` and admitted by the declared continuity rule; every continuing relation occurrence retains its direct identity; every replacement occurrence is explicitly admitted; and all four A.22 discriminators remain the same under that rule.

The continuity rule therefore compares the exact constituents, selected occurrence organization, exact applied constraint claims, and the complete question/action/stop-or-return selection-use frame. A changed constraint proposition reopens the third discriminator; changing only a membership assertion, boundary rendering, carrier, or evidence about an unchanged constraint claim does not. A changed question, action, or return condition reopens structure identity even when every substrate and relation occurrence remains unchanged. A changed explanatory guard alone reopens the affected use claim, not structure identity. If its changed content alters an applied constraint, question, action, or stop or return condition, compare that existing discriminator. A changed page, wording, rendering, carrier, description edition, or publication does not. File history, edition labels, publication order, a shared name, or membership in an edition collection establishes neither `EpistemeEditionRelation` nor bounded-model-use continuity; A.14 governs any separately selected collection of editions.

Missing evidence creates uncertainty about a continuity claim; it does not by itself end a world-side relation or structure. Any selected substrate holon may separately participate in a larger whole under A.14 and C.13; that is not parthood of `BoundedModelUseStructure`.

#### A.1.1:4.4 - Resolve semantic locality through direct values and relations

When the question is local meaning rather than joint model-use organization, recover the smallest direct result and stop:

| Exact practitioner question | Direct governed result | Subject pattern | Stop or return condition |
|---|---|---|---|
| What does this term or predicate mean here? | one exact claim-bearing episteme, its C.2.1 effective `U.ReferenceScheme`, and the needed F.17 `SchemeSenseCell` values | C.2.1 and F.17 | Return to the source expression or scheme when the exact meaning or a required sense-cell value is unavailable. |
| Over which slices is this claim made, and which slices belong? | one `U.ClaimScope` and its A.2.6 `member(slice, scope)` facts | A.2.6 | Keep the scope and membership facts as this result; select a structure separately only when its organization changes a receiving decision. |
| Which system-role kind is assigned to which system, and when? | First recover the assignment occurrence and its declared `U.SystemRoleAssignment` species. The species declares participant meanings and rules; the occurrence supplies the holder System, assigned local system-role-kind value, and any other participant values that distinguish the occurrence. If the question also needs a reportable time, recover a separate assignment assertion or occurrence-description episteme whose content states the currently known `AssignmentInterval`. | A.2 and A.2.1; A.2.7 only for an independently current relation among system-role kinds | Return until the assignment species, all declared participant values, obtaining predicate, and any needed occurrence-description episteme are recovered. The occurrence retains its maximal uninterrupted extent. Context, scheme, and interval are not generic assignment participants; an organizational title supplies no assignment. |
| Which rule, policy, invariant, or inference is local? | one C.2.1 episteme with the exact ClaimGraph and effective scheme, the A.2.6 claim scope, and the truth or admissibility predicate defined or constrained in the exact subject-pattern description | C.2.1, A.2.6, that exact predicate and its `SubjectPatternLocator` | If no exact predicate states when the rule or inference holds, preserve the claim at its current scope and stop. |
| Which unit or measurement reading is local? | one C.16 measurement basis naming bearer, characteristic, scale, coordinate or level, `U.Unit` when applicable, polarity, and evidence stub | C.16 | Return to the C.16 measurement basis when only a displayed label or value is available. |
| How is an episteme used as evidence, or how is a status consumed? | the exact episteme or status bearer, target claim, scope, polarity or status value, relevance window, provenance constraint, and intended use | A.2.4 and A.10 for evidence use; F.10 for status family and status use; B.3 only for assurance | Return to the exact evidence or status relation when only its presentation is known. For a permission, gate, or assurance claim, use its own subject pattern. |
| Can a field, department, technology, or shared spelling choose the local semantics? | no; restate the live question and recover its exact model-use structure, scheme and sense cells, system-role kind or assignment, rule or status, or Bridge from the corresponding row above | the pattern selected by that question | Restate the live question and use its corresponding row; a broad label alone leaves the selection unresolved. |
| Which admitted holon grounds a description's empirical claims? | one exact C.2.1 `EpistemeEmpiricalGroundingRelation` | C.2.1 | Return to C.2.1 until the grounding relation is recovered. |
| Does one joint model-use organization change this decision? | an independently selected `BoundedModelUseStructure` with all four A.22 discriminators | A.1.1 and A.22 | omit `modelUseStructureRef` when one direct value or relation answers the question |

For movement between local meanings, resolve the exact source and receiving F.17 sense cells and then apply F.9. An obtaining Bridge states correspondence between those readings; the separate bounded-use claim states direction, rule, and tolerance. A.10 handles ordinary reliance; B.3 adds a bounded result only when an actual named assurance claim is current. The Bridge is not the rule, unit, status use, inference, or receiving action.

If a subject pattern still asks for a generic `U.BoundedContext` or `BoundedContextRef` instead of the exact values above, do not fabricate that participant. Preserve the exact value or relation already recovered and stop at the unresolved interface in the subject pattern. The transfer is not complete merely because A.1.1 names a destination.

##### A.1.1:4.4.1 - Heterogeneous semantic-locality replays

**Hospital operating-room replay.** Recover direct values and relations.

| Distinction | Direct move and first result |
|---|---|
| Local vocabulary | C.2.1 identifies the operating-room policy episteme and its effective scheme; F.17 resolves the local senses of *case*, *time-out*, and *independent auditor*. |
| Local rule and inference | A C.2.1 claim episteme states the surgeon and auditor incompatibility rule within the exact surgical-case claim scope. A.2.1 supplies the actual `SurgeonAssignment-12` and candidate `IndependentAuditorAssignment-13`; exact F.6 `performedUnderAssignment(SurgicalCaseWork-42, SurgeonAssignment-12)` establishes the current Work attribution. When the same-holder incompatibility predicate holds, an exact context-local A.2.7 incompatibility relation between the two assigned system-role kinds obtains; the relation is only a premise. `SurgicalAdmissionService-4 : U.System` applies `IndependentAuditorAdmissionMethod-3 : U.Method` to those assignment occurrences in dated `AuditorAdmissionCheckWork-43 : U.Work`; the receiving Method's result episteme `AuditorAdmissionCheckResult-43` records `reject`. The rule is not global. |
| Evidence and status use | A sterility-audit episteme is used for one named claim only through A.2.4/A.10 with scope, polarity, window, and provenance. A `Ready` status is separately typed by F.10 for its exact target and use; neither item grants release permission or assurance. |
| Cross-setting approximation | First ask whether the local meanings correspond at all. `OperatingRoomCaseSenseCell` means one surgical episode governed by the operating-room policy; `BillingCaseSenseCell` means one billable service record. In this replay, `OperatingRoomCaseBillingBridge` obtains under F.9 as an exact `Partial-overlap` relation between those cells, independently of any coding use. Separate C.2.1 claim `HospitalCaseCodingUseClaim` proposes coding the named surgical episode as one billable service record; its content names the operating-room-to-billing direction, a rule requiring the same patient, encounter, performed procedure, and date, a tolerance that permits omission of internal time-out and auditor-assignment detail from the billing record but no patient or procedure change, affirmative polarity, and `HospitalCodingScheme-2026` as the effective scheme. A.10 states whether ordinary reliance passes; when an actual named assurance claim is current, B.3 supplies its bounded result for the same use. If a later claim says coding occurred, recover the exact coding Work and resulting billing assertion, publication, or operation application under their subject patterns. A different operating-room-to-staffing sense pair needs its own Bridge profile and use claim. Changing only either use claim leaves the Bridge identity unchanged. Establish any required coding authorization separately. |

This replay selects no `BoundedModelUseStructure` unless one exact model's applicability, assigned-Work use, fixed-content coherence, applied constraints, and selection-use frame also become current.

**Two further retained uses.**

| Prior use | Direct replay without a context holon | Stop |
|---|---|---|
| Special relativity | C.2.1 and F.17 identify the selected theory-edition episteme, effective scheme, postulate and inference senses; a later theory edition has another C.2.1 episteme identity and needs exact `EpistemeEditionRelation` for a continuity claim; A.2.6 scopes the claim; C.16 carries units and measurement readings; A.2.4/A.10 carries evidence use; F.10 carries any current status use. F.9 identifies only the exact low-speed semantic correspondence between the selected relativistic-reading and Newtonian-reading sense cells. A separate C.2.1 bounded-use claim proposes interpreting specified relativistic low-speed readings with the named Newtonian approximation rule, in the relativistic-to-Newtonian direction, within a stated velocity and error tolerance, with explicit polarity and effective scheme; A.10 states whether ordinary reliance passes; when an actual named assurance claim is current, B.3 supplies its bounded result for the same use. If a later claim says the approximation occurred, recover its exact inference or operation application, any comparison Work, and the result claim episteme under their subject patterns; absent those objects, no approximation has happened. | No theory truth, edition continuity, global equivalence, inference permission, or approximation use follows from the label *relativity*, the Bridge, the bounded-use claim, or passing reliance alone. |
| FPF pattern quality | Start with the bearer and evaluation frame under C.16.Q. For example, *first-use affordability* of this exact pattern edition for a named practitioner and task is the E.21 `UseAffordabilityAndApparatusProportionality` coordinate, not a free quality label. C.2.1 identifies the pattern edition and any separately authored `PatternQualityEvaluation` result episteme; E.21 governs that evaluation record, its coordinates, and declared use; A.2.4/A.10 governs evidence use and F.10 any status use. If bare *quality* is still ambiguous, C.16.Q first distinguishes pattern quality from a product-reliability characteristic or C.25 bundle, a C.16 manufacturing-yield characteristic and measurement, B.3 safety assurance, a service-satisfaction characteristic or bundle, and ordinary praise. Resolve exact senses before any F.17/F.9 cross-scheme relation. | The word *quality* supplies neither a bearer, evaluation frame, shared characteristic, evaluation result, assurance claim, manufacturing-yield reading, nor cross-setting substitution. |

#### A.1.1:4.5 - Keep descriptions and publications separate

A bounded-context description is a `U.Episteme`. Under its C.2.1 declaration, the description's `entityOfConcernRef` designates the exact EntityOfConcern named by the description's claims. `EntityOfConcernSlot` is the SlotKind in that declaration; it does not itself point to the world-side object. A meta-description designates that description episteme through ordinary C.2.1 recursion.

When a description claim needs empirical grounding, recover one exact C.2.1 `EpistemeEmpiricalGroundingRelation` between the description episteme and the admitted grounding holon. `GroundingHolonSlot` is only the signature-local participant meaning in that relation's declaration; a `groundingHolonRef` in a card or description designates the participant. The selected structure cannot fill that participant because it is not a holon. Viewpoint, claim scope, effective reference scheme, publication use, rendering, and presentation carrier remain separately governed.

A stale description has another episteme edition or an obsolete currentness claim. Neither condition by itself changes the model-use structure or its world-side relations.

#### A.1.1:4.6 - Recover DDD context mapping by direct object

Start with three questions: what reusable way of mapping was used, what work actually happened, and what claim-bearing product resulted? Identify that product under C.2.1. Call the same episteme a view only after it passes one exact E.17.0 viewpoint-conformance test. Keep the relation structure it describes and every diagram, page, or publication separate.

| DDD source term or use | FPF object |
|---|---|
| `Bounded Context` when the joint model-use organization changes an engineering move | `BoundedModelUseStructure`, governed as a `U.Structure` |
| subsystem at the boundary | the exact existing `U.System` under its direct pattern |
| work performed by a team system at the boundary | one exact dated Work individual independently admitted under A.15.1 after the exact actual performer System is recovered through A.13; add the same obtaining assignment occurrence and F.6 `performedUnderAssignment` relation only when this account expressly represents precise assignment-bound attribution |
| code base or database schema at the boundary | first classify the exact referent: claim-bearing code or schema content is a C.2.1 episteme; a repository, file, publication form, or carrier stays under its direct representation, publication, or carrier pattern; a deployed database or software organization stays a `U.System` or selected `U.Structure` under its subject pattern; the source phrase supplies no common kind |
| bounded-context boundary description | `U.Episteme` whose C.2.1 EntityOfConcern reference designates the exact referent named by its claims |
| `Context Mapping` as a reusable way of doing | `U.Method`; any work plan, performed mapping work, evaluation work, and evaluation result remain separate |
| relations among several bounded contexts | conditional A.22 membership for one already identified `U.Structure`, available only after independently governed exact obtaining crossings are selected among several bounded model-use structures and all four A.22 base discriminators are established; A.22 retains a local pending label for this rule but F.17 publishes no public cross-structure term |
| candidate product called `Context Map` | one independently identified C.2.1 episteme whose EntityOfConcern is the proposed or described crossing organization while a direct crossing governor or A.22 base identity is missing; only after both are established may a corresponding episteme designate the exact structure admitted by A.22's conditional cross-structure rule; either episteme has dependent `U.View` membership only when exact E.17.0 `EpistemeViewpointConformanceRelation` obtains |
| visual or interactive expression and availability of an already admitted Context Map view | any C.29 representation and correspondence, rendering work, publication occurrence, publication form, and `U.PresentationCarrier` remain separate under their direct patterns |

**Code/schema split.** Start from the exact claim, not the source phrase. Claim-bearing source-code or schema content such as `PressControllerCode-18` is a C.2.1 episteme with an exact EntityOfConcern and effective scheme. A repository, file, publication form, or presentation carrier that bears that content remains under its direct representation/publication/carrier pattern. A deployed controller, database, or software organization remains an actual system or selected structure under its subject pattern. The phrase *code base or database schema* grants none of those identities and never supplies one universal kind.

Positive case: the fixed claims expressed by `PressControllerCode-18` participate as the expression episteme in `ModelExpressionCoherenceRelation`. Near misses: `PressControllerRepository-2` is only the repository or carrier being referred to, and `DeployedPressDatabase-4` is the deployed database system or structure. Neither near miss may fill an episteme participant merely because source practice calls it a code base or schema.

This dispatch table is a reading aid for selecting the governing FPF object and pattern. Only that direct pattern supplies object identity, relation obtaining, or dependent-kind membership. If a separately current claim says that the candidate episteme first existed through the performed mapping Work, apply A.15.PROD only to that exact local inception claim. If an earlier episteme participates as source, use C.2.P to recover the exact source expression and route the source-use relation to its direct governor. Evaluation Work and any result episteme remain separate. None of those facts, and no product name, representation, rendering, publication occurrence, form, or carrier, grants `U.View` membership.

FPF `Map` remains the mapping-method head for mapping subjects to coordinates in a declared Space. The quoted DDD product name stays a retrieval cue; by itself it grants neither dependent `U.View` membership, the FPF `Map` reading, nor identity with the structure.

`BoundedModelUseStructure` and A.22's conditional cross-structure rule concern different structures. First identify every bounded model-use structure from its own model, admitted holons, three direct relation families—including each applicability occurrence's exact `U.ClaimScope` participant—exact applied constraint claims, and named frame. A scope or membership result is not copied into the constraint discriminator. Only then may a distinct A.22 structure select several such endpoints and independently governed obtaining crossings among them. Until those crossing occurrences and all four A.22 base discriminators exist, no member of that conditional specialization is asserted and its A.22-local label remains pending. Maintenance Work remains separate from both structures. A candidate context-mapping episteme may carry claims about a proposed crossing organization without designating an exact structure. Once the direct crossing and A.22 identity exist, a corresponding C.2.1 episteme may designate that exact cross-structure and its participants. Only an explicit C.29 representation may show the structure or proposal; the episteme is a `U.View` only after exact E.17.0 conformance obtains.

#### A.1.1:4.7 - Preserve the lightweight path

Most local claims need no bounded model-use structure declaration. Name the exact current participant, semantic-locality value, system-role-assignment occurrence, or direct relation occurrence under its subject pattern and stop.

Select and expose `BoundedModelUseStructure` only when the joint organization of independently governed model applicability, actual model use, fixed-content model-expression coherence, exact applied constraint claims, and the named frame changes the next engineering move. Keep each claim scope solely in its applicability occurrence unless a distinct applied constraint proposition refers to it. If a crossing matters, open the separate A.22 cross-structure question only after its direct governor makes that exact crossing obtain between already identified endpoint structures; never add it to either endpoint identity. Recognize an episteme as `U.View` only after exact E.17.0 conformance. Publish that already recognized view under E.24.PUB only when a declared audience and use need it.

