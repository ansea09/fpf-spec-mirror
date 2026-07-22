---
chunk_kind: "child"
pattern_id: "A.2.8"
pattern_title: "U.Commitment (Deontic Commitment Object)"
section_id: "A.2.8:0"
section_title: "Use This When"
source_path: "FPF-Spec.md"
output_path: "by_section/A.2.8/A.2.8__003_use-this-when.md"
commit_sha: "0990ff1d1ccee4587b8f7e16e7a725a8edbe66b4"
heading_path:
  - "A.2.8 — U.Commitment (Deontic Commitment Object)"
  - "A.2.8:0 — Use This When"
line_start: 5451
line_end: 5477
dependencies:
  - "A.15.1"
  - "A.2"
  - "A.2.1"
  - "A.2.3"
  - "A.2.6"
  - "A.2.8.PER"
  - "A.2.9"
  - "A.6.B"
  - "A.6.C"
  - "A.7"
  - "E.8"
  - "U.PromiseContent"
  - "U.Work"
keywords:
  - ") but makes the structure explicit"
  - "BCP‑14 (RFC 2119/8174)"
  - "adjudication hooks"
  - "are cues for the modality field after the deontic relation is recovered"
  - "by themselves"
  - "commitment"
  - "deontics"
  - "evidenceRefs"
  - "modality normalization"
  - "obligation"
  - "prohibition"
  - "recommendation-as-duty"
  - "scope and validity window"
  - "they are not the governed object of this pattern"
---

### A.2.8:0 - Use This When

Use this pattern when a project needs to state who is accountable for what, under which modality, scope, and time window, without pretending that the words in a specification, contract, ticket, API description, or standard are themselves the accountable actor.

**What goes wrong if missed.** A specification, interface, dashboard, contract text, or ticket is treated as the accountable party; evidence, gate admission, performed work, and commitment content collapse into one deontic-looking sentence.

**What this buys.** The accountable subject, modality, referent, scope, time window, and adjudication hooks become inspectable without turning publications, evidence, gates, or work occurrences into commitment holders.

Typical moments:

- a promise content, policy clause, requirement, SLA, protocol rule, or standard clause must become an accountable commitment;
- source wording says "MUST", "SHALL", "guarantees", "is responsible for", or "legally binding", and the project must recover the deontic relation rather than normalize keywords by themselves;
- evidence or gates are being attached to a duty and the model must keep commitment content, adjudication evidence, and performed work distinct.

**Primary EntityOfConcern.** The EntityOfConcern is `U.Commitment`: a deontic relation linking an accountable subject to referents under explicit modality, scope, validity window, and optional adjudication hooks.

**First useful move.** Name the accountable subject and the referents first. Then state modality, scope, validity window, and adjudication only if the commitment is meant to be checked or enforced.

**Not this pattern when.** If the current EntityOfConcern is the promised content, use `A.2.3`; if it is the communicative act that instituted or revoked the commitment, use `A.2.9`; if it is a gate or admissibility claim, use the gate or boundary pattern; if it is performed work, use `A.15.1`.

> **Type:** Definitional (D)
> **Normativity:** Normative (unless explicitly marked informative)
> **Placement:** Part A → **A.2 Roles & Agency Kernel**
> **Refines:** A.2 (Role Taxonomy)
> **Builds on:** E.8 (authoring template), A.2.1 (RoleAssignment), A.2.6 (Scope & `Γ_time`), A.7 (EntityOfConcern / Description episteme / carrier), A.2.3 (`U.PromiseContent` as promise), A.15.1 (`U.Work`)
> **Purpose (one line):** Provide a minimal, reusable kernel object for deontic commitments (who is accountable, under what modality, in what scope/window, with respect to which referents, with which adjudication hooks), **explicitly separating the commitment object from its utterance descriptions** (A.7), so deontics stop “living” in naming patterns and become stable across A.6 and governance patterns.

