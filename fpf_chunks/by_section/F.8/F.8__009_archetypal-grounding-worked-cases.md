---
chunk_kind: "child"
pattern_id: "F.8"
pattern_title: "Mint-or-Reuse Decision"
section_id: "F.8:7"
section_title: "Archetypal Grounding - worked cases"
source_path: "FPF-Spec.md"
output_path: "by_section/F.8/F.8__009_archetypal-grounding-worked-cases.md"
commit_sha: "1602a8d0a6934a99a79ead914610b070cedd86d2"
heading_path:
  - "F.8 — Mint-or-Reuse Decision"
  - "F.8:7 — Archetypal Grounding - worked cases"
line_start: 92313
line_end: 92393
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
  - "C.2.1"
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

The source label `PatternReview_2026` is not a context object. Classify the actual claim before using it:

- `ReviewWork-82` can be one dated `U.Work` occurrence under `A.15.1`;
- `ReviewPlan-2026-v3` can be a separately constituted plan episteme or edition under its direct owner;
- `PatternReviewReferenceScheme-2026` can be an effective by-value `U.ReferenceScheme` for interpreting review terminology; and
- "used while deciding the label for the 2026 review method" can be claim content describing the decision-use setting without minting any context entity.

If the independently governed `ReviewerRole` value is work-facing, F.8 may return `nameRoleDescription`: use `F.4` for the RoleDescription episteme and `F.5` or `F.18` for the label when its durability is current. The review label does not create that role, assign a reviewer, or demonstrate review Work.

The expression "review report has reviewer role" is a different case. `ReviewReport-82` is an episteme. A direct evidence, source, or publication relation may later use it for an adequacy claim about a reviewed pattern; the report does not hold the work-facing role, and its title does not make any evidence use or publication authority obtain.

#### F.8:7.2 - Actor Across BPMN and PROV

A manager wants one word, "actor", for a BPMN participant and a PROV agent in a diagram. First recover the two exact local senses under their effective ReferenceSchemes. If an actual F.9 Bridge relates the exact cells and one F.17 row admits naming-only use, F.8 returns `reuseAdmittedTermRow` for prose and diagram labels only.

No governed-value identity, substitution, role assignment, or Work follows. If the project later needs a work-facing role under one scheme, it creates or reuses the local RoleDescription episteme for that independently recovered role value.

#### F.8:7.3 - Access Role

An access-control source says `ApproverRole`. Under the source's effective naming ReferenceScheme, the expression may designate a permission grouping or exact policy relation. F.8 first returns to the access, policy, status, or deontic owner. Only if `A.2` independently governs a work-facing approval role does a RoleDescription naming decision become current.

Otherwise the durable designation, if needed, belongs to the direct access, policy, status, or gate pattern. The `Role` suffix, a source card, or a selected model-use Structure creates no work-facing role or assignment.

#### F.8:7.4 - Policy Identifier

A gate profile proposes `Aut-Guard-2026`. F.8 treats this as a policy-identifier question only after an exact policy specification is independently recoverable. Reuse resolves the existing identifier, its separate specification, and the original mint decision. New introduction identifies a new mint decision occurrence and, when durable trace is needed, its separate result episteme or record.

The identifier is not the specification, role, method, gate result, evidence value, permission, or source authority. It is a reference used by the pattern that governs the exact policy claim.

#### F.8:7.5 - New U-kind Candidate

A team proposes `U.InfluenceEdge` because many documents use "influence". F.8 blocks immediate minting. The team must show that the candidate is not an existing relation, causal claim, evidence relation, characteristic, method relation, Bridge relation, structural name, publication form, or local frame under current patterns. If it remains cross-family, irreducible, and needed by several domain families, the proposal goes to `E.24.UK`, `A.8`, `A.11`, `C.3`, `E.9`, and `F.18`. F.8 neither creates nor admits the kind.

#### F.8:7.6 - Filled Decision Result and Explicit Pre-F.8 Stop

The first projection records a result about a separately identified naming decision. `PatternReviewReferenceScheme-2026` is the effective naming scheme; the actual review Work, any review plan, and this decision-use setting remain separate.

```text
MintReuseDecisionResultEpisteme:
  DecisionResultEpistemeId: MRD-ReviewerRole-2026-v1
  EntityOfConcernRef: ReviewerRoleNamingDecision-2026-07-31
  CandidateExpression: ReviewerRole
  GovernedValueOrRelationRef: ReviewerRoleValue
  GovernedKindOrRelationKindRef: U.Role
  DirectGoverningPatternRef: A.2
  ProposedNamingUse: durable local label for the RoleDescription episteme used by the review method
  EffectiveNamingReferenceScheme: PatternReviewReferenceScheme-2026
  LocalSenseClaim: work-facing role whose holder may perform exact pattern-review Work under a separately governed assignment
  LocalSenseCellRef: omitted; no receiving use needs a stable cell address yet
  LocalSenseBasisRelationRef: omitted; the direct local-sense claim and A.2/F.4 basis are sufficient at this gate
  SelectedModelUseStructureRef: omitted; no independently selected Structure changes this naming use
  ReuseCandidateRefs: no existing designation or alias supports the exact proposed use
  SelectedDisposition: nameRoleDescription
  ResultingNamingRefs: F.4 RoleDescription authoring next; F.18 only if durable reuse remains current
  NonAdmissibleOverread: the decision and its result episteme do not assign Alice, show that review Work occurred, make a review report evidence, or publish the label
  ReopenCondition: reopen if the expression is used for evidence, status, access, source, publication, or cross-local row claims
```

The second case does not enter F.8. The proposed `EvidenceRole` wording has exposed an evidence-use question, but no exact governed relation, relation kind, or single direct owner has yet been recovered. The review label again supplies no context, evidence, or authority.

```text
PreF8RecoveryStop:
  CandidateExpression: EvidenceRole
  KnownSubject: ReviewReport-82 : U.Episteme
  ProposedNamingUse: reusable wording for one exact evidence-use relation
  EffectiveNamingReferenceScheme: PatternReviewReferenceScheme-2026
  RecoveredFact: ReviewReport-82 is proposed for evidence use concerning an adequacy claim; it is not a role holder
  MissingEntryFacts: the exact target claim and polarity; the exact evidence-use relation and relation kind; provenance, assurance or reliance use, and validity window when current; one direct governing pattern
  RequiredDirectOwnerAction: recover those facts under the single pattern that directly governs the exact evidence-use claim
  LocalSenseState: no stable cell address or independently current LocalSenseBasisRelation is needed for this blocked role reading
  SelectedModelUseStructureState: none; no independently selected Structure changes this use
  DirectTerminologyProbe: test the eventual direct evidence-pattern terminology only after recovery
  StopResult: do not enter F.8 and do not mint EvidenceRole; keep the expression local until the governed relation, exact kind, one direct pattern, and proposed naming use are present
  NonAdmissibleOverread: this stop creates no evidence relation, role, RoleDescription, assignment, authority, or publication
  ReopenCondition: enter F.8 only after one exact governed relation, its exact relation kind, one direct governing pattern, and the proposed naming use are independently present; reopen the direct claim first if its target claim, polarity, provenance, assurance or reliance use, or validity window changes
```

