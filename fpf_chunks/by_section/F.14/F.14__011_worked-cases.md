---
chunk_kind: "child"
pattern_id: "F.14"
pattern_title: "Anti-Explosion Control for Role and Status Name Families"
section_id: "F.14:10"
section_title: "Worked cases"
source_path: "FPF-Spec.md"
output_path: "by_section/F.14/F.14__011_worked-cases.md"
commit_sha: "6709213844a26981daf25510ac99ffb7fa53b017"
heading_path:
  - "F.14 — Anti-Explosion Control for Role and Status Name Families"
  - "F.14:10 — Worked cases"
line_start: 94511
line_end: 94570
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

### F.14:10 - Worked cases

#### F.14:10.1 - Requester and approver

Candidate family: `RequesterRole`, `ApproverRole`, `RequestApproverRole`, `SeniorApprover`.

Result:

* `RequesterRole` and `ApproverRole` are work-facing role values with RoleDescriptions.
* `RequestApproverRole` is blocked as a fused role. Use an A.2.7 role-bundle expression when the two roles travel together.
* If the same holder must not carry both assignments in the same change window, use A.2.7 incompatibility plus A.2.1 and F.6 assignment checks.
* `SeniorApprover` is not proof of independence or assurance. Recover role state, capability, assurance, or local policy before durable naming.

#### F.14:10.2 - Operators across shifts

Candidate family: `OperatorRole`, `NightOperatorRole`, `RemoteOperatorRole`, `OnCallOperatorRole`.

Result:

* `OperatorRole` is the role value.
* `night`, `remote`, and `on-call` are recovered as schedule, location, role-state, work-plan, or policy qualifiers.
* A new role is blocked unless A.2 independently admits a distinct role value with a different RoleDescription, assignment predicates, and method or Work implications for the proposed use; the naming ReferenceScheme does not create that difference.

#### F.14:10.3 - SLO compliance labels

Candidate family: `Compliant`, `AtRisk`, `Grace`, `Breached`, `Waived`.

Result:

* These are not role names.
* F.10 recovers status family, status value, status window, confidence, or deontic or policy use.
* Presentation labels may stay local or be named by the direct status pattern. They do not become `U.Role`, RoleDescription, or role relation structure.

#### F.14:10.4 - Evidence and requirement suffixes

Candidate family: `EvidenceRole`, `RequirementRole`, `StandardRole`, `SourceRole`.

Result:

* No work-facing role is recovered from suffix alone.
* Evidence, requirement, standard, source, and publication uses go to A.10, B.3, E.10.D2, E.24.PUB, or the direct requirement or source pattern.
* A durable name may be admitted for the recovered relation, but not as a role value.

#### F.14:10.5 - Same spelling across two local-sense bases

A plant team uses `Operator` for one work-facing role value. An access-control team uses `Operator` for one permission grouping. Recover both independently under their direct patterns; neither spelling nor organizational proximity makes them one value.

For local use, keep the existing expressions and stop. If one named cross-local naming use is later proposed, resolve its exact F.17 `SchemeSenseCell` endpoints and test F.9. Cite a Bridge only when its predicate obtains, then state the use direction, rule, tolerated loss, polarity, and reliance separately. A Bridge, NameCard, cell, or row imports no access permission as `U.RoleAssignment`, capability, authority, or performed Work. Publish an F.17 row only when the public/durable reuse threshold independently holds.

#### F.14:10.6 - Ordinary composite role names

A project says: "Vasya is an engineer, he works on musical robots, and he is also a musician who teaches robots to play music."

Result:

* Ordinary prose may remain `robotics engineer and musician` or `engineer-musician` when readers can recover the two exact role values and the sentence's use without ambiguity. FPF does not require a `Role` suffix.
* Recover engineering and musician role values independently under A.2. If robotics narrows the engineering role for this use, keep the exact qualifier, RoleDescription, or A.2.7 qualification/bundle relation rather than minting `EngineerRoboticistRole` automatically.
* Method and Work remain separate: engineering methods, music-teaching methods, robot-training Work, and performed music Work stay under their direct patterns. They motivate no role name by themselves.
* A durable qualified role name is considered only when the already governed role value has different assignment predicates, capability expectations, incompatibilities, method/Work implications, or a real public naming need. Otherwise keep the ordinary phrase and cite the exact relations only where they matter.

