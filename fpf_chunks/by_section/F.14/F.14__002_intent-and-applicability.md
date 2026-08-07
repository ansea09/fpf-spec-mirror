---
chunk_kind: "child"
pattern_id: "F.14"
pattern_title: "Anti-Explosion Control for Role and Status Name Families"
section_id: "F.14:1"
section_title: "Intent and applicability"
source_path: "FPF-Spec.md"
output_path: "by_section/F.14/F.14__002_intent-and-applicability.md"
commit_sha: "1602a8d0a6934a99a79ead914610b070cedd86d2"
heading_path:
  - "F.14 — Anti-Explosion Control for Role and Status Name Families"
  - "F.14:1 — Intent and applicability"
line_start: 94566
line_end: 94585
dependencies:
  - "A.10"
  - "A.15.1"
  - "A.2"
  - "A.2.1"
  - "A.2.2"
  - "A.2.5"
  - "A.2.7"
  - "A.3.1"
  - "A.3.2"
  - "A.6.5"
  - "B.3"
  - "E.10.D2"
  - "E.24.PUB"
  - "F.10"
  - "F.17"
  - "F.18"
  - "F.4"
  - "F.5"
  - "F.8"
  - "F.9"
  - "U.Role"
  - "U.RoleAssignment"
keywords:
  - "bundles"
  - "guard-rails"
  - "reuse"
  - "separation-of-duties"
  - "vocabulary growth"
---

### F.14:1 - Intent and applicability

**Use this when.** Use F.14 when proposed names, aliases, cards, local-sense cells, or rows begin to multiply faster than the independently governed distinctions. Apply its cheap stop question before minting any NameCard, `SchemeSenseCell`, Unified Term Sheet row, or durable name family: **does an existing designation, alias, local expression, or direct-pattern name already let the practitioner perform the proposed use?**

**First useful move.** For every candidate expression, name the one independently recovered governed value or relation, its exact kind, its direct pattern, the proposed use, and the effective naming `U.ReferenceScheme`. If no such value or relation is independently recoverable, keep the expression local or return it to the direct subject/value-recovery owner; do not send a value-less expression to F.8 or manufacture an object so that the name has something to denote. F.8 receives only an unresolved naming disposition for an already recovered value-or-relation/use pair, with its exact kind, direct pattern, and proposed use.

**Intent.** Keep role-like and status-like vocabularies small without losing real distinctions. F.14 is a control pass over candidate expressions and name families. It defines no role, status, assignment, sense, card, row, Bridge, or publication. It decides only whether naming pressure can stop at a smaller disposition.

**Primary working object.** One candidate family and one proposed use, with its recovered values and direct patterns. A durable control record is optional; no generic context object, selected structure, card, or table row identifies the pass.

**Primary working reader.** A method author, terminology steward, architect, manager, or checker who sees names such as `NightOperatorRole`, `EvidenceRole`, `SeniorReviewer`, `AtRiskStatus`, `PreValidated`, `AccessRole`, or `RequestApproverRole` and must stop vocabulary growth from becoming a second ontology.

**What goes wrong if missed.** Role labels become capability models, status labels become role families, access-control labels become work roles, and every local wording difference acquires a card, sense cell, row, or identifier. The corpus then contains many near-duplicate naming objects whose apparent precision hides different kinds and uses.

**What this buys.** A smaller vocabulary with stronger type separation and a short stopping path: no durable name, an existing designation, an alias, or a local expression whenever one suffices; only then the smallest justified durable naming object.

**Not this pattern when.** F.8 owns the final naming disposition for one candidate expression only after its governed value or relation, exact kind, direct pattern, and proposed use have been recovered; F.14 supplies the preceding anti-explosion stop rather than a second decision record. Assignment and performed-work claims go to A.2.1, F.6, and A.15.1. Status, evidence, authorization, publication, and subject-relation claims return to their direct patterns. F.17 constitutes a reader-facing row only after kind recovery, F.14, F.8/F.18 where needed, and the public-row threshold; E.24.PUB separately governs availability.

**Recognition versus assurance.** Recognition is the visible name-growth pressure plus the first kind-and-use recovery. Assurance is the optional record, invariants, worked countercases, and conformance tests. Neither turns F.14 into naming authority or ontology.

