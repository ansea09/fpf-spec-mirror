---
chunk_kind: "child"
pattern_id: "A.2.8"
pattern_title: "U.Commitment (Deontic Commitment Relation)"
section_id: "A.2.8:4"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/A.2.8/A.2.8__007_solution.md"
commit_sha: "9fba9529833b4e288fa149878b22a9ee44e1886f"
heading_path:
  - "A.2.8 — U.Commitment (Deontic Commitment Relation)"
  - "A.2.8:4 — Solution"
line_start: 6778
line_end: 6913
dependencies:
  - "A.10"
  - "A.15.1"
  - "A.2"
  - "A.2.1"
  - "A.2.3"
  - "A.2.6"
  - "A.2.8.PER"
  - "A.2.9"
  - "A.6.B"
  - "A.6.C"
  - "A.6.RCD"
  - "A.7"
  - "C.3"
  - "F.6"
keywords:
  - "actual bearer"
  - "constitutive rule"
  - "do not identify an individual bearer or institute a duty. Adapt"
  - "individual duty"
  - "instituting basis"
  - "obligation"
  - "prohibition"
  - "recommendation-as-duty"
  - "validity interval"
---

### A.2.8:4 - Solution

#### A.2.8:4.1 - Direct Participants and Predicate Parameters

One `U.Commitment` occurrence has:

- exactly one actual duty bearer, expressed by either `dutyBearerSystemRef : U.EntityRef constrained to an admitted U.System` or a separately governed local `dutyBearerPartyRef : PartyRef`;
- a non-empty exact set of duty referents stating the action, avoidance, outcome, promise content, claim, or other governed object to which the duty applies; and
- optional actual counterparties or beneficiaries when the duty is owed to someone.

Exactly one duty-bearer branch is filled. A system-role kind, classification judgment, assignment occurrence, organizational-position label, publication, policy, or claim record is not the bearer.

The normalized modality is a by-value predicate parameter:

```text
DeonticModalityToken ::= MUST | MUST_NOT | SHOULD | SHOULD_NOT
```

`SHALL` and `REQUIRED` map to `MUST`; `SHALL NOT` and `PROHIBITED` map to `MUST_NOT`; `RECOMMENDED` maps to `SHOULD`; and `NOT RECOMMENDED` maps to `SHOULD_NOT` only after the source claim has been recovered as a duty. `MAY` and `OPTIONAL` do not normalize into `U.Commitment`; route their current meaning to A.2.8.PER, an admissibility predicate, or ordinary prose.

Scope and validity delimit applicability. Duty referents are cited by exact identifiers when they already exist. Useful referent kinds include a claim ID, `U.PromiseContent`, an action or outcome specification, an admitted Method, or an already identified Work occurrence when the duty concerns that occurrence. A MethodDescription is cited only when the duty depends on claims in that exact episteme edition; description is not mandatory indirection to the Method.

The current normative policy or prescription, its constitutive rule, the actual instituting basis, provenance, and adjudication evidence are grounds or qualifiers. They are not extra duty bearers and do not become deontic participants by appearing in a record.

#### A.2.8:4.2 - When the Relation Obtains

For proposed occurrence `C`, the direct predicate `C : U.Commitment` obtains only when all of the following hold:

1. the actual duty bearer and any actual counterparties are admitted, and the duty referents are identified;
2. one identified normative policy or prescription is current and applies to those participants, referents, scope, and time;
3. that policy contains or cites one exact constitutive rule for an individual commitment rather than only generic content about a system-role kind;
4. the rule's required instituting basis and world-side facts obtain;
5. modality, scope, validity window, and every rule-required condition are satisfied; and
6. no valid revocation, defeat, expiry, or supersession has ended the relation.

For the current A.2.9 path, the instituting basis is an actual `U.SpeechAct` Work occurrence recognized by the current policy, with the actual performer and exact covering system-role assignment independently established. Another basis is usable only when a subject pattern admits it and gives its occurrence rule.

If the corpus lacks the constitutive rule or the required instituting-relation predicate, return `missing-governor[individual commitment institution]`. If an applicable rule is false, the proposed commitment does not obtain. If a required evidence dependency is unavailable, reliance on the assertion is `unknown`; do not invent the relation or infer its negation.

#### A.2.8:4.3 - Occurrence Identity and Continuity

One occurrence is identified by:

- the actual duty bearer;
- exact duty referents and counterparties;
- normalized modality and scope;
- constitutive policy and rule;
- the actual instituting basis, only when that rule makes the basis identity-bearing; and
- one maximal continuous validity interval.

The actual instituting basis is always required for obtaining. It is part of occurrence identity only when the exact constitutive rule says that reinstitution identifies another duty. A compatible policy edition, new record, or later instituting act preserves the occurrence only through an explicit continuity decision showing that every identity-bearing fact and the rule's deontic effect continue. A changed bearer, modality, referent set, constitutive rule, identity-bearing basis, or interrupted validity yields another occurrence. The commitment ID and its describing claim do not decide sameness.

When a rule makes a duty end with a system-role assignment, an assignment boundary ends that commitment. When the rule makes the duty persist for the same actual system across a replacement assignment, state that continuity explicitly. A different actual bearer always requires another commitment occurrence.

#### A.2.8:4.4 - Generic Prescriptions and Assignment-Mediated Rules

A generic prescription states what one exact policy or other normative episteme requires; it does not create an individual duty bearer or commitment occurrence. A claim that one actual System or separately governed party has that duty instead cites one separately obtaining A.2.8 `U.Commitment`.

For example, a policy can concern `ProviderSystemRole` or another exact local system-role kind. Its `systemRoleKindRef : U.KindRef` can appear in the rule's antecedent, but the policy episteme is not an individual `U.Commitment`.

An exact `systemRoleAssignmentRef : U.RelationRef constrained to U.SystemRoleAssignment` can show that an actual system satisfies one applicability condition for a time. The assignment is still not the duty bearer or the commitment relation. The only valid direction is:

```text
current policy or prescription
+ exact constitutive rule
+ actual admitted system
+ obtaining exact system-role assignment or other rule-required facts
+ actual instituting basis required by that rule
-> one separately identified U.Commitment whose duty bearer is that actual system
```

Classification or assignment alone never completes the implication. The rule states whether the duty starts, continues, and ends with the assignment.

#### A.2.8:4.5 - Assertion, Record, and Adjudication

An assertion or record about a commitment is a separately identified claim-bearing episteme. A compact reliance record can expose:

```text
CommitmentAssertion:
  entityOfConcernRef: U.RelationRef constrained to one exact U.Commitment occurrence
  dutyBearerSystemRef? | dutyBearerPartyRef?: the actual bearer stated by the relation
  dutyReferentRefs: non-empty exact set
  counterpartyRefs?: actual counterparties or beneficiaries
  modality: normalized by-value token
  scopeRef:
  validityWindowRef:
  constitutivePolicyRef: exact current normative episteme edition
  constitutiveRuleRef: exact rule claim
  institutingBasisRef: exact actual basis required by that rule
  evidenceClaimRefs?: exact support used for reliance or adjudication
  carrierRefs?: carriers used as evidence or source
  assertionStatus: affirmed | denied | unresolved
```

Use the record to describe the relation. `evidenceClaimRefs` and carriers support reliance; they are not participants or instituting facts unless the identified constitutive rule makes one such fact current and the pattern for that subject supplies its test. If adjudication is intended, cite the exact evidence claims, criteria, and carriers. If no adjudication is claimed, do not invent an audit apparatus.

When a later use must compare incompatible commitments, keep the commitments unchanged and carry the needed conflict inputs in one local claim:

```text
CommitmentConflictInputClaim:
  selectionUseRef: exact conflict or choice question
  commitmentRows: non-empty set of
    commitmentRef: U.RelationRef constrained to one exact U.Commitment occurrence
    institutingBasisRef: exact actual basis required by its constitutive rule
    issuingSystemRef | issuingPartyRef: exactly one actual issuer recoverable from that basis
    authorityRelationRef?: U.RelationRef constrained by the direct authority predicate used by selectionUseRef
  selectingRuleRef?: exact priority or choice rule required by selectionUseRef
  unresolvedInputRefs?: exact missing-information or missing-governor results
```

These conflict inputs stay outside commitment identity by default. Each authority relation must already obtain under its own predicate, and each selecting rule must be current and applicable to this selection use under the pattern that defines it. If this selection use requires an authority relation or selecting rule and that input is unavailable or no current pattern defines it, put its exact unresolved result in `unresolvedInputRefs`, such as `missing-governor[commitment conflict authority relation]` or `missing-governor[commitment conflict selecting rule]`. An optional field means that the input is not required for this use; it never licenses dropping a required input. For an interlevel ethical conflict, use D.3 to map the conflict and D.4 for mediation or decision use. When an explicit choice among already available options is current, C.11 supplies the `ChoiceRule` and `ChoiceResult`. Otherwise apply the direct pattern for the claimed conflict result; if none exists, return `missing-governor[commitment conflict resolution]`.

Evidence used only to measure or verify the duty belongs to the support for the assertion. An evidence-producing or evidence-retaining duty instead names that production or retention content among its duty referents.

#### A.2.8:4.6 - Direct Neighboring Relations

| Current question | Direct result | Unsupported inference |
| --- | --- | --- |
| What does a generic policy prescribe? | one normative claim episteme and its applicable rule content | an individual duty from generic content alone |
| Which System holds a local system-role assignment? | one A.2.1 assignment occurrence and its declared species | a duty or responsibility |
| Did a communicative act occur? | one A.2.9 `U.SpeechAct` Work occurrence | its institutional effect without the constitutive rule |
| Is the bearer responsible? | one admitted domain responsibility predicate and occurrence; otherwise the exact missing governor | responsibility from duty, assignment, position, or “owner” wording |
| Is an action permitted or authorized? | the exact A.2.8.PER grant, exercise, non-prohibition, non-violation, or conflict result | permission from commitment or assignment |
| Did access occur? | an exact domain access relation; otherwise `missing-governor` | access from permission, duty, or assignment |
| Did the bearer perform Work? | recover the exact actual performer through A.13 and let A.15.1 independently admit one dated `U.Work`; add F.6 only when this duty account or its receiving use expressly consumes precise assignment-bound attribution through the same obtaining A.13 assignment | Work or attribution from the duty alone |
| Was the duty satisfied or violated? | a separately governed evaluation or compliance result using actual Work and evidence | compliance from publication or record completeness |
| What resulted? | the separately identified result and its direct result relation, or A.15.PROD for production and inception | a generic result relation from duty or Work |

The common corpus has no universal responsibility predicate. `VP.AllocationResponsibility` can help a reader recognize the concern; the applicable domain responsibility predicate determines whether the relation obtains.

#### A.2.8:4.7 - Boundary Claim Use

An A.6.B D-quadrant claim about an obtaining individual obligation, recommendation-as-duty, or prohibition cites the exact `U.Commitment` occurrence. A D-claim about generic policy content remains a claim about that content until the individual predicate above is satisfied.

Strong or weak permission, exercise, non-violation, and permission-conflict claims cite their exact A.2.8.PER result and do not acquire a `U.Commitment` payload. Gates remain A-claims, laws and definitions remain L-claims, and Work and evidence effects remain E-claims.

