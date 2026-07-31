---
chunk_kind: "child"
pattern_id: "F.14"
pattern_title: "Anti-Explosion Control for Role and Status Name Families"
section_id: "F.14:10"
section_title: "Worked cases"
source_path: "FPF-Spec.md"
output_path: "by_section/F.14/F.14__011_worked-cases.md"
commit_sha: "d1f696e7c7767705206a8cacd9f6ed48e4dc5b02"
heading_path:
  - "F.14 — Anti-Explosion Control for Role and Status Name Families"
  - "F.14:10 — Worked cases"
line_start: 92878
line_end: 92942
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
* A new role is blocked unless the bounded context shows a distinct role value with different RoleDescription, assignment predicates, and method or work implications.

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
* Evidence, requirement, standard, and source uses go to A.10, B.3, E.10.D2, E.17, or the direct requirement or source pattern.
* A durable name may be admitted for the recovered relation, but not as a role value.

#### F.14:10.5 - Cross-context role labels

Two contexts both use `Operator`. One is a plant-control role; the other is an access-control permission grouping.

Result:

* F.9 Bridge Card first.
* The bridge may admit Naming-only or RoleDescription naming for a local work-facing role when the role value is recovered.
* The bridge does not import access permission as `U.RoleAssignment`, capability, or performed work.

#### F.14:10.6 - Ordinary composite role names

A project says: "Vasya is an engineer, he works on musical robots, and he is also a musician who teaches robots to play music."

Result:

* The ordinary phrase may remain "robotics engineer and musician" or "robotics engineer-musician" when the reader can recover it without ambiguity. FPF does not require a `Role` suffix in ordinary prose.
* Recover at least two work-facing role values when they are current: `EngineerRole@RobotEngineeringContext` and `MusicianRole@MusicPracticeContext`. If the engineering work is specifically robotics engineering, use a role qualifier, RoleDescription, or A.2.7 role-relation expression rather than minting `EngineerRoboticistRole` automatically.
* If "robotics engineer" is a stable local bundle or qualification relation, record it as `RoleRelationStructure@BoundedContext` under A.2.7. The relation structure may be named for local use, but it is not a new role value by itself.
* Recover method and work values separately: engineering method, robotics-engineering method family, music teaching method, robot-training work, and performed music work stay under the method and work patterns. They may motivate a role name only after F.8 and F.18 admission.
* A durable role value is selected only when the bounded context needs different assignment predicates, capability expectations, incompatibilities, method/work implications, or public naming. Otherwise keep the ordinary composite phrase and cite the recovered role relation, method, work, and capability values where they matter.

