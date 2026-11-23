---
chunk_kind: "child"
pattern_id: "A.2.9"
pattern_title: "U.SpeechAct — Communicative Work and Its Intended Use"
section_id: "A.2.9:4"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/A.2.9/A.2.9__007_solution.md"
commit_sha: "55ef163f91d42b48785bd297b50322e072d0a950"
heading_path:
  - "A.2.9 — U.SpeechAct — Communicative Work and Its Intended Use"
  - "A.2.9:4 — Solution"
line_start: 9249
line_end: 9409
dependencies:
  - "A.10"
  - "A.13"
  - "A.15.1"
  - "A.2"
  - "A.2.1"
  - "A.2.6"
  - "A.2.8"
  - "A.2.9"
  - "A.6.C"
  - "A.7"
  - "F.6"
  - "U.Work"
keywords:
  - "A.13-qualified actual performer"
  - "containment"
  - "enacted Method"
  - "evidence carrier"
  - "independently admitted speech-act Work"
  - "institutional target and effect"
  - "named receiving use"
  - "optional SpeechActRecord"
  - "publication relation"
  - "response versus achievement"
  - "same obtaining assignment"
  - "separate later performedUnderAssignment"
  - "smallest repair or stop"
  - "time"
  - "utterance description"
---

### A.2.9:4 — Solution

Start with the intended receiving use, including later use by the producer. If the order calls for an authorised response, determine whose response counts, for which subject and by when under the applicable terms. An authenticated reply meeting those conditions can itself complete the order. Where acceptance takes effect on delivery or after an objection period, establish the event and conditions that rule specifies. A question about understanding, subsequent use or causal influence requires evidence for that particular conclusion.

Repair the smallest thing that blocks the stated use—for example, wording, representation, prerequisites, medium, interaction, or a future receiving use—or stop. Judge earlier communicative Work against the use stated for that occurrence. A revised use applies to later communication or to a separately named reevaluation; it does not turn the earlier response into achievement of the earlier declared use. Authority, consent, permission, and ethical or institutional admissibility remain separate questions.

When exact occurrence identity, governance, modeling, audit, or reliance is current, use the admitted kernel kind `U.SpeechAct`. A separate recognition-taxonomy episteme and effective reference scheme make the act-type classification inspectable; an applicable policy or procedure defines any claimed institutional force. A `SpeechActRecord` may describe the occurrence and point to a MethodDescription, optional channel, utterance descriptions, or evidence carriers; none is the act or enacted Method.

#### A.2.9:4.1 — Normative definition

`U.SpeechAct <: U.Work` is a kind declaration. An actual Work individual is admitted as `SA : U.SpeechAct` when its primary effect is **communicative**: it places an utterance through an optional channel in a way classified by an exact speech-act recognition taxonomy under an effective reference scheme. A claimed institutional force additionally depends on the applicable current policy, procedure or protocol rule. The taxonomy may distinguish functions such as:

* asserting/informing,
* requesting/directing,
* promising/committing (as an instituting act),
* declaring/authorizing/revoking (status-changing acts),
* notifying (event announcement relevant for downstream work).

Per A.7 and A.15.1, the actual speech-act occurrence is a Work individual; its `SpeechActRecord` and **utterance descriptions** are epistemes, while its **carriers** are utterance carriers, publication carriers, or traces that allow observation and audit.

Occurrence identity specializes A.15.1. Admit a candidate as actual communicative Work from one exact communicative performance history, every actual performer's A.13 core, an enacted Method, temporal extent, and containing-System relation under A.15.1. To identify joint communicative Work, establish which people or other Systems performed the communication together and which contributions belonged to its performance. A record delivered to several people may instead describe the act of a single spokesperson. An independently recognized collective System can itself be the performer when its organization and action warrant that attribution.

Several satisfied act types classify that one Work occurrence. Identify more than one occurrence only when distinct performance history, enacted Methods, institutional actions, or another admitted discriminator establishes distinct Work. A shared utterance, carrier, assignment, or interval decides neither sameness nor difference. If a named use admits more than one defensible segmentation, cite its continuity or segmentation rule or leave the occurrence boundary unresolved. Check any precise assignment-bound attribution through F.6 only after admission.

Whether a given act type institutes commitments, permissions, publication relations, or status changes depends on an exact current policy or procedure and on the direct obtaining conditions of the claimed effect. Absent that basis, treat `SA : U.SpeechAct` only as actual communicative Work.

#### A.2.9:4.2 — Minimal occurrence-description record (normative)

Use the following declaration schema only when a receiving use needs a persistent claim about one already admitted actual speech-act occurrence. The record fields state claims about the referenced occurrence. A source that has only a candidate observation uses the separate non-conformant episteme/stub described under `SpeechActRef` discipline; it supplies neither a `SpeechActRef` nor a `SpeechActRecord`. Identify each actual performer. The two direct fields suffice for one performer with at most one exact assignment attribution. When the claim relies on several performers or several assignments of one performer, keep one record of the act and group each claimed assignment with its actual holder.

```
U.SpeechAct <: U.Work

SpeechActRef ::= U.EntityRef
  // resolves to one actual Work individual admitted as SA : U.SpeechAct

SpeechActRecord <: U.Episteme

PerformerEntry ::= {
    actualPerformerSystemRef: U.EntityRef,
    performedUnderAssignmentRef: optional<U.RelationRef constrained to F.6 performedUnderAssignment>
  }  // Each present F.6 reference relates this act to this performer’s A.13 assignment.

SpeechActRecord ::=
    {
      speechActOccurrenceRef: SpeechActRef,
      // Choose one form. The direct fields cover one performer and at most one assigned capacity.
      ( actualPerformerSystemRef: U.EntityRef,
        performedUnderAssignmentRef: optional<U.RelationRef constrained to F.6 performedUnderAssignment>
      | performers: set<PerformerEntry> ),  // non-empty, covers all performers and every claimed performer–assignment pair
      enactsMethodRef: optional<U.EntityRef>,        // resolves to the exact U.Method enacted by the actual Work
      methodDescriptionRef: optional<U.EpistemeRef>, // separate C.2.1 episteme used only when it identifies, constrains, or justifies that Method or intended Work
      unresolvedEnactsMethodClaimAddress: optional<ClaimAddress>,
      methodRelationGapProvenanceRef: optional<U.EpistemeRef>,
      reliancePosture: observationOnly | relianceReady,
      workContainmentRelationRefs: set<U.RelationRef>,       // non-empty; exact locally declared A.15.1 Work-to-System relation occurrences used by this record
      window: [start, end | open],                   // the act occurrence's extent, never an instituted effect's validity interval
      recognitionTaxonomyRef: U.EpistemeRef,         // exact speech-act recognition taxonomy
      effectiveReferenceScheme: EpistemeInterpretationScheme, // exact rules for the recognition-taxonomy claims used by actTypes
      policyOrProcedureRef: optional<U.EpistemeRef>, // current policy/procedure only when recognition or institutional force depends on it
      channelRef: optional<U.EntityRef>,              // optional independently governed communication channel
      utteranceSubjectRefs: optional<set<U.EntityRef>>,
      institutionalTargetRefs: optional<set<U.EntityRef>>,
      actTypes: set<SpeechActTypeRef>,                // ≥1 satisfied classifications under the named taxonomy and scheme
      addressedTo: optional<set<AddresseeRef>>,       // optional: who is addressed / audience
      utteranceDescriptionLocators: optional<set<DescriptionLocator>>, // where the utterance description is stated or recorded (A.7: Description)
      carrierRefs: optional<set<CarrierRef>>,         // evidence carriers/traces (A.7: Carrier; use A.10 when evidentiary)
      institutes: optional<InstitutedEffects>,        // references to separately obtaining objects/relations instituted or updated by this act
      notes: optional<InformativeText>                // explicitly informative
    }

DescriptionLocator ::=
  ClaimAddress | U.EpistemeRef
  // ClaimAddress here means C.2.1 ClaimAddress: exact edition plus intrinsic ClaimGraph identity; the other branch refers to the whole description episteme.

SpeechActTypeRef ::=
  RecognitionTaxonomyLocalTokenRef
  // Must be defined by recognitionTaxonomyRef and satisfied under effectiveReferenceScheme.

AddresseeRef ::=
  exactly one branch when addressee identity is required:
    addresseePartyRef?: PartyRef
    addresseeSystemRoleKindRef?: U.KindRef resolving to one exact local system-role kind
    addresseeSystemRoleAssignmentRef?: U.RelationRef constrained to U.SystemRoleAssignment

GrantedPermissionRelationRef@Context ::= U.RelationRef constrained to GrantedPermissionRelation@Context
  // resolves only to one exact obtaining grant occurrence

EpistemePublicationRelationRef ::= U.RelationRef constrained to E.24.PUB EpistemePublicationRelation
  // resolves only to one exact obtaining publication occurrence

GovernedInstitutedRelationLink ::= local link record, not a U-kind
  relationOccurrenceRef: U.RelationRef constrained to the exact declared relation kind
  relationRuleLocator: PatternID
    // locates the rule that defines and tests that relation

InstitutedEffects ::=
  {
    commitments: optional<set<U.RelationRef constrained to U.Commitment>>,
    permissions: optional<set<GrantedPermissionRelationRef@Context>>,
    systemRoleAssignments: optional<set<U.RelationRef constrained to U.SystemRoleAssignment>>,
    publicationRelations: optional<set<EpistemePublicationRelationRef>>,
    otherGovernedRelations: optional<set<GovernedInstitutedRelationLink>>
  }
```

`effectiveReferenceScheme` carries the exact interpretation rules used for the recognition-taxonomy claims behind `actTypes`; C.2.1:4.1.2 supplies its range. The selected value must interpret the classification criteria and references. A partial rule collection can satisfy membership while leaving a needed criterion unresolved; the dependent classification then remains unresolved.

Interpret a cited policy, procedure or utterance under its own effective scheme and establish any correspondence needed by the receiving inference under SA-C6. This field supplies the classification basis, not one scheme for every meaning communicated by the Work. The record itself retains its own C.2.1 constitution. Scheme membership establishes neither a satisfied act type nor an institutional effect.

**Occurrence-side constraints:**

* **(SA‑C0) Actual Work conformance.** The individual referenced by `speechActOccurrenceRef` **MUST** first satisfy independent A.15.1 admission: every actual performer has the A.13 core for the communicative action, scope, working situation, and window; the performance history is grounded; and the Work has an actual `enactsMethod -> U.Method` relation, temporal extent, and at least one obtaining locally declared Work-to-System containment relation. Add a characteristic profile only when a Grade, autonomy or profile result, criterion-dependent characteristic, or assurance use consumes it.

  An attribution for an actual performer **MAY** omit `performedUnderAssignmentRef` when it makes no exact assignment-bound claim. Each present reference **MUST** resolve to the F.6 relation established after admission for this act and that performer’s obtaining A.13 assignment. A `methodDescriptionRef` cites the episteme describing the Method.
* **(SA‑C1) Each performer and any claimed assignment.** Each actual performer **MUST** be an admitted `U.System` satisfying the A.13 agency conditions for its contribution. When an exact assignment is relied on, the record **MUST** identify the F.6 relation between this act and that assignment, stating its species and matching its holder to the performer. Use an entry for each relied-on pair, including distinct assignments of the same person. List a performer with no exact assignment-bound claim once without that reference. Establish the mandate for representing each party under the governing rule. One assignment can carry authority for several parties, or the same person may act under distinct assignments in one performance.

  The assignment **MUST** have the performer as holder, supply every other participant, cover the act, and satisfy its species predicate for the required scope, working situation, and window. Evidence supports those core facts; a characteristic profile enters only when conditionally consumed. The taxonomy episteme and the rules used to interpret its claims supply the classification basis; they are not assignment participants. Establish any authority required by the receiving use under its applicable rule.
* **(SA‑C2) Act types are independently satisfied recognition classifications.** The occurrence **MUST** instantiate at least one `SpeechActTypeRef` defined by the exact `recognitionTaxonomyRef` under the stated `effectiveReferenceScheme`. If a policy or procedure supplies an additional recognition condition, cite its exact current episteme and satisfy that condition separately.
* **(SA‑C3) Actual extent and interval separation.** The occurrence **MUST** have an actual temporal extent so freshness can be evaluated; the record's `window` is a claim about that act extent. Every instituted commitment, grant, publication relation, status relation, or other effect keeps its own independently governed occurrence or validity interval. Coincident boundaries do not merge act and effect.
* **(SA‑C3a) Policy, procedure, and channel remain neighbors.** A cited `policyOrProcedureRef` is a separate current C.2.1 episteme; its currentness, applicability, and any edition relation must be established under their subject patterns. An optional `channelRef` names an independently governed communication route or participating entity.

Keep three questions separate. `utteranceSubjectRefs` answers **what the utterance or claim is about**. `institutionalTargetRefs` answers **which object or relation the act is intended to institute or update, or which episteme edition it is intended to publish, under the cited current policy or procedure**. Actual change or institutional effect is a third world-side fact and is stated only through its exact direct change/effect relation and the matching typed `institutes.*` reference when the record needs it. An informative notice or assertion may have a subject without any institutional target or changed entity. Shared reference values do not collapse these relation meanings.

**Record- and reliance-side constraints:**

* **(SA‑C4) A relied-on occurrence must be observable.** When a gate or checklist, or a judgement about a commitment or grant, relies on a `SpeechActRef`, the `SpeechActRecord` **SHALL** identify that same occurrence and cite at least one applicable entry from `utteranceDescriptionLocators` or `carrierRefs`, or a separately governed evidence relation. Evidence-critical uses **SHOULD** cite at least one carrier through A.10. Record completeness alone does not prove occurrence or institutional force.
* **(SA‑C5) Institutional-effect claims are typed references to world-side effects.** `institutes.*` may reference only a separately obtaining commitment or relation occurrence through its declared RefKind. Each `institutes.commitments` value resolves through `U.RelationRef constrained to U.Commitment` and is usable only when an identified policy applies and A.2.8's bearer, constitutive-rule, instituting-basis, and continuation conditions hold. Each `institutes.permissions` value resolves to one `GrantedPermissionRelation@Context` whose participants, policy, scheme, and validity satisfy A.2.8.PER; each `institutes.systemRoleAssignments` value resolves to one occurrence whose species is declared under A.2.1; and each publication value resolves to an obtaining `EpistemePublicationRelation` under E.24.PUB. A status claim is an episteme about an effect; keep it and its A.10 evidence relation outside `institutes.*`. A Bridge is added only if the receiving inference depends on translating or comparing local meanings across schemes.
* **(SA‑C6) F.9 only for a cross-locality dependency.** Cite an F.9 Bridge when a receiving check, gate, provenance claim, or effect inference compares, substitutes, or transfers a speech-act type or policy meaning between different local taxonomies, schemes, or policies. A different consumer, organization label, repository location, or downstream use does not by itself create that dependency. The same token in two local schemes does not establish equivalence, and a Bridge does not transfer institutional force by itself.

#### A.2.9:4.3 — `SpeechActRef` discipline (normative)

A **`SpeechActRef`** resolves to one actual Work individual admitted as `SA : U.SpeechAct`. It never denotes the kind itself or a `SpeechActRecord`.

* If an A.2.8 commitment predicate or assertion cites this occurrence as its instituting basis, the referenced occurrence **MUST** satisfy occurrence-side **SA‑C0…SA‑C3a**. Citing the act in the obtaining predicate identifies the required world-side basis; it does not itself require a record. A receiving judgement that relies on this occurrence, including a commitment or grant judgement, gate, audit, or provenance claim, additionally needs the record and evidence basis in **SA‑C4**. It needs **SA‑C6** only when its inference crosses local taxonomies, schemes, or policies.
* A `SpeechActRef` **MUST NOT** be replaced by an `EpistemeRef` (“see the document”) when occurrence provenance is needed. A `SpeechActRecord` or utterance-description episteme may make claims about the occurrence but is not the act.
* If a source cannot yet establish A.15.1 admission for one actual occurrence, it may create a separate `U.Episteme` identified as a **candidate observation stub**. The stub is not a `SpeechActRecord`, supplies no `SpeechActRef` or `speechActOccurrenceRef`, and does not conform to the complete declaration schema or SA-C0. It carries a source-local candidate locator or C.2.1 `ClaimAddress`, known observation claims, provenance for those claims, and explicit unknowns.

  If the actual `enactsMethod -> U.Method` relation cannot yet be recovered, record that unresolved claim and its source-gap provenance in the stub; do not invent a `U.MethodDescription` to establish the missing Method relation. The stub supports no gate or deontic provenance and remains observation-only. After A.15.1 independently admits one exact actual occurrence, create a distinct conformant `SpeechActRecord`; do not promote or relabel the stub in place, though a separately governed provenance or evidence relation may cite it.

#### A.2.9:4.4 — Separation rules with `U.Commitment`, `GrantedPermissionRelation@Context`, and `U.PromiseContent` (normative)

1. **Instituting an enduring deontic relation.** A speech-act occurrence may be the actual instituting basis for one `U.Commitment` or `GrantedPermissionRelation@Context` only under an exact current constitutive policy or rule and the effect pattern's satisfied direct predicate. The enduring relation is separately identified. To state an instituted effect in `SpeechActRecord`, cite its already obtaining occurrence in `institutes.commitments` or `institutes.permissions`; quoted duty or permission wording alone does not establish that effect.

2. **Promise content and the act of offering it.**
   `U.PromiseContent` is the promised-outcome statement. A speech act may offer or issue that promise; any resulting commitment references the separate promise-content episteme.

3. **The act and its evidence carrier.**
   A “signed approval PDF”, ticket, message, or API log is a carrier; it may carry an utterance-description episteme or a `SpeechActRecord`. The speech act is the Work occurrence described or evidenced.

4. **Conditions for publication and institutional effects.**
   **Default interpretation rule (normative).** A conformant model/interpreter **MUST NOT** infer a `U.Commitment`, `GrantedPermissionRelation@Context`, publication occurrence, or subject-specific status relation solely from a `Publish`/`Approve` speech-act occurrence or its record. Publication work may establish an `EpistemePublicationRelation` only when E.24.PUB's selected edition, audience declaration, bounded-use declaration, independently identified expression, carrier, and availability conditions obtain. A constitutive policy may let an act institute a subject-specific `Approved`, `Published`, or similar status relation; then cite that exact relation occurrence through the subject pattern and separately cite any C.2.1 status claim and A.10 evidence. The claim represents the status; judge whether that status obtains under the cited status rule.

#### A.2.9:4.5 — Multi-function and multi-party support (normative)

* **Multi-function:** `actTypes` is a **set**. When one actual communicative Work performs several recognizable functions, one speech-act occurrence carries all satisfied `actTypes`. Identify several occurrences only when the occurrence-identity rule in §4.1 finds distinct world-side grounds. Their records may share utterance or carrier references. If the named use admits competing segmentations, cite its continuity or segmentation rule or leave the boundary unresolved. Institutional effects remain separately referenceable (SA‑C5).

* **Multi-party:** establish who participated in performing the act and who was addressed. One jointly issued declaration may require contributions from several actual performers under §4.1. Several individual approvals may also constitute separate acts whose combination an acceptance rule requires. Use the performance history and that rule to decide which occurred. `addressedTo` separately identifies parties, exact local system-role kinds, or exact obtaining system-role assignments in the audience. Establish any claimed authority, commitment, permission or institutional effect under its applicable rule.

A message addressed to two offices can inform both and record a decision made by one. To attribute acceptance to either office or to a body represented by both, establish who could act for whom, what the act covered and which combination of decisions the rule required. A single authorised decision can settle the whole order. For example, one delegate authorised separately by each office may issue a joint approval with a co-signer. Identify the performances that constituted that one act, the two actual people, and each exact assignment relied on for either of them. Two mandates for one person can justify representation of both offices. They identify two F.6 pairs only if distinct obtaining assignments for the same act are established. Use A.6.C:4.1 when the decision also depends on what the parties separately undertook. Receipt, understanding and use by a particular addressee each need evidence about that addressee. For example, if two offices commission one joint declaration by their delegates and both participate in issuing it as agreed, the joint performance can fulfil that order. If they commission two separate approvals, establish the required act for each. For an acknowledgement-only order, the stipulated acknowledgement by the authorised recipient can be the entire result.

