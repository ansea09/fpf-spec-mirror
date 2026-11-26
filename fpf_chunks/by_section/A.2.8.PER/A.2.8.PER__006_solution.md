---
chunk_kind: "child"
pattern_id: "A.2.8.PER"
pattern_title: "Granted Permission, Exercise, and Non-Prohibition"
section_id: "A.2.8.PER:4"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/A.2.8.PER/A.2.8.PER__006_solution.md"
commit_sha: "9d38fbfe4ce5b72d8fe05e839cbca0025a5b31cf"
heading_path:
  - "A.2.8.PER — Granted Permission, Exercise, and Non-Prohibition"
  - "A.2.8.PER:4 — Solution"
line_start: 8888
line_end: 9094
dependencies:
  - "A.10"
  - "A.13"
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

Use the object warranted by the current claim:

- `NonProhibitionFinding@Context` is a frame-relative episteme returned before action when a sufficiently complete current normative frame contains no applicable prohibition.
- `GrantedPermissionRelation@Context` is an enduring strong permission instituted by the act or combination of acts an exact policy requires. An entitlement conferred directly by a standing rule can be established from that rule and the case facts without a claim about a separate grant.
- `PermissionExerciseRelation@Context` connects actual dated work to one obtaining grant occurrence when action and beneficiary eligibility match.
- `NonViolationFinding@Context` is a frame-relative episteme about actual work that instantiates no applicable prohibition in the checked frame.
- `PermissionNormConflictFinding@Context` is an episteme exposing an incompatible current grant and prohibition or commitment over matching content, scope, and window.

For an entitlement conferred directly by a standing rule, establish the applicable rule and the case facts. If the question concerns exercise, check who acted and whether the actual action met its conditions. When another applicable norm gives an incompatible answer, apply the governing precedence rule or an authorized resolution. Where neither settles the conflict, the answer for that use remains open. The grant-specific declarations below concern a permission instituted by an act. A finding of non-prohibition does not institute a grant. A grant alone leaves its exercise open. To establish a violation, identify the norm the action breached.

#### A.2.8.PER:4.2 - Use the closed beneficiary reference family

```text
PermissionBeneficiaryRef ::=
  exactly one branch is present:
    beneficiarySystemRoleKindRef?: U.KindRef resolving to one exact local system-role kind
    beneficiarySystemRoleAssignmentRef?: U.RelationRef constrained to U.SystemRoleAssignment
    beneficiaryPartyRef?: PartyRef
```

The entity designated by the grant is its beneficiary. Apply the exercise-eligibility test for its reference branch:

- `beneficiarySystemRoleAssignmentRef` names one assignment occurrence and its declared species and applies only to that occurrence.
- `beneficiarySystemRoleKindRef` names one exact local system-role kind; the policy states which current assignments to that kind make an actual performer eligible.
- `PartyRef` covers work only when its exact performer or on-behalf-of relation satisfies the policy. Shared naming or organizational membership is insufficient.

This closed reference union describes one beneficiary. An instrument can instead grant one right to several named parties jointly. Apply its conditions to the named parties and to the action required of them together. Use a common `PartyRef` when the instrument designates that party. Naming several parties in one instrument does not by itself entitle each to act alone. The applicable subject pattern governs a beneficiary meaning outside this union.

#### A.2.8.PER:4.3 - Record weak permission and non-violation as findings

```text
NonProhibitionFinding@Context <: U.Episteme
  beneficiaryRef: PermissionBeneficiaryRef
  permittedActionSpecificationRef: U.EpistemeRef
  normativeFrameRef: U.EpistemeRef
  frameCurrentnessResultRef: U.EpistemeRef
  frameCompletenessForUseResultRef: U.EpistemeRef
  scope: U.ClaimScope
  intendedUse:
  evaluationWindow: QualificationWindowPolicy
  checkedProhibitionAddresses: set<ClaimAddress>
  result: nonProhibited | unresolved
  evaluationWorkRef?: WorkRef             # when the account asserts this dated evaluation Work

NonViolationFinding@Context <: U.Episteme
  workRef: WorkRef
  performerSystemRoleAssignmentRefs?: set<U.RelationRef constrained to U.SystemRoleAssignment> # when the checked norm uses precise assignment attribution
  onBehalfOfRelationOccurrenceRef?: U.RelationRef constrained to the direct on-behalf-of relation kind # one mandate covering the relevant contribution
  representedContributions?: contributing performers, each linked to its part, the party represented and its applicable on-behalf-of relation(s)
  normativeFrameRef: U.EpistemeRef
  frameCurrentnessResultRef: U.EpistemeRef
  frameCompletenessForUseResultRef: U.EpistemeRef
  scope: U.ClaimScope
  intendedUse:
  evaluationWindow: QualificationWindowPolicy
  checkedProhibitionAddresses: set<ClaimAddress>
  result: nonViolating | unresolved
  evaluationWorkRef?: WorkRef             # when the account asserts this dated evaluation Work
```

`nonProhibited` and `nonViolating` are admissible only when the named frame is current and explicitly sufficiently complete for the intended use. Otherwise the finding is `unresolved`. Neither finding institutes permission or proves absence outside its frame.

Every `ClaimAddress` in this pattern means the reusable `C.2.1 ClaimAddress`: an exact episteme-edition reference plus an intrinsic claim identity declared by that edition's ClaimGraph. A heading, row number, file location, or printed token is insufficient.

For a `NonViolationFinding@Context`, use the facts on which the checked prohibition turns. If it concerns representation, link each relevant contribution to the performer, the party represented and the independently established mandate covering that part. One on-behalf-of relation suffices when it covers the claim. A performer can act for different parties under different mandates. Cite a covering assignment and its declared species where the norm requires assignment-bound attribution. If only the conduct or resulting state matters, the evidence can establish that fact without identifying a representative. The Work under examination and the currentness and sufficient completeness of the frame still need grounds. Identify a separate evaluation Work when its occurrence is also asserted.

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
  // Use the direct fields for one act under one granting assignment, or the grouped form.
  ( institutingSpeechActRef: SpeechActRef,
    grantorSystemRoleAssignmentRef: U.RelationRef constrained to U.SystemRoleAssignment
  | institutingActs: non-empty set of SpeechActRef, each with its granting contributions under A.2.9:4.1–4.5 )
  grantValidityPolicyRef: U.EpistemeRef
  scope: U.ClaimScope
  validityWindow: QualificationWindowPolicy
  revocationOrSupersessionRef?: SpeechActRef       // one act sufficient under the policy
  revocationOrSupersessionActs?: set<SpeechActRef>  // acts required together, when applicable
```

The beneficiary and permitted-action specification are participants. The instituting acts, granting capacities and authority, policy, ClaimScope, validity window and any effective revocation supply grounds or qualifiers.

Apply the current grant-validity rule to the actual communication. If one delegate can grant permission, establish the act and the mandate covering the delegated decision. If several participants issue one declaration, recover their joint performance under A.2.9. If distinct approvals are required together, identify each act and establish that their contents, order where material, scopes and times meet the same rule. Keep each required granting assignment and its holder with that holder’s act, including several assignments of one holder when relied on. Establish the authority each contribution needs. A record that merely transmits the decisions can supply evidence about them. Its sender is a grantor only if the rule gives that sender an effective granting contribution.

The relation obtains while beneficiary applicability, policy continuation, scope, and window hold and no valid revocation or supersession ends it.

Identify an occurrence from its policy-required instituting act or combination, exact beneficiary reference and reference kind, action-specification edition, policy edition, ClaimScope and effective interval. Use one act reference for a joint act even if several performers took part. The permission starts when all conditions for its effectiveness hold. Beneficiary change, renewal, materially changed action specification, a non-carried policy edition or effective revocation ends or splits the occurrence. A policy edition preserves it through an explicit satisfied carry-forward rule. Apply the policy's own conditions for revocation, including any required combination of acts.

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
    refMode: U.RelationRef constrained to GrantedPermissionRelation@Context
      // resolves to one exact obtaining grant occurrence

semanticDirection: ExercisingWorkSlot -> GrantedPermissionOccurrenceSlot

RelationOccurrenceQualifiers:
  // For a single exercising contribution, use its applicable direct reference.
  beneficiarySystemRoleAssignmentRef?: U.RelationRef constrained to U.SystemRoleAssignment
  onBehalfOfRelationOccurrenceRef?: U.RelationRef constrained to the direct on-behalf-of relation kind
  exercisingContributions?: qualifying performers, each with its part in the permitted action and the eligibility grounds the policy requires
  exerciseScope: U.ClaimScope
  exerciseInterval: QualificationWindowPolicy
```

Decide exercise from two questions. Did this dated Work instantiate the permitted action? Did the contribution or combination that counts as exercising the permission meet its beneficiary conditions?

For a `beneficiarySystemRoleAssignmentRef` grant, establish that the named assignment covers the relevant contribution and that its holder performed it. For a `beneficiarySystemRoleKindRef` grant, establish the eligible assignment to that kind for each contribution that the rule requires. For a `beneficiaryPartyRef` grant, establish action by the party or the policy-recognized on-behalf-of relation for its representative. Use the direct references for a single contribution. For joint exercise, group each exercising contribution with its performer, action and qualifying capacity. A contributor providing technical support can enable the exercise without needing the entitlement to exercise the right personally.

Test the action and beneficiary predicates over this Work, grant, action specification and the relevant performers and capacities. If either predicate fails, the exercise relation does not obtain. Cite a separate evaluation or evidence item when an assurance use requires it.

If an action requires several distinct grants, check coverage under each and the rule requiring them together. Each exercise relation still refers to one grant. The exercise relation obtains only when those two predicates hold, the grant obtains throughout the exercise interval, and the work remains in scope. The work is a satisfier of permitted action content. Judge any obligation-satisfaction or discharge claim under the separate evaluation or compliance rule (A.2.8:4.6). The work consumes the grant only when the named policy explicitly makes it single-use or quota-bound.

Non-exercise leaves a grant unused; it continues while the §4.4 conditions hold. Neither non-exercise nor exercise establishes `NonViolationFinding@Context` without the separate checked-frame evaluation. Work outside the action specification, beneficiary eligibility, scope or window does not exercise the grant; any further consequence follows from the applicable prohibition, commitment, admissibility or Work-related predicate.

When a decision is required, identify its result and use the relevant decision rule; an asserted dated decision Work follows the performer-and-Work route above and any assignment or authority conditions required by that rule.

#### A.2.8.PER:4.6 - Expose conflict without inventing precedence

```text
PermissionConflictResolutionResultRef ::= U.EpistemeRef
  // resolves only to PermissionConflictResolutionResult@Context

PermissionConflictResolutionResult@Context <: U.Episteme
  conflictFindingRef: U.EpistemeRef
  governingPrecedencePolicyRef: U.EpistemeRef
  // Direct fields for one decision by one authorized holder, or the grouped form.
  ( resolutionWorkRef: WorkRef,
    deciderSystemRef: U.EntityRef,
    deciderSystemRoleAssignmentRef: U.RelationRef constrained to U.SystemRoleAssignment,
    decisionAuthorityRelationOccurrenceRef: U.RelationRef constrained to the direct decision-authority relation kind
  | resolutionContributions: decision Work occurrences, each with its deciding performers, relied-on assignments and authority relations as required by the policy )
  selectedGrantOccurrenceRef?: U.RelationRef constrained to GrantedPermissionRelation@Context
  selectedNormClaimAddress?: ClaimAddress
  effectiveScope: U.ClaimScope
  effectiveWindow: QualificationWindowPolicy
  reopenConditionClaimAddress: ClaimAddress

PermissionNormConflictFinding@Context <: U.Episteme
  grantedPermissionOccurrenceRef: U.RelationRef constrained to GrantedPermissionRelation@Context
  conflictingNormClaimAddress: ClaimAddress
  overlapScope: U.ClaimScope
  overlapWindow: QualificationWindowPolicy
  governingPrecedencePolicyRef?: U.EpistemeRef
  applicablePrecedenceRuleAddress?: ClaimAddress
  decisionAuthorityRelationOccurrenceRef?: U.RelationRef constrained to the direct decision-authority relation kind
  resolutionWorkRef?: WorkRef   // optional single decision detail; the resolution result carries any joint basis
  resolutionResultRef?: PermissionConflictResolutionResultRef
  blockedWorkOrRelianceRef: U.EntityRef
  disposition: unresolved | settledByApplicableRule | settledByDecisionResult
  reopenConditionClaimAddress: ClaimAddress
```

Create the finding only when the grant and current prohibition or commitment concern the same beneficiary/action content, overlapping scope/window, and incompatible practical conclusions. Check that match directly from the two claims and their participants. Permission and an obligation to perform the same action are not automatically in conflict.

An unresolved finding may omit `governingPrecedencePolicyRef` when no governing precedence policy has been identified. Keep the disposition unresolved and retain the missing input and what would reopen the question. A settled finding identifies the governing policy and the applicable rule or independently grounded decision result. For a proposed action, `blockedWorkOrRelianceRef` identifies the action or its WorkPlan under the applicable subject rule; it does not designate a future Work occurrence.

Resolve the conflict through exactly one of two branches:

1. **The current policy already decides.** `applicablePrecedenceRuleAddress` cites the policy claim whose stated conditions match this beneficiary, action, scope, and window. Set `settledByApplicableRule` only when that rule itself selects which claim governs the blocked use.
2. **A decision is required.** Recover the decision or combination that the policy empowers to settle this conflict. Establish the deciding participants, their actual decision Work, and the capacities and mandates needed for each contribution. One authorised body may make one decision. Where distinct approvals are jointly required, establish each and their combination on the disputed use. The grounded result of the required Work must select the grant or the conflicting norm for the stated scope and window.

`PermissionConflictResolutionResult@Context` records that decision result. Exactly one of `selectedGrantOccurrenceRef` or `selectedNormClaimAddress` is filled. In the direct form, the named assignment must cover the decision Work and have the deciding system as holder. Establish the authority to make that decision independently. In the grouped form, associate each contribution with its actual Work and authority. Check that all the policy’s decision conditions obtain before using the combined result.

If no policy rule decides and no such current result exists, the disposition remains `unresolved`, even when a responsible office or system-role kind is named. Permit text, readiness, or a passing gate does not defeat the prohibition.

#### A.2.8.PER:4.7 - Keep the handshakes narrow

| Neighboring object | Handshake |
|---|---|
| Grant or revoke act | Use A.2.9 for each actual communicative Work and any assignment-bound attribution. A grant can require one declaration by several participants or several distinct approvals. Cite the separately obtaining grant in the applicable `institutes.permissions` entry when the rule-required combination is complete. Establish revocation from its own policy conditions. |
| Permit episteme and carrier | Use `C.2.1` for claims about the permission, `E.17` for a source-backed publication face, `G.11` for source currentness and publication refresh, and `A.10` for evidence used in reliance. Use `E.24.PUB` when the publication occurrence, form, or carrier identity matters. |
| Duty or prohibition | `A.2.8 U.Commitment`; permission remains outside its modality family. |
| Boundary claim or entry predicate | `A.6.B` classifies the claim; an `A-*` predicate may consume a separately established current permission result. |
| Work plan and readiness | `A.15.2` is the pattern for the `U.WorkPlan`; `A.15.5` may cite a separately established permission/conflict result as one readiness input. |
| Gate decision | Use `A.21` for a gate outcome, citing the separate current grant or conflict result whenever its profile requires one. |
| Work and result | Identify the dated Work under `A.15.1`. For an entitlement under a standing rule, establish who qualifies and whether the action met the rule. For a right conferred by an instrument, apply its scope, interval and conditions to what the named beneficiary or joint beneficiaries did. Use the §4.5 exercise relation for a grant represented under §4.4. Capability, readiness, safety, success and result quality require their own grounds. |

