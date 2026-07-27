---
chunk_kind: "child"
pattern_id: "F.8"
pattern_title: "Mint-or-Reuse Decision"
section_id: "F.8:7"
section_title: "Archetypal Grounding - worked cases"
source_path: "FPF-Spec.md"
output_path: "by_section/F.8/F.8__009_archetypal-grounding-worked-cases.md"
commit_sha: "60caecb4751fb2a3623a1faaca757d29a19acff9"
heading_path:
  - "F.8 — Mint-or-Reuse Decision"
  - "F.8:7 — Archetypal Grounding - worked cases"
line_start: 89384
line_end: 89445
dependencies:
  - "A.11"
  - "A.15"
  - "A.15.1"
  - "A.2"
  - "A.2.1"
  - "A.2.5"
  - "A.2.7"
  - "A.6.5"
  - "A.7"
  - "A.8"
  - "C.3"
  - "E.10"
  - "E.10.ARCH"
  - "E.24.CD"
  - "E.24.PUB"
  - "E.24.UK"
  - "E.9"
  - "F.1"
  - "F.10"
  - "F.13"
  - "F.14"
  - "F.15"
  - "F.17"
  - "F.18"
  - "F.2"
  - "F.3"
  - "F.4"
  - "F.5"
  - "F.6"
  - "F.7"
  - "F.9"
keywords:
  - "decision lattice"
  - "minting new U-kinds"
  - "parsimony"
  - "reuse"
  - "type explosion"
---

### F.8:7 - Archetypal Grounding - worked cases

#### F.8:7.1 - Reviewer Role vs Review Report

The expression `ReviewerRole` in `PatternReview_2026` names a work-facing role value. F.8 admits `nameRoleDescription`: use `F.4` for the role-description episteme and `F.5` or `F.18` for the label.

The expression "review report has reviewer role" is different. The report is an episteme. It may be used as evidence or source for an adequacy claim about the reviewed pattern; it does not hold the work-facing role. F.8 does not mint a role name for the report. The evidence-use, source-use, or publication-use claim remains governed by its direct pattern.

#### F.8:7.2 - Actor Across BPMN and PROV

A manager wants one word, "actor", for BPMN participant and PROV agent in a diagram. F.8 asks for the intended use. If the Bridge Card and Concept-Set row admit only naming use, the result is `reuseConceptSetRow` for prose and diagram labels only.

No role assignment follows. If the project subsequently needs a work-facing role in one context, it creates or reuses the local role-description episteme for that context.

#### F.8:7.3 - Access Role

An access-control source says `ApproverRole`. In that source, the expression may name a permission grouping. F.8 first recovers the access or policy relation. Only if the project also defines a work-facing `U.Role` for approval work in a bounded context does a RoleDescription label become current.

Otherwise the durable name, if needed, belongs to the access, policy, status, or gate pattern, not to role ontology.

#### F.8:7.4 - Policy Id

A gate profile introduces `Aut-Guard-2026`. F.8 treats this as a policy-id decision. Reuse requires a resolvable `PolicySpecRef`. New introduction also needs a `MintDecisionRef` or equivalent accepted decision record.

The policy id is not a role, method, gate result, evidence value, or source authority by itself. It is a reference to a policy specification used by the pattern that governs the policy claim.

#### F.8:7.5 - New U-kind Candidate

A team proposes `U.InfluenceEdge` because many documents use "influence". F.8 blocks immediate minting. The team must show the candidate is not an existing relation, causal claim, evidence relation, characteristic, method relation, bridge relation, structural name, publication form, or local frame under current patterns. If it is still cross-family, irreducible, and needed by several domain families, the proposal goes to `E.24.UK`, `A.8`, `A.11`, `C.3`, `E.9`, and `F.18`.

#### F.8:7.6 - Filled Decision Records

```text
MintReuseDecision:
  CandidateExpressionSlot: ReviewerRole
  BoundedContextSlot: PatternReview_2026
  RecoveredKindOrRelationSlot: U.Role described by one RoleDescription episteme
  LocalSenseRefSlot: review-work role in PatternReview_2026
  ProposedUseSlot: durable local RoleDescription label
  ReuseCandidateRefSlot: no existing local role-description label fits
  DecisionKindSlot: nameRoleDescription
  DirectPatternRefs: F.4, F.5; F.18 if public reuse becomes current
  NameDisciplineRefs: role label must not encode assignment, capability, method, work, evidence, or status
  NonAdmissibleOverreadSlot: this decision does not assign Alice, show that review work occurred, or make a review report evidence
  ReopenConditionSlot: reopen if the label is used for evidence, status, access, source, publication, or cross-context row claims
```

```text
MintReuseDecision:
  CandidateExpressionSlot: EvidenceRole
  BoundedContextSlot: PatternReview_2026
  RecoveredKindOrRelationSlot: evidence-use relation around a review-report episteme
  LocalSenseRefSlot: review report used as evidence for an adequacy claim about the reviewed pattern
  ProposedUseSlot: durable name requested for repeated evidence-use wording
  ReuseCandidateRefSlot: no U.Role candidate, because the episteme is not a role holder
  DecisionKindSlot: nameDirectPatternValue or blockOrLowerUse
  DirectPatternRefs: A.10, B.3, G.6, or direct evidence-use pattern
  NameDisciplineRefs: F.5 or F.18 only after the evidence-use relation is recovered
  NonAdmissibleOverreadSlot: do not mint EvidenceRole as RoleDescription or U.Role
  ReopenConditionSlot: reopen if the evidence-use relation changes target claim, polarity, provenance, assurance use, or validity window
```

