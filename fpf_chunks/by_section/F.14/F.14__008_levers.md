---
chunk_kind: "child"
pattern_id: "F.14"
pattern_title: "Anti-Explosion Control for System-Role and Status Name Families"
section_id: "F.14:7"
section_title: "Levers"
source_path: "FPF-Spec.md"
output_path: "by_section/F.14/F.14__008_levers.md"
commit_sha: "b999972c4b60e6cef7206f9bbd777423e6525ec5"
heading_path:
  - "F.14 — Anti-Explosion Control for System-Role and Status Name Families"
  - "F.14:7 — Levers"
line_start: 97554
line_end: 97587
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

### F.14:7 - Levers

#### F.14:7.1 - Recover kind before naming

| Candidate shape | Likely recovery | Direct pattern |
| --- | --- | --- |
| `ReviewerSystemRole`, `OperatorSystemRole` | exact local system-role kind or its separate `SystemRoleKindDescription` episteme | A.2, F.4, F.5, F.18 |
| `AliceAsReviewer` | ordinary wording for a candidate classification, system-role assignment, or precise performed-Work attribution | A.2 with C.3 for classification; A.2.1 for assignment; A.13 then independent A.15.1 for performer and Work; F.6 only for an expressly consumed precise assignment-bound attribution |
| `SeniorReviewer` | a proposed system-role-kind name that may hide a qualifier, assignment-state condition, capability, or assurance claim | A.2, A.2.2, A.2.5, B.3, F.18 |
| `RequestApproverSystemRole` | system-role-kind bundle expression or forbidden fused kind | A.2.7, F.8 |
| `AtRisk`, `Grace`, `PreValidated` | status value, window, confidence, or presentation label | F.10 or direct status pattern |
| `EvidenceRole`, `RequirementRole`, `AccessRole` | first recover the exact claim: evidence reliance, an actual assurance claim, ambiguous description use, publication occurrence or form, or a requirement, standard, source, access, or policy use | A.10 for evidence reliance; B.3 only for an actual assurance claim; E.10.D2 only to recover description-use ambiguity; E.24.PUB for publication occurrence, form, or carrier; otherwise the pattern that directly defines, constrains, or tests the recovered claim, or `missing-governor` |
| same spelling under two local-sense bases | two designations or an exact F.9 relation question | F.18, F.9; F.17 only at its public-row threshold |

#### F.14:7.2 - Reuse before minting

Reuse only when the exact recovered value, kind, direct pattern, proposed use, and admitted naming scope match. Try an existing designation, alias, local expression, or current row before creating a card, cell, row, policy id, or new U-kind candidate. Local-sense reuse does not imply sameness with another local sense; row reuse does not widen the row's admitted use.

#### F.14:7.3 - Use relations among system-role kinds before hybrid kinds

If two system-role kinds travel together, recover the exact A.2.7 bundle or qualification relation. If they must stay apart, recover the exact A.2.7 incompatibility. Use A.2.1 and any applicable A.2.5 currentness condition to identify the assignment occurrences. Use F.6 only when the receiving claim separately says that dated Work was performed under one of those assignments. If one kind can satisfy another requirement, recover exact substitution. The relation expression assigns no system and does not become a new kind by name.

#### F.14:7.4 - Use a status window before multiplying status families

If the proposed name marks evaluation, active use, grace, archival state, confidence, or presentation, keep the status family and use F.10 windows, values, or direct status-use relations. A new status family needs a recovered governed difference, not another adjective.

#### F.14:7.5 - Keep qualifiers with the claims they qualify

Time, location, object type, seniority, permission, Method, capability, evidence, source, and publication are not system-role-kind or status identity by suffix. Keep a qualifier with the claim it qualifies and use the pattern that defines, constrains, or tests that claim. Retain the qualifier in a durable name only when the already governed value and named use genuinely require that designation.

#### F.14:7.6 - Stop before a naming-object cascade

A candidate can justify one object without justifying all later objects. A durable local expression needs no cell; a stable local sense may need a cell but no NameCard; a durable naming settlement may need a NameCard but no public row; a row may exist without a current publication occurrence; publication availability creates neither row truth nor governed-value truth. Apply the next gate only when its own use is current.

