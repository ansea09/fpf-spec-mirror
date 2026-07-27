---
chunk_kind: "child"
pattern_id: "A.2.9"
pattern_title: "U.SpeechAct (Communicative Work Kind, Occurrences, and Records)"
section_id: "A.2.9:4"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/A.2.9/A.2.9__007_solution.md"
commit_sha: "66e732dfef7a4a93ff23eec43b3f759a6664652d"
heading_path:
  - "A.2.9 — U.SpeechAct (Communicative Work Kind, Occurrences, and Records)"
  - "A.2.9:4 — Solution"
line_start: 6337
line_end: 6462
dependencies:
  - "A.10"
  - "A.15.1"
  - "A.2"
  - "A.2.1"
  - "A.2.6"
  - "A.2.8"
  - "A.6.C"
  - "A.7"
  - "U.Work"
keywords:
  - "actual communicative occurrence"
  - "admitted speech-act Work kind"
  - "authority-grounding assignment"
  - "evidence carrier"
  - "institutional target and effect"
  - "optional SpeechActRecord"
  - "performing U.System"
  - "publication relation"
  - "utterance description"
---

### A.2.9:4 — Solution

`U.SpeechAct` is the admitted kernel kind for communicative Work. An individual `SA : U.SpeechAct` is the actual enactment performed by an admitted accountable `U.System` under an exact obtaining role assignment within a bounded context. A `SpeechActRecord` may describe that occurrence and point to utterance descriptions or evidence carriers; none of those epistemic or representational objects is the act.

#### A.2.9:4.1 — Normative definition

`U.SpeechAct <: U.Work` is a kind declaration. An actual Work individual is admitted as `SA : U.SpeechAct` when its primary effect is **communicative**: it places an utterance into a context in a way that is recognized by that context’s institutional semantics (policies, procedures, protocol rules) as potentially:

* asserting/informing,
* requesting/directing,
* promising/committing (as an instituting act),
* declaring/authorizing/revoking (status-changing acts),
* notifying (event announcement relevant for downstream work).

Per A.7 and A.15.1, the actual speech-act occurrence is a Work individual; its `SpeechActRecord` and **utterance descriptions** are epistemes, while its **carriers** are utterance carriers, publication carriers, or traces that allow observation and audit. *(Note: “Surface” is reserved for MVPK publication/interoperability surfaces; do not use it here.)*

Whether a given act type institutes commitments, permissions, or status changes is entirely context-policy dependent. Absent an explicit policy, treat `SA : U.SpeechAct` only as an actual communicative Work occurrence; neither its kind membership nor a complete-looking record licenses a deontic inference.

#### A.2.9:4.2 — Minimal occurrence-description record (normative)

Use the following declaration schema only when a receiving use needs a persistent claim about an actual or candidate speech-act occurrence. The record fields state claims about the referenced occurrence; they are not fields stored in the Work individual and do not make it occur.

```
U.SpeechAct <: U.Work

SpeechActRef ::= U.EntityRef
  // resolves to one actual Work individual admitted as SA : U.SpeechAct

SpeechActRecord <: U.Episteme

SpeechActRecord ::=
    {
      speechActOccurrenceRef: SpeechActRef,
      performedBy: U.EntityRef,                     // resolves to the admitted U.System that acts
      performedUnderAssignment: RoleAssignmentRef,  // exact covering role/authority ground
      enactsMethodRef: optional<U.EntityRef>,        // resolves to the exact U.Method when recovered
      methodDescriptionRef: optional<U.EpistemeRef>, // separate description, only when the use needs it
      unresolvedEnactsMethodClaimRef: optional<ClaimIdRef>,
      methodRelationGapProvenanceRef: optional<U.EpistemeRef>,
      reliancePosture: observationOnly | relianceReady,
      executedWithin: U.EntityRef,                   // claim about the containing U.System
      window: [start, end | open],                   // claim about the occurrence's actual extent
      judgementContextRef: U.BoundedContextRef,
      utteranceSubjectRefs: optional<set<U.EntityRef>>,
      institutionalTargetRefs: optional<set<U.EntityRef>>,
      actTypes: set<SpeechActTypeRef>,               // ≥1 act types (supports multi-function)
      addressedTo: optional<set<AddresseeRef>>,      // optional: who is addressed / audience
      utteranceRefs: optional<set<DescriptionRef>>,  // where the utterance description is stated or recorded (A.7: Description)
      carrierRefs: optional<set<CarrierRef>>,        // evidence carriers/traces (A.7: Carrier; use A.10 when evidentiary)
      institutes: optional<InstitutedEffects>,       // references to objects/claims instituted/updated by this act
      notes: optional<InformativeText>               // explicitly informative
    }

DescriptionRef ::=
  ClaimIdRef | EpistemeRef
  // Pointer to an utterance description (e.g., spec clause claim ID, a policy episteme, a message-content episteme).

SpeechActTypeRef ::=
  ContextLocalTokenRef
  // Must be defined/recognized in the Work’s judgement context (bounded context).

AddresseeRef ::=
  PartyRef | RoleRef | RoleAssignmentRef

GrantedPermissionRelationRef@Context ::= U.EntityRef
  // resolves only to one exact GrantedPermissionRelation@Context occurrence

EpistemePublicationRelationRef ::= U.EntityRef
  // resolves only to one exact E.24.PUB EpistemePublicationRelation occurrence

InstitutedEffects ::=
  {
    commitments: optional<set<CommitmentIdRef>>,
    permissions: optional<set<GrantedPermissionRelationRef@Context>>,
    roleAssignments: optional<set<RoleAssignmentRef>>,
    publicationRelations: optional<set<EpistemePublicationRelationRef>>
  }
```

**Occurrence-side constraints:**

* **(SA‑C0) Actual Work conformance.** The individual referenced by `speechActOccurrenceRef` **MUST** independently satisfy `U.Work` conformance (A.15.1), including the actual performer system, covering assignment, enacted method, containing system, temporal extent, and judgement-context anchoring. A complete record neither creates those facts nor substitutes for them.
* **(SA‑C1) The accountable system performs; the assignment grounds.** The occurrence's actual performer **MUST** be an admitted `U.System`. The exact obtaining `U.RoleAssignment` under which it acts **MUST** have that system in `HolderSystemSlot` and cover the act. The assignment supplies role, authority, and attribution ground; it does not perform the act.
* **(SA‑C2) Act types are occurrence classifications and context-local.** The occurrence **MUST** instantiate at least one `SpeechActTypeRef` recognized in its judgement context. A token written into a record does not establish that classification unless the context's predicate is satisfied.
* **(SA‑C3) Time honesty.** The occurrence **MUST** have an actual temporal extent so freshness can be evaluated; a recorded timestamp is a claim about that extent, not the extent itself.

Keep three questions separate. `utteranceSubjectRefs` answers **what the utterance or claim is about**. `institutionalTargetRefs` answers **which object or relation the act is intended to institute or update under the named policy**. Actual change or institutional effect is a third world-side fact and is stated only through its exact direct change/effect relation and the matching typed `institutes.*` reference when the record needs it. An informative notice or assertion may have a subject without any institutional target or changed entity. Shared reference values do not collapse these relation meanings.

**Record- and reliance-side constraints:**

* **(SA‑C4) A relied-on occurrence must be observable.** When a gate, checklist, commitment, or grant relies on a `SpeechActRef`, the `SpeechActRecord` **SHALL** identify that same occurrence and cite at least one applicable `utteranceRef`, `carrierRef`, or separately governed evidence relation. Evidence-critical uses **SHOULD** cite at least one carrier through A.10. Record completeness alone does not prove occurrence or institutional force.
* **(SA‑C5) Institutional-effect claims are typed references to world-side effects.** `institutes.*` may reference only the exact commitment or relation occurrence through its declared RefKind. Each `institutes.permissions` value **MUST** be a `GrantedPermissionRelationRef@Context` whose context matches the speech-act occurrence's judgement context or is connected by the explicit Bridge used by the receiving claim. Each `institutes.publicationRelations` value **MUST** resolve to an obtaining `EpistemePublicationRelation` under E.24.PUB. A status claim is an episteme about an effect, not an instituted effect; keep it and its A.10 evidence relation outside `institutes.*`. The cited policy and direct world-side obtaining conditions still decide whether any effect exists.
* **(SA‑C6) Cross-context use is Bridge-only.** If a `SpeechActRef` or `SpeechActRecord` is interpreted for checking, gate evidence, or provenance in a different bounded context than the occurrence's judgement context, the receiving claim **MUST** cite the Bridge/policy that licenses that interpretation rather than assuming equivalent force from the same label.

#### A.2.9:4.3 — `SpeechActRef` discipline (normative)

A **`SpeechActRef`** resolves to one actual Work individual admitted as `SA : U.SpeechAct`. It never denotes the kind itself or a `SpeechActRecord`.

* If another object (for example, `U.Commitment.source.speechActRef`) cites a `SpeechActRef`, the referenced occurrence **MUST** satisfy occurrence-side **SA‑C0…SA‑C3**. A gate, audit, or provenance use additionally needs the record/evidence basis in **SA‑C4** and **SA‑C6** when cross-context.
* A `SpeechActRef` **MUST NOT** be replaced by an `EpistemeRef` (“see the document”) when occurrence provenance is needed. A `SpeechActRecord` or utterance-description episteme may make claims about the occurrence but is not the act.
* If a source cannot complete a `SpeechActRecord`, it may create an observation stub with the candidate `speechActOccurrenceRef`, known claims, provenance for those claims, and explicit unknowns. When the actual `enactsMethod` relation is not recoverable, leave `enactsMethodRef` absent, cite the exact unresolved claim and source-gap provenance, and set `reliancePosture=observationOnly`. The stub does not make the candidate actual, satisfy occurrence-side conformance, or support gate/deontic provenance. It becomes reliance-ready only after the exact `enactsMethod -> U.Method` relation is recovered, or after the governing Work architecture explicitly establishes that this occurrence needs no such relation. Never mint an `AdHocCommunication` or other `U.MethodDescription` solely to fill the gap; a description neither is the method nor enacts itself.

#### A.2.9:4.4 — Separation rules with `U.Commitment`, `GrantedPermissionRelation@Context`, and `U.PromiseContent` (normative)

1. **Speech act is not the enduring deontic relation.**
   A speech-act occurrence may **institute** a `U.Commitment` for an obligation, recommendation-as-duty, or prohibition, or a `GrantedPermissionRelation@Context` for strong permission. The enduring relation is the separately governed object, not the act. Do not encode obligations or permissions as prose inside its `SpeechActRecord`: cite commitments in `institutes.commitments` and grants in `institutes.permissions`, each under the exact instituting policy (`A.2.8`, `A.2.8.PER`).

2. **Speech act is not the service promise clause.**
   `U.PromiseContent` is the promised-outcome statement; a speech act may be the act of offering or issuing that promise, but the promise content lives in the promise-content object and is referenced from the resulting commitments.

3. **Speech act is not the carrier.**
   A “signed approval PDF”, ticket, message, or API log is a carrier; it may carry an utterance-description episteme or a `SpeechActRecord`. The speech act is the Work occurrence described or evidenced, not either episteme and not the carrier.

4. **Publishing a spec is not a commitment by default.**
   **Default interpretation rule (normative).** A conformant model/interpreter **MUST NOT** infer a `U.Commitment`, `GrantedPermissionRelation@Context`, publication occurrence, or subject-specific status relation solely from a `Publish`/`Approve` speech-act occurrence or its record. Publication work may establish an `EpistemePublicationRelation` only when E.24.PUB's selected edition, audience, bounded use, form, carrier, and availability conditions obtain. A constitutive policy may let an act institute a subject-specific `Approved`, `Published`, or similar status relation; then cite that exact relation occurrence through the subject pattern and separately cite any C.2.1 status claim and A.10 evidence. The claim represents the status; neither its ID nor its publication makes the status obtain.

#### A.2.9:4.5 — Multi-function and multi-party support (normative)

* **Multi-function:** `actTypes` is a **set**. If one utterance performs multiple recognizable acts (e.g., “approve + instruct + warn”), the model may either:

   * identify one speech-act occurrence and let its `SpeechActRecord` state multiple satisfied `actTypes`, or
   * identify multiple actual speech-act occurrences and give each its own `SpeechActRef`; their records may share the same `carrierRefs/utteranceRefs`.
   In either case, institutional effects must remain referenceable (SA‑C5).

* **Multi-party:** `addressedTo` is a set and may include roles/parties/assignments. If addressees matter for validity (e.g., “approval by CAB chair to deployment bot”), they should be explicit.

