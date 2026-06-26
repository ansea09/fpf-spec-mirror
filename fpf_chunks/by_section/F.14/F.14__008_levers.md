---
chunk_kind: "child"
pattern_id: "F.14"
pattern_title: "Anti-Explosion Control for Role and Status Name Families"
section_id: "F.14:7"
section_title: "Levers"
source_path: "FPF-Spec.md"
output_path: "by_section/F.14/F.14__008_levers.md"
commit_sha: "02a8b4bac1f141b1751421bf522e9dc489ae522e"
heading_path:
  - "F.14 — Anti-Explosion Control for Role and Status Name Families"
  - "F.14:7 — Levers"
line_start: 84585
line_end: 84616
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
  - "E.17"
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

Ask what the candidate expression is trying to name.

| Candidate shape | Likely recovery | Direct pattern |
| --- | --- | --- |
| `ReviewerRole`, `OperatorRole` | work-facing role value or RoleDescription label | A.2, F.4, F.5, F.18 |
| `AliceAsReviewer` | role assignment or performed-work attribution | A.2.1, F.6, A.15.1 |
| `SeniorReviewer` | role value plus qualifier, role state, capability, or assurance claim | A.2, A.2.2, A.2.5, B.3, F.18 |
| `RequestApproverRole` | role-bundle expression or forbidden hybrid | A.2.7, F.8 |
| `AtRisk`, `Grace`, `PreValidated` | status value, window, confidence, or presentation label | F.10 or direct status pattern |
| `EvidenceRole`, `RequirementRole`, `AccessRole` | evidence-use, requirement-use, policy or access, or source-use relation | A.10, E.10.D2, E.17, policy or access patterns |
| same label in two contexts | cross-context bridge or public term | F.9, F.17, F.18 |

#### F.14:7.2 - Reuse before minting

Reuse a value when the recovered value, bounded context, and admitted use match. Use F.9 when reuse crosses context. Use F.8 when a candidate appears new. Use F.18 only when a durable name is needed after kind recovery.

#### F.14:7.3 - Role Relation Structure Before Hybrid Role

If two roles often appear together, state a role-bundle expression in A.2.7. If two roles must stay apart, state an incompatibility relation in A.2.7 and check assignments with A.2.1 and F.6. If one role value can satisfy another role requirement, state a role-requirement substitution relation in A.2.7. The role-relation expression does not assign a holder and does not become a role value by itself.

#### F.14:7.4 - Status window before status family multiplication

If the proposed name marks evaluation, active use, grace, archival state, confidence, or presentation, keep the status family and use F.10 windows, values, or direct status-use relations. A new status family needs a recovered value difference, not a new adjective.

#### F.14:7.5 - Qualifier before role-name clone

If the proposed role name adds time, location, object type, seniority, permission, method, capability, evidence, or source, recover the qualifier's direct pattern. Only keep it in a durable role name if F.18 admits that the bounded context truly needs a separate role value.

