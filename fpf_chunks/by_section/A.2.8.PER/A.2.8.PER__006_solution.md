---
chunk_kind: "child"
pattern_id: "A.2.8.PER"
pattern_title: "Granted Permission, Exercise, and Non-Prohibition"
section_id: "A.2.8.PER:4"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/A.2.8.PER/A.2.8.PER__006_solution.md"
commit_sha: "4b75b56c13f5d61be5238fdbc7c20af5c6f89df7"
heading_path:
  - "A.2.8.PER — Granted Permission, Exercise, and Non-Prohibition"
  - "A.2.8.PER:4 — Solution"
line_start: 6005
line_end: 6188
dependencies:
  - "A.10"
  - "A.15.1"
  - "A.15.5"
  - "A.2.8"
  - "A.2.9"
  - "A.6"
  - "A.6.B"
  - "A.6.C"
  - "F.6"
  - "U.Work"
keywords:
  - "checked non-violation"
  - "exact policy rule or decision result"
  - "matching dated-work exercise"
  - "permission or prohibition conflict"
  - "policy-valid strong grant"
  - "weak non-prohibition finding"
---

### A.2.8.PER:4 - Solution

#### A.2.8.PER:4.1 - Keep the permission objects separate

Use exactly the object warranted by the current claim:

- `NonProhibitionFinding@Context` is a frame-relative episteme returned before action when a sufficiently complete current normative frame contains no applicable prohibition.
- `GrantedPermissionRelation@Context` is an enduring strong permission instituted under an exact policy.
- `PermissionExerciseRelation@Context` connects actual dated work to one obtaining grant occurrence when action and beneficiary eligibility match.
- `NonViolationFinding@Context` is a frame-relative episteme about actual work that instantiates no applicable prohibition in the checked frame.
- `PermissionNormConflictFinding@Context` is an episteme exposing an incompatible current grant and prohibition or commitment over matching content, scope, and window.

Absence of any one object does not imply another. In particular, no grant is inferred from a weak finding, no exercise is inferred from a grant, and work outside a grant is not called a violation of that grant.

#### A.2.8.PER:4.2 - Use the closed beneficiary reference family

```text
PermissionBeneficiaryRef ::= RoleRef | RoleAssignmentRef | PartyRef
```

The participant meaning is stable: the exact entity designated by the grant as beneficiary. The reference branch changes only the exercise-eligibility test:

- `RoleAssignmentRef` covers that exact current assignment.
- `RoleRef` covers current assignments that instantiate the role in the declared context under the grant policy; the role value itself does not perform work.
- `PartyRef` covers work only when its exact performer or on-behalf-of relation satisfies the policy. Shared naming or organizational membership is insufficient.

This is a closed ref union over admitted `U.Entity` values, not `U.PermissionBeneficiary`, `U.Authorization`, or another new U-kind. A materially different beneficiary meaning requires a separate direct-owner decision.

#### A.2.8.PER:4.3 - Record weak permission and non-violation as findings

```text
NonProhibitionFinding@Context <: U.Episteme
  beneficiaryRef: PermissionBeneficiaryRef
  permittedActionSpecificationRef: U.EpistemeRef
  normativeFrameRef: U.EpistemeRef
  frameCurrentnessResultRef: U.EpistemeRef
  frameCompletenessForUseResultRef: U.EpistemeRef
  boundedContextRef: U.BoundedContextRef
  scope: U.ClaimScope
  evaluationWindow: QualificationWindowPolicy
  checkedProhibitionRefs: set<ClaimIdRef>
  result: nonProhibited | unresolved
  evaluationWorkRef: WorkRef

NonViolationFinding@Context <: U.Episteme
  workRef: WorkRef
  performerAssignmentRefs: set<RoleAssignmentRef>
  onBehalfOfRelationOccurrenceRef?: U.EntityRef
  normativeFrameRef: U.EpistemeRef
  frameCurrentnessResultRef: U.EpistemeRef
  frameCompletenessForUseResultRef: U.EpistemeRef
  boundedContextRef: U.BoundedContextRef
  scope: U.ClaimScope
  evaluationWindow: QualificationWindowPolicy
  checkedProhibitionRefs: set<ClaimIdRef>
  result: nonViolating | unresolved
  evaluationWorkRef: WorkRef
```

`nonProhibited` and `nonViolating` are admissible only when the named frame is current and explicitly sufficiently complete for the intended use. Otherwise the finding is `unresolved`. Neither finding institutes permission, proves absence outside its frame, or becomes a world-side relation.

For `NonViolationFinding@Context`, recover the actual performer systems from the named Work and cite their exact covering `U.RoleAssignment` occurrences. If the checked norm instead turns on work done for a `PartyRef`, cite the already obtaining subject-owned on-behalf-of relation occurrence. These are direct case facts used by the evaluation, not a new `beneficiaryPerformanceBinding` episteme. Omit the on-behalf-of reference when no such branch is used.

#### A.2.8.PER:4.4 - Declare the strong granted-permission relation

```text
GrantedPermissionRelation@Context <: U.Relation

RelationSignature:
  PermissionBeneficiarySlot:
    SlotKind: PermissionBeneficiarySlot
    ValueKind: U.Entity
    refMode: PermissionBeneficiaryRef
  PermittedActionSpecificationSlot:
    SlotKind: PermittedActionSpecificationSlot
    ValueKind: U.Episteme
    refMode: U.EpistemeRef

semanticDirection: PermissionBeneficiarySlot -> PermittedActionSpecificationSlot

RelationOccurrenceGroundAndQualifiers:
  institutingSpeechActRef: SpeechActRef
  grantorAssignmentRef: RoleAssignmentRef
  grantValidityPolicyRef: U.EpistemeRef
  boundedContextRef: U.BoundedContextRef
  scope: U.ClaimScope
  validityWindow: QualificationWindowPolicy
  revocationOrSupersessionRef?: SpeechActRef
```

The beneficiary and permitted-action specification are participants. Grantor assignment, instituting act, policy, context, scope/window, and revocation are constructive ground or qualifiers, not collapsed participants.

The relation begins only when an admitted holder `U.System` performs a `U.SpeechAct` under the exact `grantorAssignmentRef`, the act satisfies the current policy's grant-validity predicate, and it institutes permission for the named participants. The assignment's `HolderSystemSlot` must resolve to that system: the system performs the act, while the assignment supplies its role and authority ground and never acts. The relation obtains while beneficiary applicability, policy continuation, scope, and window hold and no valid revocation or supersession ends it.

One occurrence is identified by the instituting speech-act occurrence, exact beneficiary ref and ref kind, action-specification edition, policy/context, and effective interval. Beneficiary change, renewal, materially changed action specification, non-carried policy edition, or revocation ends or splits the occurrence. A policy edition preserves it only through an explicit satisfied carry-forward rule.

#### A.2.8.PER:4.5 - Declare actual exercise

```text
PermissionExerciseRelation@Context <: U.Relation

RelationSignature:
  ExercisingWorkSlot:
    SlotKind: ExercisingWorkSlot
    ValueKind: U.Work
    refMode: WorkRef
  GrantedPermissionOccurrenceSlot:
    SlotKind: GrantedPermissionOccurrenceSlot
    ValueKind: U.Relation
    refMode: U.EntityRef
      // resolves to one GrantedPermissionRelation@Context occurrence

semanticDirection: ExercisingWorkSlot -> GrantedPermissionOccurrenceSlot

RelationOccurrenceQualifiers:
  beneficiaryAssignmentRef?: RoleAssignmentRef
  onBehalfOfRelationOccurrenceRef?: U.EntityRef
  exerciseScope: U.ClaimScope
  exerciseInterval: QualificationWindowPolicy
```

Decide exercise from two observable questions about the existing objects: **did this dated Work instantiate the grant's permitted-action specification, and did its actual performer satisfy the grant's beneficiary branch?** For a `RoleAssignmentRef` beneficiary, the grant's assignment must cover the Work and have that performer as its holder. For a `RoleRef`, `beneficiaryAssignmentRef` names the covering assignment that instantiates the role. For a `PartyRef`, the performer must be that party or `onBehalfOfRelationOccurrenceRef` must cite the already obtaining subject-owned relation licensed by the policy. If either question fails, this exercise relation does not obtain.

No `actionMatchFinding` or `beneficiaryEligibilityFinding` is required. The match and eligibility are direct obtaining predicates over the Work, grant, action specification, performer, and cited assignment or on-behalf-of relation. If a receiving assurance or audit use needs a separately recorded evaluation or evidence item, cite that item through its direct owner; do not mint a placeholder episteme merely to fill this relation.

The exercise relation obtains only when those two predicates hold, the grant obtains throughout the exercise interval, and the work remains in scope. The work is a satisfier of permitted action content. It does not satisfy or discharge an obligation and does not consume the grant unless the named policy explicitly makes it single-use or quota-bound.

Non-exercise leaves an obtaining grant unused and ordinarily still obtaining; it does not establish `NonViolationFinding@Context`. Exercise establishes only the exercise relation and likewise does not establish that finding without the separate checked-frame evaluation. Work outside the action specification, beneficiary binding, scope, or window does not exercise the grant; a separate prohibition, commitment, admissibility, or work owner decides any further consequence.

#### A.2.8.PER:4.6 - Expose conflict without inventing precedence

```text
PermissionConflictResolutionResultRef ::= U.EpistemeRef
  // resolves only to PermissionConflictResolutionResult@Context

PermissionConflictResolutionResult@Context <: U.Episteme
  conflictFindingRef: U.EpistemeRef
  governingPrecedencePolicyRef: U.EpistemeRef
  resolutionWorkRef: WorkRef
  deciderSystemRef: U.EntityRef
  deciderAssignmentRef: RoleAssignmentRef
  decisionAuthorityRelationOccurrenceRef: U.EntityRef
  selectedGrantOccurrenceRef?: U.EntityRef
  selectedNormClaimRef?: ClaimIdRef
  effectiveScope: U.ClaimScope
  effectiveWindow: QualificationWindowPolicy
  reopenConditionRef: ClaimIdRef

PermissionNormConflictFinding@Context <: U.Episteme
  grantedPermissionOccurrenceRef: U.EntityRef
  conflictingNormClaimRef: ClaimIdRef
  overlapScope: U.ClaimScope
  overlapWindow: QualificationWindowPolicy
  governingPrecedencePolicyRef: U.EpistemeRef
  applicablePrecedenceRuleRef?: ClaimIdRef
  decisionAuthorityRelationOccurrenceRef?: U.EntityRef
  resolutionWorkRef?: WorkRef
  resolutionResultRef?: PermissionConflictResolutionResultRef
  blockedWorkOrRelianceRef: U.EntityRef
  disposition: unresolved | settledByApplicableRule | settledByDecisionResult
  reopenConditionRef: ClaimIdRef
```

Create the finding only when the grant and current prohibition or commitment concern the same beneficiary/action content, overlapping scope/window, and incompatible practical conclusions. Check that match directly from the two claims and their participants; do not require a `beneficiaryAndActionMatchFinding` wrapper. Permission and an obligation to perform the same action are not automatically in conflict.

Resolve the conflict through exactly one of two branches:

1. **The current policy already decides.** `applicablePrecedenceRuleRef` cites the policy claim whose stated conditions match this beneficiary, action, scope, and window. Set `settledByApplicableRule` only when that rule itself selects which claim governs the blocked use.
2. **A decision is required.** Name the admitted `U.System` that decides, the covering assignment under which it performs the dated `resolutionWorkRef`, and the independently obtaining subject-owned authority relation that authorizes this decision. The direct result relation for that decision must connect the Work to a current `PermissionConflictResolutionResult@Context` selecting either the grant occurrence or the conflicting norm claim for the stated scope/window. The system decides; neither its assignment, authority relation, policy, nor organizational label performs the work.

`PermissionConflictResolutionResult@Context` is the exact decision result for this conflict, not a generic owner record. Exactly one of `selectedGrantOccurrenceRef` or `selectedNormClaimRef` is filled. Its `deciderAssignmentRef` must cover `resolutionWorkRef` and have `deciderSystemRef` as holder; `decisionAuthorityRelationOccurrenceRef` must independently authorize that decision. If no policy rule decides and no such current result exists, the disposition remains `unresolved`, even when a responsible office or role is named. Permit text, readiness, or a passing gate does not silently defeat the prohibition.

#### A.2.8.PER:4.7 - Keep the handshakes narrow

| Neighboring object | Exact handshake |
|---|---|
| Grant/revoke act | `A.2.9 U.SpeechAct <: U.Work`; an admitted holder `U.System` performs the act under the exact grantor assignment, and `institutes.permissions` cites the grant occurrence. The assignment is authority ground, not the actor; the act is not the enduring relation. |
| Permit episteme and carrier | `C.2.1`, `E.17`, `G.11`, and `A.10` may assert, publish, carry, or evidence the relation; readable form neither institutes nor equals it. |
| Duty or prohibition | `A.2.8 U.Commitment`; permission remains outside its modality family. |
| Boundary claim or entry predicate | `A.6.B` classifies the claim; an `A-*` predicate may consume a current permission result but does not create one. |
| Work plan and readiness | `A.15.2` owns the `U.WorkPlan`; `A.15.5` may cite a permission/conflict result as one readiness input. Neither creates permission. |
| Gate decision | `A.21` publishes a gate outcome. It neither creates permission nor resolves a permission conflict. |
| Work and result | `A.15.1` owns the dated work. Exercise requires the direct relation above; permission supplies no capability, readiness, safety, success, or result quality. |

