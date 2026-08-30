---
chunk_kind: "child"
pattern_id: "F.8"
pattern_title: "Mint-or-Reuse Decision"
section_id: "F.8:7"
section_title: "Archetypal Grounding - worked cases"
source_path: "FPF-Spec.md"
output_path: "by_section/F.8/F.8__009_archetypal-grounding-worked-cases.md"
commit_sha: "8bb4989c9be7fa4b33f0bb7537e4611676ee3087"
heading_path:
  - "F.8 — Mint-or-Reuse Decision"
  - "F.8:7 — Archetypal Grounding - worked cases"
line_start: 94677
line_end: 94725
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
  - "F.8"
  - "F.9"
keywords:
  - "admission before naming"
  - "alias"
  - "designation"
  - "durable naming"
  - "governed value or relation"
  - "local phrase"
  - "proposed naming use"
  - "row use"
  - "subject before name"
---

### F.8:7 - Archetypal Grounding - worked cases

#### F.8:7.1 - `ReviewerRole` Expression vs Review Report

The source label `PatternReview_2026` is not a context object. Classify the actual claim before using it:

- `ReviewWork-82` can be one dated `U.Work` occurrence under `A.15.1`;
- `ReviewPlan-2026-v3` can be a separately constituted plan episteme or edition under its subject pattern;
- `PatternReviewReferenceScheme-2026` can be an effective by-value `U.ReferenceScheme` for interpreting review terminology; and
- "used while deciding the label for the 2026 review method" can be claim content describing the decision-use setting without minting any context entity.

If the recovered `ReviewerSystemRole` kind needs a durable local designation, F.8 returns `openDurableNamingSettlement`: A.2 and C.3 keep governing the kind, F.5 governs its designation, and F.18 supplies the settlement. This need does not require a `SystemRoleKindDescription`; use F.4 only when the practice separately needs that description. The review label defines no kind, assigns no reviewer system, and demonstrates no review Work.

The expression "review report has reviewer role" is a different case. `ReviewReport-82` is an episteme. An evidence, source, or publication relation may later use it for an adequacy claim about a reviewed pattern; the report is not a `U.System`, is not classified by the review-system-role kind, and cannot enter its assignment relation. Its title establishes neither evidence use nor publication authority.

#### F.8:7.2 - Actor Across BPMN and PROV

A manager wants one word, "actor", for a BPMN participant and a PROV agent in a diagram. First recover the two local senses under their ReferenceSchemes. If an obtaining F.9 Bridge relates the named cells and an F.17 row admits naming-only use, F.8 returns `reuseAdmittedTermRow` for prose and diagram labels only. This supports no governed-value identity, substitution, system-role assignment, or Work.

If the project later needs a local system-role kind under one scheme, it first recovers the kind through A.2 and C.3. F.5 then governs any new designation, with F.18 only for durable reuse; F.4 is added only if a separate description episteme is needed.

#### F.8:7.3 - Access Role

An access-control source says `ApproverRole`. Under its naming ReferenceScheme, the expression may designate a permission grouping or policy relation. First recover the access, policy, status, or deontic claim and predicate. Only if A.2 and C.3 recover a local approval-system-role kind does F.8 consider a name for that kind. F.5 governs its designation, F.18 applies only for durability, and F.4 remains optional for a separately needed description.

Otherwise any needed durable designation belongs to the access, policy, status, or gate pattern. The `Role` suffix, a source card, or a selected model-use Structure creates no local system-role kind or assignment.

#### F.8:7.4 - Policy Identifier

A gate profile proposes `Aut-Guard-2026`. F.8 treats this as a policy-identifier question only after the policy specification is recovered. Ordinary reuse resolves the identifier and specification. Recover the mint decision or choice occurrence only when reuse relies on that history for citation, replay, accountability, supersession, or another named relation. If a new introduction makes that stronger claim without an occurrence basis, return `missing-governor`. Any C.11 result, decision-making Work, result episteme, or record stays separate.

The identifier is not the specification, local system-role kind, Method, gate result, evidence value, permission, or source authority. It is a reference used by the pattern that defines or constrains the governed policy claim.

#### F.8:7.5 - New U-kind Candidate

A team proposes `U.InfluenceEdge` because many documents use "influence". At F.8 entry there is no recovered governed value with a stable admission disposition, so F.8 returns `blockOrLowerUse` and stops naming. If the expression still hides whether the subject is an existing relation or claim—for example, a causal, evidence, Method, or Bridge relation—or a characteristic, structural name, publication form, local frame, or another object, E.24.CD recovers that object or the unresolved proposal. A recovered governed object returns to its subject pattern; a surviving U-kind proposal goes to E.24.UK for `root`, `same-individual-dependent`, `identity-dependent`, `reuse`, `local-kind`, or `reject`. Only after that result is stable may F.8 reopen for a name of the admitted or reused kind, bounded local kind, or recovered non-kind object. F.8 creates neither the proposal object nor a public spelling and admits no kind.

#### F.8:7.6 - Readable Disposition and Explicit Stops

The `ReviewerRole` case closes with one readable result. The recovered kind is a local `U.Kind` for `U.System` candidates, distinguished by its stable review contribution and tested by its `KindSignature`; any assignment remains separate. The result is:

> Under `PatternReviewReferenceScheme-2026`, use `ReviewerRole` as the Plain designation of `ReviewerSystemRole` for local review-method prose. No existing designation or alias supports that use, so select `openDurableNamingSettlement`: A.2 and C.3 continue to govern the kind, F.5 governs its designation, and F.18 supplies the durable settlement. This result creates no `SystemRoleKindDescription`, assignment, review Work, evidence use, or publication. Reopen it if the proposed use becomes evidential, status-bearing, access-related, source-facing, published, or cross-local.

That sentence is the F.8 result. It needs no decision occurrence or result episteme. If a later claim must cite, replay, or assign accountability to the decision, use §4.5. No naming-decision governor is available in this case, so that branch returns `missing-governor` rather than inventing `ReviewerSystemRoleNamingDecision-2026-07-31`. C.11 applies only to a genuine local choice among available options. For any precise decision-making Work, A.13 first recovers the exact actual performer and A.15.1 independently admits the dated Work; F.6 follows only when the later claim expressly consumes precise assignment-bound attribution through the same obtaining A.13 assignment.

`EvidenceRole` stops earlier and does not enter F.8. The known subject is `ReviewReport-82 : U.Episteme`, proposed for evidence use concerning an adequacy claim. Still missing are the target claim and polarity, the evidence-use relation and relation kind, the provenance and any assurance or reliance use and validity window, and one subject pattern that defines the relation. Apply that pattern and keep the wording local until those facts are recovered. `PatternReviewReferenceScheme-2026` may interpret the source wording, but the review label creates no evidence relation, system-role kind, description, assignment, authority, or publication. No `SchemeSenseCell`, `LocalSenseBasisRelation`, or selected Structure is needed merely to record this stop.

Re-enter F.8 only after one governed relation, its kind, its subject pattern, and the proposed naming use are available. If the target claim, polarity, provenance, assurance or reliance use, or validity window changes, reopen the subject claim rather than the name.

