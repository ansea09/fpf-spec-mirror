---
chunk_kind: "child"
pattern_id: "A.2.3"
pattern_title: "U.PromiseContent — Promised Outcomes and Acceptance Criteria"
section_id: "A.2.3:10"
section_title: "Existing promise-description repair applications"
source_path: "FPF-Spec.md"
output_path: "by_section/A.2.3/A.2.3__013_existing-promise-description-repair-applications.md"
commit_sha: "6226816d8005a4c8ee3af338bb3752f6732449a9"
heading_path:
  - "A.2.3 — U.PromiseContent — Promised Outcomes and Acceptance Criteria"
  - "A.2.3:10 — Existing promise-description repair applications"
line_start: 6274
line_end: 6284
dependencies:
  - "A.2.2"
  - "A.2.8"
  - "A.6.C"
  - "A.6.P"
  - "E.10"
  - "F.12"
keywords:
  - "SLA"
  - "SLO"
  - "Work evidence"
  - "acceptance specification"
  - "access specification"
  - "claim scope"
  - "promise content"
  - "promised outcome"
  - "provider and consumer system-role kinds"
---

### A.2.3:10 - Existing promise-description repair applications

1. **Name the promises.** Identify the consumer-facing promises needed by the project. Represent each as `U.PromiseContent` with effective reference scheme, promised outcome specification, acceptance specification, and claim scope, plus access specification and unit of delivery when current.
2. **Separate provider from promise content.** Recover each provider, access point, or delivery bearer through A.6.P:4.11a. Apply A.1 or A.1.SCR only where a provider-assignment, access-point, delivery-system, performer, or other claim depends on systemhood. When an assignment is claimed, name its A.2.1 occurrence and declared species, with the provider System as holder.
3. **Relate promise content to delivery and evidence.** Add `PromiseContentUse` for every delivery-work occurrence evaluated under the promise. Establish `PromisedOutcomeDeliveryRelation` only after work facts, affected or delivered entities, post-work states, and any direct delivery relation required by the resolved `OutcomeSpec` satisfy it; establish `PromiseContentFulfilmentRelation` only after those facts and states satisfy the declared acceptance criteria.

   Identify an evaluation-operation result binding when the governing rule or the assertion relies on that application. Identify any verdict episteme relied on, the evidence supporting the claim and its A.10 evidence relations separately.
4. **Define evaluation characteristics.** Read the acceptance clause to determine the promised unit, eligibility, reporting period and required outcome. Choose a measure in §8.2 only for that question. For a promise to answer every eligible request, include requests without a delivery and respect their deadlines. The proportion of successful performed jobs answers a different question. For each characteristic, name its scale, unit where applicable, C.16 measurement template, `Gamma_time` policy and formula. Identify the evidence for a measured verdict, and the measurement Method or its description edition where interpretation depends on it.
5. **Bridge domain schemes.** If a domain ontology distinguishes business, technical, or internal service kinds and relations, retain its reference scheme and name the exact obtaining F.9 Bridge for each selected sense and FPF counterpart. Add the separate C.2.1 claim that the Bridge suits the named use, then require the A.10 evidence-provenance relation with `RelianceDisposition=pass`. Use B.3 only for a named assurance claim. Keep `PromiseContentUse`, Work, delivery, fulfilment, result, evidence, assurance, and publication separate.
6. **Tidy relied-on language.** Apply **L-SERV** and **A.6.P:4.11a** only when *service* or access-like wording hides a concrete subject, participant, predicate, kind, permission, Work occurrence, or next route in the current relied-on use. State what the wording denotes and use the pattern that defines or constrains that claim, or stop the use; use A.1 or A.1.SCR only when a recovered bearer claim depends on systemhood. Reserve `U.PromiseContent` for the consumer-facing promise content, and leave clear, quoted, historical, illustrative, and harmless ordinary wording outside this step.

