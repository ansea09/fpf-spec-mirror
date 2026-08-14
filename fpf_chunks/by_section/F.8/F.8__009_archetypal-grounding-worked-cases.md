---
chunk_kind: "child"
pattern_id: "F.8"
pattern_title: "Mint-or-Reuse Decision"
section_id: "F.8:7"
section_title: "Archetypal Grounding - worked cases"
source_path: "FPF-Spec.md"
output_path: "by_section/F.8/F.8__009_archetypal-grounding-worked-cases.md"
commit_sha: "646b41f84ffef4918ad9bdb34e7b450f0c4903ee"
heading_path:
  - "F.8 — Mint-or-Reuse Decision"
  - "F.8:7 — Archetypal Grounding - worked cases"
line_start: 93222
line_end: 93300
dependencies:
  - "A.11"
  - "A.15"
  - "A.15.1"
  - "A.2"
  - "A.2.1"
  - "A.2.5"
  - "A.2.7"
  - "A.6.5"
  - "A.6.RCD"
  - "A.7"
  - "A.8"
  - "C.11"
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
  - "role-shaped names"
  - "type explosion"
---

### F.8:7 - Archetypal Grounding - worked cases

#### F.8:7.1 - `ReviewerRole` Expression vs Review Report

The source label `PatternReview_2026` is not a context object. Classify the actual claim before using it:

- `ReviewWork-82` can be one dated `U.Work` occurrence under `A.15.1`;
- `ReviewPlan-2026-v3` can be a separately constituted plan episteme or edition under its subject pattern;
- `PatternReviewReferenceScheme-2026` can be an effective by-value `U.ReferenceScheme` for interpreting review terminology; and
- "used while deciding the label for the 2026 review method" can be claim content describing the decision-use setting without minting any context entity.

If the independently governed `ReviewerSystemRole` is a local system-role kind, F.8 may return `nameSystemRoleKindDescription`: use `F.4` for the `SystemRoleKindDescription` episteme and `F.5` or `F.18` for the label when its durability is current. The review label does not define that kind, assign a reviewer system, or demonstrate review Work.

The expression "review report has reviewer role" is a different case. `ReviewReport-82` is an episteme. A direct evidence, source, or publication relation may later use it for an adequacy claim about a reviewed pattern; the report is not a `U.System`, is not classified by the local review-system-role kind, and cannot enter its assignment relation. Its title does not make any evidence use or publication authority obtain.

#### F.8:7.2 - Actor Across BPMN and PROV

A manager wants one word, "actor", for a BPMN participant and a PROV agent in a diagram. First recover the two exact local senses under their effective ReferenceSchemes. If an actual F.9 Bridge relates the exact cells and one F.17 row admits naming-only use, F.8 returns `reuseAdmittedTermRow` for prose and diagram labels only.

No governed-value identity, substitution, system-role assignment, or Work follows. If the project later needs a local system-role kind under one scheme, it creates or reuses the local `SystemRoleKindDescription` episteme for that independently recovered kind.

#### F.8:7.3 - Access Role

An access-control source says `ApproverRole`. Under the source's effective naming ReferenceScheme, the expression may designate a permission grouping or exact policy relation. F.8 first recovers the exact access, policy, status, or deontic assertion and predicate. Only if A.2 independently recovers an exact local approval-system-role kind does a `SystemRoleKindDescription` naming decision become current.

Otherwise the durable designation, if needed, belongs to the direct access, policy, status, or gate pattern. The `Role` suffix, a source card, or a selected model-use Structure creates no local system-role kind or assignment.

#### F.8:7.4 - Policy Identifier

A gate profile proposes `Aut-Guard-2026`. F.8 treats this as a policy-identifier question only after an exact policy specification is independently recoverable. Ordinary reuse resolves the existing identifier and its separate specification. Recover the original mint decision or choice occurrence only when the current reuse relies on that history for citation, replay, accountability, supersession, or another named relation. New introduction requires the direct mint basis when such a claim is made; without its predicate, participants, applicability, and occurrence identity, return `missing-governor` for that stronger claim. Any C.11 result, decision-making Work, result episteme, or displayed record stays separate.

The identifier is not the specification, local system-role kind, method, gate result, evidence value, permission, or source authority. It is a reference used by the pattern that defines or constrains the exact policy claim.

#### F.8:7.5 - New U-kind Candidate

A team proposes `U.InfluenceEdge` because many documents use "influence". F.8 blocks immediate minting. The team must show that the candidate is not an existing relation, causal claim, evidence relation, characteristic, method relation, Bridge relation, structural name, publication form, or local frame under current patterns. If it remains cross-family, irreducible, and needed by several domain families, the proposal goes to `E.24.UK`, `A.8`, `A.11`, `C.3`, `E.9`, and `F.18`. F.8 neither creates nor admits the kind.

#### F.8:7.6 - Readable Disposition and Explicit Stops

The first case needs only the light F.8 result. `PatternReviewReferenceScheme-2026` is the effective naming scheme; the actual review Work, any review plan, and this naming use remain separate. The following is a readable projection, not an identified decision occurrence or durable decision record:

```text
CandidateExpression: ReviewerRole
GovernedValueOrRelationRef: ReviewerSystemRole
GovernedKindOrRelationKindRef: the admitted U.Kind for ReviewerSystemRole
GovernedValueSubjectPatternLocator: A.2
ProposedNamingUse: durable local label for the SystemRoleKindDescription episteme used by the review method
EffectiveNamingReferenceScheme: PatternReviewReferenceScheme-2026
LocalSenseClaim: local U.Kind for U.System candidates, identified by the stable review contribution and tested by its KindSignature; assignment is separate
ReuseCandidateRefs: no existing designation or alias supports the exact proposed use
SelectedDisposition: nameSystemRoleKindDescription
ResultingNamingRefs: F.4 SystemRoleKindDescription authoring next; F.18 only if durable reuse remains current
DurableDecisionOccurrence: omitted; no receiving claim needs citation, replay, or accountability
DecisionResultEpisteme: omitted
NonAdmissibleOverread: the disposition assigns no System, establishes no review Work or evidence use, and publishes no label
ReopenCondition: reopen if the expression is used for evidence, status, access, source, publication, or cross-local row claims
```

If a later receiving claim genuinely needs an accountable occurrence, first recover its direct decision or choice pattern, predicate, actual participants, applicability, and identity rule. No such direct pattern is current in this worked case, so the correct durable branch result is `missing naming-decision governor`; do not mint `ReviewerSystemRoleNamingDecision-2026-07-31`. A C.11 `ChoiceResult` may be used only when the case is genuinely a local choice among already available options and satisfies C.11; any dated decision-making Work remains separate under A.15.1 and F.6.

The second case does not enter F.8. The proposed `EvidenceRole` wording has exposed an evidence-use question, but no exact governed relation, relation kind, or single subject pattern has yet been recovered. The review label again supplies no context, evidence, or authority.

```text
PreF8RecoveryStop:
  CandidateExpression: EvidenceRole
  KnownSubject: ReviewReport-82 : U.Episteme
  ProposedNamingUse: reusable wording for one exact evidence-use relation
  EffectiveNamingReferenceScheme: PatternReviewReferenceScheme-2026
  RecoveredFact: ReviewReport-82 is proposed for evidence use concerning an adequacy claim; it is not a system and cannot be assigned to a local system-role kind
  MissingEntryFacts: the exact target claim and polarity; the exact evidence-use relation and relation kind; provenance, assurance or reliance use, and validity window when current; one subject pattern
  RequiredDirectPatternUse: apply the one pattern whose Solution defines the exact evidence-use relation and recover the missing entry facts there
  LocalSenseState: no stable cell address or independently current LocalSenseBasisRelation is needed for this blocked role-word reading
  SelectedModelUseStructureState: none; no independently selected Structure changes this use
  DirectTerminologyProbe: test the eventual direct evidence-pattern terminology only after recovery
  StopResult: do not enter F.8 and do not mint EvidenceRole; keep the expression local until the governed relation, exact kind, one direct pattern, and proposed naming use are present
  NonAdmissibleOverread: this stop creates no evidence relation, local system-role kind, SystemRoleKindDescription, assignment, authority, or publication
  ReopenCondition: enter F.8 only after one exact governed relation, its exact relation kind, one subject pattern, and the proposed naming use are independently present; reopen the direct claim first if its target claim, polarity, provenance, assurance or reliance use, or validity window changes
```

