---
chunk_kind: "child"
pattern_id: "A.2.9"
pattern_title: "U.SpeechAct (Communicative Work Kind, Occurrences, and Records)"
section_id: "A.2.9:4"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/A.2.9/A.2.9__007_solution.md"
commit_sha: "0c3ef3d3921bb3176096e3e6102dd819c42f6446"
heading_path:
  - "A.2.9 — U.SpeechAct (Communicative Work Kind, Occurrences, and Records)"
  - "A.2.9:4 — Solution"
line_start: 7398
line_end: 7537
dependencies:
  - "A.10"
  - "A.13"
  - "A.15.1"
  - "A.2"
  - "A.2.1"
  - "A.2.6"
  - "A.2.8"
  - "A.6.C"
  - "A.7"
  - "F.6"
  - "U.Method"
  - "U.SystemRoleAssignment"
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

When a receiving use is current, state who should understand or do what because of the communicative Work, including later self-use by its producer, then judge that Work against evidence relevant to the stated use. A response, silence, later action, or later change may be evidence, but none by itself defines what the utterance means, proves that the use was achieved, or shows that the Work caused the later effect. Keep the communicative Work distinct from its wording, representation, medium, interpretation, response, later action or change, and any causal claim.

Repair the smallest thing that blocks the stated use—for example, wording, representation, prerequisites, medium, interaction, or a future receiving use—or stop. Judge earlier communicative Work against the use stated for that occurrence. A revised use applies to later communication or to a separately named reevaluation; it does not turn the earlier response into achievement of the earlier declared use. Authority, consent, permission, and ethical or institutional admissibility remain separate questions.

When exact occurrence identity, governance, modeling, audit, or reliance is current, use the admitted kernel kind `U.SpeechAct`. An individual `SA : U.SpeechAct` first passes the independent A.13/A.15.1 admission route: the exact actual performer System satisfies and is classified under one local agential system-role kind, holds one obtaining assignment, and has adequate core evidence; the communicative performance history, enacted Method, temporal extent, and containing-System relation are grounded. A characteristic profile is added only when conditionally consumed. If the use also claims the exact assignment under which the act occurred, F.6 then relates the already admitted `SA` to that same obtaining A.13 assignment. A separate recognition-taxonomy episteme and effective reference scheme make the act-type classification inspectable; an applicable policy or procedure defines any claimed institutional force. A `SpeechActRecord` may describe the occurrence and point to a MethodDescription, optional channel, utterance descriptions, or evidence carriers; none is the act or enacted Method.

#### A.2.9:4.1 — Normative definition

`U.SpeechAct <: U.Work` is a kind declaration. An actual Work individual is admitted as `SA : U.SpeechAct` when its primary effect is **communicative**: it places an utterance through an optional channel in a way classified by an exact speech-act recognition taxonomy under an effective reference scheme and, when institutional force is claimed, by a current policy, procedure, or protocol rule as potentially:

* asserting/informing,
* requesting/directing,
* promising/committing (as an instituting act),
* declaring/authorizing/revoking (status-changing acts),
* notifying (event announcement relevant for downstream work).

Per A.7 and A.15.1, the actual speech-act occurrence is a Work individual; its `SpeechActRecord` and **utterance descriptions** are epistemes, while its **carriers** are utterance carriers, publication carriers, or traces that allow observation and audit. *(Note: “Surface” is reserved for MVPK publication/interoperability surfaces; do not use it here.)*

Occurrence identity specializes A.15.1. Admit a candidate as actual communicative Work from one exact communicative performance history, every actual performer's A.13 core, an enacted Method, temporal extent, and containing-System relation; do not use an F.6 conclusion as an admission premise. Several satisfied act types classify that one Work occurrence. Identify more than one occurrence only when distinct performance history, enacted Methods, institutional actions, or another admitted discriminator establishes distinct Work. A shared utterance, carrier, assignment, or interval decides neither sameness nor difference. If a named use still admits more than one defensible segmentation, cite its continuity or segmentation rule or leave the occurrence boundary unresolved. Check any precise assignment-bound attribution through F.6 only after admission.

Whether a given act type institutes commitments, permissions, publication relations, or status changes depends on an exact current policy or procedure and on the direct obtaining conditions of the claimed effect. Absent that basis, treat `SA : U.SpeechAct` only as actual communicative Work; neither its kind membership, recognition classification, channel, MethodDescription, nor a complete-looking record licenses a deontic or status inference.

#### A.2.9:4.2 — Minimal occurrence-description record (normative)

Use the following declaration schema only when a receiving use needs a persistent claim about one already admitted actual speech-act occurrence. The record fields state claims about the referenced occurrence; they are not fields stored in the Work individual and do not make it occur. A source that has only a candidate observation uses the separate non-conformant episteme/stub described under `SpeechActRef` discipline; it supplies neither a `SpeechActRef` nor a `SpeechActRecord`.

```
U.SpeechAct <: U.Work

SpeechActRef ::= U.EntityRef
  // resolves to one actual Work individual admitted as SA : U.SpeechAct

SpeechActRecord <: U.Episteme

SpeechActRecord ::=
    {
      speechActOccurrenceRef: SpeechActRef,
      actualPerformerSystemRef: U.EntityRef,            // resolves to the A.13-qualified System projected as RA.HolderSystemSlot
      performedUnderAssignmentRef: optional<U.RelationRef constrained to F.6 performedUnderAssignment>, // omit when the record makes no exact assignment-bound attribution; any present reference resolves after independent Work admission to the exact relation for this act and the same obtaining A.13 assignment
      enactsMethodRef: optional<U.EntityRef>,        // resolves to the exact U.Method enacted by the actual Work
      methodDescriptionRef: optional<U.EpistemeRef>, // separate C.2.1 episteme used only when it identifies, constrains, or justifies that Method or intended Work
      unresolvedEnactsMethodClaimAddress: optional<ClaimAddress>,
      methodRelationGapProvenanceRef: optional<U.EpistemeRef>,
      reliancePosture: observationOnly | relianceReady,
      workContainmentRelationRefs: set<U.RelationRef>,       // non-empty; exact locally declared A.15.1 Work-to-System relation occurrences used by this record
      window: [start, end | open],                   // the act occurrence's extent, never an instituted effect's validity interval
      recognitionTaxonomyRef: U.EpistemeRef,         // exact speech-act recognition taxonomy
      effectiveReferenceScheme: U.ReferenceScheme,  // scheme under which actTypes and cited policy/procedure are interpreted
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
    // locates the rule that defines and tests that relation; it is not the relation or an actor

InstitutedEffects ::=
  {
    commitments: optional<set<U.RelationRef constrained to U.Commitment>>,
    permissions: optional<set<GrantedPermissionRelationRef@Context>>,
    systemRoleAssignments: optional<set<U.RelationRef constrained to U.SystemRoleAssignment>>,
    publicationRelations: optional<set<EpistemePublicationRelationRef>>,
    otherGovernedRelations: optional<set<GovernedInstitutedRelationLink>>
  }
```

**Occurrence-side constraints:**

* **(SA‑C0) Actual Work conformance.** The individual referenced by `speechActOccurrenceRef` **MUST** first satisfy independent A.15.1 admission: every actual performer has the A.13 core for the communicative action, scope, working situation, and window; the performance history is grounded; and the Work has an actual `enactsMethod -> U.Method` relation, temporal extent, and at least one obtaining locally declared Work-to-System containment relation. Add a characteristic profile only when a Grade, autonomy or profile result, criterion-dependent characteristic, or assurance use consumes it. A complete record creates none of those facts. A record that makes no exact assignment-bound attribution **MAY** omit `performedUnderAssignmentRef`. Whenever that field is present or the record claims exact assignment-bound attribution, it **MUST** resolve to a separate F.6 relation established after admission for this already admitted act through the same obtaining A.13 assignment. `methodDescriptionRef`, when present, cites a separate C.2.1 episteme; the description is not enacted.
* **(SA‑C1) The System performs; exact attribution reuses the same assignment.** The performer **MUST** be an admitted `U.System` that satisfies and is classified under one exact local agential system-role kind for this act. An observation-only or otherwise non-attribution record **MAY** omit `performedUnderAssignmentRef` and **MUST NOT** be used to satisfy a guard, gate, or claim that depends on exact assignment-bound attribution. If the field is present, it **MUST** resolve to the separately obtaining F.6 `performedUnderAssignment` relation for the already admitted act and the same obtaining assignment occurrence named by A.13, together with its declared `U.SystemRoleAssignment` species. If a guard, gate, or claim relies on exact assignment-bound attribution, the field **MUST** be present and that F.6 relation **MUST** obtain. The assignment **MUST** have the performer as holder, supply every other participant, cover the act, and satisfy its species predicate for the required scope, working situation, and window. Evidence supports those core facts; a characteristic profile enters only when conditionally consumed. Taxonomy and reference-scheme epistemes may interpret an assertion but are not assignment participants. The assignment supplies neither authority nor action by form; it does not perform the act.
* **(SA‑C2) Act types are independently satisfied recognition classifications.** The occurrence **MUST** instantiate at least one `SpeechActTypeRef` defined by the exact `recognitionTaxonomyRef` under the stated `effectiveReferenceScheme`. A token written into a record does not establish that classification. If a policy or procedure supplies an additional recognition condition, cite its exact current episteme and satisfy that condition separately.
* **(SA‑C3) Time honesty and interval separation.** The occurrence **MUST** have an actual temporal extent so freshness can be evaluated; the record's `window` is a claim about that act extent, not the extent itself. Every instituted commitment, grant, publication relation, status relation, or other effect keeps its own independently governed occurrence or validity interval. Coincident boundaries do not merge act and effect.
* **(SA‑C3a) Policy, procedure, and channel remain neighbors.** A cited `policyOrProcedureRef` is a separate current C.2.1 episteme; its currentness, applicability, and any edition relation must be established under their subject patterns. An optional `channelRef` names an independently governed communication route or participating entity. Neither citation becomes the Method, the Work occurrence, an utterance description, a carrier, or an institutional effect merely by inclusion in the record.

Keep three questions separate. `utteranceSubjectRefs` answers **what the utterance or claim is about**. `institutionalTargetRefs` answers **which object or relation the act is intended to institute or update under the cited current policy or procedure**. Actual change or institutional effect is a third world-side fact and is stated only through its exact direct change/effect relation and the matching typed `institutes.*` reference when the record needs it. An informative notice or assertion may have a subject without any institutional target or changed entity. Shared reference values do not collapse these relation meanings.

**Record- and reliance-side constraints:**

* **(SA‑C4) A relied-on occurrence must be observable.** When a gate, checklist, commitment, or grant relies on a `SpeechActRef`, the `SpeechActRecord` **SHALL** identify that same occurrence and cite at least one applicable `utteranceRef`, `carrierRef`, or separately governed evidence relation. Evidence-critical uses **SHOULD** cite at least one carrier through A.10. Record completeness alone does not prove occurrence or institutional force.
* **(SA‑C5) Institutional-effect claims are typed references to world-side effects.** `institutes.*` may reference only a separately obtaining commitment or relation occurrence through its declared RefKind. Each `institutes.commitments` value resolves through `U.RelationRef constrained to U.Commitment` and is usable only when an identified policy applies and A.2.8's bearer, constitutive-rule, instituting-basis, and continuation conditions hold. Each `institutes.permissions` value resolves to one `GrantedPermissionRelation@Context` whose participants, policy, scheme, and validity satisfy A.2.8.PER; each `institutes.systemRoleAssignments` value resolves to one occurrence whose species is declared under A.2.1; and each publication value resolves to an obtaining `EpistemePublicationRelation` under E.24.PUB. A status claim is an episteme about an effect, not an instituted effect; keep it and its A.10 evidence relation outside `institutes.*`. A Bridge is added only if the receiving inference depends on translating or comparing local meanings across schemes.
* **(SA‑C6) F.9 only for a real cross-locality dependency.** Cite an F.9 Bridge when a receiving check, gate, provenance claim, or effect inference actually compares, substitutes, or transfers a speech-act type or policy meaning between different local taxonomies, schemes, or policies. A different consumer, organization label, repository location, or downstream use does not by itself create that dependency. The same token in two local schemes does not establish equivalence, and a Bridge does not transfer institutional force by itself.

#### A.2.9:4.3 — `SpeechActRef` discipline (normative)

A **`SpeechActRef`** resolves to one actual Work individual admitted as `SA : U.SpeechAct`. It never denotes the kind itself or a `SpeechActRecord`.

* If an A.2.8 commitment predicate or assertion cites this occurrence as its instituting basis, the referenced occurrence **MUST** satisfy occurrence-side **SA‑C0…SA‑C3a**. A gate, audit, or provenance use additionally needs the record and evidence basis in **SA‑C4** and needs **SA‑C6** only when its inference really crosses local taxonomies, schemes, or policies.
* A `SpeechActRef` **MUST NOT** be replaced by an `EpistemeRef` (“see the document”) when occurrence provenance is needed. A `SpeechActRecord` or utterance-description episteme may make claims about the occurrence but is not the act.
* If a source cannot yet establish A.15.1 admission for one actual occurrence, it may create a separate `U.Episteme` identified as a **candidate observation stub**. The stub is not a `SpeechActRecord`, supplies no `SpeechActRef` or `speechActOccurrenceRef`, and does not conform to the complete declaration schema or SA-C0. It carries a source-local candidate locator or C.2.1 `ClaimAddress`, known observation claims, provenance for those claims, and explicit unknowns. If the actual `enactsMethod -> U.Method` relation cannot yet be recovered, record that unresolved claim and its source-gap provenance in the stub; never mint an `AdHocCommunication` or other `U.MethodDescription` to close it. The stub makes no candidate actual, supports no gate or deontic provenance, and remains observation-only. After A.15.1 independently admits one exact actual occurrence, create a distinct conformant `SpeechActRecord`; do not promote or relabel the stub in place, though a separately governed provenance or evidence relation may cite it.

#### A.2.9:4.4 — Separation rules with `U.Commitment`, `GrantedPermissionRelation@Context`, and `U.PromiseContent` (normative)

1. **Speech act is not an enduring deontic relation.** A speech-act occurrence may be the actual instituting basis for one `U.Commitment` or `GrantedPermissionRelation@Context` only under an exact current constitutive policy or rule and the effect pattern's satisfied direct predicate. The enduring relation is separately identified. Do not encode obligations or permissions as prose inside `SpeechActRecord`; cite only the exact already obtaining relation occurrences in `institutes.commitments` or `institutes.permissions`.

2. **Speech act is not the service promise clause.**
   `U.PromiseContent` is the promised-outcome statement; a speech act may be the act of offering or issuing that promise, but the promise content lives in the promise-content object and is referenced from the resulting commitments.

3. **Speech act is not the carrier.**
   A “signed approval PDF”, ticket, message, or API log is a carrier; it may carry an utterance-description episteme or a `SpeechActRecord`. The speech act is the Work occurrence described or evidenced, not either episteme and not the carrier.

4. **Publishing a spec is not a commitment by default.**
   **Default interpretation rule (normative).** A conformant model/interpreter **MUST NOT** infer a `U.Commitment`, `GrantedPermissionRelation@Context`, publication occurrence, or subject-specific status relation solely from a `Publish`/`Approve` speech-act occurrence or its record. Publication work may establish an `EpistemePublicationRelation` only when E.24.PUB's selected edition, audience, bounded use, form, carrier, and availability conditions obtain. A constitutive policy may let an act institute a subject-specific `Approved`, `Published`, or similar status relation; then cite that exact relation occurrence through the subject pattern and separately cite any C.2.1 status claim and A.10 evidence. The claim represents the status; neither its ID nor its publication makes the status obtain.

#### A.2.9:4.5 — Multi-function and multi-party support (normative)

* **Multi-function:** `actTypes` is a **set**. When one actual communicative Work performs several recognizable functions, one speech-act occurrence carries all satisfied `actTypes`; taxonomy tokens do not multiply the Work. Identify several occurrences only when the occurrence-identity rule in §4.1 finds distinct world-side grounds. Their records may share utterance or carrier references without thereby becoming the same occurrence. If the named use still admits competing segmentations, cite its continuity or segmentation rule or leave the boundary unresolved. Institutional effects remain separately referenceable (SA‑C5).

* **Multi-party:** `addressedTo` is a set. Its optional members may be parties, exact local system-role kinds, or exact obtaining occurrences of directly declared `U.SystemRoleAssignment` species. State which branch each addressee uses. Being addressed makes none of them the performer and establishes no authority, commitment, permission, responsibility, or institutional effect.

