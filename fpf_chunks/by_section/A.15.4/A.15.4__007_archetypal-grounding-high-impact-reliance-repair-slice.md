---
chunk_kind: "child"
pattern_id: "A.15.4"
pattern_title: "Work-Relevant Appearance-Based Reliance Repair"
section_id: "A.15.4:3.2"
section_title: "Archetypal Grounding - High-Impact Reliance-Repair Slice"
source_path: "FPF-Spec.md"
output_path: "by_section/A.15.4/A.15.4__007_archetypal-grounding-high-impact-reliance-repair-slice.md"
commit_sha: "11f2345e65e4b2ec5b84c0cecde4c9485834d28d"
heading_path:
  - "A.15.4 — Work-Relevant Appearance-Based Reliance Repair"
  - "A.15.4:3.2 — Archetypal Grounding - High-Impact Reliance-Repair Slice"
line_start: 26086
line_end: 26181
dependencies:
  - "A.10"
  - "A.15"
  - "A.15.1"
  - "A.15.5"
  - "A.16.0"
  - "A.2.1"
  - "A.2.5"
  - "A.2.8"
  - "A.2.8.PER"
  - "A.2.9"
  - "A.20"
  - "A.21"
  - "A.6"
  - "A.6.B"
  - "A.6.C"
  - "B.3"
  - "C.2.1"
  - "E.10"
  - "E.10.MOVE"
  - "E.17"
  - "E.17.EFP"
  - "F.6"
keywords:
  - "allowed or blocked use"
  - "appearance-based reliance"
  - "copied approval"
  - "credential"
  - "dashboard"
  - "exact attempted use"
  - "generated explanation"
  - "governing pattern and direct object"
  - "independent required-position rows"
  - "orientation and source-finding"
  - "project-side reference"
  - "publication face"
---

### A.15.4:3.2 - Archetypal Grounding - High-Impact Reliance-Repair Slice

A lab manager sees a green tile for `CRISPR-guide-G42 ready` and a copied message saying the edit is approved. `A.15.4` does not ask the manager to decide whether the tile is a good UI. It asks what work or reliance claim is about to be made.

```text
A.15.4 local repair record:
  RelianceAppearanceRef: B17-G42-GreenTile plus B17-CopiedApprovalMessage
  RelianceAppearanceKind: dashboard display plus copied wording
  WorkOrRelianceUseKind: intended work
  WorkOrRelianceUseRef: B17-GeneEditIntervention
  RequiredPositionEntries:
    - EntryId: B17-PROTOCOL
      SubjectPatternLocator: E.24.PUB
      DirectObjectKind: EpistemePublicationRelation
      ProjectSideObjectRef: B17-ProtocolPublication-e5
      RequiredPostureOrCurrentness: obtains; protocol edition e5 is currently available to the B-17 lab audience for this intervention use
      DependencyOnAttemptedUse: the intended Work must use the applicable protocol edition
    - EntryId: B17-GRANT-ACT
      SubjectPatternLocator: A.2.9
      DirectObjectKind: U.SpeechAct occurrence
      ProjectSideObjectRef: B17-GrantSpeechAct
      RequiredPostureOrCurrentness: actual dated Work performed by an admitted system under the exact grantor assignment and recognized by the current grant policy
      DependencyOnAttemptedUse: grounds B17-InterventionGrant; the act itself is not permission
    - EntryId: B17-GRANT
      SubjectPatternLocator: A.2.8.PER
      DirectObjectKind: GrantedPermissionRelation@Context occurrence
      ProjectSideObjectRef: B17-InterventionGrant
      RequiredPostureOrCurrentness: obtains and is current for the exact beneficiary, intervention action, sample batch, scope, and window, with no valid revocation or supersession ending the grant
      DependencyOnAttemptedUse: the intervention requires this strong grant
    - EntryId: B17-CONFLICT
      SubjectPatternLocator: A.2.8.PER
      DirectObjectKind: PermissionNormConflictFinding@Context
      ProjectSideObjectRef: B17-InterventionPermissionNormConflictFinding
      RequiredPostureOrCurrentness: current disposition=settledByApplicableRule; B17-ConflictPrecedenceRule-e2 matches this beneficiary, intervention action, sample batch, scope, and window and selects the grant for this attempted intervention
      DependencyOnAttemptedUse: an unresolved or norm-selecting disposition blocks AllowedUseNow for this intervention; the finding neither revokes nor ends B17-InterventionGrant
    - EntryId: B17-CONFLICT-EVIDENCE
      SubjectPatternLocator: A.10
      DirectObjectKind: claim-bound evidence-provenance relation
      ProjectSideObjectRef: B17-ConflictFindingEvidence
      RequiredPostureOrCurrentness: supports only the current B17-InterventionPermissionNormConflictFinding disposition and the applicability of B17-ConflictPrecedenceRule-e2 to this exact attempted use
      DependencyOnAttemptedUse: supplies the evidence/currentness path for B17-CONFLICT without becoming the finding, rule, or grant
    - EntryId: B17-GATE
      SubjectPatternLocator: A.21
      DirectObjectKind: GateDecision
      ProjectSideObjectRef: B17-InterventionGateDecision-e2
      RequiredPostureOrCurrentness: current GateDecision=pass under the applicable GateProfile and DecisionLog
      DependencyOnAttemptedUse: the current lab policy separately requires gate passage; this decision does not create the grant
    - EntryId: B17-WORK-ENTRY
      SubjectPatternLocator: A.15.5
      DirectObjectKind: WorkEntryReadiness@Context relation
      ProjectSideObjectRef: B17-WorkEntryReadiness-e3
      RequiredPostureOrCurrentness: current relation for the exact B17-GeneEditIntervention, performer, kit, context, and entry window, with CommitmentDisposition=readyForCommitment and no triggered StopCondition
      DependencyOnAttemptedUse: the current lab policy separately requires work-entry readiness; readiness does not create the grant or gate decision
    - EntryId: B17-ASSIGNMENT
      SubjectPatternLocator: A.2.1
      DirectObjectKind: B17EditorSystemRoleAssignment, a direct species of U.SystemRoleAssignment
      ProjectSideObjectRef: B17-EditorAssignment
      RequiredPostureOrCurrentness: obtains, names the intended performer as holder, and covers the proposed Work window
      DependencyOnAttemptedUse: identifies the intended performer and the assignment context required by the beneficiary branch and F.6 attribution; it establishes neither capability, permission, authority, responsibility, nor Work
    - EntryId: B17-PROTOCOL-EVIDENCE
      SubjectPatternLocator: A.10
      DirectObjectKind: claim-bound evidence-provenance relation
      ProjectSideObjectRef: B17-ProtocolPublicationEvidence
      RequiredPostureOrCurrentness: supports only the claim that B17-ProtocolPublication-e5 obtains and exposes protocol edition e5 for this lab audience and intervention use throughout the decision window
      DependencyOnAttemptedUse: supplies the publication/currentness evidence required for B17-PROTOCOL without standing in for that publication relation
    - EntryId: B17-GRANT-EVIDENCE
      SubjectPatternLocator: A.10
      DirectObjectKind: claim-bound evidence-provenance relation
      ProjectSideObjectRef: B17-InterventionGrantEvidence
      RequiredPostureOrCurrentness: supports only the claim that B17-InterventionGrant obtains and is current for this beneficiary, action, batch, scope, and window, including the instituting act, policy, revocation, and supersession sources used by that claim
      DependencyOnAttemptedUse: supplies the evidence/currentness path required for B17-GRANT without creating or replacing the grant
    - EntryId: B17-GATE-EVIDENCE
      SubjectPatternLocator: A.10
      DirectObjectKind: claim-bound evidence-provenance relation
      ProjectSideObjectRef: B17-InterventionGateEvidence
      RequiredPostureOrCurrentness: supports only the claim that B17-InterventionGateDecision-e2 is the current GateDecision=pass for this attempted use under its GateProfile and DecisionLog
      DependencyOnAttemptedUse: supplies the evidence/currentness path required for B17-GATE without becoming gate passage
    - EntryId: B17-ASSIGNMENT-EVIDENCE
      SubjectPatternLocator: A.10
      DirectObjectKind: claim-bound evidence-provenance relation
      ProjectSideObjectRef: B17-EditorAssignmentEvidence
      RequiredPostureOrCurrentness: supports only the claim that B17-EditorAssignment obtains, has the intended performer as holder, and covers the proposed Work window
      DependencyOnAttemptedUse: supplies the evidence/currentness path required for B17-ASSIGNMENT without creating or extending the assignment
    - EntryId: B17-PLAN
      SubjectPatternLocator: A.15.2
      DirectObjectKind: U.WorkPlan
      ProjectSideObjectRef: B17-GeneEditWorkPlan-e4
      RequiredPostureOrCurrentness: current plan for the intended performer, intervention, sample batch, method, resources, and window; not actual Work or permission
      DependencyOnAttemptedUse: describes the Work that would be entered if every other prerequisite passes
  AllowedUseNow: source-finding and prerequisite refresh only; do not intervene while any entry is absent or fails its required posture or currentness
  AppearanceOverreadBlocked: tile color and copied message do not authorize biological work or prove safety
  RecoveryOrStopCondition: before intervention, follow every typed ref; reopen only when every listed relation obtains or result passes its stated criterion, is current for this beneficiary, action, sample batch, scope, and window, and has its required evidence or source relation; B17-CONFLICT must have a current grant-selecting disposition, the gate must say pass, and work-entry readiness must say readyForCommitment
```

**Named-but-revoked grant near-miss.** Suppose `B17-InterventionGrant` and its complete-looking record are present, but policy-valid `B17-GrantRevocation` took effect before the intervention window. The `B17-GRANT` entry then fails `RequiredPostureOrCurrentness` because the grant no longer obtains. A current protocol, plan, `GateDecision=pass`, readiness result, and green tile do not repair that failure: `AllowedUseNow` remains source-finding and prerequisite repair, and the intervention stays blocked.

