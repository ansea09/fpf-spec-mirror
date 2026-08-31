---
chunk_kind: "child"
pattern_id: "F.14"
pattern_title: "Anti-Explosion Control for System-Role and Status Name Families"
section_id: "F.14:1"
section_title: "Intent and applicability"
source_path: "FPF-Spec.md"
output_path: "by_section/F.14/F.14__002_intent-and-applicability.md"
commit_sha: "0c3ef3d3921bb3176096e3e6102dd819c42f6446"
heading_path:
  - "F.14 — Anti-Explosion Control for System-Role and Status Name Families"
  - "F.14:1 — Intent and applicability"
line_start: 97043
line_end: 97062
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
  - "F.6"
  - "F.8"
  - "F.9"
  - "U.SystemRoleAssignment"
keywords:
  - "NameCard"
  - "assignment"
  - "designation"
  - "evidence use"
  - "permission"
  - "reuse"
  - "status names"
  - "system-role names"
  - "term row"
  - "vocabulary explosion"
---

### F.14:1 - Intent and applicability

**Use this when.** Use F.14 when proposed names, aliases, cards, local-sense cells, or rows begin to multiply faster than the independently governed distinctions. Apply its cheap stop question before minting any NameCard, `SchemeSenseCell`, Unified Term Sheet row, or durable name family: **does an existing designation, alias, local expression, or direct-pattern name already let the practitioner perform the proposed use?**

**First useful move.** For every candidate expression, name the one independently recovered governed value or relation, its exact kind, its direct pattern, the proposed use, and the effective naming `U.ReferenceScheme`. If no such value or relation is independently recoverable, keep the expression local or keep it with the exact assertion that recovers its subject or value; do not pass a value-less expression to F.8 or manufacture an object so that the name has something to denote. F.8 receives only an unresolved naming disposition for an already recovered value-or-relation and proposed-use pair, with its exact kind and direct pattern.

**Intent.** Keep system-role-facing, role-like, and status-like vocabularies small without losing real distinctions. F.14 is a control pass over candidate expressions and name families. It defines no system-role kind, status, assignment, sense, card, row, Bridge, or publication. It decides only whether naming pressure can stop at a smaller disposition.

**Primary working object.** One candidate family and one proposed use, with its recovered values and direct patterns. A durable control record is optional; no generic context object, selected structure, card, or table row identifies the pass.

**Primary working reader.** A method author or designer, an author of a `U.MethodDescription`, a terminology steward, architect, manager, or checker who sees names such as `NightOperatorSystemRole`, `EvidenceRole`, `SeniorReviewer`, `AtRiskStatus`, `PreValidated`, `AccessRole`, or `RequestApproverSystemRole` and must stop vocabulary growth from becoming a second ontology.

**What goes wrong if missed.** System-role-kind labels become capability models, status labels become system-role families, access-control labels become work-facing kinds, and every local wording difference acquires a card, sense cell, row, or identifier. The corpus then contains many near-duplicate naming objects whose apparent precision hides different kinds and uses.

**What this buys.** A smaller vocabulary with stronger type separation and a short stopping path: no durable name, an existing designation, an alias, or a local expression whenever one suffices; only then the smallest justified durable naming object.

**Not this pattern when.** Use F.8 to make the final naming disposition for one candidate expression only after its governed value or relation, exact kind, direct pattern, and proposed use have been recovered; F.14 supplies the preceding anti-explosion stop rather than a second decision record. Assignment claims go to A.2.1. For precise performed Work, A.13 first recovers each exact actual performer and A.15.1 independently admits the dated occurrence; F.6 is added only when the naming case or receiving use expressly consumes precise assignment-bound attribution through the same obtaining A.13 assignment. Status, evidence, authorization, publication, and other relation claims require exact predicates in their direct patterns. Add a reader-facing F.17 row only after kind recovery, the F.14 stop, any needed F.8 or F.18 naming decision, and satisfaction of the public-row threshold; treat publication availability as a separate E.24.PUB question.

**Recognition versus assurance.** Recognition is the visible name-growth pressure plus the first kind-and-use recovery. Assurance is the optional record, invariants, worked countercases, and conformance tests. Neither turns F.14 into naming authority or ontology.

