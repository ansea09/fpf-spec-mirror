---
chunk_kind: "child"
pattern_id: "A.6.9"
pattern_title: "Cross-Context Sameness Disambiguation - Repairing cross-context \"same\", \"equivalent\", and \"align\" via explicit Bridges (RPR-XCTX)"
section_id: "A.6.9:5"
section_title: "Archetypal Grounding"
source_path: "FPF-Spec.md"
output_path: "by_section/A.6.9/A.6.9__007_archetypal-grounding.md"
commit_sha: "373c87917e92123cfa039e24c42a1f122b54fb66"
heading_path:
  - "A.6.9 — Cross-Context Sameness Disambiguation - Repairing cross-context \"same\", \"equivalent\", and \"align\" via explicit Bridges (RPR-XCTX)"
  - "A.6.9:5 — Archetypal Grounding"
line_start: 20412
line_end: 20438
dependencies:
  - "A.10"
  - "A.15.1"
  - "A.2.1"
  - "A.2.6"
  - "A.22"
  - "A.6.3.RT"
  - "A.6.6"
  - "A.6.P"
  - "A.7"
  - "B.3"
  - "C.2.1"
  - "C.29"
  - "C.3.3"
  - "E.17"
  - "E.19"
  - "F.0.1"
  - "F.17"
  - "F.18"
  - "F.5"
  - "F.6"
  - "F.7"
  - "F.8"
  - "F.9"
keywords:
  - "A.10/B.3 reliance"
  - "LocalSenseClaim> projections"
  - "actual receiving object"
  - "ambiguous sameness"
  - "different <ReferenceScheme"
  - "direct-owner dispatch"
  - "exact F.17 SchemeSenseCell endpoints"
  - "explicit stop"
  - "relation-only F.9 Bridge"
  - "separate C.2.1 bounded-use claim"
---

### A.6.9:5 - Archetypal Grounding

#### A.6.9:5.1 - System archetype: IAM User and CRM Customer

The ambiguous sentence is: “An IAM User is the same as a CRM Customer.”

Resolve exact endpoints:

- `SenseCell(IAMRoleReferenceScheme-v3, User-human-or-service-account-role)`;
- `SenseCell(CRMRoleReferenceScheme-v5, Customer-commercial-party-role)`.

Current meanings share some human participants, while service accounts and prospects provide counterexamples. Profile `P-IAM-CRM-OVERLAP-v2` states only the symmetric `Partial-overlap` relation, exact endpoint readings, overlap and difference conditions, edition basis, truth condition, and required membership evidence. Those facts make Bridge `b-iam-crm` obtain.

Now state the use separately. Dashboard team proposes `u-actor-label`: render IAM users as “actors” in a CRM-oriented comparison. Direction `d-iam-crm` is IAM-to-CRM dashboard reading. Rule `r-actor` keeps account eligibility and customer eligibility visible as separate columns. Tolerance `t-actor` allows the shared label but no eligibility, assignment, workflow, or Work inference. A C.2.1 claim about `b-iam-crm` is affirmative for `<u-actor-label,d-iam-crm,r-actor,t-actor>`.

The exact A.10 evidence-provenance relation and `RelianceDisposition=pass` support that claim only for the named dashboard comparison. They do not authorize data processing, assign a role, or prove that a dashboard publication occurred. Reverse label reuse is another bounded-use claim even though the Bridge relation is symmetric.

An optional actual card may package the Bridge claim, this bounded-use claim, observed counterexamples, the A.10 path and disposition, currentness, and nearest non-use. Its EntityOfConcern is `b-iam-crm`; the card neither creates the relation nor performs the dashboard work.

If a later workflow isolates `HumanVerifiedUser` and `VerifiedCustomer`, refine both cells and test another Bridge. A stronger use claim over the broad cells cannot repair a false or unsuitable predicate.

#### A.6.9:5.2 - Episteme archetype: Person in two knowledge-graph schemes

The sentence is: “Person in KG-A is equivalent to Person in KG-B.” The exact cells are `Person-including-fictional` under KG-A v4 and `Person-real-with-external-id` under KG-B v7. Sherlock Holmes and the external-id rule show `Partial-overlap`, not equivalence. The exact overlap Bridge obtains under the least-committing profile.

Two proposed uses then receive separate claims. A glossary comparison that labels both rows “Person” while displaying the fiction and external-id differences can receive affirmative polarity with a warranted A.10 path. A type-structure merge receives negative polarity because its correspondence rule cannot preserve membership and its tolerance permits no such loss. Both claims concern the same Bridge; neither changes its identity. Refining KG-A into `RealPerson` and `FictionalPerson` changes an endpoint and opens a new Bridge test.

