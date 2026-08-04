---
chunk_kind: "child"
pattern_id: "F.14"
pattern_title: "Anti-Explosion Control for Role and Status Name Families"
section_id: "F.14:7"
section_title: "Levers"
source_path: "FPF-Spec.md"
output_path: "by_section/F.14/F.14__008_levers.md"
commit_sha: "7ba40a95a967ca5c69afc63aeca381e6adedc8da"
heading_path:
  - "F.14 — Anti-Explosion Control for Role and Status Name Families"
  - "F.14:7 — Levers"
line_start: 94372
line_end: 94405
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

### F.14:7 - Levers

#### F.14:7.1 - Recover kind before naming

| Candidate shape | Likely recovery | Direct pattern |
| --- | --- | --- |
| `ReviewerRole`, `OperatorRole` | work-facing role value or RoleDescription label | A.2, F.4, F.5, F.18 |
| `AliceAsReviewer` | role assignment or performed-work attribution | A.2.1, F.6, A.15.1 |
| `SeniorReviewer` | role value plus qualifier, role state, capability, or assurance claim | A.2, A.2.2, A.2.5, B.3, F.18 |
| `RequestApproverRole` | role-bundle expression or forbidden hybrid | A.2.7, F.8 |
| `AtRisk`, `Grace`, `PreValidated` | status value, window, confidence, or presentation label | F.10 or direct status pattern |
| `EvidenceRole`, `RequirementRole`, `AccessRole` | evidence-use, requirement-use, policy/access, or source-use relation | A.10, E.10.D2, policy/access/source patterns |
| same spelling under two local-sense bases | two designations or an exact F.9 relation question | F.18, F.9; F.17 only at its public-row threshold |

#### F.14:7.2 - Reuse before minting

Reuse only when the exact recovered value, kind, direct pattern, proposed use, and admitted naming scope match. Try an existing designation, alias, local expression, or current row before creating a card, cell, row, policy id, or new U-kind candidate. Local-sense reuse does not imply sameness with another local sense; row reuse does not widen the row's admitted use.

#### F.14:7.3 - Use role relations before hybrid roles

If two roles travel together, recover the exact A.2.7 bundle or qualification relation. If they must stay apart, recover exact incompatibility and check assignments through A.2.1 and F.6. If one role can satisfy another requirement, recover exact substitution. The relation expression does not assign a holder and does not become a role value by name.

#### F.14:7.4 - Use a status window before multiplying status families

If the proposed name marks evaluation, active use, grace, archival state, confidence, or presentation, keep the status family and use F.10 windows, values, or direct status-use relations. A new status family needs a recovered governed difference, not another adjective.

#### F.14:7.5 - Keep qualifiers with their direct owners

Time, location, object type, seniority, permission, method, capability, evidence, source, and publication are not role or status identity by suffix. Keep each qualifier with its direct pattern. Retain it in a durable name only when the already governed value and the named use genuinely require that designation.

#### F.14:7.6 - Stop before a naming-object cascade

A candidate can justify one object without justifying all later objects. A durable local expression needs no cell; a stable local sense may need a cell but no NameCard; a durable naming settlement may need a NameCard but no public row; a row may exist without a current publication occurrence; publication availability creates neither row truth nor governed-value truth. Apply the next gate only when its own use is current.

